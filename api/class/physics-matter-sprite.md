# Sprite {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-matter-sprite)

Matter 物理Sprite游戏对象.

这是一个已启用的Sprite, 与 Matter.js 物理引擎一起使用。 它将标准 Phaser Sprite 的全部渲染和动画能力与 Matter. js 物理机体相结合, 使其能够参与复杂的物理模拟, 包括多边形碰撞、 关节、 弹簧和制约 。

与使用简单的轴线相接的边框或圆圈的Arcade Physics不同,Matter.js支持任意的凸轮和凸轮多边形形状、复合体和现实的刚性体动力学。当您需要物理的这个水平的忠实度时,使用这个类来进行动画游戏对象。

构造时, 默认会创建一个与 sprite 框架尺寸相匹配的矩形体。 您可以通过提供 。 `shape` 属性在 `options` 配置对象,或调用其中之一 `setBody`, `setRectangle`, `setCircle`, `setPolygon`,或 ,或 , `setTrapezoid` 创建后的方法。

斯普林特游戏对象用于在游戏中显示静态和动画图像。斯普林特可以有输入事件和物理体,也可以被调色,有色,有卷轴和动画.

斯普丽特和图像游戏对象的主要区别在于无法动画图像。因此,斯普丽特需要花费更长的时间来处理,并且由于动画组件而具有更大的API脚印。如果不需要动画,那么可以安全地使用图像来替换所有情况下的斯普丽特.

**构造函数**

