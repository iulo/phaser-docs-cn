# DOMElement {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-domelement)

DOM Element Game Objects 是控制并操纵HTML Elements在游戏顶端的一种方法.

DOM 元素要显示, 您必须加入以下游戏配置对象, 才能显示 :

```javascript
dom {
  createContainer: true
}
```

您还必须有一个 Phaser 的母容器。这是游戏配置中的 `parent` 属性指定的 。

当添加这两个东西时, Phaser 将自动创建一个位于游戏画布顶部的 DOM 容器 div 。 此画布大小与画布相匹配, 如果画布大小发生变化, 则由于在 Scale 管理器内设置, 圆顶容器会相应调整大小 。

如果您还没有这样做, 您必须在游戏配置中提供 `parent`, 否则 DOM 容器将无法创建 。

您可以通过 DOM 元素在 DOM 环绕中通过, 或者通过一个引用当前想要置于 Phaser 控制之下的元素来创建 DOM 元素。 例如 :

```javascript
this.add.dom(x, y, 'div', 'background-color: lime; width: 220px; height: 100px; font: 48px Arial', 'Phaser');
```

上述代码将在给定的x/y坐标处将一个 div 元素插入 DOM 容器。 DOMSTring 在 4 参数中设置了 div 的初始 CSS 样式, 最终参数是内文本。 在这种情况下, 它将创建一个 石灰色 div, 大小为 220px 乘 100px, 其文本为 Phaser, 字体为 Arial 字体 。

您几乎应该毫无例外地使用明确大小的 HTML 元素,以便完全控制元素在常规游戏内容旁边的对齐和定位.

与其直接指定 CSS 和 HTML , 您可以使用 `load.html` 文件加载器将其加载到缓存中, 然后使用 `createFromCache` 方法。 您也可以使用 `createFromHTML` 和该类中可用的其他各种方法来帮助构建您的要素 。

一旦元素被创建, 您就可以像其他游戏对象一样控制它。 您可以设定它的位置、 尺度、 旋转、 α 等属性。 它会随着主要场景相机的移动而移动, 并在画布的边缘被剪辑。 必须记住 DOM 元素的一些限制: 显而易见的是它们出现在您的游戏画布上或下方。 您不能把它们混入显示列表, 也就是说您不能有一个 DOM 元素, 然后是 Sprite, 然后是另一个 DOM 元素。

无法启用它们来输入。 要做到这一点, 您必须使用 `addListener` 方法直接添加本地事件听器。 最后的限制是使用相机。 DOM 容器大小可以完全匹配游戏布, 并相应剪辑。 DOM Elements 尊重相机滚动和 scrollFactor 设置, 但是如果您改变相机的大小, 从而与画布的大小不再匹配, 就不会相应剪辑 。

DOM 游戏对象可以添加到 Phaser 容器中, 但是您只应该将其嵌入** 深一层**。 任何更深的链条都会忽略所有根容器属性 。

此外,所有DOM元素都插入到同一个DOM容器中,不管它们是在哪个场景中创建的.

注意您只应该在带有 _ single_ 相机的场景中设置 DOM Elements。 如果您需要多个相机, 请使用平行的场景来达到此目的 。

DOM Elements 是将本地 HTML 与您的 Phaser 游戏对象对齐的有力方法。 例如, 您可以在您的标题屏幕中直接插入多人游戏的登录表。 或者是高分表的文本输入框。 或者是来自 3rd 派对服务的横幅广告。 或者您想用它们来高分辨率文本显示和UI 。 选择权在你, 请记住您正在处理标的 HTML 和 CSS 浮在游戏顶部, 并应该相应处理它 。

**构造函数**

