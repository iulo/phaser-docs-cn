# 图形 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/graphics)

图形对象是绘制游戏原始形状的一种方法。原始对象包括几何形式,如矩形、圆形和多边形。它们还包括线条、弧形和曲线。当你最初创建图形对象时,它将是空的。要绘制到它,必须先指定一个线条样式或填充样式(或两者兼有),用路径绘制形状,最后填充或中标它们。

```js
graphics.lineStyle(5, 0xff00ff, 1.0);
graphics.beginPath();
graphics.moveTo(100, 100);
graphics.lineTo(200, 200);
graphics.closePath();
graphics.strokePath();
```

有许多有用的方法可以画和填充/中键常见的形状给您.

```js
graphics.lineStyle(5, 0xff00ff, 1.0);
graphics.fillStyle(0xffffff, 1.0);
graphics.fillRect(50, 50, 400, 200);
graphics.strokeRect(50, 50, 400, 200);
```

当一个图形对象被渲染出来时, 它会根据游戏在 Canvas 或 WebGL 下运行而产生不同的效果。 Canvas 下将使用 HTML Canvas 上下文绘制操作绘制路径。 WebGL 下, 图形数据会分解成多边形。 这两个过程都是昂贵的, 特别是形状复杂的进程 。

如果您的图形对象在绘制到形状后没有多少变化( 或者完全改变), 您会调用 Phaser.GameObjects.Graphics# generateTexture来帮助执行。 这将“ 将图形对象装入纹理中, 并返回它。 然后您可以使用此纹理来显示 Sprites 或其他显示对象。 如果您的图形对象经常更新, 您应该避免这样做, 因为它会不断生成新的纹理, 它将消耗内存 。

如你所知,图形对象有点相互权衡。虽然它们非常有用,但游戏中需要小心其复杂性和数量。

## 基本使用 {#basic-usage}

### 添加图形对象 {#add-graphics-object}

```js
var graphics = this.add.graphics();
```

or

```js
var graphics = this.add.graphics({
  x: 0,
  y: 0,

  // lineStyle: {
  //     width: 1,
  //     color: 0xffffff,
  //     alpha: 1
  // },
  // fillStyle: {
  //     color: 0xffffff,
  //     alpha: 1
  // },

  add: true,
});
```

### 自定义类 {#custom-class}

- 定义类

  ```js
  class MyGraphics extends Phaser.GameObjects.Graphics {
    constructor(scene, options) {
      super(scene, options);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var graphics = new MyGraphics(this, options);
  ```

## 绘图命令 {#drawing-commands}

### 设置行和填充样式 {#set-line-and-fill-style}

- 设置默认行样式并填充样式

  ```js
  graphics.setDefaultStyles({
    lineStyle: {
      width: 1,
      color: 0xffffff,
      alpha: 1,
    },
    fillStyle: {
      color: 0xffffff,
      alpha: 1,
    },
  });
  ```

- 设置行样式

  ```js
  graphics.lineStyle(lineWidth, color, alpha); // color: 0xRRGGBB
  ```

- 设定填充样式

  - 填充颜色

    ```js
    graphics.fillStyle(color, alpha); // color: 0xRRGGBB
    ```

  - 填充渐变颜色( 仅 WebGL)

    ```js
    graphics.fillGradientStyle(
      topLeft,
      topRight,
      bottomLeft,
      bottomRight,
      alpha
    ); // alpha= 1
    // graphics.fillGradientStyle(topLeft, topRight, bottomLeft, bottomRight, alphaTopLeft, alphaTopRight, alphaBottomLeft, alphaBottomRight);
    ```

    - `topLeft`:正在应用到游戏对象左上角的锡.
    - `topRight`:正在应用到游戏对象的右上角的锡.
    - `bottomLeft`:正在应用到游戏对象左下角的锡.
    - `bottomRight`:正在应用到游戏对象的右下角的锡.
    - `alphaTopLeft` :上部左侧的α值.
    - `alphaTopRight` :右上方的α值.
    - `alphaBottomLeft` : 下方左侧的α值.
    - `alphaBottomRight` :右下方的α值.

### 清除/删除所有绘图 {#clearerase-all-drawings}

```js
graphics.clear();
```

### 绘图路径 {#drawing-paths}

```js
graphics.beginPath();
graphics.closePath();
graphics.fillPath(); // = graphics.fill()
graphics.strokePath(); // = graphics.stroke()
```

### 绘制矩形 {#drawing-rectangles}

```js
graphics.fillRectShape(rect); // rect: {x, y, width, height}
graphics.fillRect(x, y, width, height);
graphics.strokeRectShape(rect); // rect: {x, y, width, height}
graphics.strokeRect(x, y, width, height);
```

### 绘制圆形矩形 {#drawing-rounded-rectangles}

```js
graphics.fillRoundedRect(x, y, width, height, radius);
graphics.strokeRoundedRect(x, y, width, height, radius);
```

- `radius`:编号或物体`{tl, tr, bl, br}`,
  - 正面值:康维克斯角.
  - 负值:孔洞角.

### 绘制三角形 {#drawing-triangles}

```js
graphics.fillTriangleShape(triangle); // triangle: {x1, y1, x2, y2, x3, y3}
graphics.fillTriangle(x1, y1, x2, y2, x3, y3);
graphics.strokeTriangleShape(triangle); // triangle: {x1, y1, x2, y2, x3, y3}
graphics.strokeTriangle(x1, y1, x2, y2, x3, y3);
```

