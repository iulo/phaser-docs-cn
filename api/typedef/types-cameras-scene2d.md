# Types.Cameras.Scene2D {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-cameras-scene2d)

## CameraConfig {#cameraconfig}

### \<static> CameraConfig {#static-cameraconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 名称 | string | 是 | "''" | 相机名称. |
| x | number | 是 | 0 | 相机视网的横向位置. |
| y | number | 是 | 0 | 相机视门的垂直位置. |
| width | number | 是 |  | 相机视网的宽度. |
| height | number | 是 |  | 摄像机的高度 |
| zoom | number | 是 | 1 | 相机默认缩放级别 。 |
| rotation | number | 是 | 0 | 相机的旋转,用弧度表示. |
| roundPixels | boolean | 是 | false | 摄像机在渲染前应该圆形像素吗? |
| scrollX | number | 是 | 0 | 相机的横向滚动位置 。 |
| scrollY | number | 是 | 0 | 相机的垂直滚动位置 。 |
| backgroundColor | false \| string | 是 | false | CSS 色彩字符串控制相机背景颜色 。 |
| bounds | object | 是 |  | 定义相机的界限。 |
| bounds.x | number | 是 | 0 | 摄像机左上角的距离 |
| bounds.y | number | 是 | 0 | 摄像机左上角的距离 |
| bounds.width | number | 是 |  | 相机的宽度 |
| bounds.height | number | 是 |  | 摄像机的高度 |

**类型**: object

**Member of**: Phaser.Types.Cameras.Scene2D
> 源码：[src/cameras/2d/typedefs/CameraConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/typedefs/CameraConfig.js#L1)  
引入版本：3.0.0

---

## CameraFadeCallback {#camerafadecallback}

### \<static> CameraFadeCallback {#static-camerafadecallback}

**类型**: function

**Member of**: Phaser.Types.Cameras.Scene2D
> 源码：[src/cameras/2d/typedefs/CameraFadeCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/typedefs/CameraFadeCallback.js#L1)  
引入版本：3.5.0

---

## CameraFlashCallback {#cameraflashcallback}

### \<static> CameraFlashCallback {#static-cameraflashcallback}

**类型**: function

**Member of**: Phaser.Types.Cameras.Scene2D
> 源码：[src/cameras/2d/typedefs/CameraFlashCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/typedefs/CameraFlashCallback.js#L1)  
引入版本：3.5.0

---

## CameraPaddingWrapper {#camerapaddingwrapper}

### \<static> CameraPaddingWrapper {#static-camerapaddingwrapper}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| padding | number | 否 | 相机两侧应用的粘贴量。 这可以调整相机的大小、 位置和滚动, 但相机PaddingWrapper 代理摘要 , 这样您就不需要考虑这些调整 。 |

**类型**: object

**Member of**: Phaser.Types.Cameras.Scene2D
> 源码：[src/cameras/2d/typedefs/CameraPaddingWrapper.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/typedefs/CameraPaddingWrapper.js#L1)  
引入版本：4.0.0

---

## CameraPanCallback {#camerapancallback}

### \<static> CameraPanCallback {#static-camerapancallback}

**类型**: function

**Member of**: Phaser.Types.Cameras.Scene2D
> 源码：[src/cameras/2d/typedefs/CameraPanCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/typedefs/CameraPanCallback.js#L1)  
引入版本：3.5.0

---

## CameraRotateCallback {#camerarotatecallback}

### \<static> CameraRotateCallback {#static-camerarotatecallback}

**类型**: function

**Member of**: Phaser.Types.Cameras.Scene2D
> 源码：[src/cameras/2d/typedefs/CameraRotateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/typedefs/CameraRotateCallback.js#L1)  
引入版本：3.23.0

---

## CameraShakeCallback {#camerashakecallback}

### \<static> CameraShakeCallback {#static-camerashakecallback}

**类型**: function

**Member of**: Phaser.Types.Cameras.Scene2D
> 源码：[src/cameras/2d/typedefs/CameraShakeCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/typedefs/CameraShakeCallback.js#L1)  
引入版本：3.5.0

---

## CameraZoomCallback {#camerazoomcallback}

### \<static> CameraZoomCallback {#static-camerazoomcallback}

**类型**: function

**Member of**: Phaser.Types.Cameras.Scene2D
> 源码：[src/cameras/2d/typedefs/CameraZoomCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/typedefs/CameraZoomCallback.js#L1)  
引入版本：3.11.0

---

## JSONCamera {#jsoncamera}

### \<static> JSONCamera {#static-jsoncamera}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 相机名称 |
| x | number | 否 | 相机的横向位置 |
| y | number | 否 | 相机的垂直位置 |
| width | number | 否 | 相机宽度大小 |
| height | number | 否 | 相机的高度大小 |
| zoom | number | 否 | 镜头的放大 |
| rotation | number | 否 | 相机的旋转 |
| roundPixels | boolean | 否 | 圆像素显示相机的状态 |
| scrollX | number | 否 | 相机的横向滚动 |
| scrollY | number | 否 | 相机的垂直滚动 |
| backgroundColor | string | 否 | 相机的背景颜色 |
| bounds | [Phaser.Types.Cameras.Scene2D.JSONCameraBounds](/api/typedef/types-cameras-scene2d#jsoncamerabounds) \| undefined | 是 | 镜头的界限 |

**类型**: object

**Member of**: Phaser.Types.Cameras.Scene2D
> 源码：[src/cameras/2d/typedefs/JSONCamera.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/typedefs/JSONCamera.js#L1)  
引入版本：3.0.0

---

## JSONCameraBounds {#jsoncamerabounds}

### \<static> JSONCameraBounds {#static-jsoncamerabounds}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 相机的横向位置 |
| y | number | 否 | 相机的垂直位置 |
| width | number | 否 | 相机宽度大小 |
| height | number | 否 | 相机的高度大小 |

**类型**: object

**Member of**: Phaser.Types.Cameras.Scene2D
> 源码：[src/cameras/2d/typedefs/JSONCameraBounds.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/typedefs/JSONCameraBounds.js#L1)  
引入版本：3.0.0

---

---
