# Vector3 {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/math-vector3)

A Vector3是一个代表3D空间中点或方向的数学对象,由三个组件定义:`x`,`y`,和`z`.

矢量3 对象在 Phaser 的 3D 数学工具中被使用,包括矩阵转换、四角旋转、相机未投影和 3D- 2D 投影。它们通常用于与 3D 渲染器、 自定义的阴影或任何需要代表三维空间中的位置、方向或正常的代码合作。

该类包括常见的矢量操作方法,如增减,缩放,正常化,点和交叉产物,线性插值,以及矩阵3,矩阵4和Quaternion对象的变换.

提供了一组静态的只读常数(如`Vector3.UP`,`Vector3.FORWARD`),以方便的方向参考.

**构造函数**

`new Vector3([x], [y], [z])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 是 | ×组件. |
| y | number | 是 | y组件. |
| z | number | 是 | z组件. |

---


**作用域**: static

> 源码：[src/math/Vector3.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L12)  
引入版本：3.0.0

## 公开成员 {#public-members}

### x {#x}

#### x: number {#x-number}


**说明:**

此矢量的x组件.


> 源码：[src/math/Vector3.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L44)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

此矢量的y部分.


> 源码：[src/math/Vector3.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L54)  
引入版本：3.0.0


---

### z {#z}

#### z: number {#z-number}


**说明:**

The z component of this Vector.


> 源码：[src/math/Vector3.js#L64](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L64)  
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
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 向量器来加入这个向量器. |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L348](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L348)  
引入版本：3.0.0


---

### addScalar {#addScalar}

#### \<instance> addScalar(s) {#instance-addscalars}


**说明:**

将给定的值添加到此矢量的每个组件中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| s | number | 否 | 加入这个矢量的金额。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L367](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L367)  
引入版本：3.50.0


---

### addScale {#addScale}

#### \<instance> addScale(v, scale) {#instance-addscalev-scale}


**说明:**

在此矢量上添加和缩放一个给定矢量。 添加是按组件进行 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 向量器来加入这个向量器. |
| scale | number | 否 | 以`v`为比例的金额。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L386](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L386)  
引入版本：3.50.0


---

### addVectors {#addVectors}

#### \<instance> addVectors(a, b) {#instance-addvectorsa-b}


**说明:**

将两个给定的矢量3加成,并将结果设置在这个矢量3中.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 初增诸佛性. |
| b | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 第二向量加持. |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L158)  
引入版本：3.50.0


---

### applyMatrix3 {#applyMatrix3}

#### \<instance> applyMatrix3(mat3) {#instance-applymatrix3mat3}


**说明:**

使用矩阵3,并将其应用于这个矢量3。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mat3 | [Phaser.Math.Matrix3](/api/class/math-matrix3) | 否 | 矩阵3适用于此矢量3。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L682](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L682)  
引入版本：3.50.0


---

### applyMatrix4 {#applyMatrix4}

#### \<instance> applyMatrix4(mat4) {#instance-applymatrix4mat4}


**说明:**

使用矩阵4,并将其应用于这个矢量3。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mat4 | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 矩阵4适用于此矢量3。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L706](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L706)  
引入版本：3.50.0


---

### clone {#clone}

#### \<instance> clone() {#instance-clone}


**说明:**

制作这个矢量3的克隆.


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 包含这个矢量值的新矢量3对象 。


> 源码：[src/math/Vector3.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L145)  
引入版本：3.0.0


---

### copy {#copy}

#### \<instance> copy(src) {#instance-copysrc}


**说明:**

将给定的矢量的组件复制到此矢量中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 向量从复制组件。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L242](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L242)  
引入版本：3.0.0


---

### cross {#cross}

#### \<instance> cross(v) {#instance-crossv}


**说明:**

计算此矢量( 将修改) 和给定矢量的十字( 向量) 产品 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 与产品交叉的矢量。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L628](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L628)  
引入版本：3.0.0


---

### crossVectors {#crossVectors}

#### \<instance> crossVectors(a, b) {#instance-crossvectorsa-b}


**说明:**

计算两个给定矢量的十字( 向量) 产品 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 最早在交叉产品计算中使用的矢量. |
| b | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 交叉产品计算中使用的第二个矢量. |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L198](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L198)  
引入版本：3.0.0


---

### distance {#distance}

#### \<instance> distance(v) {#instance-distancev}


**说明:**

计算此矢量和给定矢量之间的距离 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 计算距离的矢量器。 |


**返回值:** number - 从这个矢量到给定矢量的距离.


> 源码：[src/math/Vector3.js#L512](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L512)  
引入版本：3.0.0


---

### distanceSq {#distanceSq}

#### \<instance> distanceSq(v) {#instance-distancesqv}


**说明:**

计算此矢量和给定矢量之间的距离, 平方 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 计算距离的矢量器。 |


**返回值:** number - 从这个矢量到给定矢量的距离,平方.


> 源码：[src/math/Vector3.js#L531](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L531)  
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
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 矢量器可以将矢量器分割开来 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L474](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L474)  
引入版本：3.0.0


---

### dot {#dot}

#### \<instance> dot(v) {#instance-dotv}


**说明:**

计算此矢量和给定矢量的点产品 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 矢量3与这个矢量3一起生产点点产品. |


**返回值:** number - 这个矢量和`v`的点产品.


> 源码：[src/math/Vector3.js#L613](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L613)  
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
| v | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 矢量3比较. |


**返回值:** boolean - 如果两个矢量严格匹配,否则是虚假的.


> 源码：[src/math/Vector3.js#L225](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L225)  
引入版本：3.0.0


---

### fromArray {#fromArray}

#### \<instance> fromArray(array, [offset]) {#instance-fromarrayarray-offset}


**说明:**

设置此矢量3 的组件, 以偏移为基础。

矢量3.x = 阵列[offset] 矢量3.y = 阵列[offset + 1] 矢量3.z = 阵列[offset + 2] 矢量3.z = 阵列[offset + 2] 矢量3.y = 数组[offset + 2] 矢量3.z = 矢量3.z = 数组[offset + 2] 矢量3.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| array | Array.\<number> | 否 |  | 要从中获取这个矢量的数值阵列 。 |
| offset | number | 是 | 0 | 向数组中输入的偏移索引 。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L322](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L322)  
引入版本：3.50.0


---

### length {#length}

#### \<instance> length() {#instance-length}


**说明:**

计算此矢量的长度( 或大小 ) 。


**返回值:** number - 此矢量之长短.


> 源码：[src/math/Vector3.js#L550](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L550)  
引入版本：3.0.0


---

### lengthSq {#lengthSq}

#### \<instance> lengthSq() {#instance-lengthsq}


**说明:**

计算这个矢量平方的长度 。


**返回值:** number - 这个矢量的长度,平方


> 源码：[src/math/Vector3.js#L567](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L567)  
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
| v | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 |  | 向内插插管3号 |
| t | number | 是 | 0 | 插值因子,介于0到1之间. |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L654](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L654)  
引入版本：3.0.0


---

### max {#max}

#### \<instance> max(v) {#instance-maxv}


**说明:**

设定此矢量的组件为给定矢量产生的`Math.max`结果 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 矢量3 以检查最大值对齐 。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L126)  
引入版本：3.50.0


---

### min {#min}

#### \<instance> min(v) {#instance-minv}


**说明:**

设定此矢量的组件为给定矢量产生的`Math.min`结果 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 矢量3 检查最小值对齐 。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L107)  
引入版本：3.50.0


---

### multiply {#multiply}

#### \<instance> multiply(v) {#instance-multiplyv}


**说明:**

在此矢量和给定矢量之间执行一个组件乘法 。

以给定的矢量乘以这个矢量.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 向量器可以乘以这个向量器. |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L425](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L425)  
引入版本：3.0.0


---

### negate {#negate}

#### \<instance> negate() {#instance-negate}


**说明:**

取消这个矢量的`x`,`y`和`z`组件.


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L495](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L495)  
引入版本：3.0.0


---

### normalize {#normalize}

#### \<instance> normalize() {#instance-normalize}


**说明:**

使这个矢量正常化.

使矢量成为同一方向的单位长度矢量(放大度为1).


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L584](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L584)  
引入版本：3.0.0


---

### project {#project}

#### \<instance> project(mat) {#instance-projectmat}


**说明:**

用指定的矩阵乘以此矢量3, 应用 W 的分隔。 这对投影有用, 例如, 无法预测 2D 点到 3D 空间 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mat | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 矩阵4可以乘以这个矢量3。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L844](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L844)  
引入版本：3.0.0


---

### projectViewMatrix {#projectViewMatrix}

#### \<instance> projectViewMatrix(viewMatrix, projectionMatrix) {#instance-projectviewmatrixviewmatrix-projectionmatrix}


**说明:**

将这个矢量3乘以给定视图和投影矩阵。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| viewMatrix | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 视图矩阵。 |
| projectionMatrix | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 投影矩阵. |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L888](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L888)  
引入版本：3.50.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

使这个矢量为零向量( 0, 0, 0) 。


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L956](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L956)  
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


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L446](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L446)  
引入版本：3.0.0


---

### set {#set}

#### \<instance> set(x, [y], [z]) {#instance-setx-y-z}


**说明:**

设定 `x`, `y`,和 `z` 向量的组件 `x`, `y`,和 `z` 价值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number \| object | 否 | 用于此矢量的x值,或包含x,y和z组件的对象. |
| y | number | 是 | 此矢量的 Y 值设置 。 |
| z | number | 是 | 用于此矢量的 Z 值 。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L261](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L261)  
引入版本：3.0.0


---

### setFromMatrixColumn {#setFromMatrixColumn}

#### \<instance> setFromMatrixColumn(mat4, index) {#instance-setfrommatrixcolumnmat4-index}


**说明:**

从指定的矩阵4列中设定此矢量3的组件。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mat4 | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 矩阵4来取列. |
| index | number | 否 | 专栏索引. |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L306](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L306)  
引入版本：3.50.0


---

### setFromMatrixPosition {#setFromMatrixPosition}

#### \<instance> setFromMatrixPosition(mat4) {#instance-setfrommatrixpositionmat4}


**说明:**

从给定矩阵4的位置设置此矢量3的组件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mat4 | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 矩阵4 获得位置。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L291](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L291)  
引入版本：3.50.0


---

### subtract {#subtract}

#### \<instance> subtract(v) {#instance-subtractv}


**说明:**

从此矢量中减去给定的矢量。 减法是按组件进行 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector2](/api/class/math-vector2) \| [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 向量从这个向量中减掉。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L406](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L406)  
引入版本：3.0.0


---

### subVectors {#subVectors}

#### \<instance> subVectors(a, b) {#instance-subvectorsa-b}


**说明:**

将两个给定的矢量3进行减法,并将结果设定为这个矢量3.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 向量从中减. |
| b | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 向量减法. |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L178)  
引入版本：3.85.0


---

### transformCoordinates {#transformCoordinates}

#### \<instance> transformCoordinates(mat) {#instance-transformcoordinatesmat}


**说明:**

以给定的矩阵4 改变这个矢量3 的坐标 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mat | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 矩阵4可以改变这个矢量3。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L780](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L780)  
引入版本：3.0.0


---

### transformMat3 {#transformMat3}

#### \<instance> transformMat3(mat) {#instance-transformmat3mat}


**说明:**

以给定的矩阵来改变这个矢量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mat | [Phaser.Math.Matrix3](/api/class/math-matrix3) | 否 | 矩阵3 用来改变这个矢量3 。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L732](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L732)  
引入版本：3.0.0


---

### transformMat4 {#transformMat4}

#### \<instance> transformMat4(mat) {#instance-transformmat4mat}


**说明:**

用给定的矩阵4 来改变这个矢量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mat | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 矩阵4可以改变这个矢量3。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L756](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L756)  
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


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L809](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L809)  
引入版本：3.0.0


---

### unproject {#unproject}

#### \<instance> unproject(viewport, invProjectionView) {#instance-unprojectviewport-invprojectionview}


**说明:**

将此点从 2D 空间到 3D 空间。 该点的 x 和 y 属性应设置为 2D 屏幕空间, z 或 0. 0 (靠近平面) 或 1 (远平面) 。 提供的矩阵被假定为已经合并, 即投射 * 视图 * 模型 。

此操作后,此矢量( x, y, z) 组件将代表未预测的3D坐标.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| viewport | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 屏幕 x,y,宽度和高度以像素表示. |
| invProjectionView | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 综合预测和视图矩阵。 |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L920](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L920)  
引入版本：3.0.0


---

### unprojectViewMatrix {#unprojectViewMatrix}

#### \<instance> unprojectViewMatrix(projectionMatrix, worldMatrix) {#instance-unprojectviewmatrixprojectionmatrix-worldmatrix}


**说明:**

将这个矢量3乘以给定的反向投影矩阵和世界矩阵.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| projectionMatrix | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 逆向投影矩阵. |
| worldMatrix | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 世界观矩阵. |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L904](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L904)  
引入版本：3.50.0


---

### up {#up}

#### \<instance> up() {#instance-up}


**说明:**

设此矢量以指之.

将矢量的y 组件设置为 1,其他的设置为 0。


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 这个矢量3。


> 源码：[src/math/Vector3.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L88)  
引入版本：3.0.0


---

## 常量 {#constants}

## 公开成员 {#public-members-1}

### BACK {#BACK}

#### BACK: [Phaser.Math.Vector3](/api/class/math-vector3) {#back-phasermathvector3}


**说明:**

静态背向量3,用于参考.

这个常数是用于比较操作的,不应直接修改.


> 源码：[src/math/Vector3.js#L1047](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L1047)  
引入版本：3.16.0


---

### DOWN {#DOWN}

#### DOWN: [Phaser.Math.Vector3](/api/class/math-vector3) {#down-phasermathvector3}


**说明:**

静态下向量3,供参考使用.

这个常数是用于比较操作的,不应直接修改.


> 源码：[src/math/Vector3.js#L1023](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L1023)  
引入版本：3.16.0


---

### FORWARD {#FORWARD}

#### FORWARD: [Phaser.Math.Vector3](/api/class/math-vector3) {#forward-phasermathvector3}


**说明:**

静态前向矢量3,用于参考.

这个常数是用于比较操作的,不应直接修改.


> 源码：[src/math/Vector3.js#L1035](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L1035)  
引入版本：3.16.0


---

### LEFT {#LEFT}

#### LEFT: [Phaser.Math.Vector3](/api/class/math-vector3) {#left-phasermathvector3}


**说明:**

静态左向量3,供参考使用.

这个常数是用于比较操作的,不应直接修改.


> 源码：[src/math/Vector3.js#L999](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L999)  
引入版本：3.16.0


---

### ONE {#ONE}

#### ONE: [Phaser.Math.Vector3](/api/class/math-vector3) {#one-phasermathvector3}


**说明:**

静态1矢量3,用于参考.

这个常数是用于比较操作的,不应直接修改.


> 源码：[src/math/Vector3.js#L1059](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L1059)  
引入版本：3.16.0


---

### RIGHT {#RIGHT}

#### RIGHT: [Phaser.Math.Vector3](/api/class/math-vector3) {#right-phasermathvector3}


**说明:**

静态右向量3,用于参考.

这个常数是用于比较操作的,不应直接修改.


> 源码：[src/math/Vector3.js#L987](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L987)  
引入版本：3.16.0


---

### UP {#UP}

#### UP: [Phaser.Math.Vector3](/api/class/math-vector3) {#up-phasermathvector3}


**说明:**

静态上升矢量3, 用于参考.

这个常数是用于比较操作的,不应直接修改.


> 源码：[src/math/Vector3.js#L1011](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L1011)  
引入版本：3.16.0


---

### ZERO {#ZERO}

#### ZERO: [Phaser.Math.Vector3](/api/class/math-vector3) {#zero-phasermathvector3}


**说明:**

静态零矢量3,用于参考.

这个常数是用于比较操作的,不应直接修改.


> 源码：[src/math/Vector3.js#L975](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector3.js#L975)  
引入版本：3.16.0


---

---
