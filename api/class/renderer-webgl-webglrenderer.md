# WebGLRenderer {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-webglrenderer)

WebGLRenderer 是包含保持WebGLRenering Context状态清洁所需的功能的类。WebGLLRenderer的主要想法是跟踪任何发生于上下文变化的线索 WebGL 内置 Phaser。这意味着如果在 effect 的 WebGLRenderer 外调用原始的 Webgl 函数 Phaser WebGL 使生态系统发生污染,它们可能会污染当前产生意外行为的 WebGLRendering Context 状态。 WebGL 交互是通过WebGLRenderer和/或内置的Render节点实现的.

持久 WebGL对象存储在 WebGLRender 创建的“ 包装器” 中。 包装器包含 WebGL对象和关于这些对象的元数据。 用于在上下文丢失后重现 WebGL状态。 倾向于通过对包装器的引用, 而不是原始的 WebGL对象, 因为原始对象可能随时被销毁或替换。 只有在需要时才提取它们 。

WebGL状态,如混合模式或纹理单元,由WebGLRender管理. 使用`WebGLRenderer.glWrapper`来管理当前状态,而不是直接设置在WebGLLRenderingContext上. 状态包装器将确保状态只有在改变时才被设定,并且在上下文丢失或外部渲染调用后可以恢复状态.

**构造函数**

