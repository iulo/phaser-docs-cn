# DynamicBitmapText {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-dynamicbitmaptext)

BitmapText 对象通过取一个纹理文件以及描述字体结构的XML或JSON文件来工作.

在渲染过程中,每个文字字母都会被渲染到显示器,按比例间隔,并配合字体结构.

动态位图文本对象不同于静态位图文本,因为它们为在渲染传递时所给出的每个字母引用回调。这种回调允许您操纵每个正在渲染的字母的属性,如其位置,比例或锡值,允许您创建像拼接文本这样的有趣效果,而拼接文本是无法完成的。这意味着动态文本需要更多的处理时间,所以只有在您需要它们具有的回调能力时才使用它们.

比特玛普Text对象不如Text对象灵活,因为它们的特性较少,比如阴影、填充和能够使用Web字体,但您可以用这种灵活性来转换速度。您还可以通过在图像编辑器中处理字体纹理、应用填充和所需的任何其他效果来创建视觉上具有说服力的比特玛普Texts。

要创建多行文本,请在文本字符串中插入\r,\n或\rn 逃逸代码.

要创建 BitmapText 数据文件, 您需要 3 个 party app , 例如 :

BMFont(Windows,免费):[http://www.angelcode.com/products/bmfont/](http://www.angelcode.com/products/bmfont/) 格莱夫设计师(OS X,商用):[http://www.71squared.com/en/glyphdesigner](http://www.71squared.com/en/glyphdesigner) 雪BMF(基于网络,免费):[https://snowb.org/](https://snowb.org//) Littra(基于闪光,免费):[http://kvazars.com/littera/](http://kvazars.com/littera/)

对于大多数使用的案例,建议使用XML。如果您想要使用JSON,格式化应当等于通过流行的X2JS库转换一个有效的XML文件的结果。这里可以找到一个转换的在线工具:[http://codebeautify.org/xmltojson](http://codebeautify.org/xmltojson)

**构造函数**

`new DynamicBitmapText(scene, x, y, font, [text], [size], [align])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属的景点。 它只能在任何特定时间属于一个景点 。 |
| x | number | 否 |  | 世界空间中此游戏对象的x坐标 。 |
| y | number | 否 |  | 游戏对象在世界空间中的y坐标 。 |
| font | string | 否 |  | 从位图字体缓存中要使用的字体的键 。 |
| text | string \| Array.\<string> | 是 |  | 字符串,或字符串的数组,将设置为此位图文本的内容 。 |
| size | number | 是 |  | 此位图文本的字体大小 。 |
| align | number | 是 | 0 | 多行比图Text对象中的文本对齐。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext)  



> 源码：[src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L11)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext):**


 - [align](/api/class/gameobjects-bitmaptext#align)
 - [displayHeight](/api/class/gameobjects-bitmaptext#displayHeight)
 - [displayWidth](/api/class/gameobjects-bitmaptext#displayWidth)
 - [dropShadowAlpha](/api/class/gameobjects-bitmaptext#dropShadowAlpha)
 - [dropShadowColor](/api/class/gameobjects-bitmaptext#dropShadowColor)
 - [dropShadowX](/api/class/gameobjects-bitmaptext#dropShadowX)
 - [dropShadowY](/api/class/gameobjects-bitmaptext#dropShadowY)
 - [font](/api/class/gameobjects-bitmaptext#font)
 - [fontData](/api/class/gameobjects-bitmaptext#fontData)
 - [fontSize](/api/class/gameobjects-bitmaptext#fontSize)
 - [fromAtlas](/api/class/gameobjects-bitmaptext#fromAtlas)
 - [height](/api/class/gameobjects-bitmaptext#height)
 - [letterSpacing](/api/class/gameobjects-bitmaptext#letterSpacing)
 - [lineSpacing](/api/class/gameobjects-bitmaptext#lineSpacing)
 - [maxWidth](/api/class/gameobjects-bitmaptext#maxWidth)
 - [text](/api/class/gameobjects-bitmaptext#text)
 - [width](/api/class/gameobjects-bitmaptext#width)
 - [wordWrapCharCode](/api/class/gameobjects-bitmaptext#wordWrapCharCode)





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

### callbackData {#callbackData}

#### callbackData: [Phaser.Types.GameObjects.BitmapText.DisplayCallbackConfig](/api/typedef/types-gameobjects-bitmaptext#displaycallbackconfig) {#callbackdata-phasertypesgameobjectsbitmaptextdisplaycallbackconfig}


**说明:**

渲染过程中所覆盖的数据对象, 然后传递到 displayCallback 。 您应该修改此对象, 然后从调用回调中返回它。 它的更新值将用来渲染特定的格莱弗 。

请注意,如果您需要本地游戏代码中提及此对象,那么您应该浅写复制,因为它被更新并重新用于文本中的每个格莱弗.


> 源码：[src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L119)  
引入版本：3.11.0


---

### cropHeight {#cropHeight}

#### cropHeight: number {#cropheight-number}


**说明:**

位图文本的裁剪高度 。


> 源码：[src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L100)  
引入版本：3.0.0


---

### cropWidth {#cropWidth}

#### cropWidth: number {#cropwidth-number}


**说明:**

位图文本的裁剪宽度 。


> 源码：[src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L90)  
引入版本：3.0.0


---

### displayCallback {#displayCallback}

#### displayCallback: [Phaser.Types.GameObjects.BitmapText.DisplayCallback](/api/typedef/types-gameobjects-bitmaptext#displaycallback) {#displaycallback-phasertypesgameobjectsbitmaptextdisplaycallback}


**说明:**

一个改变位图文本每个字符的渲染方式的回调 。


> 源码：[src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L110](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L110)  
引入版本：3.0.0


---

### scrollX {#scrollX}

#### scrollX: number {#scrollx-number}


**说明:**

位图文本的横向滚动位置 。


> 源码：[src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L70)  
引入版本：3.0.0


---

### scrollY {#scrollY}

#### scrollY: number {#scrolly-number}


**说明:**

位图文本的垂直滚动位置 。


> 源码：[src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L80)  
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





**From [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext):**


 - [getCharacterAt](/api/class/gameobjects-bitmaptext#getCharacterAt)
 - [getTextBounds](/api/class/gameobjects-bitmaptext#getTextBounds)
 - [preDestroy](/api/class/gameobjects-bitmaptext#preDestroy)
 - [setCenterAlign](/api/class/gameobjects-bitmaptext#setCenterAlign)
 - [setCharacterTint](/api/class/gameobjects-bitmaptext#setCharacterTint)
 - [setDisplaySize](/api/class/gameobjects-bitmaptext#setDisplaySize)
 - [setDropShadow](/api/class/gameobjects-bitmaptext#setDropShadow)
 - [setFont](/api/class/gameobjects-bitmaptext#setFont)
 - [setFontSize](/api/class/gameobjects-bitmaptext#setFontSize)
 - [setLeftAlign](/api/class/gameobjects-bitmaptext#setLeftAlign)
 - [setLetterSpacing](/api/class/gameobjects-bitmaptext#setLetterSpacing)
 - [setLineSpacing](/api/class/gameobjects-bitmaptext#setLineSpacing)
 - [setMaxWidth](/api/class/gameobjects-bitmaptext#setMaxWidth)
 - [setRightAlign](/api/class/gameobjects-bitmaptext#setRightAlign)
 - [setText](/api/class/gameobjects-bitmaptext#setText)
 - [setWordTint](/api/class/gameobjects-bitmaptext#setWordTint)
 - [toJSON](/api/class/gameobjects-bitmaptext#toJSON)
 - [updateDisplayOrigin](/api/class/gameobjects-bitmaptext#updateDisplayOrigin)





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


 - [setFrame](/api/namespace/gameobjects-components-texture#setFrame)
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

### setDisplayCallback {#setDisplayCallback}

#### \<instance> setDisplayCallback(callback) {#instance-setdisplaycallbackcallback}


**说明:**

设置一个调用, 更改比图文本的每个字符的渲染方式 。

回调接收到一个[Phaser.Types.GameObjects.BitmapText.DisplayCallbackConfig](/api/typedef/types-gameobjects-bitmaptext#displaycallbackconfig)对象,该对象包含即将渲染的字符信息.

它应该返回一个具有`x`、`y`、`scale`和`rotation`等特性的物体,这些特性将在渲染时使用,而不是通常的值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | [Phaser.Types.GameObjects.BitmapText.DisplayCallback](/api/typedef/types-gameobjects-bitmaptext#displaycallback) | 否 | 显示回调设置 。 |


**返回值:** [Phaser.GameObjects.DynamicBitmapText](/api/class/gameobjects-dynamicbitmaptext) - 此游戏对象 。


> 源码：[src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L169)  
引入版本：3.0.0


---

### setScrollX {#setScrollX}

#### \<instance> setScrollX(value) {#instance-setscrollxvalue}


**说明:**

设置此位图文本的横向滚动位置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 要设置的横向滚动位置 。 |


**返回值:** [Phaser.GameObjects.DynamicBitmapText](/api/class/gameobjects-dynamicbitmaptext) - 此游戏对象 。


> 源码：[src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L192)  
引入版本：3.0.0


---

### setScrollY {#setScrollY}

#### \<instance> setScrollY(value) {#instance-setscrollyvalue}


**说明:**

设置此位图文本的垂直滚动位置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 要设置的垂直滚动位置 。 |


**返回值:** [Phaser.GameObjects.DynamicBitmapText](/api/class/gameobjects-dynamicbitmaptext) - 此游戏对象 。


> 源码：[src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L209](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L209)  
引入版本：3.0.0


---

### setSize {#setSize}

#### \<instance> setSize(width, height) {#instance-setsizewidth-height}


**说明:**

设定此位图文本的裁剪大小 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 作物的宽度. |
| height | number | 否 | 作物的高度。 |


**返回值:** [Phaser.GameObjects.DynamicBitmapText](/api/class/gameobjects-dynamicbitmaptext) - 此游戏对象 。


> 源码：[src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/dynamic/DynamicBitmapText.js#L150)  
引入版本：3.0.0


---

---
