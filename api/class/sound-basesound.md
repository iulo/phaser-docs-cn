# BaseSound {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/sound-basesound)

包含声音对象所有共享状态和行为的基类,独立于音频执行(Web Audio或HTML5 Audio). 管理播放状态(播放,暂停,停止,寻求),循环,音量,速率,调谐,播放音频子部分的标记,以及播放周期变化的事件释放.

**构造函数**

`new BaseSound(manager, key, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) | 否 | 引用当前声音管理器实例 。 |
| key | string | 否 | 声音的键 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | 包含默认声音设置的可选配置对象。 |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/sound/BaseSound.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L14)  
引入版本：3.0.0

## 公开成员 {#public-members}

### currentMarker {#currentMarker}

#### currentMarker: [Phaser.Types.Sound.SoundMarker](/api/typedef/types-sound#soundmarker) {#currentmarker-phasertypessoundsoundmarker}


**说明:**

正在播放标记。 如果整个声音正在播放, “ 无效 ” 。


> 源码：[src/sound/BaseSound.js#L162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L162)  
引入版本：3.0.0


---

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

表示持续时间的值, 以秒计。 它可以是全部声音持续时间或标记持续时间 。


> 源码：[src/sound/BaseSound.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L95)  
引入版本：3.0.0


---

### isPaused {#isPaused}

#### isPaused: boolean {#ispaused-boolean}


**说明:**

标记显示声音是否暂停 。


> 源码：[src/sound/BaseSound.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L71)  
引入版本：3.0.0


---

### isPlaying {#isPlaying}

#### isPlaying: boolean {#isplaying-boolean}


**说明:**

显示声音是否正在播放的旗帜 。


> 源码：[src/sound/BaseSound.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L60)  
引入版本：3.0.0


---

### key {#key}

#### key: string {#key-string}


**说明:**

声音的键 。


> 源码：[src/sound/BaseSound.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L50)  
引入版本：3.0.0


---

### manager {#manager}

#### manager: [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) {#manager-phasersoundbasesoundmanager}


**说明:**

本地参考音效管理器.


> 源码：[src/sound/BaseSound.js#L41](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L41)  
引入版本：3.0.0


---

### markers {#markers}

#### markers: Object.\<string, [Phaser.Types.Sound.SoundMarker](/api/typedef/types-sound#soundmarker)> {#markers-objectstring-phasertypessoundsoundmarker}


**说明:**

包含标记定义的对象 。


> 源码：[src/sound/BaseSound.js#L151](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L151)  
引入版本：3.0.0


---

### pendingRemove {#pendingRemove}

#### pendingRemove: boolean {#pendingremove-boolean}


**说明:**

旗子显示是否在此声音上调用毁灭方法 。


> 源码：[src/sound/BaseSound.js#L174](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L174)  
引入版本：3.0.0


---

### totalDuration {#totalDuration}

#### totalDuration: number {#totalduration-number}


**说明:**

声音的总持续时间以秒计.


> 源码：[src/sound/BaseSound.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L106)  
引入版本：3.0.0


---

### totalRate {#totalRate}

#### totalRate: number {#totalrate-number}


**说明:**

一个持有声音实际回放率值的属性,在它的回放率和补间与全局率和补间结合之后.


> 源码：[src/sound/BaseSound.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L82)  
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

在当前声音中添加标记。标记由名称、起始时间、持续时间和可选配置对象来表示。这样可以将多个声音组合到一个音频文件中,并使用标记在它们之间跳跃,以进行回放。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| marker | [Phaser.Types.Sound.SoundMarker](/api/typedef/types-sound#soundmarker) | 否 | 标记对象 。 |


**返回值:** boolean - 标记是否成功添加 。


> 源码：[src/sound/BaseSound.js#L185](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L185)  
引入版本：3.0.0


---

### applyConfig {#applyConfig}

#### \<instance> applyConfig() {#instance-applyconfig}


**说明:**

将配置值应用到一些声音属性时内部使用的方法.


> 源码：[src/sound/BaseSound.js#L415](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L415)  
引入版本：3.0.0


---

### calculateRate {#calculateRate}

#### \<instance> calculateRate() {#instance-calculaterate}


**说明:**

内部用于计算声音总回放率的方法.


> 源码：[src/sound/BaseSound.js#L454](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L454)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁此声音和所有相关事件,并标记它,以便从声音管理器中移除.


**重写:** Phaser.Events.EventEmitter#销毁


**触发事件:** [Phaser.Sound.Events#event:DESTROY](/api/event/sound-events#destroy)


> 源码：[src/sound/BaseSound.js#L469](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L469)  
引入版本：3.0.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

暂停声音。 只有在声音正在播放时才有效 。

你可以检查`isPlaying`和`isPaused`属性,以检查状态.


**返回值:** boolean - 声音是否被成功暂停 。


> 源码：[src/sound/BaseSound.js#L346](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L346)  
引入版本：3.0.0


---

### play {#play}

#### \<instance> play([markerName], [config]) {#instance-playmarkername-config}


**说明:**

播放此声音, 或标记其中的一节 。

它总是从一开始播放声音。 如果您想要从特定时间开始播放, 您可以设置配置对象的“ seek” 设置, 提供给此调用, 到该值 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| markerName | string \| [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 | "''" | 如果您想要播放标记, 请在此提供标记名称。 或者, 此参数可以是 SoundConfig 对象 。 |
| config | [Phaser.Types.Sound.SoundConfig](/api/typedef/types-sound#soundconfig) | 是 |  | 如果未提供标记名称, 可选的音效配置对象将应用到此标记或整个音效上。 它会被记住, 用于当前音节的未来播放 。 |


**返回值:** boolean - 声音是否开始成功播放 。


> 源码：[src/sound/BaseSound.js#L286](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L286)  
引入版本：3.0.0


---

### removeMarker {#removeMarker}

#### \<instance> removeMarker(markerName) {#instance-removemarkermarkername}


**说明:**

从声音中删除标记。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| markerName | string | 否 | 要删除的标记名称 。 |


**返回值:** [Phaser.Types.Sound.SoundMarker](/api/typedef/types-sound#soundmarker) - 如果没有提供名称的标记, 则删除了标记对象或“ 无效 ” 。


> 源码：[src/sound/BaseSound.js#L262](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L262)  
引入版本：3.0.0


---

### resetConfig {#resetConfig}

#### \<instance> resetConfig() {#instance-resetconfig}


**说明:**

内部用于重置一些配置属性的值的方法 。


> 源码：[src/sound/BaseSound.js#L431](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L431)  
引入版本：3.0.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

恢复声音。 只有声音暂停而没有播放时, 声音才会起作用 。

你可以检查`isPlaying`和`isPaused`属性,以检查状态.


**返回值:** boolean - 声音是否成功恢复 。


> 源码：[src/sound/BaseSound.js#L369](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L369)  
引入版本：3.0.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

别再弹了


**返回值:** boolean - 声音是否成功停止 。


> 源码：[src/sound/BaseSound.js#L392](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L392)  
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


> 源码：[src/sound/BaseSound.js#L443](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L443)  
引入版本：3.0.0


---

### updateMarker {#updateMarker}

#### \<instance> updateMarker(marker) {#instance-updatemarkermarker}


**说明:**

更新先前从提供的标记对象中添加的新值的标记。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| marker | [Phaser.Types.Sound.SoundMarker](/api/typedef/types-sound#soundmarker) | 否 | 带有更新值的标记对象 。 |


**返回值:** boolean - 标记是否成功更新 。


> 源码：[src/sound/BaseSound.js#L232](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/BaseSound.js#L232)  
引入版本：3.0.0


---

---
