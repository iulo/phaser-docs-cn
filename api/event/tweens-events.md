# Tweens.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/tweens-events)

## TWEEN_ACTIVE {#tween_active}


**说明:** 文活动.

当Tween管理器内部活动时,这个事件由Tween公司发出.

正在更新的“ 活动” Tween 是一个正在更新的
任意目标属性, 由 `delay` 等设置决定。 如果您需要何时发生事件
Tween开始更新它的第一个属性,见`TWEEN_START`.

听听Tween案使用`Tween.on('active', listener)`的音效,即:

```javascript
var tween = this.tweens.create({
    targets: image,
    x: 500,
    ease: 'Power1',
    duration: 3000
});
tween.on('active', listener);
this.tweens.existing(tween);
```

请注意,通常在您拨打 `this.tweens.add()` 时,此事件已经发出,并且是
用于`tweens.create()`和/或`tweens.existing()`.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| targets | any \| Array.\<any> | 否 | Tween 的目标。 如果Tween 具有多个目标, 将会是一系列目标 。 |

**所属:** [Phaser.Tweens.Events](/api/namespace/tweens-events)
> 源码：[src/tweens/events/TWEEN_ACTIVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_ACTIVE_EVENT.js#L7)  
引入版本：3.19.0

## TWEEN_COMPLETE {#tween_complete}


**说明:** 特温事件

此事件由 Tween 发送, 当它完全完成回放时, 将重复和循环作为因素 。

如果Tween被设定为无限循环或重复,则此事件将不会被发送
除非`Tween.stop`方法被称作.

如果一个Tween有`completeDelay`的设定,此事件将在延迟到期后点燃.

听听Tween案使用`Tween.on('complete', listener)`的音效,即:

```javascript
var tween = this.tweens.add({
    targets: image,
    x: 500,
    ease: 'Power1',
    duration: 3000
});
tween.on('complete', listener);
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| targets | any \| Array.\<any> | 否 | Tween 的目标。 如果Tween 具有多个目标, 将会是一系列目标 。 |

**所属:** [Phaser.Tweens.Events](/api/namespace/tweens-events)
> 源码：[src/tweens/events/TWEEN_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_COMPLETE_EVENT.js#L7)  
引入版本：3.19.0

## TWEEN_LOOP {#tween_loop}


**说明:** 特温圈事件.

此事件在循环时由 Tween 发送 。

只有在 Tween 设置了循环计数时,此事件才会被发送 。

如果一个Tween有`loopDelay`的设定,此事件将在延迟到期后点燃.

`loop`和`repeat`的区别在于,`repeat`是一个属性设置,
和`loop`一样 适用于整个Tween

听听Tween案使用`Tween.on('loop', listener)`的音效,即:

```javascript
var tween = this.tweens.add({
    targets: image,
    x: 500,
    ease: 'Power1',
    duration: 3000,
    loop: 6
});
tween.on('loop', listener);
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| targets | any \| Array.\<any> | 否 | Tween 的目标。 如果Tween 具有多个目标, 将会是一系列目标 。 |

**所属:** [Phaser.Tweens.Events](/api/namespace/tweens-events)
> 源码：[src/tweens/events/TWEEN_LOOP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_LOOP_EVENT.js#L7)  
引入版本：3.19.0

## TWEEN_PAUSE {#tween_pause}


**说明:** 特温暂停事件.

此事件在暂停时由 Tween 发送 。

听听Tween案使用`Tween.on('pause', listener)`的音效,即:

```javascript
var tween = this.tweens.add({
    targets: image,
    ease: 'Power1',
    duration: 3000,
    x: 600
});
tween.on('pause', listener);
// At some point later ...
tween.pause();
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |

**所属:** [Phaser.Tweens.Events](/api/namespace/tweens-events)
> 源码：[src/tweens/events/TWEEN_PAUSE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_PAUSE_EVENT.js#L7)  
引入版本：3.60.0

## TWEEN_REPEAT {#tween_repeat}


**说明:** 文复事件.

当一个属性在反复旋转时, 此事件由 Tween 发送 。

只有Tween拥有一个具有重复计数集的属性,此事件才会被发送.

如果一个Tween有`repeatDelay`的设定,此事件将在延迟到期后点燃.

`loop`和`repeat`的区别在于,`repeat`是一个属性设置,
和`loop`一样 适用于整个Tween

听听Tween案使用`Tween.on('repeat', listener)`的音效,即:

```javascript
var tween = this.tweens.add({
    targets: image,
    x: 500,
    ease: 'Power1',
    duration: 3000,
    repeat: 4
});
tween.on('repeat', listener);
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| key | string | 否 | 目标上的属性,刚刚重复, 即`x`或`scaleY`, 或者任何你正在调整的属性。 |
| target | any | 否 | 重复的目标对象。 通常是一个游戏对象, 但可以是任意类型的 。 |
| current | number | 否 | 目标上设定的属性的当前值 。 |
| previous | number | 否 | 目标上设定的房产的上一个值 。 |

**所属:** [Phaser.Tweens.Events](/api/namespace/tweens-events)
> 源码：[src/tweens/events/TWEEN_REPEAT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_REPEAT_EVENT.js#L7)  
引入版本：3.19.0

## TWEEN_RESUME {#tween_resume}


**说明:** 文复会事件.

本次事件由Tween在暂停状态恢复时发出.

听听Tween案使用`Tween.on('resume', listener)`的音效,即:

```javascript
var tween = this.tweens.add({
    targets: image,
    ease: 'Power1',
    duration: 3000,
    x: 600
});
tween.on('resume', listener);
// At some point later ...
tween.resume();
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |

**所属:** [Phaser.Tweens.Events](/api/namespace/tweens-events)
> 源码：[src/tweens/events/TWEEN_RESUME_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_RESUME_EVENT.js#L7)  
引入版本：3.60.0

## TWEEN_START {#tween_start}


**说明:** 文起事.

这件事情由特温公司在开始调整其第一块地产时发出.

特温只发出一次,因为它只能发动一次.

如果一个Tween有`delay`的设定,此事件将在延迟到期后点燃.

听听Tween案使用`Tween.on('start', listener)`的音效,即:

```javascript
var tween = this.tweens.add({
    targets: image,
    x: 500,
    ease: 'Power1',
    duration: 3000
});
tween.on('start', listener);
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| targets | any \| Array.\<any> | 否 | Tween 的目标。 如果Tween 具有多个目标, 将会是一系列目标 。 |

**所属:** [Phaser.Tweens.Events](/api/namespace/tweens-events)
> 源码：[src/tweens/events/TWEEN_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_START_EVENT.js#L7)  
引入版本：3.19.0

## TWEEN_STOP {#tween_stop}


**说明:** 州停运事件.

此事件在停止时由特温发送.

听听Tween案使用`Tween.on('stop', listener)`的音效,即:

```javascript
var tween = this.tweens.add({
    targets: image,
    x: 500,
    ease: 'Power1',
    duration: 3000
});
tween.on('stop', listener);
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| targets | any \| Array.\<any> | 否 | Tween 的目标。 如果Tween 具有多个目标, 将会是一系列目标 。 |

**所属:** [Phaser.Tweens.Events](/api/namespace/tweens-events)
> 源码：[src/tweens/events/TWEEN_STOP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_STOP_EVENT.js#L7)  
引入版本：3.24.0

## TWEEN_UPDATE {#tween_update}


**说明:** 文更新事件.

每次更新其正在调整的属性的_ 任意_ 时, 此事件都会由 Tween 发送 。

正在改变目标3个属性的Tween会发出这个事件,每次改变3次,每次一次.

**注意:** 这是一个非常高频事件,可能多次发出,每个帧.

听听Tween案使用`Tween.on('update', listener)`的音效,即:

```javascript
var tween = this.tweens.add({
    targets: image,
    x: 500,
    ease: 'Power1',
    duration: 3000,
});
tween.on('update', listener);
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| key | string | 否 | 目标上刚刚更新的属性,即`x`或`scaleY`,或者任何你正在调整的属性. |
| target | any | 否 | 更新的目标对象。 通常是一个游戏对象, 但可以是任意类型的 。 |
| current | number | 否 | 已调整的属性的当前值 。 |
| previous | number | 否 | 更新前的已调整属性的上一个值 。 |

**所属:** [Phaser.Tweens.Events](/api/namespace/tweens-events)
> 源码：[src/tweens/events/TWEEN_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_UPDATE_EVENT.js#L7)  
引入版本：3.19.0

## TWEEN_YOYO {#tween_yoyo}


**说明:** 阳事件.

每当有属性在给Yoyos发短信时, 都会有特温公司发出信号。

只有Tween拥有了`yoyo`设定的属性,此事件才会被发出.

如果Tween有`hold`值,则在持有到期时发出此事件.

本次活动是针对每一个属性 以及每个目标 尤尤斯
例如,如果一个Tween正在更新2个属性,并且有10个目标,那么这个事件
将派遣20次,你们要小心地使用它。

听听Tween案使用`Tween.on('yoyo', listener)`的音效,即:

```javascript
var tween = this.tweens.add({
    targets: image,
    x: 500,
    ease: 'Power1',
    duration: 3000,
    yoyo: true
});
tween.on('yoyo', listener);
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| key | string | 否 | 目标上的属性 刚刚Yoyo'd, 即`x`或`scaleY`, 或任何你正在调整的属性。 |
| target | any | 否 | 原为yoyod的目标对象,通常为游戏对象,但可以是任意类型. |
| current | number | 否 | 目标上设定的属性的当前值 。 |
| previous | number | 否 | 目标上设定的房产的上一个值 。 |

**所属:** [Phaser.Tweens.Events](/api/namespace/tweens-events)
> 源码：[src/tweens/events/TWEEN_YOYO_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_YOYO_EVENT.js#L7)  
引入版本：3.19.0

---
