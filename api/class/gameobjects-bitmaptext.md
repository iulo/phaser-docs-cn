# BitmapText {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-bitmaptext)

BitmapText 对象通过取一个纹理文件以及描述字体结构的XML或JSON文件来工作.

在为文本的每个字母渲染时,会向显示器提供正对的间隔,并配合字体结构。

比特玛普Text对象不如Text对象灵活,因为它们的特性较少,比如阴影、填充和能够使用Web字体,但您可以用这种灵活性来转换速度。您还可以通过在图像编辑器中处理字体纹理、应用填充和所需的任何其他效果来创建视觉上具有说服力的比特玛普Texts。

要创建多行文本,请在文本字符串中插入\r,\n或\rn 逃逸代码.

要创建 BitmapText 数据文件, 您需要 3 个 party app , 例如 :

BMFont(Windows,免费):[http://www.angelcode.com/products/bmfont/](http://www.angelcode.com/products/bmfont/) 格莱夫设计师(OS X,商用):[http://www.71squared.com/en/glyphdesigner](http://www.71squared.com/en/glyphdesigner) 雪BMF(基于网络,免费):[https://snowb.org/](https://snowb.org//) Littra(基于闪光,免费):[http://kvazars.com/littera/](http://kvazars.com/littera/)

对于大多数使用的案例,建议使用XML。如果您想要使用JSON,格式化应当等于通过流行的X2JS库转换一个有效的XML文件的结果。这里可以找到一个转换的在线工具:[http://codebeautify.org/xmltojson](http://codebeautify.org/xmltojson)

**构造函数**

`new BitmapText(scene, x, y, font, [text], [size], [align])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属的景点。 它只能在任何特定时间属于一个景点 。 |
| x | number | 否 |  | 世界空间中此游戏对象的x坐标 。 |
| y | number | 否 |  | 游戏对象在世界空间中的y坐标 。 |
| font | string | 否 |  | 从位图字体缓存中要使用的字体的密钥 。 |
| text | string \| Array.\<string> | 是 |  | 字符串,或字符串的数组,将设置为此位图文本的内容 。 |
| size | number | 是 |  | 此位图文本的字体大小 。 |
| align | number | 是 | 0 | 多行比图Text对象中的文本对齐。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
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



> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L19)  
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

### align {#align}

#### align: number {#align-number}


**说明:**

控制此位图图文集对象中每行文字的对齐。

只有在此 BitmapText 包含多行文本, 并用马车返回来分割时才有效果。 仅此文本的单行无效 。

参见方法`setLeftAlign`,`setCenterAlign`和`setRightAlign`.

0=左对齐(默认) 1=中对齐 2=右对齐

校对位置基于最长的文本行.


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L915](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L915)  
引入版本：3.11.0


---

### ALIGN_CENTER {#ALIGN_CENTER}

#### ALIGN_CENTER: number {#align_center-number}


**说明:**

中心对齐多行比图Text对象中的文本字符。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1235](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1235)  
引入版本：3.11.0


---

### ALIGN_LEFT {#ALIGN_LEFT}

#### ALIGN_LEFT: number {#align_left-number}


**说明:**

左侧对齐多行比图Text对象中的文本字符。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1226](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1226)  
引入版本：3.11.0


---

### ALIGN_RIGHT {#ALIGN_RIGHT}

#### ALIGN_RIGHT: number {#align_right-number}


**说明:**

右对齐多行比图Text对象中的文本字符。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1244](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1244)  
引入版本：3.11.0


---

### displayHeight {#displayHeight}

#### displayHeight: number {#displayheight-number}


**说明:**

此位图文本的显示高度 。

这一数值考虑到了比额表系数。

此属性只读 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1150)  
引入版本：3.60.0


---

### displayWidth {#displayWidth}

#### displayWidth: number {#displaywidth-number}


**说明:**

此位图文本的显示宽度 。

这一数值考虑到了比额表系数。

此属性只读 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1118)  
引入版本：3.60.0


---

### dropShadowAlpha {#dropShadowAlpha}

#### dropShadowAlpha: number {#dropshadowalpha-number}


**说明:**

滴影的α值.

你可以直接设置,或者使用`Phaser.GameObjects.BitmapText#setDropShadow`.


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L275](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L275)  
引入版本：3.50.0


---

### dropShadowColor {#dropShadowColor}

#### dropShadowColor: number {#dropshadowcolor-number}


**说明:**

投影之色.

你可以直接设置,或者使用`Phaser.GameObjects.BitmapText#setDropShadow`.


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L264](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L264)  
引入版本：3.50.0


