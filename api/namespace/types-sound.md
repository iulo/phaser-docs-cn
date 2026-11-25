# Phaser.Types.Sound {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/types-sound)

Scope: 
static
> 源码：[src/sound/typedefs/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/index.js#L7)  


## 静态函数 {#static-functions}

### AudioSpriteSound {#AudioSpriteSound}

#### AudioSpriteSound {#audiospritesound}


**说明:**

音频图示音效类型 。


> 源码：[src/sound/typedefs/AudioSpriteSound.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/AudioSpriteSound.js#L1)  
引入版本：3.0.0


---

### DecodeAudioConfig {#DecodeAudioConfig}

#### DecodeAudioConfig {#decodeaudioconfig}


**说明:**

一个音频数据对象 。

您可以将其中的一组对象传递到 WebAudioSundManager `decodeAudio` 方法,以便它同时解码它们的全部.


> 源码：[src/sound/typedefs/DecodeAudioConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/DecodeAudioConfig.js#L1)  
引入版本：3.18.0


---

### EachActiveSoundCallback {#EachActiveSoundCallback}

#### EachActiveSoundCallback {#eachactivesoundcallback}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.BaseSound](/api/class/sound-basesound) | 否 | 当前活动声音 |
| index | number | 否 | 当前活动声音的索引 |
| sounds | Array.\<[Phaser.Sound.BaseSound](/api/class/sound-basesound)> | 否 | 全部声音 |


> 源码：[src/sound/typedefs/EachActiveSoundCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/EachActiveSoundCallback.js#L1)  
引入版本：3.0.0


---

### SoundConfig {#SoundConfig}

#### SoundConfig {#soundconfig}


**说明:**

包含各种声音设置的配置对象。


> 源码：[src/sound/typedefs/SoundConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/SoundConfig.js#L1)  
引入版本：3.0.0


---

### SoundMarker {#SoundMarker}

#### SoundMarker {#soundmarker}


**说明:**

标记以名称表示的声音的段落,并选择起始时间,持续时间,和配置对象.


> 源码：[src/sound/typedefs/SoundMarker.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/SoundMarker.js#L1)  
引入版本：3.0.0


---

### SpatialSoundConfig {#SpatialSoundConfig}

#### SpatialSoundConfig {#spatialsoundconfig}


**说明:**

包含空间声音源设置的配置对象。

见[https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Web_audio_spatialization_basics](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Web_audio_spatialization_basics)


> 源码：[src/sound/typedefs/SpatialSoundConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/SpatialSoundConfig.js#L1)  
引入版本：3.60.0


---

### WebAudioDecodeEntry {#WebAudioDecodeEntry}

#### WebAudioDecodeEntry {#webaudiodecodeentry}


**说明:**

网络音频解码队列中的条目 。


> 源码：[src/sound/typedefs/WebAudioDecodeEntry.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/typedefs/WebAudioDecodeEntry.js#L1)  
引入版本：3.60.0


---

---
