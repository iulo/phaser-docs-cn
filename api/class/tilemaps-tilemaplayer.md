# TilemapLayer {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tilemaps-tilemaplayer)

蒂莱玛普Layer 是负责从蒂莱玛普中渲染一层瓦片数据的游戏对象。 它与一个或多个蒂莱塞特对象结合工作, 提供了实际的瓦片图像。 您通常会通过 `Tilemap.createLayer` 创建蒂莱玛普Leyer, 而不是直接即时生成 。

每个层对应Tilemap内部的LyerData条目,支持所有四个地图方向:Orthogonal、Isometric、Hixagonal和Stagggered。该层处理自己的相机卷动,只向渲染器发送可见的瓷砖,即使对大地图来说,也保持了性能效率。

TilemapLayers通过Arcade Physics和Mater.js支持物理学,并且可以有锡,α,以及其他标准游戏对象属性应用到它们.

提列玛普莱尔可以放在容器里,但是它的物理原理会像它直接放在世界里一样起作用。这很少是你想要的。

**构造函数**

`new TilemapLayer(scene, tilemap, layerIndex, tileset, [x], [y])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属景点 。 |
| tilemap | [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) | 否 |  | 蒂拉玛普这个层是其中的一部分. |
| layerIndex | number | 否 |  | 与此层相关的图层数据索引 。 |
| tileset | string \| Array.\<string> | [Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset) | Array.\<[Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset)> | 否 |  | 用于制导此图层的瓦片组或一系列瓦片。可以是字符串或蒂列塞特对象 。 |
| x | number | 是 | 0 | 将这个层的左上方放置的世界x位置. |
| y | number | 是 | 0 | 将这个层的左上方放置在 y 位置的世界 。 |

---


**作用域**: static


**继承**

> [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase)  



> 源码：[src/tilemaps/TilemapLayer.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L14)  
引入版本：3.50.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha):**


 - [alpha](/api/namespace/gameobjects-components-alpha#alpha)
 - [alphaBottomLeft](/api/namespace/gameobjects-components-alpha#alphaBottomLeft)
 - [alphaBottomRight](/api/namespace/gameobjects-components-alpha#alphaBottomRight)
 - [alphaTopLeft](/api/namespace/gameobjects-components-alpha#alphaTopLeft)
 - [alphaTopRight](/api/namespace/gameobjects-components-alpha#alphaTopRight)





**From [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode):**


 - [blendMode](/api/namespace/gameobjects-components-blendmode#blendMode)





**From [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize):**


 - [displayHeight](/api/namespace/gameobjects-components-computedsize#displayHeight)
 - [displayWidth](/api/namespace/gameobjects-components-computedsize#displayWidth)
 - [height](/api/namespace/gameobjects-components-computedsize#height)
 - [width](/api/namespace/gameobjects-components-computedsize#width)





**From [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth):**


 - [depth](/api/namespace/gameobjects-components-depth#depth)





**From [Phaser.GameObjects.Components.ElapseTimer](/api/namespace/gameobjects-components-elapsetimer):**


 - [timeElapsed](/api/namespace/gameobjects-components-elapsetimer#timeElapsed)
 - [timeElapsedResetPeriod](/api/namespace/gameobjects-components-elapsetimer#timeElapsedResetPeriod)
 - [timePaused](/api/namespace/gameobjects-components-elapsetimer#timePaused)





**From [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters):**


 - [filterCamera](/api/namespace/gameobjects-components-filters#filterCamera)
 - [filters](/api/namespace/gameobjects-components-filters#filters)
 - [filtersAutoFocus](/api/namespace/gameobjects-components-filters#filtersAutoFocus)
 - [filtersFocusContext](/api/namespace/gameobjects-components-filters#filtersFocusContext)
 - [filtersForceComposite](/api/namespace/gameobjects-components-filters#filtersForceComposite)
 - [maxFilterSize](/api/namespace/gameobjects-components-filters#maxFilterSize)
 - [renderFilters](/api/namespace/gameobjects-components-filters#renderFilters)





**From [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip):**


 - [flipX](/api/namespace/gameobjects-components-flip#flipX)
 - [flipY](/api/namespace/gameobjects-components-flip#flipY)





**From [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting):**


 - [lighting](/api/namespace/gameobjects-components-lighting#lighting)
 - [selfShadow](/api/namespace/gameobjects-components-lighting#selfShadow)





**From [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask):**


 - [mask](/api/namespace/gameobjects-components-mask#mask)





**From [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes):**


 - [customRenderNodes](/api/namespace/gameobjects-components-rendernodes#customRenderNodes)
 - [defaultRenderNodes](/api/namespace/gameobjects-components-rendernodes#defaultRenderNodes)
 - [renderNodeData](/api/namespace/gameobjects-components-rendernodes#renderNodeData)





**From [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor):**


 - [scrollFactorX](/api/namespace/gameobjects-components-scrollfactor#scrollFactorX)
 - [scrollFactorY](/api/namespace/gameobjects-components-scrollfactor#scrollFactorY)





**From [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform):**


 - [angle](/api/namespace/gameobjects-components-transform#angle)
 - [hasTransformComponent](/api/namespace/gameobjects-components-transform#hasTransformComponent)
 - [rotation](/api/namespace/gameobjects-components-transform#rotation)
 - [scale](/api/namespace/gameobjects-components-transform#scale)
 - [scaleX](/api/namespace/gameobjects-components-transform#scaleX)
 - [scaleY](/api/namespace/gameobjects-components-transform#scaleY)
 - [w](/api/namespace/gameobjects-components-transform#w)
 - [x](/api/namespace/gameobjects-components-transform#x)
 - [y](/api/namespace/gameobjects-components-transform#y)
 - [z](/api/namespace/gameobjects-components-transform#z)





**From [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible):**


 - [visible](/api/namespace/gameobjects-components-visible#visible)





**From [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject):**


 - [active](/api/class/gameobjects-gameobject#active)
 - [body](/api/class/gameobjects-gameobject#body)
 - [cameraFilter](/api/class/gameobjects-gameobject#cameraFilter)
 - [data](/api/class/gameobjects-gameobject#data)
 - [displayList](/api/class/gameobjects-gameobject#displayList)
 - [ignoreDestroy](/api/class/gameobjects-gameobject#ignoreDestroy)
 - [input](/api/class/gameobjects-gameobject#input)
 - [isDestroyed](/api/class/gameobjects-gameobject#isDestroyed)
 - [name](/api/class/gameobjects-gameobject#name)
 - [parentContainer](/api/class/gameobjects-gameobject#parentContainer)
 - [renderFlags](/api/class/gameobjects-gameobject#renderFlags)
 - [scene](/api/class/gameobjects-gameobject#scene)
 - [state](/api/class/gameobjects-gameobject#state)
 - [tabIndex](/api/class/gameobjects-gameobject#tabIndex)
 - [type](/api/class/gameobjects-gameobject#type)
 - [vertexRoundMode](/api/class/gameobjects-gameobject#vertexRoundMode)





**From [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase):**


 - [collisionCategory](/api/class/tilemaps-tilemaplayerbase#collisionCategory)
 - [collisionMask](/api/class/tilemaps-tilemaplayerbase#collisionMask)
 - [displayOriginX](/api/class/tilemaps-tilemaplayerbase#displayOriginX)
 - [displayOriginY](/api/class/tilemaps-tilemaplayerbase#displayOriginY)
 - [gidMap](/api/class/tilemaps-tilemaplayerbase#gidMap)
 - [isTilemap](/api/class/tilemaps-tilemaplayerbase#isTilemap)
 - [layer](/api/class/tilemaps-tilemaplayerbase#layer)
 - [layerIndex](/api/class/tilemaps-tilemaplayerbase#layerIndex)
 - [originX](/api/class/tilemaps-tilemaplayerbase#originX)
 - [originY](/api/class/tilemaps-tilemaplayerbase#originY)
 - [tilemap](/api/class/tilemaps-tilemaplayerbase#tilemap)




---

## 公开成员 {#public-members}

### cullCallback {#cullCallback}

#### cullCallback: function {#cullcallback-function}


**说明:**

瓷砖被挤碎时引用的回调 。

它将调用基于地图方向的另一种功能:

正弦( 默认) 是 `TilemapComponents.CullTiles` 偏差是: 偏差是: 偏差是: 偏差是: 偏差是: 偏差是: 偏差是: 偏差是: 偏差是: 偏差是: 偏差是: 偏差是: 偏差是: `TilemapComponents.IsometricCullTiles` 六边形是 `TilemapComponents.HexagonalCullTiles` 错位是 `TilemapComponents.StaggeredCullTiles`

然而, 您可以更改此功能以调用您喜欢的任何函数 。

将发出4项论点:

1. 此图层的 Phaser.Tilemaps.LayerData 对象

2. 正在切换层的相机。 您可以检查其 `dirty` 属性, 看看它是否自上次凹槽后有所改变 。

3. 引用 `culledTiles` 阵列,该阵列应该用来存储要渲染的瓷砖.

4. 伦德秩序常数.

有关实施自己调制系统的细节,请参见`TilemapComponents.CullTiles`源代码.


> 源码：[src/tilemaps/TilemapLayer.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L136)  
引入版本：3.50.0


---

### culledTiles {#culledTiles}

#### culledTiles: Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> {#culledtiles-arrayphasertilemapstile}


**说明:**

内部渲染时使用, 上面有相机内可见的瓷砖 。


> 源码：[src/tilemaps/TilemapLayer.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L89)  
引入版本：3.50.0


---

### cullPaddingX {#cullPaddingX}

#### cullPaddingX: number {#cullpaddingx-number}


**说明:**

在计算其水平大小时,将加进凸起矩形的瓦片数量。

详见方法`setCullPadding`.


> 源码：[src/tilemaps/TilemapLayer.js#L112](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L112)  
引入版本：3.50.0


---

### cullPaddingY {#cullPaddingY}

#### cullPaddingY: number {#cullpaddingy-number}


**说明:**

计算垂直大小时, 将加到凸起矩形中的瓦片数 。

详见方法`setCullPadding`.


> 源码：[src/tilemaps/TilemapLayer.js#L124](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L124)  
引入版本：3.50.0


---

### skipCull {#skipCull}

#### skipCull: boolean {#skipcull-boolean}


**说明:**

你可以控制摄像机是否在制作之前 粘在地上

默认情况下,相机会尝试将瓷砖堆积在这个层中,以避免过度地拖到渲染器上.

然而,有些情况下,您可能希望禁用此选项, 并使用此标记来显示您可以这样做。 也可以使用`setSkipCull` 来查看可链路方法, 它可以做同样的事情 。


> 源码：[src/tilemaps/TilemapLayer.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L98)  
引入版本：3.50.0


---

### tilesDrawn {#tilesDrawn}

#### tilesDrawn: number {#tilesdrawn-number}


**说明:**

最后一个框中渲染器绘制的瓦片总数.


> 源码：[src/tilemaps/TilemapLayer.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L69)  
引入版本：3.50.0


---

### tileset {#tileset}

#### tileset: Array.\<[Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset)> {#tileset-arrayphasertilemapstileset}


**说明:**

与此层相关的 `Tileset` 对象阵列 。


> 源码：[src/tilemaps/TilemapLayer.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L60)  
引入版本：3.50.0


---

### tilesTotal {#tilesTotal}

#### tilesTotal: number {#tilestotal-number}


**说明:**

此图层的牌数总数。 更新了每个框架 。


> 源码：[src/tilemaps/TilemapLayer.js#L79](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L79)  
引入版本：3.50.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Events.EventEmitter](/api/class/events-eventemitter):**


 - [addListener](/api/class/events-eventemitter#addListener)
 - [emit](/api/class/events-eventemitter#emit)
 - [eventNames](/api/class/events-eventemitter#eventNames)
 - [listenerCount](/api/class/events-eventemitter#listenerCount)
 - [listeners](/api/class/events-eventemitter#listeners)
 - [off](/api/class/events-eventemitter#off)
 - [on](/api/class/events-eventemitter#on)
 - [once](/api/class/events-eventemitter#once)
 - [removeAllListeners](/api/class/events-eventemitter#removeAllListeners)
 - [removeListener](/api/class/events-eventemitter#removeListener)
 - [shutdown](/api/class/events-eventemitter#shutdown)





**From [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha):**


 - [clearAlpha](/api/namespace/gameobjects-components-alpha#clearAlpha)
 - [setAlpha](/api/namespace/gameobjects-components-alpha#setAlpha)





**From [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode):**


 - [setBlendMode](/api/namespace/gameobjects-components-blendmode#setBlendMode)





**From [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize):**


 - [setDisplaySize](/api/namespace/gameobjects-components-computedsize#setDisplaySize)
 - [setSize](/api/namespace/gameobjects-components-computedsize#setSize)





**From [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth):**


 - [setAbove](/api/namespace/gameobjects-components-depth#setAbove)
 - [setBelow](/api/namespace/gameobjects-components-depth#setBelow)
 - [setDepth](/api/namespace/gameobjects-components-depth#setDepth)
 - [setToBack](/api/namespace/gameobjects-components-depth#setToBack)
 - [setToTop](/api/namespace/gameobjects-components-depth#setToTop)





**From [Phaser.GameObjects.Components.ElapseTimer](/api/namespace/gameobjects-components-elapsetimer):**


 - [resetTimer](/api/namespace/gameobjects-components-elapsetimer#resetTimer)
 - [setTimerPaused](/api/namespace/gameobjects-components-elapsetimer#setTimerPaused)
 - [setTimerResetPeriod](/api/namespace/gameobjects-components-elapsetimer#setTimerResetPeriod)
 - [updateTimer](/api/namespace/gameobjects-components-elapsetimer#updateTimer)





**From [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters):**


 - [enableFilters](/api/namespace/gameobjects-components-filters#enableFilters)
 - [focusFilters](/api/namespace/gameobjects-components-filters#focusFilters)
 - [focusFiltersOnCamera](/api/namespace/gameobjects-components-filters#focusFiltersOnCamera)
 - [focusFiltersOverride](/api/namespace/gameobjects-components-filters#focusFiltersOverride)
 - [renderWebGLFilters](/api/namespace/gameobjects-components-filters#renderWebGLFilters)
 - [setFiltersAutoFocus](/api/namespace/gameobjects-components-filters#setFiltersAutoFocus)
 - [setFiltersFocusContext](/api/namespace/gameobjects-components-filters#setFiltersFocusContext)
 - [setFiltersForceComposite](/api/namespace/gameobjects-components-filters#setFiltersForceComposite)
 - [setFilterSize](/api/namespace/gameobjects-components-filters#setFilterSize)
 - [setRenderFilters](/api/namespace/gameobjects-components-filters#setRenderFilters)
 - [willRenderFilters](/api/namespace/gameobjects-components-filters#willRenderFilters)





**From [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip):**


 - [resetFlip](/api/namespace/gameobjects-components-flip#resetFlip)
 - [setFlip](/api/namespace/gameobjects-components-flip#setFlip)
 - [setFlipX](/api/namespace/gameobjects-components-flip#setFlipX)
 - [setFlipY](/api/namespace/gameobjects-components-flip#setFlipY)
 - [toggleFlipX](/api/namespace/gameobjects-components-flip#toggleFlipX)
 - [toggleFlipY](/api/namespace/gameobjects-components-flip#toggleFlipY)





**From [Phaser.GameObjects.Components.GetBounds](/api/namespace/gameobjects-components-getbounds):**


 - [getBottomCenter](/api/namespace/gameobjects-components-getbounds#getBottomCenter)
 - [getBottomLeft](/api/namespace/gameobjects-components-getbounds#getBottomLeft)
 - [getBottomRight](/api/namespace/gameobjects-components-getbounds#getBottomRight)
 - [getBounds](/api/namespace/gameobjects-components-getbounds#getBounds)
 - [getCenter](/api/namespace/gameobjects-components-getbounds#getCenter)
 - [getLeftCenter](/api/namespace/gameobjects-components-getbounds#getLeftCenter)
 - [getRightCenter](/api/namespace/gameobjects-components-getbounds#getRightCenter)
 - [getTopCenter](/api/namespace/gameobjects-components-getbounds#getTopCenter)
 - [getTopLeft](/api/namespace/gameobjects-components-getbounds#getTopLeft)
 - [getTopRight](/api/namespace/gameobjects-components-getbounds#getTopRight)





**From [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting):**


 - [setLighting](/api/namespace/gameobjects-components-lighting#setLighting)
 - [setSelfShadow](/api/namespace/gameobjects-components-lighting#setSelfShadow)





**From [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask):**


 - [clearMask](/api/namespace/gameobjects-components-mask#clearMask)
 - [createGeometryMask](/api/namespace/gameobjects-components-mask#createGeometryMask)
 - [setMask](/api/namespace/gameobjects-components-mask#setMask)





**From [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin):**


 - [setDisplayOrigin](/api/namespace/gameobjects-components-origin#setDisplayOrigin)
 - [setOrigin](/api/namespace/gameobjects-components-origin#setOrigin)
 - [setOriginFromFrame](/api/namespace/gameobjects-components-origin#setOriginFromFrame)
 - [updateDisplayOrigin](/api/namespace/gameobjects-components-origin#updateDisplayOrigin)





**From [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes):**


 - [initRenderNodes](/api/namespace/gameobjects-components-rendernodes#initRenderNodes)
 - [setRenderNodeData](/api/namespace/gameobjects-components-rendernodes#setRenderNodeData)
 - [setRenderNodeRole](/api/namespace/gameobjects-components-rendernodes#setRenderNodeRole)





**From [Phaser.GameObjects.Components.RenderSteps](/api/namespace/gameobjects-components-rendersteps):**


 - [addRenderStep](/api/namespace/gameobjects-components-rendersteps#addRenderStep)
 - [renderWebGLStep](/api/namespace/gameobjects-components-rendersteps#renderWebGLStep)





**From [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor):**


 - [setScrollFactor](/api/namespace/gameobjects-components-scrollfactor#setScrollFactor)





**From [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform):**


 - [copyPosition](/api/namespace/gameobjects-components-transform#copyPosition)
 - [getLocalPoint](/api/namespace/gameobjects-components-transform#getLocalPoint)
 - [getLocalTransformMatrix](/api/namespace/gameobjects-components-transform#getLocalTransformMatrix)
 - [getParentRotation](/api/namespace/gameobjects-components-transform#getParentRotation)
 - [getWorldPoint](/api/namespace/gameobjects-components-transform#getWorldPoint)
 - [getWorldTransformMatrix](/api/namespace/gameobjects-components-transform#getWorldTransformMatrix)
 - [setAngle](/api/namespace/gameobjects-components-transform#setAngle)
 - [setPosition](/api/namespace/gameobjects-components-transform#setPosition)
 - [setRandomPosition](/api/namespace/gameobjects-components-transform#setRandomPosition)
 - [setRotation](/api/namespace/gameobjects-components-transform#setRotation)
 - [setScale](/api/namespace/gameobjects-components-transform#setScale)
 - [setW](/api/namespace/gameobjects-components-transform#setW)
 - [setX](/api/namespace/gameobjects-components-transform#setX)
 - [setY](/api/namespace/gameobjects-components-transform#setY)
 - [setZ](/api/namespace/gameobjects-components-transform#setZ)





**From [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible):**


 - [setVisible](/api/namespace/gameobjects-components-visible#setVisible)





**From [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject):**


 - [addToDisplayList](/api/class/gameobjects-gameobject#addToDisplayList)
 - [addToUpdateList](/api/class/gameobjects-gameobject#addToUpdateList)
 - [disableInteractive](/api/class/gameobjects-gameobject#disableInteractive)
 - [getData](/api/class/gameobjects-gameobject#getData)
 - [getDisplayList](/api/class/gameobjects-gameobject#getDisplayList)
 - [getIndexList](/api/class/gameobjects-gameobject#getIndexList)
 - [incData](/api/class/gameobjects-gameobject#incData)
 - [removeFromDisplayList](/api/class/gameobjects-gameobject#removeFromDisplayList)
 - [removeFromUpdateList](/api/class/gameobjects-gameobject#removeFromUpdateList)
 - [removeInteractive](/api/class/gameobjects-gameobject#removeInteractive)
 - [setActive](/api/class/gameobjects-gameobject#setActive)
 - [setData](/api/class/gameobjects-gameobject#setData)
 - [setDataEnabled](/api/class/gameobjects-gameobject#setDataEnabled)
 - [setInteractive](/api/class/gameobjects-gameobject#setInteractive)
 - [setName](/api/class/gameobjects-gameobject#setName)
 - [setState](/api/class/gameobjects-gameobject#setState)
 - [setVertexRoundMode](/api/class/gameobjects-gameobject#setVertexRoundMode)
 - [toggleData](/api/class/gameobjects-gameobject#toggleData)
 - [toJSON](/api/class/gameobjects-gameobject#toJSON)
 - [update](/api/class/gameobjects-gameobject#update)
 - [willRender](/api/class/gameobjects-gameobject#willRender)
 - [willRoundVertices](/api/class/gameobjects-gameobject#willRoundVertices)





**From [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision):**


 - [addCollidesWith](/api/namespace/physics-arcade-components-collision#addCollidesWith)
 - [removeCollidesWith](/api/namespace/physics-arcade-components-collision#removeCollidesWith)
 - [resetCollisionCategory](/api/namespace/physics-arcade-components-collision#resetCollisionCategory)
 - [setCollidesWith](/api/namespace/physics-arcade-components-collision#setCollidesWith)
 - [setCollisionCategory](/api/namespace/physics-arcade-components-collision#setCollisionCategory)
 - [willCollideWith](/api/namespace/physics-arcade-components-collision#willCollideWith)





**From [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase):**


 - [addedToScene](/api/class/tilemaps-tilemaplayerbase#addedToScene)
 - [calculateFacesAt](/api/class/tilemaps-tilemaplayerbase#calculateFacesAt)
 - [calculateFacesWithin](/api/class/tilemaps-tilemaplayerbase#calculateFacesWithin)
 - [copy](/api/class/tilemaps-tilemaplayerbase#copy)
 - [createFromTiles](/api/class/tilemaps-tilemaplayerbase#createFromTiles)
 - [fill](/api/class/tilemaps-tilemaplayerbase#fill)
 - [filterTiles](/api/class/tilemaps-tilemaplayerbase#filterTiles)
 - [findByIndex](/api/class/tilemaps-tilemaplayerbase#findByIndex)
 - [findTile](/api/class/tilemaps-tilemaplayerbase#findTile)
 - [forEachTile](/api/class/tilemaps-tilemaplayerbase#forEachTile)
 - [getIsoTileAtWorldXY](/api/class/tilemaps-tilemaplayerbase#getIsoTileAtWorldXY)
 - [getTileAt](/api/class/tilemaps-tilemaplayerbase#getTileAt)
 - [getTileAtWorldXY](/api/class/tilemaps-tilemaplayerbase#getTileAtWorldXY)
 - [getTileCorners](/api/class/tilemaps-tilemaplayerbase#getTileCorners)
 - [getTilesWithin](/api/class/tilemaps-tilemaplayerbase#getTilesWithin)
 - [getTilesWithinShape](/api/class/tilemaps-tilemaplayerbase#getTilesWithinShape)
 - [getTilesWithinWorldXY](/api/class/tilemaps-tilemaplayerbase#getTilesWithinWorldXY)
 - [hasTileAt](/api/class/tilemaps-tilemaplayerbase#hasTileAt)
 - [hasTileAtWorldXY](/api/class/tilemaps-tilemaplayerbase#hasTileAtWorldXY)
 - [preUpdate](/api/class/tilemaps-tilemaplayerbase#preUpdate)
 - [putTileAt](/api/class/tilemaps-tilemaplayerbase#putTileAt)
 - [putTileAtWorldXY](/api/class/tilemaps-tilemaplayerbase#putTileAtWorldXY)
 - [putTilesAt](/api/class/tilemaps-tilemaplayerbase#putTilesAt)
 - [randomize](/api/class/tilemaps-tilemaplayerbase#randomize)
 - [removedFromScene](/api/class/tilemaps-tilemaplayerbase#removedFromScene)
 - [removeTileAt](/api/class/tilemaps-tilemaplayerbase#removeTileAt)
 - [removeTileAtWorldXY](/api/class/tilemaps-tilemaplayerbase#removeTileAtWorldXY)
 - [renderDebug](/api/class/tilemaps-tilemaplayerbase#renderDebug)
 - [replaceByIndex](/api/class/tilemaps-tilemaplayerbase#replaceByIndex)
 - [setCollision](/api/class/tilemaps-tilemaplayerbase#setCollision)
 - [setCollisionBetween](/api/class/tilemaps-tilemaplayerbase#setCollisionBetween)
 - [setCollisionByExclusion](/api/class/tilemaps-tilemaplayerbase#setCollisionByExclusion)
 - [setCollisionByProperty](/api/class/tilemaps-tilemaplayerbase#setCollisionByProperty)
 - [setCollisionFromCollisionGroup](/api/class/tilemaps-tilemaplayerbase#setCollisionFromCollisionGroup)
 - [setTileIndexCallback](/api/class/tilemaps-tilemaplayerbase#setTileIndexCallback)
 - [setTileLocationCallback](/api/class/tilemaps-tilemaplayerbase#setTileLocationCallback)
 - [shuffle](/api/class/tilemaps-tilemaplayerbase#shuffle)
 - [swapByIndex](/api/class/tilemaps-tilemaplayerbase#swapByIndex)
 - [tileToWorldX](/api/class/tilemaps-tilemaplayerbase#tileToWorldX)
 - [tileToWorldXY](/api/class/tilemaps-tilemaplayerbase#tileToWorldXY)
 - [tileToWorldY](/api/class/tilemaps-tilemaplayerbase#tileToWorldY)
 - [weightedRandomize](/api/class/tilemaps-tilemaplayerbase#weightedRandomize)
 - [worldToTileX](/api/class/tilemaps-tilemaplayerbase#worldToTileX)
 - [worldToTileXY](/api/class/tilemaps-tilemaplayerbase#worldToTileXY)
 - [worldToTileY](/api/class/tilemaps-tilemaplayerbase#worldToTileY)




---

## 公开方法 {#public-methods}

### cull {#cull}

#### \<instance> cull([camera]) {#instance-cullcamera}


**说明:**

返回相机视图中给定的图层中的牌。 渲染时会内部使用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 监控库尔的摄像机 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 一系列要渲染的拼图对象 。


> 源码：[src/tilemaps/TilemapLayer.js#L296](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L296)  
引入版本：3.50.0


---

### destroy {#destroy}

#### \<instance> destroy([removeFromTilemap]) {#instance-destroyremovefromtilemap}


**说明:**

销毁此 TilemapLayer, 清除 culled 牌组并删除 cull 调用。 如果 `removeFromTilemap` 设定为 `true`, 也从 cull 中移除 tull 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| removeFromTilemap | boolean | 是 | true | 在销毁前从母端的 Tilemap 中删除此层 。 |


**Overrides:** Phaser.Tilemaps.TilemapLayerBase#销毁


> 源码：[src/tilemaps/TilemapLayer.js#L439](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L439)  
引入版本：3.50.0


---

### setCullPadding {#setCullPadding}

#### \<instance> setCullPadding([paddingX], [paddingY]) {#instance-setcullpaddingpaddingx-paddingy}


**说明:**

当相机将图片堆积在这个层中时, 它会利用它的视线进入世界, 建立一个矩形, 内有图片, 或它们会被熔化。 有时你可能需要扩大这个“ 凸轮形” 的大小, 尤其是如果您计划旋转相机查看层。 通过提供粘贴值来做到这一点。 给出的值是瓦片, 而不是像素。 所以如果平面宽度为 32px, 您将 `paddingX` 设置为 4, 它会给凸轮形加32px x 4( 调整比例) 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| paddingX | number | 是 | 1 | 加入 cull 检查 垫的 水平瓦片 。 |
| paddingY | number | 是 | 1 | 加入 cull 检查粘贴板的附加垂直瓦片的量 。 |


**返回值:** [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayer.js#L335](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L335)  
引入版本：3.50.0


---

### setRenderOrder {#setRenderOrder}

#### \<instance> setRenderOrder(renderOrder) {#instance-setrenderorderrenderorder}


**说明:**

设置此图层的渲染( draw) 顺序 。

默认为“ 右下方 ” , 意思是它会命令从左上方开始的牌, 向右画, 然后移动到下一行 。

抽签命令如下:

0=右下 1=左下 2=右上 3=左下 1=左下 1=左下 1=左下 1=左下 1=左下 1=左下 1=左下 1=左下 1=左下 1=右下 2=右上 3=左下 1=左下 1=左下 3=左下 1=左下 3=左下 1=左下 3=左下 3=左下 3 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右 右

设定渲染顺序不会改变瓷砖或如何将瓷砖储存在地层中,它会完全影响其渲染顺序.

既可以提供整数(0至3),也可以提供顺序的字符串版本.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderOrder | number \| string | 否 | 渲染(draw) 顺序值。 或整数在 0 到 3 之间, 或字符串 : “ 右下” 、 “ 左下” 、 “ 右上” 或 “ 左上” 。 |


**返回值:** [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayer.js#L254](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L254)  
引入版本：3.50.0


---

### setSkipCull {#setSkipCull}

#### \<instance> setSkipCull([value]) {#instance-setskipcullvalue}


**说明:**

你可以控制摄像机在制作之前是否要磨碎瓷砖。

默认情况下,相机会尝试将瓷砖堆积在这个层中,以避免过度地拖到渲染器上.

但是,有时您可能希望禁用此功能。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 设定为 `true` 停止 culling 瓦片 设定为 `false` 允许 culling 重现 。 |


**返回值:** [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayer.js#L312](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L312)  
引入版本：3.50.0


---

### setTint {#setTint}

#### \<instance> setTint([tint], [tileX], [tileY], [width], [height], [filteringOptions]) {#instance-settinttint-tilex-tiley-width-height-filteringoptions}


**说明:**

在指定区域内的每个瓦片上设置一个添加剂锡。

锡的功效在于从砖块纹理中取出像素的颜色值,然后用锡的颜色值乘以.

如果没有给出区域值,则所有牌将用给定的颜色涂上。

要删除一个无参数的锡称这种方法,或者通过通过白色的`0xffffff`作为锡的颜色.

如果瓷砖已经装了个小装置 那么使用这种方法就可以超过这个

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tint | number | 是 | "0xffffff" | 区域内每块瓷砖都应用着锡色。 以六进制值为单位, 即红色的 `0xff0000` 。 设置为白色( `0xffffff`) , 以重置锡色 。 |
| tileX | number | 是 |  | 左侧最瓦的索引(在瓦片坐标中)作为搜索区域的来源. |
| tileY | number | 是 |  | 用于搜索区域源头的最顶层的瓦片索引(在瓦片坐标中). |
| width | number | 是 |  | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 |  | 有多少块高的瓷砖从 `tileY` 索引区域将。 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 是 |  | 获得瓷砖时可选择的过滤器。 |


**返回值:** [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayer.js#L361](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L361)  
引入版本：3.60.0


---

### setTintMode {#setTintMode}

#### \<instance> setTintMode([tintMode], [tileX], [tileY], [width], [height], [filteringOptions]) {#instance-settintmodetintmode-tilex-tiley-width-height-filteringoptions}


**说明:**

设置将锡语应用到纹理时使用的锡字模式。

可用模式有:

- Phaser.TintModes.MULTIPLY( 默认)

- Phaser.TintModes.FILL

- Phaser.TintModes.ADD

- Phaser.TintModes.SCREEN

- Phaser.TintModes.OVERLAY

- Phaser.TintModes.HARD_LIGHT

使用此方法没有参数可以重设锡特模式为默认值 。

如果一块瓷砖已经有一个锡模式设置,那么调用这种方法将覆盖它 。

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tintMode | [Phaser.TintModes](/api/namespace/tintmodes) | 是 | "Phaser.TintModes.MULTIPLY" | 使用锡金模式 。 |
| tileX | number | 是 |  | 左侧最瓦的索引(在瓦片坐标中)作为搜索区域的来源. |
| tileY | number | 是 |  | 用于搜索区域源头的最顶层的瓦片索引(在瓦片坐标中). |
| width | number | 是 |  | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 |  | 有多少块高的瓷砖从 `tileY` 索引区域将。 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 是 |  | 获得瓷砖时可选择的过滤器。 |


**返回值:** [Phaser.Tilemaps.TilemapLayer](/api/class/tilemaps-tilemaplayer) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayer.js#L398](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayer.js#L398)  
引入版本：4.0.0


---

---
