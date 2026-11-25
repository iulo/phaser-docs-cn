# ObjectLayer {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tilemaps-objectlayer)

代表一个平面图中设定的对象层。平面图中的对象层用于将非平面元素,如产卵点、碰撞区、触发区、路径和其他游戏专用标记放置在任意位置。与平面图中不同的是,物体层存储自由形式对象(矩形、椭圆形、多边形、多线形、瓦片和文字),

此类的实例由 Phaser 当解析倾斜图数据时通过 `Phaser.Tilemaps.ParseToTilemap` 或 或 时 间 `scene.make.tilemap`。您可以从 Tilemap 中获取对象Layer 。 `tilemap.getObjectLayer(name)`.

此类映射一个平面对象层的结构, 除了:

 - “ x” & “y” 属性被忽略, 因为这些属性不能在 Tiled 中更改 。

 - 直接将“offsetx”和“offesty”应用于单个对象坐标,所以它们

   也被忽视。

 - "画序"被忽略.

**构造函数**

`new ObjectLayer([config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Tilemaps.ObjectLayerConfig](/api/typedef/types-tilemaps#objectlayerconfig) | 是 | 平面 JSON 对象的图层数据 。 |

---


**作用域**: static

> 源码：[src/tilemaps/mapdata/ObjectLayer.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/ObjectLayer.js#L10)  
引入版本：3.0.0

## 公开成员 {#public-members}

### id {#id}

#### id: number {#id-number}


**说明:**

地图数据中指定的对象层的ID.


> 源码：[src/tilemaps/mapdata/ObjectLayer.js#L51](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/ObjectLayer.js#L51)  
引入版本：3.70.0


---

### name {#name}

#### name: string {#name-string}


**说明:**

对象层的名称 。


> 源码：[src/tilemaps/mapdata/ObjectLayer.js#L42](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/ObjectLayer.js#L42)  
引入版本：3.0.0


---

### objects {#objects}

#### objects: Array.\<[Phaser.Types.Tilemaps.TiledObject](/api/typedef/types-tilemaps#tiledobject)> {#objects-arrayphasertypestilemapstiledobject}


**说明:**

由此对象层上的所有对象组成的数组。

每个斜线对象对应于一个 JavaScript 对象在此数组中。它有一个 `id` (独有), `name` (按平面排列), `type` (按平面排列), `rotation` (顺时针度), `properties` (如果有的话) `visible` 状态( E)`true` 如果可见, `false` 否则, `x` 财务报告和已审计财务报表 `y` 坐标(以像素表示,相对于平方块),和 a `width` 财务报告和已审计财务报表 `height` (以像素计).

对象牌有: `gid` 属性(代表的瓦片的GID),a `flippedHorizontal` 属性,a `flippedVertical` 属性,和 `flippedAntiDiagonal` 属性。 QQlink 中 [http://docs.mapeditor.org/en/latest/reference/tmx-map-format/](http://docs.mapeditor.org/en/latest/reference/tmx-map-format/)QQQ 已转移文档 包含翻转和旋转信息 。

聚线有 `polyline` 属性,指与点相对应的一组对象,每个点都有 `x` 属性和a `y` 。多边形在其结构上具有相同的数组。 `polygon` 属性。文本对象有 `text` 属性。

矩形和椭圆形的`rectangle`或`ellipse`属性设置为`true`.


> 源码：[src/tilemaps/mapdata/ObjectLayer.js#L105](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/ObjectLayer.js#L105)  
引入版本：3.0.0


---

### opacity {#opacity}

#### opacity: number {#opacity-number}


**说明:**

层层的不透明,在0到1之间.


> 源码：[src/tilemaps/mapdata/ObjectLayer.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/ObjectLayer.js#L60)  
引入版本：3.0.0


---

### properties {#properties}

#### properties: object {#properties-object}


**说明:**

对象层上定义的自定义属性, 由它们的名称键入 。


> 源码：[src/tilemaps/mapdata/ObjectLayer.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/ObjectLayer.js#L69)  
引入版本：3.0.0


---

### propertyTypes {#propertyTypes}

#### propertyTypes: object {#propertytypes-object}


**说明:**

对象层上定义的每个自定义属性的类型,按其名称键.


> 源码：[src/tilemaps/mapdata/ObjectLayer.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/ObjectLayer.js#L78)  
引入版本：3.0.0


---

### type {#type}

#### type: string {#type-string}


**说明:**

地层的种类,应该是`objectgroup`.


> 源码：[src/tilemaps/mapdata/ObjectLayer.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/ObjectLayer.js#L87)  
引入版本：3.0.0


---

### visible {#visible}

#### visible: boolean {#visible-boolean}


**说明:**

显示层( `true`) 或隐藏层( `false`) 。


> 源码：[src/tilemaps/mapdata/ObjectLayer.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/mapdata/ObjectLayer.js#L96)  
引入版本：3.0.0


---

---
