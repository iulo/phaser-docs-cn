# StaticGroup {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-arcade-staticgroup)

拱廊物理静态组对象.

静态组是一个游戏对象的容器,每个物体都有静态的弧形物理体。静态体固定在原位,从不因速度、重力或碰撞而移动。它们对于平台、墙壁、地板和其他不可移动的障碍等水平几何来说是理想的。 由于其位置在游戏游戏中从未改变,因此它们比动态体更能发挥这种作用。

如果游戏对象还没有一个,则该组创建或添加的所有游戏对象将自动获得一个静态弧形物理体。如果添加了一个已经拥有动态体的游戏对象,则该体将被销毁,并被静态体所取代。

它的动态对应器是[Phaser.Physics.Arcade.Group](/api/class/physics-arcade-group).

**构造函数**

`new StaticGroup(world, scene, [children], [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| world | [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) | 否 | 物理模拟. |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 剧组所属的场景. |
| children | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> \| [Phaser.Types.GameObjects.Group.GroupConfig](/api/typedef/types-gameobjects-group#groupconfig) | [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) | 是 | 要添加到此组的游戏对象; 或 `config` 参数 。 |
| config | [Phaser.Types.GameObjects.Group.GroupConfig](/api/typedef/types-gameobjects-group#groupconfig) \| [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) | 是 | 此组的设置 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Group](/api/class/gameobjects-group)  
> [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision)  



> 源码：[src/physics/arcade/StaticPhysicsGroup.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticPhysicsGroup.js#L15)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Group](/api/class/gameobjects-group):**


 - [active](/api/class/gameobjects-group#active)
 - [children](/api/class/gameobjects-group#children)
 - [classType](/api/class/gameobjects-group#classType)
 - [createCallback](/api/class/gameobjects-group#createCallback)
 - [createMultipleCallback](/api/class/gameobjects-group#createMultipleCallback)
 - [defaultFrame](/api/class/gameobjects-group#defaultFrame)
 - [defaultKey](/api/class/gameobjects-group#defaultKey)
 - [isParent](/api/class/gameobjects-group#isParent)
 - [maxSize](/api/class/gameobjects-group#maxSize)
 - [name](/api/class/gameobjects-group#name)
 - [removeCallback](/api/class/gameobjects-group#removeCallback)
 - [runChildUpdate](/api/class/gameobjects-group#runChildUpdate)
 - [scene](/api/class/gameobjects-group#scene)




---

## 公开成员 {#public-members}

### collisionCategory {#collisionCategory}

#### collisionCategory: number {#collisioncategory-number}


**说明:**

拱廊物理静态组碰撞类.

它可以设置为任何有效的碰撞位域值 。

详见`setCollisionCategory`方法.


> 源码：[src/physics/arcade/StaticPhysicsGroup.js#L117](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticPhysicsGroup.js#L117)  
引入版本：3.70.0


---

### collisionMask {#collisionMask}

#### collisionMask: number {#collisionmask-number}


**说明:**

拱廊物理静态组碰撞罩.

详见`setCollidesWith`方法.


> 源码：[src/physics/arcade/StaticPhysicsGroup.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticPhysicsGroup.js#L130)  
引入版本：3.70.0


---

### physicsType {#physicsType}

#### physicsType: number {#physicstype-number}


**说明:**

分配给这个群体中孩子的物理体型.


> 源码：[src/physics/arcade/StaticPhysicsGroup.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticPhysicsGroup.js#L107)  
引入版本：3.0.0


---

### type {#type}

#### type: string {#type-string}


**说明:**

此游戏对象的文字表达。 内部由 Phaser 使用, 但可供您自定义的类使用 。


**Overrides:** Phaser.GameObjects.Group# 类型


> 源码：[src/physics/arcade/StaticPhysicsGroup.js#L143](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticPhysicsGroup.js#L143)  
引入版本：3.21.0


---

### world {#world}

#### world: [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) {#world-phaserphysicsarcadeworld}


**说明:**

物理模拟.


> 源码：[src/physics/arcade/StaticPhysicsGroup.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticPhysicsGroup.js#L98)  
引入版本：3.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Events.EventEmitter](/api/class/events-eventemitter):**


 - [addListener](/api/class/events-eventemitter#addListener)
 - [emit](/api/class/events-eventemitter#emit)
 - [eventNames](/api/class/events-eventemitter#eventNames)
 - [listenerCount](/api/class/events-eventemitter#listenerCount)
 - [listeners](/api/class/events-eventemitter#listeners)
 - [off](/api/class/events-eventemitter#off)
 - [on](/api/class/events-eventemitter#on)
 - [once](/api/class/events-eventemitter#once)
 - [removeAllListeners](/api/class/events-eventemitter#removeAllListeners)
 - [removeListener](/api/class/events-eventemitter#removeListener)
 - [shutdown](/api/class/events-eventemitter#shutdown)





**From [Phaser.GameObjects.Group](/api/class/gameobjects-group):**


 - [add](/api/class/gameobjects-group#add)
 - [addedToScene](/api/class/gameobjects-group#addedToScene)
 - [addMultiple](/api/class/gameobjects-group#addMultiple)
 - [angle](/api/class/gameobjects-group#angle)
 - [clear](/api/class/gameobjects-group#clear)
 - [contains](/api/class/gameobjects-group#contains)
 - [countActive](/api/class/gameobjects-group#countActive)
 - [create](/api/class/gameobjects-group#create)
 - [createFromConfig](/api/class/gameobjects-group#createFromConfig)
 - [createMultiple](/api/class/gameobjects-group#createMultiple)
 - [destroy](/api/class/gameobjects-group#destroy)
 - [get](/api/class/gameobjects-group#get)
 - [getChildren](/api/class/gameobjects-group#getChildren)
 - [getFirst](/api/class/gameobjects-group#getFirst)
 - [getFirstAlive](/api/class/gameobjects-group#getFirstAlive)
 - [getFirstDead](/api/class/gameobjects-group#getFirstDead)
 - [getFirstNth](/api/class/gameobjects-group#getFirstNth)
 - [getLast](/api/class/gameobjects-group#getLast)
 - [getLastNth](/api/class/gameobjects-group#getLastNth)
 - [getLength](/api/class/gameobjects-group#getLength)
 - [getMatching](/api/class/gameobjects-group#getMatching)
 - [getTotalFree](/api/class/gameobjects-group#getTotalFree)
 - [getTotalUsed](/api/class/gameobjects-group#getTotalUsed)
 - [incX](/api/class/gameobjects-group#incX)
 - [incXY](/api/class/gameobjects-group#incXY)
 - [incY](/api/class/gameobjects-group#incY)
 - [isFull](/api/class/gameobjects-group#isFull)
 - [kill](/api/class/gameobjects-group#kill)
 - [killAndHide](/api/class/gameobjects-group#killAndHide)
 - [playAnimation](/api/class/gameobjects-group#playAnimation)
 - [preUpdate](/api/class/gameobjects-group#preUpdate)
 - [propertyValueInc](/api/class/gameobjects-group#propertyValueInc)
 - [propertyValueSet](/api/class/gameobjects-group#propertyValueSet)
 - [remove](/api/class/gameobjects-group#remove)
 - [removedFromScene](/api/class/gameobjects-group#removedFromScene)
 - [rotate](/api/class/gameobjects-group#rotate)
 - [rotateAround](/api/class/gameobjects-group#rotateAround)
 - [rotateAroundDistance](/api/class/gameobjects-group#rotateAroundDistance)
 - [scaleX](/api/class/gameobjects-group#scaleX)
 - [scaleXY](/api/class/gameobjects-group#scaleXY)
 - [scaleY](/api/class/gameobjects-group#scaleY)
 - [setActive](/api/class/gameobjects-group#setActive)
 - [setAlpha](/api/class/gameobjects-group#setAlpha)
 - [setBlendMode](/api/class/gameobjects-group#setBlendMode)
 - [setDepth](/api/class/gameobjects-group#setDepth)
 - [setHitArea](/api/class/gameobjects-group#setHitArea)
 - [setName](/api/class/gameobjects-group#setName)
 - [setOrigin](/api/class/gameobjects-group#setOrigin)
 - [setTint](/api/class/gameobjects-group#setTint)
 - [setVisible](/api/class/gameobjects-group#setVisible)
 - [setX](/api/class/gameobjects-group#setX)
 - [setXY](/api/class/gameobjects-group#setXY)
 - [setY](/api/class/gameobjects-group#setY)
 - [shiftPosition](/api/class/gameobjects-group#shiftPosition)
 - [shuffle](/api/class/gameobjects-group#shuffle)
 - [toggleVisible](/api/class/gameobjects-group#toggleVisible)





**From [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision):**


 - [addCollidesWith](/api/namespace/physics-arcade-components-collision#addCollidesWith)
 - [removeCollidesWith](/api/namespace/physics-arcade-components-collision#removeCollidesWith)
 - [resetCollisionCategory](/api/namespace/physics-arcade-components-collision#resetCollisionCategory)
 - [setCollidesWith](/api/namespace/physics-arcade-components-collision#setCollidesWith)
 - [setCollisionCategory](/api/namespace/physics-arcade-components-collision#setCollisionCategory)
 - [willCollideWith](/api/namespace/physics-arcade-components-collision#willCollideWith)




---

## 公开方法 {#public-methods}

### createCallbackHandler {#createCallbackHandler}

#### \<instance> createCallbackHandler(child) {#instance-createcallbackhandlerchild}


**说明:**

将静态物理体添加到新的组成员(如果缺少)中,并添加到模拟中.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 新组员. |


> 源码：[src/physics/arcade/StaticPhysicsGroup.js#L155](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticPhysicsGroup.js#L155)  
引入版本：3.0.0


---

### createMultipleCallbackHandler {#createMultipleCallbackHandler}

#### \<instance> createMultipleCallbackHandler(entries) {#instance-createmultiplecallbackhandlerentries}


**说明:**

多个组成员后引用的内部调用通过`createMultiple`同时创建. 呼叫[Phaser.Physics.Arcade.StaticGroup#refresh](/api/class/physics-arcade-staticgroup#refresh),以同步所有静态物理体与母游戏对象当前位置.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| entries | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 新成立的集团成员. |


> 源码：[src/physics/arcade/StaticPhysicsGroup.js#L197](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticPhysicsGroup.js#L197)  
引入版本：3.0.0


---

### refresh {#refresh}

#### \<instance> refresh() {#instance-refresh}


**说明:**

将本组中的每个静态物理体重置到其母游戏对象的当前位置。 手动调整任何成员的位置后调用此功能, 使其身体保持同步。 身体大小不会被这种方法所改变; 使用 [Phaser.Physics.Arcade.Components.Enable#refreshBody](/api/namespace/physics-arcade-components-enable#refreshBody)来调整一个天体的大小 。


**返回值:** [Phaser.Physics.Arcade.StaticGroup](/api/class/physics-arcade-staticgroup) - 这个团体。


> 源码：[src/physics/arcade/StaticPhysicsGroup.js#L214](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticPhysicsGroup.js#L214)  
引入版本：3.0.0


---

### removeCallbackHandler {#removeCallbackHandler}

#### \<instance> removeCallbackHandler(child) {#instance-removecallbackhandlerchild}


**说明:**

禁用组成员的物理体,将其从模拟中移除.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 集团成员被除名. |


> 源码：[src/physics/arcade/StaticPhysicsGroup.js#L179](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticPhysicsGroup.js#L179)  
引入版本：3.0.0


---

---
