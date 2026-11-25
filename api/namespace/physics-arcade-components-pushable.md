# Phaser.Physics.Arcade.Components.Pushable {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-components-pushable)

Scope: 
static
> 源码：[src/physics/arcade/components/Pushable.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Pushable.js#L7)  
引入版本：3.50.0

## 静态函数 {#static-functions}

### setPushable {#setPushable}

#### \<instance> setPushable([value]) {#instance-setpushablevalue}


**说明:**

如果此天体能被另一个天体推动, 则设定 。

无法推动的躯体会反射出它被赋予碰撞体的全部速度。 如果这个躯体也不可推动,那么它们之间的分离就会平分。

如果你想让身体永远不动或分开,请看`setImmovable`方法.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 是否可以通过与另一具尸体碰撞来推动这个身体. |


**返回值:** [Phaser.Physics.Arcade.Components.Pushable](/api/namespace/physics-arcade-components-pushable) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Pushable.js#L20](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Pushable.js#L20)  
引入版本：3.50.0


---

---
