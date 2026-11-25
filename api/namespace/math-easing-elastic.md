# Phaser.Math.Easing.Elastic {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-easing-elastic)

Scope: 
static
> 源码：[src/math/easing/elastic/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/elastic/index.js#L7)  


## 静态函数 {#static-functions}

### In {#In}

#### \<static> In(v, [amplitude], [period]) {#static-inv-amplitude-period}


**说明:**

弹性易感,在加速向目标前进之前,值会以弹簧般的运动回旋而行。效果始于一系列小振荡,其规模在扩大,模拟伸缩的弹性带被释放。当您想要在启动时先让一个扭矩感觉春或跳动时,就使用这个功能。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | number | 否 |  | 拟放宽的值,在0到1之间. |
| amplitude | number | 是 | 0.1 | 弹性振荡的振荡度,1以下值被夹到1. 较高的值产生一个更宽的振荡弧. |
| period | number | 是 | 0.1 | 控制正弦波振荡的紧度。 数值越小, 周期就越紧, 周期就越频繁; 数值越大, 波动就越慢。 |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/elastic/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/elastic/In.js#L7)  
引入版本：3.0.0


---

### InOut {#InOut}

#### \<static> InOut(v, [amplitude], [period]) {#static-inoutv-amplitude-period}


**说明:**

弹性易感/ 出动, 既结合易感和易感的易感效果。 这种易感功能在  的始末都会产生弹簧般的振荡, 在安顿前过度射入目标值。 对于需要两端的振荡感的动画来说, 很有用 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | number | 否 |  | 拟补间,一般在[0, 1] 范围内. |
| amplitude | number | 是 | 0.1 | 弹性振荡的振幅,1以下值被夹到1. |
| period | number | 是 | 0.1 | 控制正弦波振荡的紧度。 较小的值会产生周期较多的更紧的波 。 |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/elastic/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/elastic/InOut.js#L7)  
引入版本：3.0.0


---

### Out {#Out}

#### \<static> Out(v, [amplitude], [period]) {#static-outv-amplitude-period}


**说明:**

弹性易变,值在最后值落定前会以衰变正弦波向目标过度射击,振荡。弹性效应发生在过渡结束时,使运动看起来会弹跳或弹簧到位。接受一个在0到1之间的正常输入值`v`。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | number | 否 |  | 通常在[0, 1] 范围内的常态值要加加成的值. |
| amplitude | number | 是 | 0.1 | 弹性射线的振幅。 1 以上的值会增加射线的大小 。 |
| period | number | 是 | 0.1 | 控制正弦波振荡的强度。 数值较小, 产生更快速振荡的更紧的波 。 |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/elastic/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/elastic/Out.js#L7)  
引入版本：3.0.0


---

---
