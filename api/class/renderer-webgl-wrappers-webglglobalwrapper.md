# WebGLGlobalWrapper {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-wrappers-webglglobalwrapper)

WebGL全局状态的包装器,包括混合模式,纹理绑定,剪刀测试,天花测试,深度测试,以及其他GL上下文设置. 它跟踪当前状态并高效应用更改以避免冗余的WebGL呼叫.

**构造函数**

`new WebGLGlobalWrapper(renderer)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 创建 WebGLRender 的 WebGLGlobalWrapper 的网络GLLender 。 |

---


**作用域**: static

> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L10)  
引入版本：4.0.0

## 公开成员 {#public-members}

### renderer {#renderer}

#### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrendererwebglwebglrenderer}


**说明:**

这个WebGLLWrapper与WebGLGlobalWrapper相关联.


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L30](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L30)  
引入版本：4.0.0


---

### state {#state}

#### state: [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) {#state-phasertypesrendererwebglwebglglobalparameters}


**说明:**

由这个包装器跟踪的当前 WebGL 全球状态参数.


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L39)  
引入版本：4.0.0


---

## 公开方法 {#public-methods}

### update {#update}

#### \<instance> update([state], [force], [vaoLast]) {#instance-updatestate-force-vaolast}


**说明:**

设置全局 WebGL状态。参数仅在输入 `state`中定义,且与当前状态不同的情况下,才会在 WebGLRendering Context 上更新。

当`force`是真实的,并且`state`是定义的时,无论目前状态如何,`state`上的参数总是设定的.

当`force`是真实的,而`state`是未定义的时,则使用当前状态来重置所有参数.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 是 |  | 要设置的状态。 如果未定义, 当前状态用于 `force` 谓 `true`. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |
| vaoLast | boolean | 是 | false | 如果 `true`, VAO 将被设定为最后。 否则, 它将被设定为第一。 执行会影响 VAO 的状态变化时, 如 `bindings.elementArrayBuffer` , 这样做很有用 。 |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L49)  
引入版本：4.0.0


---

### updateBindings {#updateBindings}

#### \<instance> updateBindings(state, [force]) {#instance-updatebindingsstate-force}


**说明:**

更新绑定状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L132)  
引入版本：4.0.0


---

### updateBindingsActiveTexture {#updateBindingsActiveTexture}

#### \<instance> updateBindingsActiveTexture(state, [force]) {#instance-updatebindingsactivetexturestate-force}


**说明:**

更新活动纹理单位状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L170](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L170)  
引入版本：4.0.0


---

### updateBindingsArrayBuffer {#updateBindingsArrayBuffer}

#### \<instance> updateBindingsArrayBuffer(state, [force]) {#instance-updatebindingsarraybufferstate-force}


**说明:**

更新数组缓冲器(ARRAY_BUFFER)绑定状态。这可以绑定用于向GPU提供顶点属性数据的顶点缓冲对象。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L195](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L195)  
引入版本：4.0.0


---

### updateBindingsElementArrayBuffer {#updateBindingsElementArrayBuffer}

#### \<instance> updateBindingsElementArrayBuffer(state, [force]) {#instance-updatebindingselementarraybufferstate-force}


**说明:**

更新索引数组缓冲状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L229](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L229)  
引入版本：4.0.0


---

### updateBindingsFramebuffer {#updateBindingsFramebuffer}

#### \<instance> updateBindingsFramebuffer(state, [force]) {#instance-updatebindingsframebufferstate-force}


**说明:**

更新帧缓冲状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L262](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L262)  
引入版本：4.0.0


---

### updateBindingsProgram {#updateBindingsProgram}

#### \<instance> updateBindingsProgram(state, [force]) {#instance-updatebindingsprogramstate-force}


**说明:**

更新当前绑定的 WebGL 遮阳程序,使用`gl.useProgram`调用.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L288](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L288)  
引入版本：4.0.0


---

### updateBindingsRenderbuffer {#updateBindingsRenderbuffer}

#### \<instance> updateBindingsRenderbuffer(state, [force]) {#instance-updatebindingsrenderbufferstate-force}


**说明:**

更新缓冲状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L313](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L313)  
引入版本：4.0.0


---

### updateBlend {#updateBlend}

#### \<instance> updateBlend(state, [force]) {#instance-updateblendstate-force}


**说明:**

更新混合状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L339](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L339)  
引入版本：4.0.0


---

### updateBlendColor {#updateBlendColor}

#### \<instance> updateBlendColor(state, [force]) {#instance-updateblendcolorstate-force}


**说明:**

更新混合颜色。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L368](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L368)  
引入版本：4.0.0


---

### updateBlendEnabled {#updateBlendEnabled}

#### \<instance> updateBlendEnabled(state, [force]) {#instance-updateblendenabledstate-force}


**说明:**

更新混合启用状态 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L399](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L399)  
引入版本：4.0.0


---

### updateBlendEquation {#updateBlendEquation}

#### \<instance> updateBlendEquation(state, [force]) {#instance-updateblendequationstate-force}


**说明:**

更新混合方程式状态。

方程常当分别.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L431](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L431)  
引入版本：4.0.0


---

### updateBlendFunc {#updateBlendFunc}

#### \<instance> updateBlendFunc(state, [force]) {#instance-updateblendfuncstate-force}


**说明:**

更新混合函数状态。

职能总是被视为单独的。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L458](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L458)  
引入版本：4.0.0


---

### updateColorClearValue {#updateColorClearValue}

#### \<instance> updateColorClearValue(state, [force]) {#instance-updatecolorclearvaluestate-force}


**说明:**

更新用于在`gl.clear`被调用颜色缓冲位点时填充颜色缓冲器的 RGBA 颜色值 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L488](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L488)  
引入版本：4.0.0


---

### updateColorWritemask {#updateColorWritemask}

#### \<instance> updateColorWritemask(state, [force]) {#instance-updatecolorwritemaskstate-force}


**说明:**

更新色彩写掩码,用于控制在渲染过程中将哪些 RGBA 色彩组件写入色彩缓冲器.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L521](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L521)  
引入版本：4.0.0


---

### updateCullFace {#updateCullFace}

#### \<instance> updateCullFace(state, [force]) {#instance-updatecullfacestate-force}


**说明:**

更新阴沟面部状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L553](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L553)  
引入版本：4.0.0


---

### updateDepthTest {#updateDepthTest}

#### \<instance> updateDepthTest(state, [force]) {#instance-updatedepthteststate-force}


**说明:**

更新深度测试状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L585](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L585)  
引入版本：4.0.0


---

### updateScissor {#updateScissor}

#### \<instance> updateScissor(state, [force]) {#instance-updatescissorstate-force}


**说明:**

更新剪刀状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L617](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L617)  
引入版本：4.0.0


---

### updateScissorBox {#updateScissorBox}

#### \<instance> updateScissorBox(state, [force]) {#instance-updatescissorboxstate-force}


**说明:**

更新剪刀盒状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L670](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L670)  
引入版本：4.0.0


---

### updateScissorEnabled {#updateScissorEnabled}

#### \<instance> updateScissorEnabled(state, [force]) {#instance-updatescissorenabledstate-force}


**说明:**

更新已启用的剪刀状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L638](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L638)  
引入版本：4.0.0


---

### updateStencil {#updateStencil}

#### \<instance> updateStencil(state, [force]) {#instance-updatestencilstate-force}


**说明:**

更新星格状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L706](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L706)  
引入版本：4.0.0


---

### updateStencilClear {#updateStencilClear}

#### \<instance> updateStencilClear(state, [force]) {#instance-updatestencilclearstate-force}


**说明:**

更新在使用 Stencil 缓冲位点调用 `gl.clear` 时用于清除 Stencil 缓冲的值 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L735](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L735)  
引入版本：4.0.0


---

### updateStencilEnabled {#updateStencilEnabled}

#### \<instance> updateStencilEnabled(state, [force]) {#instance-updatestencilenabledstate-force}


**说明:**

更新已启用的天线状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L760](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L760)  
引入版本：4.0.0


---

### updateStencilFunc {#updateStencilFunc}

#### \<instance> updateStencilFunc(state, [force]) {#instance-updatestencilfuncstate-force}


**说明:**

更新音阶函数状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L792](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L792)  
引入版本：4.0.0


---

### updateStencilOp {#updateStencilOp}

#### \<instance> updateStencilOp(state, [force]) {#instance-updatestencilopstate-force}


**说明:**

更新速率操作状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L819](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L819)  
引入版本：4.0.0


---

### updateTexturing {#updateTexturing}

#### \<instance> updateTexturing(state, [force]) {#instance-updatetexturingstate-force}


**说明:**

更新纹理状态, 创建纹理时生效。 包括 `flipY` 和 `premultiplyAlpha` 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L846](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L846)  
引入版本：4.0.0


---

### updateTexturingFlipY {#updateTexturingFlipY}

#### \<instance> updateTexturingFlipY(state, [force]) {#instance-updatetexturingflipystate-force}


**说明:**

更新 `UNPACK_FLIP_Y_WEBGL`像素存储参数,该参数控制上传到GPU时是否垂直翻转纹理图像数据.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L868](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L868)  
引入版本：4.0.0


---

### updateTexturingPremultiplyAlpha {#updateTexturingPremultiplyAlpha}

#### \<instance> updateTexturingPremultiplyAlpha(state, [force]) {#instance-updatetexturingpremultiplyalphastate-force}


**说明:**

更新`UNPACK_PREMULTIPLY_ALPHA_WEBGL`像素存储参数,在纹理图像数据上传到GPU时,它控制α通道是否被预先多倍化到RGB组件中.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L894](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L894)  
引入版本：4.0.0


---

### updateVAO {#updateVAO}

#### \<instance> updateVAO(state, [force]) {#instance-updatevaostate-force}


**说明:**

更新顶点阵列对象状态。

请注意, VAO 自动受到 `elementArrayBuffer` 和 WebGL 中写入的任何属性设置的约束。 当绑定 VAO 时, 确保其他约束 , 如您所希望的那样, 前后会生效 。 当使用 `update` 时, VAO 默认先设定 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L921](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L921)  
引入版本：4.0.0


---

### updateViewport {#updateViewport}

#### \<instance> updateViewport(state, [force]) {#instance-updateviewportstate-force}


**说明:**

更新视图状态。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) | 否 |  | 州以设. |
| force | boolean | 是 | false | 如果 `true`,则无论目前状态如何,状态都会被设定. |


> 源码：[src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L960](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLGlobalWrapper.js#L960)  
引入版本：4.0.0


---

---
