# Types.Actions {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-actions)

## AddEffectBloomConfig {#addeffectbloomconfig}

### \<static> AddEffectBloomConfig {#static-addeffectbloomconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| threshold | number | 是 | 0.5 | 下亮度阈值,用于渠道对开花的贡献,范围为0-1. |
| blurRadius | number | 是 | 2 | 开花时光线半径模糊. |
| blurSteps | number | 是 | 4 | 花开中运行模糊的步数。 此值应该总是整数 。 |
| blurQuality | number | 是 | 0 | 光的质量模糊:0(低),1(中)或2(高). |
| blendAmount | number | 是 | 1 | 将开花与原始图像混合的量 。 0 是 0, 1 是 100%。 允许更高的值 。 |
| blendMode | [Phaser.BlendModes](/api/namespace/blendmodes) | 是 | "Phaser.BlendModes.ADD" | 应用花朵时使用的混合模式 。 |
| useInternal | boolean | 是 |  | 是否在效果目标的内部过滤列表中添加过滤器。默认情况下,过滤器会添加到外部过滤器列表中,因此它们相对屏幕运行 。 |

**类型**: object

**Member of**: Phaser.Types.Actions
> 源码：[src/actions/typedefs/AddEffectBloomConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/typedefs/AddEffectBloomConfig.js#L1)  
引入版本：4.0.0

---

## AddEffectBloomReturn {#addeffectbloomreturn}

### \<static> AddEffectBloomReturn {#static-addeffectbloomreturn}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| item | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) \| [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 花朵的物体或相机。 |
| parallelFilters | [Phaser.Filters.ParallelFilters](/api/class/filters-parallelfilters) | 否 | 将模糊的光线与原始图像混合起来的平行过滤器。 |
| threshold | [Phaser.Filters.Threshold](/api/class/filters-threshold) | 否 | 断绝图像较暗光的临界滤镜 |
| blur | [Phaser.Filters.Blur](/api/class/filters-blur) | 否 | 模糊的过滤器,从图像中散发出亮光 。 |

**类型**: object

**Member of**: Phaser.Types.Actions
> 源码：[src/actions/typedefs/AddEffectBloomReturn.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/typedefs/AddEffectBloomReturn.js#L1)  
引入版本：4.0.0

---

## AddEffectShineConfig {#addeffectshineconfig}

### \<static> AddEffectShineConfig {#static-addeffectshineconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| radius | number | 是 | 0.5 | 光线的宽度,按目标大小的比例计算. |
| direction | number | 是 | 0.5 | 0 的光线向右方向移动, 顺时针增加。 方向改变光线从目标哪个角落移动, 这是梯度形状向量的方向 。 |
| scale | number | 是 | 2 | 光线的长度, 与目标大小的比例。 这是梯度形状向量的长度 。 |
| width | number | 是 | 128 | 梯度纹理的宽度。 默认情况下, 由目标产生 。 |
| height | number | 是 | 128 | 梯度纹理的高度。 默认, 这是从目标中衍生出来的 。 |
| bands | [Phaser.Display.ColorBand](/api/class/display-colorband) \| [Phaser.Types.Display.ColorBandConfig](/api/typedef/types-display#colorbandconfig) | Array.\<([Phaser.Display.ColorBand](/api/class/display-colorband) | [Phaser.Types.Display.ColorBandConfig](/api/typedef/types-display#colorbandconfig))> | 是 |  | 自定义渐变中使用的颜色带。 如果定义了, `shineColor` 则不做任何动作 。 |
| colorFactor | Array.\<number> | 是 | "[ 1.15, 0.85, 0.85, 1 ]" | 将图像闪亮部分乘以倍数的系数。 必须是 4 个数字( RGBA) 。 典型的距离是 0-1, 但往往有用 。 |
| displacementMap | string | 是 |  | 用于梯度的离位图。如果没有定义,则不使用离位图。 |
| displacement | number | 是 |  | 如果采用流离失所地图,这就是其力量。 |
| duration | number | 是 | 2000 | 闪光动画的长度(通过tween),以毫秒计. |
| repeatDelay | number | 是 |  | 重复闪光动画之间的延迟. |
| ease | string \| function | 是 |  | 方便模式用于 tween 。 |
| yoyo | boolean | 是 |  | 是否将闪光前后移动。 如果不是设定, 闪光会每次都在相同的方向上横跨图像 。 |
| useExternal | boolean | 是 |  | 是否在外空间添加闪光效果, 与屏幕相关。 默认情况下, 它位于内空间, 与目标相关 。 |
| reveal | boolean | 是 |  | 是否使用曝光模式。 在曝光模式中, 效果只显示图像闪亮的部分; 其他部分是隐藏的。 由于此操作更为简单, 当开启曝光模式时返回对象中不存在 `parallelFilters` 。 |

**类型**: object

**Member of**: Phaser.Types.Actions
> 源码：[src/actions/typedefs/AddEffectShineConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/typedefs/AddEffectShineConfig.js#L1)  
引入版本：4.0.0

---

## AddEffectShineReturn {#addeffectshinereturn}

### \<static> AddEffectShineReturn {#static-addeffectshinereturn}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| item | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) \| [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 闪光所应用的物体或相机. |
| gradient | [Phaser.GameObjects.Gradient](/api/class/gameobjects-gradient) | 否 | 控制闪光区域的梯度。 此处没有添加到场景中, 因此一旦所有引用和调值被销毁, 就会被收集到垃圾 。 |
| dynamicTexture | [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) | 否 | 显示梯度的纹理, 使用任何过滤器后。 目标被摧毁时, 将销毁它。 您可以更早销毁它, 但被 tween 访问, 所以请确保 tween 停止 。 |
| tween | [Phaser.Tweens.Tween](/api/class/tweens-tween) | 否 | 控制梯度运动的扭矩。 当更新时, dynamicTexture 会被重画。 目标被摧毁时, 这会被销毁。 您可以提前销毁, 以阻止梯度更新 。 |
| parallelFilters | [Phaser.Filters.ParallelFilters](/api/class/filters-parallelfilters) | 否 | 将闪光添加到图像的并行过滤器。 如果闪光器处于 `reveal` 模式, 则此功能将不会定义。 属于目标, 当目标被摧毁时将被移除。 您可以自己移除它, 以去除闪光效果, 如果不是 `reveal` 模式的话 。 |
| blendFilter | [Phaser.Filters.Blend](/api/class/filters-blend) | 否 | 以梯度乘以图像闪亮的混合过滤器。 它控制了闪亮度。 在 `reveal`模式中, 这属于目标, 并且将在目标被摧毁时被移除。 如果您要移除闪亮效果, 您可以移除它。 如果不是 `reveal`模式, 它属于 `parallelFilters.top` 。 |

**类型**: object

**Member of**: Phaser.Types.Actions
> 源码：[src/actions/typedefs/AddEffectShineReturn.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/typedefs/AddEffectShineReturn.js#L1)  
引入版本：4.0.0

---

## AddMaskShapeConfig {#addmaskshapeconfig}

### \<static> AddMaskShapeConfig {#static-addmaskshapeconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| shape | string | 是 | "'circle'" | 要创建的形状类型。 这可以是“ 圆形 ” 、 “ 椭圆形 ” 、 “ 方形 ” 或 “ 矩形 ” 。 |
| aspectRatio | number | 是 | 1 | 椭圆和矩形的宽度与高度之比。 |
| invert | boolean | 是 |  | 是否反转掩码, 通常用于创建边框 。 |
| useInternal | boolean | 是 |  | 无论是使用内部还是外部过滤列表。内部遮罩会跟踪游戏对象,并在外部过滤之前执行 。 |
| blurRadius | number | 是 | 0 | 模糊的半径可以应用到遮罩上。 如果 0, 则不应用模糊。 一个好的值是 2 。 |
| blurSteps | number | 是 | 4 | 遮罩上运行模糊的步数。 此值应该总是整数 。 |
| blurQuality | number | 是 | 0 | 任何模糊的质量:0(低),1(中)或2(高). |
| scaleMode | number | 是 | 0 | 配置形状时使用的缩放模式 。 0 设置每个轴以独立填充区域 。 - 1 大小均统一排列, 形状会触碰区域 _ inside_ 。 1 大小均统一显示, 形状会触动区域 _ exide_ 。 |
| padding | number | 是 | 0 | 涂装在蒙蔽区域边缘上应用一个嵌套。 这为模糊蒙蔽的边缘提供空间来软化蒙蔽区域。 |
| region | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 |  | 适合的区域。 如果定义不明确, 将从目标场景范围推断 。 |

**类型**: object

**Member of**: Phaser.Types.Actions
> 源码：[src/actions/typedefs/AddMaskShapeConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/typedefs/AddMaskShapeConfig.js#L1)  
引入版本：4.0.0

---

## CallCallback {#callcallback}

### \<static> CallCallback {#static-callcallback}

**类型**: function

**Member of**: Phaser.Types.Actions
> 源码：[src/actions/typedefs/CallCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/typedefs/CallCallback.js#L1)  
引入版本：3.0.0

---

## FitToRegionItemCoverage {#fittoregionitemcoverage}

### \<static> FitToRegionItemCoverage {#static-fittoregionitemcoverage}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 是 | 1 | 覆盖项目的有效宽度。 |
| height | number | 是 | 1 | 覆盖项目的有效高度。 |
| originX | number | 是 | 0.5 | 覆盖项目的有效横向来源。 |
| originY | number | 是 | 0.5 | 覆盖项目的有效垂直源。 |

**类型**: object

**Member of**: Phaser.Types.Actions
> 源码：[src/actions/typedefs/FitToRegionItemCoverage.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/typedefs/FitToRegionItemCoverage.js#L1)  
引入版本：4.0.0

---

## GridAlignConfig {#gridalignconfig}

### \<static> GridAlignConfig {#static-gridalignconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 是 | -1 | 项中的网格宽度( 不像素 ) - 1 表示所有项的水平设置, 不论数量大小。 如果将这个值和高度都设定为 - 1, 此值将覆盖它, 且忽略 `height` 值 。 |
| height | number | 是 | -1 | 项中的网格高度( 不像素 ) 。 - 1 表示所有项的垂直排列, 不管数量大小。 如果将这个值和 `width` 都设置为 - 1, 那么 `width` 将覆盖它, 这个值会被忽略 。 |
| cellWidth | number | 是 | 1 | 单元格的宽度,以像素表示,项目位于其中。 |
| cellHeight | number | 是 | 1 | 单元格的高度,以像素表示,项目位于其中。 |
| position | number | 是 | 0 | 坐标位置,Phaser.Display.Align的凸轮之一,如`TOP_LEFT`或`RIGHT_CENTER`. |
| x | number | 是 | 0 | 可选地将最终网格的左上方置于这个坐标处. |
| y | number | 是 | 0 | 可选地将最终网格的左上方置于这个坐标处. |

**类型**: object

**Member of**: Phaser.Types.Actions
> 源码：[src/actions/typedefs/GridAlignConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/typedefs/GridAlignConfig.js#L1)  
引入版本：3.0.0

---

---
