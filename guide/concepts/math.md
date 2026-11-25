# 数学 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/math)

JavaScript本身有一个相当全面的数学API,当然它被优化,可以快速在浏览器中运行。Phaser扩展了它,它有它自己的一套数学功能,这些功能主要围绕游戏中常见的用例。例如,有数学功能用于使用角度、距离、随机数、插值等。这些功能很多是存在的,因为它们是内部需要的,所以我们也暴露出来,供您使用。其余的只是我们发现这些年来需要的功能。

Phaser数学函数都包含在自己的命名空间中。我们不会,也永远不会修改或污染本地的JavaScript数学命名空间。这意味着您可以在游戏中同时使用Phaser数学函数和本地的数学函数,而不会有任何冲突。

## 基本职能 {#basic-functions}

### 平均数 {#average}

计算给定的 `values` 的平均值 。

#### 使用量 {#usage}

```js
var result = Phaser.Math.Average(values);
```

- `result`:所有数值的平均值。
- `values` : 数字阵列。

### 差额 {#difference}

计算两个给定数字的正差。

#### 使用量 {#usage-1}

```js
var result = Phaser.Math.Difference(a, b);
```

- `a`:第一个数字。
- `b`:第二数字.
- `result`:`a`和`b`的正差.

### 阶乘 {#factorial}

计算大于 0 的整数值的给定 `value` 的因子。

#### 使用量 {#usage-2}

```js
var result = Phaser.Math.Factorial(value);
```

- `value`:一个正整数,用来计算其因子。
- `result` : 给定数字的阶乘.

### 连 {#iseven}

检查给定的 `value`是否是使用抽象的等号 `==`的偶数 。

#### 使用量 {#usage-3}

```js
var result = Phaser.Math.IsEven(value); // returns true or false
```

### 偶数显示 {#isevenstrict}

检查给定的 `value`是否是使用严格等价 `===`的偶数.

#### 使用量 {#usage-4}

```js
var result = Phaser.Math.IsEvenStrict(value); // returns true or false
```

### 黄牛2 {#pow2}

检查给出的值是否与 2 的功率有关 。

#### 使用量 {#usage-5}

- 得到最近的2的功率 到给定的`value`。

  ```js
  var result = Phaser.Math.Pow2.GetNext(value);
  ```

  - Examples:

    ```js
    var result = Phaser.Math.Pow2.GetNext(3); // returns 4
    // var result = Phaser.Math.Pow2.GetNext(4.1); // returns 8
    // var result = Phaser.Math.Pow2.GetNext(9); // returns 16
    ```

- 检查给定的`width`和`height`是否为2的功率.

  ```js
  var result = Phaser.Math.Pow2.IsSize(width, height);
  ```

  - Examples:

    ```js
    var result = Phaser.Math.Pow2.IsSize(2, 2); // returns true
    // var result = Phaser.Math.Pow2.IsSize(2, 3); // returns false
    // var result = Phaser.Math.Pow2.IsSize(4, 16); // returns true
    ```

- 测试`value`,如果是2个功率,则返回`true`.

  ```js
  var result = Phaser.Math.Pow2.IsValue(value);
  ```

  - Examples:

    ```js
    var result = Phaser.Math.Pow2.IsValue(2); // returns true
    // var result = Phaser.Math.Pow2.IsValue(3); // returns false
    // var result = Phaser.Math.Pow2.IsValue(16); // returns true
    ```

## 最低,最高额 {#minimum-maximum}

### 内插 {#interpolation}

计算 t (0~ 1) 上的内置Phaser方法的内置相位值。

#### 使用量 {#usage-6}

- 线性内插( lerp) 2 值

  ```js
  var result = Phaser.Math.Linear(p0, p1, t);
  ```

- 线性插值( lerp) 2 向量

  ```js
  var result = Phaser.Math.LinearXY(vector0, vector1, t);
  ```

  - `vector0`, `vector1` : Phaser.Math.Vector2

- 平滑插值

  ```js
  var result = Phaser.Math.Interpolation.SmoothStep(t, min, max);
  ```

  - `t` : 0~1

- 较平滑的插值

  ```js
  var result = Phaser.Math.Interpolation.SmootherStep(t, min, max);
  ```

  - `t` : 0~1

- 二次曲线贝塞尔插值

  ```js
  var result = Phaser.Math.Interpolation.QuadraticBezier(t, p0, p1, p2);
  ```

  - `t` : 0~1
  - `p0` : 起点.
  - `p1` :控制点.
  - `p2` :终点.

- 立方体贝塞尔插值

  ```js
  var result = Phaser.Math.Interpolation.CubicBezier(t, p0, p1, p2, p3);
  ```

  - `t` : 0~1
  - `p0` : 起点.
  - `p1` :第一个控制点.
  - `p2` :第二个控制点.
  - `p3` :终点.

### 百分比 {#percentage}

研究`value`在`min`和`max`之间的百分比,即内置的Phaser方法.

#### 使用量 {#usage-7}

- 获得`value`在`min`和`max`之间的百分比:

  ```js
  var result = Phaser.Math.Percent(value, min, max, upperMax);
  ```

  - `result`: 百分比(0~1).
  - `value` : 确定百分比的号码。
  - `min`:最小范围
  - `max`:最大范围
  - `upperMax`:代表100%的射程中点.

- 根据 `percent` 介于 `min` 财务报告和已审计财务报表 `max`:

  ```js
  var result = Phaser.Math.FromPercent(percent, min, max);
  ```

  - `result`:根据`min`和`max`范围之间的百分比计算得出.
  - `percent` :0至1之间的数字,代表百分比。
  - `min`:最小范围
  - `max`:最大范围

### 夹板 {#clamp}

将`value`夹在范围范围内,使其与射程`min`,`max`,内置的Phaser方法相接.

#### 使用量 {#usage-8}

```js
var result = Phaser.Math.Clamp(value, min, max);
```

