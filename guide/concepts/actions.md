# 动作（Actions） {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/actions)

在 Phaser 中,动作是通常通过将多个 Phaser 特性合并在一起来完成单一任务的函数,例如将一组图案放在一线线上,或者将一组图案围绕一个特定点旋转。动作贯穿一系列游戏对象,允许您对全部对象执行相同的动作,通常带有可选的偏移。有些动作被设定为一次,而另一些动作被设定为连续调用,作为更新循环的一部分。

动作在`Phaser.Actions`命名空间下是可用的,并且都是静态函数,所以可以直接调用它们.

## 将动作应用到一个组 {#applying-an-action-to-a-group}

如果您想要对 Phaser 游戏对象组应用动作, 您可以在引用动作时使用 Groups `getChildren()` 方法。 例如, 将 Group 中所有子的字母设置为 0. 5 。 您可以使用:

```js
Phaser.Actions.SetAlpha(myGroup.getChildren(), 0.5);
```

## 步数、索引和方向 {#step-index-and-direction}

除了游戏对象的数组可以操纵外,许多动作还采用了以下可选参数:

- `step`
- `index`
- `direction`

电话 `step` 参数是可选的金额,添加到 `value` 中,以重复计数器乘以。例如,如果在10个图案的阵列中,您将“% 1” 转至“% 1” `SetX` 行动,并设定 `value` 成为100,然后每个Sprite都会给100的同样x坐标,但是如果你设置这个 `step` 参数到50,然后第一个图案的位置是100,第二个是150,第三个是200,等等,作为 `step` 值(50)乘以数组迭代。这非常有助于快速提供单个动作的多样,而无需反复调用。

`index`参数控制从给定数组开始的偏移。 当您调用动作函数时, 您会通过一系列游戏对象来修改。 `index`参数允许您跳过数组中的“n” 项数, 由起始的 `index`定义, 并且只对剩余条目应用动作。 默认情况下, `index`z为零, 这意味着它会运行动作, 横跨数组中的每个条目。 `index`永远不能超过游戏对象数组的长度 。

`direction`参数允许您调整您通过游戏对象阵列排列的顺序。 默认值是 `1`, 表示它会从数组的起始到结尾排列。 如果您将 `direction` 设置为 `-1`, 它会从数组的结尾到起始排列。 如果您想要将动作应用到数组的顺序反转, 而无需修改数组本身, 这样做将是有益的 。

如果动作允许您指定步数、索引和方向,请回溯此处。

一些动作允许您指定两个步骤值, 如 Set Scap Action 。 这是因为该步骤被分割为动作的 `x` 属性和 `y` 属性。 如果是 Set Scap, 第一步值应用到 `scaleX` 属性, 第二个步骤值应用到 `scaleY` 属性。 请交叉引用您正在使用的动作文档, 以查看它是否支持此特性 。

## 动作列表 {#actions-list}

### 调整到 {#align-to}

取一系列游戏对象并相互对齐。

```js
Phaser.Actions.AlignTo(items, position, [offsetX], [offsetY]);
```

- `items`:此动作要更新的项目组。
- `position`: 将项目对齐的位置。 这是一个对齐常数, 如 `Phaser.Display.Align.LEFT_CENTER` 。
- `offsetX`: 位置可选水平偏移.
- `offsetY` : 位置上可选垂直冲抵.

### 角度 {#angle}

角度动作将 _ 添加_ 给定值到游戏对象数组的 `angle` 属性 。

```js
Phaser.Actions.Angle(myObjects, 90);
```

正如游戏对象指南所覆盖的,`angle`将游戏对象旋转的角度设定在度数.

因为这个动作是添加剂,这意味着你可以用`update`环来调用,或者类似,并且保持小量的递增对象角.

[文件:动作/角更新.js]

此动作支持可选的 `step`, `index`和 `direction` 参数。 详情请参见“ 步骤、 索引和方向” 部分 。

### 调用 {#call}

呼叫行动将取一系列游戏对象,然后传递给给给定的回调:

```js
Phaser.Actions.Call(myObjects, callback, context);
```

`callback`是一个函数,将针对阵列中的每个游戏对象引用它,它将被发送到游戏对象本身作为第一个参数.

使用本地的 `forEach` 方法可以实现相同的目的,所以在ES6中编码时不需要此动作:

```js
myObjects.forEach(callback, context);
```

然而,如果你使用ES5,那么这个动作就是一个有用的快捷方式.

### 获取第一并获取最后 {#get-first-and-get-last}

Get First Action 将带一组游戏对象和一个比较对象。 它会将矩阵进行斜移, 并返回第一个匹配比较对象中所有条件的游戏对象 :

```js
const first = Phaser.Actions.GetFirst(myObjects, { scaleX: 0.5, alpha: 1 });
```