`new DOMElement(scene, [x], [y], [element], [style], [innerText])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| x | number | 是 | 0 | 这个DOM元素在世界的横向位置. |
| y | number | 是 | 0 | 这个DOM元素在世界的垂直位置. |
| element | Element \| string | 是 |  | 已有的 DOM 元素, 或者字符串。 如果从 # 开始的字符串, 将会在字符串上进行 `getElementById` 的查询( 减去散列) 。 没有散列, 它代表要创建的元素类型, 即“ div ” 。 |
| style | string \| any | 是 |  | 如果字符串, 将直接设置为元素 `style` 属性值。 如果是一个普通对象, 将标注并传输值。 在这两种情况下, 替换 CSS 样式的值可能已经设置过 。 |
| innerText | string | 是 |  | 如果给出,将直接设定为元素`innerText`属性值,以取代之前的任意值。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/domelement/DOMElement.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L16)  
引入版本：3.17.0

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




---

## 公开成员 {#public-members}

### cache {#cache}

#### cache: [Phaser.Cache.BaseCache](/api/class/cache-basecache) {#cache-phasercachebasecache}


**说明:**

引用 HTML 快取 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L138](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L138)  
引入版本：3.17.0


---

### displayHeight {#displayHeight}

#### displayHeight: number {#displayheight-number}


**说明:**

基于 `getBoundingClientRect` DOM 调用,计算出此游戏对象的显示高度 。

属性 `height` 持有这个 DOM 元素的未标高度 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L275](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L275)  
引入版本：3.17.0


---

### displayWidth {#displayWidth}

#### displayWidth: number {#displaywidth-number}


**说明:**

基于 `getBoundingClientRect` DOM 调用计算出来的此游戏对象的显示宽度 。

属性 `width` 持有这个 DOM 元素的未缩放宽度 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L263](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L263)  
引入版本：3.17.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

此游戏对象的原生高度( 未标定) 。

对于 DOM 元素,此属性只读 。

`displayHeight` 属性在缩放时会包含这个 DOM 元素的计算范围。


> 源码：[src/gameobjects/domelement/DOMElement.js#L249](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L249)  
引入版本：3.17.0


---

### node {#node}

#### node: Element {#node-element}


**说明:**

此游戏对象所必须的实际 DOM 元素。 例如, 如果您创建了 `<div>`, 那么此属性直接指向该元素 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L147](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L147)  
引入版本：3.17.0


---

### parent {#parent}

#### parent: Element {#parent-element}


**说明:**

游戏实例启动时创建的父 DOM 容器的引用 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L124](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L124)  
引入版本：3.17.0


---

### perspective {#perspective}

#### perspective: number {#perspective-number}


**说明:**

视角 CSS 容器的属性值 _ centrain_ 。 这决定了 z=0 平面与用户之间的距离, 以便给出一个三维位元素。 每个带 z > 0 的 3D 元素会变大; 带 z &lt; 0 的 3 D 元素会变小。 效果的强度由此属性的值决定 。

更多信息见:[https://developer.mozilla.org/en-US/docs/Web/CSS/perspective](https://developer.mozilla.org/en-US/docs/Web/CSS/perspective)

**Changing this value changes it globally for all DOM Elements, as they all share the same parent container.**


> 源码：[src/gameobjects/domelement/DOMElement.js#L389](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L389)  
引入版本：3.17.0


---

### pointerEvents {#pointerEvents}

#### pointerEvents: string {#pointerevents-string}


**说明:**

设定渲染过程中 DOM 元素的 CSS `pointerEvents` 属性 。

这是默认的“ 自动” 。 更改它可能会产生意外的副作用, 并带有内部的 Phaser 输入处理, 如拖动, 所以只有您理解其影响时, 才会更改 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L222](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L222)  
引入版本：3.55.0


---

### rotate3d {#rotate3d}

#### rotate3d: [Phaser.Math.Vector4](/api/class/math-vector4) {#rotate3d-phasermathvector4}


**说明:**

含有此 DOM 元素在三维空间中固定轴周围的三维旋转的矢量 4。

x, y, 和 z 组件定义旋转轴的方向。 w 组件持有旋转角, 位于 `rotate3dAngle` 属性定义的单位( 默认度) 。

详情见以下MDN页:

[https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate3d](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate3d)


> 源码：[src/gameobjects/domelement/DOMElement.js#L194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L194)  
引入版本：3.17.0


---

### rotate3dAngle {#rotate3dAngle}

#### rotate3dAngle: string {#rotate3dangle-string}


**说明:**

代表三维旋转值的单位。 默认情况下, 度值为 `deg`, 但可以更改为任何支持的单位。 请参看此页面的详情 :

[https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate3d](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate3d)


> 源码：[src/gameobjects/domelement/DOMElement.js#L210](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L210)  
引入版本：3.17.0


---

### skewX {#skewX}

#### skewX: number {#skewx-number}


**说明:**

角度,用弧度表示,通过这个角度,可以将DOM元素在水平轴上扭曲.

[https://developer.mozilla.org/en-US/docs/Web/CSS/transform](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)


> 源码：[src/gameobjects/domelement/DOMElement.js#L172](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L172)  
引入版本：3.17.0


---

### skewY {#skewY}

#### skewY: number {#skewy-number}


**说明:**

角度,用弧度表示,通过这个角度,可以将DOM元素在垂直轴上扭曲.

[https://developer.mozilla.org/en-US/docs/Web/CSS/transform](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)


> 源码：[src/gameobjects/domelement/DOMElement.js#L183](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L183)  
引入版本：3.17.0


---

### transformOnly {#transformOnly}

#### transformOnly: boolean {#transformonly-boolean}


**说明:**

默认一个DOM元素将具有它的变换,显示,不透明, zIndex 并混合模式属性,在渲染时更新。如果出于某种原因,您不希望这些特性除了CSS变换外有任何改变,那么设置此旗为 `true`时 `true` 仅应用了 CSS 变形器,您可以按要求跟踪和设置其他属性.

举例来说,如果有DOM元素的巢, 并且不希望任何孩子都能捡到不透明,这可以很方便。


> 源码：[src/gameobjects/domelement/DOMElement.js#L157](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L157)  
引入版本：3.17.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

此游戏对象的原生( 未标定) 宽度 。

对于 DOM 元素,此属性只读 。

`displayWidth` 属性在缩放时会包含这个 DOM 元素的计算范围。


> 源码：[src/gameobjects/domelement/DOMElement.js#L235](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L235)  
引入版本：3.17.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Events.EventEmitter](/api/class/events-eventemitter):**


 - [emit](/api/class/events-eventemitter#emit)
 - [eventNames](/api/class/events-eventemitter#eventNames)
 - [listenerCount](/api/class/events-eventemitter#listenerCount)
 - [listeners](/api/class/events-eventemitter#listeners)
 - [off](/api/class/events-eventemitter#off)
 - [on](/api/class/events-eventemitter#on)
 - [once](/api/class/events-eventemitter#once)
 - [removeAllListeners](/api/class/events-eventemitter#removeAllListeners)
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
 - [willRoundVertices](/api/class/gameobjects-gameobject#willRoundVertices)




---

## 公开方法 {#public-methods}

### addListener {#addListener}

#### \<instance> addListener(events) {#instance-addlistenerevents}


**说明:**

将一个或多个本地 DOM 事件听众添加到游戏对象的元素中。 然后通过此游戏对象标准事件发送器发送事件 。

例如:

```javascript
var div = this.add.dom(x, y, element);

