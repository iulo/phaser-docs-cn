# BaseTweenData {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tweens-basetweendata)

BaseTweenData 是TweenData 和 TweenFrameData 类从中扩展的类。您通常不应该直接即时化这个类,而是应该使用它来组成您自己的 tween 数据类,如果您需要的话。

在Phaser 3.60之前,TweenData只是一种物体,但被重新构型到一个类,使它对自己状态和更新负责.

**构造函数**

`new BaseTweenData(tween, targetIndex, delay, duration, yoyo, hold, repeat, repeatDelay, flipX, flipY)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 这个TweenData实例属于这个. |
| targetIndex | number | 否 | Tween目标阵列内的目标指数. |
| delay | function | 否 | 函数返回 tween 开始前以毫秒计的时间 。 |
| duration | number | 否 | 千分之长的曲折时间. |
| yoyo | boolean | 否 | 确定在持有到期后, twin是否应该返回其起始值 。 |
| hold | number | 否 | 以毫秒计的时间, 如果 Yyo 设定为真实, 则 tween 将暂停重复或返回到它的起始值 。 |
| repeat | number | 否 | 重复的曲调次数。 曲调将永远运行一次, 故 1 的重播值将播放两次 。 |
| repeatDelay | number | 否 | 重复前的毫秒时间将开始 。 |
| flipX | boolean | 否 | 黄  还是重复时,应该叫toggleFlipX? |
| flipY | boolean | 否 | 黄  还是重复时,应该叫toggleFlipY? |

---


**作用域**: static

> 源码：[src/tweens/tween/BaseTweenData.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L11)  
引入版本：3.60.0

## 公开成员 {#public-members}

### delay {#delay}

#### delay: number {#delay-number}


**说明:**

时间,以毫秒,在这双曲子开始演奏之前。

此值由 `getDelay` 函数生成 。


> 源码：[src/tweens/tween/BaseTweenData.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L81)  
引入版本：3.60.0


---

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

千秒的 tween 持续时间, 不包括 Yyo 或 重复 所需的任何时间。 tween 永远不能有 0 的持续时间, 因此如果值不正确小于或等于 0, 则该持续时间将设定为 0.01 。


> 源码：[src/tweens/tween/BaseTweenData.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L60)  
引入版本：3.60.0


---

### elapsed {#elapsed}

#### elapsed: number {#elapsed-number}


**说明:**

自TweenData生效以来,时间以毫秒计。


> 源码：[src/tweens/tween/BaseTweenData.js#L184](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L184)  
引入版本：3.60.0


---

### flipX {#flipX}

#### flipX: boolean {#flipx-boolean}


**说明:**

如果出现 `true` 特温会打电话来 `toggleFlipX` 。只有当目标有与这个名称相匹配的功能时, 才会被调用, 就像大多数一样。 Phaser 游戏对象有。


> 源码：[src/tweens/tween/BaseTweenData.js#L153](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L153)  
引入版本：3.60.0


---

### flipY {#flipY}

#### flipY: boolean {#flipy-boolean}


**说明:**

如果出现 `true` 特温会打电话来 `toggleFlipY` 。只有当目标有与这个名称相匹配的功能时, 才会被调用, 就像大多数一样。 Phaser 游戏对象有。


> 源码：[src/tweens/tween/BaseTweenData.js#L164](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L164)  
引入版本：3.60.0


---

### getDelay {#getDelay}

#### getDelay: function {#getdelay-function}


**说明:**

此函数返回用于 `TweenData.delay` 的值 。


> 源码：[src/tweens/tween/BaseTweenData.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L92)  
引入版本：3.60.0


---

### hold {#hold}

#### hold: number {#hold-number}


**说明:**

时间,以毫秒,在这节之前, 开始一个yoyo重复。


> 源码：[src/tweens/tween/BaseTweenData.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L111)  
引入版本：3.60.0


---

### isCountdown {#isCountdown}

#### isCountdown: boolean {#iscountdown-boolean}


**说明:**

这是Tween Data吗? 目前等待倒计时, 还是没有?


> 源码：[src/tweens/tween/BaseTweenData.js#L203](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L203)  
引入版本：3.60.0


---

### progress {#progress}

#### progress: number {#progress-number}


**说明:**

0到1之间的值, 持有此 TweenData 的进度 。


> 源码：[src/tweens/tween/BaseTweenData.js#L175](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L175)  
引入版本：3.60.0


---

### repeat {#repeat}

#### repeat: number {#repeat-number}


**说明:**

此  复次之数.

会不管这个值,总是运行一次,所以"1"的重复值会播放  两次:一,即原玩通过,然后重复一次(1).

如果这个值被设定为 - 1 此 tween 将永远重复 。


> 源码：[src/tweens/tween/BaseTweenData.js#L120](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L120)  
引入版本：3.60.0


---

### repeatCounter {#repeatCounter}

#### repeatCounter: number {#repeatcounter-number}


**说明:**

有多少次重复还剩跑步?


> 源码：[src/tweens/tween/BaseTweenData.js#L144](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L144)  
引入版本：3.60.0


---

### repeatDelay {#repeatDelay}

#### repeatDelay: number {#repeatdelay-number}


**说明:**

重复开始前的时间,以毫秒计。


> 源码：[src/tweens/tween/BaseTweenData.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L135)  
引入版本：3.60.0


---

### state {#state}

#### state: [Phaser.Tweens.StateType](/api/typedef/tweens#statetype) {#state-phasertweensstatetype}


**说明:**

此  丹田之州.


> 源码：[src/tweens/tween/BaseTweenData.js#L194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L194)  
引入版本：3.60.0


---

### targetIndex {#targetIndex}

#### targetIndex: number {#targetindex-number}


**说明:**

Tween `targets`阵列内的目标索引.


> 源码：[src/tweens/tween/BaseTweenData.js#L51](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L51)  
引入版本：3.60.0


---

### totalDuration {#totalDuration}

#### totalDuration: number {#totalduration-number}


**说明:**

计算的总持续时间, 以毫秒计, 计时时间、 重复、 延迟和 Yoyos 。


> 源码：[src/tweens/tween/BaseTweenData.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L71)  
引入版本：3.60.0


---

### tween {#tween}

#### tween: [Phaser.Tweens.Tween](/api/class/tweens-tween) {#tween-phasertweenstween}


**说明:**

提到这个TweenData实例属于的Tween.


> 源码：[src/tweens/tween/BaseTweenData.js#L42](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L42)  
引入版本：3.60.0


---

### yoyo {#yoyo}

#### yoyo: boolean {#yoyo-boolean}


**说明:**

Tween 是否在到达终点和任何可能设定的 `hold` 值后, 能够恢复到起始值 ?


> 源码：[src/tweens/tween/BaseTweenData.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L101)  
引入版本：3.60.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

立即摧毁这个TweenData, 取消它的所有引用。


> 源码：[src/tweens/tween/BaseTweenData.js#L646](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L646)  
引入版本：3.60.0


---

### getTarget {#getTarget}

#### \<instance> getTarget() {#instance-gettarget}


**说明:**

返回属于TweenData的目标对象的引用。


**返回值:** object - 目标对象。 可以是任何 JavaScript 对象, 但通常是游戏对象 。


> 源码：[src/tweens/tween/BaseTweenData.js#L213](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L213)  
引入版本：3.60.0


---

### isComplete {#isComplete}

#### \<instance> isComplete() {#instance-iscomplete}


**说明:**

如果 TweenData 具有 CompleETE 的 _ current_状态, 返回 `true` , 否则返回 `false` 。


**返回值:** boolean - `true` 如果此 TweenData 具有 CompleTE 的 _ 流_ 状态, 否则 `false`.


> 源码：[src/tweens/tween/BaseTweenData.js#L428](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L428)  
引入版本：3.60.0


---

### isCreated {#isCreated}

#### \<instance> isCreated() {#instance-iscreated}


**说明:**

如果 TweenData 具有 _ currated_状态, 返回 `true`, 否则返回 `false` 。


**返回值:** boolean - `true` 如果此 TweenData 具有 _xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx `false`.


> 源码：[src/tweens/tween/BaseTweenData.js#L337](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L337)  
引入版本：3.60.0


---

### isDelayed {#isDelayed}

#### \<instance> isDelayed() {#instance-isdelayed}


**说明:**

如果此 TweenData 具有 DELAY 的 _ current_ 状态, 返回 `true` , 否则返回 `false` 。


**返回值:** boolean - `true` 如果此 TweenData 具有 _xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx `false`.


> 源码：[src/tweens/tween/BaseTweenData.js#L350](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L350)  
引入版本：3.60.0


---

### isHolding {#isHolding}

#### \<instance> isHolding() {#instance-isholding}


**说明:**

如果 TweenData 具有 _current_状态 HOLD_DELAY , 返回 `true` , 否则返回 `false` 。


**返回值:** boolean - `true` 如果此 TweenData 具有 _xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx `false`.


> 源码：[src/tweens/tween/BaseTweenData.js#L402](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L402)  
引入版本：3.60.0


---

### isPendingRender {#isPendingRender}

#### \<instance> isPendingRender() {#instance-ispendingrender}


**说明:**

返回值 `true` 如果此 TweenData 具有 _xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx `false`.


**返回值:** boolean - `true` 如果此 TweenData 具有 _xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx `false`.


> 源码：[src/tweens/tween/BaseTweenData.js#L363](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L363)  
引入版本：3.60.0


---

### isPlayingBackward {#isPlayingBackward}

#### \<instance> isPlayingBackward() {#instance-isplayingbackward}


**说明:**

如果此 TweenData 具有 _当前_ 状态的 PLAYNLE_ BACKWARD , 则返回 `true`, 否则返回 `false` 。


**返回值:** boolean - `true` 如果此 TweenData 具有 _xe_状态 播放_BACKWARD, 否则 `false`.


> 源码：[src/tweens/tween/BaseTweenData.js#L389](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L389)  
引入版本：3.60.0


---

### isPlayingForward {#isPlayingForward}

#### \<instance> isPlayingForward() {#instance-isplayingforward}


**说明:**

如果此 TweenData 具有 _xeur_ 状态的 PLAYLING_FORWARD 返回 `true`, 否则则返回 `false` 。


**返回值:** boolean - `true` 如果此 TweenData 具有 _xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx `false`.


> 源码：[src/tweens/tween/BaseTweenData.js#L376](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L376)  
引入版本：3.60.0


---

### isRepeating {#isRepeating}

#### \<instance> isRepeating() {#instance-isrepeating}


**说明:**

如果此 TweenData 具有 _xein_状态的 REPEAT_ DELAY 返回 `true`, 否则则返回 `false` 。


**返回值:** boolean - `true` 如果此 TweenData 具有 _xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx `false`.


> 源码：[src/tweens/tween/BaseTweenData.js#L415](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L415)  
引入版本：3.60.0


---

### onRepeat {#onRepeat}

#### \<instance> onRepeat(diff, setStart, isYoyo) {#instance-onrepeatdiff-setstart-isyoyo}


**说明:**

处理重复或Yoyo' 处理这个TweenData的内部方法。

由`setStateFromStart`和`setStateFromEnd`自动调用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| diff | number | 否 | 需要计入已过期和进度值的任何额外时间。 |
| setStart | boolean | 否 | 设置 TweenData 起始值吗 ? |
| isYoyo | boolean | 否 | 这是叫Yoyo检查吗? |


**Fires:** [Phaser.Tweens.Events#event:TWEEN_REPEAT](/api/event/tweens-events#tween_repeat), [Phaser.Tweens.Events#event:TWEEN_YOYO](/api/event/tweens-events#tween_yoyo)


> 源码：[src/tweens/tween/BaseTweenData.js#L563](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L563)  
引入版本：3.60.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

完全重置此 Tween 数据的内部方法, 包括进度和过期值 。

由父 Tween 自动调用。 不应直接调用 。


> 源码：[src/tweens/tween/BaseTweenData.js#L490](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L490)  
引入版本：3.60.0


---

### setCompleteState {#setCompleteState}

#### \<instance> setCompleteState() {#instance-setcompletestate}


**说明:**

将这个 TweenData 状态设置为 CompLETE 。


> 源码：[src/tweens/tween/BaseTweenData.js#L325](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L325)  
引入版本：3.60.0


---

### setCreatedState {#setCreatedState}

#### \<instance> setCreatedState() {#instance-setcreatedstate}


**说明:**

将此 TweenData 状态设置为 CREATED 。


> 源码：[src/tweens/tween/BaseTweenData.js#L241](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L241)  
引入版本：3.60.0


---

### setDelayState {#setDelayState}

#### \<instance> setDelayState() {#instance-setdelaystate}


**说明:**

将这个 TweenData 状态设置为 DELAY 。


> 源码：[src/tweens/tween/BaseTweenData.js#L253](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L253)  
引入版本：3.60.0


---

### setHoldState {#setHoldState}

#### \<instance> setHoldState() {#instance-setholdstate}


**说明:**

将此 TweenData 状态设置为 HOLD_DELAY 。


> 源码：[src/tweens/tween/BaseTweenData.js#L301](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L301)  
引入版本：3.60.0


---

### setPendingRenderState {#setPendingRenderState}

#### \<instance> setPendingRenderState() {#instance-setpendingrenderstate}


**说明:**

将此 TweenData 状态设定为 PENDING_RENDER 。


> 源码：[src/tweens/tween/BaseTweenData.js#L265](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L265)  
引入版本：3.60.0


---

### setPlayingBackwardState {#setPlayingBackwardState}

#### \<instance> setPlayingBackwardState() {#instance-setplayingbackwardstate}


**说明:**

设置此 TweenData 状态为播放_ BackWard 。


> 源码：[src/tweens/tween/BaseTweenData.js#L289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L289)  
引入版本：3.60.0


---

### setPlayingForwardState {#setPlayingForwardState}

#### \<instance> setPlayingForwardState() {#instance-setplayingforwardstate}


**说明:**

设置此 TweenData 状态为 Playing_FORWARD 。


> 源码：[src/tweens/tween/BaseTweenData.js#L277](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L277)  
引入版本：3.60.0


---

### setRepeatState {#setRepeatState}

#### \<instance> setRepeatState() {#instance-setrepeatstate}


**说明:**

将此 TweenData 状态设定为 REPEAT_ DELAY 。


> 源码：[src/tweens/tween/BaseTweenData.js#L313](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L313)  
引入版本：3.60.0


---

### setStateFromEnd {#setStateFromEnd}

#### \<instance> setStateFromEnd(diff) {#instance-setstatefromenddiff}


**说明:**

内部方法作为回放过程的一部分,用于检查这个TweenData是否应该yoyo,重复,或者已经完成.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| diff | number | 否 | 需要计入已过期和进度值的任何额外时间。 |


**Fires:** [Phaser.Tweens.Events#event:TWEEN_REPEAT](/api/event/tweens-events#tween_repeat), [Phaser.Tweens.Events#event:TWEEN_YOYO](/api/event/tweens-events#tween_yoyo)


> 源码：[src/tweens/tween/BaseTweenData.js#L441](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L441)  
引入版本：3.60.0


---

### setStateFromStart {#setStateFromStart}

#### \<instance> setStateFromStart(diff) {#instance-setstatefromstartdiff}


**说明:**

内部方法作为回放过程的一部分,用于检查此TweenData是否应该重复或已完成.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| diff | number | 否 | 需要计入已过期和进度值的任何额外时间。 |


**Fires:** [Phaser.Tweens.Events#event:TWEEN_REPEAT](/api/event/tweens-events#tween_repeat)


> 源码：[src/tweens/tween/BaseTweenData.js#L468](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L468)  
引入版本：3.60.0


---

### setTargetValue {#setTargetValue}

#### \<instance> setTargetValue([value]) {#instance-settargetvaluevalue}


**说明:**

设定此 TweenData 的目标对象属性为给定值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 是 | 设定目标值。 如果不给出, 则设定为最后一个 `current` 值 。 |


> 源码：[src/tweens/tween/BaseTweenData.js#L226](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/BaseTweenData.js#L226)  
引入版本：3.60.0


---

---
