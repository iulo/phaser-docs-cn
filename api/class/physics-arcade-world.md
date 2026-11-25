# World {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-arcade-world)

Arcade 物理世界.

世界负责创建、管理、碰撞和更新它内部的所有机构。

世界的一个实例属于Phaser.Scene,通过地产`physics.world`访问.

它使用RTree空间指数进行快速的宽相碰撞探测,并支持瓦片碰撞. 世界火灾事件用于碰撞,重叠,世界边界接触,以及暂停/恢复状态变化.

**构造函数**

`new World(scene, config)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 这个世界事件所属的场景 |
| config | [Phaser.Types.Physics.Arcade.ArcadeWorldConfig](/api/typedef/types-physics-arcade#arcadeworldconfig) | 否 | 一个Arcade 物理配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/physics/arcade/World.js#L38](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L38)  
引入版本：3.0.0

## 公开成员 {#public-members}

### bodies {#bodies}

#### bodies: Set.\<[Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body)> {#bodies-setphaserphysicsarcadebody}


**说明:**

模拟中充满活力的物理体


> 源码：[src/physics/arcade/World.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L78)  
引入版本：3.0.0


---

### bounds {#bounds}

#### bounds: [Phaser.Geom.Rectangle](/api/class/geom-rectangle) {#bounds-phasergeomrectangle}


**说明:**

边界限制物理体。


> 源码：[src/physics/arcade/World.js#L123](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L123)  
引入版本：3.0.0


---

### checkCollision {#checkCollision}

#### checkCollision: [Phaser.Types.Physics.Arcade.CheckCollisionObject](/api/typedef/types-physics-arcade#checkcollisionobject) {#checkcollision-phasertypesphysicsarcadecheckcollisionobject}


**说明:**

物理体可以碰撞的边界线


> 源码：[src/physics/arcade/World.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L137)  
引入版本：3.0.0


---

### colliders {#colliders}

#### colliders: Phaser.Structs.ProcessQueue.\<Phaser.Physics.Arcade.Collider> {#colliders-phaserstructsprocessqueuephaserphysicsarcadecollider}


**说明:**

这个模拟的碰撞处理器。


> 源码：[src/physics/arcade/World.js#L105](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L105)  
引入版本：3.0.0


---

### debugGraphic {#debugGraphic}

#### debugGraphic: [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) {#debuggraphic-phasergameobjectsgraphics}


**说明:**

图形对象绘制调试显示。


> 源码：[src/physics/arcade/World.js#L296](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L296)  
引入版本：3.0.0


---

### defaults {#defaults}

#### defaults: [Phaser.Types.Physics.Arcade.ArcadeWorldDefaults](/api/typedef/types-physics-arcade#arcadeworlddefaults) {#defaults-phasertypesphysicsarcadearcadeworlddefaults}


**说明:**

默认调试显示新物理体的设置 。


> 源码：[src/physics/arcade/World.js#L305](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L305)  
引入版本：3.0.0


---

### drawDebug {#drawDebug}

#### drawDebug: boolean {#drawdebug-boolean}


**说明:**

启用调试显示。


> 源码：[src/physics/arcade/World.js#L286](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L286)  
引入版本：3.0.0


---

### fixedStep {#fixedStep}

#### fixedStep: boolean {#fixedstep-boolean}


**说明:**

物理是否使用固定更新时间步( true) 或同步到渲染的 fps( 假) ? 。 此属性的假值会禁用 fps 和 timeScale 属性 。


> 源码：[src/physics/arcade/World.js#L164](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L164)  
引入版本：3.23.0


---

### forceX {#forceX}

#### forceX: boolean {#forcex-boolean}


**说明:**

总是在垂直之前横向分开重叠的物理体。假(默认)是指物理体首先在重力较大的轴上分开,如果两者都不大,则垂直轴上分开。


> 源码：[src/physics/arcade/World.js#L254](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L254)  
引入版本：3.0.0


---

### fps {#fps}

#### fps: number {#fps-number}


**说明:**

每秒要采取的物理步骤的数量.

此属性只读。 使用 `setFPS` 方法在运行时修改它 。


> 源码：[src/physics/arcade/World.js#L151](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L151)  
引入版本：3.10.0


---

### gravity {#gravity}

#### gravity: [Phaser.Math.Vector2](/api/class/math-vector2) {#gravity-phasermathvector2}


**说明:**

重力导致物理体加速,以像素每秒为单位.


> 源码：[src/physics/arcade/World.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L114)  
引入版本：3.0.0


---

### isPaused {#isPaused}

#### isPaused: boolean {#ispaused-boolean}


**说明:**

模拟是否随着游戏循环而推进.


> 源码：[src/physics/arcade/World.js#L265](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L265)  
引入版本：3.0.0


---

### maxEntries {#maxEntries}

#### maxEntries: number {#maxentries-number}


**说明:**

RTree上每个节点的最大项目数量.

如果 `useTree` 是 `false` , 则忽略了此。 如果您在世界上拥有大量物理体, 那么您可以通过增加此值来发现搜索性能的改善, 以便允许每个节点和节点的区分都有更多的项目 。


> 源码：[src/physics/arcade/World.js#L321](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L321)  
引入版本：3.0.0


---

### OVERLAP_BIAS {#OVERLAP_BIAS}

#### OVERLAP_BIAS: number {#overlap_bias-number}


**说明:**

物理体每步速度的最大绝对差及其与另一物理体的重叠, 将导致在 * 轴* 上分离。 较大的值倾向于分离 。 较小值倾向于不分离 。


> 源码：[src/physics/arcade/World.js#L229](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L229)  
引入版本：3.0.0


---

### pendingDestroy {#pendingDestroy}

#### pendingDestroy: Set.\<([Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody))> {#pendingdestroy-setphaserphysicsarcadebody-phaserphysicsarcadestaticbody}


**说明:**

静态体标为删除.


> 源码：[src/physics/arcade/World.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L96)  
引入版本：3.1.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

这场模拟赛的场景属于这个场景.


> 源码：[src/physics/arcade/World.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L69)  
引入版本：3.0.0


---

### staticBodies {#staticBodies}

#### staticBodies: Set.\<[Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody)> {#staticbodies-setphaserphysicsarcadestaticbody}


**说明:**

静态的物理体在这个模拟。


> 源码：[src/physics/arcade/World.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L87)  
引入版本：3.0.0


---

### staticTree {#staticTree}

#### staticTree: [Phaser.Structs.RTree](/api/class/structs-rtree) {#statictree-phaserstructsrtree}


**说明:**

静态物理体的空间指数.


> 源码：[src/physics/arcade/World.js#L368](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L368)  
引入版本：3.0.0


---

### stepsLastFrame {#stepsLastFrame}

#### stepsLastFrame: number {#stepslastframe-number}


**说明:**

上一个框架所采取步骤的数量。


> 源码：[src/physics/arcade/World.js#L205](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L205)  
引入版本：3.10.0


---

### TILE_BIAS {#TILE_BIAS}

#### TILE_BIAS: number {#tile_bias-number}


**说明:**

物理体与一个瓦片重叠的最大绝对值, 会导致在 * 轴* 上分离。 较大的值倾向于分离 。 较小值倾向于不分离 。 最佳值可能与瓦片大小相似 。


> 源码：[src/physics/arcade/World.js#L241](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L241)  
引入版本：3.0.0


---

### tileFilterOptions {#tileFilterOptions}

#### tileFilterOptions: [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) {#tilefilteroptions-phasertypestilemapsfilteringoptions}


**说明:**

过滤选项传递到 `GetTilesWithinWorldXY`,作为 `collideSpriteVsTilemapLayer`检查的一部分.


> 源码：[src/physics/arcade/World.js#L406](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L406)  
引入版本：3.60.0


---

### timeScale {#timeScale}

#### timeScale: number {#timescale-number}


**说明:**

适用于帧率的放大系数。

- 1.0=正常速度

- 2.0 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = 半速 = = 半速 = = 半速 = = 半速 = = 半速 = = 半速 = = = = = 半速 = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

- 0.5=双倍速


> 源码：[src/physics/arcade/World.js#L215](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L215)  
引入版本：3.10.0


---

### tree {#tree}

#### tree: [Phaser.Structs.RTree](/api/class/structs-rtree) {#tree-phaserstructsrtree}


**说明:**

动态物理体的空间指数.


> 源码：[src/physics/arcade/World.js#L359](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L359)  
引入版本：3.0.0


---

### treeMinMax {#treeMinMax}

#### treeMinMax: [Phaser.Types.Physics.Arcade.ArcadeWorldTreeMinMax](/api/typedef/types-physics-arcade#arcadeworldtreeminmax) {#treeminmax-phasertypesphysicsarcadearcadeworldtreeminmax}


**说明:**

已回收用于树搜索的输入 。


> 源码：[src/physics/arcade/World.js#L377](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L377)  
引入版本：3.0.0


---

### useTree {#useTree}

#### useTree: boolean {#usetree-boolean}


**说明:**

这个Arcade 物理世界应该使用 RTree 来进行动态物理吗?

RTree是世界所有物理体的空间分类的快速方式。 然而,在某些限度内,清理和将物理体插入树框的成本比它提供的搜索速度增益要昂贵。

如果您在世界上拥有大量动态物理体, 那么最好在物理配置中将此属性设置为 `false` 来禁用 RTree 。

它能应付的号码取决于浏览器和设备,但是在使其失效之前,应该先考虑大约5000个物理体的保守估计.

这只适用于动态体。静态体总是被保存在RTree中,因为它们不需要每个帧都清除,所以你总是从大规模搜索速度中获益。


> 源码：[src/physics/arcade/World.js#L335](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L335)  
引入版本：3.10.0


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




---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(body) {#instance-addbody}


**说明:**

在模拟中添加一个已有的Arcade 物理体或静态Body.

物理体被启用并添加到当地的搜索树上.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) \| [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) | 否 | 模拟中要加入的体型. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body), [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) - 模拟中加入的人体.


> 源码：[src/physics/arcade/World.js#L543](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L543)  
引入版本：3.10.0


---

### addCollider {#addCollider}

#### \<instance> addCollider(object1, object2, [collideCallback], [processCallback], [callbackContext]) {#instance-addcolliderobject1-object2-collidecallback-processcallback-callbackcontext}


**说明:**

创建新的对撞器对象,并添加到模拟中。

撞机是自动进行两个物体碰撞检查的一种方式,它称碰撞,如果发生,则处理回调.

在所有机构更新后,碰撞器将作为世界更新的一部分运行。

通过创建碰撞器,你不需要在你的`update`环中拨打`World.collide`,因为会自动处理它。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第一个检查碰撞的物体 。 |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第二个检查碰撞的物体 。 |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 当两个物体碰撞时,调用符来引用. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 当两个对象碰撞时调用回调。 返回布尔值 。 |
| callbackContext | * | 是 | 呼叫回调的范围。 |


**返回值:** [Phaser.Physics.Arcade.Collider](/api/class/physics-arcade-collider) - 被创造的碰撞器。


> 源码：[src/physics/arcade/World.js#L804](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L804)  
引入版本：3.0.0


---

### addOverlap {#addOverlap}

#### \<instance> addOverlap(object1, object2, [collideCallback], [processCallback], [callbackContext]) {#instance-addoverlapobject1-object2-collidecallback-processcallback-callbackcontext}


**说明:**

创建一个新的 Overlap 撞角对象,并添加到模拟中。

碰撞器是两个对象之间自动进行重叠检查的一种方式,它会调用碰撞,如果发生时处理回调.

在所有机构更新后,碰撞器将作为世界更新的一部分运行。

通过创建碰撞器,你不需要在你的`update`环中拨打`World.overlap`,因为会自动处理它。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第一个检查重叠对象 。 |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第二个检查重叠对象 。 |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 当两个对象重叠时,调用符。 |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 当两个对象重叠时, 调用符。 必须返回布尔 。 |
| callbackContext | * | 是 | 呼叫回调的范围。 |


**返回值:** [Phaser.Physics.Arcade.Collider](/api/class/physics-arcade-collider) - 被创造的碰撞器。


> 源码：[src/physics/arcade/World.js#L840](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L840)  
引入版本：3.0.0


---

### canCollide {#canCollide}

#### \<instance> canCollide(body1, body2) {#instance-cancollidebody1-body2}


**说明:**

检查两个给定的Arcade 物理体是否会根据其碰撞掩码和碰撞类别碰撞,或不碰撞.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 初检其身. |
| body2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第二身验. |


**返回值:** boolean - 如果两具物理体会碰撞 否则会弄虚作假


> 源码：[src/physics/arcade/World.js#L1972](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L1972)  
引入版本：3.70.0


---

### circleBodyIntersects {#circleBodyIntersects}

#### \<instance> circleBodyIntersects(circle, body) {#instance-circlebodyintersectscircle-body}


**说明:**

测试一个圆形体与另一个体相交。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 圆体以试. |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 长方形体以试之. |


**返回值:** boolean - 如果两具物理体相交,否则是假的,那就是真的了。


> 源码：[src/physics/arcade/World.js#L1710](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L1710)  
引入版本：3.0.0


---

### collide {#collide}

#### \<instance> collide(object1, [object2], [collideCallback], [processCallback], [callbackContext]) {#instance-collideobject1-object2-collidecallback-processcallback-callbackcontext}


**说明:**

进行两个物理允许对象之间的碰撞检查和分离,这些对象可以是单游戏对象,游戏对象阵列,物理组,物理组阵列或普通组.

如果你不需要分离,那么用[Phaser.Physics.Arcade.World#overlap](/api/class/physics-arcade-world#overlap)代替.

如果通过两个组或数组,则一个成员每个成员将对照另一个成员进行测试.

如果**只通过一个小组(作为`object1`),则小组的每个成员将与其他成员相撞。

如果****只通过一个阵列,则阵列会被反复排列,并且其中的所有元素都会被测试到其他的.

可提供两个调回; 它们接收碰撞游戏对象作为参数。 如果检测到重叠, 则首先使用 `processCallback` 。 它可以通过返回假来取消碰撞。 接下来是对象分离, 并引用 `collideCallback` 。

Arcade 物理使用弹射法的碰撞分辨率和分离。虽然它速度快,适合“弧形”风格游戏,但当多个物体相近或彼此间休息时,它缺乏稳定性。停止两个物体穿透的分离可能会形成对不同物体的新穿透。如果需要高度稳定性,请考虑使用替代物理系统,如 Matter.js 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第一个要检查的对象或对象阵列。 |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 是 | 第二个要检查的对象或一系列的对象,或 `undefined` 。 |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 对象碰撞时可选的召回函数。 |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 一个可选的回调函数,如果两个对象碰撞,您可以对他们进行额外检查。如果设置了这个功能,那么只有返回 `true`时,才使用 `collideCallback`z 。 |
| callbackContext | any | 是 | 运行回调时的背景 。 |


**返回值:** boolean - 如果游戏对象有重叠之处,则`true`被分离,否则则`false`.


> 源码：[src/physics/arcade/World.js#L1759](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L1759)  
引入版本：3.0.0


---

### collideSpriteVsTilemapLayer {#collideSpriteVsTilemapLayer}

#### \<instance> collideSpriteVsTilemapLayer(sprite, tilemapLayer, [collideCallback], [processCallback], [callbackContext], [overlapOnly]) {#instance-collidespritevstilemaplayersprite-tilemaplayer-collidecallback-processcallback-callbackcontext-overlaponly}


**说明:**

斯普丽特 v 蒂莱马普 碰撞的内部处理器。 请使用 Phaser.Physics.Arcade.World# collide 代替 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sprite | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 第一个检查碰撞的物体 。 |
| tilemapLayer | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 否 | 第二个检查碰撞的物体 。 |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 对象碰撞时可选的召回函数。 |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 一个可选的回调函数,如果两个对象碰撞,您可以对他们进行额外检查。如果设置了这个功能,那么只有返回 `true`时,才使用 `collideCallback`z 。 |
| callbackContext | any | 是 | 运行回调时的背景 。 |
| overlapOnly | boolean | 是 | 是否是碰撞或重叠检查 。 |


**返回值:** boolean - 如果有对象重叠(与 `overlapOnly`),则为真;如果有重叠对象被分离,则为真。


**触发事件:** [Phaser.Physics.Arcade.Events#event:TILE_COLLIDE](/api/event/physics-arcade-events#tile_collide), [Phaser.Physics.Arcade.Events#event:TILE_OVERLAP](/api/event/physics-arcade-events#tile_overlap)


> 源码：[src/physics/arcade/World.js#L2252](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L2252)  
引入版本：3.0.0


---

### collideTiles {#collideTiles}

#### \<instance> collideTiles(sprite, tiles, [collideCallback], [processCallback], [callbackContext]) {#instance-collidetilessprite-tiles-collidecallback-processcallback-callbackcontext}


**说明:**

这一先进方法专门用于测试单个Sprite和一组Tile对象之间的碰撞.

您通常应该使用 `collide` 方法, 使用 Sprite vs. tilemap 层, 因为它会为你进行瓦片过滤和调压, 以及自动处理有趣的面部碰撞 。

这种方法提供给那些想要检查与特定平面在一层中碰撞的人,而无需在相关的平面上设置任何碰撞属性。这样您就可以在小平面上进行快速动态碰撞。因此,对于给这种方法的平面阵列,您在将平面传递到这种方法之前,不应进行挤压或检查。

重要: 使用这种方法跳过 Tilemap 层使用的 `interesting faces` 系统。 这意味着, 如果您说出一行或一列的瓦片, 或者跳进或走过这些瓦片, 就可以在有趣的面值计算被跳过时被卡在瓦片的边缘上。 然而, 对于动态地图上的快速点火小碰撞设定测试, 这个方法可以证明非常有用 。

这种方法不计入碰撞罩或类。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sprite | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 第一个检查碰撞的物体 。 |
| tiles | Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> | 否 | 用于检查碰撞的平面阵列 。 |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 对象碰撞时可选的召回函数。 |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 一个可选的回调函数,如果两个对象碰撞,您可以对他们进行额外检查。如果设置了这个功能,那么只有返回 `true`时,才使用 `collideCallback`z 。 |
| callbackContext | any | 是 | 运行回调时的背景 。 |


**返回值:** boolean - 如果任何重叠对象被分离,则属实,否则是虚假的。


**触发事件:** [Phaser.Physics.Arcade.Events#event:TILE_COLLIDE](/api/event/physics-arcade-events#tile_collide)


> 源码：[src/physics/arcade/World.js#L2173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L2173)  
引入版本：3.17.0


---

### computeAngularVelocity {#computeAngularVelocity}

#### \<instance> computeAngularVelocity(body, delta) {#instance-computeangularvelocitybody-delta}


**说明:**

计算一个物理体的角速度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 用来计算速度的体型 |
| delta | number | 否 | 计算时使用的三角洲值, 以秒计 。 |


> 源码：[src/physics/arcade/World.js#L1166](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L1166)  
引入版本：3.10.0


---

### computeVelocity {#computeVelocity}

#### \<instance> computeVelocity(body, delta) {#instance-computevelocitybody-delta}


**说明:**

计算一个机体每轴速度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 用来计算速度的体型 |
| delta | number | 否 | 计算时使用的三角洲值, 以秒计 。 |


> 源码：[src/physics/arcade/World.js#L1212](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L1212)  
引入版本：3.0.0


---

### createDebugGraphic {#createDebugGraphic}

#### \<instance> createDebugGraphic() {#instance-createdebuggraphic}


**说明:**

创建一个图形游戏对象, 供世界用来使调试显示到 。

如果 `debug` 配置属性设定为 `true` , 则当世界被即时化时会自动调用。 但是, 如果您需要从固定点显示调试图形, 您可以随时调用它 。

您可以通过设置物理配置中的调试属性来控制绘图对象的哪些对象及其使用的颜色。

您通常不应该在制作游戏中使用此功能。 调试时使用此功能来辅助 。


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 图形对象,是世界创建的用于此对象。


> 源码：[src/physics/arcade/World.js#L671](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L671)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

关闭模拟并断开它与当前场景的连接.


**重写:** Phaser.Events.EventEmitter#销毁


> 源码：[src/physics/arcade/World.js#L2489](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L2489)  
引入版本：3.0.0


---

### disable {#disable}

#### \<instance> disable(object) {#instance-disableobject}


**说明:**

禁用游戏对象的Arcade 物理体、游戏对象的阵列或组的子体。

这与`disableBody`方法的区别在于,你可以将数组或组传递到这种方法.

物理体本身没有被删除,它只是有它的`enable`属性被设定为虚假,这意味着你可以通过将它传递到`World.enable`或`World.add`来在任何时间再次重新使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | [Phaser.GameObjects.Group](/api/class/gameobjects-group) | Array.\<[Phaser.GameObjects.Group](/api/class/gameobjects-group)> | 否 | 用于禁用物理体的物体。 |


> 源码：[src/physics/arcade/World.js#L573](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L573)  
引入版本：3.0.0


---

### disableBody {#disableBody}

#### \<instance> disableBody(body) {#instance-disablebodybody}


**说明:**

禁用已有的Arcade 物理体或静态Body,并将其从模拟中移除。

物理体被禁用,并被从当地的搜索树上移走.

物理体本身没有被删除,它只是有它的`enable`属性被设定为虚假,这意味着你可以通过将它传递到`World.enable`或`World.add`来在任何时间再次重新使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) \| [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) | 否 | 物理体要残疾。 |


> 源码：[src/physics/arcade/World.js#L624](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L624)  
引入版本：3.0.0


---

### enable {#enable}

#### \<instance> enable(object, [bodyType]) {#instance-enableobject-bodytype}


**说明:**

将Arcade 物理体添加到游戏对象,游戏对象的阵列,或组的子.

这与`enableBody`方法的区别在于,你可以将数组或组传递到这种方法.

您可以指定物理体是动态还是静态。 动态物理体可以通过速度和加速移动。 静态物理体仍然固定在原位, 因此能够使用优化的搜索树, 使其理想化为静态元素, 如等位对象。 您仍然可以与静态物理体碰撞和重叠 。

通常,你不会直接调用这种方法,而是使用Arcade物理厂现有的辅助方法,例如:

```javascript
this.physics.add.image(x, y, textureKey);
this.physics.add.sprite(x, y, textureKey);
```

调用工厂方法可以同时封装游戏对象的创建和其物理体的创建。 如果您正在创建自定义类, 您可以把它们传递到这种方法, 以便创建它们的物理体 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | [Phaser.GameObjects.Group](/api/class/gameobjects-group) | Array.\<[Phaser.GameObjects.Group](/api/class/gameobjects-group)> | 否 | 用来创建物理体的物体,或称物体. |
| bodyType | number | 是 | 物理体的种类, 要么是`DYNAMIC_BODY`, 要么是`STATIC_BODY`. |


> 源码：[src/physics/arcade/World.js#L421](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L421)  
引入版本：3.0.0


---

### enableBody {#enableBody}

#### \<instance> enableBody(object, [bodyType]) {#instance-enablebodyobject-bodytype}


**说明:**

在单个游戏对象上创建Arcade 物理体.

如果游戏对象已经拥有了机身,这种方法将简单地将其添加回模拟中.

您可以指定物理体是否是动态或静态。 动态物理体可以通过速度和加速移动。 静态物理体仍然固定在原位, 因此能够使用优化的搜索树, 使其理想化为静态元素, 如电位对象。 您仍然可以与静态物理体碰撞和重叠 。

通常,你不会直接调用这种方法,而是使用Arcade物理厂现有的辅助方法,例如:

```javascript
this.physics.add.image(x, y, textureKey);
this.physics.add.sprite(x, y, textureKey);
```

调用工厂方法可以同时封装游戏对象的创建和其物理体的创建。 如果您正在创建自定义类, 您可以把它们传递到这种方法, 以便创建它们的物理体 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 创建此物理体的游戏对象 。 |
| bodyType | number | 是 | 物理体的种类, 要么是`DYNAMIC_BODY`, 要么是`STATIC_BODY`. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 创建此物理体的游戏对象 。


> 源码：[src/physics/arcade/World.js#L489](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L489)  
引入版本：3.0.0


---

### intersects {#intersects}

#### \<instance> intersects(body1, body2) {#instance-intersectsbody1-body2}


**说明:**

检查一下两具物理体是否完全交叉

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body1 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 初检其身. |
| body2 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 第二身验. |


**返回值:** boolean - 如果两具物理体相交,否则是假的,那就是真的了。


> 源码：[src/physics/arcade/World.js#L1662](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L1662)  
引入版本：3.0.0


---

### overlap {#overlap}

#### \<instance> overlap(object1, [object2], [overlapCallback], [processCallback], [callbackContext]) {#instance-overlapobject1-object2-overlapcallback-processcallback-callbackcontext}


**说明:**

测试游戏对象重叠时。

详见[Phaser.Physics.Arcade.World#collide](/api/class/physics-arcade-world#collide).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第一个要检查的对象或对象阵列。 |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 是 | 第二个要检查的对象或一系列的对象,或 `undefined` 。 |
| overlapCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 如果对象重叠,可选择调用回调函数。 |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 一个可选的回调函数,如果两个对象重叠,您可以对他们进行额外检查。如果设置了这个功能,那么只有在返回 `true`时,才使用 `overlapCallback`z 。 |
| callbackContext | * | 是 | 运行回调时的背景 。 |


**返回值:** boolean - 如果至少一个游戏对象与另一个游戏对象重叠,则为真 。


> 源码：[src/physics/arcade/World.js#L1732](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L1732)  
引入版本：3.0.0


---

### overlapTiles {#overlapTiles}

#### \<instance> overlapTiles(sprite, tiles, [overlapCallback], [processCallback], [callbackContext]) {#instance-overlaptilessprite-tiles-overlapcallback-processcallback-callbackcontext}


**说明:**

这种高级方法专门用于测试单个Sprite和一组Tile对象之间的重叠.

您通常应该使用 `overlap` 方法, 使用 Sprite vs. tilemap 层, 因为它会为你进行瓦片过滤和调压, 以及自动处理有趣的面部碰撞 。

这种方法是提供给想要检查与特定平面重叠层的,而无需在相关的平面上设置任何碰撞属性的人的。这样您就可以对小平面进行快速动态重叠测试。因此,对于给这种方法的平面阵列,您在传递到这种方法之前,不应进行挤压或检查。

这种方法不计入碰撞罩或类。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sprite | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 第一个检查碰撞的物体 。 |
| tiles | Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> | 否 | 用于检查碰撞的平面阵列 。 |
| overlapCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 如果对象重叠,可选择调用回调函数。 |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 一个可选的回调函数,如果两个对象碰撞,您可以对他们进行额外检查。如果设置了这个功能,那么只有返回 `true`时,才使用 `overlapCallback`z 。 |
| callbackContext | any | 是 | 运行回调时的背景 。 |


**返回值:** boolean - 如果有对象重叠, 否则会错。 @ info: whatsthis


**触发事件:** [Phaser.Physics.Arcade.Events#event:TILE_OVERLAP](/api/event/physics-arcade-events#tile_overlap)


> 源码：[src/physics/arcade/World.js#L2215](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L2215)  
引入版本：3.17.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

暂停模拟。

暂停模拟不会更新任何现有的物理体,也不会运行任何碰撞器.

然而,您仍然可以启用和禁用其中的躯体,或者手动操作碰撞或重叠检查.


**返回值:** [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) - 此世界物.


**触发事件:** [Phaser.Physics.Arcade.Events#event:PAUSE](/api/event/physics-arcade-events#pause)


> 源码：[src/physics/arcade/World.js#L763](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L763)  
引入版本：3.0.0


---

### postUpdate {#postUpdate}

#### \<instance> postUpdate() {#instance-postupdate}


**说明:**

更新机构,绘制调试显示,并处理待决的队列操作.


> 源码：[src/physics/arcade/World.js#L1071](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L1071)  
引入版本：3.0.0


---

### remove {#remove}

#### \<instance> remove(body) {#instance-removebody}


**说明:**

从模拟中移除现有的Arcade 物理体或静态Body。

物理体被禁用,并被从当地的搜索树上移走.

物理体本身没有被删除,它只是有它的`enabled`属性被设定为虚假,这意味着你可以通过将它传递到`World.enable`或`World.add`来在任何时间再次重新使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) \| [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) | 否 | 模拟中要移除的躯体. |


> 源码：[src/physics/arcade/World.js#L644](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L644)  
引入版本：3.0.0


---

### removeCollider {#removeCollider}

#### \<instance> removeCollider(collider) {#instance-removecollidercollider}


**说明:**

从模拟中移除一个对撞器,所以不再处理它.

这种方法不会破坏碰撞器。 如果您想在以后阶段添加, 您可以调用 `World.colliders.add(Collider)` 。

如果您不再需要碰撞器, 您可以使用 `Collider.destroy` 方法, 这种方法将自动清除所有引用, 然后从世界中删除。 如果您在碰撞器上调用毁灭, 您不需要将它传递给这种方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| collider | [Phaser.Physics.Arcade.Collider](/api/class/physics-arcade-collider) | 否 | 从模拟中移除的对撞器. |


**返回值:** [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) - 此世界物.


> 源码：[src/physics/arcade/World.js#L875](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L875)  
引入版本：3.0.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

如果暂停, 则恢复模拟 。


**返回值:** [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) - 此世界物.


**触发事件:** [Phaser.Physics.Arcade.Events#event:RESUME](/api/event/physics-arcade-events#resume)


> 源码：[src/physics/arcade/World.js#L786](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L786)  
引入版本：3.0.0


---

### separate {#separate}

#### \<instance> separate(body1, body2, [processCallback], [callbackContext], [overlapOnly]) {#instance-separatebody1-body2-processcallback-callbackcontext-overlaponly}


**说明:**

分别二身.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body1 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 初身离诸身. |
| body2 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 第二身离分别. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 过程召回. |
| callbackContext | * | 是 | 引用回调时的上下文. |
| overlapOnly | boolean | 是 | 如果这是拼合还是重叠检查? |


**返回值:** boolean - 如果分居发生,则属实,否则是虚假的。


**触发事件:** [Phaser.Physics.Arcade.Events#event:COLLIDE](/api/event/physics-arcade-events#collide), [Phaser.Physics.Arcade.Events#event:OVERLAP](/api/event/physics-arcade-events#overlap)


> 源码：[src/physics/arcade/World.js#L1338](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L1338)  
引入版本：3.0.0


---

### separateCircle {#separateCircle}

#### \<instance> separateCircle(body1, body2, [overlapOnly]) {#instance-separatecirclebody1-body2-overlaponly}


**说明:**

分开两个物理体,当两者都是圆形的.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body1 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 初身离诸身. |
| body2 | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 第二身离分别. |
| overlapOnly | boolean | 是 | 如果这是拼合还是重叠检查? |


**返回值:** boolean - 如果分居发生,则属实,否则是虚假的。


**触发事件:** [Phaser.Physics.Arcade.Events#event:COLLIDE](/api/event/physics-arcade-events#collide), [Phaser.Physics.Arcade.Events#event:OVERLAP](/api/event/physics-arcade-events#overlap)


> 源码：[src/physics/arcade/World.js#L1455](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L1455)  
引入版本：3.0.0


---

### setBounds {#setBounds}

#### \<instance> setBounds(x, y, width, height, [checkLeft], [checkRight], [checkUp], [checkDown]) {#instance-setboundsx-y-width-height-checkleft-checkright-checkup-checkdown}


**说明:**

设置世界边界的位置、大小和属性。

世界边界是一个无形的矩形,它定义了世界的边缘。如果一个物理体被设定与世界边界相撞,那么它就会在到达任何边缘时自动停止。您可以选择选择选择边界的哪个边缘来检查。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 边界左上角的x坐标. |
| y | number | 否 | 边界的左上角坐标。 |
| width | number | 否 | 边界的宽度。 |
| height | number | 否 | 界高处. |
| checkLeft | boolean | 是 | 物理体应该检查边界左侧吗? |
| checkRight | boolean | 是 | 物理体应该检查边界的右边缘吗? |
| checkUp | boolean | 是 | 物理体应该检查边界的顶端吗? |
| checkDown | boolean | 是 | 物理体应该检查边界底部吗? |


**返回值:** [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) - 此世界物.


> 源码：[src/physics/arcade/World.js#L701](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L701)  
引入版本：3.0.0


---

### setBoundsCollision {#setBoundsCollision}

#### \<instance> setBoundsCollision([left], [right], [up], [down]) {#instance-setboundscollisionleft-right-up-down}


**说明:**

启用或禁用世界边界每个边缘的碰撞.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| left | boolean | 是 | true | 物理体应该检查边界左侧吗? |
| right | boolean | 是 | true | 物理体应该检查边界的右边缘吗? |
| up | boolean | 是 | true | 物理体应该检查边界的顶端吗? |
| down | boolean | 是 | true | 物理体应该检查边界底部吗? |


**返回值:** [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) - 此世界物.


> 源码：[src/physics/arcade/World.js#L735](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L735)  
引入版本：3.0.0


---

### setFPS {#setFPS}

#### \<instance> setFPS(framerate) {#instance-setfpsframerate}


**说明:**

设定模拟运行的帧率。

帧率值用于模拟一个固定更新的时间步,这个固定的时间步可以直接执行一个定型游戏状态.

这个帧率独立于游戏渲染频率。您设置的 fps 越高, 物理模拟步骤就越多。 相反, 您设置的频率越低, 发生的次数就越少 。

你可以自行选择直接推进模拟,使用`step`方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| framerate | number | 否 | 推进模拟的帧速率 |


**返回值:** [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) - 此世界物.


> 源码：[src/physics/arcade/World.js#L899](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L899)  
引入版本：3.10.0


---

### shutdown {#shutdown}

#### \<instance> shutdown() {#instance-shutdown}


**说明:**

关闭模拟,清除物理数据,并删除监听器.


**重写:** Phaser.Events.EventEmitter# 低调的


> 源码：[src/physics/arcade/World.js#L2472](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L2472)  
引入版本：3.0.0


---

### singleStep {#singleStep}

#### \<instance> singleStep() {#instance-singlestep}


**说明:**

一步一步推进模拟.


**触发事件:** [Phaser.Physics.Arcade.Events#event:WORLD_STEP](/api/event/physics-arcade-events#world_step)


> 源码：[src/physics/arcade/World.js#L1057](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L1057)  
引入版本：3.70.0


---

### step {#step}

#### \<instance> step(delta) {#instance-stepdelta}


**说明:**

以时间递增的方式推进模拟。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delta | number | 否 | 三角洲时间数,以秒计,通过它来推进模拟. |


**触发事件:** [Phaser.Physics.Arcade.Events#event:WORLD_STEP](/api/event/physics-arcade-events#world_step)


> 源码：[src/physics/arcade/World.js#L1010](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L1010)  
引入版本：3.10.0


---

### update {#update}

#### \<instance> update(time, delta) {#instance-updatetime-delta}


**说明:**

推进基于时间和时间的模拟。

这是您在场景下自动调用, 不需要直接引用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 请求动画框架或SetTimeout生成的当前时间戳 。 |
| delta | number | 否 | 三角洲时间,以ms计, 过去了,自上一个框架。 |


**触发事件:** [Phaser.Physics.Arcade.Events#event:WORLD_STEP](/api/event/physics-arcade-events#world_step)


> 源码：[src/physics/arcade/World.js#L927](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L927)  
引入版本：3.0.0


---

### updateMotion {#updateMotion}

#### \<instance> updateMotion(body, delta) {#instance-updatemotionbody-delta}


**说明:**

计算一个物理体的速度并更新其位置。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 物理体有待更新。 |
| delta | number | 否 | 运动计算中使用的三角洲值, 以秒计. |


> 源码：[src/physics/arcade/World.js#L1147](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L1147)  
引入版本：3.0.0


---

### wrap {#wrap}

#### \<instance> wrap(object, [padding]) {#instance-wrapobject-padding}


**说明:**

在[Phaser.Physics.Arcade.World#bounds](/api/class/physics-arcade-world#bounds)内包扎物体的坐标(或数个物体的坐标).

如果对象位于任何边界边缘(左,上,右,下)之外,则会从相反的边缘(内侧)移到相同的抵消.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| object | any | 否 |  | 一个游戏对象,一个组,一个具有`x`和`y`坐标的物体,或者一个这样的物体的阵列. |
| padding | number | 是 | 0 | 行动期间每个边界边缘增加一个金额。 |


> 源码：[src/physics/arcade/World.js#L2407](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L2407)  
引入版本：3.3.0


---

### wrapArray {#wrapArray}

#### \<instance> wrapArray(objects, [padding]) {#instance-wraparrayobjects-padding}


**说明:**

将每个物体的坐标 围在[Phaser.Physics.Arcade.World#bounds](/api/class/physics-arcade-world#bounds)内部

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| objects | Array.\<*> | 否 |  | 一系列要包裹的对象。 |
| padding | number | 是 | 0 | 增加的金额 |


> 源码：[src/physics/arcade/World.js#L2438](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L2438)  
引入版本：3.3.0


---

### wrapObject {#wrapObject}

#### \<instance> wrapObject(object, [padding]) {#instance-wrapobjectobject-padding}


**说明:**

将物体的坐标圈在[Phaser.Physics.Arcade.World#bounds](/api/class/physics-arcade-world#bounds)内部.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| object | * | 否 |  | 游戏对象、物理对象或任何带有`x`和`y`坐标的物体 |
| padding | number | 是 | 0 | 增加的金额 |


> 源码：[src/physics/arcade/World.js#L2455](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/World.js#L2455)  
引入版本：3.3.0


---

---
