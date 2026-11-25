# Phaser.Renderer.WebGL.WebGLGlobalParametersFactory {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/renderer-webgl-webglglobalparametersfactory)

Scope: 
static
> 源码：[src/renderer/webgl/parameters/WebGLGlobalParametersFactory.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/parameters/WebGLGlobalParametersFactory.js#L11)  
引入版本：4.0.0

## 静态函数 {#static-functions}

### getDefault {#getDefault}

#### \<instance> getDefault(renderer) {#instance-getdefaultrenderer}


**说明:**

创建一个新 `WebGLGlobalParameters` 对象, 内含合理的默认值。 默认反映了每次渲染开始时预期的初始 WebGL 状态 : NORMAL 混合模式、 完全开放的黑色清晰颜色、 允许写入的所有颜色通道、 面部剪切和深度测试 已禁用 、 剪切测试 启用的零大小框、 默认的音阶参数( 通过 `WebGLStencilParametersFactory` 获取) 和零大小的视口 。 这个对象通常被 WebGL 渲染器用于 初始状态或重设其跟踪的全球状态 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 创建 WebGLRenderer 的 WebGL 全球参数 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) - 默认的 WebGL GlobalParameters 。


> 源码：[src/renderer/webgl/parameters/WebGLGlobalParametersFactory.js#L25](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/parameters/WebGLGlobalParametersFactory.js#L25)  
引入版本：4.0.0


---

---
