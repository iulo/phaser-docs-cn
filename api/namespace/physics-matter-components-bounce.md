# Phaser.Physics.Matter.Components.Bounce {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter-components-bounce)

Scope: 
static
> 源码：[src/physics/matter-js/components/Bounce.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Bounce.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setBounce {#setBounce}

#### \<instance> setBounce(value) {#instance-setbouncevalue}


**说明:**

设置此 Game Object 的 Matter.js 物理体的还原( bonciness) 。 这控制了碰撞后物理体的动能保存量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 定义物理体还原(弹性)的数值。 数值总是正值, 范围是 (0, 1) 。 0 值意味着碰撞可能完全没有弹性, 并且不会发生波浪。 数值是 0. 8 意味着物理体可能以大约80%的动能反弹。 请注意, 碰撞反应是基于对物理体, 并且还原值与以下公式结合: `Math.max(bodyA.restitution, bodyB.restitution)` |


**返回值:** [Phaser.Physics.Matter.Components.Bounce](/api/namespace/physics-matter-components-bounce) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Bounce.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Bounce.js#L21)  
引入版本：3.0.0


---

---
