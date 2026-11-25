# Phaser.Renderer.WebGL.ShaderAdditionMakers {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/renderer-webgl-shaderadditionmakers)

Scope: 
static
> 源码：[src/renderer/webgl/shaders/additionMakers/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/index.js#L7)  


## 静态函数 {#static-functions}

### MakeAnimLength {#MakeAnimLength}

#### \<static> MakeAnimLength(maxAnims, [disable]) {#static-makeanimlengthmaxanims-disable}


**说明:**

返回用于定义最大动画帧数的 ShaderAddition Config。此功能被 TilemapGPULayer 使用 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| maxAnims | number | 否 |  | 支持的动画框架的最大数量。此值作为 `MAX_ANIM_FRAMES` 预处理器常数注入着色器中。 |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeAnimLength.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeAnimLength.js#L7)  
引入版本：4.0.0


---

### MakeApplyLighting {#MakeApplyLighting}

#### \<static> MakeApplyLighting([disable]) {#static-makeapplylightingdisable}


**说明:**

创建并返回 a `ShaderAdditionConfig` 将正常映射灯注入到 WebGL 遮蔽管。如果添加到渲染器中,则包括 `ApplyLighting` 碎片阴影和运行中的 GLSL 头 `applyLighting(fragColor, normal)` 将照明结果混入输出颜色。

`normal`变量必须在碎片遮蔽器中可用.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeApplyLighting.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeApplyLighting.js#L9)  
引入版本：4.0.0


---

### MakeApplyTint {#MakeApplyTint}

#### \<static> MakeApplyTint([disable]) {#static-makeapplytintdisable}


**说明:**

返回用于对纹理应用的 shaderAddition 配置 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeApplyTint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeApplyTint.js#L9)  
引入版本：4.0.0


---

### MakeBoundedSampler {#MakeBoundedSampler}

#### \<static> MakeBoundedSampler([disable]) {#static-makeboundedsamplerdisable}


**说明:**

返回一个用于有界纹理取样的阴影添加连接。 如果纹理坐标位于纹理界限之外, 则有界纹理取样器将返回透明像素 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeBoundedSampler.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeBoundedSampler.js#L9)  
引入版本：4.0.0


---

### MakeDefineLights {#MakeDefineLights}

#### \<static> MakeDefineLights([disable]) {#static-makedefinelightsdisable}


**说明:**

返回用于定义碎片遮蔽器中的灯光和核心照明算法的ShaderAddition Config。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeDefineLights.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeDefineLights.js#L9)  
引入版本：4.0.0


---

### MakeDefineTexCount {#MakeDefineTexCount}

#### \<static> MakeDefineTexCount(maxTextures, [disable]) {#static-makedefinetexcountmaxtextures-disable}


**说明:**

返回用于定义多文本阴影中纹理计数的ShaderAddition Config。此功能被其他添加用于处理纹理的正确数量。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| maxTextures | number | 否 |  | 着色器支持的最大纹理数量。 此值用于设置碎片着色器中定义的 `TEXTURE_COUNT` 预处理器 。 |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeDefineTexCount.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeDefineTexCount.js#L7)  
引入版本：4.0.0


---

### MakeFlatNormal {#MakeFlatNormal}

#### \<static> MakeFlatNormal([disable]) {#static-makeflatnormaldisable}


**说明:**

返回用于定义平坦普通的阴影添加配置。用于点亮没有普通地图的物体。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeFlatNormal.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeFlatNormal.js#L7)  
引入版本：4.0.0


---

### MakeGetNormalFromMap {#MakeGetNormalFromMap}

#### \<static> MakeGetNormalFromMap([disable]) {#static-makegetnormalfrommapdisable}


**说明:**

返回一个向碎片遮蔽器头注入 `getNormalFromMap` 函数的ShaderAddition Config, 并在碎片处理过程中在当前的纹理坐标上对普通地图进行样本。 由此产生的正常矢量被照明管道用于将每个像素的照明应用到纹理上 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeGetNormalFromMap.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeGetNormalFromMap.js#L9)  
引入版本：4.0.0


---

### MakeGetTexCoordOut {#MakeGetTexCoordOut}

#### \<static> MakeGetTexCoordOut([disable]) {#static-makegettexcoordoutdisable}


**说明:**

返回一个阴影附加配置,通过 `outTexCoord` 变量从顶点着色器获取纹理坐标。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeGetTexCoordOut.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeGetTexCoordOut.js#L7)  
引入版本：4.0.0


---

### MakeGetTexRes {#MakeGetTexRes}

#### \<static> MakeGetTexRes([disable]) {#static-makegettexresdisable}


**说明:**

创建并返回一个 ShaderAddition Config,该图形将 GLSL 片段阴影页眉注入,为从一个统一的分辨率序列中查找纹理分辨率提供辅助功能,该功能用于多文本渲染,其中每个绑定纹理可能具有不同的大小。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeGetTexRes.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeGetTexRes.js#L9)  
引入版本：4.0.0


---

### MakeGetTexture {#MakeGetTexture}

#### \<static> MakeGetTexture([maxTextures], [disable]) {#static-makegettexturemaxtextures-disable}


**说明:**

创建一个用于 WebGL 着色器中多文本采样的 ShaderAddTion Config。 返回的配置将 `getTexture` GLSL 函数注入到碎片遮蔽器头中, 其构建为一个如果... 的链条, 选择基于纹理 ID 的 `maxTextures` 纹理单位。 它还注入一个单行进程, 通过该函数对当前碎片颜色进行样本 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| maxTextures | number | 是 | 1 | 支持的纹理单位数量。 如果... else 链条, 确定纹理选择中产生多少分支 。 |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeGetTexture.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeGetTexture.js#L9)  
引入版本：4.0.0


---

### MakeOutFrame {#MakeOutFrame}

#### \<static> MakeOutFrame([disable]) {#static-makeoutframedisable}


**说明:**

返回一个显示器附加配置,将 `inFrame` 声明为顶点属性,并通过 `outFrame` 变化的碎片着色器传递给碎片着色器。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeOutFrame.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeOutFrame.js#L7)  
引入版本：4.0.0


---

### MakeOutInverseRotation {#MakeOutInverseRotation}

#### \<static> MakeOutInverseRotation([disable]) {#static-makeoutinverserotationdisable}


**说明:**

返回一个用于创建顶点阴影处变化的 `outInverseRotationMatrix` 的 ShaderAddition Config。此矩阵用于照明计算,以正确将正常矢量转换成世界空间,确保光线方向相对于游戏对象的方向适用。

`rotation`变量必须在顶点渲染器中可用.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeOutInverseRotation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeOutInverseRotation.js#L9)  
引入版本：4.0.0


---

### MakeRotationDatum {#MakeRotationDatum}

#### \<static> MakeRotationDatum([disable]) {#static-makerotationdatumdisable}


**说明:**

创建并返回一个 `ShaderAdditionConfig`, 读取 `inTexDatum`顶点属性的旋转值, 并把它暴露为顶点阴影处理阶段的 `float rotation` 变量。 此添加被标记为用照明阴影, 从而能够进行方向和正常的照明计算, 以计算所渲染几何的旋转 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeRotationDatum.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeRotationDatum.js#L7)  
引入版本：4.0.0


---

### MakeSampleNormal {#MakeSampleNormal}

#### \<static> MakeSampleNormal([disable]) {#static-makesamplenormaldisable}


**说明:**

返回一个 `ShaderAdditionConfig`, 将普通地图采样添加到 TilemapGPULayer 着色器中。 添加的样本通过 `uNormSampler` 来显示正常地图纹理, 将存储的 RGB 值从 [0, 1] 范围解码回 [ 1, 1] 范围中的正态方向矢量, 通过 `Samples` 对象曝光结果, 以便其他阴影添加( 如照明计算) 能够消耗它。 添加的标记为 `LIGHTING`, 意味着它只有在使用照明通道时才会生效 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeSampleNormal.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeSampleNormal.js#L7)  
引入版本：4.0.0


---

### MakeSmoothPixelArt {#MakeSmoothPixelArt}

#### \<static> MakeSmoothPixelArt([disable]) {#static-makesmoothpixelartdisable}


**说明:**

创建并返回一个能够平滑像素艺术渲染的 ShaderAddition Config 。

当应用到着色器时,此添加会用块状的采样方法取代标准纹理坐标插值,在使用texel边界时保留脆度像素边缘,同时应用子像素反异名,结果是像素艺术资产在非整流尺度上放大或制成,保留尖端,干净的边缘,而不是双线性过滤带来的模糊度.

内部使用`GL_OES_standard_derivatives` WebGL扩展计算每片裂纹衍生信息,通过`getBlockyTexCoord` GLSL帮助器驱动反异名边缘混合.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeSmoothPixelArt.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeSmoothPixelArt.js#L9)  
引入版本：4.0.0


---

### MakeTexCoordFrameClamp {#MakeTexCoordFrameClamp}

#### \<static> MakeTexCoordFrameClamp([disable]) {#static-maketexcoordframeclampdisable}


**说明:**

返回用于在框架内夹住坐标的阴影添加配置。这可以防止框架边缘的流血。然而,它会在框架边界上形成硬边。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeTexCoordFrameClamp.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeTexCoordFrameClamp.js#L9)  
引入版本：4.0.0


---

### MakeTexCoordFrameWrap {#MakeTexCoordFrameWrap}

#### \<static> MakeTexCoordFrameWrap([disable]) {#static-maketexcoordframewrapdisable}


**说明:**

返回一个用于在框架内包装坐标的阴影添加配置。 这样会让纹理在框架的界限内重复 - 这使得一个 TileSprite 工作。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disable | boolean | 是 | false | 是否在创建时禁用阴影添加 。 |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 遮荫器添加配置.


> 源码：[src/renderer/webgl/shaders/additionMakers/MakeTexCoordFrameWrap.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/shaders/additionMakers/MakeTexCoordFrameWrap.js#L7)  
引入版本：4.0.0


---

---
