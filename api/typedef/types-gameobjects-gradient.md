# Types.GameObjects.Gradient {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-gradient)

## GradientConfig {#gradientconfig}

### \<static> GradientConfig {#static-gradientconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | string \| [Phaser.Types.GameObjects.Gradient.GradientQuadConfig](/api/typedef/types-gameobjects-gradient#gradientquadconfig) | 是 |  | 此渐变将使用的配置对象 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Gradient
> 源码：[src/gameobjects/gradient/typedefs/GradientConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/gradient/typedefs/GradientConfig.js#L1)  
引入版本：4.0.0

---

## GradientQuadConfig {#gradientquadconfig}

### \<static> GradientQuadConfig {#static-gradientquadconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| bands | [Phaser.Types.Display.ColorBandConfig](/api/typedef/types-display#colorbandconfig) \| [Phaser.Display.ColorBand](/api/class/display-colorband) | Array.\<([Phaser.Types.Display.ColorBandConfig](/api/typedef/types-display#colorbandconfig) | [Phaser.Display.ColorBand](/api/class/display-colorband))> | 是 | "{colorStart: 0x000000, colorEnd: 0xffffff}" | 用于渐变的色彩框配置或实例。这些配置用于创建 `ColorRamp` 。 |
| offset | number | 是 | 0 | 梯度相抵。此梯度沿形状推进或撤回梯度 。 |
| repeatMode | number | 是 | 0 | 重复模式。 渐变进度被评价为数字, 其中 0 是 `shape` 向量的起始, 1 是结束。 请注意, 二次曲线梯度在非偏移时不会离开 0-1 的 。 如果您这样做, 可能看起来很怪异 。 重复模式告诉我们如何处理 0/ 以上 1 的数值 。 这可以是以下之一 : - 0 (EXTEND): 值被夹在 0 和 1 之间, 梯度的结尾会变成平整的颜色 。 - 1 (TRUNCATE): 值被丢弃在 0-1 之外, 梯度的结束会变得透明 。 - 2 (SA TOOTH): 值是 moulo 1, 所以梯度重复 。 - 3 (TRINGULAR): 值上升至 1, 然后下降至 0, 梯度会顺畅回转至 0 。 |
| shapeMode | number | 是 | 0 | 形状模式。形状基于 `shape` 矢量。 这可以是以下之一: - 0 (LINEAR): 一种从一边到另一边的形状指向另一边的丝带。 通常用于天空等。 - 1 (BILINEAR): 如LINEAR一样, 但双向反射。 用于温和的波浪、反射等。 - 2 (RADIAL): 梯度从天向外扩散。 `start`,以至描述的半径 `shape`,用于发光、波纹等。 - 3(CONIC_SYMMETRIC):梯度由角度决定到 `shape`,从形状向量0到对面1。对于锐视特性或光效应有用。 - 4(CONIC_ASYMMETRIC):梯度由角度决定到 `shape`,从 0 到 1 , 并带有一个完整的旋转。这可以创建一个接合器。 用于创建带有角度变化的颜色, 如速度表。 |
| start | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 | "{x: 0, y: 0}" | 梯度的起始,其中0为上/左,1为下/右。 |
| shape | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 | "{x: 1, y: 0}" | 梯度的形状,作为矢量从起始点指向的形状。默认情况下,梯度会跨越其对象的宽度。 |
| length | number | 是 | 1 | 梯度的长度。 如果未定义 `shape` , 则使用此方法 。 |
| direction | number | 是 | 0 | 梯度的方向。 如果未定义 `shape` , 则使用此方法 。 |
| dither | boolean | 是 |  | 是否将梯度缩小。 向输出引入噪声可以消除带宽。 当渐变或缩放时, 此效果会丢失, 所以只有在您想要时才会启用 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Gradient
> 源码：[src/gameobjects/gradient/typedefs/GradientQuadConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/gradient/typedefs/GradientQuadConfig.js#L1)  
引入版本：4.0.0

---

---
