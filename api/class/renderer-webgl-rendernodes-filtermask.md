# FilterMask {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filtermask)

一个使遮罩过滤器效果的RenderNode,用来使用遮罩纹理选择性显示或隐藏游戏对象的区域.

面具是从一个 [Phaser.Filters.Mask](/api/class/filters-mask) 控制器,它既可以提供静态的 GL 纹理,也可以提供动态渲染的游戏对象作为遮罩。当使用遮罩游戏对象时,如果使用,这个节点将重新将其放入每个框架的纹理中。 `autoUpdate` 已启用,或何时启用 `needsUpdate` 标记。可以选择将面具反转,这样,掩盖的区域就被显示而不是隐藏。

这个节点将源图像绑定在纹理单元0上,将遮罩纹理绑定在纹理单元1上,然后将`invert`旗传递到碎片遮蔽器上,以控制遮罩极性.

见[Phaser.Filters.Mask](/api/class/filters-mask).

**构造函数**

`new FilterMask(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterMask.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterMask.js#L12)  
引入版本：4.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader):**


 - [run](/api/class/renderer-webgl-rendernodes-basefiltershader#run)
 - [updateShaderConfig](/api/class/renderer-webgl-rendernodes-basefiltershader#updateShaderConfig)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### setupTextures {#setupTextures}

#### \<instance> setupTextures(controller, textures, drawingContext) {#instance-setuptexturescontroller-textures-drawingcontext}


**说明:**

准备遮罩滤镜遮蔽器所需的纹理槽.

0纹理单元是源图像(由基类约束),这种方法将遮罩GL纹理指定为1单元,如果控制器有遮罩游戏对象,并且设置了`autoUpdate`或Z`needsUpdate`,那么在绑定前,动态纹理会在当前的绘图上下文维度下重新发回.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Mask](/api/class/filters-mask) | 否 | 提供遮罩纹理和更新旗帜的过滤控制器. |
| textures | Array.\<WebGLTexture> | 否 | 要填充的纹理阵列。 面具纹理被写入索引 1 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图上下文,用于确定动态纹理更新的尺寸. |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupTextures


> 源码：[src/renderer/webgl/renderNodes/filters/FilterMask.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterMask.js#L45)  
引入版本：4.0.0


---

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(controller, drawingContext) {#instance-setupuniformscontroller-drawingcontext}


**说明:**

设置遮罩过滤器所需的遮蔽制服。

将`uMaskSampler`制服套在纹理单元1上,这样,口罩纹理的碎片遮蔽样品就会通过`invert`布林旗来控制口罩是正常应用的还是倒置的.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Mask](/api/class/filters-mask) | 否 | 提供`invert`旗的过滤控制器. |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupUniforms


> 源码：[src/renderer/webgl/renderNodes/filters/FilterMask.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterMask.js#L72)  
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
