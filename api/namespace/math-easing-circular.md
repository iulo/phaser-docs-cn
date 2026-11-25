# Phaser.Math.Easing.Circular {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-easing-circular)

Scope: 
static
> 源码：[src/math/easing/circular/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/circular/index.js#L7)  


## 静态函数 {#static-functions}

### In {#In}

#### \<static> In(v) {#static-inv}


**说明:**

应用一个循环易入值。 这种易入值是基于一个圆的方程, 生成一个开始非常缓慢, 然后急剧加速到尾端的曲线。 它是`Circular.Out`的补充, 通常用于动画, 在启动前需要犹豫的开始 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/circular/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/circular/In.js#L7)  
引入版本：3.0.0


---

### InOut {#InOut}

#### \<static> InOut(v) {#static-inoutv}


**说明:**

循环易行/出局. 应用一个循环宽松曲线,开始缓慢,通过中点加速,然后减速到平稳的停站. 曲线的形状从一个圆弧的弧形推导出来,产生一种自然易行运动,比正弦易行更渐进,但比四极易行更尖锐. 结合易行和易行使过渡对称性:前半段易行使用圆弧,后半段易行使用镜弧.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟补间,在[0, 1]之间. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/circular/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/circular/InOut.js#L7)  
引入版本：3.0.0


---

### Out {#Out}

#### \<static> Out(v) {#static-outv}


**说明:**

以单位圆的方程为基础,对`v`应用循环宽松效应,运动以全速开始,并顺着四分之一圆的曲线顺利减速到一站. `v`应该介于0到1之间.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟放宽的值,在0到1之间. |


**返回值:** number - 放宽值,在0到1之间.


> 源码：[src/math/easing/circular/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/circular/Out.js#L7)  
引入版本：3.0.0


---

---
