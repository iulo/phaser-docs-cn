# FilterBlur {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filterblur)

应用多路高斯模糊效果的RenderNode,由[Phaser.Filters.Blur](/api/class/filters-blur)控制器驱动.

这个节点不是直接运行模糊的遮蔽器,而是充当调度器:它检查控制器的`quality`设置,并代表三个专用模糊节点中的一个——`FilterBlurLow`(质量0),`FilterBlurMed`(质量1),或`FilterBlurHigh`(质量2).

对于控制器要求的每个步骤,节点执行两个分隔的通道——一个水平的,一个垂直的. 由于高斯模糊是轴分隔的,这会产生一个完整的2D高斯通道的同样视觉结果,同时执行的费用也明显较低. 帕丁只在第一个通道上应用,这样后续的通道不会逐渐地增大渲染区域.

**构造函数**

`new FilterBlur(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilter](/api/class/renderer-webgl-rendernodes-basefilter)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterBlur.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterBlur.js#L11)  
引入版本：4.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(controller, inputDrawingContext, outputDrawingContext, [padding]) {#instance-runcontroller-inputdrawingcontext-outputdrawingcontext-padding}


**说明:**

运行模糊过滤器效果。

该方法基于`controller.quality`选择合适的模糊的遮阳节点,然后执行轴分隔的高斯模糊的`controller.steps`迭代。每次迭代由水平传球和垂直传球组成。从控制器上划出的位置只在第一个传球上应用;随后的传球使用空矩形,这样渲染区域不会随每个迭代而增长。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Blur](/api/class/filters-blur) | 否 | 模糊过滤器控制器,提供质量,步骤,强度,颜色,以及轴模糊的量. |
| inputDrawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 包含源质素的图案上下文以模糊 。 |
| outputDrawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 接收最终模糊输出的绘图上下文 。 |
| padding | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 将应用在第一个通行证上的渲染区域周围。如果省略,则从控制器中提取。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilter#运行


**返回值:** [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) - 包含模糊结果的绘图上下文 。


> 源码：[src/renderer/webgl/renderNodes/filters/FilterBlur.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterBlur.js#L43)  
引入版本：4.0.0


---

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

---
