# 游戏对象组件 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/components)

## 阿尔法组件 {#alpha-component}

Alpha 组件负责设定游戏对象的α值,这是0到1. 之间的值,1 的值完全不透明,其中- 作为 0 的值是完全透明的,默认情况下,游戏对象的α值为1.

游戏对象当前本地的alpha值存储在其`alpha`属性中:

```js
const alpha = player.alpha;
```

要设置α,您可以使用可链式`setAlpha`方法:

```js
player.setAlpha(alpha);
```

或者,你可以设置 `alpha` 属性直接:

```js
player.alpha = alpha;
```

默认情况下, Game Objects 的alpha 值为 1 。 这意味着它们会完全可见。 您可以通过将 Game Object 的 `alpha` 属性设置为 1 或调用可链式 `clearAlpha` 方法来重置 Game Objee 的alpha:

```js
player.clearAlpha();
```

您可以使用此属性来创建效果, 如游戏对象“ 淡出” , 或者使游戏对象看起来是半透明的。 作为内部优化, 将让渲染器跳过 。

### 以每张 Vertex Alpha 格式 {#per-vertex-alpha}

对于一些游戏对象,可以设置一个不同的每个角的α值。这被称为顶点α。它允许您创建效果,比如游戏对象从一个角消失到另一个角,或者使游戏对象在某个角看起来半透明,但另一个角却不是。并非所有游戏对象支持顶点α,但是那些确实会有一个`setAlpha`方法,接受4个值,每个角一个.

角按以下顺序排列:左上,右上,左下和右下:

```js
player.setAlpha(topLeft, topRight, bottomLeft, bottomRight);
```

您也可以直接设置属性 :

```js
player.alphaTopLeft = topLeft;
player.alphaTopRight = topRight;
player.alphaBottomLeft = bottomLeft;
player.alphaBottomRight = bottomRight;
```

设定每个顶点α的能力是一个WebGL唯一的特征.

### 阿尔法和父母 {#alpha-and-parents}

当游戏对象拥有其α属性设置时,如果它拥有一个,它会将其α值乘以父容器的α值。例如,如果您拥有一个父游戏对象的α值为0.5,而一个子的α值为0.5.,那么孩子将随着其与父容器的α值的乘以0.25 α而得到:

```js
container.setAlpha(0.5);
child.setAlpha(0.5);
```

## 混合模式组件 {#blend-mode-component}

混合模式组件允许游戏对象设置在渲染过程中使用的混合模式. 混合模式允许将游戏对象中的像素与背景的像素进行不同类型的组合/混合.

目前游戏对象的混合模式存储在其`blendMode`的数值属性中:

```js
const blendMode = sprite.blendMode;
```

您可以使用可链式`setBlendMode`方法设置游戏对象的混合模式:

```js
sprite.setBlendMode(mode);
```

或者,你可以设置 `blendMode` 属性直接:

```js
sprite.blendMode = mode;
```

模式值可以是`BlendModes`常数之一,例如`Phaser.BlendModes.SCREEN`。也可以是弦,例如`SCREEN`,也可以是整数,例如`3`。如果给定一个字符串,则必须是所有大写,并精确匹配`BlendModes`常数列表中可用的那些。如果给定一个整数,那么它必须是下面列表中有效的混合模式常数ID。

默认值为0,即`NORMAL`混合模式.

### 混合模式常数 {#blend-mode-constants}

现有混合模式有:

身份证明 QQ常数 QQ 描述
--- | --- | ---
0 | `NORMAL` 普通混合模式。用于 Canvas 和 WebGL.
1 | `ADD` 添加混合模式。用于 Canvas 和 WebGL.
2 | `MULTIPLY` 混合模式。用于 Canvas 和 WebGL.
3 | `SCREEN` 屏幕混合模式。用于 Canvas 和 WebGL.
4 | `OVERLAY` 重叠混合模式,只用于Canvas
5 | `DARKEN` 暗黑混合模式,只用于Canvas
6 | `LIGHTEN` 轻轻混合模式,只用于Canvas.
7 Q`COLOR_DODGE` 颜色躲避混合模式,只用于Canvas.
8 Q`COLOR_BURN` 彩色燃烧模式,仅用于彩色
9 | `HARD_LIGHT` 硬光混合模式,只用于Canvas.
10 | `SOFT_LIGHT` 软光混合模式,只用于Canvas.
11 | `DIFFERENCE` 差异混合模式,只用于Canvas.
12 | `EXCLUSION` 排除混合模式,只用于Canvas
13 | `HUE` 胡伊混合模式,只用于Canvas.
14 | `SATURATION` 饱和混合模式,只用于Canvas.
15 Q`COLOR` 彩色混合模式,仅限Canvas.
16 | `LUMINOSITY` 轻度混合模式,只用于Canvas
17 | `ERASE` 擦除混合模式。用于 Canvas 和 WebGL.
18 | `SOURCE_IN` 混合模式下的源码,只用于 Canvas 。
19 | `SOURCE_OUT` 源代码为混合模式,仅用于 Canvas 。
20 Q`SOURCE_ATOP` 源代码 atop 混合模式,仅用于 Canvas.
21 | `DESTINATION_OVER` 目的地在混合模式上,只限Canvas
22 | `DESTINATION_IN` 混合模式下的目标,只用于Canvas
23 | `DESTINATION_OUT` 目的地 混合模式 只用于 Canvas 。
24 Q`DESTINATION_ATOP` 目标 atop 混合模式,只用于 Canvas 。
25 | `LIGHTER` | Xor blend mode. For Canvas only.
26 | `COPY` 复制混合模式,只用于Canvas.
27 | `XOR` | Xor blend mode. For Canvas only.

