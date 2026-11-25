# TweenChain {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tweens-tweenchain)

(TweenChain)是  的一种特殊类型,可以使您创建  的序列,链条为单体,并加入  管理器.

串排按顺序播放, 从开始到完成。 您可以选择设置链条重复您想要的多次 。 一旦链条播放完毕, 或者如果设置了重复, 链条中的所有串排都会自动被销毁 。 要覆盖此选项, 请设置“ persist” 参数为“ true ” 。

播放会立即开始, 除非已配置 _ first_ Tween 暂停 。

请注意,补间动画不会操纵任何以下划线开头的目标属性.

**构造函数**

`new TweenChain(parent)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) \| [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) | 否 | 参考了Tween经理,或TweenChain,拥有这个TweenChain. |

---


**作用域**: static


**继承**

> [Phaser.Tweens.BaseTween](/api/class/tweens-basetween)  



> 源码：[src/tweens/tween/TweenChain.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L15)  
引入版本：3.60.0

## 继承的成员 {#inherited-members}


**From [Phaser.Tweens.BaseTween](/api/class/tweens-basetween):**


 - [callbacks](/api/class/tweens-basetween#callbacks)
 - [callbackScope](/api/class/tweens-basetween#callbackScope)
 - [completeDelay](/api/class/tweens-basetween#completeDelay)
 - [countdown](/api/class/tweens-basetween#countdown)
 - [data](/api/class/tweens-basetween#data)
 - [hasStarted](/api/class/tweens-basetween#hasStarted)
 - [loop](/api/class/tweens-basetween#loop)
 - [loopCounter](/api/class/tweens-basetween#loopCounter)
 - [loopDelay](/api/class/tweens-basetween#loopDelay)
 - [parent](/api/class/tweens-basetween#parent)
 - [paused](/api/class/tweens-basetween#paused)
 - [persist](/api/class/tweens-basetween#persist)
 - [startDelay](/api/class/tweens-basetween#startDelay)
 - [state](/api/class/tweens-basetween#state)
 - [timeScale](/api/class/tweens-basetween#timeScale)
 - [totalData](/api/class/tweens-basetween#totalData)




---

## 公开成员 {#public-members}

### currentIndex {#currentIndex}

#### currentIndex: number {#currentindex-number}


**说明:**

引用当前播放的 tween 的数据数组索引 。


> 源码：[src/tweens/tween/TweenChain.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L56)  
引入版本：3.60.0


---

### currentTween {#currentTween}

#### currentTween: [Phaser.Tweens.Tween](/api/class/tweens-tween) {#currenttween-phasertweenstween}


**说明:**

参考了这个TweenChain目前演奏的Tween.


> 源码：[src/tweens/tween/TweenChain.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L47)  
引入版本：3.60.0


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





**From [Phaser.Tweens.BaseTween](/api/class/tweens-basetween):**


 - [complete](/api/class/tweens-basetween#complete)
 - [completeAfterLoop](/api/class/tweens-basetween#completeAfterLoop)
 - [getTimeScale](/api/class/tweens-basetween#getTimeScale)
 - [isActive](/api/class/tweens-basetween#isActive)
 - [isCompleteDelayed](/api/class/tweens-basetween#isCompleteDelayed)
 - [isDestroyed](/api/class/tweens-basetween#isDestroyed)
 - [isFinished](/api/class/tweens-basetween#isFinished)
 - [isLoopDelayed](/api/class/tweens-basetween#isLoopDelayed)
 - [isPaused](/api/class/tweens-basetween#isPaused)
 - [isPending](/api/class/tweens-basetween#isPending)
 - [isPendingRemove](/api/class/tweens-basetween#isPendingRemove)
 - [isPlaying](/api/class/tweens-basetween#isPlaying)
 - [isRemoved](/api/class/tweens-basetween#isRemoved)
 - [isStartDelayed](/api/class/tweens-basetween#isStartDelayed)
 - [onCompleteHandler](/api/class/tweens-basetween#onCompleteHandler)
 - [pause](/api/class/tweens-basetween#pause)
 - [resume](/api/class/tweens-basetween#resume)
 - [setActiveState](/api/class/tweens-basetween#setActiveState)
 - [setCallback](/api/class/tweens-basetween#setCallback)
 - [setCompleteDelayState](/api/class/tweens-basetween#setCompleteDelayState)
 - [setDestroyedState](/api/class/tweens-basetween#setDestroyedState)
 - [setFinishedState](/api/class/tweens-basetween#setFinishedState)
 - [setLoopDelayState](/api/class/tweens-basetween#setLoopDelayState)
 - [setPendingRemoveState](/api/class/tweens-basetween#setPendingRemoveState)
 - [setPendingState](/api/class/tweens-basetween#setPendingState)
 - [setRemovedState](/api/class/tweens-basetween#setRemovedState)
 - [setStartDelayState](/api/class/tweens-basetween#setStartDelayState)
 - [setTimeScale](/api/class/tweens-basetween#setTimeScale)
 - [stop](/api/class/tweens-basetween#stop)
 - [updateCompleteDelay](/api/class/tweens-basetween#updateCompleteDelay)
 - [updateLoopCountdown](/api/class/tweens-basetween#updateLoopCountdown)
 - [updateStartCountdown](/api/class/tweens-basetween#updateStartCountdown)





**From [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain):**


 - [makeActive](/api/class/tweens-tweenchain#makeActive)
 - [remove](/api/class/tweens-tweenchain#remove)




---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(tweens) {#instance-addtweens}


**说明:**

建立"补间动画"的序列,连锁到另一个,并加入到这个特温钱中.

串排按顺序播放, 从开始到完成。 您可以选择设置链条重复您想要的多次 。 一旦链条播放完毕, 或者如果设置了重复, 链条中的所有串排都会自动被销毁 。 要覆盖此选项, 请设置“ persist” 参数为“ true ” 。

播放会立即开始, 除非已配置 _ first_ Tween 暂停 。

请注意,补间动画不会操纵任何以下划线开头的目标属性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tweens | Array.\<[Phaser.Types.Tweens.TweenBuilderConfig](/api/typedef/types-tweens#tweenbuilderconfig)> \| Array.\<object> | 否 | 此链中的 Tween 配置对象阵列 。 |


**返回值:** [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) - 此特云钦例.


> 源码：[src/tweens/tween/TweenChain.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L95)  
引入版本：3.60.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

立即摧毁这个特温琴, 废除它的所有引用。


**重写:** Phaser.Tweens.BaseTween#销毁


> 源码：[src/tweens/tween/TweenChain.js#L534](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L534)  
引入版本：3.60.0


---

### dispatchEvent {#dispatchEvent}

#### \<instance> dispatchEvent(event, [callback]) {#instance-dispatcheventevent-callback}


**说明:**

内部方法,将释放基于TweenChain的事件并引用给定的回调.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | [Phaser.Types.Tweens.Event](/api/typedef/types-tweens#event) | 否 | 即将举行的活动。 |
| callback | [Phaser.Types.Tweens.TweenCallbackTypes](/api/typedef/types-tweens#tweencallbacktypes) | 是 | 引用的回调名称。 可以是 `null` 或 `undefined` 来跳过引用 。 |


> 源码：[src/tweens/tween/TweenChain.js#L513](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L513)  
引入版本：3.60.0


---

### hasTarget {#hasTarget}

#### \<instance> hasTarget(target) {#instance-hastargettarget}


**说明:**

看看这个Tween链中是否有一个Tween 链正在对指定目标采取行动.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | object | 否 | 目标检查这个TweenChain。 |


**返回值:** boolean - `true` 如果给定的目标 是这个TweenChain的目标, 否则 `false`.


> 源码：[src/tweens/tween/TweenChain.js#L172](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L172)  
引入版本：3.60.0


---

### init {#init}

#### \<instance> init() {#instance-init}


**说明:**

准备这个TweenChain回放。

由 Tween 管理器自动调用。 不应该直接调用 。


**返回值:** [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) - 此特云钦例.


**触发事件:** [Phaser.Tweens.Events#event:TWEEN_ACTIVE](/api/event/tweens-events#tween_active)


> 源码：[src/tweens/tween/TweenChain.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L66)  
引入版本：3.60.0


---

### makeActive {#makeActive}

#### \<instance> makeActive(tween) {#instance-makeactivetween}


**说明:**

重新启用给定的特温,并将其设定为主动状态.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 特温重创,定置为积极州. |


**返回值:** [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) - 此特云钦例.


> 源码：[src/tweens/tween/TweenChain.js#L251](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L251)  
引入版本：3.60.0


---

### nextState {#nextState}

#### \<instance> nextState() {#instance-nextstate}


**说明:**

推进到TweenChain播放的下一状态的内部方法.


**返回值:** boolean - 如果TweenChain完成了,就用`true`, 否则用`false`.


**触发事件:** [Phaser.Tweens.Events#event:TWEEN_COMPLETE](/api/event/tweens-events#tween_complete), [Phaser.Tweens.Events#event:TWEEN_LOOP](/api/event/tweens-events#tween_loop)


> 源码：[src/tweens/tween/TweenChain.js#L271](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L271)  
引入版本：3.60.0


---

### nextTween {#nextTween}

#### \<instance> nextTween() {#instance-nexttween}


**说明:**

立即推进到链条中的下一个特温.

通常这在内部称为,但如果出于某种原因需要推进回放,可以使用.


**返回值:** boolean - 如果链子里没有Tweens的话,就用`true`,否则用`false`.


> 源码：[src/tweens/tween/TweenChain.js#L468](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L468)  
引入版本：3.60.0


---

### play {#play}

#### \<instance> play() {#instance-play}


**说明:**

开始玩《TweenChain》

您只需在创建时暂停使用此方法 。

如果 TweenChain 已经播放, 调用此方法将没有效果 。 如果您想要重新启动链条, 请使用 `TweenChain.restart` 来代替 。

在TweenChain完成后调用这种方法, 将会从头开始链子播放 。


**返回值:** [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) - 此特云钦例.


> 源码：[src/tweens/tween/TweenChain.js#L318](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L318)  
引入版本：3.60.0


---

### remove {#remove}

#### \<instance> remove(tween) {#instance-removetween}


**说明:**

从此 Tween 链中删除给定的 Tween 。

移除的 tween 已_ not_ 销毁。 它刚刚从 Tween 链中移除 。

如果给定的Tween正在播放,则链会自动移动到链中的下一个 tween。如果没有更多的 tween,则此链会完成 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 特温被除去. |


**返回值:** [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) - 这个Tween链的例子。


> 源码：[src/tweens/tween/TweenChain.js#L139](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L139)  
引入版本：3.60.0


---

### reset {#reset}

#### \<instance> reset(tween) {#instance-resettween}


**说明:**

重置给定的图文.

它将寻求定位0,重播将在下一个帧开始.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 复置  文. |


**返回值:** [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) - 此特云钦例.


> 源码：[src/tweens/tween/TweenChain.js#L230](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L230)  
引入版本：3.60.0


---

### resetTweens {#resetTweens}

#### \<instance> resetTweens() {#instance-resettweens}


**说明:**

重新设置所有 Tweens 和当前索引指针的内部方法 。


> 源码：[src/tweens/tween/TweenChain.js#L361](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L361)  
引入版本：3.60.0


---

### restart {#restart}

#### \<instance> restart() {#instance-restart}


**说明:**

复置  川从初.

如果这个 TweenChain 配置为有循环, 或启动延迟, 这些也重置到初始值。 它还会再次发送 `onActive` 调用和事件 。


**返回值:** [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) - 此特云钦例.


> 源码：[src/tweens/tween/TweenChain.js#L197](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L197)  
引入版本：3.60.0


---

### setCurrentTween {#setCurrentTween}

#### \<instance> setCurrentTween(index) {#instance-setcurrenttweenindex}


**说明:**

设定当前活动的Tween 到给定索引,基于其在TweenChain数据阵列中的条目。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 将制时的图文索引. |


> 源码：[src/tweens/tween/TweenChain.js#L495](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L495)  
引入版本：3.60.0


---

### update {#update}

#### \<instance> update(delta) {#instance-updatedelta}


**说明:**

以时间值为基础推进TweenChain的内部方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


**返回值:** boolean - 如果 TweenChain 完成并应该从 Tween 管理器中移除, 返回 `true`, 否则返回 `false` 。


**触发事件:** [Phaser.Tweens.Events#event:TWEEN_COMPLETE](/api/event/tweens-events#tween_complete), [Phaser.Tweens.Events#event:TWEEN_LOOP](/api/event/tweens-events#tween_loop), [Phaser.Tweens.Events#event:TWEEN_START](/api/event/tweens-events#tween_start)


> 源码：[src/tweens/tween/TweenChain.js#L380](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L380)  
引入版本：3.60.0


---

---
