# TweenFrameData {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tweens-tweenframedata)

TweenFrameData是一个包含一个单一目标,在Tween结尾会改变纹理帧的类.

TweenFrameData 实例通常由 TweenBuilder 自动创建,当它检测到存在一个“ 纹理” 属性时, 键被调解 。

一个Tween可以拥有多个TweenFrameData实例,但一个TweenFrameData只属于一个单一的Tween.

通常你不应该自己创建这些,而是使用TweenBuilder,或者`Tween.addFrame`方法.

**构造函数**

`new TweenFrameData(tween, targetIndex, texture, frame, delay, duration, hold, repeat, repeatDelay, flipX, flipY)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 这个TweenData实例属于这个. |
| targetIndex | number | 否 | Tween目标阵列内的目标指数. |
| texture | string | 否 | 纹理键将设置于此 tween 的尾端 。 |
| frame | string \| number | 否 | 纹理帧将设置在这个  的尾端. |
| delay | function | 否 | 函数返回 tween 开始前以毫秒计的时间 。 |
| duration | number | 否 | 千分之长的曲折时间. |
| hold | number | 否 | 以毫秒计的时间, 双胞胎在重复或返回其起始纹理和框架之前会暂停, 如果 Yyo 被设定为真实的话 。 |
| repeat | number | 否 | 重复的曲调次数。 曲调将永远运行一次, 故 1 的重播值将播放两次 。 |
| repeatDelay | number | 否 | 重复前的毫秒时间将开始 。 |
| flipX | boolean | 否 | 黄  还是重复时,应该叫toggleFlipX? |
| flipY | boolean | 否 | 黄  还是重复时,应该叫toggleFlipY? |

---


**作用域**: static


**继承**

> [Phaser.Tweens.BaseTweenData](/api/class/tweens-basetweendata)  



> 源码：[src/tweens/tween/TweenFrameData.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenFrameData.js#L12)  
引入版本：3.60.0

## 继承的成员 {#inherited-members}


**From [Phaser.Tweens.BaseTweenData](/api/class/tweens-basetweendata):**


 - [delay](/api/class/tweens-basetweendata#delay)
 - [duration](/api/class/tweens-basetweendata#duration)
 - [elapsed](/api/class/tweens-basetweendata#elapsed)
 - [flipX](/api/class/tweens-basetweendata#flipX)
 - [flipY](/api/class/tweens-basetweendata#flipY)
 - [getDelay](/api/class/tweens-basetweendata#getDelay)
 - [hold](/api/class/tweens-basetweendata#hold)
 - [isCountdown](/api/class/tweens-basetweendata#isCountdown)
 - [progress](/api/class/tweens-basetweendata#progress)
 - [repeat](/api/class/tweens-basetweendata#repeat)
 - [repeatCounter](/api/class/tweens-basetweendata#repeatCounter)
 - [repeatDelay](/api/class/tweens-basetweendata#repeatDelay)
 - [state](/api/class/tweens-basetweendata#state)
 - [targetIndex](/api/class/tweens-basetweendata#targetIndex)
 - [totalDuration](/api/class/tweens-basetweendata#totalDuration)
 - [tween](/api/class/tweens-basetweendata#tween)




---

## 公开成员 {#public-members}

### endFrame {#endFrame}

#### endFrame: string, number {#endframe-string-number}


**说明:**

架子设于  尾.


> 源码：[src/tweens/tween/TweenFrameData.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenFrameData.js#L93)  
引入版本：3.60.0


---

### endTexture {#endTexture}

#### endTexture: string {#endtexture-string}


**说明:**

纹理拟定在  尾.


> 源码：[src/tweens/tween/TweenFrameData.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenFrameData.js#L75)  
引入版本：3.60.0


---

### key {#key}

#### key: string {#key-string}


**说明:**

目标的属性要被扭曲。

总是为 TweenFrameData 对象的“ 纹理 ” 。


> 源码：[src/tweens/tween/TweenFrameData.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenFrameData.js#L54)  
引入版本：3.60.0


---

### startFrame {#startFrame}

#### startFrame: string, number {#startframe-string-number}


**说明:**

初设框.


> 源码：[src/tweens/tween/TweenFrameData.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenFrameData.js#L84)  
引入版本：3.60.0


---

### startTexture {#startTexture}

#### startTexture: string {#starttexture-string}


**说明:**

纹理在  文开头设定.


> 源码：[src/tweens/tween/TweenFrameData.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenFrameData.js#L66)  
引入版本：3.60.0


---

### yoyo {#yoyo}

#### yoyo: boolean {#yoyo-boolean}


**说明:**

Tween 到达终点和任何可能设定的 `hold` 值后, 是否会恢复到它的起始纹理和框架 ?


**重写:** Phaser.Tweens.BaseTweenData# 哟#


> 源码：[src/tweens/tween/TweenFrameData.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenFrameData.js#L102)  
引入版本：3.60.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Tweens.BaseTweenData](/api/class/tweens-basetweendata):**


 - [getTarget](/api/class/tweens-basetweendata#getTarget)
 - [isComplete](/api/class/tweens-basetweendata#isComplete)
 - [isCreated](/api/class/tweens-basetweendata#isCreated)
 - [isDelayed](/api/class/tweens-basetweendata#isDelayed)
 - [isHolding](/api/class/tweens-basetweendata#isHolding)
 - [isPendingRender](/api/class/tweens-basetweendata#isPendingRender)
 - [isPlayingBackward](/api/class/tweens-basetweendata#isPlayingBackward)
 - [isPlayingForward](/api/class/tweens-basetweendata#isPlayingForward)
 - [isRepeating](/api/class/tweens-basetweendata#isRepeating)
 - [onRepeat](/api/class/tweens-basetweendata#onRepeat)
 - [setCompleteState](/api/class/tweens-basetweendata#setCompleteState)
 - [setCreatedState](/api/class/tweens-basetweendata#setCreatedState)
 - [setDelayState](/api/class/tweens-basetweendata#setDelayState)
 - [setHoldState](/api/class/tweens-basetweendata#setHoldState)
 - [setPendingRenderState](/api/class/tweens-basetweendata#setPendingRenderState)
 - [setPlayingBackwardState](/api/class/tweens-basetweendata#setPlayingBackwardState)
 - [setPlayingForwardState](/api/class/tweens-basetweendata#setPlayingForwardState)
 - [setRepeatState](/api/class/tweens-basetweendata#setRepeatState)
 - [setStateFromEnd](/api/class/tweens-basetweendata#setStateFromEnd)
 - [setStateFromStart](/api/class/tweens-basetweendata#setStateFromStart)
 - [setTargetValue](/api/class/tweens-basetweendata#setTargetValue)




---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

立即摧毁这个TweenData, 取消它的所有引用。


**重写:** Phaser.Tweens.BaseTweenData#销毁


> 源码：[src/tweens/tween/TweenFrameData.js#L298](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenFrameData.js#L298)  
引入版本：3.60.0


---

### dispatchEvent {#dispatchEvent}

#### \<instance> dispatchEvent(event, [callback]) {#instance-dispatcheventevent-callback}


**说明:**

内部方法, 将基于父 Tween 事件发布 TweenData, 并且如果提供, 也会引用给定的回调 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Types.Tweens.Event](/api/typedef/types-tweens#event) | 否 | 即将举行的活动。 |
| callback | [Phaser.Types.Tweens.TweenCallbackTypes](/api/typedef/types-tweens#tweencallbacktypes) | 是 | 引用的回调名称。 可以是 `null` 或 `undefined` 来跳过引用 。 |


> 源码：[src/tweens/tween/TweenFrameData.js#L268](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenFrameData.js#L268)  
引入版本：3.60.0


---

### reset {#reset}

#### \<instance> reset([isSeeking]) {#instance-resetisseeking}


**说明:**

完全重置此 Tween 数据的内部方法, 包括进度和过期值 。

由父 Tween 自动调用。 不应直接调用 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| isSeeking | boolean | 是 | false | 是否将 Tween 数据作为 Tween 请求的一部分重置 ? |


**重写:** Phaser.Tweens.BaseTweenData# 重置( 重置)


> 源码：[src/tweens/tween/TweenFrameData.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenFrameData.js#L113)  
引入版本：3.60.0


---

### update {#update}

#### \<instance> update(delta) {#instance-updatedelta}


**说明:**

基于给出的三角形值推进此 TweenData 的内部方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delta | number | 否 | 三角洲时间的过去 以ms计。 |


**返回值:** boolean - 如果这个TweenData还在播放,则`true`;如果它已经完全完成,则`false`。


**触发事件:** [Phaser.Tweens.Events#event:TWEEN_UPDATE](/api/event/tweens-events#tween_update), [Phaser.Tweens.Events#event:TWEEN_REPEAT](/api/event/tweens-events#tween_repeat)


> 源码：[src/tweens/tween/TweenFrameData.js#L141](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenFrameData.js#L141)  
引入版本：3.60.0


---

---
