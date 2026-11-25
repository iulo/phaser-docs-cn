# DataManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/data-datamanager)

数据管理器提供了一种方法,可以存储、检索和管理任意的关于任何游戏对象、系统或插件的键值数据。每个条目都用字符串键存储,并可以持有任何值类型。

数据变化通过事件来传达:在创建新键时发生`setdata`事件起火,在更新现有值时发生`changedata` / `changedata-key`事件起火。这使得数据管理器非常适合驱动UI,触发游戏逻辑,或系统之间的同步状态.

母对象必须直接延伸`EventEmitter`,或者暴露一个名为`events`的属性,这是`EventEmitter`的一个例子.

**构造函数**

`new DataManager(parent, [eventEmitter])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | object | 否 | 此数据管理器所属对象。 |
| eventEmitter | [Phaser.Events.EventEmitter](/api/class/events-eventemitter) | 是 | 数据管理员事件发射器. |

---


**作用域**: static

> 源码：[src/data/DataManager.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L19)  
引入版本：3.0.0

## 公开成员 {#public-members}

### count {#count}

#### count: number {#count-number}


**说明:**

返回此数据管理器中的条目总数 。


> 源码：[src/data/DataManager.js#L689](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L689)  
引入版本：3.0.0


---

### events {#events}

#### events: [Phaser.Events.EventEmitter](/api/class/events-eventemitter) {#events-phasereventseventemitter}


**说明:**

数据管理员事件发射器.


> 源码：[src/data/DataManager.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L54)  
引入版本：3.0.0


---

### freeze {#freeze}

#### freeze: boolean {#freeze-boolean}


**说明:**

获取或设置此数据管理器的冻结状态。 被冻结的数据管理器将阻止所有创建新值或更新现有值的尝试 。


> 源码：[src/data/DataManager.js#L667](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L667)  
引入版本：3.0.0


---

### list {#list}

#### list: Object.\<string, *> {#list-objectstring}


**说明:**

数据列表.


> 源码：[src/data/DataManager.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L68)  
引入版本：3.0.0


---

### parent {#parent}

#### parent: * {#parent-1}


**说明:**

此数据管理器所属对象。


> 源码：[src/data/DataManager.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L45)  
引入版本：3.0.0


---

### values {#values}

#### values: Object.\<string, *> {#values-objectstring}


**说明:**

公共值列表。 您可以使用此选项访问您存储在此数据管理器中的任何内容。 例如, 如果您设置了一个名为 `gold` 的值, 您可以通过 :

```javascript
this.data.values.gold;
```

您也可以直接修改:

```javascript
this.data.values.gold += 1000;
```

这样做将发出来自此数据管理器母端的 `changedata`事件 。

不要直接修改此对象。 直接添加属性到此对象将不会释放任何事件。 总是使用 `DataManager.set` 来创建新项目 。


> 源码：[src/data/DataManager.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L78)  
引入版本：3.10.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此数据管理器。 所有存储的数据都被删除, 所有事件监听器被删除, 并且对父对象的引用被清除。 当父对象发出 `destroy`事件时, 自动调用 。


> 源码：[src/data/DataManager.js#L648](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L648)  
引入版本：3.0.0


---

### each {#each}

#### \<instance> each(callback, [context], [args]) {#instance-eachcallback-context-args}


**说明:**

将所有数据条目传递给给给定的调回。调回是数据管理器中每个条目的调回,接收母对象、键、值和向这种方法提供的其他参数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | DataEachCallback | 否 | 调用功能 。 |
| context | * | 是 | 执行回调时用作 `this` 值 。 |
| args | * | 是 | 附加参数,将传递到回调,在游戏对象,键,和数据之后. |


**返回值:** [Phaser.Data.DataManager](/api/class/data-datamanager) - 此数据管理器实例 。


> 源码：[src/data/DataManager.js#L427](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L427)  
引入版本：3.0.0


---

### get {#get}

#### \<instance> get(key) {#instance-getkey}


**说明:**

获取给定键的值,或者如果不存在,则未定义。

您也可以通过 `values` 对象访问值。 例如, 如果您有名为 `gold` 的键, 您也可以这样做 :

```javascript
this.data.get('gold');
```

或者直接访问值 :

```javascript
this.data.values.gold;
```

您也可以在一系列键中通过,在这种情况下,返回一系列的值:

```javascript
this.data.get([ 'gold', 'armor', 'health' ]);
```

这种方法对ES6中的分解数组有用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| Array.\<string> | 否 | 要检索的值的键, 或一系列键 。 |


**返回值:** * - 属于给定键的值,或一系列值,其顺序将匹配输入数组.


> 源码：[src/data/DataManager.js#L122](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L122)  
引入版本：3.0.0


---

### getAll {#getAll}

#### \<instance> getAll() {#instance-getall}


**说明:**

检索新对象中的所有数据值。


**返回值:** Object.\<string, *> - 所有数据值.


> 源码：[src/data/DataManager.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L173)  
引入版本：3.0.0


---

### has {#has}

#### \<instance> has(key) {#instance-haskey}


**说明:**

确定是否在此数据管理器中设置了给定的键 。

请注意, 键对大小写敏感, 并且必须是有效的 JavaScript对象属性字符串 。 这意味着 , 键 `gold` 和 `Gold` 被作为数据管理器内的两个独特的值处理 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 检查的钥匙。 |


**返回值:** boolean - 如果键存在, 返回 `true`, 否则返回 `false` 。


> 源码：[src/data/DataManager.js#L591](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L591)  
引入版本：3.0.0


---

### inc {#inc}

#### \<instance> inc(key, [amount]) {#instance-inckey-amount}


**说明:**

增加给定键的值。 如果键在数据管理器中不存在, 则在增加前以 0 的值创建 。

当键首次创建时, 将释放 `setdata` 事件。 如果键已经存在, 则将释放 `changedata` 事件和 `changedata-key` 事件, 将 `key` 替换为实际的键名 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 更改值的键 。 |
| amount | number | 是 | 1 | 将给定的键增加的金额。 传递负值来减少键 。 |


**返回值:** [Phaser.Data.DataManager](/api/class/data-datamanager) - 此数据管理器实例 。


**触发事件:** [Phaser.Data.Events#event:SET_DATA](/api/event/data-events#set_data), [Phaser.Data.Events#event:CHANGE_DATA](/api/event/data-events#change_data), [Phaser.Data.Events#event:CHANGE_DATA_KEY](/api/event/data-events#change_data_key)


> 源码：[src/data/DataManager.js#L291](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L291)  
引入版本：3.23.0


---

### merge {#merge}

#### \<instance> merge(data, [overwrite]) {#instance-mergedata-overwrite}


**说明:**

将给定的按键值对对象合并到此数据管理器中。

任何新建的值都会发出 `setdata`事件。任何更新的值(参见 `overwrite`参数) 都会发出 `changedata`事件 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| data | Object.\<string, *> | 否 |  | 数据要合并 。 |
| overwrite | boolean | 是 | true | 是否覆盖已有数据。 默认为真实 。 |


**返回值:** [Phaser.Data.DataManager](/api/class/data-datamanager) - 此数据管理器实例 。


**触发事件:** [Phaser.Data.Events#event:SET_DATA](/api/event/data-events#set_data), [Phaser.Data.Events#event:CHANGE_DATA](/api/event/data-events#change_data), [Phaser.Data.Events#event:CHANGE_DATA_KEY](/api/event/data-events#change_data_key)


> 源码：[src/data/DataManager.js#L461](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L461)  
引入版本：3.0.0


---

### pop {#pop}

#### \<instance> pop(key) {#instance-popkey}


**说明:**

获取与给定的“ key” 相关的数据, 从此数据管理器中删除, 然后返回 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 检索和删除值的键 。 |


**返回值:** * - 给定键的值 。


**触发事件:** [Phaser.Data.Events#event:REMOVE_DATA](/api/event/data-events#remove_data)


> 源码：[src/data/DataManager.js#L563](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L563)  
引入版本：3.0.0


---

### query {#query}

#### \<instance> query(search) {#instance-querysearch}


**说明:**

查询数据管理器中匹配给定正则表达式的键值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| search | RegExp | 否 | 正则表达式对象。如果一个非 RegExp 对象obj 被传递,则通过使用新的 RegExp(obj) 来暗示它转换成 RegExp 。 |


**返回值:** Object.\<string, *> - 匹配搜索字符串的键值 。


> 源码：[src/data/DataManager.js#L196](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L196)  
引入版本：3.0.0


---

### remove {#remove}

#### \<instance> remove(key) {#instance-removekey}


**说明:**

删除给定的键值 。

如果在此数据管理器中找到键, 则从内部列表中删除, 并释放 `removedata` 事件 。

您也可以在一系列键中通过,在这种情况下,该数组中的所有键都会被删除:

```javascript
this.data.remove([ 'gold', 'armor', 'health' ]);
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| Array.\<string> | 否 | 删除键,或删除的键数组 。 |