在上述例子中,第一个游戏对象的`scaleX`值为0.5,`alpha`值为1,如果阵列中游戏对象没有匹配条件,则返回`null`.

比较还可以包括引用其他对象。例如,要获得第一个有特定纹理的游戏对象,你可以做到:

```js
const fireTexture = this.textures.get('fire');

const first = Phaser.Actions.GetFirst(myObjects, { texture: fireTexture });
```

比较对象可以拥有您喜欢的多个属性。 比较对象中的每个属性都必须映射到游戏对象上的属性, 即 `visible`, `x`, `y`, `scaleX`等。 如果您包含一个游戏对象没有的属性, 它很可能永远无法返回匹配。 比较不能匹配嵌入属性, 如 `texture.name`。 比较很严格, 所以 `===`用来比较数值 。

Get Last Action 完全一样工作, 但返回与比较对象匹配的阵列中的 _ last_ Game Object。 它从阵列的结尾开始, 向起始点方向移动, 以此实现此目的 。

### 网格对齐 {#grid-align}

取一系列游戏对象,或任何具有公开的`x`和`y`属性的物体,然后根据给予此动作的网格配置来校正它们.

```js
Phaser.Actions.GridAlign(items, options);
```

- `items`:此动作要更新的项目组。
- `options`: 网格对齐配置对象.
  - `width`: 各个项( 不像素) 的网格宽度。 - 1 表示所有项都水平排列, 不论数量大小 。
  - `height`: 物品中的网格高度(不是像素)。 -1 表示所有物品都垂直排列,无论数量多少。
  - `cellWidth`:单元格的宽度,以像素表示,项目位于其中。
  - `cellHeight`:单元格的高度,以像素表示,物品所在的位置.
  - `position`:对齐位置,`Phaser.Display.Align`的其中一款曲轴,如`TOP_LEFT`或`RIGHT_CENTER`.
  - `x` :可选地将最终网格的左上方置于这个坐标处.
  - `y` :可选地将最终网格的左上方置于这个坐标处.

### 阿尔法 Inc Alpha 公司 {#inc-alpha}

Inc Alpha Action 将_add_ 游戏对象数组的 `alpha` 属性的给定值 。

```js
Phaser.Actions.IncAlpha(myObjects, 0.1);
```

正如游戏对象指南所涵盖,`alpha`属性控制了游戏对象的α值,其中0完全透明,1完全不透明.

因为这个动作是添加剂,这意味着你可以用`update`环来调用它,或者类似,以保持物体的α的递增小量.

[文件:动作/inc alpha更新.js]

此动作支持可选的 `step`, `index`和 `direction` 参数。 详情请参见“ 步骤、 索引和方向” 部分 。

### 第十、Y和XY公司 {#inc-x-inc-y-and-inc-xy}

Inc X Action 将_add_ 游戏对象数组的 `x` 属性的给定值 。

```js
Phaser.Actions.IncX(myObjects, 10);
```

在上述例子中,阵列中的所有游戏对象都会在其目前的`x`值中增加10个.

Inc Y 动作将 _ add_ 游戏对象数组的 `y` 属性的给定值 。

```js
Phaser.Actions.IncY(myObjects, 10);
```

在这个例子中,阵列中的所有游戏对象都会在其目前的`y`值中增加10个.

这两种动作都是添加剂,这意味着你可以用`update`环来称呼它们,或类似的,以保持小量的物体位置增量.

ex和Inc Y Actions都支持可选的`step`,`index`和`direction`参数. 详情请参见"步骤,索引和方向"部分.

Inc XY Action 将 _add_给定值添加到游戏对象阵列的`x`和`y`属性中.

```js
Phaser.Actions.IncXY(myObjects, 4, 6);
```

在上述例子中,阵列中的所有游戏对象都会在其当前`x`值中加上4个,在目前`y`值中加上6个.

动作是添加剂,这意味着你可以用`update`环来调用,或者类似,以保持小量的物体位置增量.

此动作支持可选 `index` 财务报告和已审计财务报表 `direction` 参数。详情请参见“步骤、索引和方向”部分。它也支持 `step`然而,这被指定为两个不同的值, `stepX` 财务报告和已审计财务报表 `stepY` 用于乘法 `x` 财务报告和已审计财务报表 `y` 数值分别为:

```js
Phaser.Actions.IncXY(myObjects, 4, 6, 1.25, 1.5);
```

在上述例子中, `x` 数值将乘以1.25, `y` 数值将乘以1.5。

如果您想要设定游戏对象的位置而不是加增它们,请参见Set XY动作。

### 圆形上的位置 {#place-on-circle}

环形动作上的空间取一系列游戏对象,并围绕给定圆周圈的均匀间距点将其定位.

```js
const circle = new Phaser.Geom.Circle(400, 300, 200);

Phaser.Actions.PlaceOnCircle(myObjects, circle, startAngle, endAngle);
```

