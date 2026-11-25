# FilterCombineColorMatrix {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filtercombinecolormatrix)

一个应用[Phaser.Filters.CombineColorMatrix](/api/class/filters-combinecolormatrix)定义的组合颜色矩阵滤镜效果的RenderNode.

这种效果将两个独立的颜色矩阵混合在一起:一个应用到游戏对象本身(`colorMatrixSelf`),一个来源于外部传输纹理(`colorMatrixTransfer`). 每个矩阵都有自己的α乘数,每个通道的额外添加值和乘法值可以提供,以进一步调整最终的颜色输出.

当需要将两个不同来源的颜色分级组合或混合在一个WebGL的单次通过中时,例如将底部的脱饱和度通过与一个有色覆盖的纹理结合时,使用这个滤波器.

**构造函数**

`new FilterCombineColorMatrix(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterCombineColorMatrix.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterCombineColorMatrix.js#L12)  
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

#### \<instance> setupTextures(controller, textures, _drawingContext) {#instance-setuptexturescontroller-textures-_drawingcontext}


**说明:**

将着色器所需的传输纹理捆绑。

将控制器预发的GL纹理指定为纹理槽1,碎片遮蔽器通过`uTransferSampler`制服读取,作为传输颜色矩阵通过的来源.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.CombineColorMatrix](/api/class/filters-combinecolormatrix) | 否 | 提供传输 GL 纹理的过滤控制器 。 |
| textures | Array.\<WebGLTexture> | 否 | 着色器所用的纹理阵列。 传输纹理被写入索引 1 。 |
| _drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图上下文( 此方法未使用) 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupTextures


> 源码：[src/renderer/webgl/renderNodes/filters/FilterCombineColorMatrix.js#L42](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterCombineColorMatrix.js#L42)  
引入版本：4.0.0


---

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(controller, drawingContext) {#instance-setupuniformscontroller-drawingcontext}


**说明:**

上传组合颜色矩阵效应所需的所有遮阳制服。

设置在活动阴影程序上的下列制服:

- `uTransferSampler` — 传输纹理的纹理单元索引.

- `uColorMatrixSelf`——游戏对象本身应用的4×5颜色矩阵.

- `uColorMatrixTransfer`——适用于传输纹理的4×5色矩阵.

- `uAlphaSelf`——自色矩阵的全球α乘数.

- `uAlphaTransfer`——转录颜色矩阵的全球α乘数.

- `uAdditions`——矩阵乘法后每通道添加剂应用抵消.

- `uMultiplications`——在矩阵乘法后应用的每通道乘法因子.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.CombineColorMatrix](/api/class/filters-combinecolormatrix) | 否 | 过滤器控制器提供颜色矩阵数据,α值,添加,以及乘法. |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupUniforms


> 源码：[src/renderer/webgl/renderNodes/filters/FilterCombineColorMatrix.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterCombineColorMatrix.js#L60)  
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
