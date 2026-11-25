# Types.Physics.Arcade {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-physics-arcade)

## ArcadeBodyBounds {#arcadebodybounds}

### \<static> ArcadeBodyBounds {#static-arcadebodybounds}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 左边 |
| y | number | 否 | 上边边. |
| right | number | 否 | 右边边. |
| bottom | number | 否 | 下缘. |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/ArcadeBodyBounds.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/ArcadeBodyBounds.js#L1)  
引入版本：3.0.0

---

## ArcadeBodyCollision {#arcadebodycollision}

### \<static> ArcadeBodyCollision {#static-arcadebodycollision}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| none | boolean | 否 | 如果物理体没有碰撞的话,那就是真的了。 |
| up | boolean | 否 | 如果物理体在上边碰撞的话,那就是真的了。 |
| down | boolean | 否 | 如果物理体在它的下边缘发生碰撞,那就是真的了。 |
| left | boolean | 否 | 如果物理体在左边缘相撞的话,那就是真的了。 |
| right | boolean | 否 | 如果物理体在右边缘相撞的话,那就是真的了。 |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/ArcadeBodyCollision.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/ArcadeBodyCollision.js#L1)  
引入版本：3.0.0

---

## ArcadeColliderType {#arcadecollidertype}

### \<static> ArcadeColliderType {#static-arcadecollidertype}


Arcade 物理对撞器类型.

