# Collider {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-arcade-collider)

弧形物理对撞器会自动检查每个步骤两个对象之间的碰撞,或重叠。如果发生碰撞,或重叠,它会引用给定的回调。

注意, 如果将 `overlapOnly` 设置为 `true`, 而其中一个物体是 `TilemapLayer`, 则将检查层中的每个瓦片, 不论瓦片的ID 是否发生碰撞。 即使层中只允许有子集的瓦片ID 来进行碰撞, 仍然会检查所有瓦片的重叠 。

**构造函数**

`new Collider(world, overlapOnly, object1, object2, collideCallback, processCallback, callbackContext)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| world | [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) | 否 | 将管理碰撞的拱廊物理世界. |
| overlapOnly | boolean | 否 | 是否检查碰撞或重叠 。 |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第一个检查碰撞的物体 。 |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第二个检查碰撞的物体 。 |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 否 | 当两个物体碰撞时,调用符来引用. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 否 | 碰撞处理发生前的调用。 如果返回 `false`, 则该对碰撞或重叠被跳过 。 |
| callbackContext | any | 否 | 呼叫回调的范围。 |

---


**作用域**: static

> 源码：[src/physics/arcade/Collider.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Collider.js#L9)  
引入版本：3.0.0

## 公开成员 {#public-members}

### active {#active}

#### active: boolean {#active-boolean}


**说明:**

是否对撞机活动 。


> 源码：[src/physics/arcade/Collider.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Collider.js#L54)  
引入版本：3.0.0


---

### callbackContext {#callbackContext}

#### callbackContext: object {#callbackcontext-object}


**说明:**

上下文的collideCallback和processCallback将运行在其中.


> 源码：[src/physics/arcade/Collider.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Collider.js#L109)  
引入版本：3.0.0


---

### collideCallback {#collideCallback}

#### collideCallback: [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) {#collidecallback-phasertypesphysicsarcadearcadephysicscallback}


**说明:**

当两个物体碰撞时,调用符来引用.


> 源码：[src/physics/arcade/Collider.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Collider.js#L91)  
引入版本：3.0.0


---

### name {#name}

#### name: string {#name-string}


**说明:**

拼接机的名称(未使用Phaser).


> 源码：[src/physics/arcade/Collider.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Collider.js#L45)  
引入版本：3.1.0


---

### object1 {#object1}

#### object1: [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) {#object1-phasertypesphysicsarcadearcadecollidertype}


**说明:**

第一个检查碰撞的物体 。


> 源码：[src/physics/arcade/Collider.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Collider.js#L73)  
引入版本：3.0.0


---

### object2 {#object2}

#### object2: [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) {#object2-phasertypesphysicsarcadearcadecollidertype}


**说明:**

第二个检查碰撞的物体 。


> 源码：[src/physics/arcade/Collider.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Collider.js#L82)  
引入版本：3.0.0


---

### overlapOnly {#overlapOnly}

#### overlapOnly: boolean {#overlaponly-boolean}


**说明:**

是否检查碰撞或重叠 。


> 源码：[src/physics/arcade/Collider.js#L64](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Collider.js#L64)  
引入版本：3.0.0


---

### processCallback {#processCallback}

#### processCallback: [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) {#processcallback-phasertypesphysicsarcadearcadephysicscallback}


**说明:**

如果存在processCallback,它必须返回真实,否则碰撞检查会被跳过.


> 源码：[src/physics/arcade/Collider.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Collider.js#L100)  
引入版本：3.0.0


---

### world {#world}

#### world: [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) {#world-phaserphysicsarcadeworld}


**说明:**

身体会碰撞的世界


> 源码：[src/physics/arcade/Collider.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Collider.js#L36)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

从世界中删除对撞机并处理其资源.


> 源码：[src/physics/arcade/Collider.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Collider.js#L156)  
引入版本：3.0.0


---

### setName {#setName}

#### \<instance> setName(name) {#instance-setnamename}


**说明:**

指对撞车的名字

Phaser没有使用这个值,这是为你自己参考.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 指定对撞机的名称 。 |


**返回值:** [Phaser.Physics.Arcade.Collider](/api/class/physics-arcade-collider) - 这个对撞机的例子。


> 源码：[src/physics/arcade/Collider.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Collider.js#L119)  
引入版本：3.1.0


---

### update {#update}

#### \<instance> update() {#instance-update}


**说明:**

由Arcade Physics World在步骤中自动调用,进行两个已注册对象之间的碰撞或重叠检查,并引用适当的回调.


> 源码：[src/physics/arcade/Collider.js#L138](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Collider.js#L138)  
引入版本：3.0.0


---

---
