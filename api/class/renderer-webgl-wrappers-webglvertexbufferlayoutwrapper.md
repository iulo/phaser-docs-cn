# WebGLVertexBufferLayoutWrapper {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-wrappers-webglvertexbufferlayoutwrapper)

将 WebGL 顶点缓冲器及其属性布局描述包在一起。 此类管理 `WebGLBufferWrapper`( 原始 GPU 缓冲器) 与描述顶点数据如何排列的属性布局之间的关系, 包括阶梯、 偶位字节计数和字节偏移。 它被 Phaser 的 WebGL 渲染器用来在绘制几何时将顶点数据绑定在阴影属性位置。 在构造时, 排版是通过计算脚步、 字节计数和从所提供的属性定义中抵消, 以及任何指定为字符串的GL 值都解到其数值等值。

**构造函数**

`new WebGLVertexBufferLayoutWrapper(renderer, program, layout, [buffer])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有这个包装的 WebGLRender 实例 。 |
| program | [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](/api/class/renderer-webgl-wrappers-webglprogramwrapper) | 否 | 此布局与之相关的程序 。 |
| layout | Partial.\<[Phaser.Types.Renderer.WebGL.WebGLAttributeBufferLayout](/api/typedef/types-renderer-webgl#webglattributebufferlayout)> | 否 | 缓冲器的布局。 在构造时, 这会不完整。 构造时会填充边距和属性位置、 字节和偏移。 这将改变对象 。 |
| buffer | [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) | 是 | 此布局应该使用的缓冲。 如果不提供, 将会创建一个新的缓冲。 如果缓冲太小, 则会丢弃例外 。 |

---


**作用域**: static

> 源码：[src/renderer/webgl/wrappers/WebGLVertexBufferLayoutWrapper.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVertexBufferLayoutWrapper.js#L9)  
引入版本：4.0.0

## 公开成员 {#public-members}

### buffer {#buffer}

#### buffer: [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) {#buffer-phaserrendererwebglwrapperswebglbufferwrapper}


**说明:**

WebGLBaferWrapper 持有此布局的顶点数据.


> 源码：[src/renderer/webgl/wrappers/WebGLVertexBufferLayoutWrapper.js#L64](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVertexBufferLayoutWrapper.js#L64)  
引入版本：4.0.0


---

### layout {#layout}

#### layout: [Phaser.Types.Renderer.WebGL.WebGLAttributeBufferLayout](/api/typedef/types-renderer-webgl#webglattributebufferlayout) {#layout-phasertypesrendererwebglwebglattributebufferlayout}


**说明:**

完成的属性缓冲布局,描述顶点缓冲范围内的步态,属性,类型,大小,字节计数,以及字节抵消.


> 源码：[src/renderer/webgl/wrappers/WebGLVertexBufferLayoutWrapper.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVertexBufferLayoutWrapper.js#L43)  
引入版本：4.0.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrendererwebglwebglrenderer}


**说明:**

拥有这个包装的 WebGLRender 实例 。


> 源码：[src/renderer/webgl/wrappers/WebGLVertexBufferLayoutWrapper.js#L34](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVertexBufferLayoutWrapper.js#L34)  
引入版本：4.0.0


---

## 公开方法 {#public-methods}

### completeLayout {#completeLayout}

#### \<instance> completeLayout(attributeBufferLayout) {#instance-completelayoutattributebufferlayout}


**说明:**

完成所提供属性缓冲布局的布局。 这将填充步数、 字节数和偏移。 此外, 它将将指定为字符串的任何 GLenums 转换为其数值。 这样会改变布局 。

排版内属性的顺序构成缓冲的顺序.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| attributeBufferLayout | [Phaser.Types.Renderer.WebGL.WebGLAttributeBufferLayout](/api/typedef/types-renderer-webgl#webglattributebufferlayout) | 否 | 完成布局. |


> 源码：[src/renderer/webgl/wrappers/WebGLVertexBufferLayoutWrapper.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLVertexBufferLayoutWrapper.js#L74)  
引入版本：4.0.0


---

---
