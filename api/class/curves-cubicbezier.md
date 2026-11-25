# CubicBezier {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/curves-cubicbezier)

立方体贝塞尔曲线是一个平滑的参数曲线,由四个点定义:一个起点(`p0`),两个控制点(`p1` 财务报告和已审计财务报表 `p2`),以形状曲面,并有一个终点(`p3`。曲线通过 `p0` 财务报告和已审计财务报表 `p3` 只能被拉到控制点上 让你创造出各种各样的平滑的形状

Phaser中通常使用立方体贝塞尔曲线来定义运动路径,沿弧线动画对象,以及构建复杂的`Path`对象。您可以使用从 0(起始)到 1(结束)的正态`t`Z 值来对曲线沿线的任何位置进行取样,或者使用`getPoints`和`getSpacedPoints`等继承的辅助方法来获取均匀分布的坐标来渲染或移动.

**构造函数**

`new CubicBezier(p0, p1, p2, p3)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| p0 | [Phaser.Math.Vector2](/api/class/math-vector2) \| Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 否 | 起点,或指一对点的阵列. |
| p1 | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 控制点1。 |
| p2 | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 控制点2。 |
| p3 | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 终点. |

---


**作用域**: static


**继承**

> [Phaser.Curves.Curve](/api/class/curves-curve)  



> 源码：[src/curves/CubicBezierCurve.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/CubicBezierCurve.js#L14)  
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

### p0 {#p0}

#### p0: [Phaser.Math.Vector2](/api/class/math-vector2) {#p0-phasermathvector2}


**说明:**

此曲线的起点 。


> 源码：[src/curves/CubicBezierCurve.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/CubicBezierCurve.js#L56)  
引入版本：3.0.0


---

### p1 {#p1}

#### p1: [Phaser.Math.Vector2](/api/class/math-vector2) {#p1-phasermathvector2}


**说明:**

此曲线的第一个控制点.


> 源码：[src/curves/CubicBezierCurve.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/CubicBezierCurve.js#L65)  
引入版本：3.0.0


---

### p2 {#p2}

#### p2: [Phaser.Math.Vector2](/api/class/math-vector2) {#p2-phasermathvector2}


**说明:**

此曲线的第二个控制点.


> 源码：[src/curves/CubicBezierCurve.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/CubicBezierCurve.js#L74)  
引入版本：3.0.0


---

### p3 {#p3}

#### p3: [Phaser.Math.Vector2](/api/class/math-vector2) {#p3-phasermathvector2}


**说明:**

此曲线的终点.


> 源码：[src/curves/CubicBezierCurve.js#L83](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/CubicBezierCurve.js#L83)  
引入版本：3.0.0


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

将这个曲线绘制到指定的图形对象。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 |  | 图形对象此曲线应绘制到。 |
| pointsTotal | number | 是 | 32 | 构成这个曲线的中间点数,如果点数多一点,则会使曲线更平滑。 |


**Overrides:** Phaser.Curves.Curve画画


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 图形对象此曲线被绘制。 可用于方法链。 Name


> 源码：[src/curves/CubicBezierCurve.js#L152](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/CubicBezierCurve.js#L152)  
引入版本：3.0.0


---

### fromJSON {#fromJSON}

#### \<static> fromJSON(data) {#static-fromjsondata}


**说明:**

从 JSON 对象生成曲线 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | [Phaser.Types.Curves.JSONCurve](/api/typedef/types-curves#jsoncurve) | 否 | JSON 对象包含此曲线数据. |


**返回值:** [Phaser.Curves.CubicBezier](/api/class/curves-cubicbezier) - JSON 对象生成的曲线 。


> 源码：[src/curves/CubicBezierCurve.js#L208](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/CubicBezierCurve.js#L208)  
引入版本：3.0.0


---

### getPoint {#getPoint}

#### \<instance> getPoint(t, [out]) {#instance-getpointt-out}


**说明:**

使用立方贝塞尔插值计算该曲线上给定的正态位置(`t`)的点坐标。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 沿曲线返回的位置。 0 开始和 1 结束。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储结果的矢量2 对象。 如果不给定, 将会创建 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 曲线上点的坐标。 如果给定了 `out` 对象, 将会返回 。


> 源码：[src/curves/CubicBezierCurve.js#L127](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/CubicBezierCurve.js#L127)  
引入版本：3.0.0


---

### getResolution {#getResolution}

#### \<instance> getResolution(divisions) {#instance-getresolutiondivisions}


**说明:**

返回此曲线的分辨率, 即计算长度或采样时用来进行近似的点数。 对于一个立方体贝塞尔, 分辨率等于所要求的除数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| divisions | number | 否 | 此曲线使用的分区量 。 |


**返回值:** number - 曲线的解析度.


> 源码：[src/curves/CubicBezierCurve.js#L112](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/CubicBezierCurve.js#L112)  
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


> 源码：[src/curves/CubicBezierCurve.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/CubicBezierCurve.js#L93)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

返回描述此曲线的 JSON 对象。


**返回值:** [Phaser.Types.Curves.JSONCurve](/api/typedef/types-curves#jsoncurve) - JSON 对象包含此曲线数据.


> 源码：[src/curves/CubicBezierCurve.js#L185](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/CubicBezierCurve.js#L185)  
引入版本：3.0.0


---

---
