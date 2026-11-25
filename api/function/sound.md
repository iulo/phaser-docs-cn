# Phaser.Sound.SoundManagerCreator {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/function/sound)

### create {#create}

#### \<static> create(game) {#static-creategame}


**说明:**

确定最合适的 Sound Management , 以当前设备的游戏配置和音频能力为基础使用, 然后创建并返回实例 。

如果游戏配置有 `audio.noAudio` 设置为 `true`,或者设备既支持Web音频,也不支持HTML5音频,a `NoAudioSoundManager` 返回,默默地将所有声音调用。如果支持Web Audio,而不通过 `audio.disableWebAudio`, a 时 `WebAudioSoundManager` 返回。否则,则 `HTML5AudioSoundManager` 以倒置方式返回。

注意[https://developers.google.com/web/updates/2017/09/autoplay-policy-changes](https://developers.google.com/web/updates/2017/09/autoplay-policy-changes) 注意点

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 参考当前游戏实例 。 |


**返回值:** [Phaser.Sound.HTML5AudioSoundManager](/api/class/sound-html5audiosoundmanager), [Phaser.Sound.WebAudioSoundManager](/api/class/sound-webaudiosoundmanager), [Phaser.Sound.NoAudioSoundManager](/api/class/sound-noaudiosoundmanager) - 创建的 Sound 管理器实例 。


> 源码：[src/sound/SoundManagerCreator.js#L22](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/SoundManagerCreator.js#L22)  
引入版本：3.0.0

---
