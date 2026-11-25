# InputPlugin {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/input-inputplugin)

输入插件属于一个场景,并处理所有与之相关的输入事件和操作.

你可以从场内使用`this.input`访问它.

它直接释放事件。例如,你可以:

```javascript
this.input.on('pointerdown', callback, context);
```

来听游戏布上的任何一次指向事件

游戏对象可以通过调用其`setInteractive`方法来启用输入。 之后它们会直接发送输入事件:

```javascript
var sprite = this.add.sprite(x, y, texture);
sprite.setInteractive();
sprite.on('pointerdown', callback, context);
```

有很多与输入相关的游戏配置选项。 更多细节请参见 [Input Config object](code Phaser.Types.Core.InputConfig) , 包括如何处理 Phaser 为画布外的输入事件监听, 如何设置默认的指针数, 输入捕获设置等等 。

更多信息请参见输入示例和教程。

**Incorrect input coordinates with Angular**

如果您在角内使用 Phaser, 并使用 nglf 或 路由器, 使 Phaser 游戏所居的组件成为变化状态( 即出现或消失), 您需要通知 Scale 管理器, 因为 Angular 会以 Phaser 无法直接检测的方式与 DOM 相撞 。 请调用 `this.scale.updateBounds()` , 作为游戏的一部分, 以刷新 Phaser 用于输入点位置计算 。

**构造函数**

