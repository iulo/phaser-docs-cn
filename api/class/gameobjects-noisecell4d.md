# NoiseCell4D {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-noisecell4d)

一个噪声Cell4D游戏对象.

此游戏对象是一个四重奏, 显示细胞噪声。 您可以像其它任何一重奏一样操作此对象, 使其具有交互性, 并用在过滤器和面具中, 以产生视觉惊人的效果 。

幕后,一个噪声Cell4D是使用特定遮蔽程序的一种[Phaser.GameObjects.Shader](/api/class/gameobjects-shader).

细胞噪声,又称沃利噪声或沃罗诺伊噪声,由细胞的图案组成,这有利于模拟波,云,或鳞等自然现象.

您可以设置噪音的颜色和透明度、 单元格数、 变异和种子值。 您可以通过增加 `noiseIterations` 来改变细节级别。 您可以改变噪音模式, 输出锐边、 柔软边缘或单元格的平面颜色 。

你可以通过动画`noiseOffset`属性来滚动噪音.

您可以设置 `noiseNormalMap` 输出普通地图。 这是添加照明纹理的快速方式 。

噪声Cell的4D版本有两个额外的维度: Z 和 W 。 着色器只使 XY 切片穿过噪声域。 由于细胞中心通常位于超大容量的其他地方, 细胞在亮度上会变异。 您可以在 Z 轴上滚动, 以切片, 平稳地改变细胞模式。 在 4D 中, 您可以将 ZW 抵消的移动到一个圆中, 从而形成一个不断变化的模式, 重复而不反转或重置。 ZW 环绕技术被推荐用于长期效果, 因为它避免了会导致浮点精确问题的大抵消 。

**构造函数**

