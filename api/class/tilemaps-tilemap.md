# Tilemap {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tilemaps-tilemap)

蒂勒马普是蒂勒马普数据的容器。 这不是一个显示对象, 而是它保存关于地图的数据, 并允许您在地图中添加瓦片和图片层。 地图可以有一个或多个图片层, 它们是显示对象, 真正使图片产生。

Tilemap 数据可以从 Tiled JSON 文件、 CSV 文件或 2D 阵列中解析。 Tiled 是专门用于创建瓦片地图的自由软件包, 可从: [http://www.mapeditor.org](http://www.mapeditor.org)

Tilemap API 支持以下类型的地图:

1) 斜体 2, 异构 3, 六边形 4, 相交

所有地图类型都使用统一的`TilemapLayer`类,将前静态和动态层的能力结合成一个单一的简化API.

平面图具有在一层内获取和操纵瓦片的实用方法,可以让您在运行时构建或修改平面图数据.

注意所有 Tilemaps 使用基片大小来计算维度, 但 TilemapLayer 可能具有它自己独特的瓦片大小来覆盖此值 。

如果您的平面图包括层组(平面图1.2.0+的一个特征),这些层组将经过曲折,以下属性将影响孩子: 平面图:

- 不透明(与父母混合)和可见度(父母凌驾于孩子之上)

- 纵向和横向

组分等级没有保留,所有层层都会被平整成一个单数组.

组层在 Tilemap 构建过程中被解析, 但解析后被丢弃, 因此动态层不会继续受到父结构的影响 。

为了避免层名重复, 组层的子层会用“ /” 来准备其父组名。 例如, 考虑将一个名为“ Layer 1” 的组称为“ 家长小组 ” 。 在 Tilemap 对象中, “ Layer 1” 会使用“ PairentGroup/ Layer 1” 一词 。

Phaser 倾斜解析器** not** 支持“ 收集图像” 特性的倾斜。 您必须确保您的所有砖块都包含在一个单的平板图像文件( 每层) 中, 并在导出的倾斜 JSON 映射数据中包含“ 嵌入 ” 。

**构造函数**

