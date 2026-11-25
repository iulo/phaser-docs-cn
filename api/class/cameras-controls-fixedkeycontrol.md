# FixedKeyControl {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/cameras-controls-fixedkeycontrol)

固定的钥匙摄像机控制器

这使得您可以使用键盘键控制摄像机的移动和缩放。 与 `SmoothedKeyControl` 不同, 此控制可以直接应用移动和缩放, 并且每次更新勾选时都不会放松或平滑。 摄像机在按下键时立即响应, 并在发布时立即停止, 使其适合基于网格或精确摄像机导航 。

```javascript
var camControl = new FixedKeyControl({
    camera: this.cameras.main,
    left: cursors.left,
    right: cursors.right,
    speed: float OR { x: 0, y: 0 }
});
```

运动是准确的,没有“舒缓”应用。

您必须调用此控制器的 `update` 方法 。

**构造函数**

`new FixedKeyControl(config)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Cameras.Controls.FixedKeyControlConfig](/api/typedef/types-cameras-controls#fixedkeycontrolconfig) | 否 | 固定键控制配置对象 。 |

---


**作用域**: static

> 源码：[src/cameras/controls/FixedKeyControl.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L10)  
引入版本：3.0.0

## 公开成员 {#public-members}

### active {#active}

#### active: boolean {#active-boolean}


**说明:**

控制控制器是否更新摄像机的旗帜 。


> 源码：[src/cameras/controls/FixedKeyControl.js#L190](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L190)  
引入版本：3.0.0


---

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#camera-phasercamerasscene2dcamera}


**说明:**

控制器会更新的摄像机


> 源码：[src/cameras/controls/FixedKeyControl.js#L46](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L46)  
引入版本：3.0.0


---

### down {#down}

#### down: [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) {#down-phaserinputkeyboardkey}


**说明:**

将摄像机移到下方的按键。


> 源码：[src/cameras/controls/FixedKeyControl.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L86)  
引入版本：3.0.0


---

### left {#left}

#### left: [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) {#left-phaserinputkeyboardkey}


**说明:**

将左侧的摄像机移动的按键 。


> 源码：[src/cameras/controls/FixedKeyControl.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L56)  
引入版本：3.0.0


---

### maxZoom {#maxZoom}

#### maxZoom: number {#maxzoom-number}


**说明:**

放大时摄像机会达到最大的放大值。


> 源码：[src/cameras/controls/FixedKeyControl.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L136)  
引入版本：3.53.0


---

### minZoom {#minZoom}

#### minZoom: number {#minzoom-number}


**说明:**

缩放后,摄像机将达到最小的缩放值。


> 源码：[src/cameras/controls/FixedKeyControl.js#L126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L126)  
引入版本：3.53.0


---

### right {#right}

#### right: [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) {#right-phaserinputkeyboardkey}


**说明:**

将摄像机右移的按键 。


> 源码：[src/cameras/controls/FixedKeyControl.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L66)  
引入版本：3.0.0


---

### speedX {#speedX}

#### speedX: number {#speedx-number}


**说明:**

摄像机滚动时的水平速度,以每毫秒像素计.


> 源码：[src/cameras/controls/FixedKeyControl.js#L146](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L146)  
引入版本：3.0.0


---

### speedY {#speedY}

#### speedY: number {#speedy-number}


**说明:**

摄像机滚动的垂直速度,以每毫秒像素计.


> 源码：[src/cameras/controls/FixedKeyControl.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L156)  
引入版本：3.0.0


---

### up {#up}

#### up: [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) {#up-phaserinputkeyboardkey}


**说明:**

将摄像机移动的按键。


> 源码：[src/cameras/controls/FixedKeyControl.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L76)  
引入版本：3.0.0


---

### zoomIn {#zoomIn}

#### zoomIn: [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) {#zoomin-phaserinputkeyboardkey}


**说明:**

将摄像机放大的按键 。


> 源码：[src/cameras/controls/FixedKeyControl.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L96)  
引入版本：3.0.0


---

### zoomOut {#zoomOut}

#### zoomOut: [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) {#zoomout-phaserinputkeyboardkey}


**说明:**

将摄像机放大的按键。


> 源码：[src/cameras/controls/FixedKeyControl.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L106)  
引入版本：3.0.0


---

### zoomSpeed {#zoomSpeed}

#### zoomSpeed: number {#zoomspeed-number}


**说明:**

在每次更新时按下 `zoomIn` 或 `zoomOut` 键时,摄像机缩放级别的变化量。 与滚动速度不同, 此值不会被三角形时间缩放 。


> 源码：[src/cameras/controls/FixedKeyControl.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L116)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此键控制, 取消其摄像机和键引用以允许垃圾收集 。 此键控制在被销毁后无法再次使用 。


> 源码：[src/cameras/controls/FixedKeyControl.js#L308](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L308)  
引入版本：3.0.0


---

### setCamera {#setCamera}

#### \<instance> setCamera(camera) {#instance-setcameracamera}


**说明:**

将此键控制器绑在摄像机上 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 将键控制器绑定的摄像机 。 |


**返回值:** [Phaser.Cameras.Controls.FixedKeyControl](/api/class/cameras-controls-fixedkeycontrol) - 此键控制实例 。


> 源码：[src/cameras/controls/FixedKeyControl.js#L230](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L230)  
引入版本：3.0.0


---

### start {#start}

#### \<instance> start() {#instance-start}


**说明:**

启动键控制器运行, 条件是它已经链接到摄像机上 。


**返回值:** [Phaser.Cameras.Controls.FixedKeyControl](/api/class/cameras-controls-fixedkeycontrol) - 此键控制实例 。


> 源码：[src/cameras/controls/FixedKeyControl.js#L200](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L200)  
引入版本：3.0.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

停止此键控制器运行。 呼叫 `start` 重新开始 。


**返回值:** [Phaser.Cameras.Controls.FixedKeyControl](/api/class/cameras-controls-fixedkeycontrol) - 此键控制实例 。


> 源码：[src/cameras/controls/FixedKeyControl.js#L215](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L215)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update(delta) {#instance-updatedelta}


**说明:**

应用按下控制键对摄像机的结果.

你必须把每个步骤都叫这个,它不是自动的。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/cameras/controls/FixedKeyControl.js#L247](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/FixedKeyControl.js#L247)  
引入版本：3.0.0


---

---
