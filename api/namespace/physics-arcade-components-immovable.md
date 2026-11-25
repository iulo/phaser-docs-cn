# Phaser.Physics.Arcade.Components.Immovable {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-components-immovable)

Scope: 
static
> 源码：[src/physics/arcade/components/Immovable.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Immovable.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setImmovable {#setImmovable}

#### \<instance> setImmovable([value]) {#instance-setimmovablevalue}


**说明:**

设定此物理体在与其他物理体碰撞时能否分离 。

当一个物理体是不可移动的,它意味着它根本动不了,甚至连碰撞重叠都无法分离。如果你只是想防止一个物理体被其他物理体撞倒,请参见`setPushable`方法。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 碰撞时,这具物理体是不可移动的(`true`)还是可移动的(`false`)。 |


**返回值:** [Phaser.Physics.Arcade.Components.Immovable](/api/namespace/physics-arcade-components-immovable) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Immovable.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Immovable.js#L18)  
引入版本：3.0.0


---

---
