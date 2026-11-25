# DynamicTexture {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/textures-dynamictexture)

动态纹理(Dynamic Texture)是一种特殊的纹理,它允许您直接绘制纹理,帧和最类游戏对象.

您可以带许多复杂的对象到这个纹理, 然后可以用来作为其他游戏对象, 如Sprites 的基础纹理。 如果您再更新这个纹理, 所有使用它的游戏对象都会立即更新, 立即反映变化 。

这是一种强大的方法,在运行时生成动态纹理,这种纹理是WebGL友好的,并且不会在每个变化上引用昂贵的GPU上传.

```js
const t = this.textures.addDynamicTexture('player', 64, 128);
// draw objects to t
this.add.sprite(x, y, 'player');
this.render();
```

因为这是Phaser内部的标准纹理,因此可以添加框架,意思是用它来生成精灵表,纹理图集或瓦片集.

在 WebGL1 下,一个框架缓冲器,即这个动态纹理内部使用的东西,不能被反异化。这意味着当将形状或图形等对象绘制到这个纹理时,它们可能看起来没有在边缘周围作别名。这是WebGL1的技术限制。要绕过它,在艺术包中创建你的形状,然后将它绘制到这个纹理上。

如果您在游戏中激活了 mipmap 支持, 它不会自动应用到动态图案。 这是因为在 10 微秒内重生成 mipmap 的纹理成本, 一个框架的性能损失很大 。 如果您想要用 mipmap 来渲染您的动态图案, 您也必须激活 compare 配置选项 Z`mipmapRegeneration` 。

如果 WebGL 上下文丢失, 此动态图解将丢失其内容。 一旦恢复上下文( 由 `restorewebgl` 事件标注) , 您可以选择重绘动态图解的内容。 您负责重绘逻辑 。

**构造函数**

