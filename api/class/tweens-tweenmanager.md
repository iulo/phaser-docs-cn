# TweenManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tweens-tweenmanager)

Tween 管理器是一个默认的 Scene 插件,它控制和更新 Tweens 。

是一种在一定的时间内改变目标对象的一个或多个属性的方法.

屈指可数是通过调用`add`方法并在配置对象中通过而创建的.

```js
const logo = this.add.image(100, 100, 'logo');

this.tweens.add({
  targets: logo,
  x: 600,
  ease: 'Power1',
  duration: 2000
});
```

查看`TweenBuilderConfig`的所有选项

除非已配置 tween 以暂停, 否则将立即开始播放 。

请注意, Tween 将不会操纵任何以下划线开头的目标属性 。

特温斯被设计为“ 火与忘” 。 一旦重播完成, 自动毁灭自己, 释放内存和资源。 如果您想要在重播后保留一个特温, 即以后再播放, 那么您应该将 `persist`Z 属性设置为配置中的 `true` 。 然而, 这样做意味着在您完成后完全可以销毁特温, 否则它会永远留在记忆中 。

如果目标已经达到,那么这个圈子会很早就完成 `isDestroyed` 设置为 `true`。这可以避免由于调用方法在被破坏的游戏对象上或用其他任何对象上调用而导致的错误。 `isDestroyed` 属性。当目标对象可能在未来发生变化时,仍然可以引起错误,所以要小心。

如果你想将Tweens连在一起进行顺序回放,请参见`TweenManager.chain`方法.

**构造函数**

`new TweenManager(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 拥有这个Tween经理的场景 |

---


**作用域**: static

> 源码：[src/tweens/TweenManager.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L19)  
引入版本：3.0.0

## 公开成员 {#public-members}

### events {#events}

#### events: [Phaser.Events.EventEmitter](/api/class/events-eventemitter) {#events-phasereventseventemitter}


**说明:**

场景系统事件 Emitter.


> 源码：[src/tweens/TweenManager.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L80)  
引入版本：3.60.0


---

### gap {#gap}

#### gap: number {#gap-number}


**说明:**

内部值,在从目标帧率推导的更新之间,以毫秒计,保持最小的间隔时间。


> 源码：[src/tweens/TweenManager.js#L199](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L199)  
引入版本：3.60.0


---

### lagSkip {#lagSkip}

#### lagSkip: number {#lagskip-number}


**说明:**

时间量,以毫秒计,当应用时用于设定三角洲的缓缓平滑.

详见`TweenManager.setLagSmooth`方法.


> 源码：[src/tweens/TweenManager.js#L186](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L186)  
引入版本：3.60.0


---

### maxLag {#maxLag}

#### maxLag: number {#maxlag-number}


**说明:**

最大时间量,以毫秒计,浏览器可以滞后,然后才应用滞后平滑.

详见`TweenManager.setLagSmooth`方法.


> 源码：[src/tweens/TweenManager.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L173)  
引入版本：3.60.0


---

### nextTime {#nextTime}

#### nextTime: number {#nexttime-number}


**说明:**

Tween 管理器下次更新的时间 。


> 源码：[src/tweens/TweenManager.js#L155](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L155)  
引入版本：3.60.0


---

### paused {#paused}

#### paused: boolean {#paused-boolean}


**说明:**

切换此 Tween 管理器的更新状态 。

设置 `paused` 到 `true`( 或称 `pauseAll` 方法) 将阻止 Tween 管理器更新任何调值, 包括新建的调值。 设置到 `false` 以恢复播放 。


> 源码：[src/tweens/TweenManager.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L101)  
引入版本：3.60.0


---

### prevTime {#prevTime}

#### prevTime: number {#prevtime-number}


**说明:**

Tween 管理器之前更新的时间 。


> 源码：[src/tweens/TweenManager.js#L164](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L164)  
引入版本：3.60.0


---

### processing {#processing}

#### processing: boolean {#processing-boolean}


**说明:**

此 Tween 管理器目前处理 tween 作为其“ 更新” 循环的一部分吗 ? 此设置为“ 更新” 启动时的“ true” , 并重置为函数末尾的“ 假 ” 。 允许您在调用时将 Tween 管理者状态套入 。


> 源码：[src/tweens/TweenManager.js#L115](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L115)  
引入版本：3.60.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

拥有这个Tween经理的场景


> 源码：[src/tweens/TweenManager.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L71)  
引入版本：3.0.0


---

### startTime {#startTime}

#### startTime: number {#starttime-number}


**说明:**

文经理开始的时间.


> 源码：[src/tweens/TweenManager.js#L146](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L146)  
引入版本：3.60.0


---

### time {#time}

#### time: number {#time-number}


**说明:**

Tween经理更新时间.


> 源码：[src/tweens/TweenManager.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L137)  
引入版本：3.60.0


---

### timeScale {#timeScale}

#### timeScale: number {#timescale-number}


**说明:**

腾讯经理的时标.

这个值在两个帧之间标定时间三角形,从而影响这个Tween管理器拥有的所有Tweens的时间速度.


> 源码：[src/tweens/TweenManager.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L89)  
引入版本：3.0.0


---

### tweens {#tweens}

#### tweens: Array.\<[Phaser.Tweens.Tween](/api/class/tweens-tween)> {#tweens-arrayphasertweenstween}


**说明:**

Tween 管理器正在积极处理的 Tweens 系列 。


> 源码：[src/tweens/TweenManager.js#L128](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L128)  
引入版本：3.60.0


---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(config) {#instance-addconfig}


**说明:**

创建 Tween 并将此通过通过通过 Tween 配置对象添加到 Tween 管理器中 。

示例,从场景中运行:

```js
const logo = this.add.image(100, 100, 'logo');

