# TilemapGPULayer {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tilemaps-tilemapgpulayer)

TILEMAPGPULAYER是一种特殊类型的游戏对象,它使LayerData从TILEMAPLAYER中产生。与更加灵活的TILEMAPLALYER不同,这个对象使用单一的TILEMPLAYER,并且比灵活性更优化速度和质量。它用于高性能渲染不更新内容的tilemaps。它仍然支持瓷砖动画和翻转。

此层的设计仅与WebGL渲染器使用.

此图层的性能是极好的。 如果您不需要操纵图层中的瓷砖, 而该图层是支持的类型, 这是渲染图层的最佳选项。 它几乎完全由 GPU 绑定, 因此它会释放CPU 资源用于其它游戏代码( CPU 在游戏中通常比 GPU 做得多的工作 ) 。 它在屏幕上每个像素都有固定的成本, 无论该瓷砖中有什么, 一般来说, 当许多图片可见时, 它不会受到性能损失 。

通过在 `Tilemap.createLayer()` 的呼叫中添加 `gpu` 旗, 创建 TilemapGPULayer 。 这将返回 TilemapGPULayer 实例 。

这个层具有以下能力和限制: 电源:

- 使用单色的瓦片,并带有单纹理图像.

- 最大瓦片大小为4096x4096瓦.

- 最大2^23(8388608) 独特的瓦片标识.

- 可能翻动了砖头。

- 平面可能是动画片.

- 动画数据限制为8388608条目(动画或动画的每个帧都使用一个条目).

- 仅限整形砖.

层通过特殊的遮蔽器来制成。 它使用包含层砖数据的纹理, 以及包含任何瓦片动画的第二个纹理。 遮蔽器将瓦片变成一个单一的四重奏。 因为不需要在 CPU 上计算单个的瓷砖, 这比 TilemapLayer 更快。 但是, 由于它把瓦片当作单一的正交格, 它不适合使用异构或六角瓦片, 或者需要不同渲染方法的其他类型的瓦片 。

如果平板图像使用 NEAREST 密丝, 遮蔽器会使尖端像素变形。 否则它会假设 LINEAR 过滤。 遮蔽器会自动使 LINEAR 模式中的平板间边界变得平滑, 没有缝隙或流血, 以取得完美的结果。 普通的 TilemapLayer 无法使平板边界变成这样, 在瓷砖之间产生尖锐的缝隙 。

层可以编辑,但不会自动更新. 重生成层砖数据纹理,使用`generateLayerDataTexture`调用.

**构造函数**

`new TilemapGPULayer(scene, tilemap, layerIndex, tileset, [x], [y])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 这台提列玛普GPULayer所属的场景. |
| tilemap | [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) | 否 | 蒂拉玛普这个层是其中的一部分. |
| layerIndex | number | 否 | 与此层相关的图层数据索引 。 |
| tileset | string \| [Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset) | 否 | 用于在此层中制成瓷砖的瓦片。 可以是字符串或蒂莱塞特对象 。 |
| x | number | 是 | 将这个层的左上方放置的世界x位置. |
| y | number | 是 | 将这个层的左上方放置在 y 位置的世界 。 |

---


**作用域**: static


**继承**

> [Phaser.Tilemaps.TilemapLayerBase](/api/class/tilemaps-tilemaplayerbase)  



> 源码：[src/tilemaps/TilemapGPULayer.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapGPULayer.js#L12)  
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

### layerDataTexture {#layerDataTexture}

#### layerDataTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#layerdatatexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

包含此游戏对象的瓦片数据的纹理。 每个 Texel 描述层中的单片 。

每个texel被存储为32位值,因此编码为:

- 1位:水平翻转旗.

- 1位:垂直翻转旗.

- 1位:动画旗.

- 1位:未使用.

- 28位:瓷砖指数.


> 源码：[src/tilemaps/TilemapGPULayer.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapGPULayer.js#L99)  
引入版本：4.0.0


---

### tileset {#tileset}

#### tileset: [Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset) {#tileset-phasertilemapstileset}


**说明:**

与这层相关的`Tileset`.

与`TilemapLayer`不同,这个物体只能有一个瓦片集,因为渲染器被优化为单一的纹理.


> 源码：[src/tilemaps/TilemapGPULayer.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapGPULayer.js#L87)  
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
 - [destroy](/api/class/tilemaps-tilemaplayerbase#destroy)
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

### generateLayerDataTexture {#generateLayerDataTexture}

#### \<instance> generateLayerDataTexture() {#instance-generatelayerdatatexture}


**说明:**

生成此游戏对象的层数据纹理。

层数据纹理是 WebGL 纹理,每个texel 编码了层中单瓦的瓦片索引,翻转旗和动画旗。它被 GPU 遮蔽器消耗,将整个瓦片变成一个单一的四边形。

此方法由 `setTileset` 自动调用。 您应该在图层中编辑瓷砖数据后手动调用, 因为 GPU 纹理不会在瓷砖变化时自动更新 。


> 源码：[src/tilemaps/TilemapGPULayer.js#L161](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapGPULayer.js#L161)  
引入版本：4.0.0


---

---
