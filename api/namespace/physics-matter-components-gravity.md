# Phaser.Physics.Matter.Components.Gravity {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter-components-gravity)

Scope: 
static
> 源码：[src/physics/matter-js/components/Gravity.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Gravity.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setIgnoreGravity {#setIgnoreGravity}

#### \<instance> setIgnoreGravity(value) {#instance-setignoregravityvalue}


**说明:**

设定此游戏对象的 Matter.js 天体是否应当忽略世界引力。 当设定为 `true` 时, 天体将不会受到 Matter.j 的世界配置中定义的全球引力的影响, 允许它自由漂浮, 不论世界引力设置如何。 游戏播放期间的任何时候都可以改变, 以动态地启用或禁用身体上的引力 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 定在真实中忽略世界引力的影响,或假的不忽略它. |


**返回值:** [Phaser.Physics.Matter.Components.Gravity](/api/namespace/physics-matter-components-gravity) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Gravity.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Gravity.js#L18)  
引入版本：3.0.0


---

---
