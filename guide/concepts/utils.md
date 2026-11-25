# 实用工具 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/utils)

Phaser收集了提供各种功能的公用功能和辅助器类,设计简化了共同的任务.

## Phaser.Utils.Array {#phaserutilsarray}

提供各种用于处理阵列的实用方法。

### 添加元素 {#adding-elements}

- 将项目添加到数组中。

  ```js
  Add(array, item, [limit], [callback], [context]);
  ```

  - `item`: 添加到数组中的项目, 或数组。 每个项目必须是在数组中独有的 。
  - 可选 `limit`: 限制阵列大小的可选限制 。
  - 可选 `callback` : 每个项目要被成功添加到数组中, 引用回调 。
  - 可选 `context`: 引用回调时的上下文.

  示例

  ```js
  let array = [1, 2, 3];
  Phaser.Utils.Array.Add(array, 4); // Adds 4 to the array
  console.log(array); // [1, 2, 3, 4]
  ```

- 在指定的索引中添加一个项目到数组中。

  ```js
  let array = [1, 2, 3];
  Phaser.Utils.Array.AddAt(array, 4, 1); // Inserts 4 at index 1
  console.log(array); // [1, 4, 2, 3]
  ```

### 删除元素 {#removing-elements}

- 从数组中删除指定项目的首次出现。

  ```js
  Remove(array, item, [callback], [context]);
  ```

  - `item`:要从阵列中移除的项目,或项目数组。
  - 可选 `callback` : 成功从阵列中删除的每个项目, 将引用回调 。
  - 可选 `context`: 引用回调时的上下文.

  示例

  ```js
  let array = [1, 2, 3, 2];
  Phaser.Utils.Array.Remove(array, 2); // Removes the first occurrence of 2
  console.log(array); // [1, 3, 2]
  ```

- 删除指定索引中的元素。

  ```js
  RemoveAt(array, index, [callback], [context]);
  ```

  - `index` : 删除项目时的数组索引。 索引必须包含在界限内, 否则会出错 。
  - 可选 `callback` : 取消数组中的项目时要引用的回调 。
  - 可选 `context`: 引用回调时的上下文.

  示例

  ```js
  let array = [1, 2, 3];
  Phaser.Utils.Array.RemoveAt(array, 1); // Removes the element at index 1
  console.log(array); // [1, 3]
  ```

- 删除 `startIndex`和 `endIndex`(包括)之间的元素.

  ```js
  RemoveBetween(array, startIndex, endIndex, [callback], [context]);
  ```

  - `startIndex`:包括从中移除的起始索引。
  - `endIndex` : 不包括要删除的端索引 。
  - `callback`:从阵列中移除的项目需要引用回调。
  - `context`: 引用回调时的上下文.

  示例

  ```js
  let array = [1, 2, 3, 4, 5];
  Phaser.Utils.Array.RemoveBetween(array, 1, 3); // Removes elements from index 1 to 3
  console.log(array); // [1, 4, 5]
  ```

- 删除并返回数组中的一个随机元素。

  ```js
  RemoveRandomElement(array, [start], [length]);
  ```

  - `start`: 启动搜索的阵列索引从. 默认到 0 。
  - `length`: 对随机选择的元素数量可选限制。默认为数组长度 。

  示例

  ```js
  let array = [1, 2, 3];
  let randomItem = Phaser.Utils.Array.RemoveRandomElement(array);
  console.log(randomItem); // Random item removed (e.g., 2)
  console.log(array); // [1, 3]
  ```

- 从指定的索引中的数组中删除一个元素。

  ```js
  SpliceOne(array, index);
  ```

  - `index`:应该分解的项目索引。

  示例

  ```js
  let array = [1, 2, 3];
  Phaser.Utils.Array.SpliceOne(array, 1); // Removes element at index 1
  console.log(array); // [1, 3]
  ```

### 移动元素 {#moving-elements}

- 将指定项目移动到新索引。

  ```js
  MoveTo(array, item, index);
  ```

  - `item` : 要移动的元素。
  - `index`:元素将移动到的新索引。

  示例

  ```js
  let array = [1, 2, 3, 4];
  Phaser.Utils.Array.MoveTo(array, 3, 1); // Moves 3 to index 1
  console.log(array); // [1, 3, 2, 4]
  ```

- 在数组中将指定的项目上移一个索引。

  ```js
  MoveUp(array, item);
  ```

  - `item` : 向上移动阵列的元素。

  示例

  ```js
  let array = [1, 2, 3];
  Phaser.Utils.Array.MoveUp(array, 2); // Moves 2 up one index
  console.log(array); // [1, 3, 2]
  ```

- 在数组中将指定的项目下移一个索引。

  ```js
  MoveDown(array, item);
  ```

  - `item` : 向下移动阵列的元素。

  示例

  ```js
  let array = [1, 2, 3];
  Phaser.Utils.Array.MoveDown(array, 2); // Moves 2 down one index
  console.log(array); // [2, 1, 3]
  ```

- 将项目1 的位置移动到 `baseElement` 上方, 或者在 `baseElement` 后移动一个索引。 如果给定的元素已经高于 `baseElement` , 它不会移动 。

  ```js
  MoveAbove(array, item, baseElement);
  ```

  - `item` : 将移动到基元素之上的元素。
  - `baseElement` : 基数元素.

  示例

  ```js
  let array = [1, 2, 3, 4];
  Phaser.Utils.Array.MoveAbove(array, 1, 3); // Moves 1 above 3
  console.log(array); // [2, 3, 4, 1]
  ```

