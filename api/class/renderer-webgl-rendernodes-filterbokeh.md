# FilterBokeh {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filterbokeh)

这个 RenderNode 使 Bokeh 过滤器效果, 模拟镜头模糊和深度的场外外观, 既支持标准圆形的 bokeh 模糊, 也支持倾斜的转变模式, 它只模糊图像的上下区域, 以产生浅色焦平面的幻觉。 效果通过关联的过滤控制器来控制 。 见 [Phaser.Filters.Bokeh](/api/class/filters-bokeh) 。

**构造函数**

`new FilterBokeh(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterBokeh.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterBokeh.js#L12)  
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

设置 Bokeh 片段着色器所需的 WebGL 着色器制服, 向过滤器控制器和当前绘图上下文获取值。 每次过滤器打开时,都会自动调用这种方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Bokeh](/api/class/filters-bokeh) | 否 | 提供效果参数的波基滤波控制器. |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 用于提供渲染解析度的当前绘图上下文 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupUniforms


> 源码：[src/renderer/webgl/renderNodes/filters/FilterBokeh.js#L37](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterBokeh.js#L37)  
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
