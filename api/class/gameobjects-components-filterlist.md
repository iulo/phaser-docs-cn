# FilterList {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-components-filterlist)

正在对 [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) 应用的过滤器列表 。

过滤器可以应用特效和遮罩,它们只能用WebGL来使用,使用`gameObject.enableFilters()`来应用到游戏对象上.

过滤器包括以下内容:

* 弹匣扭曲

* Blend

* Blocky

* Blur

* 博凯/ 倾斜移动

* 颜色矩阵

* Displacement

* Glow

* Key

* Mask

* 平行过滤器

* Pixelate

* Sampler

* Shadow

* Threshold

此列表是“ 内部” 或“ 外部 ” 。 内部过滤器适用于摄像机内的东西。 外部过滤器适用于摄像机本身, 适用于其渲染上下文。 完整的摄像机渲染步骤列表如下 :

1. 物体使摄像机的体积达到纹理。

2. 内部滤波器将纹理绘制为新的纹理,应用效果.

  这些通常尺寸相同,但可能扩大以容纳模糊.

3. 纹理被引向摄像机上下文大小的纹理

  将绘制, 计算摄像机本身的转换。

4. 外部过滤器将纹理绘制为新的纹理,

  继续发挥效果,必要时扩大效力。

5. 最终纹理将过滤的摄像机内容引向上下文.

例如, 考虑一个旋转45度的游戏对象。 应用横向模糊过滤器。 如果过滤器是内部的, 模糊度会以45度显示, 因为它在旋转对象之前被应用。 如果过滤器是外部的, 模糊度将显示横向, 因为是在旋转对象之后被应用的 。

您应该尽可能使用内部过滤器, 因为这些过滤器只适用于摄像机/游戏对象的区域。 外部过滤器是全屏的, 并且可能更昂贵 。

过滤器可以堆叠。列表的顺序是应用的顺序。

正如您所理解的那样,一些效果比其他效果更昂贵。比如,开花效果比简单的颜色矩阵效果要贵,所以请考虑明智地使用这些效果,并在生产初期就对目标平台进行性能测试。

此过滤列表是内部创建的, 不需要直接被即时处理 。

在Phaser 3中,滤镜被称为FX.

**构造函数**

