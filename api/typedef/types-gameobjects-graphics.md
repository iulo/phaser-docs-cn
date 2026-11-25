# Types.GameObjects.Graphics {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-graphics)

## FillStyle {#fillstyle}

### \<static> FillStyle {#static-fillstyle}


图形填充样式设置。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | number | 是 | 补色. |
| alpha | number | 是 | 填充的阿尔法。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Graphics
> 源码：[src/gameobjects/graphics/typedefs/FillStyle.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/typedefs/FillStyle.js#L1)  
引入版本：3.0.0

---

## LineStyle {#linestyle}

### \<static> LineStyle {#static-linestyle}


图形行样式(或中风样式)设置。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 是 | 中风宽度。 |
| color | number | 是 | 中风颜色. |
| alpha | number | 是 | 中风的α。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Graphics
> 源码：[src/gameobjects/graphics/typedefs/LineStyle.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/typedefs/LineStyle.js#L1)  
引入版本：3.0.0

---

## Options {#options}

### \<static> Options {#static-options}


图形游戏对象的选项。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 是 | 图形的x坐标 。 |
| y | number | 是 | 图形的y坐标 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Graphics
> 源码：[src/gameobjects/graphics/typedefs/Options.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/typedefs/Options.js#L1)  
引入版本：3.0.0

---

## RoundedRectRadius {#roundedrectradius}

### \<static> RoundedRectRadius {#static-roundedrectradius}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tl | number | 是 | 20 | 左上角半径。 如果半径为负, 则绘制圆弧 。 |
| tr | number | 是 | 20 | 右上角半径。 如果半径为负, 绘制圆弧 。 |
| br | number | 是 | 20 | 右下角半径,如果半径为负,请绘制圆弧 。 |
| bl | number | 是 | 20 | 左下角半径。 如果半径为负, 则绘制圆弧 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Graphics
> 源码：[src/gameobjects/graphics/typedefs/RoundedRectRadius.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/typedefs/RoundedRectRadius.js#L1)  
引入版本：3.11.0

---

## Styles {#styles}

### \<static> Styles {#static-styles}


图形样式设置。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| lineStyle | [Phaser.Types.GameObjects.Graphics.LineStyle](/api/typedef/types-gameobjects-graphics#linestyle) | 是 | 样式适用于形状轮廓. |
| fillStyle | [Phaser.Types.GameObjects.Graphics.FillStyle](/api/typedef/types-gameobjects-graphics#fillstyle) | 是 | 风格适用于形状区域. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Graphics
> 源码：[src/gameobjects/graphics/typedefs/Styles.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/typedefs/Styles.js#L1)  
引入版本：3.0.0

---

## WidePoint {#widepoint}

### \<static> WidePoint {#static-widepoint}


宽度的点,用来描述线上的点.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 是 | 点的x坐标. |
| y | number | 是 | 点的y坐标. |
| width | number | 是 | 点的宽度 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Graphics
> 源码：[src/gameobjects/graphics/typedefs/WidePoint.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/typedefs/WidePoint.js#L1)  
引入版本：4.0.0

---

---