- 将项目1 的位置移动到 `baseElement` 下方, 或将索引移动到 `baseElement` 后方。 如果给定的元素已经高于 `baseElement` , 则不会移动 。

  ```js
  MoveBelow(array, item, baseElement);
  ```

  - `item` : 基元素以下移动的元素。
  - `baseElement` : 基数元素.

  示例

  ```js
  let array = [1, 2, 3, 4];
  Phaser.Utils.Array.MoveBelow(array, 4, 2); // Moves 4 below 2
  console.log(array); // [1, 4, 2, 3]
  ```

### 排序和洗牌 {#sorting-shuffling}

排序和排空阵列的函数 。

- 随机地分散数组的元素。

  ```js
  SortByDigits(array);
  ```

  示例

  ```js
  let array = [1, 2, 3];
  Phaser.Utils.Array.Shuffle(array); // Randomly shuffles the array
  console.log(array); // Random order (e.g., [3, 1, 2])
  ```

- 按字符串的数值部分排序一系列字符,而忽略任何非数字字符。

  ```js
  SortByDigits(array);
  ```

  示例

  ```js
  let array = ["item20", "item5", "item100", "item1"];
  Phaser.Utils.Array.SortByDigits(array);
  console.log(array); // ['item1', 'item5', 'item20', 'item100']
  ```

- 一种稳定,保持等元的相对顺序.

  ```js
  StableSort(array, compare);
  ```

  - `compare` : 比较函数。

  示例

  ```js
  let array = [5, 2, 9, 1];
  Phaser.Utils.Array.StableSort(array, (a, b) => a - b); // Sorts array
  console.log(array); // [1, 2, 5, 9]
  ```

- 重新排列一个数组,使[左,k]范围内的所有项目都比[k,右]中的所有项目小; k-th元素在[左,右]中将拥有(k-左+1)第最小值。

  ```js
  QuickSelect(array, k, [left], [right], [compare]);
  ```

  - `k` : k-th 元素指数.
  - `left` : 范围左侧部分的索引.
  - `right`: 范围右侧部分的索引.
  - `compare`: 一个可选的比较函数。 它通过两个元素, 并应该返回 0、 1 或 - 1 。

  示例

  ```js
  var array = [10, 4, 5, 8, 6, 11, 26];
  Phaser.Utils.Array.QuickSelect(array, 2);
  console.log(array); // [ 4, 5, 6, 8, 10, 11, 26 ]
  ```

### 获取元素 {#retrieving-elements}

基于不同条件的元素检索方法.

- 返回数组中的第一个元素,并使用 `property` 和 `value` 的可选匹配标准。如果找不到匹配元素,则返回 `null` 。

  ```js
  GetFirst(array, [property], [value], [startIndex], [endIndex]);
  ```

  - `property`:每个阵列元素测试的属性.
  - `value`: 对照属性测试值。 必须通过严格的( ) 比较检查 。
  - `startIndex`:包括从.默认到0的可选起始索引。
  - `endIndex` : 排除可选的搜索端索引。 默认为 `array` 长度 。

  例1:获得第一个匹配特定值的财产的项目

  ```js
  var array = [
    { name: "apple", color: "red" },
    { name: "banana", color: "yellow" },
    { name: "grape", color: "purple" },
    { name: "strawberry", color: "red" },
    { name: "squash", color: "yellow" },
    { name: "eggplant", color: "purple" },
  ];

  var result = Phaser.Utils.Array.GetFirst(array, "color", "yellow");
  console.log(result); // Output: { name: 'banana', color: 'yellow' }
  ```

  例2: 获得第一个匹配属性的项目, 不论价值大小

  ```js
  var array = [
    { name: "apple" },
    { name: "banana", color: "yellow" },
    { name: "grape", color: "purple" },
    { name: "strawberry", color: "red" },
    { name: "squash", color: "yellow" },
    { name: "eggplant", color: "purple" },
  ];

  var result = Phaser.Utils.Array.GetFirst(array, "color");
  console.log(result); // Output: { name: 'banana', color: 'yellow' }
  ```

  例3: 获取第一个项目而不指定属性

  ```js
  var array = [
    { name: "apple", color: "red" },
    { name: "banana", color: "yellow" },
    { name: "grape", color: "purple" },
    { name: "strawberry", color: "red" },
    { name: "squash", color: "yellow" },
    { name: "eggplant", color: "purple" },
  ];

  var result = Phaser.Utils.Array.GetFirst(array);
  console.log(result); // Output: { name: 'apple', color: 'red' }
  ```

  例4:获得第一个匹配属性和索引的项目,包括`startIndex`和不包括`endIndex`。

  ```js
  var array = [
    { name: "apple", color: "red" },
    { name: "banana", color: "yellow" },
    { name: "grape", color: "purple" },
    { name: "strawberry", color: "red" },
    { name: "squash", color: "yellow" },
    { name: "eggplant", color: "purple" },
  ];

  var result = Phaser.Utils.Array.GetFirst(array, "color", "purple", 3, 6);
  console.log(result); // Output: { name: 'eggplant', color: 'purple' }
  ```

