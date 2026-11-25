# RotateTo {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/cameras-scene2d-effects-rotateto)

相机旋转效果,在指定时间内将相机顺利旋转到目标角度。

这种效果将旋转相机,使其视门以给定角度以弧度完成,在持续时间和指定的方便度内完成.

相机旋转总是根据相机的视门进行。默认情况下,旋转发生在视门中心。您可以根据`originX`和`originY`的属性来调整此功能。

旋转会影响此相机可见的_all_Game Objects的渲染。 然而, 它不会旋转相机的视门本身, 它始终是一个轴向矩形 。

只有相机被旋转。 它显示的物体没有受到影响, 即它们的位置不会改变 。

效果会在相机本身上发出几个事件,您也可以指定一个`onUpdate`调回,如果需要,每个帧都会在效果的持续时间里引用.

**构造函数**

`new RotateTo(camera)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 摄像机,这个效果正在采取行动。 |

---


**作用域**: static

> 源码：[src/cameras/2d/effects/RotateTo.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L13)  
引入版本：3.23.0

## 公开成员 {#public-members}

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#camera-phasercamerasscene2dcamera}


**说明:**

相机这个效果属于。


> 源码：[src/cameras/2d/effects/RotateTo.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L45)  
引入版本：3.23.0


---

### clockwise {#clockwise}

#### clockwise: boolean {#clockwise-boolean}


**说明:**

旋转是顺时针方向(`true`)还是逆时针方向(`false`)进行.


> 源码：[src/cameras/2d/effects/RotateTo.js#L153](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L153)  
引入版本：3.23.0


---

### current {#current}

#### current: number {#current-number}


**说明:**

旋转时的当前相机角度,以弧度表示.


> 源码：[src/cameras/2d/effects/RotateTo.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L86)  
引入版本：3.23.0


---

### destination {#destination}

#### destination: number {#destination-number}


**说明:**

将相机旋转到的目的地角度,以弧度表示.


> 源码：[src/cameras/2d/effects/RotateTo.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L95)  
引入版本：3.23.0


---

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

效果的持续时间,以毫秒计.


> 源码：[src/cameras/2d/effects/RotateTo.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L66)  
引入版本：3.23.0


---

### ease {#ease}

#### ease: function {#ease-function}


**说明:**

旋转时使用的易用功能。


> 源码：[src/cameras/2d/effects/RotateTo.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L104)  
引入版本：3.23.0


---

### isRunning {#isRunning}

#### isRunning: boolean {#isrunning-boolean}


**说明:**

效果是否积极运行?


> 源码：[src/cameras/2d/effects/RotateTo.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L55)  
引入版本：3.23.0


---

### progress {#progress}

#### progress: number {#progress-number}


**说明:**

如果正在运行此效果, 则当前进度将保持 0 (启动) 到 1 (结束) 之间的值 。


> 源码：[src/cameras/2d/effects/RotateTo.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L113)  
引入版本：3.23.0


---

### shortestPath {#shortestPath}

#### shortestPath: boolean {#shortestpath-boolean}


**说明:**

效果是否应该通过最短的角路径旋转到目的地角度 。


> 源码：[src/cameras/2d/effects/RotateTo.js#L162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L162)  
引入版本：3.23.0


---

### source {#source}

#### source: number {#source-number}


**说明:**

开始角度从弧度旋转相机。


> 源码：[src/cameras/2d/effects/RotateTo.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L77)  
引入版本：3.23.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这种效果,从镜头中释放出来.


> 源码：[src/cameras/2d/effects/RotateTo.js#L336](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L336)  
引入版本：3.23.0


---

### effectComplete {#effectComplete}

#### \<instance> effectComplete() {#instance-effectcomplete}


**说明:**

效果完成后内部调用.


> 源码：[src/cameras/2d/effects/RotateTo.js#L305](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L305)  
引入版本：3.23.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

重置此相机效果。 如果它之前运行过, 它会立即停止, 而不调用它的 onComplete 回调或释放事件 。


> 源码：[src/cameras/2d/effects/RotateTo.js#L321](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L321)  
引入版本：3.23.0


---

### start {#start}

#### \<instance> start(angle, [shortestPath], [duration], [ease], [force], [callback], [context]) {#instance-startangle-shortestpath-duration-ease-force-callback-context}


**说明:**

在整个期间和指定的方便范围内将相机旋转到给定角度。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| angle | number | 否 |  | 以弧度表示的目的地角旋转相机视图到. |
| shortestPath | boolean | 是 | false | 如果选中的话, 请将最短的距离拖到目的地。 这将调整目的地角度, 使其在起始角度的半转角之内 。 |
| duration | number | 是 | 1000 | 效果持续时间以毫秒计. |
| ease | string \| function | 是 | "'Linear'" | 易用。 可以是 Phaser 减速常数或自定义函数 。 |
| force | boolean | 是 | false | 强制旋转效果立即启动, 即使已经运行 。 |
| callback | [Phaser.Types.Cameras.Scene2D.CameraRotateCallback](/api/typedef/types-cameras-scene2d#camerarotatecallback) | 是 |  | 此调用符会在效果的持续时间里被引用到每个帧。 它被发送到三个参数: 引用相机, 0 到 1 之间的进度量, 表示效果的完成程度, 以及当前相机旋转 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为相机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 开始效果的相机。


**Fires:** [Phaser.Cameras.Scene2D.Events#event:ROTATE_START](/api/event/cameras-scene2d-events#rotate_start), [Phaser.Cameras.Scene2D.Events#event:ROTATE_COMPLETE](/api/event/cameras-scene2d-events#rotate_complete)


> 源码：[src/cameras/2d/effects/RotateTo.js#L172](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L172)  
引入版本：3.23.0


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


> 源码：[src/cameras/2d/effects/RotateTo.js#L252](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/RotateTo.js#L252)  
引入版本：3.23.0


---

---
