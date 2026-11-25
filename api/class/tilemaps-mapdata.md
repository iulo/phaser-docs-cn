# MapData {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tilemaps-mapdata)

用于表示地图数据的一个类。 地图是从 CSV 、 平面等解析到此格式的。 平面对象得到此数据的复制件, 然后将所需的属性解开为它本身 。

**构造函数**

`new MapData([config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Tilemaps.MapDataConfig](/api/typedef/types-tilemaps#mapdataconfig) | 是 | 映射配置对象 。 |

---


**作用域**: static

> 源码：[src/tilemaps/mapdata/MapData.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L11)  
引入版本：3.0.0

## 公开成员 {#public-members}

### collision {#collision}

#### collision: object {#collision-object}


**说明:**

包含地图碰撞数据的对象。 只有在地图被启用物理系统时才被覆盖 。


> 源码：[src/tilemaps/mapdata/MapData.js#L187](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L187)  
引入版本：3.0.0


---

### format {#format}

#### format: number {#format-number}


**说明:**

地图数据的格式.


> 源码：[src/tilemaps/mapdata/MapData.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L104)  
引入版本：3.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

整个瓦片的高度,用瓦片表示.


> 源码：[src/tilemaps/mapdata/MapData.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L50)  
引入版本：3.0.0


---

### heightInPixels {#heightInPixels}

#### heightInPixels: number {#heightinpixels-number}


**说明:**

整个瓦片的高度以像素表示.


> 源码：[src/tilemaps/mapdata/MapData.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L95)  
引入版本：3.0.0


---

### hexSideLength {#hexSideLength}

#### hexSideLength: number {#hexsidelength-number}


**说明:**

六边形的横向侧长.

仅用于六边形定向Tilemaps.


> 源码：[src/tilemaps/mapdata/MapData.js#L223](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L223)  
引入版本：3.50.0


---

### imageCollections {#imageCollections}

#### imageCollections: array {#imagecollections-array}


**说明:**

地图使用的图像的收集(用斜拉图表示).


> 源码：[src/tilemaps/mapdata/MapData.js#L205](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L205)  
引入版本：3.0.0


---

### images {#images}

#### images: array {#images-array}


**说明:**

平面图像层的阵列 。


> 源码：[src/tilemaps/mapdata/MapData.js#L163](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L163)  
引入版本：3.0.0


---

### infinite {#infinite}

#### infinite: boolean {#infinite-boolean}


**说明:**

若图无穷无尽.


> 源码：[src/tilemaps/mapdata/MapData.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L59)  
引入版本：3.17.0


---

### layers {#layers}

#### layers: Array.\<[Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata)>, [Phaser.Tilemaps.ObjectLayer](/api/class/tilemaps-objectlayer) {#layers-arrayphasertilemapslayerdata-phasertilemapsobjectlayer}


**说明:**

属于此 MapData 的所有图层的阵列。


> 源码：[src/tilemaps/mapdata/MapData.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L154)  
引入版本：3.0.0


---

### name {#name}

#### name: string {#name-string}


**说明:**

Phaser缓存中对应已装入的图片数据的键.


> 源码：[src/tilemaps/mapdata/MapData.js#L32](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L32)  
引入版本：3.0.0


---

### objects {#objects}

#### objects: Array.\<[Phaser.Types.Tilemaps.ObjectLayerConfig](/api/typedef/types-tilemaps#objectlayerconfig)> {#objects-arrayphasertypestilemapsobjectlayerconfig}


**说明:**

平面对象层的阵列 。


> 源码：[src/tilemaps/mapdata/MapData.js#L172](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L172)  
引入版本：3.0.0


---

### orientation {#orientation}

#### orientation: [Phaser.Tilemaps.OrientationType](/api/typedef/tilemaps#orientationtype) {#orientation-phasertilemapsorientationtype}


**说明:**

地图数据(即正对角、异构、六边形)的方向,默认的“正对角”。


> 源码：[src/tilemaps/mapdata/MapData.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L113)  
引入版本：3.50.0


---

### properties {#properties}

#### properties: object {#properties-object}


**说明:**

映射特定属性( 可以在 Tiled 中指定) 。


> 源码：[src/tilemaps/mapdata/MapData.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L145)  
引入版本：3.0.0


---

### renderOrder {#renderOrder}

#### renderOrder: string {#renderorder-string}


**说明:**

确定图片的绘图顺序。默认为右下。

0,或"右下"1,或"左下"2,或"右上"3,或"左上"


> 源码：[src/tilemaps/mapdata/MapData.js#L122](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L122)  
引入版本：3.12.0


---

### staggerAxis {#staggerAxis}

#### staggerAxis: string {#staggeraxis-string}


**说明:**

斜拉线中定义的 Stagger 轴 。

仅用于六边形定向Tilemaps.


> 源码：[src/tilemaps/mapdata/MapData.js#L234](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L234)  
引入版本：3.60.0


---

### staggerIndex {#staggerIndex}

#### staggerIndex: string {#staggerindex-string}


**说明:**

斜拉线中定义的 Stagger 索引 。

要么"odd"要么"even".

仅用于六边形定向Tilemaps.


> 源码：[src/tilemaps/mapdata/MapData.js#L245](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L245)  
引入版本：3.60.0


---

### tileHeight {#tileHeight}

#### tileHeight: number {#tileheight-number}


**说明:**

瓦片的高度,以像素表示.


> 源码：[src/tilemaps/mapdata/MapData.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L77)  
引入版本：3.0.0


---

### tiles {#tiles}

#### tiles: array {#tiles-array}


**说明:**

一系列的瓦片实例。


> 源码：[src/tilemaps/mapdata/MapData.js#L214](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L214)  
引入版本：3.0.0


---

### tilesets {#tilesets}

#### tilesets: Array.\<[Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset)> {#tilesets-arrayphasertilemapstileset}


**说明:**

一系列的提列赛特。


> 源码：[src/tilemaps/mapdata/MapData.js#L196](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L196)  
引入版本：3.0.0


---

### tileWidth {#tileWidth}

#### tileWidth: number {#tilewidth-number}


**说明:**

瓦片的宽度,以像素表示.


> 源码：[src/tilemaps/mapdata/MapData.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L68)  
引入版本：3.0.0


---

### version {#version}

#### version: string {#version-string}


**说明:**

地图数据的版本(如图案所指定).


> 源码：[src/tilemaps/mapdata/MapData.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L136)  
引入版本：3.0.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

整个瓦片的宽度,以瓦片表示.


> 源码：[src/tilemaps/mapdata/MapData.js#L41](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L41)  
引入版本：3.0.0


---

### widthInPixels {#widthInPixels}

#### widthInPixels: number {#widthinpixels-number}


**说明:**

整个平面的宽度以像素表示.


> 源码：[src/tilemaps/mapdata/MapData.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/MapData.js#L86)  
引入版本：3.0.0


---

---