`new FilterList(camera)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 拥有这张名单的摄像机 |

---


**作用域**: static

> 源码：[src/gameobjects/components/FilterList.js#L31](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L31)  
引入版本：4.0.0

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(filter, [index]) {#instance-addfilter-index}


**说明:**

向此列表添加过滤器。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| filter | [Phaser.Filters.Controller](/api/class/filters-controller) | 否 | 过滤器要添加 。 |
| index | number | 是 | 插入过滤器的索引。如果不给定,则过滤器将添加到列表的末尾。如果是负的,则从结尾插入。 |


**返回值:** [Phaser.Filters.Controller](/api/class/filters-controller) - 添加的过滤器 。


> 源码：[src/gameobjects/components/FilterList.js#L150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L150)  
引入版本：4.0.0


---

### addBarrel {#addBarrel}

#### \<instance> addBarrel([amount]) {#instance-addbarrelamount}


**说明:**

添加弹匣效果 。

枪管效果允许您对游戏对象应用“ pinch” 或“ expendd” 扭曲。 效果的大小可以实时修改 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| amount | number | 是 | 1 | 用于枪管效果的扭曲量。 1 值不是扭曲值。 通常保持在+-1 内 。 |


**返回值:** [Phaser.Filters.Barrel](/api/class/filters-barrel) - 新的Barrel过滤控制器.


> 源码：[src/gameobjects/components/FilterList.js#L214](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L214)  
引入版本：4.0.0


---

### addBlend {#addBlend}

#### \<instance> addBlend([texture], [blendMode], [amount], [color]) {#instance-addblendtexture-blendmode-amount-color}


**说明:**

添加混合效果。

混合效果允许您使用特定的混合模式对视图应用另一个纹理。这支持WebGL中无法以其他方式使用的混合模式。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| texture | string | 是 | "'__WHITE'" | 纹理适用于视图. |
| blendMode | [Phaser.BlendModes](/api/namespace/blendmodes) | 是 | "Phaser.BlendModes.NORMAL" | 用于视图的混合模式 。 |
| amount | number | 是 | 1 | 混合效果的大小适用于视图。 0 时, 原图像被保存。 1 时, 混合纹理被完全应用。 预期范围为 0 到 1, 但您可以在此范围之外进行不同效果 。 |
| color | Array.\<number> | 是 | "[1, 1, 1, 1]" | 混合纹理的颜色。 每个值对应 RGBA 中的彩色通道。 期望范围为 0 到 1, 但您可以在此范围之外进行不同效果 。 |


**返回值:** [Phaser.Filters.Blend](/api/class/filters-blend) - 新的混合过滤器控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L230](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L230)  
引入版本：4.0.0


---

### addBlocky {#addBlocky}

#### \<instance> addBlocky([config]) {#instance-addblockyconfig}


**说明:**

添加块状效果。

此过滤器控制器管理一个块状效果 。

块状效果通过取块状像素的中央像素,并用它来填充整个块,从而产生像素化的效果.

它降低了图像的分辨率,创造了像素或块状的外观,这经常用于像素艺术等结构化目的. 一种技术是使游戏在更高分辨率,以N的因子缩放,然后在大小 N 上应用块状效果. 这创造了大,可见的像素,适合进一步分层化,效果也可以用来遮蔽游戏中的某些元素,比如在过渡期间或者检查特定内容.

Blocky在游戏上最擅长无反异名,因此它可以从原始图像中读取未过滤的像素颜色,它保存了原始艺术的颜色,而不是像像像素素滤镜那样混合.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Filters.BlockyConfig](/api/typedef/types-filters#blockyconfig) | 是 | Blocky 效果的配置对象 。 |


**返回值:** [Phaser.Filters.Blocky](/api/class/filters-blocky) - 新的布洛克过滤控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L256](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L256)  
引入版本：4.0.0


---

### addBlur {#addBlur}

#### \<instance> addBlur([quality], [x], [y], [strength], [color], [steps]) {#instance-addblurquality-x-y-strength-color-steps}


**说明:**

添加模糊效果。

高斯模糊是高斯函数模糊图像的结果,是广泛使用的效果,一般是为了减少图像噪音和细节,这种模糊技术的视觉效果是光滑模糊的类似通过半透明屏幕观看图像,与偏焦镜头产生的波克效应或通常照明下物体的阴影明显不同.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| quality | number | 是 | 0 | 模糊效果的质量。 可以是低质量的 0, 中质量的 1, 也可以是高质量的 2。 |
| x | number | 是 | 2 | 模糊效果的横向抵消. |
| y | number | 是 | 2 | 模糊效果的垂直偏移. |
| strength | number | 是 | 1 | 模糊效应的强度. |
| color | number | 是 | "0xffffff" | 模糊的颜色,作为六进制值. |
| steps | number | 是 | 4 | 运行模糊效果的步骤数。 此值应该总是整数 。 |


**返回值:** [Phaser.Filters.Blur](/api/class/filters-blur) - 新的模糊过滤器控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L289)  
引入版本：4.0.0


---

### addBokeh {#addBokeh}

#### \<instance> addBokeh([radius], [amount], [contrast]) {#instance-addbokehradius-amount-contrast}


**说明:**

添加波克效应。

博凯(Bokeh)是指模仿摄影技术创造浅深场的视觉效果,这种效果用来强调游戏的主题或动作,通过模糊背景或前缘元素,导致更浸润和视觉吸引人的经历,通过模拟外焦区域,给游戏图形带来深度感和现实感的渲染技术实现.

另见斜向移动。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| radius | number | 是 | 0.5 | 博克效应的半径. |
| amount | number | 是 | 1 | 博基效应的金额. |
| contrast | number | 是 | 0.2 | 博克效应的颜色对比. |


**返回值:** [Phaser.Filters.Bokeh](/api/class/filters-bokeh) - 新的波基过滤控制器.


> 源码：[src/gameobjects/components/FilterList.js#L322](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L322)  
引入版本：4.0.0


---

### addColorMatrix {#addColorMatrix}

#### \<instance> addColorMatrix() {#instance-addcolormatrix}


**说明:**

添加颜色矩阵效果。

色彩矩阵效应是一种视觉技术,它涉及使用数学矩阵来操纵图像或场景的颜色,这一过程可以调整色调,饱和度,亮度,对比度,使开发者能够在游戏中创建各种风格外观或情绪设置. 常见的应用包括模拟不同的照明条件,应用色彩滤镜,或者实现特定的视觉风格.


**返回值:** [Phaser.Filters.ColorMatrix](/api/class/filters-colormatrix) - 新的 ColorMatrix 过滤控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L351](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L351)  
引入版本：4.0.0


---

### addCombineColorMatrix {#addCombineColorMatrix}

#### \<instance> addCombineColorMatrix([texture]) {#instance-addcombinecolormatrixtexture}


**说明:**

添加组合颜色矩阵效果。

此过滤器将两个纹理的通道结合在一起。 有很多可能性。 然而, 一个重要目的是操纵α通道。 使用 `setupAlphaTransfer` 配置常见选项, 或直接设置 `colorMatrixSelf` 和 `colorMatrixTransfer` 属性 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 | "'__WHITE'" | 用于传输纹理的纹理或纹理键. |


**返回值:** [Phaser.Filters.CombineColorMatrix](/api/class/filters-combinecolormatrix) - 新的CombineColorMatrix过滤控制器.


> 源码：[src/gameobjects/components/FilterList.js#L369](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L369)  
引入版本：4.0.0


---

### addDisplacement {#addDisplacement}

#### \<instance> addDisplacement([texture], [x], [y]) {#instance-adddisplacementtexture-x-y}


**说明:**

添加一个移位效应。

移位效应是一种视效技术,它根据移位图的值改变像素在图像或纹理中的位置。这种效应用于在平坦元素中产生深度、表面异常或扭曲的幻觉。它可用于人物、对象或背景,以加强现实主义、传递运动或实现各种结构外观。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| texture | string | 是 | "'__WHITE'" | 用于移位的纹理中唯一基于字符串的键,它必须存在于纹理管理器中. |
| x | number | 是 | 0.005 | 水平移位量,一个很小的浮点数,如0.005。 |
| y | number | 是 | 0.005 | 垂直移位的数量,一个非常小的浮点数,如0.005。 |


**返回值:** [Phaser.Filters.Displacement](/api/class/filters-displacement) - 新的“ 流离失所” 过滤控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L389](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L389)  
引入版本：4.0.0


---

### addGlow {#addGlow}

#### \<instance> addGlow([color], [outerStrength], [innerStrength], [scale], [knockout], [quality], [distance]) {#instance-addglowcolor-outerstrength-innerstrength-scale-knockout-quality-distance}


**说明:**

添加一个 Glow 效果 。

光线效应是一种视觉技术,它围绕游戏对象,人物,或UI元素,创建了柔软,光线光环,这种效应用于强调重要性,增强视觉吸引力,或传递能量,魔法,或其他世界存在的感知,效果也可以设定在边缘的内侧,光线的颜色和强度可以修改.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| color | number | 是 | "0xffffff" | 光线效应的颜色作为数字值. |
| outerStrength | number | 是 | 4 | 发光的强度从纹理边缘向外延伸. |
| innerStrength | number | 是 | 0 | 发光的强度从纹理边缘向内倾. |
| scale | number | 是 | 1 | 光线效应的尺度, 将固定距离乘以倍数 。 |
| knockout | boolean | 是 | false | 如果`true`只画出光线,而不是纹理本身. |
| quality | number | 是 | 10 | 发光效果的质量。 过滤器创建后无法更改 。 |
| distance | number | 是 | 10 | 光线效果的距离。 过滤器创建后无法更改 。 |


**返回值:** [Phaser.Filters.Glow](/api/class/filters-glow) - 新的 Glow 过滤器控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L417](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L417)  
引入版本：4.0.0


---

### addGradientMap {#addGradientMap}

#### \<instance> addGradientMap([config]) {#instance-addgradientmapconfig}


**说明:**

添加渐变映射效果。

渐变映射重映射图像使用 ColorRamp 。 图像在每个点转换成进度值, 并且该进度被评价为斜坡沿线的颜色 。

进度值通常为图像的亮度。 您可以使用 `colorFactor` 和 `color` 属性来自定义它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Filters.GradientMapConfig](/api/typedef/types-filters#gradientmapconfig) | 是 | 渐变映射效果的配置对象 。 |


**返回值:** [Phaser.Filters.GradientMap](/api/class/filters-gradientmap) - 新的 GradientMap 过滤控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L452](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L452)  
引入版本：4.0.0


---

### addImageLight {#addImageLight}

#### \<instance> addImageLight(config) {#instance-addimagelightconfig}


**说明:**

添加图像光效应。

图像灯(ImageLight)是用于图像基照明(IBL)的滤镜,用于使用环境图和普通地图模拟图像的照明.

环境图是描述场景照明的图像,此过滤器使用单一全景图作为环境图,图像的顶部是天空,底部是地面,X轴覆盖全旋转,这种图像向上和底部扭曲,因为X轴伸展宽,所以如果您正在创建自己的环境图,请小心.

立方体地图在撰写时不由Phaser支持.

效果基本上是无限范围内的环境反射。 锐利的环境图将产生尖锐的反射, 而模糊的环境图则会产生分散的反射。 使用全景图Blur过滤器来创建正确的模糊的环境图。 必要时使用普通工具过滤器来操纵普通的地图, 使用动态图来捕捉输出 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Filters.ImageLightConfig](/api/typedef/types-filters#imagelightconfig) | 否 | 图像光效果的配置对象 。 |


**返回值:** [Phaser.Filters.ImageLight](/api/class/filters-imagelight) - 新的图像光过滤控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L474](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L474)  
引入版本：4.0.0


---

### addKey {#addKey}

#### \<instance> addKey([config]) {#instance-addkeyconfig}


**说明:**

添加键效果。

键效应可以去除或隔离图像中的特定颜色,可用于去除图像中的背景颜色,或者隔离特定颜色,以便进一步处理.

默认情况下, Key 将会删除匹配键颜色的像素。 您可以设置 `isolate` 来保存匹配的像素 。

阈值和羽毛设置控制了键颜色匹配的几近程度. 匹配通过"颜色矢量之间的距离"来测量;即像素的RGB值与键颜色的RGB值的距离有多近.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Filters.KeyConfig](/api/typedef/types-filters#keyconfig) | 是 | 键效果的配置对象 。 |


**返回值:** [Phaser.Filters.Key](/api/class/filters-key) - 新的键过滤控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L509](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L509)  
引入版本：4.0.0


---

### addMask {#addMask}

#### \<instance> addMask([mask], [invert], [viewCamera], [viewTransform], [scaleFactor]) {#instance-addmaskmask-invert-viewcamera-viewtransform-scalefactor}


**说明:**

添加遮罩效果 。

遮罩使用纹理来隐藏输入的部分,它将遮罩的α在相应的texel中输入的颜色和α相乘.

遮罩可以反转, 开关他们隐藏的东西和他们展示的东西。

遮罩可以使用纹理或游戏对象。如果使用游戏对象,遮罩会使游戏对象变成动态图案,并使用该图案。当游戏对象改变时,遮罩会自动更新,除非`autoUpdate`旗设定为`false`。

当遮罩过滤器被用作内部过滤器时,遮罩将匹配被过滤的对象/视图。这对创建随对象而来的效果是有用的,例如意在匹配动画图案的效果。

当遮罩滤镜被用作外部滤镜时,遮罩会匹配摄像机的上下文,这对创建覆盖整个视图的效果很有用.

在创建遮罩时可以指定一个可选的 `viewCamera`。 如果没有使用, 遮罩对象将通过默认的摄像机查看。 将 `viewCamera` 设定为场景的主摄像机( `this.cameras.main`) , 通过主摄像机查看遮罩 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| mask | string \| [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 是 | "'__WHITE'" | 遮罩的来源。 这可以是用于遮罩的独特的基于字符串的纹理键, 它必须存在于纹理管理器中。 或者它可以是 Game Object, 在这种情况下, 遮罩会让 Game Objects 变成动态图解并使用 。 |
| invert | boolean | 是 | false | 是否要反转遮罩 。 |
| viewCamera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 |  | 使用 Game Object 渲染遮罩时使用的摄像机。 如果没有指定, 请使用该场景的 `main` 摄像机 。 |
| viewTransform | 'local' \| 'world' | 是 | "'world'" | 使用 Game Object 渲染掩码时使用的转换 。 “ 本地” 使用 Game October 的属性 。 “ 世界” 使用 GameObject 的 `parentContainer` 值来计算世界位置 。 |
| scaleFactor | number | 是 | 1 | 适用于底部遮罩纹理的尺度因子。 可用于平衡内存使用和所需的遮罩精度。 这只调整纹理的大小; 您还必须调整遮罩大小以匹配, 例如, scaleFactor为0. 5, 您的遮罩可能是带有0. 5 尺度的容器。 当组合尺度因子、 对象转换和摄像机转换时, 很容易使事情变得复杂, 所以在使用此选项时要尽量精确 。 |


**返回值:** [Phaser.Filters.Mask](/api/class/filters-mask) - 新的遮罩过滤控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L535](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L535)  
引入版本：4.0.0


---

### addNormalTools {#addNormalTools}

#### \<instance> addNormalTools(config) {#instance-addnormaltoolsconfig}


**说明:**

添加普通工具效应。

普通工具是用于操纵普通地图的正常功能的过滤器。它具有以下几种功能:

- 旋转或调整普通地图。

- 改变正常人面对镜头的强烈程度.

- 输出灰色的纹理,显示正常人面对摄像机的强度,或者其他的向量.

输出可用于各种目的,例如:

- 编辑用于特殊应用程序的普通地图。

- 通过操纵面力来改变普通地图的明显视觉深度.

- 创建其它效果的基点,例如用于梯度或其他效果的遮罩.

您甚至可以将输出作为常规照明的普通地图。 通常, 普通地图会和主纹理一起加载, 但您可以编辑此内容 。

```js
// Given a dynamic texture `dyn` where the filter output is drawn,
// and a texture `spiderTex` with lighting enabled,
// we can inject the WebGL texture straight into the scene lighting as a normal map.
const dynTex = dyn.getWebGLTexture();
const dynSource = new Phaser.Textures.TextureSource(spiderTex, dynTex);
spiderTex.dataSource[0] = dynSource; // This is where the normal map is located.
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Filters.NormalToolsConfig](/api/typedef/types-filters#normaltoolsconfig) | 否 | 普通工具效果的配置对象。 |


**返回值:** [Phaser.Filters.NormalTools](/api/class/filters-normaltools) - 新的普通工具过滤控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L587](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L587)  
引入版本：4.0.0


