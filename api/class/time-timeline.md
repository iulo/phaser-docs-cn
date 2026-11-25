# Timeline {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/time-timeline)

A Timeline是未来特定时间安排事件发生的一种方式.

你可以把它看作是游戏的事件排序器,允许你在未来特定时间安排回调,事件和其他动作的运行.

一个时间线是一个场景级别系统,意思是您可以任意拥有尽可能多的时间线,每个时间线属于不同的场景,也可以同时运行多个时间线.

如果暂停了场景, 时间线也会暂停。 如果破坏场景, 时间线会自动被销毁。 然而, 您可以直接控制时间线, 拖动、 恢复和停止它 。

通过游戏对象工厂创建时间线实例 :

```js
const timeline = this.add.timeline();
```

时间线总是暂停。 你必须打电话给`play`,以便启动它。

您也可以在创建时在配置对象中通过,或者在其中的数组中通过:

```js
const timeline = this.add.timeline({
    at: 1000,
    run: () => {
        this.add.sprite(400, 300, 'logo');
    }
});

timeline.play();
```

在这个例子中,我们排列了几个不同的事件:

```js
const timeline = this.add.timeline([
    {
        at: 1000,
        run: () => { this.logo = this.add.sprite(400, 300, 'logo'); },
        sound: 'TitleMusic'
    },
    {
        at: 2500,
        tween: {
            targets: this.logo,
            y: 600,
            yoyo: true
        },
        sound: 'Explode'
    },
    {
        at: 8000,
        event: 'HURRY_PLAYER',
        target: this.background,
        set: {
            tint: 0xff0000
        }
    }
]);

timeline.play();
```

时间线也可以用重复方法循环:

```js
timeline.repeat().play();
```