`circle`参数可以是任何具有公共`x`,`y`和`radius`属性的物体,然而对于强型语言来说,此动作会期望您通过一个`Phaser.Geom.Circle`对象,或者扩展它的一个对象.

`startAngle`和`endAngle`参数是可选的,允许您控制放置的始末位置。角度以弧度表示,其中值0在右侧,顺时针增加。因此,例如,如果您想要显示从圆顶到下方的游戏对象弧,您可以使用:

```js
Phaser.Actions.PlaceOnCircle(myObjects, circle, Math.PI * 1.5, Math.PI * 0.5);
```

游戏对象按其在阵列中出现时的顺序排列。 阵列中的第一个游戏对象将放置在圆上方的`startAngle`点, 下一个游戏对象将放置在环绕圆的下一个点, 直至到达`endAngle`点。 它们通过调整它们的`x`和`y`坐标来定位, 因此它们的起源将对这些点的显示方式发挥作用 。

如果您在调用此动作后修改了该动作的下方圆对象, 它不会对定位在它上的游戏对象产生影响, 直到您再次调用此动作。 如果您想要激活此进程, 您可以在修改圆形以创建一些有趣的实时效果的同时, 将此动作调用 `update`、 扭矩或定时循环 。

### 椭圆上的位置 {#place-on-ellipse}

椭圆行动上的"位置"取一系列游戏对象,并定位在给定椭圆周长周围的均匀空位点上.

```js
const ellipse = new Phaser.Geom.Ellipse(400, 300, 200, 300);

Phaser.Actions.PlaceOnEllipse(myObjects, ellipse, startAngle, endAngle);
```

`ellipse`参数可以是任何具有公共`x`,`y`,`width`和`height`属性的物体,然而对于强型语言,此动作会期望您通过一个`Phaser.Geom.Ellipse`对象,或者扩展它的一个对象.

`startAngle`和`endAngle`参数是可选的,允许您控制放置的始末。角度以弧度表示,其中值为 0 向右并顺时针增加。因此,例如,如果您想要显示从椭圆顶部到底部的游戏对象弧,您可以使用:

```js
Phaser.Actions.PlaceOnEllipse(myObjects, ellipse, Math.PI * 1.5, Math.PI * 0.5);
```

游戏对象按其在阵列中出现顺序排列。 阵列中的第一个游戏对象将放置在椭圆形上的`startAngle`点, 下一个游戏对象将放置在环椭圆形的下一个点, 直至到达`endAngle`点。 它们通过调整它们的`x`和`y`坐标来定位, 因此它们的起源将在这些点的显示方式中发挥作用 。

如果您在调用此动作后修改了下面的椭圆对象, 它不会对它上定位的游戏对象产生影响, 直到您再次调用此动作。 如果您想要激活此进程, 您可以在修改椭圆形状以创建一些有趣的实时效果的同时, 将此动作调用 `update`、 扭矩或定时循环 。

### 在线位置 {#place-on-line}

线上行动位置取一系列游戏对象,并沿给定线长度在均匀的空格点上定位.

```js
const line = new Phaser.Geom.Line(100, 100, 700, 500);

Phaser.Actions.PlaceOnLine(myObjects, line);
```

`line`参数可以是任何具有公共`x1`,`y1`,`x2`和`y2`属性的物体,然而对于强型语言,此动作会期望您通过一个`Phaser.Geom.Line`对象,或者扩展它的一个对象.

游戏对象按其在阵列中出现的顺序排列。阵列中的第一个游戏对象将放置在 `x1` 财务报告和已审计财务报表 `y1` 点,下个游戏对象放在线上的下一个点,等等,直到它到达 `x2` 财务报告和已审计财务报表 `y2` 。通过调整其位置来定位它们。 `x` 财务报告和已审计财务报表 `y` 坐标,所以它们的起源将在如何显示它们与这些点的关系上发挥作用.

如果您在调用此动作后修改了该动作的下行对象, 它不会对定位在它上的游戏对象产生影响, 直到您再次调用此动作。 如果您想要激活此进程, 您可以在修改行形状以创建一些有趣的实时效果的同时, 以 `update` 、 tween 或 定时循环方式调用此动作 。

### 位于矩形上 {#place-on-rectangle}

矩形动作上的位置取一系列游戏对象,并把它们定位在指定矩形周边的均匀的空格点上.

```js
const rect = new Phaser.Geom.Rectangle(100, 100, 600, 400);

Phaser.Actions.PlaceOnRectangle(myObjects, rect);
```

`rect`的论证应该是`Phaser.Geom.Rectangle`对象的实例,或者扩展对象的实例.

放置从矩形的上左开始,然后顺时针方向继续绕着它。游戏对象按其在阵列中出现顺序排列。阵列中的第一个游戏对象将放在矩形的上左,下一个游戏对象将放在矩状的下个点,等等,直到它再次绕到左上点。它们通过调整它们的`x`和`y`坐标来定位,因此它们的起源将在这些点的显示方式中发挥作用。

