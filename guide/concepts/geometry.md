# 几何 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/geometry)

Phaser有一套广泛的几何类,这些类被物理和输入系统内部使用,但也可以在自己的游戏中使用. 提供几何类包括:圆形,椭圆形,线形,点形,多边形,矩形,三角形和网状类.

每个类都有一套方法和支持功能,可以让您在它们上执行几何操作。例如,您可以检查一个点是否包含在一个圆内,获得椭圆的界限,或者从一行中获取最近的点,以及许多其他特征.

也有广泛的交叉函数。您可以测试一个圆形与矩形相交,或者从点到多边形的射线等条件。

几何类不是游戏对象。 您不能将它们添加到“ 显示列表 ” 中。 相反, 把它们看作您可以用来执行几何操作的数据结构, 大多数游戏都倾向于有相当一部分。

## 圆形 {#circle}

### 创建圆 {#create-circle}

```js
var circle = new Phaser.Geom.Circle(x, y, radius);
```

### 克隆圆 {#clone-circle}

```js
var circle1 = Phaser.Geom.Circle.Clone(circle0);
```

### 绘制图形对象 {#draw-on-graphics-object}

- 填充形状

  ```js
  // graphics.fillStyle(color, alpha);   // color: 0xRRGGBB
  graphics.fillCircleShape(circle);
  ```

- 划线形状

  ```js
  // graphics.lineStyle(lineWidth, color, alpha);   // color: 0xRRGGBB
  graphics.strokeCircleShape(circle);
  ```

!!! note
负半径将被视为正半径,即`Math.abs(radius)`

### 设置圆形属性 {#set-circle-properties}

- 所有属性

  ```js
  circle.setTo(x, y, radius);
  ```

  or

  ```js
  Phaser.Geom.Circle.CopyFrom(source, dest);
  ```

  !!! note
  `CopyFrom` 需要已有的源和离线圆圈

- Position

  ```js
  circle.setPosition(x, y);
  ```

  or

  ```js
  circle.x = 0;
  circle.y = 0;
  ```

  or

  ```js
  circle.left = 0; // circle.x
  circle.top = 0; // circle.y
  // circle.right = 0;   // circle.x
  // circle.bottom = 0;  // circle.y
  ```

  or

  ```js
  Phaser.Geom.Circle.Offset(circle, dx, dy); // circle.x += dx, circle.y += dy
  ```

  or

  ```js
  Phaser.Geom.Circle.OffsetPoint(circle, point); // circle.x += point.x, circle.y += point.y
  ```

- Radius

  ```js
  circle.radius = radius;
  ```

  or

  ```js
  circle.diameter = diameter; // diameter = 2 * radius
  ```

### 获取属性 {#get-properties}

- Position

  ```js
  var x = circle.x;
  var y = circle.y;
  var top = circle.top;
  var left = circle.left;
  var right = circle.right;
  var bottom = circle.bottom;
  ```

- Radius

  ```js
  var radius = circle.radius;
  // var diameter = circle.diameter;
  ```

- Bounds

  ```js
  var bound = Phaser.Geom.Circle.GetBounds(circle);
  // var bound = Phaser.Geom.Circle.GetBounds(circle, bound);  // push bound
  ```

  - `bound`: `GetBounds`返回矩形

- Area

  ```js
  var area = Phaser.Geom.Circle.Area(circle);
  ```

- Circumference

  ```js
  var circumference = Phaser.Geom.Circle.Circumference(circle);
  ```

- Type:

  ```js
  var type = circle.type; // GEOM_CONST.CIRCLE or 0
  ```

### 点形状( F) {#points-shape}

- 点到圆圈的边缘

  ```js
  var point = circle.getPoint(t);
  // var point = circle.getPoint(t, point);
  ```

  - Arguments:
    - `t` : 0到1之间的值,其中0等于0度,0.5等于180度,1等于360环绕圆圈.
    - `point`:如果没有提供点,则返回已有点或新点

  or

  ```js
  var point = Phaser.Geom.Circle.CircumferencePoint(circle, angle); // angle in radians
  // var point = Phaser.Geom.Circle.CircumferencePoint(circle, angle, point);  // modify existing point or returns a new point if point is not provided
  ```

- 获得圆内随机点

  ```js
  var point = circle.getRandomPoint();
  // var point = circle.getRandomPoint(point);  // modify existing point or returns a new point if point is not provided
  ```

- 绕圈边点数.
  - 根据数量:
  
  ```js
  var points = circle.getPoints(quantity);
  // var points = circle.getPoints(quantity, null, pointsArray);  // If pointsArray not provided a new array will be created.
  ```

  - 根据stepRate:

  ```js
  var points = circle.getPoints(false, stepRate);
  // var points = circle.getPoints(false, stepRate, pointsArray);  // If pointsArray not provided a new array will be created.
  ```

  - `pointsArray` : 一个已有的阵列
  - `stepRate`:通过将圆圈的圆圈除以stepRate来设定数量

- 点在圆内

  ```js
  var isInside = circle.contains(x, y);
  ```

  or

  ```js
  var isInside = Phaser.Geom.Circle.ContainsPoint(circle, point);
  ```

- 矩形为内形

  ```js
  var isInside = Phaser.Geom.Circle.ContainsRect(circle, rect); // rect : 4 points
  ```

### 空的 。 {#empty}

- 设置为空

  ```js
  circle.setEmpty(); // circle.radius = 0
  ```

- 空的 。

  ```js
  var isEmpty = circle.isEmpty(); // circle.radius <= 0
  ```

### 平等 {#equal}

```js
var isEqual = Phaser.Geom.Circle.Equals(circle0, circle1);
```

位置和半径相等.

### 交叉 {#intersection}

#### 圆形至 [circle](#circle) {#circle-to-circle}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.CircleToCircle(circleA, circleB);
  ```

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetCircleToCircle(circleA, circleB);
  // var out = Phaser.Geom.Intersects.GetCircleToCircle(circleA, circleB, out);
  ```

#### 圆形至 [rectangle](#rectangle) {#circle-to-rectangle}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.CircleToRectangle(circle, rect);
  ```

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetCircleToRectangle(circle, rect);
  // var out = Phaser.Geom.Intersects.GetCircleToRectangle(circle, rect, out);
  ```

