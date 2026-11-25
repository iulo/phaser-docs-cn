# Tweens {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/constant/tweens)

### CREATED {#CREATED}

#### CREATED: number {#created-number}


**说明:**

TweenData状态. TweenData 已经创建,但尚未开始处理.


> 源码：[src/tweens/tween/const.js#L25](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L25)  
引入版本：3.0.0


### DELAY {#DELAY}

#### DELAY: number {#delay-number}


**说明:**

TweenData状态。 TweenData 正在等待它开始播放前的初始延迟 。


> 源码：[src/tweens/tween/const.js#L37](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L37)  
引入版本：3.0.0


### PENDING_RENDER {#PENDING_RENDER}

#### PENDING_RENDER: number {#pending_render-number}


**说明:**

TweenData状态。 TweenData 正在等待它的目标游戏对象在开始播放前被渲染出来 。


> 源码：[src/tweens/tween/const.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L49)  
引入版本：3.0.0


### PLAYING_FORWARD {#PLAYING_FORWARD}

#### PLAYING_FORWARD: number {#playing_forward-number}


**说明:**

TweenData状态。 TweenData 正在积极向前进方向插入其属性, 从起始值到结束值 。


> 源码：[src/tweens/tween/const.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L59)  
引入版本：3.0.0


### PLAYING_BACKWARD {#PLAYING_BACKWARD}

#### PLAYING_BACKWARD: number {#playing_backward-number}


**说明:**

TweenData状态。 TweenData 正在积极向后方向插入其属性, 从端值返回到起始值 。


> 源码：[src/tweens/tween/const.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L69)  
引入版本：3.0.0


### HOLD_DELAY {#HOLD_DELAY}

#### HOLD_DELAY: number {#hold_delay-number}


**说明:**

TweenData状态。 TweenData 已达到其最终值, 并等待延迟结束, 然后再逆转或重复 。


> 源码：[src/tweens/tween/const.js#L79](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L79)  
引入版本：3.0.0


### REPEAT_DELAY {#REPEAT_DELAY}

#### REPEAT_DELAY: number {#repeat_delay-number}


**说明:**

TweenData状态。 TweenData 已完成播放, 等待重复延迟结束, 然后再开始下一次重复 。


> 源码：[src/tweens/tween/const.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L89)  
引入版本：3.0.0


### COMPLETE {#COMPLETE}

#### COMPLETE: number {#complete-number}


**说明:**

TweenData状态. TweenData 已完成全部重复,其回放完成.


> 源码：[src/tweens/tween/const.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L99)  
引入版本：3.0.0


### PENDING {#PENDING}

#### PENDING: number {#pending-number}


**说明:**

州,  州已创,但尚未加为  州管理.


> 源码：[src/tweens/tween/const.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L111)  
引入版本：3.0.0


### ACTIVE {#ACTIVE}

#### ACTIVE: number {#active-number}


**说明:**

Tween 状态。 Tween 正在 Tween 管理器内部活动。 这意味着它要么正在播放,要么正在播放, 并且目前暂停, 但是在这两种情况下, 它仍然在 Tween 管理机的处理中, 所以被认为是“ 活动 ” 。


> 源码：[src/tweens/tween/const.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L121)  
引入版本：3.0.0


### LOOP_DELAY {#LOOP_DELAY}

#### LOOP_DELAY: number {#loop_delay-number}


**说明:**

州,  州等环数降,以示灭亡.


> 源码：[src/tweens/tween/const.js#L133](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L133)  
引入版本：3.0.0


### COMPLETE_DELAY {#COMPLETE_DELAY}

#### COMPLETE_DELAY: number {#complete_delay-number}


**说明:**

州,  州刺史  等完全拖延,  州刺史  .


> 源码：[src/tweens/tween/const.js#L143](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L143)  
引入版本：3.0.0


### START_DELAY {#START_DELAY}

#### START_DELAY: number {#start_delay-number}


**说明:**

州,  州刺史  等起事延缓,以  .


> 源码：[src/tweens/tween/const.js#L153](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L153)  
引入版本：3.0.0


### PENDING_REMOVE {#PENDING_REMOVE}

#### PENDING_REMOVE: number {#pending_remove-number}


**说明:**

州,  州已完回放,正待除  州管理.


> 源码：[src/tweens/tween/const.js#L163](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L163)  
引入版本：3.0.0


### REMOVED {#REMOVED}

#### REMOVED: number {#removed-number}


**说明:**

州,  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  州刺史  的  等.


> 源码：[src/tweens/tween/const.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L173)  
引入版本：3.0.0


### FINISHED {#FINISHED}

#### FINISHED: number {#finished-number}


**说明:**

Tween 状态。 Tween 已完成播放, 但创建时被标记为“ 持久性 ” , 因此不会被 Tween 管理器自动删除 。


> 源码：[src/tweens/tween/const.js#L183](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L183)  
引入版本：3.60.0


### DESTROYED {#DESTROYED}

#### DESTROYED: number {#destroyed-number}


**说明:**

州,  州已毁,不能再由  州经理出演.


> 源码：[src/tweens/tween/const.js#L194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L194)  
引入版本：3.60.0


### MAX {#MAX}

#### MAX: number {#max-number}


**说明:**

用于“ 无限” 样式倒计时的大型整数值 。

和数字.MAQXSAFE_INTEGER类似,但我们不能使用,因为它在IE上没有支持.


> 源码：[src/tweens/tween/const.js#L204](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/const.js#L204)  
引入版本：3.60.0

---
