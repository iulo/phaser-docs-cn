# Phaser.Geom.Circle {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/function/geom)

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


### CircumferencePoint {#CircumferencePoint}

#### \<static> CircumferencePoint(circle, angle, [out]) {#static-circumferencepointcircle-angle-out}


**说明:**

返回一个矢量2对象,其中包含一个点的坐标,该点根据给定角度环绕圆圈。

**Tags:**

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


### CopyFrom {#CopyFrom}

#### \<static> CopyFrom(source, dest) {#static-copyfromsource-dest}


**说明:**

复制本 `x`, `y` 财务报告和已审计财务报表 `radius` 从“属性”中 `source` 圆圈进入给定 `dest` 圆形,然后返回 `dest` 圆.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 复制值的源圆 。 |
| dest | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 复制值的目的地圆 。 |


**返回值:** [Phaser.Geom.Circle](/api/class/geom-circle) - 目的地圆.


> 源码：[src/geom/circle/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/CopyFrom.js#L7)  
引入版本：3.0.0


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


### GetBounds {#GetBounds}

#### \<static> GetBounds(circle, [out]) {#static-getboundscircle-out}


**说明:**

返回圆形对象的界限。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆能取法界. |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) \| object | 是 | 矩形,或类似矩形的对象,将圆形边界存储在其中。如果不给定新的矩形,则会创建。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle), object - 包含圆形界限的矩形天体.


