# NoAudioSoundManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/sound-noaudiosoundmanager)

声音管理器的无自动执行。 如果游戏配置中已禁用音频, 或设备不支持任何音频, 则使用此操作 。

它代表了声音管理器逻辑的优雅退化,提供了最小的功能,防止使用音频的Phaser项目在不支持任何音频回放技术的设备上发生中断.

**构造函数**

`new NoAudioSoundManager(game)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 参考当前游戏实例 。 |

---


**作用域**: static


**继承**

> [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager)  



> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L14)  
引入版本：3.0.0

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


 - [getAllPlaying](/api/class/sound-basesoundmanager#getAllPlaying)
 - [isPlaying](/api/class/sound-basesoundmanager#isPlaying)
 - [setListenerPosition](/api/class/sound-basesoundmanager#setListenerPosition)




---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(key, [config]) {#instance-addkey-config}


**说明:**

将新声音添加到声音管理器中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 声音的键 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | 包含默认声音设置的可选配置对象。 |


**重写:** Phaser.Sound.BaseSoundManager添加( 添加 )


**返回值:** [Phaser.Sound.NoAudioSound](/api/class/sound-noaudiosound) - 新声闻例.


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L51](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L51)  
引入版本：3.60.0


---

### addAudioSprite {#addAudioSprite}

#### \<instance> addAudioSprite(key, [config]) {#instance-addaudiospritekey-config}


**说明:**

将一个新的音频图示声音添加到声音管理器中。 Audio Sprites 是音频文件与 JSON 配置的组合。 JSON 遵循 [https://github.com/tonistiigi/audiosprite](https://github.com/tonistiigi/audiosprite) 创建的格式

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 声音的键 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | 包含默认声音设置的可选配置对象。 |


**重写:** Phaser.Sound.BaseSoundManager#addAudioSprite


**返回值:** [Phaser.Sound.NoAudioSound](/api/class/sound-noaudiosound) - 新的音频图示音效实例 。


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L71)  
引入版本：3.60.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

破坏游戏中的所有声音和所有相关活动.


**重写:** Phaser.Sound.BaseSoundManager#销毁


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L396](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L396)  
引入版本：3.0.0


---

### get {#get}

#### \<instance> get(key) {#instance-getkey}


**说明:**

获得管理器中符合给定键的第一个声音, 如果有的话 。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 音响资源键. |


**重写:** Phaser.Sound.BaseSoundManager得到的,我发现


**返回值:** [Phaser.Sound.BaseSound](/api/class/sound-basesound) - - 声音,或者无效。


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L93)  
引入版本：3.23.0


---

### getAll {#getAll}

#### \<instance> getAll(key) {#instance-getallkey}


**说明:**

管理器中获取匹配给定键的任何声音 。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 音响资源键. |


**重写:** Phaser.Sound.BaseSoundManager#getAll


**返回值:** Array.\<[Phaser.Sound.BaseSound](/api/class/sound-basesound)> - - 声音,或者一个空阵列。


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L111)  
引入版本：3.23.0


---

### onBlur {#onBlur}

#### \<instance> onBlur() {#instance-onblur}


**说明:**

这个方法对于无音效管理器没有任何作用,可以保持与其他音效管理器的兼容性.

在真正的 Sound 管理器中,当浏览器窗口失去焦点时会叫它,如果启用 `pauseOnBlur`,则会暂停所有播放声音.


**重写:** Phaser.Sound.BaseSoundManager#onBlur


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L224](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L224)  
引入版本：3.0.0


---

### onFocus {#onFocus}

#### \<instance> onFocus() {#instance-onfocus}


**说明:**

这个方法对于无音效管理器没有任何作用,可以保持与其他音效管理器的兼容性.

在真正的Sound管理器中,当浏览器窗口重新重现焦点时,会叫它,并恢复任何在焦点丢失时暂停的音效.


**重写:** Phaser.Sound.BaseSoundManager#onFocus


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L236](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L236)  
引入版本：3.0.0


---

### onGameBlur {#onGameBlur}

#### \<instance> onGameBlur() {#instance-ongameblur}


**说明:**

这个方法对于无音效管理器没有任何作用,可以保持与其他音效管理器的兼容性.

在真正的Sound管理器中,当Phaser Game 实例失去焦点(例如画布失去指针),并相应暂停声音时,会叫这个.


**重写:** Phaser.Sound.BaseSoundManager#onGameBlur


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L248](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L248)  
引入版本：3.0.0


---

### onGameFocus {#onGameFocus}

#### \<instance> onGameFocus() {#instance-ongamefocus}


**说明:**

这个方法对于无音效管理器没有任何作用,可以保持与其他音效管理器的兼容性.

在真正的Sound Management中,当Phaser Game 实例重拾焦点并恢复任何被暂停在模糊上的声音时,会叫这个.


**重写:** Phaser.Sound.BaseSoundManager#onGameFocus


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L260](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L260)  
引入版本：3.0.0


---

### pauseAll {#pauseAll}

#### \<instance> pauseAll() {#instance-pauseall}


**说明:**

这个方法对于无音效管理器没有任何作用,可以保持与其他音效管理器的兼容性.

在真正的音效管理器中, 这将暂停所有当前播放的音效 。


**重写:** Phaser.Sound.BaseSoundManager#pauseAll


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L272](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L272)  
引入版本：3.0.0


---

### play {#play}

#### \<instance> play(key, [extra]) {#instance-playkey-extra}


**说明:**

这个方法除了返回"假"之外,对无音频声音管理器毫无作用,以保持与其他声音管理器的兼容性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 声音的键 。 |
| extra | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) \| [Phaser.Types.Sound.SoundMarker](/api/typedef/types-sound#soundmarker) | 是 | 包含要应用到声音的设置的可选附加对象。 它可以是配置对象,也可以是标记对象 。 |


**重写:** Phaser.Sound.BaseSoundManager游戏


**返回值:** boolean - 总是为无声管理器"假".


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L129](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L129)  
引入版本：3.0.0


---

### playAudioSprite {#playAudioSprite}

#### \<instance> playAudioSprite(key, spriteName, [config]) {#instance-playaudiospritekey-spritename-config}


**说明:**

这个方法除了返回"假"之外,对无音频声音管理器毫无作用,以保持与其他声音管理器的兼容性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 声音的键 。 |
| spriteName | string | 否 | 播放的音响图案的名称 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | 包含默认声音设置的可选配置对象。 |


**重写:** Phaser.Sound.BaseSoundManager#playAudioSprite


**返回值:** boolean - 总是为无声管理器"假".


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L147](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L147)  
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


**重写:** Phaser.Sound.BaseSoundManager# 移动


**返回值:** boolean - 如果声音被成功删除, 否则会是虚假的 。


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L166](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L166)  
引入版本：3.0.0


---

### removeAll {#removeAll}

#### \<instance> removeAll() {#instance-removeall}


**说明:**

从管理器中删除所有声音, 销毁声音 。


**重写:** Phaser.Sound.BaseSoundManager#removeAll


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L182](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L182)  
引入版本：3.23.0


---

### removeByKey {#removeByKey}

#### \<instance> removeByKey(key) {#instance-removebykeykey}


**说明:**

从声音管理器中删除所有符合给定值的资源键的音效。删除的音效在删除前会被销毁。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 删除声音对象时匹配的键 。 |


**重写:** Phaser.Sound.BaseSoundManager#removeByKey


**返回值:** number - 匹配已删除的音效对象的数量 。


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L193](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L193)  
引入版本：3.0.0


---

### resumeAll {#resumeAll}

#### \<instance> resumeAll() {#instance-resumeall}


**说明:**

这个方法对于无音效管理器没有任何作用,可以保持与其他音效管理器的兼容性.

在真正的声音管理器中,这可以恢复所有暂停的声音.


**重写:** Phaser.Sound.BaseSoundManager#resumeAll


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L283](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L283)  
引入版本：3.0.0


---

### setDetune {#setDetune}

#### \<instance> setDetune() {#instance-setdetune}


**说明:**

这个方法对于无音效管理器没有任何作用,可以保持与其他音效管理器的兼容性.

在真正的Sound Manager中,这可以设置所有声音的全球补间,用美分计,其中百分等于一个半音.


**重写:** Phaser.Sound.BaseSoundManager#setDetune


**返回值:** [Phaser.Sound.NoAudioSoundManager](/api/class/sound-noaudiosoundmanager) - 此音声管理者.


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L331](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L331)  
引入版本：3.0.0


---

### setMute {#setMute}

#### \<instance> setMute() {#instance-setmute}


**说明:**

这个方法对于无音效管理器没有任何作用,可以保持与其他音效管理器的兼容性.

在真正的Sound Manager中,这将会使管理器中的所有声音都变哑或解密.


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L345](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L345)  
引入版本：3.0.0


---

### setRate {#setRate}

#### \<instance> setRate() {#instance-setrate}


**说明:**

这个方法对于无音效管理器没有任何作用,可以保持与其他音效管理器的兼容性.

在真正的Sound Manager中,这将设定所有声音的全球回放速率,其中1是正常速度,0.5是半速,2是双速.


**重写:** Phaser.Sound.BaseSoundManager#setRate


**返回值:** [Phaser.Sound.NoAudioSoundManager](/api/class/sound-noaudiosoundmanager) - 此音声管理者.


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L317](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L317)  
引入版本：3.0.0


---

### setVolume {#setVolume}

#### \<instance> setVolume() {#instance-setvolume}


**说明:**

这个方法对于无音效管理器没有任何作用,可以保持与其他音效管理器的兼容性.

在真正的Sound Manager中,这将设定管理器中所有声音的全球音量,其中0是静音,1是全音量.


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L356](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L356)  
引入版本：3.0.0


---

### stopAll {#stopAll}

#### \<instance> stopAll() {#instance-stopall}


**说明:**

这个方法对于无音效管理器没有任何作用,可以保持与其他音效管理器的兼容性.

在真正的Sound Manager中,这可以停止所有当前播放的音效.


**重写:** Phaser.Sound.BaseSoundManager#stopAll


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L294](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L294)  
引入版本：3.0.0


---

### stopByKey {#stopByKey}

#### \<instance> stopByKey(key) {#instance-stopbykeykey}


**说明:**

停止任何符合给定键的声音。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 音响资源键. |


**重写:** Phaser.Sound.BaseSoundManager#stopByKey


**返回值:** number - - 有多少声音被停止。


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L209](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L209)  
引入版本：3.23.0


---

### unlock {#unlock}

#### \<instance> unlock() {#instance-unlock}


**说明:**

这个方法对于无音效管理器没有任何作用,可以保持与其他音效管理器的兼容性.

在真正的Sound管理器中,这将会尝试在用户手势后解锁音频上下文,现代浏览器在音频回放开始前需要解锁.


**重写:** Phaser.Sound.BaseSoundManager#解锁


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L368](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L368)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update() {#instance-update}


**说明:**

这个方法对于无音效管理器没有任何作用,可以保持与其他音效管理器的兼容性.

在真正的Sound Manager中,这将会被呼吁到每个游戏步骤上更新所有活动声音的状态.


**重写:** Phaser.Sound.BaseSoundManager#更新日期


> 源码：[src/sound/noaudio/NoAudioSoundManager.js#L305](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/noaudio/NoAudioSoundManager.js#L305)  
引入版本：3.0.0


---

## 继承的成员 {#inherited-members}


**From [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager):**


 - [detune](/api/class/sound-basesoundmanager#detune)
 - [game](/api/class/sound-basesoundmanager#game)
 - [gameLostFocus](/api/class/sound-basesoundmanager#gameLostFocus)
 - [jsonCache](/api/class/sound-basesoundmanager#jsonCache)
 - [listenerPosition](/api/class/sound-basesoundmanager#listenerPosition)
 - [locked](/api/class/sound-basesoundmanager#locked)
 - [mute](/api/class/sound-basesoundmanager#mute)
 - [pauseOnBlur](/api/class/sound-basesoundmanager#pauseOnBlur)
 - [rate](/api/class/sound-basesoundmanager#rate)
 - [volume](/api/class/sound-basesoundmanager#volume)




---

---