### 绘图点 {#drawing-points}

```js
graphics.fillPointShape(point, size); // point: {x, y}
graphics.fillPoint(x, y, size);
```

### 绘图线 {#drawing-lines}

```js
graphics.strokeLineShape(line); // line: {x1, y1, x2, y2}
graphics.lineBetween(x1, y1, x2, y2);
graphics.lineTo(x, y);
graphics.moveTo(x, y);
```

### 绘制一系列线条 {#drawing-a-series-of-lines}

```js
graphics.strokePoints(points, closeShape, closePath, endIndex); // points: [{x, y}, ...]
graphics.fillPoints(points, closeShape, closePath, endIndex); // points: [{x, y}, ...]
```

- `points`: 一组`{x, y}`
- `closeShape`:当`true`时,通过加入最后一点到第一点的形状关闭.
- `closePath` : 当 `true`,在被中风之前,路径是关闭的。
- `endIndex`: 停止绘图的`points`索引。默认为`points.length` 。

### 绘制圆圈 {#drawing-circles}

```js
graphics.fillCircleShape(circle); // circle: {x, y, radius}
graphics.fillCircle(x, y, radius);
graphics.strokeCircleShape(circle); // circle: {x, y, radius}
graphics.strokeCircle(x, y, radius);
```

按点绘制或填充圆形。

### 绘图椭圆 {#drawing-ellipses}

```js
graphics.strokeEllipseShape(ellipse, smoothness); // ellipse: Phaser.Geom.Ellipse
graphics.strokeEllipse(x, y, width, height, smoothness);
graphics.fillEllipseShape(ellipse, smoothness); // ellipse: Phaser.Geom.Ellipse
graphics.fillEllipse(x, y, width, height, smoothness);
```

以点绘制或填充椭圆形状。

### 绘图弧 {#drawing-arcs}

```js
graphics.arc(x, y, radius, startAngle, endAngle, anticlockwise);
graphics.arc(x, y, radius, startAngle, endAngle, anticlockwise, overshoot);
```

按点绘制弧曲线。

### 绘制饼图片 {#drawing-pie-chart-slices}

```js
graphics.slice(x, y, radius, startAngle, endAngle, anticlockwise);
graphics.slice(x, y, radius, startAngle, endAngle, anticlockwise, overshoot);
```

按点绘制饼图切片形状.

填充此形状

```js
graphics.fillPath();
```

### 清晰的图案 {#clear-pattern}

```js
graphics.setTexture();
```

### 转让 {#transfer}

```js
graphics.save();
graphics.restore();
graphics.translateCanvas(x, y);
graphics.scaleCanvas(x, y);
graphics.rotateCanvas(radians);
```

### 生成纹理 {#generate-texture}

```js
graphics.generateTexture(key, width, height); // key: texture key
```

### 创建遮罩 {#create-mask}

```js
var mask = graphics.createGeometryMask();
```

## 形状 {#shapes}

### 弧形 {#arc}

绘制弧形。 您可以控制弧的起始和结束角度, 或者角度是顺时针还是逆时针。 默认设置会形成一个完整的圆 。

#### 创建形状 {#create-shape}

```js
var arc = this.add.arc(
  x,
  y,
  radius,
  startAngle,
  endAngle,
  anticlockwise,
  fillColor
);
// var arc = this.add.arc(x, y, radius, startAngle, endAngle, anticlockwise, fillColor, fillAlpha);
```

#### 自定义类 {#custom-class-1}

- 定义类

  ```js
  class MyArc extends Phaser.GameObjects.Arc {
    constructor(
      scene,
      x,
      y,
      radius,
      startAngle,
      endAngle,
      anticlockwise,
      fillColor
    ) {
      super(
        scene,
        x,
        y,
        radius,
        startAngle,
        endAngle,
        anticlockwise,
        fillColor
      );
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var arc = new MyArc(
    scene,
    x,
    y,
    radius,
    startAngle,
    endAngle,
    anticlockwise,
    fillColor
  );
  ```

#### 颜色 {#color}

- 填充颜色

  - Get

    ```js
    var color = arc.fillColor;
    var alpha = arc.fillAlpha;
    ```

  - Set

    ```js
    arc.setFillStyle(color, alpha);
    ```

  - Clear

    ```js
    arc.setFillStyle();
    ```

- 划线颜色

  - Get

    ```js
    var color = arc.strokeColor;
    ```

  - Set

    ```js
    arc.setStrokeStyle(lineWidth, color, alpha);
    ```

  - Clear

    ```js
    arc.setStrokeStyle();
    ```

警告"不要用任何手段"
使用`arc.setFillStyle(color, alpha)`来改变颜色.

#### 阿尔法 {#alpha}

- Get

  ```js
  var alpha = arc.alpha;
  ```

- Set

  ```js
  arc.setAlpha(alpha);
  // arc.alpha = alpha;
  ```

#### 角度 {#angle}

- 开始角度,以度计。

  - Get

    ```js
    var startAngle = arc.startAngle;
    ```

  - Set

    ```js
    arc.setStartAngle(startAngle);
    // arc.setStartAngle(startAngle, anticlockwise);
    ```

    or

    ```js
    arc.startAngle = startAngle;
    ```

