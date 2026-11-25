# MouseManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/input-mouse-mousemanager)

鼠标管理器是属于输入管理器的辅助类.

其作用是聆听原生的DOM鼠标事件,然后传递到输入管理器进行进一步处理.

您不需要直接创建此类, 输入管理器会自动创建一个实例 。

**构造函数**

`new MouseManager(inputManager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| inputManager | [Phaser.Input.InputManager](/api/class/input-inputmanager) | 否 | 输入管理器的参考文献 。 |

---


**作用域**: static

> 源码：[src/input/mouse/MouseManager.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L15)  
引入版本：3.0.0

## 公开成员 {#public-members}

### enabled {#enabled}

#### enabled: boolean {#enabled-boolean}


**说明:**

如果鼠标管理器启用与否, 则控制布尔值。 可以在运行时切换 。


> 源码：[src/input/mouse/MouseManager.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L85)  
引入版本：3.0.0


---

### isTop {#isTop}

#### isTop: boolean {#istop-boolean}


**说明:**

活动监听器是被`window.top`或`window`迷上了吗?

此设定在 `boot` 序列中。 如果浏览器无法访问 `window.top`, 如在跨源iframe 环境中, 此属性会被设定为 `false` , 而事件被连接到 `window` 中 。


> 源码：[src/input/mouse/MouseManager.js#L215](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L215)  
引入版本：3.50.0


---

### locked {#locked}

#### locked: boolean {#locked-boolean}


**说明:**

如果鼠标已成功锁定指针, 则此选项将设定为真实 。


> 源码：[src/input/mouse/MouseManager.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L106)  
引入版本：3.0.0


---

### manager {#manager}

#### manager: [Phaser.Input.InputManager](/api/class/input-inputmanager) {#manager-phaserinputinputmanager}


**说明:**

输入管理器的参考文献 。


> 源码：[src/input/mouse/MouseManager.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L36)  
引入版本：3.0.0


---

### onMouseDown {#onMouseDown}

#### onMouseDown: function {#onmousedown-function}


**说明:**

鼠标下行事件处理器。 此函数被发送到本地 DOM 鼠标下行程序。 最初是空的, 并用 `startListeners` 方法绑定 。


> 源码：[src/input/mouse/MouseManager.js#L127](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L127)  
引入版本：3.10.0


---

### onMouseDownWindow {#onMouseDownWindow}

#### onMouseDownWindow: function {#onmousedownwindow-function}


**说明:**

鼠标下行事件处理器, 专门处理窗口上的事件。 此函数会发送本地的 DOM 鼠标下行程序。 初始是空的, 并绑定在 `startListeners` 方法中 。


> 源码：[src/input/mouse/MouseManager.js#L149](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L149)  
引入版本：3.17.0


---

### onMouseMove {#onMouseMove}

#### onMouseMove: function {#onmousemove-function}


**说明:**

鼠标移动事件处理器。 此函数被发送到本地 DOM 鼠标Event。 初始时为空, 并绑定在 `startListeners` 方法中 。


> 源码：[src/input/mouse/MouseManager.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L116)  
引入版本：3.10.0


---

### onMouseOut {#onMouseOut}

#### onMouseOut: function {#onmouseout-function}


**说明:**

鼠标出局事件处理器。 此函数被发送到本地 DOM 鼠标出局。 初始是空的, 并用 `startListeners` 方法绑定 。


> 源码：[src/input/mouse/MouseManager.js#L182](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L182)  
引入版本：3.16.0


---

### onMouseOver {#onMouseOver}

#### onMouseOver: function {#onmouseover-function}


**说明:**

鼠标超事件处理器。 此函数会发送本地 DOM 鼠标Event 。 最初是空的, 并用 `startListeners` 方法绑定 。


> 源码：[src/input/mouse/MouseManager.js#L171](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L171)  
引入版本：3.16.0


---

### onMouseUp {#onMouseUp}

#### onMouseUp: function {#onmouseup-function}


**说明:**

鼠标上事件处理器。 此函数被发送本地 DOM 鼠标Event。 最初是空的, 并绑定在 `startListeners` 方法中 。


> 源码：[src/input/mouse/MouseManager.js#L138](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L138)  
引入版本：3.10.0


---

### onMouseUpWindow {#onMouseUpWindow}

#### onMouseUpWindow: function {#onmouseupwindow-function}


**说明:**

鼠标 Up 事件处理器, 专门处理窗口上的事件。 此函数是发送本地 DOM 鼠标 Event 。 最初是空的, 并绑定在 `startListeners` 方法中 。


> 源码：[src/input/mouse/MouseManager.js#L160](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L160)  
引入版本：3.17.0


---

### onMouseWheel {#onMouseWheel}

#### onMouseWheel: function {#onmousewheel-function}


**说明:**

鼠标轮事件处理器。 此函数被发送到本地 DOM 鼠标 Event。 最初是空的, 并用 `startListeners` 方法绑定 。


> 源码：[src/input/mouse/MouseManager.js#L193](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L193)  
引入版本：3.18.0


---

### pointerLockChange {#pointerLockChange}

#### pointerLockChange: function {#pointerlockchange-function}


**说明:**

内部 pointerLockChange 处理器。 此函数会发送本地 DOM 鼠标Event。 最初是空的, 并绑定在 `startListeners` 方法中 。


> 源码：[src/input/mouse/MouseManager.js#L204](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L204)  
引入版本：3.0.0


---

### preventDefaultDown {#preventDefaultDown}

#### preventDefaultDown: boolean {#preventdefaultdown-boolean}


**说明:**

如果`true`,DOM `mousedown`事件将设置`preventDefault`.


> 源码：[src/input/mouse/MouseManager.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L45)  
引入版本：3.50.0


---

### preventDefaultMove {#preventDefaultMove}

#### preventDefaultMove: boolean {#preventdefaultmove-boolean}


**说明:**

如果`true`,DOM `mousemove`事件将设置`preventDefault`.


> 源码：[src/input/mouse/MouseManager.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L65)  
引入版本：3.50.0


---

### preventDefaultUp {#preventDefaultUp}

#### preventDefaultUp: boolean {#preventdefaultup-boolean}


**说明:**

如果`true`,DOM `mouseup`事件将设置`preventDefault`.


> 源码：[src/input/mouse/MouseManager.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L55)  
引入版本：3.50.0


---

### preventDefaultWheel {#preventDefaultWheel}

#### preventDefaultWheel: boolean {#preventdefaultwheel-boolean}


**说明:**

如果`true`,DOM `wheel`事件将设置`preventDefault`.


> 源码：[src/input/mouse/MouseManager.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L75)  
引入版本：3.50.0


---

### target {#target}

#### target: any {#target-any}


**说明:**

鼠标目标, 定义在 Game Config 中。 通常游戏要渲染的画布, 但可以是任何交互式的 DOM 元素 。


> 源码：[src/input/mouse/MouseManager.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L96)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁鼠标管理器实例 。


> 源码：[src/input/mouse/MouseManager.js#L553](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L553)  
引入版本：3.0.0


---

### disableContextMenu {#disableContextMenu}

#### \<instance> disableContextMenu() {#instance-disablecontextmenu}


**说明:**

尝试在游戏画布上右键单击或指定输入目标时,禁用上下文菜单。

工作方式是监听`contextmenu`事件,防止默认.

如果您需要启用游戏中的右键鼠标支持, 则使用此选项, 且上下文菜单会一直阻碍您 。


**返回值:** [Phaser.Input.Mouse.MouseManager](/api/class/input-mouse-mousemanager) - 此鼠标管理器实例 。


> 源码：[src/input/mouse/MouseManager.js#L272](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L272)  
引入版本：3.0.0


---

### releasePointerLock {#releasePointerLock}

#### \<instance> releasePointerLock() {#instance-releasepointerlock}


**说明:**

如果浏览器支持指针锁定, 这将要求释放指针锁定。 如果浏览器成功退出了锁定状态, 将会从游戏的输入管理器中发送一个“ POINTER_ LOCK_ Change_ EVENT ” , 并带有 `isPointerLocked` 属性 。


> 源码：[src/input/mouse/MouseManager.js#L329](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L329)  
引入版本：3.0.0


---

### requestPointerLock {#requestPointerLock}

#### \<instance> requestPointerLock() {#instance-requestpointerlock}


**说明:**

如果浏览器支持,可以要求将指针锁定到浏览器窗口.

这在传统意义上被称为"FPS控制器",指针在用户按出键之前不能离开浏览器.

如果浏览器成功进入锁定状态,将从游戏输入管理器中发送一个`POINTER_LOCK_CHANGE_EVENT`,并带有`isPointerLocked`属性.

需要注意的是,指针锁只有在“ 接触手势” 后才能启用, 参见: [https://w3c.github.io/pointerlock/#dfn-engagement-gesture.](https://w3c.github.io/pointerlock/#dfn-engagement-gesture.)

Firefox的注释: 某些Firefox释放物中有一个错误, 导致本地的 DOM 事件, 如 `mousemove` 。在指针锁定模式下,您可以通过设置绕过此模式。 `this.preventDefaultMove` 改为: `false` 也可能需要为 `preventDefaultDown` 和/或 资源 `preventDefaultUp`。如果遇到错误,请测试这些组合。


> 源码：[src/input/mouse/MouseManager.js#L296](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L296)  
引入版本：3.0.0


---

### startListeners {#startListeners}

#### \<instance> startListeners() {#instance-startlisteners}


**说明:**

启动鼠标事件正在运行的监听器。 自动调用, 不需要手动引用 。


> 源码：[src/input/mouse/MouseManager.js#L346](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L346)  
引入版本：3.0.0


---

### stopListeners {#stopListeners}

#### \<instance> stopListeners() {#instance-stoplisteners}


**说明:**

停止鼠标事件监听器。 自动调用, 不需要手动引用 。


> 源码：[src/input/mouse/MouseManager.js#L520](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/mouse/MouseManager.js#L520)  
引入版本：3.0.0


---

---
