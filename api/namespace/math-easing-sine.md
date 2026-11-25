# Phaser.Math.Easing.Sine {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-easing-sine)

Scope: 
static
> 源码：[src/math/easing/sine/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/sine/index.js#L7)  


## 静态函数 {#static-functions}

### In {#In}

#### \<static> In(v) {#static-inv}


**说明:**

将一个sinusoid的易入曲线应用到给定值。 运动开始缓慢, 并加速到尾端, 沿着正弦波的形状。 这比其他大多数易入函数产生一个更温和的开始, 使它非常适合像 UI 元素中淡出或者平稳地开始一个摄像机锅这样的微妙动画 。

`v`的输入值应在0到1之间,其中0代表起始值,1代表端点。此范围以外的值不扣。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟放宽的值,一般在0到1之间. |


**返回值:** number - 放宽值,在0到1之间.


> 源码：[src/math/easing/sine/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/sine/In.js#L7)  
引入版本：3.0.0


---

### InOut {#InOut}

#### \<static> InOut(v) {#static-inoutv}


**说明:**

将一个sinusoidal 易入/出到给定值。运动会缓慢地开始,从中点加速,并在结尾处减速到一个站点,产生平滑的 S 曲线过渡。这对动画需要自然的、对称的感,并有温和的始末。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟补间,在[0, 1]之间. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/sine/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/sine/InOut.js#L7)  
引入版本：3.0.0


---

### Out {#Out}

#### \<static> Out(v) {#static-outv}


**说明:**

偏辛松动(sinusoidal easy-out),开始快速移动,并减速到一个温和的停站,沿着正弦波的曲线,在动画和Tweens中常用来平滑减速.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟补间,在[0, 1]之间. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/sine/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/sine/Out.js#L7)  
引入版本：3.0.0


---

---
