# WebGLTextureWrapper {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-wrappers-webgltexturewrapper)

用于WebGL纹理的包装器,包含用于创建它的所有信息.

网络GLTexture 不应该在 WebGLRender 外曝光,所以 WebGLRENder 可以处理上下文丢失和其他事件而不需要其他系统知道。 总是使用 WebGLTexture Wrapper 代替 。

**构造函数**

`new WebGLTextureWrapper(renderer, mipLevel, minFilter, magFilter, wrapT, wrapS, format, pixels, width, height, [pma], [forceSize], [flipY])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 |  | 拥有这个包装的 WebGLRender 实例 。 |
| mipLevel | number | 否 |  | 纹理的米普级. |
| minFilter | number | 否 |  | 过滤纹理。 |
| magFilter | number | 否 |  | 过滤纹理。 |
| wrapT | number | 否 |  | 纹理的包扎模式 。 |
| wrapS | number | 否 |  | 纹理的包扎模式 。 |
| format | number | 否 |  | 纹理使用哪种格式 。 |
| pixels | object | 否 |  | 用于填充纹理的像素数据。可以是 Canvas, Video, ImageData, Uint8Array, 也可以是压缩纹理对象 。 |
| width | number | 否 |  | 纹理的宽度以像素表示. |
| height | number | 否 |  | 纹理高度以像素表示. |
| pma | boolean | 是 | true | 纹理是否预先多倍化了α? |
| forceSize | boolean | 是 | false | 如果 `true` , 它会使用向这种方法传递的宽度和高度, 不管像素的尺寸大小如何. |
| flipY | boolean | 是 | true | 设置 `UNPACK_FLIP_Y_WEBGL` 上传时的 WebGL 纹理用途的标志 。 |

---


**作用域**: static

> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L10)  
引入版本：3.80.0

## 公开成员 {#public-members}

### batchUnit {#batchUnit}

#### batchUnit: number {#batchunit-number}


**说明:**

此纹理将在当前渲染批次中绑定到的纹理单元 。

此选项应该由批发者设定。 快速的判断方法可以确定此纹理是否包含在批发中。 如果是 - 1 , 它没有 。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L207](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L207)  
引入版本：4.0.0


---

### flipY {#flipY}

#### flipY: boolean {#flipy-boolean}


**说明:**

设置 `UNPACK_FLIP_Y_WEBGL` 上传时的 WebGL 纹理用途的标志 。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L185](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L185)  
引入版本：3.80.0


---

### forceSize {#forceSize}

#### forceSize: boolean {#forcesize-boolean}


**说明:**

是否使用宽度和高度属性, 不论像素尺寸大小 。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L176](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L176)  
引入版本：3.80.0


---

### format {#format}

#### format: number {#format-number}


**说明:**

纹理的WebGL像素格式(如`gl.RGBA`或`gl.RGB`).


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L131](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L131)  
引入版本：3.80.0


---

### generateMipmap {#generateMipmap}

#### generateMipmap {#generatemipmap}


**说明:**

生成纹理的 mipmap 级别。 这种方法叫做内部 。

微波炉只有在此纹理被 mipmap 激活且大小为 2 的电势时才会生成。 否则此函数返回时不会产生副作用 。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L467](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L467)  
引入版本：4.1.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

纹理高度以像素表示.


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L158)  
引入版本：3.80.0


---

### isMipmap {#isMipmap}

#### isMipmap {#ismipmap}


**说明:**

返回是否设置了纹理以使用 impmap minification 过滤器 。


**返回值:** boolean - 是否设置纹理使用 mipmap minification filter 。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L450](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L450)  
引入版本：4.1.0


---

### isRenderTexture {#isRenderTexture}

#### isRenderTexture: boolean {#isrendertexture-boolean}


**说明:**

是否将此用作渲染器 。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L70)  
引入版本：3.80.0


---

### magFilter {#magFilter}

#### magFilter: number {#magfilter-number}


**说明:**

纹理的放大滤波器,作为WebGL滤波器常数(如`gl.LINEAR`或`gl.NEAREST`),在纹理放大时应用.


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L100)  
引入版本：3.80.0


---

### minFilter {#minFilter}

#### minFilter: number {#minfilter-number}


**说明:**

纹理的微分滤波器,作为WebGL滤波器常数(如`gl.LINEAR`或`gl.NEAREST`),在纹理缩放时应用.


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L89)  
引入版本：3.80.0


---

### mipLevel {#mipLevel}

#### mipLevel: number {#miplevel-number}


**说明:**

纹理的米普级.


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L80)  
引入版本：3.80.0


---

### needsMipmapRegeneration {#needsMipmapRegeneration}

#### needsMipmapRegeneration: boolean {#needsmipmapregeneration-boolean}


**说明:**

是否要重生成 mipmaps 。 这只与内容迅速变化的动态纹理和帧布有关。 修改内容的过程应该设置此旗帜。 当纹理被下一条绑定时, WebGLTexture UnitsWrapper 将触发 `generateMipmap` 方法 。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L221](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L221)  
引入版本：4.1.0


---

### pixels {#pixels}

#### pixels: object {#pixels-object}


**说明:**

像素数据。 这是用于创建 WebGLTexture 的源数据 。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L140)  
引入版本：3.80.0


---

### pma {#pma}

#### pma: boolean {#pma-boolean}


**说明:**

纹理是否预先多倍化了α?


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L167](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L167)  
引入版本：3.80.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrendererwebglwebglrenderer}


**说明:**

这个WebGLLTexture属于WebGLRenderer.


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L47)  
引入版本：4.0.0


---

### spectorMetadata {#spectorMetadata}

#### spectorMetadata: object {#spectormetadata-object}


**说明:**

电话 `__SPECTOR_Metadata` 属性的损益 `WebGLTexture`,用于添加额外的数据到调试SpectorJS集成中.


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L491](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L491)  
引入版本：3.80.0


---

### webGLTexture {#webGLTexture}

#### webGLTexture: WebGLTexture {#webgltexture-webgltexture}


**说明:**

这张包装纸正在包装的 WebGLTexture.

此属性随时会改变。 因此, 您不应该存储此值的引用。 它只应直接传递到 WebGL API 中进行绘图 。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L56)  
引入版本：3.80.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

纹理的宽度以像素表示.


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L149](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L149)  
引入版本：3.80.0


---

### wrapS {#wrapS}

#### wrapS: number {#wraps-number}


**说明:**

纹理的S(横向)轴的包接模式,作为WebGL的包接常数(如`gl.REPEAT`或`gl.CLAMP_TO_EDGE`).


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L121)  
引入版本：3.80.0


---

### wrapT {#wrapT}

#### wrapT: number {#wrapt-number}


**说明:**

纹理的T(垂直)轴的包接模式,作为WebGL的包接常数(如`gl.REPEAT`或`gl.CLAMP_TO_EDGE`).


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L111)  
引入版本：3.80.0


---

## 公开方法 {#public-methods}

### _processTexture {#_processTexture}

#### \<instance> _processTexture() {#instance-_processtexture}


**说明:**

设定每存储值的 WebGLTexture 参数 。


**访问权限:** 受保护


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L382](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L382)  
引入版本：4.0.0


---

### createResource {#createResource}

#### \<instance> createResource() {#instance-createresource}


**说明:**

从给定参数创建 WebGLTexture 。

由构建器自动调用。 如果 WebGLTexture 需要重新创建, 也可以再次调用 。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L239](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L239)  
引入版本：3.80.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

从 GPU 删除 WebGLTextture, 如果还没有。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L516](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L516)  
引入版本：3.80.0


---

### resize {#resize}

#### \<instance> resize(width, height) {#instance-resizewidth-height}


**说明:**

将 WebGLTextture 调整为新尺寸。 这将破坏纹理的内容 。

包模式将更新:如果新大小为 2 的功率,则将更新 REPEAT, 如果没有 CLAMP_TO_EDGE 。

纹理微细滤波器将更新 :

- 使用游戏配置中的 mipmap 设置, 前提是:

  - 大小是两强

  - 有个缩影设定

  - 这不是渲染纹理, OR MIPMAP 重生被启用

- 否则使用常规纹理过滤器。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | WebGLTexture 的新宽度 。 |
| height | number | 否 | 网络GLTexture的新高度. |


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L278](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L278)  
引入版本：4.0.0


---

### update {#update}

#### \<instance> update(source, width, height, flipY, wrapS, wrapT, minFilter, magFilter, format) {#instance-updatesource-width-height-flipy-wraps-wrapt-minfilter-magfilter-format}


**说明:**

从更新的源头更新 WebGLTextture 。

只有在源是Canvas或Video元素时才应使用此功能.

因为纹理通常会变成复杂而独特的东西,这种方法迫使所有属性都无需检查就更新.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | object | 否 | 使用WebGLTextture更新的源头 。 |
| width | number | 否 | WebGLTexture 的新宽度 。 |
| height | number | 否 | 网络GLTexture的新高度. |
| flipY | boolean | 否 | 网络GLTexture应该设置 `UNPACK_FLIP_Y_WEBGL`吗? |
| wrapS | number | 否 | WebGLTexture 的新包头模式 。 |
| wrapT | number | 否 | WebGLTexture 的新包头模式 。 |
| minFilter | number | 否 | WebGLTexture 的新微缩过滤器 。 |
| magFilter | number | 否 | WebGLTexture 的新放大过滤器 。 |
| format | number | 否 | WebGLTextture 的新格式 。 |


> 源码：[src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L340](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L340)  
引入版本：3.80.0


---

---
