# Gradient {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-gradient)

渐变游戏对象 。

此游戏对象是一个四重奏, 显示渐变。 您可以像其它任何角色一样操纵此对象, 使其具有交互性, 并用在过滤器和面具中, 以创建视觉惊人的效果 。

幕后,一个渐变器(A Gradient)是使用特定遮荫程序的一种[Phaser.GameObjects.Shader](/api/class/gameobjects-shader).

梯度颜色由包含一个或多个[Phaser.Display.ColorBand](/api/class/display-colorband)对象的[Phaser.Display.ColorRamp](/api/class/display-colorramp)决定。坡度沿梯度的`shape`排列,源于`start`的位置。`shapeMode`描述了梯度如何填充到其他地方,例如LINEAR梯度产生直带,而RADIAL梯度则产生圆圈。

注意梯度的形状是配方形。如果宽度和高度不相等,形状就会扭曲。这可能是你想要的。

渐变可以通过修改其`offset`属性或修改坡道数据来进行动画化。如果修改坡道数据,可能需要拨打`gradient.ramp.encode()`以重建它。

**构造函数**

`new Gradient(scene, [config], [x], [y], [width], [height])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属景点 。 |
| config | [Phaser.Types.GameObjects.Gradient.GradientQuadConfig](/api/typedef/types-gameobjects-gradient#gradientquadconfig) | 是 |  | 此游戏对象的配置 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Shader](/api/class/gameobjects-shader)  



> 源码：[src/gameobjects/gradient/Gradient.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/gradient/Gradient.js#L14)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


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





**From [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin):**


 - [displayOriginX](/api/namespace/gameobjects-components-origin#displayOriginX)
 - [displayOriginY](/api/namespace/gameobjects-components-origin#displayOriginY)
 - [originX](/api/namespace/gameobjects-components-origin#originX)
 - [originY](/api/namespace/gameobjects-components-origin#originY)





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





**From [Phaser.GameObjects.Shader](/api/class/gameobjects-shader):**


 - [drawingContext](/api/class/gameobjects-shader#drawingContext)
 - [glTexture](/api/class/gameobjects-shader#glTexture)
 - [renderNode](/api/class/gameobjects-shader#renderNode)
 - [renderToTexture](/api/class/gameobjects-shader#renderToTexture)
 - [texture](/api/class/gameobjects-shader#texture)
 - [textureCoordinateBottomLeft](/api/class/gameobjects-shader#textureCoordinateBottomLeft)
 - [textureCoordinateBottomRight](/api/class/gameobjects-shader#textureCoordinateBottomRight)
 - [textureCoordinateTopLeft](/api/class/gameobjects-shader#textureCoordinateTopLeft)
 - [textureCoordinateTopRight](/api/class/gameobjects-shader#textureCoordinateTopRight)
 - [textures](/api/class/gameobjects-shader#textures)




---

## 公开成员 {#public-members}

### dither {#dither}

#### dither: boolean {#dither-boolean}


**说明:**

是否将梯度缩小。 这会通过在梯度中添加微小的噪音来消除带宽。 调整大小可能会失去效果, 所以只有在它能产生效果时才会启用它 。


> 源码：[src/gameobjects/gradient/Gradient.js#L242](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/gradient/Gradient.js#L242)  
引入版本：4.0.0


---

### offset {#offset}

#### offset: number {#offset-number}


**说明:**

移动梯度的起始。您可以以此方式对梯度进行动画。

注意, 偏移效果会根据形状和重复模式变化。 二次曲线梯度可能看起来很奇怪 !

使用模式1(TRUNCATE)将偏移从 -1 改为 1 来创建一次性冲击波。

使用模式2(SAWOTH)或模式3(TRINGULAR)来创建移动模式.


> 源码：[src/gameobjects/gradient/Gradient.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/gradient/Gradient.js#L132)  
引入版本：4.0.0


---

### ramp {#ramp}

#### ramp: [Phaser.Display.ColorRamp](/api/class/display-colorramp) {#ramp-phaserdisplaycolorramp}


**说明:**

包含梯度颜色数据的斜坡 。

默认情况下, 这是从黑色到白色的线性进展。 您可以用 ColorRamp 编码更加复杂的梯度 。


> 源码：[src/gameobjects/gradient/Gradient.js#L117](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/gradient/Gradient.js#L117)  
引入版本：4.0.0


---

### repeatMode {#repeatMode}

#### repeatMode: number {#repeatmode-number}


**说明:**

梯度的重复模式。 渐变进度被评价为数字, 其中 0 是 `shape` 向量的开始, 1 是结束。 重复模式告诉我们如何处理 0 / 以上 1 下的数字 。

这可以包括以下内容:

- 0(EXTEND): 值被夹在 0 和 1 之间,

  渐变的末端变成平整的颜色。

- 1(TRUNCATE):值在0-1之外被丢弃.

  从而渐变的结束变得透明。

- 2 (SAWOOTH):值为modulo 1,

  梯度会重复

- 3 (TRIANGULAR):数值上升至1,然后下降至0,

  梯度会顺畅地回转

注意, 二次曲线梯度不会离开范围 0-1, 除非应用了偏移。 如果您使用, 则可能看起来很奇怪 。


> 源码：[src/gameobjects/gradient/Gradient.js#L151](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/gradient/Gradient.js#L151)  
引入版本：4.0.0


---

### shape {#shape}

#### shape: [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) {#shape-phasertypesmathvector2like}


**说明:**

渐变的形状向量在其四边形中。这从开始指向渐变向量流的方向。渐变的颜色从 `start` 向量开始,到此端结束。


> 源码：[src/gameobjects/gradient/Gradient.js#L221](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/gradient/Gradient.js#L221)  
引入版本：4.0.0


---

### shapeMode {#shapeMode}

#### shapeMode: number {#shapemode-number}


**说明:**

梯度的形状模式。形状以`shape`向量为基础。

这可以包括以下内容:

- 0(LINEAR):一种带状,形状从一边指向另一边.

  通常用于天空等.

- 1(BILINEAR):类似于LINEAR,但反映于双向.

  用于温柔的波浪,反射等.

- 2 (RADIAL): 梯度从`start`展开,

  以`shape`描述的半径为单位.

  可用于光线,波纹等.

- 3 (CONIC_SYMMETRIC):梯度由角度决定到`shape`,

  从0沿形状向量到1对面

  用于锐视特征或光效应.

- 4 (CONIC_ASYMMETRIC):梯度由角度决定到`shape`,

  由 0 到 1 , 并进行全旋转。 这会产生一个连接 。

  不错的创造颜色 随角度而变化,

  像是速度计


> 源码：[src/gameobjects/gradient/Gradient.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/gradient/Gradient.js#L178)  
引入版本：4.0.0


---

### start {#start}

#### start: [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) {#start-phasertypesmathvector2like}


**说明:**

渐变在四角内开始的位置。渐变来自此点。渐变的颜色从这里开始,到`shape`向量的尖端结束。


> 源码：[src/gameobjects/gradient/Gradient.js#L206](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/gradient/Gradient.js#L206)  
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





**From [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin):**


 - [setDisplayOrigin](/api/namespace/gameobjects-components-origin#setDisplayOrigin)
 - [setOrigin](/api/namespace/gameobjects-components-origin#setOrigin)
 - [setOriginFromFrame](/api/namespace/gameobjects-components-origin#setOriginFromFrame)
 - [updateDisplayOrigin](/api/namespace/gameobjects-components-origin#updateDisplayOrigin)





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





**From [Phaser.GameObjects.Shader](/api/class/gameobjects-shader):**


 - [getUniform](/api/class/gameobjects-shader#getUniform)
 - [renderImmediate](/api/class/gameobjects-shader#renderImmediate)
 - [setRenderToTexture](/api/class/gameobjects-shader#setRenderToTexture)
 - [setTextureCoordinates](/api/class/gameobjects-shader#setTextureCoordinates)
 - [setTextureCoordinatesFromFrame](/api/class/gameobjects-shader#setTextureCoordinatesFromFrame)
 - [setTextures](/api/class/gameobjects-shader#setTextures)
 - [setUniform](/api/class/gameobjects-shader#setUniform)
 - [setupUniforms](/api/class/gameobjects-shader#setupUniforms)




---

## 公开方法 {#public-methods}

### preDestroy {#preDestroy}

#### \<instance> preDestroy() {#instance-predestroy}


**说明:**

内部破坏处理器,作为破坏过程的一部分而叫作.


**Access:** 保护


**Overrides:** Phaser.GameObjects.Shader#preDestroy


> 源码：[src/gameobjects/gradient/Gradient.js#L306](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/gradient/Gradient.js#L306)  
引入版本：4.0.0


---

---
