# Line {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/geom-line)

定义线段:以起点描述的线段的有限部分( )`x1`, `y1`)和一个终点(`x2`, `y2`) 与无限数学线不同,一线段具有固定的长度和方向.

全线段使用 Phaser 用于碰撞探测、几何计算、路径和边界定义以及放置工具。您可以通过 `getPoint`,通过 `getPoints`,或通过 `left`, `right`, `top`,和 `bottom` 进入者。

**构造函数**

`new Line([x1], [y1], [x2], [y2])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x1 | number | 是 | 0 | 线路起点的x坐标. |
| y1 | number | 是 | 0 | 线路起点的y坐标. |
| x2 | number | 是 | 0 | 线路终点的x坐标. |
| y2 | number | 是 | 0 | 线的终点的y坐标. |

---


**作用域**: static

> 源码：[src/geom/line/Line.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L14)  
引入版本：3.0.0

## 公开方法 {#public-methods}

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


---

### BresenhamPoints {#BresenhamPoints}

#### \<static> BresenhamPoints(line, [stepRate], [results]) {#static-bresenhampointsline-steprate-results}


**说明:**

使用 Bresenham 的线程算法, 这将返回给定线上所有坐标的阵列 。

电话 `start` 财务报告和已审计财务报表 `end` 点数在此运行前随算法对整数起作用而四舍五入。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 |  | 线条. |
| stepRate | number | 是 | 1 | 控制沿线对点进行取样的密度。一个值为 1 返回每个整数坐标;一个值为 2 返回其他坐标,等等。 |
| results | Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 是 |  | 将生成的坐标推向的可选数组 。 |


**返回值:** Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> - 线上坐标阵列.


> 源码：[src/geom/line/BresenhamPoints.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/BresenhamPoints.js#L7)  
引入版本：3.0.0


---

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


---

### Clone {#Clone}

#### \<static> Clone(source) {#static-clonesource}


**说明:**

切除给定的线条。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 克隆的源线 。 |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 克隆线.


> 源码：[src/geom/line/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Clone.js#L9)  
引入版本：3.0.0


---

### CopyFrom {#CopyFrom}

#### \<static> CopyFrom(source, dest) {#static-copyfromsource-dest}


**说明:**

复制一行的值到目的地行 。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 复制这些值的源行 。 |
| dest | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 复制值到的目标行 。 |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 目的地线


> 源码：[src/geom/line/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/CopyFrom.js#L7)  
引入版本：3.0.0


---

### Equals {#Equals}

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


---

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


---

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

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 |  | 线条对象. |
| ease | string \| function | 否 |  | 使用方便。 这可以是 EaseMap 的字符串, 也可以是自定义函数 。 |
| quantity | number | 否 |  | 返回的点数。 请注意, 如果您提供了 `collinearThreshold`, 所产生的数组可能并不总是包含这个点数 。 |
| collinearThreshold | number | 是 | 0 | 一个可选的阈值。 最终阵列被缩小, 使每个点至少被隔开这个距离。 这有助于减少在吵闹的易行度中的集群 。 |
| easeParams | Array.\<number> | 是 |  | 随易的可选的易解参数组. |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 包含线上各点坐标的数组数组数组数数组数组数. Vector2s.


> 源码：[src/geom/line/GetEasedPoints.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/GetEasedPoints.js#L11)  
引入版本：3.23.0


---

### GetMidPoint {#GetMidPoint}

#### \<static> GetMidPoint(line, [out]) {#static-getmidpointline-out}


**说明:**

获取给定线的中点 。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 取中点的线. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 可选的矢量2对象,将中点存储在其中 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 中线.


> 源码：[src/geom/line/GetMidPoint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/GetMidPoint.js#L9)  
引入版本：3.0.0


---

### GetNearestPoint {#GetNearestPoint}

#### \<static> GetNearestPoint(line, vec, [out]) {#static-getnearestpointline-vec-out}


**说明:**

将指定线段定义的无限线上最接近点到指定点。请注意,返回点将投射到全线上,而不是夹在段端点上。

**标签:**

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


---

### GetNormal {#GetNormal}

#### \<static> GetNormal(line, [out]) {#static-getnormalline-out}


**说明:**

计算给定行的正常值 。

线的正常是从它中指向垂直的矢量.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 计算正常的线条 。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 可选的矢量2对象存储正常的内置. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 线的正常。


> 源码：[src/geom/line/GetNormal.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/GetNormal.js#L11)  
引入版本：3.0.0


---

### getPoint {#getPoint}

#### \<instance> getPoint(position, [output]) {#instance-getpointposition-output}


**说明:**

获得一个点的线,这个线的长度是一定的百分数.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| position | number | 否 | 0到1之间的值,其中0为起始,0.5为中间,1为终点. |
| output | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 可选的矢量2对象存储线上点的坐标. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 含有线上点坐标的矢量2天体.


> 源码：[src/geom/line/Line.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L95)  
引入版本：3.0.0


---

### GetPoint {#GetPoint}

#### \<static> GetPoint(line, position, [out]) {#static-getpointline-position-out}


**说明:**

获得一个点的线,这个线的长度是一定的百分数.

**标签:**

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


---

### getPointA {#getPointA}

#### \<instance> getPointA([vec2]) {#instance-getpointavec2}


**说明:**

返回一个与本行起始对应的矢量2对象。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vec2 | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 设置结果的矢量2 对象。 如果 `undefined` 将创建新的矢量2 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 与此行起始相对应的矢量2对象。


> 源码：[src/geom/line/Line.js#L206](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L206)  
引入版本：3.0.0


---

### getPointB {#getPointB}

#### \<instance> getPointB([vec2]) {#instance-getpointbvec2}


**说明:**

返回一个与本行末尾相对应的矢量2对象。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vec2 | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 设置结果的矢量2 对象。 如果 `undefined` 将创建新的矢量2 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 与本行末端相对应的矢量2对象。


> 源码：[src/geom/line/Line.js#L227](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L227)  
引入版本：3.0.0


---

### getPoints {#getPoints}

#### \<instance> getPoints(quantity, [stepRate], [output]) {#instance-getpointsquantity-steprate-output}


**说明:**

沿着一行长度获得一些点数.

提供`quantity`,以获得沿线精确的点数.

提供a `stepRate` 以确保线上每个点之间的特定距离。设置 `quantity` 改为: `0` 提供时 `stepRate`.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| quantity | number | 否 | 线上要放置的点数。 设定为 `0` , 代之以 `stepRate` 。 |
| stepRate | number | 是 | 线上每个点之间的距离。 设定时, `quantity` 表示, 并设定为 `0` 。 |
| output | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 用于存储线上各点坐标的可选的矢量2对象数组。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 包含线上各点坐标的矢量2天体阵列。


> 源码：[src/geom/line/Line.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L113)  
引入版本：3.0.0


---

### GetPoints {#GetPoints}

#### \<static> GetPoints(line, quantity, [stepRate], [out]) {#static-getpointsline-quantity-steprate-out}


**说明:**

从第一个终点(x1,y1)开始,沿着一条线获得若干平方位点,最后一个终点(x2,y2)不包含在返回的点中.

提供`quantity`,以获得沿线精确的点数.

提供a `stepRate` 以确保线上每个点之间的特定距离。设置 `quantity` 改为: `0` 提供时 `stepRate`.

另见`GetEasedPoints`,以按照易性类型或输入函数将点数分布到横线的方法.

**标签:**

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


---

### getRandomPoint {#getRandomPoint}

#### \<instance> getRandomPoint([point]) {#instance-getrandompointpoint}


**说明:**

返回此行上随机选择的点, 并按其长度以统一分布方式选择。 如果提供了矢量2, 它将与结果一起被覆盖并返回; 否则将创建一个新的矢量2 。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 需要修改的矢量2的例子。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 随机点行.


> 源码：[src/geom/line/Line.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L137)  
引入版本：3.0.0


---

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


---

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


---

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


---

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


---

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


---

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


---

### Offset {#Offset}

#### \<static> Offset(line, x, y) {#static-offsetline-x-y}


**说明:**

将给定线的端点都通过指定的水平和垂直量翻译,在保留长度和角度的同时,有效将线向2D空间中的新位置移动.

**标签:**

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


---

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


---

### Random {#Random}

#### \<static> Random(line, [out]) {#static-randomline-out}


**说明:**

返回给定行上的随机点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 计算随机点的线条 。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 需要修改的矢量2的例子。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 存储在矢量2中的线上的随机点.


> 源码：[src/geom/line/Random.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Random.js#L9)  
引入版本：3.0.0


---

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


---

### Rotate {#Rotate}

#### \<static> Rotate(line, angle) {#static-rotateline-angle}


**说明:**

以弧度的给定角度绕其中点旋转一条线。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 轮回的线条。 |
| angle | number | 否 | 弧度旋转的角度. |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 旋转行.


> 源码：[src/geom/line/Rotate.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Rotate.js#L9)  
引入版本：3.0.0


---

### RotateAroundPoint {#RotateAroundPoint}

#### \<static> RotateAroundPoint(line, point, angle) {#static-rotatearoundpointline-point-angle}


**说明:**

以弧度以给定角度绕一个点旋转一条线 。

**标签:**

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


---

### RotateAroundXY {#RotateAroundXY}

#### \<static> RotateAroundXY(line, x, y, angle) {#static-rotatearoundxyline-x-y-angle}


**说明:**

以弧度以给定角度绕给定坐标旋转一条线 。

**标签:**

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


---

### setFromObjects {#setFromObjects}

#### \<instance> setFromObjects(start, end) {#instance-setfromobjectsstart-end}


**说明:**

设定此线以匹配两个给定的矢量2like对象的 x/y 坐标。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| start | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 任何具有公共`x`和`y`属性的天体,其值将被指定为本行的x1/y1组件. |
| end | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 任何具有公共`x`和`y`属性的天体,其值将被指定为本行的x2/y2组件. |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 此线对象 。


> 源码：[src/geom/line/Line.js#L184](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L184)  
引入版本：3.70.0


---

### setTo {#setTo}

#### \<instance> setTo([x1], [y1], [x2], [y2]) {#instance-settox1-y1-x2-y2}


**说明:**

设置线端点的新坐标 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x1 | number | 是 | 0 | 线路起点的x坐标. |
| y1 | number | 是 | 0 | 线路起点的y坐标. |
| x2 | number | 是 | 0 | 线路终点的x坐标. |
| y2 | number | 是 | 0 | 线的终点的y坐标. |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 此线对象 。


> 源码：[src/geom/line/Line.js#L155](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L155)  
引入版本：3.0.0


---

### SetToAngle {#SetToAngle}

#### \<static> SetToAngle(line, x, y, angle, length) {#static-settoangleline-x-y-angle-length}


**说明:**

设置一条线到给定的位置、角度和长度。

**标签:**

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


---

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


---

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


---

## 公开成员 {#public-members}

### bottom {#bottom}

#### bottom: number {#bottom-number}


**说明:**

本行最下端的y坐标, 即 `y1` 和 `y2` 的坐标越大。 当设定时, 当前持有较大y值的终点移动到新位置 。


> 源码：[src/geom/line/Line.js#L335](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L335)  
引入版本：3.0.0


---

### left {#left}

#### left: number {#left-number}


**说明:**

此线的左- 最左坐标, 即 `x1` 和 `x2` 的下坐标。 设定时, 当前持有较小的 x 值的终点移动到新位置 。


> 源码：[src/geom/line/Line.js#L248](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L248)  
引入版本：3.0.0


---

### right {#right}

#### right: number {#right-number}


**说明:**

本线最右侧的x坐标, 即 `x1` 和 `x2` 的坐标越大。 当设定时, 当前持有较大x值的终点将移到新位置 。


> 源码：[src/geom/line/Line.js#L277](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L277)  
引入版本：3.0.0


---

### top {#top}

#### top: number {#top-number}


**说明:**

本行最上方的y坐标, 即 `y1` 和 `y2` 的坐标越小。 当设定时, 当前持有较小 y 值的终点将移到新位置 。


> 源码：[src/geom/line/Line.js#L306](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L306)  
引入版本：3.0.0


---

### type {#type}

#### type: number {#type-number}


**说明:**

此对象的几何常数类型: `GEOM_CONST.LINE`. 用于快速类型比较.


> 源码：[src/geom/line/Line.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L47)  
引入版本：3.19.0


---

### x1 {#x1}

#### x1: number {#x1-number}


**说明:**

线路起点的x坐标.


> 源码：[src/geom/line/Line.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L58)  
引入版本：3.0.0


---

### x2 {#x2}

#### x2: number {#x2-number}


**说明:**

线路终点的x坐标.


> 源码：[src/geom/line/Line.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L76)  
引入版本：3.0.0


---

### y1 {#y1}

#### y1: number {#y1-number}


**说明:**

线路起点的y坐标.


> 源码：[src/geom/line/Line.js#L67](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L67)  
引入版本：3.0.0


---

### y2 {#y2}

#### y2: number {#y2-number}


**说明:**

线的终点的y坐标.


> 源码：[src/geom/line/Line.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/line/Line.js#L85)  
引入版本：3.0.0


---

---
