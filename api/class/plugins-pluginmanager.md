# PluginManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/plugins-pluginmanager)

插件管理器负责安装和添加插件到Phaser.

这是一种全球系统,因此属于Game excent,而不是特定的场景.

它与插件缓存一起工作。核心内部插件自动与缓存注册,但负责向外加插件管理器注入它们。

插件有两种类型:

1. 全局插件

2. 场景插件

一个全局插件是一个插件,它生活在插件管理器内部,而不是场景。您可以通过拨打 `PluginManager.get` 并提供一个密钥来访问它。任何以这种方式请求插件的场景都会获得同一插件实例,允许您使用一个跨越多个场景的单一插件 。

场景插件是一个用于在场景内运行的插件。 这些插件不同于全局插件, 因为它们的插件不生活在插件管理器内部, 而是在场景系统类内。 此外, 每个创建的场景都得到了它自己独特的场景插件。 核心场景插件的例子包括输入插件、 Tween 插件和物理插件 。

您可以以三种不同的方式在 Phaser 中添加插件 :

1. 预装

2. 将其包含在您的源代码中,并通过 Game Cfig 安装

3. 将其包含在您的源代码中, 并安装在场景中

所有这些方法的例子请见Phaser 3实例Repo `plugins`文件夹。

关于创建自己的插件,请参见Phaser 3插件模板。

**构造函数**

