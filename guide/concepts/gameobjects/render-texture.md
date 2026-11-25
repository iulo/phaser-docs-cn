# 渲染纹理 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/render-texture)

成形纹理是动态纹理和图像游戏对象的结合,使用动态纹理来显示自己.

动态纹理(Dynamic Texture)是一种特殊的纹理,它允许您直接绘制纹理,帧和最类游戏对象.

您可以带许多复杂的对象到这个纹理, 然后可以用来作为其他游戏对象, 如Sprites 的基础纹理。 如果您再更新这个纹理, 所有使用它的游戏对象都会立即更新, 立即反映变化 。

这是一种强大的方法,在运行时生成动态纹理,这种纹理是WebGL友好的,并且不会在每个变化上引用昂贵的GPU上传.

在3:60之前的Phaser版本中,一个Render纹理是唯一可以创建这样的纹理的方法,它具有被抽取的能力。但是在3:60中,我们把核心功能分割到动态纹理类,因为这使得它们更能生活在其中。因此,Render纹理现在是一个轻量级的shim,它坐在图像游戏对象的顶部,并为动态纹理中可用的特性提供代理方法。

**您何时使用质地对动态质地?**

如果纹理将被多个游戏对象使用,或者要跨多个景区使用,则应当使用动态纹理,因为纹理是全球存储的.

如果纹理不会在游戏中显示,而是会被用于像面具或遮阳器之类的东西,你应该使用动态纹理.

需要在一个游戏对象上显示纹理的纹理时,您应该使用一个Render纹理,因为它为您提供了将图像和动态纹理包裹在一起的便利.

在 WebGL1 下,一个框架缓冲器,即这个动态纹理内部使用的东西,不能被反异化。这意味着当将形状或图形等对象绘制到这个纹理时,它们可能看起来没有在边缘周围作别名。这是WebGL1的技术限制。要绕过它,在艺术包中创建你的形状,然后将它绘制到这个纹理上。

## 添加渲染纹理对象 {#add-render-texture-object}

- 创建空质感对象 。

    ```javascript
    var rt = this.add.renderTexture(x, y, width, height);
    ```

从 JSON 添加渲染纹理

```javascript
var rt = this.make.renderTexture({
    x: 0,
    y: 0,
    width: 32,
    height: 32,

    // angle: 0,
    // alpha: 1
    // flipX: true,
    // flipY: true,
    // scale : {
    //    x: 1,
    //    y: 1
    //},
    // origin: {x: 0.5, y: 0.5},

    add: true
});
```

记下奥里金的位置
    这个渲染纹理的原位是 `(0, 0)`(左上)

## 自定义类 {#custom-class}

- 定义类

    ```javascript
    class MyRenderTexture extends Phaser.GameObjects.RenderTexture {
        constructor(scene, x, y, width, height) {
            super(scene, x, y, width, height);
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
    var rt = new MyRenderTexture(scene, x, y, width, height);
    ```

## 设定大小 {#set-size}

```javascript
rt.setSize(width, height);
```

## 填充颜色 {#fill-color}

```javascript
rt.fill(rgb);
// rt.fill(rgb, alpha, x, y, width, height);
```

- `rgb`: 以数字颜色填充此动态纹理 。
- `alpha`:填充时使用的α值。默认值为`1`。
- `x`,`y`,`width`,`height`:填充矩形的区域,默认行为是填充整块大小.

## 清除 {#clear}

```javascript
rt.clear();
```

```javascript
rt.clear(x, y, width, height);
```

## 绘制游戏对象 {#draw-game-object}

```javascript
rt.draw(entries);
// rt.draw(entries,x, y);
// rt.draw(entries, x, y, alpha, tint);
```

- `entries` :
  - 任意可渲染的游戏对象,例如Sprite,Text,Graphics或TileSprite.
  - 平面图层.
  - A组,内容将依次加以修改和绘制。
  - 集装箱,内装物将按顺序完全悬挂和抽取。
  - 一个场景显示列表,通过`Scene.children`来绘制整个列表.
  - 另一种动态纹理,或称Render纹理.
  - 纹理框架实例 。
  - 字符串。 用于从纹理管理器中查找纹理 。
- `x`, `y`: 绘制框架的 x/y 位置,或对对象应用的偏移.
  - 如果物体是团体、集装箱或显示清单,则在儿童位置上加座标*。
  - 对于所有其他类型的天体,坐标是准确的.
- `alpha`,`tint`:只有纹理框架使用.
  - 游戏对象在绘制时使用自己的α和锡值.

## 擦除 {#erase}

```javascript
rt.erase(entries);
// rt.erase(entries, x, y);
```

- `entries` :
  - 任意可渲染的游戏对象,例如Sprite,Text,Graphics或TileSprite.
  - 平面图层.
  - A组,内容将依次加以修改和绘制。
  - 集装箱,内装物将按顺序完全悬挂和抽取。
  - 一个场景显示列表,通过`Scene.children`来绘制整个列表.
  - 另一种动态纹理,或称Render纹理.
  - 纹理框架实例 。
  - 字符串。 用于从纹理管理器中查找纹理 。
