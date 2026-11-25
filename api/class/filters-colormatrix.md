# ColorMatrix {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-colormatrix)

色彩Matrix 过滤控制器 。

此过滤控制器管理摄像机的颜色矩阵效果 。

色彩矩阵效应是一种视觉技术,它涉及使用数学矩阵来操纵图像或场景的颜色,这一过程可以调整色调,饱和度,亮度,对比度,使开发者能够在游戏中创建各种风格外观或情绪设置. 常见的应用包括模拟不同的照明条件,应用色彩滤镜,或者实现特定的视觉风格.

彩色Matrix效果通过过滤列表组件添加到摄像机中:

```js
const camera = this.cameras.main;

const cmFilter = camera.filters.internal.addColorMatrix();
camera.filters.external.addColorMatrix();

// To set the matrix values:
cmFilter.colorMatrix.sepia();
```

**构造函数**

`new ColorMatrix(camera)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 拥有这个过滤器的摄像机. |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/ColorMatrix.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ColorMatrix.js#L11)  
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

### colorMatrix {#colorMatrix}

#### colorMatrix: [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) {#colormatrix-phaserdisplaycolormatrix}


**说明:**

颜色矩阵用于此效果。 使用此选项应用预设或自定义的颜色转换, 如 sepia, 灰度, 饱和度, 亮度, 色调旋转等 。


> 源码：[src/filters/ColorMatrix.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ColorMatrix.js#L49)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Filters.Controller](/api/class/filters-controller):**


 - [getPadding](/api/class/filters-controller#getPadding)
 - [getPaddingCeil](/api/class/filters-controller#getPaddingCeil)
 - [setActive](/api/class/filters-controller#setActive)
 - [setPaddingOverride](/api/class/filters-controller#setPaddingOverride)




---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此过滤器, 释放所有引用和资源 。


**重写:** Phaser.Filters.Controller#销毁


> 源码：[src/filters/ColorMatrix.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ColorMatrix.js#L61)  
引入版本：4.0.0


---

---
