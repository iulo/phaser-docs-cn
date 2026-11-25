# Phaser.Renderer.Canvas {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/function/renderer)

### GetBlendModes {#GetBlendModes}

#### \<static> GetBlendModes() {#static-getblendmodes}


**说明:**

返回一个阵列, 将默认混合模式映射到支持 Canvas 混合模式 。

如果浏览器不支持混合模式,它会默认为普通的`source-over`混合模式.


**返回值:** array - 彩色混合模式对应的就是默认的 Phaser 混合模式。


> 源码：[src/renderer/canvas/utils/GetBlendModes.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/utils/GetBlendModes.js#L10)  
引入版本：3.0.0


### SetTransform {#SetTransform}

#### \<static> SetTransform(renderer, ctx, src, camera, [parentMatrix]) {#static-settransformrenderer-ctx-src-camera-parentmatrix}


**说明:**

引用 Canvas 渲染器、 Canvas 渲染上下文、 游戏对象、 相机和母矩阵, 然后执行以下步骤 :

1. 检查源的α与相机α结合。 如果 0 或 更小, 则中止 。

2. 使用相机和游戏对象矩阵,并把它们乘以,如果给出的话,与母矩阵结合。

3. 设置上下文的混合模式,以作为游戏对象所使用的模式。

4. 设定上下文的α值,以游戏对象与相机结合使用。

5. 保存上下文状态。

6. 通过 setTransform 将最终矩阵值设置到上下文中。

7. 如果游戏对象有纹理框架, imageSmoothingEnabled 以帧. source 设置。scaleMode.

8. 如果游戏对象没有纹理框架,imageSmoothingEnabled则基于Render.antalias设定.

此功能仅用于内部, 大部分Canvas Renderer 类都使用它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) | 否 | 参考当前活跃的Canvas渲染器. |
| ctx | CanvasRenderingContext2D | 否 | 设置转换的画布上下文 。 |
| src | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 正在渲染游戏对象。 可以是扩展基类的任意类型 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 正在制作游戏对象的相机 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 父变换矩阵,在渲染前应用到 Game Object 上. |


**返回值:** boolean - 如果设定了游戏对象上下文,则使用`true`,否则使用`false`.


