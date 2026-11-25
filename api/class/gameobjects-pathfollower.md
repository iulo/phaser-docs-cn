# PathFollower {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-pathfollower)

路径跟踪器(PathCapcraper)是一种Sprite,它会自动沿着[Phaser.Curves.Path](/api/class/curves-path)移动,使它成为切换,敌方巡逻路线,移动平台,射电弧,或者任何应该穿越世界预先定义的航线的游戏对象的理想.

它延伸了斯普丽特,因此标准斯普丽特上的一切可用——动画,锡金,缩放,α,混合模式等等——都在这里同样工作.

路径跟踪器在任何时间都绑定到单一路径,并且可以从开始到完成该路径的全部长度,从任意方向,或者从它沿途的任何特定点到终点。回放速度和持续时间通过一个类似Tween的配置对象通过传递到`startFollow`来控制。后续者可以选择旋转,以面对旅行方向,从路径坐标中抵消,或者独立于路径旋转。

**构造函数**

`new PathFollower(scene, path, x, y, texture, [frame])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此路径跟踪器所属景区 。 |
| path | [Phaser.Curves.Path](/api/class/curves-path) | 否 | 此路径跟踪器遵循的路径。 它只能一次遵循一个路径 。 |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此游戏对象将使用用于渲染的纹理的密钥或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite)  
> [Phaser.GameObjects.Components.PathFollower](/api/namespace/gameobjects-components-pathfollower)  



> 源码：[src/gameobjects/pathfollower/PathFollower.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/pathfollower/PathFollower.js#L11)  
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





**From [Phaser.GameObjects.Components.PathFollower](/api/namespace/gameobjects-components-pathfollower):**


 - [path](/api/namespace/gameobjects-components-pathfollower#path)
 - [pathRotationOffset](/api/namespace/gameobjects-components-pathfollower#pathRotationOffset)
 - [rotateToPath](/api/namespace/gameobjects-components-pathfollower#rotateToPath)





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




---

## 公开成员 {#public-members}

### pathConfig {#pathConfig}

#### pathConfig: [Phaser.Types.GameObjects.PathFollower.PathConfig](/api/typedef/types-gameobjects-pathfollower#pathconfig) {#pathconfig-phasertypesgameobjectspathfollowerpathconfig}


**说明:**

路径跟踪器的设置 。


> 源码：[src/gameobjects/components/PathFollower.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L93)  
引入版本：3.0.0


---

### pathDelta {#pathDelta}

#### pathDelta: [Phaser.Math.Vector2](/api/class/math-vector2) {#pathdelta-phasermathvector2}


**说明:**

追随者从前一点到当前点的行驶距离,在最后更新时.


> 源码：[src/gameobjects/components/PathFollower.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L75)  
引入版本：3.23.0


---

### pathOffset {#pathOffset}

#### pathOffset: [Phaser.Math.Vector2](/api/class/math-vector2) {#pathoffset-phasermathvector2}


**说明:**

用于添加路径跟踪器位置的附加向量,允许您从路径坐标中抵消它 。


> 源码：[src/gameobjects/components/PathFollower.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L56)  
引入版本：3.0.0


---

### pathTween {#pathTween}

#### pathTween: [Phaser.Tweens.Tween](/api/class/tweens-tween) {#pathtween-phasertweenstween}


**说明:**

特温用来遵循路径.


> 源码：[src/gameobjects/components/PathFollower.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L84)  
引入版本：3.0.0


---

### pathVector {#pathVector}

#### pathVector: [Phaser.Math.Vector2](/api/class/math-vector2) {#pathvector-phasermathvector2}


**说明:**

存储跟踪者所开启路径当前点的矢量2。


> 源码：[src/gameobjects/components/PathFollower.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L66)  
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





**From [Phaser.GameObjects.Components.PathFollower](/api/namespace/gameobjects-components-pathfollower):**


 - [isFollowing](/api/namespace/gameobjects-components-pathfollower#isFollowing)
 - [pathUpdate](/api/namespace/gameobjects-components-pathfollower#pathUpdate)
 - [pauseFollow](/api/namespace/gameobjects-components-pathfollower#pauseFollow)
 - [resumeFollow](/api/namespace/gameobjects-components-pathfollower#resumeFollow)
 - [setPath](/api/namespace/gameobjects-components-pathfollower#setPath)
 - [setRotateToPath](/api/namespace/gameobjects-components-pathfollower#setRotateToPath)
 - [startFollow](/api/namespace/gameobjects-components-pathfollower#startFollow)
 - [stopFollow](/api/namespace/gameobjects-components-pathfollower#stopFollow)





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
 - [removedFromScene](/api/class/gameobjects-sprite#removedFromScene)
 - [stop](/api/class/gameobjects-sprite#stop)
 - [stopAfterDelay](/api/class/gameobjects-sprite#stopAfterDelay)
 - [stopAfterRepeat](/api/class/gameobjects-sprite#stopAfterRepeat)
 - [stopOnFrame](/api/class/gameobjects-sprite#stopOnFrame)
 - [toJSON](/api/class/gameobjects-sprite#toJSON)




---

## 公开方法 {#public-methods}

### preUpdate {#preUpdate}

#### \<instance> preUpdate(time, delta) {#instance-preupdatetime-delta}


**说明:**

将路径跟踪器沿路径推进的内部更新处理器 。

由场景步骤自动调用,一般不应直接调用.


**Access:** 保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 请求动画框架或SetTimeout生成的当前时间戳 。 |
| delta | number | 否 | 三角洲时间,以ms计, 过去了,自上一个框架。 |


**Overrides:** Phaser.GameObjects.Sprite#preUpdate


> 源码：[src/gameobjects/pathfollower/PathFollower.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/pathfollower/PathFollower.js#L58)  
引入版本：3.0.0


---

---
