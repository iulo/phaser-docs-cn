# TimerEvent {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/time-timerevent)

定时器事件代表延迟函数调用。 它由 Scene 的 [Clock](https://phaser.io/oss/docs/api-documentation/class/Clock.md) 管理, 并在设定的时间量过后调用它的职能。 定时器事件可以可选择重复, 即完成前多次调用它的职能, 或者无限循环 。

由于它由时钟管理,一个时钟事件基于游戏时间,会受到其时钟的时间缩放倍率的影响,如果其时钟暂停,则会暂停.

**构造函数**

`new TimerEvent(config)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Time.TimerEventConfig](/api/typedef/types-time#timereventconfig) | 否 | 计时器事件的配置,包括它的延迟和回调. |

---


**作用域**: static

> 源码：[src/time/TimerEvent.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L10)  
引入版本：3.0.0

## 公开成员 {#public-members}

### args {#args}

#### args: array {#args-array}


**说明:**

将补充论据传递到回调中.


> 源码：[src/time/TimerEvent.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L90)  
引入版本：3.0.0


---

### callback {#callback}

#### callback: function {#callback-function}


**说明:**

计时器事件发生时将调用回调 。


> 源码：[src/time/TimerEvent.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L72)  
引入版本：3.0.0


---

### callbackScope {#callbackScope}

#### callbackScope: object {#callbackscope-object}


**说明:**

调用范围 。


> 源码：[src/time/TimerEvent.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L81)  
引入版本：3.0.0


---

### delay {#delay}

#### delay: number {#delay-number}


**说明:**

时间节点的延迟


> 源码：[src/time/TimerEvent.js#L29](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L29)  
引入版本：3.0.0


---

### elapsed {#elapsed}

#### elapsed: number {#elapsed-number}


**说明:**

时间事件开始后 以毫秒的速度计算

此值是时钟事件本地值, 相对于它的时钟值。 因此, 它受到时钟的时间缩放倍率和暂停状态, 时钟事件初始的 [#startAt](#startAt) 属性, 以及时钟事件 [#timeScale](#timeScale) 和 [#paused](#paused) 状态的影响 。


> 源码：[src/time/TimerEvent.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L119)  
引入版本：3.0.0


---

### hasDispatched {#hasDispatched}

#### hasDispatched: boolean {#hasdispatched-boolean}


**说明:**

是否调用过定时器事件功能 。

当定时器事件起火时, 此属性会在调用回调函数之前设定为 `true`, 如果定时器事件重复, 则此属性将在之后立即重设。 此属性的价值不会直接影响定时器事件是否从时钟中移除, 但能够防止它发射 。


> 源码：[src/time/TimerEvent.js#L141](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L141)  
引入版本：3.0.0


---

### loop {#loop}

#### loop: boolean {#loop-boolean}


**说明:**

如果这个时光节循环,否则是虚假的,那么这个时间节循环是真实的.


> 源码：[src/time/TimerEvent.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L61)  
引入版本：3.0.0


---

### paused {#paused}

#### paused: boolean {#paused-boolean}


**说明:**

此定时器是否暂停 。


> 源码：[src/time/TimerEvent.js#L131](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L131)  
引入版本：3.0.0


---

### repeat {#repeat}

#### repeat: number {#repeat-number}


**说明:**

完成前, 此TimerEvent 将重复的总数 。


> 源码：[src/time/TimerEvent.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L40)  
引入版本：3.0.0


---

### repeatCount {#repeatCount}

#### repeatCount: number {#repeatcount-number}


**说明:**

如果重复, 此值包含当前要重复的倒计时数。 它从 [#repeat](#repeat) 的值开始, 每次时间事件起火时, 计数为 0 。


> 源码：[src/time/TimerEvent.js#L51](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L51)  
引入版本：3.0.0


---

### startAt {#startAt}

#### startAt: number {#startat-number}


**说明:**

进入时间以内开始计时器事件的时间数。 这样可以让长时间重复计时器事件在第一次重复时更早开火, 同时又不影响后续重复的持续时间 。


> 源码：[src/time/TimerEvent.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L109)  
引入版本：3.0.0


---

### timeScale {#timeScale}

#### timeScale: number {#timescale-number}


**说明:**

用于更新此计时器事件的时间缩放倍率因子。 大于1 的值会让事件更快点火, 而低于1 的值会延迟点火。 时间缩放倍率独立于时钟本身的时间缩放倍率, 并随时间缩放倍率的乘以。


> 源码：[src/time/TimerEvent.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L99)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁计时器事件中的所有对象引用,即它的召回,范围和参数.

通常,这种方法只在关闭时被时钟调用,因此它不会停止计时器事件,如果被人工调用,计时器事件仍然会被时钟更新,但当它开火时它不会做任何事情.


> 源码：[src/time/TimerEvent.js#L347](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L347)  
引入版本：3.0.0


---

### getElapsed {#getElapsed}

#### \<instance> getElapsed() {#instance-getelapsed}


**说明:**

返回当前时间事件重复的本地时间 。


**返回值:** number - 当地时间以毫秒计。


> 源码：[src/time/TimerEvent.js#L250](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L250)  
引入版本：3.0.0


---

### getElapsedSeconds {#getElapsedSeconds}

#### \<instance> getElapsedSeconds() {#instance-getelapsedseconds}


**说明:**

返回当前时间事件重复的本地时间( 秒) 。


**返回值:** number - 当地时间用秒。


> 源码：[src/time/TimerEvent.js#L263](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L263)  
引入版本：3.0.0


---

### getOverallProgress {#getOverallProgress}

#### \<instance> getOverallProgress() {#instance-getoverallprogress}


**说明:**

获得计时器的总体进度,计入重复。


**返回值:** number - 计时器事件总体进展0-1.


> 源码：[src/time/TimerEvent.js#L212](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L212)  
引入版本：3.0.0


---

### getOverallRemaining {#getOverallRemaining}

#### \<instance> getOverallRemaining() {#instance-getoverallremaining}


**说明:**

返回时间间隔,直到计时器事件最后一次重排。


**返回值:** number - 时间间隔( 毫秒) 。


> 源码：[src/time/TimerEvent.js#L302](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L302)  
引入版本：3.50.0


---

### getOverallRemainingSeconds {#getOverallRemainingSeconds}

#### \<instance> getOverallRemainingSeconds() {#instance-getoverallremainingseconds}


**说明:**

返回时间间隔, 直至计时器事件以秒计的最后一次重迭 。


**返回值:** number - 时间间隔以秒计.


> 源码：[src/time/TimerEvent.js#L315](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L315)  
引入版本：3.50.0


---

### getProgress {#getProgress}

#### \<instance> getProgress() {#instance-getprogress}


**说明:**

获得当前迭代的进展,而不是重复的因数。


**返回值:** number - 0至1之间的数字代表目前的进展。


> 源码：[src/time/TimerEvent.js#L199](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L199)  
引入版本：3.0.0


---

### getRemaining {#getRemaining}

#### \<instance> getRemaining() {#instance-getremaining}


**说明:**

返回时间间隔, 直至时间事件下次重现 。


**返回值:** number - 时间间隔( 毫秒) 。


> 源码：[src/time/TimerEvent.js#L276](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L276)  
引入版本：3.50.0


---

### getRemainingSeconds {#getRemainingSeconds}

#### \<instance> getRemainingSeconds() {#instance-getremainingseconds}


**说明:**

返回时间间隔, 直至时间事件在秒内下一次重复 。


**返回值:** number - 时间间隔以秒计.


> 源码：[src/time/TimerEvent.js#L289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L289)  
引入版本：3.50.0


---

### getRepeatCount {#getRepeatCount}

#### \<instance> getRepeatCount() {#instance-getrepeatcount}


**说明:**

返回此计时器事件在完成前重复的次数 。

这不应该与定时器事件在完成前会开火的次数混淆。 0 的返回值并不表示定时器事件已完成运行 - 它表明它不会在下次开火后重复。


**返回值:** number - 计时器事件将重复多少次.


> 源码：[src/time/TimerEvent.js#L235](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L235)  
引入版本：3.0.0


---

### remove {#remove}

#### \<instance> remove([dispatchCallback]) {#instance-removedispatchcallback}


**说明:**

迫使计时器事件立即到期,从而安排在下一个框架中删除。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| dispatchCallback | boolean | 是 | false | 如果 `true`,在删除前将调用计时器事件的功能. |


> 源码：[src/time/TimerEvent.js#L328](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L328)  
引入版本：3.0.0


---

### reset {#reset}

#### \<instance> reset(config) {#instance-resetconfig}


**说明:**

完全重新初始化时器事件,不管它目前的状况如何,都根据配置对象进行。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Time.TimerEventConfig](/api/typedef/types-time#timereventconfig) | 否 | 时事事件的新状态. |


**返回值:** [Phaser.Time.TimerEvent](/api/class/time-timerevent) - 此定时事件对象 。


> 源码：[src/time/TimerEvent.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/TimerEvent.js#L156)  
引入版本：3.0.0


---

---
