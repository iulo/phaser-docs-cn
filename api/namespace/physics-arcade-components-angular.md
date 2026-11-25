# Phaser.Physics.Arcade.Components.Angular {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-components-angular)

Scope: 
static
> 源码：[src/physics/arcade/components/Angular.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Angular.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setAngularAcceleration {#setAngularAcceleration}

#### \<instance> setAngularAcceleration(value) {#instance-setangularaccelerationvalue}


**说明:**

设置机体角加速.

在Arcade物理中,身体不能旋转,它们总是轴向相通的。但是,它们可以有角运动,它传递给捆绑在身体上的游戏对象,导致它们视向旋转,即使身体仍然轴向相通。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 角加速的量,以每秒方位的度计. |


**返回值:** [Phaser.Physics.Arcade.Components.Angular](/api/namespace/physics-arcade-components-angular) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Angular.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Angular.js#L36)  
引入版本：3.0.0


---

### setAngularDrag {#setAngularDrag}

#### \<instance> setAngularDrag(value) {#instance-setangulardragvalue}


**说明:**

设置正体的角拖动。拖动被应用到当前速度,提供减速形式。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 拖动量, 以每秒平方度计 。 |


**返回值:** [Phaser.Physics.Arcade.Components.Angular](/api/namespace/physics-arcade-components-angular) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Angular.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Angular.js#L57)  
引入版本：3.0.0


---

### setAngularVelocity {#setAngularVelocity}

#### \<instance> setAngularVelocity(value) {#instance-setangularvelocityvalue}


**说明:**

设定身体的角速度。

在Arcade物理中,身体不能旋转,它们总是轴向相通的。但是,它们可以有角运动,它传递给捆绑在身体上的游戏对象,导致它们视向旋转,即使身体仍然轴向相通。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 角速度的量,以每秒度计. |


**返回值:** [Phaser.Physics.Arcade.Components.Angular](/api/namespace/physics-arcade-components-angular) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Angular.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Angular.js#L15)  
引入版本：3.0.0


---

---
