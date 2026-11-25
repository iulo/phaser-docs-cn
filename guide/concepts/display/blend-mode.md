# 混合模式 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/display/blend-mode)

控制渲染时纹理与背景的混合。 设置混合模式会影响图示或游戏对象的颜色与后面像素的颜色的结合。

混合模式在 Canvas 和 WebGL 下,以及浏览器到浏览器之间, 取决于支持, 混合模式在遇到新的混合模式时也会产生 WebGL 批量冲洗。 由于这些原因, 请注意您所构建的场景和使用混合模式的频率 。

## WebGL 和彩色画 {#webgl-and-canvas}

- `'NORMAL'`,或 ,或 , `Phaser.BlendModes.NORMAL`,或 ,或 , `0`
  - 默认设置和绘制新形状, 覆盖现有画布内容 。
- `'ADD'`,或 ,或 , `Phaser.BlendModes.ADD`,或 ,或 , `1`
  - 在两种形状重叠的情况下,颜色通过添加颜色值来确定.
- `'MULTIPLY'`,或 ,或 , `Phaser.BlendModes.MULTIPLY`,或 ,或 , `2`
  - 像素属于顶层,与底层相应的像素相乘,结果为更暗的图片.
- `'SCREEN'`,或 ,或 , `Phaser.BlendModes.SCREEN`,或 ,或 , `3`
  - 像素是倒数,乘数,再反数,一个较轻的图片就是结果(对乘数)
- `'ERASE'`,或 ,或 , `Phaser.BlendModes.ERASE`,或 ,或 , `17`
  - Alpha 擦除混合模式。 只有在向帧缓冲器渲染时才有效, 如 * 渲染纹理 *

## 仅限画板 {#canvas-only}

- `'OVERLAY'`,或 ,或 , `Phaser.BlendModes.OVERLAY`,或 ,或 , `4`
  - 复数和屏幕的结合,底层上的暗部分变暗,光部分变轻.
- `'DARKEN'`,或 ,或 , `Phaser.BlendModes.DARKEN`,或 ,或 , `5`
  - 保留两层最黑暗的像素。
- `'LIGHTEN'`,或 ,或 , `Phaser.BlendModes.LIGHTEN`,或 ,或 , `6`
  - 保留两层最轻的像素.
- `'COLOR_DODGE'`,或 ,或 , `Phaser.BlendModes.COLOR_DODGE`,或 ,或 , `7`
  - 将底层除以倒数顶层。
- `'COLOR_BURN'`,或 ,或 , `Phaser.BlendModes.COLOR_BURN`,或 ,或 , `8`
  - 将倒转的底层除以顶层,然后反转结果。
- `'HARD_LIGHT'`,或 ,或 , `Phaser.BlendModes.HARD_LIGHT`,或 ,或 , `9`
  - 混合了倍数和屏幕,如覆面,但上层和下层互换.
- `'SOFT_LIGHT'`,或 ,或 , `Phaser.BlendModes.SOFT_LIGHT`,或 ,或 , `10`
  - 较软的硬灯版本,纯黑或白不会产生纯黑或白.
- `'DIFFERENCE'`,或 ,或 , `Phaser.BlendModes.DIFFERENCE`,或 ,或 , `11`
  - 从顶层或反方向切换下层,以获得一个正值。
- `'EXCLUSION'`,或 ,或 , `Phaser.BlendModes.EXCLUSION`,或 ,或 , `12`
  - 和不同,但对比较低
- `'HUE'`,或 ,或 , `Phaser.BlendModes.HUE`,或 ,或 , `13`
  - 保留底层的露马和染色体,同时采用顶层的花蕾.
- `'SATURATION'`,或 ,或 , `Phaser.BlendModes.SATURATION`,或 ,或 , `14`
  - 保留底层的露马和花蕾,同时采用顶层的染色体.
- `'COLOR'`,或 ,或 , `Phaser.BlendModes.COLOR`,或 ,或 , `15`
  - 保留底层的露米,同时采用顶层的乳腺和铬.
- `'LUMINOSITY'`,或 ,或 , `Phaser.BlendModes.LUMINOSITY`,或 ,或 , `16`
  - 保留底层层的乳腺和铬,同时采用顶层的乳腺.
- `'SOURCE_IN'`,或 ,或 , `Phaser.BlendModes.SOURCE_IN`,或 ,或 , `18`
  - 新的形状只有在新形状和目的地画布重叠时才画出来。其他的都透明。
- `'SOURCE_OUT'`,或 ,或 , `Phaser.BlendModes.SOURCE_OUT`,或 ,或 , `19`
  - 新形状绘制时不与现有的画布内容重叠.
- `'SOURCE_ATOP'`,或 ,或 , `Phaser.BlendModes.SOURCE_ATOP`,或 ,或 , `20`
  - 新形状只画在与现有画布内容重叠的地方.
- `'DESTINATION_OVER'`,或 ,或 , `Phaser.BlendModes.DESTINATION_OVER`,或 ,或 , `21`
  - 在现有画布内容后面绘制新的形状。
- `'DESTINATION_IN'`,或 ,或 , `Phaser.BlendModes.DESTINATION_IN`,或 ,或 , `22`
  - 现有的画布内容保存在新形状和现有的画布内容重叠的地方。其他内容都透明。
- `'DESTINATION_OUT'`,或 ,或 , `Phaser.BlendModes.DESTINATION_OUT`,或 ,或 , `23`
  - 现存内容保存在不与新形状重叠的地方.
- `'DESTINATION_ATOP'`,或 ,或 , `Phaser.BlendModes.DESTINATION_ATOP`,或 ,或 , `24`
  - 现有的画布只保存在与新形状重叠的地方。新形状在画布内容后面绘制。
- `'LIGHTER'`,或 ,或 , `Phaser.BlendModes.LIGHTER`,或 ,或 , `25`
  - 在两种形状重叠的情况下,颜色通过添加颜色值来确定.
- `'COPY'`,或 ,或 , `Phaser.BlendModes.COPY`,或 ,或 , `26`
  - 仅显示新形状 。
- `'XOR'`,或 ,或 , `Phaser.BlendModes.XOR`,或 ,或 , `27`
  - 形状在其他地方都重叠和正常地画出来时,是透明的。

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
