# BatchHandlerPointLight {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-batchhandlerpointlight)

一个批量处理器RenderNode,它使`PointLight`游戏对象使用WebGL.

每个点光作为纹理四重奏(4个顶点,6个指数)提交到共享顶点缓冲器中。专用点光遮蔽器会计算每个片段的光线落地,使用光的世界位置,半径,衰减因子,颜色,强度等多个灯光组合在一起,当批量满满满或渲染器需要切换上下文时,用一个抽图调出一个光线。

这个处理器没有使用纹理;它将一个空纹理阵列传递到绘图调用,因为照明完全在碎片遮蔽器中计算.

**构造函数**

`new BatchHandlerPointLight(manager, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerConfig](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerconfig) | 是 | 此处理器的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BatchHandler](/api/class/renderer-webgl-rendernodes-batchhandler)  



> 源码：[src/renderer/webgl/renderNodes/BatchHandlerPointLight.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerPointLight.js#L12)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.BatchHandler](/api/class/renderer-webgl-rendernodes-batchhandler):**


 - [batchEntries](/api/class/renderer-webgl-rendernodes-batchhandler#batchEntries)
 - [bytesPerIndexPerInstance](/api/class/renderer-webgl-rendernodes-batchhandler#bytesPerIndexPerInstance)
 - [bytesPerInstance](/api/class/renderer-webgl-rendernodes-batchhandler#bytesPerInstance)
 - [currentBatchEntry](/api/class/renderer-webgl-rendernodes-batchhandler#currentBatchEntry)
 - [floatsPerInstance](/api/class/renderer-webgl-rendernodes-batchhandler#floatsPerInstance)
 - [indexBuffer](/api/class/renderer-webgl-rendernodes-batchhandler#indexBuffer)
 - [indicesPerInstance](/api/class/renderer-webgl-rendernodes-batchhandler#indicesPerInstance)
 - [instanceCount](/api/class/renderer-webgl-rendernodes-batchhandler#instanceCount)
 - [instancesPerBatch](/api/class/renderer-webgl-rendernodes-batchhandler#instancesPerBatch)
 - [maxTexturesPerBatch](/api/class/renderer-webgl-rendernodes-batchhandler#maxTexturesPerBatch)
 - [programManager](/api/class/renderer-webgl-rendernodes-batchhandler#programManager)
 - [vertexBufferLayout](/api/class/renderer-webgl-rendernodes-batchhandler#vertexBufferLayout)
 - [verticesPerInstance](/api/class/renderer-webgl-rendernodes-batchhandler#verticesPerInstance)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### defaultConfig {#defaultConfig}

#### defaultConfig: [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerConfig](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerconfig) {#defaultconfig-phasertypesrendererwebglrendernodesbatchhandlerconfig}


**说明:**

此处理器的默认配置 。


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerPointLight.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerPointLight.js#L55)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.BatchHandler](/api/class/renderer-webgl-rendernodes-batchhandler):**


 - [resize](/api/class/renderer-webgl-rendernodes-batchhandler#resize)
 - [updateTextureCount](/api/class/renderer-webgl-rendernodes-batchhandler#updateTextureCount)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### batch {#batch}

#### \<instance> batch(drawingContext, light, xTL, yTL, xBL, yBL, xTR, yTR, xBR, yBR, lightX, lightY) {#instance-batchdrawingcontext-light-xtl-ytl-xbl-ybl-xtr-ytr-xbr-ybr-lightx-lighty}


**说明:**

增灯于批.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| light | [Phaser.GameObjects.PointLight](/api/class/gameobjects-pointlight) | 否 | 增量之灯. |
| xTL | number | 否 | 光的左上角的x坐标. |
| yTL | number | 否 | 光的左上方的Y坐标 |
| xBL | number | 否 | 光线的左下角的x坐标. |
| yBL | number | 否 | 光的左下方的Y坐标 |
| xTR | number | 否 | 光线的上右X坐标. |
| yTR | number | 否 | 光线的上右Y坐标. |
| xBR | number | 否 | 光线的下部右侧X坐标. |
| yBR | number | 否 | 光线的下部右Y坐标. |
| lightX | number | 否 | 光中心的世界x坐标,被遮光器用来计算光圈落变. |
| lightY | number | 否 | 光中心的世界y坐标,被遮蔽器用来计算光圈落变. |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BatchHandler# 批量着


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerPointLight.js#L213](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerPointLight.js#L213)  
引入版本：4.0.0


---

### run {#run}

#### \<instance> run(drawingContext) {#instance-rundrawingcontext}


**说明:**

绘制然后清空当前批次 。

这种方法在批量满满时,或者在需要做其他事情时,由这个节点或管理器自动称为.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BatchHandler#运行


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerPointLight.js#L163](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerPointLight.js#L163)  
引入版本：4.0.0


---

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(drawingContext) {#instance-setupuniformsdrawingcontext}


**说明:**

更新当前遮阳程序制服 。

批量运行时,这种方法会自动调用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerPointLight.js#L131](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerPointLight.js#L131)  
引入版本：4.0.0


---

---
