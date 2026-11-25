# Phaser.Cameras.Scene2D.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/cameras-scene2d-events)

Scope: 
static
> 源码：[src/cameras/2d/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/index.js#L7)  


## 静态函数 {#static-functions}

### DESTROY {#DESTROY}

#### DESTROY {#destroy}


**说明:**

毁灭摄像机事件。

由摄像机管理员破坏时, 由摄像机实例发出。

可以用以下任一方式监听此事件。

```js
this.cameras.main.on('cameradestroy', () => {});
```

也可以使用事件常量，省去记忆事件字符串的步骤。

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.DESTROY, () => {});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) | 否 | 被摧毁的摄像机。 |


> 源码：[src/cameras/2d/events/DESTROY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/DESTROY_EVENT.js#L7)  
引入版本：3.0.0


---

### FADE_IN_COMPLETE {#FADE_IN_COMPLETE}

#### FADE_IN_COMPLETE {#fade_in_complete}


**说明:**

完全事件时的镜头消失

当效果淡出时, 由摄像机实例发出此事件 。

用`Camera.on('camerafadeincomplete', listener)`从镜头中听它

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](/api/class/cameras-scene2d-effects-fade) | 否 | 提及效果实例。 |


> 源码：[src/cameras/2d/events/FADE_IN_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/FADE_IN_COMPLETE_EVENT.js#L7)  
引入版本：3.3.0


---

### FADE_IN_START {#FADE_IN_START}

#### FADE_IN_START {#fade_in_start}


**说明:**

镜头在开始事件中消失。

事件由摄像机实例在“消失效应”开始时发出 。

用`Camera.on('camerafadeinstart', listener)`从镜头中听它

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](/api/class/cameras-scene2d-effects-fade) | 否 | 提及效果实例。 |
| duration | number | 否 | 效期长短. |
| red | number | 否 | 红色通道值 。 |
| green | number | 否 | 绿色通道值 。 |
| blue | number | 否 | 蓝色通道值 。 |


> 源码：[src/cameras/2d/events/FADE_IN_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/FADE_IN_START_EVENT.js#L7)  
引入版本：3.3.0


---

### FADE_OUT_COMPLETE {#FADE_OUT_COMPLETE}

#### FADE_OUT_COMPLETE {#fade_out_complete}


**说明:**

摄像机完全消失事件。

当淡出效应完成时, 由摄像机实例发出此事件 。

用`Camera.on('camerafadeoutcomplete', listener)`从镜头中听它

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](/api/class/cameras-scene2d-effects-fade) | 否 | 提及效果实例。 |


> 源码：[src/cameras/2d/events/FADE_OUT_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/FADE_OUT_COMPLETE_EVENT.js#L7)  
引入版本：3.3.0


---

### FADE_OUT_START {#FADE_OUT_START}

#### FADE_OUT_START {#fade_out_start}


**说明:**

摄像机消失的启动事件。

当淡出效应开始时, 由摄像机实例发出此事件 。

用`Camera.on('camerafadeoutstart', listener)`从镜头中听它

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Fade](/api/class/cameras-scene2d-effects-fade) | 否 | 提及效果实例。 |
| duration | number | 否 | 效期长短. |
| red | number | 否 | 红色通道值 。 |
| green | number | 否 | 绿色通道值 。 |
| blue | number | 否 | 蓝色通道值 。 |


> 源码：[src/cameras/2d/events/FADE_OUT_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/FADE_OUT_START_EVENT.js#L7)  
引入版本：3.3.0


---

### FLASH_COMPLETE {#FLASH_COMPLETE}

#### FLASH_COMPLETE {#flash_complete}


**说明:**

摄像机闪光事件

当闪光效应完成时, 由摄像机实例发出此事件 。

可以用以下任一方式监听此事件。

```js
this.cameras.main.on('cameraflashcomplete', () => {});
```

也可以使用事件常量，省去记忆事件字符串的步骤。

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.FLASH_COMPLETE, () => {});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Flash](/api/class/cameras-scene2d-effects-flash) | 否 | 提及效果实例。 |


