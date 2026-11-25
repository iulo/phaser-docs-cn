# Phaser.Math.Fuzzy {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-fuzzy)

Scope: 
static
> 源码：[src/math/fuzzy/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/fuzzy/index.js#L7)  


## 静态函数 {#static-functions}

### Ceil {#Ceil}

#### \<static> Ceil(value, [epsilon]) {#static-ceilvalue-epsilon}


**说明:**

计算给定值的模糊上限 。

将数值四舍五入到最近的整数,但在应用 `Math.ceil` 之前减去一个小的 epsiloon 容积。这意味着,数值略高于整数边界(在 epsiloon 在 epsilon 范围内) 会被当做它们完全位于该边界上,避免浮点精度错误,否则会意外地将结果推到下一个整数。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 计算模糊天花板的值 。 |
| epsilon | number | 是 | 0.0001 | epsilon的容性用来减少浮点精度错误. |


**返回值:** number - 值的模糊天花板。


> 源码：[src/math/fuzzy/Ceil.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/fuzzy/Ceil.js#L7)  
引入版本：3.0.0


---

### Equal {#Equal}

#### \<static> Equal(a, b, [epsilon]) {#static-equala-b-epsilon}


**说明:**

检查给定的值是否模糊地相等 。

如果两者的差值小于`epsilon`,则两者模糊相等。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| a | number | 否 |  | 初标值. |
| b | number | 否 |  | 第二义值. |
| epsilon | number | 是 | 0.0001 | 两者数值下方最大绝对差值相等. |


**返回值:** boolean - 如果数值模糊,则使用`true`,否则使用`false`。


> 源码：[src/math/fuzzy/Equal.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/fuzzy/Equal.js#L7)  
引入版本：3.0.0


---

### Floor {#Floor}

#### \<static> Floor(value, [epsilon]) {#static-floorvalue-epsilon}


**说明:**

通过在下架前添加一个小的epsilon来计算给定值的模糊底。这样可以避免浮点精度问题,因为数学上应该是一个整数(如2.99999999)的值会错转到下面的整数。下一轮整数上方的epsilon内的任何值都会被下调到整数。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 计算模糊底部的值。 |
| epsilon | number | 是 | 0.0001 | epsilon 值。 下个整数的距离内值被下调到整数。 |


**返回值:** number - 给定值的模糊层.


> 源码：[src/math/fuzzy/Floor.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/fuzzy/Floor.js#L7)  
引入版本：3.0.0


---

### GreaterThan {#GreaterThan}

#### \<static> GreaterThan(a, b, [epsilon]) {#static-greaterthana-b-epsilon}


**说明:**

检查`a`是否模糊大于`b`.

`a`如果大于`b - epsilon`,则模糊度大于`b`.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| a | number | 否 |  | 初标值. |
| b | number | 否 |  | 第二义值. |
| epsilon | number | 是 | 0.0001 | 用于控制模糊度的 epsiron 值。 更大的值使比较更加宽松 。 |


**返回值:** boolean - `true` 如果出现 `a` 模糊的大于 `b`,否则 `false`.


> 源码：[src/math/fuzzy/GreaterThan.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/fuzzy/GreaterThan.js#L7)  
引入版本：3.0.0


---

### LessThan {#LessThan}

#### \<static> LessThan(a, b, [epsilon]) {#static-lessthana-b-epsilon}


**说明:**

检查`a`是否模糊小于`b`.

`a` 模糊度小于 `b` 如果它小于 `b + epsilon`.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| a | number | 否 |  | 初标值. |
| b | number | 否 |  | 第二义值. |
| epsilon | number | 是 | 0.0001 | 模糊比较所用的容积值。 此距离内的值被认为是相等的 。 |


**返回值:** boolean - `true` 如果出现 `a` 模糊度小于 `b`,否则 `false`.


> 源码：[src/math/fuzzy/LessThan.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/fuzzy/LessThan.js#L7)  
引入版本：3.0.0


---

---
