# Core.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/core-events)

## BLUR {#blur}


**说明:** 游戏模糊事件.

当游戏实例嵌入窗口时,此事件由游戏可见度处理器发送
输入模糊状态。当窗口失去焦点时,模糊事件会上升。如果用户互换,则会发生
选项卡,或者如果它们只是将浏览器的焦点转移到另一个应用程序。

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/BLUR_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/BLUR_EVENT.js#L7)  
引入版本：3.0.0

## BOOT {#boot}


**说明:** 游戏靴事件.

本次事件在 Phaser Game 实例完成启动时发出, 但在此之前它已经准备好开始运行 。
全球系统利用这一活动来了解何时可以自行设置,并根据需要自行发送`ready`事件.

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/BOOT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/BOOT_EVENT.js#L7)  
引入版本：3.0.0

## CONTEXT_LOST {#context_lost}


**说明:** 游戏背景失落事件.

如果使用 WebGL 渲染器时, 游戏会发出此事件, 它会遇到浏览器上下文丢失的 WebGL 事件 。

渲染器停止所有渲染, 发生后无法恢复 。

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/CONTEXT_LOST_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/CONTEXT_LOST_EVENT.js#L7)  
引入版本：3.19.0

## DESTROY {#destroy}


**说明:** 游戏毁灭事件.

当游戏实例被告知要毁灭自己时,此事件会被发送.
许多内部系统都听这个事件,以便自己澄清。
自定义插件和游戏代码也应该这样做.

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/DESTROY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/DESTROY_EVENT.js#L7)  
引入版本：3.0.0

## FOCUS {#focus}


**说明:** 游戏焦点事件.

当游戏实例嵌入窗口时,此事件由游戏可见度处理器发送
输入焦点状态。当窗口重现焦点时,焦点事件会上升,因为先前它已经丢失。

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/FOCUS_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/FOCUS_EVENT.js#L7)  
引入版本：3.0.0

## HIDDEN {#hidden}


**说明:** 游戏隐藏事件.

当游戏实例嵌入的文档时,此事件由游戏可见度处理器发送
输入隐藏状态。只有支持可见度 API 的浏览器才会导致此事件被释放 。

在大多数现代浏览器中,当文档进入隐藏状态时,请求动画框架和setTimeout,它
控制主游戏循环, 将自动暂停。 无法阻止这种情况发生 。
如果暂停是一个问题(即多人游戏),则您的游戏应在自己的代码中说明。

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/HIDDEN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/HIDDEN_EVENT.js#L7)  
引入版本：3.0.0

## PAUSE {#pause}


**说明:** 游戏暂停事件.

此事件在游戏循环进入暂停状态时发出,通常由于可见度处理器.

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/PAUSE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/PAUSE_EVENT.js#L7)  
引入版本：3.0.0

## POST_RENDER {#post_render}


**说明:** 游戏后渲染事件.

本次事件在渲染过程结束时即刻发出.

每一个场景都会在这场事件被发射时 被制成并被引到画布上
在下一个游戏步骤开始前,在任何最后一分钟的处理中使用它.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) \| [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 参考 Game 实例正在使用的当前渲染器 。 |

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/POST_RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/POST_RENDER_EVENT.js#L7)  
引入版本：3.0.0

## POST_STEP {#post_step}


**说明:** 游戏后步事件.

此事件在场景管理器更新后发送 。
由插件或系统在渲染开始前需要做一些事情来插入.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/POST_STEP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/POST_STEP_EVENT.js#L7)  
引入版本：3.0.0

## PRE_RENDER {#pre_render}


**说明:** 游戏预渲染事件.

本次事件是在任何幕后人物开始做出行动之前立即发出的。

渲染器已经初始化了这个帧,自己清理,准备接收Scases的渲染,但实际上它还没有画出任何图.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) \| [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 参考 Game 实例正在使用的当前渲染器 。 |

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/PRE_RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/PRE_RENDER_EVENT.js#L7)  
引入版本：3.0.0

## PRE_STEP {#pre_step}


**说明:** 游戏预赛事件.

此事件在游戏主步开始前发送。 到游戏周期的这时, 还没有发生任何场景更新 。
从插件或系统上插入,在场景管理器之前需要更新.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/PRE_STEP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/PRE_STEP_EVENT.js#L7)  
引入版本：3.0.0

## READY {#ready}


**说明:** 游戏准备事件.

当Phaser游戏实例完成启动时, 纹理管理器已经完全准备好了, 本次事件即为发出。
并且所有本地系统现在都能够启动。

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/READY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/READY_EVENT.js#L7)  
引入版本：3.0.0

## RESUME {#resume}


**说明:** 游戏复出事件.

当游戏循环离开暂停状态并恢复运行时,此事件会被发送.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pauseDuration | number | 否 | 游戏暂停的时间, 以ms计, 如果使用QQlink Phaser.Game#resume} 则使用 0 。 |

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/RESUME_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/RESUME_EVENT.js#L7)  
引入版本：3.0.0

## STEP {#step}


**说明:** 游戏步进事件.

此事件在游戏预演后和场景管理器步骤前发送.
从插件或系统上插入,这些插件或系统需要在场景管理器之前更新,但在核心系统完成之后更新.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/STEP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/STEP_EVENT.js#L7)  
引入版本：3.0.0

## SYSTEM_READY {#system_ready}


**说明:** 本次事件是在场景管理器创建系统场景时发出,
哪些其他插件和系统可以用来初始化自己。

此事件仅由 Game 实例发送一次 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sys | [Phaser.Scenes.Systems](/api/class/scenes-systems) | 否 | 引用了事件发生的场景系统级。 |

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/SYSTEM_READY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/SYSTEM_READY_EVENT.js#L7)  
引入版本：3.70.0

## VISIBLE {#visible}


**说明:** 游戏可见事件.

当游戏实例嵌入的文档时,此事件由游戏可见度处理器发送
进入一个可见状态, 之前已被隐藏 。

只有支持可见度 API 的浏览器才会导致此事件被释放 。

**Member of:** [Phaser.Core.Events](/api/namespace/core-events)
> 源码：[src/core/events/VISIBLE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/events/VISIBLE_EVENT.js#L7)  
引入版本：3.0.0

---
