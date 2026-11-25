# FilterBlurHigh {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filterblurhigh)

使用专用的碎片遮蔽器使高斯因效果变得高品质模糊的RenderNode。与标准模糊变体不同,这个节点使用更大的内核,以每通格普工作增加为代价,产生更平滑,更视觉准确的结果.

此节点不应被即时或直接调用。 当模糊控制器的质量设置设置被设置为高时, 它会被 `FilterBlur` 朗德节点自动选中和引用 。

**构造函数**

`new FilterBlurHigh(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterBlurHigh.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterBlurHigh.js#L12)  
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

上传高质量模糊度高的通行证所需的遮阳制服.

在模糊着色器执行之前, 它会自动通过渲染管道调用。 它会像 `resolution` 制服、 模糊的 `strength` 、 锡的 `color` 和 方向`offset` (x/y) 一样通过当前导线。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Blur](/api/class/filters-blur) | 否 | Blur 过滤器控制器提供模糊参数 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前用于确定渲染解析度的绘图上下文 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupUniforms


> 源码：[src/renderer/webgl/renderNodes/filters/FilterBlurHigh.js#L38](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterBlurHigh.js#L38)  
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
