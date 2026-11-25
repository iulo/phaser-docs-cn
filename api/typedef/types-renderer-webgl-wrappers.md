# Types.Renderer.WebGL.Wrappers {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-renderer-webgl-wrappers)

## ShaderSetter {#shadersetter}

### \<static> ShaderSetter {#static-shadersetter}


WebGL常数和功能用于设定遮蔽制服.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| constant | GLenum | 否 | GL 常数描述数据类型. |
| baseType | GLenum | 否 | GL 常数描述基础数据类型。 这与非阵列类型中的 `constant` 相同 。 |
| size | number | 否 | 数据类型中的元素数量. |
| bytes | number | 否 | 数据类型中每个元素的字节数。 |
| set | function | 否 | WebGL功能设定制服. |
| setV | function | 否 | WebGL功能设置带有值数组(vector)的制服. |
| isMatrix | boolean | 否 | 制服是否为矩阵 。 |

**类型**: object

**所属**: Phaser.Types.Renderer.WebGL.Wrappers
> 源码：[src/renderer/webgl/wrappers/typedefs/ShaderSetter.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/typedefs/ShaderSetter.js#L7)  
引入版本：4.0.0

---

## ShaderSetterConstants {#shadersetterconstants}

### \<static> ShaderSetterConstants {#static-shadersetterconstants}


一套用于设定不同类型遮荫制服的ShaderSetter描述符集.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 0x1404 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | 缩写 |
| 0x8B53 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | gl.INT_VEC2 数据 |
| 0x8B54 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | gl.INT_VEC3 数据 |
| 0x8B55 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | gl.INT_VEC4 数据格式 |
| 0x1406 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | 胶片 |
| 0x8B50 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | gl.FLOAT_VEC2 维基月球在线解说-双子星. |
| 0x8B51 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | gl.FLOAT_VEC3 维基月球在线解说-多维环球网 |
| 0x8B52 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | gl.FLOAT_VEC4 维基月球在线解说-多维环球网 |
| 0x1405 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | gl. 已签名_INT |
| 0x1400 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | 格列尔贝特 |
| 0x1401 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | 格莱特(签名) |
| 0x1402 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | 缩写 |
| 0x1403 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | 斜拉线 |
| 0x8B56 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | 格卢.博尔 |
| 0x8B57 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | gl.bOOL_VEC2 常规 |
| 0x8B58 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | 光学图 |
| 0x8B59 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | gl.bOL_VEC4 常规部分: 第23页, 1.A.1.a.2.c |
| 0x8B5A | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | gl.FLOAT_MAT2 数据 |
| 0x8B5B | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | gl.FLOAT_MAT3 图像 |
| 0x8B5C | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | gl.FLOAT_MAT4 数据 |
| 0x8B5E | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | gl. SAMPLER_2D 导弹发射装置 |
| 0x8B60 | [Phaser.Types.Renderer.WebGL.Wrappers.ShaderSetter](/api/typedef/types-renderer-webgl-wrappers#shadersetter) | 否 | gl. 桑普尔_ CUBE |

**类型**: object

**所属**: Phaser.Types.Renderer.WebGL.Wrappers
> 源码：[src/renderer/webgl/wrappers/typedefs/ShaderSetterConstants.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/typedefs/ShaderSetterConstants.js#L7)  
引入版本：4.0.0

---

---
