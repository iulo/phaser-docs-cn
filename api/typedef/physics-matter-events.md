# Physics.Matter.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/physics-matter-events)

## AfterAddEvent {#afteraddevent}

### \<static> AfterAddEvent {#static-afteraddevent}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object | Array.\<any> | 否 | 添加的对象的数组。 可以是单个的物体、 约束、 复合物或这些物体的混合物 。 |
| source | any | 否 | 事件源对象. |
| 名称 | string | 否 | 活动名称. |

**类型**: object

**Member of**: Phaser.Physics.Matter.Events
> 源码：[src/physics/matter-js/events/AFTER_ADD_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/AFTER_ADD_EVENT.js#L7)  


---

## AfterRemoveEvent {#afterremoveevent}

### \<static> AfterRemoveEvent {#static-afterremoveevent}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object | Array.\<any> | 否 | 被移除对象的数组。可以是单个物体、约束、复合物或这些物体的混合物。 |
| source | any | 否 | 事件源对象. |
| 名称 | string | 否 | 活动名称. |

**类型**: object

**Member of**: Phaser.Physics.Matter.Events
> 源码：[src/physics/matter-js/events/AFTER_REMOVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/AFTER_REMOVE_EVENT.js#L7)  


---

## AfterUpdateEvent {#afterupdateevent}

### \<static> AfterUpdateEvent {#static-afterupdateevent}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| timestamp | number | 否 | 事件物质引擎的值 `timing.timestamp` 。 |
| source | any | 否 | 事件源对象. |
| 名称 | string | 否 | 活动名称. |

**类型**: object

**Member of**: Phaser.Physics.Matter.Events
> 源码：[src/physics/matter-js/events/AFTER_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/AFTER_UPDATE_EVENT.js#L7)  


---

## BeforeAddEvent {#beforeaddevent}

### \<static> BeforeAddEvent {#static-beforeaddevent}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object | Array.\<any> | 否 | 要添加的对象的数组。 可以是单个的物体、 约束、 复合物或这些物体的混合物 。 |
| source | any | 否 | 事件源对象. |
| 名称 | string | 否 | 活动名称. |

**类型**: object

**Member of**: Phaser.Physics.Matter.Events
> 源码：[src/physics/matter-js/events/BEFORE_ADD_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/BEFORE_ADD_EVENT.js#L7)  


---

## BeforeRemoveEvent {#beforeremoveevent}

### \<static> BeforeRemoveEvent {#static-beforeremoveevent}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object | Array.\<any> | 否 | 要删除的对象的数组。 可以是单个的物体、 约束、 复合物或这些物体的混合物 。 |
| source | any | 否 | 事件源对象. |
| 名称 | string | 否 | 活动名称. |

**类型**: object

**Member of**: Phaser.Physics.Matter.Events
> 源码：[src/physics/matter-js/events/BEFORE_REMOVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/BEFORE_REMOVE_EVENT.js#L7)  


---

## BeforeUpdateEvent {#beforeupdateevent}

### \<static> BeforeUpdateEvent {#static-beforeupdateevent}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| timestamp | number | 否 | 事件物质引擎的值 `timing.timestamp` 。 |
| source | any | 否 | 事件源对象. |
| 名称 | string | 否 | 活动名称. |

**类型**: object

**Member of**: Phaser.Physics.Matter.Events
> 源码：[src/physics/matter-js/events/BEFORE_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/BEFORE_UPDATE_EVENT.js#L7)  


---

## CollisionActiveEvent {#collisionactiveevent}

### \<static> CollisionActiveEvent {#static-collisionactiveevent}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pairs | Array.\<[Phaser.Types.Physics.Matter.MatterCollisionPair](/api/typedef/types-physics-matter#mattercollisionpair)> | 否 | 碰撞中所有受影响对子的列表. |
| timestamp | number | 否 | 事件物质引擎的值 `timing.timestamp` 。 |
| source | any | 否 | 事件源对象. |
| 名称 | string | 否 | 活动名称. |

**类型**: object

**Member of**: Phaser.Physics.Matter.Events
> 源码：[src/physics/matter-js/events/COLLISION_ACTIVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/COLLISION_ACTIVE_EVENT.js#L7)  


---

## CollisionEndEvent {#collisionendevent}

### \<static> CollisionEndEvent {#static-collisionendevent}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pairs | Array.\<[Phaser.Types.Physics.Matter.MatterCollisionPair](/api/typedef/types-physics-matter#mattercollisionpair)> | 否 | 碰撞中所有受影响对子的列表. |
| timestamp | number | 否 | 事件物质引擎的值 `timing.timestamp` 。 |
| source | any | 否 | 事件源对象. |
| 名称 | string | 否 | 活动名称. |

**类型**: object

**Member of**: Phaser.Physics.Matter.Events
> 源码：[src/physics/matter-js/events/COLLISION_END_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/COLLISION_END_EVENT.js#L7)  


---

## CollisionStartEvent {#collisionstartevent}

### \<static> CollisionStartEvent {#static-collisionstartevent}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pairs | Array.\<[Phaser.Types.Physics.Matter.MatterCollisionPair](/api/typedef/types-physics-matter#mattercollisionpair)> | 否 | 碰撞中所有受影响对子的列表. |
| timestamp | number | 否 | 事件物质引擎的值 `timing.timestamp` 。 |
| source | any | 否 | 事件源对象. |
| 名称 | string | 否 | 活动名称. |

**类型**: object

**Member of**: Phaser.Physics.Matter.Events
> 源码：[src/physics/matter-js/events/COLLISION_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/COLLISION_START_EVENT.js#L7)  


---

## SleepEndEvent {#sleependevent}

### \<static> SleepEndEvent {#static-sleependevent}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | any | 否 | 事件源对象. |
| 名称 | string | 否 | 活动名称. |

**类型**: object

**Member of**: Phaser.Physics.Matter.Events
> 源码：[src/physics/matter-js/events/SLEEP_END_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/SLEEP_END_EVENT.js#L7)  


---

## SleepStartEvent {#sleepstartevent}

### \<static> SleepStartEvent {#static-sleepstartevent}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | any | 否 | 事件源对象. |
| 名称 | string | 否 | 活动名称. |

**类型**: object

**Member of**: Phaser.Physics.Matter.Events
> 源码：[src/physics/matter-js/events/SLEEP_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/events/SLEEP_START_EVENT.js#L7)  


---

---