> 源码：[src/cameras/2d/events/FLASH_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/FLASH_COMPLETE_EVENT.js#L7)  
引入版本：3.3.0


---

### FLASH_START {#FLASH_START}

#### FLASH_START {#flash_start}


**说明:**

摄像机闪光启动事件.

当闪光效应开始时, 由摄像机实例发出此事件 。

可以用以下任一方式监听此事件。

```js
this.cameras.main.on('cameraflashstart', () => {});
```

也可以使用事件常量，省去记忆事件字符串的步骤。

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.FLASH_START, () => {});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Flash](/api/class/cameras-scene2d-effects-flash) | 否 | 提及效果实例。 |
| duration | number | 否 | 效期长短. |
| red | number | 否 | 红色通道值 。 |
| green | number | 否 | 绿色通道值 。 |
| blue | number | 否 | 蓝色通道值 。 |


> 源码：[src/cameras/2d/events/FLASH_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/FLASH_START_EVENT.js#L7)  
引入版本：3.3.0


---

### FOLLOW_UPDATE {#FOLLOW_UPDATE}

#### FOLLOW_UPDATE {#follow_update}


**说明:**

摄像机跟踪者更新事件.

本次事件是由摄像机实例发出的,当时它正在跟踪一个游戏对象,摄像机位置也因随后的镜头位置而更新.

从一个镜头中听它使用: `camera.on('followupdate', listener)`。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) | 否 | 发射事件的摄像机。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 摄像机所跟踪的游戏对象 。 |


> 源码：[src/cameras/2d/events/FOLLOW_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/FOLLOW_UPDATE_EVENT.js#L7)  
引入版本：3.50.0


---

### PAN_COMPLETE {#PAN_COMPLETE}

#### PAN_COMPLETE {#pan_complete}


**说明:**

摄像机Pan完整事件。

泛效应完成后, 由摄像机实例发送此事件 。

可以用以下任一方式监听此事件。

```js
this.cameras.main.on('camerapancomplete', () => {});
```

也可以使用事件常量，省去记忆事件字符串的步骤。

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.PAN_COMPLETE, () => {});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Pan](/api/class/cameras-scene2d-effects-pan) | 否 | 提及效果实例。 |


> 源码：[src/cameras/2d/events/PAN_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/PAN_COMPLETE_EVENT.js#L7)  
引入版本：3.3.0


---

### PAN_START {#PAN_START}

#### PAN_START {#pan_start}


**说明:**

摄像机潘启动事件.

当泛效应开始时,此事件由摄像机实例发出 。

可以用以下任一方式监听此事件。

```js
this.cameras.main.on('camerapanstart', () => {});
```

也可以使用事件常量，省去记忆事件字符串的步骤。

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.PAN_START, () => {});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Pan](/api/class/cameras-scene2d-effects-pan) | 否 | 提及效果实例。 |
| duration | number | 否 | 效期长短. |
| x | number | 否 | 目的地卷轴 X坐标 。 |
| y | number | 否 | 目的地卷轴 y 坐标。 |


> 源码：[src/cameras/2d/events/PAN_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/PAN_START_EVENT.js#L7)  
引入版本：3.3.0


---

### POST_RENDER {#POST_RENDER}

#### POST_RENDER {#post_render}


**说明:**

摄像机后渲染事件.

此事件由摄像机实例发送, 完成渲染后, 无论是摄像机渲染成纹理还是主画布, 都会发送到此事件 。

从一个镜头中听它使用: `camera.on('postrender', listener)`。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) | 否 | 完成对纹理的摄像机。 |


> 源码：[src/cameras/2d/events/POST_RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/POST_RENDER_EVENT.js#L7)  
引入版本：3.0.0


---

### PRE_RENDER {#PRE_RENDER}

#### PRE_RENDER {#pre_render}


**说明:**

摄像机预渲染事件.

事件在即将渲染时由摄像机实例发出。 只有在摄像机向纹理渲染时才发出 。

从一个镜头中听它使用: `camera.on('prerender', listener)`。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) | 否 | 即将渲染成纹理的摄像机. |


> 源码：[src/cameras/2d/events/PRE_RENDER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/PRE_RENDER_EVENT.js#L7)  
引入版本：3.0.0


---

### ROTATE_COMPLETE {#ROTATE_COMPLETE}

#### ROTATE_COMPLETE {#rotate_complete}


**说明:**

摄像机旋转完成事件。

当旋转效果完成时, 由摄像机实例发送此事件 。

可以用以下任一方式监听此事件。

```js
this.cameras.main.on('camerarotatecomplete', () => {});
```

也可以使用事件常量，省去记忆事件字符串的步骤。

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.ROTATE_COMPLETE, () => {});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.RotateTo](/api/class/cameras-scene2d-effects-rotateto) | 否 | 提及效果实例。 |


