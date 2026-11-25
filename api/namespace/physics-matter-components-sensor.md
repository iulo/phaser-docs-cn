# Phaser.Physics.Matter.Components.Sensor {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter-components-sensor)

Scope: 
static
> 源码：[src/physics/matter-js/components/Sensor.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Sensor.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### isSensor {#isSensor}

#### \<instance> isSensor() {#instance-issensor}


**说明:**

属于这个游戏对象的身体是否是传感器?


**返回值:** boolean - 如果身体是传感器,则使用`true`,否则使用`false`.


> 源码：[src/physics/matter-js/components/Sensor.js#L37](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Sensor.js#L37)  
引入版本：3.0.0


---

### setSensor {#setSensor}

#### \<instance> setSensor(value) {#instance-setsensorvalue}


**说明:**

设定属于此游戏对象的身体为传感器。 传感器触发碰撞事件, 但不要对碰撞对象进行物理反应或推动碰撞对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | `true`将身体设定为传感器,或`false`将其禁用. |


**返回值:** [Phaser.Physics.Matter.Components.Sensor](/api/namespace/physics-matter-components-sensor) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Sensor.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Sensor.js#L19)  
引入版本：3.0.0


---

---