---

### dropShadowX {#dropShadowX}

#### dropShadowX: number {#dropshadowx-number}


**说明:**

下降阴影的横向偏移。

你可以直接设置,或者使用`Phaser.GameObjects.BitmapText#setDropShadow`.


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L242](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L242)  
引入版本：3.50.0


---

### dropShadowY {#dropShadowY}

#### dropShadowY: number {#dropshadowy-number}


**说明:**

倒影的垂直偏移

你可以直接设置,或者使用`Phaser.GameObjects.BitmapText#setDropShadow`.


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L253](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L253)  
引入版本：3.50.0


---

### font {#font}

#### font: string {#font-string}


**说明:**

此位图文本所使用的位图字体的密钥。 要在创建后更改字体, 请使用 `setFont` 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L100)  
引入版本：3.0.0


---

### fontData {#fontData}

#### fontData: [Phaser.Types.GameObjects.BitmapText.BitmapFontData](/api/typedef/types-gameobjects-bitmaptext#bitmapfontdata) {#fontdata-phasertypesgameobjectsbitmaptextbitmapfontdata}


**说明:**

此位图文本所用的位图字体数据 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L118)  
引入版本：3.0.0


---

### fontSize {#fontSize}

#### fontSize: number {#fontsize-number}


**说明:**

此位图文本的字体大小 。

如果您想要一个可链路的改变字体大小的方法,也可以使用`setFontSize`的方法.


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L971](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L971)  
引入版本：3.0.0


---

### fromAtlas {#fromAtlas}

#### fromAtlas: boolean {#fromatlas-boolean}


**说明:**

表示字体纹理是否来自地图集。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L286](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L286)  
引入版本：3.54.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

此位图文本的高度 。

此属性只读 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1097](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1097)  
引入版本：3.0.0


---

### letterSpacing {#letterSpacing}

#### letterSpacing: number {#letterspacing-number}


**说明:**

添加/ 删除字符之间的间隔。

可以是负数或正数.

如果要用可链路改变字母间隔,也可以使用`setLetterSpacing`方法.


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L995](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L995)  
引入版本：3.0.0


---

### lineSpacing {#lineSpacing}

#### lineSpacing: number {#linespacing-number}


**说明:**

添加/ 删除行间距。

可以是负数或正数.

如果您想要一个可链路方式来改变行距,也可以使用`setLineSpacing`方法.


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1021](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1021)  
引入版本：3.60.0


---

### maxWidth {#maxWidth}

#### maxWidth: number {#maxwidth-number}


**说明:**

此位图Text 的最大显示宽度, 以像素表示 。

如果 BitmapText.text 长于 maxWidth,那么这些行会自动地根据该行中找到的最后一个白空字符包裹.

如果没有找到白空间,则不会进行包装,因此不会遵守maxWidth值。

通过设置值为 0 来禁用 maxWidth 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1047](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1047)  
引入版本：3.21.0


---

### text {#text}

#### text: string {#text-string}


**说明:**

此位图文本对象显示的文本 。

如果您想要一个可链路方式来改变文本内容,也可以使用`setText`的方法.


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L948](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L948)  
引入版本：3.0.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

此位图文本的宽度 。

此属性只读 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1076](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1076)  
引入版本：3.0.0


---

### wordWrapCharCode {#wordWrapCharCode}

#### wordWrapCharCode: number {#wordwrapcharcode-number}


**说明:**

