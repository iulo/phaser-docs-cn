# FilterDisplacement {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filterdisplacement)

将移位滤波器作用应用到WebGL渲染管道的RenderNode。

移位过滤会使用移位图纹理来抵消源图像的像素. 移位图的红色通道控制水平偏移,绿色通道控制垂直偏移。 移位的大小会由控制器的`x`和`y`的量值来缩放, 允许您在运行时创建波, 热潮, 以及类似的扭曲效果 。

这个节点由 [Phaser.Filters.Displacement](/api/class/filters-displacement) 内部使用, 通常不会直接被即时化。 在游戏对象或相机上使用移位过滤器来应用此效果 。

**构造函数**

`new FilterDisplacement(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterDisplacement.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterDisplacement.js#L12)  
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

#### \<instance> setupTextures(controller, textures) {#instance-setuptexturescontroller-textures}


**说明:**

将此过滤器所用的移位图纹理捆绑 。

将控制器的WebGL移位纹理指定为纹理插槽1,该插槽将`uDisplacementSampler`制服映射在碎片遮蔽器中.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Displacement](/api/class/filters-displacement) | 否 | 提供流离图纹理的流离过滤控制器 。 |
| textures | Array.\<WebGLTexture> | 否 | 此渲染的纹理阵列已过。 移位纹理被写入索引 1 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupTextures


> 源码：[src/renderer/webgl/renderNodes/filters/FilterDisplacement.js#L42](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterDisplacement.js#L42)  
引入版本：4.0.0


---

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(controller, drawingContext) {#instance-setupuniformscontroller-drawingcontext}


**说明:**

设置移位过滤器所需的遮蔽制服。

将移位采样器指数和移位量矢量传递到碎片遮蔽器。量矢量是一个两个组成部分值,其x和y两个组成部分分别按照[Phaser.Filters.Displacement](/api/class/filters-displacement)控制器的定义,对水平和垂直移位进行比例测量。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Displacement](/api/class/filters-displacement) | 否 | 提供转移量值的“流离失所过滤控制器”。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupUniforms


> 源码：[src/renderer/webgl/renderNodes/filters/FilterDisplacement.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterDisplacement.js#L59)  
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
