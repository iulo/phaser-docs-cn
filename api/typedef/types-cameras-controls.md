# Types.Cameras.Controls {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-cameras-controls)

## FixedKeyControlConfig {#fixedkeycontrolconfig}

### \<static> FixedKeyControlConfig {#static-fixedkeycontrolconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 |  | 控制器会更新的相机 |
| left | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 是 |  | 将左侧的相机移动的按键 。 |
| right | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 是 |  | 将相机右移的按键 。 |
| up | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 是 |  | 将摄像机移动的按键。 |
| down | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 是 |  | 将摄像机移到下方的按键。 |
| zoomIn | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 是 |  | 将相机放大的按键 。 |
| zoomOut | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 是 |  | 将相机放大的按键。 |
| zoomSpeed | number | 是 | 0.01 | 如果按下`zoomIn`或`zoomOut`键,相机会放大的速度. |
| speed | number \| Object | 是 | 0 | 相机的横向和纵向速度会移动. |
| minZoom | number | 是 | 0.001 | 缩放后,相机将达到最小的缩放值。 |
| maxZoom | number | 是 | 1000 | 放大时摄像机会达到最大的放大值。 |

**类型**: object

**Member of**: Phaser.Types.Cameras.Controls
> 源码：[src/cameras/controls/typedefs/FixedKeyControlConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/typedefs/FixedKeyControlConfig.js#L1)  
引入版本：3.0.0

---

## SmoothedKeyControlConfig {#smoothedkeycontrolconfig}

### \<static> SmoothedKeyControlConfig {#static-smoothedkeycontrolconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 |  | 控制器会更新的相机 |
| left | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 是 |  | 将左侧的相机移动的按键 。 |
| right | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 是 |  | 将相机右移的按键 。 |
| up | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 是 |  | 将摄像机移动的按键。 |
| down | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 是 |  | 将摄像机移到下方的按键。 |
| zoomIn | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 是 |  | 将相机放大的按键 。 |
| zoomOut | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 是 |  | 将相机放大的按键。 |
| zoomSpeed | number | 是 | 0.01 | 如果按下`zoomIn`或`zoomOut`键,相机会放大的速度. |
| acceleration | number \| Object | 是 | 0 | 相机的横向和纵向加速会移动. |
| drag | number \| Object | 是 | 0 | 水平拖曳和垂直拖曳在相机移动时应用. |
| maxSpeed | number \| Object | 是 | 0 | 相机的最大水平和垂直速度会移动. |
| minZoom | number | 是 | 0.001 | 缩放后,相机将达到最小的缩放值。 |
| maxZoom | number | 是 | 1000 | 放大时摄像机会达到最大的放大值。 |

**类型**: object

**Member of**: Phaser.Types.Cameras.Controls
> 源码：[src/cameras/controls/typedefs/SmoothedKeyControlConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/controls/typedefs/SmoothedKeyControlConfig.js#L1)  
引入版本：3.0.0

---

---