用于检测文字包的字符代码。 默认为32( 一个空格字符) 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L222](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L222)  
引入版本：3.21.0


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

### getCharacterAt {#getCharacterAt}

#### \<instance> getCharacterAt(x, y, [camera]) {#instance-getcharacteratx-y-camera}


**说明:**

获取此位图文本中给定的 x/y 坐标中的字符 。

您所传递的坐标被翻译为比图文本的本地空间, 然而,首先要由您将输入坐标翻译为世界空间。

如果您想结合输入事件使用, 请务必通过 `Pointer.worldX` 和 `worldY` , 从而它们处于世界空间 。

在某些情况下,基于kerning,字符可以重叠。当发生这种情况时,词中的第一个字符会被返回.

注意, 如果您在渲染过程中更改了字符位置, 这对于动态比特玛普文本无效 。 它只会扫描未翻译的字符状态 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 检查的 X 位置 。 |
| y | number | 否 | 检查位置 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 正在测试的相机。 如果不给它, 将会使用场景默认相机 。 |


**返回值:** [Phaser.Types.GameObjects.BitmapText.BitmapTextCharacter](/api/typedef/types-gameobjects-bitmaptext#bitmaptextcharacter) - 指定位置的字符对象,或`null`.


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L748](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L748)  
引入版本：3.50.0


---

### getTextBounds {#getTextBounds}

#### \<instance> getTextBounds([round]) {#instance-gettextboundsround}


**说明:**

计算此位图文本的界限 。

返回一个包含本地和全局背景中的位图文本的位置、宽度和高度的对象。

本地大小仅基于字体大小和一个[0,0]位置.

全球大小考虑到游戏对象的规模,世界位置和显示来源.

对象中还有关于每行长度的数据,如果是多行比特玛普Text。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| round | boolean | 是 | false | 是否将结果整数整数到最近的整数 。 |


**返回值:** [Phaser.Types.GameObjects.BitmapText.BitmapTextSize](/api/typedef/types-gameobjects-bitmaptext#bitmaptextsize) - 描述此位图文本大小的对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L711](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L711)  
引入版本：3.0.0


---

### ParseFromAtlas {#ParseFromAtlas}

#### \<static> ParseFromAtlas(scene, fontName, textureKey, frameKey, xmlKey, [xSpacing], [ySpacing]) {#static-parsefromatlasscene-fontname-texturekey-framekey-xmlkey-xspacing-yspacing}


**说明:**

从一个 Atlas 中分析一个 XML 位图字体 。

将解析的位图字体数据添加到缓存中,并配有 `fontName` 键。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 解析位图字体的场景 。 |
| fontName | string | 否 | 添加到位图字体缓存的字体密钥 。 |
| textureKey | string | 否 | 比特玛普方块纹理的密钥. |
| frameKey | string | 否 | 比特玛普方格纹理框架的密钥. |
| xmlKey | string | 否 | 字体的 XML 数据解析的密钥 。 |
| xSpacing | number | 是 | 每个字母之间要添加的x轴间隔。 |
| ySpacing | number | 是 | 线高的Y轴间隔。 |


**返回值:** boolean - 解析是否成功 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1253](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1253)  
引入版本：3.0.0


---

### ParseXMLBitmapFont {#ParseXMLBitmapFont}

#### \<static> ParseXMLBitmapFont(xml, frame, [xSpacing], [ySpacing]) {#static-parsexmlbitmapfontxml-frame-xspacing-yspacing}


**说明:**

为位图字体缓存分析一个 XML 字体到位图字体数据 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| xml | XMLDocument | 否 |  | XML 文档从中解析字体 。 |
| frame | [Phaser.Textures.Frame](/api/class/textures-frame) | 否 |  | 创建 uv 数据时要考虑的纹理框架 。 |
| xSpacing | number | 是 | 0 | 每个字母之间要添加的x轴间隔。 |
| ySpacing | number | 是 | 0 | 线高的Y轴间隔。 |


