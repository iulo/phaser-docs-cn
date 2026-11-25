# Text {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-text)

文字游戏对象。

文本对象通过创建自己的内部隐藏的 Canvas 来工作, 然后使用标准的 Canvas `fillText`Z API 来制作文本。 然后从这个画布中创建一个纹理, 在渲染传阅时将它交给您的游戏 。

因为它使用 Canvas API 您可以利用所有这些要约的特性, 比如在文本中应用渐变填充, 或者用中键、 阴影等。 您也可以使用外部加载的自定义字体, 如 Google 或 TypeKit Web 字体 。

**Important:** 如果字体名称包含某些数字或特殊字符组合,在创建文本对象时,或通过`setFont`或`setFontFamily`设置字体时,必须引用该字体名称,例如:

```javascript
this.add.text(0, 0, 'Hello World', { fontFamily: 'Georgia, "Goudy Bookletter 1911", Times, serif' });
```

```javascript
this.add.text(0, 0, 'Hello World', { font: '"Press Start 2P"' });
```

您只能显示当前已装入且可供浏览器使用的字体: 因此字体必须预先装入. Phaser不会为您这样做, 因此您需要使用第3方字体加载器, 或者在您 Phaser游戏所居住的页面上有 CSS 中随时可用的字体 。

移动浏览器中可用的默认字体,请参见 [this](http://www.jordanm.co.uk/tinytype).

性能说明: 每次文本对象的内容发生变化, 即更改显示的文本或文本样式, 它需要重新制作文本画布, 如果在 WebGL 上, 则将新纹理重新加载到 GPU 。 如果经常使用, 或者在游戏中有大量文本对象, 这将是一个昂贵的操作。 如果您遇到性能问题, 您最好使用 Bitmap Text , 因为它从批量中获利, 避免了昂贵的 Canvas API 调用 。

**构造函数**

`new Text(scene, x, y, text, style)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| text | string \| Array.\<string> | 否 | 此文本对象将显示的文本 。 |
| style | [Phaser.Types.GameObjects.Text.TextStyle](/api/typedef/types-gameobjects-text#textstyle) | 否 | 文本样式配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize)  
> [Phaser.GameObjects.Components.Crop](/api/namespace/gameobjects-components-crop)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip)  
> [Phaser.GameObjects.Components.GetBounds](/api/namespace/gameobjects-components-getbounds)  
> [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask)  
> [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin)  
> [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  
> [Phaser.GameObjects.Components.Tint](/api/namespace/gameobjects-components-tint)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/text/Text.js#L20](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L20)  
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





**From [Phaser.GameObjects.Components.Crop](/api/namespace/gameobjects-components-crop):**


 - [frame](/api/namespace/gameobjects-components-crop#frame)
 - [isCropped](/api/namespace/gameobjects-components-crop#isCropped)
 - [texture](/api/namespace/gameobjects-components-crop#texture)





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

### autoRound {#autoRound}

#### autoRound: boolean {#autoround-boolean}


**说明:**

是否自动绕行位置 。


> 源码：[src/gameobjects/text/Text.js#L160](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L160)  
引入版本：3.0.0


---

### canvas {#canvas}

#### canvas: HTMLCanvasElement {#canvas-htmlcanvaselement}


**说明:**

文本要向哪个画布元素 。


> 源码：[src/gameobjects/text/Text.js#L131](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L131)  
引入版本：3.0.0


---

### context {#context}

#### context: CanvasRenderingContext2D {#context-canvasrenderingcontext2d}


**说明:**

文本的画布元素的背景。


> 源码：[src/gameobjects/text/Text.js#L140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L140)  
引入版本：3.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

此文本对象的高度 。


**Overrides:** Phaser.GameObjects.Components.ComputedSize高音声


> 源码：[src/gameobjects/text/Text.js#L211](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L211)  
引入版本：3.0.0


---

### letterSpacing {#letterSpacing}

#### letterSpacing: number {#letterspacing-number}


**说明:**

添加 / 删除字符之间的间隔。 可以是负数或正数 。

如果您直接更新此属性, 而不是使用 `setLetterSpacing` 方法, 请在之后拨打 `updateText` , 否则您不会看到文本对象中反映的更改 。


> 源码：[src/gameobjects/text/Text.js#L235](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L235)  
引入版本：3.60.0


---

### lineSpacing {#lineSpacing}

#### lineSpacing: number {#linespacing-number}


**说明:**

线段间距值。该值将添加到字体高度中,以计算整条线段高度。只有在此文本对象包含多行文字时才有效果。

如果您直接更新此属性, 而不是使用 `setLineSpacing` 方法, 请在之后拨打 `updateText` , 否则您不会看到文本对象中反映的更改 。


> 源码：[src/gameobjects/text/Text.js#L221](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L221)  
引入版本：3.13.0


---

### padding {#padding}

#### padding: [Phaser.Types.GameObjects.Text.TextPadding](/api/typedef/types-gameobjects-text#textpadding) {#padding-phasertypesgameobjectstexttextpadding}


**说明:**

指定在计算文本大小时添加到行宽和高度的粘贴值。如果浏览器无法准确确定字体的真伪尺寸,则允许您添加额外间隔。


> 源码：[src/gameobjects/text/Text.js#L191](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L191)  
引入版本：3.0.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer), [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrenderercanvascanvasrenderer-phaserrendererwebglwebglrenderer}


**说明:**

本文本对象正在使用的渲染器。


> 源码：[src/gameobjects/text/Text.js#L118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L118)  
引入版本：3.12.0


---

### splitRegExp {#splitRegExp}

#### splitRegExp: object {#splitregexp-object}


**说明:**

用于将文本分解成行的正则表达式, 以多行文字形式。 默认这是 `/(?:\r\n|\r|\n)/`。 您可以修改此 RegExp 以成为您可能需要的其它任何内容 。


> 源码：[src/gameobjects/text/Text.js#L170](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L170)  
引入版本：3.0.0


---

### style {#style}

#### style: [Phaser.GameObjects.TextStyle](/api/class/gameobjects-textstyle) {#style-phasergameobjectstextstyle}


**说明:**

文本样式对象。

管理此文本对象的样式。


> 源码：[src/gameobjects/text/Text.js#L149](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L149)  
引入版本：3.0.0


---

### text {#text}

#### text: string {#text-string}


**说明:**

此文本游戏对象正在提供文本字符串 。


> 源码：[src/gameobjects/text/Text.js#L1518](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L1518)  
引入版本：3.0.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

此文本对象的宽度 。


**Overrides:** Phaser.GameObjects.Components.ComputedSize# 摇摆 #


> 源码：[src/gameobjects/text/Text.js#L201](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L201)  
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





**From [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize):**


 - [setDisplaySize](/api/namespace/gameobjects-components-computedsize#setDisplaySize)
 - [setSize](/api/namespace/gameobjects-components-computedsize#setSize)





**From [Phaser.GameObjects.Components.Crop](/api/namespace/gameobjects-components-crop):**


 - [setCrop](/api/namespace/gameobjects-components-crop#setCrop)





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
 - [update](/api/class/gameobjects-gameobject#update)
 - [willRender](/api/class/gameobjects-gameobject#willRender)
 - [willRoundVertices](/api/class/gameobjects-gameobject#willRoundVertices)




---

## 公开方法 {#public-methods}

### advancedWordWrap {#advancedWordWrap}

#### \<instance> advancedWordWrap(text, context, wordWrapWidth) {#instance-advancedwordwraptext-context-wordwrapwidth}


**说明:**

高级的包线算法, 它将随着线条的线长超过其水平界限而包线。 连续的空格会崩溃, 并替换为单个空格。 处理前会将线条修剪为白色空格。 如果 wordWrapWidth 的字符小于单个, 则丢出一个错误 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| text | string | 否 | 文字来进行文字包装检测。 |
| context | CanvasRenderingContext2D | 否 | 坎瓦斯渲染背景. |
| wordWrapWidth | number | 否 | 字包宽度. |


**返回值:** string - 包裹的文字。


> 源码：[src/gameobjects/text/Text.js#L410](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L410)  
引入版本：3.0.0


---

### appendText {#appendText}

#### \<instance> appendText(value, [addCR]) {#instance-appendtextvalue-addcr}


**说明:**

将给定的文本附加到此文本对象已经显示的内容中。

将用 `\n` 换行符加入一系列字符串 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | string \| Array.\<string> | 否 |  | 字符串,或字符串数组,将附加在本文本对象的现有内容上。 |
| addCR | boolean | 是 | true | 在字符串值前插入车厢返回 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L661](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L661)  
引入版本：3.60.0


---

### basicWordWrap {#basicWordWrap}

#### \<instance> basicWordWrap(text, context, wordWrapWidth) {#instance-basicwordwraptext-context-wordwrapwidth}


**说明:**

贪婪的包扎算法, 它将随着线条的长于其水平界限而包扎文字。 空间不会崩溃, 白空间不会被剪切 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| text | string | 否 | 文字来进行文字包装检测。 |
| context | CanvasRenderingContext2D | 否 | 坎瓦斯渲染背景. |
| wordWrapWidth | number | 否 | 字包宽度. |


**返回值:** string - 包裹的文字。


> 源码：[src/gameobjects/text/Text.js#L534](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L534)  
引入版本：3.0.0


---

### getTextMetrics {#getTextMetrics}

#### \<instance> getTextMetrics() {#instance-gettextmetrics}


**说明:**

获取当前文本的参数 。


**返回值:** [Phaser.Types.GameObjects.Text.TextMetrics](/api/typedef/types-gameobjects-text#textmetrics) - 文字的度量衡.


> 源码：[src/gameobjects/text/Text.js#L1505](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L1505)  
引入版本：3.0.0


---

### getWrappedText {#getWrappedText}

#### \<instance> getWrappedText([text]) {#instance-getwrappedtexttext}


**说明:**

通过此文本对象将给定的文本运行,并将结果作为数组返回,其中数组的每个元素对应一个被包的文本行。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| text | string | 是 | 将计算包线的文字。如果未说明,则文字会显示当前文字。 |


**返回值:** Array.\<string> - 带包裹文本的字符串阵列。


> 源码：[src/gameobjects/text/Text.js#L605](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L605)  
引入版本：3.0.0


---

### initRTL {#initRTL}

#### \<instance> initRTL() {#instance-initrtl}


**说明:**

初始化右侧到左侧文本 。


> 源码：[src/gameobjects/text/Text.js#L331](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L331)  
引入版本：3.0.0


---

### preDestroy {#preDestroy}

#### \<instance> preDestroy() {#instance-predestroy}


**说明:**

内部破坏处理器,作为破坏过程的一部分而叫作.


**Access:** 保护


> 源码：[src/gameobjects/text/Text.js#L1570](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L1570)  
引入版本：3.0.0


---

### runWordWrap {#runWordWrap}

#### \<instance> runWordWrap(text) {#instance-runwordwraptext}


**说明:**

将文字包装到给定的文字,然后返回结果。如果设置了自定义的文字包装回调,则将引用。否则,将根据样式配置使用高级或基本文字包装算法。如果没有文字包装设置活动,则原文字返回时不变。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| text | string | 否 | 文字来进行文字包装检测。 |


**返回值:** string - 已应用了包扎后的文字。


> 源码：[src/gameobjects/text/Text.js#L365](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L365)  
引入版本：3.0.0


---

### setAlign {#setAlign}

#### \<instance> setAlign([align]) {#instance-setalignalign}


**说明:**

设置此文本对象中文本的对齐 。

论点可以是: `left`, `right`, `center` 或 或 时 间 `justify`.

只有当文本对象有不止一行文字时,对齐才有效。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| align | string | 是 | "'left'" | 多行文本的文本对齐。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L1040](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L1040)  
引入版本：3.0.0


---

### setBackgroundColor {#setBackgroundColor}

#### \<instance> setBackgroundColor(color) {#instance-setbackgroundcolorcolor}


**说明:**

设置背景颜色 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | string | 否 | 后色相为. |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L841](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L841)  
引入版本：3.0.0


---

### setColor {#setColor}

#### \<instance> setColor(color) {#instance-setcolorcolor}


**说明:**

设置文本填充颜色。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | string \| CanvasGradient | CanvasPattern | 否 | 文字充色. |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L876](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L876)  
引入版本：3.0.0


---

### setFill {#setFill}

#### \<instance> setFill(color) {#instance-setfillcolor}


**说明:**

设置文本对象使用的填充样式。

这可以是任何有效的 CanvasRendering Context2D fillStyle 值,例如一个颜色(在六进制,rgb,rgba,hsl或命名值),一个梯度或模式.

详见[MDN fillStyle docs](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/fillStyle).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | string \| CanvasGradient | CanvasPattern | 否 | 文本填充样式。 可以是任何有效的 CanvasRendering Context `fillStyle` 值 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L856](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L856)  
引入版本：3.0.0


---

### setFixedSize {#setFixedSize}

#### \<instance> setFixedSize(width, height) {#instance-setfixedsizewidth-height}


**说明:**

设置文本的固定宽度和高度 。

在`0`中通过其中任一参数分别禁用固定宽度或高度.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 要设置的固定宽度。 `0` 禁用固定宽度 。 |
| height | number | 否 | 固定高度设定。 `0` 禁用固定高度 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L823](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L823)  
引入版本：3.0.0


---

### setFont {#setFont}

#### \<instance> setFont(font) {#instance-setfontfont}


**说明:**

设置字体 。

如果给出了字符串,则设置了字体家族.

如果给出了某个物体,则设定该物体的`fontFamily`,`fontSize`和`fontStyle`属性.

**Important:** 如果字体名称包含某些数字或特殊字符组合,则必须引用:

```javascript
Text.setFont('"Press Start 2P"');
```

同样,如果您想提供倒置字体列表,您应该确保它们都被正确引用:

```javascript
Text.setFont('Georgia, "Goudy Bookletter 1911", Times, serif');
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| font | string | 否 | 要设置的字体家族或字体设置 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L726](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L726)  
引入版本：3.0.0


