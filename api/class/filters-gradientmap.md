# GradientMap {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-gradientmap)

渐变映射过滤控制器 。

此控制器管理摄像机的渐变映射效果 。

渐变映射重映射图像使用 ColorRamp 。 图像在每个点转换成进度值, 并且该进度被评价为斜坡沿线的颜色 。

进度值通常为图像的亮度。 您可以使用 `colorFactor` 和 `color` 属性来自定义它 。

**构造函数**

`new GradientMap(camera, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 拥有这个过滤器的摄像机. |
| config | [Phaser.Types.Filters.GradientMapConfig](/api/typedef/types-filters#gradientmapconfig) | 是 | 渐变映射效果的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/GradientMap.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/GradientMap.js#L11)  
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

### alpha {#alpha}

#### alpha: number {#alpha-number}


**说明:**

梯度映射效果在原图像之上的混合强度,介于0(无效果,原图像完全可见)到1(完全梯度映射效果,原图像完全取代)之间.


> 源码：[src/filters/GradientMap.js#L140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/GradientMap.js#L140)  
引入版本：4.0.0


---

### color {#color}

#### color: Array.\<number> {#color-arraynumber}


**说明:**

RGBA 抵消 `colorFactor` 应用后直接添加到坡道进度的值。每个元素对应一个通道:红,绿,蓝,和α。例如,当相应的 `colorFactor` 条目是 `-1` 时,设置一个通道给 `1` , 有效反转了通道对进步值的贡献 。


> 源码：[src/filters/GradientMap.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/GradientMap.js#L85)  
引入版本：4.0.0


---

### colorFactor {#colorFactor}

#### colorFactor: Array.\<number> {#colorfactor-arraynumber}


**说明:**

RGBA 乘数应用于源图像的每个通道,以计算坡道进度值。结果被汇总。默认值为 `[ 0.3, 0.6, 0.1, 0 ]` 近似标准亮度加权,产生一个感知准确的灰度进度。为正常结果,将系数总和保持在1,或使用负值(以 `color` 抵消)来反转信道的贡献。


> 源码：[src/filters/GradientMap.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/GradientMap.js#L106)  
引入版本：4.0.0


---

### dither {#dither}

#### dither: boolean {#dither-boolean}


**说明:**

是否使用 Interleaved Gradient 噪声来抖动斜坡 。 这可以减少带宽, 但是如果图像后来被转换, 效果很容易丢失 。


> 源码：[src/filters/GradientMap.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/GradientMap.js#L73)  
引入版本：4.0.0


---

### ramp {#ramp}

#### ramp: [Phaser.Display.ColorRamp](/api/class/display-colorramp) {#ramp-phaserdisplaycolorramp}


**说明:**

用于重新显示图像的颜色Ramp。 每个像素的亮度( 或 `colorFactor` 和 `color` 的自定义进度值) 沿着这个斜坡向上查看, 以确定其输出颜色 。


> 源码：[src/filters/GradientMap.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/GradientMap.js#L62)  
引入版本：4.0.0


---

### unpremultiply {#unpremultiply}

#### unpremultiply: boolean {#unpremultiply-boolean}


**说明:**

是否在计算进度前输入不预先加乘。 这意味着透明颜色在完全亮度时被考虑。 通常需要 。


> 源码：[src/filters/GradientMap.js#L128](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/GradientMap.js#L128)  
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
