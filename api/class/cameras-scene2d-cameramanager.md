# CameraManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/cameras-scene2d-cameramanager)

相机管理器是一个属于一个场景的插件,负责管理所有场景的相机.

默认情况下,您可以从场内使用 `this.cameras` 访问相机管理器,尽管此功能可以在游戏配置中更改 。

使用 `add` 方法创建新相机。 或用您自己的添加代码扩展相机类, 然后在使用 `addExisting` 方法时添加新相机 。

相机提供进入游戏世界的视图,可以定位,旋转,放大和滚动相应.

相机由两个元素组成:观光灯和滚动值.

视图端口是游戏中相机的物理位置和大小。 相机默认是和游戏大小相同的, 但其位置和大小可以设定为任意一种。 这意味着如果您想要创建一个大小为320x200的相机, 并定位在游戏的右下角, 您会调整视图端口来完成此任务( 使用方法如 ) `setViewport` 财务报告和已审计财务报表 `setSize`).

如果您想要改变游戏中镜头的搜索位置, 请滚动它。 您可以通过属性 `scrollX` 和 `scrollY` 或方法 `setScroll` 来完成 。 滚动对视图没有影响, 更改视图对滚动没有影响 。

默认情况下, 相机会让它看到所有游戏对象。 您可以使用 `ignore` 方法修改此功能, 允许您在每集的基础上过滤游戏对象。 相机管理器可以管理最多 31 个独特的“ Game Object 忽略能力” 相机。 您创建的超过 31 个相机都会被赋予 0 的相机ID, 这意味着它们不能用于游戏对象排除 。 这意味着 如果您需要相机忽略 Game Objects, 请确定它是 最早创建的 31 之一 。

一台相机还具有内置的特效,包括Fade,Flash,Camera Shake,Pan和Zoom.

**构造函数**

