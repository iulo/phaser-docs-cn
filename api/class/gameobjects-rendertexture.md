# RenderTexture {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-rendertexture)

成形纹理是动态纹理和图像游戏对象的结合,使用动态纹理来显示自己.

动态纹理(Dynamic Texture)是一种特殊的纹理,它允许您直接绘制纹理,帧和最类游戏对象.

您可以带许多复杂的对象到这个纹理, 然后可以用来作为其他游戏对象, 如Sprites 的基础纹理。 如果您再更新这个纹理, 所有使用它的游戏对象都会立即更新, 立即反映变化 。

这是一种强大的方法,在运行时生成动态纹理,这种纹理是WebGL友好的,并且不会在每个变化上引用昂贵的GPU上传.

在3:60之前的Phaser版本中,一个Render纹理是唯一可以创建这样的纹理的方法,它具有被抽取的能力。但是在3:60中,我们把核心功能分割到动态纹理类,因为这使得它们更能生活在其中。因此,Render纹理现在是一个轻量级的shim,它坐在图像游戏对象的顶部,并为动态纹理中可用的特性提供代理方法。

**When should you use a Render Texture vs. a Dynamic Texture?**

如果纹理将被多个游戏对象使用,或者要跨多个景区使用,则应当使用动态纹理,因为纹理是全球存储的.

如果纹理不会在游戏中显示,而是会被用于像面具或遮阳器之类的东西,你应该使用动态纹理.

需要在一个游戏对象上显示纹理的纹理时,您应该使用一个Render纹理,因为它为您提供了将图像和动态纹理包裹在一起的便利.

在 WebGL1 下,一个框架缓冲器,即这个动态纹理内部使用的东西,不能被反异化。这意味着当将形状或图形等对象绘制到这个纹理时,它们可能看起来没有在边缘周围作别名。这是WebGL1的技术限制。要绕过它,在艺术包中创建你的形状,然后将它绘制到这个纹理上。

如果您在游戏中激活了 mipmap 支持, 它不会自动应用到动态图案。 这是因为在 10 微秒内重生成 mipmap 的纹理成本, 一个框架的性能损失很大 。 如果您想要用 mipmap 来渲染您的动态图案, 您也必须激活 compare 配置选项 Z`mipmapRegeneration` 。

如果 WebGL 上下文丢失, 此动态图解将丢失其内容。 一旦恢复上下文( 由 `restorewebgl` 事件标注) , 您可以选择重绘动态图解的内容。 您负责重绘逻辑 。

**构造函数**

`new RenderTexture(scene, [x], [y], [width], [height], [forceEven])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 32 | 宽度的Render纹理。 |
| height | number | 是 | 32 | 风化纹理的高度。 |
| forceEven | boolean | 是 | true | 强制给定的宽度和高度以四舍五入到偶数。这大大改善了渲染质量。 如果您知道需要奇数大小的纹理, 则设置为假 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Image](/api/class/gameobjects-image)  



> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L13)  
引入版本：3.2.0

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

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) {#camera-phasercamerasscene2dbasecamera}


**说明:**

内部的摄像机,可以用来绕着这个纹理移动.

控制它就像你对任何场景相机一样。不同的是它只影响游戏对象的位置,然后将它绘制到这个纹理上。

你可以滚动,放大和旋转这台摄像机.

这房子是`RenderTexture.texture.camera`的参考物.


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L99)  
引入版本：3.12.0


---

### isCurrentlyRendering {#isCurrentlyRendering}

#### isCurrentlyRendering: boolean {#iscurrentlyrendering-boolean}


**说明:**

此工程是否正在执行 `renderWebGL` 。 用于防止在绘制容器时出现无限循环。 您不应该直接设置此属性 。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L142)  
引入版本：4.0.0


---

### renderMode {#renderMode}

#### renderMode: 'render', 'redraw', 'all' {#rendermode-render-redraw-all}


**说明:**

此渲染纹理的渲染模式。 设定此属性以改变渲染纹理的渲染方式 。

- `提交'模式将“提交”纹理的内容绘制到每个框架。

- 重新绘制模式叫`render()` 重新绘制每个帧的纹理,

  用于更新纹理

  用于其他物体的再利用。

- '所有'模式叫`render()`,然后将纹理画到帧上.


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L125)  
引入版本：4.0.0


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




---

## 公开方法 {#public-methods}

### callback {#callback}

#### \<instance> callback(callback) {#instance-callbackcallback}


**说明:**

添加调试程序运行时的调用。 调用程序将作为命令缓冲器的一步运行。 它可用于为下一步绘制设置条件 。

