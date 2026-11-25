# Phaser.Physics.Arcade.Components.Bounce {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-components-bounce)

Scope: 
static
> 源码：[src/physics/arcade/components/Bounce.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Bounce.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setBounce {#setBounce}

#### \<instance> setBounce(x, [y]) {#instance-setbouncex-y}


**说明:**

设置此天体的弹跳值。

弹跳是身体与另一个物体碰撞时的还原量或弹性。1值意味着它将在反弹后保持其全部速度。0值意味着它根本不会反弹。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 水平反弹的量适用于碰撞。浮点,一般在0到1之间。 |
| y | number | 是 | "x" | 垂直反弹的量适用于碰撞。浮点,一般在0到1之间。 |


**返回值:** [Phaser.Physics.Arcade.Components.Bounce](/api/namespace/physics-arcade-components-bounce) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Bounce.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Bounce.js#L15)  
引入版本：3.0.0


---

### setBounceX {#setBounceX}

#### \<instance> setBounceX(value) {#instance-setbouncexvalue}


**说明:**

设定此天体的横向弹跳值。 这是当天体与另一个物体碰撞时在 x 轴上应用的还原值。 反弹后1 值保留了全部横向速度。 0 值表示完全没有横向弹跳 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 水平反弹的量适用于碰撞。浮点,一般在0到1之间。 |


**返回值:** [Phaser.Physics.Arcade.Components.Bounce](/api/namespace/physics-arcade-components-bounce) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Bounce.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Bounce.js#L36)  
引入版本：3.0.0


---

### setBounceY {#setBounceY}

#### \<instance> setBounceY(value) {#instance-setbounceyvalue}


**说明:**

设置此天体的垂直弹跳值。 这是当天体与另一个物体碰撞时在y轴上应用的还原量。 反弹后1 的值保留了全部垂直速度。 0 的值意味着完全没有垂直弹跳 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 垂直反弹的量适用于碰撞。浮点,一般在0到1之间。 |


**返回值:** [Phaser.Physics.Arcade.Components.Bounce](/api/namespace/physics-arcade-components-bounce) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Bounce.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Bounce.js#L55)  
引入版本：3.0.0


---

### setCollideWorldBounds {#setCollideWorldBounds}

#### \<instance> setCollideWorldBounds([value], [bounceX], [bounceY], [onWorldBounds]) {#instance-setcollideworldboundsvalue-bouncex-bouncey-onworldbounds}


**说明:**

确定这天体是否与世界边界相撞。

可选的还设置了世界跳动值。 如果 `Body.worldBounce` 无效, 则首先设定为新的 Phaser.Math.Vector2 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 如果这个机构与世界范围相撞的话,就用`true`,否则用`false`. |
| bounceX | number | 是 |  | 如果给出, 这将取代 `worldBounce.x` 值 。 |
| bounceY | number | 是 |  | 如果给出, 这将取代 `worldBounce.y` 值 。 |
| onWorldBounds | boolean | 是 |  | 如果给它替换了机体的`onWorldBounds`值. |


**返回值:** [Phaser.Physics.Arcade.Components.Bounce](/api/namespace/physics-arcade-components-bounce) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Bounce.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Bounce.js#L74)  
引入版本：3.0.0


---

---
