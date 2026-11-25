# Phaser.Input {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/input)

Scope: 
static
> 源码：[src/input/index.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/index.js#L10)  


## 静态函数 {#static-functions}

- [InputManager](/api/class/input-inputmanager)
- [InputPlugin](/api/class/input-inputplugin)
- [Pointer](/api/class/input-pointer)
## 静态函数 {#static-functions-1}

### MOUSE_DOWN {#MOUSE_DOWN}

#### MOUSE_DOWN: number {#mouse_down-number}


**说明:**

鼠标指针按钮已被按下 。


> 源码：[src/input/const.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/const.js#L9)  
引入版本：3.10.0


---

### MOUSE_MOVE {#MOUSE_MOVE}

#### MOUSE_MOVE: number {#mouse_move-number}


**说明:**

鼠标指针正在移动中 。


> 源码：[src/input/const.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/const.js#L18)  
引入版本：3.10.0


---

### MOUSE_UP {#MOUSE_UP}

#### MOUSE_UP: number {#mouse_up-number}


**说明:**

鼠标指针发布.


> 源码：[src/input/const.js#L27](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/const.js#L27)  
引入版本：3.10.0


---

### MOUSE_WHEEL {#MOUSE_WHEEL}

#### MOUSE_WHEEL: number {#mouse_wheel-number}


**说明:**

鼠轮变了.


> 源码：[src/input/const.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/const.js#L81)  
引入版本：3.18.0


---

### POINTER_LOCK_CHANGE {#POINTER_LOCK_CHANGE}

#### POINTER_LOCK_CHANGE: number {#pointer_lock_change-number}


**说明:**

指针锁变了


> 源码：[src/input/const.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/const.js#L63)  
引入版本：3.10.0


---

### TOUCH_CANCEL {#TOUCH_CANCEL}

#### TOUCH_CANCEL: number {#touch_cancel-number}


**说明:**

浏览器取消了一个触点。


> 源码：[src/input/const.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/const.js#L72)  
引入版本：3.15.0


---

### TOUCH_END {#TOUCH_END}

#### TOUCH_END: number {#touch_end-number}


**说明:**

触点器已经停止了


> 源码：[src/input/const.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/const.js#L54)  
引入版本：3.10.0


---

### TOUCH_MOVE {#TOUCH_MOVE}

#### TOUCH_MOVE: number {#touch_move-number}


**说明:**

触觉指针已经移动了。


> 源码：[src/input/const.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/const.js#L45)  
引入版本：3.10.0


---

### TOUCH_START {#TOUCH_START}

#### TOUCH_START: number {#touch_start-number}


**说明:**

触点器已经开始了。


> 源码：[src/input/const.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/const.js#L36)  
引入版本：3.10.0


---

## 静态函数 {#static-functions-2}

### CreateInteractiveObject {#CreateInteractiveObject}

#### \<static> CreateInteractiveObject(gameObject, hitArea, hitAreaCallback) {#static-createinteractiveobjectgameobject-hitarea-hitareacallback}


**说明:**

创建新的交互式对象。

交互式对象是一个普通数据对象,它存储了游戏对象的所有输入状态。这包括命中区域几何、拖动状态、局部指针坐标、摄像机和任何投放区目标的引用。它不是一个类实例,而是该函数返回的普通对象字面。

当您启用游戏对象进行输入时, 输入管理器会自动调用此功能 。

由此而来的互动对象被映射到游戏对象的`input`属性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此交互对象所约束的游戏对象 。 |
| hitArea | any | 否 | 此交互对象的命中区域。 通常是一个几何形状, 如矩形或圆形 。 |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 否 | 命中区形状将用来进行所有命中测试的“ 封装” 检查回调 。 |


**返回值:** [Phaser.Types.Input.InteractiveObject](/api/typedef/types-input#interactiveobject) - 新的交互式对象 。


> 源码：[src/input/CreateInteractiveObject.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/CreateInteractiveObject.js#L7)  
引入版本：3.0.0


---

### CreatePixelPerfectHandler {#CreatePixelPerfectHandler}

#### \<static> CreatePixelPerfectHandler(textureManager, alphaTolerance) {#static-createpixelperfecthandlertexturemanager-alphatolerance}


**说明:**

创建新的像素完美处理器功能。

像素完美地击中检测测试了特定像素在游戏对象纹理上相互作用的α值,而不是完全依赖其约束框或命中区域几何,这使得在指针和重叠检查时完全透明的图样区域会被正确忽略,而每次测试都要以纹理检查为代价.

访问通过 `InputPlugin.makePixelPerfect` 而不是直接打电话

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| textureManager | [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) | 否 | 纹理管理器的参考文献. |
| alphaTolerance | number | 否 | 像素必须位于或高于的α级,以算作成功的交互. |


**返回值:** function - 新的像素完美处理器功能 。


> 源码：[src/input/CreatePixelPerfectHandler.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/CreatePixelPerfectHandler.js#L7)  
引入版本：3.10.0


---

## 静态函数 {#static-functions-3}

- [Events](/api/namespace/input-events)
- [Gamepad](/api/namespace/input-gamepad)
- [InputPluginCache](/api/namespace/input-inputplugincache)
- [Keyboard](/api/namespace/input-keyboard)
- [Mouse](/api/namespace/input-mouse)
- [Touch](/api/namespace/input-touch)

---
