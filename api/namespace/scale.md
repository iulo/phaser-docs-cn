# Phaser.Scale {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/scale)

Scope: 
static
> 源码：[src/scale/index.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/index.js#L10)  


## 静态函数 {#static-functions}

- [ScaleManager](/api/class/scale-scalemanager)
## 静态函数 {#static-functions-1}

- [Center](/api/namespace/scale-center)
- [Events](/api/namespace/scale-events)
- [Orientation](/api/namespace/scale-orientation)
- [ScaleModes](/api/namespace/scale-scalemodes)
- [Zoom](/api/namespace/scale-zoom)
## 静态函数 {#static-functions-2}

### CenterType {#CenterType}

#### CenterType {#centertype}


**说明:**

Phaser 缩放管理器常数,用于游戏画布的中枢.

要了解每种模式都做些什么,请参见[Phaser.Scale.Center](/api/namespace/scale-center).


> 源码：[src/scale/const/CENTER_CONST.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/CENTER_CONST.js#L15)  
引入版本：3.16.0


---

### OrientationType {#OrientationType}

#### OrientationType {#orientationtype}


**说明:**

Phaser 方向的缩放管理器常数.

要了解每种模式都做些什么,请参见[Phaser.Scale.Orientation](/api/namespace/scale-orientation).


> 源码：[src/scale/const/ORIENTATION_CONST.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/ORIENTATION_CONST.js#L15)  
引入版本：3.16.0


---

### ScaleModeType {#ScaleModeType}

#### ScaleModeType {#scalemodetype}


**说明:**

用于不同可选比例模式的 Phaser 比例管理器常数 。

要了解每种模式都做些什么,请参见[Phaser.Scale.ScaleModes](/api/namespace/scale-scalemodes).


> 源码：[src/scale/const/SCALE_MODE_CONST.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/SCALE_MODE_CONST.js#L15)  
引入版本：3.16.0


---

### ZoomType {#ZoomType}

#### ZoomType {#zoomtype}


**说明:**

缩放模式的 Phaser 缩放管理器常数 。

要了解每种模式都做些什么,请参见[Phaser.Scale.Zoom](/api/namespace/scale-zoom).


> 源码：[src/scale/const/ZOOM_CONST.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/ZOOM_CONST.js#L15)  
引入版本：3.16.0


---

## 静态函数 {#static-functions-3}

### CENTER_BOTH {#CENTER_BOTH}

#### CENTER_BOTH: number {#center_both-number}


**说明:**

游戏画布在母版内部横向和纵向都以中心为中心,要做到这一点,母版必须有一个可以计算而不是空的界限.

居中是通过设置游戏画布的左侧边距和顶端属性来实现的,并且不考虑您可能应用的任何其他 CSS 样式.


> 源码：[src/scale/const/CENTER_CONST.js#L38](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/CENTER_CONST.js#L38)  
引入版本：3.16.0


---

### CENTER_HORIZONTALLY {#CENTER_HORIZONTALLY}

#### CENTER_HORIZONTALLY: number {#center_horizontally-number}


**说明:**

游戏画布在父公司内部水平中心。 要做到这一点,父公司必须有一个可以计算而不是空的界限。

居中是通过设置游戏画布的边距左侧属性来实现的,并且不考虑您可能应用过的任何其他 CSS 样式.


> 源码：[src/scale/const/CENTER_CONST.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/CENTER_CONST.js#L52)  
引入版本：3.16.0


---

### CENTER_VERTICALLY {#CENTER_VERTICALLY}

#### CENTER_VERTICALLY: number {#center_vertically-number}


**说明:**

游戏画布在母版内垂直中心,要做到这一点,母版必须有一个可以计算而不是空的界限.

居中是通过设置游戏画布的边距顶端属性实现的,不考虑您可能应用的任何其他 CSS 样式.


> 源码：[src/scale/const/CENTER_CONST.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/CENTER_CONST.js#L66)  
引入版本：3.16.0


---

### ENVELOP {#ENVELOP}

#### ENVELOP: number {#envelop-number}


**说明:**

宽度和高度会自动调整, 使大小覆盖整个目标区域, 同时保持宽度比。 这可能会比目标大小更远 。


> 源码：[src/scale/const/SCALE_MODE_CONST.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/SCALE_MODE_CONST.js#L71)  
引入版本：3.16.0


---

### EXPAND {#EXPAND}

#### EXPAND: number {#expand-number}


**说明:**

Canvas的可见区域被调整大小,以适应所有可用的_parent_空间,如RESIZE模式,并缩放画布大小以适应像FIT模式一样的可见区域内部.


> 源码：[src/scale/const/SCALE_MODE_CONST.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/SCALE_MODE_CONST.js#L92)  
引入版本：3.80.0


---

### FIT {#FIT}

#### FIT: number {#fit-number}


**说明:**

宽度和高度会自动调整,以适应给定目标区域,同时保持宽度比。视宽度比而定,在区域内可能有一些空间没有覆盖。


> 源码：[src/scale/const/SCALE_MODE_CONST.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/SCALE_MODE_CONST.js#L59)  
引入版本：3.16.0


---

### HEIGHT_CONTROLS_WIDTH {#HEIGHT_CONTROLS_WIDTH}

#### HEIGHT_CONTROLS_WIDTH: number {#height_controls_width-number}


**说明:**

宽度根据高度自动调整.


> 源码：[src/scale/const/SCALE_MODE_CONST.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/SCALE_MODE_CONST.js#L49)  
引入版本：3.16.0


---

### LANDSCAPE {#LANDSCAPE}

#### LANDSCAPE: string {#landscape-string}


**说明:**

主要景观导向.


> 源码：[src/scale/const/ORIENTATION_CONST.js#L27](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/ORIENTATION_CONST.js#L27)  
引入版本：3.16.0


---

### MAX_ZOOM {#MAX_ZOOM}

#### MAX_ZOOM: number {#max_zoom-number}


**说明:**

根据将适合父游戏的最大乘法大小计算放大值,如果没有设定父游戏,则计算浏览器窗口。


> 源码：[src/scale/const/ZOOM_CONST.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/ZOOM_CONST.js#L57)  
引入版本：3.16.0


---

### NO_CENTER {#NO_CENTER}

#### NO_CENTER: number {#no_center-number}


**说明:**

游戏画布不是以 Phaser 居于父方内部。 您仍可以通过 CSS 居于中心 。


> 源码：[src/scale/const/CENTER_CONST.js#L27](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/CENTER_CONST.js#L27)  
引入版本：3.16.0


---

### NO_ZOOM {#NO_ZOOM}

#### NO_ZOOM: number {#no_zoom-number}


**说明:**

游戏画布不会被Phaser放大.


> 源码：[src/scale/const/ZOOM_CONST.js#L27](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/ZOOM_CONST.js#L27)  
引入版本：3.16.0


---

### NONE {#NONE}

#### NONE: number {#none-number}


**说明:**

完全没有缩放。 画布被设定为游戏配置和 Phaser 中给出的大小, 之后不会再次更改。 如果您通过 CSS 或直接通过代码更改画布大小, 那么您需要调用 Scale Managementers `resize` 方法来给出新的尺寸, 否则输入事件会停止工作 。


> 源码：[src/scale/const/SCALE_MODE_CONST.js#L27](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/SCALE_MODE_CONST.js#L27)  
引入版本：3.16.0


---

### PORTRAIT {#PORTRAIT}

#### PORTRAIT: string {#portrait-string}


**说明:**

初画像方向.


> 源码：[src/scale/const/ORIENTATION_CONST.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/ORIENTATION_CONST.js#L47)  
引入版本：3.16.0


---

### RESIZE {#RESIZE}

#### RESIZE: number {#resize-number}


**说明:**

彩虹的大小被调整,以适应所有可用的_parent_空间,而不论宽度比.


> 源码：[src/scale/const/SCALE_MODE_CONST.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/SCALE_MODE_CONST.js#L82)  
引入版本：3.16.0


---

### WIDTH_CONTROLS_HEIGHT {#WIDTH_CONTROLS_HEIGHT}

#### WIDTH_CONTROLS_HEIGHT: number {#width_controls_height-number}


**说明:**

高度根据宽度自动调整.


> 源码：[src/scale/const/SCALE_MODE_CONST.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/SCALE_MODE_CONST.js#L39)  
引入版本：3.16.0


---

### ZOOM_2X {#ZOOM_2X}

#### ZOOM_2X: number {#zoom_2x-number}


**说明:**

游戏画布将由Phaser放大2x.


> 源码：[src/scale/const/ZOOM_CONST.js#L37](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/ZOOM_CONST.js#L37)  
引入版本：3.16.0


---

### ZOOM_4X {#ZOOM_4X}

#### ZOOM_4X: number {#zoom_4x-number}


**说明:**

游戏布面将由Phaser放大4x.


> 源码：[src/scale/const/ZOOM_CONST.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/ZOOM_CONST.js#L47)  
引入版本：3.16.0


---

---
