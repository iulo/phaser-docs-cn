# Phaser.Math.Easing.Quintic {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-easing-quintic)

Scope: 
static
> 源码：[src/math/easing/quintic/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quintic/index.js#L7)  


## 静态函数 {#static-functions}

### In {#In}

#### \<static> In(v) {#static-inv}


**说明:**

将一个五进制易入曲线应用到给定值。 该值开始变化非常缓慢, 并急剧加速到最后, 沿着第五功率( v^5) 曲线。 这比立方或夸式易入函数产生更显著的加速效果, 使其适合动画, 需要以近零速度开始, 快速快速地累积到全速 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/quintic/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quintic/In.js#L7)  
引入版本：3.0.0


---

### InOut {#InOut}

#### \<static> InOut(v) {#static-inoutv}


**说明:**

将一个昆曲易入/出函数应用到给定值中。运动开始缓慢,从中点快速加速,然后减速回慢。与立方或夸张的放松相比,五进制曲线(提升到第五强)产生更戏剧性的加速和减速,使其非常适合需要强健的,拳头的感觉,并有平稳的起始和结束的过渡。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟补间,在[0, 1]之间. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/quintic/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quintic/InOut.js#L7)  
引入版本：3.0.0


---

### Out {#Out}

#### \<static> Out(v) {#static-outv}


**说明:**

昆曲轻松出炉.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/quintic/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quintic/Out.js#L7)  
引入版本：3.0.0


---

---
