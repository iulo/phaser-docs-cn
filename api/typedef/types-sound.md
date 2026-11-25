# Types.Sound {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-sound)

## AudioSpriteSound {#audiospritesound}

### \<static> AudioSpriteSound {#static-audiospritesound}


音频图示音效类型 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| spritemap | object | 否 | 本地引用“ spritimap” 对象形式 json 文件, 由 音频sprite 工具生成 。 |

**类型**: object

**所属**: Phaser.Types.Sound
> 源码：[src/sound/typedefs/AudioSpriteSound.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/AudioSpriteSound.js#L1)  
引入版本：3.0.0

---

## DecodeAudioConfig {#decodeaudioconfig}

### \<static> DecodeAudioConfig {#static-decodeaudioconfig}


一个音频数据对象 。

您可以将其中的一组对象传递到 WebAudioSondManager `decodeAudio` 方法,使其解码
一次一次地把他们都杀了

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要用于引用音频缓存中解码音频的基于字符串的键 。 |
| data | ArrayBuffer \| string | 否 | 音频数据,要么是一个基数64编码字符串,一个音频媒体类型的数据uri,要么是一个ArrayBuffer实例. |

**类型**: object

**所属**: Phaser.Types.Sound
> 源码：[src/sound/typedefs/DecodeAudioConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/DecodeAudioConfig.js#L1)  
引入版本：3.18.0

---

## EachActiveSoundCallback {#eachactivesoundcallback}

### \<static> EachActiveSoundCallback {#static-eachactivesoundcallback}

**类型**: function

**所属**: Phaser.Types.Sound
> 源码：[src/sound/typedefs/EachActiveSoundCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/EachActiveSoundCallback.js#L1)  
引入版本：3.0.0

---

## SoundConfig {#soundconfig}

### \<static> SoundConfig {#static-soundconfig}


包含各种声音设置的配置对象。

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| mute | boolean | 是 | false | 布尔表示声音是否应当变音 。 |
| volume | number | 是 | 1 | 0(静态)到1(全容积)之间的值. |
| rate | number | 是 | 1 | 定义声音播放速度。 |
| detune | number | 是 | 0 | 代表[cents](https://en.wikipedia.org/wiki/Cent_%28music%29)中声音的调谐. |
| seek | number | 是 | 0 | 播放此声音的位置, 以秒计 。 |
| loop | boolean | 是 | false | 声音或当前声音标记是否应该循环 。 |
| delay | number | 是 | 0 | 时间,几秒钟, 时间应该会过去,然后声音才开始回放。 |
| pan | number | 是 | 0 | 值介于 -1( 完全左锅) 和 1( 完全右锅) 之间。 0 表示无 。 |
| source | [Phaser.Types.Sound.SpatialSoundConfig](/api/typedef/types-sound#spatialsoundconfig) | 是 | null | 一个包含默认空间声音设置的可选配置对象。 |

**类型**: object

**所属**: Phaser.Types.Sound
> 源码：[src/sound/typedefs/SoundConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/SoundConfig.js#L1)  
引入版本：3.0.0

---

## SoundMarker {#soundmarker}

### \<static> SoundMarker {#static-soundmarker}


标记以名称表示的声音的段落,并选择起始时间,持续时间,和配置对象.

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 名称 | string | 否 |  | 声音标记的独特标识符 。 |
| start | number | 是 | 0 | 音响位置抵消,该位置应开始播放。 |
| duration | number | 是 |  | 此标记的播放时间 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 |  | 包含默认标记设置的可选配置对象 。 |

**类型**: object

**所属**: Phaser.Types.Sound
> 源码：[src/sound/typedefs/SoundMarker.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/SoundMarker.js#L1)  
引入版本：3.0.0

---

## SpatialSoundConfig {#spatialsoundconfig}

### \<static> SpatialSoundConfig {#static-spatialsoundconfig}


包含空间声音源设置的配置对象。

见https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Web_audio_spatialization_basics

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 音频在右手笛卡尔坐标系统中的横向位置. |
| y | number | 是 | 0 | 音频在右手笛卡尔坐标系统中的垂直位置. |
| z | number | 是 | 0 | 代表音频在右手笛卡尔坐标系统中的纵向(前后)位置. |
| panningModel | 'equalpower' \| 'HRTF' | 是 | "'equalpower'" | 列出的数值决定了用于将音频定位在3D空间的空间化算法. |
| distanceModel | 'linear' \| 'inverse' | 'exponential' | 是 | "'inverse'" | 用于在音频源远离听器时减少音量的算法。 可能的值是“ 线性 ” 、 “ 反向 ” 和 “ 责任 ” 。 默认值是“ 反向 ” |
| orientationX | number | 是 | 0 | 音频源矢量在右手笛卡尔坐标系统中的横向位置. |
| orientationY | number | 是 | 0 | 音频源矢量在右手笛卡尔坐标系统中的垂直位置. |
| orientationZ | number | 是 | -1 | 代表音频源矢量在右手笛卡尔坐标系统中的纵向(前后)位置. |
| refDistance | number | 是 | 1 | 双值代表音频源离听器更远时减小音量的参考距离。 对于比此更大的音量,则会根据`rolloffFactor`和`distanceModel`来减小音量。 |
| maxDistance | number | 是 | 10000 | 音频源与听器的最大距离,之后音量不会再进一步缩小. |
| rolloffFactor | number | 是 | 1 | 双值描述当源代码远离听器时音量会如何快速减少。此值被所有距离模型使用 。 |
| coneInnerAngle | number | 是 | 360 | 其角,以度表示,内侧的锥体不会发生体积减量. |
| coneOuterAngle | number | 是 | 0 | 圆锥体外的角,以度为单位,其体积将减少一个恒值,由`coneOuterGain`属性定义. |
| coneOuterGain | number | 是 | 0 | `coneOuterAngle`属性定义的圆锥外的体积还原量,其默认值为0,表示无法听到声音。数值在0到1之间。 |
| follow | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 设定此声音对象可自动跟踪此对象的 x/y 位置。 可以是 Phaser 游戏对象, Vec2 或任何暴露 public x/y 属性的 。 |

**类型**: object

**所属**: Phaser.Types.Sound
> 源码：[src/sound/typedefs/SpatialSoundConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/SpatialSoundConfig.js#L1)  
引入版本：3.60.0

---

## WebAudioDecodeEntry {#webaudiodecodeentry}

### \<static> WebAudioDecodeEntry {#static-webaudiodecodeentry}


网络音频解码队列中的条目 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 声闻之钥. |
| success | function | 否 | 调用在成功的解码上 |
| failure | function | 否 | 如果解码失败, 调用回调 。 |
| decoding | boolean | 否 | 这个声音文件的解码工作已经开始了吗 ? |

**类型**: object

**所属**: Phaser.Types.Sound
> 源码：[src/sound/typedefs/WebAudioDecodeEntry.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/WebAudioDecodeEntry.js#L1)  
引入版本：3.60.0

---

---
