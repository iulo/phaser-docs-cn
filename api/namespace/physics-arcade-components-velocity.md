# Phaser.Physics.Arcade.Components.Velocity {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-components-velocity)

Scope: 
static
> 源码：[src/physics/arcade/components/Velocity.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Velocity.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setMaxVelocity {#setMaxVelocity}

#### \<instance> setMaxVelocity(x, [y]) {#instance-setmaxvelocityx-y}


**说明:**

设定物理体的最大速度。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 新的最大水平速度,以每秒像素计. |
| y | number | 是 | "x" | 新的最大垂直速度,以每秒像素计. |


**返回值:** [Phaser.Physics.Arcade.Components.Velocity](/api/namespace/physics-arcade-components-velocity) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Velocity.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Velocity.js#L73)  
引入版本：3.0.0


---

### setVelocity {#setVelocity}

#### \<instance> setVelocity(x, [y]) {#instance-setvelocityx-y}


**说明:**

设定物理体的速度。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 物理体的横向速度,以像素每秒为单位。正值将物理体移到右边,负值则移到左边。 |
| y | number | 是 | "x" | 物理体的垂直速度, 以像素每秒为单位。 正值将物理体向下移动, 而负值则向上移动 。 |


**返回值:** [Phaser.Physics.Arcade.Components.Velocity](/api/namespace/physics-arcade-components-velocity) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Velocity.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Velocity.js#L17)  
引入版本：3.0.0


---

### setVelocityX {#setVelocityX}

#### \<instance> setVelocityX(x) {#instance-setvelocityxx}


**说明:**

设置物理体速度的横向组成部分。

正值将正体移到右边,负值则移到左边.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 新的水平速度,以像素每秒为单位. |


**返回值:** [Phaser.Physics.Arcade.Components.Velocity](/api/namespace/physics-arcade-components-velocity) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Velocity.js#L35](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Velocity.js#L35)  
引入版本：3.0.0


---

### setVelocityY {#setVelocityY}

#### \<instance> setVelocityY(y) {#instance-setvelocityyy}


**说明:**

设置物理体速度的垂直组成部分。

正值将正体向下移动,而负值则向上移动.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| y | number | 否 | 新的垂直速度,以像素每秒为单位. |


**返回值:** [Phaser.Physics.Arcade.Components.Velocity](/api/namespace/physics-arcade-components-velocity) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Velocity.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Velocity.js#L54)  
引入版本：3.0.0


---

---
