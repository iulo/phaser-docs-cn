# Curve {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/curves-curve)

一个基曲面类,所有其他曲线类型都延伸.

一个曲线代表了通过2D空间的数学路径,提供了采样点,计算弧长,并沿它获得切向量的方法. 曲线是`Phaser.Curves.Path`的构件,它允许游戏对象通过一个场景遵循复杂的路线.

本类并非直接用即时处理。 `Phaser.Curves` 命名空间, 例如 `LineCurve`, `QuadraticBezier`, `CubicBezier`, `EllipseCurve`,或 ,或 , `SplineCurve`.

基于 [zz85](http://www.lab4games.net/zz85/blog) 创建的三门Js曲线课

**构造函数**

`new Curve(type)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 类型 | string | 否 | 曲线类型. |

---


**作用域**: static

> 源码：[src/curves/Curve.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L12)  
引入版本：3.0.0

## 公开成员 {#public-members}

### active {#active}

#### active: boolean {#active-boolean}


**说明:**

对于路径上的曲线,`false`表示路径会忽略这个曲线.


> 源码：[src/curves/Curve.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L89)  
引入版本：3.0.0


---

### arcLengthDivisions {#arcLengthDivisions}

#### arcLengthDivisions: number {#arclengthdivisions-number}


**说明:**

曲线内弧长的分数。


> 源码：[src/curves/Curve.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L59)  
引入版本：3.0.0


---

### cacheArcLengths {#cacheArcLengths}

#### cacheArcLengths: Array.\<number> {#cachearclengths-arraynumber}


**说明:**

缓存弧长度值阵列 。


> 源码：[src/curves/Curve.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L69)  
引入版本：3.0.0


---

### defaultDivisions {#defaultDivisions}

#### defaultDivisions: number {#defaultdivisions-number}


**说明:**

曲线内默认的分区数 。


> 源码：[src/curves/Curve.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L49)  
引入版本：3.0.0


---

### needsUpdate {#needsUpdate}

#### needsUpdate: boolean {#needsupdate-boolean}


**说明:**

此曲线的数据是否需要更新?


> 源码：[src/curves/Curve.js#L79](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L79)  
引入版本：3.0.0


---

### type {#type}

#### type: string {#type-string}


**说明:**

曲线类型的字符串标识符。


> 源码：[src/curves/Curve.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L40)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### draw {#draw}

#### \<instance> draw(graphics, [pointsTotal]) {#instance-drawgraphics-pointstotal}


**说明:**

在给定的图形对象上绘制此曲线。

曲线是使用 `Graphics.strokePoints` 绘制的, 所以无论当前图形的描边颜色是什么, 都会绘制。 图形对象在绘图前没有清除, 因此曲线会出现在其他已显示对象的上方 。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 |  | 绘制此曲线的图形实例 。 |
| pointsTotal | number | 是 | 32 | 曲线的分辨率。 其产生的值越高, 其产生的光滑度就越高, 其代价就是渲染性能。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 曲线绘制对象的图形。


> 源码：[src/curves/Curve.js#L120](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L120)  
引入版本：3.0.0


---

### getBounds {#getBounds}

#### \<instance> getBounds([out], [accuracy]) {#instance-getboundsout-accuracy}


**说明:**

返回一个矩形,其中位置和维度与此曲线的界限相匹配。

您可以控制界限的准确性。 给出的值用于绘制曲线的几点。 更高的值在计算速度上更准确 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 |  | 将界限存储到的矩形。 如果错误, 将创建新对象 。 |
| accuracy | number | 是 | 16 | 界限计算精度. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 矩形天体持有此曲线的界限。 如果给它 `out` , 则它就是此天体 。


> 源码：[src/curves/Curve.js#L144](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L144)  
引入版本：3.0.0


---

### getDistancePoints {#getDistancePoints}

#### \<instance> getDistancePoints(distance) {#instance-getdistancepointsdistance}


**说明:**

返回一个点数组, 将 X 距离像素分开。 距离越小, 数组就越大 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| distance | number | 否 | 沿曲线的每个点之间的距离,以像素表示. |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 矢量2天体阵列。


> 源码：[src/curves/Curve.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L178)  
引入版本：3.0.0


---

### getEndPoint {#getEndPoint}

#### \<instance> getEndPoint([out]) {#instance-getendpointout}


**说明:**

得到曲线末端的点数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 可选矢量对象存储结果 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 含有曲线终点坐标的矢量2.


> 源码：[src/curves/Curve.js#L198](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L198)  
引入版本：3.0.0


---

### getLength {#getLength}

#### \<instance> getLength() {#instance-getlength}


**说明:**

返回曲线的弧总长度,以像素为单位。长度是通过对曲线沿线取样点之间的距离进行相互比较计算出来的。


**返回值:** number - 曲线的总长度.


> 源码：[src/curves/Curve.js#L215](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L215)  
引入版本：3.0.0


---

### getLengths {#getLengths}

#### \<instance> getLengths([divisions]) {#instance-getlengthsdivisions}


**说明:**

获得累积段长列表.

这些长度是计算和缓存的,这是第一次使用这种方法.

- [0] 0

- [1] 第一部分

- [2] 第一和第二部分

- ...

- [司 所有部分

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| divisions | number | 是 | 师或段数. |


**返回值:** Array.\<number> - 累积长度的数组 。


> 源码：[src/curves/Curve.js#L231](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L231)  
引入版本：3.0.0


---

### getPointAt {#getPointAt}

#### \<instance> getPointAt(u, [out]) {#instance-getpointatu-out}


**说明:**

得到曲线上相对位置的点,以弧长表示.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| u | number | 否 | 相对位置, [0. 1]. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 将结果存储在其中的一点. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 关键是...


> 源码：[src/curves/Curve.js#L287](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L287)  
引入版本：3.0.0


---

### getPoints {#getPoints}

#### \<instance> getPoints([divisions], [stepRate], [out]) {#instance-getpointsdivisions-steprate-out}


**说明:**

从曲线中获取一个均匀的点序列.

你可以通过`divisions`,`stepRate`,或者两个都不通过.

师数将.

1. `divisions`,如果 `divisions` > 0;或 单倍径

2. `this.getLength / stepRate`,如果 `stepRate` > 0;或 单倍径

3. `this.defaultDivisions`

将返回`1 + divisions`点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| divisions | number | 是 | 师拟制之数. |
| stepRate | number | 是 | 点之间的曲线距离,暗示`divisions`. |
| out | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 将点数存储到的可选数组 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 曲线上的一阵矢量2点.


> 源码：[src/curves/Curve.js#L309](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L309)  
引入版本：3.0.0


---

### getRandomPoint {#getRandomPoint}

#### \<instance> getRandomPoint([out]) {#instance-getrandompointout}


**说明:**

从曲线中获取随机点.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 存储结果的点对象 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 关键是...


> 源码：[src/curves/Curve.js#L358](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L358)  
引入版本：3.0.0


---

### getSpacedPoints {#getSpacedPoints}

#### \<instance> getSpacedPoints([divisions], [stepRate], [out]) {#instance-getspacedpointsdivisions-steprate-out}


**说明:**

从曲线中获取一个等距点的序列(通过弧距离)。

将返回`1 + divisions`点。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| divisions | number | 是 | "this.defaultDivisions" | 师拟制之数. |
| stepRate | number | 是 |  | 点间步数。 用于计算分区变弱时返回的点数。 如果分区为正数, 则忽略 。 |
| out | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 |  | 将点数存储到的可选数组 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 一系列矢量2分数.


> 源码：[src/curves/Curve.js#L379](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L379)  
引入版本：3.0.0


---

### getStartPoint {#getStartPoint}

#### \<instance> getStartPoint([out]) {#instance-getstartpointout}


**说明:**

曲线起始处获得点数.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 将结果存储在其中的一点. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 关键是...


> 源码：[src/curves/Curve.js#L420](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L420)  
引入版本：3.0.0


---

### getTangent {#getTangent}

#### \<instance> getTangent(t, [out]) {#instance-gettangentt-out}


**说明:**

在曲线上相对位置获得单位矢量正切。 如果子类不使用分析正切导出来覆盖这种方法, 则正切值大致为将小三角形分开两个点取样, 并计算它们之间正常方向向量。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 曲线上的相对位置, [0. 1]. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 存储结果的向量 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 矢量近似于点t的正线(德尔塔+/-0.0001)


> 源码：[src/curves/Curve.js#L439](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L439)  
引入版本：3.0.0


---

### getTangentAt {#getTangentAt}

#### \<instance> getTangentAt(u, [out]) {#instance-gettangentatu-out}


**说明:**

在曲线的相对位置上,按弧长得到一个单位矢量正切值。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| u | number | 否 | 曲线上的相对位置, [0. 1]. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 存储结果的向量 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 切向量.


> 源码：[src/curves/Curve.js#L481](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L481)  
引入版本：3.0.0


---

### getTFromDistance {#getTFromDistance}

#### \<instance> getTFromDistance(distance, [divisions]) {#instance-gettfromdistancedistance-divisions}


**说明:**

鉴于曲线上以像素表示的距离,返回相应的T参数值,该参数值可用于`getPoint()`,以找到该距离的位置。这可以使您在曲线上得到等距点。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| distance | number | 否 | 距离,以像素计. |
| divisions | number | 是 | 分数可选. |


**返回值:** number - 曲线上给定距离的 t 值( 0 到 1 之间) 。


> 源码：[src/curves/Curve.js#L501](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L501)  
引入版本：3.0.0


---

### getUtoTmapping {#getUtoTmapping}

#### \<instance> getUtoTmapping(u, distance, [divisions]) {#instance-getutotmappingu-distance-divisions}


**说明:**

将一个统一的参数u(0至1,以弧长均匀分布)映射到原始曲线参数t。这种映射确保了在u的定期间隔中取样的点将沿着曲线相当远,与原始参数t不同,该参数可能产生不均衡的间隔。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| u | number | 否 | 浮在0到1之间 |
| distance | number | 否 | 距离,以像素计. |
| divisions | number | 是 | 分数可选. |


**返回值:** number - 等距离值 。


> 源码：[src/curves/Curve.js#L522](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L522)  
引入版本：3.0.0


---

### updateArcLengths {#updateArcLengths}

#### \<instance> updateArcLengths() {#instance-updatearclengths}


**说明:**

计算和缓存弧长度 。


> 源码：[src/curves/Curve.js#L603](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/Curve.js#L603)  
引入版本：3.0.0


---

---
