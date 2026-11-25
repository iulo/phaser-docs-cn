# Phaser.Physics.Matter.Components.Velocity {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter-components-velocity)

Scope: 
static
> 源码：[src/physics/matter-js/components/Velocity.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Velocity.js#L9)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### getAngularSpeed {#getAngularSpeed}

#### \<instance> getAngularSpeed() {#instance-getangularspeed}


**说明:**

获得当前物理体的旋转速度。 等同于其角速度的大小。


**返回值:** number - 物理体目前的角速度.


> 源码：[src/physics/matter-js/components/Velocity.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Velocity.js#L137)  
引入版本：3.60.0


---

### getAngularVelocity {#getAngularVelocity}

#### \<instance> getAngularVelocity() {#instance-getangularvelocity}


**说明:**

获得当前物理体的旋转速度。


**返回值:** number - 物理体目前的角速度.


> 源码：[src/physics/matter-js/components/Velocity.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Velocity.js#L106)  
引入版本：3.60.0


---

### getVelocity {#getVelocity}

#### \<instance> getVelocity() {#instance-getvelocity}


**说明:**

获得物理体的当前线性速度。


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 物理体目前的线性速度.


> 源码：[src/physics/matter-js/components/Velocity.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Velocity.js#L75)  
引入版本：3.60.0


---

### setAngularSpeed {#setAngularSpeed}

#### \<instance> setAngularSpeed(speed) {#instance-setangularspeedspeed}


**说明:**

设置当前物理体的旋转速度。方向得到维护。会影响物理体的角速度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| speed | number | 否 | 角速(原变种). |


**返回值:** [Phaser.Physics.Matter.Components.Velocity](/api/namespace/physics-matter-components-velocity) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Velocity.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Velocity.js#L119)  
引入版本：3.60.0


---

### setAngularVelocity {#setAngularVelocity}

#### \<instance> setAngularVelocity(velocity) {#instance-setangularvelocityvelocity}


**说明:**

立即设定物理体的角速度。位置、角度、力等不变。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| velocity | number | 否 | 角速法门. |


**返回值:** [Phaser.Physics.Matter.Components.Velocity](/api/namespace/physics-matter-components-velocity) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Velocity.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Velocity.js#L88)  
引入版本：3.0.0


---

### setVelocity {#setVelocity}

#### \<instance> setVelocity(x, [y]) {#instance-setvelocityx-y}


**说明:**

设置物理体的横向和纵向速度。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 水平速度值。 |
| y | number | 是 | "x" | 垂直速度值,可以是正的也可以是负的。如果不给定,它将会与`x`值相同。 |


**返回值:** [Phaser.Physics.Matter.Components.Velocity](/api/namespace/physics-matter-components-velocity) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Velocity.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Velocity.js#L55)  
引入版本：3.0.0


---

### setVelocityX {#setVelocityX}

#### \<instance> setVelocityX(x) {#instance-setvelocityxx}


**说明:**

设置物理体的横向速度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 水平速度值,以像素每秒为单位. |


**返回值:** [Phaser.Physics.Matter.Components.Velocity](/api/namespace/physics-matter-components-velocity) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Velocity.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Velocity.js#L17)  
引入版本：3.0.0


---

### setVelocityY {#setVelocityY}

#### \<instance> setVelocityY(y) {#instance-setvelocityyy}


**说明:**

设置物理体的垂直速度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| y | number | 否 | 垂直速度值,以像素每秒计. |


**返回值:** [Phaser.Physics.Matter.Components.Velocity](/api/namespace/physics-matter-components-velocity) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Velocity.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Velocity.js#L36)  
引入版本：3.0.0


---

---