### 帆布对WebGL {#canvas-vs-webgl}

Canvas 渲染器支持所有的混合模式。 然而, WebGL 渲染器只支持以下混合模式 :

* `NORMAL`
* `ADD`
* `MULTIPLY`
* `SCREEN`
* `ERASE`

如果设置一种不由WebGL渲染器支持的混合模式,则将使用`NORMAL`混合模式.

在 WebGL 下,您可以创建自己的自定义混合模式 。

Canvas 渲染器将使用作为浏览器 Canvas API 的一部分的 Canvas `globalCompositeOperation` 特性。 这就是为什么它有这么多额外的混合模式可用 。

### WebGL 性能考量 {#webgl-performance-considerations}

Phaser WebGL 渲染器将使用内置的GL 搅拌器功能,这些功能极快。然而,它们比Canvas 搅拌器的范围更有限,所以默认情况下只能使用5个。因为使用GL混合功能意味着在设定之前需要批量冲洗。所以,如果一组游戏对象在一起,但其中一组游戏对象的混合模式与其余的有不同,那么渲染器会停止批次,全部绘制,设定混合模式,绘制一个游戏对象,然后为其余部分重新开始一个新的批次。

虽然现代的GPU设计是为了轻松地处理这样的任务,但您应该始终注意这种恒定批量冲洗可能产生的影响。 如果您需要经常改变混合模式, 请尝试组织您的游戏对象, 以便那些具有共享混合模式的游戏被连续添加到显示列表中, 而不中断, 因为这将允许它们尽可能少批量地被提交 。

## 界元件 {#bounds-component}

Boundes 组件负责提供您可以调用的方法, 以返回游戏对象中的各种相关边框值 。

游戏对象的"范围"可以概括为矩形,结合其规模和旋转,完全封装游戏对象的视觉界限.

并非所有游戏对象都有界限。例如,图形游戏对象没有内向界限,因为其工作方式。然而,大多数基于纹理的游戏对象,如Sprites,Text和TileSprites,都可以返回其界限。

如果游戏对象有一个父容器,那么其界限将根据它来自容器的影响来算出.

游戏对象的界限可以通过使用其`getBounds`方法来获得:

```js
const bounds = sprite.getBounds();
```

这个会还给你的 `Rectangle` 形状对象, 其中 `x` 财务报告和已审计财务报表 `y` 值是边框的左上角, `width` 财务报告和已审计财务报表 `height` 值是界限的宽度和高度。

您也可以在一个矩形对象中传递到 `getBounds` 方法,它会根据游戏对象的界限设置值:

```js
const rect = new Phaser.Geom.Rectangle();

sprite.getBounds(rect);
```

如果您在矩形中不通过, 那么将创建一个新的实例并返回给您。 因此, 如果您需要频繁使用这种方法, 请在矩形实例中通过, 以帮助减缓对象的创建 。

每次您使用这种方法时, 边界会被计算为新鲜的。 边界不会在内部缓存, 也不会自动更新。 如果您正在使用任何类型的更新循环或比例的边界, 请注意 。

### 相关界点 {#bounds-related-points}

除了`getBounds`方法之外,还有其他一些方法可以将游戏对象的界限中的特定点返回。如果不需要全部界限,那么获得你确实需要的点就更有效。

这些方法有:

* `getTopLeft`
* `getTopCenter`
* `getTopRight`
* `getLeftCenter`
* `getCenter`
* `getRightCenter`
* `getBottomLeft`
* `getBottomCenter`
* `getBottomRight`

它们都以同样的方式运行。 您可以可选择地通过一个 Vector2 实例来存储结果的点, 或者它们可以为你创建一个点。 它们也拥有 `includeParent` 布尔, 如果游戏对象有的话, 允许它们使用父容器 。

例如,这里是使用`getTopLeft`方法而不在父中计及:

```js
const point = sprite.getTopLeft();
```

这里有如何使用它, 但因素在父母:

```js
const point = sprite.getTopLeft(null, true);
```

这里说明如何使用它,但因子在母体中, 并存储结果为预生成的矢量2:

```js
const point = new Phaser.Math.Vector2();

sprite.getTopLeft(point, true);
```

所有列出的方法都可以以这种方式使用.

没有任何一种方法允许您设定界限。 它们都是“ 仅读” 方法 。

## 作物构成部分 {#crop-component}

Crop 组件允许基于纹理的游戏对象自行“ 裁剪 ” 。 裁剪是一个矩形, 它限制渲染时可见的纹理帧区域 。

裁剪游戏对象不会改变其大小、尺寸、物理体或命中区域,它只是视觉上改变在渲染通道期间所看到的。

游戏对象当前裁剪状态保存在其 `isCropped` 布尔 中 :

```js
const isCropped = player.isCropped;
```

要裁剪游戏对象,您可以使用可链式`setCrop`方法:

```js
player.setCrop(x, y, width, height);
```

作物的大小和高度。 作物总是一个矩形, 无法成为其他形状。

坐标与游戏对象相对,因此0×0是游戏对象纹理帧的左上角.

