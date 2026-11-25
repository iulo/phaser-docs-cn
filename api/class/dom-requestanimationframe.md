# RequestAnimationFrame {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/dom-requestanimationframe)

摘要取消使用`requestAnimationFrame`或`setTimeout`来进行核心游戏更新循环,不管使用哪种机制,都提供统一的界面.

当 `requestAnimationFrame` 可用且不覆时,它被用于驱动游戏循环,该循环将更新与显示刷新速率联系起来,并在隐藏标签时自动暂停. 如果 `forceSetTimeOut` 在 Game Config 中启用,则使用 `setTimeout` 代替,它运行在固定的间隔中,而无论可见度或显示同步性如何.

此类由Phaser.Game实例自动即时管理.


**作用域**: static

> 源码：[src/dom/RequestAnimationFrame.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/RequestAnimationFrame.js#L10)  
引入版本：3.0.0

## 公开成员 {#public-members}

### callback {#callback}

#### callback: FrameRequestCallback {#callback-framerequestcallback}


**说明:**

每一步都要引用回调.


> 源码：[src/dom/RequestAnimationFrame.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/RequestAnimationFrame.js#L43)  
引入版本：3.0.0


---

### delay {#delay}

#### delay: number {#delay-number}


**说明:**

使用 setTimeout 时,每步之间的延迟数,以毫秒计。


> 源码：[src/dom/RequestAnimationFrame.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/RequestAnimationFrame.js#L72)  
引入版本：3.60.0


---

### isRunning {#isRunning}

#### isRunning: boolean {#isrunning-boolean}


**说明:**

如果请求动画Frame运行, 否则会是假的 。


> 源码：[src/dom/RequestAnimationFrame.js#L33](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/RequestAnimationFrame.js#L33)  
引入版本：3.0.0


---

### isSetTimeOut {#isSetTimeOut}

#### isSetTimeOut: boolean {#issettimeout-boolean}


**说明:**

如果台阶是使用setTimeout而不是RAF,那么就是真的.


> 源码：[src/dom/RequestAnimationFrame.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/RequestAnimationFrame.js#L52)  
引入版本：3.0.0


---

### step {#step}

#### step: FrameRequestCallback {#step-framerequestcallback}


**说明:**

RAF步法功能.

重新调用,并安排 又一次呼叫requestAnimationFrame。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 时间戳从请求动画Frame传入. |


> 源码：[src/dom/RequestAnimationFrame.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/RequestAnimationFrame.js#L84)  
引入版本：3.0.0


---

### stepTimeout {#stepTimeout}

#### stepTimeout: function {#steptimeout-function}


**说明:**

SetTimeout 步骤函数 。

重新调用,并安排 又一次呼叫setTimeout。


> 源码：[src/dom/RequestAnimationFrame.js#L105](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/RequestAnimationFrame.js#L105)  
引入版本：3.0.0


---

### timeOutID {#timeOutID}

#### timeOutID: number {#timeoutid-number}


**说明:**

取消时使用的setTimeout或RAF召回ID.


> 源码：[src/dom/RequestAnimationFrame.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/RequestAnimationFrame.js#L62)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

停止步骤运行并清除回调引用。


> 源码：[src/dom/RequestAnimationFrame.js#L174](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/RequestAnimationFrame.js#L174)  
引入版本：3.0.0


---

### start {#start}

#### \<instance> start(callback, forceSetTimeOut, delay) {#instance-startcallback-forcesettimeout-delay}


**说明:**

启动 requestAnimationFrame或 setTimeout进程运行.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | FrameRequestCallback | 否 | 召回以引诸步. |
| forceSetTimeOut | boolean | 否 | 它应该使用SetTimeout, 即使有RAF吗? |
| delay | number | 否 | 使用 setTimeout 时,每步之间的延迟数,以毫秒计。 |


> 源码：[src/dom/RequestAnimationFrame.js#L126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/RequestAnimationFrame.js#L126)  
引入版本：3.0.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

停止requestAnimationFrame或setTimeout运行.


> 源码：[src/dom/RequestAnimationFrame.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/RequestAnimationFrame.js#L154)  
引入版本：3.0.0


---

---
