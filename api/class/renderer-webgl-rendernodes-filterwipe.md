# FilterWipe {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filterwipe)

这个 RenderNode 使擦拭过滤器效果, 它将产生方向过渡, 横扫屏幕以揭示或隐藏第二个纹理。 擦拭可以沿着轴线或方向行走, 并具有可配置的边缘柔软度( 宽度) 。 它被 [Phaser.Filters.Wipe](/api/class/filters-wipe) 过滤器控制器用来产生场景过渡或游戏中显示效果 。 见 [Phaser.Filters.Wipe](/api/class/filters-wipe) 。

**构造函数**

`new FilterWipe(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterWipe.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterWipe.js#L12)  
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

将擦拭线套在1号纹理槽上,使其作为二级采样器提供给碎片遮蔽器,随着擦拭的进展而混合.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Wipe](/api/class/filters-wipe) | 否 | 提供擦拭纹理的过滤控制器 。 |
| textures | Array.\<WebGLTexture> | 否 | 此渲染节点的纹理阵列。 索引 1 设置在显式纹理上 。 |
| _drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图上下文( 未使用) 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupTextures


> 源码：[src/renderer/webgl/renderNodes/filters/FilterWipe.js#L37](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterWipe.js#L37)  
引入版本：4.0.0


---

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(controller, _drawingContext) {#instance-setupuniformscontroller-_drawingcontext}


**说明:**

上传来自过滤器控制器的擦拭遮蔽制服。 设置二次纹理采样器单元, 并传递一个 vec4 , 包含当前进度( 0–1 ) 、 擦边软度宽度、 擦拭方向(1 或 - 1 ) 和轴( 0 表示水平, 1 表示垂直) 。 同时上传显示的旗帜, 由它决定擦拭是揭开二次纹理( reveal) 还是覆盖( hide) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Wipe](/api/class/filters-wipe) | 否 | 提供擦拭参数的过滤控制器 。 |
| _drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图上下文( 未使用) 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupUniforms


> 源码：[src/renderer/webgl/renderNodes/filters/FilterWipe.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterWipe.js#L54)  
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
