# NoiseSimplex2D {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-noisesimplex2d)

一个噪声Simplex2D对象.

此游戏对象是一个四重奏, 显示简单x噪声。 您可以像其它任何声音一样操纵此对象, 使其具有交互性, 并用在过滤器和面具中, 以创建视觉惊人的效果 。

幕后,一个噪声Simple2D是一个使用特定遮荫程序(英语:See Phaser.GameObjects.Shader)的XQSee ZZZX}.

Simplex噪声是柔软自然现象的一种光滑模式理想,对云,火焰,水,以及其他许多效果都有用. Perlin噪声的创造者Ken Perlin创建了Simplex噪声,以提高性能和质量,而不是原声.

默认情况下,噪声模式是周期性的:它重复。您可以在 X 和 Y 中滚动。您也可以改变 `noiseFlow` 值,以沿周期性进程演化模式。

您可以设置单元格数、 颜色和图案的透明度。 您可以用 `noiseIterations` 添加细细的细节。 您可以用 `noiseWarpAmount` 添加动荡 。

可以用`noiseSeed`来改变基本模式,不同的种子会产生完全不同的模式.

您可以设置 `noiseNormalMap` 输出普通地图。 这是添加照明纹理的快速方式 。

对于高级用户,您可以配置八进制迭代的特性。使用 `noiseDetailPower`, `noiseFlowPower`,和 `noiseContributionPower` 以调整这些值的指数缩放率。 `noiseWarpDetailPower`, `noiseWarpFlowPower`,和 `noiseWarpContributionPower` 用于曲速效应。

**构造函数**

