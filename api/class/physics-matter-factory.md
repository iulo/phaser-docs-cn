# Factory {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-matter-factory)

物质工厂负责迅速创造各种不同类型的体,约束和游戏对象,并把它们加入物理学界.

你从场内进入工厂 用`add`:

```javascript
this.matter.add.rectangle(x, y, width, height);
```

使用工厂是可选的。 它创建的所有对象也可以直接通过您的代码或构造器创建。 它被提供作为保持代码简洁性的手段 。

**构造函数**

`new Factory(world)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| world | [Phaser.Physics.Matter.World](/api/class/physics-matter-world) | 否 | 工厂所增加的物质世界。 |

---


**作用域**: static

> 源码：[src/physics/matter-js/Factory.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L21)  
引入版本：3.0.0

## 公开成员 {#public-members}

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

工厂物质世界的场景


> 源码：[src/physics/matter-js/Factory.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L58)  
引入版本：3.0.0


---

### sys {#sys}

#### sys: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#sys-phaserscenessystems}


**说明:**

引用 Scene.Systems 这个物质物理实例属于。


> 源码：[src/physics/matter-js/Factory.js#L67](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L67)  
引入版本：3.0.0


---

### world {#world}

#### world: [Phaser.Physics.Matter.World](/api/class/physics-matter-world) {#world-phaserphysicsmatterworld}


**说明:**

工厂所增加的物质世界。


> 源码：[src/physics/matter-js/Factory.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L49)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### car {#car}

#### \<instance> car(x, y, width, height, wheelSize) {#instance-carx-y-width-height-wheelsize}


**说明:**

创建一个包含简单车身设置和约束的复合体.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 汽车在世界水平位置. |
| y | number | 否 | 车在世界的垂直位置. |
| width | number | 否 | 车底盘的宽度. |
| height | number | 否 | 车底盘的高度. |
| wheelSize | number | 否 | 车轮的半径. |


**返回值:** MatterJS.CompositeType - 新的复合车体.


> 源码：[src/physics/matter-js/Factory.js#L534](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L534)  
引入版本：3.0.0


---

### chain {#chain}

#### \<instance> chain(composite, xOffsetA, yOffsetA, xOffsetB, yOffsetB, [options]) {#instance-chaincomposite-xoffseta-yoffseta-xoffsetb-yoffsetb-options}


**说明:**

利用各种限制将特定复合体中的所有体连在一起。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| composite | MatterJS.CompositeType | 否 | 将所有机构依次连在一起的复合体。 |
| xOffsetA | number | 否 | 身体A限制的横向抵消,这是根据体积而不是世界位置得出的百分比。 |
| yOffsetA | number | 否 | 身体A限制的垂直抵消。这是根据体积而不是世界位置计算的百分比。 |
| xOffsetB | number | 否 | 身体B限制的横向抵消。这是根据体积而不是世界位置计算的百分比。 |
| yOffsetB | number | 否 | 身体B限制的垂直抵消。这是根据体积而不是世界位置计算的百分比。 |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](/api/typedef/types-physics-matter#matterconstraintconfig) | 是 | 用于设定创建时初始约束属性的可选约束配置对象。 |


**返回值:** MatterJS.CompositeType - 最初的复合物被传递到这种方法中.


> 源码：[src/physics/matter-js/Factory.js#L472](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L472)  
引入版本：3.0.0


---

### circle {#circle}

#### \<instance> circle(x, y, radius, [options], [maxSides]) {#instance-circlex-y-radius-options-maxsides}


**说明:**

创建新的硬圆形体,并加入到世界中.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 身体中心X坐标. |
| y | number | 否 | 身体中心Y坐标. |
| radius | number | 否 | 圆之半径. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |
| maxSides | number | 是 | 用于多边形的最大边数, 以接近此圆 。 |


**返回值:** MatterJS.BodyType - 联合来文机构。


> 源码：[src/physics/matter-js/Factory.js#L124](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L124)  
引入版本：3.0.0


---

### constraint {#constraint}

#### \<instance> constraint(bodyA, bodyB, [length], [stiffness], [options]) {#instance-constraintbodya-bodyb-length-stiffness-options}


**说明:**

限制(或关节)用于规定两个机构之间必须保持固定距离,或一个机构和固定的世界空间位置。

约束的僵硬性可以被修改以产生弹簧或弹性.

模拟回旋约束(或称针联)设置`length: 0`和高值的`stiffness`(如`0.7`或以上).

如果约束不稳定, 请尝试在 Materal Config 中降低 `stiffness` 值和 / 或增加 `constraintIterations` 。

对于复合体,必须限制母体而不是其一部分。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| bodyA | MatterJS.BodyType | 否 |  | 首个可能附加这种限制的`Body`. |
| bodyB | MatterJS.BodyType | 否 |  | 附加这一限制的第二个可能的`Body`. |
| length | number | 是 |  | 一个指定约束的休息时间目标长度的号码。如果未给出,则从`constraint.bodyA`和`constraint.bodyB`的初始位置自动计算为`Constraint.create`。 |
| stiffness | number | 是 | 1 | 一个数字,它指定了约束的硬度,即它返回休息的`constraint.length`的速度。一个值的`1`表示约束应该非常坚硬。一个值的`0.2`表示约束作为软弹簧。 |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](/api/typedef/types-physics-matter#matterconstraintconfig) | 是 |  | 用于设定创建时初始约束属性的可选约束配置对象。 |


**返回值:** MatterJS.ConstraintType - 联合来文约束。


> 源码：[src/physics/matter-js/Factory.js#L649](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L649)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这工厂


> 源码：[src/physics/matter-js/Factory.js#L909](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L909)  
引入版本：3.5.0


---

### fromJSON {#fromJSON}

#### \<instance> fromJSON(x, y, config, [options], [addToWorld]) {#instance-fromjsonx-y-config-options-addtoworld}


**说明:**

使用 JSON 文件提供的物理数据创建一个天体。

数据文件应该装入为 JSON :

```javascript
preload ()
{
  this.load.json('ninjas', 'assets/ninjas.json);
}

create ()
{
  const ninjaShapes = this.cache.json.get('ninjas');

  this.matter.add.fromJSON(400, 300, ninjaShapes.shinobi);
}
```

不要将整个JSON文件传递到这种方法,而是通过其中包含的一个形状.

如果您在 `options` 对象中通过, 任何设置都会覆盖配置对象中的那些设置 。

JSON文件的结构如下:

```text
{
  'generator_info': // The name of the application that created the JSON data
  'shapeName': {
    'type': // The type of body
    'label': // Optional body label
    'vertices': // An array, or an array of arrays, containing the vertex data in x/y object pairs
  }
}
```

在撰写本报告时,只有Phaser物理追踪器App以这种格式输出。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 身体的X坐标. |
| y | number | 否 |  | 身体的Y坐标. |
| config | any | 否 |  | JSON物理数据. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 |  | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |
| addToWorld | boolean | 是 | true | 刚刚创建的机构应该立即加入世界吗? |


**返回值:** MatterJS.BodyType - 联合来文机构。


> 源码：[src/physics/matter-js/Factory.js#L311](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L311)  
引入版本：3.22.0


---

### fromPhysicsEditor {#fromPhysicsEditor}

#### \<instance> fromPhysicsEditor(x, y, config, [options], [addToWorld]) {#instance-fromphysicseditorx-y-config-options-addtoworld}


**说明:**

使用应用程序物理编辑器( https://www.codeandweb.com/physicseditor)) 输出的数据创建正文

物理编辑器文件应该装入为 JSON :

```javascript
preload ()
{
  this.load.json('vehicles', 'assets/vehicles.json);
}

create ()
{
  const vehicleShapes = this.cache.json.get('vehicles');
  this.matter.add.fromPhysicsEditor(400, 300, vehicleShapes.truck);
}
```

不要将整个JSON文件传递到这种方法,而是通过其中包含的一个形状.

如果您在 `options` 对象中通过, 里面的任何设置都会覆盖物理编辑器配置对象中的设置 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 身体的横向世界位置. |
| y | number | 否 |  | 身体的垂直世界位置. |
| config | any | 否 |  | JSON数据从物理编辑器导出. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 |  | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |
| addToWorld | boolean | 是 | true | 刚刚创建的机构应该立即加入世界吗? |


**返回值:** MatterJS.BodyType - 联合来文机构。


> 源码：[src/physics/matter-js/Factory.js#L201](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L201)  
引入版本：3.22.0


---

### fromSVG {#fromSVG}

#### \<instance> fromSVG(x, y, xml, [scale], [options], [addToWorld]) {#instance-fromsvgx-y-xml-scale-options-addtoworld}


**说明:**

使用 SVG 文件的路径数据创建正文。

SVG 解析需要从 [https://github.com/progers/pathseg](https://github.com/progers/pathseg) 中选择路径加多填充

SVG文件应该装入为XML,因为这种方法需要能够从中提取路径数据. I. e.

```javascript
preload ()
{
  this.load.xml('face', 'assets/face.svg);
}

create ()
{
  this.matter.add.fromSVG(400, 300, this.cache.xml.get('face'));
}
```

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 身体的X坐标. |
| y | number | 否 |  | 身体的Y坐标. |
| xml | object | 否 |  | SVG路径数据. |
| scale | number | 是 | 1 | 创建后, 顶点按此量缩放 。 |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 |  | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |
| addToWorld | boolean | 是 | true | 刚刚创建的机构应该立即加入世界吗? |


**返回值:** MatterJS.BodyType - 联合来文机构。


> 源码：[src/physics/matter-js/Factory.js#L248](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L248)  
引入版本：3.22.0


---

### fromVertices {#fromVertices}

#### \<instance> fromVertices(x, y, vertexSets, [options], [flagInternal], [removeCollinear], [minimumArea]) {#instance-fromverticesx-y-vertexsets-options-flaginternal-removecollinear-minimumarea}


**说明:**

使用所提供的顶点(或包含多个顶点的阵列)创建一个身体,并添加到世界中。如果顶点是凸起的,它们会按所提供的情况通过。否则,如果顶点是凸出,它们会分解。请注意,这个过程不能保证支持复杂的顶点,例如有孔的顶点。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 身体中心X坐标. |
| y | number | 否 |  | 身体中心Y坐标. |
| vertexSets | string \| array | 否 |  | 顶点数据。 要么是路径字符串, 要么是一系列顶点。 |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 |  | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |
| flagInternal | boolean | 是 | false | 旗内边缘( 事故部分边缘) |
| removeCollinear | number | 是 | 0.01 | Matter.js是否丢弃串联边缘( 以提高性能) 。 |
| minimumArea | number | 是 | 10 | 在分解过程中,弃置部分的面积低于此. |


**返回值:** MatterJS.BodyType - 联合来文机构。


> 源码：[src/physics/matter-js/Factory.js#L170](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L170)  
引入版本：3.0.0


---

### gameObject {#gameObject}

#### \<instance> gameObject(gameObject, [options], [addToWorld]) {#instance-gameobjectgameobject-options-addtoworld}


**说明:**

将一个已有的游戏对象注入其中。

这使得您能够直接从此游戏对象使用`setVelocity`或`isSensor`等组件方法.

您也可以通过 Matter Body 配置对象, 或者 Matter Body 实例来链接到此游戏对象 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将物质组件注入到的游戏对象 。 |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) \| MatterJS.Body | 是 |  | 物质体的配置对象, 或物质体的示例 。 |
| addToWorld | boolean | 是 | true | 将此物质体添加到世界中吗 ? |


**返回值:** [Phaser.Physics.Matter.Image](/api/class/physics-matter-image), [Phaser.Physics.Matter.Sprite](/api/class/physics-matter-sprite), [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 游戏对象, 里面注入了物质组件 。


> 源码：[src/physics/matter-js/Factory.js#L886](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L886)  
引入版本：3.3.0


---

### image {#image}

#### \<instance> image(x, y, key, [frame], [options]) {#instance-imagex-y-key-frame-options}


**说明:**

创建物质物理图像游戏对象。

图像是用于在游戏中显示静态图像的轻量级游戏对象,例如标识,背景,景色或其他非动画元素. 图像可以有输入事件和物理体,或者被调色,有色或滚动. 图像和Sprite的主要区别在于,由于没有动画组件,无法给图像动画.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| key | string | 否 | 此游戏对象将使用的质地密钥用于渲染, 如保存在质地管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在渲染的纹理可选框架。 设定为 `null` 以跳过此值 。 |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** [Phaser.Physics.Matter.Image](/api/class/physics-matter-image) - 物质图像游戏对象 。


> 源码：[src/physics/matter-js/Factory.js#L801](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L801)  
引入版本：3.0.0


---

### imageStack {#imageStack}

#### \<instance> imageStack(key, frame, x, y, columns, rows, [columnGap], [rowGap], [options]) {#instance-imagestackkey-frame-x-y-columns-rows-columngap-rowgap-options}


**说明:**

创建包含在网格安排中创建的 Matter Image 对象的新复合材料。此函数使用机构界限来防止重叠。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 此游戏对象将使用的质地密钥用于渲染, 如保存在质地管理器中 。 |
| frame | string \| number | 否 |  | 游戏对象正在渲染的纹理可选框架。 设定为 `null` 以跳过此值 。 |
| x | number | 否 |  | 这种复合材料在世界的横向位置. |
| y | number | 否 |  | 这种复合材料在世界的垂直位置. |
| columns | number | 否 |  | 网格中的列数. |
| rows | number | 否 |  | 网格中的行数. |
| columnGap | number | 是 | 0 | 每列之间的距离. |
| rowGap | number | 是 | 0 | 每行之间的距离. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 |  | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** MatterJS.CompositeType - 堆积物


> 源码：[src/physics/matter-js/Factory.js#L375](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L375)  
引入版本：3.0.0


---

### joint {#joint}

#### \<instance> joint(bodyA, bodyB, [length], [stiffness], [options]) {#instance-jointbodya-bodyb-length-stiffness-options}


**说明:**

此方法为`Factory.constraint`的别名.

限制(或关节)用于规定两个机构之间必须保持固定距离,或一个机构和固定的世界空间位置。

约束的僵硬性可以被修改以产生弹簧或弹性.

模拟回旋约束(或称针联)设置`length: 0`和高值的`stiffness`(如`0.7`或以上).

如果约束不稳定, 请尝试在 Materal Config 中降低 `stiffness` 值和 / 或增加 `constraintIterations` 。

对于复合体,必须限制母体而不是其一部分。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| bodyA | MatterJS.BodyType | 否 |  | 首个可能附加这种限制的`Body`. |
| bodyB | MatterJS.BodyType | 否 |  | 附加这一限制的第二个可能的`Body`. |
| length | number | 是 |  | 一个指定约束的休息时间目标长度的号码。如果未给出,则从`constraint.bodyA`和`constraint.bodyB`的初始位置自动计算为`Constraint.create`。 |
| stiffness | number | 是 | 1 | 一个数字,它指定了约束的硬度,即它返回休息的`constraint.length`的速度。一个值的`1`表示约束应该非常坚硬。一个值的`0.2`表示约束作为软弹簧。 |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](/api/typedef/types-physics-matter#matterconstraintconfig) | 是 |  | 用于设定创建时初始约束属性的可选约束配置对象。 |


**返回值:** MatterJS.ConstraintType - 联合来文约束。


> 源码：[src/physics/matter-js/Factory.js#L585](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L585)  
引入版本：3.0.0


---

### mesh {#mesh}

#### \<instance> mesh(composite, columns, rows, crossBrace, [options]) {#instance-meshcomposite-columns-rows-crossbrace-options}


**说明:**

将复合体中的身体与网格模式中的制约连接起来,并带有可选的交叉括号.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| composite | MatterJS.CompositeType | 否 | 所有机构将连在一起的复合体。 |
| columns | number | 否 | 网格中的列数. |
| rows | number | 否 | 网格中的行数. |
| crossBrace | boolean | 否 | 还要为网状膜建立交叉架? |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](/api/typedef/types-physics-matter#matterconstraintconfig) | 是 | 用于设定创建时初始约束属性的可选约束配置对象。 |


**返回值:** MatterJS.CompositeType - 最初的复合物被传递到这种方法中.


> 源码：[src/physics/matter-js/Factory.js#L492](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L492)  
引入版本：3.0.0


---

### mouseSpring {#mouseSpring}

#### \<instance> mouseSpring([options]) {#instance-mousespringoptions}


**说明:**

此方法为`Factory.pointerConstraint`的别名.

指针约束是一种特殊类型的约束, 允许您在 Mater World 中单击并拖动身体。 它监视在场景中的主动指针, 当按下它时, 它会检查是否击中世界上任何活动身体的任何部分。 如果它确实击中, 并且身体已启用输入, 它会开始拖动它, 直到释放, 或者通过 `stopDrag` 方法停止它 。

您可以通过创建上的`options`对象来调整约束的硬度,长度和其他属性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](/api/typedef/types-physics-matter#matterconstraintconfig) | 是 | 用于设定创建时初始约束属性的可选约束配置对象。 |


**返回值:** MatterJS.ConstraintType - 联合来文约束。


> 源码：[src/physics/matter-js/Factory.js#L744](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L744)  
引入版本：3.0.0


---

### newtonsCradle {#newtonsCradle}

#### \<instance> newtonsCradle(x, y, number, size, length) {#instance-newtonscradlex-y-number-size-length}


**说明:**

以牛顿摇篮设定的机体和制约来创建复合体.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 摇篮起始的横向位置. |
| y | number | 否 | 摇篮开始的垂直位置. |
| number | number | 否 | 摇篮里球的数量。 |
| size | number | 否 | 摇篮中每个球的半径. |
| length | number | 否 | 球的长度是"弦"的悬浮。 |


**返回值:** MatterJS.CompositeType - 牛顿摇篮复合材料.


> 源码：[src/physics/matter-js/Factory.js#L511](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L511)  
引入版本：3.0.0


---

### pointerConstraint {#pointerConstraint}

#### \<instance> pointerConstraint([options]) {#instance-pointerconstraintoptions}


**说明:**

指针约束是一种特殊类型的约束, 允许您在 Mater World 中单击并拖动身体。 它监视在场景中的主动指针, 当按下它时, 它会检查是否击中世界上任何活动身体的任何部分。 如果它确实击中, 并且身体已启用输入, 它会开始拖动它, 直到释放, 或者通过 `stopDrag` 方法停止它 。

您可以通过创建上的`options`对象来调整约束的硬度,长度和其他属性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](/api/typedef/types-physics-matter#matterconstraintconfig) | 是 | 用于设定创建时初始约束属性的可选约束配置对象。 |


**返回值:** MatterJS.ConstraintType - 联合来文约束。


> 源码：[src/physics/matter-js/Factory.js#L768](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L768)  
引入版本：3.0.0


---

### polygon {#polygon}

#### \<instance> polygon(x, y, sides, radius, [options]) {#instance-polygonx-y-sides-radius-options}


**说明:**

创建新的刚性多边形体,并添加到世界中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 身体中心X坐标. |
| y | number | 否 | 身体中心Y坐标. |
| sides | number | 否 | 多边形的边数 。 |
| radius | number | 否 | 多边形的"辐射",即从它的中心到任何顶点的距离,这也是它的环绕半径. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** MatterJS.BodyType - 联合来文机构。


> 源码：[src/physics/matter-js/Factory.js#L147](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L147)  
引入版本：3.0.0


---

### pyramid {#pyramid}

#### \<instance> pyramid(x, y, columns, rows, columnGap, rowGap, callback) {#instance-pyramidx-y-columns-rows-columngap-rowgap-callback}


**说明:**

创建包含在金字塔安排中调用回调中创建的天体的新复合体。此函数使用天体边框来防止重叠。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这种复合材料在世界的横向位置. |
| y | number | 否 | 这种复合材料在世界的垂直位置. |
| columns | number | 否 | 金字塔中的柱数. |
| rows | number | 否 | 金字塔中的行数. |
| columnGap | number | 否 | 每列之间的距离. |
| rowGap | number | 否 | 每行之间的距离. |
| callback | function | 否 | 要引用的回调函数 。 |


**返回值:** MatterJS.CompositeType - 联合材料综合金字塔


> 源码：[src/physics/matter-js/Factory.js#L446](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L446)  
引入版本：3.0.0


---

### rectangle {#rectangle}

#### \<instance> rectangle(x, y, width, height, [options]) {#instance-rectanglex-y-width-height-options}


**说明:**

创建新的刚性矩形体,并加入到世界中.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 身体中心X坐标. |
| y | number | 否 | 身体中心Y坐标. |
| width | number | 否 | 体宽. |
| height | number | 否 | 身高之高处. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** MatterJS.BodyType - 联合来文机构。


> 源码：[src/physics/matter-js/Factory.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L77)  
引入版本：3.0.0


---

### softBody {#softBody}

#### \<instance> softBody(x, y, columns, rows, columnGap, rowGap, crossBrace, particleRadius, [particleOptions], [constraintOptions]) {#instance-softbodyx-y-columns-rows-columngap-rowgap-crossbrace-particleradius-particleoptions-constraintoptions}


**说明:**

创建像对象一样的简单柔软的身体。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这种复合材料在世界的横向位置. |
| y | number | 否 | 这种复合材料在世界的垂直位置. |
| columns | number | 否 | 复合体中的列数. |
| rows | number | 否 | 复合体中的行数. |
| columnGap | number | 否 | 每列之间的距离. |
| rowGap | number | 否 | 每行之间的距离. |
| crossBrace | boolean | 否 | `true`在身体之间创建交叉支架,或者`false`仅仅创建直支架. |
| particleRadius | number | 否 | 复合材料中每个圆粒体的半径. |
| particleOptions | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |
| constraintOptions | [Phaser.Types.Physics.Matter.MatterConstraintConfig](/api/typedef/types-physics-matter#matterconstraintconfig) | 是 | 用于设定创建时初始约束属性的可选约束配置对象。 |


**返回值:** MatterJS.CompositeType - 一个新的复合简单软体.


> 源码：[src/physics/matter-js/Factory.js#L557](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L557)  
引入版本：3.0.0


---

### spring {#spring}

#### \<instance> spring(bodyA, bodyB, [length], [stiffness], [options]) {#instance-springbodya-bodyb-length-stiffness-options}


**说明:**

此方法为`Factory.constraint`的别名.

限制(或关节)用于规定两个机构之间必须保持固定距离,或一个机构和固定的世界空间位置。

约束的僵硬性可以被修改以产生弹簧或弹性.

模拟回旋约束(或称针联)设置`length: 0`和高值的`stiffness`(如`0.7`或以上).

如果约束不稳定, 请尝试在 Materal Config 中降低 `stiffness` 值和 / 或增加 `constraintIterations` 。

对于复合体,必须限制母体而不是其一部分。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| bodyA | MatterJS.BodyType | 否 |  | 首个可能附加这种限制的`Body`. |
| bodyB | MatterJS.BodyType | 否 |  | 附加这一限制的第二个可能的`Body`. |
| length | number | 是 |  | 一个指定约束的休息时间目标长度的号码。如果未给出,则从`constraint.bodyA`和`constraint.bodyB`的初始位置自动计算为`Constraint.create`。 |
| stiffness | number | 是 | 1 | 一个数字,它指定了约束的硬度,即它返回休息的`constraint.length`的速度。一个值的`1`表示约束应该非常坚硬。一个值的`0.2`表示约束作为软弹簧。 |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](/api/typedef/types-physics-matter#matterconstraintconfig) | 是 |  | 用于设定创建时初始约束属性的可选约束配置对象。 |


**返回值:** MatterJS.ConstraintType - 联合来文约束。


> 源码：[src/physics/matter-js/Factory.js#L617](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L617)  
引入版本：3.0.0


---

### sprite {#sprite}

#### \<instance> sprite(x, y, key, [frame], [options]) {#instance-spritex-y-key-frame-options}


**说明:**

创建物质物理Sprite游戏对象。

斯普林特游戏对象用于在游戏中显示静态和动画图像。斯普林特可以有输入事件和物理体,也可以被调色,有色,有卷轴和动画.

斯普丽特和图像游戏对象的主要区别在于无法动画图像。因此,斯普丽特需要花费更长的时间来处理,并且由于动画组件而具有更大的API脚印。如果不需要动画,那么可以安全地使用图像来替换所有情况下的斯普丽特.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| key | string | 否 | 此游戏对象将使用的质地密钥用于渲染, 如保存在质地管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在渲染的纹理可选框架。 设定为 `null` 以跳过此值 。 |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** [Phaser.Physics.Matter.Sprite](/api/class/physics-matter-sprite) - 物质闪烁游戏对象 。


> 源码：[src/physics/matter-js/Factory.js#L854](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L854)  
引入版本：3.0.0


---

### stack {#stack}

#### \<instance> stack(x, y, columns, rows, columnGap, rowGap, callback) {#instance-stackx-y-columns-rows-columngap-rowgap-callback}


**说明:**

创建包含在网格安排中回调中创建的天体的新复合体.

此函数使用正文边界来防止重叠.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这种复合材料在世界的横向位置. |
| y | number | 否 | 这种复合材料在世界的垂直位置. |
| columns | number | 否 | 网格中的列数. |
| rows | number | 否 | 网格中的行数. |
| columnGap | number | 否 | 每列之间的距离. |
| rowGap | number | 否 | 每行之间的距离. |
| callback | function | 否 | 创建堆栈的回调. |


**返回值:** MatterJS.CompositeType - 包含在召回中创建的对象的新复合材料 。


> 源码：[src/physics/matter-js/Factory.js#L419](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L419)  
引入版本：3.0.0


---

### tileBody {#tileBody}

#### \<instance> tileBody(tile, [options]) {#instance-tilebodytile-options}


**说明:**

围绕一个砖块创建一个包, 以提供对相应物质体的访问。 砖块只能有一个物质体与之相关。 您可以在现有的砖块中通过一个物质体, 或者允许构造者为您创建相应的实体。 如果砖块有碰撞组( 以平面定义) , 这些形状将用来创建主体。 否则, 砖块的矩形边框将被使用 。

相应的机体可以通过Tile.physics.ZmatterBody在Tile上自行访问.

注:并非所有倾斜碰撞形状都得到支持。更多信息请参见Phaser.Physics.Matter.TileBody#setFromTileCollision。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tile | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 目标瓦,应该有一个物质体。 |
| options | [Phaser.Types.Physics.Matter.MatterTileOptions](/api/typedef/types-physics-matter#mattertileoptions) | 是 | 创建 Matter 天体时要使用的选项 。 |


**返回值:** [Phaser.Physics.Matter.TileBody](/api/class/physics-matter-tilebody) - 物质图纸游戏对象.


> 源码：[src/physics/matter-js/Factory.js#L829](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L829)  
引入版本：3.0.0


---

### trapezoid {#trapezoid}

#### \<instance> trapezoid(x, y, width, height, slope, [options]) {#instance-trapezoidx-y-width-height-slope-options}


**说明:**

创建新的硬质的陷阱体并添加到世界中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 身体中心X坐标. |
| y | number | 否 | 身体中心Y坐标. |
| width | number | 否 | 宽度的Trepezoid体。 |
| height | number | 否 | 夹层体的高度。 |
| slope | number | 否 | 夹角的斜率. 0 创建矩形, 1 创建三角形。 正面值使上方缩短, 而负值则使下方缩短 。 |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** MatterJS.BodyType - 联合来文机构。


> 源码：[src/physics/matter-js/Factory.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L100)  
引入版本：3.0.0


---

### worldConstraint {#worldConstraint}

#### \<instance> worldConstraint(body, [length], [stiffness], [options]) {#instance-worldconstraintbody-length-stiffness-options}


**说明:**

限制(或关节)用于规定两个机构之间必须保持固定距离,或一个机构和固定的世界空间位置。

约束世界只有一个机构, 您应该在约束选项参数中指定 `pointA` 位置, 以附加约束世界 。

约束的僵硬性可以被修改以产生弹簧或弹性.

模拟回旋约束(或称针联)设置`length: 0`和高值的`stiffness`(如`0.7`或以上).

如果约束不稳定, 请尝试在 Materal Config 中降低 `stiffness` 值和 / 或增加 `constraintIterations` 。

对于复合体,必须限制母体而不是其一部分。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | MatterJS.BodyType | 否 |  | 附加这一约束的物质`Body`。 |
| length | number | 是 |  | 指定约束的剩余目标长度的编号。如果未给出,则自动计算为 `Constraint.create` 原职 `constraint.bodyA` 财务报告和已审计财务报表 `constraint.bodyB`. |
| stiffness | number | 是 | 1 | 一个数字,它指定了约束的硬度,即它返回休息的`constraint.length`的速度。一个值的`1`表示约束应该非常坚硬。一个值的`0.2`表示约束作为软弹簧。 |
| options | [Phaser.Types.Physics.Matter.MatterConstraintConfig](/api/typedef/types-physics-matter#matterconstraintconfig) | 是 |  | 用于设定创建时初始约束属性的可选约束配置对象。 |


**返回值:** MatterJS.ConstraintType - 联合来文约束。


> 源码：[src/physics/matter-js/Factory.js#L696](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/Factory.js#L696)  
引入版本：3.0.0


---

---
