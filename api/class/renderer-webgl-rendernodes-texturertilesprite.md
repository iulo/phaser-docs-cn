# TexturerTileSprite {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-texturertilesprite)

处理单一 TileSprite 游戏对象的纹理的 RenderNode 。

与标准图示文本器不同,此节点计算出一个紫外线变换矩阵,它能说明蒂勒斯普里特的瓦片位置,瓦片尺度,以及瓦片旋转,使纹理能够与Game Object的自身变换独立滚动,缩放,旋转,它存储了由此产生的帧数据和紫外线矩阵,以便在这个节点被重新使用之前被后续的渲染节点所消耗.

**构造函数**

`new TexturerTileSprite(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/texturer/TexturerTileSprite.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/texturer/TexturerTileSprite.js#L11)  
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


> 源码：[src/renderer/webgl/renderNodes/texturer/TexturerTileSprite.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/texturer/TexturerTileSprite.js#L36)  
引入版本：4.0.0


---

### uvMatrix {#uvMatrix}

#### uvMatrix: [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) {#uvmatrix-phasergameobjectscomponentstransformmatrix}


**说明:**

内部使用矩阵计算紫外线坐标.


> 源码：[src/renderer/webgl/renderNodes/texturer/TexturerTileSprite.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/texturer/TexturerTileSprite.js#L45)  
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

将这个 RenderNode 以纹理数据覆盖给定的 TileSprite Game Object 。 将框架存储并计算紫外线变换矩阵, 按 动砖位置、 瓦片比例和瓦片旋转顺序进行 TSR 排序, 然后将结果映射到 Game Objects 显示区域 。 如果 Game Objee 被裁剪, 则首先更新裁剪的 UV , 以计及任何翻转状态变化 。 存储的数值必须先被消耗, 然后再重新使用此节点 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| gameObject | [Phaser.GameObjects.Image](/api/class/gameobjects-image) | 否 | 游戏对象正在被渲染 。 |
| element | object | 是 | 游戏对象中的特定元素。 用于由多个四位元组成的对象, 这里没有使用 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/texturer/TexturerTileSprite.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/texturer/TexturerTileSprite.js#L55)  
引入版本：4.0.0


---

---