`new NoiseSimplex2D(scene, [config], [x], [y], [width], [height])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属景点 。 |
| config | [Phaser.Types.GameObjects.NoiseSimplex2D.NoiseSimplex2DQuadConfig](/api/typedef/types-gameobjects-noisesimplex2d#noisesimplex2dquadconfig) | 是 |  | 此游戏对象的配置 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Shader](/api/class/gameobjects-shader)  



> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L12)  
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

### noiseCells {#noiseCells}

#### noiseCells: Array.\<number> {#noisecells-arraynumber}


**说明:**

每个维度的单元格数。

这一定是两个数字的数组。

尝试将细胞数保持在纹理分辨率的2到约8分之一之间。细胞数大于纹理分辨率,本质上是昂贵的白色噪音。


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L97)  
引入版本：4.0.0


---

### noiseColorEnd {#noiseColorEnd}

#### noiseColorEnd: [Phaser.Display.Color](/api/namespace/display-color) {#noisecolorend-phaserdisplaycolor}


**说明:**

调整后的噪声值为1. 此颜色与 noiseColorStart 混合 。

默认是白色的。 您可以设置任何颜色, 并更改 α 。


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L395](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L395)  
引入版本：4.0.0


---

### noiseColorStart {#noiseColorStart}

#### noiseColorStart: [Phaser.Display.Color](/api/namespace/display-color) {#noisecolorstart-phaserdisplaycolor}


**说明:**

调整噪声值为 0 时的颜色。 此颜色与 noiseColorEnd 混合 。

默认是黑色的。 您可以设置任何颜色, 并更改 α 。


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L383](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L383)  
引入版本：4.0.0


---

### noiseContributionPower {#noiseContributionPower}

#### noiseContributionPower: number {#noisecontributionpower-number}


**说明:**

从接下来的八进制噪声中 取多少价值?

以此为引号的底部。 默认 2 将贡献减半, 数值降低速度, 优先处理高频细节。 值降低速度, 优先解决低频细节 。


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L249](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L249)  
引入版本：4.0.0


---

### noiseDetailPower {#noiseDetailPower}

#### noiseDetailPower: number {#noisedetailpower-number}


**说明:**

增加八分位噪音之间的详细频率需要多少。

以此为参数的基数。 默认值 2 将频率每八进制时翻倍。 数值的比值要慢, 值的比值要高 。


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L219](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L219)  
引入版本：4.0.0


---

### noiseFlow {#noiseFlow}

#### noiseFlow: number {#noiseflow-number}


**说明:**

噪音字段的当前流。 模式随流而变化。 这是旋转, 因此在流增后, 模式会恢复到原来的状态 。 @ 2.

使用流来随着时间推移而演化模式,并有周期性的重复.


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L157](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L157)  
引入版本：4.0.0


---

### noiseFlowPower {#noiseFlowPower}

#### noiseFlowPower: number {#noiseflowpower-number}


**说明:**

噪音八进制之间 增加流量多少

此值用作一个引号的基数。 默认 2 将流量进化率每八进制翻倍。 数值降低速度, 数值提高 。


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L234](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L234)  
引入版本：4.0.0


---

### noiseIterations {#noiseIterations}

#### noiseIterations: number {#noiseiterations-number}


**说明:**

需要应用多少八分之八的噪音,这增加了噪音的详细细节,以性能为代价。

此值应该是 1 或 更高 的整数。 5 或 5 以上的值效果越来越小。 每个迭代都有成本, 所以只使用您需要的 !

使用`noiseDetailPower`,`noiseFlowPower`和`noiseContributionPower`来配置八维之间的差.


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L186](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L186)  
引入版本：4.0.0


---

### noiseNormalMap {#noiseNormalMap}

#### noiseNormalMap: boolean {#noisenormalmap-boolean}


**说明:**

是否将噪声输出转换为普通映射 。

以`noiseNormalScale`控制曲率强度.


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L312](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L312)  
引入版本：4.0.0


---

### noiseNormalScale {#noiseNormalScale}

#### noiseNormalScale: number {#noisenormalscale-number}


**说明:**

普通地图输出的曲线强度。 当启用 `noiseNormalMap` 时使用此功能 。

默认值为 1. 较高的值产生更多的曲率;较低的值为夸张值.

表面角度由噪声变化速度决定.


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L324](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L324)  
引入版本：4.0.0


---

### noiseOffset {#noiseOffset}

#### noiseOffset: Array.\<number> {#noiseoffset-arraynumber}


**说明:**

每个维度的噪声的偏移:[x,y]. 动画x和y来滚动噪声模式.

这一定是两个数字的数组。


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L135)  
引入版本：4.0.0


---

### noisePeriod {#noisePeriod}

#### noisePeriod: Array.\<number> {#noiseperiod-arraynumber}


**说明:**

图案包接前的单元格数 。

这一定是两个数字的数组。

默认情况下,这与`noiseCells`相同.


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L114)  
引入版本：4.0.0


---

### noiseSeed {#noiseSeed}

#### noiseSeed: Array.\<number> {#noiseseed-arraynumber}


**说明:**

声闻种子.

这抵消了简单的网格, 导致其散列评价不同。 种子的任何变化都会导致新的模式。 它必须是2个数字的数组 。

使用自定义种子来创建不同的,但可复制的,随机的.


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L412](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L412)  
引入版本：4.0.0


---

### noiseValueAdd {#noiseValueAdd}

#### noiseValueAdd: number {#noisevalueadd-number}


**说明:**

原噪声输出增加值.

原始噪音的排放量在-1至1. 之间,调整如下:rawNoise * noiseValueFactor + noiseValueAdd) ^ noiseValuePower.


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L357](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L357)  
引入版本：4.0.0


---

### noiseValueFactor {#noiseValueFactor}

#### noiseValueFactor: number {#noisevaluefactor-number}


**说明:**

原始噪音输出适用的因素。

原始噪音的排放量在-1至1. 之间,调整如下:rawNoise * noiseValueFactor + noiseValueAdd) ^ noiseValuePower.


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L344](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L344)  
引入版本：4.0.0


---

### noiseValuePower {#noiseValuePower}

#### noiseValuePower: number {#noisevaluepower-number}


**说明:**

标注应用于原始噪声输出.

原始噪音的排放量在-1至1. 之间,调整如下:rawNoise * noiseValueFactor + noiseValueAdd) ^ noiseValuePower.


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L370](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L370)  
引入版本：4.0.0


---

### noiseWarpAmount {#noiseWarpAmount}

#### noiseWarpAmount: number {#noisewarpamount-number}


**说明:**

将噪声纹理曲折多少 。 曲折可以给输出增加一种动荡感 。

这流出数个八进制的噪音来产生随机曲折。 它增加了着色器的成本 。


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L172](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L172)  
引入版本：4.0.0


---

### noiseWarpContributionPower {#noiseWarpContributionPower}

#### noiseWarpContributionPower: number {#noisewarpcontributionpower-number}


**说明:**

从曲面中后续的八进制噪声中可以得出多少值.

以此为引号的底部。 默认 2 将贡献减半, 数值降低速度, 优先处理高频细节。 值降低速度, 优先解决低频细节 。


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L296](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L296)  
引入版本：4.0.0


---

### noiseWarpDetailPower {#noiseWarpDetailPower}

#### noiseWarpDetailPower: number {#noisewarpdetailpower-number}


**说明:**

曲面中八分位噪声之间 增加详细频率的多少?

以此为参数的基数。 默认值 2 将频率每八进制时翻倍。 数值的比值要慢, 值的比值要高 。


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L264](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L264)  
引入版本：4.0.0


---

### noiseWarpFlowPower {#noiseWarpFlowPower}

#### noiseWarpFlowPower: number {#noisewarpflowpower-number}


**说明:**

曲面上八进制噪音之间的流量增加多少

此值用作一个引号的基数。 默认 2 将流量进化率每八进制翻倍。 数值降低速度, 数值提高 。


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L280](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L280)  
引入版本：4.0.0


---

### noiseWarpIterations {#noiseWarpIterations}

#### noiseWarpIterations: number {#noisewarpiterations-number}


**说明:**

敲响噪音时要应用多少八分之的噪音.

这行为与 `noiseIterations` 很像, 但用于曲速计算。 它只在 `noiseWarpAmount` 并非 0 时使用。 您可能需要比普通的曲速重迭更少 。


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L204](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L204)  
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


**返回值:** [Phaser.GameObjects.NoiseSimplex2D](/api/class/gameobjects-noisesimplex2d) - 此游戏对象.


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L496](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L496)  
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
| start | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0x000000" | 噪声值为0时的颜色,对应`noiseColorStart`. |
| end | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0xffffff" | 噪声值为1时的颜色,对应`noiseColorEnd`. |


**返回值:** [Phaser.GameObjects.NoiseSimplex2D](/api/class/gameobjects-noisesimplex2d) - 此游戏对象.


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L430](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L430)  
引入版本：4.0.0


---

### wrapNoise {#wrapNoise}

#### \<instance> wrapNoise() {#instance-wrapnoise}


**说明:**

设置噪声纹理以无缝包裹.

将`noisePeriod`设定为所有维度的等效`noiseCells`.


**返回值:** [Phaser.GameObjects.NoiseSimplex2D](/api/class/gameobjects-noisesimplex2d) - 此游戏对象.


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L513](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2D.js#L513)  
引入版本：4.0.0


---

---
