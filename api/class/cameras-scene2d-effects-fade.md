# Fade {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/cameras-scene2d-effects-fade)

相机失效效应.

这一效果将在指定时间内将相机的视窗淡化到给定的颜色.

只有相机的视图被淡出。 它显示的物体没有受到影响, 即它们的颜色不会改变 。

效果会在相机本身上发出几个事件,您也可以指定一个`onUpdate`调回,在效果持续期间,如果需要,每个帧都会引用.

**构造函数**

`new Fade(camera)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 摄像机,这个效果正在采取行动。 |

---


**作用域**: static

> 源码：[src/cameras/2d/effects/Fade.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Fade.js#L11)  
引入版本：3.5.0

## 公开成员 {#public-members}

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#camera-phasercamerasscene2dcamera}


**说明:**

相机这个效果属于。


> 源码：[src/cameras/2d/effects/Fade.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Fade.js#L36)  
引入版本：3.5.0


---

### direction {#direction}

#### direction: boolean {#direction-boolean}


**说明:**

淡出方向. `true` = 淡出(透明为颜色), `false` = 淡出(颜色为透明)


> 源码：[src/cameras/2d/effects/Fade.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Fade.js#L71)  
引入版本：3.5.0


---

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

效果的持续时间,以毫秒计.


> 源码：[src/cameras/2d/effects/Fade.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Fade.js#L82)  
引入版本：3.5.0


---

### isComplete {#isComplete}

#### isComplete: boolean {#iscomplete-boolean}


**说明:**

此效果是否运行完毕 ?

这与`isRunning`不同,因为它在效果结束时仍然被设定为`true`,直到效果被重置或再次启动.


> 源码：[src/cameras/2d/effects/Fade.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Fade.js#L57)  
引入版本：3.5.0


---

### isRunning {#isRunning}

#### isRunning: boolean {#isrunning-boolean}


**说明:**

效果是否积极运行?


> 源码：[src/cameras/2d/effects/Fade.js#L46](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Fade.js#L46)  
引入版本：3.5.0


---

### progress {#progress}

#### progress: number {#progress-number}


**说明:**

如果正在运行此效果, 则该结果将保留当前进度的百分比, 值在 0 到 1 之间 。


> 源码：[src/cameras/2d/effects/Fade.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Fade.js#L137)  
引入版本：3.5.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这种效果,从镜头中释放出来.


> 源码：[src/cameras/2d/effects/Fade.js#L348](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Fade.js#L348)  
引入版本：3.5.0


---

### effectComplete {#effectComplete}

#### \<instance> effectComplete() {#instance-effectcomplete}


**说明:**

效果完成后内部调用.


**Fires:** [Phaser.Cameras.Scene2D.Events#event:FADE_IN_COMPLETE](/api/event/cameras-scene2d-events#fade_in_complete), [Phaser.Cameras.Scene2D.Events#event:FADE_OUT_COMPLETE](/api/event/cameras-scene2d-events#fade_out_complete)


> 源码：[src/cameras/2d/effects/Fade.js#L311](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Fade.js#L311)  
引入版本：3.5.0


---

### postRenderCanvas {#postRenderCanvas}

#### \<instance> postRenderCanvas(ctx) {#instance-postrendercanvasctx}


**说明:**

由坎瓦斯兰代尔公司内部召见.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ctx | CanvasRenderingContext2D | 否 | 坎瓦斯的上下文将变成。 |


**返回值:** boolean - 如果效果向渲染器引出`true`,否则会发出`false`.


> 源码：[src/cameras/2d/effects/Fade.js#L273](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Fade.js#L273)  
引入版本：3.5.0


---

### postRenderWebGL {#postRenderWebGL}

#### \<instance> postRenderWebGL() {#instance-postrenderwebgl}


**说明:**

由WebGL制片人内部召集.


**返回值:** boolean - 如果效果应引向渲染器,则使用`true`,否则使用`false`.


> 源码：[src/cameras/2d/effects/Fade.js#L298](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Fade.js#L298)  
引入版本：3.5.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

重置此相机效果。 如果它之前运行过, 它会立即停止, 而不调用它的 onComplete 回调或释放事件 。


> 源码：[src/cameras/2d/effects/Fade.js#L332](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Fade.js#L332)  
引入版本：3.5.0


---

### start {#start}

#### \<instance> start([direction], [duration], [red], [green], [blue], [force], [callback], [context]) {#instance-startdirection-duration-red-green-blue-force-callback-context}


**说明:**

相机在指定期间从给定颜色向或向外显示。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| direction | boolean | 是 | true | 淡出方向. `true` = 淡出(透明为颜色), `false` = 淡出(颜色为透明) |
| duration | number | 是 | 1000 | 效果持续时间以毫秒计. |
| red | number | 是 | 0 | 向红色通道淡化的数值, 值在 0 到 255 之间 。 |
| green | number | 是 | 0 | 向绿色通道淡去的金额,数值在0到255之间。 |
| blue | number | 是 | 0 | 向蓝色通道淡去的金额, 值在 0 到 255 之间 。 |
| force | boolean | 是 | false | 强制效果立即启动, 即使已经运行 。 |
| callback | [Phaser.Types.Cameras.Scene2D.CameraFadeCallback](/api/typedef/types-cameras-scene2d#camerafadecallback) | 是 |  | 将在此效果持续期间引用每个帧。 它会被发送两个参数: 引用相机和0到1之间的进度量, 说明效果有多完整 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为相机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 开始效果的相机。


**Fires:** [Phaser.Cameras.Scene2D.Events#event:FADE_IN_START](/api/event/cameras-scene2d-events#fade_in_start), [Phaser.Cameras.Scene2D.Events#event:FADE_OUT_START](/api/event/cameras-scene2d-events#fade_out_start)


> 源码：[src/cameras/2d/effects/Fade.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Fade.js#L178)  
引入版本：3.5.0


---

### update {#update}

#### \<instance> update(time, delta) {#instance-updatetime-delta}


**说明:**

此效果的主要更新环路。 自动由相机调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 请求动画框架或SetTimeout生成的当前时间戳 。 |
| delta | number | 否 | 三角洲时间,以ms计, 过去了,自上一个框架。 |


> 源码：[src/cameras/2d/effects/Fade.js#L237](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Fade.js#L237)  
引入版本：3.5.0


---

---
