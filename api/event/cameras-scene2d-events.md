# Cameras.Scene2D.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/cameras-scene2d-events)

## DESTROY {#destroy}


**说明:** 毁灭摄像机事件。

由相机管理员破坏时, 由相机实例发出。

通过以下任一方式倾听:

```js
this.cameras.main.on('cameradestroy', () => {});
```

或使用常数,以避免需要记住正确的事件字符串:

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.DESTROY, () => {});
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) | 否 | 被摧毁的摄像机。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/DESTROY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/DESTROY_EVENT.js#L7)  
引入版本：3.0.0

## FADE_IN_COMPLETE {#fade_in_complete}


**说明:** 完全事件时的镜头消失

当效果淡出时, 由相机实例发出此事件 。

用`Camera.on('camerafadeincomplete', listener)`从镜头中听它

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](/api/class/cameras-scene2d-effects-fade) | 否 | 提及效果实例。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/FADE_IN_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/FADE_IN_COMPLETE_EVENT.js#L7)  
引入版本：3.3.0

## FADE_IN_START {#fade_in_start}


**说明:** 镜头在开始事件中消失。

事件由相机实例在“消失效应”开始时发出 。

用`Camera.on('camerafadeinstart', listener)`从镜头中听它

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](/api/class/cameras-scene2d-effects-fade) | 否 | 提及效果实例。 |
| duration | number | 否 | 效期长短. |
| red | number | 否 | 红色通道值 。 |
| green | number | 否 | 绿色通道值 。 |
| blue | number | 否 | 蓝色通道值 。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/FADE_IN_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/FADE_IN_START_EVENT.js#L7)  
引入版本：3.3.0

## FADE_OUT_COMPLETE {#fade_out_complete}


**说明:** 摄像机完全消失事件。

当淡出效应完成时, 由相机实例发出此事件 。

用`Camera.on('camerafadeoutcomplete', listener)`从镜头中听它

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](/api/class/cameras-scene2d-effects-fade) | 否 | 提及效果实例。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/FADE_OUT_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/FADE_OUT_COMPLETE_EVENT.js#L7)  
引入版本：3.3.0

## FADE_OUT_START {#fade_out_start}


**说明:** 相机消失的启动事件。

当淡出效应开始时, 由相机实例发出此事件 。

用`Camera.on('camerafadeoutstart', listener)`从镜头中听它

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](/api/class/cameras-scene2d-effects-fade) | 否 | 提及效果实例。 |
| duration | number | 否 | 效期长短. |
| red | number | 否 | 红色通道值 。 |
| green | number | 否 | 绿色通道值 。 |
| blue | number | 否 | 蓝色通道值 。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/FADE_OUT_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/FADE_OUT_START_EVENT.js#L7)  
引入版本：3.3.0

## FLASH_COMPLETE {#flash_complete}


**说明:** 摄像机闪光事件

当闪光效应完成时, 由相机实例发出此事件 。

通过以下任一方式倾听:

```js
this.cameras.main.on('cameraflashcomplete', () => {});
```

或使用常数,以避免需要记住正确的事件字符串:

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.FLASH_COMPLETE, () => {});
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Flash](/api/class/cameras-scene2d-effects-flash) | 否 | 提及效果实例。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/FLASH_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/FLASH_COMPLETE_EVENT.js#L7)  
引入版本：3.3.0

## FLASH_START {#flash_start}


**说明:** 相机闪光启动事件.

当闪光效应开始时, 由相机实例发出此事件 。

通过以下任一方式倾听:

```js
this.cameras.main.on('cameraflashstart', () => {});
```

或使用常数,以避免需要记住正确的事件字符串:

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.FLASH_START, () => {});
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Flash](/api/class/cameras-scene2d-effects-flash) | 否 | 提及效果实例。 |
| duration | number | 否 | 效期长短. |
| red | number | 否 | 红色通道值 。 |
| green | number | 否 | 绿色通道值 。 |
| blue | number | 否 | 蓝色通道值 。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/FLASH_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/FLASH_START_EVENT.js#L7)  
引入版本：3.3.0

## FOLLOW_UPDATE {#follow_update}


**说明:** 相机跟踪者更新事件.

事件由相机事件发出 当它跟随一个
游戏对象和相机位置已更新,原因是
接下来

从一个镜头中听它使用: `camera.on('followupdate', listener)`。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) | 否 | 发射事件的摄像机。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 相机所跟踪的游戏对象 。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/FOLLOW_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/FOLLOW_UPDATE_EVENT.js#L7)  
引入版本：3.50.0

## PAN_COMPLETE {#pan_complete}


**说明:** 摄像机Pan完整事件。

泛效应完成后, 由相机实例发送此事件 。

通过以下任一方式倾听:

```js
this.cameras.main.on('camerapancomplete', () => {});
```

或使用常数,以避免需要记住正确的事件字符串:

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.PAN_COMPLETE, () => {});
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Pan](/api/class/cameras-scene2d-effects-pan) | 否 | 提及效果实例。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/PAN_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/PAN_COMPLETE_EVENT.js#L7)  
引入版本：3.3.0

## PAN_START {#pan_start}


**说明:** 摄像机潘启动事件.

当泛效应开始时,此事件由相机实例发出 。

