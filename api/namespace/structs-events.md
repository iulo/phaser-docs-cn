# Phaser.Structs.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/structs-events)

Scope: 
static
> 源码：[src/structs/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/events/index.js#L7)  


## 静态函数 {#static-functions}

### PROCESS_QUEUE_ADD {#PROCESS_QUEUE_ADD}

#### PROCESS_QUEUE_ADD {#process_queue_add}


**说明:**

进程队列添加事件 。

当新项目成功移动到其活动列表时,此事件由进程队列发送 。

您最常看到在添加新的游戏对象时 Scene 更新列表中使用的 。

以这个例子,从场景中听这个事件,使用:`this.sys.updateList.on('add', listener)`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| item | * | 否 | 添加到进程队列的项目 。 |


> 源码：[src/structs/events/PROCESS_QUEUE_ADD_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/events/PROCESS_QUEUE_ADD_EVENT.js#L7)  
引入版本：3.20.0


---

### PROCESS_QUEUE_REMOVE {#PROCESS_QUEUE_REMOVE}

#### PROCESS_QUEUE_REMOVE {#process_queue_remove}


**说明:**

进程队列删除事件 。

当新项目成功从活动列表中删除时, 进程队列会发出此事件 。

您最常看到游戏对象被删除时 Scene 更新列表使用的此功能 。

以这个例子,从场景中听这个事件,使用:`this.sys.updateList.on('remove', listener)`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| item | * | 否 | 进程队列中删除的项目 。 |


> 源码：[src/structs/events/PROCESS_QUEUE_REMOVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/events/PROCESS_QUEUE_REMOVE_EVENT.js#L7)  
引入版本：3.20.0


---

---
