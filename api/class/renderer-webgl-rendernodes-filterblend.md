# FilterBlend {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filterblend)

这个 RenderNode 使 Blend 过滤器效果, 将主制成的纹理与二次混合纹理相混合, 使用指定的混合模式( 如 Normal, 乘积, 屏幕, 或 Overlay) 。 活动混合模式被注入到碎片遮蔽器中, 作为在绘图时定义的预处理器, 允许单个遮蔽器程序通过遮蔽器添加支持多个混杂算法 。

通过[Phaser.Filters.Blend](/api/class/filters-blend)过滤控制器间接使用这个RenderNode,它将混合模式,混合纹理,混合量,和锡色等暴露为可配置属性.

见[Phaser.Filters.Blend](/api/class/filters-blend).

**构造函数**

`new FilterBlend(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterBlend.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterBlend.js#L14)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader):**


 - [indexBuffer](/api/class/renderer-webgl-rendernodes-basefiltershader#indexBuffer)
 - [programManager](/api/class/renderer-webgl-rendernodes-basefiltershader#programManager)
 - [vertexBufferLayout](/api/class/renderer-webgl-rendernodes-basefiltershader#vertexBufferLayout)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

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

#### \<instance> setupTextures(controller, textures, drawingContext) {#instance-setuptexturescontroller-textures-drawingcontext}


**说明:**

将混合纹理从滤波控制器指定为纹理槽1. 主制纹理占据了槽0;槽1是碎片遮蔽器混合的二次纹理,与使用主动混合模式相对应.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Blend](/api/class/filters-blend) | 否 | 提供混合纹理的过滤控制器 。 |
| textures | Array.\<WebGLTexture> | 否 | 要填充的纹理阵列。 Index 1 设置在混合纹理中 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupTextures


> 源码：[src/renderer/webgl/renderNodes/filters/FilterBlend.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterBlend.js#L99)  
引入版本：4.0.0


---

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(controller, drawingContext) {#instance-setupuniformscontroller-drawingcontext}


**说明:**

设置混合碎片遮蔽器所需的 WebGL 制服 :

- `uMainSampler2` — 绑定在纹理单元1(混合纹理).

- `amount` — 混合强度,其中`0`只显示主纹理

  和`1`应用了完整的混合效应.

- `color`——混凝土混凝土过程中对混合纹理的一种锡色.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Blend](/api/class/filters-blend) | 否 | 提供统一值的过滤控制器 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupUniforms


> 源码：[src/renderer/webgl/renderNodes/filters/FilterBlend.js#L117](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterBlend.js#L117)  
引入版本：4.0.0


---

### updateShaderConfig {#updateShaderConfig}

#### \<instance> updateShaderConfig(controller, drawingContext) {#instance-updateshaderconfigcontroller-drawingcontext}


**说明:**

更新着色器配置,以匹配过滤器控制器指定的混合模式。该混合模式将解至其字符串名称,并注入碎片着色器中作为一个 `#define BLEND` 通过加贴阴影符预处理器指令。如果控制器指定 `SKIP_CHECK`,混合模式会回到 `NORMAL`如果内部地图中找不到混合模式, `NORMAL` 用作安全默认值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Blend](/api/class/filters-blend) | 否 | 提供混合模式的过滤控制器 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#updateShaderConfig


> 源码：[src/renderer/webgl/renderNodes/filters/FilterBlend.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterBlend.js#L72)  
引入版本：4.0.0


---

---
