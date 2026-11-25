# Phaser.Physics.Arcade.Components {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/function/physics)

### OverlapCirc {#OverlapCirc}

#### \<static> OverlapCirc(world, x, y, radius, [includeDynamic], [includeStatic]) {#static-overlapcircworld-x-y-radius-includedynamic-includestatic}


**说明:**

这种方法将搜索给定的圆形区域,并返回所有与之重叠的物理体的阵列。它可以返回动态、静态体或两者的混合体。

尸体只需与要考虑的搜索区域相交,不需要完全控制在其中.

如果设定使用RTree(默认为RTree),那么搜索速度相当快,否则搜索是O(N)的动态天体.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| world | [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) | 否 |  | 拱廊物理世界. |
| x | number | 否 |  | 区域中心的x坐标以像素为单位进行内部搜索. |
| y | number | 否 |  | 区域中心的y坐标以像素为单位进行内部搜索。 |
| radius | number | 否 |  | 搜索区域半径在内部,以像素表示. |
| includeDynamic | boolean | 是 | true | 搜索中是否应该包括动态天体? |
| includeStatic | boolean | 是 | false | 搜索内容应该包括静态尸体吗? |


**返回值:** Array.\<[Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body)>, Array.\<[Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody)> - 一系列与指定区域重叠的天体.


