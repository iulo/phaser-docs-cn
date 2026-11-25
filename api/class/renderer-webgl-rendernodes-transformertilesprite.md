# TransformerTileSprite {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-transformertilesprite)

一个RenderNode,它计算和存储了制作TileSprite Game Object所需的世界空间变换数据.

此类扩展了 `TransformerImage` , 关键区别是: `TransformerImage` 是从纹理帧中获取四维的, 而 `TransformerTileSprite` 直接从 Game Object 的 `width` 和 `height` 属性中读取它们。 这样做是必要的, 因为 TileSprite 的任意大小独立于其底部的瓦质纹理 。

在其`run`呼叫中,节点构建了摄像机和喷射变换矩阵(计算滚动因子,可选母矩阵,旋转,尺度,翻转),将Game Object的四角线设定为屏幕空间,并可选地将所产生的顶点进行精密像素对齐渲染。产生的四角坐标存储在`this.quad`上,供下游的变换节点(如纹理器和批量器节点)在同一渲染通道中使用。

**构造函数**

`new TransformerTileSprite(manager, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | object | 是 | 此 RenderNode 的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.TransformerImage](/api/class/renderer-webgl-rendernodes-transformerimage)  



> 源码：[src/renderer/webgl/renderNodes/transformer/TransformerTileSprite.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/transformer/TransformerTileSprite.js#L10)  
引入版本：4.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(drawingContext, gameObject, [texturerNode], [parentMatrix], [element]) {#instance-rundrawingcontext-gameobject-texturernode-parentmatrix-element}


**说明:**

计算一个TileSprite Game Object的屏幕-空间四角,并将其存储在`this.quad`中,供下游的渲染节点使用.

该方法读取Game Object自己的`width`和`height`(而不是帧维度),应用显示源偏移,处理水平和垂直翻转,然后从摄像机视图,可选母矩阵,以及图样本身的位置,旋转,和尺度构建一个合并的变换矩阵. 由此得出的四个角坐标被写成`this.quad`,如果此Game Object和摄像机组合需要顶点圆,则以像素圆表示.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象正在被渲染 。 |
| texturerNode | [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode) | 是 | 用于为游戏对象纹理的文本器节点。 此节点包含对象尺寸的相关数据。 此处未使用 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 如果游戏对象是嵌入式,则定义了这个变换矩阵. |
| element | object | 是 | 游戏对象中的特定元素。 用于由多个四位元组成的对象, 这里没有使用 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.TransformerImage#运行


> 源码：[src/renderer/webgl/renderNodes/transformer/TransformerTileSprite.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/transformer/TransformerTileSprite.js#L50)  
引入版本：4.0.0


---

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)





**From [Phaser.Renderer.WebGL.RenderNodes.TransformerImage](/api/class/renderer-webgl-rendernodes-transformerimage):**


 - [quad](/api/class/renderer-webgl-rendernodes-transformerimage#quad)




---

---
