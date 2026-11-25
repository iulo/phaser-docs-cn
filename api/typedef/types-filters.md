# Types.Filters {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-filters)

## BlockyConfig {#blockyconfig}

### \<static> BlockyConfig {#static-blockyconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| size | number \| [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 | 块大小。如果数字,则将 x 和 Y 设置为相同的值。如果一个矢量2like,则将 x 和 Y 设置为相应的值。 |
| offset | number \| [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 | 区块的偏移。如果数字是x和y,则两者设置为相同值。如果一个矢量2like,则设置为x和y。 |

**类型**: object

**所属**: Phaser.Types.Filters
> 源码：[src/filters/typedefs/BlockyConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/typedefs/BlockyConfig.js#L1)  
引入版本：4.0.0

---

## GradientMapConfig {#gradientmapconfig}

### \<static> GradientMapConfig {#static-gradientmapconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| ramp | [Phaser.Display.ColorRamp](/api/class/display-colorramp) \| [Phaser.Types.Display.ColorBandConfig](/api/typedef/types-display#colorbandconfig) | [Phaser.Display.ColorBand](/api/class/display-colorband) | Array.\<([Phaser.Types.Display.ColorBandConfig](/api/typedef/types-display#colorbandconfig) | [Phaser.Display.ColorBand](/api/class/display-colorband))> | 是 |  | 拟使用的彩色斜坡. |
| dither | boolean | 是 | false | 是否将渐变输出抖动 。 |
| color | Array.\<number> | 是 | "[0, 0, 0, 0]" | 值以加至每个信道. |
| colorFactor | Array.\<number> | 是 | "[0.3, 0.6, 0.1, 0]" | 适用于每个频道的因数。 尽量将它们缩合到 1 。 |
| unpremultiply | boolean | 是 | true | 是否在处理之前先解析颜色数据 。 |
| alpha | number | 是 | 1 | 有多少效果可以混合在原版上. |

**类型**: object

**所属**: Phaser.Types.Filters
> 源码：[src/filters/typedefs/GradientMapConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/typedefs/GradientMapConfig.js#L1)  
引入版本：4.0.0

---

## ImageLightConfig {#imagelightconfig}

### \<static> ImageLightConfig {#static-imagelightconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| normalMap | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 | "'__NORMAL'" | 图像光效果普通映射所用的纹理。 这应该与被过滤的对象匹配。 默认是平面照明 。 |
| environmentMap | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 | "'__WHITE'" | 图像光效应环境图所用的纹理 。 |
| modelMatrix | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 是 |  | 初始模型矩阵。 如果不提供, 将创建默认矩阵 。 |
| modelRotation | number | 是 | 0 | 车型在弧度上的初始旋转. |
| modelRotationSource | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| [Phaser.Types.Filters.ImageLightSourceCallback](/api/typedef/types-filters#imagelightsourcecallback) | null | 是 | null | 模式旋转的来源。 如果函数, 则会叫它来获得旋转。 如果是游戏对象, 则它会用来从游戏对象的世界变换中获取旋转。 如果无效, 模式旋转将取自 modelRotation 属性 。 |
| bulge | number | 是 | 0 | 用于图像光效应的凸起量。 这略微扭曲了表面, 防止了普通地图中的平面区域反映单一的平面颜色。 值为 0.1 的值往往很充足 。 |
| colorFactor | Array.\<number> | 是 | "[1, 1, 1]" | 适用于图像光效应的颜色因子。这可以乘以每个色通道中光线的强度。使用高于1的值来取代高动态范围照明。 |

**类型**: object

**所属**: Phaser.Types.Filters
> 源码：[src/filters/typedefs/ImageLightConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/typedefs/ImageLightConfig.js#L1)  
引入版本：4.0.0

---

## ImageLightSourceCallback {#imagelightsourcecallback}

### \<static> ImageLightSourceCallback {#static-imagelightsourcecallback}

**类型**: function

**所属**: Phaser.Types.Filters
> 源码：[src/filters/typedefs/ImageLightSourceCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/typedefs/ImageLightSourceCallback.js#L1)  
引入版本：4.0.0

---

## KeyConfig {#keyconfig}

### \<static> KeyConfig {#static-keyconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| color | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "[1, 1, 1]" | 用于键的颜色。 它可以是六进制码数或字符串, 3 个数字的阵列在 0 到 1 之间, 也可以是 color 对象 。 |
| alpha | number | 是 | 1 | 需要移除的α 的量。 应该是 0 到 1 之间的值, 但是您可以在此范围之外 , 以获得不同的效果 。 |
| isolate | boolean | 是 | false | 是否保持区域匹配键颜色。 如果选中, 匹配键颜色的区域将被保留, 其余区域将被删除。 如果错误, 匹配键色的区域将被删除, 其他区域将被保留 。 |
| threshold | number | 是 | 0.0625 | 键色的阈值。 如果像素和键色之间的差小于阈值, 则像素被认为是键色。 这应该是 0 到 1 之间的值。 默认阈值是 1 / 16, 对于大多数图像来说, 是一个很好的起点 。 |
| feather | number | 是 | 0 | 键色的羽毛值。 阈值以外的像素, 但仍在羽毛内部, 将是部分匹配值。 这应该是 0 到 1 之间的值 。 |

**类型**: object

**所属**: Phaser.Types.Filters
> 源码：[src/filters/typedefs/KeyConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/typedefs/KeyConfig.js#L1)  
引入版本：4.0.0

---

## NormalToolsConfig {#normaltoolsconfig}

### \<static> NormalToolsConfig {#static-normaltoolsconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| rotation | number | 是 | 0 | 普通地图的二维旋转弧度。 对于更高级的控件, 操纵过滤器的 `viewMatrix` 来控制 3D 旋转 。 |
| rotationSource | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| [Phaser.Types.Filters.NormalToolsSourceCallback](/api/typedef/types-filters#normaltoolssourcecallback) | null | 是 | null | 旋转的来源。 如果函数, 则会叫它来获得旋转。 如果游戏对象, 则它会用来从游戏对象的世界变换得到旋转。 如果无效, 旋转将不会被过滤器更新 。 ] |
| facingPower | number | 是 | 1 | 操纵正常人面对摄像机的倾向。 更高的值会让正常人向摄像机弯曲; 较低的值会让它们弯曲。 这对建议2D场景的深度很有用 。 |
| outputRatio | boolean | 是 | false | 如果真,输出会是一个灰色的纹理,白色区域是正常人面对摄像机的区域,在正交时会逐渐变黑,这可以作为其他效果的基点. |
| ratioVector | [Phaser.Math.Vector3](/api/class/math-vector3) | 是 | "[0, 0, 1]" | 比例输出所用的矢量。 这是比例的计算方向。 默认是摄像机的前进方向。 操纵此方向可以突出显示地图中正面临特定方向的部分。 只有在 outputRatio 属实时才会使用 。 |
| ratioRadius | number | 是 | 1 | 比例输出时, 需要考虑一个半球的多少。 1 时, 将计算整个半球的比例。 0时, 将计算一个点的比例。 这使用与 `PanoramaBlur.radius` 相同的算法。 只有在 outputRatio 属实时才使用 。 |

**类型**: object

**所属**: Phaser.Types.Filters
> 源码：[src/filters/typedefs/NormalToolsConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/typedefs/NormalToolsConfig.js#L1)  
引入版本：4.0.0

---

## NormalToolsSourceCallback {#normaltoolssourcecallback}

### \<static> NormalToolsSourceCallback {#static-normaltoolssourcecallback}

**类型**: function

**所属**: Phaser.Types.Filters
> 源码：[src/filters/typedefs/NormalToolsSourceCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/typedefs/NormalToolsSourceCallback.js#L1)  
引入版本：4.0.0

---

## PanoramaBlurConfig {#panoramablurconfig}

### \<static> PanoramaBlurConfig {#static-panoramablurconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| radius | number | 是 | 1 | 模糊效应的半径。 1 个样本 整个半球; 0 个样本 单个点。 |
| samplesX | number | 是 | 32 | 沿着X轴采集的样本数量。 更多的样本会产生更准确的模糊, 但以性能为代价。 总体中的X轴通常比Y轴要宽 。 |
| samplesY | number | 是 | 16 | 沿着Y轴采集的样本数量。更多的样本会产生更准确的模糊,但以性能为代价。 |
| power | number | 是 | 1 | 应用到样本中的标注。 1 以上的力量会增加黑暗, 让更亮的颜色占据主导地位。 1 以下的力量会增加亮度, 减少亮度的影响。 要模拟 HDR 环境, 以无法以 sRGB 颜色表示的阳光来模拟 HDR 。 |

**类型**: object

**所属**: Phaser.Types.Filters
> 源码：[src/filters/typedefs/PanoramaBlurConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/typedefs/PanoramaBlurConfig.js#L1)  
引入版本：4.0.0

---

## QuantizeConfig {#quantizeconfig}

### \<static> QuantizeConfig {#static-quantizeconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| steps | Array.\<number> | 是 | "[ 8, 8, 8, 8 ]" | 每个频道使用的步数. |
| gamma | Array.\<number> | 是 | "[ 1, 1, 1, 1 ]" | 伽玛每个通道的应用能力. |
| offset | Array.\<number> | 是 | "[ 0, 0, 0, 0 ]" | 折抵以应用每个频道。 |
| dither | boolean | 是 | false | 是否要分解量化值 。 |
| mode | number | 是 | 0 | 色彩空间模式. 0是RGBA. 1是HSVA. 使用HSVA来更好的处理胡桃. |

**类型**: object

**所属**: Phaser.Types.Filters
> 源码：[src/filters/typedefs/QuantizeConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/typedefs/QuantizeConfig.js#L1)  
引入版本：4.0.0

---

---
