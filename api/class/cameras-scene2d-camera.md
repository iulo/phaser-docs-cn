# Camera {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/cameras-scene2d-camera)

摄像机提供游戏世界的视图, 并且是 Phaser 中主要渲染场景的方式。 每个场景至少有一台摄像机( 主摄像机), 您可以通过摄像机管理器添加摄像机。 摄像机可以滚动、 缩放、 旋转, 并配备一些特殊效果, 如淡化、 闪光、 摇晃、 锅和缩放过渡 。

摄像机是所有游戏以 Phaser 格式渲染的方式。它们为您的游戏世界提供了视图,可以定位、旋转、放大和滚动。

摄像机由两个元素组成:观光灯和滚动值.

视口是游戏中摄像机的物理位置和大小。 摄像机默认是和游戏大小相同的, 但其位置和大小可以设定为任意一种。 这意味着如果您想要创建一个大小为320x200的摄像机, 并定位在游戏的右下角, 您会调整视口来完成此任务( 使用方法如 ) `setViewport` 财务报告和已审计财务报表 `setSize`然而,视口仅限于作为轴向对齐的矩形,不能旋转。使用一个轴向对角更强大、更可靠。 `RenderTexture` 或 或 时 间 `DynamicTexture` 。将其摄像机指向您想要的视口,设定其大小,然后绘制游戏对象。

如果您想要改变游戏中镜头的搜索位置, 请滚动它。 您可以通过属性 `scrollX` 和 `scrollY` 或方法 `setScroll` 来完成 。 滚动对视图没有影响, 更改视图对滚动没有影响 。

默认情况下, 摄像机会让它看到所有游戏对象。 您可以使用 `ignore` 方法更改此功能, 允许您在每加美拉的基础上过滤游戏对象 。

摄像机还具有内置的特效,包括Fade,Flash和Camera Shake.

您可以应用全摄像机过滤器。 有些过滤器需要离屏幕数据, 如 Blur; 使用 `camera.getPaddingWrapper()` 来获得一个代理设备, 用于使用应用的粘贴符来操作摄像机 。

**构造函数**

