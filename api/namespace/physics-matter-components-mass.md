# Phaser.Physics.Matter.Components.Mass {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter-components-mass)

Scope: 
static
> 源码：[src/physics/matter-js/components/Mass.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Mass.js#L10)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setDensity {#setDensity}

#### \<instance> setDensity(value) {#instance-setdensityvalue}


**说明:**

设置物理体密度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 物理体的新密度. |


**返回值:** [Phaser.Physics.Matter.Components.Mass](/api/namespace/physics-matter-components-mass) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Mass.js#L35](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Mass.js#L35)  
引入版本：3.0.0


---

### setMass {#setMass}

#### \<instance> setMass(value) {#instance-setmassvalue}


**说明:**

设定游戏对象物质体的质量。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 物理体新质. |


**返回值:** [Phaser.Physics.Matter.Components.Mass](/api/namespace/physics-matter-components-mass) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Mass.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Mass.js#L18)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### centerOfMass {#centerOfMass}

#### centerOfMass: [Phaser.Math.Vector2](/api/class/math-vector2) {#centerofmass-phasermathvector2}


**说明:**

物理体的弥撒中心.

调用此功能,每次都会产生一个新的`Vector2`,以避免突变.

如果你只需要读取值而不改变,可以从`GameObject.body.centerOfMass`获得.


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 弥撒之中心.


> 源码：[src/physics/matter-js/components/Mass.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Mass.js#L52)  
引入版本：3.10.0


---

---
