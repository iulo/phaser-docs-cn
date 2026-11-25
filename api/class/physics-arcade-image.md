# Image {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-arcade-image)

弧形物理影像(An Arcade Physics Image)是一个标准图像游戏对象,其天体和相关物理组件混合在其中,它是Arcade物理中可用的最轻量级的物理辅助游戏对象,使其对于静态景物,收集器,平台,子弹,或任何需要参与物理碰撞和重叠检查的非动态物体来说,都非常理想.

物理体可以是动态的(受速度,加速度和重力的影响),也可以是静态的(不可移动,用于平台和边界). 物理行为通过混合的弧形物理组件,如极速,加速,弹跳,重力等来控制.

弧形图像和弧形闪光片之间的关键区别在于,弧形图像不能播放基于纹理的动画。如果需要帧动画,请使用`Phaser.Physics.Arcade.Sprite`。如果只需要一个静态或程序化的物体,而不需要动画,则弧形图像是效率更高的选择。

通常你不应该直接创建ArcadeImage。 相反,使用厂家方法`this.physics.add.image()`从场景内部创建图像,并将其身体自动添加到Arcade物理世界中。

**构造函数**

`new Image(scene, x, y, texture, [frame])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此游戏对象将使用用于渲染的纹理的密钥或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Image](/api/class/gameobjects-image)  
> [Phaser.Physics.Arcade.Components.Acceleration](/api/namespace/physics-arcade-components-acceleration)  
> [Phaser.Physics.Arcade.Components.Angular](/api/namespace/physics-arcade-components-angular)  
> [Phaser.Physics.Arcade.Components.Bounce](/api/namespace/physics-arcade-components-bounce)  
> [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision)  
> [Phaser.Physics.Arcade.Components.Debug](/api/namespace/physics-arcade-components-debug)  
> [Phaser.Physics.Arcade.Components.Drag](/api/namespace/physics-arcade-components-drag)  
> [Phaser.Physics.Arcade.Components.Enable](/api/namespace/physics-arcade-components-enable)  
> [Phaser.Physics.Arcade.Components.Friction](/api/namespace/physics-arcade-components-friction)  
> [Phaser.Physics.Arcade.Components.Gravity](/api/namespace/physics-arcade-components-gravity)  
> [Phaser.Physics.Arcade.Components.Immovable](/api/namespace/physics-arcade-components-immovable)  
> [Phaser.Physics.Arcade.Components.Mass](/api/namespace/physics-arcade-components-mass)  
> [Phaser.Physics.Arcade.Components.Pushable](/api/namespace/physics-arcade-components-pushable)  
> [Phaser.Physics.Arcade.Components.Size](/api/namespace/physics-arcade-components-size)  
> [Phaser.Physics.Arcade.Components.Velocity](/api/namespace/physics-arcade-components-velocity)  
> [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip)  
> [Phaser.GameObjects.Components.GetBounds](/api/namespace/gameobjects-components-getbounds)  
> [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask)  
> [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  
> [Phaser.GameObjects.Components.Size](/api/namespace/gameobjects-components-size)  
> [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture)  
> [Phaser.GameObjects.Components.Tint](/api/namespace/gameobjects-components-tint)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/physics/arcade/ArcadeImage.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadeImage.js#L11)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha):**


 - [alpha](/api/namespace/gameobjects-components-alpha#alpha)
 - [alphaBottomLeft](/api/namespace/gameobjects-components-alpha#alphaBottomLeft)
 - [alphaBottomRight](/api/namespace/gameobjects-components-alpha#alphaBottomRight)
 - [alphaTopLeft](/api/namespace/gameobjects-components-alpha#alphaTopLeft)
 - [alphaTopRight](/api/namespace/gameobjects-components-alpha#alphaTopRight)





**From [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode):**


 - [blendMode](/api/namespace/gameobjects-components-blendmode#blendMode)





**From [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth):**


 - [depth](/api/namespace/gameobjects-components-depth#depth)





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





**From [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin):**


 - [displayOriginX](/api/namespace/gameobjects-components-origin#displayOriginX)
 - [displayOriginY](/api/namespace/gameobjects-components-origin#displayOriginY)
 - [originX](/api/namespace/gameobjects-components-origin#originX)
 - [originY](/api/namespace/gameobjects-components-origin#originY)





**From [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes):**


 - [customRenderNodes](/api/namespace/gameobjects-components-rendernodes#customRenderNodes)
 - [defaultRenderNodes](/api/namespace/gameobjects-components-rendernodes#defaultRenderNodes)
 - [renderNodeData](/api/namespace/gameobjects-components-rendernodes#renderNodeData)





**From [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor):**


 - [scrollFactorX](/api/namespace/gameobjects-components-scrollfactor#scrollFactorX)
 - [scrollFactorY](/api/namespace/gameobjects-components-scrollfactor#scrollFactorY)





**From [Phaser.GameObjects.Components.Size](/api/namespace/gameobjects-components-size):**


 - [displayHeight](/api/namespace/gameobjects-components-size#displayHeight)
 - [displayWidth](/api/namespace/gameobjects-components-size#displayWidth)
 - [height](/api/namespace/gameobjects-components-size#height)
 - [width](/api/namespace/gameobjects-components-size#width)





**From [Phaser.GameObjects.Components.TextureCrop](/api/namespace/gameobjects-components-texturecrop):**


 - [frame](/api/namespace/gameobjects-components-texturecrop#frame)
 - [isCropped](/api/namespace/gameobjects-components-texturecrop#isCropped)
 - [texture](/api/namespace/gameobjects-components-texturecrop#texture)





**From [Phaser.GameObjects.Components.Tint](/api/namespace/gameobjects-components-tint):**


 - [isTinted](/api/namespace/gameobjects-components-tint#isTinted)
 - [tint](/api/namespace/gameobjects-components-tint#tint)
 - [tintBottomLeft](/api/namespace/gameobjects-components-tint#tintBottomLeft)
 - [tintBottomRight](/api/namespace/gameobjects-components-tint#tintBottomRight)
 - [tintMode](/api/namespace/gameobjects-components-tint#tintMode)
 - [tintTopLeft](/api/namespace/gameobjects-components-tint#tintTopLeft)
 - [tintTopRight](/api/namespace/gameobjects-components-tint#tintTopRight)





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





**From [Phaser.Physics.Arcade.Components.Debug](/api/namespace/physics-arcade-components-debug):**


 - [debugBodyColor](/api/namespace/physics-arcade-components-debug#debugBodyColor)
 - [debugShowBody](/api/namespace/physics-arcade-components-debug#debugShowBody)
 - [debugShowVelocity](/api/namespace/physics-arcade-components-debug#debugShowVelocity)




---

## 公开成员 {#public-members}

### body {#body}

#### body: [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body), [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) {#body-phaserphysicsarcadebody-phaserphysicsarcadestaticbody}


**说明:**

此游戏对象的物理体 。


**Overrides:** Phaser.GameObjects.Image身体的伤痛


> 源码：[src/physics/arcade/ArcadeImage.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/ArcadeImage.js#L98)  
引入版本：3.0.0


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





**From [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth):**


 - [setAbove](/api/namespace/gameobjects-components-depth#setAbove)
 - [setBelow](/api/namespace/gameobjects-components-depth#setBelow)
 - [setDepth](/api/namespace/gameobjects-components-depth#setDepth)
 - [setToBack](/api/namespace/gameobjects-components-depth#setToBack)
 - [setToTop](/api/namespace/gameobjects-components-depth#setToTop)





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





**From [Phaser.GameObjects.Components.Size](/api/namespace/gameobjects-components-size):**


 - [setDisplaySize](/api/namespace/gameobjects-components-size#setDisplaySize)
 - [setSize](/api/namespace/gameobjects-components-size#setSize)
 - [setSizeToFrame](/api/namespace/gameobjects-components-size#setSizeToFrame)





**From [Phaser.GameObjects.Components.TextureCrop](/api/namespace/gameobjects-components-texturecrop):**


 - [setCrop](/api/namespace/gameobjects-components-texturecrop#setCrop)
 - [setFrame](/api/namespace/gameobjects-components-texturecrop#setFrame)
 - [setTexture](/api/namespace/gameobjects-components-texturecrop#setTexture)





**From [Phaser.GameObjects.Components.Tint](/api/namespace/gameobjects-components-tint):**


 - [clearTint](/api/namespace/gameobjects-components-tint#clearTint)
 - [setTint](/api/namespace/gameobjects-components-tint#setTint)
 - [setTintFill](/api/namespace/gameobjects-components-tint#setTintFill)
 - [setTintMode](/api/namespace/gameobjects-components-tint#setTintMode)





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


 - [addedToScene](/api/class/gameobjects-gameobject#addedToScene)
 - [addToDisplayList](/api/class/gameobjects-gameobject#addToDisplayList)
 - [addToUpdateList](/api/class/gameobjects-gameobject#addToUpdateList)
 - [destroy](/api/class/gameobjects-gameobject#destroy)
 - [disableInteractive](/api/class/gameobjects-gameobject#disableInteractive)
 - [getData](/api/class/gameobjects-gameobject#getData)
 - [getDisplayList](/api/class/gameobjects-gameobject#getDisplayList)
 - [getIndexList](/api/class/gameobjects-gameobject#getIndexList)
 - [incData](/api/class/gameobjects-gameobject#incData)
 - [removedFromScene](/api/class/gameobjects-gameobject#removedFromScene)
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





**From [Phaser.Physics.Arcade.Components.Acceleration](/api/namespace/physics-arcade-components-acceleration):**


 - [setAcceleration](/api/namespace/physics-arcade-components-acceleration#setAcceleration)
 - [setAccelerationX](/api/namespace/physics-arcade-components-acceleration#setAccelerationX)
 - [setAccelerationY](/api/namespace/physics-arcade-components-acceleration#setAccelerationY)





**From [Phaser.Physics.Arcade.Components.Angular](/api/namespace/physics-arcade-components-angular):**


 - [setAngularAcceleration](/api/namespace/physics-arcade-components-angular#setAngularAcceleration)
 - [setAngularDrag](/api/namespace/physics-arcade-components-angular#setAngularDrag)
 - [setAngularVelocity](/api/namespace/physics-arcade-components-angular#setAngularVelocity)





**From [Phaser.Physics.Arcade.Components.Bounce](/api/namespace/physics-arcade-components-bounce):**


 - [setBounce](/api/namespace/physics-arcade-components-bounce#setBounce)
 - [setBounceX](/api/namespace/physics-arcade-components-bounce#setBounceX)
 - [setBounceY](/api/namespace/physics-arcade-components-bounce#setBounceY)
 - [setCollideWorldBounds](/api/namespace/physics-arcade-components-bounce#setCollideWorldBounds)





**From [Phaser.Physics.Arcade.Components.Collision](/api/namespace/physics-arcade-components-collision):**


 - [addCollidesWith](/api/namespace/physics-arcade-components-collision#addCollidesWith)
 - [removeCollidesWith](/api/namespace/physics-arcade-components-collision#removeCollidesWith)
 - [resetCollisionCategory](/api/namespace/physics-arcade-components-collision#resetCollisionCategory)
 - [setCollidesWith](/api/namespace/physics-arcade-components-collision#setCollidesWith)
 - [setCollisionCategory](/api/namespace/physics-arcade-components-collision#setCollisionCategory)
 - [willCollideWith](/api/namespace/physics-arcade-components-collision#willCollideWith)





**From [Phaser.Physics.Arcade.Components.Debug](/api/namespace/physics-arcade-components-debug):**


 - [setDebug](/api/namespace/physics-arcade-components-debug#setDebug)
 - [setDebugBodyColor](/api/namespace/physics-arcade-components-debug#setDebugBodyColor)





**From [Phaser.Physics.Arcade.Components.Drag](/api/namespace/physics-arcade-components-drag):**


 - [setDamping](/api/namespace/physics-arcade-components-drag#setDamping)
 - [setDrag](/api/namespace/physics-arcade-components-drag#setDrag)
 - [setDragX](/api/namespace/physics-arcade-components-drag#setDragX)
 - [setDragY](/api/namespace/physics-arcade-components-drag#setDragY)





**From [Phaser.Physics.Arcade.Components.Enable](/api/namespace/physics-arcade-components-enable):**


 - [disableBody](/api/namespace/physics-arcade-components-enable#disableBody)
 - [enableBody](/api/namespace/physics-arcade-components-enable#enableBody)
 - [refreshBody](/api/namespace/physics-arcade-components-enable#refreshBody)
 - [setDirectControl](/api/namespace/physics-arcade-components-enable#setDirectControl)





**From [Phaser.Physics.Arcade.Components.Friction](/api/namespace/physics-arcade-components-friction):**


 - [setFriction](/api/namespace/physics-arcade-components-friction#setFriction)
 - [setFrictionX](/api/namespace/physics-arcade-components-friction#setFrictionX)
 - [setFrictionY](/api/namespace/physics-arcade-components-friction#setFrictionY)





**From [Phaser.Physics.Arcade.Components.Gravity](/api/namespace/physics-arcade-components-gravity):**


 - [setGravity](/api/namespace/physics-arcade-components-gravity#setGravity)
 - [setGravityX](/api/namespace/physics-arcade-components-gravity#setGravityX)
 - [setGravityY](/api/namespace/physics-arcade-components-gravity#setGravityY)





**From [Phaser.Physics.Arcade.Components.Immovable](/api/namespace/physics-arcade-components-immovable):**


 - [setImmovable](/api/namespace/physics-arcade-components-immovable#setImmovable)





**From [Phaser.Physics.Arcade.Components.Mass](/api/namespace/physics-arcade-components-mass):**


 - [setMass](/api/namespace/physics-arcade-components-mass#setMass)





**From [Phaser.Physics.Arcade.Components.Pushable](/api/namespace/physics-arcade-components-pushable):**


 - [setPushable](/api/namespace/physics-arcade-components-pushable#setPushable)





**From [Phaser.Physics.Arcade.Components.Size](/api/namespace/physics-arcade-components-size):**


 - [setBodySize](/api/namespace/physics-arcade-components-size#setBodySize)
 - [setCircle](/api/namespace/physics-arcade-components-size#setCircle)
 - [setOffset](/api/namespace/physics-arcade-components-size#setOffset)





**From [Phaser.Physics.Arcade.Components.Velocity](/api/namespace/physics-arcade-components-velocity):**


 - [setMaxVelocity](/api/namespace/physics-arcade-components-velocity#setMaxVelocity)
 - [setVelocity](/api/namespace/physics-arcade-components-velocity#setVelocity)
 - [setVelocityX](/api/namespace/physics-arcade-components-velocity#setVelocityX)
 - [setVelocityY](/api/namespace/physics-arcade-components-velocity#setVelocityY)




---

---
