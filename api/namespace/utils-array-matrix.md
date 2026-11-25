# Phaser.Utils.Array.Matrix {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/utils-array-matrix)

Scope: 
static
> 源码：[src/utils/array/matrix/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/matrix/index.js#L7)  


## 静态函数 {#static-functions}

### CheckMatrix {#CheckMatrix}

#### \<static> CheckMatrix([matrix]) {#static-checkmatrixmatrix}


**说明:**

检查一个数组是否可以用作矩阵 。

矩阵是一个二维阵列(数组阵列),所有子阵列(数组)的长度都是一样的。这是示例矩阵 :

```
[
   [ 1, 1, 1, 1, 1, 1 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 2, 0, 1, 2, 0, 4 ],
   [ 2, 0, 3, 4, 0, 4 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 3, 3, 3, 3, 3, 3 ]
]
```

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| matrix | Array.\<Array.\<T>> | 是 | 要检查的阵列 。 |


**返回值:** boolean - 如果给定的`matrix`阵列是一个有效的矩阵,则`true`.


> 源码：[src/utils/array/matrix/CheckMatrix.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/matrix/CheckMatrix.js#L7)  
引入版本：3.0.0


---

### MatrixToString {#MatrixToString}

#### \<static> MatrixToString([matrix]) {#static-matrixtostringmatrix}


**说明:**

生成给定矩阵矩阵的格式化字符串代表,适合通过该矩阵记录到控制台 `console.log`中,每行均按单元格值的自身线条进行制取,单元格值由 ` |`,行除以 a `---+` 分隔线。

矩阵是一个二维阵列(数组阵列),所有子阵列(数组)的长度都是一样的。 至少有两行。 这是示例矩阵 :

```
[
   [ 1, 1, 1, 1, 1, 1 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 2, 0, 1, 2, 0, 4 ],
   [ 2, 0, 3, 4, 0, 4 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 3, 3, 3, 3, 3, 3 ]
]
```

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| matrix | Array.\<Array.\<T>> | 是 | 代表矩阵的二维数组进行转换。 |


**返回值:** string - 代表矩阵的格式化字符串,列用 ` |` 分隔,行用 `---+` 分隔线分隔。如果矩阵无效,返回空字符串。


> 源码：[src/utils/array/matrix/MatrixToString.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/matrix/MatrixToString.js#L10)  
引入版本：3.0.0


---

### ReverseColumns {#ReverseColumns}

#### \<static> ReverseColumns([matrix]) {#static-reversecolumnsmatrix}


**说明:**

反转给定矩阵矩阵的行顺序,其效果是将每个列内值的顺序从上到下反转。

矩阵是一个二维阵列(数组阵列),所有子阵列(数组)的长度都是一样的。 至少有两行。 这是示例矩阵 :

```
[
   [ 1, 1, 1, 1, 1, 1 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 2, 0, 1, 2, 0, 4 ],
   [ 2, 0, 3, 4, 0, 4 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 3, 3, 3, 3, 3, 3 ]
]
```

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| matrix | Array.\<Array.\<T>> | 是 | 数组矩阵,其行顺序将逆向 。 |


**返回值:** Array.\<Array.\<T>> - 列反向矩阵.


> 源码：[src/utils/array/matrix/ReverseColumns.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/matrix/ReverseColumns.js#L7)  
引入版本：3.0.0


---

### ReverseRows {#ReverseRows}

#### \<static> ReverseRows([matrix]) {#static-reverserowsmatrix}


**说明:**

反转给定矩阵矩阵中每行元素的顺序。

矩阵是一个二维阵列(数组阵列),所有子阵列(数组)的长度都是一样的。 至少有两行。 这是示例矩阵 :

```
[
   [ 1, 1, 1, 1, 1, 1 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 2, 0, 1, 2, 0, 4 ],
   [ 2, 0, 3, 4, 0, 4 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 3, 3, 3, 3, 3, 3 ]
]
```

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| matrix | Array.\<Array.\<T>> | 是 | 逆向每行元素的矩阵矩阵。 |


**返回值:** Array.\<Array.\<T>> - 每行元素的矩阵倒置在原位.


> 源码：[src/utils/array/matrix/ReverseRows.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/matrix/ReverseRows.js#L7)  
引入版本：3.0.0


---

### Rotate180 {#Rotate180}

#### \<static> Rotate180([matrix]) {#static-rotate180matrix}


**说明:**

旋转矩阵矩阵 180 度。

矩阵是一个二维阵列(数组阵列),所有子阵列(数组)的长度都是一样的。 至少有两行。 这是示例矩阵 :

```
[
   [ 1, 1, 1, 1, 1, 1 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 2, 0, 1, 2, 0, 4 ],
   [ 2, 0, 3, 4, 0, 4 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 3, 3, 3, 3, 3, 3 ]
]
```

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| matrix | Array.\<Array.\<T>> | 是 | 要旋转的阵列 。 |


**返回值:** Array.\<Array.\<T>> - 旋转矩阵。 源矩阵应该被丢弃, 用于返回矩阵 。


> 源码：[src/utils/array/matrix/Rotate180.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/matrix/Rotate180.js#L9)  
引入版本：3.0.0


---

### RotateLeft {#RotateLeft}

#### \<static> RotateLeft([matrix], [amount]) {#static-rotateleftmatrix-amount}


**说明:**

将数组矩阵旋转到左侧(逆时针),每步90度。

矩阵是一个二维阵列(数组阵列),所有子阵列(数组)的长度都是一样的。 至少有两行。 这是示例矩阵 :

```
[
   [ 1, 1, 1, 1, 1, 1 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 2, 0, 1, 2, 0, 4 ],
   [ 2, 0, 3, 4, 0, 4 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 3, 3, 3, 3, 3, 3 ]
]
```

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| matrix | Array.\<Array.\<T>> | 是 |  | 要旋转的阵列 。 |
| amount | number | 是 | 1 | 左转90度矩阵旋转的次数. |


**返回值:** Array.\<Array.\<T>> - 旋转矩阵。 源矩阵应该被丢弃, 用于返回矩阵 。


> 源码：[src/utils/array/matrix/RotateLeft.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/matrix/RotateLeft.js#L9)  
引入版本：3.0.0


---

### RotateMatrix {#RotateMatrix}

#### \<static> RotateMatrix([matrix], [direction]) {#static-rotatematrixmatrix-direction}


**说明:**

根据给定的旋转值旋转数组矩阵。

值可以给出度:90, -90,270, -270,180或 -180,或字符串命令:`rotateLeft`,`rotateRight`或`rotate180`.

根据[http://jsfiddle.net/MrPolywhirl/NH42z/](http://jsfiddle.net/MrPolywhirl/NH42z/)的常规.

矩阵是一个二维阵列(数组阵列),所有子阵列(数组)的长度都是一样的。 至少有两行。 这是示例矩阵 :

```
[
   [ 1, 1, 1, 1, 1, 1 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 2, 0, 1, 2, 0, 4 ],
   [ 2, 0, 3, 4, 0, 4 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 3, 3, 3, 3, 3, 3 ]
]
```

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| matrix | Array.\<Array.\<T>> | 是 |  | 要旋转的阵列 。 |
| direction | number \| string | 是 | 90 | 以 90、 -90、 270、 - 270、 180 或 -180 等度值旋转矩阵的量。 或 `rotateLeft`、 `rotateRight` 或 `rotate180` 的字符串命令。 如果给出了未识别值, 矩阵将不会旋转 。 |


**返回值:** Array.\<Array.\<T>> - 旋转矩阵。 源矩阵应该被丢弃, 用于返回矩阵 。


> 源码：[src/utils/array/matrix/RotateMatrix.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/matrix/RotateMatrix.js#L10)  
引入版本：3.0.0


---

### RotateRight {#RotateRight}

#### \<static> RotateRight([matrix], [amount]) {#static-rotaterightmatrix-amount}


**说明:**

将矩阵矩阵向右旋转90度(顺时针)。

矩阵是一个二维阵列(数组阵列),所有子阵列(数组)的长度都是一样的。 至少有两行。 这是示例矩阵 :

```
[
   [ 1, 1, 1, 1, 1, 1 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 2, 0, 1, 2, 0, 4 ],
   [ 2, 0, 3, 4, 0, 4 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 3, 3, 3, 3, 3, 3 ]
]
```

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| matrix | Array.\<Array.\<T>> | 是 |  | 要旋转的阵列 。 |
| amount | number | 是 | 1 | 顺时针旋转矩阵的次数 90 度 。 |


**返回值:** Array.\<Array.\<T>> - 旋转矩阵。 源矩阵应该被丢弃, 用于返回矩阵 。


> 源码：[src/utils/array/matrix/RotateRight.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/matrix/RotateRight.js#L9)  
引入版本：3.0.0


---

### Translate {#Translate}

#### \<static> Translate([matrix], [x], [y]) {#static-translatematrix-x-y}


**说明:**

通过按指定的数量来转换矩阵矩阵,将矩阵矩阵和每行中的元素转换成矩阵矩阵。翻译周期性地包起来:元素从矩阵的一个边缘上移出,在相反的边缘上重新出现。

正面`x`值将每行内的元素向右移动,负值将它们向左移动。正面`y`值将行向下移动,负值将这些元素向上移动。

矩阵是一个二维阵列(数组阵列),所有子阵列(数组)的长度都是一样的。 至少有两行。 这是示例矩阵 :

```
[
   [ 1, 1, 1, 1, 1, 1 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 2, 0, 1, 2, 0, 4 ],
   [ 2, 0, 3, 4, 0, 4 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 3, 3, 3, 3, 3, 3 ]
]
```

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| matrix | Array.\<Array.\<T>> | 是 |  | 要翻译的矩阵矩阵 。 |
| x | number | 是 | 0 | 水平翻译矩阵的金额 。 |
| y | number | 是 | 0 | 垂直翻译矩阵的金额。 |


**返回值:** Array.\<Array.\<T>> - 译经总目.


> 源码：[src/utils/array/matrix/TranslateMatrix.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/matrix/TranslateMatrix.js#L10)  
引入版本：3.50.0


---

### TransposeMatrix {#TransposeMatrix}

#### \<static> TransposeMatrix([array]) {#static-transposematrixarray}


**说明:**

转换给定矩阵的元素(数组阵列).

矩阵的转写是一个新的矩阵,其行是原矩阵的列.

矩阵是一个二维阵列(数组阵列),所有子阵列(数组)的长度相同。至少必须有一行。这是示例矩阵 :

```
[
   [ 1, 1, 1, 1, 1, 1 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 2, 0, 1, 2, 0, 4 ],
   [ 2, 0, 3, 4, 0, 4 ],
   [ 2, 0, 0, 0, 0, 4 ],
   [ 3, 3, 3, 3, 3, 3 ]
]
```

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | Array.\<Array.\<T>> | 是 | 换位的矩阵矩阵 。 |


**返回值:** Array.\<Array.\<T>> - 新的数组矩阵,它是给定数组的移植版本。


> 源码：[src/utils/array/matrix/TransposeMatrix.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/matrix/TransposeMatrix.js#L7)  
引入版本：3.0.0


---

---