而不是直接以数值通过,或者您可以提供单个矩形几何对象实例作为第一个和唯一的参数:

```js
const rect = new Phaser.Geom.Rectangle(x, y, width, height);

player.setCrop(rect);
```

注意这是几何天体,不是矩形形状天体。

一组,为调整裁剪,您可以使用新的值再次调用 `setCrop` 方法,也可以在更新的矩形实例中通过。

如果您想要从游戏对象中删除裁剪, 重新设置它以再次显示整个纹理, 请使用 `setCrop` 方法, 没有参数 :

```js
player.setCrop();
```

### 作物限制 {#crop-limitations}

内部,作物在渲染前通过调整纹理紫外线坐标来工作,因此作物只能是一个适合现有纹理区域内的矩形.

您不能裁剪一个 Game Object 来显示比最初允许的更多纹理, 或使用除矩形以外的其它形状 。

因为它只是调整紫外线坐标 提供了一种超快的遮罩, 如果你需要长方形遮罩。

## 深度组件 {#depth-component}

深度组件允许游戏对象根据其"深度"值在游戏场景内排序,允许其在游戏对象的前部或后部移动,在一些游戏框架中,这被称为"z-index".

当一个场景摄像机准备制作每个帧时,它将根据它的深度值排序场景中所有可渲染的游戏对象。那些深度值最低的,首先渲染,而深度值最高的游戏对象则最后渲染,或者在前面的游戏中“在”上。

默认情况下,所有游戏对象都获得0的深度值,这意味着它们都根据其创建顺序排序,并被放置在显示列表中。深度组件允许您覆盖此功能。

游戏对象当前深度存储在其 `depth` 数字属性中:

```js
const depth = sprite.depth;
```

您可以使用可链式`setDepth`方法设置游戏对象的深度 :

```js
sprite.setDepth(value);
```

或者,你可以直接修改 `depth` 属性:

```js
sprite.depth = value;
```

值可以是任意数字,可以是整数,也可以是浮点。默认值是零。

值的大小没有上下界限,数字也不必连续指定,如果您给游戏对象一个深度为1000,另一个深度为500,那么您可以随意指定.

您也可以将深度属性绑定在一个游戏对象位置上。 例如, 将游戏对象的深度绑定在它的 `y` 位置上是很常见的, 这样它位于景区越高, 深度值就越高 :

```js
update ()
{
    sprite.setDepth(sprite.y);
}
```

如果一个或多个游戏对象共享相同的`depth`值,那么它们会根据显示列表中的索引进行排序。列表中的第一个是先渲染,等等。

### 深度更新 {#depth-updates}

当修改任何游戏对象的 `depth` 属性时, 深度组件告诉场景, 它需要在显示列表中运行一个深度排序 。 这是由调用 `DisplayList.queueDepthSort` 方法的组件完成的, 它会自动发生, 您不需要做其他任何工作 。

因为如果有很多游戏对象,对渲染列表进行排序可能是一项代价高昂的操作,Phaser会排队深度排序,并且只在渲染时执行它。如果自上一个帧以来没有游戏对象的深度发生变化,深度排序会被完全跳过 。

创建新的游戏对象,或删除已有的对象,也会导致深度排序被排队.

### 深度和容器 {#depth-and-containers}

容器游戏对象可以像其他游戏对象一样设置深度属性,并会影响其渲染的时点。然而,当一个孩子被放置在容器内时,其自身的深度值会被忽略。相反,容器的深度被所有儿童使用,不能被过度忽略。

如果要调整容器内儿童的顺序,可以采取具体方法,例如: `moveUp`, `moveDown`, `sendToBack` 详情见容器文件。

## 翻转组件 {#flip-component}

Flip 组件允许基于纹理的游戏对象在水平,垂直或两者之间自行“ flip” 。名称意味着,游戏对象显示的纹理在相应的轴上反转 。

游戏对象当前翻转存储在其`flipX`和`flipY`布尔属性中:

```js
const flipX = player.flipX;
const flipY = player.flipY;
```

要设置游戏对象的翻转状态,您可以使用可链式的`setFlip`,`setFlipX`和`setFlipY`方法:

```js
player.setFlip(x, y);
player.setFlipX(x);
player.setFlipY(y);
```

或者,你可以设置 `flipX`和 `flipY` 属性直接:

```js
player.flipX = true;
player.flipY = false;
```

### 切换和重置翻转 {#toggle-and-reset-a-flip}

有两种帮助方法可以切换当前flipX或flipY状态:

```js
player.toggleFlipX();
player.toggleFlipY();
```

您可以调用 `resetFlip` 方法来重置游戏对象的翻转状态 :

```js
player.resetFlip();
```

### 翻转对缩放 {#flip-vs-scale}

正如您在指南的缩放部分所读到的那样,您可以通过将缩放设置为负值来达到与翻转相同的视觉效果.

然而,翻转工作独立于尺度,被设定为布尔,而不是比例。这使得您可以根据事件翻转一个游戏对象,例如巡逻敌人到达墙壁,而不管其尺度值如何。

游戏对象总是根据纹理帧的中心翻转。您不能设置翻转的源头 。

## 遮罩组件 {#mask-component}

遮罩组件允许您设定在渲染过程中是否应该“ 遮罩” 。 遮罩控制器在渲染过程中可以显示游戏对象的像素。 遮罩以外的任何内容都不会被渲染。 在 Phaser中, 遮罩有两种类型: 比特玛普遮罩和几何遮罩 。