`new CameraManager(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 拥有相机管理器插件的场景 。 |

---


**作用域**: static

> 源码：[src/cameras/2d/CameraManager.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L15)  
引入版本：3.0.0

## 公开成员 {#public-members}

### cameras {#cameras}

#### cameras: Array.\<[Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera)> {#cameras-arrayphasercamerasscene2dcamera}


**说明:**

由相机管理器管理的相机对象的矩阵。相机按其出现在此阵列的顺序进行更新和渲染。不要直接添加或删除该阵列的条目。但是,如果您想要调整显示顺序,可以将内容移动到数组周围。


> 源码：[src/cameras/2d/CameraManager.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L89)  
引入版本：3.0.0


---

### default {#default}

#### default: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#default-phasercamerasscene2dcamera}


**说明:**

默认的未变形相机, 它不存在于相机列表中, 并且不计算所管理相机的总数。 它存在于其他系统, 以及您自己的代码, 如果它们需要一个基本的未变形相机实例, 来计算视图矩阵 。


> 源码：[src/cameras/2d/CameraManager.js#L118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L118)  
引入版本：3.17.0


---

### main {#main}

#### main: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#main-phasercamerasscene2dcamera}


**说明:**

方便地引用“ 主” 相机。 默认这是相机管理器创建的第一台相机。 您也可以直接设定, 或者使用 `makeMain` 参数中 `add` 财务报告和已审计财务报表 `addExisting` 它允许您从游戏中访问它 :

```javascript
var cam = this.cameras.main;
```

亦见属性`camera1`,`camera2`等.


> 源码：[src/cameras/2d/CameraManager.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L101)  
引入版本：3.0.0


---

### roundPixels {#roundPixels}

#### roundPixels: boolean {#roundpixels-boolean}


**说明:**

所有由此相机管理器创建或添加的相机都会有匹配此值的`roundPixels`属性设定。 默认情况下, 将设定匹配游戏配置中的值设定, 但可以在任意时间更改 。 同样, 单个相机也可以根据需要更改 。


> 源码：[src/cameras/2d/CameraManager.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L77)  
引入版本：3.11.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

拥有相机管理器插件的场景 。


> 源码：[src/cameras/2d/CameraManager.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L59)  
引入版本：3.0.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

参考Scene.Systems处理器,用于拥有相机管理器的Scene.


> 源码：[src/cameras/2d/CameraManager.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L68)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add([x], [y], [width], [height], [makeMain], [name]) {#instance-addx-y-width-height-makemain-name}


**说明:**

将新相机添加到相机管理器中,相机管理器最多可以支持31个不同的相机.

每台相机都有自己的视门,它控制相机的大小及其在画布中的位置.

使用`Camera.scrollX`和`Camera.scrollY`的属性来改变相机的外观,或者像`centerOn`这样的相机方法. 相机也构建了特殊效果,如淡化,闪光,摇晃,锅和缩放.

默认相机是透明的,并且会根据它们的`scrollX`和`scrollY`值来渲染它们能看见的任何东西. 游戏对象可以通过使用`Camera.ignore`方法被设定为被相机忽略.

相机会设置它的 `roundPixels` 属性到 `CameraManager.roundPixels` 的任意位置。 如果需要, 您可以在创建后更改它 。

详情请见相机类文档.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 相机视网的横向位置. |
| y | number | 是 | 0 | 相机视门的垂直位置. |
| width | number | 是 |  | 相机视图的宽度。 如果不给出, 则会是游戏配置大小 。 |
| height | number | 是 |  | 相机视网的高度, 如果不给出, 将会是游戏配置大小 。 |
| makeMain | boolean | 是 | false | 设定此相机为“ 主” 相机。 这只使属性 `main` 成为了它的参考 。 |
| 名称 | string | 是 | "''" | 相机名称. |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 刚创建的摄像机。


> 源码：[src/cameras/2d/CameraManager.js#L205](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L205)  
引入版本：3.0.0


---

### addExisting {#addExisting}

#### \<instance> addExisting(camera, [makeMain]) {#instance-addexistingcamera-makemain}


**说明:**

将已有的相机添加到相机管理器中 。

摄像机要么是`Phaser.Cameras.Scene2D.Camera`实例,要么是从中延伸出来的类.

相机会设置它的 `roundPixels` 属性到 `CameraManager.roundPixels` 的任意位置。 如果需要, 您可以在添加后更改 。

相机将被分配到一个ID, 用于游戏对象排除, 然后添加到管理器中。 只要管理器中不存在它, 就会被添加到它中然后返回 。

如果这种方法返回 `null`,那么相机已经存在于这个相机管理器中.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 相机管理员要加的相机 |
| makeMain | boolean | 是 | false | 设定此相机为“ 主” 相机。 这只使属性 `main` 成为了它的参考 。 |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 相机管理员加的相机,或者说如果无法加的`null`.


> 源码：[src/cameras/2d/CameraManager.js#L261](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L261)  
引入版本：3.0.0


---

### fromJSON {#fromJSON}

#### \<instance> fromJSON(config) {#instance-fromjsonconfig}


**说明:**

基于给定配置对象,或配置对象的数组, 复制此相机管理器 。

关于对象结构的细节,请参见`Phaser.Types.Cameras.Scene2D.CameraConfig`文档.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Cameras.Scene2D.CameraConfig](/api/typedef/types-cameras-scene2d#cameraconfig) \| Array.\<[Phaser.Types.Cameras.Scene2D.CameraConfig](/api/typedef/types-cameras-scene2d#cameraconfig)> | 否 | 相机配置对象,或其中的数组,将添加到此相机管理器中 。 |


**返回值:** [Phaser.Cameras.Scene2D.CameraManager](/api/class/cameras-scene2d-cameramanager) - 这个摄像机管理员的例子。


> 源码：[src/cameras/2d/CameraManager.js#L388](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L388)  
引入版本：3.0.0


---

### getCamera {#getCamera}

#### \<instance> getCamera(name) {#instance-getcameraname}


**说明:**

获得一个基于它的名字的相机.

相机名称是可选的,不需要设置,因此这种方法只有在你给相机取了自己独特的名称时才有任何用处.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 相机名称. |


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 第一台相机,名字与给定的字符串匹配,否则会`null`.


> 源码：[src/cameras/2d/CameraManager.js#L457](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L457)  
引入版本：3.0.0


---

### getCamerasBelowPointer {#getCamerasBelowPointer}

#### \<instance> getCamerasBelowPointer(pointer) {#instance-getcamerasbelowpointerpointer}


**说明:**

返回给定指针下方的所有相机阵列。

阵列中的第一个镜头是镜头列表中最顶尖的镜头.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 指针来检查。 |


**返回值:** Array.\<[Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera)> - 指针下面的一组摄像机


> 源码：[src/cameras/2d/CameraManager.js#L485](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L485)  
引入版本：3.10.0


---

### getTotal {#getTotal}

#### \<instance> getTotal([isVisible]) {#instance-gettotalisvisible}


**说明:**

得到摄像机管理器的摄像机总数。

如果设置了可选的 `isVisible` 参数, 则只计算当前可见的相机 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| isVisible | boolean | 是 | false | 设定为 `true` , 仅包含可见相机在总数中. |


**返回值:** number - 摄像机经理的摄像机总数


> 源码：[src/cameras/2d/CameraManager.js#L355](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L355)  
引入版本：3.11.0


---

### getVisibleChildren {#getVisibleChildren}

#### \<instance> getVisibleChildren(children, camera) {#instance-getvisiblechildrenchildren-camera}


**说明:**

取出一系列游戏对象和一个相机,返回一个只包含那些通过`willRender`测试的游戏对象的新阵列,以对抗给定的相机.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| children | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 一组游戏对象, 需要对照相机检查 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 过滤游戏对象的相机 。 |


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 过滤后, 将针对给定的相机渲染的场景中仅包含游戏对象的列表 。


> 源码：[src/cameras/2d/CameraManager.js#L612](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L612)  
引入版本：3.50.0


---

### onResize {#onResize}

#### \<instance> onResize(gameSize, baseSize) {#instance-onresizegamesize-basesize}


**说明:**

管理由缩放管理器发出的 `resize` 事件的事件处理器 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameSize | [Phaser.Structs.Size](/api/class/structs-size) | 否 | 默认的游戏大小对象。 这是未修改的游戏尺寸 。 |
| baseSize | [Phaser.Structs.Size](/api/class/structs-size) | 否 | 基数对象。 游戏尺寸。 画布宽度/ 高度值与此相符 。 |


> 源码：[src/cameras/2d/CameraManager.js#L676](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L676)  
引入版本：3.18.0


---

### remove {#remove}

#### \<instance> remove(camera, [runDestroy]) {#instance-removecamera-rundestroy}


**说明:**

从这个相机管理器中移除给定的相机,或一系列相机.

如果在相机管理器中找到它, 将立即从本地相机阵列中移除。 如果目前“ main” 相机, “main” 将被重置为相机 0 。

如果 `runDestroy` 参数是 `true`, 则自动销毁。 如果您想要重新使用这些相机, 请将此设定为 `false`, 但知道它们会保留其参考文献和内部数据, 直至被销毁或重新添加到相机管理器中 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) \| Array.\<[Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera)> | 否 |  | 相机,或一系列相机, 将从相机管理员中移除。 |
| runDestroy | boolean | 是 | true | 从这台相机管理员中移除的每台相机上自动拨打`Camera.destroy`. |


**返回值:** number - 相机的总数被移除了.


> 源码：[src/cameras/2d/CameraManager.js#L520](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L520)  
引入版本：3.0.0


---

### render {#render}

#### \<instance> render(renderer, displayList) {#instance-renderrenderer-displaylist}


**说明:**

内部渲染方法。 由 Scene 自动调用, 不应直接引用 。

它会通过所有局部摄像机进行移动,并依次使其成型,只要它们可见,并具有α级>0.


**Access:** 保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) \| [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 将孩子们带到这台摄像机上的发光器 |
| displayList | [Phaser.GameObjects.DisplayList](/api/class/gameobjects-displaylist) | 否 | 场景的显示列表 。 |


> 源码：[src/cameras/2d/CameraManager.js#L579](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L579)  
引入版本：3.0.0


---

### resetAll {#resetAll}

#### \<instance> resetAll() {#instance-resetall}


**说明:**

重新调用这个相机管理员。

这将通过所有当前相机进行伸缩,摧毁全部相机,然后它会重置相机阵列,重置ID计数器,并使用默认值创建1个新的单相机.


**返回值:** [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) - 刚创建的正摄像机


> 源码：[src/cameras/2d/CameraManager.js#L633](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L633)  
引入版本：3.0.0


---

### resize {#resize}

#### \<instance> resize(width, height) {#instance-resizewidth-height}


**说明:**

将所有相机的大小调整到给定的尺寸。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 相机的新宽度. |
| height | number | 否 | 摄像机的新高度. |


> 源码：[src/cameras/2d/CameraManager.js#L701](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L701)  
引入版本：3.2.0


---

### update {#update}

#### \<instance> update(time, delta) {#instance-updatetime-delta}


**说明:**

主更新循环, 场景步骤时自动调用 。


**Access:** 保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 请求动画框架或SetTimeout生成的当前时间戳 。 |
| delta | number | 否 | 三角洲时间,以ms计, 过去了,自上一个框架。 |


> 源码：[src/cameras/2d/CameraManager.js#L658](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/CameraManager.js#L658)  
引入版本：3.0.0


---

---
