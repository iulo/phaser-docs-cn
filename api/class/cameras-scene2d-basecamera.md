# BaseCamera {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/cameras-scene2d-basecamera)

基地摄影课

摄像机是所有游戏以 Phaser 格式渲染的方式。它们为您的游戏世界提供了视图,可以定位、旋转、放大和滚动。

摄像机由两个元素组成:观光灯和滚动值.

视口是游戏中摄像机的物理位置和大小。 摄像机默认是和游戏大小相同的, 但其位置和大小可以设定为任意一种。 这意味着如果您想要创建一个大小为320x200的摄像机, 并定位在游戏的右下角, 您会调整视口来完成此任务( 使用方法如 ) `setViewport` 财务报告和已审计财务报表 `setSize`).

如果您想要改变游戏中镜头的搜索位置, 请滚动它。 您可以通过属性 `scrollX` 和 `scrollY` 或方法 `setScroll` 来完成 。 滚动对视图没有影响, 更改视图对滚动没有影响 。

默认情况下, 摄像机会让它看到所有游戏对象。 您可以使用 `ignore` 方法更改此功能, 允许您在每加美拉的基础上过滤游戏对象 。

基座摄像机由摄像机类扩展,增加了包括Fade,Flash和Camera Shake等特殊效果,以及跟踪游戏对象的能力.

基部摄像机是用 Phaser 3. 12 引入的。 它从摄像机类中分离出来, 以便您根据需要分离特殊效果。 因此, 相对于此类属性的“ 自” 值与它们加入摄像机类时有关 。

**构造函数**

`new BaseCamera(x, y, width, height)`

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

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  
> [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/cameras/2d/BaseCamera.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L18)  
引入版本：3.12.0

## 公开成员 {#public-members}

### alpha {#alpha}

#### alpha: number {#alpha-number}


**说明:**

摄像机的alpha值。 设定此属性会撞击此摄像机所生成的每个对象。 您可以直接设定此属性, 即通过Tween, 来淡出摄像机的进出, 或者通过可链式的 `setAlpha` 方法 。


**重写:** Phaser.GameObjects.Components.AlphaSingle#阿尔法


