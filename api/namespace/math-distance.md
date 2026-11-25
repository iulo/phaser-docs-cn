# Phaser.Math.Distance {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-distance)

Scope: 
static
> 源码：[src/math/distance/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/distance/index.js#L7)  


## 静态函数 {#static-functions}

### Between {#Between}

#### \<static> Between(x1, y1, x2, y2) {#static-betweenx1-y1-x2-y2}


**说明:**

计算两组坐标(点)之间的距离。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x1 | number | 否 | 第一点的x坐标. |
| y1 | number | 否 | 第一点的y坐标 |
| x2 | number | 否 | 第二点的x坐标. |
| y2 | number | 否 | 第二点的y坐标. |


**返回值:** number - 每个点之间的距离.


> 源码：[src/math/distance/DistanceBetween.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/distance/DistanceBetween.js#L7)  
引入版本：3.0.0


---

### BetweenPoints {#BetweenPoints}

#### \<static> BetweenPoints(a, b) {#static-betweenpointsa-b}


**说明:**

计算两点之间的距离。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 第一义. |
| b | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 第二义. |


**返回值:** number - 点间之距离.


> 源码：[src/math/distance/DistanceBetweenPoints.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/distance/DistanceBetweenPoints.js#L7)  
引入版本：3.22.0


---

### BetweenPointsSquared {#BetweenPointsSquared}

#### \<static> BetweenPointsSquared(a, b) {#static-betweenpointssquareda-b}


**说明:**

计算两点之间的平方距离。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 第一义. |
| b | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 第二义. |


**返回值:** number - 点间平方距离.


> 源码：[src/math/distance/DistanceBetweenPointsSquared.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/distance/DistanceBetweenPointsSquared.js#L7)  
引入版本：3.22.0


---

### Chebyshev {#Chebyshev}

#### \<static> Chebyshev(x1, y1, x2, y2) {#static-chebyshevx1-y1-x2-y2}


**说明:**

计算两组坐标(点)之间的切比舍夫距离.

切比舍夫距离(或棋盘距离)是水平和垂直距离的最大距离,是运动可以水平,垂直,或对角时的有效距离.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x1 | number | 否 | 第一点的x坐标. |
| y1 | number | 否 | 第一点的y坐标 |
| x2 | number | 否 | 第二点的x坐标. |
| y2 | number | 否 | 第二点的y坐标. |


**返回值:** number - 每个点之间的距离.


> 源码：[src/math/distance/DistanceChebyshev.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/distance/DistanceChebyshev.js#L7)  
引入版本：3.22.0


---

### Power {#Power}

#### \<static> Power(x1, y1, x2, y2, [pow]) {#static-powerx1-y1-x2-y2-pow}


**说明:**

使用通用电源公式计算两组坐标之间的距离: `sqrt((x2 - x1)^pow + (y2 - y1)^pow)`。 `pow`是 `2` 时,这相当于标准的欧几里得距离。 增加 `pow` 强调更大的轴差 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x1 | number | 否 |  | 第一点的x坐标. |
| y1 | number | 否 |  | 第一点的y坐标 |
| x2 | number | 否 |  | 第二点的x坐标. |
| y2 | number | 否 |  | 第二点的y坐标. |
| pow | number | 是 | 2 | 符号应用到每个轴差。 默认为 `2`, 因为它给出了标准的欧几里得距离 。 |


**返回值:** number - 二者之远.


> 源码：[src/math/distance/DistancePower.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/distance/DistancePower.js#L7)  
引入版本：3.0.0


---

### Snake {#Snake}

#### \<static> Snake(x1, y1, x2, y2) {#static-snakex1-y1-x2-y2}


**说明:**

计算两组坐标(点)之间的蛇距离.

蛇距离(rectilinear star,曼哈顿距离)是水平距离和垂直距离的总称,它是只有水平或垂直(但两者均不允许)移动时的有效距离.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x1 | number | 否 | 第一点的x坐标. |
| y1 | number | 否 | 第一点的y坐标 |
| x2 | number | 否 | 第二点的x坐标. |
| y2 | number | 否 | 第二点的y坐标. |


**返回值:** number - 每个点之间的距离.


> 源码：[src/math/distance/DistanceSnake.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/distance/DistanceSnake.js#L7)  
引入版本：3.22.0


---

### Squared {#Squared}

#### \<static> Squared(x1, y1, x2, y2) {#static-squaredx1-y1-x2-y2}


**说明:**

计算两组坐标(点)之间的距离,平方。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x1 | number | 否 | 第一点的x坐标. |
| y1 | number | 否 | 第一点的y坐标 |
| x2 | number | 否 | 第二点的x坐标. |
| y2 | number | 否 | 第二点的y坐标. |


**返回值:** number - 每个点之间的距离,平方.


> 源码：[src/math/distance/DistanceSquared.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/distance/DistanceSquared.js#L7)  
引入版本：3.0.0


---

---