div.addListener('click');

div.on('click', handler);
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| events | string | 否 | DOM 事件/ 需要倾听。 您可以用空格分隔多个事件 。 |


**Overrides:** Phaser.GameObjects.GameObject#addListener


**返回值:** [Phaser.GameObjects.DOMElement](/api/class/gameobjects-domelement) - 这个DOM元素实例 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L417](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L417)  
引入版本：3.17.0


---

### createElement {#createElement}

#### \<instance> createElement(tagName, [style], [innerText]) {#instance-createelementtagname-style-innertext}


**说明:**

创建本地 DOM 元素, 添加到父 DOM 容器中, 然后绑定到此游戏对象, 这样您就可以控制它。 `tagName`应该是一个字符串, 并传递到 `document.createElement` :

```javascript
this.add.dom().createElement('div');
```

关于可接受的标签名称的更多详情,见:[https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)

您也可以通过 DOMSTring 或样式对象来设定 CSS 的创建元素, 以及可选的 `innerText` 值。 以下是 DOMSTring 的示例 :

```javascript
this.add.dom().createElement('div', 'background-color: lime; width: 220px; height: 100px; font: 48px Arial', 'Phaser');
```

使用样式对象 :

```javascript
var style = {
  'background-color': 'lime';
  'width': '200px';
  'height': '100px';
  'font': '48px Arial';
};

this.add.dom().createElement('div', style, 'Phaser');
```

