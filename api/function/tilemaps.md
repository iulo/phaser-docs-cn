# Phaser.Tilemaps.Components {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/function/tilemaps)

### CalculateFacesAt {#CalculateFacesAt}

#### \<static> CalculateFacesAt(tileX, tileY, layer) {#static-calculatefacesattilex-tiley-layer}


**说明:**

在指定的层的瓦片坐标处计算有趣的面。 有趣的面用于优化与瓦片的碰撞。 这种方法大多用于在仅更改一个瓦片时优化再计算面。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | 砖格网格坐标中的瓦片的x坐标. |
| tileY | number | 否 | 瓦片网格坐标中的y坐标. |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 指定坐标的瓦片,或者如果没有瓦片,则使用`null`。


> 源码：[src/tilemaps/components/CalculateFacesAt.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/CalculateFacesAt.js#L9)  
引入版本：3.0.0


### CalculateFacesWithin {#CalculateFacesWithin}

#### \<static> CalculateFacesWithin(tileX, tileY, width, height, layer) {#static-calculatefaceswithintilex-tiley-width-height-layer}


**说明:**

计算层内指定(在砖座坐标)所有可碰撞的瓦片的有趣面。 “ 有趣的面” 是可碰撞瓦片的暴露边缘, 具体来说, 任何没有与邻近的另一块可碰撞瓦片共享的面。 例如, 如果两块可碰撞瓦片坐在一起, 其之间的共享边缘不是有趣的面, 因为相互移动的物理体永远不会与之碰撞。 只有有趣的面在碰撞解析过程中进行测试, 避免了内缘问题, 并保持碰撞检查的效率。 此功能在瓦片放置或移走时自动调用, 并且大多由瓦片系统内部使用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 否 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 否 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 否 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/CalculateFacesWithin.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/CalculateFacesWithin.js#L10)  
引入版本：3.0.0


### CheckIsoBounds {#CheckIsoBounds}

#### \<static> CheckIsoBounds(tileX, tileY, layer, [camera]) {#static-checkisoboundstilex-tiley-layer-camera}


**说明:**

检查给定的瓦片坐标是否在摄像机的可见范围内, 用于同位素瓦片层。 用于在瓦片卷曲中确定是否应该制取一个瓦片 。

瓦片坐标首先通过层的瓦片对世界的转换转换转换成世界空间,然后对照摄像机的世界观矩形测试所形成的位置,再由层的`cullPaddingX`值和`cullPaddingY`值(以瓦片单位表示)进行扩展,以避免在视图端的边缘出现瓦片,补丁抵消从每个瓦片的中心测量.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 需要检查的图层 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 监控库尔的摄像机 |


**返回值:** boolean - 如果坐标在等效界限内,则返回 `true`。


> 源码：[src/tilemaps/components/CheckIsoBounds.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/CheckIsoBounds.js#L11)  
引入版本：3.50.0


### Copy {#Copy}

#### \<static> Copy(srcTileX, srcTileY, width, height, destTileX, destTileY, recalculateFaces, layer) {#static-copysrctilex-srctiley-width-height-desttilex-desttiley-recalculatefaces-layer}


**说明:**

复制源长方形区域的瓦片到层内的新目的地( 全部在瓦片坐标中指定) 。 此复制所有瓦片属性, 并重新计算目的地区域的碰撞信息 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| srcTileX | number | 否 | 要复制的区域的x坐标,以瓦片表示,而不是像素. |
| srcTileY | number | 否 | 要复制的区域的y坐标, 以瓦片而不是像素表示 。 |
| width | number | 否 | 要复制的区域的宽度,以瓦片表示,而不是像素. |
| height | number | 否 | 要复制的区域的高度,以瓦片表示,而不是像素. |
| destTileX | number | 否 | 要复制的区域的x坐标,以瓦片表示,而不是像素. |
| destTileY | number | 否 | 区域y坐标以瓦片形式复制,而不是像素。 |
| recalculateFaces | boolean | 否 | 如果碰撞在目的地区域面临瓦片数据,应在复制后重新计算`true`。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/Copy.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/Copy.js#L12)  
引入版本：3.0.0


### CreateFromTiles {#CreateFromTiles}

#### \<static> CreateFromTiles(indexes, replacements, spriteConfig, scene, camera, layer) {#static-createfromtilesindexes-replacements-spriteconfig-scene-camera-layer}


**说明:**

为每个匹配层中给定的瓦片索引的对象创建 Sprite。 您可以选择指定每个瓦片是否在 Sprite 创建后被替换为新瓦片。 如果您想要在转换成 Sprite 的级别下置特殊瓦片, 但想要在转换后将瓦片本身替换为地板瓦片或类似的瓦片, 则此操作是有用的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| indexes | number \| Array.\<number> | 否 | 砖块索引,或指向的数组,用来创建Sprites。 |
| replacements | number \| Array.\<number> | 否 | 将转换的瓦片转换为 . 设置为 `null` 使瓦片保持不变。 如果给出了数组, 则假定它是与索引数组的一对一映射 。 |
| spriteConfig | [Phaser.Types.GameObjects.Sprite.SpriteConfig](/api/typedef/types-gameobjects-sprite#spriteconfig) | 否 | 配置对象可以传递到Sprite创建者(即场景. make.sprite)中. |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 创造内在的斯普丽特的场景. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 用于确定每块瓦片的世界 XY 位置的摄像机 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** Array.\<[Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite)> - 创建的 Sprite 阵列 。


> 源码：[src/tilemaps/components/CreateFromTiles.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/CreateFromTiles.js#L11)  
引入版本：3.0.0


### CullBounds {#CullBounds}

#### \<static> CullBounds(layer, camera) {#static-cullboundslayer-camera}


**说明:**

计算摄像机视窗内给定的正交式平面图板层内的瓦片坐标界限。结果会说明每根轴上层的位置、尺度和粘贴。这在内部被凸轮平面图板函数用来确定需要制导的瓦片。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 监控库尔的摄像机 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 包含圆圈的矩形。 如果您想要保留此对象, 请复制它, 因为它是内部循环的 。


> 源码：[src/tilemaps/components/CullBounds.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/CullBounds.js#L13)  
引入版本：3.50.0


### CullTiles {#CullTiles}

#### \<static> CullTiles(layer, camera, [outputArray], [renderOrder]) {#static-culltileslayer-camera-outputarray-renderorder}


**说明:**

返回摄像机视口内所显示的图片。 粘合器避免渲染出屏幕外的图片, 提高性能。 摄像机的世界视野范围被计算并折叠到缩放的图片大小, 同时考虑到凸起的粘贴( 用图片表示) 。 如果该图层启用 `skipCull`, 或它的滚动因子与 1 不同, 则使用全层维度, 从而包含所有图片。 此功能由 lomap 渲染 管道内部使用 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 |  | 提列玛普层要采取行动。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 监控库尔的摄像机 |
| outputArray | array | 是 |  | 可选的将被填充的平板物体存储在内部的数组 。 |
| renderOrder | number | 是 | 0 | 渲染顺序常数。控制了拼图的排列顺序,并添加到输出数组中。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 一系列的平板物体。


> 源码：[src/tilemaps/components/CullTiles.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/CullTiles.js#L10)  
引入版本：3.50.0


### Fill {#Fill}

#### \<static> Fill(index, tileX, tileY, width, height, recalculateFaces, layer) {#static-fillindex-tilex-tiley-width-height-recalculatefaces-layer}


**说明:**

设置图层的矩形区域( 以瓦片坐标) 中的瓦片与指定的索引相配合。 如果指定的索引是碰撞索引, 则图层将被设定为碰撞。 区域中的碰撞信息将被重新计算 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 填充区域用的瓦片索引 。 |
| tileX | number | 否 | 左最瓦座坐标(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 否 | 最顶部的瓦座坐标(在瓦座坐标中),作为该地区的起源. |
| width | number | 否 | 有多少块的瓦片从`tileX`坐标 区域将是。 |
| height | number | 否 | 有多少高的砖块 从`tileY`坐标 区域将是。 |
| recalculateFaces | boolean | 否 | 如果面额数据应重新计算,则使用`true`。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 要使用的瓦片层。 如果不给定当前层, 则使用 。 |


> 源码：[src/tilemaps/components/Fill.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/Fill.js#L11)  
引入版本：3.0.0


### FilterTiles {#FilterTiles}

#### \<static> FilterTiles(callback, context, tileX, tileY, width, height, filteringOptions, layer) {#static-filtertilescallback-context-tilex-tiley-width-height-filteringoptions-layer}


**说明:**

对于图层中指定的矩形区域(在平面坐标)的每个瓦片, 运行指定的过滤回调功能。 任何通过过滤测试的瓦片( 即回调返回真实的) 都将作为新阵列返回 。 类似于 Array. prototype. filter 在 vanilla JS 中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | function | 否 | 回调。 指定区域的每一块牌将传递给这个回调, 作为第一个也是唯一的参数。 回调应该返回通过过滤器的牌的真值 。 |
| context | object | 否 | 恢复召回的场合 。 |
| tileX | number | 否 | 左最瓦索引(在瓦座坐标中)用作过滤区域的来源. |
| tileY | number | 否 | 用于过滤区域源头的最顶部的瓦片索引(在瓦片坐标中). |
| width | number | 否 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 否 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 否 | 获得瓦片时可选择的过滤器。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 滤波器阵列 。


> 源码：[src/tilemaps/components/FilterTiles.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/FilterTiles.js#L9)  
引入版本：3.0.0


### FindByIndex {#FindByIndex}

#### \<static> FindByIndex(index, skip, reverse, layer) {#static-findbyindexindex-skip-reverse-layer}


**说明:**

搜索第一个匹配给定索引的图板的整层地图,然后返回该图板对象。如果找不到匹配,则返回无效。搜索从左上方的图板开始,并水平地持续到其到达行的末尾,然后下降至下一行。如果反向布尔值是真实的,则从右下角扫描,从上到左上。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 要搜索的瓦片索引值 。 |
| skip | number | 否 | 返回前跳过匹配的瓦片的次数 。 |
| reverse | boolean | 否 | 如果真有, 它会逆向扫描层, 从右下方开始。 否则它会从左上方扫描 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 第一个(或n跳过)带有匹配索引的瓦片 。


> 源码：[src/tilemaps/components/FindByIndex.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/FindByIndex.js#L7)  
引入版本：3.0.0


### FindTile {#FindTile}

#### \<static> FindTile(callback, context, tileX, tileY, width, height, filteringOptions, layer) {#static-findtilecallback-context-tilex-tiley-width-height-filteringoptions-layer}


**说明:**

找到该图层中符合所提供测试功能的第一个长方形区域( 砖座坐标)的瓦片。 I. 即找到 `callback` 返回真实的第一瓦片。 类似于 Array. prototype. find in vanilla JS 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | FindTileCallback | 否 | 回调。 指定区域内的每个瓦片都会作为第一个参数传递给这个回调, 连同瓦片索引和瓦片数组。 |
| context | object | 否 | 恢复召回的场合 。 |
| tileX | number | 否 | 左最瓦索引(在瓦座坐标中)用作过滤区域的来源. |
| tileY | number | 否 | 用于过滤区域源头的最顶部的瓦片索引(在瓦片坐标中). |
| width | number | 否 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 否 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 否 | 获得瓦片时可选择的过滤器。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 匹配搜索的拼贴板, 如果没有找到拼贴板, 则无效


> 源码：[src/tilemaps/components/FindTile.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/FindTile.js#L19)  
引入版本：3.0.0


### ForEachTile {#ForEachTile}

#### \<static> ForEachTile(callback, context, tileX, tileY, width, height, filteringOptions, layer) {#static-foreachtilecallback-context-tilex-tiley-width-height-filteringoptions-layer}


**说明:**

对于在给定的长方形区域(在平面坐标)中的每个瓦片,运行给定的调回。类似于 Array.prototive 。forEach 以梵蒂冈JS为主

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | EachTileCallback | 否 | 回调。 指定区域的每一块瓦片都将连同其数组中的索引和数组本身一起传递给这个回调。 |
| context | object | 否 | 恢复召回的场合 。 |
| tileX | number | 否 | 左最瓦索引(在瓦座坐标中)用作过滤区域的来源. |
| tileY | number | 否 | 用于过滤区域源头的最顶部的瓦片索引(在瓦片坐标中). |
| width | number | 否 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 否 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 否 | 获得瓦片时可选择的过滤器。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/ForEachTile.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/ForEachTile.js#L17)  
引入版本：3.0.0


### GetCullTilesFunction {#GetCullTilesFunction}

#### \<static> GetCullTilesFunction(orientation) {#static-getculltilesfunctionorientation}


**说明:**

获取正确的函数来用于凸起瓦片,基于地图方向。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| orientation | number | 否 | 蒂拉玛普方向常数. |


**返回值:** function - 用于为给定地图类型 cull 牌的函数。


> 源码：[src/tilemaps/components/GetCullTilesFunction.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/GetCullTilesFunction.js#L14)  
引入版本：3.50.0


### GetTileAt {#GetTileAt}

#### \<static> GetTileAt(tileX, tileY, nonNull, layer) {#static-gettileattilex-tiley-nonnull-layer}


**说明:**

从给定的地层获得给定的地砖坐标的瓦片。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | X 位置从( 以瓦片单位表示, 不以像素表示) 获取瓦片 。 |
| tileY | number | 否 | Y 位置从( 以瓦片单位表示, 而非像素) 得到瓦片 。 |
| nonNull | boolean | 否 | 对于空的牌,返回索引为 -1 的牌标对象,而不是空的牌标。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 指定坐标的瓦片,如果找不到瓦片或坐标无效,则无效。


> 源码：[src/tilemaps/components/GetTileAt.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/GetTileAt.js#L9)  
引入版本：3.0.0


### GetTileAtWorldXY {#GetTileAtWorldXY}

#### \<static> GetTileAtWorldXY(worldX, worldY, nonNull, camera, layer) {#static-gettileatworldxyworldx-worldy-nonnull-camera-layer}


**说明:**

从给定的地层获得给定的世界坐标的瓦片。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | 从(以像素形式给出)获取瓦片的 X 位置 |
| worldY | number | 否 | Y 位置从 (以像素形式给出) 获取牌 |
| nonNull | boolean | 否 | 对于空的牌,返回索引为 -1 的牌标对象,而不是空的牌标。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 指定坐标的瓦片,如果找不到瓦片或坐标无效,则无效。


> 源码：[src/tilemaps/components/GetTileAtWorldXY.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/GetTileAtWorldXY.js#L12)  
引入版本：3.0.0


### GetTileCorners {#GetTileCorners}

#### \<static> GetTileCorners(tileX, tileY, camera, layer) {#static-gettilecornerstilex-tiley-camera-layer}


**说明:**

获得一个瓦片的四个角, 因其瓦片空间坐标, 作为世界空间矢量2 位置的阵列。 返回的位置是该层的世界位置、 尺度和摄像机卷轴的偏移, 并被命令: 上左、 上右、 下右、 下左。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 计算瓦片角的世界空间位置时,使用其滚动抵消的摄像机. |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 与每个瓦片角的世界 XY 位置相对应的矢量2阵列.


> 源码：[src/tilemaps/components/GetTileCorners.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/GetTileCorners.js#L9)  
引入版本：3.60.0


### GetTileCornersFunction {#GetTileCornersFunction}

#### \<static> GetTileCornersFunction(orientation) {#static-gettilecornersfunctionorientation}


**说明:**

获得正确的函数以获取基于地图方向的瓦片角。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| orientation | number | 否 | 蒂拉玛普方向常数. |


**返回值:** function - 用于获取给定地图方向的瓦片角的函数。


> 源码：[src/tilemaps/components/GetTileCornersFunction.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/GetTileCornersFunction.js#L12)  
引入版本：3.60.0


### GetTilesWithin {#GetTilesWithin}

#### \<static> GetTilesWithin(tileX, tileY, width, height, filteringOptions, layer) {#static-gettileswithintilex-tiley-width-height-filteringoptions-layer}


**说明:**

获取图层的指定矩形区域(在图砖坐标内)的瓦片。

这返回包含提及蒂勒实例本身的数组,所以要意识到修改它们会直接影响层数据.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 否 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 否 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 否 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 否 | 获得瓦片时可选择的过滤器。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 提勒物体阵列。


> 源码：[src/tilemaps/components/GetTilesWithin.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/GetTilesWithin.js#L9)  
引入版本：3.0.0


### GetTilesWithinShape {#GetTilesWithinShape}

#### \<static> GetTilesWithinShape(shape, filteringOptions, camera, layer) {#static-gettileswithinshapeshape-filteringoptions-camera-layer}


**说明:**

获取与指定图层中的形状重叠的牌。形状必须是圆形、线形、矩形或三角形。形状应在世界坐标中。

**注意:** 目前这种方法只与正交形的平面层配合.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| shape | [Phaser.Geom.Circle](/api/class/geom-circle) \| [Phaser.Geom.Line](/api/class/geom-line) | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 世界的形状( 像素) 坐标 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 否 | 获得瓦片时可选择的过滤器。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 与给定形状相交的平板对象数组,如果没有平板块重叠或层层不为正交式,则为空数组。


> 源码：[src/tilemaps/components/GetTilesWithinShape.js#L23](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/GetTilesWithinShape.js#L23)  
引入版本：3.0.0


### GetTilesWithinWorldXY {#GetTilesWithinWorldXY}

#### \<static> GetTilesWithinWorldXY(worldX, worldY, width, height, filteringOptions, camera, layer) {#static-gettileswithinworldxyworldx-worldy-width-height-filteringoptions-camera-layer}


**说明:**

获取该层指定矩形区域(世界坐标)的瓦片.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | 地球X坐标为该地区左上角. |
| worldY | number | 否 | 地球和坐标是该地区左上角 |
| width | number | 否 | 面积宽度. |
| height | number | 否 | 地区高度. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 否 | 获得瓦片时可选择的过滤器。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 用于计算返回的瓦片的摄像机。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 提勒物体阵列。


> 源码：[src/tilemaps/components/GetTilesWithinWorldXY.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/GetTilesWithinWorldXY.js#L13)  
引入版本：3.0.0


### GetTileToWorldXFunction {#GetTileToWorldXFunction}

#### \<static> GetTileToWorldXFunction(orientation) {#static-gettiletoworldxfunctionorientation}


**说明:**

返回用于将平面 X 坐标转换为世界 X 像素坐标的正确函数,其基础是地图方向。对于正交图,此函数返回`TileToWorldX`函数。对于所有其他方向,返回一个NOOP函数,因为非正交图不支持此转换。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| orientation | number | 否 | 蒂拉玛普方向常数. |


**返回值:** function - 用于将平板 X 坐标转换为给定地图方向的世界 X 像素坐标的函数.


> 源码：[src/tilemaps/components/GetTileToWorldXFunction.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/GetTileToWorldXFunction.js#L11)  
引入版本：3.50.0


### GetTileToWorldXYFunction {#GetTileToWorldXYFunction}

#### \<static> GetTileToWorldXYFunction(orientation) {#static-gettiletoworldxyfunctionorientation}


**说明:**

获得正确的函数来翻译根据地图方向的牌。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| orientation | number | 否 | 蒂拉玛普方向常数. |


**返回值:** function - 用于翻译给定地图类型的牌的函数。


> 源码：[src/tilemaps/components/GetTileToWorldXYFunction.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/GetTileToWorldXYFunction.js#L14)  
引入版本：3.50.0


### GetTileToWorldYFunction {#GetTileToWorldYFunction}

#### \<static> GetTileToWorldYFunction(orientation) {#static-gettiletoworldyfunctionorientation}


**说明:**

获得正确的函数来翻译根据地图方向的牌。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| orientation | number | 否 | 蒂拉玛普方向常数. |


**返回值:** function - 用于翻译给定地图类型的牌的函数。


> 源码：[src/tilemaps/components/GetTileToWorldYFunction.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/GetTileToWorldYFunction.js#L12)  
引入版本：3.50.0


### GetWorldToTileXFunction {#GetWorldToTileXFunction}

#### \<static> GetWorldToTileXFunction(orientation) {#static-getworldtotilexfunctionorientation}


**说明:**

返回用于根据地图方向将世界像素 X 坐标转换为平面 X (列) 索引的正确函数。只有正向图支持此转换;对于所有其他方向,则返回一个 NULL 函数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| orientation | number | 否 | 蒂拉玛普方向常数. |


**返回值:** function - 用于将世界X坐标转换成给定地图方向的平板 X 索引的函数,或者如果方向不支持的NULL函数.


> 源码：[src/tilemaps/components/GetWorldToTileXFunction.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/GetWorldToTileXFunction.js#L11)  
引入版本：3.50.0


### GetWorldToTileXYFunction {#GetWorldToTileXYFunction}

#### \<static> GetWorldToTileXYFunction(orientation) {#static-getworldtotilexyfunctionorientation}


**说明:**

返回给定的映射方向的适当的世界对平面坐标转换函数。返回的函数将世界像素坐标(X, Y)转换为平面网格坐标,使用对正对、对称、六边形或交错的图示的正确投影数学。如果方向无法识别,则返回NOOP函数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| orientation | number | 否 | `Phaser.Tilemaps.ORIENTATION_CONST`中定义的Tilemap方向常数. |


**返回值:** function - 给定地图方向的世界对瓦坐标转换功能.


> 源码：[src/tilemaps/components/GetWorldToTileXYFunction.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/GetWorldToTileXYFunction.js#L14)  
引入版本：3.50.0


### GetWorldToTileYFunction {#GetWorldToTileYFunction}

#### \<static> GetWorldToTileYFunction(orientation) {#static-getworldtotileyfunctionorientation}


**说明:**

返回用于将世界 Y 坐标转换为平板 Y 坐标的正确函数, 以地图方向为基础。 返回正交地图的 `WorldToTileY` , 返回交错地图的 `StaggeredWorldToTileY` , 以及所有其他方向的 NULL 函数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| orientation | number | 否 | 蒂拉玛普方向常数. |


**返回值:** function - 用于将世界 Y 坐标转换成给定地图方向的 瓦片 Y 坐标的函数 。


> 源码：[src/tilemaps/components/GetWorldToTileYFunction.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/GetWorldToTileYFunction.js#L12)  
引入版本：3.50.0


### HasTileAt {#HasTileAt}

#### \<static> HasTileAt(tileX, tileY, layer) {#static-hastileattilex-tiley-layer}


**说明:**

检查在给定的层中(在砖座坐标)的指定位置是否有一个瓦片。如果没有瓦片,或者该位置的瓦片有−1的索引,返回时会弄虚作假。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | X 位置从( 以瓦片单位表示, 不以像素表示) 获取瓦片 。 |
| tileY | number | 否 | Y 位置从( 以瓦片单位表示, 而非像素) 得到瓦片 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** boolean - 如果在给定坐标上存在有效的瓦片(指数大于 -1),返回 `true`,如果坐标超出界限,则返回 `false`,或者返回该瓦片的索引为 -1。


> 源码：[src/tilemaps/components/HasTileAt.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/HasTileAt.js#L9)  
引入版本：3.0.0


### HasTileAtWorldXY {#HasTileAtWorldXY}

#### \<static> HasTileAtWorldXY(worldX, worldY, camera, layer) {#static-hastileatworldxyworldx-worldy-camera-layer}


**说明:**

检查指定位置( 世界坐标) 是否有瓦片。 如果没有瓦片, 或者该位置的瓦片有 - 1 的索引, 返回时会弄虚作假 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | 世界位置的X坐标. |
| worldY | number | 否 | 世界位置的Y坐标. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 用于计算返回的瓦片的摄像机。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** boolean - 返回布尔值,如果给出的图层无效,则返回无效值。


> 源码：[src/tilemaps/components/HasTileAtWorldXY.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/HasTileAtWorldXY.js#L12)  
引入版本：3.0.0


### HexagonalCullBounds {#HexagonalCullBounds}

#### \<static> HexagonalCullBounds(layer, camera) {#static-hexagonalcullboundslayer-camera}


**说明:**

计算属于摄像机视口的六边形斜拉线层的砖格索引边界。该界限表示层的交错轴(x或y)、六边形长度、瓦片缩放、层面抵消和凸起等,返回需要渲染的砖柱和线的面积。这在六边形砖块的内部使用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 监控库尔的摄像机 |


**返回值:** object - 包含 `left`, `right`, `top` 财务报告和已审计财务报表 `bottom` 瓦片网格索引边界 。


> 源码：[src/tilemaps/components/HexagonalCullBounds.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/HexagonalCullBounds.js#L10)  
引入版本：3.50.0


### HexagonalCullTiles {#HexagonalCullTiles}

#### \<static> HexagonalCullTiles(layer, camera, [outputArray], [renderOrder]) {#static-hexagonalculltileslayer-camera-outputarray-renderorder}


**说明:**

返回摄像机视图端的图片。 内部使用此图片。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 |  | 提列玛普层要采取行动。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 监控库尔的摄像机 |
| outputArray | array | 是 |  | 将平板对象存储在内部的可选数组 。 |
| renderOrder | number | 是 | 0 | 渲染令常数. |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 一系列的平板物体。


> 源码：[src/tilemaps/components/HexagonalCullTiles.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/HexagonalCullTiles.js#L10)  
引入版本：3.50.0


### HexagonalGetTileCorners {#HexagonalGetTileCorners}

#### \<static> HexagonalGetTileCorners(tileX, tileY, camera, layer) {#static-hexagonalgettilecornerstilex-tiley-camera-layer}


**说明:**

计算并返回六角形瓦片在世界空间中的六个角位置,作为矢量2天体的阵列。瓦片用其瓦片网格坐标来识别,角相对于瓦片的世界中心来计算,同时考虑到层的交错轴和适用于瓦片层的任何尺度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 将瓦座坐标转换为世界位置时使用的摄像机. |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 与每个瓦片角的世界 XY 位置相对应的矢量2阵列.


> 源码：[src/tilemaps/components/HexagonalGetTileCorners.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/HexagonalGetTileCorners.js#L12)  
引入版本：3.60.0


### HexagonalTileToWorldXY {#HexagonalTileToWorldXY}

#### \<static> HexagonalTileToWorldXY(tileX, tileY, point, camera, layer) {#static-hexagonaltiletoworldxytilex-tiley-point-camera-layer}


**说明:**

从六边形的平面XY坐标(平面单位)转换为世界XY坐标(像素),以图层位置、尺度和滚动为因数。这将返回一个新的矢量2对象或更新给定的`point`对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 用于存储坐标的矢量2。 如果未给定新的矢量2, 则创建 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 计算世界坐标时用到的摄像机,用瓦片值计算. |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 世界坐标中的 XY位置.


> 源码：[src/tilemaps/components/HexagonalTileToWorldXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/HexagonalTileToWorldXY.js#L9)  
引入版本：3.50.0


### HexagonalWorldToTileXY {#HexagonalWorldToTileXY}

#### \<static> HexagonalWorldToTileXY(worldX, worldY, snapToFloor, point, camera, layer) {#static-hexagonalworldtotilexyworldx-worldy-snaptofloor-point-camera-layer}


**说明:**

从世界 XY 坐标( 像素) 转换为六边形的 牌子 XY 坐标( 瓦片单位), 以图层位置、 缩放和滚动为因数。 这将返回一个新的矢量2 对象或更新给定的 `point` 对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | 要转换的x坐标,以像素表示,而不是用瓦片表示. |
| worldY | number | 否 | 转换的y坐标,以像素表示,而不是瓦片. |
| snapToFloor | boolean | 否 | 是否将平面坐标向下绕至最近的整数 。 |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 用于存储坐标的矢量2。 如果未给定新的矢量2, 则创建 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 从世界值计算平面 XY坐标时使用的摄像机 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - XY位置在瓦片单位.


> 源码：[src/tilemaps/components/HexagonalWorldToTileXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/HexagonalWorldToTileXY.js#L9)  
引入版本：3.50.0


### IsInLayerBounds {#IsInLayerBounds}

#### \<static> IsInLayerBounds(tileX, tileY, layer) {#static-isinlayerboundstilex-tiley-layer}


**说明:**

检查给定的瓦片坐标是否在层的界限内 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** boolean - 如果瓦座坐标在地层的界限内,则`true`,否则则`false`.


> 源码：[src/tilemaps/components/IsInLayerBounds.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/IsInLayerBounds.js#L7)  
引入版本：3.0.0


### IsometricCullTiles {#IsometricCullTiles}

#### \<static> IsometricCullTiles(layer, camera, [outputArray], [renderOrder]) {#static-isometricculltileslayer-camera-outputarray-renderorder}


**说明:**

返回摄像机视图端的图片。 内部使用此图片。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 |  | 提列玛普层要采取行动。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 监控库尔的摄像机 |
| outputArray | array | 是 |  | 将平板对象存储在内部的可选数组 。 |
| renderOrder | number | 是 | 0 | 渲染定单常数. 0 = 右下方, 1 = 左下方, 2 = 右上方, 3 = 左上方. |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 一系列的平板物体。


> 源码：[src/tilemaps/components/IsometricCullTiles.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/IsometricCullTiles.js#L9)  
引入版本：3.50.0


### IsometricTileToWorldXY {#IsometricTileToWorldXY}

#### \<static> IsometricTileToWorldXY(tileX, tileY, point, camera, layer) {#static-isometrictiletoworldxytilex-tiley-point-camera-layer}


**说明:**

从等位平面的 XY 坐标( 平面单位) 转换为世界 XY 坐标( 像素), 以图层位置、 缩放和滚动为因数。 这将返回一个新的矢量2 对象或更新给定的 `point` 对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 用于存储坐标的矢量2。 如果未给定新的矢量2, 则创建 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 用来计算瓦片坐标世界位置的摄像机。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 世界坐标中的 XY位置.


> 源码：[src/tilemaps/components/IsometricTileToWorldXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/IsometricTileToWorldXY.js#L9)  
引入版本：3.50.0


### IsometricWorldToTileXY {#IsometricWorldToTileXY}

#### \<static> IsometricWorldToTileXY(worldX, worldY, snapToFloor, point, camera, layer, [originTop]) {#static-isometricworldtotilexyworldx-worldy-snaptofloor-point-camera-layer-origintop}


**说明:**

从世界 XY 坐标( 像素) 转换为等位的平面 XY 坐标( 平面单位), 以图层位置、 缩放和滚动为因数。 这将返回一个新的矢量2 对象或更新给定的 `point` 对象 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| worldX | number | 否 |  | 要转换的x坐标,以像素表示,而不是用瓦片表示. |
| worldY | number | 否 |  | 转换的y坐标,以像素表示,而不是瓦片. |
| snapToFloor | boolean | 否 |  | 是否将平板坐标向下折叠到最近的整数 。 |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 |  | 用于存储坐标的矢量2。 如果未给定新的矢量2, 则创建 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 |  | 提列玛普层要采取行动。 |
| originTop | boolean | 是 | true | 何为等位牌的正面 ? 顶部( 默认, 真实) 还是底部 ? (假) |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - XY位置在瓦片单位.


> 源码：[src/tilemaps/components/IsometricWorldToTileXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/IsometricWorldToTileXY.js#L9)  
引入版本：3.50.0


### PutTileAt {#PutTileAt}

#### \<static> PutTileAt(tile, tileX, tileY, recalculateFaces, layer) {#static-puttileattile-tilex-tiley-recalculatefaces-layer}


**说明:**

在指定的地层中设置一个砖块坐标。您可以在索引或图块对象中传递。如果在图块中传递,所有属性都将复制到指定位置。如果在索引中通过,则只更改指定位置的索引。碰撞信息将在指定位置重新计算。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tile | number \| [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 此牌的索引可以设置或设置一个牌面对象。 |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| recalculateFaces | boolean | 否 | 如果面额数据应重新计算,则使用`true`。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 创建或添加到此地图中的图案对象 。


> 源码：[src/tilemaps/components/PutTileAt.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/PutTileAt.js#L12)  
引入版本：3.0.0


### PutTileAtWorldXY {#PutTileAtWorldXY}

#### \<static> PutTileAtWorldXY(tile, worldX, worldY, recalculateFaces, camera, layer) {#static-puttileatworldxytile-worldx-worldy-recalculatefaces-camera-layer}


**说明:**

在指定的层中设置一个瓦片, 您可以在一个索引或一个图案对象中传递。 如果您在图案中通过, 所有属性都会复制到指定位置。 如果您在索引中通过, 只有指定位置的索引会被更改。 如果`recalculateFaces`是 `true`, 则在指定位置会重新计算折叠面值信息 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tile | number \| [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 此牌的索引可以设置或设置一个牌面对象。 |
| worldX | number | 否 | x坐标,以像素表示. |
| worldY | number | 否 | y坐标,以像素表示. |
| recalculateFaces | boolean | 否 | `true` 如果砖边碰撞面部数据应该重新计算. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 创建或添加到此地图中的图案对象 。


> 源码：[src/tilemaps/components/PutTileAtWorldXY.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/PutTileAtWorldXY.js#L12)  
引入版本：3.0.0


### PutTilesAt {#PutTilesAt}

#### \<static> PutTilesAt(tilesArray, tileX, tileY, recalculateFaces, layer) {#static-puttilesattilesarray-tilex-tiley-recalculatefaces-layer}


**说明:**

在指定的图片坐标上放置一个瓦片数组或一个2D的瓦片数组。该数组可以是瓦片索引或瓦片对象。如果在图片中通过,所有属性都将复制到指定位置。如果在索引中通过,则只更改指定位置的索引。碰撞信息将在区域牌块内重新计算。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tilesArray | Array.\<number> \| Array.\<Array.\<number>> | Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> | Array.\<Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)>> | 否 | 铺设一个列( 阵列) 或格(2D 阵列) 的平面或瓦片索引。 |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| recalculateFaces | boolean | 否 | 如果面额数据应重新计算,则使用`true`。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/PutTilesAt.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/PutTilesAt.js#L10)  
引入版本：3.0.0


### Randomize {#Randomize}

#### \<static> Randomize(tileX, tileY, width, height, indexes, layer) {#static-randomizetilex-tiley-width-height-indexes-layer}


**说明:**

随机化指定层内一个长方形的瓦片区域(在瓦片坐标内)的索引。每个瓦片将获得一个新的索引。如果一个索引数组被传递进来,那么这些索引将被用于随机分配新的瓦片索引。如果不提供数组,则区域内发现的索引(不包括 -1)将被用于随机分配新的瓷片索引。这种方法只修改了瓦片索引,不会改变碰撞信息。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | 左最砖座坐标(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 否 | 最顶部的瓦座坐标(在瓦座坐标中)作为该地区的起源. |
| width | number | 否 | 有多少块的瓦片从`tileX`坐标 区域将是。 |
| height | number | 否 | 有多少高的砖块 从`tileY`坐标 区域将是。 |
| indexes | Array.\<number> | 否 | 随机化过程中随机抽取的一系列索引. |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/Randomize.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/Randomize.js#L10)  
引入版本：3.0.0


### RemoveTileAt {#RemoveTileAt}

#### \<static> RemoveTileAt(tileX, tileY, replaceWithNull, recalculateFaces, layer) {#static-removetileattilex-tiley-replacewithnull-recalculatefaces-layer}


**说明:**

删除指定层中瓦片坐标的瓦片,并更新层的碰撞信息。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | 要删除的瓦片的x坐标, 以瓦片网格单位( 不是像素) 。 |
| tileY | number | 否 | 要移除的瓦片的y坐标, 以瓦片网格单位( 不像素) 。 |
| replaceWithNull | boolean | 否 | 如果为真, 这将用无效的砖来取代指定位置的瓦, 而不是以 - 1 的索引为单位的砖。 |
| recalculateFaces | boolean | 否 | 如果面额数据应重新计算,则使用`true`。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 删除的拼贴对象 。


> 源码：[src/tilemaps/components/RemoveTileAt.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/RemoveTileAt.js#L11)  
引入版本：3.0.0


### RemoveTileAtWorldXY {#RemoveTileAtWorldXY}

#### \<static> RemoveTileAtWorldXY(worldX, worldY, replaceWithNull, recalculateFaces, camera, layer) {#static-removetileatworldxyworldx-worldy-replacewithnull-recalculatefaces-camera-layer}


**说明:**

删除指定世界坐标所在的瓦片,并更新该层的碰撞信息。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | x坐标,以像素表示. |
| worldY | number | 否 | y坐标,以像素表示. |
| replaceWithNull | boolean | 否 | 如果为真, 这将用无效的砖来取代指定位置的瓦, 而不是以 - 1 的索引为单位的砖。 |
| recalculateFaces | boolean | 否 | 如果面额数据应重新计算,则使用`true`。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 删除的拼贴对象 。


> 源码：[src/tilemaps/components/RemoveTileAtWorldXY.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/RemoveTileAtWorldXY.js#L12)  
引入版本：3.0.0


### RenderDebug {#RenderDebug}

#### \<static> RenderDebug(graphics, styleConfig, layer) {#static-renderdebuggraphics-styleconfig-layer}


**说明:**

绘制图层的调试表示式。 如果您想要快速了解您的哪些牌正在碰撞, 哪些牌有有趣的面孔, 这样做很有帮助。 调试表示式从图形( 0 ) 开始绘制, 允许您将调试表示式放置在屏幕上 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 目标图形对象可以引用 。 |
| styleConfig | [Phaser.Types.Tilemaps.DebugStyleOptions](/api/typedef/types-tilemaps#debugstyleoptions) | 否 | 指定调试绘图所用的颜色的对象。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/RenderDebug.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/RenderDebug.js#L14)  
引入版本：3.0.0


### ReplaceByIndex {#ReplaceByIndex}

#### \<static> ReplaceByIndex(findIndex, newIndex, tileX, tileY, width, height, layer) {#static-replacebyindexfindindex-newindex-tilex-tiley-width-height-layer}


**说明:**

扫描给定的矩形区域(在平面坐标中给出),以匹配`findIndex`的索引来扫描瓦片,并更新其索引以匹配`newIndex`。这只修改索引,不会改变碰撞信息。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| findIndex | number | 否 | 查找的瓦片索引 。 |
| newIndex | number | 否 | 以瓦片代替的索引 。 |
| tileX | number | 否 | 左最瓦座坐标(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 否 | 最顶部的瓦座坐标(在瓦座坐标中),作为该地区的起源. |
| width | number | 否 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 否 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/ReplaceByIndex.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/ReplaceByIndex.js#L9)  
引入版本：3.0.0


### RunCull {#RunCull}

#### \<static> RunCull(layer, bounds, renderOrder, outputArray) {#static-runculllayer-bounds-renderorder-outputarray}


**说明:**

返回摄像机视图端的图片。 内部使用此图片。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |
| bounds | object | 否 | 包含`left`,`right`,`top`和`bottom`边界的天体. |
| renderOrder | number | 否 | 渲染定单常数. 0 = 右下方, 1 = 左下方, 2 = 右上方, 3 = 左上方. |
| outputArray | array | 否 | 将图案对象存储在其中的数组 。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 一系列的平板物体。


> 源码：[src/tilemaps/components/RunCull.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/RunCull.js#L7)  
引入版本：3.50.0


### SetCollision {#SetCollision}

#### \<static> SetCollision(indexes, collides, recalculateFaces, layer, [updateLayer]) {#static-setcollisionindexes-collides-recalculatefaces-layer-updatelayer}


**说明:**

将一个图片或牌片的碰撞按指数排列。 您可以通过一个单一的数字索引或一系列索引: [2、 3、 15、 20]。 `collides` 参数控制如果碰撞将被启用( 真实) 或禁用( 假) 。

此函数既更新了层的碰撞指数(它影响到将来放置的任何瓦片),又更新了除`updateLayer`是虚假的外,层中所有与给定索引匹配的现有瓦片.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| indexes | number \| array | 否 |  | 或单瓦索引,或单瓦索引的数组。 |
| collides | boolean | 否 |  | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 否 |  | 更新后是否重新计算瓦片面孔 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 |  | 提列玛普层要采取行动。 |
| updateLayer | boolean | 是 | true | 如果选中的话, 请更新层上的当前牌。 如果没有设置牌, 则设置为不实 。 |


> 源码：[src/tilemaps/components/SetCollision.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/SetCollision.js#L11)  
引入版本：3.0.0


### SetCollisionBetween {#SetCollisionBetween}

#### \<static> SetCollisionBetween(start, stop, collides, recalculateFaces, layer, [updateLayer]) {#static-setcollisionbetweenstart-stop-collides-recalculatefaces-layer-updatelayer}


**说明:**

设定一个图片的碰撞范围, 其指数介于指定的 `start`和 `stop`( 包括) 之间。 使用起始值为 10, 止值为 14 的图片, 将设置为 10、 11、 12、 13 和 14 的碰撞范围, 如果启用碰撞( 真实) 或 禁用( 假) , `collides` 参数控制会设置 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| start | number | 否 |  | 设定碰撞的瓦片的第一个索引. |
| stop | number | 否 |  | 设定碰撞的瓦片的最后一个索引 。 |
| collides | boolean | 否 |  | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 否 |  | 更新后是否重新计算瓦片面孔 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 |  | 提列玛普层要采取行动。 |
| updateLayer | boolean | 是 | true | 如果选中的话, 请更新层上的当前牌。 如果没有设置牌, 则设置为不实 。 |


> 源码：[src/tilemaps/components/SetCollisionBetween.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/SetCollisionBetween.js#L11)  
引入版本：3.0.0


### SetCollisionByExclusion {#SetCollisionByExclusion}

#### \<static> SetCollisionByExclusion(indexes, collides, recalculateFaces, layer) {#static-setcollisionbyexclusionindexes-collides-recalculatefaces-layer}


**说明:**

设定在给定的层中所有瓦片上的碰撞, 除了在给定数组中指定索引的瓦片。 如果启用碰撞( 真实) 或禁用( 假) , `collides` 参数控制。 目前未在层中使用的拖动索引不受影响 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| indexes | Array.\<number> | 否 | 一系列的瓦片索引, 以排除碰撞更新。 带有这些索引的图案不会改变其碰撞状态 。 |
| collides | boolean | 否 | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 否 | 更新后是否重新计算瓦片面孔 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/SetCollisionByExclusion.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/SetCollisionByExclusion.js#L11)  
引入版本：3.0.0


### SetCollisionByProperty {#SetCollisionByProperty}

#### \<static> SetCollisionByProperty(properties, collides, recalculateFaces, layer) {#static-setcollisionbypropertyproperties-collides-recalculatefaces-layer}


**说明:**

通过检查瓦片属性来设定一层内瓦片的碰撞。 如果瓦片具有与给定的属性对象匹配的属性, 则会设置其碰撞标志。 如果启用碰撞( 真实) 或禁用( 假) , 则 `collides` 参数控制。 在 `{ collides: true }` 中通过, 将会将任何砖片上的碰撞标志更新为具有真实值的“ collides ” 属性。 任何没有设置“ collide” 的瓦片都会被忽略。 您也可以使用一系列值, 如 `{ types: ["stone", "lava", "sand" ] }`。 如果一个瓦片具有与任何这些值匹配的“ 类型” 属性, 其碰撞标志将会被更新 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| properties | object | 否 | 具有瓦片属性和相应值的对象,应当检查。 |
| collides | boolean | 否 | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 否 | 更新后是否重新计算瓦片面孔 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/SetCollisionByProperty.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/SetCollisionByProperty.js#L11)  
引入版本：3.0.0


### SetCollisionFromCollisionGroup {#SetCollisionFromCollisionGroup}

#### \<static> SetCollisionFromCollisionGroup(collides, recalculateFaces, layer) {#static-setcollisionfromcollisiongroupcollides-recalculatefaces-layer}


**说明:**

通过检查每块瓦片的碰撞组数据(通常在平板碰撞编辑器内在平板上定义),将瓦片的碰撞设定在一层内。如果在瓦片的碰撞组内发现任何物体,则会设置瓦片的碰撞信息。如果启用碰撞(真)或禁用(假),则`collides`参数控制。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| collides | boolean | 否 | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 否 | 更新后是否重新计算瓦片面孔 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/SetCollisionFromCollisionGroup.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/SetCollisionFromCollisionGroup.js#L10)  
引入版本：3.0.0


### SetLayerCollisionIndex {#SetLayerCollisionIndex}

#### \<static> SetLayerCollisionIndex(tileIndex, collides, layer) {#static-setlayercollisionindextileindex-collides-layer}


**说明:**

内部使用的方法来跟踪在一层内碰撞的瓦片索引。这可以将LyewsData.ZcollideIndexes更新为包含或不包含指定的`tileIndex`。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileIndex | number | 否 | 设置碰撞布林的瓦片索引 。 |
| collides | boolean | 否 | 瓦片指数是否应该碰撞? |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/SetLayerCollisionIndex.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/SetLayerCollisionIndex.js#L7)  
引入版本：3.0.0


### SetTileCollision {#SetTileCollision}

#### \<static> SetTileCollision(tile, [collides]) {#static-settilecollisiontile-collides}


**说明:**

内部使用的方法设置一个瓦片的碰撞状态。 这不会重新计算有趣的面孔 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tile | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 |  | 启动碰撞的瓦片。 |
| collides | boolean | 是 | true | 瓦片是否应该碰撞? |


> 源码：[src/tilemaps/components/SetTileCollision.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/SetTileCollision.js#L7)  
引入版本：3.0.0


### SetTileIndexCallback {#SetTileIndexCallback}

#### \<static> SetTileIndexCallback(indexes, callback, callbackContext, layer) {#static-settileindexcallbackindexes-callback-callbackcontext-layer}


**说明:**

设置层内给定的瓦片索引的全局碰撞调用。 这将影响此层上所有具有相同索引的瓦片。 如果为瓦片索引设置了调用调用调用调取调用调用调用的调用调用调试调用调用调制调用调用调出调用调用调出的调用调用调色调用调用调用了调用调用调减减调用调用调的调用调用调就可以看到 setTileLocationCallback 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| indexes | number \| array | 否 | 或单瓦指数,或一串瓦指数,以设定碰撞回调 。 |
| callback | function | 否 | 当瓦片被碰撞时将引用的回调 。 |
| callbackContext | object | 否 | 调用时的上下文 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/SetTileIndexCallback.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/SetTileIndexCallback.js#L7)  
引入版本：3.0.0


### SetTileLocationCallback {#SetTileLocationCallback}

#### \<static> SetTileLocationCallback(tileX, tileY, width, height, callback, callbackContext, layer) {#static-settilelocationcallbacktilex-tiley-width-height-callback-callbackcontext-layer}


**说明:**

设置层内给定的矩形区域( 平面坐标) 的碰撞调用。 如果已经为平面设置调用, 则将替换。 设置调用调用为无效以删除 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | 左最瓦的坐标用来作为该地区的起源. |
| tileY | number | 否 | 最顶部的瓦片坐标用来作为该地区的起源. |
| width | number | 否 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 否 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| callback | function | 否 | 当瓦片被碰撞时将引用的回调 。 |
| callbackContext | object | 否 | 调用时的上下文 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/SetTileLocationCallback.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/SetTileLocationCallback.js#L9)  
引入版本：3.0.0


### Shuffle {#Shuffle}

#### \<static> Shuffle(tileX, tileY, width, height, layer) {#static-shuffletilex-tiley-width-height-layer}


**说明:**

在指定的层内, 将牌片划入长方形区域( 以瓦片坐标表示) 。 它只会随机排列该区域的牌片, 所以如果它们都一样, 似乎不会改变 ! 这种方法只会修改瓦片索引, 并且不会改变碰撞信息 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | 左最瓦的索引(在瓦座坐标中)作为区域的起源. |
| tileY | number | 否 | 以砖座坐标为最顶的瓦片索引作为区域的起源. |
| width | number | 否 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 否 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/Shuffle.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/Shuffle.js#L10)  
引入版本：3.0.0


### StaggeredCullBounds {#StaggeredCullBounds}

#### \<static> StaggeredCullBounds(layer, camera) {#static-staggeredcullboundslayer-camera}


**说明:**

返回摄像机视图端的图层中的界限。这是由 cull 牌函数内部使用的。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 监控库尔的摄像机 |


**返回值:** object - 包含`left`,`right`,`top`和`bottom`边界的天体.


> 源码：[src/tilemaps/components/StaggeredCullBounds.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/StaggeredCullBounds.js#L10)  
引入版本：3.50.0


### StaggeredCullTiles {#StaggeredCullTiles}

#### \<static> StaggeredCullTiles(layer, camera, [outputArray], [renderOrder]) {#static-staggeredculltileslayer-camera-outputarray-renderorder}


**说明:**

返回摄像机视图端的图片。 内部使用此图片。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 |  | 提列玛普层要采取行动。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 监控库尔的摄像机 |
| outputArray | array | 是 |  | 将平板对象存储在内部的可选数组 。 |
| renderOrder | number | 是 | 0 | 渲染令常数. |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 一系列的平板物体。


> 源码：[src/tilemaps/components/StaggeredCullTiles.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/StaggeredCullTiles.js#L10)  
引入版本：3.50.0


### StaggeredTileToWorldXY {#StaggeredTileToWorldXY}

#### \<static> StaggeredTileToWorldXY(tileX, tileY, point, camera, layer) {#static-staggeredtiletoworldxytilex-tiley-point-camera-layer}


**说明:**

从错位的平面图 XY 坐标( 平面单位) 转换为世界 XY 坐标( 像素), 以图层位置、 缩放和滚动为因数。 这将返回一个新的矢量2 对象或更新给定的 `point` 对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 用于存储坐标的矢量2。 如果未给定新的矢量2, 则创建 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 用来计算瓦片坐标世界位置的摄像机。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 世界坐标中的 XY位置.


> 源码：[src/tilemaps/components/StaggeredTileToWorldXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/StaggeredTileToWorldXY.js#L9)  
引入版本：3.50.0


### StaggeredTileToWorldY {#StaggeredTileToWorldY}

#### \<static> StaggeredTileToWorldY(tileY, camera, layer) {#static-staggeredtiletoworldytiley-camera-layer}


**说明:**

从错位的瓦片Y坐标(瓦片单位)转换为世界Y坐标(像素),在层的位置,尺度和卷轴中进行计数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 转换时用于计算卷轴偏移的摄像机。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** number - 世界坐标Y位置.


> 源码：[src/tilemaps/components/StaggeredTileToWorldY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/StaggeredTileToWorldY.js#L7)  
引入版本：3.50.0


### StaggeredWorldToTileXY {#StaggeredWorldToTileXY}

#### \<static> StaggeredWorldToTileXY(worldX, worldY, snapToFloor, point, camera, layer) {#static-staggeredworldtotilexyworldx-worldy-snaptofloor-point-camera-layer}


**说明:**

从世界 XY 坐标( 像素) 转换为交错的 牌XY 坐标( 瓦片单位), 以图层位置、 缩放和滚动为因数。 这将返回一个新的矢量2 对象, 或更新给定的 `point` 对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | 要转换的x坐标,以像素表示,而不是用瓦片表示. |
| worldY | number | 否 | 转换的y坐标,以像素表示,而不是瓦片. |
| snapToFloor | boolean | 否 | 是否将平板坐标向下折叠到最近的整数 。 |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 用于存储坐标的矢量2。 如果未给定新的矢量2, 则创建 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - XY位置在瓦片单位.


> 源码：[src/tilemaps/components/StaggeredWorldToTileXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/StaggeredWorldToTileXY.js#L9)  
引入版本：3.50.0


### StaggeredWorldToTileY {#StaggeredWorldToTileY}

#### \<static> StaggeredWorldToTileY(worldY, snapToFloor, camera, layer) {#static-staggeredworldtotileyworldy-snaptofloor-camera-layer}


**说明:**

从世界Y坐标(像素)转换为交错的瓦片Y坐标(瓦单位),在层的位置,尺度和卷轴中进行计数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldY | number | 否 | 转换的y坐标,以像素表示,而不是瓦片. |
| snapToFloor | boolean | 否 | 是否将平板坐标向下折叠到最近的整数 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** number - Y的位置在瓦片单位。


> 源码：[src/tilemaps/components/StaggeredWorldToTileY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/StaggeredWorldToTileY.js#L7)  
引入版本：3.50.0


### SwapByIndex {#SwapByIndex}

#### \<static> SwapByIndex(indexA, indexB, tileX, tileY, width, height, layer) {#static-swapbyindexindexa-indexb-tilex-tiley-width-height-layer}


**说明:**

扫描给定的矩形区域(在平面坐标中显示),以匹配`indexA`的索引来扫描瓦片,然后与`indexB`交换。这只修改索引,不会改变碰撞信息。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| indexA | number | 否 | 用于搜索和替换`indexB`的瓦片索引. |
| indexB | number | 否 | 用瓦片索引代替 `indexA` 。 |
| tileX | number | 否 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 否 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 否 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 否 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/SwapByIndex.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/SwapByIndex.js#L9)  
引入版本：3.0.0


### TileToWorldX {#TileToWorldX}

#### \<static> TileToWorldX(tileX, camera, layer) {#static-tiletoworldxtilex-camera-layer}


**说明:**

从平面X坐标(平面单位)转换为世界X坐标(像素),在层的位置,尺度和滚动中进行计数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 用来计算瓦片坐标世界位置的摄像机。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** number - 世界X坐标,以像素表示,对应给定的瓦片X坐标.


> 源码：[src/tilemaps/components/TileToWorldX.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/TileToWorldX.js#L7)  
引入版本：3.0.0


### TileToWorldXY {#TileToWorldXY}

#### \<static> TileToWorldXY(tileX, tileY, point, camera, layer) {#static-tiletoworldxytilex-tiley-point-camera-layer}


**说明:**

从平面 XY 坐标( 平面单位) 转换为世界 XY 坐标( 像素), 以图层的位置、 缩放和滚动为因数。 这将返回一个新的矢量2 对象或更新指定的 `point` 对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 用于存储坐标的矢量2。 如果未给定新的矢量2, 则创建 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 将瓦片坐标转换为世界像素值时使用的摄像机 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 世界坐标中的 XY位置.


> 源码：[src/tilemaps/components/TileToWorldXY.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/TileToWorldXY.js#L11)  
引入版本：3.0.0


### TileToWorldY {#TileToWorldY}

#### \<static> TileToWorldY(tileY, camera, layer) {#static-tiletoworldytiley-camera-layer}


**说明:**

从瓦片 Y 坐标( 平面单位) 转换为世界 Y 坐标( 像素), 以图层位置、 缩放和滚动为因数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** number - 世界坐标Y位置.


> 源码：[src/tilemaps/components/TileToWorldY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/TileToWorldY.js#L7)  
引入版本：3.0.0


### WeightedRandomize {#WeightedRandomize}

#### \<static> WeightedRandomize(tileX, tileY, width, height, weightedIndexes, layer) {#static-weightedrandomizetilex-tiley-width-height-weightedindexes-layer}


**说明:**

随机化指定层内一个矩形的瓦片区域(在瓦片坐标内)的索引。每个瓦片将获得一个新的索引。新的索引是从给定的 weightedIndexes 阵列中抽取的。一个加权数组的例子:

[{指数:6,重量:4},//指数6的概率为4/8{指数:7,重量:2},/指数7的概率为2/8{指数:8,重量:1.5},/指数8的概率为1.5/8{指数:26,重量:0.5}/指数26的概率为0.5/8]].

选择任何索引的概率是(索引的权重) /(所有权重的和) 。 这种方法只修改了瓦片索引, 并且不会改变碰撞信息 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 否 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 否 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 否 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| weightedIndexes | Array.\<object> | 否 | 随机化过程中随机抽取的一组对象。 其形式应该是 : { 指数: 0, 重量: 4} 或{ 指数: [0], 重量: 4( 如果您想从多块的索引中抽取 ) 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


> 源码：[src/tilemaps/components/WeightedRandomize.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/WeightedRandomize.js#L10)  
引入版本：3.0.0


### WorldToTileX {#WorldToTileX}

#### \<static> WorldToTileX(worldX, snapToFloor, camera, layer) {#static-worldtotilexworldx-snaptofloor-camera-layer}


**说明:**

从世界X坐标(像素)转换为瓦片X坐标(瓦片单位),在图层位置,尺度和滚动中进行计数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | 要转换的x坐标,以像素表示,而不是用瓦片表示. |
| snapToFloor | boolean | 否 | 是否将平板坐标向下折叠到最近的整数 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** number - 以瓦片单位表示的 X 位置 。


> 源码：[src/tilemaps/components/WorldToTileX.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/WorldToTileX.js#L12)  
引入版本：3.0.0


### WorldToTileXY {#WorldToTileXY}

#### \<static> WorldToTileXY(worldX, worldY, snapToFloor, point, camera, layer) {#static-worldtotilexyworldx-worldy-snaptofloor-point-camera-layer}


**说明:**

从世界 XY 坐标( 像素) 转换为 平面 XY 坐标( 平面单位), 以图层位置、 缩放和滚动为因数。 这将返回一个新的矢量2 对象或更新给定的 `point` 对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | 要转换的x坐标,以像素表示,而不是用瓦片表示. |
| worldY | number | 否 | 转换的y坐标,以像素表示,而不是瓦片. |
| snapToFloor | boolean | 否 | 是否将平板坐标向下折叠到最近的整数 。 |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 用于存储坐标的矢量2。 如果未给定新的矢量2, 则创建 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - XY位置在瓦片单位.


> 源码：[src/tilemaps/components/WorldToTileXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/WorldToTileXY.js#L9)  
引入版本：3.0.0


### WorldToTileY {#WorldToTileY}

#### \<static> WorldToTileY(worldY, snapToFloor, camera, layer) {#static-worldtotileyworldy-snaptofloor-camera-layer}


**说明:**

从世界Y坐标(像素)转换为瓦片Y坐标(瓦片单位),在层的位置,尺度和卷轴中进行计数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldY | number | 否 | 转换的y坐标,以像素表示,而不是瓦片. |
| snapToFloor | boolean | 否 | 是否将平板坐标向下折叠到最近的整数 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 从世界值计算瓦片索引时使用的摄像机 。 |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | 提列玛普层要采取行动。 |


**返回值:** number - Y的位置在瓦片单位。


> 源码：[src/tilemaps/components/WorldToTileY.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/components/WorldToTileY.js#L12)  
引入版本：3.0.0


# Phaser.Tilemaps.Parsers {#page-title-1}

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


# Phaser.Tilemaps.Parsers.Impact {#page-title-2}

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


# Phaser.Tilemaps.Parsers.Tiled {#page-title-3}

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


### ParseTileLayers {#ParseTileLayers-1}

#### \<static> ParseTileLayers(json, insertNull) {#static-parsetilelayersjson-insertnull-1}


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


### ParseTilesets {#ParseTilesets-1}

#### \<static> ParseTilesets(json) {#static-parsetilesetsjson-1}


**说明:**

从平面 JSON 地图中解析瓦片和图像收藏,将其转换为 Phaser `Tileset` 财务报告和已审计财务报表 `ImageCollection` 例。处理平面 1.x 和平面 2.x 格式,包括每片属性、对象组、动画数据、王集和打牌的瓦片。外部瓦片(带有一个瓦片的) `source` 将不支持,而且将发出警告。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| json | object | 否 | 平面JSON数据. |


**返回值:** object - 包含平板和图像收集数据的对象。


> 源码：[src/tilemaps/parsers/tiled/ParseTilesets.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/parsers/tiled/ParseTilesets.js#L12)  
引入版本：3.0.0


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


### ParseToTilemap {#ParseToTilemap}

#### \<static> ParseToTilemap(scene, [key], [tileWidth], [tileHeight], [width], [height], [data], [insertNull]) {#static-parsetotilemapscene-key-tilewidth-tileheight-width-height-data-insertnull}


**说明:**

从给定的键或数据创建 Tilemap。 如果给定的键或数据都没有, 请将 Tilemap 改为空白。 从 CSV 或 2D 阵列加载时, 您应该指定 tileWidth & tileHeight。从图中解析时, tileWidth, tileHeight,宽度和高度将从地图数据中拉出。对于空地图,您应当指定 tileWidth, tileHeight,宽度和高度。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 蒂莱玛普属于的场景. |
| key | string | 是 |  | Phaser缓存中对应已装入的图片数据的键. |
| tileWidth | number | 是 | 32 | 以像素表示的瓦片宽度 。 |
| tileHeight | number | 是 | 32 | 瓦片在像素中的高度. |
| width | number | 是 | 10 | 以瓦片计的地图宽度 。 |
| height | number | 是 | 10 | 地图的高度,以瓦片计. |
| data | Array.\<Array.\<number>> | 是 |  | 与其从缓存中加载,还可以直接从2D的片片索引中加载. |
| insertNull | boolean | 是 | false | 控制如何处理地图数据中的空牌, 索引为 - 1 的牌。 如果 `true`, 空位置将获得 `null` 的值。 如果 `false` , 空位置将得到索引为 - 1 的一个牌对象, 如果您有大片的地图, 而牌块数据不需要更改, 那么设置这个值为 `true` 将会帮助内存消耗。 然而, 如果您的地图很小, 或者您需要动态更新牌, 那么就留下默认值设定 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 从给定数据创建的 Tilemap 对象 。


> 源码：[src/tilemaps/ParseToTilemap.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ParseToTilemap.js#L12)  
引入版本：3.0.0

---
