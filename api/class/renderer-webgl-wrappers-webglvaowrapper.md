# WebGLVAOWrapper {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-wrappers-webglvaowrapper)

WebGL Vertex 阵列对象(VAO)的包装器.

VAO存储一个绘图调用的全部顶点属性配置,包括属性指针定义,启用属性数组,以及绑定元素数组缓冲器. 在绘制恢复此状态之前,将一个VAO装订在一个单调中,减少每个帧需要的WebGL API调用次数.

一个原始的WebGLVertexArray对象不应该在WebGLRenderer之外曝光,因此WebGLLRenderer可以处理上下文丢失和其他事件,而不需要其他系统知道. 总是使用WebGLWAOWrapper代替.

**构造函数**

`new WebGLVAOWrapper(renderer, program, indexBuffer, attributeBufferLayouts)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有这个包装的 WebGLRender 实例 。 |
| program | [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](/api/class/renderer-webgl-wrappers-webglprogramwrapper) | 否 | 这个 VAO 与之相关的遮荫程序. |
| indexBuffer | [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) | 否 | 此 VAO 中使用的索引缓冲器, 如果有的话 。 |
| attributeBufferLayouts | Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLVertexBufferLayoutWrapper](/api/class/renderer-webgl-wrappers-webglvertexbufferlayoutwrapper)> | 否 | 包含此 VAO 属性数据的顶点缓冲器, 以及相关的属性布局 。 |

---


**作用域**: static

> 源码：[src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L9)  
引入版本：4.0.0

## 公开成员 {#public-members}

### attributeBufferLayouts {#attributeBufferLayouts}

#### attributeBufferLayouts: Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLVertexBufferLayoutWrapper](/api/class/renderer-webgl-wrappers-webglvertexbufferlayoutwrapper)> {#attributebufferlayouts-arrayphaserrendererwebglwrapperswebglvertexbufferlayoutwrapper}


**说明:**

包含此 VAO 属性数据的顶点缓冲器, 以及相关的属性布局 。


> 源码：[src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L78)  
引入版本：4.0.0


---

### glState {#glState}

#### glState: object {#glstate-object}


**说明:**

用于绑定此 VAO 的状态对象 。


> 源码：[src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L88)  
引入版本：4.0.0


---

### indexBuffer {#indexBuffer}

#### indexBuffer: [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) {#indexbuffer-phaserrendererwebglwrapperswebglbufferwrapper}


**说明:**

此 VAO 中使用的元素数组缓冲器( 如果有的话) 。


> 源码：[src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L68)  
引入版本：4.0.0


---

### program {#program}

#### program: [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](/api/class/renderer-webgl-wrappers-webglprogramwrapper) {#program-phaserrendererwebglwrapperswebglprogramwrapper}


**说明:**

这个 VAO 与之相关的遮荫程序.


> 源码：[src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L45)  
引入版本：4.0.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrendererwebglwebglrenderer}


**说明:**

拥有这个包装的 WebGLRender 实例 。


> 源码：[src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L36)  
引入版本：4.0.0


---

### vertexArrayObject {#vertexArrayObject}

#### vertexArrayObject: WebGLVertexArrayObject {#vertexarrayobject-webglvertexarrayobject}


**说明:**

由此类包扎的 WebGLVertex 箭头对象 。

此属性随时会改变。 因此, 您不应该存储此值的引用。 它只应直接传递到 WebGL API 中进行绘图 。


> 源码：[src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L54)  
引入版本：4.0.0


---

## 公开方法 {#public-methods}

### bind {#bind}

#### \<instance> bind() {#instance-bind}


**说明:**

将此 WebGLVAOWrapper 绑定到当前 WebGLRendering Context 中 。


> 源码：[src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L207](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L207)  
引入版本：4.0.0


---

### createResource {#createResource}

#### \<instance> createResource() {#instance-createresource}


**说明:**

创建新的 WebGLVertex Array 对象, 并将完整的顶点属性配置记录到其中。 这包括绑定可选索引缓冲, 允许每个顶点属性数组, 设置属性指针( 包括矩阵属性的每个柱点) , 并应用实例 divisors 来进行渲染 。 VAO 已完全配置后, 它将与任何阵列和元素阵列缓冲一起, 离开 WebGL 状态 。

这种方法由构造器自动调用。 当上下文丢失事件后WebGL上下文恢复时, 也叫WebGLRenderer 。


> 源码：[src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L102)  
引入版本：4.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此 WebGLVAOWrapper 并删除所有相关资源 。


> 源码：[src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L218](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVAOWrapper.js#L218)  
引入版本：4.0.0


---

---
