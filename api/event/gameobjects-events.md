# GameObjects.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/gameobjects-events)

## ADDED_TO_SCENE {#added_to_scene}


**说明:** 游戏对象添加到场景事件 。

当游戏对象被添加到场景中时,此事件会被发送 。

在游戏对象实例上用`GameObject.on('addedtoscene', listener)`来听.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象被添加到场景中 。 |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 游戏对象被添加到的景色 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/ADDED_TO_SCENE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/ADDED_TO_SCENE_EVENT.js#L7)  
引入版本：3.50.0

## DESTROY {#destroy}


**说明:** 游戏对象毁灭事件 。

当游戏对象实例被销毁时, 将会发出此事件 。

在游戏对象实例上用`GameObject.on('destroy', listener)`来听.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 正在被销毁的游戏对象 。 |
| fromScene | boolean | 否 | `True` 如果游戏对象被场景所破坏, `false` 如果不是的话。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/DESTROY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/DESTROY_EVENT.js#L7)  
引入版本：3.0.0

## REMOVED_FROM_SCENE {#removed_from_scene}


**说明:** 游戏对象从场景事件中移除 。

当游戏对象从场景中移除时,此事件会被发送 。

在游戏对象实例上用`GameObject.on('removedfromscene', listener)`来听.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象被删除于场景 。 |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 游戏对象被删除的场景 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/REMOVED_FROM_SCENE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/REMOVED_FROM_SCENE_EVENT.js#L7)  
引入版本：3.50.0

## VIDEO_COMPLETE {#video_complete}


**说明:** 视频游戏对象完成事件.

当视频完成播放并到达持续时间结束时, 将发送此事件。 它
如果正在播放视频标记序列并到达尾端,也会发出。

请注意,并非所有视频都可以点燃此事件。例如,直播流没有固定的持续时间,
所以从技术上讲,绝对不要"完成".

如果一段视频停止播放,通过`Video.stop`方法,它会释放出
`VIDEO_STOP` 事件而不是这个。

使用 `Video.on('complete', listener)` 从视频游戏对象实例中听取它 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 完成回放的视频游戏对象 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_COMPLETE_EVENT.js#L7)  
引入版本：3.20.0

## VIDEO_CREATED {#video_created}


**说明:** 电子游戏对象创建事件.

当视频的纹理创建时, 将发送此事件。 发生此事件
当视频源已装入足够多的视频源,浏览器可以制成一个
框从它。

使用 `Video.on('created', listener)` 从视频游戏对象实例中听取它 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 视频游戏对象 , 举办此事件 。 |
| width | number | 否 | 视频的宽度. |
| height | number | 否 | 视频的高度. |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_CREATED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_CREATED_EVENT.js#L7)  
引入版本：3.20.0

## VIDEO_ERROR {#video_error}


**说明:** 视频游戏对象错误事件.

当视频试图播放不存在的源, 或者是错误的文件类型时, 将发送此事件 。

使用 `Video.on('error', listener)` 从视频游戏对象实例中听取它 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 丢出错误的视频游戏对象 。 |
| event | DOMException \| string | 否 | 浏览器在回放时提出的本地 DOM 事件 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_ERROR_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_ERROR_EVENT.js#L7)  
引入版本：3.20.0

## VIDEO_LOCKED {#video_locked}


**说明:** 视频游戏对象锁定事件.

此事件是在试图播放视频时发送的, 但浏览器阻止了它
媒体参与互动政策导致的不这样做。

如果您得到此事件, 您需要等待用户在浏览器之前进行交互
。这是防止视频自动播放的浏览器安全措施。
音频。交互包括鼠标点击、触摸或按键。

使用 `Video.on('locked', listener)` 从视频游戏对象实例中听取它 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 视频游戏对象 , 举办此事件 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_LOCKED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_LOCKED_EVENT.js#L7)  
引入版本：3.60.0

## VIDEO_LOOP {#video_loop}


**说明:** 电子游戏对象循环事件.

当正在播放的视频循环时, 发送此事件。 只此
如果指定了`loop`参数,或者使用`setLoop`方法,则会发生。
如果视频有固定的长度,例如,视频流不能循环,例如
他们没有期限。

循环是基于视频 `timeupdate`事件的结果。 此事件不是
帧精确, 由于浏览器的工作方式, 请不要依赖此循环 。
事件是时间或框架的精确。

使用 `Video.on('loop', listener)` 从视频游戏对象实例中听取它 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 循环的视频游戏对象 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_LOOP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_LOOP_EVENT.js#L7)  
引入版本：3.20.0

## VIDEO_METADATA {#video_metadata}


**说明:** 电子游戏对象元数据事件.

当视频访问元数据时, 将发送此事件 。

使用 `Video.on('metadata', listener)` 从视频游戏对象实例中听取它 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 启动此事件的视频游戏对象 。 |
| event | DOMException \| string | 否 | 浏览器在回放时提出的本地 DOM 事件 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_METADATA_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_METADATA_EVENT.js#L7)  
引入版本：3.80.0

