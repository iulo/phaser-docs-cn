# TweenData {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tweens-tweendata)

TweenData是一个包含单一目标和财产的类别,正在被曲解.

Tweens创建时创建了TweenData实例,每个目标有一个TweenData的实例,每个属性。一个Tween可以拥有多个TweenData例,但一个TweenData只属于一个Tween。

通常你不应该自己创建这些,而是使用TweenBuilder,或者`Tween.add`方法.

在Phaser 3.60之前,TweenData只是一种物体,但被重新构型到一个类,使它对自己状态和更新负责.

**构造函数**

`new TweenData(tween, targetIndex, key, getEnd, getStart, getActive, ease, delay, duration, yoyo, hold, repeat, repeatDelay, flipX, flipY, interpolation, interpolationData)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 这个TweenData实例属于这个. |
| targetIndex | number | 否 | Tween目标阵列内的目标指数. |
| key | string | 否 | 目标财产到  . |
| getEnd | [Phaser.Types.Tweens.GetEndCallback](/api/typedef/types-tweens#getendcallback) | 否 | 特温的末端会有什么财产 |
| getStart | [Phaser.Types.Tweens.GetStartCallback](/api/typedef/types-tweens#getstartcallback) | 否 | 特温号的裁武条约会有什么财产? |
| getActive | [Phaser.Types.Tweens.GetActiveCallback](/api/typedef/types-tweens#getactivecallback) | 否 | 如果不是无效,则在TweenData运行后立即引用_imteme_,并设定在目标属性上. |
| ease | function | 否 | 此 tween 使用的易操作 。 |
| delay | function | 否 | 函数返回 tween 开始前以毫秒计的时间 。 |
| duration | number | 否 | 千分之长的曲折时间. |
| yoyo | boolean | 否 | 确定在持有到期后, twin是否应该返回其起始值 。 |
| hold | number | 否 | 以毫秒计的时间, 如果 Yyo 设定为真实, 则 tween 将暂停重复或返回到它的起始值 。 |
| repeat | number | 否 | 重复的曲调次数。 曲调将永远运行一次, 故 1 的重播值将播放两次 。 |
| repeatDelay | number | 否 | 重复前的毫秒时间将开始 。 |
| flipX | boolean | 否 | 黄  还是重复时,应该叫toggleFlipX? |
| flipY | boolean | 否 | 黄  还是重复时,应该叫toggleFlipY? |
| interpolation | function | 否 | 用于数组数据的插值函数。默认为“ nall ” 。 |
| interpolationData | Array.\<number> | 否 | 要设置的插值数据阵列。 默认为“ 无效 ” 。 |

---


**作用域**: static


**继承**

> [Phaser.Tweens.BaseTweenData](/api/class/tweens-basetweendata)  



> 源码：[src/tweens/tween/TweenData.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L12)  
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
 - [yoyo](/api/class/tweens-basetweendata#yoyo)




---

## 公开成员 {#public-members}

### current {#current}

#### current: number {#current-number}


**说明:**

目标当前值,如最近一步所记录.


> 源码：[src/tweens/tween/TweenData.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L135)  
引入版本：3.60.0


---

### ease {#ease}

#### ease: function {#ease-function}


**说明:**

Tween 用于计算目标值的易性函数 。


> 源码：[src/tweens/tween/TweenData.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L108)  
引入版本：3.60.0


---

### end {#end}

#### end: number {#end-number}


**说明:**

目标最终值,由`getEndValue`返回.


> 源码：[src/tweens/tween/TweenData.js#L144](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L144)  
引入版本：3.60.0


---

### getActiveValue {#getActiveValue}

#### getActiveValue: [Phaser.Types.Tweens.GetActiveCallback](/api/typedef/types-tweens#getactivecallback) {#getactivevalue-phasertypestweensgetactivecallback}


**说明:**

函数返回目标属性设置到什么, 即TweenData 被引用时 。

当 TweenData 被关闭或重置时, 便会叫它 。


> 源码：[src/tweens/tween/TweenData.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L70)  
引入版本：3.60.0


---

### getEndValue {#getEndValue}

#### getEndValue: [Phaser.Types.Tweens.GetEndCallback](/api/typedef/types-tweens#getendcallback) {#getendvalue-phasertypestweensgetendcallback}


**说明:**

函数返回将目标属性设置在 tween 结尾的函数 。

此处是调值在调值开始播放时,在任何初始启动延迟后,或者调值重置,或者设定重播时使用.


> 源码：[src/tweens/tween/TweenData.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L82)  
引入版本：3.60.0


---

### getStartValue {#getStartValue}

#### getStartValue: [Phaser.Types.Tweens.GetStartCallback](/api/typedef/types-tweens#getstartcallback) {#getstartvalue-phasertypestweensgetstartcallback}


**说明:**

一个函数,返回在 tween 开始时设定目标属性的功能 。

此处是调值在调值开始播放时,在任何初始启动延迟后,或者调值重置,或者设定重播时使用.


> 源码：[src/tweens/tween/TweenData.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L95)  
引入版本：3.60.0


---

### interpolation {#interpolation}

#### interpolation: function {#interpolation-function}


**说明:**

用于数组数据的插值函数。


> 源码：[src/tweens/tween/TweenData.js#L153](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L153)  
引入版本：3.60.0


---

### interpolationData {#interpolationData}

#### interpolationData: Array.\<number> {#interpolationdata-arraynumber}


**说明:**

如果使用插值,则使用插值的数据数组。


> 源码：[src/tweens/tween/TweenData.js#L163](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L163)  
引入版本：3.60.0


---

### key {#key}

#### key: string {#key-string}


**说明:**

目标的财产要被扭曲。


> 源码：[src/tweens/tween/TweenData.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L60)  
引入版本：3.60.0


---

### previous {#previous}

#### previous: number {#previous-number}


**说明:**

目标值来自前一步.


> 源码：[src/tweens/tween/TweenData.js#L126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L126)  
引入版本：3.60.0


---

### start {#start}

#### start: number {#start-number}


**说明:**

目标开始值,由`getStartValue`返回.


> 源码：[src/tweens/tween/TweenData.js#L117](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L117)  
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


**Overrides:** Phaser.Tweens.BaseTweenData#销毁


> 源码：[src/tweens/tween/TweenData.js#L399](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L399)  
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


> 源码：[src/tweens/tween/TweenData.js#L366](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L366)  
引入版本：3.60.0


---

### reset {#reset}

#### \<instance> reset([isSeeking]) {#instance-resetisseeking}


**说明:**

完全重置此 Tween 数据的内部方法, 包括进度和过期值 。

由父 Tween 自动调用。 不应直接调用 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| isSeeking | boolean | 是 | false | 是否将 Tween 数据作为 Tween 请求的一部分重置 ? |


**Overrides:** Phaser.Tweens.BaseTweenData# 重置( 重置)


> 源码：[src/tweens/tween/TweenData.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L173)  
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


**Fires:** [Phaser.Tweens.Events#event:TWEEN_UPDATE](/api/event/tweens-events#tween_update), [Phaser.Tweens.Events#event:TWEEN_REPEAT](/api/event/tweens-events#tween_repeat)


> 源码：[src/tweens/tween/TweenData.js#L206](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenData.js#L206)  
引入版本：3.60.0


---

---
