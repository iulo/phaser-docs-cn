# NoAudioSound {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/sound-noaudiosound)

声音没有音频执行,如果音频在游戏配置中已被禁用,或者设备不支持任何音频,则使用.

它代表了声音逻辑的优雅退化,提供了最小的功能,并阻止使用音频的Phaser项目在不支持任何音频回放技术的设备上发生中断.

**构造函数**

`new NoAudioSound(manager, key, [config])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| manager | [Phaser.Sound.NoAudioSoundManager](/api/class/sound-noaudiosoundmanager) | 否 |  | 引用当前声音管理器实例 。 |
| key | string | 否 |  | 声音的键 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | "{}" | 包含默认声音设置的可选配置对象。 |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/sound/noaudio/NoAudioSound.js#L29](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L29)  
引入版本：3.0.0

## 公开成员 {#public-members}

### config {#config}

#### config: [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) {#config-phasertypessoundsoundconfig}


**说明:**

用于存储默认声音设置值的配置对象。 默认值将由属性设置器设置 。


> 源码：[src/sound/noaudio/NoAudioSound.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L135)  
引入版本：3.0.0


---

### currentConfig {#currentConfig}

#### currentConfig: [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) {#currentconfig-phasertypessoundsoundconfig}


**说明:**

引用当前使用的配置。 它可以是默认的配置或标记配置 。


> 源码：[src/sound/noaudio/NoAudioSound.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L154)  
引入版本：3.0.0


---

### currentMarker {#currentMarker}

#### currentMarker: [Phaser.Types.Sound.SoundMarker](/api/typedef/types-sound#soundmarker) {#currentmarker-phasertypessoundsoundmarker}


**说明:**

正在播放标记。 如果整个声音正在播放, “ 无效 ” 。


> 源码：[src/sound/noaudio/NoAudioSound.js#L260](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L260)  
引入版本：3.0.0


---

### detune {#detune}

#### detune: number {#detune-number}


**说明:**

此声音的补间, 以 [cents](https://en.wikipedia.org/wiki/Cent_%28music%29) 给出。 值的范围为 - 1200 到 1200, 但我们建议设定为 [50](https://en.wikipedia.org/wiki/50_Cent) 。


**触发事件:** [Phaser.Sound.Events#event:DETUNE](/api/event/sound-events#detune)


> 源码：[src/sound/noaudio/NoAudioSound.js#L200](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L200)  
引入版本：3.0.0


---

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

表示持续时间的值, 以秒计。 它可以是全部声音持续时间或标记持续时间 。


> 源码：[src/sound/noaudio/NoAudioSound.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L114)  
引入版本：3.0.0


---

### isPaused {#isPaused}

#### isPaused: boolean {#ispaused-boolean}


**说明:**

标记显示声音是否暂停 。


> 源码：[src/sound/noaudio/NoAudioSound.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L90)  
引入版本：3.0.0


---

### isPlaying {#isPlaying}

#### isPlaying: boolean {#isplaying-boolean}


**说明:**

显示声音是否正在播放的旗帜 。


> 源码：[src/sound/noaudio/NoAudioSound.js#L79](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L79)  
引入版本：3.0.0


---

### key {#key}

#### key: string {#key-string}


**说明:**

声音的键 。


> 源码：[src/sound/noaudio/NoAudioSound.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L69)  
引入版本：3.0.0


---

### loop {#loop}

#### loop: boolean {#loop-boolean}


**说明:**

显示声音或当前声音标记是否循环的旗帜 。


**触发事件:** [Phaser.Sound.Events#event:LOOP](/api/event/sound-events#loop)


> 源码：[src/sound/noaudio/NoAudioSound.js#L225](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L225)  
引入版本：3.0.0


---

### manager {#manager}

#### manager: [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) {#manager-phasersoundbasesoundmanager}


**说明:**

本地参考音效管理器.


> 源码：[src/sound/noaudio/NoAudioSound.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L60)  
引入版本：3.0.0


---

### markers {#markers}

#### markers: Object.\<string, [Phaser.Types.Sound.SoundMarker](/api/typedef/types-sound#soundmarker)> {#markers-objectstring-phasertypessoundsoundmarker}


**说明:**

包含标记定义的对象 。


> 源码：[src/sound/noaudio/NoAudioSound.js#L249](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L249)  
引入版本：3.0.0


---

### mute {#mute}

#### mute: boolean {#mute-boolean}


**说明:**

布尔表示声音是否变音。 获取或设置此声音的变音状态 。


**触发事件:** [Phaser.Sound.Events#event:MUTE](/api/event/sound-events#mute)


> 源码：[src/sound/noaudio/NoAudioSound.js#L164](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L164)  
引入版本：3.0.0


---

### pan {#pan}

#### pan: number {#pan-number}


**说明:**

获取或设置此声音的 pan, 值介于 - 1 (完全左锅) 和 1 (完全右锅) 之间 。

总是在iOS / Safari 上返回0,因为它不支持立体式泛纳节点.


**触发事件:** [Phaser.Sound.Events#event:PAN](/api/event/sound-events#pan)


> 源码：[src/sound/noaudio/NoAudioSound.js#L236](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L236)  
引入版本：3.50.0


---

### pendingRemove {#pendingRemove}

#### pendingRemove: boolean {#pendingremove-boolean}


**说明:**

旗子显示是否在此声音上调用毁灭方法 。


> 源码：[src/sound/noaudio/NoAudioSound.js#L272](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L272)  
引入版本：3.0.0


---

### rate {#rate}

#### rate: number {#rate-number}


**说明:**

播放此声音的速度。 值为 1.0 以全速播放音频, 值为 0. 5 以半速播放音频, 值为 2.0 将音频的播放速度增加一倍 。


**触发事件:** [Phaser.Sound.Events#event:RATE](/api/event/sound-events#rate)


> 源码：[src/sound/noaudio/NoAudioSound.js#L187](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L187)  
引入版本：3.0.0


---

### seek {#seek}

#### seek: number {#seek-number}


**说明:**

代表此声音的播放位置的属性, 以秒计。 设置到特定值后, 将当前播放的播放移动到该位置。 给出的值被夹在 0 到当前标记持续时间之间。 设置一个已停止的声音的搜索没有效果 。


**触发事件:** [Phaser.Sound.Events#event:SEEK](/api/event/sound-events#seek)


> 源码：[src/sound/noaudio/NoAudioSound.js#L212](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L212)  
引入版本：3.0.0


---

### totalDuration {#totalDuration}

#### totalDuration: number {#totalduration-number}


**说明:**

声音的总持续时间以秒计.


> 源码：[src/sound/noaudio/NoAudioSound.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L125)  
引入版本：3.0.0


---

### totalRate {#totalRate}

#### totalRate: number {#totalrate-number}


**说明:**

一个持有声音实际回放率值的属性,在它的回放率和补间与全局率和补间结合之后.


> 源码：[src/sound/noaudio/NoAudioSound.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L101)  
引入版本：3.0.0


---

### volume {#volume}

#### volume: number {#volume-number}


**说明:**

获取或设置此声音的音量,值介于 0(静态)到 1(全音量)之间.


**触发事件:** [Phaser.Sound.Events#event:VOLUME](/api/event/sound-events#volume)


> 源码：[src/sound/noaudio/NoAudioSound.js#L176](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L176)  
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




---

## 公开方法 {#public-methods}

### addMarker {#addMarker}

#### \<instance> addMarker(marker) {#instance-addmarkermarker}


**说明:**

向此声音添加标记。 标记允许您在声音剪辑中定义区域, 并独立播放 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| marker | [Phaser.Types.Sound.SoundMarker](/api/typedef/types-sound#soundmarker) | 否 | 标记对象 。 |


**返回值:** boolean - 虚假


> 源码：[src/sound/noaudio/NoAudioSound.js#L283](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L283)  
引入版本：3.0.0


---

### applyConfig {#applyConfig}

#### \<instance> applyConfig() {#instance-applyconfig}


**说明:**

将配置值应用到一些声音属性时内部使用的方法.


> 源码：[src/sound/noaudio/NoAudioSound.js#L452](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L452)  
引入版本：3.0.0


---

### calculateRate {#calculateRate}

#### \<instance> calculateRate() {#instance-calculaterate}


**说明:**

内部用于计算声音总回放率的方法.


> 源码：[src/sound/noaudio/NoAudioSound.js#L480](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L480)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁此声音和所有相关事件,并标记它,以便从声音管理器中移除.


**重写:** Phaser.Events.EventEmitter#销毁


**触发事件:** [Phaser.Sound.Events#event:DESTROY](/api/event/sound-events#destroy)


> 源码：[src/sound/noaudio/NoAudioSound.js#L488](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L488)  
引入版本：3.0.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

暂停这个声音。


**返回值:** boolean - 虚假


> 源码：[src/sound/noaudio/NoAudioSound.js#L332](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L332)  
引入版本：3.0.0


---

### play {#play}

#### \<instance> play([markerName], [config]) {#instance-playmarkername-config}


**说明:**

播放此声音, 或其中的特定标记。 可选的配置对象可以覆盖此调用默认的回放设置 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| markerName | string \| [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | "''" | 如果您想要播放标记, 请在此提供标记名称。 或者, 此参数可以是 SoundConfig 对象 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 |  | 如果未提供标记名称, 可选的音效配置对象将应用到此标记或整个音效上。 它会被记住, 用于当前音节的未来播放 。 |


**返回值:** boolean - 虚假


> 源码：[src/sound/noaudio/NoAudioSound.js#L319](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L319)  
引入版本：3.0.0


---

### removeMarker {#removeMarker}

#### \<instance> removeMarker(markerName) {#instance-removemarkermarkername}


**说明:**

从此声音中移除一个标记。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| markerName | string | 否 | 要删除的标记名称 。 |


**返回值:** null - 无效


> 源码：[src/sound/noaudio/NoAudioSound.js#L307](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L307)  
引入版本：3.0.0


---

### resetConfig {#resetConfig}

#### \<instance> resetConfig() {#instance-resetconfig}


**说明:**

内部用于重置一些配置属性的值的方法 。


> 源码：[src/sound/noaudio/NoAudioSound.js#L460](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L460)  
引入版本：3.0.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

复说声闻.


**返回值:** boolean - 虚假


> 源码：[src/sound/noaudio/NoAudioSound.js#L342](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L342)  
引入版本：3.0.0


---

### setDetune {#setDetune}

#### \<instance> setDetune(value) {#instance-setdetunevalue}


**说明:**

设置此声音的补间, 以 [cents](https://en.wikipedia.org/wiki/Cent_%28music%29) 给出。 值的范围为 - 1200 到 1200, 但我们建议将其设置为 [50](https://en.wikipedia.org/wiki/50_Cent) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 值范围为 -1200 到 1200,但我们建议设定为 [50](https://en.wikipedia.org/wiki/50_Cent). |


**返回值:** [Phaser.Sound.NoAudioSound](/api/class/sound-noaudiosound) - 这个声音的例子。


> 源码：[src/sound/noaudio/NoAudioSound.js#L401](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L401)  
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


**返回值:** [Phaser.Sound.NoAudioSound](/api/class/sound-noaudiosound) - 这个声音的例子。


> 源码：[src/sound/noaudio/NoAudioSound.js#L426](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L426)  
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


**返回值:** [Phaser.Sound.NoAudioSound](/api/class/sound-noaudiosound) - 这个声音的例子。


> 源码：[src/sound/noaudio/NoAudioSound.js#L362](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L362)  
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


**返回值:** [Phaser.Sound.NoAudioSound](/api/class/sound-noaudiosound) - 这个声音的例子。


> 源码：[src/sound/noaudio/NoAudioSound.js#L438](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L438)  
引入版本：3.50.0


---

### setRate {#setRate}

#### \<instance> setRate(value) {#instance-setratevalue}


**说明:**

设定此声音的播放率。

例如,1.0的值是全速播放音频,0.5的值是半速播放音频,2.0的值是音频回放速度的两倍.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 此声音的播放率 。 |


**返回值:** [Phaser.Sound.NoAudioSound](/api/class/sound-noaudiosound) - 这个声音的例子。


> 源码：[src/sound/noaudio/NoAudioSound.js#L386](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L386)  
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


**返回值:** [Phaser.Sound.NoAudioSound](/api/class/sound-noaudiosound) - 这个声音的例子。


> 源码：[src/sound/noaudio/NoAudioSound.js#L414](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L414)  
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


**返回值:** [Phaser.Sound.NoAudioSound](/api/class/sound-noaudiosound) - 这个声音的例子。


> 源码：[src/sound/noaudio/NoAudioSound.js#L374](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L374)  
引入版本：3.4.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

别再弹了


**返回值:** boolean - 虚假


> 源码：[src/sound/noaudio/NoAudioSound.js#L352](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L352)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update(time, delta) {#instance-updatetime-delta}


**说明:**

更新方法在每个游戏步骤上由声音管理器自动调用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 请求动画框架或SetTimeout生成的当前时间戳 。 |
| delta | number | 否 | 三角洲时间已经过去 自上个框架。 |


> 源码：[src/sound/noaudio/NoAudioSound.js#L468](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L468)  
引入版本：3.0.0


---

### updateMarker {#updateMarker}

#### \<instance> updateMarker(marker) {#instance-updatemarkermarker}


**说明:**

更新此声音中已有标记的值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| marker | [Phaser.Types.Sound.SoundMarker](/api/typedef/types-sound#soundmarker) | 否 | 带有更新值的标记对象 。 |


**返回值:** boolean - 虚假


> 源码：[src/sound/noaudio/NoAudioSound.js#L295](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSound.js#L295)  
引入版本：3.0.0


---

---
