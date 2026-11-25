# TilemapLayerBase {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tilemaps-tilemaplayerbase)

TIlemapLayer 是一个游戏对象,它使 LyerData 在使用时与一个或多个 Tilesets 组合起来, 使 LyermapLayer 从 Tilemap 中生成。 这是一个通用的基础类, 由 TilemapLaye 类扩展。 它不是直接使用的, 不应该被即时使用 。

**构造函数**

`new TilemapLayerBase(scene, tilemap, layerIndex, [x], [y])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属景点 。 |
| tilemap | [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) | 否 |  | 蒂拉玛普这个层是其中的一部分. |
| layerIndex | number | 否 |  | 与此层相关的图层数据索引 。 |
| x | number | 是 | 0 | 将这个层的左上方放置的世界x位置. |
| y | number | 是 | 0 | 将这个层的左上方放置在 y 位置的世界 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.ElapseTimer](/api/namespace/gameobjects-components-elapsetimer)  
> [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip)  
> [Phaser.GameObjects.Components.GetBounds](/api/namespace/gameobjects-components-getbounds)  
> [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting)  
> [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask)  
> [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin)  
> [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  
> [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision)  



> 源码：[src/tilemaps/TilemapLayerBase.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L14)  
引入版本：4.0.0

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




---

## 公开成员 {#public-members}

### collisionCategory {#collisionCategory}

#### collisionCategory: number {#collisioncategory-number}


**说明:**

蒂勒马普层碰撞类.

这完全由Arcade物理系统使用.

它可以设置为任何有效的碰撞位域值 。

详见`setCollisionCategory`方法.


> 源码：[src/tilemaps/TilemapLayerBase.js#L140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L140)  
引入版本：3.70.0


---

### collisionMask {#collisionMask}

#### collisionMask: number {#collisionmask-number}


**说明:**

蒂莱玛普层碰撞罩.

这完全由Arcade物理系统使用.

详见`setCollidesWith`方法.


> 源码：[src/tilemaps/TilemapLayerBase.js#L155](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L155)  
引入版本：3.70.0


---

### displayOriginX {#displayOriginX}

#### displayOriginX: number {#displayoriginx-number}


**说明:**

此 Tilemap 层的横向显示源 。


**重写:** Phaser.GameObjects.Components.Origin#displayOriginX


> 源码：[src/tilemaps/TilemapLayerBase.js#L188](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L188)  
引入版本：3.0.0


---

### displayOriginY {#displayOriginY}

#### displayOriginY: number {#displayoriginy-number}


**说明:**

此 Tilemap 层的垂直显示源 。


**重写:** Phaser.GameObjects.Components.Origin#displayOriginY


> 源码：[src/tilemaps/TilemapLayerBase.js#L198](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L198)  
引入版本：3.0.0


---

### gidMap {#gidMap}

#### gidMap: Array.\<[Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset)> {#gidmap-arrayphasertilemapstileset}


**说明:**

在一个图片索引和它们所属的图片之间保持映射的阵列。


> 源码：[src/tilemaps/TilemapLayerBase.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L121)  
引入版本：3.50.0


---

### isTilemap {#isTilemap}

#### isTilemap: boolean {#istilemap-boolean}


**说明:**

内部被物理系统用于进行快速类型检查.


> 源码：[src/tilemaps/TilemapLayerBase.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L80)  
引入版本：3.50.0


---

### layer {#layer}

#### layer: [Phaser.Tilemaps.LayerData](/api/class/tilemaps-layerdata) {#layer-phasertilemapslayerdata}


**说明:**

与此图层相关的图层Data。 LyerData 只能与一个图层连接 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L108)  
引入版本：3.50.0


---

### layerIndex {#layerIndex}

#### layerIndex: number {#layerindex-number}


**说明:**

与此层相关的图层数据索引 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L99)  
引入版本：3.50.0


---

### originX {#originX}

#### originX: number {#originx-number}


**说明:**

此 Tilemap 层的横向来源 。


**重写:** Phaser.GameObjects.Components.Origin#originX


> 源码：[src/tilemaps/TilemapLayerBase.js#L168](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L168)  
引入版本：3.0.0


---

### originY {#originY}

#### originY: number {#originy-number}


**说明:**

此 Tilemap 层的垂直源 。


**重写:** Phaser.GameObjects.Components.Origin#originY


> 源码：[src/tilemaps/TilemapLayerBase.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L178)  
引入版本：3.0.0


---

### tilemap {#tilemap}

#### tilemap: [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) {#tilemap-phasertilemapstilemap}


**说明:**

这个层是其中的一部分的提列玛普.


> 源码：[src/tilemaps/TilemapLayerBase.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L90)  
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




---

## 公开方法 {#public-methods}

### addedToScene {#addedToScene}

#### \<instance> addedToScene() {#instance-addedtoscene}


**说明:**

此方法在游戏对象添加时被 Scene 自动称为 。 它会用 Scene 的更新列表来注册该层, 这样 `preUpdate`Z 就可以称为每个游戏步骤 。


**重写:** Phaser.GameObjects.GameObject#addedToScene


> 源码：[src/tilemaps/TilemapLayerBase.js#L214](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L214)  
引入版本：4.0.0


---

### calculateFacesAt {#calculateFacesAt}

#### \<instance> calculateFacesAt(tileX, tileY) {#instance-calculatefacesattilex-tiley}


**说明:**

在指定的层的瓦片坐标处计算有趣的面。 有趣的面用于优化与瓦片的碰撞。 这种方法大多用于在仅更改一个瓦片时优化再计算面。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | 坐标是x |
| tileY | number | 否 | 调和器 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L253](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L253)  
引入版本：3.50.0


---

### calculateFacesWithin {#calculateFacesWithin}

#### \<instance> calculateFacesWithin([tileX], [tileY], [width], [height]) {#instance-calculatefaceswithintilex-tiley-width-height}


**说明:**

计算层的矩形区域( 平面坐标) 内有趣的面孔。 有趣的面孔用于优化与瓦片的碰撞。 这种方法大多在内部使用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L273](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L273)  
引入版本：3.50.0


---

### copy {#copy}

#### \<instance> copy(srcTileX, srcTileY, width, height, destTileX, destTileY, [recalculateFaces]) {#instance-copysrctilex-srctiley-width-height-desttilex-desttiley-recalculatefaces}


**说明:**

复制源长方形区域中的瓦片到层内的新目的地( 全部在瓦片坐标中指定) 。 复制所有瓦片属性并重新计算目的地区域的碰撞信息 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| srcTileX | number | 否 |  | 要复制的区域的x坐标,以瓦片表示,而不是像素. |
| srcTileY | number | 否 |  | 要复制的区域的y坐标, 以瓦片而不是像素表示 。 |
| width | number | 否 |  | 要复制的区域的宽度,以瓦片表示,而不是像素. |
| height | number | 否 |  | 要复制的区域的高度,以瓦片表示,而不是像素. |
| destTileX | number | 否 |  | 要复制的区域的x坐标,以瓦片表示,而不是像素. |
| destTileY | number | 否 |  | 区域y坐标以瓦片形式复制,而不是像素。 |
| recalculateFaces | boolean | 是 | true | 如果面额数据应重新计算,则使用`true`。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L320](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L320)  
引入版本：3.50.0


---

### createFromTiles {#createFromTiles}

#### \<instance> createFromTiles(indexes, replacements, [spriteConfig], [scene], [camera]) {#instance-createfromtilesindexes-replacements-spriteconfig-scene-camera}


**说明:**

为每个匹配层中给定的瓦片索引的对象创建 Sprite。 您可以选择指定每个瓦片是否在 Sprite 创建后被替换为新瓦片。 如果您想要在转换成 Sprite 的级别下置特殊瓦片, 但想要在转换后将瓦片本身替换为地板瓦片或类似的瓦片, 则此操作是有用的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| indexes | number \| array | 否 | 砖块索引,或指向的数组,用来创建Sprites。 |
| replacements | number \| array | 否 | 将转换的瓦片转换为 . 设置为 `null` 使瓦片保持不变。 如果给出了数组, 则假定它是与索引数组的一对一映射 。 |
| spriteConfig | [Phaser.Types.GameObjects.Sprite.SpriteConfig](/api/typedef/types-gameobjects-sprite#spriteconfig) | 是 | 配置对象可以传递到Sprite创建者(即场景. make.sprite)中. |
| scene | [Phaser.Scene](/api/class/scene) | 是 | 创造内在的斯普丽特的场景. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用于确定 XY 世界的摄像机 |


**返回值:** Array.\<[Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite)> - 创建的 Sprite 阵列 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L295](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L295)  
引入版本：3.50.0


---

### destroy {#destroy}

#### \<instance> destroy([removeFromTilemap]) {#instance-destroyremovefromtilemap}


**说明:**

摧毁此 TilemapLayer 并删除其与关联的LayerData 的链接。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| removeFromTilemap | boolean | 是 | true | 从父图解中移除此层 ? |


**重写:** Phaser.GameObjects.GameObject#销毁


> 源码：[src/tilemaps/TilemapLayerBase.js#L1173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L1173)  
引入版本：3.50.0


---

### fill {#fill}

#### \<instance> fill(index, [tileX], [tileY], [width], [height], [recalculateFaces]) {#instance-fillindex-tilex-tiley-width-height-recalculatefaces}


**说明:**

设置图层的矩形区域( 以瓦片坐标) 中的瓦片与指定的索引相配合。 如果指定的索引是碰撞索引, 则图层将被设定为碰撞。 区域中的碰撞信息将被重新计算 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| index | number | 否 |  | 填充区域用的瓦片索引 。 |
| tileX | number | 是 |  | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 |  | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 |  | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 |  | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| recalculateFaces | boolean | 是 | true | 如果面额数据应重新计算,则使用`true`。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L345](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L345)  
引入版本：3.50.0


---

### filterTiles {#filterTiles}

#### \<instance> filterTiles(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions]) {#instance-filtertilescallback-context-tilex-tiley-width-height-filteringoptions}


**说明:**

对于图层中指定矩形区域(在平面坐标)的每个瓦片,运行给定的过滤回调功能。任何通过过滤测试的瓦片(即回调返回真实的)都将作为新阵列返回。类似于 Array.prototytype.Filter 在vanilla JS 中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | function | 否 | 回调。 指定区域的每一块牌将传递给这个回调, 作为第一个也是唯一的参数。 回调应该返回通过过滤器的牌的真值 。 |
| context | object | 是 | 恢复召回的场合 。 |
| tileX | number | 是 | 左最瓦索引(在瓦座坐标中)用作过滤区域的来源. |
| tileY | number | 是 | 用于过滤区域源头的最顶部的瓦片索引(在瓦片坐标中). |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 是 | 获得瓦片时可选择的过滤器。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 一系列的平板物体。


> 源码：[src/tilemaps/TilemapLayerBase.js#L369](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L369)  
引入版本：3.50.0


---

### findByIndex {#findByIndex}

#### \<instance> findByIndex(index, [skip], [reverse]) {#instance-findbyindexindex-skip-reverse}


**说明:**

搜索第一个匹配给定索引的图板的整层地图,然后返回该图板对象。如果找不到匹配,则返回无效。搜索从左上方的图板开始,并水平地持续到其到达行的末尾,然后下降至下一行。如果反向布尔值是真实的,则从右下角扫描,从上到左上。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| index | number | 否 |  | 要搜索的瓦片索引值 。 |
| skip | number | 是 | 0 | 返回前跳过匹配的瓦片的次数 。 |
| reverse | boolean | 是 | false | 如果真有, 它会逆向扫描层, 从右下方开始。 否则它会从左上方扫描 。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 第一个匹配的平板对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L394](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L394)  
引入版本：3.50.0


---

### findTile {#findTile}

#### \<instance> findTile(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions]) {#instance-findtilecallback-context-tilex-tiley-width-height-filteringoptions}


**说明:**

找到该图层中符合所提供测试功能的第一个长方形区域( 砖座坐标)的瓦片。 I. 即找到 `callback` 返回真实的第一瓦片。 类似于 Array. prototype. find in vanilla JS 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | FindTileCallback | 否 | 回调。 指定区域内的每个瓦片都会被传递到这个回调中, 作为第一个也是唯一的参数 。 |
| context | object | 是 | 恢复召回的场合 。 |
| tileX | number | 是 | 左侧最瓦的索引(在瓦片坐标中)作为搜索区域的来源. |
| tileY | number | 是 | 用于搜索区域源头的最顶层的瓦片索引(在瓦片坐标中). |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 是 | 获得瓦片时可选择的过滤器。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 第一个在指定地点发现的图案.


> 源码：[src/tilemaps/TilemapLayerBase.js#L415](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L415)  
引入版本：3.50.0


---

### forEachTile {#forEachTile}

#### \<instance> forEachTile(callback, [context], [tileX], [tileY], [width], [height], [filteringOptions]) {#instance-foreachtilecallback-context-tilex-tiley-width-height-filteringoptions}


**说明:**

对于在给定的长方形区域(在平面坐标)中的每个瓦片,运行给定的调回。类似于 Array.prototive 。forEach 以梵蒂冈JS为主

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | EachTileCallback | 否 | 回调。 指定区域内的每个瓦片都会被传递到这个回调中, 作为第一个也是唯一的参数 。 |
| context | object | 是 | 恢复召回的上下文或范围。 |
| tileX | number | 是 | 左侧最瓦的索引(在瓦片坐标中)作为搜索区域的来源. |
| tileY | number | 是 | 用于搜索区域源头的最顶层的瓦片索引(在瓦片坐标中). |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 是 | 获得瓦片时可选择的过滤器。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L438](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L438)  
引入版本：3.50.0


---

### getIsoTileAtWorldXY {#getIsoTileAtWorldXY}

#### \<instance> getIsoTileAtWorldXY(worldX, worldY, [originTop], [nonNull], [camera]) {#instance-getisotileatworldxyworldx-worldy-origintop-nonnull-camera}


**说明:**

从给定的同位素层获得给定世界坐标的瓦片。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| worldX | number | 否 |  | 从(以像素形式给出)获取瓦片的 X 位置 |
| worldY | number | 否 |  | Y 位置从 (以像素形式给出) 获取牌 |
| originTop | boolean | 是 | true | 何为等位牌的正面 ? 顶部( 默认, 真实) 还是底部 ? (假) |
| nonNull | boolean | 是 | false | 对于空的牌,返回索引为 -1 的牌标对象,而不是空的牌标。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 |  | 从世界值计算瓦片索引时使用的摄像机 。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 指定坐标的瓦片,如果找不到瓦片或坐标无效,则无效。


> 源码：[src/tilemaps/TilemapLayerBase.js#L497](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L497)  
引入版本：3.60.0


---

### getTileAt {#getTileAt}

#### \<instance> getTileAt(tileX, tileY, [nonNull]) {#instance-gettileattilex-tiley-nonnull}


**说明:**

从给定的地层获得给定的地砖坐标的瓦片。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tileX | number | 否 |  | X 位置从( 以瓦片单位表示, 不以像素表示) 获取瓦片 。 |
| tileY | number | 否 |  | Y 位置从( 以瓦片单位表示, 而非像素) 得到瓦片 。 |
| nonNull | boolean | 是 | false | 对于空的牌,返回索引为 -1 的牌标对象,而不是空的牌标。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 指定坐标的平板,如果没有找到平板,或坐标无效,则无效。


> 源码：[src/tilemaps/TilemapLayerBase.js#L462](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L462)  
引入版本：3.50.0


---

### getTileAtWorldXY {#getTileAtWorldXY}

#### \<instance> getTileAtWorldXY(worldX, worldY, [nonNull], [camera]) {#instance-gettileatworldxyworldx-worldy-nonnull-camera}


**说明:**

从给定的地层获得给定的世界坐标的瓦片。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| worldX | number | 否 |  | 从(以像素形式给出)获取瓦片的 X 位置 |
| worldY | number | 否 |  | Y 位置从 (以像素形式给出) 获取牌 |
| nonNull | boolean | 是 | false | 对于空的牌,返回索引为 -1 的牌标对象,而不是空的牌标。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 |  | 从世界值计算瓦片索引时使用的摄像机 。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 指定坐标的瓦片,如果找不到瓦片或坐标无效,则无效。


> 源码：[src/tilemaps/TilemapLayerBase.js#L479](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L479)  
引入版本：3.50.0


---

### getTileCorners {#getTileCorners}

#### \<instance> getTileCorners(tileX, tileY, [camera]) {#instance-gettilecornerstilex-tiley-camera}


**说明:**

返回一个矢量2的数组,每个条目对应所请求的瓦片的角。

`tileX`和`tileY`参数在瓦片坐标,而不是世界坐标.

角坐标位于世界空间,如果给出,则在TilemapLayer比例、位置和摄像机中计及。

阵列的大小会因地图的方向而异。 例如, 直径图将返回4个向量的阵列, 作为六边形图, 自然会返回6个角向量的阵列。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 返回矢量2的数组,如果给出的图层无效,则返回为无效。


> 源码：[src/tilemaps/TilemapLayerBase.js#L1049](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L1049)  
引入版本：3.60.0


---

### getTilesWithin {#getTilesWithin}

#### \<instance> getTilesWithin([tileX], [tileY], [width], [height], [filteringOptions]) {#instance-gettileswithintilex-tiley-width-height-filteringoptions}


**说明:**

获取图层的指定矩形区域(在图砖坐标内)的瓦片。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 是 | 获得瓦片时可选择的过滤器。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 在区域内发现的一组平板物体。


> 源码：[src/tilemaps/TilemapLayerBase.js#L522](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L522)  
引入版本：3.50.0


---

### getTilesWithinShape {#getTilesWithinShape}

#### \<instance> getTilesWithinShape(shape, [filteringOptions], [camera]) {#instance-gettileswithinshapeshape-filteringoptions-camera}


**说明:**

获取与指定图层中的形状重叠的牌。形状必须是圆形、线形、矩形或三角形。形状应在世界坐标中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| shape | [Phaser.Geom.Circle](/api/class/geom-circle) \| [Phaser.Geom.Line](/api/class/geom-line) | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 世界的形状( 像素) 坐标 |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 是 | 获得瓦片时可选择的过滤器。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用于计算返回的瓦片的摄像机。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 在形状中发现的一组平板物体。


> 源码：[src/tilemaps/TilemapLayerBase.js#L541](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L541)  
引入版本：3.50.0


---

### getTilesWithinWorldXY {#getTilesWithinWorldXY}

#### \<instance> getTilesWithinWorldXY(worldX, worldY, width, height, [filteringOptions], [camera]) {#instance-gettileswithinworldxyworldx-worldy-width-height-filteringoptions-camera}


**说明:**

获取该层指定矩形区域(世界坐标)的瓦片.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | 地球X坐标为该地区左上角. |
| worldY | number | 否 | 地球和坐标是该地区左上角 |
| width | number | 否 | 面积宽度. |
| height | number | 否 | 地区高度. |
| filteringOptions | [Phaser.Types.Tilemaps.FilteringOptions](/api/typedef/types-tilemaps#filteringoptions) | 是 | 获得瓦片时可选择的过滤器。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用于计算返回的瓦片的摄像机。 |


**返回值:** Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> - 在区域内发现的一组平板物体。


> 源码：[src/tilemaps/TilemapLayerBase.js#L559](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L559)  
引入版本：3.50.0


---

### hasTileAt {#hasTileAt}

#### \<instance> hasTileAt(tileX, tileY) {#instance-hastileattilex-tiley}


**说明:**

检查在给定的层中(在砖座坐标)的指定位置是否有一个瓦片。如果没有瓦片,或者该位置的瓦片有−1的索引,返回时会弄虚作假。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |


**返回值:** boolean - 如果在指定地点找到一块瓦子,则使用`true`,否则使用`false`.


> 源码：[src/tilemaps/TilemapLayerBase.js#L579](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L579)  
引入版本：3.50.0


---

### hasTileAtWorldXY {#hasTileAtWorldXY}

#### \<instance> hasTileAtWorldXY(worldX, worldY, [camera]) {#instance-hastileatworldxyworldx-worldy-camera}


**说明:**

检查指定位置( 世界坐标) 是否有瓦片。 如果没有瓦片, 或者该位置的瓦片有 - 1 的索引, 返回时会弄虚作假 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | x坐标,以像素表示. |
| worldY | number | 否 | y坐标,以像素表示. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 用于计算返回的瓦片的摄像机。 |


**返回值:** boolean - 如果在指定地点找到一块瓦子,则使用`true`,否则使用`false`.


> 源码：[src/tilemaps/TilemapLayerBase.js#L596](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L596)  
引入版本：3.50.0


---

### preUpdate {#preUpdate}

#### \<instance> preUpdate(time, delta) {#instance-preupdatetime-delta}


**说明:**

此 Tilemap 层的内部更新步骤。 由 Scene 的更新列表自动调用 。 推进层的过期定时器, 用于基于时间的瓦片动画 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 现时时标. |
| delta | number | 否 | 三角洲时间,以毫秒计,自上个框架结束。 |


> 源码：[src/tilemaps/TilemapLayerBase.js#L238](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L238)  
引入版本：4.0.0


---

### putTileAt {#putTileAt}

#### \<instance> putTileAt(tile, tileX, tileY, [recalculateFaces]) {#instance-puttileattile-tilex-tiley-recalculatefaces}


**说明:**

在指定的地层中设置一个砖块坐标。您可以在索引或图块对象中传递。如果在图块中传递,所有属性都将复制到指定位置。如果在索引中通过,则只更改指定位置的索引。碰撞信息将在指定位置重新计算。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tile | number \| [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 |  | 此牌的索引可以设置或设置一个牌面对象。 |
| tileX | number | 否 |  | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 |  | y坐标,以瓦片表示,而不是像素. |
| recalculateFaces | boolean | 是 | true | 如果面额数据应重新计算,则使用`true`。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 插入到给定坐标的平板物体。


> 源码：[src/tilemaps/TilemapLayerBase.js#L614](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L614)  
引入版本：3.50.0


---

### putTileAtWorldXY {#putTileAtWorldXY}

#### \<instance> putTileAtWorldXY(tile, worldX, worldY, [recalculateFaces], [camera]) {#instance-puttileatworldxytile-worldx-worldy-recalculatefaces-camera}


**说明:**

在指定的层中设置一个瓦片,您可以在索引或图文对象中传递。如果在图文中通过,所有属性都将复制到指定位置。如果在索引中通过,则只更改指定位置的索引。碰撞信息将在指定位置重新计算。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tile | number \| [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) | 否 | 此牌的索引可以设置或设置一个牌面对象。 |
| worldX | number | 否 | x坐标,以像素表示. |
| worldY | number | 否 | y坐标,以像素表示. |
| recalculateFaces | boolean | 是 | 如果面额数据应重新计算,则使用`true`。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 插入到给定坐标的平板物体。


> 源码：[src/tilemaps/TilemapLayerBase.js#L635](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L635)  
引入版本：3.50.0


---

### putTilesAt {#putTilesAt}

#### \<instance> putTilesAt(tile, tileX, tileY, [recalculateFaces]) {#instance-puttilesattile-tilex-tiley-recalculatefaces}


**说明:**

在指定的图片坐标上放置一个瓦片数组或一个2D的瓦片数组。该数组可以是瓦片索引或瓦片对象。如果在图片中通过,所有属性都将复制到指定位置。如果在索引中通过,则只更改指定位置的索引。碰撞信息将在区域牌块内重新计算。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tile | Array.\<number> \| Array.\<Array.\<number>> | Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)> | Array.\<Array.\<[Phaser.Tilemaps.Tile](/api/class/tilemaps-tile)>> | 否 |  | 铺设一个列( 阵列) 或格(2D 阵列) 的平面或瓦片索引。 |
| tileX | number | 否 |  | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 |  | y坐标,以瓦片表示,而不是像素. |
| recalculateFaces | boolean | 是 | true | 如果面额数据应重新计算,则使用`true`。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L657](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L657)  
引入版本：3.50.0


---

### randomize {#randomize}

#### \<instance> randomize([tileX], [tileY], [width], [height], [indexes]) {#instance-randomizetilex-tiley-width-height-indexes}


**说明:**

随机化指定层内一个长方形的瓦片区域(在瓦片坐标内)的索引。每个瓦片将获得一个新的索引。如果一个索引数组被传递进来,那么这些索引将被用于随机分配新的瓦片索引。如果不提供数组,则区域内发现的索引(不包括 -1)将被用于随机分配新的瓷片索引。这种方法只修改了瓦片索引,不会改变碰撞信息。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| indexes | Array.\<number> | 是 | 随机化过程中随机抽取的一系列索引. |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L681](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L681)  
引入版本：3.50.0


---

### removedFromScene {#removedFromScene}

#### \<instance> removedFromScene() {#instance-removedfromscene}


**说明:**

此方法在游戏对象从中移除时被Scene自动称为,它从Scene的更新列表中解录了层.


**重写:** Phaser.GameObjects.GameObject#removedFromScene


> 源码：[src/tilemaps/TilemapLayerBase.js#L226](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L226)  
引入版本：4.0.0


---

### removeTileAt {#removeTileAt}

#### \<instance> removeTileAt(tileX, tileY, [replaceWithNull], [recalculateFaces]) {#instance-removetileattilex-tiley-replacewithnull-recalculatefaces}


**说明:**

删除指定层中砖块坐标的瓦片,并更新层碰撞信息。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tileX | number | 否 |  | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 |  | y坐标,以瓦片表示,而不是像素. |
| replaceWithNull | boolean | 是 | true | 如果为真, 这将用无效的砖来取代指定位置的瓦, 而不是以 - 1 的索引为单位的砖。 |
| recalculateFaces | boolean | 是 | true | 如果面额数据应重新计算,则使用`true`。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 从给定位置移走的拼贴对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L706](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L706)  
引入版本：3.50.0


---

### removeTileAtWorldXY {#removeTileAtWorldXY}

#### \<instance> removeTileAtWorldXY(worldX, worldY, [replaceWithNull], [recalculateFaces], [camera]) {#instance-removetileatworldxyworldx-worldy-replacewithnull-recalculatefaces-camera}


**说明:**

删除指定世界坐标的瓦片,更新层碰撞信息。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| worldX | number | 否 |  | x坐标,以像素表示. |
| worldY | number | 否 |  | y坐标,以像素表示. |
| replaceWithNull | boolean | 是 | true | 如果为真, 这将用无效的砖来取代指定位置的瓦, 而不是以 - 1 的索引为单位的砖。 |
| recalculateFaces | boolean | 是 | true | 如果面额数据应重新计算,则使用`true`。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 |  | 从世界值计算瓦片索引时使用的摄像机 。 |


**返回值:** [Phaser.Tilemaps.Tile](/api/class/tilemaps-tile) - 从给定位置移走的拼贴对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L725](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L725)  
引入版本：3.50.0


---

### renderDebug {#renderDebug}

#### \<instance> renderDebug(graphics, [styleConfig]) {#instance-renderdebuggraphics-styleconfig}


**说明:**

绘制图层的调试表示式。 如果您想要快速了解您的哪些牌正在碰撞, 哪些牌有有趣的面孔, 这样做很有帮助。 调试表示式从图形( 0 ) 开始绘制, 允许您将调试表示式放置在屏幕上 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 目标图形对象可以引用 。 |
| styleConfig | [Phaser.Types.Tilemaps.StyleConfig](/api/typedef/types-tilemaps#styleconfig) | 是 | 指定调试绘图所用的颜色的对象。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L745](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L745)  
引入版本：3.50.0


---

### replaceByIndex {#replaceByIndex}

#### \<instance> replaceByIndex(findIndex, newIndex, [tileX], [tileY], [width], [height]) {#instance-replacebyindexfindindex-newindex-tilex-tiley-width-height}


**说明:**

扫描给定的矩形区域(在平面坐标中给出),以匹配`findIndex`的索引来扫描瓦片,并更新其索引以匹配`newIndex`。这只修改索引,不会改变碰撞信息。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| findIndex | number | 否 | 查找的瓦片索引 。 |
| newIndex | number | 否 | 以瓦片代替的索引 。 |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L766](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L766)  
引入版本：3.50.0


---

### setCollision {#setCollision}

#### \<instance> setCollision(indexes, [collides], [recalculateFaces], [updateLayer]) {#instance-setcollisionindexes-collides-recalculatefaces-updatelayer}


**说明:**

将一个图片或牌片的碰撞按指数排列。 您可以通过一个单一的数字索引或一系列索引: [2、 3、 15、 20]。 `collides` 参数控制如果碰撞将被启用( 真实) 或禁用( 假) 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| indexes | number \| array | 否 |  | 或单瓦索引,或单瓦索引的数组。 |
| collides | boolean | 是 | true | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 是 | true | 更新后是否重新计算瓦片面孔 。 |
| updateLayer | boolean | 是 | true | 如果选中的话, 请更新层上的当前牌。 如果没有设置牌, 则设置为不实 。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L790](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L790)  
引入版本：3.50.0


---

### setCollisionBetween {#setCollisionBetween}

#### \<instance> setCollisionBetween(start, stop, [collides], [recalculateFaces]) {#instance-setcollisionbetweenstart-stop-collides-recalculatefaces}


**说明:**

设定一个图片的碰撞范围, 其指数介于指定的 `start`和 `stop`( 包括) 之间。 使用起始值为 10, 止值为 14 的图片, 将设置为 10、 11、 12、 13 和 14 的碰撞范围, 如果启用碰撞( 真实) 或 禁用( 假) , `collides` 参数控制会设置 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| start | number | 否 |  | 设定碰撞的瓦片的第一个索引. |
| stop | number | 否 |  | 设定碰撞的瓦片的最后一个索引 。 |
| collides | boolean | 是 | true | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 是 | true | 更新后是否重新计算瓦片面孔 。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L812](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L812)  
引入版本：3.50.0


---

### setCollisionByExclusion {#setCollisionByExclusion}

#### \<instance> setCollisionByExclusion(indexes, [collides], [recalculateFaces]) {#instance-setcollisionbyexclusionindexes-collides-recalculatefaces}


**说明:**

设定在给定的层中所有瓦片上的碰撞, 除了在给定数组中指定索引的瓦片。 如果启用碰撞( 真实) 或禁用( 假) , `collides` 参数控制。 目前未在层中使用的拖动索引不受影响 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| indexes | Array.\<number> | 否 |  | 一块砖索引的数组,不计算碰撞。 |
| collides | boolean | 是 | true | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 是 | true | 更新后是否重新计算瓦片面孔 。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L860](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L860)  
引入版本：3.50.0


---

### setCollisionByProperty {#setCollisionByProperty}

#### \<instance> setCollisionByProperty(properties, [collides], [recalculateFaces]) {#instance-setcollisionbypropertyproperties-collides-recalculatefaces}


**说明:**

通过检查瓦片属性来设定一层内瓦片的碰撞。 如果瓦片具有与给定的属性对象匹配的属性, 则会设置其碰撞标志。 如果启用碰撞( 真实) 或禁用( 假) , 则 `collides` 参数控制。 在 `{ collides: true }` 中通过, 将会将任何砖片上的碰撞标志更新为具有真实值的“ collides ” 属性。 任何没有设置“ collide” 的瓦片都会被忽略。 您也可以使用一系列值, 如 `{ types: ["stone", "lava", "sand" ] }`。 如果一个瓦片具有与任何这些值匹配的“ 类型” 属性, 其碰撞标志将会被更新 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| properties | object | 否 |  | 具有瓦片属性和相应值的对象,应当检查。 |
| collides | boolean | 是 | true | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 是 | true | 更新后是否重新计算瓦片面孔 。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L835](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L835)  
引入版本：3.50.0


---

### setCollisionFromCollisionGroup {#setCollisionFromCollisionGroup}

#### \<instance> setCollisionFromCollisionGroup([collides], [recalculateFaces]) {#instance-setcollisionfromcollisiongroupcollides-recalculatefaces}


**说明:**

通过检查每块瓦片碰撞组数据(通常在平板碰撞编辑器内在平板内定义),将瓦片碰撞设为一层内。如果在瓦片碰撞组内发现任何物体,则会设置瓦片碰撞信息。如果碰撞启用(真)或禁用(假),则`collides`参数控制。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| collides | boolean | 是 | true | 如果真有它,会让碰撞发生 如果假的,会让碰撞发生 |
| recalculateFaces | boolean | 是 | true | 更新后是否重新计算瓦片面孔 。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L881](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L881)  
引入版本：3.50.0


---

### setTileIndexCallback {#setTileIndexCallback}

#### \<instance> setTileIndexCallback(indexes, callback, callbackContext) {#instance-settileindexcallbackindexes-callback-callbackcontext}


**说明:**

设置层内给定的瓦片索引的全局碰撞调用。 这将影响此层上所有具有相同索引的瓦片。 如果为瓦片索引设置了调用调用调用调取调用调用调用的调用调用调试调用调用调制调用调用调出调用调用调出的调用调用调色调用调用调用了调用调用调减减调用调用调的调用调用调就可以看到 setTileLocationCallback 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| indexes | number \| Array.\<number> | 否 | 或单瓦指数,或一串瓦指数,以设定碰撞回调 。 |
| callback | function | 否 | 当瓦片被碰撞时将引用的回调 。 |
| callbackContext | object | 否 | 调用时的上下文 。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L902](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L902)  
引入版本：3.50.0


---

### setTileLocationCallback {#setTileLocationCallback}

#### \<instance> setTileLocationCallback([tileX], [tileY], [width], [height], [callback], [callbackContext]) {#instance-settilelocationcallbacktilex-tiley-width-height-callback-callbackcontext}


**说明:**

设置层内给定的矩形区域( 平面坐标) 的碰撞调用。 如果已经为平面索引设置了调用调用调用调取, 则将替换。 设置调用调用调用的调用调用调出调用调用调减调取调用调用补间 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |
| callback | function | 是 | 当瓦片被碰撞时将引用的回调 。 |
| callbackContext | object | 是 | 援引回调时的上下文,或范围. |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L924](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L924)  
引入版本：3.50.0


---

### shuffle {#shuffle}

#### \<instance> shuffle([tileX], [tileY], [width], [height]) {#instance-shuffletilex-tiley-width-height}


**说明:**

在指定的层内, 将牌片划入长方形区域( 以瓦片坐标表示) 。 它只会随机排列该区域的牌片, 所以如果它们都一样, 似乎不会改变 ! 这种方法只会修改瓦片索引, 并且不会改变碰撞信息 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L948](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L948)  
引入版本：3.50.0


---

### swapByIndex {#swapByIndex}

#### \<instance> swapByIndex(tileA, tileB, [tileX], [tileY], [width], [height]) {#instance-swapbyindextilea-tileb-tilex-tiley-width-height}


**说明:**

扫描给定的矩形区域(在平面坐标中显示),以匹配`indexA`的索引来扫描瓦片,然后与`indexB`交换。这只修改索引,不会改变碰撞信息。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileA | number | 否 | 首张瓦片索引. |
| tileB | number | 否 | 第二瓦指数. |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L971](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L971)  
引入版本：3.50.0


---

### tileToWorldX {#tileToWorldX}

#### \<instance> tileToWorldX(tileX, [camera]) {#instance-tiletoworldxtilex-camera}


**说明:**

从平面X坐标(平面单位)转换为世界X坐标(像素),在层位,尺度和卷轴中进行计数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |


**返回值:** number - 梯子 X 坐标转换成像素.


> 源码：[src/tilemaps/TilemapLayerBase.js#L995](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L995)  
引入版本：3.50.0


---

### tileToWorldXY {#tileToWorldXY}

#### \<instance> tileToWorldXY(tileX, tileY, [point], [camera]) {#instance-tiletoworldxytilex-tiley-point-camera}


**说明:**

从平面的 XY 坐标( 平面单位) 转换为世界 XY 坐标( 像素), 以层位、 缩放和滚动为因数。 这将返回一个新的矢量2 对象或更新给定的 `point` 对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileX | number | 否 | x坐标,以瓦片表示,而非像素. |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储坐标的矢量2。 如果未给定新的矢量2, 则创建 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 包含提尔河世界坐标的矢量2。


> 源码：[src/tilemaps/TilemapLayerBase.js#L1029](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L1029)  
引入版本：3.50.0


---

### tileToWorldY {#tileToWorldY}

#### \<instance> tileToWorldY(tileY, [camera]) {#instance-tiletoworldytiley-camera}


**说明:**

从瓦片 Y 坐标( 平面单位) 转换为世界 Y 坐标( 像素), 以层位、 缩放和滚动为因数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tileY | number | 否 | y坐标,以瓦片表示,而不是像素. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |


**返回值:** number - 梯Y坐标转换成像素.


> 源码：[src/tilemaps/TilemapLayerBase.js#L1012](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L1012)  
引入版本：3.50.0


---

### weightedRandomize {#weightedRandomize}

#### \<instance> weightedRandomize(weightedIndexes, [tileX], [tileY], [width], [height]) {#instance-weightedrandomizeweightedindexes-tilex-tiley-width-height}


**说明:**

随机化指定层内一个矩形的瓦片区域(在瓦片坐标内)的索引。每个瓦片将获得一个新的索引。新的索引是从给定的 weightedIndexes 阵列中抽取的。一个加权数组的例子:

[{指数:6,重量:4},//指数6的概率为4/8{指数:7,重量:2},/指数7的概率为2/8{指数:8,重量:1.5},/指数8的概率为1.5/8{指数:26,重量:0.5}/指数26的概率为0.5/8]].

选择任何索引的概率是(索引的权重) /(所有权重的和) 。 这种方法只修改了瓦片索引, 并且不会改变碰撞信息 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| weightedIndexes | Array.\<object> | 否 | 随机化过程中随机抽取的一组对象。 其形式应该是 : { 指数: 0, 重量: 4} 或{ 指数: [0], 重量: 4( 如果您想从多块的索引中抽取 ) 。 |
| tileX | number | 是 | 左最瓦指数(在瓦座坐标中)作为该地区的起源. |
| tileY | number | 是 | 以砖块坐标为最顶部的瓦片索引作为区域来源. |
| width | number | 是 | 有多少块瓦片宽度从 `tileX` 索引区域将。 |
| height | number | 是 | 有多少块高的瓦片从 `tileY` 索引区域将。 |


**返回值:** [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase) - 此 Tilemap 层对象 。


> 源码：[src/tilemaps/TilemapLayerBase.js#L1075](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L1075)  
引入版本：3.50.0


---

### worldToTileX {#worldToTileX}

#### \<instance> worldToTileX(worldX, [snapToFloor], [camera]) {#instance-worldtotilexworldx-snaptofloor-camera}


**说明:**

从世界 X 坐标(像素)转换为瓦片 X坐标(瓦单位),在层位,尺度和卷轴中进行计分.

使用这种方法不能叫做Isometric或六边形瓦片,因为它们要求`worldX`和`worldY`值都能够确定正确的瓦片,相反,你应该使用`worldToTileXY`方法。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | 要转换的x坐标,以像素表示,而不是用瓦片表示. |
| snapToFloor | boolean | 是 | 是否将平板坐标向下折叠到最近的整数 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |


**返回值:** number - 瓦片X坐标基于世界值.


> 源码：[src/tilemaps/TilemapLayerBase.js#L1108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L1108)  
引入版本：3.50.0


---

### worldToTileXY {#worldToTileXY}

#### \<instance> worldToTileXY(worldX, worldY, [snapToFloor], [point], [camera]) {#instance-worldtotilexyworldx-worldy-snaptofloor-point-camera}


**说明:**

从世界 XY 坐标( 像素) 转换为平面 XY 坐标( 平面单位), 以图层位置、 缩放和滚动为因数。 这将返回一个新的矢量2 对象或更新给定的 `point` 对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldX | number | 否 | 要转换的x坐标,以像素表示,而不是用瓦片表示. |
| worldY | number | 否 | 转换的y坐标,以像素表示,而不是瓦片. |
| snapToFloor | boolean | 是 | 是否将平板坐标向下折叠到最近的整数 。 |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储坐标的矢量2。 如果未给定新的矢量2, 则创建 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 含有世界值的瓦片坐标的矢量2。


> 源码：[src/tilemaps/TilemapLayerBase.js#L1152](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L1152)  
引入版本：3.50.0


---

### worldToTileY {#worldToTileY}

#### \<instance> worldToTileY(worldY, [snapToFloor], [camera]) {#instance-worldtotileyworldy-snaptofloor-camera}


**说明:**

从世界Y坐标(像素)转换为瓦片Y坐标(瓦片单位),在层位,尺度和卷轴中进行计分.

使用这种方法不能叫做Isometric或六边形瓦片,因为它们要求`worldX`和`worldY`值都能够确定正确的瓦片,相反,你应该使用`worldToTileXY`方法。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| worldY | number | 否 | 转换的y坐标,以像素表示,而不是瓦片. |
| snapToFloor | boolean | 是 | 是否将平板坐标向下折叠到最近的整数 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 从世界值计算瓦片索引时使用的摄像机 。 |


**返回值:** number - 瓦片Y坐标基于世界值.


> 源码：[src/tilemaps/TilemapLayerBase.js#L1130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapLayerBase.js#L1130)  
引入版本：3.50.0


---

---
