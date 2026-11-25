# Noise {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-noise)

一个噪音游戏对象 。

此游戏对象是一个四重奏, 显示随机噪声。 您可以像其它任何一对一样操纵此对象, 使其具有交互性, 并用在过滤器和面具中, 以产生视觉惊人的效果 。

幕后,一个噪声是使用特定遮蔽程序的一种[Phaser.GameObjects.Shader](/api/class/gameobjects-shader).

噪音或“ 白色噪音” 仅仅是随机值。 这些是用散列向向量坐标来创建的, 因此在同一位置总是产生相同的噪音。 这会产生可复制的效果 。

你可以设定噪音的颜色和透明度.

您可以通过动画`noiseOffset`属性滚动噪音。 请注意, 浮点精度对这个效果非常重要 。 滚动非常大距离可能导致输出的阻塞性。 滚动非常小的距离可能导致输出完全改变, 因为输出处理的准确值并不相同 。 如果您滚动对象的精确分数, 输出将基本保持不变, 但不能保证稳定 。 使用`setRenderToTexture` 并将其作为TileSprite 的纹理会更有效 。

您可以设定 `noisePower` 来雕刻输出级别。 更高的功率会降低更高的值。 较低的功率会降低较低的值 。

**构造函数**

`new Noise(scene, [config], [x], [y], [width], [height])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属景点 。 |
| config | [Phaser.Types.GameObjects.Noise.NoiseQuadConfig](/api/typedef/types-gameobjects-noise#noisequadconfig) | 是 |  | 此游戏对象的配置 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Shader](/api/class/gameobjects-shader)  



> 源码：[src/gameobjects/noise/Noise.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/Noise.js#L12)  
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

### noiseColorEnd {#noiseColorEnd}

#### noiseColorEnd: [Phaser.Display.Color](/api/namespace/display-color) {#noisecolorend-phaserdisplaycolor}


**说明:**

映射到高噪值的颜色(接近1).

默认是白色的。 您可以设置任何颜色, 并更改 α 。


> 源码：[src/gameobjects/noise/Noise.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/Noise.js#L114)  
引入版本：4.0.0


---

### noiseColorStart {#noiseColorStart}

#### noiseColorStart: [Phaser.Display.Color](/api/namespace/display-color) {#noisecolorstart-phaserdisplaycolor}


**说明:**

映射到低噪值的颜色(接近0).

默认是黑色的。 您可以设置任何颜色, 并更改 α 。


> 源码：[src/gameobjects/noise/Noise.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/Noise.js#L103)  
引入版本：4.0.0


---

### noiseOffset {#noiseOffset}

#### noiseOffset: Array.\<number> {#noiseoffset-arraynumber}


**说明:**

每个维度的噪声的偏移:[x,y]. 动画x和y来滚动噪声模式.

这一定是两个数字的数组。


> 源码：[src/gameobjects/noise/Noise.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/Noise.js#L75)  
引入版本：4.0.0


---

### noisePower {#noisePower}

#### noisePower: number {#noisepower-number}


**说明:**

用于噪声值的力量。 它可以增强/ 压制高/ 低噪声 。


> 源码：[src/gameobjects/noise/Noise.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/Noise.js#L92)  
引入版本：4.0.0


---

### noiseRandomChannels {#noiseRandomChannels}

#### noiseRandomChannels: boolean {#noiserandomchannels-boolean}


**说明:**

是否将信道噪声分开, 创建许多输出颜色 。


> 源码：[src/gameobjects/noise/Noise.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/Noise.js#L130)  
引入版本：4.0.0


---

### noiseRandomNormal {#noiseRandomNormal}

#### noiseRandomNormal: boolean {#noiserandomnormal-boolean}


**说明:**

是否使每个像素的任意正常值成像。 正常值位于相机正面的半球 。

此值将覆盖 `noiseRandomChannels` 。


> 源码：[src/gameobjects/noise/Noise.js#L141](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/Noise.js#L141)  
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
| start | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0x000000" | 映射到低噪值的颜色(接近0). |
| end | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0xffffff" | 映射到高噪值的颜色(接近1). |


**返回值:** [Phaser.GameObjects.Noise](/api/class/gameobjects-noise) - 此游戏对象.


> 源码：[src/gameobjects/noise/Noise.js#L155](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/Noise.js#L155)  
引入版本：4.0.0


---

---
