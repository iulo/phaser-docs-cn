# Phaser.Scenes.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/scenes-events)

Scope: 
static
> 源码：[src/scene/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/index.js#L7)  


## 静态函数 {#static-functions}

### ADDED_TO_SCENE {#ADDED_TO_SCENE}

#### ADDED_TO_SCENE {#added_to_scene}


**说明:**

游戏对象添加到场景事件 。

当游戏对象被添加到场景中时,此事件会被发送 。

听听场景用`this.events.on('addedtoscene', listener)`的

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象被添加到场景中 。 |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 游戏对象被添加到的景色 。 |


> 源码：[src/scene/events/ADDED_TO_SCENE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/ADDED_TO_SCENE_EVENT.js#L7)  
引入版本：3.50.0


---

### BOOT {#BOOT}

#### BOOT {#boot}


**说明:**

场景系统靴子事件.

此事件由 Scene 系统启动过程中的 Scene 发送。 主要由 Scene 插件使用 。

听听场景用`this.events.on('boot', listener)`的

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sys | [Phaser.Scenes.Systems](/api/class/scenes-systems) | 否 | 引用了事件发生的场景系统级。 |


> 源码：[src/scene/events/BOOT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/BOOT_EVENT.js#L7)  
引入版本：3.0.0


---

### CREATE {#CREATE}

#### CREATE {#create}


**说明:**

场景创建事件.

此事件由场景管理器创建后由场景发送.

如果场景有 `create` 方法,则此事件将发布 _after_ that has running 。

如果有过渡,此事件将在`TRANSITION_START`事件后发射.

听听场景用`this.events.on('create', listener)`的

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 提到事件发生的场景 |


> 源码：[src/scene/events/CREATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/CREATE_EVENT.js#L7)  
引入版本：3.17.0


---

### DESTROY {#DESTROY}

#### DESTROY {#destroy}


**说明:**

场景系统破坏事件。

此事件由场景系统破坏过程中的场景发送.

听听场景用`this.events.on('destroy', listener)`的

您应该销毁您所在的场景中可能用于此事件处理器的任何资源 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sys | [Phaser.Scenes.Systems](/api/class/scenes-systems) | 否 | 引用了事件发生的场景系统级。 |


> 源码：[src/scene/events/DESTROY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/DESTROY_EVENT.js#L7)  
引入版本：3.0.0


---

### PAUSE {#PAUSE}

#### PAUSE {#pause}


**说明:**

场景系统暂停事件。

此事件由一幕暂停时直接通过`pause`方法发出,或者作为另一幕的动作发出.

听听场景用`this.events.on('pause', listener)`的

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sys | [Phaser.Scenes.Systems](/api/class/scenes-systems) | 否 | 引用了事件发生的场景系统级。 |
| data | any | 是 | 暂停时传递到此场景的可选数据对象 。 |


> 源码：[src/scene/events/PAUSE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/PAUSE_EVENT.js#L7)  
引入版本：3.0.0


---

### POST_UPDATE {#POST_UPDATE}

#### POST_UPDATE {#post_update}


**说明:**

场景系统后更新事件.

此事件由游戏主循环步骤中由场景发送.

场景单步的事件流程如下:

1. [``PRE_UPDATE``](/api/event/scenes-events#pre_update)

2. [``UPDATE``](/api/event/scenes-events#update)

3. 如果存在,则使用 `Scene.update` 方法

4. [``POST_UPDATE``](/api/event/scenes-events#post_update)

5. [``PRE_RENDER``](/api/event/scenes-events#pre_render)

6. [``RENDER``](/api/event/scenes-events#render)

听听场景用`this.events.on('postupdate', listener)`的

场景只有在活动时才会运行其步骤.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/scene/events/POST_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/POST_UPDATE_EVENT.js#L7)  
引入版本：3.0.0


---

### PRE_RENDER {#PRE_RENDER}

#### PRE_RENDER {#pre_render}


**说明:**

场景系统预渲染事件.

此事件由游戏主循环步骤中由场景发送.

场景单步的事件流程如下:

1. [``PRE_UPDATE``](/api/event/scenes-events#pre_update)

2. [``UPDATE``](/api/event/scenes-events#update)

3. 如果存在,则使用 `Scene.update` 方法

4. [``POST_UPDATE``](/api/event/scenes-events#post_update)

5. [``PRE_RENDER``](/api/event/scenes-events#pre_render)

6. [``RENDER``](/api/event/scenes-events#render)

听听现场用`this.events.on('prerender', listener)`的这个事件

场景只有在可见的情况下才会变形.

此事件在选取场景显示列表排序后, 并在渲染场景之前发出 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) \| [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 制造场景的造型者 |


> 源码：[src/scene/events/PRE_RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/PRE_RENDER_EVENT.js#L7)  
引入版本：3.53.0


---

### PRE_UPDATE {#PRE_UPDATE}

#### PRE_UPDATE {#pre_update}


**说明:**

场景系统预更新事件.

此事件由游戏主循环步骤中由场景发送.

场景单步的事件流程如下:

1. [``PRE_UPDATE``](/api/event/scenes-events#pre_update)

2. [``UPDATE``](/api/event/scenes-events#update)

3. 如果存在,则使用 `Scene.update` 方法

4. [``POST_UPDATE``](/api/event/scenes-events#post_update)

5. [``PRE_RENDER``](/api/event/scenes-events#pre_render)

6. [``RENDER``](/api/event/scenes-events#render)

听听场景用`this.events.on('preupdate', listener)`的

场景只有在活动时才会运行其步骤.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/scene/events/PRE_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/PRE_UPDATE_EVENT.js#L7)  
引入版本：3.0.0


---

### READY {#READY}

#### READY {#ready}


**说明:**

场景系统准备事件

此事件由 Scene 系统启动过程中的 Scene 发送。 到此时, Scene 已完全激活并渲染。 此事件是供您的游戏代码使用, 因为所有插件都响应了先前的“ start” 事件 。

听听场景用`this.events.on('ready', listener)`的

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sys | [Phaser.Scenes.Systems](/api/class/scenes-systems) | 否 | 引用了事件发生的场景系统级。 |
| data | any | 是 | 启动时传递给此场景的可选数据对象 。 |


> 源码：[src/scene/events/READY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/READY_EVENT.js#L7)  
引入版本：3.0.0


---

### REMOVED_FROM_SCENE {#REMOVED_FROM_SCENE}

#### REMOVED_FROM_SCENE {#removed_from_scene}


**说明:**

游戏对象从场景事件中移除 。

当游戏对象从场景中移除时,此事件会被发送 。

听听场景用`this.events.on('removedfromscene', listener)`的

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象被删除于场景 。 |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 游戏对象被删除的场景 。 |


> 源码：[src/scene/events/REMOVED_FROM_SCENE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/REMOVED_FROM_SCENE_EVENT.js#L7)  
引入版本：3.50.0


---

### RENDER {#RENDER}

#### RENDER {#render}


**说明:**

场景系统变迁事件.

此事件由游戏主循环步骤中由场景发送.

场景单步的事件流程如下:

1. [``PRE_UPDATE``](/api/event/scenes-events#pre_update)

2. [``UPDATE``](/api/event/scenes-events#update)

3. 如果存在,则使用 `Scene.update` 方法

4. [``POST_UPDATE``](/api/event/scenes-events#post_update)

5. [``PRE_RENDER``](/api/event/scenes-events#pre_render)

6. [``RENDER``](/api/event/scenes-events#render)

听听场景用`this.events.on('render', listener)`的

场景只有在可见的情况下才会变形.

等事件发出 场景就已经发出来了

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) \| [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 制造场景的造型者 |


> 源码：[src/scene/events/RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/RENDER_EVENT.js#L7)  
引入版本：3.0.0


---

### RESUME {#RESUME}

#### RESUME {#resume}


**说明:**

场景系统复出事件.

本次事件由场景在从暂停状态恢复时直接通过`resume`方法发出,或者作为来自另一个场景的动作发出.

听听场景用`this.events.on('resume', listener)`的

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sys | [Phaser.Scenes.Systems](/api/class/scenes-systems) | 否 | 引用了事件发生的场景系统级。 |
| data | any | 是 | 一个可选的数据对象,在恢复时被传递到此场景. |


> 源码：[src/scene/events/RESUME_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/RESUME_EVENT.js#L7)  
引入版本：3.0.0


---

### SHUTDOWN {#SHUTDOWN}

#### SHUTDOWN {#shutdown}


**说明:**

场景系统关闭事件。

本次事件由场景系统关闭过程中的场景发送.

听听场景用`this.events.on('shutdown', listener)`的

您应该释放您所在的场景在此事件处理器中可能使用的任何资源, 前提是场景可能随时再次活动。 关闭场景不会“ 损坏 ” , 但它目前根本没有活动 。 使用 [``DESTROY``](/api/event/scenes-events#destroy) 事件来完全清除资源 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sys | [Phaser.Scenes.Systems](/api/class/scenes-systems) | 否 | 引用了事件发生的场景系统级。 |
| data | any | 是 | 关闭时传递给此场景的可选数据对象 。 |


> 源码：[src/scene/events/SHUTDOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/SHUTDOWN_EVENT.js#L7)  
引入版本：3.0.0


---

### SLEEP {#SLEEP}

#### SLEEP {#sleep}


**说明:**

场景系统睡眠事件.

本次事件在送入睡眠时由场景发出,或者直接通过`sleep`方法发出,或者作为来自另一个场景的动作发出.

听听场景用`this.events.on('sleep', listener)`的

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sys | [Phaser.Scenes.Systems](/api/class/scenes-systems) | 否 | 引用了事件发生的场景系统级。 |
| data | any | 是 | 被发送到睡眠时传递到此场景的可选数据对象. |


> 源码：[src/scene/events/SLEEP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/SLEEP_EVENT.js#L7)  
引入版本：3.0.0


---

### START {#START}

#### START {#start}


**说明:**

场景系统启动事件.

此事件由 Scene 系统启动过程中的 Scene 发送。 主要由 Scene 插件使用 。

听听场景用`this.events.on('start', listener)`的

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sys | [Phaser.Scenes.Systems](/api/class/scenes-systems) | 否 | 引用了事件发生的场景系统级。 |


> 源码：[src/scene/events/START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/START_EVENT.js#L7)  
引入版本：3.0.0


---

### TRANSITION_COMPLETE {#TRANSITION_COMPLETE}

#### TRANSITION_COMPLETE {#transition_complete}


**说明:**

场景过渡完成事件.

本次活动由过渡目标场景发出.

转换过程完成时发生, 持续时间等于或超过转换时间 。

听听场景用`this.events.on('transitioncomplete', listener)`的

场景过渡事件流程如下:

1. [``TRANSITION_OUT``](/api/event/scenes-events#transition_out) - 启动过渡的场景将释放出这个事件.

2. [``TRANSITION_INIT``](/api/namespace/scenes-events#transition_init) - 目标场景会发出这个事件,如果它有`init`的方法.

3. [``TRANSITION_START``](/api/namespace/scenes-events#transition_start) - 目标场景将在它的`create`方法被称作,或.

4. [``TRANSITION_WAKE``](/api/event/scenes-events#transition_wake) - 目标场景会释放出这个事件,如果它睡着了,并且已经被唤醒以过渡到.

5. [``TRANSITION_COMPLETE``](/api/event/scenes-events#transition_complete) - 目标场景将在过渡结束后释放此事件.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 过渡完成的场景 。 |


> 源码：[src/scene/events/TRANSITION_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/TRANSITION_COMPLETE_EVENT.js#L7)  
引入版本：3.5.0


---

### TRANSITION_INIT {#TRANSITION_INIT}

#### TRANSITION_INIT {#transition_init}


**说明:**

场景过渡事件

本次活动由过渡目标场景发出.

它在`Scene.init`方法被调用后立即发生。 如果场景没有`init`方法, 此事件不会被发送 。

听听场景用`this.events.on('transitioninit', listener)`的

场景过渡事件流程如下:

1. [``TRANSITION_OUT``](/api/event/scenes-events#transition_out) - 启动过渡的场景将释放出这个事件.

2. [``TRANSITION_INIT``](/api/namespace/scenes-events#transition_init) - 目标场景会发出这个事件,如果它有`init`的方法.

3. [``TRANSITION_START``](/api/namespace/scenes-events#transition_start) - 目标场景将在它的`create`方法被称作,或.

4. [``TRANSITION_WAKE``](/api/event/scenes-events#transition_wake) - 目标场景会释放出这个事件,如果它睡着了,并且已经被唤醒以过渡到.

5. [``TRANSITION_COMPLETE``](/api/event/scenes-events#transition_complete) - 目标场景将在过渡结束后释放此事件.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| from | [Phaser.Scene](/api/class/scene) | 否 | 参考正在过渡的场景。 |
| duration | number | 否 | 过渡期以毫秒计。 |


> 源码：[src/scene/events/TRANSITION_INIT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/TRANSITION_INIT_EVENT.js#L7)  
引入版本：3.5.0


---

### TRANSITION_OUT {#TRANSITION_OUT}

#### TRANSITION_OUT {#transition_out}


**说明:**

场景过渡事件。

此事件在启动向另一个场景的过渡时,由场景发送.

听听场景用`this.events.on('transitionout', listener)`的

场景过渡事件流程如下:

1. [``TRANSITION_OUT``](/api/event/scenes-events#transition_out) - 启动过渡的场景将释放出这个事件.

2. [``TRANSITION_INIT``](/api/namespace/scenes-events#transition_init) - 目标场景会发出这个事件,如果它有`init`的方法.

3. [``TRANSITION_START``](/api/namespace/scenes-events#transition_start) - 目标场景将在它的`create`方法被称作,或.

4. [``TRANSITION_WAKE``](/api/event/scenes-events#transition_wake) - 目标场景会释放出这个事件,如果它睡着了,并且已经被唤醒以过渡到.

5. [``TRANSITION_COMPLETE``](/api/event/scenes-events#transition_complete) - 目标场景将在过渡结束后释放此事件.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Scene](/api/class/scene) | 否 | 参考正在向外过渡的场景. |
| duration | number | 否 | 过渡期以毫秒计。 |


> 源码：[src/scene/events/TRANSITION_OUT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/TRANSITION_OUT_EVENT.js#L7)  
引入版本：3.5.0


---

### TRANSITION_START {#TRANSITION_START}

#### TRANSITION_START {#transition_start}


**说明:**

场景过渡启动事件 。

本次事件是由过渡中的目标场景发出的,只有当该场景没有睡着时.

它在`Scene.create`方法被调用后立即发生。 如果场景没有`create`方法, 无论如何,此事件都会被发送 。

如果目标场景在睡觉 那么[``TRANSITION_WAKE``](/api/event/scenes-events#transition_wake)事件就被发送 而不是这个事件。

听听场景用`this.events.on('transitionstart', listener)`的

场景过渡事件流程如下:

1. [``TRANSITION_OUT``](/api/event/scenes-events#transition_out) - 启动过渡的场景将释放出这个事件.

2. [``TRANSITION_INIT``](/api/namespace/scenes-events#transition_init) - 目标场景会发出这个事件,如果它有`init`的方法.

3. [``TRANSITION_START``](/api/namespace/scenes-events#transition_start) - 目标场景将在它的`create`方法被称作,或.

4. [``TRANSITION_WAKE``](/api/event/scenes-events#transition_wake) - 目标场景会释放出这个事件,如果它睡着了,并且已经被唤醒以过渡到.

5. [``TRANSITION_COMPLETE``](/api/event/scenes-events#transition_complete) - 目标场景将在过渡结束后释放此事件.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| from | [Phaser.Scene](/api/class/scene) | 否 | 参考正在过渡的场景。 |
| duration | number | 否 | 过渡期以毫秒计。 |


> 源码：[src/scene/events/TRANSITION_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/TRANSITION_START_EVENT.js#L7)  
引入版本：3.5.0


---

### TRANSITION_WAKE {#TRANSITION_WAKE}

#### TRANSITION_WAKE {#transition_wake}


**说明:**

场景过渡的醒悟事件.

本次事件是由过渡的目标场景发出的, 只有当过渡开始前该场景已经睡着。 如果该场景没有睡着, [``TRANSITION_START``](/api/event/scenes-events#transition_start)事件将被发送到此位置 。

听听场景用`this.events.on('transitionwake', listener)`的

场景过渡事件流程如下:

1. [``TRANSITION_OUT``](/api/event/scenes-events#transition_out) - 启动过渡的场景将释放出这个事件.

2. [``TRANSITION_INIT``](/api/namespace/scenes-events#transition_init) - 目标场景会发出这个事件,如果它有`init`的方法.

3. [``TRANSITION_START``](/api/namespace/scenes-events#transition_start) - 目标场景将在它的`create`方法被称作,或.

4. [``TRANSITION_WAKE``](/api/event/scenes-events#transition_wake) - 目标场景会释放出这个事件,如果它睡着了,并且已经被唤醒以过渡到.

5. [``TRANSITION_COMPLETE``](/api/event/scenes-events#transition_complete) - 目标场景将在过渡结束后释放此事件.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| from | [Phaser.Scene](/api/class/scene) | 否 | 参考正在过渡的场景。 |
| duration | number | 否 | 过渡期以毫秒计。 |


> 源码：[src/scene/events/TRANSITION_WAKE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/TRANSITION_WAKE_EVENT.js#L7)  
引入版本：3.5.0


---

### UPDATE {#UPDATE}

#### UPDATE {#update}


**说明:**

场景系统更新事件.

此事件由游戏主循环步骤中由场景发送.

场景单步的事件流程如下:

1. [``PRE_UPDATE``](/api/event/scenes-events#pre_update)

2. [``UPDATE``](/api/event/scenes-events#update)

3. `Scene.update`方法被称作,如果它存在,而场景处于运行状态,否则这个被跳过.

4. [``POST_UPDATE``](/api/event/scenes-events#post_update)

5. [``PRE_RENDER``](/api/event/scenes-events#pre_render)

6. [``RENDER``](/api/event/scenes-events#render)

听听场景用`this.events.on('update', listener)`的

场景只有在活动时才会运行其步骤.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/scene/events/UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/UPDATE_EVENT.js#L7)  
引入版本：3.0.0


---

### WAKE {#WAKE}

#### WAKE {#wake}


**说明:**

场景系统事件

本次事件由场景在睡眠中醒过来时直接通过`wake`方法发出,或者作为来自另一场景的动作.

听听场景用`this.events.on('wake', listener)`的

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sys | [Phaser.Scenes.Systems](/api/class/scenes-systems) | 否 | 引用了事件发生的场景系统级。 |
| data | any | 是 | 醒悟时传递给这个场景的可选数据对象. |


> 源码：[src/scene/events/WAKE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/events/WAKE_EVENT.js#L7)  
引入版本：3.0.0


---

---
