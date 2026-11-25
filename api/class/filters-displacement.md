# Displacement {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-displacement)

驱离过滤器控制器。

此过滤器控制器管理移位效果 。

移位效应是一种视效技术,它根据移位图的值改变像素在图像或纹理中的位置。这种效应用于在平坦元素中产生深度、表面异常或扭曲的幻觉。它可用于人物、对象或背景,以加强现实主义、传递运动或实现各种结构外观。

此效果样本跨越一个区域。 为了避免在边缘丢失数据, 请使用 `controller.setPaddingOverride(null)` 自动垫下游戏对象, 或是 `camera.getPaddingWrapper(x)` 来放大摄像机 。

通过过滤列表组件将离散效应添加到摄像机中:

```js
const camera = this.cameras.main;

camera.filters.internal.addDisplacement();
camera.filters.external.addDisplacement();
```

**构造函数**

`new Displacement(camera, [texture], [x], [y])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的摄像机。 |
| texture | string | 是 | "'__WHITE'" | 用于移位的纹理中唯一基于字符串的键,它必须存在于纹理管理器中. |
| x | number | 是 | 0.005 | 水平移位量,一个很小的浮点数,如0.005。 |
| y | number | 是 | 0.005 | 垂直移位的数量,一个非常小的浮点数,如0.005。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Displacement.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Displacement.js#L10)  
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

### texture {#texture}

#### texture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#texture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

用于迁移的基本纹理。


> 源码：[src/filters/Displacement.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Displacement.js#L80)  
引入版本：4.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

应用水平移位的量。 像素中的最大水平移位是 `x` 乘以显示过滤器的摄像机宽度的0.5倍。


> 源码：[src/filters/Displacement.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Displacement.js#L56)  
引入版本：4.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

应用垂直移位的量。像素中最大垂直移位是 `y` 乘以显示过滤器的摄像机高度的0.5倍。


> 源码：[src/filters/Displacement.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Displacement.js#L68)  
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

返回此过滤器在渲染时所需的额外粘贴量。 粘贴值会说明超出摄像机输出的原始范围的影响 。


**重写:** Phaser.Filters.Controller#getPadding


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 贴板矩形


> 源码：[src/filters/Displacement.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Displacement.js#L114)  
引入版本：4.0.0


---

### setTexture {#setTexture}

#### \<instance> setTexture([texture]) {#instance-settexturetexture}


**说明:**

设置用于移位效果的纹理。

您只能使用整个纹理, 而不是来自纹理图集或图示表的框 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| texture | string | 是 | "'__WHITE'" | 用于移位的纹理中唯一基于字符串的键,它必须存在于纹理管理器中. |


**返回值:** [Phaser.Filters.Displacement](/api/class/filters-displacement) - 此过滤控制器 。


> 源码：[src/filters/Displacement.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Displacement.js#L92)  
引入版本：4.0.0


---

---
