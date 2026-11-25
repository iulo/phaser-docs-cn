# Shadow {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-shadow)

影影滤镜.

此过滤控制器管理相机的阴影效果 。

影子效应是一种视觉技术,通过增加更暗,抵消游戏对象,人物或环境下的淤积或形状来创造深度和现实主义的幻觉. 这些模拟的影子有助于增强视觉吸引力和浸润,使2D游戏世界显得更具活力和三维.

此效果样本跨越一个区域。 为了避免在边缘丢失数据, 请使用 `controller.setPaddingOverride(null)` 自动垫下游戏对象, 或是 `camera.getPaddingWrapper(x)` 来放大相机 。

通过过滤列表组件在相机中添加阴影效果:

```js
const camera = this.cameras.main;

camera.filters.internal.addShadow();
camera.filters.external.addShadow();
```

**构造函数**

`new Shadow(camera, [x], [y], [decay], [power], [color], [samples], [intensity])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的相机. |
| x | number | 是 | 0 | 横向抵消阴影效应. |
| y | number | 是 | 0 | 阴影效应的垂直抵消. |
| decay | number | 是 | 0.1 | 阴之衰减之量. |
| power | number | 是 | 1 | 阴之效之力. |
| color | number | 是 | "0x000000" | 阴之色,为六合之值. |
| samples | number | 是 | 6 | 阴影效应将运行的样本数量 。 |
| intensity | number | 是 | 1 | 阴之效之烈. |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Shadow.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Shadow.js#L10)  
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

阴影的颜色, 表示为十六进制的 RGB 值( 如红色的 `0xff0000` , 黑色的 `0x000000` ) 。 设置此属性可更新 WebGL 着色器所用的内部 `glcolor` 阵列 。


> 源码：[src/filters/Shadow.js#L138](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Shadow.js#L138)  
引入版本：4.0.0


---

### decay {#decay}

#### decay: number {#decay-number}


**说明:**

控制阴影在距离上消失的速度。 数值越低, 产生越长越渐进的阴影; 数值越高, 产生越短, 越集中的阴影。


> 源码：[src/filters/Shadow.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Shadow.js#L80)  
引入版本：4.0.0


---

### glcolor {#glcolor}

#### glcolor: Array.\<number> {#glcolor-arraynumber}


**说明:**

着色器使用的内部 WebGL颜色阵列。 将阴影颜色存储为 0 到 1 之间的正常 RGBA 浮点值。 此阵列在 `color` 属性设定时会自动更新 。


> 源码：[src/filters/Shadow.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Shadow.js#L100)  
引入版本：4.0.0


---

### intensity {#intensity}

#### intensity: number {#intensity-number}


**说明:**

整体阴影可见度的乘数。更高的值会产生更暗,更突出的阴影。


> 源码：[src/filters/Shadow.js#L122](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Shadow.js#L122)  
引入版本：4.0.0


---

### power {#power}

#### power: number {#power-number}


**说明:**

应用到阴影落下曲线上的缩写。 更高的值会产生更尖锐的阴影边缘; 较低的值会产生更柔软, 更分散的阴影 。


> 源码：[src/filters/Shadow.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Shadow.js#L90)  
引入版本：4.0.0


---

### samples {#samples}

#### samples: number {#samples-number}


**说明:**

阴影效应将运行的样本数量 。

其应是一个最小值为1,最高值为12的整数.


> 源码：[src/filters/Shadow.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Shadow.js#L111)  
引入版本：4.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

横向抵消阴影效应.


> 源码：[src/filters/Shadow.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Shadow.js#L62)  
引入版本：4.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

阴影效应的垂直抵消.


> 源码：[src/filters/Shadow.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Shadow.js#L71)  
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

返回此过滤器在渲染时所需的额外粘贴量, 以像素计。 粘贴值会记录扩展至过滤游戏对象的原始界限以外的阴影效果 。


**Overrides:** Phaser.Filters.Controller#getPadding


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 贴板矩形


> 源码：[src/filters/Shadow.js#L167](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Shadow.js#L167)  
引入版本：4.0.0


---

---