---

### addPanoramaBlur {#addPanoramaBlur}

#### \<instance> addPanoramaBlur(config) {#instance-addpanoramablurconfig}


**说明:**

添加全景Blur效应。

PanoramaBlur 是模糊全景图像的过滤器。 用于像图像光一样的过滤器, 将全景图像作为环境图。 模糊度将长方形地图当作球体, 并应用靠近柱子的重扭曲来获取正确结果。 您不应该将其用于一般目的模糊 。

效果可能非常缓慢,因为它使用一个网格的样本。 样本总数等于 samplesX * samplesY。 这可以非常高,非常快, 所以在增加这些值时要小心。 它们不需要太高, 就能取得好的结果 。

默认情况下,模糊度会完全扩散, 并逐点取样一个整个半球。 如果您缩小半径, 效果会更集中。 使用此方法来控制对象中不同程度的光度 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Filters.PanoramaBlurConfig](/api/typedef/types-filters#panoramablurconfig) | 否 | 用于全景Blur效果的配置对象。 |


**返回值:** [Phaser.Filters.PanoramaBlur](/api/class/filters-panoramablur) - 新的全景Blur过滤控制器.


> 源码：[src/gameobjects/components/FilterList.js#L627](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L627)  
引入版本：4.0.0


---

### addParallelFilters {#addParallelFilters}

#### \<instance> addParallelFilters() {#instance-addparallelfilters}


**说明:**

添加平行过滤效果。

这个过滤控制器将输入分为两个过滤列表,分别运行每个列表,然后将结果混合在一起.

并行过滤器效果对重用输入很有用。 通常情况下, 过滤器会修改输入并传递到下一个过滤器。 这种效果允许您在其它地方分割输入并重用。 它不会从并行处理中获得性能好处; 它是重用输入的便利 。

平行过滤器效果本身不是过滤器。 它是管理两个过滤器的控件, 也是将结果组合在一起的最后一个混合过滤器。 过滤器列表被命名为“ 顶” 和“ 底” 。 “ 顶” 输出被应用为“ 底” 输出的混合纹理 。

您不必填充两个列表。 如果只包含一个列表, 则它将被与结尾的原始输入混合。 如果您想要保留在过滤过程中丢失的图像数据, 这样做将很有用 。


**返回值:** [Phaser.Filters.ParallelFilters](/api/class/filters-parallelfilters) - 新建的并行过滤器过滤控制器 。


> 源码：[src/filters/ParallelFilters.js#L112](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ParallelFilters.js#L112)  
引入版本：4.0.0


---

### addPixelate {#addPixelate}

#### \<instance> addPixelate([amount]) {#instance-addpixelateamount}


**说明:**

添加像素效应。

象素效应是一种视觉技术,它故意降低图像的分辨率或细节,形成由大,可见像素组成的块状或镶嵌的外观,这种效果可用于结构化目的,作为对复古游戏的致敬,或者作为游戏中某些元素的遮蔽手段,比如在过渡期间或者审查特定内容.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| amount | number | 是 | 象素的大小。 更高的值会产生更显著的效果 。 |


**返回值:** [Phaser.Filters.Pixelate](/api/class/filters-pixelate) - 新的 Pixelate 过滤器控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L662](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L662)  
引入版本：4.0.0


---

### addQuantize {#addQuantize}

#### \<instance> addQuantize([config]) {#instance-addquantizeconfig}


**说明:**

添加一个量化效果。

量化可以减少图像中独特的颜色数量, 其依据是每个颜色通道的一定有限的步骤。 这有利于创建反演或分层化效果 。

基本的量化将每个信道分解为若干个 `steps`。 这些步骤通常都是常规的。 您可以通过改变信道的 `gamma` 值来将其偏移到上下。 您可以调整最小的步数, 从而调整所有后续步骤, 并使用 `offset` 。

量化在 RGBA 或 HSVA 空间中进行。步骤、 伽马 和 抵消总是以相同的顺序应用, 但取决于颜色模式, 它们要么应用到 `[ red, green, blue, alpha ]` 或 `[ hue, saturation, value, alpha ]` 。

输出可能可选地被抖动,以消除带状,并产生使用中还有更多颜色的幻觉.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Filters.QuantizeConfig](/api/typedef/types-filters#quantizeconfig) | 是 | 用于量化效果的配置对象 。 |


**返回值:** [Phaser.GameObjects.Components.FilterList](/api/class/gameobjects-components-filterlist) - 新的量化过滤控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L685](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L685)  
引入版本：4.0.0


---

### addSampler {#addSampler}

#### \<instance> addSampler(callback, [region]) {#instance-addsamplercallback-region}


**说明:**

添加样本效果。

此控制器管理一个采样器。 它不会实际渲染任何东西, 并且使图像没有改变。 它用来对摄像机视图的某个区域进行采样, 然后将结果传递给调回。 这对于从摄像机视图中提取数据是有用的 。

手术很贵,请少用

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 |  | 随采样者结果调用回调. |
| region | null \| [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | null | 要采样的区域。 如果 `null`, 整个摄像机视图都会被采样。 如果一个 `Phaser.Types.Math.Vector2Like`, 则会采样一个点。 如果一个 `Phaser.Geom.Rectangle`, 区域会被采样 。 |


**返回值:** [Phaser.Filters.Sampler](/api/class/filters-sampler) - 新的样本过滤控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L717](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L717)  
引入版本：4.0.0


---

### addShadow {#addShadow}

#### \<instance> addShadow([x], [y], [decay], [power], [color], [samples], [intensity]) {#instance-addshadowx-y-decay-power-color-samples-intensity}


**说明:**

添加阴影效果。

影子效应是一种视觉技术,通过增加更暗,抵消游戏对象,人物或环境下的淤积或形状来创造深度和现实主义的幻觉. 这些模拟的影子有助于增强视觉吸引力和浸润,使2D游戏世界显得更具活力和三维.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 横向抵消阴影效应. |
| y | number | 是 | 0 | 阴影效应的垂直抵消. |
| decay | number | 是 | 0.1 | 阴之衰减之量. |
| power | number | 是 | 1 | 阴之效之力. |
| color | number | 是 | "0x000000" | 阴之色,为六合之值. |
| samples | number | 是 | 6 | 阴影效应将运行的样本数量 。 |
| intensity | number | 是 | 1 | 阴之效之烈. |


**返回值:** [Phaser.Filters.Shadow](/api/class/filters-shadow) - 新的阴影过滤控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L744](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L744)  
引入版本：4.0.0


