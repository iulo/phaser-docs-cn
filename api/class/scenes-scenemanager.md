# SceneManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/scenes-scenemanager)

场景经理.

场景管理器是一个游戏级别系统,负责在游戏实例中创建,处理和更新所有场景.

您通常不应该直接与场景管理器互动。 相反, 您应该使用场景插件, 它可以通过 `this.scene` 属性从游戏中的每个场景中获取 。

使用此场景管理器中的方法会直接断开队列操作, 并可能引发运行时间错误 。 相反, 通过场景管理器的插件。 此场景管理器提供的每个特性也可以通过场景插件使用 。

**构造函数**

`new SceneManager(game, sceneConfig)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 这个场景管理器属于Phaser.Game的例. |
| sceneConfig | object | 否 | 场景特定配置设置 。 |

---


**作用域**: static

> 源码：[src/scene/SceneManager.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L17)  
引入版本：3.0.0

## 公开成员 {#public-members}

### customViewports {#customViewports}

#### customViewports: number {#customviewports-number}


**说明:**

任何镜头中的任何镜头都需要自定义的视窗吗?


> 源码：[src/scene/SceneManager.js#L134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L134)  
引入版本：3.12.0


---

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

此 SceneManager 属于的游戏 。


> 源码：[src/scene/SceneManager.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L45)  
引入版本：3.0.0


---

### isBooted {#isBooted}

#### isBooted: boolean {#isbooted-boolean}


**说明:**

场景管理器正常开始了吗?


> 源码：[src/scene/SceneManager.js#L123](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L123)  
引入版本：3.4.0


---

### isProcessing {#isProcessing}

#### isProcessing: boolean {#isprocessing-boolean}


**说明:**

场景管理者是否在积极处理场景列表?.


> 源码：[src/scene/SceneManager.js#L112](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L112)  
引入版本：3.0.0


---

### keys {#keys}

#### keys: Record.\<string, [Phaser.Scene](/api/class/scene)> {#keys-recordstring-phaserscene}


**说明:**

一个将键映射到现场的物体,这样我们就可以从一个键上快速地得到一个没有迭代的场景.


> 源码：[src/scene/SceneManager.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L54)  
引入版本：3.0.0


---

### scenes {#scenes}

#### scenes: Array.\<[Phaser.Scene](/api/class/scene)> {#scenes-arrayphaserscene}


**说明:**

所有场景都保存在其中的阵列.


> 源码：[src/scene/SceneManager.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L63)  
引入版本：3.0.0


---

### systemScene {#systemScene}

#### systemScene: [Phaser.Scene](/api/class/scene) {#systemscene-phaserscene}


**说明:**

此系统 Scene是在`bootQueue`期间创建的,是默认的空空 Scene ,它生活在 Scene 列表之外,但可以被需要访问一个活的 Scene 的插件和管理者使用,而无需绑定在其中.


> 源码：[src/scene/SceneManager.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L145)  
引入版本：3.60.0


---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(key, sceneConfig, [autoStart], [data]) {#instance-addkey-sceneconfig-autostart-data}


**说明:**

将新场景添加到场景管理器中。您必须给每个场景一个独特的键,您可以通过它来识别它。

The `sceneConfig` can be:

* 一个`Phaser.Scene`物体,或者一个能扩展它的物体.

* 一个简单的 JavaScript 对象

* A. 国家 JavaScript 扩展的ES6类 `Phaser.Scene`

* 以 JavaScript ES5 为基础的原型类

* JavaScript 函数

如果给定了一个函数,那么通过调用将创建一个新场景.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 一个独特的键用于引用景色,即`MainMenu`或`Level1`. |
| sceneConfig | [Phaser.Types.Scenes.SceneType](/api/typedef/types-scenes#scenetype) | 否 |  | 场景的配置 |
| autoStart | boolean | 是 | false | 如果 `true` , 场景会在添加后立即开始 。 |
| data | object | 是 |  | 可选数据对象。 这将设定为 `Scene.settings.data` 并传递到 `Scene.init` 和 `Scene.create` 。 |


**返回值:** [Phaser.Scene](/api/class/scene) - 增加的场景,如果立即加,否则会`null`.


> 源码：[src/scene/SceneManager.js#L322](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L322)  
引入版本：3.0.0


---

### bringToTop {#bringToTop}

#### \<instance> bringToTop(key) {#instance-bringtotopkey}


**说明:**

将场景列入"幕后人物"名单中.

也就是说它会让其他的幕后人物 都更受欢迎

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 斯人之所动. |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1384](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1384)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这个场景管理器和它的所有系统

这一进程不能逆转。

当一个 Phaser 游戏实例被破坏时,这种方法会自动称为.


> 源码：[src/scene/SceneManager.js#L1709](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1709)  
引入版本：3.0.0


---

### dump {#dump}

#### \<instance> dump() {#instance-dump}


**说明:**

向开发者控制台跳槽调试每个场景的信息.


> 源码：[src/scene/SceneManager.js#L1685](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1685)  
引入版本：3.2.0


---

### getAt {#getAt}

#### \<instance> getAt(index) {#instance-getatindex}


**说明:**

按数值索引检索一个场景。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 用于检索的场景索引 。 |


**返回值:** [Phaser.Scene](/api/class/scene), undefined - 景之所见.


> 源码：[src/scene/SceneManager.js#L1346](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1346)  
引入版本：3.0.0


---

### getIndex {#getIndex}

#### \<instance> getIndex(key) {#instance-getindexkey}


**说明:**

检索一个场景的数值索引。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 景之钥. |


**返回值:** number - 景德镇地情索引.


> 源码：[src/scene/SceneManager.js#L1364](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1364)  
引入版本：3.0.0


---

### getScene {#getScene}

#### \<instance> getScene(key) {#instance-getscenekey}


**说明:**

基于给定的键获取一个场景 。

如果将实际的场景传递到这种方法,可以用来检查其目前是否在场景管理器内,或者没有.

**标签:**

 - generic
 - genericUse
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 取回场景的钥匙. |


**返回值:** [Phaser.Scene](/api/class/scene) - 场景,或者如果找不到匹配的场景,则使用`null`.


> 源码：[src/scene/SceneManager.js#L881](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L881)  
引入版本：3.0.0


---

### getScenes {#getScenes}

#### \<instance> getScenes([isActive], [inReverse]) {#instance-getscenesisactive-inreverse}


**说明:**

返回由此场景管理器管理的所有当前场景的数组 。

您可以通过 Scene 的活跃状态过滤输出, 选择使数组按正常或反转顺序返回 。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| isActive | boolean | 是 | true | 只包括目前活动场景的场景吗? |
| inReverse | boolean | 是 | false | 倒转返回Scenes的阵列吗 ? |


**返回值:** Array.\<[Phaser.Scene](/api/class/scene)> - 包含全部场景的阵列, 包含场景管理器 。


> 源码：[src/scene/SceneManager.js#L843](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L843)  
引入版本：3.16.0


---

### isActive {#isActive}

#### \<instance> isActive(key) {#instance-isactivekey}


**说明:**

确定是否正在运行场景 。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 现场检查。 |


**返回值:** boolean - 是否正在运行 Scene, 或找不到匹配 Scene 时的 `null` 。


> 源码：[src/scene/SceneManager.js#L921](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L921)  
引入版本：3.0.0


---

### isPaused {#isPaused}

#### \<instance> isPaused(key) {#instance-ispausedkey}


**说明:**

确定是否暂停场景。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 现场检查。 |


**返回值:** boolean - 是否暂停了场景, 或如果找不到匹配场景, 则会执行 `null` 。


> 源码：[src/scene/SceneManager.js#L946](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L946)  
引入版本：3.17.0


---

### isSleeping {#isSleeping}

#### \<instance> isSleeping(key) {#instance-issleepingkey}


**说明:**

确定场景是否在睡觉。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 现场检查。 |


**返回值:** boolean - 无论是现场正在睡觉,还是如果找不到匹配的场景,则使用`null`.


> 源码：[src/scene/SceneManager.js#L996](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L996)  
引入版本：3.0.0


---

### isVisible {#isVisible}

#### \<instance> isVisible(key) {#instance-isvisiblekey}


**说明:**

确定场景是否可见。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 现场检查。 |


**返回值:** boolean - 是否可见场景, 或如果找不到匹配场景的 `null` 。


> 源码：[src/scene/SceneManager.js#L971](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L971)  
引入版本：3.0.0


---

### moveAbove {#moveAbove}

#### \<instance> moveAbove(keyA, keyB) {#instance-moveabovekeya-keyb}


**说明:**

移动一个场景, 使其位于场景列表中的另一场景之上。 如果场景已经高于另一场景, 则不会移动 。

这意味着它会超越其他场景的顶部

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| keyA | string \| [Phaser.Scene](/api/class/scene) | 否 | 乙场的场景会被移动到上面 |
| keyB | string \| [Phaser.Scene](/api/class/scene) | 否 | 须移之景. |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1525](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1525)  
引入版本：3.2.0


---

### moveBelow {#moveBelow}

#### \<instance> moveBelow(keyA, keyB) {#instance-movebelowkeya-keyb}


**说明:**

移动一个场景, 使其位于场景列表中的另一场景下方。 如果场景已经位于另一场景下方, 它不会移动 。

这意味着它会让另一个场景出现

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| keyA | string \| [Phaser.Scene](/api/class/scene) | 否 | 将B场景移到下面的场景。 |
| keyB | string \| [Phaser.Scene](/api/class/scene) | 否 | 须移之景. |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1571](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1571)  
引入版本：3.2.0


---

### moveDown {#moveDown}

#### \<instance> moveDown(key) {#instance-movedownkey}


**说明:**

将 Scene 列表中的一个位置下移 。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 斯人之所动. |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1455](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1455)  
引入版本：3.0.0


---

### moveUp {#moveUp}

#### \<instance> moveUp(key) {#instance-moveupkey}


**说明:**

将 Scenes 列表中的一个位置移动到上 。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 斯人之所动. |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1490](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1490)  
引入版本：3.0.0


---

### pause {#pause}

#### \<instance> pause(key, [data]) {#instance-pausekey-data}


**说明:**

暂停给定的场景。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 斯景止观. |
| data | object | 是 | 一个可选数据对象, 将传递到场景并因其暂停事件而释放 。 |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1021](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1021)  
引入版本：3.0.0


---

### processQueue {#processQueue}

#### \<instance> processQueue() {#instance-processqueue}


**说明:**

处理 `_pending` 列表中待决的景色添加, 并执行 `_queue` 列表中队列中的任何景色操作, 如启动、停止、睡眠、醒悟和命令更改。 这种方法在游戏步骤开始时自动调用, 不应直接调用 。


> 源码：[src/scene/SceneManager.js#L268](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L268)  
引入版本：3.0.0


---

### remove {#remove}

#### \<instance> remove(key) {#instance-removekey}


**说明:**

从场景管理器中删除场景。

场景从局部场景阵列中移除,其键从键缓存中清除出来,然后将Scene.Systems.destroy调用.

如果SceneManager在使用这种方法时正在处理Scenes,它会为下一次更新序列排队操作.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 一个独特的键用于引用景色,即`MainMenu`或`Level1`. |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L413](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L413)  
引入版本：3.2.0


---

### render {#render}

#### \<instance> render(renderer) {#instance-renderrenderer}


**说明:**

摄摄诸法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) \| [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拟用之造化器. |


> 源码：[src/scene/SceneManager.js#L581](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L581)  
引入版本：3.0.0


---

### resume {#resume}

#### \<instance> resume(key, [data]) {#instance-resumekey-data}


**说明:**

复次给定场场.

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 景复论曰. |
| data | object | 是 | 一个可选的数据对象,将传递到场景并因其恢复事件而释放出来. |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1047](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1047)  
引入版本：3.0.0


---

### run {#run}

#### \<instance> run(key, [data]) {#instance-runkey-data}


**说明:**

运行给定的场景。

如果给定的场景暂停, 将会恢复它。 如果睡觉, 它将唤醒它。 如果完全不运行, 则会开始 。

如果您希望打开模式景, 请使用此选项, 请使用当前模式景上的 `pause` , 然后使用模式景中的 `run` 。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 场景要跑. |
| data | object | 是 | 一个数据对象,将在启动、醒悟或恢复时传递到场景。 |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1125)  
引入版本：3.10.0


---

### sendToBack {#sendToBack}

#### \<instance> sendToBack(key) {#instance-sendtobackkey}


**说明:**

将一个场景发送到幕后名单.

这意味着它会做出低于所有其他的幕后。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 斯人之所动. |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1420](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1420)  
引入版本：3.0.0


---

### sleep {#sleep}

#### \<instance> sleep(key, [data]) {#instance-sleepkey-data}


**说明:**

使给定的场景入睡.

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 斯景以安眠. |
| data | object | 是 | 将传递到场景并因其睡眠事件而释放的可选数据对象 。 |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1073](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1073)  
引入版本：3.0.0


---

### start {#start}

#### \<instance> start(key, [data]) {#instance-startkey-data}


**说明:**

启动给定的场景, 如果它不是开始、 装入或创建的话 。

如果场景在运行,暂停,或睡觉,它会关闭然后开始.

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 景开场. |
| data | object | 是 | 可选数据对象通过`Scene.Settings`和`Scene.init`,以及`Scene.create`. |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1179](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1179)  
引入版本：3.0.0


---

### stop {#stop}

#### \<instance> stop(key, [data]) {#instance-stopkey-data}


**说明:**

停止给定的场景。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 景者止之. |
| data | object | 是 | 可选数据对象可传递至Scene.shutdown. |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1275](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1275)  
引入版本：3.0.0


---

### swapPosition {#swapPosition}

#### \<instance> swapPosition(keyA, keyB) {#instance-swappositionkeya-keyb}


**说明:**

换掉两个Scenes在Scenes列表中的位置.

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| keyA | string \| [Phaser.Scene](/api/class/scene) | 否 | 首座换乘场景. |
| keyB | string \| [Phaser.Scene](/api/class/scene) | 否 | 第二场换人 |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1645](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1645)  
引入版本：3.0.0


---

### switch {#switch}

#### \<instance> switch(from, to, [data]) {#instance-switchfrom-to-data}


**说明:**

睡一幕而起彼处.

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| from | string \| [Phaser.Scene](/api/class/scene) | 否 | 斯场而眠. |
| to | string \| [Phaser.Scene](/api/class/scene) | 否 | 景开场. |
| data | object | 是 | 可选数据对象通过`Scene.Settings`和`Scene.init`,以及`Scene.create`,只有在场景首次开始时才通过. |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1309](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1309)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update(time, delta) {#instance-updatetime-delta}


**说明:**

更新Scees。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 目前的游戏时间戳,以毫秒计. |
| delta | number | 否 | 三角洲时间,以毫秒计,自上一个游戏步骤后已经过去. |


> 源码：[src/scene/SceneManager.js#L549](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L549)  
引入版本：3.0.0


---

### wake {#wake}

#### \<instance> wake(key, [data]) {#instance-wakekey-data}


**说明:**

唤醒了给定的场景。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Scene](/api/class/scene) | 否 | 斯场唤醒. |
| data | object | 是 | 将传递到场景并因其醒悟事件而释放的可选数据对象 。 |


**返回值:** [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) - 这个场景管理器实例 。


> 源码：[src/scene/SceneManager.js#L1099](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/SceneManager.js#L1099)  
引入版本：3.0.0


---

---