---

### setFontFamily {#setFontFamily}

#### \<instance> setFontFamily(family) {#instance-setfontfamilyfamily}


**说明:**

设置字体家族 。

**Important:** 如果字体名称包含某些数字或特殊字符组合,则必须引用:

```javascript
Text.setFontFamily('"Press Start 2P"');
```

同样,如果您想提供倒置字体列表,您应该确保它们都被正确引用:

```javascript
Text.setFontFamily('Georgia, "Goudy Bookletter 1911", Times, serif');
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| family | string | 否 | 字体家族. |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L762](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L762)  
引入版本：3.0.0


---

### setFontSize {#setFontSize}

#### \<instance> setFontSize(size) {#instance-setfontsizesize}


**说明:**

设置字体大小。 可以是带有效 CSS 单元的字符串, 即 `16px`, 或数字 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| size | string \| number | 否 | 字体大小 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L793](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L793)  
引入版本：3.0.0


---

### setFontStyle {#setFontStyle}

#### \<instance> setFontStyle(style) {#instance-setfontstylestyle}


**说明:**

设置字体样式。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| style | string | 否 | 字体样式。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L808](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L808)  
引入版本：3.0.0


---

### setLetterSpacing {#setLetterSpacing}

#### \<instance> setLetterSpacing(value) {#instance-setletterspacingvalue}


**说明:**

设置字母间隔值。

这将添加, 或删除此文本游戏对象每个字符之间的间隔。 数值可以是正的, 也可以是负的。 正面值会增加每个字符之间的间隔, 而负值会减少间隔。 请注意, 有些字体的间隔会比其他字体更接近 。

请理解启用此功能会导致 Phaser 使文本对象中每个字符逐个生成, 而不是对整个字符串使用一个绘图。 使用长字符串或全部字符串时, 费用会非常昂贵。 如果您需要显示大量对字母间隔有精细控制的字符, 则创建位图字体文本会更好 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 添加到字母宽度的金额。 设置为零以禁用 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L1099](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L1099)  
引入版本：3.70.0


---

### setLineSpacing {#setLineSpacing}

#### \<instance> setLineSpacing(value) {#instance-setlinespacingvalue}


**说明:**

设置行距值。

此值在计算整行高度时为 _ 添加_ 到字体高度。 只有当此文本对象包含多行文本时, 才会有效果 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 增加字体高度的金额,以实现整体线高. |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L1079](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L1079)  
引入版本：3.13.0


---

### setMaxLines {#setMaxLines}

#### \<instance> setMaxLines([max]) {#instance-setmaxlinesmax}


**说明:**

设置要绘制的最大行数 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| max | number | 是 | 0 | 绘制的最大行数 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L1192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L1192)  
引入版本：3.0.0


---

### setPadding {#setPadding}

#### \<instance> setPadding(left, [top], [right], [bottom]) {#instance-setpaddingleft-top-right-bottom}


**说明:**

设置在计算画布大小时围绕文本内容应用的粘贴符。

第一个参数可以是数字或编目配置对象。当给出数字时,它会适用于所有四边,除非其他参数压倒它们。当给出对象时,您可以指定 `left`, `right`, `top`,和 `bottom` 单独使用或使用 `x` 将左右同时设置,以及 `y` 设置上下两个位置。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| left | number \| [Phaser.Types.GameObjects.Text.TextPadding](/api/typedef/types-gameobjects-text#textpadding) | 否 | 左侧的粘贴值, 或粘贴配置对象 。 |
| top | number | 是 | 顶部的垫装值 。 |
| right | number | 是 | 右侧的贴纸值 。 |
| bottom | number | 是 | 底部的粘贴值 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L1125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L1125)  
引入版本：3.0.0


---

### setResolution {#setResolution}

#### \<instance> setResolution(value) {#instance-setresolutionvalue}


**说明:**

设置此文本对象所使用的纹理分辨率 。

设置高于 1 的分辨率只有在您正在放大此文本对象( 或祖先) 或放大其上的相机时才有用。 否则, 质素中的任何额外细节都会在渲染过程中丢失 。

请小心使用,因为你拥有的越高分辨率文本,它使用的记忆就越多.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 本文本的分辨率是反对使用的, 相对于 1 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L1059](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L1059)  
引入版本：3.12.0


---

### setRTL {#setRTL}

#### \<instance> setRTL([rtl]) {#instance-setrtlrtl}


**说明:**

右对左或左对右的文本 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| rtl | boolean | 是 | true | 设定为 `true` 从右到左进行渲染. |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L1207](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L1207)  
引入版本：3.70.0


---

### setShadow {#setShadow}

#### \<instance> setShadow([x], [y], [color], [blur], [shadowStroke], [shadowFill]) {#instance-setshadowx-y-color-blur-shadowstroke-shadowfill}


**说明:**

设置阴影设置 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 横向阴影抵消。 |
| y | number | 是 | 0 | 垂直阴影抵消。 |
| color | string | 是 | "'#000'" | 阴色. |
| blur | number | 是 | 0 | 阴影模糊半径。 |
| shadowStroke | boolean | 是 | false | 是否要打中阴影. |
| shadowFill | boolean | 是 | true | 是否填满阴影. |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L907](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L907)  
引入版本：3.0.0


---

### setShadowBlur {#setShadowBlur}

#### \<instance> setShadowBlur(blur) {#instance-setshadowblurblur}


**说明:**

设定阴影模糊半径 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| blur | number | 否 | 阴影模糊半径。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L958](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L958)  
引入版本：3.0.0


---

### setShadowColor {#setShadowColor}

#### \<instance> setShadowColor(color) {#instance-setshadowcolorcolor}


**说明:**

设影色.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | string | 否 | 阴色. |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L943](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L943)  
引入版本：3.0.0


---

### setShadowFill {#setShadowFill}

#### \<instance> setShadowFill(enabled) {#instance-setshadowfillenabled}


**说明:**

启用或禁用阴影填充 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| enabled | boolean | 否 | 是否启用阴影填充 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L988](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L988)  
引入版本：3.0.0


---

### setShadowOffset {#setShadowOffset}

#### \<instance> setShadowOffset(x, y) {#instance-setshadowoffsetx-y}


**说明:**

设阴偏.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 横向阴影抵消。 |
| y | number | 否 | 垂直阴影抵消。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L927](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L927)  
引入版本：3.0.0


---

### setShadowStroke {#setShadowStroke}

#### \<instance> setShadowStroke(enabled) {#instance-setshadowstrokeenabled}


**说明:**

启用或禁用阴影中风 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| enabled | boolean | 否 | 是否启用阴影中风 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L973](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L973)  
引入版本：3.0.0


---

### setStroke {#setStroke}

#### \<instance> setStroke(color, thickness) {#instance-setstrokecolor-thickness}


**说明:**

设置中风设置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | string \| CanvasGradient | CanvasPattern | 否 | 中风颜色. |
| thickness | number | 否 | 中风厚度。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L891](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L891)  
引入版本：3.0.0


---

### setStyle {#setStyle}

#### \<instance> setStyle(style) {#instance-setstylestyle}


**说明:**

设置文本样式。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| style | object | 否 | 要设置的样式设置 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L702](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L702)  
引入版本：3.0.0


---

### setText {#setText}

#### \<instance> setText(value) {#instance-settextvalue}


**说明:**

设定要显示的文本 。

将用 `\n` 换行符加入一系列字符串 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | string \| Array.\<string> | 否 | 字符串,或字符串数组,将设定为本文本对象的内容。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L627](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L627)  
引入版本：3.0.0


---

### setWordWrapCallback {#setWordWrapCallback}

#### \<instance> setWordWrapCallback(callback, [scope]) {#instance-setwordwrapcallbackcallback-scope}


**说明:**

设置一个自定义的回调线条来包装。 以回调方式删除回调线条是无效的 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| callback | TextStyleWordWrapCallback | 否 |  | 用于包装文本的自定义函数。 它将收到两个参数: 文本( 要包装的字符串) , textObject( 此文本实例) 。 它应该将包装的行作为数组或带有新行字符的字符串返回, 以指示中断点的发生地点 。 |
| scope | object | 是 | null | 引用回调时将适用的范围 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L1021](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L1021)  
引入版本：3.0.0


---

### setWordWrapWidth {#setWordWrapWidth}

#### \<instance> setWordWrapWidth(width, [useAdvancedWrap]) {#instance-setwordwrapwidthwidth-useadvancedwrap}


**说明:**

设置用于包线的宽度( 像素) 。 将空格带入以宽度删除 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number \| null | 否 |  | 线条的最大宽度, 以像素表示。 设置为无法删除包线 。 |
| useAdvancedWrap | boolean | 是 | false | 是否使用高级的包线算法。 如果为真, 空格会崩溃, 空格会从线条中剪切。 如果错误, 空格和空格会照原样保留 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L1003](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L1003)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

构建文本对象的 JSON 表示式。


**Overrides:** Phaser.GameObjects.GameObject#toJSON


**返回值:** [Phaser.Types.GameObjects.JSONGameObject](/api/typedef/types-gameobjects#jsongameobject) - 文本对象的 JSON 表示式。


> 源码：[src/gameobjects/text/Text.js#L1539](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L1539)  
引入版本：3.0.0


---

### updateText {#updateText}

#### \<instance> updateText() {#instance-updatetext}


**说明:**

重新计算文本内容并将其重新交给内部画布。 当文本字符串或任何样式属性发生变化时, 都会自动调用。 它处理文字包、 文本缩放、 多行布局、 校正、 阴影、 中风和字母间隔。 如果渲染器是 WebGL, 更新后的画布会被重新加载到 GPU 中, 则它会作为一个新的纹理。 您只有在没有使用相应的设置方法直接更新 `lineSpacing`Z 或 `letterSpacing` 时, 才会手动调用此功能 。


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 此文本对象 。


> 源码：[src/gameobjects/text/Text.js#L1256](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/Text.js#L1256)  
引入版本：3.0.0


---

---
