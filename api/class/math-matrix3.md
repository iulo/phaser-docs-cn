# Matrix3 {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/math-matrix3)

3x3 列主矩阵作为浮点32 的矩阵存储, 数值为 9 。 用于 2D 的离子转换, 提取矩阵4 的左上方部分 3x3 , 并计算正常矩阵的照明计算 。 数值按列主排列, 以匹配 WebGL 常规 。

即时状态时默认身份矩阵 。

**构造函数**

`new Matrix3([m])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| m | [Phaser.Math.Matrix3](/api/class/math-matrix3) | 是 | 可选矩阵3 复制值。 |

---


**作用域**: static

> 源码：[src/math/Matrix3.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L12)  
引入版本：3.0.0

## 公开成员 {#public-members}

### val {#val}

#### val: Float32Array {#val-float32array}


**说明:**

矩阵值。


> 源码：[src/math/Matrix3.js#L34](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L34)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### adjoint {#adjoint}

#### \<instance> adjoint() {#instance-adjoint}


**说明:**

计算这个矩阵的连带或附加物。


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 这个矩阵3。


> 源码：[src/math/Matrix3.js#L268](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L268)  
引入版本：3.0.0


---

### clone {#clone}

#### \<instance> clone() {#instance-clone}


**说明:**

制造这个矩阵3的克隆.


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 这个矩阵3的克隆体.


> 源码：[src/math/Matrix3.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L55)  
引入版本：3.0.0


---

### copy {#copy}

#### \<instance> copy(src) {#instance-copysrc}


**说明:**

将给定矩阵的值复制到此矩阵中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Math.Matrix3](/api/class/math-matrix3) | 否 | 复制值的矩阵 。 |


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 这个矩阵3。


> 源码：[src/math/Matrix3.js#L83](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L83)  
引入版本：3.0.0


---

### determinant {#determinant}

#### \<instance> determinant() {#instance-determinant}


**说明:**

计算这个矩阵的决定因素 。


**返回值:** number - 母体的决定因素。


> 源码：[src/math/Matrix3.js#L303](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L303)  
引入版本：3.0.0


---

### fromArray {#fromArray}

#### \<instance> fromArray(a) {#instance-fromarraya}


**说明:**

从给定的数组中设定此矩阵的值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | array | 否 | 复制数值的数组 。 |


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 这个矩阵3。


> 源码：[src/math/Matrix3.js#L141](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L141)  
引入版本：3.0.0


---

### fromMat4 {#fromMat4}

#### \<instance> fromMat4(m) {#instance-frommat4m}


**说明:**

将矩阵4的左上方3x3值复制到这个矩阵3, 丢弃第四行和列。 当您需要转换矩阵的旋转和比例部分而无需其翻译组件时, 这样做是有用的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| m | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 复制数值的矩阵 4。 |


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 这个矩阵3。


> 源码：[src/math/Matrix3.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L111)  
引入版本：3.0.0


---

### fromQuat {#fromQuat}

#### \<instance> fromQuat(q) {#instance-fromquatq}


**说明:**

从给定的 Quaternion 中设置此矩阵的值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| q | [Phaser.Math.Quaternion](/api/class/math-quaternion) | 否 | 用于设定这个矩阵的值的 Quaternion 。 |


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 这个矩阵3。


> 源码：[src/math/Matrix3.js#L466](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L466)  
引入版本：3.0.0


---

### identity {#identity}

#### \<instance> identity() {#instance-identity}


**说明:**

将这个矩阵重置为身份( 默认) 矩阵 。


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 这个矩阵3。


> 源码：[src/math/Matrix3.js#L168](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L168)  
引入版本：3.0.0


---

### invert {#invert}

#### \<instance> invert() {#instance-invert}


**说明:**

反转此矩阵。 如果矩阵不是不可逆的, 返回 `null`( 即它的决定因素为 0) 。


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 如果矩阵不能反转, 则使用此矩阵 3, 或 `null` 。


> 源码：[src/math/Matrix3.js#L218](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L218)  
引入版本：3.0.0


---

### multiply {#multiply}

#### \<instance> multiply(src) {#instance-multiplysrc}


**说明:**

以给定的矩阵乘以这个矩阵.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Math.Matrix3](/api/class/math-matrix3) | 否 | 将这个矩阵乘以矩阵。 |


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 这个矩阵3。


> 源码：[src/math/Matrix3.js#L328](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L328)  
引入版本：3.0.0


---

### normalFromMat4 {#normalFromMat4}

#### \<instance> normalFromMat4(m) {#instance-normalfrommat4m}


**说明:**

从给定矩阵中衍生出一个正常矩阵4. 正常矩阵是矩阵4反向的转录,在应用非统一缩放时用于照明计算以正确转换表面正常. 如果矩阵4不是不可逆的,返回`null`(即其决定因素为0).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| m | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 矩阵4从中得出正常矩阵. |


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 如果矩阵4不能反转,则使用这个矩阵3,或`null`.


> 源码：[src/math/Matrix3.js#L516](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L516)  
引入版本：3.0.0


---

### rotate {#rotate}

#### \<instance> rotate(rad) {#instance-rotaterad}


**说明:**

将旋转转换应用到此矩阵中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rad | number | 否 | 弧度的角度来旋转. |


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 这个矩阵3。


> 源码：[src/math/Matrix3.js#L402](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L402)  
引入版本：3.0.0


---

### scale {#scale}

#### \<instance> scale(v) {#instance-scalev}


**说明:**

将比例转换应用到此矩阵中 。

使用给定矢量的`x`和`y`组件来放大矩阵.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 矢量器可以放大这个矩阵。 |


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 这个矩阵3。


> 源码：[src/math/Matrix3.js#L437](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L437)  
引入版本：3.0.0


---

### set {#set}

#### \<instance> set(src) {#instance-setsrc}


**说明:**

此方法为`Matrix3.copy`的别名.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Math.Matrix3](/api/class/math-matrix3) | 否 | 设置此矩阵值的矩阵 。 |


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 这个矩阵3。


> 源码：[src/math/Matrix3.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L68)  
引入版本：3.0.0


---

### translate {#translate}

#### \<instance> translate(v) {#instance-translatev}


**说明:**

用给定的矢量来翻译这个矩阵 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 矢量者,用这个矩阵来翻译. |


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 这个矩阵3。


> 源码：[src/math/Matrix3.js#L379](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L379)  
引入版本：3.0.0


---

### transpose {#transpose}

#### \<instance> transpose() {#instance-transpose}


**说明:**

转录这个矩阵。


**返回值:** [Phaser.Math.Matrix3](/api/class/math-matrix3) - 这个矩阵3。


> 源码：[src/math/Matrix3.js#L193](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix3.js#L193)  
引入版本：3.0.0


---

---