`new WebGLRenderer(game)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 拥有这个WebGL渲染器的游戏实例. |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/renderer/webgl/WebGLRenderer.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L44)  
引入版本：3.0.0

## 公开成员 {#public-members}

### baseDrawingContext {#baseDrawingContext}

#### baseDrawingContext: [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) {#basedrawingcontext-phaserrendererwebgldrawingcontext}


**说明:**

用于底画布的绘图康特文.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L323](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L323)  
引入版本：4.0.0


---

### blankTexture {#blankTexture}

#### blankTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#blanktexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

空白的 32x32 透明纹理, 需要时为图形系统使用。 此设置在 `boot` 方法中 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L527](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L527)  
引入版本：3.12.0


---

### blendModes {#blendModes}

#### blendModes: Array.\<[Phaser.Types.Renderer.WebGL.WebGLBlendParameters](/api/typedef/types-renderer-webgl#webglblendparameters)> {#blendmodes-arrayphasertypesrendererwebglwebglblendparameters}


**说明:**

由 WebGL 渲染器支持的混合模式阵列 。

这个阵列包括默认的混合模式以及通过[#addBlendMode](#addBlendMode)添加的任何自定义混合模式.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L199](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L199)  
引入版本：3.0.0


---

### cameraRenderNode {#cameraRenderNode}

#### cameraRenderNode: [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode) {#camerarendernode-phaserrendererwebglrendernodesrendernode}


**说明:**

用于渲染单个摄像机的RenderNode.

使用`boot`方法时,将使用该方法。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L150)  
引入版本：4.0.0


---

### canvas {#canvas}

#### canvas: HTMLCanvasElement {#canvas-htmlcanvaselement}


**说明:**

这WebGL的画布 被画到。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L190](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L190)  
引入版本：3.0.0


---

### compression {#compression}

#### compression: [Phaser.Types.Renderer.WebGL.WebGLTextureCompression](/api/typedef/types-renderer-webgl#webgltexturecompression) {#compression-phasertypesrendererwebglwebgltexturecompression}


**说明:**

存储此设备及浏览器所支持的 WebGL 纹理压缩格式 。

Phaser版本3.60中增加了对使用压缩纹理格式的支持.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L506](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L506)  
引入版本：3.8.0


---

### config {#config}

#### config: object {#config-object}


**说明:**

此 WebGL 渲染器的本地配置设置 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L100)  
引入版本：3.0.0


---

### contextLost {#contextLost}

#### contextLost: boolean {#contextlost-boolean}


**说明:**

如果渲染器的 WebGL 上下文丢失, 此属性将被设定为 `true` 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L211](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L211)  
引入版本：3.0.0


---

### contextLostHandler {#contextLostHandler}

#### contextLostHandler: function {#contextlosthandler-function}


**说明:**

上下文丢失时引用的处理器。 不应更改, 并设置在启动方法中 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L351](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L351)  
引入版本：3.19.0


---

### contextRestoredHandler {#contextRestoredHandler}

#### contextRestoredHandler: function {#contextrestoredhandler-function}


**说明:**

恢复上下文时要引用的处理器。 不应更改, 并设置在启动方法中 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L361](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L361)  
引入版本：3.19.0


---

### currentViewCamera {#currentViewCamera}

#### currentViewCamera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#currentviewcamera-phasercamerasscene2dcamera}


**说明:**

摄像机目前由`render`提供.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L332](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L332)  
引入版本：4.0.0


---

### drawingBufferHeight {#drawingBufferHeight}

#### drawingBufferHeight: number {#drawingbufferheight-number}


**说明:**

缓冲图缓冲高度以减少 gl 调用 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L517](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L517)  
引入版本：3.11.0


---

### drawingContextPool {#drawingContextPool}

#### drawingContextPool: [Phaser.Renderer.WebGL.DrawingContextPool](/api/class/renderer-webgl-drawingcontextpool) {#drawingcontextpool-phaserrendererwebgldrawingcontextpool}


**说明:**

一组可以重复使用的绘图连接符。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L342](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L342)  
引入版本：4.0.0


---

### extensions {#extensions}

#### extensions: object {#extensions-object}


**说明:**

WebGL扩展装入当前上下文中.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L485](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L485)  
引入版本：3.0.0


---

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

拥有这个WebGL渲染器的游戏实例.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L122](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L122)  
引入版本：3.0.0


---

### genericQuadIndexBuffer {#genericQuadIndexBuffer}

#### genericQuadIndexBuffer: [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) {#genericquadindexbuffer-phaserrendererwebglwrapperswebglbufferwrapper}


**说明:**

通用四边形索引缓冲器。 这是 READ- ONLY 缓冲器。 它描述四边形的四角, 这种结构在渲染器的多个位置使用 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L311](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L311)  
引入版本：4.0.0


---

### gl {#gl}

#### gl: WebGLRenderingContext {#gl-webglrenderingcontext}


**说明:**

渲染器的深层的 WebGL 上下文.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L391](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L391)  
引入版本：3.0.0


---

### glBufferWrappers {#glBufferWrappers}

#### glBufferWrappers: Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper)> {#glbufferwrappers-arrayphaserrendererwebglwrapperswebglbufferwrapper}


**说明:**

此渲染器创建的所有 WebGL 缓冲器列表 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L266](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L266)  
引入版本：3.80.0


---

### glFormats {#glFormats}

#### glFormats: array {#glformats-array}


**说明:**

存储当前 WebGL 组件格式供进一步使用。

这个阵列被包含在 `init` 方法中.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L495](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L495)  
引入版本：3.2.0


---

### glFramebufferWrappers {#glFramebufferWrappers}

#### glFramebufferWrappers: Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](/api/class/renderer-webgl-wrappers-webglframebufferwrapper)> {#glframebufferwrappers-arrayphaserrendererwebglwrapperswebglframebufferwrapper}


**说明:**

此渲染器创建的所有 WebGLFramebuswrappers 列表 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L293](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L293)  
引入版本：3.80.0


---

### glProgramWrappers {#glProgramWrappers}

#### glProgramWrappers: Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](/api/class/renderer-webgl-wrappers-webglprogramwrapper)> {#glprogramwrappers-arrayphaserrendererwebglwrapperswebglprogramwrapper}


**说明:**

此渲染器创建的所有 WebGL 程序程序解析器列表 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L275](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L275)  
引入版本：3.80.0


---

### glTextureUnits {#glTextureUnits}

#### glTextureUnits: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureUnitsWrapper](/api/class/renderer-webgl-wrappers-webgltextureunitswrapper) {#gltextureunits-phaserrendererwebglwrapperswebgltextureunitswrapper}


**说明:**

正在使用的当前 WebGL 纹理单元 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L411](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L411)  
引入版本：4.0.0


---

### glTextureWrappers {#glTextureWrappers}

#### glTextureWrappers: Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper)> {#gltexturewrappers-arrayphaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

此渲染器创建的所有 WebGLTexture Wrappers 列表 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L284](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L284)  
引入版本：3.80.0


---

### glVAOWrappers {#glVAOWrappers}

#### glVAOWrappers: Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLVAOWrapper](/api/class/renderer-webgl-wrappers-webglvaowrapper)> {#glvaowrappers-arrayphaserrendererwebglwrapperswebglvaowrapper}


**说明:**

此渲染器创建的所有 WebGLVAO rappers 列表 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L302](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L302)  
引入版本：4.0.0


---

### glWrapper {#glWrapper}

#### glWrapper: [Phaser.Renderer.WebGL.Wrappers.WebGLGlobalWrapper](/api/class/renderer-webgl-wrappers-webglglobalwrapper) {#glwrapper-phaserrendererwebglwrapperswebglglobalwrapper}


**说明:**

当前的WebGLRendering Context状态.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L401](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L401)  
引入版本：4.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

显示显示在 onResize 事件处理器中 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L180](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L180)  
引入版本：3.0.0


---

### instancedArraysExtension {#instancedArraysExtension}

#### instancedArraysExtension: ANGLE_instanced_arrays {#instancedarraysextension-angle_instanced_arrays}


**说明:**

如果浏览器支持`ANGLE_instanced_arrays`扩展,此属性会为其保留一个引用glExtension的功能.

这是一种`setExtensions`方法。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L432](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L432)  
引入版本：3.50.0


---

### isBooted {#isBooted}

#### isBooted: boolean {#isbooted-boolean}


**说明:**

变形器已经启动了吗?


> 源码：[src/renderer/webgl/WebGLRenderer.js#L604](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L604)  
引入版本：3.50.0


---

### maxTextures {#maxTextures}

#### maxTextures: number {#maxtextures-number}


**说明:**

GPU 所能处理的纹理的最大数量。 WebGL1 spec 下最小的为 8. 这是通过 Game Config `maxTextures` 属性设定的, 启动后绝不应更改 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L245](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L245)  
引入版本：3.50.0


---

### mipmapFilter {#mipmapFilter}

#### mipmapFilter: GLenum {#mipmapfilter-glenum}


**说明:**

用于创建纹理的缩写 magFilter 。

您可以在游戏配置中将此指定为字符串, 即:

`render: { mipmapFilter: 'NEAREST_MIPMAP_LINEAR' }`

WebGL1的6个选项按从最低到最昂贵的计算顺序排列:

NEAREST(用于像素艺术) LINEAR(默认) NEAREST_MIPMAP_NEAREST LINEAR_MIPMAP_NEAREST NEAREST_MIPMAP_LINEAR_MIPMAP_LINEAR

咪咪咪只与体积完全为2的纹理配合.

详情见[https://webglfundamentals.org/webgl/lessons/webgl-3d-textures.html](https://webglfundamentals.org/webgl/lessons/webgl-3d-textures.html)

截至 v3.60 , 除非游戏配置中给出字符串, 否则不会生成 mipmaps 。 不需要时, 这会保存在 VRAM 上 。 要获得上一个结果, 将属性设置为配置中的 `LINEAR` 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L574](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L574)  
引入版本：3.21.0


---

### normalTexture {#normalTexture}

#### normalTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#normaltexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

空白 1x1 # 7f7ff 纹理, 平坦的普通地图, 需要时由图形系统使用。 设置在 `boot` 方法中 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L538](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L538)  
引入版本：3.80.0


---

### parallelShaderCompileExtension {#parallelShaderCompileExtension}

#### parallelShaderCompileExtension: KHR_parallel_shader_compile {#parallelshadercompileextension-khr_parallel_shader_compile}


**说明:**

如果浏览器支持`KHR_parallel_shader_compile`扩展,此属性会为其保留一个引用glExtension的功能.

这是一种`setExtensions`方法。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L445](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L445)  
引入版本：4.0.0


---

### previousContextLostHandler {#previousContextLostHandler}

#### previousContextLostHandler: function {#previouscontextlosthandler-function}


**说明:**

之前使用的 contextLostHandler 。 使用 `setContextHandlers` 时设定此选项 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L371](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L371)  
引入版本：3.85.0


---

### previousContextRestoredHandler {#previousContextRestoredHandler}

#### previousContextRestoredHandler: function {#previouscontextrestoredhandler-function}


**说明:**

之前使用的 contextRestoredHandler 。 使用 `setContextHandlers` 时设定此选项 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L381](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L381)  
引入版本：3.85.0


---

### projectionFlipY {#projectionFlipY}

#### projectionFlipY: boolean {#projectionflipy-boolean}


**说明:**

缓存的 flipY 状态的投影矩阵 。

这通常是`false`, 保存WebGL坐标空间.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L640](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L640)  
引入版本：4.0.0


---

### projectionHeight {#projectionHeight}

#### projectionHeight: number {#projectionheight-number}


**说明:**

投影矩阵的缓存高度 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L631](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L631)  
引入版本：3.50.0


---

### projectionMatrix {#projectionMatrix}

#### projectionMatrix: [Phaser.Math.Matrix4](/api/class/math-matrix4) {#projectionmatrix-phasermathmatrix4}


**说明:**

全球游戏Projection矩阵,被遮阳器用作"uProjectionMatrix"制服.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L613](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L613)  
引入版本：3.50.0


---

### projectionWidth {#projectionWidth}

#### projectionWidth: number {#projectionwidth-number}


**说明:**

投影矩阵的缓存宽度 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L622](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L622)  
引入版本：3.50.0


---

### renderNodes {#renderNodes}

#### renderNodes: [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) {#rendernodes-phaserrendererwebglrendernodesrendernodemanager}


**说明:**

一个处理 WebGLRender 所使用的所有 Render 节点的 Render 节点管理器类的例子 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L140)  
引入版本：4.0.0


---

### shaderProgramFactory {#shaderProgramFactory}

#### shaderProgramFactory: [Phaser.Renderer.WebGL.ShaderProgramFactory](/api/class/renderer-webgl-shaderprogramfactory) {#shaderprogramfactory-phaserrendererwebglshaderprogramfactory}


**说明:**

用于管理变种荫影的遮荫器程序工厂.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L161](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L161)  
引入版本：4.0.0


---

### shaderSetters {#shaderSetters}

#### shaderSetters: [Phaser.Renderer.WebGL.Wrappers.WebGLShaderSetterWrapper](/api/class/renderer-webgl-wrappers-webglshadersetterwrapper) {#shadersetters-phaserrendererwebglwrapperswebglshadersetterwrapper}


**说明:**

gl 函数映射用于统一和属性的查看.

[https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/uniform](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/uniform)

[https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/vertexAttribPointer](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/vertexAttribPointer)


> 源码：[src/renderer/webgl/WebGLRenderer.js#L561](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L561)  
引入版本：4.0.0


---

### snapshotState {#snapshotState}

#### snapshotState: [Phaser.Types.Renderer.Snapshot.SnapshotState](/api/typedef/types-renderer-snapshot#snapshotstate) {#snapshotstate-phasertypesrenderersnapshotsnapshotstate}


**说明:**

详细介绍目前计划中的快照 。

如果在此对象中设置了非null `callback`,则在当前框架完全渲染后将拍摄画布的快照.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L221](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L221)  
引入版本：3.0.0


---

### spector {#spector}

#### spector: function {#spector-function}


**说明:**

用于WebGL调试的SpectorJS实例.

仅在 Phaser 调试构建中可用 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L651](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L651)  
引入版本：3.60.0


---

### standardDerivativesExtension {#standardDerivativesExtension}

#### standardDerivativesExtension: OES_standard_derivatives {#standardderivativesextension-oes_standard_derivatives}


**说明:**

如果浏览器支持`OES_standard_derivatives`扩展,而`smoothPixelArt`配置选项是真实的,则此属性会为其保留一个glExtension的引用.

这是一种`setExtensions`方法。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L458](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L458)  
引入版本：4.0.0


---

### supportedExtensions {#supportedExtensions}

#### supportedExtensions: Array.\<string> {#supportedextensions-arraystring}


**说明:**

显示浏览器支持 WebGL扩展的字符串。 串是 `setExtensions` 方法所覆盖的 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L421](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L421)  
引入版本：3.0.0


---

### textureUnitIndices {#textureUnitIndices}

#### textureUnitIndices: Array.\<number> {#textureunitindices-arraynumber}


**说明:**

包含所有可用纹理单位索引的列表。 其包含在 `init` 方法中。 它用于将纹理单位与遮蔽器连接。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L255](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L255)  
引入版本：4.0.0


---

### type {#type}

#### type: number {#type-number}


**说明:**

常数,可以方便地将渲染器识别为WebGL渲染器.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L131](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L131)  
引入版本：3.0.0


---

### vaoExtension {#vaoExtension}

#### vaoExtension: OES_vertex_array_object {#vaoextension-oes_vertex_array_object}


**说明:**

如果浏览器支持`OES_vertex_array_object`扩展,此属性会为其保留一个引用glExtension的功能.

这是一种`setExtensions`方法。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L472](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L472)  
引入版本：3.50.0


---

### whiteTexture {#whiteTexture}

#### whiteTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#whitetexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

纯白的4x4纹理, 需要时为图形系统使用。 此设置在 `boot` 方法中 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L550](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L550)  
引入版本：3.50.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

向画布的宽度。 位于 onResize 事件处理器中 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L170](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L170)  
引入版本：3.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Events.EventEmitter](/api/class/events-eventemitter):**


 - [addListener](/api/class/events-eventemitter#addListener)
 - [emit](/api/class/events-eventemitter#emit)
 - [eventNames](/api/class/events-eventemitter#eventNames)
 - [listenerCount](/api/class/events-eventemitter#listenerCount)
 - [listeners](/api/class/events-eventemitter#listeners)
 - [off](/api/class/events-eventemitter#off)
 - [on](/api/class/events-eventemitter#on)
 - [once](/api/class/events-eventemitter#once)
 - [removeAllListeners](/api/class/events-eventemitter#removeAllListeners)
 - [removeListener](/api/class/events-eventemitter#removeListener)
 - [shutdown](/api/class/events-eventemitter#shutdown)




---

## 公开方法 {#public-methods}

### addBlendMode {#addBlendMode}

#### \<instance> addBlendMode(func, equation) {#instance-addblendmodefunc-equation}


**说明:**

为渲染器创建新的自定义混合模式。

见[https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Constants#Blending_modes](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Constants#Blending_modes)

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| func | Array.\<GLenum> | 否 | 包含 WebGL 函数的阵列, 用于源和目的混合因子。 请参看 QQlink WebGLRendering Context# blendFunc ()} 可能的常数 。 |
| equation | GLenum | 否 | 用于将新像素的 RGB 和 alpha 组件与渲染的像素组合的公式。 请参见 QQlink WebGLRendering Context# blendEquation()} 可能的常数 。 |


**返回值:** number - 新的混合模式的索引,用于今后参考.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1556](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1556)  
引入版本：3.0.0


---

### canvasToTexture {#canvasToTexture}

#### \<instance> canvasToTexture(srcCanvas, [dstTexture], [noRepeat], [flipY]) {#instance-canvastotexturesrccanvas-dsttexture-norepeat-flipy}


**说明:**

创建基于给定的 Canvas 元素的新 WebGL 纹理 。

如果给出了`dstTexture`参数,则更新了WebGL纹理,而不是创建了新鲜的.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| srcCanvas | HTMLCanvasElement | 否 |  | 创建 WebGL 纹理的帆布 |
| dstTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 是 |  | 要设置的目的地 WebGLTextureWrapper 。 |
| noRepeat | boolean | 是 | false | 是否允许此画布设置 `REPEAT`( 如文本对象) ? |
| flipY | boolean | 是 | true | 是否应该用WebGL纹理设定`UNPACK_FLIP_Y_WEBGL`? |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) - 新建或更新的WebGLTextureWrapper.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2283](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2283)  
引入版本：3.0.0


---

### captureFrame {#captureFrame}

#### \<instance> captureFrame([quickCapture], [fullCapture]) {#instance-captureframequickcapture-fullcapture}


**说明:**

这种方法仅在Phaser的除臭建筑中,或Webpack配置中设置的`WEBGL_DEBUG`旗的建筑中可以使用.

Phaser v3.60 调试器内嵌了Spector.js的构件,是WebGL的检查员,可以现场检查您的WebGL呼叫。虽然将Spector扩展器添加到桌面浏览器中很容易,但通过嵌入Phaser,我们也可以在移动浏览器中提供,使其成为在不允许扩展的移动设备上调试ZWebGL游戏的强大工具.

详情请见[https://github.com/BabylonJS/Spector.js](https://github.com/BabylonJS/Spector.js)。

这种方法将捕获当前WebGL框架,并发送给Spector.js工具进行检查.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| quickCapture | boolean | 是 | false | 如果`true`缩略图没有被捕获,以加速捕获. |
| fullCapture | boolean | 是 | false | 如果`true`所有的细节都被捕获. |


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1075](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1075)  
引入版本：3.60.0


---

### captureNextFrame {#captureNextFrame}

#### \<instance> captureNextFrame() {#instance-capturenextframe}


**说明:**

这种方法仅在Phaser的除臭建筑中,或Webpack配置中设置的`WEBGL_DEBUG`旗的建筑中可以使用.

Phaser v3.60 调试器内嵌了Spector.js的构件,是WebGL的检查员,可以现场检查您的WebGL呼叫。虽然将Spector扩展器添加到桌面浏览器中很容易,但通过嵌入Phaser,我们也可以在移动浏览器中提供,使其成为在不允许扩展的移动设备上调试ZWebGL游戏的强大工具.

详情请见[https://github.com/BabylonJS/Spector.js](https://github.com/BabylonJS/Spector.js)。

这种方法将捕获下一个WebGL框架,并发送给Spector.js工具进行检查.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1108)  
引入版本：3.60.0


---

### clearFramebuffer {#clearFramebuffer}

#### \<instance> clearFramebuffer([color], [stencil], [depth]) {#instance-clearframebuffercolor-stencil-depth}


**说明:**

清除当前帧缓冲器到给定颜色 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | Array.\<number> | 是 | 要清除的颜色。 介于 0.0 - 1. 0 之间的四个值。 |
| stencil | number | 是 | 清净的质素值 |
| depth | number | 是 | 要清除的深度值。 目前, 尚未设置, 仅决定深度缓冲是否被清除 。 |


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1636](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1636)  
引入版本：4.0.0


---

### createCanvasTexture {#createCanvasTexture}

#### \<instance> createCanvasTexture(srcCanvas, [noRepeat], [flipY]) {#instance-createcanvastexturesrccanvas-norepeat-flipy}


**说明:**

创建基于给定的 Canvas 元素的新 WebGL 纹理 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| srcCanvas | HTMLCanvasElement | 否 |  | 制作WebGL纹理的帆布 |
| noRepeat | boolean | 是 | false | 是否允许此画布设置 `REPEAT`( 如文本对象) ? |
| flipY | boolean | 是 | true | 是否应该用WebGL纹理设定`UNPACK_FLIP_Y_WEBGL`? |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) - 新建的WebGLTextureWrapper. 中国植物物种信息数据库.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2337](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2337)  
引入版本：3.20.0


---

### createFramebuffer {#createFramebuffer}

#### \<instance> createFramebuffer(renderTexture, [addStencilBuffer], [addDepthBuffer]) {#instance-createframebufferrendertexture-addstencilbuffer-adddepthbuffer}


**说明:**

创建 WebGL框架缓冲器对象,并可选择地绑定深度速率制成缓冲器。

这将解开当前任何绑定的帧缓冲器 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| renderTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) \| Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper)> | null | 否 |  | 写着颜色像素的颜色纹理。 指定多个颜色附件的阵列, 但 WebGL1 默认只支持第一个颜色附件。 指定 `null` 来为底画布创建帧缓冲器 。 |
| addStencilBuffer | boolean | 是 | false | 创建缓冲器吗 ? |
| addDepthBuffer | boolean | 是 | false | 创建深处的缓冲器 ? |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](/api/class/renderer-webgl-wrappers-webglframebufferwrapper) - 装有装帧缓冲器, 与渲染器一起安全使用 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1759](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1759)  
引入版本：3.0.0


---

### createIndexBuffer {#createIndexBuffer}

#### \<instance> createIndexBuffer(initialDataOrSize, bufferUsage) {#instance-createindexbufferinitialdataorsize-bufferusage}


**说明:**

用于创建索引缓冲器的折叠器 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| initialDataOrSize | ArrayBuffer | 否 | 或显示 vbo 大小的矩阵缓冲器 。 |
| bufferUsage | number | 否 | 缓冲器是如何使用的. gl.DYNAMIC_DRAW, gl.STATIC_DRAW 或 gl.STREAM_DRAW. |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) - 已包装索引缓冲器


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1830](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1830)  
引入版本：3.0.0


---

### createProgram {#createProgram}

#### \<instance> createProgram(vertexShader, fragmentShader) {#instance-createprogramvertexshader-fragmentshader}


**说明:**

基于给定的顶点和碎片阴影源创建 WebGL 方案实例。

然后在包扎和返回程序之前编译,附加和链接程序.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vertexShader | string | 否 | 顶点阴影源代码作为单弦. |
| fragmentShader | string | 否 | 碎片荫影源代码作为单字符串. |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](/api/class/renderer-webgl-wrappers-webglprogramwrapper) - 由给定的遮阳器源创建的包扎,链接的WebGL方案.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1791](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1791)  
引入版本：3.0.0


---

### createTexture2D {#createTexture2D}

#### \<instance> createTexture2D(mipLevel, minFilter, magFilter, wrapT, wrapS, format, pixels, width, height, [pma], [forceSize], [flipY]) {#instance-createtexture2dmiplevel-minfilter-magfilter-wrapt-wraps-format-pixels-width-height-pma-forcesize-flipy}


**说明:**

创建 WebGLTexture Wrapper 的包装器。 如果没有像素数据被传递, 它将创建空质素 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| mipLevel | number | 否 |  | 纹理的米普级. |
| minFilter | number | 否 |  | 过滤纹理。 |
| magFilter | number | 否 |  | 过滤纹理。 |
| wrapT | number | 否 |  | 纹理的包扎模式 。 |
| wrapS | number | 否 |  | 纹理的包扎模式 。 |
| format | number | 否 |  | 纹理使用哪种格式 。 |
| pixels | object | 否 |  | 像素数据. |
| width | number | 否 |  | 纹理的宽度以像素表示。 如果得不到, 则必须从 `pixels` 中获取 。 |
| height | number | 否 |  | 纹理高度以像素表示。 如果不提供, 则必须从 `pixels` 中得出 。 |
| pma | boolean | 是 | true | 纹理是否预先多倍化了α? |
| forceSize | boolean | 是 | false | 如果 `true` , 它会使用向这种方法传递的宽度和高度, 不管像素的尺寸大小如何. |
| flipY | boolean | 是 | true | 设置 `UNPACK_FLIP_Y_WEBGL` 上传时的 WebGL 纹理用途的标志 。 |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) - 创建的 WebGLTexture Wrapper 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1726](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1726)  
引入版本：3.0.0


---

### createTextureFromSource {#createTextureFromSource}

#### \<instance> createTextureFromSource(source, width, height, scaleMode, [forceClamp], [flipY]) {#instance-createtexturefromsourcesource-width-height-scalemode-forceclamp-flipy}


**说明:**

从图像源创建纹理。如果源不合法,则创建空纹理。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| source | object | 否 |  | 纹理之源. |
| width | number | 否 |  | 纹理的宽度. |
| height | number | 否 |  | 纹理的高度. |
| scaleMode | number | 否 |  | 纹理所使用的比例模式 。 |
| forceClamp | boolean | 是 | false | 强制纹理使用 CLAMP_TO_EDGE 包模式, 即使有2 个功率 ? |
| flipY | boolean | 是 | true | 设置 `UNPACK_FLIP_Y_WEBGL` 上传时的 WebGL 纹理用途的标志 。 |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) - 创建的WebGLTextureWrapper,或者无法创建的`null`.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1666](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1666)  
引入版本：3.0.0


---

### createUint8ArrayTexture {#createUint8ArrayTexture}

#### \<instance> createUint8ArrayTexture(data, width, height, [pma], [flipY]) {#instance-createuint8arraytexturedata-width-height-pma-flipy}


**说明:**

从 Uint8 箭头创建 WebGLTexture 。

Uint8Array被假定为RGBA值,每个颜色组件一个字节.

纹理会用 `gl.NEAREST` 过滤, 不会被遮住 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| data | Uint8Array | 否 |  | 创建纹理的 Uint8 箭头 。 |
| width | number | 否 |  | 纹理的宽度. |
| height | number | 否 |  | 纹理的高度. |
| pma | boolean | 是 | true | 纹理是否应该设定为具有预倍倍倍的α? |
| flipY | boolean | 是 | true | 是否应该用WebGL纹理设定`UNPACK_FLIP_Y_WEBGL`? |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) - 新建的WebGLTextureWrapper. 中国植物物种信息数据库.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2473](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2473)  
引入版本：3.80.0


---

### createVAO {#createVAO}

#### \<instance> createVAO(program, indexBuffer, attributeBufferLayouts) {#instance-createvaoprogram-indexbuffer-attributebufferlayouts}


**说明:**

用于创建顶点阵列对象的折叠器。此操作管理顶点属性约束状态。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| program | [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](/api/class/renderer-webgl-wrappers-webglprogramwrapper) | 否 | 将VAO绑定的程序. |
| indexBuffer | [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) | 否 | 指数缓冲器. |
| attributeBufferLayouts | Array.\<[Phaser.Types.Renderer.WebGL.WebGLAttributeBufferLayout](/api/typedef/types-renderer-webgl#webglattributebufferlayout)> | 否 | 属性缓冲布局. |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLVAOWrapper](/api/class/renderer-webgl-wrappers-webglvaowrapper) - 新创建的WebGLVAOWrapper.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1849](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1849)  
引入版本：4.0.0


---

### createVertexBuffer {#createVertexBuffer}

#### \<instance> createVertexBuffer(initialDataOrSize, bufferUsage) {#instance-createvertexbufferinitialdataorsize-bufferusage}


**说明:**

用于创建顶点缓冲器的包装器 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| initialDataOrSize | ArrayBuffer | 否 | 它不是指向线粒体,就是指向 vbo 大小的整数 |
| bufferUsage | number | 否 | 缓冲器是如何使用的. gl.DYNAMIC_DRAW, gl.STATIC_DRAW 或 gl.STREAM_DRAW 的 |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) - 包装顶点缓冲器


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1811](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1811)  
引入版本：3.0.0


---

### createVideoTexture {#createVideoTexture}

#### \<instance> createVideoTexture(srcVideo, [noRepeat], [flipY]) {#instance-createvideotexturesrcvideo-norepeat-flipy}


**说明:**

创建基于 HTML 视频元素的新 WebGL 纹理 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| srcVideo | HTMLVideoElement | 否 |  | 创建 WebGL 纹理的视频 |
| noRepeat | boolean | 是 | false | 是否允许此画布设置 `REPEAT` ? |
| flipY | boolean | 是 | true | 是否应该用WebGL纹理设定`UNPACK_FLIP_Y_WEBGL`? |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) - 新建的WebGLTextureWrapper. 中国植物物种信息数据库.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2432](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2432)  
引入版本：3.20.0


---

### deleteBuffer {#deleteBuffer}

#### \<instance> deleteBuffer(buffer) {#instance-deletebufferbuffer}


**说明:**

从 GL 实例中删除 WebGL 缓冲器。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| buffer | [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) | 否 | 要删除的 WebGL 缓存 。 |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个 WebGLRender 实例 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1931](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1931)  
引入版本：3.0.0


---

### deleteFramebuffer {#deleteFramebuffer}

#### \<instance> deleteFramebuffer(framebuffer) {#instance-deleteframebufferframebuffer}


**说明:**

从 GL 实例中删除一个框架缓冲器。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| framebuffer | [Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](/api/class/renderer-webgl-wrappers-webglframebufferwrapper) \| null | 否 | 框架缓冲器将被删除 。 |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个 WebGLRender 实例 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1889](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1889)  
引入版本：3.0.0


---

### deleteProgram {#deleteProgram}

#### \<instance> deleteProgram(program) {#instance-deleteprogramprogram}


**说明:**

从 GL 实例中删除 WebGL 程序。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| program | [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](/api/class/renderer-webgl-wrappers-webglprogramwrapper) | 否 | 要删除的遮阳程序 。 |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个 WebGLRender 实例 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1910](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1910)  
引入版本：3.0.0


---

### deleteTexture {#deleteTexture}

#### \<instance> deleteTexture(texture) {#instance-deletetexturetexture}


**说明:**

从 GPU 中删除纹理。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 否 | 将删除的 WebGL 纹理 。 |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个 WebGLRender 实例 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1868](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1868)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此 WebGLRenderer, 清理所有相关的资源, 如包装器, 本地纹理等 。


**重写:** Phaser.Events.EventEmitter#销毁


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2617](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2617)  
引入版本：3.0.0


---

### dispatchContextLost {#dispatchContextLost}

#### \<instance> dispatchContextLost(event) {#instance-dispatchcontextlostevent}


**说明:**

当 WebGL 上下文丢失时, 这种方法会被称为。 默认情况下, 这种方法会绑定在属性 `WebGLRenderer.contextLostHandler` 上。 如果您通过 `setContextHandlers` 方法覆盖了上下文处理器, 请确保适时引用此方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | WebGLContextEvent | 否 | WebGL 上下文丢失事件 。 |


> 源码：[src/renderer/webgl/WebGLRenderer.js#L986](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L986)  
引入版本：3.85.0


---

### dispatchContextRestored {#dispatchContextRestored}

#### \<instance> dispatchContextRestored(event) {#instance-dispatchcontextrestoredevent}


**说明:**

当恢复 WebGL 上下文时, 这种方法叫做。 默认情况下, 这种方法会绑定在属性 `WebGLRenderer.contextRestoredHandler` 上。 如果您通过 `setContextHandlers` 方法覆盖了恢复的上下文处理器, 请确保在适当时候引用这种方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | WebGLContextEvent | 否 | WebGL 上下文恢复事件 。 |


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1009](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1009)  
引入版本：3.85.0


---

### drawElements {#drawElements}

#### \<instance> drawElements(drawingContext, textures, program, vao, count, offset, topology) {#instance-drawelementsdrawingcontext-textures-program-vao-count-offset-topology}


**说明:**

绘制一些图的顶点到绘图上下文。

使用索引缓冲绘制顶点。 缓冲应绑定在 VAO 上。 默认情况下, Vertices 被绘制为 `TRIANGLE_STRIP` 。

这是主要渲染方法,它需要所有制作顶点所必需的WebGL资源,所以它们不必在别处设置临时的.

它不会上传顶点数据到缓冲器。 确保在调用此方法之前完成此任务 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 画的图文图文 |
| textures | Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper)> | 否 | 要绑定的纹理阵列。纹理会绑定在与数组中的指数相对应的单位。 |
| program | [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](/api/class/renderer-webgl-wrappers-webglprogramwrapper) | 否 | 用于遮蔽的程序。 |
| vao | [Phaser.Renderer.WebGL.Wrappers.WebGLVAOWrapper](/api/class/renderer-webgl-wrappers-webglvaowrapper) | 否 | 绑定 Vertex 矩阵对象。 它必须附带索引缓冲器 。 |
| count | number | 否 | 要绘制的顶点数。 由于 TRIANGLE_STRIP 地形, 这应该是 `n + 2`, 其中 `n` 是要绘制的三角形数, 包括退化的三角形 。 |
| offset | number | 否 | 开始从索引缓冲中提取的偏移。 此处为字节, 应为 2 的倍数( 对于 16 位 `UNSIGNED_SHORT` 索引 ) 。 |
| topology | number | 否 | 原始人的类型,默认为`TRIANGLE_STRIP`. |


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2042](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2042)  
引入版本：4.0.0


---

### drawInstancedArrays {#drawInstancedArrays}

#### \<instance> drawInstancedArrays(drawingContext, textures, program, vao, first, count, instanceCount) {#instance-drawinstancedarraysdrawingcontext-textures-program-vao-first-count-instancecount}


**说明:**

绘制一些实例到绘图上下文。

此选项使用 ANGLE_instanced_arrays 扩展绘制顶点。 这通常使用实例缓冲和顶点缓冲。 两者都应该绑定在 VAO 上。 默认情况下, Vertices 被绘制为 `TRIANGLE_STRIP` 。

它不会上传顶点数据到缓冲器。 确保在调用此方法之前完成此任务 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 画的图文图文 |
| textures | Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper)> | 否 | 要绑定的纹理阵列。纹理会绑定在与数组中的指数相对应的单位。 |
| program | [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](/api/class/renderer-webgl-wrappers-webglprogramwrapper) | 否 | 用于遮蔽的程序。 |
| vao | [Phaser.Renderer.WebGL.Wrappers.WebGLVAOWrapper](/api/class/renderer-webgl-wrappers-webglvaowrapper) | 否 | 绑定的 Vertex 矩阵对象。 它不需要附加索引缓冲 。 |
| first | number | 否 | 矢量点数组中的起始索引。 |
| count | number | 否 | 画顶数. |
| instanceCount | number | 否 | 需要提供的实例数目。 |


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2080](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2080)  
引入版本：4.0.0


---

### getAspectRatio {#getAspectRatio}

#### \<instance> getAspectRatio() {#instance-getaspectratio}


**说明:**

获得WebGLRenderer维度的宽度比。


**返回值:** number - WebGLRenderer 维度的宽比 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1438](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1438)  
引入版本：3.50.0


---

### getCompressedTextureName {#getCompressedTextureName}

#### \<instance> getCompressedTextureName(baseFormat, [format]) {#instance-getcompressedtexturenamebaseformat-format}


**说明:**

返回基于给定格式的压缩纹理格式 GLenum 名称。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| baseFormat | string | 否 | 要检查的基底格式 。 |
| format | GLenum | 是 | 用于检查底部格式的可选 GLenum 格式。 |


**返回值:** string - 压缩的纹理格式名称,作为字符串.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1387](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1387)  
引入版本：3.60.0


---

### getCompressedTextures {#getCompressedTextures}

#### \<instance> getCompressedTextures() {#instance-getcompressedtextures}


**说明:**

确定浏览器和设备支持的压缩纹理格式。

作为 WebGL 渲染器进程的一部分自动调用。 如果您需要调查它支持哪种格式, 请查看 `Phaser.Renderer.WebGL.WebGLRenderer#compression` 属性 。


