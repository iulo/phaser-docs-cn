# Phaser.Renderer.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/renderer-events)

Scope: 
static
> 源码：[src/renderer/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/index.js#L7)  


## 静态函数 {#static-functions}

### LOSE_WEBGL {#LOSE_WEBGL}

#### LOSE_WEBGL {#lose_webgl}


**说明:**

输掉的WebGL事件。

当 WebGL 上下文丢失时,此事件由 WebGLRenderer 发送 。

上下文可能由于各种原因丢失,比如离开浏览器标签。游戏布景 DOM 对象会发送 `webglcontextlost`。所有 WebGL 资源都被擦除,上下文被重置 。

WebGL虽然丢失,游戏会继续运行,但所有WebGL资源都丢失,无法创建新的资源.

一旦上下文恢复,而渲染器自动恢复状态,渲染器就会发出`RESTORE_WEBGL`事件,此时可以继续.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有 WebGL 上下文的渲染器 |


> 源码：[src/renderer/events/LOSE_WEBGL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/LOSE_WEBGL_EVENT.js#L7)  
引入版本：3.80.0


---

### POST_RENDER {#POST_RENDER}

#### POST_RENDER {#post_render}


**说明:**

后风流事件.

当所有摄像机的渲染完成后, 由渲染器发出, 但还没有拍摄到任何即将拍摄的镜头。


> 源码：[src/renderer/events/POST_RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/POST_RENDER_EVENT.js#L7)  
引入版本：3.50.0


---

### PRE_RENDER {#PRE_RENDER}

#### PRE_RENDER {#pre_render}


**说明:**

预展事件.

此事件由 Phaser 渲染器发送。 此事发生在渲染过程的开始, 上下文被清除后, 剪刀被启用( 只使用 WebGL) , 所有内容都已经准备好渲染 。


> 源码：[src/renderer/events/PRE_RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/PRE_RENDER_EVENT.js#L7)  
引入版本：3.50.0


---

### PRE_RENDER_CLEAR {#PRE_RENDER_CLEAR}

#### PRE_RENDER_CLEAR {#pre_render_clear}


**说明:**

预展清场事件.

此事件由 Phaser 渲染器发送。 它发生在渲染步骤的开始, 在调用 WebGL gl. clear 函数之前。 这样您就可以按要求切换 `config.clearBeforeRender` 属性, 以便精确控制渲染过程中的画布清除时 。

听听场内的声音 用`this.renderer.events.on('prerenderclear', listener)`

切除器和掩码堆栈清除前, 一定要知道这个事件叫做_。 这意味着您不应该使用这个事件来修改切除器或掩码。 相反, 请使用 `prerender`z 事件来进行此修改 。

如果使用 Canvas 渲染器, 这项活动会在画布清除之前发出, 但上下文 globalAlpha 和变换被重置 。


> 源码：[src/renderer/events/PRE_RENDER_CLEAR_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/PRE_RENDER_CLEAR_EVENT.js#L7)  
引入版本：3.85.0


---

### RENDER {#RENDER}

#### RENDER {#render}


**说明:**

伦德事件.

本次活动由Phaser渲染器为每场场景的每台相机发出.

在现场任何儿童被送走之前,即已发出。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 场景正在被制造 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 场景摄像机正在被拍摄 |


> 源码：[src/renderer/events/RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/RENDER_EVENT.js#L7)  
引入版本：3.50.0


---

### RESIZE {#RESIZE}

#### RESIZE {#resize}


**说明:**

灵丹徒调整规模事件.

此事件在调整大小时由Phaser渲染器发送,通常由于缩放管理器重排大小.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 变形器的新宽度 。 |
| height | number | 否 | 造物器的新高度. |


> 源码：[src/renderer/events/RESIZE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/RESIZE_EVENT.js#L7)  
引入版本：3.50.0


---

### RESTORE_WEBGL {#RESTORE_WEBGL}

#### RESTORE_WEBGL {#restore_webgl}


**说明:**

恢复WebGL事件。

本次事件由WebGLRender在恢复WebGL上下文时发送.

它在全部 WebGL 资源被重新创建后被发送。 大多数资源应该自动返回, 但是您需要重新绘制绑定 GPU 的动态纹理 。 请听此事件, 以知道您何时可以安全完成 。

上下文可能由于各种原因丢失,比如离开浏览器标签。游戏布景 DOM 对象会发送 `webglcontextlost`。所有 WebGL 资源都被擦除,上下文被重置 。

一旦恢复上下文, 画布会发送 `webglcontextrestored`. Phaser 使用此程序来重新创建必要的资源 。 请等待 Phaser 发送 `RESTORE_WEBGL` 事件, 然后再重新创建您自己的资源 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有 WebGL 上下文的渲染器 |


> 源码：[src/renderer/events/RESTORE_WEBGL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/RESTORE_WEBGL_EVENT.js#L7)  
引入版本：3.80.0


---

### SET_PARALLEL_TEXTURE_UNITS {#SET_PARALLEL_TEXTURE_UNITS}

#### SET_PARALLEL_TEXTURE_UNITS {#set_parallel_texture_units}


**说明:**

设置平行纹理单位事件 。

此事件由 RenderNodeManager 在启动后设置 `maxParallelTextureUnits` 时发送。 这可以向听众建议由于性能原因应当平行使用的纹理单位数量 。

一般来说,单位数要么是设备上可用的纹理单位数,要么是设备预计与多个纹理单位平行运行时性能不佳的1个.

此次活动的主要消费者是批量制成节点.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| units | number | 否 | 纹理单位的数目已通知。 |


> 源码：[src/renderer/events/SET_PARALLEL_TEXTURE_UNITS_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/events/SET_PARALLEL_TEXTURE_UNITS_EVENT.js#L7)  
引入版本：4.0.0


---

---
