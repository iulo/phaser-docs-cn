# Shake {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/cameras-scene2d-effects-shake)

摄像机摇晃效应.

此效果会以一个随机量来震动摄像机的视图,以指定的强度,每个帧为界.

只有摄像机查看端被移动。 它显示的物体没有受到影响, 即它们的位置不会改变 。

效果会在摄像机本身上发出几个事件,您也可以指定一个`onUpdate`调回,如果需要,每个帧都会在效果的持续时间里引用.

**构造函数**

`new Shake(camera)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 摄像机,这个效果正在采取行动。 |

---


**作用域**: static

> 源码：[src/cameras/2d/effects/Shake.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Shake.js#L12)  
引入版本：3.5.0

## 公开成员 {#public-members}

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#camera-phasercamerasscene2dcamera}


**说明:**

摄像机这个效果属于。


> 源码：[src/cameras/2d/effects/Shake.js#L37](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Shake.js#L37)  
引入版本：3.5.0


---

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

效果的持续时间,以毫秒计.


> 源码：[src/cameras/2d/effects/Shake.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Shake.js#L58)  
引入版本：3.5.0


---

### intensity {#intensity}

#### intensity: [Phaser.Math.Vector2](/api/class/math-vector2) {#intensity-phasermathvector2}


**说明:**

效果的强度。 使用小浮点数。 效果开始时默认为 0.05。 这是一个矢量2 对象, 您可以独立控制 x 和 y 之间的摇动强度。 您可以修改这个值, 而效果是活跃的, 以创建更多不同的摇动效果 。


> 源码：[src/cameras/2d/effects/Shake.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Shake.js#L69)  
引入版本：3.5.0


---

### isRunning {#isRunning}

#### isRunning: boolean {#isrunning-boolean}


**说明:**

效果是否积极运行?


> 源码：[src/cameras/2d/effects/Shake.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Shake.js#L47)  
引入版本：3.5.0


---

### progress {#progress}

#### progress: number {#progress-number}


**说明:**

如果正在运行此效果, 则该结果将保留当前进度的百分比, 值在 0 到 1 之间 。


> 源码：[src/cameras/2d/effects/Shake.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Shake.js#L80)  
引入版本：3.5.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这种效果,从镜头中释放出来.


> 源码：[src/cameras/2d/effects/Shake.js#L297](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Shake.js#L297)  
引入版本：3.5.0


---

### effectComplete {#effectComplete}

#### \<instance> effectComplete() {#instance-effectcomplete}


**说明:**

效果完成后内部调用.


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:SHAKE_COMPLETE](/api/event/cameras-scene2d-events#shake_complete)


> 源码：[src/cameras/2d/effects/Shake.js#L259](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Shake.js#L259)  
引入版本：3.5.0


---

### preRender {#preRender}

#### \<instance> preRender() {#instance-prerender}


**说明:**

预降步骤用于此效果,由摄像机自动调用.


> 源码：[src/cameras/2d/effects/Shake.js#L198](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Shake.js#L198)  
引入版本：3.5.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

重置此摄像机效果。 如果它之前运行过, 它会立即停止, 而不调用它的 onComplete 回调或释放事件 。


> 源码：[src/cameras/2d/effects/Shake.js#L279](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Shake.js#L279)  
引入版本：3.5.0


---

### start {#start}

#### \<instance> start([duration], [intensity], [force], [callback], [context]) {#instance-startduration-intensity-force-callback-context}


**说明:**

在特定期间,通过给定的强度来摇动摄像机。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| duration | number | 是 | 100 | 效果持续时间以毫秒计. |
| intensity | number \| [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 0.05 | 摇动的强度. |
| force | boolean | 是 | false | 强制摇动效果立即启动, 即使已经运行 。 |
| callback | [Phaser.Types.Cameras.Scene2D.CameraShakeCallback](/api/typedef/types-cameras-scene2d#camerashakecallback) | 是 |  | 将在此效果持续期间引用每个帧。 它会被发送两个参数: 引用摄像机和0到1之间的进度量, 说明效果有多完整 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为摄像机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 开始效果的摄像机。


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:SHAKE_START](/api/event/cameras-scene2d-events#shake_start), [Phaser.Cameras.Scene2D.Events#event:SHAKE_COMPLETE](/api/event/cameras-scene2d-events#shake_complete)


> 源码：[src/cameras/2d/effects/Shake.js#L143](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Shake.js#L143)  
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


> 源码：[src/cameras/2d/effects/Shake.js#L212](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Shake.js#L212)  
引入版本：3.5.0


---

---
