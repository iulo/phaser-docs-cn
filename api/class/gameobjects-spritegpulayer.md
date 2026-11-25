# SpriteGPULayer {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-spritegpulayer)

SpriteGPULayer Game Object。 这是只使用 WebGL Game Objects。 它被优化为在简单的曲折动画之后渲染大量四角。 它适合动画的复杂背景 。

SpriteGPULayer是一个包含成员对象集合的复合对象。它将这些对象的渲染数据存储在GPU缓冲器中,并使它们成为单一的绘图调用。因为它只在必要时更新GPU缓冲,比单个对象渲染速度要快100倍。避免频繁更改SpriteGPUlayer的内容,因为这需要更新整个缓冲器 。

层一般可以用百万个小四角来表现, 精确的性能取决于设备以及四角的大小。 如果四角是大的, 层将受填充率的限制。 避免每个框架绘制超过几百万像素 。

当充电 SpriteGPULayer 时, 请使用 `addMember` 在层的顶部添加一个新的成员。 您应该一次充电层, 并且不改变它, 而不是经常添加和删除成员, 因为更新缓冲器的费用很高 。

与其为每次`addMember`呼叫创建新的`SpriteGPULayer.Member`对象,不如重新使用同一对象。这样做效率更高,因为创建数百万对象具有重大性能成本,并可能导致垃圾收集问题。

关于修改 SpriteGPULayer 的注释 :

下列操作费用昂贵,需要更新部分或全部缓冲器:

- `addData`

- `addMember`

- `editMember`

- `patchMember`

- `resize`

- `removeMembers`

成员在缓冲器的末尾会添加。 被删除的成员会被从缓冲器中分解出来, 从而更新整个缓冲器。 如果您删除一个较早的成员, 后成员索引将会改变。 如果您需要维持一个结构, 如砖块网格, 最好通过设置一个成员 scaleX, scaleY, 和 alpha 到 0 来“ 移走” 。 它仍然被渲染, 但不会填充任何像素 。

修改缓冲器的一小段费用较低。 缓冲器被分成若干段, 每个段可以独立更新。 编辑和补丁成员只会更新包含正在编辑的成员的段。 更新发生在时间上, 所以所有编辑都同时进行。 这可以减少需要更新的数据数量, 但是比不更新缓冲器要贵。 如果您正在更新大量段, 可能更有效率的是一次性调用 `setAllSegmentsNeedUpdate` 并更新整个缓冲器, 而不是连续进行多个段更新 。

初始成员数据中的动画用于编译遮阳器和`frameDataTexture`。如果在初始编译后添加新的动画,则遮阳器和纹理会重建,费用昂贵.

纹理说明:

此层从不灵活中获取了它的许多速度。 它只能使用一个纹理, 而纹理必须是单一的图像。 它不能使用多图集纹理 。

此外,如果纹理不是两块大小的功率,那么如果精确排列成图案,则可能会出现一些纹理的缝合。这是因为GPU精度受到二进制逻辑的限制,纹理坐标只能完全准确地表达两个纹理的功率。这可以通过在纹理中在每个框上添加/冲刷一个像素的粘贴,或者使用两个纹理的功力来避免。

你该用哪一种?

- 如果您使用像素艺术模式或圆像素,

  您应该使用两个纹理的功率。

- 如果你使用平滑模式,你可以使用两个纹理的非电源,

  但你应该在每个框上加贴板 以避免缝合

- 如果您使用单个图像, 或者没有纹理中的框

  需要瓦片,没关系。

**构造函数**

