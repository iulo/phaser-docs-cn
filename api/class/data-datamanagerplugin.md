# DataManagerPlugin {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/data-datamanagerplugin)

数据管理器插件是一个场景插件,它为场景提供数据存储和检索功能,与场景生命周期结合。它扩展了基础数据管理器类,为场景关闭和破坏事件自动处理,确保存储的数据和事件听器在场景停止或被破坏时被妥善清理。它通过`scene.data`在任何场景中访问。

**构造函数**

`new DataManagerPlugin(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 引用此 DataManager 属于的场景 。 |

---


**作用域**: static


**继承**

> [Phaser.Data.DataManager](/api/class/data-datamanager)  



> 源码：[src/data/DataManagerPlugin.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManagerPlugin.js#L12)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Data.DataManager](/api/class/data-datamanager):**


 - [count](/api/class/data-datamanager#count)
 - [events](/api/class/data-datamanager#events)
 - [freeze](/api/class/data-datamanager#freeze)
 - [list](/api/class/data-datamanager#list)
 - [parent](/api/class/data-datamanager#parent)
 - [values](/api/class/data-datamanager#values)




---

## 公开成员 {#public-members}

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

引用此 DataManager 属于的场景 。


> 源码：[src/data/DataManagerPlugin.js#L38](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManagerPlugin.js#L38)  
引入版本：3.0.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

参考史诗的系统.


> 源码：[src/data/DataManagerPlugin.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManagerPlugin.js#L47)  
引入版本：3.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Data.DataManager](/api/class/data-datamanager):**


 - [each](/api/class/data-datamanager#each)
 - [get](/api/class/data-datamanager#get)
 - [getAll](/api/class/data-datamanager#getAll)
 - [has](/api/class/data-datamanager#has)
 - [inc](/api/class/data-datamanager#inc)
 - [merge](/api/class/data-datamanager#merge)
 - [pop](/api/class/data-datamanager#pop)
 - [query](/api/class/data-datamanager#query)
 - [remove](/api/class/data-datamanager#remove)
 - [reset](/api/class/data-datamanager#reset)
 - [set](/api/class/data-datamanager#set)
 - [setFreeze](/api/class/data-datamanager#setFreeze)
 - [toggle](/api/class/data-datamanager#toggle)




---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此数据管理器 Plugin, 调用数据库 DataManager 销毁方法, 删除全部 Scene 事件监听器, 并清除所有内部引用。 当自有 Scene 被销毁时, 将自动调用 。


**重写:** Phaser.Data.DataManager#销毁


> 源码：[src/data/DataManagerPlugin.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/data/DataManagerPlugin.js#L102)  
引入版本：3.5.0


---

---
