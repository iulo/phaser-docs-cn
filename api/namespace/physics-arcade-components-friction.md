# Phaser.Physics.Arcade.Components.Friction {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-components-friction)

Scope: 
static
> 源码：[src/physics/arcade/components/Friction.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Friction.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setFriction {#setFriction}

#### \<instance> setFriction(x, [y]) {#instance-setfrictionx-y}


**说明:**

设定此游戏对象物理体的摩擦. 在Arcade Physics中,摩擦是运动从"不可移动"体转移到骑体的特殊案例.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 应用水平摩擦的量, [0, 1]. |
| y | number | 是 | "x" | 应用的垂直摩擦量, [0, 1]. |


**返回值:** [Phaser.Physics.Arcade.Components.Friction](/api/namespace/physics-arcade-components-friction) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Friction.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Friction.js#L19)  
引入版本：3.0.0


---

### setFrictionX {#setFrictionX}

#### \<instance> setFrictionX(x) {#instance-setfrictionxx}


**说明:**

设置此游戏对象物理体的横向摩擦。 当骑行体与这个物理体在垂直轴上相撞时, 它可以横向移动。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 适用摩擦的量, [0, 1]. |


**返回值:** [Phaser.Physics.Arcade.Components.Friction](/api/namespace/physics-arcade-components-friction) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Friction.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Friction.js#L40)  
引入版本：3.0.0


---

### setFrictionY {#setFrictionY}

#### \<instance> setFrictionY(y) {#instance-setfrictionyy}


**说明:**

设置此游戏对象物理体的垂直摩擦。 当它与这个物理体在水平轴上碰撞时, 它可以垂直移动 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| y | number | 否 | 适用摩擦的量, [0, 1]. |


**返回值:** [Phaser.Physics.Arcade.Components.Friction](/api/namespace/physics-arcade-components-friction) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Friction.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Friction.js#L60)  
引入版本：3.0.0


---

---