此动作还有一个可选的 `shift` 参数。 这样您就可以控制放置的起点。 默认情况下, 阵列中的第一个游戏对象位于周边的第一个点。 但是 `shift`参数允许您从另一个点开始放置。 例如, 如果您设定 `shift` 为 1, 那么, 阵列中第一个游戏对象将放在周边的第二点, 而不是第一个。 如果您设定 `shift`为 2, 那么, 阵阵列中的第一个游戏目标将放在周边的第三点, 依此推。 游戏对象仍将环绕矩形的全部周边, 不论 `shift`值如何 。

如果您在调用此动作后修改了其中的矩形对象, 它不会对定位在它上的游戏对象产生影响, 直到您再次调用此动作。 如果您想要激活此进程, 您可以在修改矩形以创建一些有趣的实时效果的同时, 将此动作调用 `update`、 扭矩或定时循环 。

### 沿三角形边缘放置 {#place-on-triangle}

"三角行动"(Place on Trangle Action)拍摄了一系列游戏对象,并把它们定位在指定三角形周边的均匀的空间点上.

```js
const triangle = new Phaser.Geom.Triangle(400, 100, 100, 500, 700, 500);

Phaser.Actions.PlaceOnTriangle(myObjects, triangle);
```

`triangle`参数可以是任何具有公共`x1`,`y1`,`x2`,`y2`,`x3`和`y3`属性的物体,然而对于强型语言来说,此动作会期望您通过一个`Phaser.Geom.Triangle`对象,或者扩展它的一个对象.

游戏对象按其在阵列中出现顺序排列. 阵列中的第一个游戏对象将放置在三角形上的`x1`和`y1`点,下一个游戏对象将放置在环三角形的下一个点,等等,直到它再次到达起点. 三角形的每个面的点使用布雷森汉姆斯线算法计算,并消除重叠.

游戏对象通过调整其`x`和`y`坐标定位,因此其起源将发挥与这些点相关的显示方式的作用.

此动作有一个可选的 `stepRate` 参数。 这使得您可以控制点的包装密度。 默认值为 1 。 将其修改为下或上值, 以修改点之间的间隔 。

如果您在调用此动作后修改了底部的三角对象, 它不会对定位在它上的游戏对象产生影响, 直到您再次调用此动作。 如果您想要激活此进程, 您可以在修改三角形状以创建一些有趣的实时效果的同时, 将此动作调用 `update` 、 tween 或 定时循环 。

### 播放动画 {#play-animation}

游戏动画动作将在阵列中的所有游戏对象上开始播放给定的动画.

```js
Phaser.Actions.PlayAnimation(myObjects, key);
```

此动作将检查, 以确保游戏对象在尝试播放动画前有动画状态组件。 如果没有, 则会跳过 。

动作有可选的 `ignoreIfPlaying` 参数。 如果设定为 `true`, 如果游戏对象已经在播放指定的动画, 则不会开始动画。 默认值为 `false` 。

### 递增属性值 {#property-value-inc}

取一系列游戏对象, 或任何在 `key` 中定义的公共属性对象, 然后添加到给定值 _adds_。 可选的 `step` 属性被递增应用, 乘以数组中的每个项目 。

```js
Phaser.Actions.PropertyValueInc(items, key, value, [step], [index], [direction]);
```

- `items`:此动作要更新的项目组。
- `key` : 需要更新的属性.
- `value` : 属性中应加的金额.
- `step`:这是加在数值上的乘以重置计数器。
- `index`: 从项目阵列中开始搜索的可选偏移 。
- `direction`:通过阵列的斜拉方向。 1 是从头到尾, - 1 从头到尾。

### 属性值集 {#property-value-set}

取一系列游戏对象,或任何具有`key`定义的公共属性的对象,然后设定为给定值。可选的`step`属性被递增应用,乘以数组中的每个项目。

```js
Phaser.Actions.PropertyValueSet(items, key, value, [step], [index], [direction]);
```

- `items`:此动作要更新的项目组。
- `key` : 需要更新的属性.
- `value` : 属性中应加的金额.
- `step`:这是加在数值上的乘以重置计数器。
- `index`: 从项目阵列中开始搜索的可选偏移 。
- `direction`:通过阵列的斜拉方向。 1 是从头到尾, - 1 从头到尾。

### 随机圆 {#random-circle}

随机圆形动作取一系列游戏对象,并在圆形的随机位置定位.

```js
const circle = new Phaser.Geom.Circle(400, 300, 200);

Phaser.Actions.RandomCircle(myObjects, circle);
```

`circle`参数可以是任何具有公共`x`,`y`和`radius`属性的物体,然而对于强型语言来说,此动作会期望您通过一个`Phaser.Geom.Circle`对象,或者扩展它的一个对象.