- 端角,以度计.

  - Get

    ```js
    var endAngle = arc.endAngle;
    ```

  - Set

    ```js
    arc.seEndAngle(endAngle);
    ```

    or

    ```js
    arc.endAngle = endAngle;
    ```

- 逆时针(`true`,或`false`)

  - Get

    ```js
    var anticlockwise = arc.anticlockwise;
    ```

  - Set

    ```js
    arc.anticlockwise = anticlockwise;
    ```

#### 半径 {#radius}

- Get

  ```js
  var radius = arc.radius;
  ```

- Set

  ```js
  arc.setRadius(radius);
  ```

or

  ```js
  arc.radius = radius;
  ```

#### 较滑动弧 {#smoother-arcs}

增加此数值用于更平滑的弧, 以获得更多多边形为代价。 默认为 `0.01`

- Get

  ```js
  var iterations = arc.iterations;
  ```

- Set

  ```js
  arc.iterations = iterations;
  ```

#### 显示大小 {#display-size}

- Get

  ```js
  var width = arc.displayWidth;
  var height = arc.displayHeight;
  ```

- Set

  ```js
  arc.setDisplaySize(width, height);
  ```

  or

  ```js
  arc.displayWidth = width;
  arc.displayHeight = height;
  ```

#### 创建遮罩 {#create-mask-1}

```js
var mask = arc.createGeometryMask();
```

### 圆形 {#circle}

画圆形.

#### 创建形状对象 {#create-shape-object}

```js
var circle = this.add.circle(x, y, radius, fillColor);
// var circle = this.add.circle(x, y, radius, fillColor, fillAlpha);
```

#### 自定义类 {#custom-class-2}

- 定义类

  ```js
  class MyCircle extends Phaser.GameObjects.Arc {
    constructor(scene, x, y, radius, fillColor, fillAlpha) {
      super(scene, x, y, radius, 0, 360, false, fillColor, fillAlpha);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var circle = new MyCircle(scene, x, y, radius, fillColor, fillAlpha);
  ```

#### 颜色 {#color-1}

- 填充颜色

  - Get

    ```js
    var color = circle.fillColor;
    var alpha = circle.fillAlpha;
    ```

  - Set

    ```js
    circle.setFillStyle(color, alpha);
    ```

  - Clear

    ```js
    circle.setFillStyle();
    ```

- 划线颜色

  - Get

    ```js
    var color = circle.strokeColor;
    ```

  - Set

    ```js
    circle.setStrokeStyle(lineWidth, color, alpha);
    ```

  - Clear

    ```js
    circle.setStrokeStyle();
    ```

警告"不要用任何手段"
使用`circle.setFillStyle(color, alpha)`来改变颜色.

#### 阿尔法 {#alpha-1}

- Get

  ```js
  var alpha = circle.alpha;
  ```

- Set

  ```js
  circle.setAlpha(alpha);
  // circle.alpha = alpha;
  ```

#### 半径 {#radius-1}

- Radius

  - Get

    ```js
    var radius = circle.radius;
    ```

  - Set

    ```js
    circle.setRadius(radius);
    ```

    or

    ```js
    circle.radius = radius;
    ```

#### 较滑动弧 {#smoother-arcs-1}

增加此数值用于更平滑的弧, 以获得更多多边形为代价。 默认为 `0.01`

- Get

  ```js
  var iterations = circle.iterations;
  ```

- Set

  ```js
  circle.iterations = iterations;
  ```

#### 显示大小 {#display-size-1}

- Get

  ```js
  var width = circle.displayWidth;
  var height = circle.displayHeight;
  ```

- Set

  ```js
  circle.setDisplaySize(width, height);
  ```

  or

  ```js
  circle.displayWidth = width;
  circle.displayHeight = height;
  ```

#### 创建遮罩 {#create-mask-2}

```js
var mask = circle.createGeometryMask();
```

### 曲线 {#curve}

画一曲形.

#### 创建形状对象 {#create-shape-object-1}

```js
var curve = this.add.curve(x, y, path, fillColor);
// var curve = this.add.curve(x, y, path, fillColor, fillAlpha);
```