- `value` :要夹的值.
- `min`:最小范围
- `max`:最大范围

### 最大添加 {#maxadd}

将`amount`加到`value`上,将最大结果限制在`max`上.

#### 使用量 {#usage-9}

```js
var result = Phaser.Math.MaxAdd(value, amount, max);
```

- `value` : 添加的值.
- `amount` : 拟加的金额。
- `max` : 返回的最大值。

### 小型潜艇 {#minsub}

从`value`中减掉一个`amount`,将最小结果限制在`min`.

#### 使用量 {#usage-10}

```js
var result = Phaser.Math.MinSub(value, amount, min);
```

- `value` : 减到的值。
- `amount` : 减去的金额。
- `min` : 返回的最小值。

### 环绕 {#wrap}

将给定的`value`包在`min`和`max`之间,是Phaser的内置方法.

#### 使用量 {#usage-11}

```js
var result = Phaser.Math.Wrap(value, min, max);
```

- `value` : 需要包扎的值。
- `min`:最小范围
- `max`:最大范围

### 轻松 {#ease}

易功能,内置的Phaser方法.

#### 使用量 {#usage-12}

##### 易用函数 {#ease-functions}

- 线性: `Phaser.Math.Easing.Linear`
- 四方、 动力1
  - 四边形易行:`Phaser.Math.Easing.Quadratic.Out`
  - 四方易行:`Phaser.Math.Easing.Quadratic.In`
  - 四方易行/出:`Phaser.Math.Easing.Quadratic.InOut`
- 立方体, 动力2
  - 立方体易解脱: `Phaser.Math.Easing.Cubic.Out`
  - 立方体易行性: `Phaser.Math.Easing.Cubic.In`
  - 立方体易行/出:`Phaser.Math.Easing.Cubic.InOut`
- Quartic, Power3 设备
  - Quartic 轻松出局: `Phaser.Math.Easing.Quartic.Out`
  - Quartic 轻松进入: `Phaser.Math.Easing.Quartic.In`
  - Quartic 易行/出行: `Phaser.Math.Easing.Quartic.InOut`
- Quitic, Power4 设备 设备
  - 昆式轻松出局:`Phaser.Math.Easing.Quintic.Out`
  - 昆曲轻松入场:`Phaser.Math.Easing.Quintic.In`
  - 昆式易行/出行:`Phaser.Math.Easing.Quintic.InOut`
- Sinusoidal
  - 偏辛醇-安逸:`Phaser.Math.Easing.Sine.Out`
  - 顺辛醇-安逸:`Phaser.Math.Easing.Sine.In`
  - 偏西式易入/出:`Phaser.Math.Easing.Sine.InOut`
- Exponential
  - 指示易行度: `Phaser.Math.Easing.Expo.Out`
  - 指证易用性:`Phaser.Math.Easing.Expo.In`
  - 指向易入/易出:`Phaser.Math.Easing.Expo.InOut`
- Circular
  - 循环易行 : `Phaser.Math.Easing.Circular.Out`
  - 循环易用性: `Phaser.Math.Easing.Circular.In`
  - 循环易行/出行:`Phaser.Math.Easing.Circular.InOut`
- Elastic
  - 弹性易解脱: `Phaser.Math.Easing.Elastic.Out`
  - 弹性易行性:`Phaser.Math.Easing.Elastic.In`
  - 弹性易行/出行:`Phaser.Math.Easing.Elastic.InOut`
- Bounce
  - 弹出放松: `Phaser.Math.Easing.Bounce.Out`
  - 弹幕易入:`Phaser.Math.Easing.Bounce.In`
  - 弹出易控/出:`Phaser.Math.Easing.Bounce.InOut`
- Back
  - 后放轻松: `Phaser.Math.Easing.Back.Out`
  - 后易行: `Phaser.Math.Easing.Back.In`
  - 后易行/出:`Phaser.Math.Easing.Back.InOut`
- 已踩踏 : `Phaser.Math.Easing.Stepped(v, step)`

##### 通过字符串获取易操作 {#get-ease-function-via-string}

```js
var easeFunction = Phaser.Tweens.Builders.GetEaseFunction(ease);
// var easeFunction = Phaser.Tweens.Builders.GetEaseFunction(ease, easeParams);
```

- `ease` :

  - 字符串 :
    - `Power0` 线性
    - `Power1` : 四方报. 出.
    - `Power2` : 立方体。 出局
    - `Power3` : 夸蒂奇. 出局
    - `Power4` : 昆蒂克. 出处
    - `Linear`
    - `Quad` : 四方报. 出.
    - `Cubic` : 立方体。 出局
    - `Quart` : 夸蒂奇. 出局
    - `Quint` : 昆蒂克. 出处
    - `Sine` : 正弦。 出局( 秒)
    - `Expo` : 博览. 出局
    - `Circ` : 循环。 出局
    - `Elastic` : 弹性。 退出
    - `Back` : 后退。 出局
    - `Bounce` 弹跳,出来
    - `Stepped`
    - `Quad.easeIn`
    - `Cubic.easeIn`
    - `Quart.easeIn`
    - `Quint.easeIn`
    - `Sine.easeIn`
    - `Expo.easeIn`
    - `Circ.easeIn`
    - `Back.easeIn`
    - `Bounce.easeIn`
    - `Quad.easeOut`
    - `Cubic.easeOut`
    - `Quart.easeOut`
    - `Quint.easeOut`
    - `Sine.easeOut`
    - `Expo.easeOut`
    - `Circ.easeOut`
    - `Back.easeOut`
    - `Bounce.easeOut`
    - `Quad.easeInOut`
    - `Cubic.easeInOut`
    - `Quart.easeInOut`
    - `Quint.easeInOut`
    - `Sine.easeInOut`
    - `Expo.easeInOut`
    - `Circ.easeInOut`
    - `Back.easeInOut`
    - `Bounce.easeInOut`
  - 自定义函数

    ```js
    function(v) {
        return v;
    }
    ```

    ```js
    function(v, param0, param1, ...) {
        return v;
    }
    ```

    - `v` : `0` ~ `1`