**类型**: [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | [Phaser.GameObjects.Group](/api/class/gameobjects-group) | [Phaser.Physics.Arcade.Sprite](/api/class/physics-arcade-sprite) | [Phaser.Physics.Arcade.Image](/api/class/physics-arcade-image) | [Phaser.Physics.Arcade.StaticGroup](/api/class/physics-arcade-staticgroup) | [Phaser.Physics.Arcade.Group](/api/class/physics-arcade-group) | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | Array.\<([Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | [Phaser.GameObjects.Group](/api/class/gameobjects-group) | [Phaser.Physics.Arcade.Sprite](/api/class/physics-arcade-sprite) | [Phaser.Physics.Arcade.Image](/api/class/physics-arcade-image) | [Phaser.Physics.Arcade.StaticGroup](/api/class/physics-arcade-staticgroup) | [Phaser.Physics.Arcade.Group](/api/class/physics-arcade-group) | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer))>

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/ArcadeColliderType.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/ArcadeColliderType.js#L1)  
引入版本：3.0.0

---

## ArcadePhysicsCallback {#arcadephysicscallback}

### \<static> ArcadePhysicsCallback {#static-arcadephysicscallback}

**类型**: function

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/ArcadePhysicsCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/ArcadePhysicsCallback.js#L1)  


---

## ArcadeWorldConfig {#arcadeworldconfig}

### \<static> ArcadeWorldConfig {#static-arcadeworldconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| fps | number | 是 | 60 | 设定 QQLink Phaser.Physics.Arcade.World#fps}. |
| fixedStep | boolean | 是 | true | 设置 QQlink 选项 Phaser.Physics.Arcade.World#fixedStep}. |
| timeScale | number | 是 | 1 | 设置 QQlink 选项 Phaser.Physics.Arcade.World#timeScale}. |
| gravity | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 设定为 QQLink Phaser.Physics.Arcade.World#重力 }. |
| x | number | 是 | 0 | 设定为 QQLink Phaser.Physics.Arcade.World#bounds bounds.x}. |
| y | number | 是 | 0 | 设定为 QQLink Phaser.Physics.Arcade.World#bounds bounds.y}. |
| width | number | 是 | 0 | 设定 QQLINK Phaser.Physics.Arcade.World#bounds bounds.width}. 星洲网. |
| height | number | 是 | 0 | 设定为 QQLINK Phaser.Physics.Arcade.World# 边界. heights }. |
| checkCollision | [Phaser.Types.Physics.Arcade.CheckCollisionObject](/api/typedef/types-physics-arcade#checkcollisionobject) | 是 |  | 设置 QQlink 选项 Phaser.Physics.Arcade.World#checkCollision}. |
| overlapBias | number | 是 | 4 | 设置 QQlink 选项 Phaser.Physics.Arcade.World。 。 。 |
| tileBias | number | 是 | 16 | 设置 QQLINK Phaser.Physics.Arcade.World#TIE_BIAS}. |
| forceX | boolean | 是 | false | 设置 QQlink 选项 Phaser.Physics.Arcade.World#forceX}. |
| isPaused | boolean | 是 | false | 设置 QQlink 选项 Phaser.Physics.Arcade.World#isPaused}. |
| debug | boolean | 是 | false | 设定 QQLink Phaser.Physics.Arcade.World#debug }. |
| debugShowBody | boolean | 是 | true | 设置 QQlink 选项 Phaser.Physics.Arcade.World# 违约 debugShowBody}. |
| debugShowStaticBody | boolean | 是 | true | 设置 QQlink 选项 Phaser.Physics.Arcade.World# 违约 debugShowStaticBody}. |
| debugShowVelocity | boolean | 是 | true | 设置 QQlink 选项 Phaser.Physics.Arcade.World# 违约 debugShowStaticBody}. |
| debugBodyColor | number | 是 | "0xff00ff" | 设置 QQlink 选项 Phaser.Physics.Arcade.World# 违约 bodyDebugColor}. |
| debugStaticBodyColor | number | 是 | "0x0000ff" | 设置 QQlink 选项 Phaser.Physics.Arcade.World# 违约 staticBodyDebugColor}. |
| debugVelocityColor | number | 是 | "0x00ff00" | 设置 QQlink 选项 Phaser.Physics.Arcade.World# 违约 velocityDebugColor}. |
| maxEntries | number | 是 | 16 | 设置 QQlink 选项 Phaser.Physics.Arcade.World#maxEntries}. |
| useTree | boolean | 是 | true | 设置 QQlink 选项 Phaser.Physics.Arcade.World#useTree}. |
| customUpdate | boolean | 是 | false | 如果启用, 您需要自己拨打 `World.update` 。 |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/ArcadeWorldConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/ArcadeWorldConfig.js#L1)  
引入版本：3.0.0

---

## ArcadeWorldDefaults {#arcadeworlddefaults}

### \<static> ArcadeWorldDefaults {#static-arcadeworlddefaults}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| debugShowBody | boolean | 否 | 设定为 `true` , 以将动态物理体大纲渲染到调试显示中 。 |
| debugShowStaticBody | boolean | 否 | 设定为 `true` , 以将静态的物理体轮廓制成调试显示 。 |
| debugShowVelocity | boolean | 否 | 设定为 `true` , 以将机体速度标记转换为调试显示 。 |
| bodyDebugColor | number | 否 | 向调试显示器渲染时动态体的颜色轮廓 。 |
| staticBodyDebugColor | number | 否 | 向调试显示器渲染时的静态物理体轮廓颜色. |
| velocityDebugColor | number | 否 | 向调试显示器渲染时速度标记的颜色 。 |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/ArcadeWorldDefaults.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/ArcadeWorldDefaults.js#L1)  
引入版本：3.0.0

---

## ArcadeWorldTreeMinMax {#arcadeworldtreeminmax}

### \<static> ArcadeWorldTreeMinMax {#static-arcadeworldtreeminmax}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| minX | number | 否 | RTree搜索中使用的最小x值. |
| minY | number | 否 | RTree搜索中使用的最小y值. |
| maxX | number | 否 | RTree搜索中使用的最大x值. |
| maxY | number | 否 | RTree搜索中使用的最大y值. |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/ArcadeWorldTreeMinMax.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/ArcadeWorldTreeMinMax.js#L1)  
引入版本：3.0.0

---

## CheckCollisionObject {#checkcollisionobject}

### \<static> CheckCollisionObject {#static-checkcollisionobject}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| up | boolean | 否 | 物理体会和世界顶端相撞吗? |
| down | boolean | 否 | 物理体会和世界的底部碰撞吗? |
| left | boolean | 否 | 物理体会和世界左侧相撞吗? |
| right | boolean | 否 | 物理体会和世界的右侧相撞吗? |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/CheckCollisionObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/CheckCollisionObject.js#L1)  
引入版本：3.0.0

---

## GameObjectWithBody {#gameobjectwithbody}

### \<static> GameObjectWithBody {#static-gameobjectwithbody}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) \| [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) | 否 | 未提供说明 |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/GameObjectWithBody.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/GameObjectWithBody.js#L1)  


---

## GameObjectWithDynamicBody {#gameobjectwithdynamicbody}

### \<static> GameObjectWithDynamicBody {#static-gameobjectwithdynamicbody}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 未提供说明 |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/GameObjectWithDynamicBody.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/GameObjectWithDynamicBody.js#L1)  


---

## GameObjectWithStaticBody {#gameobjectwithstaticbody}

### \<static> GameObjectWithStaticBody {#static-gameobjectwithstaticbody}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) | 否 | 未提供说明 |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/GameObjectWithStaticBody.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/GameObjectWithStaticBody.js#L1)  


---

## ImageWithDynamicBody {#imagewithdynamicbody}

### \<static> ImageWithDynamicBody {#static-imagewithdynamicbody}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 未提供说明 |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/ImageWithDynamicBody.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/ImageWithDynamicBody.js#L1)  


---

## ImageWithStaticBody {#imagewithstaticbody}

### \<static> ImageWithStaticBody {#static-imagewithstaticbody}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) | 否 | 未提供说明 |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/ImageWithStaticBody.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/ImageWithStaticBody.js#L1)  


---

## PhysicsGroupConfig {#physicsgroupconfig}

### \<static> PhysicsGroupConfig {#static-physicsgroupconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| collideWorldBounds | boolean | 是 | false | 设置 QQlink 选项 Phaser.Physics.Arcade.Body#collideWorldBounds}. |
| customBoundsRectangle | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | null | 设置 QQlink 选项 Phaser.Physics.Arcade.Body#setBoundsRectangle setBoundsRectangle}. |
| accelerationX | number | 是 | 0 | 设置 QQLink Phaser.Physics.Arcade.Body#加速.x}. |
| accelerationY | number | 是 | 0 | 设置 QQLINK Phaser.Physics.Arcade.Body#加速.y}. |
| allowDrag | boolean | 是 | true | 设置 QQlink 选项 Phaser.Physics.Arcade.Body#allowDrag}. |
| allowGravity | boolean | 是 | true | 设置 QQlink 选项 Phaser.Physics.Arcade.Body#allowGravity}. |
| allowRotation | boolean | 是 | true | 设置 QQlink 选项 Phaser.Physics.Arcade.Body#allowRotation}. |
| useDamping | boolean | 是 | false | 设置 QQlink 选项 Phaser.Physics.Arcade.Body#useDamping useDamping}. |
| bounceX | number | 是 | 0 | 设定为 QQLINK Phaser.Physics.Arcade.Body#弹跳.x}. |
| bounceY | number | 是 | 0 | 设定 QQLINK Phaser.Physics.Arcade.Body#弹跳.y}. |
| dragX | number | 是 | 0 | 设置为 QQLink Phaser.Physics.Arcade.Body#drag straw.x}. |
| dragY | number | 是 | 0 | 设置为 QQLINK Phaser.Physics.Arcade.Body#drag straw.y}. |
| enable | boolean | 是 | true | 设置 QQLink Phaser.Physics.Arcade.Body#enable 启用 }. |
| gravityX | number | 是 | 0 | 设定为 QQLINK Phaser.Physics.Arcade.Body#重力引力.x}. |
| gravityY | number | 是 | 0 | 设定为 QQLink Phaser.Physics.Arcade.Body#重力引力.y}. |
| frictionX | number | 是 | 0 | 设定为QQLink Phaser.Physics.Arcade.Body#软体摩擦.x}. |
| frictionY | number | 是 | 0 | 设定 QQLINK Phaser.Physics.Arcade.Body#软体摩擦.y}. |
| maxSpeed | number | 是 | -1 | 设置 QQlink 选项 Phaser.Physics.Arcade.Body#maxSpeed maxSpeed}. |
| maxVelocityX | number | 是 | 10000 | 设置 QQlink 选项 Phaser.Physics.Arcade.Body#maxVelocity maxVelocity.x] (英语). |
| maxVelocityY | number | 是 | 10000 | 设置 QQlink 选项 Phaser.Physics.Arcade.Body#maxVelocity maxVelocity曰为甚么. |
| velocityX | number | 是 | 0 | 设置 QQLink Phaser.Physics.Arcade.Body#高速速度.x}. |
| velocityY | number | 是 | 0 | 设置为 QQLink Phaser.Physics.Arcade.Body#高速速度.y}. |
| angularVelocity | number | 是 | 0 | 设置 QQlink 选项 Phaser.Physics.Arcade.Body#angularVelocity}. |
| angularAcceleration | number | 是 | 0 | 设置 QQlink 选项 Phaser.Physics.Arcade.Body#angularAcceleration}. |
| angularDrag | number | 是 | 0 | 设置 QQlink 选项 Phaser.Physics.Arcade.Body#angularDrag}. |
| mass | number | 是 | 0 | 设定为 QQLINK Phaser.Physics.Arcade.Body#Mass}. |
| immovable | boolean | 是 | false | 设置 QQLink Phaser.Physics.Arcade.Body#immobile}. |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/PhysicsGroupConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/PhysicsGroupConfig.js#L1)  
引入版本：3.0.0

---

## PhysicsGroupDefaults {#physicsgroupdefaults}

### \<static> PhysicsGroupDefaults {#static-physicsgroupdefaults}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| setCollideWorldBounds | boolean | 否 | 和Phaser.Physics.Arcade.Body#setCollideWorldBounds}一样 |
| setBoundsRectangle | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 和Phaser.Physics.Arcade.Body#setBoundsRectangle}一样 |
| setAccelerationX | number | 否 | 和Phaser.Physics.Arcade.Body#setAccelerationX}一样 |
| setAccelerationY | number | 否 | 和Phaser.Physics.Arcade.Body#setAccelerationY}一样 |
| setAllowDrag | boolean | 否 | 和Phaser.Physics.Arcade.Body#setAllowDrag}一样 |
| setAllowGravity | boolean | 否 | 和Phaser.Physics.Arcade.Body#setAllowGravity}一样 |
| setAllowRotation | boolean | 否 | 和Phaser.Physics.Arcade.Body#setAllowRotation}一样 |
| setDamping | boolean | 否 | 和Phaser.Physics.Arcade.Body#setDamping}一样 |
| setBounceX | number | 否 | 和Phaser.Physics.Arcade.Body#setBounceX}一样 |
| setBounceY | number | 否 | 和Phaser.Physics.Arcade.Body#setBounceY}一样 |
| setDragX | number | 否 | 和Phaser.Physics.Arcade.Body#setDragX}一样 |
| setDragY | number | 否 | 和Phaser.Physics.Arcade.Body#setDragY}一样 |
| setEnable | boolean | 否 | 和Phaser.Physics.Arcade.Body#setEnable}一样 |
| setGravityX | number | 否 | 和Phaser.Physics.Arcade.Body#setGravityX}一样 |
| setGravityY | number | 否 | 和Phaser.Physics.Arcade.Body#setGravityY}一样 |
| setFrictionX | number | 否 | 和Phaser.Physics.Arcade.Body#setFrictionX}一样 |
| setFrictionY | number | 否 | 和Phaser.Physics.Arcade.Body#setFrictionY}一样 |
| setMaxSpeed | number | 否 | 和Phaser.Physics.Arcade.Body#setMaxSpeed}一样 |
| setVelocityX | number | 否 | 和Phaser.Physics.Arcade.Body#setVelocityX}一样 |
| setVelocityY | number | 否 | 和Phaser.Physics.Arcade.Body#setVelocityY}一样 |
| setAngularVelocity | number | 否 | 和Phaser.Physics.Arcade.Body#setAngularVelocity}一样 |
| setAngularAcceleration | number | 否 | 和Phaser.Physics.Arcade.Body#setAngularAcceleration}一样 |
| setAngularDrag | number | 否 | 和Phaser.Physics.Arcade.Body#setAngularDrag}一样 |
| setMass | number | 否 | 和Phaser.Physics.Arcade.Body#setMass}一样 |
| setImmovable | boolean | 否 | 和Phaser.Physics.Arcade.Body#setImmovable}一样 |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/PhysicsGroupDefaults.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/PhysicsGroupDefaults.js#L1)  
引入版本：3.0.0

---

## SpriteWithDynamicBody {#spritewithdynamicbody}

### \<static> SpriteWithDynamicBody {#static-spritewithdynamicbody}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 未提供说明 |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/SpriteWithDynamicBody.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/SpriteWithDynamicBody.js#L1)  


---

## SpriteWithStaticBody {#spritewithstaticbody}

### \<static> SpriteWithStaticBody {#static-spritewithstaticbody}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) | 否 | 未提供说明 |

**类型**: object

**所属**: Phaser.Types.Physics.Arcade
> 源码：[src/physics/arcade/typedefs/SpriteWithStaticBody.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/typedefs/SpriteWithStaticBody.js#L1)  


---

---
