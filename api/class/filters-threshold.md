# Threshold {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-threshold)

阈值过滤控制器 。

此控制器管理一个阈值过滤器。 输入值被比作阈值或范围。 阈值以下的值被设定为 0, 阈值以上值被设定为 1。 值范围内的值被线性地插入 0 到 1 之间 。

这对于从梯度产生尖端效应,或者对产生二进制效应,都是有用的.

阈值为存储范围,有两边,每个边对每个通道都有值,介于0到1之间,如果两个边缘相同,则阈值没有内插,并且会输出0到1. 每个通道也可以反转.

通过过滤列表组件,将阈值效应添加到相机中:

```js
const camera = this.cameras.main;

camera.filters.internal.addThreshold();
camera.filters.external.addThreshold();
```

**构造函数**

`new Threshold(camera, [edge1], [edge2], [invert])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的摄像机。 |
| edge1 | number \| Array.\<number> | 是 | 0.5 | 阈值的第一个边缘。 这可能是 RGBA 频道的数组, 或者一个单一的号码, 用于所有 4 频道 。 |
| edge2 | number \| Array.\<number> | 是 | 0.5 | 阈值的第二个边缘。 这可能是 RGBA 频道的数组, 或者一个单一的数字来应用到所有 4 频道 。 |
| invert | boolean \| Array.\<boolean> | 是 | false | 是否每个频道都倒转。 这可能是 RGBA 频道的数组, 或者一个布尔来应用到所有 4 频道 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Threshold.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Threshold.js#L10)  
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

### edge1 {#edge1}

#### edge1: Array.\<number> {#edge1-arraynumber}


**说明:**

阈值的第一个边缘。 此边值包含每个通道的最低值 。


> 源码：[src/filters/Threshold.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Threshold.js#L54)  
引入版本：4.0.0


---

### edge2 {#edge2}

#### edge2: Array.\<number> {#edge2-arraynumber}


**说明:**

阈值的第二边。 这包含每个通道的最高值。 如果它与第一边相同, 阈值是一个单一值 。


> 源码：[src/filters/Threshold.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Threshold.js#L65)  
引入版本：4.0.0


---

### invert {#invert}

#### invert: Array.\<boolean> {#invert-arrayboolean}


**说明:**

是否每个信道都倒转。 当一个信道倒转时, 其输出会翻转, 通常输出0的值会变为输出1, 而反之亦然。 这适用于阈值结果的 RGBA 组件 。


> 源码：[src/filters/Threshold.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Threshold.js#L77)  
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

### setEdge {#setEdge}

#### \<instance> setEdge([edge1], [edge2]) {#instance-setedgeedge1-edge2}


**说明:**

设置阈值的边缘。 如果没有提供第二边, 则将设置为第一边 。

这保证了第一边缘不会大于第二边缘,它可能会在边缘之间互换通道来保证这一点.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| edge1 | number \| Array.\<number> | 是 | 0.5 | 阈值的第一个边缘。 这可能是 RGBA 频道的数组, 或者一个单一的号码, 用于所有 4 频道 。 |
| edge2 | number \| Array.\<number> | 是 | 0.5 | 阈值的第二个边缘。 这可能是 RGBA 频道的数组, 或者一个单一的数字来应用到所有 4 频道 。 |


**返回值:** [Phaser.Filters.Threshold](/api/class/filters-threshold) - 此阈值例.


> 源码：[src/filters/Threshold.js#L94](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Threshold.js#L94)  
引入版本：4.0.0


---

### setInvert {#setInvert}

#### \<instance> setInvert([invert]) {#instance-setinvertinvert}


**说明:**

设置阈值过滤器每个通道的反转状态。 当一个通道被反转时, 其输出会翻转: 输出0 的像素, 而输出1 的反转。 它可以用来创建负值或反转的每个通道的阈值效果。 如果不提供 `invert`, 所有通道默认为 `false` 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| invert | boolean \| Array.\<boolean> | 是 | false | 是否每个频道都倒转。 这可能是 RGBA 频道的数组, 或者一个布尔来应用到所有 4 频道 。 |


**返回值:** [Phaser.Filters.Threshold](/api/class/filters-threshold) - 此阈值例.


> 源码：[src/filters/Threshold.js#L150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Threshold.js#L150)  
引入版本：4.0.0


---

---
