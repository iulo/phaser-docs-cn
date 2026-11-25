# Blur {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-blur)

模糊过滤器控制器 。

此过滤器控制器管理模糊效果 。

高斯模糊是高斯函数模糊图像的结果,是广泛使用的效果,一般是为了减少图像噪音和细节,这种模糊技术的视觉效果是光滑模糊的类似通过半透明屏幕观看图像,与偏焦镜头产生的波克效应或通常照明下物体的阴影明显不同.

此效果样本跨越一个区域。 为了避免在边缘丢失数据, 请使用 `controller.setPaddingOverride(null)` 自动垫下游戏对象, 或是 `camera.getPaddingWrapper(x)` 来放大相机 。

通过过滤列表组件将模糊效果添加到相机中:

```js
const camera = this.cameras.main;

camera.filters.internal.addBlur();
camera.filters.external.addBlur();
```

**构造函数**

`new Blur(camera, [quality], [x], [y], [strength], [color], [steps])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的摄像机。 |
| quality | number | 是 | 0 | 模糊效果的质量。 可以是低质量的 0, 中质量的 1, 也可以是高质量的 2。 |
| x | number | 是 | 2 | 模糊效果的横向抵消. |
| y | number | 是 | 2 | 模糊效果的垂直偏移. |
| strength | number | 是 | 1 | 模糊效应的强度. |
| color | number | 是 | "0xffffff" | 模糊的颜色,作为六进制值. |
| steps | number | 是 | 4 | 运行模糊效果的步骤数。 此值应该总是整数 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Blur.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blur.js#L10)  
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

### color {#color}

#### color: number {#color-number}


**说明:**

模糊效果的颜色, 作为装填的 RGB 六角整数( 如 `0xff0000` 表示红色) 。 这可以将模糊的样本打上, 允许有色的开花式效果 。 默认为白色( `0xffffff`) , 产生无色的中性模糊 。


> 源码：[src/filters/Blur.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blur.js#L154)  
引入版本：4.0.0


---

### glcolor {#glcolor}

#### glcolor: Array.\<number> {#glcolor-arraynumber}


**说明:**

内部gl颜色阵列.


> 源码：[src/filters/Blur.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blur.js#L121)  
引入版本：4.0.0


---

### quality {#quality}

#### quality: number {#quality-number}


**说明:**

模糊效果的质量.

这可以是:

0 低质量 1 中质量 2 高品质

质量越高,使用的遮蔽器越复杂,处理时间也越多,用于GPU计算最终模糊度,这个值与`steps`值结合使用,因为一个值对另一个值有直接影响.

尽量保持这个值低,同时仍然实现游戏所需的预期效果.


> 源码：[src/filters/Blur.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blur.js#L60)  
引入版本：4.0.0


---

### steps {#steps}

#### steps: number {#steps-number}


**说明:**

运行模糊效果的步数 。

此值应该始终是整数.

值越高,越平滑,模糊度越高,但代价是指数性地增加gl操作.

保持尽可能低的数, 同时仍然寻找正确的游戏。


> 源码：[src/filters/Blur.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blur.js#L135)  
引入版本：4.0.0


---

### strength {#strength}

#### strength: number {#strength-number}


**说明:**

模糊效果的强度。 此值与 x 和 y 相乘, 以及确定全模糊半径的步数相乘。 增加此值可以使模糊度更加清晰, 而无需改变质量或步骤数 。


> 源码：[src/filters/Blur.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blur.js#L108)  
引入版本：4.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

模糊效果的横向偏移。 这控制了 x 轴上模糊样本点之间的距离。 更大的值会增加模糊水平的分布 。


> 源码：[src/filters/Blur.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blur.js#L84)  
引入版本：4.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

模糊效果的垂直抵消。 这会控制沿 y 轴模糊样本点之间的距离。 更大的值会垂直地增加模糊的分布 。


> 源码：[src/filters/Blur.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blur.js#L96)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Filters.Controller](/api/class/filters-controller):**


 - [destroy](/api/class/filters-controller#destroy)
 - [getPaddingCeil](/api/class/filters-controller#getPaddingCeil)
 - [setActive](/api/class/filters-controller#setActive)
 - [setPaddingOverride](/api/class/filters-controller#setPaddingOverride)




---

## 公开方法 {#public-methods}

### getPadding {#getPadding}

#### \<instance> getPadding() {#instance-getpadding}


**说明:**

返回此过滤器在渲染时所需的额外粘贴量, 以像素计。 这说明模糊的半径会延伸到过滤过的游戏对象的原边界之外 。


**Overrides:** Phaser.Filters.Controller#getPadding


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 贴板矩形


> 源码：[src/filters/Blur.js#L183](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blur.js#L183)  
引入版本：4.0.0


---

---
