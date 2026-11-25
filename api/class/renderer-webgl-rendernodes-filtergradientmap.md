# FilterGradientMap {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filtergradientmap)

一个使渐变图像过滤器效果的RenderNode,它从梯度坡道纹理将源图像中每个像素的光度映射到相应的颜色。较暗的像素被映射到梯度的一端,而较亮的像素则被另一端,完全取代了原来的颜色。这可以实现诸如热成像、夜视、Sepia到线或任何由亮度驱动的任意的颜色等级等结构效应。

梯度由一个[Phaser.Display.ColorRamp](/api/class/display-colorramp)附加在控制[Phaser.Filters.GradientMap](/api/class/filters-gradientmap)过滤器上,坡道作为数据纹理上传,并在片段遮蔽器中取样. 遮蔽器变体根据坡道的带状树深进行动态选择,因此当坡道结构改变时程序会重新编译.

见[Phaser.Filters.GradientMap](/api/class/filters-gradientmap).

**构造函数**

`new FilterGradientMap(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterGradientMap.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterGradientMap.js#L13)  
引入版本：4.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader):**


 - [run](/api/class/renderer-webgl-rendernodes-basefiltershader#run)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### setupTextures {#setupTextures}

#### \<instance> setupTextures(controller, textures, _drawingContext) {#instance-setuptexturescontroller-textures-_drawingcontext}


**说明:**

将梯度映射阴影所需的纹理进行套装。用于编码梯度颜色的坡度数据纹理被分配到纹理槽1. 槽0用于源质化纹理,由基类处理。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.GradientMap](/api/class/filters-gradientmap) | 否 | 提供斜坡数据的过滤控制器 。 |
| textures | Array.\<WebGLTexture> | 否 | 此绘图调用所需的纹理阵列 。 |
| _drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图上下文。 不适用此方法 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupTextures


> 源码：[src/renderer/webgl/renderNodes/filters/FilterGradientMap.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterGradientMap.js#L55)  
引入版本：4.0.0


---

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(controller, _drawingContext) {#instance-setupuniformscontroller-_drawingcontext}


**说明:**

设置梯度映射效果所需的所有遮阳制服。 其中包括坡道纹理指数、坡道的数据纹理分辨率和首带偏移( 用于在共享坡道地图集中处理正确的行)、 双色图案、 不可预加的旗帜、 锡色及其混合因子以及总体的α值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.GradientMap](/api/class/filters-gradientmap) | 否 | 提供统一值的过滤控制器 。 |
| _drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图上下文。 不适用此方法 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupUniforms


> 源码：[src/renderer/webgl/renderNodes/filters/FilterGradientMap.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterGradientMap.js#L73)  
引入版本：4.0.0


---

### updateShaderConfig {#updateShaderConfig}

#### \<instance> updateShaderConfig(controller, _drawingContext) {#instance-updateshaderconfigcontroller-_drawingcontext}


**说明:**

更新着色器程序配置, 以匹配当前斜坡的带树深度。 RAMP 着色器添加器的名称被设置为 `RAMP_<depth>`, 以便程序管理器缓存并检索正确的变体, `BAND_TREE_DEPTH`预处理器在片段着色器头中定义的预处理器也相应重写。 这使得程序在斜坡结构改变时会被重新编译 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.GradientMap](/api/class/filters-gradientmap) | 否 | 其坡道提供当前波段树深的过滤控制器. |
| _drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图上下文。 不适用此方法 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#updateShaderConfig


> 源码：[src/renderer/webgl/renderNodes/filters/FilterGradientMap.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterGradientMap.js#L101)  
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
