# WebGLProgramWrapper {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-wrappers-webglprogramwrapper)

环绕 a WebGL 着色器程序,即GPU侧面程序,由顶点阴影和片段阴影编译。这些着色器程序共同定义几何的变形方式以及几何中每个像素的颜色。 Phaser的,因为 WebGL 渲染器由WebGLProgramWrapper支持.

除了持有编译的程序,这个包装器管理了相关的WebGL资源的整个生命周期:它跟踪顶点属性位置和布局,存储统一值,并在程序被绑定用于绘图时,排队使用统一更新请求.

原始的WebGLProgram对象绝不应直接使用或存储在WebGLRenderer之外。通过此包件将所有访问都定位到路由,渲染器可以透明地处理WebGL上下文丢失和恢复——重新创建基础程序并重新应用所有状态——而不需要其他系统知道它。总是使用WebGLProgramWrapper而不是持有一个直接的WebGPROGram参考.

**构造函数**

`new WebGLProgramWrapper(renderer, vertexSource, fragmentSource)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有这个包装的 WebGLRender 实例 。 |
| vertexSource | string | 否 | 顶点遮蔽源代码作为字符串. |
| fragmentSource | string | 否 | 碎片阴影源代码作为字符串. |

---


**作用域**: static

> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L26](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L26)  
引入版本：3.80.0

## 公开成员 {#public-members}

### compileTimeMs {#compileTimeMs}

#### compileTimeMs: number {#compiletimems-number}


**说明:**

编译这个程序所需的时间,以毫秒计.


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L106)  
引入版本：4.0.0


---

### compiling {#compiling}

#### compiling: boolean {#compiling-boolean}


**说明:**

是否正在编译此程序。 除非通过 `config.render.skipUnreadyShaders` 启用并行的阴影编译, 否则此程序将永远是虚假的 。


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L82)  
引入版本：4.0.0


---

### fragmentSource {#fragmentSource}

#### fragmentSource: string {#fragmentsource-string}


**说明:**

碎片阴影源代码作为字符串.


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L136)  
引入版本：3.80.0


---

### glAttributeBuffer {#glAttributeBuffer}

#### glAttributeBuffer: WebGLBuffer {#glattributebuffer-webglbuffer}


**说明:**

此程序用于属性的缓冲 。


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L188](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L188)  
引入版本：4.0.0


---

### glAttributeNames {#glAttributeNames}

#### glAttributeNames: Map.\<string, number> {#glattributenames-mapstring-number}


**说明:**

`glAttributes`中其索引的属性名称地图.


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L179](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L179)  
引入版本：4.0.0


---

### glAttributes {#glAttributes}

#### glAttributes: Array.\<{location: GLint, name: string, size: number, type: GLenum}> {#glattributes-arraylocation-glint-name-string-size-number-type-glenum}


**说明:**

此程序的属性状态 。

这些代表WebGL中的实际状态,只有在程序用于绘图时才更新.


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L167](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L167)  
引入版本：4.0.0


---

### glState {#glState}

#### glState: [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) {#glstate-phasertypesrendererwebglwebglglobalparameters}


**说明:**

绑定这个程序所必需的WebGL状态.

内部使用此方法来加速状态变化.


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L116)  
引入版本：4.0.0


---

### glUniforms {#glUniforms}

#### glUniforms: Map.\<string, [Phaser.Types.Renderer.WebGL.WebGLUniform](/api/typedef/types-renderer-webgl#webgluniform)> {#gluniforms-mapstring-phasertypesrendererwebglwebgluniform}


**说明:**

方案的统一状态。

这些代表WebGL中的实际状态,只有在程序用于绘图时才更新.


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L198](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L198)  
引入版本：4.0.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrendererwebglwebglrenderer}


**说明:**

拥有这个包装的 WebGLRender 实例 。


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L59)  
引入版本：4.0.0


---

### uniformRequests {#uniformRequests}

#### uniformRequests: Map.\<string, any> {#uniformrequests-mapstring-any}


**说明:**

请求更新统一状态。 将请求名称设定为新值。 仅在程序用于绘图时才处理这些请求 。


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L210](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L210)  
引入版本：4.0.0


---

### vertexSource {#vertexSource}

#### vertexSource: string {#vertexsource-string}


**说明:**

顶点遮蔽源代码作为字符串.


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L127](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L127)  
引入版本：3.80.0


---

### webGLProgram {#webGLProgram}

#### webGLProgram: WebGLProgram {#webglprogram-webglprogram}


**说明:**

这个类正在包着的 WebGL 方案.

此属性随时会改变。 因此, 您不应该存储此值的引用。 它只应直接传递到 WebGL API 中进行绘图 。


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L68)  
引入版本：3.80.0


---

## 公开方法 {#public-methods}

### bind {#bind}

#### \<instance> bind() {#instance-bind}


**说明:**

将此程序设定为 WebGL 语境下的激活程序, 然后处理所有通过 `setUniform` 排队的待统一更新请求。 每个请求都被应用到 GPU 中, 并且队列被清除, 因此只有已经实际更改的值会被发送到 WebGL 。


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L441](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L441)  
引入版本：4.0.0


---

### checkParallelCompile {#checkParallelCompile}

#### \<instance> checkParallelCompile() {#instance-checkparallelcompile}


**说明:**

Poll 遮荫器编译状态, 如果程序已准备好, 则完成程序。 只有在启用 `skipUnreadyShaders` 和 KHR_ 并行_ 阴影_ 编译扩展时, 才使用此程序 。


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L290](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L290)  
引入版本：4.0.0


---

### createResource {#createResource}

#### \<instance> createResource() {#instance-createresource}


**说明:**

从给定的顶点和片段阴影创建 WebGL 方案。

由构建器自动调用。 如果 WebGL 程序需要重新创建, 也可以再次调用 。


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L224](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L224)  
引入版本：3.80.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此 WebGL 程序程序并释放所有相关的 WebGL 资源 。

如果上下文没有丢失, 此选项会删除顶点阴影、 片段阴影、 链接的 WebGL 程序表, 并禁用此程序使用的所有顶点属性数组。 统一地图、 属性地图以及任何未决的统一请求也已被清除。 然后所有内部引用将被取消, 这样可以安全收集垃圾 。


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L543](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L543)  
引入版本：3.80.0


---

### setUniform {#setUniform}

#### \<instance> setUniform(name, value) {#instance-setuniformname-value}


**说明:**

为此 WebGL 方案设置一个统一的值 。

此方法不直接设置 WebGL值, 而是在 `uniformRequests` 地图上添加一个请求。 这些请求在程序用于绘图时会处理 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 服之名曰  . |
| value | number \| Array.\<number> | Int32Array | Float32Array | 否 | 要设置的值 。 |


> 源码：[src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L424](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L424)  
引入版本：4.0.0


---

---
