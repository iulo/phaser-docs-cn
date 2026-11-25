# Phaser.Core.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/core-events)

Scope: 
static
> 源码：[src/core/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/index.js#L7)  


## 静态函数 {#static-functions}

### BLUR {#BLUR}

#### BLUR {#blur}


**说明:**

游戏模糊事件.

当游戏实例嵌入的窗口进入模糊状态时, 游戏显性处理器会发出此事件。 当窗口失去焦点时, 模糊事件会上升。 如果用户交换标签, 或者如果它们只是将浏览器的焦点移到另一个应用程序, 则会发生这种情况 。


> 源码：[src/core/events/BLUR_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/BLUR_EVENT.js#L7)  
引入版本：3.0.0


---

### BOOT {#BOOT}

#### BOOT {#boot}


**说明:**

游戏靴事件.

本次事件是在 Phaser Game 实例完成启动后发出, 但还没有准备好启动。 全球系统使用此事件来了解何时设置自己, 并按要求发送自己的 `ready` 事件 。


> 源码：[src/core/events/BOOT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/BOOT_EVENT.js#L7)  
引入版本：3.0.0


---

### CONTEXT_LOST {#CONTEXT_LOST}

#### CONTEXT_LOST {#context_lost}


**说明:**

游戏背景失落事件.

如果使用 WebGL 渲染器时, 游戏会发出此事件, 它会遇到浏览器上下文丢失的 WebGL 事件 。

渲染器停止所有渲染, 发生后无法恢复 。


> 源码：[src/core/events/CONTEXT_LOST_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/CONTEXT_LOST_EVENT.js#L7)  
引入版本：3.19.0


---

### DESTROY {#DESTROY}

#### DESTROY {#destroy}


**说明:**

游戏毁灭事件.

当游戏实例被告知要毁灭自己时, 将会发出此事件。 许多内部系统都会听此事件以澄清自己。 自定义插件和游戏代码也应该这样做 。


> 源码：[src/core/events/DESTROY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/DESTROY_EVENT.js#L7)  
引入版本：3.0.0


---

### FOCUS {#FOCUS}

#### FOCUS {#focus}


**说明:**

游戏焦点事件.

当游戏实例嵌入的窗口进入焦点状态时,此事件由游戏显性处理器发出。 当窗口重现焦点时, 焦点事件会上升, 因为它先前已经丢失 。


> 源码：[src/core/events/FOCUS_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/FOCUS_EVENT.js#L7)  
引入版本：3.0.0


---

### HIDDEN {#HIDDEN}

#### HIDDEN {#hidden}


**说明:**

游戏隐藏事件.

当游戏实例嵌入的文档进入隐藏状态时,此事件由游戏可见度处理器发出。 只有支持可见度 API 的浏览器才会导致此事件被释放 。

在大多数现代浏览器中,当文档进入隐藏状态时,控制主游戏循环的"请求动画框架"和setTimeout会自动暂停。无法阻止这种情况的发生。如果暂停是一个问题(即多人游戏),则这是您游戏在自己的代码中应该说明的问题。


> 源码：[src/core/events/HIDDEN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/HIDDEN_EVENT.js#L7)  
引入版本：3.0.0


---

### PAUSE {#PAUSE}

#### PAUSE {#pause}


**说明:**

游戏暂停事件.

此事件在游戏循环进入暂停状态时发出,通常由于可见度处理器.


> 源码：[src/core/events/PAUSE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/PAUSE_EVENT.js#L7)  
引入版本：3.0.0


---

### POST_RENDER {#POST_RENDER}

#### POST_RENDER {#post_render}


**说明:**

游戏后渲染事件.

本次事件在渲染过程结束时即刻发出.

每个场景都会在本次事件发射时渲染并被引到画布上。 在下一个游戏步骤开始前, 使用它进行最后一分钟的处理 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) \| [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 参考 Game 实例正在使用的当前渲染器 。 |


> 源码：[src/core/events/POST_RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/POST_RENDER_EVENT.js#L7)  
引入版本：3.0.0


---

### POST_STEP {#POST_STEP}

#### POST_STEP {#post_step}


**说明:**

游戏后步事件.

此事件是在场景管理器更新后发送的。 将需要先完成渲染的插件或系统插入其中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/core/events/POST_STEP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/POST_STEP_EVENT.js#L7)  
引入版本：3.0.0


---

### PRE_RENDER {#PRE_RENDER}

#### PRE_RENDER {#pre_render}


**说明:**

游戏预渲染事件.

本次事件是在任何幕后人物开始做出行动之前立即发出的。

渲染器已经初始化了这个帧,自己清理,准备接收Scases的渲染,但实际上它还没有画出任何图.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) \| [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 参考 Game 实例正在使用的当前渲染器 。 |


> 源码：[src/core/events/PRE_RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/PRE_RENDER_EVENT.js#L7)  
引入版本：3.0.0


---

### PRE_STEP {#PRE_STEP}

#### PRE_STEP {#pre_step}


**说明:**

游戏预赛事件.

此事件在游戏主步开始前发出。 游戏周期的这时, 还没有发生任何场景更新。 需要从插件或系统插入, 以在场景管理器之前更新 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/core/events/PRE_STEP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/PRE_STEP_EVENT.js#L7)  
引入版本：3.0.0


---

### READY {#READY}

#### READY {#ready}


**说明:**

游戏准备事件.

本次事件在Phaser游戏实例完成启动后发出,纹理管理器已经完全准备就绪,所有本地系统现在都能启动.


> 源码：[src/core/events/READY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/READY_EVENT.js#L7)  
引入版本：3.0.0


---

### RESUME {#RESUME}

#### RESUME {#resume}


**说明:**

游戏复出事件.

当游戏循环离开暂停状态并恢复运行时,此事件会被发送.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pauseDuration | number | 否 | 游戏暂停的时间, 以ms计, 如果使用QQlink Phaser.Game#resume} 则使用 0 。 |


> 源码：[src/core/events/RESUME_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/RESUME_EVENT.js#L7)  
引入版本：3.0.0


---

### STEP {#STEP}

#### STEP {#step}


**说明:**

游戏步进事件.

此事件在游戏预演后和场景管理器步骤前发出. Hook into it 从插件或系统上找到,需要更新的时间在场景管理器之前,但在核心系统之后.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/core/events/STEP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/STEP_EVENT.js#L7)  
引入版本：3.0.0


---

### SYSTEM_READY {#SYSTEM_READY}

#### SYSTEM_READY {#system_ready}


**说明:**

当场景管理器创建了系统场景时,此事件即被发出,其他插件和系统可能用来初始化自己.

此事件仅由 Game 实例发送一次 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sys | [Phaser.Scenes.Systems](/api/class/scenes-systems) | 否 | 引用了事件发生的场景系统级。 |


> 源码：[src/core/events/SYSTEM_READY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/SYSTEM_READY_EVENT.js#L7)  
引入版本：3.70.0


---

### VISIBLE {#VISIBLE}

#### VISIBLE {#visible}


**说明:**

游戏可见事件.

当游戏实例嵌入的文档进入一个可见状态,之前已被隐藏时,此事件由游戏显性处理器发送.

只有支持可见度 API 的浏览器才会导致此事件被释放 。


> 源码：[src/core/events/VISIBLE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/VISIBLE_EVENT.js#L7)  
引入版本：3.0.0


---

---
