# RTree {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/structs-rtree)

RBush是用于点和矩形的2D空间索引的高性能JavaScript库,它基于一个最优化的R-tree数据结构,并有批量插入支持.

空间索引是用于点和矩的特殊数据结构,可以使您非常高效地执行像"此边框内的所有项目"这样的查询(例如比环绕所有项目的速度快数百倍).

这个版本的RBush使用`[ '.left', '.top', '.right', '.bottom' ]`的固定的min/max存取器结构,这是为了避免原始库使用的eval类函数创建,这导致了CSP政策违规.

由弗拉基米尔·阿加丰金从[https://github.com/mourner/rbush](https://github.com/mourner/rbush) 上叉出


**作用域**: static

> 源码：[src/structs/RTree.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/RTree.js#L10)  
引入版本：3.0.0

## 公开方法 {#public-methods}

### all {#all}

#### \<instance> all() {#instance-all}


**说明:**

返回 RTree 中存储的所有项目为平方阵列。


**返回值:** Array.\<any> - 包含当前存储在树上的所有项目的阵列 。


> 源码：[src/structs/RTree.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/RTree.js#L44)  
引入版本：3.0.0


---

### clear {#clear}

#### \<instance> clear() {#instance-clear}


**说明:**

从RTree中删除所有项目,将其重置为空状态。


**返回值:** [Phaser.Structs.RTree](/api/class/structs-rtree) - 这个RTree的例子,用于链条。


> 源码：[src/structs/RTree.js#L203](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/RTree.js#L203)  
引入版本：3.0.0


---

### collides {#collides}

#### \<instance> collides(bbox) {#instance-collidesbbox}


**说明:**

测试RTree中的任何项目是否与给定的边框相交.

与`search`不同,这种方法在发现第一个交叉点后立即停止,当只需要知道碰撞是否存在而不是检索所有结果时,就使它更加有效.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bbox | Object | 否 | 定界盒必须具有`minX`,`minY`,`maxX`,以及`maxY`的特性. |


**返回值:** boolean - 如果树上的任何物品与边框相交,则`true`,否则则`false`.


> 源码：[src/structs/RTree.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/RTree.js#L96)  
引入版本：3.0.0


---

### compareMinX {#compareMinX}

#### \<instance> compareMinX(a, b) {#instance-compareminxa-b}


**说明:**

用于按最小X边界(`left`属性)排序物品的比较函数。

如果返回负数,则返回负数 `a` 应在 `b`,如果在之后是正数,则是零,如果等于。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | Object | 否 | 初标比品. |
| b | Object | 否 | 第二品以比较. |


**返回值:** number - 两种项目的`left`值的差值。


> 源码：[src/structs/RTree.js#L569](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/RTree.js#L569)  
引入版本：3.0.0


---

### compareMinY {#compareMinY}

#### \<instance> compareMinY(a, b) {#instance-compareminya-b}


**说明:**

用于按最小 Y 边界( `top` 属性) 排序项目的比较函数。

如果返回负数,则返回负数 `a` 应在 `b`,如果在之后是正数,则是零,如果等于。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | Object | 否 | 初标比品. |
| b | Object | 否 | 第二品以比较. |


**返回值:** number - 两种项目的`top`值的差值。


> 源码：[src/structs/RTree.js#L587](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/RTree.js#L587)  
引入版本：3.0.0


---

### fromJSON {#fromJSON}

#### \<instance> fromJSON(data) {#instance-fromjsondata}


**说明:**

将这个RTree与先前通过`toJSON`输出的数据相匹配.

这使得一棵树可以被序列化和还原,而无需单独重新插入每个项目.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | Object | 否 | 需要导入的树数据, 由 `toJSON` 返回 。 |


**返回值:** [Phaser.Structs.RTree](/api/class/structs-rtree) - 这个RTree的例子,用于链条。


> 源码：[src/structs/RTree.js#L299](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/RTree.js#L299)  
引入版本：3.0.0


---

### insert {#insert}

#### \<instance> insert(item) {#instance-insertitem}


**说明:**

将单个项目插入RTree。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| item | * | 否 | 要插入的项目。必须 `left`, `top`, `right`,和 `bottom` 属性。 |


**返回值:** [Phaser.Structs.RTree](/api/class/structs-rtree) - 这个RTree的例子,用于链条。


> 源码：[src/structs/RTree.js#L187](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/RTree.js#L187)  
引入版本：3.0.0


---

### load {#load}

#### \<instance> load(data) {#instance-loaddata}


**说明:**

散装将一系列项目装入RTree。

散装加载比在添加大数据集时逐个插入项目要高效得多,因为它使用OMT算法在单段通道中构建了结构优化的树。如果数组小于最小的输入阈值,则单独插入项目。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | Array.\<any> | 否 | 要插入的数组项目。 每个项目必须具有`left`、`top`、`right`和`bottom`的特性。 |


**返回值:** [Phaser.Structs.RTree](/api/class/structs-rtree) - 这个RTree的例子,用于链条。


> 源码：[src/structs/RTree.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/RTree.js#L136)  
引入版本：3.0.0


---

### remove {#remove}

#### \<instance> remove(item, [equalsFn]) {#instance-removeitem-equalsfn}


**说明:**

从RTree中删除单个项目。

可以通过一个可选的等值函数来比较项目的价值,而不是参考,当原始项目引用不可用时,该函数会有所帮助。该函数收到两个项目,如果它们被认为是等值,则应当返回 `true`。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| item | * | 否 | 移除的项目 。 |
| equalsFn | function | 是 | 选择自定义平等功能可带两个项目并返回布尔值 。 |


**返回值:** [Phaser.Structs.RTree](/api/class/structs-rtree) - 这个RTree的例子,用于链条。


> 源码：[src/structs/RTree.js#L217](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/RTree.js#L217)  
引入版本：3.0.0


---

### search {#search}

#### \<instance> search(bbox) {#instance-searchbbox}


**说明:**

搜索所有与指定边框相交的项,并将其作为数组返回。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bbox | Object | 否 | 内置的边框。必须 `minX`, `minY`, `maxX`,和 `maxY` 属性。 |


**返回值:** Array.\<any> - 树上与给定的边框交叉的所有项目阵列。


> 源码：[src/structs/RTree.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/RTree.js#L57)  
引入版本：3.0.0


---

### toBBox {#toBBox}

#### \<instance> toBBox(a) {#instance-tobboxa}


**说明:**

将 Phaser 风格的边框对象转换为 RTree 所使用的内部边框格式。

地图 `left`, `top`, `right`,和 `bottom` 输入到 `minX`, `minY`, `maxX`,和 `maxY` 分别是R-tree算法所期望的格式.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | Object | 否 | 要转换的对象。 必须是 `left`, `top`, `right`,和 `bottom` 属性。 |


**返回值:** Object - 装有`minX`,`minY`,`maxX`的边框对象,以及`maxY`的特性.


> 源码：[src/structs/RTree.js#L605](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/RTree.js#L605)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

返回原始的内部树数据为 JSON 兼容对象。

返回的值可以传递到`fromJSON`,以便在稍后点恢复树状态.


**返回值:** Object - 内树数据对象.


> 源码：[src/structs/RTree.js#L287](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/RTree.js#L287)  
引入版本：3.0.0


---

---
