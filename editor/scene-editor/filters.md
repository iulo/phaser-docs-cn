# 滤镜 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/filters)

Phaser 4引入了几种特殊的过滤效果,这些效果是内置的,准备使用,可以应用到任意的游戏对象上.

在 Phaser 编辑器中,您可以添加到游戏对象中的效果,调整属性,并在场景编辑器中看到结果.

这些是它所支持的效果:

## 向游戏对象添加过滤器 {#adding-a-filter-to-a-game-object}

检查官的视野中,每个游戏对象都有一个 ** Filters ** 的段落:

![Filters section](https://cdn.phaser.games/oss-docs/assets/b055a47aa42eeee5-scene-editor-filters-section-20250404.webp)

它包含 **Add** 按钮,允许您在游戏对象中添加新效果。单击 **Add** 按钮时,则出现 **Shader Effects** 对话框:

![Filters dialog](https://cdn.phaser.games/oss-docs/assets/0abd130681a10639-scene-editor-filters-dialog-20250404.webp)

您可以在此选择过滤器,然后单击**Add**按钮将其添加到游戏对象中.

添加过滤器的另一种方法是在场景中选择游戏对象,打开上下文菜单并填充**Filter**子菜单,它显示了添加特定过滤器的选项:

![Add filter object from the context menu.](https://cdn.phaser.games/oss-docs/assets/30c77908af37a7eb-scene-editor-filters-menu-add-20250404.webp)

您可以在游戏对象中添加多个过滤器。 它们和任何其他场景对象一样, 都列在大纲视图中 :

![Filters in the Outline view.](https://cdn.phaser.games/oss-docs/assets/41b1ee13a855cd1b-scene-editor-filters-outline-view-202504.webp)

您可以选择过滤对象并删除,复制/粘贴,[change its rendering order](/editor/scene-editor/working-with-parent-objects#changing-the-rendering-order-of-children),或者修改其属性.

滤镜对象与其他任何场景对象一样,通过使用[Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties),可以将滤镜指定给变量,或者一个字段,或者设置为[nested prefab](/editor/scene-editor/prefabs/prefab-nested).

假设您想要调整阴影过滤器的强度。 您可以通过设置可变范围到 ** CLASS ** 来将过滤器指定为字段 :

![Set class scope to filter.](https://cdn.phaser.games/oss-docs/assets/6d34cbda720e7697-scene-editor-filter-variable-scope-20250.webp)

然后[scene compiler](/editor/scene-editor/scene-compiler)为FX对象生成一个变量和字段:

```javascript
editorCreate() {
    ...
    // shadowFx
    const shadowFx = logo.filters.internal.addShadow(0, 0, 0.1, 1, 0, 6, 1);
    ...
    this.shadowFx = shadowFx;
}

private shadowFx!: Phaser.Filters.Shadow;
```

然后,在**create**方法中,你可以调整阴影FX的强度:

```javascript
create() {
    ...
    this.add.tween({
        targets: this.shadowFx,
        intensity: 1,
    });
}
```

不仅可以给变量指定过滤器,还可以用它来制作一个[nested prefab](/editor/scene-editor/prefabs/prefab-nested)。这样,就可以在不同场景中重新使用过滤器。

## 过滤属性 {#filter-properties}

每个过滤器类型都共享一组常见属性。 您可以在 ** Filter ** 区编辑这些属性。 属性涉及过滤器的粘贴及其所属的过滤器列表( `Internal` 或 `External` ):

![Filter properties](https://cdn.phaser.games/oss-docs/assets/4891572fa3bc99a7-scene-editor-filter-properties-20250404.webp)

## 轻 {#glow}

光线是简单的滤波器,它给图像边缘添加了光线.

[Learn more about the Phaser.Filters.Glow properties in the Phaser documentation](/api/class/filters-glow)

![Glow filter](https://cdn.phaser.games/oss-docs/assets/ca137bb0bbd26d4a-scene-editor-filter-glow-properties-2025.webp)

## 阴影 {#shadow}

阴影是您图像的简单易用阴影过滤器。 您可以在 [Phaser.Filters.Shadow Phaser documentation](/api/class/filters-shadow) 中更多地了解其属性 。

![Shadow filter](https://cdn.phaser.games/oss-docs/assets/017ec0fc7820e3af-scen-editor-filter-shadow-properties-202.webp)

## 像素 {#pixelate}

象素滤镜是一种视觉技术,它故意降低图像的分辨率或细节,形成由大,可见像素组成的块状或镶嵌外观. 这种滤镜可用于结构化
目的,作为纪念重现游戏,或作为掩盖游戏中某些元素的手段,例如过渡期间或审查特定内容.

[Learn more about the Phaser.Filters.Pixelate properties in the Phaser documentation](/api/class/filters-pixelate)

![Pixelate effect](https://cdn.phaser.games/oss-docs/assets/004a898618398c38-scene-editor-filters-pixelate-20250404.webp)

## 模糊 {#blur}

高斯模糊是高斯函数模糊图像的结果,是广泛使用的效果,
通常用于减少图像噪声和细节。这种模糊技术的视觉效果是:
光滑模糊,类似于通过透明屏幕观看图像,明显不同
由焦外镜或物体在通常的照明下产生的波克效应产生。

[Learn more about the Phaser.Filters.Blur properties in the Phaser documentation](/api/class/filters-blur)

![Blur effect](https://cdn.phaser.games/oss-docs/assets/7c2c2e7827a6818e-scene-editor-filters-blur-20250404.webp)

## 弹匣 {#barrel}

枪管效果允许您将“ pinch” 或“ 扩展” 扭曲应用到
a 游戏对象。效果的大小可以实时修改。

[Learn more about the Phaser.Filters.Barrel properties in the Phaser documentation](/api/class/filters-barrel)

![Barrel filter](https://cdn.phaser.games/oss-docs/assets/b25403a962766c73-scene-editor-filters-barrel.webp)

## 流离失所 {#displacement}

此过滤器将绘制一个围绕游戏对象纹理的移位, 有效遮盖移位以外的任何区域而不需要实际的遮盖。 如果纹理透明, 您可以控制移位的厚度、 移位的颜色和背景的颜色 。 您也可以控制移位时的羽毛, 允许有严酷或柔软的边缘 。

请注意,如果游戏对象有输入区域或物理正文,则在游戏对象中添加此效果不会改变输入区域或物理正体.

[Learn more about the Phaser.Filters.Displacement properties in the Phaser documentation](/api/class/filters-displacement)

![Displacement filter](https://cdn.phaser.games/oss-docs/assets/218414a26acb815d-scene-editor-filters-displacement-202504.webp)

## 博凯 {#bokeh}

博凯(Bokeh)是指模仿摄影技术创造浅深场的视觉效果,这种效果用来强调游戏主体或动作,模糊背景或前缘元素,从而产生更沉浸和视觉上吸引人的经验。它通过模拟外焦区域,给游戏图形带来深度感和现实感的渲染技术来实现.

另见斜向移动。

[Learn more about the Phaser.Filters.Bokeh properties in the Phaser documentation](/api/class/filters-bokeh)

![Bokeh filter](https://cdn.phaser.games/oss-docs/assets/3b6c13fe839a9994-scene-editor-filters-bokeh-20250404.webp)!

## 组合 {#blend}

此过滤控制器管理摄像机的混合效果。 混合效果允许您使用特定的混合模式对视图应用另一个纹理。 这支持WebGL中无法使用的混合模式 。

![Blend filter](https://cdn.phaser.games/oss-docs/assets/6cbad509ac543ad9-scene-editor-filters-blend-20250405.webp)

## 遮罩 {#mask}

遮罩过滤器是一种特殊的过滤器,允许您对游戏对象应用一个遮罩,这个过滤器用于创建多种效果,比如根据遮罩纹理揭示或隐藏物体的部分内容. Phaser允许您使用任何纹理作为遮罩,甚至游戏对象也可以作为遮罩.

在Phaser编辑器中,我们把遮罩分为两个不同的对象:**TextureMask**和**ObjectMask**.

### 纹理掩码 {#texturemask}

应用了带有纹理遮罩的背景图像 :

![Texture mask filter](https://cdn.phaser.games/oss-docs/assets/cd3685c3606a08ef-scene-editor-filters-texture-mask-202504.webp)

相同的过滤器, 但倒转 :

![Inverted texture mask filter](https://cdn.phaser.games/oss-docs/assets/c6ce9c87da6d9b03-scene-editor-filters-texture-mask-invert.webp)

### 对象任务 {#objectmask}

您可以使用任意游戏对象作为掩码。 例如, 粒子发射器可以用作背景图像的掩码 :

![Object mask filter](https://cdn.phaser.games/oss-docs/assets/cdf85cb67804089f-scene-editor-filters-object-mask-2025040.webp)

## 阈值 {#threshold}

输入值与阈值或范围进行比较。阈值以下的值被设定为0,阈值以上值被设定为1,在0到1之间线性插值,这对产生梯度的锐边等效应,或产生二进制效应,都是有益的.

阈值为存储范围,有两边,每个边对每个通道都有值,介于0到1之间,如果两个边缘相同,则阈值没有内插,并且会输出0到1. 每个通道也可以反转.

![Threshold filter](https://cdn.phaser.games/oss-docs/assets/51c8fde2712ff60a-scene-editor-filters-threshold-20250405.webp)

## 样本 {#sampler}

此过滤器管理一个采样器。 它不会实际渲染任何东西, 并且使图像没有改变。 它用来对一个区域进行摄像机视图的取样, 然后将结果传递给调回。 这对于从摄像机视图中提取数据是有用的。 此操作费用昂贵, 所以请尽量使用 。

![Sampler filter](https://cdn.phaser.games/oss-docs/assets/823898c15d638abd-scene-editor-filters-sampler-20250405.webp)

## 颜色Matrix 颜色 {#colormatrix}

ColorMatrix 指的是模仿摄影技术来创造浅浅的场面的视觉效果。这种效果用来强调游戏的主题或动作,通过模糊背景或前缘元素,导致更具有浸润性和视觉吸引力的经验。它通过模拟外焦区域,给游戏图形带来深度感和现实感的渲染技术来实现。

[Learn more about the Phaser.Filters.ColorMatrix properties in the Phaser documentation](/api/class/filters-colormatrix)

ColorMatrix FX有不同的预设,可用于产生不同的效果.

预设为:

![ColorMatrix filters](https://cdn.phaser.games/oss-docs/assets/27c16aea058da0dd-scene-editor-filter-colormatrix-list-202.webp)

所有预设都有共同的Alpha属性,这使得您可以设置过滤器的alpha. 其他属性是每个预设的特有属性.

![ColorMatrix properties](https://cdn.phaser.games/oss-docs/assets/0c6fa8707836b605-scene-editor-filters-colormatrix-graysca.webp)

## 布莱克 {#blocky}

Blocky 过滤器通过降低图像的分辨率来创建像素或块状的外观,它通过取一个像素块的中心像素并用它来填充整个块,产生巨大的可见像素,这种效果常用于结构学目的(如像素艺术),在过渡时模糊某些元素,或者审查特定内容. Blocky 不同于像素过滤器,而是保留了原来的颜色而不是混合.

[Learn more about the Phaser.Filters.Blocky properties in the Phaser documentation](/api/class/filters-blocky)

![Blocky filter](https://cdn.phaser.games/oss-docs/assets/9408568b233729a5-scene-editor-filters-blocky-20260313.webp)

## 维涅特 {#vignette}

Vignette过滤器在屏幕或游戏对象的边缘逐渐变暗或模糊,从而形成类似帧的外观时,会产生视觉效果,这种效果用来吸引玩家的焦点面向中心动作或主体,增强浸润,并为游戏视觉提供影视或艺术品质. 过滤器支持彩色边框和有限的组合模式(NORMAL,ADD,MULTIPLY,和SCREEN),以提高其结构力.

[Learn more about the Phaser.Filters.Vignette properties in the Phaser documentation](/api/class/filters-vignette)

![Vignette filter](https://cdn.phaser.games/oss-docs/assets/d1b592f72503c6ad-scene-editor-filters-vignette-20260313.webp)

## 擦除( E) {#wipe}

擦拭过滤器会生成擦拭或揭示过渡效果, 从而逐渐发现或隐藏游戏中的元素, 如图像、 文本或场景过渡。 这个效果通常用于创建进取感, 揭示隐藏的内容, 或提供游戏状态间平滑和视觉吸引人的过渡。 您可以控制擦拭效果的方向( 左到右, 右到右, 上到下, 或下到上) 和轴( X 或 Y) , 以及进步值( 典型的通过 Tween 动画) 。

[Learn more about the Phaser.Filters.Wipe properties in the Phaser documentation](/api/class/filters-wipe)

![Wipe filter](https://cdn.phaser.games/oss-docs/assets/a5c747d245e3a1e5-scene-editor-filters-wipe-20260313.webp)

## 图像光 {#imagelight}

图像光是图像照明的滤镜, 它使用环境图和普通地图模拟图像的照明。 环境图是描述场景照明的全景图像, 图像的顶部代表天空, 底部代表地面, X轴覆盖全旋转。 效果在无限范围内产生环境的反射 — 尖锐的环境图产生尖锐的反射, 而模糊的环境图则产生分散的反射。 为了取得最佳效果, 请使用全景图过滤器来创建正确的模糊环境图, 必要时使用普通图过滤器来操纵正常的地图 。

[Learn more about the Phaser.Filters.ImageLight properties in the Phaser documentation](/api/class/filters-imagelight)

![ImageLight filter](https://cdn.phaser.games/oss-docs/assets/f274b96b88adf293-scene-editor-filters-image-light-2026031.webp)

## 键 {#key}

键过滤器从图像中去除或隔离特定颜色, 可用于从图像中去除背景颜色( 如绿色屏幕效果) 或隔离特定颜色, 再进一步处理。 默认情况下, Key 将去除匹配键颜色的像素, 但您可以通过设置 `isolate` 以真实的方式保存匹配的像素 。 阈值和羽毛设置通过测量颜色矢量之间的距离来控制键颜色匹配度( 像素的 RGB 值如何接近键颜色的 RGB 值) 。

[Learn more about the Phaser.Filters.Key properties in the Phaser documentation](/api/class/filters-key)

![Key filter](https://cdn.phaser.games/oss-docs/assets/7ebd2acc435fd072-scene-editor-filters-key-20260313.webp)

## 普通工具 {#normaltools}

普通图是用来操纵普通地图正常情况的滤镜。 它提供了几种功能: 旋转或调整法线贴图, 改变正常人面对摄像机的强度, 输出灰色的纹理, 显示正常人面对摄像机的程度( 或其他向量) 。 输出可用于各种目的, 如编辑普通地图用于特殊应用, 通过操纵面部力量改变法线贴图的视觉深度, 或创建遮罩等其他效果的基点。 您甚至可以将输出作为正常照明的法线贴图, 将它注入场景照明系统。

[Learn more about the Phaser.Filters.NormalTools properties in the Phaser documentation](/api/class/filters-normaltools)

![normal tools](https://cdn.phaser.games/oss-docs/assets/d9c086f0e1f4fb9b-scene-editor-filters-normaltools-1.webp)

![normal tools](https://cdn.phaser.games/oss-docs/assets/50bfdc8b328a930b-scene-editor-normaltools-2.webp)

## 概观Blur {#panoramablur}

PanoramaBlur是一个专门为模糊全景图像设计的滤波器, 用于像图像光一样的过滤器, 将全景图像作为环境图使用。 模糊度将长方形地图作为一个球体对待, 并应用靠近柱子的重扭曲来获取正确结果—— 它不应该用于一般目的模糊。 效果会非常缓慢, 因为它使用一个样本网格( samplesX × samplesY), 所以当增加这些值时要小心。 默认情况下, 模糊度会完全分散, 每点取样一个整个半球; 半径降低会使效果更集中, 您可以使用环境图控制物体中不同层次的光度。

[Learn more about the Phaser.Filters.PanoramaBlur properties in the Phaser documentation](/api/class/filters-panoramablur)

![Panorama Blur](https://cdn.phaser.games/oss-docs/assets/f71ee336b0963d41-scene-editor-filters-panoramablur-1.webp)

![Panorama Blur](https://cdn.phaser.games/oss-docs/assets/ddc17ae3b02a3d95-scene-editor-filters-panoramablur-2.webp)

## 组合颜色Matrix {#combinecolormatrix}

组合 ColorMatrix 是将两个纹理的通道组合在一起的过滤器, 有许多可能性进行操纵。 一个重要目的是操纵α通道。 过滤器使用颜色矩阵( `colorMatrixSelf`和 `colorMatrixTransfer`) 来控制来自基输入和传输纹理的值是如何组合的。 您可以使用 `setupAlphaTransfer`来配置常见选项或直接设置颜色矩阵属性。 `additions` 属性控制每个通道( R, G, B, A) 的加法权重, 决定最终输出中数值是保留 (1) 还是丢弃 ( 0) 。

[Learn more about the Phaser.Filters.CombineColorMatrix properties in the Phaser documentation](/api/class/filters-combinecolormatrix)

![CombineColorMatrix filter](https://cdn.phaser.games/oss-docs/assets/0091f78b9be0f713-scene-editor-filters-combinecolormatrix-.webp)

![CombineColorMatrix filter](https://cdn.phaser.games/oss-docs/assets/d812801ad3fa778b-scene-editor-filters-combinecolormatrix-.webp)

## 并行函数 {#parallelfilters}

并行过滤器是一个控制器,它将输入分成两个独立的过滤器列表,独立运行每个列表,然后将结果混合在一起。这个效果对于重新使用输入是有用的,通常,过滤器会修改输入并将其传递到下一个过滤器,但并行过滤器允许您将输入器分割到其他地方,并重新使用它。它管理两个过滤器列表(命名为“上”和“下”)和一个组合结果的最终混合过滤器。“上”输出被应用为“下”输出的混合纹理。如果只包含一个,则它会与原始输入混合,这在过滤器过程中丢失的图像时是有用的。一个常见的用途是创建了可定制的布鲁姆效应,因为它显示了下一张图像:

[Learn more about the Phaser.Filters.ParallelFilters properties in the Phaser documentation](/api/class/filters-parallelfilters)

![ParallelFilters filter](https://cdn.phaser.games/oss-docs/assets/53aa1a4eaf2d6f54-scene-editor-filters-parallelfilters-202.webp)

在检查器中,您可以看到两个词,一个用于顶部过滤器列表,另一个用于底部过滤器列表。每个段落都有按钮,可以在列表中添加一个新的过滤器 。

在大纲视图中,所有子过滤器都显示在平行过滤母程序下面。 您可以选择它们并进行共同操作, 如编辑、 删除、 声明为嵌套预制体文件等...

![ParallelFilters outline](https://cdn.phaser.games/oss-docs/assets/8fc6936332a59eff-scene-editor-parallelfilters-outline-202.webp)

---