> 源码：[src/renderer/canvas/utils/SetTransform.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/utils/SetTransform.js#L9)  
引入版本：3.12.0


# Phaser.Renderer.Snapshot {#page-title-1}

### Canvas {#Canvas}

#### \<static> Canvas(canvas, config) {#static-canvascanvas-config}


**说明:**

绘制画布显示的当前框架的快照。 根据配置, 它可以以三种模式之一运行: 单像素颜色取样、 局部区域捕获或全画布捕获 。

在像素模式下,读取给定(x,y)坐标的颜色,并立即用`Phaser.Display.Color`对象引用回调.

在区域或全捕获模式中,相关区域被编码为数据 URL,并被指定给一个新的图像对象。一旦图像被装入,就会以图像为参数引用Snapshot配置对象中提供的调用回调。如果图像未能装入,则仍然引用调用回调,但没有参数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| canvas | HTMLCanvasElement | 否 | 画布来拍一张照片 |
| config | [Phaser.Types.Renderer.Snapshot.SnapshotState](/api/typedef/types-renderer-snapshot#snapshotstate) | 否 | 即时配置对象 。 |


> 源码：[src/renderer/snapshot/CanvasSnapshot.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/snapshot/CanvasSnapshot.js#L11)  
引入版本：3.0.0


### WebGL {#WebGL}

#### \<static> WebGL(sourceContext, config) {#static-webglsourcecontext-config}


**说明:**

取出一个由 WebGL 画布显示的当前框架的快照,或者读取一个像素的颜色值,这取决于快照配置对象的 `getPixel` 属性.

捕获一个区域时,原始像素数据从 WebGL 上下文读取,并合成到一个临时画布,核算 WebGL 的反转Y轴,并可选地逆转预先多倍化的α. 画布然后被串装到数据 URL 并装入一个图像对象,一旦装入完成,就会传递到Snapshot配置对象定义的回调中.

在读取单个像素时,给定坐标的RGBA值直接通过`gl.readPixels`读取,并通过调用返回作为`Phaser.Display.Color`对象.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sourceContext | WebGLRenderingContext | 否 | 需要一览的 WebGL上下文 。 |
| config | [Phaser.Types.Renderer.Snapshot.SnapshotState](/api/typedef/types-renderer-snapshot#snapshotstate) | 否 | 即时配置对象 。 |


> 源码：[src/renderer/snapshot/WebGLSnapshot.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/snapshot/WebGLSnapshot.js#L11)  
引入版本：3.0.0


# Phaser.Renderer.WebGL.ShaderAdditionMakers {#page-title-2}

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


# Phaser.Renderer.WebGL.Utils {#page-title-3}

### getTintFromFloats {#getTintFromFloats}

#### \<static> getTintFromFloats(r, g, b, a) {#static-gettintfromfloatsr-g-b-a}


**说明:**

将 0.0 到 1.0 之间的四个浮点装入一个 Uint32

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| r | number | 否 | 红色组件,介于 0.0 到 1.0 之间 |
| g | number | 否 | 绿色成分,介于 0.0 到 1.0 之间 |
| b | number | 否 | 蓝色成分,介于 0.0 到 1.0 之间 |
| a | number | 否 | 阿尔法组件,范围为 0.0 到 1.0 |


**返回值:** number - 装入的 RGBA 值为 Uint32 。


> 源码：[src/renderer/webgl/Utils.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/Utils.js#L17)  
引入版本：3.0.0


### getTintAppendFloatAlpha {#getTintAppendFloatAlpha}

#### \<static> getTintAppendFloatAlpha(rgb, a) {#static-gettintappendfloatalphargb-a}


**说明:**

包装一个代表 RGB 组件的 Uint24, 并装有代表α组件的 Float32, 范围在 0.0 和 1.0 之间, 并返回一个 Uint32

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rgb | number | 否 | 代表 RGB 组件的 Uint24 |
| a | number | 否 | 代表阿尔法组件的浮点32 |


**返回值:** number - 包装为 Uint32 的 RGBA


> 源码：[src/renderer/webgl/Utils.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/Utils.js#L40)  
引入版本：3.0.0


### getTintAppendFloatAlphaAndSwap {#getTintAppendFloatAlphaAndSwap}

#### \<static> getTintAppendFloatAlphaAndSwap(rgb, a) {#static-gettintappendfloatalphaandswaprgb-a}


**说明:**

包装一个代表 RGB 组件的 Uint24, 并装有代表α组件的 Float32, 范围在 0.0 和 1.0 之间, 并返回一个与红和蓝通道交换的旋绕的 Uint32( RGB 成为 BGR)

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rgb | number | 否 | 代表 RGB 组件的 Uint24 |
| a | number | 否 | 代表阿尔法组件的浮点32 |


**返回值:** number - 包装为 Uint32 的 RGBA


> 源码：[src/renderer/webgl/Utils.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/Utils.js#L59)  
引入版本：3.0.0


### getFloatsFromUintRGB {#getFloatsFromUintRGB}

#### \<static> getFloatsFromUintRGB(rgb) {#static-getfloatsfromuintrgbrgb}


**说明:**

将一个 Uint24 RGB 拆卸成数值在 0.0 到 1.0 之间的浮动阵列

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rgb | number | 否 | RGB 装入 Uint24 时 |


**返回值:** array - 以浮点表示每个组件的浮点阵


> 源码：[src/renderer/webgl/Utils.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/Utils.js#L82)  
引入版本：3.0.0


### checkShaderMax {#checkShaderMax}

#### \<static> checkShaderMax(gl, maxTextures) {#static-checkshadermaxgl-maxtextures}


**说明:**

选中可查看 GPU 在片段阴影中支持的纹理单元 , 以及是否允许游戏配置中指定的值 。

由于Android设备上的性能原因,这个值硬解为16.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gl | WebGLRenderingContext | 否 | WebGLContext用来创建阴间. |
| maxTextures | number | 否 | 游戏配置 maxTextures值. |


**返回值:** number - 此浏览器和 GPU 支持的纹理单元的数量 。


> 源码：[src/renderer/webgl/Utils.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/Utils.js#L101)  
引入版本：3.50.0


### updateLightingUniforms {#updateLightingUniforms}

#### \<static> updateLightingUniforms(enable, drawingContext, programManager, textureUnit, vec, [selfShadow], [selfShadowPenumbra], [selfShadowThreshold]) {#static-updatelightinguniformsenable-drawingcontext-programmanager-textureunit-vec-selfshadow-selfshadowpenumbra-selfshadowthreshold}


**说明:**

设置或清除给定的荫影程序管理器上所有与照明相关的制服.

`enable`是`true`时,此函数会查询Scene的灯光管理器对相机可见的所有活动灯光进行查询,并将它们的位置,颜色,强度,以及光度作为统一的阵列上传到遮荫层。它也会上传环境光色,相机变换,以及普通的地图纹理单元。通过上传笔光和散射阈值制服,可以选择地实现自我遮蔽。

当 `enable`是 `false`时,所有先前设置的照明制服都会从程序管理器中移除. 如果Scene没有活动光管理器,则函数会提前返回而无需做任何更改.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| enable | boolean | 否 | 是否启用照明 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 绘图康特实例。 |
| programManager | [Phaser.Renderer.WebGL.ProgramManager](/api/class/renderer-webgl-programmanager) | 否 | 阴影程序管理器实例 。 |
| textureUnit | number | 否 | 用于普通地图的纹理单元。 |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 一种矢量2 实例。 |
| selfShadow | boolean | 是 | 是否启用自我阴影 。 |
| selfShadowPenumbra | number | 是 | 笔形的自影价值. |
| selfShadowThreshold | number | 是 | 自我影视的阈值 。 |


> 源码：[src/renderer/webgl/Utils.js#L133](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/Utils.js#L133)  
引入版本：4.0.0

---
