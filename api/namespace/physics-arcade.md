# Phaser.Physics.Arcade {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade)

Scope: 
static
> 源码：[src/physics/arcade/index.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/index.js#L10)  


## 静态函数 {#static-functions}

- [ArcadePhysics](/api/class/physics-arcade-arcadephysics)
- [Body](/api/class/physics-arcade-body)
- [Collider](/api/class/physics-arcade-collider)
- [Factory](/api/class/physics-arcade-factory)
- [Group](/api/class/physics-arcade-group)
- [Image](/api/class/physics-arcade-image)
- [Sprite](/api/class/physics-arcade-sprite)
- [StaticBody](/api/class/physics-arcade-staticbody)
- [StaticGroup](/api/class/physics-arcade-staticgroup)
- [World](/api/class/physics-arcade-world)
## 静态函数 {#static-functions-1}

- [Components](/api/namespace/physics-arcade-components)
- [Events](/api/namespace/physics-arcade-events)
- [ProcessX](/api/namespace/physics-arcade-processx)
- [ProcessY](/api/namespace/physics-arcade-processy)
- [Tilemap](/api/namespace/physics-arcade-tilemap)
## 静态函数 {#static-functions-2}

### DYNAMIC_BODY {#DYNAMIC_BODY}

#### DYNAMIC_BODY: number {#dynamic_body-number}


**说明:**

动态身体。


> 源码：[src/physics/arcade/const.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/const.js#L15)  
引入版本：3.0.0


---

### FACING_DOWN {#FACING_DOWN}

#### FACING_DOWN: number {#facing_down-number}


**说明:**

面朝下  .


> 源码：[src/physics/arcade/const.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/const.js#L85)  
引入版本：3.0.0


---

### FACING_LEFT {#FACING_LEFT}

#### FACING_LEFT: number {#facing_left-number}


**说明:**

面对左.


> 源码：[src/physics/arcade/const.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/const.js#L97)  
引入版本：3.0.0


---

### FACING_NONE {#FACING_NONE}

#### FACING_NONE: number {#facing_none-number}


**说明:**

面对无方向( 初始值 ) 。


> 源码：[src/physics/arcade/const.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/const.js#L61)  
引入版本：3.0.0


---

### FACING_RIGHT {#FACING_RIGHT}

#### FACING_RIGHT: number {#facing_right-number}


**说明:**

面对右.


> 源码：[src/physics/arcade/const.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/const.js#L109)  
引入版本：3.0.0


---

### FACING_UP {#FACING_UP}

#### FACING_UP: number {#facing_up-number}


**说明:**

面对.


> 源码：[src/physics/arcade/const.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/const.js#L73)  
引入版本：3.0.0


---

### GROUP {#GROUP}

#### GROUP: number {#group-number}


**说明:**

弧形物理组,包含动态天体.


> 源码：[src/physics/arcade/const.js#L41](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/const.js#L41)  
引入版本：3.0.0


---

### STATIC_BODY {#STATIC_BODY}

#### STATIC_BODY: number {#static_body-number}


**说明:**

静态身体.


> 源码：[src/physics/arcade/const.js#L28](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/const.js#L28)  
引入版本：3.0.0


---

### TILEMAPLAYER {#TILEMAPLAYER}

#### TILEMAPLAYER: number {#tilemaplayer-number}


**说明:**

平面图层 。


> 源码：[src/physics/arcade/const.js#L51](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/const.js#L51)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-3}

### GetCollidesWith {#GetCollidesWith}

#### \<static> GetCollidesWith(categories) {#static-getcollideswithcategories}


**说明:**

组合一个或多个类位元字段使用位元OR,并返回由此而来的碰撞掩码。这个掩码可以被分配到Arcade物理机构,以定义它应该与哪几类天体碰撞。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| categories | number \| Array.\<number> | 否 | 独有的类位场,或其中的数组. |


**返回值:** number - 代表组合的、应触发碰撞的类别。


> 源码：[src/physics/arcade/GetCollidesWith.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/GetCollidesWith.js#L7)  
引入版本：3.70.0


---

### GetOverlapX {#GetOverlapX}

#### \<static> GetOverlapX(body1, body2, overlapOnly, bias) {#static-getoverlapxbody1-body2-overlaponly-bias}


**说明:**

计算并返回两个街机物理体之间的横向重叠,并相应设置其属性,包括:`touching.left`,`touching.right`,`touching.none`和`overlapX`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body1 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 初身分别. |
| body2 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 第二身分别. |
| overlapOnly | boolean | 否 | 这是重复的检查,还是分离的一部分? |
| bias | number | 否 | 在碰撞检查时增加三角洲值的值。 增加它以防止闪烁隧道( 闪烁通过另一个而不是碰撞) 。 |


**返回值:** number - 重叠的量。


> 源码：[src/physics/arcade/GetOverlapX.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/GetOverlapX.js#L9)  
引入版本：3.0.0


---

### GetOverlapY {#GetOverlapY}

#### \<static> GetOverlapY(body1, body2, overlapOnly, bias) {#static-getoverlapybody1-body2-overlaponly-bias}


**说明:**

计算并返回两个街机物理体之间的垂直重叠,并相应设定其属性,包括: `touching.up`, `touching.down`, `touching.none`, `blocked.up`, `blocked.down` 财务报告和已审计财务报表 `overlapY`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body1 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 初身分别. |
| body2 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 第二身分别. |
| overlapOnly | boolean | 否 | 这是重复的检查,还是分离的一部分? |
| bias | number | 否 | 在碰撞检查时增加三角洲值的值。 增加它以防止闪烁隧道( 闪烁通过另一个而不是碰撞) 。 |


**返回值:** number - 重叠的量。


> 源码：[src/physics/arcade/GetOverlapY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/GetOverlapY.js#L9)  
引入版本：3.0.0


---

### SeparateX {#SeparateX}

#### \<static> SeparateX(body1, body2, overlapOnly, bias, [overlap]) {#static-separatexbody1-body2-overlaponly-bias-overlap}


**说明:**

分离X轴上两个重叠的机体(视距).

分离涉及移动两个重叠的体,这样它们就不再重叠,并且根据质量调整速度。这是碰撞探测的核心部分。

如果它们之间没有横向重叠,如果两者都是不可移动的,或者如果其中一方通过`customSeparateX`使用自定义的分离逻辑,则两者不会被分离.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body1 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 初身分别. |
| body2 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 第二身分别. |
| overlapOnly | boolean | 否 | 如果`true`,则两具尸体只能有重叠的数据集,不会进行分离. |
| bias | number | 否 | 重复检查时添加三角洲值的值。 用于防止图示隧道的挖掘 。 |
| overlap | number | 是 | 如果给出了, 此值将被用作重叠, 并且不会运行检查 。 |


**返回值:** boolean - 如果两具尸体横向重叠,则使用`true`,否则使用`false`.


> 源码：[src/physics/arcade/SeparateX.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/SeparateX.js#L10)  
引入版本：3.0.0


---

### SeparateY {#SeparateY}

#### \<static> SeparateY(body1, body2, overlapOnly, bias, [overlap]) {#static-separateybody1-body2-overlaponly-bias-overlap}


**说明:**

分离Y轴上两个重叠的机体(垂直).

分离涉及移动两个重叠的体,这样它们就不再重叠,并且根据质量调整速度。这是碰撞探测的核心部分。

如果两者之间没有垂直重叠,如果它们都是静态的,或者如果其中之一使用自定义逻辑来进行分离,则它们不会被分离.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body1 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 初身分别. |
| body2 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 第二身分别. |
| overlapOnly | boolean | 否 | 如果`true`,则两具尸体只能有重叠的数据集,不会进行分离. |
| bias | number | 否 | 重复检查时添加三角洲值的值。 用于防止图示隧道的挖掘 。 |
| overlap | number | 是 | 如果给出了, 此值将被用作重叠, 并且不会运行检查 。 |


**返回值:** boolean - `true` 如果两个机构垂直重叠,否则 `false`.


> 源码：[src/physics/arcade/SeparateY.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/SeparateY.js#L10)  
引入版本：3.0.0


---

### SetCollisionObject {#SetCollisionObject}

#### \<static> SetCollisionObject(noneFlip, [data]) {#static-setcollisionobjectnoneflip-data}


**说明:**

设置或创建弧形体碰撞对象 。

设定 `none` 属性的值 `noneFlip`时 `noneFlip` 谓 `false`,所有四个方向旗(`up`, `down`, `left`, `right`) 设置为 `true`,表示四面碰撞。 `noneFlip` 谓 `true`,所有方向旗帜都设置为 `false`.

大部分只使用内部。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| noneFlip | boolean | 否 | `none`属性的指定值。当 `false` 启用时,所有方向碰撞标记都启用 。 |
| data | [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](/api/typedef/types-physics-arcade#arcadebodycollision) | 是 | 碰撞数据对象为充值,或者如果未给出则创建。 |


**返回值:** [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](/api/typedef/types-physics-arcade#arcadebodycollision) - 碰撞数据。


> 源码：[src/physics/arcade/SetCollisionObject.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/SetCollisionObject.js#L7)  
引入版本：3.70.0


---

---
