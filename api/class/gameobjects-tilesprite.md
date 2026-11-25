# TileSprite {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-tilesprite)

纹理(TileSprite)是一种具有重复纹理的螺旋体.

纹理可以独立于TileSprite本身进行滚动和缩放,纹理会自动包扎,设计上可以让您以无缝纹理作为源头创建游戏背景.

您不应该创建比实际画布大小更大的 TileSprite 。 如果您想要创建一个大背景, 滚动整个游戏的地图, 那么您就创建一个符合画布大小的 TileSpritet, 然后在玩家移动时使用 `tilePosition` 属性来滚动纹理。 如果您创建一个像素为千的 TileSprite, 那么它会消耗大量的内存, 并引起性能问题 。 请记住: 使用 `tilePosition`来滚动您的纹理和 `tileScale`来调整纹理的大小 - 不要调整纹理本身大小或使其比它需要的要大 。

Phaser 4 之前, TileSprite 不支持旋转. WebGL 中,它要求纹理为两大小的功率,也不支持压缩纹理或动态纹理,它可以引入非两大小的纹理的异名文物,这些限制已经在v4中解除.

**构造函数**

`new TileSprite(scene, x, y, width, height, textureKey, [frameKey])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| width | number | 否 | 游戏对象的宽度。 如果为零, 则会使用纹理框架的大小 。 |
| height | number | 否 | 游戏对象的高度。 如果为零, 则会使用纹理框架的大小 。 |
| textureKey | string | 否 | 此游戏对象将使用的质地键用于渲染, 如保存在质地管理器中。 无法成为动态图案 。 |
| frameKey | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip)  
> [Phaser.GameObjects.Components.GetBounds](/api/namespace/gameobjects-components-getbounds)  
> [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting)  
> [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask)  
> [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin)  
> [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  
> [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture)  
> [Phaser.GameObjects.Components.Tint](/api/namespace/gameobjects-components-tint)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/tilesprite/TileSprite.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L21)  
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





**From [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize):**


 - [displayHeight](/api/namespace/gameobjects-components-computedsize#displayHeight)
 - [displayWidth](/api/namespace/gameobjects-components-computedsize#displayWidth)
 - [height](/api/namespace/gameobjects-components-computedsize#height)
 - [width](/api/namespace/gameobjects-components-computedsize#width)





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





**From [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture):**


 - [frame](/api/namespace/gameobjects-components-texture#frame)
 - [texture](/api/namespace/gameobjects-components-texture#texture)





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

这部TileSprite的动画状态组件.

此组件提供了将动画应用到这个TileSprite的功能,负责播放,加载,排队动画进行后期播放,动画间混合,并将当前动画框设置到这个TileSprite.


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L253](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L253)  
引入版本：3.0.0


---

### canvas {#canvas}

#### canvas: HTMLCanvasElement {#canvas-htmlcanvaselement}


**说明:**

TileSprite 使填充模式变为的 Canvas 元素。 仅用于 Canvas 模式 。


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L163](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L163)  
引入版本：3.12.0


---

### context {#context}

#### context: CanvasRenderingContext2D {#context-canvasrenderingcontext2d}


**说明:**

TileSprite 将其填充模式变为 Canvas 元素的背景。 仅用于 Canvas 模式 。


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L173)  
引入版本：3.12.0


---

### dirty {#dirty}

#### dirty: boolean {#dirty-boolean}


**说明:**

梯形螺旋桨是否以某种方式改变,需要重新调整其瓦质纹理.

这些变化包括了Tile Sprite的纹理框架和滚动位置.

这在WebGL模式中是无关紧要的.


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L140)  
引入版本：3.0.0


---

### fillCanvas {#fillCanvas}

#### fillCanvas: HTMLCanvasElement {#fillcanvas-htmlcanvaselement}


**说明:**

提勒斯普里特的纹理被制成的 Canvas。 用来创建 WebGL 纹理 。


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L224](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L224)  
引入版本：3.12.0


---

### fillContext {#fillContext}

#### fillContext: CanvasRenderingContext2D {#fillcontext-canvasrenderingcontext2d}


**说明:**

用来制作蒂勒斯普里特纹理的 Canvas Control 。


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L234](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L234)  
引入版本：3.12.0


---

### fillPattern {#fillPattern}

#### fillPattern: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper), CanvasPattern {#fillpattern-phaserrendererwebglwrapperswebgltexturewrapper-canvaspattern}


**说明:**

将“平板玻璃”制成的纹理,然后被制成一个场景。在WebGL中,这是一台“WebGLTexture Wrapper”。在Canvas中,它是一个“Canvas填充模式”。


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L243](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L243)  
引入版本：3.12.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer), [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrenderercanvascanvasrenderer-phaserrendererwebglwebglrenderer}


**说明:**

这个 Tile Sprite 正在使用的渲染器 。


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L154)  
引入版本：3.0.0


---

### tilePositionX {#tilePositionX}

#### tilePositionX: number {#tilepositionx-number}


**说明:**

平面螺旋桨的横向滚动位置 。


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L641](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L641)  
引入版本：3.0.0


---

### tilePositionY {#tilePositionY}

#### tilePositionY: number {#tilepositiony-number}


**说明:**

蒂尔螺旋柱的垂直滚动位置 。


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L664](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L664)  
引入版本：3.0.0


---

### tileRotation {#tileRotation}

#### tileRotation: number {#tilerotation-number}


**说明:**

梯形螺旋纹理的旋转,以弧度表示.


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L687](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L687)  
引入版本：4.0.0


---

### tileScaleX {#tileScaleX}

#### tileScaleX: number {#tilescalex-number}


**说明:**

平面螺旋纹理的横向尺度.


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L708](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L708)  
引入版本：3.11.0


---

### tileScaleY {#tileScaleY}

#### tileScaleY: number {#tilescaley-number}


**说明:**

梯形螺旋纹理的垂直尺度.


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L731](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L731)  
引入版本：3.11.0


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





**From [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture):**


 - [setTexture](/api/namespace/gameobjects-components-texture#setTexture)





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
 - [toJSON](/api/class/gameobjects-gameobject#toJSON)
 - [update](/api/class/gameobjects-gameobject#update)
 - [willRender](/api/class/gameobjects-gameobject#willRender)
 - [willRoundVertices](/api/class/gameobjects-gameobject#willRoundVertices)




---

## 公开方法 {#public-methods}

### addedToScene {#addedToScene}

#### \<instance> addedToScene() {#instance-addedtoscene}


**说明:**

将这个 TileSprite 添加到 Scene 的更新列表中, 以便其 `preUpdate` 方法被称为每个游戏步骤来推进其动画。 当此游戏对象被添加到 Scene时, 自动调用 。


**Overrides:** Phaser.GameObjects.GameObject#addedToScene


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L290](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L290)  
引入版本：3.50.0


---

### preDestroy {#preDestroy}

#### \<instance> preDestroy() {#instance-predestroy}


**说明:**

内部破坏处理器,作为破坏过程的一部分而叫作.


**Access:** 保护


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L609](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L609)  
引入版本：3.9.0


---

### preUpdate {#preUpdate}

#### \<instance> preUpdate(time, delta) {#instance-preupdatetime-delta}


**说明:**

更新此 TileSprite 的动画 。


**Access:** 保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 现时时标. |
| delta | number | 否 | 三角洲时间,以ms计, 过去了,自上一个框架。 |


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L316](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L316)  
引入版本：3.0.0


---

### removedFromScene {#removedFromScene}

#### \<instance> removedFromScene() {#instance-removedfromscene}


**说明:**

从 Scene 更新列表中删除此 TileSprite, 停止调用它的 `preUpdate` 方法。 当此游戏对象从 Scene 中删除时, 自动调用 。


**Overrides:** Phaser.GameObjects.GameObject#removedFromScene


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L303](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L303)  
引入版本：3.50.0


---

### setFrame {#setFrame}

#### \<instance> setFrame(frame) {#instance-setframeframe}


**说明:**

设置此游戏对象将使用的框架 。

框架必须属于当前使用的纹理。

可以是字符串也可以是索引.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| frame | string \| number | 否 | 纹理内框的名称或索引. |


**Overrides:** Phaser.GameObjects.Components.Texture#setFrame


**返回值:** [Phaser.GameObjects.TileSprite](/api/class/gameobjects-tilesprite) - 此游戏对象实例 。


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L331](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L331)  
引入版本：3.0.0


---

### setSize {#setSize}

#### \<instance> setSize(width, height) {#instance-setsizewidth-height}


**说明:**

设定 TileSprite 输出区域的大小 。

这不会改变比例。

如果您启用了此游戏对象输入, 更改大小也会改变命中区域的大小, 除非您定义了自定义的命中区域 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 此游戏对象的宽度 。 |
| height | number | 否 | 此游戏对象的高度 。 |


**Overrides:** Phaser.GameObjects.Components.ComputedSize#setSize


**返回值:** [Phaser.GameObjects.TileSprite](/api/class/gameobjects-tilesprite) - 此游戏对象实例 。


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L575](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L575)  
引入版本：4.0.0


---

### setSizeToFrame {#setSizeToFrame}

#### \<instance> setSizeToFrame() {#instance-setsizetoframe}


**说明:**

与动画兼容的无-op方法.


**返回值:** [Phaser.GameObjects.TileSprite](/api/class/gameobjects-tilesprite) - 这个"砖石"的例子


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L365](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L365)  
引入版本：4.0.0


---

### setTilePosition {#setTilePosition}

#### \<instance> setTilePosition([x], [y]) {#instance-settilepositionx-y}


**说明:**

设置平板纹理的横向和纵向滚动位置, 更新 [Phaser.GameObjects.TileSprite#tilePositionX](/api/class/gameobjects-tilesprite#tilePositionX) 和 [Phaser.GameObjects.TileSprite#tilePositionY](/api/class/gameobjects-tilesprite#tilePositionY) 。 任何值都可以省略, 以保持不变 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 是 | 此图案的纹理的 x 位置 。 |
| y | number | 是 | 此图案的纹理的y位置 。 |


**返回值:** [Phaser.GameObjects.TileSprite](/api/class/gameobjects-tilesprite) - 这个"砖石"的例子


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L377](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L377)  
引入版本：3.3.0


---

### setTileRotation {#setTileRotation}

#### \<instance> setTileRotation([radians]) {#instance-settilerotationradians}


**说明:**

设置平板纹理的旋转, 以弧度表示, 更新 [Phaser.GameObjects.TileSprite#tileRotation](/api/class/gameobjects-tilesprite#tileRotation)。 纹理会绕着自己的起源旋转, 独立于 TileSprite 的世界旋转 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| radians | number | 是 | 0 | 的旋转纹理,用弧度表示. |


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L405](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L405)  
引入版本：4.0.0


---

### setTileScale {#setTileScale}

#### \<instance> setTileScale([x], [y]) {#instance-settilescalex-y}


**说明:**

设置平板纹理的横向和纵向尺度,更新 [Phaser.GameObjects.TileSprite#tileScaleX](/api/class/gameobjects-tilesprite#tileScaleX) 财务报告和已审计财务报表 [Phaser.GameObjects.TileSprite#tileScaleY](/api/class/gameobjects-tilesprite#tileScaleY)。该比例表独立于蒂莱Sprite的自身比例表。如果 `x` 提供两个轴的值。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 |  | 平板纹理的横向尺度。 如果不给出, 则会使用当前 `tileScaleX` 值 。 |
| y | number | 是 | "x" | 竖立纹理的垂直比例。 如果不给出, 则使用 `x` 值 。 |


**返回值:** [Phaser.GameObjects.TileSprite](/api/class/gameobjects-tilesprite) - 这个"砖石"的例子


> 源码：[src/gameobjects/tilesprite/TileSprite.js#L424](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSprite.js#L424)  
引入版本：3.12.0


---

---
