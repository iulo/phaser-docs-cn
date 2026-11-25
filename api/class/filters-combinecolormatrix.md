# CombineColorMatrix {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-combinecolormatrix)

组合颜色Matrix过滤器控制器 。

此过滤器将两个纹理的色通道组合在一起:一个基输入和一个二次传输纹理。每个源由自身独立转换 `ColorMatrix` (`colorMatrixSelf` 财务报告和已审计财务报表 `colorMatrixTransfer`),然后利用可配置的附加权重将结果进行每个通道的混合(`additions`)和乘法权重(`multiplications`),这使得它适合广泛的堆肥效果,尽管其主要用途是α通道操纵——例如,使用灰度转移纹理作为软面罩或者对底像应用亮度衍生的α. `setupAlphaTransfer` 来配置常见的α-转移模式的矩阵和加权,或设置 `colorMatrixSelf`, `colorMatrixTransfer`, `additions`,和 `multiplications` 属性直接用于自定义效果。

将一个组合颜色Matrix过滤器通过过滤列表组件添加到摄像机中:

```js
const camera = this.cameras.main;
camera.filters.internal.addCombineColorMatrix();
camera.filters.external.addCombineColorMatrix();
```

**构造函数**

`new CombineColorMatrix(camera, [texture])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的摄像机. |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 | "'__WHITE'" | 用于传输纹理的纹理或纹理键. |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/CombineColorMatrix.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/CombineColorMatrix.js#L11)  
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

### additions {#additions}

#### additions: Array.\<number> {#additions-arraynumber}


**说明:**

每个信道(R、G、B、A)的加重。 最终输出包括自矩阵和转录矩阵加的值; 这些值乘以这个数组。 因此, 保留了 1 的值, 而丢弃了 0 的值 。

默认情况下,RGB值会加在一起,最终输出.


> 源码：[src/filters/CombineColorMatrix.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/CombineColorMatrix.js#L77)  
引入版本：4.0.0


---

### colorMatrixSelf {#colorMatrixSelf}

#### colorMatrixSelf: [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) {#colormatrixself-phaserdisplaycolormatrix}


**说明:**

从基数输入中贡献值的颜色矩阵 。


> 源码：[src/filters/CombineColorMatrix.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/CombineColorMatrix.js#L59)  
引入版本：4.0.0


---

### colorMatrixTransfer {#colorMatrixTransfer}

#### colorMatrixTransfer: [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) {#colormatrixtransfer-phaserdisplaycolormatrix}


**说明:**

传输纹理中提供值的颜色矩阵 。


> 源码：[src/filters/CombineColorMatrix.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/CombineColorMatrix.js#L68)  
引入版本：4.0.0


---

### glTexture {#glTexture}

#### glTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#gltexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

传输纹理用来提供额外通道.


> 源码：[src/filters/CombineColorMatrix.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/CombineColorMatrix.js#L50)  
引入版本：4.0.0


---

### multiplications {#multiplications}

#### multiplications: Array.\<number> {#multiplications-arraynumber}


**说明:**

每一通道的乘法(R、G、B、A)的重量。最终输出包括自转矩阵的值乘以乘;这些值乘以这个数组。所以保留了1的值,而丢弃0的值。

默认情况下,α值在最终输出时会被乘以.


> 源码：[src/filters/CombineColorMatrix.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/CombineColorMatrix.js#L92)  
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


> 源码：[src/filters/CombineColorMatrix.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/CombineColorMatrix.js#L178)  
引入版本：4.0.0


---

### setTexture {#setTexture}

#### \<instance> setTexture(texture) {#instance-settexturetexture}


**说明:**

设置传输纹理。 将它的数据传输到过滤的图像中, 以此为额外的通道源 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 用于传输纹理的纹理或纹理键. |


**返回值:** [Phaser.Filters.CombineColorMatrix](/api/class/filters-combinecolormatrix) - 此过滤实例 。


> 源码：[src/filters/CombineColorMatrix.js#L110](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/CombineColorMatrix.js#L110)  
引入版本：4.0.0


---

### setupAlphaTransfer {#setupAlphaTransfer}

#### \<instance> setupAlphaTransfer([colorSelf], [colorTransfer], [brightnessToAlphaSelf], [brightnessToAlphaTransfer], [brightnessToAlphaInverseSelf], [brightnessToAlphaInverseTransfer]) {#instance-setupalphatransfercolorself-colortransfer-brightnesstoalphaself-brightnesstoalphatransfer-brightnesstoalphainverseself-brightnesstoalphainversetransfer}


**说明:**

重新设置颜色矩阵和`additions`和`multiplications`加权数组,然后应用预设的配置来进行α转录——这个滤镜的常用例。在预设中,RGB通道通过加成和α通道通过乘法结合。混合前将颜色和亮度到α的变换应用到每个源的布尔参数控制。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| colorSelf | boolean | 是 | 是否从底部图像中保留颜色 。 |
| colorTransfer | boolean | 是 | 是否从传输纹理中保留颜色 。 |
| brightnessToAlphaSelf | boolean | 是 | 是否从基亮度中确定基亮度 。 |
| brightnessToAlphaTransfer | boolean | 是 | 是否从转移亮度中确定转移的α 。 |
| brightnessToAlphaInverseSelf | boolean | 是 | 是否从底部亮度中确定底部的α, 反转。 覆盖 `brightnessToAlphaSelf` 。 |
| brightnessToAlphaInverseTransfer | boolean | 是 | 是否从转动亮度中确定转动的α, 反转。 这覆盖了 `brightnessToAlphaTransfer` 。 |


**返回值:** [Phaser.Filters.CombineColorMatrix](/api/class/filters-combinecolormatrix) - 此过滤实例 。


> 源码：[src/filters/CombineColorMatrix.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/CombineColorMatrix.js#L132)  
引入版本：4.0.0


---

---
