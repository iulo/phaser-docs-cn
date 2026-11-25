# Physics.Arcade.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/physics-arcade-events)

## COLLIDE {#collide}


**说明:** Arcade 物理世界碰撞事件.

如果两个物理体碰撞... 和... 至少是...
他们中有一个人,onCollide~ 链接 ~ Phaser.Physics.Arcade.Body#onCollide属性设置为 `true`.

它提供了处理碰撞事件的一种替代手段,而不是使用回调方法.

听听场景用`this.physics.world.on('collide', listener)`

请注意,"碰撞"和"重叠"是Arcade物理中两个不同的事物.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject1 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 第一个游戏对象 参与碰撞。 这是 `body1` 的母游戏 。 |
| gameObject2 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 第二个游戏对象 参与碰撞。 这是 `body2` 的母游戏 。 |
| body1 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) \| [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) | 否 | 参与碰撞的第一台物理体. |
| body2 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) \| [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) | 否 | 第二物理体参与碰撞. |

**所属:** [Phaser.Physics.Arcade.Events](/api/namespace/physics-arcade-events)
> 源码：[src/physics/arcade/events/COLLIDE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/events/COLLIDE_EVENT.js#L7)  
引入版本：3.0.0

## OVERLAP {#overlap}


**说明:** Arcade 物理世界重叠事件.

如果两个物理体重叠到_和_和_至少是_,则本次事件由Arcade物理世界实例发出
他们中有一个人,onOverlap~ 链接 ~ Phaser.Physics.Arcade.Body#onOverlap属性设置为 `true`.

它提供了处理重叠事件的一种替代手段,而不是使用回调方法。

听听场景用`this.physics.world.on('overlap', listener)`

请注意,"碰撞"和"重叠"是Arcade物理中两个不同的事物.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject1 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 第一个游戏对象涉及重叠。 这是 `body1` 的母游戏 。 |
| gameObject2 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 重复中涉及的第二个游戏对象。 这是 `body2` 的母游戏 。 |
| body1 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) \| [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) | 否 | 第一个物理体参与重叠。 |
| body2 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) \| [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) | 否 | 第二物理体参与重叠. |

**所属:** [Phaser.Physics.Arcade.Events](/api/namespace/physics-arcade-events)
> 源码：[src/physics/arcade/events/OVERLAP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/events/OVERLAP_EVENT.js#L7)  
引入版本：3.0.0

## PAUSE {#pause}


**说明:** Arcade 物理世界暂停事件.

本次事件是由一个Arcade物理世界实例在暂停时发出的.

听听场景用`this.physics.world.on('pause', listener)`

**所属:** [Phaser.Physics.Arcade.Events](/api/namespace/physics-arcade-events)
> 源码：[src/physics/arcade/events/PAUSE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/events/PAUSE_EVENT.js#L7)  
引入版本：3.0.0

## RESUME {#resume}


**说明:** Arcade 物理世界复出事件.

本次事件由Arcade物理世界实例发出,当它从暂停状态恢复时.

听听场景用`this.physics.world.on('resume', listener)`

**所属:** [Phaser.Physics.Arcade.Events](/api/namespace/physics-arcade-events)
> 源码：[src/physics/arcade/events/RESUME_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/events/RESUME_EVENT.js#L7)  
引入版本：3.0.0

## TILE_COLLIDE {#tile_collide}


**说明:** Arcade 物理台式电路碰撞事件.

如果一个物理体与一个砖瓦碰撞,则这个事件是由Arcade物理世界实例发出的。
将它的[onCollide] QQLINK Phaser.Physics.Arcade.Body#onCollide]属性设置到`true`.

它提供了处理碰撞事件的一种替代手段,而不是使用回调方法.

听听场景用`this.physics.world.on('tilecollide', listener)`

请注意,"碰撞"和"重叠"是Arcade物理中两个不同的事物.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 碰撞中涉及的游戏对象。 这是 `body` 的母体 。 |
| tile | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 物理体的瓦片相撞了 物理体的瓦片上 |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 游戏对象的Arcade 物理体 参与碰撞。 |

**所属:** [Phaser.Physics.Arcade.Events](/api/namespace/physics-arcade-events)
> 源码：[src/physics/arcade/events/TILE_COLLIDE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/events/TILE_COLLIDE_EVENT.js#L7)  
引入版本：3.16.1

## TILE_OVERLAP {#tile_overlap}


**说明:** Arcade 物理事件 泰尔重叠事件

如果一个物理体与一个图案重叠,则该事件由Arcade物理世界实例发出_和__
将它的[onOverlap] QQLINK Phaser.Physics.Arcade.Body#onOverlap]属性设置到`true`.

它提供了处理重叠事件的一种替代手段,而不是使用回调方法。

听听场景用`this.physics.world.on('tileoverlap', listener)`

请注意,"碰撞"和"重叠"是Arcade物理中两个不同的事物.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 重叠中涉及的游戏对象。 这是 `body` 的母程序 。 |
| tile | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 车身的瓦片重叠。 |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 游戏对象的Arcade 物理体 涉及重叠。 |

**所属:** [Phaser.Physics.Arcade.Events](/api/namespace/physics-arcade-events)
> 源码：[src/physics/arcade/events/TILE_OVERLAP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/events/TILE_OVERLAP_EVENT.js#L7)  
引入版本：3.16.1

## WORLD_BOUNDS {#world_bounds}


**说明:** Arcade 物理世界大事件.

如果一个机构与世界边界发生联系,则该事件由Arcade物理世界实例发出。
它的[onWorldBounds] QQLINK Phaser.Physics.Arcade.Body#onWorldBounds] 属性设置为 `true`.

它提供了处理碰撞事件的一种替代手段,而不是使用回调方法.

听听场景用`this.physics.world.on('worldbounds', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 撞到世界极限的Arcade 物理体 |
| up | boolean | 否 | 物理体被挡住了吗? |
| down | boolean | 否 | 物理体被挡住了吗? |
| left | boolean | 否 | 物理体被挡住了吗? |
| right | boolean | 否 | 物理体被挡住了吗? |

**所属:** [Phaser.Physics.Arcade.Events](/api/namespace/physics-arcade-events)
> 源码：[src/physics/arcade/events/WORLD_BOUNDS_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/events/WORLD_BOUNDS_EVENT.js#L7)  
引入版本：3.0.0

## WORLD_STEP {#world_step}


**说明:** Arcade 物理世界步步事件.

每当物理步骤启动时, 都会由Arcade物理世界实例发出这个信号。
已更新了此物理体和碰撞器。

在高帧度的设定中,这可以是每个游戏帧的多次.

听听场景用`this.physics.world.on('worldstep', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delta | number | 否 | 三角洲时间的这个步骤, 以秒计。 |

**所属:** [Phaser.Physics.Arcade.Events](/api/namespace/physics-arcade-events)
> 源码：[src/physics/arcade/events/WORLD_STEP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/events/WORLD_STEP_EVENT.js#L7)  
引入版本：3.18.0

---
