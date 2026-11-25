# Phaser.BlendModes {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/blendmodes)

Scope: 
static
> 源码：[src/renderer/BlendModes.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### ADD {#ADD}

#### ADD: number {#add-number}


**说明:**

添加混合模式。对于 Canvas 和 WebGL ,如果两者的形状重叠,则通过添加颜色值来决定颜色。


> 源码：[src/renderer/BlendModes.js#L37](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L37)  
引入版本：3.0.0


---

### COLOR {#COLOR}

#### COLOR: number {#color-number}


**说明:**

颜色混合模式。只用于 Canvas 。保护底层的润滑液,同时采用顶层的色素和铬。


> 源码：[src/renderer/BlendModes.js#L191](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L191)  
引入版本：3.0.0


---

### COLOR_BURN {#COLOR_BURN}

#### COLOR_BURN: number {#color_burn-number}


**说明:**

彩色 Burn 混合模式。只用于 Canvas 。将反向底层除以顶层,然后反转结果。


> 源码：[src/renderer/BlendModes.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L114)  
引入版本：3.0.0


---

### COLOR_DODGE {#COLOR_DODGE}

#### COLOR_DODGE: number {#color_dodge-number}


**说明:**

颜色道奇混合模式。只用于 Canvas 。将底层除以反向顶层。


> 源码：[src/renderer/BlendModes.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L103)  
引入版本：3.0.0


---

### COPY {#COPY}

#### COPY: number {#copy-number}


**说明:**

复制混合模式。 只用于 Canvas 。 只显示新形状 。


> 源码：[src/renderer/BlendModes.js#L311](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L311)  
引入版本：3.0.0


---

### DARKEN {#DARKEN}

#### DARKEN: number {#darken-number}


**说明:**

暗黑混合模式,只用于 Canvas 。 保留两层最黑暗的像素 。


> 源码：[src/renderer/BlendModes.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L81)  
引入版本：3.0.0


---

### DESTINATION_ATOP {#DESTINATION_ATOP}

#### DESTINATION_ATOP: number {#destination_atop-number}


**说明:**

目标- atop 混合模式。 仅用于 Canvas 。 现有的画布只保存在与新形状重叠的地方。 新形状被绘制在画布内容后面 。


> 源码：[src/renderer/BlendModes.js#L289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L289)  
引入版本：3.0.0


---

### DESTINATION_IN {#DESTINATION_IN}

#### DESTINATION_IN: number {#destination_in-number}


**说明:**

目标混合模式。 仅用于 Canvas 。 现有的画布内容保存在新形状和现有的画布内容重叠的地方。 其他内容都透明 。


> 源码：[src/renderer/BlendModes.js#L267](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L267)  
引入版本：3.0.0


---

### DESTINATION_OUT {#DESTINATION_OUT}

#### DESTINATION_OUT: number {#destination_out-number}


**说明:**

目标外混合模式。 只用于 Canvas 。 现有内容保存在不与新形状重叠的地方 。


> 源码：[src/renderer/BlendModes.js#L278](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L278)  
引入版本：3.0.0


---

### DESTINATION_OVER {#DESTINATION_OVER}

#### DESTINATION_OVER: number {#destination_over-number}


**说明:**

目标翻转混合模式。 仅用于 Canvas。 新的形状被绘制在已有画布内容后面 。


> 源码：[src/renderer/BlendModes.js#L256](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L256)  
引入版本：3.0.0


---

### DIFFERENCE {#DIFFERENCE}

#### DIFFERENCE: number {#difference-number}


**说明:**

差异混合模式。 仅用于 Canvas 。 从顶层或反方向将底层分解, 以获得正值 。


> 源码：[src/renderer/BlendModes.js#L147](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L147)  
引入版本：3.0.0


---

### ERASE {#ERASE}

#### ERASE: number {#erase-number}


**说明:**

阿尔法擦除混合模式,用于Canvas和WebGL.


> 源码：[src/renderer/BlendModes.js#L213](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L213)  
引入版本：3.0.0


---

### EXCLUSION {#EXCLUSION}

#### EXCLUSION: number {#exclusion-number}


**说明:**

排除混合模式,只用于Canvas,像不同,但对比度较低。


> 源码：[src/renderer/BlendModes.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L158)  
引入版本：3.0.0


---

### HARD_LIGHT {#HARD_LIGHT}

#### HARD_LIGHT: number {#hard_light-number}


**说明:**

硬光混合模式,只用于 Canvas 。 混合的复数和屏幕, 类似覆盖, 但上层和下层互换 。


> 源码：[src/renderer/BlendModes.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L125)  
引入版本：3.0.0


---

### HUE {#HUE}

#### HUE: number {#hue-number}


**说明:**

色调混合模式。只用于 Canvas 。 保护底层的露马和染色体, 同时采用顶层的色调 。


> 源码：[src/renderer/BlendModes.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L169)  
引入版本：3.0.0


---

### LIGHTEN {#LIGHTEN}

#### LIGHTEN: number {#lighten-number}


**说明:**

轻度混合模式,只用于Canvas,保留两层最轻度的像素.


> 源码：[src/renderer/BlendModes.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L92)  
引入版本：3.0.0


---

### LIGHTER {#LIGHTER}

#### LIGHTER: number {#lighter-number}


**说明:**

更轻的混合模式。只用于 Canvas。在两种形状重叠的情况下,颜色通过添加颜色值来确定。


> 源码：[src/renderer/BlendModes.js#L300](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L300)  
引入版本：3.0.0


---

### LUMINOSITY {#LUMINOSITY}

#### LUMINOSITY: number {#luminosity-number}


**说明:**

光度混合模式。只用于 Canvas 。保护下层的色素和染色体,同时采用顶层的色素。


> 源码：[src/renderer/BlendModes.js#L202](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L202)  
引入版本：3.0.0


---

### MULTIPLY {#MULTIPLY}

#### MULTIPLY: number {#multiply-number}


**说明:**

乘以混合模式。 对于 Canvas 和 WebGL , 顶层的像素与底层的对应像素相乘, 结果是更暗的图片 。


> 源码：[src/renderer/BlendModes.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L48)  
引入版本：3.0.0


---

### NORMAL {#NORMAL}

#### NORMAL: number {#normal-number}


**说明:**

普通混合模式。 对于 Canvas 和 WebGL , 这是默认设置, 并在已有画布内容上绘制新形状 。


> 源码：[src/renderer/BlendModes.js#L26](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L26)  
引入版本：3.0.0


---

### OVERLAY {#OVERLAY}

#### OVERLAY: number {#overlay-number}


**说明:**

重叠混合模式,只用于Canvas,是倍数和屏幕的组合,底层的暗部分变暗,光部分变轻.


> 源码：[src/renderer/BlendModes.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L70)  
引入版本：3.0.0


---

### SATURATION {#SATURATION}

#### SATURATION: number {#saturation-number}


**说明:**

饱和混合模式。只用于 Canvas 。 保留底层的润滑液和乳腺,同时采用顶层的铬。


> 源码：[src/renderer/BlendModes.js#L180](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L180)  
引入版本：3.0.0


---

### SCREEN {#SCREEN}

#### SCREEN: number {#screen-number}


**说明:**

屏幕混合模式。 对于 Canvas 和 WebGL 。 像素是反转的, 乘以, 并再次反转。 较轻的图片是结果( 相对于乘法) 。


> 源码：[src/renderer/BlendModes.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L59)  
引入版本：3.0.0


---

### SKIP_CHECK {#SKIP_CHECK}

#### SKIP_CHECK: number {#skip_check-number}


**说明:**

在渲染器中跳过混合模式检查 。


> 源码：[src/renderer/BlendModes.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L16)  
引入版本：3.0.0


---

### SOFT_LIGHT {#SOFT_LIGHT}

#### SOFT_LIGHT: number {#soft_light-number}


**说明:**

软光混合模式,只用于Canvas,硬光的更软版本,纯黑或白不会产生纯黑或白.


> 源码：[src/renderer/BlendModes.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L136)  
引入版本：3.0.0


---

### SOURCE_ATOP {#SOURCE_ATOP}

#### SOURCE_ATOP: number {#source_atop-number}


**说明:**

源头- atop 混合模式。 只用于 Canvas 。 新的形状只绘制与现有画布内容重叠的地方 。


> 源码：[src/renderer/BlendModes.js#L245](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L245)  
引入版本：3.0.0


---

### SOURCE_IN {#SOURCE_IN}

#### SOURCE_IN: number {#source_in-number}


**说明:**

源码混合模式。 只用于 Canvas 。 新形状只绘制在新形状和目的画布重叠的地方。 其他的都透明 。


> 源码：[src/renderer/BlendModes.js#L223](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L223)  
引入版本：3.0.0


---

### SOURCE_OUT {#SOURCE_OUT}

#### SOURCE_OUT: number {#source_out-number}


**说明:**

源代码混合模式。 仅用于 Canvas。 新的形状绘制在它不与现有的画布内容重叠的地方 。


> 源码：[src/renderer/BlendModes.js#L234](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L234)  
引入版本：3.0.0


---

### XOR {#XOR}

#### XOR: number {#xor-number}


**说明:**

Xor 混合模式。 仅用于 Canvas。 形状在其它地方都重叠和绘制正常的地方是透明的 。


> 源码：[src/renderer/BlendModes.js#L322](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/BlendModes.js#L322)  
引入版本：3.0.0


---

---
