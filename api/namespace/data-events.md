# Phaser.Data.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/data-events)

Scope: 
static
> 源码：[src/data/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/events/index.js#L7)  


## 静态函数 {#static-functions}

### CHANGE_DATA {#CHANGE_DATA}

#### CHANGE_DATA {#change_data}


**说明:**

变化数据事件.

当数据存储中的项目被更改时, 数据管理器会发送此事件 。

启用数据的游戏对象在 `data` 属性下有一个数据管理器实例。 因此, 要从您使用的游戏对象中听到一个更改数据事件: `sprite.on('changedata', listener)` 。

此事件将发送到数据管理器中所有更改的项目。 要查看特定项目的更改, 请使用 `CHANGE_DATA_KEY_EVENT` 事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | any | 否 | 引用此事件的数据管理器所属对象 。 |
| key | string | 否 | 数据管理器内数据项的独有键 。 |
| value | any | 否 | 数据管理器中此项目的新值 。 |
| previousValue | any | 否 | 数据管理器中此项目的上一个值 。 |


> 源码：[src/data/events/CHANGE_DATA_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/events/CHANGE_DATA_EVENT.js#L7)  
引入版本：3.0.0


---

### CHANGE_DATA_KEY {#CHANGE_DATA_KEY}

#### CHANGE_DATA_KEY {#change_data_key}


**说明:**

变化数据键事件.

当数据存储中的项目被更改时, 数据管理器会发送此事件 。

启用数据的游戏对象在 `data` 属性下有一个数据管理器实例。 因此, 要从您使用的游戏对象中查看特定数据项的更改: `sprite.on('changedata-key', listener)`, 其中 `key` 是数据项中唯一的字符串键。 例如, 如果您存储了一个名为 `gold` 的数据项, 您可以为 `sprite.on('changedata-gold')` 的用户收听 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | any | 否 | 引用了拥有负责此事件的数据管理器实例的对象 。 |
| value | any | 否 | 在数据管理器中更新的项目。 它可以是任意的数据类型, 即字符串、 布尔、 数字、 对象或实例 。 |
| previousValue | any | 否 | 数据管理器中更新的上一个项目。 它可以是任意的数据类型, 即字符串、 布尔、 数字、 对象或实例 。 |


> 源码：[src/data/events/CHANGE_DATA_KEY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/events/CHANGE_DATA_KEY_EVENT.js#L7)  
引入版本：3.16.1


---

### DESTROY {#DESTROY}

#### DESTROY {#destroy}


**说明:**

数据管理器毁灭事件 。

数据管理器会从母公司那里听断事件,然后关闭自己.


> 源码：[src/data/events/DESTROY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/events/DESTROY_EVENT.js#L7)  
引入版本：3.50.0


---

### REMOVE_DATA {#REMOVE_DATA}

#### REMOVE_DATA {#remove_data}


**说明:**

删除数据事件 。

当项目被删除时, 数据管理器会发出此事件 。

启用数据的游戏对象在 `data` 属性下有一个数据管理器的例子。 因此, 想要听到您将使用的 Game Object 上的数据项删除: `sprite.on('removedata', listener)` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | any | 否 | 引用了拥有负责此事件的数据管理器实例的对象 。 |
| key | string | 否 | 数据管理器内数据项的独有键 。 |
| data | any | 否 | 从数据管理器中删除的项目。 这可能是任意的数据类型, 即字符串、 布尔、 数字、 对象或实例 。 |


> 源码：[src/data/events/REMOVE_DATA_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/events/REMOVE_DATA_EVENT.js#L7)  
引入版本：3.0.0


---

### SET_DATA {#SET_DATA}

#### SET_DATA {#set_data}


**说明:**

集数据事件.

当数据存储中添加新项目时, 数据管理器会发出此事件 。

启用数据的游戏对象在 `data` 属性下有一个数据管理器的例子。 因此, 想要在您使用的游戏对象上输入一个新的数据项: `sprite.on('setdata', listener)` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | any | 否 | 引用了拥有负责此事件的数据管理器实例的对象 。 |
| key | string | 否 | 数据管理器内数据项的独有键 。 |
| data | any | 否 | 添加到数据管理器中的项目。 它可以是任意的数据类型, 即字符串、 布尔、 数字、 对象或实例 。 |


> 源码：[src/data/events/SET_DATA_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/events/SET_DATA_EVENT.js#L7)  
引入版本：3.0.0


---

---
