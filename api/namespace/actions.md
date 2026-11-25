# Phaser.Actions {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/actions)

Scope: 
static
> 源码：[src/actions/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/index.js#L7)  


## 静态函数 {#static-functions}

### AddEffectBloom {#AddEffectBloom}

#### \<static> AddEffectBloom(items, [config]) {#static-addeffectbloomitems-config}


**说明:**

将 Bloom 效果添加到相机或游戏对象或其中的列表中。

Bloom是亮光在图像中扩散的现象,可以用来增加场景的现实主义,尽管太多是显而易见的,而微妙的效果是最好的.

此动作通过对目标应用多个过滤器来创建Bloom效果.

- `ParallelFilters`将过滤流分割,让我们可以组合

  以原始图像显示的其他过滤器的结果。

  其他滤波器则加入`top`流.

- `Threshold`去除较暗的颜色.

- `Blur`将剩下的亮色散开.

此动作返回包含这些过滤器引用的对象。 您可以直接控制其属性, 例如, 如果您想要激活 Bloom, 或者如果您想要设置属性, 此动作不会表面 。

Bloom 效果会像目标关闭时的其它过滤器一样被销毁。 要手动禁用或删除 Bloom 效果, 请访问返回对象中的 `parallelFilters` 控制器。 它会保存其他过滤器 。

- `parallelFilters.active = false`: 关闭 Bloom 。

- `parallelFilters.destroy()`: 摧毁 Bloom 。

Bloom 最好作为全屏效果。 如果您应用到带有α区域的 Game Object上, 它无法将光亮与背景正确混合。 这是因为光亮应该使用 ADD 混合, 但对象本身应该使用 NORMAL 混合, 两者都无法。 您仍然可以将光亮应用到 Game Objects上, 但是在坚实的纹理上效果最好 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) \| [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | Array.\<([Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject))> | 否 | Bloom 效应的收件人 |
| config | [Phaser.Types.Actions.AddEffectBloomConfig](/api/typedef/types-actions#addeffectbloomconfig) | 是 | Bloom效应的初始配置. |


**返回值:** Array.\<[Phaser.Types.Actions.AddEffectBloomReturn](/api/typedef/types-actions#addeffectbloomreturn)> - 包含创建的过滤器的对象列表 。


> 源码：[src/actions/AddEffectBloom.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/AddEffectBloom.js#L9)  
引入版本：4.0.0


---

### AddEffectShine {#AddEffectShine}

#### \<static> AddEffectShine(items, [config]) {#static-addeffectshineitems-config}


**说明:**

将闪光效果添加到相机或游戏对象或其中的列表中。

Shine模拟了表面的亮点闪烁。它是一个亮点的短暂光谱反射,典型的光谱来自相当平坦的表面,它只从某些角度反映亮点。在游戏中,你可能用它来突出一个重要物体,传达一种光泽感,或者将一个干扰波段移动到传输上。

这项行动通过创造若干资源而奏效。

- 一个渐变对象生成闪光的区域.

- 动态触控能占据着闪耀区域。

- 特温动画片 闪耀区域。

- 混合滤镜结合了闪光和图像.

- (可选)一个平行过滤器将图像的其余部分添加回.

您可以使用 `config` 参数以若干方式配置效果 。

使用 `radius`, `direction` 和 `scale` 来设置梯度方向。 缩放默认值为目标大小的2倍, 以保证亮度在重现前完全离开图像。 半径在图像的两侧也增加了一个额外的偏移, 因此梯度有空间进出图像 。

使用 `colorFactor` 来控制突出点的 RGBA 颜色。 您可以将此值超过 1 来创建非常亮的亮度 。 默认情况下, 它会有一个微小的红色的亮度来创建温暖的突出点 。

使用 `displacementMap` 和 `displacement` 在渐变中添加一个移位过滤器。 这给人留下了表面略微缩放的印象。 您可以在渐变中添加其它过滤器, 将它们制成动态图解, 用于最后的混合 。

使用 `reveal` 将效果放入显示模式。 在此模式下, 图像只在闪光下可见 。

使用`duration`,`yoyo`和`ease`来控制Tween动画.

这样创建的资源在目标被摧毁时会自动被销毁。 您可以自己更早地去除它们。 除非在其他系统中使用, 否则它们会被隔离, 并且安全地被摧毁 。 (Tween 需要其它资源存在时 。 )

当用这种方法瞄准多个对象时,每个对象都会创建自己的资源集,每个集合都是独立的,并且可以被破坏或操纵而不影响其他对象.

你可以用它作为基础或灵感来创造自己的闪光效果.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) \| [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | Array.\<([Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject))> | 否 | 闪光效应的收件人 |
| config | [Phaser.Types.Actions.AddEffectShineConfig](/api/typedef/types-actions#addeffectshineconfig) | 是 | 初设光辉效果. |


**返回值:** Array.\<[Phaser.Types.Actions.AddEffectShineReturn](/api/typedef/types-actions#addeffectshinereturn)> - 包含创建资源的对象列表 。


> 源码：[src/actions/AddEffectShine.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/AddEffectShine.js#L13)  
引入版本：4.0.0


---

### AddMaskShape {#AddMaskShape}

#### \<static> AddMaskShape(items, config) {#static-addmaskshapeitems-config}


**说明:**

使用形状将遮罩应用到游戏对象或相机上或其中的列表中。

这是在对象/相机中添加一个面具的快速方法。 它创建了一个形状, 并使用 FitTroRegion 来正确大小 。

默认情况下,面具是圆形,缩放以适应游戏画布的X和Y轴(因此它不再真正是一个圆形).

您可以将形状改为“ 平方 ” 、 “ 矩形 ” 或 “ 椭圆形 ” 。 通过 `config.aspectRatio` 控制矩形或椭圆形 。

您可以像 FitTrongion 那样更改覆盖范围。 您可以在内部、 外部或两个轴上进行缩放。 您可以设定目标区域; 如果您不这样做, 动作会选择适合您的区域 。

动作支持可选的模糊效果, 应用到形状上。 这对口罩上的柔性边缘有好处。 您可以使用 `config.padding` 来缩小形状区域向内, 从而为模糊区域向外扩散到预定边界留下空间 。

形状在创建时被从现场移除。 您不需要管理其生命周期; 应该是在面具过滤器被摧毁后收集的垃圾, 通常是当场景或目标被关闭时。 如果您想要访问形状, 它可以在面具过滤器上找到 。

如果您一次将它应用到多个对象上, 它们都有自己的形状和遮罩过滤器。 请注意, 如果您使用外部过滤器, 遮罩会看起来排成一行。 在这种情况下, 将所有目标放入层或容器并遮盖起来可能更有效。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | Array.\<([Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera))> | 否 | 用于安装面具的游戏对象或相机或清单。 |
| config | [Phaser.Types.Actions.AddMaskShapeConfig](/api/typedef/types-actions#addmaskshapeconfig) | 否 | 面具形状的配置. |


**返回值:** Array.\<[Phaser.Filters.Mask](/api/class/filters-mask)> - 新蒙面滤镜,按目标顺序排列.


> 源码：[src/actions/AddMaskShape.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/AddMaskShape.js#L11)  
引入版本：4.0.0


---

### AlignTo {#AlignTo}

#### \<static> AlignTo(items, position, [offsetX], [offsetY]) {#static-aligntoitems-position-offsetx-offsety}


**说明:**

取一系列游戏对象并相互对齐。

配位位置由`position`参数控制,该参数应该是Phaser.Display.Align常数之一,如`Phaser.Display.Align.TOP_LEFT`,`Phaser.Display.Align.TOP_CENTER`等.

首项不动,第二项与第一项对齐,第三项与第二项对齐,等等.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| position | number | 否 |  | 将项目对齐的位置。 这是一个对齐常数, 如 `Phaser.Display.Align.LEFT_CENTER` 。 |
| offsetX | number | 是 | 0 | 位置上可选水平偏移,以像素计. |
| offsetY | number | 是 | 0 | 位置上可选垂直偏移,以像素计. |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/AlignTo.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/AlignTo.js#L9)  
引入版本：3.22.0


---

### Angle {#Angle}

#### \<static> Angle(items, value, [step], [index], [direction]) {#static-angleitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共`angle`属性的对象,然后将给定的值添加到其每个`angle`属性中.

可选的 `step` 属性被递增应用,乘以数组中的每个项目.

使用此选项时, 组为: `Angle(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 以度计的金额, 将加到`angle`的地产中。 |
| step | number | 是 | 0 | 将这个加到`value`的金额中,乘以迭代计数器。例如,一个`step`的10将增加第一个项目0,第二个项目10,第三个项目20,等等。 |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/Angle.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/Angle.js#L9)  
引入版本：3.0.0


---

### Call {#Call}

#### \<static> Call(items, callback, context) {#static-callitems-callback-context}


**说明:**

取出一系列对象,然后将每个对象传递给给定的回调。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 此动作要更新的项目序列 。 |
| callback | [Phaser.Types.Actions.CallCallback](/api/typedef/types-actions#callcallback) | 否 | 引用的回调。 它将仅被传递一个参数: 数组中的项目 。 |
| context | * | 否 | 将引用回调的范围 。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/Call.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/Call.js#L7)  
引入版本：3.0.0


---

### FitToRegion {#FitToRegion}

#### \<static> FitToRegion(items, [scaleMode], [region], [itemCoverage]) {#static-fittoregionitems-scalemode-region-itemcoverage}


**说明:**

将游戏对象匹配到一个区域 。

这是一种快速的方式,可以将背景与一个场景相匹配,移动一个物体而不担心起源,或者覆盖一个已知大小的洞.

这将将每个对象转换成长方形区域。 旋转被忽略, 但翻译和比例被改变。 注意负比例将变为正; 使用翻转来解决这个问题。 对象必须支持转换 。

适切可以按比例进行,以触摸区域内外;但默认情况下,它会独立地对两轴进行相撞,以触摸所有方.

区域是一个轴向对齐的边框(AABB),默认它来自对象,通过场景比例属性,即`{ x: 0, y: 0, width: scene.scale.width, height: scene.scale.height }`.

如果游戏对象没有大小或来源,例如容器,那么如何调整大小使之适合是困难的。 `itemCoverage` 参数允许您设置 `width`, `height`, `originX` 和/或 资源 `originY` 属性以补充可用数据。这些设置优先于原始项目属性,即使存在。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 适合区域的游戏对象或游戏对象。每个对象必须具有Phaser.GameObjects.Components.Transform组件 。 |
| scaleMode | number | 是 | 0 | 比例尺模式 。 0 设置每个轴以独立填充区域 。 - 1 大小轴均一致, 使项目触及区域 _ inside_ 。 1 大小轴均统一, 使项目触及区域的 _ exide_ 。 |
| region | [Phaser.Types.Math.RectangleLike](/api/typedef/types-math#rectanglelike) | 是 |  | 适合的区域。 如果定义不明确, 将从第一个项目的场景尺度推断 。 |
| itemCoverage | [Phaser.Types.Actions.FitToRegionItemCoverage](/api/typedef/types-actions#fittoregionitemcoverage) | 是 |  | 覆盖或定义项目覆盖的区域。 目的是为没有这些区域的物品提供尺寸, 如容器, 允许它们调整尺寸 。 |


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - - 装好的装备


> 源码：[src/actions/FitToRegion.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/FitToRegion.js#L10)  
引入版本：4.0.0


---

### GetFirst {#GetFirst}

#### \<static> GetFirst(items, compare, [index]) {#static-getfirstitems-compare-index}


**说明:**

取一系列对象,返回数组中具有与该矩阵中所有指定对象匹配的属性的第一个元素。 `compare` 对象。例如,如果比较对象是: `{ scaleX: 0.5, alpha: 1 }` 然后它会归还第一个有财产的物品 `scaleX` 设为0.5, `alpha` 设置为 1 。

使用此选项时, 组为: `GetFirst(group.getChildren(), compare, index)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要搜索的项目数组 。 |
| compare | object | 否 |  | 比较对象。 此对象中的每个属性将对照数组的项目检查 。 |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |


**返回值:** object, [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 阵列中第一个匹配比较对象的对象,或者如果找不到匹配对象,则使用`null`.


> 源码：[src/actions/GetFirst.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/GetFirst.js#L7)  
引入版本：3.0.0


---

### GetLast {#GetLast}

#### \<static> GetLast(items, compare, [index]) {#static-getlastitems-compare-index}


**说明:**

取一系列对象,返回数组中最后一个属性与 `compare` 对象中所有指定的属性相匹配的元素。例如,如果比较对象是: `{ scaleX: 0.5, alpha: 1 }`,那么它就会返回最后一个属性为: `scaleX` 设定为0.5, `alpha` 设定为 1 的项目。

使用此选项时, 组为: `GetLast(group.getChildren(), compare, index)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要搜索的项目数组 。 |
| compare | object | 否 |  | 比较对象。 此对象中的每个属性将对照数组的项目检查 。 |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |


**返回值:** object, [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 数组中最后一个匹配比较对象的对象,或者如果找不到匹配对象,则使用 `null` 。


> 源码：[src/actions/GetLast.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/GetLast.js#L7)  
引入版本：3.3.0


---

### GridAlign {#GridAlign}

#### \<static> GridAlign(items, options) {#static-gridalignitems-options}


**说明:**

取一系列游戏对象,或任何具有公共`x`和`y`属性的物体,并基于所提供的配置将其定位在网格布局中.

网格由一个 `width` (栏数)和/或 `height` (行数). 网格中的每个单元格都有大小由 `cellWidth` 财务报告和已审计财务报表 `cellHeight`,以像素形式。项目从左上方源头开始被放置到单元格中(`x`, `y`),并默认地填入左对右,上下。如果 `width` 设置为 -1,项目以单行水平排列。 `height` 设置为-1, 将项目置于单列垂直。 `width` 财务报告和已审计财务报表 `height` 设置时,网格逐行填充,如果网格在全部项目放置之前已经填满,则会提前停止。

`position`选项控制每个项目如何在单元格内对齐,使用`Phaser.Display.Align`常数之一,如`CENTER`或`TOP_LEFT`.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 此动作要更新的项目序列 。 |
| options | [Phaser.Types.Actions.GridAlignConfig](/api/typedef/types-actions#gridalignconfig) | 否 | GridAlign 配置对象 。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/GridAlign.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/GridAlign.js#L15)  
引入版本：3.0.0


---

### IncAlpha {#IncAlpha}

#### \<static> IncAlpha(items, value, [step], [index], [direction]) {#static-incalphaitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共`alpha`属性的对象,然后将给定的值添加到其每个`alpha`属性中.

可选的 `step` 属性被递增应用,乘以数组中的每个项目.

使用此选项时, 组为: `IncAlpha(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 将增加的`alpha`财产金额。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/IncAlpha.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/IncAlpha.js#L9)  
引入版本：3.0.0


---

### IncX {#IncX}

#### \<static> IncX(items, value, [step], [index], [direction]) {#static-incxitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共`x`属性的对象,然后将给定的值添加到其每个`x`属性中.

可选的 `step` 属性被递增应用,乘以数组中的每个项目.

使用此选项时, 组为: `IncX(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 将增加的`x`财产金额。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/IncX.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/IncX.js#L9)  
引入版本：3.0.0


---

### IncXY {#IncXY}

#### \<static> IncXY(items, x, [y], [stepX], [stepY], [index], [direction]) {#static-incxyitems-x-y-stepx-stepy-index-direction}


**说明:**

取一系列游戏对象,或任何具有公开的`x`和`y`属性的物体,然后将给定的值添加到每个对象上.

可选的`stepX`和`stepY`属性被递增应用,乘以阵列中的每个项.

使用此选项时, 组为: `IncXY(group.getChildren(), x, y, stepX, stepY)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| x | number | 否 |  | 将增加的`x`财产金额。 |
| y | number | 是 | "x" | `y` 属性的加法。如果 `undefined` 或 `null` ,则使用 `x` 值 。 |
| stepX | number | 是 | 0 | 这一点被加到`x`的金额中,乘以迭代计数器. |
| stepY | number | 是 | 0 | 这一点被加到`y`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/IncXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/IncXY.js#L9)  
引入版本：3.0.0


---

### IncY {#IncY}

#### \<static> IncY(items, value, [step], [index], [direction]) {#static-incyitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共`y`属性的对象,然后将给定的值添加到其每个`y`属性中.

可选的 `step` 属性被递增应用,乘以数组中的每个项目.

使用此选项时, 组为: `IncY(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 将增加的`y`财产金额。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/IncY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/IncY.js#L9)  
引入版本：3.0.0


---

### PlaceOnCircle {#PlaceOnCircle}

#### \<static> PlaceOnCircle(items, circle, [startAngle], [endAngle]) {#static-placeoncircleitems-circle-startangle-endangle}


**说明:**

取一系列游戏对象,并将其定位在一个圆周周边的均匀空格点上.

如果您希望通过一个 `Phaser.GameObjects.Circle`形状来达到此功能, 您应该通过它的 `geom` 属性 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 |  | 将游戏对象定位在哪个圆形上 。 |
| startAngle | number | 是 | 0 | 以弧度为起始位置的可选角度 。 |
| endAngle | number | 是 | 6.28 | 以弧度为单位的可选角度停止位置。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/PlaceOnCircle.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/PlaceOnCircle.js#L7)  
引入版本：3.0.0


---

### PlaceOnEllipse {#PlaceOnEllipse}

#### \<static> PlaceOnEllipse(items, ellipse, [startAngle], [endAngle]) {#static-placeonellipseitems-ellipse-startangle-endangle}


**说明:**

取出一系列游戏对象,并在椭圆周边的均匀空间点上定位它们.

每个游戏对象的`x`和`y`属性都更新到位,对象之间的间隔通过将角范围(从`startAngle`到`endAngle`)平分到项目数来决定.

如果您希望通过一个 `Phaser.GameObjects.Ellipse`形状来达到此功能, 您应该通过它的 `geom` 属性 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 |  | 将游戏对象定位在椭圆形上 。 |
| startAngle | number | 是 | 0 | 以弧度为起始位置的可选角度 。 |
| endAngle | number | 是 | 6.28 | 以弧度为单位的可选角度停止位置。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/PlaceOnEllipse.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/PlaceOnEllipse.js#L7)  
引入版本：3.0.0


---

### PlaceOnLine {#PlaceOnLine}

#### \<static> PlaceOnLine(items, line, [ease]) {#static-placeonlineitems-line-ease}


**说明:**

沿一行定位一系列游戏对象,设置每个对象的`x`和`y`坐标。默认情况下,游戏对象会被放置在线上的平间间隔。如果提供了`ease`参数,则点之间的间隔由该放松函数控制,从而可以将线上的分布组合或加速。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 游戏对象定位的线条 。 |
| ease | string \| function | 是 | 用于点分布的可选易用键。 可以是 EaseMap( 如 `'Sine.easeInOut'`) 的字符串键, 也可以是自定义的宽松函数。 如果省略, 点间距是均匀的 。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/PlaceOnLine.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/PlaceOnLine.js#L10)  
引入版本：3.0.0


---

### PlaceOnRectangle {#PlaceOnRectangle}

#### \<static> PlaceOnRectangle(items, rect, [shift]) {#static-placeonrectangleitems-rect-shift}


**说明:**

取出一系列游戏对象,并将其定位在矩形周界的均匀空格点上.

放置从矩形的左上方开始,然后顺时针方向进行。如果给出了 `shift` 参数,您可以在开始放置的地方抵消。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 |  | 将游戏对象定位在矩形上 。 |
| shift | number | 是 | 0 | 选择起始数的偏移。 正值将起始位置顺时针绕周线转动, 负值则逆时针转动 。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/PlaceOnRectangle.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/PlaceOnRectangle.js#L11)  
引入版本：3.0.0


---

### PlaceOnTriangle {#PlaceOnTriangle}

#### \<static> PlaceOnTriangle(items, triangle, [stepRate]) {#static-placeontriangleitems-triangle-steprate}


**说明:**

取一系列游戏对象,并将其定位在三角边缘的均匀空位点上。

如果您希望通过一个 `Phaser.GameObjects.Triangle`形状来达到此功能, 您应该通过它的 `geom` 属性 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 |  | 三角形将游戏对象定位在 。 |
| stepRate | number | 是 | 1 | 使用 Bresenham 的线程算法控制三角形边缘沿线取样点密度的可选步法。更高的值产生较少、更宽的间隔点;较低的值产生更多的点和密度。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/PlaceOnTriangle.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/PlaceOnTriangle.js#L9)  
引入版本：3.0.0


---

### PlayAnimation {#PlayAnimation}

#### \<static> PlayAnimation(items, key, [ignoreIfPlaying]) {#static-playanimationitems-key-ignoreifplaying}


**说明:**

在阵列中所有具有动画组件的游戏对象上播放动画.

您可以通过动画密钥, 或通过动画配置对象来对播放进行更多的控制 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| key | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | 否 |  | 动画要播放的字符串键,或动画实例,或`PlayAnimationConfig`对象. |
| ignoreIfPlaying | boolean | 是 | false | 如果这款动画已经播放了,那么就忽略这个电话. |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/PlayAnimation.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/PlayAnimation.js#L7)  
引入版本：3.0.0


---

### PropertyValueInc {#PropertyValueInc}

#### \<static> PropertyValueInc(items, key, value, [step], [index], [direction]) {#static-propertyvalueincitems-key-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有`key`定义的公共属性的对象,然后添加给定值.

可选的 `step` 属性被递增应用,乘以数组中的每个项目.

使用此选项时, 组为: `PropertyValueInc(group.getChildren(), key, value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| key | string | 否 |  | 需要更新的属性 。 |
| value | number | 否 |  | 所加财产之数. |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/PropertyValueInc.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/PropertyValueInc.js#L7)  
引入版本：3.3.0


---

### PropertyValueSet {#PropertyValueSet}

#### \<static> PropertyValueSet(items, key, value, [step], [index], [direction]) {#static-propertyvaluesetitems-key-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有`key`定义的公共属性的对象,然后设定为给定值.

可选的 `step` 属性被递增应用,乘以数组中的每个项目.

使用此选项时, 组为: `PropertyValueSet(group.getChildren(), key, value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| key | string | 否 |  | 需要更新的属性 。 |
| value | number | 否 |  | 设定财产的金额 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/PropertyValueSet.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/PropertyValueSet.js#L7)  
引入版本：3.3.0


---

### RandomCircle {#RandomCircle}

#### \<static> RandomCircle(items, circle) {#static-randomcircleitems-circle}


**说明:**

取出一系列游戏对象,并在圆圈内的随机位置定位它们.

如果您希望通过一个 `Phaser.GameObjects.Circle`形状来达到此功能, 您应该通过它的 `geom` 属性 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| circle | [Phaser.Geom.Circle](/api/class/geom-circle) | 否 | 将游戏对象定位在内部的圆 。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/RandomCircle.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/RandomCircle.js#L9)  
引入版本：3.0.0


---

### RandomEllipse {#RandomEllipse}

#### \<static> RandomEllipse(items, ellipse) {#static-randomellipseitems-ellipse}


**说明:**

取一系列游戏对象,并在椭圆形范围内随机位置定位.

如果您希望通过一个 `Phaser.GameObjects.Ellipse`形状来达到此功能, 您应该通过它的 `geom` 属性 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| ellipse | [Phaser.Geom.Ellipse](/api/class/geom-ellipse) | 否 | 将游戏对象定位在内部的椭圆 。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/RandomEllipse.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/RandomEllipse.js#L9)  
引入版本：3.0.0


---

### RandomLine {#RandomLine}

#### \<static> RandomLine(items, line) {#static-randomlineitems-line}


**说明:**

取一系列游戏对象,并将其定位在线上随机位置.

如果您希望通过一个 `Phaser.GameObjects.Line`形状来达到此功能, 您应该通过它的 `geom` 属性 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 否 | 随机定位游戏对象的线条 。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/RandomLine.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/RandomLine.js#L9)  
引入版本：3.0.0


---

### RandomRectangle {#RandomRectangle}

#### \<static> RandomRectangle(items, rect) {#static-randomrectangleitems-rect}


**说明:**

取一系列游戏对象,并将其定位在矩形范围内的随机位置.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 将游戏对象定位在其中的矩形 。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/RandomRectangle.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/RandomRectangle.js#L9)  
引入版本：3.0.0


---

### RandomTriangle {#RandomTriangle}

#### \<static> RandomTriangle(items, triangle) {#static-randomtriangleitems-triangle}


**说明:**

取一系列游戏对象,并将其定位在三角范围内的随机位置.

如果您希望通过一个 `Phaser.GameObjects.Triangle`形状来达到此功能, 您应该通过它的 `geom` 属性 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| triangle | [Phaser.Geom.Triangle](/api/class/geom-triangle) | 否 | 将游戏对象定位在其中的三角 。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/RandomTriangle.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/RandomTriangle.js#L9)  
引入版本：3.0.0


---

### Rotate {#Rotate}

#### \<static> Rotate(items, value, [step], [index], [direction]) {#static-rotateitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共`rotation`属性的对象,然后将给定的值添加到其每个`rotation`属性中.

可选的 `step` 属性被递增应用,乘以数组中的每个项目.

使用此选项时, 组为: `Rotate(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 加入`rotation`财产(弧度)的金额。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/Rotate.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/Rotate.js#L9)  
引入版本：3.0.0


---

### RotateAround {#RotateAround}

#### \<static> RotateAround(items, point, angle) {#static-rotatearounditems-point-angle}


**说明:**

按给定角度围绕给定点旋转每个项目。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| point | object | 否 | 任何具有公共`x`和`y`属性的天体. |
| angle | number | 否 | 旋转的角度,用弧度表示。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/RotateAround.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/RotateAround.js#L10)  
引入版本：3.0.0


---

### RotateAroundDistance {#RotateAroundDistance}

#### \<static> RotateAroundDistance(items, point, angle, distance) {#static-rotatearounddistanceitems-point-angle-distance}


**说明:**

将指定数组中的每个游戏对象按指定角度围绕一个点旋转,将每个项目定位在从该点到的指定距离。如果距离为零,则项目不移动。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| point | object | 否 | 任何具有公共`x`和`y`属性的天体. |
| angle | number | 否 | 旋转的角度,用弧度表示。 |
| distance | number | 否 | 以像素表示的旋转点距离. |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/RotateAroundDistance.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/RotateAroundDistance.js#L9)  
引入版本：3.0.0


---

### ScaleX {#ScaleX}

#### \<static> ScaleX(items, value, [step], [index], [direction]) {#static-scalexitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共`scaleX`属性的对象,然后将给定的值添加到其每个`scaleX`属性中.

可选的 `step` 属性被递增应用,乘以数组中的每个项目.

使用此选项时, 组为: `ScaleX(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 将增加的`scaleX`财产金额。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/ScaleX.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/ScaleX.js#L9)  
引入版本：3.0.0


---

### ScaleXY {#ScaleXY}

#### \<static> ScaleXY(items, scaleX, [scaleY], [stepX], [stepY], [index], [direction]) {#static-scalexyitems-scalex-scaley-stepx-stepy-index-direction}


**说明:**

取一系列游戏对象,或任何具有公开的`scaleX`和`scaleY`属性的物体,然后将给定的值添加到每个对象上.

可选的`stepX`和`stepY`属性被递增应用,乘以阵列中的每个项.

使用此选项时, 组为: `ScaleXY(group.getChildren(), scaleX, scaleY, stepX, stepY)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| scaleX | number | 否 |  | 将增加的`scaleX`财产金额。 |
| scaleY | number | 是 |  | `scaleY` 属性的加法。如果 `undefined` 或 `null` ,则使用 `scaleX` 值 。 |
| stepX | number | 是 | 0 | 这一点被加到`scaleX`的金额中,乘以迭代计数器. |
| stepY | number | 是 | 0 | 这一点被加到`scaleY`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/ScaleXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/ScaleXY.js#L9)  
引入版本：3.0.0


---

### ScaleY {#ScaleY}

#### \<static> ScaleY(items, value, [step], [index], [direction]) {#static-scaleyitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共`scaleY`属性的对象,然后将给定的值添加到其每个`scaleY`属性中.

可选的`step`参数被递增应用,乘以阵列中每个项目的迭代指数.

使用此选项时, 组为: `ScaleY(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 将增加的`scaleY`财产金额。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/ScaleY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/ScaleY.js#L9)  
引入版本：3.0.0


---

### SetAlpha {#SetAlpha}

#### \<static> SetAlpha(items, value, [step], [index], [direction]) {#static-setalphaitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性`alpha`的对象,然后设定到给定值.

可选的`step`属性被递增应用,乘以迭代指数,并加入`value`.

使用此选项时, 组为: `SetAlpha(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 设定每个项目的α值。 范围应该是 0( 完全透明) 到 1( 完全不透明) 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetAlpha.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetAlpha.js#L9)  
引入版本：3.0.0


---

### SetBlendMode {#SetBlendMode}

#### \<static> SetBlendMode(items, value, [index], [direction]) {#static-setblendmodeitems-value-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性`blendMode`的对象,然后设定到给定值.

使用此选项时, 组为: `SetBlendMode(group.getChildren(), value)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | [Phaser.BlendModes](/api/namespace/blendmodes) \| string | number | 否 |  | 要设置的混合模式 。 |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetBlendMode.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetBlendMode.js#L9)  
引入版本：3.0.0


---

### SetDepth {#SetDepth}

#### \<static> SetDepth(items, value, [step], [index], [direction]) {#static-setdepthitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性的天体`depth`,然后设定为给定值。`depth`属性控制游戏对象在景区内的渲染顺序:深度值较高的对象在数值较低的对象之上渲染.

可选的 `step` 属性被递增应用,乘以数组中的每个项目.

使用此选项时, 组为: `SetDepth(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 每个项目的深度值 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetDepth.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetDepth.js#L9)  
引入版本：3.0.0


---

### SetHitArea {#SetHitArea}

#### \<static> SetHitArea(items, [hitArea], [hitAreaCallback]) {#static-sethitareaitems-hitarea-hitareacallback}


**说明:**

在特定阵列中的所有项目上进行迭接,并给每个项目拨打`setInteractive`,对阵列中的每一游戏对象都应用相同的命中区域形状并回调.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| hitArea | [Phaser.Types.Input.InputConfiguration](/api/typedef/types-input#inputconfiguration) \| any | 是 | 输入配置对象, 或定义游戏对象的命中区域的几何形状。 如果不给定, 则会尝试根据纹理框架创建矩形 。 |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 是 | 用于确定指针是否在 Hit 区域形状之内的调用。 如果您提供了形状, 您也必须提供调用 。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/SetHitArea.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetHitArea.js#L7)  
引入版本：3.0.0


---

### SetOrigin {#SetOrigin}

#### \<static> SetOrigin(items, originX, [originY], [stepX], [stepY], [index], [direction]) {#static-setoriginitems-originx-originy-stepx-stepy-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性的`originX`和`originY`的物体,然后设定为给定值.

可选的`stepX`和`stepY`属性被递增应用,乘以阵列中的每个项.

使用此选项时, 组为: `SetOrigin(group.getChildren(), originX, originY, stepX, stepY)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| originX | number | 否 |  | 设定 `originX` 属性的金额 。 |
| originY | number | 是 |  | 设置 `originY` 属性的金额。 如果 `undefined` 或 `null` , 它使用 `originX` 值 。 |
| stepX | number | 是 | 0 | 这一点被加到`originX`的金额中,乘以迭代计数器. |
| stepY | number | 是 | 0 | 这一点被加到`originY`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetOrigin.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetOrigin.js#L9)  
引入版本：3.0.0


---

### SetRotation {#SetRotation}

#### \<static> SetRotation(items, value, [step], [index], [direction]) {#static-setrotationitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性`rotation`的对象,然后设定到给定值.

可选的 `step` 属性被递增应用,乘以数组中的每个项目.

使用此选项时, 组为: `SetRotation(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 将财产设定为(弧度)的金额。 |
| step | number | 是 | 0 | 每一个连续项目都会被加到`value`中,从而使每个对象都得到一个渐进的旋转(弧度),乘以迭代指数。 |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetRotation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetRotation.js#L9)  
引入版本：3.0.0


---

### SetScale {#SetScale}

#### \<static> SetScale(items, scaleX, [scaleY], [stepX], [stepY], [index], [direction]) {#static-setscaleitems-scalex-scaley-stepx-stepy-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性的`scaleX`和`scaleY`的物体,然后设定为给定值.

可选的`stepX`和`stepY`属性被递增应用,乘以阵列中的每个项.

使用此选项时, 组为: `SetScale(group.getChildren(), scaleX, scaleY, stepX, stepY)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| scaleX | number | 否 |  | 设定 `scaleX` 属性的金额 。 |
| scaleY | number | 是 |  | 设置 `scaleY` 属性的金额。 如果 `undefined` 或 `null` , 它使用 `scaleX` 值 。 |
| stepX | number | 是 | 0 | 这一点被加到`scaleX`的金额中,乘以迭代计数器. |
| stepY | number | 是 | 0 | 这一点被加到`scaleY`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetScale.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetScale.js#L9)  
引入版本：3.0.0


---

### SetScaleX {#SetScaleX}

#### \<static> SetScaleX(items, value, [step], [index], [direction]) {#static-setscalexitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性`scaleX`的对象,然后设定到给定值.

可选的`step`属性被递增应用,乘以迭代计数器.

使用此选项时, 组为: `SetScaleX(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 设置 `scaleX` 属性的值 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetScaleX.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetScaleX.js#L9)  
引入版本：3.0.0


---

### SetScaleY {#SetScaleY}

#### \<static> SetScaleY(items, value, [step], [index], [direction]) {#static-setscaleyitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性`scaleY`的对象,然后设定到给定值.

可选的`step`属性被递增应用,乘以迭代计数器.

使用此选项时, 组为: `SetScaleY(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 设定财产的金额 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetScaleY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetScaleY.js#L9)  
引入版本：3.0.0


---

### SetScrollFactor {#SetScrollFactor}

#### \<static> SetScrollFactor(items, scrollFactorX, [scrollFactorY], [stepX], [stepY], [index], [direction]) {#static-setscrollfactoritems-scrollfactorx-scrollfactory-stepx-stepy-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性的`scrollFactorX`和`scrollFactorY`的物体,然后设定为给定值.

可选的`stepX`和`stepY`属性被递增应用,乘以阵列中的每个项.

使用此选项时, 组为: `SetScrollFactor(group.getChildren(), scrollFactorX, scrollFactorY, stepX, stepY)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| scrollFactorX | number | 否 |  | 设定 `scrollFactorX` 属性的金额 。 |
| scrollFactorY | number | 是 |  | 设置 `scrollFactorY` 属性的金额。 如果 `undefined` 或 `null` , 它使用 `scrollFactorX` 值 。 |
| stepX | number | 是 | 0 | 这一点被加到`scrollFactorX`的金额中,乘以迭代计数器. |
| stepY | number | 是 | 0 | 这一点被加到`scrollFactorY`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetScrollFactor.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetScrollFactor.js#L9)  
引入版本：3.21.0


---

### SetScrollFactorX {#SetScrollFactorX}

#### \<static> SetScrollFactorX(items, value, [step], [index], [direction]) {#static-setscrollfactorxitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性`scrollFactorX`的对象,然后设定到给定值.

可选的 `step` 属性被递增应用,乘以数组中的每个项目.

使用此选项时, 组为: `SetScrollFactorX(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 设定财产的金额 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetScrollFactorX.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetScrollFactorX.js#L9)  
引入版本：3.21.0


---

### SetScrollFactorY {#SetScrollFactorY}

#### \<static> SetScrollFactorY(items, value, [step], [index], [direction]) {#static-setscrollfactoryitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性`scrollFactorY`的对象,然后设定到给定值.

可选的 `step` 属性被递增应用,乘以数组中的每个项目.

使用此选项时, 组为: `SetScrollFactorY(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 设定财产的金额 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetScrollFactorY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetScrollFactorY.js#L9)  
引入版本：3.21.0


---

### SetTint {#SetTint}

#### \<static> SetTint(items, topLeft, [topRight], [bottomLeft], [bottomRight]) {#static-settintitems-topleft-topright-bottomleft-bottomright}


**说明:**

取一系列游戏对象, 或任何具有公用方法 setTint () 的对象, 然后将每个对象的锡值更新到给定值。 您可以指定每个角的锡色, 或者只提供 `topLeft`参数的一个颜色值, 在这种情况下, 整个项目会用该颜色来涂色 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| topLeft | number | 否 | 每个项目的左上角将应用的锡。如果省略其他参数,则该锡将应用到整个项目。 |
| topRight | number | 是 | 用于项目右上角的锡。 |
| bottomLeft | number | 是 | 用于项目左下角的锡。 |
| bottomRight | number | 是 | 用于项目右下角的锡。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/SetTint.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetTint.js#L7)  
引入版本：3.0.0


---

### SetVisible {#SetVisible}

#### \<static> SetVisible(items, value, [index], [direction]) {#static-setvisibleitems-value-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性`visible`的对象,然后设定到给定值.

使用此选项时, 组为: `SetVisible(group.getChildren(), value)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | boolean | 否 |  | 设置每个项目的可见状态。 设定为 `true` 使项目可见, 或者 `false` 隐藏它们 。 |
| index | number | 是 | 0 | 从项目数组内开始移动的可选偏移 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetVisible.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetVisible.js#L9)  
引入版本：3.0.0


---

### SetX {#SetX}

#### \<static> SetX(items, value, [step], [index], [direction]) {#static-setxitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性`x`的对象,然后设定到给定值.

可选的 `step` 属性被递增应用,乘以数组中的每个项目.

使用此选项时, 组为: `SetX(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | x 坐标, 以像素形式设置在每个项上。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代指数,使每个项目得到一个逐渐增加的x抵消. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetX.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetX.js#L9)  
引入版本：3.0.0


---

### SetXY {#SetXY}

#### \<static> SetXY(items, x, [y], [stepX], [stepY], [index], [direction]) {#static-setxyitems-x-y-stepx-stepy-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性的`x`和`y`的物体,然后设定为给定值.

可选的`stepX`和`stepY`属性被递增应用,乘以阵列中的每个项.

使用此选项时, 组为: `SetXY(group.getChildren(), x, y, stepX, stepY)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| x | number | 否 |  | 设定 `x` 属性的金额 。 |
| y | number | 是 | "x" | 设置 `y` 属性的金额。 如果 `undefined` 或 `null` , 它使用 `x` 值 。 |
| stepX | number | 是 | 0 | 这一点被加到`x`的金额中,乘以迭代计数器. |
| stepY | number | 是 | 0 | 这一点被加到`y`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetXY.js#L9)  
引入版本：3.0.0


---

### SetY {#SetY}

#### \<static> SetY(items, value, [step], [index], [direction]) {#static-setyitems-value-step-index-direction}


**说明:**

取一系列游戏对象,或任何具有公共属性`y`的对象,然后设定到给定值.

可选的 `step` 属性被递增应用,乘以数组中的每个项目.

使用此选项时, 组为: `SetY(group.getChildren(), value, step)`

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 此动作要更新的项目序列 。 |
| value | number | 否 |  | 设定财产的金额 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的天体数组 。


> 源码：[src/actions/SetY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SetY.js#L9)  
引入版本：3.0.0


---

### ShiftPosition {#ShiftPosition}

#### \<static> ShiftPosition(items, x, y, [direction], [output]) {#static-shiftpositionitems-x-y-direction-output}


**说明:**

取一系列项目, 如 Game Objects, 或任何具有公共 `x` 和 `y` 属性的物体, 然后穿行它们。 由于此函数在位, 它移动当前元素的位置为数组中上一个条目的位置 。 重复到所有项目被移动为止 。

方向控制迭代的顺序。 值为 0( 默认值) 的值假设数组中的最后一项是“ 头” 项 。

方向值为 1 的假设是,数组中的第一个项目是“头”项。

“ 头” 项的位置设定为给此函数的 x/y 值。 数组中的其他所有项目依次更新为数组中上一个( 或下一个) 项的值。

最终的 x/y coords 返回,或设置在“ 输出” 矢量2 中。

把它当成是游戏Snake,在那里"头"被移动,然后每个身体的作品被移动到前一部作品的空间.

**Tags:**

 - generic
 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 游戏对象的阵列,或具有公共 x 和 y 位置的对象。此动作将更新此阵列的内容 。 |
| x | number | 否 |  | 将头项放置在 x 坐标处 。 |
| y | number | 否 |  | 将头项放置在 Y 坐标 。 |
| direction | number | 是 | 0 | 迭代方向. 0 = 上位至第一, 1 = 上位至第一. |
| output | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 选择 Vec2 类似对象, 将最后位置存储在其中 。 |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 输出向量 。


> 源码：[src/actions/ShiftPosition.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/ShiftPosition.js#L9)  
引入版本：3.0.0


---

### Shuffle {#Shuffle}

#### \<static> Shuffle(items) {#static-shuffleitems}


**说明:**

正在移动阵列。 正在修改阵列并返回。 Name

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象阵列。 此动作将更新此阵列的内容 。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/Shuffle.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/Shuffle.js#L9)  
引入版本：3.0.0


---

### SmootherStep {#SmootherStep}

#### \<static> SmootherStep(items, property, min, max, [inc]) {#static-smootherstepitems-property-min-max-inc}


**说明:**

使用更平滑的阶梯插值,取一系列游戏对象,并在指定属性间分配值。每个阶梯中的项目都根据其位置被分配到更平滑的阶段插值,从而产生比平滑阶梯更平滑的过渡。

平滑步法是一种类似西格莫德的插图和夹插功能.

函数取决于三个参数, 输入 x, "左边" 和 "右边" , 左边被假定为小于右边。 函数收到一个实际数字 x 作为参数, 如果x 少于或等于左边, 返回 0, 如果x 大于或等于右边, 并且使用 Hermite 多诺米 , 否则将平滑步函数的坡度为 0。 这有利于创建一个转换序列, 使用更平滑的步法将每个段插到一个段, 以替代使用更精密或昂贵的插入技术。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| property | string | 否 |  | 游戏对象的属性 Interpolate 。 |
| min | number | 否 |  | 最小内插值. |
| max | number | 否 |  | 最大内插值. |
| inc | boolean | 是 | false | 如果 `true`,则数值会递增。如果 `false`(默认),则数值会设定 。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/SmootherStep.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SmootherStep.js#L9)  
引入版本：3.0.0


---

### SmoothStep {#SmoothStep}

#### \<static> SmoothStep(items, property, min, max, [inc]) {#static-smoothstepitems-property-min-max-inc}


**说明:**

使用平滑步插图,在指定的属性中选择一系列游戏对象并分配值。每个阵列中的每个项目都根据其位置被分配一个平滑步插值,从而在项目之间形成平滑的易入/易出过渡。

平滑步法是一种类似西格莫德的插图和夹子功能.

功能取决于三个参数,输入x,"左边缘"和"右边缘",左边缘被假定比右边缘小.

该函数作为参数收到一个真数字 x,如果x小于或等于左边缘,则返回 0,如果x大于或等于右边缘,则返回 1,然后使用一个赫米特多诺米语顺畅地插到 0 到 1 之间。平滑步函数的坡度在两个边缘为0。

这样做便于利用平滑步骤来内插每个段来创建一系列的过渡,作为使用更精密或昂贵的内插技术的替代.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| property | string | 否 |  | 游戏对象的属性 Interpolate 。 |
| min | number | 否 |  | 平滑步的左边缘。 此值应该小于 `max` 。 |
| max | number | 否 |  | 平滑步的右边缘。 此值应该大于 `min` 。 |
| inc | boolean | 是 | false | 财产价值应递增(`true`)还是设定(`false`)? |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/SmoothStep.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/SmoothStep.js#L9)  
引入版本：3.0.0


---

### Spread {#Spread}

#### \<static> Spread(items, property, min, max, [inc]) {#static-spreaditems-property-min-max-inc}


**说明:**

取一系列游戏对象,然后修改其`property`,使数值等于或递增,以计算出来的散值。

分布值来自给定的`min`和`max`值以及阵列中项目总数.

例如,要让一系列的Sprites在α中从0变为1,您可以调用:

```javascript
Phaser.Actions.Spread(itemsArray, 'alpha', 0, 1);
```

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| property | string | 否 |  | 游戏对象的属性要传播 。 |
| min | number | 否 |  | 最低值。 。 |
| max | number | 否 |  | 最大值( 最大值 ) 。 |
| inc | boolean | 是 | false | 如果数值递增(`true`)或直接设定(`false`)? |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 传递到此动作的游戏对象数组 。


> 源码：[src/actions/Spread.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/Spread.js#L7)  
引入版本：3.0.0


---

### ToggleVisible {#ToggleVisible}

#### \<static> ToggleVisible(items) {#static-togglevisibleitems}


**说明:**

需要一系列游戏对象并切换每个对象的可见度。 先前的 `visible = false` 将会变成 `visible = true`, 反之亦然 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象阵列。 此动作将更新此阵列的内容 。 |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/ToggleVisible.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/ToggleVisible.js#L7)  
引入版本：3.0.0


---

### WrapInRectangle {#WrapInRectangle}

#### \<static> WrapInRectangle(items, rect, [padding]) {#static-wrapinrectangleitems-rect-padding}


**说明:**

穿透给定数组,并确保每个对象的x和y属性被包裹,以保持它们被包含在给定矩形区域中.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| items | array \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 游戏对象阵列。 此动作将更新此阵列的内容 。 |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 |  | 物体被包裹的矩形 。 |
| padding | number | 是 | 0 | 操作期间,每侧矩形都增加了一个金额. |


**返回值:** array, Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的数组被传递到此动作 。


> 源码：[src/actions/WrapInRectangle.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/actions/WrapInRectangle.js#L10)  
引入版本：3.0.0


---

---
