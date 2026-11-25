# Color {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/display-color)

一种可变色表示,将 RGBA 值( 0-255 范围) 自动转换为 WebGL-兼容的常态浮标(0-1),HSV色彩空间,CSS rgba字符串,以及装入的24/32位整数格式。提供色彩操纵方法,包括饱和度、光度、亮度调整、灰度度和随机化。支持从 RGB 整数、六重字符串、HSV值或颜色对象构造。 Phaser 用于制毒、效果和渲染

**构造函数**

`new Color([red], [green], [blue], [alpha])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| red | number | 是 | 0 | 红色值,数字在0到255之间 |
| green | number | 是 | 0 | 绿色的颜色值,数字在0到255之间. |
| blue | number | 是 | 0 | 蓝色的颜色值,数字在0到255之间. |
| alpha | number | 是 | 255 | α值,数字在0到255之间. |

---


**作用域**: static

> 源码：[src/display/color/Color.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L17)  
引入版本：3.0.0

## 公开成员 {#public-members}

### alpha {#alpha}

#### alpha: number {#alpha-number}


**说明:**

α色值,在0到255之间.


> 源码：[src/display/color/Color.js#L762](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L762)  
引入版本：3.0.0


---

### alphaGL {#alphaGL}

#### alphaGL: number {#alphagl-number}


**说明:**

α色值,正常化为0至1度.


> 源码：[src/display/color/Color.js#L656](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L656)  
引入版本：3.0.0


---

### blue {#blue}

#### blue: number {#blue-number}


**说明:**

蓝色的颜色值,在0到255之间.


> 源码：[src/display/color/Color.js#L735](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L735)  
引入版本：3.0.0


---

### blueGL {#blueGL}

#### blueGL: number {#bluegl-number}


**说明:**

蓝色的颜色值, 正常化到 0 到 1 之间 。


> 源码：[src/display/color/Color.js#L631](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L631)  
引入版本：3.0.0


---

### color {#color}

#### color: number {#color-number}


**说明:**

包装的24位RGB整数表示这个颜色,不包括α通道.


> 源码：[src/display/color/Color.js#L530](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L530)  
引入版本：3.0.0


---

### color32 {#color32}

#### color32: number {#color32-number}


**说明:**

包装的32位RGBA整数表示这个颜色,包括α通道.


> 源码：[src/display/color/Color.js#L547](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L547)  
引入版本：3.0.0


---

### gl {#gl}

#### gl: Array.\<number> {#gl-arraynumber}


**说明:**

包含WebGL兼容的常态浮标格式中的RGBA颜色组件的阵列,以`[red, green, blue, alpha]`存储,每个值在0到1之间.


> 源码：[src/display/color/Color.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L137)  
引入版本：3.0.0


---

### green {#green}

#### green: number {#green-number}


**说明:**

绿色的颜色值,在0到255之间.


> 源码：[src/display/color/Color.js#L708](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L708)  
引入版本：3.0.0


---

### greenGL {#greenGL}

#### greenGL: number {#greengl-number}


**说明:**

绿色的颜色值, 规范为 0 到 1 之间 。


> 源码：[src/display/color/Color.js#L606](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L606)  
引入版本：3.0.0


---

### h {#h}

#### h: number {#h-number}


**说明:**

色值。 0 到 1 之间的数字是底色 。


> 源码：[src/display/color/Color.js#L789](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L789)  
引入版本：3.13.0


---

### red {#red}

#### red: number {#red-number}


**说明:**

红色值,在0到255之间.


> 源码：[src/display/color/Color.js#L681](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L681)  
引入版本：3.0.0


---

### redGL {#redGL}

#### redGL: number {#redgl-number}


**说明:**

红色值, 规范为 0 到 1 之间 。


> 源码：[src/display/color/Color.js#L581](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L581)  
引入版本：3.0.0


---

### rgba {#rgba}

#### rgba: string {#rgba-string}


**说明:**

此颜色对象的颜色是 CSS 兼容的 `rgba()` 字符串, 适合与 Canvas 2D 或 HTML 元素使用 。


> 源码：[src/display/color/Color.js#L564](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L564)  
引入版本：3.0.0


---

### s {#s}

#### s: number {#s-number}


**说明:**

饱和色值。 0 和 1 之间的数字控制了 最终颜色中多少色调, 其中 1 完全饱和, 0 将给予您白色 。


> 源码：[src/display/color/Color.js#L813](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L813)  
引入版本：3.13.0


---

### v {#v}

#### v: number {#v-number}


**说明:**

HSV 色彩空间中此颜色的值( 亮度) 组件。 0 到 1 之间的数字, 其中 1 完全亮度和 0 黑色 。


> 源码：[src/display/color/Color.js#L837](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L837)  
引入版本：3.13.0


---

## 公开方法 {#public-methods}

### brighten {#brighten}

#### \<instance> brighten(amount) {#instance-brightenamount}


**说明:**

以给定的百分比数来显示此颜色 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| amount | number | 否 | 百分比值可以改变此颜色。 数值在 0 到 100 之间 。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 此颜色对象 。


> 源码：[src/display/color/Color.js#L507](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L507)  
引入版本：3.13.0


---

### clone {#clone}

#### \<instance> clone() {#instance-clone}


**说明:**

使用此值返回新的颜色组件。


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 一个新的颜色对象。


> 源码：[src/display/color/Color.js#L365](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L365)  
引入版本：3.0.0


---

### ColorSpectrum {#ColorSpectrum}

#### \<static> ColorSpectrum([limit]) {#static-colorspectrumlimit}


**说明:**

返回代表全色谱的彩色对象数组。

谱色周期通过色轮按顺序排列:红,黄,绿,青,蓝,紫,回红.

默认情况下,此函数将返回一个包含 1024 元素的数组 。

但是,如果需要,您可以通过指定 `limit` 参数来将它减少到较小的数量。当给出一个小于 1024 的限值时,颜色在全谱中均匀地取样,这样无论阵列大小,色调分布都保持统一。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| limit | number | 是 | 1024 | 返回的颜色是多少? 最多为 1024 个, 但需要时可以设定较小的颜色 。 |


**返回值:** Array.\<[Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject)> - 包含 `limit` 参数数的元素数组,其中每个元素包含一个色彩对象.


> 源码：[src/display/color/ColorSpectrum.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/ColorSpectrum.js#L9)  
引入版本：3.50.0


---

### ColorToRGBA {#ColorToRGBA}

#### \<static> ColorToRGBA(color) {#static-colortorgbacolor}


**说明:**

将给定的颜色值转换成包含 r、g、b 和属性的对象。

颜色值可以是24位RGB整数(如`0xRRGGBB`)或32位ARGB整数(如 `0xAARRGGBB`),如果值是24位(即不超过`0xFFFFFF`),返回对象的α组件默认为255(完全不透明),否则,α从值的上8位中提取.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | number | 否 | 一个24位RGB或32位ARGB的颜色整数,可选地在最显著的字节中包含一个α元件. |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) - 包含解析的颜色值的对象。


> 源码：[src/display/color/ColorToRGBA.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/ColorToRGBA.js#L7)  
引入版本：3.0.0


---

### ComponentToHex {#ComponentToHex}

#### \<static> ComponentToHex(color) {#static-componenttohexcolor}


**说明:**

返回包含给定颜色组件的六进制表示符的字符串。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | number | 否 | 获取六进制值的颜色通道,必须是0到255之间的值. |


**返回值:** string - 长度2字符的字符串,即255=ff,100=64.


> 源码：[src/display/color/ComponentToHex.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/ComponentToHex.js#L7)  
引入版本：3.0.0


---

### darken {#darken}

#### \<instance> darken(amount) {#instance-darkenamount}


**说明:**

将此颜色的光度减少给定的百分比量。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| amount | number | 否 | 百分比值可以改变此颜色。 数值在 0 到 100 之间 。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 此颜色对象 。


> 源码：[src/display/color/Color.js#L490](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L490)  
引入版本：3.13.0


---

### desaturate {#desaturate}

#### \<instance> desaturate(amount) {#instance-desaturateamount}


**说明:**

将此颜色的饱和度减少为给定的百分比量。饱和度是色调中基色的量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| amount | number | 否 | 百分比值可以改变此颜色。 数值在 0 到 100 之间 。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 此颜色对象 。


> 源码：[src/display/color/Color.js#L455](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L455)  
引入版本：3.13.0


---

### GetColor {#GetColor}

#### \<static> GetColor(red, green, blue) {#static-getcolorred-green-blue}


**说明:**

将三个独立的红,绿,蓝三个颜色成分值按0xRGGBB格式,组合成一个单一的24位整数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| red | number | 否 | 红色值,数字在0到255之间 |
| green | number | 否 | 绿色的颜色值,数字在0到255之间. |
| blue | number | 否 | 蓝色的颜色值,数字在0到255之间. |


**返回值:** number - 组合的颜色值作为0xRRGGBB格式中的24位整数.


> 源码：[src/display/color/GetColor.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/GetColor.js#L7)  
引入版本：3.0.0


---

### GetColor32 {#GetColor32}

#### \<static> GetColor32(red, green, blue, alpha) {#static-getcolor32red-green-blue-alpha}


**说明:**

将4个ARGB组件值(红,绿,蓝,和α)以ARGB格式包装成一个32位单数整数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| red | number | 否 | 红色值,数字在0到255之间 |
| green | number | 否 | 绿色的颜色值,数字在0到255之间. |
| blue | number | 否 | 蓝色的颜色值,数字在0到255之间. |
| alpha | number | 否 | α颜色值,数字在 0 到 255 之间 。 |


**返回值:** number - 装箱的32位ARGB颜色值.


> 源码：[src/display/color/GetColor32.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/GetColor32.js#L7)  
引入版本：3.0.0


---

### gray {#gray}

#### \<instance> gray(shade) {#instance-grayshade}


**说明:**

设定此颜色对象为灰色,其范围以给定的阴影值为准。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| shade | number | 否 | 值在 0 至 255 之间 。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 此颜色对象 。


> 源码：[src/display/color/Color.js#L378](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L378)  
引入版本：3.13.0


---

### HexStringToColor {#HexStringToColor}

#### \<static> HexStringToColor(hex, [color]) {#static-hexstringtocolorhex-color}


**说明:**

将六角弦转换成 Phaser 颜色对象。

十六进制字符串可以以`'#0033ff'`或`'#03f'`的短手格式提供;它可以从可选的"#"或"0x"开始,也可以不设前缀.

支持的 Alpha 频道为 _ not_ 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| hex | string | 否 | 要转换的六角星颜色值,例如`#0033ff`或短手格式:`#03f`. |
| color | [Phaser.Display.Color](/api/namespace/display-color) | 是 | 将存储新颜色的颜色。如果不定义,则返回新颜色对象。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 以给定字符串的值为对象的颜色对象。


