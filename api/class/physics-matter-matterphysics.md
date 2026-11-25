# MatterPhysics {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-matter-matterphysics)

Phaser物质插件提供了在您的Phaser游戏中使用物质JS物理引擎的能力.

与拱廊物理不同的是,另一个物理系统提供Phaser, Matter JS是一个全身物理系统。

* 硬体

* 复合体

* 复合体

* 孔洞和对流船体

* 物理性质(质量、面积、密度等)

* 复原(弹性和无弹性碰撞)

* 碰撞(宽相、中相和窄相)

* 稳定堆放和休息

* 保持势头

* 防滑和阻力

* Constraints

* Gravity

* 睡眠和静态身体

* 圆角( 圆角)

* 视图(翻译、缩放)

* 碰撞查询(广播、区域测试)

* 时间缩放( 慢- 摩, 速度)

Matter 配置是通过 Matter World Config 对象处理的,可以通过 Phaser Game Config 或 Phaser 组合 Scene Config 来传递。这里是一个基本的例子:

```js
physics: {
    default: 'matter',
    matter: {
        enableSleeping: true,
        gravity: {
            y: 0
        },
        debug: {
            showBody: true,
            showStaticBody: true
        }
    }
}
```

这个类作为Phaser场景和物质引擎的单实例之间的接口.

使用它来访问最常用的 Matter 特性和帮助器函数 。

