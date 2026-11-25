# ColorMatrix {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/display-colormatrix)

ColorMatrix类创建了可用于遮阳和图形操作的5x4矩阵,它提供了修改颜色值所需的方法,如调整亮度,设置sepia语调,hue旋转等.

矩阵行(indices 0, 1, 2, 3, 4 组成第一行) 被归纳为按顺序创建红,绿,蓝,和α通道. 矩阵列(indices  0, 5, 10, 15 组成第一列) 描述来自初始通道的捐赠, 通常在 - 1 到 1 之间 , 最后一个列( 4, 9, 14, 19) 包含一个附加, 预计将在 0 - 255 之间( 尽管其他值是有效的) 。 例如, 设置绿色通道内容的红色通道, 首列将是 [0, 0, 0, 0, 0. ] 。 设置红色通道为满, 不论当前频道, 首列将是 0, 0, 0 255] 。

这些操作是默认的使用,但您可以使用 ColorMatrix 来方便地存储数据用于其他目的.

使用 `getData` 方法返回含有当前颜色值的 Float32 箭头。这可以将添加的列从 0-255 缩小到 0-1(但不将其夹住) 。


**作用域**: static

> 源码：[src/display/ColorMatrix.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L11)  
引入版本：3.50.0

## 公开成员 {#public-members}

### alpha {#alpha}

#### alpha: number {#alpha-number}


**说明:**

用于决定混合颜色时使用多少原始颜色的值。 0( 所有原始颜色) 到 1( 所有最终颜色) 之间的值


> 源码：[src/display/ColorMatrix.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L57)  
引入版本：3.50.0


---

## 公开方法 {#public-methods}

### alphaToBrightness {#alphaToBrightness}

#### \<instance> alphaToBrightness([multiply]) {#instance-alphatobrightnessmultiply}


**说明:**

将一个α- 光线色效果应用到这个 ColorMatrix 上。 它将颜色替换为灰度的描述原α, 黑色代表透明, 白色代表不透明, 并设置为全色 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L525](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L525)  
引入版本：4.0.0


---

### alphaToBrightnessInverse {#alphaToBrightnessInverse}

#### \<instance> alphaToBrightnessInverse([multiply]) {#instance-alphatobrightnessinversemultiply}


**说明:**

将一个α对亮度的颜色效果应用到这个 ColorMatrix 上。这可以将颜色替换成灰度的描述原α,其中白色代表透明,黑色代表不透明,并设置全α.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L545](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L545)  
引入版本：4.0.0


---

### black {#black}

#### \<instance> black([multiply]) {#instance-blackmultiply}


**说明:**

设置此 ColorMatrix 为黑色, 只保留 alpha。 用于您只想要 alpha 的大小写 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L305](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L305)  
引入版本：4.0.0


---

### blackWhite {#blackWhite}

#### \<instance> blackWhite([multiply]) {#instance-blackwhitemultiply}


**说明:**

设定此颜色Matrix为黑白 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L288](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L288)  
引入版本：3.50.0


---

### brightness {#brightness}

#### \<instance> brightness([value], [multiply]) {#instance-brightnessvalue-multiply}


**说明:**

以给定的量修改此 ColorMatrix 的亮度 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 0 | 适用于此 ColorMatrix 的亮度。 0( 黑色) 到 1 之间 。 |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L167](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L167)  
引入版本：3.50.0


---

### brightnessToAlpha {#brightnessToAlpha}

#### \<instance> brightnessToAlpha([multiply]) {#instance-brightnesstoalphamultiply}


**说明:**

将亮度对α颜色效果应用到此 ColorMatrix 上。这保存了 RGB, 但用颜色的亮度取代了α 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L565](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L565)  
引入版本：4.0.0


---

### brightnessToAlphaInverse {#brightnessToAlphaInverse}

#### \<instance> brightnessToAlphaInverse([multiply]) {#instance-brightnesstoalphainversemultiply}


**说明:**

将亮度对阿尔法颜色效果应用到这个 ColorMatrix 上。这保存了 RGB,但用颜色的亮度来取代α, 反转 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L583](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L583)  
引入版本：4.0.0


---

### brown {#brown}

#### \<instance> brown([multiply]) {#instance-brownmultiply}


**说明:**

将棕色调应用到这个 ColorMatrix 上.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L440](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L440)  
引入版本：3.50.0


---

### contrast {#contrast}

#### \<instance> contrast([value], [multiply]) {#instance-contrastvalue-multiply}


**说明:**

以给定的量来更改此 ColorMatrix 的对比度 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 0 | 适用于此 ColorMatrix 的对比度 。 |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L321](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L321)  
引入版本：3.50.0


---

### desaturate {#desaturate}

#### \<instance> desaturate([multiply]) {#instance-desaturatemultiply}


**说明:**

消除此颜色Matrix( 从它中移走颜色) 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L220](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L220)  
引入版本：3.50.0


---

### desaturateLuminance {#desaturateLuminance}

#### \<instance> desaturateLuminance([multiply]) {#instance-desaturateluminancemultiply}


**说明:**

将不饱和光辉应用到此 ColorMatrix 上 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L365](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L365)  
引入版本：3.50.0


