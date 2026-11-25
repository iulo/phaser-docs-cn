# World {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-matter-world)

物质世界级负责管理Phaser的单一物质物理世界实例。

透过场景内`this.matter.world`通过这个进入.

该课在即时演练期间与Mater JS引擎一起创建了Mater JS World Complex,同时还处理三角洲时间,界限,身体和约束的创建和调试绘图.

如果您希望直接访问 Matter JS World 对象, 请查看 `localWorld` 属性。 如果您希望直接访问 Matter 引擎, 请查看 `engine` 属性 。

校对:Soup

**构造函数**

`new World(scene, config)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 这个世界大事记的场景 |
| config | [Phaser.Types.Physics.Matter.MatterWorldConfig](/api/typedef/types-physics-matter#matterworldconfig) | 否 | 物质世界配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/physics/matter-js/World.js#L24](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L24)  
引入版本：3.0.0

## 公开成员 {#public-members}

### autoUpdate {#autoUpdate}

#### autoUpdate: boolean {#autoupdate-boolean}


**说明:**

每次游戏步骤自动调用 Engine.update。 如果您禁用此选项, 您负责直接从游戏中调用 `World.step`。 如果您调用 `set60Hz` 或 `set30Hz`, 那么 `autoUpdate` 将重置为 `true` 。


> 源码：[src/physics/matter-js/World.js#L165](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L165)  
引入版本：3.4.0


---

### debugConfig {#debugConfig}

#### debugConfig: [Phaser.Types.Physics.Matter.MatterDebugConfig](/api/typedef/types-physics-matter#matterdebugconfig) {#debugconfig-phasertypesphysicsmattermatterdebugconfig}


**说明:**

调试配置对象 。

此对象中存储的值来自 Matter World Config `debug` 属性 。

当一个新的body或约束被加到世界_时,它们会被赋予存储在这个对象中的值,除非它们有它们自己的`render`对象集,将覆盖它们.

注意, 您可以在运行时修改此对象的属性值, 但它不会改变任何已添加_ a 的天体。 它只会撞击新添加到世界的物体, 或者一个被移除, 并在稍后重新添加的物体 。


> 源码：[src/physics/matter-js/World.js#L198](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L198)  
引入版本：3.22.0


---

### debugGraphic {#debugGraphic}

#### debugGraphic: [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) {#debuggraphic-phasergameobjectsgraphics}


**说明:**

如果启用, 调试对象将被引向图形对象的示例 。


> 源码：[src/physics/matter-js/World.js#L189](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L189)  
引入版本：3.0.0


---

### drawDebug {#drawDebug}

#### drawDebug: boolean {#drawdebug-boolean}


**说明:**

用于控制调试图形是否被绘制到或不显示的旗帜 。


> 源码：[src/physics/matter-js/World.js#L179](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L179)  
引入版本：3.0.0


---

### enabled {#enabled}

#### enabled: boolean {#enabled-boolean}


**说明:**

旗子如果世界被启用或没有被启用的话,它会切换.


> 源码：[src/physics/matter-js/World.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L104)  
引入版本：3.0.0


---

### engine {#engine}

#### engine: MatterJS.Engine {#engine-matterjsengine}


**说明:**

物质JS引擎的一个例子。


> 源码：[src/physics/matter-js/World.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L66)  
引入版本：3.0.0


---

### getDelta {#getDelta}

#### getDelta: function {#getdelta-function}


**说明:**

此功能每次核心游戏循环步骤时都会被称作,除非另有修改,否则该循环步骤将约束在请求动画框架频率上.

该函数通过两个值:`time`和`delta`,两者都来自游戏的步数.

它必须返回一个数字。 这个数字被用作传送到 Matter. Engine.update 的三角形值 。

您可以用自己的功能来覆盖此功能, 以定义自己的时间步 。

如果您需要在单游戏步骤中多次更新引擎, 请按要求拨打 `World.update`。 每次呼叫都会触发 `getDelta` 函数。 如果您想要完全控制引擎更新时, 请查看属性 `autoUpdate` 。

您也可以调整 Engine.update 所执行的迭代数。使用 Scene Materys 配置对象设置以下属性:

positionIterations (违约6) velocityIterations (默认为4) constraintIterations (违约2)

调整这些值在某些情况下可以帮助性能,这取决于游戏的物理要求.


> 源码：[src/physics/matter-js/World.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L114)  
引入版本：3.4.0


---

### localWorld {#localWorld}

#### localWorld: MatterJS.World {#localworld-matterjsworld}


**说明:**

将包含所有模拟体和约束的`World`复合物.


> 源码：[src/physics/matter-js/World.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L75)  
引入版本：3.0.0


---

### runner {#runner}

#### runner: [Phaser.Types.Physics.Matter.MatterRunnerConfig](/api/typedef/types-physics-matter#matterrunnerconfig) {#runner-phasertypesphysicsmattermatterrunnerconfig}


**说明:**

Matter JS 运行器配置对象 。

此对象通过 Matter 配置对象的 `runner` 属性被覆盖,并在游戏步骤中不断更新.


> 源码：[src/physics/matter-js/World.js#L153](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L153)  
引入版本：3.22.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

这个世界大事记的场景


> 源码：[src/physics/matter-js/World.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L57)  
引入版本：3.0.0


---

### walls {#walls}

#### walls: [Phaser.Types.Physics.Matter.MatterWalls](/api/typedef/types-physics-matter#matterwalls) {#walls-phasertypesphysicsmattermatterwalls}


**说明:**

包含四个壁体的物体 将物理界捆绑在一起


> 源码：[src/physics/matter-js/World.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L95)  
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




---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(object) {#instance-addobject}


**说明:**

向世界添加物质 JS 对象, 或一系列对象 。

物体应当是有效的物质联合材料实体,如体、复合体或约束体。

触发`beforeAdd`和`afterAdd`事件.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object | object \| Array.\<object> | 否 | 可以是单物体,也可以是数组,也可以是体,复合体或约束体. |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 此物质世界对象 。


> 源码：[src/physics/matter-js/World.js#L953](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L953)  
引入版本：3.0.0


---

### convertTilemapLayer {#convertTilemapLayer}

#### \<instance> convertTilemapLayer(tilemapLayer, [options]) {#instance-converttilemaplayertilemaplayer-options}


**说明:**

添加给定的平面层内所有碰撞的瓦片的 `MatterTileBody` 实例 。

在调用此方法之前, 设定您的层中合适的瓦片以碰撞 !

如果您在调用此方法后修改了地图, 即通过像 `putTileAt` 这样的函数, 那么您应该直接调用 `Phaser.Physics.Matter.World.convertTiles` 函数, 将您添加到地图中的一阵牌递给它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tilemapLayer | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 否 | 包含要转换的瓷砖的 Tilemap 层 。 |
| options | object | 是 | 选项要传递给 MatterTileBody 构建器 。\\\ x见 Phaser.Physics.Matter.TileBody} |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 此物质世界对象 。


> 源码：[src/physics/matter-js/World.js#L1028](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1028)  
引入版本：3.0.0


---

### convertTiles {#convertTiles}

#### \<instance> convertTiles(tiles, [options]) {#instance-converttilestiles-options}


**说明:**

为所有给定的牌片创建 `MatterTileBody` 实例。这创建了机构,无论牌片是否被设定为碰撞,或者它们是否已经存在。

如果您想要通过可能已经存在天体的牌盘数组, 您应该先过滤该牌盘 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tiles | Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> | 否 | 一系列的瓷砖。 |
| options | object | 是 | 选项要传递给 MatterTileBody 构建器 。\\\ x见 Phaser.Physics.Matter.TileBody} |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 此物质世界对象 。


> 源码：[src/physics/matter-js/World.js#L1055](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1055)  
引入版本：3.0.0


---

### create {#create}

#### \<instance> create(x, y, width, height, options) {#instance-createx-y-width-height-options}


**说明:**

创建矩形物质体并添加到世界中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 身体在世界的横向位置. |
| y | number | 否 | 身体在世界的垂直位置. |
| width | number | 否 | 体之宽. |
| height | number | 否 | 身高之高处. |
| options | object | 否 | 可选物质配置对象 。 |


**返回值:** MatterJS.BodyType - 物质J的躯体是被创造出来的


> 源码：[src/physics/matter-js/World.js#L930](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L930)  
引入版本：3.0.0


---

### createDebugGraphic {#createDebugGraphic}

#### \<instance> createDebugGraphic() {#instance-createdebuggraphic}


**说明:**

创建一个 Phaser.GameObjects.Graphics 对象,用于将所有调试对象和关节都转换为 。

如果调试已被启用, 构造器会自动调用这种方法 。

所创建的图形对象在0x0时自动添加到Scene,并给定深度为`Number.MAX_VALUE`,因此它使在Scene中其他所有物体都处于首位.

图形对象被分配到此类的`debugGraphic`属性,`drawDebug`被启用.


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 新建的图形对象 。


> 源码：[src/physics/matter-js/World.js#L858](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L858)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

将删除所有物质物理事件听众,并清除物质物理世界,引擎和任何调试图形,如果有的话.

摧毁世界之后,它不能再被再次使用。


**Overrides:** Phaser.Events.EventEmitter#销毁


> 源码：[src/physics/matter-js/World.js#L2288](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L2288)  
引入版本：3.0.0


---

### disableGravity {#disableGravity}

#### \<instance> disableGravity() {#instance-disablegravity}


**说明:**

将世界重力和重力的比分设定为0.


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 此物质世界对象 。


> 源码：[src/physics/matter-js/World.js#L886](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L886)  
引入版本：3.0.0


---

### getAllBodies {#getAllBodies}

#### \<instance> getAllBodies() {#instance-getallbodies}


**说明:**

递归物质世界中所有的身体,包括所有儿童的身体。


**返回值:** Array.\<MatterJS.BodyType> - 世界上所有物质JS机构都存在


> 源码：[src/physics/matter-js/World.js#L1342](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1342)  
引入版本：3.22.0


---

### getAllComposites {#getAllComposites}

#### \<instance> getAllComposites() {#instance-getallcomposites}


**说明:**

递归物质世界中的所有复合材料,包括儿童中的所有复合材料。


**返回值:** Array.\<MatterJS.CompositeType> - 一系列的 物质JS 复合物 在这个世界上。


> 源码：[src/physics/matter-js/World.js#L1368](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1368)  
引入版本：3.22.0


---

### getAllConstraints {#getAllConstraints}

#### \<instance> getAllConstraints() {#instance-getallconstraints}


**说明:**

递归物质世界的所有限制,包括儿童的所有限制。


**返回值:** Array.\<MatterJS.ConstraintType> - 一系列的 物质JS 制约在这个世界上。


> 源码：[src/physics/matter-js/World.js#L1355](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1355)  
引入版本：3.22.0


---

### has {#has}

#### \<instance> has(body) {#instance-hasbody}


**说明:**

如果在世界范围内可以找到给定的天体,则返回 `true`。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | MatterJS.Body \| [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 物质体,或游戏对象, 寻找世界范围内。 |


**返回值:** boolean - 如果尸体在世界上被发现,则`true`,否则则`false`.


> 源码：[src/physics/matter-js/World.js#L1325](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1325)  
引入版本：3.22.0


---

### nextCategory {#nextCategory}

#### \<instance> nextCategory() {#instance-nextcategory}


**说明:**

返回下一个唯一类位元( 在初始默认类 0x0001 之后开始) 。 有32个可用 。


**返回值:** number - 唯一类位字


> 源码：[src/physics/matter-js/World.js#L1100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1100)  
引入版本：3.0.0


---

### nextGroup {#nextGroup}

#### \<instance> nextGroup([isNonColliding]) {#instance-nextgroupisnoncolliding}


**说明:**

返回下一个唯一组合索引, 天体将碰撞。 如果 `isNonColliding` 是 `true`, 则返回下一个唯一组合索引, 天体不会碰撞 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| isNonColliding | boolean | 是 | false | 如果 `true`,返回下一个唯一组索引,其中的天体将_ not_ 碰撞。 |


**返回值:** number - 唯一类位字


> 源码：[src/physics/matter-js/World.js#L1084](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1084)  
引入版本：3.0.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

暂停这个世界实例 将`enabled`设定为`false`。

一个被暂停的世界在被暂停的时间内不会运行任何模拟.


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 此物质世界对象 。


**Fires:** [Phaser.Physics.Matter.Events#event:PAUSE](/api/event/physics-matter-events#pause)


> 源码：[src/physics/matter-js/World.js#L1114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1114)  
引入版本：3.0.0


---

### remove {#remove}

#### \<instance> remove(object, [deep]) {#instance-removeobject-deep}


**说明:**

从世界上删除一个物质JS对象,或一系列对象。

物体应当是有效的物质联合材料实体,如体、复合体或约束体。

触发`beforeRemove`和`afterRemove`事件.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| object | object \| Array.\<object> | 否 |  | 可以是单物体,也可以是数组,也可以是体,复合体或约束体. |
| deep | boolean | 是 | false | 选择性地搜查儿童的物品,并递归地去除这些物品。 |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 此物质世界对象 。


> 源码：[src/physics/matter-js/World.js#L974](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L974)  
引入版本：3.0.0


---

### removeConstraint {#removeConstraint}

#### \<instance> removeConstraint(constraint, [deep]) {#instance-removeconstraintconstraint-deep}


**说明:**

消除世界范围内的JS物质制约或一系列制约。

触发`beforeRemove`和`afterRemove`事件.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| constraint | MatterJS.ConstraintType \| Array.\<MatterJS.ConstraintType> | 否 |  | 联合来文约束,或一系列限制,有待消除。 |
| deep | boolean | 是 | false | 选择性地搜查儿童的物品,并递归地去除这些物品。 |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 此物质世界对象 。


> 源码：[src/physics/matter-js/World.js#L1008](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1008)  
引入版本：3.0.0


---

### renderBody {#renderBody}

#### \<instance> renderBody(body, graphics, showInternalEdges, [lineColor], [lineOpacity], [lineThickness], [fillColor], [fillOpacity]) {#instance-renderbodybody-graphics-showinternaledges-linecolor-lineopacity-linethickness-fillcolor-fillopacity}


**说明:**

将一个物质体渲染到给定的 Phaser Graphics 游戏对象上.

这种方法被 Matter Rebug 渲染器内部使用, 但是如果您想要将一个天体变成自己的图形实例, 也会被公开曝光 。

如果你不想在身体周围画一条线,就设置 `lineColor` 参数改为 `null`同样,如果你不想填满,请设置 `fillColor` 参数改为 `null`.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | MatterJS.BodyType | 否 |  | 物质体要被改造出来 |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 |  | 图形对象要渲染到 。 |
| showInternalEdges | boolean | 否 |  | 多边形的内边缘? |
| lineColor | number | 是 |  | 线条色. |
| lineOpacity | number | 是 |  | 线条不透明,在0到1之间. |
| lineThickness | number | 是 | 1 | 线条厚度。 |
| fillColor | number | 是 |  | 补色. |
| fillOpacity | number | 是 |  | 填充不透明,在0到1之间. |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 这个世界的这个例子 方法链。


> 源码：[src/physics/matter-js/World.js#L1931](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1931)  
引入版本：3.22.0


---

### renderBodyAxes {#renderBodyAxes}

#### \<instance> renderBodyAxes(bodies, graphics, showAxes, lineColor, lineOpacity) {#instance-renderbodyaxesbodies-graphics-showaxes-linecolor-lineopacity}


**说明:**

将一系列天体的所有轴或单个轴指标都渲染到给定的图形实例。

如果设置了 `showAxes` 或 `showAngleIndicator` 配置值,调试渲染器会调用这种方法 。

这种方法被Mater Debug Renderer内部使用,但如果您想将身体轴转换成自己的图形实例,也会公开曝光.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bodies | array | 否 | 一群来自localWorld的尸体 |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 图形对象要渲染到 。 |
| showAxes | boolean | 否 | 如果 `true` 它会变成所有车轴 如果 `false` 它会变成一个单一的轴指示器 |
| lineColor | number | 否 | 线条色. |
| lineOpacity | number | 否 | 线条不透明,在0到1之间. |


> 源码：[src/physics/matter-js/World.js#L1722](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1722)  
引入版本：3.22.0


---

### renderBodyBounds {#renderBodyBounds}

#### \<instance> renderBodyBounds(bodies, graphics, lineColor, lineOpacity) {#instance-renderbodyboundsbodies-graphics-linecolor-lineopacity}


**说明:**

将一系列天体的界限显示为给定的图形实例。

如果尸体是复合体,它会为母体复合物制造界.

如果设置了 `showBounds` 配置值,调试渲染器会调用这种方法 。

这种方法被 Matter Rebug 渲染器内部使用, 但是如果您想要将界限转换到自己的图形实例, 也会被公开曝光 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bodies | array | 否 | 一群来自localWorld的尸体 |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 图形对象要渲染到 。 |
| lineColor | number | 否 | 线条色. |
| lineOpacity | number | 否 | 线条不透明,在0到1之间. |


> 源码：[src/physics/matter-js/World.js#L1658](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1658)  
引入版本：3.22.0


---

### renderBodyVelocity {#renderBodyVelocity}

#### \<instance> renderBodyVelocity(bodies, graphics, lineColor, lineOpacity, lineThickness) {#instance-renderbodyvelocitybodies-graphics-linecolor-lineopacity-linethickness}


**说明:**

将一系列天体的速度指标显示为给定的图形实例。

如果设置了 `showVelocity` 配置值,调试渲染器会调用这种方法 。

这种方法被 Matter Debug 渲染器内部使用, 但是如果您想要将速度指示器提供给自己的图形实例, 也会被公开曝光 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bodies | array | 否 | 一群来自localWorld的尸体 |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 图形对象要渲染到 。 |
| lineColor | number | 否 | 线条色. |
| lineOpacity | number | 否 | 线条不透明,在0到1之间. |
| lineThickness | number | 否 | 线条厚度。 |


> 源码：[src/physics/matter-js/World.js#L1799](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1799)  
引入版本：3.22.0


---

### renderCollisions {#renderCollisions}

#### \<instance> renderCollisions(pairs, graphics, lineColor) {#instance-rendercollisionspairs-graphics-linecolor}


**说明:**

将碰撞点和正常的列表提交给定图形实例。

如果设置了 `showCollisions` 配置值,调试渲染器会调用这种方法 。

这种方法被Mater Debug Render 内部使用,但如果您想将碰撞点和正常点变成自己的图形实例,也会被公开曝光.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pairs | Array.\<MatterJS.Pair> | 否 | 一系列要渲染的物质对等 。 |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 图形对象要渲染到 。 |
| lineColor | number | 否 | 线条色. |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 这个世界的这个例子 方法链。


> 源码：[src/physics/matter-js/World.js#L1561](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1561)  
引入版本：3.22.0


---

### renderConstraint {#renderConstraint}

#### \<instance> renderConstraint(constraint, graphics, lineColor, lineOpacity, lineThickness, pinSize, anchorColor, anchorSize) {#instance-renderconstraintconstraint-graphics-linecolor-lineopacity-linethickness-pinsize-anchorcolor-anchorsize}


**说明:**

将一个单一的 Matter 约束,例如一个 Pin 或一个 Spring, 给定的 Phaser 图形游戏对象 。

这种方法被 Matter Debug 渲染器内部使用, 但是如果您想要将约束器切换到自己的图形实例, 也会被公开曝光 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| constraint | MatterJS.ConstraintType | 否 | 物质约束 制造。 |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 图形对象要渲染到 。 |
| lineColor | number | 否 | 线条色. |
| lineOpacity | number | 否 | 线条不透明,在0到1之间. |
| lineThickness | number | 否 | 线条厚度。 |
| pinSize | number | 否 | 如果这个约束是针形,则设定针形圆的大小. |
| anchorColor | number | 否 | 渲染此约束锚时所用的颜色 。 设定为 `null` 以不渲染锚 。 |
| anchorSize | number | 否 | 如果这种约束有锚,并正在使其产生锚,那么锚圈的大小。 |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 这个世界的这个例子 方法链。


> 源码：[src/physics/matter-js/World.js#L2149](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L2149)  
引入版本：3.22.0


---

### renderConvexHull {#renderConvexHull}

#### \<instance> renderConvexHull(body, graphics, hullColor, [lineThickness]) {#instance-renderconvexhullbody-graphics-hullcolor-linethickness}


**说明:**

将 Convex 游戏标本为单个物质体, 以给定的 Phaser 图形游戏对象 。

这种方法被Mater Rebug Render 内部使用,但是如果您想让身体壳切换到自己的图形实例,也会被公开曝光.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | MatterJS.BodyType | 否 |  | 物质体要被改造出来 |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 |  | 图形对象要渲染到 。 |
| hullColor | number | 否 |  | 用来制造船体的颜色。 |
| lineThickness | number | 是 | 1 | 船体线厚度。 |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 这个世界的这个例子 方法链。


> 源码：[src/physics/matter-js/World.js#L2071](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L2071)  
引入版本：3.22.0


---

### renderGrid {#renderGrid}

#### \<instance> renderGrid(grid, graphics, lineColor, lineOpacity) {#instance-rendergridgrid-graphics-linecolor-lineopacity}


**说明:**

将引擎宽相控器网格渲染到给定的图形实例 。

如果设置了 `showBroadphase` 配置值,调试渲染器会调用这种方法 。

这种方法被 Matter Rebug 渲染器内部使用, 但是如果您想要将 Grid 渲染到您自己的图形实例中, 也会被公开曝光 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| grid | MatterJS.Grid | 否 | 物质网格要被打开 |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 图形对象要渲染到 。 |
| lineColor | number | 否 | 线条色. |
| lineOpacity | number | 否 | 线条不透明,在0到1之间. |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 这个世界的这个例子 方法链。


> 源码：[src/physics/matter-js/World.js#L1446](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1446)  
引入版本：3.22.0


---

### renderSeparations {#renderSeparations}

#### \<instance> renderSeparations(pairs, graphics, lineColor) {#instance-renderseparationspairs-graphics-linecolor}


**说明:**

将对等分离列表提交给定的图形实例。

如果设置了 `showSeparations` 配置值,调试渲染器会调用这种方法 。

这种方法被 Matter 调试器内部使用, 但是如果您想要将对子分离转换成自己的图形实例, 也会被公开曝光 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pairs | Array.\<MatterJS.Pair> | 否 | 一系列要渲染的物质对等 。 |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 图形对象要渲染到 。 |
| lineColor | number | 否 | 线条色. |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 这个世界的这个例子 方法链。


> 源码：[src/physics/matter-js/World.js#L1492](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1492)  
引入版本：3.22.0


---

### resetCollisionIDs {#resetCollisionIDs}

#### \<instance> resetCollisionIDs() {#instance-resetcollisionids}


**说明:**

重置内碰撞ID, 用于身体碰撞组。

如果您需要在同一页上再次重启游戏, 无需重新装入页面, 请在销毁游戏前先拨打此选项。 或者, 如果您想要一致销毁包含 Matter.js 的场景, 然后在同一游戏中再次运行它 。


> 源码：[src/physics/matter-js/World.js#L2245](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L2245)  
引入版本：3.17.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

将这个世界实例从暂停状态中恢复, 并设置 `enabled` 到 `true` 。


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 此物质世界对象 。


**Fires:** [Phaser.Physics.Matter.Events#event:RESUME](/api/event/physics-matter-events#resume)


> 源码：[src/physics/matter-js/World.js#L1134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1134)  
引入版本：3.0.0


---

### setBodyRenderStyle {#setBodyRenderStyle}

#### \<instance> setBodyRenderStyle(body, [lineColor], [lineOpacity], [lineThickness], [fillColor], [fillOpacity]) {#instance-setbodyrenderstylebody-linecolor-lineopacity-linethickness-fillcolor-fillopacity}


**说明:**

设置给定物质体的调试渲染样式。

如果您正在使用此功能在 Phaser 游戏对象上, 如 Matter Sprite , 那么在实体属性中传递到此方法, 而不是游戏对象本身 。

如果您想要跳过一个参数, 因此它保留其当前值, 请通过 `false` 。

如果您想要重置天体使颜色符合世界调试配置中发现的默认值, 那么使用仅提供的 `body` 参数调用此方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | MatterJS.BodyType | 否 | 设置渲染样式的主体 |
| lineColor | number | 是 | 线条颜色。 如果 `null` , 它会使用世界调试配置值 。 |
| lineOpacity | number | 是 | 线条不透明,在0到1之间,如果`null`,它会使用世界调试配置值. |
| lineThickness | number | 是 | 线厚度。 如果 `null` , 它将使用世界调试配置值 。 |
| fillColor | number | 是 | 填充颜色。 如果 `null` 会使用世界调试配置值 。 |
| fillOpacity | number | 是 | 填充不透明, 0 到 1 之间, 如果 `null` , 它会使用 World Debug 配置值 。 |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 这个世界的这个例子 方法链。


> 源码：[src/physics/matter-js/World.js#L364](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L364)  
引入版本：3.22.0


---

### setBounds {#setBounds}

#### \<instance> setBounds([x], [y], [width], [height], [thickness], [left], [right], [top], [bottom]) {#instance-setboundsx-y-width-height-thickness-left-right-top-bottom}


**说明:**

设置物理世界的界限,以匹配给定的世界像素尺寸。

您可以选择设置要创建的“ 墙” : 左、 右、 上或下。 如果没有墙壁被赋予, 将默认使用它以前设置的墙壁。 I. , 如果你以前告诉它没有左右墙壁, 然后调整世界大小, 新建的界限也不会有左右墙壁。 明确在参数中声明它们以覆盖此设置 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 界左上角的x坐标. |
| y | number | 是 | 0 | 界上左上角的y坐标. |
| width | number | 是 |  | 界之宽. |
| height | number | 是 |  | 界之高处. |
| thickness | number | 是 | 64 | 每面壁的厚度,以像素为单位. |
| left | boolean | 是 | true | 如果真能创建左边的边墙 。 |
| right | boolean | 是 | true | 如果真能创建正确的界限墙 。 |
| top | boolean | 是 | true | 如果真能创建顶部的边框壁 。 |
| bottom | boolean | 是 | true | 如果真能创建下方的边框壁 。 |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 此物质世界对象 。


> 源码：[src/physics/matter-js/World.js#L772](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L772)  
引入版本：3.0.0


---

### setCompositeRenderStyle {#setCompositeRenderStyle}

#### \<instance> setCompositeRenderStyle(composite) {#instance-setcompositerenderstylecomposite}


**说明:**

设置给定物质复合的子程序的调试渲染样式。

复合物本身并不产生,但可以包含身体、约束和其他可能产生的复合物。因此,这种复合物的子孙被传给了人类。 `setBodyRenderStyle`, `setCompositeRenderStyle` 财务报告和已审计财务报表 `setConstraintRenderStyle` 相应方法。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| composite | MatterJS.CompositeType | 否 | 设置渲染样式的元素复合 。 |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 这个世界的这个例子 方法链。


> 源码：[src/physics/matter-js/World.js#L314](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L314)  
引入版本：3.22.0


---

### setConstraintRenderStyle {#setConstraintRenderStyle}

#### \<instance> setConstraintRenderStyle(constraint, [lineColor], [lineOpacity], [lineThickness], [pinSize], [anchorColor], [anchorSize]) {#instance-setconstraintrenderstyleconstraint-linecolor-lineopacity-linethickness-pinsize-anchorcolor-anchorsize}


**说明:**

设置给定物质约束的调试渲染样式。

如果您正在使用此功能在一个 Phaser 游戏对象上, 那么在约束属性中传递到此方法, 而不是游戏对象本身 。

如果您想要跳过一个参数, 因此它保留其当前值, 请通过 `false` 。

如果您想要重置 Construct 将颜色转换为默认值, 则使用仅提供的 `constraint` 参数调用此方法, 而不是其它参数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| constraint | MatterJS.ConstraintType | 否 | 物质约束来设置渲染样式 。 |
| lineColor | number | 是 | 线条颜色。 如果 `null` , 它会使用世界调试配置值 。 |
| lineOpacity | number | 是 | 线条不透明,在0到1之间,如果`null`,它会使用世界调试配置值. |
| lineThickness | number | 是 | 线厚度。 如果 `null` , 它将使用世界调试配置值 。 |
| pinSize | number | 是 | 如果此约束是针形, 则设置针形圆的大小。 如果 `null` 将使用 World Debug 配置值 。 |
| anchorColor | number | 是 | 渲染此约束锚时所用的颜色。 如果 `null` , 它会使用 World Debug 配置值 。 |
| anchorSize | number | 是 | 锚圈大小, 如果此约束有锚。 如果 `null` , 它会使用世界调试配置值 。 |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 这个世界的这个例子 方法链。


> 源码：[src/physics/matter-js/World.js#L450](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L450)  
引入版本：3.22.0


---

### setEventsProxy {#setEventsProxy}

#### \<instance> setEventsProxy() {#instance-seteventsproxy}


**说明:**

这种内部方法在所有物质JS事件之间起到代名词作用,然后通过这一类重新提出。


> 源码：[src/physics/matter-js/World.js#L561](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L561)  
引入版本：3.0.0


---

### setGravity {#setGravity}

#### \<instance> setGravity([x], [y], [scale]) {#instance-setgravityx-y-scale}


**说明:**

设定世界对给出的值的重力。

重力效应了世界上所有的身体,除非它们有`ignoreGravity`旗设定.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 世界重力X组件. |
| y | number | 是 | 1 | 世界引力Y组件. |
| scale | number | 是 | 0.001 | 重力尺度因子. |


**返回值:** [Phaser.Physics.Matter.World](/api/class/physics-matter-world) - 此物质世界对象 。


> 源码：[src/physics/matter-js/World.js#L903](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L903)  
引入版本：3.0.0


---

### shutdown {#shutdown}

#### \<instance> shutdown() {#instance-shutdown}


**说明:**

将删除所有物质物理事件听众,并清除物质物理世界,引擎和任何调试图形,如果有的话.


**Overrides:** Phaser.Events.EventEmitter# 低调的


> 源码：[src/physics/matter-js/World.js#L2265](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L2265)  
引入版本：3.0.0


---

### step {#step}

#### \<instance> step([delta]) {#instance-stepdelta}


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


> 源码：[src/physics/matter-js/World.js#L1268](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1268)  
引入版本：3.4.0


---

### update {#update}

#### \<instance> update(time, delta) {#instance-updatetime-delta}


**说明:**

内部更新方法。 由父 Scene 自动调用 。

将模拟按 delta ms 移动到时间。 使用 `World.correction` 值作为可选的数字, 指定用于更新的时间校正因数。 这有助于在 delta 值在更新之间发生变化的情况下提高模拟的准确性。 校正值被定义为 `delta / lastDelta`, 即三角洲相对于最后一步的百分比变化。 因此, 当三角洲是恒定的( 或者没有要求更正, 默认的) 时, 数值总是 1 ( 不校正) 。 请参看关于时间校正的 Verlet 的文件 。

触发 `beforeUpdate` 财务报告和已审计财务报表 `afterUpdate` 触发器 `collisionStart`, `collisionActive` 财务报告和已审计财务报表 `collisionEnd` 事件。

如果世界暂停,`update`仍然运行,但提前退出,不更新物质引擎.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/physics/matter-js/World.js#L1154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1154)  
引入版本：3.0.0


---

### update30Hz {#update30Hz}

#### \<instance> update30Hz() {#instance-update30hz}


**说明:**

运行物质引擎. update 在一个30Hz的固定时间步.


**返回值:** number - 三角洲值将传递到 Engine.update 。


> 源码：[src/physics/matter-js/World.js#L1312](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1312)  
引入版本：3.4.0


---

### update60Hz {#update60Hz}

#### \<instance> update60Hz() {#instance-update60hz}


**说明:**

运行 Matter 引擎. update 在一个固定的60Hz时间步.


**返回值:** number - 三角洲值将传递到 Engine.update 。


> 源码：[src/physics/matter-js/World.js#L1299](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L1299)  
引入版本：3.4.0


---

### updateWall {#updateWall}

#### \<instance> updateWall(add, [position], [x], [y], [width], [height]) {#instance-updatewalladd-position-x-y-width-height}


**说明:**

更新创建的 4 个矩形机构, 如果在 Materal 配置中设置了 `setBounds` , 则使用新的位置和大小。 这种方法通常只能通过 `setBounds` 方法在内部调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| add | boolean | 否 | 如果墙壁被加加或更新,则`true`,`false`将其从世界中移除. |
| position | string | 是 | 或`left`,`right`,`top`或`bottom`,只有`add`是`false`时,才有可选性. |
| x | number | 是 | 水平位置放置墙壁。 只有 `add` 时, 才有 `false` 选项 。 |
| y | number | 是 | 垂直位置放置墙壁。 只有 `add` 时, 才有 `false` 选项 。 |
| width | number | 是 | 墙的宽度, 以像素表示。 只有 `add` 才有 `false` 的可选性 。 |
| height | number | 是 | 墙的高度,以像素表示。只有`add`是`false`时,才能选择。 |


> 源码：[src/physics/matter-js/World.js#L816](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/World.js#L816)  
引入版本：3.0.0


---

---
