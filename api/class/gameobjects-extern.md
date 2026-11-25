# Extern {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-extern)

Extern Game Object是一类特殊的游戏Object,它允许您将渲染传递给第三派对.

当创建Extern并把它放入显示景物的列表时,渲染器会一如既往地处理列表。当它找到extern时,会冲洗当前批次并准备一个变换矩阵,如果需要,你的渲染功能可以利用。

电话 WebGL 上下文会处于“干净”状态,可以将自己的遮阳镜绑起来,或者画进它,无论你想做什么。如果这一切都发生在 `render` 方法。部署一个极端对象的正确方式是创建扩展其范围的类,然后覆盖 `render` (可选) `preUpdate`) 方法和将控制权传递给您第3党的图书馆或风俗 WebGL 密码

`render`方法的命名就是这个签名:`render(renderer: Phaser.Renderer.WebGL.WebGLRenderer, drawingContext: Phaser.Renderer.WebGL.DrawingContext, calcMatrix: Phaser.GameObjects.Components.TransformMatrix, displayList: Phaser.GameObjects.GameObject[], displayListIndex: number): void`.

`displayList`和`displayListIndex`参数允许您检查显示列表中的其他对象。 这可能有助于优化资源管理等操作。

一旦完成, 您应该腾出任何资源。 Extern 将返回 Phaser 状态, 并继续渲染显示列表 。

虽然此天体具有阿尔法,混合模式和丁特等许多属性,但在渲染过程中,除非您在自己的渲染码中利用它们,否则它们都无一使用.

**构造函数**

`new Extern(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip)  
> [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  
> [Phaser.GameObjects.Components.Size](/api/namespace/gameobjects-components-size)  
> [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture)  
> [Phaser.GameObjects.Components.Tint](/api/namespace/gameobjects-components-tint)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/extern/Extern.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/extern/Extern.js#L12)  
引入版本：3.16.0

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





**From [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip):**


 - [resetFlip](/api/namespace/gameobjects-components-flip#resetFlip)
 - [setFlip](/api/namespace/gameobjects-components-flip#setFlip)
 - [setFlipX](/api/namespace/gameobjects-components-flip#setFlipX)
 - [setFlipY](/api/namespace/gameobjects-components-flip#setFlipY)
 - [toggleFlipX](/api/namespace/gameobjects-components-flip#toggleFlipX)
 - [toggleFlipY](/api/namespace/gameobjects-components-flip#toggleFlipY)





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





**From [Phaser.GameObjects.Components.Size](/api/namespace/gameobjects-components-size):**


 - [setDisplaySize](/api/namespace/gameobjects-components-size#setDisplaySize)
 - [setSize](/api/namespace/gameobjects-components-size#setSize)
 - [setSizeToFrame](/api/namespace/gameobjects-components-size#setSizeToFrame)





**From [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture):**


 - [setFrame](/api/namespace/gameobjects-components-texture#setFrame)
 - [setTexture](/api/namespace/gameobjects-components-texture#setTexture)





**From [Phaser.GameObjects.Components.Tint](/api/namespace/gameobjects-components-tint):**


 - [clearTint](/api/namespace/gameobjects-components-tint#clearTint)
 - [setTint](/api/namespace/gameobjects-components-tint#setTint)
 - [setTintFill](/api/namespace/gameobjects-components-tint#setTintFill)
 - [setTintMode](/api/namespace/gameobjects-components-tint#setTintMode)





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


 - [addToDisplayList](/api/class/gameobjects-gameobject#addToDisplayList)
 - [addToUpdateList](/api/class/gameobjects-gameobject#addToUpdateList)
 - [destroy](/api/class/gameobjects-gameobject#destroy)
 - [disableInteractive](/api/class/gameobjects-gameobject#disableInteractive)
 - [getData](/api/class/gameobjects-gameobject#getData)
 - [getDisplayList](/api/class/gameobjects-gameobject#getDisplayList)
 - [getIndexList](/api/class/gameobjects-gameobject#getIndexList)
 - [incData](/api/class/gameobjects-gameobject#incData)
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

### addedToScene {#addedToScene}

#### \<instance> addedToScene() {#instance-addedtoscene}


**说明:**

当此外观被添加到场景中时调用 。

将Exten 与 Scene 更新列表一起注册,这样 `preUpdate` 就可以称为每个帧 。


**Overrides:** Phaser.GameObjects.GameObject#addedToScene


> 源码：[src/gameobjects/extern/Extern.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/extern/Extern.js#L104)  
引入版本：3.50.0


---

### preUpdate {#preUpdate}

#### \<instance> preUpdate(time, delta) {#instance-preupdatetime-delta}


**说明:**

由场景更新列表自动调用每个帧 。

在自己的类中覆盖这种方法,以添加自定义逻辑,该逻辑应该运行每个帧,例如更新动画或物理.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间戳,由请求动画框架或SetTimeout生成. |
| delta | number | 否 | 三角洲时间,以ms计, 过去了,自上一个框架。 |


> 源码：[src/gameobjects/extern/Extern.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/extern/Extern.js#L130)  
引入版本：3.16.0


---

### removedFromScene {#removedFromScene}

#### \<instance> removedFromScene() {#instance-removedfromscene}


**说明:**

取出场景时调用 。

从 Scene 更新列表中删除extern, 这样 `preUpdate` 不再被调用 。


**Overrides:** Phaser.GameObjects.GameObject#removedFromScene


> 源码：[src/gameobjects/extern/Extern.js#L117](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/extern/Extern.js#L117)  
引入版本：3.50.0


---

### render {#render}

#### \<instance> render(renderer, drawingContext, calcMatrix, displayList, displayListIndex) {#instance-renderrenderer-drawingcontext-calcmatrix-displaylist-displaylistindex}


**说明:**

覆盖您自己的类中此方法以提供自定义渲染逻辑 。

当渲染器在显示列表中遇到此Extern时,它会冲洗当前批次,准备一个变换矩阵,并将WebGL上下文置于干净状态,以便您绑定自己的遮阳器或绘制调用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 电话 WebGL 伦德勒的例子。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| calcMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 此Extern 的计算变形矩阵 。 |
| displayList | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 场景当前显示列表 。 |
| displayListIndex | number | 否 | 显示列表中此extern 的索引 。 |


> 源码：[src/gameobjects/extern/Extern.js#L148](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/extern/Extern.js#L148)  
引入版本：3.16.0


---

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





**From [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip):**


 - [flipX](/api/namespace/gameobjects-components-flip#flipX)
 - [flipY](/api/namespace/gameobjects-components-flip#flipY)





**From [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin):**


 - [displayOriginX](/api/namespace/gameobjects-components-origin#displayOriginX)
 - [displayOriginY](/api/namespace/gameobjects-components-origin#displayOriginY)
 - [originX](/api/namespace/gameobjects-components-origin#originX)
 - [originY](/api/namespace/gameobjects-components-origin#originY)





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





**From [Phaser.GameObjects.Components.Tint](/api/namespace/gameobjects-components-tint):**


 - [isTinted](/api/namespace/gameobjects-components-tint#isTinted)
 - [tint](/api/namespace/gameobjects-components-tint#tint)
 - [tintBottomLeft](/api/namespace/gameobjects-components-tint#tintBottomLeft)
 - [tintBottomRight](/api/namespace/gameobjects-components-tint#tintBottomRight)
 - [tintMode](/api/namespace/gameobjects-components-tint#tintMode)
 - [tintTopLeft](/api/namespace/gameobjects-components-tint#tintTopLeft)
 - [tintTopRight](/api/namespace/gameobjects-components-tint#tintTopRight)





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

---
