# FilterParallelFilters {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filterparallelfilters)

一个处理两个独立滤镜链的RenderNode——一个底层和一个顶层——每个都应用到同一个输入上,然后用可配置的混合模式来组合它们的结果。这可以使您将两个完全不同的滤镜效果结合到一个游戏对象上;例如,将发光应用到底层,将颜色修正到顶层,然后用加或乘的混合来组合它们.

每个层(下层和顶层)都连续运行着自己订购的过滤链,其中一个过滤器的输出会反馈到下一个层。一旦两个链条完成,结果就会根据控制器的混合设置使用`FilterBlend` RenderNode进行混合.

如果两个层都没有包含任何活动过滤器,输入直接复制到输出时无需修改.

此节点代表在执行期间向其他 RenderNodes 工作。 关联控制器请参见 [Phaser.Filters.ParallelFilters](/api/class/filters-parallelfilters) 。

**构造函数**

`new FilterParallelFilters(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilter](/api/class/renderer-webgl-rendernodes-basefilter)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterParallelFilters.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterParallelFilters.js#L12)  
引入版本：4.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(controller, inputDrawingContext, outputDrawingContext, padding) {#instance-runcontroller-inputdrawingcontext-outputdrawingcontext-padding}


**说明:**

运行平行过滤进程。输入绘图上下文通过底过滤链和顶过滤链独立传递,产生两个单独的过滤结果。这些结果然后通过`FilterBlend` RenderNode与控制器上定义的混合模式和设置混合在一起。

铺设只在每个链条的第一个过滤器上应用;之后在同一链条的过滤器得到零铺设,以避免输出界限的双展.

如果两个层上都没有过滤器活动,输入直接复制到输出上,没有改变.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.ParallelFilters](/api/class/filters-parallelfilters) | 否 | 定义下层和上层过滤链及其混合设置的控制器. |
| inputDrawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 用于两个过滤链的源图像的绘图上下文 。 |
| outputDrawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 将最终混合结果绘制成的图文背景。 可能是 `null`, 届时将分配一个新的上下文 。 |
| padding | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第一次过滤通道上将应用到已显示区域周围的粘贴板。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.BaseFilter#运行


**返回值:** [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) - 包含最终复合输出的绘图上下文 。


> 源码：[src/renderer/webgl/renderNodes/filters/FilterParallelFilters.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterParallelFilters.js#L47)  
引入版本：4.0.0


---

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

---
