# Phaser.GameObjects {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects)

Scope: 
static
> 源码：[src/gameobjects/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/index.js#L7)  


## 静态函数 {#static-functions}

- [Arc](/api/class/gameobjects-arc)
- [BitmapText](/api/class/gameobjects-bitmaptext)
- [Blitter](/api/class/gameobjects-blitter)
- [Bob](/api/class/gameobjects-bob)
- [CaptureFrame](/api/class/gameobjects-captureframe)
- [Container](/api/class/gameobjects-container)
- [Curve](/api/class/gameobjects-curve)
- [DisplayList](/api/class/gameobjects-displaylist)
- [DOMElement](/api/class/gameobjects-domelement)
- [DynamicBitmapText](/api/class/gameobjects-dynamicbitmaptext)
- [Ellipse](/api/class/gameobjects-ellipse)
- [Extern](/api/class/gameobjects-extern)
- [GameObject](/api/class/gameobjects-gameobject)
- [GameObjectCreator](/api/class/gameobjects-gameobjectcreator)
- [GameObjectFactory](/api/class/gameobjects-gameobjectfactory)
- [Gradient](/api/class/gameobjects-gradient)
- [Graphics](/api/class/gameobjects-graphics)
- [Grid](/api/class/gameobjects-grid)
- [Group](/api/class/gameobjects-group)
- [Image](/api/class/gameobjects-image)
- [IsoBox](/api/class/gameobjects-isobox)
- [IsoTriangle](/api/class/gameobjects-isotriangle)
- [Layer](/api/class/gameobjects-layer)
- [Light](/api/class/gameobjects-light)
- [LightsManager](/api/class/gameobjects-lightsmanager)
- [LightsPlugin](/api/class/gameobjects-lightsplugin)
- [Line](/api/class/gameobjects-line)
- [NineSlice](/api/class/gameobjects-nineslice)
- [NineSliceVertex](/api/class/gameobjects-nineslicevertex)
- [Noise](/api/class/gameobjects-noise)
- [NoiseCell2D](/api/class/gameobjects-noisecell2d)
- [NoiseCell3D](/api/class/gameobjects-noisecell3d)
- [NoiseCell4D](/api/class/gameobjects-noisecell4d)
- [NoiseSimplex2D](/api/class/gameobjects-noisesimplex2d)
- [NoiseSimplex3D](/api/class/gameobjects-noisesimplex3d)
- [PathFollower](/api/class/gameobjects-pathfollower)
- [PointLight](/api/class/gameobjects-pointlight)
- [Polygon](/api/class/gameobjects-polygon)
- [Rectangle](/api/class/gameobjects-rectangle)
- [RenderTexture](/api/class/gameobjects-rendertexture)
- [Rope](/api/class/gameobjects-rope)
- [Shader](/api/class/gameobjects-shader)
- [Shape](/api/class/gameobjects-shape)
- [Sprite](/api/class/gameobjects-sprite)
- [SpriteGPULayer](/api/class/gameobjects-spritegpulayer)
- [Stamp](/api/class/gameobjects-stamp)
- [Star](/api/class/gameobjects-star)
- [Text](/api/class/gameobjects-text)
- [TextStyle](/api/class/gameobjects-textstyle)
- [TileSprite](/api/class/gameobjects-tilesprite)
- [Triangle](/api/class/gameobjects-triangle)
- [UpdateList](/api/class/gameobjects-updatelist)
- [Video](/api/class/gameobjects-video)
- [Zone](/api/class/gameobjects-zone)
## 静态函数 {#static-functions-1}

- [Components](/api/namespace/gameobjects-components)
- [Events](/api/namespace/gameobjects-events)
- [Particles](/api/namespace/gameobjects-particles)
- [RetroFont](/api/namespace/gameobjects-retrofont)
## 静态函数 {#static-functions-2}

### BuildGameObject {#BuildGameObject}

#### \<static> BuildGameObject(scene, gameObject, config) {#static-buildgameobjectscene-gameobject-config}


**说明:**

使用提供的配置对象构建游戏对象, 应用诸如位置、 深度、 翻转、 尺度、 滚动因子、 旋转、 α、 来源、 混合模式、 和可见度等属性。 如果配置的 `add` 属性是 `true`( 默认) , 游戏对象会被添加到 Scene 显示列表中。 如果游戏对象有 `preUpdate` 方法, 也会被添加到 Scene的更新列表中。 此功能由 Game Object 工厂和创建者内部使用, 一般不直接使用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 参考景区. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 初游戏对象. |
| config | [Phaser.Types.GameObjects.GameObjectConfig](/api/typedef/types-gameobjects#gameobjectconfig) | 否 | 用于构建游戏对象的配置 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已建游戏对象.


> 源码：[src/gameobjects/BuildGameObject.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/BuildGameObject.js#L10)  
引入版本：3.0.0


---

### BuildGameObjectAnimation {#BuildGameObjectAnimation}

#### \<static> BuildGameObjectAnimation(sprite, config) {#static-buildgameobjectanimationsprite-config}


**说明:**

从游戏对象配置对象读取 `anims` 属性,并使用它来配置给定的Sprite 的动画状态。如果 `anims` 属性不存在,则Sprite 返回时不变 。

电话 `anims` 值可以是字符串或对象。如果是字符串,则它被当作动画键,动画立即播放。如果是对象,则动画键和回放选项(例如: `delay`, `repeat`, `yoyo`,和 `startFrame`)从中读取。 `play` 财务报告和已审计财务报表 `delayedPlay` 属性,动画会立即播放,在延迟后播放,或者只是装入准备稍后播放。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sprite | [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) | 否 | 将配置动画状态的 Sprite 。 |
| config | object | 否 | 游戏对象配置对象。 此对象的 `anims` 属性用于配置动画 。 |


**返回值:** [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) - 更新的Sprite( 斯普拉蒂 ).


> 源码：[src/gameobjects/BuildGameObjectAnimation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/BuildGameObjectAnimation.js#L9)  
引入版本：3.0.0


---

### GetCalcMatrix {#GetCalcMatrix}

#### \<static> GetCalcMatrix(src, camera, [parentMatrix], [ignoreCameraPosition]) {#static-getcalcmatrixsrc-camera-parentmatrix-ignorecameraposition}


**说明:**

计算给定的游戏对象和相机的变换矩阵,如果提供的话,在母矩阵中计算。

注意此结果包含 _References_ to the Transform Matrices,而不是新实例。因此,您应该立即使用它们的值,或者将其复制到自己的矩阵中,因为一旦推出另一个游戏对象,它们就会被替换 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| src | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 计算变换矩阵的游戏对象 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 用于渲染游戏对象的相机 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 |  | 母容器的变换矩阵,如果有的话。 |
| ignoreCameraPosition | boolean | 是 | false | 相机的翻译是否应当忽略? 这就是在屏幕上移动相机的原因, 但是当相机被传送到帧缓冲器时, 却应该忽略它 。 |


**返回值:** [Phaser.Types.GameObjects.GetCalcMatrixResults](/api/typedef/types-gameobjects#getcalcmatrixresults) - 包含更新的变换矩阵的结果对象.


> 源码：[src/gameobjects/GetCalcMatrix.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GetCalcMatrix.js#L21)  
引入版本：3.50.0


---

### GetTextSize {#GetTextSize}

#### \<static> GetTextSize(text, size, lines) {#static-gettextsizetext-size-lines}


**说明:**

计算并返回文本对象的已渲染尺寸,包括每行宽度、最大线宽度、总高度(计算行距)和绘图线数(尊重`maxLines`)。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| text | [Phaser.GameObjects.Text](/api/class/gameobjects-text) | 否 | 计算大小的文本对象。 |
| size | [Phaser.Types.GameObjects.Text.TextMetrics](/api/typedef/types-gameobjects-text#textmetrics) | 否 | 计算大小时使用的文本度量。 |
| lines | Array.\<string> | 否 | 用来计算大小的文字线条。 |


**返回值:** [Phaser.Types.GameObjects.Text.GetTextSizeObject](/api/typedef/types-gameobjects-text#gettextsizeobject) - 包含文本对象尺寸的天体。


> 源码：[src/gameobjects/text/GetTextSize.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/GetTextSize.js#L7)  
引入版本：3.0.0


---

### MeasureText {#MeasureText}

#### \<static> MeasureText(textStyle) {#static-measuretexttextstyle}


**说明:**

通过将文本渲染到一个临时的屏幕外布上并测量像素边界来计算给定的文本Style的升空、降空和fontSize的度量。它使用`actualBoundingBoxAscent`/`actualBoundingBoxDescent` API(如果有的话),回到旧浏览器的像素扫描方法。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| textStyle | [Phaser.GameObjects.TextStyle](/api/class/gameobjects-textstyle) | 否 | 文本样式对象可以测量 。 |


**返回值:** [Phaser.Types.GameObjects.Text.TextMetrics](/api/typedef/types-gameobjects-text#textmetrics) - 包含文本样式的升降、降降和fontSize的天体。


> 源码：[src/gameobjects/text/MeasureText.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/MeasureText.js#L9)  
引入版本：3.0.0


---

---
