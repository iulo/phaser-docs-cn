# Phaser.Plugins.DefaultPlugins {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/plugins-defaultplugins)

Scope: 
static
> 源码：[src/plugins/DefaultPlugins.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/DefaultPlugins.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### CoreScene {#CoreScene}

#### CoreScene: array {#corescene-array}


**说明:**

这些核心插件被安装到每个 Scene.Systems 实例中, 不管怎样, 它们也可以在 Scene 中选择曝光( 详情请参见 InjectionMap) 。

它们按照它们在这个数组中出现的顺序创建,事件Emitter总是最先出现的.


> 源码：[src/plugins/DefaultPlugins.js#L53](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/DefaultPlugins.js#L53)  
引入版本：3.0.0


---

### DefaultScene {#DefaultScene}

#### DefaultScene: array {#defaultscene-array}


**说明:**

这些插件除了CoreScenePlugins之外,还在Scene.Systems中创建.

您可以选择不拥有这些插件, 要么创建默认 Plugins 对象作为游戏配置的一部分, 要么创建插件对象作为Scene Config的一部分, 要么修改此数组并构建自己的捆绑 。

在场景中也可以选择暴露(详情见注射地图)

它们总是按照它们在阵列中出现时的顺序来创建.


> 源码：[src/plugins/DefaultPlugins.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/DefaultPlugins.js#L76)  
引入版本：3.0.0


---

### Global {#Global}

#### Global: array {#global-array}


**说明:**

这些是 Phaser.Game 实例创建的全局管理器。 它们来自 Scene. Systems , 以便插件使用 。


> 源码：[src/plugins/DefaultPlugins.js#L31](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/DefaultPlugins.js#L31)  
引入版本：3.0.0


---

---
