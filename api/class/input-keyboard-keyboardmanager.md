# KeyboardManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/input-keyboard-keyboardmanager)

键盘管理器是属于全局输入管理器的辅助类.

它的作用是聆听原生的DOM键盘事件,然后将其存储,由键盘插件进行进一步处理.

您不需要直接创建此类, 如果在 Game Cfig 中启用键盘输入, 输入管理器会自动创建一个实例 。

**构造函数**

`new KeyboardManager(inputManager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| inputManager | [Phaser.Input.InputManager](/api/class/input-inputmanager) | 否 | 输入管理器的参考文献 。 |

---


**作用域**: static

> 源码：[src/input/keyboard/KeyboardManager.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardManager.js#L14)  
引入版本：3.16.0

## 公开成员 {#public-members}

### captures {#captures}

#### captures: Array.\<number> {#captures-arraynumber}


**说明:**

只要`KeyboardManager.preventDefault`布林设定为`true`,一系列将自动让`preventDefault`调用它们的密钥代码值.

默认情况下, 阵列是空的 。

键按下后必须不加修改才能被捕获.

一个非修改键是没有修改键的键,它与之并存,修改键是移位,控制,代位和元键(Mac上的Command,Windows上的Windows键),因此,如果用户按下转动+r,它不会阻止这种组合,因为修改键。但是,如果用户只按R键,它就会被阻止它的事件.

如果您希望停止抓取密钥, 例如切换到基于 DOM 的元素, 您可以在运行时切换 `KeyboardManager.preventDefault` 布尔 。

如果您需要更具体的控制,您可以创建关键对象,并在每个对象上设置旗子。

此阵列可以通过设置 `input.keyboard.capture` 阵列来进行配置, 或者您可以调用 `addCapture` 方法。 另见 `removeCapture` 和 `clearCaptures` 。


> 源码：[src/input/keyboard/KeyboardManager.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardManager.js#L73)  
引入版本：3.16.0


---

### enabled {#enabled}

#### enabled: boolean {#enabled-boolean}


**说明:**

如果启用键盘管理器, 则会显示布林值。 可以在苍蝇上切换 。


> 源码：[src/input/keyboard/KeyboardManager.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardManager.js#L100)  
引入版本：3.16.0


---

### manager {#manager}

#### manager: [Phaser.Input.InputManager](/api/class/input-inputmanager) {#manager-phaserinputinputmanager}


**说明:**

输入管理器的参考文献 。


> 源码：[src/input/keyboard/KeyboardManager.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardManager.js#L36)  
引入版本：3.16.0


---

### onKeyDown {#onKeyDown}

#### onKeyDown: function {#onkeydown-function}


**说明:**

键下事件处理器。 此函数会发送本地 DOM 键上事件。 最初是空的, 并绑定在 `startListeners` 方法中 。


> 源码：[src/input/keyboard/KeyboardManager.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardManager.js#L121)  
引入版本：3.16.0


---

### onKeyUp {#onKeyUp}

#### onKeyUp: function {#onkeyup-function}


**说明:**

键上事件处理器。 此函数会发送本地 DOM 键上事件处理器。 初始是空的, 并用 `startListeners` 方法绑定 。


> 源码：[src/input/keyboard/KeyboardManager.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardManager.js#L132)  
引入版本：3.16.0


---

### preventDefault {#preventDefault}

#### preventDefault: boolean {#preventdefault-boolean}


**说明:**

一个旗子,它控制的是,是否匹配了`captures`阵列中存储的未修改的密钥,是否调用过`preventDefault`.

一个非修改键是没有修改键的键,它与之并存,修改键是移位,控制,代位和元键(Mac上的Command,Windows上的Windows键),因此,如果用户按下转动+r,它不会阻止这种组合,因为修改键。但是,如果用户只按R键,它就会被阻止它的事件.

如果您想要停止抓取密钥, 例如切换到基于 DOM 的元素, 您可以在运行时切换此属性 。


> 源码：[src/input/keyboard/KeyboardManager.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardManager.js#L55)  
引入版本：3.16.0


---

### target {#target}

#### target: any {#target-any}


**说明:**

键盘事件目标,如Game Config中定义的,一般是游戏渲染的窗口,但可以是任何交互式的DOM元素.


> 源码：[src/input/keyboard/KeyboardManager.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardManager.js#L111)  
引入版本：3.16.0


---

## 公开方法 {#public-methods}

### addCapture {#addCapture}

#### \<instance> addCapture(keycode) {#instance-addcapturekeycode}


**说明:**

默认情况下, 按下一个键的 Phaser 将不会阻止事件向浏览器传播。 有些键会令您感到烦恼, 例如箭头键或空间栏, 这使得浏览器窗口滚动 。

这种`addCapture`方法可以消耗特定键的键盘事件,这样它们就不会泡到浏览器上,引起默认浏览器的行为.

请注意键盘抓取是全局的。 这意味着, 如果您从场景内调用这种方法, 也就是说防止空间 BAR 触发页卷轴, 那么它将会防止您游戏中的任何场景, 而不仅仅是调用它 。

您可以以单个密钥代码值, 或一系列密钥代码, 或字符串通过 :

```javascript
this.input.keyboard.addCapture(62);
```

一系列密钥代码 :

```javascript
this.input.keyboard.addCapture([ 62, 63, 64 ]);
```

或弦词:

```javascript
this.input.keyboard.addCapture('W,S,A,D');
```

要使用非α数字键,请使用一个字符串,如“ UP”、“SPACE” 或“ LEFT”。

也可以提供混合字符串和密钥代码整数的数组.

如果在调用此方法后有活动抓取,则`preventDefault`属性设定为`true`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| keycode | string \| number | Array.\<number> | Array.\<any> | 否 | 用于获取的密钥代码,防止它们到达浏览器. |


> 源码：[src/input/keyboard/KeyboardManager.js#L267](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardManager.js#L267)  
引入版本：3.16.0


---

### clearCaptures {#clearCaptures}

#### \<instance> clearCaptures() {#instance-clearcaptures}


**说明:**

删除所有键盘抓取,并将 `preventDefault` 属性设置为 `false` 。


> 源码：[src/input/keyboard/KeyboardManager.js#L402](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardManager.js#L402)  
引入版本：3.16.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此键盘管理器实例 。


> 源码：[src/input/keyboard/KeyboardManager.js#L415](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardManager.js#L415)  
引入版本：3.16.0


---

### removeCapture {#removeCapture}

#### \<instance> removeCapture(keycode) {#instance-removecapturekeycode}


**说明:**

删除已有的密钥抓取。

请注意键盘抓取是全局的。 这意味着, 如果您从场景内调用这种方法, 以删除抓取的键, 那么它将会从游戏中切除, 而不仅仅是调用它 。

您可以以单个密钥代码值, 或一系列密钥代码, 或字符串通过 :

```javascript
this.input.keyboard.removeCapture(62);
```

一系列密钥代码 :

```javascript
this.input.keyboard.removeCapture([ 62, 63, 64 ]);
```

或弦词:

```javascript
this.input.keyboard.removeCapture('W,S,A,D');
```

要使用非α数字键,请使用一个字符串,如“ UP”、“SPACE” 或“ LEFT”。

也可以提供混合字符串和密钥代码整数的数组.

如果在调用这种方法后没有留下捕获,则`preventDefault`属性被设定为`false`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| keycode | string \| number | Array.\<number> | Array.\<any> | 否 | 禁用抓取的密钥代码, 允许它们再次到达浏览器 。 |


> 源码：[src/input/keyboard/KeyboardManager.js#L338](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardManager.js#L338)  
引入版本：3.16.0


---

### startListeners {#startListeners}

#### \<instance> startListeners() {#instance-startlisteners}


**说明:**

启动运行的键盘事件听众。此程序是自动调用,不需要手动引用。


> 源码：[src/input/keyboard/KeyboardManager.js#L175](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardManager.js#L175)  
引入版本：3.16.0


---

### stopListeners {#stopListeners}

#### \<instance> stopListeners() {#instance-stoplisteners}


**说明:**

停止密钥事件听众。 此选项是自动调用, 不需要手动引用 。


> 源码：[src/input/keyboard/KeyboardManager.js#L237](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardManager.js#L237)  
引入版本：3.16.0


---

---
