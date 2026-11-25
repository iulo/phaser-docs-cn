# Sound.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/sound-events)

## COMPLETE {#complete}


**说明:** 声音完成事件。

此事件由Web Audio和HTML5 Audio Sound两个对象在完成回放时同时发送.

使用`Sound.on('complete', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('complete', listener);
music.play();
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/COMPLETE_EVENT.js#L7)  
引入版本：3.16.1

## DECODED_ALL {#decoded_all}


**说明:** 音频数据解码了全部事件 。

本次活动由网络音频管理器发出,因为调用`decodeAudio`方法,
一旦所有文件传递到方法上,则解码(或错误).

使用 `Phaser.Sound.Events#DECODED` 来听解码中的单个声音, `DECODED_ALL` 则使用到
都听好了,他们都完成了。

使用 `this.sound.on('decodedall', listener)` 在场景中听声音管理器的,即:

```javascript
this.sound.once('decodedall', handler);
this.sound.decodeAudio([ audioFiles ]);
```

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/DECODED_ALL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/DECODED_ALL_EVENT.js#L7)  
引入版本：3.18.0

## DECODED {#decoded}


**说明:** 音频数据解码事件.

本次活动由网络音频音效管理器因调用`decodeAudio`方法而发出.

使用 `this.sound.on('decoded', listener)` 在场景中听声音管理器的,即:

