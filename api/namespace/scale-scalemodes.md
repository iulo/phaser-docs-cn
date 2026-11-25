# Phaser.Scale.ScaleModes {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/scale-scalemodes)

Scope: 
static
> 源码：[src/scale/const/SCALE_MODE_CONST.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/SCALE_MODE_CONST.js#L7)  
引入版本：3.16.0

## 静态函数 {#static-functions}

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

### NONE {#NONE}

#### NONE: number {#none-number}


**说明:**

完全没有缩放。 画布被设定为游戏配置和 Phaser 中给出的大小, 之后不会再次更改。 如果您通过 CSS 或直接通过代码更改画布大小, 那么您需要调用 Scale Managementers `resize` 方法来给出新的尺寸, 否则输入事件会停止工作 。


> 源码：[src/scale/const/SCALE_MODE_CONST.js#L27](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/const/SCALE_MODE_CONST.js#L27)  
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

---
