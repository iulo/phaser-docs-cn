# 缩放管理器 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/scale-manager)

缩放游戏窗口,内置的Phaser方法.

## 设置 {#setup}

[game configuration](/guide/concepts/game)中的设置比例模式.

```javascript
var config = {
    // ...
    parent: divId,

    // Game size
    width: 1024,
    height: 768,

    scale: {
        // Or set parent divId here
        parent: divId,

        mode: Phaser.Scale.FIT,
        autoCenter: Phaser.Scale.CENTER_BOTH,

        // Or put game size here
        // width: 1024,
        // height: 768,

        // Minimum size
        min: {
            width: 800,
            height: 600
        },
        // Or set minimum size like these
        // minWidth: 800,
        // minHeight: 600,

        // Maximum size
        max: {
            width: 1600,
            height: 1200
        },
        // Or set maximum size like these
        // maxWidth: 1600,
        // maxHeight: 1200,

        zoom: 1,  // Size of game canvas = game size * zoom
    },
    autoRound: false
    // ...
};
var game = new Phaser.Game(config);
```

- `scale.mode` :
  - `Phaser.Scale.NONE` : 完全没有缩放。
  - `Phaser.Scale.FIT` : 宽度和高度会自动调整, 以适应给定目标区域, 同时保持宽度比。 根据宽度比, 区域内可能有一些空间没有覆盖 。
  - `Phaser.Scale.ENVELOP`: 宽度和高度会自动调整, 使大小覆盖整个目标区域, 同时保持宽度比。 这可能会比目标大小更远 。
  - `Phaser.Scale.WIDTH_CONTROLS_HEIGHT`:高度根据宽度自动调整.
  - `Phaser.Scale.HEIGHT_CONTROLS_WIDTH`:宽度根据高度自动调整.
  - `Phaser.Scale.EXPAND`:Canvas的可见区域被调整大小,以适应所有可用的母空间,如RESIZE模式,以及比例帆布大小以适应像FIT模式一样的可见区域内部.
  - `Phaser.Scale.RESIZE`: 坎瓦的大小被调整,以适应所有可用的_parent_空间,无论宽度比.
- `scale.autoCenter` :
  - `Phaser.Scale.NO_CENTER`:游戏画布不是以Phaser为中心在母体内部.
  - `Phaser.Scale.CENTER_BOTH`:游戏画布在母体内部横向和纵向都以中心为中心.
  - `Phaser.Scale.CENTER_HORIZONTALLY`:游戏画布在母体内部水平中心.
  - `Phaser.Scale.CENTER_VERTICALLY`:游戏画布在母体内部垂直地双向中心.

## 调整画布元素大小 {#resize-canvas-element}

```javascript
scene.scale.resize(width, height);
```

直接修改 Phaser 画布元素的大小。 您只应在使用 `NO_SCALE` 比例模式时使用此功能,

## 设定游戏大小 {#set-game-size}

```javascript
scene.scale.setGameSize(width, height);
```

它只应用于您想要改变游戏的基数大小,并且正在使用一个缩放管理器缩放模式,即`FIT`. 如果您使用`NO_SCALE`并想要直接改变游戏和画布大小,那么请使用`resize`方法代替.

## 获取视图端口 {#get-view-port}

```javascript
var viewport = scene.scale.getViewPort();
// var viewport = scene.scale.getViewPort(camera, out);
```

- `viewport` : 数据 [Rectangle](/guide/concepts/geometry#rectangle) 可见区域。
- `camera` : 数据 [camera](/guide/concepts/cameras) 视门已响应 。
- `out` : 数据 [Rectangle](/guide/concepts/geometry#rectangle) 可见区域。

## 成员 {#members}

- 未修改的游戏大小, 如游戏配置( 原始宽度 / 高度) 中要求的, 如用于世界界限, 相机等

    ```javascript
    var gameSize = scene.scale.gameSize;
    ```

  - `gameSize.width`, `gameSize.height`
- 修改后的游戏大小,即自动圆形的gameSize,用于设置画布宽度和高度(但不是CSS风格).

    ```javascript
    var baseSize = scene.scale.baseSize;
    ```

  - `baseSize.width`, `baseSize.height`
- 画布样式所用的大小,在比例模式,父值和其他值中作为因素.

    ```javascript
    var displaySize = scene.scale.displaySize;
    ```

  - `displaySize.width`, `displaySize.height`
- 父多姆元素的大小

    ```javascript
    var parentSize = scene.scale.parentSize;
    ```

  - `parentSize.width`, `parentSize.height`

## 事件 {#events}

```javascript
scene.scale.on('resize', function(gameSize, baseSize, displaySize, previousWidth, previousHeight) {});
```

- `gameSize`:未修改的游戏大小,按照游戏配置中的要求(原始宽度/高度)
  - `gameSize.width`, `gameSize.height`
- `baseSize`:画布宽度和高度(画布的实际大小)
  - `baseSize.width`, `baseSize.height`
- `displaySize`:画布样式所用的大小(画布的显示大小)
  - `displaySize.width`, `displaySize.height`

## 更新界限 {#update-bounds}

无需使用这种方法剂量,除非布布位置,或通过任何其他方法(即通过角线)改变可见度。

```javascript
scene.scale.updateBounds();
```

## 全屏 {#full-screen}

在`'pointerup'`触摸活动下:

- 开始全屏

    ```javascript
    scene.scale.startFullscreen();
    ```

- 停止全屏显示

    ```javascript
    scene.scale.stopFullscreen();
    ```

- 切换全屏

    ```javascript
    scene.scale.toggleFullscreen();
    ```

- 屏幕全显示

    ```javascript
    var isFullscreen = scene.scale.isFullscreen;
    ```

iframe 内的游戏也会被屏蔽到全屏
除非iframe有`allowfullscreen`属性.

执行一个可导航到另一页的动作,
或打开另一个标签,将自动取消全屏模式,
用户按 ESC 键时也会这样做。

### 事件 {#events-1}

- 输入全屏

    ```javascript
    scene.scale.on('enterfullscreen', function() {}, scope);
    ```

- 输入全屏失败

    ```javascript
    scene.scale.on('fullscreenfailed', function(error) {}, scope);
    ```

- 离开全屏

    ```javascript
    scene.scale.on('leavefullscreen', function() {}, scope);
    ```

- 完全屏幕不支持

    ```javascript
    scene.scale.on('fullscreenunsupported', function() {}, scope);
    ```

- 离开全屏

    ```javascript
    scene.scale.on('leavefullscreen', function() {}, scope);
    ```

## 方向 {#orientation}

### 属性 {#properties}

- 画像取向

    ```javascript
    var isPortrait = scene.scale.isPortrait;
    ```

- 风景取向

    ```javascript
    var isLandscape = scene.scale.isLandscape;
    ```

### 锁定方向 {#lock-orientation}

```javascript
scene.scale.lockOrientation(orientation);
```

- `orientation` : `'landscape'`,或 ,或 , `'portrait'`;

### 事件 {#events-2}

```javascript
scene.scale.on('orientationchange', function(orientation) {
    if (orientation === Phaser.Scale.PORTRAIT) {

    } else if (orientation === Phaser.Scale.LANDSCAPE) {

    }
}, scope);
```

## 作者的信用额度 {#author-credits}

本页的内容包括下列工作:

- [RexRainbow](https://github.com/rexrainbow)

---
