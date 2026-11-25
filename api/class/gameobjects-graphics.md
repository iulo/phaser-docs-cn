# Graphics {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-graphics)

图形对象是绘制游戏原始形状的一种方法。原始对象包括几何形式,如矩形、圆形和多边形。它们还包括线条、弧形和曲线。当你最初创建图形对象时,它将是空的。

要绘制到它,您必须首先指定行样式或填充样式(或两者兼有),使用路径绘制形状,最后填充或中标。例如:

```javascript
graphics.lineStyle(5, 0xFF00FF, 1.0);
graphics.beginPath();
graphics.moveTo(100, 100);
graphics.lineTo(200, 200);
graphics.closePath();
graphics.strokePath();
```

有许多有用的方法可以画和填充/中键常见的形状给您.

```javascript
graphics.lineStyle(5, 0xFF00FF, 1.0);
graphics.fillStyle(0xFFFFFF, 1.0);
graphics.fillRect(50, 50, 400, 200);
graphics.strokeRect(50, 50, 400, 200);
```

当一个图形对象被渲染出来时, 它会根据游戏在 Canvas 或 WebGL 下运行而产生不同的效果。 Canvas 下将使用 HTML Canvas 上下文绘制操作绘制路径。 WebGL 下, 图形数据会分解成多边形。 这两个过程都是昂贵的, 特别是形状复杂的进程 。