#### 圆形至 [triangle](#triangle) {#circle-to-triangle}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.TriangleToCircle(triangle, circle);
  ```

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetTriangleToCircle(triangle, circle);
  // var out = Phaser.Geom.Intersects.GetTriangleToCircle(triangle, circle, out);
  ```

#### 圆形至 [line](#line) {#circle-to-line}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.LineToCircle(line, circle);
  // var result = Phaser.Geom.Intersects.LineToCircle(line, circle, nearest);
  ```

  - `nearest` : 线上最近的点.

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetLineToCircle(line, circle);
  // var out = Phaser.Geom.Intersects.GetLineToCircle(line, circle, out);
  ```

## 椭圆 {#ellipse}

### 创建椭圆 {#create-ellipse}

```js
var ellipse = new Phaser.Geom.Ellipse(x, y, width, height);
```

### 克隆椭圆 {#clone-ellipse}

```js
var ellipse1 = Phaser.Geom.Ellipse.Clone(ellipse0);
```

### 绘制图形对象 {#draw-on-graphics-object-1}

- 填充形状

  ```js
  // graphics.fillStyle(color, alpha);   // color: 0xRRGGBB
  graphics.fillEllipseShape(ellipse);
  ```

- 划线形状

  ```js
  // graphics.lineStyle(lineWidth, color, alpha);   // color: 0xRRGGBB
  graphics.strokeEllipseShape(ellipse);
  ```

!!! note
负宽,高度将被视为正宽,高度,即`Math.abs(width)`,`Math.abs(height)`.

### 设置属性 {#set-properties}

- 所有属性

  ```js
  ellipse.setTo(x, y, width, height);
  ```

  or

  ```js
  Phaser.Geom.Ellipse.CopyFrom(source, dest);
  ```

  !!! note
  `CopyFrom` 需要已有的源和离线圆圈

- Position

  ```js
  ellipse.setPosition(x, y);
  ```

  or

  ```js
  ellipse.x = 0;
  ellipse.y = 0;
  ```

  or

  ```js
  ellipse.left = 0; // ellipse.x
  ellipse.top = 0; // ellipse.y
  // ellipse.right = 0;   // ellipse.x
  // ellipse.bottom = 0;  // ellipse.y
  ```

  or

  ```js
  Phaser.Geom.Ellipse.Offset(ellipse, dx, dy); // ellipse.x += dx, ellipse.y += dy
  ```

  or

  ```js
  Phaser.Geom.Ellipse.OffsetPoint(ellipse, point); // ellipse.x += point.x, ellipse.y += point.y
  ```

- 宽度, 高度

  ```js
  ellipse.width = width;
  ellipse.height = height;
  ```

### 获取属性 {#get-properties-1}

- Position

  ```js
  var x = ellipse.x;
  var y = ellipse.y;
  var top = ellipse.top;
  var left = ellipse.left;
  var right = ellipse.right;
  var bottom = ellipse.bottom;
  ```

- 宽度, 高度

  ```js
  var width = ellipse.width;
  var height = ellipse.height;
  ```

- Bounds

  ```js
  var bound = Phaser.Geom.Ellipse.GetBounds(ellipse);
  // var bound = Phaser.Geom.Ellipse.GetBounds(ellipse, bound);  // push bound
  ```

  - `bound`: `GetBounds`返回矩形

- Area

  ```js
  var area = Phaser.Geom.Ellipse.Area(ellipse);
  ```

- Circumference

  ```js
  var circumference = Phaser.Geom.Ellipse.Circumference(ellipse);
  ```

- Type:

  ```js
  var type = ellipse.type; // GEOM_CONST.ELLIPSE or 1
  ```

### 点形状( F) {#points-shape-1}

- 瞄准形状的边缘

  ```js
  var point = ellipse.getPoint(t);
  // var point = ellipse.getPoint(t, point);
  ```

  - Arguments:
    - `t` : 0到1之间的值,其中0等于0度,0.5等于180度,1等于360环绕圆圈.
    - `point`:如果没有提供点,则返回已有点或新点

  or

  ```js
  var point = Phaser.Geom.Ellipse.CircumferencePoint(ellipse, angle); // angle in degrees
  // var point = Phaser.Geom.Ellipse.CircumferencePoint(ellipse, angle, point);  // modify point
  ```

- 获得一个随机点内侧形状

  ```js
  var point = ellipse.getRandomPoint();
  // var point = ellipse.getRandomPoint(point);  // modify point
  ```

- 将点数绕到形状的边缘
  - 根据数量:

  ```js
  var points = ellipse.getPoints(quantity);
  // var points = ellipse.getPoints(quantity, null, pointsArray);  // If pointsArray not provided a new array will be created.
  ```

  - 根据stepRate:

  ```js
  var points = ellipse.getPoints(false, stepRate);
  // var points = ellipse.getPoints(false, stepRate, pointsArray);  // If pointsArray not provided a new array will be created.
  ```

  - `pointsArray` : 一个已有的阵列
  - `stepRate`:通过将椭圆除以stepRate来设定数量

- 点是内在形状

  ```js
  var isInside = ellipse.contains(x, y);
  ```

  or

  ```js
  var isInside = Phaser.Geom.Ellipse.ContainsPoint(ellipse, point);
  ```

- 矩形为内形

  ```js
  var isInside = Phaser.Geom.Ellipse.ContainsRect(ellipse, rect); // rect : 4 points
  ```

### 空的 。 {#empty-1}

- 设置为空

  ```js
  ellipse.setEmpty(); // ellipse.width = 0, ellipse.height = 0
  ```

- 空的 。

  ```js
  var isEmpty = ellipse.isEmpty(); // ellipse.width <= 0 || ellipse.height <= 0
  ```

### 平等 {#equal-1}

```js
var isEqual = Phaser.Geom.Ellipse.Equals(ellipse0, ellipse1);
```

位置和宽度,高度相等.

## 行线 {#line}

### 创建行 {#create-line}

```js
var line = new Phaser.Geom.Line(x1, y1, x2, y2);
```

