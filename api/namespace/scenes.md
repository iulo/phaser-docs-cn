# Phaser.Scenes {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/scenes)

Scope: 
static
> 源码：[src/scene/index.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/index.js#L10)  


## 静态函数 {#static-functions}

- [SceneManager](/api/class/scenes-scenemanager)
- [ScenePlugin](/api/class/scenes-sceneplugin)
- [Systems](/api/class/scenes-systems)
## 静态函数 {#static-functions-1}

### CREATING {#CREATING}

#### CREATING: number {#creating-number}


**说明:**

场景正在执行它的创建方法.


> 源码：[src/scene/const.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/const.js#L55)  
引入版本：3.0.0


---

### DESTROYED {#DESTROYED}

#### DESTROYED: number {#destroyed-number}


**说明:**

场景已被完全销毁,无法再启动或使用.


> 源码：[src/scene/const.js#L105](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/const.js#L105)  
引入版本：3.0.0


---

### INIT {#INIT}

#### INIT: number {#init-number}


**说明:**

场景目前由场景管理器初始化, 正在调用 init 方法 。


> 源码：[src/scene/const.js#L25](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/const.js#L25)  
引入版本：3.0.0


---

### LOADING {#LOADING}

#### LOADING: number {#loading-number}


**说明:**

场景正在通过它的加载器插件装入资源。 装入完成后, 创建方法将被调用 。


> 源码：[src/scene/const.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/const.js#L45)  
引入版本：3.0.0


---

### PAUSED {#PAUSED}

#### PAUSED: number {#paused-number}


**说明:**

场景已通过场景管理器或场景插件暂停。 更新方法没有被调用, 但场景仍在渲染 。


> 源码：[src/scene/const.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/const.js#L75)  
引入版本：3.0.0


---

### PENDING {#PENDING}

#### PENDING: number {#pending-number}


**说明:**

场景已经添加到场景管理器中,但尚未启动或初始化.


> 源码：[src/scene/const.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/const.js#L15)  
引入版本：3.0.0


---

### RUNNING {#RUNNING}

#### RUNNING: number {#running-number}


**说明:**

场景已完全运行。 更新和渲染方法都被称为每个帧 。


> 源码：[src/scene/const.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/const.js#L65)  
引入版本：3.0.0


---

### SHUTDOWN {#SHUTDOWN}

#### SHUTDOWN: number {#shutdown-number}


**说明:**

场景正在关闭。 所有属于它的游戏对象和插件正在被销毁 。


> 源码：[src/scene/const.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/const.js#L95)  
引入版本：3.0.0


---

### SLEEPING {#SLEEPING}

#### SLEEPING: number {#sleeping-number}


**说明:**

场景已经被安眠,更新和渲染方法都没有被调用,但场景并没有关闭.


> 源码：[src/scene/const.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/const.js#L85)  
引入版本：3.0.0


---

### START {#START}

#### START: number {#start-number}


**说明:**

场景正在启动。 创建方法尚未调用 。


> 源码：[src/scene/const.js#L35](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/const.js#L35)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-2}

- [Events](/api/namespace/scenes-events)
- [Settings](/api/namespace/scenes-settings)
## 静态函数 {#static-functions-3}

### GetPhysicsPlugins {#GetPhysicsPlugins}

#### \<static> GetPhysicsPlugins(sys) {#static-getphysicspluginssys}


**说明:**

构建一个阵列,为给定场景激活物理插件。

它检查游戏配置中定义的全球默认物理系统以及任何场景特定的物理设置。每个独特的物理插件键都以标题附加字符串的形式格式化,并附有“物理”附件(例如“arcade”变为“ArcadePhysics ” )。如果找不到默认系统或场景级别的物理设置,则返回 `undefined` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sys | [Phaser.Scenes.Systems](/api/class/scenes-systems) | 否 | 用于解决活动物理插件的场景系统。 |


**返回值:** array - 此场景要启动的物理插件键阵, 如果没有配置的话, 则启动 `undefined` 。


> 源码：[src/scene/GetPhysicsPlugins.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/GetPhysicsPlugins.js#L10)  
引入版本：3.0.0


---

### GetScenePlugins {#GetScenePlugins}

#### \<static> GetScenePlugins(sys) {#static-getscenepluginssys}


**说明:**

构建一个阵列,为给定的场景激活其中的插件(不包括物理插件).

此函数首先检查 S`plugins` 阵列的自身设置。 如果定义了, 则优先处理并立即返回。 否则, 将返回在插件管理器注册的全局默认 Scene 插件。 如果两者都不可用, 则返回空阵列 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sys | [Phaser.Scenes.Systems](/api/class/scenes-systems) | 否 | 用于检查插件的场景系统对象 。 |


**返回值:** array - 用于 Scene 的插件键。 Scene 级别插件优先于全局默认。 如果没有配置插件, 返回空的数组 。


> 源码：[src/scene/GetScenePlugins.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/GetScenePlugins.js#L9)  
引入版本：3.0.0


---

---
