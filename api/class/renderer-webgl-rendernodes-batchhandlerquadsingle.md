# BatchHandlerQuadSingle {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-batchhandlerquadsingle)

批量处理器(BatchHandler QuadSingle)是用于每批单例渲染四重奏的专用批量处理器,它扩展了批量处理器的类别,并为单次渲染提供了特定的配置,它被用来高效地使只需要单四重奏,具体来说就是过滤器的操作。由于移动设备往往与大型缓冲器大小发生碰撞,所以这一类的设计是为了处理只需要一个四重奏的大小问题。

如果没有提供配置,默认值为:

- `name`:"巴奇汉德勒四角星"

- `shaderName`: 圣歌(歌声)

- `instancesPerBatch`: 1

**构造函数**

`new BatchHandlerQuadSingle(manager, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerConfig](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerconfig) | 是 | 此处理器的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BatchHandlerQuad](/api/class/renderer-webgl-rendernodes-batchhandlerquad)  



> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuadSingle.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuadSingle.js#L10)  
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


 - [defaultConfig](/api/class/renderer-webgl-rendernodes-batchhandlerquad#defaultConfig)
 - [nextRenderOptions](/api/class/renderer-webgl-rendernodes-batchhandlerquad#nextRenderOptions)
 - [renderOptions](/api/class/renderer-webgl-rendernodes-batchhandlerquad#renderOptions)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




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

---
