# Pixelate {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-pixelate)

位素过滤控制器 。

此过滤控制器管理相机的像素效应. 象素效应是一种视觉技术,它故意降低图像的分辨率或细节,形成由大型,可见像素组成的块状或镶嵌外观,这种效果可用于结构化目的,作为回溯游戏的致敬,或作为遮蔽游戏中某些元素的手段,比如在过渡期间或审查特定内容.

通过过滤列表组件,将像素酸效应添加到相机中:

```js
const camera = this.cameras.main;
camera.filters.internal.addPixelate();
```

**构造函数**

`new Pixelate(camera, [amount])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的摄像机。 |
| amount | number | 是 | 1 | 应用的像素量 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Pixelate.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Pixelate.js#L10)  
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

### amount {#amount}

#### amount: number {#amount-number}


**说明:**

应用的像素量 。

像素的大小等于2+这个量.


> 源码：[src/filters/Pixelate.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Pixelate.js#L44)  
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
