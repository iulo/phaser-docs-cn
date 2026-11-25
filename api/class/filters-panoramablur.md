# PanoramaBlur {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-panoramablur)

全景Blur过滤控制器。

此过滤控制器管理摄像机的全景Blur效果 。

PanoramaBlur 是模糊全景图像的过滤器。 用于像图像光一样的过滤器, 将全景图像作为环境图。 模糊度将长方形地图当作球体, 并应用靠近柱子的重扭曲来获取正确结果。 您不应该将其用于一般目的模糊 。

效果可能非常缓慢,因为它使用一个网格的样本。 样本总数等于 samplesX * samplesY。 这可以非常高,非常快, 所以在增加这些值时要小心。 它们不需要太高, 就能取得好的结果 。

默认情况下,模糊度会完全扩散, 并逐点取样一个整个半球。 如果您缩小半径, 效果会更集中。 使用此方法来控制对象中不同程度的光度 。

通过过滤列表组件,将全景Blur效应添加到摄像机中:

```js
const camera = this.cameras.main;

camera.filters.internal.addPanoramaBlur({});
camera.filters.external.addPanoramaBlur({});
```

**构造函数**

`new PanoramaBlur(camera, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 拥有这个过滤器的摄像机。 |
| config | [Phaser.Types.Filters.PanoramaBlurConfig](/api/typedef/types-filters#panoramablurconfig) | 是 | 用于全景Blur效果的配置对象。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/PanoramaBlur.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/PanoramaBlur.js#L10)  
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

### power {#power}

#### power: number {#power-number}


**说明:**

应用到样本中的一个解析器。 1 以上的力量使样本整体变暗,但亮色被压制得比暗色少,导致其在结果中相对占据优势。 1 以下的动力使样本整体变亮,降低了亮色和暗色之间的对比。 要模拟一个阳光明亮、无法用 sRGB 颜色表示的HDR环境,请使用高功率。


> 源码：[src/filters/PanoramaBlur.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/PanoramaBlur.js#L103)  
引入版本：4.0.0


---

### radius {#radius}

#### radius: number {#radius-number}


**说明:**

模糊效应的半径。 1 个样本 整个半球; 0 个样本 单个点。


> 源码：[src/filters/PanoramaBlur.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/PanoramaBlur.js#L72)  
引入版本：4.0.0


---

### samplesX {#samplesX}

#### samplesX: number {#samplesx-number}


**说明:**

沿着X轴采集的样本数量。 更多的样本会产生更准确的模糊, 但以性能为代价。 总体中的X轴通常比Y轴要宽 。

更改此值触发阴影重编 。


> 源码：[src/filters/PanoramaBlur.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/PanoramaBlur.js#L81)  
引入版本：4.0.0


---

### samplesY {#samplesY}

#### samplesY: number {#samplesy-number}


**说明:**

沿着Y轴采集的样本数量。更多的样本会产生更准确的模糊,但以性能为代价。

更改此值触发阴影重编 。


> 源码：[src/filters/PanoramaBlur.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/PanoramaBlur.js#L92)  
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
