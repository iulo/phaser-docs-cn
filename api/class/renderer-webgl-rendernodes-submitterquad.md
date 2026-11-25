# SubmitterQuad {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-submitterquad)

提交者Quad RenderNode 提交数据以渲染一个像图像一样的游戏对象。它使用一个批量的手提箱来渲染图像。

此节点接收绘图上下文、 游戏对象和父矩阵。 也可以接收引用它的节点的文本器、 线条和变压器节点。 这样就可以通过在 Game Object 上为单个调幅设置适当的节点, 或者在为全局变化引用的 Render 节点来配置行为 。

**构造函数**

`new SubmitterQuad(manager, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | [Phaser.Types.Renderer.WebGL.RenderNodes.SubmitterQuadConfig](/api/typedef/types-renderer-webgl-rendernodes#submitterquadconfig) | 是 | 此 RenderNode 的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterQuad.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterQuad.js#L14)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### batchHandler {#batchHandler}

#### batchHandler: string {#batchhandler-string}


**说明:**

用于渲染数据的 RenderNode 密钥 。


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterQuad.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterQuad.js#L43)  
引入版本：4.0.0


---

### defaultConfig {#defaultConfig}

#### defaultConfig: [Phaser.Types.Renderer.WebGL.RenderNodes.SubmitterQuadConfig](/api/typedef/types-renderer-webgl-rendernodes#submitterquadconfig) {#defaultconfig-phasertypesrendererwebglrendernodessubmitterquadconfig}


**说明:**

此 Render 节点的默认配置 。


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterQuad.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterQuad.js#L85)  



---

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(drawingContext, gameObject, parentMatrix, element, texturerNode, transformerNode, [tinterNode], [normalMap], [normalMapRotation]) {#instance-rundrawingcontext-gameobject-parentmatrix-element-texturernode-transformernode-tinternode-normalmap-normalmaprotation}


**说明:**

处理给定的 Game Object 并提交四顶点数据给相应的批处理器进行渲染。 这种方法会引用文本器、 变压器和可选的锡器节点, 以计算纹理坐标、 变形顶点位置和锡色。 如果不提供锡器节点, 就直接从 Game Objector 读取图像风格的锡器。 然后调用 `setRenderOptions` 来解析照明和光滑像素艺术设置, 然后将所有组装的数据传递给批处理器 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象正在被渲染 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | Game Object 的母矩阵 。 |
| element | object | 否 | 游戏对象中的特定元素。 用于由多个四角组成的对象 。 |
| texturerNode | [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode) | 否 | 用于为游戏对象纹理的文本器节点。 您可以通过一个文本器图像节点, 或者一个包含等效数据的对象, 而不使用 `run` 方法 。 |
| transformerNode | [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode) \| Object | 否 | 变压器节点用来转换 Game Object。 您可以通过变压器节点或带有 `quad` 属性的物体 。 |
| tinterNode | [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode), Omit.\<[Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode), 'run'> | 是 | 用于给游戏对象点缀的锡条节点。 您可以通过一个锡条节点或包含等效数据的对象, 而无需使用 `run` 方法。 如果省略, 将使用图像式的锡条 。 |
| normalMap | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 是 | 照明所用的普通地图纹理。 如果省略, 将使用游戏对象的普通地图纹理, 或者默认的普通地图纹理 。 |
| normalMapRotation | number | 是 | 普通地图纹理的旋转。 如果省略, 将使用 Game Object 的旋转 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterQuad.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterQuad.js#L97)  
引入版本：4.0.0


---

### setRenderOptions {#setRenderOptions}

#### \<instance> setRenderOptions(gameObject, [normalMap], [normalMapRotation]) {#instance-setrenderoptionsgameobject-normalmap-normalmaprotation}


**说明:**

解析并存储当前游戏对象的选项 `_renderOptions` 包括确定正确的普通地图纹理和照明旋转( 返回游戏对象的基础纹理数据源, 然后是渲染器默认的正常纹理) , 解决自阴影设置( 如果未设定在对象上的话 ) , 以及 从基本纹理或全球游戏配置中确定平滑的像素艺术设置 。 如果游戏对象没有照明组件, 则设定照明选项为 `null`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象正在被渲染 。 |
| normalMap | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 是 | 照明所用的普通地图纹理。 如果省略, 将从游戏对象的基础纹理数据源或渲染器默认的正常纹理中解析 。 |
| normalMapRotation | number | 是 | 一般地图纹理的旋转, 以弧度表示。 如果省略或`NaN`, 则它会从游戏对象的旋转或属于容器的世界变换矩阵中解决 。 |


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterQuad.js#L203](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterQuad.js#L203)  
引入版本：4.0.0


---

---
