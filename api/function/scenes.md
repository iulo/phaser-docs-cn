# Phaser.Scenes {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/function/scenes)

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


# Phaser.Scenes.Settings {#page-title-1}

### create {#create}

#### \<static> create(config) {#static-createconfig}


**说明:**

使用场景配置对象并返回一个完全形成的系统设置对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | string \| [Phaser.Types.Scenes.SettingsConfig](/api/typedef/types-scenes#settingsconfig) | 否 | 用于创建此场景设置的场景配置对象 。 |


**返回值:** [Phaser.Types.Scenes.SettingsObject](/api/typedef/types-scenes#settingsobject) - 由配置和默认设置所创建的场景设置对象.


> 源码：[src/scene/Settings.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Settings.js#L18)  
引入版本：3.0.0

---