如果此游戏对象已经有一个元素, 它将被从 DOM 中完全删除。 您先前创建的任何事件听众都需要在此调用后重新创建 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tagName | string | 否 | 指定要创建的元素类型的字符串。 创建元素的 nodeName 以 tagName 的值初始化。 不要使用此方法的限定名称( 如“ html: a ” ) 。 |
| style | string \| any | 是 | 要么是持有 CSS 样式的 DOMSTring 样式用于创建元素,要么是该样式将从对象读取 。 |
| innerText | string | 是 | 一种DOMSTring,它持有将被设定为创建元素的innerText的文本. |


**返回值:** [Phaser.GameObjects.DOMElement](/api/class/gameobjects-domelement) - 这个DOM元素实例 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L492](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L492)  
引入版本：3.17.0


---

### createFromCache {#createFromCache}

#### \<instance> createFromCache(key, [tagName]) {#instance-createfromcachekey-tagname}


**说明:**

从 HTML 缓存中取出块 html, 之前已经预装到游戏中, 然后从中创建 DOM Element。 已装入的 HTML 被设定为创建元素的 `innerHTML` 属性 。

假设以下html存储在一个名为`loginform.html`的文件中:

```html
<input type="text" name="nameField" placeholder="Enter your name" style="font-size: 32px">
<input type="button" name="playButton" value="Let's Play" style="font-size: 32px">
```

使用缓存密钥“ login” 装入到您的游戏中 :

```javascript
this.load.html('login', 'assets/loginform.html');
```

您可以使用缓存键创建 DOM 元素 :

```javascript
this.add.dom().createFromCache('login');
```

可选的 `elementType` 参数控制创建的容器, 将装入的 html 插入其中。 默认是一个普通 `div` 对象, 但可以给出任何有效的 tagName 。

如果此游戏对象已经有一个元素, 它将被从 DOM 中完全删除。 您先前创建的任何事件听众都需要在此调用后重新创建 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 用于此 DOM Element 的 html 缓存项的密钥 。 |
| tagName | string | 是 | "'div'" | 插入全部已装入的 html 的元素的标记名称。 默认为普通 div 标记 。 |


**返回值:** [Phaser.GameObjects.DOMElement](/api/class/gameobjects-domelement) - 这个DOM元素实例 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L654](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L654)  
引入版本：3.17.0


---

### createFromHTML {#createFromHTML}

#### \<instance> createFromHTML(html, [tagName]) {#instance-createfromhtmlhtml-tagname}


**说明:**

取一个 html 的字符串,然后从中创建 DOM 元素。 HTML 被设定为创建元素的 `innerHTML` 属性 。

```javascript
let form = `
<input type="text" name="nameField" placeholder="Enter your name" style="font-size: 32px">
<input type="button" name="playButton" value="Let's Play" style="font-size: 32px">
`;
```

您可以使用字符串创建 DOM 元素 :

```javascript
this.add.dom().createFromHTML(form);
```

选项 `elementType` 参数控制创建的容器类型, 将 html 插入其中。 默认是一个普通 `div` 对象, 但是任何有效的 tagName 都可以给出 。

如果此游戏对象已经有一个元素, 它将被从 DOM 中完全删除。 您先前创建的任何事件听众都需要在此调用后重新创建 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| html | string | 否 |  | 将设置为创建元素的 `innerHTML` 属性的 html 字符串 。 |
| tagName | string | 是 | "'div'" | 插入所有 html 的元素的标记名称。 默认为 plain div 标记 。 |


**返回值:** [Phaser.GameObjects.DOMElement](/api/class/gameobjects-domelement) - 这个DOM元素实例 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L704](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L704)  
引入版本：3.17.0


---

### getChildByID {#getChildByID}

#### \<instance> getChildByID(id) {#instance-getchildbyidid}


**说明:**

将所有的孩子从 DOM 元素节点中获取, 使用 `querySelectorAll('*')` 并穿插到它们, 寻找第一个有匹配的 ID 。 如果找到的话, 它会返回这个孩子, 如果找不到, 也可以返回 `null` 。

要注意阶级和身份名称对案件有敏感认识.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| id | string | 否 | 寻找孩子们的ID |


**返回值:** Element - 第一个匹配的孩子 DOM Element, 或者 `null` 如果找不到的话.