`new NoiseCell4D(scene, [config], [x], [y], [width], [height])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属景点 。 |
| config | [Phaser.Types.GameObjects.NoiseCell4D.NoiseCell4DQuadConfig](/api/typedef/types-gameobjects-noisecell4d#noisecell4dquadconfig) | 是 |  | 此游戏对象的配置 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Shader](/api/class/gameobjects-shader)  



> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L12)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


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





**From [Phaser.GameObjects.Shader](/api/class/gameobjects-shader):**


 - [drawingContext](/api/class/gameobjects-shader#drawingContext)
 - [glTexture](/api/class/gameobjects-shader#glTexture)
 - [renderNode](/api/class/gameobjects-shader#renderNode)
 - [renderToTexture](/api/class/gameobjects-shader#renderToTexture)
 - [texture](/api/class/gameobjects-shader#texture)
 - [textureCoordinateBottomLeft](/api/class/gameobjects-shader#textureCoordinateBottomLeft)
 - [textureCoordinateBottomRight](/api/class/gameobjects-shader#textureCoordinateBottomRight)
 - [textureCoordinateTopLeft](/api/class/gameobjects-shader#textureCoordinateTopLeft)
 - [textureCoordinateTopRight](/api/class/gameobjects-shader#textureCoordinateTopRight)
 - [textures](/api/class/gameobjects-shader#textures)




---

## 公开成员 {#public-members}

### keepAwake {#keepAwake}

#### keepAwake: boolean {#keepawake-boolean}


**说明:**

是否将阴影输入抖动以强制持续高精度。 这是一个高级设置 。

Chromium浏览器似乎在WebGL渲染模式之间切换,这改变了噪声遮蔽器可用的精度,这可以改变噪声计算,导致部分输出不可预测的闪烁. `keepAwake`设置在渲染过程中增加了一个无法察觉的偏移量,这似乎迫使Chrimum一致并消除闪烁.

无法控制的问题, 可能不会出现在浏览器或设备中, 但会出现在其他用户身上 。


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L369](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L369)  
引入版本：4.0.0


---

### noiseCells {#noiseCells}

#### noiseCells: Array.\<number> {#noisecells-arraynumber}


**说明:**

每个维度的单元格数。

这一定是4个数字的数组。

尝试将单元格数保持在纹理分辨率的2到约8分之一之间。1的单元格数没有变化的余地。大于纹理分辨率的单元格数本质上将是昂贵的白色噪音。


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L104)  
引入版本：4.0.0


---

### noiseColorEnd {#noiseColorEnd}

#### noiseColorEnd: [Phaser.Display.Color](/api/namespace/display-color) {#noisecolorend-phaserdisplaycolor}


**说明:**

细胞边缘的颜色.

默认是白色的。 您可以设置任何颜色, 并更改 α 。


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L329](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L329)  
引入版本：4.0.0


---

### noiseColorStart {#noiseColorStart}

#### noiseColorStart: [Phaser.Display.Color](/api/namespace/display-color) {#noisecolorstart-phaserdisplaycolor}


**说明:**

细胞中间的颜色.

默认是黑色的。 您可以设置任何颜色, 并更改 α 。


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L318](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L318)  
引入版本：4.0.0


---

### noiseIterations {#noiseIterations}

#### noiseIterations: number {#noiseiterations-number}


**说明:**

需要应用多少八分之八的噪音,这增加了噪音的详细细节,以性能为代价。

每一个八分位的噪音具有两倍的分辨率,对输出的贡献是一半。

此值应该是 1 或 更高 的整数。 5 或 5 以上的值效果越来越小。 每个迭代都有成本, 所以只使用您需要的 !


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L220](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L220)  
引入版本：4.0.0


---

### noiseMode {#noiseMode}

#### noiseMode: number {#noisemode-number}


**说明:**

输出噪音的模式是什么 。

- 0:细胞间有尖锐的边界.

- 1:索引模式,单元格具有单一的平面颜色.

  这是一种随机的,可能不是独一无二的。

- 2: 单元格间平滑边界.

  使用`noiseSmoothing`来控制光滑.


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L242](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L242)  
引入版本：4.0.0


---

### noiseNormalMap {#noiseNormalMap}

#### noiseNormalMap: boolean {#noisenormalmap-boolean}


**说明:**

是否将噪声输出转换为普通映射 。

这与噪声模式0和2一起正常工作,它们形成曲线.

以`noiseNormalScale`控制曲率强度.


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L282](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L282)  
引入版本：4.0.0


---

### noiseNormalScale {#noiseNormalScale}

#### noiseNormalScale: number {#noisenormalscale-number}


**说明:**

普通地图输出的曲线强度。 当启用 `noiseNormalMap` 时使用此功能 。

默认值为 1. 较高的值产生更多的曲率;较低的值为夸张值.

表面角度由噪声变化的速度决定. 迭代较多的噪声往往变化更快,因此有更明显的常态.


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L296](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L296)  
引入版本：4.0.0


---

### noiseOffset {#noiseOffset}

#### noiseOffset: Array.\<number> {#noiseoffset-arraynumber}


**说明:**

每个维度的噪声的偏移:[x,y,z,w]. 动画x和y来滚动噪声模式. 动画z和w来平稳改变噪声模式.

这一定是4个数字的数组。

距离 0 的距离太远将引入浮点精确问题。 这会导致噪音出现阻塞。 我们开始看到明显的阻塞, 相抵数为几千, 所以不要靠近它。

您可以通过滚动 Z 轴来演化噪音模式。 然而, 这最终会满足这些浮点精确问题 。

在四个维度中,您可以通过沿ZW平面的圆向移动来演化噪声模式,这可以平稳地改变模式,而不会离开安全区域,也不需要停止和反转或重置. 4D噪声对于持续滚动的图案非常有用.


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L158)  
引入版本：4.0.0


---

### noiseSeed {#noiseSeed}

#### noiseSeed: Array.\<number> {#noiseseed-arraynumber}


**说明:**

噪声的种子值。 使用这些来改变图案中的细胞形状。 不同的种子会形成完全不同的图案 。

这一定是16个数字的数组。

噪声种子值应该相当小。 建议在 0 至 1 或 0 至 16 之间出现数字。 巨大的种子值可能会失去浮点精度, 并导致噪声出现阻塞 。


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L345](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L345)  
引入版本：4.0.0


---

### noiseSmoothing {#noiseSmoothing}

#### noiseSmoothing: number {#noisesmoothing-number}


**说明:**

在平滑模式下应用的平滑度是多少 。

默认值为 1, 介于单元格之间应用中度平滑。 值是一个系数。 0-1 的值会减少平滑。 1 以上的值会加强平滑。 强度慢于 4 左右 。


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L262](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L262)  
引入版本：4.0.0


---

### noiseVariation {#noiseVariation}

#### noiseVariation: Array.\<number> {#noisevariation-arraynumber}


**说明:**

每个单元格的网格位置可变化多少。高值与网格的距离会更远。

0时,细胞是完全平方的。1时,细胞是完全混乱的。永远不要高于1,因为这会扭曲细胞基质,以至于最近的细胞不在采样范围,从而造成噪音中的缝合。


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L199](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L199)  
引入版本：4.0.0


---

### noiseWrap {#noiseWrap}

#### noiseWrap: Array.\<number> {#noisewrap-arraynumber}


**说明:**

模式的细胞宽度是多少.

默认情况下, 设置到与 `noiseCells` 相同的尺寸。 这会导致输出在边缘无缝地包裹。 如果您更改了设置, 请调用 `this.wrapNoise()` 。

数值较低会导致输出重复.

更高的值会打破可见的包。 单元格模式仍然重复离相机。 尽量保持这个值的低, 因为它有助于避免浮点精度错误 。

这一定是4个数字的数组。


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L126)  
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





**From [Phaser.GameObjects.Shader](/api/class/gameobjects-shader):**


 - [getUniform](/api/class/gameobjects-shader#getUniform)
 - [preDestroy](/api/class/gameobjects-shader#preDestroy)
 - [renderImmediate](/api/class/gameobjects-shader#renderImmediate)
 - [setRenderToTexture](/api/class/gameobjects-shader#setRenderToTexture)
 - [setTextureCoordinates](/api/class/gameobjects-shader#setTextureCoordinates)
 - [setTextureCoordinatesFromFrame](/api/class/gameobjects-shader#setTextureCoordinatesFromFrame)
 - [setTextures](/api/class/gameobjects-shader#setTextures)
 - [setUniform](/api/class/gameobjects-shader#setUniform)
 - [setupUniforms](/api/class/gameobjects-shader#setupUniforms)




---

## 公开方法 {#public-methods}

### randomizeNoiseSeed {#randomizeNoiseSeed}

#### \<instance> randomizeNoiseSeed() {#instance-randomizenoiseseed}


**说明:**

随机产生噪声种子,形成独特的模式.


**返回值:** [Phaser.GameObjects.NoiseCell4D](/api/class/gameobjects-noisecell4d) - 此游戏对象.


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L459](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L459)  
引入版本：4.0.0


---

### setNoiseColor {#setNoiseColor}

#### \<instance> setNoiseColor([start], [end]) {#instance-setnoisecolorstart-end}


**说明:**

设定噪声的颜色, 从各种颜色格式中选择 。

- 一个数字预计为24或32位RGB或ARGB值.

- 字符串是六进制码 。

- 一组数字预计在0-1之间是RGB或RGBA.

- 可用一个颜色对象。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| start | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0x000000" | 细胞中间的颜色. |
| end | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0xffffff" | 细胞边缘的颜色. |


**返回值:** [Phaser.GameObjects.NoiseCell4D](/api/class/gameobjects-noisecell4d) - 此游戏对象.


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L393](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L393)  
引入版本：4.0.0


---

### wrapNoise {#wrapNoise}

#### \<instance> wrapNoise() {#instance-wrapnoise}


**说明:**

设置噪声纹理以无缝包裹.

将`noiseWrap`设定为所有维度的等效`noiseCells`.


**返回值:** [Phaser.GameObjects.NoiseCell4D](/api/class/gameobjects-noisecell4d) - 此游戏对象.


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L476](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4D.js#L476)  
引入版本：4.0.0


---

---
