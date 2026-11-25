# Types.Tilemaps {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-tilemaps)

## CreateFromObjectLayerConfig {#createfromobjectlayerconfig}

### \<static> CreateFromObjectLayerConfig {#static-createfromobjectlayerconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| id | number | 是 |  | 要转换的独有对象 ID 。 |
| gid | number | 是 |  | 要转换的对象 GID 。 |
| 名称 | string | 是 |  | 要转换的对象名称 。 |
| 类型 | string | 是 |  | 要转换的对象类型 。 |
| classType | function | 是 |  | 转换对象的自定义类类型。 默认为 QQlink Phaser.GameObjects.Sprite}。 自定义类应该类似 Sprite 或 Image; 见 QQlink Phaser.Types.Tilemaps.CreateFromObjectsClassTypeConstructor} 。 |
| ignoreTileset | boolean | 是 |  | 默认情况下, Gid 对象复制属性, 并尊重该 gid 时的瓦片类型, 并将对象视为覆盖。 如果这是真的, 它们不会, 并且只使用对象本身上设置的字段 。 |
| scene | [Phaser.Scene](/api/class/scene) | 是 |  | 场景参考, 传递给游戏对象构建器 。 |
| container | [Phaser.GameObjects.Container](/api/class/gameobjects-container) | 是 |  | 游戏对象添加的可选容器。 |
| key | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 |  | 用于文本管理器或文本实例中的可选键。如果省略,则使用对象的 gid 的砖瓦套键。 |
| frame | string \| number | 是 |  | 纹理内框架的可选名称或索引。如果省略,则使用砖块索引,假设图示表框架与砖块索引和几何美图完全匹配 -- -- 如果有的话。 |
| sortByY | boolean | 是 | false | 按 Y 位置将对象按层排序。 Y 较高对象显示于下 y 的物体上方。 |

**类型**: object

