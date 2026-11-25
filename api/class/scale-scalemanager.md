# ScaleManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/scale-scalemanager)

缩放管理器处理游戏画布的缩放,调整大小和对齐.

缩放处理方式是设置游戏画布到固定大小, 并在游戏配置中定义。 您也会定义游戏配置中的母容器。 如果没有给出父容器, 则默认使用文档正文。 缩放管理器将查看_ parent_ 内可用的空间, 并相应缩放画布。 缩放处理方式是通过设置画布 CSS 宽度和高度属性, 使画布元素本身的宽度和高度不受影响。 因此, 缩放是通过保持核心画布的大小和“ 伸缩” 来达到的。 这样可以给出与使用 CSS 属性相同的结果和速度 。 `transform-scale` CSS属性,不需要浏览器前缀处理.

对比例尺的计算受到边框父大小的很大影响,这是画布母大小的计算维度。 母元素的 CSS 规则在比例尺管理器的操作中起着重要作用。 例如, 如果父方没有定义的宽度或高度, 则自动中心化等动作将无法实现所需的结果。 比例尺管理器与您在主机页面上设置的 CSS 同步工作, 而不是控制它 。

#### Parent and Display canvas containment guidelines: {#parent-and-display-canvas-containment-guidelines}

- 样式 父元素 (游戏画布) 来控制父大小,从而控制游戏大小和布局.

- 父元素的 CSS 样式应该_ 有效_ 应用最大( 和最小) 约束行为 。

- 父元素应_ not_ 应用一个补丁, 因为此不计。

  如果要求贴补金适用于父母的亲生子女,或适用于父母的亲生子女。

  如果您需要在游戏容器周围添加边框、边框或任何其他 CSS,则使用父元素,

  应用 CSS 来代替, 否则您会不断调整游戏容器的形状 。

- 显示布局 CSS 样式( 即边距、 大小) 不应更改 / 指定为

  缩放管理器可以更新这些表格。

#### Scale Modes {#scale-modes}

缩放处理方式由 `scaleMode` 属性决定。 默认是 `NONE`, 它防止 Phaser 缩放或触摸画布, 或者说它的主页。 在这个模式下, 您负责所有的缩放。 其他缩放模式可以自动缩放 。

如果您想要缩放游戏, 使其始终适合父游戏中可用的空间, 请使用缩放模式 `FIT` 。 请查看其他缩放模式的文档, 查看可用的选项。 以下是一个基本配置, 显示如何设置缩放模式 :

```javascript
scale: {
    parent: 'yourgamediv',
    mode: Phaser.Scale.FIT,
    width: 800,
    height: 600
}
```

将 `scale` 配置对象置于游戏配置中。

如果您希望画布直接调整大小, 让画布本身填充可用的空间( 即它没有缩放, 而是重新缩放), 那么使用 `RESIZE` 比例模式。 这将给您一个1: 1 绘制画布像素到游戏大小的映射。 在这个模式中 CSS 不用于画布的缩放, 它会被字面调整, 以填补父方内部所有可用的空间 。 您应该非常小心您正在创建的画布的大小, 因为面积越大, GPU 需要做的就越多, 并且非常容易快速击中填充率限制 。

对于复杂的,自定义缩放要求,您可能应当考虑使用`RESIZE`比例模式,而你自己的局限性就放在了下面: 画幅尺寸,以及用游戏场景来管理缩放。 然而,对于绝大多数游戏来说,`FIT`模式很可能是最常用的。

请欣赏缩放管理器无法实现奇迹。 它所做的只是根据它能从周围区域推断出的大小来尽可能地放大您的游戏画布。 有很多类型的环境, 需要您来引导和帮助画布定位, 特别是当您在像 React 和 Vue 这样的渲染框架中构建时。 如果您的页面需要元标记来防止用户缩放手势, 或者像 , 那么您就负责确保这些画布存在于 html 中 。

#### Centering {#centering}

您也可以自动将游戏画布置于中心位置。 这在很大程度上依赖于父版的配置和样式, 因为中心位置的偏移完全基于母版元素内可用的空间。 默认中位被禁用, 或者可以横向、 纵向或两者同时应用。 例如 :

```javascript
scale: {
    parent: 'yourgamediv',
    autoCenter: Phaser.Scale.CENTER_BOTH,
    width: 800,
    height: 600
}
```

#### Fullscreen API {#fullscreen-api}

