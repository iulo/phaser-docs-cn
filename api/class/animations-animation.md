# Animation {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/animations-animation)

以框架为基础的动画 。

Phaser中的动画由`AnimationFrame`对象的序列组成,这些对象由本类管理,同时还有影响回放的属性,如动画的帧速率或延迟.

此类包含所有属性和方法,可以直接处理动画的回放到一个`AnimationState`实例,这个实例由Sprite拥有,或类似的Game Object.

通常你不会直接创建这个类的实例,而是通过`AnimationManager`或`AnimationState`来使用他们的`create`方法,这取决于是否需要全局动画,或者本地到特定Sprite.

**构造函数**

`new Animation(manager, key, config)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Animations.AnimationManager](/api/class/animations-animationmanager) | 否 | 参考全球动画管理器 |
| key | string | 否 | 此动画的独有识别字符串 。 |
| config | [Phaser.Types.Animations.Animation](/api/typedef/types-animations#animation) | 否 | 动画配置. |

---


**作用域**: static

> 源码：[src/animations/Animation.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L15)  
引入版本：3.0.0

## 公开成员 {#public-members}

### delay {#delay}

#### delay: number {#delay-number}


**说明:**

播放开始前的 ms 延迟 。


> 源码：[src/animations/Animation.js#L127](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L127)  
引入版本：3.0.0


---

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

动画播放时间为几毫秒。 如果设定了 `frameRate` 属性, 它会覆盖这个值, 否则 `frameRate` 将衍生自 `duration` 。


> 源码：[src/animations/Animation.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L97)  
引入版本：3.0.0


---

### frameRate {#frameRate}

#### frameRate: number {#framerate-number}


**说明:**

帧每秒播放的帧速率( 如果持续时间为空, 默认为 24)


> 源码：[src/animations/Animation.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L87)  
引入版本：3.0.0


---

### frames {#frames}

#### frames: Array.\<[Phaser.Animations.AnimationFrame](/api/class/animations-animationframe)> {#frames-arrayphaseranimationsanimationframe}


**说明:**

构成此动画的动画Frame对象阵列.


> 源码：[src/animations/Animation.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L73)  
引入版本：3.0.0


---

### hideOnComplete {#hideOnComplete}

#### hideOnComplete: boolean {#hideoncomplete-boolean}


**说明:**

游戏对象的`visible`属性是否应该设定为动画完成后`false`?.


> 源码：[src/animations/Animation.js#L190](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L190)  
引入版本：3.0.0


---

### key {#key}

#### key: string {#key-string}


**说明:**

此动画的独有识别字符串 。


> 源码：[src/animations/Animation.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L54)  
引入版本：3.0.0


---

### manager {#manager}

#### manager: [Phaser.Animations.AnimationManager](/api/class/animations-animationmanager) {#manager-phaseranimationsanimationmanager}


**说明:**

参考全球动画管理器.


> 源码：[src/animations/Animation.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L45)  
引入版本：3.0.0


---

### msPerFrame {#msPerFrame}

#### msPerFrame: number {#msperframe-number}


**说明:**

每个帧有多少ms,不包括帧特定修饰符.


> 源码：[src/animations/Animation.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L108)  
引入版本：3.0.0


---

### paused {#paused}

#### paused: boolean {#paused-boolean}


**说明:**

全局暂停。 所有使用此动画实例的游戏对象都会受到此属性的影响 。


> 源码：[src/animations/Animation.js#L210](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L210)  
引入版本：3.0.0


---

### randomFrame {#randomFrame}

#### randomFrame: boolean {#randomframe-boolean}


**说明:**

从随机帧开始播放这款动画?


> 源码：[src/animations/Animation.js#L200](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L200)  
引入版本：3.60.0


---

### repeat {#repeat}

#### repeat: number {#repeat-number}


**说明:**

重复动画的次数。 设定为 - 1 以永久重复 。


> 源码：[src/animations/Animation.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L137)  
引入版本：3.0.0


---

### repeatDelay {#repeatDelay}

#### repeatDelay: number {#repeatdelay-number}


**说明:**

重复播放开始前的延迟 。


> 源码：[src/animations/Animation.js#L147](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L147)  
引入版本：3.0.0


---

### showBeforeDelay {#showBeforeDelay}

#### showBeforeDelay: boolean {#showbeforedelay-boolean}


**说明:**

如果动画有延迟设置, 在播放开始前, 当第一个帧设定在 Sprite 上时, 将控制此设定。 如果此属性是“ 假的 ” , 则此帧仅在延迟到期后设定 。 这是默认的行为 。


> 源码：[src/animations/Animation.js#L167](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L167)  
引入版本：3.60.0


---

### showOnStart {#showOnStart}

#### showOnStart: boolean {#showonstart-boolean}


**说明:**

当动画开始播放时,游戏对象的`visible`属性是否应该设定为`true`?


> 源码：[src/animations/Animation.js#L180](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L180)  
引入版本：3.0.0


---

### skipMissedFrames {#skipMissedFrames}

#### skipMissedFrames: boolean {#skipmissedframes-boolean}


**说明:**

如果时间滞后, 跳过框架, 或者总是向前走?


> 源码：[src/animations/Animation.js#L117](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L117)  
引入版本：3.0.0


---

### type {#type}

#### type: string {#type-string}


**说明:**

帧制动画(相对于骨制动画).


> 源码：[src/animations/Animation.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L63)  
引入版本：3.0.0


---

### yoyo {#yoyo}

#### yoyo: boolean {#yoyo-boolean}


**说明:**

动画Yoyo( 倒转回开始) 是否应该重复?


> 源码：[src/animations/Animation.js#L157](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L157)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### addFrame {#addFrame}

#### \<instance> addFrame(config) {#instance-addframeconfig}


**说明:**

在动画结尾添加帧.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | string \| Array.\<[Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe)> | 否 | 要么是字符串,在这种情况下它将使用与匹配键的纹理中的所有框架,要么是动画框架配置对象的数组. |


**返回值:** [Phaser.Animations.Animation](/api/class/animations-animation) - 此动画对象 。


> 源码：[src/animations/Animation.js#L281](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L281)  
引入版本：3.0.0


---

### addFrameAt {#addFrameAt}

#### \<instance> addFrameAt(index, config) {#instance-addframeatindex-config}


**说明:**

在指定的索引中,在动画中插入一个或多个帧。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 将框架插入动画中的索引。 |
| config | string \| Array.\<[Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe)> | 否 | 要么是字符串,在这种情况下它将使用与匹配键的纹理中的所有框架,要么是动画框架配置对象的数组. |


**返回值:** [Phaser.Animations.Animation](/api/class/animations-animation) - 此动画对象 。


> 源码：[src/animations/Animation.js#L296](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L296)  
引入版本：3.0.0


---

### calculateDuration {#calculateDuration}

#### \<instance> calculateDuration(target, totalFrames, [duration], [frameRate]) {#instance-calculatedurationtarget-totalframes-duration-framerate}


**说明:**

计算持续时间、帧率和msPerFrame值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 设定值的目标 。 |
| totalFrames | number | 否 | 动画中帧总数. |
| duration | number | 是 | 计算帧率的时间。 如果您想要设置 `frameRate` , 请通过 `null` 。 |
| frameRate | number | 是 | 计算持续时间的帧率 。 |


> 源码：[src/animations/Animation.js#L242](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L242)  
引入版本：3.50.0


---

### checkFrame {#checkFrame}

#### \<instance> checkFrame(index) {#instance-checkframeindex}


**说明:**

检查给定的框架索引是否有效 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 索引待查. |


**返回值:** boolean - 如果索引有效,则使用`true`,否则使用`false`.


> 源码：[src/animations/Animation.js#L335](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L335)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此动画实例。 它会删除所有事件监听器, 从全球动画管理器中删除此动画及其键, 然后依次销毁所有动画框架 。


> 源码：[src/animations/Animation.js#L917](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L917)  
引入版本：3.0.0


---

### getFirstTick {#getFirstTick}

#### \<instance> getFirstTick(state) {#instance-getfirsttickstate}


**说明:**

当此动画首次开始播放时, 内部调用。 设置累积器和 nextTick 属性 。


**访问权限:** 受保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| state | [Phaser.Animations.AnimationState](/api/class/animations-animationstate) | 否 | 游戏对象所属动画国引用此调用. |


> 源码：[src/animations/Animation.js#L350](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L350)  
引入版本：3.0.0


---

### getFrameAt {#getFrameAt}

#### \<instance> getFrameAt(index) {#instance-getframeatindex}


**说明:**

返回所提供索引的动画Frame

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 动画Frame 阵列中的索引 |


**返回值:** [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) - 动画序列提供的索引框


> 源码：[src/animations/Animation.js#L368](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L368)  
引入版本：3.0.0


---

### getFrameByProgress {#getFrameByProgress}

#### \<instance> getFrameByProgress(value) {#instance-getframebyprogressvalue}


**说明:**

返回最接近给定进度值的帧, 范围在 0 到 1 之间 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 值在 0 到 1 之间 。 |


**返回值:** [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) - 离给定进度值最近的框架 。


> 源码：[src/animations/Animation.js#L521](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L521)  
引入版本：3.4.0


---

### getFrames {#getFrames}

#### \<instance> getFrames(textureManager, frames, [defaultTextureKey]) {#instance-getframestexturemanager-frames-defaulttexturekey}


**说明:**

基于给定的框架数据创建动画Frame实例。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| textureManager | [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) | 否 | 参考全球纹理管理器. |
| frames | string \| Array.\<[Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe)> | 否 | 要么是字符串,在这种情况下它将使用与匹配键的纹理中的所有框架,要么是动画框架配置对象的数组. |
| defaultTextureKey | string | 是 | 如果框架配置对象中没有设置键,则使用键。 |


**返回值:** Array.\<[Phaser.Animations.AnimationFrame](/api/class/animations-animationframe)> - 一组新创建的动画Frame实例 。


> 源码：[src/animations/Animation.js#L383](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L383)  
引入版本：3.0.0


---

### getLastFrame {#getLastFrame}

#### \<instance> getLastFrame() {#instance-getlastframe}


**说明:**

返回此动画中的最后框架 。


**返回值:** [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) - 最后一部动画框架.


> 源码：[src/animations/Animation.js#L623](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L623)  
引入版本：3.12.0


---

### getNextTick {#getNextTick}

#### \<instance> getNextTick(state) {#instance-getnexttickstate}


**说明:**

内部调用。 设置当前动画的累积器和 nextTick 值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| state | [Phaser.Animations.AnimationState](/api/class/animations-animationstate) | 否 | 游戏对象所属动画国引用此调用. |


> 源码：[src/animations/Animation.js#L506](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L506)  
引入版本：3.0.0


---

### getTotalFrames {#getTotalFrames}

#### \<instance> getTotalFrames() {#instance-gettotalframes}


**说明:**

获得此动画中帧的总数.


**返回值:** number - 本动画中帧总数.


> 源码：[src/animations/Animation.js#L229](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L229)  
引入版本：3.50.0


---

### nextFrame {#nextFrame}

#### \<instance> nextFrame(state) {#instance-nextframestate}


**说明:**

推进动画框架.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| state | [Phaser.Animations.AnimationState](/api/class/animations-animationstate) | 否 | 动画国要推进. |


> 源码：[src/animations/Animation.js#L538](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L538)  
引入版本：3.0.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

暂停播放此动画。 暂停状态立即设定 。


**返回值:** [Phaser.Animations.Animation](/api/class/animations-animation) - 此动画对象 。


> 源码：[src/animations/Animation.js#L887](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L887)  
引入版本：3.0.0


---

### previousFrame {#previousFrame}

#### \<instance> previousFrame(state) {#instance-previousframestate}


**说明:**

当动画向后播放时内部调用,设置上一个帧,导致一个yoyo,重复,完整或更新,相应.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| state | [Phaser.Animations.AnimationState](/api/class/animations-animationstate) | 否 | 游戏对象所属动画国引用此调用. |


> 源码：[src/animations/Animation.js#L636](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L636)  
引入版本：3.0.0


---

### removeFrame {#removeFrame}

#### \<instance> removeFrame(frame) {#instance-removeframeframe}


**说明:**

从此动画实例中删除给定的动画Frame。 这是一个全局动作。 使用此动画的任何游戏对象都会受到此变化的影响 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| frame | [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) | 否 | 动画Frame要删除. |


**返回值:** [Phaser.Animations.Animation](/api/class/animations-animation) - 此动画对象 。


> 源码：[src/animations/Animation.js#L698](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L698)  
引入版本：3.0.0


---

### removeFrameAt {#removeFrameAt}

#### \<instance> removeFrameAt(index) {#instance-removeframeatindex}


**说明:**

从提供的索引中移除一个动画Frame阵列中的帧,并相应更新动画.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 动画Frame 阵列中的索引 |


**返回值:** [Phaser.Animations.Animation](/api/class/animations-animation) - 此动画对象 。


> 源码：[src/animations/Animation.js#L721](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L721)  
引入版本：3.0.0


---

### repeatAnimation {#repeatAnimation}

#### \<instance> repeatAnimation(state) {#instance-repeatanimationstate}


**说明:**

在播放时内部调用。 强迫动画重复, 只要重复计数器中有足够的计数值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| state | [Phaser.Animations.AnimationState](/api/class/animations-animationstate) | 否 | 游戏对象所属动画国引用此调用. |


**触发事件:** [Phaser.Animations.Events#event:ANIMATION_REPEAT](/api/event/animations-events#animation_repeat), Phaser.Animations.Events事件: 和平_新闻_新闻, Phaser.Animations.Events事件: 和平_动漫_KEY_REPEAT


> 源码：[src/animations/Animation.js#L741](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L741)  
引入版本：3.0.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

重播此动画的回放。 暂停状态立即重设 。


**返回值:** [Phaser.Animations.Animation](/api/class/animations-animation) - 此动画对象 。


> 源码：[src/animations/Animation.js#L902](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L902)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

将动画数据转换为 JSON 。


**返回值:** [Phaser.Types.Animations.JSONAnimation](/api/typedef/types-animations#jsonanimation) - 由此而来的 JSON 动画格式化对象 。


> 源码：[src/animations/Animation.js#L795](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L795)  
引入版本：3.0.0


---

### updateFrameSequence {#updateFrameSequence}

#### \<instance> updateFrameSequence() {#instance-updateframesequence}


**说明:**

每当此动画中添加或删除帧时, 都会在内部调用 。


**返回值:** [Phaser.Animations.Animation](/api/class/animations-animation) - 此动画对象 。


> 源码：[src/animations/Animation.js#L830](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/Animation.js#L830)  
引入版本：3.0.0


---

---
