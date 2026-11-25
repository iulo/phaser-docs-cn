# TransformerStamp {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-transformerstamp)

一个RenderNode,它为一个像邮票的游戏对象计算和存储世界空间四角圆顶,例如一个没有受到相机变换影响的直接进入世界空间的Samp或类似对象.

这是`TransformerImage` RenderNode的修改版。 与 `TransformerImage` 不同的是, 这个节点完全跳过相机矩阵乘法, 意思是 产生的四位坐标位于世界空间而不是相机投影屏幕空间。 这使得它适合管理自己世界对屏幕定位的物体, 如 Stamp Game Object 。

在`run`呼叫中,节点应用Game Object的位置,旋转,尺度,翻转,以及显示源来计算已渲染的四角四角最后的顶点,将其存储在`quad` Float32Array中. Vertex 圆环也酌情应用,以防止子像素渲染工艺品.

**构造函数**

`new TransformerStamp(manager, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | object | 是 | 此 RenderNode 的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/transformer/TransformerStamp.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/transformer/TransformerStamp.js#L12)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### quad {#quad}

#### quad: Float32Array {#quad-float32array}


**说明:**

浮图32 箭头,包含变形四角的八个顶点坐标(x,y对),在`run`期间写成,并被后续的渲染器节点消耗,以绘制游戏对象.


> 源码：[src/renderer/webgl/renderNodes/transformer/TransformerStamp.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/transformer/TransformerStamp.js#L57)  
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

#### \<instance> run(drawingContext, gameObject, texturerNode, [parentMatrix], [element]) {#instance-rundrawingcontext-gameobject-texturernode-parentmatrix-element}


**说明:**

为给定的像邮票的游戏对象计算世界空间四极顶点,并将其存储在`quad` Float32箭头中,供随后的节点使用。此计算中故意排除了相机矩阵。

这种方法解决了帧偏移和显示源到本地空间角坐标,应用水平和垂直翻转(在未设定自定义枢轴时调整偏移),然后从Game Object的位置,旋转和比例构建图案变换矩阵. 四个角顶点通过矩阵通过`setQuad`进行预测,当需要顶点圆形时,每个坐标被绕到最近的整数,以避免子像素渲染工艺品.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象正在被渲染 。 |
| texturerNode | [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode) | 否 | 用于为 Game Object 纹理的文本器节点。 此节点包含关于对象尺寸的相关数据 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 如果游戏对象被嵌入, 此变换矩阵将定义。 此处没有使用 。 |
| element | object | 是 | 游戏对象中的特定元素。 用于由多个四位元组成的对象, 这里没有使用 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/transformer/TransformerStamp.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/transformer/TransformerStamp.js#L74)  
引入版本：4.0.0


---

---
