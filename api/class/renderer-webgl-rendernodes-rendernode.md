# RenderNode {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-rendernode)

RenderNode

**构造函数**

`new RenderNode(name, manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 兰德诺德的名字. |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static

> 源码：[src/renderer/webgl/renderNodes/RenderNode.js#L32](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNode.js#L32)  
引入版本：4.0.0

## 公开成员 {#public-members}

### manager {#manager}

#### manager: [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) {#manager-phaserrendererwebglrendernodesrendernodemanager}


**说明:**

这个RenderNode的经理


> 源码：[src/renderer/webgl/renderNodes/RenderNode.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNode.js#L47)  
引入版本：4.0.0


---

### name {#name}

#### name: string {#name-string}


**说明:**

兰德诺德的名字.


> 源码：[src/renderer/webgl/renderNodes/RenderNode.js#L38](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNode.js#L38)  
引入版本：4.0.0


---

## 公开方法 {#public-methods}

### onRunBegin {#onRunBegin}

#### \<instance> onRunBegin(drawingContext) {#instance-onrunbegindrawingcontext}


**说明:**

默认情况下, 这是空方法钩子, 您可以在自定义中覆盖并使用 complete conference 节点 。

这种方法在 `run` 方法的开头叫做,不要忘记在您的自定义方法中称之为.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 目前使用的上下文 。 |


> 源码：[src/renderer/webgl/renderNodes/RenderNode.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNode.js#L85)  
引入版本：4.0.0


---

### onRunEnd {#onRunEnd}

#### \<instance> onRunEnd(drawingContext) {#instance-onrunenddrawingcontext}


**说明:**

默认情况下, 这是空方法钩子, 您可以在自定义中覆盖并使用 complete conference 节点 。

这种方法在 `run` 方法的结尾处被称作,不要忘记在您的自定义方法中称之为.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 目前使用的上下文 。 |


> 源码：[src/renderer/webgl/renderNodes/RenderNode.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNode.js#L98)  
引入版本：4.0.0


---

### run {#run}

#### \<instance> run([args]) {#instance-runargs}


**说明:**

运行 RenderNode。 这是一个应该被特定执行所覆盖的根节法 。

这种方法可能由`setDebug`包扎.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| args | * | 是 | 传递到节点的参数。 这些参数会因节点而异 。 |


> 源码：[src/renderer/webgl/renderNodes/RenderNode.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNode.js#L69)  
引入版本：4.0.0


---

### setDebug {#setDebug}

#### \<instance> setDebug(debug) {#instance-setdebugdebug}


**说明:**

启用或禁用此节点的调试报告 。

启用时, `run`方法被一个包装器取代,将节点的名字推到管理器的调试堆栈上,然后执行后弹出,使渲染器能够跟踪哪些节点是活跃的. `run`执行原保存在 `_run`中.

禁用时,恢复原`run`方法,清除`_run`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| debug | boolean | 否 | 是否报告调试信息 。 |


> 源码：[src/renderer/webgl/renderNodes/RenderNode.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RenderNode.js#L111)  
引入版本：4.0.0


---

---
