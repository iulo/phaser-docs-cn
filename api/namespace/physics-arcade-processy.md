# Phaser.Physics.Arcade.ProcessY {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-processy)

Scope: 
static
> 源码：[src/physics/arcade/ProcessY.js#L406](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessY.js#L406)  


## 静态函数 {#static-functions}

### BlockCheck {#BlockCheck}

#### \<static> BlockCheck() {#static-blockcheck}


**说明:**

被封堵的方向检查,因为一个物体能否被推动并不重要,被封堵被封堵.


**返回值:** number - 块检查结果. 0 = 未封堵 1 = 体 1 被封堵 2 = 体 2 被封堵.


> 源码：[src/physics/arcade/ProcessY.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessY.js#L71)  
引入版本：3.50.0


---

### Check {#Check}

#### \<static> Check() {#static-check}


**说明:**

主检查功能。 运行于四个可能测试中的一项并返回结果 。


**返回值:** boolean - 如果支票通过,则`true`,否则,`false`。


> 源码：[src/physics/arcade/ProcessY.js#L118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessY.js#L118)  
引入版本：3.50.0


---

### Run {#Run}

#### \<static> Run(side) {#static-runside}


**说明:**

执行两体的垂直分离和速度交换,根据`Check`函数确定的碰撞侧面,处理所有可推力和非推力的机体组合,分配重叠,并相应重新计算后碰撞速度.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| side | number | 否 | 测试的侧面,通过`Check`功能传递. |


**返回值:** boolean - 总是返回 `true`。


> 源码：[src/physics/arcade/ProcessY.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessY.js#L169)  
引入版本：3.50.0


---

### RunImmovableBody1 {#RunImmovableBody1}

#### \<static> RunImmovableBody1(blockedState) {#static-runimmovablebody1blockedstate}


**说明:**

当 Body1 不可移动,而 Body2 则不是时,此函数会运行 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| blockedState | number | 否 | 块态值 。 |


> 源码：[src/physics/arcade/ProcessY.js#L334](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessY.js#L334)  
引入版本：3.50.0


---

### RunImmovableBody2 {#RunImmovableBody2}

#### \<static> RunImmovableBody2(blockedState) {#static-runimmovablebody2blockedstate}


**说明:**

当 Body2 是不可移动的,而Body1 则不是时,此函数会运行.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| blockedState | number | 否 | 块态值 。 |


> 源码：[src/physics/arcade/ProcessY.js#L370](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ProcessY.js#L370)  
引入版本：3.50.0


---

### Set {#Set}

#### \<static> Set(b1, b2, ov) {#static-setb1-b2-ov}


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


---

---
