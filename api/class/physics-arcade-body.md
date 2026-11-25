# Body {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-arcade-body)

动态拱门机体。 这样的机体类型可以移动、 加速、 与其他机体碰撞, 并弹出表面。 它支持矩形和圆形碰撞形状, 并提供速度、 加速、 拖曳( 带有可选的坝模式 ) 、 摩擦、 重力、 弹出和世界界限碰撞。 动态机体是最常见的物理机体类型, 用于玩家、 敌人、 射弹和其他移动游戏实体。

它的静态对应是[Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody).

**构造函数**

`new Body(world, [gameObject])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| world | [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) | 否 | 弧场砰砰 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 是 | 游戏对象属于此天体。 至 Phaser 3. 60 此对象现在可选 。 |

---


**作用域**: static


**继承**

> [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision)  



> 源码：[src/physics/arcade/Body.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L17)  
引入版本：3.0.0

## 公开成员 {#public-members}

### acceleration {#acceleration}

#### acceleration: [Phaser.Math.Vector2](/api/class/math-vector2) {#acceleration-phasermathvector2}


**说明:**

身体速度的变化,以像素每秒平方英寸表示.


> 源码：[src/physics/arcade/Body.js#L363](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L363)  
引入版本：3.0.0


---

### allowDrag {#allowDrag}

#### allowDrag: boolean {#allowdrag-boolean}


**说明:**

机体的速度是否受到其`drag`的影响.


> 源码：[src/physics/arcade/Body.js#L372](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L372)  
引入版本：3.0.0


---

### allowGravity {#allowGravity}

#### allowGravity: boolean {#allowgravity-boolean}


**说明:**

该机构的地位是否受到重力(当地或世界)的影响.


> 源码：[src/physics/arcade/Body.js#L403](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L403)  
引入版本：3.0.0


---

### allowRotation {#allowRotation}

#### allowRotation: boolean {#allowrotation-boolean}


**说明:**

这个机体的`rotation`是否受到它的角加速和角速度的影响.


> 源码：[src/physics/arcade/Body.js#L221](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L221)  
引入版本：3.0.0


---

### angle {#angle}

#### angle: number {#angle-number}


**说明:**

计算出这个天体的速度矢量在最后一步中以弧度表示的角.


> 源码：[src/physics/arcade/Body.js#L601](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L601)  
引入版本：3.0.0


---

### angularAcceleration {#angularAcceleration}

#### angularAcceleration: number {#angularacceleration-number}


**说明:**

机体角加速(变化于角速度),以每秒方位的度表示.


> 源码：[src/physics/arcade/Body.js#L558](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L558)  
引入版本：3.0.0


---

### angularDrag {#angularDrag}

#### angularDrag: number {#angulardrag-number}


**说明:**

角运动导致角速度丧失,以每秒度计.

角拖曳只在角加速度为零时才应用.


> 源码：[src/physics/arcade/Body.js#L568](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L568)  
引入版本：3.0.0


---

### angularVelocity {#angularVelocity}

#### angularVelocity: number {#angularvelocity-number}


**说明:**

以每秒度计的这个机身`rotation`的改变率.


> 源码：[src/physics/arcade/Body.js#L548](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L548)  
引入版本：3.0.0


---

### blocked {#blocked}

#### blocked: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](/api/typedef/types-physics-arcade#arcadebodycollision) {#blocked-phasertypesphysicsarcadearcadebodycollision}


**说明:**

无论这天体与静态天体、瓦片或世界边界相撞。如果静态天体的碰撞速度为零,则`embedded`将被设定为零。


> 源码：[src/physics/arcade/Body.js#L807](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L807)  
引入版本：3.0.0


---

### bottom {#bottom}

#### bottom: number {#bottom-number}


**说明:**

身体的底部边缘


> 源码：[src/physics/arcade/Body.js#L2784](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2784)  
引入版本：3.0.0


---

### bounce {#bounce}

#### bounce: [Phaser.Math.Vector2](/api/class/math-vector2) {#bounce-phasermathvector2}


**说明:**

碰撞后返回,相对1。


> 源码：[src/physics/arcade/Body.js#L426](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L426)  
引入版本：3.0.0


---

### center {#center}

#### center: [Phaser.Math.Vector2](/api/class/math-vector2) {#center-phasermathvector2}


**说明:**

身体中心,它的`position`(左上角)和右下角的中点。


> 源码：[src/physics/arcade/Body.js#L323](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L323)  
引入版本：3.0.0


---

### checkCollision {#checkCollision}

#### checkCollision: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](/api/typedef/types-physics-arcade#arcadebodycollision) {#checkcollision-phasertypesphysicsarcadearcadebodycollision}


**说明:**

是否检查此天体的碰撞和方向。 您可以设置 `checkCollision.none = true` 来禁用碰撞检查 。


> 源码：[src/physics/arcade/Body.js#L773](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L773)  
引入版本：3.0.0


---

### collideWorldBounds {#collideWorldBounds}

#### collideWorldBounds: boolean {#collideworldbounds-boolean}


**说明:**

此天体是否与世界边界相互作用 。


> 源码：[src/physics/arcade/Body.js#L763](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L763)  
引入版本：3.0.0


---

### collisionCategory {#collisionCategory}

#### collisionCategory: number {#collisioncategory-number}


**说明:**

拱廊物理体碰撞类.

它可以设置为任何有效的碰撞位域值 。

详见`setCollisionCategory`方法.


> 源码：[src/physics/arcade/Body.js#L842](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L842)  
引入版本：3.70.0


---

### collisionMask {#collisionMask}

#### collisionMask: number {#collisionmask-number}


**说明:**

拱廊物理碰撞罩.

详见`setCollidesWith`方法.


> 源码：[src/physics/arcade/Body.js#L855](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L855)  
引入版本：3.70.0


---

### customBoundsRectangle {#customBoundsRectangle}

#### customBoundsRectangle: [Phaser.Geom.Rectangle](/api/class/geom-rectangle) {#customboundsrectangle-phasergeomrectangle}


**说明:**

用于世界边界碰撞的矩形.

默认它被设定为世界边界矩形。或者,如果这个天体是由物理组创建的,那么该组定义的矩形就是什么。

也可以通过使用`Body.setBoundsRectangle`方法来改变.


> 源码：[src/physics/arcade/Body.js#L446](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L446)  
引入版本：3.20


---

### customSeparateX {#customSeparateX}

#### customSeparateX: boolean {#customseparatex-boolean}


**说明:**

旗子会破坏碰撞身体的默认水平分离。 将自己的 `collideCallback` 传递给对撞机 。


> 源码：[src/physics/arcade/Body.js#L701](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L701)  
引入版本：3.0.0


---

### customSeparateY {#customSeparateY}

#### customSeparateY: boolean {#customseparatey-boolean}


**说明:**

旗子会解除碰撞体的默认垂直分离。 将自己的 `collideCallback` 传递给对撞机 。


> 源码：[src/physics/arcade/Body.js#L712](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L712)  
引入版本：3.0.0


---

### debugBodyColor {#debugBodyColor}

#### debugBodyColor: number {#debugbodycolor-number}


**说明:**

调试显示时此天体的颜色 。


> 源码：[src/physics/arcade/Body.js#L139](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L139)  
引入版本：3.0.0


---

### debugShowBody {#debugShowBody}

#### debugShowBody: boolean {#debugshowbody-boolean}


**说明:**

是否将天体引向调试显示 。


> 源码：[src/physics/arcade/Body.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L121)  
引入版本：3.0.0


---

### debugShowVelocity {#debugShowVelocity}

#### debugShowVelocity: boolean {#debugshowvelocity-boolean}


**说明:**

是否将机体的速度引向调试显示 。


> 源码：[src/physics/arcade/Body.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L130)  
引入版本：3.0.0


---

### deltaMax {#deltaMax}

#### deltaMax: [Phaser.Math.Vector2](/api/class/math-vector2) {#deltamax-phasermathvector2}


**说明:**

身体的绝对最大位置变化,以每步像素表示.


> 源码：[src/physics/arcade/Body.js#L354](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L354)  
引入版本：3.0.0


---

### directControl {#directControl}

#### directControl: boolean {#directcontrol-boolean}


**说明:**

这个天体是否在物理引擎之外受到直接控制? 例如, 你是试图通过一个Tween 移动它吗? 还是它遵循了路径? 如果这样的话, 您可以启用这个布林, 这样天体就可以完全根据它的位置变化来计算它的速度。 这样, 天体就可以调整位置, 并且仍然与其他物体相撞。 然而, 设定速度不会在设定时对这个天体产生影响 。


> 源码：[src/physics/arcade/Body.js#L940](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L940)  
引入版本：3.70.0


---

### drag {#drag}

#### drag: [Phaser.Math.Vector2](/api/class/math-vector2) {#drag-phasermathvector2}


**说明:**

当`useDamping`是假的(默认)时,这是由于运动而绝对失去速度,以像素每秒平方表示.

当`useDamping`是真的时,这是0到1之间的一个坝积乘数.

0值意味着身体立即停止。0.01值意味着身体保持1%每秒的速度,损失99%。0.1值意味着身体保持10%每秒的速度,损失90%。1值意味着身体没有失去速度。你可以使用非常小的值(例如,0.001)快速阻止身体。

x和y两个组件分别应用.

拖曳只在 `acceleration` 零时才应用.


> 源码：[src/physics/arcade/Body.js#L382](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L382)  
引入版本：3.0.0


---

### embedded {#embedded}

#### embedded: boolean {#embedded-boolean}


**说明:**

是否此正文与另一个正文重叠, 且两者都不在移动, 至少在一个轴上 。


> 源码：[src/physics/arcade/Body.js#L753](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L753)  
引入版本：3.0.0


---

### enable {#enable}

#### enable: boolean {#enable-boolean}


**说明:**

此天体是否通过物理模拟更新 。


> 源码：[src/physics/arcade/Body.js#L148](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L148)  
引入版本：3.0.0


---

### facing {#facing}

#### facing: number {#facing-number}


**说明:**

上一步计算出的天体速度方向。 这是一个数值常数值( FACING_UP, FACING_DOWN, FACING-LEFT, FACING/RIGHT)。 如果天体在两轴上移动, 则仅描述垂直轴上的运动 。


> 源码：[src/physics/arcade/Body.js#L621](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L621)  
引入版本：3.0.0


---

### friction {#friction}

#### friction: [Phaser.Math.Vector2](/api/class/math-vector2) {#friction-phasermathvector2}


**说明:**

如果此天体是`immovable`, 并且正在运动, `friction`是骑车体在每个轴上收到的这个天体运动的比例, 相对于1. 的水平元件 (x) 只在两个垂直碰撞体被分离时才适用。 垂直元件 (y) 只在两个垂直相分离体被分离时适用。 默认值 (1, 0) 将骑车体横向移动到这个天体, 垂直比例根本不是 。


> 源码：[src/physics/arcade/Body.js#L518](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L518)  
引入版本：3.0.0


---

### gameObject {#gameObject}

#### gameObject: [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) {#gameobject-phasergameobjectsgameobject}


**说明:**

此天体所属的游戏对象 。

至Phaser 3.60,此为现在可选,可以不定义.


> 源码：[src/physics/arcade/Body.js#L83](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L83)  
引入版本：3.0.0


---

### gravity {#gravity}

#### gravity: [Phaser.Math.Vector2](/api/class/math-vector2) {#gravity-phasermathvector2}


**说明:**

由于重力(特指本体)加速,以像素每秒平方位表示,总重力是这个矢量和模拟的`gravity`的总和.


> 源码：[src/physics/arcade/Body.js#L415](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L415)  
引入版本：3.0.0


---

### halfHeight {#halfHeight}

#### halfHeight: number {#halfheight-number}


**说明:**

半身高,以像素为单位.


> 源码：[src/physics/arcade/Body.js#L314](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L314)  
引入版本：3.0.0


---

### halfWidth {#halfWidth}

#### halfWidth: number {#halfwidth-number}


**说明:**

半身宽度,以像素表示.


> 源码：[src/physics/arcade/Body.js#L305](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L305)  
引入版本：3.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

身体高度, 以像素表示。 如果身体是圆形, 直径也是这个。 如果您想要改变高度, 请使用 `Body.setSize` 方法 。


> 源码：[src/physics/arcade/Body.js#L264](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L264)  
引入版本：3.0.0


---

### immovable {#immovable}

#### immovable: boolean {#immovable-boolean}


**说明:**

是否可以通过与另一个天体的碰撞来移动此天体 。


> 源码：[src/physics/arcade/Body.js#L637](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L637)  
引入版本：3.0.0


---

### isBody {#isBody}

#### isBody: boolean {#isbody-boolean}


**说明:**

快速测试的旗帜表示这个是身体, 用于世界碰撞处理器。


> 源码：[src/physics/arcade/Body.js#L94](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L94)  
引入版本：3.60.0


---

### isCircle {#isCircle}

#### isCircle: boolean {#iscircle-boolean}


**说明:**

此天体是圆形( 真) 还是长方形( 假) 。


> 源码：[src/physics/arcade/Body.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L158)  
引入版本：3.0.0


---

### left {#left}

#### left: number {#left-number}


**说明:**

身体左边缘,与X相同


> 源码：[src/physics/arcade/Body.js#L2733](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2733)  
引入版本：3.0.0


---

### mass {#mass}

#### mass: number {#mass-number}


**说明:**

机体的惯性,相对于默认单位(1). 使用`bounce`,这影响了碰撞时的动力(速度)的交换.


> 源码：[src/physics/arcade/Body.js#L590](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L590)  
引入版本：3.0.0


---

### maxAngular {#maxAngular}

#### maxAngular: number {#maxangular-number}


**说明:**

人体最大角速度,以每秒度计.


> 源码：[src/physics/arcade/Body.js#L580](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L580)  
引入版本：3.0.0


---

### maxSpeed {#maxSpeed}

#### maxSpeed: number {#maxspeed-number}


**说明:**

允许达到的最大速度,以每秒像素计。

如果不是负值,它会限制速度的刻度值。

任何负值都意味着没有应用最大值(默认值)。


> 源码：[src/physics/arcade/Body.js#L504](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L504)  
引入版本：3.16.0


---

### maxVelocity {#maxVelocity}

#### maxVelocity: [Phaser.Math.Vector2](/api/class/math-vector2) {#maxvelocity-phasermathvector2}


**说明:**

绝对最大速度, 以像素每秒为单位。 水平和垂直组件分别应用 。


> 源码：[src/physics/arcade/Body.js#L494](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L494)  
引入版本：3.0.0


---

### moves {#moves}

#### moves: boolean {#moves-boolean}


**说明:**

机体的位置和旋转是否受到其速度,加速度,拖动和重力的影响.


> 源码：[src/physics/arcade/Body.js#L691](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L691)  
引入版本：3.0.0


---

### newVelocity {#newVelocity}

#### newVelocity: [Phaser.Math.Vector2](/api/class/math-vector2) {#newvelocity-phasermathvector2}


**说明:**

身体在最后一步的位置变化(由于速度),以像素表示.

这个值的大小取决于模拟的步速.


> 源码：[src/physics/arcade/Body.js#L342](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L342)  
引入版本：3.0.0


---

### offset {#offset}

#### offset: [Phaser.Math.Vector2](/api/class/math-vector2) {#offset-phasermathvector2}


**说明:**

其Game Object在源像素中的位置抵消了此天体的位置.


> 源码：[src/physics/arcade/Body.js#L181](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L181)  
引入版本：3.0.0


---

### onCollide {#onCollide}

#### onCollide: boolean {#oncollide-boolean}


**说明:**

当这个天体与另一个天体碰撞时, 模拟是否释放出 `collide` 事件 。


> 源码：[src/physics/arcade/Body.js#L472](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L472)  
引入版本：3.0.0


---

### onOverlap {#onOverlap}

#### onOverlap: boolean {#onoverlap-boolean}


**说明:**

当此天体与另一个天体重叠时, 模拟是否释放出 `overlap` 事件 。


> 源码：[src/physics/arcade/Body.js#L483](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L483)  
引入版本：3.0.0


---

### onWorldBounds {#onWorldBounds}

#### onWorldBounds: boolean {#onworldbounds-boolean}


**说明:**

当这个天体与世界边界碰撞时, 模拟是否发出 `worldbounds`事件( 和 `collideWorldBounds` 也是真实的) 。


> 源码：[src/physics/arcade/Body.js#L460](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L460)  
引入版本：3.0.0


---

### overlapR {#overlapR}

#### overlapR: number {#overlapr-number}


**说明:**

如果这个机构是循环的,并与另一个循环机构相撞,则重叠(在分离前)的数量。


> 源码：[src/physics/arcade/Body.js#L743](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L743)  
引入版本：3.0.0


---

### overlapX {#overlapX}

#### overlapX: number {#overlapx-number}


**说明:**

如果此天体与另一天体相撞,则水平重叠(在分离前)的幅度。


> 源码：[src/physics/arcade/Body.js#L723](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L723)  
引入版本：3.0.0


---

### overlapY {#overlapY}

#### overlapY: number {#overlapy-number}


**说明:**

如果此天体正与另一个天体相撞,则垂直重叠(在分离之前)的数量。


> 源码：[src/physics/arcade/Body.js#L733](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L733)  
引入版本：3.0.0


---

### physicsType {#physicsType}

#### physicsType: number {#physicstype-number}


**说明:**

人体的物理类型(动力学或静态).


> 源码：[src/physics/arcade/Body.js#L831](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L831)  
引入版本：3.0.0


---

### position {#position}

#### position: [Phaser.Math.Vector2](/api/class/math-vector2) {#position-phasermathvector2}


**说明:**

该机构在模拟中的位置。


> 源码：[src/physics/arcade/Body.js#L191](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L191)  
引入版本：3.0.0


---

### preRotation {#preRotation}

#### preRotation: number {#prerotation-number}


**说明:**

身体旋转,以度数计,在前一步。


> 源码：[src/physics/arcade/Body.js#L242](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L242)  
引入版本：3.0.0


---

### prev {#prev}

#### prev: [Phaser.Math.Vector2](/api/class/math-vector2) {#prev-phasermathvector2}


**说明:**

本机构在前一个步骤中的立场。


> 源码：[src/physics/arcade/Body.js#L203](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L203)  
引入版本：3.0.0


---

### prevFrame {#prevFrame}

#### prevFrame: [Phaser.Math.Vector2](/api/class/math-vector2) {#prevframe-phasermathvector2}


**说明:**

该机构在前一框架期间的立场。


> 源码：[src/physics/arcade/Body.js#L212](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L212)  
引入版本：3.20.0


---

### pushable {#pushable}

#### pushable: boolean {#pushable-boolean}


**说明:**

如果此天体能被另一个天体推动, 则设定 。

无法推动的躯体会反射出它被赋予碰撞体的全部速度。 如果这个躯体也不可推动,那么它们之间的分离就会平分。

如果你想让身体永远不动或分开,请看`setImmovable`方法.

默认情况下,动态天体总是可推的.


> 源码：[src/physics/arcade/Body.js#L647](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L647)  
引入版本：3.50.0


---

### radius {#radius}

#### radius: number {#radius-number}


**说明:**

如果此天体是圆形, 则此天体的无标半径由 setCircle() 设定, 以源像素表示。 真实半径等于 `halfWidth` 。


> 源码：[src/physics/arcade/Body.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L169)  
引入版本：3.0.0


---

### right {#right}

#### right: number {#right-number}


**说明:**

右侧的躯体边缘.


> 源码：[src/physics/arcade/Body.js#L2750](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2750)  
引入版本：3.0.0


---

### rotation {#rotation}

#### rotation: number {#rotation-number}


**说明:**

身体的旋转,以度为单位,基于它的角加速和角速度. 身体的旋转控制着它的游戏对象的`angle`,它不旋转身体自己的几何,这总是轴向相向的矩形或圆形.


> 源码：[src/physics/arcade/Body.js#L231](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L231)  
引入版本：3.0.0


---

### slideFactor {#slideFactor}

#### slideFactor: [Phaser.Math.Vector2](/api/class/math-vector2) {#slidefactor-phasermathvector2}


**说明:**

此天体的幻灯片因子 。

幻灯片因子控制当此天体被另一个天体推动时,其速度被保存多少 。

默认值为 1, 这意味着它会承担推力中给出的所有速度。 您可以调整这个值, 以控制这个机构在推力结束时保留多少速度 。

例如,0的值将允许这个正体被推,但在推后完全保持静止,比如在像Sokoban这样的游戏中可以看到.

或者您可以设置一个中点, 例如0. 25, 可以在推力结束时保留 25% 的 原速度。 您可以将这个方法与 `setDrag()` 方法结合起来, 以创建减速 。


> 源码：[src/physics/arcade/Body.js#L666](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L666)  
引入版本：3.70.0


---

### sourceHeight {#sourceHeight}

#### sourceHeight: number {#sourceheight-number}


**说明:**

由 setSize () 设定的未标高 body, 以源像素表示。 默认值是 body 游戏对象的纹理框架的高度 。


> 源码：[src/physics/arcade/Body.js#L288](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L288)  
引入版本：3.0.0


---

### sourceWidth {#sourceWidth}

#### sourceWidth: number {#sourcewidth-number}


**说明:**

由 setSize () 设定的未标定的 Object 宽度, 以源像素表示。 默认值是 Object 的 Game Object 纹理框架的宽度 。


> 源码：[src/physics/arcade/Body.js#L277](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L277)  
引入版本：3.0.0


---

### speed {#speed}

#### speed: number {#speed-number}


**说明:**

身体速度的计算值,以每秒像素为单位,在最后一步中.


> 源码：[src/physics/arcade/Body.js#L611](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L611)  
引入版本：3.0.0


---

### syncBounds {#syncBounds}

#### syncBounds: boolean {#syncbounds-boolean}


**说明:**

是否自动同步此天体的维度到它的游戏对象的视觉界限的维度 。


> 源码：[src/physics/arcade/Body.js#L820](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L820)  
引入版本：3.0.0


---

### top {#top}

#### top: number {#top-number}


**说明:**

身体的顶端,与Y相同


> 源码：[src/physics/arcade/Body.js#L2767](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2767)  
引入版本：3.0.0


---

### touching {#touching}

#### touching: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](/api/typedef/types-physics-arcade#arcadebodycollision) {#touching-phasertypesphysicsarcadearcadebodycollision}


**说明:**

无论是身体还是静态身体, 还是在哪个方向。 在两具身体均无速度的碰撞中, `embedded` 将被设定为正反方 。


> 源码：[src/physics/arcade/Body.js#L783](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L783)  
引入版本：3.0.0


---

### transform {#transform}

#### transform: object {#transform-object}


**说明:**

适用于本机构的转变。


> 源码：[src/physics/arcade/Body.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L104)  
引入版本：3.4.0


---

### useDamping {#useDamping}

#### useDamping: boolean {#usedamping-boolean}


**说明:**

如果此天体正在使用 `drag` 来控制拖曳方式的应用。 如果设置为 `true` 拖曳, 则会使用一个起锚效果而不是线性方法。 如果您正在创建一个让天体在任意角度自由移动的游戏( 即像小行星中的飞船) , 那么您将会通过使用起锚方式获得一个更平滑和更直观的减速, 避免线性减速而容易触发轴线的拖曳 。

如果您启用此属性, 您应该使用比线性小得多的 `drag`值, 因为这些值被用作速度的乘数。 例如 0. 95 等值会给您带来一个良好的缓慢减速 。


> 源码：[src/physics/arcade/Body.js#L530](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L530)  
引入版本：3.10.0


---

### velocity {#velocity}

#### velocity: [Phaser.Math.Vector2](/api/class/math-vector2) {#velocity-phasermathvector2}


**说明:**

身体的速度,以像素每秒为单位.


> 源码：[src/physics/arcade/Body.js#L333](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L333)  
引入版本：3.0.0


---

### wasTouching {#wasTouching}

#### wasTouching: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](/api/typedef/types-physics-arcade#arcadebodycollision) {#wastouching-phasertypesphysicsarcadearcadebodycollision}


**说明:**

这辆汽车的前一步值是`touching`


> 源码：[src/physics/arcade/Body.js#L796](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L796)  
引入版本：3.0.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

车身的宽度, 以像素表示。 如果车身是圆形, 直径也是这个。 如果您想要改变车身的宽度, 请使用 `Body.setSize` 方法 。


> 源码：[src/physics/arcade/Body.js#L251](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L251)  
引入版本：3.0.0


---

### world {#world}

#### world: [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) {#world-phaserphysicsarcadeworld}


**说明:**

弧场砰砰


> 源码：[src/physics/arcade/Body.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L74)  
引入版本：3.0.0


---

### worldBounce {#worldBounce}

#### worldBounce: [Phaser.Math.Vector2](/api/class/math-vector2) {#worldbounce-phasermathvector2}


**说明:**

与世界边界相撞后,相对于1. 如果无效,则使用`bounce`。


> 源码：[src/physics/arcade/Body.js#L435](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L435)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

身体的横向位置(左边缘).


> 源码：[src/physics/arcade/Body.js#L2691](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2691)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

身体的垂直位置(顶端边缘).


> 源码：[src/physics/arcade/Body.js#L2712](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2712)  
引入版本：3.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision):**


 - [addCollidesWith](/api/namespace/physics-arcade-components-collision#addCollidesWith)
 - [removeCollidesWith](/api/namespace/physics-arcade-components-collision#removeCollidesWith)
 - [resetCollisionCategory](/api/namespace/physics-arcade-components-collision#resetCollisionCategory)
 - [setCollidesWith](/api/namespace/physics-arcade-components-collision#setCollidesWith)
 - [setCollisionCategory](/api/namespace/physics-arcade-components-collision#setCollisionCategory)
 - [willCollideWith](/api/namespace/physics-arcade-components-collision#willCollideWith)




---

## 公开方法 {#public-methods}

### checkWorldBounds {#checkWorldBounds}

#### \<instance> checkWorldBounds() {#instance-checkworldbounds}


**说明:**

检查这个天体与世界边界的碰撞,然后将它们分开。


**返回值:** boolean - 如果这个身体与世界边界相撞,那就是真的。


> 源码：[src/physics/arcade/Body.js#L1333](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1333)  
引入版本：3.0.0


---

### deltaAbsX {#deltaAbsX}

#### \<instance> deltaAbsX() {#instance-deltaabsx}


**说明:**

本机构水平位置的绝对(非负)变化与前一步相比.


**返回值:** number - 自最后一步以来水平位置的绝对变化,以像素表示.


> 源码：[src/physics/arcade/Body.js#L1736](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1736)  
引入版本：3.0.0


---

### deltaAbsY {#deltaAbsY}

#### \<instance> deltaAbsY() {#instance-deltaabsy}


**说明:**

该机构的垂直位置与前一步相比,绝对(非负)变化.


**返回值:** number - 自最后一步以来垂直位置的绝对变化,以像素表示.


> 源码：[src/physics/arcade/Body.js#L1749](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1749)  
引入版本：3.0.0


---

### deltaX {#deltaX}

#### \<instance> deltaX() {#instance-deltax}


**说明:**

本天体水平位置与前一步的改变。 此值设定在天体更新阶段 。

由于一个天体每步可以更新多次, 这可能无法为天体保留最终三角形值。 在这种情况下, 请参看 `deltaXFinal` 方法 。


**返回值:** number - 自最后一步以来水平位置的变化,以像素表示.


> 源码：[src/physics/arcade/Body.js#L1762](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1762)  
引入版本：3.0.0


---

### deltaXFinal {#deltaXFinal}

#### \<instance> deltaXFinal() {#instance-deltaxfinal}


**说明:**

本机的横向位置与之前的游戏更新相比有所变化.

这个值是在`postUpdate`阶段设定的,并考虑到了`deltaMax`和机体的最终位置.

由于这个值直到 `postUpdate`才计算, 您必须在 Scene `POST_UPDATE` 或 `RENDER` 事件期间, 而不是在 `update` 中听, 因为此值不会通过该点计算 。 如果您_ do_ 在 `update` 中使用这些值, 它们将会代表 从 _ precen_ game 帧中得出的三角形 。


**返回值:** number - 最终三角洲值x.


> 源码：[src/physics/arcade/Body.js#L1796](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1796)  
引入版本：3.22.0


---

### deltaY {#deltaY}

#### \<instance> deltaY() {#instance-deltay}


**说明:**

本天体垂直位置与上一步的改变。 此值设定在天体更新阶段 。

由于一个天体每步可以更新多次, 这可能无法为天体保留最终三角形值。 在这种情况下, 请参看 `deltaYFinal` 方法 。


**返回值:** number - 自最后一步以来垂直位置的变化,以像素表示.


> 源码：[src/physics/arcade/Body.js#L1779](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1779)  
引入版本：3.0.0


---

### deltaYFinal {#deltaYFinal}

#### \<instance> deltaYFinal() {#instance-deltayfinal}


**说明:**

本机的垂直位置与之前的游戏更新相比的变化.

这个值是在`postUpdate`阶段设定的,并考虑到了`deltaMax`和机体的最终位置.

由于这个值直到 `postUpdate`才计算, 您必须在 Scene `POST_UPDATE` 或 `RENDER` 事件期间, 而不是在 `update` 中听, 因为此值不会通过该点计算 。 如果您_ do_ 在 `update` 中使用这些值, 它们将会代表 从 _ precen_ game 帧中得出的三角形 。


**返回值:** number - 最后三角洲的值是多少? 最终三角洲的值是几百万


> 源码：[src/physics/arcade/Body.js#L1817](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1817)  
引入版本：3.22.0


---

### deltaZ {#deltaZ}

#### \<instance> deltaZ() {#instance-deltaz}


**说明:**

该机构的轮换从前一步, 以度计的变化。


**返回值:** number - 上一步以来的旋转变化,以度计.


> 源码：[src/physics/arcade/Body.js#L1838](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1838)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

禁用此天体, 并标记它, 以便通过模拟删除 。


> 源码：[src/physics/arcade/Body.js#L1851](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1851)  
引入版本：3.0.0


---

### drawDebug {#drawDebug}

#### \<instance> drawDebug(graphic) {#instance-drawdebuggraphic}


**说明:**

如果启用, 则绘制此天体及其速度 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| graphic | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 图形对象要绘制 。 |


> 源码：[src/physics/arcade/Body.js#L1867](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1867)  
引入版本：3.0.0


---

### getBounds {#getBounds}

#### \<instance> getBounds(obj) {#instance-getboundsobj}


**说明:**

将本天体边缘坐标复制成物体。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| obj | [Phaser.Types.Physics.Arcade.ArcadeBodyBounds](/api/typedef/types-physics-arcade#arcadebodybounds) | 否 | 复制这些值的对象 。 |


**返回值:** [Phaser.Types.Physics.Arcade.ArcadeBodyBounds](/api/typedef/types-physics-arcade#arcadebodybounds) - - {x,y,右,底}的物体。


> 源码：[src/physics/arcade/Body.js#L1644](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1644)  
引入版本：3.0.0


---

### hitTest {#hitTest}

#### \<instance> hitTest(x, y) {#instance-hittestx-y}


**说明:**

测试坐标是否在本体之内。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 水平坐标 |
| y | number | 否 | 竖坐标. |


**返回值:** boolean - 如果(x,y)是属于本机构,则为真。


> 源码：[src/physics/arcade/Body.js#L1664](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1664)  
引入版本：3.0.0


---

### onCeiling {#onCeiling}

#### \<instance> onCeiling() {#instance-onceiling}


**说明:**

无论是这个天体在向上移动时触摸一个瓦片还是世界边界.


**返回值:** boolean - 摸摸就对了


> 源码：[src/physics/arcade/Body.js#L1708](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1708)  
引入版本：3.0.0


---

### onFloor {#onFloor}

#### \<instance> onFloor() {#instance-onfloor}


**说明:**

无论是这台机器在向下移动时触摸一个瓦片还是世界边界.


**返回值:** boolean - 摸摸就对了


> 源码：[src/physics/arcade/Body.js#L1694](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1694)  
引入版本：3.0.0


---

### onWall {#onWall}

#### \<instance> onWall() {#instance-onwall}


**说明:**

无论是此天体在左右移动时触摸一个瓦片还是世界边界 。


**返回值:** boolean - 摸摸就对了


> 源码：[src/physics/arcade/Body.js#L1722](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1722)  
引入版本：3.0.0


---

### postUpdate {#postUpdate}

#### \<instance> postUpdate() {#instance-postupdate}


**说明:**

将“身体”结果反馈到母游戏对象。

这种方法被称为每个游戏框,无论世界是否步入.


> 源码：[src/physics/arcade/Body.js#L1233](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1233)  
引入版本：3.0.0


---

### preUpdate {#preUpdate}

#### \<instance> preUpdate(willStep, delta) {#instance-preupdatewillstep-delta}


**说明:**

与母游戏对象同步对象位置。

这种方法被称为每个游戏框,无论世界是否步入.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| willStep | boolean | 否 | 这个机构还会更新吗? |
| delta | number | 否 | 三角洲时间,几秒钟, 过去了,从上一个框架。 |


> 源码：[src/physics/arcade/Body.js#L1116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1116)  
引入版本：3.17.0


---

### processX {#processX}

#### \<instance> processX(x, [vx], [left], [right]) {#instance-processxx-vx-left-right}


**说明:**

这是内部处理器, 由 `ProcessX` 函数调用为碰撞步骤的一部分。 您几乎永远不要直接调用它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 增加机构位置的金额。 |
| vx | number | 是 | 增加体速的金额。 |
| left | boolean | 是 | 设置被封存的值。 左侧值 ? |
| right | boolean | 是 | 设置被屏蔽的. 正确的值吗 ? |


> 源码：[src/physics/arcade/Body.js#L2615](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2615)  
引入版本：3.50.0


---

### processY {#processY}

#### \<instance> processY(y, [vy], [up], [down]) {#instance-processyy-vy-up-down}


**说明:**

这是内部处理器, 由 `ProcessY` 函数调用为碰撞步骤的一部分。 您几乎永远不要直接调用它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| y | number | 否 | 增加机构位置的金额。 |
| vy | number | 是 | 增加体速的金额。 |
| up | boolean | 是 | 设置被封存的. up 值吗 ? |
| down | boolean | 是 | 设置被封存的. 下限值 ? |


> 源码：[src/physics/arcade/Body.js#L2653](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2653)  
引入版本：3.50.0


---

### reset {#reset}

#### \<instance> reset(x, y) {#instance-resetx-y}


**说明:**

将此天体的母游戏对象设定为给定坐标, 并将此天体重新设置在新坐标。 如果天体有任何速度或加速度, 则会因调用此天体而丢失 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 放置游戏对象的水平位置 。 |
| y | number | 否 | 放置游戏对象的垂直位置 。 |


> 源码：[src/physics/arcade/Body.js#L1571](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1571)  
引入版本：3.0.0


---

### resetFlags {#resetFlags}

#### \<instance> resetFlags([clear]) {#instance-resetflagsclear}


**说明:**

将`wasTouching`,`touching`和`blocked`的状态重新设置,为物理步骤做好准备.

只有在物理世界要运行这个框架的一步时,这个方法才被称为"方法".

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| clear | boolean | 是 | false | 设定 `wasTouching` 值为默认值 。 |


> 源码：[src/physics/arcade/Body.js#L1071](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1071)  
引入版本：3.18.0


---

### setAcceleration {#setAcceleration}

#### \<instance> setAcceleration(x, [y]) {#instance-setaccelerationx-y}


**说明:**

设定身体加速。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 水平元件,以像素每秒平方英寸表示. |
| y | number | 是 | "x" | 垂直的组件,以像素每秒平方表示. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2216](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2216)  
引入版本：3.0.0


---

### setAccelerationX {#setAccelerationX}

#### \<instance> setAccelerationX(value) {#instance-setaccelerationxvalue}


**说明:**

设定身体水平加速 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 加速,以像素每秒平方英寸表示. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2234](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2234)  
引入版本：3.0.0


---

### setAccelerationY {#setAccelerationY}

#### \<instance> setAccelerationY(value) {#instance-setaccelerationyvalue}


**说明:**

设置天体的垂直加速 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 加速,以像素每秒平方英寸表示. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2251](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2251)  
引入版本：3.0.0


---

### setAllowDrag {#setAllowDrag}

#### \<instance> setAllowDrag([value]) {#instance-setallowdragvalue}


**说明:**

启用或禁用拖曳 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | `true`允许拖曳到这个身体上,或者`false`可以禁用它. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2268](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2268)  
引入版本：3.9.0


---

### setAllowGravity {#setAllowGravity}

#### \<instance> setAllowGravity([value]) {#instance-setallowgravityvalue}


**说明:**

启用或禁用重力对这个机体的影响 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | `true`允许引力在这个身体上,或者`false`使其失效. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2288](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2288)  
引入版本：3.9.0


---

### setAllowRotation {#setAllowRotation}

#### \<instance> setAllowRotation([value]) {#instance-setallowrotationvalue}


**说明:**

启用或禁用旋转 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | `true`允许旋转此机体,或者`false`可以禁用它. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2308](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2308)  
引入版本：3.9.0


---

### setAngularAcceleration {#setAngularAcceleration}

#### \<instance> setAngularAcceleration(value) {#instance-setangularaccelerationvalue}


**说明:**

设定天体角加速 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 加速,以每秒方位的度计。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2526](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2526)  
引入版本：3.0.0


---

### setAngularDrag {#setAngularDrag}

#### \<instance> setAngularDrag(value) {#instance-setangulardragvalue}


**说明:**

设置天体的角拖动。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 拖曳,以每秒平方度计。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2543](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2543)  
引入版本：3.0.0


---

### setAngularVelocity {#setAngularVelocity}

#### \<instance> setAngularVelocity(value) {#instance-setangularvelocityvalue}


**说明:**

设定天体的角速度 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 速度,以每秒度计。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2509](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2509)  
引入版本：3.0.0


---

### setBounce {#setBounce}

#### \<instance> setBounce(x, [y]) {#instance-setbouncex-y}


**说明:**

设定身体的反弹。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 水平反弹,相对1。 |
| y | number | 是 | "x" | 垂直反弹,相对1。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2164](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2164)  
引入版本：3.0.0


---

### setBounceX {#setBounceX}

#### \<instance> setBounceX(value) {#instance-setbouncexvalue}


**说明:**

设定身体水平反弹.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 弹跳,比1强。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2182](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2182)  
引入版本：3.0.0


---

### setBounceY {#setBounceY}

#### \<instance> setBounceY(value) {#instance-setbounceyvalue}


**说明:**

设置身体的垂直反弹。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 弹跳,比1强。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2199](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2199)  
引入版本：3.0.0


---

### setBoundsRectangle {#setBoundsRectangle}

#### \<instance> setBoundsRectangle([bounds]) {#instance-setboundsrectanglebounds}


**说明:**

设置自定义碰撞边界矩形。如果想要设置自定义边界,则使用该边界。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bounds | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 新边界矩形 传`null` 使用世界边界 。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L1315](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1315)  
引入版本：3.20


---

### setCircle {#setCircle}

#### \<instance> setCircle(radius, [offsetX], [offsetY]) {#instance-setcircleradius-offsetx-offsety}


**说明:**

大小和位置 这个机构,作为一个圆。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| radius | number | 否 | 体的半径,在源像素中. |
| offsetX | number | 是 | 其Game Object中"天体"的横向偏移,以源像素表示. |
| offsetY | number | 是 | 其Game Object中"天体"的垂直偏移,以源像素表示. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L1528](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1528)  
引入版本：3.0.0


---

### setCollideWorldBounds {#setCollideWorldBounds}

#### \<instance> setCollideWorldBounds([value], [bounceX], [bounceY], [onWorldBounds]) {#instance-setcollideworldboundsvalue-bouncex-bouncey-onworldbounds}


**说明:**

确定这天体是否与世界边界相撞。

也可选择设置世界跳跃和`onWorldBounds`值.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 如果身体与世界边界相撞,则使用`true`,否则使用`false`. |
| bounceX | number | 是 |  | 如果给它替换了机体的`worldBounce.x`值. |
| bounceY | number | 是 |  | 如果给它替换了机体的`worldBounce.y`值. |
| onWorldBounds | boolean | 是 |  | 如果给它替换了机体的`onWorldBounds`值. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L1959](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1959)  
引入版本：3.0.0


---

### setDamping {#setDamping}

#### \<instance> setDamping(value) {#instance-setdampingvalue}


**说明:**

如果此天体正在使用 `drag` 来控制拖曳方式的应用。 如果设置为 `true` 拖曳, 则会使用一个起锚效果而不是线性方法。 如果您正在创建一个让天体在任意角度自由移动的游戏( 即像小行星中的飞船) , 那么您将会通过使用起锚方式获得一个更平滑和更直观的减速, 避免线性减速而容易触发轴线的拖曳 。

如果您启用此属性, 您应该使用比线性小得多的 `drag`值, 因为这些值被用作速度的乘数。 例如 0. 95 等值将给一个良好的慢减速, 在那里, 如 0. 5 等较小的值几乎会立即停止一个对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | `true`使用坝式,或`false`使用拖动. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2346](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2346)  
引入版本：3.50.0


---

### setDirectControl {#setDirectControl}

#### \<instance> setDirectControl([value]) {#instance-setdirectcontrolvalue}


**说明:**

设定此天体是否应该根据它在每个框架的位置变化来计算其速度。 默认, 即不这样做, 意味着您通过直接设置速度来让此天体移动。 然而, 如果您试图通过调温移动此天体, 或者它遵循路径, 那么您应该启用它。 这将允许它与其他天体碰撞, 如果您只是直接改变它的位置, 则不可能实现 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 如果机体根据位置变化计算速度,则`true`,否则则`false`. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L1935](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1935)  
引入版本：3.70.0


---

### setDrag {#setDrag}

#### \<instance> setDrag(x, [y]) {#instance-setdragx-y}


**说明:**

设置身体拖动。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 水平元件,以像素每秒平方英寸表示. |
| y | number | 是 | "x" | 垂直的组件,以像素每秒平方表示. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2328](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2328)  
引入版本：3.0.0


---

### setDragX {#setDragX}

#### \<instance> setDragX(value) {#instance-setdragxvalue}


**说明:**

设置身体水平拖曳。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 拖曳,以像素每秒平方英寸表示. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2371](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2371)  
引入版本：3.0.0


---

### setDragY {#setDragY}

#### \<instance> setDragY(value) {#instance-setdragyvalue}


**说明:**

设置天体的垂直拖曳。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 拖曳,以像素每秒平方英寸表示. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2388](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2388)  
引入版本：3.0.0


---

### setEnable {#setEnable}

#### \<instance> setEnable([value]) {#instance-setenablevalue}


**说明:**

设定身体的`enable`属性.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 指定 `enable` 的值 。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2596](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2596)  
引入版本：3.15.0


---

### setFriction {#setFriction}

#### \<instance> setFriction(x, [y]) {#instance-setfrictionx-y}


**说明:**

设机身摩擦.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 水平元件,相对1. |
| y | number | 是 | "x" | 垂直元件,相对1. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2457](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2457)  
引入版本：3.0.0


---

### setFrictionX {#setFrictionX}

#### \<instance> setFrictionX(value) {#instance-setfrictionxvalue}


**说明:**

设置机体水平摩擦.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 摩擦值,相对1. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2475](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2475)  
引入版本：3.0.0


---

### setFrictionY {#setFrictionY}

#### \<instance> setFrictionY(value) {#instance-setfrictionyvalue}


**说明:**

设置身体的垂直摩擦.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 摩擦值,相对1. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2492](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2492)  
引入版本：3.0.0


---

### setGameObject {#setGameObject}

#### \<instance> setGameObject(gameObject, [enable]) {#instance-setgameobjectgameobject-enable}


**说明:**

将此天体指定为新的游戏对象 。

从物理世界中移除此天体,指派给新的游戏对象,调用`setSize`,然后再次将此天体添加回世界,设置它启用,除非`enable`参数设置到`false`.

如果这个机构已经有一个游戏对象,那么它会首先从该游戏对象中移除自己.

如果给定的`gameObject`没有`body`属性,则它被创建,这个机构被分配给它.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 指定此天体的游戏对象 。 |
| enable | boolean | 是 | true | 自动启用此天体用于物理 。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L1414](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1414)  
引入版本：3.60.0


---

### setGravity {#setGravity}

#### \<instance> setGravity(x, [y]) {#instance-setgravityx-y}


**说明:**

设定身体的引力。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 水平元件,以像素每秒平方英寸表示. |
| y | number | 是 | "x" | 垂直的组件,以像素每秒平方表示. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2405](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2405)  
引入版本：3.0.0


---

### setGravityX {#setGravityX}

#### \<instance> setGravityX(value) {#instance-setgravityxvalue}


**说明:**

设定天体的横向引力 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 重力,以像素每秒平方英寸表示. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2423](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2423)  
引入版本：3.0.0


---

### setGravityY {#setGravityY}

#### \<instance> setGravityY(value) {#instance-setgravityyvalue}


**说明:**

设定天体的垂直重力.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 重力,以像素每秒平方英寸表示. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2440](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2440)  
引入版本：3.0.0


---

### setImmovable {#setImmovable}

#### \<instance> setImmovable([value]) {#instance-setimmovablevalue}


**说明:**

设定身体的`immovable`属性.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 指定 `immovable` 的值 。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2577](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2577)  
引入版本：3.0.0


---

### setMass {#setMass}

#### \<instance> setMass(value) {#instance-setmassvalue}


**说明:**

设定身体的质量。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 质量值,相对于1. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2560](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2560)  
引入版本：3.0.0


---

### setMaxSpeed {#setMaxSpeed}

#### \<instance> setMaxSpeed(value) {#instance-setmaxspeedvalue}


**说明:**

设定天体可移动的最大速度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 最大速度值, 以像素每秒为单位。 设置为负值以禁用 。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2114)  
引入版本：3.16.0


---

### setMaxVelocity {#setMaxVelocity}

#### \<instance> setMaxVelocity(x, [y]) {#instance-setmaxvelocityx-y}


**说明:**

设定身体的最大速度 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 水平速度,以像素每秒为单位. |
| y | number | 是 | "x" | 垂直速度,以像素每秒为单位. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2062](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2062)  
引入版本：3.10.0


---

### setMaxVelocityX {#setMaxVelocityX}

#### \<instance> setMaxVelocityX(value) {#instance-setmaxvelocityxvalue}


**说明:**

设定天体的最大水平速度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 最大水平速度,以每秒像素计. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2080](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2080)  
引入版本：3.50.0


---

### setMaxVelocityY {#setMaxVelocityY}

#### \<instance> setMaxVelocityY(value) {#instance-setmaxvelocityyvalue}


**说明:**

设定天体的最大垂直速度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 最大垂直速度,以像素每秒为单位. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2097](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2097)  
引入版本：3.50.0


---

### setOffset {#setOffset}

#### \<instance> setOffset(x, [y]) {#instance-setoffsetx-y}


**说明:**

设定天体位置的偏移值, 以设定其游戏对象位置。 天体的 `position` 在下一个 `preUpdate` 之前不会更改 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 水平偏移,以源像素计. |
| y | number | 是 | "x" | 垂直偏移, 以源像素计 。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L1393](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1393)  
引入版本：3.0.0


---

### setSize {#setSize}

#### \<instance> setSize([width], [height], [center]) {#instance-setsizewidth-height-center}


**说明:**

大小和位置 。 如果 `center` 是真的, 修改 body `offset` 。 如果没有提供宽度和高度, 找到框架, 则重新调整宽度和高度, 跟当前框架匹配 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 是 |  | 以像素表示的天体宽度。 无法为零。 如果不给出, 而母游戏对象有框架, 它会使用框架宽度 。 |
| height | number | 是 |  | 以像素表示的天体高度。 无法为 0。 如果不给出, 而母游戏对象有框架, 它会使用框架高度 。 |
| center | boolean | 是 | true | 修改 body 的 `offset`, 将 body 的中心置于其游戏对象的中心。 只有在游戏对象有 `getCenter` 方法时才有效 。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L1470](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1470)  
引入版本：3.0.0


---

### setSlideFactor {#setSlideFactor}

#### \<instance> setSlideFactor(x, [y]) {#instance-setslidefactorx-y}


**说明:**

设置此正文的幻灯片因数。

幻灯片因子控制当此天体被另一个天体推动时,其速度被保存多少 。

默认值为 1, 这意味着它会承担推力中给出的所有速度。 您可以调整这个值, 以控制这个机构在推力结束时保留多少速度 。

例如,0的值将允许这个正体被推,但在推后完全保持静止,比如在像Sokoban这样的游戏中可以看到.

或者您可以设置一个中点, 例如0. 25, 可以在推力结束时保留 25% 的 原速度。 您可以将这个方法与 `setDrag()` 方法结合起来, 以创建减速 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 水平滑动因子。 0 到 1 之间的数值 。 |
| y | number | 是 | "x" | 垂直滑动因子。 0 到 1 之间的数值 。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2131](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2131)  
引入版本：3.70.0


---

### setVelocity {#setVelocity}

#### \<instance> setVelocity(x, [y]) {#instance-setvelocityx-y}


**说明:**

设定身体的速度。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 水平速度,以像素每秒为单位. |
| y | number | 是 | "x" | 垂直速度,以像素每秒为单位. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2009](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2009)  
引入版本：3.0.0


---

### setVelocityX {#setVelocityX}

#### \<instance> setVelocityX(value) {#instance-setvelocityxvalue}


**说明:**

设定身体的横向速度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 速度,以像素每秒为单位. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2032](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2032)  
引入版本：3.0.0


---

### setVelocityY {#setVelocityY}

#### \<instance> setVelocityY(value) {#instance-setvelocityyvalue}


**说明:**

设定身体的垂直速度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 速度,以像素每秒为单位. |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L2047](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L2047)  
引入版本：3.0.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

设置加速,速度,速度为0.


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 身体的这个物体。


> 源码：[src/physics/arcade/Body.js#L1625](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1625)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update(delta) {#instance-updatedelta}


**说明:**

执行单个物理步骤,并更新身体速度,角度,速度和其他属性.

这种方法可以根据物理步法速率,每个游戏帧可以称为多次.

其结果被同步回`postUpdate`中的游戏对象.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delta | number | 否 | 三角洲时间,几秒钟, 过去了,从上一个框架。 |


**Fires:** [Phaser.Physics.Arcade.Events#event:WORLD_BOUNDS](/api/event/physics-arcade-events#world_bounds)


> 源码：[src/physics/arcade/Body.js#L1159](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1159)  
引入版本：3.0.0


---

### updateBounds {#updateBounds}

#### \<instance> updateBounds() {#instance-updatebounds}


**说明:**

更新天体的 `transform`, `width`, `height`,和 `center` 。从它的游戏对象。 `position` 并没有改变。


> 源码：[src/physics/arcade/Body.js#L965](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L965)  
引入版本：3.0.0


---

### updateCenter {#updateCenter}

#### \<instance> updateCenter() {#instance-updatecenter}


**说明:**

更新天体的 `center` 从其 `position`, `width`,和 `height`.


> 源码：[src/physics/arcade/Body.js#L1036](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1036)  
引入版本：3.0.0


---

### updateFromGameObject {#updateFromGameObject}

#### \<instance> updateFromGameObject() {#instance-updatefromgameobject}


**说明:**

更新天体的 `position`, `width`, `height`,和 `center` 从其游戏对象中 `offset`.

不需要将它称为动态天体,因为它在物理步骤中会自动发生。但是如果你修改了天体抵消或游戏对象变换,需要立即读取天体的新`position`或`center`,你就可以使用它。

为了让身体与其游戏对象重同步,使用`reset()`代替.


> 源码：[src/physics/arcade/Body.js#L1047](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1047)  
引入版本：3.24.0


---

### willDrawDebug {#willDrawDebug}

#### \<instance> willDrawDebug() {#instance-willdrawdebug}


**说明:**

是否将绘制此天体到调试显示 。


**返回值:** boolean - 如果启用 `debugShowBody` 或 `debugShowVelocity` , 则为真 。


> 源码：[src/physics/arcade/Body.js#L1922](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Body.js#L1922)  
引入版本：3.0.0


---

---
