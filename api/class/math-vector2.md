# Vector2 {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/math-vector2)

由`x`和`y`组件定义的二维空间中矢量的表示.

矢量2 在整个过程中使用 Phaser 用于位置、方向、速度和具有大小和方向的其他数量。它提供了常见的矢量操作方法,如加、减、缩放、正常化、点和交叉产品、线性插值和旋转。 Phaser APIs 接受一个 `Vector2Like` 对象(任何对象,均需 `x` 财务报告和已审计财务报表 `y` 数字属性),使矢量2更容易在全框架中集成.

**构造函数**

`new Vector2([x], [y])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number \| [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 | 0 | x 组件,或具有`x`和`y`特性的物体. |
| y | number | 是 | "x" | y组件. |

---


**作用域**: static

> 源码：[src/math/Vector2.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L13)  
引入版本：3.0.0

## 公开成员 {#public-members}

### x {#x}

#### x: number {#x-number}


**说明:**

此矢量的x组件.


> 源码：[src/math/Vector2.js#L38](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L38)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

此矢量的y部分.


> 源码：[src/math/Vector2.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L48)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(src) {#instance-addsrc}


**说明:**

在此向量中添加一个给定的矢量。 添加是按组件设置的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 向量器来加入这个向量器. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L294](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L294)  
引入版本：3.0.0


---

### angle {#angle}

#### \<instance> angle() {#instance-angle}


**说明:**

计算这个矢量和正X轴之间的角,以弧度计。


**返回值:** number - 这个矢量与正X轴之间的角度,以弧度表示.


> 源码：[src/math/Vector2.js#L257](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L257)  
引入版本：3.0.0


---

### ceil {#ceil}

#### \<instance> ceil() {#instance-ceil}


**说明:**

通过 Math.ceil 运行此矢量2 的 x 和 y 组件,然后设置它们。


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L158)  
引入版本：4.0.0


---

### clone {#clone}

#### \<instance> clone() {#instance-clone}


**说明:**

制作这个矢量2的克隆.


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 这个矢量2的克隆体.


> 源码：[src/math/Vector2.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L72)  
引入版本：3.0.0


---

### copy {#copy}

#### \<instance> copy(src) {#instance-copysrc}


**说明:**

将给定的矢量的组件复制到此矢量中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 向量从复制组件。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L85)  
引入版本：3.0.0


---

### cross {#cross}

#### \<instance> cross(src) {#instance-crosssrc}


**说明:**

计算此矢量和给定矢量的交叉产物 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 矢量2号与这个矢量2号交叉. |


**返回值:** number - 这种矢量的十字产品和给定的矢量.


> 源码：[src/math/Vector2.js#L573](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L573)  
引入版本：3.0.0


---

### distance {#distance}

#### \<instance> distance(src) {#instance-distancesrc}


**说明:**

计算此矢量和给定矢量之间的距离 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 计算距离的矢量器。 |


**返回值:** number - 从这个矢量到给定矢量的距离.


> 源码：[src/math/Vector2.js#L412](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L412)  
引入版本：3.0.0


---

### distanceSq {#distanceSq}

#### \<instance> distanceSq(src) {#instance-distancesqsrc}


**说明:**

计算此矢量和给定矢量之间的距离, 平方 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 计算距离的矢量器。 |


**返回值:** number - 从这个矢量到给定矢量的距离,平方.


> 源码：[src/math/Vector2.js#L430](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L430)  
引入版本：3.0.0


---

### divide {#divide}

#### \<instance> divide(src) {#instance-dividesrc}


**说明:**

在此矢量和给定矢量之间执行一个组件区分 。

将这个矢量除以给定的矢量。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 矢量器可以将矢量器分割开来 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L376](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L376)  
引入版本：3.0.0


---

### dot {#dot}

#### \<instance> dot(src) {#instance-dotsrc}


**说明:**

计算此矢量和给定矢量的点产品 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 矢量2与这个矢量2一起的点产品. |


**返回值:** number - 这个矢量的点产品和给定的矢量.


> 源码：[src/math/Vector2.js#L558](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L558)  
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
| v | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 与这个矢量比较的矢量 。 |


**返回值:** boolean - 给定的矢量是否与这个矢量相等 。


> 源码：[src/math/Vector2.js#L224](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L224)  
引入版本：3.0.0


---

### floor {#floor}

#### \<instance> floor() {#instance-floor}


**说明:**

运行此矢量2的 x 和 y 组件, 运行到 Math. deplace , 然后设置它们 。


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L174](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L174)  
引入版本：4.0.0


---

### fuzzyEquals {#fuzzyEquals}

#### \<instance> fuzzyEquals(v, [epsilon]) {#instance-fuzzyequalsv-epsilon}


**说明:**

检查这个矢量是否与给定的矢量大致相等 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| v | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 |  | 与这个矢量比较的矢量 。 |
| epsilon | number | 是 | 0.0001 | 宽容的价值。 |


**返回值:** boolean - x和y两个组件的绝对差异是否都小于`epsilon`.


> 源码：[src/math/Vector2.js#L241](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L241)  
引入版本：3.23.0


---

### invert {#invert}

#### \<instance> invert() {#instance-invert}


**说明:**

交换此矢量2的 x 和 y 组件 。


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L190](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L190)  
引入版本：4.0.0


---

### length {#length}

#### \<instance> length() {#instance-length}


**说明:**

计算此矢量的长度( 或大小 ) 。


**返回值:** number - 此矢量之长短.


> 源码：[src/math/Vector2.js#L448](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L448)  
引入版本：3.0.0


---

### lengthSq {#lengthSq}

#### \<instance> lengthSq() {#instance-lengthsq}


**说明:**

计算这个矢量平方的长度 。


**返回值:** number - 这个矢量的长度,平方


> 源码：[src/math/Vector2.js#L479](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L479)  
引入版本：3.0.0


---

### lerp {#lerp}

#### \<instance> lerp(src, [t]) {#instance-lerpsrc-t}


**说明:**

线性插图介于这个矢量和给定矢量之间.

将这个矢量向给定矢量进发.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| src | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 |  | 向内插插进的矢量2 |
| t | number | 是 | 0 | 插值百分比,介于0到1之间. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L588](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L588)  
引入版本：3.0.0


---

### limit {#limit}

#### \<instance> limit(max) {#instance-limitmax}


**说明:**

限制此矢量的长度( 或大小 ) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| max | number | 否 | 最大长度。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L674](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L674)  
引入版本：3.23.0


---

### mirror {#mirror}

#### \<instance> mirror(axis) {#instance-mirroraxis}


**说明:**

反射这个矢量 跨越另一个。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| axis | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 向量反射到对面。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L713](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L713)  
引入版本：3.23.0


---

### multiply {#multiply}

#### \<instance> multiply(src) {#instance-multiplysrc}


**说明:**

在此矢量和给定矢量之间执行一个组件乘法 。

以给定的矢量乘以这个矢量.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 向量器可以乘以这个向量器. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L330](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L330)  
引入版本：3.0.0


---

### negate {#negate}

#### \<instance> negate() {#instance-negate}


**说明:**

取消这个矢量的`x`和`y`组件.


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L396](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L396)  
引入版本：3.0.0


---

### normalize {#normalize}

#### \<instance> normalize() {#instance-normalize}


**说明:**

使这个矢量正常化.

使矢量成为同一方向的单位长度矢量(放大度为1).


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L495](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L495)  
引入版本：3.0.0


---

### normalizeLeftHand {#normalizeLeftHand}

#### \<instance> normalizeLeftHand() {#instance-normalizelefthand}


**说明:**

将这个矢量旋转到它的垂直方向, 向负方向旋转 。


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L540](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L540)  
引入版本：3.23.0


---

### normalizeRightHand {#normalizeRightHand}

#### \<instance> normalizeRightHand() {#instance-normalizerighthand}


**说明:**

将这个矢量旋转到它的垂直方向, 向正方向旋转 。


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L522](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L522)  
引入版本：3.0.0


---

### project {#project}

#### \<instance> project(src) {#instance-projectsrc}


**说明:**

将此矢量投射到另一个上 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 投影的矢量 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L746](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L746)  
引入版本：3.60.0


---

### projectUnit {#projectUnit}

#### \<instance> projectUnit(vecB, [out]) {#instance-projectunitvecb-out}


**说明:**

计算此矢量2 的矢量投影到非零 `vecB`。 这是此矢量的正向投影到一条与 `vecB`平行的直线上 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vecB | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 投影的矢量 。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 矢量2 对象将位置存储在其中。 如果不给定, 则创建新的矢量2 实例 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 含有预测值的`out`矢量2。


> 源码：[src/math/Vector2.js#L763](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L763)  
引入版本：4.0.0


---

### reflect {#reflect}

#### \<instance> reflect(normal) {#instance-reflectnormal}


**说明:**

将这个矢量从普通人定义的线上反射出来 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| normal | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 向量垂直于线. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L696](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L696)  
引入版本：3.23.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

使这个矢量为0向量( 0, 0) 。


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L658](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L658)  
引入版本：3.0.0


---

### rotate {#rotate}

#### \<instance> rotate(delta) {#instance-rotatedelta}


**说明:**

以角度量旋转此矢量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delta | number | 否 | 旋转的角度,用弧度表示。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L728](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L728)  
引入版本：3.23.0


---

### scale {#scale}

#### \<instance> scale(value) {#instance-scalevalue}


**说明:**

按给定的值对这个矢量进行缩放 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 以何值缩放此矢量 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L350](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L350)  
引入版本：3.0.0


---

### set {#set}

#### \<instance> set(x, [y]) {#instance-setx-y}


**说明:**

设定 `x` 财务报告和已审计财务报表 `y` 向量的组件 `x` 财务报告和已审计财务报表 `y` 价值。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 此矢量的x值设置 。 |
| y | number | 是 | "x" | 此矢量的 Y 值设置 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L121)  
引入版本：3.0.0


---

### setAngle {#setAngle}

#### \<instance> setAngle(angle) {#instance-setangleangle}


**说明:**

设定矢量的角 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| angle | number | 否 | 角度,用弧度表示。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L279](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L279)  
引入版本：3.23.0


---

### setFromObject {#setFromObject}

#### \<instance> setFromObject(obj) {#instance-setfromobjectobj}


**说明:**

设定从给定的矢量2 类似对象中生成的矢量的组件值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| obj | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 包含要为此矢量设置的组件值的对象。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L103)  
引入版本：3.0.0


---

### setLength {#setLength}

#### \<instance> setLength(length) {#instance-setlengthlength}


**说明:**

设定此矢量的长度( 或大小 ) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| length | number | 否 | 这个矢量的新尺寸 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L464](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L464)  
引入版本：3.23.0


---

### setTo {#setTo}

#### \<instance> setTo(x, [y]) {#instance-settox-y}


**说明:**

此方法为`Vector2.set`的别名.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 此矢量的x值设置 。 |
| y | number | 是 | "x" | 此矢量的 Y 值设置 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L142)  
引入版本：3.4.0


---

### setToPolar {#setToPolar}

#### \<instance> setToPolar(angle, [length]) {#instance-settopolarangle-length}


**说明:**

从给定的角度和长度设置此矢量的 x 和 y 组件。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| angle | number | 否 |  | 从正X轴的角度,以弧度表示. |
| length | number | 是 | 1 | 与源之远. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L203](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L203)  
引入版本：3.0.0


---

### subtract {#subtract}

#### \<instance> subtract(src) {#instance-subtractsrc}


**说明:**

从此矢量中减去给定的矢量。 减法是按组件进行 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 向量从这个向量中减掉。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L312](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L312)  
引入版本：3.0.0


---

### transformMat3 {#transformMat3}

#### \<instance> transformMat3(mat) {#instance-transformmat3mat}


**说明:**

用给定的矩阵3 来改变这个矢量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mat | [Phaser.Math.Matrix3](/api/class/math-matrix3) | 否 | 矩阵3可以改变这个矢量2。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L614](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L614)  
引入版本：3.0.0


---

### transformMat4 {#transformMat4}

#### \<instance> transformMat4(mat) {#instance-transformmat4mat}


**说明:**

用给定的矩阵4 来改变这个矢量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mat | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 | 将这个矢量2 转换成的矩阵 4 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此矢量2号.


> 源码：[src/math/Vector2.js#L636](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L636)  
引入版本：3.0.0


---

## 常量 {#constants}

## 公开成员 {#public-members-1}

### DOWN {#DOWN}

#### DOWN: [Phaser.Math.Vector2](/api/class/math-vector2) {#down-phasermathvector2}


**说明:**

静态下向量2,用于参考.

此常量用于比较操作。请勿直接修改。


> 源码：[src/math/Vector2.js#L840](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L840)  
引入版本：3.16.0


---

### LEFT {#LEFT}

#### LEFT: [Phaser.Math.Vector2](/api/class/math-vector2) {#left-phasermathvector2}


**说明:**

静态左向量2,以参考使用.

此常量用于比较操作。请勿直接修改。


> 源码：[src/math/Vector2.js#L816](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L816)  
引入版本：3.16.0


---

### ONE {#ONE}

#### ONE: [Phaser.Math.Vector2](/api/class/math-vector2) {#one-phasermathvector2}


**说明:**

静态1矢量2,用于参考.

此常量用于比较操作。请勿直接修改。


> 源码：[src/math/Vector2.js#L852](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L852)  
引入版本：3.16.0


---

### RIGHT {#RIGHT}

#### RIGHT: [Phaser.Math.Vector2](/api/class/math-vector2) {#right-phasermathvector2}


**说明:**

静态右向量2,用于参考.

此常量用于比较操作。请勿直接修改。


> 源码：[src/math/Vector2.js#L804](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L804)  
引入版本：3.16.0


---

### UP {#UP}

#### UP: [Phaser.Math.Vector2](/api/class/math-vector2) {#up-phasermathvector2}


**说明:**

静态上升矢量2,供参考使用.

此常量用于比较操作。请勿直接修改。


> 源码：[src/math/Vector2.js#L828](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L828)  
引入版本：3.16.0


---

### ZERO {#ZERO}

#### ZERO: [Phaser.Math.Vector2](/api/class/math-vector2) {#zero-phasermathvector2}


**说明:**

静态零矢量2,用于参考.

此常量用于比较操作。请勿直接修改。


> 源码：[src/math/Vector2.js#L792](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Vector2.js#L792)  
引入版本：3.1.0


---

---
