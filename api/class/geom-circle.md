# Circle {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/geom-circle)

圆形几何物体,由中心位置和半径定义.

这是一个几何对象,包含数字值和相关方法来检查和修改它们。它不是一个游戏对象,因为您不能将其添加到显示列表中,也没有纹理。要使一个圆圈,您应该查看图形类的能力。

圆形物体通常用于命中测试,重叠检查,遮掩,以及定义场景内感兴趣的圆形区域,可以直接使用Phaser的几何交叉方法,如`Phaser.Geom.Intersects.CircleToCircle`或`Phaser.Geom.Intersects.CircleToRectangle`,使其在不需要物理体的情况下用于简单的空间查询.

**构造函数**

`new Circle([x], [y], [radius])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 圆形中心位置的x位置. |
| y | number | 是 | 0 | 圆心的y位置. |
| radius | number | 是 | 0 | 圆之半径. |

---


**作用域**: static

> 源码：[src/geom/circle/Circle.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L14)  
引入版本：3.0.0

## 公开方法 {#public-methods}

### Area {#Area}

#### \<static> Area(circle) {#static-areacircle}


**说明:**

计算圆形的区域。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆得到的区域。 |


**返回值:** number - 圆周之域.


> 源码：[src/geom/circle/Area.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Area.js#L7)  
引入版本：3.0.0


---

### Circumference {#Circumference}

#### \<static> Circumference(circle) {#static-circumferencecircle}


**说明:**

返回给定圆的周轴。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆得到圆周. |


**返回值:** number - 圆周之圆.


> 源码：[src/geom/circle/Circumference.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circumference.js#L7)  
引入版本：3.0.0


---

### CircumferencePoint {#CircumferencePoint}

#### \<static> CircumferencePoint(circle, angle, [out]) {#static-circumferencepointcircle-angle-out}


**说明:**

返回一个矢量2对象,其中包含一个点的坐标,该点根据给定角度环绕圆圈。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆得到环点. |
| angle | number | 否 | 从圆形中心到圆形的角度返回点。 以弧度表示 。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储结果的矢量2。 如果不给定矢量2, 将会创建 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 矢量2物体,其中`x`和`y`属性是环面上的点.


> 源码：[src/geom/circle/CircumferencePoint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/CircumferencePoint.js#L9)  
引入版本：3.0.0


---

### Clone {#Clone}

#### \<static> Clone(source) {#static-clonesource}


**说明:**

根据给定源的值创建新圆实例。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Circle](/api/class/geom-circle) \| object | 否 | 要克隆的圆。可以是圆形或圆形物体的例,具有x,y和半径属性. |


**返回值:** [Phaser.Geom.Circle](/api/class/geom-circle) - 源圈的克隆体.


> 源码：[src/geom/circle/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Clone.js#L9)  
引入版本：3.0.0


---

### contains {#contains}

#### \<instance> contains(x, y) {#instance-containsx-y}


**说明:**

选中可查看圆形是否包含给定的 x / y 坐标 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | ×坐标以检查圆圈内. |
| y | number | 否 | y坐标来检查圆圈内. |


**返回值:** boolean - 如果坐标在圆圈内,则属真,否则是假的.


> 源码：[src/geom/circle/Circle.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L98)  
引入版本：3.0.0


---

### Contains {#Contains}

#### \<static> Contains(circle, x, y) {#static-containscircle-x-y}


**说明:**

选中可查看圆形是否包含给定的 x / y 坐标 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆来检查. |
| x | number | 否 | ×坐标以检查圆圈内. |
| y | number | 否 | y坐标来检查圆圈内. |


**返回值:** boolean - 如果坐标在圆圈内,则属真,否则是假的.


> 源码：[src/geom/circle/Contains.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Contains.js#L7)  
引入版本：3.0.0


---

### ContainsPoint {#ContainsPoint}

#### \<static> ContainsPoint(circle, vec) {#static-containspointcircle-vec}


**说明:**

检查是否包含存储在矢量2中的给定x和y坐标 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆来检查. |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 矢量2对象检查它的坐标是否在圆圈内. |


**返回值:** boolean - 如果矢量2坐标位于圆内,否则是虚假的.


> 源码：[src/geom/circle/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/ContainsPoint.js#L9)  
引入版本：3.0.0


---

### ContainsRect {#ContainsRect}

#### \<static> ContainsRect(circle, rect) {#static-containsrectcircle-rect}


**说明:**

检查是否包含给定矩形对象的全部四个点 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆来检查. |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) \| object | 否 | 矩形对象以检查是否在圆形内. |


**返回值:** boolean - 如果所有矩形坐标都在圆圈内,否则是虚假的.


> 源码：[src/geom/circle/ContainsRect.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/ContainsRect.js#L9)  
引入版本：3.0.0


---

### CopyFrom {#CopyFrom}

#### \<static> CopyFrom(source, dest) {#static-copyfromsource-dest}


**说明:**

复制本 `x`, `y` 财务报告和已审计财务报表 `radius` 从“属性”中 `source` 圆圈进入给定 `dest` 圆形,然后返回 `dest` 圆.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 复制值的源圆 。 |
| dest | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 复制值的目的地圆 。 |


**返回值:** [Phaser.Geom.Circle](/api/class/geom-circle) - 目的地圆.


> 源码：[src/geom/circle/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/CopyFrom.js#L7)  
引入版本：3.0.0


---

### Equals {#Equals}

#### \<static> Equals(circle, toCompare) {#static-equalscircle-tocompare}


**说明:**

比较两个给定圆圈的`x`,`y`和`radius`属性。如果全部匹配,则返回`true`,否则返回`false`。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 初圆相比较. |
| toCompare | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 第二圆相比. |


**返回值:** boolean - 如果两个圆圈相对,则`true`,否则则`false`.


> 源码：[src/geom/circle/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Equals.js#L7)  
引入版本：3.0.0


---

### GetBounds {#GetBounds}

#### \<static> GetBounds(circle, [out]) {#static-getboundscircle-out}


**说明:**

返回圆形对象的界限。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆能取法界. |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) \| object | 是 | 矩形,或类似矩形的对象,将圆形边界存储在其中。如果不给定新的矩形,则会创建。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle), object - 包含圆形界限的矩形天体.


> 源码：[src/geom/circle/GetBounds.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/GetBounds.js#L9)  
引入版本：3.0.0


---

### getPoint {#getPoint}

#### \<instance> getPoint(position, [out]) {#instance-getpointposition-out}


**说明:**

返回一个点对象,其中包含一个点的坐标,该点以给定角度为基础,使0至1. 之间正常化,即0.5的值将给出圆周180度的点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| position | number | 否 | 0到1之间的值,其中0等于0度,0.5等于180度,1等于360环绕圆圈. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储返回值的矢量2。如果不给定矢量2对象,将创建该对象。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 包含圆周点坐标的矢量2.


> 源码：[src/geom/circle/Circle.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L114)  
引入版本：3.0.0


---

### GetPoint {#GetPoint}

#### \<static> GetPoint(circle, position, [out]) {#static-getpointcircle-position-out}


**说明:**

返回一个矢量2物体,其中含有一个点的坐标,该点以给定角度为基础,使圆周的圆周度正常化到0至1. I. 即0.5的值会在圆周180度时给出点.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆得到环点. |
| position | number | 否 | 0到1之间的值,其中0等于0度,0.5等于180度,1等于360环绕圆圈. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储返回值的矢量2 实例。 如果不给定新的矢量2 对象, 将会创建 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 包含圆周点坐标的矢量2.


> 源码：[src/geom/circle/GetPoint.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/GetPoint.js#L12)  
引入版本：3.0.0


---

### getPoints {#getPoints}

#### \<instance> getPoints(quantity, [stepRate], [output]) {#instance-getpointsquantity-steprate-output}


**说明:**

返回含有环绕圆周度的点坐标的点对象数组,以给定的数量或stepRate值为基础。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| quantity | number | 否 | 返回的点数。 如果一个疟原虫值, 则数量将从 `stepRate` 中得出 。 |
| stepRate | number | 是 | 通过获得圆圈的圆圈来设定数量,再以stepRate来划分. |
| output | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 插入矢量2s的数组。 如果不提供新的数组, 将会创建 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 与圆周周围的点有关的一系列矢量2物体。


> 源码：[src/geom/circle/Circle.js#L134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L134)  
引入版本：3.0.0


---

### GetPoints {#GetPoints}

#### \<static> GetPoints(circle, quantity, [stepRate], [out]) {#static-getpointscircle-quantity-steprate-out}


**说明:**

返回含有环绕圆圈的点坐标的矢量2对象数组,其数值以给定的数量或stepRate值为准。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆取分从. |
| quantity | number | 否 | 返回的点数。 如果一个疟原虫值, 则数量将从 `stepRate` 中得出 。 |
| stepRate | number | 是 | 通过获得圆圈的圆圈来设定数量,再以stepRate来划分. |
| out | array | 是 | 插入点数组。 如果不提供新的数组, 将创建 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 与圆周周围的点有关的一系列矢量2物体。


> 源码：[src/geom/circle/GetPoints.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/GetPoints.js#L12)  
引入版本：3.0.0


---

### getRandomPoint {#getRandomPoint}

#### \<instance> getRandomPoint([vec]) {#instance-getrandompointvec}


**说明:**

从圆圈内的任意位置返回一个统一分布的随机点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 一个矢量2对象设置随机的`x`和`y`值. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 具有`x`和`y`属性中随机值的矢量2对象.


> 源码：[src/geom/circle/Circle.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L154)  
引入版本：3.0.0


---

### isEmpty {#isEmpty}

#### \<instance> isEmpty() {#instance-isempty}


**说明:**

检查是否圆形为空:半径为0。


**返回值:** boolean - 如果圆圈是空的,否则是假的。


> 源码：[src/geom/circle/Circle.js#L232](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L232)  
引入版本：3.0.0


---

### Offset {#Offset}

#### \<static> Offset(circle, x, y) {#static-offsetcircle-x-y}


**说明:**

以给出的值来抵消圆。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 将予冲抵的圆圈(译) |
| x | number | 否 | 水平抵消圆的金额由. |
| y | number | 否 | 垂直抵消圆圈的金额由. |


**返回值:** [Phaser.Geom.Circle](/api/class/geom-circle) - 被抵消的圆圈。


> 源码：[src/geom/circle/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Offset.js#L7)  
引入版本：3.0.0


---

### OffsetPoint {#OffsetPoint}

#### \<static> OffsetPoint(circle, vec) {#static-offsetpointcircle-vec}


**说明:**

以矢量2对象的`x`和`y`属性中给出的值来抵消圆。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 将予冲抵的圆圈(译) |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 含有值的矢量2对象,以抵消圆圈. |


**返回值:** [Phaser.Geom.Circle](/api/class/geom-circle) - 被抵消的圆圈。


> 源码：[src/geom/circle/OffsetPoint.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/OffsetPoint.js#L7)  
引入版本：3.0.0


---

### Random {#Random}

#### \<static> Random(circle, [out]) {#static-randomcircle-out}


**说明:**

返回一个来自指定圆内任意位置的分布一致的随机点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆从随机点. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 一个矢量2对象设置随机的`x`和`y`值. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 具有`x`和`y`属性中随机值的矢量2对象.


> 源码：[src/geom/circle/Random.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Random.js#L9)  
引入版本：3.0.0


---

### setEmpty {#setEmpty}

#### \<instance> setEmpty() {#instance-setempty}


**说明:**

设置此圆为空, 半径为 0。 不改变其位置 。


**返回值:** [Phaser.Geom.Circle](/api/class/geom-circle) - 此圆形天体 。


> 源码：[src/geom/circle/Circle.js#L193](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L193)  
引入版本：3.0.0


---

### setPosition {#setPosition}

#### \<instance> setPosition([x], [y]) {#instance-setpositionx-y}


**说明:**

设置此圆的位置。 如果省略 `y` 参数, x 和 y 位置都将设置为 `x` 的值 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 圆形中心位置的x位置. |
| y | number | 是 | 0 | 圆心的y位置. |


**返回值:** [Phaser.Geom.Circle](/api/class/geom-circle) - 此圆形天体 。


> 源码：[src/geom/circle/Circle.js#L210](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L210)  
引入版本：3.0.0


---

### setTo {#setTo}

#### \<instance> setTo([x], [y], [radius]) {#instance-settox-y-radius}


**说明:**

设置此圆的 x, y 和半径 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 圆形中心位置的x位置. |
| y | number | 是 | 0 | 圆心的y位置. |
| radius | number | 是 | 0 | 圆之半径. |


**返回值:** [Phaser.Geom.Circle](/api/class/geom-circle) - 此圆形天体 。


> 源码：[src/geom/circle/Circle.js#L171](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L171)  
引入版本：3.0.0


---

## 公开成员 {#public-members}

### bottom {#bottom}

#### bottom: number {#bottom-number}


**说明:**

圆心的最下点, 等于 `y + radius`。 设置此值会调整圆心的y位置, 同时保持半径不变 。


> 源码：[src/geom/circle/Circle.js#L355](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L355)  
引入版本：3.0.0


---

### diameter {#diameter}

#### diameter: number {#diameter-number}


**说明:**

圆的直径是半径的两倍。设置这个值也会相应更新半径。


> 源码：[src/geom/circle/Circle.js#L267](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L267)  
引入版本：3.0.0


---

### left {#left}

#### left: number {#left-number}


**说明:**

圆圈的最左端点,等于`x - radius`。设置此值会调整圆圈中心的x位置,同时保持半径不变。


> 源码：[src/geom/circle/Circle.js#L289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L289)  
引入版本：3.0.0


---

### radius {#radius}

#### radius: number {#radius-number}


**说明:**

圆的半径。 设置此值也会相应更新直径 。


> 源码：[src/geom/circle/Circle.js#L245](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L245)  
引入版本：3.0.0


---

### right {#right}

#### right: number {#right-number}


**说明:**

圆圈的最右点,等于`x + radius`。设置此值会调整圆圈中心的x位置,同时保持半径不变。


> 源码：[src/geom/circle/Circle.js#L311](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L311)  
引入版本：3.0.0


---

### top {#top}

#### top: number {#top-number}


**说明:**

圆顶点,等于`y - radius`。设置此值会调整圆中心的y位置,同时保持半径不变。


> 源码：[src/geom/circle/Circle.js#L333](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L333)  
引入版本：3.0.0


---

### type {#type}

#### type: number {#type-number}


**说明:**

此对象的几何常数类型: `GEOM_CONST.CIRCLE`. 用于快速类型比较.


> 源码：[src/geom/circle/Circle.js#L46](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L46)  
引入版本：3.19.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

圆形中心位置的x位置.


> 源码：[src/geom/circle/Circle.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L57)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

圆心的y位置.


> 源码：[src/geom/circle/Circle.js#L67](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Circle.js#L67)  
引入版本：3.0.0


---

---
