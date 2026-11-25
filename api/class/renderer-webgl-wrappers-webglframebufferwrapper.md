# WebGLFramebufferWrapper {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-wrappers-webglframebufferwrapper)

用于WebGL帧缓冲器的包装器,包含用于创建它的所有信息.

一个WebGLFramebuffer不应该在WebGLRenderer之外被曝光,因此WebGLLRenderer可以处理上下文丢失和其他事件而无需其他系统意识到它. 总是使用WebGLPLFramebaferWrapper代替.

这也管理了帧缓冲器的附属物,包括缓冲器的生命周期.

**构造函数**

`new WebGLFramebufferWrapper(renderer, colorAttachments, [addStencilBuffer], [addDepthBuffer])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 |  | 这个WebGLFramebuffer属于的渲染器. |
| colorAttachments | Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper)> | 否 |  | 写着颜色像素的颜色纹理。 如果是空的, 画布将被用作颜色附件。 默认情况下只使用第一个颜色附件 WebGL1 。 |
| addStencilBuffer | boolean | 是 | false | 是否在帧缓冲器中添加一个天线缓冲。 如果将画布作为颜色附件, 则此选项将被忽略 。 |
| addDepthBuffer | boolean | 是 | false | 是否在帧缓冲器中添加深度缓冲。 如果同时提供了深度和速率, 它们将被合并为单个深度速率缓冲器。 如果将画布用作颜色附件, 则忽略此选项 。 |

---


**作用域**: static

> 源码：[src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L27](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L27)  
引入版本：3.80.0

## 公开成员 {#public-members}

### attachments {#attachments}

#### attachments: Array.\<Attachment> {#attachments-arrayattachment}


**说明:**

帧缓冲器的附件。 这些数据包括宽度、 高度、 渲染缓冲器或纹理 。


> 源码：[src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L116)  
引入版本：4.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

帧缓冲器的高度, 以像素为单位。 由第一个颜色附件产生, 用于分配缓冲器存储 。


> 源码：[src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L106)  
引入版本：3.80.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrendererwebglwebglrenderer}


**说明:**

这个WebGLLLFramebuffer属于的WebGLLLRenderer.


> 源码：[src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L75)  
引入版本：4.0.0


---

### renderTexture {#renderTexture}

#### renderTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#rendertexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

写着颜色像素的颜色纹理.

如果画布被用作颜色附件, 则此图将是 `null`。 它是帧缓冲器上的第一个颜色附件 。


> 源码：[src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L173)  
引入版本：3.80.0


---

### useCanvas {#useCanvas}

#### useCanvas: boolean {#usecanvas-boolean}


**说明:**

是否使用画布作为颜色附件。 如果这是真的, 将不会创建帧缓冲器。 这对浏览器创建的主要帧缓冲器有用 。


> 源码：[src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L84)  
引入版本：4.0.0


---

### webGLFramebuffer {#webGLFramebuffer}

#### webGLFramebuffer: WebGLFramebuffer {#webglframebuffer-webglframebuffer}


**说明:**

韦伯格拉姆缓冲器被这个班包住了.

此属性随时会改变。 因此, 您不应该存储此值的引用。 它只应直接传递到 WebGL API 中进行绘图 。

如果框架缓冲器将画布作为颜色附件,则此属性将是 `null` 。


> 源码：[src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L58)  
引入版本：3.80.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

帧缓冲器的宽度, 以像素为单位。 其来源于第一个颜色附件, 用于分配缓冲器存储 。


> 源码：[src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L96)  
引入版本：3.80.0


---

## 公开方法 {#public-methods}

### createResource {#createResource}

#### \<instance> createResource() {#instance-createresource}


**说明:**

从给定参数创建 WebGLFramebuffer 。

由构建器自动调用。 如果 WebGLFramebuffer 需要重新创建, 也可以再次调用 。


> 源码：[src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L194)  
引入版本：3.80.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这个WebGLFramebusferWrapper。


> 源码：[src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L301](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L301)  
引入版本：3.80.0


---

### resize {#resize}

#### \<instance> resize(width, height) {#instance-resizewidth-height}


**说明:**

更改此 WebGLFramebofferWrapper 的附件大小 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 帧缓冲器的新宽度 。 |
| height | number | 否 | 帧缓冲器的新高度. |


> 源码：[src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L278](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLFramebufferWrapper.js#L278)  
引入版本：4.0.0


---

---
