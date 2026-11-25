# Pointer {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/input-pointer)

一个指针对象将鼠标和触摸输入都封装在Phaser中.

默认情况下, Phaser 会为您的游戏创建2个指针。 如果您需要更多指针, 即多触摸游戏, 那么使用 `InputPlugin.addPointer` 方法来完成, 而不是直接即时切换这个类, 否则它不会被输入系统管理 。

您可以通过 `InputPlugin.activePointer` 引用当前活动的指针。 您也可以使用属性 `InputPlugin.pointer1` 通到 `pointer10`, 用于您在游戏中启用的每个指针 。

此对象的属性由输入插件在处理过程中设置。 然后,该对象会被发送到输入插件所发出的所有输入相关事件, 这样您就可以直接在调用回话中引用它属性 。

**构造函数**

`new Pointer(manager, id)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Input.InputManager](/api/class/input-inputmanager) | 否 | 输入管理器的参考文献 。 |
| id | number | 否 | 指针的内部身份 |

---


**作用域**: static

> 源码：[src/input/Pointer.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L15)  
引入版本：3.0.0

## 公开成员 {#public-members}

### active {#active}

#### active: boolean {#active-boolean}


**说明:**

活动指针是当前按下显示的指针。 鼠标总是被视为活动 。


> 源码：[src/input/Pointer.js#L440](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L440)  
引入版本：3.10.0


---

### angle {#angle}

#### angle: number {#angle-number}


**说明:**

指针的当前角度正在移动,以弧度表示,基于其先前和当前位置.

角度是基于面对当前位置的旧位置.

指针移动时都会更新此属性, 不论按钮状态如何。 换句话说, 它仅根据移动而改变 — 按钮不必先按 。


> 源码：[src/input/Pointer.js#L194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L194)  
引入版本：3.16.0


---

### button {#button}

#### button: number {#button-number}


**说明:**

仅读属性, 表示最近事件时在指针上按下或放出哪个按钮。 它只在 `up`和 `down`事件期间设置 。

在触摸设备上,值总是0.

用户可能会改变其指点设备上的按钮配置,这样如果事件按钮属性为零,它可能不是由物理上左的按钮造成的,最大部分是指点设备上的按钮;然而,它应该表现得像左键在标准按钮布局中被点击一样.


> 源码：[src/input/Pointer.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L107)  
引入版本：3.18.0


---

### buttons {#buttons}

#### buttons: number {#buttons-number}


**说明:**

一个位图,代表当前鼠标的按钮被按住。 可能的值是 :

0:没有按钮或未初始化的 1:左键2:右键 4:轮键或中键 8:第四键(一般为"浏览器后退"按钮) 16:第五键(一般为"阅读器前退"按钮) 4:

对于用于左手使用的鼠标,按钮动作会被反转。在这种情况下,数值从右到左读。


> 源码：[src/input/Pointer.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L125)  
引入版本：3.0.0


---

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#camera-phasercamerasscene2dcamera}


**说明:**

指针在上次更新时与之交互的相机.

指针只能一次与一台相机进行交互,如果多台相机被定位在对方的顶部,这台相机将成为列表中最高的相机.


> 源码：[src/input/Pointer.js#L94](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L94)  
引入版本：3.0.0


---

### deltaX {#deltaX}

#### deltaX: number {#deltax-number}


**说明:**

由用户移动鼠标轮或类似输入设备而发生的水平滚动量.


> 源码：[src/input/Pointer.js#L466](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L466)  
引入版本：3.18.0


---

### deltaY {#deltaY}

#### deltaY: number {#deltay-number}


**说明:**

由用户移动鼠标轮盘或类似输入设备产生的垂直滚动量。 如果用户向上滚动, 则该数值通常小于 0, 向下滚动时大于 0 。


> 源码：[src/input/Pointer.js#L476](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L476)  
引入版本：3.18.0


---

### deltaZ {#deltaZ}

#### deltaZ: number {#deltaz-number}


**说明:**

由用户移动鼠标轮或类似输入设备而发生的z轴滚动量.


> 源码：[src/input/Pointer.js#L487](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L487)  
引入版本：3.18.0


---

### distance {#distance}

#### distance: number {#distance-number}


**说明:**

指针移动的距离,基于其先前和现在的位置.

根据 `motionFactor` 属性,此值会平滑出每个框架 。

指针移动时都会更新此属性, 不论按钮状态如何。 换句话说, 它仅根据移动而改变 — 按钮不必先按 。

如果需要主按钮按下后所行走的总距离,则使用`Pointer.getDistance`方法.


> 源码：[src/input/Pointer.js#L209](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L209)  
引入版本：3.16.0


---

### downElement {#downElement}

#### downElement: any {#downelement-any}


**说明:**

指针被按下, 从 DOM 事件中取出。 默认设置中, 将使用 Phaser 渲染的 Canvas 或 Window 元素 。


> 源码：[src/input/Pointer.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L72)  
引入版本：3.16.0


---

### downTime {#downTime}

#### downTime: number {#downtime-number}


**说明:**

按下第一个按钮时的事件时间戳, 或触摸输入。 用于拖动对象 。


> 源码：[src/input/Pointer.js#L319](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L319)  
引入版本：3.0.0


---

### downX {#downX}

#### downX: number {#downx-number}


**说明:**

按钮 1(左键) 时的 X 坐标指针,或触摸,按下,用于拖动对象.


> 源码：[src/input/Pointer.js#L299](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L299)  
引入版本：3.0.0


---

### downY {#downY}

#### downY: number {#downy-number}


**说明:**

Y 指针坐标,当按下按钮 1(左键),或触摸,用于拖曳对象时。


> 源码：[src/input/Pointer.js#L309](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L309)  
引入版本：3.0.0


---

### event {#event}

#### event: TouchEvent, MouseEvent, WheelEvent {#event-touchevent-mouseevent-wheelevent}


**说明:**

最新一次本地的DOM事件,这个指针已经处理。


> 源码：[src/input/Pointer.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L63)  
引入版本：3.0.0


---

### id {#id}

#### id: number {#id-number}


**说明:**

指针的内部身份


> 源码：[src/input/Pointer.js#L53](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L53)  
引入版本：3.0.0


---

### identifier {#identifier}

#### identifier: number {#identifier-number}


**说明:**

此指针启动时 DOM 事件设定的指针标识属性 。


> 源码：[src/input/Pointer.js#L421](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L421)  
引入版本：3.10.0


---

### isDown {#isDown}

#### isDown: boolean {#isdown-boolean}


**说明:**

此指针上的 __按钮是否被认为是下方 ?


> 源码：[src/input/Pointer.js#L369](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L369)  
引入版本：3.0.0


---

### locked {#locked}

#### locked: boolean {#locked-boolean}


**说明:**

指针锁定了吗?

只有鼠标指针可以被锁定,并且只有在通过浏览器Pointer Lock API请求时才会被锁定.

您可以通过调用 `pointerdown` 或 `pointerup` 事件处理器的 `this.input.mouse.requestPointerLock()` 方法来请求此请求 。


> 源码：[src/input/Pointer.js#L450](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L450)  
引入版本：3.19.0


---

### manager {#manager}

#### manager: [Phaser.Input.InputManager](/api/class/input-inputmanager) {#manager-phaserinputinputmanager}


**说明:**

输入管理器的参考文献 。


> 源码：[src/input/Pointer.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L44)  
引入版本：3.0.0


---

### motionFactor {#motionFactor}

#### motionFactor: number {#motionfactor-number}


**说明:**

适用于每个帧平滑运动的因子.

此值被传递到用于计算指针速度、角度和距离的平滑步内插。 它被应用到每个帧,直到midPoint到达指针的当前位置。 0.2 提供了良好的平均值,但如果您需要更快的更新, 并且正在高性能环境中工作, 则可以增加。 永远不要将这个值设置为零 。


> 源码：[src/input/Pointer.js#L247](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L247)  
引入版本：3.16.0


---

### movementX {#movementX}

#### movementX: number {#movementx-number}


**说明:**

如果鼠标被锁定,则指针自上个帧以来在像素中的横向相对运动.


> 源码：[src/input/Pointer.js#L401](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L401)  
引入版本：3.0.0


---

### movementY {#movementY}

#### movementY: number {#movementy-number}


**说明:**

如果鼠标被锁定,则指针自上个帧以来在像素中的垂直相对运动.


> 源码：[src/input/Pointer.js#L411](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L411)  
引入版本：3.0.0


---

### moveTime {#moveTime}

#### moveTime: number {#movetime-number}


**说明:**

最近一次移动这个指针的时间( 不论按钮的状态, 如果有的话) 。


> 源码：[src/input/Pointer.js#L289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L289)  
引入版本：3.0.0


---

### pointerId {#pointerId}

#### pointerId: number {#pointerid-number}


**说明:**

此指针启动时, DOM 事件设定的指针属性 pointerId 。 浏览器可以并且将会循环该值 。


> 源码：[src/input/Pointer.js#L430](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L430)  
引入版本：3.10.0


---

### position {#position}

#### position: [Phaser.Math.Vector2](/api/class/math-vector2) {#position-phasermathvector2}


**说明:**

指针在屏幕空间的位置 。


> 源码：[src/input/Pointer.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L145)  
引入版本：3.0.0


---

### prevPosition {#prevPosition}

#### prevPosition: [Phaser.Math.Vector2](/api/class/math-vector2) {#prevposition-phasermathvector2}


**说明:**

指针在屏幕空间的上一个位置 。

输入管理器中存储了旧的x和y值. transformPointer呼叫中.

使用属性 `velocity`, `angle`和 `distance` 创建自己的手势识别.


> 源码：[src/input/Pointer.js#L155](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L155)  
引入版本：3.11.0


---

### primaryDown {#primaryDown}

#### primaryDown: boolean {#primarydown-boolean}


**说明:**

主按钮下调了吗? (通常是按钮 0,鼠标左键)


> 源码：[src/input/Pointer.js#L359](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L359)  
引入版本：3.0.0


---

### smoothFactor {#smoothFactor}

#### smoothFactor: number {#smoothfactor-number}


**说明:**

适用于指针位置的平滑因子.

由于其性质,指针位置本身就很吵。虽然这对很多游戏来说是好的,但如果需要更清洁的位置,那么您可以设置这个值,对记录的位置自动应用平滑。

0的默认值表示“ 不平滑 ” 。 设置到一个小值, 如 0.2, 以便在位置之间应用平均平滑水平。 您可以直接更改这个值, 或者在 Game Config 中设置 `input.smoothFactor` 属性 。

位置只有在指针移动时才平滑。如果这个指针上的主按钮进入上下状态,则位置总是精确的,而不是平滑的。


> 源码：[src/input/Pointer.js#L227](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L227)  
引入版本：3.16.0


---

### time {#time}

#### time: number {#time-number}


**说明:**

最近一次通过 DOM 事件更新此指针的时间。 直接来自 `event.timeStamp` 属性。 如果尚未发生任何事件, 则返回零 。


> 源码：[src/input/Pointer.js#L1306](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L1306)  
引入版本：3.16.0


---

### upElement {#upElement}

#### upElement: any {#upelement-any}


**说明:**

指针的 DOM 元素从 DOM 事件上释放, 取自 DOM 事件。 默认设置中, 这将包含 Phaser 正在渲染的 Canvas , 或窗口元素 。


> 源码：[src/input/Pointer.js#L83](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L83)  
引入版本：3.16.0


---

### upTime {#upTime}

#### upTime: number {#uptime-number}


**说明:**

最终按钮或触摸输入时的事件时间戳。 用于拖动对象 。


> 源码：[src/input/Pointer.js#L349](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L349)  
引入版本：3.0.0


---

### upX {#upX}

#### upX: number {#upx-number}


**说明:**

当按钮1(左键),或Touch,被释放时,指针的X坐标,用于拖曳对象.


> 源码：[src/input/Pointer.js#L329](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L329)  
引入版本：3.0.0


---

### upY {#upY}

#### upY: number {#upy-number}


**说明:**

Y 指针坐标当按钮 1( 左键) 时, 或 Touch , 释放出来, 用于拖动对象 。


> 源码：[src/input/Pointer.js#L339](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L339)  
引入版本：3.0.0


---

### velocity {#velocity}

#### velocity: [Phaser.Math.Vector2](/api/class/math-vector2) {#velocity-phasermathvector2}


**说明:**

指针目前的速度,基于其当前和以往的位置.

根据 `motionFactor` 属性,此值会平滑出每个框架 。

指针移动时都会更新此属性, 不论按钮状态如何。 换句话说, 它仅根据移动而改变 — 按钮不必先按 。


> 源码：[src/input/Pointer.js#L179](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L179)  
引入版本：3.16.0


---

### wasCanceled {#wasCanceled}

#### wasCanceled: boolean {#wascanceled-boolean}


**说明:**

这个指针被触摸取消了吗?

注:"canceled"是"canceled"的美英拼写,请不要提交PRs更正!


> 源码：[src/input/Pointer.js#L389](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L389)  
引入版本：3.15.0


---

### wasTouch {#wasTouch}

#### wasTouch: boolean {#wastouch-boolean}


**说明:**

上次输入事件来自触摸输入( true) 还是鼠标 ? (假)


> 源码：[src/input/Pointer.js#L379](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L379)  
引入版本：3.0.0


---

### worldX {#worldX}

#### worldX: number {#worldx-number}


**说明:**

这个指针的x位置,被翻译为它与之相互作用的最新相机的坐标空间.

如果您想使用输入事件处理器的这个值_ 外部_, 您应该先使用 `Pointer.updateWorldPoint` 方法更新它 。


> 源码：[src/input/Pointer.js#L263](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L263)  
引入版本：3.10.0


---

### worldY {#worldY}

#### worldY: number {#worldy-number}


**说明:**

这个指针的y位置, 翻译为它与之交互的最近相机的坐标空间 。

如果您想使用输入事件处理器的这个值_ 外部_, 您应该先使用 `Pointer.updateWorldPoint` 方法更新它 。


> 源码：[src/input/Pointer.js#L276](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L276)  
引入版本：3.10.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

此指针的 x 位置。 值位于屏幕空间。 请参见 `worldX` 以获得相机转换位置 。


> 源码：[src/input/Pointer.js#L1260](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L1260)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

此指针的y位置。 值位于屏幕空间。 请参见 `worldY` 以获得相机转换位置 。


> 源码：[src/input/Pointer.js#L1283](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L1283)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### backButtonDown {#backButtonDown}

#### \<instance> backButtonDown() {#instance-backbuttondown}


**说明:**

检查是否在此指针上按住后键 。


**返回值:** boolean - 如果后扣被扣住,则使用`true`.


> 源码：[src/input/Pointer.js#L932](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L932)  
引入版本：3.0.0


---

### backButtonReleased {#backButtonReleased}

#### \<instance> backButtonReleased() {#instance-backbuttonreleased}


**说明:**

检查是否打开后键是此指针上最近的活动 。


**返回值:** boolean - `true` 如果释放后键是这个指针上最新的活动.


> 源码：[src/input/Pointer.js#L997](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L997)  
引入版本：3.18.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此指针实例并重排其外部引用 。


> 源码：[src/input/Pointer.js#L1247](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L1247)  
引入版本：3.0.0


---

### forwardButtonDown {#forwardButtonDown}

#### \<instance> forwardButtonDown() {#instance-forwardbuttondown}


**说明:**

检查是否在此指针上按住前方按钮 。


**返回值:** boolean - 如果前方按钮被扣住,则使用`true`.


> 源码：[src/input/Pointer.js#L945](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L945)  
引入版本：3.0.0


---

### forwardButtonReleased {#forwardButtonReleased}

#### \<instance> forwardButtonReleased() {#instance-forwardbuttonreleased}


**说明:**

检查是否打开了此指针上的最新活动 。


**返回值:** boolean - `true` 如果释放前方按钮是这个指针上最新的活动.


> 源码：[src/input/Pointer.js#L1010](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L1010)  
引入版本：3.18.0


---

### getAngle {#getAngle}

#### \<instance> getAngle() {#instance-getangle}


**说明:**

如果在调用这种方法时点针有按下按钮,它会返回点针的`downX`值和`downY`值与当前位置之间的角度.

如果没有按住按钮,它会返回最后一个记录的角度,基于点数在按钮释放时的位置.

角度是基于面对当前位置的旧位置.

如果您想要获得当前角度, 根据指针的速度, 那么请参见 `Pointer.angle` 属性 。


**返回值:** number - 指针坐标之间以弧度表示的角.


> 源码：[src/input/Pointer.js#L1122](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L1122)  
引入版本：3.16.0


---

### getDistance {#getDistance}

#### \<instance> getDistance() {#instance-getdistance}


**说明:**

如果在调用这种方法时点针有一个按下按钮,它会返回点针的`downX`值和`downY`值之间的距离以及当前位置.

如果没有按住按钮,它将返回最后一个记录的距离,根据是该按钮放出时点的位置.

如果您希望目前能按指针的速度获得所行距,请查看`Pointer.distance`属性.


**返回值:** number - 指针移动的距离.


> 源码：[src/input/Pointer.js#L1023](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L1023)  
引入版本：3.13.0


---

### getDistanceX {#getDistanceX}

#### \<instance> getDistanceX() {#instance-getdistancex}


**说明:**

如果在调用这种方法时点针有按下按钮,它会返回点针的`downX`值与当前`x`位置之间的水平距离.

如果没有按住按钮,它会根据点数在按钮放出时的位置返回最后记录的横向距离.


**返回值:** number - 指针移动的横向距离.


> 源码：[src/input/Pointer.js#L1050](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L1050)  
引入版本：3.16.0


---

### getDistanceY {#getDistanceY}

#### \<instance> getDistanceY() {#instance-getdistancey}


**说明:**

如果在调用这种方法时点针有按下按钮,它会返回点针的`downY`值与当前`y`位置之间的垂直距离.

如果没有按住按钮,它将返回上次记录的垂直距离,根据是当按钮释放时点位置.


**返回值:** number - 指针移动的垂直距离 。


> 源码：[src/input/Pointer.js#L1074](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L1074)  
引入版本：3.16.0


---

### getDuration {#getDuration}

#### \<instance> getDuration() {#instance-getduration}


**说明:**

如果在调用这种方法时点针有按下按钮,它会返回自按下按钮以来的长度.

如果没有按键,它将根据点球上最后一个按键的发布时间返回上次记录的时间.


**返回值:** number - 指针的长度以毫秒计。


> 源码：[src/input/Pointer.js#L1098](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L1098)  
引入版本：3.16.0


---

### getInterpolatedPosition {#getInterpolatedPosition}

#### \<instance> getInterpolatedPosition([steps], [out]) {#instance-getinterpolatedpositionsteps-out}


**说明:**

取上一个和当前指针位置,然后在二者之间生成一系列插值。该数组将被覆盖到 `steps` 参数的大小 。

```javascript
var points = pointer.getInterpolatedPosition(4);

