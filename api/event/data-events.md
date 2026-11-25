# Data.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/data-events)

## CHANGE_DATA {#change_data}


**说明:** 变化数据事件.

当数据存储中的项目被更改时, 数据管理器会发送此事件 。

启用数据的游戏对象在 `data` 属性下有一个数据管理器实例。 因此, 需要聆听 。
将使用游戏对象的更改数据事件: `sprite.on('changedata', listener)`。

此事件将发送到数据管理器中更改的所有项目 。
要查看特定项目的更改,请使用 `CHANGE_DATA_KEY_EVENT` 事件.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | any | 否 | 引用此事件的数据管理器所属对象 。 |
| key | string | 否 | 数据管理器内数据项的独有密钥 。 |
| value | any | 否 | 数据管理器中此项目的新值 。 |
| previousValue | any | 否 | 数据管理器中此项目的上一个值 。 |

**Member of:** [Phaser.Data.Events](/api/namespace/data-events)
> 源码：[src/data/events/CHANGE_DATA_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/events/CHANGE_DATA_EVENT.js#L7)  
引入版本：3.0.0

## CHANGE_DATA_KEY {#change_data_key}


**说明:** 变化数据密钥事件.

当数据存储中的项目被更改时, 数据管理器会发送此事件 。

启用数据的游戏对象在 `data` 属性下有一个数据管理器实例。 因此, 需要聆听 。
从您将使用的游戏对象中更改一个特定数据项: `sprite.on('changedata-key', listener)`,
中 `key` 是数据项中唯一的字符串键。例如,如果您存储了一个名为 `gold`的数据项
然后你可以听`sprite.on('changedata-gold')`。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | any | 否 | 引用了拥有负责此事件的数据管理器实例的对象 。 |
| value | any | 否 | 在数据管理器中更新的项目。 它可以是任意的数据类型, 即字符串、 布尔、 数字、 对象或实例 。 |
| previousValue | any | 否 | 数据管理器中更新的上一个项目。 它可以是任意的数据类型, 即字符串、 布尔、 数字、 对象或实例 。 |

**Member of:** [Phaser.Data.Events](/api/namespace/data-events)
> 源码：[src/data/events/CHANGE_DATA_KEY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/events/CHANGE_DATA_KEY_EVENT.js#L7)  
引入版本：3.16.1

## DESTROY {#destroy}


**说明:** 数据管理器毁灭事件 。

数据管理器会从母公司那里听断事件,然后关闭自己.

**Member of:** [Phaser.Data.Events](/api/namespace/data-events)
> 源码：[src/data/events/DESTROY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/events/DESTROY_EVENT.js#L7)  
引入版本：3.50.0

## REMOVE_DATA {#remove_data}


**说明:** 删除数据事件 。

当项目被删除时, 数据管理器会发出此事件 。

启用数据的游戏对象在 `data` 属性下有一个数据管理器实例。 因此, 需要聆听 。
将您将使用的游戏对象上的数据项删除: `sprite.on('removedata', listener)`。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | any | 否 | 引用了拥有负责此事件的数据管理器实例的对象 。 |
| key | string | 否 | 数据管理器内数据项的独有密钥 。 |
| data | any | 否 | 从数据管理器中删除的项目。 这可能是任意的数据类型, 即字符串、 布尔、 数字、 对象或实例 。 |

**Member of:** [Phaser.Data.Events](/api/namespace/data-events)
> 源码：[src/data/events/REMOVE_DATA_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/events/REMOVE_DATA_EVENT.js#L7)  
引入版本：3.0.0

## SET_DATA {#set_data}


**说明:** 集数据事件.

当数据存储中添加新项目时, 数据管理器会发出此事件 。

启用数据的游戏对象在 `data` 属性下有一个数据管理器实例。 因此, 需要聆听 。
添加到您将使用的游戏对象上的新数据项: `sprite.on('setdata', listener)`。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | any | 否 | 引用了拥有负责此事件的数据管理器实例的对象 。 |
| key | string | 否 | 数据管理器内数据项的独有密钥 。 |
| data | any | 否 | 添加到数据管理器中的项目。 它可以是任意的数据类型, 即字符串、 布尔、 数字、 对象或实例 。 |

**Member of:** [Phaser.Data.Events](/api/namespace/data-events)
> 源码：[src/data/events/SET_DATA_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/events/SET_DATA_EVENT.js#L7)  
引入版本：3.0.0

---