> 源码：[src/physics/arcade/components/OverlapCirc.js#L6](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/OverlapCirc.js#L6)  
引入版本：3.21.0


### OverlapRect {#OverlapRect}

#### \<static> OverlapRect(world, x, y, width, height, [includeDynamic], [includeStatic]) {#static-overlaprectworld-x-y-width-height-includedynamic-includestatic}


**说明:**

这种方法将搜索给定的矩形区域,并返回所有与它重叠的物理体的阵列。它可以返回动态、静态体或两者的混合体。

尸体只需与要考虑的搜索区域相交,不需要完全控制在其中.

如果设定使用RTree(默认为RTree),那么搜索速度极快,否则搜索是O(N)的动态天体.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| world | [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) | 否 |  | 拱廊物理世界. |
| x | number | 否 |  | 左上方的x坐标 搜索区域内部。 |
| y | number | 否 |  | 左上方的坐标 搜索区域内部。 |
| width | number | 否 |  | 搜索区域宽度 。 |
| height | number | 否 |  | 搜索区域高度 |
| includeDynamic | boolean | 是 | true | 搜索中是否应该包括动态天体? |
| includeStatic | boolean | 是 | false | 搜索内容应该包括静态尸体吗? |


**返回值:** Array.\<[Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body)>, Array.\<[Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody)> - 一系列与指定区域重叠的天体.


> 源码：[src/physics/arcade/components/OverlapRect.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/OverlapRect.js#L1)  
引入版本：3.17.0


# Phaser.Physics.Arcade {#page-title-1}

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


# Phaser.Physics.Arcade.ProcessX {#page-title-2}

### Set {#Set}

#### \<static> Set(b1, b2, ov) {#static-setb1-b2-ov}


**说明:**

设置所有本地处理值,并计算速度交换。

然后运行 `BlockCheck`,并返回它的值.

这种方法由`Phaser.Physics.Arcade.SeparateX`称呼,不应直接称呼.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| b1 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 初身分别. |
| b2 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 第二身分别. |
| ov | number | 否 | 重叠值。 |


**返回值:** number - 块检查结果. 0 = 未封堵 1 = 体 1 被封堵 2 = 体 2 被封堵.


> 源码：[src/physics/arcade/ProcessX.js#L25](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessX.js#L25)  
引入版本：3.50.0


### BlockCheck {#BlockCheck}

#### \<static> BlockCheck() {#static-blockcheck}


**说明:**

检查其中任一天体是否在旅行方向被阻挡,如果是的话,则将撞击速度完全应用到移动天体,并返回被阻挡状态。被阻挡的天体无论是否可推,都不能进一步分离。


**返回值:** number - 块检查结果. 0 = 未封堵 1 = 体 1 被封堵 2 = 体 2 被封堵.


> 源码：[src/physics/arcade/ProcessX.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessX.js#L71)  
引入版本：3.50.0


### Check {#Check}

#### \<static> Check() {#static-check}


**说明:**

计算两个机体的质量调整撞击速度,然后确定四种横向碰撞情景中哪一种适用(机体1或机体2向左或右移动到另一个机体),代表器为`Run`,并具有相应的侧值.


**返回值:** boolean - 如果支票通过,则`true`,否则,`false`。


> 源码：[src/physics/arcade/ProcessX.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessX.js#L119)  
引入版本：3.50.0


### Run {#Run}

#### \<static> Run(side) {#static-runside}


**说明:**

执行两体在`Check`确定的碰撞侧面基础上的水平分离和速度交换. 处理所有可推力和非可推力的机体的组合:既可推力(等量反弹),只可推力(完全撞击适用于可推力机体),又不能推力(重叠分裂基于运动方向和相对速度).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| side | number | 否 | 测试的侧面,通过`Check`功能传递. |


**返回值:** boolean - 总是返回 `true`。


> 源码：[src/physics/arcade/ProcessX.js#L172](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessX.js#L172)  
引入版本：3.50.0


### RunImmovableBody1 {#RunImmovableBody1}

#### \<static> RunImmovableBody1(blockedState) {#static-runimmovablebody1blockedstate}


**说明:**

当Body1是不可移动的,Body2不是时处理水平分离. 将Body2从重叠中推出,并应用全部撞击速度来进行它. 如果Body1是一个移动平台(即`body1.moves`是`true`),Body2的垂直位置也使用Body1的垂直摩擦来调整,使Body2可以和平台一起搭乘.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| blockedState | number | 否 | 块态值 。 |


> 源码：[src/physics/arcade/ProcessX.js#L338](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessX.js#L338)  
引入版本：3.50.0


### RunImmovableBody2 {#RunImmovableBody2}

#### \<static> RunImmovableBody2(blockedState) {#static-runimmovablebody2blockedstate}


**说明:**

当Body2是不可移动时处理水平分离,而Body1不是. 将Body1从重叠中推出,并应用全部撞击速度来达到它. 如果Body2是一个移动平台(即. `body2.moves` 谓 `true`),Bodd1的垂直位置也使用Bodd2的垂直摩擦来调整,使Bodd1可以随月台一同搭乘.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| blockedState | number | 否 | 块态值 。 |


> 源码：[src/physics/arcade/ProcessX.js#L378](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessX.js#L378)  
引入版本：3.50.0


# Phaser.Physics.Arcade.ProcessY {#page-title-3}

### Set {#Set-1}

#### \<static> Set(b1, b2, ov) {#static-setb1-b2-ov-1}


**说明:**

设置所有本地处理值,并计算速度交换。

然后运行 `BlockCheck`,并返回它的值.

这种方法由`Phaser.Physics.Arcade.SeparateY`称呼,不应直接称呼.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| b1 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 初身分别. |
| b2 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 第二身分别. |
| ov | number | 否 | 重叠值。 |


**返回值:** number - 块检查结果. 0 = 未封堵 1 = 体 1 被封堵 2 = 体 2 被封堵.


> 源码：[src/physics/arcade/ProcessY.js#L25](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessY.js#L25)  
引入版本：3.50.0


### BlockCheck {#BlockCheck-1}

#### \<static> BlockCheck() {#static-blockcheck-1}


**说明:**

被封堵的方向检查,因为一个物体能否被推动并不重要,被封堵被封堵.


**返回值:** number - 块检查结果. 0 = 未封堵 1 = 体 1 被封堵 2 = 体 2 被封堵.


> 源码：[src/physics/arcade/ProcessY.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessY.js#L71)  
引入版本：3.50.0


### Check {#Check-1}

#### \<static> Check() {#static-check-1}


**说明:**

主检查功能。 运行于四个可能测试中的一项并返回结果 。


**返回值:** boolean - 如果支票通过,则`true`,否则,`false`。


> 源码：[src/physics/arcade/ProcessY.js#L118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessY.js#L118)  
引入版本：3.50.0


### Run {#Run-1}

#### \<static> Run(side) {#static-runside-1}


**说明:**

执行两体的垂直分离和速度交换,根据`Check`函数确定的碰撞侧面,处理所有可推力和非推力的机体组合,分配重叠,并相应重新计算后碰撞速度.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| side | number | 否 | 测试的侧面,通过`Check`功能传递. |


**返回值:** boolean - 总是返回 `true`。


> 源码：[src/physics/arcade/ProcessY.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessY.js#L169)  
引入版本：3.50.0


### RunImmovableBody1 {#RunImmovableBody1-1}

#### \<static> RunImmovableBody1(blockedState) {#static-runimmovablebody1blockedstate-1}


**说明:**

当 Body1 不可移动,而 Body2 则不是时,此函数会运行 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| blockedState | number | 否 | 块态值 。 |


> 源码：[src/physics/arcade/ProcessY.js#L334](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessY.js#L334)  
引入版本：3.50.0


### RunImmovableBody2 {#RunImmovableBody2-1}

#### \<static> RunImmovableBody2(blockedState) {#static-runimmovablebody2blockedstate-1}


**说明:**

当 Body2 是不可移动的,而Body1 则不是时,此函数会运行.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| blockedState | number | 否 | 块态值 。 |


> 源码：[src/physics/arcade/ProcessY.js#L370](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessY.js#L370)  
引入版本：3.50.0


# Phaser.Physics.Arcade.Tilemap {#page-title-4}

### ProcessTileCallbacks {#ProcessTileCallbacks}

#### \<static> ProcessTileCallbacks(tile, sprite) {#static-processtilecallbackstile-sprite}


**说明:**

检查是否为给定的牌盘注册了每瓦或每瓦索引的碰撞调用,如果是的话,则引用它与碰撞的游戏对象。 调用级别调用( 直接设置在牌盘上) 优先于层层调用( 以牌盘指数设置在牌盘层上 ) 。 如果调用返回 `true` , 则碰撞被否决, 此函数返回 `false` , 以跳过此对子的进一步处理。 如果没有注册调用, 此函数返回 `true`, 从而继续正常的 Arcade 物理碰撞分辨率 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tile | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 处理的拖车。 |
| sprite | [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) | 否 | 使用 Tile 处理的游戏对象 。 |


**返回值:** boolean - 如果继续处理这种瓦片/成片的碰撞,则`true`;如果回调否决碰撞,则`false`。


> 源码：[src/physics/arcade/tilemap/ProcessTileCallbacks.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/ProcessTileCallbacks.js#L7)  
引入版本：3.0.0


### ProcessTileSeparationX {#ProcessTileSeparationX}

#### \<static> ProcessTileSeparationX(body, x) {#static-processtileseparationxbody-x}


**说明:**

处理物理体与瓦片横向分离的内部功能,它根据分离方向更新身体的左或右屏蔽旗,按照分离量沿X轴移动身体,更新其中心,然后或者根据身体的弹跳系数将水平速度零化或者应用弹跳.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 身体反对分开。 |
| x | number | 否 | x轴分离距离, 以像素为单位。 一个负值表示身体被屏蔽在左侧; 一个正值表示它被屏蔽在右侧。 |


> 源码：[src/physics/arcade/tilemap/ProcessTileSeparationX.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/ProcessTileSeparationX.js#L7)  
引入版本：3.0.0


### ProcessTileSeparationY {#ProcessTileSeparationY}

#### \<static> ProcessTileSeparationY(body, y) {#static-processtileseparationybody-y}


**说明:**

内部功能处理物理体与瓷砖的垂直分离.

更新身体的屏蔽旗,根据分离方向,按照分离量调整身体的垂直位置,然后或者将垂直速度零化,或者应用身体的弹跳因子来逆向.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 身体反对分开。 |
| y | number | 否 | 垂直分离量, 以像素为单位。 一个负值表示身体被上面屏蔽; 一个正值表示它被下面屏蔽 。 |


> 源码：[src/physics/arcade/tilemap/ProcessTileSeparationY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/ProcessTileSeparationY.js#L7)  
引入版本：3.0.0


### SeparateTile {#SeparateTile}

#### \<static> SeparateTile(i, body, tile, tileWorldRect, tilemapLayer, tileBias, isLayer) {#static-separatetilei-body-tile-tileworldrect-tilemaplayer-tilebias-islayer}


**说明:**

将物理体与瓦片分开,解决它们之间的任何重叠。它决定了哪个轴首先根据天体的当前速度处理:如果天体横向移动更快,则首先检查X轴,反之亦然。当将两轴上相撞面的对角移入瓦片时,优先处理最小重叠的轴。分离时,酌情调用`TileCheckX`和/或`TileCheckY`,如果第一个轴分离足以完全解决交叉,则提前调用短路。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| i | number | 否 | 地图数据中的瓦片索引 。 |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 身体反对分开。 |
| tile | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 瓦片可以碰撞对战. |
| tileWorldRect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形物体定义瓦片的尺寸。 |
| tilemapLayer | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 否 | The tilemapLayer to collide against. |
| tileBias | number | 否 | 瓦片偏移值,由`World.TILE_BIAS`常数定义,用于防止快速移动的机体通过薄的瓦片进行隧道通路. |
| isLayer | boolean | 否 | 这是来自TilemapLayer的支票还是一系列的瓷砖? |


**返回值:** boolean - 如果尸体分开的话,就用`true`,否则用`false`.


> 源码：[src/physics/arcade/tilemap/SeparateTile.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/SeparateTile.js#L11)  
引入版本：3.0.0


### TileCheckX {#TileCheckX}

#### \<static> TileCheckX(body, tile, tileLeft, tileRight, tileBias, isLayer) {#static-tilecheckxbody-tile-tileleft-tileright-tilebias-islayer}


**说明:**

检查给定物理体与 X 轴上的瓦片, 计算重叠值, 并在发现碰撞时应用分离。 当检查来源于 TilemapLayer 时, 尊重瓦片的面部和碰撞标记, 并发送到 `ProcessTileSeparationX`( 或者在启用 `customSeparateX` 时设置 `body.overlapX`) 。 由 Exploy 函数在内部使用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 身体反对分开。 |
| tile | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 瓦片来检查。 |
| tileLeft | number | 否 | 在世界坐标的瓦片的左边缘,以像素表示. |
| tileRight | number | 否 | 世界坐标的瓦片的右边缘,以像素表示. |
| tileBias | number | 否 | 瓦片偏移值。 重叠大于此阈值会被忽略以防止隧道通透。 通常设置为 `World.TILE_BIAS` 。 |
| isLayer | boolean | 否 | 这是来自TilemapLayer的支票还是一系列的瓷砖? |


**返回值:** number - 发生的分离量。


> 源码：[src/physics/arcade/tilemap/TileCheckX.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/TileCheckX.js#L9)  
引入版本：3.0.0


### TileCheckY {#TileCheckY}

#### \<static> TileCheckY(body, tile, tileTop, tileBottom, tileBias, isLayer) {#static-tilecheckybody-tile-tiletop-tilebottom-tilebias-islayer}


**说明:**

检查物理体与Y轴上的瓦片之间的重叠,并解决任何发现的碰撞。如果天体有自定义的分隔符设置,重叠值将存储在`body.overlapY`上,供呼叫者处理;否则,`ProcessTileSeparationY`会被调用以立即解决碰撞。由SollectTile函数在内部使用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 身体反对分开。 |
| tile | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 瓦片来检查。 |
| tileTop | number | 否 | 瓦片在世界空间的顶部位置,以像素表示. |
| tileBottom | number | 否 | 瓦片在世界空间的底部位置,以像素表示. |
| tileBias | number | 否 | 瓦片偏移值,由`World.TILE_BIAS`常数定义. |
| isLayer | boolean | 否 | 这是来自TilemapLayer的支票还是一系列的瓷砖? |


**返回值:** number - 发生的垂直分离量,以像素计.


> 源码：[src/physics/arcade/tilemap/TileCheckY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/TileCheckY.js#L9)  
引入版本：3.0.0


### TileIntersectsBody {#TileIntersectsBody}

#### \<static> TileIntersectsBody(tileWorldRect, body) {#static-tileintersectsbodytileworldrect-body}


**说明:**

检查给定的瓷砖矩形物体与弧形物理体之间的交叉点.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileWorldRect | Object | 否 | 定义世界瓷砖放置的矩形对象. |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 检查与交叉点的车体 |


**返回值:** boolean - 如果瓦片与机体相交,则返回`true`,否则返回`false`.


> 源码：[src/physics/arcade/tilemap/TileIntersectsBody.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/TileIntersectsBody.js#L7)  
引入版本：3.0.0


# Phaser.Physics.Matter {#page-title-5}

### MatterGameObject {#MatterGameObject}

#### \<static> MatterGameObject(world, gameObject, [options], [addToWorld]) {#static-mattergameobjectworld-gameobject-options-addtoworld}


**说明:**

将所有 Matter.js 物理组件混合到任何现有的 Phaser 游戏对象,包括您自己扩展或创建的游戏对象的工厂函数。这使得您能够给任何游戏对象完全的 Matter 物理能力,而无需它扩展特定类。

以下组件直接混合到游戏对象上: 弹跳、 碰撞、 强制、 硬盘、 重力、 质量、 感应器、 秒拍、 睡眠、 静态、 变形和 速度。 这意味着在调用此功能后, `setVelocity`、 `setFriction` 和 `isSensor` 等方法可以直接在游戏对象上使用 。

如果 `options`是现有的物质体实例(即它的 `type`属性等于 `'body'`),则通过 `setExistingBody` 来附加该天体,否则, `options` 被作为 `MatterBodyConfig` 处理,并通过 `setBody` 创建新天体,如果不提供 `shape`属性,则默认为矩形.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| world | [Phaser.Physics.Matter.World](/api/class/physics-matter-world) | 否 |  | 物质世界来增加身体。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将应用物质对象的游戏对象 。 |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) \| MatterJS.Body | 是 |  | 物质体的配置对象, 或物质体的示例 。 |
| addToWorld | boolean | 是 | true | 刚刚创建的机构应该立即加入世界吗? |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 游戏对象被传递,现在用物质物理组件增强.


> 源码：[src/physics/matter-js/MatterGameObject.js#L26](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterGameObject.js#L26)  
引入版本：3.3.0


# Phaser.Physics.Matter.PhysicsEditorParser {#page-title-6}

### parseBody {#parseBody}

#### \<static> parseBody(x, y, config, [options]) {#static-parsebodyx-y-config-options}


**说明:**

解析物理编辑器导出的身体配置,并从中创建复合 Matter.js body。组合中的每个固定定义都被解析并转换成一个儿童身体(圆形或凸起多边形),所有儿童身体被组合成一个位于指定世界坐标的单一复合体。额外的 Matter.j 身体属性可以通过`options`参数提供,并将合并到身体配置中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 身体的横向世界位置. |
| y | number | 否 | 身体的垂直世界位置. |
| config | object | 否 | 物理编辑器导出的身体配置和固定(儿童身体)定义。 |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** MatterJS.BodyType - 复合物 物质JS体。


> 源码：[src/physics/matter-js/PhysicsEditorParser.js#L29](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PhysicsEditorParser.js#L29)  
引入版本：3.10.0


### parseFixture {#parseFixture}

#### \<static> parseFixture(fixtureConfig) {#static-parsefixturefixtureconfig}


**说明:**

从物理编辑器导出的“固定”列表中解析一个单个固定条目。固定选项可以描述圆(由中心位置和半径定义)或一组凸起多边形顶点列表。适当的 Matter.js 的机体或机体被创建并作为数组返回,以便由调用器将它们组合成复合机体。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| fixtureConfig | object | 否 | 固定对象来分析。 |


**返回值:** Array.\<MatterJS.BodyType> - - 一系列物质JS机构。


> 源码：[src/physics/matter-js/PhysicsEditorParser.js#L79](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PhysicsEditorParser.js#L79)  
引入版本：3.10.0


### parseVertices {#parseVertices}

#### \<static> parseVertices(vertexSets, [options]) {#static-parseverticesvertexsets-options}


**说明:**

解析物理编辑器导出的一个或多个顶点设置,并为每个集合创建 Matter.js 天体。在创建每个天体之前,顶点按顺时针风向顺序排序,并且将天体定位在顶点设置的中间体。在所有天体创建后,标记相邻部分之间的巧合边缘,以便 Matter.j在碰撞探测时正确处理它们。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vertexSets | array | 否 | 顶点列表来分析. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** Array.\<MatterJS.BodyType> - - 一系列物质JS机构。


> 源码：[src/physics/matter-js/PhysicsEditorParser.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PhysicsEditorParser.js#L116)  
引入版本：3.10.0


# Phaser.Physics.Matter.PhysicsJSONParser {#page-title-7}

### parseBody {#parseBody-1}

#### \<static> parseBody(x, y, config, [options]) {#static-parsebodyx-y-config-options-1}


**说明:**

从给定的JSON数据中分析一个天体元素.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 身体的横向世界位置. |
| y | number | 否 | 身体的垂直世界位置. |
| config | object | 否 | 体型配置数据. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** MatterJS.BodyType - 联合来文机构。


> 源码：[src/physics/matter-js/PhysicsJSONParser.js#L53](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PhysicsJSONParser.js#L53)  
引入版本：3.22.0

---
