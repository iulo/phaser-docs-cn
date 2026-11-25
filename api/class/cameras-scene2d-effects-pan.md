# Pan {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/cameras-scene2d-effects-pan)

摄像机潘效应.

这种效果将滚动相机,使其视港中心在指定目的地,持续时间和指定的方便度完成.

只有相机滚动被移动。 它显示的物体没有受到影响, 即它们的位置不会改变 。

效果会在相机本身上发出几个事件,您也可以指定一个`onUpdate`调回,如果需要,每个帧都会在效果的持续时间里引用.

**构造函数**

`new Pan(camera)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 摄像机,这个效果正在采取行动。 |

---


**作用域**: static

> 源码：[src/cameras/2d/effects/Pan.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Pan.js#L13)  
引入版本：3.11.0

## 公开成员 {#public-members}

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#camera-phasercamerasscene2dcamera}


**说明:**

相机这个效果属于。


> 源码：[src/cameras/2d/effects/Pan.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Pan.js#L39)  
引入版本：3.11.0


---

### current {#current}

#### current: [Phaser.Math.Vector2](/api/class/math-vector2) {#current-phasermathvector2}


**说明:**

相机的缩放调整卷轴坐标,在平板机中重新计算每个帧,以说明当前相机缩放级别。在插入源卷轴位置和目的地卷轴位置时,作为中间值使用。


> 源码：[src/cameras/2d/effects/Pan.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Pan.js#L80)  
引入版本：3.11.0


---

### destination {#destination}

#### destination: [Phaser.Math.Vector2](/api/class/math-vector2) {#destination-phasermathvector2}


**说明:**

目的地滚动坐标可以把相机装到


> 源码：[src/cameras/2d/effects/Pan.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Pan.js#L91)  
引入版本：3.11.0


---

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

效果的持续时间,以毫秒计.


> 源码：[src/cameras/2d/effects/Pan.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Pan.js#L60)  
引入版本：3.11.0


---

### ease {#ease}

#### ease: function {#ease-function}


**说明:**

锅锅中要使用的易用功能.


> 源码：[src/cameras/2d/effects/Pan.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Pan.js#L100)  
引入版本：3.11.0


---

### isRunning {#isRunning}

#### isRunning: boolean {#isrunning-boolean}


**说明:**

效果是否积极运行?


> 源码：[src/cameras/2d/effects/Pan.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Pan.js#L49)  
引入版本：3.11.0


---

### progress {#progress}

#### progress: number {#progress-number}


**说明:**

如果正在运行此效果, 则该结果将保留当前进度的百分比, 值在 0 到 1 之间 。


> 源码：[src/cameras/2d/effects/Pan.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Pan.js#L109)  
引入版本：3.11.0


---

### source {#source}

#### source: [Phaser.Math.Vector2](/api/class/math-vector2) {#source-phasermathvector2}


**说明:**

开始滚动坐标 将相机从。


> 源码：[src/cameras/2d/effects/Pan.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Pan.js#L71)  
引入版本：3.11.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这种效果,从镜头中释放出来.


> 源码：[src/cameras/2d/effects/Pan.js#L304](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Pan.js#L304)  
引入版本：3.11.0


---

### effectComplete {#effectComplete}

#### \<instance> effectComplete() {#instance-effectcomplete}


**说明:**

效果完成后内部调用.


**Fires:** [Phaser.Cameras.Scene2D.Events#event:PAN_COMPLETE](/api/event/cameras-scene2d-events#pan_complete)


> 源码：[src/cameras/2d/effects/Pan.js#L272](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Pan.js#L272)  
引入版本：3.11.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

重置此相机效果。 如果它之前运行过, 它会立即停止, 而不调用它的 onComplete 回调或释放事件 。


> 源码：[src/cameras/2d/effects/Pan.js#L289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Pan.js#L289)  
引入版本：3.11.0


---

### start {#start}

#### \<instance> start(x, y, [duration], [ease], [force], [callback], [context]) {#instance-startx-y-duration-ease-force-callback-context}


**说明:**

这种效果将滚动相机,使其视港中心在指定目的地,持续时间和指定的方便度完成.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 目的地x坐标滚动镜头视门中心到. |
| y | number | 否 |  | 目标 Y 坐标滚动相机视门中心到 。 |
| duration | number | 是 | 1000 | 效果持续时间以毫秒计. |
| ease | string \| function | 是 | "'Linear'" | 锅的易用性。 可以是任何 Phaser 减速常数或自定义函数 。 |
| force | boolean | 是 | false | 强迫锅效果立即启动, 即使已经运行了 。 |
| callback | [Phaser.Types.Cameras.Scene2D.CameraPanCallback](/api/typedef/types-cameras-scene2d#camerapancallback) | 是 |  | 此调用符会在效果的持续时间里被引用到每个帧。 它被发送四个参数: 引用相机, 表示效果完成程度的0到1 之间的进度量, 当前相机滚动x坐标和当前相机滚动y坐标 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为相机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 开始效果的相机。


**Fires:** [Phaser.Cameras.Scene2D.Events#event:PAN_START](/api/event/cameras-scene2d-events#pan_start), [Phaser.Cameras.Scene2D.Events#event:PAN_COMPLETE](/api/event/cameras-scene2d-events#pan_complete)


> 源码：[src/cameras/2d/effects/Pan.js#L150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Pan.js#L150)  
引入版本：3.11.0


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


> 源码：[src/cameras/2d/effects/Pan.js#L219](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/effects/Pan.js#L219)  
引入版本：3.11.0


---

---