详情、文件和实例请见Mative JS网站:[https://brm.io/matter-js/](https://brm.io/matter-js/)

**构造函数**

`new MatterPhysics(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 拥有这个物质物理实例的 Phaser场景。 |

---


**作用域**: static

> 源码：[src/physics/matter-js/MatterPhysics.js#L38](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L38)  
引入版本：3.0.0

## 公开成员 {#public-members}

### add {#add}

#### add: [Phaser.Physics.Matter.Factory](/api/class/physics-matter-factory) {#add-phaserphysicsmatterfactory}


**说明:**

物质工厂的例子。 这个类提供了许多功能, 用于创建各种各样的物理对象, 并自动添加到物质世界 。

您可以使用这个类来削减游戏中所需的代码数量, 但是, 使用工厂是完全可选的, 并且应该被看作是一种发展援助。 完全可以不使用它而创建和添加 Matter 的组件 。


> 源码：[src/physics/matter-js/MatterPhysics.js#L138](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L138)  
引入版本：3.0.0


---

### axes {#axes}

#### axes: MatterJS.AxesFactory {#axes-matterjsaxesfactory}


**说明:**

参考`Matter.Axes`模块.

`Matter.Axes`模块包含创建和操纵各组轴的方法.


> 源码：[src/physics/matter-js/MatterPhysics.js#L304](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L304)  
引入版本：3.22.0


---

### bodies {#bodies}

#### bodies: MatterJS.BodiesFactory {#bodies-matterjsbodiesfactory}


**说明:**

参考`Matter.Bodies`模块.

`Matter.Bodies`模块包含工厂方法,用于创建具有常用体型配置的刚性体(如矩形,圆形和其他多边形).


> 源码：[src/physics/matter-js/MatterPhysics.js#L278](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L278)  
引入版本：3.18.0


---

### body {#body}

#### body: MatterJS.BodyFactory {#body-matterjsbodyfactory}


**说明:**

参考`Matter.Body`模块.

`Matter.Body`模块包含创建和操纵车体模型的方法. A`Matter.Body`是一个刚性车体,可以由`Matter.Engine`模拟. 常用车体配置(如矩形,圆形和其他多边形)的工厂可以在`Bodies`模块中找到.


> 源码：[src/physics/matter-js/MatterPhysics.js#L164](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L164)  
引入版本：3.18.0


---

### bodyBounds {#bodyBounds}

#### bodyBounds: [Phaser.Physics.Matter.BodyBounds](/api/class/physics-matter-bodybounds) {#bodybounds-phaserphysicsmatterbodybounds}


**说明:**

身体边界类的一个实例。该类包含用于从物理体的界限周围的多个点获得世界位置的函数。


> 源码：[src/physics/matter-js/MatterPhysics.js#L152](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L152)  
引入版本：3.22.0


---

### bounds {#bounds}

#### bounds: MatterJS.BoundsFactory {#bounds-matterjsboundsfactory}


**说明:**

参考`Matter.Bounds`模块.

`Matter.Bounds`模块包含创建和操纵轴对齐边框(AABB)的方法.


> 源码：[src/physics/matter-js/MatterPhysics.js#L315](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L315)  
引入版本：3.22.0


---

### collision {#collision}

#### collision: MatterJS.Collision {#collision-matterjscollision}


**说明:**

参考`Matter.Collision`模块.

`Matter.Collision`模块包含探测特定对天体碰撞的方法.

关于在尸体清单之间进行有效的检测,见`Matter.Detector`和`Matter.Query`。


> 源码：[src/physics/matter-js/MatterPhysics.js#L193](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L193)  
引入版本：3.60.0


---

### composite {#composite}

#### composite: MatterJS.CompositeFactory {#composite-matterjscompositefactory}


**说明:**

参考`Matter.Composite`模块.

电话 `Matter.Composite` 模块包含创建和操纵复合体的方法。 `Matter.Body`, `Matter.Constraint` 其他项目 `Matter.Composite`因此,复合材料构成树状结构。重要的是利用本模块中的函数来修改复合材料,而不是直接修改其属性。 `Matter.World` 对象也是类型 `Matter.Composite` 因此,所有综合方法也可在以下条件下运作: `Matter.World`.


> 源码：[src/physics/matter-js/MatterPhysics.js#L177](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L177)  
引入版本：3.22.0


---

### composites {#composites}

#### composites: MatterJS.CompositesFactory {#composites-matterjscompositesfactory}


**说明:**

参考`Matter.Composites`模块.

`Matter.Composites`模块包含厂家方法,用于创建具有常用配置(如堆栈和链)的复合体.


> 源码：[src/physics/matter-js/MatterPhysics.js#L290](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L290)  
引入版本：3.22.0


---

### config {#config}

#### config: [Phaser.Types.Physics.Matter.MatterWorldConfig](/api/typedef/types-physics-matter#matterworldconfig) {#config-phasertypesphysicsmattermatterworldconfig}


**说明:**

解析物质配置对象 。


> 源码：[src/physics/matter-js/MatterPhysics.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L119)  
引入版本：3.0.0


---

### constraint {#constraint}

#### constraint: MatterJS.ConstraintFactory {#constraint-matterjsconstraintfactory}


**说明:**

参考`Matter.Constraint`模块.

`Matter.Constraint`模块包含创建和操纵约束的方法,用于指定两个机构(或一个机构以及固定的世界空间位置)之间必须保持固定距离的限制,可以修改约束的硬度以创建弹簧或弹性.


> 源码：[src/physics/matter-js/MatterPhysics.js#L263](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L263)  
引入版本：3.22.0


---

### detector {#detector}

#### detector: MatterJS.DetectorFactory {#detector-matterjsdetectorfactory}


**说明:**

参考`Matter.Detector`模块.

`Matter.Detector`模块包含检测一组对子碰撞的方法.


> 源码：[src/physics/matter-js/MatterPhysics.js#L206](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L206)  
引入版本：3.22.0


---

### pair {#pair}

#### pair: MatterJS.PairFactory {#pair-matterjspairfactory}


**说明:**

参考`Matter.Pair`模块.

`Matter.Pair`模块包含生成和操纵碰撞对的方法.


> 源码：[src/physics/matter-js/MatterPhysics.js#L217](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L217)  
引入版本：3.22.0


---

### pairs {#pairs}

#### pairs: MatterJS.PairsFactory {#pairs-matterjspairsfactory}


**说明:**

参考`Matter.Pairs`模块.

`Matter.Pairs`模块包含创建和操纵碰撞对集的方法.


> 源码：[src/physics/matter-js/MatterPhysics.js#L228](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L228)  
引入版本：3.22.0


---

### query {#query}

#### query: MatterJS.QueryFactory {#query-matterjsqueryfactory}


**说明:**

参考`Matter.Query`模块.

`Matter.Query`模块包含进行碰撞查询的方法.


> 源码：[src/physics/matter-js/MatterPhysics.js#L239](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L239)  
引入版本：3.22.0


---

### resolver {#resolver}

#### resolver: MatterJS.ResolverFactory {#resolver-matterjsresolverfactory}


**说明:**

参考`Matter.Resolver`模块.

`Matter.Resolver`舱内包含解决碰撞对的方法.


> 源码：[src/physics/matter-js/MatterPhysics.js#L250](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L250)  
引入版本：3.22.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

拥有这个物质物理实例的 Phaser场景。


> 源码：[src/physics/matter-js/MatterPhysics.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L101)  
引入版本：3.0.0


---

### svg {#svg}

#### svg: MatterJS.SvgFactory {#svg-matterjssvgfactory}


**说明:**

参考`Matter.Svg`模块.

`Matter.Svg`模块包含将SVG图像转换成向量点阵列的方法.

要使用此模块, 您还需要 SVGPathSeg 的多填充: [https://github.com/progers/pathseg](https://github.com/progers/pathseg)


> 源码：[src/physics/matter-js/MatterPhysics.js#L326](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L326)  
引入版本：3.22.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

指属于拥有这个物质物理实例的场景系统.


> 源码：[src/physics/matter-js/MatterPhysics.js#L110](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L110)  
引入版本：3.0.0


---

### vector {#vector}

#### vector: MatterJS.VectorFactory {#vector-matterjsvectorfactory}


**说明:**

参考`Matter.Vector`模块.

`Matter.Vector`模块包含生成和操纵矢量的方法,矢量是引擎中所有几何相关操作的基础,一个`Matter.Vector`对象是`{ x: 0, y: 0 }`的形态.


> 源码：[src/physics/matter-js/MatterPhysics.js#L339](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L339)  
引入版本：3.22.0


---

### vertices {#vertices}

#### vertices: MatterJS.VerticesFactory {#vertices-matterjsverticesfactory}


**说明:**

参考`Matter.Vertices`模块.

`Matter.Vertices`模块包含创建和操纵顶点的组合方法. 一组顶点是`Matter.Vector`的一组,附加了`Vertices.create`插入的索引属性. A`Matter.Body`维护一组顶点,以表示物体的形状(它的凸轮船体).


> 源码：[src/physics/matter-js/MatterPhysics.js#L352](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L352)  
引入版本：3.22.0


---

### verts {#verts}

#### verts: MatterJS.VerticesFactory {#verts-matterjsverticesfactory}


**说明:**

参考 `Matter.Vertices` 模块。 这是 [Phaser.Physics.Matter.MatterPhysics#vertices](/api/class/physics-matter-matterphysics#vertices) 的别名 。

`Matter.Vertices`模块包含创建和操纵顶点的组合方法. 一组顶点是`Matter.Vector`的一组,附加了`Vertices.create`插入的索引属性. A`Matter.Body`维护一组顶点,以表示物体的形状(它的凸轮船体).


> 源码：[src/physics/matter-js/MatterPhysics.js#L365](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L365)  
引入版本：3.14.0


---

### world {#world}

#### world: [Phaser.Physics.Matter.World](/api/class/physics-matter-world) {#world-phaserphysicsmatterworld}


**说明:**

Matter World 类的一个实例。该类负责更新 Matter Physics 界,以及处理调试绘图功能。


> 源码：[src/physics/matter-js/MatterPhysics.js#L128](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L128)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### alignBody {#alignBody}

#### \<instance> alignBody(body, x, y, align) {#instance-alignbodybody-x-y-align}


**说明:**

将一个正文,或 Matter Game Object, 对齐给定的坐标 。

校对时使用体界,其中考虑到体积和旋转等因素.

虽然一个天体有`position`属性,但它是基于身体的质量中心,而不是基于维度的中心。这使得对齐天体变得困难,特别是如果它们旋转或缩放的话。这种方法将基于身体的界限及其质量抵消中心得出正确的位置,以便使身体与给定坐标一致。

例如,如果你想调整一个身体,所以它坐落在景点的下层中心,世界大小为800×600:

```javascript
this.matter.alignBody(body, 400, 600, Phaser.Display.Align.BOTTOM_CENTER);
```

你用400块来换x坐标 因为那是世界的中心, 而用600块来换y坐标, 因为那是世界的基础。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) | 否 | 身体要对齐。 |
| x | number | 否 | 横向位置使身体与. |
| y | number | 否 | 垂直位置使身体与它一致。 |
| align | number | 否 | 其中一个`Phaser.Display.Align`常数,例如`Phaser.Display.Align.TOP_LEFT`. |


**返回值:** [Phaser.Physics.Matter.MatterPhysics](/api/class/physics-matter-matterphysics) - 这个物质物理实例。


> 源码：[src/physics/matter-js/MatterPhysics.js#L1202](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L1202)  
引入版本：3.22.0


---

### applyForce {#applyForce}

#### \<instance> applyForce(bodies, force) {#instance-applyforcebodies-force}


**说明:**

将力量运用到身体,在身体目前的位置,包括由此产生的扭矩.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bodies | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) \| Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 否 | 要么是单一的身体,要么是一系列的身体来更新。如果弄虚作假,它就会使用世界上所有的身体。 |
| force | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 指定要施用的力量的矢量。 |


**返回值:** [Phaser.Physics.Matter.MatterPhysics](/api/class/physics-matter-matterphysics) - 这个物质物理实例。


> 源码：[src/physics/matter-js/MatterPhysics.js#L1067](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L1067)  
引入版本：3.22.0


---

### applyForceFromAngle {#applyForceFromAngle}

#### \<instance> applyForceFromAngle(bodies, speed, [angle]) {#instance-applyforcefromanglebodies-speed-angle}


**说明:**

将一个力应用到基于给定角度和速度的天体。如果没有给定角度,则使用当前天体角度。

视质量和要求的速度,使用极小的速度值,如0.1.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bodies | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) \| Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 否 | 要么是单一的身体,要么是一系列的身体来更新。如果弄虚作假,它就会使用世界上所有的身体。 |
| speed | number | 否 | 用于方向力的速度值 。 |
| angle | number | 是 | 角度,用弧度表示,以应用力。请不要定义,以使用当前身体角度。 |


**返回值:** [Phaser.Physics.Matter.MatterPhysics](/api/class/physics-matter-matterphysics) - 这个物质物理实例。


> 源码：[src/physics/matter-js/MatterPhysics.js#L1133](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L1133)  
引入版本：3.22.0


---

### applyForceFromPosition {#applyForceFromPosition}

#### \<instance> applyForceFromPosition(bodies, position, speed, [angle]) {#instance-applyforcefrompositionbodies-position-speed-angle}


**说明:**

将一个力应用到一个身体,从给定的世界位置,包括产生的扭矩。如果没有给出角度,则使用当前身体角度。

视质量和要求的速度,使用极小的速度值,如0.1.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bodies | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) \| Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 否 | 要么是单一的身体,要么是一系列的身体来更新。如果弄虚作假,它就会使用世界上所有的身体。 |
| position | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 指定世界空间位置的矢量,用于施加力。 |
| speed | number | 否 | 用于方向力的速度值 。 |
| angle | number | 是 | 角度,用弧度表示,以应用力。请不要定义,以使用当前身体角度。 |


**返回值:** [Phaser.Physics.Matter.MatterPhysics](/api/class/physics-matter-matterphysics) - 这个物质物理实例。


> 源码：[src/physics/matter-js/MatterPhysics.js#L1095](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L1095)  
引入版本：3.22.0


---

### containsPoint {#containsPoint}

#### \<instance> containsPoint(body, x, y) {#instance-containspointbody-x-y}


**说明:**

检查给定身体的顶点,或一系列的体,是否包含给定点。

您可以通过单个机构, 或者要检查的一系列机构。 如果阵列中的 _ 任何机构包含点, 此方法将会返回 `true` 。 如果您需要获取一个交叉机构列表, 请参见 `intersectPoint` 方法 。

点应该提前转换成 Matter World 坐标系统。 默认情况下, 输入指针会发生这种情况, 但是如果您想要使用来自另一个系统的点, 您可能需要在传递它们之前先进行转换 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) \| Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 否 | 身体,或一系列身体, 来检查点。 |
| x | number | 否 | 点的横向坐标. |
| y | number | 否 | 点的垂直坐标. |


**返回值:** boolean - 如果点在其中之一,则`true`, 否则则`false`。


> 源码：[src/physics/matter-js/MatterPhysics.js#L555](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L555)  
引入版本：3.22.0


---

### getConfig {#getConfig}

#### \<instance> getConfig() {#instance-getconfig}


**说明:**

此类开始检索最终 Matter World Config 时,这种内部方法被称为.


**返回值:** [Phaser.Types.Physics.Matter.MatterWorldConfig](/api/typedef/types-physics-matter#matterworldconfig) - 物质世界配置。


> 源码：[src/physics/matter-js/MatterPhysics.js#L439](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L439)  
引入版本：3.0.0


---

### getConstraintLength {#getConstraintLength}

#### \<instance> getConstraintLength(constraint) {#instance-getconstraintlengthconstraint}


**说明:**

返回给定约束的长度,即两点之间的距离。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| constraint | MatterJS.ConstraintType | 否 | 限制获得长度。 |


**返回值:** number - 约束的长度.


> 源码：[src/physics/matter-js/MatterPhysics.js#L1170](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L1170)  
引入版本：3.22.0


---

### getMatterBodies {#getMatterBodies}

#### \<instance> getMatterBodies([bodies]) {#instance-getmatterbodiesbodies}


**说明:**

取一个数组,然后返回从原始数组中找到的所有物质天体中制成的新数组。

例如,在 Matter Game Objects,比如一串 Matter Sprites 中传递到这种方法,将会返回一个包含所有其原生 Matter body 对象的阵列.

如果`bodies`的争论是虚假的,它会归还世界上所有的尸体.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bodies | array | 是 | 一系列物体来提取尸体。如果假象,它会归还世界上所有的尸体。 |


**返回值:** Array.\<MatterJS.BodyType> - 本地物质天体的数组。


> 源码：[src/physics/matter-js/MatterPhysics.js#L917](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L917)  
引入版本：3.22.0


---

### intersectBody {#intersectBody}

#### \<instance> intersectBody(body, [bodies]) {#instance-intersectbodybody-bodies}


**说明:**

检查给定的物质体,看看它是否与给定的任何天体相交.

如果没有人提供尸体,它将与物质世界的所有机构进行核对。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) | 否 | 目标身体。 |
| bodies | Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 是 | 一系列的人体来检查目标身体,如果不提供它,它将搜索世界上所有的身体。 |


**返回值:** Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> - 一系列的躯体,其顶点与目标体相交.


> 源码：[src/physics/matter-js/MatterPhysics.js#L706](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L706)  
引入版本：3.22.0


---

### intersectPoint {#intersectPoint}

#### \<instance> intersectPoint(x, y, [bodies]) {#instance-intersectpointx-y-bodies}


**说明:**

检查给定的坐标,看看给定的天体是否有顶点包含它。

如果没有提供尸体,它将搜寻物质世界的所有尸体,包括综合体内部的遗体。

坐标应提前转换成 Matter World 坐标系统。 默认情况下, 输入指针会发生这种情况, 但是如果您想要使用来自另一个系统的坐标, 您可能需要在通过它们之前进行转换 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 点的横向坐标. |
| y | number | 否 | 点的垂直坐标. |
| bodies | Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 是 | 一系列要检查的尸体。 如果不提供, 它将搜索世界上所有的尸体 。 |


**返回值:** Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> - 包含给定点的天体阵列 。


> 源码：[src/physics/matter-js/MatterPhysics.js#L586](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L586)  
引入版本：3.22.0


---

### intersectRay {#intersectRay}

#### \<instance> intersectRay(x1, y1, x2, y2, [rayWidth], [bodies]) {#instance-intersectrayx1-y1-x2-y2-raywidth-bodies}


**说明:**

检查给定的射线段,看看给定的天体是否有顶点与它相交.

如果没有尸体,它将搜索物质世界的所有尸体。

射线的宽度可以通过`rayWidth`参数指定.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x1 | number | 否 |  | 射线段起始的横向坐标. |
| y1 | number | 否 |  | 射线段起始的垂直坐标. |
| x2 | number | 否 |  | 射线段末端的横向坐标. |
| y2 | number | 否 |  | 射线段末端的垂直坐标. |
| rayWidth | number | 是 | 1 | 射线段的宽度 。 |
| bodies | Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 是 |  | 一系列要检查的尸体。 如果不提供, 它将搜索世界上所有的尸体 。 |


**返回值:** Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> - 一系列的体体,其顶点与射线段相交.


> 源码：[src/physics/matter-js/MatterPhysics.js#L670](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L670)  
引入版本：3.22.0


---

### intersectRect {#intersectRect}

#### \<instance> intersectRect(x, y, width, height, [outside], [bodies]) {#instance-intersectrectx-y-width-height-outside-bodies}


**说明:**

检查给定的矩形区域, 以查看给定天体是否有顶点与它相交。 或者, 如果 `outside` 参数设置为 `true`, 它检查哪些天体没有与之相交 。

如果没有提供尸体,它将搜寻物质世界的所有尸体,包括综合体内部的遗体。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 区域左上角的横向坐标. |
| y | number | 否 |  | 区域左上角的垂直坐标. |
| width | number | 否 |  | 面积宽度. |
| height | number | 否 |  | 地区高度. |
| outside | boolean | 是 | false | 如果`false`检查区内的顶点,如果`true`检查区内外的顶点. |
| bodies | Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 是 |  | 一系列要检查的尸体。 如果不提供, 它将搜索世界上所有的尸体 。 |


**返回值:** Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> - 与指定区域交汇的一组天体.


> 源码：[src/physics/matter-js/MatterPhysics.js#L625](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L625)  
引入版本：3.22.0


---

### overlap {#overlap}

#### \<instance> overlap(target, [bodies], [overlapCallback], [processCallback], [callbackContext]) {#instance-overlaptarget-bodies-overlapcallback-processcallback-callbackcontext}


**说明:**

检查是否与任何给定的天体交叉,以查看目标体,或一系列目标体.

如果发生交叉,此方法将返回`true`,如果提供,则引用回调。

如果没有提供第二个参数的躯体,目标将对照物质世界的所有躯体进行检查。

**Note that bodies can only overlap if they are in non-colliding collision groups or categories.**

如果您提供了 `processCallback`, 那么重叠的两具尸体将被发送到它。 此调回必须返回布尔, 并用于允许您在最后结果确定之前进行额外的处理测试。 如果返回 `true`, 那么如果设定的话, 尸体最终会传递到 `overlapCallback` 。

如果你提供`overlapCallback`,那么相匹配的对重叠的天体会被发送到它.

这两种回调都有以下的签名: `function (bodyA, bodyB, collisionInfo)`,其中`bodyA`总是目标体. `collisionInfo`对象包含额外数据,如渗透角和深度.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) \| Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 否 | 目标体,或一系列目标体,以检查. |
| bodies | Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 是 | 第二具尸体,或者说尸体的种类,来检查。如果伪造,它会检查世界上所有的尸体。 |
| overlapCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 如果机构重叠,则可以调用可选的回调函数。 |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 一个可选的回调函数,如果两个机构重叠,您可以对这两个机构进行额外检查。如果设置了此功能,则只有在返回 `true`时才会引用 `overlapCallback`。 |
| callbackContext | * | 是 | 运行回调的上下文,或范围. |


**返回值:** boolean - 如果目标体与给定的某具体相交,则`true`,否则则`false`.


> 源码：[src/physics/matter-js/MatterPhysics.js#L743](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L743)  
引入版本：3.22.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

暂停物质世界实例 将`enabled`设定为`false`.

一个被暂停的世界在被暂停的时间内不会运行任何模拟.


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 物质世界对象。


**Fires:** [Phaser.Physics.Matter.Events#event:PAUSE](/api/event/physics-matter-events#pause)


> 源码：[src/physics/matter-js/MatterPhysics.js#L460](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L460)  
引入版本：3.0.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

将这个世界实例从暂停状态中恢复, 并设置 `enabled` 到 `true` 。


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 物质世界对象。


> 源码：[src/physics/matter-js/MatterPhysics.js#L476](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L476)  
引入版本：3.0.0


---

### set30Hz {#set30Hz}

#### \<instance> set30Hz() {#instance-set30hz}


**说明:**

设置在 30Hz 的固定时间步运行的物质引擎并启用 `autoUpdate`。 如果您设置了自定义的 `getDelta` 函数, 这将覆盖它 。


**返回值:** [Phaser.Physics.Matter.MatterPhysics](/api/class/physics-matter-matterphysics) - 这个物质物理实例。


> 源码：[src/physics/matter-js/MatterPhysics.js#L506](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L506)  
引入版本：3.4.0


---

### set60Hz {#set60Hz}

#### \<instance> set60Hz() {#instance-set60hz}


**说明:**

设置在 60Hz 的固定时间步运行物质引擎, 并启用 `autoUpdate` 。 如果您设置了自定义的 `getDelta` 函数, 这将覆盖它 。


**返回值:** [Phaser.Physics.Matter.MatterPhysics](/api/class/physics-matter-matterphysics) - 这个物质物理实例。


> 源码：[src/physics/matter-js/MatterPhysics.js#L489](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L489)  
引入版本：3.4.0


---

### setAngularVelocity {#setAngularVelocity}

#### \<instance> setAngularVelocity(bodies, value) {#instance-setangularvelocitybodies-value}


**说明:**

立即设定天体的角速度。位置、角度、力等保持不变。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bodies | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) \| Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 否 | 要么是单一的身体,要么是一系列的身体来更新。如果弄虚作假,它就会使用世界上所有的身体。 |
| value | number | 否 | 角速法门. |


**返回值:** [Phaser.Physics.Matter.MatterPhysics](/api/class/physics-matter-matterphysics) - 这个物质物理实例。


> 源码：[src/physics/matter-js/MatterPhysics.js#L1043](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L1043)  
引入版本：3.22.0


---

### setCollidesWith {#setCollidesWith}

#### \<instance> setCollidesWith(bodies, categories) {#instance-setcollideswithbodies-categories}


**说明:**

将所有给定物质体的碰撞过滤罩设置到给定值。

两个不同碰撞组的物质体只有在基于位法和操作将其他类别纳入其面具时才会碰撞:`(categoryA & maskB) !== 0`和`(categoryB & maskA) !== 0`都是真实的。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bodies | Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 否 | 一系列要更新的天体。 如果假的, 它会使用世界上所有的身体 。 |
| categories | number \| Array.\<number> | 否 | 独有的类位场,或其中的数组. |


**返回值:** [Phaser.Physics.Matter.MatterPhysics](/api/class/physics-matter-matterphysics) - 这个物质物理实例。


> 源码：[src/physics/matter-js/MatterPhysics.js#L876](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L876)  
引入版本：3.22.0


---

### setCollisionCategory {#setCollisionCategory}

#### \<instance> setCollisionCategory(bodies, value) {#instance-setcollisioncategorybodies-value}


**说明:**

将所有给定物质体的碰撞过滤器类别设置为给定值。

此数必须是2^0(=1)至2^31之间的二位功率.

具有不同碰撞组的物体(见[#setCollisionGroup](#setCollisionGroup))只有在其碰撞口罩中包括碰撞类别时才会发生碰撞(见[#setCollidesWith](#setCollidesWith))。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bodies | Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 否 | 一系列要更新的天体。 如果假的, 它会使用世界上所有的身体 。 |
| value | number | 否 | 独特的类位元 。 |


**返回值:** [Phaser.Physics.Matter.MatterPhysics](/api/class/physics-matter-matterphysics) - 这个物质物理实例。


> 源码：[src/physics/matter-js/MatterPhysics.js#L819](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L819)  
引入版本：3.22.0


---

### setCollisionGroup {#setCollisionGroup}

#### \<instance> setCollisionGroup(bodies, value) {#instance-setcollisiongroupbodies-value}


**说明:**

将所有给定物质体的碰撞过滤组设置到给定值。

如果组值为零,或者如果两个物质体有不同的组值,它们会按照通常的碰撞滤波规则(见[#setCollisionCategory](#setCollisionCategory)和[#setCollidesWith](#setCollidesWith))碰撞.

如果两个物质体具有相同的正组值,它们总是碰撞;如果它们具有相同的负组值,它们永远不会碰撞.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bodies | Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 否 | 一系列要更新的天体。 如果假的, 它会使用世界上所有的身体 。 |
| value | number | 否 | 独具群指数. |


**返回值:** [Phaser.Physics.Matter.MatterPhysics](/api/class/physics-matter-matterphysics) - 这个物质物理实例。


> 源码：[src/physics/matter-js/MatterPhysics.js#L847](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L847)  
引入版本：3.22.0


---

### setVelocity {#setVelocity}

#### \<instance> setVelocity(bodies, x, y) {#instance-setvelocitybodies-x-y}


**说明:**

设置物理体的横向和纵向线性速度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bodies | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) \| Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 否 | 要么是单一的身体,要么是一系列的身体来更新。如果弄虚作假,它就会使用世界上所有的身体。 |
| x | number | 否 | 水平线性速度值。 |
| y | number | 否 | 垂直线性速度值 。 |


**返回值:** [Phaser.Physics.Matter.MatterPhysics](/api/class/physics-matter-matterphysics) - 这个物质物理实例。


> 源码：[src/physics/matter-js/MatterPhysics.js#L956](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L956)  
引入版本：3.22.0


---

### setVelocityX {#setVelocityX}

#### \<instance> setVelocityX(bodies, x) {#instance-setvelocityxbodies-x}


**说明:**

设定物理体的水平线性速度。 天体的垂直速度不变 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bodies | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) \| Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 否 | 要么是单一的身体,要么是一系列的身体来更新。如果弄虚作假,它就会使用世界上所有的身体。 |
| x | number | 否 | 水平线性速度值。 |


**返回值:** [Phaser.Physics.Matter.MatterPhysics](/api/class/physics-matter-matterphysics) - 这个物质物理实例。


> 源码：[src/physics/matter-js/MatterPhysics.js#L985](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L985)  
引入版本：3.22.0


---

### setVelocityY {#setVelocityY}

#### \<instance> setVelocityY(bodies, y) {#instance-setvelocityybodies-y}


**说明:**

设定物理体的垂直线性速度。 天体的横向速度不变 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bodies | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) \| Array.\<[Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody)> | 否 | 要么是单一的身体,要么是一系列的身体来更新。如果弄虚作假,它就会使用世界上所有的身体。 |
| y | number | 否 | 垂直线性速度值 。 |


**返回值:** [Phaser.Physics.Matter.MatterPhysics](/api/class/physics-matter-matterphysics) - 这个物质物理实例。


> 源码：[src/physics/matter-js/MatterPhysics.js#L1014](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L1014)  
引入版本：3.22.0


---

### step {#step}

#### \<instance> step([delta], [correction]) {#instance-stepdelta-correction}


**说明:**

手动推进物理模拟 一次迭代。

您可以在 Engine.update 使用的 `delta` 和 `correction` 值中可选择通过。 如果未定义, 它们使用 60Hz 的 Matter 默认值, 并且没有修正 。

直接拨打`step`绕过任何`enabled`或`autoUpdate`的检查.

也忽略了任何自定义的 `getDelta` 函数,因为您应该将三角洲值传递到这个调用中.

您可以调整 Engine.update 内部执行的迭代数。 使用 Scene Materical 配置对象设置以下属性:

positionIterations (违约6) velocityIterations (默认为4) constraintIterations (违约2)

调整这些值在某些情况下可以帮助性能,这取决于游戏的物理要求.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| delta | number | 是 | 16.666 | 三角洲的价值。 |
| correction | number | 是 | 1 | 可选三角洲校正值 。 |


> 源码：[src/physics/matter-js/MatterPhysics.js#L523](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterPhysics.js#L523)  
引入版本：3.4.0


---

---