游戏对象按其出现在阵列中的顺序排列。阵列中的第一个游戏对象将放在圆内随机点,下一个游戏对象将放在圆内的下一个随机点,直至其到达阵列的终点。它们通过调整它们的`x`和`y`坐标来定位,因此它们的起源将在这些点的显示方式中发挥作用。

此动作并不试图在圆内符合游戏对象的界限,它只是按其位置来放置,所以完全有可能根据大小将游戏对象扩展到圆外,从圆内选择的随机位置是统一分布的,也就是说它和圆内中心内的一个点一样有可能返回.

如果您在调用此动作后修改了该动作的内在圆形对象, 它不会对它内定位的游戏对象产生影响, 直到您再次调用此动作。 请注意, 调用此动作多次总是会使您获得不同的随机位置 。

### 随机椭圆 {#random-ellipse}

"随机椭圆行动"取了一系列游戏对象,并在椭圆形状的随机位置定位.

```js
const ellipse = new Phaser.Geom.Ellipse(400, 300, 200, 300);

Phaser.Actions.RandomEllipse(myObjects, ellipse);
```

`ellipse`参数可以是任何具有公共`x`,`y`,`width`和`height`属性的物体,然而对于强型语言,此动作会期望您通过一个`Phaser.Geom.Ellipse`对象,或者扩展它的一个对象.

游戏对象按其出现在阵列中的顺序排列。阵列中的第一个游戏对象将放在椭圆内部的随机点,下一个游戏对象将放在椭球内部的下一个随机点,直至其到达阵列的末尾。它们通过调整它们的`x`和`y`坐标来定位,因此它们的起源将在这些点的显示方式中发挥作用。

此动作并不试图在椭圆内符合游戏对象的界限,它只是按其位置将其放置,所以完全有可能您的游戏对象会根据其大小在椭圆外延伸.

如果您在调用此动作后修改了下面的椭圆对象, 则在您再次调用此动作之前, 它对游戏中定位的游戏对象不会产生任何效果 。 请注意, 多次调用此动作将总是导致您获得不同的随机位置 。

### 随机线 {#random-line}

"随机线行动"取一系列游戏对象,并沿一个线段长度随机定位.

```js
const line = new Phaser.Geom.Line(100, 100, 700, 500);

Phaser.Actions.RandomLine(myObjects, line);
```

`line`参数可以是任何具有公共`x1`,`y1`,`x2`和`y2`属性的物体,然而对于强型语言,此动作会期望您通过一个`Phaser.Geom.Line`对象,或者扩展它的一个对象.

Game Objects按其出现在阵列中的顺序排列. 阵列中的第一个游戏对象将放在线上的随机点,下一个游戏对象将放在线上下一个随机点,直至其到达阵列的末尾为止。 它们通过调整它们的`x`和`y`坐标来定位,因此它们的起源将在这些点的显示方式上发挥作用。

如果您在调用此动作后修改了该动作的下行对象, 它不会对之前定位于它的游戏对象产生影响, 直到您再次调用此动作。 请注意, 调用此动作多次将总是导致您获得不同的随机位置 。

### 随机矩形 {#random-rectangle}

"随机矩形"动作取一系列游戏对象,并在一个矩形的随机位置定位.

```js
const rect = new Phaser.Geom.Rectangle(100, 100, 600, 400);

Phaser.Actions.RandomRectangle(myObjects, rect);
```

`rect`参数可以是任何具有公共`x`,`y`,`width`和`height`属性的物体,然而对于强型语言,此动作会期望您通过一个`Phaser.Geom.Rectangle`对象,或者扩展它的一个对象.

游戏对象按其出现在阵列中的顺序排列。 阵列中的第一个游戏对象将放在矩形内的随机点, 下一个游戏对象将放在矩体内的下一个随机点, 直至其到达阵列的末尾。 它们通过调整它们的`x`和`y`坐标来定位, 因此它们的起源将在这些点的显示方式中发挥作用 。

这个动作并不试图在矩形内符合游戏对象的界限,它只是按其位置将其放置,因此,你的游戏对象完全有可能根据大小在矩形外延伸.

如果您在调用此动作后修改了后面的矩形对象, 它不会对它内定位的游戏对象产生影响, 直到您再次调用此动作。 请注意, 调用此动作多次将总是导致您获得不同的随机位置 。

### 随机三角形 {#random-triangle}

"随机三角行动"取了一系列游戏对象,并在三角形的随机位置定位.

```js
const triangle = new Phaser.Geom.Triangle(400, 100, 100, 500, 700, 500);

Phaser.Actions.RandomTriangle(myObjects, triangle);
```

