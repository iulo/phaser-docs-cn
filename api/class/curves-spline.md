# Spline {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/curves-spline)

斯普林曲线(Spline Curve)是一种通过一系列控制点的平滑曲线,它使用Catmull-Rom插值来产生一个自然外观的路径,与贝塞尔曲线不同,每个控制点都精确被访问,因此很容易定义对象所遵循的精确路径.

当您需要通过多个路标,例如相机多利轨道,弹射飞行路径,或游戏角色的巡逻路径等平滑路径时使用 Spline 曲线. 点可以在施工时添加,也可以通过`addPoint`和`addPoints`递增.

**构造函数**

`new Spline([points])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| points | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> \| Array.\<number> | Array.\<Array.\<number>> | 是 | 配置曲线的点。 |

---


**作用域**: static


**继承**

> [Phaser.Curves.Curve](/api/class/curves-curve)  



> 源码：[src/curves/SplineCurve.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/SplineCurve.js#L14)  
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

### points {#points}

#### points: Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> {#points-arrayphasermathvector2}


**说明:**

配置曲线的矢量2 点。


> 源码：[src/curves/SplineCurve.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/SplineCurve.js#L44)  
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

### addPoint {#addPoint}

#### \<instance> addPoint(x, y) {#instance-addpointx-y}


**说明:**

在当前曲线矢量2点列表中添加点.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 添加点的x坐标 。 |
| y | number | 否 | 添加点的y坐标 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 曲线中新增矢量2


> 源码：[src/curves/SplineCurve.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/SplineCurve.js#L97)  
引入版本：3.0.0


---

### addPoints {#addPoints}

#### \<instance> addPoints(points) {#instance-addpointspoints}


**说明:**

在曲线矢量2点当前列表中添加一个点列表.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| points | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> \| Array.\<number> | Array.\<Array.\<number>> | 否 | 添加的点。 接受一组`Vector2`对象, 一组平整的互离`x, y`数字对, 或一组双元素的`[x, y]`数字数组。 |


**返回值:** [Phaser.Curves.Spline](/api/class/curves-spline) - 此曲线对象 。


> 源码：[src/curves/SplineCurve.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/SplineCurve.js#L57)  
引入版本：3.0.0


---

### fromJSON {#fromJSON}

#### \<static> fromJSON(data) {#static-fromjsondata}


**说明:**

导入包含此曲线数据的 JSON 对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | [Phaser.Types.Curves.JSONCurve](/api/typedef/types-curves#jsoncurve) | 否 | JSON 对象包含此曲线数据. |


**返回值:** [Phaser.Curves.Spline](/api/class/curves-spline) - 创建的示意图曲线 。


> 源码：[src/curves/SplineCurve.js#L210](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/SplineCurve.js#L210)  
引入版本：3.0.0


---

### getPoint {#getPoint}

#### \<instance> getPoint(t, [out]) {#instance-getpointt-out}


**说明:**

根据长度在曲线中相对位置获得点.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 沿曲线返回的位置。 0 开始和 1 结束。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储结果的矢量2 对象。 如果不给定, 将会创建 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 曲线上点的坐标。 如果给定了 `out` 对象, 将会返回 。


> 源码：[src/curves/SplineCurve.js#L151](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/SplineCurve.js#L151)  
引入版本：3.0.0


---

### getResolution {#getResolution}

#### \<instance> getResolution(divisions) {#instance-getresolutiondivisions}


**说明:**

返回此曲线的分辨率, 即用于每个段的大概点数。 对于 Spline, 此比例尺包含点数和要求的除数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| divisions | number | 否 | 曲线近似时每段使用的分区数. |


**返回值:** number - 曲线分辨率。


> 源码：[src/curves/SplineCurve.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/SplineCurve.js#L136)  
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


> 源码：[src/curves/SplineCurve.js#L117](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/SplineCurve.js#L117)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

导出一个包含此曲线数据的 JSON 对象。


**返回值:** [Phaser.Types.Curves.JSONCurve](/api/typedef/types-curves#jsoncurve) - JSON 对象包含此曲线数据.


> 源码：[src/curves/SplineCurve.js#L184](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/SplineCurve.js#L184)  
引入版本：3.0.0


---

---