---

### addThreshold {#addThreshold}

#### \<instance> addThreshold([edge1], [edge2], [invert]) {#instance-addthresholdedge1-edge2-invert}


**说明:**

添加阈值效应。

输入值与阈值或范围进行比较。阈值以下的值被设定为0,阈值以上值被设定为1。 范围内的值被线性地插值在0到1之间。

这对于从梯度产生尖端效应,或者对产生二进制效应,都是有用的.

阈值为存储范围,有两边,每个边对每个通道都有值,介于0到1之间,如果两个边缘相同,则阈值没有内插,并且会输出0到1. 每个通道也可以反转.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| edge1 | number \| Array.\<number> | 是 | 0.5 | 阈值的第一边缘。 这可能是 RGBA 频道的数组, 或者所有 4 频道的单个数字 。 |
| edge2 | number \| Array.\<number> | 是 | 0.5 | 阈值的第二边。 这可能是 RGBA 频道的数组, 或者所有 4 频道的单个数字 。 |
| invert | boolean \| Array.\<boolean> | 是 | false | 是否每个频道都倒置。 这可能是 RGBA 频道的数组, 也可能是所有 4 频道的 单布尔 。 |


**返回值:** [Phaser.Filters.Threshold](/api/class/filters-threshold) - 新的阈值过滤控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L778](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L778)  
引入版本：4.0.0


