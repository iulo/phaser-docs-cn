# Blitter {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-blitter)

一个闪烁的游戏对象 。

Blitter Game Object 是一类特殊容器, 用于创建、 更新和管理 Bob 对象。 Bob 是为渲染速度而不是灵活性而设计的。 它们由纹理、 或纹理、 位置和α值的帧组成。 您不能缩放或旋转它们。 在渲染速度时,它们使用批量绘图方法 。

闪光游戏对象有一个纹理绑定在它上。 闪光游戏创建的鲍勃可以使用这个纹理中的任何框架来渲染, 但是他们不能使用其他的纹理。 正是这个单一的纹理- 包, 允许它们速度 。

如果您需要将大量框架在屏幕周围爆破, 那么闪光物体就值得调查。 它们对使用自己的特效系统特别有用 。

**构造函数**

`new Blitter(scene, [x], [y], [texture], [frame])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属的景点。 它只能在任何特定时间属于一个景点 。 |
| x | number | 是 | 0 | 世界空间中此游戏对象的x坐标 。 |
| y | number | 是 | 0 | 游戏对象在世界空间中的y坐标 。 |
| texture | string | 是 | "'__DEFAULT'" | 游戏对象用于渲染的纹理键。 纹理管理器中必须已经存在 。 |
| frame | string \| number | 是 | 0 | 此游戏对象将使用的纹理帧。 只有在纹理有多个框架, 如纹理图集或 精灵表时才会设置 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting)  
> [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask)  
> [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  
> [Phaser.GameObjects.Components.Size](/api/namespace/gameobjects-components-size)  
> [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/blitter/Blitter.js#L23](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Blitter.js#L23)  
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





**From [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes):**


 - [customRenderNodes](/api/namespace/gameobjects-components-rendernodes#customRenderNodes)
 - [defaultRenderNodes](/api/namespace/gameobjects-components-rendernodes#defaultRenderNodes)
 - [renderNodeData](/api/namespace/gameobjects-components-rendernodes#renderNodeData)





**From [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor):**


 - [scrollFactorX](/api/namespace/gameobjects-components-scrollfactor#scrollFactorX)
 - [scrollFactorY](/api/namespace/gameobjects-components-scrollfactor#scrollFactorY)





**From [Phaser.GameObjects.Components.Size](/api/namespace/gameobjects-components-size):**


 - [displayHeight](/api/namespace/gameobjects-components-size#displayHeight)
 - [displayWidth](/api/namespace/gameobjects-components-size#displayWidth)
 - [height](/api/namespace/gameobjects-components-size#height)
 - [width](/api/namespace/gameobjects-components-size#width)





**From [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture):**


 - [frame](/api/namespace/gameobjects-components-texture#frame)
 - [texture](/api/namespace/gameobjects-components-texture#texture)





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

### children {#children}

#### children: Phaser.Structs.List.\<Phaser.GameObjects.Bob> {#children-phaserstructslistphasergameobjectsbob}


**说明:**

此闪光器的子嗣。 此列表包含闪光器创建的所有 Bob 对象 。


> 源码：[src/gameobjects/blitter/Blitter.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Blitter.js#L92)  
引入版本：3.0.0


---

### dirty {#dirty}

#### dirty: boolean {#dirty-boolean}


**说明:**

闪光灯是否被认为是脏的? 自上个框架以来, 闪光灯的孩子数已经改变 。


> 源码：[src/gameobjects/blitter/Blitter.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Blitter.js#L114)  
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





**From [Phaser.GameObjects.Components.Size](/api/namespace/gameobjects-components-size):**


 - [setDisplaySize](/api/namespace/gameobjects-components-size#setDisplaySize)
 - [setSize](/api/namespace/gameobjects-components-size#setSize)
 - [setSizeToFrame](/api/namespace/gameobjects-components-size#setSizeToFrame)





**From [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture):**


 - [setFrame](/api/namespace/gameobjects-components-texture#setFrame)
 - [setTexture](/api/namespace/gameobjects-components-texture#setTexture)





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

### childCanRender {#childCanRender}

#### \<instance> childCanRender(child) {#instance-childcanrenderchild}


**说明:**

通过检查其`visible`和`alpha`值,检查给定孩子是否能够渲染.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.Bob](/api/class/gameobjects-bob) | 否 | 鲍勃检查的渲染。 |


**返回值:** boolean - 如果给定的孩子能制得,则返回`true`,否则返回`false`.


> 源码：[src/gameobjects/blitter/Blitter.js#L250](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Blitter.js#L250)  
引入版本：3.0.0


---

### clear {#clear}

#### \<instance> clear() {#instance-clear}


**说明:**

从孩子名单中删除所有鲍勃,并标记闪光剂为脏.


> 源码：[src/gameobjects/blitter/Blitter.js#L285](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Blitter.js#L285)  
引入版本：3.0.0


---

### create {#create}

#### \<instance> create(x, y, [frame], [visible], [index]) {#instance-createx-y-frame-visible-index}


**说明:**

在此闪烁中创建新 Bob 。

鲍勃在给定坐标处创建,相对闪光器,并使用给定帧. 鲍勃可以使用属于捆绑在闪光器上的纹理的任何帧.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | Bob的x位置. Bob坐标相对闪光物体的位置. |
| y | number | 否 |  | Bob的y位置 。 Bob 坐标相对于闪光物体的位置 。 |
| frame | string \| number | [Phaser.Textures.Frame](/api/class/textures-frame) | 是 |  | Bob 将使用的框架。 它必须是父闪点对象所使用的纹理的一部分 。 |
| visible | boolean | 是 | true | 造物主鲍勃到底该不该造物呢? |
| index | number | 是 |  | 闪烁显示列表中的位置, 以添加新的 Bob 。 默认为列表的首位 。 |


**返回值:** [Phaser.GameObjects.Bob](/api/class/gameobjects-bob) - 新建的鲍勃对象 。


> 源码：[src/gameobjects/blitter/Blitter.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Blitter.js#L142)  
引入版本：3.0.0


---

### createFromCallback {#createFromCallback}

#### \<instance> createFromCallback(callback, quantity, [frame], [visible]) {#instance-createfromcallbackcallback-quantity-frame-visible}


**说明:**

在此闪烁器内创建多个 Bob 对象, 然后将每个对象传递到指定的回调 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| callback | CreateCallback | 否 |  | 创建 bb 后调用。 将会发送两个参数: 鲍勃 和 鲍勃 索引 。 |
| quantity | number | 否 |  | 鲍勃的设定数量 |
| frame | string \| number | [Phaser.Textures.Frame](/api/class/textures-frame) | Array.\<string> | Array.\<number> | Array.\<[Phaser.Textures.Frame](/api/class/textures-frame)> | 是 |  | Bobs将使用的框架。 它必须是闪光纹理的一部分 。 |
| visible | boolean | 是 | true | 造物主鲍勃到底该不该造物呢? |


**返回值:** Array.\<[Phaser.GameObjects.Bob](/api/class/gameobjects-bob)> - 创建的一组 Bob 对象 。


> 源码：[src/gameobjects/blitter/Blitter.js#L182](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Blitter.js#L182)  
引入版本：3.0.0


---

### createMultiple {#createMultiple}

#### \<instance> createMultiple(quantity, [frame], [visible]) {#instance-createmultiplequantity-frame-visible}


**说明:**

在一个呼叫中创建多个鲍勃.

创建的量由`quantity`参数和所提供的帧数的组合来控制.

如果数量被设定为10,你提供2帧,那么20个Bob将创建. 10个与第一个帧,10个与第二个帧.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| quantity | number | 否 |  | 鲍勃的设定数量 |
| frame | string \| number | [Phaser.Textures.Frame](/api/class/textures-frame) | Array.\<string> | Array.\<number> | Array.\<[Phaser.Textures.Frame](/api/class/textures-frame)> | 是 |  | Bobs将使用的框架。 它必须是闪光纹理的一部分 。 |
| visible | boolean | 是 | true | 造物主鲍勃到底该不该造物呢? |


**返回值:** Array.\<[Phaser.GameObjects.Bob](/api/class/gameobjects-bob)> - 创建的一组 Bob 对象 。


> 源码：[src/gameobjects/blitter/Blitter.js#L209](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Blitter.js#L209)  
引入版本：3.0.0


---

### getRenderList {#getRenderList}

#### \<instance> getRenderList() {#instance-getrenderlist}


**说明:**

返回要渲染的 Bob 数组。 如果闪烁器脏了, 则生成新的列表, 并存储在 `renderList` 中 。


**返回值:** Array.\<[Phaser.GameObjects.Bob](/api/class/gameobjects-bob)> - 将制成此帧的 Bob 对象数组 。


> 源码：[src/gameobjects/blitter/Blitter.js#L265](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Blitter.js#L265)  
引入版本：3.0.0


---

### preDestroy {#preDestroy}

#### \<instance> preDestroy() {#instance-predestroy}


**说明:**

销毁对象时调用的内部处理函数。


**访问权限:** 受保护


> 源码：[src/gameobjects/blitter/Blitter.js#L297](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Blitter.js#L297)  
引入版本：3.9.0


---

---