`triangle`参数可以是任何具有公共`x1`,`y1`,`x2`,`y2`,`x3`和`y3`属性的物体,然而对于强型语言来说,此动作会期望您通过一个`Phaser.Geom.Triangle`对象,或者扩展它的一个对象.

游戏对象按其在阵列中出现顺序定位。 阵列中的第一个游戏对象将放在三角形的随机点, 下一个游戏对象将放在三角座的下一个随机点, 直至其到达阵列的末尾。 它们通过调整它们的`x`和`y`坐标来定位, 因此它们的起源将对这些点的显示方式发挥作用 。

这个动作并不试图在三角形内匹配游戏对象的界限,它只是按其位置将其放置,所以完全有可能你的游戏对象会根据大小在三角形之外延伸.

如果您在调用此动作后修改了该动作的三角对象, 则它不会对它内置的游戏对象产生影响, 直到您再次调用此动作。 请注意, 调用此动作多次将总是导致您获得不同的随机位置 。

### 旋转 {#rotate}

旋转动作将 _ 添加_ 给定值到游戏对象数组的 `rotation` 属性 。

```js
Phaser.Actions.Rotate(myObjects, 0.5);
```

如游戏对象指南所覆盖,`rotation`设定了一个游戏对象在弧度中旋转的角度.

因为这个动作是添加剂,这意味着你可以用`update`环来调用,或者类似,并且保持小量的物体旋转增量.

此动作支持可选的 `step`, `index`和 `direction` 参数。 详情请参见“ 步骤、 索引和方向” 部分 。

### 旋转 {#rotate-around}

以弧度角度将每个项目绕给定点旋转。

```js
Phaser.Actions.RotateAround(items, point, angle);
```

- `items`: 游戏对象阵列。 此阵列的内容由此动作更新 。
- `point`:任何具有公共x和y属性的物体.
- `angle` : 旋转的角度, 以弧度表示。

### 绕距离旋转 {#rotate-around-distance}

将游戏对象的阵列绕一个点旋转,以给定的角度和距离。

```js
Phaser.Actions.RotateAroundDistance(items, point, angle, distance);
```

- `items`: 游戏对象阵列。 此阵列的内容由此动作更新 。
- `point`:任何具有公共x和y属性的物体.
- `angle` : 旋转的角度, 以弧度表示。
- `distance`:以像素表示的旋转点的距离.

### 缩放 X、 Y 和 XY {#scale-x-y-and-xy}

缩放动作将 _ 添加到给定值到游戏对象数组的 `scaleX` 或 `scaleY` 属性中 。

```js
Phaser.Actions.ScaleX(myObjects, 0.5);
Phaser.Actions.ScaleY(myObjects, 0.5);
Phaser.Actions.ScaleXY(myObjects, 0.5, 0.25);
```

在上述例子中,阵列中的所有游戏对象都会在当前的游戏中添加0.5 `scaleX` 值。“缩放 Y”动作将同样用于 `scaleY` 属性。缩放 XY 动作将同时对两个 `scaleX` 财务报告和已审计财务报表 `scaleY` 属性。您可以选择适合您需要的动作。

因为这些动作是添加剂,这意味着你可以用`update`环来称呼它们,或者类似,并且不断用小量修改对象的尺度.

这三种动作支持可选的`step`,`index`和`direction`参数. 详情请参见"步骤,索引和方向"部分.

### 设定 Alpha {#set-alpha}

Set Alpha Action 将设定游戏对象阵列的 `alpha` 属性为给定值 :

```js
Phaser.Actions.SetAlpha(myObjects, 0.5);
```

正如游戏对象指南所涵盖,`alpha`属性控制了游戏对象的α值,其中0完全透明,1完全不透明.

Set Alpha 动作不测试游戏对象是否有Alpha 组件。 它只是设置属性, 不管怎样, 所以要小心您通过的项目数组 。

此动作支持可选的 `step`, `index`和 `direction` 参数。 详情请参见“ 步骤、 索引和方向” 部分 。

### 设置组合模式 {#set-blend-mode}

Set 混合模式动作将设定游戏对象阵列的 `blendMode` 属性为给定值 :

```js
Phaser.Actions.SetBlendMode(myObjects, Phaser.BlendModes.ADD);
```

请参见指南中的“混合模式”部分,以了解可用不同模式的详细情况。

Set 混合模式动作不测试游戏对象是否支持混合模式。它只是设置属性,不管怎样,所以要小心您通过的项目数组 。

此动作支持可选的 `index`和 `direction` 参数。 详情请参见“ 步骤、 索引和方向” 部分。 请注意, 它不包括 `step` 支持 。

### 设置深度 {#set-depth}

设定深度动作将把一系列游戏对象的 `depth` 属性设定为给定值 :

```js
Phaser.Actions.SetDepth(myObjects, 100);
```

正如Game Objects指南所涵盖,`depth`属性控制着一个Game Objects的渲染顺序,其中数值越高,它会越是在其他Game Objeces上渲染.