`new Camera(x, y, width, height)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 摄像机的x位置,相对于游戏画布的左上角. |
| y | number | 否 | 摄像机的y位置,相对于游戏画布的左上角. |
| width | number | 否 | 摄像机的宽度,以像素表示. |
| height | number | 否 | 摄像机的高度,以像素表示. |

---


**作用域**: static


**继承**

> [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera)  



> 源码：[src/cameras/2d/Camera.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L18)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera):**


 - [alpha](/api/class/cameras-scene2d-basecamera#alpha)
 - [backgroundColor](/api/class/cameras-scene2d-basecamera#backgroundColor)
 - [cameraManager](/api/class/cameras-scene2d-basecamera#cameraManager)
 - [centerX](/api/class/cameras-scene2d-basecamera#centerX)
 - [centerY](/api/class/cameras-scene2d-basecamera#centerY)
 - [dirty](/api/class/cameras-scene2d-basecamera#dirty)
 - [disableCull](/api/class/cameras-scene2d-basecamera#disableCull)
 - [displayHeight](/api/class/cameras-scene2d-basecamera#displayHeight)
 - [displayWidth](/api/class/cameras-scene2d-basecamera#displayWidth)
 - [forceComposite](/api/class/cameras-scene2d-basecamera#forceComposite)
 - [height](/api/class/cameras-scene2d-basecamera#height)
 - [id](/api/class/cameras-scene2d-basecamera#id)
 - [isSceneCamera](/api/class/cameras-scene2d-basecamera#isSceneCamera)
 - [mask](/api/class/cameras-scene2d-basecamera#mask)
 - [matrixCombined](/api/class/cameras-scene2d-basecamera#matrixCombined)
 - [matrixExternal](/api/class/cameras-scene2d-basecamera#matrixExternal)
 - [midPoint](/api/class/cameras-scene2d-basecamera#midPoint)
 - [name](/api/class/cameras-scene2d-basecamera#name)
 - [originX](/api/class/cameras-scene2d-basecamera#originX)
 - [originY](/api/class/cameras-scene2d-basecamera#originY)
 - [renderList](/api/class/cameras-scene2d-basecamera#renderList)
 - [renderRoundPixels](/api/class/cameras-scene2d-basecamera#renderRoundPixels)
 - [roundPixels](/api/class/cameras-scene2d-basecamera#roundPixels)
 - [scaleManager](/api/class/cameras-scene2d-basecamera#scaleManager)
 - [scene](/api/class/cameras-scene2d-basecamera#scene)
 - [sceneManager](/api/class/cameras-scene2d-basecamera#sceneManager)
 - [scrollX](/api/class/cameras-scene2d-basecamera#scrollX)
 - [scrollY](/api/class/cameras-scene2d-basecamera#scrollY)
 - [transparent](/api/class/cameras-scene2d-basecamera#transparent)
 - [useBounds](/api/class/cameras-scene2d-basecamera#useBounds)
 - [visible](/api/class/cameras-scene2d-basecamera#visible)
 - [width](/api/class/cameras-scene2d-basecamera#width)
 - [worldView](/api/class/cameras-scene2d-basecamera#worldView)
 - [x](/api/class/cameras-scene2d-basecamera#x)
 - [y](/api/class/cameras-scene2d-basecamera#y)
 - [zoom](/api/class/cameras-scene2d-basecamera#zoom)
 - [zoomX](/api/class/cameras-scene2d-basecamera#zoomX)
 - [zoomY](/api/class/cameras-scene2d-basecamera#zoomY)




---

## 公开成员 {#public-members}

### deadzone {#deadzone}

#### deadzone: [Phaser.Geom.Rectangle](/api/class/geom-rectangle) {#deadzone-phasergeomrectangle}


**说明:**

摄像机死区。

死区只在镜头跟随目标时才使用.

它定义了一个矩形区域,如果目标存在,摄像机不会滚动。如果目标移动到此区域之外,摄像机会开始滚动,以便跟踪它。

您可以为后续对象设定的 `lerp` 值在使用死区时也会适用.

您可以直接设置此属性为矩形实例。 或者, 您可以使用 `setDeadzone` 方法来进行可链路处理 。

但是,请注意,它的方格位置是每个框架更新的,因为它不断重新以摄像机中点为中心。

调用无参数的 `setDeadzone` 将重设一个活动死区, 以及将此属性设置为 `null` 。


> 源码：[src/cameras/2d/Camera.js#L203](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L203)  
引入版本：3.11.0


---

### fadeEffect {#fadeEffect}

#### fadeEffect: [Phaser.Cameras.Scene2D.Effects.Fade](/api/class/cameras-scene2d-effects-fade) {#fadeeffect-phasercamerasscene2deffectsfade}


**说明:**

摄像机变淡效果处理器 需要看到`Camera.fade`的方法


> 源码：[src/cameras/2d/Camera.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L114)  
引入版本：3.5.0


---

### filters {#filters}

#### filters: [Phaser.Types.GameObjects.FiltersInternalExternal](/api/typedef/types-gameobjects#filtersinternalexternal) {#filters-phasertypesgameobjectsfiltersinternalexternal}


**说明:**

用于此摄像机的滤镜,滤镜控制特效和遮罩.

此对象包含两个过滤器列表: `internal`和 `external`. 更多信息请参见 [Phaser.GameObjects.Components.FilterList](/api/class/gameobjects-components-filterlist).


> 源码：[src/cameras/2d/Camera.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L76)  
引入版本：4.0.0


---

### flashEffect {#flashEffect}

#### flashEffect: [Phaser.Cameras.Scene2D.Effects.Flash](/api/class/cameras-scene2d-effects-flash) {#flasheffect-phasercamerasscene2deffectsflash}


**说明:**

摄像机闪光效果处理器 闪光这台摄像机要看到`Camera.flash`的方法


> 源码：[src/cameras/2d/Camera.js#L124](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L124)  
引入版本：3.5.0


---

### followOffset {#followOffset}

#### followOffset: [Phaser.Math.Vector2](/api/class/math-vector2) {#followoffset-phasermathvector2}


**说明:**

存储在此属性中的值从摄像机目标位置中减去, 允许您从实际目标 x/y 坐标中抵消摄像机的这个金额。 也可以通过 `setFollowOffset` 设定, 或者作为 `startFollow` 调用的一部分 。


> 源码：[src/cameras/2d/Camera.js#L192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L192)  
引入版本：3.9.0


---

### inputEnabled {#inputEnabled}

#### inputEnabled: boolean {#inputenabled-boolean}


**说明:**

是否此摄像机允许它制作的游戏对象接收输入事件 ?


> 源码：[src/cameras/2d/Camera.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L104)  
引入版本：3.0.0


---

### isObjectInversion {#isObjectInversion}

#### isObjectInversion: boolean {#isobjectinversion-boolean}


**说明:**

这是用于游戏对象转换反转的摄像机吗? 这是`Filters`组件在渲染对象进行过滤时用来取消游戏对象的变换的.


> 源码：[src/cameras/2d/Camera.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L92)  
引入版本：4.0.0


---

### lerp {#lerp}

#### lerp: [Phaser.Math.Vector2](/api/class/math-vector2) {#lerp-phasermathvector2}


**说明:**

跟踪目标时使用的线性插值。

也可以通过`setLerp`设定,或作为`startFollow`呼叫的一部分.

1的默认值意味着摄像机会立即向目标坐标方向快速的响亮。一个更低的值,如0.1表示摄像机会更慢地跟踪目标,从而实现平稳的过渡。您可以独立设定水平值和垂直值,并在游戏中实时调整此值。

确定将值保持在 0 到 1 之间, 0 值将禁用该轴上的跟踪 。


> 源码：[src/cameras/2d/Camera.js#L174](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L174)  
引入版本：3.9.0


---

### panEffect {#panEffect}

#### panEffect: [Phaser.Cameras.Scene2D.Effects.Pan](/api/class/cameras-scene2d-effects-pan) {#paneffect-phasercamerasscene2deffectspan}


**说明:**

照摄像机潘效果处理器 拍这个摄像机时,请看`Camera.pan`的方法


> 源码：[src/cameras/2d/Camera.js#L144](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L144)  
引入版本：3.11.0


---

### rotateToEffect {#rotateToEffect}

#### rotateToEffect: [Phaser.Cameras.Scene2D.Effects.RotateTo](/api/class/cameras-scene2d-effects-rotateto) {#rotatetoeffect-phasercamerasscene2deffectsrotateto}


**说明:**

摄像机旋转以生效处理器。 要旋转此摄像机, 请查看 `Camera.rotateTo` 方法 。


> 源码：[src/cameras/2d/Camera.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L154)  
引入版本：3.23.0


---

### shakeEffect {#shakeEffect}

#### shakeEffect: [Phaser.Cameras.Scene2D.Effects.Shake](/api/class/cameras-scene2d-effects-shake) {#shakeeffect-phasercamerasscene2deffectsshake}


**说明:**

摄像机摇晃效果处理器 摇晃这个摄像机时可以看到`Camera.shake`的方法.


> 源码：[src/cameras/2d/Camera.js#L134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L134)  
引入版本：3.5.0


---

### zoomEffect {#zoomEffect}

#### zoomEffect: [Phaser.Cameras.Scene2D.Effects.Zoom](/api/class/cameras-scene2d-effects-zoom) {#zoomeffect-phasercamerasscene2deffectszoom}


**说明:**

摄像机放大效果处理器 要放大这个摄像机,请看`Camera.zoomTo`方法.


> 源码：[src/cameras/2d/Camera.js#L164](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L164)  
引入版本：3.11.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera):**


 - [addToRenderList](/api/class/cameras-scene2d-basecamera#addToRenderList)
 - [centerOn](/api/class/cameras-scene2d-basecamera#centerOn)
 - [centerOnX](/api/class/cameras-scene2d-basecamera#centerOnX)
 - [centerOnY](/api/class/cameras-scene2d-basecamera#centerOnY)
 - [centerToBounds](/api/class/cameras-scene2d-basecamera#centerToBounds)
 - [centerToSize](/api/class/cameras-scene2d-basecamera#centerToSize)
 - [clampX](/api/class/cameras-scene2d-basecamera#clampX)
 - [clampY](/api/class/cameras-scene2d-basecamera#clampY)
 - [clearMask](/api/class/cameras-scene2d-basecamera#clearMask)
 - [cull](/api/class/cameras-scene2d-basecamera#cull)
 - [getBounds](/api/class/cameras-scene2d-basecamera#getBounds)
 - [getScroll](/api/class/cameras-scene2d-basecamera#getScroll)
 - [getWorldPoint](/api/class/cameras-scene2d-basecamera#getWorldPoint)
 - [ignore](/api/class/cameras-scene2d-basecamera#ignore)
 - [removeBounds](/api/class/cameras-scene2d-basecamera#removeBounds)
 - [setAlpha](/api/class/cameras-scene2d-basecamera#setAlpha)
 - [setAngle](/api/class/cameras-scene2d-basecamera#setAngle)
 - [setBackgroundColor](/api/class/cameras-scene2d-basecamera#setBackgroundColor)
 - [setBounds](/api/class/cameras-scene2d-basecamera#setBounds)
 - [setForceComposite](/api/class/cameras-scene2d-basecamera#setForceComposite)
 - [setIsSceneCamera](/api/class/cameras-scene2d-basecamera#setIsSceneCamera)
 - [setMask](/api/class/cameras-scene2d-basecamera#setMask)
 - [setName](/api/class/cameras-scene2d-basecamera#setName)
 - [setOrigin](/api/class/cameras-scene2d-basecamera#setOrigin)
 - [setPosition](/api/class/cameras-scene2d-basecamera#setPosition)
 - [setRotation](/api/class/cameras-scene2d-basecamera#setRotation)
 - [setRoundPixels](/api/class/cameras-scene2d-basecamera#setRoundPixels)
 - [setScene](/api/class/cameras-scene2d-basecamera#setScene)
 - [setScroll](/api/class/cameras-scene2d-basecamera#setScroll)
 - [setSize](/api/class/cameras-scene2d-basecamera#setSize)
 - [setViewport](/api/class/cameras-scene2d-basecamera#setViewport)
 - [setVisible](/api/class/cameras-scene2d-basecamera#setVisible)
 - [setZoom](/api/class/cameras-scene2d-basecamera#setZoom)
 - [toJSON](/api/class/cameras-scene2d-basecamera#toJSON)





**From [Phaser.Events.EventEmitter](/api/class/events-eventemitter):**


 - [addListener](/api/class/events-eventemitter#addListener)
 - [emit](/api/class/events-eventemitter#emit)
 - [eventNames](/api/class/events-eventemitter#eventNames)
 - [listenerCount](/api/class/events-eventemitter#listenerCount)
 - [listeners](/api/class/events-eventemitter#listeners)
 - [off](/api/class/events-eventemitter#off)
 - [on](/api/class/events-eventemitter#on)
 - [once](/api/class/events-eventemitter#once)
 - [removeAllListeners](/api/class/events-eventemitter#removeAllListeners)
 - [removeListener](/api/class/events-eventemitter#removeListener)
 - [shutdown](/api/class/events-eventemitter#shutdown)





**From [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle):**


 - [clearAlpha](/api/namespace/gameobjects-components-alphasingle#clearAlpha)




---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这个镜头,你很少直接打电话

由摄像机管理员呼叫。如果你想摧毁摄像机,请使用`CameraManager.remove`,因为摄像机存放在游泳池里,准备在稍后回收,直接拨打这个可以防止发生这种情况。


**重写:** Phaser.Cameras.Scene2D.BaseCamera#销毁


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:DESTROY](/api/event/cameras-scene2d-events#destroy)


> 源码：[src/cameras/2d/Camera.js#L938](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L938)  
引入版本：3.0.0


---

### fade {#fade}

#### \<instance> fade([duration], [red], [green], [blue], [force], [callback], [context]) {#instance-fadeduration-red-green-blue-force-callback-context}


**说明:**

摄像机在指定时间内从透明到给定的颜色。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| duration | number | 是 | 1000 | 效果持续时间以毫秒计. |
| red | number | 是 | 0 | 向红色通道淡化的数值, 值在 0 到 255 之间 。 |
| green | number | 是 | 0 | 向绿色通道淡去的金额,数值在0到255之间。 |
| blue | number | 是 | 0 | 向蓝色通道淡去的金额, 值在 0 到 255 之间 。 |
| force | boolean | 是 | false | 强制效果立即启动, 即使已经运行 。 |
| callback | function | 是 |  | 将在此效果持续期间引用每个帧。 它会被发送两个参数: 引用摄像机和0到1之间的进度量, 说明效果有多完整 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为摄像机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:FADE_OUT_START](/api/event/cameras-scene2d-events#fade_out_start), [Phaser.Cameras.Scene2D.Events#event:FADE_OUT_COMPLETE](/api/event/cameras-scene2d-events#fade_out_complete)


> 源码：[src/cameras/2d/Camera.js#L373](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L373)  
引入版本：3.0.0


---

### fadeFrom {#fadeFrom}

#### \<instance> fadeFrom([duration], [red], [green], [blue], [force], [callback], [context]) {#instance-fadefromduration-red-green-blue-force-callback-context}


**说明:**

摄像机从给定的颜色向透明显示的长度。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| duration | number | 是 | 1000 | 效果持续时间以毫秒计. |
| red | number | 是 | 0 | 向红色通道淡化的数值, 值在 0 到 255 之间 。 |
| green | number | 是 | 0 | 向绿色通道淡去的金额,数值在0到255之间。 |
| blue | number | 是 | 0 | 向蓝色通道淡去的金额, 值在 0 到 255 之间 。 |
| force | boolean | 是 | false | 强制效果立即启动, 即使已经运行 。 |
| callback | function | 是 |  | 将在此效果持续期间引用每个帧。 它会被发送两个参数: 引用摄像机和0到1之间的进度量, 说明效果有多完整 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为摄像机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:FADE_IN_START](/api/event/cameras-scene2d-events#fade_in_start), [Phaser.Cameras.Scene2D.Events#event:FADE_IN_COMPLETE](/api/event/cameras-scene2d-events#fade_in_complete)


> 源码：[src/cameras/2d/Camera.js#L349](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L349)  
引入版本：3.5.0


---

### fadeIn {#fadeIn}

#### \<instance> fadeIn([duration], [red], [green], [blue], [callback], [context]) {#instance-fadeinduration-red-green-blue-callback-context}


**说明:**

摄像机在指定时间内从给定的颜色中变形。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| duration | number | 是 | 1000 | 效果持续时间以毫秒计. |
| red | number | 是 | 0 | 向红色通道淡化的数值, 值在 0 到 255 之间 。 |
| green | number | 是 | 0 | 向绿色通道淡去的金额,数值在0到255之间。 |
| blue | number | 是 | 0 | 向蓝色通道淡去的金额, 值在 0 到 255 之间 。 |
| callback | function | 是 |  | 将在此效果持续期间引用每个帧。 它会被发送两个参数: 引用摄像机和0到1之间的进度量, 说明效果有多完整 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为摄像机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:FADE_IN_START](/api/event/cameras-scene2d-events#fade_in_start), [Phaser.Cameras.Scene2D.Events#event:FADE_IN_COMPLETE](/api/event/cameras-scene2d-events#fade_in_complete)


> 源码：[src/cameras/2d/Camera.js#L302](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L302)  
引入版本：3.3.0


---

### fadeOut {#fadeOut}

#### \<instance> fadeOut([duration], [red], [green], [blue], [callback], [context]) {#instance-fadeoutduration-red-green-blue-callback-context}


**说明:**

将摄像机在指定时间内向给定的颜色飞去。 这是摄像机的别名。 假使显示显示会开始, 不论是否存在淡出 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| duration | number | 是 | 1000 | 效果持续时间以毫秒计. |
| red | number | 是 | 0 | 向红色通道淡化的数值, 值在 0 到 255 之间 。 |
| green | number | 是 | 0 | 向绿色通道淡去的金额,数值在0到255之间。 |
| blue | number | 是 | 0 | 向蓝色通道淡去的金额, 值在 0 到 255 之间 。 |
| callback | function | 是 |  | 将在此效果持续期间引用每个帧。 它会被发送两个参数: 引用摄像机和0到1之间的进度量, 说明效果有多完整 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为摄像机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:FADE_OUT_START](/api/event/cameras-scene2d-events#fade_out_start), [Phaser.Cameras.Scene2D.Events#event:FADE_OUT_COMPLETE](/api/event/cameras-scene2d-events#fade_out_complete)


> 源码：[src/cameras/2d/Camera.js#L325](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L325)  
引入版本：3.3.0


---

### flash {#flash}

#### \<instance> flash([duration], [red], [green], [blue], [force], [callback], [context]) {#instance-flashduration-red-green-blue-force-callback-context}


**说明:**

将镜头立即设定到给定的颜色,然后在指定的时间里迅速消失。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| duration | number | 是 | 250 | 效果持续时间以毫秒计. |
| red | number | 是 | 255 | 向红色通道淡化的数值, 值在 0 到 255 之间 。 |
| green | number | 是 | 255 | 向绿色通道淡去的金额,数值在0到255之间。 |
| blue | number | 是 | 255 | 向蓝色通道淡去的金额, 值在 0 到 255 之间 。 |
| force | boolean | 是 | false | 强制效果立即启动, 即使已经运行 。 |
| callback | function | 是 |  | 将在此效果持续期间引用每个帧。 它会被发送两个参数: 引用摄像机和0到1之间的进度量, 说明效果有多完整 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为摄像机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:FLASH_START](/api/event/cameras-scene2d-events#flash_start), [Phaser.Cameras.Scene2D.Events#event:FLASH_COMPLETE](/api/event/cameras-scene2d-events#flash_complete)


> 源码：[src/cameras/2d/Camera.js#L397](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L397)  
引入版本：3.0.0


---

### getPaddingWrapper {#getPaddingWrapper}

#### \<instance> getPaddingWrapper([padding]) {#instance-getpaddingwrapperpadding}


**说明:**

返回管理摄像机粘贴的代理 。

摄像机粘贴会放大摄像机, 添加到区域的每一边。 如果您需要来自正常摄像机区域以外的数据, 例如使用 Blur 过滤器, 这样做会很有用 。

使用代理设备代替摄像机。 它隐藏了复杂的部件, 这样您就可以像以前一样使用摄像机继续工作。 您仍然可以使用原始摄像机来查看调整后的数值 。

铺设会影响原摄像机上的以下属性:

- 减法自 `x`, `y`, `scrollX`, `scrollY`.

- 将双倍的`width`加到高度。

铺设会增加渲染区域, 因此它可以有一个性能成本。 如果您在某个时候不需要额外数据, 请设置为 0 。

一次不能使用一个以上的这样的代理,如果你尝试,他们会战斗,没有人会赢.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| padding | number | 是 | 0 | 初始贴值 。 |


**返回值:** [Phaser.Types.Cameras.Scene2D.CameraPaddingWrapper](/api/typedef/types-cameras-scene2d#camerapaddingwrapper) - 摄像机的代理设备.


> 源码：[src/cameras/2d/Camera.js#L675](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L675)  
引入版本：4.0.0


---

### getViewMatrix {#getViewMatrix}

#### \<instance> getViewMatrix([forceComposite]) {#instance-getviewmatrixforcecomposite}


**说明:**

返回摄像机的视图矩阵。这是内部使用的。

如果摄像机是用来向帧缓冲器渲染的,这是`matrix`,否则就是`matrixCombined`。

**标签:**

 - webglonly

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| forceComposite | boolean | 是 | false | 如果 `true`, 视图矩阵将总是 `matrix`。 这通常用于向帧缓冲器渲染, 因此外部矩阵无关紧要 。 |


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 摄像机的视图矩阵.


> 源码：[src/cameras/2d/Camera.js#L647](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L647)  
引入版本：4.0.0


---

### pan {#pan}

#### \<instance> pan(x, y, [duration], [ease], [force], [callback], [context]) {#instance-panx-y-duration-ease-force-callback-context}


**说明:**

这种效果将滚动摄像机,使其视港中心在指定目的地,持续时间和指定的方便度完成.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 目的地x坐标滚动镜头视门中心到. |
| y | number | 否 |  | 目标 Y 坐标滚动摄像机视门中心到 。 |
| duration | number | 是 | 1000 | 效果持续时间以毫秒计. |
| ease | string \| function | 是 | "'Linear'" | 锅的易用性。 可以是任何 Phaser 减速常数或自定义函数 。 |
| force | boolean | 是 | false | 强迫锅效果立即启动, 即使已经运行了 。 |
| callback | [Phaser.Types.Cameras.Scene2D.CameraPanCallback](/api/typedef/types-cameras-scene2d#camerapancallback) | 是 |  | 此调用符会在效果的持续时间里被引用到每个帧。 它被发送四个参数: 引用摄像机, 表示效果完成程度的0到1 之间的进度量, 当前摄像机滚动x坐标和当前摄像机滚动y坐标 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为摄像机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:PAN_START](/api/event/cameras-scene2d-events#pan_start), [Phaser.Cameras.Scene2D.Events#event:PAN_COMPLETE](/api/event/cameras-scene2d-events#pan_complete)


> 源码：[src/cameras/2d/Camera.js#L443](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L443)  
引入版本：3.11.0


---

### preRender {#preRender}

#### \<instance> preRender() {#instance-prerender}


**说明:**

更新摄像机矩阵。 同时重置此摄像机上的任何有效效果( 如摇晃、 闪光和淡化) , 并迅速清除它们 。


> 源码：[src/cameras/2d/Camera.js#L516](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L516)  
引入版本：3.0.0


---

### resetFX {#resetFX}

#### \<instance> resetFX() {#instance-resetfx}


**说明:**

重新设置任何活动的 FX, 如淡出、 闪出或摇动。 可以在淡出后拨打, 以删除淡出 。


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


> 源码：[src/cameras/2d/Camera.js#L895](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L895)  
引入版本：3.0.0


---

### rotateTo {#rotateTo}

#### \<instance> rotateTo(angle, [shortestPath], [duration], [ease], [force], [callback], [context]) {#instance-rotatetoangle-shortestpath-duration-ease-force-callback-context}


**说明:**

在整个期间和指定的方便范围内将摄像机旋转到给定角度。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| angle | number | 否 |  | 以弧度表示的目的地角旋转摄像机视图到. |
| shortestPath | boolean | 是 | false | 如果选中的话, 请将最短的距离拖到目的地。 这将调整目的地角度, 使其在起始角度的半转角之内 。 |
| duration | number | 是 | 1000 | 效果持续时间以毫秒计. |
| ease | string \| function | 是 | "'Linear'" | 易用。 可以是 Phaser 减速常数或自定义函数 。 |
| force | boolean | 是 | false | 强制旋转效果立即启动, 即使已经运行 。 |
| callback | [Phaser.Types.Cameras.Scene2D.CameraRotateCallback](/api/typedef/types-cameras-scene2d#camerarotatecallback) | 是 |  | 此调用符会在效果的持续时间里被引用到每个帧。 它被发送到三个参数: 引用摄像机, 0 到 1 之间的进度量, 表示效果的完成程度, 以及当前摄像机旋转 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为摄像机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


> 源码：[src/cameras/2d/Camera.js#L469](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L469)  
引入版本：3.23.0


---

### setDeadzone {#setDeadzone}

#### \<instance> setDeadzone([width], [height]) {#instance-setdeadzonewidth-height}


**说明:**

设定摄像机死区。

死区只在镜头跟随目标时才使用.

它定义了一个矩形区域,如果目标存在,摄像机不会滚动。如果目标移动到此区域之外,摄像机会开始滚动,以便跟踪它。

死区矩形被重新定位到每个帧, 使其以摄像机的中点为中心。 这样您就可以使用对象进行额外的游戏相关检查, 例如测试是否在其中的某个对象是否通过矩形. contains 调用 。

您可以为后续对象设定的 `lerp` 值在使用死区时也会适用.

使用这个没有参数的方法会重设活动区 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 是 | 以像素表示的死区矩形的宽度。如果不指定死区,则删除。 |
| height | number | 是 | 以像素表示的死区矩形高度. |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


> 源码：[src/cameras/2d/Camera.js#L240](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L240)  
引入版本：3.11.0


---

### setFollowOffset {#setFollowOffset}

#### \<instance> setFollowOffset([x], [y]) {#instance-setfollowoffsetx-y}


**说明:**

设定摄像机从后续目标中的水平和垂直偏移。 数值从摄像机更新步骤中的目标位置中减去。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 摄像机的横向偏移跟随目标.x位置. |
| y | number | 是 | 0 | 摄像机的垂直偏移 沿着目标.y的位置。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


> 源码：[src/cameras/2d/Camera.js#L793](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L793)  
引入版本：3.9.0


---

### setLerp {#setLerp}

#### \<instance> setLerp([x], [y]) {#instance-setlerpx-y}


**说明:**

设置跟踪目标时使用的线性插值。

1 的默认值意味着摄像机会立即向目标坐标方向坐标方向坐标方向坐标点点点点点点。 更低的值, 如 0.1 表示摄像机会更慢地跟踪目标, 从而实现平稳的过渡。 您可以独立设定水平值和垂直值, 并在游戏中实时调整此值 。

确定将值保持在 0 到 1 之间, 0 值将禁用该轴上的跟踪 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 1 | 后续目标的水平线性插值。 0 到 1 之间的值 。 |
| y | number | 是 | 1 | 后续目标的垂直线性插值。 0 到 1 之间的数值 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


> 源码：[src/cameras/2d/Camera.js#L765](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L765)  
引入版本：3.9.0


---

### shake {#shake}

#### \<instance> shake([duration], [intensity], [force], [callback], [context]) {#instance-shakeduration-intensity-force-callback-context}


**说明:**

在特定期间,通过给定的强度来摇动摄像机。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| duration | number | 是 | 100 | 效果持续时间以毫秒计. |
| intensity | number \| [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 0.05 | 摇动的强度. |
| force | boolean | 是 | false | 强制摇动效果立即启动, 即使已经运行 。 |
| callback | function | 是 |  | 将在此效果持续期间引用每个帧。 它会被发送两个参数: 引用摄像机和0到1之间的进度量, 说明效果有多完整 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为摄像机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:SHAKE_START](/api/event/cameras-scene2d-events#shake_start), [Phaser.Cameras.Scene2D.Events#event:SHAKE_COMPLETE](/api/event/cameras-scene2d-events#shake_complete)


> 源码：[src/cameras/2d/Camera.js#L421](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L421)  
引入版本：3.0.0


---

### startFollow {#startFollow}

#### \<instance> startFollow(target, [roundPixels], [lerpX], [lerpY], [offsetX], [offsetY]) {#instance-startfollowtarget-roundpixels-lerpx-lerpy-offsetx-offsety}


**说明:**

设定摄像机以跟随游戏对象。

启用后,摄像机将自动调整其滚动位置,以将目标游戏对象保留在中心.

您可以设置以下代码中使用的线性插值。 使用低脂值( 如 0.1) 自动平滑摄像机运动 。

如果您发现在跟踪对象时会得到轻微的“ jitter” 效果, 这可能与子像素渲染目标位置有关。 您可以设置 `roundPixels` 参数到 `true` 来强制进行全像素圆形渲染 。 请注意, 如果您在摄像机上指定了非整数缩放值, 仍可以打破此效果 。 所以请将摄像机缩放到整数 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| object | 否 |  | 摄像机的目标 |
| roundPixels | boolean | 是 | false | 绕过摄像机位置到整数,以避免子像素渲染? |
| lerpX | number | 是 | 1 | 0到1之间的值,该值指定了水平跟踪目标时使用的线性插值。数值越接近1,摄像机跟踪的速度就越快。 |
| lerpY | number | 是 | 1 | 0到1之间的值,该值指定了垂直跟踪目标时使用的线性插值。值越接近1,摄像机跟踪的速度就越快。 |
| offsetX | number | 是 | 0 | 摄像机的横向偏移跟随目标.x位置. |
| offsetY | number | 是 | 0 | 摄像机的垂直偏移 沿着目标.y的位置。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


> 源码：[src/cameras/2d/Camera.js#L815](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L815)  
引入版本：3.0.0


---

### stopFollow {#stopFollow}

#### \<instance> stopFollow() {#instance-stopfollow}


**说明:**

停止跟踪一个游戏对象, 如果之前通过 `Camera.startFollow` 设定的话。


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


> 源码：[src/cameras/2d/Camera.js#L880](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L880)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update(time, delta) {#instance-updatetime-delta}


**说明:**

由摄像机管理员自动调用的内部方法.


**访问权限:** 受保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 请求动画框架或SetTimeout生成的当前时间戳 。 |
| delta | number | 否 | 三角洲时间,以ms计, 过去了,自上一个框架。 |


**重写:** Phaser.Cameras.Scene2D.BaseCamera#更新日期


> 源码：[src/cameras/2d/Camera.js#L915](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L915)  
引入版本：3.0.0


---

### zoomTo {#zoomTo}

#### \<instance> zoomTo(zoom, [duration], [ease], [force], [callback], [context]) {#instance-zoomtozoom-duration-ease-force-callback-context}


**说明:**

这种效果将使摄像机在规定的持续时间和方便程度上放大到给定的尺度.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| zoom | number | 否 |  | 目标镜头放大值。 |
| duration | number | 是 | 1000 | 效果持续时间以毫秒计. |
| ease | string \| function | 是 | "'Linear'" | 缩放的方便度。 可以是 Phaser 减速常数或自定义函数 。 |
| force | boolean | 是 | false | 强制放大效果立即启动, 即使已经运行 。 |
| callback | [Phaser.Types.Cameras.Scene2D.CameraZoomCallback](/api/typedef/types-cameras-scene2d#camerazoomcallback) | 是 |  | 此调用符会在效果的持续时间里被引用到每个帧。 它被发送三个参数: 引用摄像机, 0 到 1 之间的进度量, 表示效果的完成程度, 以及当前摄像机缩放值 。 |
| context | any | 是 |  | 引用回调时的上下文。 默认为摄像机所属的场景 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 这个镜头的例子。


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:ZOOM_START](/api/event/cameras-scene2d-events#zoom_start), [Phaser.Cameras.Scene2D.Events#event:ZOOM_COMPLETE](/api/event/cameras-scene2d-events#zoom_complete)


> 源码：[src/cameras/2d/Camera.js#L492](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/Camera.js#L492)  
引入版本：3.11.0


---

---
