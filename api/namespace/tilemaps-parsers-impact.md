# Phaser.Tilemaps.Parsers.Impact {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/tilemaps-parsers-impact)

Scope: 
static
> 源码：[src/tilemaps/parsers/impact/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/impact/index.js#L7)  


## 静态函数 {#static-functions}

### ParseTileLayers {#ParseTileLayers}

#### \<static> ParseTileLayers(json, insertNull) {#static-parsetilelayersjson-insertnull}


**说明:**

将撞击 JSON 对象中的所有图片层都分析成新的LayerData 对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| json | object | 否 | 撞击JSON对象。 |
| insertNull | boolean | 否 | 控制层数据中空牌( 索引为 - 1 的) 如何存储。 如果 `true`, 空牌位置则以 `null` 的形式存储。 如果 `false` , 则为每个空位创建索引为 - 1 的一个牌对象 。 |


**返回值:** Array.\<[Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata)> - - 一系列图层数据对象,每个条目一个

json. layer. 杀人犯 杀人犯


> 源码：[src/tilemaps/parsers/impact/ParseTileLayers.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/impact/ParseTileLayers.js#L10)  
引入版本：3.0.0


---

### ParseTilesets {#ParseTilesets}

#### \<static> ParseTilesets(json) {#static-parsetilesetsjson}


**说明:**

将撞击( Weltmeister) 的图片所有独特的图片标注为 Tileset 对象, 并把它们作为一系列的图片返回。 JSON 中的每个图层都被检查为图片名称; 重复名称和碰撞层( 带有空白的图片名称) 被忽略。 撞击图片中的图片标识相对于图片标注而非全球独有的, 并且图片没有边距或加挂, 所以每个图片的值被设定为零 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| json | object | 否 | 影响JSON数据. |


**返回值:** array - 一系列的提列赛特。


> 源码：[src/tilemaps/parsers/impact/ParseTilesets.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/impact/ParseTilesets.js#L9)  
引入版本：3.0.0


---

### ParseWeltmeister {#ParseWeltmeister}

#### \<static> ParseWeltmeister(name, json, insertNull) {#static-parseweltmeistername-json-insertnull}


**说明:**

将一个Weltmeister JSON对象分析成一个新的 MapData 对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 拼图的名称,用于在 MapData 上设置名称. |
| json | object | 否 | 韦特梅斯特·杰森天体. |
| insertNull | boolean | 否 | 控制如何处理地图数据中的空牌, 带有 -1 索引的牌。 如果 `true`, 空位置将获得 `null` 值。 如果 `false` , 空位置将得到一个带有 - 1 索引的牌对象, 如果您有大片人烟稀少的地图, 牌块数据不需要更改, 那么设置这个值到 `true` 将会帮助内存消耗。 但是, 如果您的地图很小, 或者您需要动态更新牌, 那么留下默认值设定 。 |


**返回值:** [Phaser.Tilemaps.MapData](/api/class/tilemaps-mapdata) - 创建的 MapData 对象, 或 `null` 如果数据无法解析 。


> 源码：[src/tilemaps/parsers/impact/ParseWeltmeister.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/impact/ParseWeltmeister.js#L12)  
引入版本：3.0.0


---

---
