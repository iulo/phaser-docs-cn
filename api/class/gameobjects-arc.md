# Arc {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-arc)

Arc 形状是游戏对象,可以添加到景物、 组合或容器中。 您可以把它当作游戏中的其他对象, 如对它进行曲折、 缩放或允许输入或物理。 它为您提供了快速和容易的方法, 可以在游戏中不使用纹理来渲染此形状, 同时仍然利用在 WebGL 中被完全批量处理 。

此形状既支持填充颜色,也支持中风颜色.

当它显示弧形时, 您可以控制弧形的起始和结束角度, 或者这些角度是顺时针或逆时针旋转的。 默认设置会形成一个完整的圆形。 通过改变角度, 您可以创建其他的弧形, 如半圆形 。

弧形还具有`iterations`属性和相应的`setIterations`方法。这允许您通过控制构造过程中的重迭次数来控制形状在WebGL中如何平滑。

**构造函数**

`new Arc(scene, [x], [y], [radius], [startAngle], [endAngle], [anticlockwise], [fillColor], [fillAlpha])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| radius | number | 是 | 128 | 弧的半径. |
| startAngle | number | 是 | 0 | 弧的起始角度,以度计. |
| endAngle | number | 是 | 360 | 弧的端角,以度计. |
| anticlockwise | boolean | 是 | false | 始末角的风向顺序. |
| fillColor | number | 是 |  | 弧的颜色会被填充,即0xff000为红色. |
| fillAlpha | number | 是 |  | 弧的α会被填充。 您也可以使用其`alpha`属性设置整个形状的α 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Shape](/api/class/gameobjects-shape)  



> 源码：[src/gameobjects/shape/arc/Arc.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/arc/Arc.js#L15)  
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

### anticlockwise {#anticlockwise}

#### anticlockwise: boolean {#anticlockwise-boolean}


**说明:**

起始和结束角度的旋转顺序。 如果 `true` 弧是逆时针绘制的( 逆时针) , 否则是顺时针绘制的。 这影响到起始和结束角度之间向哪个弧扫射的方向 。


> 源码：[src/gameobjects/shape/arc/Arc.js#L224](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/arc/Arc.js#L224)  
引入版本：3.13.0


---

### endAngle {#endAngle}

#### endAngle: number {#endangle-number}


**说明:**

弧的端角,以度计.


> 源码：[src/gameobjects/shape/arc/Arc.js#L201](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/arc/Arc.js#L201)  
引入版本：3.13.0


---

### iterations {#iterations}

#### iterations: number {#iterations-number}


**说明:**

绘制弧时使用的重迭数。 以提供更多多边形为代价, 增加此数值。 修改此数值时要小一些, 如 0.01 。


> 源码：[src/gameobjects/shape/arc/Arc.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/arc/Arc.js#L125)  
引入版本：3.13.0


---

### radius {#radius}

#### radius: number {#radius-number}


**说明:**

弧的半径, 以像素表示。 更改这个值也会更新游戏对象的大小, 并触发对其几何数据进行重新计算 。


> 源码：[src/gameobjects/shape/arc/Arc.js#L151](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/arc/Arc.js#L151)  
引入版本：3.13.0


---

### startAngle {#startAngle}

#### startAngle: number {#startangle-number}


**说明:**

弧的起始角度,以度计.


> 源码：[src/gameobjects/shape/arc/Arc.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/arc/Arc.js#L178)  
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
 - [setFillStyle](/api/class/gameobjects-shape#setFillStyle)
 - [setStrokeStyle](/api/class/gameobjects-shape#setStrokeStyle)




---

## 公开方法 {#public-methods}

### setEndAngle {#setEndAngle}

#### \<instance> setEndAngle(value, [anticlockwise]) {#instance-setendanglevalue-anticlockwise}


**说明:**

设置弧的结束角度, 以度计。 可选的还更新了风向顺序。 此调用可被链条连接 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 设置结束角度的值 。 |
| anticlockwise | boolean | 是 | 如果 `true` 弧将反时针绘制。 如果 `false` 将顺时针绘制。 如果不给出, 则使用当前 `anticlockwise` 属性值 。 |


**返回值:** [Phaser.GameObjects.Arc](/api/class/gameobjects-arc) - 此游戏对象实例 。


> 源码：[src/gameobjects/shape/arc/Arc.js#L313](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/arc/Arc.js#L313)  
引入版本：3.13.0


---

### setIterations {#setIterations}

#### \<instance> setIterations(value) {#instance-setiterationsvalue}


**说明:**

设定绘制弧时所用的重迭次数。 以显示更多多边形为代价, 增加此数值。 修改此数值时, 如 0.01 等小量。 此调用可以连锁进行 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 设置重迭的值 。 |


**返回值:** [Phaser.GameObjects.Arc](/api/class/gameobjects-arc) - 此游戏对象实例 。


> 源码：[src/gameobjects/shape/arc/Arc.js#L267](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/arc/Arc.js#L267)  
引入版本：3.13.0


---

### setRadius {#setRadius}

#### \<instance> setRadius(value) {#instance-setradiusvalue}


**说明:**

设置弧的半径。此调用可被链条连接 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 设定半径的值 。 |


**返回值:** [Phaser.GameObjects.Arc](/api/class/gameobjects-arc) - 此游戏对象实例 。


> 源码：[src/gameobjects/shape/arc/Arc.js#L249](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/arc/Arc.js#L249)  
引入版本：3.13.0


---

### setStartAngle {#setStartAngle}

#### \<instance> setStartAngle(value, [anticlockwise]) {#instance-setstartanglevalue-anticlockwise}


**说明:**

设置弧的起始角度, 以度计。 可选的还更新了风向顺序。 此调用可被链条连接 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 设置起始角度的值 。 |
| anticlockwise | boolean | 是 | 如果 `true` 弧将反时针绘制。 如果 `false` 将顺时针绘制。 如果不给出, 则使用当前 `anticlockwise` 属性值 。 |


**返回值:** [Phaser.GameObjects.Arc](/api/class/gameobjects-arc) - 此游戏对象实例 。


> 源码：[src/gameobjects/shape/arc/Arc.js#L289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/arc/Arc.js#L289)  
引入版本：3.13.0


---

---
