# Phaser.Tilemaps.Parsers {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/tilemaps-parsers)

Scope: 
static
> 源码：[src/tilemaps/parsers/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/index.js#L7)  


## 静态函数 {#static-functions}

### FromOrientationString {#FromOrientationString}

#### \<static> FromOrientationString([orientation]) {#static-fromorientationstringorientation}


**说明:**

将 Tilemap 方向字符串转换为相应的 `Phaser.Tilemaps.OrientationType` 。确认的值是 `'isometric'`, `'staggered'`,和 `'hexagonal'`。任何其他字符串,包括 `'orthogonal'`,将返回正向方向常数,这是大多数图列虫使用的默认网格方向。

比较是忽略不计的。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| orientation | string | 是 | 方向类型作为字符串. |


**返回值:** [Phaser.Tilemaps.OrientationType](/api/typedef/tilemaps#orientationtype) - 蒂莱玛普方向类型 。


> 源码：[src/tilemaps/parsers/FromOrientationString.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/FromOrientationString.js#L9)  
引入版本：3.50.0


---

### Parse {#Parse}

#### \<static> Parse(name, mapFormat, data, tileWidth, tileHeight, insertNull) {#static-parsename-mapformat-data-tilewidth-tileheight-insertnull}


**说明:**

将给定的 Tilemap 格式的原始数据分析成一个新的 MapData 对象。 如果找不到公认的数据格式, 请返回 `null`。 从 CSV 或 2D 阵列加载时, 请指定 tileWidth 和 tileHeight 。 从 Tiled 地图中解析时, 将从地图数据中提取 tileWidth 和 tileHeight 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 拼图的名称,用于在 MapData 上设置名称. |
| mapFormat | number | 否 | 地图数据的格式。 必须是 `Phaser.Tilemaps.Formats` 常数之一, 如 `Phaser.Tilemaps.Formats.TILED_JSON` 。 |
| data | Array.\<Array.\<number>> \| string | object | 否 | 原始映射数据来解析。视格式的不同,一个2D的瓦片索引阵列、一个CSV字符串或一个平面 JSON对象。 |
| tileWidth | number | 否 | 像素中的瓦片宽度。 需要2D 阵列和 CSV, 但忽略了 Tiled JSON 。 |
| tileHeight | number | 否 | 像素中的瓦片高度。 需要2D 阵列和 CSV, 但忽略了 Tiled JSON 。 |
| insertNull | boolean | 否 | 控制如何处理地图数据中的空牌, 带有 -1 索引的牌。 如果 `true`, 空位置将获得 `null` 值。 如果 `false` , 空位置将得到一个带有 - 1 索引的牌对象, 如果您有大片人烟稀少的地图, 牌块数据不需要更改, 那么设置这个值到 `true` 将会帮助内存消耗。 但是, 如果您的地图很小, 或者您需要动态更新牌, 那么留下默认值设定 。 |


**返回值:** [Phaser.Tilemaps.MapData](/api/class/tilemaps-mapdata) - 创建的 `MapData` 对象,或 `null` 如果地图格式不被识别。


> 源码：[src/tilemaps/parsers/Parse.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/Parse.js#L13)  
引入版本：3.0.0


---

### Parse2DArray {#Parse2DArray}

#### \<static> Parse2DArray(name, data, tileWidth, tileHeight, insertNull) {#static-parse2darrayname-data-tilewidth-tileheight-insertnull}


**说明:**

将2D 组的瓦索引分析成一个新的 MapData 对象,并用一个单层。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 拼图的名称,用于在 MapData 上设置名称. |
| data | Array.\<Array.\<number>> | 否 | 砖块索引的2D 阵列。 |
| tileWidth | number | 否 | 以像素表示的瓦片宽度 。 |
| tileHeight | number | 否 | 瓦片在像素中的高度. |
| insertNull | boolean | 否 | 控制如何处理地图数据中的空牌, 索引为 - 1 的牌。 如果 `true`, 空位置将获得 `null` 的值。 如果 `false` , 空位置将得到索引为 - 1 的一个牌对象, 如果您有大片的地图, 而牌块数据不需要更改, 那么设置这个值为 `true` 将会帮助内存消耗。 然而, 如果您的地图很小, 或者您需要动态更新牌, 那么就留下默认值设定 。 |


**返回值:** [Phaser.Tilemaps.MapData](/api/class/tilemaps-mapdata) - MapData 对象。


> 源码：[src/tilemaps/parsers/Parse2DArray.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/Parse2DArray.js#L12)  
引入版本：3.0.0


---

### ParseCSV {#ParseCSV}

#### \<static> ParseCSV(name, data, tileWidth, tileHeight, insertNull) {#static-parsecsvname-data-tilewidth-tileheight-insertnull}


**说明:**

将一个 CSV 的瓦片索引串分析成新的具有单层的 MapData 对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 拼图的名称,用于在 MapData 上设置名称. |
| data | string | 否 | CSV 的瓦片索引串 。 |
| tileWidth | number | 否 | 以像素表示的瓦片宽度 。 |
| tileHeight | number | 否 | 瓦片在像素中的高度. |
| insertNull | boolean | 否 | 控制如何处理地图数据中的空牌, 带有 -1 索引的牌。 如果 `true`, 空位置将获得 `null` 值。 如果 `false` , 空位置将得到一个带有 - 1 索引的牌对象, 如果您有大片人烟稀少的地图, 牌块数据不需要更改, 那么设置这个值到 `true` 将会帮助内存消耗。 但是, 如果您的地图很小, 或者您需要动态更新牌, 那么留下默认值设定 。 |


**返回值:** [Phaser.Tilemaps.MapData](/api/class/tilemaps-mapdata) - 由此产生的 MapData 对象 。


> 源码：[src/tilemaps/parsers/ParseCSV.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/ParseCSV.js#L10)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

- [Impact](/api/namespace/tilemaps-parsers-impact)
- [Tiled](/api/namespace/tilemaps-parsers-tiled)

---