- `path` : [Path object](/guide/concepts/math#path).

#### 自定义类 {#custom-class-3}

- 定义类

  ```js
  class MyCurve extends Phaser.GameObjects.Curve {
    constructor(scene, x, y, path, fillColor, fillAlpha) {
      super(scene, x, y, path, fillColor, fillAlpha);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var curve = new MyCurve(scene, x, y, path, fillColor, fillAlpha);
  ```

#### 颜色 {#color-2}

- 填充颜色

  - Get

    ```js
    var color = curve.fillColor;
    var alpha = curve.fillAlpha;
    ```

  - Set

    ```js
    curve.setFillStyle(color, alpha);
    ```

  - Clear

    ```js
    curve.setFillStyle();
    ```

- 划线颜色

  - Get

    ```js
    var color = curve.strokeColor;
    ```

  - Set

    ```js
    curve.setStrokeStyle(lineWidth, color, alpha);
    ```

  - Clear

    ```js
    curve.setStrokeStyle();
    ```

警告"不要用任何手段"
使用`curve.setFillStyle(color, alpha)`来改变颜色.

#### 阿尔法 {#alpha-2}

- Get

  ```js
  var alpha = curve.alpha;
  ```

- Set

  ```js
  curve.setAlpha(alpha);
  // curve.alpha = alpha;
  ```

#### 平滑度 {#smoothness}

渲染时所用的点数。 增加此值用于更平滑的曲线, 代价是渲染更多多边形 。

```js
curve.setSmoothness(smoothness);
```

or

```js
curve.smoothness = smoothness;
```

#### 显示大小 {#display-size-2}

- Get

  ```js
  var width = curve.displayWidth;
  var height = curve.displayHeight;
  ```

- Set

  ```js
  curve.setDisplaySize(width, height);
  ```

  or

  ```js
  curve.displayWidth = width;
  curve.displayHeight = height;
  ```

#### 创建遮罩 {#create-mask-3}

```js
var mask = curve.createGeometryMask();
```

### 椭圆 {#ellipse}

画一椭圆形.

#### 创建形状对象 {#create-shape-object-2}

```js
var ellipse = this.add.ellipse(x, y, width, height, fillColor);
// var ellipse = this.add.ellipse(x, y, width, height, fillColor, fillAlpha);
```

#### 自定义类 {#custom-class-4}

- 定义类

  ```js
  class MyEllipse extends Phaser.GameObjects.Ellipse {
    constructor(scene, x, y, width, height, fillColor, fillAlpha) {
      super(scene, x, y, width, height, fillColor, fillAlpha);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var ellipse = new MyEllipse(scene, x, y, width, height, fillColor, fillAlpha);
  ```

#### 颜色 {#color-3}

- 填充颜色

  - Get

    ```js
    var color = ellipse.fillColor;
    var alpha = ellipse.fillAlpha;
    ```

  - Set

    ```js
    ellipse.setFillStyle(color, alpha);
    ```

  - Clear

    ```js
    ellipse.setFillStyle();
    ```

- 划线颜色

  - Get

    ```js
    var color = ellipse.strokeColor;
    ```

  - Set

    ```js
    ellipse.setStrokeStyle(lineWidth, color, alpha);
    ```

  - Clear

    ```js
    ellipse.setStrokeStyle();
    ```

警告"不要用任何手段"
使用`ellipse.setFillStyle(color, alpha)`来改变颜色.

#### 阿尔法 {#alpha-3}

- Get

  ```js
  var alpha = ellipse.alpha;
  ```

- Set

  ```js
  ellipse.setAlpha(alpha);
  // ellipse.alpha = alpha;
  ```

#### 大小 {#size}

- Get

  ```js
  var width = ellipse.width;
  var height = ellipse.height;
  ```

- Set

  ```js
  ellipse.setSize(width, height);
  ```

#### 显示大小 {#display-size-3}

- Get

  ```js
  var width = ellipse.displayWidth;
  var height = ellipse.displayHeight;
  ```

- Set

  ```js
  ellipse.setDisplaySize(width, height);
  ```

  or

  ```js
  ellipse.displayWidth = width;
  ellipse.displayHeight = height;
  ```

#### 平滑度 {#smoothness-1}

渲染时所用的点数。 增加此值用于更平滑的曲线, 代价是渲染更多多边形 。

```js
ellipse.setSmoothness(smoothness);
```

or

```js
ellipse.smoothness = smoothness;
```

#### 创建遮罩 {#create-mask-4}

```js
var mask = ellipse.createGeometryMask();
```

### 网格 {#grid}

画网格形状.

#### 创建形状对象 {#create-shape-object-3}

```js
var grid = this.add.grid(
  x,
  y,
  width,
  height,
  cellWidth,
  cellHeight,
  fillColor,
  fillAlpha,
  outlineFillColor,
  outlineFillAlpha
);
```

#### 自定义类 {#custom-class-5}

- 定义类

  ```js
  class MyGrid extends Phaser.GameObjects.Grid {
    constructor(
      scene,
      x,
      y,
      width,
      height,
      cellWidth,
      cellHeight,
      fillColor,
      fillAlpha,
      outlineFillColor,
      outlineFillAlpha
    ) {
      super(
        scene,
        x,
        y,
        width,
        height,
        cellWidth,
        cellHeight,
        fillColor,
        fillAlpha,
        outlineFillColor,
        outlineFillAlpha
      );
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var grid = new MyGrid(
    scene,
    x,
    y,
    width,
    height,
    cellWidth,
    cellHeight,
    fillColor,
    fillAlpha,
    outlineFillColor,
    outlineFillAlpha
  );
  ```

#### 颜色 {#color-4}

- 填充颜色

  - Get

    ```js
    var color = grid.fillColor;
    var alpha = grid.fillAlpha;
    ```

  - Set

    ```js
    grid.setFillStyle(color, alpha);
    ```

  - Clear

    ```js
    grid.setFillStyle();
    ```

- 划线颜色

  - Get

    ```js
    var color = grid.strokeColor;
    ```

  - Set

    ```js
    grid.setStrokeStyle(lineWidth, color, alpha);
    ```

  - Clear

    ```js
    grid.setStrokeStyle();
    ```

- 替换颜色

  - Get

    ```js
    var color = grid.altFillColor;
    ```

  - Set

    ```js
    grid.setAltFillStyle(color, alpha);
    ```

  - Clear

    ```js
    grid.setAltFillStyle();
    ```

- 大纲颜色

  - Get

    ```js
    var color = grid.outlineFillColor;
    ```

  - Set

    ```js
    grid.setOutlineStyle(color, alpha;
    ```

  - Clear

    ```js
    grid.setOutlineStyle();
    ```

警告"不要用任何手段"
使用`grid.setFillStyle(color, alpha)`来改变颜色.

#### 阿尔法 {#alpha-4}

- Get

  ```js
  var alpha = grid.alpha;
  ```

- Set

  ```js
  grid.setAlpha(alpha);
  // grid.alpha = alpha;
  ```

#### 显示大小 {#display-size-4}

- Get

  ```js
  var width = grid.displayWidth;
  var height = grid.displayHeight;
  ```

- Set

  ```js
  grid.setDisplaySize(width, height);
  ```

  or

  ```js
  grid.displayWidth = width;
  grid.displayHeight = height;
  ```

#### 创建遮罩 {#create-mask-5}

```js
var mask = grid.createGeometryMask();
```

### 图标 {#isobox}

IsoBox 是“ 同位素” 矩形。 每个面部的填充颜色不同。 您可以分别设置矩形的上方、左方和右方的颜色。 您也可以选择哪个面部通过 `showTop` 、 `showLeft` 和 `showRight` 属性来渲染 。

您不能从下方查看 IsoBox, 但是您可以通过设置 `projection` 属性来更改“ 角 ” 。

#### 创建形状对象 {#create-shape-object-4}

```js
var isoBox = this.add.isobox(
  x,
  y,
  width,
  height,
  fillTop,
  fillLeft,
  fillRight
);
```

#### 自定义类 {#custom-class-6}

- 定义类

  ```js
  class MyIsoBox extends Phaser.GameObjects.IsoBox {
    constructor(scene, x, y, width, height, fillTop, fillLeft, fillRight) {
      super(scene, x, y, width, height, fillTop, fillLeft, fillRight);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var isoBox = new MyIsoBox(
    scene,
    x,
    y,
    width,
    height,
    fillTop,
    fillLeft,
    fillRight
  );
  ```

#### 设定颜色 {#set-color}

- 填充颜色

  ```js
  isoBox.setFillStyle(fillTop, fillLeft, fillRight);
  ```

- 显示脸

  ```js
  isoBox.setFaces(showTop, showLeft, showRight);
  ```

  - 装上`showTop`,`showLeft`,`showRight`:设置`true`,以显示面部.

警告"不要用任何手段"
使用`isoBox.setFillStyle(fillTop, fillLeft, fillRight)`来改变颜色.

#### 阿尔法 {#alpha-5}

- Get

  ```js
  var alpha = isoBox.alpha;
  ```

- Set

  ```js
  isoBox.setAlpha(alpha);
  // isoBox.alpha = alpha;
  ```

#### 预测 {#projection}

异位框的 `projection` 级别。 更改此值以改变您查看该框的“ 角 ” 。

- Get

  ```js
  var projection = isoBox.projection;
  ```

- Set

  ```js
  isoBox.setProjection(value);
  ```

  or

  ```js
  isoBox.projection = value;
  ```

#### 显示大小 {#display-size-5}

- Get

  ```js
  var width = isoBox.displayWidth;
  var height = isoBox.displayHeight;
  ```

- Set

  ```js
  isoBox.setDisplaySize(width, height);
  ```

  or

  ```js
  isoBox.displayWidth = width;
  isoBox.displayHeight = height;
  ```

#### 创建遮罩 {#create-mask-6}

```js
var mask = isoBox.createGeometryMask();
```

### 异端调 {#isotriangle}

IsoTriangle 是“ 同位素” 三角形。 把它当金字塔一样看待。 每个面都有一个不同的填充颜色。 您可以分别设置三角形的上方、左方和右方的颜色。 您也可以选择哪个面孔通过 `showTop`、 `showLeft`和 `showRight` 属性来渲染 。

您无法从阴暗处查看 IsoTriangle, 但是您可以通过设置 `projection` 属性来更改“ 角 ” 。 如果 IsoTriangel 是否被颠倒, `reversed` 属性控制 。

#### 创建形状对象 {#create-shape-object-5}

```js
var isoTriangle = this.add.isotriangle(
  x,
  y,
  width,
  height,
  reversed,
  fillTop,
  fillLeft,
  fillRight
);
```

#### 自定义类 {#custom-class-7}

- 定义类

  ```js
  class MyIsoTriangle extends Phaser.GameObjects.IsoTriangle {
    constructor(
      scene,
      x,
      y,
      width,
      height,
      reversed,
      fillTop,
      fillLeft,
      fillRight
    ) {
      super(scene, x, y, width, height, reversed, fillTop, fillLeft, fillRight);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var isoTriangle = new MyIsoTriangle(
    scene,
    x,
    y,
    width,
    height,
    reversed,
    fillTop,
    fillLeft,
    fillRight
  );
  ```

#### 设定颜色 {#set-color-1}

- 填充颜色

  ```js
  isoTriangle.setFillStyle(fillTop, fillLeft, fillRight);
  ```

- 显示脸

  ```js
  isoTriangle.setFaces(showTop, showLeft, showRight);
  ```

  - 装上`showTop`,`showLeft`,`showRight`:设置`true`,以显示面部.

警告"不要用任何手段"
使用`isoTriangle.setFillStyle(fillTop, fillLeft, fillRight)`来改变颜色.

#### 阿尔法 {#alpha-6}

- Get

  ```js
  var alpha = isoTriangle.alpha;
  ```

- Set

  ```js
  isoTriangle.setAlpha(alpha);
  // isoTriangle.alpha = alpha;
  ```

#### 预测 {#projection-1}

异位框的 `projection` 级别。 更改此值以改变您查看该框的“ 角 ” 。

- Get

  ```js
  var projection = isoTriangle.projection;
  ```

- Set

  ```js
  isoTriangle.setProjection(value);
  ```

  or

  ```js
  isoTriangle.projection = value;
  ```

#### 反转 {#reverse}

- Get

  ```js
  var isReversed = isoTriangle.isReversed;
  ```

- Set

  ```js
  isoTriangle.setReversed(reversed);
  ```

  or

  ```js
  isoTriangle.reversed = reversed;
  ```

  - 设定`true`来颠倒.

#### 显示大小 {#display-size-6}

- Get

  ```js
  var width = isoTriangle.displayWidth;
  var height = isoTriangle.displayHeight;
  ```

- Set

  ```js
  isoTriangle.setDisplaySize(width, height);
  ```

  or

  ```js
  isoTriangle.displayWidth = width;
  isoTriangle.displayHeight = height;
  ```

#### 创建遮罩 {#create-mask-7}

```js
var mask = isoTriangle.createGeometryMask();
```

### 行线 {#line}

线形允许您在游戏中绘制两点之间的线条。 您可以控制线条的中风颜色和厚度。 在 WebGL 中, 您只能指定线条的起始和结尾的厚度, 允许您渲染线条的自启动 。

如果您需要绘制序列中的多行,您可能希望使用 [Polygon Shape](#polygon) 来代替 。

#### 创建形状对象 {#create-shape-object-6}

```js
var line = this.add.line(x, y, x1, y1, x2, y2, strokeColor);
// var line = this.add.line(x, y, x1, y1, x2, y2, strokeColor, strokeAlpha);
```

#### 自定义类 {#custom-class-8}

- 定义类

  ```js
  class MyCurve extends Phaser.GameObjects.Line {
    constructor(scene, x, y, x1, y1, x2, y2, strokeColor) {
      super(scene, x, y, x1, y1, x2, y2, strokeColor);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var line = new MyLine(scene, x, y, x1, y1, x2, y2, strokeColor);
  ```

#### 设定颜色 {#set-color-2}

- 填充颜色

  - Get

    ```js
    var color = line.fillColor;
    var alpha = line.fillAlpha;
    ```

  - Set

    ```js
    line.setFillStyle(color, alpha);
    ```

  - Clear

    ```js
    line.setFillStyle();
    ```

- 划线颜色

  - Get

    ```js
    var color = line.strokeColor;
    ```

  - Set

    ```js
    line.setStrokeStyle(lineWidth, color, alpha);
    ```

  - Clear

    ```js
    line.setStrokeStyle();
    ```

警告"不要用任何手段"
使用`line.setFillStyle(color, alpha)`来改变颜色.

#### 阿尔法 {#alpha-7}

- Get

  ```js
  var alpha = line.alpha;
  ```

- Set

  ```js
  line.setAlpha(alpha);
  // line.alpha = alpha;
  ```

#### 设置终点 {#set-end-points}

```js
line.setTo(x1, y1, x2, y2);
```

#### 行宽度 {#line-width}

```js
line.setLineWidth(startWidth, endWidth);
```

- `endWidth`:该线的尾宽,只在WebGL中使用.

#### 显示大小 {#display-size-7}

- Get

  ```js
  var width = line.displayWidth;
  var height = line.displayHeight;
  ```

- Set

  ```js
  line.setDisplaySize(width, height);
  ```

  or

  ```js
  line.displayWidth = width;
  line.displayHeight = height;
  ```

#### 创建遮罩 {#create-mask-8}

```js
var mask = line.createGeometryMask();
```

### 多边形 {#polygon}

多边形形状是通过提供点列表创建的,然后用来创建内部的多边形几何对象。这些点可以从多种格式设置:

- 包含对数值的字符串, 由单个空格分隔: `'40 0 40 20 100 20 100 80 40 80 40 100 0 50'`
- 点或矢量2对象阵列: `[new Phaser.Math.Vector2(x1, y1), ...]`
- 具有公共 x/y 属性的天体阵列: `[obj1, obj2, ...]`
- 代表点坐标的对数组: `[x1,y1, x2,y2, ...]`
- 一组阵列,其中两个元素代表x/y坐标:`[[x1, y1], [x2, y2], ...]`

默认情况下,此形状的`x`和`y`坐标是指其中心,但视所提供的点的坐标而定,最终形状可能会被其来源抵消.

注意: 如果多边形中的任何点为负值, 方法 `getBounds`z 将返回不正确的边框。 如果是, 请使用函数 `Phaser.Geom.Polygon.GetAABB(polygon.geom)` , 然后对返回的矩形位置进行相应调整 。

#### 创建形状对象 {#create-shape-object-7}

```js
var polygon = this.add.polygon(x, y, points, fillColor);
// var polygon = this.add.polygon(x, y, points, fillColor, fillAlpha);
```

- `points` :
  - 数字阵列: `[x0, y0, x1, y1, ...]`
  - 数组点数 : `[{x:x0, y:y0}, {x:x1, y:y1}, ...]`
  - 字符串: `'x0 y0 x1 y1 ...'`

!!! note
将给定的点移到位置**(0, 0) **

#### 自定义类 {#custom-class-9}

- 定义类

  ```js
  class MyPolygon extends Phaser.GameObjects.Polygon {
    constructor(scene, x, y, points, fillColor) {
      super(scene, x, y, points, fillColor);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var polygon = new MyPolygon(scene, x, y, points, fillColor);
  ```

#### 颜色 {#color-5}

- 填充颜色

  - Get

    ```js
    var color = polygon.fillColor;
    var alpha = polygon.fillAlpha;
    ```

  - Set

    ```js
    polygon.setFillStyle(color, alpha);
    ```

  - Clear

    ```js
    polygon.setFillStyle();
    ```

- 划线颜色

  - Get

    ```js
    var color = polygon.strokeColor;
    ```

  - Set

    ```js
    polygon.setStrokeStyle(lineWidth, color, alpha);
    ```

  - Clear

    ```js
    polygon.setStrokeStyle();
    ```

警告"不要用任何手段"
使用`polygon.setFillStyle(color, alpha)`来改变颜色.

#### 阿尔法 {#alpha-8}

- Get

  ```js
  var alpha = polygon.alpha;
  ```

- Set

  ```js
  polygon.setAlpha(alpha);
  // polygon.alpha = alpha;
  ```

#### 平滑 {#smooth}

使多边形在指定的迭代数上平滑。

```js
polygon.smooth(iterations);
```

#### 设定点 {#set-points}

```js
polygon.setTo(points);
```

- `point` :
  - 由单个空格分隔的包含对数的字符串 : `'40 0 40 20 100 20 100 80 40 80 40 100 0 50'`
  - 点对象数组: `[new Phaser.Point(x1, y1), ...]`
  - 具有公共 x/y 属性的天体数组: `[obj1, obj2, ...]`
  - 代表点坐标的对数组: `[x1,y1, x2,y2, ...]`
  - 一组阵列,有两个元素代表x/y坐标:`[[x1, y1], [x2, y2], ...]`

#### 显示大小 {#display-size-8}

- Get

  ```js
  var width = polygon.displayWidth;
  var height = polygon.displayHeight;
  ```

- Set

  ```js
  polygon.setDisplaySize(width, height);
  ```

  or

  ```js
  polygon.displayWidth = width;
  polygon.displayHeight = height;
  ```

#### 创建遮罩 {#create-mask-9}

```js
var mask = polygon.createGeometryMask();
```

### 矩形 {#rectangle}

画一矩形.

#### 创建形状对象 {#create-shape-object-8}

```js
var rect = this.add.rectangle(x, y, width, height, fillColor);
// var rect = this.add.rectangle(x, y, width, height, fillColor, fillAlpha);
```

#### 自定义类 {#custom-class-10}

- 定义类

  ```js
  class MyRectangle extends Phaser.GameObjects.Rectangle {
    constructor(scene, x, y, width, height, fillColor) {
      super(scene, x, y, width, height, fillColor);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var rect = new MyRectangle(scene, x, y, width, height, fillColor);
  ```

#### 颜色 {#color-6}

- 填充颜色

  - Get

    ```js
    var color = rect.fillColor;
    var alpha = rect.fillAlpha;
    ```

  - Set

    ```js
    rect.setFillStyle(color, alpha);
    ```

  - Clear

    ```js
    rect.setFillStyle();
    ```

- 划线颜色

  - Get

    ```js
    var color = rect.strokeColor;
    ```

  - Set

    ```js
    rect.setStrokeStyle(lineWidth, color, alpha);
    ```

  - Clear

    ```js
    rect.setStrokeStyle();
    ```

警告"不要用任何手段"
使用`rect.setFillStyle(color, alpha)`来改变颜色.

#### 阿尔法 {#alpha-9}

- Get

  ```js
  var alpha = rect.alpha;
  ```

- Set

  ```js
  rect.setAlpha(alpha);
  // rect.alpha = alpha;
  ```

#### 大小 {#size-1}

- Get

  ```js
  var width = rect.width;
  var height = rect.height;
  ```

- Set

  ```js
  rect.setSize(width, height);
  ```

  or

  ```js
  rect.width = width;
  rect.height = height;
  ```

#### 显示大小 {#display-size-9}

- Get

  ```js
  var width = rect.displayWidth;
  var height = rect.displayHeight;
  ```

- Set

  ```js
  rect.setDisplaySize(width, height);
  ```

  or

  ```js
  rect.displayWidth = width;
  rect.displayHeight = height;
  ```

#### 创建遮罩 {#create-mask-10}

```js
var mask = rect.createGeometryMask();
```

### 星号 {#star}

绘制星形。 您可以控制星形的几个方面, 包括构成恒星的点数。 默认值为 5, 如果您将其改为 4, 它会变成菱形 。 如果您增加它们, 你会得到一个更闪烁的恒星形状 。

您也可以控制内侧和外侧半径, 恒星的每个点是怎样的“ 长 ” 。 修改这些值以创建更有趣的形状 。

#### 创建形状对象 {#create-shape-object-9}

```js
var star = this.add.star(x, y, points, innerRadius, outerRadius, fillColor);
// var star = this.add.star(x, y, points, innerRadius, outerRadius, fillColor, fillAlpha);
```

- `points` : 恒星上的点数,默认为5.
- `innerRadius` :恒星内半径,默认值为32.
- `outerRadius` :恒星的外半径,默认为64.

#### 自定义类 {#custom-class-11}

- 定义类

  ```js
  class MyStar extends Phaser.GameObjects.Star {
    constructor(scene, x, y, points, innerRadius, outerRadius, fillColor) {
      super(scene, x, y, points, innerRadius, outerRadius, fillColor);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var star = new MyStar(
    scene,
    x,
    y,
    points,
    innerRadius,
    outerRadius,
    fillColor
  );
  ```

#### 颜色 {#color-7}

- 填充颜色

  - Get

    ```js
    var color = star.fillColor;
    var alpha = star.fillAlpha;
    ```

  - Set

    ```js
    star.setFillStyle(color, alpha);
    ```

  - Clear

    ```js
    star.setFillStyle();
    ```

- 划线颜色

  - Get

    ```js
    var color = star.strokeColor;
    ```

  - Set

    ```js
    star.setStrokeStyle(lineWidth, color, alpha);
    ```

  - Clear

    ```js
    star.setStrokeStyle();
    ```

警告"不要用任何手段"
使用`star.setFillStyle(color, alpha)`来改变颜色.

#### 阿尔法 {#alpha-10}

- Get

  ```js
  var alpha = star.alpha;
  ```

- Set

  ```js
  star.setAlpha(alpha);
  // star.alpha = alpha;
  ```

#### 半径 {#radius-2}

- 内半径

  - Get

    ```js
    var innerRadius = star.innerRadius;
    ```

  - Set

    ```js
    star.setInnerRadius(innerRadius);
    ```

    or

    ```js
    star.innerRadius = innerRadius;
    ```

- 外半径

  - Get

    ```js
    var outerRadius = star.outerRadius;
    ```

  - Set

    ```js
    star.setOuterRadius(outerRadius);
    ```

    or

    ```js
    star.outerRadius = outerRadius;
    ```

- Points

  - Get

    ```js
    var points = star.points;
    ```

  - Set

    ```js
    star.setPoints(points);
    ```

    or

    ```js
    star.points = points;
    ```

#### 显示大小 {#display-size-10}

- Get

  ```js
  var width = star.displayWidth;
  var height = star.displayHeight;
  ```

- Set

  ```js
  star.setDisplaySize(width, height);
  ```

  or

  ```js
  star.displayWidth = width;
  star.displayHeight = height;
  ```

#### 创建遮罩 {#create-mask-11}

```js
var mask = star.createGeometryMask();
```

### 三角形 {#triangle}

绘制三角形。三角形由3行组成,并列形成三角形。您可以控制这些线的每个点的位置。三角形总是封闭的,不能有张开的面孔。如果需要,请使用多边形。

#### 创建形状对象 {#create-shape-object-10}

```js
var triangle = this.add.triangle(x, y, x1, y1, x2, y2, x3, y3, fillColor);
// var triangle = this.add.triangle(x, y, x1, y1, x2, y2, x3, y3, fillColor, fillAlpha);
```

#### 自定义类 {#custom-class-12}

- 定义类

  ```js
  class MyTriangle extends Phaser.GameObjects.Triangle {
    constructor(scene, x, y, x1, y1, x2, y2, x3, y3, fillColor) {
      super(scene, x, y, x1, y1, x2, y2, x3, y3, fillColor);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var triangle = new MyTriangle(scene, x, y, x1, y1, x2, y2, x3, y3, fillColor);
  ```

#### 颜色 {#color-8}

- 填充颜色

  - Get

    ```js
    var color = triangle.fillColor;
    var alpha = triangle.fillAlpha;
    ```

  - Set

    ```js
    triangle.setFillStyle(color, alpha);
    ```

  - Clear

    ```js
    triangle.setFillStyle();
    ```

- 划线颜色

  - Get

    ```js
    var color = triangle.strokeColor;
    ```

  - Set

    ```js
    triangle.setStrokeStyle(lineWidth, color, alpha);
    ```

  - Clear

    ```js
    triangle.setStrokeStyle();
    ```

警告"不要用任何手段"
使用`triangle.setFillStyle(color, alpha)`来改变颜色.

#### 阿尔法 {#alpha-11}

- Get

  ```js
  var alpha = triangle.alpha;
  ```

- Set

  ```js
  triangle.setAlpha(alpha);
  // triangle.alpha = alpha;
  ```

#### 设置顶点 {#set-vertices}

```js
triangle.setTo(x1, y1, x2, y2, x3, y3);
```

#### 三角宽度 {#triangle-width}

```js
triangle.setLineWidth(startWidth, endWidth);
```

- `endWidth`:三角形的端宽,只在WebGL中使用.

#### 显示大小 {#display-size-11}

- Get

  ```js
  var width = triangle.displayWidth;
  var height = triangle.displayHeight;
  ```

- Set

  ```js
  triangle.setDisplaySize(width, height);
  ```

  or

  ```js
  triangle.displayWidth = width;
  triangle.displayHeight = height;
  ```

#### 创建遮罩 {#create-mask-12}

```js
var mask = triangle.createGeometryMask();
```

## 作者的信用额度 {#author-credits}

本页的内容包括下列工作:

- [RexRainbow](https://github.com/rexrainbow)

---
