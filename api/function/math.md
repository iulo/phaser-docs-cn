# Phaser.Math.Angle {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/function/math)

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


### Random {#Random}

#### \<static> Random() {#static-random}


**说明:**

返回范围 [-pi, pi] 中的随机角度。


**返回值:** number - 角度,用弧度表示。


> 源码：[src/math/angle/Random.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/Random.js#L10)  
引入版本：3.23.0


### RandomDegrees {#RandomDegrees}

#### \<static> RandomDegrees() {#static-randomdegrees}


**说明:**

返回范围 [-180, 180] 中的随机角度。


**返回值:** number - 角度,以度计。


> 源码：[src/math/angle/RandomDegrees.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/angle/RandomDegrees.js#L10)  
引入版本：3.23.0


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


### Average {#Average}

#### \<static> Average(values) {#static-averagevalues}


**说明:**

计算给定值的平均值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| values | Array.\<number> | 否 | 值为平均值. |


**返回值:** number - 平均值。


> 源码：[src/math/Average.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Average.js#L7)  
引入版本：3.0.0


### Bernstein {#Bernstein}

#### \<static> Bernstein(n, i) {#static-bernsteinn-i}


**说明:**

计算伯恩施泰因基础多诺系数,作为贝塞尔曲线计算中的加权系数。结果为二元系数n / (i! * (n-i)!),它决定了`i`在学位-`n`贝塞尔曲线上的影响力点。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| n | number | 否 | 伯恩斯坦多诺米亚的学位 |
| i | number | 否 | 基础函数的索引. |


**返回值:** number - 伯恩斯坦基准系数: 系数(n)/系数(i)/系数(n-i)。


> 源码：[src/math/Bernstein.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Bernstein.js#L9)  
引入版本：3.0.0


### Between {#Between-1}

#### \<static> Between(min, max) {#static-betweenmin-max}


**说明:**

计算 `min`值和 `max`值之间的随机整数,包含在内.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| min | number | 否 | 最低值。 。 |
| max | number | 否 | 最大值( 最大值 ) 。 |


**返回值:** number - 随机整数.


> 源码：[src/math/Between.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Between.js#L7)  
引入版本：3.0.0


### CatmullRom {#CatmullRom}

#### \<static> CatmullRom(t, p0, p1, p2, p3) {#static-catmullromt-p0-p1-p2-p3}


**说明:**

使用0.5的百分位α计算出从给定控制点推导的 Catmull-Rom 值。插值发生在 `p1` 财务报告和已审计财务报表 `p2`,与 `p0` 财务报告和已审计财务报表 `p3` 提供段段每一端的正切上下文。 `t = 0` 结果等于 `p1`; 时间 `t = 1` 结果等于 `p2`.

此函数被Phaser的Speline曲线执行器内部使用,生成通过每个控制点的平滑,连续的曲线.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 插值因子,一般在0到1之间. |
| p0 | number | 否 | 第一个控制点(影响`p1`的切合点). |
| p1 | number | 否 | 第二控制点(插座段的起始). |
| p2 | number | 否 | 第三控制点(插座段的结束). |
| p3 | number | 否 | 第四控制点(影响`p2`的切值). |


**返回值:** number - 插值为`p1`和`p2`之间的Catmull-Rom值.


> 源码：[src/math/CatmullRom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/CatmullRom.js#L7)  
引入版本：3.0.0


### CeilTo {#CeilTo}

#### \<static> CeilTo(value, [place], [base]) {#static-ceiltovalue-place-base}


**说明:**

赛尔斯给一个特定的值 最近的倍数的`base` 升到`place`的功率。

电话 `place` 由适用于下列权利来代表: `base` 。例如,默认基准为 10, a `place` 以 0 舍入到最接近的整数中,a `place` 以1  至最接近的0.1  为单位,a `place` 1 头到10头。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 值为  . |
| place | number | 是 | 0 | 盖之所至. |
| base | number | 是 | 10 | 切入的基数。 十进制默认为十进制 。 |


**返回值:** number - 彩色值。 。


> 源码：[src/math/CeilTo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/CeilTo.js#L7)  
引入版本：3.0.0


### Clamp {#Clamp}

#### \<static> Clamp(value, min, max) {#static-clampvalue-min-max}


**说明:**

强制在边界内一个值, 把它夹在`min`,`max`的射程上。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 被夹住的值 。 |
| min | number | 否 | 最小界限。 |
| max | number | 否 | 最大界限。 |


**返回值:** number - 夹着的值。


> 源码：[src/math/Clamp.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Clamp.js#L7)  
引入版本：3.0.0


### DegToRad {#DegToRad}

#### \<static> DegToRad(degrees) {#static-degtoraddegrees}


**说明:**

从度转换给定角度, 以弧度转换为等角 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| degrees | number | 否 | 角度( 以度计) 转换为弧度 。 |


**返回值:** number - 给定的角度转换成弧度.


> 源码：[src/math/DegToRad.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/DegToRad.js#L9)  
引入版本：3.0.0


### Difference {#Difference}

#### \<static> Difference(a, b) {#static-differencea-b}


**说明:**

计算两个给定数字的正差。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | number | 否 | 计算中的第一个数字。 |
| b | number | 否 | 算法中第二数. |


**返回值:** number - 两者的正差 给定的数字。


> 源码：[src/math/Difference.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Difference.js#L7)  
引入版本：3.0.0


### Factorial {#Factorial}

#### \<static> Factorial(value) {#static-factorialvalue}


**说明:**

计算一个数值的因数,以表示大于 0 的整数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 计算因子的正整数 。 |


**返回值:** number - 给定数的因子.


> 源码：[src/math/Factorial.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Factorial.js#L7)  
引入版本：3.0.0


### FloatBetween {#FloatBetween}

#### \<static> FloatBetween(min, max) {#static-floatbetweenmin-max}


**说明:**

生成两个给定界限之间的随机浮点数,最小包容性,最大独占性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| min | number | 否 | 下界为浮,含之. |
| max | number | 否 | 上界为浮,独行. |


**返回值:** number - 任意浮动在给定范围内 。


> 源码：[src/math/FloatBetween.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/FloatBetween.js#L7)  
引入版本：3.0.0


### FloorTo {#FloorTo}

#### \<static> FloorTo(value, [place], [base]) {#static-floortovalue-place-base}


**说明:**

与`base`相比,某个地方的楼层,十进制位数为10。

`place`代表的是`base`应用的电源,以获得那个位置.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 价值到地板。 |
| place | number | 是 | 0 | 地上到楼下的地方 |
| base | number | 是 | 10 | 底部到底部。 十进制默认为十进制 。 |


**返回值:** number - 底价 额


> 源码：[src/math/FloorTo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/FloorTo.js#L7)  
引入版本：3.0.0


### FromPercent {#FromPercent}

#### \<static> FromPercent(percent, min, [max]) {#static-frompercentpercent-min-max}


**说明:**

返回基于 `min` 和 `max` 之间的范围以及给出的百分比的值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| percent | number | 否 | 代表百分比的值,介于0到1之间,在此范围以外的值被夹住。 |
| min | number | 否 | 最低值。 。 |
| max | number | 是 | 最大值( 最大值 ) 。 |


**返回值:** number - 值是`percent`% 在`min`和`max`之间。


> 源码：[src/math/FromPercent.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/FromPercent.js#L9)  
引入版本：3.0.0


### GetCentroid {#GetCentroid}

#### \<static> GetCentroid(points, [out]) {#static-getcentroidpoints-out}


**说明:**

获取平面图的中间或几何中心(图中所有点的算术平均位置),非正式地,它是在针尖上切除形状时完全平衡的点。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| points | Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 否 | 一组像矢量2一样的物体,以获得几何中心。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储输出坐标的矢量2 对象。 如果未给出, 则创建新的矢量2 实例 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 代表给定点几何中心的一个矢量2天体。


> 源码：[src/math/GetCentroid.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/GetCentroid.js#L9)  
引入版本：4.0.0


### GetSpeed {#GetSpeed}

#### \<static> GetSpeed(distance, time) {#static-getspeeddistance-time}


**说明:**

计算在特定时间覆盖特定距离所需的速度 。

距离被假定为像素,时间被给出为秒,结果以像素每毫秒返回.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| distance | number | 否 | 旅行的距离,以像素表示. |
| time | number | 否 | 允许的时段 覆盖距离,以秒计。 |


**返回值:** number - 所需速度,以每毫秒像素计.


> 源码：[src/math/GetSpeed.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/GetSpeed.js#L7)  
引入版本：3.0.0


### GetVec2Bounds {#GetVec2Bounds}

#### \<static> GetVec2Bounds(points, [out]) {#static-getvec2boundspoints-out}


**说明:**

从数组点计算轴对齐的边框(或abb)。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| points | Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 否 | 用于获取 AABB 的矢量2类似对象的阵列 。 |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 一个用于存储结果的矩形对象。如果不给出,则创建新的矩形实例。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 矩形对象,为给定点持有 AABB 值。


> 源码：[src/math/GetVec2Bounds.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/GetVec2Bounds.js#L9)  
引入版本：4.0.0


### Hash {#Hash}

#### \<static> Hash(vector, [algorithm]) {#static-hashvector-algorithm}


**说明:**

挂载数字或数字列表.

散列是输入的不可预测的转换,它总是从相同的输入返回相同的输出。它对于以可预测的方式生成随机数据是有用的。

例如,您可以用散列来将物体放置在某个场景周围。由于输入相同,物体总是出现在同一个地方,尽管这些地方是随机的。

此函数以1-4数字作为输入,并从0-1返回一个单数.

免责声明: 此功能旨在高效生成视觉多样性, 并非用于加密。 不要用于安全/ 认证/ 加密目的。 使用一个合适的工具 。

性能说明:一个16ms帧有足够的时间产生数万或数十万个散列值,这取决于系统和其他活动.

您可以从不同的散列算法中选择 。

- 0: TRIG. 这使用正弦函数和点产品来散开输入.

- 1: PCG. 这使用一个穿透的相容发生器来将输入进行散列,

  ,但仅限于整数输入。

- 2: PCG_FLOAT. PCG的这个变体接受浮点输入.

TRIG 是 Phaser 4 噪声对象和亲缘关系中使用的相同算法。 它产生像样的品种, 并且接受任意数字作为输入。 它的精度是32位。 如果大于 32位( 4294967296) , 它的输入值可能会失去区分 。 它的输出值不能超过 1/ 4294967296。 这个算法旨在对图形硬件工作, 因为它缺乏位移能力, 并且不是最先进的 。

PCG 是 Permuted Congrusic 生成器。 有关该理论的更多信息, 请参看 [https://www.pcg-random.org/](https://www.pcg-random.org/) 。 这个算法更现代, 被认为质量更高。 它运行的稍快于TRIG。 它只接受全数( integers) 作为输入, 它的精度为32位, 如果大于32位( 4294967296) , 它的输入值可能会失去区分 。 它的输出值不能超过 1/4294967296 。

PCG_FLOAT 工作与 PCG 相同, 但接受浮点输入。 这个转换过程使其运行速度略慢于 TRIG 。 同样的精度关切也适用 。

如果您的散列值开始集群, 您可能会在安全区域之外使用值, 精确度比特不足。 您可以通过循环路径的采样来将值保持在安全区域。 这就是为什么输入的多个维度是有用的 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| vector | number \| Array.\<number> | 否 |  | 散列编号或编号列表 1到4 个数字. |
| algorithm | number | 是 | 0 | 使用的算法. 0是TRIG. 1是PCG. 2是PCG_FLOAT. |


**返回值:** number - - 0 -1的号码


> 源码：[src/math/Hash.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Hash.js#L11)  
引入版本：4.0.0


### HashCell {#HashCell}

#### \<static> HashCell(vector, [config]) {#static-hashcellvector-config}


**说明:**

将数字或数字列表显示为细胞噪声值 。

散列是输入的不可预测的转换,它总是从相同的输入返回相同的输出。它对于以可预测的方式生成随机数据是有用的。

细胞噪声使用散列来扭曲一个网格,在连续模式中创建独特的“细胞”。虽然结果仍然是随机的,但它是连续的:非常相似的输入输出非常相似(尽管细胞之间可能有一些轻微的不连续)。结果有一个明显的突起模式。这是Game Objects的NoiseCell2D家族所使用的算法,有时它被称为Worley或Voronia噪声。

例如,您可以使用蜂窝噪声来创造一系列跨越程序地形的山脊。每次生成同一个区域,它就会看起来是一样的。

此函数以1-4 数字作为输入,返回一个数字。返回数的范围随着输入数的增加而增加。它是从输入矢量到最近的扭曲单元格中心的距离。在更高的维度中,可能的距离更大。

注意: 如果您在配置参数中指定了维度属性, 请至少确保它们与输入向量相同。 缺少值会损坏结果 。

免责声明: 此功能旨在高效生成视觉多样性, 并非用于加密。 不要用于安全/ 认证/ 加密目的。 使用一个合适的工具 。

性能说明:一个16ms帧有足够的时间产生几百个散列值,这取决于设备与工作量.

关于散列算法的更多信息,请参见[Phaser.Math.Hash](/api/namespace/math#Hash).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vector | number \| Array.\<number> | 否 | 输入矢量为散列数。 1 至 4 个数字 。 |
| config | [Phaser.Types.Math.HashCellConfig](/api/typedef/types-math#hashcellconfig) | 是 | 噪声细胞场的配置. |


**返回值:** number - 散列细胞噪声值。 范围随着输入维度的增多而增加, 因为它代表了距离最近的扭曲细胞中心。


> 源码：[src/math/HashCell.js#L3](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/HashCell.js#L3)  
引入版本：4.0.0


### HashSimplex {#HashSimplex}

#### \<static> HashSimplex(vector, [config]) {#static-hashsimplexvector-config}


**说明:**

将数字或数字列表排列为简单的x噪声值 。

散列是输入的不可预测的转换,它总是从相同的输入返回相同的输出。它对于以可预测的方式生成随机数据是有用的。

输出范围为−1至1.

您可以设置配置对象来控制输出。 您可以添加八进制的细节, 添加一个动荡曲折的曲折, 调整梯度流, 并设置随机性种子 。

Simplex噪声是Perlin噪声的一种演化,两者都是Ken Perlin发明的,是一种梯度噪声的形式,它形成了一个平滑连续的场:非常相似的输入输出非常相似,尽管场本身仍然是随机的.

Simplex噪声通过指定任意的渐变点在网格上,将空间分割成网格细胞(使用最小的三角形状称为simplex),识别输入的网格细胞属于哪个网格,以及该网格的梯度之间的混合.

此版本使用流参数来动画噪声字段。流值会旋转所处的梯度,从而形成周期性移位模式。

此执行会刻意复制 `NoiseSimplex2D` 和 `NoiseSimplex3D` 游戏对象的阴影。 它们的行为类似, 配置对象也非常相似。 HashSimplex 不支持值因子/ add/ power 术语, 因为您可以自己处理输出 。

HashSimprex 也支持一维输入。 这自动添加到2维。

Simplex 性能因八进制和曲速设置而异。您可能根据设备及工作量计算每毫秒一千或多少散列。

注意: 如果您在配置参数中指定了维度属性, 请至少确保它们与输入向量相同。 缺少值会损坏结果 。

免责声明: 此功能旨在高效生成视觉多样性, 并非用于加密。 不要用于安全/ 认证/ 加密目的。 使用一个合适的工具 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vector | number \| Array.\<number> | 否 | 输入矢量为散列数。 1 到 3 个数字 。 |
| config | [Phaser.Types.Math.HashSimplexConfig](/api/typedef/types-math#hashsimplexconfig) | 是 | 噪声场的配置. |


**返回值:** number - 噪声值在 - 1 到 1 之间 。


> 源码：[src/math/HashSimplex.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/HashSimplex.js#L1)  
引入版本：4.0.0


### IsEven {#IsEven}

#### \<static> IsEven(value) {#static-isevenvalue}


**说明:**

检查某个值是否为偶数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 用来检查的号码 。 |


**返回值:** boolean - 数数是否均.


> 源码：[src/math/IsEven.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/IsEven.js#L7)  
引入版本：3.0.0


### IsEvenStrict {#IsEvenStrict}

#### \<static> IsEvenStrict(value) {#static-isevenstrictvalue}


**说明:**

使用严格的类型检查检查给定的值是否为偶数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 用来检查的号码 。 |


**返回值:** boolean - 数数是否均.


> 源码：[src/math/IsEvenStrict.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/IsEvenStrict.js#L7)  
引入版本：3.0.0


### Linear {#Linear}

#### \<static> Linear(p0, p1, t) {#static-linearp0-p1-t}


**说明:**

在两个值之间进行线性插值,返回该值 `t` 中间的% `p0` 财务报告和已审计财务报表 `p1`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| p0 | number | 否 | 第一义. |
| p1 | number | 否 | 第二义. |
| t | number | 否 | p0和p1之间返回的百分比,为0和1之间的数字。 |


**返回值:** number - p0和p1之间的插值,位于位置t.


> 源码：[src/math/Linear.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Linear.js#L7)  
引入版本：3.0.0


### LinearXY {#LinearXY}

#### \<static> LinearXY(vector1, vector2, [t]) {#static-linearxyvector1-vector2-t}


**说明:**

将两个给定的矢量,并在它们之间返回一个新的矢量.

不得修改任何经过的矢量。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| vector1 | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 |  | 开始的矢量2从中插出. |
| vector2 | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 |  | 终结的矢量2 插到。 |
| t | number | 是 | 0 | 向量1和向量2之间的返回百分比,以0到1之间的数字表示。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 向量1 和向量2 之间的步骤 t% 。


> 源码：[src/math/LinearXY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/LinearXY.js#L7)  
引入版本：3.60.0


### MaxAdd {#MaxAdd}

#### \<static> MaxAdd(value, amount, max) {#static-maxaddvalue-amount-max}


**说明:**

将`amount`加到`value`上,将最大结果限制在`max`上.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 增益之值. |
| amount | number | 否 | 拟加之数. |
| max | number | 否 | 返回的最大值 。 |


**返回值:** number - 由此而来的价值.


> 源码：[src/math/MaxAdd.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/MaxAdd.js#L7)  
引入版本：3.0.0


### Median {#Median}

#### \<static> Median(values) {#static-medianvalues}


**说明:**

计算给定值的中值。这些值被排序,中间值被返回。如果值数为偶数,则返回两个中间值的平均值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| values | Array.\<number> | 否 | 查找中位数的值 。 |


**返回值:** number - 中值(一说为"中值").


> 源码：[src/math/Median.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Median.js#L7)  
引入版本：3.54.0


### MinSub {#MinSub}

#### \<static> MinSub(value, amount, min) {#static-minsubvalue-amount-min}


**说明:**

从`value`中减掉一个`amount`,将最小结果限制在`min`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 要从中减去的值 。 |
| amount | number | 否 | 减之数. |
| min | number | 否 | 最小值返回。 |


**返回值:** number - 由此而来的价值.


> 源码：[src/math/MinSub.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/MinSub.js#L7)  
引入版本：3.0.0


### Percent {#Percent}

#### \<static> Percent(value, min, [max], [upperMax]) {#static-percentvalue-min-max-uppermax}


**说明:**

确定百分比 `value` 位于 `min` 财务报告和已审计财务报表 `max`。如果 `max` 默认为 `min + 1`,给出宽度 1 的单位范围,起始于 `min`.

您可以选择指定一个 `upperMax` 值, 即代表100% 的 范围的中点, 之后% 开始再次降至 0 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 确定百分比的值。 |
| min | number | 否 | 最低值。 。 |
| max | number | 是 | 最大值( 最大值 ) 。 |
| upperMax | number | 是 | 代表100%的射程中点. |


**返回值:** number - 数值在0至1之间,代表百分比。


> 源码：[src/math/Percent.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Percent.js#L7)  
引入版本：3.0.0


### RadToDeg {#RadToDeg}

#### \<static> RadToDeg(radians) {#static-radtodegradians}


**说明:**

将给定的弧度角度转换为等角度角度.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| radians | number | 否 | 弧度的角度转换成度. |


**返回值:** number - 给定的角度转换为度 。


> 源码：[src/math/RadToDeg.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RadToDeg.js#L9)  
引入版本：3.0.0


### RandomXY {#RandomXY}

#### \<static> RandomXY(vector, [scale]) {#static-randomxyvector-scale}


**说明:**

计算随机单位矢量。

计算到 -1 和 1 之间的向量随机值,用于表示方向。

可选接受一个比例值来缩放所产生的矢量 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| vector | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 |  | 用于计算随机值的矢量。 |
| scale | number | 是 | 1 | 随机值的尺度 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 给定的矢量。


> 源码：[src/math/RandomXY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RandomXY.js#L7)  
引入版本：3.0.0


### RandomXYZ {#RandomXYZ}

#### \<static> RandomXYZ(vec3, [radius]) {#static-randomxyzvec3-radius}


**说明:**

计算给定半径球体表面的随机位置矢量。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| vec3 | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 |  | 用于计算随机值的矢量。 |
| radius | number | 是 | 1 | 球体的半径. |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 给定的矢量。


> 源码：[src/math/RandomXYZ.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RandomXYZ.js#L7)  
引入版本：3.0.0


### RandomXYZW {#RandomXYZW}

#### \<static> RandomXYZW(vec4, [scale]) {#static-randomxyzwvec4-scale}


**说明:**

计算随机四维矢量.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| vec4 | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 |  | 用于计算随机值的矢量。 |
| scale | number | 是 | 1 | 随机值的尺度 。 |


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 给定的矢量。


> 源码：[src/math/RandomXYZW.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RandomXYZW.js#L7)  
引入版本：3.0.0


### Rotate {#Rotate}

#### \<static> Rotate(point, angle) {#static-rotatepoint-angle}


**说明:**

绕原点(0,0)绕一个特定角度旋转一个定点,反时针方向.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 所要旋转之点. |
| angle | number | 否 | 旋转角度,以弧度表示,呈逆时针方向. |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 给定点,由给定角度在逆时针方向旋转.


> 源码：[src/math/Rotate.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Rotate.js#L7)  
引入版本：3.0.0


### RotateAround {#RotateAround}

#### \<static> RotateAround(point, x, y, angle) {#static-rotatearoundpoint-x-y-angle}


**说明:**

旋转 a `point` 环绕 `x` 财务报告和已审计财务报表 `y` 由给定的 `angle`在同一距离上 , 在同一距离上 。

在极性标记中,这个图将一个点从(r, t)到(r, t + 角度),对应于起源(x, y).

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 所要旋转之点. |
| x | number | 否 | 横向坐标旋转. |
| y | number | 否 | 垂直坐标旋转。 |
| angle | number | 否 | 弧度旋转的角度. |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 给定的点。


> 源码：[src/math/RotateAround.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RotateAround.js#L7)  
引入版本：3.0.0


### RotateAroundDistance {#RotateAroundDistance}

#### \<static> RotateAroundDistance(point, x, y, angle, distance) {#static-rotatearounddistancepoint-x-y-angle-distance}


**说明:**

旋转 a `point` 环绕 `x` 财务报告和已审计财务报表 `y` 由给定的 `angle` 财务报告和已审计财务报表 `distance`.

在极性标记中,这个图将一个点从(r, t)到(距离, t + 角度),对应于起源(x, y).

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 所要旋转之点. |
| x | number | 否 | 横向坐标旋转. |
| y | number | 否 | 垂直坐标旋转。 |
| angle | number | 否 | 弧度旋转的角度. |
| distance | number | 否 | 距离(x,y)将点放在位置. |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 给定的点。


> 源码：[src/math/RotateAroundDistance.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RotateAroundDistance.js#L7)  
引入版本：3.0.0


### RotateTo {#RotateTo-1}

#### \<static> RotateTo(point, x, y, angle, distance) {#static-rotatetopoint-x-y-angle-distance}


**说明:**

立场a `point` 给定的 `angle` 财务报告和已审计财务报表 `distance` 改为(a)`x`, `y`).

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 位置的点。 |
| x | number | 否 | 水平坐标从位置。 |
| y | number | 否 | 垂直坐标从位置。 |
| angle | number | 否 | 弧度旋转的角度. |
| distance | number | 否 | 距离(x,y)将点放在位置. |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 给定的点。


> 源码：[src/math/RotateTo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RotateTo.js#L7)  
引入版本：3.24.0


### RotateVec3 {#RotateVec3}

#### \<static> RotateVec3(vec, axis, radians) {#static-rotatevec3vec-axis-radians}


**说明:**

以轴角旋转一个矢量。

这与轴角四角线变换一个点相同,但精度更高.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vec | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 向量要旋转 。 |
| axis | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 轴以旋转. |
| radians | number | 否 | 弧度旋转的角度. |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 给定的向量.


> 源码：[src/math/RotateVec3.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RotateVec3.js#L15)  
引入版本：3.0.0


### RoundAwayFromZero {#RoundAwayFromZero}

#### \<static> RoundAwayFromZero(value) {#static-roundawayfromzerovalue}


**说明:**

绕一个给定的数字,使它离零更远。也就是说,正数被四舍五入,负数被四舍五入。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 数至圆. |


**返回值:** number - 圆数,从零舍去.


> 源码：[src/math/RoundAwayFromZero.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RoundAwayFromZero.js#L7)  
引入版本：3.0.0


### RoundTo {#RoundTo}

#### \<static> RoundTo(value, [place], [base]) {#static-roundtovalue-place-base}


**说明:**

圆向给定精度的值 。

例如:

```javascript
RoundTo(123.456, 0) = 123
RoundTo(123.456, 1) = 120
RoundTo(123.456, 2) = 100
```

以负的 `place` 键绕小数,即圆至精度:

```javascript
RoundTo(123.456789, 0) = 123
RoundTo(123.456789, -1) = 123.5
RoundTo(123.456789, -2) = 123.46
RoundTo(123.456789, -3) = 123.457
```

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 值为圆. |
| place | number | 是 | 0 | 圆形位置 圆形单位 负形单位 圆形单位 圆形单位 圆形单位 圆形单位 圆形单位 圆形单位 |
| base | number | 是 | 10 | 圆形的底部。 十进制默认为十进制 。 |


**返回值:** number - 圆数.


> 源码：[src/math/RoundTo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RoundTo.js#L7)  
引入版本：3.0.0


### SmootherStep {#SmootherStep}

#### \<static> SmootherStep(x, min, max) {#static-smootherstepx-min-max}


**说明:**

计算比较平滑的插值百分比 `x` 介于 `min` 财务报告和已审计财务报表 `max`.

函数接收到编号`x`作为参数,如果`x`小于或等于左边缘,如果`x`大于或等于右边缘,则返回0,如果使用一个赫米特多诺米法,则返回1,否则返回0。

产生比[Phaser.Math.SmoothStep](/api/namespace/math#SmoothStep)更平滑的插值.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 输入值. |
| min | number | 否 | 最小值,又称"左边",假定比"右边"小. |
| max | number | 否 | 最大值,又称"右边缘",假定值大于"左边缘". |


**返回值:** number - 插值的百分比,在0到1之间.


> 源码：[src/math/SmootherStep.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/SmootherStep.js#L7)  
引入版本：3.0.0


### SmoothStep {#SmoothStep}

#### \<static> SmoothStep(x, min, max) {#static-smoothstepx-min-max}


**说明:**

计算平滑插值百分比 `x` 介于 `min` 财务报告和已审计财务报表 `max`.

函数接收到编号`x`作为参数,如果`x`小于或等于左边缘,如果`x`大于或等于右边缘,则返回0,如果使用一个赫米特多诺米法,则返回1,否则返回0。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 输入值. |
| min | number | 否 | 最小值,又称"左边",假定比"右边"小. |
| max | number | 否 | 最大值,又称"右边缘",假定值大于"左边缘". |


**返回值:** number - 插值的百分比,在0到1之间.


> 源码：[src/math/SmoothStep.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/SmoothStep.js#L7)  
引入版本：3.0.0


### ToXY {#ToXY}

#### \<static> ToXY(index, width, height, [out]) {#static-toxyindex-width-height-out}


**说明:**

返回一个矢量2,其中包含给定索引在 a 中的 x 和 y 位置 `width` ưμ㼯A `height` 大小网格.

例如,在6×4格子中,指数16等于x:4y:2.

如果给定的索引超出范围,则返回一个带有x和y设置为0的矢量2。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 网格内的位置以获取 x/y 值 。 |
| width | number | 否 | 网格的宽度. |
| height | number | 否 | 网格的高度. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 保存结果的可选矢量2。 如果不给出, 将会创建一个新的矢量2 实例 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 包含从给定索引中衍生出来的x和y网格坐标的矢量2。


> 源码：[src/math/ToXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/ToXY.js#L9)  
引入版本：3.19.0


### TransformXY {#TransformXY}

#### \<static> TransformXY(x, y, positionX, positionY, rotation, scaleX, scaleY, [output]) {#static-transformxyx-y-positionx-positiony-rotation-scalex-scaley-output}


**说明:**

取`x`和`y`坐标并将其转换为指定位置、旋转和比例值定义的局部坐标空间。这进行反向转换,将一个点从世界空间转换成游戏对象或其他变形实体的等效局部空间坐标。当您需要确定一个世界空间点位于变形对象局部坐标系统之内时,这可用于命中测试或指针输入。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 将转换的x坐标 。 |
| y | number | 否 | 调和Y要转换。 |
| positionX | number | 否 | 变点的水平位置 。 |
| positionY | number | 否 | 变点的垂直位置 。 |
| rotation | number | 否 | 变点旋转,以弧度表示. |
| scaleX | number | 否 | 变位点的横向尺度 。 |
| scaleY | number | 否 | 变点的垂直尺度。 |
| output | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 | 翻译坐标的输出矢量、点或对象。 |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 译之点.


> 源码：[src/math/TransformXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/TransformXY.js#L9)  
引入版本：3.0.0


### Within {#Within}

#### \<static> Within(a, b, tolerance) {#static-withina-b-tolerance}


**说明:**

检查这两个值是否在对方给定的 `tolerance` 内 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | number | 否 | 计算中使用的第一个值。 |
| b | number | 否 | 计算中使用的第二个值。 |
| tolerance | number | 否 | 耐受性:任何等于或小于这一数值的,均视为在幅度之内。 |


**返回值:** boolean - 如果`a`和`b`的绝对差小于或等于`tolerance`,则返回`true`.


> 源码：[src/math/Within.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Within.js#L7)  
引入版本：3.0.0


### Wrap {#Wrap-1}

#### \<static> Wrap(value, min, max) {#static-wrapvalue-min-max}


**说明:**

包起来给定 `value` 介于 `min` (包括)和 `max` (排他性).

当值超过`max`时,它会绕回`min`,当值低于`min`时,它就会绕到`max`以下。 这对通过一个范围循环有用,如将一个角度保持在0-360度以内,或者在砖块内循环一个瓦片索引。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 包装值 。 |
| min | number | 否 | 最小范围(包括). |
| max | number | 否 | 范围的最大约束(排他性). |


**返回值:** number - 包裹值,保证在`[min, max)`内.


> 源码：[src/math/Wrap.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Wrap.js#L7)  
引入版本：3.0.0


# Phaser.Math.Distance {#page-title-1}

### Between {#Between-2}

#### \<static> Between(x1, y1, x2, y2) {#static-betweenx1-y1-x2-y2-1}


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


### BetweenPoints {#BetweenPoints-1}

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


# Phaser.Math.Easing.Back {#page-title-2}

### In {#In}

#### \<static> In(v, [overshoot]) {#static-inv-overshoot}


**说明:**

后放。 放松功能在前进前会向相反方向短暂拉回, 在过渡开始时会产生预期效果, 启动后`overshoot`值越高, 值拉越后, 开始前会越低 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | number | 否 |  | 平时的平时值为0到1。 |
| overshoot | number | 是 | 1.70158 | 超射量。 控制值在前进前的后退。 更高的值会产生更明显的后退效果 。 |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/back/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/back/In.js#L7)  
引入版本：3.0.0


### InOut {#InOut}

#### \<static> InOut(v, [overshoot]) {#static-inoutv-overshoot}


**说明:**

后易/出。 此放松功能对双曲的起始和结尾都应用了后退效果: 值在加速前进前先稍回拉, 然后在扣回休息前过度射入目标, 产生对称的弹簧般运动。 如果您想要动画两端的活泼的, 跳动的感觉, 请使用此功能 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | number | 否 |  | 拟解之值. |
| overshoot | number | 是 | 1.70158 | 控制拉回和射出过度的大小。 值较高会产生更显著的效果。 默认在每一端产生大约10%的射出过度 。 |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/back/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/back/InOut.js#L7)  
引入版本：3.0.0


### Out {#Out}

#### \<static> Out(v, [overshoot]) {#static-outv-overshoot}


**说明:**

后放轻松。 双关先快速移动, 然后在返回目标之前超标其最终值。 超标发生在过渡结束时, 给出一个轻微的“ 弹出过去和返回” 效果 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | number | 否 |  | 拟调值,一般在[0, 1] 范围内. |
| overshoot | number | 是 | 1.70158 | 超射量 值较高会导致超射率更明显 |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/back/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/back/Out.js#L7)  
引入版本：3.0.0


# Phaser.Math.Easing.Bounce {#page-title-3}

### In {#In-1}

#### \<static> In(v) {#static-inv}


**说明:**

将弹跳放松应用到 tween 的开始。 弹跳值会在加速向目标移动之前在源头附近“ 弹跳” 几次, 模拟球弹跳在开始移动时的效果。 这就是弹跳效果的易变体, 意思是弹跳效果发生在过渡开始时而不是结束。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟放宽的值,在0到1之间. |


**返回值:** number - 放宽值,在0到1之间.


> 源码：[src/math/easing/bounce/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/bounce/In.js#L7)  
引入版本：3.0.0


### InOut {#InOut-1}

#### \<static> InOut(v) {#static-inoutv}


**说明:**

对给定值应用弹跳易/出效果。这结合了弹跳易/出易效果,在  的始末产生弹跳动画。输入值应在0到1之间,其中0为起始值,1为尾值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/bounce/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/bounce/InOut.js#L7)  
引入版本：3.0.0


### Out {#Out-1}

#### \<static> Out(v) {#static-outv}


**说明:**

将弹出易控效果应用到给定值。 运动会快速启动, 并减速到尾端, 产生弹出效果, 模拟一个球落地, 弹出到停点。 弹出是通过四个片面的四极区段实现的, 它们在沉淀前产生三个递减弹出。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/bounce/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/bounce/Out.js#L7)  
引入版本：3.0.0


# Phaser.Math.Easing.Circular {#page-title-4}

### In {#In-2}

#### \<static> In(v) {#static-inv-1}


**说明:**

应用一个循环易入值。 这种易入值是基于一个圆的方程, 生成一个开始非常缓慢, 然后急剧加速到尾端的曲线。 它是`Circular.Out`的补充, 通常用于动画, 在启动前需要犹豫的开始 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/circular/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/circular/In.js#L7)  
引入版本：3.0.0


### InOut {#InOut-2}

#### \<static> InOut(v) {#static-inoutv-1}


**说明:**

循环易行/出局. 应用一个循环宽松曲线,开始缓慢,通过中点加速,然后减速到平稳的停站. 曲线的形状从一个圆弧的弧形推导出来,产生一种自然易行运动,比正弦易行更渐进,但比四极易行更尖锐. 结合易行和易行使过渡对称性:前半段易行使用圆弧,后半段易行使用镜弧.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟调值,在[0, 1]之间. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/circular/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/circular/InOut.js#L7)  
引入版本：3.0.0


### Out {#Out-2}

#### \<static> Out(v) {#static-outv-1}


**说明:**

以单位圆的方程为基础,对`v`应用循环宽松效应,运动以全速开始,并顺着四分之一圆的曲线顺利减速到一站. `v`应该介于0到1之间.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟放宽的值,在0到1之间. |


**返回值:** number - 放宽值,在0到1之间.


> 源码：[src/math/easing/circular/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/circular/Out.js#L7)  
引入版本：3.0.0


# Phaser.Math.Easing.Cubic {#page-title-5}

### In {#In-3}

#### \<static> In(v) {#static-inv-2}


**说明:**

立方体易动。 开始缓慢且快速, 沿着立方曲线( v3) , 由此产生一个渐进的开始, 并逐渐形成快速的完成, 使它非常适合动画, 物体应该从休息中收集动力 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟调值,一般在[0, 1] 范围内. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/cubic/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/cubic/In.js#L7)  
引入版本：3.0.0


### InOut {#InOut-3}

#### \<static> InOut(v) {#static-inoutv-2}


**说明:**

立方体易行/ 出方。 生成一个 S 曲线, 由零加速, 在中点达到最高速度, 然后减速回零。 加速和减速都遵循一个立方体( t3) 曲线, 给予比四极等效的更强的易行性。 通常用于在过渡中间快速移动时平稳开始和结束的动量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟调值,在[0, 1]之间. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/cubic/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/cubic/InOut.js#L7)  
引入版本：3.0.0


### Out {#Out-3}

#### \<static> Out(v) {#static-outv-2}


**说明:**

立方体易动.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/cubic/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/cubic/Out.js#L7)  
引入版本：3.0.0


# Phaser.Math.Easing.Elastic {#page-title-6}

### In {#In-4}

#### \<static> In(v, [amplitude], [period]) {#static-inv-amplitude-period}


**说明:**

弹性易感,在加速向目标前进之前,值会以弹簧般的运动回旋而行。效果始于一系列小振荡,其规模在扩大,模拟伸缩的弹性带被释放。当您想要在启动时先让一个扭矩感觉春或跳动时,就使用这个功能。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | number | 否 |  | 拟放宽的值,在0到1之间. |
| amplitude | number | 是 | 0.1 | 弹性振荡的振荡度,1以下值被夹到1. 较高的值产生一个更宽的振荡弧. |
| period | number | 是 | 0.1 | 控制正弦波振荡的紧度。 数值越小, 周期就越紧, 周期就越频繁; 数值越大, 波动就越慢。 |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/elastic/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/elastic/In.js#L7)  
引入版本：3.0.0


### InOut {#InOut-4}

#### \<static> InOut(v, [amplitude], [period]) {#static-inoutv-amplitude-period}


**说明:**

弹性易感/ 出动, 既结合易感和易感的易感效果。 这种易感功能在  的始末都会产生弹簧般的振荡, 在安顿前过度射入目标值。 对于需要两端的振荡感的动画来说, 很有用 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | number | 否 |  | 拟调值,一般在[0, 1] 范围内. |
| amplitude | number | 是 | 0.1 | 弹性振荡的振幅,1以下值被夹到1. |
| period | number | 是 | 0.1 | 控制正弦波振荡的紧度。 较小的值会产生周期较多的更紧的波 。 |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/elastic/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/elastic/InOut.js#L7)  
引入版本：3.0.0


### Out {#Out-4}

#### \<static> Out(v, [amplitude], [period]) {#static-outv-amplitude-period}


**说明:**

弹性易变,值在最后值落定前会以衰变正弦波向目标过度射击,振荡。弹性效应发生在过渡结束时,使运动看起来会弹跳或弹簧到位。接受一个在0到1之间的正常输入值`v`。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | number | 否 |  | 通常在[0, 1] 范围内的常态值要加加成的值. |
| amplitude | number | 是 | 0.1 | 弹性射线的振幅。 1 以上的值会增加射线的大小 。 |
| period | number | 是 | 0.1 | 控制正弦波振荡的强度。 数值较小, 产生更快速振荡的更紧的波 。 |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/elastic/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/elastic/Out.js#L7)  
引入版本：3.0.0


# Phaser.Math.Easing.Expo {#page-title-7}

### In {#In-5}

#### \<static> In(v) {#static-inv-3}


**说明:**

证入方便.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/expo/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/expo/In.js#L7)  
引入版本：3.0.0


### InOut {#InOut-5}

#### \<static> InOut(v) {#static-inoutv-3}


**说明:**

指示易入/出。 产生曲线, 使用上半段的指数曲线从零急剧加速, 然后对称减速到平稳的停站。 结果就是一个S形的显著曲线, 它以快速过渡的方式从中点开始和缓慢结束。 对于戏剧动画来说是有用的, 因为它需要强烈的快进和快出效果 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟调值,在[0, 1]之间. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/expo/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/expo/InOut.js#L7)  
引入版本：3.0.0


### Out {#Out-5}

#### \<static> Out(v) {#static-outv-3}


**说明:**

证得方便.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/expo/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/expo/Out.js#L7)  
引入版本：3.0.0


# Phaser.Math.Easing {#page-title-8}

### Linear {#Linear-1}

#### \<static> Linear(v) {#static-linearv}


**说明:**

线性宽松(无变异).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/linear/Linear.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/linear/Linear.js#L7)  
引入版本：3.0.0


### Stepped {#Stepped}

#### \<static> Stepped(v, [steps]) {#static-steppedv-steps}


**说明:**

将输入值量化为若干个零散的平方步的自动放松函数,从而形成阶梯式进程而不是平方曲线。输出在步数之间立即跳动,而不是插值,这对逐帧动画、网格扭曲移动或任何应明显递增的效果都有益。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | number | 否 |  | 拟解之值. |
| steps | number | 是 | 1 | 方便中步数. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/stepped/Stepped.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/stepped/Stepped.js#L7)  
引入版本：3.0.0


# Phaser.Math.Easing.Quadratic {#page-title-9}

### In {#In-6}

#### \<static> In(v) {#static-inv-4}


**说明:**

四释方便.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/quadratic/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quadratic/In.js#L7)  
引入版本：3.0.0


### InOut {#InOut-6}

#### \<static> InOut(v) {#static-inoutv-4}


**说明:**

四方易入/出。 应用四极曲线, 在范围上半段加速, 并在下半段减速, 产生平滑的 S 曲线过渡 。 用于需要轻轻开始的动画, 快速移动到中间, 并在结尾平稳地安顿 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟调值,在[0, 1]之间. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/quadratic/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quadratic/InOut.js#L7)  
引入版本：3.0.0


### Out {#Out-6}

#### \<static> Out(v) {#static-outv-4}


**说明:**

四谛方便解脱.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/quadratic/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quadratic/Out.js#L7)  
引入版本：3.0.0


# Phaser.Math.Easing.Quartic {#page-title-10}

### In {#In-7}

#### \<static> In(v) {#static-inv-5}


**说明:**

夸文易入.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/quartic/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quartic/In.js#L7)  
引入版本：3.0.0


### InOut {#InOut-7}

#### \<static> InOut(v) {#static-inoutv-5}


**说明:**

Quartic 易入/ 出。 应用一个自始至终快速加速的夸尔曲线( 第四力) , 然后急剧减速, 进入尾端。 运动是对称的: 上半半边反射易入, 后半边反射易出。 这比四极或立方宽松更能产生戏剧性的加速和减速, 使其适合快速的高能过渡 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟调值,在[0, 1]之间. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/quartic/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quartic/InOut.js#L7)  
引入版本：3.0.0


### Out {#Out-7}

#### \<static> Out(v) {#static-outv-5}


**说明:**

夸奇式轻松出局.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/quartic/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quartic/Out.js#L7)  
引入版本：3.0.0


# Phaser.Math.Easing.Quintic {#page-title-11}

### In {#In-8}

#### \<static> In(v) {#static-inv-6}


**说明:**

将一个五进制易入曲线应用到给定值。 该值开始变化非常缓慢, 并急剧加速到最后, 沿着第五功率( v^5) 曲线。 这比立方或夸式易入函数产生更显著的加速效果, 使其适合动画, 需要以近零速度开始, 快速快速地累积到全速 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/quintic/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quintic/In.js#L7)  
引入版本：3.0.0


### InOut {#InOut-8}

#### \<static> InOut(v) {#static-inoutv-6}


**说明:**

将一个昆曲易入/出函数应用到给定值中。运动开始缓慢,从中点快速加速,然后减速回慢。与立方或夸张的放松相比,五进制曲线(提升到第五强)产生更戏剧性的加速和减速,使其非常适合需要强健的,拳头的感觉,并有平稳的起始和结束的过渡。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟调值,在[0, 1]之间. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/quintic/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quintic/InOut.js#L7)  
引入版本：3.0.0


### Out {#Out-8}

#### \<static> Out(v) {#static-outv-6}


**说明:**

昆曲轻松出炉.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/quintic/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quintic/Out.js#L7)  
引入版本：3.0.0


# Phaser.Math.Easing.Sine {#page-title-12}

### In {#In-9}

#### \<static> In(v) {#static-inv-7}


**说明:**

将一个sinusoid的易入曲线应用到给定值。 运动开始缓慢, 并加速到尾端, 沿着正弦波的形状。 这比其他大多数易入函数产生一个更温和的开始, 使它非常适合像 UI 元素中淡出或者平稳地开始一个相机锅这样的微妙动画 。

`v`的输入值应在0到1之间,其中0代表起始值,1代表端点。此范围以外的值不扣。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟放宽的值,一般在0到1之间. |


**返回值:** number - 放宽值,在0到1之间.


> 源码：[src/math/easing/sine/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/sine/In.js#L7)  
引入版本：3.0.0


### InOut {#InOut-9}

#### \<static> InOut(v) {#static-inoutv-7}


**说明:**

将一个sinusoidal 易入/出到给定值。运动会缓慢地开始,从中点加速,并在结尾处减速到一个站点,产生平滑的 S 曲线过渡。这对动画需要自然的、对称的感,并有温和的始末。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟调值,在[0, 1]之间. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/sine/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/sine/InOut.js#L7)  
引入版本：3.0.0


### Out {#Out-9}

#### \<static> Out(v) {#static-outv-7}


**说明:**

偏辛松动(sinusoidal easy-out),开始快速移动,并减速到一个温和的停站,沿着正弦波的曲线,在动画和Tweens中常用来平滑减速.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟调值,在[0, 1]之间. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/sine/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/sine/Out.js#L7)  
引入版本：3.0.0


# Phaser.Math.Fuzzy {#page-title-13}

### Ceil {#Ceil}

#### \<static> Ceil(value, [epsilon]) {#static-ceilvalue-epsilon}


**说明:**

计算给定值的模糊上限 。

将数值四舍五入到最近的整数,但在应用 `Math.ceil` 之前减去一个小的 epsiloon 容积。这意味着,数值略高于整数边界(在 epsiloon 在 epsilon 范围内) 会被当做它们完全位于该边界上,避免浮点精度错误,否则会意外地将结果推到下一个整数。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 计算模糊天花板的值 。 |
| epsilon | number | 是 | 0.0001 | epsilon的容性用来减少浮点精度错误. |


**返回值:** number - 值的模糊天花板。


> 源码：[src/math/fuzzy/Ceil.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/fuzzy/Ceil.js#L7)  
引入版本：3.0.0


### Equal {#Equal}

#### \<static> Equal(a, b, [epsilon]) {#static-equala-b-epsilon}


**说明:**

检查给定的值是否模糊地相等 。

如果两者的差值小于`epsilon`,则两者模糊相等。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| a | number | 否 |  | 初标值. |
| b | number | 否 |  | 第二义值. |
| epsilon | number | 是 | 0.0001 | 两者数值下方最大绝对差值相等. |


**返回值:** boolean - 如果数值模糊,则使用`true`,否则使用`false`。


> 源码：[src/math/fuzzy/Equal.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/fuzzy/Equal.js#L7)  
引入版本：3.0.0


### Floor {#Floor}

#### \<static> Floor(value, [epsilon]) {#static-floorvalue-epsilon}


**说明:**

通过在下架前添加一个小的epsilon来计算给定值的模糊底。这样可以避免浮点精度问题,因为数学上应该是一个整数(如2.99999999)的值会错转到下面的整数。下一轮整数上方的epsilon内的任何值都会被下调到整数。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 计算模糊底部的值。 |
| epsilon | number | 是 | 0.0001 | epsilon 值。 下个整数的距离内值被下调到整数。 |


**返回值:** number - 给定值的模糊层.


> 源码：[src/math/fuzzy/Floor.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/fuzzy/Floor.js#L7)  
引入版本：3.0.0


### GreaterThan {#GreaterThan}

#### \<static> GreaterThan(a, b, [epsilon]) {#static-greaterthana-b-epsilon}


**说明:**

检查`a`是否模糊大于`b`.

`a`如果大于`b - epsilon`,则模糊度大于`b`.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| a | number | 否 |  | 初标值. |
| b | number | 否 |  | 第二义值. |
| epsilon | number | 是 | 0.0001 | 用于控制模糊度的 epsiron 值。 更大的值使比较更加宽松 。 |


**返回值:** boolean - `true` 如果出现 `a` 模糊的大于 `b`,否则 `false`.


> 源码：[src/math/fuzzy/GreaterThan.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/fuzzy/GreaterThan.js#L7)  
引入版本：3.0.0


### LessThan {#LessThan}

#### \<static> LessThan(a, b, [epsilon]) {#static-lessthana-b-epsilon}


**说明:**

检查`a`是否模糊小于`b`.

`a` 模糊度小于 `b` 如果它小于 `b + epsilon`.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| a | number | 否 |  | 初标值. |
| b | number | 否 |  | 第二义值. |
| epsilon | number | 是 | 0.0001 | 模糊比较所用的容积值。 此距离内的值被认为是相等的 。 |


**返回值:** boolean - `true` 如果出现 `a` 模糊度小于 `b`,否则 `false`.


> 源码：[src/math/fuzzy/LessThan.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/fuzzy/LessThan.js#L7)  
引入版本：3.0.0


# Phaser.Math.Interpolation {#page-title-14}

### Bezier {#Bezier}

#### \<static> Bezier(v, k) {#static-bezierv-k}


**说明:**

执行一个通用的贝塞尔插值, 覆盖任意数控制点。 `v` 阵列提供了控制点值, `k`( 0 至 1) 确定了曲线上的位置。 与使用精确4 点的 CubicBezier 刑警组织不同, 它支持任意数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | Array.\<number> | 否 | 输入值阵列, 以插入值之间 。 |
| k | number | 否 | 插值的百分比,在0到1之间. |


**返回值:** number - 内插值.


> 源码：[src/math/interpolation/BezierInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/BezierInterpolation.js#L9)  
引入版本：3.0.0


### CatmullRom {#CatmullRom-1}

#### \<static> CatmullRom(v, k) {#static-catmullromv-k}


**说明:**

在一个数值阵列上执行 Catmull-Rom 线性插值,产生一个平滑曲线,通过每个控制点。 `k`参数(0至1) 确定整个曲线的位置。

如果`v`中的第一和最后一个值相等,则曲线被视作闭合(rooping),插值被无缝地包裹起来。否则曲线被视作开阔,而0至1范围以外的`k`值将推导出终点之外。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | Array.\<number> | 否 | 用于插入控制点值的输入数组。 |
| k | number | 否 | 插值的百分比,介于0到1之间,在这个范围以外的数值在开阔曲线上推算,或者在闭合曲线上包扎. |


**返回值:** number - 内插值.


> 源码：[src/math/interpolation/CatmullRomInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/CatmullRomInterpolation.js#L9)  
引入版本：3.0.0


### CubicBezier {#CubicBezier}

#### \<static> CubicBezier(t, p0, p1, p2, p3) {#static-cubicbeziert-p0-p1-p2-p3}


**说明:**

计算给定参数的立方贝塞尔插值 `t`,基于四个控制点。曲线通过 `p0` 时 `t=0` 财务报告和已审计财务报表 `p3` 时 `t=1`时 `p1` 财务报告和已审计财务报表 `p2` 充当拉点,在不必然出现在这些终点之间塑造曲线。这使得立方贝塞尔插值非常适合动画、相机路径和程序运动中平滑、艺术引导的转换。

[https://medium.com/@adrian_cooney/bezier-interpolation-13b68563313a](https://medium.com/@adrian_cooney/bezier-interpolation-13b68563313a)

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 插值的百分比,在0到1之间. |
| p0 | number | 否 | 始发点. |
| p1 | number | 否 | 初总控点. |
| p2 | number | 否 | 第二控制点. |
| p3 | number | 否 | 终处. |


**返回值:** number - 内插值.


> 源码：[src/math/interpolation/CubicBezierInterpolation.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/CubicBezierInterpolation.js#L43)  
引入版本：3.0.0


### Linear {#Linear-2}

#### \<static> Linear(v, k) {#static-linearv-k}


**说明:**

进行一系列数值的线性插值。

鉴于`v`和进展因子`k`在0到1之间,此函数将`k`映射到数组沿边的位置,并返回两个最接近数组元素之间的线性插值。一个0的`k`返回第一个元素附近的值,而一个1的`k`返回最后一个元素附近的值。在0到1之间值的`k`被推导到数组的末尾。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | Array.\<number> | 否 | 输入值阵列, 以插入值之间 。 |
| k | number | 否 | 插值的百分比,在0到1之间. |


**返回值:** number - 内插值.


> 源码：[src/math/interpolation/LinearInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/LinearInterpolation.js#L9)  
引入版本：3.0.0


### QuadraticBezier {#QuadraticBezier}

#### \<static> QuadraticBezier(t, p0, p1, p2) {#static-quadraticbeziert-p0-p1-p2}


**说明:**

沿着一个起点、一个控制点和一个终点定义的四边形贝塞尔曲线计算一个单一点。 `t`的数值决定了返回值沿曲线的大小:0返回起始点值,1返回终点值,而中间的值是顺畅的插值。控制点将曲线拉向它,在起点和终点之间形成弧线,而不会直接穿过曲线。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 沿曲线的插值位置,介于 0(起始)至 1(结束)之间. |
| p0 | number | 否 | 起点值. |
| p1 | number | 否 | 控制点值,将曲线拉向它,决定它的弧. |
| p2 | number | 否 | 终点值. |


**返回值:** number - 沿四面体贝塞尔曲线的`t`位置的插值。


> 源码：[src/math/interpolation/QuadraticBezierInterpolation.js#L35](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/QuadraticBezierInterpolation.js#L35)  
引入版本：3.2.0


### SmootherStep {#SmootherStep-1}

#### \<static> SmootherStep(t, min, max) {#static-smootherstept-min-max}


**说明:**

基于肯·佩林的平滑步态函数的插值法,它是标准平滑步态曲线的改进变体. 平滑步态不同于平滑步态,平滑步态在终点有0个首辅衍生物,平滑步态还在终点有0个次辅衍生物,导致`min`和`max`之间更平滑的S曲线过渡. 使用此方法时需要特别流畅的松动,在过渡开始或结束时没有可视加速或减速的文物.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 插值的百分比,在0到1之间. |
| min | number | 否 | 最小值,又称"左边",假定比"右边"小. |
| max | number | 否 | 最大值,又称"右边缘",假定值大于"左边缘". |


**返回值:** number - 内插值.


> 源码：[src/math/interpolation/SmootherStepInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/SmootherStepInterpolation.js#L9)  
引入版本：3.9.0


### SmoothStep {#SmoothStep-1}

#### \<static> SmoothStep(t, min, max) {#static-smoothstept-min-max}


**说明:**

平滑步态插值法,它利用平滑步态函数在`min`和`max`值之间产生平滑的,S形的过渡。与线性插值不同,平滑步态在两边都容易进出,导致过渡的逐渐开始和结束。这使得它非常适合动画和过渡,因为边界的突然变化看起来是不自然的。

插值参数 `t` 首先是通过平滑步曲线重新映射(它夹住并应用立方赫米特函数),然后使用结果线性插到 `min` 财务报告和已审计财务报表 `max`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 插值的百分比,在0到1之间. |
| min | number | 否 | 最小值,又称"左边",假定比"右边"小. |
| max | number | 否 | 最大值,又称"右边缘",假定值大于"左边缘". |


**返回值:** number - 内插值.


> 源码：[src/math/interpolation/SmoothStepInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/SmoothStepInterpolation.js#L9)  
引入版本：3.9.0


# Phaser.Math.Pow2 {#page-title-15}

### GetPowerOfTwo {#GetPowerOfTwo}

#### \<static> GetPowerOfTwo(value) {#static-getpoweroftwovalue}


**说明:**

返回大于或等于给定的 `value` 的最小功率 2 。 例如, 值 7 返回 8 , 值 8 返回 8 , 9 返回 16 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 找到下一个 2 的 值应该是正数 。 |


**返回值:** number - 2的最小功率大于或等于`value`.


> 源码：[src/math/pow2/GetPowerOfTwo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/pow2/GetPowerOfTwo.js#L7)  
引入版本：3.0.0


### IsSize {#IsSize}

#### \<static> IsSize(width, height) {#static-issizewidth-height}


**说明:**

检查给定的 `width`和 `height` 是否具有两个功率。 用于检查纹理尺寸 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 要检查的宽度, 以像素计 。 |
| height | number | 否 | 要检查的高度, 以像素表示 。 |


**返回值:** boolean - `true` 如果出现 `width` 财务报告和已审计财务报表 `height` 是一种二强的力量,否则 `false`.


> 源码：[src/math/pow2/IsSizePowerOfTwo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/pow2/IsSizePowerOfTwo.js#L7)  
引入版本：3.0.0


### IsValue {#IsValue}

#### \<static> IsValue(value) {#static-isvaluevalue}


**说明:**

如果值为2,则测试值并返回`true`。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 值以验其有无二力. |


**返回值:** boolean - 如果`value`是2的功率,则返回`true`,否则返回`false`.


> 源码：[src/math/pow2/IsValuePowerOfTwo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/pow2/IsValuePowerOfTwo.js#L7)  
引入版本：3.0.0


# Phaser.Math.Snap {#page-title-16}

### Ceil {#Ceil-1}

#### \<static> Ceil(value, gap, [start], [divide]) {#static-ceilvalue-gap-start-divide}


**说明:**

使用 ceil 来将一个值与最近的网格切片相匹配 。

示例:如果间隔间距间距为 `5` 和职位 `12`...你会很快地 `15`。 。 。 。 `14` 转弯到 `15`. 不过... `16` 将会迅速 `20`.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 价值来扣 |
| gap | number | 否 |  | 网格的间隔间隙 。 |
| start | number | 是 | 0 | 可选起始数冲抵缺口。 |
| divide | boolean | 是 | false | 如果 `true` 返回前, 它会将断裂值除以空隙 。 |


**返回值:** number - 崩溃的值。


> 源码：[src/math/snap/SnapCeil.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/snap/SnapCeil.js#L7)  
引入版本：3.0.0


### Floor {#Floor-1}

#### \<static> Floor(value, gap, [start], [divide]) {#static-floorvalue-gap-start-divide}


**说明:**

使用地板将一个值与最近的下网格切片对齐。

示例:如果间隔间距间距为 `5` 和职位 `12`...你会很快地 `10`。 。 。 。 `14` 转弯到 `10`. 不过... `16` 将会迅速 `15`.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 价值来扣 |
| gap | number | 否 |  | 网格的间隔间隙 。 |
| start | number | 是 | 0 | 可选起始数冲抵缺口。 |
| divide | boolean | 是 | false | 如果 `true` 返回前, 它会将断裂值除以空隙 。 |


**返回值:** number - 崩溃的值。


> 源码：[src/math/snap/SnapFloor.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/snap/SnapFloor.js#L7)  
引入版本：3.0.0


### To {#To}

#### \<static> To(value, gap, [start], [divide]) {#static-tovalue-gap-start-divide}


**说明:**

使用四舍五入来将一个值与最近的网格切片相匹配。在两个切片之间完全落到一半的值会向更高的切片相匹配。

示例:如果间隔间距间距为 `5` 和职位 `12`...你会很快地 `10` 却 `14` 将会迅速 `15`.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 价值来扣 |
| gap | number | 否 |  | 网格的间隔间隙 。 |
| start | number | 是 | 0 | 可选起始值为网格抵消,允许网格对齐开始值为零以外的值. |
| divide | boolean | 是 | false | 如果 `true` 返回前, 它会将断裂值除以空隙 。 |


**返回值:** number - 崩溃的值。


> 源码：[src/math/snap/SnapTo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/snap/SnapTo.js#L7)  
引入版本：3.0.0

---
