# Phaser.Physics.Arcade.ProcessX {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-processx)

Scope: 
static
> 源码：[src/physics/arcade/ProcessX.js#L418](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessX.js#L418)  


## 静态函数 {#static-functions}

### BlockCheck {#BlockCheck}

#### \<static> BlockCheck() {#static-blockcheck}


**说明:**

检查其中任一物理体是否在旅行方向被阻挡,如果是的话,则将撞击速度完全应用到移动物理体,并返回被阻挡状态。被阻挡的物理体无论是否可推,都不能进一步分离。


**返回值:** number - 块检查结果. 0 = 未封堵 1 = 体 1 被封堵 2 = 体 2 被封堵.


> 源码：[src/physics/arcade/ProcessX.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessX.js#L71)  
引入版本：3.50.0


---

### Check {#Check}

#### \<static> Check() {#static-check}


**说明:**

计算两个机体的质量调整撞击速度,然后确定四种横向碰撞情景中哪一种适用(机体1或机体2向左或右移动到另一个机体),代表器为`Run`,并具有相应的侧值.


**返回值:** boolean - 如果支票通过,则`true`,否则,`false`。


> 源码：[src/physics/arcade/ProcessX.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessX.js#L119)  
引入版本：3.50.0


---

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


---

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


---

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


---

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


---

---