注意, 只有在 `render()` 调用后, 才会执行 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | function | 否 | 渲染过程中要运行的调用函数 。 |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 这个纹理实例。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L568](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L568)  
引入版本：4.0.0


---

### capture {#capture}

#### \<instance> capture(entry, config) {#instance-captureentry-config}


**说明:**

绘制给定对象到此 Render 纹理。 这样您就可以绘制对象在游戏世界中出现, 或者在配置中使用各种参数覆盖 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| entry | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 任何可渲染的游戏对象。 |
| config | [Phaser.Types.Textures.CaptureConfig](/api/typedef/types-textures#captureconfig) | 否 | 抓取的配置对象 。 |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 这个纹理实例。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L492](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L492)  
引入版本：4.0.0


---

### clear {#clear}

#### \<instance> clear([x], [y], [width], [height]) {#instance-clearx-y-width-height}


**说明:**

清除从此质地中的一部分或所有内容, 将它擦除, 并将其重置为空白、 透明、 质地。 要清除一个区域, 请指定 `x`, `y`, `width` 财务报告和已审计财务报表 `height`.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 清晰矩形的左坐标. |
| y | number | 是 | 0 | 清矩的顶部坐标. |
| width | number | 是 | "this.width" | 清晰矩形的宽度 。 |
| height | number | 是 | "this.height" | 清净矩形的高度. |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 这个纹理实例。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L360](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L360)  
引入版本：3.2.0


---

### draw {#draw}

#### \<instance> draw(entries, [x], [y], [alpha], [tint]) {#instance-drawentries-x-y-alpha-tint}


**说明:**

绘制给定的对象,或一系列对象,以图示此工程。

它可以接受下列任何一种:

* 任意可渲染的游戏对象,例如Sprite,Text,Graphics或TileSprite.

* 平面图层.

* A组,内容将依次加以修改和绘制。

* 集装箱,内装物将按顺序完全悬挂和抽取。

* 一个场景显示列表,通过`Scene.children`来绘制整个列表.

* 另一种动态纹理,或称Render纹理.

* 纹理框架实例 。

* 字符串。 用于从纹理管理器中查找纹理 。

注1:你不能自己画出一个成形的纹理。

注2: Game Objects将使用相机,而纹理和帧则不会. 纹理和帧是使用`stamp`方法绘制的.

如果在一组或集装箱内通过,则只吸引在使用`willRender()`方法时返回`true`的儿童。 也就是说,一个有10个儿童的集装箱,其中5个有`visible=false`,只吸引5个可见的集装箱。

如果在一系列游戏对象中通过,它会绘制全部,无论它们是否通过`willRender`检查.

您可以在一个字符串中通过, 在这种情况下它会寻找匹配该字符串的纹理管理器, 并绘制底框。 如果您需要指定要绘制的框的确切位置, 请使用 `drawFrame` 方法 。

您可以在 `x` 和 `y` 坐标中通过绘制对象。 坐标的使用因绘制对象不同而不同。 如果对象是组、 容器或显示列表, 则坐标将 _ 添加到孩子的位置。 对于所有其他类型的对象, 坐标是准确的。 对于纹理和框架, `x` 和 `y` 值是纹理的中间值 。

`alpha`和`tint`的值只用于纹理框架。游戏对象在绘制时使用自己的α和锡值。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| entries | any | 否 |  | 任何可变游戏对象,或组合、容器、显示列表、其他纹理、纹理框架或其中任何一组。 |
| x | number | 是 | 0 | 绘制框架的x位置,或对象的偏移。 |
| y | number | 是 | 0 | 绘制框架的y位置,或对象的偏移。 |
| alpha | number | 是 | 1 | α值。 仅在绘制纹理框架到此纹理时使用。 游戏对象使用自己的α 。 |
| tint | number | 是 | "0xffffff" | 颜色值。 仅在绘制纹理框架到此纹理时使用。 游戏对象只使用自己的颜色值 。 WebGL 。 |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 这个纹理实例。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L435](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L435)  
引入版本：3.2.0


---

### erase {#erase}

#### \<instance> erase(entries, [x], [y]) {#instance-eraseentries-x-y}


**说明:**

使用 EASE 的混合模式绘制给定对象或一系列对象到此纹理。这可以消除从此纹理中显示的对象中的任何已填充像素。

