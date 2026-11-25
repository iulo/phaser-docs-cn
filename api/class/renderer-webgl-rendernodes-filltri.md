# FillTri {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filltri)

一个 RenderNode 使一个单个填充的三角形带有顶点的颜色。 它被 Phaser 内部用来绘制平面的三角形, 如图形游戏对象在填充形状时生成的三角形。 每个顶点可以携带一个独立的包装的 ARGB 锡色, 允许三角形平滑的颜色梯度。 在提交 GPU 批次之前, 可以提供一个可选的变换矩阵, 以定位世界内的三角形 。

**构造函数**

`new FillTri(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/FillTri.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/FillTri.js#L10)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(drawingContext, currentMatrix, submitterNode, xA, yA, xB, yB, xC, yC, tintA, tintB, tintC, lighting) {#instance-rundrawingcontext-currentmatrix-submitternode-xa-ya-xb-yb-xc-yc-tinta-tintb-tintc-lighting}


**说明:**

将一个装填的三角形用于在当前绘图上下文中渲染。 三个顶点在传递到`currentMatrix`之前, 会被`submitterNode` 选择转换, 将它们写入 GPU 顶点批量。 顶点的颜色可以使三角形显示一个平滑的颜色梯度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 目前使用的上下文 。 |
| currentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 一个适用于顶点的变换矩阵。如果不定义,顶点就不会变换。 |
| submitterNode | [Phaser.Renderer.WebGL.RenderNodes.BatchHandlerTriFlat](/api/class/renderer-webgl-rendernodes-batchhandlertriflat) | 否 | 用于提交节点的节点 。 |
| xA | number | 否 | 第一个顶点的x坐标. |
| yA | number | 否 | 初顶峰的y坐标. |
| xB | number | 否 | 第二顶点的x坐标. |
| yB | number | 否 | 第二顶点的y坐标. |
| xC | number | 否 | 第三顶点的x坐标. |
| yC | number | 否 | 第三顶点的y坐标. |
| tintA | number | 否 | 第一个顶点的锡色,作为一个装填的ARGB整数. |
| tintB | number | 否 | 第二个顶点的锡色,作为包装的ARGB整数. |
| tintC | number | 否 | 第三个顶点的锡色,作为装填的ARGB整数. |
| lighting | boolean | 否 | 是否将照明效果应用到三角形上 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/FillTri.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/FillTri.js#L48)  
引入版本：4.0.0


---

---
