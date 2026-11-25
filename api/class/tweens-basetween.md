# BaseTween {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tweens-basetween)

如名称所暗示,这是Tween和TweenChain都继承的基底Tween类,包含两种类型Tween共同的共有属性和方法.

通常你不会直接即兴表演这个课,尽管你肯定可以用它来创造出自己对Tweens的变体。

**构造函数**

`new BaseTween(parent)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) \| [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) | 否 | 参考了Tween经理,或Tween链,拥有这个Tween. |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/tweens/tween/BaseTween.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L12)  
引入版本：3.60.0

## 公开成员 {#public-members}

### callbacks {#callbacks}

#### callbacks: [Phaser.Types.Tweens.TweenCallbacks](/api/typedef/types-tweens#tweencallbacks) {#callbacks-phasertypestweenstweencallbacks}


**说明:**

包含不同Tween调用函数的对象。

你可以把这些设置在Tween配置中, 或者使用`Tween.setCallback`方法。

现有类型如下:

`onActive` - 当 Tween 创建之初, 它会移动到“ 活动” 状态, 当添加到 Tween 管理器中时。 “ 主动” 并不意味着“ 玩” 。 `onStart` 当Tween在延迟状态或暂停状态后开始播放时。这将会同时发生。 `onActive` 如果这个圈子没有拖延,也没有停顿。 `onLoop` - 当一个Tween循环,如果它被设定这样做。这发生在_after_ the `loopDelay` 过期, 如果设置 。 `onComplete` 当Tween完全重播时, 如果Tween被设定为无限重播, 则永远不要引用 。 `onStop` - 只有在 `Tween.stop` 方法叫做 。 `onPause` - 只有在 `Tween.pause` 方法。如果 Tween 管理器被暂停,则不引用。 `onResume` - 只有在 `Tween.resume` 方法。如果 Tween 管理器恢复使用,则不引用。

以下类型也可用,并被引用在`TweenData`级别上——即每个对象,每个财产,被加成  .

`onYoyo` 当TweenData开始一个优等生。 `hold` 如果设置, 延迟过期 。 `onRepeat` 当TweenData重复播放时。这种情况发生在_after_ the `repeatDelay` 过期, 如果设置 。 `onUpdate` - 当TweenData在播放时更新源目标上的属性时。


> 源码：[src/tweens/tween/BaseTween.js#L195](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L195)  
引入版本：3.60.0


---

### callbackScope {#callbackScope}

#### callbackScope: any {#callbackscope-any}


**说明:**

引用所有回调的范围(或上下文).

此默认为 Tween, 但是您可以覆盖此属性, 设置为您需要的对象 。


> 源码：[src/tweens/tween/BaseTween.js#L233](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L233)  
引入版本：3.60.0


---

### completeDelay {#completeDelay}

#### completeDelay: number {#completedelay-number}


**说明:**

以毫秒计的时数 在"onComplete"事件起火前

如果`loop = -1`没有完成,这永远不会起火,因为它已经注定永远循环。


> 源码：[src/tweens/tween/BaseTween.js#L149](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L149)  
引入版本：3.60.0


---

### countdown {#countdown}

#### countdown: number {#countdown-number}


**说明:**

内部倒计时器(由loopDelay和completeDelay使用)


> 源码：[src/tweens/tween/BaseTween.js#L162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L162)  
引入版本：3.60.0


---

### data {#data}

#### data: Array.\<[Phaser.Tweens.TweenData](/api/class/tweens-tweendata)>, Array.\<[Phaser.Tweens.Tween](/api/class/tweens-tween)> {#data-arrayphasertweenstweendata-arrayphasertweenstween}


**说明:**

主要的数据阵列。 对于一个Tween, 它包含所有 `TweenData` 对象, 每个对象都包含一个独特的属性和目标, 正在被调整 。

对于一个TweenChain,它包含一系列`Tween`实例,它们正在按顺序播放。


> 源码：[src/tweens/tween/BaseTween.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L47)  
引入版本：3.60.0


---

### hasStarted {#hasStarted}

#### hasStarted: boolean {#hasstarted-boolean}


**说明:**

这个Tween开始重播了吗?

当 Tween 离开“ 启动延迟” 状态并开始运行时, 此布尔会切换 。


> 源码：[src/tweens/tween/BaseTween.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L82)  
引入版本：3.60.0


---

### loop {#loop}

#### loop: number {#loop-number}


**说明:**

此特温循环的次数.

可以是 -1 表示无限环,0表示无,也可以表示正整数.

通常这在配置对象中设置,但也可以直接设置,只要Tween暂停,没有开始播放.

启用后, 它将再次通过所有调值器播放 。

使用 TweenData.repeat 循环单个元素.


> 源码：[src/tweens/tween/BaseTween.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L108)  
引入版本：3.60.0


---

### loopCounter {#loopCounter}

#### loopCounter: number {#loopcounter-number}


**说明:**

内部计数器记录了有多少个循环还剩运行.


> 源码：[src/tweens/tween/BaseTween.js#L139](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L139)  
引入版本：3.60.0


---

### loopDelay {#loopDelay}

#### loopDelay: number {#loopdelay-number}


**说明:**

特温环形山前的毫秒时间.

只有在 `loop` 大于 0 时才使用.


> 源码：[src/tweens/tween/BaseTween.js#L127](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L127)  
引入版本：3.60.0


---

### parent {#parent}

#### parent: [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager), [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) {#parent-phasertweenstweenmanager-phasertweenstweenchain}


**说明:**

参考了Tween经理,或Tween链,拥有这个Tween.


> 源码：[src/tweens/tween/BaseTween.js#L38](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L38)  
引入版本：3.60.0


---

### paused {#paused}

#### paused: boolean {#paused-boolean}


**说明:**

特温号目前暂停吗 ?

需要用`play`方法开始暂停的Tween,或者用`resume`方法恢复.

需要时, 此属性可以在运行时切换 。


> 源码：[src/tweens/tween/BaseTween.js#L181](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L181)  
引入版本：3.60.0


---

### persist {#persist}

#### persist: boolean {#persist-boolean}


**说明:**

此 Tween 是否在播放后会持续 ? 坚持的 Tween 会被 Tween 管理器销毁 _ not_ , 或者在调用 `Tween.stop` 时被重播, 并可以根据需要重新播放 。 您可以在 创建 tween 配置时设置此属性, 或者设置 _ preor_ 以重播 。

然而,你有责任确保你销毁 持久性的扭矩 当你完成它们, 或者他们会保留 引用你可能不再需要 浪费记忆。

默认情况下,`Tweens`被设定为_not_持续,因此它们会被Tween管理器自动清理.


> 源码：[src/tweens/tween/BaseTween.js#L245](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L245)  
引入版本：3.60.0


---

### startDelay {#startDelay}

#### startDelay: number {#startdelay-number}


**说明:**

以毫秒计的时数 在"onStart"事件起火前

对于一个Tween, 这是它拥有的所有TweenDatas中最短的 `delay`值。 对于TweenChain, 无论是哪个配置给出了延迟值, 都是一样的 。


> 源码：[src/tweens/tween/BaseTween.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L69)  
引入版本：3.60.0


---

### state {#state}

#### state: [Phaser.Tweens.StateType](/api/typedef/tweens#statetype) {#state-phasertweensstatetype}


**说明:**

文氏的目前状态.


> 源码：[src/tweens/tween/BaseTween.js#L172](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L172)  
引入版本：3.60.0


---

### timeScale {#timeScale}

#### timeScale: number {#timescale-number}


**说明:**

缩放此 Tween 应用的时间。 1 的值是实时运行的。 0. 5 的值是慢了 50% 。

计算  的总持续时间时不使用该值,它只是运行时三角洲调整.

此值乘以 `TweenManager.timeScale` 。


> 源码：[src/tweens/tween/BaseTween.js#L94](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L94)  
引入版本：3.60.0


---

### totalData {#totalData}

#### totalData: number {#totaldata-number}


**说明:**

数据数组的缓存大小 。


> 源码：[src/tweens/tween/BaseTween.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L60)  
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




---

## 公开方法 {#public-methods}

### complete {#complete}

#### \<instance> complete([delay]) {#instance-completedelay}


**说明:**

标注Tween号是完整的, 无论它处于哪个阶段。

如果`onComplete`召回定义已经定义,它将自动引用,除非提供`delay`参数,在这种情况下,Tween在调回召回之前会延迟该时间段.

如果你不需要延迟或没有`onComplete`调用,那么就叫`Tween.stop`。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| delay | number | 是 | 0 | 等待时间,然后启动完全回调 如果0,它会立即开火。 |


**返回值:** [Phaser.Tweens.BaseTween](/api/class/tweens-basetween) - 此特云证.


**Fires:** [Phaser.Tweens.Events#event:TWEEN_COMPLETE](/api/event/tweens-events#tween_complete)


> 源码：[src/tweens/tween/BaseTween.js#L404](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L404)  
引入版本：3.2.0


---

### completeAfterLoop {#completeAfterLoop}

#### \<instance> completeAfterLoop([loops]) {#instance-completeafterlooploops}


**说明:**

标记为当前循环完成后才完成 Truen 。

这是一种有用的方法,可以阻止一个完整的周期一旦结束,而不是突然的循环。

如果你没有回路 那就叫`Tween.stop`来代替

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| loops | number | 是 | 0 | 完成此 tween 之前的循环数。 0 表示仅完成当前循环 。 |


**返回值:** [Phaser.Tweens.BaseTween](/api/class/tweens-basetween) - 此特云证.


**Fires:** [Phaser.Tweens.Events#event:TWEEN_COMPLETE](/api/event/tweens-events#tween_complete)


> 源码：[src/tweens/tween/BaseTween.js#L438](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L438)  
引入版本：3.60.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

处理这个 Tween 的破坏过程, 销毁所有 TweenData 对象, 移除所有事件听众, 并取消内部引用 。 已被破坏的 Tween 将永远无法被玩弄或使用 。


**Overrides:** Phaser.Events.EventEmitter#销毁


> 源码：[src/tweens/tween/BaseTween.js#L851](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L851)  
引入版本：3.60.0


---

### getTimeScale {#getTimeScale}

#### \<instance> getTimeScale() {#instance-gettimescale}


**说明:**

获得这个 Tween 应用的时间尺度值。 1 的值在实时运行。 0. 5 的值在运行中慢50% 。


**返回值:** number - 时间尺度的值适用于这个Tween.


> 源码：[src/tweens/tween/BaseTween.js#L285](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L285)  
引入版本：3.60.0


---

### isActive {#isActive}

#### \<instance> isActive() {#instance-isactive}


**说明:**

如果此 Tween 具有 _ Excuse_ 状态 , 返回 `true`, 否则返回 `false` 。


**返回值:** boolean - `true` 如果此图文具有 ACTIE 的 _ 流_状态, 否则 `false`.


> 源码：[src/tweens/tween/BaseTween.js#L747](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L747)  
引入版本：3.60.0


---

### isCompleteDelayed {#isCompleteDelayed}

#### \<instance> isCompleteDelayed() {#instance-iscompletedelayed}


**说明:**

如果 Tween 具有 _xxx_xxxx 的 Complete_DELAY 状态, 返回 `true`, 否则返回 `false` 。


**返回值:** boolean - 如果这个 Tween 具有 Complete_DELAY 的 _ current_状态,则使用 `true` , 否则使用 `false` 。


> 源码：[src/tweens/tween/BaseTween.js#L773](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L773)  
引入版本：3.60.0


---

### isDestroyed {#isDestroyed}

#### \<instance> isDestroyed() {#instance-isdestroyed}


**说明:**

如果 Tween 具有 _ 流态 DESTROYED 状态, 返回 `true`, 否则返回 `false` 。


**返回值:** boolean - 如果Tween的状态是零下半身,则`true`,否则则`false`.


> 源码：[src/tweens/tween/BaseTween.js#L838](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L838)  
引入版本：3.60.0


---

### isFinished {#isFinished}

#### \<instance> isFinished() {#instance-isfinished}


**说明:**

返回值 `true` 如果此图文的状态为 _ 当前_ 已完成, 否则 `false`.


**返回值:** boolean - `true` 如果此图文的状态为 _ 当前_ 已完成, 否则 `false`.


> 源码：[src/tweens/tween/BaseTween.js#L825](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L825)  
引入版本：3.60.0


---

### isLoopDelayed {#isLoopDelayed}

#### \<instance> isLoopDelayed() {#instance-isloopdelayed}


**说明:**

如果 Tween 具有 _ current_ state of LOOP_DELAY 状态, 返回 `true`, 否则返回 `false` 。


**返回值:** boolean - `true` 如果此图文有 _ 当前_ 状态 LOOP_ DELAY, 否则 `false`.


> 源码：[src/tweens/tween/BaseTween.js#L760](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L760)  
引入版本：3.60.0


---

### isPaused {#isPaused}

#### \<instance> isPaused() {#instance-ispaused}


**说明:**

检查当前是否暂停 Tween 。

这和直接检查`BaseTween.paused`财产相同.


**返回值:** boolean - 如果Tween被暂停的话,`true`,否则`false`.


> 源码：[src/tweens/tween/BaseTween.js#L314](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L314)  
引入版本：3.60.0


---

### isPending {#isPending}

#### \<instance> isPending() {#instance-ispending}


**说明:**

如果此 Tween 具有 _ current_ state of PENDING 状态, 则返回 `true`, 否则返回 `false` 。


**返回值:** boolean - `true` 如果此图文有 _ 当前_ 状态 PENDING, 否则 `false`.


> 源码：[src/tweens/tween/BaseTween.js#L734](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L734)  
引入版本：3.60.0


---

### isPendingRemove {#isPendingRemove}

#### \<instance> isPendingRemove() {#instance-ispendingremove}


**说明:**

返回值 `true` 如果此图文有 _xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx `false`.


**返回值:** boolean - `true` 如果此图文有 _xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx `false`.


> 源码：[src/tweens/tween/BaseTween.js#L799](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L799)  
引入版本：3.60.0


---

### isPlaying {#isPlaying}

#### \<instance> isPlaying() {#instance-isplaying}


**说明:**

检查此 Tween 是否正在播放 。

如果这个 Tween 被暂停, 或者不活动, 这个方法会返回假 。


**返回值:** boolean - 如果Tween在演奏,就用`true`,否则用`false`.


> 源码：[src/tweens/tween/BaseTween.js#L299](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L299)  
引入版本：3.60.0


---

### isRemoved {#isRemoved}

#### \<instance> isRemoved() {#instance-isremoved}


**说明:**

如果 Tween 具有 _ 流态 REMOVED , 则返回 `true`, 否则返回 `false` 。


**返回值:** boolean - `true` 如果此 Tween 具有 _ 当前_ 状态 , 否则 `false`.


> 源码：[src/tweens/tween/BaseTween.js#L812](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L812)  
引入版本：3.60.0


---

### isStartDelayed {#isStartDelayed}

#### \<instance> isStartDelayed() {#instance-isstartdelayed}


**说明:**

如果 Tween 具有 _ Express_ DELAY 状态, 返回 `true`, 否则返回 `false` 。


**返回值:** boolean - 如果这个Tween有_当前_START_DELAY状态,则`true`,否则`false`.


> 源码：[src/tweens/tween/BaseTween.js#L786](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L786)  
引入版本：3.60.0


---

### makeActive {#makeActive}

#### \<instance> makeActive() {#instance-makeactive}


**说明:**

内部方法使这个Tween在TweenManager内活动,并发布onActive事件和回调.


**Fires:** [Phaser.Tweens.Events#event:TWEEN_ACTIVE](/api/event/tweens-events#tween_active)


> 源码：[src/tweens/tween/BaseTween.js#L375](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L375)  
引入版本：3.60.0


---

### onCompleteHandler {#onCompleteHandler}

#### \<instance> onCompleteHandler() {#instance-oncompletehandler}


**说明:**

处理这个Twen完成和释放onComplete事件和回调的内部方法.


> 源码：[src/tweens/tween/BaseTween.js#L390](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L390)  
引入版本：3.60.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

立即暂停调制。 使用 `resume` 继续播放 。

您也可以切换 `Tween.paused`布尔属性, 但这样做不会触发 PAUSE 事件 。


**返回值:** [Phaser.Tweens.BaseTween](/api/class/tweens-basetween) - 此特云证.


**Fires:** [Phaser.Tweens.Events#event:TWEEN_PAUSE](/api/event/tweens-events#tween_pause)


> 源码：[src/tweens/tween/BaseTween.js#L329](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L329)  
引入版本：3.60.0


---

### remove {#remove}

#### \<instance> remove() {#instance-remove}


**说明:**

立即从 Tween 管理器及其所有内部阵列中移除此 Tween。 然后将 tween 状态设置为 `REMOVED` 。

使用此方法后, 您应该处理您对这个 tween 的引用, 以释放它与记忆。 如果您不再需要, 请在它上拨打 `Tween.destroy()` 。


**返回值:** [Phaser.Tweens.BaseTween](/api/class/tweens-basetween) - 此特云证.


> 源码：[src/tweens/tween/BaseTween.js#L466](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L466)  
引入版本：3.60.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

恢复播放先前暂停的特温.

您也可以切换 `Tween.paused`布尔属性, 但这样做不会触发 ResUME 事件 。


**返回值:** [Phaser.Tweens.BaseTween](/api/class/tweens-basetween) - 此特云证.


**Fires:** [Phaser.Tweens.Events#event:TWEEN_RESUME](/api/event/tweens-events#tween_resume)


> 源码：[src/tweens/tween/BaseTween.js#L352](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L352)  
引入版本：3.60.0


---

### setActiveState {#setActiveState}

#### \<instance> setActiveState() {#instance-setactivestate}


**说明:**

设定此 Tween 状态为 实际操作 。


> 源码：[src/tweens/tween/BaseTween.js#L640](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L640)  
引入版本：3.60.0


---

### setCallback {#setCallback}

#### \<instance> setCallback(type, callback, [params]) {#instance-setcallbacktype-callback-params}


**说明:**

设置一个基于事件的回调, 用于在播放时引用 。

调用这种方法将取代先前为给定类型设定的回调, 如果存在的话 。

现有类型如下:

`onActive` - 当 Tween 创建之初, 它会移动到“ 活动” 状态, 当添加到 Tween 管理器中时。 “ 主动” 并不意味着“ 玩” 。 `onStart` 当Tween在延迟状态或暂停状态后开始播放时。这将会同时发生。 `onActive` 如果这个圈子没有拖延,也没有停顿。 `onLoop` - 当一个Tween循环,如果它被设定这样做。这发生在_after_ the `loopDelay` 过期, 如果设置 。 `onComplete` 当Tween完全重播时, 如果Tween被设定为无限重播, 则永远不要引用 。 `onStop` - 只有在 `Tween.stop` 方法叫做 。 `onPause` - 只有在 `Tween.pause` 方法。如果 Tween 管理器被暂停,则不引用。 `onResume` - 只有在 `Tween.resume` 方法。如果 Tween 管理器恢复使用,则不引用。

以下类型也可用,并被引用在`TweenData`级别上——即每个对象,每个财产,被加成  .

`onYoyo` 当TweenData开始一个优等生。 `hold` 如果设置, 延迟过期 。 `onRepeat` 当TweenData重复播放时。这种情况发生在_after_ the `repeatDelay` 过期, 如果设置 。 `onUpdate` - 当TweenData在播放时更新源目标上的属性时。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 类型 | [Phaser.Types.Tweens.TweenCallbackTypes](/api/typedef/types-tweens#tweencallbacktypes) | 否 | 回调设置的类型。 其中之一 : `onActive`, `onComplete`, `onLoop`, `onPause`, `onRepeat`, `onResume`, `onStart`, `onStop`, `onUpdate` 或 或 时 间 `onYoyo`. |
| callback | function | 否 | 你的回电会被调用 |
| params | array | 是 | 传递到调用时的参数。 如果您不想定义任何一个, 但确实希望设定范围, 请通过一个空的数组 。 |


**返回值:** [Phaser.Tweens.BaseTween](/api/class/tweens-basetween) - 此特云证.


> 源码：[src/tweens/tween/BaseTween.js#L587](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L587)  
引入版本：3.60.0


---

### setCompleteDelayState {#setCompleteDelayState}

#### \<instance> setCompleteDelayState() {#instance-setcompletedelaystate}


**说明:**

设置此 Tween 状态为 CompleETE_DELAY 。


> 源码：[src/tweens/tween/BaseTween.js#L664](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L664)  
引入版本：3.60.0


---

### setDestroyedState {#setDestroyedState}

#### \<instance> setDestroyedState() {#instance-setdestroyedstate}


**说明:**

设置此 Tween 状态为 DESTROYED 。


> 源码：[src/tweens/tween/BaseTween.js#L723](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L723)  
引入版本：3.60.0


---

### setFinishedState {#setFinishedState}

#### \<instance> setFinishedState() {#instance-setfinishedstate}


**说明:**

设定此 Tween 状态完成 。


> 源码：[src/tweens/tween/BaseTween.js#L712](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L712)  
引入版本：3.60.0


---

### setLoopDelayState {#setLoopDelayState}

#### \<instance> setLoopDelayState() {#instance-setloopdelaystate}


**说明:**

将此 Tween 状态设定为 LOOP_ DELAY 。


> 源码：[src/tweens/tween/BaseTween.js#L653](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L653)  
引入版本：3.60.0


---

### setPendingRemoveState {#setPendingRemoveState}

#### \<instance> setPendingRemoveState() {#instance-setpendingremovestate}


**说明:**

设置此图文状态为 PENDING_REMOVE 。


> 源码：[src/tweens/tween/BaseTween.js#L690](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L690)  
引入版本：3.60.0


---

### setPendingState {#setPendingState}

#### \<instance> setPendingState() {#instance-setpendingstate}


**说明:**

设置此 Tween 状态为 PENDING 。


> 源码：[src/tweens/tween/BaseTween.js#L629](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L629)  
引入版本：3.60.0


---

### setRemovedState {#setRemovedState}

#### \<instance> setRemovedState() {#instance-setremovedstate}


**说明:**

设置此 Tween 状态为 REMOVED 。


> 源码：[src/tweens/tween/BaseTween.js#L701](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L701)  
引入版本：3.60.0


---

### setStartDelayState {#setStartDelayState}

#### \<instance> setStartDelayState() {#instance-setstartdelaystate}


**说明:**

设置此 Tween 状态为START_DELAY 。


> 源码：[src/tweens/tween/BaseTween.js#L675](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L675)  
引入版本：3.60.0


---

### setTimeScale {#setTimeScale}

#### \<instance> setTimeScale(value) {#instance-settimescalevalue}


**说明:**

设置适用于 Tween 的时间尺度的值。 1 的值在实时运行。 0. 5 的值在运行中慢了 50% , 以此类推 。

计算  的总持续时间时不使用该值,它只是运行时三角洲调整.

此值乘以 `TweenManager.timeScale` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 要设置的时间尺度值 。 |


**返回值:** [Phaser.Tweens.BaseTween](/api/class/tweens-basetween) - 此特云证.


> 源码：[src/tweens/tween/BaseTween.js#L263](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L263)  
引入版本：3.60.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

立即阻止特温号 不管它处于什么阶段

如果不是Tween链的一部分,则Tween管理器也标注要删除。

如果`onStop`调用已被定义,它会自动引用它。

Tween将在下一个游戏框中被移除,但应该从此被视为"毁灭".

通常情况下,你不能玩已被停止的调图。如果您只是想暂停调图,而不是摧毁调图,那么请拨打调图。 `pause` 方法与使用 `resume` 。如果想要重新启动 Tween,请使用 `restart` 或 或 时 间 `seek` 方法, 方法, 方法, 方法, 方法, 方法, 方法, 方法, 方法。


**返回值:** [Phaser.Tweens.BaseTween](/api/class/tweens-basetween) - 此特云证.


**Fires:** [Phaser.Tweens.Events#event:TWEEN_STOP](/api/event/tweens-events#tween_stop)


> 源码：[src/tweens/tween/BaseTween.js#L488](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L488)  
引入版本：3.60.0


---

### updateCompleteDelay {#updateCompleteDelay}

#### \<instance> updateCompleteDelay(delta) {#instance-updatecompletedelaydelta}


**说明:**

处理完整延迟倒计时器处理和相关活动发送的内部方法。由 `Tween.update`自动调用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/tweens/tween/BaseTween.js#L568](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L568)  
引入版本：3.60.0


---

### updateLoopCountdown {#updateLoopCountdown}

#### \<instance> updateLoopCountdown(delta) {#instance-updateloopcountdowndelta}


**说明:**

处理循环延迟倒计时器和发送相关活动的内部方法。由 `Tween.update`自动调用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/tweens/tween/BaseTween.js#L519](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L519)  
引入版本：3.60.0


---

### updateStartCountdown {#updateStartCountdown}

#### \<instance> updateStartCountdown(delta) {#instance-updatestartcountdowndelta}


**说明:**

处理启动延迟倒计时器和相关活动发送的内部方法。由 `Tween.update`自动调用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/tweens/tween/BaseTween.js#L540](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTween.js#L540)  
引入版本：3.60.0


---

---