这种方法在内部使用`draw`方法,参数的表现也相同.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| entries | any | 否 |  | 任何可渲染的游戏对象,或组合、容器、显示列表、纹理、纹理框架或其中任何一组。 |
| x | number | 是 | 0 | 绘制框架的x位置,或对象的偏移。 |
| y | number | 是 | 0 | 绘制框架的y位置,或对象的偏移。 |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 这个纹理实例。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L412](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L412)  
引入版本：3.16.0


---

### fill {#fill}

#### \<instance> fill(rgb, [alpha], [x], [y], [width], [height]) {#instance-fillrgb-alpha-x-y-width-height}


**说明:**

以给定的颜色填充此纹理 。

默认它会填充整个纹理,但您可以通过使用x,y,宽度和高度参数来设置它以填充特定的矩形区域.

颜色应采用六分法,即0xff000红,0x00ff00绿等.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| rgb | number | 否 |  | 将这个纹理填充的颜色, 如 0xff000 表示红色 。 |
| alpha | number | 是 | 1 | 填充时所用的α值 。 |
| x | number | 是 | 0 | 填充矩的左坐标. |
| y | number | 是 | 0 | 填充矩形的顶部坐标. |
| width | number | 是 | "this.width" | 填充矩的宽度 。 |
| height | number | 是 | "this.height" | 填充矩的高度. |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 这个纹理实例。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L333](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L333)  
引入版本：3.2.0


---

### preDestroy {#preDestroy}

#### \<instance> preDestroy() {#instance-predestroy}


**说明:**

内部破坏处理器,作为破坏过程的一部分而叫作.


**Access:** 保护


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L677](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L677)  
引入版本：3.9.0


---

### preserve {#preserve}

#### \<instance> preserve(preserve) {#instance-preservepreserve}


**说明:**

设置此动态纹理的保存旗。 通常, 每次渲染后, 命令缓冲被清除。 当此旗帜被设定为 `true` 时, 命令缓冲在渲染之间被保存。 这样就可以在每个渲染时重复相同的绘图命令 。

确定在开始时给`clear()`打电话,如果你不想在自己顶端积累绘画细节.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| preserve | boolean | 否 | 渲染后是否保留命令缓冲 。 |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 这个纹理实例。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L547](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L547)  
引入版本：4.0.0


---

### render {#render}

#### \<instance> render() {#instance-render}


**说明:**

将缓冲绘图命令渲染到此动态纹理中。 您必须这样做才能看到任何被绘制到它上 。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L319](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L319)  
引入版本：4.0.0


---

### repeat {#repeat}

#### \<instance> repeat(key, [frame], [x], [y], [width], [height], [config]) {#instance-repeatkey-frame-x-y-width-height-config}


**说明:**

将给定的纹理框架绘制到这个动态纹理中, 作为填充图案, 即基于框架尺寸的网格铺放。 它使用内部的 `TileSprite`来反复绘制框架 。

纹理通过基于字符串的密钥来引用, 存储在纹理管理器中.

您可以选择提供位置、 宽度、 高度、 α 和 tint 值, 用于绘制框架。 位置控制重复填充开始的左上角。 宽度和高度控制填充区域的大小 。

如果需要,这种位置可以是负的,但维度不能。

这种方法尊重动态纹理的相机设置.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 要使用的纹理密钥, 如存储在纹理管理器中 。 |
| frame | string \| number | 是 |  | 纹理内框架的名称或索引。 如果不需要, 设置为 `null` 来跳过此参数 。 |
| x | number | 是 | 0 | 从( 可以是负的, 以抵消) 开始绘制框架的 x 位置 。 |
| y | number | 是 | 0 | 开始从( 可以是负的来抵消) 绘制帧的 Y 位置 。 |
| width | number | 是 | "this.width" | 重复框架在内部的区域宽度。默认为此动态纹理的宽度 。 |
| height | number | 是 | "this.height" | 区域高度以重复内框。默认为此动态纹理的高度 。 |
| config | [Phaser.Types.GameObjects.TileSprite.TileSpriteConfig](/api/typedef/types-gameobjects-tilesprite#tilespriteconfig) | 是 |  | 重复纹理的 TileSprite 配置对象, 允许您在它上设置更多属性 。 |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 这个纹理实例。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L512](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L512)  
引入版本：3.60.0


---

### resize {#resize}

#### \<instance> resize(width, [height], [forceEven]) {#instance-resizewidth-height-forceeven}


**说明:**

将“Render纹理”的大小调整到给定的新尺寸。

在 WebGL 中,它会破坏并重造Render 纹理使用的帧缓冲器。在 Canvas 中,它会调整基本画布元素的大小 。

这两种方法将消除目前绘制到“纹理”的所有内容。

调用此选项将引用 `setSize` 方法, 将此游戏对象的内部大小设定为给此方法的值 。

调用此选项将引用 `setSize` 方法, 将此游戏对象的内部大小设定为给此方法的值 。

如果给出的维度与已经使用的维度相同,那么称这个方法将无济于事.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 否 |  | 新的宽度 render 纹理。 |
| height | number | 是 | "width" | 渲染纹理的新高度。 如果没有指定, 将会设置为 `width` 。 |
| forceEven | boolean | 是 | true | 强制给定的宽度和高度以四舍五入到偶数。这大大改善了渲染质量。 如果您知道需要奇数大小的纹理, 则设置为假 。 |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 此是灵丹色.


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L193](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L193)  
引入版本：3.10.0


