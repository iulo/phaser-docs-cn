# 制作第一个 Phaser 游戏 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/getting-started/making-your-first-phaser-game)

![image](https://cdn.phaser.games/oss-docs/assets/5231a636fe7df734-tutorial-header.png)

欢迎来到我们的第一个关于用 Phaser 3 制作游戏的教程。 在这里,我们将学习如何创建一个小游戏,让玩家在平台上跑步跳跃,收集星星,避免坏人。 在经历这个过程的同时,我们将解释框架的一些核心特征。

## 所需经费 {#requirements}

[Download this zip file](https://cdn.phaser.io/tutorials/making-your-first-phaser-3-game/phaser3-tutorial-src.zip) 包含此教程的每个步骤, 代码和随它而来的资产。

你需要对JavaScript有非常基本的知识.

同时确保您通过[Getting Started Guide](/guide/getting-started/set-up-dev-environment),它会显示您如何下载框架,建立本地开发环境,并给您一个Phaser项目的结构及其核心职能的一瞥.

如果您已经读过“ 获取启动指南” , 您将会下载 Phaser 并准备好所有设置和代码。 将此教程的资源下载到您的网络根中 。

在您选择的编辑器中打开 `part1.html`的页面,让我们仔细看看代码。 在包含 Phaser的小锅炉板 HTML 之后,代码结构看起来是这样的:

```js
var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config);

function preload ()
{
}

function create ()
{
}

function update ()
{
}
```

配置对象是您如何配置您的 Phaser 游戏。 有很多选项可以放在此对象中, 当你扩展您的 Phaser 知识时, 您将会遇到更多的选项。 但是在这个教程中, 我们只是设置渲染器、 尺寸和默认的场景 。

Phaser.Game对象的示例被指定给一个名为`game`的本地变量,配置对象被传递给它。这将启动将Phaser带回生命的过程 。

`type`属性可以是`Phaser.CANVAS`, `Phaser.WEBGL`, 也可以是`Phaser.AUTO`。 这是您想要用于游戏的渲染上下文。 建议的值是 `Phaser.AUTO`, 它会自动尝试使用 WebGL, 但如果浏览器或设备不支持它, 它会掉回 Canvas 。 PhaserZ 创建的画布元素会在脚本被调用时直接附在文档中, 但是如果您愿意, 您也可以在游戏配置中指定一个母容器 。

`width`和`height`的属性设定了 Phaser 将创建的画布元素的大小。 在这种情况下, 800 x 600 像素。 您的游戏世界可以是任意大小, 但游戏将显示的分辨率是此 。 

配置对象的 `scene` 属性将在此教程中进一步详细覆盖 。

# 制作第一个 Phaser 游戏 {#page-title-1}

来装上我们游戏所需的资产吧,你打个电话 Phaser 位于一个叫做“ 景色函数” 的内装器 `preload`. Phaser 将自动查找此函数, 当它开始并装入它内部定义的任何内容时。

目前 `preload` 函数为空。 将其修改为:

```js
function preload ()
{
    this.load.image('sky', 'assets/sky.png');
    this.load.image('ground', 'assets/platform.png');
    this.load.image('star', 'assets/star.png');
    this.load.image('bomb', 'assets/bomb.png');
    this.load.spritesheet('dude', 
        'assets/dude.png',
        { frameWidth: 32, frameHeight: 48 }
    );
}
```

这将装入5个资产: 4 个图像和一个图案工作表。 这对于你们中的一些人来说可能很明显, 但我想指出第一个参数, 也称为资产密钥( 即“ sky” , “ bomb” ) 。 此字符串是连接到已装入资产的一个链接, 也是您创建 Game Objects 时在代码中所使用的。 您可以随意使用任何有效的 JavaScript 字符串作为密钥 。

### 显示图像 {#display-an-image}

为了显示其中的一幅图像,我们加载的`create`函数内置了以下代码: .

`this.add.image(400, 300, 'sky');`

您可以在 `part3.html` 中找到它。 如果您在浏览器中加载它, 您现在应该看到一个包含蓝色天空背景的游戏屏幕 :

![image](https://cdn.phaser.games/oss-docs/assets/97eb81bbd8ae10c2-part3.png)

`400`和`300`是图像的x和y坐标。为什么是400和300?这是因为在Phaser 3中,所有游戏对象默认都根据中心定位。背景图像大小为800x600像素,所以如果我们显示它以0x0为中心,你只看到它的右下角。如果我们显示它为400x300,你可以看到整个东西。

**提示( I):** 可以用吗 `setOrigin` 更改此选项。例如,代码: `this.add.image(0, 0, 'sky').setOrigin(0, 0)` 将图像的绘图位置重置到左上。 Phaser 2 实现这一目的是通过 `anchor` 属性,但 Phaser 3,这是 `originX` 财务报告和已审计财务报表 `originY` 属性。

显示游戏对象的顺序与创建对象的顺序一致。 因此, 如果您想要将星图示置于背景之上, 您需要确保它作为图像第二, 仅次于天空图像 :

```js
function create ()
{
    this.add.image(400, 300, 'sky');
    this.add.image(400, 300, 'star');
}
```

如果你先放`star`图像的话,它会被天空图像遮盖.

# 制作第一个 Phaser 游戏 {#page-title-2}

在头罩下 `this.add.image`正在创建一个新的图像游戏对象, 并添加到当前 Scases 显示列表中。 此列表是您所有游戏对象的居住地点。 您可以将图像定位到任何地方, Phaser不会介意。 当然, 如果它不在 0x0 到 800x600 的区域, 那么您不会看到它, 因为它会是“ 关闭屏幕 ” , 但是它仍然存在于 Scee 中 。

场景本身没有固定的大小, 并且无限地向各个方向延伸。 相机系统控制您的视线进入场景, 您可以按要求移动和放大活动相机。 您也可以为其它视线进入场景创建新的相机。 这一主题超出了此特定导师的范围, 足以说明Phaser 3 中的相机系统比 v2 中的强得多 。 在此之前实际上不可能实现的事情是 。

现在让我们通过添加背景图像和一些平台来建立场景。 以下是更新的 `create` 函数 :

```js
var platforms;

function create ()
{
    this.add.image(400, 300, 'sky');

    platforms = this.physics.add.staticGroup();

    platforms.create(400, 568, 'ground').setScale(2).refreshBody();

    platforms.create(600, 400, 'ground');
    platforms.create(50, 250, 'ground');
    platforms.create(750, 220, 'ground');
}
```

快速地在代码上闪烁,你会看到一个给`this.physics`的电话。这意味着我们正在使用Arcade物理系统,但是在这样做之前,我们需要把它添加到我们的游戏配置中,告诉Phaser我们的游戏需要它。所以让我们更新这个功能,以包括物理支持。这里是经过修改的游戏配置:

```js
var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 300 },
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};
```

新的添加是 `physics` 属性。 如果您运行的话, 此代码已经存在, 您可以在导读的zip文件中找到 `part4.html`, 您应该看到一个更像游戏的场景 :

![image](https://cdn.phaser.games/oss-docs/assets/6847c736400e5a69-part4.png)

我们有一个背景和一些平台, 但是这些平台究竟如何运作?

# 制作第一个 Phaser 游戏 {#page-title-3}

我们刚刚在`create`功能上添加了一组代码,值得更详细解释。

```js
platforms = this.physics.add.staticGroup();
```

由此创建了一个新的静态物理组,并将其分配到本地变量`platforms`. 在Arcade物理中,有两种物理体:动态和静态. 动态体是一个可以通过速度或加速等力运动的体,它可以反弹并与其他物体碰撞,碰撞受体积和其他元素的质量影响.

与此形成鲜明对比的是,静态体只是有一个位置和大小。它没有重力的触动,不能设定速度,当东西与它碰撞时,它就永远不动。静态体是名副其实的,静态体是自然的。 完美地适合我们让玩家运行的地面和平台。

但是,什么是游戏群?由于它们的名字意味着它们是一种方法,可以将相似的对象组合在一起,并作为一个单一单位控制它们。您也可以检查游戏群与其他游戏对象之间的碰撞。各小组可以通过`create`等手动辅助功能创建自己的游戏对象。一个物理群将自动创建物理功能化的孩子,从而在过程中节省一些腿动工。

有了我们的平台集团,我们现在可以利用它来创建平台:

```js
platforms.create(400, 568, 'ground').setScale(2).refreshBody();

platforms.create(600, 400, 'ground');
platforms.create(50, 250, 'ground');
platforms.create(750, 220, 'ground');
```

正如我们以前看到的,它创造了这个场景:

在预装过程中,我们导入了一个“地面”图像。它是一个简单的绿色矩形,大小400x32像素,将满足我们的基本方形需求:

![image](https://cdn.phaser.games/oss-docs/assets/217f58784eec49b7-platform.png)

上面的第一行代码增加了一个新的地面图像, 显示在400 x 568 (记住, 图像是按其中心定位的) —— 问题在于我们需要这个平台来横跨游戏的全部宽度, 否则玩家会从侧面掉下来。 要做到这一点, 我们用功能 `setScale(2)` 来缩放 x2 。 现在它已经是800 x 64 大小, 适合我们的需要。 需要给 `refreshBody()` 打电话是因为我们缩放了一个_ static_ 物理体, 所以我们必须告诉物理界我们所做的改变 。

地面被缩小并到位,所以其他平台的时间是:

```js
platforms.create(600, 400, 'ground');
platforms.create(50, 250, 'ground');
platforms.create(750, 220, 'ground');
```

过程与以前完全相同,只是我们不需要对这些平台进行规模化,因为它们已经是合适的大小了.

3个平台被放置在屏幕周围,合适的距离相隔,以便玩家跳跃到它们.

不如我们再加个玩家

# 制作第一个 Phaser 游戏 {#page-title-4}

我们有一些可爱的诱人平台, 但没人可以绕过它们,我们纠正一下

创建一个新的变量,称为 `player`,并在 `create` 函数中添加以下代码。 您可以在 `part5.html` 中看到此代码 :

```js
player = this.physics.add.sprite(100, 450, 'dude');

player.setBounce(0.2);
player.setCollideWorldBounds(true);

this.anims.create({
    key: 'left',
    frames: this.anims.generateFrameNumbers('dude', { start: 0, end: 3 }),
    frameRate: 10,
    repeat: -1
});

this.anims.create({
    key: 'turn',
    frames: [ { key: 'dude', frame: 4 } ],
    frameRate: 20
});

this.anims.create({
    key: 'right',
    frames: this.anims.generateFrameNumbers('dude', { start: 5, end: 8 }),
    frameRate: 10,
    repeat: -1
});
```

这里有两个不同的事物:一个是创建物理学螺旋桨,另一个是创作一些它可以使用的动画.

### 物理斯普莱特 {#physics-sprite}

代码的第一部分创建了图示:

```js
player = this.physics.add.sprite(100, 450, 'dude');

player.setBounce(0.2);
player.setCollideWorldBounds(true);
```

这创造了一个新的名为`player`的图示,定位在游戏底部的100x450像素上,该图示是通过物理游戏对象工厂(`this.physics.add`)创建的,这意味着它默认拥有动态物理体.

创建图案后, 它得到0. 2 的微微反弹值。 这意味着它跳过后着陆时它会跳过如此微小的反弹。 将图案设定为与世界边界相撞。 默认边界位于游戏的外部维度上。 当我们设定游戏为 800 x 600 时, 玩家将无法在这个区域外运行, 将阻止玩家从屏幕边缘上跳过屏幕或跳过顶端 。

### 动画 {#animations}

如果你再看`preload`函数,你会看到“dude”被装入到一个图示工作表,而不是一个图像。这是因为它包含动画框架。这就是完整的图示工作表的长相:

![image](https://cdn.phaser.games/oss-docs/assets/2b245ac6b613a283-dude.png)

共有9帧,4帧用于左跑,1帧用于对面镜头,4帧用于右跑. 注:Phaser支持翻转的图案来保存动画帧,但为了这个教程,我们将保留它老校. 

我们定义了两部动画,叫做“左”和“右”。

```js
this.anims.create({
    key: 'left',
    frames: this.anims.generateFrameNumbers('dude', { start: 0, end: 3 }),
    frameRate: 10,
    repeat: -1
});
```

“ 左” 动画使用帧 0、 1、 2 和 3, 运行时每秒10帧。 “ 重播 1” 值告诉动画循环 。

这是我们的标准运行周期,我们重复它,因为运行方向相反,使用键“右”和最后一个键“转弯”.

**额外信息:** Phaser 3 中的动画管理器是一个全球系统。 其内部创建的动画可以全球范围地提供给所有游戏对象。 它们共享基础动画数据, 同时管理自己的时间。 这样您就可以定义一个单一的动画, 并按需要应用到尽可能多的游戏对象。 这与Phaser 2 不同, 动画专门属于它们创建的游戏对象 。

# 制作第一个 Phaser 游戏 {#page-title-5}

Phaser支持各种不同的物理系统,每个系统都充当任何Phaser场景可用的插件。在撰写时,它与Arcade Physics, Interactive Physicies和 Matter.js Physicsics 一起飞船。 为了这个教程,我们将使用Arcade Phicsics系统来进行我们的游戏,这个系统简单而轻巧,适合移动浏览器。

当物理闪存器被创建时,它会得到一个`body`属性,这是它弧形物理体的参考。这代表了Sparters Arcade物理引擎中作为物理体的星形。天体对象有很多特性和方法,我们可以玩。 

例如,要模拟重力对一个图示的影响,它和写作一样简单:

```js
player.body.setGravityY(300);
```

这是一个任意的值,但逻辑上,值越高,对象感觉越重,下降得越快。如果在代码中添加这个值或者运行 `part5.html`,你会看到玩家不停车就倒下,完全忽略我们之前创造的地面:

![image](https://cdn.phaser.games/oss-docs/assets/162c05e93f424d33-part5.png)

其原因是我们还没有测试地面与玩家的碰撞.

我们已经告诉Phaser,我们的地面和平台将是静止的身体。如果我们不这样做,而是创造动态的身体,那么当玩家与它们碰撞时,它会停止一时,然后一切就会崩溃。这是因为除非另有说明,地面的石块是移动的物理物体,当玩家击中它时,由此产生的碰撞力被应用到地面上,因此,两个身体交换速度,地面也开始下降。

为了让玩家与平台碰撞,我们可以创建一个对撞器对象。这个对象监视两个物理对象(其中可以包括群),并检查它们之间的碰撞或重叠。如果发生碰撞或重叠,它可以选择引用您自己的回调,但为了仅仅与平台碰撞,我们不要求:

```js
this.physics.add.collider(player, platforms);
```

对抗器是执行魔法的。它需要两个对象和测试来进行碰撞,并对他们进行分离。在这种情况下,我们正在给予它玩家星云和平台组。它足够聪明,可以运行碰撞到所有组成员,所以这个呼叫会碰撞到地面和所有平台。结果是一个坚定的平台,不会崩溃:

![image](https://cdn.phaser.games/oss-docs/assets/1fbf40cc32486670-part6.png)

# 制作第一个 Phaser 游戏 {#page-title-6}

拼接是好的, 但我们真的需要玩家移动。 您可能考虑前往文档并搜索如何添加事件倾听器, 但这里没有必要。 Phaser有一个内置的键盘管理器, 使用这个功能的好处之一是:

```js
cursors = this.input.keyboard.createCursorKeys();
```

将光标对象填充为四个属性:上,下,左,右,这些都是关键对象的例。然后我们只需要在我们的`update`环中进行这些调查:

```js
if (cursors.left.isDown)
{
    player.setVelocityX(-160);

    player.anims.play('left', true);
}
else if (cursors.right.isDown)
{
    player.setVelocityX(160);

    player.anims.play('right', true);
}
else
{
    player.setVelocityX(0);

    player.anims.play('turn');
}

if (cursors.up.isDown && player.body.touching.down)
{
    player.setVelocityY(-330);
}
```

虽然我们加了很多代码,但应该都读得很清楚。

首先,它要检查左键是否被扣住。 如果这是负水平速度, 并启动“ 左” 运行动画。 如果他们按住“ 右” , 我们就会完全相反。 通过清除速度并以此方式设置它, 每个框架都会形成“ 停止启动” 运动风格 。

玩家只会在按键被扣下并立即停止时才会移动. Phaser也允许您创建更复杂的动作,具有动力和加速,但这给了我们这个游戏所需的效果. 密钥检查的最后一部分将动画设定为"转动",如果没有按键,则将水平速度设定为零.

### 跳起来 {#jump-to-it}

代码的最后一部分增加了跳跃的能力。 向上光标是跳动键, 如果跳动键下方, 我们测试。 然而, 我们还测试玩家是否在触摸地板, 否则他们在中空跳动 。

如果这两个条件都满足, 我们应用一个垂直速度 330 px/sec sq 。 玩家会因为重力而自动掉到地面上。 随着控制已经到位, 我们可以探索游戏世界。 装入 part7. html 并有游戏。 尝试像 330 那样的调试值, 以显示它将会产生的效果 。

![image](https://cdn.phaser.games/oss-docs/assets/1e411675d5d65fd9-part7.png)

# 制作第一个 Phaser 游戏 {#page-title-7}

是时候给小游戏一个目的了。 让我们把一束星星扔到场景中, 让玩家可以收集它们。 为了实现这一点, 我们将创建一个名为“明星”的新小组, 并加入它。 在我们的创建功能中, 我们添加以下代码( 可以在 `part8.html` 中看到 ):

```js
stars = this.physics.add.group({
    key: 'star',
    repeat: 11,
    setXY: { x: 12, y: 0, stepX: 70 }
});

stars.children.iterate(function (child) {

    child.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8));

});
```

这一过程类似于我们创建平台组时的过程。当我们需要星星移动和反弹时,我们创建了一个动态物理组而不是静态的。

组合可以选择配置对象来帮助其设置。 在这种情况下, 组合配置对象有3个部分: 首先它设置纹理键为星形图像。 这意味着任何由配置对象创建的孩子默认都会被赋予星形纹理。 然后它将重复值设定为11。 因为它会自动创建一个孩子, 重复11次意味着我们总共得到12个, 这正是我们游戏所需要的。

最后一个部分是`setXY`, 用于设定小组创建的12个孩子的位置。 每个孩子将被放置在x: 12, y: 0 , 并有一个x 70 步骤。 这意味着第一个孩子将被放置在 12 x 0 位置, 第二个是 70 像素, 而不是82 x 0, 第三个是 152 x 0, 诸如此类。 “ 步骤” 值是创造过程中一个群体孩子间隔的非常方便的方式。 选择 70 值是因为意味着所有 12 个孩子都会被完全隔开屏幕。

下一个代码将所有的孩子都延展到0.4到0.8之间,并给他们一个随机的Y弹跳值。弹跳范围在0,完全没有弹跳,到1,一个完全弹跳。因为所有恒星都是在Y0重力下产的,它们会拉下来直到它们与平台或地面碰撞。弹跳值意味着它们会再次随机回弹,直到最后安顿下来。

如果我们要像现在这样运行代码, 星星会从游戏底部掉下来, 并且无法看见。 为了阻止这种情况, 我们需要检查它们与平台的碰撞。 我们可以使用另一个对撞器对象来完成此任务 :

```js
this.physics.add.collider(stars, platforms);
```

除了这样做,我们还将检查玩家是否与恒星重叠:

```js
this.physics.add.overlap(player, stars, collectStar, null, this);
```

这让 Phaser 检查玩家和星团中的任何恒星之间的重叠。 如果找到, 它们会被传递到“ collectStar” 函数 :

```js
function collectStar (player, star)
{
    star.disableBody(true, true);
}
```

简单来说, 恒星的物理体被禁用, 而其母游戏对象被非活动化和隐形化, 从而使其无法显示。 运行游戏现在给我们一个玩家, 它可以冲撞、 跳跃、 跳出平台、 收集从上面掉下来的恒星。 对几行希望大多可以读的代码来说, 并不坏 :

![image](https://cdn.phaser.games/oss-docs/assets/eef3b03b6e3a02bb-part8.png)

# 制作第一个 Phaser 游戏 {#page-title-8}

游戏中还有两个最后的触摸:一个是避免可以杀死玩家的敌人,另一个是收集星星时的得分,第一是得分.

为此,我们将使用文字游戏对象。在这里我们创建两个新的变量,一个是实际的分数和文字对象本身:

```js
var score = 0;
var scoreText;
```

`scoreText`在`create`函数中设置:

```js
scoreText = this.add.text(16, 16, 'score: 0', { fontSize: '32px', fill: '#000' });
```

16 x 16 是显示文本的坐标 。 'core: 0' 是显示的默认字符串, 后面的对象包含字体大小和填充颜色。 不指定我们实际使用 Phaser 默认字体, 即 Courier 。

接下来我们需要修改 `collectStar` 函数,以便玩家在拾取恒星时,他们的得分会增加,文本会更新以反映这一点:

```js
function collectStar (player, star)
{
    star.disableBody(true, true);

    score += 10;
    scoreText.setText('Score: ' + score);
}
```

因此每颗恒星都增加了10分, `scoreText` 更新后显示这个新的总数。如果运行 `part9.html`, 将会看到恒星下降, 并且在收集时得分增加。

![image](https://cdn.phaser.games/oss-docs/assets/5a573812b8af955a-part9.png)

最后部分我们再加些坏蛋

# 制作第一个 Phaser 游戏 {#page-title-9}

为了打完我们的比赛,是时候加点坏蛋了。这将会给比赛带来一个很好的挑战,这是以前缺失的。

想法是:当你第一次收集所有恒星时,它会释放弹跳炸弹。炸弹会随机弹跳到关卡周围,如果与它相撞,就会死亡。所有恒星都会重新喷发,这样你就可以再次收集它们,如果收集,它就会释放另一个炸弹。这将给玩家一个挑战:尽可能获得最高分而不死亡。

我们首先需要的就是一组炸弹和几架对撞机:

```js
bombs = this.physics.add.group();

this.physics.add.collider(bombs, platforms);

this.physics.add.collider(player, bombs, hitBomb, null, this);
```

当然炸弹会弹出平台,如果玩家击中它们,我们就会叫`hitBomb`功能。只要停止游戏,让玩家变红:

```js
function hitBomb (player, bomb)
{
    this.physics.pause();

    player.setTint(0xff0000);

    player.anims.play('turn');

    gameOver = true;
}
```

目前为止,很好,但我们需要放炸弹。为了修改`collectStar`功能:

```js
function collectStar (player, star)
{
    star.disableBody(true, true);

    score += 10;
    scoreText.setText('Score: ' + score);

    if (stars.countActive(true) === 0)
    {
        stars.children.iterate(function (child) {

            child.enableBody(true, child.x, 0, true, true);

        });

        var x = (player.x < 400) ? Phaser.Math.Between(400, 800) : Phaser.Math.Between(0, 400);

        var bomb = bombs.create(x, 16, 'bomb');
        bomb.setBounce(1);
        bomb.setCollideWorldBounds(true);
        bomb.setVelocity(Phaser.Math.Between(-200, 200), 20);

    }
}
```

我们使用一个名为`countActive`的群星法来查看有多少恒星还剩在生命中。 如果没有, 那么玩家已经收集了全部恒星, 所以我们利用斜率函数来重新启用所有恒星, 并将其y 位置重新设置为零。 这将让所有恒星再次从屏幕的顶部下降 。

接下来的代码会生成炸弹。首先我们选择一个随机x坐标,总是在屏幕对面给玩家一个机会。然后炸弹被制造出来,它设定与世界碰撞,弹跳,并具有随机的速度。

最终的结果是一个漂亮的小炸弹图案,它会反弹在屏幕周围。小到足够容易避免,在一开始,但一旦数字累积起来,就变得困难得多了!

![image](https://cdn.phaser.games/oss-docs/assets/9f5af5a25441f7a9-part10.png)

游戏完成了

# 制作第一个 Phaser 游戏 {#page-title-10}

您现在已经学会了如何创建具有物理属性的图案,控制其运动,并让它与小游戏世界中的其他对象互动。您还可以做更多的事情来增强这个功能。 为什么不扩展关卡的大小,让相机滚动? 也许可以添加不同的坏蛋类型,不同的价值拾取,或者给玩家一个健康条 。

或者说对于一个非暴力的风格游戏,你可以使它成为快速运行,并简单地挑战他们,以尽快收集星星.

在您在此教程中学到的教训和您可以学习的数百个实例的帮助下,您现在应该为未来的项目打下坚实的基础。 但是,与往常一样,您有问题、需要建议或想要分享您一直在研究的东西,然后在Phaser论坛中可以自由地请求帮助。

---
