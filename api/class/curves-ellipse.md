# Ellipse {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/curves-ellipse)

椭圆曲线(英语:Ellipse Curve)是一种描述椭圆路径的平滑曲线,可用于沿椭圆路径移动游戏对象,生成分布在椭圆周围的点,或者绘制椭圆弧作为路径或图形对象的一部分.

您可以控制中心位置,水平和垂直的光度,起始和结束角度,旋转,以及曲线是顺时针还是逆时针运行. 仅通过`xRadius`将创建一个圆(默认情况下,光度均相等).

此曲线扩展了基数`Phaser.Curves.Curve`类,可以在Phaser接受曲线的任何地方使用,例如`Phaser.Curves.Path`或一个`PathFollower`游戏对象.

详情请见[https://en.wikipedia.org/wiki/Ellipse](https://en.wikipedia.org/wiki/Ellipse)。

**构造函数**

`new Ellipse([x], [y], [xRadius], [yRadius], [startAngle], [endAngle], [clockwise], [rotation])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number \| [Phaser.Types.Curves.EllipseCurveConfig](/api/typedef/types-curves#ellipsecurveconfig) | 是 | 0 | 椭圆的x坐标,或椭圆曲线配置对象. |
| y | number | 是 | 0 | 椭圆形的y坐标. |
| xRadius | number | 是 | 0 | 椭圆的横向半径. |
| yRadius | number | 是 | 0 | 椭圆的垂直半径. |
| startAngle | number | 是 | 0 | 椭圆的起始角,以度计. |
| endAngle | number | 是 | 360 | 椭圆的端角,以度计. |
| clockwise | boolean | 是 | false | 椭圆角是按顺时针(`true`)还是逆时针(`false`)给出的. |
| rotation | number | 是 | 0 | 椭圆的旋转,以度数表示. |

---


**作用域**: static


**继承**

> [Phaser.Curves.Curve](/api/class/curves-curve)  



> 源码：[src/curves/EllipseCurve.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L16)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Curves.Curve](/api/class/curves-curve):**


 - [active](/api/class/curves-curve#active)
 - [arcLengthDivisions](/api/class/curves-curve#arcLengthDivisions)
 - [cacheArcLengths](/api/class/curves-curve#cacheArcLengths)
 - [defaultDivisions](/api/class/curves-curve#defaultDivisions)
 - [needsUpdate](/api/class/curves-curve#needsUpdate)
 - [type](/api/class/curves-curve#type)




---

## 公开成员 {#public-members}

### angle {#angle}

#### angle: number {#angle-number}


**说明:**

椭圆的旋转,相对中心,以度数表示.


> 源码：[src/curves/EllipseCurve.js#L545](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L545)  
引入版本：3.14.0


---

### clockwise {#clockwise}

#### clockwise: boolean {#clockwise-boolean}


**说明:**

如果椭圆旋转顺时针,则`true`;如果逆时针旋转,则`false`。


> 源码：[src/curves/EllipseCurve.js#L524](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L524)  
引入版本：3.0.0


---

### endAngle {#endAngle}

#### endAngle: number {#endangle-number}


**说明:**

椭圆的端角以度表示.


> 源码：[src/curves/EllipseCurve.js#L503](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L503)  
引入版本：3.0.0


---

### p0 {#p0}

#### p0: [Phaser.Math.Vector2](/api/class/math-vector2) {#p0-phasermathvector2}


**说明:**

椭圆的中心点。 用于计算旋转 。


> 源码：[src/curves/EllipseCurve.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L80)  
引入版本：3.0.0


---

### rotation {#rotation}

#### rotation: number {#rotation-number}


**说明:**

椭圆相对中心旋转,以弧度表示.


> 源码：[src/curves/EllipseCurve.js#L566](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L566)  
引入版本：3.0.0


---

### startAngle {#startAngle}

#### startAngle: number {#startangle-number}


**说明:**

椭圆的起始角度,以度计.


> 源码：[src/curves/EllipseCurve.js#L482](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L482)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

椭圆中心轴的x坐标.


> 源码：[src/curves/EllipseCurve.js#L398](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L398)  
引入版本：3.0.0


---

### xRadius {#xRadius}

#### xRadius: number {#xradius-number}


**说明:**

椭圆的横向半径.


> 源码：[src/curves/EllipseCurve.js#L440](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L440)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

椭圆中心y坐标.


> 源码：[src/curves/EllipseCurve.js#L419](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L419)  
引入版本：3.0.0


---

### yRadius {#yRadius}

#### yRadius: number {#yradius-number}


**说明:**

椭圆的垂直半径.


> 源码：[src/curves/EllipseCurve.js#L461](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L461)  
引入版本：3.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Curves.Curve](/api/class/curves-curve):**


 - [draw](/api/class/curves-curve#draw)
 - [getBounds](/api/class/curves-curve#getBounds)
 - [getDistancePoints](/api/class/curves-curve#getDistancePoints)
 - [getEndPoint](/api/class/curves-curve#getEndPoint)
 - [getLength](/api/class/curves-curve#getLength)
 - [getLengths](/api/class/curves-curve#getLengths)
 - [getPointAt](/api/class/curves-curve#getPointAt)
 - [getPoints](/api/class/curves-curve#getPoints)
 - [getRandomPoint](/api/class/curves-curve#getRandomPoint)
 - [getSpacedPoints](/api/class/curves-curve#getSpacedPoints)
 - [getTangent](/api/class/curves-curve#getTangent)
 - [getTangentAt](/api/class/curves-curve#getTangentAt)
 - [getTFromDistance](/api/class/curves-curve#getTFromDistance)
 - [getUtoTmapping](/api/class/curves-curve#getUtoTmapping)
 - [updateArcLengths](/api/class/curves-curve#updateArcLengths)




---

## 公开方法 {#public-methods}

### fromJSON {#fromJSON}

#### \<static> fromJSON(data) {#static-fromjsondata}


**说明:**

从提供的椭圆曲线配置对象创建曲线。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | [Phaser.Types.Curves.JSONEllipseCurve](/api/typedef/types-curves#jsonellipsecurve) | 否 | JSON 对象包含此曲线数据. |


**返回值:** [Phaser.Curves.Ellipse](/api/class/curves-ellipse) - 由配置对象构建的椭圆曲线。


> 源码：[src/curves/EllipseCurve.js#L612](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L612)  
引入版本：3.0.0


---

### getPoint {#getPoint}

#### \<instance> getPoint(t, [out]) {#instance-getpointt-out}


**说明:**

返回给定的正态位置 `t` 的此曲线点, 0 是起始点, 1 是终点点。 结果将计算起始角、 结束角、 顺时针方向和椭圆旋转 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 沿曲线返回的位置。 0 开始和 1 结束。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储结果的矢量2 对象。 如果不给定, 将会创建 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 曲线上点的坐标。 如果给定了 `out` 对象, 将会返回 。


> 源码：[src/curves/EllipseCurve.js#L186](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L186)  
引入版本：3.0.0


---

### getResolution {#getResolution}

#### \<instance> getResolution(divisions) {#instance-getresolutiondivisions}


**说明:**

返回此曲线的分辨率, 即用于大致的点数。 对于椭圆, 将请求的除数增加一倍, 以提供准确的弧长计算 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| divisions | number | 否 | 选择的分值。 |


**返回值:** number - 曲线分辨率。


> 源码：[src/curves/EllipseCurve.js#L171](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L171)  
引入版本：3.0.0


---

### getStartPoint {#getStartPoint}

#### \<instance> getStartPoint([out]) {#instance-getstartpointout}


**说明:**

获得曲线的起点。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储结果的矢量2 对象。 如果不给定, 将会创建 。 |


**Overrides:** Phaser.Curves.Curve#getStartPoint


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 曲线上点的坐标。 如果给定了 `out` 对象, 将会返回 。


> 源码：[src/curves/EllipseCurve.js#L152](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L152)  
引入版本：3.0.0


---

### setClockwise {#setClockwise}

#### \<instance> setClockwise(value) {#instance-setclockwisevalue}


**说明:**

设定此曲线是否顺时针或逆时针延伸 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 此曲线的顺时针状态 。 |


**返回值:** [Phaser.Curves.Ellipse](/api/class/curves-ellipse) - 此曲线对象 。


> 源码：[src/curves/EllipseCurve.js#L364](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L364)  
引入版本：3.0.0


---

### setEndAngle {#setEndAngle}

#### \<instance> setEndAngle(value) {#instance-setendanglevalue}


**说明:**

设置此曲线的端角。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 这个曲线的终点, 以度计. |


**返回值:** [Phaser.Curves.Ellipse](/api/class/curves-ellipse) - 此曲线对象 。


> 源码：[src/curves/EllipseCurve.js#L347](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L347)  
引入版本：3.0.0


---

### setHeight {#setHeight}

#### \<instance> setHeight(value) {#instance-setheightvalue}


**说明:**

设置此曲线的高度。 垂直半径( `yRadius`) 设定为给定值的一半 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 此曲线的高度 。 |


**返回值:** [Phaser.Curves.Ellipse](/api/class/curves-ellipse) - 此曲线对象 。


> 源码：[src/curves/EllipseCurve.js#L313](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L313)  
引入版本：3.0.0


---

### setRotation {#setRotation}

#### \<instance> setRotation(value) {#instance-setrotationvalue}


**说明:**

设置此曲线的旋转。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 这个曲线的旋转,以弧度表示. |


**返回值:** [Phaser.Curves.Ellipse](/api/class/curves-ellipse) - 此曲线对象 。


> 源码：[src/curves/EllipseCurve.js#L381](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L381)  
引入版本：3.0.0


---

### setStartAngle {#setStartAngle}

#### \<instance> setStartAngle(value) {#instance-setstartanglevalue}


**说明:**

设置此曲线的起始角度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 这个曲线的起始角度, 以度计. |


**返回值:** [Phaser.Curves.Ellipse](/api/class/curves-ellipse) - 此曲线对象 。


> 源码：[src/curves/EllipseCurve.js#L330](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L330)  
引入版本：3.0.0


---

### setWidth {#setWidth}

#### \<instance> setWidth(value) {#instance-setwidthvalue}


**说明:**

设置此曲线的宽度。 水平半径( `xRadius`) 设定为给定值的一半 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 此曲线的宽度 。 |


**返回值:** [Phaser.Curves.Ellipse](/api/class/curves-ellipse) - 此曲线对象 。


> 源码：[src/curves/EllipseCurve.js#L296](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L296)  
引入版本：3.0.0


---

### setXRadius {#setXRadius}

#### \<instance> setXRadius(value) {#instance-setxradiusvalue}


**说明:**

设置此曲线的横向半径。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 此曲线的横向半径. |


**返回值:** [Phaser.Curves.Ellipse](/api/class/curves-ellipse) - 此曲线对象 。


> 源码：[src/curves/EllipseCurve.js#L262](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L262)  
引入版本：3.0.0


---

### setYRadius {#setYRadius}

#### \<instance> setYRadius(value) {#instance-setyradiusvalue}


**说明:**

设置此曲线的垂直半径。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 此曲线的垂直半径 。 |


**返回值:** [Phaser.Curves.Ellipse](/api/class/curves-ellipse) - 此曲线对象 。


> 源码：[src/curves/EllipseCurve.js#L279](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L279)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

JSON 曲线的序列化.


**返回值:** [Phaser.Types.Curves.JSONEllipseCurve](/api/typedef/types-curves#jsonellipsecurve) - JSON 对象包含此曲线数据.


> 源码：[src/curves/EllipseCurve.js#L587](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/EllipseCurve.js#L587)  
引入版本：3.0.0


---

---
