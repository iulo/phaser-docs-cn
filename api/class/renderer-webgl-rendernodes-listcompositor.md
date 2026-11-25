# ListCompositor {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-listcompositor)

ListCompositor

**构造函数**

`new ListCompositor(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/ListCompositor.js#L27](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/ListCompositor.js#L27)  
引入版本：4.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(displayContext, children, [parentTransformMatrix], [renderStep]) {#instance-rundisplaycontext-children-parenttransformmatrix-renderstep}


**说明:**

显示列表中每个孩子的显示 。

如果一个孩子的混合模式与上一个孩子不同, 此会分配一个新的“ 显示” 。 如果正在进行中, 这将启动新的批次 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| displayContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 |  | 目前使用的上下文 。 |
| children | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 儿童名单。 |
| parentTransformMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 |  | 母游戏对象的累积变换矩阵,当此列表作为嵌入式显示结构的一部分被渲染出来时,会传递下来. |
| renderStep | number | 是 | 0 | 当前在此框架执行的渲染函数列表中显示的渲染步骤索引 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/ListCompositor.js#L35](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/ListCompositor.js#L35)  
引入版本：4.0.0


---

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

---
