# SmoothedKeyControl {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/cameras-controls-smoothedkeycontrol)

滑动的密钥控制器。

这样您就可以使用定义的密钥控制相机的移动和缩放。 与固定相机控制器不同, 您也可以提供加速、 拖动和 maxSpeed 的物理值来进行平滑效果 。

```javascript
var controlConfig = {
    camera: this.cameras.main,
    left: cursors.left,
    right: cursors.right,
    up: cursors.up,
    down: cursors.down,
    zoomIn: this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.Q),
    zoomOut: this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.E),
    zoomSpeed: 0.02,
    acceleration: 0.06,
    drag: 0.0005,
    maxSpeed: 1.0
};
```

您必须调用此控制器的 `update` 方法 。

**构造函数**

`new SmoothedKeyControl(config)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Cameras.Controls.SmoothedKeyControlConfig](/api/typedef/types-cameras-controls#smoothedkeycontrolconfig) | 否 | 平滑密钥控制配置对象 。 |

---


**作用域**: static

> 源码：[src/cameras/controls/SmoothedKeyControl.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L10)  
引入版本：3.0.0

## 公开成员 {#public-members}

### accelX {#accelX}

#### accelX: number {#accelx-number}


**说明:**

当一个方向键被扣住时,水平加速适用于镜头的运动.


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L148](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L148)  
引入版本：3.0.0


---

### accelY {#accelY}

#### accelY: number {#accely-number}


**说明:**

当一个方向键被扣住时,垂直加速适用于相机的运动.


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L158)  
引入版本：3.0.0


---

### active {#active}

#### active: boolean {#active-boolean}


**说明:**

控制控制器是否更新相机的旗帜 。


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L280](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L280)  
引入版本：3.0.0


---

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#camera-phasercamerasscene2dcamera}


**说明:**

控制器会更新的相机


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L48)  
引入版本：3.0.0


---

### down {#down}

#### down: [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) {#down-phaserinputkeyboardkey}


**说明:**

将摄像机移到下方的按键。


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L88)  
引入版本：3.0.0


---

### dragX {#dragX}

#### dragX: number {#dragx-number}


**说明:**

水平拖曳在相机移动时应用到它.


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L181](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L181)  
引入版本：3.0.0


---

### dragY {#dragY}

#### dragY: number {#dragy-number}


**说明:**

移动时垂直拖曳应用到相机上.


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L191](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L191)  
引入版本：3.0.0


---

### left {#left}

#### left: [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) {#left-phaserinputkeyboardkey}


**说明:**

将左侧的相机移动的按键 。


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L58)  
引入版本：3.0.0


---

### maxSpeedX {#maxSpeedX}

#### maxSpeedX: number {#maxspeedx-number}


**说明:**

相机可以达到的最大水平速度.


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L214](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L214)  
引入版本：3.0.0


---

### maxSpeedY {#maxSpeedY}

#### maxSpeedY: number {#maxspeedy-number}


**说明:**

相机可达到的最大垂直速度.


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L224](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L224)  
引入版本：3.0.0


---

### maxZoom {#maxZoom}

#### maxZoom: number {#maxzoom-number}


**说明:**

放大时摄像机会达到最大的放大值。


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L138](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L138)  
引入版本：3.53.0


---

### minZoom {#minZoom}

#### minZoom: number {#minzoom-number}


**说明:**

缩放后,相机将达到最小的缩放值。


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L128](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L128)  
引入版本：3.53.0


---

### right {#right}

#### right: [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) {#right-phaserinputkeyboardkey}


**说明:**

将相机右移的按键 。


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L68)  
引入版本：3.0.0


---

### up {#up}

#### up: [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) {#up-phaserinputkeyboardkey}


**说明:**

将摄像机移动的按键。


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L78)  
引入版本：3.0.0


---

### zoomIn {#zoomIn}

#### zoomIn: [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) {#zoomin-phaserinputkeyboardkey}


**说明:**

将相机放大的按键 。


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L98)  
引入版本：3.0.0


---

### zoomOut {#zoomOut}

#### zoomOut: [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) {#zoomout-phaserinputkeyboardkey}


**说明:**

将相机放大的按键。


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L108)  
引入版本：3.0.0


---

### zoomSpeed {#zoomSpeed}

#### zoomSpeed: number {#zoomspeed-number}


**说明:**

如果按下`zoomIn`或`zoomOut`键,相机会放大的速度.


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L118)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁此密钥控制 。


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L480](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L480)  
引入版本：3.0.0


---

### setCamera {#setCamera}

#### \<instance> setCamera(camera) {#instance-setcameracamera}


**说明:**

将此密钥控制器绑在相机上 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 将密钥控制器绑定的相机 。 |


**返回值:** [Phaser.Cameras.Controls.SmoothedKeyControl](/api/class/cameras-controls-smoothedkeycontrol) - 此密钥控制实例 。


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L320](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L320)  
引入版本：3.0.0


---

### start {#start}

#### \<instance> start() {#instance-start}


**说明:**

启动密钥控制器运行, 条件是它已经链接到相机上 。


**返回值:** [Phaser.Cameras.Controls.SmoothedKeyControl](/api/class/cameras-controls-smoothedkeycontrol) - 此密钥控制实例 。


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L290](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L290)  
引入版本：3.0.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

停止此密钥控制器运行。 呼叫 `start` 重新开始 。


**返回值:** [Phaser.Cameras.Controls.SmoothedKeyControl](/api/class/cameras-controls-smoothedkeycontrol) - 此密钥控制实例 。


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L305](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L305)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update(delta) {#instance-updatedelta}


**说明:**

应用按下控制键对相机的结果.

你必须把每个步骤都叫这个,它不是自动的。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/cameras/controls/SmoothedKeyControl.js#L337](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/SmoothedKeyControl.js#L337)  
引入版本：3.0.0


---

---