**返回值:** [Phaser.Data.DataManager](/api/class/data-datamanager) - 此数据管理器实例 。


**触发事件:** [Phaser.Data.Events#event:REMOVE_DATA](/api/event/data-events#remove_data)


> 源码：[src/data/DataManager.js#L494](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L494)  
引入版本：3.0.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

删除此数据管理器中的所有数据并解冻它 。


**返回值:** [Phaser.Data.DataManager](/api/class/data-datamanager) - 此数据管理器实例 。


> 源码：[src/data/DataManager.js#L627](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L627)  
引入版本：3.0.0


---

### set {#set}

#### \<instance> set(key, [data]) {#instance-setkey-data}


**说明:**

设置给定键的值。如果键在数据管理器中不存在,则该键将被创建。

```javascript
data.set('name', 'Red Gem Stone');
```

您也可以在键值对的对象中通过,作为第一个参数:

```javascript
data.set({ name: 'Red Gem Stone', level: 2, owner: 'Link', gold: 50 });
```

为了重新获得一个值,你可以叫`get`:

```javascript
data.get('gold');
```

或者你可以直接通过`values`属性访问该值,在那里它像其他变量一样工作:

```javascript
data.values.gold += 50;
```

当值被首次设定时, 将释放 `setdata` 事件 。

如果键已经存在, 则会沿着以键命名的事件释放 `changedata`事件。 例如, 如果您更新了一个名为 `PlayerLives` 的现有键, 它会释放该事件 `changedata-PlayerLives`。 这些事件将会释放, 无论您使用这种方法设置值, 或直接的 `values` 设置器 。

请注意, 数据键是区分大小写, 必须有效 JavaScript 对象属性字符串。 这意味着, 数据管理器内将键 `gold` 和 `Gold` 视为两个独特的值 。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| object | 否 | 设置值的键。 或者按键值对的对象。 如果对象忽略 `data` 参数 。 |
| data | * | 是 | 给定键设置的值。 如果一个对象作为键提供, 此参数将被忽略 。 |


**返回值:** [Phaser.Data.DataManager](/api/class/data-datamanager) - 此数据管理器实例 。


**触发事件:** [Phaser.Data.Events#event:SET_DATA](/api/event/data-events#set_data), [Phaser.Data.Events#event:CHANGE_DATA](/api/event/data-events#change_data), [Phaser.Data.Events#event:CHANGE_DATA_KEY](/api/event/data-events#change_data_key)


> 源码：[src/data/DataManager.js#L221](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L221)  
引入版本：3.0.0


---

### setFreeze {#setFreeze}

#### \<instance> setFreeze(value) {#instance-setfreezevalue}


**说明:**

冻结或解冻此数据管理器。 冻结的数据管理器将屏蔽所有创建新值或更新现有值的尝试 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 是否冻结或解冻数据管理器 。 |


**返回值:** [Phaser.Data.DataManager](/api/class/data-datamanager) - 此数据管理器实例 。


> 源码：[src/data/DataManager.js#L609](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L609)  
引入版本：3.0.0


---

### toggle {#toggle}

#### \<instance> toggle(key) {#instance-togglekey}


**说明:**

切换给定键的布尔值。 如果键在数据管理器中不存在, 那么在切换前, 将创建 `false` 的值 。

当键首次创建时, 将释放 `setdata` 事件。 如果键已经存在, 则将释放 `changedata` 事件和 `changedata-key` 事件, 将 `key` 替换为实际的键名 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 切换值的关键 。 |


**返回值:** [Phaser.Data.DataManager](/api/class/data-datamanager) - 此数据管理器实例 。


**触发事件:** [Phaser.Data.Events#event:SET_DATA](/api/event/data-events#set_data), [Phaser.Data.Events#event:CHANGE_DATA](/api/event/data-events#change_data), [Phaser.Data.Events#event:CHANGE_DATA_KEY](/api/event/data-events#change_data_key)


> 源码：[src/data/DataManager.js#L332](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManager.js#L332)  
引入版本：3.23.0


---

---