游戏对象当前遮罩存储在其 `mask` 属性中 :

```js
const mask = sprite.mask;
```

您可以使用可链式`setMask`方法设置游戏对象的遮罩:

```js
sprite.setMask(mask);
```

或者,你可以设置 `mask` 属性直接:

```js
sprite.mask = mask;
```

要移除遮罩,可以使用链式`clearMask`方法:

```js
sprite.clearMask();
```

或者,设置`mask`属性为`null`:

```js
sprite.mask = null;
```

在使用 `clearMask` 方法时,您也可以选择销毁目前附在 Gamne 对象上的掩码:

```js
sprite.clearMask(true);
```

### Phaser 中遮罩的工作原理 {#how-masks-work-in-phaser}

Phaser中有两个类型的遮罩,我们将在接下来的两个部分中覆盖。虽然它们提供了不同的特性,但它们都是以同样的方式创建和应用的。

遮罩是全球对象。 它们不与任何单一的游戏对象绑定, 也不属于任何单一的游戏对象。 您可以, 并且常常应该同时在您喜欢的游戏对象上使用相同的遮罩 。

遮罩只被创建和定位在世界空间中。 它们没有被应用到它们所遮盖的游戏对象上。 例如, 如果您创建一个位于世界坐标200x300的遮罩, 那么它将被定位到200x300, 不管它所遮盖的游戏物体在哪里 。

遮罩本身不是游戏对象,它们不是生活在显示列表中,不能像游戏对象那样被修改,即不能像Sprite那样设定它们的旋转或比例。这并不意味着不能修改创建后的遮罩,这仅仅意味着遮罩对象没有变形组件。

### 几何遮罩 {#geometry-mask}

几何遮罩(英语:Geometry Mask)是一种特殊的遮罩类型,它使用图形游戏对象的路径信息来定义其形状.

与Canvas Renderer一起,它使用Canvas API的"clipping path"特性. WebGL Renderer使用内置的WebGL特性,称为Stencil缓冲器.

它被称为几何遮罩,因为它使用几何数据来创建自己. Graphics Game Objects 有很多可用于生成这些路径的特性,包括: `lineTo`, `arc`, `ellipse` 。请查看 Graphics Game Object 文档,了解更多详情。

因为它使用路径数据来遮盖遮罩, 这意味着您无法用这种遮盖来进行“ per 像素” 遮盖。 它不适合用梯度纹理来创建遮盖。 例如, 您应该使用比特玛普遮盖 。

几何遮罩有能力设置其 `invertAlpha` 布尔属性。 这是 WebGL 唯一的特性, 允许您“ 反转” 应用遮罩的哪个区域 。

### 位图遮盖 {#bitmap-mask}

一个比特玛普遮罩使用纹理来控制在渲染过程中哪些像素会被目标游戏对象“抹掉”的纹理。为了实现这一点,它使用一个特殊的内部管道,名为比特玛普马斯管道。由于这个原因,它只与WebGL 渲染器合作。

由于它使用纹理来进行遮蔽输入,这意味着您可以在每像素级别上掩盖事物,而几何遮罩是不可能做到的。 Bitmap 遮罩的来源可以是基于纹理的游戏对象,比如Sprite,也可以是动态纹理实例.

比特玛普遮蔽器通过从遮罩纹理和遮罩游戏对象的α级中取出α级,从两个,每个像素中计算最终产生的α级,这与遮罩纹理所吸引的颜色无关,它只看每个像素的α值,例如,如果遮罩对特定像素的α值为0.95,而游戏对象的α值为同一像素的α值则为0.5,最终的α值在生成时会是0.45. 自然,所得出的α值越低,通过它可以看到的游戏对象就越少.

位图遮罩具有设置其`invertAlpha`布尔属性的能力。这使得您可以反转α比较,这样,遮罩纹理中的低α值就会导致遮罩游戏对象中的高α值,反之亦然。

注意您无法在单个游戏对象上设置 Bitmap 遮盖和 Blend 模式 。

### 业绩考量 {#performance-considerations}

当使用几何遮罩时,您应该记住路径的复杂性,即它里面有多少点。路径越复杂,Canvas和WebGL两个都需要越久才能制作出蒙面游戏对象。

在使用Bitmap 面罩时,您应该记住蒙面纹理的大小,越大,越需要通过蒙面遮蔽器传递像素,并且需要更多的GPU功率才能制作出蒙面游戏对象.

使用这两种遮罩, 渲染器需要进行很多额外的计算来处理遮罩。 这包括在 WebGL 中破解批次, 启用了质谱函数或遮罩遮蔽器, 然后渲染遮罩游戏对象。 因此, 您不应该对一个尚未需要的游戏对象使用遮罩 。

然而,遮罩被分批处理。这意味着,如果在“显示列表”中,一组被蒙蔽的游戏对象按顺序排列,所有这些对象都共享同样的遮罩,那么,你只支付一次建立遮罩的费用。

## 来源组件 {#origin-component}

默认大多数游戏对象在它们的 `x` 和 `y` 坐标上是 _centre_。这意味着,如果在 300x200 坐标上创建 Sprite, 那么 Sprite 的 _center_ 将被放置在 300x200 。

在一些游戏框架中,默认来源是左上方,而在另一些游戏中,则左下方。有时也被称为“锁定点”或“枢轴点”。然而,在Phaser中,它被称为源,默认为中心。您可以通过源组件中可用的方法更改此内容。

