# Vector4 {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/math-vector4)

用于3D数学和变换的四元矢量(x,y,z,w).

矢量4通常用于代表3D空间中的均匀坐标,其中 `w` 组件起到缩放系数的作用,使其与4x4矩阵乘法兼容。 `Matrix4`。它也用于代表 RGBA 颜色值、四角体组件,以及需要四个独立分级值的任何其他量。该类支持您所期望的标准矢量操作:加、减、缩、正常化、点产品、线性插值和两种方法的转换。 `Matrix4` 财务报告和已审计财务报表 `Quaternion` 对象。

**构造函数**

`new Vector4([x], [y], [z], [w])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 是 | ×组件. |
| y | number | 是 | y组件. |
| z | number | 是 | z组件. |
| w | number | 是 | 维元件. |

---


**作用域**: static

> 源码：[src/math/Vector4.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L12)  
引入版本：3.0.0

## 公开成员 {#public-members}

### w {#w}

#### w: number {#w-number}


**说明:**

矢量的W成分。


> 源码：[src/math/Vector4.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L69)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

此矢量的x组件.


> 源码：[src/math/Vector4.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L39)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

此矢量的y部分.


> 源码：[src/math/Vector4.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L49)  
引入版本：3.0.0


---

### z {#z}

#### z: number {#z-number}


**说明:**

The z component of this Vector.


> 源码：[src/math/Vector4.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L59)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(v) {#instance-addv}


**说明:**

在此向量中添加一个给定的矢量。 添加是按组件设置的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 向量器来加入这个向量器. |


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 这个矢量4。


> 源码：[src/math/Vector4.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L178)  
引入版本：3.0.0


---

### clone {#clone}

#### \<instance> clone() {#instance-clone}


**说明:**

制作这个矢量4的克隆.


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 一种这个矢量4的克隆体.


> 源码：[src/math/Vector4.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L95)  
引入版本：3.0.0


---

### copy {#copy}

#### \<instance> copy(src) {#instance-copysrc}


**说明:**

将给定的矢量的组件复制到此矢量中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 向量从复制组件。 |


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 这个矢量4。


> 源码：[src/math/Vector4.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L108)  
引入版本：3.0.0


---

### distance {#distance}

#### \<instance> distance(v) {#instance-distancev}


**说明:**

计算此矢量和给定矢量之间的距离 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 计算距离的矢量器。 |


**返回值:** number - 从这个矢量到给定矢量的距离.


> 源码：[src/math/Vector4.js#L394](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L394)  
引入版本：3.0.0


---

### distanceSq {#distanceSq}

#### \<instance> distanceSq(v) {#instance-distancesqv}


**说明:**

计算此矢量和给定矢量之间的距离, 平方 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 计算距离的矢量器。 |


**返回值:** number - 从这个矢量到给定矢量的距离,平方.


> 源码：[src/math/Vector4.js#L414](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L414)  
引入版本：3.0.0


---

### divide {#divide}

#### \<instance> divide(v) {#instance-dividev}


**说明:**

在此矢量和给定矢量之间执行一个组件区分 。

将这个矢量除以给定的矢量。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 矢量器可以将矢量器分割开来 |


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 这个矢量4。


> 源码：[src/math/Vector4.js#L372](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L372)  
引入版本：3.0.0


---

### dot {#dot}

#### \<instance> dot(v) {#instance-dotv}


**说明:**

计算此矢量和给定矢量的点产品 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 矢量4与这个矢量4一起的点产品. |


**返回值:** number - 这个矢量的点产品和给定的矢量.


> 源码：[src/math/Vector4.js#L305](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L305)  
引入版本：3.0.0


---

### equals {#equals}

#### \<instance> equals(v) {#instance-equalsv}


**说明:**

检查此矢量是否等同于给定矢量 。

对每个矢量的成分进行严格的平等检查.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 检查平等的向量 。 |


**返回值:** boolean - 布尔表示两种矢量是否相等。


> 源码：[src/math/Vector4.js#L128](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L128)  
引入版本：3.0.0


---

### length {#length}

#### \<instance> length() {#instance-length}


**说明:**

计算此矢量的长度( 或大小 ) 。


**返回值:** number - 此矢量之长短.


> 源码：[src/math/Vector4.js#L238](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L238)  
引入版本：3.0.0


---

### lengthSq {#lengthSq}

#### \<instance> lengthSq() {#instance-lengthsq}


**说明:**

计算这个矢量平方的长度 。


**返回值:** number - 这个矢量的长度,平方


> 源码：[src/math/Vector4.js#L256](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L256)  
引入版本：3.0.0


---

### lerp {#lerp}

#### \<instance> lerp(v, [t]) {#instance-lerpv-t}


**说明:**

线性插图介于这个矢量和给定矢量之间.

将这个矢量向给定矢量进发.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 |  | 向内插插管4号 |
| t | number | 是 | 0 | 插值百分比,介于0到1之间. |


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 这个矢量4。


> 源码：[src/math/Vector4.js#L320](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L320)  
引入版本：3.0.0


---

### multiply {#multiply}

#### \<instance> multiply(v) {#instance-multiplyv}


**说明:**

在此矢量和给定矢量之间执行一个组件乘法 。

以给定的矢量乘以这个矢量.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 向量器可以乘以这个向量器. |


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 这个矢量4。


> 源码：[src/math/Vector4.js#L350](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L350)  
引入版本：3.0.0


---

### negate {#negate}

#### \<instance> negate() {#instance-negate}


**说明:**

忽略 `x`, `y`, `z` 财务报告和已审计财务报表 `w` 的组件。


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 这个矢量4。


> 源码：[src/math/Vector4.js#L434](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L434)  
引入版本：3.0.0


---

### normalize {#normalize}

#### \<instance> normalize() {#instance-normalize}


**说明:**

使这个矢量正常化.

使矢量成为同一方向的单位长度矢量(放大度为1).


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 这个矢量4。


> 源码：[src/math/Vector4.js#L274](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L274)  
引入版本：3.0.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

使这个矢量为零向量( 0, 0, 0, 0) 。


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 这个矢量4。


> 源码：[src/math/Vector4.js#L512](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L512)  
引入版本：3.0.0


---

### scale {#scale}

#### \<instance> scale(scale) {#instance-scalescale}


**说明:**

按给定的值对这个矢量进行缩放 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scale | number | 否 | 以何值缩放此矢量 。 |


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 这个矢量4。


> 源码：[src/math/Vector4.js#L218](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L218)  
引入版本：3.0.0


---

### set {#set}

#### \<instance> set(x, y, z, w) {#instance-setx-y-z-w}


**说明:**

设定 `x`, `y`, `z` 财务报告和已审计财务报表 `w` 中,将“矢量”的组件切换到“给定”的组件 `x`, `y`, `z` 财务报告和已审计财务报表 `w` 价值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number \| object | 否 | 用于此矢量的x值,或包含x,y,z和w组件的对象. |
| y | number | 否 | 此矢量的 Y 值设置 。 |
| z | number | 否 | 用于此矢量的 Z 值 。 |
| w | number | 否 | 此矢量的w值设置 。 |


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 这个矢量4。


> 源码：[src/math/Vector4.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L145)  
引入版本：3.0.0


---

### subtract {#subtract}

#### \<instance> subtract(v) {#instance-subtractv}


**说明:**

从此矢量中减去给定的矢量。 减法是按组件进行 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 向量从这个向量中减掉。 |


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 这个矢量4。


> 源码：[src/math/Vector4.js#L198](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L198)  
引入版本：3.0.0


---

### transformMat4 {#transformMat4}

#### \<instance> transformMat4(mat) {#instance-transformmat4mat}


**说明:**

以给定的矩阵来改变这个矢量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mat | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 将这个矢量4 转换成的矩阵 4 。 |


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 这个矢量4。


> 源码：[src/math/Vector4.js#L452](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L452)  
引入版本：3.0.0


---

### transformQuat {#transformQuat}

#### \<instance> transformQuat(q) {#instance-transformquatq}


**说明:**

用给定的Quaternion 来改变这个矢量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| q | [Phaser.Math.Quaternion](/api/class/math-quaternion) | 否 | Quaternion用来改变这个矢量的。 |


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 这个矢量4。


> 源码：[src/math/Vector4.js#L478](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector4.js#L478)  
引入版本：3.0.0


---

---
