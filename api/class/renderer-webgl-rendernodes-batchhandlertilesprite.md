# BatchHandlerTileSprite {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-batchhandlertilesprite)

一个处理 WebGL 中TileSprite 和 Tile 游戏对象的批量渲染的RenderNode , 它通过将顶点框架数据( 纹理坐标源和源框的尺寸) 传递到着色器上来扩展 `BatchHandlerQuad` , 使着色器能够在框架的界限内正确夹住或包裹纹理坐标。 这对平面图板至关重要, 纹理在表面反复或滚动, 并且不能在纹理图上流血到相邻的帧中 。

支持另外两个渲染选项:`clampFrame`,它防止纹理坐标在框架区域外采样;`wrapFrame`,它使框架区域得到瓦片。这些选项得到动态管理,以便只有在选项改变时才能编译和交换阴影变量。

**构造函数**

`new BatchHandlerTileSprite(manager, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerConfig](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerconfig) | 是 | 此处理器的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BatchHandlerQuad](/api/class/renderer-webgl-rendernodes-batchhandlerquad)  



> 源码：[src/renderer/webgl/renderNodes/BatchHandlerTileSprite.js#L26](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerTileSprite.js#L26)  
引入版本：4.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.BatchHandler](/api/class/renderer-webgl-rendernodes-batchhandler):**


 - [resize](/api/class/renderer-webgl-rendernodes-batchhandler#resize)





**From [Phaser.Renderer.WebGL.RenderNodes.BatchHandlerQuad](/api/class/renderer-webgl-rendernodes-batchhandlerquad):**


 - [batchTextures](/api/class/renderer-webgl-rendernodes-batchhandlerquad#batchTextures)
 - [finalizeTextureCount](/api/class/renderer-webgl-rendernodes-batchhandlerquad#finalizeTextureCount)
 - [pushCurrentBatchEntry](/api/class/renderer-webgl-rendernodes-batchhandlerquad#pushCurrentBatchEntry)
 - [run](/api/class/renderer-webgl-rendernodes-batchhandlerquad#run)
 - [setupTextureUniforms](/api/class/renderer-webgl-rendernodes-batchhandlerquad#setupTextureUniforms)
 - [setupUniforms](/api/class/renderer-webgl-rendernodes-batchhandlerquad#setupUniforms)
 - [updateTextureCount](/api/class/renderer-webgl-rendernodes-batchhandlerquad#updateTextureCount)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### batch {#batch}

#### \<instance> batch(drawingContext, glTexture, x0, y0, x1, y1, x2, y2, x3, y3, texX, texY, texWidth, texHeight, tintMode, tintTL, tintBL, tintTR, tintBR, renderOptions, u0, v0, u1, v1, u2, v2, u3, v3) {#instance-batchdrawingcontext-gltexture-x0-y0-x1-y1-x2-y2-x3-y3-texx-texy-texwidth-texheight-tintmode-tinttl-tintbl-tinttr-tintbr-renderoptions-u0-v0-u1-v1-u2-v2-u3-v3}


**说明:**

在批量中添加一个纹理四进制成的 TileSprite 或 Tile 渲染。 每个顶点都接收到全帧区域( )texX, texY, texWidth, texHeight)这样,着色器就可以在框架界限内夹住或包裹紫外线坐标。如果在调用后批量满了,则立即冲走。如果渲染选项与当前批量所使用的选项不同,则批量也会冲走,并在写入新四位之前更新着色器配置。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| glTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 否 | 纹理要制造。 |
| x0 | number | 否 | 左上角的x坐标. |
| y0 | number | 否 | 左上角的y坐标 |
| x1 | number | 否 | 左下角的x坐标. |
| y1 | number | 否 | 左下角的y坐标. |
| x2 | number | 否 | 右上角的x坐标. |
| y2 | number | 否 | 右上角的y坐标 |
| x3 | number | 否 | 右下角的x坐标. |
| y3 | number | 否 | 右下角的y坐标 |
| texX | number | 否 | 左方的u坐标(0-1). |
| texY | number | 否 | 顶部v坐标( 0-1). |
| texWidth | number | 否 | 纹理的宽度( 0-1). |
| texHeight | number | 否 | 纹理高度(0-1). |
| tintMode | [Phaser.TintModes](/api/namespace/tintmodes) | 否 | 使用锡金模式 。 |
| tintTL | number | 否 | 左上角的颜色 |
| tintBL | number | 否 | 左下角的颜色 |
| tintTR | number | 否 | 右上角的颜色 |
| tintBR | number | 否 | 右下角的颜色 |
| renderOptions | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerQuadRenderOptions](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerquadrenderoptions) | 否 | 具有可选特性。 |
| u0 | number | 否 | 左上角的坐标被扭曲了 |
| v0 | number | 否 | 扭曲的左上角的V坐标 |
| u1 | number | 否 | 扭曲的左下角的u坐标. |
| v1 | number | 否 | 扭曲的左下角的v坐标 。 |
| u2 | number | 否 | 右上角的坐标 |
| v2 | number | 否 | 右上角的V坐标 |
| u3 | number | 否 | 扭曲的右下角的u坐标 |
| v3 | number | 否 | 扭曲的右下角的v坐标 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BatchHandlerQuad# 批量着


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerTileSprite.js#L194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerTileSprite.js#L194)  
引入版本：4.0.0


---

### updateRenderOptions {#updateRenderOptions}

#### \<instance> updateRenderOptions(renderOptions) {#instance-updaterenderoptionsrenderoptions}


**说明:**

读取已收到的渲染选项, 并将其与当前激活的选项进行比较。 如果任何 TileSprite 选项已经改变( `clampFrame`、 `wrapFrame` 或衍生的 `texRes` 旗) , 则设置了内部更改旗, 以便 `updateShaderConfig` 在下次绘图调用前更新活动阴影添加。 同时调用父程序 `BatchHandlerQuad` 执行来处理共享渲染选项 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderOptions | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerQuadRenderOptions](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerquadrenderoptions) | 否 | 选项。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BatchHandlerQuad#updateRenderOptions


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerTileSprite.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerTileSprite.js#L111)  
引入版本：4.0.0


---

### updateShaderConfig {#updateShaderConfig}

#### \<instance> updateShaderConfig() {#instance-updateshaderconfig}


**说明:**

应用任何待处理的选项更改活动阴影程序, 即按要求启用或取消 `TexCoordFrameClamp`和 `TexCoordFrameWrap` 阴影程序添加。 当 `updateRenderOptions` 发现变化时, 在当前批次被冲走后, 使用此选项。 另请使用父 `BatchHandlerQuad` 执行处理共享阴影配置 。


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BatchHandlerQuad#updateShaderConfig


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerTileSprite.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerTileSprite.js#L156)  
引入版本：4.0.0


---

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


 - [defaultConfig](/api/class/renderer-webgl-rendernodes-batchhandlerquad#defaultConfig)
 - [nextRenderOptions](/api/class/renderer-webgl-rendernodes-batchhandlerquad#nextRenderOptions)
 - [renderOptions](/api/class/renderer-webgl-rendernodes-batchhandlerquad#renderOptions)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

---
