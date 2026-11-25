# Layer {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-layer)

一个图层游戏对象 。

层是游戏对象的特殊类型, 其作用是显示列表。 您可以像对场景一样, 将任意类型的游戏对象添加到层中。 层可以用来将游戏对象的“ 层” 组合在一起 :

```javascript
const spaceman = this.add.sprite(150, 300, 'spaceman');
const bunny = this.add.sprite(400, 300, 'bunny');
const elephant = this.add.sprite(650, 300, 'elephant');

const layer = this.add.layer();

layer.add([ spaceman, bunny, elephant ]);
```

上面的例子中的3个图案现在将由它们被添加的图层管理。 因此, 如果您设置 `layer.setVisible(false)` , 它们都会从显示中消失 。

您也可以控制图层内游戏对象的深度。 例如, 使用图层中的孩子的 `setDepth` 方法, 您可以调整该孩子的深度_ 在图层本身内部, 而不是整个场景。 图层也可以设定其深度 。

层类还提供了许多不同的操纵列表的方法,例如方法 `moveUp`, `moveDown`, `sendToBack`, `bringToTop` 。这些可以让您更改图层子的显示列表位置, 从而调整其显示顺序。 使用 `setDepth` 在一个孩子上,你可以 推翻这个。

层在空间中没有位置或大小。 这意味着您无法允许层用于物理或输入, 或改变层的位置、 旋转或尺度。 它们也没有滚动因子、 纹理、 锡、 来源、 裁剪或边框 。

如果需要这些特性,您应该使用一个容器。容器可以添加到层中,但是不能添加到层中。

然而, 您可以设置一个层的 Alpha, 混合模式, 深度, 遮罩和可见状态。 这些设置会影响所有由层制成的孩子 。

层应该始终是任何场景等级中最顶尖的元素,它们可以是层的子嗣,但不能是其他任何子嗣.

直到Phaser版本4.1.0,Layer不是真正的游戏对象。它现在是一个真正的游戏对象。

**构造函数**