##### 获取结果 {#get-result}

```js
var result = easeFunction(t);
```

- `t` : `0` ~ `1`

## 回合至 {#round-to}

圆/圆/底到给定精度,内置的Phaser方法.

### 切换到 {#ceilto}

与基数相比,Ceils到某个地方,默认值为十位小数。

这个地方的标志是 用来获取那个地方的权力。

#### 使用量 {#usage-13}

```js
var result = Phaser.Math.CeilTo(value);
```

or

```js
var result = Phaser.Math.CeilTo(value, place, base);
```

- `value` : 圆的值。
- `place` : 圆形到圆形的位置。 正形到圆形, 负形到小数位。 默认是 `0`.
- `base`: 圆形的底部。 默认为小数的`10` 。

### 下限到 {#floorto}

相对于一个基数, 低于某个基数的地方的底数, 默认值为十。

这个地方的标志是 用来获取那个地方的权力。

#### 使用量 {#usage-14}

```js
var result = Phaser.Math.floorTo(value);
```

or

```js
var result = Phaser.Math.floorTo(value, place, base);
```

- `value` : 圆的值。
- `place` : 圆形到圆形的位置。 正形到圆形, 负形到小数位。 默认是 `0`.
- `base`: 圆形的底部。 默认为小数的`10` 。

### 绕过零度 {#roundawayfromzero}

绕一个给定的数字,使它离零更远。也就是说,正数被四舍五入,负数被四舍五入。

#### 使用量 {#usage-15}

```js
var result = Phaser.Math.RoundAwayFromZero(value);
```

- `value` : 圆的值。

Examples:

```js
RoundAwayFromZero(10.5) = 11
RoundAwayFromZero(123.45) = 124
RoundAwayFromZero(-5.45) = -6
RoundAwayFromZero(-123.45) = -124
```

### 回合改为 {#roundto}

圆向给定精度的值 。

#### 使用量 {#usage-16}

```js
var result = Phaser.Math.RoundTo(value);
```

or

```js
var result = Phaser.Math.RoundTo(value, place, base);
```

- `value` : 圆的值。
- `place` : 圆形到圆形的位置。 正形到圆形, 负形到小数位。 默认是 `0`.
- `base`: 圆形的底部。 默认为小数的`10` 。

Examples:

```js
RoundTo(123.456789, 0) = 123
RoundTo(123.456789, -1) = 123.5
RoundTo(123.456789, -2) = 123.46
RoundTo(123.456789, -3) = 123.457
```

### 齐和 {#snap}

将一个值与最近的网格切片, Phaser的内置方法相匹配 。

#### 使用量 {#usage-17}

- 使用四舍五入键将值与最近的网格切片对齐 。

  ```js
  var out = Phaser.Math.Snap.To(value, gap);
  // var out = Phaser.Math.Snap.To(value, gap, start);
  ```

  示例: 将 `gap` 设置为 `5`

  - 将 `value` 设定为 `12`, 返回 `10`
  - 将 `value` 设定为 `14`, 返回 `15`

- 使用 `Ceil` 将一个值与最近的网格切片对齐 。

  ```js
  var out = Phaser.Math.Snap.Ceil(value, gap);
  // var out = Phaser.Math.Snap.Ceil(value, gap, start);
  ```

  示例: 将 `gap` 设置为 `5`

  - 将 `value` 设定为 `12`, 返回 `15`
  - 将 `value` 设定为 `14`, 返回 `15`

- 使用 `Floor` 将一个值与最近的网格切片对齐 。

  ```js
  var out = Phaser.Math.Snap.Floor(value, gap);
  // var out = Phaser.Math.Snap.Floor(value, gap, start);
  ```

  示例: 将 `gap` 设置为 `5`

  - 将 `value` 设定为 `12`, 返回 `10`
  - 将 `value` 设定为 `14`, 返回 `10`

## 距离 {#distance}

获得距离,内置的Phaser方法.

### 获取2点之间的距离 {#get-distance-between-2-points}

```js
var d = Phaser.Math.Distance.Between(x1, y1, x2, y2);
```

or

```js
var d = Phaser.Math.Distance.BetweenPoints(a, b); // a, b: {x, y}
```

### 获得两点之间的平方距离 {#get-squared-distance-between-two-points}

```js
var d = Phaser.Math.Distance.BetweenPointsSquared(a, b); // a, b: {x, y}
```

or

```js
var d = Phaser.Math.Distance.Squared(x1, y1, x2, y2);
```

### 获取切比舍夫距离( 水平和垂直距离的最大距离) {#get-chebyshev-distance-the-maximum-of-the-horizontal-and-vertical-distances}

```js
var d = Phaser.Math.Distance.Chebyshev(x1, y1, x2, y2);
```

### 获取电源距离(水平电源距离和垂直电源距离之和) {#get-power-distance-the-sum-of-the-horizontal-power-distance-and-vertical-power-distance}

```js
var d = Phaser.Math.Distance.Power(x1, y1, x2, y2);
```

### 获取蛇距离(即直线距离,曼哈顿距离,水平距离和垂直距离之和) {#get-snake-distanceie-rectilinear-distance-manhattan-distance-the-sum-of-the-horizontal-and-vertical-distance}

```js
var d = Phaser.Math.Distance.Snake(x1, y1, x2, y2);
```

### 获取速度 {#get-speed}

```js
var d = Phaser.Math.GetSpeed(distance, time);
```

- `distance` : 以像素表示的行走距离.
- `time` :时间,以ms计,以覆盖距离.

## 角度 {#angle}

转换角度值,Phaser的内置方法.

### 度 : `<->` 弧度 {#degree---radians}

将给定的角度从 `degrees` 转换为弧度 。

```js
var radians = Phaser.Math.DegToRad(degrees);
```