**返回值:** [Phaser.Types.Renderer.WebGL.WebGLTextureCompression](/api/typedef/types-renderer-webgl#webgltexturecompression) - 压缩对象 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1337](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1337)  
引入版本：3.60.0


---

### getExtension {#getExtension}

#### \<instance> getExtension(extensionName) {#instance-getextensionextensionname}


**说明:**

装入 WebGL 扩展

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| extensionName | string | 否 | 扩展名以加载 。 |


**返回值:** object - 如果支持扩展, 则 WebGL 扩展


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1534](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1534)  
引入版本：3.0.0


---

### getFps {#getFps}

#### \<instance> getFps() {#instance-getfps}


**说明:**

这种方法仅在Phaser的除臭建筑中,或Webpack配置中设置的`WEBGL_DEBUG`旗的建筑中可以使用.

Phaser v3.60 调试器内嵌了Spector.js的构件,是WebGL的检查员,可以现场检查您的WebGL呼叫。虽然将Spector扩展器添加到桌面浏览器中很容易,但通过嵌入Phaser,我们也可以在移动浏览器中提供,使其成为在不允许扩展的移动设备上调试ZWebGL游戏的强大工具.

详情请见[https://github.com/BabylonJS/Spector.js](https://github.com/BabylonJS/Spector.js)。

此方法将返回 WebGL 帆布的当前 FPS 。


**返回值:** number - 现时WebGL帆布的FPS.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1135)  
引入版本：3.60.0


