# Phaser.Tilemaps.Parsers.Tiled {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/tilemaps-parsers-tiled)

Scope: 
static
> 源码：[src/tilemaps/parsers/tiled/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/tiled/index.js#L7)  


## 静态函数 {#static-functions}

### AssignTileProperties {#AssignTileProperties}

#### \<static> AssignTileProperties(mapData) {#static-assigntilepropertiesmapdata}


**说明:**

将所给 MapData 的每层所有瓦片上加起来, 并让每层瓦片与母砖同步。 对于每个有效的瓦片, 此功能确保瓦片的尺寸与其瓦片所定义的尺寸相匹配( 对于使用多个瓦片大小不同的地图很重要), 然后将瓦片中为瓦片类型定义的任何自定义属性合并到瓦片实例中。 这被称为“ 斜图剖析” 管道的一部分, 以确保在运行时, 单个瓦片对象上可以获取从斜图编辑器导出的单片类型元数据 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mapData | [Phaser.Tilemaps.MapData](/api/class/tilemaps-mapdata) | 否 | 地图数据对象. |


> 源码：[src/tilemaps/parsers/tiled/AssignTileProperties.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/tiled/AssignTileProperties.js#L9)  
引入版本：3.0.0


---

### Base64Decode {#Base64Decode}

#### \<static> Base64Decode(data) {#static-base64decodedata}


**说明:**

解码一个基-64编码字符串,这是蒂莱德在导出基-64编码的图列层数据时使用的. 二进制数据被解释为一个小端无符号的32位整数的序列,每个序列代表层中的瓦片GID(Global Tile ID).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | object | 否 | 基-64编码字符串解码. |


**返回值:** array - 代表解码的平板 GID 的无符号32位整数组。


> 源码：[src/tilemaps/parsers/tiled/Base64Decode.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/tiled/Base64Decode.js#L7)  
引入版本：3.0.0


---

### BuildTilesetIndex {#BuildTilesetIndex}

#### \<static> BuildTilesetIndex(mapData) {#static-buildtilesetindexmapdata}


**说明:**

构建一个查找索引,将每个全局瓦片ID(GID)映射到其瓦片映射图像中的像素位置,并在地图数据中显示该瓦片的索引。返回的数组是稀疏的,由GID键入,每个条目都是`[x, y, tilesetIndex]`的表单的三元素阵列。x和y值是其瓦片映射图中上左角的像素坐标,计算瓦片边距和间隔。在建立索引前,地图数据中的任何图像集合都转换成Tileset对象并添加到`mapData.tilesets`中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mapData | [Phaser.Tilemaps.MapData](/api/class/tilemaps-mapdata) \| [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) | 否 | 地图数据对象. |


**返回值:** array - 一个由全局瓦片ID(GID)键入的稀疏阵列,每个条目都是`[x, y, tilesetIndex]`.


> 源码：[src/tilemaps/parsers/tiled/BuildTilesetIndex.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/tiled/BuildTilesetIndex.js#L9)  
引入版本：3.0.0


---

### CreateGroupLayer {#CreateGroupLayer}

#### \<static> CreateGroupLayer(json, [group], [parentState]) {#static-creategrouplayerjson-group-parentstate}


**说明:**

分析一个倾斜组层,并构建一个继承的状态对象,用于处理其子层。倾斜组层可以嵌入其他层次,并积累诸如名称前缀、不透明、可见度和位置偏移等属性。此函数将给定的组自身属性与其母状态属性结合,生成一个孩子层将继承的新状态。

如果没有提供组,则返回一个默认的根态,其值为中性值(完全不透明,可见,零偏移),适合在层层的顶层使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| json | object | 否 | 平面JSON对象. |
| group | object | 是 | 提列德 JSON 文件的当前组层 。 |
| parentState | object | 是 | 父组的继承状态, 如先前调用此函数时返回的。 需要提供 `group` 时 。 |


**返回值:** object - 一个包含累积名称前缀,不透明,可见度,和x/y位置的组状态对象,在解析子层时抵消使用.


> 源码：[src/tilemaps/parsers/tiled/CreateGroupLayer.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/tiled/CreateGroupLayer.js#L9)  
引入版本：3.21.0


---

### ParseGID {#ParseGID}

#### \<static> ParseGID(gid) {#static-parsegidgid}


**说明:**

解析一个平面全球平面图案 ID( GID), 提取在数值的高位编码的平面索引和任何翻转旗。 在平面图案 TMX 格式中, GID 的前三位用于表示水平翻转, 垂直翻转, 以及反对角翻转( 即 90度旋转) 。

此函数从 GID 中剥离这些旗位以恢复原始的瓦片索引,然后解释所有三种旗的八种可能的组合,将其转换为旋转值(以弧度表示),布尔的`flipped`声明Phaser在渲染时可以直接应用到一个瓦片上.

参见全旗规格的砖瓦翻转上的平板文档: [http://docs.mapeditor.org/en/latest/reference/tmx-map-format/](http://docs.mapeditor.org/en/latest/reference/tmx-map-format/)

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gid | number | 否 | 一个斜拉式的GID, 可能带有高位编码的翻转旗. |


**返回值:** [Phaser.Types.Tilemaps.GIDData](/api/typedef/types-tilemaps#giddata) - 一个GIDData对象,包含原始的瓦片索引,三个单个的翻转旗帜,以及衍生的旋转(以弧度表示)和翻转状态.


> 源码：[src/tilemaps/parsers/tiled/ParseGID.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/tiled/ParseGID.js#L11)  
引入版本：3.0.0


---

### ParseImageLayers {#ParseImageLayers}

#### \<static> ParseImageLayers(json) {#static-parseimagelayersjson}


**说明:**

解析一个平面 JSON 对象并提取所有图像层,包括组层内嵌入的图像层。每个图像层都作为平面对象返回,其名称、图像源、计算位置(核算组和层的偏移)、合并不透明、可见度和自定义属性从平面层定义中继承。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| json | object | 否 | 平面JSON对象. |


**返回值:** array - 对象阵列,每个图像层一个,每个包含 `name`, `image`, `x`, `y`, `alpha`, `visible`,和 `properties` 字段中选择


> 源码：[src/tilemaps/parsers/tiled/ParseImageLayers.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/tiled/ParseImageLayers.js#L10)  
引入版本：3.0.0


---

### ParseJSONTiled {#ParseJSONTiled}

#### \<static> ParseJSONTiled(name, source, insertNull) {#static-parsejsontiledname-source-insertnull}


**说明:**

将一个倾斜的 JSON 对象绘制为一个新的 MapData 对象。 源 JSON 在处理前会深复制。 此函数处理正对角、 同位素、 交错和六边形地图方向。 对于六边形地图, 还可以根据六边形的侧长和交错轴计算像素的维度。 它将 JSON 中发现的所有砖层、 图像层、 对象层和砖层进行剖析, 构建砖块集索引, 并在返回完全人气的 MapData 实例之前指定自定义的瓦片属性 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 拼图的名称,用于在 MapData 上设置名称. |
| source | object | 否 | 原始的 Tiled JSON 对象。 此函数会复制深层 。 |
| insertNull | boolean | 否 | 控制如何处理地图数据中的空牌, 其索引为 - 1 的牌。 如果 `true`, 空位置将获得 `null` 的值。 如果 `false`, 空位将获得一个索引为 - 1 的小地图的牌标对象, 并且牌标数据不需要更改, 则设置此值为 `true` 将帮助内存消耗。 然而, 如果您的地图很小或者需要动态更新牌标, 请留下默认值设置 。 |


**返回值:** [Phaser.Tilemaps.MapData](/api/class/tilemaps-mapdata) - 创建的 MapData 对象, 或 `null` 如果数据无法解析 。


> 源码：[src/tilemaps/parsers/tiled/ParseJSONTiled.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/tiled/ParseJSONTiled.js#L19)  
引入版本：3.0.0


---

### ParseObject {#ParseObject}

#### \<static> ParseObject(tiledObject, [offsetX], [offsetY]) {#static-parseobjecttiledobject-offsetx-offsety}


**说明:**

将平面对象转换为内部解析对象, 使其属性正常化和复制, 同时应用可选 x 和 Y 偏移。 解析对象将始终具有属性 `id`, `name`, `type`, `rotation`, `properties`, `visible`, `x`, `y`, `width` 财务报告和已审计财务报表 `height`。其他属性将根据对象类型(如文本、多线、  等)添加。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tiledObject | object | 否 |  | 原始的倾斜对象数据, 从倾斜图编辑器导出 。 |
| offsetX | number | 是 | 0 | 可选附加的偏移以适用于对象的x属性。默认为 0。 |
| offsetY | number | 是 | 0 | 可选附加的偏移以适用于对象的 y 属性。默认为 0 。 |


**返回值:** object - 包含从平面对象中根据类型读取属性的解析对象,其x值和y值根据给定的偏移更新。


> 源码：[src/tilemaps/parsers/tiled/ParseObject.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/tiled/ParseObject.js#L14)  
引入版本：3.0.0


---

### ParseObjectLayers {#ParseObjectLayers}

#### \<static> ParseObjectLayers(json) {#static-parseobjectlayersjson}


**说明:**

将所有物体层从平面 JSON 平面图解成 `ObjectLayer` 对象的阵列。

垂直通过图中的每个层,包括嵌入在平面组层内的层,并将每个 `objectgroup` 类型层转换为 `ObjectLayer` 实例。不透明值和可见值从母组层继承,并乘以子组。非对象层(平面层、图像层等)和非对象组组成员被跳过。产生的阵列包含在任何嵌入深度发现的每个对象层的一个条目。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| json | object | 否 | 平面JSON对象. |


**返回值:** array - 以 `ObjectLayer` 形式在图片中包含所有天体层的阵列。


> 源码：[src/tilemaps/parsers/tiled/ParseObjectLayers.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/tiled/ParseObjectLayers.js#L12)  
引入版本：3.0.0


---

### ParseTileLayers {#ParseTileLayers}

#### \<static> ParseTileLayers(json, insertNull) {#static-parsetilelayersjson-insertnull}


**说明:**

从平面 JSON 对象中解析所有瓦片层, 并把它们作为图层Data 对象的数组返回。 JSON 中的每个瓦片层都成为一个图层Data 实例, 里面有图层对象 。

函数将整个层层排列, 降入平铺组层, 从而包含嵌入式的瓦片层。 组变换属性( 偏移、 不透明、 可见度) 被累积并应用到每个子层。 压缩的瓦片数据不支持, 任何压缩层都会被控制台警告跳过。 编码为未压缩的 Base64 的层在处理前自动解码 。

处理有限和无限( 圆) 斜线图。 对于六边形图, 斜线轴、 斜线索引和六边形侧长从 JSON 读取, 并存储在每个 LayerData 上, 并据此计算层的像素尺寸 。

每个瓦片的翻转旗和旋转都来源于斜拉片使用的GID位包,因此翻转Horizontal,翻转Vertical,翻转AntiDiagonal被翻译为瓦片的`flipX`和`rotation`属性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| json | object | 否 | 平面JSON对象. |
| insertNull | boolean | 否 | 控制地图数据中处理的空牌, 索引为 -1 的牌( 见 QQlink Phaser.Tilemaps.Parsers.Tiled.ParseJSONTiled}) 。 |


**返回值:** Array.\<[Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata)> - - 一系列图层数据对象,每个条目一个

json.layers 与类型“ 拖网员” 。


> 源码：[src/tilemaps/parsers/tiled/ParseTileLayers.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/tiled/ParseTileLayers.js#L16)  
引入版本：3.0.0


---

### ParseTilesets {#ParseTilesets}

#### \<static> ParseTilesets(json) {#static-parsetilesetsjson}


**说明:**

从平面 JSON 地图中解析瓦片和图像收藏,将其转换为 Phaser `Tileset` 财务报告和已审计财务报表 `ImageCollection` 例。处理平面 1.x 和平面 2.x 格式,包括每片属性、对象组、动画数据、王集和打牌的瓦片。外部瓦片(带有一个瓦片的) `source` 将不支持,而且将发出警告。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| json | object | 否 | 平面JSON数据. |


**返回值:** object - 包含平板和图像收集数据的对象。


> 源码：[src/tilemaps/parsers/tiled/ParseTilesets.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/tiled/ParseTilesets.js#L12)  
引入版本：3.0.0


---

### ParseWangsets {#ParseWangsets}

#### \<static> ParseWangsets(wangsets, datas) {#static-parsewangsetswangsets-datas}


**说明:**

从平面 1.1.5+地图数据中解析 Wangset 信息, 如果存在的话。

由于给定的瓦片可能处于一个以上的光泽中,因此产生的属性被嵌入. `tile.data.wangid[someWangsetName]`将在此执行中返回基于数组的光泽 ID.

请注意,我们无法保证,如果砖块中唯一的东西是光泽的定义,那么会有任何“正常”的瓦片,所以必须分别解析。

更多信息请参见[https://doc.mapeditor.org/en/latest/manual/using-wang-tiles/](https://doc.mapeditor.org/en/latest/manual/using-wang-tiles/).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| wangsets | Array.\<object> | 否 | 光集对象的阵列( 从 JSON 分隔) |
| datas | object | 否 | 存储来自平面的光集数据的对象,用瓦片ID键入. |


> 源码：[src/tilemaps/parsers/tiled/ParseWangsets.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/tiled/ParseWangsets.js#L7)  
引入版本：3.53.0


---

---
