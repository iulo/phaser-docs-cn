# FillCamera {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-fillcamera)

一个RenderNode,它将一个照摄像机的视门填充到一个坚固的颜色,用来在绘制任何游戏对象之前渲染一个照摄像机的背景颜色.

在WebGL渲染管道中,每当摄像机有背景颜色集时,都会引用这个节点。它将实际绘制的图像代表给`FillRect` RenderNode,这意味着填充是作为批量四重奏而不是单独拨打,保持高效。

对于向帧缓冲器(resource textures)渲染的摄像机,镜头的屏幕位置被忽略,填充则在帧缓冲器的起源处绘制,因为帧缓冲器本身会在正确位置被合成成主场景.

**构造函数**

`new FillCamera(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/FillCamera.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/FillCamera.js#L10)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### fillRectNode {#fillRectNode}

#### fillRectNode: [Phaser.Renderer.WebGL.RenderNodes.FillRect](/api/class/renderer-webgl-rendernodes-fillrect) {#fillrectnode-phaserrendererwebglrendernodesfillrect}


**说明:**

绘制填充矩形的RenderNode 。


> 源码：[src/renderer/webgl/renderNodes/FillCamera.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/FillCamera.js#L39)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(drawingContext, color, [isFramebufferCamera]) {#instance-rundrawingcontext-color-isframebuffercamera}


**说明:**

用颜色填充摄像机。 这使用 `FillRect`, 所以它与其他的四角组进行批量 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 目前使用的上下文 。 |
| color | number | 否 | 以色充摄. |
| isFramebufferCamera | boolean | 是 | 此摄像机是否向帧缓冲器渲染? 如果是这样, 摄像机位置将不会被应用, 假设摄像机位置将被用于在外部上下文中定位帧缓冲器 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/FillCamera.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/FillCamera.js#L49)  
引入版本：4.0.0


---

---
