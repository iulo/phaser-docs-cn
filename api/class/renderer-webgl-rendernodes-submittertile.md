# SubmitterTile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-submittertile)

一个专门的RenderNode,将Sontenter Quad扩展为处理向WebGL批处理器提交瓦片渲染数据。它被Tilemap层内部用于制作单个瓦片。与底片Sontenter Quad不同的是,SontentterTile允许在渲染选项上进行帧夹击(`clampFrame = true`),防止相邻的瓷片之间出现纹理流血,这些瓷片共享一个瓦片纹理图集。

**构造函数**

`new SubmitterTile(manager, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有此提交器的 WebGLRenderer 。 |
| config | [Phaser.Types.Renderer.WebGL.RenderNodes.SubmitterQuadConfig](/api/typedef/types-renderer-webgl-rendernodes#submitterquadconfig) | 是 | 此提交器的配置对象。 这是带有“ 提交方” 的配置对象 `name` 默认为 `SubmitterTile`. |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.SubmitterQuad](/api/class/renderer-webgl-rendernodes-submitterquad)  



> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTile.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTile.js#L10)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)





**From [Phaser.Renderer.WebGL.RenderNodes.SubmitterQuad](/api/class/renderer-webgl-rendernodes-submitterquad):**


 - [batchHandler](/api/class/renderer-webgl-rendernodes-submitterquad#batchHandler)




---

## 公开成员 {#public-members}

### defaultConfig {#defaultConfig}

#### defaultConfig: [Phaser.Types.Renderer.WebGL.RenderNodes.SubmitterQuadConfig](/api/typedef/types-renderer-webgl-rendernodes#submitterquadconfig) {#defaultconfig-phasertypesrendererwebglrendernodessubmitterquadconfig}


**说明:**

此 Render 节点的默认配置 。


**重写:** Phaser.Renderer.WebGL.RenderNodes.SubmitterQuad#defaultConfig


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTile.js#L37](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTile.js#L37)  



---

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)





**From [Phaser.Renderer.WebGL.RenderNodes.SubmitterQuad](/api/class/renderer-webgl-rendernodes-submitterquad):**


 - [setRenderOptions](/api/class/renderer-webgl-rendernodes-submitterquad#setRenderOptions)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(drawingContext, gameObject, parentMatrix, element, texturerNode, transformerNode, [tinterNode], [normalMap], [normalMapRotation]) {#instance-rundrawingcontext-gameobject-parentmatrix-element-texturernode-transformernode-tinternode-normalmap-normalmaprotation}


**说明:**

向 WebGL 批处理器提交单瓦制成数据。 选择执行文本器、 变压器和锡器节点, 以解析纹理坐标、 变形四几何和每角的锡色。 如果没有提供锡器节点, 该瓦片将使用全白( 0xffffffffff) 颜色不进行加锡。 解析后的数据将传递给相应的批处理器, 以便提交 GPU 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象正在被渲染 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | Game Object 的母矩阵 。 |
| element | object | 否 | 游戏对象中的特定元素。 用于由多个四角组成的对象 。 |
| texturerNode | [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode) | 否 | 用于为游戏对象纹理的文本器节点。 您可以通过一个文本器TILESprite节点, 或者一个包含等效数据的对象, 而不使用 `run` 方法 。 |
| transformerNode | [Phaser.Renderer.WebGL.RenderNodes.TransformerTileSprite](/api/class/renderer-webgl-rendernodes-transformertilesprite) \| Object | 否 | 变压器节点用来转换 Game Object。 您可以通过变压器节点或带有 `quad` 属性的物体 。 |
| tinterNode | [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode), Omit.\<[Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode), 'run'> | 是 | 用于给游戏对象点注音的锡条节点。 您可以通过一个锡条节点或一个包含等效数据的对象, 而不使用 `run` 方法。 如果省略, 将不会使用锡条 。 |
| normalMap | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 是 | 照明所用的普通地图纹理。 如果省略, 将使用游戏对象的普通地图纹理, 或者默认的普通地图纹理 。 |
| normalMapRotation | number | 是 | 普通地图纹理的旋转。 如果省略, 将使用 Game Object 的旋转 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.SubmitterQuad#运行


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTile.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTile.js#L49)  
引入版本：4.0.0


---

---