> 源码：[src/geom/circle/GetBounds.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/GetBounds.js#L9)  
引入版本：3.0.0


### GetPoint {#GetPoint}

#### \<static> GetPoint(circle, position, [out]) {#static-getpointcircle-position-out}


**说明:**

返回一个矢量2物体,其中含有一个点的坐标,该点以给定角度为基础,使圆周的圆周度正常化到0至1. I. 即0.5的值会在圆周180度时给出点.

**Tags:**

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


### Offset {#Offset}

#### \<static> Offset(circle, x, y) {#static-offsetcircle-x-y}


**说明:**

以给出的值来抵消圆。

**Tags:**

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


### OffsetPoint {#OffsetPoint}

#### \<static> OffsetPoint(circle, vec) {#static-offsetpointcircle-vec}


**说明:**

以矢量2对象的`x`和`y`属性中给出的值来抵消圆。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 将予冲抵的圆圈(译) |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 含有值的矢量2对象,以抵消圆圈. |


**返回值:** [Phaser.Geom.Circle](/api/class/geom-circle) - 被抵消的圆圈。


> 源码：[src/geom/circle/OffsetPoint.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/OffsetPoint.js#L7)  
引入版本：3.0.0


### Random {#Random}

#### \<static> Random(circle, [out]) {#static-randomcircle-out}


**说明:**

返回一个来自指定圆内任意位置的分布一致的随机点。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆从随机点. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 一个矢量2对象设置随机的`x`和`y`值. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 具有`x`和`y`属性中随机值的矢量2对象.


> 源码：[src/geom/circle/Random.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/circle/Random.js#L9)  
引入版本：3.0.0


# Phaser.Geom.Ellipse {#page-title-1}

### Area {#Area-1}

#### \<static> Area(ellipse) {#static-areaellipse}


**说明:**

使用公式计算给定椭圆的区域: ^ X majorRadius X minorRadius。 如果椭圆为空(即没有宽度或高度), 返回 0。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 椭圆形以获得面积. |


**返回值:** number - 椭圆形区域,或如果椭圆形为空则为0.


> 源码：[src/geom/ellipse/Area.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Area.js#L7)  
引入版本：3.0.0


### Circumference {#Circumference-1}

#### \<static> Circumference(ellipse) {#static-circumferenceellipse}


**说明:**

返回给定椭圆的周长。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 椭圆形以获得周遭. |


**返回值:** number - 椭圆形的环形.


> 源码：[src/geom/ellipse/Circumference.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Circumference.js#L7)  
引入版本：3.0.0


### CircumferencePoint {#CircumferencePoint-1}

#### \<static> CircumferencePoint(ellipse, angle, [out]) {#static-circumferencepointellipse-angle-out}


**说明:**

返回一个矢量2,其中包含一个点的坐标,这个点根据给定角度在椭圆上。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 椭圆形以获得环形点. |
| angle | number | 否 | 从椭圆中心到圆圈的角度返回点。 以弧度表示 。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储结果的矢量2。 如果不给定矢量2, 将会创建 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 矢量2物体,其中`x`和`y`属性是环面上的点.


> 源码：[src/geom/ellipse/CircumferencePoint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/CircumferencePoint.js#L9)  
引入版本：3.0.0


### Clone {#Clone-1}

#### \<static> Clone(source) {#static-clonesource-1}


**说明:**

根据给定源所含值创建新的椭圆实例。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 要克隆的椭圆。可以是椭圆形或椭圆形物体的例,具有x、y、宽度和高度等属性。 |


**返回值:** [Phaser.Geom.Ellipse](/api/class/geom-ellipse) - 源椭圆的克隆.


> 源码：[src/geom/ellipse/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Clone.js#L9)  
引入版本：3.0.0


### Contains {#Contains-1}

#### \<static> Contains(ellipse, x, y) {#static-containsellipse-x-y}


**说明:**

检查是否包含给定的 x / y 坐标 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 椭圆形去检查。 |
| x | number | 否 | x 坐标以检查椭圆内部. |
| y | number | 否 | 以Y坐标检查椭圆内. |


**返回值:** boolean - 如果坐标在椭圆内,则真实性不正确,否则是虚假的。


> 源码：[src/geom/ellipse/Contains.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Contains.js#L7)  
引入版本：3.0.0


### ContainsPoint {#ContainsPoint-1}

#### \<static> ContainsPoint(ellipse, vec) {#static-containspointellipse-vec}


**说明:**

检查是否在椭圆形上包含所指定的x和y坐标, 并存储在矢量2 中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 椭圆形去检查。 |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 矢量2对象检查它的坐标是否在椭圆内. |


**返回值:** boolean - 如果矢量2坐标在椭圆内,否则是虚假的.


> 源码：[src/geom/ellipse/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/ContainsPoint.js#L9)  
引入版本：3.0.0


### ContainsRect {#ContainsRect-1}

#### \<static> ContainsRect(ellipse, rect) {#static-containsrectellipse-rect}


**说明:**

选中可查看椭圆是否包含给定矩形对象的全部四个点 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 椭圆形去检查。 |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) \| object | 否 | 矩形对象以检查是否在椭圆形内. |


**返回值:** boolean - 如果所有矩形坐标都在椭圆内,否则是虚假的.


> 源码：[src/geom/ellipse/ContainsRect.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/ContainsRect.js#L9)  
引入版本：3.0.0


### CopyFrom {#CopyFrom-1}

#### \<static> CopyFrom(source, dest) {#static-copyfromsource-dest-1}


**说明:**

复制本 `x`, `y`, `width` 财务报告和已审计财务报表 `height` 从“属性”中 `source` 椭圆进入给定 `dest` 椭圆,然后返回 `dest` 椭圆形.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 源 Ellipse 复制这些值 。 |
| dest | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 目标椭圆复制值到 。 |


**返回值:** [Phaser.Geom.Ellipse](/api/class/geom-ellipse) - 目的地椭圆形.


> 源码：[src/geom/ellipse/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/CopyFrom.js#L7)  
引入版本：3.0.0


### Equals {#Equals-1}

#### \<static> Equals(ellipse, toCompare) {#static-equalsellipse-tocompare}


**说明:**

比较两个给定椭圆形的`x`,`y`,`width`和`height`的属性. 如果全部匹配,返回`true`,否则返回`false`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 最早的椭圆比较. |
| toCompare | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 第二椭圆相较. |


**返回值:** boolean - 如果两个椭圆相等,则`true`,否则则`false`.


> 源码：[src/geom/ellipse/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Equals.js#L7)  
引入版本：3.0.0


### GetBounds {#GetBounds-1}

#### \<static> GetBounds(ellipse, [out]) {#static-getboundsellipse-out}


**说明:**

返回椭圆对象的界限。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 椭圆形以获得境界. |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) \| object | 是 | 矩形,或类似矩形的对象,将椭圆边界存储在其中。如果不给定新的矩形,则会创建。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle), object - 含有椭圆边框的矩形天体。


> 源码：[src/geom/ellipse/GetBounds.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/GetBounds.js#L9)  
引入版本：3.0.0


### GetPoint {#GetPoint-1}

#### \<static> GetPoint(ellipse, position, [out]) {#static-getpointellipse-position-out}


**说明:**

返回一个矢量2物体,其中含有一个点的坐标,该点在椭圆周长上,基于给定角度的正态化到0到1之间,即0.5的值会在椭圆周围180度给出点.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 椭圆形以获得环形点. |
| position | number | 否 | 0到1之间的值,其中0等于0度,0.5等于180度,1等于360度围绕椭圆. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储返回值的矢量2对象。如果不给定新的矢量2对象,将创建该对象。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - A Vector2天体,包含椭圆周围点的坐标.


> 源码：[src/geom/ellipse/GetPoint.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/GetPoint.js#L12)  
引入版本：3.0.0


### GetPoints {#GetPoints-1}

#### \<static> GetPoints(ellipse, quantity, [stepRate], [out]) {#static-getpointsellipse-quantity-steprate-out}


**说明:**

返回含有椭圆周轴周围点坐标的矢量2对象阵列,以给定的数量或stepRate值为基础。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 椭圆形以获得点数. |
| quantity | number | 否 | 返回的点数。 如果一个疟原虫值, 则数量将从 `stepRate` 中得出 。 |
| stepRate | number | 是 | 通过获得椭圆的圆圈来设定数量,并以stepRate来划分. |
| out | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 将 Vector2 对象插入到其中的数组。 如果不提供新的数组, 将会创建 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 椭圆周长周围各点相关的矢量2天体阵列。


> 源码：[src/geom/ellipse/GetPoints.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/GetPoints.js#L12)  
引入版本：3.0.0


### Offset {#Offset-1}

#### \<static> Offset(ellipse, x, y) {#static-offsetellipse-x-y}


**说明:**

以给出的数值来抵消椭圆。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 缩略语:Ellipes (译). |
| x | number | 否 | 水平抵销椭圆的金额。 |
| y | number | 否 | 垂直抵消椭圆的金额。 |


**返回值:** [Phaser.Geom.Ellipse](/api/class/geom-ellipse) - 椭圆形被冲掉.


> 源码：[src/geom/ellipse/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Offset.js#L7)  
引入版本：3.0.0


### OffsetPoint {#OffsetPoint-1}

#### \<static> OffsetPoint(ellipse, vec) {#static-offsetpointellipse-vec}


**说明:**

以矢量2对象的`x`和`y`属性中给出的值来抵消椭圆。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 缩略语: |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 含有以椭圆抵消值的矢量2对象。 |


**返回值:** [Phaser.Geom.Ellipse](/api/class/geom-ellipse) - 椭圆形被冲掉.


> 源码：[src/geom/ellipse/OffsetPoint.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/OffsetPoint.js#L7)  
引入版本：3.0.0


### Random {#Random-1}

#### \<static> Random(ellipse, [out]) {#static-randomellipse-out}


**说明:**

从给定椭圆内的任何位置返回一个统一分布的随机点。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 椭圆形从中随机得到点. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 一个矢量2对象设置随机的`x`和`y`值. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 具有`x`和`y`属性中随机值的矢量2对象.


> 源码：[src/geom/ellipse/Random.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Random.js#L9)  
引入版本：3.0.0


# Phaser.Geom.Intersects {#page-title-2}

### CircleToCircle {#CircleToCircle}

#### \<static> CircleToCircle(circleA, circleB) {#static-circletocirclecirclea-circleb}


**说明:**

检查两圈是否交叉.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circleA | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 第一个检查交叉点的圆圈. |
| circleB | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 第二圆明察交界处. |


**返回值:** boolean - 如果两个圆交错,则`true`,否则则`false`.


> 源码：[src/geom/intersects/CircleToCircle.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/CircleToCircle.js#L9)  
引入版本：3.0.0


### CircleToRectangle {#CircleToRectangle}

#### \<static> CircleToRectangle(circle, rect) {#static-circletorectanglecircle-rect}


**说明:**

检查圆形和矩形之间的交叉点。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆受检. |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 检查的矩形 。 |


**返回值:** boolean - 如果两个物体交叉,则`true`,否则则`false`.


> 源码：[src/geom/intersects/CircleToRectangle.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/CircleToRectangle.js#L7)  
引入版本：3.0.0


### GetCircleToCircle {#GetCircleToCircle}

#### \<static> GetCircleToCircle(circleA, circleB, [out]) {#static-getcircletocirclecirclea-circleb-out}


**说明:**

检查两个圆是否交叉,并将交叉点作为点对象阵列返回.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circleA | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 第一个检查交叉点的圆圈. |
| circleB | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 第二圆明察交界处. |
| out | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 用于存储交叉点的可选的矢量2对象阵列。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 如果物体相交,则带有交点的数组,否则则是一个空数组。


> 源码：[src/geom/intersects/GetCircleToCircle.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetCircleToCircle.js#L11)  
引入版本：3.0.0


### GetCircleToRectangle {#GetCircleToRectangle}

#### \<static> GetCircleToRectangle(circle, rect, [out]) {#static-getcircletorectanglecircle-rect-out}


**说明:**

检查圆形和矩形之间的交叉, 并将交叉点作为点对象的数组返回。 如果形状不相交, 则返回空数组。 如果它们确实相交, 则对矩形的四个边缘进行对照圆形的测试, 并将发现的任何交叉点添加到输出数组中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆受检. |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 检查的矩形 。 |
| out | array | 是 | 存储交汇点的可选数组。 |


**返回值:** array - 如果物体相交,则带有交点的数组,否则则是一个空数组。


> 源码：[src/geom/intersects/GetCircleToRectangle.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetCircleToRectangle.js#L11)  
引入版本：3.0.0


### GetLineToCircle {#GetLineToCircle}

#### \<static> GetLineToCircle(line, circle, [out]) {#static-getlinetocircleline-circle-out}


**说明:**

检查线段和圆之间的交叉,并返回交叉点作为矢量2对象阵列.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 线路段要检查 。 |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆相以验其行. |
| out | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 用于存储交叉点的可选的矢量2对象阵列。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 如果物体相交,则带有交点的数组,否则则是一个空数组。


> 源码：[src/geom/intersects/GetLineToCircle.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetLineToCircle.js#L11)  
引入版本：3.0.0


### GetLineToLine {#GetLineToLine}

#### \<static> GetLineToLine(line1, line2, [isRay], [out]) {#static-getlinetolineline1-line2-isray-out}


**说明:**

检查两条线段之间的交叉,或一条线段和一条线段,如果两条线平行,或不交叉,则返回作为矢量3的交叉点,或`null`.

矢量3的`z`属性包含参数的`t`值(0到1之间的一个标尺),代表着`line1`的交汇点发生多远,可用于排序或比较多个交叉结果,从一组线段找到最接近的交叉点.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| line1 | [Phaser.Geom.Line](/api/class/geom-line) | 否 |  | 第一条线段,或一线,以检查. |
| line2 | [Phaser.Geom.Line](/api/class/geom-line) | 否 |  | 第二行段要检查. |
| isRay | boolean | 是 | false | `line1`是射线还是线段? |
| out | [Phaser.Math.Vector3](/api/class/math-vector3) | 是 |  | 用于存储交叉结果的矢量3。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 矢量3 位于何处 `x` 财务报告和已审计财务报表 `y` 是一个交点坐标, `z` 参数 `t` 沿边值 `line1`,或 ,或 , `null` 如果线不交叉。


> 源码：[src/geom/intersects/GetLineToLine.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetLineToLine.js#L9)  
引入版本：3.50.0


### GetLineToPoints {#GetLineToPoints}

#### \<static> GetLineToPoints(line, points, [isRay], [out]) {#static-getlinetopointsline-points-isray-out}


**说明:**

检查线段和数点之间最接近的交叉点,每对连续的点被转换成线段进行交叉测试。该数组被作为封闭形状处理,这意味着最后一个点被连接回第一点。

如果没有找到交叉点,此函数返回 `null` 。

如果找到交叉点, 返回一个矢量3, 其属性如下:

`x`和`y`组件包含交汇点,`z`组件包含最近的距离.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 |  | 线段,或射线,以检查。如果有射线,则将 `isRay` 参数设置为 `true` 。 |
| points | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> \| Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 否 |  | 一系列要检查的点 。 |
| isRay | boolean | 是 | false | `line`是射线还是线段? |
| out | [Phaser.Math.Vector3](/api/class/math-vector3) | 是 |  | 用于存储交叉结果的矢量3。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 含有交叉结果的矢量3,或`null`.


> 源码：[src/geom/intersects/GetLineToPoints.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetLineToPoints.js#L17)  
引入版本：3.50.0


### GetLineToPolygon {#GetLineToPolygon}

#### \<static> GetLineToPolygon(line, polygons, [isRay], [out]) {#static-getlinetopolygonline-polygons-isray-out}


**说明:**

检查线段与多边形阵列之间最接近的交汇点。

如果没有找到交叉点,此函数返回 `null` 。

如果找到交叉点, 返回一个矢量4, 其属性如下:

`x`和`y`组件包含交汇点. `z`组件包含最近的距离. `w`组件包含特定阵列中触发交汇的多边形索引.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 |  | 线段,或射线,以检查。如果有射线,则将 `isRay` 参数设置为 `true` 。 |
| polygons | [Phaser.Geom.Polygon](/api/class/geom-polygon) \| Array.\<[Phaser.Geom.Polygon](/api/class/geom-polygon)> | 否 |  | 要检查的是一个单一的多边形, 或多边形的数组 。 |
| isRay | boolean | 是 | false | `line`是射线还是线段? |
| out | [Phaser.Math.Vector4](/api/class/math-vector4) | 是 |  | 用于存储交叉结果的矢量4。 |


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 含有交点结果的矢量4,或`null`.


> 源码：[src/geom/intersects/GetLineToPolygon.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetLineToPolygon.js#L14)  
引入版本：3.50.0


### GetLineToRectangle {#GetLineToRectangle}

#### \<static> GetLineToRectangle(line, rect, [out]) {#static-getlinetorectangleline-rect-out}


**说明:**

检查线条与矩形之间的交叉点,然后返回交点作为矢量2阵列.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 检查交叉点的线条 。 |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 检查交叉点的矩形 。 |
| out | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 用于存储交叉点的可选的矢量2对象阵列。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 如果物体相交,则带有交点的数组,否则则是一个空数组。


> 源码：[src/geom/intersects/GetLineToRectangle.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetLineToRectangle.js#L12)  
引入版本：3.0.0


### GetRaysFromPointToPolygon {#GetRaysFromPointToPolygon}

#### \<static> GetRaysFromPointToPolygon(x, y, polygons) {#static-getraysfrompointtopolygonx-y-polygons}


**说明:**

工程射线从给定点射出,到多边形的每个顶点.

如果射线与多边形相交,则交汇点以数组形式返回.

如果没有找到交叉点,返回的数组将是空的 。

每个矢量4的交叉结果具有以下属性: 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量4 向量 向量4 向量

`x`和`y`组件包含交点. `z`组件包含投射射线的角,以弧度表示. `w`组件包含特定阵列中多边形的索引,触发了交点.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | x坐标来投射射射线 |
| y | number | 否 | 以Y坐标投射射射线。 |
| polygons | [Phaser.Geom.Polygon](/api/class/geom-polygon) \| Array.\<[Phaser.Geom.Polygon](/api/class/geom-polygon)> | 否 | 单多边形,或多边形的阵列,以对照射线进行检查. |


**返回值:** Array.\<[Phaser.Math.Vector4](/api/class/math-vector4)> - 包含所有矢量4s中的交叉点的阵列.


> 源码：[src/geom/intersects/GetRaysFromPointToPolygon.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetRaysFromPointToPolygon.js#L40)  
引入版本：3.50.0


### GetRectangleIntersection {#GetRectangleIntersection}

#### \<static> GetRectangleIntersection(rectA, rectB, [output]) {#static-getrectangleintersectionrecta-rectb-output}


**说明:**

检查两个矩形是否交叉,并返回此交叉点的区域为矩形对象.

如果省略了可选的 `output` 参数,则创建并返回新的矩形对象。如果有交叉,则包含交叉区域。如果没有交叉,则将变为空矩形(所有值设定为零)。

如果矩形物体作为`output`传递,并且有交叉点,则会将交叉区数据加载到其中并返回。如果没有交叉点,则不作任何修改。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectA | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第一个矩形物体. |
| rectB | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第二矩形物体. |
| output | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 可选矩形对象。 如果给出, 将加载交叉数据( 如果没有交叉, 则不设任何交叉) 。 否则, 将创建新的矩形对象, 并将其与交叉数据或空( 所有值设为零) 返回, 如果没有交叉点 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 具有交叉数据的矩形对象。


> 源码：[src/geom/intersects/GetRectangleIntersection.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetRectangleIntersection.js#L10)  
引入版本：3.0.0


### GetRectangleToRectangle {#GetRectangleToRectangle}

#### \<static> GetRectangleToRectangle(rectA, rectB, [out]) {#static-getrectangletorectanglerecta-rectb-out}


**说明:**

检查两个矩形是否交叉,并将交叉点作为点对象数组返回.

如果一个矩形的界限在另一个矩形的界限内,则它会交叉另一个矩形。因此,两个矩形被认为是“固体 ” 。一个没有宽度或高度的矩形永远不会交叉另一个矩形。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectA | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第一个检查交叉点的矩形. |
| rectB | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第二个对角检查 |
| out | array | 是 | 存储交汇点的可选数组。 |


**返回值:** array - 如果物体相交,则带有交点的数组,否则则是一个空数组。


> 源码：[src/geom/intersects/GetRectangleToRectangle.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetRectangleToRectangle.js#L11)  
引入版本：3.0.0


### GetRectangleToTriangle {#GetRectangleToTriangle}

#### \<static> GetRectangleToTriangle(rect, triangle, [out]) {#static-getrectangletotrianglerect-triangle-out}


**说明:**

检查矩形和三角形之间的交叉,并返回交汇点作为点对象阵列.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 要测试的矩形对象 。 |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角形对象要测试 。 |
| out | array | 是 | 存储交汇点的可选数组。 |


**返回值:** array - 如果物体相交,则带有交点的数组,否则则是一个空数组。


> 源码：[src/geom/intersects/GetRectangleToTriangle.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetRectangleToTriangle.js#L11)  
引入版本：3.0.0


### GetTriangleToCircle {#GetTriangleToCircle}

#### \<static> GetTriangleToCircle(triangle, circle, [out]) {#static-gettriangletocircletriangle-circle-out}


**说明:**

检查三角和圆是否交叉,然后返回交点作为点对象阵列。

一个圆环如果其中心位于其内部,或者三角的任何一个侧面都与圆环相交,因此,三角和圆环被认为是对交汇点的"固态".

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角区要检查交叉点 。 |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 检查十字路口的圆圈 。 |
| out | array | 是 | 存储交汇点的可选数组。 |


**返回值:** array - 如果物体相交,则带有交点的数组,否则则是一个空数组。


> 源码：[src/geom/intersects/GetTriangleToCircle.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetTriangleToCircle.js#L11)  
引入版本：3.0.0


### GetTriangleToLine {#GetTriangleToLine}

#### \<static> GetTriangleToLine(triangle, line, [out]) {#static-gettriangletolinetriangle-line-out}


**说明:**

检查三角线和线条是否交叉,然后返回交汇点作为点对象阵列。

该线若从内向,内向,或跨越三角的任何一面,则会交叉三角,因此三角被认为是"固".

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角形要检查。 |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 线要检查。 |
| out | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 用于存储交叉点的可选的矢量2对象阵列。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 如果物体相交,则带有交点的数组,否则则是一个空数组。


> 源码：[src/geom/intersects/GetTriangleToLine.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetTriangleToLine.js#L12)  
引入版本：3.0.0


### GetTriangleToTriangle {#GetTriangleToTriangle}

#### \<static> GetTriangleToTriangle(triangleA, triangleB, [out]) {#static-gettriangletotriangletrianglea-triangleb-out}


**说明:**

检查两个三角是否交叉,然后返回交叉点作为点对象阵列。

如果一对三角线相互交织,或者一个三角线的任何点在另一个三角线之内,则一个三角线会相互交织,因此三角线被认为是"固态".

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangleA | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 首批三角区检查交叉点. |
| triangleB | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 第二个三角区检查交叉点. |
| out | array | 是 | 存储交汇点的可选数组。 |


**返回值:** array - 如果物体相交,则带有交点的数组,否则则是一个空数组。


> 源码：[src/geom/intersects/GetTriangleToTriangle.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetTriangleToTriangle.js#L11)  
引入版本：3.0.0


### LineToCircle {#LineToCircle}

#### \<static> LineToCircle(line, circle, [nearest]) {#static-linetocircleline-circle-nearest}


**说明:**

检查线路段与圆之间的交叉点.

依据[Matt DesLauriers](https://github.com/mattdesl/line-circle-collision/blob/master/LICENSE.md)的代码.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 线路段要检查 。 |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆相以验其行. |
| nearest | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 选择矢量2对象。如果给定圆相交的线上最接近的点,则会存储在这个对象中。 |


**返回值:** boolean - 如果两个物体交叉,则`true`,否则则`false`.


> 源码：[src/geom/intersects/LineToCircle.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/LineToCircle.js#L12)  
引入版本：3.0.0


### LineToLine {#LineToLine}

#### \<static> LineToLine(line1, line2, [out]) {#static-linetolineline1-line2-out}


**说明:**

检查两条线是否交叉。 如果两条线完全相同, 则它们将被作为平行处理, 因此不相互连接 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line1 | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 初一行检. |
| line2 | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 复次行中明验. |
| out | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 | 必要时可选的点状对象,用于存储交叉点的坐标。 |


**返回值:** boolean - 如果两条线相交,则`true`,如果给出的话,`out`对象会被人覆盖。否则,`false`。


> 源码：[src/geom/intersects/LineToLine.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/LineToLine.js#L10)  
引入版本：3.0.0


### LineToRectangle {#LineToRectangle}

#### \<static> LineToRectangle(line, rect) {#static-linetorectangleline-rect}


**说明:**

检查线与矩形的交叉点,或类似矩形的物体,具有公共的`x`,`y`,`right`和`bottom`等属性,如Sprite或Body.

在下列情况下,一个交叉点被视为有效:

线条在矩形内部或内部起,或结束. 线段交叉4个矩形边缘中的一个.

3⁄4 ̄ ̧漯B

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 检查交叉点的线条 。 |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) \| object | 否 | 检查交叉点的矩形 。 |


**返回值:** boolean - 如果线和矩形交叉,则`true`,否则则`false`.


> 源码：[src/geom/intersects/LineToRectangle.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/LineToRectangle.js#L7)  
引入版本：3.0.0


### PointToLine {#PointToLine}

#### \<static> PointToLine(point, line, [lineThickness]) {#static-pointtolinepoint-line-linethickness}


**说明:**

检查一个点是否在一线的两个端点之间落下,根据给定的线厚度.

假设线端点是圆形的,而不是方形的.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) \| any | 否 |  | 点,或类似点的物体来检查. |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 |  | 测试交汇点的线段开始. |
| lineThickness | number | 是 | 1 | 线厚度,假设线端点是圆形的. |


**返回值:** boolean - 如果点落到线上,则`true`,否则则`false`.


> 源码：[src/geom/intersects/PointToLine.js#L8](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/PointToLine.js#L8)  
引入版本：3.0.0


### PointToLineSegment {#PointToLineSegment}

#### \<static> PointToLineSegment(point, line) {#static-pointtolinesegmentpoint-line}


**说明:**

检查点是否位于给定的线段上 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 检查交叉点的点。 |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 检查交叉路口的线路段. |


**返回值:** boolean - 如果点位于给定的线段上,则`true`,否则则`false`.


> 源码：[src/geom/intersects/PointToLineSegment.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/PointToLineSegment.js#L9)  
引入版本：3.0.0


### RectangleToRectangle {#RectangleToRectangle}

#### \<static> RectangleToRectangle(rectA, rectB) {#static-rectangletorectanglerecta-rectb}


**说明:**

检查两个矩形交叉处是否为空.

如果一个矩形的界限在另一个矩形的界限内,则它会交叉另一个矩形。因此,两个矩形被认为是“固体 ” 。一个没有宽度或高度的矩形永远不会交叉另一个矩形。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectA | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第一个检查交叉点的矩形. |
| rectB | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第二个对角检查 |


**返回值:** boolean - 如果两个矩形交叉,则`true`,否则则`false`.


> 源码：[src/geom/intersects/RectangleToRectangle.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/RectangleToRectangle.js#L7)  
引入版本：3.0.0


### RectangleToTriangle {#RectangleToTriangle}

#### \<static> RectangleToTriangle(rect, triangle) {#static-rectangletotrianglerect-triangle}


**说明:**

检查矩形和三角形之间的交叉点。

测试是在成本增加的多个阶段进行的,首先,将两个形状的边框作比较,以便快速提前退出。如果它们重叠,测试检查是否有任何三角顶点位于矩形内部,然后三角形的任何边缘是否交叉任何矩形边缘,最后是否有矩形的角位于三角形内部.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形来试. |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角去试. |


**返回值:** boolean - 如果物体交叉, 值为 `true`; 否则为 `false` 。


> 源码：[src/geom/intersects/RectangleToTriangle.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/RectangleToTriangle.js#L12)  
引入版本：3.0.0


### RectangleToValues {#RectangleToValues}

#### \<static> RectangleToValues(rect, left, right, top, bottom, [tolerance]) {#static-rectangletovaluesrect-left-right-top-bottom-tolerance}


**说明:**

检查矩形是否与由明确的左、右、上和下边界值定义的区域相交。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 |  | 检查交叉点的矩形 。 |
| left | number | 否 |  | 区域左边缘的x坐标以检查是否对应. |
| right | number | 否 |  | 区域右边缘的x坐标来检查对比. |
| top | number | 否 |  | 区域顶端的y坐标来检查对比. |
| bottom | number | 否 |  | 区域底缘的y坐标以检查对照. |
| tolerance | number | 是 | 0 | 允许在计算中允许的容忍,以像素表示. |


**返回值:** boolean - 如果有交叉点, 返回真实值 。


> 源码：[src/geom/intersects/RectangleToValues.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/RectangleToValues.js#L7)  
引入版本：3.0.0


### TriangleToCircle {#TriangleToCircle}

#### \<static> TriangleToCircle(triangle, circle) {#static-triangletocircletriangle-circle}


**说明:**

检查三角和圆是否交汇。

一个圆环如果其中心位于其内部,或者三角的任何一个侧面都与圆环相交,因此,三角和圆环被认为是对交汇点的"固态".

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角区要检查交叉点 。 |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 检查十字路口的圆圈 。 |


**返回值:** boolean - `true` 如果三角和三角 `Circle` 交叉,否则 `false`.


> 源码：[src/geom/intersects/TriangleToCircle.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/TriangleToCircle.js#L10)  
引入版本：3.0.0


### TriangleToLine {#TriangleToLine}

#### \<static> TriangleToLine(triangle, line) {#static-triangletolinetriangle-line}


**说明:**

检查三角线和线是否交叉。

该线若从内向,内向,或跨越三角的任何一面,则会交叉三角,因此三角被认为是"固".

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角形要检查。 |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 线要检查。 |


**返回值:** boolean - 如果三角线和线交汇,则`true`,否则则`false`.


> 源码：[src/geom/intersects/TriangleToLine.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/TriangleToLine.js#L9)  
引入版本：3.0.0


### TriangleToTriangle {#TriangleToTriangle}

#### \<static> TriangleToTriangle(triangleA, triangleB) {#static-triangletotriangletrianglea-triangleb}


**说明:**

检查两个三角交叉处.

如果一对三角线相互交织,或者一个三角线的任何点在另一个三角线之内,则一个三角线会相互交织,因此三角线被认为是"固态".

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangleA | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 首批三角区检查交叉点. |
| triangleB | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 第二个三角区检查交叉点. |


**返回值:** boolean - 如果三角交错,则`true`,否则则`false`.


> 源码：[src/geom/intersects/TriangleToTriangle.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/TriangleToTriangle.js#L11)  
引入版本：3.0.0


# Phaser.Geom.Line {#page-title-3}

### Angle {#Angle}

#### \<static> Angle(line) {#static-angleline}


**说明:**

以弧度计算线角.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 计算角度的线条 。 |


**返回值:** number - 线的角,用弧度表示.


> 源码：[src/geom/line/Angle.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Angle.js#L7)  
引入版本：3.0.0


### BresenhamPoints {#BresenhamPoints}

#### \<static> BresenhamPoints(line, [stepRate], [results]) {#static-bresenhampointsline-steprate-results}


**说明:**

使用 Bresenham 的线程算法, 这将返回给定线上所有坐标的阵列 。

电话 `start` 财务报告和已审计财务报表 `end` 点数在此运行前随算法对整数起作用而四舍五入。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 |  | 线条. |
| stepRate | number | 是 | 1 | 控制沿线对点进行取样的密度。一个值为 1 返回每个整数坐标;一个值为 2 返回其他坐标,等等。 |
| results | Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 是 |  | 将生成的坐标推向的可选数组 。 |


**返回值:** Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> - 线上坐标阵列.


> 源码：[src/geom/line/BresenhamPoints.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/BresenhamPoints.js#L7)  
引入版本：3.0.0


### CenterOn {#CenterOn}

#### \<static> CenterOn(line, x, y) {#static-centeronline-x-y}


**说明:**

将一条线放在指定坐标上

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 线至中心. |
| x | number | 否 | 水平坐标使线中心开. |
| y | number | 否 | 垂直坐标以中线为中心. |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 中行经.


> 源码：[src/geom/line/CenterOn.js#L8](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/CenterOn.js#L8)  
引入版本：3.0.0


### Clone {#Clone-2}

#### \<static> Clone(source) {#static-clonesource-2}


**说明:**

切除给定的线条。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 克隆的源线 。 |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 克隆线.


> 源码：[src/geom/line/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Clone.js#L9)  
引入版本：3.0.0


### CopyFrom {#CopyFrom-2}

#### \<static> CopyFrom(source, dest) {#static-copyfromsource-dest-2}


**说明:**

复制一行的值到目的地行 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 复制这些值的源行 。 |
| dest | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 复制值到的目标行 。 |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 目的地线


> 源码：[src/geom/line/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/CopyFrom.js#L7)  
引入版本：3.0.0


### Equals {#Equals-2}

#### \<static> Equals(line, toCompare) {#static-equalsline-tocompare}


**说明:**

比较两行的严格平等。 如果两行的起始点和终点点精确地协调所有匹配,则认为两行相等 : `x1`, `y1`, `x2`,和 `y2`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 初一行比拟. |
| toCompare | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 第二行比较. |


**返回值:** boolean - 如果两条线路的起始点和终点坐标完全相同,则`true`,否则则`false`.


> 源码：[src/geom/line/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Equals.js#L7)  
引入版本：3.0.0


### Extend {#Extend}

#### \<static> Extend(line, left, [right]) {#static-extendline-left-right}


**说明:**

以给定的金额延长一行的起始点和终点。

数值可以是正数,也可以是负数。正值会增加线的长度,而负值会减少线的长度。

如果未提供`right`值,则将平均延长线的长度。

传递一个0的值,使起始点或终点保持不变。

`left`值从起点(x1,y1)沿线方向向外延伸,`right`值从终点(x2,y2)向外延伸.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 线性实例要扩展 。 |
| left | number | 否 | 将线条的起始时间延长的金额 。 |
| right | number | 是 | 将线尾延伸的金额。 如果不给出, 则设定为 `left` 值 。 |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 修改的 Line 实例 。


> 源码：[src/geom/line/Extend.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Extend.js#L9)  
引入版本：3.16.0


### GetEasedPoints {#GetEasedPoints}

#### \<static> GetEasedPoints(line, ease, quantity, [collinearThreshold], [easeParams]) {#static-geteasedpointsline-ease-quantity-collinearthreshold-easeparams}


**说明:**

返回 `quantity` 点数组,每个点从给定的线上取出,按照指定的易操作进行空格。

```javascript
const line = new Phaser.Geom.Line(100, 300, 700, 300);
const points = Phaser.Geom.Line.GetEasedPoints(line, 'sine.out', 32)
```

在上述例子中,`points`阵列将包含32个点,分布在`line`的长度,每个点的位置由`Sine.out`的易性函数决定.

您可以选择提供连线阈值。 在这种情况下, 所产生的点会相互检查, 如果它们相距为 `< collinearThreshold` , 则它们会从结果中被丢弃。 这有助于避免在线条最远处的很多集群点, 并带有像Quartic 这样的严格包装的便捷。 将设定的值留为零来跳过此检查 。

注意,如果您提供了串联阈值,所产生的阵列可能并不总是包含`quantity`点.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 |  | 线条对象. |
| ease | string \| function | 否 |  | 使用方便。 这可以是 EaseMap 的字符串, 也可以是自定义函数 。 |
| quantity | number | 否 |  | 返回的点数。 请注意, 如果您提供了 `collinearThreshold`, 所产生的数组可能并不总是包含这个点数 。 |
| collinearThreshold | number | 是 | 0 | 一个可选的阈值。 最终阵列被缩小, 使每个点至少被隔开这个距离。 这有助于减少在吵闹的易行度中的集群 。 |
| easeParams | Array.\<number> | 是 |  | 随易的可选的易解参数组. |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 包含线上各点坐标的数组数组数组数数组数组数. Vector2s.


> 源码：[src/geom/line/GetEasedPoints.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/GetEasedPoints.js#L11)  
引入版本：3.23.0


### GetMidPoint {#GetMidPoint}

#### \<static> GetMidPoint(line, [out]) {#static-getmidpointline-out}


**说明:**

获取给定线的中点 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 取中点的线. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 可选的矢量2对象,将中点存储在其中 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 中线.


> 源码：[src/geom/line/GetMidPoint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/GetMidPoint.js#L9)  
引入版本：3.0.0


### GetNearestPoint {#GetNearestPoint}

#### \<static> GetNearestPoint(line, vec, [out]) {#static-getnearestpointline-vec-out}


**说明:**

将指定线段定义的无限线上最接近点到指定点。请注意,返回点将投射到全线上,而不是夹在段端点上。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 线以获得最近的点。 |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 矢量2号可以得到最接近的点. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 选择矢量2对象,用于存储线上最接近点的坐标. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 线上最近的点.


> 源码：[src/geom/line/GetNearestPoint.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/GetNearestPoint.js#L10)  
引入版本：3.16.0


### GetNormal {#GetNormal}

#### \<static> GetNormal(line, [out]) {#static-getnormalline-out}


**说明:**

计算给定行的正常值 。

线的正常是从它中指向垂直的矢量.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 计算正常的线条 。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 可选的矢量2对象存储正常的内置. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 线的正常。


> 源码：[src/geom/line/GetNormal.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/GetNormal.js#L11)  
引入版本：3.0.0


### GetPoint {#GetPoint-2}

#### \<static> GetPoint(line, position, [out]) {#static-getpointline-position-out}


**说明:**

获得一个点的线,这个线的长度是一定的百分数.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 线条. |
| position | number | 否 | 0到1之间的值,其中0为起始,0.5为中间,1为终点. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 可选的矢量2对象存储线上点的坐标. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 线上点.


> 源码：[src/geom/line/GetPoint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/GetPoint.js#L9)  
引入版本：3.0.0


### GetPoints {#GetPoints-2}

#### \<static> GetPoints(line, quantity, [stepRate], [out]) {#static-getpointsline-quantity-steprate-out}


**说明:**

从第一个终点(x1,y1)开始,沿着一条线获得若干平方位点,最后一个终点(x2,y2)不包含在返回的点中.

提供`quantity`,以获得沿线精确的点数.

提供a `stepRate` 以确保线上每个点之间的特定距离。设置 `quantity` 改为: `0` 提供时 `stepRate`.

另见`GetEasedPoints`,以按照易性类型或输入函数将点数分布到横线的方法.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 线条. |
| quantity | number | 否 | 线上要放置的点数。 设定为 `0` , 代之以 `stepRate` 。 |
| stepRate | number | 是 | 线上每个点之间的距离。 设定时, `quantity` 将计算为线长除以此值; `quantity` 将被设定为 `0` 。 |
| out | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 用于存储线上各点坐标的可选的矢量2对象数组。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 包含线上各点坐标的矢量2天体阵列。


> 源码：[src/geom/line/GetPoints.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/GetPoints.js#L10)  
引入版本：3.0.0


### GetShortestDistance {#GetShortestDistance}

#### \<static> GetShortestDistance(line, point) {#static-getshortestdistanceline-point}


**说明:**

计算从指定线对象的两个端点定义的无限线到给定点的最短(双直线)距离。如果线的长度为零(两个端点都相同),此函数返回 `false`。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 取其远近之线. |
| point | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 得到最短距离的点。 |


**返回值:** boolean, number - 从线到点的最短的垂直距离,或者如果线有零长度的`false`.


> 源码：[src/geom/line/GetShortestDistance.js#L8](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/GetShortestDistance.js#L8)  
引入版本：3.16.0


### Height {#Height}

#### \<static> Height(line) {#static-heightline}


**说明:**

计算给定线的高度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 计算高度的线条 。 |


**返回值:** number - 线的高度。


> 源码：[src/geom/line/Height.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Height.js#L7)  
引入版本：3.0.0


### Length {#Length}

#### \<static> Length(line) {#static-lengthline}


**说明:**

计算给定行的长度 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 计算长度的线条 。 |


**返回值:** number - 线的长度.


> 源码：[src/geom/line/Length.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Length.js#L7)  
引入版本：3.0.0


### NormalAngle {#NormalAngle}

#### \<static> NormalAngle(line) {#static-normalangleline}


**说明:**

以弧度获取给定线的正常角度.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 计算正常角度的线条。 |


**返回值:** number - 线的正常角度用弧度表示.


> 源码：[src/geom/line/NormalAngle.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/NormalAngle.js#L11)  
引入版本：3.0.0


### NormalX {#NormalX}

#### \<static> NormalX(line) {#static-normalxline}


**说明:**

返回给定行的正常矢量的x组件。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 线条对象从中获取正常值 。 |


**返回值:** number - 线路正常矢量的x组件.


> 源码：[src/geom/line/NormalX.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/NormalX.js#L10)  
引入版本：3.0.0


### NormalY {#NormalY}

#### \<static> NormalY(line) {#static-normalyline}


**说明:**

给定线的正常的Y值。线的正常是向量,它从中指向垂直的。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 计算正常的线条 。 |


**返回值:** number - 线的正常值的Y值 。


> 源码：[src/geom/line/NormalY.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/NormalY.js#L10)  
引入版本：3.0.0


### Offset {#Offset-2}

#### \<static> Offset(line, x, y) {#static-offsetline-x-y}


**说明:**

将给定线的端点都通过指定的水平和垂直量翻译,在保留长度和角度的同时,有效将线向2D空间中的新位置移动.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 拟冲抵的线条. |
| x | number | 否 | 水平偏移以加于行. |
| y | number | 否 | 垂直偏移以添加到线上。 |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 修改的行对象,两个端点都由给定的偏移移动.


> 源码：[src/geom/line/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Offset.js#L7)  
引入版本：3.0.0


### PerpSlope {#PerpSlope}

#### \<static> PerpSlope(line) {#static-perpslopeline}


**说明:**

计算给定线的垂直坡度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 计算垂直坡度的线条 。 |


**返回值:** number - 线条的垂直坡度.


> 源码：[src/geom/line/PerpSlope.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/PerpSlope.js#L7)  
引入版本：3.0.0


### Random {#Random-2}

#### \<static> Random(line, [out]) {#static-randomline-out}


**说明:**

返回给定行上的随机点。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 计算随机点的线条 。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 需要修改的矢量2的例子。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 存储在矢量2中的线上的随机点.


> 源码：[src/geom/line/Random.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Random.js#L9)  
引入版本：3.0.0


### ReflectAngle {#ReflectAngle}

#### \<static> ReflectAngle(lineA, lineB) {#static-reflectanglelinea-lineb}


**说明:**

计算由B线代表的A线表面的反射角。这是基于事件角(A线)和B线表面正常的向外角。结果为弧度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| lineA | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 使用事件角度的事件线. |
| lineB | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 表面线,用来计算反射的正常角度. |


**返回值:** number - A线在B线表面的反射角,以弧度表示.


> 源码：[src/geom/line/ReflectAngle.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/ReflectAngle.js#L10)  
引入版本：3.0.0


### Rotate {#Rotate}

#### \<static> Rotate(line, angle) {#static-rotateline-angle}


**说明:**

以弧度的给定角度绕其中点旋转一条线。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 轮回的线条。 |
| angle | number | 否 | 弧度旋转的角度. |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 旋转行.


> 源码：[src/geom/line/Rotate.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Rotate.js#L9)  
引入版本：3.0.0


### RotateAroundPoint {#RotateAroundPoint}

#### \<static> RotateAroundPoint(line, point, angle) {#static-rotatearoundpointline-point-angle}


**说明:**

以弧度以给定角度绕一个点旋转一条线 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 轮回的线条。 |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 线条旋转的点. |
| angle | number | 否 | 弧度旋转的角度. |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 旋转行.


> 源码：[src/geom/line/RotateAroundPoint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/RotateAroundPoint.js#L9)  
引入版本：3.0.0


### RotateAroundXY {#RotateAroundXY}

#### \<static> RotateAroundXY(line, x, y, angle) {#static-rotatearoundxyline-x-y-angle}


**说明:**

以弧度以给定角度绕给定坐标旋转一条线 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 轮回的线条。 |
| x | number | 否 | 横向坐标来旋转线条绕行. |
| y | number | 否 | 垂直坐标来旋转线条。 |
| angle | number | 否 | 弧度旋转的角度. |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 旋转行.


> 源码：[src/geom/line/RotateAroundXY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/RotateAroundXY.js#L7)  
引入版本：3.0.0


### SetToAngle {#SetToAngle}

#### \<static> SetToAngle(line, x, y, angle, length) {#static-settoangleline-x-y-angle-length}


**说明:**

设置一条线到给定的位置、角度和长度。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 线要设置。 |
| x | number | 否 | 线的横向起始位置. |
| y | number | 否 | 线的垂直起始位置 。 |
| angle | number | 否 | 线角用弧度表示. |
| length | number | 否 | 线的长度. |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 更新的行号.


> 源码：[src/geom/line/SetToAngle.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/SetToAngle.js#L7)  
引入版本：3.0.0


### Slope {#Slope}

#### \<static> Slope(line) {#static-slopeline}


**说明:**

计算给定线的斜率。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 计算斜坡的线条. |


**返回值:** number - 线的坡度.


> 源码：[src/geom/line/Slope.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Slope.js#L7)  
引入版本：3.0.0


### Width {#Width}

#### \<static> Width(line) {#static-widthline}


**说明:**

计算给定线的宽度,定义为其两个终点的x坐标之间的绝对差(`x1` 财务报告和已审计财务报表 `x2`。这代表线的横向范围,而不是其几何长度。要获得线的真实长度,请使用 `Phaser.Geom.Line.Length` 换成是的

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 计算宽度的线条 。 |


**返回值:** number - 线宽度,即其x1和x2坐标的绝对差.


> 源码：[src/geom/line/Width.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Width.js#L7)  
引入版本：3.0.0


# Phaser.Geom.Polygon {#page-title-4}

### Clone {#Clone-3}

#### \<static> Clone(polygon) {#static-clonepolygon}


**说明:**

创建新多边形, 即指定的多边形的副本

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| polygon | [Phaser.Geom.Polygon](/api/class/geom-polygon) | 否 | 创建克隆的多边形 |


**返回值:** [Phaser.Geom.Polygon](/api/class/geom-polygon) - 基于相同点的从指定的多边形中复制出来的新单独的多边形.


> 源码：[src/geom/polygon/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Clone.js#L9)  
引入版本：3.0.0


### Contains {#Contains-2}

#### \<static> Contains(polygon, x, y) {#static-containspolygon-x-y}


**说明:**

检查一个点是否在多边形的界限内。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| polygon | [Phaser.Geom.Polygon](/api/class/geom-polygon) | 否 | 检查多边形。 |
| x | number | 否 | 检查点的X坐标 |
| y | number | 否 | 检查点的Y坐标 |


**返回值:** boolean - 如果点在多边形的界限内,则`true`,否则则`false`.


> 源码：[src/geom/polygon/Contains.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Contains.js#L10)  
引入版本：3.0.0


### ContainsPoint {#ContainsPoint-2}

#### \<static> ContainsPoint(polygon, vec) {#static-containspointpolygon-vec}


**说明:**

检查给定的点对多边形,看点是否位于它的顶点内.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| polygon | [Phaser.Geom.Polygon](/api/class/geom-polygon) | 否 | 检查多边形。 |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 矢量2点检查是否在多边形内. |


**返回值:** boolean - 如果点在多边形内,则`true`,否则则`false`.


> 源码：[src/geom/polygon/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/ContainsPoint.js#L9)  
引入版本：3.0.0


### Earcut {#Earcut}

#### \<static> Earcut(data, [holeIndices], [dimensions]) {#static-earcutdata-holeindices-dimensions}


**说明:**

本模块执行一个修改后的耳切算法,通过z-顺序曲线散列进行优化,并扩展至处理孔,扭曲的多边形,变质和自交路段,其方式不能保证三角化的正确性,而是试图总是为实用数据产生可接受的结果.

Example:

```javascript
const triangles = Phaser.Geom.Polygon.Earcut([10,0, 0,50, 60,60, 70,10]); // returns [1,0,3, 3,2,1]
```

由此形成的数组中每组三个顶点指数形成一个三角形.

```javascript
// triangulating a polygon with a hole
earcut([0,0, 100,0, 100,100, 0,100,  20,20, 80,20, 80,80, 20,80], [4]);
// [3,0,4, 5,4,0, 3,4,7, 5,0,1, 2,3,7, 6,5,1, 2,7,6, 6,1,2]

// triangulating a polygon with 3d coords
earcut([10,0,1, 0,50,2, 60,60,3, 70,10,4], null, 3);
// [1,0,3, 3,2,1]
```

如果通过一个单一顶点作为洞,厄尔克特把它当作施泰纳点.

如果输入是一个多维阵列(例如GeoJSON Polygon),您可以将其转换成Earcut以 `Phaser.Geom.Polygon.Earcut.flatten`来期望的格式:

```javascript
var data = earcut.flatten(geojson.geometry.coordinates);
var triangles = earcut(data.vertices, data.holes, data.dimensions);
```

在得到三角测量后,您可以用`Phaser.Geom.Polygon.Earcut.deviation`验证其正确性:

```javascript
var deviation = earcut.deviation(vertices, holes, dimensions, triangles);
```

返回三角形总面积与输入多边形面积的相对差. 0表示三角形完全正确.

更多信息见[https://github.com/mapbox/earcut](https://github.com/mapbox/earcut)

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| data | Array.\<number> | 否 |  | 一个平坦的顶点坐标阵列,如\[x0,y0,x1,y1,x2,y2,.\] |
| holeIndices | Array.\<number> | 是 |  | 如果有孔指数阵列(例如12顶点输入的[5, 8]),则指一个孔有顶点5-7,另一个孔有8-11。 |
| dimensions | number | 是 | 2 | 输入阵列中每个顶点的坐标数(2默认). |


**返回值:** Array.\<number> - 三角数据阵列.


> 源码：[src/geom/polygon/Earcut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Earcut.js#L7)  
引入版本：3.50.0


### GetAABB {#GetAABB}

#### \<static> GetAABB(polygon, [out]) {#static-getaabbpolygon-out}


**说明:**

计算多边形的边界 AABB 矩形。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| polygon | [Phaser.Geom.Polygon](/api/class/geom-polygon) | 否 | 应计算的多边形 。 |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) \| object | 是 | 矩形或对象具有x、y、宽度和高度属性以存储结果。可选。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle), object - 由此形成的矩形或物体,随多边形的ABB的位置和维度而传递.


> 源码：[src/geom/polygon/GetAABB.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/GetAABB.js#L9)  
引入版本：3.0.0


### GetNumberArray {#GetNumberArray}

#### \<static> GetNumberArray(polygon, [output]) {#static-getnumberarraypolygon-output}


**说明:**

将一个多边形的所有点存储到一个按照顺序\[x,y,x,y,x\]排列的平整数组中,即多边形的每个点,按照定义的顺序,对应该点的X和Y坐标的后产生的数组的两个元素.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| polygon | [Phaser.Geom.Polygon](/api/class/geom-polygon) | 否 | 指向导出的多边形。 |
| output | array \| Array.\<number> | 是 | 附加点的坐标的阵列。 |


**返回值:** array, Array.\<number> - 修改后的 `output` 阵列, 或者如果没有给出新的阵列 。


> 源码：[src/geom/polygon/GetNumberArray.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/GetNumberArray.js#L9)  
引入版本：3.0.0


### GetPoints {#GetPoints-3}

#### \<static> GetPoints(polygon, quantity, [stepRate], [output]) {#static-getpointspolygon-quantity-steprate-output}


**说明:**

返回含有多边形周边各点坐标的矢量2对象阵列,其数值以给定的数量或stepRate值为准。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| polygon | [Phaser.Geom.Polygon](/api/class/geom-polygon) | 否 | 得到点数的多边形。 |
| quantity | number | 否 | 返回的点数。 如果一个疟原虫值, 则数量将从 `stepRate` 中得出 。 |
| stepRate | number | 是 | 以stepRate来划分多边形的周界,设定数量。 |
| output | array | 是 | 插入点数组。 如果不提供新的数组, 将创建 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 与多边形周边各点有关的一系列矢量2物体。


> 源码：[src/geom/polygon/GetPoints.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/GetPoints.js#L11)  
引入版本：3.12.0


### Perimeter {#Perimeter}

#### \<static> Perimeter(polygon) {#static-perimeterpolygon}


**说明:**

以所有边缘的长度相交返回给定多边形的周界。多边形被作为闭合物处理,因此,在最后一点和第一点之间的边缘被包括在总数中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| polygon | [Phaser.Geom.Polygon](/api/class/geom-polygon) | 否 | 多边形可以进入周边 |


**返回值:** number - 多边形的周边.


> 源码：[src/geom/polygon/Perimeter.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Perimeter.js#L10)  
引入版本：3.12.0


### Reverse {#Reverse}

#### \<static> Reverse(polygon) {#static-reversepolygon}


**说明:**

反转多边形点的顺序。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| polygon | [Phaser.Geom.Polygon](/api/class/geom-polygon) | 否 | 修改的多边形 。 |


**返回值:** [Phaser.Geom.Polygon](/api/class/geom-polygon) - 修改后的多边形.


> 源码：[src/geom/polygon/Reverse.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Reverse.js#L7)  
引入版本：3.0.0


### Simplify {#Simplify}

#### \<static> Simplify(polygon, [tolerance], [highestQuality]) {#static-simplifypolygon-tolerance-highestquality}


**说明:**

取一个多边形对象,并通过道格拉斯-佩克和拉达尔远程算法的组合来运行来简化点数。简化在保留多边形形状的同时会大幅降低点数,在处理时会给予巨大的性能助推,同时也会减少视觉噪声。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| polygon | [Phaser.Geom.Polygon](/api/class/geom-polygon) | 否 |  | 要简化的多边形。 多边形将按原位修改并返回。 |
| tolerance | number | 是 | 1 | 影响简化的量(与点坐标相同的度量). |
| highestQuality | boolean | 是 | false | 不包括基于远程的预处理步骤,该步骤导致最高质量简化,但运行速度却慢了~10-20倍. |


**返回值:** [Phaser.Geom.Polygon](/api/class/geom-polygon) - 输入多边形。


> 源码：[src/geom/polygon/Simplify.js#L160](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Simplify.js#L160)  
引入版本：3.50.0


### Smooth {#Smooth}

#### \<static> Smooth(polygon) {#static-smoothpolygon}


**说明:**

取一个多边形对象,并在其点上应用Chaikin的平滑算法.

Chaikin的算法是一种切角技术,它用沿边的两个新点位置来取代两个连续点之间的每个边,从而产生一个更平滑的曲线。算法的每次迭代都会增加多边形中的点数总数。原来的第一点和最后一个点被保留下来,而所有的中间点则被85%和15%的新点所取代。

多边形在位置上被修改,并返回相同的多边形对象。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| polygon | [Phaser.Geom.Polygon](/api/class/geom-polygon) | 否 | 要平滑的多边形。 多边形将在原位修改后返回 。 |


**返回值:** [Phaser.Geom.Polygon](/api/class/geom-polygon) - 输入多边形。


> 源码：[src/geom/polygon/Smooth.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Smooth.js#L19)  
引入版本：3.13.0


### Translate {#Translate}

#### \<static> Translate(polygon, x, y) {#static-translatepolygon-x-y}


**说明:**

翻译给定的多边形的点。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| polygon | [Phaser.Geom.Polygon](/api/class/geom-polygon) | 否 | 修改的多边形 。 |
| x | number | 否 | 水平翻译点的金额。 |
| y | number | 否 | 垂直翻译点数的金额 。 |


**返回值:** [Phaser.Geom.Polygon](/api/class/geom-polygon) - 修改后的多边形.


> 源码：[src/geom/polygon/Translate.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Translate.js#L7)  
引入版本：3.50.0


# Phaser.Geom.Rectangle {#page-title-5}

### Area {#Area-2}

#### \<static> Area(rect) {#static-arearect}


**说明:**

计算给定矩形对象的区域。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 用于计算区域范围的矩形。 |


**返回值:** number - 矩形天体的区域。


> 源码：[src/geom/rectangle/Area.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Area.js#L7)  
引入版本：3.0.0


### Ceil {#Ceil}

#### \<static> Ceil(rect) {#static-ceilrect}


**说明:**

绕一个矩形的位置,其最小整数大于或等于每个电流坐标。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形要调整. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 调整后的矩形.


> 源码：[src/geom/rectangle/Ceil.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Ceil.js#L7)  
引入版本：3.0.0


### CeilAll {#CeilAll}

#### \<static> CeilAll(rect) {#static-ceilallrect}


**说明:**

圆形矩形的位置和大小,以大于或等于每个相应值的最小整数为限。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形要修改 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 修改后的矩形.


> 源码：[src/geom/rectangle/CeilAll.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/CeilAll.js#L7)  
引入版本：3.0.0


### CenterOn {#CenterOn-1}

#### \<static> CenterOn(rect, x, y) {#static-centeronrect-x-y}


**说明:**

移动矩形左上角,使其中心位于给定坐标。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形要以圆为中心. |
| x | number | 否 | 矩形中心X坐标. |
| y | number | 否 | 矩形中心Y坐标. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 中心矩形(原变种).


> 源码：[src/geom/rectangle/CenterOn.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/CenterOn.js#L7)  
引入版本：3.0.0


### Clone {#Clone-4}

#### \<static> Clone(source) {#static-clonesource-3}


**说明:**

创建与给定的矩形相同的新矩形。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形变克隆. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 新建的矩形,它与给定的矩形是分开的.


> 源码：[src/geom/rectangle/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Clone.js#L9)  
引入版本：3.0.0


### Contains {#Contains-3}

#### \<static> Contains(rect, x, y) {#static-containsrect-x-y}


**说明:**

检查某个点是否位于矩形的界限内。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形要检查。 |
| x | number | 否 | 检查点的X坐标 |
| y | number | 否 | 检查点的Y坐标 |


**返回值:** boolean - 如果点在矩形的界限内,则`true`,否则则`false`.


> 源码：[src/geom/rectangle/Contains.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Contains.js#L7)  
引入版本：3.0.0


### ContainsPoint {#ContainsPoint-3}

#### \<static> ContainsPoint(rect, vec) {#static-containspointrect-vec}


**说明:**

确定指定的点是否包含在这个矩形对象定义的矩形区域之内。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形对象. |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 矢量2对象检查坐标 。 |


**返回值:** boolean - 如果矩形对象包含指定的点,则真实值,否则为虚假值。


> 源码：[src/geom/rectangle/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/ContainsPoint.js#L9)  
引入版本：3.0.0


### ContainsRect {#ContainsRect-2}

#### \<static> ContainsRect(rectA, rectB) {#static-containsrectrecta-rectb}


**说明:**

如果一个矩形完全包含另一个矩形。 如果一个矩形的边缘( 左、 右、 上、 下) 全部严格位于外矩形的界限内, 则该矩形被认为完全被控制。 仅触摸或重叠的矩形并不被视为被控制 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectA | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 外矩作为容器进行试验. |
| rectB | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 内侧矩形测试rectA内部的全封闭. |


**返回值:** boolean - 只有rectA完全包含rectB时才算属实.


> 源码：[src/geom/rectangle/ContainsRect.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/ContainsRect.js#L7)  
引入版本：3.0.0


### CopyFrom {#CopyFrom-3}

#### \<static> CopyFrom(source, dest) {#static-copyfromsource-dest-3}


**说明:**

将一个矩形的值复制到一个目的地矩形。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 源矩形复制这些值。 |
| dest | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 目标矩形将数值复制到 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 目的地矩形.


> 源码：[src/geom/rectangle/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/CopyFrom.js#L7)  
引入版本：3.0.0


### Decompose {#Decompose}

#### \<static> Decompose(rect, [out]) {#static-decomposerect-out}


**说明:**

创建矩形四个角的平面 `{x, y}` 点对象阵列, 顺序为: 左上右下右下左下。 如果提供了输出数组, 每个点对象将被推到它的末尾, 否则将创建并返回一个新的数组 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 要分解的矩形对象 。 |
| out | array | 是 | 如果提供,每个点都会被添加到这个数组中. |


**返回值:** array - 将返回您指定的数组或包含矩形点的新数组。


> 源码：[src/geom/rectangle/Decompose.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Decompose.js#L7)  
引入版本：3.0.0


### Equals {#Equals-3}

#### \<static> Equals(rect, toCompare) {#static-equalsrect-tocompare}


**说明:**

比较 `x`, `y`, `width` 财务报告和已审计财务报表 `height` 返回 `true` 只有所有四个值都完全使用严格的平等。此函数并不认为具有相同区域但不同位置或维度的矩形是平等的。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 初对矩相类. |
| toCompare | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 与第二矩相对. |


**返回值:** boolean - 如果矩形的属性是精确匹配的,则`true`,否则`false`.


> 源码：[src/geom/rectangle/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Equals.js#L7)  
引入版本：3.0.0


### FitInside {#FitInside}

#### \<static> FitInside(target, source) {#static-fitinsidetarget-source}


**说明:**

调整目标矩,改变其宽度,高度和位置,使其适合源矩区域内部,同时保持其原宽比.

与`FitOutside`函数不同,源区内部可能有一些空间没有覆盖.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 目标矩形以调整. |
| source | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 源矩以包围目标. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 修改的目标矩形实例 。


> 源码：[src/geom/rectangle/FitInside.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/FitInside.js#L9)  
引入版本：3.0.0


### FitOutside {#FitOutside}

#### \<static> FitOutside(target, source) {#static-fitoutsidetarget-source}


**说明:**

调整目标矩,改变其宽度,高度和位置,使其完全覆盖源矩的区域,同时保持其原宽比.

与`FitInside`函数不同,目标矩形可能比源头更远的延伸.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 目标矩形以调整. |
| source | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 源矩形可以将目标包入. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 修改的目标矩形实例 。


> 源码：[src/geom/rectangle/FitOutside.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/FitOutside.js#L9)  
引入版本：3.0.0


### Floor {#Floor}

#### \<static> Floor(rect) {#static-floorrect}


**说明:**

向下(地板)圆,向下(底),向下(底),向下(底),向下(底),向下),向下(底),向下(底),向下),向下(底),向下(底),向下),向下(底),向下(底),向下),向下(底),向下),向下(底),向下(底),向下),向下(底),向下(底),向下(底),向下),向下(底),向下(底),向下(底),向下(底),向下(底),向下(底),向下(底),向下(底),向下(底),向下(底),向下(底),向下,向下(底),向下(底),向下,向下),向下(底,向下),向下(底),向上),向上(底),向下(底),向下),(底,向上(底),向下),(底),(底,(底),向下),向下(底,向下),向下(底(底),(底),向下),向下),(底,(底,(底,(底),(底),(底),(底),(底,(底),(底),(底)/底),(底),(底),(底(底)和(底),(底),(底),(底),向上),(底),(底),(底),(底),(底),向(底),(底),(底),(底),(底),(底),(底),(底),(底),(底),

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 左上方的X和Y坐标 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 坐标为底座的矩形传递到此函数上。


> 源码：[src/geom/rectangle/Floor.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Floor.js#L7)  
引入版本：3.0.0


### FloorAll {#FloorAll}

#### \<static> FloorAll(rect) {#static-floorallrect}


**说明:**

圆矩形的位置和大小下至最大整数小于或等于每个电流坐标或维度。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形要调整. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 调整后的矩形.


> 源码：[src/geom/rectangle/FloorAll.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/FloorAll.js#L7)  
引入版本：3.0.0


### FromPoints {#FromPoints}

#### \<static> FromPoints(points, [out]) {#static-frompointspoints-out}


**说明:**

构造新的矩形或重新定位并调整现有矩形的大小,以便所有给定的点都位于或在其界限之内。

`points`参数是类似点的天体阵列:

```js
const points = [
    [100, 200],
    [200, 400],
    { x: 30, y: 60 }
]
```

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| points | array | 否 | 由矩形环绕的点阵(既包括两个与X和Y坐标相对应的元素的阵列,也包括一个具有公共`x`和`y`属性的物体)。 |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 可选矩形以调整 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 调整后的 `out`矩形,或者如果没有提供新的矩形。


> 源码：[src/geom/rectangle/FromPoints.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/FromPoints.js#L10)  
引入版本：3.0.0


### FromXY {#FromXY}

#### \<static> FromXY(x1, y1, x2, y2, [out]) {#static-fromxyx1-y1-x2-y2-out}


**说明:**

创建最小的矩形, 包含两个坐标对 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x1 | number | 否 | 第一点的X坐标. |
| y1 | number | 否 | 初点的Y坐标 |
| x2 | number | 否 | 第二点的X坐标. |
| y2 | number | 否 | 第二点的Y坐标. |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 可选矩形以调整 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 调整后的 `out`矩形,或者如果没有提供新的矩形。


> 源码：[src/geom/rectangle/FromXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/FromXY.js#L9)  
引入版本：3.23.0


### GetAspectRatio {#GetAspectRatio}

#### \<static> GetAspectRatio(rect) {#static-getaspectratiorect}


**说明:**

计算矩形的宽度/ 高比。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 长方形. |


**返回值:** number - 矩形的宽度/ 高度比 。


> 源码：[src/geom/rectangle/GetAspectRatio.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/GetAspectRatio.js#L7)  
引入版本：3.0.0


### GetCenter {#GetCenter}

#### \<static> GetCenter(rect, [out]) {#static-getcenterrect-out}


**说明:**

返回矩形中心作为点。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形以获得中心. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 可选矢量2对象,可使用中心坐标进行更新. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 修改后的 `out` 对象,或者如果没有提供新的矢量2。


> 源码：[src/geom/rectangle/GetCenter.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/GetCenter.js#L9)  
引入版本：3.0.0


### GetPoint {#GetPoint-3}

#### \<static> GetPoint(rectangle, position, [out]) {#static-getpointrectangle-position-out}


**说明:**

计算矩形周边某个特定`position`的点的坐标。

`position`是0到1之间的一个分数,它定义了该点的周界有多远.

0或1值返回矩形左上角的点,0.5值返回矩形右下角的点。0至0.5值位于上方或右侧,0.5至1值位于下方或左侧。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectangle | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形以获得周边点. |
| position | number | 否 | 正常的距离进入矩形的周界返回. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 使用点的`x`和`y`坐标更新的矢量2对象. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 更新后的 `out` 对象,或者如果没有给出 `out` 对象,则会给新的矢量2 。


> 源码：[src/geom/rectangle/GetPoint.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/GetPoint.js#L10)  
引入版本：3.0.0


### GetPoints {#GetPoints-4}

#### \<static> GetPoints(rectangle, quantity, stepRate, [out]) {#static-getpointsrectangle-quantity-steprate-out}


**说明:**

从矩形的周长返回一个矢量2的数组点,每个点根据所需数量或步骤而间隔.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectangle | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形对象以获取点数 。 |
| quantity | number | 否 | 从矩形的周界返回的均匀间隔点数。 如果有假, 则使用 stepRate 参数来计算点数 。 |
| stepRate | number | 否 | 点间步骤。 用于计算数量不实时返回的点数。 如果数量为正数, 则忽略 。 |
| out | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 将点数存储到的可选数组 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 矩形周边的一阵矢量2点.


> 源码：[src/geom/rectangle/GetPoints.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/GetPoints.js#L10)  
引入版本：3.0.0


### GetSize {#GetSize}

#### \<static> GetSize(rect, [out]) {#static-getsizerect-out}


**说明:**

返回矩形的大小, 以矢量2 对象表示。 以 `width` 的值为 `x` 属性, 以 `height` 属性为 `y` 属性。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形以获得大小. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 矢量2 对象将大小存储在其中。 如果不给定, 则创建新的矢量2 实例 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - `x`持有宽度,`y`持有矩形高度的矢量2物体.


> 源码：[src/geom/rectangle/GetSize.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/GetSize.js#L9)  
引入版本：3.0.0


### Inflate {#Inflate}

#### \<static> Inflate(rect, x, y) {#static-inflaterect-x-y}


**说明:**

将矩形的大小增加指定数量。

矩形的中心保持不变,金额被加到两侧,所以实际的宽度或高度的增加比相应的参数大2倍.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 长方形以充气. |
| x | number | 否 | 左侧和右侧应水平移动多少像素. |
| y | number | 否 | 上下两侧应垂直移动多少像素. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 充气矩形的圆柱形.


> 源码：[src/geom/rectangle/Inflate.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Inflate.js#L9)  
引入版本：3.0.0


### Intersection {#Intersection}

#### \<static> Intersection(rectA, rectB, [out]) {#static-intersectionrecta-rectb-out}


**说明:**

需要两个矩形并首先检查它们是否交叉。 如果它们相交, 则返回`out`矩形中的交叉区域。 如果它们不相交, `out`矩形的宽度和高度为0 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectA | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 最早的矩形从路口得到. |
| rectB | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第二矩形从中取出交汇点. |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 用于存储交叉结果的矩形 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 交叉结果。 如果宽度和高度为零, 则没有发生交叉 。


> 源码：[src/geom/rectangle/Intersection.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Intersection.js#L10)  
引入版本：3.11.0


### MarchingAnts {#MarchingAnts}

#### \<static> MarchingAnts(rect, [step], [quantity], [out]) {#static-marchingantsrect-step-quantity-out}


**说明:**

返回矩形周边平均分布的矢量2点数组。这通常用来创建“总体蚂蚁”选择效果,即返回的点用来激活一个表面在矩形边缘行进的破折的轮廓。

您可以通过提供每个点之间的像素`step`距离来控制点间距, 或者指定在全周周周周平均分布点的`quantity`。 如果省略了两者, 则返回空阵列。 如果提供了`step`, `quantity` 则从周周长中导出, 由该步位除以。 如果只提供了 `quantity`, 则取而代之 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形以获得周边点. |
| step | number | 是 | 周界每个点之间的距离。 如果您想要使用 `quantity` 参数, 请设定为 `null` 。 |
| quantity | number | 是 | 返回的点数总数。然后,该步骤根据矩形的长度计算,除以此值。 |
| out | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 将存储周边点的数组。 如果不给出, 则创建新的数组实例 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 包含矩形周边点的阵列。


> 源码：[src/geom/rectangle/MarchingAnts.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/MarchingAnts.js#L10)  
引入版本：3.0.0


### MergePoints {#MergePoints}

#### \<static> MergePoints(target, points) {#static-mergepointstarget-points}


**说明:**

将矩形与点列表合并,重新定位和/或重新调整大小,使所有点都位于其界限或界限内。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形,应该合并。 |
| points | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 否 | 向量2 对象的阵列,应该与矩形合并。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 修改后的矩形.


> 源码：[src/geom/rectangle/MergePoints.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/MergePoints.js#L7)  
引入版本：3.0.0


### MergeRect {#MergeRect}

#### \<static> MergeRect(target, source) {#static-mergerecttarget-source}


**说明:**

将源矩合并到目标矩形中并返回目标。两个矩形都不应该有负宽度或高度。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 目标矩形。 将修改以包含源矩形 。 |
| source | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 将合并为目标矩形的矩形 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 含有源矩的修改目标矩形.


> 源码：[src/geom/rectangle/MergeRect.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/MergeRect.js#L7)  
引入版本：3.0.0


### MergeXY {#MergeXY}

#### \<static> MergeXY(target, x, y) {#static-mergexytarget-x-y}


**说明:**

通过重新定位和/或重新调整大小将矩形与点合并,使点处于或在其界限内。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形,应该合并和修改。 |
| x | number | 否 | 合并点的X坐标。 |
| y | number | 否 | 合并点的Y坐标。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 修改后的`target`矩形.


> 源码：[src/geom/rectangle/MergeXY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/MergeXY.js#L7)  
引入版本：3.0.0


### Offset {#Offset-3}

#### \<static> Offset(rect, x, y) {#static-offsetrect-x-y}


**说明:**

以给定的横向和纵向数量翻译一个矩形,在保留其大小的同时移动其位置。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形要调整. |
| x | number | 否 | 水平移动矩形的距离 。 |
| y | number | 否 | 垂直移动矩形的距离 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 调整后的矩形.


> 源码：[src/geom/rectangle/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Offset.js#L7)  
引入版本：3.0.0


### OffsetPoint {#OffsetPoint-2}

#### \<static> OffsetPoint(rect, vec) {#static-offsetpointrect-vec}


**说明:**

用翻译向量的坐标翻译矩形左上角。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形要调整. |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 坐标应用作抵消的矢量2点。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 调整后的矩形.


> 源码：[src/geom/rectangle/OffsetPoint.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/OffsetPoint.js#L7)  
引入版本：3.0.0


### Overlaps {#Overlaps}

#### \<static> Overlaps(rectA, rectB) {#static-overlapsrecta-rectb}


**说明:**

检查两个矩形重叠。 如果一个矩形在另一个矩形内, 两者将被视为重叠。 因此, 矩形被视作“ 固体 ” 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectA | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 首座矩形检查. |
| rectB | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第二矩形来验. |


**返回值:** boolean - `true` 如果两个矩形重叠, `false` 否则。


> 源码：[src/geom/rectangle/Overlaps.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Overlaps.js#L7)  
引入版本：3.0.0


### Perimeter {#Perimeter-1}

#### \<static> Perimeter(rect) {#static-perimeterrect}


**说明:**

计算矩形的周界。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形来用. |


**返回值:** number - 矩形的周长,等于`(width * 2) + (height * 2)`.


> 源码：[src/geom/rectangle/Perimeter.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Perimeter.js#L7)  
引入版本：3.0.0


### PerimeterPoint {#PerimeterPoint}

#### \<static> PerimeterPoint(rectangle, angle, [out]) {#static-perimeterpointrectangle-angle-out}


**说明:**

返回一个点,从矩形的周界,以给定角度为基础,从矩形的中心以度数测量。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectangle | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形以获得周边点. |
| angle | number | 否 | 点角,以度计. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 矢量2 对象将位置存储在其中。 如果不给定, 则创建新的矢量2 实例 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 位于矩形周长的矢量2物体,持有点坐标.


> 源码：[src/geom/rectangle/PerimeterPoint.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/PerimeterPoint.js#L10)  
引入版本：3.0.0


### Random {#Random-3}

#### \<static> Random(rect, out) {#static-randomrect-out}


**说明:**

返回矩形内的随机点。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形从这里返回一点. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 以点坐标更新的对象 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 修改后的 `out` 对象,或者如果未提供新的点。


> 源码：[src/geom/rectangle/Random.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Random.js#L9)  
引入版本：3.0.0


### RandomOutside {#RandomOutside}

#### \<static> RandomOutside(outer, inner, [out]) {#static-randomoutsideouter-inner-out}


**说明:**

计算位于 `outer` 矩形,但外侧 `inner` 矩形。 内矩形必须完全包含在外矩形内才能产生点。 如果 `inner` 尚未完全纳入 `outer`,函数返回 `out` 矢量不变。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| outer | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 外矩形以获得内部的随机点. |
| inner | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 内矩形以排除返回点。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 一个用于存储结果的矢量2对象。 如果未指定, 将会创建一个新的矢量2 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 一个矢量2对象,含有其`x`和`y`属性中的随机值.


> 源码：[src/geom/rectangle/RandomOutside.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/RandomOutside.js#L11)  
引入版本：3.10.0


### SameDimensions {#SameDimensions}

#### \<static> SameDimensions(rect, toCompare) {#static-samedimensionsrect-tocompare}


**说明:**

确定两个对象(矩形或类似矩形)在严格平等的情况下是否具有相同的宽度和高度值.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第一个矩形物体. |
| toCompare | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第二矩形物体. |


**返回值:** boolean - `true` 如果对象具有等值,则 `width` 财务报告和已审计财务报表 `height` 属性,否则 `false`.


> 源码：[src/geom/rectangle/SameDimensions.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/SameDimensions.js#L7)  
引入版本：3.15.0


### Scale {#Scale}

#### \<static> Scale(rect, x, y) {#static-scalerect-x-y}


**说明:**

以给定的因子缩放给定的矩形的宽度和高度。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 将缩放到指定数量中的 `Rectangle` 对象 。 |
| x | number | 否 | 水平地缩放矩形的因子 。 |
| y | number | 否 | 垂直缩放矩形的因子。如果不指定,则矩形将按双向的因子`x`缩放。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 矩形对象,其特性为更新后的`width`和`height`,由缩放系数计算.


> 源码：[src/geom/rectangle/Scale.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Scale.js#L7)  
引入版本：3.0.0


### Union {#Union}

#### \<static> Union(rectA, rectB, [out]) {#static-unionrecta-rectb-out}


**说明:**

创建新的矩形或重新定位和/或调整已有矩形的大小,使其包含两个给定的矩形,即计算它们的结合。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectA | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 最早使用的矩形. |
| rectB | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第二矩形用. |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 将工会存放在矩形的. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 修改后的 `out` 矩形,或者如果没有提供新的矩形。


> 源码：[src/geom/rectangle/Union.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Union.js#L9)  
引入版本：3.0.0


# Phaser.Geom.Triangle {#page-title-6}

### Area {#Area-3}

#### \<static> Area(triangle) {#static-areatriangle}


**说明:**

返回三角形区域。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角形用来使用. |


**返回值:** number - 三角地带,总是非负面的.


> 源码：[src/geom/triangle/Area.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Area.js#L9)  
引入版本：3.0.0


### BuildEquilateral {#BuildEquilateral}

#### \<static> BuildEquilateral(x, y, length) {#static-buildequilateralx-y-length}


**说明:**

构造一个等边三角形。在等边三角形中,所有边长(连)相同,所有角大小(连)相同。x/y指定三角形(x1/y1)的上中段,长度为每边的长度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | x 三角形顶点坐标. |
| y | number | 否 | y 三角形顶点坐标。 |
| length | number | 否 | 三角形两侧的长度。 |


**返回值:** [Phaser.Geom.Triangle](/api/class/geom-triangle) - 一个新的等角三角,顶端为(`x`,`y`),并覆盖指定为`length`的四面.


> 源码：[src/geom/triangle/BuildEquilateral.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/BuildEquilateral.js#L9)  
引入版本：3.0.0


### BuildFromPolygon {#BuildFromPolygon}

#### \<static> BuildFromPolygon(data, [holes], [scaleX], [scaleY], [out]) {#static-buildfrompolygondata-holes-scalex-scaley-out}


**说明:**

然后返回三角形的数组,其中给定的顶点已分解成一系列三角形。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| data | array | 否 |  | 平坦的顶点数组坐标,如 \[x0,y0, x1,y1, x2,y2,...\] |
| holes | array | 是 | null | 如果有孔指数阵列(例如12顶点输入的[5, 8]),则指一个孔有顶点5-7,另一个孔有8-11。 |
| scaleX | number | 是 | 1 | 水平比例系数将结果的点乘以。 |
| scaleY | number | 是 | 1 | 垂直比例系数,将产生的点乘以。 |
| out | array \| Array.\<[Phaser.Geom.Triangle](/api/class/geom-triangle)> | 是 |  | 一个将三角形实例存储到其中的数组。 如果不提供, 则会创建新数组 。 |


**返回值:** array, Array.\<[Phaser.Geom.Triangle](/api/class/geom-triangle)> - 三角形实例的阵列,每个三角形都基于已分解的顶点数据.


> 源码：[src/geom/triangle/BuildFromPolygon.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/BuildFromPolygon.js#L10)  
引入版本：3.0.0


### BuildRight {#BuildRight}

#### \<static> BuildRight(x, y, width, height) {#static-buildrightx-y-width-height}


**说明:**

构建一个右三角形,即一个具有90度角和两个急性角的三角形. `x` 财务报告和已审计财务报表 `y` 坐标标记右角顶点的位置,它成为三角的第一点。 `width` 财务报告和已审计财务报表 `height` 值决定了两侧与正确角度相邻的长度,可能是正的或负的,它控制着两侧从右角顶点延伸的方向。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 右角的X坐标,这也是构造三角的第一个X坐标. |
| y | number | 否 | 右角的Y坐标,这也是构造三角的第一个Y坐标. |
| width | number | 否 | 左侧或右侧的右角的长度。 |
| height | number | 否 | 右角度上或下方的边长。如果不给定,则默认为 `width` 值 。 |


**返回值:** [Phaser.Geom.Triangle](/api/class/geom-triangle) - 构造的右三角形。


> 源码：[src/geom/triangle/BuildRight.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/BuildRight.js#L13)  
引入版本：3.0.0


### CenterOn {#CenterOn-2}

#### \<static> CenterOn(triangle, x, y, [centerFunc]) {#static-centerontriangle-x-y-centerfunc}


**说明:**

定位三角,使其以给定坐标为中心。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角形要定位 。 |
| x | number | 否 | 水平坐标以中心为中心. |
| y | number | 否 | 垂直坐标以中心为中心. |
| centerFunc | CenterFunction | 是 | 三角形中点所用的函数。默认为中心形中点 。 |


**返回值:** [Phaser.Geom.Triangle](/api/class/geom-triangle) - 三角地带是中心地带


> 源码：[src/geom/triangle/CenterOn.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/CenterOn.js#L18)  
引入版本：3.0.0


### Centroid {#Centroid}

#### \<static> Centroid(triangle, [out]) {#static-centroidtriangle-out}


**说明:**

计算三角形的半人马体的位置,它也是其质量中心(重力中心).

中间体是其三个中位数(从顶点到对面的两段线)在三角交汇的点,它以2:1的比例将每个中间体分成.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角形用来使用. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储坐标的矢量2对象 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - `out`对象具有修改后的`x`和`y`属性,或者如果没有提供新的矢量2.


> 源码：[src/geom/triangle/Centroid.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Centroid.js#L9)  
引入版本：3.0.0


### CircumCenter {#CircumCenter}

#### \<static> CircumCenter(triangle, [out]) {#static-circumcentertriangle-out}


**说明:**

计算三角形的圆形,环形是环形圆形的中心,是穿过三角形的所有三个顶点的独特圆形,也是三角形两侧垂直两段的常见交点,也是与三角形的所有三个顶部具有等距离的唯一点.

改编自 [http://bjornharrtell.github.io/jsts/doc/api/jsts_geom_Triangle.js.html](http://bjornharrtell.github.io/jsts/doc/api/jsts_geom_Triangle.js.html)

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角地带将获得环绕 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 矢量2 对象将位置存储在其中。 如果不给定, 则创建新的矢量2 实例 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 具有三角环坐标的矢量2天体。


> 源码：[src/geom/triangle/CircumCenter.js#L28](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/CircumCenter.js#L28)  
引入版本：3.0.0


### CircumCircle {#CircumCircle}

#### \<static> CircumCircle(triangle, [out]) {#static-circumcircletriangle-out}


**说明:**

查找三角形对象的圆(圆圈),圆圈是触及三角形所有顶点的圆圈。

改编自 [https://gist.github.com/mutoo/5617691](https://gist.github.com/mutoo/5617691)

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角形作为输入使用. |
| out | [Phaser.Geom.Circle](/api/class/geom-circle) | 是 | 存储结果的可选圆 。 |


**返回值:** [Phaser.Geom.Circle](/api/class/geom-circle) - 更新的 `out` 圆,或者如果没有提供新圆。


> 源码：[src/geom/triangle/CircumCircle.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/CircumCircle.js#L9)  
引入版本：3.0.0


### Clone {#Clone-5}

#### \<static> Clone(source) {#static-clonesource-4}


**说明:**

克隆是一个三角天体。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角形要克隆了 三角形要克隆了 |


**返回值:** [Phaser.Geom.Triangle](/api/class/geom-triangle) - 一个与给定的三角形完全相同的新三角形,但与它相分离.


> 源码：[src/geom/triangle/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Clone.js#L9)  
引入版本：3.0.0


### Contains {#Contains-4}

#### \<static> Contains(triangle, x, y) {#static-containstriangle-x-y}


**说明:**

检查一个点(作为一对坐标)是否位于三角的界限内.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角区要检查。 |
| x | number | 否 | 检查点的X坐标 |
| y | number | 否 | 检查点的Y坐标 |


**返回值:** boolean - 如果点在三角之内,则`true`,否则则`false`.


> 源码：[src/geom/triangle/Contains.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Contains.js#L9)  
引入版本：3.0.0


### ContainsArray {#ContainsArray}

#### \<static> ContainsArray(triangle, points, [returnFirst], [out]) {#static-containsarraytriangle-points-returnfirst-out}


**说明:**

过滤一组类似点的物体,仅用于三角形内的对象。

如果 `returnFirst` 是真的, 则返回只包含三角形内所提供阵列中第一个点的阵列( 或如果没有这样的点, 则返回空阵列) 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 |  | 检查点的三角形 |
| points | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 否 |  | 要检查它们是否位于三角形之内, 需要一系列的矢量2 对象 。 |
| returnFirst | boolean | 是 | false | 如果 `true`,返回只包含发现在三角形内的第一点的阵列。 |
| out | array | 是 |  | 如果提供, 三角形内的点将附加到这个数组中, 而不是添加到一个新的数组中。 如果 `returnFirst` 是真实的, 则只附加三角形内的第一个点。 此数组也会被此函数返回 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 如果一个阵列作为`out`提供,则包含`points`中位于三角形范围内的所有点的阵列,点数将附在该阵列上,并在此返回。


> 源码：[src/geom/triangle/ContainsArray.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/ContainsArray.js#L7)  
引入版本：3.0.0


### ContainsPoint {#ContainsPoint-4}

#### \<static> ContainsPoint(triangle, vec) {#static-containspointtriangle-vec}


**说明:**

测试三角形是否包含点。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角形的 三角形的 三角形的 The 三角形的 三角形的 The 三角形的 三角形的 |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 矢量2的点值测试是否位于三角形内. |


**返回值:** boolean - 如果点在三角形内,则使用`true`,否则使用`false`.


> 源码：[src/geom/triangle/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/ContainsPoint.js#L9)  
引入版本：3.0.0


### CopyFrom {#CopyFrom-4}

#### \<static> CopyFrom(source, dest) {#static-copyfromsource-dest-4}


**说明:**

复制一个三角的值到目的地三角 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 复制值的源三角 。 |
| dest | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 目的地三角区将数值复制到 。 |


**返回值:** [Phaser.Geom.Triangle](/api/class/geom-triangle) - 目的地三角区.


> 源码：[src/geom/triangle/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/CopyFrom.js#L7)  
引入版本：3.0.0


### Decompose {#Decompose-1}

#### \<static> Decompose(triangle, [out]) {#static-decomposetriangle-out}


**说明:**

将三角形分解成一系列的点。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角化去分解. |
| out | array | 是 | 存储点数组 。 |


**返回值:** array - 提供的`out`阵列,或者如果没有提供新的阵列,有三个物体,其`x`和`y`特性代表其所附三角的每个点。


> 源码：[src/geom/triangle/Decompose.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Decompose.js#L7)  
引入版本：3.0.0


### Equals {#Equals-4}

#### \<static> Equals(triangle, toCompare) {#static-equalstriangle-tocompare}


**说明:**

如果两个三角坐标相同, 返回真实值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 首个三角形检查. |
| toCompare | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 检查第二个三角形 |


**返回值:** boolean - 如果两个三角形的坐标完全相同,则`true`,否则则`false`.


> 源码：[src/geom/triangle/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Equals.js#L7)  
引入版本：3.0.0


### GetPoint {#GetPoint-4}

#### \<static> GetPoint(triangle, position, [out]) {#static-getpointtriangle-position-out}


**说明:**

返回三角形周边的点作为矢量2,以正态位置值为基础。

`position`参数是一个0到1之间的值,其中0到1都映射到A线(第一个顶点)的起始点,该点通过绕过三角形的周长来计算,顺序是:A线,然后是B线,然后是C线.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角洲从周边得到点。 |
| position | number | 否 | 0到1之间的正态值代表着三角形周边位置,0到1都返回A线的起始点. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 存储结果的可选矢量2 点。 如果不给出, 将会创建新的矢量2 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 包含三角形周边位置坐标的矢量2点.


> 源码：[src/geom/triangle/GetPoint.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/GetPoint.js#L10)  
引入版本：3.0.0


### GetPoints {#GetPoints-5}

#### \<static> GetPoints(triangle, quantity, stepRate, [out]) {#static-getpointstriangle-quantity-steprate-out}


**说明:**

返回三角形周边的均匀空格点数组。

点沿三角形的三边排列顺序(A,B,然后C),其位置根据总周长按比例计算.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角帮从中得分 |
| quantity | number | 否 | 平方位点数返回。 设定为 0 以返回基于 `stepRate` 的任意点数 。 |
| stepRate | number | 否 | 如果 `quantity` 是 0,则沿周边返回的每个点之间的像素距离。 |
| out | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 数组,这些点应附加在其中。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 修改后的 `out` 阵列, 或者如果没有提供新的阵列。


> 源码：[src/geom/triangle/GetPoints.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/GetPoints.js#L10)  
引入版本：3.0.0


### InCenter {#InCenter}

#### \<static> InCenter(triangle, [out]) {#static-incentertriangle-out}


**说明:**

计算三角形物体的中间位置。这是其三个角双扇形交汇的点,也是圆圈的中心,即三角形内嵌的圆圈。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角寻找中心 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 可选的矢量2点,用于存储坐标. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 三角形的中间点在矢量2中。


> 源码：[src/geom/triangle/InCenter.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/InCenter.js#L21)  
引入版本：3.0.0


### Offset {#Offset-4}

#### \<static> Offset(triangle, x, y) {#static-offsettriangle-x-y}


**说明:**

以给定的偏移移动三角的每个点(顶点),从而以偏移移动整个三角。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角移动. |
| x | number | 否 | 水平偏移( 距离) 移动每个点。 可以是正的还是负的 。 |
| y | number | 否 | 垂直偏移( 距离) 移动每个点。 可以是正的还是负的 。 |


**返回值:** [Phaser.Geom.Triangle](/api/class/geom-triangle) - 改编的三角形.


> 源码：[src/geom/triangle/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Offset.js#L7)  
引入版本：3.0.0


### Perimeter {#Perimeter-2}

#### \<static> Perimeter(triangle) {#static-perimetertriangle}


**说明:**

获得给定三角形的周长。通过加加三边的长度来计算。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角线从这里得到长度。 |


**返回值:** number - 三角线的长度.


> 源码：[src/geom/triangle/Perimeter.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Perimeter.js#L9)  
引入版本：3.0.0


### Random {#Random-4}

#### \<static> Random(triangle, [out]) {#static-randomtriangle-out}


**说明:**

从给定三角区域范围内返回随机点。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角从随机点得到。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 矢量2 点对象将位置存储在其中。 如果不给定, 则创建新的矢量2 实例 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 一个矢量2点物体,在三角内随机位置的坐标。


> 源码：[src/geom/triangle/Random.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Random.js#L9)  
引入版本：3.0.0


### Rotate {#Rotate-1}

#### \<static> Rotate(triangle, angle) {#static-rotatetriangle-angle}


**说明:**

旋转三角形的中间点,这是其三角双扇交汇点。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角旋转. |
| angle | number | 否 | 三角旋转的角度,以弧度表示. |


**返回值:** [Phaser.Geom.Triangle](/api/class/geom-triangle) - 旋转三角形.


> 源码：[src/geom/triangle/Rotate.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Rotate.js#L10)  
引入版本：3.0.0


### RotateAroundPoint {#RotateAroundPoint-1}

#### \<static> RotateAroundPoint(triangle, point, angle) {#static-rotatearoundpointtriangle-point-angle}


**说明:**

在一个给定的矢量2 点上以一定角度旋转三角形。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角旋转. |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 矢量2点旋转三角形绕圈. |
| angle | number | 否 | 三角旋转的角度,以弧度表示. |


**返回值:** [Phaser.Geom.Triangle](/api/class/geom-triangle) - 旋转三角形.


> 源码：[src/geom/triangle/RotateAroundPoint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/RotateAroundPoint.js#L9)  
引入版本：3.0.0


### RotateAroundXY {#RotateAroundXY-1}

#### \<static> RotateAroundXY(triangle, x, y, angle) {#static-rotatearoundxytriangle-x-y-angle}


**说明:**

在一个特定点上以特定角度旋转整个三角。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角旋转. |
| x | number | 否 | 三角旋转点的X坐标 |
| y | number | 否 | 三角旋转点的Y坐标 |
| angle | number | 否 | 三角旋转的角度,以弧度表示. |


**返回值:** [Phaser.Geom.Triangle](/api/class/geom-triangle) - 旋转三角形.


> 源码：[src/geom/triangle/RotateAroundXY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/RotateAroundXY.js#L7)  
引入版本：3.0.0

---
