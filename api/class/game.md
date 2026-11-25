# Game {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/game)

Phaser.Game实例是整个Phaser游戏的主要控制器,负责处理启动进程,解析配置值,创建渲染器,并设置全球Phaser系统,如声音和输入。一旦完成,它将启动场景管理器,然后开始游戏主循环。

您一般应该避免访问Game创建的任何系统,而使用通过Phaser.Scene系统类提供给您的系统.

**构造函数**

`new Game([config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Core.GameConfig](/api/typedef/types-core#gameconfig) | 是 | 您的 Phaser 游戏实例的配置对象 。 |

---


**作用域**: static

> 源码：[src/core/Game.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L36)  
引入版本：3.0.0

## 公开成员 {#public-members}

### anims {#anims}

#### anims: [Phaser.Animations.AnimationManager](/api/class/animations-animationmanager) {#anims-phaseranimationsanimationmanager}


**说明:**

动画经理的一个例子.

动画管理器是一个全球系统,负责管理游戏中所有使用的动画.


> 源码：[src/core/Game.js#L151](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L151)  
引入版本：3.0.0


---

### cache {#cache}

#### cache: [Phaser.Cache.CacheManager](/api/class/cache-cachemanager) {#cache-phasercachecachemanager}


**说明:**

缓存管理员的例子 。

缓存管理器是一个全球性系统,负责缓存,访问和释放外部游戏资源.


> 源码：[src/core/Game.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L173)  
引入版本：3.0.0


---

### canvas {#canvas}

#### canvas: HTMLCanvasElement {#canvas-htmlcanvaselement}


**说明:**

引用 Phaser 用于渲染游戏的 HTML 坎瓦斯 元素。 此选项由 Phaser 自动创建, 除非您在游戏配置中提供 `canvas` 属性 。


> 源码：[src/core/Game.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L98)  
引入版本：3.0.0


---

### config {#config}

#### config: [Phaser.Core.Config](/api/class/core-config) {#config-phasercoreconfig}


**说明:**

解析游戏配置对象 。

此对象内存储的值是只读的,在运行时不应更改.


> 源码：[src/core/Game.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L63)  
引入版本：3.0.0


---

### context {#context}

#### context: CanvasRenderingContext2D, WebGLRenderingContext {#context-canvasrenderingcontext2d-webglrenderingcontext}


**说明:**

引用属于 Canvas Elements 的渲染语境。 如果游戏运行在 Canvas 下, 则将使用 2d Canvas 渲染语境 。 如果游戏运行在下方 WebGL 这将是一个 WebGL 渲染上下文。 此上下文由 Phaser 除非你提供 `context` 属性在您的游戏配置中。


> 源码：[src/core/Game.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L109)  
引入版本：3.0.0


---

### device {#device}

#### device: [Phaser.DeviceConf](/api/typedef/phaser#deviceconf) {#device-phaserdeviceconf}


**说明:**

设备检查员的参考信息

包含运行此游戏的设备信息, 如 OS, 浏览器供应商和特性支持 。 被各种系统用于确定能力和代码路径 。


> 源码：[src/core/Game.js#L217](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L217)  
引入版本：3.0.0


---

### domContainer {#domContainer}

#### domContainer: HTMLDivElement {#domcontainer-htmldivelement}


**说明:**

用于 DOM 元素容器的 HTML 元素。

只有在游戏配置中`createDOMContainer`是`true`(默认情况下是`false`),并且提供母元素将Phaser游戏插入到游戏内部时才设定.

详见 DOM 元素游戏对象.


> 源码：[src/core/Game.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L84)  
引入版本：3.17.0


---

### events {#events}

#### events: [Phaser.Events.EventEmitter](/api/class/events-eventemitter) {#events-phasereventseventemitter}


**说明:**

用于播放全球系统游戏级活动的事件信息。


> 源码：[src/core/Game.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L142)  
引入版本：3.0.0


---

### hasFocus {#hasFocus}

#### hasFocus: boolean {#hasfocus-boolean}


**说明:**

游戏运行中的窗口是否具有焦点? 此窗口由可见汉德勒修改 。


> 源码：[src/core/Game.js#L313](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L313)  
引入版本：3.9.0


---

### input {#input}

#### input: [Phaser.Input.InputManager](/api/class/input-inputmanager) {#input-phaserinputinputmanager}


**说明:**

输入管理器的例子 。

输入管理器是一个负责捕捉浏览器级输入事件的全局系统.


> 源码：[src/core/Game.js#L195](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L195)  
引入版本：3.0.0


---

### isBooted {#isBooted}

#### isBooted: boolean {#isbooted-boolean}


**说明:**

显示此 Game 实例何时完成启动进程的旗帜 。


> 源码：[src/core/Game.js#L122](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L122)  
引入版本：3.0.0


---

### isPaused {#isPaused}

#### isPaused: boolean {#ispaused-boolean}


**说明:**

游戏是否目前暂停 ? 这将阻止所有内容更新, 除了 `TimeStep` 和相关的 Arequest AnimationFrame 或 setTimeout 。 这些会继续踩踏, 但核心游戏步骤将被跳过 。


> 源码：[src/core/Game.js#L324](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L324)  
引入版本：3.60.0


---

### isRunning {#isRunning}

#### isRunning: boolean {#isrunning-boolean}


**说明:**

显示此游戏当前是否运行游戏步骤的旗帜 。


> 源码：[src/core/Game.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L132)  
引入版本：3.0.0


---

### loop {#loop}

#### loop: [Phaser.Core.TimeStep](/api/class/core-timestep) {#loop-phasercoretimestep}


**说明:**

时间步法的一个例子。

"时间步"是一个全球性系统,负责设置和响应浏览器帧事件,处理它们和计算三角洲值,然后自动调用游戏步骤.


> 源码：[src/core/Game.js#L258](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L258)  
引入版本：3.0.0


---

### plugins {#plugins}

#### plugins: [Phaser.Plugins.PluginManager](/api/class/plugins-pluginmanager) {#plugins-phaserpluginspluginmanager}


**说明:**

插件管理器的示例 。

插件管理器是一个全局系统,允许插件自己用它注册,然后可以根据需要将这些插件安装到Scenes中.


> 源码：[src/core/Game.js#L270](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L270)  
引入版本：3.0.0


---

### registry {#registry}

#### registry: [Phaser.Data.DataManager](/api/class/data-datamanager) {#registry-phaserdatadatamanager}


**说明:**

数据管理器的一个例子。 这是一个全局管理器, 可以从任意场景中获取, 允许您分享和交换自己的游戏级别数据或事件, 而无需使用内部事件系统 。


> 源码：[src/core/Game.js#L184](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L184)  
引入版本：3.0.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer), [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrenderercanvascanvasrenderer-phaserrendererwebglwebglrenderer}


**说明:**

参考本游戏使用的Canvas或WebGL 渲染器.


> 源码：[src/core/Game.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L75)  
引入版本：3.0.0


---

### scale {#scale}

#### scale: [Phaser.Scale.ScaleManager](/api/class/scale-scalemanager) {#scale-phaserscalescalemanager}


**说明:**

缩放管理器的例子 。

缩放管理器是一个全球性系统,负责处理游戏画布的缩放.


> 源码：[src/core/Game.js#L229](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L229)  
引入版本：3.16.0


---

### scene {#scene}

#### scene: [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) {#scene-phaserscenesscenemanager}


**说明:**

现场经理的一个例子

场景管理器是一个全球系统,负责在您的游戏中创建,修改和更新场景.


> 源码：[src/core/Game.js#L206](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L206)  
引入版本：3.0.0


---

### sound {#sound}

#### sound: [Phaser.Sound.NoAudioSoundManager](/api/class/sound-noaudiosoundmanager), [Phaser.Sound.HTML5AudioSoundManager](/api/class/sound-html5audiosoundmanager), [Phaser.Sound.WebAudioSoundManager](/api/class/sound-webaudiosoundmanager) {#sound-phasersoundnoaudiosoundmanager-phasersoundhtml5audiosoundmanager-phasersoundwebaudiosoundmanager}


**说明:**

基地声音管理器的例子.

声音管理器是一个全球系统,负责对游戏中的所有音频进行回放和更新.

您可以通过浏览网页包装 `FEATURE_SOUND` 旗来禁用将声音管理器包含在您的构建中 。


> 源码：[src/core/Game.js#L240](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L240)  
引入版本：3.0.0


---

### textures {#textures}

#### textures: [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) {#textures-phasertexturestexturemanager}


**说明:**

纹理经理的一个例子。

纹理管理器是一个全局系统,负责管理您游戏使用的所有纹理.


> 源码：[src/core/Game.js#L162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L162)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### boot {#boot}

#### \<instance> boot() {#instance-boot}


**说明:**

当 DOM 准备好时, 这种方法会自动被调用。 它负责创建渲染器, 显示调试头, 将游戏布布加入 DOM 并释放“ 启动” 事件。 它会从基系统中听到“ 准备” 事件, 一旦收到, 就会调用 `Game.start` 。


**访问权限:** 受保护


**触发事件:** [Phaser.Core.Events#event:BOOT](/api/event/core-events#boot)


> 源码：[src/core/Game.js#L339](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L339)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy(removeCanvas, [noReturn]) {#instance-destroyremovecanvas-noreturn}


**说明:**

标出此游戏实例, 以表示需要销毁在 _ next 帧_ 上, 使此操作成为同步操作 。

它将等待当前框架完成,然后在内部拨打`runDestroy`.

如果您需要回应游戏的最终毁灭,请听好`DESTROY`事件.

如果您** 不需要** 再次在同一网页上运行 Phaser 您可以将 `noReturn` 参数设置为 `true` , 并且它将释放核心 Phaser 插件所持有的内存。 如果您需要在同一页上创建另一个游戏实例, 请将此保留为 `false` 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| removeCanvas | boolean | 否 |  | 如果您希望将主帆布元素从 DOM 中移除, 或 `false` 将其留在原位, 请设定为 `true` 。 |
| noReturn | boolean | 是 | false | 如果 `true` 全部核心 Phaser 插件被销毁。 如果您这样做, 您无法在同一网页上创建另一个 Phaser 实例 。 |


**触发事件:** [Phaser.Core.Events#event:DESTROY](/api/event/core-events#destroy)


> 源码：[src/core/Game.js#L695](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L695)  
引入版本：3.0.0


---

### getFrame {#getFrame}

#### \<instance> getFrame() {#instance-getframe}


**说明:**

返回当前游戏框架。

游戏开始运行时,每一次请求动画框架,或设定超时,火力时,帧都会递增.


**返回值:** number - 现游戏框.


> 源码：[src/core/Game.js#L667](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L667)  
引入版本：3.16.0


---

### getTime {#getTime}

#### \<instance> getTime() {#instance-gettime}


**说明:**

返回当前游戏步骤开始的时间, 以 `performance.now` 为基础 。


**返回值:** number - 当前的游戏时间戳.


> 源码：[src/core/Game.js#L682](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L682)  
引入版本：3.16.0


---

### headlessStep {#headlessStep}

#### \<instance> headlessStep(time, delta) {#instance-headlesssteptime-delta}


**说明:**

仅用于HEAELES渲染器的游戏步法特殊版本.

主游戏步骤。 由时间步骤自动调用, 每浏览器框架一次( 通常是因请求动画框架, 或者在非常旧的浏览器上设置超时) 。

该步骤将首先更新全球管理人员,然后通过场景管理器依次更新每个场景。

这个过程会发出`prerender`和`postrender`事件,尽管实际上没有显示任何东西.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


**触发事件:** [Phaser.Core.Events#event:PRE_RENDER](/api/event/core-events#pre_render), [Phaser.Core.Events#event:POST_RENDER](/api/event/core-events#post_render)


> 源码：[src/core/Game.js#L505](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L505)  
引入版本：3.2.0


---

### onBlur {#onBlur}

#### \<instance> onBlur() {#instance-onblur}


**说明:**

由可见度处理器自动调用。 这将将主循环设置为“ blured” 状态, 从而暂停它 。


**访问权限:** 受保护


> 源码：[src/core/Game.js#L637](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L637)  
引入版本：3.0.0


---

### onFocus {#onFocus}

#### \<instance> onFocus() {#instance-onfocus}


**说明:**

由可见度处理器自动调用。 这将将主循环设置为“ 聚焦” 状态, 恢复它 。


**访问权限:** 受保护


> 源码：[src/core/Game.js#L652](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L652)  
引入版本：3.0.0


---

### onHidden {#onHidden}

#### \<instance> onHidden() {#instance-onhidden}


**说明:**

由可见度处理器自动调用。 这将暂停主循环, 然后发出暂停事件 。


**访问权限:** 受保护


**触发事件:** [Phaser.Core.Events#event:PAUSE](/api/event/core-events#pause)


> 源码：[src/core/Game.js#L561](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L561)  
引入版本：3.0.0


---

### onVisible {#onVisible}

#### \<instance> onVisible() {#instance-onvisible}


**说明:**

由可见度处理器自动调用。 这将恢复主循环, 然后发出一个恢复事件 。


**访问权限:** 受保护


**触发事件:** [Phaser.Core.Events#event:RESUME](/api/event/core-events#resume)


> 源码：[src/core/Game.js#L600](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L600)  
引入版本：3.0.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

这将暂停整个游戏,并发布一个`PAUSE`事件.

Phaser的所有内部系统都会暂停,游戏不会重新发售.

注意它不暂停任何正在飞行的装货者请求。


**触发事件:** [Phaser.Core.Events#event:PAUSE](/api/event/core-events#pause)


> 源码：[src/core/Game.js#L577](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L577)  
引入版本：3.60.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

这将恢复整个游戏,并发布一个`RESUME`事件.

Phaser的所有内部系统都将恢复,游戏将重新开始渲染.


**触发事件:** [Phaser.Core.Events#event:RESUME](/api/event/core-events#resume)


> 源码：[src/core/Game.js#L616](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L616)  
引入版本：3.60.0


---

### start {#start}

#### \<instance> start() {#instance-start}


**说明:**

由 Game. boot 自动调用, 一旦全球系统都完成设置。 此时游戏已准备好启动主循环运行, 也可以启用可见度处理器 。


**访问权限:** 受保护


> 源码：[src/core/Game.js#L401](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L401)  
引入版本：3.0.0


---

### step {#step}

#### \<instance> step(time, delta) {#instance-steptime-delta}


**说明:**

主游戏步骤。 由时间步骤自动调用, 每浏览器框架一次( 通常是因请求动画框架, 或者在非常旧的浏览器上设置超时) 。

该步骤将首先更新全球管理人员,然后通过场景管理器依次更新每个场景。

然后,它通过渲染器将每个场景依次制作。这个过程会显示 `prerender`和 `postrender`事件。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


**触发事件:** [Phaser.Core.Events#event:PRE_STEP](/api/event/core-events#pre_step), [Phaser.Core.Events#event:STEP](/api/event/core-events#step), [Phaser.Core.Events#event:POST_STEP](/api/event/core-events#post_step), [Phaser.Core.Events#event:PRE_RENDER](/api/event/core-events#pre_render), [Phaser.Core.Events#event:POST_RENDER](/api/event/core-events#post_render)


> 源码：[src/core/Game.js#L435](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Game.js#L435)  
引入版本：3.0.0


---

---