`new Tilemap(scene, mapData)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 蒂莱玛普属于的场景. |
| mapData | [Phaser.Tilemaps.MapData](/api/class/tilemaps-mapdata) | 否 | 包含 Tilemap 数据的 MapData 实例 。 |

---


**作用域**: static

> 源码：[src/tilemaps/Tilemap.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L47)  
引入版本：3.0.0

## 公开成员 {#public-members}

### currentLayerIndex {#currentLayerIndex}

#### currentLayerIndex: number {#currentlayerindex-number}


**说明:**

当前所选的LyerData对象的索引。


> 源码：[src/tilemaps/Tilemap.js#L282](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L282)  
引入版本：3.0.0


---

### format {#format}

#### format: number {#format-number}


**说明:**

地图数据的格式.


> 源码：[src/tilemaps/Tilemap.js#L179](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L179)  
引入版本：3.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

地图的高度(以瓦片计).


> 源码：[src/tilemaps/Tilemap.js#L143](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L143)  
引入版本：3.0.0


---

### heightInPixels {#heightInPixels}

#### heightInPixels: number {#heightinpixels-number}


**说明:**

地图的高度,以高度*tileHeight为基数.


> 源码：[src/tilemaps/Tilemap.js#L218](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L218)  
引入版本：3.0.0


---

### hexSideLength {#hexSideLength}

#### hexSideLength: number {#hexsidelength-number}


**说明:**

六边形的横向侧面长度,仅用于六边形方向 Tilemaps.


> 源码：[src/tilemaps/Tilemap.js#L291](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L291)  
引入版本：3.50.0


---

### imageCollections {#imageCollections}

#### imageCollections: Array.\<[Phaser.Tilemaps.ImageCollection](/api/class/tilemaps-imagecollection)> {#imagecollections-arrayphasertilemapsimagecollection}


**说明:**

从平面图数据解析的图像集 。


> 源码：[src/tilemaps/Tilemap.js#L227](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L227)  
引入版本：3.0.0


---

### images {#images}

#### images: array {#images-array}


**说明:**

平面图像层的阵列 。


> 源码：[src/tilemaps/Tilemap.js#L236](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L236)  
引入版本：3.0.0


---

### layer {#layer}

#### layer: [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) {#layer-phasertilemapslayerdata}


**说明:**

目前选中的图中的图层数据对象。 您可以使用 setLayer 支持的任意类型设置此属性 。


> 源码：[src/tilemaps/Tilemap.js#L1607](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1607)  
引入版本：3.0.0


---

### layers {#layers}

#### layers: Array.\<[Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata)> {#layers-arrayphasertilemapslayerdata}


**说明:**

一系列的蒂列玛普层数据.


> 源码：[src/tilemaps/Tilemap.js#L245](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L245)  
引入版本：3.0.0


---

### objects {#objects}

#### objects: Array.\<[Phaser.Tilemaps.ObjectLayer](/api/class/tilemaps-objectlayer)> {#objects-arrayphasertilemapsobjectlayer}


**说明:**

从平面对象层解析的 ObjectLayer 实例数组 。


> 源码：[src/tilemaps/Tilemap.js#L273](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L273)  
引入版本：3.0.0


---

### orientation {#orientation}

#### orientation: string {#orientation-string}


**说明:**

地图数据的方向(如图中指定的),通常为“正弦” 。


> 源码：[src/tilemaps/Tilemap.js#L152](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L152)  
引入版本：3.0.0


---

### properties {#properties}

#### properties: object, Array.\<object> {#properties-object-arrayobject}


**说明:**

映射图中指定的特定属性 。

根据图案化和JSON导出所使用的版本,它将是一个对象或一个阵列。对于图案化1.2.0+地图,它将成为数组。


> 源码：[src/tilemaps/Tilemap.js#L197](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L197)  
引入版本：3.0.0


---

### renderOrder {#renderOrder}

#### renderOrder: string {#renderorder-string}


**说明:**

映射数据的渲染(draw)顺序(如图案所指定的),通常为"右下方".

抽签命令如下:

右下左下右上左下 右下右上

这可以通过`setRenderOrder`方法改变.


> 源码：[src/tilemaps/Tilemap.js#L161](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L161)  
引入版本：3.12.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


> 源码：[src/tilemaps/Tilemap.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L107)  
引入版本：3.0.0


---

### tileHeight {#tileHeight}

#### tileHeight: number {#tileheight-number}


**说明:**

以像素表示的瓦片基高。请注意,各层的瓦片高度可能不同。


> 源码：[src/tilemaps/Tilemap.js#L124](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L124)  
引入版本：3.0.0


---

### tiles {#tiles}

#### tiles: array {#tiles-array}


**说明:**

砖块主列表 - > x,y, 以砖块为索引.


> 源码：[src/tilemaps/Tilemap.js#L254](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L254)  
引入版本：3.60.0


---

### tilesets {#tilesets}

#### tilesets: Array.\<[Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset)> {#tilesets-arrayphasertilemapstileset}


**说明:**

地图中使用的提列塞茨阵列 。


> 源码：[src/tilemaps/Tilemap.js#L264](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L264)  
引入版本：3.0.0


---

### tileWidth {#tileWidth}

#### tileWidth: number {#tilewidth-number}


**说明:**

以像素表示的瓦片基宽度。请注意,单个层的瓦片宽度可能不同。


> 源码：[src/tilemaps/Tilemap.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L114)  
引入版本：3.0.0


---

### version {#version}

#### version: number {#version-number}


**说明:**

地图数据版本(如图案所指定,通常为1).


> 源码：[src/tilemaps/Tilemap.js#L188](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L188)  
引入版本：3.0.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

地图的宽度( 以平板块计) 。


> 源码：[src/tilemaps/Tilemap.js#L134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L134)  
引入版本：3.0.0


---

### widthInPixels {#widthInPixels}

#### widthInPixels: number {#widthinpixels-number}


**说明:**

以宽度 * tileWidth为单位的地图宽度,以像素表示.


> 源码：[src/tilemaps/Tilemap.js#L209](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L209)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### addTilesetImage {#addTilesetImage}

#### \<instance> addTilesetImage(tilesetName, [key], [tileWidth], [tileHeight], [tileMargin], [tileSpacing], [gid], [tileOffset]) {#instance-addtilesetimagetilesetname-key-tilewidth-tileheight-tilemargin-tilespacing-gid-tileoffset}


**说明:**

将图像添加到地图中, 用作平板块。 单一的地图可能使用多个平板块。 请注意, 平板块名称可以在从平板块导出的 JSON 文件或平板块编辑器中找到 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tilesetName | string | 否 |  | 地图数据中指定的平板名称。 |
| key | string | 是 |  | 用于此平面图的 Phaser.Cache 图像的键。 如果 `undefined` 或 `null` , 则会寻找一个匹配 tilesetName 参数的键的图像 。 |
| tileWidth | number | 是 |  | 蒂莱塞特图像中的瓦片( 像素) 宽度。 如果不给出它, 将默认为地图的 tileWidth 值, 或者默认 Tiled JSON 文件指定的 tileWidth 值 。 |
| tileHeight | number | 是 |  | 蒂莱塞特图像中的瓦片高度( 像素) 。 如果不给出, 将默认为地图的 tileHeight 值, 或是 Tiled JSON 文件指定的 tileHeight 。 |
| tileMargin | number | 是 |  | 工作表中的瓦片周围的边距( 像素) 。 如果不指定, 它会默认为 0 或 平面 JSON 文件指定的值 。 |
| tileSpacing | number | 是 |  | 工作表中每个瓦之间的间距( 像素) 。 如果不指定, 则默认为 0 或 平面 JSON 文件指定的值 。 |
| gid | number | 是 | 0 | 如果将多个牌加到空白地图中, 请指定此集将使用的 GID 起始位置 。 |
| tileOffset | object | 是 | "{x: 0, y: 0}" | 平铺纹理绘图偏移。 如果不指定, 则默认为{0, 0} |


**返回值:** [Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset) - 返回创建或更新的 Tileset 对象,如果失败则无效。


> 源码：[src/tilemaps/Tilemap.js#L369](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L369)  
引入版本：3.0.0


---

### calculateFacesAt {#calculateFacesAt}

#### \<instance> calculateFacesAt(tileX, tileY, [layer]) {#instance-calculatefacesattilex-tiley-layer}


**说明:**

在指定的层的瓦片坐标处计算有趣的面。 有趣的面用于优化与瓦片的碰撞。 这种方法大多用于在仅更改一个瓦片时优化再计算面。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此值, 如果给出的图层无效, 则返回此值或为无效 。


> 源码：[src/tilemaps/Tilemap.js#L1753](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1753)  
引入版本：3.0.0


---

### calculateFacesWithin {#calculateFacesWithin}

#### \<instance> calculateFacesWithin([tileX], [tileY], [width], [height], [layer]) {#instance-calculatefaceswithintilex-tiley-width-height-layer}


**说明:**

计算层的矩形区域( 平面坐标) 内有趣的面孔。 有趣的面孔用于优化与瓦片的碰撞。 这种方法大多在内部使用 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此值, 如果给出的图层无效, 则返回此值或为无效 。


> 源码：[src/tilemaps/Tilemap.js#L1780](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1780)  
引入版本：3.0.0


---

### copy {#copy}

#### \<instance> copy(srcTileX, srcTileY, width, height, destTileX, destTileY, [recalculateFaces], [layer]) {#instance-copysrctilex-srctiley-width-height-desttilex-desttiley-recalculatefaces-layer}


**说明:**

复制源长方形区域中的瓦片到层内的新目的地( 全部在瓦片坐标中指定) 。 复制所有瓦片属性并重新计算目的地区域的碰撞信息 。

如果没有指定图层,则使用地图的当前图层.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| srcTileX | number | 否 |  | 要复制的区域的x坐标,以瓦片表示,而不是像素. |
| srcTileY | number | 否 |  | 要复制的区域的y坐标, 以瓦片而不是像素表示 。 |
| width | number | 否 |  | 要复制的区域的宽度,以瓦片表示,而不是像素. |
| height | number | 否 |  | 要复制的区域的高度,以瓦片表示,而不是像素. |
| destTileX | number | 否 |  | 要复制的区域的x坐标,以瓦片表示,而不是像素. |
| destTileY | number | 否 |  | 区域y坐标以瓦片形式复制,而不是像素。 |
| recalculateFaces | boolean | 是 | true | 如果面额数据应重新计算,则使用`true`。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 |  | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此值, 如果给出的图层无效, 则返回此值或为无效 。


> 源码：[src/tilemaps/Tilemap.js#L458](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L458)  
引入版本：3.0.0


---

### createBlankLayer {#createBlankLayer}

#### \<instance> createBlankLayer(name, tileset, [x], [y], [width], [height], [tileWidth], [tileHeight]) {#instance-createblanklayername-tileset-x-y-width-height-tilewidth-tileheight}


**说明:**

创建新和空的 Tilemap 层。 地图中目前选中的层被设置为这个新层。

在v3.50.0之前,这种方法被称为`createBlankDynamicLayer`.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 名称 | string | 否 |  | 此图层的名称。 必须是地图中唯一的 。 |
| tileset | string \| Array.\<string> | [Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset) | Array.\<[Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset)> | 否 |  | 用于制导此图层的瓦片组或一系列瓦片。可以是字符串或蒂列塞特对象 。 |
| x | number | 是 | 0 | 将这个层的左上方放置的世界x位置. |
| y | number | 是 | 0 | 将这个层的左上方放置在 y 位置的世界 。 |
| width | number | 是 |  | 以瓦片计的图层宽度。 如果不指定, 则默认为地图宽度 。 |
| height | number | 是 |  | 以瓦片计的图层高度。 如果不指定, 则默认为地图的高度 。 |
| tileWidth | number | 是 |  | 计算时使用的图片宽度。 如果不指定, 则默认为地图的 tileWidth 。 |
| tileHeight | number | 是 |  | 层的高度用于计算。 如果不指定, 它会默认为地图的 tileHeight 。 |


**返回值:** [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) - 返回创建的新图层, 如果失败, 返回 `null` 。


> 源码：[src/tilemaps/Tilemap.js#L500](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L500)  
引入版本：3.0.0


---

### createFromObjects {#createFromObjects}

#### \<instance> createFromObjects(objectLayerName, config, [useTileset]) {#instance-createfromobjectsobjectlayername-config-usetileset}


**说明:**

此方法将覆盖一个平面对象层中定义的所有对象, 然后将匹配结果转换为 Phaser 游戏对象( 默认为 Sprites)

对象在4个标准之一中匹配:对象ID,对象GID,对象名称,或者对象类型.

在倾斜中,对象ID是每个对象独有的。然而,对象GID是所有对象使用相同的图像共享的。最后,对象名称和类型是字符串,在倾斜中的多个对象上可以使用相同名称,它们不一定是独一无二的; 名称是对象所特有的,而类型则可以使用相同的图像从对象GID中继承.

您据此设置配置参数, 其标准类型是您想要匹配的。 例如, 将对象层上的所有项目转换为 `gid` 26 :

```javascript
createFromObjects(layerName, {
  gid: 26
});
```

或者,要转换名称为“ bonus” 的物体:

```javascript
createFromObjects(layerName, {
  name: 'bonus'
});
```

或,用特定的代号转换对象:

```javascript
createFromObjects(layerName, {
  id: 9
});
```

您只应该指定其中之一 `id`, `gid`, `name`, `type`,或者没有。在配置中不要添加一个以上的标准。如果您没有指定任何标准,那么将转换对象层中的 _所有_对象。

默认情况下,这种方法将把对象转换成 [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) 实例,但您可以通过提供自己的类类型来覆盖此:

```javascript
createFromObjects(layerName, {
  gid: 26,
  classType: Coin
});
```

这将将所有对象的 gid 26 转换为您的自定义的 `Coin` 类。 您可以在此通过任何类类型, 但是它将 _ must_ 扩展 [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) 作为其基础类。 您的类将永远通过 1 参数: `scene`, 它指的是配置对象中指定的景物, 或者, 如果不是, 是指这个 Tilemap 属于的景物。 该类必须具有 [setPosition](/api/namespace/gameobjects-components-transform#setPosition) 和 [setTexture](/api/namespace/gameobjects-components-texture#setTexture) 方法 。

这种方法将在新的游戏对象上设置以下平面对象属性:

- `flippedHorizontal` 作为 `flipX`

- `flippedVertical` 作为 `flipY`

- `height` 作为 `displayHeight`

- `name`

- `rotation`

- `visible`

- `width` 作为 `displayWidth`

- `x`,根据原产地调整

- `y`,根据原产地调整

此外,这种方法将设置倾斜对象自定义属性

- (a) 具有相同属性名称和不为`undefined`的值的;或

- 游戏对象的[data](/api/class/gameobjects-gameobject#data) 否则。

例如,一个自定义属性`{ alpha: 0.5, gold: 1 }`的倾斜对象将会被创建为游戏对象,其`alpha`值为0.5,`data.values.gold`值为1.

`useTileset`是 `true`(默认)时, 砖块对象会继承纹理和任何砖块属性, 本地的砖块ID会被用作纹理帧。 要进行框架选择, 您需要将砖块纹理加载为精灵表, 使其框架名称与本地的砖块ID匹配 。

例如,一个平板砖

```
{ id: 3, type: 'treadmill', speed: 4 }
```

带有 Gid 19 和对象

```
{ id: 7, gid: 19, speed: 5, rotation: 90 }
```

将解释为

```
{ id: 7, gid: 19, speed: 5, rotation: 90, type: 'treadmill', texture: '[the tileset texture]', frame: 3 }
```

您可以为每个 `config` 设置布尔 `ignoreTileset` 来压制这种行为, 因为它应该忽略对象 gid 牌。

您可以在配置中设置 `container` 属性。 如果给出, 新的游戏对象将被添加到容器或图层实例中, 而不是场景 。

您可以设置命名为纹理- `key` 和纹理- `frame` 属性, 将在新的游戏对象上设置 。

最后,您可以提供一组配置对象,在单个调用中转换多个类型对象:

```javascript
createFromObjects(layerName, [
  {
    gid: 26,
    classType: Coin
  },
  {
    id: 9,
    classType: BossMonster
  },
  {
    name: 'lava',
    classType: LavaTile
  },
  {
    type: 'endzone',
    classType: Phaser.GameObjects.Zone
  }
]);
```

在 v3. 60.0 中, 此方法的签名发生了显著变化 。 在此之前, 它没有取到配置对象 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| objectLayerName | string | 否 |  | 用于创建游戏对象的平面对象层名称 。 |
| config | [Phaser.Types.Tilemaps.CreateFromObjectLayerConfig](/api/typedef/types-tilemaps#createfromobjectlayerconfig) \| Array.\<[Phaser.Types.Tilemaps.CreateFromObjectLayerConfig](/api/typedef/types-tilemaps#createfromobjectlayerconfig)> | 否 |  | 从对象配置对象创建, 或其中的数组 。 |
| useTileset | boolean | 是 | true | 如果设置 gid 对象也搜索下面的瓦片以查找属性和数据,则为真 。 |


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 包含游戏对象的阵列。 如果无效的对象层为空, 或找不到匹配的 id/ gid/ name 。


> 源码：[src/tilemaps/Tilemap.js#L661](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L661)  
引入版本：3.0.0


---

### createFromTiles {#createFromTiles}

#### \<instance> createFromTiles(indexes, replacements, [spriteConfig], [scene], [camera], [layer]) {#instance-createfromtilesindexes-replacements-spriteconfig-scene-camera-layer}


**说明:**

为图层中匹配所给的瓦片索引的每个瓦片创建一个 Sprite。 您可以选择指定每个瓦片是否在 sprite 创建后被替换为新瓦片。 如果您想要在转换后删除瓦片, 请将这个值设定为 - 1 。

如果您想要在转换成Sprites的级别下铺设特殊瓦片,但想要在转换后用地板或类似瓦片来替换瓦片本身,此操作是有用的.

Phaser v3.80中增加了以下特性: :          ;    ; :    ; ;    .

默认情况下, Phaser Sprites 的起源设定为 0.5 x 0.5. 如果您在 spriteConfig 中未指定新的起源, 那么它会调整 spriite 位置 , 使其在地图上精确定位 。

当创建了Sprite后,它将从砖块中复制以下属性:

旋转,flipX,flipY,Alpha,"可见"和"提示"。

spriteConfig还有一个特殊的属性叫做`useSpriteSheet`。如果设置为`true`,您已经将瓦片装入成精灵表(不是图像),那么它会设置Sprite 键和框架,以匹配图示纹理和瓦片索引。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| indexes | number \| array | 否 | 砖块索引,或指向的数组,用来创建Sprites。 |
| replacements | number \| array | 否 | 将转换的瓦片转换为 . 设置为 `null` 使瓦片保持不变。 如果给出了数组, 则假定它是与索引数组的一对一映射 。 |
| spriteConfig | [Phaser.Types.GameObjects.Sprite.SpriteConfig](/api/typedef/types-gameobjects-sprite#spriteconfig) | 是 | 配置对象可以传递到Sprite创建者(即场景. make.sprite)中. |
| scene | [Phaser.Scene](/api/class/scene) | 是 | 创造内在的斯普丽特的场景. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** Array.\<[Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite)> - 返回一个 Sprite 数组, 如果给出的图层无效, 则返回为无效 。


> 源码：[src/tilemaps/Tilemap.js#L950](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L950)  
引入版本：3.0.0


---

### createLayer {#createLayer}

#### \<instance> createLayer(layerID, tileset, [x], [y], [gpu]) {#instance-createlayerlayerid-tileset-x-y-gpu}


**说明:**

创建新的 Tilemap 层,使图层数据与给定的 `layerID` 相关。当前在地图中选定的层被设置为这个新层。

`layerID`很重要。 如果您在倾斜器中创建了您的地图, 您可以通过查看倾斜器和层名来获取它。 或者您可以打开 JSON 文件, 输出并查看层 []. name 值。 无论哪种方式, 它都必须匹配 。

在v3.50.0之前,这种方法被称为`createDynamicLayer`.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| layerID | number \| string | 否 |  | 层数组索引值,或者如果给出字符串,则从倾斜图中得出层名. |
| tileset | string \| Array.\<string> | [Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset) | Array.\<[Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset)> | 否 |  | 用于渲染此层的瓦片组或数组瓦片。 可以是字符串或蒂列塞特对象。 当它是数组时, 如果 `gpu`是 `true`, 则只使用数组中的第一个元素作为瓦片组 。 |
| x | number | 是 | 0 | 将层放置在世界中的x位置。 如果不指定, 它会默认为从平面或 0 中抵消的层 。 |
| y | number | 是 | 0 | 将层放置在世界中的y位置。 如果不指定, 它会默认为从平面或 0 中抵消的层 。 |
| gpu | boolean | 是 | false | 创建 TilemapGPULayer 而不是 TilemapLayer。 此选项只使用 WebGL 。 A TilemapG PULayer 的灵活性较小, 但可以更快。 它只能与整形图列正常工作 。 |


**返回值:** [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer), [Phaser.Tilemaps.TilemapGPULayer](/api/class/tilemaps-tilemapgpulayer) - 返回创建的新层, 如果失败则无效 。


> 源码：[src/tilemaps/Tilemap.js#L573](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L573)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

从 Tilemap 中删除所有层数据, 并取消场景引用。 这将摧毁任何已创建的 TilemapLayers 。


> 源码：[src/tilemaps/Tilemap.js#L2731](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2731)  
引入版本：3.0.0


---

### destroyLayer {#destroyLayer}

#### \<instance> destroyLayer([layer]) {#instance-destroylayerlayer}


**说明:**

摧毁给定的 TilemapLayer , 并把它从 Tilemap 中移除 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 瓦片层要销毁。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此值, 如果给出的图层无效, 则返回此值或为无效 。


> 源码：[src/tilemaps/Tilemap.js#L1850](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1850)  
引入版本：3.17.0


---

### fill {#fill}

#### \<instance> fill(index, [tileX], [tileY], [width], [height], [recalculateFaces], [layer]) {#instance-fillindex-tilex-tiley-width-height-recalculatefaces-layer}


**说明:**

设置图层的矩形区域( 以瓦片坐标) 中的瓦片与指定的索引相配合。 如果指定的索引是碰撞索引, 则图层将被设定为碰撞。 区域中的碰撞信息将被重新计算 。

如果没有指定图层,则使用地图的当前图层.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| index | number | 否 |  | 填充区域用的瓦片索引 。 |
| tileX | number | 是 |  | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 |  | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 |  | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 |  | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| recalculateFaces | boolean | 是 | true | 如果面额数据应重新计算,则使用`true`。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 |  | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此值, 如果给出的图层无效, 则返回此值或为无效 。


> 源码：[src/tilemaps/Tilemap.js#L995](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L995)  
引入版本：3.0.0


---

### filterObjects {#filterObjects}

#### \<instance> filterObjects(objectLayer, callback, [context]) {#instance-filterobjectsobjectlayer-callback-context}


**说明:**

对于给定对象层中的每个对象, 请运行给定的过滤回调功能。 任何通过过滤测试( 即回调返回真实) 的对象, 都会在新阵列中返回。 类似于 Array. prototype. Filter in vanilla JS 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| objectLayer | [Phaser.Tilemaps.ObjectLayer](/api/class/tilemaps-objectlayer) \| string | 否 | 对象层的名称( 从平面) 或对象Layer 实例 。 |
| callback | TilemapFilterCallback | 否 | 回调。 指定区域内的每个对象将被传递到这个回调中, 作为第一个也是唯一的参数 。 |
| context | object | 是 | 恢复召回的场合 。 |


**返回值:** Array.\<[Phaser.Types.Tilemaps.TiledObject](/api/typedef/types-tilemaps#tiledobject)> - 匹配搜索对象的数组, 如果给定的 objectLayer 无效, 则无效 。


> 源码：[src/tilemaps/Tilemap.js#L1028](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1028)  
引入版本：3.0.0


---

### filterTiles {#filterTiles}

#### \<instance> filterTiles(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions], [layer]) {#instance-filtertilescallback-context-tilex-tiley-width-height-filteringoptions-layer}


**说明:**

对于图层中指定的矩形区域(在图砖坐标)的每个瓦片, 运行指定的过滤回调功能。 通过过滤测试( 即调回返回真实的) 的瓦片将返回为新数组。 类似于 Array. prototype. Filter 在vanilla JS 中。 如果没有指定图层, 则使用地图当前图层 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | function | 否 | 回调。 指定区域的每一块牌将传递给这个回调, 作为第一个也是唯一的参数。 回调应该返回通过过滤器的牌的真值 。 |
| context | object | 是 | 恢复召回的场合 。 |
| tileX | number | 是 | 左最瓦索引(在瓦座坐标中)用作过滤区域的来源. |
| tileY | number | 是 | 用于过滤区域源头的最顶部的瓦片索引(在瓦片坐标中). |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 是 | 获得瓦片时可选择的过滤器。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 返回一个图案数组,如果给出的图层无效,则无效。


> 源码：[src/tilemaps/Tilemap.js#L1060](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1060)  
引入版本：3.0.0


---

### findByIndex {#findByIndex}

#### \<instance> findByIndex(index, [skip], [reverse], [layer]) {#instance-findbyindexindex-skip-reverse-layer}


**说明:**

搜索第一个匹配给定索引的图层,然后返回该图件。如果找不到匹配,则返回无效。从左上方的图板开始,并水平地继续搜索,直到它到达行的末尾,然后它会下降至下一列。如果反向布尔值是真实的,它会从右下角扫描,从上到左上。如果没有指定图层,则使用地图目前的图层。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| index | number | 否 |  | 要搜索的瓦片索引值 。 |
| skip | number | 是 | 0 | 返回前跳过匹配的瓦片的次数 。 |
| reverse | boolean | 是 | false | 如果真有, 它会逆向扫描层, 从右下方开始。 否则它会从左上方扫描 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 |  | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 返回一个图案,如果给出的图层无效,则无效。


> 源码：[src/tilemaps/Tilemap.js#L1091](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1091)  
引入版本：3.0.0


---

### findObject {#findObject}

#### \<instance> findObject(objectLayer, callback, [context]) {#instance-findobjectobjectlayer-callback-context}


**说明:**

查找给定对象层中第一个符合所提供测试功能的对象。 I. 即找到第一个`callback`返回真实对象。 类似于 Array. prototype. find in vanilla JS 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| objectLayer | [Phaser.Tilemaps.ObjectLayer](/api/class/tilemaps-objectlayer) \| string | 否 | 对象层的名称( 从平面) 或对象Layer 实例 。 |
| callback | TilemapFindCallback | 否 | 回调。 指定区域内的每个对象将被传递到这个回调中, 作为第一个也是唯一的参数 。 |
| context | object | 是 | 恢复召回的场合 。 |


**返回值:** [Phaser.Types.Tilemaps.TiledObject](/api/typedef/types-tilemaps#tiledobject) - 匹配搜索对象, 如果没有找到对象, 则无效 。


> 源码：[src/tilemaps/Tilemap.js#L1118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1118)  
引入版本：3.0.0


---

### findTile {#findTile}

#### \<instance> findTile(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions], [layer]) {#instance-findtilecallback-context-tilex-tiley-width-height-filteringoptions-layer}


**说明:**

找到该图层中符合所提供测试功能的第一个平面( 平面坐标) 。 I. 找到 `callback` 返回真实的第一个平面。 类似于 Array. prototype. find in vanilla JS。 如果没有指定图层, 则使用地图的当前图层 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | FindTileCallback | 否 | 回调。 指定区域内的每个瓦片都会被传递到这个回调中, 作为第一个也是唯一的参数 。 |
| context | object | 是 | 恢复召回的场合 。 |
| tileX | number | 是 | 左侧最瓦的索引(在瓦片坐标中)作为搜索区域的来源. |
| tileY | number | 是 | 用于搜索区域源头的最顶层的瓦片索引(在瓦片坐标中). |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 是 | 获得瓦片时可选择的过滤器。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 运行搜索的图层。 如果不提供, 将使用当前图层 。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 返回一个图案,如果给出的图层无效,则无效。


> 源码：[src/tilemaps/Tilemap.js#L1150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1150)  
引入版本：3.0.0


---

### forEachTile {#forEachTile}

#### \<instance> forEachTile(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions], [layer]) {#instance-foreachtilecallback-context-tilex-tiley-width-height-filteringoptions-layer}


**说明:**

对于在给定的长方形区域(在平面坐标)中的每个瓦片,运行给定的调回。类似于 Array.prototive 。forEach 以梵蒂冈JS为主

如果没有指定图层,则使用地图的当前图层.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | EachTileCallback | 否 | 回调。 指定区域内的每个瓦片都会被传递到这个回调中, 作为第一个也是唯一的参数 。 |
| context | object | 是 | 恢复召回的场合 。 |
| tileX | number | 是 | 左侧最瓦的索引(在瓦片坐标中)作为搜索区域的来源. |
| tileY | number | 是 | 用于搜索区域源头的最顶层的瓦片索引(在瓦片坐标中). |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 是 | 获得瓦片时可选择的过滤器。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 运行搜索的图层。 如果不提供, 将使用当前图层 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此值, 如果给出的图层无效, 则返回此值或为无效 。


> 源码：[src/tilemaps/Tilemap.js#L1179](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1179)  
引入版本：3.0.0


---

### getImageIndex {#getImageIndex}

#### \<instance> getImageIndex(name) {#instance-getimageindexname}


**说明:**

获取基于其名称的图像层索引。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 取之像名. |


**返回值:** number - 此图纸中的图像索引, 或找不到的无效 。


> 源码：[src/tilemaps/Tilemap.js#L1210](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1210)  
引入版本：3.0.0


---

### getImageLayerNames {#getImageLayerNames}

#### \<instance> getImageLayerNames() {#instance-getimagelayernames}


**说明:**

返回在此 Tilemap 中装入的所有有效图像显示器名列表 。


**返回值:** Array.\<string> - 装入此 Tilemap 的有效图像显示器名称/ ID 组 。


> 源码：[src/tilemaps/Tilemap.js#L1225](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1225)  
引入版本：3.21.0


---

### getIndex {#getIndex}

#### \<instance> getIndex(location, name) {#instance-getindexlocation-name}


**说明:**

内部使用。 返回一个 Tilemaps 阵列中对象的索引, 其名称属性与给定的 `name` 匹配 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| location | array | 否 | 要搜索的 Tilemap 阵列 。 |
| 名称 | string | 否 | 要获取的数组元素的名称 。 |


**返回值:** number - 数组中元素的索引,如果找不到,则无效。


> 源码：[src/tilemaps/Tilemap.js#L1246](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1246)  
引入版本：3.0.0


---

### getLayer {#getLayer}

#### \<instance> getLayer([layer]) {#instance-getlayerlayer}


**说明:**

从与给定的 `layer` 相关的 `this.layers` 获取图层数据, 如果图层无效则无效 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 图层的名称,图中的图层索引或图层索引。如果不给定,则默认为图层索引。 |


**返回值:** [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) - 相应的`LayerData`在`this.layers`,或无效.


> 源码：[src/tilemaps/Tilemap.js#L1271](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1271)  
引入版本：3.0.0


---

### getLayerIndex {#getLayerIndex}

#### \<instance> getLayerIndex([layer]) {#instance-getlayerindexlayer}


**说明:**

获取给定的图层数据索引 `layer` 内 this.layers无效时为无效 `layer` 给出。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 平面图的图层名称, 地图中的图层索引或图层索引。 如果不给出, 则默认为当前图层索引 。 |


**返回值:** number - this.layers内部的图层数据索引.


> 源码：[src/tilemaps/Tilemap.js#L1326](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1326)  
引入版本：3.0.0


---

### getLayerIndexByName {#getLayerIndexByName}

#### \<instance> getLayerIndexByName(name) {#instance-getlayerindexbynamename}


**说明:**

获取this.layers内具有给定的`name`的LyerData索引,如果给出了无效的`name`,则无效。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 层名要获得. |


**返回值:** number - this.layers内部的图层数据索引.


> 源码：[src/tilemaps/Tilemap.js#L1361](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1361)  
引入版本：3.0.0


---

### getObjectLayer {#getObjectLayer}

#### \<instance> getObjectLayer([name]) {#instance-getobjectlayername}


**说明:**

从 `this.objects` 拥有给定的 `name`,或者如果找不到该名称的ObjectLayer,则无效。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 是 | 从 Tiled 中取出的对象层名称 。 |


**返回值:** [Phaser.Tilemaps.ObjectLayer](/api/class/tilemaps-objectlayer) - 相应的`ObjectLayer`在`this.objects`,或无效.


> 源码：[src/tilemaps/Tilemap.js#L1288](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1288)  
引入版本：3.0.0


---

### getObjectLayerNames {#getObjectLayerNames}

#### \<instance> getObjectLayerNames() {#instance-getobjectlayernames}


**说明:**

返回在此 Tilemap 中装入的所有有效对象组名称列表 。


**返回值:** Array.\<string> - 装入此 Tilemap 的有效对象组名称/ ID 的矩阵 。


> 源码：[src/tilemaps/Tilemap.js#L1305](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1305)  
引入版本：3.21.0


---

### getTileAt {#getTileAt}

#### \<instance> getTileAt(tileX, tileY, [nonNull], [layer]) {#instance-gettileattilex-tiley-nonnull-layer}


**说明:**

从给定的地层获得给定的地砖坐标的瓦片。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tileX | number | 否 |  | X 位置从( 以瓦片单位表示, 不以像素表示) 获取瓦片 。 |
| tileY | number | 否 |  | Y 位置从( 以瓦片单位表示, 而非像素) 得到瓦片 。 |
| nonNull | boolean | 是 | false | 对于空的牌,返回索引为 -1 的牌标对象,而不是空的牌标。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 |  | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 返回一个图案,如果给出的图层无效,则无效。


> 源码：[src/tilemaps/Tilemap.js#L1377](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1377)  
引入版本：3.0.0


---

### getTileAtWorldXY {#getTileAtWorldXY}

#### \<instance> getTileAtWorldXY(worldX, worldY, [nonNull], [camera], [layer]) {#instance-gettileatworldxyworldx-worldy-nonnull-camera-layer}


**说明:**

从给定的地层获得给定的世界坐标的瓦片。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| worldX | number | 否 |  | 从(以像素形式给出)获取瓦片的 X 位置 |
| worldY | number | 否 |  | Y 位置从 (以像素形式给出) 获取牌 |
| nonNull | boolean | 是 | false | 对于空的牌,返回索引为 -1 的牌标对象,而不是空的牌标。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 |  | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 |  | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 返回一个图案,如果给出的图层无效,则无效。


> 源码：[src/tilemaps/Tilemap.js#L1401](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1401)  
引入版本：3.0.0


---

### getTileCorners {#getTileCorners}

#### \<instance> getTileCorners(tileX, tileY, [camera], [layer]) {#instance-gettilecornerstilex-tiley-camera-layer}


**说明:**

返回一个矢量2的数组,每个条目对应所请求的瓦片的角。

`tileX`和`tileY`参数在瓦片坐标,而不是世界坐标.

角坐标位于世界空间,如果给出,则在TilemapLayer比例、位置和摄像机中计及。

阵列的大小会因地图的方向而异。 例如, 直径图将返回4个向量的阵列, 作为六边形图, 自然会返回6个角向量的阵列。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 返回矢量2的数组,如果给出的图层无效,则返回为无效。


> 源码：[src/tilemaps/Tilemap.js#L2572](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2572)  
引入版本：3.60.0


---

### getTileLayerNames {#getTileLayerNames}

#### \<instance> getTileLayerNames() {#instance-gettilelayernames}


**说明:**

返回在此 Tilemap 中装入的所有有效平板电脑名称列表 。


**返回值:** Array.\<string> - 装入此 Tilemap 的有效平板机名称/ ID 的矩阵 。


> 源码：[src/tilemaps/Tilemap.js#L1426](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1426)  
引入版本：3.21.0


---

### getTileset {#getTileset}

#### \<instance> getTileset(name) {#instance-gettilesetname}


**说明:**

获得带有给定的 `name` 的 Tilesset, 或者如果给出无效的 `name` 则无效 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 提勒斯特人的名字来得到。 |


**返回值:** [Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset) - 找不到匹配的名为 tileset 的 tileset 或 `null` 。


> 源码：[src/tilemaps/Tilemap.js#L1525](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1525)  
引入版本：3.14.0


---

### getTilesetIndex {#getTilesetIndex}

#### \<instance> getTilesetIndex(name) {#instance-gettilesetindexname}


**说明:**

获得this.tilesets内带有给定的`name`的提力键索引,如果给出无效的`name`,则无效。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 提勒斯特人的名字来得到。 |


**返回值:** number - this.tilesets内部的提列斯指数.


> 源码：[src/tilemaps/Tilemap.js#L1542](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1542)  
引入版本：3.0.0


---

### getTilesWithin {#getTilesWithin}

#### \<instance> getTilesWithin([tileX], [tileY], [width], [height], [filteringOptions], [layer]) {#instance-gettileswithintilex-tiley-width-height-filteringoptions-layer}


**说明:**

获取图层的指定矩形区域(在图砖坐标内)的瓦片。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 是 | 获得瓦片时可选择的过滤器。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 返回一个图案数组,如果给出的图层无效,则无效。


> 源码：[src/tilemaps/Tilemap.js#L1447](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1447)  
引入版本：3.0.0


---

### getTilesWithinShape {#getTilesWithinShape}

#### \<instance> getTilesWithinShape(shape, [filteringOptions], [camera], [layer]) {#instance-gettileswithinshapeshape-filteringoptions-camera-layer}


**说明:**

获取与指定图层中的形状重叠的牌。形状必须是圆形、线形、矩形或三角形。形状应在世界坐标中。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| shape | [Phaser.Geom.Circle](/api/class/geom-circle) \| [Phaser.Geom.Line](/api/class/geom-line) | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 世界的形状( 像素) 坐标 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 是 | 获得瓦片时可选择的过滤器。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用于计算返回的瓦片的摄像机。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 返回一个图案数组,如果给出的图层无效,则无效。


> 源码：[src/tilemaps/Tilemap.js#L1473](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1473)  
引入版本：3.0.0


---

### getTilesWithinWorldXY {#getTilesWithinWorldXY}

#### \<instance> getTilesWithinWorldXY(worldX, worldY, width, height, [filteringOptions], [camera], [layer]) {#instance-gettileswithinworldxyworldx-worldy-width-height-filteringoptions-camera-layer}


**说明:**

获取该层指定矩形区域(世界坐标)的瓦片.

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | 地球X坐标为该地区左上角. |
| worldY | number | 否 | 地球和坐标是该地区左上角 |
| width | number | 否 | 面积宽度. |
| height | number | 否 | 地区高度. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 是 | 获得瓦片时可选择的过滤器。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用于计算返回的瓦片的摄像机。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 返回一个图案数组,如果给出的图层无效,则无效。


> 源码：[src/tilemaps/Tilemap.js#L1498](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1498)  
引入版本：3.0.0


---

### hasTileAt {#hasTileAt}

#### \<instance> hasTileAt(tileX, tileY, [layer]) {#instance-hastileattilex-tiley-layer}


**说明:**

检查在给定的层中(在砖座坐标)的指定位置是否有一个瓦片。如果没有瓦片,或者该位置的瓦片有−1的索引,返回时会弄虚作假。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** boolean - 返回布尔值,如果给出的图层无效,则返回无效值。


> 源码：[src/tilemaps/Tilemap.js#L1558](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1558)  
引入版本：3.0.0


---

### hasTileAtWorldXY {#hasTileAtWorldXY}

#### \<instance> hasTileAtWorldXY(worldX, worldY, [camera], [layer]) {#instance-hastileatworldxyworldx-worldy-camera-layer}


**说明:**

检查指定位置( 世界坐标) 是否有瓦片。 如果没有瓦片, 或者该位置的瓦片有 - 1 的索引, 返回时会弄虚作假 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | x坐标,以像素表示. |
| worldY | number | 否 | y坐标,以像素表示. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用于计算返回的瓦片的摄像机。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** boolean - 返回布尔值,如果给出的图层无效,则返回无效值。


> 源码：[src/tilemaps/Tilemap.js#L1582](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1582)  
引入版本：3.0.0


---

### putTileAt {#putTileAt}

#### \<instance> putTileAt(tile, tileX, tileY, [recalculateFaces], [layer]) {#instance-puttileattile-tilex-tiley-recalculatefaces-layer}


**说明:**

在指定的地层中设置一个砖块坐标。您可以在索引或图块对象中传递。如果在图块中传递,所有属性都将复制到指定位置。如果在索引中通过,则只更改指定位置的索引。碰撞信息将在指定位置重新计算。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tile | number \| [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 此牌的索引可以设置或设置一个牌面对象。 |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| recalculateFaces | boolean | 是 | 如果面额数据应重新计算,则使用`true`。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 返回一个图案,如果给出的图层无效或坐标已超出界限,则返回为无效。


> 源码：[src/tilemaps/Tilemap.js#L1627](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1627)  
引入版本：3.0.0


---

### putTileAtWorldXY {#putTileAtWorldXY}

#### \<instance> putTileAtWorldXY(tile, worldX, worldY, [recalculateFaces], [camera], [layer]) {#instance-puttileatworldxytile-worldx-worldy-recalculatefaces-camera-layer}


**说明:**

在指定的层中设置一个瓦片,您可以在索引或图文对象中传递。如果在图文中通过,所有属性都将复制到指定位置。如果在索引中通过,则只更改指定位置的索引。碰撞信息将在指定位置重新计算。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tile | number \| [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 此牌的索引可以设置或设置一个牌面对象。 |
| worldX | number | 否 | x坐标,以像素表示. |
| worldY | number | 否 | y坐标,以像素表示. |
| recalculateFaces | boolean | 是 | 如果面额数据应重新计算,则使用`true`。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 返回一个图案,如果给出的图层无效,则无效。


> 源码：[src/tilemaps/Tilemap.js#L1657](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1657)  
引入版本：3.0.0


---

### putTilesAt {#putTilesAt}

#### \<instance> putTilesAt(tile, tileX, tileY, [recalculateFaces], [layer]) {#instance-puttilesattile-tilex-tiley-recalculatefaces-layer}


**说明:**

在指定的图片坐标上放置一个瓦片数组或一个2D的瓦片数组。该数组可以是瓦片索引或瓦片对象。如果在图片中通过,所有属性都将复制到指定位置。如果在索引中通过,则只更改指定位置的索引。碰撞信息将在区域牌块内重新计算。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tile | Array.\<number> \| Array.\<Array.\<number>> | Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> | Array.\<Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)>> | 否 | 铺设一个列( 阵列) 或格(2D 阵列) 的平面或瓦片索引。 |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| recalculateFaces | boolean | 是 | 如果面额数据应重新计算,则使用`true`。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此值, 如果给出的图层无效, 则返回此值或为无效 。


> 源码：[src/tilemaps/Tilemap.js#L1688](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1688)  
引入版本：3.0.0


---

### randomize {#randomize}

#### \<instance> randomize([tileX], [tileY], [width], [height], [indexes], [layer]) {#instance-randomizetilex-tiley-width-height-indexes-layer}


**说明:**

随机化指定层内一个长方形的瓦片区域(在瓦片坐标内)的索引。每个瓦片将获得一个新的索引。如果一个索引数组被传递进来,那么这些索引将被用于随机分配新的瓦片索引。如果不提供数组,则区域内发现的索引(不包括 -1)将被用于随机分配新的瓷片索引。这种方法只修改了瓦片索引,不会改变碰撞信息。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| indexes | Array.\<number> | 是 | 随机化过程中随机抽取的一系列索引. |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此值, 如果给出的图层无效, 则返回此值或为无效 。


> 源码：[src/tilemaps/Tilemap.js#L1721](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1721)  
引入版本：3.0.0


---

### removeAllLayers {#removeAllLayers}

#### \<instance> removeAllLayers() {#instance-removealllayers}


**说明:**

从此 Tilemap 中删除所有 Tilemap 层, 并调用 `destroy` 。


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 此 Tilemap 对象 。


> 源码：[src/tilemaps/Tilemap.js#L1887](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1887)  
引入版本：3.0.0


---

### removeLayer {#removeLayer}

#### \<instance> removeLayer([layer]) {#instance-removelayerlayer}


**说明:**

从 TilemapLayer 中删除给定的 TilemapLayer ,而不销毁它 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 拟移除的瓦片层. |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此值, 如果给出的图层无效, 则返回此值或为无效 。


> 源码：[src/tilemaps/Tilemap.js#L1809](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1809)  
引入版本：3.17.0


---

### removeTile {#removeTile}

#### \<instance> removeTile(tiles, [replaceIndex], [recalculateFaces]) {#instance-removetiletiles-replaceindex-recalculatefaces}


**说明:**

从所属于的层中去除给定的图案,或一系列图案,并可选地重新计算碰撞信息。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tiles | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) \| Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> | 否 |  | 要删除的图案, 或是一组图案。 |
| replaceIndex | number | 是 | -1 | 删除 tyle 后, 用给定索引插入一个全新的 tyle 位置。 离开 as - 1 即可删除 tyle 。 |
| recalculateFaces | boolean | 是 | true | 如果面额数据应重新计算,则使用`true`。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 返回已删除的图案。


> 源码：[src/tilemaps/Tilemap.js#L1914](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1914)  
引入版本：3.17.0


---

### removeTileAt {#removeTileAt}

#### \<instance> removeTileAt(tileX, tileY, [replaceWithNull], [recalculateFaces], [layer]) {#instance-removetileattilex-tiley-replacewithnull-recalculatefaces-layer}


**说明:**

删除指定层中砖块坐标的瓦片,并更新层碰撞信息。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| replaceWithNull | boolean | 是 | 如果 `true`(默认),这将用无效的砖块代替指定位置的砖块,而不是指数为 -1 的砖块。 |
| recalculateFaces | boolean | 是 | 如果 `true`(默认),面额数据会被重新计算. |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 返回已删除的图案,如果给出的图层无效,则返回为无效。


> 源码：[src/tilemaps/Tilemap.js#L1954](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1954)  
引入版本：3.0.0


---

### removeTileAtWorldXY {#removeTileAtWorldXY}

#### \<instance> removeTileAtWorldXY(worldX, worldY, [replaceWithNull], [recalculateFaces], [camera], [layer]) {#instance-removetileatworldxyworldx-worldy-replacewithnull-recalculatefaces-camera-layer}


**说明:**

删除指定世界坐标的瓦片,更新层碰撞信息。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | x坐标,以像素表示. |
| worldY | number | 否 | y坐标,以像素表示. |
| replaceWithNull | boolean | 是 | 如果 `true`(默认),这将用无效的砖块代替指定位置的砖块,而不是指数为 -1 的砖块。 |
| recalculateFaces | boolean | 是 | 如果 `true`(默认),面额数据会被重新计算. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 返回一个图案,如果给出的图层无效,则无效。


> 源码：[src/tilemaps/Tilemap.js#L1982](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L1982)  
引入版本：3.0.0


---

### renderDebug {#renderDebug}

#### \<instance> renderDebug(graphics, [styleConfig], [layer]) {#instance-renderdebuggraphics-styleconfig-layer}


**说明:**

绘制图层对给定图形对象的调试表示。 如果您想要快速了解您的哪些牌正在碰撞, 哪些牌有有趣的面孔, 这样做很有帮助。 这些牌从图形中绘制( 0 ) 开始, 允许您将调试表示放在屏幕上 。

省略图层时，使用瓦片地图的当前图层。

**注意:** 目前这种方法只与正交形的平面层配合.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 目标图形对象可以引用 。 |
| styleConfig | [Phaser.Types.Tilemaps.StyleConfig](/api/typedef/types-tilemaps#styleconfig) | 是 | 指定调试绘图所用的颜色的对象。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此 Tilemap 对象, 如果给出的图层无效, 则返回为无效 。


> 源码：[src/tilemaps/Tilemap.js#L2011](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2011)  
引入版本：3.0.0


---

### renderDebugFull {#renderDebugFull}

#### \<instance> renderDebugFull(graphics, [styleConfig]) {#instance-renderdebugfullgraphics-styleconfig}


**说明:**

绘制此 Tilemap 中所有图层的调试表示符到给定的图形对象。

如果您想快速了解您的牌是哪个在碰撞, 哪些有有趣的面孔, 这一点很有帮助。 这些牌从图形( 0 ) 开始绘制, 允许您在屏幕上设置调试代表 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 目标图形对象可以引用 。 |
| styleConfig | [Phaser.Types.Tilemaps.StyleConfig](/api/typedef/types-tilemaps#styleconfig) | 是 | 指定调试绘图所用的颜色的对象。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 提列玛普案


> 源码：[src/tilemaps/Tilemap.js#L2044](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2044)  
引入版本：3.17.0


---

### replaceByIndex {#replaceByIndex}

#### \<instance> replaceByIndex(findIndex, newIndex, [tileX], [tileY], [width], [height], [layer]) {#instance-replacebyindexfindindex-newindex-tilex-tiley-width-height-layer}


**说明:**

扫描给定的矩形区域(在平面坐标中给出),以匹配`findIndex`的索引来扫描瓦片,并更新其索引以匹配`newIndex`。这只修改索引,不会改变碰撞信息。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| findIndex | number | 否 | 查找的瓦片索引 。 |
| newIndex | number | 否 | 以瓦片代替的索引 。 |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此 Tilemap 对象, 如果给出的图层无效, 则返回为无效 。


> 源码：[src/tilemaps/Tilemap.js#L2071](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2071)  
引入版本：3.0.0


---

### setBaseTileSize {#setBaseTileSize}

#### \<instance> setBaseTileSize(tileWidth, tileHeight) {#instance-setbasetilesizetilewidth-tileheight}


**说明:**

设定地图的基片大小。 注意: 这不一定符合所有图层的 tileWidth 和 tileHeight 。 这也更新了所有图层上所有图层的基片大小 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileWidth | number | 否 | 用于计算地图的瓦片宽度。 |
| tileHeight | number | 否 | 地图用于计算时的瓦片高度。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 此 Tilemap 对象 。


> 源码：[src/tilemaps/Tilemap.js#L2347](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2347)  
引入版本：3.0.0


---

### setCollision {#setCollision}

#### \<instance> setCollision(indexes, [collides], [recalculateFaces], [layer], [updateLayer]) {#instance-setcollisionindexes-collides-recalculatefaces-layer-updatelayer}


**说明:**

将一个图片或牌片的碰撞按指数排列。 您可以通过一个单一的数字索引或一系列索引: [2、 3、 15、 20]。 `collides` 参数控制如果碰撞将被启用( 真实) 或禁用( 假) 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| indexes | number \| array | 否 |  | 或单瓦索引,或单瓦索引的数组。 |
| collides | boolean | 是 |  | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 是 |  | 更新后是否重新计算瓦片面孔 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 |  | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |
| updateLayer | boolean | 是 | true | 如果选中的话, 请更新层上的当前牌。 如果没有设置牌, 则设置为不实 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此 Tilemap 对象, 如果给出的图层无效, 则返回为无效 。


> 源码：[src/tilemaps/Tilemap.js#L2102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2102)  
引入版本：3.0.0


---

### setCollisionBetween {#setCollisionBetween}

#### \<instance> setCollisionBetween(start, stop, [collides], [recalculateFaces], [layer]) {#instance-setcollisionbetweenstart-stop-collides-recalculatefaces-layer}


**说明:**

设定一个图片的碰撞范围, 其指数介于指定的 `start`和 `stop`( 包括) 之间。 使用起始值为 10, 止值为 14 的图片, 将设置为 10、 11、 12、 13 和 14 的碰撞范围, 如果启用碰撞( 真实) 或 禁用( 假) , `collides` 参数控制会设置 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| start | number | 否 | 设定碰撞的瓦片的第一个索引. |
| stop | number | 否 | 设定碰撞的瓦片的最后一个索引 。 |
| collides | boolean | 是 | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 是 | 更新后是否重新计算瓦片面孔 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此 Tilemap 对象, 如果给出的图层无效, 则返回为无效 。


> 源码：[src/tilemaps/Tilemap.js#L2135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2135)  
引入版本：3.0.0


---

### setCollisionByExclusion {#setCollisionByExclusion}

#### \<instance> setCollisionByExclusion(indexes, [collides], [recalculateFaces], [layer]) {#instance-setcollisionbyexclusionindexes-collides-recalculatefaces-layer}


**说明:**

设定在给定的层中所有瓦片上的碰撞, 除了在给定数组中指定索引的瓦片。 如果启用碰撞( 真实) 或禁用( 假) , `collides` 参数控制。 目前未在层中使用的拖动索引不受影响 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| indexes | Array.\<number> | 否 | 一块砖索引的数组,不计算碰撞。 |
| collides | boolean | 是 | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 是 | 更新后是否重新计算瓦片面孔 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此 Tilemap 对象, 如果给出的图层无效, 则返回为无效 。


> 源码：[src/tilemaps/Tilemap.js#L2203](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2203)  
引入版本：3.0.0


---

### setCollisionByProperty {#setCollisionByProperty}

#### \<instance> setCollisionByProperty(properties, [collides], [recalculateFaces], [layer]) {#instance-setcollisionbypropertyproperties-collides-recalculatefaces-layer}


**说明:**

通过检查瓦片属性来设定一层内瓦片的碰撞。 如果瓦片具有与给定的属性对象匹配的属性, 则会设置其碰撞标志。 如果启用碰撞( 真实) 或禁用( 假) , 则 `collides` 参数控制。 在 `{ collides: true }` 中通过, 将会将任何砖片上的碰撞标志更新为具有真实值的“ collides ” 属性。 任何没有设置“ collide” 的瓦片都会被忽略。 您也可以使用一系列值, 如 `{ types: ["stone", "lava", "sand" ] }`。 如果一个瓦片具有与任何这些值匹配的“ 类型” 属性, 其碰撞标志将会被更新 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| properties | object | 否 | 具有瓦片属性和相应值的对象,应当检查。 |
| collides | boolean | 是 | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 是 | 更新后是否重新计算瓦片面孔 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此 Tilemap 对象, 如果给出的图层无效, 则返回为无效 。


> 源码：[src/tilemaps/Tilemap.js#L2168](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2168)  
引入版本：3.0.0


---

### setCollisionFromCollisionGroup {#setCollisionFromCollisionGroup}

#### \<instance> setCollisionFromCollisionGroup([collides], [recalculateFaces], [layer]) {#instance-setcollisionfromcollisiongroupcollides-recalculatefaces-layer}


**说明:**

将平板板上碰撞设定为一层内, 检查每块平板板板碰撞组数据( 一般在平板碰撞编辑器内在平板板板内定义) 。 如果在平板板板碰撞群内发现任何物体, 则会设置平板碰撞信息 。 如果启用碰撞( 真实) 或禁用( 假) , 则 `collides` 参数控制 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| collides | boolean | 是 | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 是 | 更新后是否重新计算瓦片面孔 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此 Tilemap 对象, 如果给出的图层无效, 则返回为无效 。


> 源码：[src/tilemaps/Tilemap.js#L2234](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2234)  
引入版本：3.0.0


---

### setLayer {#setLayer}

#### \<instance> setLayer([layer]) {#instance-setlayerlayer}


**说明:**

将当前图层设置为与 `layer` 相关的图层数据 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 图层的名称,图中的图层索引或图中的图层索引。如果不给定,则默认为图层索引。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 此 Tilemap 对象 。


> 源码：[src/tilemaps/Tilemap.js#L2325](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2325)  
引入版本：3.0.0


---

### setLayerTileSize {#setLayerTileSize}

#### \<instance> setLayerTileSize(tileWidth, tileHeight, [layer]) {#instance-setlayertilesizetilewidth-tileheight-layer}


**说明:**

设置一个特定的 `layer` 的瓦片大小 。 注意: 这不一定匹配所有图层的地图 tileWidth 和 tileHeight 。 这将设定图层的瓦片大小和图层的瓦片 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileWidth | number | 否 | 层中的瓦片宽度( 像素) 。 |
| tileHeight | number | 否 | 层中的瓦片高度(以像素计). |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 图层的名称,图中的图层索引或图中的图层索引。如果不给定,则默认为图层索引。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 此 Tilemap 对象 。


> 源码：[src/tilemaps/Tilemap.js#L2393](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2393)  
引入版本：3.0.0


---

### setRenderOrder {#setRenderOrder}

#### \<instance> setRenderOrder(renderOrder) {#instance-setrenderorderrenderorder}


**说明:**

设置此地图中瓦片的渲染( draw) 顺序 。

默认为“ 右下方 ” , 意思是它会命令从左上方开始的牌, 向右画, 然后移动到下一行 。

抽签命令如下:

0=右下 1=左下 2=右上 3=左下 1=左下 1=左下 1=左下 1=左下 1=左下 1=左下 1=左下 1=左下 1=左下 1=右下 2=右上 3=左下 1=左下 1=左下 3=左下 1=左下 3=左下 1=左下 3=左下 3=左下 3 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右

设定渲染顺序不会改变瓦片或如何将瓦片储存在地层中,它会完全影响其渲染顺序.

既可以提供整数(0至3),也可以提供顺序的字符串版本.

调用此方法_ after_ 创建 Tilemap 层将 ** 不** 自动更新它们, 以使用新的渲染顺序。 如果您在创建层后调用此方法, 请使用自己的 `setRenderOrder` 方法来修改它们 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderOrder | number \| string | 否 | 渲染(draw) 顺序值。 或整数在 0 到 3 之间, 或字符串 : “ 右下” 、 “ 左下” 、 “ 右上” 或 “ 左上” 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 此 Tilemap 对象 。


> 源码：[src/tilemaps/Tilemap.js#L323](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L323)  
引入版本：3.12.0


---

### setTileIndexCallback {#setTileIndexCallback}

#### \<instance> setTileIndexCallback(indexes, callback, callbackContext, [layer]) {#instance-settileindexcallbackindexes-callback-callbackcontext-layer}


**说明:**

设置层内给定的瓦片索引的全局碰撞调用。 这将影响此层上所有具有相同索引的瓦片。 如果为瓦片索引设置了调用调用调用调取调用调用调用的调用调用调试调用调用调制调用调用调出调用调用调出的调用调用调色调用调用调用了调用调用调减减调用调用调的调用调用调就可以看到 `setTileLocationCallback` 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| indexes | number \| Array.\<number> | 否 | 单瓦索引,或一组瓦索引,可以设定碰撞回调。所有值都应该是整数。 |
| callback | function | 否 | 当瓦片被碰撞时将引用的回调 。 |
| callbackContext | object | 否 | 调用时的上下文 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此 Tilemap 对象, 如果给出的图层无效, 则返回为无效 。


> 源码：[src/tilemaps/Tilemap.js#L2265](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2265)  
引入版本：3.0.0


---

### setTileLocationCallback {#setTileLocationCallback}

#### \<instance> setTileLocationCallback(tileX, tileY, width, height, callback, [callbackContext], [layer]) {#instance-settilelocationcallbacktilex-tiley-width-height-callback-callbackcontext-layer}


**说明:**

设置层内给定的矩形区域( 平面坐标) 的碰撞调用。 如果已经为平面索引设置了调用调用调用调取, 则将替换。 设置调用调用调用的调用调用调出调用调用调减调取调用调用补间 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 否 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 否 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 否 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| callback | function | 否 | 当瓦片被碰撞时将引用的回调 。 |
| callbackContext | object | 是 | 调用时的上下文 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此 Tilemap 对象, 如果给出的图层无效, 则返回为无效 。


> 源码：[src/tilemaps/Tilemap.js#L2294](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2294)  
引入版本：3.0.0


---

### shuffle {#shuffle}

#### \<instance> shuffle([tileX], [tileY], [width], [height], [layer]) {#instance-shuffletilex-tiley-width-height-layer}


**说明:**

在指定的层内, 将牌片划入长方形区域( 以瓦片坐标表示) 。 它只会随机排列该区域的牌片, 所以如果它们都一样, 似乎不会改变 ! 这种方法只会修改瓦片索引, 并且不会改变碰撞信息 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此 Tilemap 对象, 如果给出的图层无效, 则返回为无效 。


> 源码：[src/tilemaps/Tilemap.js#L2436](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2436)  
引入版本：3.0.0


---

### swapByIndex {#swapByIndex}

#### \<instance> swapByIndex(tileA, tileB, [tileX], [tileY], [width], [height], [layer]) {#instance-swapbyindextilea-tileb-tilex-tiley-width-height-layer}


**说明:**

扫描给定的矩形区域(在平面坐标中显示),以匹配`indexA`的索引来扫描瓦片,然后与`indexB`交换。这只修改索引,不会改变碰撞信息。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileA | number | 否 | 首张瓦片索引. |
| tileB | number | 否 | 第二瓦指数. |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此 Tilemap 对象, 如果给出的图层无效, 则返回为无效 。


> 源码：[src/tilemaps/Tilemap.js#L2466](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2466)  
引入版本：3.0.0


---

### tileToWorldX {#tileToWorldX}

#### \<instance> tileToWorldX(tileX, [camera], [layer]) {#instance-tiletoworldxtilex-camera-layer}


**说明:**

从平面X坐标(平面单位)转换为世界X坐标(像素),在层位,尺度和卷轴中进行计数.

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** number - 返回一个数字,如果给定的图层无效,则返回为无效。


> 源码：[src/tilemaps/Tilemap.js#L2497](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2497)  
引入版本：3.0.0


---

### tileToWorldXY {#tileToWorldXY}

#### \<instance> tileToWorldXY(tileX, tileY, [vec2], [camera], [layer]) {#instance-tiletoworldxytilex-tiley-vec2-camera-layer}


**说明:**

从平面的 XY 坐标( 平面单位) 转换为世界 XY 坐标( 像素), 以层位、 缩放和滚动为因数。 这将返回一个新的矢量2 对象或更新给定的 `point` 对象 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| vec2 | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储坐标的矢量2。 如果未给定新的矢量2, 则创建 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 返回矢量2, 如果给出的图层无效, 则返回无效 。


> 源码：[src/tilemaps/Tilemap.js#L2545](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2545)  
引入版本：3.0.0


---

### tileToWorldY {#tileToWorldY}

#### \<instance> tileToWorldY(tileY, [camera], [layer]) {#instance-tiletoworldytiley-camera-layer}


**说明:**

从瓦片 Y 坐标( 平面单位) 转换为世界 Y 坐标( 像素), 以层位、 缩放和滚动为因数 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** number - 返回一个数字,如果给定的图层无效,则返回为无效。


> 源码：[src/tilemaps/Tilemap.js#L2521](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2521)  
引入版本：3.0.0


---

### weightedRandomize {#weightedRandomize}

#### \<instance> weightedRandomize(weightedIndexes, [tileX], [tileY], [width], [height], [layer]) {#instance-weightedrandomizeweightedindexes-tilex-tiley-width-height-layer}


**说明:**

随机化指定层内一个矩形的瓦片区域(在瓦片坐标内)的索引。每个瓦片将获得一个新的索引。新的索引是从给定的 weightedIndexes 阵列中抽取的。一个加权数组的例子:

[{指数:6,重量:4},//指数6的概率为4/8{指数:7,重量:2},/指数7的概率为2/8{指数:8,重量:1.5},/指数8的概率为1.5/8{指数:26,重量:0.5}/指数26的概率为0.5/8]].

选择任何索引的概率是(指数权重) /(所有权重的总和) 。 这种方法只修改了瓦片索引, 并且不会改变碰撞信息 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| weightedIndexes | Array.\<object> | 否 | 随机化过程中随机抽取的一组对象。 其形式应该是 : { 指数: 0, 重量: 4} 或{ 指数: [0], 重量: 4( 如果您想从多块的索引中抽取 ) 。 |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 返回此 Tilemap 对象, 如果给出的图层无效, 则返回为无效 。


> 源码：[src/tilemaps/Tilemap.js#L2605](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2605)  
引入版本：3.0.0


---

### worldToTileX {#worldToTileX}

#### \<instance> worldToTileX(worldX, [snapToFloor], [camera], [layer]) {#instance-worldtotilexworldx-snaptofloor-camera-layer}


**说明:**

从世界 X 坐标(像素)转换为瓦片 X坐标(瓦单位),在层位,尺度和卷轴中进行计分.

省略图层时，使用瓦片地图的当前图层。

使用这种方法不能叫做Isometric或六边形瓦片,因为它们要求`worldX`和`worldY`值都能够确定正确的瓦片,相反,你应该使用`worldToTileXY`方法。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | 要转换的x坐标,以像素表示,而不是用瓦片表示. |
| snapToFloor | boolean | 是 | 是否将平板坐标向下折叠到最近的整数 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** number - 返回一个数字,如果给定的图层无效,则返回为无效。


> 源码：[src/tilemaps/Tilemap.js#L2645](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2645)  
引入版本：3.0.0


---

### worldToTileXY {#worldToTileXY}

#### \<instance> worldToTileXY(worldX, worldY, [snapToFloor], [vec2], [camera], [layer]) {#instance-worldtotilexyworldx-worldy-snaptofloor-vec2-camera-layer}


**说明:**

从世界 XY 坐标( 像素) 转换为平面 XY 坐标( 平面单位), 以图层位置、 缩放和滚动为因数。 这将返回一个新的矢量2 对象或更新给定的 `point` 对象 。

省略图层时，使用瓦片地图的当前图层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | 要转换的x坐标,以像素表示,而不是用瓦片表示. |
| worldY | number | 否 | 转换的y坐标,以像素表示,而不是瓦片. |
| snapToFloor | boolean | 是 | 是否将平板坐标向下折叠到最近的整数 。 |
| vec2 | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储坐标的矢量2。 如果未给定新的矢量2, 则创建 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 返回矢量2, 如果给出的图层无效, 则返回无效 。


> 源码：[src/tilemaps/Tilemap.js#L2703](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2703)  
引入版本：3.0.0


---

### worldToTileY {#worldToTileY}

#### \<instance> worldToTileY(worldY, [snapToFloor], [camera], [layer]) {#instance-worldtotileyworldy-snaptofloor-camera-layer}


**说明:**

从世界Y坐标(像素)转换为瓦片Y坐标(瓦片单位),在层位,尺度和卷轴中进行计分.

省略图层时，使用瓦片地图的当前图层。

使用这种方法不能叫做Isometric或六边形瓦片,因为它们要求`worldX`和`worldY`值都能够确定正确的瓦片,相反,你应该使用`worldToTileXY`方法。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldY | number | 否 | 转换的y坐标,以像素表示,而不是瓦片. |
| snapToFloor | boolean | 是 | 是否将平板坐标向下折叠到最近的整数 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | string \| number | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


**返回值:** number - 返回一个数字,如果给定的图层无效,则返回为无效。


> 源码：[src/tilemaps/Tilemap.js#L2674](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tilemap.js#L2674)  
引入版本：3.0.0


---

---
