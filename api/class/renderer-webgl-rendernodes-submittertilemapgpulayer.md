# SubmitterTilemapGPULayer {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-submittertilemapgpulayer)

提交器TilemapGPULayer RenderNode处理WebGL渲染器中TilemapGPULayER天体的GPU加速渲染.

与基于批量的提交者不同, 这是 Stand Onely Render, 意思是每个层都是在自己的绘图调用中绘制的。 它通过程序管理程序来管理自己的着色器程序, 它支持多个可选的阴影特性, 包括平滑像素艺术的提升, 正常的映射照明, 动画瓦, 自阴影, 以及双线边框过滤。 适当的阴影变体是根据层的配置选择的 。

**构造函数**

`new SubmitterTilemapGPULayer(manager, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerConfig](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerconfig) | 是 | 此处理器的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L23](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L23)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### config {#config}

#### config: object {#config-object}


**说明:**

此 RenderNode 已完成的配置对象。 这是由默认配置和用户定义的配置对象定义的 。


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L56)  
引入版本：4.0.0


---

### defaultConfig {#defaultConfig}

#### defaultConfig: [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerConfig](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerconfig) {#defaultconfig-phasertypesrendererwebglrendernodesbatchhandlerconfig}


**说明:**

此 Render 节点的默认配置 。


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L168](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L168)  
引入版本：4.0.0


---

### indexBuffer {#indexBuffer}

#### indexBuffer: [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) {#indexbuffer-phaserrendererwebglwrapperswebglbufferwrapper}


**说明:**

索引缓冲定义顶点顺序.


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L66)  
引入版本：4.0.0


---

### programManager {#programManager}

#### programManager: [Phaser.Renderer.WebGL.ProgramManager](/api/class/renderer-webgl-programmanager) {#programmanager-phaserrendererwebglprogrammanager}


**说明:**

程序管理器用来创建和管理遮荫程序。 包含遮荫变体 。


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L91)  
引入版本：4.0.0


---

### vertexBufferLayout {#vertexBufferLayout}

#### vertexBufferLayout: [Phaser.Renderer.WebGL.Wrappers.WebGLVertexBufferLayoutWrapper](/api/class/renderer-webgl-wrappers-webglvertexbufferlayoutwrapper) {#vertexbufferlayout-phaserrendererwebglwrapperswebglvertexbufferlayoutwrapper}


**说明:**

此 RenderNode 的顶点缓冲布局 。

这包括4个顶点(指数为0-3),每四角一个.


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L75)  
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


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L206](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L206)  
引入版本：4.0.0


---

### run {#run}

#### \<instance> run(drawingContext, tilemapLayer, [parentMatrix]) {#instance-rundrawingcontext-tilemaplayer-parentmatrix}


**说明:**

将层四转换为摄像机视图矩阵, 并进行任何父变换, 将四个角位置和纹理坐标写入顶点缓冲器, 组装纹理阵列( 平面图像、 层数据、 可选动画数据、 以及照明的可选普通地图) , 选择正确的遮蔽变体 。 `updateRenderOptions`,将所有制服都通过 `setupUniforms`,并发出一个图层的单调。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| tilemapLayer | [Phaser.Tilemaps.TilemapGPULayer](/api/class/tilemaps-tilemapgpulayer) | 否 | 提列玛普格普莱尔正在被交付。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 描述游戏对象上下文的母矩阵. |


**重写:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L445](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L445)  
引入版本：4.0.0


---

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(drawingContext, tilemapLayer) {#instance-setupuniformsdrawingcontext-tilemaplayer}


**说明:**

配制所有制成给定的TilemapGPULayer所需的遮阳制服.

这包括视图分辨率和投影矩阵、砖块图像纹理、层数据纹理、动画数据纹理、瓦片尺寸(宽度、高度、边距和间隔)、层的α和动画经过的时间,以及层块照明时的任何照明制服。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| tilemapLayer | [Phaser.Tilemaps.TilemapGPULayer](/api/class/tilemaps-tilemapgpulayer) | 否 | 提列玛普格普莱尔正在被交付。 |


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L254](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L254)  
引入版本：4.0.0


---

### updateRenderOptions {#updateRenderOptions}

#### \<instance> updateRenderOptions(gameObject) {#instance-updaterenderoptionsgameobject}


**说明:**

评估 TilemapGPULayer 的当前状态, 并相应更新着色器程序配置。 每次渲染前都会调用, 并可能导致选择不同的阴影变量 。

具体来说,它配置:动画长度的加法(基于砖块的最大动画帧数),照明加法(基于层的照明设置,启用或禁用,在活动时,光线计数定义更新),自影特征旗,平滑像素艺术加法,边框滤镜特征旗(基于砖块纹理是否使用线性放大滤镜).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.Tilemaps.TilemapGPULayer](/api/class/tilemaps-tilemapgpulayer) | 否 | 提列玛普格普莱尔正在被交付。 |


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L349](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTilemapGPULayer.js#L349)  
引入版本：4.0.0


---

---
