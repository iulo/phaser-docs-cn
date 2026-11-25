# Phaser.Geom.Intersects {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/geom-intersects)

Scope: 
static
> 源码：[src/geom/intersects/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/index.js#L7)  


## 静态函数 {#static-functions}

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


---

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


---

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


---

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


---

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


---

### GetLineToLine {#GetLineToLine}

#### \<static> GetLineToLine(line1, line2, [isRay], [out]) {#static-getlinetolineline1-line2-isray-out}


**说明:**

检查两条线段之间的交叉,或一条线段和一条线段,如果两条线平行,或不交叉,则返回作为矢量3的交叉点,或`null`.

矢量3的`z`属性包含参数的`t`值(0到1之间的一个标尺),代表着`line1`的交汇点发生多远,可用于排序或比较多个交叉结果,从一组线段找到最接近的交叉点.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| line1 | [Phaser.Geom.Line](/api/class/geom-line) | 否 |  | 第一条线段,或一线,以检查. |
| line2 | [Phaser.Geom.Line](/api/class/geom-line) | 否 |  | 第二行段要检查. |
| isRay | boolean | 是 | false | `line1`是射线还是线段? |
| out | [Phaser.Math.Vector3](/api/class/math-vector3) | 是 |  | 用于存储交叉结果的矢量3。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 矢量3 位于何处 `x` 财务报告和已审计财务报表 `y` 是一个交点坐标, `z` 参数 `t` 沿边值 `line1`,或 ,或 , `null` 如果线不交叉。


> 源码：[src/geom/intersects/GetLineToLine.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetLineToLine.js#L9)  
引入版本：3.50.0


---

### GetLineToPoints {#GetLineToPoints}

#### \<static> GetLineToPoints(line, points, [isRay], [out]) {#static-getlinetopointsline-points-isray-out}


**说明:**

检查线段和数点之间最接近的交叉点,每对连续的点被转换成线段进行交叉测试。该数组被作为封闭形状处理,这意味着最后一个点被连接回第一点。

如果没有找到交叉点,此函数返回 `null` 。

如果找到交叉点, 返回一个矢量3, 其属性如下:

`x`和`y`组件包含交汇点,`z`组件包含最近的距离.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 |  | 线段,或射线,以检查。如果有射线,则将 `isRay` 参数设置为 `true` 。 |
| points | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> \| Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 否 |  | 一系列要检查的点 。 |
| isRay | boolean | 是 | false | `line`是射线还是线段? |
| out | [Phaser.Math.Vector3](/api/class/math-vector3) | 是 |  | 用于存储交叉结果的矢量3。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 含有交叉结果的矢量3,或`null`.


> 源码：[src/geom/intersects/GetLineToPoints.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetLineToPoints.js#L17)  
引入版本：3.50.0


---

### GetLineToPolygon {#GetLineToPolygon}

#### \<static> GetLineToPolygon(line, polygons, [isRay], [out]) {#static-getlinetopolygonline-polygons-isray-out}


**说明:**

检查线段与多边形阵列之间最接近的交汇点。

如果没有找到交叉点,此函数返回 `null` 。

如果找到交叉点, 返回一个矢量4, 其属性如下:

`x`和`y`组件包含交汇点. `z`组件包含最近的距离. `w`组件包含特定阵列中触发交汇的多边形索引.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 |  | 线段,或射线,以检查。如果有射线,则将 `isRay` 参数设置为 `true` 。 |
| polygons | [Phaser.Geom.Polygon](/api/class/geom-polygon) \| Array.\<[Phaser.Geom.Polygon](/api/class/geom-polygon)> | 否 |  | 要检查的是一个单一的多边形, 或多边形的数组 。 |
| isRay | boolean | 是 | false | `line`是射线还是线段? |
| out | [Phaser.Math.Vector4](/api/class/math-vector4) | 是 |  | 用于存储交叉结果的矢量4。 |


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 含有交点结果的矢量4,或`null`.


> 源码：[src/geom/intersects/GetLineToPolygon.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/GetLineToPolygon.js#L14)  
引入版本：3.50.0


---

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


---

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


---

### GetRectangleIntersection {#GetRectangleIntersection}

#### \<static> GetRectangleIntersection(rectA, rectB, [output]) {#static-getrectangleintersectionrecta-rectb-output}


**说明:**

检查两个矩形是否交叉,并返回此交叉点的区域为矩形对象.

如果省略了可选的 `output` 参数,则创建并返回新的矩形对象。如果有交叉,则包含交叉区域。如果没有交叉,则将变为空矩形(所有值设定为零)。

如果矩形物体作为`output`传递,并且有交叉点,则会将交叉区数据加载到其中并返回。如果没有交叉点,则不作任何修改。

**标签:**

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


---

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


---

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


---

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


---

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


---

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


---

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


---

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


---

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


---

### PointToLine {#PointToLine}

#### \<static> PointToLine(point, line, [lineThickness]) {#static-pointtolinepoint-line-linethickness}


**说明:**

检查一个点是否在一线的两个端点之间落下,根据给定的线厚度.

假设线端点是圆形的,而不是方形的.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) \| any | 否 |  | 点,或类似点的物体来检查. |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 |  | 测试交汇点的线段开始. |
| lineThickness | number | 是 | 1 | 线厚度,假设线端点是圆形的. |


**返回值:** boolean - 如果点落到线上,则`true`,否则则`false`.


> 源码：[src/geom/intersects/PointToLine.js#L8](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/intersects/PointToLine.js#L8)  
引入版本：3.0.0


---

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


---

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


---

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


---

### RectangleToValues {#RectangleToValues}

#### \<static> RectangleToValues(rect, left, right, top, bottom, [tolerance]) {#static-rectangletovaluesrect-left-right-top-bottom-tolerance}


**说明:**

检查矩形是否与由明确的左、右、上和下边界值定义的区域相交。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
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


---

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


---

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


---

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


---

---
