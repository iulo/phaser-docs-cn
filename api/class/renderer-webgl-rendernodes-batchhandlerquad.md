# BatchHandlerQuad {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-batchhandlerquad)

Phaser的WebGL管道中的主要批次渲染节点,它绘制了大批次的纹理四极(被Image,Sprite,BitmapText,TileSprite等游戏对象使用)用于性能. 支持多纹理,普通地图的照明,以及平滑的像素艺术渲染. 游戏对象被累积成顶点缓冲器,并尽可能在一次抽图调中冲到GPU中.

**构造函数**

`new BatchHandlerQuad(manager, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerConfig](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerconfig) | 是 | 此处理器的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BatchHandler](/api/class/renderer-webgl-rendernodes-batchhandler)  



> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L26](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L26)  
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





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### defaultConfig {#defaultConfig}

#### defaultConfig: [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerConfig](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerconfig) {#defaultconfig-phasertypesrendererwebglrendernodesbatchhandlerconfig}


**说明:**

此处理器的默认配置对象。 与构造器中通过的 `config` 对象合并 。


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L106)  
引入版本：4.0.0


---

### nextRenderOptions {#nextRenderOptions}

#### nextRenderOptions: object {#nextrenderoptions-object}


**说明:**

正在构建的渲染选项 。


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L76)  
引入版本：4.0.0


---

### renderOptions {#renderOptions}

#### renderOptions: object {#renderoptions-object}


**说明:**

当前为批量构建的选项。这些选项有助于定义阴影。


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L49)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.BatchHandler](/api/class/renderer-webgl-rendernodes-batchhandler):**


 - [resize](/api/class/renderer-webgl-rendernodes-batchhandler#resize)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### batch {#batch}

#### \<instance> batch(currentContext, glTexture, x0, y0, x1, y1, x2, y2, x3, y3, texX, texY, texWidth, texHeight, tintMode, tintTL, tintBL, tintTR, tintBR, renderOptions, [args]) {#instance-batchcurrentcontext-gltexture-x0-y0-x1-y1-x2-y2-x3-y3-texx-texy-texwidth-texheight-tintmode-tinttl-tintbl-tinttr-tintbr-renderoptions-args}


**说明:**

给批次加一个四

对于与TRIANGLE_STRIP渲染的兼容性,顶点按顺序写入缓冲器:

- Bottom-left

- Top-left

- Bottom-right

- Top-right

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| currentContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| glTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 否 | 纹理要制造。 |
| x0 | number | 否 | 左上角的x坐标 |
| y0 | number | 否 | 左上角的Y坐标 |
| x1 | number | 否 | 左下角的x坐标 |
| y1 | number | 否 | 左下角的Y坐标 |
| x2 | number | 否 | 右上角的X坐标 |
| y2 | number | 否 | 右上角的Y坐标 |
| x3 | number | 否 | 右下角的x坐标. |
| y3 | number | 否 | 右下角的Y坐标 |
| texX | number | 否 | 左方的u坐标(0-1). |
| texY | number | 否 | 顶部v坐标( 0-1). |
| texWidth | number | 否 | 纹理的宽度( 0-1). |
| texHeight | number | 否 | 纹理高度(0-1). |
| tintMode | number | 否 | 使用锡金模式 。 |
| tintTL | number | 否 | 左上方的颜色 |
| tintBL | number | 否 | 左下色色为色. |
| tintTR | number | 否 | 右上方色色为色. |
| tintBR | number | 否 | 右下色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色色 |
| renderOptions | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerQuadRenderOptions](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerquadrenderoptions) | 否 | 具有可选特性。 |
| args | * | 是 | 子类的附加论据. |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BatchHandler# 批量着


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L623](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L623)  
引入版本：4.0.0


---

### batchTextures {#batchTextures}

#### \<instance> batchTextures(glTexture, renderOptions) {#instance-batchtexturesgltexture-renderoptions}


**说明:**

批量处理的纹理。 这种方法被 `batch` 方法自动称为 。 它返回用于各种纹理任务的数据, 取决于渲染选项 。

纹理基准可用于纹理ID或普通的映射旋转.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| glTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 否 | 纹理要制造。 |
| renderOptions | object | 否 | 当前的选项 。 |


**返回值:** number - 纹理基准.


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L744](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L744)  
引入版本：4.0.0


---

### finalizeTextureCount {#finalizeTextureCount}

#### \<instance> finalizeTextureCount(count) {#instance-finalizetexturecountcount}


**说明:**

最终确定当前子批量的纹理计数。 当渲染运行时, 自动调用。 它请求一个具有必要纹理数量的遮蔽程序, 如果它少于允许的最大值。 这样做会减少 GPU 必须处理的纹理数量, 从而改进性能 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| count | number | 否 | 批次纹理总数. |


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L342](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L342)  



---

### pushCurrentBatchEntry {#pushCurrentBatchEntry}

#### \<instance> pushCurrentBatchEntry() {#instance-pushcurrentbatchentry}


**说明:**

将当前批次条目推入批次条目列表,创建新的批次条目供未来使用.


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L832](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L832)  
引入版本：4.0.0


---

### run {#run}

#### \<instance> run(drawingContext) {#instance-rundrawingcontext}


**说明:**

绘制然后清空当前批次 。

这种方法在批量满满时,或者在需要做其他事情时,由这个节点或管理器自动称为.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BatchHandler#运行


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L550](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L550)  
引入版本：4.0.0


---

### setupTextureUniforms {#setupTextureUniforms}

#### \<instance> setupTextureUniforms(textures) {#instance-setuptextureuniformstextures}


**说明:**

设置当前遮蔽程序的纹理分辨率制服。 具体来说, 此设置了 `uMainResolution` 制服, 上面包含每个绑定纹理的像素尺寸。 这些信息需要遮蔽器的特性, 如平滑像素艺术渲染 。

当批量运行时,此方法自动调用,`texRes`渲染选项被启用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| textures | Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper)> | 否 | 纹理要制造。 |


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L300](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L300)  
引入版本：4.0.0


---

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(drawingContext) {#instance-setupuniformsdrawingcontext}


**说明:**

更新当前遮阳程序制服 。

批量运行时,这种方法会自动调用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L258](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L258)  
引入版本：4.0.0


---

### updateRenderOptions {#updateRenderOptions}

#### \<instance> updateRenderOptions(renderOptions) {#instance-updaterenderoptionsrenderoptions}


**说明:**

将当前生效选项与输入的渲染选项进行比较, 并将任何差异级为 `nextRenderOptions`。 如果任何选项有变化, 将设置 `_renderOptionsChanged` 至 `true` , 并提示当前批次应冲洗, 并在下一张图前通过 `updateShaderConfig` 重建阴影 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderOptions | object | 否 | 新的变形选项。 |


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L384](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L384)  
引入版本：4.0.0


---

### updateShaderConfig {#updateShaderConfig}

#### \<instance> updateShaderConfig() {#instance-updateshaderconfig}


**说明:**

基于渲染选项更新阴影配置。 当渲染选项改变时, 将自动调用 。


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L447](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L447)  
引入版本：4.0.0


---

### updateTextureCount {#updateTextureCount}

#### \<instance> updateTextureCount([count]) {#instance-updatetexturecountcount}


**说明:**

更新每批的最大纹理数量。 这将用新的纹理计数重建阴影程序。 纹理的最低数量是 1, 最大数量是渲染器中定义的纹理单位的数量。 重建阴影可能很昂贵, 所以请节制使用 。

如果这在批次中运行,且新计数低于当前批次条目中的纹理数量,则批次会在阴影程序重建之前被冲洗,因此没有纹理被跳过.

这通常由收听者自动调用`Phaser.Renderer.Events.SET_PARALLEL_TEXTURE_UNITS`事件,由RenderNodeManager触发.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| count | number | 是 | 每批新建的纹理最大数量。如果未定义,则使用纹理单位的最大数量。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BatchHandler#updateTextureCount


> 源码：[src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L195](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/BatchHandlerQuad.js#L195)  
引入版本：4.0.0


---

---
