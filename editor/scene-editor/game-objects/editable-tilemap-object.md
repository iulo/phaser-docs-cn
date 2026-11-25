# 可编辑的瓦片地图 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/editable-tilemap-object)

在Phaser编辑器中,我们有两种图案, 一种是您可以在平面和[import them into the scene editor](/editor/scene-editor/game-objects/tilemap-object)中创建的, 另一种是您可以在编辑器中直接创建的。

[Tiled](https://www.mapeditor.org)是一个地图编辑器,已经存在多年,并且已经融入了各种工具,使级别创建变得更容易。它仍然是您可以访问的最佳选择之一。然而,Phaser编辑器中安装的地图编辑器在将平面图与场景中的其他对象整合时,会带来显著的优势。在本节中,我们将讨论如何利用场景编辑器中的工具创建一个平面图。

## 创建可编辑的平面图 {#creating-an-editable-tilemap}

要创建可编辑的平面图, 请从块视图中拖动 ** Ediable Tilemap ** 块, 并将其丢入现场 :

![Add editable tilemap to the scene](https://cdn.phaser.games/oss-docs/assets/86e2df9965e49ed2-scene-editor-editable-tilemap-create-1.webp)

编辑器立即显示一个对话框,用于设置图片的基本参数,例如列数和行数,以及图片大小:

![Setting tilemap parameters](https://cdn.phaser.games/oss-docs/assets/01d160e9590efc7e-scene-editor-editable-tilemap-create-2-2.webp)

新的图片对象出现在大纲视图的 ** 平面图** 类别中。 您可以在 检查器视图的 ** 可变** 部分更改对象名称 :

![Tilemap object in the Outline view](https://cdn.phaser.games/oss-docs/assets/c1fad9b0c7e2d120-scene-editor-editable-tilemap-3-20241106.webp)

平面图主要由平面图和平面图层组成。平面图是包含用于构建地图的平面图的图像。平面图层是绘制平面图的游戏对象。

### 创建平板 {#creating-a-tileset}

检查官的 ** 字段显示地图的瓦片和图层。 首先, 我们需要创建一个瓦片集。 要做到这一点,我们就按下在 ** TIRE STES** 段找到的添加按钮: ![Add tileset](https://cdn.phaser.games/oss-docs/assets/904cd1f0611d46b2-scene-editor-editable-tilemap-add-tilese.webp) 它打开了对话框, 包含项目资源包中定义的所有图像和图示表。 请选择一个 。 ![Select tileset image](https://cdn.phaser.games/oss-docs/assets/4e918f0e8eab4dd9-scene-editor-editable-tilemap-add-tilese.webp) 当按下 ** 选择 ** 按钮时, 它会为地图创建新的瓦片集, 其名称与资源相同。 瓦片集有多个参数。 如果您以图示表资源作为图像创建, 瓦片集会复制许多图示表参数, 如边距、 间隔、 瓦片宽度和瓦片高度 。

新瓦片列于**TILE STES** 部分:

![Tilesets](https://cdn.phaser.games/oss-docs/assets/7645d8c44b711d2a-scene-editor-editable-tilemap-add-tilese.webp)

您可以点击 ** Trash** 图标删除它, 或者点击它的名称来更改它的属性 :

![Tileset properties](https://cdn.phaser.games/oss-docs/assets/ca48b359f56bf515-scene-editor-editable-tilemap-tileset-pr.webp)

在平板属性中,您可以更改其大小和图像。此外,该部分还显示 ** Edit Map ** 按钮,您可以按该按钮返回到编辑图片时。

砖块属性下方为 ** 砖块预览 ** 部分,其中显示砖块图像和标出不同砖块的网格.
### 创建新图片层 {#create-a-new-tilemap-layer}

一旦我们准备好瓦片,我们可以在地图上添加新的层。要做到这一点,请按 **LAYERS** 部分中找到的添加按钮:

![Add layer](https://cdn.phaser.games/oss-docs/assets/8b9b729376db7165-scene-editor-editable-tilemap-add-layer-.webp)

新层会自动取一个名称 。

![The layers list](https://cdn.phaser.games/oss-docs/assets/edc599f146234e7c-scene-editor-editable-tilemap-add-layer-.webp)

要更改名称和其他属性,可以点击层名或者选择场景中的层.

![Tilemap layer properties](https://cdn.phaser.games/oss-docs/assets/9b6fa96a0abeff93-scene-editor-editable-tilemap-layer-prop.webp)

(要返回图片属性,可以点击 ** Edit Map ** 按钮)

平面图层是游戏对象,出现在场景中,因此也可以在场景和大纲视图中选择.

![Tilemap layer in the outline view](https://cdn.phaser.games/oss-docs/assets/82b55da39251fbf4-scene-editor-tilemap-layer-select-202411.webp)

要删除一个层次,您遵循与其他游戏对象相同的程序,请选择该层次并按 **Delete**。

## 绘制图层 {#drawing-on-a-tilemap-layer}

要绘制图片的单元格,必须满足某些要求:

- 在大纲视图中选择一个可编辑的图片。这可以激活“编辑图片”模式。
- 添加至少一个瓦片和一个瓦片层.
- 在检查器视图的 ** 平面板** 部分中, 选择您要绘制的平面板和您要绘制的平脸板层。 平面板总是绘制在特定的层上 。

![Select tileset and layer to paint](https://cdn.phaser.games/oss-docs/assets/d4ae5cf24f208587-scene-editor-editable-tilemap-paint-1-20.webp)

当选择要绘制的图片层时,在现场用橙色边框突出显示,并显示您可以画砖的网格。

![Layer selected to paint](https://cdn.phaser.games/oss-docs/assets/c0dca925191326cc-scene-editor-editable-tilemap-layer-to-p.webp)

下一步是选择要用什么工具来画,以及您要用作刷子的瓦片部分。

![Tilemap painting tools](https://cdn.phaser.games/oss-docs/assets/20d9497d09da5016-scene-editor-editable-tilemap-tools-intr.webp) 

下一节详细解释了图版工具如何运作.

## 斜拉图工具 {#tilemap-tools}

此时, tilemap 编辑器为图版层上绘画提供了一些基本工具。 如上一节所解释的那样, 要激活“ tilemap编辑器” 模式, 您必须选择可编辑的tilemap, 并选择一个 tileset 和 tilemap 图版来进行绘画 。

工具在工具栏中显示, 您可以选择它们。 这些工具是迄今为止可用的工具 :

![Tilemap toolbar](https://cdn.phaser.games/oss-docs/assets/ce952e55202276c5-scene-editor-editable-tilemap-toolbar-20.webp)

- **邮票**: 使用刷子在图版层上盖章。
- **装填桶**: 使用刷子填充所有空单元格或具有相同瓦片标识的单元格。
- **矩形填充**: 使用刷子填充长方形区域。
- **擦除器**: 。它可以使用一个像算法那样的桶装来删除单元格。
- **矩形选择**: 来选择图片层中的区域。它可用于擦除单元格或与选定的单元格创建刷。

### 刷子 刷子 {#the-brush}

许多工具都使用刷子。在我们解释每个工具是如何工作的之前,让我们解释你如何选择刷子。

刷子是砖块的长方形部分。 要选择这部分, 您必须首先选择一个支持刷子的工具, 如 Stamp, Bucket fill等... 然后, 您必须拖动鼠标, 从刷子左上角开始, 拖到右下角 。 您可以在拖动鼠标时看到刷子区域被突出显示 :

![Select brush](https://cdn.phaser.games/oss-docs/assets/75b8698c53be7ed5-scene-editor-editable-tilemap-select-bru.gif)

顺便说一下,你可以用鼠标轮子放大和放大平板图像,按下`Alt`键并拖动鼠标来压平图像。另外,在图像底部还有控制缩放的按钮。

### 印花工具 {#stamp-tool}

印花工具是最基本的工具。 您可以用它来印上图片层上的刷子。 要绘制, 请选择一个刷子, 然后到图片层并按下鼠标左键。 您可以点击鼠标位置的刷子印上, 或者用鼠标左键拖动鼠标以绘制整个中键 :

![stamp tool](https://cdn.phaser.games/oss-docs/assets/0fabc528b351982a-scene-editor-editable-tilemap-stamp-tool.gif)

### 装填工具 {#bucket-fill-tool}

使用桶装工具,您可以单击时填充整个空间。 填充的空间由拥有相同身份和邻居的牌块决定 。

![bucket fill tool](https://cdn.phaser.games/oss-docs/assets/bcead2799a0f9163-scene-editor-editable-tilemap-bucket-fil.gif)

### 矩形填充工具 {#rectangular-fill-tool}

使用长方形填充工具,您可以在图版层中填充长方形空间。填充覆盖您选择的整长方形区域并绘制刷子图案。

![rect fill tool](https://cdn.phaser.games/oss-docs/assets/4267e000d8ec3410-scene-editor-editable-tilemap-rect-fill-.gif)

### 擦除工具 {#eraser-tool}

您可以使用此工具去除图片层的单元格。 您不需要选择刷子。 只要将鼠标拖到图层上, 即可删除光标通过的所有单元格。 您也可以选择按住 `Shift`Z 键, 点击单元格删除所有带有相同瓦片标识的相邻单元格, 并遵循桶填充算法 。

![eraser tool](https://cdn.phaser.games/oss-docs/assets/ed9bf59a9dfc42ad-scene-editor-editable-tilemap-eraser-too.gif)

### 矩形选择工具 {#rectangular-selection-tool}

使用矩形选择工具,您可以在地图上选择一个区域, 并做两件事: 按下 `Delete` 键删除它, 或者用选择创建刷子。 要用选择创建刷子, 您必须遵循这些步骤 :

- 选择地图上的区域。
- 按 `Ctrl+C`(或如果您也想要剪切区域的话按 `Ctrl+X`) 。编辑器自动激活了 **Stamp** 工具,并加载所选的瓦片作为刷子。
- 绘制地图时经常使用**Stamp**工具。

![rect selection tool](https://cdn.phaser.games/oss-docs/assets/9f2b7cd851788598-scene-editor-editable-tilemap-rect-selec.gif)

### 蒂莱塞特信息工具 {#tileset-info-tool}

通过这个工具,您可以看到砖块和所选层的砖块索引。 下一张图像显示所选的 `mario-tileset` 砖块和所选的 `pipe` 层的砖块索引 :

![Tileset info tool](https://cdn.phaser.games/oss-docs/assets/ff61c79026b08578-scene-editor-tilemap-tool-info-20250801.webp)

## 代码生成 {#code-generation}

Phaser通常的做法是从外部文件,例如资源中加载图版。 这是因为地图是用第三方工具设计的, 也因为这样更容易按要求加载地图。 但是, 我们用这个纳入ZPhaser编辑器的图版编辑器, 我们做一些不同的事情。 我们不是将地图数据保存在外部文件, 如 JSON 文件, 而是直接将这些数据嵌入到场景代码中。 这对开发者来说可能适得其反, 但是, 我们发现这是释放图版编辑器第一版的最简单的选择。 包括代码中的图版数据( 长整数组) , 也不违背编辑器的哲学, 因为无论任何类型的场景有多大, 所有对象都是通过场景编译器生成的代码创建的。 然而, 对于编辑器的未来版本, 我们可能会提供在单独文件中生成图版数据的选项 。

当您创建可编辑的图版时, 编译器会生成代码, 将 JSON 对象以格式加载到加载器缓存中。 这样, 将使用常用的 Phaser API 创建图版实例 。

代码会像这样。 首先, 缓存中保存了图片数据, 并遵循 `Tiled` 格式 。

```js
// levelMap
this.cache.tilemap.add("levelMap_5ca7319c-74c6-458a-8589-37cef0ce2ff4", {
    format: 1,
    data: {
        width: 50,
        height: 30,
        orientation: "orthogonal",
        tilewidth: 16,
        tileheight: 16,
        tilesets: [
            {
                columns: 20,
                margin: 0,
                spacing: 0,
                tilewidth: 16,
                tileheight: 16,
                tilecount: 240,
                firstgid: 1,
                image: "tileset",
                name: "tileset",
                imagewidth: 320,
                imageheight: 192,
            },
        ],
        layers: [
            {
                type: "tilelayer",
                name: "mainLayer",
                width: 50,
                height: 15,
                opacity: 1,
                data: [0, 0, , 109, 109, 109, 109, ..., 109, 109, 109, 109],
            },
        ],
    },
});
```

然后,用缓存中的数据键创建了图砖:

```js
const levelMap = this.add.tilemap("levelMap_5ca7319c-74c6-458a-8589-37cef0ce2ff4");
```

瓦片也是按通常的方式创建的. `addTilesetImage()`方法将瓦片的名称作为参数:

```js
evelMap.addTilesetImage("tileset");
```

最后,按照在现场出现的顺序,这些层用`createLayer()`方法创建。这种方法作为参数接收层的名称、所用的瓦片以及层的位置:

```js
// mainLayer
const mainLayer = levelMap.createLayer("mainLayer", ["tileset"], 0, 0);
```

既可以将图列实例也可以将图列层实例指定为具有不同范围,就像你对场景中其他任何物体一样的变量.

---
