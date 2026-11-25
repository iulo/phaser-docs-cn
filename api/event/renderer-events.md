# Renderer.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/renderer-events)

## LOSE_WEBGL {#lose_webgl}


**说明:** 输掉的WebGL事件。

当 WebGL 上下文时,此事件由 WebGLRender 发送
丢失。

背景可能由于各种原因丢失,比如离开浏览器标签.
游戏画布 DOM 对象会发送 `webglcontextlost`.
全部WebGL资源被擦除,上下文被重置.

WebGL丢失的同时,游戏将继续运行,但所有WebGL资源
失去,而新的则无法创建。

上下文恢复后, 渲染器自动恢复
国家, 制造者将发出一个 `RESTORE_WEBGL` 那时,
继续是安全的。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有 WebGL 上下文的渲染器 |

**Member of:** [Phaser.Renderer.Events](/api/namespace/renderer-events)
> 源码：[src/renderer/events/LOSE_WEBGL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/LOSE_WEBGL_EVENT.js#L7)  
引入版本：3.80.0

## POST_RENDER {#post_render}


**说明:** 后风流事件.

本次活动由制作者发出 当所有渲染,所有摄像机在所有的镜头,
已经写好了,但在拍完任何待发的快照之前。

**Member of:** [Phaser.Renderer.Events](/api/namespace/renderer-events)
> 源码：[src/renderer/events/POST_RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/POST_RENDER_EVENT.js#L7)  
引入版本：3.50.0

## PRE_RENDER_CLEAR {#pre_render_clear}


**说明:** 预展清场事件.

此事件由 Phaser 渲染器发送。 它发生在渲染步骤的开始, 也就是在
已调用 WebGL gl. clear 函数。 这样您就可以切换 `config.clearBeforeRender` 属性
以精细控制在渲染过程中清除帆布。

听听场内的声音 用`this.renderer.events.on('prerenderclear', listener)`

了解这个事件非常重要,在剪刀和面具堆被清除之前,叫做_.
这意味着您不应该使用此事件来修改剪刀或面具。 相反, 请使用 `prerender` 事件来修改 。

如果使用 Canvas 渲染器, 此事件会在画布清除前发出, 但在上下文 globalAlpha 之后
并重新设置了变换。

**Member of:** [Phaser.Renderer.Events](/api/namespace/renderer-events)
> 源码：[src/renderer/events/PRE_RENDER_CLEAR_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/PRE_RENDER_CLEAR_EVENT.js#L7)  
引入版本：3.85.0

## PRE_RENDER {#pre_render}


**说明:** 预展事件.

此事件由 Phaser 渲染器发送。 此事发生在渲染的开始
程序,在上下文清除后,剪刀启用(仅WebGL),所有东西都已经
重置准备完成渲染

**Member of:** [Phaser.Renderer.Events](/api/namespace/renderer-events)
> 源码：[src/renderer/events/PRE_RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/PRE_RENDER_EVENT.js#L7)  
引入版本：3.50.0

## RENDER {#render}


**说明:** 伦德事件.

本次活动由Phaser渲染器为每场场景的每台相机发出.

在现场任何儿童被送走之前,即已发出。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 场景正在被制造 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 场景摄像机正在被拍摄 |

**Member of:** [Phaser.Renderer.Events](/api/namespace/renderer-events)
> 源码：[src/renderer/events/RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/RENDER_EVENT.js#L7)  
引入版本：3.50.0

## RESIZE {#resize}


**说明:** 灵丹徒调整规模事件.

本次事件由Phaser渲染器在调整大小时发出,通常因此
缩放管理器的缩放。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 变形器的新宽度 。 |
| height | number | 否 | 造物器的新高度. |

**Member of:** [Phaser.Renderer.Events](/api/namespace/renderer-events)
> 源码：[src/renderer/events/RESIZE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/RESIZE_EVENT.js#L7)  
引入版本：3.50.0

## RESTORE_WEBGL {#restore_webgl}


**说明:** 恢复WebGL事件。

当 WebGL 上下文时,此事件由 WebGLRender 发送
恢复。

它在WebGL资源全部被重新创建后发送.
大部分资源应该自动回来,但需要重新绘制
绑定了 GPU 的动态纹理 。
听听这个事件,知道什么时候你能够安全地做到这一点。

背景可能由于各种原因丢失,比如离开浏览器标签.
游戏画布 DOM 对象会发送 `webglcontextlost`.
全部WebGL资源被擦除,上下文被重置.

恢复上下文后,画布会发出
`webglcontextrestored`. Phaser使用此功能重新创建必要的资源.
请等待 Phaser 在前发送 `RESTORE_WEBGL` 事件
重新创造任何资源。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有 WebGL 上下文的渲染器 |

**Member of:** [Phaser.Renderer.Events](/api/namespace/renderer-events)
> 源码：[src/renderer/events/RESTORE_WEBGL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/RESTORE_WEBGL_EVENT.js#L7)  
引入版本：3.80.0

## SET_PARALLEL_TEXTURE_UNITS {#set_parallel_texture_units}


**说明:** 设置平行纹理单位事件 。

本次活动由当
`maxParallelTextureUnits`是布置在靴子后。
这可以向听者建议纹理单位的数量
出于业绩原因,应同时使用。

一般来说,单位数目是
设备上可用的纹理单元数量,
如果设备预期会使用下列设备进行不良操作:
平行的多个纹理单元。

此次活动的主要消费者是批量制成节点.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| units | number | 否 | 纹理单位的数目已通知。 |

**Member of:** [Phaser.Renderer.Events](/api/namespace/renderer-events)
> 源码：[src/renderer/events/SET_PARALLEL_TEXTURE_UNITS_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/SET_PARALLEL_TEXTURE_UNITS_EVENT.js#L7)  
引入版本：4.0.0

---
