# Animations.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/animations-events)

## ADD_ANIMATION {#add_animation}


**说明:** 增动画事件.

当全球动画管理器中添加了新的动画时,此事件会被发送.

无论是因为动画管理器增加了一个动画实例,
或动画管理器直接创建新动画.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 被加入全球动画管理器的动画的键. |
| animation | [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 刚创作的动画的一个实例. |

**所属:** [Phaser.Animations.Events](/api/namespace/animations-events)
> 源码：[src/animations/events/ADD_ANIMATION_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/events/ADD_ANIMATION_EVENT.js#L7)  
引入版本：3.0.0

## ANIMATION_COMPLETE {#animation_complete}


**说明:** 动画完成事件.

当一个动画在它上播放完成播放时,这个事件由Sprite发出.
当动画到达其序列的尽头时, 就会发生这种情况, 将任何延迟都考虑在内
或者重复它可能必须处理。

设定为循环或永久重复的动画永远不会点燃这个事件,因为
从来没有完成。 如果您需要处理, 请听听 `ANIMATION_STOP`
事件,因为当动画被直接停止时会释放出此信息。

使用 `sprite.on('animationcomplete', listener)` 在Sprite上听

动画事件流如下:

1. `ANIMATION_START`
2. `ANIMATION_UPDATE`(重复了动画的多个帧)
3. `ANIMATION_REPEAT`(仅在动画设定重现时,它才会在此之后发出更多的更新事件)
4. `ANIMATION_COMPLETE`(只有在有限定值或0,重复计数的情况下)
5. `ANIMATION_COMPLETE_KEY`(只有在有限定值或0,重复计数的情况下)

如果动画被直接停止,则会发送`ANIMATION_STOP`事件而不是`ANIMATION_COMPLETE`.

如果动画在播放时重新启动,则会释放 `ANIMATION_RESTART` 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| animation | [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 提及完成的动画. |
| frame | [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) | 否 | 动画的当前动画框架. |
| gameObject | [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) | 否 | 提及动画更新的游戏对象. |
| frameKey | string | 否 | 动画片内动画框架的独特关键. |

**所属:** [Phaser.Animations.Events](/api/namespace/animations-events)
> 源码：[src/animations/events/ANIMATION_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/events/ANIMATION_COMPLETE_EVENT.js#L7)  
引入版本：3.50.0

## ANIMATION_COMPLETE_KEY {#animation_complete_key}


**说明:** 动画"完整的动态键事件".

当一个动画在它上播放完成播放时,这个事件由Sprite发出.
当动画到达其序列的尽头时, 就会发生这种情况, 将任何延迟都考虑在内
或者重复它可能必须处理。

设定为循环或永久重复的动画永远不会点燃这个事件,因为
从来没有完成。 如果您需要处理, 请听听 `ANIMATION_STOP`
事件,因为当动画被直接停止时会释放出此信息。

这件事和`ANIMATION_COMPLETE`事件的不同之处在于,这个事件有一个
动态事件名称, 包含其中的动画名称。 例如,
如果你有动画"`explode`" 你可以听完成这个
使用 `sprite.on('animationcomplete-explode', listener)` 来制作特定的动画。或者,如果你
想要使用类型: `sprite.on(Phaser.Animations.Events.ANIMATION_COMPLETE_KEY + 'explode', listener)`。

动画事件流如下:

1. `ANIMATION_START`
2. `ANIMATION_UPDATE`(重复了动画的多个帧)
3. `ANIMATION_REPEAT`(仅在动画设定重现时,它才会在此之后发出更多的更新事件)
4. `ANIMATION_COMPLETE`(只有在有限定值或0,重复计数的情况下)
5. `ANIMATION_COMPLETE_KEY`(只有在有限定值或0,重复计数的情况下)

如果动画被直接停止,则会发送`ANIMATION_STOP`事件而不是`ANIMATION_COMPLETE`.

如果动画在播放时重新启动,则会释放 `ANIMATION_RESTART` 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| animation | [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 提及完成的动画. |
| frame | [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) | 否 | 动画的当前动画框架. |
| gameObject | [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) | 否 | 提及动画更新的游戏对象. |
| frameKey | string | 否 | 动画片内动画框架的独特关键. |

**所属:** [Phaser.Animations.Events](/api/namespace/animations-events)
> 源码：[src/animations/events/ANIMATION_COMPLETE_KEY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/events/ANIMATION_COMPLETE_KEY_EVENT.js#L7)  
引入版本：3.50.0

## ANIMATION_REPEAT {#animation_repeat}


**说明:** 动画重复事件.

当动画重复播放时,此事件由Sprite发送.
如果动画是创建的,或者播放的,指定了`repeat`值,则会发生这种情况.

动画在达到其序列的末端时会重复.

使用 `sprite.on('animationrepeat', listener)` 在Sprite上听

动画事件流如下:

1. `ANIMATION_START`
2. `ANIMATION_UPDATE`(重复了动画的多个帧)
3. `ANIMATION_REPEAT`(仅在动画设定重现时,它才会在此之后发出更多的更新事件)
4. `ANIMATION_COMPLETE`(只有在有限定值或0,重复计数的情况下)
5. `ANIMATION_COMPLETE_KEY`(只有在有限定值或0,重复计数的情况下)

如果动画被直接停止,则会发送`ANIMATION_STOP`事件而不是`ANIMATION_COMPLETE`.

如果动画在播放时重新启动,则会释放 `ANIMATION_RESTART` 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| animation | [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 重复的提及动画. |
| frame | [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) | 否 | 动画的当前动画框架. |
| gameObject | [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) | 否 | 提及动画重复的游戏对象. |
| frameKey | string | 否 | 动画片内动画框架的独特关键. |

**所属:** [Phaser.Animations.Events](/api/namespace/animations-events)
> 源码：[src/animations/events/ANIMATION_REPEAT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/events/ANIMATION_REPEAT_EVENT.js#L7)  
引入版本：3.50.0

## ANIMATION_RESTART {#animation_restart}


**说明:** 动画"重启事件".

当动画重新开始播放时, 由 Sprite 发送此事件 。
这只有在`Sprite.anims.restart`方法被调用时才会发生.

使用 `sprite.on('animationrestart', listener)` 在Sprite上听

动画事件流如下:

1. `ANIMATION_START`
2. `ANIMATION_UPDATE`(重复了动画的多个帧)
3. `ANIMATION_REPEAT`(仅在动画设定重现时,它才会在此之后发出更多的更新事件)
4. `ANIMATION_COMPLETE`(只有在有限定值或0,重复计数的情况下)
5. `ANIMATION_COMPLETE_KEY`(只有在有限定值或0,重复计数的情况下)

如果动画被直接停止,则会发送`ANIMATION_STOP`事件而不是`ANIMATION_COMPLETE`.

如果动画在播放时重新启动,则会释放 `ANIMATION_RESTART` 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| animation | [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 提及已重启的动画. |
| frame | [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) | 否 | 动画的当前动画框架. |
| gameObject | [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) | 否 | 提及动画重启的游戏对象 。 |
| frameKey | string | 否 | 动画片内动画框架的独特关键. |

**所属:** [Phaser.Animations.Events](/api/namespace/animations-events)
> 源码：[src/animations/events/ANIMATION_RESTART_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/events/ANIMATION_RESTART_EVENT.js#L7)  
引入版本：3.50.0

## ANIMATION_START {#animation_start}


**说明:** 动画开机事件.

当动画开始播放时, 由 Sprite 发送此事件 。
动画播放时会发生这种情况,将可能已经指定的任何延迟计入其中.
此事件发生在延迟到期后, 以及第一次更新事件之前 。

使用 `sprite.on('animationstart', listener)` 在Sprite上听

动画事件流如下:

1. `ANIMATION_START`
2. `ANIMATION_UPDATE`(重复了动画的多个帧)
3. `ANIMATION_REPEAT`(仅在动画设定重现时,它才会在此之后发出更多的更新事件)
4. `ANIMATION_COMPLETE`(只有在有限定值或0,重复计数的情况下)
5. `ANIMATION_COMPLETE_KEY`(只有在有限定值或0,重复计数的情况下)

如果动画被直接停止,则会发送`ANIMATION_STOP`事件而不是`ANIMATION_COMPLETE`.

如果动画在播放时重新启动,则会释放 `ANIMATION_RESTART` 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| animation | [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 参考已开动画. |
| frame | [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) | 否 | 动画的当前动画框架. |
| gameObject | [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) | 否 | 提及动画开始的游戏对象. |
| frameKey | string | 否 | 动画片内动画框架的独特关键. |

**所属:** [Phaser.Animations.Events](/api/namespace/animations-events)
> 源码：[src/animations/events/ANIMATION_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/events/ANIMATION_START_EVENT.js#L7)  
引入版本：3.50.0

## ANIMATION_STOP {#animation_stop}


**说明:** 动画停止事件.

当动画停止时, 由 Sprite 发送此事件。 动画
只有在`Sprite.stop`或`Sprite.anims.stopAfterDelay`等方法停止时才会停止
。如果在当前动画完成前开始新的动画,也可以释放。

使用 `sprite.on('animationstop', listener)` 在Sprite上听

动画事件流如下:

1. `ANIMATION_START`
2. `ANIMATION_UPDATE`(重复了动画的多个帧)
3. `ANIMATION_REPEAT`(仅在动画设定重现时,它才会在此之后发出更多的更新事件)
4. `ANIMATION_COMPLETE`(只有在有限定值或0,重复计数的情况下)
5. `ANIMATION_COMPLETE_KEY`(只有在有限定值或0,重复计数的情况下)

如果动画被直接停止,则会发送`ANIMATION_STOP`事件而不是`ANIMATION_COMPLETE`.

如果动画在播放时重新启动,则会释放 `ANIMATION_RESTART` 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| animation | [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 参考已停动画. |
| frame | [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) | 否 | 动画的当前动画框架. |
| gameObject | [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) | 否 | 提及动画停止的游戏对象 。 |
| frameKey | string | 否 | 动画片内动画框架的独特关键. |

**所属:** [Phaser.Animations.Events](/api/namespace/animations-events)
> 源码：[src/animations/events/ANIMATION_STOP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/events/ANIMATION_STOP_EVENT.js#L7)  
引入版本：3.50.0

## ANIMATION_UPDATE {#animation_update}


**说明:** 动画最新事件.

当动画在它上播放时, 由 Sprite 发出此事件。 当动画改变框架时, 会发生此事件 。
动画会根据帧率和诸如`timeScale`和`delay`等其他因素来改变帧,也可以改变
框,当停止或重新启动时。

使用 `sprite.on('animationupdate', listener)` 在Sprite上听

如果动画的播放速度快于游戏帧率所能处理的速度,则完全有可能发出几张
更新单个游戏框中的事件, 请在您的代码中注意此内容。 ** final ** 事件收到此框架
是游戏中要被转换出来的

动画事件流如下:

1. `ANIMATION_START`
2. `ANIMATION_UPDATE`(重复了动画的多个帧)
3. `ANIMATION_REPEAT`(仅在动画设定重现时,它才会在此之后发出更多的更新事件)
4. `ANIMATION_COMPLETE`(只有在有限定值或0,重复计数的情况下)
5. `ANIMATION_COMPLETE_KEY`(只有在有限定值或0,重复计数的情况下)

如果动画被直接停止,则会发送`ANIMATION_STOP`事件而不是`ANIMATION_COMPLETE`.

如果动画在播放时重新启动,则会释放 `ANIMATION_RESTART` 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| animation | [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 参考更新后的动画. |
| frame | [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) | 否 | 动画的当前动画框架. |
| gameObject | [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) | 否 | 提及动画更新的游戏对象. |
| frameKey | string | 否 | 动画片内动画框架的独特关键. |

**所属:** [Phaser.Animations.Events](/api/namespace/animations-events)
> 源码：[src/animations/events/ANIMATION_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/events/ANIMATION_UPDATE_EVENT.js#L7)  
引入版本：3.50.0

## PAUSE_ALL {#pause_all}


**说明:** 暂停所有动画事件。

当全球动画管理器被告知暂停时,此事件会被发送.

当发生这种情况时,所有目前的动画都会停止更新,尽管这并不一定意味着
游戏也暂停了

**所属:** [Phaser.Animations.Events](/api/namespace/animations-events)
> 源码：[src/animations/events/PAUSE_ALL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/events/PAUSE_ALL_EVENT.js#L7)  
引入版本：3.0.0

## REMOVE_ANIMATION {#remove_animation}


**说明:** 移除动画事件.

本次事件是在动画从全球动画管理器中删除时发送的.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 从全球动画管理器中移除的动画的键. |
| animation | [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 被移除的动画的一个实例. |

**所属:** [Phaser.Animations.Events](/api/namespace/animations-events)
> 源码：[src/animations/events/REMOVE_ANIMATION_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/events/REMOVE_ANIMATION_EVENT.js#L7)  
引入版本：3.0.0

## RESUME_ALL {#resume_all}


**说明:** 续作"全动画事件".

本次事件是在全球动画管理器恢复时发出,此前曾暂停.

当这种情况发生时,所有目前的动画都会继续更新.

**所属:** [Phaser.Animations.Events](/api/namespace/animations-events)
> 源码：[src/animations/events/RESUME_ALL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/events/RESUME_ALL_EVENT.js#L7)  
引入版本：3.0.0

---