> 源码：[src/gameobjects/domelement/DOMElement.js#L837](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L837)  
引入版本：3.17.0


---

### getChildByName {#getChildByName}

#### \<instance> getChildByName(name) {#instance-getchildbynamename}


**说明:**

将所有的孩子从 DOM 元素节点中获取, 使用 `querySelectorAll('*')` 并穿插到它们中, 寻找第一个有匹配名称的。 如果找到, 它会返回这个孩子, 如果找不到, 则返回 `null` 。

要注意阶级和身份名称对案件有敏感认识.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 搜身寻童之名. |


**返回值:** Element - 第一个匹配的孩子 DOM Element, 或者 `null` 如果找不到的话.


> 源码：[src/gameobjects/domelement/DOMElement.js#L855](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L855)  
引入版本：3.17.0


---

### getChildByProperty {#getChildByProperty}

#### \<instance> getChildByProperty(property, value) {#instance-getchildbypropertyproperty-value}


**说明:**

从 DOM 元素节点中获取所有的孩子, 使用 `querySelectorAll('*')` 并穿插到它们, 寻找第一个具有匹配给定的密钥和值的属性的孩子。 如果找到的话, 它会返回这个孩子, 如果找不到的话, 也可以返回 `null` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| property | string | 否 | 寻找孩子的财产 |
| value | string | 否 | 财产的价值必须严格平等。 |


**返回值:** Element - 第一个匹配的孩子 DOM Element, 或者 `null` 如果找不到的话.


> 源码：[src/gameobjects/domelement/DOMElement.js#L806](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L806)  
引入版本：3.17.0


---

### removeElement {#removeElement}

#### \<instance> removeElement() {#instance-removeelement}


**说明:**

从 DOM 中完全删除当前绑定到此游戏对象的 DOM 元素, 并将此游戏对象的 `node` 属性重排为 `null` 。


**返回值:** [Phaser.GameObjects.DOMElement](/api/class/gameobjects-domelement) - 这个DOM元素实例 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L761](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L761)  
引入版本：3.17.0


---

### removeListener {#removeListener}

#### \<instance> removeListener(events) {#instance-removelistenerevents}


**说明:**

从游戏对象的内在元素中移除一个或多个本地 DOM 事件听众 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| events | string | 否 | DOM 事件/ 停止监听。 您可以用空格分隔多个事件 。 |


**Overrides:** Phaser.GameObjects.GameObject#removeListener


**返回值:** [Phaser.GameObjects.DOMElement](/api/class/gameobjects-domelement) - 这个DOM元素实例 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L453](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L453)  
引入版本：3.17.0


---

### setClassName {#setClassName}

#### \<instance> setClassName(className) {#instance-setclassnameclassname}


**说明:**

设置 DOM 元素节点的 `className` 属性并更新内部大小 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| className | string | 否 | 代表元素的类或空格分隔的类的字符串。 |


**返回值:** [Phaser.GameObjects.DOMElement](/api/class/gameobjects-domelement) - 这个DOM元素实例 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L873](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L873)  
引入版本：3.17.0


---

### setElement {#setElement}

#### \<instance> setElement(element, [style], [innerText]) {#instance-setelementelement-style-innertext}


**说明:**

将一个新的 DOM 元素绑入此游戏对象。 如果此游戏对象已经有一个元素, 它将被从 DOM 中完全删除。 您先前创建的任何事件听众都需要在新元素上重新创建 。

你通过这个方法的`element`的论据可以是字符串tagName:

```javascript
<h1 id="heading">Phaser</h1>

this.add.dom().setElement('heading');
```

或提及元素实例:

```javascript
<h1 id="heading">Phaser</h1>

var h1 = document.getElementById('heading');

this.add.dom().setElement(h1);
```

您也可以通过 DOMSTring 或样式对象来设定 CSS 的创建元素, 以及可选的 `innerText` 值。 以下是 DOMSTring 的示例 :

```javascript
this.add.dom().setElement(h1, 'background-color: lime; width: 220px; height: 100px; font: 48px Arial', 'Phaser');
```

使用样式对象 :

