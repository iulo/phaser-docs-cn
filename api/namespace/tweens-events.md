# Phaser.Tweens.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/tweens-events)

Scope: 
static
> 源码：[src/tweens/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/index.js#L7)  


## 静态函数 {#static-functions}

### TWEEN_ACTIVE {#TWEEN_ACTIVE}

#### TWEEN_ACTIVE {#tween_active}


**说明:**

文活动.

当Tween管理器内部活动时,这个事件由Tween公司发出.

“ 活动” Tween 是一个正在进步的, 尽管由于 `delay` 等设置, 它可能还没有更新任何目标属性。 如果您需要Tween 开始实际更新其第一个属性时的事件, 请参见 `TWEEN_START` 。

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

注意,此事件通常在您拨打`this.tweens.add()`时已经发出,并打算与`tweens.create()`和/或`tweens.existing()`一起使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| targets | any \| Array.\<any> | 否 | Tween 的目标。 如果Tween 具有多个目标, 将会是一系列目标 。 |


> 源码：[src/tweens/events/TWEEN_ACTIVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_ACTIVE_EVENT.js#L7)  
引入版本：3.19.0


---

### TWEEN_COMPLETE {#TWEEN_COMPLETE}

#### TWEEN_COMPLETE {#tween_complete}


**说明:**

特温事件

此事件由 Tween 发送, 当它完全完成回放时, 将重复和循环作为因素 。

如果Tween被设定为循环或无限重复,除非调用`Tween.stop`方法,否则将不会发出此事件.

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

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| targets | any \| Array.\<any> | 否 | Tween 的目标。 如果Tween 具有多个目标, 将会是一系列目标 。 |


> 源码：[src/tweens/events/TWEEN_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_COMPLETE_EVENT.js#L7)  
引入版本：3.19.0


---

### TWEEN_LOOP {#TWEEN_LOOP}

#### TWEEN_LOOP {#tween_loop}


**说明:**

特温圈事件.

此事件在循环时由 Tween 发送 。

只有在 Tween 设置了循环计数时,此事件才会被发送 。

如果一个Tween有`loopDelay`的设定,此事件将在延迟到期后点燃.

`loop`和`repeat`的区别在于`repeat`是一个属性设置,其中-as `loop`适用于整个Tween.

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

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| targets | any \| Array.\<any> | 否 | Tween 的目标。 如果Tween 具有多个目标, 将会是一系列目标 。 |


> 源码：[src/tweens/events/TWEEN_LOOP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_LOOP_EVENT.js#L7)  
引入版本：3.19.0


---

### TWEEN_PAUSE {#TWEEN_PAUSE}

#### TWEEN_PAUSE {#tween_pause}


**说明:**

特温暂停事件.

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

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |


> 源码：[src/tweens/events/TWEEN_PAUSE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_PAUSE_EVENT.js#L7)  
引入版本：3.60.0


---

### TWEEN_REPEAT {#TWEEN_REPEAT}

#### TWEEN_REPEAT {#tween_repeat}


**说明:**

文复事件.

当一个属性在反复旋转时, 此事件由 Tween 发送 。

只有Tween拥有一个具有重复计数集的属性,此事件才会被发送.

如果一个Tween有`repeatDelay`的设定,此事件将在延迟到期后点燃.

`loop`和`repeat`的区别在于`repeat`是一个属性设置,其中-as `loop`适用于整个Tween.

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

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| key | string | 否 | 目标上的属性,刚刚重复, 即`x`或`scaleY`, 或者任何你正在调整的属性。 |
| target | any | 否 | 重复的目标对象。 通常是一个游戏对象, 但可以是任意类型的 。 |
| current | number | 否 | 目标上设定的属性的当前值 。 |
| previous | number | 否 | 目标上设定的房产的上一个值 。 |


> 源码：[src/tweens/events/TWEEN_REPEAT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_REPEAT_EVENT.js#L7)  
引入版本：3.19.0


---

### TWEEN_RESUME {#TWEEN_RESUME}

#### TWEEN_RESUME {#tween_resume}


**说明:**

文复会事件.

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

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |


> 源码：[src/tweens/events/TWEEN_RESUME_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_RESUME_EVENT.js#L7)  
引入版本：3.60.0


---

### TWEEN_START {#TWEEN_START}

#### TWEEN_START {#tween_start}


**说明:**

文起事.

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

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| targets | any \| Array.\<any> | 否 | Tween 的目标。 如果Tween 具有多个目标, 将会是一系列目标 。 |


> 源码：[src/tweens/events/TWEEN_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_START_EVENT.js#L7)  
引入版本：3.19.0


---

### TWEEN_STOP {#TWEEN_STOP}

#### TWEEN_STOP {#tween_stop}


**说明:**

州停运事件.

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

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| targets | any \| Array.\<any> | 否 | Tween 的目标。 如果Tween 具有多个目标, 将会是一系列目标 。 |


> 源码：[src/tweens/events/TWEEN_STOP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_STOP_EVENT.js#L7)  
引入版本：3.24.0


---

### TWEEN_UPDATE {#TWEEN_UPDATE}

#### TWEEN_UPDATE {#tween_update}


**说明:**

文更新事件.

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

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| key | string | 否 | 目标上刚刚更新的属性,即`x`或`scaleY`,或者任何你正在调整的属性. |
| target | any | 否 | 更新的目标对象。 通常是一个游戏对象, 但可以是任意类型的 。 |
| current | number | 否 | 已调整的属性的当前值 。 |
| previous | number | 否 | 更新前的已调整属性的上一个值 。 |


> 源码：[src/tweens/events/TWEEN_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_UPDATE_EVENT.js#L7)  
引入版本：3.19.0


---

### TWEEN_YOYO {#TWEEN_YOYO}

#### TWEEN_YOYO {#tween_yoyo}


**说明:**

阳事件.

每当有属性在给Yoyos发短信时, 都会有特温公司发出信号。

只有Tween拥有了`yoyo`设定的属性,此事件才会被发出.

如果Tween有`hold`值,则在持有到期时发出此事件.

本次活动是为每个属性和每个目标,即Yoyos的。例如,如果一个Tween正在更新2个属性,并且有10个目标,则这次活动将发出20次(每目标两次),所以请小心如何使用它!

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

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 提到事件发端的特温事件。 |
| key | string | 否 | 目标上的属性 刚刚Yoyo'd, 即`x`或`scaleY`, 或任何你正在调整的属性。 |
| target | any | 否 | 原为yoyod的目标对象,通常为游戏对象,但可以是任意类型. |
| current | number | 否 | 目标上设定的属性的当前值 。 |
| previous | number | 否 | 目标上设定的房产的上一个值 。 |


> 源码：[src/tweens/events/TWEEN_YOYO_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/events/TWEEN_YOYO_EVENT.js#L7)  
引入版本：3.19.0


---

---
