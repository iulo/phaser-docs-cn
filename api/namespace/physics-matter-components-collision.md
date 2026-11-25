# Phaser.Physics.Matter.Components.Collision {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter-components-collision)

Scope: 
static
> 源码：[src/physics/matter-js/components/Collision.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Collision.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setCollidesWith {#setCollidesWith}

#### \<instance> setCollidesWith(categories) {#instance-setcollideswithcategories}


**说明:**

设置此游戏对象物质体的碰撞掩码。 具有不同碰撞组的两个物质实体只有在基于位元和即位的将对方的类别纳入其掩码时才会碰撞。 `(categoryA & maskB) !== 0` 财务报告和已审计财务报表 `(categoryB & maskA) !== 0` 都是真的 都一样

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| categories | number \| Array.\<number> | 否 | 独有的类位场,或其中的数组. |


**返回值:** [Phaser.Physics.Matter.Components.Collision](/api/namespace/physics-matter-components-collision) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Collision.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Collision.js#L54)  
引入版本：3.0.0


---

### setCollisionCategory {#setCollisionCategory}

#### \<instance> setCollisionCategory(value) {#instance-setcollisioncategoryvalue}


**说明:**

设置此游戏对象物质体的碰撞类别。 此数字必须是 2^0 (= 1) 和 2^31 之间的两个功率。 两个具有不同碰撞组的物理体( 见 [#setCollisionGroup](#setCollisionGroup)) 只有在它们的碰撞类别包含在碰撞遮罩中时才会碰撞( 见 [#setCollidesWith](#setCollidesWith)) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 独特的类位元 。 |


**返回值:** [Phaser.Physics.Matter.Components.Collision](/api/namespace/physics-matter-components-collision) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Collision.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Collision.js#L15)  
引入版本：3.0.0


---

### setCollisionGroup {#setCollisionGroup}

#### \<instance> setCollisionGroup(value) {#instance-setcollisiongroupvalue}


**说明:**

设置此游戏对象物质体的碰撞组。 如果这是零或两个物质体有不同的值, 它们会按照通常的规则( 见 [#setCollisionCategory](#setCollisionCategory) 和 [#setCollidesWith](#setCollidesWith)) 碰撞。 如果两个物质体有相同的正值, 它们总是碰撞; 如果它们有相同的负值, 它们永远不会碰撞 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 独具群指数. |


**返回值:** [Phaser.Physics.Matter.Components.Collision](/api/namespace/physics-matter-components-collision) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Collision.js#L34](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Collision.js#L34)  
引入版本：3.0.0


---

### setOnCollide {#setOnCollide}

#### \<instance> setOnCollide(callback) {#instance-setoncollidecallback}


**说明:**

设置一个调用符, 当游戏对象的物质主体开始与另一个对象相撞时, 将引用该调用符。 调用符会发送一个 `Phaser.Types.Physics.Matter.MatterCollisionData` 对象 。

这不会改变物理体碰撞的类别、组或过滤器。这些必须设置在召回之外。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | function | 否 | 召回,当这个物理体 开始与另一个碰撞。 |


**返回值:** [Phaser.Physics.Matter.Components.Collision](/api/namespace/physics-matter-components-collision) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Collision.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Collision.js#L87)  
引入版本：3.22.0


---

### setOnCollideActive {#setOnCollideActive}

#### \<instance> setOnCollideActive(callback) {#instance-setoncollideactivecallback}


**说明:**

设置一个调用符, 当此游戏对象的物质体正与另一个物理体积极碰撞时, 将引用每个步骤。 调用符会发送一个 `Phaser.Types.Physics.Matter.MatterCollisionData` 对象 。

这不会改变物理体碰撞的类别、组或过滤器。这些必须设置在召回之外。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | function | 否 | 本机构期间的召回与另一个机构相撞。 |


**返回值:** [Phaser.Physics.Matter.Components.Collision](/api/namespace/physics-matter-components-collision) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Collision.js#L129](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Collision.js#L129)  
引入版本：3.22.0


---

### setOnCollideEnd {#setOnCollideEnd}

#### \<instance> setOnCollideEnd(callback) {#instance-setoncollideendcallback}


**说明:**

设置一个调用符, 当此游戏对象的物质体停止与另一个对象碰撞时, 将引用该调用符。 调用符会发送一个 `Phaser.Types.Physics.Matter.MatterCollisionData` 对象 。

这不会改变物理体碰撞的类别、组或过滤器。这些必须设置在召回之外。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | function | 否 | 当物理体停止与另一个物理体碰撞时,召回来引用。 |


**返回值:** [Phaser.Physics.Matter.Components.Collision](/api/namespace/physics-matter-components-collision) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Collision.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Collision.js#L108)  
引入版本：3.22.0


---

### setOnCollideWith {#setOnCollideWith}

#### \<instance> setOnCollideWith(body, callback) {#instance-setoncollidewithbody-callback}


**说明:**

设置一个调用符, 当此游戏对象的物质体与特定的机构碰撞时, 将引用该调用符。 调用符会发送到另一个机构, 并同时发送一个 `Phaser.Types.Physics.Matter.MatterCollisionData` 对象 。

这不会改变物理体碰撞的类别、组或过滤器。这些必须设置在召回之外。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | MatterJS.Body \| Array.\<MatterJS.Body> | 否 | 物理体,或一系列物理体, 测试与碰撞。 |
| callback | function | 否 | 当这个机构与特定机构发生碰撞时,可召回援引。 |


**返回值:** [Phaser.Physics.Matter.Components.Collision](/api/namespace/physics-matter-components-collision) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Collision.js#L150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Collision.js#L150)  
引入版本：3.22.0


---

---