设定深度动作不测试游戏对象是否有深度组件。 它只是设置属性, 不管怎样, 所以要小心您通过的项目数组 。

此动作支持可选的 `step`, `index`和 `direction` 参数。 详情请参见“ 步骤、 索引和方向” 部分 。

### 设定点击区域 {#set-hit-area}

传阅所有向输入管理器提供的游戏对象,以允许它们输入相同区域和回调的输入.

```js
Phaser.Actions.SetHitArea(items, [hitArea], [callback]);
```

- `items`: 游戏对象阵列。 此阵列的内容由此动作更新 。
- `hitArea` : 输入配置对象, 或定义游戏对象的命中区域的几何形状。 如果不给它, 它将尝试根据纹理帧创建矩形 。
- `callback`: 用于确定指针是否在命中区域形状之内的调用。 如果您提供了形状, 您也必须提供调用 。

### 设置来源 {#set-origin}



### 设置旋转 {#set-rotation}

设定旋转动作将把一系列游戏对象的 `rotation` 属性设定为给定值 :

```js
Phaser.Actions.SetRotation(myObjects, 1.5707);
```

如游戏对象指南所覆盖,`rotation`设定了一个游戏对象在弧度中旋转的角度.

设定旋转动作不会测试游戏对象是否有变形组件。 它只是设置属性, 不管怎样, 所以要小心您通过的项目数组 。

此动作支持可选的 `step`, `index`和 `direction` 参数。 详情请参见“ 步骤、 索引和方向” 部分 。

### 设置缩放 {#set-scale}

设定缩放动作将把一系列游戏对象的`scaleX`和`scaleY`属性设定为给定值:

```js
Phaser.Actions.SetScale(myObjects, 0.5, 0.25);
```

在上述例子中,阵列中的所有游戏对象都会将其`scaleX`属性设定为0.5,其`scaleY`属性设定为0.25.

Set ScaleX 动作会将一系列游戏对象的 `scaleX` 属性设定为给定值 :

```js
Phaser.Actions.SetScaleX(myObjects, 0.5);
```

在上述例子中,阵列中的所有游戏对象都会将其`scaleX`属性设定为0.5,其`scaleY`属性将保持不变.

Set ScalY 动作将把一系列游戏对象的 `scaleY` 属性设定为给定值 :

```js
Phaser.Actions.SetScaleY(myObjects, 0.25);
```

在上述例子中,阵列中的所有游戏对象都会将其`scaleY`属性设定为0.25. 它们的`scaleX`属性将保持不变.

设定缩放动作不会测试游戏对象是否有变形组件。 它只是设置属性, 不管怎样, 所以要小心您通过的项目组 。

这些行动支持可选的 `stepX`, `stepY`, `index`和 `direction` 参数。详情请参见"步骤,索引和方向" 部分.

### 设置滚动因子 {#set-scroll-factor}

设定滚动因子动作将把一系列游戏对象的`scrollFactorX`和`scrollFactorY`属性设定为给定值:

```js
Phaser.Actions.SetScrollFactor(myObjects, 1, 0);
```

在上述例子中,阵列中的所有游戏对象都会将自己的`scrollFactorX`属性设定为1,而他们的`scrollFactorY`属性设定为0.

设定 ScrollFactorX 动作会将一系列游戏对象的 `scrollFactorX` 属性设置到给定值 :

```js
Phaser.Actions.SetScrollFactorX(myObjects, 1);
```

在上述例子中,阵列中的所有游戏对象都会将其`scrollFactorX`属性设定为1. 其`scrollFactorY`属性将保持不变.

设定 ScrollFactorY 动作会将一系列游戏对象的 `scrollFactorY` 属性设置到给定值 :

```js
Phaser.Actions.SetScrollFactorY(myObjects, 0);
```

在上述例子中,阵列中的所有游戏对象都会将其`scrollFactorY`属性设定为0.25. 它们的`scrollFactorX`属性将保持不变.

设置滚动因子动作不会测试游戏对象是否有变形组件。 它只是设置属性, 不管怎样, 所以要小心您通过的项目组 。

这些行动支持可选的 `stepX`, `stepY`, `index`和 `direction` 参数。详情请参见"步骤,索引和方向" 部分.

### 设置小点 {#set-tint}

Set Tint Action 取一系列游戏对象,并给每个对象调用`setTint`方法:

```js
Phaser.Actions.SetTint(myObjects, 0xff0000);
```

如游戏对象指南所涵盖, 锡定允许您通过对它应用锡定来改变游戏对象的颜色。 锡定通过从游戏对象中取出原始像素颜色值, 然后将每个像素颜色值乘以锡定的颜色值, 您可以提供一种颜色值, 这样整个游戏对象将用该颜色进行锡定。 或者您可以提供每个角的颜色 :

