# CanvasRenderer {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-canvas-canvasrenderer)

Canvas 渲染器负责管理2D画布渲染上下文,包括游戏画布所用的上下文,它跟踪特定上下文的内部状态,并可以将纹理化的游戏对象提供给它,同时考虑到α,混合,和缩放.

**构造函数**

`new CanvasRenderer(game)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 拥有这个渲染器的 Phaser游戏实例. |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/renderer/canvas/CanvasRenderer.js#L20](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L20)  
引入版本：3.0.0

## 公开成员 {#public-members}

### antialias {#antialias}

#### antialias: boolean {#antialias-boolean}


**说明:**

画《Sprites》时, 画画是否应该使用图像平滑?


> 源码：[src/renderer/canvas/CanvasRenderer.js#L141](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L141)  
引入版本：3.20.0


---

### blendModes {#blendModes}

#### blendModes: array {#blendmodes-array}


**说明:**

由 Canvas 渲染器支持的混合模式 。

这个对象映射 [Phaser.BlendModes](/api/constant/blendmodes) 来绘制堆肥操作 。


> 源码：[src/renderer/canvas/CanvasRenderer.js#L150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L150)  
引入版本：3.0.0


---

### config {#config}

#### config: object {#config-object}


**说明:**

CanvasRender 的本地配置设置 。


> 源码：[src/renderer/canvas/CanvasRenderer.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L47)  
引入版本：3.0.0


---

### currentContext {#currentContext}

#### currentContext: CanvasRenderingContext2D {#currentcontext-canvasrenderingcontext2d}


**说明:**

CanvasRenderer 目前在所有渲染操作中使用的画布上下文 。


> 源码：[src/renderer/canvas/CanvasRenderer.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L132)  
引入版本：3.0.0


---

### drawCount {#drawCount}

#### drawCount: number {#drawcount-number}


**说明:**

在一个框架里渲染的游戏对象的总数 。


> 源码：[src/renderer/canvas/CanvasRenderer.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L80)  
引入版本：3.0.0


---

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

拥有这个渲染器的 Phaser游戏实例.


> 源码：[src/renderer/canvas/CanvasRenderer.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L62)  
引入版本：3.0.0


---

### gameCanvas {#gameCanvas}

#### gameCanvas: HTMLCanvasElement {#gamecanvas-htmlcanvaselement}


**说明:**

游戏使用的画布元素 。


> 源码：[src/renderer/canvas/CanvasRenderer.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L108)  
引入版本：3.0.0


---

### gameContext {#gameContext}

#### gameContext: CanvasRenderingContext2D {#gamecontext-canvasrenderingcontext2d}


**说明:**

游戏循环期间用于渲染所有镜头的画布上下文.


> 源码：[src/renderer/canvas/CanvasRenderer.js#L123](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L123)  
引入版本：3.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

画布的高度被推向。


> 源码：[src/renderer/canvas/CanvasRenderer.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L99)  
引入版本：3.0.0


---

### isBooted {#isBooted}

#### isBooted: boolean {#isbooted-boolean}


**说明:**

变形器已经启动了吗?


> 源码：[src/renderer/canvas/CanvasRenderer.js#L211](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L211)  
引入版本：3.50.0


---

### snapshotState {#snapshotState}

#### snapshotState: [Phaser.Types.Renderer.Snapshot.SnapshotState](/api/typedef/types-renderer-snapshot#snapshotstate) {#snapshotstate-phasertypesrenderersnapshotsnapshotstate}


**说明:**

详细介绍目前计划中的快照 。

如果在此对象中设置了非null `callback`,则在当前框架完全渲染后将拍摄画布的快照.


> 源码：[src/renderer/canvas/CanvasRenderer.js#L161](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L161)  
引入版本：3.16.0


---

### type {#type}

#### type: number {#type-number}


**说明:**

常数,可以方便地识别出渲染器为坎瓦斯渲染器.


> 源码：[src/renderer/canvas/CanvasRenderer.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L71)  
引入版本：3.0.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

显示布的宽度


> 源码：[src/renderer/canvas/CanvasRenderer.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L90)  
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

### batchSprite {#batchSprite}

#### \<instance> batchSprite(sprite, frame, camera, [parentTransformMatrix]) {#instance-batchspritesprite-frame-camera-parenttransformmatrix}


**说明:**

取一个 Sprite 游戏对象, 或任何扩展它的对象, 并绘制到当前上下文 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sprite | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 要绘制的纹理游戏对象 。 |
| frame | [Phaser.Textures.Frame](/api/class/textures-frame) | 否 | 绘制的框,不一定是游戏对象拥有的框. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 用来进行渲染变换的相机. |
| parentTransformMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 母容器的变换矩阵, 如果设置 。 |


> 源码：[src/renderer/canvas/CanvasRenderer.js#L702](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L702)  
引入版本：3.12.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

删除所有事件听众, 并取消 Canvas 渲染器中的所有对象引用, 允许将其收集为垃圾 。


**Overrides:** Phaser.Events.EventEmitter#销毁


> 源码：[src/renderer/canvas/CanvasRenderer.js#L887](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L887)  
引入版本：3.0.0


---

### init {#init}

#### \<instance> init() {#instance-init}


**说明:**

设置渲染器所需的事件听器。 具体来说, 它会监听游戏 BCOT 事件以填充画布上的背景颜色, 并等待纹理管理器的READY事件, 然后再完成启动序列并注册缩放管理器的调整处理器 。


> 源码：[src/renderer/canvas/CanvasRenderer.js#L223](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L223)  
引入版本：3.0.0


---

### onResize {#onResize}

#### \<instance> onResize(gameSize, baseSize) {#instance-onresizegamesize-basesize}


**说明:**

管理由缩放管理器发出的 `resize` 事件的事件处理器 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameSize | [Phaser.Structs.Size](/api/class/structs-size) | 否 | 默认的游戏大小对象。 这是未修改的游戏尺寸 。 |
| baseSize | [Phaser.Structs.Size](/api/class/structs-size) | 否 | 基数大小对象。 游戏尺寸乘以分辨率。 画布宽度 / 高度值与此相符 。 |


> 源码：[src/renderer/canvas/CanvasRenderer.js#L277](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L277)  
引入版本：3.16.0


---

### postRender {#postRender}

#### \<instance> postRender() {#instance-postrender}


**说明:**

恢复游戏背景的全球设置, 如果选中的话, 则需要快照 。

后退台阶发生在所有镜头都完成后


**Fires:** [Phaser.Renderer.Events#event:POST_RENDER](/api/event/renderer-events#post_render)


> 源码：[src/renderer/canvas/CanvasRenderer.js#L540](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L540)  
引入版本：3.0.0


---

### preRender {#preRender}

#### \<instance> preRender() {#instance-prerender}


**说明:**

在每次渲染循环开始时调用。 重新设置游戏背景的全局alpha, 复合操作, 并转换为默认操作。 如果渲染器在每次渲染前配置清空画布, 则清除视图, 如果背景不透明, 则填充已配置的背景颜色。 在发布 PRE_ RENDER_ CLEAR 和 PRE_ RENDER 事件之前, 请保存上下文状态并重排绘图数 。


**Fires:** [Phaser.Renderer.Events#event:PRE_RENDER_CLEAR](/api/event/renderer-events#pre_render_clear), [Phaser.Renderer.Events#event:PRE_RENDER](/api/event/renderer-events#pre_render)


> 源码：[src/renderer/canvas/CanvasRenderer.js#L377](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L377)  
引入版本：3.0.0


---

### render {#render}

#### \<instance> render(scene, children, camera) {#instance-renderscene-children-camera}


**说明:**

核心为场景镜头做制动步骤.

透过给定的游戏对象阵列,用给定的相机来进行图化.

这是用 `CameraManager.render` 方法调用。 相机管理器实例属于 Scene, 并且被 Scene Systems. render 方法引用 。

如果`Camera.visible`是`false`,或者`Camera.alpha`是零,则不叫这个方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 场景要演化。 |
| children | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 一系列可以由给定的相机渲染的过滤游戏对象. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 场景摄像机要用它来制作 |


**Fires:** [Phaser.Renderer.Events#event:RENDER](/api/event/renderer-events#render)


> 源码：[src/renderer/canvas/CanvasRenderer.js#L422](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L422)  
引入版本：3.0.0


---

### resetTransform {#resetTransform}

#### \<instance> resetTransform() {#instance-resettransform}


**说明:**

将当前上下文的变换矩阵重置为身份矩阵,从而重置任何变换.


> 源码：[src/renderer/canvas/CanvasRenderer.js#L315](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L315)  
引入版本：3.0.0


---

### resize {#resize}

#### \<instance> resize([width], [height]) {#instance-resizewidth-height}


**说明:**

将渲染器的内部宽度和高度值更新到给定的维度,并释放 RESIZE 事件。当缩放管理器检测到画布大小变化时,此值会自动调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 是 | 变形器的新宽度 。 |
| height | number | 是 | 造物器的新高度. |


**Fires:** [Phaser.Renderer.Events#event:RESIZE](/api/event/renderer-events#resize)


> 源码：[src/renderer/canvas/CanvasRenderer.js#L295](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L295)  
引入版本：3.0.0


---

### setAlpha {#setAlpha}

#### \<instance> setAlpha(alpha) {#instance-setalphaalpha}


**说明:**

设置当前上下文的全局性阿尔法。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| alpha | number | 否 | 新的α要使用,其中0完全透明,1完全不透明. |


**返回值:** [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) - 这个 CanvasRender 天体 。


> 源码：[src/renderer/canvas/CanvasRenderer.js#L360](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L360)  
引入版本：3.0.0


---

### setBlendMode {#setBlendMode}

#### \<instance> setBlendMode(blendMode) {#instance-setblendmodeblendmode}


**说明:**

设置当前上下文的混合模式(组合操作)。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| blendMode | string | 否 | 新的混合模式,应该使用。 |


**返回值:** [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) - 这个 CanvasRender 天体 。


> 源码：[src/renderer/canvas/CanvasRenderer.js#L326](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L326)  
引入版本：3.0.0


---

### setContext {#setContext}

#### \<instance> setContext([ctx]) {#instance-setcontextctx}


**说明:**

更改所有绘图操作都针对的 Canvas 渲染上下文 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ctx | CanvasRenderingContext2D | 是 | 新的 Canvas 渲染上下文以绘制所有内容。 空留以重置游戏 Canvas 。 |


**返回值:** [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) - 坎瓦斯兰德勒的例子.


> 源码：[src/renderer/canvas/CanvasRenderer.js#L343](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L343)  
引入版本：3.12.0


---

### snapshot {#snapshot}

#### \<instance> snapshot(callback, [type], [encoderOptions]) {#instance-snapshotcallback-type-encoderoptions}


**说明:**

在当前框架解析后, 将整个游戏视图端口的快照排成一个 。

要捕捉特定区域,请参见`snapshotArea`方法。要捕捉特定像素,请参见`snapshotPixel`。

只有一张快照可以激活_per fram_。例如,如果您已经调用 `snapshotPixel`,那么调用这种方法将覆盖它。

抓图通过从画布数据中创建一个图像对象来工作,这是一个阻塞过程,它得到的画布大小越大,成本就越高,所以请小心你是如何在游戏中使用这个的.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 |  | 创建了快照图像后要引用的函数 。 |
| 类型 | string | 是 | "'image/png'" | 图像创建的格式,通常为`image/png`或`image/jpeg`. |
| encoderOptions | number | 是 | 0.92 | 图像质量,介于0到1. 用于图像格式,具有失速压缩,例如`image/jpeg`. |


**返回值:** [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) - 这个坎瓦斯兰德。


> 源码：[src/renderer/canvas/CanvasRenderer.js#L607](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L607)  
引入版本：3.0.0


---

### snapshotArea {#snapshotArea}

#### \<instance> snapshotArea(x, y, width, height, callback, [type], [encoderOptions]) {#instance-snapshotareax-y-width-height-callback-type-encoderoptions}


**说明:**

在当前框架渲染后,将游戏视图端口的指定区域进行图示。

要捕捉整个游戏的视港,请查看`snapshot`方法. 要捕捉到特定的像素,请参看`snapshotPixel`.

只有一张快照可以激活_per fram_。例如,如果您已经调用 `snapshotPixel`,那么调用这种方法将覆盖它。

抓图通过从画布数据中创建一个图像对象来工作,这是一个阻塞过程,它得到的画布大小越大,成本就越高,所以请小心你是如何在游戏中使用这个的.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 坐标是用来抓的 |
| y | number | 否 |  | 调和器用来抓 |
| width | number | 否 |  | 要抓取的区域的宽度 。 |
| height | number | 否 |  | 高地的地盘要抓 |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 |  | 创建了快照图像后要引用的函数 。 |
| 类型 | string | 是 | "'image/png'" | 图像创建的格式,通常为`image/png`或`image/jpeg`. |
| encoderOptions | number | 是 | 0.92 | 图像质量,介于0到1. 用于图像格式,具有失速压缩,例如`image/jpeg`. |


**返回值:** [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) - 这个坎瓦斯兰德。


> 源码：[src/renderer/canvas/CanvasRenderer.js#L632](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L632)  
引入版本：3.16.0


---

### snapshotCanvas {#snapshotCanvas}

#### \<instance> snapshotCanvas(canvas, callback, [getPixel], [x], [y], [width], [height], [type], [encoderOptions]) {#instance-snapshotcanvascanvas-callback-getpixel-x-y-width-height-type-encoderoptions}


**说明:**

绘制给定画布的指定区域。

与其他快照方法不同,这个方法被立即处理,不等待下一次渲染.

抓图通过从画布数据中创建一个图像对象来工作,这是一个阻塞过程,它得到的画布大小越大,成本就越高,所以请小心你是如何在游戏中使用这个的.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| canvas | HTMLCanvasElement | 否 |  | 画布从。 |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 |  | 创建了快照图像后要引用的函数 。 |
| getPixel | boolean | 是 | false | 抓取一个像素作为颜色对象, 还是区域作为图像对象? |
| x | number | 是 | 0 | 坐标是用来抓的 |
| y | number | 是 | 0 | 调和器用来抓 |
| width | number | 是 | "canvas.width" | 要抓取的区域的宽度 。 |
| height | number | 是 | "canvas.height" | 高地的地盘要抓 |
| 类型 | string | 是 | "'image/png'" | 图像创建的格式,通常为`image/png`或`image/jpeg`. |
| encoderOptions | number | 是 | 0.92 | 图像质量,介于0到1. 用于图像格式,具有失速压缩,例如`image/jpeg`. |


**返回值:** [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) - 这个坎瓦斯兰德。


> 源码：[src/renderer/canvas/CanvasRenderer.js#L567](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L567)  
引入版本：3.19.0


---

### snapshotPixel {#snapshotPixel}

#### \<instance> snapshotPixel(x, y, callback) {#instance-snapshotpixelx-y-callback}


**说明:**

在当前框架渲染后,将游戏视图端口中给定的像素的快照排出日程。

要捕捉整个游戏的视港,请查看`snapshot`方法。要捕捉特定区域,请参看`snapshotArea`。

只有一张快照可以激活_per fram_。例如,如果您已经调用 `snapshotArea`,那么调用这种方法将覆盖它。

与另外两种快照方法不同,这个会返回包含所请求像素的颜色数据的`Color`对象,它不需要创建内部的Canvas或Image对象,因此执行速度要快很多,使用内存较少.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 以像素的x坐标获取. |
| y | number | 否 | 用于像素的y坐标 |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 | 提取快照像素数据后要引用的函数 。 |


**返回值:** [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) - 这个坎瓦斯兰德。


> 源码：[src/renderer/canvas/CanvasRenderer.js#L672](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/CanvasRenderer.js#L672)  
引入版本：3.16.0


---

---
