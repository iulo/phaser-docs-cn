# ProcessQueue {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/structs-processqueue)

A 进程队列维持三个内部列表.

`pending`列表是一组在下一次更新中将被“激活”的项目。 `active`列表是一组被认为活动且应当更新的项目。 `destroy`列表是一组正在运行且等待下一次更新中销毁的项目。

当进程队列中添加新项目时,它们被放在待处理的列表中,而不是立即添加到活动列表中。同样,被删除的项目被放到销毁列表中,而不是立即销毁。这使得进程队列可以在特定的固定时间而不是API请求时仔细处理每个项目。

进程队列在 Phaser 中被广泛用于安全管理相机、插件和场景系统等对象的集合,在活动更新循环中可以添加或删除项目。通过将添加和清除推迟到更新之间的控制点,可以避免在更新过程中修改列表时产生的错误。

队列延长了EventEmitter,当一个项目活动时点火`Phaser.Structs.Events#PROCESS_QUEUE_ADD`,当一个项目被移除时点火`Phaser.Structs.Events#PROCESS_QUEUE_REMOVE`。


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/structs/ProcessQueue.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/ProcessQueue.js#L11)  
引入版本：3.0.0

## 公开成员 {#public-members}

### checkQueue {#checkQueue}

#### checkQueue: boolean {#checkqueue-boolean}


**说明:**

如果队列中只允许`true`独有的对象,则阻止同一项目被添加一次以上.


> 源码：[src/structs/ProcessQueue.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/ProcessQueue.js#L100)  
引入版本：3.50.0


---

### length {#length}

#### length: number {#length-number}


**说明:**

活动列表中的条目数 。


> 源码：[src/structs/ProcessQueue.js#L351](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/ProcessQueue.js#L351)  
引入版本：3.20.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Events.EventEmitter](/api/class/events-eventemitter):**


 - [addListener](/api/class/events-eventemitter#addListener)
 - [emit](/api/class/events-eventemitter#emit)
 - [eventNames](/api/class/events-eventemitter#eventNames)
 - [listenerCount](/api/class/events-eventemitter#listenerCount)
 - [listeners](/api/class/events-eventemitter#listeners)
 - [off](/api/class/events-eventemitter#off)
 - [on](/api/class/events-eventemitter#on)
 - [once](/api/class/events-eventemitter#once)
 - [removeAllListeners](/api/class/events-eventemitter#removeAllListeners)
 - [removeListener](/api/class/events-eventemitter#removeListener)
 - [shutdown](/api/class/events-eventemitter#shutdown)




---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(item) {#instance-additem}


**说明:**

向进程队列添加新项目。

这个项目被列入待处理清单,并在下一次更新中积极发挥作用。

**Tags:**

 - genericUse
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| item | * | 否 | 添加到队列中的项目 。 |


**返回值:** * - 所加项目.


> 源码：[src/structs/ProcessQueue.js#L164](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/ProcessQueue.js#L164)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

立即销毁此进程队列,清除其所有内部阵列并重置进程总计.


**Overrides:** Phaser.Events.EventEmitter#销毁


> 源码：[src/structs/ProcessQueue.js#L368](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/ProcessQueue.js#L368)  
引入版本：3.0.0


---

### getActive {#getActive}

#### \<instance> getActive() {#instance-getactive}


**说明:**

返回当前活动项目列表。

此方法返回对活动列表数组的引用,而不是复制。 因此, 注意不要在进程队列之外修改此数组 。

**Tags:**

 - genericUse


**返回值:** Array.\<*> - 活动项目列表 。


> 源码：[src/structs/ProcessQueue.js#L333](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/ProcessQueue.js#L333)  
引入版本：3.0.0


---

### isActive {#isActive}

#### \<instance> isActive(item) {#instance-isactiveitem}


**说明:**

检查给定的项目,看看它是否已经活跃在这个进程队列中 。

**Tags:**

 - genericUse
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| item | * | 否 | 检查的项目。 |


**返回值:** boolean - 如果物品是活动式的,则使用`true`,否则使用`false`.


> 源码：[src/structs/ProcessQueue.js#L110](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/ProcessQueue.js#L110)  
引入版本：3.60.0


---

### isDestroying {#isDestroying}

#### \<instance> isDestroying(item) {#instance-isdestroyingitem}


**说明:**

检查给定的项目, 以查看是否它已经等待从此进程队列中销毁 。

**Tags:**

 - genericUse
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| item | * | 否 | 检查的项目。 |


**返回值:** boolean - 如果物品待销毁,则使用`true`,否则使用`false`.


> 源码：[src/structs/ProcessQueue.js#L146](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/ProcessQueue.js#L146)  
引入版本：3.60.0


---

### isPending {#isPending}

#### \<instance> isPending(item) {#instance-ispendingitem}


**说明:**

检查给定的项目, 以查看是否它已经待添加到此进程队列中 。

**Tags:**

 - genericUse
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| item | * | 否 | 检查的项目。 |


**返回值:** boolean - 如果物品待插入,则使用`true`,否则使用`false`.


> 源码：[src/structs/ProcessQueue.js#L128](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/ProcessQueue.js#L128)  
引入版本：3.60.0


---

### remove {#remove}

#### \<instance> remove(item) {#instance-removeitem}


**说明:**

从进程队列中删除项目。

这个项目被添加到"毁灭"列表中,并在下一次更新中被完全删除.

**Tags:**

 - genericUse
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| item | * | 否 | 队列中要删除的项目 。 |


**返回值:** * - 被移除的物品。


> 源码：[src/structs/ProcessQueue.js#L194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/ProcessQueue.js#L194)  
引入版本：3.0.0


---

### removeAll {#removeAll}

#### \<instance> removeAll() {#instance-removeall}


**说明:**

从此进程队列中删除所有活动项目。

所有物品都标注为"待销毁",并在下一次更新中全部删除.


**返回值:** [Phaser.Structs.ProcessQueue](/api/class/structs-processqueue) - 此进程队列对象 。


> 源码：[src/structs/ProcessQueue.js#L238](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/ProcessQueue.js#L238)  
引入版本：3.20.0


---

### update {#update}

#### \<instance> update() {#instance-update}


**说明:**

更新此队列。 首先, 它会处理任何待销毁的项目, 并删除它们 。

然后它会检查是否有待插入的项目,然后移动到活动状态。最后,它会返回活动项目清单,供进一步处理。

**Tags:**

 - genericUse


**返回值:** Array.\<*> - 活动项目列表 。


> 源码：[src/structs/ProcessQueue.js#L264](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/ProcessQueue.js#L264)  
引入版本：3.0.0


---

---
