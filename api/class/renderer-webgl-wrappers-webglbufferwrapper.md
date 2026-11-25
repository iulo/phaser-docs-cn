# WebGLBufferWrapper {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-wrappers-webglbufferwrapper)

用于 WebGL 缓冲器的包装器, 包含用于创建它的所有信息。 这可以是 Vertex 缓冲器 或 Index 缓冲器( Index 缓缓冲器 ) 。

一个WebGLBAffer不应该在WebGLRenderer之外曝光,因此WebGLLAFAffer可以处理上下文损失和其他事件而无需其他系统意识到这一点. 总是使用WebGLPAfferWrapper代替.

**构造函数**

`new WebGLBufferWrapper(renderer, dataBuffer, bufferType, bufferUsage)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有这个包装的 WebGLRender 实例 。 |
| dataBuffer | ArrayBuffer | 否 | 要存储的数据矩阵缓冲器。 缓冲器将永久与此数据连接 。 |
| bufferType | GLenum | 否 | 正在创建的缓冲器类型 。 |
| bufferUsage | GLenum | 否 | 正在创建的缓冲器的使用 。 gl.DYNAMIC_DRAW, gl.STATIC_DRAW 或 gl.STREAM_DRAW 。 |

---


**作用域**: static

> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L9)  
引入版本：3.80.0

## 公开成员 {#public-members}

### bufferType {#bufferType}

#### bufferType: GLenum {#buffertype-glenum}


**说明:**

缓冲器的类型.


> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L116)  
引入版本：3.80.0


---

### bufferUsage {#bufferUsage}

#### bufferUsage: GLenum {#bufferusage-glenum}


**说明:**

缓冲器的用法. gl.DYNAMIC_DRAW, gl.STATIC_DRAW 或 gl.STREAM_DRAW.


> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L125)  
引入版本：3.80.0


---

### dataBuffer {#dataBuffer}

#### dataBuffer: ArrayBuffer {#databuffer-arraybuffer}


**说明:**

与缓冲相关的数据.

注意, 如果 WebGL 上下文丢失, 将使用此程序来重现缓冲 。


> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L57)  
引入版本：4.0.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrendererwebglwebglrenderer}


**说明:**

拥有这个包装的 WebGLRender 实例 。


> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L34](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L34)  
引入版本：4.0.0


---

### viewF32 {#viewF32}

#### viewF32: Float32Array, null {#viewf32-float32array-null}


**说明:**

一张dataBuffer的浮图32箭头图

如果 dataBuffer 的字节长度不被 Float32Array 所分割,则此缓冲器将是 `null`。 这种缓冲器仅适合使用 16 位索引 。


> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L68)  
引入版本：4.0.0


---

### viewU16 {#viewU16}

#### viewU16: Uint16Array, null {#viewu16-uint16array-null}


**说明:**

一张Uint16箭头的dataBuffer的视图.

这将是 `null` 如果该字节的字节长度 dataBuffer 不被 Uint16Array 所分割。BYTES_PER_Element (2)。这样的缓冲器仅适合用字节数据。


> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L90)  
引入版本：4.0.0


---

### viewU32 {#viewU32}

#### viewU32: Uint32Array, null {#viewu32-uint32array-null}


**说明:**

一张Uint32箭头的dataBuffer的视图.

这将是 `null` 如果该字节的字节长度 dataBuffer 无法被 Uint32Array 分割。 BYTES_PER_Element (4) 。 这种缓冲器仅适合使用16位索引 。


> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L103)  
引入版本：4.0.0


---

### viewU8 {#viewU8}

#### viewU8: Uint8Array {#viewu8-uint8array}


**说明:**

一张Uint8箭头的dataBuffer的视图.


> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L81)  
引入版本：4.0.0


---

### webGLBuffer {#webGLBuffer}

#### webGLBuffer: WebGLBuffer {#webglbuffer-webglbuffer}


**说明:**

由这个类包起来的 WebGLBAFER 。

此属性随时会改变。 因此, 您不应该存储此值的引用。 它只应直接传递到 WebGL API 中进行绘图 。


> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L43)  
引入版本：3.80.0


---

## 公开方法 {#public-methods}

### bind {#bind}

#### \<instance> bind([unbind]) {#instance-bindunbind}


**说明:**

将此 WebGL 缓冲器绑定到当前 WebGLRendering Context 。 它使用此包件的 bufferType 来确定使用哪个绑定点 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| unbind | boolean | 是 | false | 是否将缓冲器解开 。 |


> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L162)  
引入版本：4.0.0


---

### createResource {#createResource}

#### \<instance> createResource() {#instance-createresource}


**说明:**

为此 WebGL 缓冲器创建 WebGL 缓冲器 。

由构建器自动调用。 如果 WebGLBaffer 需要重新创建, 也可以再次调用 。


> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L139](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L139)  
引入版本：3.80.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此 WebGLBaferWrapper, 从 GL 上下文中删除 基本的 WebGLBaffer , 并释放所有对 dataBuffer 及其输入的数组视图的引用 。


> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L284](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L284)  
引入版本：3.80.0


---

### resize {#resize}

#### \<instance> resize(bytes) {#instance-resizebytes}


**说明:**

更改此 WebGL 缓冲器的 dataBuffer 大小。 这将重现 `dataBuffer` 和其中的视图。 所有数据都将丢失。 所有视图都重现到 `dataBuffer` 将被销毁并重现 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bytes | number | 否 | 字节中缓冲的新大小 。 |


> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L229](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L229)  
引入版本：4.0.0


---

### update {#update}

#### \<instance> update([bytes], [offset]) {#instance-updatebytes-offset}


**说明:**

更新此 WebGLBaferWrapper 中的数据。 dataBuffer 必须包含要上传到 GPU 的新数据。 指定的数据范围从本地的 dataBuffer 上传到 GPO 上的 WebGLBaffer 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| bytes | number | 是 |  | 缓冲器中要更新的字节数。 如果不指定, 则会更新整个缓冲 。 |
| offset | number | 是 | 0 | 冲抵到缓冲器开始更新数据 。 |


> 源码：[src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L190](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLBufferWrapper.js#L190)  
引入版本：4.0.0


---

---