`new PluginManager(game)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 拥有此插件管理器的游戏实例 。 |

---


**作用域**: static

> 源码：[src/plugins/PluginManager.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L18)  
引入版本：3.0.0

## 公开成员 {#public-members}

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

拥有此插件管理器的游戏实例 。


> 源码：[src/plugins/PluginManager.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L69)  
引入版本：3.0.0


---

### plugins {#plugins}

#### plugins: Array.\<[Phaser.Types.Plugins.GlobalPlugin](/api/typedef/types-plugins#globalplugin)> {#plugins-arrayphasertypespluginsglobalplugin}


**说明:**

当前由此插件管理器运行和管理的全局插件。 插件必须至少启动一次才能在此列表中出现 。


> 源码：[src/plugins/PluginManager.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L78)  
引入版本：3.8.0


---

### scenePlugins {#scenePlugins}

#### scenePlugins: Array.\<string> {#sceneplugins-arraystring}


**说明:**

列表中包含应该安装到Scenes以及核心插件的插件密钥 。


> 源码：[src/plugins/PluginManager.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L88)  
引入版本：3.8.0


---

## 公开方法 {#public-methods}

### addToScene {#addToScene}

#### \<instance> addToScene(sys, globalPlugins, scenePlugins) {#instance-addtoscenesys-globalplugins-sceneplugins}


**说明:**

由 Scene 系统类调用 。 告诉插件管理器将全部 Scene 插件安装到它 。

首先,它会安装全局引用, 即从游戏系统引用到景区系统( 如果映射的话) 。 然后, 它会安装核心景区插件, 之后是插件管理器注册的景区插件。 最后, 它会安装任何对全局插件的引用, 其属性是景区本身的映射 。


**Access:** 保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sys | [Phaser.Scenes.Systems](/api/class/scenes-systems) | 否 | 场景系统类,用于安装全部插件到 。 |
| globalPlugins | array | 否 | 要安装的全局插件阵列 。 |
| scenePlugins | array | 否 | 要安装的场景插件阵列 。 |


> 源码：[src/plugins/PluginManager.js#L212](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L212)  
引入版本：3.8.0


---

### boot {#boot}

#### \<instance> boot() {#instance-boot}


**说明:**

一旦游戏启动并安装了游戏配置中配置的所有插件,就运行.


**Access:** 保护


> 源码：[src/plugins/PluginManager.js#L127](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L127)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此插件管理器和所有关联插件。 它会将找到的所有插件进行结构化, 并调用它们的 `destroy` 方法 。

插件缓存将删除所有自定义插件 。


> 源码：[src/plugins/PluginManager.js#L866](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L866)  
引入版本：3.8.0


---

### get {#get}

#### \<instance> get(key, [autoStart]) {#instance-getkey-autostart}


**说明:**

从插件管理器中根据给定的密钥获取全局插件并返回它。

如果它无法找到基于密钥的活跃插件, 但是插件缓存中有一个带有相同的密钥, 那么它将会创建缓存插件的新实例, 并返回该实例 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 要获取的插件的密钥 。 |
| autoStart | boolean | 是 | true | 如果在缓存中找到, 则自动启动新插件实例, 但不会积极运行 。 |


**返回值:** [Phaser.Plugins.BasePlugin](/api/class/plugins-baseplugin), function - 插件,或者如果找不到匹配密钥的插件,则使用 `null` 。


> 源码：[src/plugins/PluginManager.js#L644](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L644)  
引入版本：3.8.0


---

### getClass {#getClass}

#### \<instance> getClass(key) {#instance-getclasskey}


**说明:**

从缓存返回插件类。 插件管理器内部使用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要获取的插件的密钥 。 |


**返回值:** [Phaser.Plugins.BasePlugin](/api/class/plugins-baseplugin) - 插件对象


> 源码：[src/plugins/PluginManager.js#L687](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L687)  
引入版本：3.8.0


---

### getDefaultScenePlugins {#getDefaultScenePlugins}

#### \<instance> getDefaultScenePlugins() {#instance-getdefaultsceneplugins}


**说明:**

由 Scene 系统类调用。 返回要安装的插件列表 。


**Access:** 保护


**返回值:** Array.\<string> - 所有要安装的场景插件的密钥列表 。


> 源码：[src/plugins/PluginManager.js#L311](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L311)  
引入版本：3.8.0


---

### getEntry {#getEntry}

#### \<instance> getEntry(key) {#instance-getentrykey}


**说明:**

获得基于给定密钥的全球插件。


**Access:** 保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 唯一插件密钥 。 |


**返回值:** [Phaser.Types.Plugins.GlobalPlugin](/api/typedef/types-plugins#globalplugin) - 插件条目 。


> 源码：[src/plugins/PluginManager.js#L501](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L501)  
引入版本：3.8.0


---

### getIndex {#getIndex}

#### \<instance> getIndex(key) {#instance-getindexkey}


**说明:**

获取基于给定密钥的全局插件索引。


**Access:** 保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 唯一插件密钥 。 |


**返回值:** number - 插件阵列中的插件索引 。


> 源码：[src/plugins/PluginManager.js#L473](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L473)  
引入版本：3.8.0


---

### install {#install}

#### \<instance> install(key, plugin, [start], [mapping], [data]) {#instance-installkey-plugin-start-mapping-data}


**说明:**

在插件管理器中安装新的全局插件并选择启动它运行。一个全局插件管理器属于插件管理器,而不是特定的场景,可以被游戏中的所有幕后角色访问和使用。

`key` 属性是您从插件管理器访问此插件时使用的内容 。

```javascript
this.plugins.install('powerupsPlugin', pluginCode);

// and from within the scene:
this.plugins.get('powerupsPlugin');
```

如果您使用游戏配置对象安装插件,或通过装入器预先装入插件,则此方法会自动被 Phaser 调用 。

同一插件可以简单地给每个实例自己独特的密钥,从而多次安装到插件管理器中.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 插件管理器内给此插件的独有的手柄 。 |
| plugin | function | 否 |  | 插件代码。 这应该是非辅助版本 。 |
| start | boolean | 是 | false | 自动启动运行的插件吗? 如果您提供了映射值, 则总是 `true` 。 |
| mapping | string | 是 |  | 如果此插件被注入 Phaser.Scene 类, 这是要使用的属性密钥 。 |
| data | any | 是 |  | 一个值传递到插件的 `init` 方法. |


**返回值:** [Phaser.Plugins.BasePlugin](/api/class/plugins-baseplugin) - 启动的插件, 或 `null` 如果 `start` 是虚假的, 或者游戏尚未启动 。


> 源码：[src/plugins/PluginManager.js#L401](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L401)  
引入版本：3.8.0


---

### installScenePlugin {#installScenePlugin}

#### \<instance> installScenePlugin(key, plugin, [mapping], [addToScene], [fromLoader]) {#instance-installscenepluginkey-plugin-mapping-addtoscene-fromloader}


**说明:**

在插件管理器中安装一个新的场景插件, 并选择将其添加到给定场景中。 这样添加到管理器中的场景插件将自动安装到所有新的场景中, 使用给定的密钥和映射 。

`key`属性是插件被注入到 Scene.Systems 的属性。 `mapping`属性是可选的,如果指定是插件被安装到 Scene 的属性。 例如:

```javascript
this.plugins.installScenePlugin('powerupsPlugin', pluginCode, 'powerups');

