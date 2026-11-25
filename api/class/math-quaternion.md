# Quaternion {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/math-quaternion)

代表3D空间旋转的四元. Quaternion 避免了    锁,并在方向之间提供平滑的插值. equernion 被存储为四个组件(x, y, z, w). 使用 `identity`方法重置为身份之四(0, 0, 0, 1), 表示不旋转. 通常与 Matrix4 一起用于 WebGL渲染中的3D 转换.

**构造函数**

`new Quaternion([x], [y], [z], [w])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | ×组件. |
| y | number | 是 | 0 | y组件. |
| z | number | 是 | 0 | z组件. |
| w | number | 是 | 1 | 维元件. |

---


**作用域**: static

> 源码：[src/math/Quaternion.js#L27](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L27)  
引入版本：3.0.0

## 公开成员 {#public-members}

### onChangeCallback {#onChangeCallback}

#### onChangeCallback: function {#onchangecallback-function}


**说明:**

如果设置, 则每次更改此四角星中的值时都会引用此回调。 调用通过一个参数, 引用此四角星 。


> 源码：[src/math/Quaternion.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L91)  
引入版本：3.50.0


---

### w {#w}

#### w: number {#w-number}


**说明:**

这个Quaternion的w部分.


> 源码：[src/math/Quaternion.js#L170](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L170)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

此Quaternion的x组件.


> 源码：[src/math/Quaternion.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L104)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

Quaternion的y部分, 用于计算 。


> 源码：[src/math/Quaternion.js#L126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L126)  
引入版本：3.0.0


---

### z {#z}

#### z: number {#z-number}


**说明:**

The z component of this Quaternion.


> 源码：[src/math/Quaternion.js#L148](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L148)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(v) {#instance-addv}


**说明:**

在此 Quaternion 中添加一个给定的 Quaternion 或 矢量。 添加是按组件设置的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Quaternion](/api/class/math-quaternion) \| [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 夸特尼翁或矢量加此夸特尼翁. |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L248](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L248)  
引入版本：3.0.0


---

### calculateW {#calculateW}

#### \<instance> calculateW() {#instance-calculatew}


**说明:**

基于当前 x, y, 和 z 组件计算和设置此 Quaternion 的 w 组件, 使 Quaternion 有单位长度。 假设 x, y,和 z 值已经知道, 并且它们的总平方长度不超过 1 。


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L779](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L779)  
引入版本：3.0.0


---

### conjugate {#conjugate}

#### \<instance> conjugate() {#instance-conjugate}


**说明:**

将这个 Quaternion 转换为它的集合,方法是在不改变 w 时将 x、 y 和 z 组件忽略。对于单位之四, 集合等于反转, 并代表相反的旋转 。


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L668](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L668)  
引入版本：3.0.0


---

### copy {#copy}

#### \<instance> copy(src) {#instance-copysrc}


**说明:**

将给定的 Quaternion 或矢量 的组件复制到此 Quaternion 中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Math.Quaternion](/api/class/math-quaternion) \| [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | Quaternion 或 矢量 复制组件从 。 |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L192)  
引入版本：3.0.0


---

### dot {#dot}

#### \<instance> dot(v) {#instance-dotv}


**说明:**

计算此 Quaternion 和 Quaternion 或 矢量 的点产物 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Quaternion](/api/class/math-quaternion) \| [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | Quaternion或矢量与这个Quaternion一起生产点点产品. |


**返回值:** number - 这个Quaternion的点产物和给定的Quaternion或矢量.


> 源码：[src/math/Quaternion.js#L382](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L382)  
引入版本：3.0.0


---

### fromMat3 {#fromMat3}

#### \<instance> fromMat3(mat) {#instance-frommat3mat}


**说明:**

设定此 Quaternion 从给定矩阵3 代表的旋转中选择,使用 Ken Shoemake 1987 年 SIGGRAPH 文章"Quaternion Calculus and Fast Animation"中的算法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mat | [Phaser.Math.Matrix3](/api/class/math-matrix3) | 否 | 将转换为矩阵3。 |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L986](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L986)  
引入版本：3.0.0


---

### identity {#identity}

#### \<instance> identity() {#instance-identity}


**说明:**

将此 Quaternion 重置为身份之四( 0, 0, 0, 1), 表示不旋转 。


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L504](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L504)  
引入版本：3.0.0


---

### invert {#invert}

#### \<instance> invert() {#instance-invert}


**说明:**

计算此Quaternion 的乘法反向并设定结果。 反向取消该Quaternion 所代表的旋转。 如果Quaternion 长度为零, 则不作更改 。


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L640](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L640)  
引入版本：3.0.0


---

### length {#length}

#### \<instance> length() {#instance-length}


**说明:**

计算此 Quaternion 的长度 。


**返回值:** number - 此盖特尼翁之长短.


> 源码：[src/math/Quaternion.js#L314](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L314)  
引入版本：3.0.0


---

### lengthSq {#lengthSq}

#### \<instance> lengthSq() {#instance-lengthsq}


**说明:**

计算此 Quaternion 平方的长度 。


**返回值:** number - 这个Quaternion的长度,平方.


> 源码：[src/math/Quaternion.js#L332](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L332)  
引入版本：3.0.0


---

### lerp {#lerp}

#### \<instance> lerp(v, [t]) {#instance-lerpv-t}


**说明:**

直线插这个Quaternion 向给定的Quaternion或矢量.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | [Phaser.Math.Quaternion](/api/class/math-quaternion) \| [Phaser.Math.Vector4](/api/class/math-vector4) | 否 |  | Quaternion或矢量向向内插. |
| t | number | 是 | 0 | 插值的百分比。 |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L397](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L397)  
引入版本：3.0.0


---

### multiply {#multiply}

#### \<instance> multiply(b) {#instance-multiplyb}


**说明:**

乘以给定的Quaternion或矢量.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| b | [Phaser.Math.Quaternion](/api/class/math-quaternion) \| [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | Quaternion或矢量乘以这个Quaternion. |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L544](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L544)  
引入版本：3.0.0


---

### normalize {#normalize}

#### \<instance> normalize() {#instance-normalize}


**说明:**

将这个Quaternion 规范化, 将其缩放为单位长度。 如果 Quaternion 的长度为零, 则不更改 。


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L350](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L350)  
引入版本：3.0.0


---

### rotateX {#rotateX}

#### \<instance> rotateX(rad) {#instance-rotatexrad}


**说明:**

在 X 轴上旋转这个 Quaternion 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rad | number | 否 | 弧度的旋转角度. |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L689](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L689)  
引入版本：3.0.0


---

### rotateY {#rotateY}

#### \<instance> rotateY(rad) {#instance-rotateyrad}


**说明:**

在 Y 轴上旋转这个 Quaternion 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rad | number | 否 | 弧度的旋转角度. |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L719](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L719)  
引入版本：3.0.0


---

### rotateZ {#rotateZ}

#### \<instance> rotateZ(rad) {#instance-rotatezrad}


**说明:**

在 Z 轴上旋转这个 Quaternion 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rad | number | 否 | 弧度的旋转角度. |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L749](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L749)  
引入版本：3.0.0


---

### rotationTo {#rotationTo}

#### \<instance> rotationTo(a, b) {#instance-rotationtoa-b}


**说明:**

设定此 Quaternion 以表示单位矢量 `a` 到单位矢量 `b` 的最短弧旋转。 这是将 `a` 与 `b` 相匹配所需的最小旋转。 调用此方法前必须使两个矢量都正常化 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 起始单位矢量 。 |
| b | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 目标单位矢量. |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L425](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L425)  
引入版本：3.0.0


---

### scale {#scale}

#### \<instance> scale(scale) {#instance-scalescale}


**说明:**

以给定的值缩放此 Quaternion 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scale | number | 否 | 以 Quaternion 缩放的值 。 |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L292](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L292)  
引入版本：3.0.0


---

### set {#set}

#### \<instance> set([x], [y], [z], [w], [update]) {#instance-setx-y-z-w-update}


**说明:**

设定此 Quaternion 的组件, 并可选地调用 `onChangeCallback` 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number \| object | 是 | 0 | x 组件,或含有x,y,z,和w 组件的物体. |
| y | number | 是 | 0 | y组件. |
| z | number | 是 | 0 | z组件. |
| w | number | 是 | 0 | 维元件. |
| update | boolean | 是 | true | 给`onChangeCallback`打电话? |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L207](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L207)  
引入版本：3.0.0


---

### setAxes {#setAxes}

#### \<instance> setAxes(view, right, up) {#instance-setaxesview-right-up}


**说明:**

设置此 Quaternion 从给定视图中, 右侧和上轴向量。 三个向量被写入一个临时矩阵3, 然后转换成一个正态的四角。 所有三个向量应该是正向单位向量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| view | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 观(前)轴. |
| right | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 右轴. |
| up | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 上轴线 |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L471](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L471)  
引入版本：3.0.0


---

### setAxisAngle {#setAxisAngle}

#### \<instance> setAxisAngle(axis, rad) {#instance-setaxisangleaxis-rad}


**说明:**

设定此 Quaternion 以表示 `rad` 弧度围绕给定的正态轴向量旋转 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| axis | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 旋转的正态轴向量 。 |
| rad | number | 否 | 弧度的旋转角度. |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L518](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L518)  
引入版本：3.0.0


---

### setFromEuler {#setFromEuler}

#### \<instance> setFromEuler(euler, [update]) {#instance-setfromeulereuler-update}


**说明:**

设置此从给定的 Eular 对象的 Quaternion 。 转换时会尊重 Eular 的旋转顺序( 如 “ XYZ ” 、 “ YXZ ” 、  “ ZXY ” 、 “ ZZX ” ) , 生成等效的四角旋转 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| euler | [Phaser.Math.Euler](/api/class/math-euler) | 否 |  | 欧拉反对从中转换 。 |
| update | boolean | 是 | true | 运行`onChangeCallback`? |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L800](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L800)  
引入版本：3.50.0


---

### setFromRotationMatrix {#setFromRotationMatrix}

#### \<instance> setFromRotationMatrix(mat4) {#instance-setfromrotationmatrixmat4}


**说明:**

设定此 Quaternion 从给定矩阵4 的旋转 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mat4 | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 矩阵4 设定旋转从。 |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L911](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L911)  
引入版本：3.50.0


---

### slerp {#slerp}

#### \<instance> slerp(b, t) {#instance-slerpb-t}


**说明:**

执行这个Quaternion和给定的Quaternion或矢量之间的球形线性插值(slerp). 与`lerp`不同,slerp沿着单位球体最短的弧线插值,保持恒定角速度,产生平滑,自然的旋转.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| b | [Phaser.Math.Quaternion](/api/class/math-quaternion) \| [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | Quaternion或矢量向向内插. |
| t | number | 否 | 插值因子,一般在[0, 1] 范围内. |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L574](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L574)  
引入版本：3.0.0


---

### subtract {#subtract}

#### \<instance> subtract(v) {#instance-subtractv}


**说明:**

从此 Quaternion 中减去一个给定的 Quaternion 或 矢量。 子化是按组件计算的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Quaternion](/api/class/math-quaternion) \| [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 从这个Quaternion 中减去 Quaternion 或 矢量 。 |


**返回值:** [Phaser.Math.Quaternion](/api/class/math-quaternion) - 此盖特尼翁.


> 源码：[src/math/Quaternion.js#L270](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Quaternion.js#L270)  
引入版本：3.0.0


---

---
