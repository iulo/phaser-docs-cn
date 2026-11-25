# StrokePath {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-strokepath)

将中风路径作为一系列连接的线段, 将最后一个线段连接回第一个线段, 选择关闭路径。 它被 WebGL 渲染器用来绘制中风形状, 如图形游戏对象创建的形状。 每个线段都作为四( 两个三角形) 输出, 当中风宽度超过两个像素时, 相邻的线段会加入一个额外的连接四( 双三角形) 。 细化级机制允许屏幕空间中太近的中间点被跳过, 减少在稠密路径上的过度绘制 。

**构造函数**

`new StrokePath(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/StrokePath.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/StrokePath.js#L10)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### drawLineNode {#drawLineNode}

#### drawLineNode: [Phaser.Renderer.WebGL.RenderNodes.DrawLine](/api/class/renderer-webgl-rendernodes-drawline) {#drawlinenode-phaserrendererwebglrendernodesdrawline}


**说明:**

生成线段的 RenderNode 。


> 源码：[src/renderer/webgl/renderNodes/StrokePath.js#L35](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/StrokePath.js#L35)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(drawingContext, submitterNode, path, lineWidth, open, currentMatrix, tintTL, tintTR, tintBL, tintBR, detail, lighting) {#instance-rundrawingcontext-submitternode-path-linewidth-open-currentmatrix-tinttl-tinttr-tintbl-tintbr-detail-lighting}


**说明:**

将一条由数行段组成的中风路径渲染出来。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 目前使用的上下文 。 |
| submitterNode | [Phaser.Renderer.WebGL.RenderNodes.BatchHandlerTriFlat](/api/class/renderer-webgl-rendernodes-batchhandlertriflat) | 否 | 用于提交节点的节点 。 |
| path | Array.\<[Phaser.Types.GameObjects.Graphics.WidePoint](/api/typedef/types-gameobjects-graphics#widepoint)> | 否 | 定义线段的点. |
| lineWidth | number | 否 | 中风的宽度. |
| open | boolean | 否 | 如果 `true`,则路径是打开的,最后一个段将不会连接回第一个段。如果 `false`,则路径关闭,并在最后一个段和第一个段之间绘制连接的四段。 |
| currentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 现变质矩阵. |
| tintTL | number | 否 | 左上方的颜色 |
| tintTR | number | 否 | 右上方色色为色. |
| tintBL | number | 否 | 左下色色为色. |
| tintBR | number | 否 | 右下色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色 |
| detail | number | 否 | 屏幕-空间像素中最小的距离, 位于连续路径点之间。 任何距离此距离更近的中间点都会跳过, 减少密路径上的过度绘制。 每个线段的最后一个点总是被保留。 设定为 `0` 来禁用 LOD 并渲染每个点 。 |
| lighting | boolean | 否 | 是否将照明效果应用到中风上. |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/StrokePath.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/StrokePath.js#L45)  
引入版本：4.0.0


---

---
