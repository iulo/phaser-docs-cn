# LayerData {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tilemaps-layerdata)

将所有与单层相关的数据存储在平面图中。当从 CSV, Tiled JSON 或其他格式解析地图时,每个平面图层会转换成一个图层Data 实例,该实例将具有平面格、层尺寸、方向、能见度、物理体、平面回调以及编辑器中定义的任何自定义属性。

`Tilemap`和`TilemapLayer`都持有TyerleData的参考文献,并用它来查查瓦片位置,进行碰撞检查,并驱动渲染.

**构造函数**

`new LayerData([config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Tilemaps.LayerDataConfig](/api/typedef/types-tilemaps#layerdataconfig) | 是 | 层数据配置对象 。 |

---


**作用域**: static

> 源码：[src/tilemaps/mapdata/LayerData.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L11)  
引入版本：3.0.0

## 公开成员 {#public-members}

### alpha {#alpha}

#### alpha: number {#alpha-number}


**说明:**

层的α值.


> 源码：[src/tilemaps/mapdata/LayerData.js#L159](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L159)  
引入版本：3.0.0


---

### baseTileHeight {#baseTileHeight}

#### baseTileHeight: number {#basetileheight-number}


**说明:**

基片高度, 以像素为单位。 这是地图级别上定义的瓦片高度, 用于计算像素坐标和层尺寸。 它默认为 `tileHeight`, 但对于使用与地图默认不同的瓦片大小的层来说可能有所不同 。


> 源码：[src/tilemaps/mapdata/LayerData.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L121)  
引入版本：3.0.0


---

### baseTileWidth {#baseTileWidth}

#### baseTileWidth: number {#basetilewidth-number}


**说明:**

基片宽度, 以像素为单位。 这是地图级别上定义的瓦片宽度, 用于计算像素坐标和层尺寸。 它默认为 `tileWidth`, 但对于使用与地图默认不同的瓦片大小的层来说可能有所不同 。


> 源码：[src/tilemaps/mapdata/LayerData.js#L110](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L110)  
引入版本：3.0.0


---

### bodies {#bodies}

#### bodies: array {#bodies-array}


**说明:**

一系列物理体.


> 源码：[src/tilemaps/mapdata/LayerData.js#L215](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L215)  
引入版本：3.0.0


---

### callbacks {#callbacks}

#### callbacks: array {#callbacks-array}


**说明:**

已注册的此层的瓦片位置调用数组。 每个条目将一个瓦片索引映射到一个调用函数, 当物理驱动的游戏对象与该瓦片重叠或相撞时, 将引用该函数 。


> 源码：[src/tilemaps/mapdata/LayerData.js#L204](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L204)  
引入版本：3.0.0


---

### collideIndexes {#collideIndexes}

#### collideIndexes: array {#collideindexes-array}


**说明:**

拼接式碰撞ID索引地图.


> 源码：[src/tilemaps/mapdata/LayerData.js#L195](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L195)  
引入版本：3.0.0


---

### data {#data}

#### data: Array.\<Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)>> {#data-arrayarrayphasertilemapstile}


**说明:**

代表此层的瓦格网格的 2D 对象阵列。 索引为 `data[row][col]`, 每个条目都是一个图案实例( 或空单元格无效) 。


> 源码：[src/tilemaps/mapdata/LayerData.js#L224](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L224)  
引入版本：3.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

层层的高度以瓦片计.


> 源码：[src/tilemaps/mapdata/LayerData.js#L83](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L83)  
引入版本：3.0.0


---

### heightInPixels {#heightInPixels}

#### heightInPixels: number {#heightinpixels-number}


**说明:**

整个层的高度以像素表示.


> 源码：[src/tilemaps/mapdata/LayerData.js#L150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L150)  
引入版本：3.0.0


---

### hexSideLength {#hexSideLength}

#### hexSideLength: number {#hexsidelength-number}


**说明:**

六边形的横向侧面长度,仅用于六边形方向 Tilemaps.


> 源码：[src/tilemaps/mapdata/LayerData.js#L243](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L243)  
引入版本：3.50.0


---

### id {#id}

#### id: number {#id-number}


**说明:**

地图数据中指定的层的 id 。

注意: 这不是地图数据中层的索引,而是其实际的ID在平面上.


> 源码：[src/tilemaps/mapdata/LayerData.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L45)  
引入版本：3.70.0


---

### indexes {#indexes}

#### indexes: array {#indexes-array}


**说明:**

拼贴ID索引地图.


> 源码：[src/tilemaps/mapdata/LayerData.js#L186](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L186)  
引入版本：3.0.0


---

### name {#name}

#### name: string {#name-string}


**说明:**

如果在 Tiled 中指定,则图层的名称 。


> 源码：[src/tilemaps/mapdata/LayerData.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L36)  
引入版本：3.0.0


---

### orientation {#orientation}

#### orientation: [Phaser.Tilemaps.OrientationType](/api/typedef/tilemaps#orientationtype) {#orientation-phasertilemapsorientationtype}


**说明:**

层的定向,是能够确定一个瓦片的pixelX和pixelY以及层的宽度和高度所必需.


> 源码：[src/tilemaps/mapdata/LayerData.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L132)  
引入版本：3.50.0


---

### properties {#properties}

#### properties: Array.\<object> {#properties-arrayobject}


**说明:**

层特定属性(可以在平面中指定).


> 源码：[src/tilemaps/mapdata/LayerData.js#L177](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L177)  
引入版本：3.0.0


---

### staggerAxis {#staggerAxis}

#### staggerAxis: string {#staggeraxis-string}


**说明:**

斜拉线中定义的 Stagger 轴 。

仅用于六边形定向Tilemaps.


> 源码：[src/tilemaps/mapdata/LayerData.js#L253](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L253)  
引入版本：3.60.0


---

### staggerIndex {#staggerIndex}

#### staggerIndex: string {#staggerindex-string}


**说明:**

斜拉线中定义的 Stagger 索引 。

要么"odd"要么"even".

仅用于六边形定向Tilemaps.


> 源码：[src/tilemaps/mapdata/LayerData.js#L264](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L264)  
引入版本：3.60.0


---

### tileHeight {#tileHeight}

#### tileHeight: number {#tileheight-number}


**说明:**

瓦片的像素高度.


> 源码：[src/tilemaps/mapdata/LayerData.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L101)  
引入版本：3.0.0


---

### tilemapLayer {#tilemapLayer}

#### tilemapLayer: [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) {#tilemaplayer-phasertilemapstilemaplayer}


**说明:**

引用拥有此数据的 Tilemap 层 。


> 源码：[src/tilemaps/mapdata/LayerData.js#L234](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L234)  
引入版本：3.0.0


---

### tileWidth {#tileWidth}

#### tileWidth: number {#tilewidth-number}


**说明:**

瓦片的像素宽度.


> 源码：[src/tilemaps/mapdata/LayerData.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L92)  
引入版本：3.0.0


---

### visible {#visible}

#### visible: boolean {#visible-boolean}


**说明:**

层层是否可见?


> 源码：[src/tilemaps/mapdata/LayerData.js#L168](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L168)  
引入版本：3.0.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

以瓦片计的层宽度 。


> 源码：[src/tilemaps/mapdata/LayerData.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L74)  
引入版本：3.0.0


---

### widthInPixels {#widthInPixels}

#### widthInPixels: number {#widthinpixels-number}


**说明:**

整个层的宽度像素.


> 源码：[src/tilemaps/mapdata/LayerData.js#L141](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L141)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

左上方的 x 偏移到何处 。


> 源码：[src/tilemaps/mapdata/LayerData.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L56)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

从左上方抽出哪里的 Y 乘以 。


> 源码：[src/tilemaps/mapdata/LayerData.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/LayerData.js#L65)  
引入版本：3.0.0


---

---