`new DynamicTexture(manager, key, [width], [height], [forceEven])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| manager | [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) | 否 |  | 引用此纹理属于的纹理管理器 。 |
| key | string | 否 |  | 此纹理中独特的基于字符串的键 。 |
| width | number | 是 | 256 | 此动态纹理的宽度以像素表示。 默认为 256 x 256 。 |
| height | number | 是 | 256 | 此动态纹理在像素中的高度。 默认为 256 x 256 。 |
| forceEven | boolean | 是 | true | 强制给定的宽度和高度以四舍五入到偶数。这大大改善了渲染质量。 如果您知道需要奇数大小的纹理, 则设置为假 。 |

---


**作用域**: static


**继承**

> [Phaser.Textures.Texture](/api/class/textures-texture)  



> 源码：[src/textures/DynamicTexture.js#L20](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L20)  
引入版本：3.60.0

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

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#camera-phasercamerasscene2dcamera}


**说明:**

内部的摄像机,可以用来围绕这个动态纹理移动.

控制它就像你对任何场景摄像机一样。区别在于它只影响你绘制到这个纹理上的**Game对象**(不是纹理)的放置。

你可以滚动,放大和旋转这台摄像机.


> 源码：[src/textures/DynamicTexture.js#L164](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L164)  
引入版本：3.12.0


---

### canvas {#canvas}

#### canvas: HTMLCanvasElement {#canvas-htmlcanvaselement}


**说明:**

引用属于 Canvas 元素的渲染语境 。


> 源码：[src/textures/DynamicTexture.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L145)  
引入版本：3.2.0


---

### commandBuffer {#commandBuffer}

#### commandBuffer: array {#commandbuffer-array}


**说明:**

用于绘制此动态纹理的一系列命令。 使用 `render` 方法冲洗。 `clear` 方法也会清除此数组, 然后存储它本身 。


> 源码：[src/textures/DynamicTexture.js#L134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L134)  
引入版本：4.0.0


---

### context {#context}

#### context: CanvasRenderingContext2D {#context-canvasrenderingcontext2d}


**说明:**

2D Canvas 渲染背景.


> 源码：[src/textures/DynamicTexture.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L154)  
引入版本：3.7.0


---

### drawingContext {#drawingContext}

#### drawingContext: [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) {#drawingcontext-phaserrendererwebgldrawingcontext}


**说明:**

此动态纹理的绘图上下文。 此上下文包含动态纹理所绘制的帧缓冲器 。


> 源码：[src/textures/DynamicTexture.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L178)  
引入版本：4.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

动态纹理的高度 。

将此属性作为只读属性。 使用 `setSize` 方法来更改大小 。


> 源码：[src/textures/DynamicTexture.js#L123](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L123)  
引入版本：3.60.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer), [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrenderercanvascanvasrenderer-phaserrendererwebglwebglrenderer}


**说明:**

参考游戏实例使用的 Canvas 或 WebGL 朗德尔 。


> 源码：[src/textures/DynamicTexture.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L103)  
引入版本：3.2.0


---

### type {#type}

#### type: string {#type-string}


**说明:**

此天体的内部数据类型 。


> 源码：[src/textures/DynamicTexture.js#L83](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L83)  
引入版本：3.60.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

此动态纹理的宽度 。

将此属性作为只读属性。 使用 `setSize` 方法来更改大小 。


> 源码：[src/textures/DynamicTexture.js#L112](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L112)  
引入版本：3.60.0


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

### callback {#callback}

#### \<instance> callback(callback) {#instance-callbackcallback}


**说明:**

添加调试程序运行时的调用。 调用程序将作为命令缓冲器的一步运行。 它可用于为下一步绘制设置条件 。

注意, 只有在 `render()` 调用后, 才会执行 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | function | 否 | 渲染过程中要运行的调用函数 。 |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 这个动态纹理实例 。


> 源码：[src/textures/DynamicTexture.js#L1123](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L1123)  
引入版本：4.0.0


---

### capture {#capture}

#### \<instance> capture(entry, config) {#instance-captureentry-config}


**说明:**

绘制此动态纹理对象。 您可以绘制游戏世界中显示的物体, 或在配置中使用各种参数覆盖 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| entry | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 任何可渲染的游戏对象。 |
| config | [Phaser.Types.Textures.CaptureConfig](/api/typedef/types-textures#captureconfig) | 否 | 抓取的配置对象 。 |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 这个动态纹理实例 。


> 源码：[src/textures/DynamicTexture.js#L850](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L850)  
引入版本：4.0.0


---

### clear {#clear}

#### \<instance> clear([x], [y], [width], [height]) {#instance-clearx-y-width-height}


**说明:**

清除从此动态纹理中的一部分或所有东西, 将它擦除并重置为空白、 透明、 纹理。 要清除一个区域, 请指定 `x`、 `y`、 `width`和 `height` 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 地区左座坐标清空. |
| y | number | 是 | 0 | 地区最高坐标清空. |
| width | number | 是 | "this.width" | 区域宽度要清除 。 |
| height | number | 是 | "this.height" | 地区高度要清空. |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 这个动态纹理实例 。


> 源码：[src/textures/DynamicTexture.js#L619](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L619)  
引入版本：3.2.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

破坏这种纹理并发布其来源和框架的引用。


**重写:** Phaser.Textures.Texture#销毁


> 源码：[src/textures/DynamicTexture.js#L1292](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L1292)  
引入版本：3.60.0


---

### draw {#draw}

#### \<instance> draw(entries, [x], [y], [alpha], [tint]) {#instance-drawentries-x-y-alpha-tint}


**说明:**

绘制给定的对象,或一系列对象,以图示此动态纹理。

它可以接受下列任何一种:

* 任意可渲染的游戏对象,例如Sprite,Text,Graphics或TileSprite.

* 平面图层.

* A组,内容将依次加以修改和绘制。

* 容器,内装物将按顺序完全悬挂和抽取。

* 一个场景显示列表,通过`Scene.children`来绘制整个列表.

* 另一种动态纹理,或称Render纹理.

* 纹理帧实例 。

* 字符串。 用于从纹理管理器中查找纹理 。

注1:你不能为自己绘制动态纹理。

注2: Game Objects将使用摄像机,而纹理和帧则不会. 纹理和帧是使用`stamp`方法绘制的.

如果在一组或容器内通过,则只吸引在使用`willRender()`方法时返回`true`的儿童。 也就是说,一个有10个儿童的容器,其中5个有`visible=false`,只吸引5个可见的容器。

如果在一系列游戏对象中通过,它会绘制全部,无论它们是否通过`willRender`检查.

您可以在一个字符串中通过, 在这种情况下它会寻找匹配该字符串的纹理管理器, 并绘制底框。 如果您需要指定要绘制的框的确切位置, 请使用 `drawFrame` 方法 。

您可以在 `x` 和 `y` 坐标中通过绘制对象。 坐标的使用因绘制对象不同而不同。 如果对象是组、 容器或显示列表, 则坐标将 _ 添加到孩子的位置。 对于所有其他类型的对象, 坐标是准确的。 对于纹理和框架, `x` 和 `y` 值是纹理的中间值 。

`alpha`和`tint`的值只用于纹理帧。游戏对象在绘制时使用自己的α和锡值。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| entries | any | 否 |  | 任何可变游戏对象,或组合、容器、显示列表、其他纹理、纹理帧或其中任何一组。 |
| x | number | 是 | 0 | 绘制框架的x位置,或对象的偏移。 |
| y | number | 是 | 0 | 绘制框架的y位置,或对象的偏移。 |
| alpha | number | 是 | 1 | α值。 仅在绘制纹理帧到此纹理时使用。 游戏对象使用自己的α 。 |
| tint | number | 是 | "0xffffff" | 颜色值。 仅在绘制纹理帧到此纹理时使用。 游戏对象只使用自己的颜色值 。 WebGL 。 |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 这个动态纹理实例 。


> 源码：[src/textures/DynamicTexture.js#L743](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L743)  
引入版本：3.2.0


---

### erase {#erase}

#### \<instance> erase(entries, [x], [y], [alpha], [tint]) {#instance-eraseentries-x-y-alpha-tint}


**说明:**

使用 EASE 的混合模式绘制给定对象或一系列对象到此动态纹理。这可以消除从此纹理中显示的对象中的任何已填充像素。

这种方法在内部使用`draw`方法,参数的表现也相同.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| entries | any | 否 |  | 任何可渲染的游戏对象,或组合、容器、显示列表、纹理、纹理帧或其中任何一组。 |
| x | number | 是 | 0 | 绘制框架的x位置,或对象的偏移。 |
| y | number | 是 | 0 | 绘制框架的y位置,或对象的偏移。 |
| alpha | number | 是 | 1 | α值。 仅在绘制纹理帧到此纹理时使用。 游戏对象使用自己的α 。 |
| tint | number | 是 | "0xffffff" | 颜色值。 仅在绘制纹理帧到此纹理时使用。 游戏对象只使用自己的颜色值 。 WebGL 。 |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 这个动态纹理实例 。


> 源码：[src/textures/DynamicTexture.js#L700](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L700)  
引入版本：3.16.0


---

### fill {#fill}

#### \<instance> fill(rgb, [alpha], [x], [y], [width], [height]) {#instance-fillrgb-alpha-x-y-width-height}


**说明:**

用给定的颜色填充此动态纹理。

默认它会填充整个纹理,但您可以通过使用x,y,宽度和高度参数来设置它以填充特定的矩形区域.

颜色应采用六分法,即0xff000红,0x00ff00绿等.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| rgb | number | 否 |  | 填充此动态纹理的颜色, 如 0xff000 表示红色 。 |
| alpha | number | 是 | 1 | 填充时所用的α值 。 |
| x | number | 是 | 0 | 填充矩的左坐标. |
| y | number | 是 | 0 | 填充矩形的顶部坐标. |
| width | number | 是 | "this.width" | 填充矩的宽度 。 |
| height | number | 是 | "this.height" | 填充矩的高度. |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 这个动态纹理实例 。


> 源码：[src/textures/DynamicTexture.js#L576](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L576)  
引入版本：3.2.0


---

### finishCapture {#finishCapture}

#### \<instance> finishCapture(entry, cacheConfig) {#instance-finishcaptureentry-cacheconfig}


**说明:**

恢复 `capture` 方法中被覆盖的对象属性。 这种方法在渲染过程中自动被调用。 不要直接调用它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| entry | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 恢复属性的游戏对象 。 |
| cacheConfig | [Phaser.Types.Textures.CaptureConfig](/api/typedef/types-textures#captureconfig) | 否 | 缓存属性要恢复 。 |


> 源码：[src/textures/DynamicTexture.js#L977](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L977)  
引入版本：4.0.0


---

### getWebGLTexture {#getWebGLTexture}

#### \<instance> getWebGLTexture() {#instance-getwebgltexture}


**说明:**

返回基础的 WebGLTexture Wrapper, 如果不是以 Canvas 模式运行的话。


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) - 基础的WebGLTextureWrapper,如果不是以Canvas模式运行的话.


> 源码：[src/textures/DynamicTexture.js#L1239](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L1239)  
引入版本：3.60.0


---

### preserve {#preserve}

#### \<instance> preserve(preserve) {#instance-preservepreserve}


**说明:**

设置此动态纹理的保存旗。 通常, 每次渲染后, 命令缓冲被清除。 当此旗帜被设定为 `true` 时, 命令缓冲在渲染之间被保存。 这样就可以在每个渲染时重复相同的绘图命令 。

确定在开始时给`clear()`打电话,如果你不想在自己顶端积累绘画细节.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| preserve | boolean | 否 | 渲染后是否保留命令缓冲 。 |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 这个动态纹理实例 。


> 源码：[src/textures/DynamicTexture.js#L1102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L1102)  
引入版本：4.0.0


---

### render {#render}

#### \<instance> render() {#instance-render}


**说明:**

将缓冲绘图命令渲染到此动态纹理中。 您必须这样做才能看到任何被绘制到它上 。


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 这个动态纹理实例 。


> 源码：[src/textures/DynamicTexture.js#L291](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L291)  
引入版本：4.0.0


---

### renderCanvas {#renderCanvas}

#### \<instance> renderCanvas(renderer, mask, camera) {#instance-rendercanvasrenderer-mask-camera}


**说明:**

这是无线轨道仪方法,动态纹理不能直接变成Canvas渲染器。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) \| [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 将交付给的风景画展 |
| mask | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 将渲染的蒙面游戏对象 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 摄像机要摄像机 |


> 源码：[src/textures/DynamicTexture.js#L1277](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L1277)  
引入版本：3.60.0


---

### renderWebGL {#renderWebGL}

#### \<instance> renderWebGL(renderer, src, camera, parentMatrix) {#instance-renderwebglrenderer-src-camera-parentmatrix}


**说明:**

将此动态纹理设置在纹理管理器上。 印章然后调用它的渲染方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 参考当前活动WebGL渲染器. |
| src | [Phaser.GameObjects.Image](/api/class/gameobjects-image) | 否 | 此调用中正在提供游戏对象 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 正在制作游戏对象的摄像机 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 如果游戏对象被嵌入, 此变换矩阵将定义 |


> 源码：[src/textures/DynamicTexture.js#L1255](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L1255)  
引入版本：3.60.0


---

### repeat {#repeat}

#### \<instance> repeat(key, [frame], [x], [y], [width], [height], [config]) {#instance-repeatkey-frame-x-y-width-height-config}


**说明:**

将给定的纹理帧绘制到这个动态纹理中, 作为填充图案, 即基于框架尺寸的网格铺放。 它使用内部的 `TileSprite`来反复绘制框架 。

纹理通过基于字符串的键来引用, 存储在纹理管理器中.

您可以选择提供位置、 宽度、 高度、 α 和 tint 值, 用于绘制框架。 位置控制重复填充开始的左上角。 宽度和高度控制填充区域的大小 。

如果需要,这种位置可以是负的,但维度不能。

这种方法尊重动态纹理的摄像机设置.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 要使用的纹理键, 如存储在纹理管理器中 。 |
| frame | string \| number | 是 |  | 纹理内框架的名称或索引。 如果不需要, 设置为 `null` 来跳过此参数 。 |
| x | number | 是 | 0 | 从( 可以是负的, 以抵消) 开始绘制框架的 x 位置 。 |
| y | number | 是 | 0 | 开始从( 可以是负的来抵消) 绘制帧的 Y 位置 。 |
| width | number | 是 | "this.width" | 重复框架在内部的区域宽度。默认为此动态纹理的宽度 。 |
| height | number | 是 | "this.height" | 区域高度以重复内框。默认为此动态纹理的高度 。 |
| config | [Phaser.Types.GameObjects.TileSprite.TileSpriteConfig](/api/typedef/types-gameobjects-tilesprite#tilespriteconfig) | 是 |  | 重复纹理的 TileSprite 配置对象, 允许您在它上设置更多属性 。 |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 这个动态纹理实例 。


> 源码：[src/textures/DynamicTexture.js#L1033](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L1033)  
引入版本：3.60.0


---

### setSize {#setSize}

#### \<instance> setSize(width, [height], [forceEven]) {#instance-setsizewidth-height-forceeven}


**说明:**

将此动态纹理调整到给定的新尺寸。

在 WebGL 中,它会破坏并重建这个动态纹理正在使用的帧缓冲器。在 Canvas 中,它会调整基本画布 DOM 元素的大小 。

这两种方法将抹去目前绘制到这种纹理上的一切。

如果给出的维度与已经使用的维度相同,那么称这个方法将无济于事.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 否 |  | 此动态纹理的新宽度 。 |
| height | number | 是 | "width" | 此动态纹理的新高度。 如果不指定, 将设置为 `width` 。 |
| forceEven | boolean | 是 | true | 强制给定的宽度和高度以四舍五入到偶数。这大大改善了渲染质量。 如果您知道需要奇数大小的纹理, 则设置为假 。 |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 动态纹理。


> 源码：[src/textures/DynamicTexture.js#L203](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L203)  
引入版本：3.10.0


---

### snapshot {#snapshot}

#### \<instance> snapshot(callback, [type], [encoderOptions]) {#instance-snapshotcallback-type-encoderoptions}


**说明:**

取出这整个动态纹理的快照。

即刻拍摄,但结果通过给定的回调返回.

要捕捉到这个动态纹理的一部分,请查看`snapshotArea`方法。要捕捉到一个特定的像素,请参看`snapshotPixel`方法。

快照工作时使用 WebGL `readPixels` 特性将帧缓冲器中的每个像素抓入一个 ArrayBufferView 。 它然后解析这个, 将内容复制到临时的 Canvas 中, 并最后从中创建一个图像对象, 即图像返回到提供的调用 。

总之,这是一个计算成本和阻断过程, 它的花费越大, 这个动态纹理的分辨率越大, 所以请小心,你是如何在游戏中使用这个的。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 |  | 创建了快照图像后要引用的函数 。 |
| 类型 | string | 是 | "'image/png'" | 图像创建的格式,通常为`image/png`或`image/jpeg`. |
| encoderOptions | number | 是 | 0.92 | 图像质量,介于0到1. 用于图像格式,具有失速压缩,例如`image/jpeg`. |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 这个动态纹理实例 。


> 源码：[src/textures/DynamicTexture.js#L1184](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L1184)  
引入版本：3.19.0


---

### snapshotArea {#snapshotArea}

#### \<instance> snapshotArea(x, y, width, height, callback, [type], [encoderOptions]) {#instance-snapshotareax-y-width-height-callback-type-encoderoptions}


**说明:**

绘制此动态纹理的指定区域。

即刻拍摄,但结果通过给定的回调返回.

要捕捉整个动态纹理,请参见`snapshot`方法。要捕捉到一个特定的像素,请参见`snapshotPixel`方法。

快照工作时使用 WebGL `readPixels` 特性将帧缓冲器中的每个像素抓入一个 ArrayBufferView 。 它然后解析这个, 将内容复制到临时的 Canvas 中, 并最后从中创建一个图像对象, 即图像返回到提供的调用 。

总之,这是一个计算成本和阻断过程, 它的花费越大, 这个动态纹理的分辨率越大, 所以请小心,你是如何在游戏中使用这个的。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 坐标是用来抓的 |
| y | number | 否 |  | 调和器用来抓 |
| width | number | 否 |  | 要抓取的区域的宽度 。 |
| height | number | 否 |  | 高地的地盘要抓 |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 |  | 创建了快照图像后要引用的函数 。 |
| 类型 | string | 是 | "'image/png'" | 图像创建的格式,通常为`image/png`或`image/jpeg`. |
| encoderOptions | number | 是 | 0.92 | 图像质量,介于0到1. 用于图像格式,具有失速压缩,例如`image/jpeg`. |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 这个动态纹理实例 。


> 源码：[src/textures/DynamicTexture.js#L1142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L1142)  
引入版本：3.19.0


---

### snapshotPixel {#snapshotPixel}

#### \<instance> snapshotPixel(x, y, callback) {#instance-snapshotpixelx-y-callback}


**说明:**

从此动态纹理中获取给定像素的快照 。

即刻拍摄,但结果通过给定的回调返回.

要捕捉整个动态纹理,请查看`snapshot`方法。要捕捉到此动态纹理的一部分,请查看`snapshotArea`方法。

与其他两种快照方法不同,这个方法会将包含请求像素的颜色数据的`Color`对象发送回调,它不需要创建内部的Canvas或Image对象,因此执行速度要快很多,使用内存比其他快照方法要少.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 以像素的x坐标获取. |
| y | number | 否 | 用于像素的y坐标 |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 | 提取快照像素数据后要引用的函数 。 |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 这个动态纹理实例 。


> 源码：[src/textures/DynamicTexture.js#L1213](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L1213)  
引入版本：3.19.0


---

### stamp {#stamp}

#### \<instance> stamp(key, [frame], [x], [y], [config]) {#instance-stampkey-frame-x-y-config}


**说明:**

取下给定的纹理键和帧, 然后在给定的 x 和 y 坐标上盖章 。 您可以使用可选的“ 配置” 参数来提供更多关于如何应用纹章的选项, 包括 alpha、 tint、 角度、 比例和来源 。

默认情况下,帧会在其中心点上的x/y坐标上盖章.

如果您想从左上方盖章, 请将配置的 `originX` 和 `originY` 属性都设置为 0 。

这种方法忽略了动态纹理的`camera`属性.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 要使用的纹理键, 如存储在纹理管理器中 。 |
| frame | string \| number | 是 |  | 纹理内框架的名称或索引。 如果不需要, 设置为 `null` 来跳过此参数 。 |
| x | number | 是 | 0 | 绘制帧的x位置 。 |
| y | number | 是 | 0 | 绘制框架的y位置 。 |
| config | [Phaser.Types.Textures.StampConfig](/api/typedef/types-textures#stampconfig) | 是 |  | 印章配置对象,允许您设置印章的α,锡,角度,比例和来源. |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 这个动态纹理实例 。


> 源码：[src/textures/DynamicTexture.js#L645](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L645)  
引入版本：3.60.0


---

### startCapture {#startCapture}

#### \<instance> startCapture(entry, config) {#instance-startcaptureentry-config}


**说明:**

准备使用 `capture` 方法渲染对象。 渲染过程中, 此方法会自动调用。 不要直接调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| entry | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 要设置的捕获对象 。 |
| config | [Phaser.Types.Textures.CaptureConfig](/api/typedef/types-textures#captureconfig) | 否 | 抓取的配置对象 。 |


**返回值:** [Phaser.Types.Textures.CaptureConfig](/api/typedef/types-textures#captureconfig) - 配置对象,包含`transform`中合适的父变换,以及任何被覆盖字段中缓存的对象属性.


> 源码：[src/textures/DynamicTexture.js#L872](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/DynamicTexture.js#L872)  
引入版本：4.0.0


---

---
