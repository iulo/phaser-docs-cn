# BatchHandlerTriFlat {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-batchhandlertriflat)

一个渲染节点,它利用WebGL的渲染器,分批绘制具有横跨顶点颜色的平面阴影三角形。与纹理制成的批处理器不同,这个节点不需要纹理数据——每个顶点只携带一个位置和一个装满的RGBA锡色,它用来渲染图形对象和其他填充或中线形状等未纹理几何.

三角通过 `batch` 方法提交,作为一组顶点位置,每个顶点颜色,以及将顶点组合成三角形的索引阵列。节点将这些组合成动态顶点缓冲和索引缓冲,当批量满满载或状态变化时自动冲刷。

可选支持动态照明:当提供照明配置时,节点切换到照明辅助的遮阳变体,并上传每个帧所需的灯服.

**构造函数**

`new BatchHandlerTriFlat(manager, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerConfig](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerconfig) | 是 | 此处理器的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BatchHandler](/api/class/renderer-webgl-rendernodes-batchhandler)  



> 源码：[src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L17)  
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

### nextRenderOptions {#nextRenderOptions}

#### nextRenderOptions: object {#nextrenderoptions-object}


**说明:**

正在构建的渲染选项 。


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L92)  
引入版本：4.0.0


---

### renderOptions {#renderOptions}

#### renderOptions: object {#renderoptions-object}


**说明:**

当前为批量构建的选项。这些选项有助于定义阴影。


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L80)  
引入版本：4.0.0


---

### vertexCount {#vertexCount}

#### vertexCount: number {#vertexcount-number}


**说明:**

目前批量的顶点数量.


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L61)  
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

#### \<instance> batch(currentContext, indexes, vertices, colors, [lighting]) {#instance-batchcurrentcontext-indexes-vertices-colors-lighting}


**说明:**

将数据添加到批量中 。

数据由顶点和指数化三角组成,每个三角由三个指数定义,进入顶点阵列.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| currentContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 |  | 当前绘图背景 。 |
| indexes | Array.\<number> | 否 |  | 指数数据。每个三角形由三个指数定义,进入顶点阵列,因此这个长度应该是3的倍数. |
| vertices | Array.\<number> | 否 |  | 顶点数据。每个顶点由一个x坐标和一个y坐标定义。 |
| colors | Array.\<number> | 否 |  | 颜色数据。 每个顶点都有一个颜色作为Uint32值。 |
| lighting | boolean | 是 | false | 这批货应该用照明吗? |


**重写:** Phaser.Renderer.WebGL.RenderNodes.BatchHandler# 批量着


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L326](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L326)  
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


**重写:** Phaser.Renderer.WebGL.RenderNodes.BatchHandler#运行


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L264](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L264)  
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


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L159](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L159)  
引入版本：4.0.0


---

### updateRenderOptions {#updateRenderOptions}

#### \<instance> updateRenderOptions(lighting) {#instance-updaterenderoptionslighting}


**说明:**

将收到的渲染选项与当前批次的渲染选项进行比较,并记录其是否更改。如果照明值与用于构建当前批次的数值不同,则修改将按下列方式进行: `nextRenderOptions` 财务报告和已审计财务报表 `_renderOptionsChanged` 设置为 `true`,表示批量必须冲刷,在添加新的几何之前,阴影重新配置。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| lighting | object \| false | 否 | 下一个绘图调用时的照明配置, 或如果禁用照明时的 `false` 。 |


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L196](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L196)  
引入版本：4.0.0


---

### updateShaderConfig {#updateShaderConfig}

#### \<instance> updateShaderConfig() {#instance-updateshaderconfig}


**说明:**

将任何待决的渲染选项修改应用到着色器程序。此方法在当前批次被冲洗后, 当 `_renderOptionsChanged` 谓 `true`同步 `renderOptions` 与 `nextRenderOptions` ,并相应启用或禁用照明阴影添加。启用照明时,它也会更新 `LIGHT_COUNT` 预处理器定义以匹配渲染器配置的最大灯光数量。


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L223](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerTriFlat.js#L223)  
引入版本：4.0.0


---

---
