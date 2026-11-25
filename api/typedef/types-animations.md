# Types.Animations {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-animations)

## Animation {#animation}

### \<static> Animation {#static-animation}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 是 |  | 动画将关联的键, 即 spirite. animations. play( 关键) |
| frames | string \| Array.\<[Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe)> | 是 |  | 要么是字符串,在这种情况下它将使用与匹配键的纹理中的所有框架,要么是动画框架配置对象的数组. |
| sortFrames | boolean | 是 | true | 如果您为 `frames` 提供了字符串, 您可以选择对框架名称进行数字排序 。 |
| defaultTextureKey | string | 是 | null | 动画的所有帧都将使用纹理的键。 每个帧可以覆盖 。 |
| frameRate | number | 是 |  | 帧每秒播放的帧速率( 如果持续时间为空, 默认为 24) |
| duration | number | 是 |  | 动画播放时间为毫秒。 如果不是来自 frameRate 。 |
| skipMissedFrames | boolean | 是 | true | 如果时间滞后, 跳过框架, 还是总是向前? |
| delay | number | 是 | 0 | 延迟开始重播。 数值以毫秒计 。 |
| repeat | number | 是 | 0 | 重复动画的次数( 1 为无限) |
| repeatDelay | number | 是 | 0 | 动画重现前的延迟。 数值以毫秒表示 。 |
| yoyo | boolean | 是 | false | 动画Yoyo应该吗? |
| showBeforeDelay | boolean | 是 | false | 如果此动画有延迟, 它应该立即显示第一个帧( 真) , 或者只显示延迟( 假) 后 |
| showOnStart | boolean | 是 | false | 是否应该显示. 可见 = 真实值 当动画开始播放时? 如果设置, 会发生 _after_ any lady 。 |
| hideOnComplete | boolean | 是 | false | 动画完成时, should smart. visible=假? |
| randomFrame | boolean | 是 | false | 从随机选择的框架开始播放此动画 ? |

**类型**: object

