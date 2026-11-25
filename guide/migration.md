# 从 Phaser 3 迁移到 Phaser 4

这篇指南涵盖将 Phaser 3 项目升级到 Phaser 4 时需要做的改动。章节按影响从大到小排列，可以依次检查。

译自 Phaser v4.2.1 的[迁移指南](https://github.com/phaserjs/phaser/blob/41be1e462bc600064e498cba370bfa8c5c055a22/changelog/v4/4.0/MIGRATION-GUIDE.md)。[上游 MIT 许可证](/license.txt)

## 1. 渲染器从管线改为渲染节点 {#1-renderer-pipelines-to-render-nodes}

Phaser 4 引入了全新的 WebGL 渲染器，替换了 Phaser 3 的整条渲染管线。这是 v4 最大的变化。

旧的 `Pipeline` 系统已移除。管线往往身兼多项职责，例如 Utility 管线会处理多种渲染任务。每条管线都要独立管理 WebGL 状态，一条管线可能破坏另一条管线所依赖的状态。

新的 `RenderNode` 架构让每个渲染节点负责一项渲染任务，便于维护。所有渲染节点都有 `run` 方法，部分节点还有 `batch` 方法，用于在调用 `run` 前汇集多个来源的状态。

- 只使用标准 Phaser API（如 Sprite、Text 或 Tilemap）的游戏通常可以直接使用新渲染器。
- 用过**自定义 WebGL 管线**的项目需要将其重写为渲染节点。使用 `RenderConfig#renderNodes` 在启动时注册自定义节点。
- 如果直接访问过 `WebGLRenderer` 的内部实现，注意以下变更。
  - `WebGLRenderer.textureIndexes` 已移除，改用 `glTextureUnits.unitIndices`。
  - `WebGLRenderer#genericVertexBuffer` 和 `#genericVertexData` 已移除，节省约 16 MB RAM/VRAM。`BatchHandler` 渲染节点现在自行创建 WebGL 数据缓冲区。
  - `WebGLAttribLocationWrapper` 已移除。
- 在 Phaser 4 游戏中直接调用 WebGL 的 `gl` 方法，会修改底层状态而不更新内部的 `WebGLGlobalWrapper`，可能导致不可预测的行为。需要直接访问 WebGL 时，使用 `Extern` 游戏对象，它会在完成后重置状态。

## 2. Canvas 渲染器已弃用 {#2-canvas-renderer-deprecated}

Canvas 渲染器仍然可用，但已弃用。Phaser 4 的高级渲染功能依赖 WebGL 技术，Canvas 无法提供这些功能。如今 WebGL 已基本普及，建议新项目使用 WebGL。

Canvas 仍有一项优势，支持 27 种混合模式，而 WebGL 原生提供 NORMAL、ADD、MULTIPLY 和 SCREEN 四种模式。Phaser 4 的 `Blend` 滤镜能在 WebGL 中复现所有 Canvas 混合模式，需要通过 `CaptureFrame`、`DynamicTexture` 或类似对象间接实现。

## 3. FX 和遮罩统一为滤镜 {#3-fx-and-masks-are-now-filters}

对于依赖 FX 或遮罩系统的 Phaser 3 项目，这是影响最大的改动之一。原来的前置、后置 FX 和遮罩统一到了 **Filter（滤镜）** 系统。滤镜接收输入图像并输出图像，通常使用单个着色器。各种滤镜可以相互配合。

- **前置和后置 FX 合并。** 滤镜分为 `internal`（只影响对象本身）和 `external`（影响对象所在的渲染上下文，通常是全屏）两个列表。
- **适用对象扩大。** Phaser 3 只有部分对象支持 FX，Phaser 4 可对任意游戏对象或场景摄像机应用滤镜，包括 `Extern` 对象。
- **`BitmapMask` 已移除。** 改用 `Mask` 滤镜。`GeometryMask` 仅在 Canvas 中保留。

| Phaser 3 FX | Phaser 4 替代方案 |
|---|---|
| `Bloom` | `Phaser.Actions.AddEffectBloom()` |
| `Shine` | `Phaser.Actions.AddEffectShine()` |
| `Circle` | `Phaser.Actions.AddMaskShape()` |
| `Gradient` | `Gradient` 游戏对象 |

`ColorMatrix` 滤镜的颜色处理方法移到了 `colorMatrix` 属性上。

```js
// v3
colorMatrix.sepia();

// v4
colorMatrix.colorMatrix.sepia();
```

将位图遮罩改为 Mask 滤镜。

```js
// v3 - BitmapMask
const mask = new Phaser.Display.Masks.BitmapMask(scene, maskObject);
sprite.setMask(mask);

// v4 - Mask filter
sprite.filters.internal.addMask(maskObject);
```

## 4. 着色系统 {#4-tint-system}

着色（Tint）系统更新了 API，并增加了混合模式。`tintFill` 属性和 `setTintFill()` 方法已移除。使用 `tintMode` 或 `setTintMode()` 控制着色混合方式。`Phaser.TintModes` 支持 `MULTIPLY`、`FILL`、`ADD`、`SCREEN`、`OVERLAY` 和 `HARD_LIGHT`。

```js
// v3
sprite.setTintFill(0xff0000);

// v4
sprite.setTint(0xff0000).setTintMode(Phaser.TintModes.FILL);
```

- `tint` 和 `setTint()` 现在只设置颜色。Phaser 3 中调用它们会隐式关闭填充模式。
- FILL 模式现在能正确处理半透明像素。
- BitmapText 现在能正确应用着色。

## 5. 摄像机系统 {#5-camera-system}

摄像机矩阵系统已重写。只使用标准属性（`scrollX`、`scrollY`、`zoom` 和 `rotation`）的代码通常可以直接运行。直接访问摄像机矩阵的代码则需要更新。

| Phaser 3 | Phaser 4 |
|---|---|
| `Camera#matrix` = 位置 + 旋转 + 缩放 | `Camera#matrix` = 旋转 + 缩放 + 滚动 |
| 滚动单独附加 | 滚动包含在 `Camera#matrix` 中 |
| 无对应项 | `Camera#matrixExternal` = 仅包含位置 |
| 无对应项 | `Camera#matrixCombined` = `matrix` × `matrixExternal` |

手动处理滚动因子时，按下面的方式迁移。

```js
// v3
spriteMatrix.e -= camera.scrollX * src.scrollFactorX;

// v4
TransformMatrix.copyWithScrollFactorFrom(matrix, scrollX, scrollY, scrollFactorX, scrollFactorY);
```

- `GetCalcMatrix()` 新增了 `ignoreCameraPosition` 参数。
- `GetCalcMatrixResults` 新增了 `matrixExternal` 属性。

## 6. 纹理坐标和 GL 方向 {#6-texture-coordinates-and-gl-orientation}

Phaser 3 的纹理以左上角为原点，和内部帧缓冲区的绘制方向不一致，因此需要翻转。Phaser 4 统一使用 GL 方向，`Y = 0` 在底部。

- **压缩纹理**需要重新压缩，使 Y 轴从底部向上递增。纹理压缩工具通常提供「翻转 Y 轴」选项。
- PNG、JPG 等普通图像纹理由引擎自动处理。
- 编写自定义着色器时，纹理坐标采用 GL 约定，`Y = 0` 对应图像底部。

## 7. DynamicTexture 和 RenderTexture {#7-dynamictexture-and-rendertexture}

Phaser 3 的 `DynamicTexture` 可以直接定义批次并执行复杂的绘制操作。Phaser 4 移除了许多此类方法，改由标准渲染系统自动处理批次。

**破坏性变更。** `DynamicTexture` 和 `RenderTexture` 现在需要调用 `render()` 才会执行缓冲区中的绘制命令。此前绘制命令会立即执行。

- `DynamicTexture#preserve()` 在渲染后保留命令缓冲区便于复用，可以用同一批命令重新渲染有变化的游戏对象。
- `DynamicTexture#callback()` 插入一个回调，在执行命令缓冲区时调用。
- `DynamicTexture#capture` 会捕获当前摄像机的视图，因此比 `draw` 更准确地渲染游戏对象。
- `RenderTexture.renderMode` 支持 `"render"`（像 Image 一样绘制）、`"redraw"`（在渲染循环中更新纹理，无画面输出）和 `"all"`（两者都执行）。`"redraw"` 可在渲染循环中途更新纹理，让着色器在同一帧使用结果。
- `TextureManager#addDynamicTexture` 新增 `forceEven` 参数。

## 8. Shader API {#8-shader-api}

`Shader` 游戏对象经过大量重写，原来的 Phaser 3 着色器需要更新。

- 构造函数现在接收一个配置对象（`ShaderQuadConfig`）。
- 分辨率、时间等 Shadertoy 风格的 uniform 需要在配置中按需设置。
- 纹理坐标遵循 GL 约定，`Y = 0` 位于底部。
- `Shader#setUniform(name, value)` 可逐个设置程序的 uniform。
- `Shader#renderImmediate` 可在常规渲染循环之外执行渲染。

## 9. 加载 GLSL {#9-glsl-loading}

- 加载时不再区分片元和顶点 GLSL。同一段代码可以用于其中一种着色器或两种都用。分别加载相应的着色器代码，在创建 Shader 时组合。
- 自定义模板语法由 `#pragma` 预处理指令替代。这些指令是合法的 GLSL，兼容自动语法检查，并在编译前移除。

## 10. 光照 {#10-lighting}

光照的用法更简单，功能也有所扩展。

```js
// v3 - Pipeline-based lighting
sprite.setPipeline('Light2D');

// v4 - Simple method call
sprite.setLighting(true);
```

- BitmapText、Blitter、Graphics、Shape、Image、Sprite、Particles、SpriteGPULayer、Stamp、Text、TileSprite、Video、TilemapLayer 和 TilemapGPULayer 都可以使用光照。
- 对象现在可以投射**自阴影**。着色器根据纹理亮度模拟表面细节产生的阴影，可全局或按对象配置。
- 光源用 `z` 明确设置高度。Phaser 3 的光源高度由游戏分辨率隐式决定。
- 光照会更改着色器，从而断开渲染批次。
- `ImageLight` 滤镜也可以实现基于图像的光照，使用的是独立于核心光照系统的机制。

## 11. TileSprite {#11-tilesprite}

TileSprite 的内部实现已重写。新的着色器自行控制纹理坐标的环绕方式。

- `TileSprite` 已取消纹理裁剪支持。
- 现在分别为宽和高设置默认值。
- 支持重复纹理图集和精灵表中的**纹理帧**。Phaser 3 只能重复整张纹理。
- 新增 `tileRotation` 属性，用于旋转重复纹理。
- 现在能正确处理压缩纹理、尺寸为非二次幂的纹理和 DynamicTexture。

## 12. Graphics 和 Shape {#12-graphics-and-shape}

- `Graphics` 新增了 `pathDetailThreshold` 属性。也可通过游戏配置设置。它会跳过间距小于阈值的顶点，提升小范围复杂曲线的绘制性能。
- `Grid` 的属性从 `outline` 改名为 `stroke`，与其他 Shape 对象保持一致。新增的控制项可以设置单元格间隔，以及是否绘制网格外缘或仅绘制单元格间的描边。
- `Rectangle` 现在支持圆角。

## 13. 几何类型 Point 迁移到 Vector2 {#13-geometry-point-replaced-by-vector2}

`Geom.Point` 和所有相关函数都已移除，改用 `Vector2`。

| Phaser 3（`Point`） | Phaser 4（`Vector2` / `Math`） |
|---|---|
| `Point.Ceil` | `Vector2.ceil` |
| `Point.Floor` | `Vector2.floor` |
| `Point.Clone` | `Vector2.clone` |
| `Point.CopyFrom(src, dest)` | `dest.copy(src)` |
| `Point.Equals` | `Vector2.equals` |
| `Point.GetCentroid` | `Math.GetCentroid` |
| `Point.GetMagnitude` | `Vector2.length` |
| `Point.GetMagnitudeSq` | `Vector2.lengthSq` |
| `Point.Invert` | `Vector2.invert` |
| `Point.Negative` | `Vector2.negate` |
| `Point.SetMagnitude` | `Vector2.setLength` |
| `Point.Project` | `Vector2.project` |
| `Point.ProjectUnit` | `Vector2.projectUnit` |
| `Point.Interpolate` | `Math.LinearXY` |
| `Point.GetRectangleFromPoints` | `Math.GetVec2Bounds` |

以下几何类及其相关辅助函数（`getPoint`、`getPoints`、`getRandomPoint`、`CircumferencePoint` 和 `Random` 等）现在返回 `Vector2` 实例。

- `Geom.Circle`
- `Geom.Ellipse`
- `Geom.Line`
- `Geom.Polygon`
- `Geom.Rectangle`
- `Geom.Triangle`

把 `instanceof Phaser.Geom.Point` 检查改为 `instanceof Phaser.Math.Vector2`。

## 14. 数学常量 {#14-math-constants}

| Phaser 3 | Phaser 4 | 说明 |
|---|---|---|
| `Math.TAU`（π / 2） | `Math.TAU`（π × 2） | 值已变更，使用数学上正确的 τ。 |
| `Math.PI2` | 已移除 | 改用 `Math.TAU`。 |
| 无对应项 | `Math.PI_OVER_2` | π / 2 的新常量，对应 Phaser 3 中错误命名的 `TAU`。 |

如果旧代码用 `Math.TAU` 表示 π / 2，迁移到 `Math.PI_OVER_2`。如果用 `Math.PI2` 表示 π × 2，迁移到 `Math.TAU`。

## 15. 数据结构 {#15-data-structures}

`Phaser.Struct.Set` 由 JavaScript 原生 `Set` 取代。`iterateLocal` 等方法已移除，使用标准的 `forEach`、`has`、`add`、`delete` 等方法。

`Phaser.Struct.Map` 由 JavaScript 原生 `Map` 取代。`contains`、`setAll` 等方法已移除，使用标准的 `has`、`get`、`set`、`delete` 等方法。

## 16. 像素取整 {#16-round-pixels}

游戏配置项 `roundPixels` 现默认为 `false`，Phaser 3 默认为 `true`。取整仅在对象与坐标轴对齐且未缩放时生效，以免变换引发闪烁。

可用 `GameObject#vertexRoundMode` 单独控制每个对象。

| 值 | 行为 |
|---|---|
| `"off"` | 始终关闭取整。 |
| `"safe"` | 只有平移时才取整。 |
| `"safeAuto"`（默认） | 与 `"safe"` 类似，同时要求摄像机开启 `roundPixels`。 |
| `"full"` | 始终取整，可能导致旋转中的 Sprite 出现类似 PS1 的抖动。 |
| `"fullAuto"` | 与 `"full"` 类似，同时要求摄像机开启 `roundPixels`。 |

`TransformMatrix#setQuad` 已移除 `roundPixels` 参数。

## 17. 已移除的游戏对象 {#17-removed-game-objects}

- **`Mesh` 和 `Plane`** 已移除。这两个对象提供的 3D 功能有限，完整的 3D 支持留待未来实现。

## 18. 已移除的插件和入口 {#18-removed-plugins-and-entry-points}

- Camera3D 插件
- Layer3D 插件
- Facebook 插件检测常量
- `phaser-ie9.js` 入口（已停止支持 IE9）

## 19. 已移除的工具和 Polyfill {#19-removed-utilities-and-polyfills}

`Create.GenerateTexture`、所有 Create Palettes 和 `create` 目录已移除，`TextureManager.generate` 也随之移除。`Math.SinCosTableGenerator` 同样已移除。

现代浏览器已原生提供相应能力，以下旧版 Polyfill 已移除。

- `Array.forEach`
- `Array.isArray`
- `AudioContextMonkeyPatch`
- `console`
- `Math.trunc`
- `performance.now`
- `requestAnimationFrame`
- `Uint32Array`

## 20. Spine 插件 {#20-spine-plugins}

Phaser 原先附带的 Spine 3 和 Spine 4 插件已停止更新。改用 Esoteric Software 发布的官方 Phaser Spine 插件。

## 21. 其他破坏性变更 {#21-miscellaneous-breaking-changes}

- **`Shader#setTextures()`** 现在会替换整个纹理数组。如果此前通过多次调用来逐项添加纹理，请改为传入完整数组，一次设置。
- **`DOMElement`** 缺少容器时会抛错。确保 DOM 元素有父容器。
- 即使场景光照管理器未启用，也可以设置 **`GameObject#enableLighting`**。实际渲染灯光仍需启用管理器。
- 游戏手柄的 **`Button` 类**新增 `isPressed` 参数，用于在切换场景时正确初始化按钮状态。
- **`BatchHandlerConfig#createOwnVertexBuffer`** 类型属性已移除。
- **`WebGLRenderer#genericVertexBuffer`** 和 **`#genericVertexData`** 已移除，节省约 16 MB RAM/VRAM。

## 迁移检查清单 {#migration-checklist}

- [ ] 执行 `npm install phaser@4` 或使用等效的包管理命令。
- [ ] 将自定义 WebGL 管线改写为渲染节点。
- [ ] 将 `BitmapMask` 替换为 `Mask` 滤镜。
- [ ] 将已移除的 `Bloom`、`Shine`、`Circle`、`Gradient` FX 换成对应 Action 或游戏对象。
- [ ] 将 `ColorMatrix` 的颜色处理方法改为在 `.colorMatrix` 属性上调用。
- [ ] 用 `setTint().setTintMode(Phaser.TintModes.FILL)` 替换 `setTintFill()`。
- [ ] 将 `Geom.Point` 替换为 `Vector2`。
- [ ] 核对 `Math.TAU` 的用法，现为 π × 2。
- [ ] 将 `Math.PI2` 替换为 `Math.TAU`。
- [ ] 将 `Phaser.Struct.Set` 替换为原生 `Set`。
- [ ] 将 `Phaser.Struct.Map` 替换为原生 `Map`。
- [ ] 在使用 `DynamicTexture` 和 `RenderTexture` 的地方添加 `render()` 调用。
- [ ] 按新的 Y 轴方向重新压缩纹理。
- [ ] 更新直接访问 `Camera#matrix` 的逻辑，使之适配新矩阵系统。
- [ ] 更新 `Shader` 游戏对象的构造方式，使用 `ShaderQuadConfig`。
- [ ] 更新 GLSL 加载与模板语法，按需组合 GLSL 文件并使用 `#pragma`。
- [ ] 将 `sprite.setPipeline('Light2D')` 替换为 `sprite.setLighting(true)`。
- [ ] 使用新的 `z` 属性设置光源高度。
- [ ] 移除 `TileSprite` 的纹理裁剪代码。
- [ ] 将 `Grid` 的 `outline` 属性改为 `stroke`。
- [ ] 移除 `Mesh` 或 `Plane` 的用法。
- [ ] 将原先 Phaser 附带的 Spine 插件替换为 Esoteric Software 的官方插件。
- [ ] 清除对 `Create.GenerateTexture` 或 `TextureManager.generate` 的依赖。
- [ ] 验证 `roundPixels` 行为，现默认为 `false`。
- [ ] 移除对已删除的 Polyfill、插件或入口的依赖。
- [ ] 检查自定义着色器的纹理坐标，`Y = 0` 现位于底部。