游戏对象的当前来源存储于其`originX`和`originY`的数值属性:

```js
const originX = player.originX;
const originY = player.originY;
```

要设置游戏对象的起源, 您可以使用可链式 `setOrigin` 方法 :

```js
player.setOrigin(x, y);
```

或者,你可以设置 `originX`和 `originY` 属性直接:

```js
player.originX = 0.5;
player.originY = 0.5;
```

数值被赋予在 0 到 1. 之间的一个常态值, 例如, 将源值设定为 0. 5 表示它会完全放在游戏对象的中心, 不管它的大小大小。 0 的值是游戏对象的左上方, 1 是右下方 。

来源既控制了游戏对象的放置,也控制了旋转的点。如果您想要在游戏对象的左上角旋转,您会将其来源设定为0x0。

或者,如果想要将一个游戏对象定位在屏幕的右下方,屏幕大小为800x600,那么可以将原产地设定为1x1,其位置设定为800x600.

游戏对象只能有一个来源。 例如, 其旋转和位置或比例表没有独有的来源。 如果您需要模仿此行为, 您可以创建容器游戏对象, 然后将您的其他游戏对象添加到其中 。

### 显示来源 {#the-display-origin}

Phaser还提供了所谓的“显示源”。这是使用像素值而不是普通值设定游戏对象的源头的一种方法。数值的范围在0到游戏对象的基宽或高度之间。

要设置游戏对象的显示源,您可以使用可链式`setDisplayOrigin`方法:

```js
player.setDisplayOrigin(x, y);
```

或者,你可以设置 `displayOriginX`和 `displayOriginY` 属性直接:

```js
player.displayOriginX = 256;
player.displayOriginY = 128;
```

### 自定义帧枢轴点 {#custom-frame-pivot}

某些软件,例如Texture Packer,允许您定义一个纹理帧的特定“中枢点”。然后在Texture Patcher创建的JSON数据中导出。Phaser将查找这些自定义的中枢点,然后设定游戏对象的源头,以与之匹配。这是通过`setOriginFromFrame`的方法完成的 :

```js
player.setOriginFromFrame();
```

如果您创建了 Sprite 并提供了在数据中具有自定义枢轴点的纹理帧,则自动调用。 如果您需要, 您也可以直接调用它 。

## 管道组件 {#pipeline-component}

管道组件控制使游戏对象使用管道渲染。 只有当 Phaser游戏使用 WebGL 渲染器时, 才会设定此管道。 Canvas 渲染器不使用自定义管道 。

一个管道是一个内部术语和类构造,Phaser用来处理不同类型游戏对象的渲染。例如,有Sprites使用的多管道,绳形游戏对象的绳形管道等等。您也可以创建自定义管道,在渲染时可以给你很多灵活性和力量。管道组件是您如何在游戏对象上设置管道的。

游戏对象当前管道存储在其 `pipeline` 属性中:

```js
const pipeline = sprite.pipeline;
```

这将默认为 `null` 。 直到游戏对象被即时调用时, 才会设定。 作为此过程的一部分, 所有游戏对象都会调用 `initPipeline` 方法, 这种方法负责设定游戏对象使用的默认管道。 这是内部方法, 不应该直接调用 。

您可以使用可链式`setPipeline`方法设置游戏对象的管道 :

```js
sprite.setPipeline(pipeline);
```

或者,你可以设置 `pipeline` 属性直接:

```js
sprite.pipeline = pipeline;
```

当使用 `setPipeline` 方法时, 您可以将一个字符串, 或者一个 `WebGLPipeline` 实例传递到该方法。 无论您通过哪一个, 它都会在管道管理器中查看管道, 如果发现它会设置在游戏对象上。 如果您通过一个与任何管道不匹配的字符串, 它将被忽略。 如果您通过管道管理器中找不到的管道, 它将被忽略 。

要移除管道,可以使用链式`resetPipeline`方法:

```js
sprite.resetPipeline();
```

或者,设置`pipeline`属性以匹配`defaultPipeline`属性:

```js
sprite.pipeline = sprite.defaultPipeline;
```

`defaultPipeline`属性设定为游戏对象首次创建时,应作为只读处理.

如果您想要获得游戏对象使用的管道的字符串名称,可以调用`getPipelineName`方法:

```js
const name = sprite.getPipelineName();
```

### 管道数据 {#pipeline-data}

管道组件还有一个`pipelineData`属性,它是一个包含管道在渲染过程中可能需要的数据的对象。您可以通过将它传递到`setPipeline`方法来设定一个作为管道数据的键值对象:

```js
sprite.setPipeline(pipeline, { foo: 1, bar: 2 });
```

或者,你可以叫`setPipelineData`方法:

```js
sprite.setPipelineData('key', value);
```

管道数据不是Phaser中任何默认管道使用,而是为您自定义管道提供。例如,如果您想要创建一条管道,以特殊方式给游戏对象配色,您可以在管道数据中存储游戏对象的颜色,准备在渲染前读取.

创建自定义管道是Phaser的一个先进特点,需要很好地了解WebGL和GLSL遮蔽器,在本指南的其他地方将涵盖。

## 滚动因子组件 {#scroll-factor-component}

滚动因子组件允许您控制游戏对象的滚动因子。“滚动因子”是指在游戏世界的摄像机滚动时,摄像机对游戏对象的影响有多大。