---

### getData {#getData}

#### \<instance> getData() {#instance-getdata}


**说明:**

获取 ColorMatrix 作为 Float32 箭头。

可作为1fv 遮阳器的统一值直接使用.


**返回值:** Float32Array - 彩色Matrix 以浮点32为轴.


> 源码：[src/display/ColorMatrix.js#L138](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L138)  
引入版本：3.50.0


---

### grayscale {#grayscale}

#### \<instance> grayscale([value], [multiply]) {#instance-grayscalevalue-multiply}


**说明:**

设定此颜色Matrix为灰度 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 1 | 灰度尺度(0为黑色). |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L269](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L269)  
引入版本：3.50.0


---

### hue {#hue}

#### \<instance> hue([rotation], [multiply]) {#instance-huerotation-multiply}


**说明:**

以给定的值旋转此颜色Matrix的色调 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| rotation | number | 是 | 0 | 适用于此 ColorMatrix 的 hue 旋转量, 以度计 。 |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L237](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L237)  
引入版本：3.50.0


---

### kodachrome {#kodachrome}

#### \<instance> kodachrome([multiply]) {#instance-kodachromemultiply}


**说明:**

将 kodachrome 颜色效果应用到此 ColorMatrix 上 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L474](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L474)  
引入版本：3.50.0


---

### lsd {#lsd}

#### \<instance> lsd([multiply]) {#instance-lsdmultiply}


**说明:**

将一个三进制的颜色调用到此 ColorMatrix 上 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L423](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L423)  
引入版本：3.50.0


---

### multiply {#multiply}

#### \<instance> multiply(a, [multiply]) {#instance-multiplya-multiply}


**说明:**

将给定的矩阵`a`与目前的`_matrix`相乘.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| a | Array.\<number> | 否 |  | 5x4 阵列与 ColorMatrix._matrix 相乘 。 |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L619](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L619)  
引入版本：3.50.0


---

### negative {#negative}

#### \<instance> negative([multiply]) {#instance-negativemultiply}


**说明:**

转换此 ColorMatrix 以获得负值 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L348](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L348)  
引入版本：3.50.0


---

### night {#night}

#### \<instance> night([intensity], [multiply]) {#instance-nightintensity-multiply}


**说明:**

将夜视调应用到这个 ColorMatrix 上.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| intensity | number | 是 | 0.1 | 这种效果的强度. |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L399](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L399)  
引入版本：3.50.0


---

### polaroid {#polaroid}

#### \<instance> polaroid([multiply]) {#instance-polaroidmultiply}


**说明:**

将极性颜色效果应用到此 ColorMatrix 上 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L508](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L508)  
引入版本：3.50.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

将 ColorMatrix 重置为默认值, 并将 `alpha` 属性重置为 1 。


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L111)  
引入版本：3.50.0


---

### saturate {#saturate}

#### \<instance> saturate([value], [multiply]) {#instance-saturatevalue-multiply}


**说明:**

以给定的量更改此颜色Matrix的饱和度 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 0 | 适用于此 ColorMatrix 的饱和度 。 |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L193](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L193)  
引入版本：3.50.0


---

### sepia {#sepia}

#### \<instance> sepia([multiply]) {#instance-sepiamultiply}


**说明:**

应用 sepia 语调来达到这个 ColorMatrix 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L382](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L382)  
引入版本：3.50.0


---

### set {#set}

#### \<instance> set(value) {#instance-setvalue}


**说明:**

设定颜色组合从给定的颜色值数组中生成此颜色。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | Array.\<number> \| Float32Array | 否 | 要设置的 ColorMatrix 值。 必须有 20 个元素 。 |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L92)  
引入版本：3.50.0


---

### shiftToBGR {#shiftToBGR}

#### \<instance> shiftToBGR([multiply]) {#instance-shifttobgrmultiply}


**说明:**

将此 ColorMatrix 的值移动到 BGR 顺序。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L602](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L602)  
引入版本：3.50.0


---

### technicolor {#technicolor}

#### \<instance> technicolor([multiply]) {#instance-technicolormultiply}


**说明:**

将一个技术色彩效果应用到此色彩Matrix 上 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L491](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L491)  
引入版本：3.50.0


---

### vintagePinhole {#vintagePinhole}

#### \<instance> vintagePinhole([multiply]) {#instance-vintagepinholemultiply}


**说明:**

将古董的针孔颜色效果应用到这个 ColorMatrix 上 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| multiply | boolean | 是 | false | 乘以产生的 ColorMatrix(`true`),或设置它(`false`) ? |


**返回值:** [Phaser.Display.ColorMatrix](/api/class/display-colormatrix) - 此 ColorMatrix 实例 。


