# Group {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-arcade-group)

弧形物理组对象.

物理组的主要用途是收集物理驱动的物体,这些物体在同一个集合中具有相同的内在结构。然后可以很容易地与其他群,或者Game Objects进行比较。

本组创建或添加的所有游戏对象将自动获得**动力**弧形物理体(如果它们已经没有躯体),并且这些天体将获得Groups [default](/api/class/physics-arcade-group#defaults).

您不应该将对象传递到不应该接收到天体的组中。 例如, 不要将基本的几何或平面层添加到组中, 因为它们不会以您预期的方式行事。 组中最好都包含相同类型的对象 。

如果您想创建一个充满静态天体的团体,请参见[Phaser.Physics.Arcade.StaticGroup](/api/class/physics-arcade-staticgroup).

**构造函数**

`new Group(world, scene, [children], [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| world | [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) | 否 | 物理模拟. |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 剧组所属的场景. |
| children | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> \| [Phaser.Types.Physics.Arcade.PhysicsGroupConfig](/api/typedef/types-physics-arcade#physicsgroupconfig) | [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) | 是 | 要添加到此组的游戏对象; 或 `config` 参数 。 |
| config | [Phaser.Types.Physics.Arcade.PhysicsGroupConfig](/api/typedef/types-physics-arcade#physicsgroupconfig) \| [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) | 是 | 此组的设置 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Group](/api/class/gameobjects-group)  
> [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision)  



> 源码：[src/physics/arcade/PhysicsGroup.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/PhysicsGroup.js#L15)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Group](/api/class/gameobjects-group):**


 - [active](/api/class/gameobjects-group#active)
 - [children](/api/class/gameobjects-group#children)
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

### classType {#classType}

#### classType: function {#classtype-function}


**说明:**

创立新集团成员的班级从.

这应该是`Phaser.Physics.Arcade.Image`,`Phaser.Physics.Arcade.Sprite`,或者扩展其中一种的类.

构造器参数必须匹配 `(scene, x, y, texture, frame)` 。


**Overrides:** Phaser.GameObjects.Group#classType


> 源码：[src/physics/arcade/PhysicsGroup.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/PhysicsGroup.js#L106)  
引入版本：3.0.0


---

### collisionCategory {#collisionCategory}

#### collisionCategory: number {#collisioncategory-number}


**说明:**

拱廊物理组碰撞类.

它可以设置为任何有效的碰撞位域值 。

详见`setCollisionCategory`方法.


> 源码：[src/physics/arcade/PhysicsGroup.js#L134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/PhysicsGroup.js#L134)  
引入版本：3.70.0


---

### collisionMask {#collisionMask}

#### collisionMask: number {#collisionmask-number}


**说明:**

拱廊物理集团碰撞面具.

详见`setCollidesWith`方法.


> 源码：[src/physics/arcade/PhysicsGroup.js#L147](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/PhysicsGroup.js#L147)  
引入版本：3.70.0


---

### defaults {#defaults}

#### defaults: [Phaser.Types.Physics.Arcade.PhysicsGroupDefaults](/api/typedef/types-physics-arcade#physicsgroupdefaults) {#defaults-phasertypesphysicsarcadephysicsgroupdefaults}


**说明:**

默认物理属性适用于游戏对象添加到Group中或由Group创建. Delectived from the `config` 参数.

您可以通过设置此属性为 `{}` 来删除默认值 。


> 源码：[src/physics/arcade/PhysicsGroup.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/PhysicsGroup.js#L158)  
引入版本：3.0.0


---

### physicsType {#physicsType}

#### physicsType: number {#physicstype-number}


**说明:**

集团成员的物理类型.


> 源码：[src/physics/arcade/PhysicsGroup.js#L124](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/PhysicsGroup.js#L124)  
引入版本：3.0.0


---

### type {#type}

#### type: string {#type-string}


**说明:**

此游戏对象的文字表达。 内部由 Phaser 使用, 但可供您自定义的类使用 。


**Overrides:** Phaser.GameObjects.Group# 类型


> 源码：[src/physics/arcade/PhysicsGroup.js#L199](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/PhysicsGroup.js#L199)  
引入版本：3.21.0


---

### world {#world}

#### world: [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) {#world-phaserphysicsarcadeworld}


**说明:**

物理模拟.


> 源码：[src/physics/arcade/PhysicsGroup.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/PhysicsGroup.js#L97)  
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

启用游戏对象的天体,并指定 `defaults`。在添加或创建组成员时调用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 正在添加游戏对象 。 |


> 源码：[src/physics/arcade/PhysicsGroup.js#L211](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/PhysicsGroup.js#L211)  
引入版本：3.0.0


---

### removeCallbackHandler {#removeCallbackHandler}

#### \<instance> removeCallbackHandler(child) {#instance-removecallbackhandlerchild}


**说明:**

禁用游戏对象的身体。 取消组成员时会呼叫 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 正在删除游戏对象 。 |


> 源码：[src/physics/arcade/PhysicsGroup.js#L240](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/PhysicsGroup.js#L240)  
引入版本：3.0.0


---

### setVelocity {#setVelocity}

#### \<instance> setVelocity(x, y, [step]) {#instance-setvelocityx-y-step}


**说明:**

设定每个组成员的速度。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 水平速度,以像素每秒为单位. |
| y | number | 否 |  | 垂直速度,以像素每秒为单位. |
| step | number | 是 | 0 | 速度递增。设定时,第一个成员收到速度(x,y),第二个成员(x+步骤,y+步骤)等. |


**返回值:** [Phaser.Physics.Arcade.Group](/api/class/physics-arcade-group) - 此物理组对象 。


> 源码：[src/physics/arcade/PhysicsGroup.js#L256](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/PhysicsGroup.js#L256)  
引入版本：3.0.0


---

### setVelocityX {#setVelocityX}

#### \<instance> setVelocityX(value, [step]) {#instance-setvelocityxvalue-step}


**说明:**

设定每个组成员的横向速度。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 速度值,以像素每秒为单位. |
| step | number | 是 | 0 | 速度递增。设定时,第一个成员会收到速度(x),第二个成员(x+步骤)等. |


**返回值:** [Phaser.Physics.Arcade.Group](/api/class/physics-arcade-group) - 此物理组对象 。


> 源码：[src/physics/arcade/PhysicsGroup.js#L282](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/PhysicsGroup.js#L282)  
引入版本：3.0.0


---

### setVelocityY {#setVelocityY}

#### \<instance> setVelocityY(value, [step]) {#instance-setvelocityyvalue-step}


**说明:**

设置每个组成员的垂直速度。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 速度值,以像素每秒为单位. |
| step | number | 是 | 0 | 速度递增。设定时,第一个成员得到速度(y),第二个成员(y+步骤)等。 |


**返回值:** [Phaser.Physics.Arcade.Group](/api/class/physics-arcade-group) - 此物理组对象 。


> 源码：[src/physics/arcade/PhysicsGroup.js#L307](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/PhysicsGroup.js#L307)  
引入版本：3.0.0


---

---
