# Line {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/curves-line)

线条链路是一个直线段,由两个完全的终点定义。尽管它被称为“曲线”,但它执行全线 `Phaser.Curves.Curve` 界面,指它可以在任何预期曲线的任何地方使用——例如,作为一个曲线的一部分 `Phaser.Curves.Path` 或作为 Tween 的运动路径。由于线条完全直,弧长计算准确而高效,使 LineCurve 成为最能表现的曲线类型。您可以从 2 构造一个 `Vector2` 点数或从四个数字的平方数组 `[x0, y0, x1, y1]`.

**构造函数**

`new Line(p0, [p1])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| p0 | [Phaser.Math.Vector2](/api/class/math-vector2) \| Array.\<number> | 否 | 初结分. |
| p1 | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 第二结分. |

---


**作用域**: static


**继承**

> [Phaser.Curves.Curve](/api/class/curves-curve)  



> 源码：[src/curves/LineCurve.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/LineCurve.js#L15)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Curves.Curve](/api/class/curves-curve):**


 - [active](/api/class/curves-curve#active)
 - [cacheArcLengths](/api/class/curves-curve#cacheArcLengths)
 - [defaultDivisions](/api/class/curves-curve#defaultDivisions)
 - [needsUpdate](/api/class/curves-curve#needsUpdate)
 - [type](/api/class/curves-curve#type)




---

## 公开成员 {#public-members}

### arcLengthDivisions {#arcLengthDivisions}

#### arcLengthDivisions: number {#arclengthdivisions-number}


**说明:**

曲线内弧长的分数。


**Overrides:** Phaser.Curves.Curve#arcLengthDivisions


> 源码：[src/curves/LineCurve.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/LineCurve.js#L70)  
引入版本：3.0.0


---

### p0 {#p0}

#### p0: [Phaser.Math.Vector2](/api/class/math-vector2) {#p0-phasermathvector2}


**说明:**

初结分.


> 源码：[src/curves/LineCurve.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/LineCurve.js#L50)  
引入版本：3.0.0


---

### p1 {#p1}

#### p1: [Phaser.Math.Vector2](/api/class/math-vector2) {#p1-phasermathvector2}


**说明:**

第二结分.


> 源码：[src/curves/LineCurve.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/LineCurve.js#L59)  
引入版本：3.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Curves.Curve](/api/class/curves-curve):**


 - [getDistancePoints](/api/class/curves-curve#getDistancePoints)
 - [getEndPoint](/api/class/curves-curve#getEndPoint)
 - [getLength](/api/class/curves-curve#getLength)
 - [getLengths](/api/class/curves-curve#getLengths)
 - [getPoints](/api/class/curves-curve#getPoints)
 - [getRandomPoint](/api/class/curves-curve#getRandomPoint)
 - [getSpacedPoints](/api/class/curves-curve#getSpacedPoints)
 - [getTangentAt](/api/class/curves-curve#getTangentAt)
 - [getTFromDistance](/api/class/curves-curve#getTFromDistance)
 - [updateArcLengths](/api/class/curves-curve#updateArcLengths)




---

## 公开方法 {#public-methods}

### draw {#draw}

#### \<instance> draw(graphics) {#instance-drawgraphics}


**说明:**

在给定的图形对象上绘制此曲线。

曲线使用 `Graphics.lineBetween` 绘制, 因此将绘制当前图形线条颜色。 图形对象在绘制前没有清除, 因此曲线将出现在已经显示的其他任何颜色的上方 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 绘制此曲线的图形实例 。 |


**Overrides:** Phaser.Curves.Curve画画


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 曲线绘制对象的图形。


> 源码：[src/curves/LineCurve.js#L244](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/LineCurve.js#L244)  
引入版本：3.0.0


---

### fromJSON {#fromJSON}

#### \<static> fromJSON(data) {#static-fromjsondata}


**说明:**

配置 JSON 表示式的此行 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | [Phaser.Types.Curves.JSONCurve](/api/typedef/types-curves#jsoncurve) | 否 | JSON 对象包含此曲线数据. |


**返回值:** [Phaser.Curves.Line](/api/class/curves-line) - 一个新的 LineCurve 对象 。


> 源码：[src/curves/LineCurve.js#L288](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/LineCurve.js#L288)  
引入版本：3.0.0


---

### getBounds {#getBounds}

#### \<instance> getBounds([out]) {#instance-getboundsout}


**说明:**

返回一个矩形,其中位置和维度与此曲线的界限相匹配。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 用于存储边框的矩形对象。 如果不给定新的矩形, 将会创建 。 |


**Overrides:** Phaser.Curves.Curve#getBounds


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 矩形天体持有此曲线的界限。 如果给它 `out` , 则它就是此天体 。


> 源码：[src/curves/LineCurve.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/LineCurve.js#L81)  
引入版本：3.0.0


---

### getPoint {#getPoint}

#### \<instance> getPoint(t, [out]) {#instance-getpointt-out}


**说明:**

获得沿线相对位置的点,其中0为起点,1为终点.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 沿曲线返回的位置。 0 开始和 1 结束。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储结果的矢量2 对象。 如果不给定, 将会创建 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 曲线上点的坐标。 如果给定了 `out` 对象, 将会返回 。


> 源码：[src/curves/LineCurve.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/LineCurve.js#L136)  
引入版本：3.0.0


---

### getPointAt {#getPointAt}

#### \<instance> getPointAt(u, [out]) {#instance-getpointatu-out}


**说明:**

获得线上指定位置的点数。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| u | number | 否 | 沿曲线返回的位置。 0 开始和 1 结束。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储结果的矢量2 对象。 如果不给定, 将会创建 。 |


**Overrides:** Phaser.Curves.Curve#getPointAt


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 曲线上点的坐标。 如果给定了 `out` 对象, 将会返回 。


> 源码：[src/curves/LineCurve.js#L165](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/LineCurve.js#L165)  
引入版本：3.0.0


---

### getResolution {#getResolution}

#### \<instance> getResolution([divisions]) {#instance-getresolutiondivisions}


**说明:**

返回此曲线的分辨率。 对于 LineCurve , 分辨率等于请求的分区数, 如果没有提供, 则默认为 1 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| divisions | number | 是 | 1 | 师数数要考. |


**返回值:** number - 决议 与分裂的数目相等


> 源码：[src/curves/LineCurve.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/LineCurve.js#L119)  
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


> 源码：[src/curves/LineCurve.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/LineCurve.js#L100)  
引入版本：3.0.0


---

### getTangent {#getTangent}

#### \<instance> getTangent([t], [out]) {#instance-gettangentt-out}


**说明:**

获得线条的斜度作为单位矢量.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 是 | 线上的相对位置, [0. 1]. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 存储结果的向量 。 |


**Overrides:** Phaser.Curves.Curve#getTangent


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 切向量.


> 源码：[src/curves/LineCurve.js#L183](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/LineCurve.js#L183)  
引入版本：3.0.0


---

### getUtoTmapping {#getUtoTmapping}

#### \<instance> getUtoTmapping(u, distance, [divisions]) {#instance-getutotmappingu-distance-divisions}


**说明:**

将沿线的基于距离的位置转换为在0到1之间的一个正常`t`值,如果提供`distance`,返回的`t`代表了被夹在线总长度上的距离。如果不给出距离,则直接返回`u`。由于直线具有统一的弧长,所以存在这种超度,因此不需要迭代重参数化。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| u | number | 否 | 浮在0到1之间 |
| distance | number | 否 | 距离,以像素计. |
| divisions | number | 是 | 分数可选. |


**Overrides:** Phaser.Curves.Curve#getUtoTmapping


**返回值:** number - 等距离值 。


> 源码：[src/curves/LineCurve.js#L205](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/LineCurve.js#L205)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

得到JSON代表线.


**返回值:** [Phaser.Types.Curves.JSONCurve](/api/typedef/types-curves#jsoncurve) - JSON 对象包含此曲线数据.


> 源码：[src/curves/LineCurve.js#L267](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/LineCurve.js#L267)  
引入版本：3.0.0


---

---
