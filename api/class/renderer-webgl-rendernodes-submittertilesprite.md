# SubmitterTileSprite {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-submittertilesprite)

提交器TileSprite RenderNode 提交数据以渲染一个单独的TileSprite Game Object。它使用一个BatchHandler来将TileSprite制成一个批件的一部分 。

此节点接收绘图上下文、 游戏对象和父矩阵。 也可以接收引用它的节点的文本器、 线条和变压器节点。 这样就可以通过在 Game Object 上为单个调幅设置适当的节点, 或者在为全局变化引用的 Render 节点来配置行为 。

**构造函数**

`new SubmitterTileSprite(manager, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | [Phaser.Types.Renderer.WebGL.RenderNodes.SubmitterQuadConfig](/api/typedef/types-renderer-webgl-rendernodes#submitterquadconfig) | 是 | 此提交器的配置对象。 这是带有“ 提交方” 的配置对象 `name` 默认为 `SubmitterTileSprite`. |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.SubmitterQuad](/api/class/renderer-webgl-rendernodes-submitterquad)  



> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTileSprite.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTileSprite.js#L13)  
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


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.SubmitterQuad#defaultConfig


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTileSprite.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTileSprite.js#L43)  



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

向适当的批量处理器提交单端晶体游戏对象的顶点、纹理和锡金数据 WebGL 渲染。这种方法将文本器、变压器和锡器节点按顺序引用,以填充所需的渲染数据,然后将其连同紫外线矩阵四进制片器一起传递给批处理器,用于瓦片滚动和包扎,以及任何照明选项,包括适用于普通地图的瓦片旋转。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象正在被渲染 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | Game Object 的母矩阵 。 |
| element | object | 否 | 游戏对象中的特定元素。 用于由多个四角组成的对象 。 |
| texturerNode | [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode) | 否 | 用于为游戏对象纹理的文本器节点。 您可以通过一个文本器TILESprite节点, 或者一个包含等效数据的对象, 而不使用 `run` 方法 。 |
| transformerNode | [Phaser.Renderer.WebGL.RenderNodes.TransformerTileSprite](/api/class/renderer-webgl-rendernodes-transformertilesprite) \| Object | 否 | 变压器节点用来转换 Game Object。 您可以通过变压器节点或带有 `quad` 属性的物体 。 |
| tinterNode | [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode), Omit.\<[Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode), 'run'> | 是 | 用于给游戏对象点缀的锡条节点。 您可以通过一个锡条节点或包含等效数据的对象, 而无需使用 `run` 方法。 如果省略, 将使用图像式的锡条 。 |
| normalMap | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 是 | 照明所用的普通地图纹理。 如果省略, 将使用游戏对象的普通地图纹理, 或者默认的普通地图纹理 。 |
| normalMapRotation | number | 是 | 普通地图纹理的旋转。 如果省略, 将使用 Game Object 的旋转 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.SubmitterQuad#运行


> 源码：[src/renderer/webgl/renderNodes/submitter/SubmitterTileSprite.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/SubmitterTileSprite.js#L55)  
引入版本：4.0.0


---

---
