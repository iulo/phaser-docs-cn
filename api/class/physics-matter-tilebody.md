# TileBody {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-matter-tilebody)

将一个可以访问相应物质体的图案包裹起来。 砖块只能有一个物质体与之相关。 您可以在现有的物质体中为砖块传递, 或者允许构造者为您创建相应的实体。 如果图案有碰撞组( 在图案中定义) , 这些形状将用来创建主体。 否则, 将使用图案的矩形边框 。

相应的机体可以通过Tile.physics.ZmatterBody在Tile上自行访问.

注:并非所有倾斜碰撞形状都得到支持。更多信息请参见Phaser.Physics.Matter.TileBody#setFromTileCollision。

**构造函数**

`new TileBody(world, tile, [options])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| world | [Phaser.Physics.Matter.World](/api/class/physics-matter-world) | 否 | 该机构属于物质世界实例。 |
| tile | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 目标瓦,应该有一个物质体。 |
| options | [Phaser.Types.Physics.Matter.MatterTileOptions](/api/typedef/types-physics-matter#mattertileoptions) | 是 | 创建 Matter 物理体时要使用的选项 。 |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  
> [Phaser.Physics.Matter.Components.Bounce](/api/namespace/physics-matter-components-bounce)  
> [Phaser.Physics.Matter.Components.Collision](/api/namespace/physics-matter-components-collision)  
> [Phaser.Physics.Matter.Components.Friction](/api/namespace/physics-matter-components-friction)  
> [Phaser.Physics.Matter.Components.Gravity](/api/namespace/physics-matter-components-gravity)  
> [Phaser.Physics.Matter.Components.Mass](/api/namespace/physics-matter-components-mass)  
> [Phaser.Physics.Matter.Components.Sensor](/api/namespace/physics-matter-components-sensor)  
> [Phaser.Physics.Matter.Components.Sleep](/api/namespace/physics-matter-components-sleep)  
> [Phaser.Physics.Matter.Components.Static](/api/namespace/physics-matter-components-static)  



> 源码：[src/physics/matter-js/MatterTileBody.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterTileBody.js#L17)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Physics.Matter.Components.Mass](/api/namespace/physics-matter-components-mass):**


 - [centerOfMass](/api/namespace/physics-matter-components-mass#centerOfMass)




---

## 公开成员 {#public-members}

### tile {#tile}

#### tile: [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) {#tile-phasertilemapstile}


**说明:**

与物理体相关的瓦片物体.


> 源码：[src/physics/matter-js/MatterTileBody.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterTileBody.js#L70)  
引入版本：3.0.0


---

### world {#world}

#### world: [Phaser.Physics.Matter.World](/api/class/physics-matter-world) {#world-phaserphysicsmatterworld}


**说明:**

物理体存在于物质世界里


> 源码：[src/physics/matter-js/MatterTileBody.js#L79](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterTileBody.js#L79)  
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





**From [Phaser.Physics.Matter.Components.Bounce](/api/namespace/physics-matter-components-bounce):**


 - [setBounce](/api/namespace/physics-matter-components-bounce#setBounce)





**From [Phaser.Physics.Matter.Components.Collision](/api/namespace/physics-matter-components-collision):**


 - [setCollidesWith](/api/namespace/physics-matter-components-collision#setCollidesWith)
 - [setCollisionCategory](/api/namespace/physics-matter-components-collision#setCollisionCategory)
 - [setCollisionGroup](/api/namespace/physics-matter-components-collision#setCollisionGroup)
 - [setOnCollide](/api/namespace/physics-matter-components-collision#setOnCollide)
 - [setOnCollideActive](/api/namespace/physics-matter-components-collision#setOnCollideActive)
 - [setOnCollideEnd](/api/namespace/physics-matter-components-collision#setOnCollideEnd)
 - [setOnCollideWith](/api/namespace/physics-matter-components-collision#setOnCollideWith)





**From [Phaser.Physics.Matter.Components.Friction](/api/namespace/physics-matter-components-friction):**


 - [setFriction](/api/namespace/physics-matter-components-friction#setFriction)
 - [setFrictionAir](/api/namespace/physics-matter-components-friction#setFrictionAir)
 - [setFrictionStatic](/api/namespace/physics-matter-components-friction#setFrictionStatic)





**From [Phaser.Physics.Matter.Components.Gravity](/api/namespace/physics-matter-components-gravity):**


 - [setIgnoreGravity](/api/namespace/physics-matter-components-gravity#setIgnoreGravity)





**From [Phaser.Physics.Matter.Components.Mass](/api/namespace/physics-matter-components-mass):**


 - [setDensity](/api/namespace/physics-matter-components-mass#setDensity)
 - [setMass](/api/namespace/physics-matter-components-mass#setMass)





**From [Phaser.Physics.Matter.Components.Sensor](/api/namespace/physics-matter-components-sensor):**


 - [isSensor](/api/namespace/physics-matter-components-sensor#isSensor)
 - [setSensor](/api/namespace/physics-matter-components-sensor#setSensor)





**From [Phaser.Physics.Matter.Components.Sleep](/api/namespace/physics-matter-components-sleep):**


 - [setAwake](/api/namespace/physics-matter-components-sleep#setAwake)
 - [setSleepEndEvent](/api/namespace/physics-matter-components-sleep#setSleepEndEvent)
 - [setSleepEvents](/api/namespace/physics-matter-components-sleep#setSleepEvents)
 - [setSleepStartEvent](/api/namespace/physics-matter-components-sleep#setSleepStartEvent)
 - [setSleepThreshold](/api/namespace/physics-matter-components-sleep#setSleepThreshold)
 - [setToSleep](/api/namespace/physics-matter-components-sleep#setToSleep)





**From [Phaser.Physics.Matter.Components.Static](/api/namespace/physics-matter-components-static):**


 - [isStatic](/api/namespace/physics-matter-components-static#isStatic)
 - [setStatic](/api/namespace/physics-matter-components-static#setStatic)




---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这个 TileBody, 从 Mater 世界上移除当前物理体, 清除砖块上的引用, 并删除所有事件监听器 。


**重写:** Phaser.Events.EventEmitter#销毁


**返回值:** [Phaser.Physics.Matter.TileBody](/api/class/physics-matter-tilebody) - 此 TileBody 对象 。


> 源码：[src/physics/matter-js/MatterTileBody.js#L312](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterTileBody.js#L312)  
引入版本：3.0.0


---

### removeBody {#removeBody}

#### \<instance> removeBody() {#instance-removebody}


**说明:**

从TileBody和物质世界中移除当前物理体。


**返回值:** [Phaser.Physics.Matter.TileBody](/api/class/physics-matter-tilebody) - 此 TileBody 对象 。


> 源码：[src/physics/matter-js/MatterTileBody.js#L292](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterTileBody.js#L292)  
引入版本：3.0.0


---

### setBody {#setBody}

#### \<instance> setBody(body, [addToWorld]) {#instance-setbodybody-addtoworld}


**说明:**

将当前物理体设置为给定物理体。 如果已存在, 这将删除上一个物理体 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | MatterJS.BodyType | 否 |  | 新的物质体要使用。 |
| addToWorld | boolean | 是 | true | 是否要将物理体添加到物质世界中. |


**返回值:** [Phaser.Physics.Matter.TileBody](/api/class/physics-matter-tilebody) - 此 TileBody 对象 。


> 源码：[src/physics/matter-js/MatterTileBody.js#L260](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterTileBody.js#L260)  
引入版本：3.0.0


---

### setFromTileCollision {#setFromTileCollision}

#### \<instance> setFromTileCollision([options]) {#instance-setfromtilecollisionoptions}


**说明:**

设置当前与 Tile 相关的碰撞组的物理体。 这通常会设置在 Tiled 的碰撞编辑器中 。

注:物质不支持斜拉面的所有形状,矩形和多边形直接支持,椭圆形被转换成圆形。多线被当做封闭多边形对待。如果一个瓦片有多个形状,则会创建多段形。如果包含多解库,则支持凸轮形状。解构不保证为复杂形状(如孔)工作,所以将凸轮多边形自行分解成多个凸轮多边形往往最好。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| options | [Phaser.Types.Physics.Matter.MatterBodyTileOptions](/api/typedef/types-physics-matter#matterbodytileoptions) | 是 | 创建 Matter 物理体时要使用的选项。 有关 MatterJS. Body 接受什么的列表请参见 MatterJS. Body 。 |


**返回值:** [Phaser.Physics.Matter.TileBody](/api/class/physics-matter-tilebody) - 此 TileBody 对象 。


> 源码：[src/physics/matter-js/MatterTileBody.js#L160](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterTileBody.js#L160)  
引入版本：3.0.0


---

### setFromTileRectangle {#setFromTileRectangle}

#### \<instance> setFromTileRectangle([options]) {#instance-setfromtilerectangleoptions}


**说明:**

将当前物理体设置为与瓦片的界限相匹配的矩形。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| options | [Phaser.Types.Physics.Matter.MatterBodyTileOptions](/api/typedef/types-physics-matter#matterbodytileoptions) | 是 | 创建 Matter 物理体时要使用的选项。 有关 MatterJS. Body 接受什么的列表请参见 MatterJS. Body 。 |


**返回值:** [Phaser.Physics.Matter.TileBody](/api/class/physics-matter-tilebody) - 此 TileBody 对象 。


> 源码：[src/physics/matter-js/MatterTileBody.js#L134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterTileBody.js#L134)  
引入版本：3.0.0


---

---