**Member of**: Phaser.Types.Tilemaps
> 源码：[src/tilemaps/typedefs/CreateFromObjectLayerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/typedefs/CreateFromObjectLayerConfig.js#L1)  
引入版本：3.50.0

---

## CreateFromObjectsClassTypeConstructor {#createfromobjectsclasstypeconstructor}

### \<static> CreateFromObjectsClassTypeConstructor {#static-createfromobjectsclasstypeconstructor}

**类型**: function

**Member of**: Phaser.Types.Tilemaps
> 源码：[src/tilemaps/typedefs/CreateFromObjectsClassTypeConstructor.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/typedefs/CreateFromObjectsClassTypeConstructor.js#L1)  
引入版本：3.60.0

---

## DebugStyleOptions {#debugstyleoptions}

### \<static> DebugStyleOptions {#static-debugstyleoptions}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tileColor | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "blue" | 用于绘制非折叠的瓷砖位置的填充矩形的颜色。如果设置为无效,则不绘制非折叠的瓷砖。 |
| collidingTileColor | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "orange" | 用于绘制碰撞牌位置的填充矩形的颜色。如果设置为无效,则不绘制碰撞牌。 |
| faceColor | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "grey" | 用于在有趣的平面画线的颜色。 如果设置为无效, 则不会绘制有趣的平面 。 |

**类型**: object

**Member of**: Phaser.Types.Tilemaps
> 源码：[src/tilemaps/typedefs/DebugStyleOptions.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/typedefs/DebugStyleOptions.js#L1)  
引入版本：3.0.0

---

## FilteringOptions {#filteringoptions}

### \<static> FilteringOptions {#static-filteringoptions}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| isNotEmpty | boolean | 是 | false | 如果为真, 只返回没有 - 1 的索引的牌 。 |
| isColliding | boolean | 是 | false | 如果是真的,只返回至少一面碰撞的瓷砖。 |
| hasInterestingFace | boolean | 是 | false | 如果真有,则只返回至少有一张有趣面孔的牌. |

**类型**: object

**Member of**: Phaser.Types.Tilemaps
> 源码：[src/tilemaps/typedefs/FilteringOptions.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/typedefs/FilteringOptions.js#L1)  
引入版本：3.0.0

---

## GIDData {#giddata}

### \<static> GIDData {#static-giddata}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gid | number | 否 | 平底胶片 |
| flippedHorizontal | boolean | 否 | 水平翻转旗子 。 |
| flippedVertical | boolean | 否 | 垂直翻转旗子 。 |
| flippedAntiDiagonal | boolean | 否 | 横角翻旗. |
| rotation | number | 否 | 轮换数量。 |
| flipped | boolean | 否 | 被翻过了吗? |

**类型**: object

**Member of**: Phaser.Types.Tilemaps
> 源码：[src/tilemaps/typedefs/GIDData.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/typedefs/GIDData.js#L1)  
引入版本：3.0.0

---

## LayerDataConfig {#layerdataconfig}

### \<static> LayerDataConfig {#static-layerdataconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 名称 | string | 是 |  | 如果在 Tiled 中指定,则图层的名称 。 |
| x | number | 是 | 0 | 左上方的 x 偏移到何处 。 |
| y | number | 是 | 0 | 从左上方抽出哪里的 Y 乘以 。 |
| width | number | 是 | 0 | 以瓦片计的层宽度 。 |
| height | number | 是 | 0 | 层层的高度以瓦片计. |
| tileWidth | number | 是 | 0 | 瓦片的像素宽度. |
| tileHeight | number | 是 | 0 | 瓦片的像素高度. |
| baseTileWidth | number | 是 | 0 | 基瓦宽度. |
| baseTileHeight | number | 是 | 0 | 基部瓦片高处. |
| widthInPixels | number | 是 | 0 | 整个层的宽度像素. |
| heightInPixels | number | 是 | 0 | 整个层的高度以像素表示. |
| alpha | number | 是 | 1 | 层的α值. |
| visible | boolean | 是 | true | 层层是否可见? |
| properties | Array.\<object> | 是 |  | 层特定属性( 可以用斜线指定) |
| indexes | array | 是 |  | 拼贴ID索引地图. |
| collideIndexes | array | 是 |  | 拼接式碰撞ID索引地图. |
| callbacks | array | 是 |  | 一系列回调. |
| bodies | array | 是 |  | 一系列物理体. |
| data | array | 是 |  | 瓦片数据索引的数组。 |
| tilemapLayer | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 是 |  | 引用拥有此数据的 Tilemap 层 。 |

**类型**: object

**Member of**: Phaser.Types.Tilemaps
> 源码：[src/tilemaps/typedefs/LayerDataConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/typedefs/LayerDataConfig.js#L1)  
引入版本：3.0.0

---

## MapDataConfig {#mapdataconfig}

### \<static> MapDataConfig {#static-mapdataconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 名称 | string | 是 |  | Phaser缓存中对应已装入的图片数据的密钥. |
| width | number | 是 | 0 | 整个瓦片的宽度 。 |
| height | number | 是 | 0 | 整个瓦片的高度。 |
| tileWidth | number | 是 | 0 | 瓦片的宽度. |
| tileHeight | number | 是 | 0 | 瓦片的高度 。 |
| widthInPixels | number | 是 |  | 整个平面的宽度以像素表示. |
| heightInPixels | number | 是 |  | 整个瓦片的高度以像素表示. |
| format | number | 是 |  | 提列德中定义的提列马普格式. |
| orientation | string \| [Phaser.Tilemaps.Orientation](/api/namespace/tilemaps-orientation) | 是 |  | 地图数据(即正对角、异构、六边形)的方向,默认的“正对角”。 |
| renderOrder | string | 是 |  | 确定图片的绘图顺序。默认为右下。 |
| version | number | 是 |  | 地图使用的"斜拉图"版本. |
| properties | number | 是 |  | 映射特定属性( 可以在 Tiled 中指定) 。 |
| layers | Array.\<[Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata)> | 是 |  | 瓦片的层层. |
| images | array | 是 |  | 一个包含所有图层的阵列, 配置到 MapData 。 |
| objects | object | 是 |  | 平面图像层的阵列 。 |
| collision | object | 是 |  | 平面对象层的对象。 |
| tilesets | Array.\<[Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset)> | 是 |  | 地图所用的瓷砖。 |
| imageCollections | array | 是 |  | 地图使用的图像的收集( 以斜线表示 ) 。 |
| tiles | array | 是 |  | 泰尔实例的矩阵 。 |

**类型**: object

**Member of**: Phaser.Types.Tilemaps
> 源码：[src/tilemaps/typedefs/MapDataConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/typedefs/MapDataConfig.js#L1)  
引入版本：3.0.0

---

## ObjectLayerConfig {#objectlayerconfig}

### \<static> ObjectLayerConfig {#static-objectlayerconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 名称 | string | 是 | "'object layer'" | 对象层的名称 。 |
| opacity | number | 是 | 1 | 层层的不透明,在0到1之间. |
| properties | any | 是 |  | 对象层上定义的自定义属性, 由它们的名称键入 。 |
| propertytypes | any | 是 |  | 对象层上定义的每个自定义属性的类型,按其名称键. |
| 类型 | string | 是 | "'objectgroup'" | 地层的种类,应该是`objectgroup`. |
| visible | boolean | 是 | true | 显示层( `true`) 或隐藏层( `false`) 。 |
| objects | Array.\<any> | 是 |  | 由此对象层上的所有对象组成的数组。 |

**类型**: object

**Member of**: Phaser.Types.Tilemaps
> 源码：[src/tilemaps/typedefs/ObjectLayerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/typedefs/ObjectLayerConfig.js#L1)  
引入版本：3.0.0

---

## StyleConfig {#styleconfig}

### \<static> StyleConfig {#static-styleconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tileColor | [Phaser.Display.Color](/api/namespace/display-color) \| number | null | 是 | "blue" | 用于绘制非折叠的瓷砖位置的填充矩形的颜色。如果设置为无效,则不绘制非折叠的瓷砖。 |
| collidingTileColor | [Phaser.Display.Color](/api/namespace/display-color) \| number | null | 是 | "orange" | 用于绘制碰撞牌位置的填充矩形的颜色。如果设置为无效,则不绘制碰撞牌。 |
| faceColor | [Phaser.Display.Color](/api/namespace/display-color) \| number | null | 是 | "grey" | 用于在有趣的平面画线的颜色。 如果设置为无效, 则不会绘制有趣的平面 。 |

**类型**: object

**Member of**: Phaser.Types.Tilemaps
> 源码：[src/tilemaps/typedefs/StyleConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/typedefs/StyleConfig.js#L1)  
引入版本：3.0.0

---

## TiledObject {#tiledobject}

### \<static> TiledObject {#static-tiledobject}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| id | number | 否 | 独有的对象 ID. |
| 名称 | string | 否 | 此天体在 Tiled 中被指定名称 。 |
| 类型 | string | 否 | 此实例的字符串类型, 如 Tiled 中指定的。 斜线支持从 loesets 中继承实例类型; 在这种情况下, 该类型将设置在 loile 的数据中, 但在此为 `''` ; 使用 `gid` 来获取 loble 数据或属性 。 |
| visible | boolean | 是 | 此对象的可见状态 。 |
| x | number | 是 | 此对象的水平位置,以像素形式,相对图片. |
| y | number | 是 | 此对象的垂直位置,以像素表示,相对于图片. |
| width | number | 是 | 此对象的宽度, 以像素计 。 |
| height | number | 是 | 此天体的高度, 以像素计 。 |
| rotation | number | 是 | 对象的旋转,以顺时针度计。 |
| properties | any | 是 | 自定义属性对象 。 |
| gid | number | 是 | 只在“ 平面” 类型时设置 。 |
| flippedHorizontal | boolean | 是 | 仅设定为平板对象。水平翻转值 。 |
| flippedVertical | boolean | 是 | 仅设定为平板对象。垂直翻转值。 |
| flippedAntiDiagonal | boolean | 是 | 仅设定为平面对象。对角翻转值 。 |
| polyline | Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 是 | 仅在多线对象设置。 对象数组对应点, 每个点都有 `x` 属性和 `y` 属性 。 |
| polygon | Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 是 | 仅在多边形对象下设定。 对象数组对应点, 每个点都有 `x` 属性和 `y` 属性 。 |
| text | any | 是 | 仅设定文本对象。包含文本对象属性。 |
| rectangle | boolean | 是 | 如果有矩形物体,则只设定,并设定为`true`。 |
| ellipse | boolean | 是 | 如果有椭圆物体,则只设定,并设定为`true`。 |
| point | boolean | 是 | 仅设定,如果是点物体,则设定为`true`. |

**类型**: object

**Member of**: Phaser.Types.Tilemaps
> 源码：[src/tilemaps/typedefs/TiledObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/typedefs/TiledObject.js#L1)  
引入版本：3.0.0

---

## TilemapConfig {#tilemapconfig}

### \<static> TilemapConfig {#static-tilemapconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 是 |  | Phaser缓存中对应已装入的图片数据的密钥. |
| data | Array.\<Array.\<number>> | 是 |  | 与其从缓存中加载,还可以直接从2D的片片索引中加载. |
| tileWidth | number | 是 | 32 | 以像素表示的瓦片宽度 。 |
| tileHeight | number | 是 | 32 | 瓦片在像素中的高度. |
| width | number | 是 | 10 | 以瓦片计的地图宽度 。 |
| height | number | 是 | 10 | 地图的高度,以瓷砖计. |
| insertNull | boolean | 是 | false | 控制如何处理地图数据中的空牌, 带有 -1 索引的牌。 如果 `true`, 空位置将获得 `null` 值。 如果 `false` , 空位置将得到一个带有 - 1 索引的牌对象, 如果您有大片人烟稀少的地图, 牌块数据不需要更改, 那么设置这个值到 `true` 将会帮助内存消耗。 但是, 如果您的地图很小, 或者您需要动态更新牌, 那么留下默认值设定 。 |

**类型**: object

**Member of**: Phaser.Types.Tilemaps
> 源码：[src/tilemaps/typedefs/TilemapConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/typedefs/TilemapConfig.js#L1)  
引入版本：3.0.0

---

---