正如变形板部分所覆盖的那样,游戏对象在世界范围内有一个位置,这个位置与场景摄像机结合,用来计算游戏对象在屏幕上应该在哪里渲染,如果摄像机在世界上移动,游戏对象会显得随它移动,尽管其位置没有改变,只是因为摄像机现在正在面向世界的另一部分.

滚动因子允许您修改游戏对象位置之间的关系以及摄像机如何预测。设置滚动因子永远不会改变游戏对象的位置,或者任何相关的物理体,它只是改变由摄像机提供的位置。

游戏对象当前滚动因子存储在其`scrollFactorX`和`scrollFactorY`数字属性中:

```js
const scrollFactorX = player.scrollFactorX;
const scrollFactorY = player.scrollFactorY;
```

要设置游戏对象的滚动因子,您可以使用可链式`setScrollFactor`方法:

```js
player.setScrollFactor(x, y);
```

或者,你可以设置 `scrollFactorX`和 `scrollFactorY` 属性直接:

```js
player.scrollFactorX = 0.5;
player.scrollFactorY = 0.5;
```

每个轴的默认值是1. 这意味着作为摄像机卷轴,游戏对象会以完全相同的速度移动.

零值将阻止游戏对象受到摄像机的影响。 这将有效“ 锁定” 它在屏幕上的位置。 如果您想要创建一个仍然处于同一位置的UI 或其他界面元素, 不论摄像机在看哪里, 这会有所帮助 。

0.5 值将使游戏对象以摄像机的一半的速度移动。滚动因子可以是0及以上的任何值,尽管现实地你可能会将其夹在0至1之间的值上.

## 大小组件 {#size-component}

大小组件负责管理游戏对象的基数和显示大小.

大多数游戏对象都有内向或基数大小。对于基于纹理的游戏对象,如Sprites,大小会自动设定,以匹配Sprite所使用的纹理帧大小。当帧改变时,大小会自动更新。有些游戏对象在创建时会指定一个大小,如Tile Sprite。

您需要更改游戏对象的基数是很少见的。 但是, 有些游戏对象, 如容器, 没有基数。 在这种情况下, `setSize` 方法用于设定游戏对象的大小 。

游戏对象当前的基础大小存储在其`width`和`height`数字属性中:

```js
const width = player.width;
const height = player.height;
```

要设置您可以使用的可链式`setSize`方法的大小:

```js
player.setSize(width, height);
```

或者,你可以设置 `width`和 `height` 属性直接:

```js
player.width = 128;
player.height = 128;
```

大小被用在很多内部地方,从创建输入命中区,到物理体,到计算游戏对象的界限。如上所述,调整它并不常见,尽管如果需要,属性是公开的。只要注意它可能会产生意想不到的后果。

### 显示大小 {#display-size}

与游戏对象的大小不同,它的显示大小是专门为您根据需要修改而创建的.

显示大小对于一个基于纹理的游戏对象来说,其框架大小乘以其局部尺度。例如,如果一个Sprite有128x128的纹理帧集和2.0的尺度,那么其显示宽度和高度将是256x256。

游戏对象当前显示大小存储于其`displayWidth`和`displayHeight`数字属性:

```js
const width = player.displayWidth;
const height = player.displayHeight;
```

要设置您可以使用的可链式`setDisplaySize`方法的大小:

```js
player.setDisplaySize(width, height);
```

或者,你可以设置 `displayWidth`和 `displayHeight` 属性直接:

```js
player.displayWidth = 128;
player.displayHeight = 128;
```

数值以像素表示。

直接或通过方法设置这些值将调整游戏对象的本地_scale_。它为您提供了一种方法,可以将您希望游戏对象显示在像素中而不是作为比例来设置大小。

### 父大小 {#parent-size}

游戏对象容器默认没有大小。 您可以通过 `setSize` 方法设定其大小, 但只影响容器本身, 而不是任何孩子。 如果您想要设定容器大小和所有儿童, 您应该将其缩放 。

如果游戏对象有一个父容器,则父容器的显示大小会自动计入游戏对象的大小。例如,如果您拥有一个尺寸为128x128的Sprite,但其父容器的尺寸为0.5,那么Sprite将显示在64x64像素上。这是因为它被容器缩放。

如果您将游戏对象的显示宽度或高度设置为零, 它会被跳过以进行渲染。 这是因为游戏对象没有尺寸, 所以无法被看到。 因此, 为了优化渲染通道, Phaser将完全跳过它 。

## 变换组件 {#transform-component}

变形组件负责管理一个游戏对象的位置,规模和旋转.

大多数游戏对象都有此组件,但您可以通过检查`hasTransformComponent`属性是否存在,以及`true`是否在程序上测试其:

```js
if (player.hasTransformComponent)
{
    //  This Game Object has a Transform Component
}
```

### 职位 {#position}

一个游戏对象的当前本地位置存储在其`x`和`y`属性中.

```js
const x = player.x;
const y = player.y;
```

您可以使用可链式`setPosition`,`setX`和`setY`方法设置位置:

```js
player.setPosition(x, y);
player.setX(x);
player.setY(y);
```

或者,你可以设置 `x`和 `y` 属性直接:

```js
player.x = x;
player.y = y;
```

它们可以是负值,也可以是正值,还有整数或浮点.

游戏对象的位置总是相对其父容器,如果它有,则它的位置是相对于它的父容器的,如果它没有父容器,那么这个位置就是它在游戏世界中的位置.