`new Layer(scene, [children])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| children | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 是 | 添加到此图层的游戏对象可选数组 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/layer/Layer.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L18)  
引入版本：3.50.0

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
 - [state](/api/class/gameobjects-gameobject#state)
 - [tabIndex](/api/class/gameobjects-gameobject#tabIndex)
 - [type](/api/class/gameobjects-gameobject#type)
 - [vertexRoundMode](/api/class/gameobjects-gameobject#vertexRoundMode)




---

## 公开成员 {#public-members}

### _sortKey {#_sortKey}

#### _sortKey: string {#_sortkey-string}


**说明:**

需要排序的属性密钥 。


> 源码：[src/gameobjects/layer/Layer.js#L512](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L512)  
引入版本：3.4.0


---

### addCallback {#addCallback}

#### addCallback: function {#addcallback-function}


**说明:**

每当儿童被列入名单时,都会重复使用。


> 源码：[src/gameobjects/layer/Layer.js#L496](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L496)  
引入版本：3.4.0


---

### events {#events}

#### events: [Phaser.Events.EventEmitter](/api/class/events-eventemitter) {#events-phasereventseventemitter}


**说明:**

参考景点事件 Emitter.


> 源码：[src/gameobjects/layer/Layer.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L125)  
引入版本：3.50.0


---

### first {#first}

#### first: [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) {#first-phasergameobjectsgameobject}


**说明:**

列表中的首项或 `null` 空列表 。


> 源码：[src/gameobjects/layer/Layer.js#L875](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L875)  
引入版本：3.0.0


---

### last {#last}

#### last: [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) {#last-phasergameobjectsgameobject}


**说明:**

列表中最后一个项目,或空列表的 `null` 。


> 源码：[src/gameobjects/layer/Layer.js#L884](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L884)  
引入版本：3.0.0


---

### length {#length}

#### length: number {#length-number}


**说明:**

清单内的项目数。


> 源码：[src/gameobjects/layer/Layer.js#L866](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L866)  
引入版本：3.0.0


---

### list {#list}

#### list: Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> {#list-arrayphasergameobjectsgameobject}


**说明:**

此收藏的对象 。


> 源码：[src/gameobjects/layer/Layer.js#L476](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L476)  
引入版本：3.0.0


---

### next {#next}

#### next: [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) {#next-phasergameobjectsgameobject}


**说明:**

清单上的下一个项目,或如果整个清单已经经过,则使用`null`。

此属性可以在读取 [#first](#first) 后相继读取, 或者手动设置 [#position](#position) 以将列表分割为直线 。


> 源码：[src/gameobjects/layer/Layer.js#L893](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L893)  
引入版本：3.0.0


---

### parent {#parent}

#### parent: * {#parent-1}


**说明:**

此列表的父关.


> 源码：[src/gameobjects/layer/Layer.js#L468](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L468)  
引入版本：3.0.0


---

### position {#position}

#### position: number {#position-number}


**说明:**

当前元素的索引 。

内部使用时,通过列表中带有[#first](#first),[#last](#last),[#next](#next),和[#previous](#previous)属性.


> 源码：[src/gameobjects/layer/Layer.js#L485](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L485)  
引入版本：3.0.0


---

### previous {#previous}

#### previous: [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) {#previous-phasergameobjectsgameobject}


**说明:**

清单上的上一项,或如果整个清单已经经过,则称为`null`。

此属性可以在读取 [#last](#last) 后相继读取, 或者手动设置 [#position](#position) 将列表向后排列 。


> 源码：[src/gameobjects/layer/Layer.js#L904](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L904)  
引入版本：3.0.0


---

### removeCallback {#removeCallback}

#### removeCallback: function {#removecallback-function}


**说明:**

每次从这个名单中除名时都会重复使用一个召回电话。


> 源码：[src/gameobjects/layer/Layer.js#L504](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L504)  
引入版本：3.4.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

引用此游戏对象所属的景色 。

游戏对象只能属于一个场景.

您应该将此属性视为只读。 您不能简单地更改它, 而将游戏对象移动到另一个场景 。


**Overrides:** Phaser.GameObjects.GameObject#风景


> 源码：[src/gameobjects/layer/Layer.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L102)  
引入版本：3.50.0


---

### sortChildrenFlag {#sortChildrenFlag}

#### sortChildrenFlag: boolean {#sortchildrenflag-boolean}


**说明:**

用于确定游戏对象是否在调用 `depthSort()` 时排序的旗帜 。


> 源码：[src/gameobjects/layer/Layer.js#L134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L134)  
引入版本：3.50.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

参考景区系统.


> 源码：[src/gameobjects/layer/Layer.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L116)  
引入版本：3.50.0


---

## 继承的方法 {#inherited-methods}


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





**From [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask):**


 - [clearMask](/api/namespace/gameobjects-components-mask#clearMask)
 - [createGeometryMask](/api/namespace/gameobjects-components-mask#createGeometryMask)
 - [setMask](/api/namespace/gameobjects-components-mask#setMask)





**From [Phaser.GameObjects.Components.RenderSteps](/api/namespace/gameobjects-components-rendersteps):**


 - [addRenderStep](/api/namespace/gameobjects-components-rendersteps#addRenderStep)
 - [renderWebGLStep](/api/namespace/gameobjects-components-rendersteps#renderWebGLStep)





**From [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible):**


 - [setVisible](/api/namespace/gameobjects-components-visible#setVisible)





**From [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject):**


 - [addedToScene](/api/class/gameobjects-gameobject#addedToScene)
 - [addToDisplayList](/api/class/gameobjects-gameobject#addToDisplayList)
 - [addToUpdateList](/api/class/gameobjects-gameobject#addToUpdateList)
 - [getData](/api/class/gameobjects-gameobject#getData)
 - [getDisplayList](/api/class/gameobjects-gameobject#getDisplayList)
 - [getIndexList](/api/class/gameobjects-gameobject#getIndexList)
 - [incData](/api/class/gameobjects-gameobject#incData)
 - [removedFromScene](/api/class/gameobjects-gameobject#removedFromScene)
 - [removeFromDisplayList](/api/class/gameobjects-gameobject#removeFromDisplayList)
 - [removeFromUpdateList](/api/class/gameobjects-gameobject#removeFromUpdateList)
 - [setActive](/api/class/gameobjects-gameobject#setActive)
 - [setData](/api/class/gameobjects-gameobject#setData)
 - [setDataEnabled](/api/class/gameobjects-gameobject#setDataEnabled)
 - [setName](/api/class/gameobjects-gameobject#setName)
 - [setState](/api/class/gameobjects-gameobject#setState)
 - [setVertexRoundMode](/api/class/gameobjects-gameobject#setVertexRoundMode)
 - [toggleData](/api/class/gameobjects-gameobject#toggleData)
 - [toJSON](/api/class/gameobjects-gameobject#toJSON)
 - [update](/api/class/gameobjects-gameobject#update)
 - [willRoundVertices](/api/class/gameobjects-gameobject#willRoundVertices)




---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(child, [skipCallback]) {#instance-addchild-skipcallback}


**说明:**

将给定的项目添加到列表的末尾。每个项目必须是独一无二的。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 将项目或项目数组添加到列表中。 |
| skipCallback | boolean | 是 | false | 跳过呼叫列表。 addCallback 如果成功添加此孩子 。 |


**返回值:** * - 列表的内在阵列.


> 源码：[src/gameobjects/layer/Layer.js#L520](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L520)  
引入版本：3.0.0


---

### addAt {#addAt}

#### \<instance> addAt(child, [index], [skipCallback]) {#instance-addatchild-index-skipcallback}


**说明:**

添加到列表中, 开始于指定的索引。 每个条目必须在列表中独有。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 将项目或项目数组添加到列表中。 |
| index | number | 是 | 0 | 插入元素的列表中的索引。 |
| skipCallback | boolean | 是 | false | 跳过呼叫列表。 addCallback 如果成功添加此孩子 。 |


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 列表的内在阵列.


> 源码：[src/gameobjects/layer/Layer.js#L532](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L532)  
引入版本：3.0.0


---

### addListener {#addListener}

#### \<instance> addListener(event, fn, [context]) {#instance-addlistenerevent-fn-context}


**说明:**

为指定事件添加一个听众 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| event | string \| symbol | 否 |  | 事件名称. |
| fn | function | 否 |  | 听者功能. |
| context | * | 是 | "this" | 用来引用听众的上下文 。 |


**Overrides:** Phaser.GameObjects.GameObject#addListener


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 这个图层实例 。


> 源码：[src/gameobjects/layer/Layer.js#L399](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L399)  
引入版本：3.50.0


---

### bringToTop {#bringToTop}

#### \<instance> bringToTop(child) {#instance-bringtotopchild}


**说明:**

将给定的孩子带到此列表的首位 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 举进士名录之项. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 被移动的物品。


> 源码：[src/gameobjects/layer/Layer.js#L751](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L751)  
引入版本：3.0.0


---

### count {#count}

#### \<instance> count(property, value) {#instance-countproperty-value}


**说明:**

返回清单上具有与给定值相符的财产的总数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| property | string | 否 | 每个项目测试的属性 。 |
| value | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 测试属性的值 。 |


**返回值:** number - 匹配元素的总数 。


> 源码：[src/gameobjects/layer/Layer.js#L645](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L645)  
引入版本：3.0.0


---

### depthSort {#depthSort}

#### \<instance> depthSort() {#instance-depthsort}


**说明:**

如果设置了旗, 立即排序显示列表 。


> 源码：[src/gameobjects/layer/Layer.js#L296](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L296)  
引入版本：3.50.0


---

### destroy {#destroy}

#### \<instance> destroy([fromScene]) {#instance-destroyfromscene}


**说明:**

销毁此图层, 将其从“ 显示列表” 和更新列表中删除, 并切除与父资源的所有链接 。

也要毁灭这层的后裔,如果你们不希望毁灭他们,那末,你们应当首先把他们从这层的后裔中移走。

如果您再也没有计划使用, 请使用此选项从游戏中删除。 只要您自己的代码中没有提及它的内容, 浏览器就应该可以免费收集垃圾 。

如果您只是想要暂时禁用一个对象, 那么请看看使用游戏对象池而不是销毁它, 因为已销毁的对象无法复活 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| fromScene | boolean | 是 | false | `True` 如果游戏对象被场景所破坏, `false` 如果不是的话。 |


**Overrides:** Phaser.GameObjects.GameObject#销毁


**Fires:** [Phaser.GameObjects.Events#event:DESTROY](/api/event/gameobjects-events#destroy)


> 源码：[src/gameobjects/layer/Layer.js#L915](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L915)  
引入版本：3.50.0


---

### disableInteractive {#disableInteractive}

#### \<instance> disableInteractive() {#instance-disableinteractive}


**说明:**

无法启用层来输入 。

这个方法无所作为,被保存以确保图层的形状与游戏对象相同.


**Overrides:** Phaser.GameObjects.GameObject#disableInteractive


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 这个游戏对象 。


> 源码：[src/gameobjects/layer/Layer.js#L183](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L183)  
引入版本：3.51.0


---

### each {#each}

#### \<instance> each(callback, [context], [args]) {#instance-eachcallback-context-args}


**说明:**

将所有的孩子传到给定的回调中.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | EachListCallback.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 调用功能 。 |
| context | any | 是 | 执行回调时用作 `this` 值 。 |
| args | any | 是 | 更多论点,在孩子出生后,会转给回电者。 |


> 源码：[src/gameobjects/layer/Layer.js#L848](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L848)  
引入版本：3.0.0


---

### emit {#emit}

#### \<instance> emit(event, [args]) {#instance-emitevent-args}


**说明:**

给每个注册参加特定活动的听众打电话。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | string \| symbol | 否 | 事件名称. |
| args | * | 是 | 将传递给事件处理者的附加参数 。 |


**Overrides:** Phaser.GameObjects.GameObject#闪米


**返回值:** boolean - 如果有听众的话,就用`true`,否则用`false`.


> 源码：[src/gameobjects/layer/Layer.js#L374](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L374)  
引入版本：3.50.0


---

### eventNames {#eventNames}

#### \<instance> eventNames() {#instance-eventnames}


**说明:**

返回一个列出发送器已注册的听器的事件的数组 。


**Overrides:** Phaser.GameObjects.GameObject#eventNames


**返回值:** Array.\<(string | symbol)> - 


> 源码：[src/gameobjects/layer/Layer.js#L343](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L343)  
引入版本：3.50.0


---

### exists {#exists}

#### \<instance> exists(child) {#instance-existschild}


**说明:**

检查清单上是否存在项目。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 检查是否存在的项目 。 |


**返回值:** boolean - 如果在列表中找到该物品,则使用`true`,否则使用`false`.


> 源码：[src/gameobjects/layer/Layer.js#L825](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L825)  
引入版本：3.0.0


---

### getAll {#getAll}

#### \<instance> getAll([property], [value], [startIndex], [endIndex]) {#instance-getallproperty-value-startindex-endindex}


**说明:**

将名单上的所有儿童送回。

您可以选择使用 `property` 和 `value` 参数指定匹配标准 。

例如:`getAll('parent')`只归还拥有名为`parent`的财产的儿童.

您还可以指定一个值来比较属性 :

`getAll('visible', true)`只把那些 拥有明显财产的孩子送回`true`

您可以选择指定一个起始和结束索引。 例如, 如果此列表有100个孩子, 您将 `startIndex` 设置为 0, `endIndex` 设置为 50, 它将会从列表中仅返回前50个孩子的匹配 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| property | string | 是 | 用于测试值参数的可选属性 。 |
| value | any | 是 | 如果设定了财产,则Child.财产必须严格地与这一价值相等,才能列入结果。 |
| startIndex | number | 是 | 首个启动搜索的孩子索引. |
| endIndex | number | 是 | 最后的婴儿索引要搜索到 |


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 清单上符合规定标准的所有项目(如有)。


> 源码：[src/gameobjects/layer/Layer.js#L619](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L619)  
引入版本：3.0.0


---

### getAt {#getAt}

#### \<instance> getAt(index) {#instance-getatindex}


**说明:**

在清单内某一位置检索该物品。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 项索引. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject), undefined - 被检索到的物品,或者如果不在清单的界限内,则使用`undefined`.


> 源码：[src/gameobjects/layer/Layer.js#L545](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L545)  
引入版本：3.0.0


---

### getByName {#getByName}

#### \<instance> getByName(name) {#instance-getbynamename}


**说明:**

寻找儿童与其 `name` 属性匹配给定的参数。如果一个以上孩子的同名名称相同,则只返回第一个。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 寻之名曰. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 第一个孩子有匹配的名字,或者如果找不到,则无效。


> 源码：[src/gameobjects/layer/Layer.js#L580](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L580)  
引入版本：3.0.0


---

### getChildren {#getChildren}

#### \<instance> getChildren() {#instance-getchildren}


**说明:**

返回包含此图层中所有游戏对象的数组的引用 。

这是参考文献,不是复制品,所以要非常小心不要变异.


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 此图层内的一系列游戏对象 。


> 源码：[src/gameobjects/layer/Layer.js#L328](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L328)  
引入版本：3.50.0


---

### getFirst {#getFirst}

#### \<instance> getFirst(property, value, [startIndex], [endIndex]) {#instance-getfirstproperty-value-startindex-endindex}


**说明:**

返回清单某一部分中符合特定标准的第一要素。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| property | string | 否 |  | 财产名称用于测试,或者虚构价值用于无标准. |
| value | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| undefined | 否 |  | 测试 `property` 相对于,或 `undefined` 允许任何值, 并且只检查存在值 。 |
| startIndex | number | 是 | 0 | 列表中要开始搜索的位置 。 |
| endIndex | number | 是 |  | 列表中的位置可以选择停止搜索, 将不会被检查 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 符合给定标准的首项,或如果没有此类项目,则使用`null`。


> 源码：[src/gameobjects/layer/Layer.js#L605](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L605)  
引入版本：3.0.0


---

### getIndex {#getIndex}

#### \<instance> getIndex(child) {#instance-getindexchild}


**说明:**

将项目置于清单中并返回其索引。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 找到的线索 |


**返回值:** number - 列表中项目索引,或如果不在列表中则为−1.


> 源码：[src/gameobjects/layer/Layer.js#L556](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L556)  
引入版本：3.0.0


---

### getRandom {#getRandom}

#### \<instance> getRandom([startIndex], [length]) {#instance-getrandomstartindex-length}


**说明:**

从列表中返回随机子 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| startIndex | number | 是 | 0 | 从列表前方除去(最小的孩子). |
| length | number | 是 | "(to top)" | 限制您想要随机选择的数值数量。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 此列表的随机子 。


> 源码：[src/gameobjects/layer/Layer.js#L593](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L593)  
引入版本：3.0.0


---

### listenerCount {#listenerCount}

#### \<instance> listenerCount(event) {#instance-listenercountevent}


**说明:**

返回收听特定事件的听众数量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | string \| symbol | 否 | 事件名称. |


**Overrides:** Phaser.GameObjects.GameObject#listenerCount


**返回值:** number - 众听者数.


> 源码：[src/gameobjects/layer/Layer.js#L363](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L363)  
引入版本：3.50.0


---

### listeners {#listeners}

#### \<instance> listeners(event) {#instance-listenersevent}


**说明:**

返回已注册的听众 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | string \| symbol | 否 | 事件名称. |


**Overrides:** Phaser.GameObjects.GameObject#听众


**返回值:** Array.\<function()> - 注册听众。


> 源码：[src/gameobjects/layer/Layer.js#L352](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L352)  
引入版本：3.50.0


---

### moveAbove {#moveAbove}

#### \<instance> moveAbove(child1, child2) {#instance-moveabovechild1-child2}


**说明:**

将某个项目移到清单上的另一项目上方。如果给定的项目已经移到另一项目上方,则不会移到清单上。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child1 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 上移基元素的元素。 |
| child2 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 基点元素. |


> 源码：[src/gameobjects/layer/Layer.js#L679](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L679)  
引入版本：3.55.0


---

### moveBelow {#moveBelow}

#### \<instance> moveBelow(child1, child2) {#instance-movebelowchild1-child2}


**说明:**

将一个项目移到清单的另一项目下方。如果给定的项目已经移到另一项目下方,则不会移动。下面是清单开始的地方。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child1 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 移动到基元素以下的元素. |
| child2 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 基点元素. |


> 源码：[src/gameobjects/layer/Layer.js#L691](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L691)  
引入版本：3.55.0


---

### moveDown {#moveDown}

#### \<instance> moveDown(child) {#instance-movedownchild}


**说明:**

将给定的孩子移到列表中一个位置, 除非它已经位于底部 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 下移项. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 被移动的物品。


> 源码：[src/gameobjects/layer/Layer.js#L784](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L784)  
引入版本：3.0.0


---

### moveTo {#moveTo}

#### \<instance> moveTo(child, index) {#instance-movetochild-index}


**说明:**

将列表中的一个项目移动到新位置。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 移动的物品。 |
| index | number | 否 | 移动项目的新位置 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 被移动的物件.


> 源码：[src/gameobjects/layer/Layer.js#L667](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L667)  
引入版本：3.0.0


---

### moveUp {#moveUp}

#### \<instance> moveUp(child) {#instance-moveupchild}


**说明:**

将给定的孩子移到列表中一个位置, 除非它已经位于顶端 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 上移的物品. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 被移动的物品。


> 源码：[src/gameobjects/layer/Layer.js#L773](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L773)  
引入版本：3.0.0


---

### off {#off}

#### \<instance> off(event, [fn], [context], [once]) {#instance-offevent-fn-context-once}


**说明:**

删除特定事件的听众。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | string \| symbol | 否 | 事件名称. |
| fn | function | 是 | 只删除匹配此函数的听众 。 |
| context | * | 是 | 只删除有此上下文的听众. |
| once | boolean | 是 | 只删除一次性的听众. |


**Overrides:** Phaser.GameObjects.GameObject关闭( O)


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 这个图层实例 。


> 源码：[src/gameobjects/layer/Layer.js#L439](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L439)  
引入版本：3.50.0


---

### on {#on}

#### \<instance> on(event, fn, [context]) {#instance-onevent-fn-context}


**说明:**

为指定事件添加一个听众 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| event | string \| symbol | 否 |  | 事件名称. |
| fn | function | 否 |  | 听者功能. |
| context | * | 是 | "this" | 用来引用听众的上下文 。 |


**Overrides:** Phaser.GameObjects.GameObject#ON 时速


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 这个图层实例 。


> 源码：[src/gameobjects/layer/Layer.js#L386](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L386)  
引入版本：3.50.0


---

### once {#once}

#### \<instance> once(event, fn, [context]) {#instance-onceevent-fn-context}


**说明:**

为特定事件添加一次性的听觉.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| event | string \| symbol | 否 |  | 事件名称. |
| fn | function | 否 |  | 听者功能. |
| context | * | 是 | "this" | 用来引用听众的上下文 。 |


**Overrides:** 刚开始的 Phaser.GameObjects.GameObject#on


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 这个图层实例 。


> 源码：[src/gameobjects/layer/Layer.js#L412](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L412)  
引入版本：3.50.0


---

### queueDepthSort {#queueDepthSort}

#### \<instance> queueDepthSort() {#instance-queuedepthsort}


**说明:**

强制在下次呼叫时显示列表的排序 depthSort.


> 源码：[src/gameobjects/layer/Layer.js#L285](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L285)  
引入版本：3.50.0


---

### remove {#remove}

#### \<instance> remove(child, [skipCallback]) {#instance-removechild-skipcallback}


**说明:**

从列表中删除一个或多个项目。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 要删除的项目, 或项目数组 。 |
| skipCallback | boolean | 是 | false | 跳过名单。 removeCallback。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject), Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 成功从清单中删除的物项或数组物项。


> 源码：[src/gameobjects/layer/Layer.js#L703](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L703)  
引入版本：3.0.0


---

### removeAll {#removeAll}

#### \<instance> removeAll([skipCallback]) {#instance-removeallskipcallback}


**说明:**

删除所有项目。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| skipCallback | boolean | 是 | false | 跳过名单。 removeCallback。 |


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 此列表对象 。


> 源码：[src/gameobjects/layer/Layer.js#L740](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L740)  
引入版本：3.0.0


---

### removeAllListeners {#removeAllListeners}

#### \<instance> removeAllListeners([event]) {#instance-removealllistenersevent}


**说明:**

删除全部听众, 或指定事件的听众 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | string \| symbol | 是 | 事件名称. |


**Overrides:** Phaser.GameObjects.GameObject#removeAllListeners


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 这个图层实例 。


> 源码：[src/gameobjects/layer/Layer.js#L453](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L453)  
引入版本：3.50.0


---

### removeAt {#removeAt}

#### \<instance> removeAt(index, [skipCallback]) {#instance-removeatindex-skipcallback}


**说明:**

删除列表中指定位置的项目。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| index | number | 否 |  | 删除项目的位置 。 |
| skipCallback | boolean | 是 | false | 跳过名单。 removeCallback。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 被移除的物品。


> 源码：[src/gameobjects/layer/Layer.js#L715](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L715)  
引入版本：3.0.0


---

### removeBetween {#removeBetween}

#### \<instance> removeBetween([startIndex], [endIndex], [skipCallback]) {#instance-removebetweenstartindex-endindex-skipcallback}


**说明:**

删除列表中指定范围内的项目。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| startIndex | number | 是 | 0 | 开始删除的索引 。 |
| endIndex | number | 是 |  | 停止删除的位置, 此位置的项目不会被移除 。 |
| skipCallback | boolean | 是 | false | 跳过名单。 removeCallback。 |


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 被移除的项目的数组 。


> 源码：[src/gameobjects/layer/Layer.js#L727](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L727)  
引入版本：3.0.0


---

### removeInteractive {#removeInteractive}

#### \<instance> removeInteractive() {#instance-removeinteractive}


**说明:**

无法启用层来输入 。

这个方法无所作为,被保存以确保图层的形状与游戏对象相同.


**Overrides:** Phaser.GameObjects.GameObject#removeInteractive


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 这个游戏对象 。


> 源码：[src/gameobjects/layer/Layer.js#L199](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L199)  
引入版本：3.51.0


---

### removeListener {#removeListener}

#### \<instance> removeListener(event, [fn], [context], [once]) {#instance-removelistenerevent-fn-context-once}


**说明:**

删除特定事件的听众。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | string \| symbol | 否 | 事件名称. |
| fn | function | 是 | 只删除匹配此函数的听众 。 |
| context | * | 是 | 只删除有此上下文的听众. |
| once | boolean | 是 | 只删除一次性的听众. |


**Overrides:** Phaser.GameObjects.GameObject#removeListener


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 这个图层实例 。


> 源码：[src/gameobjects/layer/Layer.js#L425](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L425)  
引入版本：3.50.0


---

### replace {#replace}

#### \<instance> replace(oldChild, newChild) {#instance-replaceoldchild-newchild}


**说明:**

将本列表中的子替换为指定的 newChild。 newChild 不能成为该列表的成员 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| oldChild | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 将替换的列表中的儿童 。 |
| newChild | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 拟插入该名单的儿童。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 返回在本列表中替换的 oldChild 。


> 源码：[src/gameobjects/layer/Layer.js#L813](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L813)  
引入版本：3.0.0


---

### reverse {#reverse}

#### \<instance> reverse() {#instance-reverse}


**说明:**

颠倒本列表中所有儿童的顺序。


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 此列表对象 。


> 源码：[src/gameobjects/layer/Layer.js#L795](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L795)  
引入版本：3.0.0


---

### sendToBack {#sendToBack}

#### \<instance> sendToBack(child) {#instance-sendtobackchild}


**说明:**

将给定的孩子送到此列表的底部。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 寄到列表后面的项目 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 被移动的物品。


> 源码：[src/gameobjects/layer/Layer.js#L762](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L762)  
引入版本：3.0.0


---

### setAll {#setAll}

#### \<instance> setAll(property, value, [startIndex], [endIndex]) {#instance-setallproperty-value-startindex-endindex}


**说明:**

将属性 `key` 设置为本列表所有成员的指定值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| property | string | 否 | 设置的地产名称 。 |
| value | any | 否 | 设置属性的值 。 |
| startIndex | number | 是 | 首个启动搜索的孩子索引. |
| endIndex | number | 是 | 最后的婴儿索引要搜索到 |


> 源码：[src/gameobjects/layer/Layer.js#L836](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L836)  
引入版本：3.0.0


---

### setInteractive {#setInteractive}

#### \<instance> setInteractive() {#instance-setinteractive}


**说明:**

无法启用层来输入 。

这个方法无所作为,被保存以确保图层的形状与游戏对象相同.


**Overrides:** Phaser.GameObjects.GameObject#setInteractive


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 这个游戏对象 。


> 源码：[src/gameobjects/layer/Layer.js#L167](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L167)  
引入版本：3.51.0


---

### shuffle {#shuffle}

#### \<instance> shuffle() {#instance-shuffle}


**说明:**

将列表中的项目打乱 。


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 此列表对象 。


> 源码：[src/gameobjects/layer/Layer.js#L804](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L804)  
引入版本：3.0.0


---

### shutdown {#shutdown}

#### \<instance> shutdown() {#instance-shutdown}


**说明:**

清除列表并重现其内部阵列。


**Overrides:** Phaser.GameObjects.GameObject# 低调的


> 源码：[src/gameobjects/layer/Layer.js#L859](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L859)  
引入版本：3.0.0


---

### sort {#sort}

#### \<instance> sort(property, [handler]) {#instance-sortproperty-handler}


**说明:**

排序此列表的内容, 使项目根据给定属性排列 。 例如, `sort('alpha')` 会根据它们的 `alpha` 属性的值排序列表内容 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| property | string | 否 | 地产被逻辑分类。 |
| handler | function | 是 | 提供您自己的自定义处理器功能。 将接收两个孩子, 并返回一个数字( 如果第一个是负数, 则在第二个之前出现, 如果后面出现, 则为零, 如果相等) 。 |


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 此列表对象 。


> 源码：[src/gameobjects/layer/Layer.js#L567](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L567)  
引入版本：3.0.0


---

### sortByDepth {#sortByDepth}

#### \<instance> sortByDepth(childA, childB) {#instance-sortbydepthchilda-childb}


**说明:**

比较两个游戏对象的深度.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| childA | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 第一个游戏对象. |
| childB | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 第二游戏对象. |


**返回值:** number - 每个游戏对象深度的区别.


> 源码：[src/gameobjects/layer/Layer.js#L312](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L312)  
引入版本：3.50.0


---

### swap {#swap}

#### \<instance> swap(child1, child2) {#instance-swapchild1-child2}


**说明:**

交换清单上两个物品的位置。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child1 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 首个换品. |
| child2 | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 换掉的第二个项目 |


> 源码：[src/gameobjects/layer/Layer.js#L657](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L657)  
引入版本：3.0.0


---

### willRender {#willRender}

#### \<instance> willRender(camera) {#instance-willrendercamera}


**说明:**

将 renderMask 和 renderFlags 比较,看看此游戏对象是否渲染。 还可以根据给定的相机排除列表检查游戏对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 用于检查此游戏对象的相机 。 |


**Overrides:** Phaser.GameObjects.GameObject#willRender


**返回值:** boolean - 如果游戏对象应该被渲染, 否则会弄虚作假 。


> 源码：[src/gameobjects/layer/Layer.js#L215](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/Layer.js#L215)  
引入版本：3.50.0


---

---
