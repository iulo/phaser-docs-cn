# InputManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/input-inputmanager)

输入管理器负责在单Phaser游戏实例中处理指针相关系统.

它将基于游戏配置来创建鼠标和触摸支持的处理器.

键盘和游戏板是插件,由输入Plugin类直接处理.

然后它管理事件,指针的创建和一般的命中测试相关操作.

您很少需要直接与输入管理器互动, 因此, 其所有属性和方法都应视为私密。 相反, 您应该使用输入插件, 即一个场景级别系统, 负责处理场景的所有输入事件 。

**构造函数**

`new InputManager(game, config)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 拥有输入管理器的游戏实例 。 |
| config | object | 否 | 输入配置对象, 游戏配置中设置的 。 |

---


**作用域**: static

> 源码：[src/input/InputManager.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L19)  
引入版本：3.0.0

## 公开成员 {#public-members}

### activePointer {#activePointer}

#### activePointer: [Phaser.Input.Pointer](/api/class/input-pointer) {#activepointer-phaserinputpointer}


**说明:**

最近活跃的指针对象.

如果你在游戏中只有1个指针,那么这将会是准确的,要么是第一个手指触碰的,要么是鼠标.

如果游戏不需要支持多触摸,那么您就可以安全地在游戏代码中使用此属性,并且它会根据设备来适应鼠标或触摸.


> 源码：[src/input/InputManager.js#L200](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L200)  
引入版本：3.0.0


---

### canvas {#canvas}

#### canvas: HTMLCanvasElement {#canvas-htmlcanvaselement}


**说明:**

用于所有 DOM 事件输入听器的 Canvas 。


> 源码：[src/input/InputManager.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L68)  
引入版本：3.0.0


---

### config {#config}

#### config: [Phaser.Core.Config](/api/class/core-config) {#config-phasercoreconfig}


**说明:**

游戏配置对象, 游戏启动时设置的 。


> 源码：[src/input/InputManager.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L77)  
引入版本：3.0.0


---

### defaultCursor {#defaultCursor}

#### defaultCursor: string {#defaultcursor-string}


**说明:**

与游戏交互时使用的默认 CSS 光标 。

详见`setDefaultCursor`方法.


> 源码：[src/input/InputManager.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L116)  
引入版本：3.10.0


---

### enabled {#enabled}

#### enabled: boolean {#enabled-boolean}


**说明:**

如果设定了, 输入管理器将运行其更新循环每个帧 。


> 源码：[src/input/InputManager.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L86)  
引入版本：3.0.0


---

### events {#events}

#### events: [Phaser.Events.EventEmitter](/api/class/events-eventemitter) {#events-phasereventseventemitter}


**说明:**

输入管理器用来从中释放事件的事件 Entertainment Emitter 实例 。


> 源码：[src/input/InputManager.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L96)  
引入版本：3.0.0


---

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

拥有输入管理器的游戏实例。 游戏只保留一个输入管理器实例 。


> 源码：[src/input/InputManager.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L47)  
引入版本：3.0.0


---

### globalTopOnly {#globalTopOnly}

#### globalTopOnly: boolean {#globaltoponly-boolean}


**说明:**

如果 Scene 列表中最上层的 Scene 收到了输入, 它会停止在 scene 列表中下方传播任何下层输入, 即如果您在上方有 UI 显示的 Scene 并点击其中的某个东西, 那么点击将不会被传递到下面的任何其他 Scene 。 禁用此选项, 输入事件会一直通过所有 Scenes 。


> 源码：[src/input/InputManager.js#L214](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L214)  
引入版本：3.0.0


---

### isOver {#isOver}

#### isOver: boolean {#isover-boolean}


**说明:**

游戏布景上是否有鼠标或触点。 由布景自动更新 。


> 源码：[src/input/InputManager.js#L105](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L105)  
引入版本：3.16.0


---

### keyboard {#keyboard}

#### keyboard: [Phaser.Input.Keyboard.KeyboardManager](/api/class/input-keyboard-keyboardmanager) {#keyboard-phaserinputkeyboardkeyboardmanager}


**说明:**

键盘管理器类的引用,如果通过`input.keyboard` Game Config属性启用.


> 源码：[src/input/InputManager.js#L127](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L127)  
引入版本：3.16.0


---

### mouse {#mouse}

#### mouse: [Phaser.Input.Mouse.MouseManager](/api/class/input-mouse-mousemanager) {#mouse-phaserinputmousemousemanager}


**说明:**

鼠标管理器类的引用, 如果通过 `input.mouse` 游戏配置属性启用 。


> 源码：[src/input/InputManager.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L136)  
引入版本：3.0.0


---

### mousePointer {#mousePointer}

#### mousePointer: [Phaser.Input.Pointer](/api/class/input-pointer) {#mousepointer-phaserinputpointer}


**说明:**

鼠标有它自己独特的指针对象,在制作一个 _desktop 特定游戏时可以直接引用。如果您同时支持桌面和触摸设备,那么不要使用此属性,而是使用`activePointer`,它总是映射到最近交互的指针。


> 源码：[src/input/InputManager.js#L189](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L189)  
引入版本：3.10.0


---

### pointers {#pointers}

#### pointers: Array.\<[Phaser.Input.Pointer](/api/class/input-pointer)> {#pointers-arrayphaserinputpointer}


**说明:**

游戏中添加的指针阵列。 第一个条目是鼠标指针, 其余是触摸指针 。

默认情况下, 启用了 1 个触点。 如果您需要更多使用 `addPointer` 方法启动它们, 或者在 Game Config 中设置 `input.activePointers` 属性 。


> 源码：[src/input/InputManager.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L154)  
引入版本：3.10.0


---

### pointersTotal {#pointersTotal}

#### pointersTotal: number {#pointerstotal-number}


**说明:**

激活和处理的触摸对象的数量,每次更新.

您可以在运行时调用 `addPointer` , 或者在 Game Config 中设置 `input.activePointers` 属性, 以此更改此特性 。


> 源码：[src/input/InputManager.js#L167](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L167)  
引入版本：3.10.0


---

### scaleManager {#scaleManager}

#### scaleManager: [Phaser.Scale.ScaleManager](/api/class/scale-scalemanager) {#scalemanager-phaserscalescalemanager}


**说明:**

参考全球游戏缩放管理器。 用于所有边框检查和指针缩放 。


> 源码：[src/input/InputManager.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L58)  
引入版本：3.16.0


---

### time {#time}

#### time: number {#time-number}


**说明:**

上次更新输入管理器时, 此值由 Game Step 每一个框架所覆盖 。


> 源码：[src/input/InputManager.js#L227](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L227)  
引入版本：3.16.2


---

### touch {#touch}

#### touch: [Phaser.Input.Touch.TouchManager](/api/class/input-touch-touchmanager) {#touch-phaserinputtouchtouchmanager}


**说明:**

引用到触摸管理器类,如果通过`input.touch` Game Config属性启用的话.


> 源码：[src/input/InputManager.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L145)  
引入版本：3.0.0


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


> 源码：[src/input/InputManager.js#L466](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L466)  
引入版本：3.10.0


---

### boot {#boot}

#### \<instance> boot() {#instance-boot}


**说明:**

靴子手柄在刚启动时由Phaser.Game调用,渲染器现在已经可用.


**访问权限:** 受保护


**触发事件:** [Phaser.Input.Events#event:MANAGER_BOOT](/api/event/input-events#manager_boot)


> 源码：[src/input/InputManager.js#L302](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L302)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁输入管理器及其所有系统。

这样做是无法恢复的。


> 源码：[src/input/InputManager.js#L1057](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L1057)  
引入版本：3.0.0


---

### hitTest {#hitTest}

#### \<instance> hitTest(pointer, gameObjects, camera, [output]) {#instance-hittestpointer-gameobjects-camera-output}


**说明:**

使用给定的指针和摄像机对一组交互式游戏对象进行命中测试。

游戏对象被与摄像机对峙,然后坐标被翻译为局部摄像机空间,并用来确定它们是否属于剩余的游戏对象命中区.

如果无任何匹配的空数组会被返回 。

这种方法被Intit Plugin自动称为.hitTestPointer 通常不需要直接引用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 指针来测试对手。 |
| gameObjects | array | 否 | 要检查的一系列交互式游戏对象 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 正在测试的摄像机。 |
| output | array | 是 | 一个存储结果的阵列。 如果不给出, 将创建一个新的空阵列 。 |


**返回值:** array - 游戏对象阵列,在本次命中测试中被击中.


> 源码：[src/input/InputManager.js#L868](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L868)  
引入版本：3.0.0


---

### pointWithinHitArea {#pointWithinHitArea}

#### \<instance> pointWithinHitArea(gameObject, x, y) {#instance-pointwithinhitareagameobject-x-y}


**说明:**

检查给定的 x 和 y 坐标是否在游戏对象的命中区域内 。

这种方法假设坐标值已经翻译为Game Object的空间.

如果坐标在命中区之内,它们被设定为游戏对象输入`localX`和`localY`属性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 用于检查的互动游戏对象 。 |
| x | number | 否 | 用于命中测试的翻译x坐标. |
| y | number | 否 | 命中测试的翻译 y 坐标 。 |


**返回值:** boolean - 如果坐标在游戏对象命中区之内,则`true`,否则则`false`.


> 源码：[src/input/InputManager.js#L947](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L947)  
引入版本：3.0.0


---

### pointWithinInteractiveObject {#pointWithinInteractiveObject}

#### \<instance> pointWithinInteractiveObject(object, x, y) {#instance-pointwithininteractiveobjectobject-x-y}


**说明:**

检查给定的 x 和 y 坐标是否在交互式对象的命中区域 。

这种方法假设坐标值已经转换成交互对象的空间.

如果坐标位于命中区之内,则设定为交互式对象输入`localX`和`localY`属性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object | [Phaser.Types.Input.InteractiveObject](/api/typedef/types-input#interactiveobject) | 否 | 用于检查的交互式对象 。 |
| x | number | 否 | 用于命中测试的翻译x坐标. |
| y | number | 否 | 命中测试的翻译 y 坐标 。 |


**返回值:** boolean - 如果坐标在交互式物体的命中区内,则`true`,否则则`false`.


> 源码：[src/input/InputManager.js#L984](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L984)  
引入版本：3.0.0


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


> 源码：[src/input/InputManager.js#L390](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L390)  
引入版本：3.10.0


---

### transformPointer {#transformPointer}

#### \<instance> transformPointer(pointer, pageX, pageY, wasMove) {#instance-transformpointerpointer-pagex-pagey-wasmove}


**说明:**

将指针的pageX和pageY值转换为输入管理器的缩放坐标空间。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 用于转换值的指针 。 |
| pageX | number | 否 | 页面 X 值 。 |
| pageY | number | 否 | 页面Y值 。 |
| wasMove | boolean | 否 | 我们是否要改变指针 从移动事件, 还是一个上/下事件? |


> 源码：[src/input/InputManager.js#L1017](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L1017)  
引入版本：3.10.0


---

### updateInputPlugins {#updateInputPlugins}

#### \<instance> updateInputPlugins(type, pointers) {#instance-updateinputpluginstype-pointers}


**说明:**

内部方法,可以获取游戏中所有活动输入插件的列表,并依次更新每个插件,以反序(上下),以便DOM顶级事件处理模拟.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 类型 | number | 否 | 要处理的事件类型 。 |
| pointers | Array.\<[Phaser.Input.Pointer](/api/class/input-pointer)> | 否 | 事件发生的指针数组 。 |


> 源码：[src/input/InputManager.js#L513](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputManager.js#L513)  
引入版本：3.16.0


---

---