> 源码：[src/cameras/2d/BaseCamera.js#L404](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L404)  
引入版本：3.11.0


---

### backgroundColor {#backgroundColor}

#### backgroundColor: [Phaser.Display.Color](/api/namespace/display-color) {#backgroundcolor-phaserdisplaycolor}


**说明:**

这台摄像机的背景颜色。 只有 `transparent` 时才使用 `false` 。


> 源码：[src/cameras/2d/BaseCamera.js#L395](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L395)  
引入版本：3.0.0


---

### cameraManager {#cameraManager}

#### cameraManager: [Phaser.Cameras.Scene2D.CameraManager](/api/class/cameras-scene2d-cameramanager) {#cameramanager-phasercamerasscene2dcameramanager}


**说明:**

参考了这台摄像机所属的场景摄像机管理器.


> 源码：[src/cameras/2d/BaseCamera.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L107)  
引入版本：3.17.0


---

### centerX {#centerX}

#### centerX: number {#centerx-number}


**说明:**

摄像机的视点中心水平位置,相对游戏画布左侧.


> 源码：[src/cameras/2d/BaseCamera.js#L1938](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1938)  
引入版本：3.10.0


---

### centerY {#centerY}

#### centerY: number {#centery-number}


**说明:**

摄像机的视门中心相对游戏画布顶部的垂直位置.


> 源码：[src/cameras/2d/BaseCamera.js#L1955](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1955)  
引入版本：3.10.0


---

### dirty {#dirty}

#### dirty: boolean {#dirty-boolean}


**说明:**

摄像机脏了吗?

脏摄像机的视门大小、界限、卷轴、旋转或缩放等自上一个帧以来都发生了变化。

渲染时, 此旗帜会随新值一同清除 。


> 源码：[src/cameras/2d/BaseCamera.js#L184](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L184)  
引入版本：3.11.0


---

### disableCull {#disableCull}

#### disableCull: boolean {#disablecull-boolean}


**说明:**

摄像机在检查其输入命中测试前是否要粘住游戏对象? 在某些情况下, 关闭此功能可能是有益的 。


> 源码：[src/cameras/2d/BaseCamera.js#L415](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L415)  
引入版本：3.0.0


---

### displayHeight {#displayHeight}

#### displayHeight: number {#displayheight-number}


**说明:**

显示的摄像机视台高度, 将摄像机缩放级别作为因素 。

如果一个镜头的视孔高度为600,放大度为0.5,那么它的显示高度将是1200,因为它显示的像素是缩放一级两倍.

同样,一个高度为600和放大2的摄像机的显示高度也会达到300像素.


> 源码：[src/cameras/2d/BaseCamera.js#L1995](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1995)  
引入版本：3.11.0


---

### displayWidth {#displayWidth}

#### displayWidth: number {#displaywidth-number}


**说明:**

显示的摄像机视窗宽度, 将显示在摄像机缩放级别中 。

如果一个镜头的视孔宽度为800,放大度为0.5,那么它的显示宽度将是1600,因为它显示的像素是缩放级1的两倍.

同样,宽度800和缩放2的照摄像机的显示宽度也将达到400像素。


> 源码：[src/cameras/2d/BaseCamera.js#L1972](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1972)  
引入版本：3.11.0


---

### forceComposite {#forceComposite}

#### forceComposite: boolean {#forcecomposite-boolean}


**说明:**

是否通过帧缓冲器强制摄像机渲染。 这只在使用 WebGL 渲染器时才适用。 这样, 摄像机内容就可以提供给其他 WebGL 进程, 如 `CaptureFrame` 。

**标签:**

 - webglOnly


> 源码：[src/cameras/2d/BaseCamera.js#L548](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L548)  
引入版本：4.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

镜头视门的高度,以像素表示.

视口是摄像机所进入的区域。设置视口并不限制摄像机可滚动到何处 。


> 源码：[src/cameras/2d/BaseCamera.js#L1722](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1722)  
引入版本：3.0.0


---

### id {#id}

#### id: number {#id-number}


**说明:**

摄像机标识。 由摄像机管理器指定, 并用于处理摄像机排除。 此值是一个位图 。


> 源码：[src/cameras/2d/BaseCamera.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L116)  
引入版本：3.11.0


---

### isSceneCamera {#isSceneCamera}

#### isSceneCamera: boolean {#isscenecamera-boolean}


**说明:**

这是摄像机吗? 还是属于纹理的摄像机?


> 源码：[src/cameras/2d/BaseCamera.js#L537](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L537)  
引入版本：3.60.0


---

### mask {#mask}

#### mask: [Phaser.Display.Masks.GeometryMask](/api/class/display-masks-geometrymask) {#mask-phaserdisplaymasksgeometrymask}


**说明:**

摄像机在渲染过程中使用的遮罩 。 用 `setMask` 方法设置遮罩 。 用 `clearMask` 方法移除遮罩 。


> 源码：[src/cameras/2d/BaseCamera.js#L497](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L497)  
引入版本：3.17.0


---

### matrixCombined {#matrixCombined}

#### matrixCombined: [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) {#matrixcombined-phasergameobjectscomponentstransformmatrix}


**说明:**

结合`matrix`和`matrixExternal`的本地变换矩阵.


> 源码：[src/cameras/2d/BaseCamera.js#L367](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L367)  
引入版本：4.0.0


---

### matrixExternal {#matrixExternal}

#### matrixExternal: [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) {#matrixexternal-phasergameobjectscomponentstransformmatrix}


**说明:**

用于计算摄像机位置的本地变换矩阵 。


> 源码：[src/cameras/2d/BaseCamera.js#L376](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L376)  
引入版本：4.0.0


---

### midPoint {#midPoint}

#### midPoint: [Phaser.Math.Vector2](/api/class/math-vector2) {#midpoint-phasermathvector2}


**说明:**

摄像机在"世界"坐标的中点.

用它来准确了解 摄像机中心目前正在世界中的位置

在卷轴值和跟随器处理完毕后,这个值在preRender方法中更新.


> 源码：[src/cameras/2d/BaseCamera.js#L437](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L437)  
引入版本：3.11.0


---

### name {#name}

#### name: string {#name-string}


**说明:**

摄像机名称, 空的留给您使用 。


> 源码：[src/cameras/2d/BaseCamera.js#L127](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L127)  
引入版本：3.0.0


---

### originX {#originX}

#### originX: number {#originx-number}


**说明:**

此摄像机的横向旋转源 。

默认情况下,摄像机会围绕视港中心旋转.

更改源头允许您调整旋转所在的视口。 0 值将从视口左上旋转。 1 值从右下旋转。

见`setOrigin`将两个起源设置在一个单一的,可连锁的呼叫中.


> 源码：[src/cameras/2d/BaseCamera.js#L452](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L452)  
引入版本：3.11.0


---

### originY {#originY}

#### originY: number {#originy-number}


**说明:**

垂直的旋转源 。

默认情况下,摄像机会围绕视港中心旋转.

更改源头允许您调整旋转所在的视口。 0 值将从视口左上旋转。 1 值从右下旋转。

见`setOrigin`将两个起源设置在一个单一的,可连锁的呼叫中.


> 源码：[src/cameras/2d/BaseCamera.js#L469](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L469)  
引入版本：3.11.0


---

### renderList {#renderList}

#### renderList: Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> {#renderlist-arrayphasergameobjectsgameobject}


**说明:**

此阵列包含此摄像机在上一个(或当前,取决于您检查时)帧中提供的所有游戏对象.

是在`Camera.preUpdate`开始时清除的,或者如果摄像机被摧毁。

您不应该修改这个数组, 因为输入系统内部使用它, 但是您可以按要求读取它。 请注意, 如果游戏对象属于多个非专属容器, 可能在此列表中多次出现 。


> 源码：[src/cameras/2d/BaseCamera.js#L521](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L521)  
引入版本：3.52.0


---

### renderRoundPixels {#renderRoundPixels}

#### renderRoundPixels: boolean {#renderroundpixels-boolean}


**说明:**

此摄像机能渲染圆形像素值吗 ?

此属性在 `preRender` 方法中更新, 不应直接设置 。 它基于摄像机的 `roundPixels` 属性与缩放级别相结合而设置 。 如果缩放是整数, 那么 WebGL 渲染器可以在渲染时应用四舍五入 。


> 源码：[src/cameras/2d/BaseCamera.js#L562](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L562)  
引入版本：3.86.0


---

### roundPixels {#roundPixels}

#### roundPixels: boolean {#roundpixels-boolean}


**说明:**

此摄像机应该绕过它的像素值到整数吗 ?


> 源码：[src/cameras/2d/BaseCamera.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L137)  
引入版本：3.0.0


---

### scaleManager {#scaleManager}

#### scaleManager: [Phaser.Scale.ScaleManager](/api/class/scale-scalemanager) {#scalemanager-phaserscalescalemanager}


**说明:**

游戏缩放管理器的参考文献 。


> 源码：[src/cameras/2d/BaseCamera.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L98)  
引入版本：3.16.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

提到这台摄像机属于的场景


> 源码：[src/cameras/2d/BaseCamera.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L80)  
引入版本：3.0.0


---

### sceneManager {#sceneManager}

#### sceneManager: [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) {#scenemanager-phaserscenesscenemanager}


**说明:**

游戏场景管理器的参考文献.


> 源码：[src/cameras/2d/BaseCamera.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L89)  
引入版本：3.12.0


---

### scrollX {#scrollX}

#### scrollX: number {#scrollx-number}


**说明:**

摄像机的横向滚动位置 。

更改此值, 使摄像机在您的场景上滚动 。

或者,通过`startFollow`方法设置跟踪游戏对象的摄像机,将自动相应调整摄像机滚动值.

您可以设定镜头通过`setBounds`方法滚动的界限.


> 源码：[src/cameras/2d/BaseCamera.js#L1747](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1747)  
引入版本：3.0.0


---

### scrollY {#scrollY}

#### scrollY: number {#scrolly-number}


**说明:**

此摄像机的垂直滚动位置 。

更改此值, 使摄像机在您的场景上滚动 。

或者,通过`startFollow`方法设置跟踪游戏对象的摄像机,将自动相应调整摄像机滚动值.

您可以设定镜头通过`setBounds`方法滚动的界限.


> 源码：[src/cameras/2d/BaseCamera.js#L1780](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1780)  
引入版本：3.0.0


---

### transparent {#transparent}

#### transparent: boolean {#transparent-boolean}


**说明:**

这摄像机有透明背景吗?


> 源码：[src/cameras/2d/BaseCamera.js#L385](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L385)  
引入版本：3.0.0


---

### useBounds {#useBounds}

#### useBounds: boolean {#usebounds-boolean}


**说明:**

这摄像机是用边框来限制滚动移动的吗?

通过 `Camera.setBounds` 设定此属性和界限 。


> 源码：[src/cameras/2d/BaseCamera.js#L159](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L159)  
引入版本：3.0.0


---

### visible {#visible}

#### visible: boolean {#visible-boolean}


**说明:**

这摄像机能看见吗?

可见的摄像机会渲染和进行输入测试。 可见的摄像机不会渲染任何东西, 并且会跳过输入测试 。


**重写:** Phaser.GameObjects.Components.Visible# 可见


> 源码：[src/cameras/2d/BaseCamera.js#L147](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L147)  
引入版本：3.10.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

摄像机视门的宽度,以像素表示.

视口是摄像机所进入的区域。设置视口并不限制摄像机可滚动到何处 。


> 源码：[src/cameras/2d/BaseCamera.js#L1697](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1697)  
引入版本：3.0.0


---

### worldView {#worldView}

#### worldView: [Phaser.Geom.Rectangle](/api/class/geom-rectangle) {#worldview-phasergeomrectangle}


**说明:**

世界视图是一个矩形,它定义了摄像机当前所看到的“世界”区域。在摄像机视图大小、缩放和滚动位置上,这些因素被更新到摄像机preRender步骤中。如果已经启用摄像机将世界视图绑定在这些界限上,您可以使用它来进行剪切或交叉检查。


> 源码：[src/cameras/2d/BaseCamera.js#L171](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L171)  
引入版本：3.11.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

摄像机视图的 x 位置, 相对于游戏画布的左上角。 视图是摄像机所进入的区域。 要调整摄像机在游戏世界中查看的位置, 请参见 `scrollX` 值 。


> 源码：[src/cameras/2d/BaseCamera.js#L1649](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1649)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

摄像机视图的y位置, 相对于游戏画布的左上角。 视图是摄像机所进入的区域。 要调整摄像机在游戏世界中的位置, 请查看 `scrollY`值 。


> 源码：[src/cameras/2d/BaseCamera.js#L1673](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1673)  
引入版本：3.0.0


---

### zoom {#zoom}

#### zoom: number {#zoom-number}


**说明:**

摄像机缩放值。 将此值修改为在场景中或外缩放 。

0.5 的数值可以放大摄像机,所以现在可以比以前看到两倍的场景。2的数值可以放大摄像机,所以现在每个像素在渲染时都占2像素。

设定为 1 以返回默认缩放级别 。

注意永远不要将这个值设置为零.


> 源码：[src/cameras/2d/BaseCamera.js#L1813](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1813)  
引入版本：3.0.0


---

### zoomX {#zoomX}

#### zoomX: number {#zoomx-number}


**说明:**

摄像机水平缩放值。 将此值修改为在场景中或外缩放 。

0.5 的数值可以放大摄像机,所以现在可以比以前看到两倍的场景。2的数值可以放大摄像机,所以现在每个像素在渲染时都占2像素。

设定为 1 以返回默认缩放级别 。

注意永远不要将这个值设置为零.


> 源码：[src/cameras/2d/BaseCamera.js#L1846](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1846)  
引入版本：3.50.0


---

### zoomY {#zoomY}

#### zoomY: number {#zoomy-number}


**说明:**

摄像机垂直缩放值。 将这个值修改为在场景中或外缩放 。

0.5 的数值可以放大摄像机,所以现在可以比以前看到两倍的场景。2的数值可以放大摄像机,所以现在每个像素在渲染时都占2像素。

设定为 1 以返回默认缩放级别 。

注意永远不要将这个值设置为零.


> 源码：[src/cameras/2d/BaseCamera.js#L1877](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1877)  
引入版本：3.50.0


---

## 继承的方法 {#inherited-methods}


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

### addToRenderList {#addToRenderList}

#### \<instance> addToRenderList(child) {#instance-addtorenderlistchild}


**说明:**

将给定的游戏对象添加到此摄像机的渲染列表中 。

在渲染阶段会引用此语句。 只有实际渲染的对象才会出现在渲染列表中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 添加到渲染列表中的游戏对象 。 |


> 源码：[src/cameras/2d/BaseCamera.js#L579](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L579)  
引入版本：3.52.0


---

### centerOn {#centerOn}

#### \<instance> centerOn(x, y) {#instance-centeronx-y}


**说明:**

移动摄像机,使其以给定坐标为中心,允许边框。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 水平坐标以中心为中心. |
| y | number | 否 | 垂直坐标以中心为中心. |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L723](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L723)  
引入版本：3.11.0


---

### centerOnX {#centerOnX}

#### \<instance> centerOnX(x) {#instance-centeronxx}


**说明:**

水平移动摄像机, 使其以给定的 x 坐标为中心, 允许边框。 调用此选项不会改变 scrollY 值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 水平坐标以中心为中心. |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L669](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L669)  
引入版本：3.16.0


---

### centerOnY {#centerOnY}

#### \<instance> centerOnY(y) {#instance-centeronyy}


**说明:**

垂直移动摄像机, 使其以给定的 Y 坐标为中心, 允许边框。 调用此选项不会改变 scrollX 值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| y | number | 否 | 垂直坐标以中心为中心. |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L696](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L696)  
引入版本：3.16.0


---

### centerToBounds {#centerToBounds}

#### \<instance> centerToBounds() {#instance-centertobounds}


**说明:**

移动摄像机,如果启用,它就会看到摄像机的中央。


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L742](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L742)  
引入版本：3.0.0


---

### centerToSize {#centerToSize}

#### \<instance> centerToSize() {#instance-centertosize}


**说明:**

移动摄像机,使其根据其视网膜大小重新定位。


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L767](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L767)  
引入版本：3.0.0


---

### clampX {#clampX}

#### \<instance> clampX(x) {#instance-clampxx}


**说明:**

使用 x 值并检查它是否在摄像机边框范围内, 必要时进行调整。 如果您没有使用摄像机边框, 请不要调用此方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 水平滚动夹的值 。 |


**返回值:** number - 调整后的数值用作 scrollX 。


> 源码：[src/cameras/2d/BaseCamera.js#L957](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L957)  
引入版本：3.11.0


---

### clampY {#clampY}

#### \<instance> clampY(y) {#instance-clampyy}


**说明:**

使用 y 值并检查它是否在摄像机界限范围内, 必要时进行调整。 如果您没有使用摄像机界限, 请不要调用这种方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| y | number | 否 | 垂直滚动夹的值 。 |


**返回值:** number - 调整后的数值用作 scrollY 。


> 源码：[src/cameras/2d/BaseCamera.js#L989](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L989)  
引入版本：3.11.0


---

### clearMask {#clearMask}

#### \<instance> clearMask([destroyMask]) {#instance-clearmaskdestroymask}


**说明:**

清理这台摄像机用的遮罩

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| destroyMask | boolean | 是 | false | 清理前先销毁遮罩? |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1470](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1470)  
引入版本：3.17.0


---

### cull {#cull}

#### \<instance> cull(renderableObjects) {#instance-cullrenderableobjects}


**说明:**

取出一系列游戏对象,然后返回一个仅包含这些对象的新阵列,这些对象由此摄像机可见.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderableObjects | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象库的阵列 。 |


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 摄像机可见的游戏对象阵列 。


> 源码：[src/cameras/2d/BaseCamera.js#L783](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L783)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁此摄像机实例及其内部属性和参考。 一旦被摧毁, 即使重新添加到摄像机管理器中, 您也不能再使用此摄像机 。

如果`runDestroy`的参数是默认的`true`,则这种方法会自动被`CameraManager.remove`称为.

除非有别的具体理由,否则始终使用`CameraManager.remove`并允许它处理摄像机的破坏,而不是直接调用这种方法.


**重写:** Phaser.Events.EventEmitter#销毁


**触发事件:** [Phaser.Cameras.Scene2D.Events#event:DESTROY](/api/event/cameras-scene2d-events#destroy)


> 源码：[src/cameras/2d/BaseCamera.js#L1608](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1608)  
引入版本：3.0.0


---

### getBounds {#getBounds}

#### \<instance> getBounds([out]) {#instance-getboundsout}


**说明:**

返回包含摄像机界限的矩形。

如果摄像机没有边框,矩形就会空空无一人.

矩形是界限的复制品,因此可以安全修改.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 选择要存储边框的矩形。 如果不给定, 将创建新的矩形 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 长方形,包含这摄像机的界限。


> 源码：[src/cameras/2d/BaseCamera.js#L1165](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1165)  
引入版本：3.16.0


---

### getScroll {#getScroll}

#### \<instance> getScroll(x, y, [out]) {#instance-getscrollx-y-out}


**说明:**

计算摄像机。 scrollX和 scrollY 值需要是什么才能移动摄像机, 这样它就集中在给定的 x 和 y 坐标上, 而不会实际移动摄像机。 如果设定的话, 其结果会根据摄像机的界限被夹住 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 水平坐标以中心为中心. |
| y | number | 否 | 垂直坐标以中心为中心. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储值的矢量2。如果未给定新的矢量2,则创建。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 卷轴坐标存储在`x`和`y`属性中.


> 源码：[src/cameras/2d/BaseCamera.js#L636](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L636)  
引入版本：3.11.0


---

### getWorldPoint {#getWorldPoint}

#### \<instance> getWorldPoint(x, y, [output]) {#instance-getworldpointx-y-output}


**说明:**

根据此摄像机的转换将给定的 `x` 和 `y` 坐标转换为世界空间。 您可以选择提供矢量2 或类似的对象, 以存储结果 。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 转换为世界空间的 x 位置 。 |
| y | number | 否 | 转换为世界空间的 Y 位置 。 |
| output | object \| [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 保存结果的可选对象。 如果不提供新的矢量2, 将会创建 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 一个在其`x`和`y`属性中持有转换值的物体.


> 源码：[src/cameras/2d/BaseCamera.js#L861](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L861)  
引入版本：3.0.0


---

### ignore {#ignore}

#### \<instance> ignore(entries) {#instance-ignoreentries}


**说明:**

设定一个游戏对象, 或一系列游戏对象, 它会更新所有摄像机过滤器设置, 以便被此摄像机忽略 。 这意味着它们不会被此摄像机所渲染 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| entries | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | [Phaser.GameObjects.Group](/api/class/gameobjects-group) | 否 | 游戏对象,或游戏对象阵列,要被此摄像机忽略 。 |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L916](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L916)  
引入版本：3.0.0


---

### removeBounds {#removeBounds}

#### \<instance> removeBounds() {#instance-removebounds}


**说明:**

如果这台摄像机之前已经设定了移动界限,这个会移除它们.


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1026](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1026)  
引入版本：3.0.0


---

### setAlpha {#setAlpha}

#### \<instance> setAlpha([value]) {#instance-setalphavalue}


**说明:**

设定此摄像机的 Alpha 级别。 α 控制摄像机的不透明性。 Alpha 值以 0 和 1 之间的浮点表示, 完全透明 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 1 | 摄像机的alpha值。 |


**重写:** Phaser.GameObjects.Components.AlphaSingle#setAlpha


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L595](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L595)  
引入版本：3.11.0


---

### setAngle {#setAngle}

#### \<instance> setAngle([value]) {#instance-setanglevalue}


**说明:**

设定此摄像机的旋转。 这会导致它显示的所有旋转 。

旋转摄像机不旋转视门本身,在渲染时应用.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 0 | 摄像机的旋转角度,以度数给出. |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1045](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1045)  
引入版本：3.0.0


---

### setBackgroundColor {#setBackgroundColor}

#### \<instance> setBackgroundColor([color]) {#instance-setbackgroundcolorcolor}


**说明:**

设置此摄像机的背景颜色 。

默认一个摄像机具有透明的背景,但可以通过这种方法,赋予它坚实的颜色,具有任何层次的透明度.

颜色值可以使用CSS颜色标记,六进制或数字来指定.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| color | string \| number | [Phaser.Types.Display.InputColorObject](/api/typedef/types-display#inputcolorobject) | 是 | "'rgba(0,0,0,0)'" | 颜色值。在 CSS 中,六进制或数字颜色符号。 |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1066](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1066)  
引入版本：3.0.0


---

### setBounds {#setBounds}

#### \<instance> setBounds(x, y, width, height, [centerOn]) {#instance-setboundsx-y-width-height-centeron}


**说明:**

设定摄像机的界限。 界限是一个轴向矩形 。

摄像机将控制摄像机可以滚动到哪些地方,阻止其从边缘滚动到空白空间,并不限制游戏对象的放置,也不限制摄像机视门的位置.

暂时关闭界限 通过改变布尔`Camera.useBounds`。

完全清除界限,叫`Camera.removeBounds`。

如果您设定的界限比视图小, 它会阻止摄像机滚动。 边界可以被定位到您想要的位置。 默认它们从0x0 到画布宽度x高度。 这意味着0x0 是摄像机界限的左上角。 然而, 您可以将其定位到任何地方。 所以, 如果您想要一个大小为 2048x2048 的游戏世界, 而其中的中心为 0x0 , 您可以设定 x/y 的界限为 - 1024, 宽度和高度为 2048 。 取决于您的游戏, 您可以发现 0x0 更容易成为界限的左上角, 或者您希望 0x0 成为中间 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 边框左上角的x坐标 。 |
| y | number | 否 |  | 边框的左上角坐标 。 |
| width | number | 否 |  | 界宽,以像素表示. |
| height | number | 否 |  | 界高,以象素为体. |
| centerOn | boolean | 是 | false | 如果`true`,镜头将自动以新界限为中心. |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1092](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1092)  
引入版本：3.0.0


---

### setForceComposite {#setForceComposite}

#### \<instance> setForceComposite(value) {#instance-setforcecompositevalue}


**说明:**

设置此摄像机的 `forceComposite` 属性。 此属性仅供 WebGL 渲染器使用。 如果 `true` , 摄像机会通过帧缓冲器渲染, 并提供给其他 WebGL 系统 。

**标签:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 设置属性的值 。 |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1144](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1144)  
引入版本：4.0.0


---

### setIsSceneCamera {#setIsSceneCamera}

#### \<instance> setIsSceneCamera(value) {#instance-setisscenecameravalue}


**说明:**

设定此摄像机是否被用作场景摄像机(默认), 或用于渲染纹理的纹理摄像机 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 这是作为场景摄像机还是纹理摄像机? |


> 源码：[src/cameras/2d/BaseCamera.js#L1559](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1559)  
引入版本：3.60.0


---

### setMask {#setMask}

#### \<instance> setMask(mask, [fixedPosition]) {#instance-setmaskmask-fixedposition}


**说明:**

设定在渲染过程中要应用到此摄像机上的遮罩 。

遮罩必须是以前创建的, 而且必须是几何遮罩。 这只在 Canvas 渲染器中有效。 在 WebGL 中, 改用一个 Mask 过滤器( 见 [Phaser.GameObjects.Components.FilterList#addMask](/api/class/gameobjects-components-filterlist#addMask)) 。

如果这个摄像机上已经装了遮罩,它将被立即替换。

遮罩对物理或输入检测没有影响。 它们是纯粹的渲染组件, 允许您限制在渲染传出时可见的东西 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| mask | [Phaser.Display.Masks.GeometryMask](/api/class/display-masks-geometrymask) | 否 |  | 摄像机在渲染时会用的遮罩 |
| fixedPosition | boolean | 是 | true | 遮罩应该与摄像机一起翻译,还是固定在原位,不受摄像机变形的影响? |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1439](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1439)  
引入版本：3.17.0


---

### setName {#setName}

#### \<instance> setName([value]) {#instance-setnamevalue}


**说明:**

设置此摄像机的名称。 此值是用于您自己, 而非内部使用 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | string | 是 | "''" | 摄像机名称. |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1190](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1190)  
引入版本：3.0.0


---

### setOrigin {#setOrigin}

#### \<instance> setOrigin([x], [y]) {#instance-setoriginx-y}


**说明:**

设定此摄像机的旋转源 。

数值在0到1之间给出,仅在计算摄像机旋转时使用.

默认情况下,摄像机会围绕视港中心旋转.

更改源头允许您调整旋转所在的视口。 0 值将从视口左上旋转。 1 值从右下旋转。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0.5 | 水平源值 。 |
| y | number | 是 | "x" | 垂直源值。 如果定义不明确, 则将设定为 `x` 值 。 |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L607](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L607)  
引入版本：3.11.0


---

### setPosition {#setPosition}

#### \<instance> setPosition(x, [y]) {#instance-setpositionx-y}


**说明:**

设定游戏中摄像机视门的位置.

这不会改变摄像机的“外观”位置。请参见 `setScroll`来控制它。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 镜头视门左上角的x坐标. |
| y | number | 是 | "x" | 摄像机的左上角坐标 |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1210](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1210)  
引入版本：3.0.0


---

### setRotation {#setRotation}

#### \<instance> setRotation([value]) {#instance-setrotationvalue}


**说明:**

设定此摄像机的旋转。 这会导致它显示的所有旋转 。

旋转摄像机不旋转视门本身,在渲染时应用.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 0 | 摄像机的旋转,用弧度表示. |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1233](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1233)  
引入版本：3.0.0


---

### setRoundPixels {#setRoundPixels}

#### \<instance> setRoundPixels(value) {#instance-setroundpixelsvalue}


**说明:**

摄像机圆像素在渲染游戏对象时, 是否应该对整数进行数值 ?

在某些类型的游戏中,特别是用像素艺术,这需要防止子像素别名.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | `true`到圆摄像机像素,`false`到不. |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1254](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1254)  
引入版本：3.0.0


---

### setScene {#setScene}

#### \<instance> setScene(scene, [isSceneCamera]) {#instance-setscenescene-isscenecamera}


**说明:**

设定摄像机的场景

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 镜头的场景是注定的。 |
| isSceneCamera | boolean | 是 | true | 这摄像机是用来拍摄场景还是纹理? (假) |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1273](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1273)  
引入版本：3.0.0


---

### setScroll {#setScroll}

#### \<instance> setScroll(x, [y]) {#instance-setscrollx-y}


**说明:**

设定摄像机在游戏中查看的位置。 您也可以直接修改属性 `Camera.scrollX`和 `Camera.scrollY`。 使用这种方法或滚动属性将摄像机移动到游戏世界中 。

这不会改变摄像机的视门位置。 请参看 `setPosition` 来控制它 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 游戏世界中镜头的x坐标. |
| y | number | 是 | "x" | 游戏世界的摄像机的Y坐标. |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1307](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1307)  
引入版本：3.0.0


---

### setSize {#setSize}

#### \<instance> setSize(width, [height]) {#instance-setsizewidth-height}


**说明:**

设定摄像机视网的大小 。

默认一个摄像机与游戏大小相同,但可以通过这种方法变小,通过在游戏中创建和定位一个较小的摄像机视门,从而可以创建微型摄像机风格效果.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 否 |  | 摄像机视网的宽度. |
| height | number | 是 | "width" | 摄像机的高度 |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1332](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1332)  
引入版本：3.0.0


---

### setViewport {#setViewport}

#### \<instance> setViewport(x, y, width, [height]) {#instance-setviewportx-y-width-height}


**说明:**

这种方法将镜头视门的位置和大小设置在一个单调中.

如果你想改变镜头在游戏中的位置, 那就看`Camera.setScroll`的方法。这个方法是为了改变视门本身,而不是摄像机可以看到的。

默认一个摄像机与游戏大小相同,但可以通过这种方法变小,通过在游戏中创建和定位一个较小的摄像机视门,从而可以创建微型摄像机风格效果.

请注意,这是一种有限的方法,并附有若干告诫:

- 视点是一个轴向相交矩形,不能旋转.

- 如果视门改变,过滤器和遮罩可能会出现在错误的地方.

使用 `RenderTexture` 或 `DynamicTexture` 来代替它, 效果更强大、更可靠。 将摄像机瞄准要查看的视点, 设定其大小, 然后绘制游戏对象到它 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 镜头视门左上角的x坐标. |
| y | number | 否 |  | 摄像机的左上角坐标 |
| width | number | 否 |  | 摄像机视网的宽度. |
| height | number | 是 | "width" | 摄像机的高度 |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1357](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1357)  
引入版本：3.0.0


---

### setVisible {#setVisible}

#### \<instance> setVisible(value) {#instance-setvisiblevalue}


**说明:**

设定此摄像机的可见度 。

一个隐形的摄像机会跳过 渲染和输入测试 它可以看到的一切。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 摄像机的可见状态. |


**重写:** Phaser.GameObjects.Components.Visible#setVisible


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1494](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1494)  
引入版本：3.10.0


---

### setZoom {#setZoom}

#### \<instance> setZoom([x], [y]) {#instance-setzoomx-y}


**说明:**

设定摄像机的缩放值 。

更改到一个较小的值, 如 0. 0, 会导致摄像机“ zoom out ” 。 更改到一个较大的值, 如 2 , 将导致摄像机“ zoom in ” 。

1 的值表示“ 无缩放 ” , 并是默认值 。

改变缩放不会以任何方式影响摄像机视门,只在渲染时才应用.

至Phaser 3.50,现在可以独立设置水平和垂直缩放值.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 1 | 摄像机的横向放大值,最小可以是0.001. |
| y | number | 是 | "x" | 摄像机的垂直缩放值,最小可以是0.001. |


**返回值:** [Phaser.Cameras.Scene2D.BaseCamera](/api/class/cameras-scene2d-basecamera) - 这个镜头的例子。


> 源码：[src/cameras/2d/BaseCamera.js#L1398](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1398)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

返回一个适合 JSON 存储的对象,其中包含所有摄像机视图和渲染属性 。


**返回值:** [Phaser.Types.Cameras.Scene2D.JSONCamera](/api/typedef/types-cameras-scene2d#jsoncamera) - 适合转换为JSON的造型良好的对象.


> 源码：[src/cameras/2d/BaseCamera.js#L1507](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1507)  
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


> 源码：[src/cameras/2d/BaseCamera.js#L1544](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cameras/2d/BaseCamera.js#L1544)  
引入版本：3.0.0


---

---
