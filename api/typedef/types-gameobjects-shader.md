# Types.GameObjects.Shader {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-shader)

## ShaderConfig {#shaderconfig}

### \<static> ShaderConfig {#static-shaderconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | string \| [Phaser.Types.GameObjects.Shader.ShaderQuadConfig](/api/typedef/types-gameobjects-shader#shaderquadconfig) | 否 |  | 用于此 Shader 的配置对象。 它也可以是阴影缓存中对应的着色器的密钥, 它将在新配置对象中用作 `fragmentKey` 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Shader
> 源码：[src/gameobjects/shader/typedefs/ShaderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/typedefs/ShaderConfig.js#L1)  
引入版本：3.50.0

---

## ShaderQuadConfig {#shaderquadconfig}

### \<static> ShaderQuadConfig {#static-shaderquadconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 渲染节点的名称。 如果未设定, 也会用于 `shaderName` 。 |
| shaderName | string | 是 | 着色器的名称。 此名称作为内部着色器名称的根茎。 如果存在另一个同名着色器, 则该名称将被使用, 所以最好使用一个独特的名称 。 |
| fragmentSource | string | 是 | 碎片遮蔽源代码,它覆盖 `fragmentKey`中设置的任何内容 。 |
| vertexSource | string | 是 | 顶点阴影源代码。 此代码将覆盖 `vertexKey` 中设置的任意内容 。 |
| fragmentKey | string | 是 | 从遮荫缓存中使用的碎片遮荫源的密钥 。 |
| vertexKey | string | 是 | 从遮荫缓存中使用顶点遮荫源的密钥. |
| setupUniforms | function | 是 | 设置着色器需要的一致值的函数。 它需要两个参数: `setUniform` 财务报告和已审计财务报表 `drawingContext`. `setUniform` 是函数 `(name: string, value: any) => void` 用于设置统一值。 `drawingContext` 是当前绘图上下文。 |
| initialUniforms | object | 是 | 包含初始统一值的对象。 键是统一名称, 而值是统一值。 用于在第一次渲染前设置阴影 。 |
| shaderAdditions | Array.\<[Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig)> | 是 | 添加到着色器中的附加片段。 高级配置选项。 您可以使用 `updateShaderConfig` 在渲染时编辑这些片段, 从而产生不同的阴影 。 |
| updateShaderConfig | function | 是 | 一个更新着色器配置的函数。 高级配置选项。 它需要三个参数: `drawingContext`、 `gameObject`、 `renderNode`。 `drawingContext`是当前绘图上下文。 `gameObject`是正在渲染的对象。 `renderNode`是引用该函数的ShaderQuad渲染节点 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Shader
> 源码：[src/gameobjects/shader/typedefs/ShaderQuadConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/typedefs/ShaderQuadConfig.js#L1)  
引入版本：4.0.0

---

---
