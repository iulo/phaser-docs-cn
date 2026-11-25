# Blend {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-blend)

混合过滤控制器 。

此过滤控制器管理摄像机的混合效果。 混合效果允许您使用特定的混合模式对视图应用另一个纹理。 这支持WebGL中无法使用的混合模式 。

通过过滤列表组件向摄像机添加了混合效应:

```js
const camera = this.cameras.main;
camera.filters.internal.addBlend();
camera.filters.external.addBlend();
```

**构造函数**

`new Blend(camera, [texture], [blendMode], [amount], [color])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的摄像机. |
| texture | string | 是 | "'__WHITE'" | 纹理适用于视图. |
| blendMode | [Phaser.BlendModes](/api/namespace/blendmodes) | 是 | "Phaser.BlendModes.NORMAL" | 用于视图的混合模式 。 |
| amount | number | 是 | 1 | 混合效果的大小适用于视图。 0 时, 原图像被保存。 1 时, 混合纹理被完全应用。 预期范围为 0 到 1, 但您可以在此范围之外进行不同效果 。 |
| color | Array.\<number> | 是 | "[1, 1, 1, 1]" | 混合纹理的颜色。 每个值对应 RGBA 中的彩色通道。 期望范围为 0 到 1, 但您可以在此范围之外进行不同效果 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Blend.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blend.js#L10)  
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

混合效果的大小适用于视图。 0 时, 原图像被保存。 1 时, 混合纹理被完全应用 。


> 源码：[src/filters/Blend.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blend.js#L70)  
引入版本：4.0.0


---

### blendMode {#blendMode}

#### blendMode: [Phaser.BlendModes](/api/namespace/blendmodes) {#blendmode-phaserblendmodes}


**说明:**

用于视图的混合模式。 这支持 WebGL 中无法使用的混合模式 。


> 源码：[src/filters/Blend.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blend.js#L59)  
引入版本：4.0.0


---

### color {#color}

#### color: Array.\<number> {#color-arraynumber}


**说明:**

混合纹理的颜色。 每个值对应 RGBA 中的彩色通道。 期望范围为 0 到 1, 但您可以在此范围之外进行不同效果 。


> 源码：[src/filters/Blend.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blend.js#L81)  
引入版本：4.0.0


---

### glTexture {#glTexture}

#### glTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#gltexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

混合用的内在纹理


> 源码：[src/filters/Blend.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blend.js#L50)  
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

### setTexture {#setTexture}

#### \<instance> setTexture([texture]) {#instance-settexturetexture}


**说明:**

设置混合用的纹理。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| texture | string | 是 | "'__WHITE'" | 用于混合的纹理中唯一基于字符串的键,它必须存在于纹理管理器中. |


**返回值:** [Phaser.Filters.Blend](/api/class/filters-blend) - 此过滤控制器 。


> 源码：[src/filters/Blend.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blend.js#L96)  
引入版本：4.0.0


---

---
