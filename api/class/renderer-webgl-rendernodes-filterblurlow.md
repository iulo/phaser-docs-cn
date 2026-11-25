# FilterBlurLow {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filterblurlow)

一个使BlurLow滤波器效果变得模糊的RenderNode,它使用一个小的样内核对输入纹理应用单通道高斯文模糊.

这是模糊滤波器家族中质量最低的一级,它使用比中质和高质变体更少的纹理样本,使得以不太平滑的结果为代价在GPU上执行更快,非常适合在视觉忠贞性比渲染性能更不关键的地方巧妙或快速移动的模糊效果.

此节点不应直接使用。 它由 FilterBlur RenderNode 根据正在处理的模糊控制器的质量设置自动选择和引用 。

**构造函数**

`new FilterBlurLow(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterBlurLow.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterBlurLow.js#L12)  
引入版本：4.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader):**


 - [run](/api/class/renderer-webgl-rendernodes-basefiltershader#run)
 - [setupTextures](/api/class/renderer-webgl-rendernodes-basefiltershader#setupTextures)
 - [updateShaderConfig](/api/class/renderer-webgl-rendernodes-basefiltershader#updateShaderConfig)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(controller, drawingContext) {#instance-setupuniformscontroller-drawingcontext}


**说明:**

设置模糊的碎片遮蔽器所需的 WebGL 遮蔽器制服 。

一旦每次渲染通过, 就会拨打到模糊度。 它上传当前渲染的目标尺寸为 `resolution`, 模糊的传播量为 `strength`, 锡为 `color`, 方向模糊轴为 `offset`( 一个包含控制器的横向和纵向偏移值的双元矢量) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Blur](/api/class/filters-blur) | 否 | Blur 过滤器控制器提供统一值 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图上下文,用于读取渲染目标维度. |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupUniforms


> 源码：[src/renderer/webgl/renderNodes/filters/FilterBlurLow.js#L42](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterBlurLow.js#L42)  
引入版本：4.0.0


---

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader):**


 - [indexBuffer](/api/class/renderer-webgl-rendernodes-basefiltershader#indexBuffer)
 - [programManager](/api/class/renderer-webgl-rendernodes-basefiltershader#programManager)
 - [vertexBufferLayout](/api/class/renderer-webgl-rendernodes-basefiltershader#vertexBufferLayout)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

---