**所属**: Phaser.Types.Animations
> 源码：[src/animations/typedefs/Animation.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/typedefs/Animation.js#L1)  
引入版本：3.0.0

---

## AnimationFrame {#animationframe}

### \<static> AnimationFrame {#static-animationframe}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 是 |  | 纹理管理器内用于此动画框架的纹理键 。 |
| frame | string \| number | 是 |  | 用于此动画框架的纹理内框架的键或索引号。 |
| duration | number | 是 | 0 | 动画的这个帧的长度,以ms表示. |
| visible | boolean | 是 |  | 父游戏对象是否在此动画框中可见 ? |

**类型**: object

**所属**: Phaser.Types.Animations
> 源码：[src/animations/typedefs/AnimationFrame.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/typedefs/AnimationFrame.js#L1)  
引入版本：3.0.0

---

## GenerateFrameNames {#generateframenames}

### \<static> GenerateFrameNames {#static-generateframenames}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| prefix | string | 是 | "''" | 如果使用 `frames` 的幅度或阵列, 将字符串附加到每个生成的框名中。 |
| start | number | 是 | 0 | 如果不提供`frames`,则返回第一个帧的编号。 |
| end | number | 是 | 0 | 如果不提供`frames`,则返回最后一个帧的编号。 |
| suffix | string | 是 | "''" | 如果使用 `frames` 的幅度或阵列, 将字符串附加到每个生成的框名中。 |
| zeroPad | number | 是 | 0 | 每个结果帧数的最小预期长度。 数字将被左加零, 直到它们如此长, 然后准备并附加以创建结果帧名 。 |
| outputArray | Array.\<[Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe)> | 是 | "[]" | 附加创建的配置对象的阵列 。 |
| frames | boolean \| Array.\<number> | 是 | false | 如果以数组形式提供,则`start`和`end`定义的范围将被忽略,这些帧数字将被使用. |

**类型**: object

**所属**: Phaser.Types.Animations
> 源码：[src/animations/typedefs/GenerateFrameNames.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/typedefs/GenerateFrameNames.js#L1)  
引入版本：3.0.0

---

## GenerateFrameNumbers {#generateframenumbers}

### \<static> GenerateFrameNumbers {#static-generateframenumbers}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| start | number | 是 | 0 | 动画的起始帧. |
| end | number | 是 | -1 | 动画的结局框架. |
| first | boolean \| number | 是 | false | 动画开头放置的帧,在`start`或`outputArray`或`frames`之前. |
| outputArray | Array.\<[Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe)> | 是 | "[]" | 将输出压缩到的数组 。 |
| frames | boolean \| Array.\<number> | 是 | false | 框的自定义序列 。 |

**类型**: object

**所属**: Phaser.Types.Animations
> 源码：[src/animations/typedefs/GenerateFrameNumbers.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/typedefs/GenerateFrameNumbers.js#L1)  
引入版本：3.0.0

---

## JSONAnimation {#jsonanimation}

### \<static> JSONAnimation {#static-jsonanimation}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 动画将关联的键, 即 spirite. animations. play( 关键) |
| 类型 | string | 否 | 基于帧的动画(相对于基于骨的动画) |
| frames | Array.\<[Phaser.Types.Animations.JSONAnimationFrame](/api/typedef/types-animations#jsonanimationframe)> | 否 | 本动画内部的动画Frame天体阵列. |
| frameRate | number | 否 | 帧每秒播放的帧速率( 如果持续时间为空, 默认为 24) |
| duration | number | 否 | 动画播放时间为毫秒。 如果不是来自 frameRate 。 |
| skipMissedFrames | boolean | 否 | 如果时间滞后, 跳过框架, 还是总是向前? |
| delay | number | 否 | 延迟开始重播。 数值以毫秒计 。 |
| repeat | number | 否 | 重复动画的次数( 1 为无限) |
| repeatDelay | number | 否 | 动画重现前的延迟。 数值以毫秒表示 。 |
| yoyo | boolean | 否 | 动画Yoyo应该吗? |
| showBeforeDelay | boolean | 否 | 如果此动画有延迟, 它应该立即显示第一个帧( 真) , 或者只显示延迟( 假) 后 |
| showOnStart | boolean | 否 | 动画开始播放时, should sprite. visible = true = 真实性? |
| hideOnComplete | boolean | 否 | 动画完成时, should smart. visible=假? |
| randomFrame | boolean | 是 | 从随机选择的框架开始播放此动画 ? |

**类型**: object

**所属**: Phaser.Types.Animations
> 源码：[src/animations/typedefs/JSONAnimation.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/typedefs/JSONAnimation.js#L1)  
引入版本：3.0.0

---

## JSONAnimationFrame {#jsonanimationframe}

### \<static> JSONAnimationFrame {#static-jsonanimationframe}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理的键 此动画Frame 使用. |
| frame | string \| number | 否 | 本动画Frame使用的纹理内框架的键 。 |
| duration | number | 否 | 播放时此帧应显示的额外时间( ms) 。 |

**类型**: object

**所属**: Phaser.Types.Animations
> 源码：[src/animations/typedefs/JSONAnimationFrame.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/typedefs/JSONAnimationFrame.js#L1)  
引入版本：3.0.0

---

## JSONAnimations {#jsonanimations}

### \<static> JSONAnimations {#static-jsonanimations}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| anims | Array.\<[Phaser.Types.Animations.JSONAnimation](/api/typedef/types-animations#jsonanimation)> | 否 | 动画管理器中添加了所有动画的阵列. |
| globalTimeScale | number | 否 | 动画管理器的全球时标. |

**类型**: object

**所属**: Phaser.Types.Animations
> 源码：[src/animations/typedefs/JSONAnimations.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/typedefs/JSONAnimations.js#L1)  
引入版本：3.0.0

---

## PlayAnimationConfig {#playanimationconfig}

### \<static> PlayAnimationConfig {#static-playanimationconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 动画要播放的基于字符串的键,或动画实例. |
| frameRate | number | 是 | 帧每秒播放的帧速率( 如果持续时间为空, 默认为 24) |
| duration | number | 是 | 动画播放时间为毫秒。 如果不是来自 frameRate 。 |
| delay | number | 是 | 延迟开始重播。 数值以毫秒计 。 |
| repeat | number | 是 | 重复动画的次数( 1 为无限) |
| repeatDelay | number | 是 | 动画重现前的延迟。 数值以毫秒表示 。 |
| yoyo | boolean | 是 | 动画Yoyo应该吗? |
| showBeforeDelay | boolean | 是 | 如果此动画有延迟, 它应该立即显示第一个帧( 真) , 或者只显示延迟( 假) 后 |
| showOnStart | boolean | 是 | 动画开始播放时, should sprite. visible = true = 真实性? |
| hideOnComplete | boolean | 是 | 动画完成时, should smart. visible=假? |
| skipMissedFrames | boolean | 是 | 如果时间滞后, 跳过框架, 还是总是向前? |
| startFrame | number | 是 | 动画的框式开始从此播放. |
| timeScale | number | 是 | 用于重播此动画的时间缩放倍率. |
| randomFrame | boolean | 是 | 从随机选择的框架开始播放此动画 ? |

**类型**: object

**所属**: Phaser.Types.Animations
> 源码：[src/animations/typedefs/PlayAnimationConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/typedefs/PlayAnimationConfig.js#L1)  
引入版本：3.50.0

---

---
