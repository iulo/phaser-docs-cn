# Types.Physics.Matter {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-physics-matter)

## MatterBody {#matterbody}

### \<static> MatterBody {#static-matterbody}

**类型**: MatterJS.BodyType | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | [Phaser.Physics.Matter.Image](/api/class/physics-matter-image) | [Phaser.Physics.Matter.Sprite](/api/class/physics-matter-sprite) | [Phaser.Physics.Matter.TileBody](/api/class/physics-matter-tilebody)

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterBody.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterBody.js#L1)  
引入版本：3.22.0

---

## MatterBodyConfig {#matterbodyconfig}

### \<static> MatterBodyConfig {#static-matterbodyconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| label | string | 是 | "'Body'" | 一个任意的字符串命名,以帮助识别这个机构. |
| shape | string \| [Phaser.Types.Physics.Matter.MatterSetBodyConfig](/api/typedef/types-physics-matter#mattersetbodyconfig) | 是 | null | 设定此游戏对象以创建并使用基于给定的配置对象的新对象 。 |
| parts | Array.\<MatterJS.BodyType> | 是 |  | 构成这个物理体的一组体。 数组中的第一个体必须总是对当前体例的自我参照。 `parts` 阵列中的所有体一起组成一个单一的刚性复合体。 |
| plugin | any | 是 |  | 用于存储插件特定属性的专有对象 。 |
| wrapBounds | any | 是 |  | 用于存储包边框的对象 。 |
| angle | number | 是 | 0 | 数字表示物理体的角度,用弧度表示. |
| vertices | Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 是 | null | 一组指定刚性物理体的对流体的`Vector`物体。这些应该提供,说明`(0, 0)`的来源。 |
| position | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 指定当前物理体世界空间位置的 `Vector` 。 |
| force | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 指定当前步骤中应用的力度的 `Vector` 。 它在每 `Body.update` 之后是零。 另见 `Body.applyForce` 。 |
| torque | number | 是 | 0 | 指定当前步骤中应用的矩( 转动力) 的 `Number` 。 它在每 `Body.update` 之后均为零 。 |
| isSensor | boolean | 是 | false | 标志表示物理体是否是传感器,传感器触发碰撞事件,但不会与碰撞物理体发生物理反应. |
| isStatic | boolean | 是 | false | 表示一个物理体是否被视为静止的旗帜,静止的物体永远不能改变位置或角度,并且完全固定. |
| sleepThreshold | number | 是 | 60 | 一种`Number`定义了这个物理体在被`Matter.Sleeping`舱设定为睡眠前必须具有近零速度的更新数量(如果睡眠是由引擎所允许的). |
| density | number | 是 | 0.001 | A. 国家 `Number` 定义物理体密度,即单位面积质量。如果通过 `Body.create` 编号 `mass` 属性会自动根据对象的大小(面积)来计算。这通常比简单地设定质量更可取,并允许对材料进行更直观的定义(例如岩石的密度高于木材)。 |
| restitution | number | 是 | 0 | 定义物理体还原(弹性)的 `Number`。数值总是正值,在 `(0, 1)` 范围内 。 |
| friction | number | 是 | 0.1 | 定义物理体摩擦的 `Number` 值总是正值,在`(0, 1)`的幅度内,`0`的值表示物理体可以无限滑动,`1`的值表示在施加力后物理体几乎会立即停止. |
| frictionStatic | number | 是 | 0.5 | A. 国家 `Number` 定义物理体静电摩擦(在库伦布摩擦模型中)。 `0` 表示物理体在接近静止状态时不会"棍子",只有动态 `friction` 。数值越高(例如, `10`),在接近固定状态时,它会用更多的力量使物理体在初始状态下移动。 `friction` 属性,以方便更改 `friction` 并保持适当数量的静电摩擦. |
| frictionAir | number | 是 | 0.01 | 定义物理体的空气摩擦(空气阻力)的`Number`. 值为`0`表示物理体在穿越空间时永远不会慢下来,值越高,一个物理体在穿越空间时会慢下来. |
| collisionFilter | [Phaser.Types.Physics.Matter.MatterCollisionFilter](/api/typedef/types-physics-matter#mattercollisionfilter) | 是 |  | 指定此物理体碰撞过滤特性的 `Object` 。 |
| slop | number | 是 | 0.05 | 一个 `Number` 指定一个机构允许“ 沉积” 或旋转到其它机构的程度的容积。 避免改变这个值, 除非您理解 `slop` 在物理引擎中的目的。 默认通常应该足够, 尽管非常大的机构可能需要更大的值来稳定堆叠 。 |
| timeScale | number | 是 | 1 | 一个允许每个物理体时间缩放的`Number`,例如一个力场,里面的人体在缓慢运动中,而其他的则在全速上. |
| chamfer | number \| Array.\<number> | [Phaser.Types.Physics.Matter.MatterChamferConfig](/api/typedef/types-physics-matter#matterchamferconfig) | 是 | null | 一个数字,或数组,用来勾结物理体的顶点,或一个完整的凸轮配置对象. |
| circleRadius | number | 是 | 0 | 圆形的半径 |
| mass | number | 是 | 0 | 一个定义物理体质量的`Number`,尽管更合适的是指定`density`属性。如果修改这个值,也必须修改`body.inverseMass`属性(`1 / mass`)。 |
| inverseMass | number | 是 | 0 | 一个定义正体反质量的`Number`(`1 / mass`)。如果修改这个值,也必须修改`body.mass`属性。 |
| scale | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 指定物理体初始尺度的`Vector`. |
| gravityScale | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 一种`Vector`,当它适用于这个机构时,它能测量世界重力的影响。 |
| ignoreGravity | boolean | 是 | false | 如果本机构忽视世界引力,那就更是令人毛骨悚然。 |
| ignorePointer | boolean | 是 | false | 如果这个机构忽略指针/鼠标的制约, 则会切换到布尔值 。 |
| render | [Phaser.Types.Physics.Matter.MatterBodyRenderConfig](/api/typedef/types-physics-matter#matterbodyrenderconfig) | 是 |  | 此物理体的调试Render配置对象 。 |
| onCollideCallback | function | 是 |  | 当此物理体开始与其它物理体碰撞时, 引用回调。 您可以通过提供`( pair: Matter.Pair) => void` 类型的函数来注册回调 。 |
| onCollideEndCallback | function | 是 |  | 当此物理体停止与其它物理体碰撞时, 引用回调。 您可以通过提供`( pair: Matter.Pair) => void` 类型的函数来注册回调 。 |
| onCollideActiveCallback | function | 是 |  | 在当前物理体与任何其他物理体相撞期间引用的回调。您可以通过提供`( pair: Matter.Pair) => void`的函数来注册回调。 |
| onCollideWith | any | 是 |  | `Body.setOnCollideWith`函数使用的碰撞回调词典. |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterBodyConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterBodyConfig.js#L1)  
引入版本：3.22.0

---

## MatterBodyRenderConfig {#matterbodyrenderconfig}

### \<static> MatterBodyRenderConfig {#static-matterbodyrenderconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| visible | boolean | 是 | true | 物理体应该由调试器提供吗? |
| opacity | number | 是 | 1 | 物理体及其所有部分的不透明性。 |
| fillColor | number | 是 |  | 渲染此物理体时填充的颜色值 。 |
| fillOpacity | number | 是 |  | 使这个机构时填充的不透明,值在0到1之间. |
| lineColor | number | 是 |  | 渲染此体时线条中风的颜色值 。 |
| lineOpacity | number | 是 |  | 线条在使这个正体,值在0到1之间时的不透明. |
| lineThickness | number | 是 |  | 如果渲染线条,则线条的厚度. |
| sprite | object | 是 |  | 控制物理体和父游戏对象之间的偏移,如果它有一个。 |
| sprite.xOffset | number | 是 | 0 | 物理体与父游戏对象纹理之间的水平偏移,如果它有. |
| sprite.yOffset | number | 是 | 0 | 主体与父游戏对象纹理之间的垂直抵消,如果它有一个. |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterBodyRenderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterBodyRenderConfig.js#L1)  
引入版本：3.22.0

---

## MatterBodyTileOptions {#matterbodytileoptions}

### \<static> MatterBodyTileOptions {#static-matterbodytileoptions}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| isStatic | boolean | 是 | true | 是否应该使新创建的物理体静止。 默认为真实, 因为一般的牌片不应该移动 。 |
| addToWorld | boolean | 是 | true | 是否将新创建的物理体( 或者如果使用选项. body) 添加到 Matter 的世界 。 |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterBodyTileOptions.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterBodyTileOptions.js#L1)  
引入版本：3.0.0

---

## MatterChamferConfig {#matterchamferconfig}

### \<static> MatterChamferConfig {#static-matterchamferconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| radius | number \| Array.\<number> | 是 | 8 | 单数,或数组,指定每个顶点的半径. |
| quality | number | 是 | -1 | 调色器的质量。 |
| qualityMin | number | 是 | 2 | 阴间最小质量,这个值越高,越产生顶点. |
| qualityMax | number | 是 | 14 | 阴差板的最大质量,这个值越高,越是产生顶点. |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterChamferConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterChamferConfig.js#L1)  
引入版本：3.22.0

---

## MatterCollisionData {#mattercollisiondata}

### \<static> MatterCollisionData {#static-mattercollisiondata}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| collided | boolean | 否 | 双人是否相撞? |
| bodyA | MatterJS.BodyType | 否 | 提及参与碰撞的第一只物理体. |
| bodyB | MatterJS.BodyType | 否 | 提及参与碰撞的第二具物理体. |
| axisBody | MatterJS.BodyType | 否 | 提及主轴体. |
| axisNumber | number | 否 | 主导碰撞轴矢量的指数(对接正常) |
| depth | number | 否 | 最小重叠度的碰撞深度. |
| parentA | MatterJS.BodyType | 否 | 指A体的母体,或者在没有父母的情况下指A体本身. |
| parentB | MatterJS.BodyType | 否 | 指B体的母体,或者如果B体没有父母,则指B体本身. |
| normal | MatterJS.Vector | 否 | 碰撞的正常,面对远离A体. |
| tangent | MatterJS.Vector | 否 | 碰撞的正切度正常。 |
| penetration | MatterJS.Vector | 否 | 这两具物理体之间的穿透距离. |
| supports | Array.\<MatterJS.Vector> | 否 | 一系列的支持点,或者精确的一两点。 |
| inverseMass | number | 否 | 碰撞产生的反质量 |
| friction | number | 否 | 碰撞导致的摩擦. |
| frictionStatic | number | 否 | 碰撞产生的静电摩擦. |
| restitution | number | 否 | 碰撞造成的还原。 |
| slop | number | 否 | 碰撞造成的碎片 |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterCollisionData.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterCollisionData.js#L1)  
引入版本：3.22.0

---

## MatterCollisionFilter {#mattercollisionfilter}

### \<static> MatterCollisionFilter {#static-mattercollisionfilter}


指定此物理体碰撞过滤特性的 `Object` 。

两个机构之间的碰撞将遵守以下规则:
- 如果两具物理体的无零值是`collisionFilter.group`的,
  如果数值是正值,它们总是会碰撞,它们永远不会碰撞
  如果数值为负数。
- 如果两个机构有不同的`collisionFilter.group`值或者一个
  (或两者)机构值为0,然后适用类别/任务规则如下:

每个机体都属于`collisionFilter.category`给出的碰撞类别。
值作为位字段使用,类别只应该有一个位集,意思是
此属性的值是[1, 2^31] 范围内的二种功率。因此,有32种。
现有不同碰撞类别。

每个机体还定义了由`collisionFilter.mask`给出的碰撞位图,该位图具体规定:
与之相交的类别(值是所有这些类别的位和值)。

使用分类/任务规则,如果两个体的`A`和`B`相互碰撞,则两者包括对方的
其遮罩中的类别,即`(categoryA & maskB) !== 0`和`(categoryB & maskA) !== 0`
都是真的 都一样

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| category | number | 是 | "0x0001" | 指定此物理体所属碰撞类别的位字段。 类别值只应该有一个位数, 例如 `0x0001`。 这意味着最多有32个独特的碰撞类别可用 。 |
| mask | number | 是 | "0xFFFFFFFF" | 一个指定了物理体可能碰撞的碰撞类别的小掩体. |
| group | number | 是 | 0 | 指定这个物理体所属的碰撞组的整数`Number` |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterCollisionFilter.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterCollisionFilter.js#L1)  
引入版本：3.22.0

---

## MatterCollisionPair {#mattercollisionpair}

### \<static> MatterCollisionPair {#static-mattercollisionpair}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| id | string | 否 | 独特的自动生成的碰撞对称代号,机体A和B的ID的组合. |
| bodyA | MatterJS.BodyType | 否 | 提及参与碰撞的第一只物理体. |
| bodyB | MatterJS.BodyType | 否 | 提及参与碰撞的第二具物理体. |
| contacts | Array.\<MatterJS.Vector> | 否 | 包含A和B之间所有主动联系的阵列。 |
| separation | number | 否 | A和B两体之间发生的分离量。 |
| isActive | boolean | 否 | 碰撞是否还在进行中? |
| confirmedActive | boolean | 否 | 物质是否确定碰撞正在进行中? |
| isSensor | boolean | 否 | A体或B体是传感器吗? |
| timeCreated | number | 否 | 碰撞对子创建时的时标. |
| timeUpdated | number | 否 | 碰撞对子最近一次更新时的时标. |
| collision | [Phaser.Types.Physics.Matter.MatterCollisionData](/api/typedef/types-physics-matter#mattercollisiondata) | 否 | 碰撞数据对象. |
| inverseMass | number | 否 | 碰撞产生的反质量 |
| friction | number | 否 | 碰撞导致的摩擦. |
| frictionStatic | number | 否 | 碰撞产生的静电摩擦. |
| restitution | number | 否 | 碰撞造成的还原。 |
| slop | number | 否 | 碰撞造成的碎片 |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterCollisionPair.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterCollisionPair.js#L1)  
引入版本：3.22.0

---

## MatterConstraintConfig {#matterconstraintconfig}

### \<static> MatterConstraintConfig {#static-matterconstraintconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| label | string | 是 | "'Constraint'" | 任意字符串命名,帮助识别此约束 。 |
| bodyA | MatterJS.BodyType | 是 |  | 首个可能附加这种限制的`Body`. |
| bodyB | MatterJS.BodyType | 是 |  | 附加这一限制的第二个可能的`Body`. |
| pointA | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 指定`constraint.bodyA`中心限制的抵消值的`Vector`,如果定义的话,否则是世界空间位置。 |
| pointB | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 指定`constraint.bodyB`中心限制的抵消值的`Vector`,如果定义的话,否则是世界空间位置。 |
| stiffness | number | 是 | 1 | 一个`Number`,它指定了约束的硬度,即它返回休息的`constraint.length`的速度。一个`1`值表示约束应该非常坚硬。一个`0.2`值表示约束像软弹簧一样。 |
| angularStiffness | number | 是 | 0 | 指定约束角硬度的 `Number` 。 |
| angleA | number | 是 | 0 | 强制值的 angleA。 如果设置了 bodyA, 则使用 bodyA 的角度 。 |
| angleB | number | 是 | 0 | 强制值的 angleB。 如果设置了 bodyB, 则使用 bodyB 的角度 。 |
| damping | number | 是 | 0 | 指定强制物的加固量的`Number`,即根据每个体的速度对每个体施加的阻力量限制振荡量的量. 只有在约束物也具有非常低的`stiffness`时,加固才会明显. 价值为`0.1`的值表示约束物将采用重制坝,导致很少或没有振荡. 值为`0`表示约束物不会适用加固. |
| length | number | 是 |  | A. 国家 `Number` 指定约束的剩余目标长度。它自动计算在 `Constraint.create` 原职 `constraint.bodyA` 财务报告和已审计财务报表 `constraint.bodyB`. |
| plugin | any | 是 |  | 用于存储插件特定属性的专有对象 。 |
| render | [Phaser.Types.Physics.Matter.MatterConstraintRenderConfig](/api/typedef/types-physics-matter#matterconstraintrenderconfig) | 是 |  | 此约束的调试Render配置对象 。 |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterConstraintConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterConstraintConfig.js#L1)  
引入版本：3.22.0

---

## MatterConstraintRenderConfig {#matterconstraintrenderconfig}

### \<static> MatterConstraintRenderConfig {#static-matterconstraintrenderconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| visible | boolean | 是 | true | 是否应该由调试器执行此约束 ? |
| anchors | boolean | 是 | true | 如果这种约束有锚,那么它们应该被制成吗? 柱性约束从没有锚. |
| lineColor | number | 是 |  | 执行此约束时线条中键的颜色值 。 |
| lineOpacity | number | 是 |  | 将此约束施加时线条的不透明,值介于 0 到 1 之间 。 |
| lineThickness | number | 是 |  | 如果渲染线条,则线条的厚度. |
| pinSize | number | 是 | 4 | 绘制针形约束时所画的圆圈大小 。 |
| anchorSize | number | 是 | 4 | 所画圆圈作为约束锚的大小. |
| anchorColor | number | 是 | "0xefefef" | 约束锚的颜色值 。 |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterConstraintRenderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterConstraintRenderConfig.js#L1)  
引入版本：3.22.0

---

## MatterDebugConfig {#matterdebugconfig}

### \<static> MatterDebugConfig {#static-matterdebugconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| showAxes | boolean | 是 | false | 将所有物理体轴线都磨成这样? |
| showAngleIndicator | boolean | 是 | false | 仅仅一个物理体轴? |
| angleColor | number | 是 | "0xe81153" | 车身角/轴线的颜色. |
| showBroadphase | boolean | 是 | false | 宽相网? |
| broadphaseColor | number | 是 | "0xffb400" | 广相网的颜色. |
| showBounds | boolean | 是 | false | 将物理体的界限伸展于世? |
| boundsColor | number | 是 | "0xffffff" | 体界之色相. |
| showVelocity | boolean | 是 | false | 使世界上物理体的速度变快? |
| velocityColor | number | 是 | "0x00aeef" | 体速线的颜色. |
| showCollisions | boolean | 是 | false | 将碰撞点和正常点对撞对撞。 |
| collisionColor | number | 是 | "0xf5950c" | 碰撞点的颜色。 |
| showSeparation | boolean | 是 | false | 显示物理体分离的线条。 |
| separationColor | number | 是 | "0xffa500" | 体分线的颜色. |
| showBody | boolean | 是 | true | 将世界上的动态物理体渲染到图形对象上? |
| showStaticBody | boolean | 是 | true | 将世界上的静态物理体 变成图形对象吗 ? |
| showInternalEdges | boolean | 是 | false | 当渲染物理体时, 使内部边缘也? |
| renderFill | boolean | 是 | false | 以填充颜色将物理体装好 |
| renderLine | boolean | 是 | true | 用中风把物理体打成一团 |
| fillColor | number | 是 | "0x106909" | 渲染动态体时填充的颜色值 。 |
| fillOpacity | number | 是 | 1 | 使动态体渲染时填充的不透明,值介于 0 到 1 之间 。 |
| lineColor | number | 是 | "0x28de19" | 渲染动态体时线条中风的颜色值 。 |
| lineOpacity | number | 是 | 1 | 使动态体时线条不透明,值介于 0 到 1 之间 。 |
| lineThickness | number | 是 | 1 | 如果渲染线条,则线条的厚度. |
| staticFillColor | number | 是 | "0x0d177b" | 渲染静态物理体时填充的颜色值 。 |
| staticLineColor | number | 是 | "0x1327e4" | 渲染静态体时线条中风的颜色值 。 |
| showSleeping | boolean | 是 | false | 将世界上任何睡眠体(动力体或静态体) 都显示为图形物理体? |
| staticBodySleepOpacity | number | 是 | 0.7 | 将睡眠静态物理体的不透明性乘以数量。 |
| sleepFillColor | number | 是 | "0x464646" | 渲染睡眠动态物理体时填充的颜色值 。 |
| sleepLineColor | number | 是 | "0x999a99" | 渲染睡眠动态物理体时的线条中风的颜色值. |
| showSensors | boolean | 是 | true | 被标注为传感器的发酵体或物理体部件? |
| sensorFillColor | number | 是 | "0x0d177b" | 渲染体传感器时的填充颜色. |
| sensorLineColor | number | 是 | "0x1327e4" | 渲染体传感器时的线条颜色. |
| showPositions | boolean | 是 | true | 给非静态物理体的位置? |
| positionSize | number | 是 | 4 | 绘制物理体位置时绘制的矩形大小 。 |
| positionColor | number | 是 | "0xe042da" | 绘制物理体位置时绘制的矩形的颜色值。 |
| showJoint | boolean | 是 | true | 将世界所有限制都显示在图形对象上吗 ? |
| jointColor | number | 是 | "0xe0e042" | `showJoint`设定时关节的颜色值. |
| jointLineOpacity | number | 是 | 1 | 制动关节时的线性不透明,值介于 0 到 1 之间. |
| jointLineThickness | number | 是 | 2 | 制动关节时的线厚度. |
| pinSize | number | 是 | 4 | 绘制针形约束时所画的圆圈大小 。 |
| pinColor | number | 是 | "0x42e0e0" | 绘制针形约束时绘制的圆的颜色值 。 |
| springColor | number | 是 | "0xe042e0" | 春节约束的颜色值. |
| anchorColor | number | 是 | "0xefefef" | 约束锚的颜色值 。 |
| anchorSize | number | 是 | 4 | 所画圆圈作为约束锚的大小. |
| showConvexHulls | boolean | 是 | false | 使多边形体也变成对流体? |
| hullColor | number | 是 | "0xd703d0" | `showConvexHulls`设定时船体的颜色值. |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterDebugConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterDebugConfig.js#L1)  
引入版本：3.22.0

---

## MatterRunnerConfig {#matterrunnerconfig}

### \<static> MatterRunnerConfig {#static-matterrunnerconfig}


Matter 物理运行器配置 。

只设置一个`fps`和`delta`.

`delta`是跑者固定时间步(一个物理更新)的大小.
"框架三角洲"是自上一个游戏步骤以来的时间经过.
根据帧三角洲的大小,跑者每个游戏步骤都会进行0或更多更新.

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| fps | number | 是 |  | 每秒物理更新的次数。 如果设定, 则此数将覆盖 `delta` 。 |
| delta | number | 是 | 16.666 | 更新时间步骤的大小以毫秒计。 如果设定了 `fps`, 它将覆盖 `delta` 。 |
| frameDeltaSmoothing | boolean | 是 | true | 是否平滑框架三角洲值 。 |
| frameDeltaSnapping | boolean | 是 | true | 是否将框架三角洲值绕到最近的 1 Hz 。 |
| frameDeltaHistorySize | number | 是 | 100 | 当启用平滑时, 要记录的框架三角洲值数。 将第10至第90百分位数进行抽样 。 |
| maxUpdates | number | 是 | null | 每个帧的更新数上限. |
| maxFrameTime | number | 是 | 33.333 | 在一个框架里模拟的最大时间, 以毫秒计 。 |
| enabled | boolean | 是 | true | 是否启用了物质运行器 。 |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterRunnerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterRunnerConfig.js#L1)  
引入版本：3.22.0

---

## MatterSetBodyConfig {#mattersetbodyconfig}

### \<static> MatterSetBodyConfig {#static-mattersetbodyconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 类型 | string | 是 | "'rectangle'" | 形状类型。 任意 `rectangle`, `circle`, `trapezoid`, `polygon`, `fromVertices`, `fromVerts` 或 或 时 间 `fromPhysicsEditor`. |
| x | number | 是 |  | 横向世界位置 放置物理体。 |
| y | number | 是 |  | 垂直世界的位置 将物理体放置在。 |
| width | number | 是 |  | 体之宽. |
| height | number | 是 |  | 身高之高处. |
| radius | number | 是 |  | 物理体半径,用`circle`和`polygon`形状. |
| maxSides | number | 是 | 25 | 物理体最大尺寸,用`circle`形状 |
| slope | number | 是 | 0.5 | `trapezoid`形状使用。 trapezoid. 0 的斜度创建矩形, 1 创建三角形。 正面值使顶侧缩短, 而负值使底侧缩短 。 |
| sides | number | 是 | 5 | `polygon`形状使用,多边形的边数将存在. |
| verts | string \| array | 是 |  | `fromVerts`形状使用。顶点可以显示数据。可以是路径字符串,也可以是一系列顶点。 |
| flagInternal | boolean | 是 | false | 由 `fromVerts` 形状使用. 旗内边缘( 意外部分边缘) |
| removeCollinear | number | 是 | 0.01 | `fromVerts`形状使用。 Matter.js是否丢弃山体边缘(以提高性能) 。 |
| minimumArea | number | 是 | 10 | 由`fromVerts`形状使用。在分解过程中,弃置部分的面积低于这个区域。 |
| addToWorld | boolean | 是 | true | 新机构是否应该自动加入世界? |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterSetBodyConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterSetBodyConfig.js#L1)  
引入版本：3.22.0

---

## MatterTileOptions {#mattertileoptions}

### \<static> MatterTileOptions {#static-mattertileoptions}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | MatterJS.BodyType | 是 | null | 现有物质体,不用创建新的物质体。 |
| isStatic | boolean | 是 | true | 是否应该使新创建的物理体静止。 默认为真实, 因为一般的牌片不应该移动 。 |
| addToWorld | boolean | 是 | true | 是否将新创建的物理体( 或者如果使用选项. body) 添加到 Matter 的世界 。 |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterTileOptions.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterTileOptions.js#L1)  
引入版本：3.0.0

---

## MatterWalls {#matterwalls}

### \<static> MatterWalls {#static-matterwalls}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| left | MatterJS.BodyType | 是 | null | 左边的墙是物质世界的 |
| right | MatterJS.BodyType | 是 | null | 物质世界的正确墙壁. |
| top | MatterJS.BodyType | 是 | null | 物质世界的顶部墙壁. |
| bottom | MatterJS.BodyType | 是 | null | 物质世界的底墙 |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterWalls.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterWalls.js#L1)  
引入版本：3.0.0

---

## MatterWorldConfig {#matterworldconfig}

### \<static> MatterWorldConfig {#static-matterworldconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gravity | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 设定为 QQLink Phaser.Physics.Matter.World#重力 }. |
| setBounds | object \| boolean | 是 |  | 世界是否应该默认允许界限? |
| setBounds.x | number | 是 | 0 | 世界上的x坐标线 |
| setBounds.y | number | 是 | 0 | 地球的Y坐标 |
| setBounds.width | number | 是 |  | 宽广世界界. |
| setBounds.height | number | 是 |  | 世尊高处界. |
| setBounds.thickness | number | 是 | 64 | 世间壁壁之厚薄. |
| setBounds.left | boolean | 是 | true | 左侧的世界应该围成墙吗? |
| setBounds.right | boolean | 是 | true | 右侧的世界应该围成墙吗? |
| setBounds.top | boolean | 是 | true | 顶级世界的界墙应该被创建吗? |
| setBounds.bottom | boolean | 是 | true | 是否应该创建底部世界的墙壁? |
| positionIterations | number | 是 | 6 | 执行每次更新的位置迭代次数。 数值越高, 模拟的质量就越高, 将牺牲性能。 Name |
| velocityIterations | number | 是 | 4 | 执行每次更新的速度迭代的次数。 数值越高, 模拟的质量就越高, 将牺牲性能。 |
| constraintIterations | number | 是 | 2 | 每次更新的强制迭代次数。 数值越高, 模拟的质量就越高, 将牺牲性能。 |
| enableSleeping | boolean | 是 | false | 标记可以指定引擎是否应该允许通过`Matter.Sleeping`模块睡眠。睡眠可以提高稳定性和性能,但往往会牺牲准确性。 |
| timing.timestamp | number | 是 | 0 | A. 国家 `Number` 指定当前模拟时间, 以毫秒计, 起始于 `0`逐年递增。 `Engine.update` 由给定的 `delta` 参数。 |
| timing.timeScale | number | 是 | 1 | 指定所有物理体时间的全局缩放系数的 `Number` 。 `0` 值冻结模拟。 `0.1` 值会产生慢动效应。 `1.2`值会产生快动效应 。 |
| enabled | boolean | 是 | true | 如果世界被启用或没有启用, 则切换 。 |
| correction | number | 是 | 1 | 指定用于更新的时间校正因数的可选数字。 |
| getDelta | function | 是 |  | 此功能每次核心游戏循环步骤时都会被称作,除非另有修改,否则该循环步骤将约束在请求动画框架频率上. |
| autoUpdate | boolean | 是 | true | 每次游戏步骤时自动调用 Engine.update. |
| restingThresh | number | 是 | 4 | 设置解析器休息阈值属性。 |
| restingThreshTangent | number | 是 | 6 | 设置断层器, 以休止切换属性 。 |
| positionDampen | number | 是 | 0.9 | 设置解析器位置以抑制属性。 |
| positionWarming | number | 是 | 0.8 | 设置和解方位置升温属性。 |
| frictionNormalMultiplier | number | 是 | 5 | 设置“解析器”摩擦正常乘数属性。 |
| debug | boolean \| [Phaser.Types.Physics.Matter.MatterDebugConfig](/api/typedef/types-physics-matter#matterdebugconfig) | 是 | false | 控制调试选项。如果布尔值被调试,它将使用默认值,否则将指定调试配置对象。 |
| runner | [Phaser.Types.Physics.Matter.MatterRunnerConfig](/api/typedef/types-physics-matter#matterrunnerconfig) | 是 |  | 设置物质运行器选项。 |

**类型**: object

**所属**: Phaser.Types.Physics.Matter
> 源码：[src/physics/matter-js/typedefs/MatterWorldConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterWorldConfig.js#L1)  
引入版本：3.0.0

---

---
