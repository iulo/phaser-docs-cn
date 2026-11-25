# FilterImageLight {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filterimagelight)

这个 RenderNode 使图像灯滤镜效果,它使用环境图和普通地图模拟游戏对象上基于图像的照明。环境图提供了源照明信息,而普通地图则描述了对象的表面方向,使遮光器可以计算光线如何在表面反射。这在2D场景内产生了令人信服的3D照明效果。

当一个 [Phaser.Filters.ImageLight](/api/class/filters-imagelight) 过滤控制器在游戏对象上活动时使用此节点。 它将环境和正常纹理绑定在正确的采样器槽上, 并上传碎片遮蔽器所需的视图矩阵、 模型旋转、 凸起和颜色因子制服 。

见[Phaser.Filters.ImageLight](/api/class/filters-imagelight).

**构造函数**

`new FilterImageLight(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterImageLight.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterImageLight.js#L12)  
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

将环境图和普通地图WebGL纹理绑定到各自的纹理槽中,环境图被分配到1号槽中,法线贴图被分配到2号槽中,与[Phaser.Renderer.WebGL.RenderNodes.FilterImageLight#setupUniforms](/api/class/renderer-webgl-rendernodes-filterimagelight#setupUniforms)中设定的采样器制服相匹配.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.ImageLight](/api/class/filters-imagelight) | 否 | 提供纹理参考的过滤控制器 。 |
| textures | Array.\<WebGLTexture> | 否 | 要填充的纹理槽阵列 。 |
| _drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图上下文( 未使用) 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupTextures


> 源码：[src/renderer/webgl/renderNodes/filters/FilterImageLight.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterImageLight.js#L43)  
引入版本：4.0.0


---

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(controller, _drawingContext) {#instance-setupuniformscontroller-_drawingcontext}


**说明:**

上传图像光片遮蔽器所需的遮蔽制服,包括环境和普通地图纹理的采样器指数,用于在世界空间中引导环境图的视图矩阵,被过滤对象的模型旋转,控制环境反射的球形扭曲的凸起因子,以及将照明贡献与原始对象颜色混合的颜色因子.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.ImageLight](/api/class/filters-imagelight) | 否 | 提供统一值的过滤控制器 。 |
| _drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图上下文( 未使用) 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupUniforms


> 源码：[src/renderer/webgl/renderNodes/filters/FilterImageLight.js#L64](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterImageLight.js#L64)  
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
