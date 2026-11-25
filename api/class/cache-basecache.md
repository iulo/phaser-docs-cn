# BaseCache {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/cache-basecache)

Phaser框架用于缓存已装入资产和其他数据的密钥值存储。项目使用字符串键存储和检索。BaseCache在项目添加或移除时会发出事件,允许其他系统对缓存变化作出反应。多个BaseCache实例由缓存管理员拥有,每个资产类型(JSON,二进制,音频等)各一个,您也可以通过`CacheManager.addCustom()`创建自定义缓存.


**作用域**: static

> 源码：[src/cache/BaseCache.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/BaseCache.js#L12)  
引入版本：3.0.0

## 公开成员 {#public-members}

### entries {#entries}

#### entries: Phaser.Structs.Map.\<String, *> {#entries-phaserstructsmapstring}


**说明:**

缓存对象存储的地图 。

您可以直接查询地图或使用 BaseCache 方法。


> 源码：[src/cache/BaseCache.js#L31](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/BaseCache.js#L31)  
引入版本：3.0.0


---

### events {#events}

#### events: [Phaser.Events.EventEmitter](/api/class/events-eventemitter) {#events-phasereventseventemitter}


**说明:**

缓存用来发送相关事件的 EventEmitter 实例 。


> 源码：[src/cache/BaseCache.js#L42](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/BaseCache.js#L42)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(key, data) {#instance-addkey-data}


**说明:**

将项目添加到缓存中。 本项目以一个独特的字符串来引用, 您负责设置和保存该字符串的跟踪。 只能通过使用此字符串来获取 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 用于引用添加到缓存中的数据的独有密钥 。 |
| data | * | 否 | 存储在缓存中的数据 。 |


**返回值:** [Phaser.Cache.BaseCache](/api/class/cache-basecache) - 此 BaseCache 对象 。


**Fires:** [Phaser.Cache.Events#event:ADD](/api/event/cache-events#add)


> 源码：[src/cache/BaseCache.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/BaseCache.js#L52)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此缓存及其中的所有项目。 清除条目地图, 从 EventEmitter 中删除所有事件听众, 并取消内部引用 。


> 源码：[src/cache/BaseCache.js#L163](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/BaseCache.js#L163)  
引入版本：3.0.0


---

### exists {#exists}

#### \<instance> exists(key) {#instance-existskey}


**说明:**

检查此缓存是否包含一个匹配给定密钥的项目。 此选项与 `BaseCache.has` 执行相同的动作, 并由装入器直接调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 在此缓存中检查项目的唯一密钥 。 |


**返回值:** boolean - 如果缓存中包含一个匹配给定密钥的项目,则返回 `true`, 否则返回 `false` 。


> 源码：[src/cache/BaseCache.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/BaseCache.js#L90)  
引入版本：3.7.0


---

### get {#get}

#### \<instance> get(key) {#instance-getkey}


**说明:**

根据给定的密钥从缓存中获取项目 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 从此缓存中获取项目的唯一密钥 。 |


**返回值:** * - 缓存中的项目, 或者如果找不到匹配给定密钥的项目, 则使用 `null` 。


> 源码：[src/cache/BaseCache.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/BaseCache.js#L106)  
引入版本：3.0.0


---

### getKeys {#getKeys}

#### \<instance> getKeys() {#instance-getkeys}


**说明:**

返回此缓存中所有使用的密钥 。


**返回值:** Array.\<string> - 包含当前存储在此缓存中的所有密钥的字符串数组 。


> 源码：[src/cache/BaseCache.js#L150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/BaseCache.js#L150)  
引入版本：3.17.0


---

### has {#has}

#### \<instance> has(key) {#instance-haskey}


**说明:**

检查此缓存是否包含匹配给定密钥的项目。 这执行的动作与 `BaseCache.exists` 相同 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 在此缓存中检查项目的唯一密钥 。 |


**返回值:** boolean - 如果缓存中包含一个匹配给定密钥的项目,则返回 `true`, 否则返回 `false` 。


> 源码：[src/cache/BaseCache.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/BaseCache.js#L74)  
引入版本：3.0.0


---

### remove {#remove}

#### \<instance> remove(key) {#instance-removekey}


**说明:**

从此缓存中删除一个基于给定密钥的项目。

如果找到匹配密钥的条目, 则从缓存中移除, 并释放 `remove` 事件。 没有对项目进行额外检查。 如果您的游戏代码中的其他系统或部分依赖于此项目, 则您在删除项目之前应该先切断这些关系 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 从缓存中移除项目中唯一要使用的密钥 。 |


**返回值:** [Phaser.Cache.BaseCache](/api/class/cache-basecache) - 此 BaseCache 对象 。


**Fires:** [Phaser.Cache.Events#event:REMOVE](/api/event/cache-events#remove)


> 源码：[src/cache/BaseCache.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/BaseCache.js#L121)  
引入版本：3.0.0


---

---
