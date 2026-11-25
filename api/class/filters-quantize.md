# Quantize {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-quantize)

量化过滤控制器 。

这个控制器管理着相机上的量化效应.

量化可以减少图像中独特的颜色数量, 其依据是每个颜色通道的一定有限的步骤。 这有利于创建反演或分层化效果 。

基本的量化将每个信道分解为若干个 `steps`。 这些步骤通常都是常规的。 您可以通过改变信道的 `gamma` 值来将其偏移到上下。 您可以调整最小的步数, 从而调整所有后续步骤, 并使用 `offset` 。

量化在 RGBA 或 HSVA 空间中进行。步骤、 伽马 和 抵消总是以相同的顺序应用, 但取决于颜色模式, 它们要么应用到 `[ red, green, blue, alpha ]` 或 `[ hue, saturation, value, alpha ]` 。

输出可能可选地被抖动,以消除带状,并产生使用中还有更多颜色的幻觉.

**构造函数**

`new Quantize(camera, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 拥有这个过滤器的相机. |
| config | [Phaser.Types.Filters.QuantizeConfig](/api/typedef/types-filters#quantizeconfig) | 是 | 用于量化效果的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Quantize.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Quantize.js#L10)  
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

### dither {#dither}

#### dither: boolean {#dither-boolean}


**说明:**

是否将 dither 应用到 quantization 中, 创建一个更平滑的输出, 并减少颜色 。


> 源码：[src/filters/Quantize.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Quantize.js#L142)  
引入版本：4.0.0


---

### gamma {#gamma}

#### gamma: Array.\<number> {#gamma-arraynumber}


**说明:**

伽玛曲线应用于输入通道。 这有助于在暗或光区域中排列细微的先后次序 。

在 RGBA 模式中, RGB 通道可以被同样的处理。 在 HSVA 模式中, 您可能想要将伽马应用到仅仅的值和饱和度通道中 。


> 源码：[src/filters/Quantize.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Quantize.js#L86)  
引入版本：4.0.0


---

### mode {#mode}

#### mode: number {#mode-number}


**说明:**

0是使用色空间,0是RGBA,1是HSVA. 使用HSVA控制许多光度/饱和度较低的色调.

当模式改变为 HSVA 时, `steps` , `gamma` 和 `offset` 则适用于 haue, 饱和度, 值, 和 alpha 通道。 否则, 它们是不变的 。


> 源码：[src/filters/Quantize.js#L126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Quantize.js#L126)  
引入版本：4.0.0


---

### offset {#offset}

#### offset: Array.\<number> {#offset-arraynumber}


**说明:**

偏移以应用到定量时的通道。 这一点主要用于滑动 HSVA 定量的 hue 角度 。


> 源码：[src/filters/Quantize.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Quantize.js#L108)  
引入版本：4.0.0


---

### steps {#steps}

#### steps: Array.\<number> {#steps-arraynumber}


**说明:**

将每个频道分成多少个步骤.

将最后一个位置降为1经常有用,因为它在RGBA和HSVA中都是α,α经常在开或关.

在RGBA模式中,前3频道(RGB)很可能应该相同,除非有风格需要. 在HSVA模式中,第一个频道(H)可能应该有很多区分来区分不同的色调,而第二和第三频道(SV)可能需要较少的台阶.


> 源码：[src/filters/Quantize.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Quantize.js#L59)  
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

---
