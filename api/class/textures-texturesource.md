# TextureSource {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/textures-texturesource)

纹理源是包含纹理实际源数据.

它包罗原始像素数据——通常是从文件系统或网络上装入的图像元素,一个Canvas元素,或者一个视频元素——并管理相应的 WebGL 用于渲染器的纹理对象。 WebGL 模式, 纹理源创建并拥有 `WebGLTextureWrapper` 上传到 GPU 。

您通常不会直接创建纹理源。 相反, 当文字管理器添加了纹理时, 它会自动创建。 您可以通过 `Texture.source` 访问它, 这是一系列纹理源例。 大多数纹理都有单一的纹理源, 但多层纹理可以有多个 。

纹理可以包含多个纹理源,这只有在多阿特拉斯加载时才会发生.

**构造函数**

`new TextureSource(texture, source, [width], [height], [flipY])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 |  | 这个纹理源属于的纹理. |
| source | [Phaser.Types.Textures.TextureSource](/api/typedef/types-textures#texturesource) | 否 |  | 源头图像数据. |
| width | number | 是 |  | 源图像的可选宽度。 如果没有给出, 则来源于源图像本身 。 |
| height | number | 是 |  | 源图像的可选高度。 如果不给它, 则来源于源图像本身 。 |
| flipY | boolean | 是 | true | 设置 `UNPACK_FLIP_Y_WEBGL` 上传时的 WebGL 纹理用途的标志 。 |

---


**作用域**: static

> 源码：[src/textures/TextureSource.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L13)  
引入版本：3.0.0

## 公开成员 {#public-members}

### compressionAlgorithm {#compressionAlgorithm}

#### compressionAlgorithm: number {#compressionalgorithm-number}


**说明:**

持有压缩纹理算法,或者如果不是压缩纹理,则持有`null`.

在Phaser 3.60之前,这个值总是持有`null`.


> 源码：[src/textures/TextureSource.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L95)  
引入版本：3.0.0


---

### flipY {#flipY}

#### flipY: boolean {#flipy-boolean}


**说明:**

`UNPACK_FLIP_Y_WEBGL`旗是否在上传时设置在这个WebGL纹理上。当`true`时,纹理数据在上传到GPU时会垂直翻转.


> 源码：[src/textures/TextureSource.js#L204](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L204)  
引入版本：3.20.0


---

### glTexture {#glTexture}

#### glTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#gltexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

源图像的包裹的 WebGL 纹理。 如果此纹理源已经从 WebGLTexture 驱动, 那么这个包装器包含一个对 WebGLTExture 的引用 。


> 源码：[src/textures/TextureSource.js#L192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L192)  
引入版本：3.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

源图像的高度。 如果构造器中未指定, 它将会检查 `naturalHeight`, `videoHeight`, 然后检查源图像的 `height` 属性 。


> 源码：[src/textures/TextureSource.js#L127](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L127)  
引入版本：3.0.0


---

### image {#image}

#### image: [Phaser.Types.Textures.TextureSourceElement](/api/typedef/types-textures#texturesourceelement), null {#image-phasertypestexturestexturesourceelement-null}


**说明:**

图像数据.

这或者是一个图像元素, Canvas 元素, 视频元素, 或者如果 `source` 不是 HTMLElement , 则无效。 非 HTMLElemat 源包括压缩纹理, 数据阵列, 以及引用其他 WebGL 纹理 。


> 源码：[src/textures/TextureSource.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L81)  
引入版本：3.0.0


---

### isCanvas {#isCanvas}

#### isCanvas: boolean {#iscanvas-boolean}


**说明:**

源图像是 Canvas 元素吗 ?


> 源码：[src/textures/TextureSource.js#L147](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L147)  
引入版本：3.0.0


---

### isGLTexture {#isGLTexture}

#### isGLTexture: boolean {#isgltexture-boolean}


**说明:**

源图像是 WebGLTextureWrapper 吗 ?


> 源码：[src/textures/TextureSource.js#L174](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L174)  
引入版本：3.19.0


---

### isPowerOf2 {#isPowerOf2}

#### isPowerOf2: boolean {#ispowerof2-boolean}


**说明:**

源图像维度是二的功率吗?


> 源码：[src/textures/TextureSource.js#L183](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L183)  
引入版本：3.0.0


---

### isRenderTexture {#isRenderTexture}

#### isRenderTexture: boolean {#isrendertexture-boolean}


**说明:**

源图像是Render纹理吗?


> 源码：[src/textures/TextureSource.js#L165](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L165)  
引入版本：3.12.0


---

### isVideo {#isVideo}

#### isVideo: boolean {#isvideo-boolean}


**说明:**

源图像是视频元素吗 ?


> 源码：[src/textures/TextureSource.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L156)  
引入版本：3.20.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer), [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrenderercanvascanvasrenderer-phaserrendererwebglwebglrenderer}


**说明:**

指坎瓦斯或WebGL的铸币师.


> 源码：[src/textures/TextureSource.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L50)  
引入版本：3.7.0


---

### resolution {#resolution}

#### resolution: number {#resolution-number}


**说明:**

源图像的解析度 。


> 源码：[src/textures/TextureSource.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L107)  
引入版本：3.0.0


---

### scaleMode {#scaleMode}

#### scaleMode: number {#scalemode-number}


**说明:**

图像渲染时将使用比例模式。 无论是线性还是最接近 。


> 源码：[src/textures/TextureSource.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L137)  
引入版本：3.0.0


---

### source {#source}

#### source: [Phaser.Types.Textures.TextureSource](/api/typedef/types-textures#texturesource) {#source-phasertypestexturestexturesource}


**说明:**

图像数据的来源.

这是图像元素、 扫描仪元素、 视频元素、 渲染器或 WebGLTexture Wrapper 。

在Phaser 3.60及以上,它也可以是一个压缩纹理数据对象.


> 源码：[src/textures/TextureSource.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L68)  
引入版本：3.12.0


---

### texture {#texture}

#### texture: [Phaser.Textures.Texture](/api/class/textures-texture) {#texture-phasertexturestexture}


**说明:**

纹理这个纹理源实例属于.


> 源码：[src/textures/TextureSource.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L59)  
引入版本：3.0.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

源图像的宽度。 如果构造器中未指定, 它将会检查 `naturalWidth`, `videoWidth`, 然后检查源图像的 `width` 属性 。


> 源码：[src/textures/TextureSource.js#L117](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L117)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁此纹理源并释放相关资源。

在 WebGL 模式中, 基本的 WebGL 纹理通过渲染器从 GPU 中删除。 如果源是画布, 则返回 CanvasPool 。 然后将所有内部引用设置为 `null` 。


> 源码：[src/textures/TextureSource.js#L470](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L470)  
引入版本：3.0.0


---

### init {#init}

#### \<instance> init(game) {#instance-initgame}


**说明:**

需要时创建 WebGL 纹理,并设置纹理过滤模式.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 参考 Phaser游戏实例. |


> 源码：[src/textures/TextureSource.js#L217](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L217)  
引入版本：3.0.0


---

### setFilter {#setFilter}

#### \<instance> setFilter(filterMode) {#instance-setfilterfiltermode}


**说明:**

设置此纹理的过滤模式。

模式可以是线性,默认,也可以是近似.

对于像素艺术,你应该使用最接近。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| filterMode | [Phaser.Textures.FilterMode](/api/namespace/textures-filtermode) | 否 | 过滤模式。 |


> 源码：[src/textures/TextureSource.js#L287](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L287)  
引入版本：3.0.0


---

### setFlipY {#setFlipY}

#### \<instance> setFlipY([value]) {#instance-setflipyvalue}


**说明:**

设置纹理上传时WebGL纹理的`UNPACK_FLIP_Y_WEBGL`旗.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 是否应该将WebGL纹理在纹理上传的Y轴上翻转? |


> 源码：[src/textures/TextureSource.js#L309](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L309)  
引入版本：3.20.0


---

### setWrap {#setWrap}

#### \<instance> setWrap(wrapModeS, wrapModeT) {#instance-setwrapwrapmodes-wrapmodet}


**说明:**

设置此纹理源的包覆模式。 这只可用于 WebGL 。

包装模式可以是以下一种: 包装模式:

- Phaser.Textures.WrapMode.CLAMP_TO_EDGE

- Phaser.Textures.WrapMode.REPEAT

- Phaser.Textures.WrapMode.MIRRORED_REPEAT

注意, 仅支持 CLAMP_ TO_ EDGE 的非纹理功率。 如果为这样的纹理指定了另一个包模式, 则会忽略它 。

**标签:**

 - webglonly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| wrapModeS | [Phaser.Textures.WrapMode](/api/namespace/textures-wrapmode) | 否 | S( 横向) 轴的包覆模式 。 |
| wrapModeT | [Phaser.Textures.WrapMode](/api/namespace/textures-wrapmode) | 否 | T(垂直)轴的包模式。 |


**返回值:** [Phaser.Textures.TextureSource](/api/class/textures-texturesource) - 此纹理来源例.


> 源码：[src/textures/TextureSource.js#L329](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L329)  
引入版本：4.0.0


---

### update {#update}

#### \<instance> update() {#instance-update}


**说明:**

以当前源数据更新基本的 WebGLTexture。 使用管理纹理的游戏系统, 如文本或视频, 或内部数据更改, 自动调用。 您不需要手动调用这种方法, 除非您正在手动更新源数据 。


> 源码：[src/textures/TextureSource.js#L361](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L361)  
引入版本：3.7.0


---

### updateSize {#updateSize}

#### \<instance> updateSize(width, height) {#instance-updatesizewidth-height}


**说明:**

更新此纹理源的尺寸。 使用管理纹理的游戏系统自动调用, 如 Text, 使一个专用画布改变大小 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 源图像的新宽度 。 |
| height | number | 否 | 源图像的新高度. |


> 源码：[src/textures/TextureSource.js#L406](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L406)  
引入版本：4.0.0


---

### updateSource {#updateSource}

#### \<instance> updateSource(source) {#instance-updatesourcesource}


**说明:**

更改此纹理源的源数据。 这将用新源数据更新基本的 WebGLTexture 。

注意此选项不会更新纹理的任何消费者. 带有 `Size` 组件的框架和游戏对象在创建时会自动缓存宽度和高度, 因此如果这样更改纹理分辨率, 您需要更新它们 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Types.Textures.TextureSource](/api/typedef/types-textures#texturesource) | 否 | 新来源数据. |


> 源码：[src/textures/TextureSource.js#L427](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureSource.js#L427)  
引入版本：4.0.0


---

---
