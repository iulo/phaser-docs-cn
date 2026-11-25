# Types.Renderer.WebGL.RenderNodes {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-renderer-webgl-rendernodes)

## SubmitterSpriteGPULayerConfig {#submitterspritegpulayerconfig}

### \<static> SubmitterSpriteGPULayerConfig {#static-submitterspritegpulayerconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 名称 | string | 是 | "'SubmitterSpriteGPULayer'" | 伦德节点的名称。 这应该是管理器内部唯一使用的名称 。 |
| vertexSource | string | 是 |  | 顶点阴影源代码。 如果不提供, 将使用默认的四面阴影 。 |
| fragmentSource | string | 是 |  | 碎片阴影源代码。 如果不提供, 将使用默认的四面阴影 。 |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL.RenderNodes
> 源码：[src/renderer/webgl/renderNodes/submitter/typedefs/SubmitterSpriteGPULayerConfig.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/submitter/typedefs/SubmitterSpriteGPULayerConfig.js#L7)  
引入版本：4.0.0

---

## BatchHandlerConfig {#batchhandlerconfig}

### \<static> BatchHandlerConfig {#static-batchhandlerconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 名称 | string | 否 |  | 伦德节点的名称。 这应该是管理器内部唯一使用的名称 。 |
| instancesPerBatch | number | 是 |  | 每批例数。 例数通常是四倍数。 这些因素会进入顶点缓冲的大小。 默认值基于16位顶点指数, 允许65535个顶点。 以 `verticesPerInstance` 来获取例数。 请注意, 16位指数不可能有较多的顶点 。 |
| verticesPerInstance | number | 是 | 4 | 每个实例中唯一顶点的数量。 通常为四重点的4个。 Name |
| indicesPerInstance | number | 是 | 6 | 每个实例的索引数。 用于填充和推进元素缓冲。 默认四位数使用TRIANGLE_ STRIP模式中的 6 个索引 [0, 0, 1, 2, 3, 3] 连接独立四位数与退化的地形。 最小数字为 3 。 |
| maxTexturesPerBatch | number | 是 |  | 每批项的最大纹理数量。 默认为渲染器支持的最大纹理数量。 它用于编译遮荫程序。 在运行时, 管理器可能建议不同的编号, 由节点的 `updateTextureCount`Z 方法解释 。 |
| indexBufferDynamic | boolean | 是 | false | 是否应该创建索引缓冲器作为动态缓冲器。 这对需要频繁修改索引数据的处理者有用 。 |
| shaderName | string | 是 |  | 用于阴影程序的基准名称 。 |
| vertexSource | string | 是 |  | 顶点阴影源代码。 如果不提供, 将使用默认的四面阴影 。 |
| fragmentSource | string | 是 |  | 碎片阴影源代码。 如果不提供, 将使用默认的四面阴影 。 |
| shaderAdditions | Array.\<[Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig)> | 是 |  | 用于阴影程序的阴影添加数组。 |
| shaderFeatures | Array.\<string> | 是 |  | 阴影程序中启用的一组着色器特性。 |
| vertexBufferLayout | [Phaser.Types.Renderer.WebGL.WebGLAttributeBufferLayout](/api/typedef/types-renderer-webgl#webglattributebufferlayout) \| any | 是 |  | 批量处理器的顶点缓冲布局。如果不提供,将使用默认的四重排版式。 `count` 财产将由 `instancesPerBatch` 财务报告和已审计财务报表 `verticesPerInstance` 属性。 `location` 财务报告和已审计财务报表 `bytes` 初始化时,每个属性的属性将自动确定。您可以提供部分WebGLatpiz BufferLayout,在初始化时将自动填充。 |
| vertexBufferLayoutRemove | Array.\<string> | 是 |  | 从顶点缓冲布局中删除一系列属性名称。 这对于删除阴影程序没有使用的属性很有用 。 |
| vertexBufferLayoutAdd | Array.\<([Phaser.Types.Renderer.WebGL.WebGLAttributeLayout](/api/typedef/types-renderer-webgl#webglattributelayout) \| any)> | 是 |  | 用于添加顶点缓冲布局的一组附加属性布局。 这对于向默认的阴影程序添加属性很有用。 您可以提供部分 WebGLatproject Layout, 初始化时将自动填充。 |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL.RenderNodes
> 源码：[src/renderer/webgl/renderNodes/typedefs/BatchHandlerConfig.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/typedefs/BatchHandlerConfig.js#L7)  
引入版本：4.0.0

---

## BatchHandlerQuadRenderOptionsSelfShadow {#batchhandlerquadrenderoptionsselfshadow}

### \<static> BatchHandlerQuadRenderOptionsSelfShadow {#static-batchhandlerquadrenderoptionsselfshadow}


四面体渲染的自阴影选项 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| enabled | boolean | 否 | 是否使用自我影视. |
| penumbra | number | 否 | 自影笔  布拉力. |
| diffuseFlatThreshold | number | 否 | 自影纹亮度相当于平面. |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL.RenderNodes
> 源码：[src/renderer/webgl/renderNodes/typedefs/BatchHandlerQuadRenderOptions.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/typedefs/BatchHandlerQuadRenderOptions.js#L7)  
引入版本：4.0.0

---

## BatchHandlerQuadRenderOptionsLighting {#batchhandlerquadrenderoptionslighting}

### \<static> BatchHandlerQuadRenderOptionsLighting {#static-batchhandlerquadrenderoptionslighting}


点亮四映射的选项 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| normalGLTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 否 | 普通的地图纹理要渲染. |
| normalMapRotation | number | 否 | 普通地图纹理的旋转. |
| selfShadow | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerQuadRenderOptionsSelfShadow](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerquadrenderoptionsselfshadow) | 是 | 自影选择. |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL.RenderNodes
> 源码：[src/renderer/webgl/renderNodes/typedefs/BatchHandlerQuadRenderOptions.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/typedefs/BatchHandlerQuadRenderOptions.js#L18)  
引入版本：4.0.0

---

## BatchHandlerQuadRenderOptions {#batchhandlerquadrenderoptions}

### \<static> BatchHandlerQuadRenderOptions {#static-batchhandlerquadrenderoptions}


配置四映射的着色器能力的选项 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| multiTexturing | boolean | 是 | 是否使用多文字 。 |
| lighting | [Phaser.Types.Renderer.WebGL.RenderNodes.BatchHandlerQuadRenderOptionsLighting](/api/typedef/types-renderer-webgl-rendernodes#batchhandlerquadrenderoptionslighting) | 是 | 如何处理照明。 如果定义了此对象, 将激活照明, 并禁用多文字 。 |
| smoothPixelArt | boolean | 是 | 是否使用平滑像素艺术算法 。 |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL.RenderNodes
> 源码：[src/renderer/webgl/renderNodes/typedefs/BatchHandlerQuadRenderOptions.js#L29](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/typedefs/BatchHandlerQuadRenderOptions.js#L29)  
引入版本：4.0.0

---

## GameObjectBatcherConfig {#gameobjectbatcherconfig}

### \<static> GameObjectBatcherConfig {#static-gameobjectbatcherconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 名称 | string | 否 |  | 伦德节点的名称。 这应该是管理器内部唯一使用的名称 。 |
| batchHandler | string \| [Phaser.Renderer.WebGL.RenderNodes.BatchHandler](/api/class/renderer-webgl-rendernodes-batchhandler) | 是 | "'BatchHandlerQuad'" | 此节点将发送顶点信息的批处理器。 必要时, 批处理器会添加到管理器中。 使用此语句时会引用 `run` 。 此处应该使用阴影配置 。 |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL.RenderNodes
> 源码：[src/renderer/webgl/renderNodes/typedefs/GameObjectBatcherConfig.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/typedefs/GameObjectBatcherConfig.js#L7)  
引入版本：4.0.0

---

## SubmitterQuadConfig {#submitterquadconfig}

### \<static> SubmitterQuadConfig {#static-submitterquadconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 名称 | string | 是 | "'SubmitterQuad'" | 此兰德之号. |
| role | string | 是 | "'Submitter'" | 这个RenderNode的预期角色. |
| batchHandler | string | 是 | "'BatchHandler'" | 用于此 RenderNode 的默认批量处理器节点的密钥。 这应该对应一个扩展 `BatchHandlerQuad` 的节点。 当节点运行时, 它会从游戏对象中衍生出来 。 |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL.RenderNodes
> 源码：[src/renderer/webgl/renderNodes/typedefs/SubmitterQuadConfig.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/typedefs/SubmitterQuadConfig.js#L7)  
引入版本：4.0.0

---

## DrawingContextOptions {#drawingcontextoptions}

### \<static> DrawingContextOptions {#static-drawingcontextoptions}


绘图康特的配置设置 。

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| autoClear | boolean \| Array.\<boolean> | 是 | true | 是否在上下文使用时自动清除帧缓冲器。 如果是数组, 元素是是否分别清除颜色、 深度和 速率缓冲 。 |
| blendMode | number | 是 | 0 | 渲染时使用的混合模式 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | null | 用于此上下文的相机 。 |
| clearColor | Array.\<number> | 是 | "[0, 0, 0, 0]" | 清除帧缓冲器的颜色。 这是由4个值组成的阵列: 红色、 绿色、 蓝色、 α 。 |
| useCanvas | boolean | 是 | false | 是否使用画布作为帧缓冲器 。 |
| copyFrom | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 是 |  | 复制到的绘图康特文 。 |
| enableMipmap | boolean | 是 | false | 是否启用帧缓冲纹理上的 mipmaps, 如果它存在 。 |
| width | number | 是 |  | 帧缓冲器的宽度, 如果未设置 `copyFrom` 和 `useCanvas` , 则使用。 默认是渲染器宽度 。 |
| height | number | 是 |  | 帧缓冲器的高度, 如果未设置 `copyFrom` 和 `useCanvas` , 则使用。 默认是渲染器的高度 。 |
| pool | [Phaser.Renderer.WebGL.DrawingContextPool](/api/class/renderer-webgl-drawingcontextpool) | 是 |  | 不再需要时返回的集合。 仅用于临时背景 。 |

**类型**: object

**Member of**: Phaser.Types.Renderer.WebGL.RenderNodes
> 源码：[src/renderer/webgl/typedefs/DrawingContextOptions.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/typedefs/DrawingContextOptions.js#L7)  
引入版本：4.0.0

---

---
