# Zoom {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/cameras-scene2d-effects-zoom)

摄像机缩放效果 。

此效果将摄像机的放大级从当前值平稳地放大到指定时间内的目标放大值。 使用它来创建电影的放大或放大的转换, 将玩家的注意力集中在一个感兴趣的点上, 或在切片时产生像缓慢的放大这样的戏剧效果 。

效果与Phaser的放松系统融合,允许任何内置的放松功能(或自定义的)控制插值曲线,通过`Camera.zoomTo`访问,而不是直接被即时化.

效果会在摄像机本身上发出几个事件,您也可以指定一个`onUpdate`调回,如果需要,每个帧都会在效果的持续时间里引用.

**构造函数**

`new Zoom(camera)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 摄像机,这个效果正在采取行动。 |

---


**作用域**: static

> 源码：[src/cameras/2d/effects/Zoom.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Zoom.js#L12)  
引入版本：3.11.0

## 公开成员 {#public-members}

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#camera-phasercamerasscene2dcamera}


**说明:**

摄像机这个效果属于。


> 源码：[src/cameras/2d/effects/Zoom.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Zoom.js#L40)  
引入版本：3.11.0


---

### destination {#destination}

#### destination: number {#destination-number}


**说明:**

目的地缩放值 。


> 源码：[src/cameras/2d/effects/Zoom.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Zoom.js#L81)  
引入版本：3.11.0


---

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

效果的持续时间,以毫秒计.


> 源码：[src/cameras/2d/effects/Zoom.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Zoom.js#L61)  
引入版本：3.11.0


---

### ease {#ease}

#### ease: function {#ease-function}


**说明:**

缩放时使用的易功能 。


> 源码：[src/cameras/2d/effects/Zoom.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Zoom.js#L90)  
引入版本：3.11.0


---

### isRunning {#isRunning}

#### isRunning: boolean {#isrunning-boolean}


**说明:**

效果是否积极运行?


> 源码：[src/cameras/2d/effects/Zoom.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Zoom.js#L50)  
引入版本：3.11.0


---

### progress {#progress}

#### progress: number {#progress-number}


**说明:**

如果正在运行此效果, 则该结果将保留当前进度的百分比, 值在 0 到 1 之间 。


> 源码：[src/cameras/2d/effects/Zoom.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Zoom.js#L99)  
引入版本：3.11.0


---

### source {#source}

#### source: number {#source-number}


**说明:**

初始缩放值 。


> 源码：[src/cameras/2d/effects/Zoom.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Zoom.js#L72)  
引入版本：3.11.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这种效果,从镜头中释放出来.


> 源码：[src/cameras/2d/effects/Zoom.js#L278](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Zoom.js#L278)  
引入版本：3.11.0


---

### effectComplete {#effectComplete}

#### \<instance> effectComplete() {#instance-effectcomplete}


**说明:**

效果完成后内部调用.


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:ZOOM_COMPLETE](/api/event/cameras-scene2d-events#zoom_complete)


> 源码：[src/cameras/2d/effects/Zoom.js#L246](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Zoom.js#L246)  
引入版本：3.11.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

重置此摄像机效果。 如果它之前运行过, 它会立即停止, 而不调用它的 onComplete 回调或释放事件 。


> 源码：[src/cameras/2d/effects/Zoom.js#L263](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Zoom.js#L263)  
引入版本：3.11.0


---

### start {#start}

#### \<instance> start(zoom, [duration], [ease], [force], [callback], [context]) {#instance-startzoom-duration-ease-force-callback-context}


**说明:**

这种效果将使摄像机在规定的持续时间和方便程度上放大到给定的尺度.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| zoom | number | 否 |  | 目标镜头放大值。 |
| duration | number | 是 | 1000 | 效果持续时间以毫秒计. |
| ease | string \| function | 是 | "'Linear'" | 缩放的易用性。 可以是 Phaser 减速常数或自定义函数 。 |
| force | boolean | 是 | false | 强制放大效果立即启动, 即使已经运行 。 |
| callback | [Phaser.Types.Cameras.Scene2D.CameraZoomCallback](/api/typedef/types-cameras-scene2d#camerazoomcallback) | 是 |  | 此调用符会在效果的持续时间里被引用到每个帧。 它被发送三个参数: 引用摄像机, 0 到 1 之间的进度量, 表示效果的完成程度, 以及当前摄像机缩放值 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为摄像机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 开始效果的摄像机。


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:ZOOM_START](/api/event/cameras-scene2d-events#zoom_start), [Phaser.Cameras.Scene2D.Events#event:ZOOM_COMPLETE](/api/event/cameras-scene2d-events#zoom_complete)


> 源码：[src/cameras/2d/effects/Zoom.js#L140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Zoom.js#L140)  
引入版本：3.11.0


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


> 源码：[src/cameras/2d/effects/Zoom.js#L204](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Zoom.js#L204)  
引入版本：3.11.0


---

---