```javascript
this.sound.on('decoded', handler);
this.sound.decodeAudio(key, audioData);
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 解码后添加到音频缓存中的音频文件的键. |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/DECODED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/DECODED_EVENT.js#L7)  
引入版本：3.18.0

## DESTROY {#destroy}


**说明:** 音响破坏事件.

此事件由被销毁的Web Audio和HTML5 Audio Sound两个对象同时发送, 也可以
直接或通过声音管理器。

使用`Sound.on('destroy', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('destroy', listener);
music.destroy();
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/DESTROY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/DESTROY_EVENT.js#L7)  
引入版本：3.0.0

## DETUNE {#detune}


**说明:** 声疾事件.

当Web Audio和HTML5 Audio Sound两个对象的值变化时,都会发出这个事件.

使用`Sound.on('detune', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('detune', listener);
music.play();
music.setDetune(200);
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |
| detune | number | 否 | 声音的新补间 。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/DETUNE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/DETUNE_EVENT.js#L7)  
引入版本：3.0.0

## GLOBAL_DETUNE {#global_detune}


**说明:** 声控全球变形事件.

本次活动由基地声音管理器(Base Sound Manager)发出,或更典型的Web音频声音管理器实例,
或 HTML5 音频管理器。当声音管理器的 `detune` 属性被更改时,它会发出, 在全球范围
调整所有活动声音的调试。

听听场景用`this.sound.on('detune', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) | 否 | 引用事件发声的音效管理器 。 |
| detune | number | 否 | 更新的补间 。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/GLOBAL_DETUNE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/GLOBAL_DETUNE_EVENT.js#L7)  
引入版本：3.0.0

## GLOBAL_MUTE {#global_mute}


**说明:** 声控全球哑声事件.

事件由声音管理器在更改其 `mute` 属性时直接发送
或通过 `setMute` 方法。这改变了所有活动声音的哑音状态。

听听场景用`this.sound.on('mute', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.WebAudioSoundManager](/api/class/sound-webaudiosoundmanager) \| [Phaser.Sound.HTML5AudioSoundManager](/api/class/sound-html5audiosoundmanager) | 否 | 引用事件发售的音效管理器 。 |
| mute | boolean | 否 | 哑值。 `true` 如果声音管理器现在已哑音, 否则 `false` 。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/GLOBAL_MUTE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/GLOBAL_MUTE_EVENT.js#L7)  
引入版本：3.0.0

## GLOBAL_RATE {#global_rate}


**说明:** 声音管理器全球比率事件 。

本次活动由基地声音管理器(Base Sound Manager)发出,或更典型的Web音频声音管理器实例,
或 HTML5 音频管理器。当声音管理器的 `rate` 属性被更改时,它会发出, 在全球范围
调整所有活动声音的回放率。

听听场景用`this.sound.on('rate', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) | 否 | 引用事件发声的音效管理器 。 |
| rate | number | 否 | 更新的利率值 。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/GLOBAL_RATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/GLOBAL_RATE_EVENT.js#L7)  
引入版本：3.0.0

## GLOBAL_VOLUME {#global_volume}


**说明:** 声控全球卷事件.

事件由声音管理器在更改其 `volume` 属性时直接发送
或通过 `setVolume` 方法。这改变了所有活动声音的音量。

听听场景用`this.sound.on('volume', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.WebAudioSoundManager](/api/class/sound-webaudiosoundmanager) \| [Phaser.Sound.HTML5AudioSoundManager](/api/class/sound-html5audiosoundmanager) | 否 | 引用事件发声的音效管理器 。 |
| volume | number | 否 | 音响管理器全球新卷. |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/GLOBAL_VOLUME_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/GLOBAL_VOLUME_EVENT.js#L7)  
引入版本：3.0.0

## LOOPED {#looped}


**说明:** 声律事件.

此事件由Web Audio和HTML5 Audio Sound两个对象在回放时循环时发送.

使用`Sound.on('looped', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('looped', listener);
music.setLoop(true);
music.play();
```

这与[LOOP]QQlinkcode Phaser.Sound.Events#event:LOOP]事件不相混淆,事件只在声音的循环状态改变时才会发出.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/LOOPED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/LOOPED_EVENT.js#L7)  
引入版本：3.0.0

## LOOP {#loop}


**说明:** 声圈事件.

当Web Audio和HTML5 Audio Sound两个对象的循环状态改变时,都会发出这个事件.

使用`Sound.on('loop', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('loop', listener);
music.setLoop(true);
```

这一点不应与[LOOPED]QQlinkcode Phaser.Sound.Events#event:LOOPED]事件混淆,在回放时,每一次都会发出一个声音循环.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |
| loop | boolean | 否 | 新的循环值。 `true` 如果声音会循环, 否则 `false`. |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/LOOP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/LOOP_EVENT.js#L7)  
引入版本：3.0.0

## MUTE {#mute}


**说明:** 声哑事件.

当Web Audio和HTML5 Audio Sound对象的哑状态发生变化时,此事件都会由它们同时发送.

使用`Sound.on('mute', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('mute', listener);
music.play();
music.setMute(true);
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |
| mute | boolean | 否 | 哑值。 `true` 如果声音现在被哑音, 否则`false`. |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/MUTE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/MUTE_EVENT.js#L7)  
引入版本：3.0.0

## PAN {#pan}


**说明:** 声泛事件.

当Web Audio和HTML5 Audio Sound两个对象的平板电脑改变时,都会发出这个事件.

使用`Sound.on('pan', listener)`从声音实例中听它,即:

```javascript
var sound = this.sound.add('key');
sound.on('pan', listener);
sound.play();
sound.setPan(0.5);
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |
| pan | number | 否 | 声闻新锅. |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/PAN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/PAN_EVENT.js#L7)  
引入版本：3.50.0

## PAUSE_ALL {#pause_all}


**说明:** 暂停所有声音事件。

本次活动由基地声音管理器(Base Sound Manager)发出,或更典型的Web音频声音管理器实例,
或 HTML5 音频管理器。当使用 `pauseAll` 方法时,并在所有当前声音之后,它都会被发送
已暂停 。

听听场景用`this.sound.on('pauseall', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) | 否 | 引用事件发声的音效管理器 。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/PAUSE_ALL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/PAUSE_ALL_EVENT.js#L7)  
引入版本：3.0.0

## PAUSE {#pause}


**说明:** 声音暂停事件。

此事件由Web Audio和HTML5 Audio Sound两个对象在暂停时同时发送.

使用`Sound.on('pause', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('pause', listener);
music.play();
music.pause();
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/PAUSE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/PAUSE_EVENT.js#L7)  
引入版本：3.0.0

## PLAY {#play}


**说明:** 声乐事件.

此事件在播放时由Web Audio和HTML5 Audio Sound两个对象共同发送.

使用`Sound.on('play', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('play', listener);
music.play();
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/PLAY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/PLAY_EVENT.js#L7)  
引入版本：3.0.0

## RATE {#rate}


**说明:** 音速变化事件.

当Web Audio和HTML5 Audio Sound两个对象的频率发生变化时,都会发出这个事件.

使用`Sound.on('rate', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('rate', listener);
music.play();
music.setRate(0.5);
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |
| rate | number | 否 | 声闻新率. |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/RATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/RATE_EVENT.js#L7)  
引入版本：3.0.0

## RESUME_ALL {#resume_all}


**说明:** 恢复所有声音事件。

本次活动由基地声音管理器(Base Sound Manager)发出,或更典型的Web音频声音管理器实例,
或 HTML5 音频管理器。当使用 `resumeAll` 方法时,并在所有当前声音之后,它都会被发送
现已恢复。

听听场景用`this.sound.on('resumeall', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) | 否 | 引用事件发声的音效管理器 。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/RESUME_ALL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/RESUME_ALL_EVENT.js#L7)  
引入版本：3.0.0

## RESUME {#resume}


**说明:** 声音复发事件.

此事件由Web Audio和HTML5 Audio Sound两个对象在从暂停状态恢复时发送.

使用`Sound.on('resume', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('resume', listener);
music.play();
music.pause();
music.resume();
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/RESUME_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/RESUME_EVENT.js#L7)  
引入版本：3.0.0

## SEEK {#seek}


**说明:** 寻声事件.

此事件在被搜索到新位置时, 由Web Audio和HTML5 Audio Sound两个对象发送.

使用`Sound.on('seek', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('seek', listener);
music.play();
music.setSeek(5000);
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |
| seek | number | 否 | 声音的新求值 。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/SEEK_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/SEEK_EVENT.js#L7)  
引入版本：3.0.0

## STOP_ALL {#stop_all}


**说明:** 停止所有声音事件。

本次活动由基地声音管理器(Base Sound Manager)发出,或更典型的Web音频声音管理器实例,
或 HTML5 音频管理器。当使用 `stopAll` 方法时,并在所有当前声音之后,它都会被发送
已经停止。

听听场景用`this.sound.on('stopall', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) | 否 | 引用事件发声的音效管理器 。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/STOP_ALL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/STOP_ALL_EVENT.js#L7)  
引入版本：3.0.0

## STOP {#stop}


**说明:** 止音事件.

此事件在被停止时由Web Audio和HTML5 Audio Sound两个对象发送.

使用`Sound.on('stop', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('stop', listener);
music.play();
music.stop();
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/STOP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/STOP_EVENT.js#L7)  
引入版本：3.0.0

## UNLOCKED {#unlocked}


**说明:** 声音管理器解锁事件 。

本次活动由基地声音管理器(Base Sound Manager)发出,或更典型的Web音频声音管理器实例,
或 HTML5 音频管理器。当声音管理器解锁时,它将在更新循环中发出。用于
Web Audio 这是在页面上的第一个用户手势.

听听场景用`this.sound.on('unlocked', listener)`

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| soundManager | [Phaser.Sound.BaseSoundManager](/api/class/sound-basesoundmanager) | 否 | 引用事件发声的音效管理器 。 |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/UNLOCKED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/UNLOCKED_EVENT.js#L7)  
引入版本：3.0.0

## VOLUME {#volume}


**说明:** 音量事件.

当Web Audio和HTML5 Audio Sound对象的音量变化时,都会由它们发出这个事件.

使用`Sound.on('volume', listener)`从声音实例中听它,即:

```javascript
var music = this.sound.add('key');
music.on('volume', listener);
music.play();
music.setVolume(0.5);
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sound | [Phaser.Sound.WebAudioSound](/api/class/sound-webaudiosound) \| [Phaser.Sound.HTML5AudioSound](/api/class/sound-html5audiosound) | 否 | 提到事件发声的音响。 |
| volume | number | 否 | 音声新卷. |

**所属:** [Phaser.Sound.Events](/api/namespace/sound-events)
> 源码：[src/sound/events/VOLUME_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/sound/events/VOLUME_EVENT.js#L7)  
引入版本：3.0.0

---