```javascript
var style = {
  'background-color': 'lime';
  'width': '200px';
  'height': '100px';
  'font': '48px Arial';
};

this.add.dom().setElement(h1, style, 'Phaser');
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| element | string \| Element | 否 | 如果一个字符串传递给`getElementById()`,或者它应该指代一个已有的元素. |
| style | string \| any | 是 | 要么是持有 CSS 样式的 DOMSTring 样式用于创建元素,要么是该样式将从对象读取 。 |
| innerText | string | 是 | 一种DOMSTring,它持有将被设定为创建元素的innerText的文本. |


**返回值:** [Phaser.GameObjects.DOMElement](/api/class/gameobjects-domelement) - 这个DOM元素实例 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L539](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L539)  
引入版本：3.17.0


---

### setHTML {#setHTML}

#### \<instance> setHTML(html) {#instance-sethtmlhtml}


**说明:**

设置 DOM 元素节点的 `innerHTML` 属性并更新内部大小 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| html | string | 否 | html的DOMstring 将被设定为元素的 `innerHTML` 属性 。 |


**返回值:** [Phaser.GameObjects.DOMElement](/api/class/gameobjects-domelement) - 这个DOM元素实例 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L919](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L919)  
引入版本：3.17.0


---

### setPerspective {#setPerspective}

#### \<instance> setPerspective(value) {#instance-setperspectivevalue}


**说明:**

设置 _parent DOM Control_ 的 CSS 属性。 这将确定 z=0 平面与用户之间的距离, 以便给出一个 3D 位置的元素。 每个 z > 0 的 3D 元素会变大; 每个 z &lt; 0 的 3 D 元素会变小。 效果的强度由此属性的值决定 。

更多信息见:[https://developer.mozilla.org/en-US/docs/Web/CSS/perspective](https://developer.mozilla.org/en-US/docs/Web/CSS/perspective)

**Changing this value changes it globally for all DOM Elements, as they all share the same parent container.**

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 视角值,以像素表示,它决定z平面与用户之间的距离. |


**返回值:** [Phaser.GameObjects.DOMElement](/api/class/gameobjects-domelement) - 这个DOM元素实例 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L365](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L365)  
引入版本：3.17.0


---

### setSkew {#setSkew}

#### \<instance> setSkew([x], [y]) {#instance-setskewx-y}


**说明:**

设置此 DOM 元素的横向和纵向skew 值。

更多信息见:[https://developer.mozilla.org/en-US/docs/Web/CSS/transform](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 角度,用弧度表示,通过这个角度,可以将DOM元素在水平轴上扭曲. |
| y | number | 是 | "x" | 角度,用弧度表示,通过这个角度,可以将DOM元素在垂直轴上扭曲. |


**返回值:** [Phaser.GameObjects.DOMElement](/api/class/gameobjects-domelement) - 这个DOM元素实例 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L341](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L341)  
引入版本：3.17.0


---

### setText {#setText}

#### \<instance> setText(text) {#instance-settexttext}


**说明:**

设置 DOM 元素节点的 `innerText` 属性并更新内部大小 。

注意只有某些类型的元素才能在它们上设置`innerText`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| text | string | 否 | 表示该元素已渲染的文本内容的 DOMSTring 。 |


**返回值:** [Phaser.GameObjects.DOMElement](/api/class/gameobjects-domelement) - 这个DOM元素实例 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L895](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L895)  
引入版本：3.17.0


---

### updateSize {#updateSize}

#### \<instance> updateSize() {#instance-updatesize}


**说明:**

设定 `displayWidth` 财务报告和已审计财务报表 `displayHeight` 属性,以及 `clientWidth` 财务报告和已审计财务报表 `clientHeight` 数值输入 `width` 财务报告和已审计财务报表 `height` 属性。

当创建或设定新元素时,此功能会自动调用 。


**返回值:** [Phaser.GameObjects.DOMElement](/api/class/gameobjects-domelement) - 这个DOM元素实例 。


> 源码：[src/gameobjects/domelement/DOMElement.js#L782](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L782)  
引入版本：3.17.0


---

### willRender {#willRender}

#### \<instance> willRender() {#instance-willrender}


**说明:**

将 renderMask 和 renderFlags 相比较,看看此游戏对象是否渲染成像 。

DOMElements 总是返回 `true`,因为它们需要在渲染传感时仍然设置值,即使不可见.


**Overrides:** Phaser.GameObjects.GameObject#willRender


**返回值:** boolean - 如果游戏对象应该渲染,则使用`true`,否则使用`false`.


> 源码：[src/gameobjects/domelement/DOMElement.js#L959](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElement.js#L959)  
引入版本：3.17.0


---

---
