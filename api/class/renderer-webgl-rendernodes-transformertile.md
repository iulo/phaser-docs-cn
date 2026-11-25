# TransformerTile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-transformertile)

一个处理 TilemapLayer 内单塔的变换数据的RenderNode 。

此节点以瓦片特定逻辑延伸 `TransformerImage`, 包括支持瓦片的抵消, 每瓦翻转旗, 以及每瓦旋转。 它被TilemapLayer 渲染管道用于在世界空间中定位和定位每个单片, 然后再提交批量渲染器 。

与在独立游戏对象上运行的`TransformerImage`不同,这个节点读取了来自一个瓦片元素描述符(`element`)而非直接来自游戏对象的位置和翻转数据,使其可以处理在单个渲染传中构成一个单TilemapLayer的很多瓷片.

**构造函数**

`new TransformerTile(manager, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | object | 是 | 此 RenderNode 的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.TransformerImage](/api/class/renderer-webgl-rendernodes-transformerimage)  



> 源码：[src/renderer/webgl/renderNodes/transformer/TransformerTile.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/transformer/TransformerTile.js#L10)  
引入版本：4.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(drawingContext, gameObject, texturerNode, [parentMatrix], [element]) {#instance-rundrawingcontext-gameobject-texturernode-parentmatrix-element}


**说明:**

计算并存储用于单一瓦片元素的世界空间变换四元,准备提交批量渲染器.

这种方法通过将摄像机视图矩阵(应用滚动因子),嵌入游戏对象的可选母矩阵,以及从瓦片的像素位置,旋转,以及TilemapLayer的尺度中衍生出来的每片图案矩阵相结合,来构建最终的转换. 蒂勒塞特的瓦片抵消被计入世界位置,通过否定四维来应用水平或垂直的翻转. 如果在摄像机上启用顶点圆形,则产生的四位坐标被四舍入到最近的整数,以避免子像素渲染文物.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象正在被渲染 。 |
| texturerNode | [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode) | 否 | 用于为 Game Object 纹理的文本器节点。 此节点包含关于对象尺寸的相关数据 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 如果游戏对象是嵌入式,则定义了这个变换矩阵. |
| element | object | 是 | 正在渲染的瓦片的瓦片元素描述符。 包含瓦片的像素位置、 旋转、 翻转旗子以及用于查找瓦片的 GID 索引 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.TransformerImage#运行


> 源码：[src/renderer/webgl/renderNodes/transformer/TransformerTile.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/transformer/TransformerTile.js#L45)  
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