您可通过配置对象获得很多选项。 请查看 [Phaser.Types.Time.TimelineEventConfig](/api/typedef/types-time#timelineeventconfig) 类型def 的更多细节 。

**构造函数**

`new Timeline(scene, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 拥有这个时光线的场景。 |
| config | [Phaser.Types.Time.TimelineEventConfig](/api/typedef/types-time#timelineeventconfig) \| Array.\<[Phaser.Types.Time.TimelineEventConfig](/api/typedef/types-time#timelineeventconfig)> | 是 | 此时间线事件或其中的数组的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/time/Timeline.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L14)  
引入版本：3.60.0

## 公开成员 {#public-members}

### complete {#complete}

#### complete: boolean {#complete-boolean}


**说明:**

时间线是否完整(`true`) 是否完整(`false`).

当所有活动都运行完毕时,时间线就被认为是完整的。

如果在完成后希望重设时线,可以使用`Timeline.reset`方法.

也可以使用`Timeline.stop`方法停止运行的时光线,在任何时间段,而不重设.


> 源码：[src/time/Timeline.js#L171](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L171)  
引入版本：3.60.0


---

### elapsed {#elapsed}

#### elapsed: number {#elapsed-number}


**说明:**

时间计数器

把这当作只读


> 源码：[src/time/Timeline.js#L126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L126)  
引入版本：3.60.0


---

### events {#events}

#### events: Array.\<[Phaser.Types.Time.TimelineEvent](/api/typedef/types-time#timelineevent)> {#events-arrayphasertypestimetimelineevent}


**说明:**

包含所有时间线事件的一系列 。


> 源码：[src/time/Timeline.js#L224](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L224)  
引入版本：3.60.0


---

### iteration {#iteration}

#### iteration: number {#iteration-number}


**说明:**

此时光网上循环的次数 。

如果启用循环, 此值会被递增到每个循环 。


> 源码：[src/time/Timeline.js#L213](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L213)  
引入版本：3.80.0


---

### loop {#loop}

#### loop: number {#loop-number}


**说明:**

这个时间线应该循环的次数 。

如果该值是 - 1 或任何负数,则此时间线将无限循环 。


> 源码：[src/time/Timeline.js#L202](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L202)  
引入版本：3.80.0


---

### paused {#paused}

#### paused: boolean {#paused-boolean}


**说明:**

时间线是暂停(`true`)还是活动(`false`).

暂停时, 时间线将不会运行任何动作 。

默认情况下,时刻线总是被暂停,应该通过调用`Timeline.play`方法开始.

您可以使用`Timeline.pause`和`Timeline.resume`方法来以可链路控制这个值.


> 源码：[src/time/Timeline.js#L153](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L153)  
引入版本：3.60.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

此时光网上所属景点 。


> 源码：[src/time/Timeline.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L108)  
引入版本：3.60.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

参考景区系统.


> 源码：[src/time/Timeline.js#L117](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L117)  
引入版本：3.60.0


---

### timeScale {#timeScale}

#### timeScale: number {#timescale-number}


**说明:**

时光网上"三角洲"的时标.

高于1的值会提高时间速度,而小于1的值会降低时间速度。0的值会冻结时间,并且实际上相当于延时线。

这不影响时光网上创建的任何Tweens的三角洲时标。 如果您想要匹配, 您必须设置每个Tween 或 Tween 管理器的 `timeScale` 。


> 源码：[src/time/Timeline.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L137)  
引入版本：3.85.0


---

### totalComplete {#totalComplete}

#### totalComplete: number {#totalcomplete-number}


**说明:**

已办活动总数.

如果重新启动时间线, 此值会被重置为零 。

把这当作只读


> 源码：[src/time/Timeline.js#L189](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L189)  
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

### add {#add}

#### \<instance> add(config) {#instance-addconfig}


**说明:**

将一个或多个事件添加到此时间线。

您可以在一个单一的配置对象中通过,或者通过其中的数组:

```js
const timeline = this.add.timeline({
    at: 1000,
    run: () => {
        this.add.sprite(400, 300, 'logo');
    }
});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Time.TimelineEventConfig](/api/typedef/types-time#timelineeventconfig) \| Array.\<[Phaser.Types.Time.TimelineEventConfig](/api/typedef/types-time#timelineeventconfig)> | 否 | 此时间线事件或其中的数组的配置对象 。 |


**返回值:** [Phaser.Time.Timeline](/api/class/time-timeline) - 此时法例.


> 源码：[src/time/Timeline.js#L623](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L623)  
引入版本：3.60.0


---

### clear {#clear}

#### \<instance> clear() {#instance-clear}


**说明:**

删除此时间线上的所有事件, 将已过期的时间重排为零, 并暂停时间线 。

目前因本时光线而运行的任何Tweens都会被停止.


**返回值:** [Phaser.Time.Timeline](/api/class/time-timeline) - 此时法例.


> 源码：[src/time/Timeline.js#L706](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L706)  
引入版本：3.60.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这个时光线。

这将删除时间线上的所有事件,并阻止其处理.

目前因本时光线而运行的任何Tweens都会被停止.

当场景关闭时,这种方法会自动称为"时空",但如果需要提前破坏时,也可以直接使用.


**Overrides:** Phaser.Events.EventEmitter#销毁


> 源码：[src/time/Timeline.js#L779](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L779)  
引入版本：3.60.0


---

### getProgress {#getProgress}

#### \<instance> getProgress() {#instance-getprogress}


**说明:**

返回一个0至1之间的数字,代表这个时间线的进展。

0值表示时间线刚刚开始,0.5表示半途而废,1表示完整.

如果时光网上没有事件,或者所有事件都被删除,这个会返回`NaN`.

如果暂停时间线, 这将返回暂停时的进度值 。

注意返回的值是基于已完成的事件数量,而不是事件"期限"(因为时间线对此并不知情).


**返回值:** number - 0到1之间的数字代表了这个时间线的进展.


> 源码：[src/time/Timeline.js#L754](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L754)  
引入版本：3.60.0


---

### isPlaying {#isPlaying}

#### \<instance> isPlaying() {#instance-isplaying}


**说明:**

如果当前此时间线正在播放, 返回 `true` 。

时间线如果没有暂停和完成, 将会播放 。


**返回值:** boolean - 如果这个时光线在播放,则使用`true`,否则使用`false`.


> 源码：[src/time/Timeline.js#L739](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L739)  
引入版本：3.60.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

暂停此时间线 。

为了恢复它,请拨打`Timeline.resume`方法或将`Timeline.paused`属性设置为`false`.

如果在处理当前游戏步骤时暂停时间线,则会继续该步骤期间将要运行的所有事件,并从下一个游戏步骤暂停.

请注意,如果在调用这种方法之前已经启动了任何Tweens,则不会****被暂停。


**返回值:** [Phaser.Time.Timeline](/api/class/time-timeline) - 此时法例.


> 源码：[src/time/Timeline.js#L456](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L456)  
引入版本：3.60.0


---

### play {#play}

#### \<instance> play([fromStart]) {#instance-playfromstart}


**说明:**

启动此时间线运行 。

如果时光线已经运行,而`fromStart`参数是`true`,那么称这种方法会将时光线事件重新设定为不完整.

如果您想要恢复暂停的时线,请使用`Timeline.resume`方法。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| fromStart | boolean | 是 | true | 播放前将这个时间线重置为开始 。 |


**返回值:** [Phaser.Time.Timeline](/api/class/time-timeline) - 此时法例.


> 源码：[src/time/Timeline.js#L425](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L425)  
引入版本：3.60.0


---

### preUpdate {#preUpdate}

#### \<instance> preUpdate(time, delta) {#instance-preupdatetime-delta}


**说明:**

如果该时间线没有暂停, 则更新已过期的时间计数器 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/time/Timeline.js#L245](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L245)  
引入版本：3.60.0


---

### repeat {#repeat}

#### \<instance> repeat([amount]) {#instance-repeatamount}


**说明:**

复说此时法.

如果 `amount` 的值是正值, 时间线会重复多次。 例如, 1 的值会实际运行两次此时间线 。

传动`false`等于0(没有附加重复). 传动`true`,`undefined`或负数将无限期重复.

如果这个时间线有任何事件设定为`once`,但已经删除,那么它们将**不**重复每个循环。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| amount | number \| boolean | 是 | -1 | 如果`true`或负数,重复的次数将无限。 |


**返回值:** [Phaser.Time.Timeline](/api/class/time-timeline) - 此时法例.


> 源码：[src/time/Timeline.js#L491](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L491)  
引入版本：3.80.0


---

### reset {#reset}

#### \<instance> reset([loop]) {#instance-resetloop}


**说明:**

把这个时间线重新放回开始 。

这将将过去的时间设定为零, 并设定所有事件为不完整 。

如果时间线有任何事件被设定为`once`,但已被删除,那么在调用这种方法后,它们将**不**再次出现.

如果时间线目前没有运行(即暂停或完成),那么就称这种方法重新设置这些状态,与调用`Timeline.play(true)`相同.

目前因本时光线而运行的任何Tweens都会被停止.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| loop | boolean | 是 | false | 设定为 `true` 以保存循环迭代计数器。 时间线自动重复时内部使用。 离开为 `false` 执行全重置 。 |


**返回值:** [Phaser.Time.Timeline](/api/class/time-timeline) - 此时法例.


> 源码：[src/time/Timeline.js#L570](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L570)  
引入版本：3.60.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

将这个时间线从暂停状态中恢复 。

时间线会从它留下的地方继续。

如果需要重设时间线开始,那么就拨打`Timeline.reset`方法.


**返回值:** [Phaser.Time.Timeline](/api/class/time-timeline) - 此时法例.


> 源码：[src/time/Timeline.js#L519](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L519)  
引入版本：3.60.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

停止此时光线。

这将设置 `paused` 和 `complete` 属性为 `true` 。

如果你想重设时间线开始,请拨打`Timeline.reset`方法.


**返回值:** [Phaser.Time.Timeline](/api/class/time-timeline) - 此时法例.


> 源码：[src/time/Timeline.js#L550](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L550)  
引入版本：3.60.0


---

### update {#update}

#### \<instance> update(time, delta) {#instance-updatetime-delta}


**说明:**

由场景更新步骤自动调用 。

浏览所有的时间线事件 检查是否应该运行

如果应该运行,那么事件召回和动作就被引用.

如果`TimelineEvent.once`的属性是`true`,那么事件就从时光网上删除.

如果设定了 `TimelineEvent.event` 属性,那么时间线会显示事件。

如果设置了 `TimelineEvent.run` 属性,则时光网上会引用这种方法。

如果设置了 `TimelineEvent.loop` 属性,则时间线在重复时引用了这种方法.

如果设定了`TimelineEvent.target`属性,那么时光网上就引用了该目标上的`run`方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


**Fires:** [Phaser.Time.Events#event:COMPLETE](/api/event/time-events#complete)


> 源码：[src/time/Timeline.js#L264](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L264)  
引入版本：3.60.0


---

---