如果您的图形对象在绘制形状后没有多少变化( 或者完全改变), 您会调用 [Phaser.GameObjects.Graphics#generateTexture](/api/class/gameobjects-graphics#generateTexture) 来帮助执行。 这将“ 将图形对象” 插入到纹理中, 然后返回它。 您可以使用此纹理来显示 Sprites 或其他显示对象。 如果您的图形对象经常更新, 您应该避免这样做, 因为它会不断生成新的纹理, 它将消耗内存 。

WebGL 下,图形使用它自己的遮光器,用来批量绘图操作。尝试将图形对象组合在一起,以便它们可以被批量。尽可能避免混合对象类型,因为每批都会被冲刷,成本计算性能。

如你所知,图形对象有点相互权衡。虽然它们非常有用,但游戏中需要小心其复杂性和数量。

**构造函数**

`new Graphics(scene, [options])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此图形对象所属景色 。 |
| options | [Phaser.Types.GameObjects.Graphics.Options](/api/typedef/types-gameobjects-graphics#options) | 是 | 设置此图形对象的位置和默认样式的选项。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting)  
> [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask)  
> [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  



> 源码：[src/gameobjects/graphics/Graphics.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L19)  
引入版本：3.0.0

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





**From [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting):**


 - [lighting](/api/namespace/gameobjects-components-lighting#lighting)
 - [selfShadow](/api/namespace/gameobjects-components-lighting#selfShadow)





**From [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask):**


 - [mask](/api/namespace/gameobjects-components-mask#mask)





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

### commandBuffer {#commandBuffer}

#### commandBuffer: array {#commandbuffer-array}


**说明:**

用于渲染图形的命令的阵列 。


> 源码：[src/gameobjects/graphics/Graphics.js#L133](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L133)  
引入版本：3.0.0


---

### defaultFillAlpha {#defaultFillAlpha}

#### defaultFillAlpha: number {#defaultfillalpha-number}


**说明:**

默认填充此图形对象所渲染的形状的α 。 用 `setDefaultStyles()` 设置此值 。


> 源码：[src/gameobjects/graphics/Graphics.js#L155](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L155)  
引入版本：3.0.0


---

### defaultFillColor {#defaultFillColor}

#### defaultFillColor: number {#defaultfillcolor-number}


**说明:**

此图形对象所渲染的形状默认填充颜色。 以 `setDefaultStyles()` 设置此值 。


> 源码：[src/gameobjects/graphics/Graphics.js#L143](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L143)  
引入版本：3.0.0


---

### defaultStrokeAlpha {#defaultStrokeAlpha}

#### defaultStrokeAlpha: number {#defaultstrokealpha-number}


**说明:**

默认的按下此图形对象所渲染的形状的字母。 用 `setDefaultStyles()` 设置此值 。


> 源码：[src/gameobjects/graphics/Graphics.js#L191](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L191)  
引入版本：3.0.0


---

### defaultStrokeColor {#defaultStrokeColor}

#### defaultStrokeColor: number {#defaultstrokecolor-number}


**说明:**

此图形对象所渲染的形状的默认中风颜色。 用 `setDefaultStyles()` 设置此值 。


> 源码：[src/gameobjects/graphics/Graphics.js#L179](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L179)  
引入版本：3.0.0


---

### defaultStrokeWidth {#defaultStrokeWidth}

#### defaultStrokeWidth: number {#defaultstrokewidth-number}


**说明:**

此图形对象所渲染的形状的默认中风宽度。 用 `setDefaultStyles()` 设置此值 。


> 源码：[src/gameobjects/graphics/Graphics.js#L167](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L167)  
引入版本：3.0.0


---

### displayOriginX {#displayOriginX}

#### displayOriginX: number {#displayoriginx-number}


**说明:**

图形的横向显示源 。


> 源码：[src/gameobjects/graphics/Graphics.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L113)  
引入版本：3.0.0


---

### displayOriginY {#displayOriginY}

#### displayOriginY: number {#displayoriginy-number}


**说明:**

图形的垂直显示源 。


> 源码：[src/gameobjects/graphics/Graphics.js#L123](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L123)  
引入版本：3.0.0


---

### pathDetailThreshold {#pathDetailThreshold}

#### pathDetailThreshold: number {#pathdetailthreshold-number}


**说明:**

WebGL渲染器的路径细节阈值,以像素形式表示。路径段将被合并,直到路径完成或线段长度超过阈值。

如果数值为负值,则阈值将从游戏配置`render.pathDetailThreshold`属性中取出.

这个阈值可以大大改善复杂形状上的性能,它是在渲染时间计算出来的,不影响原始路径数据。阈值在屏幕像素中进行评估,因此如果对象被放大,细细细节就会出现.


> 源码：[src/gameobjects/graphics/Graphics.js#L213](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L213)  
引入版本：4.0.0


---

### TargetCamera {#TargetCamera}

#### TargetCamera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#targetcamera-phasercamerasscene2dcamera}


**说明:**

图形系统专门用来渲染纹理的相机.


> 源码：[src/gameobjects/graphics/Graphics.js#L1608](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1608)  
引入版本：3.1.0


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





**From [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting):**


 - [setLighting](/api/namespace/gameobjects-components-lighting#setLighting)
 - [setSelfShadow](/api/namespace/gameobjects-components-lighting#setSelfShadow)





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

### arc {#arc}

#### \<instance> arc(x, y, radius, startAngle, endAngle, [anticlockwise], [overshoot]) {#instance-arcx-y-radius-startangle-endangle-anticlockwise-overshoot}


**说明:**

画一弧.

这种方法可以用来创建圆圈,或者部分圆圈.

在启动弧前请确保拨打`beginPath`,除非您希望弧在填充或中键时自动关闭.

使用可选的 `overshoot` 参数增加在 WebGL 中弧度时发生的重迭数。 如果您绘制的弧度带有特别厚的线条, 这样做会很有用, 因为这样可以让弧度完全加起来。 首先尝试小值, 即 0.01 。

在调用这种方法绘制弧后,拨打[Phaser.GameObjects.Graphics#fillPath](/api/class/gameobjects-graphics#fillPath)或[Phaser.GameObjects.Graphics#strokePath](/api/class/gameobjects-graphics#strokePath).

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 圆中心轴的x坐标. |
| y | number | 否 |  | 圆中心y坐标. |
| radius | number | 否 |  | 圆之半径. |
| startAngle | number | 否 |  | 起点,用弧度表示. |
| endAngle | number | 否 |  | 终点角,用弧度表示. |
| anticlockwise | boolean | 是 | false | 画是逆时针还是顺时针 。 |
| overshoot | number | 是 | 0 | 此值允许您在 WebGL 渲染中增加片段的迭代。 如果弧线有厚的中风, 需要过度射击才能进行合并, 则有用。 请使用 0.01 等小数字开始并视需要增加 。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1285](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1285)  
引入版本：3.0.0


---

### beginPath {#beginPath}

#### \<instance> beginPath() {#instance-beginpath}


**说明:**

启动新形状路径 。


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L422](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L422)  
引入版本：3.0.0


---

### clear {#clear}

#### \<instance> clear() {#instance-clear}


**说明:**

清除命令缓冲器,并将填充样式和行样式重置为默认样式.


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1485](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1485)  
引入版本：3.0.0


---

### closePath {#closePath}

#### \<instance> closePath() {#instance-closepath}


**说明:**

关闭当前路径 。


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L439](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L439)  
引入版本：3.0.0


---

### fill {#fill}

#### \<instance> fill() {#instance-fill}


**说明:**

填充当前路径 。

这是`Graphics.fillPath`的别名, 也做同样的事情。 它被添加到 CanvasRendering Context 2D API 中 。


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L473](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L473)  
引入版本：3.16.0


---

### fillCircle {#fillCircle}

#### \<instance> fillCircle(x, y, radius) {#instance-fillcirclex-y-radius}


**说明:**

以给定的位置和半径填满圆形.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 圆中心轴的x坐标. |
| y | number | 否 | 圆中心y坐标. |
| radius | number | 否 | 圆之半径. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L560](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L560)  
引入版本：3.0.0


---

### fillCircleShape {#fillCircleShape}

#### \<instance> fillCircleShape(circle) {#instance-fillcircleshapecircle}


**说明:**

灌满给定圆.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆入充之. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L530](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L530)  
引入版本：3.0.0


---

### fillEllipse {#fillEllipse}

#### \<instance> fillEllipse(x, y, width, height, [smoothness]) {#instance-fillellipsex-y-width-height-smoothness}


**说明:**

以给定的位置和大小填充椭圆。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 椭圆中心轴的x坐标. |
| y | number | 否 |  | 椭圆中心y坐标. |
| width | number | 否 |  | 椭圆的宽度. |
| height | number | 否 |  | 椭圆形的高度. |
| smoothness | number | 是 | 32 | 绘制椭圆的点数。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1260](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1260)  
引入版本：3.0.0


---

### fillEllipseShape {#fillEllipseShape}

#### \<instance> fillEllipseShape(ellipse, [smoothness]) {#instance-fillellipseshapeellipse-smoothness}


**说明:**

填充给定的椭圆.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 |  | 椭圆以充之. |
| smoothness | number | 是 | 32 | 绘制椭圆的点数。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1240](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1240)  
引入版本：3.0.0


---

### fillGradientStyle {#fillGradientStyle}

#### \<instance> fillGradientStyle(topLeft, topRight, bottomLeft, bottomRight, [alphaTopLeft], [alphaTopRight], [alphaBottomLeft], [alphaBottomRight]) {#instance-fillgradientstyletopleft-topright-bottomleft-bottomright-alphatopleft-alphatopright-alphabottomleft-alphabottomright}


**说明:**

设置一个渐变填充样式。 这是 WebGL 唯一的特性 。

梯度颜色值代表一个未变形矩形的4个角。梯度用于给调用此方法后绘制的所有填充形状和路径配色。如果想要关闭梯度,请调用 `fillStyle`,并提供一个新的填充颜色。

填充三角形时,三角形的3点只使用前3个颜色值。

这个特征最好只在矩形和三角形上使用,所有其他形状都会给出奇异的结果.

注意,对于弧或椭圆等物体,或三角形所制成的任何东西,每个使用的三角形都会单独填充一个梯度,此时没有作为单一实体填充形状或路径的能力.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| topLeft | number | 否 |  | 左上方填充颜色. |
| topRight | number | 否 |  | 右上方填色(见"御览"). |
| bottomLeft | number | 否 |  | 左下方填色(   ) 。 |
| bottomRight | number | 否 |  | 右下方填充颜色。 填充三角形时不使用 。 |
| alphaTopLeft | number | 是 | 1 | 上方左侧的α值。 如果您只给出这个值, 它会用于所有角落 。 |
| alphaTopRight | number | 是 | 1 | 右上方的α值。 |
| alphaBottomLeft | number | 是 | 1 | 下方左侧为α值 。 |
| alphaBottomRight | number | 是 | 1 | 右下方的α值 。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L338](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L338)  
引入版本：3.12.0


---

### fillPath {#fillPath}

#### \<instance> fillPath() {#instance-fillpath}


**说明:**

填充当前路径 。


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L456](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L456)  
引入版本：3.0.0


---

### fillPoint {#fillPoint}

#### \<instance> fillPoint(x, y, [size]) {#instance-fillpointx-y-size}


**说明:**

填入指定位置的点数 。

默认情况下在给定位置绘制一个方形,大小为1像素。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 点的x坐标. |
| y | number | 否 |  | 点的y坐标. |
| size | number | 是 | 1 | 方丈大小画. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L905](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L905)  
引入版本：3.0.0


---

### fillPoints {#fillPoints}

#### \<instance> fillPoints(points, [closeShape], [closePath], [endIndex]) {#instance-fillpointspoints-closeshape-closepath-endindex}


**说明:**

填充指定数组点所代表的形状。

通过`closeShape`通过加入最后一个到第一个点来自动关闭形状.

通过 `closePath` 在填充前自动关闭路径 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| points | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 否 |  | 补分. |
| closeShape | boolean | 是 | false | 当`true`时,形状通过加入最后一点到第一点而关闭. |
| closePath | boolean | 是 | false | `true`时,在填充前,路径关闭. |
| endIndex | number | 是 |  | `points`的索引可以停止,默认为`points.length`. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1148](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1148)  
引入版本：3.0.0


---

### fillPointShape {#fillPointShape}

#### \<instance> fillPointShape(point, [size]) {#instance-fillpointshapepoint-size}


**说明:**

灌满给定点.

默认情况下在给定位置绘制一个方形,大小为1像素。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 |  | 补之之点. |
| size | number | 是 | 1 | 方丈大小画. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L887](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L887)  
引入版本：3.0.0


---

### fillRect {#fillRect}

#### \<instance> fillRect(x, y, width, height) {#instance-fillrectx-y-width-height}


**说明:**

以给定的位置和大小填充矩形 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 矩形左上角的x坐标. |
| y | number | 否 | 矩形左上方的y坐标. |
| width | number | 否 | 矩形的宽度 。 |
| height | number | 否 | 长方形的高度. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L632](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L632)  
引入版本：3.0.0


---

### fillRectShape {#fillRectShape}

#### \<instance> fillRectShape(rect) {#instance-fillrectshaperect}


**说明:**

填充给定的矩形.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 以矩为填. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L602](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L602)  
引入版本：3.0.0


---

### fillRoundedRect {#fillRoundedRect}

#### \<instance> fillRoundedRect(x, y, width, height, [radius]) {#instance-fillroundedrectx-y-width-height-radius}


**说明:**

将圆形矩形填充到给定的位置,大小和半径.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 矩形左上角的x坐标. |
| y | number | 否 |  | 矩形左上方的y坐标. |
| width | number | 否 |  | 矩形的宽度 。 |
| height | number | 否 |  | 长方形的高度. |
| radius | [Phaser.Types.GameObjects.Graphics.RoundedRectRadius](/api/typedef/types-gameobjects-graphics#roundedrectradius) \| number | 是 | 20 | 角半径; 也可以是指定角的不同半径的对象. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L697](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L697)  
引入版本：3.11.0


---

### fillStyle {#fillStyle}

#### \<instance> fillStyle(color, [alpha]) {#instance-fillstylecolor-alpha}


**说明:**

设置当前填充样式。 用于所有“ 填充” 相关的函数 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| color | number | 否 |  | 补色. |
| alpha | number | 是 | 1 | 填充的阿尔法。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L315](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L315)  
引入版本：3.0.0


---

### fillTriangle {#fillTriangle}

#### \<instance> fillTriangle(x0, y0, x1, y1, x2, y2) {#instance-filltrianglex0-y0-x1-y1-x2-y2}


**说明:**

以给定的点填充三角形。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x0 | number | 否 | 第一点的x坐标. |
| y0 | number | 否 | 第一点的y坐标 |
| x1 | number | 否 | 第二点的x坐标. |
| y1 | number | 否 | 第二点的y坐标. |
| x2 | number | 否 | 第三点的x坐标. |
| y2 | number | 否 | 第三点的y坐标 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L969](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L969)  
引入版本：3.0.0


---

### fillTriangleShape {#fillTriangleShape}

#### \<instance> fillTriangleShape(triangle) {#instance-filltriangleshapetriangle}


**说明:**

填充给定三角形.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角形要填满. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L939](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L939)  
引入版本：3.0.0


---

### generateTexture {#generateTexture}

#### \<instance> generateTexture(key, [width], [height]) {#instance-generatetexturekey-width-height}


**说明:**

从此图形对象生成纹理 。

如果 `key` 是串, 它会生成一个新的纹理 使用它, 并添加到纹理管理器( 假设没有发生密钥冲突) 。

如果 `key` 是 Canvas , 它会将图形绘制到画布上下文。 请注意, 它不会以 WebGL 模式自动上传到 GPU 。

请理解纹理是通过浏览器的Canvas API创建的,因此一些图形功能,如`fillGradientStyle`,不会出现在由此产生的纹理上,因为它们不受Canvas ABI的支持.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| HTMLCanvasElement | 否 | 将纹理存储在纹理管理器中的密钥, 或要绘制的 Canvas 。 |
| width | number | 是 | 要生成的图形宽度 。 |
| height | number | 是 | 要生成的图形高度 。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1510](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1510)  
引入版本：3.0.0


---

### lineBetween {#lineBetween}

#### \<instance> lineBetween(x1, y1, x2, y2) {#instance-linebetweenx1-y1-x2-y2}


**说明:**

在给定点之间画一条线。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x1 | number | 否 | 线起点的x坐标. |
| y1 | number | 否 | 线的起点的y坐标. |
| x2 | number | 否 | 线的终点的x坐标. |
| y2 | number | 否 | 线的终点的y坐标. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1034](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1034)  
引入版本：3.0.0


---

### lineGradientStyle {#lineGradientStyle}

#### \<instance> lineGradientStyle(lineWidth, topLeft, topRight, bottomLeft, bottomRight, [alpha]) {#instance-linegradientstylelinewidth-topleft-topright-bottomleft-bottomright-alpha}


**说明:**

设置梯度线条样式。 这是 WebGL 唯一的特性 。

梯度颜色值代表一个未变形矩形的4个角。梯度用于给调用此方法后绘制的所有中线形状和路径配色。如果想要关闭梯度,请调用 `lineStyle`,并提供新的单行颜色。

此特性最好只在单行中使用,所有其他形状都会给出奇异的结果.

请注意,对于弧或椭圆等物体,或者三角形所制成的任何东西,每个三角形都会被自己加一个梯度,此时没有将形状或路径作为单一实体进行梯度中滑的能力.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| lineWidth | number | 否 |  | 中风宽度。 |
| topLeft | number | 否 |  | 梯度左上角的中风颜色。 |
| topRight | number | 否 |  | 梯度右上角的中风颜色。 |
| bottomLeft | number | 否 |  | 梯度左下角的中风颜色。 |
| bottomRight | number | 否 |  | 梯度右下角的中风颜色。 |
| alpha | number | 是 | 1 | 填充的阿尔法。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L384](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L384)  
引入版本：3.12.0


---

### lineStyle {#lineStyle}

#### \<instance> lineStyle(lineWidth, color, [alpha]) {#instance-linestylelinewidth-color-alpha}


**说明:**

设置当前行样式。 用于所有“ 中程” 相关函数 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| lineWidth | number | 否 |  | 中风宽度。 |
| color | number | 否 |  | 中风颜色. |
| alpha | number | 是 | 1 | 中风的α。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L289)  
引入版本：3.0.0


---

### lineTo {#lineTo}

#### \<instance> lineTo(x, y) {#instance-linetox-y}


**说明:**

从当前绘图位置绘制到给定位置的线条。

将当前绘图位置移到给定位置。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 坐标x来划线到. |
| y | number | 否 | 坐标是Y 线到。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1057](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1057)  
引入版本：3.0.0


---

### moveTo {#moveTo}

#### \<instance> moveTo(x, y) {#instance-movetox-y}


**说明:**

将当前绘图位置移到给定位置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 坐标是x的坐标 |
| y | number | 否 | 移动到Y坐标处。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1080](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1080)  
引入版本：3.0.0


---

### preDestroy {#preDestroy}

#### \<instance> preDestroy() {#instance-predestroy}


**说明:**

内部破坏处理器,作为破坏过程的一部分而叫作.


**Access:** 保护


> 源码：[src/gameobjects/graphics/Graphics.js#L1594](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1594)  
引入版本：3.9.0


---

### restore {#restore}

#### \<instance> restore() {#instance-restore}


**说明:**

恢复最近保存的图形状态, 方法是从状态堆栈中跳出。

使用 [Phaser.GameObjects.Graphics#save](/api/class/gameobjects-graphics#save) 来保存当前状态, 并在之后调用此功能来恢复该状态 。

如果没有保存状态,此命令将无所作为.


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1384](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1384)  
引入版本：3.0.0


---

### rotateCanvas {#rotateCanvas}

#### \<instance> rotateCanvas(radians) {#instance-rotatecanvasradians}


**说明:**

在此图形对象命令缓冲器中插入旋转命令。

绘制到 _after_ 的所有对象, 调用此方法, 都会被给定的量旋转 。

这不会改变图形对象本身的旋转,只改变它调用这种方法后绘制的对象的旋转.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| radians | number | 否 | 旋转角度,以弧度表示. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1459](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1459)  
引入版本：3.0.0


---

### save {#save}

#### \<instance> save() {#instance-save}


**说明:**

通过将当前状态推向堆栈来保存图形状态。

然后,可以使用[Phaser.GameObjects.Graphics#restore](/api/class/gameobjects-graphics#restore)恢复最近保存的状态。


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1365](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1365)  
引入版本：3.0.0


---

### scaleCanvas {#scaleCanvas}

#### \<instance> scaleCanvas(x, y) {#instance-scalecanvasx-y}


**说明:**

在此图形对象命令缓冲器中插入一个缩放命令。

所有绘制的_after_调用此方法的对象,都将按给定的量缩放。

这不会改变图形对象本身的尺度,只改变它调用这种方法后绘制的对象的尺度.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 水平尺度应用. |
| y | number | 否 | 垂直比例表可适用。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1432](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1432)  
引入版本：3.0.0


---

### setDefaultStyles {#setDefaultStyles}

#### \<instance> setDefaultStyles(options) {#instance-setdefaultstylesoptions}


**说明:**

设置此图形对象的默认样式设置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| options | [Phaser.Types.GameObjects.Graphics.Styles](/api/typedef/types-gameobjects-graphics#styles) | 否 | 设置为默认的样式 。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L257](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L257)  
引入版本：3.0.0


---

### slice {#slice}

#### \<instance> slice(x, y, radius, startAngle, endAngle, [anticlockwise], [overshoot]) {#instance-slicex-y-radius-startangle-endangle-anticlockwise-overshoot}


**说明:**

创建以 `x` 和 `y` 为中心的饼图切片形状, 并设定半径。 您必须定义切片的起始和结尾角度 。

设置 `anticlockwise` 参数为 `true` 创建类似 Pacman 的形状。 设置为 `false` 创建类似 片派 的形状 。

这种方法将启动一条新路径, 并在它结尾关闭路径。 要显示您需要使用 `strokePath` 或 `fillPath` 来命名它 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 切片的横向中心. |
| y | number | 否 |  | 切片的垂直中心. |
| radius | number | 否 |  | 切片的半径. |
| startAngle | number | 否 |  | 切片的起始角度,以弧度表示. |
| endAngle | number | 否 |  | 切片的端角,以弧度表示. |
| anticlockwise | boolean | 是 | false | 画是逆时针还是顺时针 。 |
| overshoot | number | 是 | 0 | 此值允许您用此量来过度射击 endAngle 。 如果弧线有厚的中风, 需要过度射击才能进行合并 。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1326](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1326)  
引入版本：3.4.0


---

### stroke {#stroke}

#### \<instance> stroke() {#instance-stroke}


**说明:**

划断当前路径 。

这是`Graphics.strokePath`的别名, 也做同样的事情。 它被添加到 CanvasRendering Context 2D API 中 。


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L510](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L510)  
引入版本：3.16.0


---

### strokeCircle {#strokeCircle}

#### \<instance> strokeCircle(x, y, radius) {#instance-strokecirclex-y-radius}


**说明:**

以给定的位置和半径打出一个圆形.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 圆中心轴的x坐标. |
| y | number | 否 | 圆中心y坐标. |
| radius | number | 否 | 圆之半径. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L581](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L581)  
引入版本：3.0.0


---

### strokeCircleShape {#strokeCircleShape}

#### \<instance> strokeCircleShape(circle) {#instance-strokecircleshapecircle}


**说明:**

划出给定的圆圈.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 圆向中风. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L545](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L545)  
引入版本：3.0.0


---

### strokeEllipse {#strokeEllipse}

#### \<instance> strokeEllipse(x, y, width, height, [smoothness]) {#instance-strokeellipsex-y-width-height-smoothness}


**说明:**

以给定的位置和大小打出椭圆 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 椭圆中心轴的x坐标. |
| y | number | 否 |  | 椭圆中心y坐标. |
| width | number | 否 |  | 椭圆的宽度. |
| height | number | 否 |  | 椭圆形的高度. |
| smoothness | number | 是 | 32 | 绘制椭圆的点数。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1215](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1215)  
引入版本：3.0.0


---

### strokeEllipseShape {#strokeEllipseShape}

#### \<instance> strokeEllipseShape(ellipse, [smoothness]) {#instance-strokeellipseshapeellipse-smoothness}


**说明:**

划出给定的椭圆形.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 |  | 椭圆至中风. |
| smoothness | number | 是 | 32 | 绘制椭圆的点数。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1195](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1195)  
引入版本：3.0.0


---

### strokeLineShape {#strokeLineShape}

#### \<instance> strokeLineShape(line) {#instance-strokelineshapeline}


**说明:**

绘制给定的线条 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 中风的线条. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1019](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1019)  
引入版本：3.0.0


---

### strokePath {#strokePath}

#### \<instance> strokePath() {#instance-strokepath}


**说明:**

划断当前路径 。


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L493](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L493)  
引入版本：3.0.0


---

### strokePoints {#strokePoints}

#### \<instance> strokePoints(points, [closeShape], [closePath], [endIndex]) {#instance-strokepointspoints-closeshape-closepath-endindex}


**说明:**

划出以给定的点数组为代表的形状。

通过`closeShape`通过加入最后一个到第一个点来自动关闭形状.

通过 `closePath` 在被中键前自动关闭路径 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| points | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 否 |  | 指中风. |
| closeShape | boolean | 是 | false | 当`true`时,形状通过加入最后一点到第一点而关闭. |
| closePath | boolean | 是 | false | 当`true`时,在被中风之前,路径被关闭. |
| endIndex | number | 是 |  | `points`的索引停止绘制。默认为`points.length` 。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1101)  
引入版本：3.0.0


---

### strokeRect {#strokeRect}

#### \<instance> strokeRect(x, y, width, height) {#instance-strokerectx-y-width-height}


**说明:**

以给定的位置和大小划出一个矩形 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 矩形左上角的x坐标. |
| y | number | 否 | 矩形左上方的y坐标. |
| width | number | 否 | 矩形的宽度 。 |
| height | number | 否 | 长方形的高度. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L655](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L655)  
引入版本：3.0.0


---

### strokeRectShape {#strokeRectShape}

#### \<instance> strokeRectShape(rect) {#instance-strokerectshaperect}


**说明:**

划出给定的矩形.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩向中风. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L617](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L617)  
引入版本：3.0.0


---

### strokeRoundedRect {#strokeRoundedRect}

#### \<instance> strokeRoundedRect(x, y, width, height, [radius]) {#instance-strokeroundedrectx-y-width-height-radius}


**说明:**

以给定的位置,大小和半径划出圆形矩形.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 矩形左上角的x坐标. |
| y | number | 否 |  | 矩形左上方的y坐标. |
| width | number | 否 |  | 矩形的宽度 。 |
| height | number | 否 |  | 长方形的高度. |
| radius | [Phaser.Types.GameObjects.Graphics.RoundedRectRadius](/api/typedef/types-gameobjects-graphics#roundedrectradius) \| number | 是 | 20 | 角半径;也可以是指定角不同弧度的对象. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L789](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L789)  
引入版本：3.11.0


---

### strokeTriangle {#strokeTriangle}

#### \<instance> strokeTriangle(x0, y0, x1, y1, x2, y2) {#instance-stroketrianglex0-y0-x1-y1-x2-y2}


**说明:**

以给定的点划出三角形 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x0 | number | 否 | 第一点的x坐标. |
| y0 | number | 否 | 第一点的y坐标 |
| x1 | number | 否 | 第二点的x坐标. |
| y1 | number | 否 | 第二点的y坐标. |
| x2 | number | 否 | 第三点的x坐标. |
| y2 | number | 否 | 第三点的y坐标 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L994](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L994)  
引入版本：3.0.0


---

### strokeTriangleShape {#strokeTriangleShape}

#### \<instance> strokeTriangleShape(triangle) {#instance-stroketriangleshapetriangle}


**说明:**

划出三角形 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 三角形至中风. |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L954](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L954)  
引入版本：3.0.0


---

### translateCanvas {#translateCanvas}

#### \<instance> translateCanvas(x, y) {#instance-translatecanvasx-y}


**说明:**

在此图形对象命令缓冲器中插入翻译命令。

所有绘制的_after_调用此方法的对象,都将按给定的量翻译 。

这不会改变图形对象本身的位置,只改变它调用这种方法后绘制的对象的位置.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 横向翻译要应用. |
| y | number | 否 | 应用的垂直翻译 。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 此游戏对象 。


> 源码：[src/gameobjects/graphics/Graphics.js#L1405](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/Graphics.js#L1405)  
引入版本：3.0.0


---

---
