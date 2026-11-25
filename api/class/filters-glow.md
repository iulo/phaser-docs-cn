# Glow {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-glow)

光滑滤镜控制器 。

这个过滤器控制器管理着相机的发光效果.

光线效应是一种视觉技术,它围绕游戏对象,人物,或UI元素,创建柔软,光线光环,这种效应用来强调重要性,增强视觉吸引力,或传递能量感,魔法感,或其他世界存在的感,效果也可以设定在边缘内部,光线的颜色和强度可以修改.

此效果样本跨越一个区域。 为了避免在边缘丢失数据, 请使用 `controller.setPaddingOverride(null)` 自动垫下游戏对象, 或是 `camera.getPaddingWrapper(x)` 来放大相机 。

通过过滤列表组件,将一个Glow效应添加到相机中:

```js
const camera = this.cameras.main;

camera.filters.internal.addGlow();
camera.filters.external.addGlow();
```

Phaser 3的转换注释:

- 遮阳器现在使用有条理的取样,而不是直线的取样。这提高了质量,特别是在角落周围。

- `scale`已经添加到参数列表中,在`knockout`之前.

- `quality`不再是分数,而是整数值。默认值从0.1变为10。由于质量的提高,这不是线性转换。按眼睛判断质量,并相应调整数值。

**构造函数**

`new Glow(camera, [color], [outerStrength], [innerStrength], [scale], [knockout], [quality], [distance])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的相机. |
| color | number | 是 | "0xffffff" | 光线效应的颜色作为数字值. |
| outerStrength | number | 是 | 4 | 发光的强度从纹理边缘向外延伸. |
| innerStrength | number | 是 | 0 | 发光的强度从纹理边缘向内倾. |
| scale | number | 是 | 1 | 光线效应的尺度, 将固定距离乘以倍数 。 |
| knockout | boolean | 是 | false | 如果`true`只画出光线,而不是纹理本身. |
| quality | number | 是 | 10 | 发光效果的质量。 过滤器创建后无法更改 。 |
| distance | number | 是 | 10 | 光线效果的距离。 过滤器创建后无法更改 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Glow.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Glow.js#L10)  
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

发光效果的颜色, 以0xRRGGBB格式的六进制颜色值表示。 获取此值后, 将转换为内部正常的 `glcolor`阵列。 设置它更新 `glcolor`, 供 WebGL 渲染器使用 。


> 源码：[src/filters/Glow.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Glow.js#L156)  
引入版本：4.0.0


---

### distance {#distance}

#### distance: number {#distance-number}


**说明:**

光线效果的距离。 过滤器创建后无法更改。 仅以像素形式控制光线效果的距离。 Integer 值 。


> 源码：[src/filters/Glow.js#L186](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Glow.js#L186)  
引入版本：4.0.0


---

### glcolor {#glcolor}

#### glcolor: Array.\<number> {#glcolor-arraynumber}


**说明:**

发光的内部RGBA颜色, 以0到1之间的四个正态浮点值( 红、 绿、 蓝、 α) 存储, 供 WebGL 渲染器直接使用。 要设定发光颜色, 请使用 `color` 属性 。


> 源码：[src/filters/Glow.js#L138](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Glow.js#L138)  
引入版本：4.0.0


---

### innerStrength {#innerStrength}

#### innerStrength: number {#innerstrength-number}


**说明:**

发光的强度从纹理边缘向内倾.


> 源码：[src/filters/Glow.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Glow.js#L77)  
引入版本：4.0.0


---

### knockout {#knockout}

#### knockout: boolean {#knockout-boolean}


**说明:**

如果`true`只画出光线,而不是纹理本身.


> 源码：[src/filters/Glow.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Glow.js#L97)  
引入版本：4.0.0


---

### outerStrength {#outerStrength}

#### outerStrength: number {#outerstrength-number}


**说明:**

发光的强度从纹理边缘向外延伸.


> 源码：[src/filters/Glow.js#L67](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Glow.js#L67)  
引入版本：4.0.0


---

### quality {#quality}

#### quality: number {#quality-number}


**说明:**

发光效果的质量。 过滤器创建后无法更改。 这控制了发光效果运行的样本数量。 更高的数字是质量更高, 但处理速度较慢。 仅整数值 。


> 源码：[src/filters/Glow.js#L206](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Glow.js#L206)  
引入版本：4.0.0


---

### scale {#scale}

#### scale: number {#scale-number}


**说明:**

光线效应的尺度, 将固定距离乘以倍数 。


> 源码：[src/filters/Glow.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Glow.js#L87)  
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

返回此过滤器在渲染时所需的额外粘贴量。 粘贴值会说明超出相机输出的原始范围所产生的光线效应。 Name


**Overrides:** Phaser.Filters.Controller#getPadding


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 贴板矩形


> 源码：[src/filters/Glow.js#L226](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Glow.js#L226)  
引入版本：4.0.0


---

---