> 源码：[src/display/ColorMatrix.js#L457](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L457)  
引入版本：3.50.0


---

## 常量 {#constants}

## 公开成员 {#public-members-1}

### ALPHA_TO_BRIGHTNESS {#ALPHA_TO_BRIGHTNESS}

#### ALPHA_TO_BRIGHTNESS: Array.\<number> {#alpha_to_brightness-arraynumber}


**说明:**

ColorMatrix类用于α对光线操作的恒定数组.


> 源码：[src/display/ColorMatrix.js#L800](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L800)  
引入版本：4.0.0


---

### ALPHA_TO_BRIGHTNESS_INVERSE {#ALPHA_TO_BRIGHTNESS_INVERSE}

#### ALPHA_TO_BRIGHTNESS_INVERSE: Array.\<number> {#alpha_to_brightness_inverse-arraynumber}


**说明:**

ColorMatrix类用于反向α对光操作的恒定数组.


> 源码：[src/display/ColorMatrix.js#L815](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L815)  
引入版本：4.0.0


---

### BLACK {#BLACK}

#### BLACK: Array.\<number> {#black-arraynumber}


**说明:**

ColorMatrix 类用于黑操作的常数组.


> 源码：[src/display/ColorMatrix.js#L685](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L685)  
引入版本：4.0.0


---

### BLACK_WHITE {#BLACK_WHITE}

#### BLACK_WHITE: Array.\<number> {#black_white-arraynumber}


**说明:**

ColorMatrix 类用于黑_白操作的恒定数组.


> 源码：[src/display/ColorMatrix.js#L700](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L700)  
引入版本：3.60.0


---

### BRIGHTNESS_TO_ALPHA {#BRIGHTNESS_TO_ALPHA}

#### BRIGHTNESS_TO_ALPHA: Array.\<number> {#brightness_to_alpha-arraynumber}


**说明:**

用于亮度对阿尔法操作的 ColorMatrix 类的常数组.


> 源码：[src/display/ColorMatrix.js#L830](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L830)  
引入版本：4.0.0


---

### BRIGHTNESS_TO_ALPHA_INVERSE {#BRIGHTNESS_TO_ALPHA_INVERSE}

#### BRIGHTNESS_TO_ALPHA_INVERSE: Array.\<number> {#brightness_to_alpha_inverse-arraynumber}


**说明:**

ColorMatrix类用于反光对α操作的恒定数组.


> 源码：[src/display/ColorMatrix.js#L845](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L845)  
引入版本：4.0.0


---

### BROWN {#BROWN}

#### BROWN: Array.\<number> {#brown-arraynumber}


**说明:**

ColorMatrix类用于棕色操作的恒定数组.


> 源码：[src/display/ColorMatrix.js#L750](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L750)  
引入版本：3.60.0


---

### DESATURATE_LUMINANCE {#DESATURATE_LUMINANCE}

#### DESATURATE_LUMINANCE: Array.\<number> {#desaturate_luminance-arraynumber}


**说明:**

ColorMatrix类用于脱饱和润滑操作的恒定数组.


> 源码：[src/display/ColorMatrix.js#L720](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L720)  
引入版本：3.60.0


---

### KODACHROME {#KODACHROME}

#### KODACHROME: Array.\<number> {#kodachrome-arraynumber}


**说明:**

ColorMatrix类用于kodachrome操作的常数组.


> 源码：[src/display/ColorMatrix.js#L770](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L770)  
引入版本：3.60.0


---

### LSD {#LSD}

#### LSD: Array.\<number> {#lsd-arraynumber}


**说明:**

用于Isd操作的 ColorMatrix 类所用的常数组。


> 源码：[src/display/ColorMatrix.js#L740](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L740)  
引入版本：3.60.0


---

### NEGATIVE {#NEGATIVE}

#### NEGATIVE: Array.\<number> {#negative-arraynumber}


**说明:**

ColorMatrix 类用于负操作的恒定数组.


> 源码：[src/display/ColorMatrix.js#L710](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L710)  
引入版本：3.60.0


---

### POLAROID {#POLAROID}

#### POLAROID: Array.\<number> {#polaroid-arraynumber}


**说明:**

ColorMatrix类用于极性移位操作的恒定数组.


> 源码：[src/display/ColorMatrix.js#L790](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L790)  
引入版本：3.60.0


---

### SEPIA {#SEPIA}

#### SEPIA: Array.\<number> {#sepia-arraynumber}


**说明:**

ColorMatrix类用于seepia操作的恒定数组.


> 源码：[src/display/ColorMatrix.js#L730](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L730)  
引入版本：3.60.0


---

### SHIFT_BGR {#SHIFT_BGR}

#### SHIFT_BGR: Array.\<number> {#shift_bgr-arraynumber}


**说明:**

ColorMatrix类用于转动BGR操作的恒定数组.


> 源码：[src/display/ColorMatrix.js#L860](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L860)  
引入版本：3.60.0


---

### TECHNICOLOR {#TECHNICOLOR}

#### TECHNICOLOR: Array.\<number> {#technicolor-arraynumber}


**说明:**

ColorMatrix 类用于技术彩色操作的常数组。


> 源码：[src/display/ColorMatrix.js#L780](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L780)  
引入版本：3.60.0


---

### VINTAGE {#VINTAGE}

#### VINTAGE: Array.\<number> {#vintage-arraynumber}


**说明:**

ColorMatrix类用于古董针孔操作的恒定数组.


> 源码：[src/display/ColorMatrix.js#L760](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorMatrix.js#L760)  
引入版本：3.60.0


---

---
