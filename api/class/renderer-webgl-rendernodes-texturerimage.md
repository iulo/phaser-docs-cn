# TexturerImage {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-texturerimage)

一个处理像图像一样的单一游戏对象的纹理的RenderNode,例如图像或Sprite.

在WebGL渲染管道中,这个节点被调用来提取和临时缓存渲染Game Object所需的纹理数据:其帧参考,UV源,以及显示维度. 它通过切换到作物的紫外坐标和调整维度来计算被裁剪的Game Objects,并通过帧源的分辨率来缩放所有维度,以便上游批量器接收设备独立的像素值.

由于这个节点可能在单一的帧内跨多个Game Objects重复使用,呼叫者必须消耗其存储值(通过 `frame`, `frameWidth`, `frameHeight`,和 `uvSource`) 下个 `run` 呼叫覆盖它们。

**构造函数**

`new TexturerImage(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/texturer/TexturerImage.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/texturer/TexturerImage.js#L10)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### frame {#frame}

#### frame: [Phaser.Textures.Frame](/api/class/textures-frame) {#frame-phasertexturesframe}


**说明:**

正在渲染的 Game Object 的框架数据 。


> 源码：[src/renderer/webgl/renderNodes/texturer/TexturerImage.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/texturer/TexturerImage.js#L40)  
引入版本：4.0.0


---

### frameHeight {#frameHeight}

#### frameHeight: number {#frameheight-number}


**说明:**

分辨率调整像素中框的显示高度。这反映了Game Object被裁剪时的裁剪高度,并被帧源的分辨率除以,为渲染器生成设备独立的像素值。


> 源码：[src/renderer/webgl/renderNodes/texturer/TexturerImage.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/texturer/TexturerImage.js#L61)  
引入版本：4.0.0


---

### frameWidth {#frameWidth}

#### frameWidth: number {#framewidth-number}


**说明:**

分辨率调整像素中框的显示宽度。这反映了Game Object被裁剪时的裁剪宽度,并被帧源的分辨率除以,为渲染器生成设备独立的像素值。


> 源码：[src/renderer/webgl/renderNodes/texturer/TexturerImage.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/texturer/TexturerImage.js#L49)  
引入版本：4.0.0


---

### uvSource {#uvSource}

#### uvSource: [Phaser.Textures.Frame](/api/class/textures-frame), [Phaser.GameObjects.Components.Crop](/api/namespace/gameobjects-components-crop) {#uvsource-phasertexturesframe-phasergameobjectscomponentscrop}


**说明:**

紫外线坐标和帧坐标存储对象。 无论是框架还是裁剪对象 。

它应该有属性u0,v0,u1,v1,x,y.


> 源码：[src/renderer/webgl/renderNodes/texturer/TexturerImage.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/texturer/TexturerImage.js#L73)  
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

#### \<instance> run(drawingContext, gameObject, [element]) {#instance-rundrawingcontext-gameobject-element}


**说明:**

以成像给定的游戏对象所需的纹理数据来复制此 RenderNode 。

此方法解决了Game Object的正确紫外线源: 如果它没有被裁剪,则使用框架本身; 如果它被裁剪, 则使用作物对象, 当翻转状态改变时, 其紫外线会重新计算。 框架维度被设定为裁剪时的裁剪维度。 在这两种情况下, 所产生的维度都由框架源的分辨率来分割, 以生成设备独立的像素值 。

存储值( Q)`frame`, `frameWidth`, `frameHeight`, `uvSource`)必须在这个节点再次运行之前消耗,因为下次呼叫时会覆盖它们.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| gameObject | [Phaser.GameObjects.Image](/api/class/gameobjects-image) | 否 | 游戏对象正在被渲染 。 |
| element | object | 是 | 游戏对象中的特定元素。 用于由多个四位元组成的对象, 这里没有使用 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/texturer/TexturerImage.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/texturer/TexturerImage.js#L86)  
引入版本：4.0.0


---

---
