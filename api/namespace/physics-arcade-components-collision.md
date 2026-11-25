# Phaser.Physics.Arcade.Components.Collision {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-components-collision)

Scope: 
static
> 源码：[src/physics/arcade/components/Collision.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Collision.js#L9)  
引入版本：3.70.0

## 静态函数 {#static-functions}

### addCollidesWith {#addCollidesWith}

#### \<instance> addCollidesWith(category) {#instance-addcollideswithcategory}


**说明:**

将给定的碰撞类添加到此Arcade 物理体会与之碰撞的列表中.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| category | number | 否 | 加入这个物理体的碰撞遮罩的碰撞类别. |


**返回值:** [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Collision.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Collision.js#L65)  
引入版本：3.70.0


---

### removeCollidesWith {#removeCollidesWith}

#### \<instance> removeCollidesWith(category) {#instance-removecollideswithcategory}


**说明:**

从此Arcade 物理体会与之碰撞的列表中删除给定的碰撞类。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| category | number | 否 | 从这个物理体的碰撞遮罩中移除碰撞的类别. |


**返回值:** [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Collision.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Collision.js#L85)  
引入版本：3.70.0


---

### resetCollisionCategory {#resetCollisionCategory}

#### \<instance> resetCollisionCategory() {#instance-resetcollisioncategory}


**说明:**

将碰撞类和遮罩类重新放回默认,这意味着物理体将属于1类,并将与所有其他类别相撞.


**返回值:** [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Collision.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Collision.js#L135)  
引入版本：3.70.0


---

### setCollidesWith {#setCollidesWith}

#### \<instance> setCollidesWith(categories) {#instance-setcollideswithcategories}


**说明:**

设置此Arcade 物理体将与之碰撞的所有碰撞类别。 您可以通过一个单一的类别值, 或者通过其中的数组 。

调用这种方法会重置所有碰撞类别,所以只有传入这种方法的才启用.

如果您想要在现有遮罩中添加一个新类别,请拨打`addCollidesWith`方法.

如果要重设碰撞类别和遮罩,请拨打`resetCollisionCategory`方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| categories | number \| Array.\<number> | 否 | 与它们碰撞的碰撞类别,或其中的一组。 |


**返回值:** [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Collision.js#L105](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Collision.js#L105)  
引入版本：3.70.0


---

### setCollisionCategory {#setCollisionCategory}

#### \<instance> setCollisionCategory(category) {#instance-setcollisioncategorycategory}


**说明:**

设定此Arcade 物理体将使用的碰撞类,以确定它能与什么碰撞.

它只能有一个单一的类别被指定给它.

如果要重设碰撞类别和遮罩,请拨打`resetCollisionCategory`方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| category | number | 否 | 通常为2,如1,2,4,8等 |


**返回值:** [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Collision.js#L22](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Collision.js#L22)  
引入版本：3.70.0


---

### willCollideWith {#willCollideWith}

#### \<instance> willCollideWith(category) {#instance-willcollidewithcategory}


**说明:**

检查是否指定碰撞类与这个Arcade 物理对象相撞 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| category | number | 否 | 碰撞类值要测试 。 |


**返回值:** boolean - 如果给定的类别与此对象相撞,则`true`,否则则`false`.


> 源码：[src/physics/arcade/components/Collision.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Collision.js#L47)  
引入版本：3.70.0


---

---
