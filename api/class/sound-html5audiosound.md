# HTML5AudioSound {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/sound-html5audiosound)

HTML5AudioSound是Phaser内部一个声音的HTML5音频API执行.

它在Web AudioSound API无法使用时被HTML5AudioSoundManager自动使用,一般在不支持它或它被禁用的环境下使用. HTML5AudioSound 与WebAudioSund类不同,HTML5AidioSound 依赖本地的`<audio>`元素进行回放,这意味着它的能力比较有限,比如没有支持音频的播音.

每个声音都保留着通过`Loader.audio`加载的`HTMLAudioElement`标记集合。由于HTML5音频不能在同时播放的回放中共享一个单一元素,所以如果想要同时多播放一次相同声音,就必须加载该资产的多个实例.

您不直接创建此类的例。 相反, 请使用 Scene 中的 `this.sound.add(key)`, 它将返回基于正在使用的音频系统的正确声音类型 。

**构造函数**

`new HTML5AudioSound(manager, key, [config])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| manager | [Phaser.Sound.HTML5AudioSoundManager](/api/class/sound-html5audiosoundmanager) | 否 |  | 引用当前声音管理器实例 。 |
| key | string | 否 |  | 声音的密钥 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | "{}" | 包含默认声音设置的可选配置对象。 |

---


**作用域**: static


**继承**

> [Phaser.Sound.BaseSound](/api/class/sound-basesound)  



> 源码：[src/sound/html5/HTML5AudioSound.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L13)  
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

### audio {#audio}

#### audio: HTMLAudioElement {#audio-htmlaudioelement}


**说明:**

引用用于播放声音的 HTML5 音频标记 。


> 源码：[src/sound/html5/HTML5AudioSound.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L66)  
引入版本：3.0.0


---

### detune {#detune}

#### detune: number {#detune-number}


**说明:**

此声音的调值, 以 [cents](https://en.wikipedia.org/wiki/Cent_%28music%29) 给出。 值的范围为 - 1200 到 1200, 但我们建议设定为 [50](https://en.wikipedia.org/wiki/50_Cent) 。


**Fires:** [Phaser.Sound.Events#event:DETUNE](/api/event/sound-events#detune)


> 源码：[src/sound/html5/HTML5AudioSound.js#L739](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L739)  
引入版本：3.0.0


---

### loop {#loop}

#### loop: boolean {#loop-boolean}


**说明:**

显示声音或当前声音标记是否循环的旗帜 。


**Fires:** [Phaser.Sound.Events#event:LOOP](/api/event/sound-events#loop)


> 源码：[src/sound/html5/HTML5AudioSound.js#L871](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L871)  
引入版本：3.0.0


---

### mute {#mute}

#### mute: boolean {#mute-boolean}


**说明:**

布尔表示声音是否变音。 获取或设置此声音的变音状态 。


**Fires:** [Phaser.Sound.Events#event:MUTE](/api/event/sound-events#mute)


> 源码：[src/sound/html5/HTML5AudioSound.js#L583](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L583)  
引入版本：3.0.0


---

### pan {#pan}

#### pan: number {#pan-number}


**说明:**

获取或设置此声音的 pan, 值介于 - 1 (完全左锅) 和 1 (完全右锅) 之间 。

对HTML5音频声音没有可调效果,但仍生成PAN Event.


**Fires:** [Phaser.Sound.Events#event:PAN](/api/event/sound-events#pan)


> 源码：[src/sound/html5/HTML5AudioSound.js#L924](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L924)  
引入版本：3.50.0


---

### previousTime {#previousTime}

#### previousTime: number {#previoustime-number}


**说明:**

音频标记的播放位置记录在上次更新方法调用中。 如果声音没有播放, 则设定为 0 。


> 源码：[src/sound/html5/HTML5AudioSound.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L88)  
引入版本：3.0.0


---

### rate {#rate}

#### rate: number {#rate-number}


**说明:**

播放此声音的速度 。 值为 1.0 的播放音频全速, 值为 0. 5 的播放音频半速, 值为 2.0 的播放速度的两倍 。


**Fires:** [Phaser.Sound.Events#event:RATE](/api/event/sound-events#rate)


> 源码：[src/sound/html5/HTML5AudioSound.js#L682](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L682)  
引入版本：3.0.0


---

### seek {#seek}

#### seek: number {#seek-number}


**说明:**

代表此声音的播放位置的属性, 以秒计。 设置到特定值后, 将当前播放的播放移动到该位置。 给出的值被夹在 0 到当前标记持续时间之间。 设置一个已停止的声音的搜索没有效果 。


**Fires:** [Phaser.Sound.Events#event:SEEK](/api/event/sound-events#seek)


> 源码：[src/sound/html5/HTML5AudioSound.js#L793](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L793)  
引入版本：3.0.0


---

### startTime {#startTime}

#### startTime: number {#starttime-number}


**说明:**

请求动画框架或SetTimeout 生成的时标, 代表延迟播放的音效开始时间。 如果声音播放没有延迟, 设置为 0 。


> 源码：[src/sound/html5/HTML5AudioSound.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L76)  
引入版本：3.0.0


---

### tags {#tags}

#### tags: Array.\<HTMLAudioElement> {#tags-arrayhtmlaudioelement}


**说明:**

包含所有 HTML5 音频标记的阵列, 可用于单个声音回放。 实例的数量取决于传递到 `Loader#audio` 方法调用时的配置值, 默认值为 1 。


