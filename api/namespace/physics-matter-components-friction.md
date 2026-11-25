# Phaser.Physics.Matter.Components.Friction {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter-components-friction)

Scope: 
static
> 源码：[src/physics/matter-js/components/Friction.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Friction.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setFriction {#setFriction}

#### \<instance> setFriction(value, [air], [fstatic]) {#instance-setfrictionvalue-air-fstatic}


**说明:**

为此游戏对象的物质体设定新的摩擦值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 身体的新摩擦,在0到1之间,0允许身体无限滑动,而1允许在施加力量后几乎立即停止. |
| air | number | 是 | 如果提供,则身体的新空气阻力。值越高,身体在穿越空间时会越快地减速。 0 表示身体没有空气阻力。 |
| fstatic | number | 是 | 如果提供, 则身体新的静电摩擦。 数值越高( 例如 10), 身体接近固定状态时, 其初始运动的动力就越大。 0 表示身体在接近固定状态时永远不会" 粘着" 。 |


**返回值:** [Phaser.Physics.Matter.Components.Friction](/api/namespace/physics-matter-components-friction) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Friction.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Friction.js#L15)  
引入版本：3.0.0


---

### setFrictionAir {#setFrictionAir}

#### \<instance> setFrictionAir(value) {#instance-setfrictionairvalue}


**说明:**

设置此游戏对象物质体的新空气阻力。 0 值意味着天体在移动空间时永远不会慢。 值越高, 天体在移动空间时会慢得越快 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 身体的新空气阻力。 |


**返回值:** [Phaser.Physics.Matter.Components.Friction](/api/namespace/physics-matter-components-friction) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Friction.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Friction.js#L44)  
引入版本：3.0.0


---

### setFrictionStatic {#setFrictionStatic}

#### \<instance> setFrictionStatic(value) {#instance-setfrictionstaticvalue}


**说明:**

设置此游戏对象物质体的新静态摩擦。 0 值表示天体在接近静止时永远不会"粘贴"。值越高( 如 10), 初始时它就越需要力使天体在接近静止时运动。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 新的静电摩擦为身体。 |


**返回值:** [Phaser.Physics.Matter.Components.Friction](/api/namespace/physics-matter-components-friction) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Friction.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Friction.js#L63)  
引入版本：3.0.0


---

---