---

### getMaxTextureSize {#getMaxTextureSize}

#### \<instance> getMaxTextureSize() {#instance-getmaxtexturesize}


**说明:**

返回可以创建的最大纹理大小( 宽度或高度) 。 请注意, VRAM 可能不允许任何给定大小的纹理, 它只是表达给定大小的硬件/ 驱动程序支持 。


**返回值:** number - 最大支持的纹理大小 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2602](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2602)  
引入版本：3.8.0


---

### hasExtension {#hasExtension}

#### \<instance> hasExtension(extensionName) {#instance-hasextensionextensionname}


**说明:**

检查是否支持 WebGL 扩展

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| extensionName | string | 否 | WebGL扩展名 |


**返回值:** boolean - 如果支持扩展,则使用`true`,否则使用`false`.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1519](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1519)  
引入版本：3.0.0


---

### init {#init}

#### \<instance> init(config) {#instance-initconfig}


**说明:**

创建新的 WebGLRendering Context 并初始化所有内部状态。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | object | 否 | 渲染器的配置对象 。 |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个 WebGLRender 实例 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L675](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L675)  
引入版本：3.0.0


---

### log {#log}

#### \<instance> log(arguments) {#instance-logarguments}


**说明:**

这种方法仅在Phaser的除臭建筑中,或Webpack配置中设置的`WEBGL_DEBUG`旗的建筑中可以使用.

