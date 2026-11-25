# 九宫格（NineSlice） {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/nine-slice)

九切游戏对象允许您显示一个既可以水平伸展又可以垂直伸展的纹理对象,但保留固定大小的角。角的尺寸通过参数设定到此类。

这对UI和元素等按钮极为有用,需要它们扩展以容纳内容而不扭曲纹理.

您为此游戏对象提供的纹理应该基于以下布局结构:

```js
     A                          B
   +---+----------------------+---+
 C | 1 |          2           | 3 |
   +---+----------------------+---+
   |   |                      |   |
   | 4 |          5           | 6 |
   |   |                      |   |
   +---+----------------------+---+
 D | 7 |          8           | 9 |
   +---+----------------------+---+
```

更改对象宽度和 / 或高度时:

- 区域1、3、7和9(角)将保持无标
- 区域2和8将仅横向伸展
- 区域4和6将仅垂直伸展
- 5 将横向和纵向拉伸

您也可以创建3个切片游戏对象 :

这种方法效果类似,但只能水平拉伸。 因此,它需要更少的配置:

```js
     A                          B
   +---+----------------------+---+
   |   |                      |   |
 C | 1 |          2           | 3 |
   |   |                      |   |
   +---+----------------------+---+
```

更改对象宽度时( 您不能更改其高度)

- 区域1和3将保持不变
- 区域2将横向拉伸

上述配置概念改编自Pixi NineSlicesPlane.

要指定一个3个切片对象而不是9个切片, 您只应该提供 `leftWidth` 和 `rightWidth` 参数。 要创建 9 个切片, 您必须提供所有参数 。

此游戏对象最小宽度的(_L) 共 `leftWidth` + `rightWidth`。此游戏对象最小高度为: `topHeight` + `bottomHeight`。如果需要以较小的尺寸显示此对象,可以将其缩放。

在性能方面,使用3切游戏对象相当于连续有3个Sprites. 使用9切游戏对象相当于连续9个Sprites,这个对象的顶点全部进行批次,可以与显示列表上的其他Sprites和图形共存,而不会引起任何额外的间接费用.

至Phaser 3.60 此游戏对象为**WebGL仅**.

至 Phaser 3. 70 此游戏对象如果设定在 Tetriure Packer 7. 1.0 或以上, 并用 json 地图集导出, 现在可以自动填充其值。 如果是这样, 您可以使用这种方法, 而不指定 纹理 键和框架 , 并且它会从 地图集 中提取区域数据 。

## 装入纹理 {#load-texture}

```javascript
this.load.image(key, url);
```

参考文献: [load image](/guide/concepts/loader#image)

## 添加九块切片对象 {#add-nine-slice-object}

```javascript
var nineSlice = this.add.nineslice(x, y, texture, frame, width, height, leftWidth, rightWidth, topHeight, bottomHeight);
```

or

```javascript
var nineSlice = this.add.nineslice(x, y, texture, frame, width, height);
// var nineSlice = this.add.nineslice(x, y, texture, frame);
```

- 如果该帧(由`texture`索引,`frame`)由Texture Packer生成.

从 JSON 添加九片

```javascript
var nineSlice = this.make.nineslice({
    x: 0,
    y: 0,
    key: '',
    // frame: '',

    // width: 256,
    // height: 256,
    // leftWidth: 10,
    // rightWidth: 10,
    // topHeight: 0,
    // bottomHeight: 0,

    // angle: 0,
    // alpha: 1,
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
    class MyNineSlice extends Phaser.GameObjects.NineSlice {
        constructor(scene, x, y, texture, frame, width, height, leftWidth, rightWidth, topHeight, bottomHeight) {
            super(scene, x, y, texture, frame, width, height, leftWidth, rightWidth, topHeight, bottomHeight);
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
    var nineSlice = new MyNineSlice(scene, x, y, texture, frame, width, height, leftWidth, rightWidth, topHeight, bottomHeight);
    ```

## 调整大小 {#resize}

```javascript
nineSlice.setSize(width, height);
```

## 设置源图像的纹理 {#set-texture-of-source-image}

```javascript
nineSlice.setTexture(texture, frame);
nineSlice.setSlices(width, height, leftWidth, rightWidth, topHeight, bottomHeight);
```

## 纹理 {#texture}

见[game object - texture](/guide/concepts/gameobjects#textures)

## 其他属性 {#other-properties}

见[game object](/guide/concepts/gameobjects)

## 创建遮罩 {#create-mask}

```javascript
var mask = nineSlice.createBitmapMask();
```

见[mask](/guide/concepts/display#masks)

## 阴影效果 {#shader-effects}

支持 [postFX effects](/guide/concepts/gameobjects/shader) 软件

!!! note
    无 preFX 效果支持

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
