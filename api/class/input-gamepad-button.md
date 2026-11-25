# Button {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/input-gamepad-button)

代表 Gamepad 控制器上的单个按钮。 每个按钮都有一个 `value` 0至1(用于触发的辅助模拟压力)和a `pressed` 布尔状态。 当值超过可配置值时 `threshold`按钮发出 `BUTTON_DOWN` 财务报告和已审计财务报表 `GAMEPAD_BUTTON_DOWN` 事件。按钮对象会根据需要由 GamePad 自动创建。

**构造函数**

`new Button(pad, index, [isPressed])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| pad | [Phaser.Input.Gamepad.Gamepad](/api/class/input-gamepad-gamepad) | 否 |  | 提到这个按钮属于Gamepad. |
| index | number | 否 |  | 此按钮的索引 。 |
| isPressed | boolean | 是 | false | 是否在创建时已经按下按钮 。 这可以防止按钮在初始更新时释放出虚假的“ 下调” 事件 。 |

---


**作用域**: static

> 源码：[src/input/gamepad/Button.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Button.js#L10)  
引入版本：3.0.0

## 公开成员 {#public-members}

### events {#events}

#### events: [Phaser.Events.EventEmitter](/api/class/events-eventemitter) {#events-phasereventseventemitter}


**说明:**

一个事件发射器,用于发送按钮事件 。


> 源码：[src/input/gamepad/Button.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Button.js#L43)  
引入版本：3.0.0


---

### index {#index}

#### index: number {#index-number}


**说明:**

此按钮的索引 。


> 源码：[src/input/gamepad/Button.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Button.js#L52)  
引入版本：3.0.0


---

### pad {#pad}

#### pad: [Phaser.Input.Gamepad.Gamepad](/api/class/input-gamepad-gamepad) {#pad-phaserinputgamepadgamepad}


**说明:**

提到这个按钮属于Gamepad.


> 源码：[src/input/gamepad/Button.js#L34](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Button.js#L34)  
引入版本：3.0.0


---

### pressed {#pressed}

#### pressed: boolean {#pressed-boolean}


**说明:**

按钮被压抑了吗?


> 源码：[src/input/gamepad/Button.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Button.js#L84)  
引入版本：3.0.0


---

### threshold {#threshold}

#### threshold: number {#threshold-number}


**说明:**

按钮必须达到最小值后才能被视为被按下。 值在 0 到 1 之间。 1 的默认值需要按下全部按钮。 对于触发器等模拟按钮, 您可以降低此阈值以检测部分按压 。


> 源码：[src/input/gamepad/Button.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Button.js#L72)  
引入版本：3.0.0


---

### value {#value}

#### value: number {#value-number}


**说明:**

按钮的当前值, 在 0( 完全释放) 到 1( 完全按下) 之间。 对于类似触发器的模拟按钮, 这反映了施加的压力 。


> 源码：[src/input/gamepad/Button.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Button.js#L61)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这个按钮实例并发布它持有的外部引用.


> 源码：[src/input/gamepad/Button.js#L133](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Button.js#L133)  
引入版本：3.10.0


---

---
