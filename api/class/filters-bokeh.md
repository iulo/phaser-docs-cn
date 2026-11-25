# Bokeh {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-bokeh)

博基过滤器控制器

这个过滤控制器管理相机的bokeh效应.

博凯(Bokeh)是指模仿摄影技术创造浅深场的视觉效果,这种效果用来强调游戏的主题或动作,通过模糊背景或前缘元素,导致更浸润和视觉吸引人的经历,通过模拟外焦区域,给游戏图形带来深度感和现实感的渲染技术实现.

这种效果也可以用来产生倾斜的Shift效应,这是一种通过模糊除图像小区域以外的一切事物来创建微型效应的技术,这种效果是通过模糊上下元素来实现的,同时保持中心区域的重点.

此效果样本跨越一个区域。 为了避免在边缘丢失数据, 请使用 `controller.setPaddingOverride(null)` 自动垫下游戏对象, 或是 `camera.getPaddingWrapper(x)` 来放大相机 。

通过过滤列表组件,将波克效应添加到相机中:

```js
const camera = this.cameras.main;

camera.filters.internal.addBokeh();
camera.filters.external.addBokeh();
```

**构造函数**

`new Bokeh(camera, [radius], [amount], [contrast], [isTiltShift], [blurX], [blurY], [strength])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的摄像机。 |
| radius | number | 是 | 0.5 | 博克效应的半径. |
| amount | number | 是 | 1 | 博基效应的金额. |
| contrast | number | 是 | 0.2 | 博克效应的颜色对比. |
| isTiltShift | boolean | 是 | false | 这是波克还是斜移效应? |
| blurX | number | 是 | 1 | 如果倾斜的移动, 水平模糊的量 。 |
| blurY | number | 是 | 1 | 如果倾斜的 Shift , 垂直模糊的量 。 |
| strength | number | 是 | 1 | 如果斜移, 模糊的强度 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Bokeh.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Bokeh.js#L10)  
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

bokeh 效果的量。 这控制了模糊通道中采样的数量。 值高, 以额外的 GPU 工作为代价, 会产生密度更高、 更明显的 bokeh 。 此属性仅适用于标准bokeh 效果; 使用 `strength` 来调整倾斜移效果的强度 。


> 源码：[src/filters/Bokeh.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Bokeh.js#L82)  
引入版本：4.0.0


---

### blurX {#blurX}

#### blurX: number {#blurx-number}


**说明:**

如果倾斜的 Shift 效果控制水平模糊度 。

设置此值为非 Tilt Shift 效果将没有效果 。


> 源码：[src/filters/Bokeh.js#L117](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Bokeh.js#L117)  
引入版本：4.0.0


---

### blurY {#blurY}

#### blurY: number {#blury-number}


**说明:**

如果倾斜的 Shift 效果控制垂直模糊的量 。

设置此值为非 Tilt Shift 效果将没有效果 。


> 源码：[src/filters/Bokeh.js#L129](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Bokeh.js#L129)  
引入版本：4.0.0


---

### contrast {#contrast}

#### contrast: number {#contrast-number}


**说明:**

bokeh效果的颜色对比。 这控制了偏重区域与偏重区域之间的亮度差异。 更高的值会增加bokeh亮度及其周围的亮度对比, 使效果在视觉上更加明显 。


> 源码：[src/filters/Bokeh.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Bokeh.js#L95)  
引入版本：4.0.0


---

### isTiltShift {#isTiltShift}

#### isTiltShift: boolean {#istiltshift-boolean}


**说明:**

这是斜移效应还是标准bokeh效应?


> 源码：[src/filters/Bokeh.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Bokeh.js#L108)  
引入版本：4.0.0


---

### radius {#radius}

#### radius: number {#radius-number}


**说明:**

博克效应的半径.

这是一个浮点值, 半径0 将不会产生任何效果, 而半径1 将产生强烈的 bokeh 。 然而, 您可以超过这个值来获取更强的效果 。


> 源码：[src/filters/Bokeh.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Bokeh.js#L68)  
引入版本：4.0.0


---

### strength {#strength}

#### strength: number {#strength-number}


**说明:**

如果倾斜的 Shift 效果控制了模糊的强度 。

设置此值为非 Tilt Shift 效果将没有效果 。


> 源码：[src/filters/Bokeh.js#L141](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Bokeh.js#L141)  
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

返回此过滤器在渲染时所需的额外粘贴量, 以像素计 。 粘贴值会记录波克效应的延伸超过过滤相机的原始界限 。


**Overrides:** Phaser.Filters.Controller#getPadding


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 贴板矩形


> 源码：[src/filters/Bokeh.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Bokeh.js#L154)  
引入版本：4.0.0


---

---