如果浏览器支持, 您可以将游戏发送到全屏模式。 在这个模式下, 游戏将填充整个显示, 移除屏幕上所有浏览器 UI 和其他任何内容。 它会一直处于这个模式, 直到游戏禁用它, 或者直到用户在桌面上按下 ESCape 。 这是实现桌面游戏的好方法, 就像浏览器的经验, 但是它确实需要一个现代浏览器来处理它。 一些移动浏览器也支持这个模式 。

**构造函数**

`new ScaleManager(game)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 参考Phaser.Game案例. |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/scale/ScaleManager.js#L23](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L23)  
引入版本：3.16.0

## 公开成员 {#public-members}

### _resetZoom {#_resetZoom}

#### _resetZoom: boolean {#_resetzoom-boolean}


**说明:**

游戏缩放因子修改时设置内部旗帜.


> 源码：[src/scale/ScaleManager.js#L254](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L254)  
引入版本：3.19.0


---

### autoCenter {#autoCenter}

#### autoCenter: [Phaser.Scale.CenterType](/api/typedef/scale#centertype) {#autocenter-phaserscalecentertype}


**说明:**

自动将画布置于父目录中? 不同的中枢模式是 :

1. 不得中心处.

2. 横向和纵向都居中.

3. 水平中心 。

4. 垂直居中( 垂直居中) 。

请注意,要将游戏画布居中,您必须指定一个有大小设置的父程序,或者画布的父程序是文档.body.


> 源码：[src/scale/ScaleManager.js#L284](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L284)  
引入版本：3.16.0


---

### autoRound {#autoRound}

#### autoRound: boolean {#autoround-boolean}


**说明:**

如果设定, 画布大小会自动通过 Math. deloor 传递。 由此得出四舍五入的像素显示值, 对于在遗留设备上的表现和低功率设备很重要, 但代价是一些浏览器窗口没有实现“ 完美” 的配置 。


> 源码：[src/scale/ScaleManager.js#L273](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L273)  
引入版本：3.16.0


---

### baseSize {#baseSize}

#### baseSize: [Phaser.Structs.Size](/api/class/structs-size) {#basesize-phaserstructssize}


**说明:**

基数组件 。

修改后的游戏大小,即自动圆形的gameSize,用于设置画布宽度和高度(但不是CSS风格).


> 源码：[src/scale/ScaleManager.js#L206](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L206)  
引入版本：3.16.0


---

### canvas {#canvas}

#### canvas: HTMLCanvasElement {#canvas-htmlcanvaselement}


**说明:**

参考 Phaser 用来制作游戏的 HTML Canvas Elements 。


> 源码：[src/scale/ScaleManager.js#L146](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L146)  
引入版本：3.16.0


---

### canvasBounds {#canvasBounds}

#### canvasBounds: [Phaser.Geom.Rectangle](/api/class/geom-rectangle) {#canvasbounds-phasergeomrectangle}


**说明:**

画布元素的 DOM 边框 。


> 源码：[src/scale/ScaleManager.js#L155](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L155)  
引入版本：3.16.0


---

### dirty {#dirty}

#### dirty: boolean {#dirty-boolean}


**说明:**

缩放管理器的脏态。 如果父大小和当前大小之间有变化, 设置 。


> 源码：[src/scale/ScaleManager.js#L340](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L340)  
引入版本：3.16.0


---

### displayScale {#displayScale}

#### displayScale: [Phaser.Math.Vector2](/api/class/math-vector2) {#displayscale-phasermathvector2}


**说明:**

baseSize与canvasBounds之间的比例系数.


> 源码：[src/scale/ScaleManager.js#L264](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L264)  
引入版本：3.16.0


---

### displaySize {#displaySize}

#### displaySize: [Phaser.Structs.Size](/api/class/structs-size) {#displaysize-phaserstructssize}


**说明:**

显示大小组件 。

画布样式所用的大小,在比例模式,父值和其他值中作为因素.


> 源码：[src/scale/ScaleManager.js#L218](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L218)  
引入版本：3.16.0


---

### fullscreen {#fullscreen}

#### fullscreen: [Phaser.Device.Fullscreen](/api/typedef/device#fullscreen) {#fullscreen-phaserdevicefullscreen}


**说明:**

引用设备. Fulllscreen 对象 。


> 源码：[src/scale/ScaleManager.js#L312](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L312)  
引入版本：3.16.0


---

### fullscreenTarget {#fullscreenTarget}

#### fullscreenTarget: any {#fullscreentarget-any}


**说明:**

发送到全屏模式的 DOM 元素 。


> 源码：[src/scale/ScaleManager.js#L321](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L321)  
引入版本：3.16.0


---

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

参考Phaser.Game案例.


> 源码：[src/scale/ScaleManager.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L136)  
引入版本：3.15.0


---

### gameSize {#gameSize}

#### gameSize: [Phaser.Structs.Size](/api/class/structs-size) {#gamesize-phaserstructssize}


**说明:**

游戏大小组件 。

未修改的游戏大小, 如游戏配置( 原始宽度 / 高度) 中要求的, 如用于世界界限, 相机等


> 源码：[src/scale/ScaleManager.js#L194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L194)  
引入版本：3.16.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

游戏高度.

这通常是游戏配置中给出的大小.


> 源码：[src/scale/ScaleManager.js#L1816](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1816)  
引入版本：3.16.0


---

### isFullscreen {#isFullscreen}

#### isFullscreen: boolean {#isfullscreen-boolean}


**说明:**

浏览器目前是否处于全屏模式?


> 源码：[src/scale/ScaleManager.js#L1780](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1780)  
引入版本：3.16.0


---

### isGameLandscape {#isGameLandscape}

#### isGameLandscape: boolean {#isgamelandscape-boolean}


**说明:**

游戏维度景观是怎样的? (即比高大)

这与设备本身处于景观导向不同.


> 源码：[src/scale/ScaleManager.js#L1890](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1890)  
引入版本：3.16.0


---

### isGamePortrait {#isGamePortrait}

#### isGamePortrait: boolean {#isgameportrait-boolean}


**说明:**

游戏维度肖像是怎样的? (即比宽度高)

这和装置本身在肖像导向上不同.


> 源码：[src/scale/ScaleManager.js#L1871](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1871)  
引入版本：3.16.0


---

### isLandscape {#isLandscape}

#### isLandscape: boolean {#islandscape-boolean}


**说明:**

设备是否为定向 API 所报告地貌导向? 通常这个值只能存在于移动设备上 。


> 源码：[src/scale/ScaleManager.js#L1853](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1853)  
引入版本：3.16.0


---

### isPortrait {#isPortrait}

#### isPortrait: boolean {#isportrait-boolean}


**说明:**

设备是否像 API 所报告的那样处于肖像方向? 这个值通常只在移动设备上可用 。


> 源码：[src/scale/ScaleManager.js#L1835](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1835)  
引入版本：3.16.0


---

### orientation {#orientation}

#### orientation: [Phaser.Scale.OrientationType](/api/typedef/scale#orientationtype) {#orientation-phaserscaleorientationtype}


**说明:**

当前设备方向.

定向事件通过设备定向API发送,一般只在移动浏览器上发送.


> 源码：[src/scale/ScaleManager.js#L301](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L301)  
引入版本：3.16.0


---

### parent {#parent}

#### parent: any {#parent-any}


**说明:**

Canvas 的母对象。 通常是一个 div, 或者浏览器窗口, 或者在非浏览器环境中没有 。

此设定在 Game Config 中为 `parent` 属性。 如果未定义( 或者只是不在场) , 则默认使用文档正文。 如果指定为 `null` Phaser , 则忽略所有父操作 。


> 源码：[src/scale/ScaleManager.js#L164](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L164)  
引入版本：3.16.0


---

### parentIsWindow {#parentIsWindow}

#### parentIsWindow: boolean {#parentiswindow-boolean}


**说明:**

母元素是浏览器窗口吗 ?


> 源码：[src/scale/ScaleManager.js#L176](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L176)  
引入版本：3.16.0


---

### parentSize {#parentSize}

#### parentSize: [Phaser.Structs.Size](/api/class/structs-size) {#parentsize-phaserstructssize}


**说明:**

父大小组件 。


> 源码：[src/scale/ScaleManager.js#L185](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L185)  
引入版本：3.16.0


---

### resizeInterval {#resizeInterval}

#### resizeInterval: number {#resizeinterval-number}


**说明:**

在检查浏览器大小是否改变之前, 需要耗时多少毫秒 ?

大多数现代浏览器都会发送一个“ 大小调整” 事件, 缩放管理器会听。 然而, 旧浏览器没有做到这一点, 或者无法一致地这样做, 所以我们会回到一个基于时间间隔的更传统的“ 大小检查 ” 。 您可以控制它在这里检查的频率 。


> 源码：[src/scale/ScaleManager.js#L350](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L350)  
引入版本：3.16.0


---

### scaleMode {#scaleMode}

#### scaleMode: [Phaser.Scale.ScaleModeType](/api/typedef/scale#scalemodetype) {#scalemode-phaserscalescalemodetype}


**说明:**

游戏比例模式.


> 源码：[src/scale/ScaleManager.js#L229](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L229)  
引入版本：3.16.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

游戏宽度.

这通常是游戏配置中给出的大小.


> 源码：[src/scale/ScaleManager.js#L1797](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1797)  
引入版本：3.16.0


---

### zoom {#zoom}

#### zoom: number {#zoom-number}


**说明:**

游戏放大系数.

此值允许您用给定的缩放系数乘以游戏基数。 然后在计算显示大小时使用, 即使在 `NONE` 情况下也是如此。 如果您根本不想要 Phaser 触摸画布样式, 此值应该是 1 。

也可以设定为 `MAX_ZOOM`,在这种情况下,会根据游戏大小和父公司内部可用的空间来得出缩放值.


> 源码：[src/scale/ScaleManager.js#L238](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L238)  
引入版本：3.16.0


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

### boot {#boot}

#### \<instance> boot() {#instance-boot}


**说明:**

靴子手柄在开始时由Phaser.Game调用,渲染器现在已经可用,帆布已经添加到DOM中.


**Access:** 保护


**Fires:** [Phaser.Scale.Events#event:RESIZE](/api/event/scale-events#resize)


> 源码：[src/scale/ScaleManager.js#L418](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L418)  
引入版本：3.16.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此缩放管理器, 释放所有外部资源的引用。 一旦销毁, 缩放管理器将无法再次使用 。


**Overrides:** Phaser.Events.EventEmitter#销毁


> 源码：[src/scale/ScaleManager.js#L1755](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1755)  
引入版本：3.16.0


---

### getFullscreenTarget {#getFullscreenTarget}

#### \<instance> getFullscreenTarget() {#instance-getfullscreentarget}


**说明:**

一种内部方法,它获得进入全屏模式时使用的目标元素.


**返回值:** object - 满屏目标元素.


> 源码：[src/scale/ScaleManager.js#L1387](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1387)  
引入版本：3.16.0


---

### getMaxZoom {#getMaxZoom}

#### \<instance> getMaxZoom() {#instance-getmaxzoom}


**说明:**

根据当前父大小和游戏大小计算并返回最大可能的缩放系数。如果父大小没有尺寸(即未命名的div),或小于未分区的游戏,则此值将返回1(未缩放)


**返回值:** number - 最大可能的缩放系数。 至少这个值至少是 1 。


> 源码：[src/scale/ScaleManager.js#L1174](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1174)  
引入版本：3.16.0


---

### getParent {#getParent}

#### \<instance> getParent(config) {#instance-getparentconfig}


**说明:**

根据游戏配置确定游戏画布的母元素(如果有的话).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Core.GameConfig](/api/typedef/types-core#gameconfig) | 否 | 游戏配置对象 。 |


> 源码：[src/scale/ScaleManager.js#L599](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L599)  
引入版本：3.16.0


---

### getParentBounds {#getParentBounds}

#### \<instance> getParentBounds() {#instance-getparentbounds}


**说明:**

计算父边界的大小并更新 `parentSize` 属性,但画布必须具有 dom 父属性。


**返回值:** boolean - `true`如果母边界已经改变大小或位置,否则`false`.


> 源码：[src/scale/ScaleManager.js#L649](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L649)  
引入版本：3.16.0


---

### getViewPort {#getViewPort}

#### \<instance> getViewPort([camera], [out]) {#instance-getviewportcamera-out}


**说明:**

计算并返回一个矩形,代表游戏画布目前可见的区域,计算画布位置、父边框和显示尺度。如果画布延伸到父边框可见区域之外,则矩形会相应被剪切。

可提供可选相机,在这种情况下,对返回的矩形作进一步调整,以计入相机的缩放级别和滚动位置.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用于计算视图的相机。如果提供了,则对矩形进行相机缩放和滚动调整。 |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 保留结果的可选矩形。如果不提供,则创建新的矩形。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 可见区域的矩形.


> 源码：[src/scale/ScaleManager.js#L1618](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1618)  
引入版本：3.60.0


---

### leaveFullScreenSuccessHandler {#leaveFullScreenSuccessHandler}

#### \<instance> leaveFullScreenSuccessHandler() {#instance-leavefullscreensuccesshandler}


**说明:**

浏览器已成功离开全屏模式.


**Fires:** [Phaser.Scale.Events#event:LEAVE_FULLSCREEN](/api/event/scale-events#leave_fullscreen)


> 源码：[src/scale/ScaleManager.js#L1472](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1472)  
引入版本：3.85.0


---

### lockOrientation {#lockOrientation}

#### \<instance> lockOrientation(orientation) {#instance-lockorientationorientation}


**说明:**

尝试使用屏幕方向 API 锁定网页浏览器的方向 。

此API只可在现代移动浏览器上获取。 详情请参见 [https://developer.mozilla.org/en-US/docs/Web/API/Screen/lockOrientation](https://developer.mozilla.org/en-US/docs/Web/API/Screen/lockOrientation) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| orientation | string | 否 | 您想要锁定浏览器的定向 。 应该是 API 字符串, 如“ 景观 ” 、 “ 景观主线 ” 、 “ 图片 ” 等 。 |


**返回值:** boolean - 如果方向被成功锁定,则使用`true`,否则使用`false`.


> 源码：[src/scale/ScaleManager.js#L704](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L704)  
引入版本：3.16.0


---

### onFullScreenChange {#onFullScreenChange}

#### \<instance> onFullScreenChange() {#instance-onfullscreenchange}


**说明:**

当DOM发送全屏更改事件时触发.


**Access:** 保护


> 源码：[src/scale/ScaleManager.js#L1586](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1586)  
引入版本：3.16.0


---

### onFullScreenError {#onFullScreenError}

#### \<instance> onFullScreenError() {#instance-onfullscreenerror}


**说明:**

当DOM发送全屏事件时触发.


> 源码：[src/scale/ScaleManager.js#L1607](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1607)  
引入版本：3.16.0


---

### parseConfig {#parseConfig}

#### \<instance> parseConfig(config) {#instance-parseconfigconfig}


**说明:**

解析游戏配置以设置缩放默认值。


**Access:** 保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Core.GameConfig](/api/typedef/types-core#gameconfig) | 否 | 游戏配置对象 。 |


> 源码：[src/scale/ScaleManager.js#L466](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L466)  
引入版本：3.16.0


---

### preBoot {#preBoot}

#### \<instance> preBoot() {#instance-preboot}


**说明:**

调用 _ 在_ 画布对象创建并添加到 DOM 中 。


**Access:** 保护


> 源码：[src/scale/ScaleManager.js#L402](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L402)  
引入版本：3.16.0


---

### refresh {#refresh}

#### \<instance> refresh([previousWidth], [previousHeight]) {#instance-refreshpreviouswidth-previousheight}


**说明:**

刷新内部缩放值、 边框大小和方向检查。

完成后, 将更改大小的事件发送到 。

浏览器窗口大小变化时, 缩放管理器会自动调用此功能, 只要它使用“ NONE” 以外的缩放模式即可 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| previousWidth | number | 是 | 游戏的上一个宽度。 只有在 gameSize 更改时才设定 。 |
| previousHeight | number | 是 | 游戏的上一个高度。 只有在 gameSize 更改时才设定 。 |


**返回值:** [Phaser.Scale.ScaleManager](/api/class/scale-scalemanager) - 缩放管理器实例 。


**Fires:** [Phaser.Scale.Events#event:RESIZE](/api/event/scale-events#resize)


> 源码：[src/scale/ScaleManager.js#L950](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L950)  
引入版本：3.16.0


---

### removeFullscreenTarget {#removeFullscreenTarget}

#### \<instance> removeFullscreenTarget() {#instance-removefullscreentarget}


**说明:**

删除添加到 DOM 的全屏目标。


> 源码：[src/scale/ScaleManager.js#L1423](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1423)  
引入版本：3.17.0


---

### resize {#resize}

#### \<instance> resize(width, height) {#instance-resizewidth-height}


**说明:**

调用此功能可以直接修改 Phaser 帆布元素的大小。 您只使用 `NONE` 缩放模式, 它可以完全更新所有内部组件 。

如果你只想改变父母的大小,请参见`setParentSize`方法.

如果想要改变游戏的基数大小,但仍由缩放管理器管理所有缩放(即你**不是**使用`NONE`),那么请参见`setGameSize`方法.

这种方法将把 `gameSize`、 `baseSize` 和 `displaySize` 组件设置到给定的维度。 然后, 它通过直接设置属性来将画布宽度和高度调整到给定的值。 最后, 如果您已经将缩放管理器缩放到除 1 (默认) 以外的任何值, 它会设置画布 CSS 宽度和高度, 以给定的大小乘以缩放系数( 画布像素大小未受影响 ) 。

如果您启用了 `autoCenter`, 则它会传递到 `updateCenter` 方法, 并设置边距, 允许仅基于其母元素来将画布中心化 。 最后, `displayScale` 将调整, 并发送 RESIZE 事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 游戏的新宽度. |
| height | number | 否 | 游戏的新高度. |


**返回值:** [Phaser.Scale.ScaleManager](/api/class/scale-scalemanager) - 缩放管理器实例 。


**Fires:** [Phaser.Scale.Events#event:RESIZE](/api/event/scale-events#resize)


> 源码：[src/scale/ScaleManager.js#L802](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L802)  
引入版本：3.16.0


---

### setGameSize {#setGameSize}

#### \<instance> setGameSize(width, height) {#instance-setgamesizewidth-height}


**说明:**

这种方法将为您的游戏设定新的大小 。

它只应用于您想要改变游戏的基数大小,并且正在使用一个缩放管理器缩放模式,即`FIT`. 如果您使用`NONE`并想要直接改变游戏和画布大小,那么请使用`resize`方法代替.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 游戏的新宽度. |
| height | number | 否 | 游戏的新高度. |


**返回值:** [Phaser.Scale.ScaleManager](/api/class/scale-scalemanager) - 缩放管理器实例 。


**Fires:** [Phaser.Scale.Events#event:RESIZE](/api/event/scale-events#resize)


> 源码：[src/scale/ScaleManager.js#L751](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L751)  
引入版本：3.16.0


---

### setMaxZoom {#setMaxZoom}

#### \<instance> setMaxZoom() {#instance-setmaxzoom}


**说明:**

根据 _current_父大小设置缩放为最大可能 。


**返回值:** [Phaser.Scale.ScaleManager](/api/class/scale-scalemanager) - 缩放管理器实例 。


**Fires:** [Phaser.Scale.Events#event:RESIZE](/api/event/scale-events#resize)


> 源码：[src/scale/ScaleManager.js#L903](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L903)  
引入版本：3.16.0


---

### setParentSize {#setParentSize}

#### \<instance> setParentSize(width, height) {#instance-setparentsizewidth-height}


**说明:**

这种方法将设定用于缩放和中心计算中的父大小组件。 如果您在游戏配置中明确禁用父大小, 但仍希望利用其他缩放管理器特性, 您只需调用此方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 父的新的宽度 。 |
| height | number | 否 | 父母新高之势. |


**返回值:** [Phaser.Scale.ScaleManager](/api/class/scale-scalemanager) - 缩放管理器实例 。


**Fires:** [Phaser.Scale.Events#event:RESIZE](/api/event/scale-events#resize)


> 源码：[src/scale/ScaleManager.js#L729](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L729)  
引入版本：3.16.0


---

### setSnap {#setSnap}

#### \<instance> setSnap([snapWidth], [snapHeight]) {#instance-setsnapsnapwidth-snapheight}


**说明:**

通过设置Snap值,当浏览器大小被修改时,其尺寸会自动被折断到最近的网格切片,使用地板。例如,如果您有16的Snap值,宽度会变为68,那么它会被折断到64(下层时16的倍数)

这个模式最好使用`FIT`比例模式.

使用此方法不设参数来重设坐标值 。

使用这种方法自动引用 `ScaleManager.refresh` , 从而发出 `RESIZE` 事件 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| snapWidth | number | 是 | 0 | 宽度的大小。 如果您不想宽度的大小, 则通过 0 值 。 |
| snapHeight | number | 是 | "snapWidth" | 将高度调高到的数值。 如果不提供, 它将使用 `snapWidth` 值。 如果您不想调高, 请通过 0 值 。 |


**返回值:** [Phaser.Scale.ScaleManager](/api/class/scale-scalemanager) - 缩放管理器实例 。


**Fires:** [Phaser.Scale.Events#event:RESIZE](/api/event/scale-events#resize)


> 源码：[src/scale/ScaleManager.js#L920](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L920)  
引入版本：3.80.0


---

### setZoom {#setZoom}

#### \<instance> setZoom(value) {#instance-setzoomvalue}


**说明:**

设置缩放管理器的缩放值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 游戏的新缩放值 。 |


**返回值:** [Phaser.Scale.ScaleManager](/api/class/scale-scalemanager) - 缩放管理器实例 。


**Fires:** [Phaser.Scale.Events#event:RESIZE](/api/event/scale-events#resize)


> 源码：[src/scale/ScaleManager.js#L884](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L884)  
引入版本：3.16.0


---

### startFullscreen {#startFullscreen}

#### \<instance> startFullscreen([fullscreenOptions]) {#instance-startfullscreenfullscreenoptions}


**说明:**

向浏览器发送请求,要求其进入全屏模式,使用QQlink [https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API) Fullscreen API}.

如果浏览器不支持此选项, 将会发布 `FULLSCREEN_UNSUPPORTED` 事件 。

此方法_ must_ 是从 `pointerup`用户输入手势调用( ** 不** `pointerdown`) 。 没有此功能, 您无法启动游戏全屏, 因为大多数浏览器会屏蔽它 。 iframe 内的游戏也会被屏蔽在全屏中, 除非 if it frame 拥有 `allowfullscreen` 属性 。

触摸装置,如Android和 iOS 萨法里,你应该总是用 `pointerup` 和不为 `pointerdown`,否则请求将失败,除非嵌入游戏的文档已经收到某种形式的触摸输入,而您无法保证。激活全屏通过 `pointerup` 绕过这个问题。

执行一个可导航到另一页的动作,或者打开另一个标签,将会自动取消全屏模式,用户也会按 ESC 键。要直接从游戏中取消全屏模式,即点击图标,调用 `stopFullscreen` 方法。

浏览器只能将一个 DOM 元素发送到全屏。 您可以通过设置游戏配置中的 `fullscreenTarget` 属性来控制哪个元素, 或者更改缩放管理器中的属性 。 请注意, 游戏画布_ must_ 是目标的孩子 。 如果您不给出目标, Phaser 将会自动创建空白的 `<div>` 元素, 并将画布移动到其中, 然后再进行全屏。 当它离开全屏时, divi将被移除 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| fullscreenOptions | object | 是 | Fullscreen Options字典用于在进入全屏幕时提供配置选项. |


**Fires:** [Phaser.Scale.Events#event:ENTER_FULLSCREEN](/api/event/scale-events#enter_fullscreen), [Phaser.Scale.Events#event:FULLSCREEN_FAILED](/api/event/scale-events#fullscreen_failed), [Phaser.Scale.Events#event:FULLSCREEN_UNSUPPORTED](/api/event/scale-events#fullscreen_unsupported), [Phaser.Scale.Events#event:RESIZE](/api/event/scale-events#resize)


> 源码：[src/scale/ScaleManager.js#L1290](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1290)  
引入版本：3.16.0


---

### startListeners {#startListeners}

#### \<instance> startListeners() {#instance-startlisteners}


**说明:**

启动不同 DOM 事件听众运行的内部方法 。


> 源码：[src/scale/ScaleManager.js#L1520](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1520)  
引入版本：3.16.0


---

### step {#step}

#### \<instance> step(time, delta) {#instance-steptime-delta}


**说明:**

内部方法, 由游戏步骤自动调用 。 监视已过期的时间并调整间隔大小, 以查看是否需要进行父边界检查 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 最新游戏步骤的时间值。 通常为高分辨率定时器值, 或 Date. now () 。 |
| delta | number | 否 | 自上一个框架以来的三角洲值。 这是为避免三角洲的悬崖被 TimeStep 级所覆盖而平滑的 。 |


> 源码：[src/scale/ScaleManager.js#L1689](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1689)  
引入版本：3.16.0


---

### stopFullscreen {#stopFullscreen}

#### \<instance> stopFullscreen() {#instance-stopfullscreen}


**说明:**

如果浏览器已输入, 调用此方法将取消全屏模式 。


**Fires:** [Phaser.Scale.Events#event:FULLSCREEN_UNSUPPORTED](/api/event/scale-events#fullscreen_unsupported)


> 源码：[src/scale/ScaleManager.js#L1446](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1446)  
引入版本：3.16.0


---

### stopListeners {#stopListeners}

#### \<instance> stopListeners() {#instance-stoplisteners}


**说明:**

停止所有 DOM 事件听众 。


> 源码：[src/scale/ScaleManager.js#L1721](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1721)  
引入版本：3.16.0


---

### toggleFullscreen {#toggleFullscreen}

#### \<instance> toggleFullscreen([fullscreenOptions]) {#instance-togglefullscreenfullscreenoptions}


**说明:**

切换全屏模式。 如果已经进入全屏, 调用此模式将取消它。 如果不进入全屏, 这将要求浏览器进入全屏模式 。

如果浏览器不支持此选项, 将会发布 `FULLSCREEN_UNSUPPORTED` 事件 。

此方法_ must_ 是从 `pointerup`用户输入手势调用( ** 不** `pointerdown`) 。 没有此功能, 您无法启动游戏全屏, 因为大多数浏览器会屏蔽它 。 iframe 内的游戏也会被屏蔽在全屏中, 除非 if it frame 拥有 `allowfullscreen` 属性 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| fullscreenOptions | object | 是 | Fullscreen Options字典用于在进入全屏幕时提供配置选项. |


**Fires:** [Phaser.Scale.Events#event:ENTER_FULLSCREEN](/api/event/scale-events#enter_fullscreen), [Phaser.Scale.Events#event:LEAVE_FULLSCREEN](/api/event/scale-events#leave_fullscreen), [Phaser.Scale.Events#event:FULLSCREEN_UNSUPPORTED](/api/event/scale-events#fullscreen_unsupported), [Phaser.Scale.Events#event:RESIZE](/api/event/scale-events#resize)


> 源码：[src/scale/ScaleManager.js#L1489](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1489)  
引入版本：3.16.0


---

### transformX {#transformX}

#### \<instance> transformX(pageX) {#instance-transformxpagex}


**说明:**

将 pageX 值转换为缩放的 Scrowd 管理器坐标空间 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pageX | number | 否 | DOM的pageX值。 |


**返回值:** number - 译值.


> 源码：[src/scale/ScaleManager.js#L1260](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1260)  
引入版本：3.16.0


---

### transformY {#transformY}

#### \<instance> transformY(pageY) {#instance-transformypagey}


**说明:**

将 pageY 值转换为缩放的 Scrowd 管理器坐标空间 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pageY | number | 否 | DOM的pageY值。 |


**返回值:** number - 译值.


> 源码：[src/scale/ScaleManager.js#L1275](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1275)  
引入版本：3.16.0


---

### updateBounds {#updateBounds}

#### \<instance> updateBounds() {#instance-updatebounds}


**说明:**

更新 `canvasBounds`矩形,以匹配用于跟踪输入事件的画布元素的边框客户端矩形.


> 源码：[src/scale/ScaleManager.js#L1242](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1242)  
引入版本：3.16.0


---

### updateCenter {#updateCenter}

#### \<instance> updateCenter() {#instance-updatecenter}


**说明:**

计算并更新画布 CSS 样式, 以将其置于父目录之内。 如果您在游戏配置中明确设置了父目录为 `null`, 那么这种方法可能会产生不正确的结果, 除非您先调用 `setParentSize` 方法 。

它通过修改画布CSS `marginLeft`和`marginTop`属性来工作.

如果它们已经被您自己的样式表或代码设置, 则它们将被覆盖 。

为防止缩放管理器将画布居中,要么在游戏配置中不设置 `autoCenter` 属性,要么确保设置为 `NO_CENTER` 。


> 源码：[src/scale/ScaleManager.js#L1192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1192)  
引入版本：3.16.0


---

### updateOrientation {#updateOrientation}

#### \<instance> updateOrientation() {#instance-updateorientation}


**说明:**

内部方法,检查当前屏幕方向,只有在内部检查旗设定的情况下.

如果方向改变,则更新方向属性,然后发送方向改变事件.


**Fires:** [Phaser.Scale.Events#event:ORIENTATION_CHANGE](/api/event/scale-events#orientation_change)


> 源码：[src/scale/ScaleManager.js#L998](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L998)  
引入版本：3.16.0


---

### updateScale {#updateScale}

#### \<instance> updateScale() {#instance-updatescale}


**说明:**

内部方法,管理基于比例模式的大小组件更新.


> 源码：[src/scale/ScaleManager.js#L1024](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/ScaleManager.js#L1024)  
引入版本：3.16.0


---

---
