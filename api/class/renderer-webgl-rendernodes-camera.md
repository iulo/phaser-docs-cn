# Camera {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-camera)

一个RenderNode负责执行一个单张Phaser摄像机的全渲染管道。它将摄像机输出的每个阶段:填充背景颜色,通过ListCompositor来制作可见的子对象列表,应用后置效果(闪烁和淡出),然后将结果混入母绘制上下文中。

当摄像机需要隔离时——因为它有非不公开的α,活动性内部或外部滤波链,或`forceComposite`被设置时,节点会从绘图上下文池中分配一个临时帧缓冲器,并让其直接进入上下文中. 内部滤波器在堆肥前应用到摄像机内容,而外部滤波器则扩大覆盖区域,并在摄像机输出被放置到场景坐标空间后应用. 最终的复合图像会使用BatchHandler QuadSingle节点进行批回父上下文,同时尊重摄像机的α和像素圆设置.

**构造函数**

`new Camera(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/Camera.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/Camera.js#L21)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### batchHandlerQuadSingleNode {#batchHandlerQuadSingleNode}

#### batchHandlerQuadSingleNode: [Phaser.Renderer.WebGL.RenderNodes.BatchHandlerQuad](/api/class/renderer-webgl-rendernodes-batchhandlerquad) {#batchhandlerquadsinglenode-phaserrendererwebglrendernodesbatchhandlerquad}


**说明:**

处理批量四位数的 RenderNode 。 当摄像机向帧缓冲器渲染时, 需要将帧缓冲器引向父上下文 。


> 源码：[src/renderer/webgl/renderNodes/Camera.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/Camera.js#L54)  
引入版本：4.0.0


---

### fillCameraNode {#fillCameraNode}

#### fillCameraNode: [Phaser.Renderer.WebGL.RenderNodes.FillCamera](/api/class/renderer-webgl-rendernodes-fillcamera) {#fillcameranode-phaserrendererwebglrendernodesfillcamera}


**说明:**

处理以平整颜色填充摄像机的RenderNode。 用于渲染摄像机背景、 闪光效果和淡化效果 。


> 源码：[src/renderer/webgl/renderNodes/Camera.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/Camera.js#L65)  
引入版本：4.0.0


---

### listCompositorNode {#listCompositorNode}

#### listCompositorNode: [Phaser.Renderer.WebGL.RenderNodes.ListCompositor](/api/class/renderer-webgl-rendernodes-listcompositor) {#listcompositornode-phaserrendererwebglrendernodeslistcompositor}


**说明:**

处理子对象列表的RenderNode。


> 源码：[src/renderer/webgl/renderNodes/Camera.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/Camera.js#L76)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(drawingContext, children, camera, [parentTransformMatrix], [forceFramebuffer], [renderStep]) {#instance-rundrawingcontext-children-camera-parenttransformmatrix-forceframebuffer-renderstep}


**说明:**

执行给定摄像机的全部渲染管道。 其中包括绘制摄像机背景颜色, 通过 ListCompositor 将所有的子游戏对象渲染, 应用任何后触点和淡出效果, 然后将结果混入父绘制上下文 。

如果摄像机需要帧缓冲器(由于活动滤波器,非不透明α,或`forceComposite`正在设置),则从绘图上下文池中分配临时上下文. 内部滤波器被应用到该帧缓冲器内的摄像机内容,输出转换为场景空间后应用外部滤波器. 最终图像被批次回上级上下文,酌情应用摄像机上下文和像素圆形.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 |  | 目前使用的上下文 。 |
| children | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 子对象列表。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 现摄摄像机. |
| parentTransformMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 |  | 如果摄像机被聚焦在被过滤的对象上,则定义了这个变换矩阵. |
| forceFramebuffer | boolean | 是 | false | 摄像机是否总是绘制到一个新的帧缓冲器上? 如果摄像机已启用过滤器, 也会启用此功能 。 |
| renderStep | number | 是 | 0 | 渲染过程的哪个步骤是这个? 这是函数列表中当前运行的函数的索引 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/Camera.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/Camera.js#L97)  
引入版本：4.0.0


---

---
