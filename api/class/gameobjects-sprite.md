# Sprite {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-sprite)

一个Sprite游戏对象.

斯普林特游戏对象用于在游戏中显示静态和动画图像。斯普林特可以有输入事件和物理体,也可以被调色,有色,有卷轴和动画.

斯普丽特和图像游戏对象的主要区别在于无法动画图像。因此,斯普丽特需要花费更长的时间来处理,并且由于动画组件而具有更大的API脚印。如果不需要动画,那么可以安全地使用图像来替换所有情况下的斯普丽特.

**构造函数**

`new Sprite(scene, x, y, texture, [frame])`

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

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip)  
> [Phaser.GameObjects.Components.GetBounds](/api/namespace/gameobjects-components-getbounds)  
> [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting)  
> [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask)  
> [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin)  
> [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  
> [Phaser.GameObjects.Components.Size](/api/namespace/gameobjects-components-size)  
> [Phaser.GameObjects.Components.TextureCrop](/api/namespace/gameobjects-components-texturecrop)  
> [Phaser.GameObjects.Components.Tint](/api/namespace/gameobjects-components-tint)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/sprite/Sprite.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L14)  
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




---

## 公开成员 {#public-members}

### anims {#anims}

#### anims: [Phaser.Animations.AnimationState](/api/class/animations-animationstate) {#anims-phaseranimationsanimationstate}


**说明:**

此 Sprite 的动画状态组件 。

此组件提供了将动画应用到此Sprite的功能,它负责播放,加载,排队动画进行后期播放,动画间混合,以及将当前动画框设置在这个Sprite上.


> 源码：[src/gameobjects/sprite/Sprite.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L93)  
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




---

## 公开方法 {#public-methods}

### addedToScene {#addedToScene}

#### \<instance> addedToScene() {#instance-addedtoscene}


**说明:**

当此 Sprite 添加到场景中时, 由 Phaser 自动调用 。

将这个Sprite与Scene的更新列表一起注册,这样其`preUpdate`方法就被称为每个游戏步骤,允许动画推进每个帧.


**Overrides:** Phaser.GameObjects.GameObject#addedToScene


> 源码：[src/gameobjects/sprite/Sprite.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L130)  
引入版本：3.53.0


---

### chain {#chain}

#### \<instance> chain([key]) {#instance-chainkey}


**说明:**

设定动画,或一系列动画,在当前动画完成或停止后立即播放.

当前动画必须输入一个"完成"状态才能实现,即完成它的所有重复,延迟等,或者直接调用`stop`方法.

将永远重复的动画集永远不会进入一个完成状态.

您可以在任何时间,包括当前动画开始播放之前,期间,或当它结束(通过其`animationcomplete`事件)时,对新动画进行链条.

链条动画是游戏对象的特有作品,意指不同的游戏对象可以有不同的链条动画而不影响他们正在玩的动画.

调用此方法, 无需参数来重置所有目前串联的动画 。

当在 Sprite 上播放动画时, 它会首先检查它能否在 Sprite 内找到匹配的密钥。 如果可以, 它会播放本地动画。 如果不行, 它会搜索全球动画管理器, 并在那里查找 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | Array.\<string> | Array.\<[Phaser.Animations.Animation](/api/class/animations-animation)> | Array.\<[Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig)> | 是 | 动画的弦键要播放,或动画实例,或`PlayAnimationConfig`对象,或其中的数组. |


**返回值:** [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) - 此游戏对象 。


