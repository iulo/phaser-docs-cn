# WebGLShaderSetterWrapper {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-wrappers-webglshadersetterwrapper)

存储为每类GLSL数据类型设置遮蔽器统一值所需的元数据和 WebGL函数引用。该类的核心是 `constants`地图,该地图由 WebGL类型常数(如 `gl.FLOAT`, `gl.FLOAT_VEC2`, `gl.FLOAT_MAT4`) 键入,并为每类提供了相应的统一设置函数,元素计数,字节大小,矩阵旗.

由于WebGL统一设置功能(`gl.uniform1f`,`gl.uniform2i`等)在构造时与渲染上下文相连,所以这一类主要存在,是为了一次捕捉这些函数引用,并在渲染器整个寿命期间提供这些函数引用. 它由`WebGLRenderer`创建,并在内部用于将统一数据上传到GPU荫影程序.

**构造函数**

`new WebGLShaderSetterWrapper(renderer)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有此 WebGLSHederSetterWrapper 的 WebGLRender 实例 。 |

---


**作用域**: static

> 源码：[src/renderer/webgl/wrappers/WebGLShaderSetterWrapper.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLShaderSetterWrapper.js#L9)  
引入版本：4.0.0

## 公开成员 {#public-members}

### constants {#constants}

#### constants: [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetterConstants](/api/typedef/types-renderer-webgl-wrappers#shadersetterconstants) {#constants-phasertypesrendererwebglwrappersshadersetterconstants}


**说明:**

键入的查询表 WebGL 键入常数( 小时值) , 将每个 GLSL 数据类型映射到其统一的设置函数、 组件计数、 字节大小每个组件, 以及显示该类型是否为矩阵的旗帜。 当将统一值上传到阴影程序时使用, 这样正确 。 WebGL 调用是自动选择的,用于每种制服的申报类型。


> 源码：[src/renderer/webgl/wrappers/WebGLShaderSetterWrapper.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLShaderSetterWrapper.js#L36)  
引入版本：4.0.0


---

---
