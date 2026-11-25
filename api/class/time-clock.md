# Clock {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/time-clock)

时钟是一个场景插件,用于管理时间和调度时间事件,用于其母场景.

您可以使用它来运行延迟后、 重复间隔或循环中的回调, 全部由 Scene 的时间而不是系统时钟来调节 。 这意味着 Clock 尊重 Scene 的 paulsing 、 时间缩放和自动关闭生命周期 。

透过场景中的`this.time`进入它。

```javascript
this.time.delayedCall(1000, this.onTimer, [], this);
```

时钟的`timeScale`属性允许您在游戏其他部分独立地加速或减慢属于它的所有时空事件.

**构造函数**

`new Clock(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 拥有这个时钟的场景. |

---


**作用域**: static

> 源码：[src/time/Clock.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Clock.js#L13)  
引入版本：3.0.0

## 公开成员 {#public-members}

### now {#now}

#### now: number {#now-number}


**说明:**

时钟的当前时间, 以毫秒计 。

如果外部访问,这相当于通常传递到Scene的`update`方法的`time`参数.


> 源码：[src/time/Clock.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Clock.js#L61)  
引入版本：3.0.0


---

### paused {#paused}

#### paused: boolean {#paused-boolean}


**说明:**

时钟是暂停(`true`)还是活动(`false`).

当暂停时,时钟不会更新其任何时事,从而冻结时间.


> 源码：[src/time/Clock.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Clock.js#L95)  
引入版本：3.0.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

拥有这个时钟的场景.


> 源码：[src/time/Clock.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Clock.js#L43)  
引入版本：3.0.0


---

### startTime {#startTime}

#### startTime: number {#starttime-number}


**说明:**

时钟(和景)开始的时间,以毫秒计.

与“E”类相比, `time` 参数传递到场景 `update` 方法。 。 方法。


> 源码：[src/time/Clock.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Clock.js#L72)  
引入版本：3.60.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

拥有此时钟的场景系统对象 。


> 源码：[src/time/Clock.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Clock.js#L52)  
引入版本：3.0.0


---

### timeScale {#timeScale}

#### timeScale: number {#timescale-number}


**说明:**

时钟时三角洲的尺度.

时间三角洲是两个连续帧之间的时间,它会影响这个时钟的时间速度以及使用它的任何东西,例如它的时钟事件。值高于1会增加时间速度,而值小于1会减少时间。值0会冻结时间,并且实际上相当于拖动时钟。


> 源码：[src/time/Clock.js#L83](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Clock.js#L83)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### addEvent {#addEvent}

#### \<instance> addEvent(config) {#instance-addeventconfig}


**说明:**

创建一个计时器事件,并在下一个帧的开头添加到此时钟中。

可以通过`TimerEventConfig`对象,从中创建新的`TimerEvent`,也可以通过`TimerEvent`实例.

如果通过一个实例, 请确定此实例以前没有使用过 。 如果它曾经进入“ 完成” 状态, 那么它将不再适合运行 。

另外,如果`TimerEvent`实例被_another_Clock(在另一个场景)使用,它也会被该时钟更新,所以在使用此特性时要小心.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Time.TimerEvent](/api/class/time-timerevent) \| [Phaser.Types.Time.TimerEventConfig](/api/typedef/types-time#timereventconfig) | 否 | 定时器事件配置, 或已有的定时器事件对象 。 |


**返回值:** [Phaser.Time.TimerEvent](/api/class/time-timerevent) - 时机事件,是创建的,还是传入的。


> 源码：[src/time/Clock.js#L180](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Clock.js#L180)  
引入版本：3.0.0


---

### clearPendingEvents {#clearPendingEvents}

#### \<instance> clearPendingEvents() {#instance-clearpendingevents}


**说明:**

清除和重现待定的计时器事件阵列。


**返回值:** [Phaser.Time.Clock](/api/class/time-clock) - - 这个钟表


> 源码：[src/time/Clock.js#L249](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Clock.js#L249)  
引入版本：3.0.0


---

### delayedCall {#delayedCall}

#### \<instance> delayedCall(delay, callback, [args], [callbackScope]) {#instance-delayedcalldelay-callback-args-callbackscope}


**说明:**

创建一个定时事件,并在帧初始添加到时钟中.

这是[#addEvent](#addEvent)的快捷键,可以缩短,并与GreenSock动画平台(GSAP)的语法兼容.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delay | number | 否 | 函数调用延迟, 以毫秒计 。 |
| callback | function | 否 | 延迟到期后调用功能 。 |
| args | Array.\<*> | 是 | 调用函数的参数 。 |
| callbackScope | * | 是 | 函数的调用范围( `this` 对象) 。 |


**返回值:** [Phaser.Time.TimerEvent](/api/class/time-timerevent) - 被创造的计时器事件。


> 源码：[src/time/Clock.js#L229](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Clock.js#L229)  
引入版本：3.0.0


---

### preUpdate {#preUpdate}

#### \<instance> preUpdate() {#instance-preupdate}


**说明:**

更新活动及待决的计时器事件数组。在帧开始时调用。


> 源码：[src/time/Clock.js#L311](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Clock.js#L311)  
引入版本：3.0.0


---

### removeAllEvents {#removeAllEvents}

#### \<instance> removeAllEvents() {#instance-removeallevents}


**说明:**

将所有活动的时间事件在帧开始时排出删除的日程。


**返回值:** [Phaser.Time.Clock](/api/class/time-clock) - - 这个钟表


> 源码：[src/time/Clock.js#L296](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Clock.js#L296)  
引入版本：3.0.0


---

### removeEvent {#removeEvent}

#### \<instance> removeEvent(events) {#instance-removeeventevents}


**说明:**

从此时钟中删除给定的定时器事件,或一系列定时器事件。

活动从所有内部清单中除名(活动、待定和删除),使活动得以重新使用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| events | [Phaser.Time.TimerEvent](/api/class/time-timerevent) \| Array.\<[Phaser.Time.TimerEvent](/api/class/time-timerevent)> | 否 | 要从此时钟中删除时钟, 需要时间事件, 或是一系列的时间事件 。 |


**返回值:** [Phaser.Time.Clock](/api/class/time-clock) - - 这个钟表


> 源码：[src/time/Clock.js#L264](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Clock.js#L264)  
引入版本：3.50.0


---

### update {#update}

#### \<instance> update(time, delta) {#instance-updatetime-delta}


**说明:**

更新时钟的内部时间及其所有的时间事件。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/time/Clock.js#L359](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Clock.js#L359)  
引入版本：3.0.0


---

---