将给定的角度从 `radians` 转换为度 。

```js
var degrees = Phaser.Math.RadToDeg(radians); // degrees : -180 ~ 180
```

### 点之间的角度 {#angle-between-points}

从 (0, 0) 到矢量 (x2 - x1, y2 - y1) 角度

```js
var rad = Phaser.Math.Angle.Between(x1, y1, x2, y2);
```

or

```js
var rad = Phaser.Math.Angle.BetweenPoints(point1, point2);
```

### 角度之间的角度 {#angle-between-angles}

2 个角度之间最短的角度( 度)

```js
var deg = Phaser.Math.Angle.ShortestBetween(angle1, angle2);
```

- `angle1`, `angle2`: 角在 -180 到 180 之间的度数
- `deg`: 角度最小的度
  - 值 > 0: 反时钟旋转
  - 值 &lt; 0: 时钟旋转

### 顺时针逆时针 {#clockwise-to-counter-clockwise}

转换 Spisters 默认顺时针 `angle` 格式,以逆时针进行.

```js
var deg = Phaser.Math.Angle.CounterClockwise(angle);
```

- `angle`:弧度角
- `deg`:弧度角

### 随机角度 {#random-angle}

返回范围 [-pi, pi] 中的随机角度。

```js
var angle = Phaser.Math.Angle.Random();
```

返回范围 [-180, 180] 中的随机角度。

```js
var angle = Phaser.Math.Angle.RandomDegrees();
```

### 反转 {#reverse}

反转给定的`angle`(旋转角度180度).

```js
var angle = Phaser.Math.Angle.Reverse(angle);
```

- `angle`:弧度角

### 围绕位置旋转 {#rotate-around-position}

绕着`x`和`y`旋转一个`point`,由给定的`angle`.

```js
var out = Phaser.Math.RotateAround(point, x, y, angle);
```

旋转 a `point` 环绕 `x` 财务报告和已审计财务报表 `y` 由给定的 `angle` 财务报告和已审计财务报表 `distance`.

```js
var out = Phaser.Math.RotateAroundDistance(point, x, y, angle, distance);
```

### 旋转到角度 {#rotate-to-angle}

旋转 `currentAngle` 向 `targetAngle` 方向旋转, 旋转距离最短。 `lerp` 是旋转的量 。

```js
var rad = Phaser.Math.Angle.RotateTo(currentAngle, targetAngle, lerp);
```

### 环绕角度 {#wrap-angle}

- 至 PI 范围的环角( 弧度)

  ```js
  var rad = Phaser.Math.Angle.Wrap(angle);
  ```

- 0至2 +%PI 范围的环角( 弧度)

  ```js
  var rad = Phaser.Math.Angle.Normalize(angle);
  ```

- 圆角(度),介于 -180 至 180 之间

  ```js
  var deg = Phaser.Math.Angle.WrapDegrees(angle);
  ```

### 旋转Vec3 {#rotatevec3}

以轴角旋转一个矢量。

```js
var result = Phaser.Math.RotateVec3(vector, axis, angle);
```

- `vector`:要旋转的矢量.
- `axis` :轴旋转.
- `angle` :弧度旋转的角度.

Example:

```js
var vector = Phaser.Math.Vector3(1, 0, 0); // x = 1, y = 0, z = 0
var axis = new Phaser.Math.Vector3(0, 0, 1); // rotate along z-axis
var angle = Math.PI / 2; // rotate 90 degrees in radians
var result = Phaser.Math.vector(vec, axis, angle);
```

- `result` : `Vector3 {x: 0, y: 1, z: 0}`

## 随机 {#random}

### 最小和最大之间 {#between-minimum-and-maximum}

- 获取随机值 `min` 财务报告和已审计财务报表 `max` 数值,包括 `min` 财务报告和已审计财务报表 `max`.

  ```js
  var value = Phaser.Math.Between(min, max); // Returns a value >= min and <= max
  ```

- 在`min`和`max`之间获得一个随机浮点数,包括`min`,不包括`max`.

  ```js
  var value = Phaser.Math.FloatBetween(min, max); // Returns a value >= min and < max
  ```

### 随机向量 {#random-vector}

- 获得随机 2D `vector` -1和1. 设置默认值 `scale` 值(默认值是 1),以乘以所产生的矢量。

  ```js
  var vec = Phaser.Math.RandomXY(vector); // return vec {x, y}
  // var vec = Phaser.Math.RandomXY(vector, scale);
  ```

- 在球形区域中获取一个随机的3D位置 `vector`。 设置默认的 `radius` 值( 默认值为 1) 以乘以所产生的矢量 。

  ```js
  var vec = Phaser.Math.RandomXYZ(vector); // return vec {x, y, z}
  // var vec = Phaser.Math.RandomXYZ(vector, radius);
  ```

- 获得一个随机的 4D `vector` 。 设置默认的 `scale` 值( 默认值为 1) 以乘以所产生的矢量 。

  ```js
  var vec = Phaser.Math.RandomXYZW(vector); // return vec {x, y, z, w}
  // var vec = Phaser.Math.RandomXYZW(vector, scale);
  ```

### 随机数据编辑器 {#randomdatagenerator}

种子随机数据生成器,通过`Phaser.Math.RND`访问,这是Phaser预先定义的这一类实例.

- 在游戏配置中为预定义的随机数据生成器设定种子

  ```js
  var config = {
    // ...
    seed: seed,
    // ...
  };
  var game = new Phaser.Game(config);
  ```

  - `seed` :
    - 字符串或串数组。

- 运行时设定种子

  ```js
  rnd.init(seed);
  ```

  - `seed`:一个字符串或一系列字符串.

- 获取预定义的随机数据生成器

  ```js
  var rnd = Phaser.Math.RND;
  ```

