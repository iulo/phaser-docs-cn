# Vignette {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-vignette)

维涅特滤镜控制器 。

这个控制器管理摄像机的阴极效应.

阴极效应是一种视觉技术,屏幕边缘,或游戏对象,逐渐变暗或模糊,产生类似帧的外观,这种效果用来吸引玩家的焦点向中心动作或主题,增强浸润,为游戏视觉提供影视或艺术品质.

这种滤波器支持彩色边框,以及有限的组合模式,以增强其结构力.

通过过滤列表组件,将 Vignette 效果添加到摄像机中:

```js
const camera = this.cameras.main;

camera.filters.internal.addVignette();
camera.filters.external.addVignette();
```

**构造函数**

`new Vignette(camera, [x], [y], [radius], [strength], [color], [blendMode])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的摄像机. |
| x | number | 是 | 0.5 | 阴极效应的横向偏移。 此值将正常化为 0 到 1 。 |
| y | number | 是 | 0.5 | 阴极效应的垂直偏移。 此值将正常化为 0 到 1 。 |
| radius | number | 是 | 0.5 | 阴极效应的半径。 此值已正常化到 0 到 1 之间 。 |
| strength | number | 是 | 0.5 | 阴阳效应的强度. |
| color | number \| string | [Phaser.Types.Display.InputColorObject](/api/typedef/types-display#inputcolorobject) | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0x000000" | 阴极效应的颜色,作为六进制码或颜色对象. |
| blendMode | number | 是 | "Phaser.BlendModes.NORMAL" | 与 vignette 混合模式。 仅支持 NORMAL、 ADD、 MULTIPLY 和 SCREEN 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Vignette.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Vignette.js#L11)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Filters.Controller](/api/class/filters-controller):**


 - [active](/api/class/filters-controller#active)
 - [allowBaseDraw](/api/class/filters-controller#allowBaseDraw)
 - [camera](/api/class/filters-controller#camera)
 - [currentPadding](/api/class/filters-controller#currentPadding)
 - [ignoreDestroy](/api/class/filters-controller#ignoreDestroy)
 - [paddingOverride](/api/class/filters-controller#paddingOverride)
 - [renderNode](/api/class/filters-controller#renderNode)




---

## 公开成员 {#public-members}

### blendMode {#blendMode}

#### blendMode: [Phaser.BlendModes](/api/namespace/blendmodes) {#blendmode-phaserblendmodes}


**说明:**

混合模式用于将阴毛颜色与输入相结合。 请注意, 仅支持 NORMAL、 ADD、 MULTIPLY 和 SCREEN 。


> 源码：[src/filters/Vignette.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Vignette.js#L111)  
引入版本：4.0.0


---

### color {#color}

#### color: [Phaser.Display.Color](/api/namespace/display-color) {#color-phaserdisplaycolor}


**说明:**

阴阳效应的颜色.


> 源码：[src/filters/Vignette.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Vignette.js#L102)  
引入版本：4.0.0


---

### radius {#radius}

#### radius: number {#radius-number}


**说明:**

阴极效应的半径。 此值已正常化到 0 到 1 之间 。


> 源码：[src/filters/Vignette.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Vignette.js#L82)  
引入版本：4.0.0


---

### strength {#strength}

#### strength: number {#strength-number}


**说明:**

阴极效应的强度。 更高的值在边缘产生更强烈、 不透明的阴极覆盖, 而较低的值则产生更微妙、更透明的效果。


> 源码：[src/filters/Vignette.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Vignette.js#L91)  
引入版本：4.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

阴极效应的横向偏移。 此值将正常化为 0 到 1 。


> 源码：[src/filters/Vignette.js#L64](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Vignette.js#L64)  
引入版本：4.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

阴极效应的垂直偏移。 此值将正常化为 0 到 1 。


> 源码：[src/filters/Vignette.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Vignette.js#L73)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Filters.Controller](/api/class/filters-controller):**


 - [destroy](/api/class/filters-controller#destroy)
 - [getPadding](/api/class/filters-controller#getPadding)
 - [getPaddingCeil](/api/class/filters-controller#getPaddingCeil)
 - [setActive](/api/class/filters-controller#setActive)
 - [setPaddingOverride](/api/class/filters-controller#setPaddingOverride)




---

## 公开方法 {#public-methods}

### setColor {#setColor}

#### \<instance> setColor(color) {#instance-setcolorcolor}


**说明:**

设置阴毛覆盖的颜色。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | number \| string | [Phaser.Types.Display.InputColorObject](/api/typedef/types-display#inputcolorobject) | [Phaser.Display.Color](/api/namespace/display-color) | 否 | 要设置的颜色。 注意将复制一个颜色对象, 而不是附加 。 |


**返回值:** [Phaser.Filters.Vignette](/api/class/filters-vignette) - 此过滤实例 。


> 源码：[src/filters/Vignette.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Vignette.js#L125)  
引入版本：4.0.0


---

---
