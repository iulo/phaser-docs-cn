# Phaser.GameObjects.Components.ElapseTimer {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-elapsetimer)

Scope: 
static
> 源码：[src/gameobjects/components/ElapseTimer.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ElapseTimer.js#L7)  
引入版本：4.0.0

## 静态函数 {#static-functions}

### timeElapsed {#timeElapsed}

#### timeElapsed: number {#timeelapsed-number}


**说明:**

时间器初始化后的时间, 以毫秒计。


> 源码：[src/gameobjects/components/ElapseTimer.js#L41](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ElapseTimer.js#L41)  
引入版本：4.0.0


---

### timeElapsedResetPeriod {#timeElapsedResetPeriod}

#### timeElapsedResetPeriod: number {#timeelapsedresetperiod-number}


**说明:**

`timeElapsed` 重置后的时间, 以毫秒计。 默认为 1小时。 如果您使用动画定时器, 您可以设定为一个与动画持续时间相匹配的时期 。

这对于定时器避免着色器中的浮点精度问题是必要的. 浮点32可以精确地表示几小时毫秒,但精度会随着值的增加而降低.


> 源码：[src/gameobjects/components/ElapseTimer.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ElapseTimer.js#L50)  
引入版本：4.0.0


---

### timePaused {#timePaused}

#### timePaused: boolean {#timepaused-boolean}


**说明:**

是否暂停了 。


> 源码：[src/gameobjects/components/ElapseTimer.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ElapseTimer.js#L68)  
引入版本：4.0.0


---

## 静态函数 {#static-functions-1}

### resetTimer {#resetTimer}

#### \<instance> resetTimer([ms]) {#instance-resettimerms}


**说明:**

重置此游戏对象的 lapse 定时器 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| ms | number | 是 | 0 | 重设定时器的时间, 以毫秒计 。 |


**返回值:** [Phaser.GameObjects.Components.ElapseTimer](/api/namespace/gameobjects-components-elapsetimer) - 此游戏对象.


> 源码：[src/gameobjects/components/ElapseTimer.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ElapseTimer.js#L108)  
引入版本：4.0.0


---

### setTimerPaused {#setTimerPaused}

#### \<instance> setTimerPaused([paused]) {#instance-settimerpausedpaused}


**说明:**

暂停或恢复此游戏对象的延时计时器。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| paused | boolean | 是 | 暂停状态( `true` 暂停状态, `false` 暂停状态) 。 如果没有指定, 定时器将停止状态 。 |


**返回值:** [Phaser.GameObjects.Components.ElapseTimer](/api/namespace/gameobjects-components-elapsetimer) - 此游戏对象.


> 源码：[src/gameobjects/components/ElapseTimer.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ElapseTimer.js#L93)  
引入版本：4.0.0


---

### setTimerResetPeriod {#setTimerResetPeriod}

#### \<instance> setTimerResetPeriod(period) {#instance-settimerresetperiodperiod}


**说明:**

设定此游戏对象的 Lapse 定时器的重置期 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| period | number | 否 | `timeElapsed`重置后的时间,以毫秒计. |


**返回值:** [Phaser.GameObjects.Components.ElapseTimer](/api/namespace/gameobjects-components-elapsetimer) - 此游戏对象.


> 源码：[src/gameobjects/components/ElapseTimer.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ElapseTimer.js#L78)  
引入版本：4.0.0


---

### updateTimer {#updateTimer}

#### \<instance> updateTimer(time, delta) {#instance-updatetimertime-delta}


**说明:**

更新此游戏对象的 lapse 定时器。 这应该自动使用 preUpdate 方法调用 。

覆盖此方法创建更高级的时间管理, 或者设置为 NOOP 函数来禁用定时器更新。 如果您想要使用 tween 或输入系统控制动画, 则禁用定时器的更新可能有用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 以毫秒计的当前时间 。 |
| delta | number | 否 | 上次更新以来的几秒钟 |


**返回值:** [Phaser.GameObjects.Components.ElapseTimer](/api/namespace/gameobjects-components-elapsetimer) - 此游戏对象.


> 源码：[src/gameobjects/components/ElapseTimer.js#L124](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ElapseTimer.js#L124)  
引入版本：4.0.0


---

---
