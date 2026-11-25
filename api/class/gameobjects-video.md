# Video {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-video)

一个视频游戏对象。

这个游戏对象能够处理视频文件,视频流或媒体流的播放回放.

您可以选择“ 预装” 视频到 Phaser 视频缓存 :

```javascript
preload () {
  this.load.video('ripley', 'assets/aliens.mp4');
}

create () {
  this.add.video(400, 300, 'ripley');
}
```

您不必“ 预装” 视频。 您也可以直接从 URL 播放 :

```javascript
create () {
  this.add.video(400, 300).loadURL('assets/aliens.mp4');
}
```

在所有意图和目的上,视频都是标准的游戏对象,就像Sprite一样。因此,你可以做所有通常的事情,比如缩放、旋转、裁剪、涂料、制作互动、赋予物理体等等。

透明视频也可以通过WebM文件格式进行。提供视频文件已经用α频道编码,并提供浏览器支持WebM播放(不是全部支持),然后它将完全透明地进行游戏。

透明视频由HEVC(H.265)编码器支持,但只在某些设备和浏览器上,有时会忽略α频道,如果你想获得一致的经验,这可能会是一个问题。我们建议不要依赖HEVC。

回放完全通过大多数现代浏览器支持的"请求视频框架 API"处理,为旧浏览器提供了多填充.

### Autoplaying Videos {#autoplaying-videos}

视频只能自动播放, 如果浏览器已经解锁了交互, 或者满足了 MEI 设置。 控制自动播放的政策是巨大的, 并且不同浏览器不同。 您可以, 并且应该在这里读更多关于它的信息 : [https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide](https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide)

如果您的视频没有包含任何音频,那么当视频被_load_时,将`noAudio`参数设置为`true`,并且它会经常允许视频立即播放:

```javascript
preload () {
  this.load.video('pixar', 'nemo.mp4', true);
}
```

负载调用中的第3个参数告诉 Phaser 视频中没有任何音频音轨. 视频没有音频就可以自动播放,不需要用户交互. 带音频的视频不能做到这一点,除非它满足浏览器的MEI设置. 详见 MDN 自动播放指南.

Or:

```javascript
create () {
  this.add.video(400, 300).loadURL('assets/aliens.mp4', true);
}
```

您可以将 `noAudio` 参数设置为 `true` , 即使视频中包含音频。 它仍然允许视频立即播放, 但音频不会启动 。

关于视频回放和所支持的媒体格式的更多细节,请查看MDN:

