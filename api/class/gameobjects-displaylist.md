# DisplayList {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-displaylist)

显示列表是一个场景插件,它维护了每个帧所要渲染的游戏对象的顺序列表。游戏对象在渲染前会按深度自动排序。您通常不会直接与显示列表互动;而是在单个游戏对象上使用 `addToDisplayList`和 `removeFromDisplayList` 。

**构造函数**

`new DisplayList(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 显示列表所属的景况 。 |

---


**作用域**: static


**继承**

> Phaser.Structs.List.\<Phaser.GameObjects.GameObject>  



> 源码：[src/gameobjects/DisplayList.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/DisplayList.js#L14)  
引入版本：3.0.0

## 公开成员 {#public-members}

### events {#events}

#### events: [Phaser.Events.EventEmitter](/api/class/events-eventemitter) {#events-phasereventseventemitter}


**说明:**

场景事件艾密特.


> 源码：[src/gameobjects/DisplayList.js#L67](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/DisplayList.js#L67)  
引入版本：3.50.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

显示列表所属的景况 。


> 源码：[src/gameobjects/DisplayList.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/DisplayList.js#L49)  
引入版本：3.0.0


---

### sortChildrenFlag {#sortChildrenFlag}

#### sortChildrenFlag: boolean {#sortchildrenflag-boolean}


**说明:**

用于确定游戏对象是否在调用 `depthSort()` 时排序的旗帜 。


> 源码：[src/gameobjects/DisplayList.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/DisplayList.js#L39)  
引入版本：3.0.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

场景系统.


> 源码：[src/gameobjects/DisplayList.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/DisplayList.js#L58)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### depthSort {#depthSort}

#### \<instance> depthSort() {#instance-depthsort}


**说明:**

如果设置了旗, 立即排序显示列表 。


> 源码：[src/gameobjects/DisplayList.js#L179](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/DisplayList.js#L179)  
引入版本：3.0.0


---

### getChildren {#getChildren}

#### \<instance> getChildren() {#instance-getchildren}


**说明:**

返回包含显示列表中所有对象的数组。 这是主要列表数组的参考, 不是复制, 所以请小心不要修改 。


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 集团成员.


> 源码：[src/gameobjects/DisplayList.js#L211](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/DisplayList.js#L211)  
引入版本：3.12.0


---

### queueDepthSort {#queueDepthSort}

#### \<instance> queueDepthSort() {#instance-queuedepthsort}


**说明:**

强制在下次呼叫时显示列表的排序 depthSort.


> 源码：[src/gameobjects/DisplayList.js#L168](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/DisplayList.js#L168)  
引入版本：3.0.0


---

### sortByDepth {#sortByDepth}

#### \<instance> sortByDepth(childA, childB) {#instance-sortbydepthchilda-childb}


**说明:**

比较两个游戏对象的深度.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| childA | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 第一个游戏对象. |
| childB | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 第二游戏对象. |


**返回值:** number - 每个游戏对象深度的区别.


> 源码：[src/gameobjects/DisplayList.js#L195](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/DisplayList.js#L195)  
引入版本：3.0.0


---

---
