# Phaser.Utils.Array {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/utils-array)

Scope: 
static
> 源码：[src/utils/array/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/index.js#L7)  


## 静态函数 {#static-functions}

### Add {#Add}

#### \<static> Add(array, item, [limit], [callback], [context]) {#static-addarray-item-limit-callback-context}


**说明:**

将给定的项目,或项目数组添加到数组中。

每个项目必须在数组内独有.

阵列在位置上修改。 添加的项目或添加的项目数组会被返回。 如果没有添加项目, 返回 `null`( 例如, 阵列已经处于极限, 或者所有项目已经存在于阵列中 ) 。

您可以选择指定最大数组大小的限度。 如果所添加的项目数量将超过此限额, 则一旦达到限额, 将停止添加。

您可以选择为每个成功添加到数组的项目指定一个调用回调 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 要添加的数组 。 |
| item | any \| Array.\<any> | 否 | 添加到数组中的项,或数组。每个项必须是数组中唯一的。 |
| limit | number | 是 | 限制数组大小的可选限制 。 |
| callback | function | 是 | 每个项目都成功添加回调符。 |
| context | object | 是 | 引用回调时的上下文 。 |


**返回值:** array - 成功添加到阵列中的项目,或数组,如果没有添加的话,则使用`null`。


> 源码：[src/utils/array/Add.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/Add.js#L7)  
引入版本：3.4.0


---

### AddAt {#AddAt}

#### \<static> AddAt(array, item, [index], [limit], [callback], [context]) {#static-addatarray-item-index-limit-callback-context}


**说明:**

将给定的项目,或项目数组添加到从指定的索引开始的数组中。

每个项目必须在数组内独有.

阵列中的现有元素被向上移.

阵列在位置上被修改。 插入的项目或插入的项目数组返回。 如果未添加项目, 返回 `null`( 如阵列已满, 或所有项目已存在) 。

您可以选择指定最大数组大小的限度。 如果所添加的项目数量将超过此限额, 则一旦达到限额, 将停止添加。

您可以选择为每个成功添加到数组的项目指定一个调用回调 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| array | array | 否 |  | 要添加的数组 。 |
| item | any \| Array.\<any> | 否 |  | 将项目,或项目数组添加到数组中。 |
| index | number | 是 | 0 | 插入项目时的数组索引。 |
| limit | number | 是 |  | 限制数组大小的可选限制 。 |
| callback | function | 是 |  | 每个项目都成功添加回调符。 |
| context | object | 是 |  | 引用回调时的上下文 。 |


**返回值:** array - 成功插入的项目,或项目数组,或未添加的`null`。


> 源码：[src/utils/array/AddAt.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/AddAt.js#L7)  
引入版本：3.4.0


---

### BringToTop {#BringToTop}

#### \<static> BringToTop(array, item) {#static-bringtotoparray-item}


**说明:**

将给定的元素移动到数组的顶端。数组在位置上被修改。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 要修改的阵列 。 |
| item | * | 否 | 移动到数组顶端的元素 。 |


**返回值:** * - 移动的元素。


> 源码：[src/utils/array/BringToTop.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/BringToTop.js#L7)  
引入版本：3.4.0


---

### CountAllMatching {#CountAllMatching}

#### \<static> CountAllMatching(array, property, value, [startIndex], [endIndex]) {#static-countallmatchingarray-property-value-startindex-endindex}


**说明:**

返回数组中与给定值匹配的属性的元素总数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 要搜索的阵列 。 |
| property | string | 否 | 在每个阵列元素上测试的属性 。 |
| value | * | 否 | 对照属性测试值。 必须进行严格的( `===`) 比较检查 。 |
| startIndex | number | 是 | 搜索对象的可选起始索引 。 |
| endIndex | number | 是 | 要搜索的可选端索引 。 |


**返回值:** number - 属性与给定值匹配的元素总数 。


> 源码：[src/utils/array/CountAllMatching.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/CountAllMatching.js#L9)  
引入版本：3.4.0


---

### Each {#Each}

#### \<static> Each(array, callback, context, [args]) {#static-eacharray-callback-context-args}


**说明:**

将数组中的每个元素传递给给给定的回调。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 将阵列移到上面 |
| callback | function | 否 | 数组中每个项目都要引用回调 。 |
| context | object | 否 | 引用回调时的上下文 。 |
| args | * | 是 | 在当前数组项目之后, 将转到调用参数 。 |


**返回值:** array - 输入阵列 。


> 源码：[src/utils/array/Each.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/Each.js#L7)  
引入版本：3.4.0


---

### EachInRange {#EachInRange}

#### \<static> EachInRange(array, callback, context, startIndex, endIndex, [args]) {#static-eachinrangearray-callback-context-startindex-endindex-args}


**说明:**

将数组中的每个元素,介于起始索引和结尾索引之间,传递给给定的回调。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 将阵列移到上面 |
| callback | function | 否 | 数组中每个项目都要引用回调 。 |
| context | object | 否 | 引用回调时的上下文 。 |
| startIndex | number | 否 | 起始指数从。 |
| endIndex | number | 否 | 端指数到 |
| args | * | 是 | 更多论点,在孩子出生后,会转给回电者。 |


**返回值:** array - 输入阵列 。


> 源码：[src/utils/array/EachInRange.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/EachInRange.js#L9)  
引入版本：3.4.0


---

### FindClosestInSorted {#FindClosestInSorted}

#### \<static> FindClosestInSorted(value, array, [key]) {#static-findclosestinsortedvalue-array-key}


**说明:**

搜索一个与给定数字最接近的预排序数组。

如果给出了 `key` 参数,它会假设阵列中包含所有具有所需的 `key` 属性名称的对象,并且会检查这些对象与给定数字最近的值.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 数组中要搜索的值 。 |
| array | array | 否 | 要搜索的阵列, 必须排序 。 |
| key | string | 是 | 选项属性密钥。 如果指定数组元素的属性, 将对照值检查 。 |


**返回值:** number, any - 数组中找到的最近值,或者如果给出了`key`,则与匹配属性值最接近的对象.


> 源码：[src/utils/array/FindClosestInSorted.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/FindClosestInSorted.js#L7)  
引入版本：3.0.0


---

### Flatten {#Flatten}

#### \<static> Flatten(array, [output]) {#static-flattenarray-output}


**说明:**

取一个数组并深为平整, 递归地将任何嵌入的数组拆解成单个平整数组。 原数组没有修改。 可以提供可选的输出数组来收集结果, 当调用此函数时或当附加到已有数组时, 这样做很有用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 阵形以平. |
| output | array | 是 | 用于保存结果的阵列 。 |


**返回值:** array - 平整输出阵列 。


> 源码：[src/utils/array/Flatten.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/Flatten.js#L7)  
引入版本：3.60.0


---

### GetAll {#GetAll}

#### \<static> GetAll(array, [property], [value], [startIndex], [endIndex]) {#static-getallarray-property-value-startindex-endindex}


**说明:**

返回数组中的所有元素。

您可以选择使用 `property` 和 `value` 参数指定匹配标准 。

例如:`GetAll('visible', true)`只将那些其可见属性设定为`true`的元素还原.

选择时您可以指定一个起始和结束索引。 例如, 如果数组有100个元素, 您将 `startIndex` 设置为 0, `endIndex` 设置为 50, 它只会从前50个元素返回匹配 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 要搜索的阵列 。 |
| property | string | 是 | 在每个阵列元素上测试的属性 。 |
| value | * | 是 | 对照属性测试值。 必须进行严格的( `===`) 比较检查 。 |
| startIndex | number | 是 | 搜索对象的可选起始索引 。 |
| endIndex | number | 是 | 要搜索的可选端索引 。 |


**返回值:** array - 所有匹配的元素来自数组 。


> 源码：[src/utils/array/GetAll.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/GetAll.js#L9)  
引入版本：3.4.0


---

### GetFirst {#GetFirst}

#### \<static> GetFirst(array, [property], [value], [startIndex], [endIndex]) {#static-getfirstarray-property-value-startindex-endindex}


**说明:**

返回数组中的第一元素。

您可以选择使用 `property` 和 `value` 参数指定匹配标准 。

例如:`GetFirst('visible', true)`会将第一个将它的`visible`属性设定为`true`的元素还原.

选择时您可以指定一个起始和结束索引。 例如, 如果阵列有100个元素, 您将 `startIndex` 设置为 0, `endIndex` 设置为 50, 它只会搜索前50个元素 。

您也可以指定一个负的 `startIndex`, 如 `-1`, 可以在阵列的末尾开始搜索

您也可以指定一个负的 `startIndex`, 如 `-1`, 可以在阵列的末尾开始搜索

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| array | array | 否 |  | 要搜索的阵列 。 |
| property | string | 是 |  | 在每个阵列元素上测试的属性 。 |
| value | * | 是 |  | 对照属性测试值。 必须进行严格的( `===`) 比较检查 。 |
| startIndex | number | 是 | 0 | 搜索的可选启动索引。 您也可以将 `startIndex` 设置为 - 1 , 以便从阵列的末尾开始搜索 。 |
| endIndex | number | 是 | "array.length" | 搜索到( 但不包含) 的可选结尾索引 |


**返回值:** object - 如果在给定的范围内找不到元素, 则来自数组的第一个匹配元素, 或是 `null` 。


> 源码：[src/utils/array/GetFirst.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/GetFirst.js#L9)  
引入版本：3.4.0


---

### GetRandom {#GetRandom}

#### \<static> GetRandom(array, [startIndex], [length]) {#static-getrandomarray-startindex-length}


**说明:**

从数组返回随机元素。

**Tags:**

 - generic
 - genericUse
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| array | Array.\<T> | 否 |  | 随机选择条目的数组。 |
| startIndex | number | 是 | 0 | 选择的启动索引 。 |
| length | number | 是 | "array.length" | 可选长度,从startIndex中选择的元素总数. |


**返回值:** T - 如果在给定的范围内找不到元素, 则从数组中随机生成元素, 或是 `null` 。


> 源码：[src/utils/array/GetRandom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/GetRandom.js#L7)  
引入版本：3.0.0


---

### MoveAbove {#MoveAbove}

#### \<static> MoveAbove(array, item1, item2) {#static-moveabovearray-item1-item2}


**说明:**

将给定的数组元素移到数组中的另一个元素上方。 如果给定的元素已经移到另一个元素上方, 它就不会移动。 上面意味着移到数组的末尾。 数组会在位置上修改 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 输入阵列 。 |
| item1 | * | 否 | 移动到基元素之上的元素. |
| item2 | * | 否 | 基点元素. |


**返回值:** array - 输入阵列 。


> 源码：[src/utils/array/MoveAbove.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/MoveAbove.js#L7)  
引入版本：3.55.0


---

### MoveBelow {#MoveBelow}

#### \<static> MoveBelow(array, item1, item2) {#static-movebelowarray-item1-item2}


**说明:**

将给定的数组元素移到数组中的另一个元素下方。 如果给定的元素已经移到另一个元素下方, 则它不会移动。 下面意味着数组的开始。 数组在位置上被修改 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 输入阵列 。 |
| item1 | * | 否 | 基元素以下移动的元素 。 |
| item2 | * | 否 | 基点元素. |


**返回值:** array - 输入阵列 。


> 源码：[src/utils/array/MoveBelow.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/MoveBelow.js#L7)  
引入版本：3.55.0


---

### MoveDown {#MoveDown}

#### \<static> MoveDown(array, item) {#static-movedownarray-item}


**说明:**

将给定的数组元素下移到数组中一个位置。数组在位置上被修改。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 输入阵列 。 |
| item | * | 否 | 下移数组的元素 。 |


**返回值:** array - 输入数组, 随物品移动到一个地方 。


> 源码：[src/utils/array/MoveDown.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/MoveDown.js#L7)  
引入版本：3.4.0


---

### MoveTo {#MoveTo}

#### \<static> MoveTo(array, item, index) {#static-movetoarray-item-index}


**说明:**

将数组中的元素移动到同一数组中的新位置。该数组在位置上被修改。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 阵列. |
| item | * | 否 | 移动的元素 。 |
| index | number | 否 | 元素将移动到的新索引 。 |


**返回值:** * - 移动的元素。


> 源码：[src/utils/array/MoveTo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/MoveTo.js#L7)  
引入版本：3.4.0


---

### MoveUp {#MoveUp}

#### \<static> MoveUp(array, item) {#static-moveuparray-item}


**说明:**

将给定的数组元素上移到数组中的一个位置。数组在位置上被修改 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 输入阵列 。 |
| item | * | 否 | 向上移动数组的元素 。 |


**返回值:** array - 输入阵列 。


> 源码：[src/utils/array/MoveUp.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/MoveUp.js#L7)  
引入版本：3.4.0


---

### NumberArray {#NumberArray}

#### \<static> NumberArray(start, end, [prefix], [suffix]) {#static-numberarraystart-end-prefix-suffix}


**说明:**

创建一个数组,代表给定的 `start` 和 `end` 参数之间的数字范围(通常是整数) 。 例如:

`var array = Phaser.Utils.Array.NumberArray(2, 4); // array = [2, 3, 4]` `var array = Phaser.Utils.Array.NumberArray(0, 9); // array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` `var array = Phaser.Utils.Array.NumberArray(8, 2); // array = [8, 7, 6, 5, 4, 3, 2]`

这相当于`Phaser.Utils.Array.NumberArrayStep(start, end, 1)`.

您可以选择提供前缀和/ 或后缀字符串。 如果给定数组将包含字符串, 而不是整数。 例如 :

`var array = Phaser.Utils.Array.NumberArray(1, 4, 'Level '); // array = ["Level 1", "Level 2", "Level 3", "Level 4"]` `var array = Phaser.Utils.Array.NumberArray(5, 7, 'HD-', '.png'); // array = ["HD-5.png", "HD-6.png", "HD-7.png"]`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| start | number | 否 | 数组起始的最小值 。 |
| end | number | 否 | 数组包含的最大值 。 |
| prefix | string | 是 | 可选的前缀放在数字之前。 如果提供数组将包含字符串, 而不是整数 。 |
| suffix | string | 是 | 可选的后缀, 以在数字后放置。 如果提供数组将包含字符串, 而不是整数 。 |


**返回值:** Array.\<number>, Array.\<string> - 数字值的数组,或者如果提供了前缀或后缀的话的字符串。


> 源码：[src/utils/array/NumberArray.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/NumberArray.js#L7)  
引入版本：3.0.0


---

### NumberArrayStep {#NumberArrayStep}

#### \<static> NumberArrayStep([start], [end], [step]) {#static-numberarraystepstart-end-step}


**说明:**

通过`step`的推进,创建一系列从`start`到但不包括`end`的(正数和/或负数)进步.

如果 `start`大于 `end`,则创建了零长范围,除非指定负的 `step`.

`start`和`end`的某些值(如NaN/underfinding/null)目前被强制为0;对于前置兼容性,确保通过实际数字。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| start | number | 是 | 0 | 范围开始。 |
| end | number | 是 | null | 范围结束。 |
| step | number | 是 | 1 | 递增或递减的值。 |


**返回值:** Array.\<number> - 数字值的数组。


> 源码：[src/utils/array/NumberArrayStep.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/NumberArrayStep.js#L9)  
引入版本：3.0.0


---

### QuickSelect {#QuickSelect}

#### \<static> QuickSelect(arr, k, [left], [right], [compare]) {#static-quickselectarr-k-left-right-compare}


**说明:**

一个[Floyd-Rivest](https://en.wikipedia.org/wiki/Floyd%E2%80%93Rivest_algorithm)快速选择算法.

重新排列数组项,使[左,k]范围内的所有项都比[k,右]中的所有项小; k-th元素在[左,右]中将拥有最小值的(k-左+1).

阵列在原位内修改 。

根据[Vladimir Agafonkin](https://www.npmjs.com/~mourner)的代码

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| arr | array | 否 |  | 重新排列位置的阵列 。 |
| k | number | 否 |  | K-th元素指数. |
| left | number | 是 | 0 | 范围左侧部分的索引 。 |
| right | number | 是 |  | 范围右侧部分的索引. |
| compare | function | 是 |  | 一个可选比较函数。是两个元素的通过,如果第一个元素少于第二个,则应当返回负数,如果相等,则返回0,如果第一个元素大于正数,则返回正数。 |


> 源码：[src/utils/array/QuickSelect.js#L25](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/QuickSelect.js#L25)  
引入版本：3.0.0


---

### Range {#Range}

#### \<static> Range(a, b, [options]) {#static-rangea-b-options}


**说明:**

根据给定的参数和配置对象创建包含一系列数值的阵列。

范围([a,b,c],[1,2,3])=a1,a2,a3,b1,b2,b3,c1,c2,c3

范围([a,b],[1,2,3],qty=3]=a1,a1,a1,a2,a2,a3,a3,a3,b1,b1,b2,b2,b2,b3,b3)

范围([a,b,c],[1,2,3],重复x1]=a1,a2,a3,b1,b2,b3,c1,c2,c3,a1,a2,a3,b1,b2,b3,c1,c2,c3) 范围(a,b2,b2,b2,b2,b2,b2,b2,b2) 范围(a,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b,b2,b,b1,b,b1,b,b,b1,b,b,b1,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,

范围([a,b],[1,2],重复 -1=无穷,最大=14)=a1,a2,b1,b2,a1,a2,b1,b2,a1,a2,b1,b2,a1,a2(封装为14个元素) 范围(封装为14个元素) 范围(A1,b2,b2,b2,b2,b2,a1,a2) 范围(A1,b2,b2,b2,b2,b2,a1,a2) 范围(封装为14个元素) 范围(A1,b1,b1,b1,b1,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b,b,b2,b,b2,b2,b,b,b,b2,b,b2,b,b,b,b,b,b2,b,b,b,b1,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b

范围([a],[1,2,3,4,5],随机=真)=a4,a1,a5,a2,a3

范围([a,b],[1,2,3],随机=真实)=b3,a2,a1,b1,a3,b2

范围([a,b,c],[1,2,3],randomB=真)=a3,a1,a2,b2,b3,b1,c1,c3,c2

范围([a],[1,2,3,4,5],yoyo = true)=a1,a2,a3,a4,a5,a4,a5,a4,a3,a2,a1

范围([a,b],[1,2,3],yoyo=real)=a1,a2,a3,b1,b2,b3,b3,b2,b1,a3,a2,a1) 范围(a,b2,a2,a1) 范围(a,b2,b2,b2,b2,b1,a2,a1) 范围(a,a2,a2,a2,a2,a2) 范围(a,a2,a2,a2,a2,a2,a2,a2) 范围(a,a,a2,a2,a,a2,a2,b2,b2,b,b2,b2,b2,b2,b2,b2,b2,b2,b1,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b2,b,b2,b2,b2,b2,a2,a2,a1,a1,b,a1,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | array | 否 | 范围元素的第一阵列. |
| b | array | 否 | 第二组范围元素. |
| options | object | 是 | 范围配置对象。 支持以下属性 : `qty` (每对重复次数,默认次数1), `repeat` (整个范围的重复次数,无穷使用 -1), `random` (舒动整个输出阵列), `randomB` (摇摆阵列) `b` 在建对之前 `yoyo` (在前方通过后反向添加射程), `max` (以产出中元素总数为首). |


**返回值:** array - 由两个输入阵列的笛卡尔产品所构建的`{ a, b }`对对象阵列,按照给定的选项排列.


> 源码：[src/utils/array/Range.js#L28](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/Range.js#L28)  
引入版本：3.0.0


---

### Remove {#Remove}

#### \<static> Remove(array, item, [callback], [context]) {#static-removearray-item-callback-context}


**说明:**

从数组中删除给定的项目,或项目数组。

阵列在原位内修改 。

您可以选择为成功从数组中删除的每个项目指定一个调用符。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 需要修改的阵列 。 |
| item | * \| Array.\<*> | 否 | 拟从数组中删除的项目,或数组项目。 |
| callback | function | 是 | 成功从数组中移除的每个项目, 将引用回调 。 |
| context | object | 是 | 引用回调时的上下文 。 |


**返回值:** *, Array.\<*> - 成功从阵列中移除的项,或数组项。


> 源码：[src/utils/array/Remove.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/Remove.js#L9)  
引入版本：3.4.0


---

### RemoveAt {#RemoveAt}

#### \<static> RemoveAt(array, index, [callback], [context]) {#static-removeatarray-index-callback-context}


**说明:**

从数组中给定的位置删除项目。

阵列在原位内修改 。

您可以选择指定一个调用符, 如果该选项从数组中成功删除的话。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 需要修改的阵列 。 |
| index | number | 否 | 删除项目时的数组索引。 索引必须包含在界限内, 否则会出错 。 |
| callback | function | 是 | 调用以调用从数组中删除的项目 。 |
| context | object | 是 | 引用回调时的上下文 。 |


**返回值:** * - 被移除的物品。


> 源码：[src/utils/array/RemoveAt.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/RemoveAt.js#L9)  
引入版本：3.4.0


---

### RemoveBetween {#RemoveBetween}

#### \<static> RemoveBetween(array, startIndex, endIndex, [callback], [context]) {#static-removebetweenarray-startindex-endindex-callback-context}


**说明:**

删除给定索引中从数组中的所有项目。

阵列在原位内修改 。

您可以选择为成功删除数组的项目指定一个调用符 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 需要修改的阵列 。 |
| startIndex | number | 否 | 起始索引要删除 。 |
| endIndex | number | 否 | 最多删除( 排他性) 的结束索引 。 |
| callback | function | 是 | 成功从数组中移除的每个项目, 将引用回调 。 |
| context | object | 是 | 引用回调时的上下文 。 |


**返回值:** Array.\<*> - 被移除的一系列项目 。


> 源码：[src/utils/array/RemoveBetween.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/RemoveBetween.js#L9)  
引入版本：3.4.0


---

### RemoveRandomElement {#RemoveRandomElement}

#### \<static> RemoveRandomElement(array, [start], [length]) {#static-removerandomelementarray-start-length}


**说明:**

从给定数组中删除随机对象并返回。如果没有属于指定范围的数组项目,或者没有随机选择的索引项目,则返回无效。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| array | array | 否 |  | 从随机元素中移除的数组 。 |
| start | number | 是 | 0 | 启动搜索的阵列索引 。 |
| length | number | 是 | "array.length" | 可选限制元素数量随机选择从中选择. |


**返回值:** object - 被删除的随机元素,或者如果没有属于指定范围的数组元素,则使用 `null` 。


> 源码：[src/utils/array/RemoveRandomElement.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/RemoveRandomElement.js#L9)  
引入版本：3.0.0


---

### Replace {#Replace}

#### \<static> Replace(array, oldChild, newChild) {#static-replacearray-oldchild-newchild}


**说明:**

用新元素替换数组的元素。新元素不能已经是数组的成员。该数组在位置上被修改。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 搜索的阵列 。 |
| oldChild | * | 否 | 将替换的数组中的元素 。 |
| newChild | * | 否 | 将插入`oldChild`位置的阵列的元素。 |


**返回值:** boolean - 如果 oldChild 成功替换, 返回真, 否则返回假 。


> 源码：[src/utils/array/Replace.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/Replace.js#L7)  
引入版本：3.4.0


---

### RotateLeft {#RotateLeft}

#### \<static> RotateLeft(array, [total]) {#static-rotateleftarray-total}


**说明:**

将数组起始的元素移到尾部,将进程的所有项目移到尾部。“旋转”发生在左边。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| array | array | 否 |  | 向左移动的阵列。 此阵列已被修改 。 |
| total | number | 是 | 1 | 移转数组的次数 。 |


**返回值:** * - 最近改变的元素。


> 源码：[src/utils/array/RotateLeft.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/RotateLeft.js#L7)  
引入版本：3.0.0


---

### RotateRight {#RotateRight}

#### \<static> RotateRight(array, [total]) {#static-rotaterightarray-total}


**说明:**

将数组末尾的元素移动到起始处,将进程的所有项目都移到开始处。“旋转”发生在右边。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| array | array | 否 |  | 向右移动的数组。 此数组已被修改 。 |
| total | number | 是 | 1 | 移转数组的次数 。 |


**返回值:** * - 最近改变的元素。


> 源码：[src/utils/array/RotateRight.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/RotateRight.js#L7)  
引入版本：3.0.0


---

### SafeRange {#SafeRange}

#### \<static> SafeRange(array, startIndex, endIndex, [throwError]) {#static-saferangearray-startindex-endindex-throwerror}


**说明:**

如果起始和结束索引定义了给定数组内一个有效、安全的范围,则进行测试。

当`startIndex`为零或更大,`startIndex`小于`endIndex`时,一个范围被认为是安全的,`endIndex`不会超过阵列的长度.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| array | array | 否 |  | 要检查的阵列 。 |
| startIndex | number | 否 |  | 范围包含的起始索引。 必须是0 或大于 `endIndex` 。 |
| endIndex | number | 否 |  | 区域独家端索引。 范围必须大于 `startIndex` , 且不大于数组长度 。 |
| throwError | boolean | 是 | false | 如果 `true`,则在射程超出范围时,而非返回 `false`时,会抛出一个 `Range Error`. |


**返回值:** boolean - 如果范围安全,否则会错


> 源码：[src/utils/array/SafeRange.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/SafeRange.js#L7)  
引入版本：3.4.0


---

### SendToBack {#SendToBack}

#### \<static> SendToBack(array, item) {#static-sendtobackarray-item}


**说明:**

将给定的元素移到数组的底部( 索引 0 ) , 将所有其他元素上移到一个位置。 数组在位置上被修改。 如果元素未在数组中找到, 或者已经处于索引 0, 则数组保持不变 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 搜索和修改的阵列 。 |
| item | * | 否 | 移动到数组底部的元素。 |


**返回值:** * - 移动的元素。


> 源码：[src/utils/array/SendToBack.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/SendToBack.js#L7)  
引入版本：3.4.0


---

### SetAll {#SetAll}

#### \<static> SetAll(array, property, value, [startIndex], [endIndex]) {#static-setallarray-property-value-startindex-endindex}


**说明:**

扫描带有给定属性的元素的数组。如果找到,属性将被设定为 `value` 。

例如:`SetAll(array, 'visible', true)`会将所有具有`visible`属性的元素设置为`true`.

选择时您可以指定起始和结束索引。 例如, 如果阵列有100个元素, 您将 `startIndex` 设置为 0, `endIndex` 设置为 50, 它只会更新前50个元素 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 要搜索的阵列 。 |
| property | string | 否 | 用于测试每个数组元素的属性 。 |
| value | * | 否 | 设置属性的值 。 |
| startIndex | number | 是 | 搜索对象的可选起始索引 。 |
| endIndex | number | 是 | 要搜索的可选端索引 。 |


**返回值:** array - 输入阵列 。


> 源码：[src/utils/array/SetAll.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/SetAll.js#L9)  
引入版本：3.4.0


---

### Shuffle {#Shuffle}

#### \<static> Shuffle(array) {#static-shufflearray}


**说明:**

使用 Fisher-Yates 执行来混淆给定数组的内容。

原阵列直接修改后返回.

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | Array.\<T> | 否 | 正在修改该阵列 。 |


**返回值:** Array.\<T> - 洗涤的阵列。


> 源码：[src/utils/array/Shuffle.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/Shuffle.js#L7)  
引入版本：3.0.0


---

### SortByDigits {#SortByDigits}

#### \<static> SortByDigits(array) {#static-sortbydigitsarray}


**说明:**

取下给定数组并运行其上的数字排序,忽略条目中可能包含的任何非数字。

您只应在包含字符串的数组中运行 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | Array.\<string> | 否 | 字符串的输入数组 。 |


**返回值:** Array.\<string> - 排序的输入数组 。


> 源码：[src/utils/array/SortByDigits.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/SortByDigits.js#L7)  
引入版本：3.50.0


---

### SpliceOne {#SpliceOne}

#### \<static> SpliceOne(array, index) {#static-spliceonearray-index}


**说明:**

从数组中删除单个项目,然后在不创建gc的情况下返回,就像本地的切片一样。基于Mike Reinstein的代码。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 组合的组合 |
| index | number | 否 | 需要分解的项目索引 。 |


**返回值:** * - 被切除(删除)的物品。


> 源码：[src/utils/array/SpliceOne.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/SpliceOne.js#L7)  
引入版本：3.0.0


---

### StableSort {#StableSort}

#### \<static> StableSort(array, [compare]) {#static-stablesortarray-compare}


**说明:**

一种在位稳定阵列类型,因为`Array#sort()`不能保证稳定.

这是合并的分类, 不再重复 。

基于 [https://github.com/Two-Screen/stable](https://github.com/Two-Screen/stable) 中的双层/稳定排序0.1.8的函数

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 要排序的输入数组 。 |
| compare | function | 是 | 比较功能. |


**返回值:** array - 排序结果 。


> 源码：[src/utils/array/StableSort.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/StableSort.js#L142)  
引入版本：3.0.0


---

### Swap {#Swap}

#### \<static> Swap(array, item1, item2) {#static-swaparray-item1-item2}


**说明:**

交换给定数组中两个元素的位置。 元素必须在同一数组中存在。 数组在位置上被修改 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| array | array | 否 | 输入阵列 。 |
| item1 | * | 否 | 第一个交换的元素。 |
| item2 | * | 否 | 换掉的第二个元素。 |


**返回值:** array - 输入阵列 。


> 源码：[src/utils/array/Swap.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/array/Swap.js#L7)  
引入版本：3.4.0


---

## 静态函数 {#static-functions-1}

- [Matrix](/api/namespace/utils-array-matrix)

---
