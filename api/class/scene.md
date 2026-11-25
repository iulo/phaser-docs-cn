# Scene {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/scene)

`Phaser.Scene` 是场景的基类，可以继承它来实现自己的场景。

场景是 Phaser 的基本组织单位。每个场景都有自己的显示列表、更新循环、摄像机、输入处理和资源加载器。多个场景可以同时运行，例如在游戏场景上叠加一个 UI 场景。`SceneManager` 负责管理场景，各场景通过 `ScenePlugin` 交换信息。

可以按需定义 [init()](/api/typedef/types-scenes#sceneinitcallback)、[preload()](/api/typedef/types-scenes#scenepreloadcallback) 和 [create()](/api/typedef/types-scenes#scenecreatecallback) 方法。

**构造函数**

`new Scene([config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | string \| [Phaser.Types.Scenes.SettingsConfig](/api/typedef/types-scenes#settingsconfig) | 是 | 场景密钥或场景特定配置设置. |

---


**作用域**: static

> 源码：[src/scene/Scene.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L10)  
引入版本：3.0.0

## 公开成员 {#public-members}

### add {#add}

#### add: [Phaser.GameObjects.GameObjectFactory](/api/class/gameobjects-gameobjectfactory) {#add-phasergameobjectsgameobjectfactory}


**说明:**

场景游戏对象工厂.

只有在 Scene 注射图中定义此属性时, 才能使用 。


> 源码：[src/scene/Scene.js#L131](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L131)  
引入版本：3.0.0


---

### anims {#anims}

#### anims: [Phaser.Animations.AnimationManager](/api/class/animations-animationmanager) {#anims-phaseranimationsanimationmanager}


**说明:**

参考全球动画管理器.

只有在 Scene 注射图中定义此属性时, 才能使用 。


> 源码：[src/scene/Scene.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L54)  
引入版本：3.0.0


---

### cache {#cache}

#### cache: [Phaser.Cache.CacheManager](/api/class/cache-cachemanager) {#cache-phasercachecachemanager}


**说明:**

参考全球缓存 。

只有在 Scene 注射图中定义此属性时, 才能使用 。


> 源码：[src/scene/Scene.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L65)  
引入版本：3.0.0


---

### cameras {#cameras}

#### cameras: [Phaser.Cameras.Scene2D.CameraManager](/api/class/cameras-scene2d-cameramanager) {#cameras-phasercamerasscene2dcameramanager}


**说明:**

场景摄像机经理

只有在 Scene 注射图中定义此属性时, 才能使用 。


> 源码：[src/scene/Scene.js#L120](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L120)  
引入版本：3.0.0


---

### children {#children}

#### children: [Phaser.GameObjects.DisplayList](/api/class/gameobjects-displaylist) {#children-phasergameobjectsdisplaylist}


**说明:**

属于此场景的游戏对象显示列表 。

只有在 Scene 注射图中定义此属性时, 才能使用 。


> 源码：[src/scene/Scene.js#L164](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L164)  
引入版本：3.0.0


---

### data {#data}

#### data: [Phaser.Data.DataManager](/api/class/data-datamanager) {#data-phaserdatadatamanager}


**说明:**

场景特定的数据管理器插件 。

参见全球数据管理器的`registry`属性.

只有Scene注射图中定义并安装插件时,此属性才会可用.


> 源码：[src/scene/Scene.js#L186](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L186)  
引入版本：3.0.0


---

### events {#events}

#### events: [Phaser.Events.EventEmitter](/api/class/events-eventemitter) {#events-phasereventseventemitter}


**说明:**

场景特异性事件 Emitter.

只有在 Scene 注射图中定义此属性时, 才能使用 。


> 源码：[src/scene/Scene.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L109)  
引入版本：3.0.0


---

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

参考Phaser.Game案例.

只有在 Scene 注射图中定义此属性时, 才能使用 。


> 源码：[src/scene/Scene.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L43)  
引入版本：3.0.0


---

### input {#input}

#### input: [Phaser.Input.InputPlugin](/api/class/input-inputplugin) {#input-phaserinputinputplugin}


**说明:**

场景输入管理器插件 。

只有Scene注射图中定义并安装插件时,此属性才会可用.


> 源码：[src/scene/Scene.js#L199](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L199)  
引入版本：3.0.0


---

### lights {#lights}

#### lights: [Phaser.GameObjects.LightsManager](/api/class/gameobjects-lightsmanager) {#lights-phasergameobjectslightsmanager}


**说明:**

场景灯光管理器插件 。

只有Scene注射图中定义并安装插件时,此属性才会可用.


> 源码：[src/scene/Scene.js#L175](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L175)  
引入版本：3.0.0


---

### load {#load}

#### load: [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) {#load-phaserloaderloaderplugin}


**说明:**

场景装填器插件 。

只有Scene注射图中定义并安装插件时,此属性才会可用.


> 源码：[src/scene/Scene.js#L210](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L210)  
引入版本：3.0.0


---

### make {#make}

#### make: [Phaser.GameObjects.GameObjectCreator](/api/class/gameobjects-gameobjectcreator) {#make-phasergameobjectsgameobjectcreator}


**说明:**

场景游戏对象创建者.

只有在 Scene 注射图中定义此属性时, 才能使用 。


> 源码：[src/scene/Scene.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L142)  
引入版本：3.0.0


---

### matter {#matter}

#### matter: [Phaser.Physics.Matter.MatterPhysics](/api/class/physics-matter-matterphysics) {#matter-phaserphysicsmattermatterphysics}


**说明:**

场景物质物理插件 。

只有当 Scene 注射地图中定义了此属性, 插件才会被安装和配置 。


> 源码：[src/scene/Scene.js#L254](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L254)  
引入版本：3.0.0


---

### physics {#physics}

#### physics: [Phaser.Physics.Arcade.ArcadePhysics](/api/class/physics-arcade-arcadephysics) {#physics-phaserphysicsarcadearcadephysics}


**说明:**

场景拱廊物理插件。

只有当 Scene 注射地图中定义了此属性, 插件才会被安装和配置 。


> 源码：[src/scene/Scene.js#L243](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L243)  
引入版本：3.0.0


---

### plugins {#plugins}

#### plugins: [Phaser.Plugins.PluginManager](/api/class/plugins-pluginmanager) {#plugins-phaserpluginspluginmanager}


**说明:**

引用全局插件管理器 。

插件管理器是一个全局系统,允许插件自己用它注册,然后可以根据需要将这些插件安装到Scenes中.


> 源码：[src/scene/Scene.js#L276](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L276)  
引入版本：3.0.0


---

### registry {#registry}

#### registry: [Phaser.Data.DataManager](/api/class/data-datamanager) {#registry-phaserdatadatamanager}


**说明:**

参考全球数据管理器.

只有在 Scene 注射图中定义此属性时, 才能使用 。


> 源码：[src/scene/Scene.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L76)  
引入版本：3.0.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer), [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrenderercanvascanvasrenderer-phaserrendererwebglwebglrenderer}


**说明:**

使用Phaser的制造器实例,或者Canvas renderer,或者WebGL renderer。


> 源码：[src/scene/Scene.js#L288](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L288)  
引入版本：3.50.0


---

### scale {#scale}

#### scale: [Phaser.Scale.ScaleManager](/api/class/scale-scalemanager) {#scale-phaserscalescalemanager}


**说明:**

参考全球比例管理器 。

只有在 Scene 注射图中定义此属性时, 才能使用 。


> 源码：[src/scene/Scene.js#L265](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L265)  
引入版本：3.16.2


---

### scene {#scene}

#### scene: [Phaser.Scenes.ScenePlugin](/api/class/scenes-sceneplugin) {#scene-phaserscenessceneplugin}


**说明:**

引用场景管理器插件 。

只有在 Scene 注射图中定义此属性时, 才能使用 。


> 源码：[src/scene/Scene.js#L153](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L153)  
引入版本：3.0.0


---

### sound {#sound}

#### sound: [Phaser.Sound.NoAudioSoundManager](/api/class/sound-noaudiosoundmanager), [Phaser.Sound.HTML5AudioSoundManager](/api/class/sound-html5audiosoundmanager), [Phaser.Sound.WebAudioSoundManager](/api/class/sound-webaudiosoundmanager) {#sound-phasersoundnoaudiosoundmanager-phasersoundhtml5audiosoundmanager-phasersoundwebaudiosoundmanager}


**说明:**

音效管理器的参考文献.

只有Scene注射图中定义并安装插件时,此属性才会可用.


> 源码：[src/scene/Scene.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L87)  
引入版本：3.0.0


---

### sys {#sys}

#### sys: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#sys-phaserscenessystems}


**说明:**

场景系统,你永远不能覆盖这个地产 否则所有的地狱都会崩溃的


> 源码：[src/scene/Scene.js#L34](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L34)  
引入版本：3.0.0


---

### textures {#textures}

#### textures: [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) {#textures-phasertexturestexturemanager}


**说明:**

纹理管理器的参考文献.

只有在 Scene 注射图中定义此属性时, 才能使用 。


> 源码：[src/scene/Scene.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L98)  
引入版本：3.0.0


---

### time {#time}

#### time: [Phaser.Time.Clock](/api/class/time-clock) {#time-phasertimeclock}


**说明:**

场景时间和时钟插件 。

只有Scene注射图中定义并安装插件时,此属性才会可用.


> 源码：[src/scene/Scene.js#L221](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L221)  
引入版本：3.0.0


---

### tweens {#tweens}

#### tweens: [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) {#tweens-phasertweenstweenmanager}


**说明:**

场景 Tween 管理器插件 。

只有Scene注射图中定义并安装插件时,此属性才会可用.


> 源码：[src/scene/Scene.js#L232](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L232)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### update {#update}

#### \<instance> update(time, delta) {#instance-updatetime-delta}


**说明:**

在您自己的 Scene 子类中覆盖此方法,以实施每帧游戏逻辑 。

这种方法在场景运行时,每游戏步骤自动称为一次,默认为空,是放置逻辑的首要位置,需要运行每个帧,如更新游戏对象位置,检查碰撞,或读取输入状态.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/scene/Scene.js#L298](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/Scene.js#L298)  
引入版本：3.0.0


---

---
