# TouchManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/input-touch-touchmanager)

触摸管理器是属于输入管理器的辅助类.

它的作用是聆听原生的DOM触摸事件,然后传到输入管理器进行进一步处理.

您不需要直接创建此类, 输入管理器会自动创建一个实例 。

**构造函数**

`new TouchManager(inputManager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| inputManager | [Phaser.Input.InputManager](/api/class/input-inputmanager) | 否 | 输入管理器的参考文献 。 |

---


**作用域**: static

> 源码：[src/input/touch/TouchManager.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L15)  
引入版本：3.0.0

## 公开成员 {#public-members}

### capture {#capture}

#### capture: boolean {#capture-boolean}


**说明:**

如果DOM事件是真的, 将会发生事件。 preventDefault 应用到它们, 如果它们是假的, 将会充分传播。


> 源码：[src/input/touch/TouchManager.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L45)  
引入版本：3.0.0


---

### enabled {#enabled}

#### enabled: boolean {#enabled-boolean}


**说明:**

触摸管理器是否启用, 可用布尔控制。 可以在苍蝇上切换 。


> 源码：[src/input/touch/TouchManager.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L55)  
引入版本：3.0.0


---

### isTop {#isTop}

#### isTop: boolean {#istop-boolean}


**说明:**

活动听众是被`window.top`或`window`迷上了吗?

此设定在 `boot` 序列中。 如果浏览器无法访问 `window.top`, 如在跨源iframe 环境中, 此属性会被设定为 `false` , 而事件被连接到 `window` 中 。


> 源码：[src/input/touch/TouchManager.js#L146](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L146)  
引入版本：3.60.0


---

### manager {#manager}

#### manager: [Phaser.Input.InputManager](/api/class/input-inputmanager) {#manager-phaserinputinputmanager}


**说明:**

输入管理器的参考文献 。


> 源码：[src/input/touch/TouchManager.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L36)  
引入版本：3.0.0


---

### onTouchCancel {#onTouchCancel}

#### onTouchCancel: function {#ontouchcancel-function}


**说明:**

触摸取消事件处理器功能。 最初是空的, 并用 `startListeners` 方法绑定 。


> 源码：[src/input/touch/TouchManager.js#L126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L126)  
引入版本：3.15.0


---

### onTouchCancelWindow {#onTouchCancelWindow}

#### onTouchCancelWindow: function {#ontouchcancelwindow-function}


**说明:**

触摸取消事件处理器专门为窗口上的事件运行。 初始时是空的, 并用 `startListeners` 方法绑定 。


> 源码：[src/input/touch/TouchManager.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L136)  
引入版本：3.18.0


---

### onTouchEnd {#onTouchEnd}

#### onTouchEnd: function {#ontouchend-function}


**说明:**

触摸端事件处理器功能。 最初是空的, 并绑定在 `startListeners` 方法中 。


> 源码：[src/input/touch/TouchManager.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L106)  
引入版本：3.0.0


---

### onTouchEndWindow {#onTouchEndWindow}

#### onTouchEndWindow: function {#ontouchendwindow-function}


**说明:**

触摸结束事件处理器专门为窗口上的事件运行。 最初是空的, 并且用 `startListeners` 方法绑定 。


> 源码：[src/input/touch/TouchManager.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L116)  
引入版本：3.17.0


---

### onTouchMove {#onTouchMove}

#### onTouchMove: function {#ontouchmove-function}


**说明:**

触摸移事件处理器功能。 最初是空的, 并绑定在 `startListeners` 方法中 。


> 源码：[src/input/touch/TouchManager.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L96)  
引入版本：3.0.0


---

### onTouchStart {#onTouchStart}

#### onTouchStart: function {#ontouchstart-function}


**说明:**

触摸启动事件处理器功能。 初始是空的, 并绑定在 `startListeners` 方法中 。


> 源码：[src/input/touch/TouchManager.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L76)  
引入版本：3.0.0


---

### onTouchStartWindow {#onTouchStartWindow}

#### onTouchStartWindow: function {#ontouchstartwindow-function}


**说明:**

触摸启动事件处理器专门为窗口上的事件运行。 初始时是空的, 并用 `startListeners` 方法绑定 。


> 源码：[src/input/touch/TouchManager.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L86)  
引入版本：3.17.0


---

### target {#target}

#### target: any {#target-any}


**说明:**

触摸事件目标, 定义在 Game Config 中. 通常游戏渲染对象的画布, 但可以是任何交互式的 DOM 元素 。


> 源码：[src/input/touch/TouchManager.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L66)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这个触摸管理器实例 。


> 源码：[src/input/touch/TouchManager.js#L384](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L384)  
引入版本：3.0.0


---

### disableContextMenu {#disableContextMenu}

#### \<instance> disableContextMenu() {#instance-disablecontextmenu}


**说明:**

尝试在浏览器上触摸到时禁用上下文菜单。

工作方式是听`contextmenu`事件 并打电话`preventDefault()`在上面。

如果您需要禁用移动上的OS上下文菜单, 请使用此选项 。


**返回值:** [Phaser.Input.Touch.TouchManager](/api/class/input-touch-touchmanager) - 这个触摸管理者的例子。


> 源码：[src/input/touch/TouchManager.js#L198](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L198)  
引入版本：3.20.0


---

### startListeners {#startListeners}

#### \<instance> startListeners() {#instance-startlisteners}


**说明:**

启动触摸事件听众运行, 只要输入目标设定。

如果在游戏配置中启用了触摸输入,则自动使用这种方法。但是,如果需要将输入捕获延迟到游戏的稍后阶段,您可以手动调用。


> 源码：[src/input/touch/TouchManager.js#L221](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L221)  
引入版本：3.0.0


---

### stopListeners {#stopListeners}

#### \<instance> stopListeners() {#instance-stoplisteners}


**说明:**

停止触摸事件听器。 自动调用, 不需要手动引用 。


> 源码：[src/input/touch/TouchManager.js#L358](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/touch/TouchManager.js#L358)  
引入版本：3.0.0


---

---
