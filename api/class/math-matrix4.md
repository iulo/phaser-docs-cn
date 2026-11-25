# Matrix4 {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/math-matrix4)

4x4 列主要矩阵作为浮点32 的矩阵存储, 共 16 个值。 用于3D 转换, 包括投影、 视图和模型矩阵。 这是主要矩阵类 WebGL 正在运行到 Phaser,支持视角/地形投影,视相机设置,以及afine变换(翻译,旋转,比例).

改编自 [gl-matrix](https://github.com/toji/gl-matrix) 由藤间和 [vecmath](https://github.com/mattdesl/vecmath) 由 mattdesl 编辑

**构造函数**

`new Matrix4([m])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| m | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 是 | 复制值的可选矩阵4 。 |

---


**作用域**: static

> 源码：[src/math/Matrix4.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L15)  
引入版本：3.0.0

## 公开成员 {#public-members}

### val {#val}

#### val: Float32Array {#val-float32array}


**说明:**

矩阵值。


> 源码：[src/math/Matrix4.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L39)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### adjoint {#adjoint}

#### \<instance> adjoint() {#instance-adjoint}


**说明:**

计算这个矩阵的连带或附加物。


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L422](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L422)  
引入版本：3.0.0


---

### clone {#clone}

#### \<instance> clone() {#instance-clone}


**说明:**

制作这个矩阵4的克隆.


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵的克隆人4。


> 源码：[src/math/Matrix4.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L60)  
引入版本：3.0.0


---

### copy {#copy}

#### \<instance> copy(src) {#instance-copysrc}


**说明:**

将给定矩阵的值复制到此矩阵中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 复制值的矩阵 。 |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L137)  
引入版本：3.0.0


---

### determinant {#determinant}

#### \<instance> determinant() {#instance-determinant}


**说明:**

计算这个矩阵的决定因素 。


**返回值:** number - 母体的决定因素。


> 源码：[src/math/Matrix4.js#L474](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L474)  
引入版本：3.0.0


---

### fromArray {#fromArray}

#### \<instance> fromArray(a) {#instance-fromarraya}


**说明:**

从给定的数组中设定此矩阵的值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | Array.\<number> | 否 | 复制这些值的数组。 必须有至少 16 个元素 。 |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L154)  
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


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L1109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L1109)  
引入版本：3.0.0


---

### fromRotationTranslation {#fromRotationTranslation}

#### \<instance> fromRotationTranslation(q, v) {#instance-fromrotationtranslationq-v}


**说明:**

从给定的旋转 Quaternion 和 翻译矢量 中设置此矩阵的值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| q | [Phaser.Math.Quaternion](/api/class/math-quaternion) | 否 | Quaternion 来设定旋转。 |
| v | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 矢量设定翻译从。 |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L1051](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L1051)  
引入版本：3.0.0


---

### fromRotationXYTranslation {#fromRotationXYTranslation}

#### \<instance> fromRotationXYTranslation(rotation, position, translateFirst) {#instance-fromrotationxytranslationrotation-position-translatefirst}


**说明:**

取旋转和位置向量,从它们中构建这个矩阵4。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rotation | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 旋转向量 。 |
| position | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 位置向量 。 |
| translateFirst | boolean | 否 | 操作是先转动(`true`),还是再转动(`false`)? |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L1677](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L1677)  
引入版本：3.50.0


---

### frustum {#frustum}

#### \<instance> frustum(left, right, bottom, top, near, far) {#instance-frustumleft-right-bottom-top-near-far}


**说明:**

生成带有指定界限的frustum矩阵 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| left | number | 否 | 左结结诸结. |
| right | number | 否 | 右结结诸结. |
| bottom | number | 否 | 胸节的下部束缚. |
| top | number | 否 | 顶端的节肢动物。 |
| near | number | 否 | 近缘结节. |
| far | number | 否 | 远缘佛刹微尘数. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L1165](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L1165)  
引入版本：3.0.0


---

### getInverse {#getInverse}

#### \<instance> getInverse(m) {#instance-getinversem}


**说明:**

将给定的矩阵4复制到这个矩阵中,然后反转它.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| m | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 将矩阵4 反转到这个矩阵4 。 |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L328](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L328)  
引入版本：3.50.0


---

### getMaxScaleOnAxis {#getMaxScaleOnAxis}

#### \<instance> getMaxScaleOnAxis() {#instance-getmaxscaleonaxis}


**说明:**

从此矩阵返回最大轴比例 4。


**返回值:** number - 最大轴尺度 。


> 源码：[src/math/Matrix4.js#L1748](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L1748)  
引入版本：3.50.0


---

### identity {#identity}

#### \<instance> identity() {#instance-identity}


**说明:**

将这个矩阵重置为身份( 默认) 矩阵 。


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L280](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L280)  
引入版本：3.0.0


---

### invert {#invert}

#### \<instance> invert() {#instance-invert}


**说明:**

倒转这个矩阵。


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L345](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L345)  
引入版本：3.0.0


---

### lookAt {#lookAt}

#### \<instance> lookAt(eye, center, up) {#instance-lookateye-center-up}


**说明:**

生成一个带有给定眼位置,焦点,以及上轴的视星等矩阵.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| eye | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 观众的位置 |
| center | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 指着观众看 |
| up | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 一种矢量3指向上,用来引导相机卷. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L1400](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L1400)  
引入版本：3.0.0


---

### lookAtRH {#lookAtRH}

#### \<instance> lookAtRH(eye, target, up) {#instance-lookatrheye-target-up}


**说明:**

生成右手视矩阵,并带有给定的视位,目标及上轴.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| eye | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 观者位. |
| target | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 指观者所观. |
| up | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 一种矢量3指向上,用来引导相机卷. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L1340](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L1340)  
引入版本：3.50.0


---

### makeRotationAxis {#makeRotationAxis}

#### \<instance> makeRotationAxis(axis, angle) {#instance-makerotationaxisaxis-angle}


**说明:**

绕给定轴产生旋转矩阵。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| axis | [Phaser.Math.Vector3](/api/class/math-vector3) \| [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 旋转轴. |
| angle | number | 否 | 弧度的旋转角度. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L818](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L818)  
引入版本：3.0.0


---

### multiply {#multiply}

#### \<instance> multiply(src) {#instance-multiplysrc}


**说明:**

以给定的矩阵乘以这个矩阵.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 将这个矩阵乘以矩阵。 |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L523](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L523)  
引入版本：3.0.0


---

### multiplyLocal {#multiplyLocal}

#### \<instance> multiplyLocal(src) {#instance-multiplylocalsrc}


**说明:**

将这个矩阵4 的值乘以 `src` 参数中给出的值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 源矩阵4,这个矩阵4乘以. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L603](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L603)  
引入版本：3.0.0


---

### multiplyMatrices {#multiplyMatrices}

#### \<instance> multiplyMatrices(a, b) {#instance-multiplymatricesa-b}


**说明:**

将两个给定的矩阵4对象乘以数,并将结果存储在这个矩阵中.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 初总论四乘. |
| b | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 第二总论四以乘. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L658](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L658)  
引入版本：3.50.0


---

### multiplyToMat4 {#multiplyToMat4}

#### \<instance> multiplyToMat4(src, out) {#instance-multiplytomat4src-out}


**说明:**

用给定的`src` 矩阵4乘以这个矩阵4,并将结果存储在`out` 矩阵4中.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 母体4与这个相乘. |
| out | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 接收母体。 |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个`out`矩阵4。


> 源码：[src/math/Matrix4.js#L1604](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L1604)  
引入版本：3.50.0


---

### ortho {#ortho}

#### \<instance> ortho(left, right, bottom, top, near, far) {#instance-ortholeft-right-bottom-top-near-far}


**说明:**

生成带有给定界限的正弦投影矩阵。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| left | number | 否 | 左结结诸结. |
| right | number | 否 | 右结结诸结. |
| bottom | number | 否 | 胸节的下部束缚. |
| top | number | 否 | 顶端的节肢动物。 |
| near | number | 否 | 近缘结节. |
| far | number | 否 | 远缘佛刹微尘数. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L1291](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L1291)  
引入版本：3.0.0


---

### perspective {#perspective}

#### \<instance> perspective(fovy, aspect, near, far) {#instance-perspectivefovy-aspect-near-far}


**说明:**

生成一个带有给定界限的视角投影矩阵。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| fovy | number | 否 | 弧度垂直视图 |
| aspect | number | 否 | 视差比。 通常为视图宽度/ 高度 。 |
| near | number | 否 | 紧靠着大肠杆菌 |
| far | number | 否 | 远近的胸肌。 |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L1209](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L1209)  
引入版本：3.0.0


---

### perspectiveLH {#perspectiveLH}

#### \<instance> perspectiveLH(width, height, near, far) {#instance-perspectivelhwidth-height-near-far}


**说明:**

生成一个带有给定的frustum维度的左侧视角投影矩阵.

与`perspective`不同,这种方法为frustum取出明显的像素宽度和高度,而不是视野角和侧面比.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 宽度的节点。 |
| height | number | 否 | 节节的高度. |
| near | number | 否 | 紧靠着大肠杆菌 |
| far | number | 否 | 远近的胸肌。 |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L1250](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L1250)  
引入版本：3.0.0


---

### premultiply {#premultiply}

#### \<instance> premultiply(m) {#instance-premultiplym}


**说明:**

将给定的矩阵4对象与这个矩阵相乘.

这跟叫`multiplyMatrices(m, this)`一样

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| m | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 母体4与这个相乘. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L641](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L641)  
引入版本：3.50.0


---

### rotate {#rotate}

#### \<instance> rotate(rad, axis) {#instance-rotaterad-axis}


**说明:**

将旋转转换应用到此矩阵中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rad | number | 否 | 弧度的角度来旋转. |
| axis | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 轴旋转上. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L850](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L850)  
引入版本：3.0.0


---

### rotateX {#rotateX}

#### \<instance> rotateX(rad) {#instance-rotatexrad}


**说明:**

在其 X 轴上旋转此矩阵 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rad | number | 否 | 弧度的角度来旋转. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L934](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L934)  
引入版本：3.0.0


---

### rotateY {#rotateY}

#### \<instance> rotateY(rad) {#instance-rotateyrad}


**说明:**

在其 Y 轴上旋转此矩阵 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rad | number | 否 | 旋转的角度,用弧度表示。 |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L973](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L973)  
引入版本：3.0.0


---

### rotateZ {#rotateZ}

#### \<instance> rotateZ(rad) {#instance-rotatezrad}


**说明:**

在其 Z 轴上旋转此矩阵 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rad | number | 否 | 旋转的角度,用弧度表示。 |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L1012](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L1012)  
引入版本：3.0.0


---

### scale {#scale}

#### \<instance> scale(v) {#instance-scalev}


**说明:**

将比例转换应用到此矩阵中 。

使用给定矢量的`x`,`y`和`z`组件来放大矩阵.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector3](/api/class/math-vector3) \| [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 矢量器可以放大这个矩阵。 |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L767](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L767)  
引入版本：3.0.0


---

### scaleXYZ {#scaleXYZ}

#### \<instance> scaleXYZ(x, y, z) {#instance-scalexyzx-y-z}


**说明:**

将比例转换应用到此矩阵中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | ×组件. |
| y | number | 否 | y组件. |
| z | number | 否 | z组件. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L784](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L784)  
引入版本：3.16.0


---

### scaling {#scaling}

#### \<instance> scaling(x, y, z) {#instance-scalingx-y-z}


**说明:**

设置此矩阵的缩放值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | x 缩放值 。 |
| y | number | 否 | y 缩放值. |
| z | number | 否 | z缩放值. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L254](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L254)  
引入版本：3.0.0


---

### set {#set}

#### \<instance> set(src) {#instance-setsrc}


**说明:**

此方法为`Matrix4.copy`的别名.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 设置此矩阵值的矩阵 。 |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L73)  
引入版本：3.0.0


---

### setValues {#setValues}

#### \<instance> setValues(m00, m01, m02, m03, m10, m11, m12, m13, m20, m21, m22, m23, m30, m31, m32, m33) {#instance-setvaluesm00-m01-m02-m03-m10-m11-m12-m13-m20-m21-m22-m23-m30-m31-m32-m33}


**说明:**

设置此矩阵的全部值 4。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| m00 | number | 否 | 兆值(千兆). |
| m01 | number | 否 | 值为m01. |
| m02 | number | 否 | 米02值. |
| m03 | number | 否 | 米03值. |
| m10 | number | 否 | 10米值 。 |
| m11 | number | 否 | m11值("  "). |
| m12 | number | 否 | m12值("  "). |
| m13 | number | 否 | m13值("  "). |
| m20 | number | 否 | 20 值. |
| m21 | number | 否 | m21值(  ). |
| m22 | number | 否 | m22值(英语:M22 value). |
| m23 | number | 否 | m23值(英语:M23 value). |
| m30 | number | 否 | 30 个值。 |
| m31 | number | 否 | m31值(千兆元)   . |
| m32 | number | 否 | 米32值. |
| m33 | number | 否 | 33 计. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4的例子。


> 源码：[src/math/Matrix4.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L88)  
引入版本：3.50.0


---

### setWorldMatrix {#setWorldMatrix}

#### \<instance> setWorldMatrix(rotation, position, scale, [viewMatrix], [projectionMatrix]) {#instance-setworldmatrixrotation-position-scale-viewmatrix-projectionmatrix}


**说明:**

从给定的旋转,位置,尺度,视图矩阵和投影矩阵中生成一个世界矩阵.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rotation | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 世界矩阵的旋转. |
| position | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 世界矩阵的地位. |
| scale | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 世界矩阵的规模. |
| viewMatrix | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 是 | 观音矩阵. |
| projectionMatrix | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 是 | 投影矩阵. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L1567](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L1567)  
引入版本：3.0.0


---

### transform {#transform}

#### \<instance> transform(position, scale, rotation) {#instance-transformposition-scale-rotation}


**说明:**

根据给定位置、尺度和旋转生成一个变换矩阵。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| position | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 位置向量 。 |
| scale | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 缩放向量 。 |
| rotation | [Phaser.Math.Quaternion](/api/class/math-quaternion) | 否 | 旋转之四。 |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L184](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L184)  
引入版本：3.50.0


---

### translate {#translate}

#### \<instance> translate(v) {#instance-translatev}


**说明:**

用给定的矢量来翻译这个矩阵 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | [Phaser.Math.Vector3](/api/class/math-vector3) \| [Phaser.Math.Vector4](/api/class/math-vector4) | 否 | 矢量者,用这个矩阵来翻译. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L728](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L728)  
引入版本：3.0.0


---

### translateXYZ {#translateXYZ}

#### \<instance> translateXYZ(x, y, z) {#instance-translatexyzx-y-z}


**说明:**

使用给定的值翻译此矩阵 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | ×组件. |
| y | number | 否 | y组件. |
| z | number | 否 | z组件. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L743](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L743)  
引入版本：3.16.0


---

### transpose {#transpose}

#### \<instance> transpose() {#instance-transpose}


**说明:**

转录这个矩阵。


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L293](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L293)  
引入版本：3.0.0


---

### xyz {#xyz}

#### \<instance> xyz(x, y, z) {#instance-xyzx-y-z}


**说明:**

设定这个矩阵的 `x`, `y`和 `z` 值.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 值x的值,请检查url=值 (帮助). |
| y | number | 否 | y值("Y值"). |
| z | number | 否 | z值( z值) 。 |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L229](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L229)  
引入版本：3.0.0


---

### yawPitchRoll {#yawPitchRoll}

#### \<instance> yawPitchRoll(yaw, pitch, roll) {#instance-yawpitchrollyaw-pitch-roll}


**说明:**

从给定的 `yaw` 、 `pitch` 和 `roll` 值中设定此矩阵的值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| yaw | number | 否 | 弧度角度,用弧度表示。 |
| pitch | number | 否 | 投球角度,用弧度表示. |
| roll | number | 否 | 卷角,用弧度表示. |


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L1506](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L1506)  
引入版本：3.0.0


---

### zero {#zero}

#### \<instance> zero() {#instance-zero}


**说明:**

重置这个矩阵 。

设定全部值为 `0` 。


**返回值:** [Phaser.Math.Matrix4](/api/class/math-matrix4) - 这个矩阵4。


> 源码：[src/math/Matrix4.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Matrix4.js#L169)  
引入版本：3.0.0


---

---
