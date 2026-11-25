# Phaser.Physics.Matter.Components.Sleep {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter-components-sleep)

Scope: 
static
> 源码：[src/physics/matter-js/components/Sleep.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Sleep.js#L11)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setAwake {#setAwake}

#### \<instance> setAwake() {#instance-setawake}


**说明:**

如果物理体目前处于睡眠状态,则唤醒它,使其恢复活跃的模拟。一旦醒了,物理体将恢复参与碰撞和物理更新。


**返回值:** [Phaser.Physics.Matter.Components.Sleep](/api/namespace/physics-matter-components-sleep) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Sleep.js#L41](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Sleep.js#L41)  
引入版本：3.22.0


---

### setSleepEndEvent {#setSleepEndEvent}

#### \<instance> setSleepEndEvent(value) {#instance-setsleependeventvalue}


**说明:**

启用或禁用此物理体的睡眠结束事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | `true`可以使此机身的`SLEEP_END`事件,或者`false`可以使其失效. |


**返回值:** [Phaser.Physics.Matter.Components.Sleep](/api/namespace/physics-matter-components-sleep) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Sleep.js#L129](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Sleep.js#L129)  
引入版本：3.0.0


---

### setSleepEvents {#setSleepEvents}

#### \<instance> setSleepEvents(start, end) {#instance-setsleepeventsstart-end}


**说明:**

使这物理体能够睡眠和唤醒事件.

默认当一个物理体睡觉,或者醒来时,它不会放出任何事件.

这些事件是由物质世界实例所揭示的,可以通过`SLEEP_START`和`SLEEP_END`事件来听取。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| start | boolean | 否 | `true` 如果你想让这个物理体 开始睡眠的事件被释放出来 |
| end | boolean | 否 | `true` 如果你想让这个物理体 被释放出睡眠末端事件的话 |


**返回值:** [Phaser.Physics.Matter.Components.Sleep](/api/namespace/physics-matter-components-sleep) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Sleep.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Sleep.js#L76)  
引入版本：3.0.0


---

### setSleepStartEvent {#setSleepStartEvent}

#### \<instance> setSleepStartEvent(value) {#instance-setsleepstarteventvalue}


**说明:**

启用或禁用此物理体的睡眠启动事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | `true`可以使此机身的`SLEEP_START`事件,或者`false`可以使其失效. |


**返回值:** [Phaser.Physics.Matter.Components.Sleep](/api/namespace/physics-matter-components-sleep) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Sleep.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Sleep.js#L100)  
引入版本：3.0.0


---

### setSleepThreshold {#setSleepThreshold}

#### \<instance> setSleepThreshold([value]) {#instance-setsleepthresholdvalue}


**说明:**

设定在设定为睡眠前(如果睡眠是由引擎所允许),此物理体必须拥有近零速度的更新数量.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 60 | 物理体睡眠前需要连续更新近零速度的数量. |


**返回值:** [Phaser.Physics.Matter.Components.Sleep](/api/namespace/physics-matter-components-sleep) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Sleep.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Sleep.js#L57)  
引入版本：3.0.0


---

### setToSleep {#setToSleep}

#### \<instance> setToSleep() {#instance-settosleep}


**说明:**

立即让这个物理体沉睡,从主动模拟中移除。一个沉睡体在被唤醒之前不会移动、产生碰撞或消耗CPU。它可以通过`setAwake`手动唤醒,或者在被另一具物理体撞击时自动唤醒。


**返回值:** [Phaser.Physics.Matter.Components.Sleep](/api/namespace/physics-matter-components-sleep) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Sleep.js#L24](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Sleep.js#L24)  
引入版本：3.22.0


---

---