`new InputPlugin(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 引用此输入插件负责的场景 。 |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/input/InputPlugin.js#L29](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L29)  
引入版本：3.0.0

## 公开成员 {#public-members}

### activePointer {#activePointer}

#### activePointer: [Phaser.Input.Pointer](/api/class/input-pointer) {#activepointer-phaserinputpointer}


**说明:**

当前活动输入指针 。


> 源码：[src/input/InputPlugin.js#L3262](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3262)  
引入版本：3.0.0


---

### cameras {#cameras}

#### cameras: [Phaser.Cameras.Scene2D.CameraManager](/api/class/cameras-scene2d-cameramanager) {#cameras-phasercamerasscene2dcameramanager}


**说明:**

用于参考场景摄像机管理器。 此属性设定在 `boot` 方法中 。


> 源码：[src/input/InputPlugin.js#L149](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L149)  
引入版本：3.0.0


---

### displayList {#displayList}

#### displayList: [Phaser.GameObjects.DisplayList](/api/class/gameobjects-displaylist) {#displaylist-phasergameobjectsdisplaylist}


**说明:**

引用 Scene 显示列表。 此属性是在 `boot` 方法中设置的 。


> 源码：[src/input/InputPlugin.js#L140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L140)  
引入版本：3.0.0


---

### dragDistanceThreshold {#dragDistanceThreshold}

#### dragDistanceThreshold: number {#dragdistancethreshold-number}


**说明:**

距离,以像素表示,一个指针在被扣住时必须移动,然后才认为是被拖动.


> 源码：[src/input/InputPlugin.js#L247](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L247)  
引入版本：3.0.0


---

### dragTimeThreshold {#dragTimeThreshold}

#### dragTimeThreshold: number {#dragtimethreshold-number}


**说明:**

时间的长度,以ms计,一个指针在它认为拖动之前必须被扣住.

默认投票率是只进行移动投票,所以一旦时间阈值到达拖动事件,拖动事件就不会开始,直到鼠标移动。如果想要在时间阈值达到时立即开始投票,则必须拨打[``setPollAlways``](/api/class/input-inputplugin#setPollAlways)或[``setPollRate``](/api/class/input-inputplugin#setPollRate)来提高投票率。


> 源码：[src/input/InputPlugin.js#L257](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L257)  
引入版本：3.0.0


---

### enabled {#enabled}

#### enabled: boolean {#enabled-boolean}


**说明:**

如果 `true` 此输入插件会处理 DOM 输入事件 。


> 源码：[src/input/InputPlugin.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L130)  
引入版本：3.5.0


---

### gamepad {#gamepad}

#### gamepad: [Phaser.Input.Gamepad.GamepadPlugin](/api/class/input-gamepad-gamepadplugin) {#gamepad-phaserinputgamepadgamepadplugin}


**说明:**

游戏板插件类实例, 如果通过 `input.gamepad` 场景或 Game Config 属性启用。 使用此选项访问连接到浏览器的 Gamepads 并回复 gamepad 按钮 。


> 源码：[src/input/gamepad/GamepadPlugin.js#L640](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L640)  
引入版本：3.10.0


---

### isOver {#isOver}

#### isOver: boolean {#isover-boolean}


**说明:**

游戏布景上目前是否有鼠标或触角指针?


> 源码：[src/input/InputPlugin.js#L3226](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3226)  
引入版本：3.16.0


---

### keyboard {#keyboard}

#### keyboard: [Phaser.Input.Keyboard.KeyboardPlugin](/api/class/input-keyboard-keyboardplugin) {#keyboard-phaserinputkeyboardkeyboardplugin}


**说明:**

键盘插件类实例,如果通过 `input.keyboard` 场景或 Game Config 属性启用。 使用此选项创建键对象并监听键盘特定事件 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L946](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L946)  
引入版本：3.10.0


---

### manager {#manager}

#### manager: [Phaser.Input.InputManager](/api/class/input-inputmanager) {#manager-phaserinputinputmanager}


**说明:**

游戏输入管理器的参考文献 。


> 源码：[src/input/InputPlugin.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L111)  
引入版本：3.0.0


---

### mouse {#mouse}

#### mouse: [Phaser.Input.Mouse.MouseManager](/api/class/input-mouse-mousemanager) {#mouse-phaserinputmousemousemanager}


**说明:**

鼠标管理器的参考文献 。

此属性只有在鼠标支持在您的游戏配置文件中被启用时才设定 。

如果您只是想访问鼠标指针, 请使用 `mousePointer` 属性 。


> 源码：[src/input/InputPlugin.js#L161](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L161)  
引入版本：3.0.0


---

### mousePointer {#mousePointer}

#### mousePointer: [Phaser.Input.Pointer](/api/class/input-pointer) {#mousepointer-phaserinputpointer}


**说明:**

鼠标有它自己独特的指针对象,在制作一个 _desktop 特定游戏时可以直接引用。如果您同时支持桌面和触摸设备,那么不要使用此属性,而是使用`activePointer`,它总是映射到最近交互的指针。


> 源码：[src/input/InputPlugin.js#L3243](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3243)  
引入版本：3.10.0


---

### pointer1 {#pointer1}

#### pointer1: [Phaser.Input.Pointer](/api/class/input-pointer) {#pointer1-phaserinputpointer}


**说明:**

基于触摸的指针对象。 这是 Phaser 创建的第一个指针, 默认情况下可用, 与 `mousePointer` 并列 。


> 源码：[src/input/InputPlugin.js#L3279](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3279)  
引入版本：3.10.0


---

### pointer10 {#pointer10}

#### pointer10: [Phaser.Input.Pointer](/api/class/input-pointer) {#pointer10-phaserinputpointer}


**说明:**

基于触摸的指针对象。 默认情况下, 这将是一个 `undefined`。 除非您使用 `addPointer` 添加新的指针 。


> 源码：[src/input/InputPlugin.js#L3441](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3441)  
引入版本：3.10.0


---

### pointer2 {#pointer2}

#### pointer2: [Phaser.Input.Pointer](/api/class/input-pointer) {#pointer2-phaserinputpointer}


**说明:**

基于触摸的指针对象。 默认情况下, 这将是一个 `undefined`。 除非您使用 `addPointer` 添加新的指针 。


> 源码：[src/input/InputPlugin.js#L3297](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3297)  
引入版本：3.10.0


---

### pointer3 {#pointer3}

#### pointer3: [Phaser.Input.Pointer](/api/class/input-pointer) {#pointer3-phaserinputpointer}


**说明:**

基于触摸的指针对象。 默认情况下, 这将是一个 `undefined`。 除非您使用 `addPointer` 添加新的指针 。


> 源码：[src/input/InputPlugin.js#L3315](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3315)  
引入版本：3.10.0


---

### pointer4 {#pointer4}

#### pointer4: [Phaser.Input.Pointer](/api/class/input-pointer) {#pointer4-phaserinputpointer}


**说明:**

基于触摸的指针对象。 默认情况下, 这将是一个 `undefined`。 除非您使用 `addPointer` 添加新的指针 。


> 源码：[src/input/InputPlugin.js#L3333](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3333)  
引入版本：3.10.0


---

### pointer5 {#pointer5}

#### pointer5: [Phaser.Input.Pointer](/api/class/input-pointer) {#pointer5-phaserinputpointer}


**说明:**

基于触摸的指针对象。 默认情况下, 这将是一个 `undefined`。 除非您使用 `addPointer` 添加新的指针 。


> 源码：[src/input/InputPlugin.js#L3351](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3351)  
引入版本：3.10.0


---

### pointer6 {#pointer6}

#### pointer6: [Phaser.Input.Pointer](/api/class/input-pointer) {#pointer6-phaserinputpointer}


**说明:**

基于触摸的指针对象。 默认情况下, 这将是一个 `undefined`。 除非您使用 `addPointer` 添加新的指针 。


> 源码：[src/input/InputPlugin.js#L3369](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3369)  
引入版本：3.10.0


---

### pointer7 {#pointer7}

#### pointer7: [Phaser.Input.Pointer](/api/class/input-pointer) {#pointer7-phaserinputpointer}


**说明:**

基于触摸的指针对象。 默认情况下, 这将是一个 `undefined`。 除非您使用 `addPointer` 添加新的指针 。


> 源码：[src/input/InputPlugin.js#L3387](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3387)  
引入版本：3.10.0


---

### pointer8 {#pointer8}

#### pointer8: [Phaser.Input.Pointer](/api/class/input-pointer) {#pointer8-phaserinputpointer}


**说明:**

基于触摸的指针对象。 默认情况下, 这将是一个 `undefined`。 除非您使用 `addPointer` 添加新的指针 。


> 源码：[src/input/InputPlugin.js#L3405](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3405)  
引入版本：3.10.0


---

### pointer9 {#pointer9}

#### pointer9: [Phaser.Input.Pointer](/api/class/input-pointer) {#pointer9-phaserinputpointer}


**说明:**

基于触摸的指针对象。 默认情况下, 这将是一个 `undefined`。 除非您使用 `addPointer` 添加新的指针 。


> 源码：[src/input/InputPlugin.js#L3423](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3423)  
引入版本：3.10.0


---

### pollRate {#pollRate}

#### pollRate: number {#pollrate-number}


**说明:**

点数应多久检查一次?

值是时间, 以毫秒表示, 并且是指针再次被授精之前在游戏步骤之间必须经过的时间。 当指针被授精时, 它会进行命中测试, 以查看当前游戏对象位于它下面的哪个, 或者与之交互 。

指针如果被用户移动,或按下或发布,则总是被检查*.

此属性只控制了它们如果不更新会被授粉的频率。 如果您想要让游戏对象不断检查指针, 即使指针本身没有移动, 您应该设置此选项 。

设定为0, 以持续投票。 设定为 - 1 , 仅对用户移动进行投票 。


> 源码：[src/input/InputPlugin.js#L187](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L187)  
引入版本：3.0.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

引用此输入插件负责的场景 。


> 源码：[src/input/InputPlugin.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L84)  
引入版本：3.0.0


---

### settings {#settings}

#### settings: [Phaser.Types.Scenes.SettingsObject](/api/typedef/types-scenes#settingsobject) {#settings-phasertypesscenessettingsobject}


**说明:**

用于参考场景系统设置的参考文献 。


> 源码：[src/input/InputPlugin.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L102)  
引入版本：3.5.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

参考景区系统类.


> 源码：[src/input/InputPlugin.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L93)  
引入版本：3.0.0


---

### topOnly {#topOnly}

#### topOnly: boolean {#toponly-boolean}


**说明:**

设定为 `true`(默认) 时, 输入插件将模拟 DOM 行为, 仅从显示列表中最顶级的游戏对象中释放出事件 。

如果设定为 `false`, 它将会从指针下方的所有游戏对象中释放出事件, 而不仅仅是顶部的事件 。


> 源码：[src/input/InputPlugin.js#L174](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L174)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

基于摄像机列表中第一个摄像机的 ActivePointer 坐标的 x 坐标。 只有在您的游戏只有 1 个非变形摄像机且不使用多触控时, 才安全使用 。


> 源码：[src/input/InputPlugin.js#L3190](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3190)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

基于摄像机列表中第一个摄像机的 ActivePointer y 坐标。 只有在您的游戏只有 1 个非变形摄像机且不使用多触控时, 才安全使用 。


> 源码：[src/input/InputPlugin.js#L3208](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3208)  
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




---

## 公开方法 {#public-methods}

### addPointer {#addPointer}

#### \<instance> addPointer([quantity]) {#instance-addpointerquantity}


**说明:**

将新的指针对象添加到输入管理器中。

默认Phaser会创建2个指针对象:`mousePointer`和`pointer1`.

您可以通过调用这种方法来创建更多, 或者在 Game Config 中设置 `input.activePointers` 属性, 最多可有 10 个指针 。

前10个指针通过`InputPlugin.pointerX`属性提供,一旦通过这种方法添加出来.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| quantity | number | 是 | 1 | 新建指针的数量。 最多允许总共创建10个指针 。 |


**返回值:** Array.\<[Phaser.Input.Pointer](/api/class/input-pointer)> - 包含所有新创建的指针对象的阵列 。


> 源码：[src/input/InputPlugin.js#L3002](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3002)  
引入版本：3.10.0


---

### clear {#clear}

#### \<instance> clear(gameObject, [skipQueue]) {#instance-cleargameobject-skipqueue}


**说明:**

清除一个游戏对象, 使其不再有与之相关的交互式对象。 游戏对象将在下一次更新时排队, 从输入插件中删除 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将删除其互动对象的游戏对象 。 |
| skipQueue | boolean | 是 | false | 跳过将此游戏对象添加到删除队列中吗 ? |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 游戏对象已删除其交互对象 。


> 源码：[src/input/InputPlugin.js#L797](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L797)  
引入版本：3.0.0


---

### disable {#disable}

#### \<instance> disable(gameObject, [resetCursor]) {#instance-disablegameobject-resetcursor}


**说明:**

禁用单个游戏对象上的输入 。

一个输入禁用游戏对象仍然保留其互动对象组件,并且可以随时通过传递到`InputPlugin.enable`而重新启用.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 游戏对象使其输入系统被禁用 。 |
| resetCursor | boolean | 是 | false | 将光标重置为默认值 ? |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入插件 。


> 源码：[src/input/InputPlugin.js#L847](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L847)  
引入版本：3.0.0


---

### enable {#enable}

#### \<instance> enable(gameObject, [hitArea], [hitAreaCallback], [dropZone]) {#instance-enablegameobject-hitarea-hitareacallback-dropzone}


**说明:**

启用游戏对象进行互动 。

如果游戏对象已经拥有交互对象组件,则启用并返回.

否则,将创建一个新的交互对象组件,并分配给游戏对象的`input`属性.

输入通过使用命中区域来工作,这些几乎总是几何形状,如矩形或圆形,它们充当游戏对象的命中区域。但是,如果你想处理一些更先进的输入检测,你可以提供自己的命中区域形状和回调。

如果没有提供参数,它将尝试根据游戏对象使用的纹理帧创建矩形命中区域。如果这不是一个纹理约束对象,如图形或比特玛普Text对象,则会失败,需要提供它使用的具体形状。

您也可以提供输入配置对象作为这种方法的唯一参数。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 要启用的游戏对象输入 。 |
| hitArea | [Phaser.Types.Input.InputConfiguration](/api/typedef/types-input#inputconfiguration) \| any | 是 |  | 输入配置对象,或者定义游戏对象的命中区域的几何形状。如果不指定矩形,则会使用。 |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 是 |  | 用于调用以检查指针是否在命中区域内的“ 包含” 函数 。 |
| dropZone | boolean | 是 | false | 这是游戏对象是投放区还是不是? |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入插件 。


> 源码：[src/input/InputPlugin.js#L903](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L903)  
引入版本：3.0.0


---

### enableDebug {#enableDebug}

#### \<instance> enableDebug(gameObject, [color]) {#instance-enabledebuggameobject-color}


**说明:**

为给定的游戏对象创建输入调试形状。

游戏对象在调用此方法前必须已经允许 _ alady_ 输入 。

用于在开发与调试期间协助您 。

调试形状只能用于使用标准Phaser几何来输入的游戏对象,包括:圆形,椭圆形,线形,多边形,矩形和三角形.

使用自动命中区域的游戏对象默认使用矩形,因此也会成功.

调试形状是创建并添加到显示列表中, 然后与它连接的游戏对象同步。 如果您需要修改, 如要隐藏, 您可以通过游戏对象属性: `GameObject.input.hitAreaDebug` 访问它 。

在已经拥有调试元件的游戏对象上调用这种方法,将会首先破坏旧形状,然后创建新的形状。如果您想要完全删除调试元件,您应该调用 `InputPlugin.removeDebug`。

注意调试形状只显示输入区域的大纲。 如果输入测试使用像素完美检查, 则此选项不显示。 如果您使用自定义形状, 则不会扩展一个基数 Phaser 几何对象, 作为您的命中区域, 这种方法将无法工作 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 创建输入调试形状的游戏对象 。 |
| color | number | 是 | "0x00ff00" | 调试形状的轮廓颜色 。 |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入插件 。


> 源码：[src/input/InputPlugin.js#L2599](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2599)  
引入版本：3.19.0


---

### forceDownState {#forceDownState}

#### \<instance> forceDownState(pointer, gameObject) {#instance-forcedownstatepointer-gameobject}


**说明:**

这种方法将强制给定的游戏对象进入“ 下” 输入状态 。

这将检查游戏对象是否被启用输入, 如果启用, 它会发出 `GAMEOBJECT_POINTER_DOWN`事件。 如果这不会改变输入状态, 它会发出 `GAMEOBJECT_DOWN`事件 。

游戏对象不检查指针,以查看它能否进入此状态,这取决于您在调用此方法之前是否这样做 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 设置状态时使用的指针 。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 设定状态的游戏对象 。 |


**触发事件:** [Phaser.Input.Events#event:GAMEOBJECT_POINTER_DOWN](/api/event/input-events#gameobject_pointer_down), [Phaser.Input.Events#event:GAMEOBJECT_DOWN](/api/event/input-events#gameobject_down)


> 源码：[src/input/InputPlugin.js#L2080](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2080)  
引入版本：3.85.0


---

### forceOutState {#forceOutState}

#### \<instance> forceOutState(pointer, gameObject) {#instance-forceoutstatepointer-gameobject}


**说明:**

这种方法将强制给定的游戏对象进入“ 退出” 输入状态 。

这将检查游戏对象是否被启用输入, 如果启用, 它会发出 `GAMEOBJECT_POINTER_OUT`事件。 如果这不会改变输入状态, 它会发出 `GAMEOBJECT_OUT`事件 。

游戏对象不检查指针,以查看它能否进入此状态,这取决于您在调用此方法之前是否这样做 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 设置状态时使用的指针 。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 设定状态的游戏对象 。 |


**触发事件:** [Phaser.Input.Events#event:GAMEOBJECT_POINTER_OUT](/api/event/input-events#gameobject_pointer_out), [Phaser.Input.Events#event:GAMEOBJECT_OUT](/api/event/input-events#gameobject_out)


> 源码：[src/input/InputPlugin.js#L2149](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2149)  
引入版本：3.85.0


---

### forceOverState {#forceOverState}

#### \<instance> forceOverState(pointer, gameObject) {#instance-forceoverstatepointer-gameobject}


**说明:**

此方法将强制给定的游戏对象进入“ over” 输入状态 。

这将检查游戏对象是否被启用输入, 如果启用, 它会发出 `GAMEOBJECT_POINTER_OVER`事件。 如果这不会改变输入状态, 它会发出 `GAMEOBJECT_OVER`事件 。

游戏对象不检查指针,以查看它能否进入此状态,这取决于您在调用此方法之前是否这样做 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 设置状态时使用的指针 。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 设定状态的游戏对象 。 |


**触发事件:** [Phaser.Input.Events#event:GAMEOBJECT_POINTER_OVER](/api/event/input-events#gameobject_pointer_over), [Phaser.Input.Events#event:GAMEOBJECT_OVER](/api/event/input-events#gameobject_over)


> 源码：[src/input/InputPlugin.js#L2126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2126)  
引入版本：3.85.0


---

### forceState {#forceState}

#### \<instance> forceState(pointer, gameObject, gameObjectEvent, inputPluginEvent, [setCursor]) {#instance-forcestatepointer-gameobject-gameobjectevent-inputpluginevent-setcursor}


**说明:**

这种方法将迫使给定的游戏对象进入给定的输入状态.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 |  | 设置状态时使用的指针 。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 设定状态的游戏对象 。 |
| gameObjectEvent | string | 否 |  | 游戏对象上发布的事件 。 |
| inputPluginEvent | string | 否 |  | 输入插件上发送的事件 。 |
| setCursor | boolean | 是 | false | 光标是否应该设置到游戏对象的光标上? |


> 源码：[src/input/InputPlugin.js#L2172](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2172)  
引入版本：3.85.0


---

### forceUpState {#forceUpState}

#### \<instance> forceUpState(pointer, gameObject) {#instance-forceupstatepointer-gameobject}


**说明:**

这种方法将强制给定的游戏对象进入“ 上” 输入状态 。

这将检查游戏对象是否被启用输入, 如果启用, 它会发出 `GAMEOBJECT_POINTER_UP`事件。 如果这不会改变输入状态, 它会发出 `GAMEOBJECT_UP`事件 。

游戏对象不检查指针,以查看它能否进入此状态,这取决于您在调用此方法之前是否这样做 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 设置状态时使用的指针 。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 设定状态的游戏对象 。 |


**触发事件:** [Phaser.Input.Events#event:GAMEOBJECT_POINTER_UP](/api/event/input-events#gameobject_pointer_up), [Phaser.Input.Events#event:GAMEOBJECT_UP](/api/event/input-events#gameobject_up)


> 源码：[src/input/InputPlugin.js#L2103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2103)  
引入版本：3.85.0


---

### getDragState {#getDragState}

#### \<instance> getDragState(pointer) {#instance-getdragstatepointer}


**说明:**

返回此输入插件的给定指针的拖动状态。

州将以下为一:   州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,  州,

0 = 不拖动任何物 1 = 主按钮下移和对象下移,所以如果符合拖动标准 3 = 指针正在检查中,通知拖动列表 4 = 指针在积极拖动拖动列表,移动 5 = 指针已积极拖动但已释放,通知拖动列表

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 指针来得到拖曳状态 |


**返回值:** number - 给定指针的拖动状态 。


> 源码：[src/input/InputPlugin.js#L1085](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L1085)  
引入版本：3.16.0


---

### hitTestPointer {#hitTestPointer}

#### \<instance> hitTestPointer(pointer) {#instance-hittestpointerpointer}


**说明:**

取下给定的指针并进行对它进行命中测试,看看它目前位于上面的哪个交互式游戏对象.

击打测试是针对指针的任意一个镜头进行的。如果它超过多个镜头,它开始检查镜头列表的顶部,如果找不到任何镜头,则将下移到列表中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 瞄准游戏对象的指针 。 |


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 指针上方包含所有交互式游戏对象的阵列 。


> 源码：[src/input/InputPlugin.js#L953](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L953)  
引入版本：3.0.0


---

### isActive {#isActive}

#### \<instance> isActive() {#instance-isactive}


**说明:**

检查是否输入管理器、 此插件及其所属的场景全部为活动并启用输入 。


**返回值:** boolean - `true` 如果插件和它所属的场景是活动.


> 源码：[src/input/InputPlugin.js#L528](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L528)  
引入版本：3.10.0


---

### makePixelPerfect {#makePixelPerfect}

#### \<instance> makePixelPerfect([alphaTolerance]) {#instance-makepixelperfectalphatolerance}


**说明:**

创建一个函数,可以传递给`setInteractive`,`enable`或`setHitArea`,在图像或基于Sprite的游戏对象上处理像素-完美输入检测,或者任何扩展它们的自定义类.

以下将创建一个可点击任意像素的图示,该像素具有α值QQ 1 。

```javascript
this.add.sprite(x, y, key).setInteractive(this.input.makePixelPerfect());
```

以下将创建一个可点击任意像素的图示, 其α值为 QQ 150 。

```javascript
this.add.sprite(x, y, key).setInteractive(this.input.makePixelPerfect(150));
```

一旦您使一个交互式对象像素完美化,它就会影响所有与之相关的输入事件:下,上,拖动,拖动等.

在一个指针与 Game Object 交互时, 它会不断对纹理进行测试, 从给定坐标中提取一个像素, 并检查其颜色值。 这是一个昂贵的过程, 所以只能对真正需要它的 Game Objects 启用 。

您无法使基于非文字的游戏对象像素完美化。 因此, 图形、 位图图文集、 文本、 提列玛普斯、 容器或粒子等将无法工作 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| alphaTolerance | number | 是 | 1 | 将像素上方的α级作为成功交互包含. |


**返回值:** function - 一个像素完美手提箱,用作hitArea形状回调.


> 源码：[src/input/InputPlugin.js#L2291](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2291)  
引入版本：3.10.0


---

### removeDebug {#removeDebug}

#### \<instance> removeDebug(gameObject) {#instance-removedebuggameobject}


**说明:**

从给定的游戏对象中删除一个输入调试形状。

形状立即被销毁,`hitAreaDebug`的属性被设定为`null`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 从输入调试形状中删除的游戏对象 。 |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入插件 。


> 源码：[src/input/InputPlugin.js#L2739](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2739)  
引入版本：3.19.0


---

### resetCursor {#resetCursor}

#### \<instance> resetCursor() {#instance-resetcursor}


**说明:**

强制输入管理器清除自定义或手游标,而不论游戏对象的交互状态如何。


> 源码：[src/input/InputPlugin.js#L562](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L562)  
引入版本：3.85.0


---

### resetPointers {#resetPointers}

#### \<instance> resetPointers() {#instance-resetpointers}


**说明:**

循环浏览所有输入管理器指针实例,并调用 `reset` 。

如果您发现输入通过Vue等第3方组件从Phaser中被盗, 请使用此功能, 您需要告诉 Phaser 重置 Pointer 状态 。


> 源码：[src/input/InputPlugin.js#L3144](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3144)  
引入版本：3.60.0


---

### setCursor {#setCursor}

#### \<instance> setCursor(interactiveObject) {#instance-setcursorinteractiveobject}


**说明:**

设置游戏母画布元素上的自定义光标,其基础是给定的互动对象(即Sprite)的`cursor`设置.

关于MDN的更多信息,请参见CSS属性`cursor`:

[https://developer.mozilla.org/en-US/docs/Web/CSS/cursor](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor)

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| interactiveObject | [Phaser.Types.Input.InteractiveObject](/api/typedef/types-input#interactiveobject) | 否 | 将光标设置在画布上的交互式对象 。 |


> 源码：[src/input/InputPlugin.js#L541](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L541)  
引入版本：3.85.0


---

### setDefaultCursor {#setDefaultCursor}

#### \<instance> setDefaultCursor(cursor) {#instance-setdefaultcursorcursor}


**说明:**

告诉输入系统设置自定义光标。

此光标将是与游戏画布互动时使用的默认光标 。

如果交互式对象也设置了自定义光标,则此光标在使用后会重置.

允许任何有效的 CSS 光标值,包括映像文件路径,即:

```javascript
this.input.setDefaultCursor('url(assets/cursors/sword.cur), pointer');
```

请读取浏览器在文件格式和它们支持的大小时的差异:

[https://developer.mozilla.org/en-US/docs/Web/CSS/cursor](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor) [https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_User_Interface/Using_URL_values_for_the_cursor_property](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_User_Interface/Using_URL_values_for_the_cursor_property)

由你来选择一个合适的光标格式,它可以工作在您需要支持的浏览器范围.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| cursor | string | 否 | 设置默认光标时使用的 CSS 。 |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入实例 。


> 源码：[src/input/InputPlugin.js#L3025](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L3025)  
引入版本：3.10.0


---

### setDraggable {#setDraggable}

#### \<instance> setDraggable(gameObjects, [value]) {#instance-setdraggablegameobjects-value}


**说明:**

设置游戏对象数组的可拖动状态。

它们可以被设定为可拖动状态,也可以通过`false`将其可拖动状态去除.

游戏对象不会点火拖动事件, 除非它已被指定用于拖动 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObjects | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 用于改变可拖动状态的游戏对象阵列 。 |
| value | boolean | 是 | true | 设定为 `true` 如果游戏对象被拖动, `false` 假设它们应该被解开 |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入式对象 。


> 源码：[src/input/InputPlugin.js#L2246](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2246)  
引入版本：3.0.0


---

### setDragState {#setDragState}

#### \<instance> setDragState(pointer, state) {#instance-setdragstatepointer-state}


**说明:**

设置此输入插件的指针拖动状态。

状态必须是以下价值观之一:

0 = 不拖动任何物 1 = 主按钮下移和对象下移,所以如果符合拖动标准 3 = 指针正在检查中,通知拖动列表 4 = 指针在积极拖动拖动列表,移动 5 = 指针已积极拖动但已释放,通知拖动列表

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 设置拖曳状态的指针 。 |
| state | number | 否 | 拖动状态值。 0 到 5 之间的整数 |


> 源码：[src/input/InputPlugin.js#L1109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L1109)  
引入版本：3.16.0


---

### setGlobalTopOnly {#setGlobalTopOnly}

#### \<instance> setGlobalTopOnly(value) {#instance-setglobaltoponlyvalue}


**说明:**

设定为 `true` 全球输入管理器将模拟 DOM 行为, 只需从 Scene 列表中最上层的空间中释放事件。 默认情况下, 如果 Scene 接收到输入事件, 则会阻止事件在 Scene 列表下方向下流到任何景物中。 要禁用此行为, 请使用此方法 。 `false`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 设定为 `true` 以停止处理接收它的场景上的输入事件,或者 `false` 使事件继续下演场景列表. |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入式对象 。


> 源码：[src/input/InputPlugin.js#L2823](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2823)  
引入版本：3.0.0


---

### setHitArea {#setHitArea}

#### \<instance> setHitArea(gameObjects, [hitArea], [hitAreaCallback]) {#instance-sethitareagameobjects-hitarea-hitareacallback}


**说明:**

设置给定游戏对象阵列的命中区域。

一个命中区通常是Phaser提供的几何形状之一,例如`Phaser.Geom.Rectangle`或`Phaser.Geom.Circle`,但是只要它与所提供的回调配合,它就可以成为任何物体.

如果未提供命中区域,则根据游戏对象的大小创建矩形,如果可能的话进行计算.

命中区调用是使用`x`和`y`坐标并返回布尔的函数,如果这些值是否属于形状区域。所有Phaser几何对象都提供这个功能,例如`Phaser.Geom.Rectangle.Contains`。

一个命中区调用回调可以不使用`hitAreaCallback`参数而供给到`hitArea`参数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObjects | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 设定命中区域的一系列游戏对象 。 |
| hitArea | [Phaser.Types.Input.InputConfiguration](/api/typedef/types-input#inputconfiguration) \| [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | any | 是 | 输入配置对象、定义命中区域的几何形状或命中区域的回调。如果没有指定矩形命中区域,则将使用。 |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 是 | 用于调用以检查指针是否在命中区域内的“ 包含” 函数 。 |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入式对象 。


> 源码：[src/input/InputPlugin.js#L2333](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2333)  
引入版本：3.0.0


---

### setHitAreaCircle {#setHitAreaCircle}

#### \<instance> setHitAreaCircle(gameObjects, x, y, radius, [callback]) {#instance-sethitareacirclegameobjects-x-y-radius-callback}


**说明:**

设定游戏对象阵列的命中区域为`Phaser.Geom.Circle`形状,使用给定的坐标和半径来控制其位置和大小.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObjects | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 设定为有圆形命中区域的一系列游戏对象 。 |
| x | number | 否 | 圆心者. |
| y | number | 否 | 圆心者. |
| radius | number | 否 | 圆之半径. |
| callback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 是 | 命中区呼叫器,如果未定义,则使用圆形。 Contons。 |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入式对象 。


> 源码：[src/input/InputPlugin.js#L2440](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2440)  
引入版本：3.0.0


---

### setHitAreaEllipse {#setHitAreaEllipse}

#### \<instance> setHitAreaEllipse(gameObjects, x, y, width, height, [callback]) {#instance-sethitareaellipsegameobjects-x-y-width-height-callback}


**说明:**

设定游戏对象阵列的命中区域为`Phaser.Geom.Ellipse`形状,使用给定坐标和维度来控制其位置和大小.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObjects | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 要设定的游戏对象阵列有椭圆命中区域 。 |
| x | number | 否 | 椭圆形的中心. |
| y | number | 否 | 椭圆形的中心. |
| width | number | 否 | 椭圆的宽度. |
| height | number | 否 | 椭圆形的高度. |
| callback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 是 | 命中区呼叫器,如果未定义,则使用椭圆形。 Contains。 |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入式对象 。


> 源码：[src/input/InputPlugin.js#L2464](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2464)  
引入版本：3.0.0


---

### setHitAreaFromTexture {#setHitAreaFromTexture}

#### \<instance> setHitAreaFromTexture(gameObjects, [callback]) {#instance-sethitareafromtexturegameobjects-callback}


**说明:**

设定游戏对象阵列的命中区域为`Phaser.Geom.Rectangle`形状,使用游戏对象纹理帧来定义命中区域的位置和大小.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObjects | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 一组游戏对象,根据它们的纹理帧设定为有矩形命中区域. |
| callback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 是 | 命中区调回。 如果未定义, 则使用矩形. contains 。 |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入式对象 。


> 源码：[src/input/InputPlugin.js#L2489](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2489)  
引入版本：3.0.0


---

### setHitAreaRectangle {#setHitAreaRectangle}

#### \<instance> setHitAreaRectangle(gameObjects, x, y, width, height, [callback]) {#instance-sethitarearectanglegameobjects-x-y-width-height-callback}


**说明:**

设定游戏对象阵列的命中区域为`Phaser.Geom.Rectangle`形状,使用给定坐标和维度来控制其位置和大小.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObjects | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 要设定为具有矩形命中区的游戏对象阵列 。 |
| x | number | 否 | 矩形的左上角. |
| y | number | 否 | 矩形的左上角. |
| width | number | 否 | 矩形的宽度 。 |
| height | number | 否 | 长方形的高度. |
| callback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 是 | 命中区调回。 如果未定义, 则使用矩形. contains 。 |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入式对象 。


> 源码：[src/input/InputPlugin.js#L2547](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2547)  
引入版本：3.0.0


---

### setHitAreaTriangle {#setHitAreaTriangle}

#### \<instance> setHitAreaTriangle(gameObjects, x1, y1, x2, y2, x3, y3, [callback]) {#instance-sethitareatrianglegameobjects-x1-y1-x2-y2-x3-y3-callback}


**说明:**

设定游戏对象阵列的命中区域为`Phaser.Geom.Triangle`形状,使用给定坐标来控制其点的位置.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObjects | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 设定为三角命中区域的游戏对象阵列 。 |
| x1 | number | 否 | 三角形第一点的x坐标. |
| y1 | number | 否 | 三角形第一点的y坐标. |
| x2 | number | 否 | 三角形第二点的x坐标. |
| y2 | number | 否 | 三角形第二点的y坐标. |
| x3 | number | 否 | 三角形第三点的x坐标. |
| y3 | number | 否 | 三角形第三点的y坐标. |
| callback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 是 | 命中区呼叫回调,如果未定义,则使用三角形. Contains. |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入式对象 。


> 源码：[src/input/InputPlugin.js#L2572](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2572)  
引入版本：3.0.0


---

### setPollAlways {#setPollAlways}

#### \<instance> setPollAlways() {#instance-setpollalways}


**说明:**

设定指针总是进行民意调查.

当一个指针被调查时,它会进行一个命中测试,以查看目前哪个游戏对象位于它下面,或者与之发生相互作用,无论指针是否实际移动.

如果您想要让游戏中的对象在 / 出局时开火, 而对象在不断移动, 但指针可能没有。 投票每个框架都会产生额外的计算成本, 特别是如果游戏中有大量交互对象 。


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入式对象 。


> 源码：[src/input/InputPlugin.js#L2768](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2768)  
引入版本：3.0.0


---

### setPollOnMove {#setPollOnMove}

#### \<instance> setPollOnMove() {#instance-setpollonmove}


**说明:**

设定指针仅在移动或更新时进行民意调查。

当一个指针被调查时,它会进行一个命中测试,以查看当前该指针下方的游戏对象,或者与之互动.


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入式对象 。


> 源码：[src/input/InputPlugin.js#L2788](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2788)  
引入版本：3.0.0


---

### setPollRate {#setPollRate}

#### \<instance> setPollRate(value) {#instance-setpollratevalue}


**说明:**

设定民意测验率值。 这是在再次对指针进行投票之前应该经过的时间。 请参看 `setPollAlways` 和 `setPollOnMove` 方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 重新计时指示器之前应该经过的时间,以毫秒计。 |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入式对象 。


> 源码：[src/input/InputPlugin.js#L2804](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2804)  
引入版本：3.0.0


---

### setTopOnly {#setTopOnly}

#### \<instance> setTopOnly(value) {#instance-settoponlyvalue}


**说明:**

当设定到 `true` 时, 此输入插件将只从显示列表中最顶级的游戏对象中释放事件来模拟 DOM 行为 。

如果设定为 `false`, 它将会从指针下方的所有游戏对象中释放出事件, 而不仅仅是顶部的事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | `true`只包含最顶级的游戏对象,或`false`将所有游戏对象都包含在命中测试中. |


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入式对象 。


> 源码：[src/input/InputPlugin.js#L2842](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2842)  
引入版本：3.0.0


---

### sortDropZones {#sortDropZones}

#### \<instance> sortDropZones(gameObjects) {#instance-sortdropzonesgameobjects}


**说明:**

鉴于一系列的投放区游戏对象,请排序阵列并返回,使对象在深度指数顺序上与底部最低的单位一致.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObjects | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 要排序的游戏对象阵列 。 |


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的排序阵列 。


> 源码：[src/input/InputPlugin.js#L2892](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2892)  
引入版本：3.52.0


---

### sortGameObjects {#sortGameObjects}

#### \<instance> sortGameObjects(gameObjects, pointer) {#instance-sortgameobjectsgameobjects-pointer}


**说明:**

将游戏对象和指针的数组排序并返回,使对象在底部最小的情况下成正态。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObjects | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 要排序的游戏对象阵列 。 |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 瞄准游戏对象的指针 。 |


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的排序阵列 。


> 源码：[src/input/InputPlugin.js#L2862](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2862)  
引入版本：3.0.0


---

### stopPropagation {#stopPropagation}

#### \<instance> stopPropagation() {#instance-stoppropagation}


**说明:**

这种方法应从输入事件处理器(如`pointerdown`)内调用.

当调用时,它阻止输入管理器允许__此特定事件_由现场列表中尚未处理的任何其他场景处理.


**返回值:** [Phaser.Input.InputPlugin](/api/class/input-inputplugin) - 此输入式对象 。


> 源码：[src/input/InputPlugin.js#L2984](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L2984)  
引入版本：3.0.0


---

### updatePoll {#updatePoll}

#### \<instance> updatePoll(time, delta) {#instance-updatepolltime-delta}


**说明:**

输入管理器自动调用此选项。 它会释放插件可以听的事务, 并且如果启用, 也会处理投票更新 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


**返回值:** boolean - `true` 如果插件和它所属的场景是活动.


> 源码：[src/input/InputPlugin.js#L577](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPlugin.js#L577)  
引入版本：3.18.0


---

---
