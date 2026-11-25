# Types.Renderer.WebGL {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-renderer-webgl)

## ShaderAdditionConfig {#shaderadditionconfig}

### \<static> ShaderAdditionConfig {#static-shaderadditionconfig}


一个ShaderAddition Config定义了要添加到阴影程序中的附加.
它包括一个名称,一组阴影加法,以及可选标记.

名称作为识别阴影加法的密钥.
它被用作遮荫程序的独特标识符的一部分.

着色器的添加是键值对弦,
中键为添加值的模板。
这一点在底荫程序源代码中找到,作为
`#pragma phaserTemplate(key)`.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 遮荫加法名,用作密钥. |
| additions | object | 否 | 应用阴影添加。每个添加是按键值对字符串,其中键是添加该值的模板。如果模板在两个字符串中都存在,则键既适用于顶点编码,也适用于碎片阴影代码。 |
| tags | Array.\<string> | 是 | 用于描述遮荫器添加的可选标记. |
| disable | boolean | 是 | 是否在编译阴影时忽略此添加 。 |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL
> 源码：[src/renderer/webgl/typedefs/ShaderAdditionConfig.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/typedefs/ShaderAdditionConfig.js#L7)  
引入版本：4.0.0

---

## WebGLAttributeLayout {#webglattributelayout}

### \<static> WebGLAttributeLayout {#static-webglattributelayout}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 名称 | string | 否 |  | 属性名称,按阴影定义. |
| size | number | 否 |  | 每个顶点属性的组件数量. |
| 类型 | GLenum \| string | 否 |  | 阵列中每个组件的数据类型。 只要WebGL能够转换类型, 与着色器中的类型不同。 如果类型是字符串, 则会转换成相应的 GLenum, 例如“ FLOAT” 。 Name |
| normalized | boolean | 否 |  | 是否在投放到浮点时将整数数据值正常化 。 |
| offset | number | 否 |  | 字节从缓冲的开始抵消. |
| bytes | number | 是 | 4 | 每个顶点属性的字节数。 这是类型大小, 一般为 FLOAT 或 INT 的 4 字节 。 |
| columns | number | 是 | 1 | 属性数据中的列数。将矩阵作为列向量,并增加列,以匹配矩阵大小。 |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL
> 源码：[src/renderer/webgl/typedefs/WebGLAttributeBufferLayout.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/typedefs/WebGLAttributeBufferLayout.js#L7)  
引入版本：4.0.0

---

## WebGLAttributeBufferLayout {#webglattributebufferlayout}

### \<static> WebGLAttributeBufferLayout {#static-webglattributebufferlayout}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| stride | number | 否 | 属性数据的步态 。 |
| count | number | 否 | 缓冲器中元素的最大数量 。 |
| usage | GLenum \| string | 否 | 数据存储的用法模式 。 gl.STATIC_ DRAW, gl.DYNAMIC_DRAW 或 gl.STREAM_ DRAW。 如果类型是字符串, 则会转换成相应的 GLenum, 如“ STATIC_ DARAW” 。 |
| instanceDivisor | number | 是 | 属性数据的实例divisor。 这是在移动到下一个时要绘制多少个顶点。 它只用于实例渲染 。 |
| layout | [Phaser.Types.Renderer.WebGL.WebGLAttributeLayout](/api/typedef/types-renderer-webgl#webglattributelayout) | 否 | 属性数据的布局. |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL
> 源码：[src/renderer/webgl/typedefs/WebGLAttributeBufferLayout.js#L20](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/typedefs/WebGLAttributeBufferLayout.js#L20)  
引入版本：4.0.0

---

## WebGLBatchEntry {#webglbatchentry}

### \<static> WebGLBatchEntry {#static-webglbatchentry}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| start | number | 否 | 顶点数 本批次条目起始. |
| count | number | 否 | 本批次条目中顶点总数. |
| unit | number | 否 | 批次条目的当前纹理单元. |
| maxUnit | number | 否 | 本批次条目中纹理单位的最大数量. |
| texture | Array.\<[Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper)> | 否 | 本批次条目中使用的WebGLTextureWrapper参考文献数组. |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL
> 源码：[src/renderer/webgl/typedefs/WebGLBatchEntry.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/typedefs/WebGLBatchEntry.js#L1)  
引入版本：4.0.0

---

## WebGLBlendParameters {#webglblendparameters}

### \<static> WebGLBlendParameters {#static-webglblendparameters}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| enabled | GLboolean | 是 | 是否启用混合 。 |
| color | Array.\<GLclampf> | 是 | 混合颜色(RGBA,0-1). |
| equation | Array.\<GLenum> | 是 | 混合方程,第一个值是RGB方程,第二个值是α方程. |
| func | Array.\<GLenum> | 是 | 混合函数。 值是 `srcRGB`, `dstRGB`, `srcAlpha`, `dstAlpha`. |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL
> 源码：[src/renderer/webgl/typedefs/WebGLBlendParameters.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/typedefs/WebGLBlendParameters.js#L7)  
引入版本：4.0.0

---

## WebGLConst {#webglconst}

### \<static> WebGLConst {#static-webglconst}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| enum | GLenum | 否 | 属性的数据类型,即: `gl.BYTE`, `gl.SHORT`, `gl.UNSIGNED_BYTE`, `gl.FLOAT`等 类. |
| size | number | 否 | 数据类型的大小,以字节表示. |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL
> 源码：[src/renderer/webgl/typedefs/WebGLConst.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/typedefs/WebGLConst.js#L1)  
引入版本：3.50.0

---

## WebGLGlobalParameters {#webglglobalparameters}

### \<static> WebGLGlobalParameters {#static-webglglobalparameters}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bindings | object | 是 | 资源要受约束。 |
| bindings.activeTexture | GLint | 是 | 主动纹理单位. |
| bindings.arrayBuffer | [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) | 是 | 顶点阵列缓冲器来绑定. |
| bindings.elementArrayBuffer | [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) | 是 | 用于绑定的索引数组缓冲器 。 |
| bindings.framebuffer | [Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](/api/class/renderer-webgl-wrappers-webglframebufferwrapper) | 是 | 装帧器来装订 |
| bindings.program | [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](/api/class/renderer-webgl-wrappers-webglprogramwrapper) | 是 | 装订程序 |
| bindings.renderbuffer | WebGLRenderbuffer | 是 | 束缚器 |
| blend | [Phaser.Types.Renderer.WebGL.WebGLBlendParameters](/api/typedef/types-renderer-webgl#webglblendparameters) | 是 | 组合参数设置 。 |
| colorClearValue | Array.\<Float32Array> | 是 | 清除颜色缓冲器的颜色到. 4 元素, RGBA. |
| colorWritemask | Array.\<GLboolean> | 是 | 颜色写掩码设置 。 4 元素, RGBA 。 |
| cullFace | boolean | 是 | 是否启用 culling 。 |
| depthTest | boolean | 是 | 是否启用深度测试 。 |
| scissor | object | 是 | 要设置剪刀参数 。 |
| scissor.enable | boolean | 是 | 是否启用剪切 。 |
| scissor.box | Array.\<Int32Array> | 是 | 剪刀矩形设置. 4 元素 XYWH 。 注意这些元素以 WebGL 格式存储, 由下而上, 因此 Y 坐标被反转以显示空间 。 |
| stencil | [Phaser.Types.Renderer.WebGL.WebGLStencilParameters](/api/typedef/types-renderer-webgl#webglstencilparameters) | 是 | 要设置的调温参数 。 |
| texturing | object | 是 | 要设置的纹理设置。 这些设置在创建纹理时生效 。 |
| texturing.flipY | GLboolean | 是 | 是否应该将纹理翻转到 Y 轴上 ? |
| texturing.premultiplyAlpha | GLboolean | 是 | 纹理应该预先多倍化的α吗? |
| vao | [Phaser.Renderer.WebGL.Wrappers.WebGLVAOWrapper](/api/class/renderer-webgl-wrappers-webglvaowrapper) | 是 | 要绑定的 Vertex 矩阵对象。 这控制顶点属性状态 。 |
| viewport | Array.\<Int32Array> | 是 | 景点设置. 4元素, XYWH. |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL
> 源码：[src/renderer/webgl/typedefs/WebGLGlobalParameters.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/typedefs/WebGLGlobalParameters.js#L7)  
引入版本：4.0.0

---

## WebGLStencilParameters {#webglstencilparameters}

### \<static> WebGLStencilParameters {#static-webglstencilparameters}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| enabled | GLboolean | 是 | 是否启用了天线测试 。 |
| func | object | 是 | Stencil 函数参数 。 |
| func.func | GLenum | 否 | 比较功能. |
| func.ref | GLint | 否 | 速记测试的参考值 。 |
| func.mask | GLuint | 否 | 口罩适用于天花板测试. |
| op | object | 是 | 斯坦西尔的操作参数. |
| op.fail | GLenum | 否 | 如果天线测试失败, 操作要进行 。 |
| op.zfail | GLenum | 否 | 如果深度测试失败, 操作要进行 。 |
| op.zpass | GLenum | 否 | 如果测深测试通过,深度测试通过或禁用,则执行操作. |
| clear | GLint | 是 | 清除天线缓冲器的值 。 |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL
> 源码：[src/renderer/webgl/typedefs/WebGLStencilParameters.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/typedefs/WebGLStencilParameters.js#L7)  
引入版本：4.0.0

---

## WebGLTextureCompression {#webgltexturecompression}

### \<static> WebGLTextureCompression {#static-webgltexturecompression}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ASTC | object \| undefined | 否 | 表示是否支持ASTC压缩(大多为iOS). |
| ATC | object \| undefined | 否 | 指示是否支持ATC压缩 。 |
| BPTC | object \| undefined | 否 | 指示是否支持BPTC压缩 。 |
| ETC | object \| undefined | 否 | 表示ETC压缩是否被支持(大多是Android). |
| ETC1 | object \| undefined | 否 | 表示是否支持ETC1压缩(多为Android). |
| IMG | object \| undefined | 否 | 表示浏览器支持真实的颜色图像(所有浏览器). |
| PVRTC | object \| undefined | 否 | 表示是否支持PVRTC压缩(大多为iOS). |
| RGTC | object \| undefined | 否 | 表示是否支持RGTC压缩(多为iOS). |
| S3TC | object \| undefined | 否 | 表示当前设备(大多为Windows)是否支持S3TC压缩. |
| S3TCSRGB | object \| undefined | 否 | 表示当前设备(大多为Windows)是否支持S3TCSRGB压缩. |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL
> 源码：[src/renderer/webgl/typedefs/WebGLTextureCompression.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/typedefs/WebGLTextureCompression.js#L1)  
引入版本：3.55.0

---

## WebGLUniform {#webgluniform}

### \<static> WebGLUniform {#static-webgluniform}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| location | GLint | 否 | 制服的位置. |
| 类型 | GLenum | 否 | 服之类. |
| size | GLint | 否 | 制服的尺寸,元素中. |
| value | number \| Array.\<number> | 否 | 制服的价值. |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL
> 源码：[src/renderer/webgl/typedefs/WebGLUniform.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/typedefs/WebGLUniform.js#L7)  
引入版本：4.0.0

---

---