- 创建新随机生成器

  ```js
  var rnd = new Phaser.Math.RandomDataGenerator(seed); // seed is a string

### 获取随机值 {#get-random-value}

- 随机实数在`0`和`1`之间.

  ```js
  var value = rnd.frac();
  ```

- `0`和`2^32`之间的随机整数.

  ```js
  var value = rnd.integer();
  ```

- 0到2^32之间的随机实数.

  ```js
  var value = rnd.real();
  ```

- 随机整数在分钟和最大之间和包括分钟。

  ```js
  var value = rnd.between(min, max);
  // var value = rnd.integerInRange(min, max);
  ```

- 分钟到最大值之间随机真实数字 。

  ```js
  var value = rnd.realInRange(min, max);
  ```

- 随机实数在 -1 和 1 之间 。

  ```js
  var value = rnd.normal();
  ```

- `-180`和`180`之间的随机角.

  ```js
  var angle = rnd.angle();
  ```

- 随机旋转的弧度,在`-3.141`和`3.141`之间.

  ```js
  var angle = rnd.rotation();
  ```

- 随机时间戳在分钟和最大值之间 。

  ```js
  var timestamp = rnd.timestamp(min, max);
  ```

  - `min`:默认值为2000年初.
  - `max`:默认值为2020年底.

- UUID

  ```js
  var uuid = rnd.uuid();
  ```

- 随机标志值

  ```js
  var sign = rnd.sign();
  ```

  - `sign` : `-1` 或 或 时 间 `1`

### 获取随机项目 {#get-random-item}

- 给定数组内随机元素 。

  ```js
  var item = rnd.pick(array);
  ```

- 随机元素来自给定数组, 偏爱前面的条目 。

  ```js
  var item = rnd.weightedPick(array);
  ```

### 摇摆阵列 {#shuffle-array}

```js
var array = rnd.shuffle(array);
```

## 颜色 {#color}

### 获得颜色整数 {#get-color-integer}

- 十六进制字符串, 或颜色整数

  ```js
  var color = Phaser.Display.Color.ValueToColor(input);
  ```

  - `input` : 十六进制字符串,或颜色整数

- RGB 到颜色

  ```js
  var color = Phaser.Display.Color.GetColor(red, green, blue);
  ```

  - `red`, `green`, `blue` : 0 ~ 255

- RGBA 颜色

  ```js
  var color = Phaser.Display.Color.GetColor32(red, green, blue, alpha);
  ```

  - `red`, `green`, `blue`, `alpha` : 0 ~ 255

- 十六进制字符串为颜色

  ```js
  var color = Phaser.Display.Color.HexStringToColor(hex).color;
  ```

  - 十六进制 : `#0033ff`, `#03f`, `0x0033ff`,或 ,或 , `0x03f`

- RGB 字符串为颜色

  ```js
  var color = Phaser.Display.Color.RGBStringToColor(rgb);
  ```

  - rgb: `'rgb(r,g,b)'`,或称 `'rgba(r,g,b,a)'`.
    - r, g, b: 0~ 255
    - a : 0 ~ 1

- HSV 改为颜色

  ```js
  var color = Phaser.Display.Color.HSVToRGB(h, s, v).color;
  ```

  - `h`, `s`, `v` : 0 ~ 1

### 颜色整数到 RGB {#color-integer-to-rgb}

```js
var rgb = Phaser.Display.Color.IntegerToRGB(color);
```

- `color` : 颜色整数 (`0xAARRGGBB`)
- `rgb` : JSON对象( 以`{r, g, b, a}`)

### HSV 彩色轮 {#hsv-color-wheel}

1. 创建颜色阵列

   ```js
   var colorArray = Phaser.Display.Color.HSVColorWheel(s, v);
   ```

1. 获取颜色

   ```js
   var color = colorArray[i].color; // i : 0 ~ 359
   ```

### 创建颜色对象 {#create-color-object}

- 通过 r,g,b,a 组件创建

  ```js
  var color = new Phaser.Display.Color(red, green, blue); // alpha = 255
  // var color = new Phaser.Display.Color(red, green, blue, alpha);
  ```

  - `red`, `green`, `blue`, `alpha`: 0 ~ 255

- 通过颜色整数创建

  ```js
  var color = Phaser.Display.Color.IntegerToColor(colorInteger);
  ```

  - colorInteger : 颜色整数 (`0xAARRGGBB`)

#### 设定颜色 {#set-color}

- 设定颜色

  ```js
  color.setTo(red, green, blue); // alpha = 255
  // color.setTo(red, green, blue, alpha);
  ```

  - `red`, `green`, `blue`, `alpha`: 0 ~ 255

- 以 GL 值设置颜色

  ```js
  color.setGLTo(red, green, blue); // alpha = 1
  // color.setTo(red, green, blue, alpha);
  ```

  - `red`, `green`, `blue`, `alpha`: 0 ~ 1

- 从颜色对象设置颜色

  ```js
  color.setFromRGB(rgba);
  ```

  - rgba :

    ```js
    {
        r: 0,
        g: 0,
        b: 0,
        // a: 0
    }
    ```

- 从 HSV 设置颜色

  ```js
  color.setFromHSV(h, s, v);
  ```

- 设置为透明( )

  ```js
  color.transparent();
  ```

  - 设定( 红色、 绿色、 蓝色) 到 `0`

- 设置为灰色

  ```js
  color.gray(value);
  ```

- 设置为随机颜色

  ```js
  color.random();
  ```

  or

  ```js
  color.random(min, max);
  ```

  - `min`: 0~255. 默认值为0.
  - `max`: 0~255,默认值为255.

- 设置为随机灰色

  ```js
  color.randomGray();
  ```

  or

  ```js
  color.randomGray(min, max);
  ```

- 设置红/绿/蓝/阿尔法通道: 0~ 255

  ```js
  color.red = value;
  // color.red += value;
  color.green = value;
  // color.green += value;
  color.blue = value;
  // color.blue += value;
  color.alpha = value;
  // color.alpha += value;
  ```