[https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement) [https://developer.mozilla.org/en-US/docs/Web/Media/Formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats)

**构造函数**

`new Video(scene, x, y, [key])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| key | string | 是 | 游戏对象将播放的视频的可选键, 如存储在视频缓存中 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip)  
> [Phaser.GameObjects.Components.GetBounds](/api/namespace/gameobjects-components-getbounds)  
> [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting)  
> [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask)  
> [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin)  
> [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  
> [Phaser.GameObjects.Components.TextureCrop](/api/namespace/gameobjects-components-texturecrop)  
> [Phaser.GameObjects.Components.Tint](/api/namespace/gameobjects-components-tint)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/video/Video.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L19)  
引入版本：3.20.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha):**


 - [alpha](/api/namespace/gameobjects-components-alpha#alpha)
 - [alphaBottomLeft](/api/namespace/gameobjects-components-alpha#alphaBottomLeft)
 - [alphaBottomRight](/api/namespace/gameobjects-components-alpha#alphaBottomRight)
 - [alphaTopLeft](/api/namespace/gameobjects-components-alpha#alphaTopLeft)
 - [alphaTopRight](/api/namespace/gameobjects-components-alpha#alphaTopRight)





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





**From [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip):**


 - [flipX](/api/namespace/gameobjects-components-flip#flipX)
 - [flipY](/api/namespace/gameobjects-components-flip#flipY)





**From [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting):**


 - [lighting](/api/namespace/gameobjects-components-lighting#lighting)
 - [selfShadow](/api/namespace/gameobjects-components-lighting#selfShadow)





**From [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask):**


 - [mask](/api/namespace/gameobjects-components-mask#mask)





**From [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin):**


 - [displayOriginX](/api/namespace/gameobjects-components-origin#displayOriginX)
 - [displayOriginY](/api/namespace/gameobjects-components-origin#displayOriginY)
 - [originX](/api/namespace/gameobjects-components-origin#originX)
 - [originY](/api/namespace/gameobjects-components-origin#originY)





**From [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes):**


 - [customRenderNodes](/api/namespace/gameobjects-components-rendernodes#customRenderNodes)
 - [defaultRenderNodes](/api/namespace/gameobjects-components-rendernodes#defaultRenderNodes)
 - [renderNodeData](/api/namespace/gameobjects-components-rendernodes#renderNodeData)





**From [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor):**


 - [scrollFactorX](/api/namespace/gameobjects-components-scrollfactor#scrollFactorX)
 - [scrollFactorY](/api/namespace/gameobjects-components-scrollfactor#scrollFactorY)





**From [Phaser.GameObjects.Components.TextureCrop](/api/namespace/gameobjects-components-texturecrop):**


 - [frame](/api/namespace/gameobjects-components-texturecrop#frame)
 - [isCropped](/api/namespace/gameobjects-components-texturecrop#isCropped)
 - [texture](/api/namespace/gameobjects-components-texturecrop#texture)





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

## 公开成员 {#public-members}

### cacheKey {#cacheKey}

#### cacheKey: string {#cachekey-string}


**说明:**

存储在视频缓存中的当前视频的键 。

如果视频不是来自缓存, 这将是一个空字符串 。


> 源码：[src/gameobjects/video/Video.js#L465](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L465)  
引入版本：3.60.0


---

### failedPlayAttempts {#failedPlayAttempts}

#### failedPlayAttempts: number {#failedplayattempts-number}


**说明:**

记录视频未能播放的次数,一般是因为用户尚未与页面互动.


> 源码：[src/gameobjects/video/Video.js#L276](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L276)  
引入版本：3.60.0


---

### frameReady {#frameReady}

#### frameReady: boolean {#frameready-boolean}


**说明:**

视频是否创建了它的纹理,并用第一个视频框来覆盖它?


> 源码：[src/gameobjects/video/Video.js#L240](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L240)  
引入版本：3.60.0


---

### glFlipY {#glFlipY}

#### glFlipY: boolean {#glflipy-boolean}


**说明:**

如果您通过 `saveTexture` 方法将这段视频保存到纹理中, 如果视频是否在 WebGL 中以 `flipY` 渲染, 则此控制会控制。 如果您发现您的视频在阴影或自定义渲染器中出现倒挂, 请翻转此属性 。


> 源码：[src/gameobjects/video/Video.js#L198](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L198)  
引入版本：4.0.0


---

### isSeeking {#isSeeking}

#### isSeeking: boolean {#isseeking-boolean}


**说明:**

录像正在寻找吗?

设定为 `true` 当 `seeking` 事件已启动,并设定为 `false` 当 `seeked` 事件被解除。


> 源码：[src/gameobjects/video/Video.js#L477](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L477)  
引入版本：3.60.0


---

### isStalled {#isStalled}

#### isStalled: boolean {#isstalled-boolean}


**说明:**

这个只读属性返回`true`,如果视频目前处于停滞状态,即由于缺少数据,或数据过多,它已经停止播放,但尚未到达视频的结尾.

如果视频 DOM 元素释放出下列任何事件,则设定此值 :

`stalled` `suspend` `waiting`

如果视频DOM元素发出`playing`事件,或处理requestVideoFrame呼叫,则清除。

听到Phaser事件`VIDEO_STALLED`通知并检查事件,看看是哪个DOM事件引起事件.

请注意, 被停滞并不总是一个负面的事情。 如果视频下载了足够多的数据到缓冲器, 以至于不需要再下载, 直至当前批次的帧已打开 。


> 源码：[src/gameobjects/video/Video.js#L249](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L249)  
引入版本：3.60.0


---

### markers {#markers}

#### markers: any {#markers-any}


**说明:**

包含序列回放的输入和输出标记的对象。


> 源码：[src/gameobjects/video/Video.js#L416](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L416)  
引入版本：3.20.0


---

### metadata {#metadata}

#### metadata: VideoFrameCallbackMetadata {#metadata-videoframecallbackmetadata}


**说明:**

如果浏览器支持请求视频框架 API, 那么这个属性将保存每次引用时从调用回调时返回的元数据 。

完整的此对象所有属性列表请参见 [https://wicg.github.io/video-rvfc/#video-frame-metadata-callback](https://wicg.github.io/video-rvfc/#video-frame-metadata-callback)。 最感兴趣的可能是 `mediaTime` 属性 :

媒体的显示时间戳(PTS)在显示帧的秒数(例如视频上的其时间戳. currentTime Timor). May对直播流或WebRTC应用有零值.

如果浏览器不支持 API,则此属性将无法定义 。


> 源码：[src/gameobjects/video/Video.js#L286](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L286)  
引入版本：3.60.0


---

### playWhenUnlocked {#playWhenUnlocked}

#### playWhenUnlocked: boolean {#playwhenunlocked-boolean}


**说明:**

视频自动播放是否应该当需要文档交互并发生时?


> 源码：[src/gameobjects/video/Video.js#L231](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L231)  
引入版本：3.20.0


---

### retry {#retry}

#### retry: number {#retry-number}


**说明:**

当前重试时间已过 。


> 源码：[src/gameobjects/video/Video.js#L307](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L307)  
引入版本：3.20.0


---

### retryInterval {#retryInterval}

#### retryInterval: number {#retryinterval-number}


**说明:**

如果一个视频由于缺乏用户交互而未能播放,则视频会等待到500ms的时间,以ms计,然后再尝试播放。默认是500ms。


> 源码：[src/gameobjects/video/Video.js#L316](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L316)  
引入版本：3.20.0


---

### snapshotTexture {#snapshotTexture}

#### snapshotTexture: [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) {#snapshottexture-phasertexturescanvastexture}


**说明:**

有个Phaser`CanvasTexture`案例 记录了录像中的最新镜头

只有当`snapshot`或`snapshotArea`方法被调用时,才会设置此功能.

在这些方法被叫出来之前,这个地产将是`undefined`.


> 源码：[src/gameobjects/video/Video.js#L185](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L185)  
引入版本：3.20.0


---

### touchLocked {#touchLocked}

#### touchLocked: boolean {#touchlocked-boolean}


**说明:**

内部旗帜持有视频锁的当前状态,如果在开始播放前需要文档交互.


> 源码：[src/gameobjects/video/Video.js#L220](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L220)  
引入版本：3.20.0


---

### video {#video}

#### video: HTMLVideoElement {#video-htmlvideoelement}


**说明:**

引用此游戏对象正在播放的 HTML 视频元素 。

将会是`undefined`,直到一个视频被装入播放。


> 源码：[src/gameobjects/video/Video.js#L152](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L152)  
引入版本：3.20.0


---

### videoTexture {#videoTexture}

#### videoTexture: [Phaser.Textures.Texture](/api/class/textures-texture) {#videotexture-phasertexturestexture}


**说明:**

游戏对象使用的 Phaser 纹理 来渲染视频 。

将会是`undefined`,直到一个视频被装入播放。


> 源码：[src/gameobjects/video/Video.js#L163](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L163)  
引入版本：3.20.0


---

### videoTextureSource {#videoTextureSource}

#### videoTextureSource: [Phaser.Textures.TextureSource](/api/class/textures-texturesource) {#videotexturesource-phasertexturestexturesource}


**说明:**

引用支持`videoTexture`纹理对象的纹理源.

将会是`undefined`,直到一个视频被装入播放。


> 源码：[src/gameobjects/video/Video.js#L174](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L174)  
引入版本：3.20.0


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





**From [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip):**


 - [resetFlip](/api/namespace/gameobjects-components-flip#resetFlip)
 - [setFlip](/api/namespace/gameobjects-components-flip#setFlip)
 - [setFlipX](/api/namespace/gameobjects-components-flip#setFlipX)
 - [setFlipY](/api/namespace/gameobjects-components-flip#setFlipY)
 - [toggleFlipX](/api/namespace/gameobjects-components-flip#toggleFlipX)
 - [toggleFlipY](/api/namespace/gameobjects-components-flip#toggleFlipY)





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





**From [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting):**


 - [setLighting](/api/namespace/gameobjects-components-lighting#setLighting)
 - [setSelfShadow](/api/namespace/gameobjects-components-lighting#setSelfShadow)





**From [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask):**


 - [clearMask](/api/namespace/gameobjects-components-mask#clearMask)
 - [createGeometryMask](/api/namespace/gameobjects-components-mask#createGeometryMask)
 - [setMask](/api/namespace/gameobjects-components-mask#setMask)





**From [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin):**


 - [setDisplayOrigin](/api/namespace/gameobjects-components-origin#setDisplayOrigin)
 - [setOrigin](/api/namespace/gameobjects-components-origin#setOrigin)
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





**From [Phaser.GameObjects.Components.TextureCrop](/api/namespace/gameobjects-components-texturecrop):**


 - [setCrop](/api/namespace/gameobjects-components-texturecrop#setCrop)
 - [setFrame](/api/namespace/gameobjects-components-texturecrop#setFrame)
 - [setTexture](/api/namespace/gameobjects-components-texturecrop#setTexture)





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

将此视频添加到 Scene 更新列表中, 以确保它收到 `preUpdate` 调用游戏的每个步骤。 当此游戏对象被添加到游戏中时, 视频会自动被 Scene 调用 。


**重写:** Phaser.GameObjects.GameObject#addedToScene


> 源码：[src/gameobjects/video/Video.js#L569](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L569)  
引入版本：3.20.0


---

### addEventHandlers {#addEventHandlers}

#### \<instance> addEventHandlers() {#instance-addeventhandlers}


**说明:**

将播放特定事件处理器添加到视频元素中。


> 源码：[src/gameobjects/video/Video.js#L1137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1137)  
引入版本：3.60.0


---

### addLoadEventHandlers {#addLoadEventHandlers}

#### \<instance> addLoadEventHandlers() {#instance-addloadeventhandlers}


**说明:**

将特定事件处理器加载到视频元素中。


> 源码：[src/gameobjects/video/Video.js#L1102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1102)  
引入版本：3.60.0


---

### addMarker {#addMarker}

#### \<instance> addMarker(key, markerIn, markerOut) {#instance-addmarkerkey-markerin-markerout}


**说明:**

在此视频中添加序列标记 。

标记允许您将视频分成序列, 以起始和结束时间来划分, 以秒表示 。

然后,您可以通过 `playMarker` 方法播放特定的标记。

注意标记时间为 _ not_ fram- profile 。 您应该以允许在每个序列前后多加加贴的方式构建您的视频, 以便允许浏览器搜索和currentTime精确度出现差异 。

关于这个问题的详情,请参看[https://github.com/w3c/media-and-entertainment/issues/4](https://github.com/w3c/media-and-entertainment/issues/4)。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 一个给这个标记的独有名称 。 |
| markerIn | number | 否 | 时间,以秒计,代表这个标记的开始. |
| markerOut | number | 否 | 时间,以秒计,代表这个标记的结束. |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L1232](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1232)  
引入版本：3.20.0


---

### changeSource {#changeSource}

#### \<instance> changeSource(key, [autoplay], [loop], [markerIn], [markerOut]) {#instance-changesourcekey-autoplay-loop-markerin-markerout}


**说明:**

这种方法允许您更改当前视频元素的源头。 它首先可以停止当前视频, 如果播放的话。 然后删除视频纹理, 如果创建了, 它将开始通过已有的视频元素播放新源。 最后, 它会制作一个新的视频纹理, 并开始播放新源 。

原因您可能希望这样做是因为需要交互解锁的视频,即使您改变了视频的来源,仍然处于解锁状态。通过将源换成新的视频,您可以避免再次通过解锁进程。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 此游戏对象将转换为播放的视频键, 存储在视频缓存中 。 |
| autoplay | boolean | 是 | true | 视频应该马上播放, 交换完成后? |
| loop | boolean | 是 | false | 视频循环是否在到达尾声时自动循环? 请注意并非所有浏览器都支持所有编码格式的_无缝_视频循环 。 |
| markerIn | number | 是 |  | 可以在标记时间,秒内选择,用于播放视频的序列. |
| markerOut | number | 是 |  | 选择出标时间,以秒计,用于播放视频的序列. |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L630](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L630)  
引入版本：3.20.0


---

### completeHandler {#completeHandler}

#### \<instance> completeHandler() {#instance-completehandler}


**说明:**

视频完成回放后调用,即达到`ended`状态.

如果视频来自一个直播流,而持续时间是`Infinity`,则这永远不会发生.


**触发事件:** [Phaser.GameObjects.Events#event:VIDEO_COMPLETE](/api/event/gameobjects-events#video_complete)


> 源码：[src/gameobjects/video/Video.js#L1643](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1643)  
引入版本：3.20.0


---

### createPlayPromise {#createPlayPromise}

#### \<instance> createPlayPromise([catchError]) {#instance-createplaypromisecatcherror}


**说明:**

创建视频. play promise,并添加成功和错误处理器.

并非所有浏览器都支持视频.play承诺,因此这种方法会回归到旧式的处理视频.play呼叫的方式.

详情见[https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/play#browser_compatibility](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/play#browser_compatibility)。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| catchError | boolean | 是 | true | 是否应该抓住错误, 并标出未播放的视频 ? |


> 源码：[src/gameobjects/video/Video.js#L1182](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1182)  
引入版本：3.60.0


---

### getCurrentTime {#getCurrentTime}

#### \<instance> getCurrentTime() {#instance-getcurrenttime}


**说明:**

双精度浮点值,以秒表示当前播放时间.

如果媒体尚未开始播放,也没有被寻找,这个值是媒体最初的回放时间.

为了更准确的值,使用`Video.metadata.mediaTime`属性代替.


**返回值:** number - 双精度浮点值,以秒表示当前播放时间.


> 源码：[src/gameobjects/video/Video.js#L1731](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1731)  
引入版本：3.20.0


---

### getDuration {#getDuration}

#### \<instance> getDuration() {#instance-getduration}


**说明:**

双精度浮点值,在媒体的时长中以秒表示媒体持续时间(总长度)。如果元素上没有媒体,或者媒体无效,返回值为NaN。

如果媒体没有已知的结束(如对持续时间不明的直播流,网络电台,从WebRTC传来的媒体等),则该值为+无穷.

如果没有装入视频,此方法将返回 0 。


**返回值:** number - 双精度浮点值,以秒表示介质的持续时间.


> 源码：[src/gameobjects/video/Video.js#L1856](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1856)  
引入版本：3.20.0


---

### getFirstFrame {#getFirstFrame}

#### \<instance> getFirstFrame() {#instance-getfirstframe}


**说明:**

尝试通过运行一次 `requestVideoFrame` 回调来获得视频的第一个帧, 然后停止。 如果您需要抓取视频的第一个帧, 以显示在“ 玩” 按钮后面, 而无需实际调用“ 玩” 方法, 这样做将很有用 。

如果视频已经播放, 或者已经排队播放 `changeSource`, 那么这种方法将返回 。


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L1064](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1064)  
引入版本：3.85.0


---

### getLoop {#getLoop}

#### \<instance> getLoop() {#instance-getloop}


**说明:**

返回布尔, 表示媒体元素是否应该在它到达尾声时重新开始 。


**返回值:** boolean - 显示媒体元素何时结束的布尔 。


> 源码：[src/gameobjects/video/Video.js#L2132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L2132)  
引入版本：3.20.0


---

### getPlaybackRate {#getPlaybackRate}

#### \<instance> getPlaybackRate() {#instance-getplaybackrate}


**说明:**

返回双倍,表示媒体播放回速率。


**返回值:** number - 双倍显示媒体播放速度。


> 源码：[src/gameobjects/video/Video.js#L2097](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L2097)  
引入版本：3.20.0


---

### getProgress {#getProgress}

#### \<instance> getProgress() {#instance-getprogress}


**说明:**

返回视频作为浮点的当前进度 。

进度定义为0(起始)到1(结束)之间的值.

视频只有持续时间才能返回进度。一些视频,例如来自直播流的视频,没有持续时间。在这种情况下,方法会返回 -1.


**返回值:** number - 播放当前的进展。 如果视频没有持续时间, 将总是返回 - 1 。


> 源码：[src/gameobjects/video/Video.js#L1825](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1825)  
引入版本：3.20.0


---

### getVideoKey {#getVideoKey}

#### \<instance> getVideoKey() {#instance-getvideokey}


**说明:**

返回当前播放的视频的键, 如存储在 Video Cache 中 。

如果视频不是来自缓存, 则返回空字符串 。


**返回值:** string - 视频缓存中播放的视频的键,如果有的话.


> 源码：[src/gameobjects/video/Video.js#L666](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L666)  
引入版本：3.20.0


---

### getVolume {#getVolume}

#### \<instance> getVolume() {#instance-getvolume}


**说明:**

返回双向指示音频音量,从 0.0(沉寂)到 1.0(最粗略).


**返回值:** number - 双向表示音频音量,从0.0(沉寂)到1.0(最隆重).


> 源码：[src/gameobjects/video/Video.js#L2060](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L2060)  
引入版本：3.20.0


---

### isMuted {#isMuted}

#### \<instance> isMuted() {#instance-ismuted}


**说明:**

返回布尔表示此视频是否已变音 。


**返回值:** boolean - 布尔表示此视频是否已变音 。


> 源码：[src/gameobjects/video/Video.js#L1901](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1901)  
引入版本：3.20.0


---

### isPaused {#isPaused}

#### \<instance> isPaused() {#instance-ispaused}


**说明:**

返回布尔, 表示视频是否正在暂停 。


**返回值:** boolean - 显示视频是否暂停的布尔语 。


> 源码：[src/gameobjects/video/Video.js#L2186](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L2186)  
引入版本：3.20.0


---

### isPlaying {#isPlaying}

#### \<instance> isPlaying() {#instance-isplaying}


**说明:**

返回布尔, 以显示视频是否正在播放 。


**返回值:** boolean - 显示视频是否播放的布尔语。


> 源码：[src/gameobjects/video/Video.js#L2173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L2173)  
引入版本：3.20.0


---

### legacyPlayHandler {#legacyPlayHandler}

#### \<instance> legacyPlayHandler() {#instance-legacyplayhandler}


**说明:**

视频发出`playing`事件时打电话.

这是不支持基于承诺的回放的浏览器的遗产处理器.


> 源码：[src/gameobjects/video/Video.js#L1517](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1517)  
引入版本：3.60.0


---

### load {#load}

#### \<instance> load(key) {#instance-loadkey}


**说明:**

从视频缓存装入视频, 准备使用 `Video.play` 方法重播 。

如果视频已经播放, 这种方法允许您更改当前视频元素的来源。 它首先可以停止当前视频, 然后通过已有视频元素开始播放新源 。

原因您可能希望这样做是因为需要交互解锁的视频,即使您改变了视频的来源,仍然处于解锁状态。通过将源换成新的视频,您可以避免再次通过解锁进程。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 游戏对象将播放的视频的键, 如存储在视频缓存中 。 |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L595](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L595)  
引入版本：3.60.0


---

### loadErrorHandler {#loadErrorHandler}

#### \<instance> loadErrorHandler(event) {#instance-loaderrorhandlerevent}


**说明:**

如果视频无法加载,则自动使用这种内部方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | Event | 否 | 错误事件 。 |


**触发事件:** [Phaser.GameObjects.Events#event:VIDEO_ERROR](/api/event/gameobjects-events#video_error)


> 源码：[src/gameobjects/video/Video.js#L1551](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1551)  
引入版本：3.20.0


---

### loadHandler {#loadHandler}

#### \<instance> loadHandler([url], [noAudio], [crossOrigin], [stream]) {#instance-loadhandlerurl-noaudio-crossorigin-stream}


**说明:**

从给定的URL中装入视频的内部方法, 准备使用 `Video.play` 方法重播 。

通常不直接使用这种方法,而是使用`Video.loadURL`方法,或者使用`Video.load`方法,如果您已经预装了视频.

调用这种方法会跳过检查浏览器是否支持URL中指定格式,其中-作为其他两种方法强制进行这些检查.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| url | string | 是 | 绝对或相对的 URL 来从中加载视频文件。 如果在 MediaStream 对象中通过, 则设置为 `null` 。 |
| noAudio | boolean | 是 | 视频是否有音频音轨? 如果您不能, 您可以启用自动播放 。 |
| crossOrigin | string | 是 | 视频负载请求中用于 `crossOrigin` 属性的值。 无论是未定义的, 或 `anonymous` , 或是 `use-credentials` 。 如果没有给出值, 请在请求中不设置 `crossorigin` 。 |
| stream | string | 是 | 如果此天体正在播放流而非文件, 则使用 MediaStream 对象 。 |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L737](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L737)  
引入版本：3.60.0


---

### loadMediaStream {#loadMediaStream}

#### \<instance> loadMediaStream(stream, [noAudio], [crossOrigin]) {#instance-loadmediastreamstream-noaudio-crossorigin}


**说明:**

从给定的MediaStream对象装入一个视频,准备使用`Video.play`方法重播.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| stream | MediaStream | 否 |  | MediaStream 对象。 |
| noAudio | boolean | 是 | false | 视频是否有音频音轨? 如果您不能, 您可以启用自动播放 。 |
| crossOrigin | string | 是 |  | 视频负载请求中用于 `crossOrigin` 属性的值。 无论是未定义的, 或 `anonymous` , 或是 `use-credentials` 。 如果没有给出值, 请在请求中不设置 `crossorigin` 。 |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L720](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L720)  
引入版本：3.50.0


---

### loadURL {#loadURL}

#### \<instance> loadURL([urls], [noAudio], [crossOrigin]) {#instance-loadurlurls-noaudio-crossorigin}


**说明:**

从给定的 URL 装入视频, 准备使用 `Video.play` 方法重播 。

如果视频已经播放, 这种方法允许您更改当前视频元素的来源。 它首先可以停止当前视频, 然后通过已有视频元素开始播放新源 。

原因您可能希望这样做是因为需要交互解锁的视频,即使您改变了视频的来源,仍然处于解锁状态。通过将源换成新的视频,您可以避免再次通过解锁进程。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| urls | string \| Array.\<string> | [Phaser.Types.Loader.FileTypes.VideoFileURLConfig](/api/typedef/types-loader-filetypes#videofileurlconfig) | Array.\<[Phaser.Types.Loader.FileTypes.VideoFileURLConfig](/api/typedef/types-loader-filetypes#videofileurlconfig)> | 是 |  | 绝对或相对的URL从中加载视频文件. |
| noAudio | boolean | 是 | false | 视频是否有音频音轨? 如果您不能, 您可以启用自动播放 。 |
| crossOrigin | string | 是 |  | 视频负载请求中用于 `crossOrigin` 属性的值。 无论是未定义的, 或 `anonymous` , 或是 `use-credentials` 。 如果没有给出值, 请在请求中不设置 `crossorigin` 。 |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L681](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L681)  
引入版本：3.60.0


---

### metadataHandler {#metadataHandler}

#### \<instance> metadataHandler(event) {#instance-metadatahandlerevent}


**说明:**

当视频元数据可用时,这种内部方法会自动调用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | Event | 否 | 装满的元数据事件。 |


**触发事件:** [Phaser.GameObjects.Events#event:VIDEO_METADATA](/api/event/gameobjects-events#video_metadata)


> 源码：[src/gameobjects/video/Video.js#L1567](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1567)  
引入版本：3.80.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

如果正在播放, 暂停当前视频 。

如果没有录影带,这种方法就没有任何作用.

呼叫`Video.resume`恢复播放.


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L2026](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L2026)  
引入版本：3.60.0


---

### play {#play}

#### \<instance> play([loop], [markerIn], [markerOut]) {#instance-playloop-markerin-markerout}


**说明:**

开始播放视频。

如果视频已经播放, 或者已经排队播放 `changeSource`, 那么这种方法将返回 。

视频只能自动播放, 如果浏览器已经解锁。 发生这种情况时, 您可以与浏览器交互, 即点击它或按键, 或是由于服务器设置。 控制自动播放的政策很广, 并且不同浏览器不同 。 您可以在这里读更多 : [https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide](https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide)

如果您的视频没有包含任何音频,那么在视频装入时将`noAudio`参数设置为`true`,并且它会经常允许视频立即播放:

```javascript
preload () {
  this.load.video('pixar', 'nemo.mp4', true);
}
```

负载调用中的第3个参数告诉 Phaser 视频没有包含任何音频音轨. 视频没有音频就可以自动播放,不需要用户交互. 带音频的视频不能做到这一点,除非它满足浏览器的MEI设置. 详情请参见 MDN Autoplay Guide.

如果你在视频中需要音频,那么你就必须考虑这样一个事实:视频在用户与浏览器互动之前,不能开始播放,进入游戏流.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| loop | boolean | 是 | false | 视频循环是否在到达尾声时自动循环? 请注意并非所有浏览器都支持所有编码格式的_无缝_视频循环 。 |
| markerIn | number | 是 |  | 可以在标记时间,秒内选择,用于播放视频的序列. |
| markerOut | number | 是 |  | 选择出标时间,以秒计,用于播放视频的序列. |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L987](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L987)  
引入版本：3.20.0


---

### playError {#playError}

#### \<instance> playError(error) {#instance-playerrorerror}


**说明:**

如果播放承诺无法解决,则这种内部方法会自动被称作.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| error | DOMException | 否 | 承诺 DOM 例外错误 。 |


**触发事件:** [Phaser.GameObjects.Events#event:VIDEO_ERROR](/api/event/gameobjects-events#video_error), [Phaser.GameObjects.Events#event:VIDEO_UNSUPPORTED](/api/event/gameobjects-events#video_unsupported), [Phaser.GameObjects.Events#event:VIDEO_LOCKED](/api/event/gameobjects-events#video_locked)


> 源码：[src/gameobjects/video/Video.js#L1480](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1480)  
引入版本：3.60.0


---

### playingHandler {#playingHandler}

#### \<instance> playingHandler() {#instance-playinghandler}


**说明:**

视频发出`playing`事件时打电话.


**触发事件:** [Phaser.GameObjects.Events#event:VIDEO_PLAYING](/api/event/gameobjects-events#video_playing)


> 源码：[src/gameobjects/video/Video.js#L1537](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1537)  
引入版本：3.60.0


---

### playMarker {#playMarker}

#### \<instance> playMarker(key, [loop]) {#instance-playmarkerkey-loop}


**说明:**

在此视频中播放一个预定义的序列.

标记允许您将视频分成序列,以起始和结束时间来划分,以秒表示,并通过`addMarker`方法指定.

注意标记时间为 _ not_ fram- profile 。 您应该以允许在每个序列前后多加加贴的方式构建您的视频, 以便允许浏览器搜索和currentTime精确度出现差异 。

关于这个问题的详情,请参看[https://github.com/w3c/media-and-entertainment/issues/4](https://github.com/w3c/media-and-entertainment/issues/4)。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 游戏标记序列的名称 。 |
| loop | boolean | 是 | false | 视频循环是否在到达尾声时自动循环? 请注意并非所有浏览器都支持所有编码格式的_无缝_视频循环 。 |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L1263](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1263)  
引入版本：3.20.0


---

### playSuccess {#playSuccess}

#### \<instance> playSuccess() {#instance-playsuccess}


**说明:**

如果播放承诺成功解决,这种内部方法会自动被称作.


**触发事件:** [Phaser.GameObjects.Events#event:VIDEO_UNLOCKED](/api/event/gameobjects-events#video_unlocked)


> 源码：[src/gameobjects/video/Video.js#L1439](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1439)  
引入版本：3.60.0


---

### removedFromScene {#removedFromScene}

#### \<instance> removedFromScene() {#instance-removedfromscene}


**说明:**

从 Scene 更新列表中删除此视频, 阻止它接收 `preUpdate` 呼叫。 当此游戏对象从中移除时, 此视频会自动被 Scene 调用 。


**重写:** Phaser.GameObjects.GameObject#removedFromScene


> 源码：[src/gameobjects/video/Video.js#L582](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L582)  
引入版本：3.20.0


---

### removeEventHandlers {#removeEventHandlers}

#### \<instance> removeEventHandlers() {#instance-removeeventhandlers}


**说明:**

从视频元素中移除播放特定事件处理器 。


> 源码：[src/gameobjects/video/Video.js#L1161](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1161)  
引入版本：3.60.0


---

### removeLoadEventHandlers {#removeLoadEventHandlers}

#### \<instance> removeLoadEventHandlers() {#instance-removeloadeventhandlers}


**说明:**

从视频元素中移除加载特定事件处理器。


> 源码：[src/gameobjects/video/Video.js#L1120](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1120)  
引入版本：3.60.0


---

### removeMarker {#removeMarker}

#### \<instance> removeMarker(key) {#instance-removemarkerkey}


**说明:**

从此视频中删除先前设置的标记 。

如果标记正在播放, 它将_ not_ 停止播放 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要删除的标记名称 。 |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L1294](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1294)  
引入版本：3.20.0


---

### removeVideoElement {#removeVideoElement}

#### \<instance> removeVideoElement() {#instance-removevideoelement}


**说明:**

从 DOM 中删除视频元素, 直接调用 parentNode. removeChild 。

同时删除自动播放和src属性,并取消`Video.video`引用.

如果您通过 `Video.loadURL` 装入了外部视频, 那么您应该调用此功能, 以清除您处理完实例, 但不要破坏此视频游戏对象 。

这种方法被`Video.destroy`自动称为.


> 源码：[src/gameobjects/video/Video.js#L2308](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L2308)  
引入版本：3.20.0


---

### requestVideoFrame {#requestVideoFrame}

#### \<instance> requestVideoFrame(now, metadata) {#instance-requestvideoframenow-metadata}


**说明:**

这种方法处理请求视频框架调用.

其名称由浏览器在新视频帧准备显示时使用.

其还负责视频纹理的创建,如果它不存在,如果存在,它会按要求更新纹理.

关于请求视频框架的更多详情,请参见:[https://web.dev/requestvideoframecallback-rvfc](https://web.dev/requestvideoframecallback-rvfc)

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| now | DOMHighResTimeStamp | 否 | 以毫秒计的当前时间 。 |
| metadata | VideoFrameCallbackMetadata | 否 | 关于最近为组成而提出的视频框架的有用元数据。见 https://wicg.github.io/video-rvfc/#video-frame-metadata-callback |


**触发事件:** [Phaser.GameObjects.Events#event:VIDEO_CREATED](/api/event/gameobjects-events#video_created), [Phaser.GameObjects.Events#event:VIDEO_LOOP](/api/event/gameobjects-events#video_loop), [Phaser.GameObjects.Events#event:VIDEO_COMPLETE](/api/event/gameobjects-events#video_complete), [Phaser.GameObjects.Events#event:VIDEO_PLAY](/api/event/gameobjects-events#video_play), [Phaser.GameObjects.Events#event:VIDEO_TEXTURE](/api/event/gameobjects-events#video_texture)


> 源码：[src/gameobjects/video/Video.js#L850](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L850)  
引入版本：3.60.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

恢复当前视频, 如果一个视频是之前播放的, 并且已被暂停 。

如果没有录影带,这种方法就没有任何作用.

呼叫`Video.pause`暂停播放.


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L2043](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L2043)  
引入版本：3.60.0


---

### saveSnapshotTexture {#saveSnapshotTexture}

#### \<instance> saveSnapshotTexture(key) {#instance-savesnapshottexturekey}


**说明:**

使用给定的键在纹理管理器中存储此 Videos `snapshotTexture` 的副本 。

这种纹理是在`snapshot`或`snapshotArea`方法被称作时创建的.

完成此任务后,任何基于纹理的游戏对象,如Sprite,都可以使用纹理键使用快照的内容:

```javascript
var vid = this.add.video(0, 0, 'intro');

vid.snapshot();

vid.saveSnapshotTexture('doodle');

this.add.image(400, 300, 'doodle');
```

更新 `snapshotTexture`的内容, 例如再次拨打 `snapshot` , 将自动更新使用它作为纹理的_ 任意_ 游戏对象。 调用 `saveSnapshotTexture` 将不再保存同一纹理的另一副本, 它只是重新命名现有的一个 。

默认它会创建一个单一的基础纹理。 您可以使用 `Texture.add` 方法在纹理中添加帧。 这样做之后, 您可以允许 Game Objects 使用特定的帧 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 将纹理存储在全球纹理管理器内部的独有键 。 |


**返回值:** [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) - 保存下来的纹理。


> 源码：[src/gameobjects/video/Video.js#L1391](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1391)  
引入版本：3.20.0


---

### saveTexture {#saveTexture}

#### \<instance> saveTexture(key, [flipY]) {#instance-savetexturekey-flipy}


**说明:**

将此视频存储在纹理管理器中, 使用给定的键作为动态纹理, 任何基于纹理的游戏对象, 如Sprite, 都可以使用它作为源 :

```javascript
const vid = this.add.video(0, 0, 'intro');

vid.play();

vid.saveTexture('doodle');

this.add.image(400, 300, 'doodle');
```

如果视频尚未播放, 您需要先为 `TEXTURE_READY` 事件收听, 然后再在游戏对象上使用此纹理 :

```javascript
const vid = this.add.video(0, 0, 'intro');

vid.play();

vid.once('textureready', (video, texture, key) => {

    this.add.image(400, 300, key);

});

vid.saveTexture('doodle');
```

保存的纹理会随着视频播放自动更新。 如果您暂停此视频, 或者更改其来源, 那么保存的纹理会立即更新 。

调用 `saveTexture` 将无法保存同一纹理的另一副本, 它只是将现有的一个重命名 。

默认它会创建一个单一的基础纹理。 您可以使用 `Texture.add` 方法在纹理中添加帧。 这样做之后, 您可以允许 Game Objects 使用特定的帧 。

如果您打算保存纹理, 以便您可以把它作为阴影的输入, 如果您发现视频在阴影中颠倒, 您可能需要切换 `flipY` 参数 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 将纹理存储在全球纹理管理器内部的独有键 。 |
| flipY | boolean | 是 | true | 上传时 WebGL纹理应该设置 `UNPACK_MULTIPLY_FLIP_Y`吗? |


**返回值:** boolean - 如果纹理立即可用, 返回 `true`, 否则返回 `false`, 您应该为 `TEXTURE_READY` 事件聆听 。


> 源码：[src/gameobjects/video/Video.js#L2199](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L2199)  
引入版本：3.20.0


---

### seekTo {#seekTo}

#### \<instance> seekTo(value) {#instance-seektovalue}


**说明:**

查找视频中某个特定点。 值作为0到1之间的浮点给出, 其中0代表视频的起始点, 1代表结尾点。

寻找工作只当视频有持续时间,所以不会为直播流工作.

当开始搜索时, 此视频会发出 `seeking` 事件。 当视频完成搜索( 即到达指定的时间戳) 时, 它将发出 `seeked` 事件 。

如果你想根据时间来寻找,请使用`Video.setCurrentTime`方法.

不幸的是,DOM视频元素并不能保证求帧精确。这是持续讨论的主题:[https://github.com/w3c/media-and-entertainment/issues/4](https://github.com/w3c/media-and-entertainment/issues/4)

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 视频中要寻找的点,值在0到1之间. |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L1691](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1691)  
引入版本：3.20.0


---

### setCurrentTime {#setCurrentTime}

#### \<instance> setCurrentTime(value) {#instance-setcurrenttimevalue}


**说明:**

寻找视频中给定的播放时间。 数值以 _ seconds_ 或字符串表示 。

寻找工作只当视频有持续时间,所以不会为直播流工作.

当开始搜索时, 此视频会发出 `seeking` 事件。 当视频完成搜索( 即到达指定的时间戳) 时, 它将发出 `seeked` 事件 。

您可以提供带有 `+` 或 `-` 的字符串前缀, 如 `+2.5` 或 `-2.5` 。 在这种情况下, 它会寻求 +/ - 相对于 _ 时空_ 的值 。

如果您想根据持续时间百分比来寻找,请使用`Video.seekTo`方法。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | string \| number | 否 | 以秒计的播放时间。 可以表达为字符串, 如 `+2` , 以从当前时间提前 2 秒 。 |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L1748](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1748)  
引入版本：3.20.0


---

### setLoop {#setLoop}

#### \<instance> setLoop([value]) {#instance-setloopvalue}


**说明:**

设置当前视频的循环状态。

给出的值是一个布尔值, 表示媒体元素到达尾端后是否会重新开始 。

并非所有视频都可以循环,例如直播流.

请注意,并非所有浏览器都支持所有编码格式的_seamle_视频环路.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 显示媒体元素何时结束的布尔 。 |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L2145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L2145)  
引入版本：3.20.0


---

### setMute {#setMute}

#### \<instance> setMute([value]) {#instance-setmutevalue}


**说明:**

设定当前播放视频的变种状态, 如果已装入的话 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 哑值。 `true` 如果视频应该哑音, 否则`false`。 |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L1875](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1875)  
引入版本：3.20.0


---

### setPaused {#setPaused}

#### \<instance> setPaused([value]) {#instance-setpausedvalue}


**说明:**

设置当前已装入视频的暂停状态 。

如果视频正在播放, 用 `true` 调用此方法会暂停播放。 如果视频暂停播放, 用 `false` 调用此方法会恢复播放 。

如果没有录影带,这种方法就没有任何作用.

如果视频尚未播放,则`Video.play`会被调用,没有参数.

如果视频结束,这种方法将无济于事.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 暂停值。 `true` 如果视频被暂停, `false` 恢复它 。 |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L1972](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1972)  
引入版本：3.20.0


---

### setPlaybackRate {#setPlaybackRate}

#### \<instance> setPlaybackRate([rate]) {#instance-setplaybackraterate}


**说明:**

设定当前视频的播放率 。

给出的值是双倍,表示媒体播放回速.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rate | number | 是 | 双倍显示媒体播放速度。 |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L2110](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L2110)  
引入版本：3.20.0


---

### setSizeToFrame {#setSizeToFrame}

#### \<instance> setSizeToFrame([frame]) {#instance-setsizetoframeframe}


**说明:**

设定此游戏对象的大小为给定框架的大小 。

这将不会改变游戏对象在游戏中渲染的大小。 为此, 您需要设置游戏对象的大小( `setScale`) 或调用 `setDisplaySize` 方法, 与改变大小是相同的, 但允许您通过像素值来做到这一点 。

如果您启用了此游戏对象输入, 更改大小将_ not_ 更改命中区域的大小。 要做到这一点, 您应该直接调整 `input.hitArea` 对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| frame | [Phaser.Textures.Frame](/api/class/textures-frame) \| boolean | 是 | 将这个游戏对象的大小以框架为基础 。 |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 此游戏对象实例 。


> 源码：[src/gameobjects/video/Video.js#L1581](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1581)  
引入版本：3.0.0


---

### setVolume {#setVolume}

#### \<instance> setVolume([value]) {#instance-setvolumevalue}


**说明:**

设定当前播放视频的音量。

给出的值是表示音频音量的双倍,从0.0(沉寂)到1.0(最粗糙).

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 1 | 双向表示音频音量,从0.0(沉寂)到1.0(最隆重). |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


> 源码：[src/gameobjects/video/Video.js#L2073](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L2073)  
引入版本：3.20.0


---

### snapshot {#snapshot}

#### \<instance> snapshot([width], [height]) {#instance-snapshotwidth-height}


**说明:**

抓取当前视频框的快照并将其制作成 CanvasTexture 对象, 然后返回。 您可以通过宽度和高度可选择修改抓取大小 。

此方法返回 `Video.snapshotTexture` 对象的引用。 多次调用此方法将覆盖上次的快照和最近的快照 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 是 | 由此而来的CanvasTexture的宽度. |
| height | number | 是 | 由此而来的CanvasTexture的高度. |


**返回值:** [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) - 画像画的画像被吸引到这里


> 源码：[src/gameobjects/video/Video.js#L1313](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1313)  
引入版本：3.20.0


---

### snapshotArea {#snapshotArea}

#### \<instance> snapshotArea([x], [y], [srcWidth], [srcHeight], [destWidth], [destHeight]) {#instance-snapshotareax-y-srcwidth-srcheight-destwidth-destheight}


**说明:**

抓取当前视频框的指定区域并制作成 CanvasTexture 对象, 然后返回。 您可以通过不同的 `destWidth` 和 `destHeight` 来选择修改抓取大小 。

此方法返回 `Video.snapshotTexture` 对象的引用。 多次调用此方法将覆盖上次的快照和最近的快照 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 区域左上方的横向位置 |
| y | number | 是 | 0 | 区域左上方要抓取的垂直位置 。 |
| srcWidth | number | 是 |  | 从视频中抓取的区域宽度。 如果不给它, 将抓取视频的全部尺寸 。 |
| srcHeight | number | 是 |  | 视频的高度。 如果没有, 将抓取视频的全部尺寸 。 |
| destWidth | number | 是 |  | 抓取的目的地宽度, 允许您更改大小 。 |
| destHeight | number | 是 |  | 抓取的目的地高度,允许您调整大小 。 |


**返回值:** [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) - 画像画的画像被吸引到这里


> 源码：[src/gameobjects/video/Video.js#L1336](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1336)  
引入版本：3.20.0


---

### stalledHandler {#stalledHandler}

#### \<instance> stalledHandler(event) {#instance-stalledhandlerevent}


**说明:**

如果视频摊位出现,无论出于何种原因,这种内部方法都会自动被称作.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | Event | 否 | 摊子事件。 |


**触发事件:** [Phaser.GameObjects.Events#event:VIDEO_STALLED](/api/event/gameobjects-events#video_stalled)


> 源码：[src/gameobjects/video/Video.js#L1627](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L1627)  
引入版本：3.60.0


---

### stop {#stop}

#### \<instance> stop([emitStopEvent]) {#instance-stopemitstopevent}


**说明:**

停止播放视频,清除所有内部事件监听器.

如果您只想暂停播放视频, 并稍后恢复播放, 请使用 `Video.pause` 方法 。

如果视频没有完成下载, 调用此方法不会中止下载。 要做到这一点, 您需要拨打 `destroy` 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| emitStopEvent | boolean | 是 | true | 是否应该释放 `VIDEO_STOP`事件? |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 这个用于方法链的视频游戏对象 。


**触发事件:** [Phaser.GameObjects.Events#event:VIDEO_STOP](/api/event/gameobjects-events#video_stop)


> 源码：[src/gameobjects/video/Video.js#L2266](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/Video.js#L2266)  
引入版本：3.20.0


---

---