Phaser v3.60 调试器内嵌了Spector.js的构件,是WebGL的检查员,可以现场检查您的WebGL呼叫。虽然将Spector扩展器添加到桌面浏览器中很容易,但通过嵌入Phaser,我们也可以在移动浏览器中提供,使其成为在不允许扩展的移动设备上调试ZWebGL游戏的强大工具.

详情请见[https://github.com/BabylonJS/Spector.js](https://github.com/BabylonJS/Spector.js)。

这种方法添加了列表中的名称值的命令。 可以在搜索中过滤。 所有日志都可以过滤搜索“ LOG ” 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| arguments | * | 否 | 将参数日志到 Spector 。 |


**返回值:** string - 现本日志.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1162)  
引入版本：3.60.0


---

### onResize {#onResize}

#### \<instance> onResize(gameSize, baseSize) {#instance-onresizegamesize-basesize}


**说明:**

管理由缩放管理器发出的 `resize` 事件的事件处理器 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameSize | [Phaser.Structs.Size](/api/class/structs-size) | 否 | 默认的游戏大小对象。 这是未修改的游戏尺寸 。 |
| baseSize | [Phaser.Structs.Size](/api/class/structs-size) | 否 | 基数对象。 游戏尺寸。 画布宽度/ 高度值与此相符 。 |


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1284](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1284)  
引入版本：3.16.0


