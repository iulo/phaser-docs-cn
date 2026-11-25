# Phaser.Types.GameObjects {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/types-gameobjects)

Scope: 
static
> 源码：[src/gameobjects/typedefs/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/typedefs/index.js#L7)  


## 静态函数 {#static-functions}

- [BitmapText](/api/namespace/types-gameobjects-bitmaptext)
- [Container](/api/namespace/types-gameobjects-container)
- [Gradient](/api/namespace/types-gameobjects-gradient)
- [Graphics](/api/namespace/types-gameobjects-graphics)
- [Group](/api/namespace/types-gameobjects-group)
- [NineSlice](/api/namespace/types-gameobjects-nineslice)
- [Noise](/api/namespace/types-gameobjects-noise)
- [NoiseCell2D](/api/namespace/types-gameobjects-noisecell2d)
- [NoiseCell3D](/api/namespace/types-gameobjects-noisecell3d)
- [NoiseCell4D](/api/namespace/types-gameobjects-noisecell4d)
- [NoiseSimplex2D](/api/namespace/types-gameobjects-noisesimplex2d)
- [NoiseSimplex3D](/api/namespace/types-gameobjects-noisesimplex3d)
- [Particles](/api/namespace/types-gameobjects-particles)
- [PathFollower](/api/namespace/types-gameobjects-pathfollower)
- [RenderTexture](/api/namespace/types-gameobjects-rendertexture)
- [Rope](/api/namespace/types-gameobjects-rope)
- [Shader](/api/namespace/types-gameobjects-shader)
- [Sprite](/api/namespace/types-gameobjects-sprite)
- [SpriteGPULayer](/api/namespace/types-gameobjects-spritegpulayer)
- [Text](/api/namespace/types-gameobjects-text)
- [TileSprite](/api/namespace/types-gameobjects-tilesprite)
- [Video](/api/namespace/types-gameobjects-video)
- [Zone](/api/namespace/types-gameobjects-zone)
## 静态函数 {#static-functions-1}

### DecomposeMatrixResults {#DecomposeMatrixResults}

#### DecomposeMatrixResults {#decomposematrixresults}


> 源码：[src/gameobjects/typedefs/DecomposeMatrixResults.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/typedefs/DecomposeMatrixResults.js#L1)  
引入版本：3.60.0


---

### FiltersInternalExternal {#FiltersInternalExternal}

#### FiltersInternalExternal {#filtersinternalexternal}


> 源码：[src/gameobjects/typedefs/FiltersInternalExternal.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/typedefs/FiltersInternalExternal.js#L1)  
引入版本：4.0.0


---

### GameObjectConfig {#GameObjectConfig}

#### GameObjectConfig {#gameobjectconfig}


> 源码：[src/gameobjects/typedefs/GameObjectConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/typedefs/GameObjectConfig.js#L1)  
引入版本：3.0.0


---

### GetCalcMatrixResults {#GetCalcMatrixResults}

#### GetCalcMatrixResults {#getcalcmatrixresults}


> 源码：[src/gameobjects/typedefs/GetCalcMatrixResults.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/typedefs/GetCalcMatrixResults.js#L1)  
引入版本：3.50.0


---

### JSONGameObject {#JSONGameObject}

#### JSONGameObject {#jsongameobject}


> 源码：[src/gameobjects/typedefs/JSONGameObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/typedefs/JSONGameObject.js#L1)  
引入版本：3.0.0


---

### RenderWebGLStep {#RenderWebGLStep}

#### RenderWebGLStep {#renderwebglstep}


**说明:**

在一个给定的游戏对象上执行渲染操作的函数。 通常这是游戏对象本身的 `renderWebGL` 方法, 但是 `Phaser.GameObjects.Components.RenderSteps` 允许您定义一系列按顺序运行的步骤。 该函数不会在任何特定范围内运行, 因此它不应该使用 `this` 。 相反, 所有所需的属性都应该通过 `gameObject` 访问 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 |  | 参考当前活动WebGL渲染器. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 此调用中正在提供游戏对象 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 |  | 当前绘图背景 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 |  | 如果游戏对象被嵌入, 此变换矩阵将定义 |
| renderStep | number | 是 | 0 | 游戏对象渲染过程列表中此函数的索引。 用于支持多个渲染函数 。 |
| displayList | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 是 |  | 目前正在提供的显示列表 。 |
| displayListIndex | number | 是 |  | 显示列表中的游戏对象索引 。 |


**返回值:** void - 


> 源码：[src/gameobjects/typedefs/RenderWebGLStep.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/typedefs/RenderWebGLStep.js#L1)  
引入版本：4.0.0


---

---
