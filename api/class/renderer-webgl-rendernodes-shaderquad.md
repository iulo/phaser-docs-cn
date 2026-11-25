# ShaderQuad {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-shaderquad)

一个使用自定义的 GLSL 阴影程序使一个四边形实现一个单一的RenderNode。它被Shader Game Object 用来执行用户定义的顶点和碎片阴影,与游戏对象的维度匹配的四边形。该四边形通过场景相机转换,并支持可选渲染直接通过纹理 `renderToTexture`。通过这个节点管理了遮蔽器、纹理取样器和遮蔽器的添加变体,使其成为定制的主要切入点。 WebGL 阴影效果在 Phaser.

**构造函数**

`new ShaderQuad(manager, config)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |
| config | [Phaser.Types.GameObjects.Shader.ShaderQuadConfig](/api/typedef/types-gameobjects-shader#shaderquadconfig) | 否 | 此 RenderNode 的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/ShaderQuad.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/ShaderQuad.js#L15)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### _texturerProxy {#_texturerProxy}

#### _texturerProxy: object {#_texturerproxy-object}


**说明:**

用于在变压器中进行纹理的代理对象。


> 源码：[src/renderer/webgl/renderNodes/ShaderQuad.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/ShaderQuad.js#L130)  
引入版本：4.0.0


---

### indexBuffer {#indexBuffer}

#### indexBuffer: [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) {#indexbuffer-phaserrendererwebglwrapperswebglbufferwrapper}


**说明:**

索引缓冲定义顶点顺序.


> 源码：[src/renderer/webgl/renderNodes/ShaderQuad.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/ShaderQuad.js#L59)  
引入版本：4.0.0


---

### programManager {#programManager}

#### programManager: [Phaser.Renderer.WebGL.ProgramManager](/api/class/renderer-webgl-programmanager) {#programmanager-phaserrendererwebglprogrammanager}


**说明:**

程序管理器用来创建和管理遮荫程序。 包含遮荫变体 。


> 源码：[src/renderer/webgl/renderNodes/ShaderQuad.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/ShaderQuad.js#L84)  
引入版本：4.0.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrendererwebglwebglrenderer}


**说明:**

正在使用的 WebGLRender.


> 源码：[src/renderer/webgl/renderNodes/ShaderQuad.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/ShaderQuad.js#L43)  
引入版本：4.0.0


---

### setUniform {#setUniform}

#### setUniform: function {#setuniform-function}


**说明:**

绑定的便利函数,将一个要应用到当前阴影程序的一致值排队。 程序管理器的代表 `setUniform` 方法。 。 方法。


> 源码：[src/renderer/webgl/renderNodes/ShaderQuad.js#L110](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/ShaderQuad.js#L110)  
引入版本：4.0.0


---

### transformerNode {#transformerNode}

#### transformerNode: [Phaser.Renderer.WebGL.RenderNodes.TransformerImage](/api/class/renderer-webgl-rendernodes-transformerimage) {#transformernode-phaserrendererwebglrendernodestransformerimage}


**说明:**

变压器节点用来转换四角用于渲染.


> 源码：[src/renderer/webgl/renderNodes/ShaderQuad.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/ShaderQuad.js#L121)  
引入版本：4.0.0


---

### vertexBufferLayout {#vertexBufferLayout}

#### vertexBufferLayout: [Phaser.Renderer.WebGL.Wrappers.WebGLVertexBufferLayoutWrapper](/api/class/renderer-webgl-wrappers-webglvertexbufferlayoutwrapper) {#vertexbufferlayout-phaserrendererwebglwrapperswebglvertexbufferlayoutwrapper}


**说明:**

此 RenderNode 的顶点缓冲布局 。

由4个顶点组成 0-3 组成四极体的角.


> 源码：[src/renderer/webgl/renderNodes/ShaderQuad.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/ShaderQuad.js#L68)  
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

#### \<instance> run(drawingContext, gameObject, parentMatrix) {#instance-rundrawingcontext-gameobject-parentmatrix}


**说明:**

使用遮蔽程序渲染一个四重奏。根据游戏对象属性转换四重奏,充值顶点缓冲,设置制服和纹理,并发出一个绘图调用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| gameObject | [Phaser.GameObjects.Shader](/api/class/gameobjects-shader) | 否 | 正在渲染的 Shader 游戏对象 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 母变矩阵. |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/ShaderQuad.js#L222](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/ShaderQuad.js#L222)  
引入版本：4.0.0


---

### setupTextures {#setupTextures}

#### \<instance> setupTextures(gameObject) {#instance-setuptexturesgameobject}


**说明:**

从游戏对象的纹理列表中提取 WebGL纹理,并把它们作为渲染时使用的阵列返回.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.Shader](/api/class/gameobjects-shader) | 否 | 沙德游戏对象提取纹理. |


**返回值:** Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper)> - 一组WebGL纹理.


> 源码：[src/renderer/webgl/renderNodes/ShaderQuad.js#L348](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/ShaderQuad.js#L348)  
引入版本：4.0.0


---

### updateShaderConfig {#updateShaderConfig}

#### \<instance> updateShaderConfig(drawingContext, gameObject, renderNode) {#instance-updateshaderconfigdrawingcontext-gameobject-rendernode}


**说明:**

更新当前渲染通道的遮蔽配置。 阴影渲染之前, 使用此配置。 这种方法是自定义遮蔽配置的钩子。 如果您在初始化后需要调整遮蔽器添加, 您应该覆盖它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象正在被渲染 。 |
| renderNode | [Phaser.Renderer.WebGL.RenderNodes.ShaderQuad](/api/class/renderer-webgl-rendernodes-shaderquad) | 否 | 正在提供“RenderNode”。 |


> 源码：[src/renderer/webgl/renderNodes/ShaderQuad.js#L372](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/ShaderQuad.js#L372)  
引入版本：4.0.0


---

---
