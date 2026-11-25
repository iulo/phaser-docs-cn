# DrawLine {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-drawline)

一个RenderNode,它计算一个线段的几何,并扩展成一个适合WebGL渲染的四角形.

一条线段有两个终点(`a`和`b`),每端可有不同的宽度,允许带线. 此节点通过在每端各半边向线方向抵消垂直线,计算代表线的四角顶点, 由此形成的顶点可选通过矩阵转换, 并附在平整的顶点列表中.

这个节点在绘制中标路径时被WebGL渲染器内部使用,例如Graphics Game Objects所制作的路径.

**构造函数**

`new DrawLine(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/DrawLine.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/DrawLine.js#L10)  
引入版本：4.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(drawingContext, currentMatrix, ax, ay, bx, by, aLineWidth, bLineWidth, vertices) {#instance-rundrawingcontext-currentmatrix-ax-ay-bx-by-alinewidth-blinewidth-vertices}


**说明:**

计算代表一个线段的四极座并附加在所提供的`vertices`列表中,该线的起始点(`a`)和终点(`b`)之间的宽度可以不同,产生一个带子形状. 8个值(4 x/y 配对)的顺序是TL,BL,BR,TR,相对于线的方向.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 目前使用的上下文 。 |
| currentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 一个适用于顶点的变换矩阵。如果不定义,顶点就不会变换。 |
| ax | number | 否 | 线路起始的x坐标. |
| ay | number | 否 | 线条起始的y坐标. |
| bx | number | 否 | 终点的x坐标. |
| by | number | 否 | 线尾的y坐标. |
| aLineWidth | number | 否 | 起始时的线宽度 。 |
| bLineWidth | number | 否 | 末端线宽度. |
| vertices | Array.\<number> | 否 | 指定顶点的列表 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/DrawLine.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/DrawLine.js#L40)  
引入版本：4.0.0


---

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

---
