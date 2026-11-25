# Types.Display {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-display)

## ColorBandConfig {#colorbandconfig}

### \<static> ColorBandConfig {#static-colorbandconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| colorStart | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0x000000" | 带首的颜色。指定颜色整数、六进制字符串、RGB或RGBA的阵列,范围为0-1,或颜色。 |
| colorEnd | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 |  | 乐队尾部的颜色,默认为`colorStart`. |
| start | number | 是 | 0 | 此带在一个 ColorRamp 中的起始点。 此值应在坡道内正常化, 介于 0( 启动) 到 1( 结束) 之间 。 |
| middle | number | 是 | 0.5 | 此带在 ColorRamp 内的中间点。 此值应在带内正常化, 在 0( 带启动) 和 1( 带端) 之间。 中点会改变颜色插值的形状 。 |
| end | number | 是 | 1 | 此带在 ColorRamp 内的终点。 此值应在坡道内, 0( ramp start) 和 1( ramp end) 之间实现正常化 。 |
| size | number | 是 |  | 色彩朗普中此带的大小。 此值应在斜坡内正常化, 在 0( 颜色朗普启动) 和 1( 颜色朗普端) 之间。 如果不指定 `end` , 则使用此值。 如果用于构造色彩朗普, 也可以设置下一个带的 `start` 。 |
| interpolation | number | 是 | 0 | 颜色插值。 这可以是以下代码之一 : - 0: LINEAR - 直配色 。 - 1: CURVED - 颜色在起始和结尾迅速变化, 在中间平整。 不错的凸起表面 。 - 2: SINUSOIDAL - 颜色在中间迅速变化, 在起始和结尾平整, 有利于平整过渡 。 - 3: CURVE_ StART - 颜色在起始时迅速变化, 在结尾平整 。 - 颜色在结尾迅速变化, 在起始时平整 。 这些功能与圆宽功能相似 。 |
| colorSpace | number | 是 | 0 | 插座的颜色空间。 这可以是以下代码之一 : - 0: RGBA - 通道直接混合, 这可能不准确 。 - 1: HSVA_ NEAREST - 颜色混合到 HSVA 空间中, 更好地保持饱和度和光度 。 色调与最短的角度混合, 例如红色和蓝色的混合通过紫色而不是绿色 。 - 2: HSVA _ NEAREST , 但色角总是增加 。 - 3: HSVA... MINUS - 作为 HSVA_NEAREST 的颜色, 但色角总是减少 。 |

**类型**: object

**所属**: Phaser.Types.Display
> 源码：[src/display/typedefs/ColorBandConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/typedefs/ColorBandConfig.js#L1)  
引入版本：4.0.0

---

## ColorObject {#colorobject}

### \<static> ColorObject {#static-colorobject}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| r | number | 否 | 0至255之间的红色值. |
| g | number | 否 | 0至255之间的绿色颜色值. |
| b | number | 否 | 0到255之间的蓝色颜色值. |
| a | number | 否 | 0到255之间的α色值. |
| color | number | 否 | 综合颜色值。 |

**类型**: object

**所属**: Phaser.Types.Display
> 源码：[src/display/typedefs/ColorObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/typedefs/ColorObject.js#L1)  
引入版本：3.0.0

---

## HSVColorObject {#hsvcolorobject}

### \<static> HSVColorObject {#static-hsvcolorobject}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| h | number | 否 | 颜色值。 0 到 1 之间的数字 |
| s | number | 否 | 饱和度颜色值。 0 到 1 之间的数字 |
| v | number | 否 | 亮度颜色值。 0 到 1 之间的数字 |

**类型**: object

**所属**: Phaser.Types.Display
> 源码：[src/display/typedefs/HSVColorObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/typedefs/HSVColorObject.js#L1)  
引入版本：3.0.0

---

## InputColorObject {#inputcolorobject}

### \<static> InputColorObject {#static-inputcolorobject}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| r | number | 是 | 0至255之间的红色值. |
| g | number | 是 | 0至255之间的绿色颜色值. |
| b | number | 是 | 0到255之间的蓝色颜色值. |
| a | number | 是 | 0到255之间的α色值. |

**类型**: object

**所属**: Phaser.Types.Display
> 源码：[src/display/typedefs/InputColorObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/typedefs/InputColorObject.js#L1)  
引入版本：3.0.0

---

---
