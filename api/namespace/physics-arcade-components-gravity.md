# Phaser.Physics.Arcade.Components.Gravity {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-components-gravity)

Scope: 
static
> 源码：[src/physics/arcade/components/Gravity.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Gravity.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setGravity {#setGravity}

#### \<instance> setGravity(x, [y]) {#instance-setgravityx-y}


**说明:**

设置 X 和 Y 轴的车体引力。 这是一种除世界引力外, 以每秒方位像素为单位的加速。 值可以是正值或负值。 较大的绝对值会导致更强的效果 。

如果只提供一个值,则将同时用于X轴和Y轴.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 将应用到X轴上的重力加速度,以每秒方位的像素表示. |
| y | number | 是 | "x" | 将应用到 Y 轴上的重力加速度, 以像素每秒平方位表示。 如果不指定, X 值将被使用 。 |


**返回值:** [Phaser.Physics.Arcade.Components.Gravity](/api/namespace/physics-arcade-components-gravity) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Gravity.js#L23](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Gravity.js#L23)  
引入版本：3.0.0


---

### setGravityX {#setGravityX}

#### \<instance> setGravityX(x) {#instance-setgravityxx}


**说明:**

设置适用于 X 轴的车体引力。这是世界引力以外的加速, 以每秒方位的像素表示。 使用正值将车体拉向右侧, 并使用负值将车体拉到左侧 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 将应用到X轴上的重力加速度,以每秒方位的像素表示. |


**返回值:** [Phaser.Physics.Arcade.Components.Gravity](/api/namespace/physics-arcade-components-gravity) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Gravity.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Gravity.js#L45)  
引入版本：3.0.0


---

### setGravityY {#setGravityY}

#### \<instance> setGravityY(y) {#instance-setgravityyy}


**说明:**

设置适用于 Y 轴的车体引力。 这是世界引力之外的一种加速, 以每秒方位的像素为单位。 使用正值将车体拉向下, 并使用负值将其推向上( 相对于重力 ) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| y | number | 否 | 将应用到Y轴上的重力加速,以像素每秒平方英寸表示. |


**返回值:** [Phaser.Physics.Arcade.Components.Gravity](/api/namespace/physics-arcade-components-gravity) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Gravity.js#L64](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Gravity.js#L64)  
引入版本：3.0.0


---

---