**返回值:** [Phaser.Types.GameObjects.BitmapText.BitmapFontData](/api/typedef/types-gameobjects-bitmaptext#bitmapfontdata) - 解析的位图字体数据 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1273](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1273)  
引入版本：3.17.0


---

### preDestroy {#preDestroy}

#### \<instance> preDestroy() {#instance-predestroy}


**说明:**

内部破坏处理器,作为破坏过程的一部分而叫作.


**Access:** 保护


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1210](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1210)  
引入版本：3.50.0


---

### setCenterAlign {#setCenterAlign}

#### \<instance> setCenterAlign() {#instance-setcenteralign}


**说明:**

将此位图图文集中的文本行设置为中线。 只有当此位图图文集包含多行文本时, 才会有任何效果 。


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 此位图文本对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L339](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L339)  
引入版本：3.11.0


---

### setCharacterTint {#setCharacterTint}

#### \<instance> setCharacterTint([start], [length], [tintMode], [topLeft], [topRight], [bottomLeft], [bottomRight]) {#instance-setcharactertintstart-length-tintmode-topleft-topright-bottomleft-bottomright}


**说明:**

设置此位图文本中的一系列字符上的锡, 起始于 `start` 参数索引, 运行为 `length` 字符数量 。

`start`参数可以是负数,在这种情况下,它从文本的结尾开始,倒数`start`位置.

您也可以以 `length` 的 1 表示通过, 并且它会将 `start` 的所有字符都标注在字符串的尾端。 请记住, 空格和插点会算作字符 。

这是WebGL唯一的功能,只与静态位图文本合作,而不是动态.

锡特将一个颜色应用到比图文字纹理中的像素颜色值中,其中一种模式是:

- Phaser.TintModes.MULTIPLY( 默认)

- Phaser.TintModes.FILL

- Phaser.TintModes.ADD

- Phaser.TintModes.SCREEN

- Phaser.TintModes.OVERLAY

- Phaser.TintModes.HARD_LIGHT

您可以提供一种颜色值, 这样整个字符会用该颜色来涂色。 或者您可以提供每个角的颜色。 颜色会混合到字符范围的不同范围内 。

要修改已设定的锡色, 请使用新的颜色值再次调用此方法 。

使用 `setWordTint` 就可以覆盖此函数设定的锡,反之亦然.

要删除一个仅使用 `start` 的锡名称, 并且可以选择, `length` 参数定义 。

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| start | number | 是 | 0 | 起始字符开始点。 如果是负, 它会从文本的结尾算回来 。 |
| length | number | 是 | 1 | 要表示的字符数。 请记住空格也算作字符。 pass - 1 将 `start` 开始的所有字符都标记为字符 。 |
| tintMode | number | 是 | "Phaser.TintModes.MULTIPLY" | 使用锡金模式 。 |
| topLeft | number | 是 | "0xffffff" | 将应用到字符左上角的锡。 如果没有其他值被给出, 则该值被均匀应用, 整个字符被涂上 。 |
| topRight | number | 是 |  | 锡在人物的右上角应用. |
| bottomLeft | number | 是 |  | 将锡笔应用到字符的左下角. |
| bottomRight | number | 是 |  | 将锡条应用到字符的下方右侧. |


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 此位图文本对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L515](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L515)  
引入版本：3.50.0


---

### setDisplaySize {#setDisplaySize}

#### \<instance> setDisplaySize(width, height) {#instance-setdisplaysizewidth-height}


**说明:**

设置此位图图的游戏对象的显示大小。

调用这个会调整比例表。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 此位图Text 游戏对象的宽度 。 |
| height | number | 否 | 此位图Text游戏对象的高度 。 |


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 此游戏对象实例 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L887](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L887)  
引入版本：3.61.0


---

### setDropShadow {#setDropShadow}

#### \<instance> setDropShadow([x], [y], [color], [alpha]) {#instance-setdropshadowx-y-color-alpha}


**说明:**

设置此位图文本的投影效果 。

这是WebGL唯一的功能,只与静态位图文本合作,而不是动态.

