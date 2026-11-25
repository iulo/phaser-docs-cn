# Flash {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/cameras-scene2d-effects-flash)

摄像机闪光效应.

此效果将在指定时间内将摄像机的视窗闪到给定的颜色.

只有摄像机的视口被闪烁。 其显示的对象没有受到影响, 即其颜色不会改变 。

效果会在摄像机本身上发出几个事件,您也可以指定一个`onUpdate`调回,在效果持续期间,如果需要,每个帧都会引用.

**构造函数**

`new Flash(camera)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 摄像机,这个效果正在采取行动。 |

---


**作用域**: static

> 源码：[src/cameras/2d/effects/Flash.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Flash.js#L11)  
引入版本：3.5.0

## 公开成员 {#public-members}

### alpha {#alpha}

#### alpha: number {#alpha-number}


**说明:**

闪光效果中使用的α通道值。 值在 0 到 1 之间 。


> 源码：[src/cameras/2d/effects/Flash.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Flash.js#L101)  
引入版本：3.5.0


---

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#camera-phasercamerasscene2dcamera}


**说明:**

摄像机这个效果属于。


> 源码：[src/cameras/2d/effects/Flash.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Flash.js#L36)  
引入版本：3.5.0


---

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

效果的持续时间,以毫秒计.


> 源码：[src/cameras/2d/effects/Flash.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Flash.js#L57)  
引入版本：3.5.0


---

### isRunning {#isRunning}

#### isRunning: boolean {#isrunning-boolean}


**说明:**

效果是否积极运行?


> 源码：[src/cameras/2d/effects/Flash.js#L46](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Flash.js#L46)  
引入版本：3.5.0


---

### progress {#progress}

#### progress: number {#progress-number}


**说明:**

如果正在运行此效果, 则该结果将保留当前进度的百分比, 值在 0 到 1 之间 。


> 源码：[src/cameras/2d/effects/Flash.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Flash.js#L111)  
引入版本：3.5.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这种效果,从镜头中释放出来.


> 源码：[src/cameras/2d/effects/Flash.js#L322](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Flash.js#L322)  
引入版本：3.5.0


---

### effectComplete {#effectComplete}

#### \<instance> effectComplete() {#instance-effectcomplete}


**说明:**

效果完成后内部调用.


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:FLASH_COMPLETE](/api/event/cameras-scene2d-events#flash_complete)


> 源码：[src/cameras/2d/effects/Flash.js#L289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Flash.js#L289)  
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


> 源码：[src/cameras/2d/effects/Flash.js#L251](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Flash.js#L251)  
引入版本：3.5.0


---

### postRenderWebGL {#postRenderWebGL}

#### \<instance> postRenderWebGL() {#instance-postrenderwebgl}


**说明:**

由WebGL制片人内部召集.


**返回值:** boolean - 如果效果应引向渲染器,则使用`true`,否则使用`false`.


> 源码：[src/cameras/2d/effects/Flash.js#L276](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Flash.js#L276)  
引入版本：3.5.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

重置此摄像机效果。 如果它之前运行过, 它会立即停止, 而不调用它的 onComplete 回调或释放事件 。


> 源码：[src/cameras/2d/effects/Flash.js#L307](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Flash.js#L307)  
引入版本：3.5.0


---

### start {#start}

#### \<instance> start([duration], [red], [green], [blue], [force], [callback], [context]) {#instance-startduration-red-green-blue-force-callback-context}


**说明:**

将摄像机在指定时间内闪到或从给定颜色闪出。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| duration | number | 是 | 250 | 效果持续时间以毫秒计. |
| red | number | 是 | 255 | 将红色通道闪向的金额。 0 到 255 之间的数值 。 |
| green | number | 是 | 255 | 将绿色通道闪向的金额, 数值在 0 到 255 之间 。 |
| blue | number | 是 | 255 | 向蓝色通道闪烁的金额, 数值在 0 到 255 之间 。 |
| force | boolean | 是 | false | 强制效果立即启动, 即使已经运行 。 |
| callback | [Phaser.Types.Cameras.Scene2D.CameraFlashCallback](/api/typedef/types-cameras-scene2d#cameraflashcallback) | 是 |  | 将在此效果持续期间引用每个帧。 它会被发送两个参数: 引用摄像机和0到1之间的进度量, 说明效果有多完整 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为摄像机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 开始效果的摄像机。


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:FLASH_START](/api/event/cameras-scene2d-events#flash_start), [Phaser.Cameras.Scene2D.Events#event:FLASH_COMPLETE](/api/event/cameras-scene2d-events#flash_complete)


> 源码：[src/cameras/2d/effects/Flash.js#L163](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Flash.js#L163)  
引入版本：3.5.0


---

### update {#update}

#### \<instance> update(time, delta) {#instance-updatetime-delta}


**说明:**

此效果的主要更新循环。 自动由摄像机调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 请求动画框架或SetTimeout生成的当前时间戳 。 |
| delta | number | 否 | 三角洲时间,以ms计, 过去了,自上一个框架。 |


> 源码：[src/cameras/2d/effects/Flash.js#L216](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Flash.js#L216)  
引入版本：3.5.0


---

---
