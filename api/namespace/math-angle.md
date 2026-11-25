# Phaser.Math.Angle {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-angle)

Scope: 
static
> 源码：[src/math/angle/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/index.js#L7)  


## 静态函数 {#static-functions}

### Between {#Between}

#### \<static> Between(x1, y1, x2, y2) {#static-betweenx1-y1-x2-y2}


**说明:**

从(x1, y1) - > (x2, y2) 中查找一个线段的角 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x1 | number | 否 | 第一点的x坐标. |
| y1 | number | 否 | 第一点的y坐标 |
| x2 | number | 否 | 第二点的x坐标. |
| y2 | number | 否 | 第二点的y坐标. |


**返回值:** number - 弧度角度.


> 源码：[src/math/angle/Between.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/Between.js#L7)  
引入版本：3.0.0


---

### BetweenPoints {#BetweenPoints}

#### \<static> BetweenPoints(point1, point2) {#static-betweenpointspoint1-point2}


**说明:**

查找一个线段从(点1.x,点1.y) - >(点2.x,点2.y)的角度。

计算从第一点到第二点的矢量角度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point1 | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 第一义. |
| point2 | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 第二义. |


**返回值:** number - 弧度角度.


> 源码：[src/math/angle/BetweenPoints.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/BetweenPoints.js#L7)  
引入版本：3.0.0


---

### BetweenPointsY {#BetweenPointsY}

#### \<static> BetweenPointsY(point1, point2) {#static-betweenpointsypoint1-point2}


**说明:**

查找一个线段从(点1.x,点1.y) - >(点2.x,点2.y)的角度。

与 [Phaser.Math.Angle.BetweenPoints](/api/namespace/math-angle#BetweenPoints) 不同,此函数从正 Y 轴(在屏幕空间向下指向) 而不是正 X 轴测量角度。 这意味着 0 弧度的角度直接向下指向屏幕, 使其对默认面向向上(即向下指向向向下指向 y) 的游戏对象有用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point1 | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 第一义. |
| point2 | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 第二义. |


**返回值:** number - 弧度角度.


> 源码：[src/math/angle/BetweenPointsY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/BetweenPointsY.js#L7)  
引入版本：3.0.0


---

### BetweenY {#BetweenY}

#### \<static> BetweenY(x1, y1, x2, y2) {#static-betweenyx1-y1-x2-y2}


**说明:**

从(x1, y1) - > (x2, y2) 中查找一个线段的角 。

这种方法和[Phaser.Math.Angle.Between](/api/namespace/math-angle#Between)的区别在于它从Y轴而不是X轴测量角度。这意味着零的结果是直接向下(在正Y轴上)指示了线段点,使它适合与默认向上面的图示一起使用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x1 | number | 否 | 第一点的x坐标. |
| y1 | number | 否 | 第一点的y坐标 |
| x2 | number | 否 | 第二点的x坐标. |
| y2 | number | 否 | 第二点的y坐标. |


**返回值:** number - 弧度角度.


> 源码：[src/math/angle/BetweenY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/BetweenY.js#L7)  
引入版本：3.0.0


---

### CounterClockwise {#CounterClockwise}

#### \<static> CounterClockwise(angle) {#static-counterclockwiseangle}


**说明:**

取Phaser默认顺时针格式的一个角度,将其转换为0为北,90为西,180为南,270为东,因此运行逆时针而不是顺时针.

您可以使用 :

```javascript
var converted = CounterClockwise(gameobject.rotation);
```

此函数的所有值都以弧度表示.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| angle | number | 否 | 转换角度,用弧度表示. |


**返回值:** number - 转换角度,用弧度表示.


> 源码：[src/math/angle/CounterClockwise.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/CounterClockwise.js#L9)  
引入版本：3.16.0


---

### GetClockwiseDistance {#GetClockwiseDistance}

#### \<static> GetClockwiseDistance(angle1, angle2) {#static-getclockwisedistanceangle1-angle2}


**说明:**

从角度1到角度2,获得顺时针(非负向)角距离.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| angle1 | number | 否 | 弧度的起始角度. |
| angle2 | number | 否 | 弧度中的目标角度. |


**返回值:** number - 弧度的距离,在范围[0, 2pi].


> 源码：[src/math/angle/GetClockwiseDistance.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/GetClockwiseDistance.js#L9)  
引入版本：4.0.0


---

### GetCounterClockwiseDistance {#GetCounterClockwiseDistance}

#### \<static> GetCounterClockwiseDistance(angle1, angle2) {#static-getcounterclockwisedistanceangle1-angle2}


**说明:**

返回反时针角距 `angle1` 到 `angle2`, 以弧度表示非正值。 反时针旋转表示为负值, 结果是总是在( 2 ) 范围内( 2 , 0) 。 0 的结果意味着角度是等值的, 或者是完全旋转而有所不同的 。 如果您需要测量逆时针旋转到目标角度的距离, 请使用此方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| angle1 | number | 否 | 弧度的起始角度. |
| angle2 | number | 否 | 弧度中的目标角度. |


**返回值:** number - 逆时针距离以弧度计,在范围(2  ,0).


> 源码：[src/math/angle/GetCounterClockwiseDistance.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/GetCounterClockwiseDistance.js#L12)  
引入版本：4.0.0


---

### GetShortestDistance {#GetShortestDistance}

#### \<static> GetShortestDistance(angle1, angle2) {#static-getshortestdistanceangle1-angle2}


**说明:**

获得最短的签名角距从角度1到角度2. 阳性距离是顺时针旋转,阴性距离是逆时针旋转.

度数计算时使用[Phaser.Math.Angle.ShortestBetween](/api/namespace/math-angle#ShortestBetween)代替.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| angle1 | number | 否 | 弧度的第一个角度. |
| angle2 | number | 否 | 弧度的第二个角度. |


**返回值:** number - 弧度的距离,在范围[-pi,pii].


> 源码：[src/math/angle/GetShortestDistance.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/GetShortestDistance.js#L9)  
引入版本：4.0.0


---

### Normalize {#Normalize}

#### \<static> Normalize(angle) {#static-normalizeangle}


**说明:**

将一个角度规范到 [0, 2pi] 范围 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| angle | number | 否 | 正常角度,用弧度表示。 |


**返回值:** number - 平整角度,用弧度表示


> 源码：[src/math/angle/Normalize.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/Normalize.js#L7)  
引入版本：3.0.0


---

### Random {#Random}

#### \<static> Random() {#static-random}


**说明:**

返回范围 [-pi, pi] 中的随机角度。


**返回值:** number - 角度,用弧度表示。


> 源码：[src/math/angle/Random.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/Random.js#L10)  
引入版本：3.23.0


---

### RandomDegrees {#RandomDegrees}

#### \<static> RandomDegrees() {#static-randomdegrees}


**说明:**

返回范围 [-180, 180] 中的随机角度。


**返回值:** number - 角度,以度计。


> 源码：[src/math/angle/RandomDegrees.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/RandomDegrees.js#L10)  
引入版本：3.23.0


---

### Reverse {#Reverse}

#### \<static> Reverse(angle) {#static-reverseangle}


**说明:**

反转给定角度, 将 Q 弧度 (180度) 加入到它上, 然后将结果正常化到 . [0] 2 的 范围。 这返回指向正反方向的角度到所提供的角度 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| angle | number | 否 | 反向角度,用弧度表示. |


**返回值:** number - 反向角度,用弧度表示。


> 源码：[src/math/angle/Reverse.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/Reverse.js#L9)  
引入版本：3.0.0


---

### RotateTo {#RotateTo}

#### \<static> RotateTo(currentAngle, targetAngle, [lerp]) {#static-rotatetocurrentangle-targetangle-lerp}


**说明:**

旋转 `currentAngle` 向 `targetAngle`,使用最短的旋转距离。 `lerp` 参数是此调用中要旋转的金额。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| currentAngle | number | 否 |  | 以弧度表示的当前角度. |
| targetAngle | number | 否 |  | 目标角度旋转到弧度 |
| lerp | number | 是 | 0.05 | 步大小,以弧度表示,在此调用中旋转。角度将按此量向目标旋转,或增或减,视旋转方向最短而定。 |


**返回值:** number - 调整角度 。


> 源码：[src/math/angle/RotateTo.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/RotateTo.js#L9)  
引入版本：3.0.0


---

### ShortestBetween {#ShortestBetween}

#### \<static> ShortestBetween(angle1, angle2) {#static-shortestbetweenangle1-angle2}


**说明:**

得到最短的角度 在`angle1`和`angle2`之间。

这两个角度必须在−180至180之间,这是`sprite.angle`使用的相同的夹角范围,因此可以用两个图案角度通过这种方法,并在两个角度之间获得最短的角度回溯.

返回的角度将处于相同的范围。 如果返回的角度大于 0, 则它是一个逆时针旋转, 如果 &lt; 0, 那么它是一个顺时针旋转 。

在弧度计算时,使用[Phaser.Math.Angle.GetShortestDistance](/api/namespace/math-angle#GetShortestDistance)代替.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| angle1 | number | 否 | 射程的第一个角度 -180到180. |
| angle2 | number | 否 | 射程的第二个角度 -180到180. |


**返回值:** number - 最短的角度, 以度计。 如果大于零, 则逆时针旋转 。


> 源码：[src/math/angle/ShortestBetween.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/ShortestBetween.js#L7)  
引入版本：3.0.0


---

### Wrap {#Wrap}

#### \<static> Wrap(angle) {#static-wrapangle}


**说明:**

绕一个角度。

将角度包成 -PI 到 PI 范围的值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| angle | number | 否 | 角度要包围,用弧度表示. |


**返回值:** number - 包裹的角,用弧度表示.


> 源码：[src/math/angle/Wrap.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/Wrap.js#L9)  
引入版本：3.0.0


---

### WrapDegrees {#WrapDegrees}

#### \<static> WrapDegrees(angle) {#static-wrapdegreesangle}


**说明:**

以度来包着角度 。

将角度围成 -180 至 180 之间的数值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| angle | number | 否 | 角度要包扎,以度计. |


**返回值:** number - 包裹的角,以度计。


> 源码：[src/math/angle/WrapDegrees.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/WrapDegrees.js#L9)  
引入版本：3.0.0


---

---
