# Ellipse {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/geom-ellipse)

椭圆天体。

椭圆按其中心位置(x,y),总宽度,总高度来定义,可用于几何交叉测试(点-在椭圆封存),在其周长或内侧取样均匀的间距或随机点,并作为碰撞或命中区的轻量级形状描述符.

这是一个几何对象,包含数值和相关的方法来检查和修改它们。它不是一个游戏对象,因为您无法将其添加到显示列表中,而且它没有纹理。要使一个椭圆形,您应该查看图形类的能力。

**构造函数**

`new Ellipse([x], [y], [width], [height])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 椭圆中心位置的x位置. |
| y | number | 是 | 0 | 椭圆中心y位置. |
| width | number | 是 | 0 | 椭圆的宽度. |
| height | number | 是 | 0 | 椭圆形的高度. |

---


**作用域**: static

> 源码：[src/geom/ellipse/Ellipse.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L14)  
引入版本：3.0.0

## 公开方法 {#public-methods}

### Area {#Area}

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


---

### Circumference {#Circumference}

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


---

### CircumferencePoint {#CircumferencePoint}

#### \<static> CircumferencePoint(ellipse, angle, [out]) {#static-circumferencepointellipse-angle-out}


**说明:**

返回一个矢量2,其中包含一个点的坐标,这个点根据给定角度在椭圆上。

**标签:**

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


---

### Clone {#Clone}

#### \<static> Clone(source) {#static-clonesource}


**说明:**

根据给定源所含值创建新的椭圆实例。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 要克隆的椭圆。可以是椭圆形或椭圆形物体的例,具有x、y、宽度和高度等属性。 |


**返回值:** [Phaser.Geom.Ellipse](/api/class/geom-ellipse) - 源椭圆的克隆.


> 源码：[src/geom/ellipse/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Clone.js#L9)  
引入版本：3.0.0


---

### contains {#contains}

#### \<instance> contains(x, y) {#instance-containsx-y}


**说明:**

检查是否包含给定的 x / y 坐标 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | x 坐标以检查椭圆内部. |
| y | number | 否 | 以Y坐标检查椭圆内. |


**返回值:** boolean - 如果坐标在椭圆内,则真实性不正确,否则是虚假的。


> 源码：[src/geom/ellipse/Ellipse.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L100)  
引入版本：3.0.0


---

### Contains {#Contains}

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


---

### ContainsPoint {#ContainsPoint}

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


---

### ContainsRect {#ContainsRect}

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


---

### CopyFrom {#CopyFrom}

#### \<static> CopyFrom(source, dest) {#static-copyfromsource-dest}


**说明:**

复制本 `x`, `y`, `width` 财务报告和已审计财务报表 `height` 从“属性”中 `source` 椭圆进入给定 `dest` 椭圆,然后返回 `dest` 椭圆形.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 源 Ellipse 复制这些值 。 |
| dest | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 目标椭圆复制值到 。 |


**返回值:** [Phaser.Geom.Ellipse](/api/class/geom-ellipse) - 目的地椭圆形.


> 源码：[src/geom/ellipse/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/CopyFrom.js#L7)  
引入版本：3.0.0


---

### Equals {#Equals}

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


---

### GetBounds {#GetBounds}

#### \<static> GetBounds(ellipse, [out]) {#static-getboundsellipse-out}


**说明:**

返回椭圆对象的界限。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 椭圆形以获得境界. |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) \| object | 是 | 矩形,或类似矩形的对象,将椭圆边界存储在其中。如果不给定新的矩形,则会创建。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle), object - 含有椭圆边框的矩形天体。


> 源码：[src/geom/ellipse/GetBounds.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/GetBounds.js#L9)  
引入版本：3.0.0


---

### getMajorRadius {#getMajorRadius}

#### \<instance> getMajorRadius() {#instance-getmajorradius}


**说明:**

返回椭圆的主要半径。 也称为半主轴 。


**返回值:** number - 主要的半径。


> 源码：[src/geom/ellipse/Ellipse.js#L283](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L283)  
引入版本：3.0.0


---

### getMinorRadius {#getMinorRadius}

#### \<instance> getMinorRadius() {#instance-getminorradius}


**说明:**

返回椭圆的微半径。又称半微轴。


**返回值:** number - 细半径.


> 源码：[src/geom/ellipse/Ellipse.js#L270](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L270)  
引入版本：3.0.0


---

### getPoint {#getPoint}

#### \<instance> getPoint(position, [point]) {#instance-getpointposition-point}


**说明:**

返回一个矢量2物体,其中含有一个点的坐标,该点以给定角度为基数,使其正常化至0至1. I. 即0.5的值将在椭圆周围180度给出点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| position | number | 否 | 0到1之间的值,其中0等于0度,0.5等于180度,1等于360在椭圆周围. |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储返回值的矢量2。如果不给定矢量2对象,将创建该对象。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 含有椭圆周围点坐标的矢量2实例。


> 源码：[src/geom/ellipse/Ellipse.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L116)  
引入版本：3.0.0


---

### GetPoint {#GetPoint}

#### \<static> GetPoint(ellipse, position, [out]) {#static-getpointellipse-position-out}


**说明:**

返回一个矢量2物体,其中含有一个点的坐标,该点在椭圆周长上,基于给定角度的正态化到0到1之间,即0.5的值会在椭圆周围180度给出点.

**标签:**

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


---

### getPoints {#getPoints}

#### \<instance> getPoints(quantity, [stepRate], [output]) {#instance-getpointsquantity-steprate-output}


**说明:**

返回含有椭圆周轴周围点坐标的矢量2对象阵列,以给定的数量或stepRate值为基础。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| quantity | number | 否 | 返回的点数。 如果一个假值, 数量将取自 `stepRate` 。 |
| stepRate | number | 是 | 通过获得椭圆的圆圈来设定数量,并以stepRate来划分. |
| output | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 插入矢量2s的数组。 如果不提供新的数组, 将会创建 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 椭圆周长周围各点相关的矢量2天体阵列。


> 源码：[src/geom/ellipse/Ellipse.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L136)  
引入版本：3.0.0


---

### GetPoints {#GetPoints}

#### \<static> GetPoints(ellipse, quantity, [stepRate], [out]) {#static-getpointsellipse-quantity-steprate-out}


**说明:**

返回含有椭圆周轴周围点坐标的矢量2对象阵列,以给定的数量或stepRate值为基础。

**标签:**

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


---

### getRandomPoint {#getRandomPoint}

#### \<instance> getRandomPoint([vec]) {#instance-getrandompointvec}


**说明:**

从给定椭圆内的任何位置返回一个统一分布的随机点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 一个矢量2对象设置随机的`x`和`y`值. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 具有`x`和`y`属性中随机值的矢量2对象.


> 源码：[src/geom/ellipse/Ellipse.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L156)  
引入版本：3.0.0


---

### isEmpty {#isEmpty}

#### \<instance> isEmpty() {#instance-isempty}


**说明:**

检查以查看椭圆是否为空:宽度或高度为零或小于零。


**返回值:** boolean - 如果椭圆形是空的,否则是假的.


> 源码：[src/geom/ellipse/Ellipse.js#L257](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L257)  
引入版本：3.0.0


---

### Offset {#Offset}

#### \<static> Offset(ellipse, x, y) {#static-offsetellipse-x-y}


**说明:**

以给出的数值来抵消椭圆。

**标签:**

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


---

### OffsetPoint {#OffsetPoint}

#### \<static> OffsetPoint(ellipse, vec) {#static-offsetpointellipse-vec}


**说明:**

以矢量2对象的`x`和`y`属性中给出的值来抵消椭圆。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 缩略语: |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 含有以椭圆抵消值的矢量2对象。 |


**返回值:** [Phaser.Geom.Ellipse](/api/class/geom-ellipse) - 椭圆形被冲掉.


> 源码：[src/geom/ellipse/OffsetPoint.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/OffsetPoint.js#L7)  
引入版本：3.0.0


---

### Random {#Random}

#### \<static> Random(ellipse, [out]) {#static-randomellipse-out}


**说明:**

从给定椭圆内的任何位置返回一个统一分布的随机点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 椭圆形从中随机得到点. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 一个矢量2对象设置随机的`x`和`y`值. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 具有`x`和`y`属性中随机值的矢量2对象.


> 源码：[src/geom/ellipse/Random.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Random.js#L9)  
引入版本：3.0.0


---

### setEmpty {#setEmpty}

#### \<instance> setEmpty() {#instance-setempty}


**说明:**

设置此椭圆为空, 宽度和高度为零。 不改变其位置 。


**返回值:** [Phaser.Geom.Ellipse](/api/class/geom-ellipse) - 此椭圆天体 。


> 源码：[src/geom/ellipse/Ellipse.js#L196](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L196)  
引入版本：3.0.0


---

### setPosition {#setPosition}

#### \<instance> setPosition(x, y) {#instance-setpositionx-y}


**说明:**

设置此椭圆的位置。 如果省略 `y` 参数, x 和 y 位置都将设置为 `x` 的值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 椭圆中心位置的x位置. |
| y | number | 否 | 椭圆中心y位置. |


**返回值:** [Phaser.Geom.Ellipse](/api/class/geom-ellipse) - 此椭圆天体 。


> 源码：[src/geom/ellipse/Ellipse.js#L213](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L213)  
引入版本：3.0.0


---

### setSize {#setSize}

#### \<instance> setSize(width, [height]) {#instance-setsizewidth-height}


**说明:**

设置此椭圆的大小。 不改变其位置。 如果省略 `height` 参数, 则设置为 `width`, 生成圆 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 否 |  | 椭圆的宽度. |
| height | number | 是 | "width" | 椭圆形的高度. |


**返回值:** [Phaser.Geom.Ellipse](/api/class/geom-ellipse) - 此椭圆天体 。


> 源码：[src/geom/ellipse/Ellipse.js#L235](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L235)  
引入版本：3.0.0


---

### setTo {#setTo}

#### \<instance> setTo(x, y, width, height) {#instance-settox-y-width-height}


**说明:**

设置此椭圆的x、y、宽度和高度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 椭圆中心位置的x位置. |
| y | number | 否 | 椭圆中心y位置. |
| width | number | 否 | 椭圆的宽度. |
| height | number | 否 | 椭圆形的高度. |


**返回值:** [Phaser.Geom.Ellipse](/api/class/geom-ellipse) - 此椭圆天体 。


> 源码：[src/geom/ellipse/Ellipse.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L173)  
引入版本：3.0.0


---

## 公开成员 {#public-members}

### bottom {#bottom}

#### bottom: number {#bottom-number}


**说明:**

椭圆形的底部位置.


> 源码：[src/geom/ellipse/Ellipse.js#L359](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L359)  
引入版本：3.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

椭圆形的高度.


> 源码：[src/geom/ellipse/Ellipse.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L89)  
引入版本：3.0.0


---

### left {#left}

#### left: number {#left-number}


**说明:**

椭圆形的左侧位置.


> 源码：[src/geom/ellipse/Ellipse.js#L296](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L296)  
引入版本：3.0.0


---

### right {#right}

#### right: number {#right-number}


**说明:**

椭圆形的正确位置.


> 源码：[src/geom/ellipse/Ellipse.js#L317](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L317)  
引入版本：3.0.0


---

### top {#top}

#### top: number {#top-number}


**说明:**

椭圆形的顶部位置.


> 源码：[src/geom/ellipse/Ellipse.js#L338](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L338)  
引入版本：3.0.0


---

### type {#type}

#### type: number {#type-number}


**说明:**

此对象的几何常数类型: `GEOM_CONST.ELLIPSE`. 用于快速类型比较.


> 源码：[src/geom/ellipse/Ellipse.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L48)  
引入版本：3.19.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

椭圆的宽度.


> 源码：[src/geom/ellipse/Ellipse.js#L79](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L79)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

椭圆中心位置的x位置.


> 源码：[src/geom/ellipse/Ellipse.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L59)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

椭圆中心y位置.


> 源码：[src/geom/ellipse/Ellipse.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/ellipse/Ellipse.js#L69)  
引入版本：3.0.0


---

---
