# ArcadePhysics {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-arcade-arcadephysics)

弧形物理插件属于一个场景,并设置和管理了该场景的物理模拟,它也有一些有用的移动和旋转弧形物理体的方法.

你可以从场内使用`this.physics`访问它.

弧形物理使用弹射法的碰撞分辨率和分离。虽然它速度快,适合“弧形”风格游戏,但当多个物体相近或彼此间休息时,它缺乏稳定性。停止两个物体穿透的分离可能会形成对不同物体的新穿透。如果需要高度稳定性,请考虑使用替代物理系统,如 Matter.js 。

**构造函数**

`new ArcadePhysics(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 显示此插件属于的场景 。 |

---


**作用域**: static

> 源码：[src/physics/arcade/ArcadePhysics.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L21)  
引入版本：3.0.0

## 公开成员 {#public-members}

### add {#add}

#### add: [Phaser.Physics.Arcade.Factory](/api/class/physics-arcade-factory) {#add-phaserphysicsarcadefactory}


**说明:**

持有Arcade物理工厂方法的物体.


> 源码：[src/physics/arcade/ArcadePhysics.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L82)  
引入版本：3.0.0


---

### config {#config}

#### config: [Phaser.Types.Physics.Arcade.ArcadeWorldConfig](/api/typedef/types-physics-arcade#arcadeworldconfig) {#config-phasertypesphysicsarcadearcadeworldconfig}


**说明:**

一个配置对象。 组合 GameConfig 和 SceneConfig 对象的 `physics.arcade.*` 属性 。


> 源码：[src/physics/arcade/ArcadePhysics.js#L64](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L64)  
引入版本：3.0.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

显示此插件属于的场景 。


> 源码：[src/physics/arcade/ArcadePhysics.js#L46](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L46)  
引入版本：3.0.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

场景系统.


> 源码：[src/physics/arcade/ArcadePhysics.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L55)  
引入版本：3.0.0


---

### world {#world}

#### world: [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) {#world-phaserphysicsarcadeworld}


**说明:**

物理模拟.


> 源码：[src/physics/arcade/ArcadePhysics.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L73)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### accelerateTo {#accelerateTo}

#### \<instance> accelerateTo(gameObject, x, y, [speed], [xSpeedMax], [ySpeedMax]) {#instance-acceleratetogameobject-x-y-speed-xspeedmax-yspeedmax}


**说明:**

设置游戏对象上的加速度.x/y属性,使其以给定的速率(以每秒像素为单位)向x/y坐标移动

您必须给出一个最大速度值,超过这个值,游戏对象不会更快地前进.

注意: 游戏对象不会持续跟踪目标, 如果目标在转机时改变位置, 则游戏对象不会修改其方向 。 注: 游戏对象到达目的地坐标后不会停止移动 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 任何带有弧形物理体的游戏对象. |
| x | number | 否 |  | 坐标加速到 |
| y | number | 否 |  | y协调加速向上. |
| speed | number | 是 | 60 | 以每秒平方像素为单位的加速度( 速度变化) 。 |
| xSpeedMax | number | 是 | 500 | 游戏对象所能达到的最大x速度. |
| ySpeedMax | number | 是 | 500 | 游戏对象可以达到的最大y速度. |


**返回值:** number - 对象应视距设定以与其新速度相匹配的角(弧度)。


> 源码：[src/physics/arcade/ArcadePhysics.js#L378](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L378)  
引入版本：3.0.0


---

### accelerateToObject {#accelerateToObject}

#### \<instance> accelerateToObject(gameObject, destination, [speed], [xSpeedMax], [ySpeedMax]) {#instance-acceleratetoobjectgameobject-destination-speed-xspeedmax-yspeedmax}


**说明:**

设置游戏对象的加速度.x/y属性,以便以给定的速率(以每秒像素为单位)向目的地对象移动.

您必须给出一个最大速度值,超过这个值,游戏对象不会更快地前进.

注意: 游戏对象不会持续跟踪目标, 如果目标在转机时改变位置, 则游戏对象不会修改其方向 。 注: 游戏对象到达目的地坐标后不会停止移动 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 任何带有弧形物理体的游戏对象. |
| destination | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 要移动的游戏对象。 可以是任何对象, 但必须有可见的 x/y 属性 。 |
| speed | number | 是 | 60 | 以每秒平方像素为单位的加速度( 速度变化) 。 |
| xSpeedMax | number | 是 | 500 | 游戏对象所能达到的最大x速度. |
| ySpeedMax | number | 是 | 500 | 游戏对象可以达到的最大y速度. |


**返回值:** number - 对象应视距设定以与其新速度相匹配的角(弧度)。


> 源码：[src/physics/arcade/ArcadePhysics.js#L414](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L414)  
引入版本：3.0.0


---

### closest {#closest}

#### \<instance> closest(source, [targets]) {#instance-closestsource-targets}


**说明:**

查找最接近源点或对象的“身体”或“游戏对象”。

如果通过 `targets` 参数,这个方法会发现其中最接近的。目标可以是Arcade Physics Game Objects,动态天体,或静态天体。

如果没有通过`targets`参数,这种方法会找到最接近的动态正体.

如果两个或两个以上的目标与源点的距离完全相同,则只返回第一个目标.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 任何具有公共`x`和`y`属性的天体,如游戏对象或几何对象. |
| targets | Array.\<Target> | 是 | 目标 |


**返回值:** Target, null - 目标最接近给定的源点.


> 源码：[src/physics/arcade/ArcadePhysics.js#L438](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L438)  
引入版本：3.0.0


---

### collide {#collide}

#### \<instance> collide(object1, [object2], [collideCallback], [processCallback], [callbackContext]) {#instance-collideobject1-object2-collidecallback-processcallback-callbackcontext}


**说明:**

进行两个物理允许对象之间的碰撞检查和分离,这些对象可以是单游戏对象,游戏对象阵列,物理组,物理组阵列或普通组.

如果你不需要分离,那么用[#overlap](#overlap)代替.

如果通过两个组或数组,则一个成员每个成员将对照另一个成员进行测试.

如果**只通过一个小组(作为`object1`),则小组的每个成员将与其他成员相撞。

如果****只通过一个阵列,则阵列会被反复排列,并且其中的所有元素都会被测试到其他的.

可提供两个调用。 如果发生碰撞, 并且两个碰撞物体被传递给它, 则引用 `collideCallback` 。

弧形物理使用弹射法的碰撞分辨率和分离。虽然它速度快,适合“弧形”风格游戏,但当多个物体相近或彼此间休息时,它缺乏稳定性。停止两个物体穿透的分离可能会形成对不同物体的新穿透。如果需要高度稳定性,请考虑使用替代物理系统,如 Matter.js 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第一个要检查的对象或对象阵列。 |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 是 | 第二个要检查的对象或一系列的对象,或 `undefined` 。 |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 对象碰撞时可选的召回函数。 |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 一个可选的回调函数,如果两个对象碰撞,您可以对他们进行额外检查。如果设置了这个功能,那么只有返回 `true`时,才使用 `collideCallback`z 。 |
| callbackContext | * | 是 | 运行回调时的背景 。 |


**返回值:** boolean - 如果游戏对象有重叠的游戏对象被分离,则真实性是真实的,否则是虚假的.


> 源码：[src/physics/arcade/ArcadePhysics.js#L249](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L249)  
引入版本：3.0.0


---

### collideTiles {#collideTiles}

#### \<instance> collideTiles(sprite, tiles, [collideCallback], [processCallback], [callbackContext]) {#instance-collidetilessprite-tiles-collidecallback-processcallback-callbackcontext}


**说明:**

这一先进方法专门用于测试单个Sprite和一组Tile对象之间的碰撞.

您通常应该使用 `collide` 方法, 使用 Sprite vs. tilemap 层, 因为它会为你进行瓷砖过滤和调压, 以及自动处理有趣的面部碰撞 。

这种方法提供给那些想要检查与特定平面在一层中碰撞的人,而无需在相关的平面上设置任何碰撞属性。这样您就可以在小平面上进行快速动态碰撞。因此,对于给这种方法的平面阵列,您在将平面传递到这种方法之前,不应进行挤压或检查。

重要: 使用这种方法跳过 Tilemap 层使用的 `interesting faces` 系统。 这意味着, 如果您说出一行或一列的瓷砖, 或者跳进或走过这些瓷砖, 就可以在有趣的面值计算被跳过时被卡在瓷砖的边缘上。 然而, 对于动态地图上的快速点火小碰撞设定测试, 这个方法可以证明非常有用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sprite | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 第一个检查碰撞的物体 。 |
| tiles | Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> | 否 | 用于检查碰撞的平面阵列 。 |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 对象碰撞时可选的召回函数。 |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 一个可选的回调函数,如果两个对象碰撞,您可以对他们进行额外检查。如果设置了这个功能,那么只有返回 `true`时,才使用 `collideCallback`z 。 |
| callbackContext | any | 是 | 运行回调时的背景 。 |


**返回值:** boolean - 如果有对象重叠(与 `overlapOnly`),则为真;如果有重叠对象被分离,则为真。


**Fires:** [Phaser.Physics.Arcade.Events#event:TILE_COLLIDE](/api/event/physics-arcade-events#tile_collide)


> 源码：[src/physics/arcade/ArcadePhysics.js#L291](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L291)  
引入版本：3.17.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

拥有此插件的场景正在被销毁。 我们需要关闭然后删除所有外部引用 。


> 源码：[src/physics/arcade/ArcadePhysics.js#L732](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L732)  
引入版本：3.0.0


---

### disableUpdate {#disableUpdate}

#### \<instance> disableUpdate() {#instance-disableupdate}


**说明:**

使 `World.update` 变为**不** 每次场景发出 `UPDATE`事件时都会自动调用。

如果您希望以自己的速率运行世界更新,或者从自己的组件运行,那么您应该使用这种方法来禁用内置链接,然后相应拨打`World.update(time, delta)`.

注意,`World.postUpdate`总是在场景发出`POST_UPDATE`事件时自动调用,无论设置如何.


> 源码：[src/physics/arcade/ArcadePhysics.js#L162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L162)  
引入版本：3.50.0


---

### enableUpdate {#enableUpdate}

#### \<instance> enableUpdate() {#instance-enableupdate}


**说明:**

导致每次 Scene 发出 `UPDATE` 事件时自动调用 `World.update` 。 这是默认设置, 所以只需要您已专门禁用它 。


> 源码：[src/physics/arcade/ArcadePhysics.js#L149](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L149)  
引入版本：3.50.0


---

### furthest {#furthest}

#### \<instance> furthest(source, [targets]) {#instance-furthestsource-targets}


**说明:**

查找距离源点或对象最远的天体或游戏对象。

如果通过 `targets` 参数, 这种方法会发现其中最远的。 目标可以是Arcade Physics Game Objects, 动态天体, 或是静态天体 。

如果没有通过`targets`参数,这种方法会发现最远的动态正体.

如果两个或两个以上的目标与源点的距离完全相同,则只返回第一个目标.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | any | 否 | 任何具有公共`x`和`y`属性的天体,如游戏对象或几何对象. |
| targets | Array.\<[Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body)> \| Array.\<[Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody)> | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 是 | 目标 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body), [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody), [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 目标离给定的源点最远.


> 源码：[src/physics/arcade/ArcadePhysics.js#L493](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L493)  
引入版本：3.0.0


---

### getConfig {#getConfig}

#### \<instance> getConfig() {#instance-getconfig}


**说明:**

创建当前场景的物理配置。


**返回值:** [Phaser.Types.Physics.Arcade.ArcadeWorldConfig](/api/typedef/types-physics-arcade#arcadeworldconfig) - 物理配置.


> 源码：[src/physics/arcade/ArcadePhysics.js#L181](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L181)  
引入版本：3.0.0


---

### moveTo {#moveTo}

#### \<instance> moveTo(gameObject, x, y, [speed], [maxTime]) {#instance-movetogameobject-x-y-speed-maxtime}


**说明:**

将给定的显示对象以稳定的速度移动到 x/y 坐标。 如果您指定 maxTime, 则会调整速度( 覆盖您设定的) , 从而以该秒数到达目的地。 时间因浏览器定时器的工作方式而大致相同 。 注意: 显示对象不会持续跟踪目标 。 如果目标在中转时改变位置, 显示对象不会改变方向 。 注意: 一旦到达目的地坐标, 显示对象不会停止移动 。 注意: 不考虑加速、 maxVelocityZ或拖动( 如果您设置拖动或加速度太高, 此对象不会移动) 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 任何带有弧形物理体的游戏对象. |
| x | number | 否 |  | 坐标是X,朝向。 |
| y | number | 否 |  | 向着Y方向移动 |
| speed | number | 是 | 60 | 它会移动的速度, 以像素每秒( 默认为 60 像素/ 秒) 计 。 |
| maxTime | number | 是 | 0 | 给出的时间以毫秒(1 000 = 1 秒) 。 如果设置速度调整, 对象将以给定的 ms 数到达目的地 。 |


**返回值:** number - 对象应视距设定以与其新速度相匹配的角(弧度)。


> 源码：[src/physics/arcade/ArcadePhysics.js#L548](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L548)  
引入版本：3.0.0


---

### moveToObject {#moveToObject}

#### \<instance> moveToObject(gameObject, destination, [speed], [maxTime]) {#instance-movetoobjectgameobject-destination-speed-maxtime}


**说明:**

将指定的显示对象以稳定的速度移动到目标对象。 如果您指定 maxTime, 它将调整速度( 覆盖您设定的) , 从而以该秒数到达目标对象。 时间因浏览器定时器的工作方式而大致相同。 注意: 显示对象不会持续跟踪目标。 如果目标在转弯时改变位置, 显示对象不会改变方向 。 注意: 表示对象到达目标坐标后不会停止移动 。 注意: 不考虑加速、 maxVelocity或拖动( 如果您设置了拖动或加速度太高, 此对象可能不会移动) 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 任何带有弧形物理体的游戏对象. |
| destination | object | 否 |  | 任何具有公共`x`和`y`属性的天体,如游戏对象或几何对象. |
| speed | number | 是 | 60 | 它会移动的速度, 以像素每秒( 默认为 60 像素/ 秒) 计 。 |
| maxTime | number | 是 | 0 | 给出的时间以毫秒(1 000 = 1 秒) 。 如果设置速度调整, 对象将以给定的 ms 数到达目的地 。 |


**返回值:** number - 对象应视距设定以与其新速度相匹配的角(弧度)。


> 源码：[src/physics/arcade/ArcadePhysics.js#L585](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L585)  
引入版本：3.0.0


---

### nextCategory {#nextCategory}

#### \<instance> nextCategory() {#instance-nextcategory}


**说明:**

返回下一个可用的碰撞类别。

最多可有32个类别。

默认所有机构都会与所有其他机构发生碰撞。

用`Body.setCollisionCategory()`和`Body.setCollidesWith()`的方法来改变这个.


**返回值:** number - 下一个碰撞类别。


> 源码：[src/physics/arcade/ArcadePhysics.js#L202](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L202)  
引入版本：3.70.0


---

### overlap {#overlap}

#### \<instance> overlap(object1, [object2], [overlapCallback], [processCallback], [callbackContext]) {#instance-overlapobject1-object2-overlapcallback-processcallback-callbackcontext}


**说明:**

测试游戏对象是否重叠。 见 [Phaser.Physics.Arcade.World#overlap](/api/class/physics-arcade-world#overlap)

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第一个要检查的对象或对象阵列。 |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 是 | 第二个要检查的对象或一系列的对象,或 `undefined` 。 |
| overlapCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 如果对象重叠,可选择调用回调函数。 |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 一个可选的回调函数,如果两个对象重叠,您可以对他们进行额外检查。如果设置了这个功能,那么只有在返回 `true`时,才使用 `overlapCallback`z 。 |
| callbackContext | * | 是 | 运行回调时的背景 。 |


**返回值:** boolean - 如果至少一个游戏对象与另一个游戏对象重叠,则为真 。


> 源码：[src/physics/arcade/ArcadePhysics.js#L224](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L224)  
引入版本：3.0.0


---

### overlapCirc {#overlapCirc}

#### \<instance> overlapCirc(x, y, radius, [includeDynamic], [includeStatic]) {#instance-overlapcircx-y-radius-includedynamic-includestatic}


**说明:**

这种方法将搜索给定的圆形区域,并返回所有与之重叠的物理体的阵列。它可以返回动态、静态体或两者的混合体。

尸体只需与要考虑的搜索区域相交,不需要完全控制在其中.

如果设定使用RTree(默认为RTree),那么搜索速度相当快,否则搜索是O(N)的动态天体.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 区域中心的x坐标 搜索内部。 |
| y | number | 否 |  | 区域中心的y坐标 搜索内部。 |
| radius | number | 否 |  | 搜索区域半径在内部。 |
| includeDynamic | boolean | 是 | true | 搜索中是否应该包括动态天体? |
| includeStatic | boolean | 是 | false | 搜索内容应该包括静态尸体吗? |


**返回值:** Array.\<[Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body)>, Array.\<[Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody)> - 一系列与指定区域重叠的天体.


> 源码：[src/physics/arcade/ArcadePhysics.js#L677](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L677)  
引入版本：3.21.0


---

### overlapRect {#overlapRect}

#### \<instance> overlapRect(x, y, width, height, [includeDynamic], [includeStatic]) {#instance-overlaprectx-y-width-height-includedynamic-includestatic}


**说明:**

这种方法将搜索给定的矩形区域,并返回所有与它重叠的物理体的阵列。它可以返回动态、静态体或两者的混合体。

尸体只需与要考虑的搜索区域相交,不需要完全控制在其中.

如果设定使用RTree(默认为RTree),那么搜索速度极快,否则搜索是O(N)的动态天体.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 左上方的x坐标 搜索区域内部。 |
| y | number | 否 |  | 左上方的坐标 搜索区域内部。 |
| width | number | 否 |  | 搜索区域宽度 。 |
| height | number | 否 |  | 搜索区域高度 |
| includeDynamic | boolean | 是 | true | 搜索中是否应该包括动态天体? |
| includeStatic | boolean | 是 | false | 搜索内容应该包括静态尸体吗? |


**返回值:** Array.\<[Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body)>, Array.\<[Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody)> - 一系列与指定区域重叠的天体.


> 源码：[src/physics/arcade/ArcadePhysics.js#L650](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L650)  
引入版本：3.17.0


---

### overlapTiles {#overlapTiles}

#### \<instance> overlapTiles(sprite, tiles, [overlapCallback], [processCallback], [callbackContext]) {#instance-overlaptilessprite-tiles-overlapcallback-processcallback-callbackcontext}


**说明:**

这种高级方法专门用于测试单个Sprite和一组Tile对象之间的重叠.

您通常应该使用 `overlap` 方法, 使用 Sprite vs. tilemap 层, 因为它会为你进行瓷砖过滤和调压, 以及自动处理有趣的面部碰撞 。

这种方法是提供给想要检查与特定平面重叠层的,而无需在相关的平面上设置任何碰撞属性的人的。这样您就可以对小平面进行快速动态重叠测试。因此,对于给这种方法的平面阵列,您在传递到这种方法之前,不应进行挤压或检查。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sprite | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 第一个检查重叠对象 。 |
| tiles | Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> | 否 | 要检查重叠的图案组。 |
| overlapCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 如果对象重叠,可选择调用回调函数。 |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 一个可选的回调函数,如果两个对象重叠,您可以对他们进行额外检查。如果设置了这个功能,那么只有在返回 `true`时,才使用 `overlapCallback`z 。 |
| callbackContext | any | 是 | 运行回调时的背景 。 |


**返回值:** boolean - 如果有对象重叠, 则为真 。


**Fires:** [Phaser.Physics.Arcade.Events#event:TILE_OVERLAP](/api/event/physics-arcade-events#tile_overlap)


> 源码：[src/physics/arcade/ArcadePhysics.js#L324](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L324)  
引入版本：3.17.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

暂停模拟。


**返回值:** [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) - 模拟


> 源码：[src/physics/arcade/ArcadePhysics.js#L352](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L352)  
引入版本：3.0.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

恢复模拟( 如果暂停) 。


**返回值:** [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) - 模拟


> 源码：[src/physics/arcade/ArcadePhysics.js#L365](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L365)  
引入版本：3.0.0


---

### shutdown {#shutdown}

#### \<instance> shutdown() {#instance-shutdown}


**说明:**

拥有此插件的场景正在关闭。 我们需要杀死并重置所有内部属性, 以及停止聆听场景事件 。


> 源码：[src/physics/arcade/ArcadePhysics.js#L703](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L703)  
引入版本：3.0.0


---

### velocityFromAngle {#velocityFromAngle}

#### \<instance> velocityFromAngle(angle, [speed], [vec2]) {#instance-velocityfromangleangle-speed-vec2}


**说明:**

考虑到角度( 度) 和速度计算速度, 并把它作为矢量返回, 或者设置到给定的矢量对象。 一种使用方法是: velocityFromAngle( 角, 200, sprite. body. velocity) , 它会直接将数值设置到该向量的速率上, 而不是创建新的矢量对象 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| angle | number | 否 |  | 按顺时针正向计算的角度(下行=90正向,右行=0正向,上行=90负向) |
| speed | number | 是 | 60 | 它的速度会移动,以每秒像素计. |
| vec2 | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 |  | 矢量2,其中x和y属性将设定为计算的速度。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 存储速度的矢量2


> 源码：[src/physics/arcade/ArcadePhysics.js#L608](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L608)  
引入版本：3.0.0


---

### velocityFromRotation {#velocityFromRotation}

#### \<instance> velocityFromRotation(rotation, [speed], [vec2]) {#instance-velocityfromrotationrotation-speed-vec2}


**说明:**

考虑到旋转( 弧度) 和速度计算速度并把它作为矢量返回, 或者设置到给定矢量对象。 一种使用方法是: velocityFromRotation( 旋转, 200, spride. body. velocity) , 它会直接将数值设置到该图示的速度上, 而不是创建新的矢量对象 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| rotation | number | 否 |  | 弧度角度. |
| speed | number | 是 | 60 | 它的速度会移动,以每秒像素计. |
| vec2 | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 |  | 矢量2,其中x和y属性将设定为计算的速度。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 存储速度的矢量2


> 源码：[src/physics/arcade/ArcadePhysics.js#L629](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadePhysics.js#L629)  
引入版本：3.0.0


---

---