> 源码：[src/gameobjects/sprite/Sprite.js#L360](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L360)  
引入版本：3.50.0


---

### play {#play}

#### \<instance> play(key, [ignoreIfPlaying]) {#instance-playkey-ignoreifplaying}


**说明:**

开始在此Sprite上播放给定的动画.

Phaser中的动画可以属于全球动画管理器,也可以具体属于这个Sprite.

全球动画的好处是,多部Sprite可以全部播放相同的动画,而无需重复数据。你可以一次一次地在任意的Sprite上播放。

以下代码显示如何创建全球重复动画。 动画将从装入密钥“ muybridge” 的图示工作表中的所有框架创建 :

```javascript
var config = {
    key: 'run',
    frames: 'muybridge',
    frameRate: 15,
    repeat: -1
};

//  This code should be run from within a Scene:
this.anims.create(config);
```

然而,如果您想要创建一个这个Sprite独有的动画, 而这个Sprite单独使用, 您可以调用 `Animation.create` 方法。 它接受与创建全局动画时完全相同的参数, 然而所产生的数据会保存在这个Sprite 中 。

在全球或本地创作的动画中,你可以在这个Sprite上播放:

```javascript
this.add.sprite(x, y).play('run');
```

或者,如果您想要以不同的帧率运行,例如,您可以通过一个配置对象:

```javascript
this.add.sprite(x, y).play({ key: 'run', frameRate: 24 });
```

当在 Sprite 上播放动画时, 它会首先检查它能否在 Sprite 内找到匹配的密钥。 如果可以, 它会播放本地动画。 如果不行, 它会搜索全球动画管理器, 并在那里查找 。

如果您需要Sprite来同时播放本地和全局动画,请确保它们没有相互冲突的密钥.

关于此方面的更多细节,请参看`PlayAnimationConfig`配置对象的文档.

另外,关于动画创作的进一步详情,请参见动画管理器中的文档.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | 否 |  | 动画要播放的字符串键,或动画实例,或`PlayAnimationConfig`对象. |
| ignoreIfPlaying | boolean | 是 | false | 如果动画已经播放了,那么就忽略这个电话. |


**返回值:** [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) - 此游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_START](/api/event/animations-events#animation_start)


> 源码：[src/gameobjects/sprite/Sprite.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L173)  
引入版本：3.0.0


---

### playAfterDelay {#playAfterDelay}

#### \<instance> playAfterDelay(key, delay) {#instance-playafterdelaykey-delay}


**说明:**

等待指定的延迟,以毫秒计,然后开始播放指定的动画.

如果动画_ also_ 在其配置中有一个延迟值设置,则会被**加到此处给出的延迟中** 。

如果动画已经运行,并且给这个方法提供了新的动画,它将会等待给定的延迟,然后开始新的动画.

如果目前没有运行动画,则在延迟后开始给定动画.

当在 Sprite 上播放动画时, 它会首先检查它能否在 Sprite 内找到匹配的密钥。 如果可以, 它会播放本地动画。 如果不行, 它会搜索全球动画管理器, 并在那里查找 。

在Phaser 3.50之前,这种方法被称为"delayedPlay".

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | 否 | 动画要播放的字符串键,或动画实例,或`PlayAnimationConfig`对象. |
| delay | number | 否 | 延迟,以毫秒计,等待动画开始播放. |


**返回值:** [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) - 此游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_START](/api/event/animations-events#animation_start)


> 源码：[src/gameobjects/sprite/Sprite.js#L303](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L303)  
引入版本：3.50.0


---

### playAfterRepeat {#playAfterRepeat}

#### \<instance> playAfterRepeat(key, [repeatCount]) {#instance-playafterrepeatkey-repeatcount}


**说明:**

等待当前动画完成`repeatCount`的重复周期数,然后开始回放给定动画.

你可以用这个来确保两组动画之间没有严酷的跳动,即通过让它们顺利地融合到彼此中来从闲动画到行走动画.

如果目前没有动画运行,则给定的动画会立即开始.

当在 Sprite 上播放动画时, 它会首先检查它能否在 Sprite 内找到匹配的密钥。 如果可以, 它会播放本地动画。 如果不行, 它会搜索全球动画管理器, 并在那里查找 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | 否 |  | 动画要播放的字符串键,或动画实例,或`PlayAnimationConfig`对象. |
| repeatCount | number | 是 | 1 | 动画在下一部开始前要重复多少次?. |


**返回值:** [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) - 此游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_START](/api/event/animations-events#animation_start)


> 源码：[src/gameobjects/sprite/Sprite.js#L333](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L333)  
引入版本：3.50.0


---

### playReverse {#playReverse}

#### \<instance> playReverse(key, [ignoreIfPlaying]) {#instance-playreversekey-ignoreifplaying}


**说明:**

开始在这张Sprite上播放给定的动画,反向播放.

Phaser中的动画可以属于全球动画管理器,也可以具体属于这个Sprite.

全球动画的好处是,多部Sprite可以全部播放相同的动画,而无需重复数据。你可以一次一次地在任意的Sprite上播放。

以下代码显示如何创建全球重复动画。 动画将从装入密钥“ muybridge” 的图示工作表中的所有框架创建 :

```javascript
var config = {
    key: 'run',
    frames: 'muybridge',
    frameRate: 15,
    repeat: -1
};

//  This code should be run from within a Scene:
this.anims.create(config);
```

然而,如果您想要创建一个这个Sprite独有的动画, 而这个Sprite单独使用, 您可以调用 `Animation.create` 方法。 它接受与创建全局动画时完全相同的参数, 然而所产生的数据会保存在这个Sprite 中 。

在全球或本地创作的动画中,你可以在这个Sprite上播放:

```javascript
this.add.sprite(x, y).playReverse('run');
```

或者,如果您想要以不同的帧率运行,例如,您可以通过一个配置对象:

```javascript
this.add.sprite(x, y).playReverse({ key: 'run', frameRate: 24 });
```

当在 Sprite 上播放动画时, 它会首先检查它能否在 Sprite 内找到匹配的密钥。 如果可以, 它会播放本地动画。 如果不行, 它会搜索全球动画管理器, 并在那里查找 。

如果您需要Sprite来同时播放本地和全局动画,请确保它们没有相互冲突的密钥.

关于此方面的更多细节,请参看`PlayAnimationConfig`配置对象的文档.

另外,关于动画创作的进一步详情,请参见动画管理器中的文档.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | 否 |  | 动画要播放的字符串键,或动画实例,或`PlayAnimationConfig`对象. |
| ignoreIfPlaying | boolean | 是 | false | 如果动画已经播放了,那么就忽略这个电话. |


**返回值:** [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) - 此游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_START](/api/event/animations-events#animation_start)


> 源码：[src/gameobjects/sprite/Sprite.js#L238](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L238)  
引入版本：3.50.0


---

### preUpdate {#preUpdate}

#### \<instance> preUpdate(time, delta) {#instance-preupdatetime-delta}


**说明:**

更新此 Sprite 的动画 。


**Access:** 保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 现时时标. |
| delta | number | 否 | 三角洲时间,以ms计, 过去了,自上一个框架。 |


> 源码：[src/gameobjects/sprite/Sprite.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L158)  
引入版本：3.0.0


---

### removedFromScene {#removedFromScene}

#### \<instance> removedFromScene() {#instance-removedfromscene}


**说明:**

当此 Sprite 从场景中移除时, 由 Phaser 自动调用 。

解除对Scene更新列表中的这个Sprite的注册,使其`preUpdate`方法不再称为每个游戏步骤.


**Overrides:** Phaser.GameObjects.GameObject#removedFromScene


> 源码：[src/gameobjects/sprite/Sprite.js#L144](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L144)  
引入版本：3.53.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

立即停止当前动画播放,并发送`ANIMATION_STOP`事件.

如果没有动画播放, 将不会发出任何事件 。

如果有另一个动画队列(通过`chain`方法),它会立即开始播放.


**返回值:** [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) - 此游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_STOP](/api/event/animations-events#animation_stop)


> 源码：[src/gameobjects/sprite/Sprite.js#L392](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L392)  
引入版本：3.50.0


---

### stopAfterDelay {#stopAfterDelay}

#### \<instance> stopAfterDelay(delay) {#instance-stopafterdelaydelay}


**说明:**

停止在指定时间延迟后播放当前动画,以毫秒计。

然后它就发出`ANIMATION_STOP`事件.

如果没有动画运行,则不会发出事件.

如果队列中还有另一部动画(通过`chain`方法设定),那么当当前动画停止时,它就会开始播放.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delay | number | 否 | 等待的毫秒数,然后停止这款动画. |


**返回值:** [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) - 此游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_STOP](/api/event/animations-events#animation_stop)


> 源码：[src/gameobjects/sprite/Sprite.js#L410](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L410)  
引入版本：3.50.0


---

### stopAfterRepeat {#stopAfterRepeat}

#### \<instance> stopAfterRepeat([repeatCount]) {#instance-stopafterrepeatrepeatcount}


**说明:**

停止当前动画在给定重复次数后播放。

然后它就发出`ANIMATION_STOP`事件.

如果没有动画运行,则不会发出事件.

如果队列中还有另一部动画(通过`chain`方法设定),那么当当前动画停止时,它就会开始播放.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| repeatCount | number | 是 | 1 | 动画在停播前要重复多少次?. |


**返回值:** [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) - 此游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_STOP](/api/event/animations-events#animation_stop)


> 源码：[src/gameobjects/sprite/Sprite.js#L433](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L433)  
引入版本：3.50.0


---

### stopOnFrame {#stopOnFrame}

#### \<instance> stopOnFrame(frame) {#instance-stoponframeframe}


**说明:**

当当前动画下个设定给定的帧时停止播放。 如果此帧不存在在动画中, 则不会阻止它播放 。

然后它就发出`ANIMATION_STOP`事件.

如果没有动画运行,则不会发出事件.

如果队列中还有另一部动画(通过`chain`方法设定),那么当当前动画停止时,它就会开始播放.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| frame | [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) | 否 | 停止这段动画前要检查的帧 。 |


**返回值:** [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) - 此游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_STOP](/api/event/animations-events#animation_stop)


> 源码：[src/gameobjects/sprite/Sprite.js#L456](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L456)  
引入版本：3.50.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

构建此 Sprite 的 JSON 代表 。


**Overrides:** Phaser.GameObjects.GameObject#toJSON


**返回值:** [Phaser.Types.GameObjects.JSONGameObject](/api/typedef/types-gameobjects#jsongameobject) - 游戏对象的JSON代表.


> 源码：[src/gameobjects/sprite/Sprite.js#L480](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/Sprite.js#L480)  
引入版本：3.0.0


---

---