- 从数组返回随机元素。

  ```js
  GetRandom(array, [startIndex], [length]);
  ```

  - `startIndex`:可选的启动索引。默认为 0。
  - `length` : 任意长度,元素总数(从 startIndex。从中选择。默认值到 `array` 长度。

  例1:获得随机元素

  ```js
  let array = [1, 2, 3, 4, 5];
  let randomItem = Phaser.Utils.Array.GetRandom(array);
  console.log(randomItem); // Output: 2
  ```

  示例2:从子阵列中获取随机元素

  ```js
  let array = [1, 2, 3, 4, 5];
  let randomItem = Phaser.Utils.Array.GetRandom(array, 2, 2); // Consider elements from index 2 to index 3
  console.log(randomItem); // Output: 3 or 4
  ```

- 在排序的数组中查找最接近给定数字的 `value` 。

  ```js
  FindClosestInSorted(value, array, [key]);
  ```

  - `value`:在阵列中查找的值。
  - `array`:要搜索的阵列,必须排序.
  - `key`: 一个可选属性密钥。 如果指定数组元素属性, 将对照值检查 。

  Example 1

  ```js
  let array = [1, 3, 7, 10];
  let closest = Phaser.Utils.Array.FindClosestInSorted(5, array); // Closest to 5
  console.log(closest); // 7
  ```

  示例2: 对象矩阵

  ```js
  var array = [
    { id: 1, value: 10 },
    { id: 2, value: 20 },
    { id: 3, value: 30 },
    { id: 4, value: 40 },
  ];

  var closest = Phaser.Utils.Array.FindClosestInSorted(35, array, "value");
  console.log(closest); // Output: { id: 4, value: 40 }
  ```

---

### 矩阵创建 {#array-creation}

创建数组的方法

- 将一个多维阵列平整成一个一维阵列.

  ```js
  Flatten(array, [output]);
  ```

  - `output`: 用于保存结果的选用阵列。

  示例

  ```js
  let array = [
    [1, 2],
    [3, 4],
  ];
  let flat = Phaser.Utils.Array.Flatten(array);
  console.log(flat); // [1, 2, 3, 4]
  ```

- 创建一个由 `start` 到 `end` 的数字数组 。

  ```js
  NumberArray(start, end, [prefix], [suffix]);
  ```

  示例

  ```js
  let array = Phaser.Utils.Array.NumberArray(1, 5);
  console.log(array); // [1, 2, 3, 4, 5]
  ```

- 创建从 `start` 到 `end`的阵列,由 `step` 递增.

  ```js
  NumberArrayStep([start], [end], [step]);
  ```

  - `start` : 范围开始.
  - `end` : 范围之末.
  - `step`:增量或减量的数值。

  示例

  ```js
  let array = Phaser.Utils.Array.NumberArrayStep(1, 10, 2);
  console.log(array); // [1, 3, 5, 7, 9]
  ```

- 根据给定的参数和配置创建包含一系列数值的数组。

  ```js
  Range(a, b, [options]);
  ```

  - `options` : 范围配置对象。可以包含: `repeat`, `random`, `randomB`, `yoyo`, `max`, `qty`.
    - `max`: 最大元素生成数。 默认为 0( 无限制 ) 。
    - `qty`:从`a`和`b`的组合中重复每个元素的次数,默认为1次.
    - `random`: 取消生成的数组? 默认为 `false`.
    - `randomB`:在生成输出前先shuffle `b`?默认为`false`.
    - `repeat`: 将 `a` 和 `b` 合并的重复次数。 设定为 `-1` , 用于无限重复。 默认为 0( 不重复) 。
    - `yoyo`: 反转生成数组的顺序, 并再次将其连接起来 ? 创建一个镜像输出 。 默认为 `false` 。

  例1:基本使用

  ```js
  var a = [1, 2];
  var b = ["A", "B"];
  var options = { qty: 1, repeat: 0 };

  var result = Phaser.Utils.Array.Range(a, b, options);
  console.log(result); // Output: [1A, 1B, 2A, 2B]
  /* 
  Output: [
    { a: 1, b: 'A' },
    { a: 1, b: 'B' },
    { a: 2, b: 'A' },
    { a: 2, b: 'B' }
  ]
  */
  ```

  例2:重复和`yoyo`效果

  ```js
  var a = [1, 2];
  var b = ["A", "B"];
  var options = { qty: 1, repeat: 1, yoyo: true };

  var result = Phaser.Utils.Array.Range(a, b, options);
  console.log(result); // Output: [1A, 1B, 2A, 2B, 2B, 2A, 1B, 1A, 1A, 1B, 2A, 2B, 2B, 2A, 1B, 1A]
  /* 
  Output: [
    { a: 1, b: 'A' }, { a: 1, b: 'B' },
    { a: 2, b: 'A' }, { a: 2, b: 'B' },
    { a: 2, b: 'B' }, { a: 2, b: 'A' },
    { a: 1, b: 'B' }, { a: 1, b: 'A' },
    { a: 1, b: 'A' }, { a: 1, b: 'B' },
    { a: 2, b: 'A' }, { a: 2, b: 'B' },
    { a: 2, b: 'B' }, { a: 2, b: 'A' },
    { a: 1, b: 'B' }, { a: 1, b: 'A' }
  ]
  */
  ```

  例3:限制使用`max`生成的元素数量

  ```js
  var a = [1, 2];
  var b = ["A", "B"];
  var options = { qty: 1, repeat: -1, max: 5 };

  var result = Phaser.Utils.Array.Range(a, b, options);
  console.log(result); // Output: [1A, 1B, 2A, 2B, 1A]

  /* 
  Output: [
    { a: 1, b: 'A' },
    { a: 1, b: 'B' },
    { a: 2, b: 'A' },
    { a: 2, b: 'B' },
    { a: 1, b: 'A' }
  ]
  */
  ```

  例4:产出的随机化

  ```js
  var a = [1, 2];
  var b = ["A", "B"];
  var options = { qty: 1, random: true };

  var result = Phaser.Utils.Array.Range(a, b, options);
  console.log(result); // Output: [2B, 1A, 1B, 2A] (randomized order)
  /* 
  Output: [
    { a: 2, b: 'B' },
    { a: 1, b: 'A' },
    { a: 1, b: 'B' },
    { a: 2, b: 'A' },
  ]
  */
  ```

### 组合操纵 {#array-manipulation}

- 将指定项目移动到数组的顶端。

  ```js
  BringToTop(array, item);
  ```

  - `item` : 要移动的元素。

  示例

  ```js
  let array = [1, 2, 3];
  Phaser.Utils.Array.BringToTop(array, 1);
  console.log(array); // [2, 3, 1]
  ```

- 将指定项目移动到数组的后端。

  ```js
  SendToBack(array, item);
  ```

  - `item` : 要移动的元素。

  示例

  ```js
  let array = [1, 2, 3];
  Phaser.Utils.Array.SendToBack(array, 3);
  console.log(array); // [3, 1, 2]
  ```

- 将元素在给定的指数中交换。

  ```js
  Swap(array, item1, item2);
  ```

  - `item1` : 第一个交换元素。
  - `item2` : 第二个交换元素。

  示例

  ```js
  let array = [1, 2, 3, 4, 5];
  Phaser.Utils.Array.Swap(array, 2, 5);
  console.log(array); // [1, 5, 3, 4, 2]
  ```

### 散装操作 {#bulk-operations}

这些方法适用于一个数组的所有或大多数元素.

- 计算数组中有多少元素具有匹配给定值的属性。

  ```js
  CountAllMatching(array, property, value, [startIndex], [endIndex]);
  ```

  - `property`:每个阵列元素测试的属性.
  - `value`: 对照属性测试值。 必须通过严格的( ) 比较检查 。
  - `startIndex`:包括从.默认到0的可选起始索引。
  - `endIndex`:不包括可选的结尾索引。默认为`array`长度。

  例1:基本使用

  ```js
  let array = [{ score: 10 }, { score: 20 }, { score: 10 }];
  let count = Phaser.Utils.Array.CountAllMatching(array, "score", 10);
  console.log(count); // 2
  ```

  示例2:限制搜索范围

  ```js
  var array = [
    { name: "apple", color: "red" },
    { name: "banana", color: "yellow" },
    { name: "cherry", color: "red" },
    { name: "grape", color: "purple" },
  ];

  var result = Phaser.Utils.Array.CountAllMatching(array, "color", "red", 1, 3);
  console.log(result); // Output: 1
  ```

- 调用数组中每个元素的回调 。

  ```js
  Each(array, callback, context, [args]);
  ```

  - `callback`:对阵列中每个项目要引用的回调。
  - `context`: 引用回调时的上下文.
  - `args` : 在当前数组项目之后, 将传递到调用的其他参数 。

  例1:基本使用

  ```js
  let array = [1, 2, 3];
  Phaser.Utils.Array.Each(array, (item) => console.log(item));
  // Output: 1, 2, 3
  ```

示例2:自定义上下文

```js
var array = [1, 2, 3];
var context = { multiplier: 2 };

Phaser.Utils.Array.Each(
  array,
  function (element) {
    console.log(element * this.multiplier);
  },
  context
);
// Output: 2, 4, 6
```

例3:通过辩论

```js
var array = [1, 2, 3];

Phaser.Utils.Array.Each(
  array,
  function (element, factor) {
    console.log(element * factor);
  },
  null,
  5
);
// Output: 5, 10, 15
```

例4:多重论据

```js
var array = ["apple", "banana"];

Phaser.Utils.Array.Each(
  array,
  function (element, prefix, suffix) {
    console.log(prefix + element + suffix);
  },
  null,
  "Fruit: ",
  " is tasty"
);
/* Output:
Fruit: apple is tasty
Fruit: banana is tasty
*/
```

- 调用指定索引范围内每个元素的回调。

  ```js
  EachInRange(array, callback, context, startIndex, endIndex, [args]);
  ```

  - `callback`:对阵列中每个项目要引用的回调。
  - `context`: 引用回调时的上下文.
  - `startIndex`:包括从中搜索的起始索引.
  - `endIndex` : 不包括要搜索的结束索引 。
  - `args`:可选的参数,将传递给回调.

  例1:指定一个范围

  ```js
  var array = [1, 2, 3, 4, 5];
  Phaser.Utils.Array.EachInRange(
    array,
    function (element) {
      console.log(element);
    },
    null,
    1,
    4
  );
  // Output: 2, 3, 4
  ```

  示例2:自定义上下文

  ```js
  var array = [1, 2, 3, 4, 5];
  var context = { multiplier: 2 };

  Phaser.Utils.Array.EachInRange(
    array,
    function (element) {
      console.log(element * this.multiplier);
    },
    context,
    3,
    5
  );
  // Output: 8, 10
  ```

  例3:指定一个范围和通过参数

  ```js
  var array = [1, 2, 3, 4, 5];

  Phaser.Utils.Array.EachInRange(
    array,
    function (element, prefix, suffix) {
      console.log(prefix + element + suffix);
    },
    null,
    1,
    4,
    "Element: ",
    "!"
  );
  /* Output:
  Element: 2!
  Element: 3!
  Element: 4!
  */
  ```

- 设置数组中所有元素的相同属性值。

  ```js
  SetAll(array, property, value, [startIndex], [endIndex]);
  ```

  - `property`:每个阵列元素测试的属性。
  - `value` : 设置属性的值。
  - `startIndex` : 包括搜索对象的可选起始索引 。
  - `endIndex` : 排除可选的搜索端索引 。

  例1:基本使用

  ```js
  let array = [{ score: 10 }, { score: 20 }];
  Phaser.Utils.Array.SetAll(array, "score", 5);
  console.log(array);
  /* Output:
  [
    { score: 5 }, 
    { score: 5 }
  ]
  */
  ```

  示例2:指定一个范围

  ```js
  let array = [{ score: 10 }, { score: 20 }, { score: 30 }, { score: 40 }];
  Phaser.Utils.Array.SetAll(array, "score", 5, 1, 3);
  console.log(array);
  /* Output:
  [
    { score: 10 }, 
    { score: 5 }, 
    { score: 5 }, 
    { score: 40 }
  ]
  */
  ```

- 将第一次出现的 `oldItem` 替换为 `newItem` 。

  ```js
  Replace(array, oldItem, newItem);
  ```

  - `oldItem`: 将替换的阵列中的元素.
  - `newItem`:在oldChild位置插入阵列的元素.

  示例

  ```js
  let array = [1, 2, 3];
  Phaser.Utils.Array.Replace(array, 2, 4);
  console.log(array); // [1, 4, 3]
  ```

### 旋转 {#rotation}

在一个阵列内旋转元素的方法。

- 将数组的元素旋转到指定的数组左边。

  ```js
  RotateLeft(array, [total]);
  ```

  - `total`: 移位数组的次数.

  示例

  ```js
  let array = [1, 2, 3, 4];
  Phaser.Utils.Array.RotateLeft(array, 2);
  console.log(array); // [3, 4, 1, 2]
  ```

- 将数组的元素旋转到指定的数组的右边。

  ```js
  RotateRight(array, [total]);
  ```

  - `total`: 移位数组的次数.

  示例

  ```js
  let array = [1, 2, 3, 4];
  Phaser.Utils.Array.RotateRight(array, 1);
  console.log(array); // [4, 1, 2, 3]
  ```

### 安全范围 {#safe-range}

- 确保索引在数组的界限内。
  
  ```js
  SafeRange(array, startIndex, endIndex, [throwError]);
  ```
  
  - `startIndex` : 开始索引.
  - `endIndex` : 终极指数.
  - `throwError`:如果设定为`true`,则丢出一个错误,范围已超出界限.

  示例

  ```js
  let array = [1, 2, 3];
  let isValid = Phaser.Utils.Array.SafeRange(array, 2);
  console.log(isValid); // true
  ```

## Phaser.Utils.Base64 {#phaserutilsbase64}

提供编码和解码Base64的实用方法,具体在ArrayBoffer和Base64编码字符串之间转换,用于与图像,音频文件或其他介质类型等二进制数据合作,使二进制数据能够转换为Base64字符串进行传输或存储.

### 串列缓冲器Tase64 {#arraybuffertobase64}

将 `arrayBuffer` 转换为 base64 字符串。如果提供了 `mediaType` 参数,所产生的字符串可以选择为数据 uri 。

```js
ArrayBufferToBase64(arrayBuffer, [mediaType]);
```

- `mediaType`:一种可选介质类型,即`audio/ogg`或`image/jpeg`.

示例

```js
var buffer = new Uint8Array([72, 101, 108, 108, 111]).buffer;  // "Hello" in binary

// Convert the ArrayBuffer to Base64
var base64String = Phaser.Utils.Base64.ArrayBufferToBase64(buffer);

console.log(base64String);  // Output: "SGVsbG8="
```

### 碱基64 用于箭头缓冲器 {#base64toarraybuffer}

将带有或没有数据uri的 `base64` 字符串转换为矩阵缓冲器。

```js
Base64ToArrayBuffer(base64);
```

示例

```js
// Assume you have a Base64 string (e.g., retrieved from a database or an API)
var base64String = "SGVsbG8=";  // Base64 for "Hello"

// Convert the Base64 string back to an ArrayBuffer
var arrayBuffer = Phaser.Utils.Base64.Base64ToArrayBuffer(base64String);

// Convert the ArrayBuffer to a string for verification
var uint8Array = new Uint8Array(arrayBuffer);
var decodedString = String.fromCharCode.apply(null, uint8Array);

console.log(decodedString);  // Output: "Hello"
```

## Phaser.Utils.Objects {#phaserutilsobjects}

提供一套用于与 Phaser 中对象打交道的实用方法。这些方法有助于管理、操纵和提取对象的数据,提供克隆、合并、价值检索等功能。

### 克隆 {#clone}

创建对象的浅拷贝。不克隆嵌套对象。

```js
Clone(object)
```

- `object` : 要克隆的对象。

示例

```js
var original = { a: 1, b: [2, 3], c: { d: 4 } };
var copy = Phaser.Utils.Objects.Clone(original);
console.log(copy);
/*
{ 
  a: 1,
  b: [2, 3],
  c: {
       d: 4
     } 
}

copy.b is a new array, changing values in original.b or copy.b does not affect either array.
copy.c is a reference to the same object as original.c, changes in original.c is automatically reflected in copy.c
*/
```

### 深层复制 {#deepcopy}

创建对象的深层副本。这种方法会递归复制所有属性,包括嵌入对象,确保新对象完全独立于原始对象。

```js
DeepCopy(source)
```

- `object` : 深复制对象.
 
示例

```js
var original = {
    a: 1,
    b: [2, 3, { d: 4 }],
    c: { e: 5, f: [6, 7] }
};
var copy = Phaser.Utils.Objects.DeepCopy(original);
console.log(copy);
/*
{
  a: 1, 
  b: [2, 3, { d: 4 }], 
  c: {
       e: 5,
       f: [6, 7] 
     } 
}
*/
```

### 扩展 {#extend}

这是稍作修改的http://api.jquery.com/jQuery.extend/.用来将一个或多个对象的属性合并成目标对象的版本,它可以执行浅重和深重的复制,这取决于深重的旗帜.

```js
Extend(object, source1, source2, ...)
```

- `object` : 扩展对象。
- `source1`, `source2`, ...: 一个或多个属性会被复制到目标的源对象.

例1: 浅色副本, `b` 属性来源 `obj1` 完全被 $ `b` 属性来源 `obj2`.

```js
var obj1 = { a: 1, b: { c: 2 } };
var obj2 = { b: { d: 3 }, e: 4 };

var result = Phaser.Utils.Objects.Extend({}, obj1, obj2);
console.log(result);
/*
{
  a: 1,
  b: {
       d: 3
     },
  e: 4 
}
*/
```

实例2:深层复制, `b` 属性从两者中 `obj1` 财务报告和已审计财务报表 `obj2` 合并,保留嵌套结构。

```js
var obj1 = { a: 1, b: { c: 2 } };
var obj2 = { b: { d: 3 }, e: 4 };

var result = Phaser.Utils.Objects.Extend({}, obj1, obj2);
console.log(result);
/*
{
  a: 1,
  b: {
       d: 3
     },
  e: 4 
}
*/
```

### 获取高级值 {#getadvancedvalue}

从带有高级选择选项的对象获取一个值。

```js
GetAdvancedValue(source, key, defaultValue)
```

- `source`: 用来获取值的物体。
- `key` :要检索的值的密钥。
- `defaultValue` : 如果密钥不存在, 默认值将返回 。

示例

```js
var source = {
    a: [1, 2, 3],
    b: { randInt: [5, 10] },
    c: { randFloat: [0.1, 0.9] },
    d: function (key) { return key + " processed"; },
    e: 42,
    f: null
};

console.log(Phaser.Utils.Objects.GetAdvancedValue(source, 'a', 0));  // Random element from [1, 2, 3]
console.log(Phaser.Utils.Objects.GetAdvancedValue(source, 'b', 0));  // Random integer between 5 and 10
console.log(Phaser.Utils.Objects.GetAdvancedValue(source, 'c', 0));  // Random float between 0.1 and 0.9
console.log(Phaser.Utils.Objects.GetAdvancedValue(source, 'd', 0));  // "d processed"
console.log(Phaser.Utils.Objects.GetAdvancedValue(source, 'e', 0));  // 42
console.log(Phaser.Utils.Objects.GetAdvancedValue(source, 'f', 100));  // 100 (default value as 'f' is null)
```

### 获取快速 VALUE {#getfastvalue}

在源对象的顶级内查找密钥,或返回 `defaultValue`。

```js
GetFastValue(source, key, defaultValue)
```

- `source`: 用来获取值的物体。
- `key` :要检索的值的密钥。
- `defaultValue` : 如果密钥不存在, 默认值将返回 。

示例

```js
var obj = { a: 10, b: 20, c: undefined };

console.log(Phaser.Utils.Objects.GetFastValue(obj, 'a', 0));  // Output: 10
console.log(Phaser.Utils.Objects.GetFastValue(obj, 'b', 0));  // Output: 20
console.log(Phaser.Utils.Objects.GetFastValue(obj, 'c', 0));  // Output: 0 (defaultValue because 'c' is undefined)
console.log(Phaser.Utils.Objects.GetFastValue(obj, 'd', 0));  // Output: 0 (defaultValue because 'd' doesn't exist)
console.log(Phaser.Utils.Objects.GetFastValue(null, 'a', 0)); // Output: 0 (defaultValue because source is null)
console.log(Phaser.Utils.Objects.GetFastValue(42, 'a', 0));   // Output: 0 (defaultValue because source is a number)
```

### 获取MinMax Value 数据 {#getminmaxvalue}

从对象获取一个值,受最小值和最大值的限制。

```js
GetMinMaxValue(source, key, min, max, defaultValue)
```

- `source`: 用来获取值的物体。
- `key` :要检索的值的密钥。
- `min` : 允许的最小值。
- `max` : 允许的最大值。
- `defaultValue` : 如果密钥不存在, 默认值将返回 。

示例

```js
var source = { speed: 120 };

console.log(Phaser.Utils.Objects.GetMinMaxValue(source, 'speed', 50, 100, 75));  // Output: 100 (clamped to max)
console.log(Phaser.Utils.Objects.GetMinMaxValue(source, 'speed', 50, 150, 75));  // Output: 120 (within range)
console.log(Phaser.Utils.Objects.GetMinMaxValue(source, 'acceleration', 50, 100, 75)); // Output: 75 (uses default value)
console.log(Phaser.Utils.Objects.GetMinMaxValue(source, 'acceleration', 50, 100));  // Output: 50 (default is set to min)
```

### 获取值 {#getvalue}

从对象获取一个值,如果找不到 `key` ,则会回落到默认值。 `key` 是一个字符串,可以根据使用周期字符来分割。

```js
GetValue(source, key, defaultValue)
```

- `source`: 用来获取值的物体。
- `key` :要检索的值的密钥。
- `defaultValue` : 如果密钥不存在, 默认值将返回 。

示例

```js
var source = { a: { b: { c: 10 } }, x: 5 };
var altSource = { a: { b: { c: 20 } }, y: 15 };

console.log(Phaser.Utils.Objects.GetValue(source, 'a.b.c', 0));  // Output: 10 (found in source)
console.log(Phaser.Utils.Objects.GetValue(source, 'y', 0, altSource));  // Output: 15 (found in altSource)
console.log(Phaser.Utils.Objects.GetValue(source, 'x', 0));  // Output: 5 (found in source)
console.log(Phaser.Utils.Objects.GetValue(source, 'a.b.z', 0));  // Output: 0 (default value, not found)
```

### 全部散开 {#hasall}

检查对象是否有所有指定的密钥 。

```js
HasAll(source, keys)
```

- `source` : 检查对象。
- `keys`:要检查的密钥阵列.

示例

```js
var obj = { a: 1, b: 2, c: 3 };

console.log(Phaser.Utils.Objects.HasAll(obj, ['a', 'b']));  // Output: true (both 'a' and 'b' are present)
console.log(Phaser.Utils.Objects.HasAll(obj, ['a', 'd']));  // Output: false ('d' is missing)
console.log(Phaser.Utils.Objects.HasAll(obj, ['a', 'b', 'c']));  // Output: true (all keys are present)
```

### 任何变速器 {#hasany}

检查对象是否有指定的密钥。

```js
HasAny(source, keys)
```

- `source` : 检查对象。
- `keys`:要检查的密钥阵列.

示例

```js
var obj = { a: 1, b: 2, c: 3 };

console.log(Phaser.Utils.Objects.HasAny(obj, ['a', 'd']));  // Output: true ('a' is found)
console.log(Phaser.Utils.Objects.HasAny(obj, ['x', 'y']));  // Output: false (none of the keys are found)
console.log(Phaser.Utils.Objects.HasAny(obj, ['b', 'c']));  // Output: true ('b' is found)
```

### 已实现 {#hasvalue}

检查对象是否有带有特定值的密钥。

```js
HasValue(source, key)
```

- `source` : 检查对象。
- `key` :要检查的密钥.

示例

```js
var obj = { name: 'Alice', age: 25 };

console.log(Phaser.Utils.Objects.HasValue(obj, 'name'));  // Output: true (because 'name' is a property of obj)
console.log(Phaser.Utils.Objects.HasValue(obj, 'gender'));  // Output: false (because 'gender' is not a property of obj)
```

### 被申请对象 {#isplainobject}

检查给定值是否是一个普通对象(即使用`{}`或`new Object()`创建).

```js
console.log(Phaser.Utils.Objects.IsPlainObject({}));                 // true (plain object)
console.log(Phaser.Utils.Objects.IsPlainObject(new Object()));       // true (plain object)
console.log(Phaser.Utils.Objects.IsPlainObject([]));                 // false (array, not a plain object)
console.log(Phaser.Utils.Objects.IsPlainObject(document.body));      // false (DOM node, not a plain object)
console.log(Phaser.Utils.Objects.IsPlainObject(window));             // false (window object, not a plain object)
console.log(Phaser.Utils.Objects.IsPlainObject(null));               // false (null, not an object)
```

- `object` : 检查的值。

示例

```js

var isPlainObject = Phaser.Utils.Objects.IsPlainObject(obj);
```

### 合并 {#merge}

使用 `obj1` 和 `obj2` 的全部值创建新对象。 如果在 obj1 和 obj2 中都存在值, 则使用 obj1 在 obj1中存在的值。 这只是一个浅层复制件。 深层嵌套对象不会被克隆, 所以请确定只使用此函数在浅层对象上 。

```js
Merge(obj1, obj2)
```

- `obj1` : 第一个对象.
- `obj2` :第二个对象.

示例

```js
var obj1 = { a: 1, b: 2 };
var obj2 = { b: 3, c: 4 };

var result = Phaser.Utils.Objects.Merge(obj1, obj2);

console.log(result);  // Output: { a: 1, b: 2, c: 4 }
console.log(obj1);    // Output: { a: 1, b: 2 } (unchanged)
console.log(obj2);    // Output: { b: 3, c: 4 } (unchanged)
```

### 合并右侧 {#mergeright}

使用全部值创建新对象 `obj1`扫描 `obj2`。如果在 `obj2` 中也存在 `obj1`,从 `obj2` ,否则该属性被跳过。

```js
MergeRight(obj1, obj2)
```

- `obj1`:第一个合并对象.
- `obj2`: 合并的第二个对象。 此对象的密钥也存在于 `obj1` 中, 将会复制到 `obj1` 。

示例
```js
var obj1 = { a: 1, b: 2, c: 3 };
var obj2 = { b: 20, c: 30, d: 40 };

var result = Phaser.Utils.Objects.MergeRight(obj1, obj2);

console.log(result);  // Output: { a: 1, b: 20, c: 30 }
console.log(obj1);    // Output: { a: 1, b: 2, c: 3 } (unchanged)
console.log(obj2);    // Output: { b: 20, c: 30, d: 40 } (unchanged)
```

### 选择 {#pick}

返回只包含在所提供对象上发现的 `keys` 的新对象。如果找不到密钥,则返回空对象。

```js
Pick(source, keys)
```

- `source` : 从中选择属性的对象。
- `keys`:从提供的对象中获取的一系列属性.

示例

```js
var person = { name: 'Alice', age: 30, city: 'New York', occupation: 'Engineer' };
var selectedKeys = ['name', 'city'];

var result = Phaser.Utils.Objects.Pick(person, selectedKeys);

console.log(result);  // Output: { name: 'Alice', city: 'New York' }
```

### 设置值 {#setvalue}

在对象中设置值,必要时创建属性路径。

```js
SetValue(source, key, value)
```

- `source`:设置值的对象。
- `key` :属性路径(例如, `'a.b.c'`).
- `value` : 要设置的值 。

示例

```js
var obj = {
    a: {
        b: {
            c: 10
        }
    }
};

// Set a simple property
var results = Phaser.Utils.Objects.SetValue(obj, 'a', 100);  // Returns true
console.log(obj);  // { a: 100 }

// Set a nested property
var results = Phaser.Utils.Objects.SetValue(obj, 'a.b.c', 20);  // Returns true
console.log(obj);  // { a: { b: { c: 20 } } }

// Try to set a non-existent nested property
var results = Phaser.Utils.Objects.SetValue(obj, 'a.x.y', 50);  // Returns false
console.log(obj); // no change to obj
```

## Phaser.Utils.String {#phaserutilsstring}

包含用于操纵和格式化字符串的实用函数。它简化了常见字符串操作,如格式化、编版和倒置字符串。

### 格式化 {#format}

取一个字符串, 并用给定数组中的值替换标记实例。 标记的形式是 `%1`、 `%2`等。 例如: `Format("The %1 is worth %2 gold", [ 'Sword', 500 ])`

```js
Format(string, values);
```

- `string`(弦):包含替换标记的字符串.
- `values`(对象):一个包含将替换标记的数值的阵列。如果没有数值,则插入空字符串。

Example:

```js
var string = "Player %1 scored %2 points";
var values = ["Alice", 100];
var result = Phaser.Utils.String.Format(string, values);
console.log(result); // result: "Player Alice scored 100 points"
```

### 纸 {#pad}

使用指定的字符,将给定的字符串和垫子取出,按所需长度。

```js
Pad(str, [len], [pad], [dir])
```

Parameters:
- `str` : 原始字符串为垫。
- `len`:所生成的字符串的目标长度.
- `pad`: 用于垫装字符串的字符 。
- `dir` : 贴垫的方向。 使用 :
  - 右侧垫的`1`,
  - 左侧垫板的`2`,
  - 双侧垫装`3`.

示例

```js
var padLeft = Phaser.Utils.String.Pad("7", 3, "0", 1); // Left Padding (dir = 1): "007"
var padRight = Phaser.Utils.String.Pad("7", 3, "0", 2); // Right Padding (dir = 2 or any other value): "700"
var padBoth = Phaser.Utils.String.Pad("7", 3, "0", 3); // Both Sides Padding (dir = 3): "070"
```

### 删除已删除 {#removeat}

取字符串并删除给定索引中的字符。

```js
RemoveAt(string, index)
```

Parameters:
- `string` :原弦词.
- `index`:要删除的字符的零基索引.

Example:

```js
const result = Phaser.Utils.String.RemoveAt("Phaser", 2); // result: "Phser"
```

### 反转 {#reverse}

取给定的字符串并反转,返回倒转的字符串。

```js
Reverse(string)
```

- `string` : 倒转的字符串.

Example:

```js
const result = Phaser.Utils.String.Reverse("Phaser"); // result: "resahP"
```

### 大写第一 {#uppercasefirst}

如果有字符串,则大写第一个字母。

```js
UppercaseFirst(string)
```

- `string`(字符串):要修改的字符串.

Example:

```js
const result = Phaser.Utils.String.UppercaseFirst("phaser"); // result: "Phaser"
```

### 用户 {#uuid}

创建并返回随机的RFC4122版本4符合通用唯一标识符(UUID).

弦形为:`xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx`,其中每张`x`被从0到f的随机十六进制数字取代,`y`被从8到b的随机十六进制数码取代.

```js
UUID()
```

Example:

```js
const uuid = Phaser.Utils.String.UUID();
// result: "3b42e58f-0d1c-4b2a-b8f7-e123456789ab"
```

---
