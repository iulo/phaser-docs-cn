# Wipe {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-wipe)

擦拭过滤器控制器 。

这个控制器管理着相机的擦拭效果.

擦拭或揭示效果是一种视觉技术,它逐渐在游戏中发现或隐藏元素,如图像,文本或场景过渡. 这种效果常用于创造进化感,揭示隐藏的内容,或者提供游戏状态间平滑和视觉吸引人的过渡.

您可以同时设置擦拭效果的方向和轴。 下列组合是可能的:

* 左到右:方向 0,轴 0

* 右到左:方向 1,轴 0

* 从上到下:方向 1, 轴 1

* 从下到上:方向 0,轴 1

由您自己设定 `progress` 值, 例如通过 Tween, 以转换效果 。

通过过滤列表组件将擦拭效果添加到相机中:

```js
const camera = this.cameras.main;
camera.filters.internal.addWipe();
camera.filters.external.addWipe();
```

**构造函数**

`new Wipe(camera, [wipeWidth], [direction], [axis], [reveal], [wipeTexture])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的相机. |
| wipeWidth | number | 是 | 0.1 | 擦拭效果的宽度。 此值在 0 到 1 之间正常化 。 |
| direction | number | 是 | 0 | 擦拭效果的方向。 要么 0( 左到右, 要么上到下) 要么 1( 右到左, 要么下到上)。 设置与轴属性结合 。 |
| axis | number | 是 | 0 | 擦拭效果的轴。 要么0( X) 要么1( Y) 。 设定与方向属性结合 。 |
| reveal | number | 是 | 0 | 这是显示(1)还是擦拭( 0) 效果 ? 启示显示在擦拭区域中的输入; 擦拭显示在未擦拭区域中的输入 。 |
| wipeTexture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 | "'__DEFAULT'" | 输入纹理未显示时使用的纹理或纹理密钥。默认纹理为空白。 使用另一个纹理进行擦拭过渡 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Wipe.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L11)  
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

### axis {#axis}

#### axis: number {#axis-number}


**说明:**

擦拭效果的轴。 要么0( X) 要么1( Y) 。 设定与方向属性结合 。


> 源码：[src/filters/Wipe.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L93)  
引入版本：4.0.0


---

### direction {#direction}

#### direction: number {#direction-number}


**说明:**

擦拭效果的方向。 要么 0( 左到右, 要么上到下) 要么 1( 右到左, 要么下到上)。 设置与轴属性结合 。


> 源码：[src/filters/Wipe.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L84)  
引入版本：4.0.0


---

### progress {#progress}

#### progress: number {#progress-number}


**说明:**

擦拭效果的进展。 此值已正常化到 0 到 1 之间 。

调整此值以进行擦拭过渡( 例如通过 Tween) 。


> 源码：[src/filters/Wipe.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L63)  
引入版本：4.0.0


---

### reveal {#reveal}

#### reveal: number {#reveal-number}


**说明:**

这是显示(1)还是擦拭( 0) 效果 ? 启示显示在擦拭区域中的输入; 擦拭显示在未擦拭区域中的输入 。


> 源码：[src/filters/Wipe.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L102)  
引入版本：4.0.0


---

### wipeTexture {#wipeTexture}

#### wipeTexture: [Phaser.Textures.Texture](/api/class/textures-texture) {#wipetexture-phasertexturestexture}


**说明:**

用于删除输入的纹理。 默认纹理“ __DEFAULT” 是空白的。 使用另一个纹理来进行擦拭过渡 。


> 源码：[src/filters/Wipe.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L113)  
引入版本：4.0.0


---

### wipeWidth {#wipeWidth}

#### wipeWidth: number {#wipewidth-number}


**说明:**

擦拭效果的宽度。 此值在 0 到 1 之间正常化 。


> 源码：[src/filters/Wipe.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L74)  
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

### setBottomToTop {#setBottomToTop}

#### \<instance> setBottomToTop() {#instance-setbottomtotop}


**说明:**

设置擦拭效果以运行到下至上 。


**返回值:** [Phaser.Filters.Wipe](/api/class/filters-wipe) - - 这个过滤器


> 源码：[src/filters/Wipe.js#L187](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L187)  
引入版本：4.0.0


---

### setLeftToRight {#setLeftToRight}

#### \<instance> setLeftToRight() {#instance-setlefttoright}


**说明:**

设置擦拭效果以向左向右运行 。


**返回值:** [Phaser.Filters.Wipe](/api/class/filters-wipe) - - 这个过滤器


> 源码：[src/filters/Wipe.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L145)  
引入版本：4.0.0


---

### setProgress {#setProgress}

#### \<instance> setProgress(value) {#instance-setprogressvalue}


**说明:**

设定擦拭效果的进度, 控制过渡的推进程度。 0 值意味着过渡尚未开始, 1 表示它已经完成。 您通常会通过调制驱动, 而不是直接设置它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 进展,正常到0 -1范围. |


**返回值:** [Phaser.Filters.Wipe](/api/class/filters-wipe) - - 这个过滤器


> 源码：[src/filters/Wipe.js#L262](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L262)  
引入版本：4.0.0


---

### setRevealEffect {#setRevealEffect}

#### \<instance> setRevealEffect() {#instance-setrevealeffect}


**说明:**

配置此过滤器作为显示效果运行, 输入会随着过渡过程的进行而逐渐被解开。 同时将纹理重排到默认的空白纹理中, 并将 `progress` 重排到 0。 使用 `setWipeEffect` 来进行相反的行为 。


**返回值:** [Phaser.Filters.Wipe](/api/class/filters-wipe) - - 这个过滤器


> 源码：[src/filters/Wipe.js#L217](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L217)  
引入版本：4.0.0


---

### setRightToLeft {#setRightToLeft}

#### \<instance> setRightToLeft() {#instance-setrighttoleft}


**说明:**

设置擦拭效果为右向左运行 。


**返回值:** [Phaser.Filters.Wipe](/api/class/filters-wipe) - - 这个过滤器


> 源码：[src/filters/Wipe.js#L159](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L159)  
引入版本：4.0.0


---

### setTexture {#setTexture}

#### \<instance> setTexture([texture]) {#instance-settexturetexture}


**说明:**

设置用于删除输入的纹理。 默认纹理是空白的, 所以输入只是隐藏 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 | "'__DEFAULT'" | 用于去除输入的区域的纹理或纹理密钥. |


**返回值:** [Phaser.Filters.Wipe](/api/class/filters-wipe) - - 这个过滤器


> 源码：[src/filters/Wipe.js#L236](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L236)  
引入版本：4.0.0


---

### setTopToBottom {#setTopToBottom}

#### \<instance> setTopToBottom() {#instance-settoptobottom}


**说明:**

设置擦拭效果以运行到上到下.


**返回值:** [Phaser.Filters.Wipe](/api/class/filters-wipe) - - 这个过滤器


> 源码：[src/filters/Wipe.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L173)  
引入版本：4.0.0


---

### setWipeEffect {#setWipeEffect}

#### \<instance> setWipeEffect() {#instance-setwipeeffect}


**说明:**

配置此过滤器作为擦拭效果运行, 输入会随着过渡过程的进行而去掉。 同时将 `progress` 重置为 0。 使用 `setRevealEffect` 来进行相反的行为 。


**返回值:** [Phaser.Filters.Wipe](/api/class/filters-wipe) - - 这个过滤器


> 源码：[src/filters/Wipe.js#L201](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L201)  
引入版本：4.0.0


---

### setWipeWidth {#setWipeWidth}

#### \<instance> setWipeWidth(width) {#instance-setwipewidthwidth}


**说明:**

设置擦拭效果的宽度 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 擦拭效果的宽度。 此值在 0 到 1 之间正常化 。 |


**返回值:** [Phaser.Filters.Wipe](/api/class/filters-wipe) - - 这个过滤器


> 源码：[src/filters/Wipe.js#L127](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Wipe.js#L127)  
引入版本：4.0.0


---

---
