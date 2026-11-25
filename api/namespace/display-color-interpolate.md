# Phaser.Display.Color.Interpolate {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/display-color-interpolate)

Scope: 
static
> 源码：[src/display/color/Interpolate.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Interpolate.js#L11)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### ColorWithColor {#ColorWithColor}

#### \<static> ColorWithColor(color1, color2, [length], [index], [hsv], [hsvSign]) {#static-colorwithcolorcolor1-color2-length-index-hsv-hsvsign}


**说明:**

在所提供长度上将两个给定的颜色对象间插入。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| color1 | [Phaser.Display.Color](/api/namespace/display-color) | 否 |  | 第一个颜色对象。 |
| color2 | [Phaser.Display.Color](/api/namespace/display-color) | 否 |  | 第二色物标. |
| length | number | 是 | 100 | 距离内插到那边去 |
| index | number | 是 | 0 | 索引从. |
| hsv | boolean | 是 | false | 是否在 HSV 中插入 。 |
| hsvSign | number | 是 | 0 | 优先使用 HSV 插值。 0 离它最近, 负数总是减少 。 负数总是增加 。 |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) - 一个包含插值的物体。


> 源码：[src/display/color/Interpolate.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Interpolate.js#L102)  
引入版本：3.0.0


---

### ColorWithRGB {#ColorWithRGB}

#### \<static> ColorWithRGB(color, r, g, b, [length], [index]) {#static-colorwithrgbcolor-r-g-b-length-index}


**说明:**

将颜色对象和颜色值之间插入到所提供长度上。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| color | [Phaser.Display.Color](/api/namespace/display-color) | 否 |  | 颜色对象 。 |
| r | number | 否 |  | 红色价值。 |
| g | number | 否 |  | 绿色价值。 |
| b | number | 否 |  | 蓝值. |
| length | number | 是 | 100 | 距离内插到那边去 |
| index | number | 是 | 0 | 索引从. |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) - 一个包含插值的物体。


> 源码：[src/display/color/Interpolate.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Interpolate.js#L132)  
引入版本：3.0.0


---

### HSVWithHSV {#HSVWithHSV}

#### \<static> HSVWithHSV(h1, s1, v1, h2, s2, v2, [length], [index], [sign]) {#static-hsvwithhsvh1-s1-v1-h2-s2-v2-length-index-sign}


**说明:**

将两种给定的 HSV 颜色在所提供的长度内进行Interprotection 。 `sign` 参数控制了 hue 插值的方向: 0 找到最近的路径, 正值总是增加 hue, 负值总是减少 hue 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| h1 | number | 否 |  | 第一色的色调( 0 到 1 ) 。 |
| s1 | number | 否 |  | 初色饱和度( 0 到 1 ). |
| v1 | number | 否 |  | 第一色的值(亮度) (0比1). |
| h2 | number | 否 |  | 第二色的色调(0到1). |
| s2 | number | 否 |  | 第二色的饱和度( 0 到 1 ) 。 |
| v2 | number | 否 |  | 第二色的值( 亮度) (0 至 1 ) 。 |
| length | number | 是 | 100 | 距离内插到那边去 |
| index | number | 是 | 0 | 索引从. |
| sign | number | 是 | 0 | 色调插向. 0=最近,正数=总增,负数=总减. |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) - 一个包含插值的物体。


> 源码：[src/display/color/Interpolate.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Interpolate.js#L55)  
引入版本：4.0.0


---

### RGBWithRGB {#RGBWithRGB}

#### \<static> RGBWithRGB(r1, g1, b1, r2, g2, b2, [length], [index]) {#static-rgbwithrgbr1-g1-b1-r2-g2-b2-length-index}


**说明:**

将两者间给定的 RGB 颜色值在所提供长度上进行国际化 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| r1 | number | 否 |  | 红色价值。 |
| g1 | number | 否 |  | 绿色价值。 |
| b1 | number | 否 |  | 蓝值. |
| r2 | number | 否 |  | 红色价值。 |
| g2 | number | 否 |  | 绿色价值。 |
| b2 | number | 否 |  | 蓝值. |
| length | number | 是 | 100 | 距离内插到那边去 |
| index | number | 是 | 0 | 索引从. |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) - 一个包含插值的物体。


> 源码：[src/display/color/Interpolate.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Interpolate.js#L17)  
引入版本：3.0.0


---

---