可以设置阴影的垂直和水平抵消,以及颜色和α.

一旦启用阴影, 您可以直接修改此位图文本的 `dropShadowX` 和 `dropShadowY` 属性, 以实时调整阴影的位置 。

如果您想要清除阴影, 请使用此方法, 没有指定参数 。

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 下降阴影的横向偏移。 |
| y | number | 是 | 0 | 倒影的垂直偏移 |
| color | number | 是 | "0x000000" | 滴影的颜色,作为六进制值给出,即黑色的`0x000000`. |
| alpha | number | 是 | 0.5 | 投影的α,作为0到1之间的浮点表示,此与比图文字α(Bitmap Text alpha)也结合. |


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 此位图文本对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L477](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L477)  
引入版本：3.50.0


---

### setFont {#setFont}

#### \<instance> setFont(font, [size], [align]) {#instance-setfontfont-size-align}


**说明:**

更改此位图图文本用于渲染的字体 。

新的纹理被加载并应用到 BitmapText 中。 现有的文本、 大小和对齐被保留, 除非通过参数被覆盖 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| font | string | 否 |  | 从位图字体缓存中要使用的字体的密钥 。 |
| size | number | 是 |  | 此位图文字的字体大小。 如果不指定当前大小, 将会使用 。 |
| align | number | 是 | 0 | 在多行比图图文集对象中文本的对齐。如果不指定当前对齐,将使用此方法。 |


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 此位图文本对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L815](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L815)  
引入版本：3.11.0


---

### setFontSize {#setFontSize}

#### \<instance> setFontSize(size) {#instance-setfontsizesize}


**说明:**

设置此位图文本的字体大小 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| size | number | 否 | 要设置的字体大小 。 |


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 此位图文本对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L375](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L375)  
引入版本：3.0.0


---

### setLeftAlign {#setLeftAlign}

#### \<instance> setLeftAlign() {#instance-setleftalign}


**说明:**

将此位图图中的文本行设置为左对齐。 只有当此位图图图包含不止一行文本时, 文本行才会有任何效果 。


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 此位图文本对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L321](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L321)  
引入版本：3.11.0


---

### setLetterSpacing {#setLetterSpacing}

#### \<instance> setLetterSpacing([spacing]) {#instance-setletterspacingspacing}


**说明:**

设置此位图文本每个字符之间的字母间隔。 可以是增加空格的正值, 也可以是缩小空格的负值。 设置 knering 值后, 将应用间隔 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| spacing | number | 是 | 0 | 每个字符之间要添加的横向空间的量 。 |


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 此位图文本对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L394](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L394)  
引入版本：3.4.0


---

### setLineSpacing {#setLineSpacing}

#### \<instance> setLineSpacing([spacing]) {#instance-setlinespacingspacing}


**说明:**

设置行距值。该值将添加到字体高度中,以计算整条行距高度。

间距可以是负数或正数.

只有在此位图Text对象包含多行文本时才有效果.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| spacing | number | 是 | 0 | 多行文本中每行之间要添加的空格量 。 |


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 此位图文本对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L417](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L417)  
引入版本：3.60.0


---

### setMaxWidth {#setMaxWidth}

#### \<instance> setMaxWidth(value, [wordWrapCharCode]) {#instance-setmaxwidthvalue-wordwrapcharcode}


**说明:**

设置此比特玛普Text的最大显示宽度,以像素计。

如果`BitmapText.text`比`maxWidth`长,那么这些线会根据在行中发现的先前的白空字符自动包裹.

如果没有找到白空间,则不会进行包装,因此不会遵守`maxWidth`值。

通过设置值为 0 来禁用 maxWidth 。

您可以设置 `wordWrapCharCode` 参数或属性来设置要搜索的空白字符 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 此位图Text 的最大显示宽度以像素表示。 设置为零以禁用 。 |
| wordWrapCharCode | number | 是 | 字包包装时检查的字符代码。默认为32(空格字符) 。 |


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 此位图文本对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L853](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L853)  
引入版本：3.21.0


