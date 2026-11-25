# NineSlice {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-nineslice)

九切游戏对象允许您显示一个既可以水平伸展又可以垂直伸展的纹理对象,但保留固定大小的角。角的尺寸通过参数设定到此类。

这对UI和元素等按钮极为有用,需要它们扩展以容纳内容而不扭曲纹理.

您为此游戏对象提供的纹理应该基于以下布局结构:

```
     A                          B
   +---+----------------------+---+
 C | 1 |          2           | 3 |
   +---+----------------------+---+
   |   |                      |   |
   | 4 |          5           | 6 |
   |   |                      |   |
   +---+----------------------+---+
 D | 7 |          8           | 9 |
   +---+----------------------+---+
```

更改对象宽度和 / 或高度时:

区域1、3、7和9(角)将保持无标

    areas 2 and 8 will be stretched horizontally only

    areas 4 and 6 will be stretched vertically only

    area 5 will be stretched both horizontally and vertically

您也可以创建3个切片游戏对象 :

这种方法效果类似,但只能水平拉伸。 因此,它需要更少的配置:

```
     A                          B
   +---+----------------------+---+
   |   |                      |   |
 C | 1 |          2           | 3 |
   |   |                      |   |
   +---+----------------------+---+
```

更改对象宽度时( 您不能更改其高度)

区域1和3将保持不变

    area 2 will be stretched horizontally

上述配置概念改编自Pixi NineSlicesPlane.

要指定一个3个切片对象而不是9个切片, 您只应该提供 `leftWidth` 和 `rightWidth` 参数。 要创建 9 个切片, 您必须提供所有参数 。

此游戏对象最小宽度的(_L) 共 `leftWidth` + `rightWidth`中,该游戏对象的高度可以达到 _最小_高度。 `topHeight` + `bottomHeight`。如果需要以较小的尺寸显示此对象,可以将其缩放。

在性能方面,使用3切游戏对象相当于连续有3个Sprites. 使用9切游戏对象相当于连续9个Sprites,这个对象的顶点全部进行批次,可以与显示列表上的其他Sprites和图形共存,而不会引起任何额外的间接费用.

如果在 Tetricure Packer 7.1.0 或以上 并用 json 地图集导出, 此游戏对象现在可以自动填充其值。 如果是这样的话, 您可以只创建此游戏对象, 而不指定任何超出纹理键和框架的字段, 它会从地图集中提取区域数据 。

此对象不支持纹理包件的修剪纹理, 修剪干扰了纹理正确拉伸的能力 。

**构造函数**

