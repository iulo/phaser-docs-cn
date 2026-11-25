# Systems {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/scenes-systems)

Scene Systems类是Phaser中每个Scene的主干,由Scene管理器自动创建,通过`sys`属性(如`this.sys`)从Scene内部可以访问.

系统管理一个景物的生命周期——启动,踩踏每个帧,渲染,并在需要时关闭或销毁它. 它拥有所有核心景物插件的引用(如显示列表,更新列表,摄像机管理器,以及事件 Emitter),以及只读引用全球游戏级别管理器(如纹理管理器,声音管理器,以及缓存).

您很少需要直接与系统交互; 相反, 使用 Phaser 注入到每个场景中的方便属性( 如 `this.add`, `this.cameras`, `this.events`) 。 然而, Systems 是查询 Scene 当前状态、 暂停、 恢复、 睡眠或唤醒它的权威场所 。

**构造函数**

`new Systems(scene, config)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 拥有这个系统实例的场景。 |
| config | string \| [Phaser.Types.Scenes.SettingsConfig](/api/typedef/types-scenes#settingsconfig) | 否 | 场景特定配置设置 。 |

---


**作用域**: static

> 源码：[src/scene/Systems.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L16)  
引入版本：3.0.0

## 公开成员 {#public-members}

### add {#add}

#### add: [Phaser.GameObjects.GameObjectFactory](/api/class/gameobjects-gameobjectfactory) {#add-phasergameobjectsgameobjectfactory}


**说明:**

参考景区游戏对象工厂.

利用此功能快速而轻松地创建新的游戏对象.

在默认设置中, 您可以通过 `this.add` 属性从场景内部访问此功能 。


> 源码：[src/scene/Systems.js#L190](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L190)  
引入版本：3.0.0


---

### anims {#anims}

#### anims: [Phaser.Animations.AnimationManager](/api/class/animations-animationmanager) {#anims-phaseranimationsanimationmanager}


**说明:**

参考全球动画管理器.

在默认设置中, 您可以通过 `this.anims` 属性从场景内部访问此功能 。


> 源码：[src/scene/Systems.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L109)  
引入版本：3.0.0


---

### cache {#cache}

#### cache: [Phaser.Cache.CacheManager](/api/class/cache-cachemanager) {#cache-phasercachecachemanager}


**说明:**

引用全局缓存。 缓存存储所有通过资源加载器带入的 Phaser 的文件, 除了图像。 图像存储在纹理管理器中 。

在默认设置中, 您可以通过 `this.cache` 属性从场景内部访问此功能 。


> 源码：[src/scene/Systems.js#L120](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L120)  
引入版本：3.0.0


---

### cameras {#cameras}

#### cameras: [Phaser.Cameras.Scene2D.CameraManager](/api/class/cameras-scene2d-cameramanager) {#cameras-phasercamerasscene2dcameramanager}


**说明:**

斯凯斯的摄像机经理的参考文献

使用此操作并创建此特定场景的摄像机.

在默认设置中, 您可以通过 `this.cameras` 属性从场景内部访问此功能 。


> 源码：[src/scene/Systems.js#L203](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L203)  
引入版本：3.0.0


---

### canvas {#canvas}

#### canvas: HTMLCanvasElement {#canvas-htmlcanvaselement}


**说明:**

引用 Phaser 制作的 HTML 画幅元素 。


> 源码：[src/scene/Systems.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L89)  
引入版本：3.0.0


---

### config {#config}

#### config: string, [Phaser.Types.Scenes.SettingsConfig](/api/typedef/types-scenes#settingsconfig) {#config-string-phasertypesscenessettingsconfig}


**说明:**

场景配置对象, 创建场景时所传递的对象 。


> 源码：[src/scene/Systems.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L71)  
引入版本：3.0.0


---

### context {#context}

#### context: CanvasRenderingContext2D {#context-canvasrenderingcontext2d}


**说明:**

用于渲染器使用的 Canvas 渲染上下文的参考 。


> 源码：[src/scene/Systems.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L98)  
引入版本：3.0.0


---

### displayList {#displayList}

#### displayList: [Phaser.GameObjects.DisplayList](/api/class/gameobjects-displaylist) {#displaylist-phasergameobjectsdisplaylist}


**说明:**

引用 Scene 显示列表 。

使用此选项来组织显示列表中包含的儿童 。

在默认设置中, 您可以通过 `this.children` 属性从场景内部访问此功能 。


> 源码：[src/scene/Systems.js#L216](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L216)  
引入版本：3.0.0


---

### events {#events}

#### events: [Phaser.Events.EventEmitter](/api/class/events-eventemitter) {#events-phasereventseventemitter}


**说明:**

参考景区事件经理.

使用此功能来收听场景特定事件,例如`pause`和`shutdown`.

在默认设置中, 您可以通过 `this.events` 属性从场景内部访问此功能 。


> 源码：[src/scene/Systems.js#L229](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L229)  
引入版本：3.0.0


---

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

参考 Phaser游戏实例.


> 源码：[src/scene/Systems.js#L53](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L53)  
引入版本：3.0.0


---

### make {#make}

#### make: [Phaser.GameObjects.GameObjectCreator](/api/class/gameobjects-gameobjectcreator) {#make-phasergameobjectsgameobjectcreator}


**说明:**

参考景点游戏对象创建者.

使用此选项可以快速和轻松地创建新的游戏对象。 与游戏对象工厂的区别在于, 创建者只是创建并返回游戏对象实例, 而不是将它们添加到显示列表或更新列表中 。

在默认设置中, 您可以通过 `this.make` 属性从场景内部访问此功能 。


> 源码：[src/scene/Systems.js#L242](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L242)  
引入版本：3.0.0


---

### plugins {#plugins}

#### plugins: [Phaser.Plugins.PluginManager](/api/class/plugins-pluginmanager) {#plugins-phaserpluginspluginmanager}


**说明:**

引用全局插件管理器 。

在默认设置中, 您可以通过 `this.plugins` 属性从场景内部访问此功能 。


> 源码：[src/scene/Systems.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L132)  
引入版本：3.0.0


---

### registry {#registry}

#### registry: [Phaser.Data.DataManager](/api/class/data-datamanager) {#registry-phaserdatadatamanager}


**说明:**

参考全球注册。 这是全游戏数据管理器的示例, 允许您通过通用和共享点在Scenes之间交换数据 。

在默认设置中, 您可以通过 `this.registry` 属性从场景内部访问此功能 。


> 源码：[src/scene/Systems.js#L143](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L143)  
引入版本：3.0.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer), [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrenderercanvascanvasrenderer-phaserrendererwebglwebglrenderer}


**说明:**

参考本游戏使用的Canvas或WebGL 渲染器.


> 源码：[src/scene/Systems.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L62)  
引入版本：3.17.0


---

### scale {#scale}

#### scale: [Phaser.Scale.ScaleManager](/api/class/scale-scalemanager) {#scale-phaserscalescalemanager}


**说明:**

参考全球比例管理器 。

在默认设置中, 您可以通过 `this.scale` 属性从场景内部访问此功能 。


> 源码：[src/scene/Systems.js#L155](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L155)  
引入版本：3.15.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

提到这些系统属于的场景.


> 源码：[src/scene/Systems.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L44)  
引入版本：3.0.0


---

### scenePlugin {#scenePlugin}

#### scenePlugin: [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) {#sceneplugin-phaserscenessceneplugin}


**说明:**

引用场景管理器插件 。

使用此选项来操纵游戏中的此和其他景物。 例如, 启动一个平行景物, 或者暂停或恢复景物, 或者从此景物切换到另一个景物 。

在默认设置中, 您可以通过 `this.scene` 属性从场景内部访问此功能 。


> 源码：[src/scene/Systems.js#L257](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L257)  
引入版本：3.0.0


---

### settings {#settings}

#### settings: [Phaser.Types.Scenes.SettingsObject](/api/typedef/types-scenes#settingsobject) {#settings-phasertypesscenessettingsobject}


**说明:**

场景设置。 这是基于场景配置的解析输出 。


> 源码：[src/scene/Systems.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L80)  
引入版本：3.0.0


---

### sound {#sound}

#### sound: [Phaser.Sound.NoAudioSoundManager](/api/class/sound-noaudiosoundmanager), [Phaser.Sound.HTML5AudioSoundManager](/api/class/sound-html5audiosoundmanager), [Phaser.Sound.WebAudioSoundManager](/api/class/sound-webaudiosoundmanager) {#sound-phasersoundnoaudiosoundmanager-phasersoundhtml5audiosoundmanager-phasersoundwebaudiosoundmanager}


**说明:**

参考全球音响管理器.

在默认设置中, 您可以通过 `this.sound` 属性从场景内部访问此功能 。


> 源码：[src/scene/Systems.js#L166](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L166)  
引入版本：3.0.0


---

### textures {#textures}

#### textures: [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) {#textures-phasertexturestexturemanager}


**说明:**

参考全球纹理管理器.

在默认设置中, 您可以通过 `this.textures` 属性从场景内部访问此功能 。


> 源码：[src/scene/Systems.js#L177](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L177)  
引入版本：3.0.0


---

### updateList {#updateList}

#### updateList: [Phaser.GameObjects.UpdateList](/api/class/gameobjects-updatelist) {#updatelist-phasergameobjectsupdatelist}


**说明:**

参考景区最新名单.

利用这一工具组织更新名单中的儿童。

更新列表负责管理需要他们使用`preUpdate`方法的儿童,以便处理内部组件——如有动画的Sprites.

在默认设置中,没有从场景本身中提及这一点.


> 源码：[src/scene/Systems.js#L271](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L271)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### canInput {#canInput}

#### \<instance> canInput() {#instance-caninput}


**说明:**

此场景能否接收输入事件 ?


**返回值:** boolean - 如果此场景可以接收输入事件,则使用 `true` 。


> 源码：[src/scene/Systems.js#L577](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L577)  
引入版本：3.60.0


---

### depthSort {#depthSort}

#### \<instance> depthSort() {#instance-depthsort}


**说明:**

如果设置了旗, 立即排序显示列表 。


> 源码：[src/scene/Systems.js#L398](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L398)  
引入版本：3.0.0


---

### getData {#getData}

#### \<instance> getData() {#instance-getdata}


**说明:**

返回由另一个场景发送到此场景的任何数据 。

数据也传递到`Scene.init`和各种场景事件,但您可以通过这种方法随时访问.


**返回值:** any - 景德镇志.


> 源码：[src/scene/Systems.js#L548](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L548)  
引入版本：3.22.0


---

### getStatus {#getStatus}

#### \<instance> getStatus() {#instance-getstatus}


**说明:**

返回此场景的当前状态 。


**返回值:** number - 这个场景的状态,`Phaser.Scene`常数之一.


> 源码：[src/scene/Systems.js#L564](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L564)  
引入版本：3.60.0


---

### init {#init}

#### \<instance> init(game) {#instance-initgame}


**说明:**

这种方法在Scene 管理器即时调用时仅被Scene 管理者调用一次,负责设置所有Scene 插件和引用,永远不应直接调用.


**访问权限:** 受保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 参考 Phaser游戏实例. |


**触发事件:** [Phaser.Scenes.Events#event:BOOT](/api/event/scenes-events#boot)


> 源码：[src/scene/Systems.js#L301](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L301)  
引入版本：3.0.0


---

### isActive {#isActive}

#### \<instance> isActive() {#instance-isactive}


**说明:**

这是场景在运行吗?


**返回值:** boolean - 如果场景在运行,就用`true`,否则用`false`.


> 源码：[src/scene/Systems.js#L605](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L605)  
引入版本：3.0.0


---

### isPaused {#isPaused}

#### \<instance> isPaused() {#instance-ispaused}


**说明:**

场景暂停了吗?


**返回值:** boolean - 如果暂停的话,请按`true`,否则按`false`.


> 源码：[src/scene/Systems.js#L618](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L618)  
引入版本：3.13.0


---

### isSleeping {#isSleeping}

#### \<instance> isSleeping() {#instance-issleeping}


**说明:**

这是场景睡觉吗?


**返回值:** boolean - 如果这幕睡着了,就用`true`,否则用`false`.


> 源码：[src/scene/Systems.js#L592](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L592)  
引入版本：3.0.0


---

### isTransitionIn {#isTransitionIn}

#### \<instance> isTransitionIn() {#instance-istransitionin}


**说明:**

此场景是否正在从另一个场景过渡 ?


**返回值:** boolean - 如果这个场景从另一个场景过渡,则`true`,否则则`false`.


> 源码：[src/scene/Systems.js#L657](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L657)  
引入版本：3.5.0


---

### isTransitioning {#isTransitioning}

#### \<instance> isTransitioning() {#instance-istransitioning}


**说明:**

这是正在向另一个场景过渡还是从另一个场景过渡?


**返回值:** boolean - 如果目前场景正在过渡,则使用`true`,否则使用`false`.


> 源码：[src/scene/Systems.js#L631](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L631)  
引入版本：3.5.0


---

### isTransitionOut {#isTransitionOut}

#### \<instance> isTransitionOut() {#instance-istransitionout}


**说明:**

这是目前从自己向另一个场景过渡的场景吗?


**返回值:** boolean - 如果这幕正在向另一幕过渡,则`true`,否则则`false`.


> 源码：[src/scene/Systems.js#L644](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L644)  
引入版本：3.5.0


---

### isVisible {#isVisible}

#### \<instance> isVisible() {#instance-isvisible}


**说明:**

这是场景可见和渲染吗?


**返回值:** boolean - 如果这幕景可见,则`true`,否则则`false`.


> 源码：[src/scene/Systems.js#L670](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L670)  
引入版本：3.0.0


---

### pause {#pause}

#### \<instance> pause([data]) {#instance-pausedata}


**说明:**

暂停这个场景。

暂停的场景仍然使 它只是没有运行任何更新的处理器或系统。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | object | 是 | 在“ 暂停” 事件中传递的数据对象 。 |


**返回值:** [Phaser.Scenes.Systems](/api/class/scenes-systems) - 此系统对象 。


**触发事件:** [Phaser.Scenes.Events#event:PAUSE](/api/event/scenes-events#pause)


> 源码：[src/scene/Systems.js#L409](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L409)  
引入版本：3.0.0


---

### queueDepthSort {#queueDepthSort}

#### \<instance> queueDepthSort() {#instance-queuedepthsort}


**说明:**

强制在下一个渲染时显示列表的某种 。


> 源码：[src/scene/Systems.js#L387](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L387)  
引入版本：3.0.0


---

### render {#render}

#### \<instance> render(renderer) {#instance-renderrenderer}


**说明:**

由场景管理器自动调用。 指示场景通过摄像机管理器向给定的渲染器进行自我渲染 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) \| [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 提起"渲染"的造物师 |


**触发事件:** [Phaser.Scenes.Events#event:PRE_RENDER](/api/event/scenes-events#pre_render), [Phaser.Scenes.Events#event:RENDER](/api/event/scenes-events#render)


> 源码：[src/scene/Systems.js#L363](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L363)  
引入版本：3.0.0


---

### resume {#resume}

#### \<instance> resume([data]) {#instance-resumedata}


**说明:**

恢复此场景的暂停状态 。

恢复一个 Scene 将其状态设定为 RUNNING 并标记为活动, 允许其更新循环再次执行。 如果 Scene 尚未暂停, 则无效 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | object | 是 | 将在“ resume” 事件中传递的数据对象 。 |


**返回值:** [Phaser.Scenes.Systems](/api/class/scenes-systems) - 此系统对象 。


**触发事件:** [Phaser.Scenes.Events#event:RESUME](/api/event/scenes-events#resume)


> 源码：[src/scene/Systems.js#L443](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L443)  
引入版本：3.0.0


---

### setActive {#setActive}

#### \<instance> setActive(value, [data]) {#instance-setactivevalue-data}


**说明:**

设定此场景的活跃状态 。

一个活动场景将运行其核心更新循环.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 如果 `true` 场景会恢复, 如果先前暂停。 如果 `false` 将会暂停 。 |
| data | object | 是 | 将在“ 假设” 或“ 暂停” 事件中传递的数据对象 。 |


**返回值:** [Phaser.Scenes.Systems](/api/class/scenes-systems) - 此系统对象 。


> 源码：[src/scene/Systems.js#L701](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L701)  
引入版本：3.0.0


---

### setVisible {#setVisible}

#### \<instance> setVisible(value) {#instance-setvisiblevalue}


**说明:**

设置此场景的可见状态。 一个无形的场景不会渲染, 但会继续处理更新 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 制作这个场景的`true`, 否则是`false`. |


**返回值:** [Phaser.Scenes.Systems](/api/class/scenes-systems) - 此系统对象 。


> 源码：[src/scene/Systems.js#L683](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L683)  
引入版本：3.0.0


---

### shutdown {#shutdown}

#### \<instance> shutdown([data]) {#instance-shutdowndata}


**说明:**

关闭此场景并发送一个关闭事件到它的所有系统。 已经关闭的场景不会运行其更新循环或渲染, 但不会破坏其任何插件或引用。 它会被放入休眠状态, 供以后使用。 如果您再也没有计划使用此场景, 那么它应该被销毁, 以释放资源 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | object | 是 | 一个数据对象,将在“shutdown”事件中传递 。 |


**触发事件:** [Phaser.Scenes.Events#event:SHUTDOWN](/api/event/scenes-events#shutdown)


> 源码：[src/scene/Systems.js#L759](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L759)  
引入版本：3.0.0


---

### sleep {#sleep}

#### \<instance> sleep([data]) {#instance-sleepdata}


**说明:**

送此场景入睡.

沉睡的场景不会运行其更新步骤或渲染任何东西,但是它也没有关闭,也没有被任何系统或儿童移除,这意味着它可以在任何时间重新激活,并且会从它留下的地方继续,它也把一切保存在记忆中,事件和来自其他场景的回电可能仍然在其中引用变化,所以要小心剩下的活动.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | object | 是 | 在“ 睡眠” 事件中传递的数据对象 。 |


**返回值:** [Phaser.Scenes.Systems](/api/class/scenes-systems) - 此系统对象 。


**触发事件:** [Phaser.Scenes.Events#event:SLEEP](/api/event/scenes-events#sleep)


> 源码：[src/scene/Systems.js#L474](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L474)  
引入版本：3.0.0


---

### start {#start}

#### \<instance> start(data) {#instance-startdata}


**说明:**

启动此场景运行和渲染。 由场景管理器自动调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | object | 否 | 可能从另一个位置传递到此景点的可选数据对象 。 |


**触发事件:** [Phaser.Scenes.Events#event:START](/api/event/scenes-events#start), [Phaser.Scenes.Events#event:READY](/api/event/scenes-events#ready)


> 源码：[src/scene/Systems.js#L726](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L726)  
引入版本：3.0.0


---

### step {#step}

#### \<instance> step(time, delta) {#instance-steptime-delta}


**说明:**

单游戏步骤。 由场景管理器自动调用, 原因是请求动画框架或设定超时调用主游戏实例 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 最新游戏步骤的时间值。 通常为高分辨率定时器值, 或 Date. now () 。 |
| delta | number | 否 | 自上一个框架以来的三角洲值。 这是为避免三角洲的悬崖被 TimeStep 级所覆盖而平滑的 。 |


**触发事件:** [Phaser.Scenes.Events#event:PRE_UPDATE](/api/event/scenes-events#pre_update), [Phaser.Scenes.Events#event:UPDATE](/api/event/scenes-events#update), [Phaser.Scenes.Events#event:POST_UPDATE](/api/event/scenes-events#post_update)


> 源码：[src/scene/Systems.js#L337](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L337)  
引入版本：3.0.0


---

### wake {#wake}

#### \<instance> wake([data]) {#instance-wakedata}


**说明:**

唤醒这个场景,如果它之前被送去睡觉。

摇晃一幕将状态设定为运行状态,并标为活动状态和可见状态,允许其更新循环执行,并再次渲染摄像机。不同于 `resume`,它只恢复了活动旗帜, `wake` 如果场景是正在进行的过渡的一部分,则 a `TRANSITION_WAKE` 事件也会被释放。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | object | 是 | 一个数据对象,将在“ 醒” 事件中传递 。 |


**返回值:** [Phaser.Scenes.Systems](/api/class/scenes-systems) - 此系统对象 。


**触发事件:** [Phaser.Scenes.Events#event:WAKE](/api/event/scenes-events#wake)


> 源码：[src/scene/Systems.js#L512](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Systems.js#L512)  
引入版本：3.0.0


---

---
