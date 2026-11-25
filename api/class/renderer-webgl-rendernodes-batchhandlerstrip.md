# BatchHandlerStrip {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-batchhandlerstrip)

这个 RenderNode 使三角形条纹, 例如用于游戏对象的绳索。 它使用批次来加速绘图 。

如果一个条条呈交的顶点过多(通常 > 32,768),则会投出一个错误.

注意,你应该叫`batchStrip`而不是`batch`来添加条.

**构造函数**

`new BatchHandlerStrip(manager, config)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerConfig](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerconfig) | 否 | 此处理器的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BatchHandlerQuad](/api/class/renderer-webgl-rendernodes-batchhandlerquad)  



> 源码：[src/renderer/webgl/renderNodes/BatchHandlerStrip.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerStrip.js#L21)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.BatchHandler](/api/class/renderer-webgl-rendernodes-batchhandler):**


 - [batchEntries](/api/class/renderer-webgl-rendernodes-batchhandler#batchEntries)
 - [bytesPerIndexPerInstance](/api/class/renderer-webgl-rendernodes-batchhandler#bytesPerIndexPerInstance)
 - [bytesPerInstance](/api/class/renderer-webgl-rendernodes-batchhandler#bytesPerInstance)
 - [currentBatchEntry](/api/class/renderer-webgl-rendernodes-batchhandler#currentBatchEntry)
 - [floatsPerInstance](/api/class/renderer-webgl-rendernodes-batchhandler#floatsPerInstance)
 - [indexBuffer](/api/class/renderer-webgl-rendernodes-batchhandler#indexBuffer)
 - [indicesPerInstance](/api/class/renderer-webgl-rendernodes-batchhandler#indicesPerInstance)
 - [instanceCount](/api/class/renderer-webgl-rendernodes-batchhandler#instanceCount)
 - [instancesPerBatch](/api/class/renderer-webgl-rendernodes-batchhandler#instancesPerBatch)
 - [maxTexturesPerBatch](/api/class/renderer-webgl-rendernodes-batchhandler#maxTexturesPerBatch)
 - [programManager](/api/class/renderer-webgl-rendernodes-batchhandler#programManager)
 - [vertexBufferLayout](/api/class/renderer-webgl-rendernodes-batchhandler#vertexBufferLayout)
 - [verticesPerInstance](/api/class/renderer-webgl-rendernodes-batchhandler#verticesPerInstance)





**From [Phaser.Renderer.WebGL.RenderNodes.BatchHandlerQuad](/api/class/renderer-webgl-rendernodes-batchhandlerquad):**


 - [nextRenderOptions](/api/class/renderer-webgl-rendernodes-batchhandlerquad#nextRenderOptions)
 - [renderOptions](/api/class/renderer-webgl-rendernodes-batchhandlerquad#renderOptions)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### defaultConfig {#defaultConfig}

#### defaultConfig: [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerConfig](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerconfig) {#defaultconfig-phasertypesrendererwebglrendernodesbatchhandlerconfig}


**说明:**

此处理器的默认配置对象。 与构造器中通过的 `config` 对象合并 。


**重写:** Phaser.Renderer.WebGL.RenderNodes.BatchHandlerQuad#defaultConfig


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerStrip.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerStrip.js#L50)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.BatchHandler](/api/class/renderer-webgl-rendernodes-batchhandler):**


 - [resize](/api/class/renderer-webgl-rendernodes-batchhandler#resize)





**From [Phaser.Renderer.WebGL.RenderNodes.BatchHandlerQuad](/api/class/renderer-webgl-rendernodes-batchhandlerquad):**


 - [batch](/api/class/renderer-webgl-rendernodes-batchhandlerquad#batch)
 - [batchTextures](/api/class/renderer-webgl-rendernodes-batchhandlerquad#batchTextures)
 - [finalizeTextureCount](/api/class/renderer-webgl-rendernodes-batchhandlerquad#finalizeTextureCount)
 - [pushCurrentBatchEntry](/api/class/renderer-webgl-rendernodes-batchhandlerquad#pushCurrentBatchEntry)
 - [run](/api/class/renderer-webgl-rendernodes-batchhandlerquad#run)
 - [setupTextureUniforms](/api/class/renderer-webgl-rendernodes-batchhandlerquad#setupTextureUniforms)
 - [setupUniforms](/api/class/renderer-webgl-rendernodes-batchhandlerquad#setupUniforms)
 - [updateRenderOptions](/api/class/renderer-webgl-rendernodes-batchhandlerquad#updateRenderOptions)
 - [updateShaderConfig](/api/class/renderer-webgl-rendernodes-batchhandlerquad#updateShaderConfig)
 - [updateTextureCount](/api/class/renderer-webgl-rendernodes-batchhandlerquad#updateTextureCount)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### batchStrip {#batchStrip}

#### \<instance> batchStrip(drawingContext, src, calcMatrix, glTexture, vertices, uv, colors, alphas, alpha, tintMode, renderOptions, [debugCallback]) {#instance-batchstripdrawingcontext-src-calcmatrix-gltexture-vertices-uv-colors-alphas-alpha-tintmode-renderoptions-debugcallback}


**说明:**

将一个纹理三角形条添加到批量中。 `vertices`中的每一对顶点构成一个实例。 顶点在写入顶点缓冲器之前由 `calcMatrix` 转换 。

当多个条块一起批量时,通过重复一个条块的最后一个顶点和下一个顶点的顶点,在它们之间自动插入退化的三角形,确保正确的渲染而无需抽取中断.

如果进入的条会溢出当前批次,则批次会先冲出。 如果条本身超过最大批次容量, 则会丢出一个错误 。

这个方法命名为`batchStrip`,而不是`batch`,因为其呼号签名不同于四基游戏对象所使用的标准批量处理器.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| src | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 正在渲染游戏对象 。 |
| calcMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 用于将每个顶点位置转换为世界空间的电流变换矩阵. |
| glTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 否 | 纹理要制造。 |
| vertices | Float32Array | 否 | 条的局部- 空间顶点位置, 作为交替 x 和 y 值的平整数组 。 |
| uv | Float32Array | 否 | 条纹的正态纹理坐标,作为交替u和v值的平整数组,与`vertices`的布局相匹配. |
| colors | Uint32Array | 否 | 横纹的反光色值 |
| alphas | Float32Array | 否 | 横条的横断面α乘数. |
| alpha | number | 否 | 整体α乘数应用在顶点α值之上. |
| tintMode | [Phaser.TintModes](/api/namespace/tintmodes) | 否 | 使用锡金模式 。 |
| renderOptions | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerQuadRenderOptions](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerquadrenderoptions) | 否 | 可选渲染特性。 脱衣渲染使用单个纹理槽, 不支持额外的多纹理。 支持 `smoothPixelArt` 选项; 忽略其他选项 。 |
| debugCallback | function | 是 | 在所有顶点处理后引用的可选回调,在`src`的背景中调用,有三种参数:源游戏对象,总顶点计数,以及一个转换顶点的交替x,y世界空间位置的平整数组. |


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerStrip.js#L128](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerStrip.js#L128)  
引入版本：4.0.0


---

---
