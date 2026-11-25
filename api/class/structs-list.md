# List {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/structs-list)

A List 是一组通用的、有秩序的集合, 提供了丰富的工具方法, 用于添加、 删除、 排序、 搜索和重排其内容。 与普通数组不同, List 支持可选添加和去除调用回调、 稳定排序、 命名项目搜索、 位置转录通过 `first`, `last`, `next`,和 `previous` 属性,以及安全的在位操作(擦拭、移动、替换、洗涤)。 Phaser 用于显示列表、摄像机列表和其他命令收藏的后置结构,其中物品必须保持独有和命令。

**构造函数**

`new List(parent)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | * | 否 | 此列表的父关. |

---


**作用域**: static

> 源码：[src/structs/List.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L19)  
引入版本：3.0.0

## 公开成员 {#public-members}

### _sortKey {#_sortKey}

#### _sortKey: string {#_sortkey-string}


**说明:**

需要排序的属性键 。


> 源码：[src/structs/List.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L95)  
引入版本：3.4.0


---

### addCallback {#addCallback}

#### addCallback: function {#addcallback-function}


**说明:**

每当儿童被列入名单时,都会重复使用。


> 源码：[src/structs/List.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L77)  
引入版本：3.4.0


---

### first {#first}

#### first: * {#first-1}


**说明:**

列表中的首项或 `null` 空列表 。

**标签:**

 - genericUse


> 源码：[src/structs/List.js#L731](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L731)  
引入版本：3.0.0


---

### last {#last}

#### last: * {#last-1}


**说明:**

列表中最后一个项目,或空列表的 `null` 。

**标签:**

 - genericUse


> 源码：[src/structs/List.js#L758](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L758)  
引入版本：3.0.0


---

### length {#length}

#### length: number {#length-number}


**说明:**

清单内的项目数。


> 源码：[src/structs/List.js#L714](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L714)  
引入版本：3.0.0


---

### list {#list}

#### list: Array.\<*> {#list-array}


**说明:**

此收藏的对象 。

**标签:**

 - genericUse


> 源码：[src/structs/List.js#L53](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L53)  
引入版本：3.0.0


---

### next {#next}

#### next: * {#next-1}


**说明:**

清单上的下一个项目,或如果整个清单已经经过,则使用`null`。

此属性可以在读取 [#first](#first) 后相继读取, 或者手动设置 [#position](#position) 以将列表分割为直线 。

**标签:**

 - genericUse


> 源码：[src/structs/List.js#L785](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L785)  
引入版本：3.0.0


---

### parent {#parent}

#### parent: * {#parent-1}


**说明:**

此列表的父关.


> 源码：[src/structs/List.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L44)  
引入版本：3.0.0


---

### position {#position}

#### position: number {#position-number}


**说明:**

当前元素的索引 。

内部使用时,通过列表中带有[#first](#first),[#last](#last),[#next](#next),和[#previous](#previous)属性.


> 源码：[src/structs/List.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L65)  
引入版本：3.0.0


---

### previous {#previous}

#### previous: * {#previous-1}


**说明:**

清单上的上一项,或如果整个清单已经经过,则称为`null`。

此属性可以在读取 [#last](#last) 后相继读取, 或者手动设置 [#position](#position) 将列表向后排列 。

**标签:**

 - genericUse


> 源码：[src/structs/List.js#L814](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L814)  
引入版本：3.0.0


---

### removeCallback {#removeCallback}

#### removeCallback: function {#removecallback-function}


**说明:**

每次从这个名单中除名时都会重复使用一个召回电话。


> 源码：[src/structs/List.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L86)  
引入版本：3.4.0


---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(child, [skipCallback]) {#instance-addchild-skipcallback}


**说明:**

将给定的项目添加到列表的末尾。每个项目必须是独一无二的。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| child | * \| Array.\<*> | 否 |  | 将项目或项目数组添加到列表中。 |
| skipCallback | boolean | 是 | false | 跳过呼叫列表。 addCallback 如果成功添加此孩子 。 |


**返回值:** * - 列表的内在阵列.


> 源码：[src/structs/List.js#L105](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L105)  
引入版本：3.0.0


---

### addAt {#addAt}

#### \<instance> addAt(child, [index], [skipCallback]) {#instance-addatchild-index-skipcallback}


**说明:**

添加到列表中, 开始于指定的索引。 每个条目必须在列表中独有。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| child | * | 否 |  | 将项目或项目数组添加到列表中。 |
| index | number | 是 | 0 | 插入元素的列表中的索引。 |
| skipCallback | boolean | 是 | false | 跳过呼叫列表。 addCallback 如果成功添加此孩子 。 |


**返回值:** * - 列表的内在阵列.


> 源码：[src/structs/List.js#L128](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L128)  
引入版本：3.0.0


---

### bringToTop {#bringToTop}

#### \<instance> bringToTop(child) {#instance-bringtotopchild}


**说明:**

将给定的孩子带到此列表的首位 。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | * | 否 | 举进士名录之项. |


**返回值:** * - 被移动的物品。


> 源码：[src/structs/List.js#L496](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L496)  
引入版本：3.0.0


---

### count {#count}

#### \<instance> count(property, value) {#instance-countproperty-value}


**说明:**

返回清单上具有与给定值相符的属性的总数。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| property | string | 否 | 每个项目测试的属性 。 |
| value | * | 否 | 测试属性的值 。 |


**返回值:** number - 匹配元素的总数 。


> 源码：[src/structs/List.js#L312](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L312)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此列表。


> 源码：[src/structs/List.js#L699](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L699)  
引入版本：3.0.0


---

### each {#each}

#### \<instance> each(callback, [context], [args]) {#instance-eachcallback-context-args}


**说明:**

将所有的孩子传到给定的回调中.

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | EachListCallback | 否 | 调用功能 。 |
| context | * | 是 | 执行回调时用作 `this` 值 。 |
| args | * | 是 | 更多论点,在孩子出生后,会转给回电者。 |


> 源码：[src/structs/List.js#L657](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L657)  
引入版本：3.0.0


---

### exists {#exists}

#### \<instance> exists(child) {#instance-existschild}


**说明:**

检查清单上是否存在项目。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | * | 否 | 检查是否存在的项目 。 |


**返回值:** boolean - 如果在列表中找到该物品,则使用`true`,否则使用`false`.


> 源码：[src/structs/List.js#L620](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L620)  
引入版本：3.0.0


---

### getAll {#getAll}

#### \<instance> getAll([property], [value], [startIndex], [endIndex]) {#instance-getallproperty-value-startindex-endindex}


**说明:**

将名单上的所有儿童送回。

您可以选择使用 `property` 和 `value` 参数指定匹配标准 。

例如:`getAll('parent')`只归还拥有名为`parent`的属性的儿童.

您还可以指定一个值来比较属性 :

`getAll('visible', true)`只把那些 拥有明显属性的孩子送回`true`

您可以选择指定一个起始和结束索引。 例如, 如果此列表有100个孩子, 您将 `startIndex` 设置为 0, `endIndex` 设置为 50, 它将会从列表中仅返回前50个孩子的匹配 。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| property | string | 是 | 用于测试值参数的可选属性 。 |
| value | any | 是 | 如果设定了属性,则Child.属性必须严格地与这一价值相等,才能列入结果。 |
| startIndex | number | 是 | 首个启动搜索的孩子索引. |
| endIndex | number | 是 | 最后的婴儿索引要搜索到 |


**返回值:** Array.\<*> - 清单上符合规定标准的所有项目(如有)。


> 源码：[src/structs/List.js#L280](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L280)  
引入版本：3.0.0


---

### getAt {#getAt}

#### \<instance> getAt(index) {#instance-getatindex}


**说明:**

在清单内某一位置检索该物品。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 项索引. |


**返回值:** * - 被检索到的物品,或者如果不在清单的界限内,则使用`undefined`.


> 源码：[src/structs/List.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L154)  
引入版本：3.0.0


---

### getByName {#getByName}

#### \<instance> getByName(name) {#instance-getbynamename}


**说明:**

寻找儿童与其 `name` 属性匹配给定的参数。如果一个以上孩子的同名名称相同,则只返回第一个。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 寻之名曰. |


**返回值:** * - 第一个孩子有匹配的名字,或者如果找不到,则无效。


> 源码：[src/structs/List.js#L223](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L223)  
引入版本：3.0.0


---

### getFirst {#getFirst}

#### \<instance> getFirst(property, value, [startIndex], [endIndex]) {#instance-getfirstproperty-value-startindex-endindex}


**说明:**

返回清单某一部分中符合特定标准的第一要素。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| property | string | 否 |  | 属性名称用于测试,或者虚构价值用于无标准. |
| value | * | 否 |  | 测试 `property` 相对于,或 `undefined` 允许任何值, 并且只检查存在值 。 |
| startIndex | number | 是 | 0 | 列表中要开始搜索的位置 。 |
| endIndex | number | 是 |  | 列表中的位置可以选择停止搜索, 将不会被检查 。 |


**返回值:** * - 符合给定标准的首项,或如果没有此类项目,则使用`null`。


> 源码：[src/structs/List.js#L260](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L260)  
引入版本：3.0.0


---

### getIndex {#getIndex}

#### \<instance> getIndex(child) {#instance-getindexchild}


**说明:**

将项目置于清单中并返回其索引。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | * | 否 | 找到的线索 |


**返回值:** number - 列表中项目索引,或如果不在列表中则为−1.


> 源码：[src/structs/List.js#L171](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L171)  
引入版本：3.0.0


---

### getRandom {#getRandom}

#### \<instance> getRandom([startIndex], [length]) {#instance-getrandomstartindex-length}


**说明:**

从列表中返回随机子 。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| startIndex | number | 是 | 0 | 从列表前方除去(最小的孩子). |
| length | number | 是 | "(to top)" | 限制您想要随机选择的数值数量。 |


**返回值:** * - 此列表的随机子 。


> 源码：[src/structs/List.js#L242](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L242)  
引入版本：3.0.0


---

### moveAbove {#moveAbove}

#### \<instance> moveAbove(child1, child2) {#instance-moveabovechild1-child2}


**说明:**

将某个项目移到清单上的另一项目上方。如果给定的项目已经移到另一项目上方,则不会移到清单上。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child1 | * | 否 | 上移基元素的元素。 |
| child2 | * | 否 | 基点元素. |


> 源码：[src/structs/List.js#L364](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L364)  
引入版本：3.55.0


---

### moveBelow {#moveBelow}

#### \<instance> moveBelow(child1, child2) {#instance-movebelowchild1-child2}


**说明:**

将一个项目移到清单的另一项目下方。如果给定的项目已经移到另一项目下方,则不会移动。下面是清单开始的地方。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child1 | * | 否 | 移动到基元素以下的元素. |
| child2 | * | 否 | 基点元素. |


> 源码：[src/structs/List.js#L382](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L382)  
引入版本：3.55.0


---

### moveDown {#moveDown}

#### \<instance> moveDown(child) {#instance-movedownchild}


**说明:**

将给定的孩子移到列表中一个位置, 除非它已经位于底部 。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | * | 否 | 下移项. |


**返回值:** * - 被移动的物品。


> 源码：[src/structs/List.js#L549](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L549)  
引入版本：3.0.0


---

### moveTo {#moveTo}

#### \<instance> moveTo(child, index) {#instance-movetochild-index}


**说明:**

将列表中的一个项目移动到新位置。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | * | 否 | 移动的物品。 |
| index | number | 否 | 移动项目的新位置 。 |


**返回值:** * - 被移动的物件.


> 源码：[src/structs/List.js#L346](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L346)  
引入版本：3.0.0


---

### moveUp {#moveUp}

#### \<instance> moveUp(child) {#instance-moveupchild}


**说明:**

将给定的孩子移到列表中一个位置, 除非它已经位于顶端 。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | * | 否 | 上移的物品. |


**返回值:** * - 被移动的物品。


> 源码：[src/structs/List.js#L530](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L530)  
引入版本：3.0.0


---

### remove {#remove}

#### \<instance> remove(child, [skipCallback]) {#instance-removechild-skipcallback}


**说明:**

从列表中删除一个或多个项目。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| child | * | 否 |  | 要删除的项目, 或项目数组 。 |
| skipCallback | boolean | 是 | false | 跳过名单。 removeCallback。 |


**返回值:** * - 成功从清单中删除的物项或数组物项。


> 源码：[src/structs/List.js#L400](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L400)  
引入版本：3.0.0


---

### removeAll {#removeAll}

#### \<instance> removeAll([skipCallback]) {#instance-removeallskipcallback}


**说明:**

删除所有项目。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| skipCallback | boolean | 是 | false | 跳过名单。 removeCallback。 |


**返回值:** [Phaser.Structs.List](/api/class/structs-list) - 此列表对象 。


> 源码：[src/structs/List.js#L474](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L474)  
引入版本：3.0.0


---

### removeAt {#removeAt}

#### \<instance> removeAt(index, [skipCallback]) {#instance-removeatindex-skipcallback}


**说明:**

删除列表中指定位置的项目。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| index | number | 否 |  | 删除项目的位置 。 |
| skipCallback | boolean | 是 | false | 跳过名单。 removeCallback。 |


**返回值:** * - 被移除的物品。


> 源码：[src/structs/List.js#L423](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L423)  
引入版本：3.0.0


---

### removeBetween {#removeBetween}

#### \<instance> removeBetween([startIndex], [endIndex], [skipCallback]) {#instance-removebetweenstartindex-endindex-skipcallback}


**说明:**

删除列表中指定范围内的项目。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| startIndex | number | 是 | 0 | 开始删除的索引 。 |
| endIndex | number | 是 |  | 停止删除的位置, 此位置的项目不会被移除 。 |
| skipCallback | boolean | 是 | false | 跳过名单。 removeCallback。 |


**返回值:** Array.\<*> - 被移除的项目的数组 。


> 源码：[src/structs/List.js#L448](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L448)  
引入版本：3.0.0


---

### replace {#replace}

#### \<instance> replace(oldChild, newChild) {#instance-replaceoldchild-newchild}


**说明:**

将本列表中的子替换为指定的 newChild。 newChild 不能成为该列表的成员 。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| oldChild | * | 否 | 将替换的列表中的儿童 。 |
| newChild | * | 否 | 拟插入该名单的儿童。 |


**返回值:** * - 返回在本列表中替换的 oldChild 。


> 源码：[src/structs/List.js#L602](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L602)  
引入版本：3.0.0


---

### reverse {#reverse}

#### \<instance> reverse() {#instance-reverse}


**说明:**

颠倒本列表中所有儿童的顺序。

**标签:**

 - genericUse


**返回值:** [Phaser.Structs.List](/api/class/structs-list) - 此列表对象 。


> 源码：[src/structs/List.js#L568](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L568)  
引入版本：3.0.0


---

### sendToBack {#sendToBack}

#### \<instance> sendToBack(child) {#instance-sendtobackchild}


**说明:**

将给定的孩子送到此列表的底部。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | * | 否 | 寄到列表后面的项目 。 |


**返回值:** * - 被移动的物品。


> 源码：[src/structs/List.js#L513](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L513)  
引入版本：3.0.0


---

### setAll {#setAll}

#### \<instance> setAll(property, value, [startIndex], [endIndex]) {#instance-setallproperty-value-startindex-endindex}


**说明:**

将属性 `key` 设置为本列表所有成员的指定值。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| property | string | 否 | 设置的地产名称 。 |
| value | * | 否 | 设置属性的值 。 |
| startIndex | number | 是 | 首个启动搜索的孩子索引. |
| endIndex | number | 是 | 最后的婴儿索引要搜索到 |


> 源码：[src/structs/List.js#L637](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L637)  
引入版本：3.0.0


---

### shuffle {#shuffle}

#### \<instance> shuffle() {#instance-shuffle}


**说明:**

将列表中的项目打乱 。

**标签:**

 - genericUse


**返回值:** [Phaser.Structs.List](/api/class/structs-list) - 此列表对象 。


> 源码：[src/structs/List.js#L585](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L585)  
引入版本：3.0.0


---

### shutdown {#shutdown}

#### \<instance> shutdown() {#instance-shutdown}


**说明:**

清除列表并重现其内部阵列。


> 源码：[src/structs/List.js#L686](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L686)  
引入版本：3.0.0


---

### sort {#sort}

#### \<instance> sort(property, [handler]) {#instance-sortproperty-handler}


**说明:**

排序此列表的内容, 使项目根据给定属性排列 。 例如, `sort('alpha')` 会根据它们的 `alpha` 属性的值排序列表内容 。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| property | string | 否 | 地产被逻辑分类。 |
| handler | function | 是 | 提供您自己的自定义处理器功能。 将接收两个孩子, 并返回一个数字( 如果第一个是负数, 则在第二个之前出现, 如果后面出现, 则为零, 如果相等) 。 |


**返回值:** [Phaser.Structs.List](/api/class/structs-list) - 此列表对象 。


> 源码：[src/structs/List.js#L189](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L189)  
引入版本：3.0.0


---

### swap {#swap}

#### \<instance> swap(child1, child2) {#instance-swapchild1-child2}


**说明:**

交换清单上两个物品的位置。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child1 | * | 否 | 首个换品. |
| child2 | * | 否 | 换掉的第二个项目 |


> 源码：[src/structs/List.js#L330](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/List.js#L330)  
引入版本：3.0.0


---

---
