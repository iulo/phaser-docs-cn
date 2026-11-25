# Phaser.Sound.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/sound-events)

Scope: 
static
> 源码：[src/sound/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/index.js#L7)  


## 静态函数 {#static-functions}

### COMPLETE {#COMPLETE}

#### COMPLETE {#complete}


**说明:**

声音完成事件。

此事件由Web Audio和HTML5 Audio Sound两个对象在完成回放时同时发送.

使用`Sound.on('complete', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('complete', listener);
music.play();
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |


> 源码：[src/sound/events/COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/COMPLETE_EVENT.js#L7)  
引入版本：3.16.1


---

### DECODED {#DECODED}

#### DECODED {#decoded}


**说明:**

音频数据解码事件.

本次活动由网络音频音效管理器因调用`decodeAudio`方法而发出.

使用 `this.sound.on('decoded', listener)` 在场景中听声音管理器的,即:

```javascript
this.sound.on('decoded', handler);
this.sound.decodeAudio(key, audioData);
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 解码后添加到音频缓存中的音频文件的密钥. |


> 源码：[src/sound/events/DECODED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/DECODED_EVENT.js#L7)  
引入版本：3.18.0


---

### DECODED_ALL {#DECODED_ALL}

#### DECODED_ALL {#decoded_all}


**说明:**

音频数据解码了全部事件 。

此事件由Web音频声音管理器发送,因为一旦所有传递到该方法的文件都解码(或错误),就会呼叫`decodeAudio`方法.

使用`Phaser.Sound.Events#DECODED`来听解码中的单声调,`DECODED_ALL`来听全部完成.

使用 `this.sound.on('decodedall', listener)` 在场景中听声音管理器的,即:

```javascript
this.sound.once('decodedall', handler);
this.sound.decodeAudio([ audioFiles ]);
```


> 源码：[src/sound/events/DECODED_ALL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/DECODED_ALL_EVENT.js#L7)  
引入版本：3.18.0


---

### DESTROY {#DESTROY}

#### DESTROY {#destroy}


**说明:**

音响破坏事件.

事件由Web Audio和HTML5 Audio Sound两个对象在被直接或通过一个Sound管理器销毁时发出.

使用`Sound.on('destroy', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('destroy', listener);
music.destroy();
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |


> 源码：[src/sound/events/DESTROY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/DESTROY_EVENT.js#L7)  
引入版本：3.0.0


---

### DETUNE {#DETUNE}

#### DETUNE {#detune}


**说明:**

声疾事件.

当Web Audio和HTML5 Audio Sound两个对象的值变化时,都会发出这个事件.

使用`Sound.on('detune', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('detune', listener);
music.play();
music.setDetune(200);
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |
| detune | number | 否 | 声音的新调值 。 |


> 源码：[src/sound/events/DETUNE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/DETUNE_EVENT.js#L7)  
引入版本：3.0.0


---

### GLOBAL_DETUNE {#GLOBAL_DETUNE}

#### GLOBAL_DETUNE {#global_detune}


**说明:**

声控全球变形事件.

此事件由 Base Sound 管理器发送, 或者更典型的, 网络音频管理器的实例, 或者 HTML5 音频管理器。 当声音管理器的 `detune` 属性被更改时, 它会被发送, 它将全球调整所有活动声音的调试 。

听听场景用`this.sound.on('detune', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) | 否 | 引用事件发声的音效管理器 。 |
| detune | number | 否 | 更新的调值 。 |


> 源码：[src/sound/events/GLOBAL_DETUNE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/GLOBAL_DETUNE_EVENT.js#L7)  
引入版本：3.0.0


---

### GLOBAL_MUTE {#GLOBAL_MUTE}

#### GLOBAL_MUTE {#global_mute}


**说明:**

声控全球哑声事件.

此事件由声音管理器在直接或通过 `setMute` 方法更改其 `mute` 属性时发出。 这将改变所有活动声音的哑音状态 。

听听场景用`this.sound.on('mute', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.WebAudioSoundManager](/api/class/sound-webaudiosoundmanager) \| [Phaser.Sound.HTML5AudioSoundManager](/api/class/sound-html5audiosoundmanager) | 否 | 引用事件发售的音效管理器 。 |
| mute | boolean | 否 | 哑值。 `true` 如果声音管理器现在已哑音, 否则 `false` 。 |


> 源码：[src/sound/events/GLOBAL_MUTE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/GLOBAL_MUTE_EVENT.js#L7)  
引入版本：3.0.0


---

### GLOBAL_RATE {#GLOBAL_RATE}

#### GLOBAL_RATE {#global_rate}


**说明:**

声音管理器全球比率事件 。

此事件由 Base Sound 管理器发送, 或者更典型的, 网络音频管理器的实例, 或者 HTML5 音频管理器。 当声音管理器的 `rate` 属性被更改时, 它会被发送, 它会在全球范围内调整所有活动声音的播放率 。

听听场景用`this.sound.on('rate', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) | 否 | 引用事件发声的音效管理器 。 |
| rate | number | 否 | 更新的利率值 。 |


> 源码：[src/sound/events/GLOBAL_RATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/GLOBAL_RATE_EVENT.js#L7)  
引入版本：3.0.0


---

### GLOBAL_VOLUME {#GLOBAL_VOLUME}

#### GLOBAL_VOLUME {#global_volume}


**说明:**

声控全球卷事件.

当其 `volume` 属性被直接或通过 `setVolume` 方法更改时, 由声音管理器发出。 这会改变所有活动声音的音量 。

听听场景用`this.sound.on('volume', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.WebAudioSoundManager](/api/class/sound-webaudiosoundmanager) \| [Phaser.Sound.HTML5AudioSoundManager](/api/class/sound-html5audiosoundmanager) | 否 | 引用事件发声的音效管理器 。 |
| volume | number | 否 | 音响管理器全球新卷. |


> 源码：[src/sound/events/GLOBAL_VOLUME_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/GLOBAL_VOLUME_EVENT.js#L7)  
引入版本：3.0.0


---

### LOOP {#LOOP}

#### LOOP {#loop}


**说明:**

声圈事件.

当Web Audio和HTML5 Audio Sound两个对象的循环状态改变时,都会发出这个事件.

使用`Sound.on('loop', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('loop', listener);
music.setLoop(true);
```

这不能和 [``LOOPED``](/api/event/sound-events#looped) 事件,每次在播放时都会发出声音循环。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |
| loop | boolean | 否 | 新的循环值。 `true` 如果声音会循环, 否则 `false`. |


> 源码：[src/sound/events/LOOP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/LOOP_EVENT.js#L7)  
引入版本：3.0.0


---

### LOOPED {#LOOPED}

#### LOOPED {#looped}


**说明:**

声律事件.

此事件由Web Audio和HTML5 Audio Sound两个对象在回放时循环时发送.

使用`Sound.on('looped', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('looped', listener);
music.setLoop(true);
music.play();
```

这与[``LOOP``](/api/event/sound-events#loop)事件不可混淆,事件只在一个声音的循环状态改变时才会发出.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |


> 源码：[src/sound/events/LOOPED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/LOOPED_EVENT.js#L7)  
引入版本：3.0.0


---

### MUTE {#MUTE}

#### MUTE {#mute}


**说明:**

声哑事件.

当Web Audio和HTML5 Audio Sound对象的哑状态发生变化时,此事件都会由它们同时发送.

使用`Sound.on('mute', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('mute', listener);
music.play();
music.setMute(true);
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |
| mute | boolean | 否 | 哑值。 `true` 如果声音现在被哑音, 否则`false`. |


> 源码：[src/sound/events/MUTE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/MUTE_EVENT.js#L7)  
引入版本：3.0.0


---

### PAN {#PAN}

#### PAN {#pan}


**说明:**

声泛事件.

当Web Audio和HTML5 Audio Sound两个对象的平板电脑改变时,都会发出这个事件.

使用`Sound.on('pan', listener)`从声音实例中听它,即:

```javascript
var sound = this.sound.add('key');
sound.on('pan', listener);
sound.play();
sound.setPan(0.5);
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |
| pan | number | 否 | 声闻新锅. |


> 源码：[src/sound/events/PAN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/PAN_EVENT.js#L7)  
引入版本：3.50.0


---

### PAUSE {#PAUSE}

#### PAUSE {#pause}


**说明:**

声音暂停事件。

此事件由Web Audio和HTML5 Audio Sound两个对象在暂停时同时发送.

使用`Sound.on('pause', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('pause', listener);
music.play();
music.pause();
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |


> 源码：[src/sound/events/PAUSE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/PAUSE_EVENT.js#L7)  
引入版本：3.0.0


---

### PAUSE_ALL {#PAUSE_ALL}

#### PAUSE_ALL {#pause_all}


**说明:**

暂停所有声音事件。

此事件由 Base 声音管理器( 或更典型的) 网络音频管理器或 HTML5 音频管理器的实例发送。 当使用 `pauseAll` 方法时, 当所有当前声音被暂停后, 即发送此事件 。

听听场景用`this.sound.on('pauseall', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) | 否 | 引用事件发声的音效管理器 。 |


> 源码：[src/sound/events/PAUSE_ALL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/PAUSE_ALL_EVENT.js#L7)  
引入版本：3.0.0


---

### PLAY {#PLAY}

#### PLAY {#play}


**说明:**

声乐事件.

此事件在播放时由Web Audio和HTML5 Audio Sound两个对象共同发送.

使用`Sound.on('play', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('play', listener);
music.play();
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |


> 源码：[src/sound/events/PLAY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/PLAY_EVENT.js#L7)  
引入版本：3.0.0


---

### RATE {#RATE}

#### RATE {#rate}


**说明:**

音速变化事件.

当Web Audio和HTML5 Audio Sound两个对象的频率发生变化时,都会发出这个事件.

使用`Sound.on('rate', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('rate', listener);
music.play();
music.setRate(0.5);
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |
| rate | number | 否 | 声闻新率. |


> 源码：[src/sound/events/RATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/RATE_EVENT.js#L7)  
引入版本：3.0.0


---

### RESUME {#RESUME}

#### RESUME {#resume}


**说明:**

声音复发事件.

此事件由Web Audio和HTML5 Audio Sound两个对象在从暂停状态恢复时发送.

使用`Sound.on('resume', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('resume', listener);
music.play();
music.pause();
music.resume();
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |


> 源码：[src/sound/events/RESUME_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/RESUME_EVENT.js#L7)  
引入版本：3.0.0


---

### RESUME_ALL {#RESUME_ALL}

#### RESUME_ALL {#resume_all}


**说明:**

恢复所有声音事件。

此事件由 Base Sound 管理器( 或更典型的) 发送, 即网络音频管理器的实例, 或是 HTML5 音频管理器。 当使用 `resumeAll` 方法时, 以及当所有当前声音被恢复后, 都会发送 。

听听场景用`this.sound.on('resumeall', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) | 否 | 引用事件发声的音效管理器 。 |


> 源码：[src/sound/events/RESUME_ALL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/RESUME_ALL_EVENT.js#L7)  
引入版本：3.0.0


---

### SEEK {#SEEK}

#### SEEK {#seek}


**说明:**

寻声事件.

此事件在被搜索到新位置时, 由Web Audio和HTML5 Audio Sound两个对象发送.

使用`Sound.on('seek', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('seek', listener);
music.play();
music.setSeek(5000);
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |
| seek | number | 否 | 声音的新求值 。 |


> 源码：[src/sound/events/SEEK_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/SEEK_EVENT.js#L7)  
引入版本：3.0.0


---

### STOP {#STOP}

#### STOP {#stop}


**说明:**

止音事件.

此事件在被停止时由Web Audio和HTML5 Audio Sound两个对象发送.

使用`Sound.on('stop', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('stop', listener);
music.play();
music.stop();
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |


> 源码：[src/sound/events/STOP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/STOP_EVENT.js#L7)  
引入版本：3.0.0


---

### STOP_ALL {#STOP_ALL}

#### STOP_ALL {#stop_all}


**说明:**

停止所有声音事件。

此事件由 Base Sound 管理器发送, 或者更典型的, 网络音频管理器的实例, 或者 HTML5 音频管理器。 当使用 `stopAll` 方法时, 并且当所有当前声音被停止后, 都会发送 。

听听场景用`this.sound.on('stopall', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) | 否 | 引用事件发声的音效管理器 。 |


> 源码：[src/sound/events/STOP_ALL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/STOP_ALL_EVENT.js#L7)  
引入版本：3.0.0


---

### UNLOCKED {#UNLOCKED}

#### UNLOCKED {#unlocked}


**说明:**

声音管理器解锁事件 。

此事件由 Base Sound 管理器发送, 或者更典型的, 网络音频管理器的实例, 或者 HTML5 音频管理器。 当声音管理器解锁后, 更新循环中发送。 对于 Web Audio, 这个问题在页面的第一个用户手势中 。

听听场景用`this.sound.on('unlocked', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) | 否 | 引用事件发声的音效管理器 。 |


> 源码：[src/sound/events/UNLOCKED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/UNLOCKED_EVENT.js#L7)  
引入版本：3.0.0


---

### VOLUME {#VOLUME}

#### VOLUME {#volume}


**说明:**

音量事件.

当Web Audio和HTML5 Audio Sound对象的音量变化时,都会由它们发出这个事件.

使用`Sound.on('volume', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('volume', listener);
music.play();
music.setVolume(0.5);
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |
| volume | number | 否 | 音声新卷. |


> 源码：[src/sound/events/VOLUME_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/VOLUME_EVENT.js#L7)  
引入版本：3.0.0


---

---
