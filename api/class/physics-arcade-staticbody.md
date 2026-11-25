# StaticBody {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-arcade-staticbody)

静态Arcade 物理体.

静态体从不移动, 也并不自动与其父游戏对象同步。 这意味着, 如果您创建或添加了 静态体后对 静态体的起源、 位置或比例表 有任何更改, 您需要手动更新 。

静态体可以与其他体相撞,但从不因碰撞而动.

静态物理体对平台、墙壁、地板和其他不可移动的环境元素来说是理想的。 与动态物理体不同,它们没有速度、加速或重力,也不被碰撞所移动。

它的动态对应器是[Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body).

**构造函数**

`new StaticBody(world, [gameObject])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| world | [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) | 否 | 弧场物理模拟 这个静态体属于。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 是 | 游戏对象属于此物理体。 至 Phaser 3. 60 此对象现在可选 。 |

---


**作用域**: static


**继承**

> [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision)  



> 源码：[src/physics/arcade/StaticBody.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L15)  
引入版本：3.0.0

## 公开成员 {#public-members}

### allowGravity {#allowGravity}

#### allowGravity: boolean {#allowgravity-boolean}


**说明:**

弧场物理模拟所预期的恒定`false`值.


> 源码：[src/physics/arcade/StaticBody.js#L237](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L237)  
引入版本：3.0.0


---

### blocked {#blocked}

#### blocked: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](/api/typedef/types-physics-arcade#arcadebodycollision) {#blocked-phasertypesphysicsarcadearcadebodycollision}


**说明:**

此属性保存为与动态物理体兼容。 请避免使用 。


> 源码：[src/physics/arcade/StaticBody.js#L443](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L443)  
引入版本：3.0.0


---

### bottom {#bottom}

#### bottom: number {#bottom-number}


**说明:**

静态Body区域的最低y坐标(y + 高度)


> 源码：[src/physics/arcade/StaticBody.js#L1095](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L1095)  
引入版本：3.0.0


---

### bounce {#bounce}

#### bounce: [Phaser.Math.Vector2](/api/class/math-vector2) {#bounce-phasermathvector2}


**说明:**

碰撞后,相对于1. 静态体总是零。


> 源码：[src/physics/arcade/StaticBody.js#L258](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L258)  
引入版本：3.0.0


---

### center {#center}

#### center: [Phaser.Math.Vector2](/api/class/math-vector2) {#center-phasermathvector2}


**说明:**

静态物理体边界的中心,这是它的中点 `position` (左上角) 及其右下角.


> 源码：[src/physics/arcade/StaticBody.js#L217](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L217)  
引入版本：3.0.0


---

### checkCollision {#checkCollision}

#### checkCollision: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](/api/typedef/types-physics-arcade#arcadebodycollision) {#checkcollision-phasertypesphysicsarcadearcadebodycollision}


**说明:**

是否检查此静态Body 是否发生碰撞以及方向。 您可以设置 `checkCollision.none = true` 来禁用碰撞检查 。


> 源码：[src/physics/arcade/StaticBody.js#L413](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L413)  
引入版本：3.0.0


---

### collideWorldBounds {#collideWorldBounds}

#### collideWorldBounds: boolean {#collideworldbounds-boolean}


**说明:**

是否此静态Body与世界边界相互作用。 总是对静态物理体不实( 静态物理体从未与世界边界相撞 ) 。


> 源码：[src/physics/arcade/StaticBody.js#L401](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L401)  
引入版本：3.0.0


---

### collisionCategory {#collisionCategory}

#### collisionCategory: number {#collisioncategory-number}


**说明:**

Arcade 物理体碰撞类.

它可以设置为任何有效的碰撞位域值 。

详见`setCollisionCategory`方法.


> 源码：[src/physics/arcade/StaticBody.js#L463](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L463)  
引入版本：3.70.0


---

### collisionMask {#collisionMask}

#### collisionMask: number {#collisionmask-number}


**说明:**

Arcade 物理碰撞罩.

详见`setCollidesWith`方法.


> 源码：[src/physics/arcade/StaticBody.js#L476](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L476)  
引入版本：3.70.0


---

### customSeparateX {#customSeparateX}

#### customSeparateX: boolean {#customseparatex-boolean}


**说明:**

旗子会破坏碰撞物理体的默认水平分离。 将自己的 `collideHandler` 传递给碰撞器 。


> 源码：[src/physics/arcade/StaticBody.js#L341](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L341)  
引入版本：3.0.0


---

### customSeparateY {#customSeparateY}

#### customSeparateY: boolean {#customseparatey-boolean}


**说明:**

旗子会解除碰撞体的默认垂直分离。 将自己的 `collideHandler` 传递给碰撞器 。


> 源码：[src/physics/arcade/StaticBody.js#L351](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L351)  
引入版本：3.0.0


---

### debugBodyColor {#debugBodyColor}

#### debugBodyColor: number {#debugbodycolor-number}


**说明:**

此静态体在调试显示上的颜色 。


> 源码：[src/physics/arcade/StaticBody.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L116)  
引入版本：3.0.0


---

### debugShowBody {#debugShowBody}

#### debugShowBody: boolean {#debugshowbody-boolean}


**说明:**

静态物理体的边界是否被引向调试显示 。


> 源码：[src/physics/arcade/StaticBody.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L107)  
引入版本：3.0.0


---

### embedded {#embedded}

#### embedded: boolean {#embedded-boolean}


**说明:**

这颗静态Body是否曾与另一个同时同时不移动.


> 源码：[src/physics/arcade/StaticBody.js#L391](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L391)  
引入版本：3.0.0


---

### enable {#enable}

#### enable: boolean {#enable-boolean}


**说明:**

此静态体是否通过物理模拟更新 。


> 源码：[src/physics/arcade/StaticBody.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L125)  
引入版本：3.0.0


---

### gameObject {#gameObject}

#### gameObject: [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) {#gameobject-phasergameobjectsgameobject}


**说明:**

此静态物理体所属的游戏对象 。

至Phaser 3.60,此为现在可选,可以不定义.


> 源码：[src/physics/arcade/StaticBody.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L86)  
引入版本：3.0.0


---

### gravity {#gravity}

#### gravity: [Phaser.Math.Vector2](/api/class/math-vector2) {#gravity-phasermathvector2}


**说明:**

特意应用到此物理体的引力。 值以像素每秒平方位值。 对于静态物理体, 总是为零 。


> 源码：[src/physics/arcade/StaticBody.js#L248](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L248)  
引入版本：3.0.0


---

### halfHeight {#halfHeight}

#### halfHeight: number {#halfheight-number}


**说明:**

静态体高度的一半,以像素表示,如果静态体是圆形的,这也是静态体的半径.


> 源码：[src/physics/arcade/StaticBody.js#L207](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L207)  
引入版本：3.0.0


---

### halfWidth {#halfWidth}

#### halfWidth: number {#halfwidth-number}


**说明:**

静态体宽度的一半,以像素表示,如果静态体是圆形的,这也是静态体的半径.


> 源码：[src/physics/arcade/StaticBody.js#L197](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L197)  
引入版本：3.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

静态体的边界高度,以像素表示。如果静态体是圆形的,这也即静态体的直径。


> 源码：[src/physics/arcade/StaticBody.js#L187](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L187)  
引入版本：3.0.0


---

### immovable {#immovable}

#### immovable: boolean {#immovable-boolean}


**说明:**

是否可以通过与另一物理体碰撞来移动此物理体.


> 源码：[src/physics/arcade/StaticBody.js#L312](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L312)  
引入版本：3.0.0


---

### isBody {#isBody}

#### isBody: boolean {#isbody-boolean}


**说明:**

快速测试的旗帜表示这个是物理体, 用于世界碰撞处理器。


> 源码：[src/physics/arcade/StaticBody.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L97)  
引入版本：3.60.0


---

### isCircle {#isCircle}

#### isCircle: boolean {#iscircle-boolean}


**说明:**

无论是这个静态体的边界是圆形(`true`)还是矩形(`false`).


> 源码：[src/physics/arcade/StaticBody.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L135)  
引入版本：3.0.0


---

### left {#left}

#### left: number {#left-number}


**说明:**

返回 StaticBody 区域的左侧最左侧x坐标 。


> 源码：[src/physics/arcade/StaticBody.js#L1044](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L1044)  
引入版本：3.0.0


---

### mass {#mass}

#### mass: number {#mass-number}


**说明:**

相对于默认单位(1)的静态Body惯性,用`bounce`,这影响到碰撞时的动力(速度)的交换.


> 源码：[src/physics/arcade/StaticBody.js#L302](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L302)  
引入版本：3.0.0


---

### offset {#offset}

#### offset: [Phaser.Math.Vector2](/api/class/math-vector2) {#offset-phasermathvector2}


**说明:**

由[Phaser.Physics.Arcade.StaticBody#setCircle](/api/class/physics-arcade-staticbody#setCircle)或[Phaser.Physics.Arcade.StaticBody#setSize](/api/class/physics-arcade-staticbody#setSize)设定的偏移.

这不影响静态体的地位,因为静态体不遵循它的游戏对象.


> 源码：[src/physics/arcade/StaticBody.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L156)  
引入版本：3.0.0


---

### onCollide {#onCollide}

#### onCollide: boolean {#oncollide-boolean}


**说明:**

当这个静态Body和另一个静态碰撞时, 模拟是否释放出 `collide`事件 。


> 源码：[src/physics/arcade/StaticBody.js#L282](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L282)  
引入版本：3.0.0


---

### onOverlap {#onOverlap}

#### onOverlap: boolean {#onoverlap-boolean}


**说明:**

当静态Body与另一个静态重叠时, 模拟是否释放出 `overlap` 事件 。


> 源码：[src/physics/arcade/StaticBody.js#L292](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L292)  
引入版本：3.0.0


---

### onWorldBounds {#onWorldBounds}

#### onWorldBounds: boolean {#onworldbounds-boolean}


**说明:**

模拟是否在静态Body与世界边界碰撞时发出 `worldbounds`事件。 总是对静态物理体不实 。 (静态物理体从未与世界边界碰撞, 也从未触发 `worldbounds`事件 。 )


> 源码：[src/physics/arcade/StaticBody.js#L270](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L270)  
引入版本：3.0.0


---

### overlapR {#overlapR}

#### overlapR: number {#overlapr-number}


**说明:**

如果这个静态Body是循环的,并且与另一个循环体相撞,则重叠的量(在分离前).


> 源码：[src/physics/arcade/StaticBody.js#L381](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L381)  
引入版本：3.0.0


---

### overlapX {#overlapX}

#### overlapX: number {#overlapx-number}


**说明:**

如果此物理体与另一物理体相撞,则水平重叠(在分离前)的幅度。


> 源码：[src/physics/arcade/StaticBody.js#L361](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L361)  
引入版本：3.0.0


---

### overlapY {#overlapY}

#### overlapY: number {#overlapy-number}


**说明:**

如果此物理体正与另一个物理体相撞,则垂直重叠(在分离之前)的数量。


> 源码：[src/physics/arcade/StaticBody.js#L371](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L371)  
引入版本：3.0.0


---

### physicsType {#physicsType}

#### physicsType: number {#physicstype-number}


**说明:**

静态博迪的物理类型(默认静态).


> 源码：[src/physics/arcade/StaticBody.js#L453](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L453)  
引入版本：3.0.0


---

### position {#position}

#### position: [Phaser.Math.Vector2](/api/class/math-vector2) {#position-phasermathvector2}


**说明:**

这个静态体在模拟中的位置.


> 源码：[src/physics/arcade/StaticBody.js#L168](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L168)  
引入版本：3.0.0


---

### pushable {#pushable}

#### pushable: boolean {#pushable-boolean}


**说明:**

如果此物理体能被另一个物理体推动, 则设定 。

无法推动的躯体会反射出它被赋予碰撞体的全部速度。 如果这个躯体也不可推动,那么它们之间的分离就会平分。

如果你想让物理体永远不动或分开,请看`setImmovable`方法.

默认,静态体是不可推的。


> 源码：[src/physics/arcade/StaticBody.js#L322](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L322)  
引入版本：3.50.0


---

### radius {#radius}

#### radius: number {#radius-number}


**说明:**

如果这个静态体是圆形的,这是[Phaser.Physics.Arcade.StaticBody#setCircle](/api/class/physics-arcade-staticbody#setCircle)设定的边界半径,以像素表示。等于`halfWidth`。


> 源码：[src/physics/arcade/StaticBody.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L145)  
引入版本：3.0.0


---

### right {#right}

#### right: number {#right-number}


**说明:**

静态Body区最右最左的x坐标.


> 源码：[src/physics/arcade/StaticBody.js#L1061](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L1061)  
引入版本：3.0.0


---

### top {#top}

#### top: number {#top-number}


**说明:**

静态Body地区最高的Y坐标


> 源码：[src/physics/arcade/StaticBody.js#L1078](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L1078)  
引入版本：3.0.0


---

### touching {#touching}

#### touching: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](/api/typedef/types-physics-arcade#arcadebodycollision) {#touching-phasertypesphysicsarcadearcadebodycollision}


**说明:**

此属性保存为与动态物理体兼容。 请避免使用 。


> 源码：[src/physics/arcade/StaticBody.js#L422](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L422)  
引入版本：3.0.0


---

### velocity {#velocity}

#### velocity: [Phaser.Math.Vector2](/api/class/math-vector2) {#velocity-phasermathvector2}


**说明:**

用于计算 Arcade 物理模拟的恒定零速度.


> 源码：[src/physics/arcade/StaticBody.js#L227](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L227)  
引入版本：3.0.0


---

### wasTouching {#wasTouching}

#### wasTouching: [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](/api/typedef/types-physics-arcade#arcadebodycollision) {#wastouching-phasertypesphysicsarcadearcadebodycollision}


**说明:**

此属性用于与动态物理体兼容。 避免使用。 对于静态物理体来说, 值总是不正确的 。


> 源码：[src/physics/arcade/StaticBody.js#L432](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L432)  
引入版本：3.0.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

静态体的边界宽度,以像素表示,如果静态体是圆形的,这也即静态体的直径.


> 源码：[src/physics/arcade/StaticBody.js#L177](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L177)  
引入版本：3.0.0


---

### world {#world}

#### world: [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) {#world-phaserphysicsarcadeworld}


**说明:**

弧场物理模拟 这个静态体属于。


> 源码：[src/physics/arcade/StaticBody.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L77)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

静态波迪的x坐标.


> 源码：[src/physics/arcade/StaticBody.js#L994](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L994)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

静态Body的Y坐标。


> 源码：[src/physics/arcade/StaticBody.js#L1019](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L1019)  
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

### deltaAbsX {#deltaAbsX}

#### \<instance> deltaAbsX() {#instance-deltaabsx}


**说明:**

此 StaticBody 的水平位置从上一步的绝对( 非负数) 变化 。 总是零 。


**返回值:** number - 静态物理体总是零。


> 源码：[src/physics/arcade/StaticBody.js#L849](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L849)  
引入版本：3.0.0


---

### deltaAbsY {#deltaAbsY}

#### \<instance> deltaAbsY() {#instance-deltaabsy}


**说明:**

这个 StaticBody 的垂直位置从上一步的绝对( 非负数) 变化 。 总是零 。


**返回值:** number - 静态物理体总是零。


> 源码：[src/physics/arcade/StaticBody.js#L862](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L862)  
引入版本：3.0.0


---

### deltaX {#deltaX}

#### \<instance> deltaX() {#instance-deltax}


**说明:**

与前一步相比, 这个 StaticBody 的水平位置的变化 。 总是零 。


**返回值:** number - 自最后一步以来水平位置的变化, 以像素表示。 对于静态物理体来说, 总是零 。


> 源码：[src/physics/arcade/StaticBody.js#L875](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L875)  
引入版本：3.0.0


---

### deltaY {#deltaY}

#### \<instance> deltaY() {#instance-deltay}


**说明:**

与上一步相比, 这个 StaticBody 的垂直位置的变化 。 总是零 。


**返回值:** number - 上一步以来垂直位置的变化, 以像素表示。 对于静态物理体, 总是零 。


> 源码：[src/physics/arcade/StaticBody.js#L888](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L888)  
引入版本：3.0.0


---

### deltaZ {#deltaZ}

#### \<instance> deltaZ() {#instance-deltaz}


**说明:**

静态Body的旋转变化 总是零


**返回值:** number - 静态Body的旋转变化 总是零


> 源码：[src/physics/arcade/StaticBody.js#L901](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L901)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

禁用此物理体,并在下一步中标记为销毁。


> 源码：[src/physics/arcade/StaticBody.js#L914](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L914)  
引入版本：3.0.0


---

### drawDebug {#drawDebug}

#### \<instance> drawDebug(graphic) {#instance-drawdebuggraphic}


**说明:**

为视觉调试目的绘制 StaticBody 的图形化表示。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| graphic | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 用于 StaticBody 调试绘图的图形对象 。 |


> 源码：[src/physics/arcade/StaticBody.js#L927](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L927)  
引入版本：3.0.0


---

### getBounds {#getBounds}

#### \<instance> getBounds(obj) {#instance-getboundsobj}


**说明:**

返回 StaticBody 左上和右下点的 x 和 Y 坐标。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| obj | [Phaser.Types.Physics.Arcade.ArcadeBodyBounds](/api/typedef/types-physics-arcade#arcadebodybounds) | 否 | 将持有界坐标的物体。 |


**返回值:** [Phaser.Types.Physics.Arcade.ArcadeBodyBounds](/api/typedef/types-physics-arcade#arcadebodybounds) - 被传递的同一件物体 `x`, `y`, `right` 财务报告和已审计财务报表 `bottom` 与 StaticBody 的值匹配的值。


> 源码：[src/physics/arcade/StaticBody.js#L803](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L803)  
引入版本：3.0.0


---

### hitTest {#hitTest}

#### \<instance> hitTest(x, y) {#instance-hittestx-y}


**说明:**

检查是否给定的 x,y 坐标与这个静态物理体相撞 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 坐标是用来检查这个物理体的 |
| y | number | 否 | 与这个物理体相对应的Y坐标 |


**返回值:** boolean - 如果给定的坐标位于这个机构,则`true`,否则则`false`.


> 源码：[src/physics/arcade/StaticBody.js#L823](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L823)  
引入版本：3.0.0


---

### postUpdate {#postUpdate}

#### \<instance> postUpdate() {#instance-postupdate}


**说明:**

NOOP


> 源码：[src/physics/arcade/StaticBody.js#L839](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L839)  
引入版本：3.12.0


---

### reset {#reset}

#### \<instance> reset([x], [y]) {#instance-resetx-y}


**说明:**

将这个静态体重置到其父游戏对象的位置.

如果给出了`x`和`y`,则父游戏对象被放置在那里,而这个静态对象被集中到它上。否则这个静态对象被以游戏对象当前的位置为中心.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 是 | x 坐标重置物理体为。 如果不给定, 则使用父游戏对象的坐标 。 |
| y | number | 是 | 将主体重置为的y坐标。 如果不给出, 则使用父游戏对象的坐标 。 |


> 源码：[src/physics/arcade/StaticBody.js#L757](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L757)  
引入版本：3.0.0


---

### setCircle {#setCircle}

#### \<instance> setCircle(radius, [offsetX], [offsetY]) {#instance-setcircleradius-offsetx-offsety}


**说明:**

设置此静态体具有圆形体,并设定其大小和位置.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| radius | number | 否 | 静态Body的半径,以像素表示. |
| offsetX | number | 是 | 其游戏对象的StaticBody的横向偏移,以像素表示. |
| offsetY | number | 是 | StaticBody从它的游戏对象中垂直的抵消,以像素表示. |


**返回值:** [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) - 这个静态物体。


> 源码：[src/physics/arcade/StaticBody.js#L701](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L701)  
引入版本：3.0.0


---

### setGameObject {#setGameObject}

#### \<instance> setGameObject(gameObject, [update], [enable]) {#instance-setgameobjectgameobject-update-enable}


**说明:**

更改此物理体必须使用的游戏对象 。

首先它从旧游戏对象中删除其引用,然后设定新的对象.

如果此物理体有纹理帧, 则将调整其大小, 以匹配给定的游戏对象的框架尺寸。 您可以选择更新此物理体的位置和尺寸, 以反映新游戏对象的位置和尺寸 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 指定此物理体的游戏对象 。 |
| update | boolean | 是 | true | 重新定位和调整此物理体大小以匹配新的游戏对象吗 ? |
| enable | boolean | 是 | true | 自动启用此物理体用于物理 。 |


**返回值:** [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) - 这个静态物体。


> 源码：[src/physics/arcade/StaticBody.js#L512](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L512)  
引入版本：3.1.0


---

### setMass {#setMass}

#### \<instance> setMass(value) {#instance-setmassvalue}


**说明:**

设置静态Body的质量。如果通过值小于或等于零,则将质量设定为0.1。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 将质量设置为. 0 或 更少的值改为 0.1 。 |


**返回值:** [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) - 这个静态物体。


> 源码：[src/physics/arcade/StaticBody.js#L971](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L971)  
引入版本：3.0.0


---

### setOffset {#setOffset}

#### \<instance> setOffset(x, y) {#instance-setoffsetx-y}


**说明:**

将静态体定位于其游戏对象的偏移处。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 游戏对象`x`的静态体横向抵消. |
| y | number | 否 | 游戏对象`y`的静态体的垂直偏移. |


**返回值:** [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) - 这个静态物体。


> 源码：[src/physics/arcade/StaticBody.js#L604](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L604)  
引入版本：3.4.0


---

### setSize {#setSize}

#### \<instance> setSize([width], [height], [center]) {#instance-setsizewidth-height-center}


**说明:**

设置静态体的大小。 `center` 是真的时, 也会重新定位它。 如果没有提供宽度和高度, 并且找到一个框架, 则重新设置宽度和高度以匹配当前框架 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 是 |  | 静态物理体的宽度以像素表示。 无法为零。 如果不给出, 而父游戏对象有框架, 它会使用框架宽度 。 |
| height | number | 是 |  | 静态物理体的高度以像素表示。 无法为零。 如果不给出, 而父游戏对象有框架, 它会使用框架高度 。 |
| center | boolean | 是 | true | 将静态物理体的中心置于其游戏对象的中心。 只有游戏对象具有 `getCenter` 方法时才有效 。 |


**返回值:** [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) - 这个静态物体。


> 源码：[src/physics/arcade/StaticBody.js#L636](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L636)  
引入版本：3.0.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

NOOP 函数。 静态体无法停止 。


**返回值:** [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) - 这个静态物体。


> 源码：[src/physics/arcade/StaticBody.js#L790](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L790)  
引入版本：3.0.0


---

### updateCenter {#updateCenter}

#### \<instance> updateCenter() {#instance-updatecenter}


**说明:**

更新静态Body的`center` 从它的`position`和维度。


> 源码：[src/physics/arcade/StaticBody.js#L746](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L746)  
引入版本：3.0.0


---

### updateFromGameObject {#updateFromGameObject}

#### \<instance> updateFromGameObject() {#instance-updatefromgameobject}


**说明:**

与父游戏对象同步静态体的位置和大小.


**返回值:** [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) - 这个静态物体。


> 源码：[src/physics/arcade/StaticBody.js#L575](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L575)  
引入版本：3.1.0


---

### willDrawDebug {#willDrawDebug}

#### \<instance> willDrawDebug() {#instance-willdrawdebug}


**说明:**

表示静态Body是否将在postUpdate期间显示调试可视化.


**返回值:** boolean - StaticBody是否在postUpdate期间显示调试可视化.


> 源码：[src/physics/arcade/StaticBody.js#L958](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/StaticBody.js#L958)  
引入版本：3.0.0


---

---