---

### postRender {#postRender}

#### \<instance> postRender() {#instance-postrender}


**说明:**

后退台阶发生在所有镜头都完成后


**触发事件:** [Phaser.Renderer.Events#event:POST_RENDER](/api/event/renderer-events#post_render)


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2017](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2017)  
引入版本：3.0.0


---

### preRender {#preRender}

#### \<instance> preRender() {#instance-prerender}


**说明:**

清除底部绘图康特文本并读取它以供使用。


**触发事件:** [Phaser.Renderer.Events#event:PRE_RENDER_CLEAR](/api/event/renderer-events#pre_render_clear), [Phaser.Renderer.Events#event:PRE_RENDER](/api/event/renderer-events#pre_render)


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1949](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1949)  
引入版本：3.0.0


---

### removeBlendMode {#removeBlendMode}

#### \<instance> removeBlendMode(index) {#instance-removeblendmodeindex}


**说明:**

从渲染器中删除自定义的混合模式。 任何仍在使用此混合模式的游戏对象都会出错, 所以请先清除它们 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 要删除的自定义混合模式索引 。 |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个 WebGLRender 实例 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1615](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1615)  
引入版本：3.0.0


---

### render {#render}

#### \<instance> render(scene, children, camera) {#instance-renderscene-children-camera}


**说明:**

核心为场景镜头做制动步骤.

透过给定的游戏对象阵列,用给定的摄像机来进行图化.

这是用 `CameraManager.render` 方法调用。 摄像机管理器实例属于 Scene, 并且被 Scene Systems. render 方法引用 。

如果`Camera.visible`是`false`,或者`Camera.alpha`是零,则不叫这个方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 场景要演化。 |
| children | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 一系列可以由给定的摄像机渲染的过滤游戏对象. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 场景摄像机要用它来制作 |


**触发事件:** [Phaser.Renderer.Events#event:RENDER](/api/event/renderer-events#render)


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1986](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1986)  
引入版本：3.0.0


---

### resetProjectionMatrix {#resetProjectionMatrix}

#### \<instance> resetProjectionMatrix() {#instance-resetprojectionmatrix}


**说明:**

将投影矩阵重置到这个渲染器宽度和高度 。

如果由于捕获过程而改变矩阵,则在`endCapture`期间使用此名称.


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个 WebGLRender 实例 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1503](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1503)  
引入版本：3.50.0


---

### resize {#resize}

#### \<instance> resize([width], [height]) {#instance-resizewidth-height}


**说明:**

调整绘图缓冲器大小,以与“缩放管理器”要求的匹配。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 是 | 变形器的新宽度 。 |
| height | number | 是 | 造物器的新高度. |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个 WebGLRender 实例 。


**触发事件:** [Phaser.Renderer.Events#event:RESIZE](/api/event/renderer-events#resize)


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1302](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1302)  
引入版本：3.0.0


---

### setContextHandlers {#setContextHandlers}

#### \<instance> setContextHandlers([contextLost], [contextRestored]) {#instance-setcontexthandlerscontextlost-contextrestored}


**说明:**

设置在 WebGL 上下文被浏览器丢失或恢复时调用到的处理器 。

默认处理器通过属性引用 `WebGLRenderer.contextLostHandler` 财务报告和已审计财务报表 `WebGLRenderer.contextRestoredHandler`。默认情况下,这些映射到方法 `WebGLRenderer.dispatchContextLost` 财务报告和已审计财务报表 `WebGLRenderer.dispatchContextRestored`.

你可以用这种方法 来控制这些操作员

如果你真的超过它们,请确保操作员适时引用`WebGLRenderer.dispatchContextLost`和`WebGLRenderer.dispatchContextRestored`的方法,否则渲染器将无法完全恢复自己.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| contextLost | function | 是 | 自定义的响应 WebGL 上下文丢失的事件的处理器。 设置为 `undefined` , 以使用默认处理器 。 |
| contextRestored | function | 是 | 自定义的响应 WebGL 上下文的处理器恢复事件。 设置为 `undefined` , 以使用默认处理器 。 |