---

### addTiltShift {#addTiltShift}

#### \<instance> addTiltShift([radius], [amount], [contrast], [blurX], [blurY], [strength]) {#instance-addtiltshiftradius-amount-contrast-blurx-blury-strength}


**说明:**

添加倾斜的移动效果。

这种波凯效应也可以用来产生倾斜的Shift效应,这是一种通过模糊除图像小区域以外的一切事物来创建微型效应的技术,这种效果是通过模糊上下元素,同时保持中心区域焦点来实现的.

亦见波  .

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| radius | number | 是 | 博克效应的半径. |
| amount | number | 是 | 博基效应的金额. |
| contrast | number | 是 | 博克效应的颜色对比. |
| blurX | number | 是 | 水平模糊度的大小 。 |
| blurY | number | 是 | 垂直模糊的量。 |
| strength | number | 是 | 模糊的强度。 |


**返回值:** [Phaser.Filters.Bokeh](/api/class/filters-bokeh) - 新的波基过滤控制器.


> 源码：[src/gameobjects/components/FilterList.js#L813](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L813)  
引入版本：4.0.0


---

### addVignette {#addVignette}

#### \<instance> addVignette([x], [y], [radius], [strength], [color], [blendMode]) {#instance-addvignettex-y-radius-strength-color-blendmode}


**说明:**

添加维格内特效应。

阴极效应是一种视觉技术,屏幕边缘,或游戏对象,逐渐变暗或模糊,产生类似帧的外观,这种效果用来吸引玩家的焦点向中心动作或主题,增强浸润,为游戏视觉提供影视或艺术品质.

这种滤波器支持彩色边框,以及有限的组合模式,以增强其结构力.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0.5 | 阴极效应的横向偏移。 此值将正常化为 0 到 1 。 |
| y | number | 是 | 0.5 | 阴极效应的垂直偏移。 此值将正常化为 0 到 1 。 |
| radius | number | 是 | 0.5 | 阴极效应的半径。 此值已正常化到 0 到 1 之间 。 |
| strength | number | 是 | 0.5 | 阴阳效应的强度. |
| color | number \| string | [Phaser.Types.Display.InputColorObject](/api/typedef/types-display#inputcolorobject) | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0x000000" | 阴极效应的颜色,作为六进制码或颜色对象. |
| blendMode | number | 是 | "Phaser.BlendModes.NORMAL" | 与 vignette 混合模式。 仅支持 NORMAL、 ADD、 MULTIPLY 和 SCREEN 。 |


**返回值:** [Phaser.Filters.Vignette](/api/class/filters-vignette) - 新的 Vignette 过滤控制器 。


> 源码：[src/gameobjects/components/FilterList.js#L848](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L848)  
引入版本：4.0.0


---

### addWipe {#addWipe}

#### \<instance> addWipe([wipeWidth], [direction], [axis], [reveal], [wipeTexture]) {#instance-addwipewipewidth-direction-axis-reveal-wipetexture}


**说明:**

添加擦拭效果。

擦拭或揭示效果是一种视觉技术,它逐渐在游戏中发现或隐藏元素,如图像,文本或场景过渡. 这种效果常用于创造进化感,揭示隐藏的内容,或者提供游戏状态间平滑和视觉吸引人的过渡.

您可以同时设置擦拭效果的方向和轴。 下列组合是可能的:

* 左到右:方向 0,轴 0

* 右到左:方向 1,轴 0

* 从上到下:方向 0,轴 1

* 从下到上:方向 1,轴 1

由您自己设定 `progress` 值, 例如通过 Tween, 以转换效果 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| wipeWidth | number | 是 | 0.1 | 擦拭效果的宽度。 此值在 0 到 1 之间正常化 。 |
| direction | number | 是 | 0 | 擦拭效果的方向。 要么 0( 左到右, 要么上到下) 要么 1( 右到左, 要么下到上)。 设置与轴属性结合 。 |
| axis | number | 是 | 0 | 擦拭效果的轴。 要么0( X) 要么1( Y) 。 设定与方向属性结合 。 |
| reveal | number | 是 | 0 | 这是显示(1)还是淡化( 0) 效果? 启示显示在被擦除的区域输入; 淡化显示在未擦除的区域输入 。 |
| wipeTexture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 | "'__DEFAULT'" | 输入纹理未显示时使用的纹理或纹理键。默认纹理为空白。 使用另一个纹理进行擦拭过渡 。 |


**返回值:** [Phaser.Filters.Wipe](/api/class/filters-wipe) - - 新的擦拭过滤器实例。


> 源码：[src/gameobjects/components/FilterList.js#L877](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L877)  
引入版本：4.0.0


---

### clear {#clear}

#### \<instance> clear() {#instance-clear}


**说明:**

销毁并删除此列表中的所有过滤器 。


**返回值:** [Phaser.GameObjects.Components.FilterList](/api/class/gameobjects-components-filterlist) - 此过滤列表实例 。


> 源码：[src/gameobjects/components/FilterList.js#L127](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L127)  
引入版本：4.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁此过滤列表。


> 源码：[src/gameobjects/components/FilterList.js#L910](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L910)  
引入版本：4.0.0


---

### getActive {#getActive}

#### \<instance> getActive() {#instance-getactive}


**说明:**

返回此列表中的所有活动过滤器 。


**返回值:** Array.\<[Phaser.Filters.Controller](/api/class/filters-controller)> - 此列表中的活动过滤器 。


> 源码：[src/gameobjects/components/FilterList.js#L202](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L202)  
引入版本：4.0.0


---

### remove {#remove}

#### \<instance> remove(filter, [forceDestroy]) {#instance-removefilter-forcedestroy}


**说明:**

从此列表中删除过滤器, 然后将其销毁 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| filter | [Phaser.Filters.Controller](/api/class/filters-controller) | 否 |  | 要删除的过滤器 。 |
| forceDestroy | boolean | 是 | false | 如果`true`,即使它有`ignoreDestroy`旗设定,过滤器也会被销毁. |


**返回值:** [Phaser.GameObjects.Components.FilterList](/api/class/gameobjects-components-filterlist) - 此过滤列表实例 。


> 源码：[src/gameobjects/components/FilterList.js#L175](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L175)  
引入版本：4.0.0


---

## 公开成员 {#public-members}

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#camera-phasercamerasscene2dcamera}


**说明:**

拥有这张名单的摄像机


> 源码：[src/gameobjects/components/FilterList.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L102)  
引入版本：4.0.0


---

### list {#list}

#### list: Array.\<[Phaser.Filters.Controller](/api/class/filters-controller)> {#list-arrayphaserfilterscontroller}


**说明:**

滤镜列表.

此列表可以直接被操纵。 如果您想要添加或删除过滤器, 请使用适当的方法确保正确处理。 列表中的过滤器周围移动是安全的 。


> 源码：[src/gameobjects/components/FilterList.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/FilterList.js#L111)  
引入版本：4.0.0


---

---
