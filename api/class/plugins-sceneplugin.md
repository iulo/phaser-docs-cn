# ScenePlugin {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/plugins-sceneplugin)

场景关卡插件是一个插件,安装到每个场景中,属于该场景的一生。与整个游戏中一度存在的全局插件不同,场景插件会针对每个场景单独进行即时化,并在场景被破坏时被销毁。

当创建您自己的自定义插件时, 您将会扩展此类, 需要每个景态或需要响应像 Scene 生命周期事件 。 `start`, `pause`, `sleep`, `wake`, `shutdown`,和 `destroy`.

该插件可以将自身映射到景区(例如`this.myPlugin`)上的属性和/或进入景区系统,使其可以在景区内的任何地方访问. over the `boot`方法来设置事件听器,并初始化您插件所需的任何每景区资源.

**构造函数**

`new ScenePlugin(scene, pluginManager, pluginKey)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 引用已安装此插件的 Scene 。 |
| pluginManager | [Phaser.Plugins.PluginManager](/api/class/plugins-pluginmanager) | 否 | 插件管理器的引用 。 |
| pluginKey | string | 否 | 此插件安装到 Scene 系统的键 。 |

---


**作用域**: static


**继承**

> [Phaser.Plugins.BasePlugin](/api/class/plugins-baseplugin)  



> 源码：[src/plugins/ScenePlugin.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/ScenePlugin.js#L11)  
引入版本：3.8.0

## 继承的成员 {#inherited-members}


**From [Phaser.Plugins.BasePlugin](/api/class/plugins-baseplugin):**


 - [game](/api/class/plugins-baseplugin#game)
 - [pluginManager](/api/class/plugins-baseplugin#pluginManager)




---

## 公开成员 {#public-members}

### pluginKey {#pluginKey}

#### pluginKey: string {#pluginkey-string}


**说明:**

此插件安装到 Scene 系统的键 。

此属性仅在插件被即时化并添加到场景时设定, 而不是在之前。 您可以在 `boot` 方法中使用 。


> 源码：[src/plugins/ScenePlugin.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/ScenePlugin.js#L70)  
引入版本：3.54.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

用于安装此插件的 Scene 的引用。 只有设置为 Scene 插件, 否则为 `null` 。 此属性只有在插件被即时添加到 Scene 时才设定, 而不是在之前。 您可以在 `boot` 方法中使用 。


**访问权限:** 受保护


> 源码：[src/plugins/ScenePlugin.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/ScenePlugin.js#L44)  
引入版本：3.8.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

引用安装了此插件的 Scene 系统。 只有设置为 Scene 插件, 否则为 `null`。 此属性只有在插件被即时添加到 Scene 时才设置, 而不是在之前。 您可以在 `boot` 方法中使用 。


**访问权限:** 受保护


> 源码：[src/plugins/ScenePlugin.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/ScenePlugin.js#L57)  
引入版本：3.8.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Plugins.BasePlugin](/api/class/plugins-baseplugin):**


 - [init](/api/class/plugins-baseplugin#init)
 - [start](/api/class/plugins-baseplugin#start)
 - [stop](/api/class/plugins-baseplugin#stop)




---

## 公开方法 {#public-methods}

### boot {#boot}

#### \<instance> boot() {#instance-boot}


**说明:**

这种方法在场景靴子时被称为"场景靴",它只被称作过一次.

到此为止, 插件属性 `scene` 和 `systems` 已经设置 。

您可以在此收听 [Scene](/api/event/scenes-events) 并设置此插件运行所需的任何设置。 以下是您可以收听的场景事件 :

- start

- ready

- preupdate

- update

- postupdate

- resize

- pause

- resume

- sleep

- wake

- transitioninit

- transitionstart

- transitioncomplete

- transitionout

- shutdown

- destroy

至少你应该提供一个破坏处理器 当场景关闭,即:

```javascript
var eventEmitter = this.systems.events;
eventEmitter.once('destroy', this.sceneDestroy, this);
```


> 源码：[src/plugins/ScenePlugin.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/ScenePlugin.js#L86)  
引入版本：3.8.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此插件并发布其持有的所有引用, 包括 Scene, Scene Systems, 和插件管理器。 当 Scene 被销毁时, 此方法会自动调用 。

如果您要扩展此类, 您应该覆盖此方法, 清理您插件创建的任何资源, 然后通过 `super.destroy()` 或原型链调用 `BasePlugin.destroy` 。


**重写:** Phaser.Plugins.BasePlugin#销毁


> 源码：[src/plugins/ScenePlugin.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/ScenePlugin.js#L125)  
引入版本：3.8.0


---

---
