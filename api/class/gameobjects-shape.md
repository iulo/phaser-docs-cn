# Shape {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-shape)

形状游戏对象是各种内置形状类型的基础类,如Arc,Star,Polygon,矩形,三角形等,它为管理填充色,中风色,线宽,以及渲染时使用的预计算路径数据提供了共同的界面.

您不能直接在您的场景中添加形状。 相反, 请使用一个内置子类, 或者扩展此类, 以创建您自己的自定义形状类型, 并使用它们自己的几何逻辑 。

形状对象在 WebGL 中渲染时与 Graphics 游戏对象共享相同的渲染批次。它们不支持梯度、路径平滑阈值或其他高级图形特性。它们反过来会存储预计算的内部几何数据,使其比动态构造的图形对象更有效率。

**构造函数**

`new Shape(scene, [type], [data])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| 类型 | string | 是 | 形状的内部类型. |
| data | any | 是 | 源数据形状几何,如果有的话. |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.GetBounds](/api/namespace/gameobjects-components-getbounds)  
> [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask)  
> [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin)  
> [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/shape/Shape.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L13)  
引入版本：3.13.0

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




---

## 公开方法 {#public-methods}

### preDestroy {#preDestroy}

#### \<instance> preDestroy() {#instance-predestroy}


**说明:**

内部破坏处理器,作为破坏过程的一部分而叫作.


**Access:** 保护


> 源码：[src/gameobjects/shape/Shape.js#L391](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L391)  
引入版本：3.13.0


---

### setClosePath {#setClosePath}

#### \<instance> setClosePath(value) {#instance-setclosepathvalue}


**说明:**

设定此形状路径在中键渲染时是否关闭 。 注意一些形状总是在中键时关闭( 如椭圆形状) 。

这个电话可以被锁起来。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 如果按下时形状应该关闭, 则设定为 `true`, 否则则设置为 `false` 。 |


**返回值:** [Phaser.GameObjects.Shape](/api/class/gameobjects-shape) - 此游戏对象实例 。


> 源码：[src/gameobjects/shape/Shape.js#L320](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L320)  
引入版本：3.13.0


---

### setDisplaySize {#setDisplaySize}

#### \<instance> setDisplaySize(width, height) {#instance-setdisplaysizewidth-height}


**说明:**

通过调整形状的显示像素大小来设定此形状的大小 `scaleX` 财务报告和已审计财务报表 `scaleY` 属性相对于其本地宽度和高度。这相当于调用 `setScale` 但允许您指定像素中想要的渲染维度,而不是比例乘数。

这个电话可以被锁起来。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 此形状的显示宽度, 以像素为单位 。 |
| height | number | 否 | 此形状的显示高度, 以像素形式显示 。 |


**返回值:** [Phaser.GameObjects.Shape](/api/class/gameobjects-shape) - 这个形状的例子。


> 源码：[src/gameobjects/shape/Shape.js#L368](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L368)  
引入版本：3.53.0


---

### setFillStyle {#setFillStyle}

#### \<instance> setFillStyle([color], [alpha]) {#instance-setfillstylecolor-alpha}


**说明:**

设置此形状的填充颜色和字母 。

如果您希望形状不被填充, 请使用这种方法, 无需参数, 或者将 `isFilled` 设置为 `false` 。

注意一些形状不支持填充颜色,例如行形状.

这个电话可以被锁起来。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| color | number | 是 |  | 填充此形状所用的颜色。 如果不提供形状, 则不会填充 。 |
| alpha | number | 是 | 1 | 如果给填充颜色, 填充此形状时所用的α值 。 |


**返回值:** [Phaser.GameObjects.Shape](/api/class/gameobjects-shape) - 此游戏对象实例 。


> 源码：[src/gameobjects/shape/Shape.js#L248](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L248)  
引入版本：3.13.0


---

### setStrokeStyle {#setStrokeStyle}

#### \<instance> setStrokeStyle([lineWidth], [color], [alpha]) {#instance-setstrokestylelinewidth-color-alpha}


**说明:**

设置此形状的中风颜色和α 。

如果您不希望形状被中键, 那就使用这种方法, 没有参数, 或者将 `isStroked` 设置为 `false` 。

注意一些形状不支持被中键,例如Iso Box形状.

这个电话可以被锁起来。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| lineWidth | number | 是 |  | 中键的线宽。 如果不提供或未定义形状, 将不会中键 。 |
| color | number | 是 |  | 用于中转此形状的颜色。 如果不提供形状, 则不会被中转 。 |
| alpha | number | 是 | 1 | 如果给定了中风颜色, 拖动此形状时所用的α值 。 |


**返回值:** [Phaser.GameObjects.Shape](/api/class/gameobjects-shape) - 此游戏对象实例 。


> 源码：[src/gameobjects/shape/Shape.js#L283](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L283)  
引入版本：3.13.0


---

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




---

## 公开成员 {#public-members}

### closePath {#closePath}

#### closePath: boolean {#closepath-boolean}


**说明:**

如果此形状路径在中风时渲染时关闭, 控制会关闭 。 请注意, 有些形状在中风时总是关闭( 如椭圆形状) 。


> 源码：[src/gameobjects/shape/Shape.js#L175](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L175)  
引入版本：3.13.0


---

### displayHeight {#displayHeight}

#### displayHeight: number {#displayheight-number}


**说明:**

此游戏对象的显示高度 。

这一数值考虑到了比额表系数。

设置此值将调整游戏对象的缩放属性 。


> 源码：[src/gameobjects/shape/Shape.js#L431](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L431)  
引入版本：3.13.0


---

### displayWidth {#displayWidth}

#### displayWidth: number {#displaywidth-number}


**说明:**

此游戏对象的显示宽度 。

这一数值考虑到了比额表系数。

设置此值将调整游戏对象的缩放属性 。


> 源码：[src/gameobjects/shape/Shape.js#L406](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L406)  
引入版本：3.13.0


---

### fillAlpha {#fillAlpha}

#### fillAlpha: number {#fillalpha-number}


**说明:**

α应用到此形状的填充, 范围在 0( 完全透明) 到 1( 完全不透明) 之间。 只有在 `isFilled` 时才使用 `true`. 通过 `setFillStyle` 设定 。


> 源码：[src/gameobjects/shape/Shape.js#L115](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L115)  
引入版本：3.13.0


---

### fillColor {#fillColor}

#### fillColor: number {#fillcolor-number}


**说明:**

此形状所用的填充颜色, 作为六进制值( 如 0xff000 表示红色) 。 只有在 `isFilled` 时才使用 `true`。 通过 `setFillStyle` 设定 。


> 源码：[src/gameobjects/shape/Shape.js#L105](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L105)  
引入版本：3.13.0


---

### geom {#geom}

#### geom: any {#geom-any}


**说明:**

源形状数据。 通常是一个几何对象。 您不应该直接操纵它 。


> 源码：[src/gameobjects/shape/Shape.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L74)  
引入版本：3.13.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

此游戏对象的原生高度( 未标定) 。

更改此值不会改变游戏对象在游戏中显示的大小。 为此, 您需要设置游戏对象( `setScale`) 的大小, 或者使用 `displayHeight` 属性 。


> 源码：[src/gameobjects/shape/Shape.js#L209](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L209)  
引入版本：3.0.0


---

### isFilled {#isFilled}

#### isFilled: boolean {#isfilled-boolean}


**说明:**

如果此形状是否填充, 控制。 请注意, 有些形状不支持填充( 如行形状)


> 源码：[src/gameobjects/shape/Shape.js#L155](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L155)  
引入版本：3.13.0


---

### isStroked {#isStroked}

#### isStroked: boolean {#isstroked-boolean}


**说明:**

如果此形状被按下或不按下, 控制。 请注意, 有些形状不支持按下( 如 Iso Box 形状)


> 源码：[src/gameobjects/shape/Shape.js#L165](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L165)  
引入版本：3.13.0


---

### lineWidth {#lineWidth}

#### lineWidth: number {#linewidth-number}


**说明:**

此形状的中风线宽度, 以像素为单位。 仅在 `isStroked` 使用 `true` 时才使用。 通过 `setStrokeStyle` 设定 。


> 源码：[src/gameobjects/shape/Shape.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L145)  
引入版本：3.13.0


---

### pathData {#pathData}

#### pathData: Array.\<number> {#pathdata-arraynumber}


**说明:**

持有多边形路径数据进行填充渲染。


> 源码：[src/gameobjects/shape/Shape.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L85)  
引入版本：3.13.0


---

### pathIndexes {#pathIndexes}

#### pathIndexes: Array.\<number> {#pathindexes-arraynumber}


**说明:**

持有用于填充渲染的耳剪多边形路径索引数据。


> 源码：[src/gameobjects/shape/Shape.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L95)  
引入版本：3.13.0


---

### strokeAlpha {#strokeAlpha}

#### strokeAlpha: number {#strokealpha-number}


**说明:**

α 适用于此形状的中风, 范围在 0( 完全透明) 到 1( 完全不透明) 之间。 只有在 `isStroked` 时才使用 `true` 。 通过 `setStrokeStyle` 设定 。


> 源码：[src/gameobjects/shape/Shape.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L135)  
引入版本：3.13.0


---

### strokeColor {#strokeColor}

#### strokeColor: number {#strokecolor-number}


**说明:**

此形状所用的中风颜色, 作为六进制值( 如 0x00ff00 for green) 。 仅当使用时 。 `isStroked` 谓 `true`设置。 `setStrokeStyle`.


> 源码：[src/gameobjects/shape/Shape.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L125)  
引入版本：3.13.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

此游戏对象的原生( 未标定) 宽度 。

更改此值不会改变游戏对象在游戏中显示的大小。 为此, 您需要设置游戏对象( `setScale`) 的大小, 或者使用 `displayWidth` 属性 。


> 源码：[src/gameobjects/shape/Shape.js#L196](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/Shape.js#L196)  
引入版本：3.13.0


---

---