> 源码：[src/renderer/webgl/WebGLRenderer.js#L934](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L934)  
引入版本：3.85.0


---

### setExtensions {#setExtensions}

#### \<instance> setExtensions() {#instance-setextensions}


**说明:**

查询 GL 上下文以获取支持的扩展名 。

然后把它们放入`supportedExtensions`,`instancedArraysExtension`和`vaoExtension`的属性中.

在`init`方法中自动调用.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L849](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L849)  
引入版本：3.85.2


---

### setProjectionMatrix {#setProjectionMatrix}

#### \<instance> setProjectionMatrix(width, height, [flipY]) {#instance-setprojectionmatrixwidth-height-flipy}


**说明:**

设置此渲染器的投影矩阵到给定的维度。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 否 |  | 投影矩阵的新宽度. |
| height | number | 否 |  | 投影矩阵的新高度. |
| flipY | boolean | 是 | false | Y轴应该翻转吗? |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个 WebGLRender 实例 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1451](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1451)  
引入版本：3.50.0


---

### setProjectionMatrixFromDrawingContext {#setProjectionMatrixFromDrawingContext}

#### \<instance> setProjectionMatrixFromDrawingContext(drawingContext) {#instance-setprojectionmatrixfromdrawingcontextdrawingcontext}


**说明:**

设置此渲染器的投影矩阵,以匹配给定的绘图上下文。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 用于设定投影矩阵的绘图上下文 。 |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个 WebGLRender 实例 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1484](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1484)  
引入版本：4.0.0


---

### setTextureFilter {#setTextureFilter}

#### \<instance> setTextureFilter(texture, filter) {#instance-settexturefiltertexture-filter}


**说明:**

设置纹理的微量化和放大过滤器。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 否 | 设置过滤器的纹理 。 |
| filter | number | 否 | 设置的过滤器。 0 用于线性过滤, 1 用于最近的邻居( blocky) 过滤 。 |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个WebGL 朗德尔的例子。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2509](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2509)  
引入版本：3.0.0


---

### setTextureWrap {#setTextureWrap}

#### \<instance> setTextureWrap(glTextureWrapper, wrapModeS, wrapModeT) {#instance-settexturewrapgltexturewrapper-wrapmodes-wrapmodet}


**说明:**

设置纹理的包扎模式。

包装模式可以是以下一种: 包装模式:

- Phaser.Textures.WrapMode.CLAMP_TO_EDGE

- Phaser.Textures.WrapMode.REPEAT

- Phaser.Textures.WrapMode.MIRRORED_REPEAT

注意, 仅支持 CLAMP_ TO_ EDGE 的非纹理功率。 如果为这样的纹理指定了另一个包模式, 则会忽略它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| glTextureWrapper | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 否 | WebGL纹理包装器设置包装模式. |
| wrapModeS | [Phaser.Textures.WrapMode](/api/namespace/textures-wrapmode) | 否 | S( 横向) 轴的包覆模式 。 |
| wrapModeT | [Phaser.Textures.WrapMode](/api/namespace/textures-wrapmode) | 否 | T(垂直)轴的包模式。 |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个WebGL 朗德尔的例子。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2547](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2547)  
引入版本：4.0.0


---

### snapshot {#snapshot}

#### \<instance> snapshot(callback, [type], [encoderOptions]) {#instance-snapshotcallback-type-encoderoptions}


**说明:**

在当前框架解析后, 将整个游戏视口的快照排成一个 。

要捕捉特定区域,请参见`snapshotArea`方法。要捕捉特定像素,请参见`snapshotPixel`。

只有一张快照可以激活_per fram_。例如,如果您已经调用 `snapshotPixel`,那么调用这种方法将覆盖它。

快照工作时使用 WebGL `readPixels` 特性将框架缓冲器中的每个像素抓入一个 ArrayBufferView。它然后解析这个,将内容复制到临时的 Canvas 中,最后从中创建一个图像对象,即图像返回到提供的调回。 总之,这是一个计算成本和阻断过程,它得到的比画布大小更大的价格,所以请小心如何在游戏中使用它。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 |  | 创建了快照图像后要引用的函数 。 |
| 类型 | string | 是 | "'image/png'" | 图像创建的格式,通常为`image/png`或`image/jpeg`. |
| encoderOptions | number | 是 | 0.92 | 图像质量,介于0到1. 用于图像格式,具有失速压缩,例如`image/jpeg`. |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个WebGL 朗德尔。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2115](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2115)  
引入版本：3.0.0


---

### snapshotArea {#snapshotArea}

#### \<instance> snapshotArea(x, y, width, height, callback, [type], [encoderOptions]) {#instance-snapshotareax-y-width-height-callback-type-encoderoptions}


**说明:**

在当前框架渲染后,将游戏视口的指定区域进行图示。

要捕捉整个游戏的视港,请查看`snapshot`方法. 要捕捉到特定的像素,请参看`snapshotPixel`.

只有一张快照可以激活_per fram_。例如,如果您已经调用 `snapshotPixel`,那么调用这种方法将覆盖它。

快照工作时使用 WebGL `readPixels` 特性将框架缓冲器中的每个像素抓入一个 ArrayBufferView。它然后解析这个,将内容复制到临时的 Canvas 中,最后从中创建一个图像对象,即图像返回到提供的调回。 总之,这是一个计算成本和阻断过程,它得到的比画布大小更大的价格,所以请小心如何在游戏中使用它。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 用于抓取的x坐标。 是基于游戏的视图, 而不是世界 。 |
| y | number | 否 |  | 游戏的坐标是用来抓的,这是基于游戏的视点,而不是世界。 |
| width | number | 否 |  | 要抓取的区域的宽度 。 |
| height | number | 否 |  | 高地的地盘要抓 |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 |  | 创建了快照图像后要引用的函数 。 |
| 类型 | string | 是 | "'image/png'" | 图像创建的格式,通常为`image/png`或`image/jpeg`. |
| encoderOptions | number | 是 | 0.92 | 图像质量,介于0到1. 用于图像格式,具有失速压缩,例如`image/jpeg`. |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个WebGL 朗德尔。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2142)  
引入版本：3.16.0


---

### snapshotFramebuffer {#snapshotFramebuffer}

#### \<instance> snapshotFramebuffer(framebuffer, bufferWidth, bufferHeight, callback, [getPixel], [x], [y], [width], [height], [type], [encoderOptions]) {#instance-snapshotframebufferframebuffer-bufferwidth-bufferheight-callback-getpixel-x-y-width-height-type-encoderoptions}


**说明:**

抓取给定框架缓冲器的指定区域。

与其他快照方法不同,这个方法被立即处理,不等待下一次渲染.

快照工作时使用 WebGL `readPixels` 特性将框架缓冲器中的每个像素抓入一个 ArrayBufferView。它然后解析这个,将内容复制到临时的 Canvas 中,最后从中创建一个图像对象,即图像返回到提供的调回。 总之,这是一个计算成本和阻断过程,它得到的比画布大小更大的价格,所以请小心如何在游戏中使用它。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| framebuffer | [Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](/api/class/renderer-webgl-wrappers-webglframebufferwrapper) | 否 |  | 挡板刹车从。 |
| bufferWidth | number | 否 |  | 帧缓冲器的宽度 。 |
| bufferHeight | number | 否 |  | 帧缓冲器的高度. |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 |  | 创建了快照图像后要引用的函数 。 |
| getPixel | boolean | 是 | false | 抓取一个像素作为颜色对象, 还是区域作为图像对象? |
| x | number | 是 | 0 | 坐标是用来抓的,这是基于帧缓冲器,而不是世界 |
| y | number | 是 | 0 | 以调制器而不是世界为主 |
| width | number | 是 | "bufferWidth" | 要抓取的区域的宽度 。 |
| height | number | 是 | "bufferHeight" | 高地的地盘要抓 |
| 类型 | string | 是 | "'image/png'" | 图像创建的格式,通常为`image/png`或`image/jpeg`. |
| encoderOptions | number | 是 | 0.92 | 图像质量,介于0到1. 用于图像格式,具有失速压缩,例如`image/jpeg`. |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个WebGL 朗德尔。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2215](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2215)  
引入版本：3.19.0


