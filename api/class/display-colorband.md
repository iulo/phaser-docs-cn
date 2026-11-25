# ColorBand {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/display-colorband)

彩色屏类代表着从一个颜色到另一个颜色的过渡。它用于一个 QQSee Phaser.Display.ColorRamp} , 并构成一个 XPhaser.GameObjects.Gradient} 的基础 。

ColorBand可以通过设置中间点,混合的色彩空间,以及插图风格来控制过渡.

本类还记录了`start`和`end`的点数,用于斜坡,这些点数表明它在斜坡内的位置。

色彩处理不预先多倍化,因此RGB值可能大于α.

**构造函数**

`new ColorBand([config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Display.ColorBandConfig](/api/typedef/types-display#colorbandconfig) | 是 | 用于乐队的配置 。 |

---


**作用域**: static

> 源码：[src/display/ColorBand.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorBand.js#L13)  
引入版本：4.0.0

## 公开成员 {#public-members}

### colorEnd {#colorEnd}

#### colorEnd: [Phaser.Display.Color](/api/namespace/display-color) {#colorend-phaserdisplaycolor}


**说明:**

颜色乐队的尾部的颜色.


> 源码：[src/display/ColorBand.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorBand.js#L60)  
引入版本：4.0.0


---

### colorSpace {#colorSpace}

#### colorSpace: number {#colorspace-number}


**说明:**

插值的颜色空间。 这可以是以下代码之一 :

- 0: RGBA - 频道直接混合.

  这会产生一些不准确的结果,因为混合

  在RGB空间中,不考虑人类对颜色的看法.

- 1: HSVA_NEAREST - 颜色混合在HSVA空间中,

  更好地保持饱和和轻度。

  色调与最短的角度混合,例如红色和蓝色

  混合通过紫色,而不是绿色。

- 2: HSVA_PLUS - 与HSVA_NEAREST一样,但hue角度总是增加.

- 3: HSVA_MINUS - 作为HSVA_NEAREST,但hue角度总是下降.


> 源码：[src/display/ColorBand.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorBand.js#L135)  
引入版本：4.0.0


---

### colorStart {#colorStart}

#### colorStart: [Phaser.Display.Color](/api/namespace/display-color) {#colorstart-phaserdisplaycolor}


**说明:**

颜色乐队开头的颜色.


> 源码：[src/display/ColorBand.js#L51](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorBand.js#L51)  
引入版本：4.0.0


---

### end {#end}

#### end: number {#end-number}


**说明:**

此带在 ColorRamp 内的终点。 此值应在坡道内, 0( ramp start) 和 1( ramp end) 之间实现正常化 。


> 源码：[src/display/ColorBand.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorBand.js#L98)  
引入版本：4.0.0


---

### interpolation {#interpolation}

#### interpolation: number {#interpolation-number}


**说明:**

颜色插值。 这可以是以下代码之一 :

- 林恩 - 一个直立的混合体。

- 1: CURVED - 颜色在开始和结束时迅速变化,

  中间平整,适合凸起表面.

- 2: SINUSOIDAL - 颜色在中间变化很快,

  平整始末,有利于平稳过渡.

- 3: CURVE_START - 颜色在开始时迅速变化,

  平地在终.

- 4: CURVE_END - 颜色在结尾变化很快,

  初平调.

模式2、3和4直接使用循环宽松功能. 模式1使用基于单位圆的相关自订公式.


> 源码：[src/display/ColorBand.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorBand.js#L111)  
引入版本：4.0.0


---

### isColorBand {#isColorBand}

#### isColorBand: boolean {#iscolorband-boolean}


**说明:**

将对象识别为色彩屏。 此属性只读, 不可修改 。


> 源码：[src/display/ColorBand.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorBand.js#L39)  
引入版本：4.0.0


---

### middle {#middle}

#### middle: number {#middle-number}


**说明:**

此带在 ColorRamp 内的中间点。 此值应在带内正常化, 在 0( 带启动) 和 1( 带端) 之间。 中点会改变颜色插值的形状 。

从数学上讲, 中间的梯度应该是0. 5。 我们用伽玛曲线来调整梯度。 因此, `0.5 = middle^gamma`。 因此, 用对数的属性来表示 `gamma = log base middle of 0.5`。


> 源码：[src/display/ColorBand.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorBand.js#L80)  
引入版本：4.0.0


---

### start {#start}

#### start: number {#start-number}


**说明:**

此带在一个 ColorRamp 中的起始点。 此值应在坡道内正常化, 介于 0( 启动) 到 1( 结束) 之间 。


> 源码：[src/display/ColorBand.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorBand.js#L69)  
引入版本：4.0.0


---

## 公开方法 {#public-methods}

### getColor {#getColor}

#### \<instance> getColor(index) {#instance-getcolorindex}


**说明:**

返回此带内一个正态位置的混合颜色。 中间点伽马曲线、 插值模式和颜色空间在混合 `colorStart` 和 `colorEnd` 之前都应用了 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 乐队内部的正常化位置,其中0为乐队开始,1为乐队结束. |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) - 位置上的混合颜色


> 源码：[src/display/ColorBand.js#L225](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorBand.js#L225)  
引入版本：4.0.0


---

### setColors {#setColors}

#### \<instance> setColors([start], [end]) {#instance-setcolorsstart-end}


**说明:**

设定乐队的颜色, 从各种颜色格式。

- 一个数字预计为24或32位RGB或ARGB值.

- 字符串是六进制码 。

- 一组数字预计在0-1之间是RGB或RGBA.

- 可用一个颜色对象。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| start | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0x000000" | 乐队开始时的颜色. |
| end | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 |  | 带尾的颜色。 如果未指定, 则等于 `start` 。 |


**返回值:** [Phaser.Display.ColorBand](/api/class/display-colorband) - 此彩条 。


> 源码：[src/display/ColorBand.js#L159](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorBand.js#L159)  
引入版本：4.0.0


---

---