- 设置 H/S/V 频道: 0~ 1

  ```js
  color.h = value;
  // color.h += value;
  color.s = value;
  // color.s += value;
  color.v = value;
  // color.v += value;
  ```

- 设定正态的红色、绿色、蓝色、 α : 0~ 1

  ```js
  color.redGL = value;
  // color.redGL += value;
  color.greenGL = value;
  // color.greenGL += value;
  color.blueGL = value;
  // color.blueGL += value;
  color.alphaGL = value;
  // color.alphaGL += value;
  ```

- 设置亮度

  ```js
  color.brighten(value);
  ```

  - `value`: 百分比,0~100

- 饱和 : 将此颜色的饱和度( S) 增加给定的百分比量 。

  ```js
  color.saturate(value);
  ```

  - `value`: 百分比,0~100

- 饱和 : 将此颜色的饱和度( S) 减少给定的百分比量。

  ```js
  color.desaturate(value);
  ```

  - `value`: 百分比,0~100

- 亮度 : 以给定的百分比数增加此颜色的亮度( V) 。

  ```js
  color.lighten(value);
  ```

  - `value`: 百分比,0~100

- 暗:用给定的百分比数来减少此颜色的亮度( V) 。

  ```js
  color.darken(value);
  ```

  - `value`: 百分比,0~100

#### 颜色属性 {#color-properties}

- RGB 颜色,不包括α通道

  ```js
  var c = color.color;
  ```

- RGB Color,包括α通道.

  ```js
  var c = color.color32;
  ```

- 可用于 CSS 颜色值的 RGB 颜色字符串 。

  ```js
  var c = color.rgba;
  ```

- 红、绿、蓝、阿尔法:0~255

  ```js
  var r = color.red;
  var g = color.green;
  var b = color.blue;
  var a = color.alpha;
  ```

- 高、西、五:0~1

  ```js
  var h = color.h;
  var s = color.s;
  var v = color.v;
  ```

- 常态化红、绿、蓝、α : 0~ 1

  ```js
  var r = color.redGL;
  var g = color.greenGL;
  var b = color.blueGL;
  var a = color.alphaGL;
  ```

#### 克隆 {#clone}

```js
var newColor = color.clone();
```

### 切换到十六进制字符串 {#to-hex-string}

```js
var hexString = Phaser.Display.Color.RGBToString(
  color.r,
  color.g,
  color.b,
  color.a
);
// var hexString = Phaser.Display.Color.RGBToString(color.r, color.g, color.b, color.a, prefix);
```

### 内插 {#interpolation-1}

内插在2种颜色之间.

```js
var colorOut = Phaser.Display.Color.Interpolate.RGBWithRGB(
  r1,
  g1,
  b1,
  r2,
  g2,
  b2,
  length,
  index
);
var colorOut = Phaser.Display.Color.Interpolate.ColorWithColor(
  color1,
  color2,
  length,
  index
);
var colorOut = Phaser.Display.Color.Interpolate.ColorWithRGB(
  color,
  r,
  g,
  b,
  length,
  index
);
```

- `length`, `index` = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = `index/length` (0~1)

## 矢量 {#vector}

2D空间(`{x, y}`)中矢量的表示,Phaser的内置对象.

### 创建向量 {#create-vector}

```js
var vector = new Phaser.Math.Vector2();
// var vector = new Phaser.Math.Vector2(x, y);
// var vector = new Phaser.Math.Vector2({x, y});
```

### 克隆向量 {#clone-vector}

```js
var newVector = vector.clone();
```

### 设定向量组件 {#set-vector-components}

- 设定( x, y)

  ```js
  vector.set(x, y);
  // vector.setTo(x, y);
  ```

  or

  ```js
  vector.copy({ x, y });
  // vector.setFromObject({x, y});
  ```

- 设定角度

  ```js
  vector.setAngle(angle);
  ```

  - `angle` :弧度的角.

- Rotate

  ```js
  vector.rotate(delta);
  ```

  - `delta` : 旋转的角度, 以弧度表示。

- Project

  ```js
  vector.project(srcVector2);
  ```

- 设置长度

  ```js
  vector.setLength(length);
  ```

- 从极坐标设定

  ```js
  vector.setToPolar(azimuth, radius);
  ```

  - `azimuth` :角坐标,以弧度表示.
  - `radius`:射线坐标(长度),默认为`1`.

- 重置为 (0, 0)

  ```js
  vector.reset();
  ```

### 获取矢量commonments {#get-vector-componments}

- , Y

  ```js
  var x = vector.x;
  var y = vector.y;
  ```

- Angle

  ```js
  var angle = vector.angle(); // angle in radians
  ```

- Length

  ```js
  var length = vector.length();
  ```

  or

  ```js
  var lengthSq = vector.lengthSq(); // squared
  ```

### 方法 {#methods}

- Scale

  ```js
  vector.scale(value);
  ```

- 限制长度

  ```js
  vector.limit(value);
  ```

- Normalize

  ```js
  vector.normalize();
  ```

- Negate

  ```js
  vector.negate();
  ```

- 旋转垂直

  ```js
  vector.normalizeRightHand();
  vector.normalizeLeftHand();
  ```

- Reflect

  - 将这个矢量从普通人定义的线上反射出来 。

    ```js
    vector.reflect(normal);
    ```

    - `normal` : 向量垂直于线.

  - 反射这个矢量 跨越另一个。

    ```js
    vector.mirror(axis);
    ```

    - `axis` : 反射的矢量。

#### 矢量方法 {#vector-methods}

- Add

  ```js
  vector.add(src); // src: {x, y}
  ```

- Subtract

  ```js
  vector.subtract(src); // src: {x, y}
  ```

- Multiply

  ```js
  vector.multiply(src); // src: {x, y}
  ```

- Divide

  ```js
  vector.divide(src); // src: {x, y}
  ```

- Dot

  ```js
  var value = vector.dot(src); // src: {x, y}
  ```

