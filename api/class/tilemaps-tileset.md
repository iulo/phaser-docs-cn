# Tileset {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tilemaps-tileset)

平面图是包含平面图和每个平面图数据容器的组合图。它将平面图索引(GID)映射到平面图图中的位置,存储每平面图属性和碰撞数据,并支持平面图间隔和边距。平面图在解析平面图数据时自动创建,在渲染时被平面图使用。

**构造函数**

`new Tileset(name, firstgid, [tileWidth], [tileHeight], [tileMargin], [tileSpacing], [tileProperties], [tileData], [tileOffset])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 名称 | string | 否 |  | 地图数据中的平板名称. |
| firstgid | number | 否 |  | 这个瓷砖的首个瓷砖索引包含. |
| tileWidth | number | 是 | 32 | 每片瓦的宽度( 像素). |
| tileHeight | number | 是 | 32 | 每块瓦的高度(像素). |
| tileMargin | number | 是 | 0 | 工作表中所有瓦片的边距( 像素) 。 |
| tileSpacing | number | 是 | 0 | 工作表内每块瓦之间的间隔(以像素计). |
| tileProperties | object | 是 | "{}" | 自定义属性在 Tileset 中每块定义。 这些属性通常是在 Tiled 编辑 tileset 时创建的 。 |
| tileData | object | 是 | "{}" | 数据存储在每块砖块中。这些数据通常在编辑砖块时以平面板创建,例如从平面板的瓦片碰撞编辑器或地形编辑器中创建。 |
| tileOffset | object | 是 | "{x: 0, y: 0}" | 平面纹理图画偏移 。 |

---


**作用域**: static

> 源码：[src/tilemaps/Tileset.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L10)  
引入版本：3.0.0

## 公开成员 {#public-members}

### animationSearchThreshold {#animationSearchThreshold}

#### animationSearchThreshold: number {#animationsearchthreshold-number}


**说明:**

将一个砖块上方的帧数视为有许多动画帧数。 用于优化渲染。 如果一个砖块的帧数比这个少, 则用线性搜索来搜索帧数。 如果砖块的帧数更多, 则用二进制搜索来搜索帧数 。


> 源码：[src/tilemaps/Tileset.js#L200](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L200)  
引入版本：4.0.0


---

### columns {#columns}

#### columns: number {#columns-number}


**说明:**

砖瓦组中的瓦柱数 。


> 源码：[src/tilemaps/Tileset.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L169)  
引入版本：3.0.0


---

### firstgid {#firstgid}

#### firstgid: number {#firstgid-number}


**说明:**

此 Tileset 包含的第一个瓦片索引的起始索引 。


> 源码：[src/tilemaps/Tileset.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L55)  
引入版本：3.0.0


---

### glTexture {#glTexture}

#### glTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#gltexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

WebGL渲染器使用的gl纹理.


> 源码：[src/tilemaps/Tileset.js#L149](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L149)  
引入版本：3.11.0


---

### image {#image}

#### image: [Phaser.Textures.Texture](/api/class/textures-texture) {#image-phasertexturestexture}


**说明:**

包含单个牌的缓存图像。 使用 setImage 设置 。


> 源码：[src/tilemaps/Tileset.js#L139](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L139)  
引入版本：3.0.0


---

### maxAnimationLength {#maxAnimationLength}

#### maxAnimationLength: number {#maxanimationlength-number}


**说明:**

此图案中任意动画的最大长度, 以框形式显示。 用于内部优化渲染。 调用 `createAnimationDataTexture` 时会更新 。


> 源码：[src/tilemaps/Tileset.js#L214](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L214)  
引入版本：4.0.0


---

### name {#name}

#### name: string {#name-string}


**说明:**

提勒斯人之名(出法师经).


> 源码：[src/tilemaps/Tileset.js#L46](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L46)  
引入版本：3.0.0


---

### rows {#rows}

#### rows: number {#rows-number}


**说明:**

瓦片组中的瓦片行数.


> 源码：[src/tilemaps/Tileset.js#L159](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L159)  
引入版本：3.0.0


---

### texCoordinates {#texCoordinates}

#### texCoordinates: Array.\<object> {#texcoordinates-arrayobject}


**说明:**

查找表到特定的瓦片图像纹理坐标(UV in 像素) 。 每个元素都包含在表态 {x,y} 对象中的瓦片坐标 。


> 源码：[src/tilemaps/Tileset.js#L189](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L189)  
引入版本：3.0.0


---

### tileData {#tileData}

#### tileData: object {#tiledata-object}


**说明:**

平面编辑器中通常定义的每块平面的斜面特定数据, 例如在平面碰撞编辑器中。 这是存储碰撞对象和地形的地方 。


> 源码：[src/tilemaps/Tileset.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L114)  
引入版本：3.0.0


---

### tileHeight {#tileHeight}

#### tileHeight: number {#tileheight-number}


**说明:**

每个瓦片的高度( 像素) 。 使用 setTileSize 来改变 。


> 源码：[src/tilemaps/Tileset.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L74)  
引入版本：3.0.0


---

### tileMargin {#tileMargin}

#### tileMargin: number {#tilemargin-number}


**说明:**

工作表中的瓦片周围的边距( 像素) 。 使用 `setSpacing` 来更改 。


> 源码：[src/tilemaps/Tileset.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L84)  
引入版本：3.0.0


---

### tileOffset {#tileOffset}

#### tileOffset: [Phaser.Math.Vector2](/api/class/math-vector2) {#tileoffset-phasermathvector2}


**说明:**

控制从瓦片源头的绘图偏移。默认为 0x0,没有偏移 。


> 源码：[src/tilemaps/Tileset.js#L124](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L124)  
引入版本：3.60.0


---

### tileProperties {#tileProperties}

#### tileProperties: object {#tileproperties-object}


**说明:**

平面特有属性,通常在平面编辑器中的平面编辑器中定义.


> 源码：[src/tilemaps/Tileset.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L104)  
引入版本：3.0.0


---

### tileSpacing {#tileSpacing}

#### tileSpacing: number {#tilespacing-number}


**说明:**

工作表中每块瓦之间的间隔( 像素) 。 使用 `setSpacing` 来更改 。


> 源码：[src/tilemaps/Tileset.js#L94](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L94)  
引入版本：3.0.0


---

### tileWidth {#tileWidth}

#### tileWidth: number {#tilewidth-number}


**说明:**

每个瓦片的宽度( 像素) 。 使用 setTileSize 来更改 。


> 源码：[src/tilemaps/Tileset.js#L64](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L64)  
引入版本：3.0.0


---

### total {#total}

#### total: number {#total-number}


**说明:**

砖瓦的总数.


> 源码：[src/tilemaps/Tileset.js#L179](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L179)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### containsTileIndex {#containsTileIndex}

#### \<instance> containsTileIndex(tileIndex) {#instance-containstileindextileindex}


**说明:**

如果且只有在此 Tileset 包含给定的瓷砖索引时, 返回 true 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileIndex | number | 否 | 地图上所有瓷砖上瓷砖的独有的标识. |


**返回值:** boolean - 


> 源码：[src/tilemaps/Tileset.js#L313](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L313)  
引入版本：3.0.0


---

### createAnimationDataTexture {#createAnimationDataTexture}

#### \<instance> createAnimationDataTexture(renderer) {#instance-createanimationdatatexturerenderer}


**说明:**

为 tileset 的动画数据创建新的 WebGLTexture 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拟用之造化器. |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) - 新的WebGLTexture. (原始内容存档于2018-09-29).


> 源码：[src/tilemaps/Tileset.js#L586](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L586)  
引入版本：4.0.0


---

### getAnimatedTileId {#getAnimatedTileId}

#### \<instance> getAnimatedTileId(tileIndex, milliseconds) {#instance-getanimatedtileidtileindex-milliseconds}


**说明:**

返回要使用的瓦片的ID,根据瓦片的动画属性,给底片和时间。

如果瓷砖没有动画化,这种方法返回基瓦ID.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileIndex | number | 否 | 地图上所有瓷砖上瓷砖的独有的标识. |
| milliseconds | number | 否 | 以毫秒计的当前时间 。 |


**返回值:** number - 使用该瓦片的标识,如果该瓦片未包含在本片片中,则无效。


> 源码：[src/tilemaps/Tileset.js#L331](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L331)  
引入版本：4.0.0


---

### getAnimationDataIndexMap {#getAnimationDataIndexMap}

#### \<instance> getAnimationDataIndexMap(renderer) {#instance-getanimationdataindexmaprenderer}


**说明:**

从瓷砖索引获取或创建地图到动画数据索引。 `TilemapGPULayer` 使用此图片进行动画 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拟用之造化器. |


**返回值:** Map.\<number, number> - 从瓷砖索引到动画数据索引的地图.


> 源码：[src/tilemaps/Tileset.js#L567](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L567)  
引入版本：4.0.0


---

### getAnimationDataTexture {#getAnimationDataTexture}

#### \<instance> getAnimationDataTexture(renderer) {#instance-getanimationdatatexturerenderer}


**说明:**

获取或创建包含此瓷砖动画数据的纹理。 使用 `TilemapGPULayer` 来动画瓦片 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拟用之造化器. |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) - 动画数据纹理.


> 源码：[src/tilemaps/Tileset.js#L548](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L548)  
引入版本：4.0.0


---

### getTileCollisionGroup {#getTileCollisionGroup}

#### \<instance> getTileCollisionGroup(tileIndex) {#instance-gettilecollisiongrouptileindex}


**说明:**

获取存储在 Tileset 中的瓦片碰撞组。 如果此 Tilesset 中未包含瓦片索引, 返回无效。 这通常在 Tiled 的瓦片碰撞编辑器中定义 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileIndex | number | 否 | 地图上所有瓷砖上瓷砖的独有的标识. |


**返回值:** object - 


> 源码：[src/tilemaps/Tileset.js#L295](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L295)  
引入版本：3.0.0


---

### getTileData {#getTileData}

#### \<instance> getTileData(tileIndex) {#instance-gettiledatatileindex}


**说明:**

获取存储在 Tileset 中的瓷砖数据。 如果此 Tileset 中未包含瓷砖索引, 返回无效。 这通常在 Tiled 中定义, 并同时包含 Tileset 碰撞信息和地形映射 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileIndex | number | 否 | 地图上所有瓷砖上瓷砖的独有的标识. |


**返回值:** object, undefined - 


> 源码：[src/tilemaps/Tileset.js#L276](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L276)  
引入版本：3.0.0


---

### getTileProperties {#getTileProperties}

#### \<instance> getTileProperties(tileIndex) {#instance-gettilepropertiestileindex}


**说明:**

获取存储在 Tileset 中的瓷砖属性。 如果此 Tileset 中未包含瓷砖索引, 返回无效。 这通常在 Tilest 编辑器下 Tiled 中定义 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileIndex | number | 否 | 地图上所有瓷砖上瓷砖的独有的标识. |


**返回值:** object, undefined - 


> 源码：[src/tilemaps/Tileset.js#L258](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L258)  
引入版本：3.0.0


---

### getTileTextureCoordinates {#getTileTextureCoordinates}

#### \<instance> getTileTextureCoordinates(tileIndex) {#instance-gettiletexturecoordinatestileindex}


**说明:**

返回给定的瓷砖索引的蒂莱塞特图像中的纹理坐标(以像素表示的UV)。如果该蒂莱塞特中未包含瓷砖索引,则返回无效。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileIndex | number | 否 | 地图上所有瓷砖上瓷砖的独有的标识. |


**返回值:** object - 表示蒂莱塞特图像中左上角紫外线坐标的表单 { x, y} 对象。


> 源码：[src/tilemaps/Tileset.js#L386](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L386)  
引入版本：3.0.0


---

### setImage {#setImage}

#### \<instance> setImage(texture) {#instance-setimagetexture}


**说明:**

设置与此 Tileset 相关的图像, 并更新瓷砖数据( 数列, 列等) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 包含瓷砖的图像 。 |


**返回值:** [Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset) - 此 Tilest 对象 。


> 源码：[src/tilemaps/Tileset.js#L405](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L405)  
引入版本：3.0.0


---

### setSpacing {#setSpacing}

#### \<instance> setSpacing([margin], [spacing]) {#instance-setspacingmargin-spacing}


**说明:**

设置瓦片边距和间距,并更新瓦片数据(行,列等).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| margin | number | 是 | 工作表中的瓦片周围的边距(像素). |
| spacing | number | 是 | 工作表中的瓦片之间的间隔(以像素计). |


**返回值:** [Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset) - 此 Tilest 对象 。


> 源码：[src/tilemaps/Tileset.js#L461](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L461)  
引入版本：3.0.0


---

### setTileSize {#setTileSize}

#### \<instance> setTileSize([tileWidth], [tileHeight]) {#instance-settilesizetilewidth-tileheight}


**说明:**

设置瓦片宽度和高度,并更新瓦片数据(行,列等).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileWidth | number | 是 | 以像素表示的瓦片宽度 。 |
| tileHeight | number | 是 | 瓦片在像素中的高度. |


**返回值:** [Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset) - 此 Tilest 对象 。


> 源码：[src/tilemaps/Tileset.js#L437](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L437)  
引入版本：3.0.0


---

### updateTileData {#updateTileData}

#### \<instance> updateTileData(imageWidth, imageHeight, [offsetX], [offsetY]) {#instance-updatetiledataimagewidth-imageheight-offsetx-offsety}


**说明:**

更新瓷砖纹理坐标和瓷砖数据。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| imageWidth | number | 否 |  | 图像切片的(预期)宽度 。 |
| imageHeight | number | 否 |  | 图像切片的(预期)高度。 |
| offsetX | number | 是 | 0 | 砖头开始处的源纹理中x抵消. |
| offsetY | number | 是 | 0 | 砖头开始处的源纹理中y 抵消。 |


**返回值:** [Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset) - 此 Tilest 对象 。


> 源码：[src/tilemaps/Tileset.js#L485](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tileset.js#L485)  
引入版本：3.0.0


---

---
