# Map {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/structs-map)

自定义的地图执行, 将条目作为按键值对和顺序重置的重置存储。 它与本地的 JavaScript 地图不同, 也维护一个内部条目阵列, 用于高效的索引访问和重置。 支持过滤、 合并和包含/ 大小操作。 内部由各种 Phaser 系统管理收藏 。

```javascript
var map = new Map([
   [ 1, 'one' ],
   [ 2, 'two' ],
   [ 3, 'three' ]
]);
```

**构造函数**

`new Map(elements)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| elements | Array.\<*> | 否 | 用于填充此地图的可选键值对数组 。 |

---


**作用域**: static

> 源码：[src/structs/Map.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L18)  
引入版本：3.0.0

## 公开成员 {#public-members}

### entries {#entries}

#### entries: Object.\<string, *> {#entries-objectstring}


**说明:**

本地图中的条目 。

**标签:**

 - genericUse


> 源码：[src/structs/Map.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L50)  
引入版本：3.0.0


---

### size {#size}

#### size: number {#size-number}


**说明:**

本地图中键/值对的数目 。


> 源码：[src/structs/Map.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L62)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### clear {#clear}

#### \<instance> clear() {#instance-clear}


**说明:**

从此地图中删除所有条目 。

**标签:**

 - genericUse


**返回值:** [Phaser.Structs.Map](/api/class/structs-map) - 此地图对象 。


> 源码：[src/structs/Map.js#L220](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L220)  
引入版本：3.0.0


---

### contains {#contains}

#### \<instance> contains(value) {#instance-containsvalue}


**说明:**

如果此地图中存在值, 返回 `true`。 否则, 返回 `false` 。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | * | 否 | 寻之值. |


**返回值:** boolean - 如果找到值,则使用`true`,否则使用`false`.


> 源码：[src/structs/Map.js#L333](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L333)  
引入版本：3.0.0


---

### delete {#delete}

#### \<instance> delete(key) {#instance-deletekey}


**说明:**

从此地图中删除指定的元素 。

**标签:**

 - genericUse
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 从此地图中删除元素的键 。 |


**返回值:** [Phaser.Structs.Map](/api/class/structs-map) - 此地图对象 。


> 源码：[src/structs/Map.js#L196](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L196)  
引入版本：3.0.0


---

### dump {#dump}

#### \<instance> dump() {#instance-dump}


**说明:**

通过`console.group`将地图的内容丢弃到控制台.


> 源码：[src/structs/Map.js#L281](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L281)  
引入版本：3.0.0


---

### each {#each}

#### \<instance> each(callback) {#instance-eachcallback}


**说明:**

将本地图的所有条目进行迭代,将每个条目传递给给定的回调 。

如果回调返回 `false`,重复会断裂.

**标签:**

 - genericUse
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | EachMapCallback | 否 | 接收此地图中控有的键和条目的回调 。 |


**返回值:** [Phaser.Structs.Map](/api/class/structs-map) - 此地图对象 。


> 源码：[src/structs/Map.js#L303](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L303)  
引入版本：3.0.0


---

### get {#get}

#### \<instance> get(key) {#instance-getkey}


**说明:**

返回与 `key` 或 `undefined` 相关的数值,如果没有的话。

**标签:**

 - genericUse
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 从 `Map` 对象返回的元素的键 。 |


**返回值:** * - 如果无法在此地图对象中找到指定的键或 `undefined` , 则与该键相关的元素 。


> 源码：[src/structs/Map.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L135)  
引入版本：3.0.0


---

### getArray {#getArray}

#### \<instance> getArray() {#instance-getarray}


**说明:**

返回此地图中存储的所有值的 `Array` 。

**标签:**

 - genericUse


**返回值:** Array.\<*> - 此地图中存储的数值阵列 。


> 源码：[src/structs/Map.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L156)  
引入版本：3.0.0


---

### has {#has}

#### \<instance> has(key) {#instance-haskey}


**说明:**

返回布尔表示一个带有指定键的元素是否存在。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 测试此地图中存在的元素键 。 |


**返回值:** boolean - 如果本地图中存在指定的键元素, 返回 `true`, 否则返回 `false` 。


> 源码：[src/structs/Map.js#L179](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L179)  
引入版本：3.0.0


---

### keys {#keys}

#### \<instance> keys() {#instance-keys}


**说明:**

返回此地图中所有条目键的数组。

**标签:**

 - genericUse


**返回值:** Array.\<string> - 包含条目键的矩阵 。


> 源码：[src/structs/Map.js#L243](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L243)  
引入版本：3.0.0


---

### merge {#merge}

#### \<instance> merge(map, [override]) {#instance-mergemap-override}


**说明:**

将给定的地图中的所有新键合并到此地图中。 如果遇到已经存在的键, 除非设置为 `true` , 否则将跳过 。

**标签:**

 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| map | [Phaser.Structs.Map](/api/class/structs-map) | 否 |  | 要合并到此地图的地图 。 |
| override | boolean | 是 | false | 设定为 `true` , 以源地图中的值替换此地图中的值, 或者 `false` 来跳过它们 。 |


**返回值:** [Phaser.Structs.Map](/api/class/structs-map) - 此地图对象 。


> 源码：[src/structs/Map.js#L360](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L360)  
引入版本：3.0.0


---

### set {#set}

#### \<instance> set(key, value) {#instance-setkey-value}


**说明:**

在此地图中添加一个带有指定的 `key` 和 `value` 元素 。

如果 `key` 已经存在,则该值将被替换 。

如果您希望在一次呼叫中添加多个元素,则使用`setAll`方法代替.

**标签:**

 - genericUse
 - genericUse
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 添加到此地图的元素键 。 |
| value | * | 否 | 添加到此地图的元素值 。 |


**返回值:** [Phaser.Structs.Map](/api/class/structs-map) - 此地图对象 。


> 源码：[src/structs/Map.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L104)  
引入版本：3.0.0


---

### setAll {#setAll}

#### \<instance> setAll(elements) {#instance-setallelements}


**说明:**

将给定数组中的所有元素添加到此地图中。

如果键已经存在, 则该值将被替换 。

**标签:**

 - generic
 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| elements | Array.\<*> | 否 | 要填充此地图, 需要一系列的键值对 。 |


**返回值:** [Phaser.Structs.Map](/api/class/structs-map) - 此地图对象 。


> 源码：[src/structs/Map.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L75)  
引入版本：3.70.0


---

### values {#values}

#### \<instance> values() {#instance-values}


**说明:**

返回此地图中存储的所有值的 `Array` 。

**标签:**

 - genericUse


**返回值:** Array.\<*> - 价值的`Array`。


> 源码：[src/structs/Map.js#L258](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Map.js#L258)  
引入版本：3.0.0


---

---
