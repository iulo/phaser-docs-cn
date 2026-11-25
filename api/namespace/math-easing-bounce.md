# Phaser.Math.Easing.Bounce {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-easing-bounce)

Scope: 
static
> 源码：[src/math/easing/bounce/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/bounce/index.js#L7)  


## 静态函数 {#static-functions}

### In {#In}

#### \<static> In(v) {#static-inv}


**说明:**

将弹跳放松应用到 tween 的开始。 弹跳值会在加速向目标移动之前在源头附近“ 弹跳” 几次, 模拟球弹跳在开始移动时的效果。 这就是弹跳效果的易变体, 意思是弹跳效果发生在过渡开始时而不是结束。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟放宽的值,在0到1之间. |


**返回值:** number - 放宽值,在0到1之间.


> 源码：[src/math/easing/bounce/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/bounce/In.js#L7)  
引入版本：3.0.0


---

### InOut {#InOut}

#### \<static> InOut(v) {#static-inoutv}


**说明:**

对给定值应用弹跳易/出效果。这结合了弹跳易/出易效果,在  的始末产生弹跳动画。输入值应在0到1之间,其中0为起始值,1为尾值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/bounce/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/bounce/InOut.js#L7)  
引入版本：3.0.0


---

### Out {#Out}

#### \<static> Out(v) {#static-outv}


**说明:**

将弹出易控效果应用到给定值。 运动会快速启动, 并减速到尾端, 产生弹出效果, 模拟一个球落地, 弹出到停点。 弹出是通过四个片面的四极区段实现的, 它们在沉淀前产生三个递减弹出。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/bounce/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/bounce/Out.js#L7)  
引入版本：3.0.0


---

---