- Cross

  ```js
  var value = vector.cross(src); // src: {x, y}
  ```

- 模糊度相等

  ```js
  var equal = vector.fuzzyEquals(src); // src: {x, y}
  // var equal = vector.fuzzyEquals(src, epsilon);
  ```

#### 矢量点方法 {#vector-points-method}

- 2点之间的距离.

  ```js
  var distance = vector.distance(src);
  ```

  or

  ```js
  var distanceSq = vector.distanceSq(src); // squared
  ```

- 线性插值介于2点之间.

  ```js
  vector.lerp(src, t); // src: {x, y}
  ```

  - `t`:插值百分比,在0到1之间.

#### 常数 {#constant}

- Zero `(0,0)`

  ```js
  var vector = Phaser.Math.Vector2.ZERO;
  ```

- One `(1,1)`

  ```js
  var vector = Phaser.Math.Vector2.ONE;
  ```

- Right `(1,0)`

  ```js
  var vector = Phaser.Math.Vector2.RIGHT;
  ```

- Left `(-1,0)`

  ```js
  var vector = Phaser.Math.Vector2.LEFT;
  ```

- Up `(0,-1)`

  ```js
  var vector = Phaser.Math.Vector2.UP;
  ```

- Down `(0,1)`

  ```js
  var vector = Phaser.Math.Vector2.DOWN;
  ```

## 曲线 {#curve}

### 路径 {#path}

#### 添加路径对象 {#add-path-object}

```js
var path = scene.add.path();
// var path = scene.add.path(x, y);  // curve start from (x, y)
```

or

```js
var path = new Phaser.Curves.Path();
// var path = new Phaser.Curves.Path(x, y);  // curve start from (x, y)
```

#### 添加带有曲线的路径对象 {#add-path-object-with-curves}

```js
var path = scene.add.path(json);
```

or

```js
var path = new Phaser.Curves.Path(json);
```

### 添加曲线 {#add-curve}

#### 行线 {#line}

- 添加行对象

  1. 创建行对象

     ```js
     var curve = new Phaser.Curves.Line({ x: x0, y: y0 }, { x: x1, y: y1 });
     ```

     or

     ```js
     var curve = new Phaser.Curves.Line([x0, y0, x1, y1]);
     ```

  1. 添加到路径

     ```js
     path.add(curve);
     ```

- 添加从上一个终点开始的行到下个终点

  ```js
  path.lineTo(endX, endY);
  ```

  or

  ```js
  path.lineTo(new Phaser.Math.Vector2({ x, y }));
  ```

Properties:

- `curve.p0` :第一个终点.
  - `curve.p0.x`, `curve.p0.y`
- `curve.p1` :第二端点.
  - `curve.p1.x`, `curve.p1.y`

#### 圆/椭圆/弧 {#circleellipsearc}

- 添加圆/ 椭圆/ 弧对象

  1. 创建圆/ 椭圆/ arc 对象

     - Circle

       ```js
       var curve = new Phaser.Curves.Ellipse(x, y, radius);
       ```

     - Ellipse

       ```js
       var curve = new Phaser.Curves.Ellipse(x, y, xRadius, yRadius);
       ```

     - Arc

       ```js
       var curve = new Phaser.Curves.Ellipse(
         x,
         y,
         xRadius,
         yRadius,
         startAngle,
         endAngle,
         clockwise,
         rotation
       );
       ```

  1. 添加到路径

     ```js
     path.add(curve);
     ```

- 添加圆/ 椭圆/ arc 从上一个终点开始到下一个终点

  - Circle

    ```js
    path.circleTo(radius);
    ```

  - Ellipse

    ```js
    path.ellipseTo(xRadius, yRadius);
    ```

  - Arc

    ```js
    path.ellipseTo(xRadius, yRadius, startAngle, endAngle, clockwise, rotation);
    ```

Properties:

- `curve.p0` :中点.
  - `curve.p0.x`, `curve.p0.y`
- `curve.xRadius`, `curve.yRadius` :水平/垂直半径.
- `curve.startAngle`,`curve.endAngle`:起始/末角,以度计.
- `curve.clockwise` : `true` 如果顺时针, `false` 如果逆时针。
- `curve.angle` :旋转,以度数计.
  - `curve.rotation` :旋转,用弧度表示.

#### 斯普林线 {#spline}

- 添加示意图对象

  1. 创建示意图对象

     ```js
     var curve = new Phaser.Curves.Spline([
       p0, // {x, y}, or [x, y]
       p1, // {x, y}, or [x, y]
       // ...
     ]);
     ```

     or

     ```js
     var curve = new Phaser.Curves.Spline([
       x0,
       y0,
       x1,
       y1,
       // ...
     ]);
     ```

  1. 添加到路径

     ```js
     path.add(curve);
     ```

- 从上一个终点开始添加到下一个点

  ```js
  var points = ;
  path.splineTo([
      p0,            // {x, y}, or [x, y]
      p1,            // {x, y}, or [x, y]
      // ...
  ]);
  ```

  or

  ```js
  path.splineTo([
    x0,
    y0,
    x1,
    y1,
    // ...
  ]);
  ```

##### 附加点 {#append-point}

```js
var point = curve.addPoint(x, y);
```

#### 四边形比齐尔曲线 {#quadratic-bezier-curve}

1. 创建四边形比齐尔曲线对象

   ```js
   var curve = new Phaser.Curves.QuadraticBezier(
     startPoint,
     controlPoint,
     endPoint
   ); // point: {x, y}
   ```

   or

   ```js
   var points = [
     x0,
     y0, // start point
     x1,
     y1, // control point
     x2,
     y2, // end point
   ];
   var curve = new Phaser.Curves.QuadraticBezier(points);
   ```

1. 添加到路径

   ```js
   path.add(curve);
   ```

添加从上一个终点开始的四边形贝塞尔曲线到下一个终点

