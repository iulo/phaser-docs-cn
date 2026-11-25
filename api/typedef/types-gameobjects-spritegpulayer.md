# Types.GameObjects.SpriteGPULayer {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-spritegpulayer)

## Member {#member}

### \<static> Member {#static-member}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number \| [Phaser.Types.GameObjects.SpriteGPULayer.MemberAnimation](/api/typedef/types-gameobjects-spritegpulayer#memberanimation) | 否 | 成员x位置. |
| y | number \| [Phaser.Types.GameObjects.SpriteGPULayer.MemberAnimation](/api/typedef/types-gameobjects-spritegpulayer#memberanimation) | 否 | 成员y的位置. |
| rotation | number \| [Phaser.Types.GameObjects.SpriteGPULayer.MemberAnimation](/api/typedef/types-gameobjects-spritegpulayer#memberanimation) | 否 | 成员轮换. |
| scaleX | number \| [Phaser.Types.GameObjects.SpriteGPULayer.MemberAnimation](/api/typedef/types-gameobjects-spritegpulayer#memberanimation) | 否 | 成员x的尺度. |
| scaleY | number \| [Phaser.Types.GameObjects.SpriteGPULayer.MemberAnimation](/api/typedef/types-gameobjects-spritegpulayer#memberanimation) | 否 | 成员y的尺度. |
| originX | number | 否 | 框架的 X 支点。 默认为 0. 5, 范围为 0 到 1 。 如果框架有自定义支点, 则将抵消这个值 。 |
| originY | number | 否 | 框架的 Y 支点。 默认为 0. 5, 范围为 0 到 1 。 如果框架有自定义支点, 则将抵消这个值 。 |
| tintMode | [Phaser.TintModes](/api/namespace/tintmodes) | 否 | 成员锡模式. |
| creationTime | number | 否 | 创建成员的时间。 是从 `layer.timeElapsed` 初始化中测量的。 使用此程序来控制在创建层后添加的成员 。 |
| scrollFactorX | number | 否 | 成员横向摄像机卷轴因子. |
| scrollFactorY | number | 否 | 成员的垂直摄像机滚动因子 y. |
| frame | string \| number | Object | 否 | 成员的框架。 您可以通过一个框架名称、 其纹理中的框架索引或 `Phaser.Types.Textures.Frame` 对象。 框架必须存在于成员使用的纹理中 。 |
| animation | string \| number | 是 | 要使用的动画。 如果未设定, 成员会使用 `frame` 来作为静态纹理 。 |
| tintBlend | number \| [Phaser.Types.GameObjects.SpriteGPULayer.MemberAnimation](/api/typedef/types-gameobjects-spritegpulayer#memberanimation) | 否 | 成员中的 tint 混合模式 。 0 是无 tint (相当于白色) , 1 是全 tint 。 使用此模式来表示 tint 值, 否则它们太复杂, 无法进行 antimate 。 |
| tintBottomLeft | number | 否 | 成员左下角的色调,作为24位的RGB值. |
| tintTopLeft | number | 否 | 成员左上角的颜色,作为24位的RGB值. |
| tintBottomRight | number | 否 | 成员右下角色,作为24位RGB值. |
| tintTopRight | number | 否 | 成员右上角色,作为24位RGB值. |
| alphaBottomLeft | number | 否 | 成员左下方的α值,在0-1之间. |
| alphaTopLeft | number | 否 | 成员左上方的α值,在0-1之间. |
| alphaBottomRight | number | 否 | 成员右下方的α值,在0-1之间. |
| alphaTopRight | number | 否 | 成员右上方的α值,在0-1范围内. |
| alpha | number \| [Phaser.Types.GameObjects.SpriteGPULayer.MemberAnimation](/api/typedef/types-gameobjects-spritegpulayer#memberanimation) | 否 | 成员在 0-1 范围内的α值,这个值将四个角的α值都乘以,并且可以被动画化. |

**类型**: object

**所属**: Phaser.Types.GameObjects.SpriteGPULayer
> 源码：[src/gameobjects/spritegpulayer/typedefs/Member.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/typedefs/Member.js#L1)  
引入版本：4.0.0

---

## MemberAnimation {#memberanimation}

### \<static> MemberAnimation {#static-memberanimation}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| base | number | 是 | 0 | 动画的基数值. |
| ease | number \| string | 是 | 0 | 动画的易懂值。 这必须是 `SpriteGPULayer.EASE` 的键或值, 如“ 边缘 ” 、 “ Quad. ZeaseIn ” 等 。 |
| amplitude | number | 是 | 0 | 动画的振幅. |
| duration | number | 是 | 0 | 动画的长度, 以毫秒计。 必须是非负数 。 |
| delay | number | 是 | 0 | 动画的延迟,以毫秒计. |
| loop | boolean | 是 | true | 0-1的动画循环(可选使用0-1-1的yoyo),还是延续到1以后1. 非扫射动画对一次性粒子效果可能有用. |
| yoyo | boolean | 是 | true | 动画完成后是否向后运行。 如果错误, 它会从头开始 。 |
| gravityFactor | number | 是 | 1 | 动画的重力因子。 如果易感是“ 重力 ” , 则使用此值, 而不是 `amplitude` 。 |
| velocity | number | 是 | 0 | 动画的速度。 必须是整数。 如果易用“ 重力 ” , 则使用 `amplitude` 。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.SpriteGPULayer
> 源码：[src/gameobjects/spritegpulayer/typedefs/MemberAnimation.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/typedefs/MemberAnimation.js#L1)  
引入版本：4.0.0

---

## SetAnimation {#setanimation}

### \<static> SetAnimation {#static-setanimation}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 动画名称. |
| frames | Array.\<number> \| Array.\<string> | 否 | 包含动画框的阵列. |
| duration | number | 否 | 动画的长度, 以毫秒计。 必须是非负数 。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.SpriteGPULayer
> 源码：[src/gameobjects/spritegpulayer/typedefs/SetAnimation.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/typedefs/SetAnimation.js#L1)  
引入版本：4.0.0

---

## SpriteGPULayerConfig {#spritegpulayerconfig}

### \<static> SpriteGPULayerConfig {#static-spritegpulayerconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| size | number | 否 |  | SpriteGPULayer 的大小; 内存中保留的四位数。 以后可以增加 。 |
| key | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 |  | 此游戏对象将使用用于渲染的纹理的键或实例, 如保存在纹理管理器中 。 |
| alpha | number | 是 | 1 | 游戏对象的α( opacity) 。 |
| blendMode | number | 是 | "BlendModes.DEFAULT" | 游戏对象的混合模式 。 |
| visible | boolean | 是 | true | 游戏对象的可见状态 。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.SpriteGPULayer
> 源码：[src/gameobjects/spritegpulayer/typedefs/SpriteGPULayerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/typedefs/SpriteGPULayerConfig.js#L1)  
引入版本：4.0.0

---

---
