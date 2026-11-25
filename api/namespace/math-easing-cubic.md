# Phaser.Math.Easing.Cubic {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-easing-cubic)

Scope: 
static
> 源码：[src/math/easing/cubic/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/cubic/index.js#L7)  


## 静态函数 {#static-functions}

### In {#In}

#### \<static> In(v) {#static-inv}


**说明:**

立方体易动。 开始缓慢且快速, 沿着立方曲线( v3) , 由此产生一个渐进的开始, 并逐渐形成快速的完成, 使它非常适合动画, 物体应该从休息中收集动力 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟调值,一般在[0, 1] 范围内. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/cubic/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/cubic/In.js#L7)  
引入版本：3.0.0


---

### InOut {#InOut}

#### \<static> InOut(v) {#static-inoutv}


**说明:**

立方体易行/ 出方。 生成一个 S 曲线, 由零加速, 在中点达到最高速度, 然后减速回零。 加速和减速都遵循一个立方体( t3) 曲线, 给予比四极等效的更强的易行性。 通常用于在过渡中间快速移动时平稳开始和结束的动量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟调值,在[0, 1]之间. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/cubic/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/cubic/InOut.js#L7)  
引入版本：3.0.0


---

### Out {#Out}

#### \<static> Out(v) {#static-outv}


**说明:**

立方体易动.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/cubic/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/cubic/Out.js#L7)  
引入版本：3.0.0


---

---
