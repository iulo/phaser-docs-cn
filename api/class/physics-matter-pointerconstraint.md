# PointerConstraint {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-matter-pointerconstraint)

指针约束是一种特殊类型的约束, 允许您在 Mater World 中单击并拖动物理体。 它监视在场景中的主动指针, 当按下它时, 它会检查是否击中世界上任何活动物理体的任何部分。 如果它确实击中, 并且物理体已启用输入, 它会开始拖动它, 直到释放, 或者通过 `stopDrag` 方法停止它 。

您可以通过创建上的`options`对象来调整约束的硬度,长度和其他属性.

**构造函数**

`new PointerConstraint(scene, world, [options])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 指向这个指针约束器所属的场景 。 |
| world | [Phaser.Physics.Matter.World](/api/class/physics-matter-world) | 否 | 提到这个约束组织所属的 Matter World excord 实例。 |
| options | object | 是 | 一个约束配置对象 。 |

---


**作用域**: static

> 源码：[src/physics/matter-js/PointerConstraint.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L19)  
引入版本：3.0.0

## 公开成员 {#public-members}

### active {#active}

#### active: boolean {#active-boolean}


**说明:**

这是否是约束活动?

每次更新都会处理一个活动约束。 将跳过一个不活动约束。 使用此功能来切换一个 指针约束 。


> 源码：[src/physics/matter-js/PointerConstraint.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L102)  
引入版本：3.0.0


---

### body {#body}

#### body: MatterJS.BodyType {#body-matterjsbodytype}


**说明:**

目前拖着的物理体,如果有的话。


> 源码：[src/physics/matter-js/PointerConstraint.js#L124](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L124)  
引入版本：3.16.2


---

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#camera-phasercamerasscene2dcamera}


**说明:**

点球手在输入下行事件处理时与之互动的摄像机.


> 源码：[src/physics/matter-js/PointerConstraint.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L81)  
引入版本：3.0.0


---

### constraint {#constraint}

#### constraint: MatterJS.ConstraintType {#constraint-matterjsconstrainttype}


**说明:**

用于附着在物理体上的原生物质约束.


> 源码：[src/physics/matter-js/PointerConstraint.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L142)  
引入版本：3.0.0


---

### part {#part}

#### part: MatterJS.BodyType {#part-matterjsbodytype}


**说明:**

被点击开始拖曳的机身部分.


> 源码：[src/physics/matter-js/PointerConstraint.js#L133](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L133)  
引入版本：3.16.2


---

### pointer {#pointer}

#### pointer: [Phaser.Input.Pointer](/api/class/input-pointer) {#pointer-phaserinputpointer}


**说明:**

启用此约束的输入指针的引用。 此设置在 `onDown` 处理器中 。


> 源码：[src/physics/matter-js/PointerConstraint.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L91)  
引入版本：3.0.0


---

### position {#position}

#### position: [Phaser.Math.Vector2](/api/class/math-vector2) {#position-phasermathvector2}


**说明:**

内部转变的位置.


> 源码：[src/physics/matter-js/PointerConstraint.js#L115](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L115)  
引入版本：3.0.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

指针约束属于的场景。 这是与 Mater World 实例相同的场景 。


> 源码：[src/physics/matter-js/PointerConstraint.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L62)  
引入版本：3.0.0


---

### world {#world}

#### world: [Phaser.Physics.Matter.World](/api/class/physics-matter-world) {#world-phaserphysicsmatterworld}


**说明:**

提到这个约束组织所属的 Matter World excord 实例。


> 源码：[src/physics/matter-js/PointerConstraint.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L72)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这个“指针”约束实例及其所有引用。


> 源码：[src/physics/matter-js/PointerConstraint.js#L361](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L361)  
引入版本：3.0.0


---

### getBody {#getBody}

#### \<instance> getBody(pointer) {#instance-getbodypointer}


**说明:**

扫描当前 Matery World 中所有活动体,看看是否有任何物理体被 Pointer 击中。发现的 _ first one_ 被设定为活动约束体 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 引用启动拖曳的指针 。 |


**返回值:** boolean - 如果发现物理体并设定了`true`, 否则是`false`.


**触发事件:** [Phaser.Physics.Matter.Events#event:DRAG_START](/api/event/physics-matter-events#drag_start)


> 源码：[src/physics/matter-js/PointerConstraint.js#L194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L194)  
引入版本：3.16.2


---

### hitTestBody {#hitTestBody}

#### \<instance> hitTestBody(body, position) {#instance-hittestbodybody-position}


**说明:**

扫描当前物理体以确定其部分是否被点击。如果找到一部分,则将它设定为`constraint.bodyB`属性以及本类的`body`属性。该部分也设定了。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | MatterJS.BodyType | 否 | 物质体要检查。 |
| position | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 一个翻译的命中测试位置 |


**返回值:** boolean - 如果物理体的一部分被击中,则`true`,否则则`false`.


> 源码：[src/physics/matter-js/PointerConstraint.js#L236](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L236)  
引入版本：3.16.2


---

### onDown {#onDown}

#### \<instance> onDown(pointer) {#instance-ondownpointer}


**说明:**

已按下一个指针到场景上 。

如果此约束没有主动指针, 那么在_ next_ call to `update` 期间, 将设定一个命中测试以对世界上所有活动体进行。 如果找到一个物理体, 它将受到此约束, 拖曳开始 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 指向被按下的指针 |


> 源码：[src/physics/matter-js/PointerConstraint.js#L157](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L157)  
引入版本：3.0.0


---

### onUp {#onUp}

#### \<instance> onUp(pointer) {#instance-onuppointer}


**说明:**

现场释放了指针 如果这是这个限制 就可以清除

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 参考了被释放的指针 |


> 源码：[src/physics/matter-js/PointerConstraint.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L178)  
引入版本：3.22.0


---

### stopDrag {#stopDrag}

#### \<instance> stopDrag() {#instance-stopdrag}


**说明:**

阻止指针控制器 拖动物理体任何进一步。

如果在主动拖曳一个物理体时释放指针,则自动调用。或者,你可以手动调用,以释放一个物理体不受约束,而不必先释放指针。


**触发事件:** [Phaser.Physics.Matter.Events#event:DRAG_END](/api/event/physics-matter-events#drag_end)


> 源码：[src/physics/matter-js/PointerConstraint.js#L332](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L332)  
引入版本：3.16.2


---

### update {#update}

#### \<instance> update() {#instance-update}


**说明:**

内部更新处理器。 在“ 关键” 步骤前已调用 。


**触发事件:** [Phaser.Physics.Matter.Events#event:DRAG](/api/event/physics-matter-events#drag)


> 源码：[src/physics/matter-js/PointerConstraint.js#L280](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PointerConstraint.js#L280)  
引入版本：3.0.0


---

---