### 克隆线 {#clone-line}

```js
var line1 = Phaser.Geom.Line.Clone(line0);
```

### 绘制图形对象 {#draw-on-graphics-object-2}

```js
// graphics.lineStyle(lineWidth, color, alpha);   // color: 0xRRGGBB
graphics.strokeLineShape(line);
```

### 设置属性 {#set-properties-1}

- 所有属性

  ```js
  line.setTo(x1, y1, x2, y2);
  ```

  or

  ```js
  Phaser.Geom.Line.CopyFrom(source, dest);
  ```

- Position

  ```js
  line.x1 = 0;
  line.y1 = 0;
  line.x2 = 0;
  line.y2 = 0;
  ```

  or

  ```js
  line.left = 0; // min(x1, x2)
  line.top = 0; // min(y1, y2)
  line.right = 0; // max(x1, x2)
  line.bottom = 0; // max(y1, y2)
  ```

  - 偏移开始, 结束

    ```js
    var line = Phaser.Geom.Line.Offset(line, dx, dy);
    // line.x1 += dx, line.y1 += dy, line.x2 += dx, line.y2 += dy
    ```

  - 设置中心位置

    ```js
    var line = Phaser.Geom.Line.CenterOn(line, x, y);
    ```

- 起点、角度、长度

  ```js
  var line = Phaser.Geom.Line.SetToAngle(line, x, y, angle, length);
  ```

  - `line` : 要设置的线条
  - `x` , `y` : 起点
  - `angle`: 线角以**弧度**

    ```js
    var rad = Phaser.Math.DegToRad(deg);
    ```

  - `length`: 线的长度

- Rotate

  - 绕**中点旋转**

    ```js
    var line = Phaser.Geom.Line.Rotate(line, angle);
    ```

    - `line` : 要设置的线条
    - `angle`: 线角以**弧度**

      ```js
      var rad = Phaser.Math.DegToRad(deg);
      ```

  - 绕点旋转

    ```js
    var line = Phaser.Geom.Line.RotateAroundPoint(line, point, angle);
    ```

    or

    ```js
    var line = Phaser.Geom.Line.RotateAroundXY(line, x, y, angle);
    ```

    - `line` : 要设置的线条
    - `angle`: 线角以**弧度**

      ```js
      var rad = Phaser.Math.DegToRad(deg);
      ```

- Extend

  ```js
  var line = Phaser.Geom.Line.Extend(line, left, right);
  ```

### 获取属性 {#get-properties-2}

- Position

  ```js
  var x1 = line.x1;
  var y1 = line.y1;
  var x2 = line.x2;
  var y2 = line.y2;
  var top = line.top; // min(x1, x2)
  var left = line.left; // min(y1, y2)
  var right = line.right; // max(x1, x2)
  var bottom = line.bottom; // max(y1, y2)
  ```

  - 起点

    ```js
    var start = line.getPointA(); // start: {x, y}
    var start = line.getPointA(start); // push start
    ```

  - 终点

    ```js
    var end = line.getPointB(); // end: {x, y}
    var end = line.getPointB(end); // push end
    ```

  - 中点

    ```js
    var middle = Phaser.Geom.Line.GetMidPoint(line); // middle: {x, y}
    // var middle = Phaser.Geom.Line.GetMidPoint(line, middle);
    ```

- Length

  ```js
  var length = Phaser.Geom.Line.Length(line);
  ```

  - 宽度 : Abs( x1 - x2)

    ```js
    var width = Phaser.Geom.Line.Width(line);
    ```

  - 高度: Abs(y1-y2)

    ```js
    var width = Phaser.Geom.Line.Height(line);
    ```

- Slope

  - 斜坡 : (y2 - y1) / (x2 - x1)

    ```js
    var slope = Phaser.Geom.Line.Slope(line);
    ```

  - 倾斜坡 : -(x2 - x1) /(y2 - y1)

    ```js
    var perpSlope = Phaser.Geom.Line.PerpSlope(line);
    ```

- Angle

  - Angle

    ```js
    var angle = Phaser.Geom.Line.Angle(line);
    ```

    - `angle`: 线角以**弧度**

      ```js
      var deg = Phaser.Math.RadToDeg(rad); // deg : -180 ~ 180
      ```

  - 正常角度( 角 - 90 度)

    - 正常角度

      ```js
      var normalAngle = Phaser.Geom.Line.NormalAngle(line);
      ```

    - 普通矢量

      ```js
      var normal = Phaser.Geom.Line.GetNormal(line); // normal: {x, y}
      // var normal = Phaser.Geom.Line.GetNormal(line, normal);  // push normal
      ```

      or

      ```js
      var normalX = Phaser.Geom.Line.NormalX(line);
      var normalY = Phaser.Geom.Line.NormalY(line);
      ```

  - 反射角度

    ```js
    var reflectAngle = Phaser.Geom.Line.ReflectAngle(aimLine, reflectingLine);
    ```

- Type:

  ```js
  var type = line.type; // GEOM_CONST.LINE or 2
  ```

### 点形状( F) {#points-shape-2}

- 瞄准形状的边缘

  ```js
  var point = line.getPoint(t);
  // var point = line.getPoint(t, point);
  ```

  - Arguments:
    - `t`:0到1之间的值,其中0为起始点,0.5为中间点,1为线的终点.
    - `point`:如果没有提供点,则返回已有点或新点

- 获得一个随机点内侧形状

  ```js
  var point = line.getRandomPoint();
  // var point = line.getRandomPoint(point);  // modify point
  ```

- 将点数绕到形状的边缘
  - 根据数量:
  
  ```js
  var points = line.getPoints(quantity);
  // var points = line.getPoints(quantity, null, pointsArray);  // push points
  ```

  - 根据stepRate:

  ```js
  var points = line.getPoints(false, stepRate);
  // var points = line.getPoints(false, stepRate, pointsArray);  // If pointsArray not provided a new array will be created.
  ```

  - `pointsArray` : 一个已有的阵列
  - `stepRate`:线上每个点之间的距离

