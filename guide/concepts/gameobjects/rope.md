# 绳索 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/rope)

绳形对象仅为_WebGL_,没有Canvas对应的.

绳子(英语:A Rope)是一类特殊的游戏对象,其纹理沿其整个长度伸展.

与“飞毛腿”不同,它不仅限于使用一个四角,而且可以在创建时定义的顶点数量相同。顶点可以排列在横向或纵向的条形上,并具有自己的颜色和α值。

绳子源头总是0.5×0.5,不能更改.

## 装入纹理 {#load-texture}

```javascript
this.load.image(key, url);
```

参考文献: [load image](/guide/concepts/loader#image)

## 添加对象 {#add-object}

```javascript
var rope = this.add.rope(x, y, texture, frame, points, horizontal);
// var rope = this.add.rope(x, y, texture, frame, points, horizontal, colors, alphas);
```

- `points` :
  - 数字:将纹理框架分割成的片段。
  - 数字数组:包含顶点数据的数组。
- `horizontal` :
  - `true` : 此绳索的垂直对齐 。
  - `false` : 此绳的垂直对齐 。
- `colors` : 包含此绳索颜色数据的可选阵列。 每对顶点有一个颜色值 。
- `alphas`: 包含此绳索的α数据的可选数组。 每对顶点有一个α值 。

从 JSON 添加绳索

```javascript
var rope = this.make.rope({
    x: 0,
    y: 0,
    key: '',
    frame: null,
    horizontal: true,
    points: undefined,
    colors: undefined,
    alphas: undefined,

    // angle: 0,
    // alpha: 1
    // flipX: true,
    // flipY: true,
    // origin: {x: 0.5, y: 0.5},
    
    add: true
});
```

## 自定义绳子类 {#custom-rope-class}

- 定义类

    ```javascript
    class MyRope extends Phaser.GameObjects.Rope {
        constructor(scene, x, y, texture, frame, points, horizontal, colors, alphas) {
            super(scene, x, y, texture, frame, points, horizontal, colors, alphas);
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

    ```javascript
    var rope = new MyRope(scene, x, y, texture, frame, points, horizontal);
    ```

## 来源 {#origin}

绳子源头总是0.5×0.5,不能更改.

## 设置顶点 {#set-vertices}

通过设置顶点

```javascript
rope.setPoints(points);
// rope.setPoints(points, colors, alphas);
```

- `points` :
  - 数字:将纹理框架分割成的片段。
  - 数字数组:包含顶点数据的数组。
- `colors` : 包含此绳索颜色数据的可选阵列。 每对顶点有一个颜色值 。
- `alphas`: 包含此绳索的α数据的可选数组。 每对顶点有一个α值 。

也改变水平模式 :

- 将垂直绳改为水平绳, 如果绳子已经是水平模式, 则不做任何动作

    ```javascript
    rope.setHorizontal(points);
    // rope.setHorizontal(points, colors, alphas);
    ```

- 将水平绳改为垂直绳, 如果绳子已经是垂直模式, 则不做任何动作

    ```javascript
    rope.setVertical(points);
    // rope.setVertical(points, colors, alphas);
    ```

或者直接设置`rope.points`:

1. 更改 `rope.points`
    - 水平绳: `rope.points[i].y = newY`
    - 垂直绳: `rope.points[i].x = newX`
1. 呼叫`rope.setDirty()`,或`rope.updateVertices()`

每一点相对于绳索物体的位置,通过

```javascript
var worldX = rope.points[i].x + rope.x;
var worldY = rope.points[i].y + rope.y;
```

## 播放动画 {#play-animation}

```javascript
rope.play(key);
// rope.play(key, ignoreIfPlaying, startFrame);
```

- `ignoreIfPlaying`: 如果动画已经播放, 请忽略此调。 默认值为 `false` 。
- `startFrame`:可选地从此帧索引开始播放动画。默认值为`0`。

## 阿尔法 {#alpha}

- 单字母

    ```javascript
    rope.setAlphas(alpha);
    ```

- 上 - 下方的字母

    ```javascript
    rope.setAlphas(topAlpha, bottomAlpha);
    ```

- 每个点的阿尔法阵列

    ```javascript
    rope.setAlphas(alphaArray);
    ```

  - `alphaArray` : 阿尔法值的矩阵。

## 颜色颜色颜色 {#color-tint}

- 单色色色点

    ```javascript
    rope.setColors(color);
    ```

- 每个点的颜色线性数组

    ```javascript
    rope.setAlphas(colorArray);
    ```

  - `colorArray` : 颜色锡值的矩阵。

### 丁补模式 {#tint-fill-mode}

设置锡装模式。

```javascript
rope.setTintFill(mode);
```

- `mode` :
  - `0` : 添加锡,将顶点颜色与纹理混合。默认行为 。
  - `1` :用α填充锡.
  - `2` : 填充无α.

## 翻转 {#flip}

```javascript
rope.flipX = flip;
rope.flipY = flip;
```

如果此游戏对象有物理体, 它不会改变身体。 这只是一个渲染切换 。

## 调试 {#debug}

绘制调试网格每个渲染勾选符 。

```javascript
rope.setDebug(graphic);
// rope.setDebug(graphic, callback);
```

- `graphic` : [Graphics game object](/guide/concepts/gameobjects/graphics)
- `callback` : 调试图形的调试( C)[default callback](https://github.com/photonstorm/phaser/blob/master/src/gameobjects/rope/Rope.js#L996-L1024))

    ```javascript
    function(rope, meshLength, verts) {
        // var graphic = rope.debugGraphic;
    }
    ```

  - `rope` :绳子实例。
    - `rope.debugGraphic` : [Graphics game object](/guide/concepts/gameobjects/graphics)
  - `meshLength` :网状顶点总数.
  - `verts`:一个翻译的顶点坐标阵列.

!!! note
    清除调试图形( E)`rope.debugGraphic.clear()`),在现场更新阶段("  ").`this.update() { }`)

## 作者的信用额度 {#author-credits}

本页的内容包括下列工作:

- [RexRainbow](https://github.com/rexrainbow)

---
