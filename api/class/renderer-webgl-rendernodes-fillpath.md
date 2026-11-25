# FillPath {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-fillpath)

以坚固的颜色填充闭路的 RenderNode 。

它通过将路径数据数组带入并传递到Earcut,将多边形三角形拼成三角形列表。然后每个三角形提交批次进行渲染。路径中的第一个和最后一个点总是保留下来的;内部点可以根据`detail`阈值跳过。

**构造函数**

`new FillPath(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/FillPath.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/FillPath.js#L11)  
引入版本：4.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(drawingContext, currentMatrix, submitterNode, path, tintTL, tintTR, tintBL, detail, lighting) {#instance-rundrawingcontext-currentmatrix-submitternode-path-tinttl-tinttr-tintbl-detail-lighting}


**说明:**

使用 Earcut 绘制路径 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 目前使用的上下文 。 |
| currentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 现变质矩阵. |
| submitterNode | [Phaser.Renderer.WebGL.RenderNodes.BatchHandlerTriFlat](/api/class/renderer-webgl-rendernodes-batchhandlertriflat) | 否 | 用于提交节点的节点 。 |
| path | Array.\<[Phaser.Types.GameObjects.Graphics.WidePoint](/api/typedef/types-gameobjects-graphics#widepoint)> | 否 | 定义线段的点. |
| tintTL | number | 否 | 左上方的颜色 |
| tintTR | number | 否 | 右上方色色为色. |
| tintBL | number | 否 | 左下色色为色. |
| detail | number | 否 | 填充路径时, 以像素表示的详细级别。 任何内部点, 其x和y距离与先前接受的点的距离均在此阈值内被跳过。 首点和末点总是被保留。 0 的值会禁用简化并保留所有点 。 |
| lighting | boolean | 否 | 是否将照明效果应用到路径中 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/FillPath.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/FillPath.js#L36)  
引入版本：4.0.0


---

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

---
