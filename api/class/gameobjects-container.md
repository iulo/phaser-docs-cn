# Container {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-container)

集装箱游戏对象。

容器,如其名称所暗示的,可以“包含”其他类型的游戏对象。当一个游戏对象被添加到容器中时,容器将承担渲染责任。默认它将从显示列表中删除,而是添加到容器内部列表中。

游戏对象的位置会自动与容器的位置相对.

集装箱的转换点是 0x0(在本地空间),不能改变。您添加到集装箱中的儿童应该铭记这一价值。即您应当将 0x0 视为集装箱的中心,并根据需要将儿童置于集装箱周围。

集装箱的制造过程也按集装箱内存在的顺序进行所有儿童,集装箱儿童可以采用`MoveUp`、`MoveDown`和`SendToBack`等方法重新定位。

如果修改集装箱的变换地产,例如`Container.x`或`Container.rotation`,那么它也会自动影响所有儿童。

集装箱可以包括用于深层嵌入式变压器的其他集装箱.

集装箱上可以设置口罩,也可以用作口罩,因为口罩是过滤器,集装箱的孩子也可以有口罩,集装箱的口罩会被应用到顶端,在Canvas渲染中,只有集装箱的口罩才会被应用.

容器可以允许输入。由于它们没有纹理,所以需要提供形状,以便用作攻击区。集装箱儿童也可以允许输入,独立于集装箱。

如果输入允许 _ child_,则不应同时设置`origin`和**负**比例系数,否则输入区域会错位。

容器可以被赋予一个物理体,用于弧形物理、撞击物理或物质物理。但是,如果容器_儿童_被允许用于物理,那么,如果容器本身或其祖先在除0x0以外的任何地方定位,则可能会得到意外的结果,例如抵消体。 集装箱中的物理儿童由于需要过多的额外计算而不计入容器。 请为围绕这个游戏进行游戏的结构安排。

了解使用集装箱的影响很重要。它们会给每个孩子增加额外的处理费用。你越是窝住他们,成本就越高。对于输入事件来说尤其如此。你还失去了以与那些不在集装箱内的儿童一样灵活的方式确定集装箱儿童的显示深度的能力。简言之,不要为了它而使用集装箱。每次你创建一个容器,都要付出小的代价,尽量在可能的地方避免这样做。

**构造函数**

