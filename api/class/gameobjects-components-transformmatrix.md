# TransformMatrix {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-components-transformmatrix)

变形Matrix是一个3x3的affine变形矩阵,用于编码一个游戏对象用于渲染的位置,旋转,尺度和skew.

它由Phaser在渲染管道中内部使用,用于积累亲子变换链和进行摄像机变换。您通常在写自定义变换器或与摄像机或显示列表变换管道工作时与它交互。

其代表情况如下:

```
| a | c | tx |
| b | d | ty |
| 0 | 0 | 1  |
```

**构造函数**

`new TransformMatrix([a], [b], [c], [d], [tx], [ty])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| a | number | 是 | 1 | 缩放 X 值 。 |
| b | number | 是 | 0 | 摇摆Y值. |
| c | number | 是 | 0 | 滑动 X 值 。 |
| d | number | 是 | 1 | 缩放 Y 值 。 |
| tx | number | 是 | 0 | 翻译 X 值 。 |
| ty | number | 是 | 0 | 翻译的Y值。 |

---


**作用域**: static

> 源码：[src/gameobjects/components/TransformMatrix.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L11)  
引入版本：3.0.0

## 公开成员 {#public-members}

### a {#a}

#### a: number {#a-number}


**说明:**

缩放 X 值 。


> 源码：[src/gameobjects/components/TransformMatrix.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L88)  
引入版本：3.4.0


---

### b {#b}

#### b: number {#b-number}


**说明:**

摇摆Y值.


> 源码：[src/gameobjects/components/TransformMatrix.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L109)  
引入版本：3.4.0


---

### c {#c}

#### c: number {#c-number}


**说明:**

滑动 X 值 。


> 源码：[src/gameobjects/components/TransformMatrix.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L130)  
引入版本：3.4.0


---

### d {#d}

#### d: number {#d-number}


**说明:**

缩放 Y 值 。


> 源码：[src/gameobjects/components/TransformMatrix.js#L151](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L151)  
引入版本：3.4.0


---

### decomposedMatrix {#decomposedMatrix}

#### decomposedMatrix: object {#decomposedmatrix-object}


**说明:**

分解的矩阵.


> 源码：[src/gameobjects/components/TransformMatrix.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L63)  
引入版本：3.0.0


---

### e {#e}

#### e: number {#e-number}


**说明:**

翻译 X 值 。


> 源码：[src/gameobjects/components/TransformMatrix.js#L172](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L172)  
引入版本：3.11.0


---

### f {#f}

#### f: number {#f-number}


**说明:**

翻译的Y值。


> 源码：[src/gameobjects/components/TransformMatrix.js#L193](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L193)  
引入版本：3.11.0


---

### matrix {#matrix}

#### matrix: Float32Array {#matrix-float32array}


**说明:**

矩阵值。


> 源码：[src/gameobjects/components/TransformMatrix.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L54)  
引入版本：3.0.0


---

### quad {#quad}

#### quad: Float32Array {#quad-float32array}


**说明:**

临时四位值缓存 。


> 源码：[src/gameobjects/components/TransformMatrix.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L78)  
引入版本：3.60.0


---

### rotation {#rotation}

#### rotation: number {#rotation-number}


**说明:**

矩阵的旋转,数值为弧度。


> 源码：[src/gameobjects/components/TransformMatrix.js#L256](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L256)  
引入版本：3.4.0


---

### rotationNormalized {#rotationNormalized}

#### rotationNormalized: number {#rotationnormalized-number}


**说明:**

矩阵的旋转,在正常状态下,在 Phaser 右手顺时针旋转空间。值以弧度表示。


> 源码：[src/gameobjects/components/TransformMatrix.js#L273](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L273)  
引入版本：3.19.0


---

### scaleX {#scaleX}

#### scaleX: number {#scalex-number}


**说明:**

矩阵的分解水平尺度。 此值总是正数 。


> 源码：[src/gameobjects/components/TransformMatrix.js#L313](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L313)  
引入版本：3.4.0


---

### scaleY {#scaleY}

#### scaleY: number {#scaley-number}


**说明:**

矩阵的分解垂直尺度。 此值总是正数 。


> 源码：[src/gameobjects/components/TransformMatrix.js#L330](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L330)  
引入版本：3.4.0


---

### tx {#tx}

#### tx: number {#tx-number}


**说明:**

翻译 X 值 。


> 源码：[src/gameobjects/components/TransformMatrix.js#L214](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L214)  
引入版本：3.4.0


---

### ty {#ty}

#### ty: number {#ty-number}


**说明:**

翻译的Y值。


> 源码：[src/gameobjects/components/TransformMatrix.js#L235](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L235)  
引入版本：3.4.0


---

## 公开方法 {#public-methods}

### applyInverse {#applyInverse}

#### \<instance> applyInverse(x, y, [output]) {#instance-applyinversex-y-output}


**说明:**

采用 `x` 和 `y` 值,返回 `output` 向量中的新位置,该位置是当前矩阵的逆向,并应用其转换。

可用于将点数从世界翻译到本地空间.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 翻译的 x 位置 。 |
| y | number | 否 | 翻译的y位置. |
| output | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 一个矢量2,或指向对象,以存储结果. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 坐标,通过这个矩阵反向转换.


> 源码：[src/gameobjects/components/TransformMatrix.js#L912](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L912)  
引入版本：3.12.0


---

### applyITRS {#applyITRS}

#### \<instance> applyITRS(x, y, rotation, scaleX, scaleY) {#instance-applyitrsx-y-rotation-scalex-scaley}


**说明:**

在矩阵上应用身份,翻译,旋转和规模化操作.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 横向译经. |
| y | number | 否 | 竖译. |
| rotation | number | 否 | 弧度旋转的角度. |
| scaleX | number | 否 | 水平尺度。 |
| scaleY | number | 否 | 竖尺. |


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 这个变形马特里克斯。


> 源码：[src/gameobjects/components/TransformMatrix.js#L878](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L878)  
引入版本：3.0.0


---

### copyFrom {#copyFrom}

#### \<instance> copyFrom(src) {#instance-copyfromsrc}


**说明:**

设定此矩阵的值以复制给定的矩阵的值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 源矩阵从复制。 |


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 这个变形马特里克斯。


> 源码：[src/gameobjects/components/TransformMatrix.js#L634](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L634)  
引入版本：3.11.0


---

### copyFromArray {#copyFromArray}

#### \<instance> copyFromArray(src) {#instance-copyfromarraysrc}


**说明:**

设定此矩阵的值以复制给定的数组的值。 当数组索引 0、 1、 2、 3、 4 和 5 被映射到 a、 b、 c、 d、 e 和 f 时 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | array | 否 | 要设置到此矩阵的数值数组 。 |


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 这个变形马特里克斯。


> 源码：[src/gameobjects/components/TransformMatrix.js#L658](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L658)  
引入版本：3.11.0


---

### copyToArray {#copyToArray}

#### \<instance> copyToArray([out]) {#instance-copytoarrayout}


**说明:**

将矩阵中的值复制到给定的数组 。

如果数组指数0、1、2、3、4和5被映射到a、b、c、d、e和f。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| out | array | 是 | 将矩阵值复制到的数组 。 |


**返回值:** array - 0至5元素包含来自此矩阵的数值的数组。


> 源码：[src/gameobjects/components/TransformMatrix.js#L757](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L757)  
引入版本：3.12.0


---

### copyToContext {#copyToContext}

#### \<instance> copyToContext(ctx) {#instance-copytocontextctx}


**说明:**

将矩阵中的值复制到给定的 Canvas 渲染上下文。 这将使用 Currect. transform 方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ctx | CanvasRenderingContext2D | 否 | 将矩阵值复制到 Canvas 的上下文 。 |


**返回值:** CanvasRenderingContext2D - 坎瓦斯渲染背景.


> 源码：[src/gameobjects/components/TransformMatrix.js#L718](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L718)  
引入版本：3.12.0


---

### copyWithScrollFactorFrom {#copyWithScrollFactorFrom}

#### \<instance> copyWithScrollFactorFrom(src, scrollX, scrollY, scrollFactorX, scrollFactorY) {#instance-copywithscrollfactorfromsrc-scrollx-scrolly-scrollfactorx-scrollfactory}


**说明:**

设定此矩阵的值以复制给定矩阵的值, 并结合摄像机滚动因子 。

这在许多渲染函数中被使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 源矩阵从复制。 |
| scrollX | number | 否 | 横向滚动值以因数计算 。 |
| scrollY | number | 否 | 用于计算因素的垂直滚动值。 |
| scrollFactorX | number | 否 | 应用水平滚动因子 。 |
| scrollFactorY | number | 否 | 要应用的垂直滚动因子 。 |


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 这个变形马特里克斯。


> 源码：[src/gameobjects/components/TransformMatrix.js#L683](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L683)  
引入版本：4.0.0


---

### decomposeMatrix {#decomposeMatrix}

#### \<instance> decomposeMatrix() {#instance-decomposematrix}


**说明:**

使用 QR 解析将这个矩阵分解为它的翻译,缩放和旋转值.

其结果必须应用在如下的次序上,以复制目前的矩阵:

翻译 - > 旋转 - > 比例


**返回值:** [Phaser.Types.GameObjects.DecomposeMatrixResults](/api/typedef/types-gameobjects#decomposematrixresults) - 分解的母体。


> 源码：[src/gameobjects/components/TransformMatrix.js#L819](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L819)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这个变形矩阵。


> 源码：[src/gameobjects/components/TransformMatrix.js#L1095](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L1095)  
引入版本：3.4.0


---

### getCSSMatrix {#getCSSMatrix}

#### \<instance> getCSSMatrix() {#instance-getcssmatrix}


**说明:**

返回一个字符串,该字符串可以用作CSS变换调用,作为`matrix`属性.


**返回值:** string - 包含 CSS 变形矩阵值的字符串 。


> 源码：[src/gameobjects/components/TransformMatrix.js#L1080](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L1080)  
引入版本：3.12.0


---

### getX {#getX}

#### \<instance> getX(x, y) {#instance-getxx-y}


**说明:**

返回此矩阵的 X 组件乘以给定值。 这与 `x * a + y * c + e` 相同 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 值x的值,请检查url=值 (帮助). |
| y | number | 否 | y值("Y值"). |


**返回值:** number - 计算值x。


> 源码：[src/gameobjects/components/TransformMatrix.js#L994](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L994)  
引入版本：3.12.0


---

### getXRound {#getXRound}

#### \<instance> getXRound(x, y, [round]) {#instance-getxroundx-y-round}


**说明:**

返回该矩阵的 X 部分乘以给定值。

这和`x * a + y * c + e`一样,可选通过`Math.round`.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 值x的值,请检查url=值 (帮助). |
| y | number | 否 |  | y值("Y值"). |
| round | boolean | 是 | false | 数学 绕过结果的值? |


**返回值:** number - 计算值x。


> 源码：[src/gameobjects/components/TransformMatrix.js#L1028](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L1028)  
引入版本：3.50.0


---

### getY {#getY}

#### \<instance> getY(x, y) {#instance-getyx-y}


**说明:**

返回该矩阵的 Y 组件乘以给定值。这与 `x * b + y * d + f` 相同。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 值x的值,请检查url=值 (帮助). |
| y | number | 否 | y值("Y值"). |


**返回值:** number - 计算出y值.


> 源码：[src/gameobjects/components/TransformMatrix.js#L1011](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L1011)  
引入版本：3.12.0


---

### getYRound {#getYRound}

#### \<instance> getYRound(x, y, [round]) {#instance-getyroundx-y-round}


**说明:**

返回该矩阵的 Y 部分乘以给定值。

这和`x * b + y * d + f`一样,可选通过`Math.round`.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 值x的值,请检查url=值 (帮助). |
| y | number | 否 |  | y值("Y值"). |
| round | boolean | 是 | false | 数学 绕过结果的值? |


**返回值:** number - 计算出y值.


> 源码：[src/gameobjects/components/TransformMatrix.js#L1054](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L1054)  
引入版本：3.50.0


---

### invert {#invert}

#### \<instance> invert() {#instance-invert}


**说明:**

颠倒母体.


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 这个变形马特里克斯。


> 源码：[src/gameobjects/components/TransformMatrix.js#L603](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L603)  
引入版本：3.0.0


---

### loadIdentity {#loadIdentity}

#### \<instance> loadIdentity() {#instance-loadidentity}


**说明:**

将矩阵重置为身份矩阵 。


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 这个变形马特里克斯。


> 源码：[src/gameobjects/components/TransformMatrix.js#L347](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L347)  
引入版本：3.0.0


---

### multiply {#multiply}

#### \<instance> multiply(rhs, [out]) {#instance-multiplyrhs-out}


**说明:**

以给定的矩阵乘以这个矩阵.

如果给出了 `out`矩阵, 则结果将被存储在其中。 如果不给出, 此矩阵将被更新到原地。 如果您不想改变该矩阵, 请使用 `out`矩阵 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rhs | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 以母体乘之. |
| out | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 用于存储结果的可选矩阵 。 |


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix), [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 要么是变形马特里克斯,要么是`out`矩阵,如果在参数中给出的话.


> 源码：[src/gameobjects/components/TransformMatrix.js#L443](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L443)  
引入版本：3.0.0


---

### multiplyWithOffset {#multiplyWithOffset}

#### \<instance> multiplyWithOffset(src, offsetX, offsetY) {#instance-multiplywithoffsetsrc-offsetx-offsety}


**说明:**

将这个矩阵乘以给定的矩阵,包括冲抵。

电话 offsetX 添加到 tx 值中 : `offsetX * a + offsetY * c + tx`。该词 offsetY 添加到 ty 值中: `offsetX * b + offsetY * d + ty`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| src | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 源矩阵从复制。 |
| offsetX | number | 否 | 水平偏移以因数乘法。 |
| offsetY | number | 否 | 垂直冲抵以乘法的乘法。 |


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 这个变形马特里克斯。


> 源码：[src/gameobjects/components/TransformMatrix.js#L489](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L489)  
引入版本：3.11.0


---

### rotate {#rotate}

#### \<instance> rotate(angle) {#instance-rotateangle}


**说明:**

旋转矩阵。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| angle | number | 否 | 弧度旋转的角度. |


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 这个变形马特里克斯。


> 源码：[src/gameobjects/components/TransformMatrix.js#L413](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L413)  
引入版本：3.0.0


---

### scale {#scale}

#### \<instance> scale(x, y) {#instance-scalex-y}


**说明:**

缩放矩阵 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 水平尺度值 。 |
| y | number | 否 | 垂直比例值。 |


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 这个变形马特里克斯。


> 源码：[src/gameobjects/components/TransformMatrix.js#L390](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L390)  
引入版本：3.0.0


---

### setQuad {#setQuad}

#### \<instance> setQuad(x, y, xw, yh, [quad]) {#instance-setquadx-y-xw-yh-quad}


**说明:**

执行基于此矩阵和给定顶点坐标创建四边形顶点所需的8个计算。

其结果保存在`TransformMatrix.quad`中,从这种方法返回.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 四角体左上方顶点的 x 值。 |
| y | number | 否 | 四角体左上方顶点的y值。 |
| xw | number | 否 | 四角体右下方顶点的 x 值。 这是 x + 宽度 。 |
| yh | number | 否 | 四角体右下方顶点的y值。这是 y + 高度 。 |
| quad | Float32Array | 是 | 可选的浮点32 箭头来存储结果。 否则会使用本地的四进制数组 。 |


**返回值:** Float32Array - 四方浮点三十二箭头


> 源码：[src/gameobjects/components/TransformMatrix.js#L948](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L948)  
引入版本：3.60.0


---

### setToContext {#setToContext}

#### \<instance> setToContext(ctx) {#instance-settocontextctx}


**说明:**

将矩阵中的值复制到给定的 Canvas 渲染上下文。 这将使用上下文. setTransform 方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ctx | CanvasRenderingContext2D | 否 | 将矩阵值复制到 Canvas 的上下文 。 |


**返回值:** CanvasRenderingContext2D - 坎瓦斯渲染背景.


> 源码：[src/gameobjects/components/TransformMatrix.js#L738](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L738)  
引入版本：3.12.0


---

### setTransform {#setTransform}

#### \<instance> setTransform(a, b, c, d, tx, ty) {#instance-settransforma-b-c-d-tx-ty}


**说明:**

设置此矩阵的值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | number | 否 | 缩放 X 值 。 |
| b | number | 否 | 剪叶值. |
| c | number | 否 | 剪X值(Sher X). |
| d | number | 否 | 缩放 Y 值 。 |
| tx | number | 否 | 翻译 X 值 。 |
| ty | number | 否 | 翻译的Y值。 |


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 这个变形马特里克斯。


> 源码：[src/gameobjects/components/TransformMatrix.js#L790](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L790)  
引入版本：3.0.0


---

### transform {#transform}

#### \<instance> transform(a, b, c, d, tx, ty) {#instance-transforma-b-c-d-tx-ty}


**说明:**

变换母体。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | number | 否 | 缩放 X 值 。 |
| b | number | 否 | 剪叶值. |
| c | number | 否 | 剪X值(Sher X). |
| d | number | 否 | 缩放 Y 值 。 |
| tx | number | 否 | 翻译 X 值 。 |
| ty | number | 否 | 翻译的Y值。 |


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 这个变形马特里克斯。


> 源码：[src/gameobjects/components/TransformMatrix.js#L536](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L536)  
引入版本：3.0.0


---

### transformPoint {#transformPoint}

#### \<instance> transformPoint(x, y, [point]) {#instance-transformpointx-y-point}


**说明:**

将一个点转换到这个矩阵的局部空间 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 变换点的x坐标. |
| y | number | 否 | 变换点的y坐标. |
| point | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 | 可选点对象将转换的坐标存储在 。 |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 包含变形坐标的点.


> 源码：[src/gameobjects/components/TransformMatrix.js#L572](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L572)  
引入版本：3.0.0


---

### translate {#translate}

#### \<instance> translate(x, y) {#instance-translatex-y}


**说明:**

翻译母体。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 横向翻译值. |
| y | number | 否 | 垂直翻译值. |


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 这个变形马特里克斯。


> 源码：[src/gameobjects/components/TransformMatrix.js#L369](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TransformMatrix.js#L369)  
引入版本：3.0.0


---

---
