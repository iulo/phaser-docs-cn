# GeometryMask {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/display-masks-geometrymask)

几何面具可以应用到游戏对象上,隐藏其中任何不会从几何面具上交叉可见像素的像素,面具本质上是剪辑路径,只能使面具完全可见或完全看不见,而不会改变其α(不透明).

一个几何面具使用图形游戏对象来决定被遮盖的游戏对象的哪些像素应该被剪辑。对于一个被遮盖的游戏物体的纹理的任何特定点,只有图形游戏对象的几何面具在同一位置具有可见像素,才会显示像素。来自几何面具的像素的颜色和α并不重要。

几何面具的位置与其图形对象的位置相符,而不是其遮盖对象的位置。移动或转换隐藏的图形对象会改变遮盖(并影响任何遮盖对象的能见度),而移动或转换遮盖对象不会影响遮盖。你可以将几何面具(或更确切地说,其图形对象)视为一个隐形幕,放置在所有遮盖对象面前,这些遮盖对象具有自己的视觉特性,自然尊重相机的视觉特性,但不会受到自己的影响,也不会跟随遮盖对象。

几何mask只在 Canvas 渲染器中支持。 如果您想要使用几何来遮盖 WebGL 中的对象, 请参见 [Phaser.GameObjects.Components.FilterList#addMask](/api/class/gameobjects-components-filterlist#addMask) 。

**构造函数**

`new GeometryMask(scene, graphicsGeometry)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此参数未使用 。 |
| graphicsGeometry | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 用于几何遮罩的图形游戏对象。 不需要在显示列表中 。 |

---


**作用域**: static

> 源码：[src/display/mask/GeometryMask.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/mask/GeometryMask.js#L9)  
引入版本：3.0.0

## 公开成员 {#public-members}

### geometryMask {#geometryMask}

#### geometryMask: [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) {#geometrymask-phasergameobjectsgraphics}


**说明:**

描述几何面具的图形对象。


> 源码：[src/display/mask/GeometryMask.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/mask/GeometryMask.js#L45)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁此几何掩码并取消它持有的任何引用 。

请注意, 如果游戏对象目前使用此掩码, 它会_ not_ 自动检测您已经销毁了它, 所以在销毁它之前, 请在任何使用它的游戏对象上拨打 `clearMask` 。


> 源码：[src/display/mask/GeometryMask.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/mask/GeometryMask.js#L106)  
引入版本：3.7.0


---

### postRenderCanvas {#postRenderCanvas}

#### \<instance> postRenderCanvas(renderer) {#instance-postrendercanvasrenderer}


**说明:**

恢复画布上下文之前的剪辑路径,从而关闭了它的遮罩.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) | 否 | 坎瓦斯兰德雷克案正在恢复 |


> 源码：[src/display/mask/GeometryMask.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/mask/GeometryMask.js#L93)  
引入版本：3.0.0


---

### preRenderCanvas {#preRenderCanvas}

#### \<instance> preRenderCanvas(renderer, mask, camera) {#instance-prerendercanvasrenderer-mask-camera}


**说明:**

设置2D画布上下文的剪切路径到几何遮盖的图形对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) | 否 | 坎瓦斯的变形器实例 来设定剪辑路径 。 |
| mask | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 正在渲染游戏对象 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 正在通过游戏对象的相机。 |


> 源码：[src/display/mask/GeometryMask.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/mask/GeometryMask.js#L72)  
引入版本：3.0.0


---

### setShape {#setShape}

#### \<instance> setShape(graphicsGeometry) {#instance-setshapegraphicsgeometry}


**说明:**

为几何遮罩设置新的图形对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| graphicsGeometry | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) | 否 | 用于几何遮罩的图形对象。 |


**返回值:** [Phaser.Display.Masks.GeometryMask](/api/class/display-masks-geometrymask) - 此几何面罩


> 源码：[src/display/mask/GeometryMask.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/mask/GeometryMask.js#L55)  
引入版本：3.0.0


---

---
