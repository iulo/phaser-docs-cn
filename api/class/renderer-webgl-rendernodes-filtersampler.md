# FilterSampler {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filtersampler)

一个执行Sampler滤镜的RenderNode,它从WebGL帧缓冲器读取像素数据,并交付给回调,而无需应用任何视觉修改.

与其他过滤节点不同, FilterSampler 不转换或组合其输入。 它充当快照机制: 它调用 `renderer.snapshotFramebuffer` 上下文中绘制的帧缓冲器,并将结果转发给控制器的调回功能。所抽样的区域由控制器的 `region` 属性。如果 `region` 是一个 `Phaser.Geom.Rectangle`,则该矩形区域被捕获。 `region` 是点(对象为 `x` 财务报告和已审计财务报表 `y` 但没有 `width`,则读取一个像素。如果不是,则读取一个像素。 `region` 设置,整个帧缓冲器都进行了抽样。

当游戏对象或摄像机通过Sampler过滤器请求帧缓冲器快照时,这个节点被Phaser过滤管内部使用.

**构造函数**

`new FilterSampler(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilter](/api/class/renderer-webgl-rendernodes-basefilter)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterSampler.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterSampler.js#L10)  
引入版本：4.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(controller, inputDrawingContext, [outputDrawingContext], [padding]) {#instance-runcontroller-inputdrawingcontext-outputdrawingcontext-padding}


**说明:**

抽样输入帧缓冲器,并将结果交付给控制器的回调,然后返回输入绘图上下文不变.

这种方法通过`renderer.snapshotFramebuffer`读取`inputDrawingContext.framebuffer`的像素数据。采样区域由`controller.region`控制:

- 如果`controller.region`是`Phaser.Geom.Rectangle`,则长方形

  区域 `x`, `y`, `width`,和 `height` 被俘虏了

- 如果`controller.region`是一个点(有`x`和`y`但无`width`),

  坐标处的单个像素会被读取。

- 如果`controller.region`没有设定,则整个帧缓冲器都进行了取样.

捕获的数据被传递到 `controller.callback` 。 输入绘图上下文返回时未修改; 此节点不会写入 `outputDrawingContext` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Sampler](/api/class/filters-sampler) | 否 | 采样器滤波控制器,提供`region`进行采样,`callback`进行检测,以获得结果. |
| inputDrawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 绘制框架缓冲器的图案背景将进行取样。 |
| outputDrawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 是 | 输出绘图上下文。 此节点未使用 。 |
| padding | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 辅助的粘贴物绕着渲染区域。 此节点没有使用 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.BaseFilter#运行


**返回值:** [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) - `inputDrawingContext`, 返回不变。


> 源码：[src/renderer/webgl/renderNodes/filters/FilterSampler.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterSampler.js#L43)  
引入版本：4.0.0


---

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

---
