# EventEmitter {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/events-eventemitter)

`EventEmitter` 封装了 `eventemitter3` 库，可作为场景系统中的插件。Phaser 用它在游戏对象、场景和各个系统之间传递事件。

每个场景都提供 `scene.events`。许多 Phaser 对象也会继承或内置事件发射器。用 `on` 或 `addListener` 注册持续监听器，用 `once` 注册触发后自动移除的一次性监听器，用 `off` 或 `removeListener` 移除监听器。

需要独立的事件总线时，也可以直接创建 `EventEmitter` 实例。

**作用域**: static

> 源码：[src/events/EventEmitter.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/events/EventEmitter.js#L11)  
引入版本：3.0.0

## 公开方法 {#public-methods}

### addListener {#addListener}

#### \<instance> addListener(event, fn, [context]) {#instance-addlistenerevent-fn-context}


**说明:**

为指定事件添加一个监听器 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| event | string \| symbol | 否 |  | 事件名称. |
| fn | function | 否 |  | 听者功能. |
| context | * | 是 | "this" | 用来引用监听器的上下文 。 |


**返回值:** [Phaser.Events.EventEmitter](/api/class/events-eventemitter) - `this`.


> 源码：[src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v4.1.0/src/events/EventEmitter.js#L124)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

从 EventEmitter 中删除所有监听器, 并将其准备用于垃圾收集。 当母对象被销毁时, 此方法会自动调用, 除非您正在手动拆卸该发送器, 否则不应直接调用 。


> 源码：[src/events/EventEmitter.js#L53](https://github.com/phaserjs/phaser/blob/v4.1.0/src/events/EventEmitter.js#L53)  
引入版本：3.0.0


---

### emit {#emit}

#### \<instance> emit(event, [args]) {#instance-emitevent-args}


**说明:**

给每个注册参加特定活动的监听器打电话。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | string \| symbol | 否 | 事件名称. |
| args | * | 是 | 将传递给事件处理者的附加参数 。 |


**返回值:** boolean - 如果有监听器的话,就用`true`,否则用`false`.


> 源码：[src/events/EventEmitter.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/events/EventEmitter.js#L99)  
引入版本：3.0.0


---

### eventNames {#eventNames}

#### \<instance> eventNames() {#instance-eventnames}


**说明:**

返回一个列出发送器已注册的听器的事件的数组 。


**返回值:** Array.\<(string | symbol)> - 


> 源码：[src/events/EventEmitter.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/events/EventEmitter.js#L68)  
引入版本：3.0.0


---

### listenerCount {#listenerCount}

#### \<instance> listenerCount(event) {#instance-listenercountevent}


**说明:**

返回收听特定事件的监听器数量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | string \| symbol | 否 | 事件名称. |


**返回值:** number - 众听者数.


> 源码：[src/events/EventEmitter.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/events/EventEmitter.js#L88)  
引入版本：3.0.0


---

### listeners {#listeners}

#### \<instance> listeners(event) {#instance-listenersevent}


**说明:**

返回已注册的监听器 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | string \| symbol | 否 | 事件名称. |


**返回值:** Array.\<function()> - 注册监听器。


> 源码：[src/events/EventEmitter.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/events/EventEmitter.js#L77)  
引入版本：3.0.0


---

### off {#off}

#### \<instance> off(event, [fn], [context], [once]) {#instance-offevent-fn-context-once}


**说明:**

删除特定事件的监听器。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | string \| symbol | 否 | 事件名称. |
| fn | function | 是 | 只删除匹配此函数的监听器 。 |
| context | * | 是 | 只删除有此上下文的监听器. |
| once | boolean | 是 | 只删除一次性的监听器. |


**返回值:** [Phaser.Events.EventEmitter](/api/class/events-eventemitter) - `this`.


> 源码：[src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v4.1.0/src/events/EventEmitter.js#L165)  
引入版本：3.0.0


---

### on {#on}

#### \<instance> on(event, fn, [context]) {#instance-onevent-fn-context}


**说明:**

为指定事件添加一个监听器 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| event | string \| symbol | 否 |  | 事件名称. |
| fn | function | 否 |  | 听者功能. |
| context | * | 是 | "this" | 用来引用监听器的上下文 。 |


**返回值:** [Phaser.Events.EventEmitter](/api/class/events-eventemitter) - `this`.


> 源码：[src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/events/EventEmitter.js#L111)  
引入版本：3.0.0


---

### once {#once}

#### \<instance> once(event, fn, [context]) {#instance-onceevent-fn-context}


**说明:**

为指定事件添加一次性的听器。 第一次发布事件时, 监听器会自动删除, 因此它永远不会被调用一次以上 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| event | string \| symbol | 否 |  | 事件名称. |
| fn | function | 否 |  | 听者功能. |
| context | * | 是 | "this" | 用来引用监听器的上下文 。 |


**返回值:** [Phaser.Events.EventEmitter](/api/class/events-eventemitter) - `this`.


> 源码：[src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/events/EventEmitter.js#L137)  
引入版本：3.0.0


---

### removeAllListeners {#removeAllListeners}

#### \<instance> removeAllListeners([event]) {#instance-removealllistenersevent}


**说明:**

删除全部监听器, 或指定事件的监听器 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | string \| symbol | 是 | 事件名称. |


**返回值:** [Phaser.Events.EventEmitter](/api/class/events-eventemitter) - `this`.


> 源码：[src/events/EventEmitter.js#L179](https://github.com/phaserjs/phaser/blob/v4.1.0/src/events/EventEmitter.js#L179)  
引入版本：3.0.0


---

### removeListener {#removeListener}

#### \<instance> removeListener(event, [fn], [context], [once]) {#instance-removelistenerevent-fn-context-once}


**说明:**

删除特定事件的监听器。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | string \| symbol | 否 | 事件名称. |
| fn | function | 是 | 只删除匹配此函数的监听器 。 |
| context | * | 是 | 只删除有此上下文的监听器. |
| once | boolean | 是 | 只删除一次性的监听器. |


**返回值:** [Phaser.Events.EventEmitter](/api/class/events-eventemitter) - `this`.


> 源码：[src/events/EventEmitter.js#L151](https://github.com/phaserjs/phaser/blob/v4.1.0/src/events/EventEmitter.js#L151)  
引入版本：3.0.0


---

### shutdown {#shutdown}

#### \<instance> shutdown() {#instance-shutdown}


**说明:**

从 EventEmitter 中删除所有监听器。 当父 Scene 关闭时, 此方法会被 Scene 系统自动调用, 以确保清除所有事件绑定, 并且不再保留 stale 引用 。


> 源码：[src/events/EventEmitter.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/events/EventEmitter.js#L40)  
引入版本：3.0.0


---

---
