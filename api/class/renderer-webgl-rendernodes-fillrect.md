# FillRect {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-fillrect)

将一个固态、平面、平面、平色的矩形转换成WebGL的导管。 它使用一个提供的变形矩阵将四个角顶点转换成两个三角形, 并提交到`BatchHandlerTriFlat`节点, 并支持每个角的锡色和可选的照明。 这个节点用于全屏色填充、背景覆盖、 相机效果, 以及任何不需要纹理的矩形几何 。

**构造函数**

`new FillRect(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/FillRect.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/FillRect.js#L11)  
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

#### \<instance> run(drawingContext, currentMatrix, submitterNode, x, y, width, height, tintTL, tintTR, tintBL, tintBR, lighting) {#instance-rundrawingcontext-currentmatrix-submitternode-x-y-width-height-tinttl-tinttr-tintbl-tintbr-lighting}


**说明:**

使用给定矩阵转换矩形的四个角顶点,然后将它们作为两个索引三角形提交批量处理器,同时提交每个角点的颜色。您想要绘制的每个矩形,每个框都使用这个名称;它将实际的绘图调用代表提交器节点。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 目前使用的上下文 。 |
| currentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 用于顶点的变换矩阵。如果不定义,则使用身份矩阵。 |
| submitterNode | [Phaser.Renderer.WebGL.RenderNodes.BatchHandlerTriFlat](/api/class/renderer-webgl-rendernodes-batchhandlertriflat) | 否 | 要使用的提交节点。 如果定义不明确, 则使用 `BatchHandlerTriFlat` 。 |
| x | number | 否 | 矩形左上角的x坐标,以像素表示. |
| y | number | 否 | 矩形左上角的y坐标,以像素表示. |
| width | number | 否 | 矩形的宽度,以像素为单位. |
| height | number | 否 | 矩形的高度,以像素表示. |
| tintTL | number | 否 | 左上方的颜色 |
| tintTR | number | 否 | 右上方色色为色. |
| tintBL | number | 否 | 左下色色为色. |
| tintBR | number | 否 | 右下色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色 |
| lighting | boolean | 否 | 是否将照明效果应用到矩形上 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/FillRect.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/FillRect.js#L71)  
引入版本：4.0.0


---

---