// and from within the scene:
this.sys.powerupsPlugin; // key value
this.powerups; // mapping value
```

如果您使用游戏配置对象安装插件,或通过装入器预先装入插件,则此方法会自动被 Phaser 调用 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 用于将此插件添加到 Scene. Systems 的属性密钥 。 |
| plugin | function | 否 |  | 插件代码。 这应该是非辅助版本 。 |
| mapping | string | 是 |  | 如果此插件被注入 Phaser.Scene 类, 这是要使用的属性密钥 。 |
| addToScene | [Phaser.Scene](/api/class/scene) | 是 |  | 可选地将这个插件自动添加到给定的场景中 。 |
| fromLoader | boolean | 是 | false | 这是装货机叫的吗? |


> 源码：[src/plugins/PluginManager.js#L330](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L330)  
引入版本：3.8.0


---

### isActive {#isActive}

#### \<instance> isActive(key) {#instance-isactivekey}


**说明:**

检查指定的全局插件是否基于其密钥活动 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 唯一插件密钥 。 |


**返回值:** boolean - 如果插件是活动时的`true`,否则就是`false`.


> 源码：[src/plugins/PluginManager.js#L522](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L522)  
引入版本：3.8.0


---

### registerFileType {#registerFileType}

#### \<instance> registerFileType(key, callback, [addToScene]) {#instance-registerfiletypekey-callback-addtoscene}


**说明:**

注册全局文件类型管理器的新文件类型, 并提供给在此之后创建的所有加载器插件 。

通常从您的插件代码中调用, 并且是一个有用的快捷键, 用于创建新的加载器文件类型 。

密钥是将注入装入器插件并用于装入文件的属性。 例如 :

```javascript
this.plugins.registerFileType('wad', doomWadLoaderCallback);
// later in your preload code:
this.load.wad();
```

调用是装入器试图装入匹配给定密钥的文件时的调用。 必须理解调用是在装入器普卢金语的语境中引用的。 在此语境中, 有若干属性/ 方法可用 :

this.addFile - 将新文件添加到负载队列的方法. this.scene - 拥有加载器插件实例的场景 。

详情请见LaderPlugin类。 列出的任何公共属性或方法均可从您在 `this` 下的回调中获取。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 与加载器插件注册的文件类型的密钥,即`wad`,`atlas`. |
| callback | function | 否 | 当装入器插件试图装入此类型的文件时, 调用回调 。 |
| addToScene | [Phaser.Scene](/api/class/scene) | 是 | 可选地将这个文件类型添加到给定场景所拥有的加载器插件中. |


> 源码：[src/plugins/PluginManager.js#L822](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L822)  
引入版本：3.8.0


---

### registerGameObject {#registerGameObject}

#### \<instance> registerGameObject(key, [factoryCallback], [creatorCallback]) {#instance-registergameobjectkey-factorycallback-creatorcallback}


**说明:**

将游戏对象的新型与全球游戏对象工厂和/或创建者注册。通常从您的插件代码中调用,并且是创建新的游戏对象的有用短剪。

键是将注入工厂并用于创建游戏对象的属性。 例如:

```javascript
this.plugins.registerGameObject('clown', clownFactoryCallback, clownCreatorCallback);
// later in your game code:
this.add.clown();
this.make.clown();
```

调用是工厂试图创建匹配给定密钥的游戏对象时所使用的名称。 需要了解调用在 Game ObjectFactory 的背景中。 在此背景中, 有若干属性可以使用 :

this.scene - 属于游戏对象Factory的景点参考. this.displayList - 属于景点的显示列表参考. this.updateList - 属于该景点的更新列表参考.

详情请参见 GameObjectFactory 和 GameObjectCreator 类。 列出的任何公共属性或方法,均可在 `this` 下从您的回调中获取 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 给定的回调对象将创建的游戏对象的密钥,即`image`,`sprite`. |
| factoryCallback | function | 是 | 游戏对象工厂被调用时的调用引用. |
| creatorCallback | function | 是 | 当游戏对象创建者被调用时, 需要引用的调用 。 |


> 源码：[src/plugins/PluginManager.js#L744](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L744)  
引入版本：3.8.0


---

### removeGameObject {#removeGameObject}

#### \<instance> removeGameObject(key, [removeFromFactory], [removeFromCreator]) {#instance-removegameobjectkey-removefromfactory-removefromcreator}


**说明:**

从全球游戏对象工厂和/或创建者中删除先前注册的游戏对象。通常从您的插件销毁代码中调用此功能,以帮助在插件被移除后进行清理。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 工厂要删除的游戏对象的密钥. |
| removeFromFactory | boolean | 是 | true | 游戏对象是否应该从游戏对象工厂中移除? |
| removeFromCreator | boolean | 是 | true | 游戏对象是否应该从游戏对象创建者中移除? |


> 源码：[src/plugins/PluginManager.js#L793](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L793)  
引入版本：3.19.0


---

### removeGlobalPlugin {#removeGlobalPlugin}

#### \<instance> removeGlobalPlugin(key) {#instance-removeglobalpluginkey}


**说明:**

从插件管理器和插件缓存中删除全局插件。

您可以删除所有您可能持有的游戏代码中对该插件的引用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要删除的插件的密钥 。 |


> 源码：[src/plugins/PluginManager.js#L703](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L703)  
引入版本：3.8.0


---

### removeScenePlugin {#removeScenePlugin}

#### \<instance> removeScenePlugin(key) {#instance-removescenepluginkey}


**说明:**

从插件管理器和插件缓存中删除一个场景插件。

这将不会从任何已使用过的当前屏幕中删除插件 。

您可以删除所有您可能持有的游戏代码中对该插件的引用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要删除的插件的密钥 。 |


> 源码：[src/plugins/PluginManager.js#L725](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L725)  
引入版本：3.8.0


---

### start {#start}

#### \<instance> start(key, [runAs]) {#instance-startkey-runas}


**说明:**

启动全局插件运行 。

如果插件之前是激活的,那么调用`start`会将其重置到活动状态,然后调用它的`start`方法.

如果插件在插件管理器内部创建新实例之前从未运行过,则其活动状态设置,然后其`init`和`start`方法都按此顺序调用.

如果插件已经在给定的密钥下运行, 那么就不会发生什么 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要启动的插件的密钥 。 |
| runAs | string | 是 | 在新密钥下运行插件。 这使得您可以多次运行一个插件 。 |


**返回值:** [Phaser.Plugins.BasePlugin](/api/class/plugins-baseplugin) - 已启动的插件, 或 `null` 如果给定无效的密钥或插件已被停止 。


> 源码：[src/plugins/PluginManager.js#L539](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L539)  
引入版本：3.8.0


---

### stop {#stop}

#### \<instance> stop(key) {#instance-stopkey}


**说明:**

停止全局插件运行 。

如果插件是活动,则其活动状态将被设定为虚假,并调用插件 `stop`方法.

如果插件尚未运行, 则不会发生任何事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 插件的键要停止 。 |


**返回值:** [Phaser.Plugins.PluginManager](/api/class/plugins-pluginmanager) - 插件管理员 。


> 源码：[src/plugins/PluginManager.js#L616](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginManager.js#L616)  
引入版本：3.8.0


---

---
