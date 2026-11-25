# Phaser.Math.Easing.Back {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-easing-back)

Scope: 
static
> 源码：[src/math/easing/back/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/back/index.js#L7)  


## 静态函数 {#static-functions}

### In {#In}

#### \<static> In(v, [overshoot]) {#static-inv-overshoot}


**说明:**

后放。 放松功能在前进前会向相反方向短暂拉回, 在过渡开始时会产生预期效果, 启动后`overshoot`值越高, 值拉越后, 开始前会越低 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | number | 否 |  | 平时的平时值为0到1。 |
| overshoot | number | 是 | 1.70158 | 超射量。 控制值在前进前的后退。 更高的值会产生更明显的后退效果 。 |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/back/In.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/back/In.js#L7)  
引入版本：3.0.0


---

### InOut {#InOut}

#### \<static> InOut(v, [overshoot]) {#static-inoutv-overshoot}


**说明:**

后易/出。 此放松功能对双曲的起始和结尾都应用了后退效果: 值在加速前进前先稍回拉, 然后在扣回休息前过度射入目标, 产生对称的弹簧般运动。 如果您想要动画两端的活泼的, 跳动的感觉, 请使用此功能 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | number | 否 |  | 拟解之值. |
| overshoot | number | 是 | 1.70158 | 控制拉回和射出过度的大小。 值较高会产生更显著的效果。 默认在每一端产生大约10%的射出过度 。 |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/back/InOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/back/InOut.js#L7)  
引入版本：3.0.0


---

### Out {#Out}

#### \<static> Out(v, [overshoot]) {#static-outv-overshoot}


**说明:**

后放轻松。 双关先快速移动, 然后在返回目标之前超标其最终值。 超标发生在过渡结束时, 给出一个轻微的“ 弹出过去和返回” 效果 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | number | 否 |  | 拟调值,一般在[0, 1] 范围内. |
| overshoot | number | 是 | 1.70158 | 超射量 值较高会导致超射率更明显 |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/back/Out.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/back/Out.js#L7)  
引入版本：3.0.0


---

---
