# Key {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/input-keyboard-key)

代表键盘上的单一键。键盘对象由键盘插件通过 `addKey()` 并跟踪特定密钥的状态,包括是否当前被扣住,所持时间,新闻发布事件的时间戳,以及重复计数。您可以使用诸如属性等属性直接在游戏循环中查看密钥对象。 `isDown` 财务报告和已审计财务报表 `isUp`,或者通过 `on` 方法。该方法 keyCode 必须是与 `Phaser.Input.Keyboard.KeyCodes` 值。

**构造函数**

`new Key(plugin, keyCode)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| plugin | [Phaser.Input.Keyboard.KeyboardPlugin](/api/class/input-keyboard-keyboardplugin) | 否 | 拥有此密钥对象的键盘插件实例 。 |
| keyCode | number | 否 | 此密钥的密钥代码 。 |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/input/keyboard/keys/Key.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L11)  
引入版本：3.0.0

## 公开成员 {#public-members}

### altKey {#altKey}

#### altKey: boolean {#altkey-boolean}


**说明:**

如果按下与此键同时键, 则 LT 键的下限状态 。


> 源码：[src/input/keyboard/keys/Key.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L96)  
引入版本：3.0.0


---

### ctrlKey {#ctrlKey}

#### ctrlKey: boolean {#ctrlkey-boolean}


**说明:**

CTRL 密钥的下方状态, 如果按下此密钥同时进行 。


> 源码：[src/input/keyboard/keys/Key.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L106)  
引入版本：3.0.0


---

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

此密钥的毫秒数在上一个下调序列中被按住。 只有在密钥更改状态时, 此值不会更新每个游戏步骤。 要获得当前持续时间, 请使用 `getDuration` 方法 。


> 源码：[src/input/keyboard/keys/Key.js#L157](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L157)  
引入版本：3.0.0


---

### emitOnRepeat {#emitOnRepeat}

#### emitOnRepeat: boolean {#emitonrepeat-boolean}


**说明:**

当一个键被扣住时,它是否应该连续发射`down`事件,每次重复一次?

默认情况下, 它只发出一次 `down` 事件, 但是如果你也希望收到每次重复的事件, 请启用此属性 。


> 源码：[src/input/keyboard/keys/Key.js#L179](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L179)  
引入版本：3.16.0


---

### enabled {#enabled}

#### enabled: boolean {#enabled-boolean}


**说明:**

此密钥能否处理 ?


> 源码：[src/input/keyboard/keys/Key.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L66)  
引入版本：3.0.0


---

### isDown {#isDown}

#### isDown: boolean {#isdown-boolean}


**说明:**

键的"下"状态。 只要键盘认为这把键被扣住, 键将保持 `true` 状态 。


> 源码：[src/input/keyboard/keys/Key.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L76)  
引入版本：3.0.0


---

### isUp {#isUp}

#### isUp: boolean {#isup-boolean}


**说明:**

键的"上"状态。 只要键盘认为键盘是上方的, 键盘就保持 `true` 。


> 源码：[src/input/keyboard/keys/Key.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L86)  
引入版本：3.0.0


---

### keyCode {#keyCode}

#### keyCode: number {#keycode-number}


**说明:**

此密钥的密钥代码 。


> 源码：[src/input/keyboard/keys/Key.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L48)  
引入版本：3.0.0


---

### location {#location}

#### location: number {#location-number}


**说明:**

修饰键的位置. 0表示标准(或未知),1表示左,2表示右,3表示南开.


> 源码：[src/input/keyboard/keys/Key.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L137)  
引入版本：3.0.0


---

### metaKey {#metaKey}

#### metaKey: boolean {#metakey-boolean}


**说明:**

如果按下与此键同时键的Meta键的下行状态, 则在Mac上, Meta键是命令键。 在Windows键盘上, 是Windows键。


> 源码：[src/input/keyboard/keys/Key.js#L126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L126)  
引入版本：3.16.0


---

### originalEvent {#originalEvent}

#### originalEvent: KeyboardEvent {#originalevent-keyboardevent}


**说明:**

原DOM事件.


> 源码：[src/input/keyboard/keys/Key.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L57)  
引入版本：3.0.0


---

### plugin {#plugin}

#### plugin: [Phaser.Input.Keyboard.KeyboardPlugin](/api/class/input-keyboard-keyboardplugin) {#plugin-phaserinputkeyboardkeyboardplugin}


**说明:**

拥有此密钥对象的键盘插件实例 。


> 源码：[src/input/keyboard/keys/Key.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L39)  
引入版本：3.17.0


---

### repeats {#repeats}

#### repeats: number {#repeats-number}


**说明:**

如果按住一个键, 键的"重复"次数将保持 。


> 源码：[src/input/keyboard/keys/Key.js#L192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L192)  
引入版本：3.0.0


---

### shiftKey {#shiftKey}

#### shiftKey: boolean {#shiftkey-boolean}


**说明:**

如果按下此键同时键, 则SHIFT 键的下方状态 。


> 源码：[src/input/keyboard/keys/Key.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L116)  
引入版本：3.0.0


---

### timeDown {#timeDown}

#### timeDown: number {#timedown-number}


**说明:**

键上次按下时的时标 。


> 源码：[src/input/keyboard/keys/Key.js#L147](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L147)  
引入版本：3.0.0


---

### timeUp {#timeUp}

#### timeUp: number {#timeup-number}


**说明:**

键上次发布时的时间戳 。


> 源码：[src/input/keyboard/keys/Key.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L169)  
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

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

删除任何约束事件处理器,并删除本地引用。


**Overrides:** Phaser.Events.EventEmitter#销毁


> 源码：[src/input/keyboard/keys/Key.js#L383](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L383)  
引入版本：3.16.0


---

### getDuration {#getDuration}

#### \<instance> getDuration() {#instance-getduration}


**说明:**

返回密钥被扣下的时间, 以毫秒计 。

如果当前键盘没有下, 则返回零 。

为了获得持续时间,在上一个上下周期中,键被扣下,而使用`Key.duration`属性值。


**返回值:** number - 键被扣下来的时间,以毫秒计,如果目前已经下调的话。


> 源码：[src/input/keyboard/keys/Key.js#L358](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L358)  
引入版本：3.17.0


---

### onDown {#onDown}

#### \<instance> onDown(event) {#instance-ondownevent}


**说明:**

处理此密钥的密钥下行。 由键盘插件自动调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | KeyboardEvent | 否 | 本地 DOM 键盘事件. |


**Fires:** [Phaser.Input.Keyboard.Events#event:DOWN](/api/event/input-keyboard-events#down)


> 源码：[src/input/keyboard/keys/Key.js#L253](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L253)  
引入版本：3.16.0


---

### onUp {#onUp}

#### \<instance> onUp(event) {#instance-onupevent}


**说明:**

处理此密钥的密钥上动作。 由键盘插件自动调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | KeyboardEvent | 否 | 本地 DOM 键盘事件. |


**Fires:** [Phaser.Input.Keyboard.Events#event:UP](/api/event/input-keyboard-events#up)


> 源码：[src/input/keyboard/keys/Key.js#L297](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L297)  
引入版本：3.16.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

将此密钥对象重置为默认未压缩状态 。

截至3.60.0版本,它不再重新设置`enabled`或`preventDefault`旗.


**返回值:** [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) - 这个关键例子。


> 源码：[src/input/keyboard/keys/Key.js#L329](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L329)  
引入版本：3.6.0


---

### setEmitOnRepeat {#setEmitOnRepeat}

#### \<instance> setEmitOnRepeat(value) {#instance-setemitonrepeatvalue}


**说明:**

控制此密钥是否在被扣下时会持续释放一个 `down` 事件( 真实), 或者在第一次按下时仅发出一次, 然后跳过未来事件( 假) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 重复的密钥关闭动作的释放`down`事件,还是只一次?. |


**返回值:** [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) - 这个关键例子。


> 源码：[src/input/keyboard/keys/Key.js#L235](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/Key.js#L235)  
引入版本：3.16.0


---

---
