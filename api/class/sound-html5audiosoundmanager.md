# HTML5AudioSoundManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/sound-html5audiosoundmanager)

HTML5 音频管理器

**构造函数**

`new HTML5AudioSoundManager(game)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 参考当前游戏实例 。 |

---


**作用域**: static


**继承**

> [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager)  



> 源码：[src/sound/html5/HTML5AudioSoundManager.js#L37](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSoundManager.js#L37)  
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

### audioPlayDelay {#audioPlayDelay}

#### audioPlayDelay: number {#audioplaydelay-number}


**说明:**

表示时差的值, 以秒计, 在音频标签上调用播放方法与它实际开始播放时之间, 用于实现更准确的延迟播放声音 。

您可能需要调整这个值以获得预期结果, 因为音频播放延迟因浏览器/ 平台而异 。


> 源码：[src/sound/html5/HTML5AudioSoundManager.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSoundManager.js#L58)  
引入版本：3.0.0


---

### loopEndOffset {#loopEndOffset}

#### loopEndOffset: number {#loopendoffset-number}


**说明:**

一种值,我们应当通过该值来抵消循环音的循环端标记以弥补由于改变音频标记回放位置而导致的滞后,以实现无间隙循环.

您可能需要调整这个值以获得预期结果, 因为循环时滞取决于浏览器/ 平台 。


> 源码：[src/sound/html5/HTML5AudioSoundManager.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSoundManager.js#L73)  
引入版本：3.0.0


---

### mute {#mute}

#### mute: boolean {#mute-boolean}


**说明:**

获取或设置此声音管理器的变音状态。 设定为 `true` 变音, 而设定为 `false` 则恢复音量。 更改时将 `GLOBAL_MUTE` 事件点燃 。


**重写:** Phaser.Sound.BaseSoundManager穆特( 穆特)


**触发事件:** [Phaser.Sound.Events#event:GLOBAL_MUTE](/api/event/sound-events#global_mute)


> 源码：[src/sound/html5/HTML5AudioSoundManager.js#L389](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSoundManager.js#L389)  
引入版本：3.0.0


---

### override {#override}

#### override: boolean {#override-boolean}


**说明:**

标记, 显示HTML5音频标记是否没有闲置实例, 对于任何特定声音, 如果其中一个使用的标记应该被劫持并用于后续播放, 或者如果后续的 Phaser.Sound.HTML5AudioSound# play call 是否应该忽略 。


> 源码：[src/sound/html5/HTML5AudioSoundManager.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSoundManager.js#L45)  
引入版本：3.0.0


---

### volume {#volume}

#### volume: number {#volume-number}


**说明:**

获取或设置此声音管理器的全局音量。 所有活动声音的音量将按此值进行缩放。 必须在 0( 静音) 到 1( 完整音量) 之间。 更改时将启动 `GLOBAL_VOLUME`事件 。


**重写:** Phaser.Sound.BaseSoundManager数量


**触发事件:** [Phaser.Sound.Events#event:GLOBAL_VOLUME](/api/event/sound-events#global_volume)


> 源码：[src/sound/html5/HTML5AudioSoundManager.js#L438](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSoundManager.js#L438)  
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
 - [setListenerPosition](/api/class/sound-basesoundmanager#setListenerPosition)
 - [setRate](/api/class/sound-basesoundmanager#setRate)
 - [stopAll](/api/class/sound-basesoundmanager#stopAll)
 - [stopByKey](/api/class/sound-basesoundmanager#stopByKey)
 - [update](/api/class/sound-basesoundmanager#update)




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


**返回值:** [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) - 新声闻例.


> 源码：[src/sound/html5/HTML5AudioSoundManager.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSoundManager.js#L142)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

呼叫 Phaser.Sound.BaseSoundManager#destroy 方法并清理所有 HTML5 音频相关资源.


**重写:** Phaser.Sound.BaseSoundManager#销毁


> 源码：[src/sound/html5/HTML5AudioSoundManager.js#L325](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSoundManager.js#L325)  
引入版本：3.0.0


---

### isLocked {#isLocked}

#### \<instance> isLocked(sound, prop, [value]) {#instance-islockedsound-prop-value}


**说明:**

Phaser.Sound.HTML5AudioSound类方法与属性设置器内部使用的方法,用于检查声音管理器是否被锁定,然后要么立即执行动作,要么在声音管理器解锁后排队执行.


**访问权限:** 受保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 执行队列动作的音效对象 。 |
| prop | string | 否 | 拟调用的方法名称或拟给定值的属性名称. |
| value | * | 是 | 一个可选参数,它要么持有一系列要传递到方法调用,要么设定到属性的值. |


**返回值:** boolean - 声音管理器是否锁定 。


> 源码：[src/sound/html5/HTML5AudioSoundManager.js#L340](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSoundManager.js#L340)  
引入版本：3.0.0


---

### onBlur {#onBlur}

#### \<instance> onBlur() {#instance-onblur}


**说明:**

如果 Phaser.Sound.HTML5AudioSoundManager# pauseOnBlur 设定为真实, 则内部用于挖掘声音管理器的方法 。


**访问权限:** 受保护


**重写:** Phaser.Sound.BaseSoundManager#onBlur


> 源码：[src/sound/html5/HTML5AudioSoundManager.js#L287](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSoundManager.js#L287)  
引入版本：3.0.0


---

### onFocus {#onFocus}

#### \<instance> onFocus() {#instance-onfocus}


**说明:**

如果 Phaser.Sound.HTML5AudioSoundManager# pauseOnBlur 设定为真实,则内部用于恢复声音管理器的方法 。


**访问权限:** 受保护


**重写:** Phaser.Sound.BaseSoundManager#onFocus


> 源码：[src/sound/html5/HTML5AudioSoundManager.js#L307](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSoundManager.js#L307)  
引入版本：3.0.0


---

### setMute {#setMute}

#### \<instance> setMute(value) {#instance-setmutevalue}


**说明:**

设置此声音管理器的变音状态 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | `true` 关闭所有的声音,`false` 解除它们。 |


**返回值:** [Phaser.Sound.HTML5AudioSoundManager](/api/class/sound-html5audiosoundmanager) - 此音声管理者.


**触发事件:** [Phaser.Sound.Events#event:GLOBAL_MUTE](/api/event/sound-events#global_mute)


> 源码：[src/sound/html5/HTML5AudioSoundManager.js#L371](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSoundManager.js#L371)  
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


**返回值:** [Phaser.Sound.HTML5AudioSoundManager](/api/class/sound-html5audiosoundmanager) - 此音声管理者.


**触发事件:** [Phaser.Sound.Events#event:GLOBAL_VOLUME](/api/event/sound-events#global_volume)


> 源码：[src/sound/html5/HTML5AudioSoundManager.js#L420](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSoundManager.js#L420)  
引入版本：3.3.0


---

### unlock {#unlock}

#### \<instance> unlock() {#instance-unlock}


**说明:**

在初始的显式用户交互上解锁HTML5音频加载和重播移动设备.


**重写:** Phaser.Sound.BaseSoundManager#解锁


> 源码：[src/sound/html5/HTML5AudioSoundManager.js#L162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/html5/HTML5AudioSoundManager.js#L162)  
引入版本：3.0.0


---

---
