# Polygon {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/geom-polygon)

多边形对象

多边形是一个封闭的形状,由一系列由命令点列表定义的连接直线组成。支持几种格式来定义点列表,检查setTo方法的细节。这是一个几何对象,允许您定义和检查形状。它不是一个游戏对象,因为您无法将其添加到显示列表中,它没有纹理。要使多边形显示,您应该查看图形类的能力。

**构造函数**

`new Polygon([points])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| points | string \| Array.\<number> | Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 是 | 定义此多边形周边的点列表。 支持几种格式 : - 包含一个单空分隔的对齐 x y 值的字符串 : `'40 0 40 20 100 20 100 80 40 80 40 100 0 50'` - 点对象阵列 : `[new Phaser.Point(x1, y1), ...]` - 具有公有 x y 属性的物体阵列 : `[obj1, obj2, ...]` - 代表点坐标的对齐数字阵列 : Z`[x1,y1, x2,y2, ...]` - 包含两个元素的阵列代表 x/y 坐标 : `[[x1, y1], [x2, y2], ...]` |

---


**作用域**: static

> 源码：[src/geom/polygon/Polygon.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Polygon.js#L12)  
引入版本：3.0.0

## 公开方法 {#public-methods}

### calculateArea {#calculateArea}

#### \<instance> calculateArea() {#instance-calculatearea}


**说明:**

使用 Shoelace 公式计算多边形的区域。结果存储在 `area` 属性中。


**返回值:** number - 多边形的区域 。


> 源码：[src/geom/polygon/Polygon.js#L160](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Polygon.js#L160)  
引入版本：3.0.0


---

### Clone {#Clone}

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


---

### contains {#contains}

#### \<instance> contains(x, y) {#instance-containsx-y}


**说明:**

选中可查看多边形是否包含给定的 x / y 坐标 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | x 坐标以检查多边形内部 。 |
| y | number | 否 | 用于检查多边形内的 Y 坐标 。 |


**返回值:** boolean - 如果坐标在多边形内,则`true`,否则则`false`.


> 源码：[src/geom/polygon/Polygon.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Polygon.js#L76)  
引入版本：3.0.0


---

### Contains {#Contains}

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


---

### ContainsPoint {#ContainsPoint}

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


---

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


---

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


---

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


---

### getPoints {#getPoints}

#### \<instance> getPoints(quantity, [stepRate], [output]) {#instance-getpointsquantity-steprate-output}


**说明:**

返回含有多边形周边各点坐标的矢量2对象阵列,其数值以给定的数量或stepRate值为准。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| quantity | number | 否 | 返回的点数。 如果一个疟原虫值, 则数量将从 `stepRate` 中得出 。 |
| stepRate | number | 是 | 以stepRate来划分多边形的周界,设定数量。 |
| output | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 插入点数组。 如果不提供新的数组, 将创建 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 与多边形周边各点有关的一系列矢量2物体。


> 源码：[src/geom/polygon/Polygon.js#L199](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Polygon.js#L199)  
引入版本：3.12.0


---

### GetPoints {#GetPoints}

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


---

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


---

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


---

### setTo {#setTo}

#### \<instance> setTo([points]) {#instance-settopoints}


**说明:**

将这个多边形设定为给定点。

可以从多种格式设定点数:

- 包含对数值的字符串, 由单个空格分隔: `'40 0 40 20 100 20 100 80 40 80 40 100 0 50'`

- 点对象数组: `[new Phaser.Point(x1, y1), ...]`

- 具有公共 x/y 属性的天体阵列: `[obj1, obj2, ...]`

- 代表点坐标的对数组: `[x1,y1, x2,y2, ...]`

- 一组阵列,其中两个元素代表x/y坐标:`[[x1, y1], [x2, y2], ...]`

`setTo`也可以在没有任何参数的情况下调用,以去除所有点.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| points | string \| Array.\<number> | Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 是 | 定义多边形周界的点。 请检查上面的函数描述 。 |


**返回值:** [Phaser.Geom.Polygon](/api/class/geom-polygon) - 此多边形对象 。


> 源码：[src/geom/polygon/Polygon.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Polygon.js#L92)  
引入版本：3.0.0


---

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


---

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


---

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


---

## 公开成员 {#public-members}

### area {#area}

#### area: number {#area-number}


**说明:**

这片多边形的区域。


> 源码：[src/geom/polygon/Polygon.js#L51](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Polygon.js#L51)  
引入版本：3.0.0


---

### points {#points}

#### points: Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> {#points-arrayphasermathvector2}


**说明:**

构成这个多边形的数对对象阵列。 I. e. \[{x,y},{x,y},{x,y}


> 源码：[src/geom/polygon/Polygon.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Polygon.js#L61)  
引入版本：3.0.0


---

### type {#type}

#### type: number {#type-number}


**说明:**

此对象的几何常数类型: `GEOM_CONST.POLYGON`. 用于快速类型比较.


> 源码：[src/geom/polygon/Polygon.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/polygon/Polygon.js#L40)  
引入版本：3.19.0


---

---
