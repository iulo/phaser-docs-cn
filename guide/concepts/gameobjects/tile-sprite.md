# 平铺精灵 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/tile-sprite)

纹理(TileSprite)是一种具有重复纹理的螺旋体.

纹理可以独立于TileSprite本身进行滚动和缩放,纹理会自动包扎,设计上可以让您以无缝纹理作为源头创建游戏背景.

您不应该创建比实际画布大小更大的 TileSprite 。 如果您想要创建一个大背景, 滚动整个游戏的地图, 那么您就创建一个符合画布大小的 TileSpritet, 然后在玩家移动时使用 `tilePosition` 属性来滚动纹理。 如果您创建一个像素为千的 TileSprite, 那么它会消耗大量的内存, 并引起性能问题 。 请记住: 使用 `tilePosition`来滚动您的纹理和 `tileScale`来调整纹理的大小 - 不要调整纹理本身大小或使其比它需要的要大 。

关于Tile Sprites和NPOT纹理的重要说明: 在内部, TileSprite纹理会使用GL_REPEAT来提供纹理的无缝重复。 这与WebGL处理纹理的方式相结合, 意味着它们需要POT( 两块) 大小才能包起来。 如果您向 TileSprite 提供了 NPOT (非两块) 纹理, 它会生成一个 POT 大小的画布, 并绘制到它, 缩放到 POT 大小。 然后在渲染到原始尺寸时再次缩放。 虽然这工作, 允许您使用任何大小的纹理来使用 Tile Sprite , 但它确实意味着 NPOT 纹理会在被重塑成 POT 纹理时出现反异。 在 Pixel 艺术图形中特别可见, 但它会成为问题, 但唯一避免给 POT 纹理提供纹理的方法就是 。

## 装入纹理 {#load-texture}

```javascript
this.load.image(key, url);
```

参考文献: [load image](/guide/concepts/loader#image)

## 添加砖块图案对象 {#add-tile-sprite-object}

```javascript
var image = this.add.tileSprite(x, y, width, height, textureKey);
```

从 JSON 添加瓷砖图案

```javascript
var image = this.make.tileSprite({
    x: 0,
    y: 0,
    width: 512,
    height: 512,
    key: '',

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

## 自定义类 {#custom-class}

- 定义类

    ```javascript
    class MyTileSprite extends Phaser.GameObjects.TileSprite {
        constructor(scene, x, y, width, height, texture, frame) {
            super(scene, x, y, width, height, texture, frame);
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
    var image = new MyTileSprite(scene, x, y, key);
    ```

## 瓦片属性 {#properties-of-tiles}

- Position

    ```javascript
    image.setTilePosition(x, y);
    ```

    or

    ```javascript
    image.tilePositionX = x;
    image.tilePositionY = y;
    ```

- Scale

    ```javascript
    image.setTileScale(scaleX, scaleY);
    ```

    or

    ```javascript
    image.tileScaleX = scaleX;
    image.tileScaleY = scaleY;
    ```

## 其他属性 {#other-properties}

见[game object](/guide/concepts/gameobjects)

## 创建遮罩 {#create-mask}

```javascript
var mask = image.createBitmapMask();
```

见[mask](/guide/concepts/display#masks)

## 阴影效果 {#shader-effects}

支持 [preFX and postFX effects](/guide/concepts/gameobjects/shader) 软件

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