例如:

```js
container.setPosition(300, 200);
child.setPosition(100, 100);
```

在上述代码中,容器定位为游戏世界的300×200,容器的孩子定位为100×100,这意味着该孩子将在游戏世界的400×300出现,因为其位置与容器相对.

```js
container.setPosition(300, 200);
child.setPosition(-100, -100);
```

在这个代码中,孩子会在游戏世界中以200×100出现,因为它相对于其父母来说有着负面的地位.

位置总是被设定并作为一个数字返回。这允许您在进一步计算时直接使用该位置,或者像您想使用其它数字一样操纵它:

```js
enemy.x = player.x;
enemy.y = player.y - 100;
```

参见源组件来学习Phaser如何知道游戏对象的哪个点可以用作它的x/y锚.

Phaser 另有两个与位置有关的属性: `z` 财务报告和已审计财务报表 `w`。您可以在调用时设置这些可选值。 `setPosition`,或者他们有自己的可链路方法 `setZ` 财务报告和已审计财务报表 `setW`。这些属性通常不由内部使用。 Phaser,但如果需要,则可以提供,以便进行更高级的位置,例如深度排序。

`copyPosition`方法允许您直接将游戏对象位置复制到另一个对象:

```js
enemy.copyPosition(player);
```

目标对象可以是任何具有公共`x`和`y`属性的物体,如另一个游戏对象,或矢量2.

您也可以设置游戏对象, 以使用 `setRandomPosition` 方法随机定位 :

```js
enemy.setRandomPosition();
```

默认情况下,如果不提供任何参数,游戏对象会在任何地方获得一个位置,而不与缩放管理器设定的大小相同。然而,您也可以以 x, y, 宽度和高度参数通过该方法, 来控制一个矩形, 将随机位置设置在其中 :

```js
enemy.setRandomPosition(100, 100, 600, 400);
```

几何类有多种相似的方法,用于将物体定位在几何形状内,然而,如果想要迅速将一个物体放置在屏幕上,这种方法是有用的。

### 缩放 {#scale}

目前游戏对象的本地尺度存储在其`scaleX`和`scaleY`属性中.

```js
const scaleX = player.scaleX;
const scaleY = player.scaleY;
```

您可以使用可链式`setScale`方法设置比例 :

```js
player.setScale(x, y);
```

或者,你可以设置 `scaleX`和 `scaleY` 属性直接:

```js
player.scaleX = x;
player.scaleY = y;
```

还有一种特殊的属性叫做`scale`,它允许您同时设置x和y两个比例,以相同值:

```js
player.scale = 2;
```

缩放值可以是负数也可以是正数,还有整数或者浮点数.

默认情况下, Game Objects 的缩放值为 1, 也就是说, 其大小将与其纹理帧相同。 通过调整缩放属性, 您可以使其看起来更大或更小。 您给出的数字将乘以其基数。 例如, 0. 5 的缩放值将游戏对象的显示大小减半, 以 2 的值将增加一倍 。

设置缩放不会改变游戏对象的实际基本大小。如果在调整游戏对象的缩放后读取其宽度或高度,返回的值将是未缩放的原始大小。 您可以在大小组件部分中读取更多关于此的文字 。

缩放总是设定并作为一个数字返回。这允许您在进一步计算时直接使用缩放,或者像其他数字一样操纵缩放。

缩放总是在游戏对象的中心周围进行,而无论游戏对象的来源如何,不能更改.

游戏对象的大小总是相对于其父容器,如果它有的话.

例如:

```js
container.setScale(2, 2);
```

在上述代码中,容器每个轴线上缩放2个,意思是,容器的所有儿童大小将增加一倍。

```js
container.setScale(2, 2);
child.setScale(2, 2);
```

在这个代码中,孩子会以容器大小的4x出现,因为其本身已经缩放过两次,同时也继承了父母的双倍缩放.

如果您将游戏对象的任何轴线缩放到零, 它会被跳过以进行渲染。 这是因为一个缩放为零的游戏对象没有尺寸, 所以无法看到。 因此, 为了优化渲染通道, Phaser将完全跳过这些游戏对象 。

如果您对游戏对象进行反向缩放, 就会发生有趣的效果。 游戏对象会显示翻转。 例如 :

```js
player.scaleX = -1;
```

这将让游戏对象变成水平翻转对象。 对于需要面对两个方向的字符来说, 这样做很方便, 但您只需要将绘制的纹理存储在一个方向, 使用负缩放来在运行时使反面发生。 请注意 Phaser还有一个“ 滑动组件” , 用于翻转游戏对象而不调整其缩放 。

当您对一个基于纹理的游戏对象进行比例化时, 需要理解渲染器需要在目前存在的由于游戏对象的大小增加而显示的像素上“ gues ” 。 例如, 如果您有 16x16 纹理, 并且将它缩放 4, 那么它会在屏幕上显示为 64x64 。 在原始纹理中不存在的所有额外像素都是在渲染过程中由 GPU 创建的。 如果您将纹理缩放, 类似的事情也会发生 。 GPU 必须决定哪个像素不显示, 并尝试创建一个最能代表纹理图像的平均值 。

