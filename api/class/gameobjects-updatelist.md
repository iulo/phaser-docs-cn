# UpdateList {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-updatelist)

更新列表是一个场景插件,它维护着每个帧应该称为`preUpdate`的游戏对象列表。像Sprites这样的游戏对象会自动加入更新列表,从而处理他们的动画。您通常不会直接与更新列表互动;而是在单个游戏对象上使用Z`addToUpdateList`和`removeFromUpdateList`。

**构造函数**

`new UpdateList(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 说明更新列表属于哪个类别 。 |

---


**作用域**: static


**继承**

> Phaser.Structs.ProcessQueue.\<Phaser.GameObjects.GameObject>  



> 源码：[src/gameobjects/UpdateList.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/UpdateList.js#L12)  
引入版本：3.0.0

## 公开成员 {#public-members}

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

说明更新列表属于哪个类别 。


> 源码：[src/gameobjects/UpdateList.js#L41](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/UpdateList.js#L41)  
引入版本：3.0.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

场景系统.


> 源码：[src/gameobjects/UpdateList.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/UpdateList.js#L50)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

拥有此插件的场景正在被销毁 。

我们需要关闭 然后清除所有外部引用。


> 源码：[src/gameobjects/UpdateList.js#L207](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/UpdateList.js#L207)  
引入版本：3.0.0


---

### sceneUpdate {#sceneUpdate}

#### \<instance> sceneUpdate(time, delta) {#instance-sceneupdatetime-delta}


**说明:**

更新步骤。

预更新列表中每个活动游戏对象.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 现时时标. |
| delta | number | 否 | 三角洲时间已经过去 自上个框架。 |


> 源码：[src/gameobjects/UpdateList.js#L134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/UpdateList.js#L134)  
引入版本：3.20.0


---

### shutdown {#shutdown}

#### \<instance> shutdown() {#instance-shutdown}


**说明:**

拥有此插件的场景正在关闭 。

我们需要销毁所有活动,待决,并排队的游戏对象,重置所有内部属性,停止听场景事件.


> 源码：[src/gameobjects/UpdateList.js#L161](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/UpdateList.js#L161)  
引入版本：3.0.0


---

---
