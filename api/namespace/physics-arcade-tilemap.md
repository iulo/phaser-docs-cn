# Phaser.Physics.Arcade.Tilemap {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-tilemap)

Scope: 
static
> 源码：[src/physics/arcade/tilemap/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/index.js#L7)  


## 静态函数 {#static-functions}

### ProcessTileCallbacks {#ProcessTileCallbacks}

#### \<static> ProcessTileCallbacks(tile, sprite) {#static-processtilecallbackstile-sprite}


**说明:**

检查是否为给定的牌盘注册了每瓦或每瓦索引的碰撞调用,如果是的话,则引用它与碰撞的游戏对象。 调用级别调用( 直接设置在牌盘上) 优先于层层调用( 以牌盘指数设置在牌盘层上 ) 。 如果调用返回 `true` , 则碰撞被否决, 此函数返回 `false` , 以跳过此对子的进一步处理。 如果没有注册调用, 此函数返回 `true`, 从而继续正常的 Arcade 物理碰撞分辨率 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tile | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 处理的拖车。 |
| sprite | [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) | 否 | 使用 Tile 处理的游戏对象 。 |


**返回值:** boolean - 如果继续处理这种瓦片/成片的碰撞,则`true`;如果回调否决碰撞,则`false`。


> 源码：[src/physics/arcade/tilemap/ProcessTileCallbacks.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/ProcessTileCallbacks.js#L7)  
引入版本：3.0.0


---

### ProcessTileSeparationX {#ProcessTileSeparationX}

#### \<static> ProcessTileSeparationX(body, x) {#static-processtileseparationxbody-x}


**说明:**

处理物理体与瓦片横向分离的内部功能,它根据分离方向更新物理体的左或右屏蔽旗,按照分离量沿X轴移动物理体,更新其中心,然后或者根据物理体的弹跳系数将水平速度零化或者应用弹跳.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 物理体反对分开。 |
| x | number | 否 | x轴分离距离, 以像素为单位。 一个负值表示物理体被屏蔽在左侧; 一个正值表示它被屏蔽在右侧。 |


> 源码：[src/physics/arcade/tilemap/ProcessTileSeparationX.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/ProcessTileSeparationX.js#L7)  
引入版本：3.0.0


---

### ProcessTileSeparationY {#ProcessTileSeparationY}

#### \<static> ProcessTileSeparationY(body, y) {#static-processtileseparationybody-y}


**说明:**

内部功能处理物理体与瓦片的垂直分离.

更新物理体的屏蔽旗,根据分离方向,按照分离量调整物理体的垂直位置,然后或者将垂直速度零化,或者应用物理体的弹跳因子来逆向.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 物理体反对分开。 |
| y | number | 否 | 垂直分离量, 以像素为单位。 一个负值表示物理体被上面屏蔽; 一个正值表示它被下面屏蔽 。 |


> 源码：[src/physics/arcade/tilemap/ProcessTileSeparationY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/ProcessTileSeparationY.js#L7)  
引入版本：3.0.0


---

### SeparateTile {#SeparateTile}

#### \<static> SeparateTile(i, body, tile, tileWorldRect, tilemapLayer, tileBias, isLayer) {#static-separatetilei-body-tile-tileworldrect-tilemaplayer-tilebias-islayer}


**说明:**

将物理体与瓦片分开,解决它们之间的任何重叠。它决定了哪个轴首先根据物理体的当前速度处理:如果物理体横向移动更快,则首先检查X轴,反之亦然。当将两轴上相撞面的对角移入瓦片时,优先处理最小重叠的轴。分离时,酌情调用`TileCheckX`和/或`TileCheckY`,如果第一个轴分离足以完全解决交叉,则提前调用短路。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| i | number | 否 | 地图数据中的瓦片索引 。 |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 物理体反对分开。 |
| tile | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 瓦片可以碰撞对战. |
| tileWorldRect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形物体定义瓦片的尺寸。 |
| tilemapLayer | [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) | 否 | The tilemapLayer to collide against. |
| tileBias | number | 否 | 瓦片偏移值,由`World.TILE_BIAS`常数定义,用于防止快速移动的机体通过薄的瓦片进行隧道通路. |
| isLayer | boolean | 否 | 这是来自TilemapLayer的支票还是一系列的瓦片? |


**返回值:** boolean - 如果物理体分开的话,就用`true`,否则用`false`.


> 源码：[src/physics/arcade/tilemap/SeparateTile.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/SeparateTile.js#L11)  
引入版本：3.0.0


---

### TileCheckX {#TileCheckX}

#### \<static> TileCheckX(body, tile, tileLeft, tileRight, tileBias, isLayer) {#static-tilecheckxbody-tile-tileleft-tileright-tilebias-islayer}


**说明:**

检查给定物理体与 X 轴上的瓦片, 计算重叠值, 并在发现碰撞时应用分离。 当检查来源于 TilemapLayer 时, 尊重瓦片的面部和碰撞标记, 并发送到 `ProcessTileSeparationX`( 或者在启用 `customSeparateX` 时设置 `body.overlapX`) 。 由 Exploy 函数在内部使用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 物理体反对分开。 |
| tile | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 瓦片来检查。 |
| tileLeft | number | 否 | 在世界坐标的瓦片的左边缘,以像素表示. |
| tileRight | number | 否 | 世界坐标的瓦片的右边缘,以像素表示. |
| tileBias | number | 否 | 瓦片偏移值。 重叠大于此阈值会被忽略以防止隧道通透。 通常设置为 `World.TILE_BIAS` 。 |
| isLayer | boolean | 否 | 这是来自TilemapLayer的支票还是一系列的瓦片? |


**返回值:** number - 发生的分离量。


> 源码：[src/physics/arcade/tilemap/TileCheckX.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/TileCheckX.js#L9)  
引入版本：3.0.0


---

### TileCheckY {#TileCheckY}

#### \<static> TileCheckY(body, tile, tileTop, tileBottom, tileBias, isLayer) {#static-tilecheckybody-tile-tiletop-tilebottom-tilebias-islayer}


**说明:**

检查物理体与Y轴上的瓦片之间的重叠,并解决任何发现的碰撞。如果物理体有自定义的分隔符设置,重叠值将存储在`body.overlapY`上,供呼叫者处理;否则,`ProcessTileSeparationY`会被调用以立即解决碰撞。由SollectTile函数在内部使用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 物理体反对分开。 |
| tile | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 瓦片来检查。 |
| tileTop | number | 否 | 瓦片在世界空间的顶部位置,以像素表示. |
| tileBottom | number | 否 | 瓦片在世界空间的底部位置,以像素表示. |
| tileBias | number | 否 | 瓦片偏移值,由`World.TILE_BIAS`常数定义. |
| isLayer | boolean | 否 | 这是来自TilemapLayer的支票还是一系列的瓦片? |


**返回值:** number - 发生的垂直分离量,以像素计.


> 源码：[src/physics/arcade/tilemap/TileCheckY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/TileCheckY.js#L9)  
引入版本：3.0.0


---

### TileIntersectsBody {#TileIntersectsBody}

#### \<static> TileIntersectsBody(tileWorldRect, body) {#static-tileintersectsbodytileworldrect-body}


**说明:**

检查给定的瓦片矩形物体与Arcade 物理体之间的交叉点.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileWorldRect | Object | 否 | 定义世界瓦片放置的矩形对象. |
| body | [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 检查与交叉点的物理体 |


**返回值:** boolean - 如果瓦片与机体相交,则返回`true`,否则返回`false`.


> 源码：[src/physics/arcade/tilemap/TileIntersectsBody.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/tilemap/TileIntersectsBody.js#L7)  
引入版本：3.0.0


---

---
