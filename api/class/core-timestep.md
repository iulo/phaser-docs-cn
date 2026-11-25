# TimeStep {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/core-timestep)

Phaser用来处理游戏循环的核心跑者类,它可以根据浏览器支持和配置设置,使用请求动画框架,或SetTimeout,在浏览器内部创建连续循环.

每次循环点火,`TimeStep.step`被调用,然后传递到游戏核心更新循环,这是游戏的核心心跳,会像请求动画框架能够处理目标设备一样频繁发射.

请注意, 浏览器会停止更新您的游戏, 有很多情况, 例如玩家会切换标签, 或者用其他应用程序覆盖浏览器窗口。 在这种情况下, 您游戏的“ 心跳” 将会暂停, 只有在玩家返回焦点时才会恢复。 您无法避免这种情况, 您只能使用浏览器的可见事件, PhaserZ 来检测它发生的时间, 然后优雅地恢复 。

**构造函数**

`new TimeStep(game, config)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 提到这个时间步的Phaser.Game实例. |
| config | [Phaser.Types.Core.FPSConfig](/api/typedef/types-core#fpsconfig) | 否 | FPS 配置对象, 由 Game Config 解析 。 |

---


**作用域**: static

> 源码：[src/core/TimeStep.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L14)  
引入版本：3.0.0

## 公开成员 {#public-members}

### actualFps {#actualFps}

#### actualFps: number {#actualfps-number}


**说明:**

每秒帧的指数移动平均值。


> 源码：[src/core/TimeStep.js#L188](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L188)  
引入版本：3.0.0


---

### callback {#callback}

#### callback: [Phaser.Types.Core.TimeStepCallback](/api/typedef/types-core#timestepcallback) {#callback-phasertypescoretimestepcallback}


**说明:**

每次时间步调时都会引用回调 。


> 源码：[src/core/TimeStep.js#L223](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L223)  
引入版本：3.0.0


---

### delta {#delta}

#### delta: number {#delta-number}


**说明:**

三角洲时间, 以ms计, 自上次游戏步骤以来。 这是一个被夹住和平滑的平均值 。


> 源码：[src/core/TimeStep.js#L340](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L340)  
引入版本：3.0.0


---

### deltaHistory {#deltaHistory}

#### deltaHistory: Array.\<number> {#deltahistory-arraynumber}


**说明:**

内部数组持有先前的三角洲值,用于三角洲平滑.


> 源码：[src/core/TimeStep.js#L360](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L360)  
引入版本：3.0.0


---

### deltaIndex {#deltaIndex}

#### deltaIndex: number {#deltaindex-number}


**说明:**

三角洲历史位置内部索引.


> 源码：[src/core/TimeStep.js#L350](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L350)  
引入版本：3.0.0


---

### deltaSmoothingMax {#deltaSmoothingMax}

#### deltaSmoothingMax: number {#deltasmoothingmax-number}


**说明:**

为了计算平滑移动平均值而保留的最大三角洲值。

可以通过 `fps.deltaHistory` 属性在 Game Config 中更改此选项。 默认为 10 。


> 源码：[src/core/TimeStep.js#L369](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L369)  
引入版本：3.0.0


---

### forceSetTimeOut {#forceSetTimeOut}

#### forceSetTimeOut: boolean {#forcesettimeout-boolean}


**说明:**

您可以在游戏配置对象中将 `forceSetTimeOut` 属性设置为 `true` , 以强制 TimeStep 使用 SetTimeOut 而不是请求动画框架。 运行时不能更改 。


> 源码：[src/core/TimeStep.js#L233](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L233)  
引入版本：3.0.0


---

### fpsLimit {#fpsLimit}

#### fpsLimit: number {#fpslimit-number}


**说明:**

执行帧率限制。 这迫使游戏步骤运行的频率是零, 默认情况下, 它会运行在浏览器( 通过 ArequestAnimationFrame) 能处理的任意限制, 这是快速动作或响应游戏的最佳速度 。

然而,如果你正在构建一个非游戏应用程序,比如图形生成器,或者不需要60fps的低强度游戏,那么您可以通过这个Game Config值降低步速:

```js
fps: {
  limit: 30
}
```

设置此_ 超越_ 请求动画Frame 的速率将没有任何变化 。

纯用于低强度情况下的_限制_更新.


> 源码：[src/core/TimeStep.js#L115](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L115)  
引入版本：3.60.0


---

### frame {#frame}

#### frame: number {#frame-number}


**说明:**

游戏当前框架正在打开。 此计数器每一步都会递增, 不论时间有多长, 也不会受到三角洲平滑的影响 。


> 源码：[src/core/TimeStep.js#L282](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L282)  
引入版本：3.0.0


---

### framesThisSecond {#framesThisSecond}

#### framesThisSecond: number {#framesthissecond-number}


**说明:**

处理的帧数是这一秒 。


> 源码：[src/core/TimeStep.js#L212](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L212)  
引入版本：3.0.0


---

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

参考Phaser.Game案例.


> 源码：[src/core/TimeStep.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L43)  
引入版本：3.0.0


---

### hasFpsLimit {#hasFpsLimit}

#### hasFpsLimit: boolean {#hasfpslimit-boolean}


**说明:**

家庭补贴费率是否有限?

设置此值时, 将 Game Config `limit` 值设置为 0 以上值 。

视此属性为只读 。


> 源码：[src/core/TimeStep.js#L140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L140)  
引入版本：3.60.0


---

### inFocus {#inFocus}

#### inFocus: boolean {#infocus-boolean}


**说明:**

浏览器目前是否被Page可见度API考虑焦点?

此值设定在 `blur` 方法中,该方法被 Game 实例自动调用.


> 源码：[src/core/TimeStep.js#L294](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L294)  
引入版本：3.0.0


---

### lastTime {#lastTime}

#### lastTime: number {#lasttime-number}


**说明:**

上一步之时.

这通常是一个高分辨率的定时器值,如Request Animation Framework提供的那样.


> 源码：[src/core/TimeStep.js#L270](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L270)  
引入版本：3.0.0


---

### minFps {#minFps}

#### minFps: number {#minfps-number}


**说明:**

您想要时间步数运行的最小 fps 速率 。

设定此选项不能保证浏览器运行以这个速度, 它只会影响内部的计时值, 帮助时间步知道它何时脱离同步 。


> 源码：[src/core/TimeStep.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L88)  
引入版本：3.0.0


---

### nextFpsUpdate {#nextFpsUpdate}

#### nextFpsUpdate: number {#nextfpsupdate-number}


**说明:**

下一次 fps 更新速度的时间将进行 。

当fps更新发生时,`framesThisSecond`值会被重置.


> 源码：[src/core/TimeStep.js#L199](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L199)  
引入版本：3.0.0


---

### now {#now}

#### now: number {#now-number}


**说明:**

时间, 设定在目前步骤的开始 。

这通常是一个高分辨率的定时器值,如Request Animation Framework提供的那样.

这与`time`值可能不同,因为它不是根据三角洲值计算的.


> 源码：[src/core/TimeStep.js#L407](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L407)  
引入版本：3.18.0


---

### panicMax {#panicMax}

#### panicMax: number {#panicmax-number}


**说明:**

冷却器在浏览器对FPS率恐慌后设定的帧数,通常由于切换制表符和重拾焦点.

可以通过 `fps.panicMax` 属性在 Game Config 中更改此选项。 默认为 120 。


> 源码：[src/core/TimeStep.js#L381](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L381)  
引入版本：3.0.0


---

### pauseDuration {#pauseDuration}

#### pauseDuration: number {#pauseduration-number}


**说明:**

最近的游戏暂停时间,如果有的话,以ms表示。


> 源码：[src/core/TimeStep.js#L307](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L307)  
引入版本：3.85.0


---

### raf {#raf}

#### raf: [Phaser.DOM.RequestAnimationFrame](/api/class/dom-requestanimationframe) {#raf-phaserdomrequestanimationframe}


**说明:**

请求动画框架 DOM 事件处理器 。


> 源码：[src/core/TimeStep.js#L53](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L53)  
引入版本：3.0.0


---

### rawDelta {#rawDelta}

#### rawDelta: number {#rawdelta-number}


**说明:**

一次更新与下一次更新之间的实际时间(以毫秒计).

与 `delta` 不同的是, 无法对这个值应用平滑、 封顶或平均值。 因此, 请在数学计算中使用这个值时小心 。


> 源码：[src/core/TimeStep.js#L394](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L394)  
引入版本：3.0.0


---

### running {#running}

#### running: boolean {#running-boolean}


**说明:**

时标在停止时运行和切换时设置。 此值和 `started`的区别在于, 当时标发送到睡眠时, `running`被切换, 此时- as `started` 仍然为 `true`, 只有当实际停止时才会改变, 而不是只暂停 。


> 源码：[src/core/TimeStep.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L74)  
引入版本：3.0.0


---

### smoothStep {#smoothStep}

#### smoothStep: boolean {#smoothstep-boolean}


**说明:**

将光滑应用到 Phaser 内部计算中使用的三角洲值中?

可以通过 `fps.smoothStep` 属性在 Game Config 中更改此选项。 默认为 `true` 。

平滑有助于在浏览器标签开关后调和三角洲值, 或其他可能导致显著三角洲突起或滑动的状态。 默认它自第一个版本以来就已启用在 Phaser 3 中, 但现在在此属性下被曝光( 以及相应的游戏配置 `smoothStep` 值) , 以便您能够在需要时轻松禁用它 。


> 源码：[src/core/TimeStep.js#L421](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L421)  
引入版本：3.22.0


---

### started {#started}

#### started: boolean {#started-boolean}


**说明:**

时空时空时空开始运行并停止时切换时设定的旗帜 。


> 源码：[src/core/TimeStep.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L63)  
引入版本：3.0.0


---

### startTime {#startTime}

#### startTime: number {#starttime-number}


**说明:**

游戏开始运行的时间.

如果游戏被暂停并恢复,则此值会调整 。


> 源码：[src/core/TimeStep.js#L258](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L258)  
引入版本：3.0.0


---

### targetFps {#targetFps}

#### targetFps: number {#targetfps-number}


**说明:**

时间步跑的目标 fps 速率 。

设置此值不会实际改变浏览器运行的速度, 即Phaser控制不了的速度。 相反, 它允许您确定性能问题, 以及时间步是否螺旋失控 。


> 源码：[src/core/TimeStep.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L101)  
引入版本：3.0.0


---

### time {#time}

#### time: number {#time-number}


**说明:**

时间, 更新每个步骤, 将已过期的三角洲时间加到上一个值 。

这与`TimeStep.now`值不同,这是请求动画框架提供的高分辨率时间值.


> 源码：[src/core/TimeStep.js#L245](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L245)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### blur {#blur}

#### \<instance> blur() {#instance-blur}


**说明:**

由游戏实例在 DOM 窗口时调用 。onBlur 事件触发。


> 源码：[src/core/TimeStep.js#L438](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L438)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁 TimeStep 。 这将停止请求动画框架, 停止步骤, 清除回调和取消任何对象 。


> 源码：[src/core/TimeStep.js#L865](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L865)  
引入版本：3.0.0


---

### focus {#focus}

#### \<instance> focus() {#instance-focus}


**说明:**

由游戏实例在 DOM 窗口时调用 。onFocus 事件触发。


> 源码：[src/core/TimeStep.js#L449](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L449)  
引入版本：3.0.0


---

### getDuration {#getDuration}

#### \<instance> getDuration() {#instance-getduration}


**说明:**

获得游戏运行的时间, 以秒计 。


**返回值:** number - 持续时间数秒。


> 源码：[src/core/TimeStep.js#L821](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L821)  
引入版本：3.17.0


---

### getDurationMS {#getDurationMS}

#### \<instance> getDurationMS() {#instance-getdurationms}


**说明:**

获得游戏运行的时间, 以ms计 。


**返回值:** number - 持续时间(ms).


> 源码：[src/core/TimeStep.js#L834](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L834)  
引入版本：3.17.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

当能见度 API 表示游戏为“ 隐藏” (tab 切换到视图等)时调用 。


> 源码：[src/core/TimeStep.js#L462](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L462)  
引入版本：3.0.0


---

### resetDelta {#resetDelta}

#### \<instance> resetDelta() {#instance-resetdelta}


**说明:**

重排时间、 lastTime、 fps 平均和 delta 历史。 当浏览器睡眠后自动调用 。


> 源码：[src/core/TimeStep.js#L487](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L487)  
引入版本：3.0.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

当能见度 API 表示游戏再次“ 可见” 时调用(  Tab 切换回视图等)


> 源码：[src/core/TimeStep.js#L473](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L473)  
引入版本：3.0.0


---

### sleep {#sleep}

#### \<instance> sleep() {#instance-sleep}


**说明:**

发送时间步调睡眠,停止请求动画框架(或Settimeout),并将`running`旗拖向假面.


> 源码：[src/core/TimeStep.js#L768](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L768)  
引入版本：3.0.0


---

### smoothDelta {#smoothDelta}

#### \<instance> smoothDelta(delta) {#instance-smoothdeltadelta}


**说明:**

取三角洲值,并基于先前的帧来平滑它.

作为步骤的一部分自动调用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delta | number | 否 | 三角洲对这个步骤的价值. |


**返回值:** number - 平滑三角形值.


> 源码：[src/core/TimeStep.js#L551](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L551)  
引入版本：3.60.0


---

### start {#start}

#### \<instance> start(callback) {#instance-startcallback}


**说明:**

如果时间步未启动, 则启动时间步运行。 由 Game Boot 进程自动调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | [Phaser.Types.Core.TimeStepCallback](/api/typedef/types-core#timestepcallback) | 否 | 每次时间步调时都会引用回调. |


> 源码：[src/core/TimeStep.js#L516](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L516)  
引入版本：3.0.0


---

### step {#step}

#### \<instance> step(time) {#instance-steptime}


**说明:**

主步骤方法。 每次浏览器更新时都会使用请求动画框架或设定超时调用。它负责计算三角洲值、框架总和、冷却历史等。您通常不应该直接调用这种方法。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 时间戳从请求动画Frame或setTimeout传递过来. |


> 源码：[src/core/TimeStep.js#L701](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L701)  
引入版本：3.0.0


---

### stepLimitFPS {#stepLimitFPS}

#### \<instance> stepLimitFPS(time) {#instance-steplimitfpstime}


**说明:**

带有 fps 限制器的主要步骤方法。 每次浏览器更新时, 无论是通过请求动画框架还是设定超时程序, 都会使用此方法。 它负责计算三角洲值、 框架总和、 冷却历史等。 一般情况下, 您不应该直接调用这种方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 时间戳从请求动画Frame或setTimeout传递过来. |


> 源码：[src/core/TimeStep.js#L650](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L650)  
引入版本：3.60.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

停止时间步跑。


**返回值:** [Phaser.Core.TimeStep](/api/class/core-timestep) - 时空步进对象.


> 源码：[src/core/TimeStep.js#L847](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L847)  
引入版本：3.0.0


---

### tick {#tick}

#### \<instance> tick() {#instance-tick}


**说明:**

使用 `window.performance.now` 的当前时间戳, 手动将 TimeStep 推进一步。 如果一个 FPS 限制有效, 则呼叫 `TimeStep.stepLimitFPS`Z , 否则则呼叫 `TimeStep.step` 。


> 源码：[src/core/TimeStep.js#L747](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L747)  
引入版本：3.0.0


---

### updateFPS {#updateFPS}

#### \<instance> updateFPS(time) {#instance-updatefpstime}


**说明:**

更新帧率的估计数 `fps`。 秒数中, 秒数中发生的帧数包含在每秒所有帧的指数移动平均值中, α为0. 25。 这意味着最近秒数对帧率的影响大于旧秒数 。

当浏览器窗口没有最小化,而是被遮盖(即您正在使用另一个在浏览器顶端上方培育出窗口的应用程序)时,它就会开始拖动raf回调时间。它会等待一段时间,然后开始将帧率降低到每秒1帧,直到下降到1fps。所以如果游戏运行在60fps,玩家打开新窗口,在60秒后(+'缓冲时间'),它会降到1fps,在1Hz时发射。

当他们再次让游戏亮相时,帧率以约8fps的速度增加,备份最高可达60fps(或它可以获得的最大)

很难确定帧率的下降是因为浏览器在减速,还是因为游戏在性能上挣扎是因为你要求它在设备上做太多.

计算新的指数移动平均值,α为0.25。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 时间戳从请求动画Frame或setTimeout传递过来. |


> 源码：[src/core/TimeStep.js#L615](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L615)  
引入版本：3.60.0


---

### wake {#wake}

#### \<instance> wake([seamless]) {#instance-wakeseamless}


**说明:**

唤醒 TimeStep, 重新启动请求动画框架( 或 SetTimeout) , 并将 `running` 旗向真向移动。 `seamless` 参数控制是否该提醒是否调整启动时间 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| seamless | boolean | 是 | false | 调整 startTime 以 lastTime 价值。 |


> 源码：[src/core/TimeStep.js#L784](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/TimeStep.js#L784)  
引入版本：3.0.0


---

---