`new Container(scene, [x], [y], [children])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| children | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 是 |  | 游戏对象的可选阵列, 添加到此容器中 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/container/Container.js#L22](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L22)  
引入版本：3.4.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle):**


 - [alpha](/api/namespace/gameobjects-components-alphasingle#alpha)





**From [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode):**


 - [blendMode](/api/namespace/gameobjects-components-blendmode#blendMode)





**From [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize):**


 - [displayHeight](/api/namespace/gameobjects-components-computedsize#displayHeight)
 - [displayWidth](/api/namespace/gameobjects-components-computedsize#displayWidth)
 - [height](/api/namespace/gameobjects-components-computedsize#height)
 - [width](/api/namespace/gameobjects-components-computedsize#width)





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

### displayOriginX {#displayOriginX}

#### displayOriginX: number {#displayoriginx-number}


**说明:**

允许容器用于输入和物理的内部值。 请不要改变此值, 它除了断裂东西之外没有其他效果 。


> 源码：[src/gameobjects/container/Container.js#L289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L289)  
引入版本：3.4.0


---

### displayOriginY {#displayOriginY}

#### displayOriginY: number {#displayoriginy-number}


**说明:**

允许容器用于输入和物理的内部值。 请不要改变此值, 它除了断裂东西之外没有其他效果 。


> 源码：[src/gameobjects/container/Container.js#L308](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L308)  
引入版本：3.4.0


---

### exclusive {#exclusive}

#### exclusive: boolean {#exclusive-boolean}


**说明:**

这个集装箱是否专门管理孩子?

默认为`true`,这意味着加入这个集装箱的儿童不能属于另一个集装箱,其中包括场景显示列表。

如果您关闭了此选项, 这个容器将不再完全管理它的孩子。 这样可以创建各种有趣的图形效果, 例如复制游戏对象而不在场景中重新显示它们。 然而, 这样做会阻止儿童接收任何类型的输入事件, 或者让物理体默认工作, 因为它们不再是显示列表中的单一实体, 而是被复制到任何容器所在的地方。


> 源码：[src/gameobjects/container/Container.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L116)  
引入版本：3.4.0


---

### first {#first}

#### first: [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) {#first-phasergameobjectsgameobject}


**说明:**

返回容器内的第一个游戏对象, 如果是空的, 则返回 `null` 。

你可以通过拨打`Container.next`和`Container.previous`来移动光标.


> 源码：[src/gameobjects/container/Container.js#L1339](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1339)  
引入版本：3.4.0


---

### last {#last}

#### last: [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) {#last-phasergameobjectsgameobject}


**说明:**

返回容器内的最后一个游戏对象, 如果是空的, 则返回 `null` 。

你可以通过拨打`Container.next`和`Container.previous`来移动光标.


> 源码：[src/gameobjects/container/Container.js#L1367](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1367)  
引入版本：3.4.0


---

### length {#length}

#### length: number {#length-number}


**说明:**

此容器内游戏对象的数量 。


> 源码：[src/gameobjects/container/Container.js#L1322](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1322)  
引入版本：3.4.0


---

### list {#list}

#### list: Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> {#list-arrayphasergameobjectsgameobject}


**说明:**

装有这个集装箱的孩子们的阵列。


> 源码：[src/gameobjects/container/Container.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L107)  
引入版本：3.4.0


---

### localTransform {#localTransform}

#### localTransform: [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) {#localtransform-phasergameobjectscomponentstransformmatrix}


**说明:**

用于本地空间转换的内部变换矩阵 。


> 源码：[src/gameobjects/container/Container.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L158)  
引入版本：3.4.0


---

### maxSize {#maxSize}

#### maxSize: number {#maxsize-number}


**说明:**

容器可以有可选的最大尺寸。如果设置在0以上,将限制在容器中添加新的游戏对象,从而将容器的最大尺寸限制在最大限度之外。


> 源码：[src/gameobjects/container/Container.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L136)  
引入版本：3.4.0


---

### next {#next}

#### next: [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) {#next-phasergameobjectsgameobject}


**说明:**

返回容器内的下一个游戏对象,如果是空的,则返回 `null` 。

你可以通过拨打`Container.next`和`Container.previous`来移动光标.


> 源码：[src/gameobjects/container/Container.js#L1395](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1395)  
引入版本：3.4.0


---

### originX {#originX}

#### originX: number {#originx-number}


**说明:**

允许容器用于输入和物理的内部值。 请不要改变此值, 它除了断裂东西之外没有其他效果 。


> 源码：[src/gameobjects/container/Container.js#L251](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L251)  
引入版本：3.4.0


---

### originY {#originY}

#### originY: number {#originy-number}


**说明:**

允许容器用于输入和物理的内部值。 请不要改变此值, 它除了断裂东西之外没有其他效果 。


> 源码：[src/gameobjects/container/Container.js#L270](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L270)  
引入版本：3.4.0


---

### position {#position}

#### position: number {#position-number}


**说明:**

用来通过集装箱儿童通过下列方法进行流动的内部光标位置: `first`, `next`, `previous` 财务报告和已审计财务报表 `last`.


> 源码：[src/gameobjects/container/Container.js#L148](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L148)  
引入版本：3.4.0


---

### previous {#previous}

#### previous: [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) {#previous-phasergameobjectsgameobject}


**说明:**

返回容器内先前的游戏对象, 如果是空的, 则返回 `null` 。

你可以通过拨打`Container.next`和`Container.previous`来移动光标.


> 源码：[src/gameobjects/container/Container.js#L1423](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1423)  
引入版本：3.4.0


---

### scrollFactorX {#scrollFactorX}

#### scrollFactorX: number {#scrollfactorx-number}


**说明:**

这个容器的横向滚动因子 。

滚动因子控制着相机对这个集装箱的移动影响。

当相机滚动时,它会改变屏幕上该容器的制造地点,不会改变容器的实际位置值。

对于一个集装箱,设定这个值只会更新集装箱本身,而不是更新其子女。如果您也想要更改儿童的scrollFactor,请使用`setScrollFactor`方法。

1 值表示它会和相机同步移动。 0 值表示它不会移动, 即使相机移动。 其他值控制了相机移动到这个容器的程度 。

请注意,在计算物理碰撞时,不考虑1以外的滚动因子值。天体总是会根据其世界位置碰撞,但改变滚动因子是对纹理的渲染地的视觉调整,如果在您的代码中没有说明,则可以从物理体中抵消。


> 源码：[src/gameobjects/container/Container.js#L187](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L187)  
引入版本：3.4.0


---

### scrollFactorY {#scrollFactorY}

#### scrollFactorY: number {#scrollfactory-number}


**说明:**

此容器的垂直滚动因子 。

滚动因子控制着相机对这个集装箱的移动影响。

当相机滚动时,它会改变屏幕上该容器的制造地点,不会改变容器的实际位置值。

对于一个集装箱,设定这个值只会更新集装箱本身,而不是更新其子女。如果您也想要更改儿童的scrollFactor,请使用`setScrollFactor`方法。

1 值表示它会和相机同步移动。 0 值表示它不会移动, 即使相机移动。 其他值控制了相机移动到这个容器的程度 。

请注意,在计算物理碰撞时,不考虑1以外的滚动因子值。天体总是会根据其世界位置碰撞,但改变滚动因子是对纹理的渲染地的视觉调整,如果在您的代码中没有说明,则可以从物理体中抵消。


> 源码：[src/gameobjects/container/Container.js#L214](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L214)  
引入版本：3.4.0


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





**From [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize):**


 - [setDisplaySize](/api/namespace/gameobjects-components-computedsize#setDisplaySize)
 - [setSize](/api/namespace/gameobjects-components-computedsize#setSize)





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





**From [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask):**


 - [clearMask](/api/namespace/gameobjects-components-mask#clearMask)
 - [createGeometryMask](/api/namespace/gameobjects-components-mask#createGeometryMask)
 - [setMask](/api/namespace/gameobjects-components-mask#setMask)





**From [Phaser.GameObjects.Components.RenderSteps](/api/namespace/gameobjects-components-rendersteps):**


 - [addRenderStep](/api/namespace/gameobjects-components-rendersteps#addRenderStep)
 - [renderWebGLStep](/api/namespace/gameobjects-components-rendersteps#renderWebGLStep)





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

### add {#add}

#### \<instance> add(child) {#instance-addchild}


**说明:**

将给定的游戏对象或游戏对象阵列添加到此容器中。

每个游戏对象必须在容器内独有.

如果您尝试添加图层, 它会丢出一个错误 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象,或游戏对象的数组,用于添加容器. |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L526](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L526)  
引入版本：3.4.0


---

### addAt {#addAt}

#### \<instance> addAt(child, [index]) {#instance-addatchild-index}


**说明:**

将指定的游戏对象或游戏对象阵列添加到指定位置的此容器中。

容器中现有的游戏对象被向上移.

每个游戏对象必须在容器内独有.

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 游戏对象,或游戏对象的数组,用于添加容器. |
| index | number | 是 | 0 | 插入游戏对象/s 位置 。 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L565](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L565)  
引入版本：3.4.0


---

### bringToTop {#bringToTop}

#### \<instance> bringToTop(child) {#instance-bringtotopchild}


**说明:**

将给定的游戏对象带到容器的顶端。 这将使它在容器中的任何其他对象上方渲染 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象 将带入容器的顶端。 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L1006](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1006)  
引入版本：3.4.0


---

### count {#count}

#### \<instance> count(property, value, [startIndex], [endIndex]) {#instance-countproperty-value-startindex-endindex}


**说明:**

返回此容器中具有匹配给定值的属性的游戏对象的总数。

例如:`count('visible', true)`会计算所有具有可见属性集的元素.

您可以选择将操作限制在 `startIndex` - `endIndex` 范围.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| property | string | 否 |  | 检查的地产。 |
| value | any | 否 |  | 检查值 。 |
| startIndex | number | 是 | 0 | 搜索对象的可选起始索引 。 |
| endIndex | number | 是 | "Container.length" | 搜索到( 但不包含) 的可选结尾索引 |


**返回值:** number - 此容器中带有匹配给定值的属性的游戏对象的总数 。


> 源码：[src/gameobjects/container/Container.js#L757](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L757)  
引入版本：3.4.0


---

### each {#each}

#### \<instance> each(callback, [context], [args]) {#instance-eachcallback-context-args}


**说明:**

将此容器中的所有游戏对象传递给给给定的回调 。

在每个条目通过回调前,会制作一个容器副本。这个可防止回调本身修改容器。

如果你确信回调不会改变这个容器的大小 那你可以使用更能表现的`Container.iterate`方法

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | function | 否 | 调用功能 。 |
| context | object | 是 | 执行回调时用作 `this` 值 。 |
| args | * | 是 | 更多论点,在孩子出生后,会转给回电者。 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L1204](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1204)  
引入版本：3.4.0


---

### exists {#exists}

#### \<instance> exists(child) {#instance-existschild}


**说明:**

如果给定的游戏对象是这个容器的直接子, 返回 `true` 。

检查不会扫描嵌入式容器 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 在此容器内检查的游戏对象 。 |


**返回值:** boolean - 如果游戏对象是这个容器的近亲,否则是假的。


> 源码：[src/gameobjects/container/Container.js#L1152](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1152)  
引入版本：3.4.0


---

### getAll {#getAll}

#### \<instance> getAll([property], [value], [startIndex], [endIndex]) {#instance-getallproperty-value-startindex-endindex}


**说明:**

返回此容器中的所有游戏对象 。

您可以选择使用 `property` 和 `value` 参数指定匹配标准 。

例如:`getAll('body')`只返回具有体质属性的游戏对象.

您还可以指定一个值来比较属性 :

`getAll('visible', true)`只将那些有可见属性的游戏对象返回到`true`.

您可以选择指定一个起始和结束索引。 例如, 如果这个容器有100个游戏对象, 您将 `startIndex` 设置为 0, `endIndex` 设置为 50, 它只从前50个游戏对象返回匹配 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| property | string | 是 |  | 容器中每个游戏对象的测试属性 。 |
| value | any | 是 |  | 如果设置了属性,则`property`必须严格等于这个值才能列入结果. |
| startIndex | number | 是 | 0 | 搜索对象的可选起始索引 。 |
| endIndex | number | 是 | "Container.length" | 搜索到( 但不包含) 的可选结尾索引 |


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 从此容器匹配游戏对象的阵列 。


> 源码：[src/gameobjects/container/Container.js#L724](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L724)  
引入版本：3.4.0


---

### getAt {#getAt}

#### \<instance> getAt(index) {#instance-getatindex}


**说明:**

返回此容器中指定位置的游戏对象。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 获取游戏对象的位置 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 指定索引上的游戏对象, 如果没有找到, 则使用 `null` 。


> 源码：[src/gameobjects/container/Container.js#L590](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L590)  
引入版本：3.4.0


---

### getBounds {#getBounds}

#### \<instance> getBounds([output]) {#instance-getboundsoutput}


**说明:**

获得这个集装箱的界限。它通过对集装箱的所有儿童进行游动,获得各自的界限,然后从中找出一个最小矩,它不考虑儿童是否做出,所有都包括在内。

一些儿童无法返回他们的界限,例如图形对象,在这种情况下,他们会被跳过。

根据这个集装箱里的儿童数量,它可能是一个非常昂贵的电话,所以缓存它,只根据需要进行投票。

数值被存储并返回到矩形对象中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| output | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 存储值的 Geom.矩形对象。 如果不提供新的矩形, 将会创建 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 输出对象中存储的值 。


> 源码：[src/gameobjects/container/Container.js#L356](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L356)  
引入版本：3.4.0


---

### getBoundsTransformMatrix {#getBoundsTransformMatrix}

#### \<instance> getBoundsTransformMatrix() {#instance-getboundstransformmatrix}


**说明:**

返回用于Boundes检查的世界变换矩阵。

返回的矩阵是暂时的,不应该被存储.


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 世界变迁矩阵.


> 源码：[src/gameobjects/container/Container.js#L511](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L511)  
引入版本：3.4.0


---

### getByName {#getByName}

#### \<instance> getByName(name) {#instance-getbynamename}


**说明:**

寻找儿童与其 `name` 属性匹配给定的参数。如果一个以上孩子的同名名称相同,则只返回第一个。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 寻之名曰. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 第一个孩子有匹配的名字,或者如果找不到的话,则使用`null`.


> 源码：[src/gameobjects/container/Container.js#L658](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L658)  
引入版本：3.4.0


---

### getFirst {#getFirst}

#### \<instance> getFirst(property, value, [startIndex], [endIndex]) {#instance-getfirstproperty-value-startindex-endindex}


**说明:**

获得此容器中的第一个游戏对象 。

您也可以指定要搜索的属性和值, 届时它会返回此容器中的第一个游戏对象, 并带有匹配属性和/ 或值 。

例如:`getFirst('visible', true)`会返回第一个拥有其`visible`属性设定的游戏对象.

你可以将搜索限制在`startIndex` - `endIndex`范围.

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| property | string | 否 |  | 容器中每个游戏对象的测试属性 。 |
| value | * | 否 |  | 对照属性测试值。 必须进行严格的( `===`) 比较检查 。 |
| startIndex | number | 是 | 0 | 搜索对象的可选起始索引 。 |
| endIndex | number | 是 | "Container.length" | 搜索到( 但不包含) 的可选结尾索引 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 首个匹配的游戏对象, 或 `null` 如果没有找到的话 。


> 源码：[src/gameobjects/container/Container.js#L696](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L696)  
引入版本：3.4.0


---

### getIndex {#getIndex}

#### \<instance> getIndex(child) {#instance-getindexchild}


**说明:**

返回此容器中给定的游戏对象的索引 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 在此容器中搜索的游戏对象 。 |


**返回值:** number - 此容器中的游戏对象索引, 如果找不到, 则为 - 1 。


> 源码：[src/gameobjects/container/Container.js#L608](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L608)  
引入版本：3.4.0


---

### getRandom {#getRandom}

#### \<instance> getRandom([startIndex], [length]) {#instance-getrandomstartindex-length}


**说明:**

从此容器返回随机游戏对象 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| startIndex | number | 是 | 0 | 选择的启动索引 。 |
| length | number | 是 |  | 可选长度,从startIndex中选择的元素总数. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 集装箱里随机出现的孩子,或者如果集装箱是空的,则使用`null`.


> 源码：[src/gameobjects/container/Container.js#L677](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L677)  
引入版本：3.4.0


---

### iterate {#iterate}

#### \<instance> iterate(callback, [context], [args]) {#instance-iteratecallback-context-args}


**说明:**

将此容器中的所有游戏对象传递给给给定的回调 。

只有在绝对知道集装箱在重迭期间不会被修改,即将其内装物移除或添加时,才使用这种方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | function | 否 | 调用功能 。 |
| context | object | 是 | 执行回调时用作 `this` 值 。 |
| args | * | 是 | 更多论点,在孩子出生后,会转给回电者。 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L1244](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1244)  
引入版本：3.4.0


---

### moveAbove {#moveAbove}

#### \<instance> moveAbove(child1, child2) {#instance-moveabovechild1-child2}


**说明:**

将游戏对象移到容器内的另一游戏对象之上。如果游戏对象已经移到另一游戏对象之上,则不会移动。

这2个游戏对象 必须是这个容器的孩子。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child1 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 移动到基数上方的游戏对象 。 |
| child2 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 基础游戏对象. |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L828](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L828)  
引入版本：3.55.0


---

### moveBelow {#moveBelow}

#### \<instance> moveBelow(child1, child2) {#instance-movebelowchild1-child2}


**说明:**

将游戏对象移到容器内的另一下方。如果游戏对象已经移到另一下方,则不会移动。

这2个游戏对象 必须是这个容器的孩子。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child1 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 移动到基底游戏对象以下的游戏对象. |
| child2 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 基础游戏对象. |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L852](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L852)  
引入版本：3.55.0


---

### moveDown {#moveDown}

#### \<instance> moveDown(child) {#instance-movedownchild}


**说明:**

将给定的游戏对象移动到这个容器中一个位置, 除非它已经位于底部 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象要移动在容器中 。 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L1068](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1068)  
引入版本：3.4.0


---

### moveTo {#moveTo}

#### \<instance> moveTo(child, index) {#instance-movetochild-index}


**说明:**

将游戏对象移动到此容器内的新位置。

游戏对象必须已经是这个容器的孩子 。

游戏对象从旧位置移走并插入新位置, 因此容器大小不会改变, 其他孩子会相应改变位置 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 要移动的游戏对象 。 |
| index | number | 否 | 游戏对象在这个容器中的新位置 。 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L802](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L802)  
引入版本：3.4.0


---

### moveUp {#moveUp}

#### \<instance> moveUp(child) {#instance-moveupchild}


**说明:**

将给定的游戏对象移动到这个容器中一个位置, 除非它已经位于顶端 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象要移动在容器中 。 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L1048](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1048)  
引入版本：3.4.0


---

### onChildDestroyed {#onChildDestroyed}

#### \<instance> onChildDestroyed() {#instance-onchilddestroyed}


**说明:**

内部处理器,当一个孩子被摧毁时呼叫.


**Access:** 保护


> 源码：[src/gameobjects/container/Container.js#L1467](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1467)  
引入版本：3.80.0


---

### pointToContainer {#pointToContainer}

#### \<instance> pointToContainer(source, [output]) {#instance-pointtocontainersource-output}


**说明:**

取一个类似点的物体,如矢量2,或具有公共 x 和 y 属性的物体,将其转换成这个容器的空间,然后在输出对象中返回。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 源点要转换. |
| output | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 | 一个存储转换点的目的地对象。 如果没有给定矢量2 , 将会创建并返回 。 |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 变位.


> 源码：[src/gameobjects/container/Container.js#L473](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L473)  
引入版本：3.4.0


---

### preDestroy {#preDestroy}

#### \<instance> preDestroy() {#instance-predestroy}


**说明:**

内部破坏处理器,作为破坏过程的一部分而叫作.


**Access:** 保护


> 源码：[src/gameobjects/container/Container.js#L1451](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1451)  
引入版本：3.9.0


---

### remove {#remove}

#### \<instance> remove(child, [destroyChild]) {#instance-removechild-destroychild}


**说明:**

从此容器中删除给定的游戏对象,或游戏对象阵列。

游戏对象必须是这个容器的子嗣 。

您也可以在从容器中移除的每个游戏对象上选择使用`destroy`.

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 游戏对象,或游戏对象的阵列,从容器中移除. |
| destroyChild | boolean | 是 | false | 给从集装箱上成功取走的每个孩子打电话`destroy` |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L876](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L876)  
引入版本：3.4.0


---

### removeAll {#removeAll}

#### \<instance> removeAll([destroyChild]) {#instance-removealldestroychild}


**说明:**

从此容器中删除所有游戏对象。

您也可以在从容器中移除的每个游戏对象上选择使用`destroy`.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| destroyChild | boolean | 是 | false | 可以在从这个容器中成功移除的每个游戏对象上选择使用`destroy`. |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L968](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L968)  
引入版本：3.4.0


---

### removeAt {#removeAt}

#### \<instance> removeAt(index, [destroyChild]) {#instance-removeatindex-destroychild}


**说明:**

删除此容器中指定位置的游戏对象。

如果找到,您也可以在游戏对象上可选择使用`destroy`。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| index | number | 否 |  | 要删除的游戏对象索引 。 |
| destroyChild | boolean | 是 | false | 如果成功从这个容器中移除, 可选择在游戏对象上调用 `destroy` 。 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L914](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L914)  
引入版本：3.4.0


---

### removeBetween {#removeBetween}

#### \<instance> removeBetween([startIndex], [endIndex], [destroyChild]) {#instance-removebetweenstartindex-endindex-destroychild}


**说明:**

删除此容器中指定位置之间的游戏对象。

您也可以在从容器中移除的每个游戏对象上选择使用`destroy`.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| startIndex | number | 是 | 0 | 搜索对象的可选起始索引 。 |
| endIndex | number | 是 | "Container.length" | 搜索到( 但不包含) 的可选结尾索引 |
| destroyChild | boolean | 是 | false | 可以在从这个容器中成功移除的每个游戏对象上选择使用`destroy`. |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L939](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L939)  
引入版本：3.4.0


---

### replace {#replace}

#### \<instance> replace(oldChild, newChild, [destroyChild]) {#instance-replaceoldchild-newchild-destroychild}


**说明:**

将这个容器中的游戏对象替换为新的游戏对象。新的游戏对象不能已经是这个容器的子 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| oldChild | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将替换的容器中的游戏对象 。 |
| newChild | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 在此容器中添加的游戏对象 。 |
| destroyChild | boolean | 是 | false | 如果成功从这个容器中移除, 可选择在游戏对象上调用 `destroy` 。 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L1118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1118)  
引入版本：3.4.0


---

### reverse {#reverse}

#### \<instance> reverse() {#instance-reverse}


**说明:**

反转此容器中所有游戏对象的顺序。


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L1088](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1088)  
引入版本：3.4.0


---

### sendToBack {#sendToBack}

#### \<instance> sendToBack(child) {#instance-sendtobackchild}


**说明:**

将给定的游戏对象发送到此容器的底部。 这将使其在容器中的任何其他对象以下渲染 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 发送到容器底部的游戏对象 。 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L1027](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1027)  
引入版本：3.4.0


---

### setAll {#setAll}

#### \<instance> setAll(property, value, [startIndex], [endIndex]) {#instance-setallproperty-value-startindex-endindex}


**说明:**

将属性设定为此容器中所有游戏对象的给定值。

您可以选择指定一个起始和结束索引。 例如, 如果这个容器有100个游戏对象, 您将 `startIndex` 设置为 0, `endIndex` 设置为 50, 它只从前50个游戏对象返回匹配 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| property | string | 否 |  | 游戏对象上必须存在的属性 。 |
| value | any | 否 |  | 设置属性的值 。 |
| startIndex | number | 是 | 0 | 搜索对象的可选起始索引 。 |
| endIndex | number | 是 | "Container.length" | 搜索到( 但不包含) 的可选结尾索引 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L1172](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1172)  
引入版本：3.4.0


---

### setExclusive {#setExclusive}

#### \<instance> setExclusive([value]) {#instance-setexclusivevalue}


**说明:**

这个集装箱是否专门管理孩子?

默认为`true`,这意味着加入这个集装箱的儿童不能属于另一个集装箱,其中包括场景显示列表。

如果您关闭了此选项, 这个容器将不再完全管理它的孩子。 这样可以创建各种有趣的图形效果, 例如复制游戏对象而不在场景中重新显示它们。 然而, 这样做会阻止儿童接收任何类型的输入事件, 或者让物理体默认工作, 因为它们不再是显示列表中的单一实体, 而是被复制到任何容器所在的地方。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 这集装箱的独家状态。 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱。


> 源码：[src/gameobjects/container/Container.js#L327](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L327)  
引入版本：3.4.0


---

### setScrollFactor {#setScrollFactor}

#### \<instance> setScrollFactor(x, [y], [updateChildren]) {#instance-setscrollfactorx-y-updatechildren}


**说明:**

设置此容器的滚动因子, 并选择其所有儿童 。

滚动因子控制了相机移动对这个游戏对象的影响.

当相机滚动时, 将更改屏幕上显示此游戏对象的位置。 它不会改变游戏对象的实际位置值 。

1 值表示它会和相机同步移动。 0 值表示它不会移动, 即使相机移动。 其他值控制了相机移动到此 Game Object 的映射程度 。

请注意,在计算物理碰撞时,不考虑1以外的滚动因子值。天体总是会根据其世界位置碰撞,但改变滚动因子是对纹理的渲染地的视觉调整,如果在您的代码中没有说明,则可以从物理体中抵消。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 此游戏对象的横向滚动因子 。 |
| y | number | 是 | "x" | 此游戏对象的垂直滚动因子。 如果不设定, 则会使用 `x` 值 。 |
| updateChildren | boolean | 是 | false | 对所有集装箱儿童也适用这种scrollFactor? |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 此游戏对象实例 。


> 源码：[src/gameobjects/container/Container.js#L1279](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1279)  
引入版本：3.4.0


---

### shuffle {#shuffle}

#### \<instance> shuffle() {#instance-shuffle}


**说明:**

使用 Fisher-Yates 执行来移动此容器中的所有游戏对象 。


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L1103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L1103)  
引入版本：3.4.0


---

### sort {#sort}

#### \<instance> sort(property, [handler]) {#instance-sortproperty-handler}


**说明:**

排序此容器的内容, 以便根据指定属性排列项目。 例如 : `sort('alpha')` 将基于其值的元素排序 `alpha` 属性。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| property | string | 否 | 地产被逻辑分类。 |
| handler | function | 是 | 提供您自定义的处理器功能。 将接收两个孩子, 并返回一个负数、 0 或正数 。 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L626](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L626)  
引入版本：3.4.0


---

### swap {#swap}

#### \<instance> swap(child1, child2) {#instance-swapchild1-child2}


**说明:**

交换此容器中两个游戏对象的位置。 这两个游戏对象必须属于此容器 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child1 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 第一个要交换的游戏对象 。 |
| child2 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 第二个游戏对象来交换. |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 这个集装箱的例子。


> 源码：[src/gameobjects/container/Container.js#L780](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/Container.js#L780)  
引入版本：3.4.0


---

---
