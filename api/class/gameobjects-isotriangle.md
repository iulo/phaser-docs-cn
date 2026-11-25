# IsoTriangle {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-isotriangle)

IsoTriangle 形状是游戏对象,可以添加到游戏场景、组或容器中。您可以把它当作游戏中的其他任何游戏对象,比如对它进行曲折、缩放或允许输入或物理。它为您提供了快速和容易的方法,在游戏中不使用纹理来渲染此形状,同时仍然利用WebGL的完整批量。

此形状只支持填充颜色, 无法被中键 。

IsoTriangle 是“ 同位素” 三角形。 把它当金字塔一样看待。 每个面都有一个不同的填充颜色。 您可以分别设置三角形的上方、左方和右方的颜色。 您也可以选择哪个面孔通过 `showTop`、 `showLeft`和 `showRight` 属性来渲染 。

您无法从阴暗处查看 IsoTriangle, 但是您可以通过设置 `projection` 属性来更改“ 角 ” 。 如果 IsoTriangel 是否被颠倒, `reversed` 属性控制 。

**构造函数**

`new IsoTriangle(scene, [x], [y], [size], [height], [reversed], [fillTop], [fillLeft], [fillRight])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| size | number | 是 | 48 | 以像素表示的等距三角形的宽度。 左右面将完全为此值的一半 。 |
| height | number | 是 | 32 | 以等距三角形的高度。 左右面部会如此高。 以等距三角形的总高度将是这个值加半个`size`值 。 |
| reversed | boolean | 是 | false | 异形三角形是倒着的吗? |
| fillTop | number | 是 | "0xeeeeee" | 以异形三角形顶部面部的填充颜色. |
| fillLeft | number | 是 | "0x999999" | 以等距三角形左面的填充颜色. |
| fillRight | number | 是 | "0xcccccc" | 以等效三角形右面的填充颜色. |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Shape](/api/class/gameobjects-shape)  



> 源码：[src/gameobjects/shape/isotriangle/IsoTriangle.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isotriangle/IsoTriangle.js#L11)  
引入版本：3.13.0

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





**From [Phaser.GameObjects.Shape](/api/class/gameobjects-shape):**


 - [closePath](/api/class/gameobjects-shape#closePath)
 - [displayHeight](/api/class/gameobjects-shape#displayHeight)
 - [displayWidth](/api/class/gameobjects-shape#displayWidth)
 - [fillAlpha](/api/class/gameobjects-shape#fillAlpha)
 - [fillColor](/api/class/gameobjects-shape#fillColor)
 - [geom](/api/class/gameobjects-shape#geom)
 - [height](/api/class/gameobjects-shape#height)
 - [isFilled](/api/class/gameobjects-shape#isFilled)
 - [isStroked](/api/class/gameobjects-shape#isStroked)
 - [lineWidth](/api/class/gameobjects-shape#lineWidth)
 - [pathData](/api/class/gameobjects-shape#pathData)
 - [pathIndexes](/api/class/gameobjects-shape#pathIndexes)
 - [strokeAlpha](/api/class/gameobjects-shape#strokeAlpha)
 - [strokeColor](/api/class/gameobjects-shape#strokeColor)
 - [width](/api/class/gameobjects-shape#width)




---

## 公开成员 {#public-members}

### fillLeft {#fillLeft}

#### fillLeft: number {#fillleft-number}


**说明:**

用于填充以等距三角形左侧的颜色.


> 源码：[src/gameobjects/shape/isotriangle/IsoTriangle.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isotriangle/IsoTriangle.js#L86)  
引入版本：3.13.0


---

### fillRight {#fillRight}

#### fillRight: number {#fillright-number}


**说明:**

填充以异形三角形右侧的颜色.


> 源码：[src/gameobjects/shape/isotriangle/IsoTriangle.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isotriangle/IsoTriangle.js#L95)  
引入版本：3.13.0


---

### fillTop {#fillTop}

#### fillTop: number {#filltop-number}


**说明:**

填充等效三角顶部时所用的颜色。 只有在三角面反转时才使用此颜色 。


> 源码：[src/gameobjects/shape/isotriangle/IsoTriangle.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isotriangle/IsoTriangle.js#L77)  
引入版本：3.13.0


---

### isReversed {#isReversed}

#### isReversed: boolean {#isreversed-boolean}


**说明:**

表示异位三角是否倒置。


> 源码：[src/gameobjects/shape/isotriangle/IsoTriangle.js#L134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isotriangle/IsoTriangle.js#L134)  
引入版本：3.13.0


---

### projection {#projection}

#### projection: number {#projection-number}


**说明:**

以等效三角形的投影水平。 更改此值以改变您所查看的金字塔的“ 角 ” 。


> 源码：[src/gameobjects/shape/isotriangle/IsoTriangle.js#L67](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isotriangle/IsoTriangle.js#L67)  
引入版本：3.13.0


---

### showLeft {#showLeft}

#### showLeft: boolean {#showleft-boolean}


**说明:**

控制是否将像样三角形的左面渲染 。


> 源码：[src/gameobjects/shape/isotriangle/IsoTriangle.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isotriangle/IsoTriangle.js#L114)  
引入版本：3.13.0


---

### showRight {#showRight}

#### showRight: boolean {#showright-boolean}


**说明:**

控制是否将像样三角形的右面渲染 。


> 源码：[src/gameobjects/shape/isotriangle/IsoTriangle.js#L124](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isotriangle/IsoTriangle.js#L124)  
引入版本：3.13.0


---

### showTop {#showTop}

#### showTop: boolean {#showtop-boolean}


**说明:**

控制是否将像样三角形的顶部面部渲染出来 。


> 源码：[src/gameobjects/shape/isotriangle/IsoTriangle.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isotriangle/IsoTriangle.js#L104)  
引入版本：3.13.0


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





**From [Phaser.GameObjects.Shape](/api/class/gameobjects-shape):**


 - [preDestroy](/api/class/gameobjects-shape#preDestroy)
 - [setClosePath](/api/class/gameobjects-shape#setClosePath)
 - [setDisplaySize](/api/class/gameobjects-shape#setDisplaySize)
 - [setStrokeStyle](/api/class/gameobjects-shape#setStrokeStyle)




---

## 公开方法 {#public-methods}

### setFaces {#setFaces}

#### \<instance> setFaces([showTop], [showLeft], [showRight]) {#instance-setfacesshowtop-showleft-showright}


**说明:**

设置将渲染异形三角形的面额。 此调用可被链条 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| showTop | boolean | 是 | true | 显示异形三角形的顶部( 只有 `reversed` 属实时) |
| showLeft | boolean | 是 | true | 显示异形三角形的左面. |
| showRight | boolean | 是 | true | 显示异形三角形的右面. |


**返回值:** [Phaser.GameObjects.IsoTriangle](/api/class/gameobjects-isotriangle) - 此游戏对象实例 。


> 源码：[src/gameobjects/shape/isotriangle/IsoTriangle.js#L188](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isotriangle/IsoTriangle.js#L188)  
引入版本：3.13.0


---

### setFillStyle {#setFillStyle}

#### \<instance> setFillStyle([fillTop], [fillLeft], [fillRight]) {#instance-setfillstylefilltop-fillleft-fillright}


**说明:**

设置以等距三角形的每个面的填充颜色。此调用可被链条连接 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| fillTop | number | 是 | 填充异色三角形顶部时所用的颜色. |
| fillLeft | number | 是 | 用于填充以等距三角形左侧的颜色. |
| fillRight | number | 是 | 填充以异形三角形右侧的颜色. |


**重写:** Phaser.GameObjects.Shape#setFillStyle


**返回值:** [Phaser.GameObjects.IsoTriangle](/api/class/gameobjects-isotriangle) - 此游戏对象实例 。


> 源码：[src/gameobjects/shape/isotriangle/IsoTriangle.js#L214](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isotriangle/IsoTriangle.js#L214)  
引入版本：3.13.0


---

### setProjection {#setProjection}

#### \<instance> setProjection(value) {#instance-setprojectionvalue}


**说明:**

设置异形三角形的投影级别。 更改此值以改变您查看金字塔的“ 角 ” 。 此调用可被链条连接 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 设定投影到的值 。 |


**返回值:** [Phaser.GameObjects.IsoTriangle](/api/class/gameobjects-isotriangle) - 此游戏对象实例 。


> 源码：[src/gameobjects/shape/isotriangle/IsoTriangle.js#L152](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isotriangle/IsoTriangle.js#L152)  
引入版本：3.13.0


---

### setReversed {#setReversed}

#### \<instance> setReversed(reversed) {#instance-setreversedreversed}


**说明:**

设定是否将异位三角形向下翻转。 此调用可被链条连接 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| reversed | boolean | 否 | 是否使异形三角形倒置 。 |


**返回值:** [Phaser.GameObjects.IsoTriangle](/api/class/gameobjects-isotriangle) - 此游戏对象实例 。


> 源码：[src/gameobjects/shape/isotriangle/IsoTriangle.js#L170](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isotriangle/IsoTriangle.js#L170)  
引入版本：3.13.0


---

---
