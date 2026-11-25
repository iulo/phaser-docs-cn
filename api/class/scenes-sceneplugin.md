# ScenePlugin {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/scenes-sceneplugin)

场景插件是场景管理器的主要接口, 允许您控制游戏中运行的任何场景。 您应该总是使用此插件。 默认情况下, 它会被映射到场景属性 `this.scene`。 意思是, 从场景内部, 您可以调用 `this.scene.start()` 等方法 。

注意, 本类中几乎所有的方法都运行在一个队列- 基准上, 而不是立即运行。 例如, 调用 `this.scene.launch('SceneB')` 将会尝试在游戏步骤开始的场景管理器下一次更新时启动 SceneB 。 所有操作都会排队运行, 顺序是在此引用 。

**构造函数**

`new ScenePlugin(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 这场场景是这个场景普鲁金的 |

---


**作用域**: static

> 源码：[src/scene/ScenePlugin.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L13)  
引入版本：3.0.0

## 公开成员 {#public-members}

### key {#key}

#### key: string {#key-string}


**说明:**

此 ScenePlugin 属于的场景的密钥 。


> 源码：[src/scene/ScenePlugin.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L65)  
引入版本：3.0.0


---

### manager {#manager}

#### manager: [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) {#manager-phaserscenesscenemanager}


**说明:**

游戏的场景管理者.


> 源码：[src/scene/ScenePlugin.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L74)  
引入版本：3.0.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

这场场景是这个场景普鲁金的


> 源码：[src/scene/ScenePlugin.js#L38](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L38)  
引入版本：3.0.0


---

### settings {#settings}

#### settings: [Phaser.Types.Scenes.SettingsObject](/api/typedef/types-scenes#settingsobject) {#settings-phasertypesscenessettingsobject}


**说明:**

此 ScenePlugin 属于的场景的设置 。


> 源码：[src/scene/ScenePlugin.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L56)  
引入版本：3.0.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

这个ScenePlugin属于的Scene Systems exceptions except exception of the Scene Plugin 属于这个ScenePlugin. 黑盒的ScenePlugin是这个ScenePlugin的子公司,是这个ScenePlugin的子公司,是这个ScenePlugin的子公司,是这个子公司的一个子公司.


> 源码：[src/scene/ScenePlugin.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L47)  
引入版本：3.0.0


---

### transitionProgress {#transitionProgress}

#### transitionProgress: number {#transitionprogress-number}


**说明:**

如果此场景目前正在向另一个场景过渡,则当前过渡进度的百分比在0到1之间。


> 源码：[src/scene/ScenePlugin.js#L83](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L83)  
引入版本：3.5.0


---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(key, sceneConfig, [autoStart], [data]) {#instance-addkey-sceneconfig-autostart-data}


**说明:**

如果“ autoStart” 是真的, 或者设定了“ 活动” 属性, 将 Scene 添加到 Scene 管理器中并启动 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 一个独特的键用于引用景色,即`MainMenu`或`Level1`. |
| sceneConfig | [Phaser.Types.Scenes.SceneType](/api/typedef/types-scenes#scenetype) | 否 |  | 场景的配置 |
| autoStart | boolean | 是 | false | 如果 `true` , 场景会在添加后立即开始 。 |
| data | object | 是 |  | 可选数据对象。 这将设定为 `Scene.settings.data` 并传递到 `Scene.init` 和 `Scene.create` 。 |


**返回值:** [Phaser.Scene](/api/class/scene) - 增加的场景,如果立即加,否则会`null`.


> 源码：[src/scene/ScenePlugin.js#L447](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L447)  
引入版本：3.0.0


---

### bringToTop {#bringToTop}

#### \<instance> bringToTop([key]) {#instance-bringtotopkey}


**说明:**

将场景列入"幕后人物"名单中.

也就是说它会让其他的幕后人物 都更受欢迎

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 斯人之所动. |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L969](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L969)  
引入版本：3.0.0


---

### get {#get}

#### \<instance> get(key) {#instance-getkey}


**说明:**

基于给定的密钥获取一个场景 。

如果将实际的场景传递到这种方法,可以用来检查其目前是否在场景管理器内,或者没有.

**Tags:**

 - generic
 - genericUse
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 场景要取回。 |


**返回值:** [Phaser.Scene](/api/class/scene) - 景之所见.


> 源码：[src/scene/ScenePlugin.js#L1017](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L1017)  
引入版本：3.0.0


---

### getIndex {#getIndex}

#### \<instance> getIndex([key]) {#instance-getindexkey}


**说明:**

获取 Scene 列表中的 Scene 的数值索引 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 场景来获得索引。 |


**返回值:** number - 景德镇地情索引.


> 源码：[src/scene/ScenePlugin.js#L1062](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L1062)  
引入版本：3.7.0


---

### getStatus {#getStatus}

#### \<instance> getStatus(key) {#instance-getstatuskey}


**说明:**

复还景定地位.

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 场景从获得状态。 |


**返回值:** number - 场景状态,这个地图是`Phaser.Scene`常数,例如`Phaser.Scene.LOADING`.


> 源码：[src/scene/ScenePlugin.js#L1039](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L1039)  
引入版本：3.60.0


---

### isActive {#isActive}

#### \<instance> isActive([key]) {#instance-isactivekey}


**说明:**

检查给定的场景是否运行 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 现场检查。 |


**返回值:** boolean - 是否正在运行 Scene, 或找不到匹配 Scene 时的 `null` 。


> 源码：[src/scene/ScenePlugin.js#L751](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L751)  
引入版本：3.0.0


---

### isPaused {#isPaused}

#### \<instance> isPaused([key]) {#instance-ispausedkey}


**说明:**

检查给定的场景是否暂停 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 现场检查。 |


**返回值:** boolean - 是否暂停了场景, 或如果找不到匹配场景, 则会执行 `null` 。


> 源码：[src/scene/ScenePlugin.js#L771](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L771)  
引入版本：3.17.0


---

### isSleeping {#isSleeping}

#### \<instance> isSleeping([key]) {#instance-issleepingkey}


**说明:**

检查给定的场景是否在睡觉.

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 现场检查。 |


**返回值:** boolean - 无论是现场正在睡觉,还是如果找不到匹配的场景,则使用`null`.


> 源码：[src/scene/ScenePlugin.js#L731](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L731)  
引入版本：3.0.0


---

### isVisible {#isVisible}

#### \<instance> isVisible([key]) {#instance-isvisiblekey}


**说明:**

检查给定的场景是否可见 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 现场检查。 |


**返回值:** boolean - 是否可见场景, 或如果找不到匹配场景的 `null` 。


> 源码：[src/scene/ScenePlugin.js#L791](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L791)  
引入版本：3.0.0


---

### launch {#launch}

#### \<instance> launch(key, [data]) {#instance-launchkey-data}


**说明:**

发射给定的场景,并与这个场景平行运行.

下一场场景管理器更新时, 将不会立即发生这种情况 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 现场发射。 |
| data | object | 是 | 景德镇资料. |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L465](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L465)  
引入版本：3.0.0


---

### moveAbove {#moveAbove}

#### \<instance> moveAbove(keyA, [keyB]) {#instance-moveabovekeya-keyb}


**说明:**

移动一个场景, 使其位于场景列表中的另一场景之上。 如果场景已经高于另一场景, 则不会移动 。

这意味着它会超越其他场景的顶部

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| keyA | string \| [Phaser.Scene](/api/class/scene) | 否 | 斯景将乙宫移,以上为上. |
| keyB | string \| [Phaser.Scene](/api/class/scene) | 是 | 要移动的景物。 如果没有人给它, 则默认为此景物 。 |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L839](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L839)  
引入版本：3.2.0


---

### moveBelow {#moveBelow}

#### \<instance> moveBelow(keyA, [keyB]) {#instance-movebelowkeya-keyb}


**说明:**

移动一个场景, 使其位于场景列表中的另一场景下方。 如果场景已经位于另一场景下方, 它不会移动 。

这意味着它会让另一个场景出现

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| keyA | string \| [Phaser.Scene](/api/class/scene) | 否 | 将B场面移到下面的场景。 |
| keyB | string \| [Phaser.Scene](/api/class/scene) | 是 | 要移动的景物。 如果没有人给它, 则默认为此景物 。 |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L868](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L868)  
引入版本：3.2.0


---

### moveDown {#moveDown}

#### \<instance> moveDown([key]) {#instance-movedownkey}


**说明:**

将 Scene 列表中的一个位置下移 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 斯人之所动. |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L947](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L947)  
引入版本：3.0.0


---

### moveUp {#moveUp}

#### \<instance> moveUp([key]) {#instance-moveupkey}


**说明:**

将 Scenes 列表中的一个位置移动到上 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 斯人之所动. |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L925](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L925)  
引入版本：3.0.0


---

### pause {#pause}

#### \<instance> pause([key], [data]) {#instance-pausekey-data}


**说明:**

暂停场景 - 这阻止了更新步骤的发生, 但它仍然可以实现 。

下一场场景管理器更新时, 将不会立即发生这种情况 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 斯景止观. |
| data | object | 是 | 将传递到场景并在暂停事件中释放的可选数据对象 。 |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L523](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L523)  
引入版本：3.0.0


---

### remove {#remove}

#### \<instance> remove([key]) {#instance-removekey}


**说明:**

从场景管理器中删除场景。

场景从局部场景阵列中移除,其密钥从密钥缓存中清除出来,然后将Scene.Systems.destroy调用.

如果SceneManager在使用这种方法时正在处理Scenes,它会为下一次更新序列排队操作.

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 须除之景. |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L897](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L897)  
引入版本：3.2.0


---

### restart {#restart}

#### \<instance> restart([data]) {#instance-restartdata}


**说明:**

重开场景。

下一场场景管理器更新时, 将不会立即发生这种情况 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | object | 是 | 场景数据。 如果没有给出值, 则不会覆盖任何可能存在的先前数据 。 |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L222](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L222)  
引入版本：3.4.0


---

### resume {#resume}

#### \<instance> resume([key], [data]) {#instance-resumekey-data}


**说明:**

恢复场景 - 重新开始更新循环 。

下一场场景管理器更新时, 将不会立即发生这种情况 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 景复论曰. |
| data | object | 是 | 一个可选的数据对象, 将传递到场景中并在其恢复事件时释放 。 |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L548](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L548)  
引入版本：3.0.0


---

### run {#run}

#### \<instance> run(key, [data]) {#instance-runkey-data}


**说明:**

运行给定的景区, 但不会改变此景区的状况 。

下一场场景管理器更新时, 将不会立即发生这种情况 。

如果给定的场景暂停, 将会恢复它。 如果睡觉, 它将唤醒它。 如果完全不运行, 则会开始 。

如果您希望打开模式景, 请使用此选项, 请使用当前模式景上的 `pause` , 然后使用模式景中的 `run` 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 场景要跑. |
| data | object | 是 | 数据对象,将传递到场景并在场景的开始、醒悟或恢复时释放出来。 |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L491](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L491)  
引入版本：3.10.0


---

### sendToBack {#sendToBack}

#### \<instance> sendToBack([key]) {#instance-sendtobackkey}


**说明:**

将一个场景发送到幕后名单.

这意味着它会做出低于所有其他的幕后。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 斯人之所动. |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L993](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L993)  
引入版本：3.0.0


---

### setActive {#setActive}

#### \<instance> setActive(value, [key], [data]) {#instance-setactivevalue-key-data}


**说明:**

设置给定景区的活跃状态。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 如果 `true` 场景会恢复。 如果 `false` 将会暂停 。 |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 设定活动状态的场景 。 |
| data | object | 是 | 将传递到场景并随其事件而释放的可选数据对象 。 |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L674](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L674)  
引入版本：3.0.0


---

### setVisible {#setVisible}

#### \<instance> setVisible(value, [key]) {#instance-setvisiblevalue-key}


**说明:**

设置给定景色的可见状态。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 如果 `true` 场景会被曝光, 如果 `false` 会被隐藏 。 |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 设置可见状态的场景 。 |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L703](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L703)  
引入版本：3.0.0


---

### sleep {#sleep}

#### \<instance> sleep([key], [data]) {#instance-sleepkey-data}


**说明:**

使场景睡眠(没有更新,没有渲染),但不会关闭.

下一场场景管理器更新时, 将不会立即发生这种情况 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 斯景以安眠. |
| data | object | 是 | 一个可选的数据对象, 将会传递到场景并在它的睡眠事件中释放出来 。 |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L573](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L573)  
引入版本：3.0.0


---

### start {#start}

#### \<instance> start([key], [data]) {#instance-startkey-data}


**说明:**

关闭这个场景,运行给定的。

下一场场景管理器更新时, 将不会立即发生这种情况 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 景开场. |
| data | object | 是 | 场景数据。 如果没有给出值, 则不会覆盖任何可能存在的先前数据 。 |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L196](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L196)  
引入版本：3.0.0


---

### stop {#stop}

#### \<instance> stop([key], [data]) {#instance-stopkey-data}


**说明:**

关闭场景,清除显示列表,计时器等.

这发生在下一次场景管理器更新时,而不是立即.

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 景者止之. |
| data | any | 是 | 可选数据对象可传递至Scene.Systems.shutdown. |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L649](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L649)  
引入版本：3.0.0


---

### swapPosition {#swapPosition}

#### \<instance> swapPosition(keyA, [keyB]) {#instance-swappositionkeya-keyb}


**说明:**

换掉史景列表中两个场景的位置.

这控制了这些物品的提供和更新顺序。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| keyA | string \| [Phaser.Scene](/api/class/scene) | 否 | 首座换乘场景. |
| keyB | string \| [Phaser.Scene](/api/class/scene) | 是 | 第二场换场。 如果没有人给它, 则默认为此场景 。 |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L811](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L811)  
引入版本：3.2.0


---

### switch {#switch}

#### \<instance> switch(key, [data]) {#instance-switchkey-data}


**说明:**

使这个场景睡眠,然后开始给定的场景.

下一场场景管理器更新时, 将不会立即发生这种情况 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 景开场. |
| data | any | 是 | 可选数据对象可传递给场景 `wake`或`start`方法. |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L623](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L623)  
引入版本：3.0.0


---

### transition {#transition}

#### \<instance> transition(config) {#instance-transitionconfig}


**说明:**

这将开始从当前场景向给定的目标场景过渡.

目标场景不能与当前场景相同.

过渡将持续到以毫秒为单位的指定期间。

您可以在显示列表中将目标景移到此景的上下 。

您可以指定更新回调。 在过渡期间, 此回调将被引用_ 每个帧_ 。

此场景可以在过渡结束时被发送到睡眠, 或停止。 默认是停止 。

也有5个过渡相关的事件: 此场景会在过渡开始时释放出事件`transitionout`, 这通常是调用这种方法后的框架.

目标场景会发出事件 `transitioninit` 当场景 `init` 方法。它会发出事件 `transitionstart` 时 `create` 如果现场正在睡觉,被唤醒,它会发出事件 `transitionwake` 而不是这两个,作为幕后 `init` 财务报告和已审计财务报表 `create` 当场景醒过来时,不引用方法。

当过渡时间结束时, 将会发出 `transitioncomplete` 事件。 当场景关闭时, 全部听众都会被清除, 但如果它被送入睡眠时则不会被清除 。

必须理解,转换的持续时间始于您称之为这种方法的瞬间。 如果您正在转换到包含延迟进程, 如等待文件加载, 则即使发生这种情况, 时间仍然会算低。 如果游戏本身暂停, 或者有其他原因导致此Scase更新循环停止, 那么过渡也会暂停。 此时, 有一些检查可以防止您意外停止转换 Scue, 但是如果你有代码可以覆盖这个理解, 在目标完成前, 输入事件可能永远无法解锁 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Scenes.SceneTransitionConfig](/api/typedef/types-scenes#scenetransitionconfig) | 否 | 过渡配置对象 。 |


**返回值:** boolean - 如果过渡开始,则使用`true`,否则使用`false`.


**Fires:** [Phaser.Scenes.Events#event:TRANSITION_OUT](/api/event/scenes-events#transition_out)


> 源码：[src/scene/ScenePlugin.js#L244](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L244)  
引入版本：3.5.0


---

### wake {#wake}

#### \<instance> wake([key], [data]) {#instance-wakekey-data}


**说明:**

使场景醒悟(启动更新和渲染).

下一场场景管理器更新时, 将不会立即发生这种情况 。

**Tags:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 是 | 斯场唤醒. |
| data | object | 是 | 一个可选的数据对象, 将传递到场景并在会后事件中释放 。 |


**返回值:** [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) - 此场景插件实例 。


> 源码：[src/scene/ScenePlugin.js#L598](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/ScenePlugin.js#L598)  
引入版本：3.0.0


---

---