- 使用 _Bresenham_ 的线程算法获取点数

  ```js
  var points = Phaser.Geom.Line.BresenhamPoints(line, step);
  // var points = Phaser.Geom.Line.BresenhamPoints(line, step, points);  // push points
  ```

- 使用放松函数获取点数

  ```js
  var points = Phaser.Geom.Line.GetEasedPoints(line, ease, quantity);
  // var points = Phaser.Geom.Line.GetEasedPoints(line, ease, quantity, collinearThreshold, easeParams);
  ```

  - `ease`:[ease function](/guide/concepts/tweens#easing-equations)的弦,或自定义函数(`function (t) { return value}`).
  - `quantity` : 返回的点数。
  - `collinearThreshold` : 每个点至少被隔开这个距离。 这有助于减少噪音易感的集群 。
  - `easeParams` : 随易性而去的易性参数阵列.

- 获取垂直线上到指定点的最近点。

  ```js
  var point = Phaser.Geom.Line.GetNearestPoint(line, pointIn);
  // var point = Phaser.Geom.Line.GetNearestPoint(line, pointIn, point);
  ```

- 从一行到给定点的距离最短.

  ```js
  var distance = Phaser.Geom.Line.GetShortestDistance(line, point);
  ```

### 平等 {#equal-2}

```js
var isEqual = Phaser.Geom.Line.Equals(line0, line1);
```

x1,y2,x2,y2是等价的.

### 交叉 {#intersection-1}

#### 直线到 [circle](#circle) {#line-to-circle}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.LineToCircle(line, circle);
  // var result = Phaser.Geom.Intersects.LineToCircle(line, circle, nearest);
  ```

  - `nearest` : 线上最近的点.

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetLineToCircle(line, circle);
  // var out = Phaser.Geom.Intersects.GetLineToCircle(line, circle, out);
  ```

#### 直线到 [rectangle](#rectangle) {#line-to-rectangle}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.LineToRectangle(line, rect);
  ```

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetLineToRectangle(line, rect);
  // var out = Phaser.Geom.Intersects.GetLineToRectangle(line, rect, out);
  ```

#### 直线到 [triangle](#triangle) {#line-to-triangle}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.TriangleToLine(triangle, line);
  ```

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetTriangleToLine(triangle, line);
  // var out = Phaser.Geom.Intersects.GetTriangleToLine(triangle, line, out);
  ```

#### 直线到 [line](#line) {#line-to-line}

- 交汇点

  ```js
  var isIntersection = Phaser.Geom.Intersects.LineToLine(line1, line2);
  ```

  - `isIntersection`: 如果1号线和2号线交汇,则返回`true`

- 获取交叉点

  ```js
  var isIntersection = Phaser.Geom.Intersects.LineToLine(line1, line2, out);
  ```

  - `isIntersection`: 如果1号线和2号线交汇,则返回`true`
  - `out`: 交点

## 点 {#point}

### 创建点 {#create-point}

```js
var point = new Phaser.Geom.Point(x, y);
```

### 克隆点 {#clone-point}

```js
var point1 = Phaser.Geom.Point.Clone(point0);
```

### 绘制图形对象 {#draw-on-graphics-object-3}

```js
// graphics.fillStyle(color, alpha);   // color: 0xRRGGBB
graphics.fillPointShape(point, size);
```

### 设置属性 {#set-properties-2}

- 所有属性

  ```js
  point.setTo(x, y);
  ```

  or

  ```js
  Phaser.Geom.Point.CopyFrom(source, dest);
  ```

- Position

  ```js
  point.x = 0;
  point.y = 0;
  ```

- Round

  - 赛尔:将`Math.ceil()`应用到给定点的每个坐标上

    ```js
    var point = Phaser.Geom.Point.Ceil(point);
    ```

  - 地板:将`Math.floor()`应用到给定点的每个坐标.

    ```js
    var point = Phaser.Geom.Point.Floor(point);
    ```

### 对称 {#symmetry}

- 反转 : x = y, y = x

  ```js
  var point = Phaser.Geom.Point.Invert(point);
  ```

- 负数: x = -x,y = -y

  ```js
  var out = Phaser.Geom.Point.Negative(point);
  // var out = Phaser.Geom.Point.Negative(point, out);  // modify out
  ```

### 获取属性 {#get-properties-3}

- Position

  ```js
  var x = point.x;
  var y = point.y;
  ```

- Type:

  ```js
  var type = point.type; // GEOM_CONST.POINT or 3
  ```

### 平等 {#equal-3}

```js
var isEqual = Phaser.Geom.Point.Equals(point0, point1);
```

x,y是平等的.

### 点 {#points}

- 中心点:一些点的中点

  ```js
  var out = Phaser.Geom.Point.GetCentroid(points);
  // var out = Phaser.Geom.Point.GetCentroid(points, out);  // modify out
  ```

- 从数组点( [rectangle](#rectangle)) 计算轴对齐的边框( 或 aabb)

  ```js
  var rect = Phaser.Geom.Point.GetRectangleFromPoints(points);
  // var rect = Phaser.Geom.Point.GetRectangleFromPoints(points, rect);  // modify rect
  ```

- Interpolate

  ```js
  var out = Phaser.Geom.Point.Interpolate(pointA, pointB, t); // out : point
  // var out = Phaser.Geom.Point.Interpolate(pointA, pointB, t, out);  // modify out
  ```

### 交叉 {#intersection-2}

- 指向 [line](#line) 时

  ```js
  var result = Phaser.Geom.Intersects.PointToLine(point, line);
  // var result = Phaser.Geom.Intersects.PointToLine(point, line, lineThickness);
  ```

  ```js
  var result = Phaser.Geom.Intersects.PointToLineSegment(point, line);
  ```

### 点为矢量 {#point-as-vector}

矢量开始于 (0, 0)

- 宽度:sqrt(x_)+(y_y) ).

  ```js
  var magnitude = Phaser.Geom.Point.GetMagnitude(point);
  ```

  or

  ```js
  var magnitudeSq = Phaser.Geom.Point.GetMagnitudeSq(point);
  ```

- Project

  ```js
  var out = Phaser.Geom.Point.Project(from, to);
  // var out = Phaser.Geom.Point.Project(from, to, out);  // modify out
  ```

  or

  ```js
  var out = Phaser.Geom.Point.ProjectUnit(from, to); // vector `from` and `to` are unit vector (length = 1)
  // var out = Phaser.Geom.Point.ProjectUnit(from, to, out);  // modify out
  ```

## 多边形 {#polygon}

### 创建多边形 {#create-polygon}

```js
var polygon = new Phaser.Geom.Polygon(points);
```

- `points` :
  - 数字阵列: `[x0, y0, x1, y1, ...]`
  - 数组点数 : `[{x:x0, y:y0}, {x:x1, y:y1}, ...]`
  - 字符串: `'x0 y0 x1 y1 ...'`

### 克隆多边形 {#clone-polygon}

```js
var polygon1 = Phaser.Geom.Polygon.Clone(polygon0);
```

### 绘制图形对象 {#draw-on-graphics-object-4}

- 填充形状

  ```js
  // graphics.fillStyle(color, alpha);   // color: 0xRRGGBB
  graphics.fillPoints(polygon.points, true);
  ```

- 划线形状

  ```js
  // graphics.lineStyle(lineWidth, color, alpha);   // color: 0xRRGGBB
  graphics.strokePoints(polygon.points, true);
  ```

### 设置属性 {#set-properties-3}

```js
polygon.setTo(points);
// points = [x0, y0, x1, y1, x2, y2, ...] , or [{x,y}, {x,y}, {x,y}, ...]
```

### 获取属性 {#get-properties-4}

- Points

  ```js
  var points = polygon.points; // array of points {x,y}
  ```

- Area

  ```js
  var area = polygon.area;
  ```

- 数字数组

  ```js
  var out = Phaser.Geom.Polygon.GetNumberArray(polygon);
  // var out = Phaser.Geom.Polygon.GetNumberArray(polygon, out);  // modify out
  ```

  - `arr`: [x0, y0, x1, y1, x2, y2, ...] (中文(简体) ).

- AABB( 覆盖这个多边形的最小矩形)

  ```js
  var out = Phaser.Geom.Polygon.GetAABB(polygon);
  // var out = Phaser.Geom.Polygon.GetAABB(polygon, out);
  ```

  - `out` 资源: [rectangle](#rectangle)

- Type:

  ```js
  var type = polygon.type; // GEOM_CONST.POLYGON or 4
  ```

### 点形状( F) {#points-shape-3}

- 点是内在形状

  ```js
  var isInside = polygon.contains(x, y);
  ```

  or

  ```js
  var isInside = Phaser.Geom.Polygon.ContainsPoint(polygon, point);
  ```

- 翻译: Shift points.

  ```js
  Phaser.Geom.Polygon.Translate(polygon, x, y);
  ```

- 倒转点数顺序.

  ```js
  var polygon = Phaser.Geom.Polygon.Reverse(polygon);
  ```

- 平滑 : 取一个多边形对象,并在其点上应用Chaikin的平滑算法.

  ```js
  Phaser.Geom.Polygon.Smooth(polygon);
  ```

- 简化:通过组合来简化积分
  道格拉斯-佩克和辐射距离算法。
  在保留多边形形状的同时减少多边形中的点数,给出
  处理时的性能大增 也减少了视觉噪音

  ```js
  var polygon = Phaser.Geom.Polygon.Simplify(polygon);
  // var polygon = Phaser.Geom.Polygon.Simplify(polygon, tolerance, highestQuality);
  ```

- 绕多边形的周界找点
  - 根据数量:
  
  ```js
  var points = polygon.getPoints(quantity);
  // var points = polygon.getPoints(quantity, null, pointsArray);  // If pointsArray not provided a new array will be created.
  ```

  - 根据stepRate:

  ```js
  var points = polygon.getPoints(false, stepRate);
  // var points = polygon.getPoints(false, stepRate, pointsArray);  // If pointsArray not provided a new array will be created.
  ```

  - `pointsArray` : 一个已有的阵列
  - `stepRate`:通过将多边形的周边划分为stepRate来设定数量

### 向量到多边形 {#vector-to-polygon}

- 获取向量和多边形数组之间最接近的交汇点

  ```js
  var result = Phaser.Geom.Intersects.GetLineToPolygon(line, polygons);
  // var out = Phaser.Geom.Intersects.GetLineToPolygon(line, polygons, isRay, out);
  ```

  - `line`: [line](#line)天体的矢量
  - `polygons`: 单一多边形,或多边形阵列
  - `isRay`:`line`是射线还是线段?
  - `out` :
    - `out.x`,`out.y`:交点
    - `out.z`:最接近的交叉距离
    - `out.w`:多边形索引

- 工程射线从给定点射向多边形的每个线段。

  ```js
  var out = Phaser.Geom.Intersects.GetRaysFromPointToPolygon(x, y, polygons);
  ```

  - `x`, `y` :射线的射线点.
  - `polygons`: 单一多边形,或多边形阵列
  - `out`:包含所有交叉的阵列
    - `out[i].x`,`out[i].y`:交点
    - `out[i].z`: 交叉角
    - `out[i].w`:多边形索引

## 矩形 {#rectangle}

### 创建矩形 {#create-rectangle}

```js
var rect = new Phaser.Geom.Rectangle(x, y, width, height);
```

### 从点创建矩形 {#create-rectangle-from-points}

所有给定的点数都在它的界限内或范围内.

```js
var rect = Phaser.Geom.Rectangle.FromPoints(points);
// var rect = Phaser.Geom.Rectangle.FromPoints(points, rect);  // push rect
```

- `points`:一个有4个点的阵列. `[x, y]`,或`{x:0, y:0}`.

or

```js
var rect = Phaser.Geom.Rectangle.FromXY(x1, y1, x2, y2);
// var rect = Phaser.Geom.Rectangle.FromXY(x1, y1, x2, y2, rect);  // push rect
```

### 克隆矩形 {#clone-rectangle}

```js
var rect1 = Phaser.Geom.Rectangle.Clone(rect0);
```

### 绘制图形对象 {#draw-on-graphics-object-5}

- 填充形状

  ```js
  // graphics.fillStyle(color, alpha);   // color: 0xRRGGBB
  graphics.fillRectShape(rect);
  ```

- 划线形状

  ```js
  // graphics.lineStyle(lineWidth, color, alpha);   // color: 0xRRGGBB
  graphics.strokeRectShape(rect);
  ```

!!! note
`x` 带正/负宽的左/右绑定  
带正/负高度的`y`为上/下绑定

### 设置属性 {#set-properties-4}

- 所有属性

  ```js
  rect.setTo(x, y, width, height);
  ```

  or

  ```js
  Phaser.Geom.Rectangle.CopyFrom(source, dest);
  ```

- Position

  ```js
  rect.setPosition(x, y);
  ```

  or

  ```js
  rect.x = 0;
  rect.y = 0;
  ```

  or

  ```js
  rect.left = 0; // rect.x, rect.width
  rect.top = 0; // rect.y, rect.height
  // rect.right = 0;   // rect.x, rect.width
  // rect.bottom = 0;  // rect.y, rect.height
  rect.centerX = 0; // rect.x
  rect.centerY = 0; // rect.y
  ```

  or

  ```js
  Phaser.Geom.Rectangle.Offset(rect, dx, dy); // rect.x += dx, rect.y += dy
  ```

  or

  ```js
  Phaser.Geom.Rectangle.OffsetPoint(rect, point); // rect.x += point.x, rect.y += point.y
  ```

  or

  ```js
  Phaser.Geom.Rectangle.CenterOn(rect, x, y); // rect.x = x - (rect.width / 2), rect.y = y - (rect.height / 2)
  ```

- Size

  ```js
  rect.setSize(width, height);
  // rect.setSize(width);   // height = width
  ```

  or

  ```js
  rect.width = 0;
  rect.height = 0;
  ```

  - Scale

    ```js
    Phaser.Geom.Rectangle.Scale(rect, x, y); // rect.width *= x, rect.height *= y;
    // Phaser.Geom.Rectangle.Scale(rect, x);   // y = x
    ```

  - 扩展大小以包含点数

    ```js
    Phaser.Geom.Rectangle.MergePoints(rect, points);
    ```

    - `points` : 一系列点。 `[x, y]`,或 ,或 , `{x:0, y:0}`

  - 扩展大小以包括另一个矩形

    ```js
    Phaser.Geom.Rectangle.MergeRect(target, source);
    ```

- Inflate

  ```js
  Phaser.Geom.Rectangle.Inflate(rect, x, y);
  ```

  1. 更改大小为 `width += x*2, height += y*2`
  1. 以上一个位置为中心

- 将目标矩形配到源矩形

  ```js
  Phaser.Geom.Rectangle.FitInside(target, source);
  ```

  保留目标矩形到源矩形的纵横比、尺度和中心

- 匹配目标矩形, 绕源矩形

  ```js
  Phaser.Geom.Rectangle.FitOutside(target, source);
  ```

  保留目标矩形到源矩形的纵横比、尺度和中心

- Ceil

  ```js
  Phaser.Geom.Rectangle.Ceil(rect); // ceil x, y
  ```

  ```js
  Phaser.Geom.Rectangle.CeilAll(rect); // ceil x, y, width, height
  ```

- Floor

  ```js
  Phaser.Geom.Rectangle.Floor(rect); // floor x, y
  ```

  ```js
  Phaser.Geom.Rectangle.FloorAll(rect); // floor x, y, width, height
  ```

### 获取属性 {#get-properties-5}

- Position

  ```js
  var x = rect.x;
  var y = rect.y;
  ```

  - Bound

    ```js
    var top = rect.top;
    var left = rect.left;
    var right = rect.right;
    var bottom = rect.bottom;
    ```

    or

    ```js
    var points = Phaser.Geom.Rectangle.Decompose(rect);
    // var points = Phaser.Geom.Rectangle.Decompose(rect, points); // push result points
    ```

    - `points`:左上右下左

  - Center

    ```js
    var centerX = rect.centerX;
    var centerY = rect.centerY;
    ```

    or

    ```js
    var point = Phaser.Geom.Rectangle.GetCenter(rect);
    // var point = Phaser.Geom.Rectangle.GetCenter(rect, point);
    ```

- Size

  ```js
  var width = rect.width;
  var height = rect.height;
  ```

  or

  ```js
  var point = Phaser.Geom.Rectangle.GetSize(rect); // {x: rect.width, y: rect.height}
  ```

- Area

  ```js
  var area = Phaser.Geom.Rectangle.Area(rect);
  ```

- Perimeter

  ```js
  var perimeter = Phaser.Geom.Rectangle.Perimeter(rect); // 2 * (rect.width + rect.height)
  ```

- 光谱比

  ```js
  var aspectRatio = Phaser.Geom.Rectangle.GetAspectRatio(rect); // rect.width / rect.height
  ```

- 矩形周围的线条

  ```js
  var topLine = rect.getLineA(); // top line of this rectangle
  var rightLine = rect.getLineB(); // right line of this rectangle
  var bottomLine = rect.getLineC(); // bottom line of this rectangle
  var leftLine = rect.getLineD(); // left line of this rectangle
  // var out = rect.getLineA(out);  // top line of this rectangle
  ```

- Type:

  ```js
  var type = rect.type; // GEOM_CONST.RECTANGLE or 5
  ```

### 点形状( F) {#points-shape-4}

- 瞄准形状的边缘

  ```js
  var point = rect.getPoint(t); // t : 0 ~ 1 (0= top-left, 0.5= bottom-right, 1= top-left)
  // var point = rect.getPoint(t, point);
  ```

  - Arguments:
    - `t` : 0或1的值位于左上角,0.5为右下角。0至0.5的值位于右上角,0.5至1的值位于左下角。
    - `point`:如果没有提供点,则返回已有点或新点

  or

  ```js
  var point = Phaser.Geom.Rectangle.PerimeterPoint(rect, angle); // angle in degrees
  // var point = Phaser.Geom.Rectangle.PerimeterPoint(rect, angle, point);  // push point
  ```

- 将点数绕到形状的边缘
  - 根据数量:
  
  ```js
  var points = rect.getPoints(quantity);
  // var points = rect.getPoints(quantity, null, pointsArray);  // push points
  ```

  - 根据stepRate:

  ```js
  var points = rect.getPoints(false, stepRate);
  // var points = rect.getPoints(false, stepRate, pointsArray);  // If pointsArray not provided a new array will be created.
  ```

  - `pointsArray` : 一个已有的阵列
  - `stepRate` : 如果数量为 0, 确定每个返回点之间的正常距离

- 点是内在形状

  ```js
  var isInside = rect.contains(x, y);
  ```

  or

  ```js
  var isInside = Phaser.Geom.Rectangle.ContainsPoint(rect, point);
  ```

- 获得一个随机点内侧形状

  ```js
  var point = rect.getRandomPoint();
  // var point = rect.getRandomPoint(point);  // modify point
  ```

- 获取外形的随机点

  ```js
  var point = Phaser.Geom.Rectangle.RandomOutside(outer, inner);
  // var point = Phaser.Geom.Rectangle.RandomOutside(outer, inner, point); // modify point
  ```

- 矩形为内形

  ```js
  var isInside = Phaser.Geom.Rectangle.ContainsRect(rectA, rectB); // rectB is inside rectA
  ```

### 多个矩形 {#multiple-rectangles}

- 重叠

  ```js
  var isOverlapping = Phaser.Geom.Rectangle.Overlaps(rectA, rectB);
  ```

- 获取交叉矩形

  ```js
  var rect = Phaser.Geom.Rectangle.Intersection(rectA, rectB);
  var rect = Phaser.Geom.Rectangle.Intersection(rectA, rectB, rect); // push rect
  ```

- 获取结合矩形

  ```js
  var rect = Phaser.Geom.Rectangle.Union(rectA, rectB);
  var rect = Phaser.Geom.Rectangle.Union(rectA, rectB, rect); // push rect
  ```

### 空的 。 {#empty-2}

- 设置为空

  ```js
  rect.setEmpty(); // rect.x = 0, rect.y = 0, rect.width = 0, rect.height = 0
  ```

- 空的 。

  ```js
  var isEmpty = rect.isEmpty(); // rect.radius <= 0;
  ```

### 平等 {#equal-4}

- 位置、宽度和高度都是一样的

  ```js
  var isEqual = Phaser.Geom.Rectangle.Equals(rect0, rect1);
  ```

- 身高和身高都一样

  ```js
  var isEqual = Phaser.Geom.Rectangle.SameDimensions(rect0, rect1);
  ```

### 交叉 {#intersection-3}

#### 矩形到 [circle](#circle) {#rectangle-to-circle}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.CircleToRectangle(circle, rect);
  ```

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetCircleToRectangle(circle, rect);
  // var out = Phaser.Geom.Intersects.GetCircleToRectangle(circle, rect, out);
  ```

#### 矩形到 [rectangle](#rectangle) {#rectangle-to-rectangle}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.RectangleToRectangle(rectA, rectB);
  ```

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetRectangleToRectangle(rectA, rectB);
  // var out = Phaser.Geom.Intersects.GetRectangleToRectangle(rectA, rectB, out);
  ```

#### 矩形到 [triangle](#triangle) {#rectangle-to-triangle}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.RectangleToTriangle(rect, triangle);
  ```

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetRectangleToTriangle(rect, triangle);
  // var out = Phaser.Geom.Intersects.GetRectangleToTriangle(rect, triangle, out);
  ```

#### 矩形到 [line](#line) {#rectangle-to-line}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.LineToRectangle(line, rect);
  ```

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetLineToRectangle(line, rect);
  // var out = Phaser.Geom.Intersects.GetLineToRectangle(line, rect, out);
  ```

## 三角形 {#triangle}

### 创建三角形 {#create-triangle}

```js
var triangle = new Phaser.Geom.Triangle(x1, y1, x2, y2, x3, y3);
```

### 克隆三角形 {#clone-triangle}

```js
var triangle1 = Phaser.Geom.Triangle.Clone(triangle0);
```

### 等边三角形 {#equilateral-triangle}

```js
var triangle = Phaser.Geom.Triangle.BuildEquilateral(x1, y1, length);
```

### 右三角形 {#right-triangle}

```js
var triangle = Phaser.Geom.Triangle.BuildRight(x1, y1, width, height);
```

### [Polygon](#polygon) 改为三角形 {#polygon-to-triangles}

```js
var out = Phaser.Geom.Triangle.BuildFromPolygon(data);
// var out = Phaser.Geom.Triangle.BuildFromPolygon(data, holes, scaleX, scaleY);
// out = Phaser.Geom.Triangle.BuildFromPolygon(data, holes, scaleX, scaleY, out);
```

- `data`:像`[x0,y0, x1,y1, x2,y2, ...]`这样的平整的顶点坐标阵列
- `out`:三角形阵列

### 绘制图形对象 {#draw-on-graphics-object-6}

- 填充形状

  ```js
  // graphics.fillStyle(color, alpha);   // color: 0xRRGGBB
  graphics.fillTriangleShape(triangle);
  ```

- 划线形状

  ```js
  // graphics.lineStyle(lineWidth, color, alpha);   // color: 0xRRGGBB
  graphics.strokeTriangleShape(triangle);
  ```

### 设置属性 {#set-properties-5}

- 所有属性

  ```js
  triangle.setTo(x1, y1, x2, y2, x3, y3);
  ```

  or

  ```js
  Phaser.Geom.Triangle.CopyFrom(source, dest);
  ```

- Position

  ```js
  triangle.x1 = 0;
  triangle.y1 = 0;
  triangle.x2 = 0;
  triangle.y2 = 0;
  triangle.x3 = 0;
  triangle.y3 = 0;
  ```

  or

  ```js
  triangle.left = 0; // triangle.x1, triangle.x2, triangle.x3
  triangle.top = 0; // triangle.y1, triangle.y2, triangle.y3
  // triangle.right = 0;   // triangle.x1, triangle.x2, triangle.x3
  // triangle.bottom = 0;  // triangle.y1, triangle.y2, triangle.y3
  ```

  or

  ```js
  Phaser.Geom.Triangle.Offset(triangle, dx, dy); // triangle.x += dx, triangle.y += dy
  ```

  or

  ```js
  Phaser.Geom.Triangle.CenterOn(triangle, x, y);
  ```

- Rotate

  - 旋转中心( 中间)

    ```js
    var triangle = Phaser.Geom.Triangle.Rotate(triangle, angle);
    ```

    - `angle` : 雷达

  - 绕点旋转

    ```js
    var triangle = Phaser.Geom.Triangle.RotateAroundPoint(
      triangle,
      point,
      angle
    );
    ```

    - `point` : `{x, y}`
    - `angle` : 雷达

  - 旋转( x,y)

    ```js
    var triangle = Phaser.Geom.Triangle.RotateAroundXY(triangle, x, y, angle);
    ```

    - `angle` : 雷达

### 获取属性 {#get-properties-6}

- Position

  ```js
  var x1 = triangle.x1;
  var y1 = triangle.y1;
  var x2 = triangle.x2;
  var y2 = triangle.y2;
  var x3 = triangle.x3;
  var y3 = triangle.y3;
  var top = triangle.top;
  var left = triangle.left;
  var right = triangle.right;
  var bottom = triangle.bottom;
  ```

  or

  ```js
  var out = Phaser.Geom.Triangle.Decompose(triangle); // out: [{x1,y1}, {x2,y2}, {x3,y3}]
  // var out = Phaser.Geom.Triangle.Decompose(triangle, out);
  ```

- Perimeter

  ```js
  var perimeter = Phaser.Geom.Triangle.Perimeter(triangle);
  ```

- Area

  ```js
  var area = Phaser.Geom.Triangle.Area(triangle);
  ```

- 三角形周围的线条

  ```js
  var line12 = rect.getLineA(); // line from (x1, y1) to (x2, y2)
  var line23 = rect.getLineB(); // line from (x2, y2) to (x3, y3)
  var line31 = rect.getLineC(); // line from (x3, y3) to (x1, y1)
  ```

- Centroid

  ```js
  var out = Phaser.Geom.Triangle.Centroid(triangle); // out: {x,y}
  ```

- Incenter

  ```js
  var out = Phaser.Geom.Triangle.InCenter(triangle); // out: {x,y}
  // var out = Phaser.Geom.Triangle.InCenter(triangle, out);
  ```

- Circumcenter

  ```js
  var out = Phaser.Geom.Triangle.CircumCenter(triangle); // out: {x,y}
  // var out = Phaser.Geom.Triangle.CircumCenter(triangle, out);
  ```

- Circumcircle

  ```js
  var out = Phaser.Geom.Triangle.CircumCircle(triangle); // out: a circle object
  // var out = Phaser.Geom.Triangle.CircumCircle(triangle, out);
  ```

- Type:

  ```js
  var type = triangle.type; // GEOM_CONST.TRIANGLE or 6
  ```

### 点形状( F) {#points-shape-5}

- 瞄准形状的边缘

  ```js
  var point = triangle.getPoint(t);
  // var point = triangle.getPoint(t, point);
  ```

  - Arguments:
    - `t` : 0 或 1 值是第一个点。 值 0 到 1 返回三角形周边的点 。
    - `point`:如果没有提供点,则返回已有点或新点

- 获得一个随机点内侧形状

  ```js
  var point = triangle.getRandomPoint();
  // var point = triangle.getRandomPoint(point);  // modify point
  ```

- 三角形边缘的点数
  - 根据数量:

  ```js
  var points = triangle.getPoints(quantity);
  // var points = triangle.getPoints(quantity, null, points);  // push points
  ```

  - 根据stepRate:

  ```js
  var points = triangle.getPoints(false, stepRate);
  // var points = triangle.getPoints(false, stepRate, points);  // If pointsArray not provided a new array will be created.
  ```

  - `pointsArray` : 一个已有的阵列
  - `stepRate`: 仅在数量不实和为两点之间的距离时使用

- 点是内在形状

  ```js
  var isInside = triangle.contains(x, y);
  ```

  or

  ```js
  var isInside = Phaser.Geom.Triangle.ContainsPoint(triangle, point);
  ```

  - 内侧形状的点

    ```js
    var out = Phaser.Geom.Triangle.ContainsArray(triangle, points, returnFirst);
    // var out = Phaser.Geom.Triangle.ContainsArray(triangle, points, returnFirst, out);
    ```

    - `out`:三角形内部的点
    - `returnFirst` : 获得匹配的拳头点的真伪

### 平等 {#equal-5}

```js
var isEqual = Phaser.Geom.Triangle.Equals(triangle0, triangle1);
```

位置和半径相等.

### 交叉 {#intersection-4}

#### 三角形改为 [circle](#circle) {#triangle-to-circle}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.TriangleToCircle(triangle, circle);
  ```

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetTriangleToCircle(triangle, circle);
  // var out = Phaser.Geom.Intersects.GetTriangleToCircle(triangle, circle, out);
  ```

#### 三角形改为 [rectangle](#rectangle) {#triangle-to-rectangle}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.RectangleToTriangle(rect, triangle);
  ```

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetRectangleToTriangle(rect, triangle);
  // var out = Phaser.Geom.Intersects.GetRectangleToTriangle(rect, triangle, out);
  ```

#### 三角形改为 [triangle](#triangle) {#triangle-to-triangle}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.TriangleToTriangle(triangleA, triangleB);
  ```

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetTriangleToTriangle(
    triangleA,
    triangleB
  );
  // var out = Phaser.Geom.Intersects.GetTriangleToTriangle(triangleA, triangleB, out);
  ```

#### 三角形改为 [line](#line) {#triangle-to-line}

- 交汇点

  ```js
  var result = Phaser.Geom.Intersects.TriangleToLine(triangle, line);
  ```

- 获取交叉点

  ```js
  var result = Phaser.Geom.Intersects.GetTriangleToLine(triangle, line);
  // var out = Phaser.Geom.Intersects.GetTriangleToLine(triangle, line, out);
  ```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。
- [RexRainbow](https://github.com/rexrainbow)

---
