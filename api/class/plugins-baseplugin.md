# BasePlugin {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/plugins-baseplugin)

仅安装一次全球插件到游戏所有插件管理器中。 它可以监听游戏事件并响应它们 。

自定义全局插件应扩展此类, 并采用任何必要的生命周期方法 : `init` (称为插件最初创建时), `start` (称为插件启动时), `stop` (称为插件停止时),和 `destroy` (称为游戏关闭时).

**构造函数**

`new BasePlugin(pluginManager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pluginManager | [Phaser.Plugins.PluginManager](/api/class/plugins-pluginmanager) | 否 | 插件管理器的引用 。 |

---


**作用域**: static

> 源码：[src/plugins/BasePlugin.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/BasePlugin.js#L9)  
引入版本：3.8.0

## 公开成员 {#public-members}

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

引用此插件运行在 Game 实例 。


**访问权限:** 受保护


> 源码：[src/plugins/BasePlugin.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/BasePlugin.js#L43)  
引入版本：3.8.0


---

### pluginManager {#pluginManager}

#### pluginManager: [Phaser.Plugins.PluginManager](/api/class/plugins-pluginmanager) {#pluginmanager-phaserpluginspluginmanager}


**说明:**

方便的引用用于此插件的插件管理器。 可用于获取游戏系统和事件。 Name


**访问权限:** 受保护


> 源码：[src/plugins/BasePlugin.js#L32](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/BasePlugin.js#L32)  
引入版本：3.8.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

当此插件被销毁时, 由插件管理器调用。 无论是游戏关闭还是插件管理器中明确删除插件, 都会取消游戏、 场景和插件管理器的内部引用, 以防止内存泄露。 覆盖此方法, 以释放它持有的任何资源 。


> 源码：[src/plugins/BasePlugin.js#L112](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/BasePlugin.js#L112)  
引入版本：3.8.0


---

### init {#init}

#### \<instance> init([data]) {#instance-initdata}


**说明:**

插件管理器在插件首次即时化时将这种方法调用到全局插件上。 将不再调用此插件。 您可以在此设置此插件运行所需的任何设备。 如果插件被设置为自动启动, 那么此插件之后将立即调用 `BasePlugin.start` 。 在 Scene 插件上, 此方法将永远不用调用 。 使用 [Phaser.Plugins.ScenePlugin#boot](/api/class/plugins-sceneplugin#boot) 代替 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | any | 是 | 用户从插件配置对象的`data`属性(如果始于游戏启动)或插件管理器的`install`方法(如果手工启动)中传递的值(如果有的话)指定. |


> 源码：[src/plugins/BasePlugin.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/BasePlugin.js#L54)  
引入版本：3.8.0


---

### start {#start}

#### \<instance> start() {#instance-start}


**说明:**

插件管理器在插件启动时将这种方法调用全局插件。 如果插件停止, 然后重新开始, 则它会被调用。 通常在 `BasePlugin.init` 之后立即调用。 在 Scene 插件上, 这种方法永远不会调用 。


> 源码：[src/plugins/BasePlugin.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/BasePlugin.js#L70)  
引入版本：3.8.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

插件管理器在插件停止时将这种方法调用到全局插件上。 游戏代码要求您的插件停止做它所做的任何事情。 现在它被插件管理器视为“ 不活动 ” 。 在此处理此进程( 即停止对事件的倾听等等 ) 如果插件再次启动, 那么 `BasePlugin.start`z 将再次调用。 在 Scene 插件上, 这种方法永远不会调用 。


> 源码：[src/plugins/BasePlugin.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/BasePlugin.js#L97)  
引入版本：3.8.0


---

---