> 源码：[src/display/color/HexStringToColor.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/HexStringToColor.js#L9)  
引入版本：3.0.0


---

### HSLToColor {#HSLToColor}

#### \<static> HSLToColor(h, s, l, [color]) {#static-hsltocolorh-s-l-color}


**说明:**

将 HSL( 色调、 饱和度和光度) 值转换为 Phaser 颜色对象 。

所有三个输入值都应该在0到1之间,如果饱和度为0,则将颜色作为色度(greyscale)处理。否则将采用标准的HSL-对RGB算法,在将每个信道下放到`HueToComponent`之前,使用光度值来得出中间q和p系数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| h | number | 否 | 0到1之间的色值. |
| s | number | 否 | 0到1之间的饱和值. |
| l | number | 否 | 0到1之间的轻度值. |
| color | [Phaser.Display.Color](/api/namespace/display-color) | 是 | 与转换值填充的可选颜色对象。如果不提供,则创建并返回新的颜色对象。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 包含由给定的 h、 s 和 l 输入产生的 RGB 值的颜色对象。 或者是 `color` 参数( 如果提供的话) , 或是新创建的颜色对象 。


> 源码：[src/display/color/HSLToColor.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/HSLToColor.js#L10)  
引入版本：3.0.0


---

### HSVColorWheel {#HSVColorWheel}

#### \<static> HSVColorWheel([s], [v]) {#static-hsvcolorwheels-v}


**说明:**

生成一个 HSV 颜色轮,作为360 色彩对象条目的数组,每度调值从 0 到 359 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| s | number | 是 | 1 | 饱和度,在0 - 1 之间. |
| v | number | 是 | 1 | 值,在0 - 1 之间. |


**返回值:** Array.\<[Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject)> - 360色彩对象元素的阵列,每个元素代表HSV色彩轮的那一色阶的RGB颜色.


> 源码：[src/display/color/HSVColorWheel.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/HSVColorWheel.js#L9)  
引入版本：3.0.0


---

### HSVToRGB {#HSVToRGB}

#### \<static> HSVToRGB(h, s, v, [out]) {#static-hsvtorgbh-s-v-out}


**说明:**

将 HSV( 色调、 饱和度和值) 颜色设置转换为 RGB 。

[https://en.wikipedia.org/wiki/HSL_and_HSV](https://en.wikipedia.org/wiki/HSL_and_HSV)的转换公式

假设HSV值包含在集 [0, 1] 中.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| h | number | 否 | 色调,在0 - 1 度之间,这是底色. |
| s | number | 否 | 饱和度,在0 - 1. 范围中,这控制了最终颜色中多少色调,其中1完全饱和,0会给你一个灰度的颜色. |
| v | number | 否 | 值,在0 - 1. 范围中,这控制着颜色的亮度,其中1尽可能亮,0为黑色. |
| out | [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) \| [Phaser.Display.Color](/api/namespace/display-color) | 是 | 用于存储结果的颜色对象。如果不给定新的颜色对象,则将创建 。 |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject), [Phaser.Display.Color](/api/namespace/display-color) - 对象,在 r, g 和 b 属性中设置红色,绿色和蓝色的值.


> 源码：[src/display/color/HSVToRGB.js#L30](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/HSVToRGB.js#L30)  
引入版本：3.0.0


---

### HueToComponent {#HueToComponent}

#### \<static> HueToComponent(p, q, t) {#static-huetocomponentp-q-t}


**说明:**

从一个 hue 偏移和 HSL 到 RGB 转换期间所用的两个中间光度值计算出一个 RGB 通道值。 给每个通道( 红、 绿、 蓝) 调用一次此函数, 每次通过适当的 hue 偏移 。 基于 Michael Jackson 的代码( https://github.com/mjijackson))

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| p | number | 否 | 第一个中间值是从HSL到RGB转换期间的轻度得到的. |
| q | number | 否 | 第二个中间值是从HSL到RGB转换期间的轻度和饱和度中衍生出来的. |
| t | number | 否 | 用于计算颜色通道(红、绿或蓝色)的色调抵消。 |


**返回值:** number - 给定的hue 偏移的 RGB 通道值,在 0 到 1 之间 。


> 源码：[src/display/color/HueToComponent.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/HueToComponent.js#L7)  
引入版本：3.0.0


---

### IntegerToColor {#IntegerToColor}

#### \<static> IntegerToColor(input, [color]) {#static-integertocolorinput-color}


**说明:**

将给定的颜色值转换成颜色对象实例。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| input | number | 否 | 转换的32位整数颜色值,例如像`0xff0000`这样的六进制值表示红色. |
| color | [Phaser.Display.Color](/api/namespace/display-color) | 是 | 保存结果的可选颜色对象。如果不提供,则创建并返回新的颜色对象。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 一个包含从给定整数中提取的红、绿、蓝和α组件的彩色对象。


> 源码：[src/display/color/IntegerToColor.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/IntegerToColor.js#L10)  
引入版本：3.0.0


---

### IntegerToRGB {#IntegerToRGB}

#### \<static> IntegerToRGB(color) {#static-integertorgbcolor}


**说明:**

返回颜色的组件部分作为对象,其属性为α,红,绿,蓝.

如果颜色值包括一个α组件(0xAARGGBB),则它会被提取并设置在`a`属性中。否则,α默认值为255(完全不透明).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | number | 否 | 转换成彩色对象的颜色值。 |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) - a, r, g, 和 b 属性中设定的α, 红色, 绿色, 和蓝色值的对象 。


> 源码：[src/display/color/IntegerToRGB.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/IntegerToRGB.js#L7)  
引入版本：3.0.0


---

### lighten {#lighten}

#### \<instance> lighten(amount) {#instance-lightenamount}


**说明:**

以给定的百分比数增加此颜色的亮度 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| amount | number | 否 | 百分比值可以改变此颜色。 数值在 0 到 100 之间 。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 此颜色对象 。


> 源码：[src/display/color/Color.js#L473](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L473)  
引入版本：3.13.0


---

### ObjectToColor {#ObjectToColor}

#### \<static> ObjectToColor(input, [color]) {#static-objecttocolorinput-color}


**说明:**

转换含有对象 `r`, `g`, `b` 财务报告和已审计财务报表 `a` 属性为颜色类实例。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| input | [Phaser.Types.Display.InputColorObject](/api/typedef/types-display#inputcolorobject) | 否 | 含有`r`,`g`,`b`和`a`属性的天体,范围为0至255. |
| color | [Phaser.Display.Color](/api/namespace/display-color) | 是 | 将存储新颜色的颜色。如果不定义,则返回新颜色对象。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 颜色对象。


> 源码：[src/display/color/ObjectToColor.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/ObjectToColor.js#L9)  
引入版本：3.0.0


---

### random {#random}

#### \<instance> random([min], [max]) {#instance-randommin-max}


**说明:**

设定此颜色对象为给定的 `min` 值和 `max` 值之间的随机颜色 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| min | number | 是 | 0 | 最小随机颜色值,在0到255之间. |
| max | number | 是 | 255 | 最大随机颜色值,在 0 到 255 之间 。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 此颜色对象 。


> 源码：[src/display/color/Color.js#L393](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L393)  
引入版本：3.13.0


---

### randomGray {#randomGray}

#### \<instance> randomGray([min], [max]) {#instance-randomgraymin-max}


**说明:**

设定此颜色对象为给定的 `min` 值和 `max` 值之间的随机灰度颜色 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| min | number | 是 | 0 | 最小随机颜色值,在0到255之间. |
| max | number | 是 | 255 | 最大随机颜色值,在 0 到 255 之间 。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 此颜色对象 。


> 源码：[src/display/color/Color.js#L416](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L416)  
引入版本：3.13.0


---

### RandomRGB {#RandomRGB}

#### \<static> RandomRGB([min], [max]) {#static-randomrgbmin-max}


**说明:**

创建一个新的颜色对象,其中 r、g和b 值被设定为基于给定的 min 最大值的随机值。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| min | number | 是 | 0 | 设定随机范围最小值从( 0 到 255 之间) |
| max | number | 是 | 255 | 设置随机范围的最大值( 0 到 255 之间) |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 颜色对象。


> 源码：[src/display/color/RandomRGB.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/RandomRGB.js#L10)  
引入版本：3.0.0


---

### RGBStringToColor {#RGBStringToColor}

#### \<static> RGBStringToColor(rgb, [color]) {#static-rgbstringtocolorrgb-color}


**说明:**

将 CSS 网络字符串转换为 Phaser 颜色对象。

网格字符串可以是r/g/b在[0.255]范围内,a在[0.1]范围内,格式为`'rgb(r,g,b)'`或`'rgba(r,g,b,a)'`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rgb | string | 否 | CSS格式的颜色字符串,使用`rgb`或`rgba`格式. |
| color | [Phaser.Display.Color](/api/namespace/display-color) | 是 | 包含解析值的可选颜色对象。如果不提供,则创建并返回新的颜色对象。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 含有解析的 RGB 或 RGBA 值的颜色对象。


> 源码：[src/display/color/RGBStringToColor.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/RGBStringToColor.js#L9)  
引入版本：3.0.0


---

### RGBToHSV {#RGBToHSV}

#### \<static> RGBToHSV(r, g, b, [out]) {#static-rgbtohsvr-g-b-out}


**说明:**

将 RGB 颜色值转换为 HSV( 色调、 饱和度和值 )。 从 [http://en.wikipedia.org/wiki/HSL_color_space.](http://en.wikipedia.org/wiki/HSL_color_space.) 的 ASumes RGB 值转换公式包含在 sects [0, 255] 中, 返回 h, s 和 v 包含在 secut [0, 1] 中。 基于 Michael Jackson 的代码( https://github.com/mjijackson)Z)

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| r | number | 否 | 红色值,数字在0到255之间 |
| g | number | 否 | 绿色的颜色值,数字在0到255之间. |
| b | number | 否 | 蓝色的颜色值,数字在0到255之间. |
| out | [Phaser.Types.Display.HSVColorObject](/api/typedef/types-display#hsvcolorobject) \| [Phaser.Display.Color](/api/namespace/display-color) | 是 | 将颜色值存储在其中的对象。 如果不给定 HSV 颜色对象, 将会创建 。 |


**返回值:** [Phaser.Types.Display.HSVColorObject](/api/typedef/types-display#hsvcolorobject), [Phaser.Display.Color](/api/namespace/display-color) - 具有`h`,`s`和`v`等特性的天体.


> 源码：[src/display/color/RGBToHSV.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/RGBToHSV.js#L7)  
引入版本：3.0.0


---

### RGBToString {#RGBToString}

#### \<static> RGBToString(r, g, b, [a], [prefix]) {#static-rgbtostringr-g-b-a-prefix}


**说明:**

将给定的红色、绿色、蓝色和α色成分值转换成六重彩色字符串。

当使用 `#` 前缀时,结果为`#rrggbb`格式的6个字符形 CSS 兼容六元字符串。此格式不包括α值。

使用`0x`前缀时,结果为`0xaarrggbb`格式的8字符串ARGB六元字符串,其中包含α元件作为最显著的字节.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| r | number | 否 |  | 红色值,数字在0到255之间 |
| g | number | 否 |  | 绿色的颜色值,数字在0到255之间. |
| b | number | 否 |  | 蓝色的颜色值,数字在0到255之间. |
| a | number | 是 | 255 | α值,数字在0到255之间. |
| prefix | string | 是 | "#" | 弦的前缀,要么是`#`,要么是`0x`. |


**返回值:** string - 以`#rrggbb`或`0xaarrggbb`格式的六角色字符串,视前缀而定.


> 源码：[src/display/color/RGBToString.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/RGBToString.js#L9)  
引入版本：3.0.0


---

### saturate {#saturate}

#### \<instance> saturate(amount) {#instance-saturateamount}


**说明:**

将此颜色的饱和度增加给定百分比量。 饱和度是色调中基色的量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| amount | number | 否 | 百分比值可以改变此颜色。 数值在 0 到 100 之间 。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 此颜色对象 。


> 源码：[src/display/color/Color.js#L437](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L437)  
引入版本：3.13.0


---

### setFromHSV {#setFromHSV}

#### \<instance> setFromHSV(h, s, v) {#instance-setfromhsvh-s-v}


**说明:**

设置基于给定的色调、饱和度和值(HSV)组件的颜色。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| h | number | 否 | 色调,在0 - 1 度之间,这是底色. |
| s | number | 否 | 饱和度,在0 -1. 范围中,这控制了多少 的色调会在最后的颜色中,其中1 完全饱和,0 将给你白色. |
| v | number | 否 | 值,在 0 - 1. 范围中, 控制颜色的暗度。 当 1 尽可能亮, 0 则为黑色 。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 此颜色对象 。


> 源码：[src/display/color/Color.js#L293](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L293)  
引入版本：3.13.0


---

### setFromRGB {#setFromRGB}

#### \<instance> setFromRGB(color) {#instance-setfromrgbcolor}


**说明:**

根据给定的颜色对象设置颜色。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | [Phaser.Types.Display.InputColorObject](/api/typedef/types-display#inputcolorobject) | 否 | 含有`r`,`g`,`b`和可选的`a`值在0到255之间的天体. |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 此颜色对象 。


> 源码：[src/display/color/Color.js#L265](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L265)  
引入版本：3.0.0


---

### setGLTo {#setGLTo}

#### \<instance> setGLTo(red, green, blue, [alpha]) {#instance-setgltored-green-blue-alpha}


**说明:**

设置此颜色组件的红、绿、蓝和α GL 值。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| red | number | 否 |  | 红色值,数字在 0 到 1 之间 。 |
| green | number | 否 |  | 绿色的颜色值,数字在0到1之间. |
| blue | number | 否 |  | 蓝色的颜色值,数字在 0 到 1 之间 。 |
| alpha | number | 是 | 1 | α值,数字在0到1之间. |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 此颜色对象 。


> 源码：[src/display/color/Color.js#L236](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L236)  
引入版本：3.0.0


---

### setTo {#setTo}

#### \<instance> setTo(red, green, blue, [alpha], [updateHSV]) {#instance-settored-green-blue-alpha-updatehsv}


**说明:**

设置此颜色组件的颜色。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| red | number | 否 |  | 红色值,数字在0到255之间 |
| green | number | 否 |  | 绿色的颜色值,数字在0到255之间. |
| blue | number | 否 |  | 蓝色的颜色值,数字在0到255之间. |
| alpha | number | 是 | 255 | α值,数字在0到255之间. |
| updateHSV | boolean | 是 | true | 设置 RGB 值后更新 HSV 值吗 ? |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 此颜色对象 。


> 源码：[src/display/color/Color.js#L205](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L205)  
引入版本：3.0.0


---

### transparent {#transparent}

#### \<instance> transparent() {#instance-transparent}


**说明:**

设置此颜色为透明。 将所有值设置为零。


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 此颜色对象 。


> 源码：[src/display/color/Color.js#L183](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Color.js#L183)  
引入版本：3.0.0


---

### ValueToColor {#ValueToColor}

#### \<static> ValueToColor(input, [color]) {#static-valuetocolorinput-color}


**说明:**

将给定的源颜色值转换成颜色类实例。该值可以是字符串(前缀均不包含) `rgb` 表示已打包的 RGB 整数,或带有 `r`, `g`,和 `b` 属性。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| input | string \| number | [Phaser.Types.Display.InputColorObject](/api/typedef/types-display#inputcolorobject) | 否 | 要转换的源颜色值 。 |
| color | [Phaser.Display.Color](/api/namespace/display-color) | 是 | 保存结果的已有颜色对象。如果不提供,则创建并返回新的颜色对象。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 包含转换的颜色值的颜色对象。


> 源码：[src/display/color/ValueToColor.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/ValueToColor.js#L12)  
引入版本：3.0.0


---

## 命名空间 {#namespaces}

- [Interpolate](/api/namespace/display-color-interpolate)

---
