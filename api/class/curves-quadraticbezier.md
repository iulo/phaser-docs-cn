# QuadraticBezier {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/curves-quadraticbezier)

由三个点构造的四角贝塞尔曲线:起点、单一控制点和终点。这是二级贝塞尔曲线,控制点影响起点和终点之间的路径曲率。

**构造函数**

`new QuadraticBezier(p0, p1, p2)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| p0 | [Phaser.Math.Vector2](/api/class/math-vector2) \| Array.\<number> | 否 | 起点,或指一对点的阵列. |
| p1 | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 控制点1。 |
| p2 | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 曲线的终点. |

---


**作用域**: static


**继承**

> [Phaser.Curves.Curve](/api/class/curves-curve)  



> 源码：[src/curves/QuadraticBezierCurve.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/QuadraticBezierCurve.js#L12)  
引入版本：3.2.0

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

### p0 {#p0}

#### p0: [Phaser.Math.Vector2](/api/class/math-vector2) {#p0-phasermathvector2}


**说明:**

始发点.


> 源码：[src/curves/QuadraticBezierCurve.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/QuadraticBezierCurve.js#L45)  
引入版本：3.2.0


---

### p1 {#p1}

#### p1: [Phaser.Math.Vector2](/api/class/math-vector2) {#p1-phasermathvector2}


**说明:**

初总控点.


> 源码：[src/curves/QuadraticBezierCurve.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/QuadraticBezierCurve.js#L54)  
引入版本：3.2.0


---

### p2 {#p2}

#### p2: [Phaser.Math.Vector2](/api/class/math-vector2) {#p2-phasermathvector2}


**说明:**

曲线的终点.


> 源码：[src/curves/QuadraticBezierCurve.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/QuadraticBezierCurve.js#L63)  
引入版本：3.2.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Curves.Curve](/api/class/curves-curve):**


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

### draw {#draw}

#### \<instance> draw(graphics, [pointsTotal]) {#instance-drawgraphics-pointstotal}


**说明:**

在给定的图形对象上绘制此曲线。

曲线是使用 `Graphics.strokePoints` 绘制的, 所以无论当前图形的中风颜色是什么, 都会绘制。 图形对象在绘图前没有清除, 因此曲线会出现在其他已显示对象的上方 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 |  | 要绘制的 `Graphics` 对象 。 |
| pointsTotal | number | 是 | 32 | 绘制曲线时要使用的点数。 数字越多, 曲线越平滑, 需要更多的处理 。 |


**Overrides:** Phaser.Curves.Curve画画


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 被引向的 `Graphics` 对象 。


> 源码：[src/curves/QuadraticBezierCurve.js#L134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/QuadraticBezierCurve.js#L134)  
引入版本：3.2.0


---

### fromJSON {#fromJSON}

#### \<static> fromJSON(data) {#static-fromjsondata}


**说明:**

从 JSON 对象创建曲线,例如 `toJSON` 创建的曲线.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | [Phaser.Types.Curves.JSONCurve](/api/typedef/types-curves#jsoncurve) | 否 | JSON 对象包含此曲线数据. |


**返回值:** [Phaser.Curves.QuadraticBezier](/api/class/curves-quadraticbezier) - 创建的曲线实例 。


> 源码：[src/curves/QuadraticBezierCurve.js#L192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/QuadraticBezierCurve.js#L192)  
引入版本：3.2.0


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


> 源码：[src/curves/QuadraticBezierCurve.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/QuadraticBezierCurve.js#L107)  
引入版本：3.2.0


---

### getResolution {#getResolution}

#### \<instance> getResolution(divisions) {#instance-getresolutiondivisions}


**说明:**

返回此曲线的分辨率。 对于一个四边形贝塞尔, 分辨率等于请求的分区数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| divisions | number | 否 | 选择的分值。 |


**返回值:** number - 曲线分辨率。


> 源码：[src/curves/QuadraticBezierCurve.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/QuadraticBezierCurve.js#L92)  
引入版本：3.2.0


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


> 源码：[src/curves/QuadraticBezierCurve.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/QuadraticBezierCurve.js#L73)  
引入版本：3.2.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

将曲线转换为 JSON 兼容对象。


**返回值:** [Phaser.Types.Curves.JSONCurve](/api/typedef/types-curves#jsoncurve) - JSON 对象包含此曲线数据.


> 源码：[src/curves/QuadraticBezierCurve.js#L170](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/QuadraticBezierCurve.js#L170)  
引入版本：3.2.0


---

---
