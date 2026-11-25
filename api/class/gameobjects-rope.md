# Rope {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-rope)

绳式游戏对象。

绳形对象仅为WebGL,没有Canvas对应物.

绳索是一种特殊的游戏对象,它具有一个沿着其整个长度伸展的纹理,并绘制在您定义的一系列顶点上。这使得它的理想效果是,在风、旗帜、布、链、瓦水表面或任何需要沿路径弯曲或变形的纹理形状中,旗帜挥舞。

与斯匹特不同,它并不局限于只使用一个四角,并且可以在创建时定义的顶点数量相同。顶点可以排列在水平或垂直的条形上,并具有自己的颜色和α值。您可以修改顶点位置,使每个框实时地对绳索的形状进行动画化。

绳索还支持通过`anims`属性的动画,允许您从绳索表面的纹理图集中播放基于帧的动画.

绳索的起源总是0.5×0.5,不能改变.

此对象不支持 Texture Packer 的修剪纹理。 修剪可能会干扰顶点安排 。

**构造函数**

`new Rope(scene, [x], [y], [texture], [frame], [points], [horizontal], [colors], [alphas])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| texture | string | 是 |  | 此游戏对象将使用的纹理键用于渲染, 如保存在纹理管理器中。 如果不给出, 则使用 `__DEFAULT` 。 |
| frame | string \| number | null | 是 |  | 游戏对象正在用此渲染的纹理的可选框架 。 |
| points | number \| Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 是 | 2 | 包含此绳索的顶点数据的数组, 或表示要将纹理帧分割成多少段的数组。 如果未提供, 则创建一个简单的四边形。 请参见 `setPoints` 设置此创建后 。 |
| horizontal | boolean | 是 | true | 这个绳子的顶点应水平对齐(`true`),还是垂直对齐(`false`)? |
| colors | Array.\<number> | 是 |  | 包含此绳索的颜色数据的可选数组。 您应该提供每对顶点一个颜色值 。 |
| alphas | Array.\<number> | 是 |  | 包含此绳索的α数据的可选数组。 您应该提供每对顶点一个α值 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip)  
> [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask)  
> [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes)  
> [Phaser.GameObjects.Components.Size](/api/namespace/gameobjects-components-size)  
> [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  



> 源码：[src/gameobjects/rope/Rope.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L16)  
引入版本：3.23.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle):**


 - [alpha](/api/namespace/gameobjects-components-alphasingle#alpha)





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





**From [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask):**


 - [mask](/api/namespace/gameobjects-components-mask#mask)





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





**From [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture):**


 - [frame](/api/namespace/gameobjects-components-texture#frame)
 - [texture](/api/namespace/gameobjects-components-texture#texture)





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

### alphas {#alphas}

#### alphas: Float32Array {#alphas-float32array}


**说明:**

包含此绳索的α数据的阵列 。

阿尔法应该作为浮点值给出, 如 0. 5。 您应该为绳索中的每个点提供 _ 2_ 阿尔法值, 为每个四位曲线的上方和下方提供一个值 。

但是,如果需要修改阵列的_大小_大小,您可以直接实时修改这个阵列的内容,那么您应该使用`setAlphas`方法。


> 源码：[src/gameobjects/rope/Rope.js#L163](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L163)  
引入版本：3.23.0


---

### anims {#anims}

#### anims: [Phaser.Animations.AnimationState](/api/class/animations-animationstate) {#anims-phaseranimationsanimationstate}


**说明:**

此绳之动画国.


> 源码：[src/gameobjects/rope/Rope.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L98)  
引入版本：3.23.0


---

### colors {#colors}

#### colors: Uint32Array {#colors-uint32array}


**说明:**

包含此绳索的颜色数据的阵列 。

颜色应该以数字 RGB 值表示, 如 0xff000。 您应该为绳索中的每个点提供_ 2_ 颜色值, 为顶端和每个四位的底端提供一个 。

但是,如果需要修改阵列的_大小_大小,您可以直接实时修改这个阵列的内容,那么您应该使用`setColors`方法。


> 源码：[src/gameobjects/rope/Rope.js#L148](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L148)  
引入版本：3.23.0


---

### debugCallback {#debugCallback}

#### debugCallback: function {#debugcallback-function}


**说明:**

您可以选择将绳索的顶点制成图形实例 。

通过设置`debugCallback`和`debugGraphic`属性来实现这一点.

您可以通过 `Rope.setDebug` 方法在一次调用中做到这一点, 这种方法将使用内置调试函数。 您也可以设定为自己的调用。 调用调用将引用_ 一次 compare_ 并发送以下参数 :

`debugCallback(src, meshLength, verts)`

`src`是正在调试的绳索实例. `meshLength`是网格顶点的总数. `verts`是翻译顶点坐标的阵列.

要禁用渲染, 请将此属性放回 `null` 。


> 源码：[src/gameobjects/rope/Rope.js#L259](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L259)  
引入版本：3.23.0


---

### debugGraphic {#debugGraphic}

#### debugGraphic: [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) {#debuggraphic-phasergameobjectsgraphics}


**说明:**

如果调试了 `setDebug`, 调试顶点将被绘制到的图形实例 。


> 源码：[src/gameobjects/rope/Rope.js#L282](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L282)  
引入版本：3.23.0


---

### dirty {#dirty}

#### dirty: boolean {#dirty-boolean}


**说明:**

如果绳子被标记为 `dirty`, 它会在下次生成时自动重新计算它的顶点。 您也可以通过调用 `updateVertices`来强制它 。


> 源码：[src/gameobjects/rope/Rope.js#L196](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L196)  
引入版本：3.23.0


---

### flipX {#flipX}

#### flipX: boolean {#flipx-boolean}


**说明:**

游戏对象的横向翻转状态 。

横向翻转的游戏对象会让横向轴上反转。翻转总是从纹理中间进行,不会影响比例值。如果游戏对象有一个物理体,它不会改变身体。这只是一个渲染切换。


**重写:** Phaser.GameObjects.Components.Flip#flipX


> 源码：[src/gameobjects/rope/Rope.js#L1111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L1111)  
引入版本：3.23.0


---

### flipY {#flipY}

#### flipY: boolean {#flipy-boolean}


**说明:**

游戏对象的垂直翻转状态 。

垂直翻转的游戏对象会使反转在垂直轴上(即倒转)翻转总是从纹理中间进行,不会影响比例值。如果游戏对象有一个物理体,它不会改变身体。这只是一个渲染切换。


**重写:** Phaser.GameObjects.Components.Flip#flipY


> 源码：[src/gameobjects/rope/Rope.js#L1139](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L1139)  
引入版本：3.23.0


---

### horizontal {#horizontal}

#### horizontal: boolean {#horizontal-boolean}


**说明:**

绳子的顶点是水平对齐的,在条状的,还是垂直的,在柱状的?

此属性在即时状态下设置, 无法直接更改。 请参看 `setVertical` 和 `setHorizontal` 方法 。


> 源码：[src/gameobjects/rope/Rope.js#L206](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L206)  
引入版本：3.23.0


---

### points {#points}

#### points: Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> {#points-arrayphasertypesmathvector2like}


**说明:**

包含此绳索点数据的阵列 。

每个点应作为矢量2like对象(即具有公用x/y属性的矢量2或对象)给出.

点坐标在局部空间给出,其中0×0是绳条的起始点.

您可以直接实时修改此数组的内容以创建有趣的效果。 如果您这样做, 请在修改此数组后拨打 `setDirty` _ , 以便在下次渲染前更新顶点数据。 或者您可以使用 `setPoints` 方法 。

如果您需要更改此阵列的_ 大小, 您应该总是使用 `setPoints` 方法 。


> 源码：[src/gameobjects/rope/Rope.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L107)  
引入版本：3.23.0


---

### tintMode {#tintMode}

#### tintMode: [Phaser.TintModes](/api/namespace/tintmodes) {#tintmode-phasertintmodes}


**说明:**

将锡剂应用到纹理时使用的锡剂模式 。

可用模式有:

- Phaser.TintModes.MULTIPLY( 默认)

- Phaser.TintModes.FILL( 纹理为 __DEFAULT 时默认)

- Phaser.TintModes.ADD

- Phaser.TintModes.SCREEN

- Phaser.TintModes.OVERLAY

- Phaser.TintModes.HARD_LIGHT


> 源码：[src/gameobjects/rope/Rope.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L178)  
引入版本：4.0.0


---

### uv {#uv}

#### uv: Float32Array {#uv-float32array}


**说明:**

包含此绳索的 uV 数据的阵列 。

这些数据根据所提供的点数,在`setPoints`方法中自动计算.


> 源码：[src/gameobjects/rope/Rope.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L137)  
引入版本：3.23.0


---

### vertices {#vertices}

#### vertices: Float32Array {#vertices-float32array}


**说明:**

包含此绳索的顶点数据的阵列 。

这些数据根据所提供的点数,在`updateVertices`方法中自动计算.


> 源码：[src/gameobjects/rope/Rope.js#L126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L126)  
引入版本：3.23.0


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





**From [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle):**


 - [clearAlpha](/api/namespace/gameobjects-components-alphasingle#clearAlpha)
 - [setAlpha](/api/namespace/gameobjects-components-alphasingle#setAlpha)





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





**From [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask):**


 - [clearMask](/api/namespace/gameobjects-components-mask#clearMask)
 - [createGeometryMask](/api/namespace/gameobjects-components-mask#createGeometryMask)
 - [setMask](/api/namespace/gameobjects-components-mask#setMask)





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





**From [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture):**


 - [setFrame](/api/namespace/gameobjects-components-texture#setFrame)
 - [setTexture](/api/namespace/gameobjects-components-texture#setTexture)





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

当游戏对象被添加到场景中时, 由 Phaser 自动调用。 将此绳子与场景的更新列表一起注册, 这样 `preUpdate` 就可以称为每个帧 。


**重写:** Phaser.GameObjects.GameObject#addedToScene


> 源码：[src/gameobjects/rope/Rope.js#L324](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L324)  
引入版本：3.23.0


---

### play {#play}

#### \<instance> play(key, [ignoreIfPlaying], [startFrame]) {#instance-playkey-ignoreifplaying-startframe}


**说明:**

开始播放给定的动画.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 动画要播放的基于字符串的键. |
| ignoreIfPlaying | boolean | 是 | false | 如果动画已经播放了,那么就忽略这个电话. |
| startFrame | number | 是 | 0 | 选择从此帧索引开始播放动画. |


**返回值:** [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) - 此游戏对象 。


> 源码：[src/gameobjects/rope/Rope.js#L371](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L371)  
引入版本：3.23.0


---

### preUpdate {#preUpdate}

#### \<instance> preUpdate(time, delta) {#instance-preupdatetime-delta}


**说明:**

绳索更新环.


**访问权限:** 受保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 现时时标. |
| delta | number | 否 | 三角洲时间,以ms计, 过去了,自上一个框架。 |


> 源码：[src/gameobjects/rope/Rope.js#L348](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L348)  
引入版本：3.23.0


---

### removedFromScene {#removedFromScene}

#### \<instance> removedFromScene() {#instance-removedfromscene}


**说明:**

当游戏对象从场景中移除时, 自动由 Phaser 调用。 从场景更新列表中删除此绳索, 这样 `preUpdate` 不再称为每个帧 。


**重写:** Phaser.GameObjects.GameObject#removedFromScene


> 源码：[src/gameobjects/rope/Rope.js#L336](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L336)  
引入版本：3.23.0


---

### renderDebugVerts {#renderDebugVerts}

#### \<instance> renderDebugVerts(src, meshLength, verts) {#instance-renderdebugvertssrc-meshlength-verts}


**说明:**

内置绳索顶点调试渲染方法.

详情请见`Rope.setDebug`。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) | 否 | 绳子对象正在被渲染 。 |
| meshLength | number | 否 | 网状层中顶点数. |
| verts | Array.\<number> | 否 | 一组翻译的顶点坐标 。 |


> 源码：[src/gameobjects/rope/Rope.js#L1046](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L1046)  
引入版本：3.23.0


---

### resizeArrays {#resizeArrays}

#### \<instance> resizeArrays(newSize) {#instance-resizearraysnewsize}


**说明:**

调整所有内部阵列的大小 : `vertices`, `uv`, `colors` 财务报告和已审计财务报表 `alphas` 以表示新给定的绳线段的总数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| newSize | number | 否 | 将绳子分割到的段数 。 |


**返回值:** [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) - 此游戏对象实例 。


> 源码：[src/gameobjects/rope/Rope.js#L889](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L889)  
引入版本：3.23.0


---

### setAlphas {#setAlphas}

#### \<instance> setAlphas([alphas], [bottomAlpha]) {#instance-setalphasalphas-bottomalpha}


**说明:**

设定绳索在渲染过程中使用的α值 。

您可以以多种方式提供这些值:

1) 单数值: `setAlphas(0.5)` - 这将为全绳设置一个单值α. 2 两个数值: `setAlphas(1, 0.5)` - 这将为整个绳子设置一个“ 顶” 和“ 底” 的α值. 3) 一系列值: `setAlphas([ 1, 0.5, 0.2 ])`

如果您提供了一系列的值,且该数组在绳索中具有与`points`完全相同的值,它会使用每个绳片段的每个α值.

如果提供的数组的值数与 `points` 不同, 那么它会按顺序使用这些值, 从第一个绳索段到它耗尽。 这样您就可以控制绳索中所有的顶点的α值 。

注意这种方法称为`setAlphas`(plural),而不是`setAlpha`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| alphas | number \| Array.\<number> | 是 | 要么是一个单独的α值, 要么是一个数值的数组。 如果没有提供任何α值, 则重置为 1 。 |
| bottomAlpha | number | 是 | 备选底α值。 详情请参见方法描述 。 |


**返回值:** [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) - 此游戏对象实例 。


> 源码：[src/gameobjects/rope/Rope.js#L495](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L495)  
引入版本：3.23.0


---

### setColors {#setColors}

#### \<instance> setColors([colors]) {#instance-setcolorscolors}


**说明:**

设定绳索在渲染过程中使用的颜色值 。

颜色用于控制整个绳纹的锡的级别。

您可以以多种方式提供这些值:

* 单数值: `setColors(0xff0000)` - 这将为整个绳索设置一个单一的颜色色点 。

* 数组: `setColors([ 0xff0000, 0x00ff00, 0x0000ff ])`

如果您提供了一系列的数值,且该数组在绳索中具有与`points`完全相同的数值,它会使用每个绳子片段的每个颜色.

如果提供的数组的值数与 `points` 不同, 那么它会按顺序使用这些值, 从第一个绳索段到它耗尽的值。 这样您就可以控制绳索中所有顶点的颜色值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| colors | number \| Array.\<number> | 是 | 或单一的颜色值,或数组的数值。如果未提供颜色,则重置为 0xffffff 。 |


**返回值:** [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) - 此游戏对象实例 。


> 源码：[src/gameobjects/rope/Rope.js#L594](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L594)  
引入版本：3.23.0


---

### setDebug {#setDebug}

#### \<instance> setDebug([graphic], [callback]) {#instance-setdebuggraphic-callback}


**说明:**

这种方法可以将绳索顶点渲染到给定的图形实例中.

如果您启用了此功能, ** 必须** 在您的 Scene `update` 中调用 `Graphics.clear()`, 否则您提供的调试图形实例会充满绘图调用, 最终崩溃浏览器。 这样做不会自动允许您将多个 Roope 对象绘制到单个图形实例中 。

绳索类有一个内置调试渲染调试回调用 `Rope.renderDebugVerts`, 但是您也可以提供自己的调用回调来代替。 这样做时设置 `callback`参数 。

回调被引用_ 一次每次渲染_ 并发送以下参数:

`callback(src, meshLength, verts)`

`src`是正在调试的绳索实例. `meshLength`是网格顶点的总数. `verts`是翻译顶点坐标的阵列.

如果使用自己的调用, 您无需为这种方法提供图形实例 。

要禁用调试渲染, 无论是您自己的调用回调还是内置的调用, 请使用这种方法, 没有参数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| graphic | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 是 | 使用内置回调时要渲染的图形实例 。 |
| callback | function | 是 | 调试渲染时要引用的调用符。 请留下未定义的调用符 。 |


**返回值:** [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) - 此游戏对象实例 。


> 源码：[src/gameobjects/rope/Rope.js#L994](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L994)  
引入版本：3.23.0


---

### setDirty {#setDirty}

#### \<instance> setDirty() {#instance-setdirty}


**说明:**

标记此绳子为脏。 脏绳子会重新计算其下一轮的顶点数据。 如果您直接更新点数组, 您应该将绳子设为脏绳 。


**返回值:** [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) - 此游戏对象实例 。


> 源码：[src/gameobjects/rope/Rope.js#L390](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L390)  
引入版本：3.23.0


---

### setHorizontal {#setHorizontal}

#### \<instance> setHorizontal([points], [colors], [alphas]) {#instance-sethorizontalpoints-colors-alphas}


**说明:**

设置此绳索中的点对齐为水平,为条形格式。

调用此方法将重设此绳索。 当前点、 顶点、 颜色和 α 值将重置为参数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| points | number \| Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 是 | 包含此绳索的顶点数据的数组, 或表示要将纹理帧分割成多少个段的数组。 如果没有, 则使用当前点长 。 |
| colors | number \| Array.\<number> | 是 | 或单一的颜色值,或一系列的数值。 |
| alphas | number \| Array.\<number> | 是 | 或单个的alpha值,或一系列值. |


**返回值:** [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) - 此游戏对象实例 。


> 源码：[src/gameobjects/rope/Rope.js#L407](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L407)  
引入版本：3.23.0


---

### setPoints {#setPoints}

#### \<instance> setPoints([points], [colors], [alphas]) {#instance-setpointspoints-colors-alphas}


**说明:**

设置此绳索所用的点。

点应作为矢量2的数组提供,或者像矢量2的物体(即具有公用 x/y 属性的物体).

每个点对应绳子的一个段,在阵列中点数越多,绳子的段数就越多.

点坐标以局部空间给出,而非世界空间,直接与这个绳索对象使用的纹理大小有关.

例如,使用512 px宽纹理的绳索,分为4个段(每个段128px),将使用以下点: 使用一个宽纹,以表示一个宽纹,以表示一个宽纹的绳索,以表示一个宽纹,以表示一个宽纹,以表示一个宽纹,以表示一个宽纹,以表示一个宽纹,以表示一个宽纹,以表示一个宽纹,以表示一个宽纹,以表示一个宽纹,以表示一个宽纹,以表示一个宽纹,以表示宽纹,例如宽纹,用一个宽纹,分为4个段(每个段128px),使用以下点:

```javascript
rope.setPoints([
  { x: 0, y: 0 },
  { x: 128, y: 0 },
  { x: 256, y: 0 },
  { x: 384, y: 0 }
]);
```

或者,你可以提供一个整数来做同样的事情:

```javascript
rope.setPoints(4);
```

将绳子根据框架宽度分为4个等大小的片段。

注意, 使用与绳索不同的点数调用此方法, 将 _ 重置颜色和α 值, 除非您为这种方法提供这些参数 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| points | number \| Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 是 | 2 | 包含此绳索的顶点数据的数组, 或者表示要将纹理帧分割成多少个段的数组。 如果没有给出任何一个简单的四段, 则创建一个简单四段 。 |
| colors | number \| Array.\<number> | 是 |  | 或单一的颜色值,或一系列的数值。 |
| alphas | number \| Array.\<number> | 是 |  | 或单个的alpha值,或一系列值. |


**返回值:** [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) - 此游戏对象实例 。


> 源码：[src/gameobjects/rope/Rope.js#L679](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L679)  
引入版本：3.23.0


---

### setTintMode {#setTintMode}

#### \<instance> setTintMode([value]) {#instance-settintmodevalue}


**说明:**

设置将锡语应用到纹理时使用的锡字模式。

可用模式有:

- Phaser.TintModes.MULTIPLY( 默认)

- Phaser.TintModes.FILL

- Phaser.TintModes.ADD

- Phaser.TintModes.SCREEN

- Phaser.TintModes.OVERLAY

- Phaser.TintModes.HARD_LIGHT

详见`setColors`方法,说明如何给每个顶点配色.

**标签:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | [Phaser.TintModes](/api/namespace/tintmodes) | 是 | "Phaser.TintModes.MULTIPLY" | 使用锡金模式 。 |


**返回值:** [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) - 此游戏对象实例 。


> 源码：[src/gameobjects/rope/Rope.js#L465](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L465)  
引入版本：4.0.0


---

### setVertical {#setVertical}

#### \<instance> setVertical([points], [colors], [alphas]) {#instance-setverticalpoints-colors-alphas}


**说明:**

设置此绳索中的点的对齐为垂直,以列格式。

调用此方法将重设此绳索。 当前点、 顶点、 颜色和 α 值将重置为参数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| points | number \| Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 是 | 包含此绳索的顶点数据的数组, 或表示要将纹理帧分割成多少个段的数组。 如果没有, 则使用当前点长 。 |
| colors | number \| Array.\<number> | 是 | 或单一的颜色值,或一系列的数值。 |
| alphas | number \| Array.\<number> | 是 | 或单个的alpha值,或一系列值. |


**返回值:** [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) - 此游戏对象实例 。


> 源码：[src/gameobjects/rope/Rope.js#L436](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L436)  
引入版本：3.23.0


---

### updateUVs {#updateUVs}

#### \<instance> updateUVs() {#instance-updateuvs}


**说明:**

更新所有基于绳子. 点和`flipX`和`flipY`设置的UV.


**返回值:** [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) - 此游戏对象实例 。


> 源码：[src/gameobjects/rope/Rope.js#L801](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L801)  
引入版本：3.23.0


---

### updateVertices {#updateVertices}

#### \<instance> updateVertices() {#instance-updatevertices}


**说明:**

以绳点为基础更新顶点。

如果 `Rope.dirty`是 `true`, 由 `setPoints` 和 `setDirty` 方法设置, 则在渲染过程中自动使用此方法。 如果您直接修改绳点, 您应该将绳子标为脏 。


**返回值:** [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) - 此游戏对象实例 。


> 源码：[src/gameobjects/rope/Rope.js#L926](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/Rope.js#L926)  
引入版本：3.23.0


---

---