> 源码：[src/cameras/2d/events/ROTATE_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/ROTATE_COMPLETE_EVENT.js#L7)  
引入版本：3.23.0


---

### ROTATE_START {#ROTATE_START}

#### ROTATE_START {#rotate_start}


**说明:**

摄像机旋转启动事件。

当旋转效果开始时, 由摄像机实例发出此事件 。

可以用以下任一方式监听此事件。

```js
this.cameras.main.on('camerarotatestart', () => {});
```

也可以使用事件常量，省去记忆事件字符串的步骤。

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.ROTATE_START, () => {});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.RotateTo](/api/class/cameras-scene2d-effects-rotateto) | 否 | 提及效果实例。 |
| duration | number | 否 | 效期长短. |
| destination | number | 否 | 目的地值。 。 |


> 源码：[src/cameras/2d/events/ROTATE_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/ROTATE_START_EVENT.js#L7)  
引入版本：3.23.0


---

### SHAKE_COMPLETE {#SHAKE_COMPLETE}

#### SHAKE_COMPLETE {#shake_complete}


**说明:**

摄像机震动事件

本次事件由摄像机实例在摇摆效应完成后发出.

可以用以下任一方式监听此事件。

```js
this.cameras.main.on('camerashakecomplete', () => {});
```

也可以使用事件常量，省去记忆事件字符串的步骤。

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.SHAKE_COMPLETE, () => {});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Shake](/api/class/cameras-scene2d-effects-shake) | 否 | 提及效果实例。 |


> 源码：[src/cameras/2d/events/SHAKE_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/SHAKE_COMPLETE_EVENT.js#L7)  
引入版本：3.3.0


---

### SHAKE_START {#SHAKE_START}

#### SHAKE_START {#shake_start}


**说明:**

摄像机摇动启动事件.

摇晃效应开始时, 由摄像机实例发出此事件 。

可以用以下任一方式监听此事件。

```js
this.cameras.main.on('camerashakestart', () => {});
```

也可以使用事件常量，省去记忆事件字符串的步骤。

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.SHAKE_START, () => {});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Shake](/api/class/cameras-scene2d-effects-shake) | 否 | 提及效果实例。 |
| duration | number | 否 | 效期长短. |
| intensity | number | 否 | 效果的强度. |


> 源码：[src/cameras/2d/events/SHAKE_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/SHAKE_START_EVENT.js#L7)  
引入版本：3.3.0


---

### ZOOM_COMPLETE {#ZOOM_COMPLETE}

#### ZOOM_COMPLETE {#zoom_complete}


**说明:**

摄像机的放大完成事件。

缩放效果完成后, 由摄像机实例发送此事件 。

可以用以下任一方式监听此事件。

```js
this.cameras.main.on('camerazoomcomplete', () => {});
```

也可以使用事件常量，省去记忆事件字符串的步骤。

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.ZOOM_COMPLETE, () => {});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Zoom](/api/class/cameras-scene2d-effects-zoom) | 否 | 提及效果实例。 |


> 源码：[src/cameras/2d/events/ZOOM_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/ZOOM_COMPLETE_EVENT.js#L7)  
引入版本：3.3.0


---

### ZOOM_START {#ZOOM_START}

#### ZOOM_START {#zoom_start}


**说明:**

摄像机放大启动事件.

缩放效果开始时, 此事件由摄像机实例发送 。

可以用以下任一方式监听此事件。

```js
this.cameras.main.on('camerazoomstart', () => {});
```

也可以使用事件常量，省去记忆事件字符串的步骤。

```js
this.cameras.main.on(Phaser.Cameras.Scene2D.Events.ZOOM_START, () => {});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 效果开始的摄像机。 |
| effect | [Phaser.Cameras.Scene2D.Effects.Zoom](/api/class/cameras-scene2d-effects-zoom) | 否 | 提及效果实例。 |
| duration | number | 否 | 效期长短. |
| zoom | number | 否 | 目的地缩放值 。 |


> 源码：[src/cameras/2d/events/ZOOM_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/events/ZOOM_START_EVENT.js#L7)  
引入版本：3.3.0


---

---
