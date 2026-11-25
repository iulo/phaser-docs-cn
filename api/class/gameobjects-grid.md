# Grid {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-grid)

网格形状是一个游戏对象,可以添加到场景、组或容器中。您可以把它像游戏中其它游戏对象一样对待,比如对它进行扭动、缩放或允许输入或物理。它为您提供了快速和容易的方法,在游戏中不使用纹理来渲染此形状,同时仍然利用WebGL的完整批量。

网格形状允许您在游戏中显示网格, 您可以在此控制网格的大小以及网格单元格的宽度和高度。 您可以为每个网格单元格设置填充色以及替代的填充色。 当设定了替代填充色后, 网格单元格会随其生成时而替换填充色, 从而产生棋盘效果。 您也可以选择使用中风填充色。 如果设置, 则在给定颜色中绘制网格单元格之间的线条。 如果您指定了带零的中风颜色, 则会绘制被分隔的单元格, 但不显示它们之间的线条。

**构造函数**

`new Grid(scene, [x], [y], [width], [height], [cellWidth], [cellHeight], [fillColor], [fillAlpha], [strokeFillColor], [strokeFillAlpha])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 网格的宽度. |
| height | number | 是 | 128 | 网格的高度. |
| cellWidth | number | 是 | 32 | 网格中一个单元格的宽度 。 |
| cellHeight | number | 是 | 32 | 网格中一个细胞的高度. |
| fillColor | number | 是 |  | 网格单元格的颜色会填充,即0xff000表示红色. |
| fillAlpha | number | 是 |  | 网格单元格将填充α。您也可以使用其`alpha`属性设置整个形状的α 。 |
| strokeFillColor | number | 是 |  | 网格单元格之间的线条颜色。请参见 `setStrokeStyle` 方法。 |
| strokeFillAlpha | number | 是 |  | 网格细胞之间的线条的α. |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Shape](/api/class/gameobjects-shape)  



> 源码：[src/gameobjects/shape/grid/Grid.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/grid/Grid.js#L11)  
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

### altFillAlpha {#altFillAlpha}

#### altFillAlpha: number {#altfillalpha-number}


**说明:**

交替的网格单元格将填充α。您也可以使用其`alpha`属性设置整个形状的α 。


> 源码：[src/gameobjects/shape/grid/Grid.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/grid/Grid.js#L104)  
引入版本：3.13.0


---

### altFillColor {#altFillColor}

#### altFillColor: number {#altfillcolor-number}


**说明:**

交替网格单元格的颜色将填充,即0xff000为红色。


> 源码：[src/gameobjects/shape/grid/Grid.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/grid/Grid.js#L95)  
引入版本：3.13.0


---

### cellHeight {#cellHeight}

#### cellHeight: number {#cellheight-number}


**说明:**

每个网格单元格的高度。 必须是正值 。


> 源码：[src/gameobjects/shape/grid/Grid.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/grid/Grid.js#L75)  
引入版本：3.13.0


---

### cellPadding {#cellPadding}

#### cellPadding: number {#cellpadding-number}


**说明:**

每个细胞周围的粘合物。细胞之间的有效沟槽是这个值的两倍。


> 源码：[src/gameobjects/shape/grid/Grid.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/grid/Grid.js#L114)  
引入版本：4.0.0


---

### cellWidth {#cellWidth}

#### cellWidth: number {#cellwidth-number}


**说明:**

每个网格单元格的宽度。 必须是正值 。


> 源码：[src/gameobjects/shape/grid/Grid.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/grid/Grid.js#L65)  
引入版本：3.13.0


---

### showAltCells {#showAltCells}

#### showAltCells: boolean {#showaltcells-boolean}


**说明:**

控制网格是否使用 `altFillColor` 和 `altFillAlpha` 值使单元格交替。通过 `setAltFillStyle` 方法设定此值 。


> 源码：[src/gameobjects/shape/grid/Grid.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/grid/Grid.js#L85)  
引入版本：3.13.0


---

### strokeOutside {#strokeOutside}

#### strokeOutside: boolean {#strokeoutside-boolean}


**说明:**

是否在网格对象的外部边缘上按下 。


> 源码：[src/gameobjects/shape/grid/Grid.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/grid/Grid.js#L125)  
引入版本：4.0.0


---

### strokeOutsideIncomplete {#strokeOutsideIncomplete}

#### strokeOutsideIncomplete: boolean {#strokeoutsideincomplete-boolean}


**说明:**

单元格不完整时是否在格子对象的外部边缘上按下,例如格子大小不均匀地与单元格大小吻合.

这只有在`strokeOutside`是`true`时才会有效果,它会影响电网的右侧和下侧边缘.


> 源码：[src/gameobjects/shape/grid/Grid.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/grid/Grid.js#L135)  
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

### setAltFillStyle {#setAltFillStyle}

#### \<instance> setAltFillStyle([fillColor], [fillAlpha]) {#instance-setaltfillstylefillcolor-fillalpha}


**说明:**

设置交替格单元格将使用的填充色和α级。

如果使用这种方法时没有值, 则转换的网格单元格将不会以不同的颜色显示 。

另见`setStrokeStyle`和`setFillStyle`方法.

这个电话可以被锁起来。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| fillColor | number | 是 |  | 交替网格单元格的颜色将填充,即0xff000为红色。 |
| fillAlpha | number | 是 | 1 | 交替的网格单元格将填充α。您也可以使用其`alpha`属性设置整个形状的α 。 |


**返回值:** [Phaser.GameObjects.Grid](/api/class/gameobjects-grid) - 此游戏对象实例 。


> 源码：[src/gameobjects/shape/grid/Grid.js#L163](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/grid/Grid.js#L163)  
引入版本：3.13.0


---

### setCellPadding {#setCellPadding}

#### \<instance> setCellPadding([value]) {#instance-setcellpaddingvalue}


**说明:**

设置网格的单元格粘贴。单元格粘贴是每个单元格周围的空间,在单元格之间。有效隔沟是这个值的两倍。

如果这种方法被调用为无值,则单元格粘贴设置为零。

这个电话可以被锁起来。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 是 | 单元格粘贴值 。 |


**返回值:** [Phaser.GameObjects.Grid](/api/class/gameobjects-grid) - 此游戏对象实例 。


> 源码：[src/gameobjects/shape/grid/Grid.js#L198](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/grid/Grid.js#L198)  
引入版本：4.0.0


---

### setStrokeOutside {#setStrokeOutside}

#### \<instance> setStrokeOutside(strokeOutside, [strokeOutsideIncomplete]) {#instance-setstrokeoutsidestrokeoutside-strokeoutsideincomplete}


**说明:**

控制整个网格物体的外周是否被划出中风,除了在细胞间划出线条外,还可以选择控制外周是否被划入部分细胞,即网格维度没有被细胞维度均匀分割,使右侧或底侧的细胞不完全.

这个电话可以被锁起来。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| strokeOutside | boolean | 否 | 是否按下网格对象的外部边缘 。 |
| strokeOutsideIncomplete | boolean | 是 | 单元格不完整时是否将网格对象的外部边缘划动 。 |


> 源码：[src/gameobjects/shape/grid/Grid.js#L219](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/grid/Grid.js#L219)  
引入版本：4.0.0


---

---
