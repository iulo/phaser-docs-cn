# Physics.Matter.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/physics-matter-events)

## AFTER_ADD {#after_add}


**说明:** 添加事件后的Matter 物理.

本次活动由Matter 物理世界实例在过程结束时发出,当一个新的物体时
或约束刚刚被添加到世界。

听听场景用`this.matter.world.on('afteradd', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.AfterAddEvent](/api/typedef/physics-matter-events#afteraddevent) | 否 | 添加事件对象 。 |

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/AFTER_ADD_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/AFTER_ADD_EVENT.js#L15)  
引入版本：3.22.0

## AFTER_REMOVE {#after_remove}


**说明:** 删除事件后的Matter 物理 。

本次活动由Matter 物理世界实例在过程结束时发出,当过程结束时,
物理体或束缚被从世界中移除.

听听场景用`this.matter.world.on('afterremove', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.AfterRemoveEvent](/api/typedef/physics-matter-events#afterremoveevent) | 否 | 删除事件对象 。 |

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/AFTER_REMOVE_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/AFTER_REMOVE_EVENT.js#L15)  
引入版本：3.22.0

## AFTER_UPDATE {#after_update}


**说明:** 更新事件后的Matter 物理 。

本次事件是由一个Matter 物理世界实例在引擎更新后,所有碰撞事件都得到解决后发出的.

听听场景用`this.matter.world.on('afterupdate', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.AfterUpdateEvent](/api/typedef/physics-matter-events#afterupdateevent) | 否 | 更新事件对象 。 |

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/AFTER_UPDATE_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/AFTER_UPDATE_EVENT.js#L15)  
引入版本：3.0.0

## BEFORE_ADD {#before_add}


**说明:** 添加事件前的Matter 物理 。

本次活动是由Matter 物理世界实例在进程开始时发出,当时一个新的物理体
或约束正增上世间.

听听场景用`this.matter.world.on('beforeadd', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.BeforeAddEvent](/api/typedef/physics-matter-events#beforeaddevent) | 否 | 添加事件对象 。 |

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/BEFORE_ADD_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/BEFORE_ADD_EVENT.js#L15)  
引入版本：3.22.0

## BEFORE_REMOVE {#before_remove}


**说明:** 事件删除前的Matter 物理 。

事件由Matter 物理世界实例在进程开始时发出,当时
物理体或束缚正在被从世界中移除。

听听场景用`this.matter.world.on('beforeremove', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.BeforeRemoveEvent](/api/typedef/physics-matter-events#beforeremoveevent) | 否 | 删除事件对象 。 |

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/BEFORE_REMOVE_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/BEFORE_REMOVE_EVENT.js#L15)  
引入版本：3.22.0

## BEFORE_UPDATE {#before_update}


**说明:** 更新事件前的Matter 物理 。

本次事件是由Matter 物理世界案例 在所有碰撞处理发生之前发出来的

听听场景用`this.matter.world.on('beforeupdate', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.BeforeUpdateEvent](/api/typedef/physics-matter-events#beforeupdateevent) | 否 | 更新事件对象 。 |

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/BEFORE_UPDATE_EVENT.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/BEFORE_UPDATE_EVENT.js#L15)  
引入版本：3.0.0

## COLLISION_ACTIVE {#collision_active}


**说明:** Matter 物理碰撞活动。

本次事件是由一个Matter 物理世界实例在引擎更新后发出的.
它提供了当前勾选中所有对对对对对的列表(如果有的话).

听听场景用`this.matter.world.on('collisionactive', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.CollisionActiveEvent](/api/typedef/physics-matter-events#collisionactiveevent) | 否 | 碰撞事件对象 。 |
| bodyA | MatterJS.BodyType | 否 | 首对碰撞的第一对躯体. `event.pairs`阵列可能包含更多的碰撞体. |
| bodyB | MatterJS.BodyType | 否 | 第一种碰撞对的第二体. `event.pairs`阵列可能包含更多的碰撞体. |

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/COLLISION_ACTIVE_EVENT.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/COLLISION_ACTIVE_EVENT.js#L16)  
引入版本：3.0.0

## COLLISION_END {#collision_end}


**说明:** Matter 物理碰撞事件结束。

本次事件是由一个Matter 物理世界实例在引擎更新后发出的.
它提供了所有已完成当前勾选中碰撞的对对的列表(如果有的话).

听听场景用`this.matter.world.on('collisionend', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.CollisionEndEvent](/api/typedef/physics-matter-events#collisionendevent) | 否 | 碰撞事件对象 。 |
| bodyA | MatterJS.BodyType | 否 | 首对碰撞的第一对躯体. `event.pairs`阵列可能包含更多的碰撞体. |
| bodyB | MatterJS.BodyType | 否 | 第一种碰撞对的第二体. `event.pairs`阵列可能包含更多的碰撞体. |

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/COLLISION_END_EVENT.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/COLLISION_END_EVENT.js#L16)  
引入版本：3.0.0

## COLLISION_START {#collision_start}


**说明:** Matter 物理碰撞启动事件.

本次事件是由一个Matter 物理世界实例在引擎更新后发出的.
它提供了所有对子的列表,这些对子在当前勾选中已经开始碰撞(如果有的话).

听听场景用`this.matter.world.on('collisionstart', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.CollisionStartEvent](/api/typedef/physics-matter-events#collisionstartevent) | 否 | 碰撞事件对象 。 |
| bodyA | MatterJS.BodyType | 否 | 首对碰撞的第一对躯体. `event.pairs`阵列可能包含更多的碰撞体. |
| bodyB | MatterJS.BodyType | 否 | 第一种碰撞对的第二体. `event.pairs`阵列可能包含更多的碰撞体. |

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/COLLISION_START_EVENT.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/COLLISION_START_EVENT.js#L16)  
引入版本：3.0.0

## DRAG_END {#drag_end}


**说明:** Matter 物理拖动结束事件 。

本次事件是由Matter 物理世界实例发出的,当指针约束时
停止拖动一个物理体。

听听场景用`this.matter.world.on('dragend', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | MatterJS.BodyType | 否 | 停止拖曳的物理体。 这是一个物质的物理体, 而不是 Phaser 游戏对象 。 |
| constraint | [Phaser.Physics.Matter.PointerConstraint](/api/class/physics-matter-pointerconstraint) | 否 | 拖着物理体的指针控制器 |

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/DRAG_END_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/DRAG_END_EVENT.js#L7)  
引入版本：3.16.2

## DRAG {#drag}


**说明:** Matter 物理拖动事件 。

本次事件是由Matter 物理世界实例发出的,当指针约束时
正在积极拖曳一个物理体。每次指针移动时都会释放它。

听听场景用`this.matter.world.on('drag', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | MatterJS.BodyType | 否 | 正在拖动的物理体。 这是一个物质物理体,而不是 Phaser 游戏对象 。 |
| constraint | [Phaser.Physics.Matter.PointerConstraint](/api/class/physics-matter-pointerconstraint) | 否 | 拖着物理体的指针控制器 |

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/DRAG_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/DRAG_EVENT.js#L7)  
引入版本：3.16.2

## DRAG_START {#drag_start}


**说明:** Matter 物理拖动启动事件 。

本次事件是由Matter 物理世界实例发出的,当指针约束时
开始拖动物理体。

听听场景用`this.matter.world.on('dragstart', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | MatterJS.BodyType | 否 | 开始拖曳的物理体。 这是一个物质物理体, 而不是 Phaser 游戏对象 。 |
| part | MatterJS.BodyType | 否 | 被点击的人体部分. |
| constraint | [Phaser.Physics.Matter.PointerConstraint](/api/class/physics-matter-pointerconstraint) | 否 | 拖着物理体的指针控制器 |

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/DRAG_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/DRAG_START_EVENT.js#L7)  
引入版本：3.16.2

## PAUSE {#pause}


**说明:** Matter 物理世界暂停事件.

本次事件是由Matter 物理世界实例发出,当它被暂停时。

听听场景用`this.matter.world.on('pause', listener)`

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/PAUSE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/PAUSE_EVENT.js#L7)  
引入版本：3.0.0

## RESUME {#resume}


**说明:** Matter 物理世界再现事件.

本次事件由Matter 物理世界实例发出, 当它从暂停状态恢复时。

听听场景用`this.matter.world.on('resume', listener)`

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/RESUME_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/RESUME_EVENT.js#L7)  
引入版本：3.0.0

## SLEEP_END {#sleep_end}


**说明:** Matter 物理睡眠结束事件.

本次事件是由Matter 物理世界的一个例子 即一个物理体停止睡觉时发出的

听听场景用`this.matter.world.on('sleepend', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.SleepEndEvent](/api/typedef/physics-matter-events#sleependevent) | 否 | 睡眠事件对象 。 |
| body | MatterJS.BodyType | 否 | 物理体已经停止睡觉。 |

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/SLEEP_END_EVENT.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/SLEEP_END_EVENT.js#L14)  
引入版本：3.0.0

## SLEEP_START {#sleep_start}


**说明:** Matter 物理睡眠启动事件.

本次事件是由Matter 物理世界的一个例子,当一个物理体睡觉时。

听听场景用`this.matter.world.on('sleepstart', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Physics.Matter.Events.SleepStartEvent](/api/typedef/physics-matter-events#sleepstartevent) | 否 | 睡眠事件对象 。 |
| body | MatterJS.BodyType | 否 | 已经睡着的躯体 |

**所属:** [Phaser.Physics.Matter.Events](/api/namespace/physics-matter-events)
> 源码：[src/physics/matter-js/events/SLEEP_START_EVENT.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/SLEEP_START_EVENT.js#L14)  
引入版本：3.0.0

---
