# Phaser.Tilemaps {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/tilemaps)

Scope: 
static
> 源码：[src/tilemaps/index.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/index.js#L10)  


## 静态函数 {#static-functions}

- [ImageCollection](/api/class/tilemaps-imagecollection)
- [LayerData](/api/class/tilemaps-layerdata)
- [MapData](/api/class/tilemaps-mapdata)
- [ObjectHelper](/api/class/tilemaps-objecthelper)
- [ObjectLayer](/api/class/tilemaps-objectlayer)
- [Tile](/api/class/tilemaps-tile)
- [Tilemap](/api/class/tilemaps-tilemap)
- [TilemapGPULayer](/api/class/tilemaps-tilemapgpulayer)
- [TilemapLayer](/api/class/tilemaps-tilemaplayer)
- [TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase)
- [Tileset](/api/class/tilemaps-tileset)
## 静态函数 {#static-functions-1}

- [Components](/api/namespace/tilemaps-components)
- [Formats](/api/namespace/tilemaps-formats)
- [Orientation](/api/namespace/tilemaps-orientation)
- [Parsers](/api/namespace/tilemaps-parsers)
## 静态函数 {#static-functions-2}

### OrientationType {#OrientationType}

#### OrientationType {#orientationtype}


**说明:**

Phaser 提列玛普常数用于定向.

要了解每种模式都做些什么,请参见[Phaser.Tilemaps.Orientation](/api/namespace/tilemaps-orientation).


> 源码：[src/tilemaps/const/ORIENTATION_CONST.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/const/ORIENTATION_CONST.js#L15)  
引入版本：3.50.0


---

## 静态函数 {#static-functions-3}

### ParseToTilemap {#ParseToTilemap}

#### \<static> ParseToTilemap(scene, [key], [tileWidth], [tileHeight], [width], [height], [data], [insertNull]) {#static-parsetotilemapscene-key-tilewidth-tileheight-width-height-data-insertnull}


**说明:**

从给定的密钥或数据创建 Tilemap。 如果给定的密钥或数据都没有, 请将 Tilemap 改为空白。 从 CSV 或 2D 阵列加载时, 您应该指定 tileWidth & tileHeight。从图中解析时, tileWidth, tileHeight,宽度和高度将从地图数据中拉出。对于空地图,您应当指定 tileWidth, tileHeight,宽度和高度。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 蒂莱玛普属于的场景. |
| key | string | 是 |  | Phaser缓存中对应已装入的图片数据的密钥. |
| tileWidth | number | 是 | 32 | 以像素表示的瓦片宽度 。 |
| tileHeight | number | 是 | 32 | 瓦片在像素中的高度. |
| width | number | 是 | 10 | 以瓦片计的地图宽度 。 |
| height | number | 是 | 10 | 地图的高度,以瓷砖计. |
| data | Array.\<Array.\<number>> | 是 |  | 与其从缓存中加载,还可以直接从2D的片片索引中加载. |
| insertNull | boolean | 是 | false | 控制如何处理地图数据中的空牌, 索引为 - 1 的牌。 如果 `true`, 空位置将获得 `null` 的值。 如果 `false` , 空位置将得到索引为 - 1 的一个牌对象, 如果您有大片的地图, 而牌块数据不需要更改, 那么设置这个值为 `true` 将会帮助内存消耗。 然而, 如果您的地图很小, 或者您需要动态更新牌, 那么就留下默认值设定 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 从给定数据创建的 Tilemap 对象 。


> 源码：[src/tilemaps/ParseToTilemap.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ParseToTilemap.js#L12)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-4}

### HEXAGONAL {#HEXAGONAL}

#### HEXAGONAL: number {#hexagonal-number}


**说明:**

六角斜拉图方向常数.


> 源码：[src/tilemaps/const/ORIENTATION_CONST.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/const/ORIENTATION_CONST.js#L57)  
引入版本：3.50.0


---

### ISOMETRIC {#ISOMETRIC}

#### ISOMETRIC: number {#isometric-number}


**说明:**

偏振式斜拉线定向常数.


> 源码：[src/tilemaps/const/ORIENTATION_CONST.js#L37](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/const/ORIENTATION_CONST.js#L37)  
引入版本：3.50.0


---

### ORTHOGONAL {#ORTHOGONAL}

#### ORTHOGONAL: number {#orthogonal-number}


**说明:**

斜斜拉线定向常数.


> 源码：[src/tilemaps/const/ORIENTATION_CONST.js#L27](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/const/ORIENTATION_CONST.js#L27)  
引入版本：3.50.0


---

### STAGGERED {#STAGGERED}

#### STAGGERED: number {#staggered-number}


**说明:**

错位的 Tilemap 方向常数 。


> 源码：[src/tilemaps/const/ORIENTATION_CONST.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/const/ORIENTATION_CONST.js#L47)  
引入版本：3.50.0


---

---
