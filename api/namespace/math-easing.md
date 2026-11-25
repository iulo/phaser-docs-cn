# Phaser.Math.Easing {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-easing)

Scope: 
static
> 源码：[src/math/easing/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/index.js#L7)  


## 静态函数 {#static-functions}

- [Back](/api/namespace/math-easing-back)
- [Bounce](/api/namespace/math-easing-bounce)
- [Circular](/api/namespace/math-easing-circular)
- [Cubic](/api/namespace/math-easing-cubic)
- [Elastic](/api/namespace/math-easing-elastic)
- [Expo](/api/namespace/math-easing-expo)
- [Quadratic](/api/namespace/math-easing-quadratic)
- [Quartic](/api/namespace/math-easing-quartic)
- [Quintic](/api/namespace/math-easing-quintic)
- [Sine](/api/namespace/math-easing-sine)
- [Stepped](/api/namespace/math-easing-stepped)
## 静态函数 {#static-functions-1}

### Linear {#Linear}

#### \<static> Linear(v) {#static-linearv}


**说明:**

线性宽松(无变异).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | number | 否 | 拟解之值. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/linear/Linear.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/linear/Linear.js#L7)  
引入版本：3.0.0


---

### Stepped {#Stepped}

#### \<static> Stepped(v, [steps]) {#static-steppedv-steps}


**说明:**

将输入值量化为若干个零散的平方步的自动放松函数,从而形成阶梯式进程而不是平方曲线。输出在步数之间立即跳动,而不是插值,这对逐帧动画、网格扭曲移动或任何应明显递增的效果都有益。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | number | 否 |  | 拟解之值. |
| steps | number | 是 | 1 | 方便中步数. |


**返回值:** number - 解脱之值.


> 源码：[src/math/easing/stepped/Stepped.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/easing/stepped/Stepped.js#L7)  
引入版本：3.0.0


---

---
