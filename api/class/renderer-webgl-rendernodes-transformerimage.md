# TransformerImage {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-transformerimage)

一个RenderNode,每次渲染时会为一个像图像一样的游戏对象计算和存储屏幕-空间四极顶点位置.

其间 `run` 调用,此节点将摄像机视图矩阵(根据游戏对象的滚动因子调整),任何父容器矩阵,以及游戏对象自身的位置,旋转,和比例化为单一的最终变换矩阵。然后通过该矩阵将游戏对象框的四个角投影,并将由此生成的八个坐标值(4 x/y 配对)写入到 `quad` Float32Array,准备由后续的提交器节点消耗.

横向和纵向翻转在此处理,当帧不使用自定义的枢轴时,会自动调整本地源头. Vertex 圆环在游戏对象或摄像机设置需要时也会应用,将所有四角都按整数像素坐标来进行曲折,以避免子像素渲染手工艺品.

**构造函数**

`new TransformerImage(manager, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | object | 是 | 此 RenderNode 的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/transformer/TransformerImage.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/transformer/TransformerImage.js#L12)  
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

平面阵列8个浮点,存储已变形四角的屏幕-空间位置,每次`run`呼叫时都会写上。数值顺序为 [x0] y0, x1, y1, x2, y2, x3, y3], 分别代表上左、 上右、 下左和下右角。


> 源码：[src/renderer/webgl/renderNodes/transformer/TransformerImage.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/transformer/TransformerImage.js#L48)  
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

计算给定的图像类游戏对象的最终屏幕-空间四极顶点位置,并将其存储在`this.quad`中.

该方法通过合并摄像机视图矩阵(由游戏对象的滚动因子修改),可选父容器矩阵,以及游戏对象自身的位置,旋转,和尺度来构建完整的转换. 水平和垂直翻转通过否定相关比例轴来进行考虑,当帧不使用自定义的偏转时,通过调整本地源来抵消图像绕过显示源的翻转,由此形成的四个角位置通过矩阵通过`setQuad`进行预测,并写入`this.quad`. 如果需要进行顶点圆,则所有八个值都会在节点退出前被截断到最近的整数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象正在被渲染 。 |
| texturerNode | [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode) | 否 | 用于为 Game Object 纹理的文本器节点。 此节点包含关于对象尺寸的相关数据 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 如果游戏对象是嵌入式,则定义了这个变换矩阵. |
| element | object | 是 | 游戏对象中的特定元素。 用于由多个四位元组成的对象, 这里没有使用 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/transformer/TransformerImage.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/transformer/TransformerImage.js#L86)  
引入版本：4.0.0


---

---
