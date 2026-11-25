# Triangle {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/geom-triangle)

三角形是一个由2D空间中三个顶点定义的封闭多边形,可用于命中测试,定义产卵区或触发区,以及几何计算。它只是一个几何对象,而不是一个游戏对象,不能直接渲染。要画三角形到屏幕,请把它传递给图形游戏对象的`strokeTriangleShape`或`fillTriangleShape`方法。

三个顶点作为坐标对储存(`x1`,`y1`), (`x2`,`y2`)和(a)`x3`,`y3`。所有坐标默认为 `0` 提供时不提供。

**构造函数**

`new Triangle([x1], [y1], [x2], [y2], [x3], [y3])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x1 | number | 是 | 0 | `x` 坐标为第一点。 |
| y1 | number | 是 | 0 | `y` 坐标为第一点。 |
| x2 | number | 是 | 0 | 第二点的`x`坐标. |
| y2 | number | 是 | 0 | 第二点的`y`坐标. |
| x3 | number | 是 | 0 | `x` 第三点的坐标。 |
| y3 | number | 是 | 0 | `y` 第三点的坐标。 |

---


**作用域**: static

> 源码：[src/geom/triangle/Triangle.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L15)  
引入版本：3.0.0

## 公开方法 {#public-methods}

### Area {#Area}

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


---

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


---

### BuildFromPolygon {#BuildFromPolygon}

#### \<static> BuildFromPolygon(data, [holes], [scaleX], [scaleY], [out]) {#static-buildfrompolygondata-holes-scalex-scaley-out}


**说明:**

然后返回三角形的数组,其中给定的顶点已分解成一系列三角形。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| data | array | 否 |  | 平坦的顶点数组坐标,如 [x0,y0, x1,y1, x2,y2,...] |
| holes | array | 是 | null | 12个顶点输入的孔指数(如[5,8])是指一个顶点5-7的孔,另一个顶点8-11的孔。 |
| scaleX | number | 是 | 1 | 水平比例系数将结果的点乘以。 |
| scaleY | number | 是 | 1 | 垂直比例系数,将产生的点乘以。 |
| out | array \| Array.\<[Phaser.Geom.Triangle](/api/class/geom-triangle)> | 是 |  | 一个将三角形实例存储到其中的数组。 如果不提供, 则会创建新数组 。 |


**返回值:** array, Array.\<[Phaser.Geom.Triangle](/api/class/geom-triangle)> - 三角形实例的阵列,每个三角形都基于已分解的顶点数据.


> 源码：[src/geom/triangle/BuildFromPolygon.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/BuildFromPolygon.js#L10)  
引入版本：3.0.0


---

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


---

### CenterOn {#CenterOn}

#### \<static> CenterOn(triangle, x, y, [centerFunc]) {#static-centerontriangle-x-y-centerfunc}


**说明:**

定位三角,使其以给定坐标为中心。

**标签:**

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


---

### Centroid {#Centroid}

#### \<static> Centroid(triangle, [out]) {#static-centroidtriangle-out}


**说明:**

计算三角形的半人马体的位置,它也是其质量中心(重力中心).

中间体是其三个中位数(从顶点到对面的两段线)在三角交汇的点,它以2:1的比例将每个中间体分成.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角形用来使用. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储坐标的矢量2对象 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - `out`对象具有修改后的`x`和`y`属性,或者如果没有提供新的矢量2.


> 源码：[src/geom/triangle/Centroid.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Centroid.js#L9)  
引入版本：3.0.0


---

### CircumCenter {#CircumCenter}

#### \<static> CircumCenter(triangle, [out]) {#static-circumcentertriangle-out}


**说明:**

计算三角形的圆形,环形是环形圆形的中心,是穿过三角形的所有三个顶点的独特圆形,也是三角形两侧垂直两段的常见交点,也是与三角形的所有三个顶部具有等距离的唯一点.

改编自 [http://bjornharrtell.github.io/jsts/doc/api/jsts_geom_Triangle.js.html](http://bjornharrtell.github.io/jsts/doc/api/jsts_geom_Triangle.js.html)

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角地带将获得环绕 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 矢量2 对象将位置存储在其中。 如果不给定, 则创建新的矢量2 实例 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 具有三角环坐标的矢量2天体。


> 源码：[src/geom/triangle/CircumCenter.js#L28](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/CircumCenter.js#L28)  
引入版本：3.0.0


---

### CircumCircle {#CircumCircle}

#### \<static> CircumCircle(triangle, [out]) {#static-circumcircletriangle-out}


**说明:**

查找三角形对象的圆(圆圈),圆圈是触及三角形所有顶点的圆圈。

改编自 [https://gist.github.com/mutoo/5617691](https://gist.github.com/mutoo/5617691)

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角形作为输入使用. |
| out | [Phaser.Geom.Circle](/api/class/geom-circle) | 是 | 存储结果的可选圆 。 |


**返回值:** [Phaser.Geom.Circle](/api/class/geom-circle) - 更新的 `out` 圆,或者如果没有提供新圆。


> 源码：[src/geom/triangle/CircumCircle.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/CircumCircle.js#L9)  
引入版本：3.0.0


---

### Clone {#Clone}

#### \<static> Clone(source) {#static-clonesource}


**说明:**

克隆是一个三角天体。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角形要克隆了 三角形要克隆了 |


**返回值:** [Phaser.Geom.Triangle](/api/class/geom-triangle) - 一个与给定的三角形完全相同的新三角形,但与它相分离.


> 源码：[src/geom/triangle/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Clone.js#L9)  
引入版本：3.0.0


---

### contains {#contains}

#### \<instance> contains(x, y) {#instance-containsx-y}


**说明:**

检查某个点是否位于三角形之内。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 检查点的x坐标 。 |
| y | number | 否 | 检查点的y坐标。 |


**返回值:** boolean - 如果坐标对在三角形之内,则`true`,否则则`false`.


> 源码：[src/geom/triangle/Triangle.js#L122](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L122)  
引入版本：3.0.0


---

### Contains {#Contains}

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


---

### ContainsArray {#ContainsArray}

#### \<static> ContainsArray(triangle, points, [returnFirst], [out]) {#static-containsarraytriangle-points-returnfirst-out}


**说明:**

过滤一组类似点的物体,仅用于三角形内的对象。

如果 `returnFirst` 是真的, 则返回只包含三角形内所提供阵列中第一个点的阵列( 或如果没有这样的点, 则返回空阵列) 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 |  | 检查点的三角形 |
| points | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 否 |  | 要检查它们是否位于三角形之内, 需要一系列的矢量2 对象 。 |
| returnFirst | boolean | 是 | false | 如果 `true`,返回只包含发现在三角形内的第一点的阵列。 |
| out | array | 是 |  | 如果提供, 三角形内的点将附加到这个数组中, 而不是添加到一个新的数组中。 如果 `returnFirst` 是真实的, 则只附加三角形内的第一个点。 此数组也会被此函数返回 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 如果一个阵列作为`out`提供,则包含`points`中位于三角形范围内的所有点的阵列,点数将附在该阵列上,并在此返回。


> 源码：[src/geom/triangle/ContainsArray.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/ContainsArray.js#L7)  
引入版本：3.0.0


---

### ContainsPoint {#ContainsPoint}

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


---

### CopyFrom {#CopyFrom}

#### \<static> CopyFrom(source, dest) {#static-copyfromsource-dest}


**说明:**

复制一个三角的值到目的地三角 。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 复制值的源三角 。 |
| dest | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 目的地三角区将数值复制到 。 |


**返回值:** [Phaser.Geom.Triangle](/api/class/geom-triangle) - 目的地三角区.


> 源码：[src/geom/triangle/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/CopyFrom.js#L7)  
引入版本：3.0.0


---

### Decompose {#Decompose}

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


---

### Equals {#Equals}

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


---

### getLineA {#getLineA}

#### \<instance> getLineA([line]) {#instance-getlinealine}


**说明:**

返回一个与此三角形的 A 线相对应的线对象, 从顶点 1 运行( Q)`x1`, `y1`)到顶点2(`x2`, `y2`).

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 是 | 一个设置结果的行对象。 如果 `undefined` 将创建新行 。 |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 与这个三角形的A线对应的线形对象.


> 源码：[src/geom/triangle/Triangle.js#L228](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L228)  
引入版本：3.0.0


---

### getLineB {#getLineB}

#### \<instance> getLineB([line]) {#instance-getlinebline}


**说明:**

返回一个与此三角形的B线相对应的线对象,运行于顶点 2 ()`x2`, `y2`)到顶点3(`x3`, `y3`).

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 是 | 一个设置结果的行对象。 如果 `undefined` 将创建新行 。 |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 与这个三角形的B线对应的线对象。


> 源码：[src/geom/triangle/Triangle.js#L249](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L249)  
引入版本：3.0.0


---

### getLineC {#getLineC}

#### \<instance> getLineC([line]) {#instance-getlinecline}


**说明:**

返回一个与这个三角形的C线相对应的线对象,运行于顶点 3 ()`x3`, `y3`返回顶点 1 ()`x1`, `y1`),关闭形状.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 是 | 一个设置结果的行对象。 如果 `undefined` 将创建新行 。 |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 与这个三角形的C线对应的线形对象.


> 源码：[src/geom/triangle/Triangle.js#L270](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L270)  
引入版本：3.0.0


---

### getPoint {#getPoint}

#### \<instance> getPoint(position, [output]) {#instance-getpointposition-output}


**说明:**

返回三角形周边某个特定正常化位置的点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| position | number | 否 | `0`和`1`中浮点的位置。`0`等于第一点。 |
| output | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 可选矢量2点,计算点将被写入. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 计算出代表请求位置的矢量2。 当给出此参数时, 它与 `output` 相同 。


> 源码：[src/geom/triangle/Triangle.js#L138](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L138)  
引入版本：3.0.0


---

### GetPoint {#GetPoint}

#### \<static> GetPoint(triangle, position, [out]) {#static-getpointtriangle-position-out}


**说明:**

返回三角形周边的点作为矢量2,以正态位置值为基础。

`position`参数是一个0到1之间的值,其中0到1都映射到A线(第一个顶点)的起始点,该点通过绕过三角形的周长来计算,顺序是:A线,然后是B线,然后是C线.

**标签:**

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


---

### getPoints {#getPoints}

#### \<instance> getPoints(quantity, [stepRate], [output]) {#instance-getpointsquantity-steprate-output}


**说明:**

计算三角形周边分布均匀点的列表。或者通过点数生成(`quantity`),或者通过连续点之间的距离(`stepRate`)。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| quantity | number | 否 | 生成的点数。 `stepRate` 使用时可能存在假差。 所有点沿三角线的距离相同 。 |
| stepRate | number | 是 | 距离两点之间。 只有在 `quantity` 假时才会使用 。 |
| output | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 可选的矢量2点数组将计算出的点写入。 否则将创建新的数组 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 返回一个计算出的 `Vector2` 实例列表,或作为参数 `output` 通过的填充数组。


> 源码：[src/geom/triangle/Triangle.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L156)  
引入版本：3.0.0


---

### GetPoints {#GetPoints}

#### \<static> GetPoints(triangle, quantity, stepRate, [out]) {#static-getpointstriangle-quantity-steprate-out}


**说明:**

返回三角形周边的均匀空格点数组。

点沿三角形的三边排列顺序(A,B,然后C),其位置根据总周长按比例计算.

**标签:**

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


---

### getRandomPoint {#getRandomPoint}

#### \<instance> getRandomPoint([vec]) {#instance-getrandompointvec}


**说明:**

从三角形区域内返回随机点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 可选矢量2 点将被修改。 否则将创建一个新的矢量2 点 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 随机矢量2. 当参数`vec`已经提供时,它将被返回.


> 源码：[src/geom/triangle/Triangle.js#L175](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L175)  
引入版本：3.0.0


---

### InCenter {#InCenter}

#### \<static> InCenter(triangle, [out]) {#static-incentertriangle-out}


**说明:**

计算三角形物体的中间位置。这是其三个角双扇形交汇的点,也是圆圈的中心,即三角形内嵌的圆圈。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角寻找中心 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 可选的矢量2点,用于存储坐标. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 三角形的中间点在矢量2中。


> 源码：[src/geom/triangle/InCenter.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/InCenter.js#L21)  
引入版本：3.0.0


---

### Offset {#Offset}

#### \<static> Offset(triangle, x, y) {#static-offsettriangle-x-y}


**说明:**

以给定的偏移移动三角的每个点(顶点),从而以偏移移动整个三角。

**标签:**

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


---

### Perimeter {#Perimeter}

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


---

### Random {#Random}

#### \<static> Random(triangle, [out]) {#static-randomtriangle-out}


**说明:**

从给定三角区域范围内返回随机点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角从随机点得到。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 矢量2 点对象将位置存储在其中。 如果不给定, 则创建新的矢量2 实例 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 一个矢量2点物体,在三角内随机位置的坐标。


> 源码：[src/geom/triangle/Random.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Random.js#L9)  
引入版本：3.0.0


---

### Rotate {#Rotate}

#### \<static> Rotate(triangle, angle) {#static-rotatetriangle-angle}


**说明:**

旋转三角形的中间点,这是其三角双扇交汇点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角旋转. |
| angle | number | 否 | 三角旋转的角度,以弧度表示. |


**返回值:** [Phaser.Geom.Triangle](/api/class/geom-triangle) - 旋转三角形.


> 源码：[src/geom/triangle/Rotate.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Rotate.js#L10)  
引入版本：3.0.0


---

### RotateAroundPoint {#RotateAroundPoint}

#### \<static> RotateAroundPoint(triangle, point, angle) {#static-rotatearoundpointtriangle-point-angle}


**说明:**

在一个给定的矢量2 点上以一定角度旋转三角形。

**标签:**

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


---

### RotateAroundXY {#RotateAroundXY}

#### \<static> RotateAroundXY(triangle, x, y, angle) {#static-rotatearoundxytriangle-x-y-angle}


**说明:**

在一个特定点上以特定角度旋转整个三角。

**标签:**

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

### setTo {#setTo}

#### \<instance> setTo([x1], [y1], [x2], [y2], [x3], [y3]) {#instance-settox1-y1-x2-y2-x3-y3}


**说明:**

设置三角形的所有三个点。 任何坐标都设置为 `0` 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x1 | number | 是 | 0 | `x` 坐标为第一点。 |
| y1 | number | 是 | 0 | `y` 坐标为第一点。 |
| x2 | number | 是 | 0 | 第二点的`x`坐标. |
| y2 | number | 是 | 0 | 第二点的`y`坐标. |
| x3 | number | 是 | 0 | `x` 第三点的坐标。 |
| y3 | number | 是 | 0 | `y` 第三点的坐标。 |


**返回值:** [Phaser.Geom.Triangle](/api/class/geom-triangle) - 此三角对象 。


> 源码：[src/geom/triangle/Triangle.js#L192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L192)  
引入版本：3.0.0


---

## 公开成员 {#public-members}

### bottom {#bottom}

#### bottom: number {#bottom-number}


**说明:**

三角形的Y坐标底部。 设置它会相应移动 Y 轴上的三角形 。


> 源码：[src/geom/triangle/Triangle.js#L405](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L405)  
引入版本：3.0.0


---

### left {#left}

#### left: number {#left-number}


**说明:**

三角形的多数 X 坐标。 设置它会相应移动 X 轴上的三角形 。


> 源码：[src/geom/triangle/Triangle.js#L291](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L291)  
引入版本：3.0.0


---

### right {#right}

#### right: number {#right-number}


**说明:**

三角形的最右X坐标。 设置它会相应移动 X 轴上的三角形 。


> 源码：[src/geom/triangle/Triangle.js#L329](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L329)  
引入版本：3.0.0


---

### top {#top}

#### top: number {#top-number}


**说明:**

三角形上方的 Y 坐标。 设置它会相应移动 Y 轴上的三角形 。


> 源码：[src/geom/triangle/Triangle.js#L367](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L367)  
引入版本：3.0.0


---

### type {#type}

#### type: number {#type-number}


**说明:**

此对象的几何常数类型: `GEOM_CONST.TRIANGLE`. 用于快速类型比较.


> 源码：[src/geom/triangle/Triangle.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L50)  
引入版本：3.19.0


---

### x1 {#x1}

#### x1: number {#x1-number}


**说明:**

`x` 坐标为第一点。


> 源码：[src/geom/triangle/Triangle.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L61)  
引入版本：3.0.0


---

### x2 {#x2}

#### x2: number {#x2-number}


**说明:**

第二点的`x`坐标.


> 源码：[src/geom/triangle/Triangle.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L81)  
引入版本：3.0.0


---

### x3 {#x3}

#### x3: number {#x3-number}


**说明:**

`x` 第三点的坐标。


> 源码：[src/geom/triangle/Triangle.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L101)  
引入版本：3.0.0


---

### y1 {#y1}

#### y1: number {#y1-number}


**说明:**

`y` 坐标为第一点。


> 源码：[src/geom/triangle/Triangle.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L71)  
引入版本：3.0.0


---

### y2 {#y2}

#### y2: number {#y2-number}


**说明:**

第二点的`y`坐标.


> 源码：[src/geom/triangle/Triangle.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L91)  
引入版本：3.0.0


---

### y3 {#y3}

#### y3: number {#y3-number}


**说明:**

`y` 第三点的坐标。


> 源码：[src/geom/triangle/Triangle.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/triangle/Triangle.js#L111)  
引入版本：3.0.0


---

---