// points[0] = { x: 0, y: 0 }
// points[1] = { x: 2, y: 1 }
// points[2] = { x: 3, y: 2 }
// points[3] = { x: 6, y: 3 }
```

如果您需要从上一个和当前指针位置之间获得平滑值,使用此功能。 DOM指针事件往往比主浏览器循环更快点火, 这样做会帮助您避免强动, 特别是如果您在指针之后有对象的话。

请注意, 如果您提供了输出数组, 它将只被覆盖到所提供步骤的数量。 它不会清除任何可能存在于步骤数范围之外的先前数据 。

内部采用平滑步法插值计算.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| steps | number | 是 | 10 | 插法步骤数用之. |
| out | array | 是 |  | 将保存结果的数组。 如果不提供新的数组, 将会创建 。 |


**返回值:** array - 一系列插值。


> 源码：[src/input/Pointer.js#L1151](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L1151)  
引入版本：3.11.0


---

### leftButtonDown {#leftButtonDown}

#### \<instance> leftButtonDown() {#instance-leftbuttondown}


**说明:**

检查是否在此指针上按下左键 。


**返回值:** boolean - 如果左键被扣住,请按下`true`


> 源码：[src/input/Pointer.js#L893](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L893)  
引入版本：3.0.0


---

### leftButtonReleased {#leftButtonReleased}

#### \<instance> leftButtonReleased() {#instance-leftbuttonreleased}


**说明:**

检查是否打开左键是否是此指针上的最新活动 。


**返回值:** boolean - `true` 如果左键的释放是这个指针上最新的活动.


> 源码：[src/input/Pointer.js#L958](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L958)  
引入版本：3.18.0


---

### middleButtonDown {#middleButtonDown}

#### \<instance> middleButtonDown() {#instance-middlebuttondown}


**说明:**

检查是否在此指针上按住中键 。


**返回值:** boolean - 如果中键被扣住的话,就用`true`.


> 源码：[src/input/Pointer.js#L919](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L919)  
引入版本：3.0.0


---

### middleButtonReleased {#middleButtonReleased}

#### \<instance> middleButtonReleased() {#instance-middlebuttonreleased}


**说明:**

检查是否打开中间按钮是否是此指针上的最新活动 。


**返回值:** boolean - `true` 如果中间按钮的释放是这个指针上最新的活动.


> 源码：[src/input/Pointer.js#L984](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L984)  
引入版本：3.18.0


---

### noButtonDown {#noButtonDown}

#### \<instance> noButtonDown() {#instance-nobuttondown}


**说明:**

检查是否在此指针上按下任何按钮 。


**返回值:** boolean - 如果没有扣下按钮,则按下`true`.


> 源码：[src/input/Pointer.js#L880](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L880)  
引入版本：3.0.0


---

### positionToCamera {#positionToCamera}

#### \<instance> positionToCamera(camera, [output]) {#instance-positiontocameracamera-output}


**说明:**

取一个相机, 返回一个包含该相机内这个指针的翻译位置的矢量2。 这可用于将这个指针位置转换成相机空间 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 用来翻译的相机. |
| output | [Phaser.Math.Vector2](/api/class/math-vector2) \| object | 是 | 一个向量2式对象,用于存储翻译位置。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2), object - 包含此指针的翻译坐标的矢量2,基于给定的相机.


> 源码：[src/input/Pointer.js#L523](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L523)  
引入版本：3.0.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

完全重置此指针回到其未初始化状态 。


> 源码：[src/input/Pointer.js#L1202](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L1202)  
引入版本：3.60.0


---

### rightButtonDown {#rightButtonDown}

#### \<instance> rightButtonDown() {#instance-rightbuttondown}


**说明:**

检查是否在此指针上按下右键 。


**返回值:** boolean - 如果右键被扣住,则使用`true`.


> 源码：[src/input/Pointer.js#L906](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L906)  
引入版本：3.0.0


---

### rightButtonReleased {#rightButtonReleased}

#### \<instance> rightButtonReleased() {#instance-rightbuttonreleased}


**说明:**

检查是否打开右键是否是此指针上最近的活动 。


**返回值:** boolean - `true` 如果右键的释放是这个指针上最新的活动.


> 源码：[src/input/Pointer.js#L971](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L971)  
引入版本：3.18.0


---

### updateWorldPoint {#updateWorldPoint}

#### \<instance> updateWorldPoint(camera) {#instance-updateworldpointcamera}


**说明:**

取一个镜头,更新这个指针的`worldX`和`worldY`值,这样它们就是通过给定的镜头翻译的结果.

注意,当点点被鼠标移动等输入事件更新时,值会自动替换,所以应该立即使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 正在测试的摄像机。 |


**返回值:** [Phaser.Input.Pointer](/api/class/input-pointer) - 此指针对象 。


> 源码：[src/input/Pointer.js#L498](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/Pointer.js#L498)  
引入版本：3.19.0


---

---
