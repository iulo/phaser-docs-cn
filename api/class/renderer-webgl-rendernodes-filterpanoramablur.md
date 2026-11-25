# FilterPanoramaBlur {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filterpanoramablur)

这个 RenderNode 使全景线Blur 滤波器效果,它应用了光圈模糊,模拟在宽角或全景镜边看到的扭曲。模糊度由一个半径和一个功率值控制,并使用可配置的横向和纵向样本计数来平衡质量和性能。更高的样本计数以GPU时间为代价产生更平滑的结果。

这个节点管理一个动态的遮荫器添加,将样品计数作为预处理器定义(`SAMPLES_X`和`SAMPLES_Y`)注入碎片遮荫器,因此正确的变体被编译并自动缓存.

见[Phaser.Filters.PanoramaBlur](/api/class/filters-panoramablur).

**构造函数**

`new FilterPanoramaBlur(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterPanoramaBlur.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterPanoramaBlur.js#L12)  
引入版本：4.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader):**


 - [run](/api/class/renderer-webgl-rendernodes-basefiltershader#run)
 - [setupTextures](/api/class/renderer-webgl-rendernodes-basefiltershader#setupTextures)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(controller, _drawingContext) {#instance-setupuniformscontroller-_drawingcontext}


**说明:**

设置全景模糊片段遮蔽器所需的 WebGL 遮蔽器制服。 将模糊半径( `uRadius`) 和模糊的电源( `uPower`) 从过滤器控制器上传到当前运行的程序 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.PanoramaBlur](/api/class/filters-panoramablur) | 否 | 提供半径和功率值的过滤控制器 。 |
| _drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图上下文( 此方法未使用) 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupUniforms


> 源码：[src/renderer/webgl/renderNodes/filters/FilterPanoramaBlur.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterPanoramaBlur.js#L73)  
引入版本：4.0.0


---

### updateShaderConfig {#updateShaderConfig}

#### \<instance> updateShaderConfig(controller, drawingContext) {#instance-updateshaderconfigcontroller-drawingcontext}


**说明:**

更新控制全景模糊片段着色器使用的样本计数的着色器添加。横向和纵向样本计数从控制器读取,并按`SAMPLES_X`和`SAMPLES_Y`预处理器定义注入,导致程序管理器编译并缓存之前没有使用过的合适的着色器变体.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.PanoramaBlur](/api/class/filters-panoramablur) | 否 | 提供样本计数值的过滤控制器 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图上下文( 此方法未使用) 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#updateShaderConfig


> 源码：[src/renderer/webgl/renderNodes/filters/FilterPanoramaBlur.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterPanoramaBlur.js#L52)  
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
