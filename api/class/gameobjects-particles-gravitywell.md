# GravityWell {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-gravitywell)

重力井粒子处理器对粒子施加一定的力,使其向某一点方向引出或击退它们。

根据牛顿的引力定律,所施加的力与粒子到点的距离的方形成反比.

这模拟了引力在大距离(例如行星之间)的影响.

**构造函数**

`new GravityWell([x], [y], [power], [epsilon], [gravity])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number \| [Phaser.Types.GameObjects.Particles.GravityWellConfig](/api/typedef/types-gameobjects-particles#gravitywellconfig) | 是 | 0 | 引力井的x坐标,在世界空间。 |
| y | number | 是 | 0 | 引力井的Y坐标,在世界空间。 |
| power | number | 是 | 0 | 重力的强度 - 数量较多产生更强大的力. |
| epsilon | number | 是 | 100 | 计算重力的最小距离。 |
| gravity | number | 是 | 50 | 引力力 引力井。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Particles.ParticleProcessor](/api/class/gameobjects-particles-particleprocessor)  



> 源码：[src/gameobjects/particles/GravityWell.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/GravityWell.js#L11)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Particles.ParticleProcessor](/api/class/gameobjects-particles-particleprocessor):**


 - [active](/api/class/gameobjects-particles-particleprocessor#active)
 - [emitter](/api/class/gameobjects-particles-particleprocessor#emitter)
 - [x](/api/class/gameobjects-particles-particleprocessor#x)
 - [y](/api/class/gameobjects-particles-particleprocessor#y)




---

## 公开成员 {#public-members}

### epsilon {#epsilon}

#### epsilon: number {#epsilon-number}


**说明:**

计算重力的最小距离,以像素计。

这在重力计算中使用的距离上起到较低的约束作用,当粒子通过非常接近井的位置时,可以防止极端或无限的力。增加这个值,使效果在近距离上变软。

默认为100。


> 源码：[src/gameobjects/particles/GravityWell.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/GravityWell.js#L132)  
引入版本：3.0.0


---

### gravity {#gravity}

#### gravity: number {#gravity-number}


**说明:**

此重力井的基重力。 这个值会起到一个与 `power` 乘以的刻度, 以确定对粒子的总力。 增加 `gravity` 将放大 `power` 的效果; 设置为 0 将使其中和, 不论 `power` 值如何 。

默认为50。


> 源码：[src/gameobjects/particles/GravityWell.js#L186](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/GravityWell.js#L186)  
引入版本：3.0.0


---

### power {#power}

#### power: number {#power-number}


**说明:**

重力的强度 - 更大的数量产生更强的吸引力力。负值扭转了效果,使颗粒远离井。

内部这个值被`gravity`缩放,所以改变`gravity`也会影响有效力,即使`power`保持不变.

默认为 0 。


> 源码：[src/gameobjects/particles/GravityWell.js#L159](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/GravityWell.js#L159)  
引入版本：3.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.GameObjects.Particles.ParticleProcessor](/api/class/gameobjects-particles-particleprocessor):**


 - [destroy](/api/class/gameobjects-particles-particleprocessor#destroy)




---

## 公开方法 {#public-methods}

### update {#update}

#### \<instance> update(particle, delta, step) {#instance-updateparticle-delta-step}


**说明:**

取一个粒子并基于这个重力井所施加的引力来更新其速度。 力的计算使用粒子与井之间的平方距离, 由 `epsilon` 夹住, 以避免极力在非常近的距离上, 然后应用到粒子的横向和纵向速度组件上。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子要更新。 |
| delta | number | 否 | 三角洲时间以ms计. |
| step | number | 否 | 三角洲值除以1000. |


**Overrides:** Phaser.GameObjects.Particles.ParticleProcessor#更新日期


> 源码：[src/gameobjects/particles/GravityWell.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/GravityWell.js#L95)  
引入版本：3.0.0


---

---
