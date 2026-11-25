# Phaser.Physics.Matter.Components.Force {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter-components-force)

Scope: 
static
> 源码：[src/physics/matter-js/components/Force.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Force.js#L9)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### applyForce {#applyForce}

#### \<instance> applyForce(force) {#instance-applyforceforce}


**说明:**

将力量应用到一个身体 处于目前的质量中心位置。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| force | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 指定要施用的力量的矢量。 |


**返回值:** [Phaser.Physics.Matter.Components.Force](/api/namespace/physics-matter-components-force) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Force.js#L23](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Force.js#L23)  
引入版本：3.0.0


---

### applyForceFrom {#applyForceFrom}

#### \<instance> applyForceFrom(position, force) {#instance-applyforcefromposition-force}


**说明:**

从特定位置对身体施加力量.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| position | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 部队的来历 |
| force | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 指定要施用的力量的矢量。 |


**返回值:** [Phaser.Physics.Matter.Components.Force](/api/namespace/physics-matter-components-force) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Force.js#L42](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Force.js#L42)  
引入版本：3.0.0


---

### thrust {#thrust}

#### \<instance> thrust(speed) {#instance-thrustspeed}


**说明:**

向身体的前进方向应用推力.

视质量和要求的速度,使用极小的值,如0.1.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| speed | number | 否 | 用于方向力的速度值 。 |


**返回值:** [Phaser.Physics.Matter.Components.Force](/api/namespace/physics-matter-components-force) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Force.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Force.js#L60)  
引入版本：3.0.0


---

### thrustBack {#thrustBack}

#### \<instance> thrustBack(speed) {#instance-thrustbackspeed}


**说明:**

将推力应用到身体的反方向.

视质量和要求的速度,使用极小的值,如0.1.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| speed | number | 否 | 用于方向力的速度值 。 |


**返回值:** [Phaser.Physics.Matter.Components.Force](/api/namespace/physics-matter-components-force) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Force.js#L129](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Force.js#L129)  
引入版本：3.0.0


---

### thrustLeft {#thrustLeft}

#### \<instance> thrustLeft(speed) {#instance-thrustleftspeed}


**说明:**

将推力应用到身体的左方向.

视质量和要求的速度,使用极小的值,如0.1.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| speed | number | 否 | 用于方向力的速度值 。 |


**返回值:** [Phaser.Physics.Matter.Components.Force](/api/namespace/physics-matter-components-force) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Force.js#L83](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Force.js#L83)  
引入版本：3.0.0


---

### thrustRight {#thrustRight}

#### \<instance> thrustRight(speed) {#instance-thrustrightspeed}


**说明:**

应用推力向身体的正确方向.

视质量和要求的速度,使用极小的值,如0.1.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| speed | number | 否 | 用于方向力的速度值 。 |


**返回值:** [Phaser.Physics.Matter.Components.Force](/api/namespace/physics-matter-components-force) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Force.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Force.js#L106)  
引入版本：3.0.0


---

---
