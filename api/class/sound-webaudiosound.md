# WebAudioSound {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/sound-webaudiosound)

基于Web Audio API的音效实例,可以播放,暂停,停止,循环,并实时控制其音量,速率,调试,泛,空间位置.

这是浏览器中可用Web Audio API时Phaser使用的默认声音执行,它内部使用一个AudioBuffer SourceNode,其中的GainNodes用于音量和变异,一个可选的立体式PannerNode用于立体式平板电脑,以及一个可选的PannerNode用作3D空间音频定位.

如果无法使用Web音频 API, Phaser 将返回 HTML5 音频执行。您通常不会直接创建WebAudioSoud 实例;而是在场景内通过 `this.sound.add(key)`使用声音管理器。

**构造函数**

`new WebAudioSound(manager, key, [config])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| manager | [Phaser.Sound.WebAudioSoundManager](/api/class/sound-webaudiosoundmanager) | 否 |  | 引用此声音实例的 WebAudio 声音管理器 。 |
| key | string | 否 |  | 声音的密钥 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | "{}" | 包含默认声音设置的可选配置对象。 |

---


**作用域**: static


**继承**

> [Phaser.Sound.BaseSound](/api/class/sound-basesound)  



> 源码：[src/sound/webaudio/WebAudioSound.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L13)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Sound.BaseSound](/api/class/sound-basesound):**


 - [currentMarker](/api/class/sound-basesound#currentMarker)
 - [duration](/api/class/sound-basesound#duration)
 - [isPaused](/api/class/sound-basesound#isPaused)
 - [isPlaying](/api/class/sound-basesound#isPlaying)
 - [key](/api/class/sound-basesound#key)
 - [manager](/api/class/sound-basesound#manager)
 - [markers](/api/class/sound-basesound#markers)
 - [pendingRemove](/api/class/sound-basesound#pendingRemove)
 - [totalDuration](/api/class/sound-basesound#totalDuration)
 - [totalRate](/api/class/sound-basesound#totalRate)




---

## 公开成员 {#public-members}

### audioBuffer {#audioBuffer}

#### audioBuffer: AudioBuffer {#audiobuffer-audiobuffer}


**说明:**

包含要播放的音频资产解码数据的音频缓冲器.


> 源码：[src/sound/webaudio/WebAudioSound.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L47)  
引入版本：3.0.0


---

### detune {#detune}

#### detune: number {#detune-number}


**说明:**

此声音的调值, 以 [cents](https://en.wikipedia.org/wiki/Cent_%28music%29) 给出。 值的范围为 - 1200 到 1200, 但我们建议设定为 [50](https://en.wikipedia.org/wiki/50_Cent) 。


**Fires:** [Phaser.Sound.Events#event:DETUNE](/api/event/sound-events#detune)


> 源码：[src/sound/webaudio/WebAudioSound.js#L839](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L839)  
引入版本：3.0.0


---

### hasEnded {#hasEnded}

#### hasEnded: boolean {#hasended-boolean}


**说明:**

当声音源回放结束时用于保持跟踪,以便其状态可以相应更新.


> 源码：[src/sound/webaudio/WebAudioSound.js#L185](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L185)  
引入版本：3.0.0


---

### hasLooped {#hasLooped}

#### hasLooped: boolean {#haslooped-boolean}


**说明:**

当声音源循环时用于保持跟踪,从而可以对其状态进行相应的更新.


> 源码：[src/sound/webaudio/WebAudioSound.js#L197](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L197)  
引入版本：3.0.0


---

### loop {#loop}

#### loop: boolean {#loop-boolean}


**说明:**

显示声音或当前声音标记是否循环的旗帜 。


**Fires:** [Phaser.Sound.Events#event:LOOP](/api/event/sound-events#loop)


> 源码：[src/sound/webaudio/WebAudioSound.js#L1049](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L1049)  
引入版本：3.0.0


---

### loopSource {#loopSource}

#### loopSource: AudioBufferSourceNode {#loopsource-audiobuffersourcenode}


**说明:**

引用用于无漏洞循环播放的第二个音频源 。


> 源码：[src/sound/webaudio/WebAudioSound.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L72)  
引入版本：3.0.0


---

### loopTime {#loopTime}

#### loopTime: number {#looptime-number}


**说明:**

声音循环源实际开始回放的时间.

基于`BaseAudioContext.currentTime`值.


> 源码：[src/sound/webaudio/WebAudioSound.js#L159](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L159)  
引入版本：3.0.0


---

### mute {#mute}

#### mute: boolean {#mute-boolean}


**说明:**

获取或设置此声音的哑音状态.


**Fires:** [Phaser.Sound.Events#event:MUTE](/api/event/sound-events#mute)


> 源码：[src/sound/webaudio/WebAudioSound.js#L886](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L886)  
引入版本：3.0.0


---

### muteNode {#muteNode}

#### muteNode: GainNode {#mutenode-gainnode}


**说明:**

控制声音的节点变弱


> 源码：[src/sound/webaudio/WebAudioSound.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L82)  
引入版本：3.0.0


---

### pan {#pan}

#### pan: number {#pan-number}


**说明:**

获取或设置此声音的 pan, 值介于 - 1 (完全左锅) 和 1 (完全右锅) 之间 。

总是在iOS / Safari 上返回0,因为它不支持立体式泛纳节点.


**Fires:** [Phaser.Sound.Events#event:PAN](/api/event/sound-events#pan)


> 源码：[src/sound/webaudio/WebAudioSound.js#L1101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L1101)  
引入版本：3.50.0


---

### pannerNode {#pannerNode}

#### pannerNode: StereoPannerNode {#pannernode-stereopannernode}


**说明:**

控制这声音的平板结

只有在设备支持的情况下才会创建。 可能无法使用 iOS / Safari 。


> 源码：[src/sound/webaudio/WebAudioSound.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L100)  
引入版本：3.50.0


---

### playTime {#playTime}

#### playTime: number {#playtime-number}


**说明:**

声音应该从开始开始播放的时代.

将此属性视为只读 。

基于`BaseAudioContext.currentTime`值.


> 源码：[src/sound/webaudio/WebAudioSound.js#L131](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L131)  
引入版本：3.0.0


---

### rate {#rate}

#### rate: number {#rate-number}


**说明:**

播放此声音的速度 。 值为 1.0 的播放音频全速, 值为 0. 5 的播放音频半速, 值为 2.0 的播放速度的两倍 。


**Fires:** [Phaser.Sound.Events#event:RATE](/api/event/sound-events#rate)


> 源码：[src/sound/webaudio/WebAudioSound.js#L789](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L789)  
引入版本：3.0.0


---

### rateUpdates {#rateUpdates}

#### rateUpdates: array {#rateupdates-array}


**说明:**

用于在播放时跟踪所有速率更新的阵列 。

将此属性视为只读 。

对象类型阵列: `{ time: number, rate: number }`


> 源码：[src/sound/webaudio/WebAudioSound.js#L171](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L171)  
引入版本：3.0.0


---

### seek {#seek}

#### seek: number {#seek-number}


**说明:**

代表此声音的播放位置的属性, 以秒计。 设置到特定值后, 将当前播放的播放移动到该位置。 给出的值被夹在 0 到当前标记持续时间之间。 设置一个已停止的声音的搜索没有效果 。


**Fires:** [Phaser.Sound.Events#event:SEEK](/api/event/sound-events#seek)


> 源码：[src/sound/webaudio/WebAudioSound.js#L973](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L973)  
引入版本：3.0.0


---

### source {#source}

#### source: AudioBufferSourceNode {#source-audiobuffersourcenode}


**说明:**

用于播放存储在Phaser.Sound.WebAudioSound#audioBuffer的音频数据的回放音频的音频源节点的引用.


> 源码：[src/sound/webaudio/WebAudioSound.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L61)  
引入版本：3.0.0


---

### spatialNode {#spatialNode}

#### spatialNode: PannerNode {#spatialnode-pannernode}


**说明:**

立体空间全景节点.


> 源码：[src/sound/webaudio/WebAudioSound.js#L112](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L112)  
引入版本：3.60.0


---

### spatialSource {#spatialSource}

#### spatialSource: [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) {#spatialsource-phasertypesmathvector2like}


**说明:**

如果空间泛纳节点已经设定用于跟踪一个向量或游戏对象,则此选项保留了引用.


> 源码：[src/sound/webaudio/WebAudioSound.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L121)  
引入版本：3.60.0


---

### startTime {#startTime}

#### startTime: number {#starttime-number}


**说明:**

声音源应该开始回放的时间.

将此属性视为只读 。

基于`BaseAudioContext.currentTime`值.


> 源码：[src/sound/webaudio/WebAudioSound.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L145)  
引入版本：3.0.0


---

### volume {#volume}

#### volume: number {#volume-number}


**说明:**

获取或设置此声音的音量,值介于 0(静态)到 1(全音量)之间.


**Fires:** [Phaser.Sound.Events#event:VOLUME](/api/event/sound-events#volume)


> 源码：[src/sound/webaudio/WebAudioSound.js#L930](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L930)  
引入版本：3.0.0


---

### volumeNode {#volumeNode}

#### volumeNode: GainNode {#volumenode-gainnode}


**说明:**

负责控制声音的音量的节点。


> 源码：[src/sound/webaudio/WebAudioSound.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L91)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

获取或设置此声音在空间音频空间中的x位置.

只有用空间声波对象创建声音时,此效果才有效果.

也参看`WebAudioSoundManager.setListenerPosition`方法.

如果您发现声音变得太安静,太快,因为它远离了听觉者,那么在配置空间声音时,就尝试不同的`refDistance`属性值.


> 源码：[src/sound/webaudio/WebAudioSound.js#L539](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L539)  
引入版本：3.60.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

获取或设置此声音在空间音频空间中的y位置 。

只有用空间声波对象创建声音时,此效果才有效果.

也参看`WebAudioSoundManager.setListenerPosition`方法.

如果您发现声音变得太安静,太快,因为它远离了听觉者,那么在配置空间声音时,就尝试不同的`refDistance`属性值.


> 源码：[src/sound/webaudio/WebAudioSound.js#L577](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L577)  
引入版本：3.60.0


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





**From [Phaser.Sound.BaseSound](/api/class/sound-basesound):**


 - [addMarker](/api/class/sound-basesound#addMarker)
 - [removeMarker](/api/class/sound-basesound#removeMarker)
 - [resetConfig](/api/class/sound-basesound#resetConfig)
 - [updateMarker](/api/class/sound-basesound#updateMarker)




---

## 公开方法 {#public-methods}

### applyConfig {#applyConfig}

#### \<instance> applyConfig() {#instance-applyconfig}


**说明:**

将配置值应用到一些声音属性时内部使用的方法.


**Overrides:** Phaser.Sound.BaseSound#applyConfig


> 源码：[src/sound/webaudio/WebAudioSound.js#L493](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L493)  
引入版本：3.0.0


---

### calculateRate {#calculateRate}

#### \<instance> calculateRate() {#instance-calculaterate}


**说明:**

内部用于计算声音总回放率的方法.


**Overrides:** Phaser.Sound.BaseSound#calculateRate


> 源码：[src/sound/webaudio/WebAudioSound.js#L707](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L707)  
引入版本：3.0.0


---

### createAndStartLoopBufferSource {#createAndStartLoopBufferSource}

#### \<instance> createAndStartLoopBufferSource() {#instance-createandstartloopbuffersource}


**说明:**

这种方法仅内部使用,并产生循环缓冲源.


> 源码：[src/sound/webaudio/WebAudioSound.js#L392](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L392)  
引入版本：3.0.0


---

### createBufferSource {#createBufferSource}

#### \<instance> createBufferSource() {#instance-createbuffersource}


**说明:**

这种方法仅内部使用,并产生缓冲源.


**返回值:** AudioBufferSourceNode - 


> 源码：[src/sound/webaudio/WebAudioSound.js#L410](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L410)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

呼叫 Phaser.Sound.BaseSound#destroy 方法并断开所有Web音频 API 节点,释放所有音频资源的引用.


**Overrides:** Phaser.Sound.BaseSound#销毁


> 源码：[src/sound/webaudio/WebAudioSound.js#L667](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L667)  
引入版本：3.0.0


---

### getCurrentTime {#getCurrentTime}

#### \<instance> getCurrentTime() {#instance-getcurrenttime}


**说明:**

用于计算播放声音当前播放时间的内部方法。


> 源码：[src/sound/webaudio/WebAudioSound.js#L739](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L739)  
引入版本：3.0.0


---

### getLoopTime {#getLoopTime}

#### \<instance> getLoopTime() {#instance-getlooptime}


**说明:**

计算循环源开始播放的时间的内部方法 。


> 源码：[src/sound/webaudio/WebAudioSound.js#L768](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L768)  
引入版本：3.0.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

暂停声闻.


**Overrides:** Phaser.Sound.BaseSound# 暂停


**返回值:** boolean - 声音是否被成功暂停 。


**Fires:** [Phaser.Sound.Events#event:PAUSE](/api/event/sound-events#pause)


> 源码：[src/sound/webaudio/WebAudioSound.js#L283](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L283)  
引入版本：3.0.0


---

### play {#play}

#### \<instance> play([markerName], [config]) {#instance-playmarkername-config}


**说明:**

播放此声音, 或标记其中的一节 。

它总是从一开始播放声音。 如果您想要从特定时间开始播放, 您可以设置配置对象的“ seek” 设置, 提供给此调用, 到该值 。

如果你想同时播放相同的声音,那么你需要创建另一个实例,并播放该声音.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| markerName | string \| [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | "''" | 如果您想要播放标记, 请在此提供标记名称。 或者, 此参数可以是 SoundConfig 对象 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 |  | 如果未提供标记名称, 可选的音效配置对象将应用到此标记或整个音效上。 它会被记住, 用于当前音节的未来播放 。 |


**Overrides:** Phaser.Sound.BaseSound游戏


**返回值:** boolean - 声音是否开始成功播放 。


**Fires:** [Phaser.Sound.Events#event:PLAY](/api/event/sound-events#play)


> 源码：[src/sound/webaudio/WebAudioSound.js#L249](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L249)  
引入版本：3.0.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

复说声闻.


**Overrides:** Phaser.Sound.BaseSound继续


**返回值:** boolean - 声音是否成功恢复 。


**Fires:** [Phaser.Sound.Events#event:RESUME](/api/event/sound-events#resume)


> 源码：[src/sound/webaudio/WebAudioSound.js#L313](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L313)  
引入版本：3.0.0


---

### setDetune {#setDetune}

#### \<instance> setDetune(value) {#instance-setdetunevalue}


**说明:**

设置此声音的调值, 以 [cents](https://en.wikipedia.org/wiki/Cent_%28music%29) 给出。 值的范围为 - 1200 到 1200, 但我们建议将其设置为 [50](https://en.wikipedia.org/wiki/50_Cent) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 值范围为 -1200 到 1200,但我们建议设定为 [50](https://en.wikipedia.org/wiki/50_Cent). |


**返回值:** [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) - 这个声音的例子。


**Fires:** [Phaser.Sound.Events#event:DETUNE](/api/event/sound-events#detune)


> 源码：[src/sound/webaudio/WebAudioSound.js#L867](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L867)  
引入版本：3.3.0


---

### setLoop {#setLoop}

#### \<instance> setLoop(value) {#instance-setloopvalue}


**说明:**

设置此声音的循环状态。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | `true`来循环这个声音,`false`来循环它。 |


**返回值:** [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) - 这个声音的例子。


**Fires:** [Phaser.Sound.Events#event:LOOP](/api/event/sound-events#loop)


> 源码：[src/sound/webaudio/WebAudioSound.js#L1083](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L1083)  
引入版本：3.4.0


---

### setMute {#setMute}

#### \<instance> setMute(value) {#instance-setmutevalue}


**说明:**

设置此声音的哑音状态 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | `true` to mute this sound, `false` to unmute it. |


**返回值:** [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) - 这个声音的例子。


**Fires:** [Phaser.Sound.Events#event:MUTE](/api/event/sound-events#mute)


> 源码：[src/sound/webaudio/WebAudioSound.js#L912](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L912)  
引入版本：3.4.0


---

### setPan {#setPan}

#### \<instance> setPan(value) {#instance-setpanvalue}


**说明:**

设置此声音的泛, 值介于 - 1( 完全左锅) 和 1( 完全右锅) 之间 。

注:iOS / Safari不支持立体式泛纳节点.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 声音的 pan。 值介于 - 1( 完全左锅) 和 1( 完全右锅) 之间 。 |


**返回值:** [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) - 这个声音的例子。


**Fires:** [Phaser.Sound.Events#event:PAN](/api/event/sound-events#pan)


> 源码：[src/sound/webaudio/WebAudioSound.js#L1139](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L1139)  
引入版本：3.50.0


---

### setRate {#setRate}

#### \<instance> setRate(value) {#instance-setratevalue}


**说明:**

设定此声音的播放率。

例如,1.0的值全速播放音频,0.5的半速播放音频,2.0的播放速度是音频的双倍.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 此声音的播放率 。 |


**返回值:** [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) - 这个声音的例子。


**Fires:** [Phaser.Sound.Events#event:RATE](/api/event/sound-events#rate)


> 源码：[src/sound/webaudio/WebAudioSound.js#L818](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L818)  
引入版本：3.3.0


---

### setSeek {#setSeek}

#### \<instance> setSeek(value) {#instance-setseekvalue}


**说明:**

寻求此声音中的特定点.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 声音中要追求的点, 秒。 |


**返回值:** [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) - 这个声音的例子。


**Fires:** [Phaser.Sound.Events#event:SEEK](/api/event/sound-events#seek)


> 源码：[src/sound/webaudio/WebAudioSound.js#L1031](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L1031)  
引入版本：3.4.0


---

### setVolume {#setVolume}

#### \<instance> setVolume(value) {#instance-setvolumevalue}


**说明:**

设置此声音的音量。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 音量,在0(静音)至1(全音量)之间. |


**返回值:** [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) - 这个声音的例子。


**Fires:** [Phaser.Sound.Events#event:VOLUME](/api/event/sound-events#volume)


> 源码：[src/sound/webaudio/WebAudioSound.js#L955](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L955)  
引入版本：3.4.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

别再弹了


**Overrides:** Phaser.Sound.BaseSound停下来


**返回值:** boolean - 声音是否成功停止 。


**Fires:** [Phaser.Sound.Events#event:STOP](/api/event/sound-events#stop)


> 源码：[src/sound/webaudio/WebAudioSound.js#L342](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L342)  
引入版本：3.0.0


---

### stopAndRemoveBufferSource {#stopAndRemoveBufferSource}

#### \<instance> stopAndRemoveBufferSource() {#instance-stopandremovebuffersource}


**说明:**

这种方法仅内部使用,并停止并移除缓冲源.


> 源码：[src/sound/webaudio/WebAudioSound.js#L450](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L450)  
引入版本：3.0.0


---

### stopAndRemoveLoopBufferSource {#stopAndRemoveLoopBufferSource}

#### \<instance> stopAndRemoveLoopBufferSource() {#instance-stopandremoveloopbuffersource}


**说明:**

这种方法仅内部使用,它停止并移除一个循环缓冲源.


> 源码：[src/sound/webaudio/WebAudioSound.js#L475](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L475)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update() {#instance-update}


**说明:**

更新方法在每个游戏步骤上由声音管理器自动调用.


**Overrides:** Phaser.Sound.BaseSound#更新日期


**Fires:** [Phaser.Sound.Events#event:COMPLETE](/api/event/sound-events#complete), [Phaser.Sound.Events#event:LOOPED](/api/event/sound-events#looped)


> 源码：[src/sound/webaudio/WebAudioSound.js#L615](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/webaudio/WebAudioSound.js#L615)  
引入版本：3.0.0


---

---