---

### saveTexture {#saveTexture}

#### \<instance> saveTexture(key) {#instance-savetexturekey}


**说明:**

使用给定的密钥在纹理管理器中存储此纹理的复制件 。

完成此任务后,任何基于纹理的游戏对象,如Sprite,都可以通过使用纹理密钥使用此Render纹理的内容:

```javascript
var rt = this.add.renderTexture(0, 0, 128, 128);

// Draw something to the Render Texture

rt.saveTexture('doodle');

this.add.image(400, 300, 'doodle');
```

更新此 Render 纹理的内容将自动更新_ 任何_ 游戏对象, 将它用作纹理。 调用 `saveTexture` 将不再保存同一纹理的另一副本, 它将只是重命名现有复制的密钥 。

默认情况下, 它会创建一个单一的基础纹理。 您可以使用 `Texture.add` 方法在纹理中添加帧。 这样做之后, 您可以允许 Game Objects 从 Render 纹理中使用特定的帧 。

如果您摧毁了此纹理, 任何通过纹理管理器使用此纹理的游戏对象都会停止渲染。 请在销毁此纹理之前, 将纹理从纹理管理器和任何使用它的游戏对象中移除 。

注意在创建时, 纹理被随机指定一个密钥。 此密钥将被替换为新密钥。 如果纹理先前从纹理管理器中移除, 则会重新添加, 以便重新使用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 将纹理存储在全球纹理管理器内部的独有密钥 。 |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 保存下来的纹理。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L227](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L227)  
引入版本：3.12.0


---

### setRenderMode {#setRenderMode}

#### \<instance> setRenderMode(mode, [preserve]) {#instance-setrendermodemode-preserve}


**说明:**

设置此纹理的 `renderMode` 。 设定此以改变纹理的渲染方式 。

