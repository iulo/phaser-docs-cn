# Tween {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tweens-tween)

Tween 能根据时间和易性类型, 操纵一个或多个对象的属性到任何给定值。 它们很少直接被即时化, 而是应该通过 TweenManager 创建 。

请注意, Tween 将不会操纵任何以下划线开头的属性 。

**构造函数**

`new Tween(parent, targets)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) | 否 | 参考了拥有这款Tween的Tween经理. |
| targets | Array.\<object> | 否 | 要调整的一系列目标。 此数组不应该在此Tween 之外被操纵 。 |

---


**作用域**: static


**继承**

> [Phaser.Tweens.BaseTween](/api/class/tweens-basetween)  



> 源码：[src/tweens/tween/Tween.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L17)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Tweens.BaseTween](/api/class/tweens-basetween):**


 - [callbacks](/api/class/tweens-basetween#callbacks)
 - [callbackScope](/api/class/tweens-basetween#callbackScope)
 - [completeDelay](/api/class/tweens-basetween#completeDelay)
 - [countdown](/api/class/tweens-basetween#countdown)
 - [data](/api/class/tweens-basetween#data)
 - [hasStarted](/api/class/tweens-basetween#hasStarted)
 - [loop](/api/class/tweens-basetween#loop)
 - [loopCounter](/api/class/tweens-basetween#loopCounter)
 - [loopDelay](/api/class/tweens-basetween#loopDelay)
 - [parent](/api/class/tweens-basetween#parent)
 - [paused](/api/class/tweens-basetween#paused)
 - [persist](/api/class/tweens-basetween#persist)
 - [startDelay](/api/class/tweens-basetween#startDelay)
 - [state](/api/class/tweens-basetween#state)
 - [timeScale](/api/class/tweens-basetween#timeScale)
 - [totalData](/api/class/tweens-basetween#totalData)




---

## 公开成员 {#public-members}

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

时间以毫秒表示,整个Tween可以播放一次,不包括循环量和循环延迟.

此值以 `Tween.initTweenData` 方法设定, 并在该点之前为0 。


> 源码：[src/tweens/tween/Tween.js#L112](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L112)  
引入版本：3.60.0


---

### elapsed {#elapsed}

#### elapsed: number {#elapsed-number}


**说明:**

时间用毫秒的推移 穿过特温河


> 源码：[src/tweens/tween/Tween.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L92)  
引入版本：3.60.0


---

### isInfinite {#isInfinite}

#### isInfinite: boolean {#isinfinite-boolean}


**说明:**

这Tween是无限循环还是重复?


> 源码：[src/tweens/tween/Tween.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L82)  
引入版本：3.60.0


---

### isNumberTween {#isNumberTween}

#### isNumberTween: boolean {#isnumbertween-boolean}


**说明:**

是数字  的吗?


> 源码：[src/tweens/tween/Tween.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L158)  
引入版本：3.88.0


---

### isSeeking {#isSeeking}

#### isSeeking: boolean {#isseeking-boolean}


**说明:**

这个特温现在在寻找吗?

这个布林在`Tween.seek`方法中切换.

当一个 tween 正在寻求,默认情况下它不会发送任何事件或召回.


> 源码：[src/tweens/tween/Tween.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L68)  
引入版本：3.19.0


---

### progress {#progress}

#### progress: number {#progress-number}


**说明:**

0到1. 通过Tween的进度,不包括环路.


> 源码：[src/tweens/tween/Tween.js#L124](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L124)  
引入版本：3.60.0


---

### targets {#targets}

#### targets: Array.\<object> {#targets-arrayobject}


**说明:**

一系列关于此 Tween 正在运行的目标的引用 。

此数组不应在此 Tween 之外被操纵 。


> 源码：[src/tweens/tween/Tween.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L44)  
引入版本：3.0.0


---

### totalDuration {#totalDuration}

#### totalDuration: number {#totalduration-number}


**说明:**

时间( 毫秒) 特温需要完成一个完整的播放( 包括循环)

对于无限的Tween来说,这个值是一个非常大的整数.


> 源码：[src/tweens/tween/Tween.js#L134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L134)  
引入版本：3.60.0


---

### totalElapsed {#totalElapsed}

#### totalElapsed: number {#totalelapsed-number}


**说明:**

整个Tween中的总时间(以毫秒计),包括环绕。


> 源码：[src/tweens/tween/Tween.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L102)  
引入版本：3.60.0


---

### totalProgress {#totalProgress}

#### totalProgress: number {#totalprogress-number}


**说明:**

通过整个Tween,包括环绕,已经取得了多少进展.

值在 0 到 1 之间 。


> 源码：[src/tweens/tween/Tween.js#L146](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L146)  
引入版本：3.60.0


---

### totalTargets {#totalTargets}

#### totalTargets: number {#totaltargets-number}


**说明:**

目标总和

内部使用,应作为只读处理。

这与数据总数不一定相同。


> 源码：[src/tweens/tween/Tween.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L55)  
引入版本：3.0.0


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





**From [Phaser.Tweens.BaseTween](/api/class/tweens-basetween):**


 - [complete](/api/class/tweens-basetween#complete)
 - [completeAfterLoop](/api/class/tweens-basetween#completeAfterLoop)
 - [getTimeScale](/api/class/tweens-basetween#getTimeScale)
 - [isActive](/api/class/tweens-basetween#isActive)
 - [isCompleteDelayed](/api/class/tweens-basetween#isCompleteDelayed)
 - [isDestroyed](/api/class/tweens-basetween#isDestroyed)
 - [isFinished](/api/class/tweens-basetween#isFinished)
 - [isLoopDelayed](/api/class/tweens-basetween#isLoopDelayed)
 - [isPaused](/api/class/tweens-basetween#isPaused)
 - [isPending](/api/class/tweens-basetween#isPending)
 - [isPendingRemove](/api/class/tweens-basetween#isPendingRemove)
 - [isPlaying](/api/class/tweens-basetween#isPlaying)
 - [isRemoved](/api/class/tweens-basetween#isRemoved)
 - [isStartDelayed](/api/class/tweens-basetween#isStartDelayed)
 - [makeActive](/api/class/tweens-basetween#makeActive)
 - [pause](/api/class/tweens-basetween#pause)
 - [remove](/api/class/tweens-basetween#remove)
 - [resume](/api/class/tweens-basetween#resume)
 - [setActiveState](/api/class/tweens-basetween#setActiveState)
 - [setCallback](/api/class/tweens-basetween#setCallback)
 - [setCompleteDelayState](/api/class/tweens-basetween#setCompleteDelayState)
 - [setDestroyedState](/api/class/tweens-basetween#setDestroyedState)
 - [setFinishedState](/api/class/tweens-basetween#setFinishedState)
 - [setLoopDelayState](/api/class/tweens-basetween#setLoopDelayState)
 - [setPendingRemoveState](/api/class/tweens-basetween#setPendingRemoveState)
 - [setPendingState](/api/class/tweens-basetween#setPendingState)
 - [setRemovedState](/api/class/tweens-basetween#setRemovedState)
 - [setStartDelayState](/api/class/tweens-basetween#setStartDelayState)
 - [setTimeScale](/api/class/tweens-basetween#setTimeScale)
 - [stop](/api/class/tweens-basetween#stop)
 - [updateCompleteDelay](/api/class/tweens-basetween#updateCompleteDelay)
 - [updateLoopCountdown](/api/class/tweens-basetween#updateLoopCountdown)
 - [updateStartCountdown](/api/class/tweens-basetween#updateStartCountdown)




---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(targetIndex, key, getEnd, getStart, getActive, ease, delay, duration, yoyo, hold, repeat, repeatDelay, flipX, flipY, interpolation, interpolationData) {#instance-addtargetindex-key-getend-getstart-getactive-ease-delay-duration-yoyo-hold-repeat-repeatdelay-flipx-flipy-interpolation-interpolationdata}


**说明:**

在此 Tween 中添加一个新的 TweenData。 通常, 此方法会被 TweenBuilder 自动调用, 但是您也可以自己引用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
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


**返回值:** [Phaser.Tweens.TweenData](/api/class/tweens-tweendata) - 添加的 TweenData 实例 。


> 源码：[src/tweens/tween/Tween.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L169)  
引入版本：3.60.0


---

### addFrame {#addFrame}

#### \<instance> addFrame(targetIndex, texture, frame, delay, duration, hold, repeat, repeatDelay, flipX, flipY) {#instance-addframetargetindex-texture-frame-delay-duration-hold-repeat-repeatdelay-flipx-flipy}


**说明:**

将一个新的 TweenFrameData 添加到此 Tween 中。 通常情况下, 此方法会自动被 TweenBuilder 所使用, 但是您也可以自己引用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| targetIndex | number | 否 | Tween目标阵列内的目标指数. |
| texture | string | 否 | 纹理设定目标时的端部为  . |
| frame | string \| number | 否 | 纹理框架设定在  尾的目标上. |
| delay | function | 否 | 函数返回 tween 开始前以毫秒计的时间 。 |
| duration | number | 否 | 千分之长的曲折时间. |
| hold | number | 否 | 以毫秒计的时间, 如果 Yyo 设定为真实, 则 tween 将暂停重复或返回到它的起始值 。 |
| repeat | number | 否 | 重复的曲调次数。 曲调将永远运行一次, 故 1 的重播值将播放两次 。 |
| repeatDelay | number | 否 | 重复前的毫秒时间将开始 。 |
| flipX | boolean | 否 | 黄  还是重复时,应该叫toggleFlipX? |
| flipY | boolean | 否 | 黄  还是重复时,应该叫toggleFlipY? |


**返回值:** [Phaser.Tweens.TweenFrameData](/api/class/tweens-tweenframedata) - 添加的TweenFrameData实例。


> 源码：[src/tweens/tween/Tween.js#L205](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L205)  
引入版本：3.60.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

处理这个 Tween 的破坏过程, 清除 Tween 数据并重设目标。 已被破坏的 Tween 永远不能被玩弄或使用 。


**Overrides:** Phaser.Tweens.BaseTween#销毁


> 源码：[src/tweens/tween/Tween.js#L816](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L816)  
引入版本：3.60.0


---

### dispatchEvent {#dispatchEvent}

#### \<instance> dispatchEvent(event, [callback]) {#instance-dispatcheventevent-callback}


**说明:**

内部方法,将释放出基于Tween的事件并引用给定的回调.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Types.Tweens.Event](/api/typedef/types-tweens#event) | 否 | 即将举行的活动。 |
| callback | [Phaser.Types.Tweens.TweenCallbackTypes](/api/typedef/types-tweens#tweencallbacktypes) | 是 | 引用的回调名称。 可以是 `null` 或 `undefined` 来跳过引用 。 |


> 源码：[src/tweens/tween/Tween.js#L787](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L787)  
引入版本：3.60.0


---

### forward {#forward}

#### \<instance> forward(ms) {#instance-forwardms}


**说明:**

以给定的毫秒数移动此 Tween 。

它只会通过Tween的当前循环推进,例如,如果Tween被设定为重复或yoyo,它只能通过序列的单个部分快速前进. 使用`Tween.seek`来进行更复杂的玩头控制.

如果Tween被暂停或已经完成,调用这个不会产生任何效果.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ms | number | 否 | 以毫秒数推进此图文. |


**返回值:** [Phaser.Tweens.Tween](/api/class/tweens-tween) - 此特云证.


> 源码：[src/tweens/tween/Tween.js#L741](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L741)  
引入版本：3.60.0


---

### getValue {#getValue}

#### \<instance> getValue([index]) {#instance-getvalueindex}


**说明:**

返回指定的Tween数据的当前值。

如果这个Tween被摧毁了,它会归还`null`.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| index | number | 是 | 0 | 数据以返回值. |


**返回值:** number, null - 请求的 Tween 数据的值, 或 `null` 如果这个特温已经被摧毁了


> 源码：[src/tweens/tween/Tween.js#L235](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L235)  
引入版本：3.0.0


---

### hasTarget {#hasTarget}

#### \<instance> hasTarget(target) {#instance-hastargettarget}


**说明:**

看看这个Tween是否正在针对指定目标采取行动.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | object | 否 | 目标检查这个Tween。 |


**返回值:** boolean - 如果给定的目标就是这个Tween的目标,则`true`,否则就是`false`.


> 源码：[src/tweens/tween/Tween.js#L261](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L261)  
引入版本：3.0.0


---

### initTweenData {#initTweenData}

#### \<instance> initTweenData([isSeeking]) {#instance-inittweendataisseeking}


**说明:**

初始化所有 Tween 数据和 Tween 值 。

这自动称为,一般不应直接援引。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| isSeeking | boolean | 是 | false | 是否将 Tween 数据重新设定为搜索的一部分 ? |


> 源码：[src/tweens/tween/Tween.js#L553](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L553)  
引入版本：3.60.0


---

### nextState {#nextState}

#### \<instance> nextState() {#instance-nextstate}


**说明:**

播放时推进到Tween下一状态的内部方法.


**返回值:** boolean - 如果Tween完成的话,就用`true`,否则用`false`.


**Fires:** [Phaser.Tweens.Events#event:TWEEN_COMPLETE](/api/event/tweens-events#tween_complete), [Phaser.Tweens.Events#event:TWEEN_LOOP](/api/event/tweens-events#tween_loop)


> 源码：[src/tweens/tween/Tween.js#L365](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L365)  
引入版本：3.0.0


---

### onCompleteHandler {#onCompleteHandler}

#### \<instance> onCompleteHandler() {#instance-oncompletehandler}


**说明:**

处理此  的内部方法完成并启动链中的下一个  ,如果有的话.


**Overrides:** Phaser.Tweens.BaseTween#onCompleteHandler


> 源码：[src/tweens/tween/Tween.js#L414](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L414)  
引入版本：3.60.0


---

### play {#play}

#### \<instance> play() {#instance-play}


**说明:**

开始玩Tween。

您只需要在创建时配置了 tween 即可调用此方法 。

如果 Tween 已经播放, 调用此方法将没有效果 。 如果您想要重新启动 Tween , 请使用 `Tween.restart` 来代替 。

Tween 完成后调用这种方法将重新开始 Tween 播放。 这与调用 `Tween.seek(0)` 和 后调用 `Tween.play()` 相同 。


**返回值:** [Phaser.Tweens.Tween](/api/class/tweens-tween) - 此特云证.


> 源码：[src/tweens/tween/Tween.js#L429](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L429)  
引入版本：3.0.0


---

### reset {#reset}

#### \<instance> reset([skipInit]) {#instance-resetskipinit}


**说明:**

重新准备这个 Tween 进行另一场比赛

这从Tween管理器或从母的TweenChain自动调用,一般不应直接引用.

如果您想要重启此 Tween, 请使用 `Tween.restart` 或 `Tween.seek` 方法 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| skipInit | boolean | 是 | false | 跳过重置 TweenData 和 active 状态 ? |


**返回值:** [Phaser.Tweens.Tween](/api/class/tweens-tween) - 此特云证.


**Fires:** [Phaser.Tweens.Events#event:TWEEN_ACTIVE](/api/event/tweens-events#tween_active)


> 源码：[src/tweens/tween/Tween.js#L596](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L596)  
引入版本：3.60.0


---

### restart {#restart}

#### \<instance> restart() {#instance-restart}


**说明:**

从初复发  文.

如果 Tween 已完成并被销毁, 重新启动它会丢出一个错误 。

如果您想从特定点重新启动Tween,请使用`Tween.seek`方法代替.


**返回值:** [Phaser.Tweens.Tween](/api/class/tweens-tween) - 此特云证.


> 源码：[src/tweens/tween/Tween.js#L323](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L323)  
引入版本：3.0.0


---

### rewind {#rewind}

#### \<instance> rewind(ms) {#instance-rewindms}


**说明:**

将 Tween 向后移动到给定的毫秒。

它只会通过Tween的当前循环回转,例如,如果Tween被设定为重复或yoyo,它只能通过序列的单个部分回转. 使用`Tween.seek`来进行更复杂的播放头控制.

如果Tween被暂停或已经完成,调用这个不会产生任何效果.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ms | number | 否 | 倒转这个 Tween 的毫秒数 。 |


**返回值:** [Phaser.Tweens.Tween](/api/class/tweens-tween) - 此特云证.


> 源码：[src/tweens/tween/Tween.js#L764](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L764)  
引入版本：3.60.0


---

### seek {#seek}

#### \<instance> seek([amount], [delta], [emit]) {#instance-seekamount-delta-emit}


**说明:**

求于特温中特定分.

给定的金额是一个以毫秒计的值,它代表您想要从图文开始到图文的距离。

注意, 求值包含整个Tween 持续时间, 包括延迟、 循环和重复。 例如, 一个持续2秒但循环3次的Tween 将总持续时间为6秒, 因此, 寻求 3,000 ms 将根据其 _ entire_ 持续时间向 Tweens 半程点求值 。

在Phaser 3.60之前,这个值被给出在0到1之间的数字,对Tweens没有无限重复的效果,这个新方法对所有Tweens都有效.

将 Tween 重置为初始值, 然后在 Tween 中按每步 `delta` 跳跃来浏览 。 Tween 越长, 这个时间就越长 。 如果您需要更精确的查找, 您可以降低三角洲值。 如果您需要更快的查找, 您可以增加它。 当 Tween 重设时, 它会刷新起始值和结尾值。 如果这些值来自动态函数, 或者随机数组, 则需要每个查找 。

在寻找 Tween 时, 除非将 3 参数设置为 `true` , 否则_ 不_ 发出它的任何事件或回调 。

如果这个Tween被暂停,寻求将不会改变这个事实,它将将Tween推进到理想点,然后再次暂停.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| amount | number | 是 | 0 | 初明求入特温数毫秒. |
| delta | number | 是 | 16.6 | 查找 Tween 时每个步骤的大小。 更高的值完成得更快, 但代价更不精确 。 |
| emit | boolean | 是 | false | 在寻求时,特温号是否应该放出任何事件或召回?默认是‘虚伪',即默默寻求. |


**返回值:** [Phaser.Tweens.Tween](/api/class/tweens-tween) - 此特云证.


> 源码：[src/tweens/tween/Tween.js#L466](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L466)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update(delta) {#instance-updatedelta}


**说明:**

以时间值为基础推进Tween的内部方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


**返回值:** boolean - 如果 Tween 完成并应该从 Tween 管理器中移除, 返回 `true`, 否则返回 `false` 。


**Fires:** [Phaser.Tweens.Events#event:TWEEN_COMPLETE](/api/event/tweens-events#tween_complete), [Phaser.Tweens.Events#event:TWEEN_LOOP](/api/event/tweens-events#tween_loop), [Phaser.Tweens.Events#event:TWEEN_START](/api/event/tweens-events#tween_start)


> 源码：[src/tweens/tween/Tween.js#L640](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L640)  
引入版本：3.0.0


---

### updateTo {#updateTo}

#### \<instance> updateTo(key, value, [startToCurrent]) {#instance-updatetokey-value-starttocurrent}


**说明:**

只要Tween目前播放( 要么向前, 要么向后) , 更新所有匹配目标的给定属性的“ end” 值 。

调用此选项不会调整 Tween 的长度, 或当前的进展 。

您可以选择将其设置为当前值的“ 启动” 值 。

如果Tween除了演奏之外处于任何其他状态,那么称这种方法没有效果.

此外,如果Tween重复,被重置,或被寻求,它会恢复到原来的起始和结尾值.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 设置新值的属性。 您无法通过此方法更新“ 纹理” 属性 。 |
| value | number | 否 |  | 地产的新价值. |
| startToCurrent | boolean | 是 | false | 此更改是否应该将起始值设定为当前值 ? |


**返回值:** [Phaser.Tweens.Tween](/api/class/tweens-tween) - 此特云证.


> 源码：[src/tweens/tween/Tween.js#L276](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L276)  
引入版本：3.0.0


---

---
