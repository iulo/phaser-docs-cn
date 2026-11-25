# SubmitterSpriteGPULayer {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-submitterspritegpulayer)

这个 RenderNode 处理单个 SpriteGPULayer 对象的渲染。 每个 SpriteGPuLayer 对象应该创建一个新 RenderNode, 因为它存储对象的遮蔽程序和顶点缓冲数据 。

它是Stand-Alone Render节点,意思是它不与其他对象进行批量,最适合渲染高度复杂的GPU驱动的图样层.

**构造函数**

`new SubmitterSpriteGPULayer(manager, config, gameObject)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | [Phaser.Types.Renderer.WebGL.RenderNodes.SubmitterSpriteGPULayerConfig](/api/typedef/types-renderer-webgl-rendernodes#submitterspritegpulayerconfig) | 否 | 此处理器的配置对象 。 |
| gameObject | [Phaser.GameObjects.SpriteGPULayer](/api/class/gameobjects-spritegpulayer) | 否 | 要渲染的 SpriteGPULayer 对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L29](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L29)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### _calcMatrix {#_calcMatrix}

#### _calcMatrix: [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) {#_calcmatrix-phasergameobjectscomponentstransformmatrix}


**说明:**

用于临时计算的一个矩阵。


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L155](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L155)  
引入版本：4.0.0


---

### config {#config}

#### config: object {#config-object}


**说明:**

此 RenderNode 已完成的配置对象。 这是由默认配置和用户定义的配置对象定义的 。


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L60)  
引入版本：4.0.0


---

### defaultConfig {#defaultConfig}

#### defaultConfig: object {#defaultconfig-object}


**说明:**

此 Render 节点的默认配置 。


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L175](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L175)  
引入版本：4.0.0


---

### gameObject {#gameObject}

#### gameObject: [Phaser.GameObjects.SpriteGPULayer](/api/class/gameobjects-spritegpulayer) {#gameobject-phasergameobjectsspritegpulayer}


**说明:**

SpriteGPULayer 游戏对象 此 RenderNode 正在渲染 。


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L70)  
引入版本：4.0.0


---

### instanceBufferLayout {#instanceBufferLayout}

#### instanceBufferLayout: [Phaser.Renderer.WebGL.Wrappers.WebGLVertexBufferLayoutWrapper](/api/class/renderer-webgl-wrappers-webglvertexbufferlayoutwrapper) {#instancebufferlayout-phaserrendererwebglwrapperswebglvertexbufferlayoutwrapper}


**说明:**

此 Render 节点的实例缓冲布局 。


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L80)  
引入版本：4.0.0


---

### programManager {#programManager}

#### programManager: [Phaser.Renderer.WebGL.ProgramManager](/api/class/renderer-webgl-programmanager) {#programmanager-phaserrendererwebglprogrammanager}


**说明:**

程序管理器用来创建和管理遮荫程序。 包含遮荫变体 。


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L119)  
引入版本：4.0.0


---

### vertexBufferLayout {#vertexBufferLayout}

#### vertexBufferLayout: [Phaser.Renderer.WebGL.Wrappers.WebGLVertexBufferLayoutWrapper](/api/class/renderer-webgl-wrappers-webglvertexbufferlayoutwrapper) {#vertexbufferlayout-phaserrendererwebglwrapperswebglvertexbufferlayoutwrapper}


**说明:**

此 RenderNode 的顶点缓冲布局 。

由4字节,0-3组成一个四实例的角.


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L94](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L94)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### _completeLayout {#_completeLayout}

#### \<instance> _completeLayout(config) {#instance-_completelayoutconfig}


**说明:**

需要时用默认值填充配置对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | object | 否 | 要完成的配置对象 。 |


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L287](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L287)  
引入版本：4.0.0


---

### run {#run}

#### \<instance> run(drawingContext) {#instance-rundrawingcontext}


**说明:**

将 SpriteGPULayer 对象渲染成 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L528](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L528)  
引入版本：4.0.0


---

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(drawingContext) {#instance-setupuniformsdrawingcontext}


**说明:**

上传当前渲染通道所需的所有遮阳器制服。 其中包括摄像机投影和视图矩阵、 渲染分辨率、 像素圆形、 滚动抵消、 过期时间、 散射和帧数据纹理分辨率、 重力、 纹理采样器绑定, 如果层上启用照明, 以及照明制服 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L373](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L373)  
引入版本：4.0.0


---

### updateRenderOptions {#updateRenderOptions}

#### \<instance> updateRenderOptions() {#instance-updaterenderoptions}


**说明:**

根据SpriteGPULayer游戏对象的当前状态更新着色器程序选项。启用或禁用照明阴影添加,设置活动光线计数定义,配置平滑像素艺术渲染,并应用游戏对象报告的任何阴影特性,包括自我阴影支持.


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L471](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterSpriteGPULayer.js#L471)  
引入版本：4.0.0


---

---
