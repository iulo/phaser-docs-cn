# Phaser.Physics.Matter.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter-events)

Scope: 
static
> 源码：[src/physics/matter-js/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/index.js#L7)  


## 静态函数 {#static-functions}

### AfterAddEvent {#AfterAddEvent}

#### AfterAddEvent {#afteraddevent}


> 源码：[src/physics/matter-js/events/AFTER_ADD_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/AFTER_ADD_EVENT.js#L7)  



---

### AfterRemoveEvent {#AfterRemoveEvent}

#### AfterRemoveEvent {#afterremoveevent}


> 源码：[src/physics/matter-js/events/AFTER_REMOVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/AFTER_REMOVE_EVENT.js#L7)  



---

### AfterUpdateEvent {#AfterUpdateEvent}

#### AfterUpdateEvent {#afterupdateevent}


> 源码：[src/physics/matter-js/events/AFTER_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/AFTER_UPDATE_EVENT.js#L7)  



---

### BeforeAddEvent {#BeforeAddEvent}

#### BeforeAddEvent {#beforeaddevent}


> 源码：[src/physics/matter-js/events/BEFORE_ADD_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/BEFORE_ADD_EVENT.js#L7)  



---

### BeforeRemoveEvent {#BeforeRemoveEvent}

#### BeforeRemoveEvent {#beforeremoveevent}


> 源码：[src/physics/matter-js/events/BEFORE_REMOVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/BEFORE_REMOVE_EVENT.js#L7)  



---

### BeforeUpdateEvent {#BeforeUpdateEvent}

#### BeforeUpdateEvent {#beforeupdateevent}


> 源码：[src/physics/matter-js/events/BEFORE_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/BEFORE_UPDATE_EVENT.js#L7)  



---

### CollisionActiveEvent {#CollisionActiveEvent}

#### CollisionActiveEvent {#collisionactiveevent}


> 源码：[src/physics/matter-js/events/COLLISION_ACTIVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/COLLISION_ACTIVE_EVENT.js#L7)  



---

### CollisionEndEvent {#CollisionEndEvent}

#### CollisionEndEvent {#collisionendevent}


> 源码：[src/physics/matter-js/events/COLLISION_END_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/COLLISION_END_EVENT.js#L7)  



---

### CollisionStartEvent {#CollisionStartEvent}

#### CollisionStartEvent {#collisionstartevent}


> 源码：[src/physics/matter-js/events/COLLISION_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/COLLISION_START_EVENT.js#L7)  



---

### SleepEndEvent {#SleepEndEvent}

#### SleepEndEvent {#sleependevent}


> 源码：[src/physics/matter-js/events/SLEEP_END_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/SLEEP_END_EVENT.js#L7)  



---

### SleepStartEvent {#SleepStartEvent}

#### SleepStartEvent {#sleepstartevent}


> 源码：[src/physics/matter-js/events/SLEEP_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/SLEEP_START_EVENT.js#L7)  



---

## 静态函数 {#static-functions-1}

### AFTER_ADD {#AFTER_ADD}

#### AFTER_ADD {#after_add}


**说明:**

添加事件后的物质物理.

本次活动是由物质物理世界的一个例子在过程结束时,当世界刚刚增加了一个新的体或约束时,才发出.

听听场景用`this.matter.world.on('afteradd', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.AfterAddEvent](/api/typedef/physics-matter-events#afteraddevent) | 否 | 添加事件对象 。 |


> 源码：[src/physics/matter-js/events/AFTER_ADD_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/AFTER_ADD_EVENT.js#L15)  
引入版本：3.22.0


---

### AFTER_REMOVE {#AFTER_REMOVE}

#### AFTER_REMOVE {#after_remove}


**说明:**

删除事件后的物质物理 。

本次活动是由物质物理世界的一个实例在从世界中移除一个身体或约束的过程结束时发出的。

听听场景用`this.matter.world.on('afterremove', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.AfterRemoveEvent](/api/typedef/physics-matter-events#afterremoveevent) | 否 | 删除事件对象 。 |


> 源码：[src/physics/matter-js/events/AFTER_REMOVE_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/AFTER_REMOVE_EVENT.js#L15)  
引入版本：3.22.0


---

### AFTER_UPDATE {#AFTER_UPDATE}

#### AFTER_UPDATE {#after_update}


**说明:**

更新事件后的物质物理 。

本次事件是由一个物质物理世界实例在引擎更新后,所有碰撞事件都得到解决后发出的.

听听场景用`this.matter.world.on('afterupdate', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.AfterUpdateEvent](/api/typedef/physics-matter-events#afterupdateevent) | 否 | 更新事件对象 。 |


> 源码：[src/physics/matter-js/events/AFTER_UPDATE_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/AFTER_UPDATE_EVENT.js#L15)  
引入版本：3.0.0


---

### BEFORE_ADD {#BEFORE_ADD}

#### BEFORE_ADD {#before_add}


**说明:**

添加事件前的物质物理 。

这项活动是由物质物理世界的一个实例在进程开始时,即世界正在增加一个新的体或约束。

听听场景用`this.matter.world.on('beforeadd', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.BeforeAddEvent](/api/typedef/physics-matter-events#beforeaddevent) | 否 | 添加事件对象 。 |


> 源码：[src/physics/matter-js/events/BEFORE_ADD_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/BEFORE_ADD_EVENT.js#L15)  
引入版本：3.22.0


---

### BEFORE_REMOVE {#BEFORE_REMOVE}

#### BEFORE_REMOVE {#before_remove}


**说明:**

事件删除前的物质物理 。

本次活动是由物质物理世界实例在从世界中移除一个身体或约束物的过程开始时发出的。

听听场景用`this.matter.world.on('beforeremove', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.BeforeRemoveEvent](/api/typedef/physics-matter-events#beforeremoveevent) | 否 | 删除事件对象 。 |


> 源码：[src/physics/matter-js/events/BEFORE_REMOVE_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/BEFORE_REMOVE_EVENT.js#L15)  
引入版本：3.22.0


---

### BEFORE_UPDATE {#BEFORE_UPDATE}

#### BEFORE_UPDATE {#before_update}


**说明:**

更新事件前的物质物理 。

本次事件是由物质物理世界案例 在所有碰撞处理发生之前发出来的

听听场景用`this.matter.world.on('beforeupdate', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.BeforeUpdateEvent](/api/typedef/physics-matter-events#beforeupdateevent) | 否 | 更新事件对象 。 |


> 源码：[src/physics/matter-js/events/BEFORE_UPDATE_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/BEFORE_UPDATE_EVENT.js#L15)  
引入版本：3.0.0


---

### COLLISION_ACTIVE {#COLLISION_ACTIVE}

#### COLLISION_ACTIVE {#collision_active}


**说明:**

物质物理碰撞活动。

此事件由引擎更新后的物质物理世界实例发送。 它提供了当前勾选中所有对对对的列表( 如果有的话) 。

听听场景用`this.matter.world.on('collisionactive', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.CollisionActiveEvent](/api/typedef/physics-matter-events#collisionactiveevent) | 否 | 碰撞事件对象 。 |
| bodyA | MatterJS.BodyType | 否 | 首对碰撞的第一对躯体. `event.pairs`阵列可能包含更多的碰撞体. |
| bodyB | MatterJS.BodyType | 否 | 第一种碰撞对的第二体. `event.pairs`阵列可能包含更多的碰撞体. |


> 源码：[src/physics/matter-js/events/COLLISION_ACTIVE_EVENT.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/COLLISION_ACTIVE_EVENT.js#L16)  
引入版本：3.0.0


---

### COLLISION_END {#COLLISION_END}

#### COLLISION_END {#collision_end}


**说明:**

物质物理碰撞事件结束。

此事件由引擎更新后的物质物理世界实例发送。 它提供了当前勾选中已完成碰撞的所有对子( 如果有) 列表 。

听听场景用`this.matter.world.on('collisionend', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.CollisionEndEvent](/api/typedef/physics-matter-events#collisionendevent) | 否 | 碰撞事件对象 。 |
| bodyA | MatterJS.BodyType | 否 | 首对碰撞的第一对躯体. `event.pairs`阵列可能包含更多的碰撞体. |
| bodyB | MatterJS.BodyType | 否 | 第一种碰撞对的第二体. `event.pairs`阵列可能包含更多的碰撞体. |


> 源码：[src/physics/matter-js/events/COLLISION_END_EVENT.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/COLLISION_END_EVENT.js#L16)  
引入版本：3.0.0


---

### COLLISION_START {#COLLISION_START}

#### COLLISION_START {#collision_start}


**说明:**

物质物理碰撞启动事件.

此事件由引擎更新后的物质物理世界实例发送。 它提供了当前勾选中所有开始碰撞的对子( 如果有) 列表 。

听听场景用`this.matter.world.on('collisionstart', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.CollisionStartEvent](/api/typedef/physics-matter-events#collisionstartevent) | 否 | 碰撞事件对象 。 |
| bodyA | MatterJS.BodyType | 否 | 首对碰撞的第一对躯体. `event.pairs`阵列可能包含更多的碰撞体. |
| bodyB | MatterJS.BodyType | 否 | 第一种碰撞对的第二体. `event.pairs`阵列可能包含更多的碰撞体. |


> 源码：[src/physics/matter-js/events/COLLISION_START_EVENT.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/COLLISION_START_EVENT.js#L16)  
引入版本：3.0.0


---

### DRAG {#DRAG}

#### DRAG {#drag}


**说明:**

物质物理拖动事件 。

当一个指针约束器正在积极拖曳一个天体时, 事件由物质物理世界实例发出。 每次指针移动时都会释放它 。

听听场景用`this.matter.world.on('drag', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | MatterJS.BodyType | 否 | 正在拖动的天体。 这是一个物质天体,而不是 Phaser 游戏对象 。 |
| constraint | [Phaser.Physics.Matter.PointerConstraint](/api/class/physics-matter-pointerconstraint) | 否 | 拖着尸体的指针控制器 |


> 源码：[src/physics/matter-js/events/DRAG_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/DRAG_EVENT.js#L7)  
引入版本：3.16.2


---

### DRAG_END {#DRAG_END}

#### DRAG_END {#drag_end}


**说明:**

物质物理拖动结束事件 。

当一个指针约束停止拖曳一个身体时, 事件是由物质物理世界实例发出的。

听听场景用`this.matter.world.on('dragend', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | MatterJS.BodyType | 否 | 停止拖曳的身体。 这是一个物质的身体, 而不是 Phaser 游戏对象 。 |
| constraint | [Phaser.Physics.Matter.PointerConstraint](/api/class/physics-matter-pointerconstraint) | 否 | 拖着尸体的指针控制器 |


> 源码：[src/physics/matter-js/events/DRAG_END_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/DRAG_END_EVENT.js#L7)  
引入版本：3.16.2


---

### DRAG_START {#DRAG_START}

#### DRAG_START {#drag_start}


**说明:**

物质物理拖动启动事件 。

当一个指针约束器开始拖曳一个身体时, 事件是由物质物理世界实例发出的。

听听场景用`this.matter.world.on('dragstart', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | MatterJS.BodyType | 否 | 开始拖曳的天体。 这是一个物质天体, 而不是 Phaser 游戏对象 。 |
| part | MatterJS.BodyType | 否 | 被点击的人体部分. |
| constraint | [Phaser.Physics.Matter.PointerConstraint](/api/class/physics-matter-pointerconstraint) | 否 | 拖着尸体的指针控制器 |


> 源码：[src/physics/matter-js/events/DRAG_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/DRAG_START_EVENT.js#L7)  
引入版本：3.16.2


---

### PAUSE {#PAUSE}

#### PAUSE {#pause}


**说明:**

物质物理世界暂停事件.

本次事件是由物质物理世界实例发出,当它被暂停时。

听听场景用`this.matter.world.on('pause', listener)`


> 源码：[src/physics/matter-js/events/PAUSE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/PAUSE_EVENT.js#L7)  
引入版本：3.0.0


---

### RESUME {#RESUME}

#### RESUME {#resume}


**说明:**

物质物理世界再现事件.

本次事件由物质物理世界实例发出, 当它从暂停状态恢复时。

听听场景用`this.matter.world.on('resume', listener)`


> 源码：[src/physics/matter-js/events/RESUME_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/RESUME_EVENT.js#L7)  
引入版本：3.0.0


---

### SLEEP_END {#SLEEP_END}

#### SLEEP_END {#sleep_end}


**说明:**

物质物理睡眠结束事件.

本次事件是由物质物理世界的一个例子 即一个身体停止睡觉时发出的

听听场景用`this.matter.world.on('sleepend', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.SleepEndEvent](/api/typedef/physics-matter-events#sleependevent) | 否 | 睡眠事件对象 。 |
| body | MatterJS.BodyType | 否 | 尸体已经停止睡觉。 |


> 源码：[src/physics/matter-js/events/SLEEP_END_EVENT.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/SLEEP_END_EVENT.js#L14)  
引入版本：3.0.0


---

### SLEEP_START {#SLEEP_START}

#### SLEEP_START {#sleep_start}


**说明:**

物质物理睡眠启动事件.

本次事件是由物质物理世界的一个例子,当一个身体睡觉时。

听听场景用`this.matter.world.on('sleepstart', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.SleepStartEvent](/api/typedef/physics-matter-events#sleepstartevent) | 否 | 睡眠事件对象 。 |
| body | MatterJS.BodyType | 否 | 已经睡着的躯体 |


> 源码：[src/physics/matter-js/events/SLEEP_START_EVENT.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/SLEEP_START_EVENT.js#L14)  
引入版本：3.0.0


---

---
