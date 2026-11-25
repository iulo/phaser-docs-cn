# BaseSoundManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/sound-basesoundmanager)

用于Web Audio和HTML5 Audio Sound Management执行的基类,它管理一组声音实例,处理全局音量,哑音,分率,调谐设置,提供空间音频听器定位(仅Web Audy),并在游戏失去或重拾焦点时与游戏生命周期协调,以挖掘和恢复音频.

**构造函数**

`new BaseSoundManager(game)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 参考当前游戏实例 。 |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/sound/BaseSoundManager.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L18)  
引入版本：3.0.0

## 公开成员 {#public-members}

### detune {#detune}

#### detune: number {#detune-number}


**说明:**

以 [cents](https://en.wikipedia.org/wiki/Cent_%28music%29) 中所有声音的全球调谐。 值的范围为 - 1200 到 1200, 但我们建议将其保持在合理的范围内, 用于音乐目的 。


> 源码：[src/sound/BaseSoundManager.js#L809](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L809)  
引入版本：3.0.0


---

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

本地参考游戏.


> 源码：[src/sound/BaseSoundManager.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L48)  
引入版本：3.0.0


---

### gameLostFocus {#gameLostFocus}

#### gameLostFocus: boolean {#gamelostfocus-boolean}


**说明:**

旗子用来跟踪游戏是否失去焦点.


> 源码：[src/sound/BaseSoundManager.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L156)  
引入版本：3.60.0


---

### jsonCache {#jsonCache}

#### jsonCache: [Phaser.Cache.BaseCache](/api/class/cache-basecache) {#jsoncache-phasercachebasecache}


**说明:**

本地参考 JSON 缓存, 音频Sprites 使用 。


> 源码：[src/sound/BaseSoundManager.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L58)  
引入版本：3.7.0


---

### listenerPosition {#listenerPosition}

#### listenerPosition: [Phaser.Math.Vector2](/api/class/math-vector2) {#listenerposition-phasermathvector2}


**说明:**

空间音频听器位置 。

仅可与WebAudio一同使用.

您可以直接修改此 Vec2 的 x/y 属性,以调整游戏世界内的听者位置.


> 源码：[src/sound/BaseSoundManager.js#L166](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L166)  
引入版本：3.60.0


---

### locked {#locked}

#### locked: boolean {#locked-boolean}


**说明:**

移动设备需要从一个明确的用户动作,例如水龙头, 触发声音, 才能在网页上装入/播放任何声音。 如果音频系统目前锁定等待用户交互, 则设定为真实 。


> 源码：[src/sound/BaseSoundManager.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L132)  
引入版本：3.0.0


---

### mute {#mute}

#### mute: boolean {#mute-boolean}


**说明:**

全球哑声设置.


> 源码：[src/sound/BaseSoundManager.js#L79](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L79)  
引入版本：3.0.0


---

### pauseOnBlur {#pauseOnBlur}

#### pauseOnBlur: boolean {#pauseonblur-boolean}


**说明:**

标记显示当游戏失去焦点时是否应该暂停声音, 例如当用户切换到另一个标签/ 程序/ app 时 。


> 源码：[src/sound/BaseSoundManager.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L99)  
引入版本：3.0.0


---

### rate {#rate}

#### rate: number {#rate-number}


**说明:**

将播放所有声音的全球回放速率。 值为 1.0 以全速播放音频, 值为 0. 5 以半速播放音频, 数为 2.0 倍音频的回放速率 。


> 源码：[src/sound/BaseSoundManager.js#L759](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L759)  
引入版本：3.0.0


---

### volume {#volume}

#### volume: number {#volume-number}


**说明:**

全球量设定.


> 源码：[src/sound/BaseSoundManager.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L89)  
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

### add {#add}

#### \<instance> add(key, [config]) {#instance-addkey-config}


**说明:**

将新声音添加到声音管理器中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 声音的密钥 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | 包含默认声音设置的可选配置对象。 |


**返回值:** [Phaser.Sound.BaseSound](/api/class/sound-basesound) - 新声闻例.


> 源码：[src/sound/BaseSoundManager.js#L188](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L188)  
引入版本：3.0.0


---

### addAudioSprite {#addAudioSprite}

#### \<instance> addAudioSprite(key, [config]) {#instance-addaudiospritekey-config}


**说明:**

将一个新的音频图示声音添加到声音管理器中。 Audio Sprites 是音频文件与 JSON 配置的组合。 JSON 遵循 [https://github.com/tonistiigi/audiosprite](https://github.com/tonistiigi/audiosprite) 创建的格式

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 声音的密钥 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | 包含默认声音设置的可选配置对象。 |


**返回值:** [Phaser.Sound.NoAudioSound](/api/class/sound-noaudiosound), [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound), [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) - 新的音频图示音效实例 。


> 源码：[src/sound/BaseSoundManager.js#L202](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L202)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

破坏游戏中的所有声音和所有相关活动.


**Overrides:** Phaser.Events.EventEmitter#销毁


> 源码：[src/sound/BaseSoundManager.js#L693](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L693)  
引入版本：3.0.0


---

### get {#get}

#### \<instance> get(key) {#instance-getkey}


**说明:**

获取此声音管理器中符合给定密钥的第一个声音。 如果找不到, 则返回 `null` 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 音响资产密钥. |


**返回值:** [Phaser.Sound.BaseSound](/api/class/sound-basesound) - - 声音,或者无效。


> 源码：[src/sound/BaseSoundManager.js#L247](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L247)  
引入版本：3.23.0


---

### getAll {#getAll}

#### \<instance> getAll([key]) {#instance-getallkey}


**说明:**

声音管理器中会得到所有的声音 。

您可以选择指定一个密钥,在这种情况下,只返回符合给定密钥的音响实例。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 是 | 可选资产密钥。 如果给定, 将返回只有带有此密钥的音响实例 。 |


**返回值:** Array.\<[Phaser.Sound.BaseSound](/api/class/sound-basesound)> - - 声音,或者一个空阵列。


> 源码：[src/sound/BaseSoundManager.js#L266](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L266)  
引入版本：3.23.0


---

### getAllPlaying {#getAllPlaying}

#### \<instance> getAllPlaying() {#instance-getallplaying}


**说明:**

返回当前正在播放的音效管理器的所有声音。 即, 声音实例将它们的 `isPlaying` 属性设定为 `true` 。

**Tags:**

 - generic
 - genericUse


**返回值:** Array.\<[Phaser.Sound.BaseSound](/api/class/sound-basesound)> - - 所有正在播放的声音,或空阵列。


> 源码：[src/sound/BaseSoundManager.js#L294](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L294)  
引入版本：3.60.0


---

### isPlaying {#isPlaying}

#### \<instance> isPlaying(key) {#instance-isplayingkey}


**说明:**

当给定密钥时, 如果有声音使用该密钥, 返回真值 。

当未给出密钥时, 如果有声音在播放, 返回真 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 音响资产密钥. |


**返回值:** boolean - - 任何匹配的声音都是真的 否则是虚假的


> 源码：[src/sound/BaseSoundManager.js#L542](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L542)  
引入版本：3.85.0


---

### onBlur {#onBlur}

#### \<instance> onBlur() {#instance-onblur}


**说明:**

如果 Phaser.Sound.BaseSoundManager# pauseOnBlur 设定为真实, 则内部用于挖掘声音管理器的方法 。


**Access:** 保护


> 源码：[src/sound/BaseSoundManager.js#L601](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L601)  
引入版本：3.0.0


---

### onFocus {#onFocus}

#### \<instance> onFocus() {#instance-onfocus}


**说明:**

如果 Phaser.Sound.BaseSoundManager# pauseOnBlur 设定为真实,则内部用于恢复声音管理器的方法 。


**Access:** 保护


> 源码：[src/sound/BaseSoundManager.js#L612](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L612)  
引入版本：3.0.0


---

### pauseAll {#pauseAll}

#### \<instance> pauseAll() {#instance-pauseall}


**说明:**

暂停游戏中的所有声音.


**Fires:** [Phaser.Sound.Events#event:PAUSE_ALL](/api/event/sound-events#pause_all)


> 源码：[src/sound/BaseSoundManager.js#L452](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L452)  
引入版本：3.0.0


---

### play {#play}

#### \<instance> play(key, [extra]) {#instance-playkey-extra}


**说明:**

向声音管理器添加新声音并播放。

复播结束后,声音会自动被移除(销毁).

这使得你无需提及就可以在苍蝇上演奏新声音.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 声音的密钥 。 |
| extra | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) \| [Phaser.Types.Sound.SoundMarker](/api/typedef/types-sound#soundmarker) | 是 | 包含要应用到声音的设置的可选附加对象。 它可以是配置对象,也可以是标记对象 。 |


**返回值:** boolean - 声音是否开始成功播放 。


> 源码：[src/sound/BaseSoundManager.js#L312](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L312)  
引入版本：3.0.0


---

### playAudioSprite {#playAudioSprite}

#### \<instance> playAudioSprite(key, spriteName, [config]) {#instance-playaudiospritekey-spritename-config}


**说明:**

向声音管理器添加一个新的音频图示声音并播放。一旦重播结束,将自动删除(已销毁)该图示。这样您就可以在苍蝇上播放新声音,而无需保留引用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 声音的密钥 。 |
| spriteName | string | 否 | 播放的音响图案的名称 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | 包含默认声音设置的可选配置对象。 |


**返回值:** boolean - 音频图示声音是否开始成功播放 。


> 源码：[src/sound/BaseSoundManager.js#L353](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L353)  
引入版本：3.0.0


---

### remove {#remove}

#### \<instance> remove(sound) {#instance-removesound}


**说明:**

从声音管理器中删除声音。删除的声音在删除前会被销毁。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.BaseSound](/api/class/sound-basesound) | 否 | 要删除的音效对象 。 |


**返回值:** boolean - 如果声音被成功删除, 否则会是虚假的 。


> 源码：[src/sound/BaseSoundManager.js#L377](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L377)  
引入版本：3.0.0


---

### removeAll {#removeAll}

#### \<instance> removeAll() {#instance-removeall}


**说明:**

从管理器中删除所有声音, 销毁声音 。


> 源码：[src/sound/BaseSoundManager.js#L404](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L404)  
引入版本：3.23.0


---

### removeByKey {#removeByKey}

#### \<instance> removeByKey(key) {#instance-removebykeykey}


**说明:**

从声音管理器中删除所有符合给定值的资产密钥的音效。删除的音效在删除前会被销毁。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 删除声音对象时匹配的密钥 。 |


**返回值:** number - 匹配已删除的音效对象的数量 。


> 源码：[src/sound/BaseSoundManager.js#L420](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L420)  
引入版本：3.0.0


---

### resumeAll {#resumeAll}

#### \<instance> resumeAll() {#instance-resumeall}


**说明:**

复说游戏中一切声闻.


**Fires:** [Phaser.Sound.Events#event:RESUME_ALL](/api/event/sound-events#resume_all)


> 源码：[src/sound/BaseSoundManager.js#L469](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L469)  
引入版本：3.0.0


---

### setDetune {#setDetune}

#### \<instance> setDetune(value) {#instance-setdetunevalue}


**说明:**

设置 [cents](https://en.wikipedia.org/wiki/Cent_%28music%29) 中所有声音的全球调值。 值的范围为 - 1200 到 1200, 但我们建议将其保持在合理的范围内, 用于音乐目的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 以美分计的调值,范围是 -1200 到 1200,但我们建议保持合理范围,用于音乐目的。 |


**返回值:** [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) - 此音声管理者.


**Fires:** [Phaser.Sound.Events#event:GLOBAL_DETUNE](/api/event/sound-events#global_detune)


> 源码：[src/sound/BaseSoundManager.js#L790](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L790)  
引入版本：3.3.0


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


> 源码：[src/sound/BaseSoundManager.js#L486](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L486)  
引入版本：3.60.0


---

### setRate {#setRate}

#### \<instance> setRate(value) {#instance-setratevalue}


**说明:**

设定所有声音播放时的全局播放率 。

例如,1.0的值是全速播放音频,0.5的值是半速播放音频,2.0的值是音频回放速度的两倍.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 播放所有声音的全球回放率 。 |


**返回值:** [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) - 此音声管理者.


**Fires:** [Phaser.Sound.Events#event:GLOBAL_RATE](/api/event/sound-events#global_rate)


> 源码：[src/sound/BaseSoundManager.js#L738](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L738)  
引入版本：3.3.0


---

### stopAll {#stopAll}

#### \<instance> stopAll() {#instance-stopall}


**说明:**

停止游戏中的所有声音.


**Fires:** [Phaser.Sound.Events#event:STOP_ALL](/api/event/sound-events#stop_all)


> 源码：[src/sound/BaseSoundManager.js#L503](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L503)  
引入版本：3.0.0


---

### stopByKey {#stopByKey}

#### \<instance> stopByKey(key) {#instance-stopbykeykey}


**说明:**

停止任何符合给定密钥的声音。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 音响资产密钥. |


**返回值:** number - - 有多少声音被停止。


> 源码：[src/sound/BaseSoundManager.js#L520](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L520)  
引入版本：3.23.0


---

### unlock {#unlock}

#### \<instance> unlock() {#instance-unlock}


**说明:**

在任何声音在网页播放之前,在需要用户交互的设备上解锁音频播放的内部方法.

更多关于这个问题如何在这里处理,[this article](https://medium.com/@pgoloskokovic/unlocking-web-audio-the-smarter-way-8858218c0e09)。


**Access:** 保护


> 源码：[src/sound/BaseSoundManager.js#L588](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L588)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update(time, delta) {#instance-updatetime-delta}


**说明:**

更新方法召唤到每个游戏步骤。 删除已销毁的声音, 更新游戏中每个活动的声音 。


**Access:** 保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 请求动画框架或SetTimeout生成的当前时间戳 。 |
| delta | number | 否 | 三角洲时间已经过去 自上个框架。 |


**Fires:** [Phaser.Sound.Events#event:UNLOCKED](/api/event/sound-events#unlocked)


> 源码：[src/sound/BaseSoundManager.js#L657](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSoundManager.js#L657)  
引入版本：3.0.0


---

---
