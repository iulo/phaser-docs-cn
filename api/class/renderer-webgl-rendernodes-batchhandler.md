# BatchHandler {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-batchhandler)

批量处理器 render 节点。 这是用于其他批量处理器 rander 节点的基类 。

批量处理器缓冲数据,用于一组要一起渲染的对象,负责制备批量物品的顶点缓冲布局和遮蔽器.

这个班级并非直接使用,而是被其他班级扩展.

**构造函数**

`new BatchHandler(manager, defaultConfig, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| defaultConfig | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerConfig](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerconfig) | 否 | 此 RenderNode 的默认配置对象。 用于确保所有所需的属性都存在, 所以它必须是完整的 。 |
| config | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerConfig](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerconfig) | 是 | 此 RenderNode 的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L13)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### batchEntries {#batchEntries}

#### batchEntries: Array.\<[Phaser.Types.Renderer.WebGL.WebGLBatchEntry](/api/typedef/types-renderer-webgl#webglbatchentry)> {#batchentries-arrayphasertypesrendererwebglwebglbatchentry}


**说明:**

批次中的条目。 每个条目代表一个使用相同纹理池的“ 子批次” 的四位数。 这样, 渲染器可以继续缓冲四位数进入同一批次, 而无需上传顶点缓冲。 当批次冲出时, 将有一个顶点缓冲上传, 每批次有一个抽取调用 。


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L232](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L232)  
引入版本：4.0.0


---

### bytesPerIndexPerInstance {#bytesPerIndexPerInstance}

#### bytesPerIndexPerInstance: number {#bytesperindexperinstance-number}


**说明:**

每个索引的字节数。 用于推进索引缓冲, 并计算一个 Uint16Array 元素的大小 。


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L98)  
引入版本：4.0.0


---

### bytesPerInstance {#bytesPerInstance}

#### bytesPerInstance: number {#bytesperinstance-number}


**说明:**

每个实例的字节数,用来确定要上传的顶点缓冲的多少.


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L200](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L200)  
引入版本：4.0.0


---

### currentBatchEntry {#currentBatchEntry}

#### currentBatchEntry: [Phaser.Types.Renderer.WebGL.WebGLBatchEntry](/api/typedef/types-renderer-webgl#webglbatchentry) {#currentbatchentry-phasertypesrendererwebglwebglbatchentry}


**说明:**

当前批次条目正填充纹理.


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L218](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L218)  
引入版本：4.0.0


---

### floatsPerInstance {#floatsPerInstance}

#### floatsPerInstance: number {#floatsperinstance-number}


**说明:**

每个实例的浮点数,用来确定顶点缓冲器的更新量.


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L209](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L209)  
引入版本：4.0.0


---

### indexBuffer {#indexBuffer}

#### indexBuffer: [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) {#indexbuffer-phaserrendererwebglwrapperswebglbufferwrapper}


**说明:**

索引缓冲定义顶点顺序.


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L132)  
引入版本：4.0.0


---

### indicesPerInstance {#indicesPerInstance}

#### indicesPerInstance: number {#indicesperinstance-number}


**说明:**

每个实例的指数数。 通常为 6, 每个指数对应顶点缓冲器中的顶点 。


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L86)  
引入版本：4.0.0


---

### instanceCount {#instanceCount}

#### instanceCount: number {#instancecount-number}


**说明:**

批次中目前实例的数量。


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L247](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L247)  
引入版本：4.0.0


---

### instancesPerBatch {#instancesPerBatch}

#### instancesPerBatch: number {#instancesperbatch-number}


**说明:**

每批实例的数量,用于确定顶点缓冲的大小,以及要渲染的实例数量.

这通常受顶点的最大数量的限制,这些顶点可以用16位的UNSIGNED_INT索引缓冲器区分,这个缓冲器是65536. 这在游戏渲染配置中设定为`batchSize`.


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L52)  
引入版本：4.0.0


---

### maxTexturesPerBatch {#maxTexturesPerBatch}

#### maxTexturesPerBatch: number {#maxtexturesperbatch-number}


**说明:**

每批项的纹理最大数量。 这通常设定为可用纹理单位的最大数量, 但对于某些用途来说可能较小 。


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L110](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L110)  
引入版本：4.0.0


---

### programManager {#programManager}

#### programManager: [Phaser.Renderer.WebGL.ProgramManager](/api/class/renderer-webgl-programmanager) {#programmanager-phaserrendererwebglprogrammanager}


**说明:**

程序管理器用来创建和管理遮荫程序。 包含遮荫变体 。


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L164](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L164)  
引入版本：4.0.0


---

### vertexBufferLayout {#vertexBufferLayout}

#### vertexBufferLayout: [Phaser.Renderer.WebGL.Wrappers.WebGLVertexBufferLayoutWrapper](/api/class/renderer-webgl-wrappers-webglvertexbufferlayoutwrapper) {#vertexbufferlayout-phaserrendererwebglwrapperswebglvertexbufferlayoutwrapper}


**说明:**

用于存储顶点数据的布局,数据,和顶点缓冲.

默认布局是用于一个四重奏,每个顶点上都有位置,纹理坐标,纹理ID,锡效应,以及锡色.


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L148](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L148)  
引入版本：4.0.0


---

### verticesPerInstance {#verticesPerInstance}

#### verticesPerInstance: number {#verticesperinstance-number}


**说明:**

每一例的顶点数。

这通常是一个四角。

每个顶点对应元素缓冲中的索引.


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L66)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### batch {#batch}

#### \<instance> batch([args]) {#instance-batchargs}


**说明:**

将实例添加到批次中。 游戏对象调用此方法来添加到批次中。 此方法应该被子类所覆盖 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| args | * | 是 | 批量处理器的参数。 视处理器的不同而有所不同 。 |


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L407](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L407)  
引入版本：4.0.0


---

### resize {#resize}

#### \<instance> resize(width, height) {#instance-resizewidth-height}


**说明:**

为渲染器设定新尺寸。 这应该被子类覆盖 。

当渲染器重新大小时,此功能会自动调用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 变形器的新宽度 。 |
| height | number | 否 | 造物器的新高度. |


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L365](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L365)  
引入版本：4.0.0


---

### run {#run}

#### \<instance> run(drawingContext, [args]) {#instance-rundrawingcontext-args}


**说明:**

绘制然后清空当前批次 。

这种方法在批量满满时,或者在需要做其他事情时,由这个节点或管理器自动称为.

这种方法应该被子类所取代.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| args | * | 是 | 需要传递给批处理器的附加参数 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L392](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L392)  
引入版本：4.0.0


---

### updateTextureCount {#updateTextureCount}

#### \<instance> updateTextureCount([count]) {#instance-updatetexturecountcount}


**说明:**

更新每批可用的平行纹理单位数。 下级应覆盖此数 。

这是由收听者自动调用,用于`Phaser.Renderer.Events.SET_PARALLEL_TEXTURE_UNITS`事件,由RenderNodeManager触发.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| count | number | 是 | 每批可用的平行纹理单位新数。 如果未定义, 则使用最高纹理单位数 。 |


> 源码：[src/renderer/webgl/renderNodes/BatchHandler.js#L378](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandler.js#L378)  
引入版本：4.0.0


---

---