`new Sprite(world, x, y, texture, [frame], [options])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| world | [Phaser.Physics.Matter.World](/api/class/physics-matter-world) | 否 | 提到这个实体,这个机构所属的世界实例。 |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此游戏对象将使用用于渲染的纹理的键或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite)  
> [Phaser.Physics.Matter.Components.Bounce](/api/namespace/physics-matter-components-bounce)  
> [Phaser.Physics.Matter.Components.Collision](/api/namespace/physics-matter-components-collision)  
> [Phaser.Physics.Matter.Components.Force](/api/namespace/physics-matter-components-force)  
> [Phaser.Physics.Matter.Components.Friction](/api/namespace/physics-matter-components-friction)  
> [Phaser.Physics.Matter.Components.Gravity](/api/namespace/physics-matter-components-gravity)  
> [Phaser.Physics.Matter.Components.Mass](/api/namespace/physics-matter-components-mass)  
> [Phaser.Physics.Matter.Components.Sensor](/api/namespace/physics-matter-components-sensor)  
> [Phaser.Physics.Matter.Components.SetBody](/api/namespace/physics-matter-components-setbody)  
> [Phaser.Physics.Matter.Components.Sleep](/api/namespace/physics-matter-components-sleep)  
> [Phaser.Physics.Matter.Components.Static](/api/namespace/physics-matter-components-static)  
> [Phaser.Physics.Matter.Components.Transform](/api/namespace/physics-matter-components-transform)  
> [Phaser.Physics.Matter.Components.Velocity](/api/namespace/physics-matter-components-velocity)  
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



> 源码：[src/physics/matter-js/MatterSprite.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterSprite.js#L15)  
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





**From [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite):**


 - [anims](/api/class/gameobjects-sprite#anims)





**From [Phaser.Physics.Matter.Components.Mass](/api/namespace/physics-matter-components-mass):**


 - [centerOfMass](/api/namespace/physics-matter-components-mass#centerOfMass)




---

## 公开成员 {#public-members}

### world {#world}

#### world: [Phaser.Physics.Matter.World](/api/class/physics-matter-world) {#world-phaserphysicsmatterworld}


**说明:**

提到这个实体,这个机构所属的世界实例。


> 源码：[src/physics/matter-js/MatterSprite.js#L122](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterSprite.js#L122)  
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


 - [addToDisplayList](/api/class/gameobjects-gameobject#addToDisplayList)
 - [addToUpdateList](/api/class/gameobjects-gameobject#addToUpdateList)
 - [destroy](/api/class/gameobjects-gameobject#destroy)
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
 - [update](/api/class/gameobjects-gameobject#update)
 - [willRender](/api/class/gameobjects-gameobject#willRender)
 - [willRoundVertices](/api/class/gameobjects-gameobject#willRoundVertices)





**From [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite):**


 - [addedToScene](/api/class/gameobjects-sprite#addedToScene)
 - [chain](/api/class/gameobjects-sprite#chain)
 - [play](/api/class/gameobjects-sprite#play)
 - [playAfterDelay](/api/class/gameobjects-sprite#playAfterDelay)
 - [playAfterRepeat](/api/class/gameobjects-sprite#playAfterRepeat)
 - [playReverse](/api/class/gameobjects-sprite#playReverse)
 - [preUpdate](/api/class/gameobjects-sprite#preUpdate)
 - [removedFromScene](/api/class/gameobjects-sprite#removedFromScene)
 - [stop](/api/class/gameobjects-sprite#stop)
 - [stopAfterDelay](/api/class/gameobjects-sprite#stopAfterDelay)
 - [stopAfterRepeat](/api/class/gameobjects-sprite#stopAfterRepeat)
 - [stopOnFrame](/api/class/gameobjects-sprite#stopOnFrame)
 - [toJSON](/api/class/gameobjects-sprite#toJSON)





**From [Phaser.Physics.Matter.Components.Bounce](/api/namespace/physics-matter-components-bounce):**


 - [setBounce](/api/namespace/physics-matter-components-bounce#setBounce)





**From [Phaser.Physics.Matter.Components.Collision](/api/namespace/physics-matter-components-collision):**


 - [setCollidesWith](/api/namespace/physics-matter-components-collision#setCollidesWith)
 - [setCollisionCategory](/api/namespace/physics-matter-components-collision#setCollisionCategory)
 - [setCollisionGroup](/api/namespace/physics-matter-components-collision#setCollisionGroup)
 - [setOnCollide](/api/namespace/physics-matter-components-collision#setOnCollide)
 - [setOnCollideActive](/api/namespace/physics-matter-components-collision#setOnCollideActive)
 - [setOnCollideEnd](/api/namespace/physics-matter-components-collision#setOnCollideEnd)
 - [setOnCollideWith](/api/namespace/physics-matter-components-collision#setOnCollideWith)





**From [Phaser.Physics.Matter.Components.Force](/api/namespace/physics-matter-components-force):**


 - [applyForce](/api/namespace/physics-matter-components-force#applyForce)
 - [applyForceFrom](/api/namespace/physics-matter-components-force#applyForceFrom)
 - [thrust](/api/namespace/physics-matter-components-force#thrust)
 - [thrustBack](/api/namespace/physics-matter-components-force#thrustBack)
 - [thrustLeft](/api/namespace/physics-matter-components-force#thrustLeft)
 - [thrustRight](/api/namespace/physics-matter-components-force#thrustRight)





**From [Phaser.Physics.Matter.Components.Friction](/api/namespace/physics-matter-components-friction):**


 - [setFriction](/api/namespace/physics-matter-components-friction#setFriction)
 - [setFrictionAir](/api/namespace/physics-matter-components-friction#setFrictionAir)
 - [setFrictionStatic](/api/namespace/physics-matter-components-friction#setFrictionStatic)





**From [Phaser.Physics.Matter.Components.Gravity](/api/namespace/physics-matter-components-gravity):**


 - [setIgnoreGravity](/api/namespace/physics-matter-components-gravity#setIgnoreGravity)





**From [Phaser.Physics.Matter.Components.Mass](/api/namespace/physics-matter-components-mass):**


 - [setDensity](/api/namespace/physics-matter-components-mass#setDensity)
 - [setMass](/api/namespace/physics-matter-components-mass#setMass)





**From [Phaser.Physics.Matter.Components.Sensor](/api/namespace/physics-matter-components-sensor):**


 - [isSensor](/api/namespace/physics-matter-components-sensor#isSensor)
 - [setSensor](/api/namespace/physics-matter-components-sensor#setSensor)





**From [Phaser.Physics.Matter.Components.SetBody](/api/namespace/physics-matter-components-setbody):**


 - [setBody](/api/namespace/physics-matter-components-setbody#setBody)
 - [setCircle](/api/namespace/physics-matter-components-setbody#setCircle)
 - [setExistingBody](/api/namespace/physics-matter-components-setbody#setExistingBody)
 - [setPolygon](/api/namespace/physics-matter-components-setbody#setPolygon)
 - [setRectangle](/api/namespace/physics-matter-components-setbody#setRectangle)
 - [setTrapezoid](/api/namespace/physics-matter-components-setbody#setTrapezoid)





**From [Phaser.Physics.Matter.Components.Sleep](/api/namespace/physics-matter-components-sleep):**


 - [setAwake](/api/namespace/physics-matter-components-sleep#setAwake)
 - [setSleepEndEvent](/api/namespace/physics-matter-components-sleep#setSleepEndEvent)
 - [setSleepEvents](/api/namespace/physics-matter-components-sleep#setSleepEvents)
 - [setSleepStartEvent](/api/namespace/physics-matter-components-sleep#setSleepStartEvent)
 - [setSleepThreshold](/api/namespace/physics-matter-components-sleep#setSleepThreshold)
 - [setToSleep](/api/namespace/physics-matter-components-sleep#setToSleep)





**From [Phaser.Physics.Matter.Components.Static](/api/namespace/physics-matter-components-static):**


 - [isStatic](/api/namespace/physics-matter-components-static#isStatic)
 - [setStatic](/api/namespace/physics-matter-components-static#setStatic)





**From [Phaser.Physics.Matter.Components.Transform](/api/namespace/physics-matter-components-transform):**


 - [setFixedRotation](/api/namespace/physics-matter-components-transform#setFixedRotation)





**From [Phaser.Physics.Matter.Components.Velocity](/api/namespace/physics-matter-components-velocity):**


 - [getAngularSpeed](/api/namespace/physics-matter-components-velocity#getAngularSpeed)
 - [getAngularVelocity](/api/namespace/physics-matter-components-velocity#getAngularVelocity)
 - [getVelocity](/api/namespace/physics-matter-components-velocity#getVelocity)
 - [setAngularSpeed](/api/namespace/physics-matter-components-velocity#setAngularSpeed)
 - [setAngularVelocity](/api/namespace/physics-matter-components-velocity#setAngularVelocity)
 - [setVelocity](/api/namespace/physics-matter-components-velocity#setVelocity)
 - [setVelocityX](/api/namespace/physics-matter-components-velocity#setVelocityX)
 - [setVelocityY](/api/namespace/physics-matter-components-velocity#setVelocityY)




---

---
