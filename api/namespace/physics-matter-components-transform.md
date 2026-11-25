# Phaser.Physics.Matter.Components.Transform {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter-components-transform)

Scope: 
static
> 源码：[src/physics/matter-js/components/Transform.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Transform.js#L17)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### angle {#angle}

#### angle: number {#angle-number}


**说明:**

使用 `angle` 设置或获得与此游戏对象相关的物理正体旋转。 与 `rotation` 不同, 当设置此值时, 它以度来指定, 值在内部转换为弧度 。


> 源码：[src/physics/matter-js/components/Transform.js#L174](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Transform.js#L174)  
引入版本：3.0.0


---

### rotation {#rotation}

#### rotation: number {#rotation-number}


**说明:**

使用 `rotation` 设置或获得与此 Game Object 相关的物理体旋转。 设定时的值必须是弧度 。


> 源码：[src/physics/matter-js/components/Transform.js#L196](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Transform.js#L196)  
引入版本：3.0.0


---

### scale {#scale}

#### scale: number {#scale-number}


**说明:**

这是一个特殊的设置器, 允许您同时将游戏对象的横向和纵向尺度设置为相同的值。 当读取此值时, 返回的结果是 `(scaleX + scaleY) / 2` 。

使用此属性意味着您希望水平和垂直的尺度是平等的。 如果不是, 请使用 `scaleX` 或 `scaleY` 属性 。


> 源码：[src/physics/matter-js/components/Transform.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Transform.js#L74)  
引入版本：3.88.0


---

### scaleX {#scaleX}

#### scaleX: number {#scalex-number}


**说明:**

此游戏对象的横向尺度 。


> 源码：[src/physics/matter-js/components/Transform.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Transform.js#L99)  
引入版本：3.0.0


---

### scaleY {#scaleY}

#### scaleY: number {#scaley-number}


**说明:**

此游戏对象的垂直尺度 。


> 源码：[src/physics/matter-js/components/Transform.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Transform.js#L137)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

此游戏对象的 x 位置 。


> 源码：[src/physics/matter-js/components/Transform.js#L28](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Transform.js#L28)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

此游戏对象的y 位置 。


> 源码：[src/physics/matter-js/components/Transform.js#L51](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Transform.js#L51)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### setAngle {#setAngle}

#### \<instance> setAngle([degrees]) {#instance-setangledegrees}


**说明:**

立即设定机体的角,角速度,位置,力等均保持不变.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| degrees | number | 是 | 0 | 角度设定,以度计. |


**返回值:** [Phaser.Physics.Matter.Components.Transform](/api/namespace/physics-matter-components-transform) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Transform.js#L283](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Transform.js#L283)  
引入版本：3.0.0


---

### setFixedRotation {#setFixedRotation}

#### \<instance> setFixedRotation() {#instance-setfixedrotation}


**说明:**

设定固定旋转将机体惯性设置到无限,这使其无法在施加力时旋转.


**返回值:** [Phaser.Physics.Matter.Components.Transform](/api/namespace/physics-matter-components-transform) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Transform.js#L267](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Transform.js#L267)  
引入版本：3.0.0


---

### setPosition {#setPosition}

#### \<instance> setPosition([x], [y]) {#instance-setpositionx-y}


**说明:**

设置物理体沿 x 和 y 轴的位置。 如果没有提供, 则两个参数都是可选的, 默认为 0。 速度、 角度、 力等不变 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 身体的横向位置. |
| y | number | 是 | "x" | 身体的垂直位置. |


**返回值:** [Phaser.Physics.Matter.Components.Transform](/api/namespace/physics-matter-components-transform) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Transform.js#L220](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Transform.js#L220)  
引入版本：3.0.0


---

### setRotation {#setRotation}

#### \<instance> setRotation([radians]) {#instance-setrotationradians}


**说明:**

立即设定机体的角,角速度,位置,力等均保持不变.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| radians | number | 是 | 0 | 身体的角度,用弧度表示. |


**返回值:** [Phaser.Physics.Matter.Components.Transform](/api/namespace/physics-matter-components-transform) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Transform.js#L245](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Transform.js#L245)  
引入版本：3.0.0


---

### setScale {#setScale}

#### \<instance> setScale([x], [y], [point]) {#instance-setscalex-y-point}


**说明:**

设置此游戏对象及其基础 Matter.js 物理体的大小。可选的 `point` 参数指定了缩放的源头。如果省略,则从当前天体的位置应用缩放。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 1 | 此游戏对象的横向尺度 。 |
| y | number | 是 | "x" | 此游戏对象的垂直尺度。 如果不设定, 将使用 x 值 。 |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 |  | 缩放的点( Vector2) 。 |


**返回值:** [Phaser.Physics.Matter.Components.Transform](/api/namespace/physics-matter-components-transform) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/Transform.js#L305](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/Transform.js#L305)  
引入版本：3.0.0


---

---