通过以下任一方式倾听:

```js
this.cameras.main.on('camerapanstart', () => {});
```

或使用常数,以避免需要记住正确的事件字符串:

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.PAN_START, () => {});
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Pan](/api/class/cameras-scene2d-effects-pan) | 否 | 提及效果实例。 |
| duration | number | 否 | 效期长短. |
| x | number | 否 | 目的地卷轴 X坐标 。 |
| y | number | 否 | 目的地卷轴 y 坐标。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/PAN_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/PAN_START_EVENT.js#L7)  
引入版本：3.3.0

## POST_RENDER {#post_render}


**说明:** 摄像机后渲染事件.

此事件由相机实例发送, 完成渲染后 。
无论是摄像机向纹理还是主画布都发出信号。

从一个镜头中听它使用: `camera.on('postrender', listener)`。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) | 否 | 完成对纹理的摄像机。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/POST_RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/POST_RENDER_EVENT.js#L7)  
引入版本：3.0.0

## PRE_RENDER {#pre_render}


**说明:** 相机预渲染事件.

本次事件在即将发生时由相机实例发出.
只有在摄像机向纹理上显示时才发出信号。

从一个镜头中听它使用: `camera.on('prerender', listener)`。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) | 否 | 即将渲染成纹理的相机. |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/PRE_RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/PRE_RENDER_EVENT.js#L7)  
引入版本：3.0.0

## ROTATE_COMPLETE {#rotate_complete}


**说明:** 摄像机旋转完成事件。

当旋转效果完成时, 由相机实例发送此事件 。

通过以下任一方式倾听:

```js
this.cameras.main.on('camerarotatecomplete', () => {});
```

或使用常数,以避免需要记住正确的事件字符串:

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.ROTATE_COMPLETE, () => {});
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.RotateTo](/api/class/cameras-scene2d-effects-rotateto) | 否 | 提及效果实例。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/ROTATE_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/ROTATE_COMPLETE_EVENT.js#L7)  
引入版本：3.23.0

## ROTATE_START {#rotate_start}


**说明:** 相机旋转启动事件。

当旋转效果开始时, 由相机实例发出此事件 。

通过以下任一方式倾听:

```js
this.cameras.main.on('camerarotatestart', () => {});
```

或使用常数,以避免需要记住正确的事件字符串:

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.ROTATE_START, () => {});
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.RotateTo](/api/class/cameras-scene2d-effects-rotateto) | 否 | 提及效果实例。 |
| duration | number | 否 | 效期长短. |
| destination | number | 否 | 目的地值。 。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/ROTATE_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/ROTATE_START_EVENT.js#L7)  
引入版本：3.23.0

## SHAKE_COMPLETE {#shake_complete}


**说明:** 摄像机震动事件

本次事件由相机实例在摇摆效应完成后发出.

通过以下任一方式倾听:

```js
this.cameras.main.on('camerashakecomplete', () => {});
```

或使用常数,以避免需要记住正确的事件字符串:

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.SHAKE_COMPLETE, () => {});
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Shake](/api/class/cameras-scene2d-effects-shake) | 否 | 提及效果实例。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/SHAKE_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/SHAKE_COMPLETE_EVENT.js#L7)  
引入版本：3.3.0

## SHAKE_START {#shake_start}


**说明:** 相机摇动启动事件.

摇晃效应开始时, 由相机实例发出此事件 。

通过以下任一方式倾听:

```js
this.cameras.main.on('camerashakestart', () => {});
```

或使用常数,以避免需要记住正确的事件字符串:

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.SHAKE_START, () => {});
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Shake](/api/class/cameras-scene2d-effects-shake) | 否 | 提及效果实例。 |
| duration | number | 否 | 效期长短. |
| intensity | number | 否 | 效果的强度. |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/SHAKE_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/SHAKE_START_EVENT.js#L7)  
引入版本：3.3.0

## ZOOM_COMPLETE {#zoom_complete}


**说明:** 摄像机的放大完成事件。

缩放效果完成后, 由相机实例发送此事件 。

通过以下任一方式倾听:

```js
this.cameras.main.on('camerazoomcomplete', () => {});
```

或使用常数,以避免需要记住正确的事件字符串:

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.ZOOM_COMPLETE, () => {});
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Zoom](/api/class/cameras-scene2d-effects-zoom) | 否 | 提及效果实例。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/ZOOM_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/ZOOM_COMPLETE_EVENT.js#L7)  
引入版本：3.3.0

## ZOOM_START {#zoom_start}


**说明:** 相机放大启动事件.

缩放效果开始时, 此事件由相机实例发送 。

通过以下任一方式倾听:

```js
this.cameras.main.on('camerazoomstart', () => {});
```

或使用常数,以避免需要记住正确的事件字符串:

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.ZOOM_START, () => {});
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Zoom](/api/class/cameras-scene2d-effects-zoom) | 否 | 提及效果实例。 |
| duration | number | 否 | 效期长短. |
| zoom | number | 否 | 目的地缩放值 。 |

**Member of:** [Phaser.Cameras.Scene2D.Events](/api/namespace/cameras-scene2d-events)
> 源码：[src/cameras/2d/events/ZOOM_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/ZOOM_START_EVENT.js#L7)  
引入版本：3.3.0

---
