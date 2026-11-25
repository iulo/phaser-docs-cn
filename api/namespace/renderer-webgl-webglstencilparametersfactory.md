# Phaser.Renderer.WebGL.WebGLStencilParametersFactory {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/renderer-webgl-webglstencilparametersfactory)

Scope: 
static
> 源码：[src/renderer/webgl/parameters/WebGLStencilParametersFactory.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/parameters/WebGLStencilParametersFactory.js#L7)  
引入版本：4.0.0

## 静态函数 {#static-functions}

### create {#create}

#### \<instance> create(renderer, [enabled], [func], [funcRef], [funcMask], [opFail], [opZfail], [opZpass], [clear]) {#instance-createrenderer-enabled-func-funcref-funcmask-opfail-opzfail-opzpass-clear}


**说明:**

创建新 `WebGLStencilParameters` 对象,将全速缓冲配置封装为 a WebGL 使参数通过。返回对象将参数分组到渲染器预期的三个子对象中: `func` (传至 `gl.stencilFunc`), `op` (传至 `gl.stencilOp`),以及 `clear` (清除时所写的值) 所有参数都是可选的,并返回到合理的不开放默认值,所以该定时缓冲符的行为就像被禁用一样。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 |  | 创建 WebGLStencilParameters 的 WebGLRenderer 程序 。 |
| enabled | GLboolean | 是 | false | 是否启用了天线测试 。 |
| func | GLenum | 是 | "GL_ALWAYS" | 用于比较参考值与当前stencil缓冲值的stencil比较函数. |
| funcRef | GLint | 是 | 0 | 在stencil测试中比较stencil缓冲值的参考值. |
| funcMask | GLuint | 是 | "0xFF" | 对比前,比特式掩码既适用于参考值,也适用于速率缓冲值. |
| opFail | GLenum | 是 | "GL_KEEP" | 如果天线测试失败, 操作要进行 。 |
| opZfail | GLenum | 是 | "GL_KEEP" | 如果测速测试通过但深度测试失败,则操作进行. |
| opZpass | GLenum | 是 | "GL_KEEP" | 如果测深测试通过,深度测试通过或禁用,则执行操作. |
| clear | GLint | 是 | 0 | 清除天线缓冲器的值 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.WebGLStencilParameters](/api/typedef/types-renderer-webgl#webglstencilparameters) - 创建的 WebGLStencilParameters. 中国植物物种信息数据库.


> 源码：[src/renderer/webgl/parameters/WebGLStencilParametersFactory.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/parameters/WebGLStencilParametersFactory.js#L19)  
引入版本：4.0.0


---

---
