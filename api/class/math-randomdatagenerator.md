# RandomDataGenerator {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/math-randomdatagenerator)

种子随机数据生成器.

通过 `Phaser.Math.RND` 访问, 是 Phaser 预先定义的类的示例。 或者, 创建您自己的实例, 以便按您需要使用 。

`Math.RND`生成器由 Game Config 属性值 `seed` 种子。如果没有这样的配置属性,则使用随机数字 。

如果您创建了本类的自己实例, 您应该为此提供种子。 如果没有种子, 它将使用基于 Date. now 的“ 随机” 。

**构造函数**

`new RandomDataGenerator([seeds])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| seeds | string \| Array.\<string> | 是 | 随机数生成器所用的种子 。 |

---


**作用域**: static

> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L9)  
引入版本：3.0.0

## 公开成员 {#public-members}

### signs {#signs}

#### signs: Array.\<number> {#signs-arraynumber}


**说明:**

标志要选择。


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L92)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### angle {#angle}

#### \<instance> angle() {#instance-angle}


**说明:**

返回一个随机角度, 以度计, 在 -180 和 180 之间 。


**返回值:** number - 随机整数角的度,在 -180 至 180 之间.


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L413](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L413)  
引入版本：3.0.0


---

### between {#between}

#### \<instance> between(min, max) {#instance-betweenmin-max}


**说明:**

返回一个在分钟和最大值之间和包含的随机整数。这种方法是RandomDataGenerator.integerInRange的别名。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| min | number | 否 | 最小值在范围。 |
| max | number | 否 | 最大值在范围中。 |


**返回值:** number - 分钟到最大值之间的随机数字 。


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L278](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L278)  
引入版本：3.0.0


---

### frac {#frac}

#### \<instance> frac() {#instance-frac}


**说明:**

返回 0 到 1 之间的随机真实数字 。


**返回值:** number - 0到1之间的随机实数.


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L235](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L235)  
引入版本：3.0.0


---

### init {#init}

#### \<instance> init(seeds) {#instance-initseeds}


**说明:**

初始化随机数据生成器的状态 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| seeds | string \| Array.\<string> | 否 | 种子以初始化随机数据生成器 。 |


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L163](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L163)  
引入版本：3.0.0


---

### integer {#integer}

#### \<instance> integer() {#instance-integer}


**说明:**

返回 0 和 2^32 之间的随机整数。


**返回值:** number - 0到2^32之间的随机整数.


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L221](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L221)  
引入版本：3.0.0


---

### integerInRange {#integerInRange}

#### \<instance> integerInRange(min, max) {#instance-integerinrangemin-max}


**说明:**

返回一个在分钟和最大值之间并包含的随机整数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| min | number | 否 | 最小值在范围。 |
| max | number | 否 | 最大值在范围中。 |


**返回值:** number - 分钟到最大值之间的随机数字 。


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L262](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L262)  
引入版本：3.0.0


---

### normal {#normal}

#### \<instance> normal() {#instance-normal}


**说明:**

返回 -1 和 1 之间的随机实数 。


**返回值:** number - 随机真实数字在 -1 和 1 之间 。


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L311](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L311)  
引入版本：3.0.0


---

### pick {#pick}

#### \<instance> pick(array) {#instance-pickarray}


**说明:**

从给定数组中返回随机元素。

**Tags:**

 - generic
 - genericUse
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | Array.\<T> | 否 | 随机元素的矩阵 。 |


**返回值:** T - 随机数组成员.


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L345](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L345)  
引入版本：3.0.0


---

### real {#real}

#### \<instance> real() {#instance-real}


**说明:**

返回 0 到 2^32 之间的随机实数 。


**返回值:** number - 0到2^32之间的随机实数.


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L249](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L249)  
引入版本：3.0.0


---

### realInRange {#realInRange}

#### \<instance> realInRange(min, max) {#instance-realinrangemin-max}


**说明:**

返回分钟至最大值之间的随机实数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| min | number | 否 | 最小值在范围。 |
| max | number | 否 | 最大值在范围中。 |


**返回值:** number - 分钟到最大值之间的随机数字 。


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L295](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L295)  
引入版本：3.0.0


---

### rotation {#rotation}

#### \<instance> rotation() {#instance-rotation}


**说明:**

返回到-3.1415926至3.1415926(约-  至  )之间的弧度随机旋转.


**返回值:** number - 随机实数的弧度,介于 -3.1415926 至 3.1415926之间.


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L426](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L426)  
引入版本：3.0.0


---

### shuffle {#shuffle}

#### \<instance> shuffle([array]) {#instance-shufflearray}


**说明:**

使用当前种子来调整给定的阵列。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | Array.\<T> | 是 | 要洗涤的阵列 。 |


**返回值:** Array.\<T> - 洗涤的阵列。


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L474](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L474)  
引入版本：3.7.0


---

### sign {#sign}

#### \<instance> sign() {#instance-sign}


**说明:**

返回随机选择的标志值, 要么是 - 1 要么是+1. 用于乘以任意翻转一个值的方向, 例如随机地将水平或垂直移动 。


**返回值:** number - -1或+1 (双倍) - 或+1 (双双双双双双) 。


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L364](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L364)  
引入版本：3.0.0


---

### sow {#sow}

#### \<instance> sow(seeds) {#instance-sowseeds}


**说明:**

重置随机数据生成器的种子 。

_Note_:种子阵列的处理量只有第一个`undefined`(或`null`)值,如果存在的话。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| seeds | Array.\<string> | 否 | 种子的阵列:使用每个值的`toString()`. |


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L183](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L183)  
引入版本：3.0.0


---

### state {#state}

#### \<instance> state([state]) {#instance-statestate}


**说明:**

获取或设定生成器状态。这使得您可以保留生成器在游戏间使用的值,即在游戏保存文件中使用。

要用先前保存的状态来种子此生成器, 您可以在游戏配置中以 `seed` 值通过它, 或者在 Phaser 启动后直接调用此方法 。

调用此方法, 没有参数可以返回当前状态 。

如果提供状态, 它应该与这个方法返回的格式相同, 因为它是一个带有标题的字符串 `!rnd` 之后是 `c`, `s0`, `s1` 财务报告和已审计财务报表 `s2` 值,每个逗号限制。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| state | string | 是 | 发电机状态待设定 。 |


**返回值:** string - 生成器的当前状态 。


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L439](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L439)  
引入版本：3.0.0


---

### timestamp {#timestamp}

#### \<instance> timestamp(min, max) {#instance-timestampmin-max}


**说明:**

如果未指定分钟和最大值,则返回一个在分钟和最大值之间的随机时间戳,或者在2000年初至2020年底之间。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| min | number | 否 | 最小值在范围。 |
| max | number | 否 | 最大值在范围中。 |


**返回值:** number - 分钟到最大时间间隔间随机时间戳.


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L397](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L397)  
引入版本：3.0.0


---

### uuid {#uuid}

#### \<instance> uuid() {#instance-uuid}


**说明:**

从 [https://gist.github.com/1308368](https://gist.github.com/1308368) 返回有效的 RFC4122 版本 4 ID 十六进制字符串


**返回值:** string - 有效的 RFC4122 版本4 ID 十六进制字符串


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L324](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L324)  
引入版本：3.0.0


---

### weightedPick {#weightedPick}

#### \<instance> weightedPick(array) {#instance-weightedpickarray}


**说明:**

从给定数组中返回随机元素, 并偏向先前的条目 。

**Tags:**

 - generic
 - genericUse
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | Array.\<T> | 否 | 随机元素的矩阵 。 |


**返回值:** T - 随机数组成员.


> 源码：[src/math/random-data-generator/RandomDataGenerator.js#L378](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/random-data-generator/RandomDataGenerator.js#L378)  
引入版本：3.0.0


---

---