- `提交'模式将“提交”纹理的内容绘制到每个框架。

- 重新绘制模式叫`render()` 重新绘制每个帧的纹理,

  用于更新纹理

  用于其他物体的再利用。

- '所有'模式叫`render()`,然后将纹理画到帧上.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| mode | 'render' \| 'redraw' | 'all' | 否 |  | 要设置的渲染模式 。 |
| preserve | boolean | 是 | false | 是否呼叫 `preserve(true)` 以保留当前命令缓冲 。 |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 这个纹理实例。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L291](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L291)  
引入版本：4.0.0


---

### setSize {#setSize}

#### \<instance> setSize(width, height) {#instance-setsizewidth-height}


**说明:**

设置用于框架或物理体创建的此渲染纹理的内部大小。

这将不会改变游戏对象在游戏中渲染的大小。 为此您需要设置游戏对象的大小( `setScale`) 或调用 `setDisplaySize` 方法, 这与改变大小是相同的, 但允许您通过给像素值来做到这一点。 您也可以调用 `resize` 方法, 因为这种方法会调整基础纹理的大小 。

如果您启用了此游戏对象输入, 更改大小也会改变命中区域的大小, 除非您定义了自定义的命中区域 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 此游戏对象的宽度 。 |
| height | number | 否 | 此游戏对象的高度 。 |


**Overrides:** Phaser.GameObjects.Image#setSize


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 此游戏对象实例 。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L155](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L155)  
引入版本：3.0.0


---

### snapshot {#snapshot}

#### \<instance> snapshot(callback, [type], [encoderOptions]) {#instance-snapshotcallback-type-encoderoptions}


**说明:**

拍下整个纹理的画面

即刻拍摄,但结果通过给定的回调返回.

要捕捉到这个Render纹理的一部分,请查看`snapshotArea`方法。要捕捉到一个特定的像素,请查看`snapshotPixel`方法。

快照工作时使用 WebGL `readPixels` 特性将帧缓冲器中的每个像素抓入一个 ArrayBufferView 。 它然后解析这个, 将内容复制到临时的 Canvas 中, 并最后从中创建一个图像对象, 即图像返回到提供的调用 。

总之,这是一个计算成本和阻塞过程, 它得到的花费越大 这个Render纹理的分辨率, 所以请小心你是如何在游戏中使用这个的。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 |  | 创建了快照图像后要引用的函数 。 |
| 类型 | string | 是 | "'image/png'" | 图像创建的格式,通常为`image/png`或`image/jpeg`. |
| encoderOptions | number | 是 | 0.92 | 图像质量,介于0到1. 用于图像格式,具有失速压缩,例如`image/jpeg`. |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 这个纹理实例。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L622](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L622)  
引入版本：3.19.0


---

### snapshotArea {#snapshotArea}

#### \<instance> snapshotArea(x, y, width, height, callback, [type], [encoderOptions]) {#instance-snapshotareax-y-width-height-callback-type-encoderoptions}


**说明:**

绘制此纹理的指定区域 。

即刻拍摄,但结果通过给定的回调返回.

要捕捉整个Render纹理,请查看`snapshot`方法。要捕捉到一个特定的像素,请参看`snapshotPixel`方法。

快照工作时使用 WebGL `readPixels` 特性将帧缓冲器中的每个像素抓入一个 ArrayBufferView 。 它然后解析这个, 将内容复制到临时的 Canvas 中, 并最后从中创建一个图像对象, 即图像返回到提供的调用 。

总之,这是一个计算成本和阻塞过程, 它得到的花费越大 这个Render纹理的分辨率, 所以请小心你是如何在游戏中使用这个的。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 坐标是用来抓的 |
| y | number | 否 |  | 调和器用来抓 |
| width | number | 否 |  | 要抓取的区域的宽度 。 |
| height | number | 否 |  | 高地的地盘要抓 |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 |  | 创建了快照图像后要引用的函数 。 |
| 类型 | string | 是 | "'image/png'" | 图像创建的格式,通常为`image/png`或`image/jpeg`. |
| encoderOptions | number | 是 | 0.92 | 图像质量,介于0到1. 用于图像格式,具有失速压缩,例如`image/jpeg`. |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 这个纹理实例。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L587](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L587)  
引入版本：3.19.0


---

### snapshotPixel {#snapshotPixel}

#### \<instance> snapshotPixel(x, y, callback) {#instance-snapshotpixelx-y-callback}


**说明:**

从这个 Render 纹理中获取给定像素的快照 。

即刻拍摄,但结果通过给定的回调返回.

捕捉整个风化纹理 `snapshot` 方法。要捕捉此纹理的一部分,请参见 `snapshotArea` 方法。 。 方法。

与其他两种快照方法不同,这个方法会将包含请求像素的颜色数据的`Color`对象发送回调,它不需要创建内部的Canvas或Image对象,因此执行速度要快很多,使用内存比其他快照方法要少.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 以像素的x坐标获取. |
| y | number | 否 | 用于像素的y坐标 |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 | 提取快照像素数据后要引用的函数 。 |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 这个纹理实例。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L651](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L651)  
引入版本：3.19.0


---

### stamp {#stamp}

#### \<instance> stamp(key, [frame], [x], [y], [config]) {#instance-stampkey-frame-x-y-config}


**说明:**

取下给定的纹理密钥和帧, 然后在给定的 x 和 y 坐标上盖章 。 您可以使用可选的“ 配置” 参数来提供更多关于如何应用纹章的选项, 包括 alpha、 tint、 角度、 比例和来源 。

默认情况下,帧会在其中心点上的x/y坐标上盖章.

如果您想从左上方盖章, 请将配置的 `originX` 和 `originY` 属性都设置为 0 。

这种方法忽略了动态纹理的`camera`属性.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 要使用的纹理密钥, 如存储在纹理管理器中 。 |
| frame | string \| number | 是 |  | 纹理内框架的名称或索引。 如果不需要, 设置为 `null` 来跳过此参数 。 |
| x | number | 是 | 0 | 绘制帧的x位置 。 |
| y | number | 是 | 0 | 绘制框架的y位置 。 |
| config | [Phaser.Types.Textures.StampConfig](/api/typedef/types-textures#stampconfig) | 是 |  | 印章配置对象,允许您设置印章的α,锡,角度,比例和来源. |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 这个纹理实例。


> 源码：[src/gameobjects/rendertexture/RenderTexture.js#L381](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTexture.js#L381)  
引入版本：3.60.0


---

---
