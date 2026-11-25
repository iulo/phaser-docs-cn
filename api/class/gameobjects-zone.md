# Zone {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-zone)

AZO是非交替的矩形游戏对象,具有位置和大小但无纹理,它从不显示视觉,但确实在显示列表中存在,可以像其他游戏对象一样移动,缩放,旋转.

它的主要用途是创建 Dropp Zones 和 Introduction Hit Regions , 它为循环和矩形的跳动区提供了辅助方法, 也可以接受自定义的几何形状. Zones 也可用于对象重叠检查, 或者作为您自己非跳动游戏对象的基类.

默认来源为0.5,将其置于"区"中心,与其他游戏对象一致.

**构造函数**

`new Zone(scene, x, y, [width], [height])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属景点 。 |
| x | number | 否 |  | 这个游戏对象在世界的横向位置. |
| y | number | 否 |  | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 1 | 游戏对象的宽度 。 |
| height | number | 是 | 1 | 游戏对象的高度 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.GetBounds](/api/namespace/gameobjects-components-getbounds)  
> [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/zone/Zone.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/zone/Zone.js#L16)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


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

### blendMode {#blendMode}

#### blendMode: number {#blendmode-number}


**说明:**

游戏对象的混合模式。 尽管一个区域从未实现,但它仍然有一个混合模式,可以使其无缝地融入显示列表,而不会引起批量冲洗 。


> 源码：[src/gameobjects/zone/Zone.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/zone/Zone.js#L89)  
引入版本：3.0.0


---

### displayHeight {#displayHeight}

#### displayHeight: number {#displayheight-number}


**说明:**

此游戏对象的显示高度。 此值会考虑比例因素 。


> 源码：[src/gameobjects/zone/Zone.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/zone/Zone.js#L125)  
引入版本：3.0.0


---

### displayWidth {#displayWidth}

#### displayWidth: number {#displaywidth-number}


**说明:**

此游戏对象的显示宽度。 此值会考虑比例因素 。


> 源码：[src/gameobjects/zone/Zone.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/zone/Zone.js#L103)  
引入版本：3.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

此游戏对象的原生高度( 未标定) 。


> 源码：[src/gameobjects/zone/Zone.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/zone/Zone.js#L80)  
引入版本：3.0.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

此游戏对象的原生( 未标定) 宽度 。


> 源码：[src/gameobjects/zone/Zone.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/zone/Zone.js#L71)  
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




---

## 公开方法 {#public-methods}

### setCircleDropZone {#setCircleDropZone}

#### \<instance> setCircleDropZone(radius) {#instance-setcircledropzoneradius}


**说明:**

设定此区域为圆形投放区。 圆形以该区的`x`和`y`坐标为中心。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| radius | number | 否 | 将形成"落地区"的圆形半径. |


**返回值:** [Phaser.GameObjects.Zone](/api/class/gameobjects-zone) - 此游戏对象 。


> 源码：[src/gameobjects/zone/Zone.js#L200](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/zone/Zone.js#L200)  
引入版本：3.0.0


---

### setDisplaySize {#setDisplaySize}

#### \<instance> setDisplaySize(width, height) {#instance-setdisplaysizewidth-height}


**说明:**

设置此游戏对象的显示大小。 调用此功能将调整比例 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 此游戏对象的宽度 。 |
| height | number | 否 | 此游戏对象的高度 。 |


**返回值:** [Phaser.GameObjects.Zone](/api/class/gameobjects-zone) - 此游戏对象 。


> 源码：[src/gameobjects/zone/Zone.js#L180](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/zone/Zone.js#L180)  
引入版本：3.0.0


---

### setDropZone {#setDropZone}

#### \<instance> setDropZone([hitArea], [hitAreaCallback]) {#instance-setdropzonehitarea-hitareacallback}


**说明:**

通过调用启用此区域作为交互式投放区域 `setInteractive` 带有给定的命中区域形状和回调。您可以通过任意一个 Phaser 几何形状, 或带有匹配的命中测试回调的自定义形状。 如果没有提供参数, 将自动使用匹配此区域大小的矩形 。 如果此区域已经是交互式的, 则不会产生效果 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| hitArea | object | 是 | 几何形状实例, 如 Phaser.Geom.Ellipse , 或者您自己的自定义形状。 如果不给出, 它将尝试根据此区域大小创建矩形 。 |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 是 | 如果发送给定的 x/y coords 函数在形状之内, 则返回 `true` 函数。 如果您提供了形状, 您也必须提供回调 。 |


**返回值:** [Phaser.GameObjects.Zone](/api/class/gameobjects-zone) - 此游戏对象 。


> 源码：[src/gameobjects/zone/Zone.js#L233](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/zone/Zone.js#L233)  
引入版本：3.0.0


---

### setRectangleDropZone {#setRectangleDropZone}

#### \<instance> setRectangleDropZone(width, height) {#instance-setrectangledropzonewidth-height}


**说明:**

设定此区域为矩形投放区。 矩形位于此区域的 `x` 和 `y` 坐标上 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 矩形投放区的宽度. |
| height | number | 否 | 矩形落地带的高度. |


**返回值:** [Phaser.GameObjects.Zone](/api/class/gameobjects-zone) - 此游戏对象 。


> 源码：[src/gameobjects/zone/Zone.js#L216](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/zone/Zone.js#L216)  
引入版本：3.0.0


---

### setSize {#setSize}

#### \<instance> setSize(width, height, [resizeInput]) {#instance-setsizewidth-height-resizeinput}


**说明:**

设置此区的原生( 未标定) 宽度和高度。 同时更新显示源, 并默认更改与此区相关的任何非定制输入命中区域大小 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 否 |  | 此游戏对象的宽度 。 |
| height | number | 否 |  | 此游戏对象的高度 。 |
| resizeInput | boolean | 是 | true | 如果这个区域有一个矩形的撞击区域,这个参数也会改变撞击区域大小。 |


**返回值:** [Phaser.GameObjects.Zone](/api/class/gameobjects-zone) - 此游戏对象 。


> 源码：[src/gameobjects/zone/Zone.js#L147](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/zone/Zone.js#L147)  
引入版本：3.0.0


---

---