- `x`, `y`: 绘制框架的 x/y 位置,或对对象应用的偏移.
  - 如果物体是团体、集装箱或显示清单,则在儿童位置上加座标*。
  - 对于所有其他类型的天体,坐标是准确的.

## 绘制框架 {#draw-frame}

```javascript
rt.stamp(key, frame, x, y, {
    alpha: 1,
    tint: 0xffffff,
    angle: 0,
    rotation: 0,
    scale: 1,
    scaleX: 1,
    scaleY: 1,
    originX: 0.5,
    originY: 0.5,
    blendMode: 0,
    erase: false,
    skipBatch: false
})
```

or

```javascript
rt.drawFrame(key, frame, x, y);
// rt.drawFrame(key, frame, x, y, alpha, tint);
```

- `x`, `y` : 左上方位置

## 绘制重复框架 {#draw-repeat-frames}

- 重复装满大小的帧

    ```javascript
    rt.repeat(key, frame);
    ```

- 在区域中重复

    ```javascript
    rt.repeat(key, frame, x, y, width, height);
    // rt.repeat(key, frame, x, y, width, height, alpha, tint, skipBatch);
    ```

## 批量绘图 {#batch-draw}

1. Begin

    ```javascript
    rt.beginDraw();
    ```

2. Draw
    - 绘制游戏对象

        ```javascript
        rt.batchDraw(entries, x, y, alpha, tint);
        ```

        - `entries` :
            - 任意可渲染的游戏对象,例如Sprite,Text,Graphics或TileSprite.
            - 平面图层.
            - A组,内容将依次加以修改和绘制。
            - 集装箱,内装物将按顺序完全悬挂和抽取。
            - 一个场景显示列表,通过`Scene.children`来绘制整个列表.
            - 另一种动态纹理,或称Render纹理.
            - 纹理框架实例 。
            - 字符串。 用于从纹理管理器中查找纹理 。
    - 绘制框架

        ```javascript
        rt.batchDrawFrame(key, frame, x, y, alpha, tint);
        ```

    - 绘制图像

        ```javascript
        rt.stamp(key, frame, x, y, {
            // ...
            skipBatch: true
        })
        ```

    - 绘制重复图像

        ```javascript
        rt.repeat(key, frame, x, y, width, height, alpha, tint, true);
        ```

3. End

    ```javascript
    rt.endDraw();
    ```

## 内部相机 {#internal-camera}

内部相机 `rt.camera`

- 滚动( 抵销)

    ```javascript
    rt.camera.setScroll(x, y);
    ```

- 缩放( 缩放)

    ```javascript
    rt.camera.setZoom(zoom);
    ```

- Rotate

    ```javascript
    rt.camera.setAngle(angle);  // angle in degrees
    ```

## 抓图 {#snapshot}

### 抓图区域 {#snapshot-area}

```javascript
texture.snapshot(callback);
// texture.snapshot(callback, type, encoderOptions);
```

or

```javascript
texture.snapshotArea(x, y, width, height, callback, type, encoderOptions);
```

- `callback`:在快照图像创建后要引用的函数 。

    ```javascript
    function(imageElement) {
    }
    ```

  - `imageElement` : HTML ImageElement. 维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维尔日报-维尔日报-维尔德·维尔曼.
- `type`:图像创建的格式,通常为`'image/png'`或`'image/jpeg'`. 默认值为`'image/png'`.
- `encoderOptions`: 图像质量,介于`0`和`1`之间,用于图像格式,具有失压缩,如`'image/jpeg'`,默认值为`0.92`.
- `x`, `y`, `width`, `height` :快照区。

### 获取像素的颜色 {#get-color-of-a-pixel}

```javascript
texture.snapshotPixel(x, y, callback);
```

- `x`,`y`:像素的x/y坐标来得到.
- `callback`:在快照图像创建后要引用的函数 。

    ```javascript
    function(color) {        
    }
    ```

  - `color` : 彩色对象.

## 全球阿尔法 {#global-alpha}

```javascript
rt.setGlobalAlpha(alpha);
// rt.globalAlpha = alpha;
```

## 全球锡 {#global-tint}

```javascript
rt.setGlobalTint(tint);
// rt.globalTint = tint;
```

## 保存纹理 {#save-texture}

使用给定的密钥在纹理管理器中存储此纹理的复制件 。

```javascript
rt.saveTexture(key);
```

再一次调用 `saveTexture` 将无法保存同一纹理的另一副本, 它只会重命名现有副本的密钥 。

## 其他属性 {#other-properties}

见[game object](/guide/concepts/gameobjects)

## 创建遮罩 {#create-mask}

```javascript
var mask = rt.createBitmapMask();
```

见[mask](/guide/concepts/display#masks)

## 阴影效果 {#shader-effects}

支持 [preFX and postFX effects](/guide/concepts/gameobjects/shader) 软件

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
