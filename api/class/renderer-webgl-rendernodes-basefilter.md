# BaseFilter {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-basefilter)

人人享受的基数 WebGL 处理后过滤器 Phaser.

过滤器通过处理输入绘图上下文和生成输出绘图上下文,使将视觉效果应用到WebGL纹理的节点成为节点。它们由`Phaser.Filters.Controller`管理,将多个过滤器连在一起,使每个过滤器的输出成为下一个过滤器的输入。过滤器的例子包括模糊、发光、开花和色校正。

此类不应直接被即时化。 相反, 扩展它以创建一个自定义过滤器, 以覆盖 [run](/api/class/renderer-webgl-rendernodes-basefilter#run) 方法 。

**构造函数**

`new BaseFilter(name, manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 滤镜的名称 。 |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 拥有这个过滤器的经理. |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/filters/BaseFilter.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/BaseFilter.js#L10)  
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

运行过滤器,处理输入绘图上下文,并返回包含输出纹理的绘图上下文。

此基础执行无所作为, 并被子类所覆盖。 每个子类应该通过使用 WebGL 阴影程序对输出绘图上下文进行写入来应用其特定的视觉效果( 例如模糊或发光) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Controller](/api/class/filters-controller) | 否 | 过滤器控制器。 |
| inputDrawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 包含输入纹理的绘图上下文。 要么是初始渲染, 要么是上一个过滤器的输出。 这将在运行过程中释放, 并且不再使用 。 |
| outputDrawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 是 | 绘制输出纹理的绘图上下文。 如果不指定, 将生成新的绘图上下文。 一般来说, 此参数用于链条中最后一个过滤器, 因此输出纹理被绘制到主帧缓冲器 。 |
| padding | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 输入纹理中添加的粘贴符, 以创建输出纹理。 如果未指定, 控制器将用来获取粘贴符。 内部过滤器应该未定义, 因此控制器会按需要扩展纹理; 定义为外部过滤器的上一个过滤器的负粘贴符, 因此纹理会缩小到正确的大小 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


**返回值:** [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) - 包含输出纹理的绘图上下文 。


> 源码：[src/renderer/webgl/renderNodes/filters/BaseFilter.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/BaseFilter.js#L40)  
引入版本：4.0.0


---

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

---
