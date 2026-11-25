# RenderNodeManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-rendernodemanager)

RenderNodeManager

**构造函数**

`new RenderNodeManager(renderer)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有这个经理的造型师. |

---


**作用域**: static

> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L101)  
引入版本：4.0.0

## 公开成员 {#public-members}

### currentBatchDrawingContext {#currentBatchDrawingContext}

#### currentBatchDrawingContext: [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) {#currentbatchdrawingcontext-phaserrendererwebgldrawingcontext}


**说明:**

当前批次的绘图上下文。 此处存储此数据是因为批次节点是无国籍的 。


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L249](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L249)  
引入版本：4.0.0


---

### currentBatchNode {#currentBatchNode}

#### currentBatchNode: [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode) {#currentbatchnode-phaserrendererwebglrendernodesrendernode}


**说明:**

目前正在填充的 Render 节点。 保存此节点是为了在运行另一类型渲染时完成 。


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L237](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L237)  
引入版本：4.0.0


---

### currentDebugNode {#currentDebugNode}

#### currentDebugNode: DebugGraphNode {#currentdebugnode-debuggraphnode}


**说明:**

调试图中当前节点。 `debug` 启用时使用此功能 。


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L280](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L280)  



---

### debug {#debug}

#### debug: boolean {#debug-boolean}


**说明:**

节点是否应该记录其调试运行方法。 应通过 `setDebug` 设置 。


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L260](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L260)  
引入版本：4.0.0


---

### debugGraph {#debugGraph}

#### debugGraph: DebugGraphNode {#debuggraph-debuggraphnode}


**说明:**

运行的节点调试图。 `debug` 启用时使用此图 。


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L271](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L271)  



---

### maxParallelTextureUnits {#maxParallelTextureUnits}

#### maxParallelTextureUnits: number {#maxparalleltextureunits-number}


**说明:**

最多选择一个批次的纹理单位。 蝙蝠可以绑定多个纹理, 并且每个实例选择一个, 允许更大的批次。 但是, 一些移动设备在使用多个纹理单位时会降低性能。 因此, 如果启用游戏配置选项 `autoMobileTextures`, 设备不是桌面, 则会设定为 1 。 否则, 将设定为渲染器的 `maxTextures` 。

一些遮蔽剂可能需要一个以上的纹理单元,因此每批对纹理单元的实际限制是`maxTextures`.

此值可以在运行时通过`setMaxParallelTextureUnits`更改.


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L119)  
引入版本：4.0.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrendererwebglwebglrenderer}


**说明:**

拥有这个经理的造型师.


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L108)  
引入版本：4.0.0


---

## 公开方法 {#public-methods}

### addNode {#addNode}

#### \<instance> addNode(name, node) {#instance-addnodename-node}


**说明:**

向管理器添加节点 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 结节之名. |
| node | [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode) | 否 | 结节要加. |


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L291](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L291)  
引入版本：4.0.0


---

### addNodeConstructor {#addNodeConstructor}

#### \<instance> addNodeConstructor(name, constructor) {#instance-addnodeconstructorname-constructor}


**说明:**

为管理器添加一个节点的构造器。 这将允许在调用 `getNode` 时构建节点 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 结节之名. |
| constructor | function | 否 | 节点的构造器. |


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L316](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L316)  
引入版本：4.0.0


---

### debugToString {#debugToString}

#### \<instance> debugToString() {#instance-debugtostring}


**说明:**

将当前调试图格式化为缩进的字符串。


**返回值:** string - 格式化调试图 。


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L544](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L544)  
引入版本：4.0.0


---

### finishBatch {#finishBatch}

#### \<instance> finishBatch() {#instance-finishbatch}


**说明:**

完成当前批次的渲染。 在开始新的渲染任务时, 需要调用 。


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L425](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L425)  
引入版本：4.0.0


---

### getNode {#getNode}

#### \<instance> getNode(name) {#instance-getnodename}


**说明:**

从经理那里得到一个节点。

如果节点不存在,且有构造器可用,则会建置并添加到管理器中,然后返回.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 结节之名. |


**返回值:** [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode) - 节点,如果不存在,则无效.


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L335](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L335)  
引入版本：4.0.0


---

### hasNode {#hasNode}

#### \<instance> hasNode(name, [constructed]) {#instance-hasnodename-constructed}


**说明:**

检查管理器中是否存在节点 。

如果一个节点没有构建,但有一个构造器,则它将被视为存在。设置 `constructed`为真,以要求该节点已经构建 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 名称 | string | 否 |  | 结节之名. |
| constructed | boolean | 是 | false | 是否必须构建节点以视为存在 。 |


**返回值:** boolean - 节点是否存在 。


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L362](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L362)  
引入版本：4.0.0


---

### popDebug {#popDebug}

#### \<instance> popDebug() {#instance-popdebug}


**说明:**

从调试图中弹出最后一个录制的 RenderNode 。


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L521](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L521)  
引入版本：4.0.0


---

### pushDebug {#pushDebug}

#### \<instance> pushDebug(name) {#instance-pushdebugname}


**说明:**

在调试图中记录新运行的 RenderNode 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 结节之名. |


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L489](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L489)  
引入版本：4.0.0


---

### setCurrentBatchNode {#setCurrentBatchNode}

#### \<instance> setCurrentBatchNode(node, [drawingContext]) {#instance-setcurrentbatchnodenode-drawingcontext}


**说明:**

设置当前批号节点。 如果一个批号节点已经在进行中, 将在新节点设置之前完成 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| node | [Phaser.Renderer.WebGL.RenderNodes.BatchHandler](/api/class/renderer-webgl-rendernodes-batchhandler) | 否 | 要设置的节点, 或清除当前节点的无效 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 是 | 绘图上下文。 只有在定义 `node` 时才使用 。 |


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L380](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L380)  
引入版本：4.0.0


---

### setDebug {#setDebug}

#### \<instance> setDebug(value) {#instance-setdebugvalue}


**说明:**

设定节点是否记录调试的运行方法。 这将在所有节点设置调试属性, 重置调试图表, 并在调试功能失效前记录一个图表框 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 节点是否应该记录其调试运行方法 。 |


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L452](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L452)  
引入版本：4.0.0


---

### setMaxParallelTextureUnits {#setMaxParallelTextureUnits}

#### \<instance> setMaxParallelTextureUnits([value]) {#instance-setmaxparalleltextureunitsvalue}


**说明:**

设定 `maxParallelTextureUnits` 以切换到新值。此值将被粘贴在范围[1, 渲染器] 上。maxTextures].

这可以帮助用户在运行时调整游戏的性能.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 是 | 新的数值 `maxParallelTextureUnits`。必须是数字;它将被夹在范围[1],渲染器。maxTextures]. |


**Fires:** [Phaser.Renderer.Events#event:SET_PARALLEL_TEXTURE_UNITS](/api/event/renderer-events#set_parallel_texture_units)


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L406](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L406)  
引入版本：4.0.0


---

### startStandAloneRender {#startStandAloneRender}

#### \<instance> startStandAloneRender() {#instance-startstandalonerender}


**说明:**

启动独立渲染器, 这不是批次的一部分。 如果批次正在进行, 则会触发批次完成 。


> 源码：[src/renderer/webgl/renderNodes/RenderNodeManager.js#L440](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNodeManager.js#L440)  
引入版本：4.0.0


---

---