许多艺术软件,比如Photoshop,在重新调整图像大小以创造更精细的结果时,都能够应用特殊的过滤器和效果。然而,WebGL和Canvas没有这个特性,它们倾向于速度而不是视觉忠诚。毕竟,它们与Photoshop不同,必须每秒或多做60次。如果你看到视觉质量下降的下降比预期的要差,那么就应该考虑使用一个在艺术包中预估的较小或更大的纹理。

### 旋转 {#rotation}

游戏对象当前本地旋转被存储在其 `rotation` 属性中:

```js
const rotation = player.rotation;
```

`rotation`值总是用弧度表示。如果您喜欢用度法工作,您可以使用 `angle` 属性来代替 :

```js
const angle = player.angle;
```

要设置旋转或角度,可以使用可链式`setRotation`和`setAngle`方法:

```js
player.setRotation(rotation);
player.setAngle(angle);
```

或者,你可以设置 `rotation`和 `angle` 属性直接:

```js
player.rotation = rotation;
player.angle = angle;
```

Phaser使用右手坐标系统,其中0为东向,3.14(或180度)为西向,左向,南向1.57,或90度,北向-1.57(或-90度). 如果将旋转视线视同为圆形,则下半身为正,上半身为负,这与Adobe Flash相同,Phaser的第一个版本从中吸取了它的灵感.

Phaser中的旋转总是围绕游戏对象的起源进行,也就是说,默认的游戏对象一般会围绕其中心旋转。您已经读过,可以调整来源。这改变了游戏对象的位置和旋转位置。您不能改变游戏对象的旋转点,只能改变其起源。

游戏对象的旋转总是相对其父容器的,如果它有.

例如:

```js
container.setRotation(0.75);
```

在上述代码中,容器由0.75弧度旋转,这意味着其所有子将按相同数量旋转.

```js
container.setRotation(0.75);
child.setRotation(0.75);
```

在这个代码中,孩子将总共被1.5弧度旋转,因为它继承了父母的旋转,然后会加入自己的旋转.

`rotation`属性只包含本地旋转值。 如果您想要获得游戏对象的旋转总和, 同时考虑到其所有祖先, 您可以使用 `getParentRotation` 方法 :

```js
const rotation = player.getParentRotation();
```

这将返回所有父容器的全旋转, 弧度。 如果您需要世界旋转, 请将游戏对象旋转加入到最终值中 :

```js
const rotation = player.getParentRotation() + player.rotation;
```

### 地方和世界变迁 {#local-and-world-transforms}

变形元件有几种方法可以让您返回变形矩阵实例, 被设定为本地或世界变形为游戏对象的变形实例 。

变形矩阵是用于执行affine变形的3x3身份矩阵。在Phaser中,操作按翻译、旋转和然后是Scale的顺序进行,始终按这个顺序进行。

`getLocalTransformMatrix`方法会返回一个纯粹本地变换矩阵:

```js
const matrix = player.getLocalTransformMatrix();
```

此矩阵将不包括父容器的任何变换。 它只包含游戏对象本身的变换 。

`getWorldTransformMatrix`方法将返回包含游戏对象局部变换的变换矩阵,乘以其所有父容器的变换:

```js
const matrix = player.getWorldTransformMatrix();
```

两种方法都有被通过变换矩阵的选项。 如果给出, 数值会被设置在这些选项中, 而不是创建并返回一个新的实例。 如果您经常调用其中任一方法, 即一个恒更新循环, 或者进行组合, 那么您应该创建一些临时矩阵来传递给它们, 以避免不断创建新对象 :

```js
const tempMatrix = new Phaser.GameObjects.Components.TransformMatrix();

player.getLocalTransformMatrix(tempMatrix);
```

Or:

```js
const tempMatrix = new Phaser.GameObjects.Components.TransformMatrix();
const tempParentMatrix = new Phaser.GameObjects.Components.TransformMatrix();

player.getWorldTransformMatrix(tempMatrix, tempParentMatrix);
```

## 可见组件 {#visible-component}

可见组件负责设定游戏对象的可见状态.

一个可见状态为`true`的游戏对象被渲染到显示器上,其中-作为一个可见状态为`false`的游戏对象不是. 默认情况下,Game Objects的可见状态为`true`.

目前游戏对象的本地可见状态存储在其 `visible` 布尔属性中:

```js
const visible = player.visible;
```

要设置可见状态,您可以使用可链式`setVisible`方法:

```js
player.setVisible(visible);
```

或者,你可以设置 `visible`布尔直接:

```js
player.visible = false;
```

默认情况下, Game Objects 将具有 `true` 的可见状态, 这意味着它们将被渲染 。

能够切换一个游戏对象的能见度,对于快速显示或隐藏游戏对象非常有用,而不会影响其位置或其他属性.

隐藏游戏对象被渲染器跳过, 保存周期时间, 但仍然保留其内部位置和状态 。 这意味着您可以隐藏游戏对象, 然后在稍后阶段再次显示, 无需重新定位或再次设定其他属性 。

然而,一个隐形游戏对象仍然在更新中。例如,如果您有动画Sprite正在通过动画序列播放,那么设定它为隐形不会像它仍在更新一样导致动画暂停。其他动作,如tweens,或者物理碰撞,同样如此。可见状态纯粹是渲染切换。

### 父可见度 {#parent-visibility}

如果游戏对象有一个父容器,那么如果其任何孩子被渲染,则其父的可见状态会控制。无论儿童本身的可见环境如何,其父的无形身份都会跳过所有儿童的渲染。但是,如果父母是可见的,那么孩子的粘性将被使用。

---
