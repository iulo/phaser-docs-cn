# BaseFilterShader {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-basefiltershader)

这是所有使用遮蔽器的过滤器的基类。 大多数过滤器会扩展此类 。

它负责设置着色器程序和顶点缓冲布局。 它还提供了处理过滤器渲染的 `run` 方法。 在渲染时, 它生成一个新的绘图康特来渲染并释放输入绘图康特。

注意: 在阴影码中使用 `gl_FragCoord` 时要小心。 这个内置变量会给您一个处理中的像素的“ 窗口相对” 坐标。 但这实际上与帧缓冲器大小是相对的, Phaser 将除主帆布以外的所有帧缓冲器都视为垂直翻转。 这意味着 阴影罩中的 `gl_FragCoord.y = 0` 将是帧缓冲器的底部, 但画布的顶部。 这意味着 `gl_FragCoord` 给与主帆布相比在帧缓冲器( 如 Render 纹理或过滤器) 内时会给出不同的结果 。 在写入阴影罩时要注意这个限制 。

**构造函数**

`new BaseFilterShader(name, manager, [fragmentShaderKey], [fragmentShaderSource], [shaderAdditions])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 滤镜的名称 。 |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 拥有这个过滤器的经理. |
| fragmentShaderKey | string | 是 | 阴影缓存中碎片遮蔽源的键。 只有在未设置 `fragmentShaderSource` 时才会使用 。 |
| fragmentShaderSource | string | 是 | 碎片遮蔽源. |
| shaderAdditions | Array.\<[Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig)> | 是 | 用于着色器程序的阴影添加数组。 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilter](/api/class/renderer-webgl-rendernodes-basefilter)  



> 源码：[src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L14)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### indexBuffer {#indexBuffer}

#### indexBuffer: [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) {#indexbuffer-phaserrendererwebglwrapperswebglbufferwrapper}


**说明:**

索引缓冲定义顶点顺序.


> 源码：[src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L96)  
引入版本：4.0.0


---

### programManager {#programManager}

#### programManager: [Phaser.Renderer.WebGL.ProgramManager](/api/class/renderer-webgl-programmanager) {#programmanager-phaserrendererwebglprogrammanager}


**说明:**

程序管理器用来创建和管理遮荫程序。 包含遮荫变体 。


> 源码：[src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L121)  
引入版本：4.0.0


---

### vertexBufferLayout {#vertexBufferLayout}

#### vertexBufferLayout: [Phaser.Renderer.WebGL.Wrappers.WebGLVertexBufferLayoutWrapper](/api/class/renderer-webgl-wrappers-webglvertexbufferlayoutwrapper) {#vertexbufferlayout-phaserrendererwebglwrapperswebglvertexbufferlayoutwrapper}


**说明:**

此 RenderNode 的顶点缓冲布局 。

这包括四个顶点组成一个四角的角.


> 源码：[src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L105](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L105)  
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

#### \<instance> run(controller, inputDrawingContext, [outputDrawingContext], [padding]) {#instance-runcontroller-inputdrawingcontext-outputdrawingcontext-padding}


**说明:**

运行滤镜遮蔽器。这种方法处理过滤器的全部渲染管道:它获得输出的绘图连接(或使用所提供的一个),计算加法四极顶点,填充顶点缓冲器,通过遮蔽程序设置纹理和制服,发出绘图调用,并释放输入上下文。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Controller](/api/class/filters-controller) | 否 | 拥有此过滤器的过滤器控制器 。 |
| inputDrawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 包含源质的输入图文背景 。 |
| outputDrawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 是 | 选项输出绘图上下文。 如果不提供, 将从池中获取 。 |
| padding | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 可选的粘贴矩形。 如果不提供, 则使用控制器的粘贴符 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.BaseFilter#运行


**返回值:** [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) - 包含过滤结果的输出绘图上下文 。


> 源码：[src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L151](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L151)  
引入版本：4.0.0


---

### setupTextures {#setupTextures}

#### \<instance> setupTextures(controller, textures, drawingContext) {#instance-setuptexturescontroller-textures-drawingcontext}


**说明:**

运行纹理阵列上的任何必要的修改。 覆盖此方法来处理纹理输入 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Controller](/api/class/filters-controller) | 否 | 过滤器控制器。 |
| textures | Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper)> | 否 | 用于修改位置的纹理阵列。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 正在使用的绘图上下文 。 |


> 源码：[src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L313](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L313)  
引入版本：4.0.0


---

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(controller, drawingContext) {#instance-setupuniformscontroller-drawingcontext}


**说明:**

以控制器为基础为这个遮蔽器设置制服, 覆盖此处理制服设置的方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Controller](/api/class/filters-controller) | 否 | 过滤器控制器。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 正在使用的绘图上下文 。 |


> 源码：[src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L328](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L328)  
引入版本：4.0.0


---

### updateShaderConfig {#updateShaderConfig}

#### \<instance> updateShaderConfig(controller, drawingContext) {#instance-updateshaderconfigcontroller-drawingcontext}


**说明:**

设置此阴影的阴影配置 。 覆盖此方法处理阴影配置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.Controller](/api/class/filters-controller) | 否 | 过滤器控制器。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 正在使用的绘图上下文 。 |


> 源码：[src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L299](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/BaseFilterShader.js#L299)  
引入版本：4.0.0


---

---
