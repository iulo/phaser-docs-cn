# Tile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tilemaps-tile)

平面图是图层内单砖的表示。 每个平面图在图网格内有一个位置( 以平面坐标表示), 大小像素, 其四个边缘的碰撞标志, 从平面图编辑器中导入的可选自定义属性, 以及可选的碰撞回调。 平面是轻量级数据对象 - 它们不扩展 Game Object - 因此其像素位置相对于图层来源是存储的, 并且不考虑相机滚动、 层尺度或层位置 。 使用该图板 。 `getLeft`, `getRight`, `getTop`, `getBottom`,和 `getBounds` 获得世界空间坐标的方法,以说明这些变化。

平面由 `TilemapLayer` 创建和管理,通常不应直接被即时化。您可以通过 `TilemapLayer.getTileAt` 或类似的 Tilemap 方法访问它们 。

**构造函数**

`new Tile(layer, index, x, y, width, height, baseWidth, baseHeight)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| layer | [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) | 否 | Tilemap 中的 LayerData 对象属于此牌。 |
| index | number | 否 | 地图中这种瓦片的独特索引 。 |
| x | number | 否 | 这块瓷砖的x坐标在瓷砖坐标中. |
| y | number | 否 | 这张瓷砖的Y坐标在瓷砖坐标中. |
| width | number | 否 | 瓦片的宽度以像素表示. |
| height | number | 否 | 瓦片高度以像素表示. |
| baseWidth | number | 否 | 地图中基底宽度为瓦片(以像素计). 平面图支持一个地图内多个瓦片大小,但它们仍然被放置在基底瓦片宽度的间隔处. |
| baseHeight | number | 否 | 瓦片在像素中的基高. 斜拉图支持一个图中的多个瓦片大小,但它们仍然被放置在基高的间隔处. |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle)  
> [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/tilemaps/Tile.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L14)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle):**


 - [alpha](/api/namespace/gameobjects-components-alphasingle#alpha)





**From [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip):**


 - [flipX](/api/namespace/gameobjects-components-flip#flipX)
 - [flipY](/api/namespace/gameobjects-components-flip#flipY)





**From [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible):**


 - [visible](/api/namespace/gameobjects-components-visible#visible)




---

## 公开成员 {#public-members}

### baseHeight {#baseHeight}

#### baseHeight: number {#baseheight-number}


**说明:**

地图的基部高度为像素中的瓦片,平面图支持一个地图内的多个瓦片大小,但它们仍然被放置在基部瓦片大小的间隔处.


> 源码：[src/tilemaps/Tile.js#L148](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L148)  
引入版本：3.0.0


---

### baseWidth {#baseWidth}

#### baseWidth: number {#basewidth-number}


**说明:**

地图的基宽度为像素中的瓦片,平面图支持一个地图内的多个瓦片大小,但它们仍然被放置在基片大小的间隔处.


> 源码：[src/tilemaps/Tile.js#L138](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L138)  
引入版本：3.0.0


---

### bottom {#bottom}

#### bottom: number {#bottom-number}


**说明:**

瓦片的底部以像素表示.

设定在 `updatePixelXY`方法中.


> 源码：[src/tilemaps/Tile.js#L127](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L127)  
引入版本：3.50.0


---

### canCollide {#canCollide}

#### canCollide: boolean {#cancollide-boolean}


**说明:**

如果这瓷砖能撞到它的脸 或者有碰撞回调装置的话,那就是真的了。


> 源码：[src/tilemaps/Tile.js#L872](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L872)  
引入版本：3.0.0


---

### collideDown {#collideDown}

#### collideDown: boolean {#collidedown-boolean}


**说明:**

是否将瓷砖与底部的任何物体相撞。

这块地产只被Arcade物理使用, 不过,你也可以在自己的支票中使用.


> 源码：[src/tilemaps/Tile.js#L236](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L236)  
引入版本：3.0.0


---

### collideLeft {#collideLeft}

#### collideLeft: boolean {#collideleft-boolean}


**说明:**

是否将瓷砖与左边的任何物体相撞。

这块地产只被Arcade物理使用, 不过,你也可以在自己的支票中使用.


> 源码：[src/tilemaps/Tile.js#L200](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L200)  
引入版本：3.0.0


---

### collideRight {#collideRight}

#### collideRight: boolean {#collideright-boolean}


**说明:**

是否将牌与任何物体在右侧相撞 。

这块地产只被Arcade物理使用, 不过,你也可以在自己的支票中使用.


> 源码：[src/tilemaps/Tile.js#L212](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L212)  
引入版本：3.0.0


---

### collides {#collides}

#### collides: boolean {#collides-boolean}


**说明:**

如果这瓷砖能撞到它的脸上 是真的


> 源码：[src/tilemaps/Tile.js#L889](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L889)  
引入版本：3.0.0


---

### collideUp {#collideUp}

#### collideUp: boolean {#collideup-boolean}


**说明:**

是否将瓷砖与任何物体碰撞在顶端 。

这块地产只被Arcade物理使用, 不过,你也可以在自己的支票中使用.


> 源码：[src/tilemaps/Tile.js#L224](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L224)  
引入版本：3.0.0


---

### collisionCallback {#collisionCallback}

#### collisionCallback: function {#collisioncallback-function}


**说明:**

当Arcade物理体与这个瓦片相撞时,可选的调回功能被引用。调回必须返回 `true`, 才能进行碰撞处理。 通过 `setCollisionCallback`设定 。


> 源码：[src/tilemaps/Tile.js#L284](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L284)  
引入版本：3.0.0


---

### collisionCallbackContext {#collisionCallbackContext}

#### collisionCallbackContext: object {#collisioncallbackcontext-object}


**说明:**

碰撞回调的上下文 。


> 源码：[src/tilemaps/Tile.js#L295](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L295)  
引入版本：3.0.0


---

### faceBottom {#faceBottom}

#### faceBottom: boolean {#facebottom-boolean}


**说明:**

瓦片的底部边缘是否对碰撞感兴趣.


> 源码：[src/tilemaps/Tile.js#L275](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L275)  
引入版本：3.0.0


---

### faceLeft {#faceLeft}

#### faceLeft: boolean {#faceleft-boolean}


**说明:**

瓦片的左边缘是否对碰撞有意思.


> 源码：[src/tilemaps/Tile.js#L248](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L248)  
引入版本：3.0.0


---

### faceRight {#faceRight}

#### faceRight: boolean {#faceright-boolean}


**说明:**

瓷砖的右边缘是否对碰撞有意思.


> 源码：[src/tilemaps/Tile.js#L257](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L257)  
引入版本：3.0.0


---

### faceTop {#faceTop}

#### faceTop: boolean {#facetop-boolean}


**说明:**

瓦片的顶端是否对碰撞感兴趣.


> 源码：[src/tilemaps/Tile.js#L266](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L266)  
引入版本：3.0.0


---

### hasInterestingFace {#hasInterestingFace}

#### hasInterestingFace: boolean {#hasinterestingface-boolean}


**说明:**

如果这瓷砖有有趣的面孔的话,那就是真的了。


> 源码：[src/tilemaps/Tile.js#L906](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L906)  
引入版本：3.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

瓦片在像素中的高度.


> 源码：[src/tilemaps/Tile.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L107)  
引入版本：3.0.0


---

### index {#index}

#### index: number {#index-number}


**说明:**

与平面图对应的地图数据中此瓦的索引, 或 - 1 如果它代表空白的平面图 。


> 源码：[src/tilemaps/Tile.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L70)  
引入版本：3.0.0


---

### layer {#layer}

#### layer: [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) {#layer-phasertilemapslayerdata}


**说明:**

此瓷砖所属的 Tilemap 数据中的 LayerData 。


> 源码：[src/tilemaps/Tile.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L61)  
引入版本：3.0.0


---

### physics {#physics}

#### physics: object {#physics-object}


**说明:**

空物体,其中可以存储物理-引擎特定信息(如天体).


> 源码：[src/tilemaps/Tile.js#L333](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L333)  
引入版本：3.0.0


---

### pixelX {#pixelX}

#### pixelX: number {#pixelx-number}


**说明:**

此瓦片左上方的x坐标以像素表示。 这是相对于此瓦片内部制成的图层左上方的。 此属性不考虑相机滚动、 图层缩放或图层位置 。


> 源码：[src/tilemaps/Tile.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L158)  
引入版本：3.0.0


---

### pixelY {#pixelY}

#### pixelY: number {#pixely-number}


**说明:**

以像素表示的此瓦片左上方的y坐标。 这是相对于此瓦片在内部制成的图层左上方的。 此属性不考虑相机滚动、 图层缩放或图层位置 。


> 源码：[src/tilemaps/Tile.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L169)  
引入版本：3.0.0


---

### properties {#properties}

#### properties: any {#properties-any}


**说明:**

拼贴特性,通常来自拼贴。


> 源码：[src/tilemaps/Tile.js#L182](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L182)  
引入版本：3.0.0


---

### right {#right}

#### right: number {#right-number}


**说明:**

瓦片在像素中的右侧.

设定在 `updatePixelXY`方法中.


> 源码：[src/tilemaps/Tile.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L116)  
引入版本：3.50.0


---

### rotation {#rotation}

#### rotation: number {#rotation-number}


**说明:**

此瓦片的旋转角度 。


> 源码：[src/tilemaps/Tile.js#L191](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L191)  
引入版本：3.0.0


---

### tilemap {#tilemap}

#### tilemap: [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) {#tilemap-phasertilemapstilemap}


**说明:**

包含此图案的图案。 只有在图案放在图案表内之前, 才能从图案数据库中访问到此图案, 才会返回无效 。


> 源码：[src/tilemaps/Tile.js#L972](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L972)  
引入版本：3.0.0


---

### tilemapLayer {#tilemapLayer}

#### tilemapLayer: [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) {#tilemaplayer-phasertilemapstilemaplayer}


**说明:**

包含此图案的图案层。 只有在图案放在图案层内之前, 才能从图案数据库中访问到此图案层时, 才会返回无效 。


> 源码：[src/tilemaps/Tile.js#L954](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L954)  
引入版本：3.0.0


---

### tileset {#tileset}

#### tileset: [Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset) {#tileset-phasertilemapstileset}


**说明:**

包含此图案的平板块。 如果在图案被放置在图案之前从图案数据库中访问到图案, 或者如果图案的索引与地图上的任何图案不匹配, 则此选项无效 。


> 源码：[src/tilemaps/Tile.js#L923](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L923)  
引入版本：3.0.0


---

### tint {#tint}

#### tint: number {#tint-number}


**说明:**

适用于此牌的锡。 注意: 锡目前是一个单一的颜色值, 而不是其他 Game Objects 上的 4 角锡组件 。


> 源码：[src/tilemaps/Tile.js#L304](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L304)  
引入版本：3.0.0


---

### tintMode {#tintMode}

#### tintMode: [Phaser.TintModes](/api/namespace/tintmodes) {#tintmode-phasertintmodes}


**说明:**

锡模式.

可用模式有:

- Phaser.TintModes.MULTIPLY( 默认)

- Phaser.TintModes.FILL

- Phaser.TintModes.ADD

- Phaser.TintModes.SCREEN

- Phaser.TintModes.OVERLAY

- Phaser.TintModes.HARD_LIGHT


> 源码：[src/tilemaps/Tile.js#L315](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L315)  
引入版本：4.0.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

瓦片以像素表示的宽度.


> 源码：[src/tilemaps/Tile.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L98)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

以瓦片单位表示的此瓦片的x映射坐标.


> 源码：[src/tilemaps/Tile.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L80)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

以瓦片单位表示的此瓦片的y地图坐标 。


> 源码：[src/tilemaps/Tile.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L89)  
引入版本：3.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle):**


 - [clearAlpha](/api/namespace/gameobjects-components-alphasingle#clearAlpha)
 - [setAlpha](/api/namespace/gameobjects-components-alphasingle#setAlpha)





**From [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip):**


 - [resetFlip](/api/namespace/gameobjects-components-flip#resetFlip)
 - [setFlip](/api/namespace/gameobjects-components-flip#setFlip)
 - [setFlipX](/api/namespace/gameobjects-components-flip#setFlipX)
 - [setFlipY](/api/namespace/gameobjects-components-flip#setFlipY)
 - [toggleFlipX](/api/namespace/gameobjects-components-flip#toggleFlipX)
 - [toggleFlipY](/api/namespace/gameobjects-components-flip#toggleFlipY)





**From [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible):**


 - [setVisible](/api/namespace/gameobjects-components-visible#setVisible)




---

## 公开方法 {#public-methods}

### containsPoint {#containsPoint}

#### \<instance> containsPoint(x, y) {#instance-containspointx-y}


**说明:**

检查给定的 x 和 y 世界坐标是否在此图中。 这不计入相机滚动、 层缩放或层位置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 使用x坐标测试. |
| y | number | 否 | 测试的Y坐标 |


**返回值:** boolean - 如果坐标在这块地上,那么就是真的,否则就是假的。


> 源码：[src/tilemaps/Tile.js#L343](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L343)  
引入版本：3.0.0


---

### copy {#copy}

#### \<instance> copy(tile) {#instance-copytile}


**说明:**

将所给的瓷砖数据及属性复制到此瓷砖。 除了位置和有趣的面部计算之外, 其它所有都复制 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tile | [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 瓦片从复制。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 此拼图对象实例 。


> 源码：[src/tilemaps/Tile.js#L360](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L360)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁这种瓦片,方法是取消其碰撞回调和自定义属性,释放出本来可以防止垃圾收集的参考文献。


> 源码：[src/tilemaps/Tile.js#L858](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L858)  
引入版本：3.0.0


---

### getBottom {#getBottom}

#### \<instance> getBottom([camera]) {#instance-getbottomcamera}


**说明:**

获得瓦片底侧的世界 Y 位置, 将图层的位置, 缩放和滚动计算 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用来检查的摄像机 |


**返回值:** number - 此牌的底部( Y) 值 。


> 源码：[src/tilemaps/Tile.js#L492](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L492)  
引入版本：3.0.0


---

### getBounds {#getBounds}

#### \<instance> getBounds([camera], [output]) {#instance-getboundscamera-output}


**说明:**

获得瓦片的世界矩形边框,在层的位置,尺度和卷轴中进行计数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用来检查的摄像机 |
| output | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 可选矩形对象存储结果。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle), object - 此瓦之界.


> 源码：[src/tilemaps/Tile.js#L512](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L512)  
引入版本：3.0.0


---

### getCenterX {#getCenterX}

#### \<instance> getCenterX([camera]) {#instance-getcenterxcamera}


**说明:**

获得瓷砖中心的世界X位置,在层的位置,尺度和卷轴中进行计分.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用来检查的摄像机 |


**返回值:** number - 这个砖块的中心X位置.


> 源码：[src/tilemaps/Tile.js#L536](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L536)  
引入版本：3.0.0


---

### getCenterY {#getCenterY}

#### \<instance> getCenterY([camera]) {#instance-getcenterycamera}


**说明:**

获得瓦片中心的世界Y位置,在层的位置中进行计分,尺度和卷轴.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用来检查的摄像机 |


**返回值:** number - 这张纸的中线位置 。


> 源码：[src/tilemaps/Tile.js#L552](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L552)  
引入版本：3.0.0


---

### getCollisionGroup {#getCollisionGroup}

#### \<instance> getCollisionGroup() {#instance-getcollisiongroup}


**说明:**

此图案的碰撞组, 定义在 Tileset 内。 这返回了对存储在 Tileset内碰撞组的引用, 因此对返回对象的任何修改都会影响所有与该图案相同的索引的图案 。


**返回值:** object - 蒂莱塞特定义的此图案的碰撞组,如果没有定义组,则使用`null`。


> 源码：[src/tilemaps/Tile.js#L390](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L390)  
引入版本：3.0.0


---

### getLeft {#getLeft}

#### \<instance> getLeft([camera]) {#instance-getleftcamera}


**说明:**

获得砖块左侧的世界X位置,在层的位置,尺度和卷轴中计算.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用来检查的摄像机 |


**返回值:** number - 此瓷砖的左( x) 值 。


> 源码：[src/tilemaps/Tile.js#L421](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L421)  
引入版本：3.0.0


---

### getRight {#getRight}

#### \<instance> getRight([camera]) {#instance-getrightcamera}


**说明:**

获得瓷砖右侧的世界X位置,在层的位置,尺度和卷轴中进行计分.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用来检查的摄像机 |


**返回值:** number - 此牌的右值( x) 。


> 源码：[src/tilemaps/Tile.js#L446](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L446)  
引入版本：3.0.0


---

### getTileData {#getTileData}

#### \<instance> getTileData() {#instance-gettiledata}


**说明:**

此图案的瓦片数据, 定义在 Tileset 中。 这通常包含 Tiled 碰撞数据、 瓦片动画和地形信息。 这返回了对 Tileset 内存储的瓦片数据的引用, 因此对返回对象的任何修改都会影响所有与该图案相同的索引的瓦片 。


**返回值:** object - 平板电脑,在Tileset中定义,如果没有定义数据,则使用`null`。


> 源码：[src/tilemaps/Tile.js#L405](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L405)  
引入版本：3.0.0


---

### getTop {#getTop}

#### \<instance> getTop([camera]) {#instance-gettopcamera}


**说明:**

获得瓦片顶部的Y世界位置,在层的位置,尺度和卷轴中进行计分.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用来检查的摄像机 |


**返回值:** number - 此瓷砖的顶值( Y) 。


> 源码：[src/tilemaps/Tile.js#L464](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L464)  
引入版本：3.0.0


---

### intersects {#intersects}

#### \<instance> intersects(x, y, right, bottom) {#instance-intersectsx-y-right-bottom}


**说明:**

检查与此牌的交叉点。 这不考虑相机滚动、 层缩放或层位置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 矩形的左边缘与相交,以像素表示. |
| y | number | 否 | 与矩形交错的顶端边缘,以像素表示. |
| right | number | 否 | 矩形的右边缘与相交,以像素表示. |
| bottom | number | 否 | 矩形的下边缘与相交,以像素表示. |


**返回值:** boolean - `true` 如果图案与给定的维度相交, 否则 `false`.


> 源码：[src/tilemaps/Tile.js#L568](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L568)  
引入版本：3.0.0


---

### isInteresting {#isInteresting}

#### \<instance> isInteresting(collides, faces) {#instance-isinterestingcollides-faces}


**说明:**

检查此牌是否根据所提供的标准被视为“ 兴趣 ” 。 如果牌面有主动碰撞标记, 或根据所通过参数显示其正面或两者均有趣, 则牌面是否很有趣 。 瓦片碰撞系统内部用于快速过滤需要进一步处理的牌面 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| collides | boolean | 否 | 如果是真的,如果瓷砖在任何一边碰撞,那么它会觉得这瓷砖很有趣。 |
| faces | boolean | 否 | 如果是真的,如果它有有趣的面孔,它会觉得瓷砖很有趣. |


**返回值:** boolean - 如果这牌子有趣的话,否则就是假的


> 源码：[src/tilemaps/Tile.js#L590](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L590)  
引入版本：3.0.0


---

### resetCollision {#resetCollision}

#### \<instance> resetCollision([recalculateFaces]) {#instance-resetcollisionrecalculatefaces}


**说明:**

将此牌盘上的所有碰撞状态标记重置到 `false`, 清除其四个边缘上设置的任何碰撞。 如果 `recalculateFaces` 是真的( 默认) , 也会重新计算该牌盘及其在层中的邻居的有趣的面旗 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| recalculateFaces | boolean | 是 | true | 是否要为这瓷砖和它的邻居 重新计算有趣的面孔 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 此拼图对象实例 。


> 源码：[src/tilemaps/Tile.js#L622](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L622)  
引入版本：3.0.0


---

### resetFaces {#resetFaces}

#### \<instance> resetFaces() {#instance-resetfaces}


**说明:**

重新设置所有四个有趣的面旗( R)`faceTop`, `faceBottom`, `faceLeft`, `faceRight`改为 `false`。与 `resetCollision`,这并不影响碰撞的旗帜,也不会引发对邻近的瓷砖的面部重新计算.


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 此拼图对象实例 。


> 源码：[src/tilemaps/Tile.js#L661](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L661)  
引入版本：3.0.0


---

### setCollision {#setCollision}

#### \<instance> setCollision(left, [right], [up], [down], [recalculateFaces]) {#instance-setcollisionleft-right-up-down-recalculatefaces}


**说明:**

设置此牌的两侧的碰撞标记, 并更新有趣的面额列表 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| left | boolean | 否 |  | 表示与左边任何物体相撞。 |
| right | boolean | 是 |  | 指与任何物体在右边相撞。 |
| up | boolean | 是 |  | 表示与任何物体在顶部相撞。 |
| down | boolean | 是 |  | 表示与底部任何物体相撞。 |
| recalculateFaces | boolean | 是 | true | 是否要为这瓷砖和它的邻居 重新计算有趣的面孔 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 此拼图对象实例 。


> 源码：[src/tilemaps/Tile.js#L681](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L681)  
引入版本：3.0.0


---

### setCollisionCallback {#setCollisionCallback}

#### \<instance> setCollisionCallback(callback, context) {#instance-setcollisioncallbackcallback-context}


**说明:**

设定一个调用符, 当此牌被对象击中时, 将调用符。 调用符必须返回真实值, 才能进行碰撞处理 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | function | 否 | 召回功能. |
| context | object | 否 | 将在这一背景下召回。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 此拼图对象实例 。


> 源码：[src/tilemaps/Tile.js#L725](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L725)  
引入版本：3.0.0


---

### setSize {#setSize}

#### \<instance> setSize(tileWidth, tileHeight, baseWidth, baseHeight) {#instance-setsizetilewidth-tileheight-basewidth-baseheight}


**说明:**

设置瓦片大小并更新其pixelX和pixelY.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileWidth | number | 否 | 瓦片以像素表示的宽度. |
| tileHeight | number | 否 | 瓦片在像素中的高度. |
| baseWidth | number | 否 | 地图中基部宽度为瓦片(以像素计). |
| baseHeight | number | 否 | 瓦片在像素中的基高. |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 此拼图对象实例 。


> 源码：[src/tilemaps/Tile.js#L753](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L753)  
引入版本：3.0.0


---

### updatePixelXY {#updatePixelXY}

#### \<instance> updatePixelXY() {#instance-updatepixelxy}


**说明:**

内部使用。 根据当前瓦片大小更新瓦片的世界 XY 位置 。


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 此拼图对象实例 。


> 源码：[src/tilemaps/Tile.js#L778](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/Tile.js#L778)  
引入版本：3.0.0


---

---
