# Phaser.Math.Pow2 {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-pow2)

Scope: 
static
> 源码：[src/math/pow2/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/pow2/index.js#L7)  


## 静态函数 {#static-functions}

### GetPowerOfTwo {#GetPowerOfTwo}

#### \<static> GetPowerOfTwo(value) {#static-getpoweroftwovalue}


**说明:**

返回大于或等于给定的 `value` 的最小功率 2 。 例如, 值 7 返回 8 , 值 8 返回 8 , 9 返回 16 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 找到下一个 2 的 值应该是正数 。 |


**返回值:** number - 2的最小功率大于或等于`value`.


> 源码：[src/math/pow2/GetPowerOfTwo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/pow2/GetPowerOfTwo.js#L7)  
引入版本：3.0.0


---

### IsSize {#IsSize}

#### \<static> IsSize(width, height) {#static-issizewidth-height}


**说明:**

检查给定的 `width`和 `height` 是否具有两个功率。 用于检查纹理尺寸 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 要检查的宽度, 以像素计 。 |
| height | number | 否 | 要检查的高度, 以像素表示 。 |


**返回值:** boolean - `true` 如果出现 `width` 财务报告和已审计财务报表 `height` 是一种二强的力量,否则 `false`.


> 源码：[src/math/pow2/IsSizePowerOfTwo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/pow2/IsSizePowerOfTwo.js#L7)  
引入版本：3.0.0


---

### IsValue {#IsValue}

#### \<static> IsValue(value) {#static-isvaluevalue}


**说明:**

如果值为2,则测试值并返回`true`。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 值以验其有无二力. |


**返回值:** boolean - 如果`value`是2的功率,则返回`true`,否则返回`false`.


> 源码：[src/math/pow2/IsValuePowerOfTwo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/pow2/IsValuePowerOfTwo.js#L7)  
引入版本：3.0.0


---

---