this.tweens.add({
  targets: logo,
  x: 600,
  ease: 'Power1',
  duration: 2000
});
```

查看`TweenBuilderConfig`的所有选项

除非已配置 tween 以暂停, 否则将立即开始播放 。

请注意, Tween 将不会操纵任何以下划线开头的目标属性 。

特温斯被设计为“ 火与忘” 。 一旦重播完成, 自动毁灭自己, 释放内存和资源。 如果您想要在重播后保留一个特温, 即以后再播放, 那么您应该将 `persist`Z 属性设置为配置中的 `true` 。 然而, 这样做意味着在您完成后完全可以销毁特温, 否则它会永远留在记忆中 。

如果你想将Tweens连在一起进行顺序回放,请参见`TweenManager.chain`方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Tweens.TweenBuilderConfig](/api/typedef/types-tweens#tweenbuilderconfig) \| [Phaser.Types.Tweens.TweenChainBuilderConfig](/api/typedef/types-tweens#tweenchainbuilderconfig) | [Phaser.Tweens.Tween](/api/class/tweens-tween) | [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) | 否 | Tween 配置对象,或 Tween 或 TweenChain 实例 。 |


**返回值:** [Phaser.Tweens.Tween](/api/class/tweens-tween) - 所造特温者.


> 源码：[src/tweens/TweenManager.js#L296](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L296)  
引入版本：3.0.0


---

### addCounter {#addCounter}

#### \<instance> addCounter(config) {#instance-addcounterconfig}


**说明:**

创建数字图文并将其添加到活动图文列表中.

数字图文是一种特殊的没有目标图文。 相反, 它允许您在 2 个数字值之间进行调值。 默认值是 。 `0` 财务报告和已审计财务报表 `1`但你可以改变它们 通过 `from` 财务报告和已审计财务报表 `to` 属性。

通过`Tween.getValue()`方法,可以得到当前增量值.

除非已配置 tween 以暂停, 否则将立即开始播放 。

请注意, Tween 将不会操纵任何以下划线开头的目标属性 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Tweens.NumberTweenBuilderConfig](/api/typedef/types-tweens#numbertweenbuilderconfig) | 否 | 数字 Tween 的配置对象 。 |


**返回值:** [Phaser.Tweens.Tween](/api/class/tweens-tween) - 所创数特云.


> 源码：[src/tweens/TweenManager.js#L504](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L504)  
引入版本：3.0.0


---

### addMultiple {#addMultiple}

#### \<instance> addMultiple(configs) {#instance-addmultipleconfigs}


**说明:**

通过传递一系列的Tween配置对象,创建多个Tweens并将其全部添加到这个Tween管理器中.

查看`TweenBuilderConfig`的所有选项

播放会立即开始, 除非已配置 tweens 以暂停 。

请注意, Tween 将不会操纵任何以下划线开头的目标属性 。

特温斯被设计为“ 火与忘” 。 一旦重播完成, 自动毁灭自己, 释放内存和资源。 如果您想要在重播后保留一个特温, 即以后再播放, 那么您应该将 `persist`Z 属性设置为配置中的 `true` 。 然而, 这样做意味着在您完成后完全可以销毁特温, 否则它会永远留在记忆中 。

如果你想将Tweens连在一起进行顺序回放,请参见`TweenManager.chain`方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| configs | Array.\<[Phaser.Types.Tweens.TweenBuilderConfig](/api/typedef/types-tweens#tweenbuilderconfig)> \| Array.\<object> | 否 | Tween 配置对象的阵列 。 |


**返回值:** Array.\<[Phaser.Tweens.Tween](/api/class/tweens-tween)> - 一系列创建的特温斯.


> 源码：[src/tweens/TweenManager.js#L359](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L359)  
引入版本：3.60.0


---

### chain {#chain}

#### \<instance> chain(tweens) {#instance-chaintweens}


**说明:**

创建一个Tweens序列,互相连锁,并加入到这个Tween管理器中.

播放时按顺序进行。 您可以选择设置链条重复您想要的多次。 一旦链条播放完毕, 或者如果设置了重复, 链条中的所有链条都会自动被销毁 。 要覆盖此选项, 请将 `persist` 参数设置为“ true ” 。

播放会立即开始, 除非已配置 _ first_ Tween 暂停 。

请注意,特温斯不会操纵任何以下划线开头的目标属性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tweens | [Phaser.Types.Tweens.TweenChainBuilderConfig](/api/typedef/types-tweens#tweenchainbuilderconfig) \| object | 否 | Tween 链配置对象 。 |


**返回值:** [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) - 特温链案例.


> 源码：[src/tweens/TweenManager.js#L417](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L417)  
引入版本：3.60.0


---

### create {#create}

#### \<instance> create(config) {#instance-createconfig}


**说明:**

创建一个 Tween 并返回, 但不会添加到这个 Tween 管理器中 。

请注意, Tween 将不会操纵任何以下划线开头的目标属性 。

为了玩这个  ,需要通过`TweenManager.existing`方法加入到一个  管理器中.

您可以选择将一个** array ** 的 Tween 配置对象传递到此方法, 并且它将在数组中每个条目创建一个 Tween 。 如果给出了数组, 则返回一个 tweens 数组 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Tweens.TweenBuilderConfig](/api/typedef/types-tweens#tweenbuilderconfig) \| Array.\<[Phaser.Types.Tweens.TweenBuilderConfig](/api/typedef/types-tweens#tweenbuilderconfig)> | object | Array.\<object> | 否 | Tween 配置对象。 或者一系列 Tween 配置对象 。 |


**返回值:** [Phaser.Tweens.Tween](/api/class/tweens-tween), Array.\<[Phaser.Tweens.Tween](/api/class/tweens-tween)> - 创建的 Tween, 或如果提供一组 tween 配置的 Tween 数组 。


> 源码：[src/tweens/TweenManager.js#L247](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L247)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

拥有此插件的场景正在被销毁。 我们需要关闭然后删除所有外部引用 。


> 源码：[src/tweens/TweenManager.js#L1140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L1140)  
引入版本：3.0.0


---

### each {#each}

#### \<instance> each(callback, [scope], [args]) {#instance-eachcallback-scope-args}


**说明:**

将所有Tweens传递给给给定的回调.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | function | 否 | 调用功能 。 |
| scope | object | 是 | 函数的调用范围( `this` 对象) 。 |
| args | * | 是 | 传递到函数的参数。 它的第一个参数将永远是当前正在重复的 Tween 。 |


**返回值:** [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) - 这个Tween经理的例子。


> 源码：[src/tweens/TweenManager.js#L858](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L858)  
引入版本：3.0.0


---

### existing {#existing}

#### \<instance> existing(tween) {#instance-existingtween}


**说明:**

将已有的 Tween 添加到此 Tween 管理器 。

除非已配置 tween 以暂停, 否则将立即开始播放 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 特云增上. |


**返回值:** [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) - 这个Tween经理的例子。


> 源码：[src/tweens/TweenManager.js#L482](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L482)  
引入版本：3.0.0


---

### getChainedTweens {#getChainedTweens}

#### \<instance> getChainedTweens(tween) {#instance-getchainedtweenstween}


**说明:**

返回包含给定的 Tween 和所有 tweens 的 串联的数组, 顺序为播放 。

如果没有链条的Tweens,则返回空数组。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 特温人以还链从. |


**返回值:** Array.\<[Phaser.Tweens.Tween](/api/class/tweens-tween)> - 链条的串联,或者如果没有空的串联.


> 源码：[src/tweens/TweenManager.js#L445](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L445)  
引入版本：3.60.0


---

### getDelta {#getDelta}

#### \<instance> getDelta([tick]) {#instance-getdeltatick}


**说明:**

内部方法,可以计算三角洲值,连同其他计时值,返回新的三角洲.

通常不应直接使用这种方法 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tick | boolean | 是 | false | 这是手动勾选还是自动勾选? |


**返回值:** number - 新的三角洲价值。


> 源码：[src/tweens/TweenManager.js#L636](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L636)  
引入版本：3.60.0


---

### getGlobalTimeScale {#getGlobalTimeScale}

#### \<instance> getGlobalTimeScale() {#instance-getglobaltimescale}


**说明:**

返回该 Tween 管理器拥有的所有 Tweens 的时间三角形的大小 。


**返回值:** number - 时间三角洲的尺度,通常为1.


> 源码：[src/tweens/TweenManager.js#L955](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L955)  
引入版本：3.0.0


---

### getTweens {#getTweens}

#### \<instance> getTweens() {#instance-gettweens}


**说明:**

返回包含此 Tween 管理器中所有 Tweens 引用的数组 。

将返回的数组进行突变是安全的。 但是, 将按其中的任何调值调整存储在调值管理器中的调值, 因为这些调值是通过参考而不是复制的 。

如果你想得到一个特定目标的特写,请参见`getTweensOf`.


**返回值:** Array.\<[Phaser.Tweens.Tween](/api/class/tweens-tween)> - 包含所有 Tweens 引用的新数组 。


> 源码：[src/tweens/TweenManager.js#L890](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L890)  
引入版本：3.0.0


---

### getTweensOf {#getTweensOf}

#### \<instance> getTweensOf(target) {#instance-gettweensoftarget}


**说明:**

返回 Tween 管理器中影响给定目标或一系列目标的 Tweens 数组 。

此方法可以将即将从Tween管理器中移除的  还原,在采取行动前,您应该先检查返回的  的状态.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | object \| Array.\<object> | 否 | 要寻找的目标。 提供一个阵列来寻找多个目标 。 |


**返回值:** Array.\<[Phaser.Tweens.Tween](/api/class/tweens-tween)> - 包含所有影响给定目标的Tweens的新阵列 。


> 源码：[src/tweens/TweenManager.js#L909](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L909)  
引入版本：3.0.0


---

### has {#has}

#### \<instance> has(tween) {#instance-hastween}


**说明:**

检查是否在此 Tween 管理器中存在给定的 Tween 实例 。

只要Tween的处理由Tween经理进行,就会返回`true`.

如果不在场,则返回`false`,或者状态为`REMOVED`或`DESTROYED`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 特温的例子来检查。 |


**返回值:** boolean - 如果Tween在Tween经理内部存在,则`true`,否则`false`.


> 源码：[src/tweens/TweenManager.js#L463](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L463)  
引入版本：3.60.0


---

### isTweening {#isTweening}

#### \<instance> isTweening(target) {#instance-istweeningtarget}


**说明:**

检查给定对象是否受到_playing_Tween 的影响.

若  文停,此法必归假.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | object | 否 | 检查 tween 是否活动的对象 。 |


**返回值:** boolean - 如果一个双音在给定目标上活动,则返回 `true`,否则返回 `false`.


> 源码：[src/tweens/TweenManager.js#L987](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L987)  
引入版本：3.0.0


---

### killAll {#killAll}

#### \<instance> killAll() {#instance-killall}


**说明:**

摧毁所有Tween经理的Tweens.

双胞胎会删除所有提及他们持有的目标的文字,并被立即制止.

如果在Tween管理器运行更新进程时调用这种方法, 那么在下一个框架开始时将删除 tweens。 在此之外, 立即删除 。


**返回值:** [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) - 这个Tween经理的例子。


> 源码：[src/tweens/TweenManager.js#L1017](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L1017)  
引入版本：3.0.0


---

### killTweensOf {#killTweensOf}

#### \<instance> killTweensOf(target) {#instance-killtweensoftarget}


**说明:**

停止所有影响给定目标或一系列目标的调子。

双胞胎会删除所有提及他们持有的目标的文字,并被立即制止.

如果在Tween管理器运行更新进程时调用这种方法, 那么在下一个框架开始时将删除 tweens。 在此之外, 立即删除 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | object \| array | 否 | 杀死 tweens 的目标。 提供使用多个目标的阵列 。 |


**返回值:** [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) - 这个Tween经理的例子。


> 源码：[src/tweens/TweenManager.js#L1049](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L1049)  
引入版本：3.0.0


---

### makeActive {#makeActive}

#### \<instance> makeActive(tween) {#instance-makeactivetween}


**说明:**

检查一个 Tween 是否在活动, 如果不是, 在框架开头添加到 Tween 管理器中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 特温检查。 |


**返回值:** [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) - 这个Tween经理的例子。


> 源码：[src/tweens/TweenManager.js#L839](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L839)  
引入版本：3.0.0


---

### pauseAll {#pauseAll}

#### \<instance> pauseAll() {#instance-pauseall}


**说明:**

暂停此 Tween 管理器。 暂停时不会更新 Tween 。

这包括这种方法被称作后创建的  .

参见`TweenManager#resumeAll`恢复播放.

