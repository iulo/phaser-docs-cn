# Axis {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/input-gamepad-axis)

代表 Gamepad 控制器上的单个轴, 如模拟棒的一个方向。 每个轴都有 `value` 属性范围为 -1 到 1( 以 0 为 死中心), 且可配置 `threshold` 下方的数值按零处理 `getValue()`。轴对象由 Gamepad 自动创建,以适应需要。

**构造函数**

`new Axis(pad, index)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pad | [Phaser.Input.Gamepad.Gamepad](/api/class/input-gamepad-gamepad) | 否 | 提到这个轴属于的Gamepad. |
| index | number | 否 | 此轴的索引 。 |

---


**作用域**: static

> 源码：[src/input/gamepad/Axis.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Axis.js#L9)  
引入版本：3.0.0

## 公开成员 {#public-members}

### events {#events}

#### events: [Phaser.Events.EventEmitter](/api/class/events-eventemitter) {#events-phasereventseventemitter}


**说明:**

用于释放轴事件的事件发射器 。


> 源码：[src/input/gamepad/Axis.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Axis.js#L39)  
引入版本：3.0.0


---

### index {#index}

#### index: number {#index-number}


**说明:**

此轴的索引 。


> 源码：[src/input/gamepad/Axis.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Axis.js#L48)  
引入版本：3.0.0


---

### pad {#pad}

#### pad: [Phaser.Input.Gamepad.Gamepad](/api/class/input-gamepad-gamepad) {#pad-phaserinputgamepadgamepad}


**说明:**

提到这个轴属于的Gamepad.


> 源码：[src/input/gamepad/Axis.js#L30](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Axis.js#L30)  
引入版本：3.0.0


---

### threshold {#threshold}

#### threshold: number {#threshold-number}


**说明:**

运动容忍阈值,`getValue`中忽略了低于此阈值的轴值。


> 源码：[src/input/gamepad/Axis.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Axis.js#L68)  
引入版本：3.0.0


---

### value {#value}

#### value: number {#value-number}


**说明:**

原始轴值,在 - 1 和 1 之间, 0 成为死中点。 使用 `getValue` 方法获得一个与所应用的阈值相一致的值 。


> 源码：[src/input/gamepad/Axis.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Axis.js#L57)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这个轴实例,并发布它持有的外部引用.


> 源码：[src/input/gamepad/Axis.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Axis.js#L109)  
引入版本：3.10.0


---

### getValue {#getValue}

#### \<instance> getValue() {#instance-getvalue}


**说明:**

应用死区阈值后返回轴值。如果轴值的绝对值小于`threshold`,则返回零,防止小棒漂移登记为有意输入。否则返回原`value`。


**返回值:** number - 轴值,根据运动阈值调整.


> 源码：[src/input/gamepad/Axis.js#L94](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/Axis.js#L94)  
引入版本：3.0.0


---

---