---

### setRightAlign {#setRightAlign}

#### \<instance> setRightAlign() {#instance-setrightalign}


**说明:**

将此位图图文集中的文本行设置为右对齐。 只有当此位图图文集包含不止一行文本时, 文本行才会有任何效果 。


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 此位图文本对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L357](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L357)  
引入版本：3.11.0


---

### setText {#setText}

#### \<instance> setText(value) {#instance-settextvalue}


**说明:**

设置此位图Text 的文本内容 。

将一系列字符串转换成多行文本。使用对齐方法来改变多行对齐。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | string \| Array.\<string> | 否 | 字符串,或字符串的数组, 将设置为此位图文本的内容 。 |


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 此位图文本对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L441](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L441)  
引入版本：3.0.0


---

### setWordTint {#setWordTint}

#### \<instance> setWordTint(word, [count], [tintMode], [topLeft], [topRight], [bottomLeft], [bottomRight]) {#instance-setwordtintword-count-tintmode-topleft-topright-bottomleft-bottomright}


**说明:**

在此位图文本中设置匹配的单词的锡值 。

`word`参数可以是字符串或数字.

如果一个字符串,它会运行一个字符串与文本内容的比较,如果匹配,它会给整个词点缀.

如果数字,它会根据词组内的索引来表示这个词。

`count` 参数控制了替换的字数。 将全部替换到 - 1 中 。

如果您通过一个数字作为要搜索的 `word` , 此参数将被忽略 。

这是WebGL唯一的功能,只与静态位图文本合作,而不是动态.

锡特将一个颜色应用到比图文字纹理中的像素颜色值中,其中一种模式是:

- Phaser.TintModes.MULTIPLY( 默认)

- Phaser.TintModes.FILL

- Phaser.TintModes.ADD

- Phaser.TintModes.SCREEN

- Phaser.TintModes.OVERLAY

- Phaser.TintModes.HARD_LIGHT

您可以提供一种颜色值, 这样整个字符会用该颜色来涂色。 或者您可以提供每个角的颜色。 颜色会混合到字符范围的不同范围内 。

要修改已设定的锡色, 请使用新的颜色值再次调用此方法 。

使用 `setCharacterTint` 就可以覆盖此函数设定的锡,反之亦然.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| word | string \| number | 否 |  | 要搜索的单词。 要么是字符串, 要么是单词数组中的单词索引 。 |
| count | number | 是 | 1 | 匹配字数到 tin。 ass - 1 到 tin 全部匹配字数 。 |
| tintMode | number | 是 | "Phaser.TintModes.MULTIPLY" | 使用锡金模式 。 |
| topLeft | number | 是 | "0xffffff" | 将应用到词的左上角的锡。 如果没有其他值被赋予, 则该值被均匀应用, 整个词被锡到 。 |
| topRight | number | 是 |  | 锡正应用于字头右侧. |
| bottomLeft | number | 是 |  | 锡被应用到词的左下角. |
| bottomRight | number | 是 |  | 锡语被应用到词的右下方. |


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 此位图文本对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L631](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L631)  
引入版本：3.50.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

构建此位图文本的 JSON 代表 。


**Overrides:** Phaser.GameObjects.GameObject#toJSON


**返回值:** [Phaser.Types.GameObjects.BitmapText.JSONBitmapText](/api/typedef/types-gameobjects-bitmaptext#jsonbitmaptext) - JSON 表示此位图文本 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1182](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1182)  
引入版本：3.0.0


---

### updateDisplayOrigin {#updateDisplayOrigin}

#### \<instance> updateDisplayOrigin() {#instance-updatedisplayorigin}


**说明:**

更新存储在此游戏对象上的“显示源”缓存值。您通常不直接调用,但会暴露在边缘大小写中。


**Overrides:** Phaser.GameObjects.Components.Origin#updateDisplayOrigin


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 此游戏对象实例 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L797](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L797)  
引入版本：3.0.0


---

---
