# Path {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/curves-path)

路径将多个曲线组合为一个连续复合曲线。它可以包含任意类型的任意数量的曲线,包括 Line, Bezier, Ellipse,和 Spline 曲线。路径通常在 Phaser 中用于定义游戏对象遵循的路径,或者通过路径跟踪器组件,或者通过路径沿线的采样点来驱动Tween或自定义的运动逻辑。

路径中的曲线不必在前面的曲线结束的地方开始,也就是说,路径不一定是不间断的曲线。只有路径的顺序会影响路径上的实际点。

**构造函数**

`new Path([x], [y])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 路径起点的X坐标或QQlink Phaser.Types.Curves.JSONPath}. |
| y | number | 是 | 0 | 路径起点的Y坐标. |

---


**作用域**: static

> 源码：[src/curves/path/Path.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L21)  
引入版本：3.0.0

## 公开成员 {#public-members}

### autoClose {#autoClose}

#### autoClose: boolean {#autoclose-boolean}


**说明:**

自动关闭路径 。


> 源码：[src/curves/path/Path.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L91)  
引入版本：3.0.0


---

### cacheLengths {#cacheLengths}

#### cacheLengths: Array.\<number> {#cachelengths-arraynumber}


**说明:**

路径中每个曲线的缓存长度 。

内部使用[#getCurveLengths](#getCurveLengths).


> 源码：[src/curves/path/Path.js#L79](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L79)  
引入版本：3.0.0


---

### curves {#curves}

#### curves: Array.\<[Phaser.Curves.Curve](/api/class/curves-curve)> {#curves-arrayphasercurvescurve}


**说明:**

构成此路径的曲线列表 。


> 源码：[src/curves/path/Path.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L69)  
引入版本：3.0.0


---

### defaultDivisions {#defaultDivisions}

#### defaultDivisions: number {#defaultdivisions-number}


**说明:**

曲线内默认的分区数 。


> 源码：[src/curves/path/Path.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L59)  
引入版本：3.70.0


---

### name {#name}

#### name: string {#name-string}


**说明:**

此路径的名称。 默认情况下是空的, 并且从未被 Phaser 所覆盖, 留给开发者使用 。


> 源码：[src/curves/path/Path.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L48)  
引入版本：3.0.0


---

### startPoint {#startPoint}

#### startPoint: [Phaser.Math.Vector2](/api/class/math-vector2) {#startpoint-phasermathvector2}


**说明:**

路径的起点.

这不一定等同于路径中第一个曲线的起点,在空路径中,它也被当作终点.


> 源码：[src/curves/path/Path.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L101)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(curve) {#instance-addcurve}


**说明:**

将曲线附加到路径的末尾。

曲线不必从路径结束的地方开始,对于空路径,也不必从它确定的起点开始。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| curve | [Phaser.Curves.Curve](/api/class/curves-curve) | 否 | 曲线到附件。 |


**返回值:** [Phaser.Curves.Path](/api/class/curves-path) - 此路径对象 。


> 源码：[src/curves/path/Path.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L142)  
引入版本：3.0.0


---

### circleTo {#circleTo}

#### \<instance> circleTo(radius, [clockwise], [rotation]) {#instance-circletoradius-clockwise-rotation}


**说明:**

创建路径末端的圆形椭圆曲线。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| radius | number | 否 |  | 圆之半径. |
| clockwise | boolean | 是 | false | `true`用来创建顺时针圆,而不是逆时针圆. |
| rotation | number | 是 | 0 | 圆圈的旋转以度数为单位. |


**返回值:** [Phaser.Curves.Path](/api/class/curves-path) - 此路径对象 。


> 源码：[src/curves/path/Path.js#L161](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L161)  
引入版本：3.0.0


---

### closePath {#closePath}

#### \<instance> closePath() {#instance-closepath}


**说明:**

确保路径关闭 。

关闭路径在同一点开始和结束。 如果路径没有关闭, 则会从终点直接创建直线曲线到起始点。 在检查过程中, 路径的实际起点, 即第一个曲线的起点, 将会被使用, 而不是路径定义的 [startPoint](https://phaser.io/oss/docs/api-documentation/class/startPoint.md), 可能有所不同 。

在空路径上调用这种方法将导致错误 。


**返回值:** [Phaser.Curves.Path](/api/class/curves-path) - 此路径对象 。


> 源码：[src/curves/path/Path.js#L180](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L180)  
引入版本：3.0.0


---

### cubicBezierTo {#cubicBezierTo}

#### \<instance> cubicBezierTo(x, y, control1X, [control1Y], [control2X], [control2Y]) {#instance-cubicbeziertox-y-control1x-control1y-control2x-control2y}


**说明:**

创建一个立方贝塞尔曲线,从上一端点开始,到p3结束,使用p1和p2作为控制点.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number \| [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 终点的 x 坐标。 或者, 如果是矢量2, p1 值 。 |
| y | number \| [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 终点的y坐标。或者,如果是矢量2,则表示p2值。 |
| control1X | number \| [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 第一个控制点的x坐标。或者,如果是矢量2,则表示p3值。 |
| control1Y | number | 是 | 第一个控制点的y坐标。 如果提供了矢量2作为前3个参数,则不使用。 |
| control2X | number | 是 | 第二个控制点的 x 坐标。 如果提供了矢量2s作为前3 个参数, 则不使用 。 |
| control2Y | number | 是 | 第二个控制点的y坐标。如果向量2s作为前3个参数提供,则不使用。 |


**返回值:** [Phaser.Curves.Path](/api/class/curves-path) - 此路径对象 。


> 源码：[src/curves/path/Path.js#L207](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L207)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

处理此路径, 清除其内部对对象的引用, 以便它们可以被垃圾收集 。


> 源码：[src/curves/path/Path.js#L897](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L897)  
引入版本：3.0.0


---

### draw {#draw}

#### \<instance> draw(graphics, [pointsTotal]) {#instance-drawgraphics-pointstotal}


**说明:**

在图形游戏对象的路径中绘制全部曲线。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 |  | 要绘制的图形游戏对象 。 |
| pointsTotal | number | 是 | 32 | 每个曲线的绘图点数。 数字越多, 曲线越平滑, 需要更多的处理 。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 绘制到的图形对象 。


> 源码：[src/curves/path/Path.js#L282](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L282)  
引入版本：3.0.0


---

### ellipseTo {#ellipseTo}

#### \<instance> ellipseTo([xRadius], [yRadius], [startAngle], [endAngle], [clockwise], [rotation]) {#instance-ellipsetoxradius-yradius-startangle-endangle-clockwise-rotation}


**说明:**

使用给定参数创建位于上一个终点的椭圆曲线。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| xRadius | number | 是 | 0 | 椭圆的横向半径. |
| yRadius | number | 是 | 0 | 椭圆的垂直半径. |
| startAngle | number | 是 | 0 | 椭圆的起始角,以度计. |
| endAngle | number | 是 | 360 | 椭圆的端角,以度计. |
| clockwise | boolean | 是 | false | 椭圆角是按顺时针(`true`)还是逆时针(`false`)给出的. |
| rotation | number | 是 | 0 | 椭圆的旋转,以度数表示. |


**返回值:** [Phaser.Curves.Path](/api/class/curves-path) - 此路径对象 。


> 源码：[src/curves/path/Path.js#L312](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L312)  
引入版本：3.0.0


---

### fromJSON {#fromJSON}

#### \<instance> fromJSON(data) {#instance-fromjsondata}


**说明:**

从路径配置对象创建路径。

提供的对象应为[Phaser.Types.Curves.JSONPath](/api/typedef/types-curves#jsonpath), 由[#toJSON](#toJSON)返回。 提供一个畸形的对象可能会产生错误 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | [Phaser.Types.Curves.JSONPath](/api/typedef/types-curves#jsonpath) | 否 | JSON 对象包含路径数据 。 |


**返回值:** [Phaser.Curves.Path](/api/class/curves-path) - 此路径对象 。


> 源码：[src/curves/path/Path.js#L344](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L344)  
引入版本：3.0.0


---

### getBounds {#getBounds}

#### \<instance> getBounds([out], [accuracy]) {#instance-getboundsout-accuracy}


**说明:**

返回一个矩形,其位置和大小与此路径的界限相符。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 |  | 矩形以存储界限. |
| accuracy | number | 是 | 16 | 边界计算准确性。 较高的数值在计算速度上更为准确 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 修改后的 `out` 矩形,或者如果没有提供新的矩形。


> 源码：[src/curves/path/Path.js#L398](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L398)  
引入版本：3.0.0


---

### getCurveAt {#getCurveAt}

#### \<instance> getCurveAt(t) {#instance-getcurveatt}


**说明:**

返回在给定的正态位置( 0 和 1 之间) 构成路径的曲线 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 路径上正常位置, 0 到 1 之间 。 |


**返回值:** [Phaser.Curves.Curve](/api/class/curves-curve) - 指定位置的路径部分, 或如果没有找到曲线, 则 `null` 。


> 源码：[src/curves/path/Path.js#L484](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L484)  
引入版本：3.60.0


---

### getCurveLengths {#getCurveLengths}

#### \<instance> getCurveLengths() {#instance-getcurvelengths}


**说明:**

返回每个曲线末端含有路径长度的数组。

此方法的结果会被缓存以避免在后续调用中重新计算它. 缓存只有在[#curves](#curves)阵列的长度变化时才会被无效,如果路径中的曲线被更改,或者曲线被移除,另一个被替换时才被取消.


**返回值:** Array.\<number> - 包含路径长度的阵列,位于其曲线的每个端。


> 源码：[src/curves/path/Path.js#L447](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L447)  
引入版本：3.0.0


---

### getEndPoint {#getEndPoint}

#### \<instance> getEndPoint([out]) {#instance-getendpointout}


**说明:**

返回路径的终点。

一个路径的终点相当于路径中最后一个曲线的终点。对于一个空路径,终点位于路径定义的[#startPoint](#startPoint)。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 存储点的对象 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 修改后的 `out` 对象,或者如果没有提供新的矢量2。


> 源码：[src/curves/path/Path.js#L513](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L513)  
引入版本：3.0.0


---

### getLength {#getLength}

#### \<instance> getLength() {#instance-getlength}


**说明:**

返回路径的全长 。


**返回值:** number - 路径的总长度 。


> 源码：[src/curves/path/Path.js#L543](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L543)  
引入版本：3.0.0


---

### getPoint {#getPoint}

#### \<instance> getPoint(t, [out]) {#instance-getpointt-out}


**说明:**

计算路径上给定的正态位置(0至1之间)的点坐标。

位置相对于整个路径,而不是单个曲线。 0. 5 的位置总是位于路径中间, 从而与其起点和终点相距相当。 在一条路径中, 它会位于曲线中间; 在一条路径中, 有两个曲线, 它可能随其长度而出现在其中任何一个位置。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 返回点的位置,在0到1之间. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 存储计算点的对象。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 修改 `out` 对象,或新对象 `Vector2` ,如果没有提供。


> 源码：[src/curves/path/Path.js#L569](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L569)  
引入版本：3.0.0


---

### getPoints {#getPoints}

#### \<instance> getPoints([divisions], [stepRate]) {#instance-getpointsdivisions-steprate}


**说明:**

获得路径的顺序点数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| divisions | number | 是 | 每个曲线的分辨率要划分的分区数。 |
| stepRate | number | 是 | 每条曲线的点之间的曲线距离,暗示`divisions`. |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 含有路径沿线点的矢量2天体阵列。


> 源码：[src/curves/path/Path.js#L612](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L612)  
引入版本：3.0.0


---

### getRandomPoint {#getRandomPoint}

#### \<instance> getRandomPoint([out]) {#instance-getrandompointout}


**说明:**

返回路径中任意选择的点。 这遵循与 `getPoint` 相同的规则, 因为它可能返回路径中任意曲线上的点 。

在多次调用这种方法时,不保证各点在空间上相等.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储结果的 `Vector2` 实例。 如果 `undefined` 将创建新的 `Vector2` 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 修改 `out` 对象,或新对象 `Vector2` ,如果没有提供。


> 源码：[src/curves/path/Path.js#L671](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L671)  
引入版本：3.0.0


---

### getSpacedPoints {#getSpacedPoints}

#### \<instance> getSpacedPoints([divisions]) {#instance-getspacedpointsdivisions}


**说明:**

将此路径分割为一组等距点。

由此得出的点数在点数在路径上的位置上具有同等的间距,但不一定在空间上具有同等的间距.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| divisions | number | 是 | 40 | 将此路径分割成的点数 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 这条路径的点列表又细分为几个点.


> 源码：[src/curves/path/Path.js#L692](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L692)  
引入版本：3.0.0


---

### getStartPoint {#getStartPoint}

#### \<instance> getStartPoint([out]) {#instance-getstartpointout}


**说明:**

返回路径的起点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储结果的 `Vector2` 实例。 如果 `undefined` 将创建新的 `Vector2` 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 修改后的 `out` 对象,或者如果没有提供新的矢量2。


> 源码：[src/curves/path/Path.js#L723](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L723)  
引入版本：3.0.0


---

### getTangent {#getTangent}

#### \<instance> getTangent(t, [out]) {#instance-gettangentt-out}


**说明:**

获得路径上相对位置的单位矢量正切值。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 路径上的相对位置, [0. 1]. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 存储结果的向量 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 矢量近似于点t的正线(德尔塔+/-0.0001)


> 源码：[src/curves/path/Path.js#L742](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L742)  
引入版本：3.23.0


---

### lineTo {#lineTo}

#### \<instance> lineTo(x, [y]) {#instance-linetox-y}


**说明:**

从上一个端点创建到x/y的线条曲线。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number \| [Phaser.Math.Vector2](/api/class/math-vector2) | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 线端的X坐标,或包含整个端点的`Vector2` / `Vector2Like`. |
| y | number | 是 | 线的终点的Y坐标,如果一个数字作为X参数被传递. |


**返回值:** [Phaser.Curves.Path](/api/class/curves-path) - 此路径对象 。


> 源码：[src/curves/path/Path.js#L782](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L782)  
引入版本：3.0.0


---

### moveTo {#moveTo}

#### \<instance> moveTo(x, [y]) {#instance-movetox-y}


**说明:**

从路径当前终点到给定坐标,在此路径中创建“gap”。

调用此函数后,此路径的终点将等于给定坐标.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number \| [Phaser.Math.Vector2](/api/class/math-vector2) | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 将路径的终点移动到位置的X坐标,或包含整个新终点的`Vector2` / `Vector2Like`. |
| y | number | 是 | 如果一个数字作为X坐标通过,则移动路径终点的位置的Y坐标. |


**返回值:** [Phaser.Curves.Path](/api/class/curves-path) - 此路径对象 。


> 源码：[src/curves/path/Path.js#L830](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L830)  
引入版本：3.0.0


---

### quadraticBezierTo {#quadraticBezierTo}

#### \<instance> quadraticBezierTo(x, [y], [controlX], [controlY]) {#instance-quadraticbeziertox-y-controlx-controly}


**说明:**

创建一条从路径终点开始的四方贝塞尔曲线。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number \| Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 否 | 第二个控制点的X坐标,或者,如果是`Vector2`,第一个控制点. |
| y | number | 是 | 第二控制点的Y坐标,或者,如果`x`是`Vector2`,那么是第二控制点. |
| controlX | number | 是 | 如果`x`不是`Vector2`,则第一个控制点的X坐标. |
| controlY | number | 是 | 如果`x`不是`Vector2`,则第一个控制点的Y坐标. |


**返回值:** [Phaser.Curves.Path](/api/class/curves-path) - 此路径对象 。


> 源码：[src/curves/path/Path.js#L248](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L248)  
引入版本：3.2.0


---

### splineTo {#splineTo}

#### \<instance> splineTo(points) {#instance-splinetopoints}


**说明:**

使用曲线上的指定点创建一条从上一个终点开始的线条曲线。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| points | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 否 | 新创建的线条曲线应该包括的点。 |


**返回值:** [Phaser.Curves.Path](/api/class/curves-path) - 此路径对象 。


> 源码：[src/curves/path/Path.js#L813](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L813)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

将此路径转换为包含路径信息及其组成曲线的 JSON 对象。


**返回值:** [Phaser.Types.Curves.JSONPath](/api/typedef/types-curves#jsonpath) - 包含此路径数据的 JSON 对象 。


> 源码：[src/curves/path/Path.js#L855](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L855)  
引入版本：3.0.0


---

### updateArcLengths {#updateArcLengths}

#### \<instance> updateArcLengths() {#instance-updatearclengths}


**说明:**

清除缓存的弧长, 并强制它们根据下一次调用[#getCurveLengths](#getCurveLengths)或任何依赖于它的方法进行重新计算。 如果您在此路径中修改了曲线, 则使用此选项, 因为缓存只在曲线数变化时自动失效 。


> 源码：[src/curves/path/Path.js#L881](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L881)  
引入版本：3.0.0


---

---