```js
path.quadraticBezierTo(endX, endY, controlX, controlY);
```

or

```js
path.quadraticBezierTo(endPoint, controlPoint); // point : Phaser.Math.Vector2
```

#### 立方体贝塞尔曲线 {#cubic-bezier-curve}

1. 创建四边形比齐尔曲线对象

   ```js
   var curve = new Phaser.Curves.CubicBezier(
     startPoint,
     controlPoint1,
     controlPoint2,
     endPoint
   ); // point: {x, y}
   ```

   or

   ```js
   var points = [
     x0,
     y0, // start point
     x1,
     y1, // control point1
     x2,
     y2, // control point2
     x3,
     y3, // end point
   ];
   var curve = new Phaser.Curves.CubicBezier(points);
   ```

1. 添加到路径

   ```js
   path.add(curve);
   ```

添加从上一个终点开始的立方贝塞尔曲线到下一个终点

```js
path.cubicBezierTo(endX, endY, control1X, control1Y, control2X, control2Y);
```

or

```js
path.cubicBezierTo(endPoint, controlPoint1, controlPoint2); // point : Phaser.Math.Vector2
```

#### 移动到点上 {#move-to-point}

```js
path.moveTo(x, y);
```

#### 从 JSON 添加曲线 {#add-curves-from-json}

```js
path.fromJSON(json);
```

### 获取曲线 {#get-curves}

```js
var curves = path.curves;
```

#### 曲线在 t 时得到 {#get-curve-at-t}

```js
var curve = path.getCurveAt(t);
```

- `t`:路径上的正常位置. `0`与`1`之间

### 绘制于 [graphics](/guide/concepts/gameobjects/graphics) {#draw-on-graphics}

```js
path.draw(graphics);
// path.draw(graphics, pointsTotal);
```

- `pointsTotal`:每条曲线要绘制的点数。

or

```js
curve.draw(graphics);
// curve.draw(graphics, pointsTotal);
```

- `pointsTotal` :曲线的分辨率。

### 点 {#point}

- 点头

  ```js
  var out = path.getPoint(t); // t: 0 ~ 1
  // var out = path.getPoint(t, out);  // modify out
  ```

  or

  ```js
  var out = curve.getPoint(t); // t: 0 ~ 1
  // var out = curve.getPoint(t, out);  // modify out
  ```

  从起始点到目标点(出)的路径距离可能与 t 无关。

- 获取随机点

  ```js
  var out = path.getRandomPoint();
  // var out = path.getRandomPoint(out);  // modify out
  ```

  or

  ```js
  var out = curve.getRandomPoint();
  // var out = curve.getRandomPoint(out);  // modify out
  ```

- 获取n点

  - Path

    ```js
    var points = path.getPoints(divisions);
    ```

    - `divisions`: 分辨率**每曲线**的分区数**.

  - Curve

    ```js
    var points = curve.getPoints(divisions);
    // var points = curve.getPoints(divisions, undefined, out);
    ```

    or

    ```js
    var points = curve.getPoints(undefined, stepRate);
    // var points = curve.getPoints(undefined, stepRate, out);
    ```

    - `divisions` :此曲线中的分区数.
      1. `divisions`,如果 `divisions > 0`,其他则
      1. `this.getLength / stepRate`,如果 `stepRate > 0`,其他则
      1. `defaultDivisions`
    - `points` : 返回( E) `1 + divisions` 点。

- 获得(n+1)点,在曲线上相等间隔

  ```js
  var points = path.getSpacedPoints(n);
  ```

  or

  ```js
  var points = curve.getSpacedPoints(n);
  // var points = curve.getSpacedPoints(undefined, stepRate);
  // var points = curve.getSpacedPoints(divisions, stepRate, out);
  ```

- 将点数间隔为 n 像素

  ```js
  var points = curve.getDistancePoints(n);
  ```

  距离越小,阵列就会越大.  
   路径对象的**NOT**支持此特性。

- 获取起始点

  ```js
  var out = path.getStartPoint();
  // var out = path.getStartPoint(out);  // modify out
  ```

  or

  ```js
  var out = curve.getStartPoint();
  // var out = curve.getStartPoint(out);  // modify out
  ```

- 获取终点

  ```js
  var out = path.getEndPoint();
  // var out = path.getEndPoint(out);  // modify out
  ```

  or

  ```js
  var out = curve.getEndPoint();
  // var out = curve.getEndPoint(out);  // modify out
  ```

- 从距离获取 t (0~ 1)

  ```js
  var t = curve.getTFromDistance(d);
  ```

  路径对象的**NOT**支持此特性。

- 获取正切

  ```js
  var out = path.getTangent(t); // t: 0~1
  // var out = path.getTangent(t, out);  // modify out
  ```

  or

  ```js
  var out = curve.getTangent(t); // t: 0~1
  // var out = curve.getTangent(t, out);  // modify out
  ```

### 路径长度 {#length-of-path}

```js
var l = path.getLength();
```

or

```js
var l = curve.getLength();
```

路径/ 曲线的长度将被缓存 。

#### 更新长度 {#update-length}

```js
path.updateArcLengths();
```

or

```js
curve.updateArcLengths();
```

### 曲线到 JSON {#curves-to-json}

```js
var json = path.toJSON();
```

or

```js
var json = curve.toJSON();
```

### 路径约束 {#path-bounds}

获得界限

```js
var out = path.getBounds(); // accuracy = 16
// var out = path.getBounds(out);
// var out = path.getBounds(out, accuracy);
```

or

```js
var out = curve.getBounds(); // accuracy = 16
// var out = curve.getBounds(out);
// var out = curve.getBounds(out, accuracy);
```

- `out` 资源: [rectangle object](/guide/concepts/geometry#rectangle)

### 销毁路径 {#destroy-path}

```js
path.destroy();
```

## 作者的信用额度 {#author-credits}

本页的内容包括下列工作:

- [RexRainbow](https://github.com/rexrainbow)

---
