# Phaser.Math.Easing.Quartic {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-easing-quartic)

Scope: 
static
> 源码：[src/math/easing/quartic/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quartic/index.js#L7)  


## 静态函数 {#static-functions}

### In {#In}

#### \<static> In(v) {#static-inv}


**说明:**

夸文易入.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/quartic/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quartic/In.js#L7)  
引入版本：3.0.0


---

### InOut {#InOut}

#### \<static> InOut(v) {#static-inoutv}


**说明:**

Quartic 易入/ 出。 应用一个自始至终快速加速的夸尔曲线( 第四力) , 然后急剧减速, 进入尾端。 运动是对称的: 上半半边反射易入, 后半边反射易出。 这比四极或立方宽松更能产生戏剧性的加速和减速, 使其适合快速的高能过渡 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟调值,在[0, 1]之间. |


**返回值:** number - 易值,在[0, 1] 范围内.


> 源码：[src/math/easing/quartic/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quartic/InOut.js#L7)  
引入版本：3.0.0


---

### Out {#Out}

#### \<static> Out(v) {#static-outv}


**说明:**

夸奇式轻松出局.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/quartic/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/quartic/Out.js#L7)  
引入版本：3.0.0


---

---