---

### snapshotPixel {#snapshotPixel}

#### \<instance> snapshotPixel(x, y, callback) {#instance-snapshotpixelx-y-callback}


**说明:**

在当前框架渲染后,将游戏视口中给定的像素的快照排出日程。

要捕捉整个游戏的视港,请查看`snapshot`方法。要捕捉特定区域,请参看`snapshotArea`。

只有一张快照可以激活_per fram_。例如,如果您已经调用 `snapshotArea`,那么调用这种方法将覆盖它。

与另外两种快照方法不同,这个会返回包含所请求像素的颜色数据的`Color`对象,它不需要创建内部的Canvas或Image对象,因此执行速度要快很多,使用内存较少.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 要获取的像素的x坐标, 以游戏的视图为主, 而不是世界 。 |
| y | number | 否 | 要获取的像素的y坐标。 其基于游戏视图, 而非世界 。 |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 | 提取快照像素数据后要引用的函数 。 |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个WebGL 朗德尔。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2185](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2185)  
引入版本：3.16.0


---

### startCapture {#startCapture}

#### \<instance> startCapture([commandCount], [quickCapture], [fullCapture]) {#instance-startcapturecommandcount-quickcapture-fullcapture}


**说明:**

这种方法仅在Phaser的除臭建筑中,或Webpack配置中设置的`WEBGL_DEBUG`旗的建筑中可以使用.

Phaser v3.60 调试器内嵌了Spector.js的构件,是WebGL的检查员,可以现场检查您的WebGL呼叫。虽然将Spector扩展器添加到桌面浏览器中很容易,但通过嵌入Phaser,我们也可以在移动浏览器中提供,使其成为在不允许扩展的移动设备上调试ZWebGL游戏的强大工具.

详情请见[https://github.com/BabylonJS/Spector.js](https://github.com/BabylonJS/Spector.js)。

此方法将在 Phaser 帆布上启动抓取。 一旦它达到指定为参数的命令数, 或10秒后, 抓取就会停止。 如果快速抓取属实, 缩略图不会被抓取, 以便加快抓取速度 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| commandCount | number | 是 | 0 | 捕获的命令数。 如果为零, 将捕获10秒 。 |
| quickCapture | boolean | 是 | false | 如果`true`缩略图没有被捕获,以加速捕获. |
| fullCapture | boolean | 是 | false | 如果`true`所有的细节都被捕获. |


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1194)  
引入版本：3.60.0


---

### stopCapture {#stopCapture}

#### \<instance> stopCapture() {#instance-stopcapture}


**说明:**

这种方法仅在Phaser的除臭建筑中,或Webpack配置中设置的`WEBGL_DEBUG`旗的建筑中可以使用.

Phaser v3.60 调试器内嵌了Spector.js的构件,是WebGL的检查员,可以现场检查您的WebGL呼叫。虽然将Spector扩展器添加到桌面浏览器中很容易,但通过嵌入Phaser,我们也可以在移动浏览器中提供,使其成为在不允许扩展的移动设备上调试ZWebGL游戏的强大工具.

详情请见[https://github.com/BabylonJS/Spector.js](https://github.com/BabylonJS/Spector.js)。

此方法将停止当前抓取并返回 JSON 中的结果。 如果显示 UI , 它会显示结果。 如果抓取尚未完成或找不到任何命令, 则返回未定义 。


**返回值:** object - 现摄摄.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1231](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1231)  
引入版本：3.60.0


---

### supportsCompressedTexture {#supportsCompressedTexture}

#### \<instance> supportsCompressedTexture(baseFormat, [format]) {#instance-supportscompressedtexturebaseformat-format}


**说明:**

检查是否支持给定的压缩纹理格式, 或不支持 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| baseFormat | string | 否 | 要检查的基底格式 。 |
| format | GLenum | 是 | 用于检查底部格式的可选 GLenum 格式。 |


**返回值:** boolean - 如果格式被支持, 则真实性为假 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1408](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1408)  
引入版本：3.60.0


---

### updateBlendMode {#updateBlendMode}

#### \<instance> updateBlendMode(index, func, equation) {#instance-updateblendmodeindex-func-equation}


**说明:**

更新绑定在给定自定义混合模式下的函数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 自定义混合模式的索引 。 |
| func | Array.\<GLenum> | 否 | 混合模式使用的函数。指定两个元素用于src和dest,或四个元素用于分离 srcRGB, destRGB, srcAlpha, destAlpha. |
| equation | GLenum \| Array.\<GLenum> | 否 | 混合模式所用的方程式。 这可以是源和目的的单一方程式,也可以是包含源和目的的单独方程式的数组。 |


**返回值:** [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) - 这个 WebGLRender 实例 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L1576](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L1576)  
引入版本：3.0.0


---

### updateCanvasTexture {#updateCanvasTexture}

#### \<instance> updateCanvasTexture(srcCanvas, dstTexture, [flipY], [noRepeat]) {#instance-updatecanvastexturesrccanvas-dsttexture-flipy-norepeat}


**说明:**

更新基于给定的 Canvas 元素的 WebGL 纹理 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| srcCanvas | HTMLCanvasElement | 否 |  | 彩虹号用来更新WebGL纹理 |
| dstTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 否 |  | 目的地WebGLTextureWrapper 更新. |
| flipY | boolean | 是 | true | 是否应该用WebGL纹理设定`UNPACK_FLIP_Y_WEBGL`? |
| noRepeat | boolean | 是 | false | 是否允许此画布设置 `REPEAT`( 如文本对象) ? |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) - 更新的 WebGLTexture Wrapper。 此对象与 `dstTexture` 相同 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2357](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2357)  
引入版本：3.20.0


---

### updateVideoTexture {#updateVideoTexture}

#### \<instance> updateVideoTexture(srcVideo, dstTexture, [flipY], [noRepeat]) {#instance-updatevideotexturesrcvideo-dsttexture-flipy-norepeat}


**说明:**

基于给定的 HTML 视频元素更新 WebGL 纹理 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| srcVideo | HTMLVideoElement | 否 |  | 更新WebGL纹理的视频. |
| dstTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 否 |  | 目的地WebGLTextureWrapper 更新. |
| flipY | boolean | 是 | true | 是否应该用WebGL纹理设定`UNPACK_FLIP_Y_WEBGL`? |
| noRepeat | boolean | 是 | false | 是否允许此画布设置 `REPEAT` ? |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) - 更新的 WebGLTexture Wrapper。 此对象与 `dstTexture` 相同 。


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2452](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2452)  
引入版本：3.20.0


---

### videoToTexture {#videoToTexture}

#### \<instance> videoToTexture(srcVideo, [dstTexture], [noRepeat], [flipY]) {#instance-videototexturesrcvideo-dsttexture-norepeat-flipy}


**说明:**

创建或更新基于给定的 HTML 视频元素的 WebGL 纹理 。

如果给出了`dstTexture`参数,则更新了WebGL纹理,而不是创建了新鲜的.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| srcVideo | HTMLVideoElement | 否 |  | 创建 WebGL 纹理的视频 |
| dstTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 是 |  | 要设置的目的地 WebGLTextureWrapper 。 |
| noRepeat | boolean | 是 | false | 是否允许此画布设置 `REPEAT` ? |
| flipY | boolean | 是 | true | 是否应该用WebGL纹理设定`UNPACK_FLIP_Y_WEBGL`? |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) - 新建或更新的WebGLTextureWrapper.


> 源码：[src/renderer/webgl/WebGLRenderer.js#L2378](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/WebGLRenderer.js#L2378)  
引入版本：4.0.0


---

---
