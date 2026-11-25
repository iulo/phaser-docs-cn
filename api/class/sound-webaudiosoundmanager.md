# WebAudioSoundManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/sound-webaudiosoundmanager)

网络音频API实施Phaser音效管理器.

这是Phaser中默认使用的用于浏览器支持Web Audio API的音频管理器,它创建和管理了`AudioContext`,通过主增益节点链来引导所有声音进行全局的哑音和音量控制,并通过在第一个用户交互上解锁音频来处理浏览器的自动播放策略.

使用此管理器在您的游戏中添加、 播放和控制声音。 它通过 S`this.sound` 访问到场景中。 如果浏览器不支持 Web Audio API, Phaser 将反之回到 `HTML5AudioSoundManager` 。

并非所有浏览器都能播放所有音频格式.

支持的有很好的指南:[Cross-browser audio basics: Audio codec support](https://developer.mozilla.org/en-US/Apps/Fundamentals/Audio_and_video_delivery/Cross-browser_audio_basics#Audio_Codec_Support).

**构造函数**

`new WebAudioSoundManager(game)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 参考当前游戏实例 。 |

---


**作用域**: static


**继承**

> [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager)  



> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L16)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager):**


 - [detune](/api/class/sound-basesoundmanager#detune)
 - [game](/api/class/sound-basesoundmanager#game)
 - [gameLostFocus](/api/class/sound-basesoundmanager#gameLostFocus)
 - [jsonCache](/api/class/sound-basesoundmanager#jsonCache)
 - [listenerPosition](/api/class/sound-basesoundmanager#listenerPosition)
 - [locked](/api/class/sound-basesoundmanager#locked)
 - [pauseOnBlur](/api/class/sound-basesoundmanager#pauseOnBlur)
 - [rate](/api/class/sound-basesoundmanager#rate)




---

## 公开成员 {#public-members}

### context {#context}

#### context: AudioContext {#context-audiocontext}


**说明:**

用于播放的音频康特文本 。


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L49)  
引入版本：3.0.0


---

### destination {#destination}

#### destination: AudioNode {#destination-audionode}


**说明:**

连接单个声音的目标节点 。


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L80)  
引入版本：3.0.0


---

### masterMuteNode {#masterMuteNode}

#### masterMuteNode: GainNode {#mastermutenode-gainnode}


**说明:**

负责控制全球变异的增益节点 。


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L58)  
引入版本：3.0.0


---

### masterVolumeNode {#masterVolumeNode}

#### masterVolumeNode: GainNode {#mastervolumenode-gainnode}


**说明:**

负责控制全球量的增益节点。


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L67](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L67)  
引入版本：3.0.0


---

### mute {#mute}

#### mute: boolean {#mute-boolean}


**Overrides:** Phaser.Sound.BaseSoundManager穆特( 穆特)


**Fires:** [Phaser.Sound.Events#event:GLOBAL_MUTE](/api/event/sound-events#global_mute)


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L537](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L537)  
引入版本：3.0.0


---

### volume {#volume}

#### volume: number {#volume-number}


**Overrides:** Phaser.Sound.BaseSoundManager数量


**Fires:** [Phaser.Sound.Events#event:GLOBAL_VOLUME](/api/event/sound-events#global_volume)


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L577](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L577)  
引入版本：3.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Events.EventEmitter](/api/class/events-eventemitter):**


 - [addListener](/api/class/events-eventemitter#addListener)
 - [emit](/api/class/events-eventemitter#emit)
 - [eventNames](/api/class/events-eventemitter#eventNames)
 - [listenerCount](/api/class/events-eventemitter#listenerCount)
 - [listeners](/api/class/events-eventemitter#listeners)
 - [off](/api/class/events-eventemitter#off)
 - [on](/api/class/events-eventemitter#on)
 - [once](/api/class/events-eventemitter#once)
 - [removeAllListeners](/api/class/events-eventemitter#removeAllListeners)
 - [removeListener](/api/class/events-eventemitter#removeListener)
 - [shutdown](/api/class/events-eventemitter#shutdown)





**From [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager):**


 - [addAudioSprite](/api/class/sound-basesoundmanager#addAudioSprite)
 - [get](/api/class/sound-basesoundmanager#get)
 - [getAll](/api/class/sound-basesoundmanager#getAll)
 - [getAllPlaying](/api/class/sound-basesoundmanager#getAllPlaying)
 - [isPlaying](/api/class/sound-basesoundmanager#isPlaying)
 - [pauseAll](/api/class/sound-basesoundmanager#pauseAll)
 - [play](/api/class/sound-basesoundmanager#play)
 - [playAudioSprite](/api/class/sound-basesoundmanager#playAudioSprite)
 - [remove](/api/class/sound-basesoundmanager#remove)
 - [removeAll](/api/class/sound-basesoundmanager#removeAll)
 - [removeByKey](/api/class/sound-basesoundmanager#removeByKey)
 - [resumeAll](/api/class/sound-basesoundmanager#resumeAll)
 - [setDetune](/api/class/sound-basesoundmanager#setDetune)
 - [setRate](/api/class/sound-basesoundmanager#setRate)
 - [stopAll](/api/class/sound-basesoundmanager#stopAll)
 - [stopByKey](/api/class/sound-basesoundmanager#stopByKey)




---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(key, [config]) {#instance-addkey-config}


**说明:**

将新声音添加到声音管理器中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 声音的密钥 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | 包含默认声音设置的可选配置对象。 |


**Overrides:** Phaser.Sound.BaseSoundManager添加( 添加 )


**返回值:** [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) - 新声闻例.


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L214](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L214)  
引入版本：3.0.0


---

### createAudioContext {#createAudioContext}

#### \<instance> createAudioContext(game) {#instance-createaudiocontextgame}


**说明:**

用于即时和返回音频文本实例的方法。 如果通过游戏配置提供了音频文本类实例, 则该实例将被返回。 如果您在从未适当刷新的页面( 如在 SPA 项目中) 重新装入 Phaser 游戏, 并且您想要重用已经更新的即时音频文本, 这样做会有所帮助 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 参考当前游戏实例 。 |


**返回值:** AudioContext - 用于播放的音频 Context 实例 。


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L135)  
引入版本：3.0.0


---

### decodeAudio {#decodeAudio}

#### \<instance> decodeAudio([audioKey], [audioData]) {#instance-decodeaudioaudiokey-audiodata}


**说明:**

将音频数据解码为一种通过Web Audio可以播放的格式。

音频数据可以是基数64编码字符串,音频介质类型数据uri,也可以是ArrayBuffer实例.

`audioKey`是用于将解码音频保存到音频缓存的密钥.

与其通过单个条目,不如通过`Phaser.Types.Sound.DecodeAudioConfig`对象的数组作为第一个也是唯一的参数。

解码是一个Async过程,所以要注意听好事件,知道解码完成的时间.

一旦音频解码,它就可以添加到声音管理器中,或者通过它的密钥播放.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| audioKey | Array.\<[Phaser.Types.Sound.DecodeAudioConfig](/api/typedef/types-sound#decodeaudioconfig)> \| string | 是 | 要用于引用音频缓存中解码音频的字符串键,或者一组音频配置对象. |
| audioData | ArrayBuffer \| string | 是 | 音频数据,要么是一个基数64编码字符串,一个音频媒体类型的数据uri,要么是一个ArrayBuffer实例. |


**Fires:** [Phaser.Sound.Events#event:DECODED](/api/event/sound-events#decoded), [Phaser.Sound.Events#event:DECODED_ALL](/api/event/sound-events#decoded_all)


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L234](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L234)  
引入版本：3.18.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

呼叫 Phaser.Sound.BaseSoundManager#destroy 方法并清理所有Web Audio API相关资源.


**Overrides:** Phaser.Sound.BaseSoundManager#销毁


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L485](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L485)  
引入版本：3.0.0


---

### onBlur {#onBlur}

#### \<instance> onBlur() {#instance-onblur}


**说明:**

如果 Phaser.Sound.WebAudioSoundManager# pauseOnBlur 设定为真实, 则内部用于挖掘声音管理器的方法 。


**Access:** 保护


**Overrides:** Phaser.Sound.BaseSoundManager#onBlur


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L391](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L391)  
引入版本：3.0.0


---

### onFocus {#onFocus}

#### \<instance> onFocus() {#instance-onfocus}


**说明:**

如果 Phaser.Sound.WebAudioSoundManager# pauseOnBlur 设定为真实,则内部用于恢复声音管理器的方法 。


**Access:** 保护


**Overrides:** Phaser.Sound.BaseSoundManager#onFocus


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L407](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L407)  
引入版本：3.0.0


---

### setAudioContext {#setAudioContext}

#### \<instance> setAudioContext(context) {#instance-setaudiocontextcontext}


**说明:**

这种方法需要一个新的音频Context引用,然后设置此声音管理器,用于所有播放的上下文 。

作为这个调用的一部分,它也断开主哑音和音量节点,然后在新的给定上下文上重新创建.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| context | AudioContext | 否 | 引用一个已经创建的音频Context 实例 。 |


**返回值:** [Phaser.Sound.WebAudioSoundManager](/api/class/sound-webaudiosoundmanager) - 网络音频管理者实例。


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L170](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L170)  
引入版本：3.21.0


---

### setListenerPosition {#setListenerPosition}

#### \<instance> setListenerPosition([x], [y]) {#instance-setlistenerpositionx-y}


**说明:**

在此 Web 音频上下文设置空间音频听器的 X 和 Y 位置 。

如果您将这种方法调用为没有参数, 它会默认为游戏画布的中点。 根据您正在制作的游戏类型, 您可能需要调用这种方法来不断重置听众位置为相机卷轴 。

调用这种方法对 HTML5Audio 没有任何作用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 是 | 空间音频听器的 x 位置 。 |
| y | number | 是 | 空间音频听众的y位置 。 |


**Overrides:** Phaser.Sound.BaseSoundManager#setListenerPosition


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L315](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L315)  
引入版本：3.60.0


---

### setMute {#setMute}

#### \<instance> setMute(value) {#instance-setmutevalue}


**说明:**

设置此声音管理器的变音状态 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | `true` 关闭所有的声音,`false` 解除它们。 |


**返回值:** [Phaser.Sound.WebAudioSoundManager](/api/class/sound-webaudiosoundmanager) - 此音声管理者.


**Fires:** [Phaser.Sound.Events#event:GLOBAL_MUTE](/api/event/sound-events#global_mute)


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L519](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L519)  
引入版本：3.3.0


---

### setVolume {#setVolume}

#### \<instance> setVolume(value) {#instance-setvolumevalue}


**说明:**

设置此声音管理器的音量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 此 Sound 管理器的全球音量 。 |


**返回值:** [Phaser.Sound.WebAudioSoundManager](/api/class/sound-webaudiosoundmanager) - 此音声管理者.


**Fires:** [Phaser.Sound.Events#event:GLOBAL_VOLUME](/api/event/sound-events#global_volume)


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L559](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L559)  
引入版本：3.3.0


---

### unlock {#unlock}

#### \<instance> unlock() {#instance-unlock}


**说明:**

在初始输入事件上解锁Web音频 API.

更多关于这个问题如何在这里处理,[this article](https://medium.com/@pgoloskokovic/unlocking-web-audio-the-smarter-way-8858218c0e09)。


**Overrides:** Phaser.Sound.BaseSoundManager#解锁


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L340](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L340)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update(time, delta) {#instance-updatetime-delta}


**说明:**

更新方法调用到每个游戏步骤 。

删除游戏中被破坏的声音并更新每个活动声音.


**Access:** 保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 请求动画框架或SetTimeout生成的当前时间戳 。 |
| delta | number | 否 | 三角洲时间已经过去 自上个框架。 |


**Overrides:** Phaser.Sound.BaseSoundManager#更新日期


**Fires:** [Phaser.Sound.Events#event:UNLOCKED](/api/event/sound-events#unlocked)


> 源码：[src/sound/webaudio/WebAudioSoundManager.js#L425](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSoundManager.js#L425)  
引入版本：3.0.0


---

---