`new SpriteGPULayer(scene, texture, size)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 这支SpriteGPULayer所属的场景. |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 用于渲染 SpriteGPULayer 的纹理。 这必须来自一个图像; 多图集将无法工作 。 |
| size | number | 否 | 此 SpriteGPULayer 将持有的最大二次数。 必要时, 可在稍后增加 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.ElapseTimer](/api/namespace/gameobjects-components-elapsetimer)  
> [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting)  
> [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask)  
> [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes)  
> [Phaser.GameObjects.Components.TextureCrop](/api/namespace/gameobjects-components-texturecrop)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L18)  
引入版本：4.0.0

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





**From [Phaser.GameObjects.Components.ElapseTimer](/api/namespace/gameobjects-components-elapsetimer):**


 - [timeElapsed](/api/namespace/gameobjects-components-elapsetimer#timeElapsed)
 - [timeElapsedResetPeriod](/api/namespace/gameobjects-components-elapsetimer#timeElapsedResetPeriod)
 - [timePaused](/api/namespace/gameobjects-components-elapsetimer#timePaused)





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





**From [Phaser.GameObjects.Components.TextureCrop](/api/namespace/gameobjects-components-texturecrop):**


 - [frame](/api/namespace/gameobjects-components-texturecrop#frame)
 - [isCropped](/api/namespace/gameobjects-components-texturecrop#isCropped)
 - [texture](/api/namespace/gameobjects-components-texturecrop#texture)





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

### animationData {#animationData}

#### animationData: Array.\<object> {#animationdata-arrayobject}


**说明:**

框架数据纹理中订购的动画列表.


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L330](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L330)  
引入版本：4.0.0


---

### animationDataIndices {#animationDataIndices}

#### animationDataIndices: object {#animationdataindices-object}


**说明:**

框架索引图用于框架数据纹理中的动画参数。这些是顶点着色器使用的起始帧索引,可用于将名称映射回`animationDataIndices`。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L351](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L351)  
引入版本：4.0.0


---

### animationDataNames {#animationDataNames}

#### animationDataNames: object {#animationdatanames-object}


**说明:**

框架数据纹理中动画名称的映射到动画参数。此图用于将动画名称转换为顶点阴影的索引和持续时间 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L339](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L339)  
引入版本：4.0.0


---

### bufferUpdateSegments {#bufferUpdateSegments}

#### bufferUpdateSegments: number {#bufferupdatesegments-number}


**说明:**

缓冲器的哪个部分需要更新。 这是一个比特字段, 其部分等于 `_segments` 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L201](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L201)  
引入版本：4.0.0


---

### bufferUpdateSegmentSize {#bufferUpdateSegmentSize}

#### bufferUpdateSegmentSize: number {#bufferupdatesegmentsize-number}


**说明:**

需要更新的缓冲器的每个部分的大小 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L211](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L211)  
引入版本：4.0.0


---

### EASE {#EASE}

#### EASE: object {#ease-object}


**说明:**

用于有效松动函数的字符串, 用于 SpriteGPULayer Member Animation 的 `ease` 属性。 这是 `this.EASE_CODES` 的反向映射 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L258](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L258)  
引入版本：4.0.0


---

### EASE_CODES {#EASE_CODES}

#### EASE_CODES: object {#ease_codes-object}


**说明:**

用于有效松动函数的代码, 可用于 SpriteGPULayer Member Animation 的 `ease` 属性。 这是 `this.EASE` 的反向映射 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L270](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L270)  
引入版本：4.0.0


---

### frameDataIndices {#frameDataIndices}

#### frameDataIndices: object {#framedataindices-object}


**说明:**

框架名称映射到框架数据纹理中的索引。用于将框架名称转换为顶点阴影的索引。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L310](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L310)  
引入版本：4.0.0


---

### frameDataIndicesInv {#frameDataIndicesInv}

#### frameDataIndicesInv: object {#framedataindicesinv-object}


**说明:**

框架数据纹理中用于框架索引的索引图。用于将框架索引转换为名称以进行调试。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L320](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L320)  
引入版本：4.0.0


---

### frameDataTexture {#frameDataTexture}

#### frameDataTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#framedatatexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

包含 SpriteGPULayer 框架数据的纹理。 顶点着色器使用此纹理 。

纹理由像素的跨度组成,其中每个步程被解释为6个16位无符号的整数,代表一个框的x,y,宽度,高度,以及来源x和y. 纹理将高达4096像素宽度,并视需要达到高.

纹理中有两组数据:帧和动画. 帧取自`texture`. 动画通过调用`setAnimations`来定义, 由适合遮荫动画的帧构成的运行. 虽然纹理会由`setAnimations`重新生成,但帧是先存储的,所以它们的指数不会改变.

如果你改变这个层的`texture`,你需要通过调用`generateFrameDataTexture`来重生这个.


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L285](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L285)  
引入版本：4.0.0


---

### gravity {#gravity}

#### gravity: number {#gravity-number}


**说明:**

成员动画在“ 重力” 模式中使用的重力。 这是以像素每秒平方位加速, 默认为每秒1024像素 。

任何动画都可以设定为`ease: 'Gravity'`来使用这个值. 动画不使用`amplitude`,而是使用`velocity`(若干像素)和`gravityFactor`(1至1)参数. 注意,一个为0的`gravityFactor`被假定为错误,并将转换为1.


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L220](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L220)  
引入版本：4.0.0


---

### MAX_BUFFER_UPDATE_SEGMENTS_FULL {#MAX_BUFFER_UPDATE_SEGMENTS_FULL}

#### MAX_BUFFER_UPDATE_SEGMENTS_FULL: number {#max_buffer_update_segments_full-number}


**说明:**

满时的`bufferUpdateSegments`状态,这是一个恒定值,不应更改,如果改变,所有的地狱都会松动.


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L188](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L188)  
引入版本：4.0.0


---

### memberCount {#memberCount}

#### memberCount: number {#membercount-number}


**说明:**

斯普里蒂格普莱尔的四位成员数.


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L145)  
引入版本：4.0.0


---

### nextMember {#nextMember}

#### nextMember: ArrayBuffer {#nextmember-arraybuffer}


**说明:**

下一个成员缓冲器,用于存储成员数据,然后将其添加到GPU缓冲器中.


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L385](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L385)  
引入版本：4.0.0


---

### nextMemberF32 {#nextMemberF32}

#### nextMemberF32: Float32Array {#nextmemberf32-float32array}


**说明:**

下一个成员缓冲器的浮图32箭头视图 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L395](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L395)  
引入版本：4.0.0


---

### nextMemberU32 {#nextMemberU32}

#### nextMemberU32: Uint32Array {#nextmemberu32-uint32array}


**说明:**

下一个成员缓冲器的 Uint32Array 视图。 用于将32 位整数数据写入缓冲器, 用于颜色数据 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L404](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L404)  
引入版本：4.0.0


---

### size {#size}

#### size: number {#size-number}


**说明:**

最多可以进入 SpriteGPULayer 的四位成员数。 此值只读。 使用 `resize` 更改缓冲大小 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L154)  
引入版本：4.0.0


---

### submitterNode {#submitterNode}

#### submitterNode: [Phaser.Renderer.WebGL.RenderNodes.SubmitterSpriteGPULayer](/api/class/renderer-webgl-rendernodes-submitterspritegpulayer) {#submitternode-phaserrendererwebglrendernodessubmitterspritegpulayer}


**说明:**

此 SpriteGPULayer 的提交器 RenderNode 。

此手柄将 SpriteGPULayer 渲染为 GPU 。 当 SpriteGPuLayer 初始化时, 它会自动创建。 多数 RenderNodes 是存储在 RenderNode Manager 的单调, 但是由于这个单调手柄持有非常具体的数据, 它会存储在 SpriteGPouLayer 本身 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L365](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L365)  
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





**From [Phaser.GameObjects.Components.ElapseTimer](/api/namespace/gameobjects-components-elapsetimer):**


 - [resetTimer](/api/namespace/gameobjects-components-elapsetimer#resetTimer)
 - [setTimerPaused](/api/namespace/gameobjects-components-elapsetimer#setTimerPaused)
 - [setTimerResetPeriod](/api/namespace/gameobjects-components-elapsetimer#setTimerResetPeriod)
 - [updateTimer](/api/namespace/gameobjects-components-elapsetimer#updateTimer)





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





**From [Phaser.GameObjects.Components.TextureCrop](/api/namespace/gameobjects-components-texturecrop):**


 - [setCrop](/api/namespace/gameobjects-components-texturecrop#setCrop)
 - [setFrame](/api/namespace/gameobjects-components-texturecrop#setFrame)
 - [setTexture](/api/namespace/gameobjects-components-texturecrop#setTexture)





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

### addData {#addData}

#### \<instance> addData(member) {#instance-adddatamember}


**说明:**

将数据添加到 SpriteGPULayer 缓冲器中。它被插入到缓冲器的末尾。

这主要被SpriteGPULayer内部使用,它以原始数据为缓冲器,非常高效,但`addMember`更容易使用.

注意,如果用动画添加一个成员,动画必须已经启用,或者必须使用`setAnimationEnabled`,例如`layer.setAnimationEnabled('Linear', true)`或`layer.setAnimationEnabled(layer.EASE_CODES[layer.EASE.Linear], true)`来启用.

这是一种缓冲器的修改,而且很昂贵。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| member | Float32Array | 否 | 用于添加缓冲器的原始数据. |


**返回值:** [Phaser.GameObjects.SpriteGPULayer](/api/class/gameobjects-spritegpulayer) - 此 SpriteGPULayer 物件 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L743](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L743)  
引入版本：4.0.0


---

### addedToScene {#addedToScene}

#### \<instance> addedToScene() {#instance-addedtoscene}


**说明:**

当此 SpriteGPULayer 添加到场景时调用。 将它与场景的更新列表一起注册, 以便它接收 `preUpdate` 调用每个帧 。


**Overrides:** Phaser.GameObjects.GameObject#addedToScene


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L416](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L416)  
引入版本：4.0.0


---

### addMember {#addMember}

#### \<instance> addMember([member]) {#instance-addmembermember}


**说明:**

将成员添加到 SpriteGPULayer 中。 这是将成员添加到 SpriteGPULayer 中最简单的方式 。

这是一种缓冲器的修改,而且很昂贵。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| member | Partial.\<[Phaser.Types.GameObjects.SpriteGPULayer.Member](/api/typedef/types-gameobjects-spritegpulayer#member)> | 是 | 加入SpriteGPULayer的成员. |


**返回值:** [Phaser.GameObjects.SpriteGPULayer](/api/class/gameobjects-spritegpulayer) - 此 SpriteGPULayer 物件 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L783](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L783)  
引入版本：4.0.0


---

### clearAllSegmentsNeedUpdate {#clearAllSegmentsNeedUpdate}

#### \<instance> clearAllSegmentsNeedUpdate() {#instance-clearallsegmentsneedupdate}


**说明:**

清除缓冲器中需要更新的所有部分。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L732](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L732)  
引入版本：4.0.0


---

### editMember {#editMember}

#### \<instance> editMember(index, member) {#instance-editmemberindex-member}


**说明:**

编辑 SpriteGPULayer 成员。 这将更新成员在 GPU 缓冲器中的数据。 只有包含目标成员的缓冲段会被标记为更新, 这使得此程序比完整的缓冲更新费用更低 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 成员索引待编辑. |
| member | Partial.\<[Phaser.Types.GameObjects.SpriteGPULayer.Member](/api/typedef/types-gameobjects-spritegpulayer#member)> | 否 | 新成员数据. |


**返回值:** [Phaser.GameObjects.SpriteGPULayer](/api/class/gameobjects-spritegpulayer) - 此 SpriteGPULayer 物件 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L964](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L964)  
引入版本：4.0.0


---

### generateFrameDataTexture {#generateFrameDataTexture}

#### \<instance> generateFrameDataTexture() {#instance-generateframedatatexture}


**说明:**

为 SpriteGPULayer 生成 `frameDataTexture`。 顶点着色器使用此方法访问框架数据 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L556](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L556)  
引入版本：4.0.0


---

### getDataByteSize {#getDataByteSize}

#### \<instance> getDataByteSize() {#instance-getdatabytesize}


**说明:**

获取定义成员所用的字节数。 如果您正在直接编辑缓冲, 您需要这个值作为“ 跳跃” 才能移动缓冲 。


**返回值:** number - 每一个成员所用的字节数 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L454](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L454)  
引入版本：4.0.0


---

### getMember {#getMember}

#### \<instance> getMember(index) {#instance-getmemberindex}


**说明:**

返回 SpriteGPULayer 成员。

返回从缓冲器复制的对象。 编辑后不会改变 SpriteGPULayer 中的任何内容。 对象在功能上与创建缓冲器所用的数据完全相同, 但有些值可能不同 。

- 支持动画,但没有振幅或持续时间或放松了“无” (0) 的属性将作为数字显示。

- 动画缓和值将以数字(数值)表示

  输入 `this.EASE`).

- 动画延迟值将常态化到持续时间,

  例如,拖延150年,期限为100年,将返回50年。

- 由于浮点精度,一些四舍五入可能发生.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 成员索引来得到. |


**返回值:** [Phaser.Types.GameObjects.SpriteGPULayer.Member](/api/typedef/types-gameobjects-spritegpulayer#member) - 成员数据,如果索引超出范围则无效。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L1046](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L1046)  
引入版本：4.0.0


---

### getMemberData {#getMemberData}

#### \<instance> getMemberData(index, [out]) {#instance-getmemberdataindex-out}


**说明:**

返回 SpriteGPULayer 成员的原始数据。 这可以作为高效编辑操作的基础, 包括给 `addData` 和 `patchMember` 的呼叫, 因此不需要转换数据 。

返回从缓冲器复制的 Uint32 箭头。 编辑后不会改变 SpriteGPULayer 中的任何内容。 阵列将功能上与创建缓冲器所用的数据相同 。

默认情况下,数据会被复制到 `this.nextMember`。 您可以使用视图 `this.nextMemberF32` 和 `this.nextMemberU32` 来访问不同格式的数据。 如果您提供了 `out` 参数, 数据将被复制到该数组中, 您必须构建自己的视图 。

原始数据视图是32位浮点数的42个元素阵列。一些值被组合成动画,形式是:

- 0: 基准值

- 1: amplitude

- 2:持续时间(如果否定,动画会Yoyo).

- 3:延迟(整数部分为放松,小数部分为延迟除以2 * 持续时间;如果是负数,动画不会循环) :

因此,总体结构是:

- 0-3: x(动画)

- 4-7:y(动画)

- 8-11:旋转(动画)

- 12-15: scaleX(动画)

- 16-19: scaleY(动画)

- 20-23:α(动画)

- 24-27:帧指数(动画).

- 28-31: tintBlend(动画)

- 32-35:无数据

- 36: originX

- 37: originY

- 38: tintMode

- 39: creationTime

- 40: scrollFactorX

- 41: scrollFactorY

元素 32-35 只可见于 Uint32Array 视图中。 它们存储了 锡的四角的 32 位 RGBA 值 :

- 32: bottom-left

- 33: top-left

- 34: bottom-right

- 35: top-right

如果动画的易用性是"重力",振幅则被替换为二部分值:整数部分是 `velocity`,分数部分是重映射 `gravityFactor`来得到真实的 `gravityFactor`, 使用 `gravityFactor * 2 - 1` 以映射 [0] 到 [1] 。一个输出 `gravityFactor` 0实际意味着1。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 成员索引来得到. |
| out | Uint32Array | 是 | 复制数据到的可选数组。 如果不提供, `this.nextMember` 将被覆盖, `nextMemberU32` 将被返回 。 |


**返回值:** Uint32Array - 成员数据,如果索引超出范围则无效。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L1154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L1154)  
引入版本：4.0.0


---

### getShaderFeatures {#getShaderFeatures}

#### \<instance> getShaderFeatures() {#instance-getshaderfeatures}


**说明:**

返回用于阴影程序特性的列表。 阴影程序编译时使用此列表 。


**返回值:** Array.\<string> - 一组特性,可以在阴影程序中启用。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L468](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L468)  
引入版本：4.0.0


---

### insertMembers {#insertMembers}

#### \<instance> insertMembers(index, members) {#instance-insertmembersindex-members}


**说明:**

将成员插入 SpriteGPULayer 。 这将更新 GPU 缓冲。 这是一个昂贵的操作,因为它需要在整个缓冲器插入点后更新 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 插入成员索引。 |
| members | [Phaser.Types.GameObjects.SpriteGPULayer.Member](/api/typedef/types-gameobjects-spritegpulayer#member) \| Array.\<[Phaser.Types.GameObjects.SpriteGPULayer.Member](/api/typedef/types-gameobjects-spritegpulayer#member)> | 否 | 成员要插入。 |


**返回值:** [Phaser.GameObjects.SpriteGPULayer](/api/class/gameobjects-spritegpulayer) - 此 SpriteGPULayer 物件 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L1289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L1289)  
引入版本：4.0.0


---

### insertMembersData {#insertMembersData}

#### \<instance> insertMembersData(index, data) {#instance-insertmembersdataindex-data}


**说明:**

将原始数据插入 SpriteGPULayer 。 这将更新 GPU 缓冲器。 这是一个昂贵的操作, 因为它需要整个缓冲器在插入点后更新 。

数据必须作为 Uint32 箭头传输。 这将保存其它类型箭头不会传输的数据。 由于它使用一个基础的箭头缓冲器, 您可以在提交数据前使用任何类型箭头视图来研究数据 。

缓冲器可以包含1个或更多成员。确保缓冲器是成员数的正确大小。数据结构请参见 `getMemberData` 。

注意,如果用动画添加一个成员,动画必须已经启用,或者必须使用`setAnimationEnabled`,例如`layer.setAnimationEnabled('Linear', true)`或`layer.setAnimationEnabled(layer.EASE_CODES[layer.EASE.Linear], true)`来启用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 插入成员索引。 |
| data | Uint32Array | 否 | 成员要插入。 |


**返回值:** [Phaser.GameObjects.SpriteGPULayer](/api/class/gameobjects-spritegpulayer) - 此 SpriteGPULayer 物件 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L1350](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L1350)  
引入版本：4.0.0


---

### patchMember {#patchMember}

#### \<instance> patchMember(index, member, [mask]) {#instance-patchmemberindex-member-mask}


**说明:**

用原始数据更新 SpriteGPULayer 成员。 这将更新成员在 GPU 缓冲器中的数据。 只有包含目标成员的缓冲部分会被标记用于更新, 这使得此费用低于完整的缓冲更新 。

您可以提供一个掩码来控制哪些属性被更新。 它可以用于仅更新一个属性子集。 尝试使用 `getMemberData` 复制一个现有成员的数据, 然后修改您想要更改的数据 。

数据必须作为 Uint32 箭头传输。 这将保存其它类型箭头不会传输的数据。 由于它使用一个基础的箭头缓冲器, 您可以在提交数据前先使用任何类型箭头视图来研究数据 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 成员补丁的索引 。 |
| member | Uint32Array | 否 | 新成员数据. |
| mask | Array.\<number> | 是 | 用于成员数据的掩码。1值将更新成员数据,0值将保留现有成员数据。 |


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L991](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L991)  
引入版本：4.0.0


---

### preDestroy {#preDestroy}

#### \<instance> preDestroy() {#instance-predestroy}


**说明:**

内部破坏处理器,作为破坏过程的一部分而叫作.


**Access:** 保护


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L1632](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L1632)  
引入版本：4.0.0


---

### preUpdate {#preUpdate}

#### \<instance> preUpdate(time, delta) {#instance-preupdatetime-delta}


**说明:**

此 SpriteGPULayer 的更新步骤, 由 Scene 调用每个框架 。 提前推进成员动画所用的内部已过期的定时器 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间戳,由请求动画框架或SetTimeout生成. |
| delta | number | 否 | 三角洲时间,以毫秒计,自上个框架结束。 |


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L440](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L440)  
引入版本：4.0.0


---

### removedFromScene {#removedFromScene}

#### \<instance> removedFromScene() {#instance-removedfromscene}


**说明:**

当这个 SpriteGPULayer 从场景中移除时调用。 从场景的更新列表中调用它, 因此它不再收到 `preUpdate` 的呼叫 。


**Overrides:** Phaser.GameObjects.GameObject#removedFromScene


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L428](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L428)  
引入版本：4.0.0


---

### removeMembers {#removeMembers}

#### \<instance> removeMembers(index, [count]) {#instance-removemembersindex-count}


**说明:**

从 SpriteGPULayer 中删除一个成员或若干成员。 这将更新 GPU 缓冲器。 这是一个昂贵的操作, 因为需要更新整个缓冲器 。

缓冲器没有调整大小 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| index | number | 否 |  | 要删除的成员索引 。 |
| count | number | 是 | 1 | 要删除的成员数,默认为 1. |


**返回值:** [Phaser.GameObjects.SpriteGPULayer](/api/class/gameobjects-spritegpulayer) - 此 SpriteGPULayer 物件 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L1242](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L1242)  
引入版本：4.0.0


---

### resize {#resize}

#### \<instance> resize(count, [clear]) {#instance-resizecount-clear}


**说明:**

将 SpriteGPULayer 缓冲器大小调整为新大小。可选的,可以清除缓冲器。

这是一项昂贵的操作,因为它需要更新整个缓冲器,需要许多帧才能完成.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| count | number | 否 |  | 斯普里特GPULayer中的新成员数. |
| clear | boolean | 是 | false | 是否清除缓冲器 。 |


**返回值:** [Phaser.GameObjects.SpriteGPULayer](/api/class/gameobjects-spritegpulayer) - 此 SpriteGPULayer 物件 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L658](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L658)  
引入版本：4.0.0


---

### setAllSegmentsNeedUpdate {#setAllSegmentsNeedUpdate}

#### \<instance> setAllSegmentsNeedUpdate() {#instance-setallsegmentsneedupdate}


**说明:**

设置缓冲器的所有部分以要求更新。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L721](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L721)  
引入版本：4.0.0


---

### setAnimationEnabled {#setAnimationEnabled}

#### \<instance> setAnimationEnabled(name, enabled) {#instance-setanimationenabledname-enabled}


**说明:**

设定动画的启用状态。 这将启用或禁用阴影程序中的动画。 动画加到 `addMember` 时会自动调用这种方法, 所以您不需要手动调用它 。

每部被启用的动画在阴影程序里都有成本,特别是低端设备可能无法编译大量动画,所以在启用许多动画时要小心.

注意动画即使没有被任何成员使用,也不会自动禁用,可能成员太多,无法高效使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 启用或禁用动画的名称 。 |
| enabled | boolean | 否 | 是否启用或禁用动画 。 |


**返回值:** [Phaser.GameObjects.SpriteGPULayer](/api/class/gameobjects-spritegpulayer) - 此 SpriteGPULayer 对象


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L1605](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L1605)  
引入版本：4.0.0


---

### setAnimations {#setAnimations}

#### \<instance> setAnimations(animations) {#instance-setanimationsanimations}


**说明:**

设定 SpriteGPULayer 可用的动画。 这将调用 `generateFrameDataTexture` 来重生 `frameDataTexture` 。

每部动画可以是动画对象,也可以是包含名称,持续时间,以及框名/数组的物体,如果使用动画,则会转换为对象形式,丢弃任何自定义的单个帧持续时间,并以动画持续时间作为默认.

这不是 Phaser 动画, 它不是在不设监督或交互的情况下自动在 GPU 上循环。 它不会释放事件, 允许您暂停动画, 设定重复次数等 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| animations | Array.\<[Phaser.Animations.Animation](/api/class/animations-animation)> \| Array.\<[Phaser.Types.GameObjects.SpriteGPULayer.SetAnimation](/api/typedef/types-gameobjects-spritegpulayer#setanimation)> | 否 | 要设定的一系列动画 。 |


**返回值:** [Phaser.GameObjects.SpriteGPULayer](/api/class/gameobjects-spritegpulayer) - 此 SpriteGPULayer 物件 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L494](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L494)  
引入版本：4.0.0


---

### setSegmentNeedsUpdate {#setSegmentNeedsUpdate}

#### \<instance> setSegmentNeedsUpdate(index) {#instance-setsegmentneedsupdateindex}


**说明:**

设置缓冲器的一段以要求更新。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 更新时的索引,需要更新段段. |


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayer.js#L700](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayer.js#L700)  
引入版本：4.0.0


---

---
