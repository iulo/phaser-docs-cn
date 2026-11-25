# Phaser.Renderer.WebGL.WebGLBlendParametersFactory {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/renderer-webgl-webglblendparametersfactory)

Scope: 
static
> 源码：[src/renderer/webgl/parameters/WebGLBlendParametersFactory.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/parameters/WebGLBlendParametersFactory.js#L7)  
引入版本：4.0.0

## 静态函数 {#static-functions}

### createCombined {#createCombined}

#### \<instance> createCombined(renderer, [enabled], [color], [equation], [funcSrc], [funcDst]) {#instance-createcombinedrenderer-enabled-color-equation-funcsrc-funcdst}


**说明:**

创建新的 WebGLBlendParameters 对象 。

默认值是用于普通混合模式的 。

- 启用: 真

- color: [ 0, 0, 0, 0 ]

- 方程式: gl.FUNC_ADD

- funcSrc: GL. 无

- funcDst: gl.one_MINUS_SRC_ALPHA 互联网档案馆的存档,存档日期2013-03-02.

在哪里,我们在哪里 `equation`, `funcSrc`,和 `funcDst` RGB 和 Alpha 的代码相同。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 |  | 创建 WebGLBlendParameters 的 WebGLRenderer 软件。 |
| enabled | GLboolean | 是 | true | 是否启用混合 。 |
| color | Array.\<GLclampf> | 是 | "[0, 0, 0, 0]" | 混合色(4个频道的阵列,0-1). |
| equation | GLenum | 是 | "gl.FUNC_ADD" | 混合方程式 。 |
| funcSrc | GLenum | 是 | "gl.ONE" | 源的混合函数. |
| funcDst | GLenum | 是 | "gl.ONE_MINUS_SRC_ALPHA" | 目的地混合功能. |


**返回值:** [Phaser.Types.Renderer.WebGL.WebGLBlendParameters](/api/typedef/types-renderer-webgl#webglblendparameters) - 创建的 WebGLBlendParameters. 中国植物物种信息数据库.


> 源码：[src/renderer/webgl/parameters/WebGLBlendParametersFactory.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/parameters/WebGLBlendParametersFactory.js#L21)  
引入版本：4.0.0


---

### createSeparate {#createSeparate}

#### \<instance> createSeparate(renderer, [enabled], [color], [equationRGB], [equationAlpha], [funcSrcRGB], [funcDstRGB], [funcSrcAlpha], [funcDstAlpha]) {#instance-createseparaterenderer-enabled-color-equationrgb-equationalpha-funcsrcrgb-funcdstrgb-funcsrcalpha-funcdstalpha}


**说明:**

创建一个新的WebGLBlendParamomels对象,对RGB和α混合方程和函数有独立的控制.

默认值是用于普通混合模式的 。

- 启用: 真

- color: [ 0, 0, 0, 0 ]

- equationRGB: gl.FUNC_ADD 数据

- equationAlpha: gl.FUNC_ADD 数据

- funcSrcRGB: GL. 无

- funcDstRGB: gl.one_MINUS_SRC_ALPHA 互联网档案馆的存档,存档日期2013-03-02.

- funcSrcAlpha: GL. 无

- funcDstAlpha: gl.one_MINUS_SRC_ALPHA 互联网档案馆的存档,存档日期2013-03-02.

与`createCombined`不同,RGB和α通道可以使用不同的方程和混合功能.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 |  | 创建 WebGLBlendParameters 的 WebGLRenderer 软件。 |
| enabled | GLboolean | 是 | true | 是否启用混合 。 |
| color | Array.\<GLclampf> | 是 | "[0, 0, 0, 0]" | 混合色(4个频道的阵列,0-1). |
| equationRGB | GLenum | 是 | "gl.FUNC_ADD" | RGB混合方程式. |
| equationAlpha | GLenum | 是 | "gl.FUNC_ADD" | 阿尔法混合方程式. |
| funcSrcRGB | GLenum | 是 | "gl.ONE" | RGB源混合函数. |
| funcDstRGB | GLenum | 是 | "gl.ONE_MINUS_SRC_ALPHA" | RGB 目标混合功能. |
| funcSrcAlpha | GLenum | 是 | "gl.ONE" | α源混合函数. |
| funcDstAlpha | GLenum | 是 | "gl.ONE_MINUS_SRC_ALPHA" | α目的地混合功能. |


**返回值:** [Phaser.Types.Renderer.WebGL.WebGLBlendParameters](/api/typedef/types-renderer-webgl#webglblendparameters) - 创建的 WebGLBlendParameters. 中国植物物种信息数据库.


> 源码：[src/renderer/webgl/parameters/WebGLBlendParametersFactory.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/parameters/WebGLBlendParametersFactory.js#L61)  
引入版本：4.0.0


---

---
