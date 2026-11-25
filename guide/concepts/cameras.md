# 摄像机 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/cameras)

Phaser有一个内置的摄像机系统。 摄像机是控制您当前所看到的游戏世界的哪一部分的一种方法。 您可以将摄像机移动到世界各地, 而这反过来会影响游戏对象的显示, 以它们的世界位置为基础。 默认情况下, 摄像机会创建一个单一的摄像机供您使用。 它必须至少拥有一个摄像机, 否则将没有任何东西可以渲染 。

您可以随意添加更多摄像机。 您也可以控制每个摄像机的位置、 大小、 旋转、 缩放和视图。 能够多摄像机的常用方法是创建分屏游戏, 或者具有图片效果的游戏。

摄像机也可以被赋予一个界限。 这是摄像机无法在外侧滚动的矩形区域。 默认情况下, 摄像机没有界限, 所以可以随便在任何地方滚动。 然而, 在实际操作中, 您可能需要将摄像机限制在游戏世界的固定区域, 而摄像机的边界就是您如何这样做的 。

## 摄像机基础 {#camera-basics}

![Four cameras showing a giant robot](https://labs.phaser.io/screenshots/camera/cameras%20from%20state%20config.png)

摄像机显示游戏对象在场景中。 您从场景摄像机管理器 `this.cameras` 创建或访问它们。 默认每个场景都有一台摄像机 。

### 获取主摄像机 {#get-the-main-camera}

  ```js
  var camera = this.cameras.main;
  ```

  or

  ```js
  var camera = this.cameras.cameras[0];
  ```

### 按名称获取摄像机 {#get-camera-by-name}

  ```js
  var camera = this.cameras.getCamera(name);
  ```

### 添加摄像机 {#add-new-camera}

  ```js
  var camera = this.cameras.add();
  // var camera = this.cameras.add(x, y, width, height);
  ```

### 添加具名摄像机 {#add-new-camera-with-name}

  ```js
  var camera = this.cameras.add(
    undefined,
    undefined,
    undefined,
    undefined,
    false,
    name
  );
  // var camera = this.cameras.add(x, y, width, height, makeMain, name);
  ```

### 添加已有摄像机 {#add-existing-camera}

  ```js
  this.cameras.addExisting(camera);
  ```

### 从 JSON 创建摄像机 {#create-cameras-from-json}

  ```js
  this.cameras.fromJSON(config);
  // this.cameras.fromJSON(configArray);
  ```

### 相机`config`: 相机: {#camera-config}

  ```js
  {
      name: '',
      x: 0,
      y: 0,
      width: scene.sys.scale.width,
      height: scene.sys.scale.height,
      zoom: 1,
      rotation: 0,
      scrollX: 0,
      scrollY: 0,
      roundPixels: false,
      visible: true,
      backgroundColor: false,
      bounds: null, // {x, y, width, height}
  }
  ```

### 移除摄像机 {#remove-a-camera}

  ```js
  this.cameras.remove(camera);
  ```

### 销毁摄像机 {#destroy-a-camera}

  ```js
  camera.destroy();
  ```

如果你创建多个摄像机,那么 `main` 被一些选项用作默认值 Phaser 用于接受摄像机参数的函数。您可以指定任何摄像机为主。

`this.cameras.default`是代表摄像机默认状态(不调整大小或转换)的非还原摄像机.

每次拍摄开始时都会重新制作镜头,所以不要保留任何参考.

摄像机有两个不同的坐标空间,它的**viewport**和**worldview**.

| 视口  | 世界观                            |
| --------- | ------------------------------------- |
| `x`       | `worldView.x` 或 或 时 间 `worldView.left`     |
| `y`       | `worldView.y` 或 或 时 间 `worldView.top`      |
| `width`   | `displayWidth` 或 或 时 间 `worldView.width`   |
| `height`  | `displayHeight` 或 或 时 间 `worldView.height` |
| `centerX` | `midPoint.x` 或 或 时 间 `worldView.centerX`   |
| `centerY` | `midPoint.y` 或 或 时 间 `worldView.centerY`   |

## 视口 {#viewport}

摄像机 `viewport` 表示其“窗口”或游戏画布上的可见区域。 `x` (左边) `y` (顶部) `width`, `height`, `centerX`, `centerY`, `setSize()`,和 `setViewport()` 默认情况下,摄像机的视门与游戏的视门完全相同,即:

`{ x: 0, y: 0, width: this.scale.width, height: this.scale.height }`

### 用法 {#usage}

- 获取摄像机位置

  - Top-left

    ```js
    var top = camera.x;
    var left = camera.y;
    ```

  - 中,相对于游戏画布左上角.

    ```js
    var x = camera.centerX;
    var y = camera.centerY;
    ```

- 获取摄像机大小( 宽度和高度) (H)

  ```js
  var width = camera.width;
  var height = camera.height;
  ```

  ```js
  var displayWidth = camera.displayWidth;
  var displayHeight = camera.displayHeight;
  ```

- 设定摄像机视图

  ```js
  camera.setViewport(top, left, width, height);
  ```

- 设定摄像机位置

  ```js
  camera.setPosition(top, left);
  // camera.x = top;
  // camera.y = left;
  ```

- 设定摄像机大小

  ```js
  camera.setSize(width, height);
  // camera.width = width;
  // camera.height = height;
  ```

## 世界坐标中的可视范围 {#world-view}

摄像机`worldView`是它可以"看见"的游戏世界的区域,基于它的卷轴,旋转,缩放,在游戏世界坐标上. Z`midPoint`,`displayWidth`,和`displayHeight`参考了这个景区.

`midPoint`和`worldView`在第一次场景渲染后仅更新 ** **。如果需要更早使用,请使用

```js
function create() {
  // …
  this.cameras.main.preRender();
}
```

如果你从不滚动、放大或旋转摄像机,那么其世界观与其视门完全相同。

### 用法 {#usage-1}

- 世界观,一个[rectangle object](/guide/concepts/geometry#rectangle)

  ```js
  var worldView = camera.worldView;
  var x = worldView.x;
  var y = worldView.y;
  var width = worldView.width; // displayWidth
  var height = worldView.height; // displayHeight
  var left = worldView.left; // x
  var right = worldView.right; // x + width
  var top = worldView.top; // y
  var bottom = worldView.bottom; // y + height
  var centerX = worldView.centerX;
  var centerY = worldView.centerY;
  var isInside = worldView.contains(x, y);
  var randPoint = worldView.getRandomPoint(point); // point: {x, y}
  ```

- 获取中间点

  ```js
  var x = camera.midPoint.x;
  var y = camera.midPoint.y;
  ```

- 获得世界位置

  ```js
  var out = camera.getWorldPoint(x, y);
  // var out = camera.getWorldPoint(x, y, out);
  ```

  - `x` , `y` : 摄像机位置。
  - `out` : 世界立场 `{x, y}`

## 可见性与输入 {#visibility-input}

可见的摄像机会渲染并响应指针输入,除非将摄像机的`inputEnabled`设置为`false`.

隐形摄像机不会渲染任何东西,会跳过输入测试.

### 用法 {#usage-2}

- 获取摄像机可见度

  ```js
  var visible = camera.visible;
  ```

- 设定摄像机可见度

  ```js
  camera.setVisible(value);
  // camera.visible = value
  ```

## 渲染 {#rendering}

您可以更改每台摄像机的 `roundPixels` 属性。 默认它与游戏配置中设定的值相同, 或是 `false` 。

`startFollow()`还默认将摄像机的`roundPixels`属性设置为`false`,除非提供`roundPixels`的参数.

设置 `roundPixels` 到 `true`, 使摄像机在渲染游戏对象时圆像素值为整整数, 在某些类型的游戏中, 特别是用像素艺术, 需要这样做来防止子像素的异名 。

### 像素坐标取整 {#round-pixels-usage}

- 拿摄像机来`roundPixels`

  ```js
  var roundPixels = camera.roundPixels;
  ```

- 设定摄像机 `roundPixels`

  ```js
  camera.setRoundPixels(value);
  // camera.roundPixels = value
  ```

### 设置背景颜色 {#set-background-color}

使用此选项设置摄像机的默认背景颜色 。

```js
camera.setBackgroundColor(color);
```

### 忽略游戏对象 {#ignoring-game-objects}

摄像机不会渲染指定的游戏对象 。

```js
camera.ignore(gameObject);
```

- `gameObject` :
  - 游戏对象
  - 游戏对象阵列
  - 一个团体

## 效果 {#effects}

摄像机已定时了 ** fade **, ** flash **, **pan **, **rotate **, **shake **, 和 **zoom ** 效果。 请参看方法的细节。 大多数方法不会中断持续效果,除非您通过 。 `force = true`。您可以重设一个给定的效果,例如, `fadeEffect.reset()` 或 或 时 间 `flashEffect.reset()`。您可以监测持续效应,例如, `fadeEffect.isRunning`, `fadeEffect.progress`等 类.

每当更新时你都不应该启动摄像机效果。 `centerOn()`, `setRotation()`, `setZoom()` 换成是的

`fadeOut()`通常与`fadeIn()`对称.

您可以在摄像机上通过调用或注册事件处理器(通常使用`once()`),以在事件完成时采取行动.

你可以通过调用镜头的`resetFX()`方法来重置所有效果.

您也可以调色一些摄像机属性( Name`alpha`, `rotation`, `scrollX`, `scrollY`, `zoom`)自己而不是使用效果.

### 不透明度（Alpha） {#alpha}

摄像机的α值会撞击摄像机制作的每个物体。您可以直接设定属性,即通过Tween来淡出摄像机,也可以通过可链式setAlpha方法来淡出。

#### 用法 {#usage-3}

- 获取摄像机 alpha

  ```js
  var alpha = camera.alpha;
  ```

- 设定摄像机 alpha

  ```js
  camera.setAlpha(value);
  // camera.alpha = value;
  ```

### 旋转 {#rotation}

摄像机旋转总是根据摄像机的视门进行。默认情况下,旋转发生在`viewport`的中心。您可以根据`originX`和`originY`的属性来调整此功能。

旋转会影响此摄像机所可见的所有游戏对象的渲染。 然而, 它不会旋转摄像机的视门本身, 它始终是一个轴向的矩形 。

#### 用法 {#usage-4}

- 获得摄像机旋转

  ```js
  var angle = camera.rotation; // angle in radians
  ```

- 设定摄像机旋转

  ```js
  camera.setAngle(angle); // angle in degree
  camera.setRotation(angle); // angle in radians
  camera.rotation = angle; // angle in radians
  ```

### 原点 {#origin}

更改源头允许您调整旋转所在的视口。设置 `x` 财务报告和已审计财务报表 `y` 以 0 旋转从视图端左上角的摄像机。设置 `x` 财务报告和已审计财务报表 `y` 以1从右下角旋转摄像机。

#### 用法 {#usage-5}

- 获取摄像机来源

  ```js
  var originX = camera.originX;
  var originY = camera.originY;
  ```

- 设定摄像机来源

  ```js
  camera.setOrigin(x, y);
  // camera.originX = 0.5;
  // camera.originY = 0.5;
  ```

### 滚动 {#scrolling}

`scrollX`,`scrollY`是摄像机滚动坐标,其中(0,0)是初始滚动位置,它们代表摄像机世界观及其视门的左上角之间的距离,因此增加`scrollX`和`scrollY`将摄像机视图向下移动,向上或向上移动,视您视角而定,向上或向左移动游戏世界对象.

`setScroll(x, y)`直接设置了`scrollX`和`scrollY`.

`centerOn(x, y)`和`pan(x, y)`也滚动了摄像机,但他们的论据指的是摄像机的`midPoint`,所以它们常常是一个比较自然的选择.

卷轴坐标为无分解.

#### 用法 {#usage-6}

- 将摄像机滚动到 x, Y 位置

  ```js
  camera.scrollX = scrollX;
  camera.scrollY = scrollY;
  ```

  or

  ```js
  camera.setScroll(x, y);
  ```

- 将摄像机移动到摄像机边界中心

  ```js
  camera.centerToBounds();
  ```

- 将摄像机中心到 x, y 位置

  ```js
  camera.centerOn(x, y); // centered on the given coordinates
  ```

  or

  ```js
  camera.centerOnX(x);
  camera.centerOnY(y);
  ```

- 中央摄像机根据视网膜大小。

  ```js
  camera.centerToSize();
  ```

### 跟踪游戏对象 {#follow-game-object}

设定摄像机以跟随游戏对象。

`camera.startFollow(target, roundPixels, lerpX, lerpY, offsetX, offsetY)`

`target`可以是游戏对象或类似点的物体.

摄像机滚动自动将目标保留在视点中心. 可选的`lerpX`和`lerpY`参数通过插两个位置来平滑运动.

摄像机死区(如果设置)是后续目标可以移动(相对于视点)而不滚动摄像机的区域,死区总是以后续目标为中心,在世界坐标中.

#### 用法 {#usage-7}

- 开始跟着

  ```js
  camera.startFollow(gameObject);
  // camera.startFollow(gameObject, roundPx, lerpX, lerpY, offsetX, offsetY);  //
  ```

  - `roundPx` : 将摄像机位置的正圆设置为整数
  - `lerpX`, `lerpY` : 0 至 1 之间的数值。
    - `1` 摄像机会立刻向目标坐标方向响起
    - `0.1` :摄像机会更缓慢地跟踪目标,给出平稳的过渡.
  - `offsetX`,`offsetY`:摄像机的横向/垂直偏移跟随目标.x位置.

- 别跟着我

  ```js
  camera.stopFollow();
  ```

- 设置后继位置

  ```js
  camera.setFollowOffset(x, y);
  ```

- 设置麻风

  ```js
  camera.setLerp(x, y);
  ```

  - `1` 摄像机会立刻向目标坐标方向响起
  - `0.1` :摄像机会更缓慢地跟踪目标,给出平稳的过渡.

- Deadzone

  ```js
  camera.setDeadzone(width, height);
  ```

  如果目标移动到这个区域之外,摄像机会开始滚动,以便跟随它.

  - Boundaries

    ```js
    var left = camera.deadzone.left;
    var right = camera.deadzone.right;
    var top = camera.deadzone.top;
    var bootom = camera.deadzone.bottom;
    ```

  - 清除死区

    ```js
    camera.setDeadzone();
    ```

#### 事件 {#events}

- 跟踪者更新

  ```js
  camera.on("followupdate", function (camera, gameObject) {});
  ```

### 边界 {#bounds}

设定摄像机的界限。 界限是一个轴向矩形 。

摄像机将控制摄像机可以滚动到哪些地方,阻止其从边缘滚动到空白空间,并不限制游戏对象的放置,也不限制摄像机视门的位置.

暂时关闭界限 通过改变布尔`Camera.useBounds`。

完全清除界限,叫`Camera.removeBounds`。

如果您设定的界限比视图小, 它会阻止摄像机滚动。 边界可以放在任何您想要的地方。 默认它们从0x0 到画布宽度x高度。 这意味着0x0 是摄像机界限的左上方。 但是, 您可以将其定位到任何地方。 因此, 如果您想要一个大小为2048x2048, 以0x0为中心, 您可以设定 x/y为 - 1024, 以宽度和高度为2048 。 取决于您的游戏, 您可以发现 0x0 更容易成为界限的左上方, 或者您希望 0x0 成为中间方 。

#### 用法 {#usage-8}

- 获取摄像机界限

  ```js
  var bounds = camera.getBounds(); // bounds: a rectangle object
  // var out = camera.getBounds(out);
  ```

- 设定摄像机界限

  ```js
  camera.setBounds(x, y, width, height);
  ```

### 缩放 {#zoom}

摄像机可以放大或变形成场。

0.5 的数值可以放大摄像机, 显示摄像机的两倍。 2 的数值可以放大摄像机, 所以现在每个像素在渲染时都占2 像素。

设定为 1 以返回默认缩放级别 。

注意永远不要将这个值设置为零.

#### 用法 {#usage-9}

- 放大镜头

  ```js
  var zoomValue = camera.zoom;
  ```

- 设定摄像机缩放

  ```js
  camera.setZoom(zoomValue); // The minimum it can be is 0.001.
  camera.zoom = zoomValue;
  ```

## 其他特征 {#other-features}

### 获取指针所在位置的摄像机 {#get-cameras-below-pointer}

返回给定指针下方的所有摄像机阵列。

阵列中的第一个镜头是镜头列表中最顶尖的镜头.

- 将所有摄像机都放在指针下

```js
var cameras = this.cameras.getCamerasBelowPointer(pointer);
```

- `cameras` : 一系列摄像机。
- `pointer` : `{x, y}`

### 子对象 {#children}

取出一系列游戏对象和一个摄像机,返回一个只包含那些通过willRender测试的游戏对象的新阵列,以对抗给定的摄像机.

#### 可见的子对象 {#visible-children}

- 过滤可见子

  ```js
  var visible = this.cameras.getVisibleChildren(children, camera);
  ```

- 带所有可见的孩子

  ```js
  var visible = this.cameras.getVisibleChildren(
    scene.sys.displayList.list,
    camera
  );
  ```

#### 渲染子对象 {#render-children}

此阵列包含此摄像机在上一个(或当前,取决于您检查时)帧中提供的所有游戏对象.

摄像机开始时就清除了 preUpdate 或者摄像机被摧毁了

- 来点鸡尾酒
  
  ```js
  var children = camera.renderList;
  ```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)
- [samme](https://github.com/samme)

---