## VIDEO_PLAYING {#video_playing}


**说明:** 视频游戏对象播放事件 。

播放活动在播放开始后即开始播放,
并当它重新启动时。例如,在重播时它会被发射
由于缺乏数据,暂停或延迟后恢复。

使用 `Video.on('playing', listener)` 从视频游戏对象实例中听取它 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 开始播放的视频游戏对象 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_PLAYING_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_PLAYING_EVENT.js#L7)  
引入版本：3.60.0

## VIDEO_PLAY {#video_play}


**说明:** 电子游戏对象游戏事件.

当视频开始重播时, 将发送此事件。 对于不需要的视频
交互解锁,通常在`Video.play`方法被调用后立即进行.
但是,对于需要解锁的视频,一旦播放开始,就会发射
已经解锁了

使用 `Video.on('play', listener)` 从视频游戏对象实例中听取它 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 开始播放的视频游戏对象 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_PLAY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_PLAY_EVENT.js#L7)  
引入版本：3.20.0

## VIDEO_SEEKED {#video_seeked}


**说明:** 电子游戏对象搜索事件.

当视频完成搜索时, 将发送此事件。

使用 `Video.on('seeked', listener)` 从视频游戏对象实例中听取它 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 完成搜索的视频游戏对象 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_SEEKED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_SEEKED_EVENT.js#L7)  
引入版本：3.20.0

## VIDEO_SEEKING {#video_seeking}


**说明:** 电子游戏对象搜索事件.

当视频_ begins_ 寻求时间线中的新点时, 将发送此事件 。
当搜索完成后,它将发送`VIDEO_SEEKED`事件以结束.

使用 `Video.on('seeking', listener)` 从视频游戏对象实例中听取它 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 开始寻找的视频游戏对象 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_SEEKING_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_SEEKING_EVENT.js#L7)  
引入版本：3.20.0

## VIDEO_STALLED {#video_stalled}


**说明:** 视频游戏对象已停止事件 。

当视频播放时, 由视频游戏对象发送此事件 。

如果视频是缓冲的,这种情况就可能发生.

如果为下列任何本地 DOM 事件开火:

`stalled`
`suspend`
`waiting`

使用 `Video.on('stalled', listener)` 从视频游戏对象实例中听取它 。

注意,被停滞并不总是消极的,如果视频被停滞,就可能被停止
已下载足够的数据到缓冲器, 以至在
已打开当前批框 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 丢出错误的视频游戏对象 。 |
| event | Event | 否 | 浏览器在回放时提出的本地 DOM 事件 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_STALLED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_STALLED_EVENT.js#L7)  
引入版本：3.60.0

## VIDEO_STOP {#video_stop}


**说明:** 视频游戏对象停止事件 。

视频通过`Video.stop`方法停止播放时,会发出此事件,
或直接通过游戏代码,或因改变视频源或破坏视频源而间接产生.

使用 `Video.on('stop', listener)` 从视频游戏对象实例中听取它 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 停止播放的视频游戏对象 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_STOP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_STOP_EVENT.js#L7)  
引入版本：3.20.0

## VIDEO_TEXTURE {#video_texture}


**说明:** 电子游戏对象纹理准备事件.

此事件由一个视频游戏对象在完成创建纹理后发送.

当视频完成为它的第一个帧装入足够的数据时,就会出现这种情况.

如果你想在游戏中其它地方使用视频纹理,比如Sprite纹理,
那你应该先听这个事件,然后再创建使用它的Sprites.

使用 `Video.on('textureready', listener)` 从视频游戏对象实例中听取它 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 发布此事件的视频游戏对象 。 |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 创造的纹理。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_TEXTURE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_TEXTURE_EVENT.js#L7)  
引入版本：3.60.0

## VIDEO_UNLOCKED {#video_unlocked}


**说明:** 视频游戏对象解锁事件.

当一个视频由于浏览器而无法播放时, 事件会发出
媒体互动政策,通过用户姿态解锁。

使用 `Video.on('unlocked', listener)` 从视频游戏对象实例中听取它 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 视频游戏对象 , 举办此事件 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_UNLOCKED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_UNLOCKED_EVENT.js#L7)  
引入版本：3.20.0

## VIDEO_UNSUPPORTED {#video_unsupported}


**说明:** 视频游戏对象不支持的事件 。

如果媒体来源, 此事件由视频游戏对象发送
(可指定为MediaStream、MediaSource、Blob或File,
例如)不代表支持的媒体格式.

使用 `Video.on('unsupported', listener)` 从视频游戏对象实例中听取它 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| video | [Phaser.GameObjects.Video](/api/class/gameobjects-video) | 否 | 开始播放的视频游戏对象 。 |
| event | DOMException \| string | 否 | 浏览器在回放时提出的本地 DOM 事件 。 |

**所属:** [Phaser.GameObjects.Events](/api/namespace/gameobjects-events)
> 源码：[src/gameobjects/events/VIDEO_UNSUPPORTED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/events/VIDEO_UNSUPPORTED_EVENT.js#L7)  
引入版本：3.60.0

---
