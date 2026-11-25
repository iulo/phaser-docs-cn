# CanvasTexture {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/textures-canvastexture)

坎瓦斯纹理是一种特殊的纹理,它以HTML Canvas Element作为源头.

您可以使用此纹理的属性直接绘制到画布元素, 使用浏览器中可用的所有标准画布操作。 任何游戏对象都可以被赋予此纹理, 并将随它渲染 。

注意: 在 WebGL 下运行时, Canvas 纹理需要重新生成其基础的 WebGLTexture 并将其重新加载到 GPU 中, 否则您对纹理的修改将无法看见 。 要做到这一点, 您应该在完成对画布的修改后调用 `CanvasTexture.refresh()`z 。 请尝试并保持最小, 特别是在大画布大小上, 或者您会不慎将 GPU 上传到它 。 如果使用 Canvas 渲染器, 此限制不适用 。

它从一个覆盖整个画布的框架开始。 您可以添加更多画布, 使用 `add` 方法指定画布的段落 。

如果您需要调整画布的大小, 使用 `setSize` 方法, 以便精确更新所有基础纹理数据。 忘记这样做( 即直接从您的代码中更改画布大小) 可能会造成图形错误 。

**构造函数**

`new CanvasTexture(manager, key, source, width, height)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) | 否 | 引用此纹理属于的纹理管理器 。 |
| key | string | 否 | 此纹理中独特的基于字符串的键 。 |
| source | HTMLCanvasElement | 否 | 用作此纹理底部的画布元素 。 |
| width | number | 否 | 画布的宽度。 |
| height | number | 否 | 画布的高度 |

---


**作用域**: static


**继承**

> [Phaser.Textures.Texture](/api/class/textures-texture)  



> 源码：[src/textures/CanvasTexture.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L14)  
引入版本：3.7.0

## 继承的成员 {#inherited-members}


**From [Phaser.Textures.Texture](/api/class/textures-texture):**


 - [customData](/api/class/textures-texture#customData)
 - [dataSource](/api/class/textures-texture#dataSource)
 - [firstFrame](/api/class/textures-texture#firstFrame)
 - [frames](/api/class/textures-texture#frames)
 - [frameTotal](/api/class/textures-texture#frameTotal)
 - [key](/api/class/textures-texture#key)
 - [manager](/api/class/textures-texture#manager)
 - [smoothPixelArt](/api/class/textures-texture#smoothPixelArt)
 - [source](/api/class/textures-texture#source)




---

## 公开成员 {#public-members}

### buffer {#buffer}

#### buffer: ArrayBuffer {#buffer-arraybuffer}


**说明:**

与上下文图像数据大小相同的矩阵缓冲器 。


> 源码：[src/textures/CanvasTexture.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L145)  
引入版本：3.13.0


---

### canvas {#canvas}

#### canvas: HTMLCanvasElement {#canvas-htmlcanvaselement}


**说明:**

源头坎瓦斯元素.


> 源码：[src/textures/CanvasTexture.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L68)  
引入版本：3.7.0


---

### context {#context}

#### context: CanvasRenderingContext2D {#context-canvasrenderingcontext2d}


**说明:**

2D Canvas 渲染背景.


> 源码：[src/textures/CanvasTexture.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L78)  
引入版本：3.7.0


---

### data {#data}

#### data: Uint8ClampedArray {#data-uint8clampedarray}


**说明:**

将 Uint8ClampedArray 视图插入 `buffer` 。 画布改变时使用 `update` 方法填充此内容。 请注意, 由于Epic 浏览器等浏览器的安全限制, 在一些浏览器中无法使用 。


> 源码：[src/textures/CanvasTexture.js#L120](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L120)  
引入版本：3.13.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

Canvas 的高度。 此属性只读, 如果您想要更改, 请使用 `setSize` 方法 。


> 源码：[src/textures/CanvasTexture.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L99)  
引入版本：3.7.0


---

### imageData {#imageData}

#### imageData: ImageData {#imagedata-imagedata}


**说明:**

上下文图像数据。 当画布改变时, 使用 `update` 方法填充此数据 。


> 源码：[src/textures/CanvasTexture.js#L110](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L110)  
引入版本：3.13.0


---

### pixels {#pixels}

#### pixels: Uint32Array {#pixels-uint32array}


**说明:**

进入`buffer`的Uint32箭头视图.


> 源码：[src/textures/CanvasTexture.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L136)  
引入版本：3.13.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

Canvas 的宽度。 如果您想要更改, 此属性只读, 请使用 `setSize` 方法 。


> 源码：[src/textures/CanvasTexture.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L88)  
引入版本：3.7.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Textures.Texture](/api/class/textures-texture):**


 - [add](/api/class/textures-texture#add)
 - [get](/api/class/textures-texture#get)
 - [getDataSourceImage](/api/class/textures-texture#getDataSourceImage)
 - [getFrameBounds](/api/class/textures-texture#getFrameBounds)
 - [getFrameNames](/api/class/textures-texture#getFrameNames)
 - [getFramesFromTextureSource](/api/class/textures-texture#getFramesFromTextureSource)
 - [getSourceImage](/api/class/textures-texture#getSourceImage)
 - [getTextureSourceIndex](/api/class/textures-texture#getTextureSourceIndex)
 - [has](/api/class/textures-texture#has)
 - [remove](/api/class/textures-texture#remove)
 - [setDataSource](/api/class/textures-texture#setDataSource)
 - [setFilter](/api/class/textures-texture#setFilter)
 - [setSmoothPixelArt](/api/class/textures-texture#setSmoothPixelArt)
 - [setSource](/api/class/textures-texture#setSource)
 - [setWrap](/api/class/textures-texture#setWrap)




---

## 公开方法 {#public-methods}

### clear {#clear}

#### \<instance> clear([x], [y], [width], [height], [update]) {#instance-clearx-y-width-height-update}


**说明:**

清除指定区域中的 Canvas 纹理, 将其重置为透明。 如果没有给出区域, 则清除整个 Canvas 纹理 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 区域左上角的x坐标以清除. |
| y | number | 是 | 0 | 区域左上角的y坐标来清除. |
| width | number | 是 |  | 区域宽度. |
| height | number | 是 |  | 地区高度. |
| update | boolean | 是 | true | 更新内部的图像数据缓冲器和数组。 |


**返回值:** [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) - 坎瓦斯纹理.


> 源码：[src/textures/CanvasTexture.js#L554](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L554)  
引入版本：3.7.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

破坏这种纹理并发布其来源和框架的引用。


**重写:** Phaser.Textures.Texture#销毁


> 源码：[src/textures/CanvasTexture.js#L626](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L626)  
引入版本：3.16.0


---

### draw {#draw}

#### \<instance> draw(x, y, source, [update]) {#instance-drawx-y-source-update}


**说明:**

绘制给定的图像或 Canvas 元素到此 CanvasTexture, 然后更新内部的图像数据缓冲器和阵列 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 坐标x以绘制源 。 |
| y | number | 否 |  | 绘制源的Y坐标 。 |
| source | HTMLImageElement \| HTMLCanvasElement | 否 |  | 画到画布上的元素 。 |
| update | boolean | 是 | true | 更新内部的图像数据缓冲器和数组。 |


**返回值:** [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) - 这个CanvasTexture。


> 源码：[src/textures/CanvasTexture.js#L213](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L213)  
引入版本：3.13.0


---

### drawFrame {#drawFrame}

#### \<instance> drawFrame(key, [frame], [x], [y], [update]) {#instance-drawframekey-frame-x-y-update}


**说明:**

绘制给定的纹理帧到这个 CanvasTexture, 然后更新内部的图像数据缓冲器和阵列 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 纹理中独特的基于字符串的键. |
| frame | string \| number | 是 |  | 框架的字符串名称,或整数索引,从纹理中获取。 |
| x | number | 是 | 0 | 坐标x以绘制源 。 |
| y | number | 是 | 0 | 绘制源的Y坐标 。 |
| update | boolean | 是 | true | 更新内部的图像数据缓冲器和数组。 |


**返回值:** [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) - 这个CanvasTexture。


> 源码：[src/textures/CanvasTexture.js#L241](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L241)  
引入版本：3.16.0


---

### getCanvas {#getCanvas}

#### \<instance> getCanvas() {#instance-getcanvas}


**说明:**

获得坎瓦斯元素.


**返回值:** HTMLCanvasElement - 纹理使用的 Canvas DOM 元素 。


> 源码：[src/textures/CanvasTexture.js#L528](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L528)  
引入版本：3.7.0


---

### getContext {#getContext}

#### \<instance> getContext() {#instance-getcontext}


**说明:**

获取 2D 坎瓦斯渲染背景 。


**返回值:** CanvasRenderingContext2D - 以 Canvas 渲染背景 。


> 源码：[src/textures/CanvasTexture.js#L541](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L541)  
引入版本：3.7.0


---

### getData {#getData}

#### \<instance> getData(x, y, width, height) {#instance-getdatax-y-width-height}


**说明:**

从指定的位置和大小获取图像数据区域。 您可以使用 `CanvasTexture.putData` 将它写回, 或者操纵它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 区域左上角的x坐标从中获取图像数据。 必须是这个 CanvasTexture 的尺寸, 并且是一个整数 。 |
| y | number | 否 | 区域左上角的y坐标来获取图像数据。 必须是这个 CanvasTexture 的尺寸, 并且是一个整数 。 |
| width | number | 否 | 用于提取图像数据 的矩形宽度。 正值为 右, 负值为 左 。 |
| height | number | 否 | 将提取图像数据时的矩形高度。 正值下降, 负值上升 。 |


**返回值:** ImageData - 从这个CanvasTexture中提取的图像数据(ImageData).


> 源码：[src/textures/CanvasTexture.js#L360](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L360)  
引入版本：3.16.0


---

### getIndex {#getIndex}

#### \<instance> getIndex(x, y) {#instance-getindexx-y}


**说明:**

返回 CanvasTexture 中给定像素的图像数据索引 。

该索引可以直接从`this.data`阵列读取.

索引指向数组中的红色值。随后的3个索引分别指向绿色、蓝色和α。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 要获取的像素的x坐标。 必须是这个 CanvasTexture 的尺寸, 并且是一个整数 。 |
| y | number | 否 | 要得到的像素的y坐标。 必须是这个 CanvasTexture 的尺寸, 并且是一个整数 。 |


**返回值:** number - 图像数据阵列中像素的索引,或者如果坐标超出范围,则使用 - 1 。


> 源码：[src/textures/CanvasTexture.js#L480](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L480)  
引入版本：3.16.0


---

### getPixel {#getPixel}

#### \<instance> getPixel(x, y, [out]) {#instance-getpixelx-y-out}


**说明:**

从此纹理中获取特定像素的颜色,并将其存储在一个彩色对象中.

如果您自创建以来已经绘制到 CanvasTexture 中, 您必须拨打 `CanvasTexture.update` 来刷新阵列缓冲器, 否则它可能返回过时的颜色值, 或者更糟糕的是 - 在试图访问一个不存在的阵列元素时, 丢出一个运行时错误 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 要获取的像素的x坐标。 必须是这个 CanvasTexture 的尺寸, 并且是一个整数 。 |
| y | number | 否 | 要得到的像素的y坐标。 必须是这个 CanvasTexture 的尺寸, 并且是一个整数 。 |
| out | [Phaser.Display.Color](/api/namespace/display-color) | 是 | 一个将像素值存储到其中的颜色对象。 如果不提供新的颜色对象, 将会创建 。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 一个在r,g,b和属性中设置了红色,绿色,蓝色和α值的对象.


> 源码：[src/textures/CanvasTexture.js#L386](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L386)  
引入版本：3.13.0


---

### getPixels {#getPixels}

#### \<instance> getPixels([x], [y], [width], [height]) {#instance-getpixelsx-y-width-height}


**说明:**

返回包含指定区域所有像素的阵列。

如果请求的区域延伸到这个CanvasTexture的边界之外,则该区域被切换以适应.

如果您自创建以来已经绘制到 CanvasTexture 中, 您必须拨打 `CanvasTexture.update` 来刷新阵列缓冲器, 否则它可能返回过时的颜色值, 或者更糟糕的是 - 在试图访问一个不存在的阵列元素时, 丢出一个运行时错误 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 区域左上角的x坐标。 必须是这个 CanvasTexture 的尺寸, 并且是一个整数 。 |
| y | number | 是 | 0 | 区域左上角的y坐标。 必须是这个 CanvasTexture 的尺寸, 并且是一个整数 。 |
| width | number | 是 |  | 要获取的区域宽度。 必须是一个整数。 如果不给出, 则默认为画布宽度 。 |
| height | number | 是 |  | 要得到的区域高度。 必须是整数。 如果不给定, 将设置为 `width` 。 |


**返回值:** Array.\<Array.\<[Phaser.Types.Textures.PixelConfig](/api/typedef/types-textures#pixelconfig)>> - 2d 阵列的像素对象。


> 源码：[src/textures/CanvasTexture.js#L425](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L425)  
引入版本：3.16.0


---

### putData {#putData}

#### \<instance> putData(imageData, x, y, [dirtyX], [dirtyY], [dirtyWidth], [dirtyHeight]) {#instance-putdataimagedata-x-y-dirtyx-dirtyy-dirtywidth-dirtyheight}


**说明:**

将图像数据置于指定坐标处的 CanvasTexture 上下文中。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| imageData | ImageData | 否 |  | 图像数据将放置在指定位置 。 |
| x | number | 否 |  | 将 imageData 放置在 X 坐标上。 必须在 CanvasTexture 的尺寸范围内, 并是一个整数 。 |
| y | number | 否 |  | 将imageData放入的Y坐标,必须位于这个CanvasTexture的维度内,并是一个整数. |
| dirtyX | number | 是 | 0 | 左上角的横向位置(x坐标),从中提取图像数据。 |
| dirtyY | number | 是 | 0 | 左上角的垂直位置(y坐标),从中提取图像数据。 |
| dirtyWidth | number | 是 |  | 要绘制的矩形宽度。 默认为图像数据的宽度 。 |
| dirtyHeight | number | 是 |  | 要绘制的矩形高度。 默认为图像数据的高度 。 |


**返回值:** [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) - 这个CanvasTexture。


> 源码：[src/textures/CanvasTexture.js#L332](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L332)  
引入版本：3.16.0


---

### refresh {#refresh}

#### \<instance> refresh() {#instance-refresh}


**说明:**

如果您运行在 WebGL 下, 则应该手工使用此功能。 这将从 Canvas 源头刷新 WebGLTexture 。 只有知道画布已经改变, 才会使用此功能, 因为这样做需要相当大的 GPU 纹理分配成本 。


**返回值:** [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) - 这个CanvasTexture。


> 源码：[src/textures/CanvasTexture.js#L511](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L511)  
引入版本：3.7.0


---

### setPixel {#setPixel}

#### \<instance> setPixel(x, y, red, green, blue, [alpha]) {#instance-setpixelx-y-red-green-blue-alpha}


**说明:**

在 CanvasTexture 中设置像素,以表示给定的颜色和α值。

这是一项昂贵的操作, 大量运行, 所以少用。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 要设置的像素的x坐标。 必须是这个 CanvasTexture 的尺寸, 并且是一个整数 。 |
| y | number | 否 |  | 要设置的像素的y坐标。 必须是这个 CanvasTexture 的尺寸, 并且是一个整数 。 |
| red | number | 否 |  | 红色值,数字在0到255之间 |
| green | number | 否 |  | 绿色的颜色值,数字在0到255之间. |
| blue | number | 否 |  | 蓝色的颜色值,数字在0到255之间. |
| alpha | number | 是 | 255 | α值,数字在0到255之间. |


**返回值:** [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) - 这个CanvasTexture。


> 源码：[src/textures/CanvasTexture.js#L291](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L291)  
引入版本：3.16.0


---

### setSize {#setSize}

#### \<instance> setSize(width, [height]) {#instance-setsizewidth-height}


**说明:**

改变这个 Canvas 纹理的大小 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 坎瓦斯号的新宽度. |
| height | number | 是 | 坎瓦斯号的新高度。 如果不给出, 将使用宽度作为高度 。 |


**返回值:** [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) - 坎瓦斯纹理.


> 源码：[src/textures/CanvasTexture.js#L587](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L587)  
引入版本：3.7.0


---

### update {#update}

#### \<instance> update() {#instance-update}


**说明:**

这从当前上下文中重新创建了 `imageData`。 然后它又重建了 ArrayBuffer 、 `data` Uint8ClampedArray 参考器和 `pixels` Uint32Array 。

警告:这是一个非常昂贵的操作,所以要小心使用.


**返回值:** [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) - 这个CanvasTexture。


> 源码：[src/textures/CanvasTexture.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/CanvasTexture.js#L173)  
引入版本：3.13.0


---

---