`new NineSlice(scene, x, y, texture, [frame], [width], [height], [leftWidth], [rightWidth], [topHeight], [bottomHeight], [tileX], [tileY])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| x | number | 否 |  | 这个游戏对象的中心在世界的横向位置. |
| y | number | 否 |  | 这个游戏对象的中心在世界的垂直位置. |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 |  | 此游戏对象将使用用于渲染的纹理的键或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 |  | 游戏对象正在用此渲染的纹理的可选框架 。 |
| width | number | 是 | 256 | 九切游戏对象的宽度。 您可以调整创建后的宽度 。 |
| height | number | 是 | 256 | 九切游戏对象的高度。 如果这是 3 切片对象, 高度将固定到纹理高度, 无法更改 。 |
| leftWidth | number | 是 | 10 | 左纵列的大小(A). |
| rightWidth | number | 是 | 10 | 右垂直列的大小(B). |
| topHeight | number | 是 | 0 | 水平线顶端的大小( C) 。 设置为 0 或未定义以创建 3 个切片对象 。 |
| bottomHeight | number | 是 | 0 | 下水平行的大小( D) 。 设置为 0 或未定义以创建 3 个切片对象 。 |
| tileX | boolean | 是 | false | 启用时, 可伸缩水平区域会重复在对象之间, 而不是被拉伸。 每个瓦片仍然略微拉伸, 使其完全可见, 这可能会造成轻微的扭曲, 但远小于纯伸展。 纹理应该无缝, 以避免在瓦片之间出现可见的文物 。 |
| tileY | boolean | 是 | false | 启用时, 可伸缩的垂直区域会重复在对象之间, 而不是被拉伸。 每个瓦片仍然略微拉伸, 使其完全可见, 这可能会造成轻微的扭曲, 但远小于纯伸展。 纹理应该无缝, 以避免在瓦片之间出现可见的文物 。 |

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
> [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/nineslice/NineSlice.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L15)  
引入版本：3.60.0

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





**From [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes):**


 - [customRenderNodes](/api/namespace/gameobjects-components-rendernodes#customRenderNodes)
 - [defaultRenderNodes](/api/namespace/gameobjects-components-rendernodes#defaultRenderNodes)
 - [renderNodeData](/api/namespace/gameobjects-components-rendernodes#renderNodeData)





**From [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor):**


 - [scrollFactorX](/api/namespace/gameobjects-components-scrollfactor#scrollFactorX)
 - [scrollFactorY](/api/namespace/gameobjects-components-scrollfactor#scrollFactorY)





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

### bottomHeight {#bottomHeight}

#### bottomHeight: number {#bottomheight-number}


**说明:**

底水平栏的大小 (D).

如果这是3个切片对象, 此属性将被设定为零 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L268](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L268)  
引入版本：3.60.0


---

### displayHeight {#displayHeight}

#### displayHeight: number {#displayheight-number}


**说明:**

此游戏对象的显示高度 。

这一数值考虑到了比额表系数。

设置此值将调整游戏对象的缩放属性 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L1033](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L1033)  
引入版本：3.60.0


---

### displayWidth {#displayWidth}

#### displayWidth: number {#displaywidth-number}


**说明:**

此游戏对象的显示宽度 。

这一数值考虑到了比额表系数。

设置此值将调整游戏对象的缩放属性 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L1008](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L1008)  
引入版本：3.60.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

此游戏对象的显示高度 。

设置此值将垂直调整此九切对象的缩放方式, 如果配置的话 。

此游戏对象最小高度的 _ 最小高度可以是 `topHeight` + `bottomHeight`。 如果您需要以较小的大小显示此对象, 您也可以缩放它 。

如果这是三切对象,只能水平伸展,改变高度会被忽略.


> 源码：[src/gameobjects/nineslice/NineSlice.js#L972](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L972)  
引入版本：3.60.0


---

### is3Slice {#is3Slice}

#### is3Slice: boolean {#is3slice-boolean}


**说明:**

这块地产是 `true` 如果此九切游戏对象配置为 Just `leftWidth` 财务报告和已审计财务报表 `rightWidth` 值,使其成为3-切而不是9-切对象。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L355](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L355)  
引入版本：3.60.0


---

### isTinted {#isTinted}

#### isTinted: boolean {#istinted-boolean}


**说明:**

此游戏对象是否应用了 tin ?

它检查是否将锡克属性设定为 0xffffff 以外的值, 或者锡克模式不是默认的 Phaser.TintModes.MULTIPLY 。 这表明游戏对象已有锡值 。

**标签:**

 - webglOnly


> 源码：[src/gameobjects/nineslice/NineSlice.js#L920](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L920)  
引入版本：3.60.0


---

### leftWidth {#leftWidth}

#### leftWidth: number {#leftwidth-number}


**说明:**

左侧垂直栏的大小(A).


> 源码：[src/gameobjects/nineslice/NineSlice.js#L235](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L235)  
引入版本：3.60.0


---

### originX {#originX}

#### originX: number {#originx-number}


**说明:**

此游戏对象的横向起源。 来源图示了游戏对象大小和位置之间的关系。 默认值为 0. 5, 表示所有游戏对象的位置都基于其中心。 设定值为 0 表示该位置与游戏对象左侧有关 。


**重写:** Phaser.GameObjects.Components.Origin#originX


> 源码：[src/gameobjects/nineslice/NineSlice.js#L1118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L1118)  
引入版本：3.60.0


---

### originY {#originY}

#### originY: number {#originy-number}


**说明:**

此游戏对象的垂直来源。 来源图示了游戏对象大小和位置之间的关系。 默认值为 0. 5, 表示所有游戏对象的位置都是基于其中心。 设定值为 0 表示当前位置与游戏对象顶端相关 。


**重写:** Phaser.GameObjects.Components.Origin#originY


> 源码：[src/gameobjects/nineslice/NineSlice.js#L1143](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L1143)  
引入版本：3.60.0


---

### rightWidth {#rightWidth}

#### rightWidth: number {#rightwidth-number}


**说明:**

右垂直栏的大小(B).


> 源码：[src/gameobjects/nineslice/NineSlice.js#L245](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L245)  
引入版本：3.60.0


---

### tileX {#tileX}

#### tileX: boolean {#tilex-boolean}


**说明:**

指示九块线的可伸缩水平区域是否在对象之间重复,而不是被拉伸。每个瓦片仍然略微拉伸,以便保持其全可见 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L280](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L280)  
引入版本：4.0.0


---

### tileY {#tileY}

#### tileY: boolean {#tiley-boolean}


**说明:**

指示九切的可伸缩垂直区域是否在对象之间重复,而不是被拉伸。每个瓦片仍然略微拉伸,以便保持其全可见 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L292](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L292)  
引入版本：4.0.0


---

### tint {#tint}

#### tint: number {#tint-number}


**说明:**

正在应用到游戏对象的锡值。 值应该设置为十六进制数字, 即: 0xff000 表示红色, 0xff00ff表示紫色 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L324](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L324)  
引入版本：3.60.0


---

### tintMode {#tintMode}

#### tintMode: [Phaser.TintModes](/api/namespace/tintmodes) {#tintmode-phasertintmodes}


**说明:**

将锡剂应用到纹理时使用的锡剂模式 。

可用模式有:

- Phaser.TintModes.MULTIPLY( 默认)

- Phaser.TintModes.FILL

- Phaser.TintModes.ADD

- Phaser.TintModes.SCREEN

- Phaser.TintModes.OVERLAY

- Phaser.TintModes.HARD_LIGHT


> 源码：[src/gameobjects/nineslice/NineSlice.js#L335](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L335)  
引入版本：4.0.0


---

### topHeight {#topHeight}

#### topHeight: number {#topheight-number}


**说明:**

上水平栏的大小(C).

如果这是3个切片对象, 此属性将被设定为使用的纹理高度 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L255](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L255)  
引入版本：3.60.0


---

### vertices {#vertices}

#### vertices: Array.\<[Phaser.GameObjects.NineSliceVertex](/api/class/gameobjects-nineslicevertex)> {#vertices-arrayphasergameobjectsnineslicevertex}


**说明:**

一组对应此九切游戏对象的四位数的Vertex对象。 其保存顺序如下 :

左上方 - 指数0 - 5 上中 - 指数6 - 11 右上方 - 指数12 - 17 左上方 - (英文) 指数18 - 23 中 - 指数24 - 29 中 - 指数30 - 35 左下方 - 指数36 - 41 下方中心 - 指数42 - 47 右下方 - 指数48 - 53 右下方 - (英文)

每个四边形由6个Vertex实例代表.

这个阵列将包含一个3个切片对象的18个元素,一个9个切片对象的54个元素.

已装入此阵列后, 您就不应该修改 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L208](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L208)  
引入版本：3.60.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

此游戏对象的显示宽度 。

如果配置, 设置此值将水平调整此九切对象的缩放方式 。

此游戏对象最小的宽度可以是 `leftWidth` + `rightWidth` 的总计。 如果您需要以较小的大小显示此对象, 您也可以缩放它 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L942](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L942)  
引入版本：3.60.0


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

### clearTint {#clearTint}

#### \<instance> clearTint() {#instance-cleartint}


**说明:**

清除与此游戏对象相关的所有锡值。

立即将颜色值设定为0xffffff,将锡类型设定为"倍数",这导致纹理没有明显变化.

**标签:**

 - webglOnly


**返回值:** [Phaser.GameObjects.NineSlice](/api/class/gameobjects-nineslice) - 此游戏对象实例 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L842](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L842)  
引入版本：3.60.0


---

### setDisplaySize {#setDisplaySize}

#### \<instance> setDisplaySize(width, height) {#instance-setdisplaysizewidth-height}


**说明:**

设定此游戏对象的显示大小。

调用这个会调整比例表。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 此游戏对象的宽度 。 |
| height | number | 否 | 此游戏对象的高度 。 |


**返回值:** [Phaser.GameObjects.NineSlice](/api/class/gameobjects-nineslice) - 此游戏对象实例 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L1097](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L1097)  
引入版本：3.60.0


---

### setOrigin {#setOrigin}

#### \<instance> setOrigin([x], [y]) {#instance-setoriginx-y}


**说明:**

设置此游戏对象的源头 。

数值在0到1之间。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0.5 | 水平源值 。 |
| y | number | 是 | "x" | 垂直源值。 如果定义不明确, 则将设定为 `x` 值 。 |


**重写:** Phaser.GameObjects.Components.Origin#setOrigin


**返回值:** [Phaser.GameObjects.NineSlice](/api/class/gameobjects-nineslice) - 此游戏对象实例 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L1168](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L1168)  
引入版本：3.60.0


---

### setSize {#setSize}

#### \<instance> setSize(width, height) {#instance-setsizewidth-height}


**说明:**

设定此游戏对象的大小 。

对于一个九切游戏对象,这意味着它会根据给定的尺寸,按照它如何配置为各种角大小,在水平和垂直上进行拉伸(或缩缩放).

如果这是三切对象,只能水平伸展,改变高度会被忽略.

如果您启用了此游戏对象进行输入, 更改大小也会改变命中区域的大小 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 此游戏对象的宽度 。 |
| height | number | 否 | 此游戏对象的高度 。 |


**返回值:** [Phaser.GameObjects.NineSlice](/api/class/gameobjects-nineslice) - 此游戏对象实例 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L1058](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L1058)  
引入版本：3.60.0


---

### setSizeToFrame {#setSizeToFrame}

#### \<instance> setSizeToFrame() {#instance-setsizetoframe}


**说明:**

重置此九切游戏对象的大小, 以匹配当前纹理帧 。

对于一个3-slice对象,此设定高度以匹配帧高度并刷新紫外线坐标。对于一个9-slice对象来说,只有紫外线才刷新。当纹理帧发生变化时,此名称会自动调用,通常不需要直接调用。


**返回值:** [Phaser.GameObjects.NineSlice](/api/class/gameobjects-nineslice) - 此游戏对象实例 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L1194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L1194)  
引入版本：3.60.0


---

### setSlices {#setSlices}

#### \<instance> setSlices([width], [height], [leftWidth], [rightWidth], [topHeight], [bottomHeight], [skipScale9]) {#instance-setsliceswidth-height-leftwidth-rightwidth-topheight-bottomheight-skipscale9}


**说明:**

重置此 NineSlice 游戏对象的宽度、 高度和切片 。

这使得您可以修改此对象正在使用的纹理,然后重置切片配置,以避免为了用于不同的游戏元素而不得不破坏此游戏对象.

请注意,您不能将9号切片改为3号切片,反之亦然。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 是 | 256 | 九切游戏对象的宽度。 您可以调整创建后的宽度 。 |
| height | number | 是 | 256 | 九切游戏对象的高度。 如果这是 3 切片对象, 高度将固定到纹理高度, 无法更改 。 |
| leftWidth | number | 是 | 10 | 左纵列的大小(A). |
| rightWidth | number | 是 | 10 | 右垂直列的大小(B). |
| topHeight | number | 是 | 0 | 水平线顶端的大小( C) 。 设置为 0 或未定义以创建 3 个切片对象 。 |
| bottomHeight | number | 是 | 0 | 下水平行的大小( D) 。 设置为 0 或未定义以创建 3 个切片对象 。 |
| skipScale9 | boolean | 是 | false | 如果此九切是从Texture Packer 缩放9 地图集数据创建的,请设置此属性,以使用指定的列大小,而不是 JSON 中指定的大小 。 |


**返回值:** [Phaser.GameObjects.NineSlice](/api/class/gameobjects-nineslice) - 此游戏对象实例 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L407](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L407)  
引入版本：3.60.0


---

### setTint {#setTint}

#### \<instance> setTint([color]) {#instance-settintcolor}


**说明:**

设置此游戏对象的颜色 。

锡特将一个颜色应用到Game Object的纹理中的像素颜色值中,它是用`setTintMode`或`tintMode`属性设定的几种模式之一.

要修改设置后的锡色,要么用新的值再次调用这种方法,要么使用`tint`属性.

要删除一个叫 `clearTint` 的锡, 或者用这个没有参数的法调用 。

**标签:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| color | number | 是 | "0xffffff" | 将该符号应用到整个游戏对象中 。 |


**返回值:** [Phaser.GameObjects.NineSlice](/api/class/gameobjects-nineslice) - 此游戏对象实例 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L862](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L862)  
引入版本：3.60.0


---

### setTintMode {#setTintMode}

#### \<instance> setTintMode([mode]) {#instance-settintmodemode}


**说明:**

设置此游戏对象的锡特模式。

锡特模式在几种模式中的一种,对Game Object的纹理中的像素颜色值应用了一种颜色:

- Phaser.TintModes.MULTIPLY( 默认)

- Phaser.TintModes.FILL

- Phaser.TintModes.ADD

- Phaser.TintModes.SCREEN

- Phaser.TintModes.OVERLAY

- Phaser.TintModes.HARD_LIGHT

**标签:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| mode | [Phaser.TintModes](/api/namespace/tintmodes) | 是 | "Phaser.TintModes.MULTIPLY" | 使用锡金模式 。 |


**返回值:** [Phaser.GameObjects.NineSlice](/api/class/gameobjects-nineslice) - 此游戏对象实例 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L891](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L891)  
引入版本：4.0.0


---

### updateQuad {#updateQuad}

#### \<instance> updateQuad(offset, x1, y1, x2, y2) {#instance-updatequadoffset-x1-y1-x2-y2}


**说明:**

内部更新给定四面体偏移所有顶点的位置坐标。

一般不需要直接使用这种方法,但如果扩展类需要,则该方法会对外开放。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| offset | number | 否 | 乘以四角形的顶点阵列进行更新。 |
| x1 | number | 否 | 四角体左上角的X坐标,在正态空间(-0.5至0.5). |
| y1 | number | 否 | 四角形的左上方Y坐标,在正态空间(-0.5至0.5). |
| x2 | number | 否 | 四方的下方右X坐标,在正态空间(-0.5至0.5). |
| y2 | number | 否 | 四方的下方右Y坐标,在正态空间(-0.5至0.5). |


> 源码：[src/gameobjects/nineslice/NineSlice.js#L756](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L756)  
引入版本：3.60.0


---

### updateQuadUVs {#updateQuadUVs}

#### \<instance> updateQuadUVs(offset, u1, v1, u2, v2) {#instance-updatequaduvsoffset-u1-v1-u2-v2}


**说明:**

根据框架大小,在内部更新特定四面体所有顶点的紫外线坐标。

一般不需要直接使用这种方法,但如果扩展类需要,则该方法会对外开放。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| offset | number | 否 | 乘以四角形的顶点阵列进行更新。 |
| u1 | number | 否 | 四方左上方的U坐标,在0到1之间. |
| v1 | number | 否 | 四方左上方的V坐标,在0到1之间. |
| u2 | number | 否 | 四方的下方右方U坐标,在0到1之间. |
| v2 | number | 否 | 四方的下方右侧V坐标,在0到1之间. |


> 源码：[src/gameobjects/nineslice/NineSlice.js#L789](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L789)  
引入版本：3.60.0


---

### updateUVs {#updateUVs}

#### \<instance> updateUVs() {#instance-updateuvs}


**说明:**

更新顶点紫外线坐标。在创建九角星游戏对象时,或者在纹理帧发生变化时,此名称会自动被称作。

不同于 `updateVertices` 方法, 如果九切会改变大小, 您不需要使用这种方法。 只有它会改变纹理帧 。


> 源码：[src/gameobjects/nineslice/NineSlice.js#L504](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L504)  
引入版本：3.60.0


---

### updateVertices {#updateVertices}

#### \<instance> updateVertices() {#instance-updatevertices}


**说明:**

根据“九切”游戏对象重算此九切游戏对象中的所有顶点 `leftWidth`, `rightWidth`, `topHeight`, `bottomHeight`, `tileX` 财务报告和已审计财务报表 `tileY` 属性,结合游戏对象大小。

当创建此对象或改变其来源时,此方法会自动被称作.

通常你不需要直接调用这种方法,但是如果在创建后发现需要修改其中之一属性,则这种方法会被公之于众.


> 源码：[src/gameobjects/nineslice/NineSlice.js#L580](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSlice.js#L580)  
引入版本：3.60.0


---

---