> 源码：[src/sound/html5/HTML5AudioSound.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L50)  
引入版本：3.0.0


---

### volume {#volume}

#### volume: number {#volume-number}


**说明:**

获取或设置此声音的音量,值介于 0(静态)到 1(全音量)之间.


**Fires:** [Phaser.Sound.Events#event:VOLUME](/api/event/sound-events#volume)


> 源码：[src/sound/html5/HTML5AudioSound.js#L633](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L633)  
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





**From [Phaser.Sound.BaseSound](/api/class/sound-basesound):**


 - [addMarker](/api/class/sound-basesound#addMarker)
 - [applyConfig](/api/class/sound-basesound#applyConfig)
 - [removeMarker](/api/class/sound-basesound#removeMarker)
 - [resetConfig](/api/class/sound-basesound#resetConfig)
 - [updateMarker](/api/class/sound-basesound#updateMarker)




---

## 公开方法 {#public-methods}

### calculateRate {#calculateRate}

#### \<instance> calculateRate() {#instance-calculaterate}


**说明:**

这种方法在内部用于更新此声音的回放速率.


**Overrides:** Phaser.Sound.BaseSound#calculateRate


> 源码：[src/sound/html5/HTML5AudioSound.js#L567](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L567)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

呼叫 Phaser.Sound.BaseSound#destroy 方法并清理所有 HTML5 音频相关资源.


**Overrides:** Phaser.Sound.BaseSound#销毁


> 源码：[src/sound/html5/HTML5AudioSound.js#L520](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L520)  
引入版本：3.0.0


---

### onBlur {#onBlur}

#### \<instance> onBlur() {#instance-onblur}


**说明:**

如果 Phaser.Sound.HTML5AudioSoundManager# pauseOnBlur 设定为真实, 声音管理器内部用于拔声的方法 。


> 源码：[src/sound/html5/HTML5AudioSound.js#L419](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L419)  
引入版本：3.0.0


---

### onFocus {#onFocus}

#### \<instance> onFocus() {#instance-onfocus}


**说明:**

如果 Phaser.Sound.HTML5AudioSoundManager# pauseOnBlur 设定为真实, 声音管理器内部用于恢复声音的方法 。


> 源码：[src/sound/html5/HTML5AudioSound.js#L438](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L438)  
引入版本：3.0.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

暂停声闻.


**Overrides:** Phaser.Sound.BaseSound# 暂停


**返回值:** boolean - 声音是否被成功暂停 。


**Fires:** [Phaser.Sound.Events#event:PAUSE](/api/event/sound-events#pause)


> 源码：[src/sound/html5/HTML5AudioSound.js#L148](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L148)  
引入版本：3.0.0


---

### pickAndPlayAudioTag {#pickAndPlayAudioTag}

#### \<instance> pickAndPlayAudioTag() {#instance-pickandplayaudiotag}


**说明:**

这种方法在内部用于选择和播放下一个可用的音频标记.


**返回值:** boolean - 声音是否成功指定了音频标记 。


> 源码：[src/sound/html5/HTML5AudioSound.js#L250](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L250)  
引入版本：3.0.0


---

### pickAudioTag {#pickAudioTag}

#### \<instance> pickAudioTag() {#instance-pickaudiotag}


**说明:**

这种方法执行音频标签集合逻辑。 它首先查找未使用的音频标签来指定此音频对象。 如果没有未使用的音频标记, 则基于 HTML5AudioSoundManager# 覆盖属性值, 它会以最先进的播放功能查找声音, 并劫持其音频标记或无所作为 。


**返回值:** boolean - 声音是否成功指定了音频标记 。


> 源码：[src/sound/html5/HTML5AudioSound.js#L299](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L299)  
引入版本：3.0.0


---

### play {#play}

#### \<instance> play([markerName], [config]) {#instance-playmarkername-config}


**说明:**

播放此声音, 或标记其中的一节 。

它总是从一开始播放声音。 如果您想要从特定时间开始播放, 您可以设置配置对象的“ seek” 设置, 提供给此调用, 到该值 。

如果您想要同时播放相同的声音, 您需要创建另一个实例并播放该声音。 对于 HTML5 音频, 这还需要在加载音频文件时创建多个音频实例 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| markerName | string \| [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | "''" | 如果您想要播放标记, 请在此提供标记名称。 或者, 此参数可以是 SoundConfig 对象 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 |  | 如果未提供标记名称, 可选的音效配置对象将应用到此标记或整个音效上。 它会被记住, 用于当前音节的未来播放 。 |


**Overrides:** Phaser.Sound.BaseSound游戏


**返回值:** boolean - 声音是否开始成功播放 。


**Fires:** [Phaser.Sound.Events#event:PLAY](/api/event/sound-events#play)


> 源码：[src/sound/html5/HTML5AudioSound.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L106)  
引入版本：3.0.0


---

### playCatchPromise {#playCatchPromise}

#### \<instance> playCatchPromise() {#instance-playcatchpromise}


**说明:**

播放音频标签和捕捉被拒绝的许诺中可能抛出的例外的方法,从播放方法调用中返回。


> 源码：[src/sound/html5/HTML5AudioSound.js#L367](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L367)  
引入版本：3.0.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

内部使用的方法来重置声音状态,通常在停止声音或从另一个声音劫持音频标记时使用.


> 源码：[src/sound/html5/HTML5AudioSound.js#L407](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L407)  
引入版本：3.0.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

复说声闻.


**Overrides:** Phaser.Sound.BaseSound继续


**返回值:** boolean - 声音是否成功恢复 。


**Fires:** [Phaser.Sound.Events#event:RESUME](/api/event/sound-events#resume)


> 源码：[src/sound/html5/HTML5AudioSound.js#L184](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L184)  
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


**返回值:** [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) - 这个声音的例子。


**Fires:** [Phaser.Sound.Events#event:DETUNE](/api/event/sound-events#detune)


> 源码：[src/sound/html5/HTML5AudioSound.js#L774](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L774)  
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


**返回值:** [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) - 这个声音的例子。


**Fires:** [Phaser.Sound.Events#event:LOOP](/api/event/sound-events#loop)


> 源码：[src/sound/html5/HTML5AudioSound.js#L906](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L906)  
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


**返回值:** [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) - 这个声音的例子。


**Fires:** [Phaser.Sound.Events#event:MUTE](/api/event/sound-events#mute)


> 源码：[src/sound/html5/HTML5AudioSound.js#L615](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L615)  
引入版本：3.4.0


---

### setPan {#setPan}

#### \<instance> setPan(value) {#instance-setpanvalue}


**说明:**

设置此声音的泛, 值介于 - 1( 完全左锅) 和 1( 完全右锅) 之间 。

对HTML5音频声音没有可调效果,但仍生成PAN Event.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 声音的 pan。 值介于 - 1( 完全左锅) 和 1( 完全右锅) 之间 。 |


**返回值:** [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) - 这个声音的例子。


**Fires:** [Phaser.Sound.Events#event:PAN](/api/event/sound-events#pan)


> 源码：[src/sound/html5/HTML5AudioSound.js#L950](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L950)  
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


**返回值:** [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) - 这个声音的例子。


**Fires:** [Phaser.Sound.Events#event:RATE](/api/event/sound-events#rate)


> 源码：[src/sound/html5/HTML5AudioSound.js#L718](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L718)  
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


**返回值:** [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) - 这个声音的例子。


**Fires:** [Phaser.Sound.Events#event:SEEK](/api/event/sound-events#seek)


> 源码：[src/sound/html5/HTML5AudioSound.js#L853](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L853)  
引入版本：3.4.0


---

### setVolume {#setVolume}

#### \<instance> setVolume(value) {#instance-setvolumevalue}


**说明:**

设置此声音的音量。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 音量,值介于 0(静态)到 1(全音量)之间. |


**返回值:** [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) - 这个声音的例子。


**Fires:** [Phaser.Sound.Events#event:VOLUME](/api/event/sound-events#volume)


> 源码：[src/sound/html5/HTML5AudioSound.js#L664](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L664)  
引入版本：3.4.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

别再弹了


**Overrides:** Phaser.Sound.BaseSound停下来


**返回值:** boolean - 声音是否成功停止 。


**Fires:** [Phaser.Sound.Events#event:STOP](/api/event/sound-events#stop)


> 源码：[src/sound/html5/HTML5AudioSound.js#L221](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L221)  
引入版本：3.0.0


---

### stopAndReleaseAudioTag {#stopAndReleaseAudioTag}

#### \<instance> stopAndReleaseAudioTag() {#instance-stopandreleaseaudiotag}


**说明:**

这种方法在内部用于停止并释放当前音频标记.


> 源码：[src/sound/html5/HTML5AudioSound.js#L388](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L388)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update(time) {#instance-updatetime}


**说明:**

更新方法在每个游戏步骤上由声音管理器自动调用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 请求动画框架或SetTimeout生成的当前时间戳 。 |


**Overrides:** Phaser.Sound.BaseSound#更新日期


**Fires:** [Phaser.Sound.Events#event:COMPLETE](/api/event/sound-events#complete), [Phaser.Sound.Events#event:LOOPED](/api/event/sound-events#looped)


> 源码：[src/sound/html5/HTML5AudioSound.js#L452](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L452)  
引入版本：3.0.0


---

### updateMute {#updateMute}

#### \<instance> updateMute() {#instance-updatemute}


**说明:**

此方法在内部用于更新此声音的哑声设置.


> 源码：[src/sound/html5/HTML5AudioSound.js#L539](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L539)  
引入版本：3.0.0


---

### updateVolume {#updateVolume}

#### \<instance> updateVolume() {#instance-updatevolume}


**说明:**

这种方法在内部用于更新此声音的音量.


> 源码：[src/sound/html5/HTML5AudioSound.js#L553](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSound.js#L553)  
引入版本：3.0.0


---

---