```js
Phaser.Actions.SetTint(myObjects, 0xff0000, 0x00ff00, 0x0000ff, 0xff00ff, 0x00ffff);
```

在上方的例子中, Game Object 将用红色色色在左上角,绿色在右上角,蓝色在左下角,紫色在右下角。颜色将混合到游戏对象的全程。

Set Tint Action 无法测试游戏对象是否有Tint 组件。 它只是设置属性, 不管怎样, 所以要小心您通过的项目组 。

### 设置可见 {#set-visible}

设定可见动作会将一组游戏对象的`visible`属性设定为给定值:

```js
Phaser.Actions.SetVisible(myObjects, false);
```

如游戏对象指南所涵盖,`visible`属性控制是否渲染出游戏对象.

此动作支持可选的 `index`和 `direction` 参数。 详情请参见“ 步骤、 索引和方向” 部分。 请注意, 它不包括 `step` 支持 。

### 设定 XY {#set-xy}

Set XY动作将把一组游戏对象的`x`和`y`属性设定为给定值:

```js
Phaser.Actions.SetXY(myObjects, 100, 200);
```

在上述例子中,阵列中的所有游戏对象都会将他们的`x`属性设定为100,而他们的`y`属性设定为200.

Set X Action 将把一系列游戏对象的 `x` 属性设定为给定值 :

```js
Phaser.Actions.SetX(myObjects, 100);
```

在上述例子中,阵列中的所有游戏对象都会将他们的`x`属性设定为100. 它们的`y`属性将保持不变.

Set Y 动作将把一系列游戏对象的 `y` 属性设定到给定值 :

```js
Phaser.Actions.SetY(myObjects, 200);
```

在上述例子中,阵列中的所有游戏对象都会将其`y`属性设定为200. 它们的`x`属性将保持不变.

Set XY 动作不会测试游戏对象是否有变形组件。 它只是设置属性, 不管怎样, 所以要小心您通过的项目的数组 。

这些行动支持可选的 `stepX`, `stepY`, `index`和 `direction` 参数。详情请参见"步骤,索引和方向" 部分.

如果您想要增加游戏对象的位置而不是设置它们,请参见Inc X, Inc Y 和 Inc XY Actions 。

### 移动位置 {#shift-position}

Shift 位置动作将一系列游戏对象,然后通过它们进行移动,调整它们的`x`和`y`位置,成为数组中上一个条目的功能。数组中的第一个游戏对象被称为“头”项。头的位置被设定为您传递到此动作的`x`和`y`值 :

```js
Phaser.Actions.ShiftPosition(myObjects, 400, 300);
```

在上述例子中,阵列中的第一个游戏对象将被定位为400 x 300. 阵列中的下一个游戏对象将被定位到第一个游戏对象移动前的任意位置,等等. 阵列结束时,最后一个游戏对象将被定位到第二个游戏对象的位置.

您可以在控制迭代顺序的 `direction` 参数中通过。 默认值为 0, 表示输入数组中从第一个到最后一个。 如果您在数值中向后通过1, 从数组中的最后元素到第一个元素。

动作返回一个矢量2,它包含动作被调用之前数组中最后一个游戏对象的位置.

思考此动作的好方法与经典的诺基亚蛇游戏有关,当蛇移动时,蛇的“头”会朝一个方向移动,然后所有尾片会移到前一个尾段的位置,这个动作可以用来复制这种效果.

### 散牌游戏 {#shuffle}

shuffle Action将采取一个阵列,它实际上可以出现在任何东西上,但主要针对游戏对象,并洗涤它的内容:

```js
Phaser.Actions.Shuffle(myObjects);
```

阵列的内容被洗涤到位。 没有创建新的阵列 。

### Smooth Step 与 Smoother Step 插值 {#smooth-step-and-smoother-step}

这样做便于建立使用`smoothstep`的转换序列,将每个段插入,作为使用更精密或昂贵的插入技术的替代.

```js
Phaser.Actions.SmoothStep(items, property, min, max, [inc]);
Phaser.Actions.SmootherStep(items, property, min, max, [inc]);
```

- `items`: 游戏对象阵列。 此阵列的内容由此动作更新 。
- `property`:游戏对象的属性,用于插图.
- 最小插值(`min`):
- `max`:最大内插值.
- `inc`: 属性值是递增(`true`)还是设定(`false`)?

### 展开 {#spread}



### 切换可见 {#toggle-visible}

切换可见动作将取一系列游戏对象,然后切换每个对象的“可见”状态:

```js
Phaser.Actions.ToggleVisible(myObjects);
```

如果游戏对象可见, 则会设置为无形。 如果它看不见, 则设置为可见 。

切换可见动作不会测试游戏对象是否有可见属性。 它只是设置属性, 不论大小, 所以要小心您通过的项目组 。

### 在矩形中环绕 {#wrap-in-rectangle}

---
