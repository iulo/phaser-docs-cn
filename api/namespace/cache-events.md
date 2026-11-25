# Phaser.Cache.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/cache-events)

Scope: 
static
> 源码：[src/cache/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/events/index.js#L7)  


## 静态函数 {#static-functions}

### ADD {#ADD}

#### ADD {#add}


**说明:**

快取添加事件 。

此事件由每次添加新对象时扩展 BaseCache 的缓存发送 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| cache | [Phaser.Cache.BaseCache](/api/class/cache-basecache) | 否 | 对象被添加的缓存 。 |
| key | string | 否 | 对象的密钥添加到缓存中 。 |
| object | * | 否 | 缓存中添加的对象的引用 。 |


> 源码：[src/cache/events/ADD_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/events/ADD_EVENT.js#L7)  
引入版本：3.0.0


---

### REMOVE {#REMOVE}

#### REMOVE {#remove}


**说明:**

快取事件 。

每当对象被删除时, 此事件都会由扩展 BaseCache 的缓存发送 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| cache | [Phaser.Cache.BaseCache](/api/class/cache-basecache) | 否 | 对象被删除的缓存 。 |
| key | string | 否 | 从缓存中移除对象的密钥 。 |
| object | * | 否 | 缓存中移除的对象的引用 。 |


> 源码：[src/cache/events/REMOVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/events/REMOVE_EVENT.js#L7)  
引入版本：3.0.0


---

---