截至2007年12月31日的 Phaser 3: 60 您也可以切换布尔属性 `TweenManager.paused`.


**返回值:** [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) - 这个Tween经理的例子。


> 源码：[src/tweens/TweenManager.js#L1080](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L1080)  
引入版本：3.0.0


---

### remove {#remove}

#### \<instance> remove(tween) {#instance-removetween}


**说明:**

从 Tween 管理器中删除给定的 Tween , 即使它还没有开始播放。 如果在 Tween 管理机处理更新循环时调用这种方法, 那么在下一个帧开始时会标记 tween 以删除。 否则, 立即删除它 。

移除的 tween 已被 _ not_ 销毁。 它刚刚从 Tween 管理器中移除 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 特温被除去. |


**返回值:** [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) - 这个Tween经理的例子。


> 源码：[src/tweens/TweenManager.js#L781](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L781)  
引入版本：3.17.0


---

### reset {#reset}

#### \<instance> reset(tween) {#instance-resettween}


**说明:**

重置给定的图文.

若特温不属此特温经理,则先加.

然后它会寻求定位0,然后在下一个帧开始播放.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 复置  文. |


**返回值:** [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) - 这个Tween经理的例子。


> 源码：[src/tweens/TweenManager.js#L814](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L814)  
引入版本：3.60.0


---

### resumeAll {#resumeAll}

#### \<instance> resumeAll() {#instance-resumeall}


**说明:**

收录了这个Tween管理器的播放.

所有活跃的Tweens将继续更新.

见`TweenManager#pauseAll`暂停播放.

截至2007年12月31日的 Phaser 3: 60 您也可以切换布尔属性 `TweenManager.paused`.


**返回值:** [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) - 这个Tween经理的例子。


> 源码：[src/tweens/TweenManager.js#L1101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L1101)  
引入版本：3.0.0


---

### setFps {#setFps}

#### \<instance> setFps([fps]) {#instance-setfpsfps}


**说明:**

限制Tween系统运行在特定帧速率.

您不应该设置此_ 高于_ 浏览器的频率, 而是可以在某种情况下使用它来降低帧率 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| fps | number | 是 | 240 | 框速率可以勾选 。 |


**返回值:** [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) - 这个Tween经理的例子。


> 源码：[src/tweens/TweenManager.js#L612](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L612)  
引入版本：3.60.0


---

### setGlobalTimeScale {#setGlobalTimeScale}

#### \<instance> setGlobalTimeScale(value) {#instance-setglobaltimescalevalue}


**说明:**

为这个 Tween 管理器设定新的时间三角形比例 。

时间三角洲是连续两个帧之间的时间, 并影响这个 Tween 管理器和它拥有的所有 Tweens 的时间速度。 值高于 1 的值会增加时间速度, 而值小于 1 的值会减少时间。 0 值会冻结时间, 并且实际上相当于将所有 Tweens 都浪费掉 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 时间三角洲的新尺度,其中1是正常速度. |


**返回值:** [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) - 这个Tween经理的例子。


> 源码：[src/tweens/TweenManager.js#L968](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L968)  
引入版本：3.0.0


---

### setLagSmooth {#setLagSmooth}

#### \<instance> setLagSmooth([limit], [skip]) {#instance-setlagsmoothlimit-skip}


**说明:**

设定浏览器遇到滞后时使用的限度, 或是导致两个帧之间时间跨度超过预期数量的延迟。 如果发生这种情况, Tween 管理器将像“ skip” 时间跨度一样行事, 以保持严格的曲折顺序 。

默认情况下启用了该选项, 其值为 5 000 ms 的后置限制, 跳过时则启用 33 ms 。

不应该设置为低值, 因为这样不会给浏览器时间 来追赶自己并恢复同步 。

调用此方法时没有参数可禁用平滑 。

用参数`500`和`33`调用它来重置默认值.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| limit | number | 是 | 0 | 如果浏览器超过这个数量, 以毫秒计, 它会像“ skip” 数量已经过去一样 。 |
| skip | number | 是 | 0 | 浏览器在“ 限值” 后差时, 用作步骤三角洲的数值, 以毫秒计 。 |


**返回值:** [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) - 这个Tween经理的例子。


> 源码：[src/tweens/TweenManager.js#L579](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L579)  
引入版本：3.60.0


---

### shutdown {#shutdown}

#### \<instance> shutdown() {#instance-shutdown}


**说明:**

拥有此插件的场景正在关闭 。

我们需要杀死和重置所有内部属性,以及停止听闻场景事件.


> 源码：[src/tweens/TweenManager.js#L1122](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L1122)  
引入版本：3.0.0


---

### stagger {#stagger}

#### \<instance> stagger(value, [config]) {#instance-staggervalue-config}


**说明:**

创建 Staggger 函数,供 Tween 属性使用。

交错函数将允许您在 tween 的所有目标上错开属性值的更改 。

只有在  有多个目标时才值得使用.

以下将错开百米的延迟,跨过所有  的目标,使其在指定期限内缩放到0.2: 1.

```javascript
this.tweens.add({
    targets: [ ... ],
    scale: 0.2,
    ease: 'linear',
    duration: 1000,
    delay: this.tweens.stagger(100)
});
```

以下将使用10×6格栅在  的所有目标上错开500ms的延迟,从中心向外突起,使用立方易行.

```javascript
this.tweens.add({
    targets: [ ... ],
    scale: 0.2,
    ease: 'linear',
    duration: 1000,
    delay: this.tweens.stagger(500, { grid: [ 10, 6 ], from: 'center', ease: 'cubic.out' })
});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number \| Array.\<number> | 否 | 由或包含两个元素的阵列交错的金额, 代表分钟和最大值, 以在两者之间交错 。 |
| config | [Phaser.Types.Tweens.StaggerConfig](/api/typedef/types-tweens#staggerconfig) | 是 | Stagger 函数的配置对象 。 |


**返回值:** function - 交错功能.


> 源码：[src/tweens/TweenManager.js#L533](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L533)  
引入版本：3.19.0


---

### step {#step}

#### \<instance> step([tick]) {#instance-steptick}


**说明:**

更新属于 Tween 管理器的全部 Tweens 。

由`update`和`tick`自动调用.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tick | boolean | 是 | false | 这是手动勾选还是自动勾选? |


> 源码：[src/tweens/TweenManager.js#L713](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L713)  
引入版本：3.60.0


---

### tick {#tick}

#### \<instance> tick() {#instance-tick}


**说明:**

手动推进特温系统一步.

这将更新所有 Tweens , 即使 Tween 管理器目前暂停 。


**返回值:** [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) - 这个Tween经理的例子。


> 源码：[src/tweens/TweenManager.js#L678](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L678)  
引入版本：3.60.0


---

### update {#update}

#### \<instance> update() {#instance-update}


**说明:**

内部更新处理器.

只要Tween管理器没有被暂停,就给`TweenManager.step`打电话.


> 源码：[src/tweens/TweenManager.js#L696](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/TweenManager.js#L696)  
引入版本：3.0.0


---

---
