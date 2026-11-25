# Gamepad {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/input-gamepad-gamepad)

代表一个连接的游戏板控制器。每个游戏板包含由 Gamepad 插件自动创建和更新的按钮和轴对象。您可以通过 `leftStick` 财务报告和已审计财务报表 `rightStick` 矢量2属性,通过 `buttons` 阵列和轴通过 `axes` 阵列。 Gamepad 通常通过 `this.input.gamepad.pad1` 结束 `pad4` 场景。

**构造函数**

`new Gamepad(manager, pad)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Input.Gamepad.GamepadPlugin](/api/class/input-gamepad-gamepadplugin) | 否 | 引用 Gamepad 插件 。 |
| pad | [Phaser.Types.Input.Gamepad.Pad](/api/typedef/types-input-gamepad#pad) | 否 | Gamepad 对象, 取自 GamepadEvent 。 |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/input/gamepad/Gamepad.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L13)  
引入版本：3.0.0

## 公开成员 {#public-members}

### A {#A}

#### A: boolean {#a-boolean}


**说明:**

Gamepad 右键组的下键是否被按下 ? 如果 Gamepad 没有此按钮, 它将总是返回假。 在双击控制器上, 是 X 按钮。 在 XBox 控制器上是 A 按钮 。


> 源码：[src/input/gamepad/Gamepad.js#L611](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L611)  
引入版本：3.10.0


---

### axes {#axes}

#### axes: Array.\<[Phaser.Input.Gamepad.Axis](/api/class/input-gamepad-axis)> {#axes-arrayphaserinputgamepadaxis}


**说明:**

一组Gamepad轴对象,对应Gamepad上可用的不同轴,如果有的话.


> 源码：[src/input/gamepad/Gamepad.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L107)  
引入版本：3.0.0


---

### B {#B}

#### B: boolean {#b-boolean}


**说明:**

Gamepad 右键是否在右键组中被按下 ? 如果 Gamepad 没有此按钮, 它总是会返回错误。 在双击控制器上, 是圆形按钮。 在 XBox 控制器上是 B 按钮 。


> 源码：[src/input/gamepad/Gamepad.js#L668](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L668)  
引入版本：3.10.0


---

### buttons {#buttons}

#### buttons: Array.\<[Phaser.Input.Gamepad.Button](/api/class/input-gamepad-button)> {#buttons-arrayphaserinputgamepadbutton}


**说明:**

一组Gamepad按钮对象,对应Gamepad上可用的不同按钮.


> 源码：[src/input/gamepad/Gamepad.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L91)  
引入版本：3.0.0


---

### connected {#connected}

#### connected: boolean {#connected-boolean}


**说明:**

这是Gamepad 连接到吗 ?


> 源码：[src/input/gamepad/Gamepad.js#L506](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L506)  
引入版本：3.0.0


---

### down {#down}

#### down: boolean {#down-boolean}


**说明:**

Gamepad 的下调按钮是否被按下 ? 如果 Gamepad 没有此按钮, 它将总是返回错误 。 这是标准 Gamepad 映射下的 d- 将按钮 。


> 源码：[src/input/gamepad/Gamepad.js#L593](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L593)  
引入版本：3.10.0


---

### id {#id}

#### id: string {#id-string}


**说明:**

包含一些控制器信息的字符串 。

这一点没有严格规定,但在Firefox中,它将包含以破折号(-)分隔的三条信息:两条四位数十六进制字符串,包含USB供应商和控制器产品代号,以及驱动器提供的控制器名称。在Chrome中,它将包含驱动器提供的控制器的名称,然后是供应商和产品四位数十六进式字符串。


> 源码：[src/input/gamepad/Gamepad.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L58)  
引入版本：3.0.0


---

### index {#index}

#### index: number {#index-number}


**说明:**

单个 Gamepad 系统当前连接的整数。 可用于区分多个控制器。 请注意, 连接设备后连接新设备, 可以重用上一个索引 。


> 源码：[src/input/gamepad/Gamepad.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L73)  
引入版本：3.0.0


---

### L1 {#L1}

#### L1: number {#l1-number}


**说明:**

返回 Gamepad 左上肩按钮的值。 如果 Gamepad 没有此按钮, 它将总是返回零。 值是 0 到 1 之间的浮点, 与按钮的压抑程度相对应。 在双击控制器上是 L1 按钮。 在 XBox 控制器上是 LB 按钮 。


> 源码：[src/input/gamepad/Gamepad.js#L687](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L687)  
引入版本：3.10.0


---

### L2 {#L2}

#### L2: number {#l2-number}


**说明:**

返回 Gamepad 左下方肩部按钮的值。 如果 Gamepad 没有此按钮, 它将总是返回零。 值是 0 到 1 之间的浮点数, 与按钮的压抑程度相对应。 在双击控制器上是 L2 按钮。 在 XBox 控制器上是 LT 按钮 。


> 源码：[src/input/gamepad/Gamepad.js#L707](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L707)  
引入版本：3.10.0


---

### left {#left}

#### left: boolean {#left-boolean}


**说明:**

Gamepad 的左键是否被按下 ? 如果 Gamepad 没有此按钮, 它将总是返回错误 。 这是 Gamepad 标准绘图下的 d- pad 左键 。


> 源码：[src/input/gamepad/Gamepad.js#L539](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L539)  
引入版本：3.10.0


---

### leftStick {#leftStick}

#### leftStick: [Phaser.Math.Vector2](/api/class/math-vector2) {#leftstick-phasermathvector2}


**说明:**

包含 Gamepad 左轴棒上最近值的矢量 2。 它会自动更新为 Gamepad.update 循环的一部分。 H轴被映射到 `Vector2.x` 属性,以及 V 轴对 `Vector2.y` 属性。数值基于轴阈值。如果 Gamepad 没有左轴棒,则数值将永远为零。


> 源码：[src/input/gamepad/Gamepad.js#L293](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L293)  
引入版本：3.10.0


---

### manager {#manager}

#### manager: [Phaser.Input.Gamepad.GamepadPlugin](/api/class/input-gamepad-gamepadplugin) {#manager-phaserinputgamepadgamepadplugin}


**说明:**

引用 Gamepad 插件 。


> 源码：[src/input/gamepad/Gamepad.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L40)  
引入版本：3.0.0


---

### pad {#pad}

#### pad: any {#pad-any}


**说明:**

引用连接到浏览器的本地 Gamepad 对象 。


> 源码：[src/input/gamepad/Gamepad.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L49)  
引入版本：3.10.0


---

### R1 {#R1}

#### R1: number {#r1-number}


**说明:**

返回 Gamepad 右上方肩部按钮的值。 如果 Gamepad 没有此按钮, 它将总是返回零。 值是0 到 1 之间的浮点数, 与按钮的压抑程度相对应。 在双震控件上是 R1 按钮。 在 XBox 控制器上是 RB 按钮 。


> 源码：[src/input/gamepad/Gamepad.js#L727](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L727)  
引入版本：3.10.0


---

### R2 {#R2}

#### R2: number {#r2-number}


**说明:**

返回 Gamepad 右下方肩部按钮的值。 如果 Gamepad 没有此按钮, 它将总是返回零。 值是 0 到 1 之间的浮点数, 与按钮的压抑程度相对应。 在双击控制器上是 R2 按钮。 在 XBox 控制器上是 RT 按钮 。


> 源码：[src/input/gamepad/Gamepad.js#L747](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L747)  
引入版本：3.10.0


---

### right {#right}

#### right: boolean {#right-boolean}


**说明:**

Gamepad 的右键是否被按下 ? 如果 Gamepad 没有此按钮, 它将总是返回错误 。 这是 Gamepad 绘制标准下的 d- pad 右键 。


> 源码：[src/input/gamepad/Gamepad.js#L557](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L557)  
引入版本：3.10.0


---

### rightStick {#rightStick}

#### rightStick: [Phaser.Math.Vector2](/api/class/math-vector2) {#rightstick-phasermathvector2}


**说明:**

包含 Gamepad 右轴棒最近值的矢量 2。 它会自动更新为 Gamepad.update 循环的一部分。 H 轴被映射到 `Vector2.x` 属性,以及 V 轴对 `Vector2.y` 属性。数值基于轴阈值。如果 Gamepad 没有右轴棒,则数值将永远为零。


> 源码：[src/input/gamepad/Gamepad.js#L306](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L306)  
引入版本：3.10.0


---

### timestamp {#timestamp}

#### timestamp: number {#timestamp-number}


**说明:**

包含此 Gamepad 最新更新时间的时标 。


> 源码：[src/input/gamepad/Gamepad.js#L523](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L523)  
引入版本：3.0.0


---

### up {#up}

#### up: boolean {#up-boolean}


**说明:**

Gamepad 的 Up 按钮是否被按下 ? 如果 Gamepad 没有这个按钮, 它总是会返回错误的 。 这是标准 Gamepad 映射下的 d- pad 按钮 。


> 源码：[src/input/gamepad/Gamepad.js#L575](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L575)  
引入版本：3.10.0


---

### vibration {#vibration}

#### vibration: GamepadHapticActuator {#vibration-gamepadhapticactuator}


**说明:**

Gamepad 的 Haptic 起动器(Vibation / Rumble 支持) 。 这是一种高度实验性, 并且只有在设备上同时存在, 并且被硬件和浏览器都曝光的情况下才设定 。


> 源码：[src/input/gamepad/Gamepad.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L116)  
引入版本：3.10.0


---

### X {#X}

#### X: boolean {#x-boolean}


**说明:**

Gamepad 的左键是否在右键集群中被按下? 如果 Gamepad 没有这个按钮, 它总是会返回假的。 在双震荡控制器上, 是 Square 按钮。 在 XBox 控制器上是 X 按钮 。


> 源码：[src/input/gamepad/Gamepad.js#L649](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L649)  
引入版本：3.10.0


---

### Y {#Y}

#### Y: boolean {#y-boolean}


**说明:**

Gamepad 右键集群的顶部按钮是否被按下? 如果 Gamepad 没有此按钮, 它总是会返回错误。 在双震荡控制器上, 是三角形按钮。 在 XBox 控制器上, 是 Y 按钮 。


> 源码：[src/input/gamepad/Gamepad.js#L630](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L630)  
引入版本：3.10.0


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

摧毁这个 Gamepad 实例,其按钮和轴,并发布它持有的外部引用.


**Overrides:** Phaser.Events.EventEmitter#销毁


> 源码：[src/input/gamepad/Gamepad.js#L477](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L477)  
引入版本：3.10.0


---

### getAxisTotal {#getAxisTotal}

#### \<instance> getAxisTotal() {#instance-getaxistotal}


**说明:**

获得 Gamepad 声称的轴数支持 。


**返回值:** number - Gamepad声称支持的轴数总数.


> 源码：[src/input/gamepad/Gamepad.js#L330](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L330)  
引入版本：3.10.0


---

### getAxisValue {#getAxisValue}

#### \<instance> getAxisValue(index) {#instance-getaxisvalueindex}


**说明:**

以给定索引为基础获取轴值。该索引必须在此 Gamepad 支持的轴范围内有效。返回值将是 - 1 和 1 之间的浮点数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 获得值的轴索引 。 |


**返回值:** number - 轴值,在 -1 和 1 之间.


> 源码：[src/input/gamepad/Gamepad.js#L343](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L343)  
引入版本：3.10.0


---

### getButtonTotal {#getButtonTotal}

#### \<instance> getButtonTotal() {#instance-getbuttontotal}


**说明:**

获得 Gamepad 声称拥有的按钮总数 。


**返回值:** number - Gamepad 声称拥有的按钮总数 。


> 源码：[src/input/gamepad/Gamepad.js#L377](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L377)  
引入版本：3.10.0


---

### getButtonValue {#getButtonValue}

#### \<instance> getButtonValue(index) {#instance-getbuttonvalueindex}


**说明:**

获取基于给定索引的按钮值。该索引必须在此 Gamepad 支持的按钮范围内有效。

返回值将是一个数字按钮的0或1,或者一个0至1之间的浮点,用于压力敏感的模拟按钮,如双震上的肩扣.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 按钮的索引以获取值 。 |


**返回值:** number - 按钮值, 0 到 1 之间 。


> 源码：[src/input/gamepad/Gamepad.js#L390](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L390)  
引入版本：3.10.0


---

### isButtonDown {#isButtonDown}

#### \<instance> isButtonDown(index) {#instance-isbuttondownindex}


**说明:**

如果按下按钮或不按下,返回。索引必须在此 Gamepad 支持的按钮范围内有效。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 按钮的索引以获取值 。 |


**返回值:** boolean - 如果按下按钮就按下`true`,否则按下`false`.


> 源码：[src/input/gamepad/Gamepad.js#L409](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L409)  
引入版本：3.10.0


---

### setAxisThreshold {#setAxisThreshold}

#### \<instance> setAxisThreshold(value) {#instance-setaxisthresholdvalue}


**说明:**

设定此 Gamepad 上所有轴的阈值。 值为 0 到 1 之间的浮点, 并且是轴的下方被认为未移动的数值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 值在 0 到 1 之间 。 |


> 源码：[src/input/gamepad/Gamepad.js#L360](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Gamepad.js#L360)  
引入版本：3.10.0


---

---
