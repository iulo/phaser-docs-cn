# 场景间通信 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/scenes/cross-scene-communication)

现在我们知道如何创建和配置Scases, 让我们让他们互相交谈。有几种方法可以实现:直接调用一个函数,为某个事件收听,或通过注册交换数据。我们现在将分别覆盖:

### 调用场景函数 {#calling-a-scene-function}

首先我们先创造两个基本情景:

```js
class SceneA extends Phaser.Scene {

    constructor ()
    {
        super('MyFirstScene');
    }

    preload ()
    {
        this.load.image('asuna', 'assets/sprites/asuna_by_vali233.png');
    }

    create ()
    {
        this.input.on('pointerup', this.clickHandler, this);

        this.add.text(10, 10, 'Click to get image', { font: '16px Courier', fill: '#00ff00' }).setDepth(1000);
    }

    clickHandler ()
    {
        let sceneB = this.scene.get('MySecondScene');

        let position = sceneB.getPosition();

        this.add.image(position.x, position.y, 'asuna');
    }

}

class SceneB extends Phaser.Scene {

    constructor ()
    {
        super('MySecondScene');
    }

    getPosition ()
    {
        let x = Phaser.Math.Between(0, 800);
        let y = Phaser.Math.Between(0, 600);

        return new Phaser.Math.Vector2(x, y);
    }

}
```

此处的 `SceneA` 用于指针事件。 当它收到一个时, 它会叫做 `clickHandler` 方法。 在此我们获取一个 SceneB 的引用。 使用 Scenes 键进行, 即 `MySecondScene` 。 一旦我们得到这个方法, 我们可以调用它所曝光的公开方法。 在这种情况下, 我们调用 `getPosition` 。 这个方法返回一个 vec2 , 并带有随机位置。 然后我们在该位置添加一个图像 。

这并不是一个复杂的例子,但你应该得到这个想法:任何在场景上定义的公开功能都可以被任何其他场景调用.

### 现场事件监听 {#listening-for-scene-events}

以这个例子来说,我们不是直接在SceneB上调用一个功能,而是让它从SceneA那里听事件,设置和以前一样,但我们的clickHandler是不同的:

```js
class SceneA extends Phaser.Scene {

    constructor ()
    {
        super('GameScene');
    }

    preload ()
    {
        this.load.image('bg', 'assets/skies/sky4.png');
        this.load.image('crate', 'assets/sprites/crate.png');
    }

    create ()
    {
        this.add.image(400, 300, 'bg');

        for (let i = 0; i < 64; i++)
        {
            let x = Phaser.Math.Between(0, 800);
            let y = Phaser.Math.Between(0, 600);

            this.add.image(x, y, 'crate').setInteractive();
        }

        this.input.on('gameobjectup', this.clickHandler, this);
    }

    clickHandler (pointer, box)
    {
        //  Disable our box
        box.input.enabled = false;
        box.setVisible(false);

        //  Dispatch a Scene event
        this.events.emit('addScore');
    }

}
```

在这里,当一个框被点击时,我们发送 `addScore` 事件。我们的场景B 看起来像这样:

```js
class SceneB extends Phaser.Scene {

    constructor ()
    {
        super({ key: 'UIScene', active: true });

        this.score = 0;
    }

    create ()
    {
        //  Our Text object to display the Score
        let info = this.add.text(10, 10, 'Score: 0', { font: '48px Arial', fill: '#000000' });

        //  Grab a reference to the Game Scene
        let ourGame = this.scene.get('GameScene');

        //  Listen for events from it
        ourGame.events.on('addScore', function () {

            this.score += 10;

            info.setText('Score: ' + this.score);

        }, this);
    }
}
```

它创建了显示分数的文本对象,获得SceneA的引用,然后从中聆听 `addScore`事件。当它收到一个时,它更新了本地分数和文本对象。

这个方法的优点是SceneA与你的SceneB没有紧密结合,只要事件名称不变,SceneA就可以快乐地坐在那里,只要它喜欢,就发出事件,知道任何其他对事件感兴趣的SceneA都会接过来,然而,这确实意味着SceneB与SceneA是结合的,因为它需要引用它来倾听它的事件发射器,我们可以通过使用游戏注册来完全避免.

### 通过游戏注册交换数据 {#exchange-data-via-the-game-registry}

将略微扩充前一个例子。 这次我们将使用游戏注册, 这是数据管理器插件的一个例子, 以便交换数据。 这是我们的游戏景。 和以前一样, 除了我们把每个盒子都涂上红色。 如果您点击红盒子, 就会失去一个生命。 如果您点击一个普通的盒子, 就会得到一点 :

```js
class SceneA extends Phaser.Scene {

    constructor ()
    {
        super('GameScene');

        this.score = 0;
        this.lives = 6;
    }

    preload ()
    {
        this.load.image('bg', 'assets/skies/sky4.png');
        this.load.image('crate', 'assets/sprites/crate.png');
    }

    create ()
    {
        //  Store the score and lives in the Game Registry
        this.registry.set('score', this.score);
        this.registry.set('lives', this.lives);

        this.add.image(400, 300, 'bg');

        for (let i = 0; i < 64; i++)
        {
            let x = Phaser.Math.Between(0, 800);
            let y = Phaser.Math.Between(0, 600);

            let box = this.add.image(x, y, 'crate').setInteractive();

            if (i % 2)
            {
                box.setTint(0xff0000);
            }
        }

        this.input.on('gameobjectup', this.clickHandler, this);
    }

    clickHandler (pointer, box)
    {
        if (this.lives === 0)
        {
            return;
        }

        //  Disable our box
        box.input.enabled = false;
        box.setVisible(false);

        //  If the box was tinted red, you lose a life
        if (box.tintTopLeft === 255)
        {
            this.lives--;
            this.registry.set('lives', this.lives);
        }
        else
        {
            this.score++;
            this.registry.set('score', this.score);
        }
    }

}
```

当这些框被点击时,我们用`registry.set`呼叫更新了登记册中相应的值。

现在到场景B。这场场景和以前一样,除了我们添加了另一个文本对象来显示剩下的生命:

```js
class SceneB extends Phaser.Scene {

    constructor ()
    {
        super({ key: 'UIScene', active: true });

        this.scoreText;
        this.livesText;
    }

    create ()
    {
        //  Our Text object to display the Score
        this.scoreText = this.add.text(10, 10, 'Score: 0', { font: '32px Arial', fill: '#000000' });
        this.livesText = this.add.text(10, 48, 'Lives: 6', { font: '32px Arial', fill: '#000000' });

        //  Check the Registry and hit our callback every time the 'score' value is updated
        this.registry.events.on('changedata', this.updateData, this);
    }

    updateData (parent, key, data)
    {
        if (key === 'score')
        {
            this.scoreText.setText('Score: ' + data);
        }
        else if (key === 'lives')
        {
            this.livesText.setText('Lives: ' + data);
        }
    }
}
```

它从注册处听出一个 `changedata`事件, 如果它收到一个, 则引用 `updateData` 方法。 此方法设置了 3 个项目: 父, 即数据管理器的拥有者, 此处为游戏。 然后它接收了更改的条目的字符串键, 最后是本条目的新值 。

通过检查键,我们可以分辨是比分还是生命 被改变,并更新我们的文本对象。

如你所见,使用游戏注册 给我们一个完全解开 方法 联系多个幕后。

## 场景更新和渲染 {#scene-updating-and-rendering}

我们提到,游戏拥有真正的全球类——其中两个是渲染器和场景管理器。当游戏步骤时,通常由于浏览器中的请求动画框架更新,它会告诉场景管理器更新。场景管理器负责照顾游戏中的所有场景,它可以添加新的场景,开始和停止,并且从游戏中选择何时更新。

景点存储在景点管理器的列表中。此列表中的景点顺序控制两个重要因素,第一个是它控制了景点的发布顺序,第二个是它控制了景端更新的顺序。

每个游戏步骤, 场景管理器会按_ 逆_ 顺序排列其全部场景, 依次更新其中的每一场景。 它首先检查场景是否活动( 即没有被发送到睡眠或关闭) , 然后告诉场景系统进行更新 。 这反过来会告诉所有场景插件进行更新, 告诉所有游戏对象进行更新 。 本质上, 您的场景所做的与此时渲染无关的一切 。

一旦更新循环完成, 场景管理器将遍历所有场景, 从背面到前, 渲染每个场景。 它通过将一个引用到渲染器到每个场景, 转而交给场景相机管理器处理。 镜头管理器将渲染器并构建场景的视觉显示, 将多个镜头中, 他们可以看到的一切和任何特殊效果都包含在它们身上 。

### 场景列表 {#scene-list}

绘制顺序很重要。 如果您在场景管理器中添加了三个场景, 它会按照它们从后到前的顺序绘制它们, 意思是第一个场景的添加会位于显示器的后面, 而最近添加的场景会画出它的顶部, 在前面。 它像一个标准显示列表一样工作, 可以被控制, 我们在下一节中覆盖。 下面是一个简化的例子, 显示添加多个场景的效果 。

这是我们的第一个场景。它所做的只是画一个长方形,上面有一封信,但它足以证明发生了什么:

```js
class SceneA extends Phaser.Scene {

    constructor ()
    {
        super({ key: 'SceneA', active: true });
    }

    create ()
    {
        let graphics = this.add.graphics();

        graphics.fillStyle(0xff3300, 1);

        graphics.fillRect(100, 200, 600, 300);
        graphics.fillRect(100, 100, 100, 100);

        this.add.text(120, 110, 'A', { font: '96px Courier', fill: '#000000' });
    }
}

let config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    backgroundColor: '#392542',
    parent: 'phaser-example',
    scene: [ SceneA ]
};

let game = new Phaser.Game(config);
```

如果你把代码作为 - 你会看到这一点:

**此处的性能图片**

现在,让我们再加一个场景,它会再次做同样的事情,但颜色不同:

```js
class SceneB extends Phaser.Scene {

    constructor ()
    {
        super({ key: 'SceneB', active: true });
    }

    create ()
    {
        let graphics = this.add.graphics();

        graphics.fillStyle(0xff9933, 1);

        graphics.fillRect(100, 200, 600, 300);
        graphics.fillRect(200, 100, 100, 100);

        this.add.text(220, 110, 'B', { font: '96px Courier', fill: '#000000' });
    }
}
```

我们需要更新游戏配置中的场景阵列,以便在这个新场景中添加:

```js
scene: [ SceneA, SceneB ]
```

结果,正如你所期望的,这个:

**此处的性能图片**

B场出现在A场的顶部,因为它在游戏配置中通过的场景阵列中被添加到第二位。如果换掉这个阵列中的顺序,A场将出现在顶部。

我们再加一个最后场景来完成效果,C场完全和以前一样,我们最后的顺序是这样的:

**此处的性能图片**

因为我们在游戏配置中使用了这个阵列:

```js
scene: [ SceneA, SceneB, SceneC ]
```

将其中的任何元素绕过,你就会影响它们被渲染和更新的顺序。当然,你并不限于在配置中指定景色的顺序。你可以使用景色普鲁金来操纵它们,我们将在一瞬间充分演示。

### 场景列表输入 {#scene-list-input}

您可能想知道为什么场景管理器在更新时会以反序顺序通过场景进行移动 。 原因在于输入。 如果您看上面的图像, 您可以看到我们的UI场景是显示中最顶级的场景, 因为自然我们想要UI 坐在游戏本身的顶级。 但是想象一下您在游戏中有一个交互对象, 如可点击区域, 并且UI 与它重叠。 您几乎总是希望UI 接收输入事件, 而不是交互对象重叠 。 因此, 输入插件有机会先处理显示列表中最顶级的项目_ 和场景列表中最顶级的景 。

默认情况下, 如果场景列表的顶端的场景收到_ 并处理_ 有效的输入请求, 那么下面的所有场景都会跳过它们的输入处理, 以节省时间。 您可以从任何场景调用 `this.input.setGlobalTopOnly(false)`, 改变这个行为 。 之后, 每一个场景都会处理输入, 不论它在场景列表中的位置如何 。

通过按此顺序的延展,我们也能够让UI Scene立即控制游戏场景,例如,你可以有一个暂停图标,点击它就可以让游戏立刻暂停,而不必先等待下一个帧,这只会使游戏感觉更具有响应性.

## 控制场景顺序 {#controlling-scene-order}

场景插件有一系列方法可以让你精确控制场景列表中的幕景顺序,这是至关重要的,因为他们在列表中的位置决定了画的顺序,在创建场景时并不总是能够事先知道场景的顺序,或者哪些场景会同时运行,所以关键在于你可以轻松控制场景的顺序.

值得指出的是,所有与Scenes的交互都应该通过Scene插件完成。每个Scene拥有一个核心插件实例,并且它充当Scene管理器的接口。如果有的话,你应该很少直接访问Scene管理机。如果发现自己在Scene管理程式上调用方法,那么就改变代码,因为它可能存在会随着时间推移而不断增长的结构问题。

简言之,使用`this.scene`和**不**`this.game.scene`。我无法足够地理解这一点。

场景插件有很多可用的方法。 例如, 您可以从场景插件中进行 `this.scene.restart`, 或者说 `this.scene.launch`, 但不能从场景管理器中进行_ not_ 如果您尝试调用一个方法, 它抱怨它不存在, 请重复检查您不会错误地通过 `game` 进入, 并纠正您的处理方式 。

### 移动场景 {#moving-scenes}

用于安排场景列表的主要命令有6个:

```js
bringToTop()
sendToBack()
moveUp()
moveDown()
moveAbove()
moveBelow()
```

您可通过场景插件访问这些方法 :

```js
this.scene.bringToTop();
```

如果您不提供参数, 那么动作会发生在当前场景上, 即您称之为方法的场景。 因此, 上面的代码会尝试将当前场景移到场景列表的顶端( 假设它已经不存在 ) 。

您可以选择提供移动场景 :

```js
this.scene.bringToTop('SceneB');
```

这将尝试将按键 `SceneB` 引用的场景移动到场景列表的顶端。 以及您也可以在对目标场景本身的引用中传递的字符串 。

`moveAbove`和`moveBelow`方法要求您提供目标场景:

```js
this.scene.moveAbove('Game', 'PauseScreen');
```

上面的代码会移动 `PauseScreen` Scene 移动到 Schene 列表中的 `Game` Scene上方。 如果您省略了 2 个参数, 它会尝试移动当前(调用) Scene 移动至 `Game` Scene以上 。

### 场景顺序 {#scene-ordering-demo}

使用这6种方法,你可以构建完整的场景布局。让我们举个例子来证明这一点, 因为这样比阅读更容易看到运行。

粉色盒,就像我们以前的例子一样,都是好的,但是时候把事情调好。我们要用7个镜像来做一个镜像。其中之一将是我们的控制器镜像。这个镜像将容纳您可以用来操纵其他镜像的UI。其他的画面将是独特的图形效果。我们用一套科幻游戏图形来制作一个旋转的星云,一个发光的太阳,一个小行星,一个行星,一个带有排气痕迹的太空船和一些旋转的空间地雷。

用于这个例子的所有代码和资产都可以在Phaser 3 实例重播中找到. 因为有很多代码我只涉及与移动Scenes直接相关的部分,但通过文件挖掘非常值得,以便获得一些关于Phaser 3如何工作的其他方面的想法.

用户界面将允许您选择一个场景, 然后围绕场景列表移动, 切换其活动状态并切换可见度。 其外观如下 :

**此处的性能图片**

左侧的按钮允许您选择一个场景。 亮着光线的是一个当前场景, 名称也显示在 LCD 屏幕上。 在它下面, 您可以看到它目前持有的哪个索引在场景列表中。 在星云场景上方的图像是索引 1, 表示它正右侧渲染。 您可以使用 d- 盘点来调整这个位置。 最后, 右侧的两个切换会显示所选场景的可见和活跃状态 。

这个UI的所有代码都可以在Captain.js文件中找到,这只不过是几个图像和输入事件,但是在事件里你会看到我们从Capain Scene到目标场景的链接.

正如您在UI中看到的, 共有 6 个场景可以选择。 在下面的屏幕镜头中, 您可以看到它们全部一起运行。 点击镜头与示例链接, 以便您可以玩它 :

**此处的性能图片**

通过控制器,你可以重新安排星云。在接下来的星云中,我们把星云全部隐藏起来, 买下太阳,然后让飞船飞到地球后面。

**此处的性能图片**

玩控件并查看源头,直到你对"场景列表"的操作方式有好感.

## 大量外观 {#spawning-multiple-scenes}

事情会变得有点疯狂。到目前为止,我们是在一个类=一个场景的基础上工作的。但是,这不一定是事实。你可以一次又一次地 产生多个场景的版本,如果你想,所有场景都在同一时间运行。

这是基本场景课,叫做`Spawn`:

```js
class Spawn extends Phaser.Scene {

    constructor (handle)
    {
        super(handle);
    }

    create ()
    {
        this.add.image(0, 0, 'phaserRulez');
    }

}
```

与其在游戏配置中添加到场景阵列中,不如在运行时创建实例:

```js
let key = 'Spawn1';
let spawned = new Spawn(key);

this.scene.add(key, spawned, true);
```

我们定义了密钥,创建了新的Spawn类,然后添加到场景管理器(最终的论证告诉场景管理器立即运行).

现在,想象一下,在循环中:

```js
for (let i = 0; i < 10; i++)
{
    let key = 'Spawn' + i;
    let spawned = new Spawn(key);

    this.scene.add(key, spawned, true);
}
```

突然间,你得到了十本《大闪电》的复制品, 你可以用他们的钥匙找到其中任何一个:

```js
let ref = this.scene.get('Spawn5');
```

一旦你找到景物的参考文献,你可以像其他的一样控制它。把它绕到景物列表周围,暂停,隐藏等等.

还有一点我们需要覆盖 在制作演示之前 展示这一切 这就是Scases的制作方式

### 场景渲染 {#scene-rendering}

我们已经详细介绍了 场景列表上的场景顺序 控制它何时产生, 如果它完全产生,它就是可见状态控制。 然而,还有最后一个要素需要考虑:场景的视觉大小。

默认情况下, 新场景将和游戏大小相同。 它会创建自己的相机管理器, 默认相机会被设定为游戏尺寸。 在许多情况下, 但不是全部情况下, 都很好。 您可以通过设定默认相机大小来改变行为 :

```js
class MiniScene extends Phaser.Scene {

    constructor (handle)
    {
        super(handle);
    }

    create ()
    {
        this.cameras.main.setViewport(0, 0, 300, 200);
    }

}
```

上面的代码告诉我们的场景,它有一个300x200像素的相机,并且左上方的位置是0x0。我们现在可以把任何我们喜欢的都添加到场景中:图形,图像,动画,物理,但是它们只能在300x200窗口内渲染。其它的都被剪掉了。

在此代码中,场景是一个固定大小和固定位置,可以简单地移动主相机来移动:

```js
this.cameras.main.setPosition(128, 256);
```

现在场景将在128 x 256 上渲染。 大小仍然为300 x 200 , 我们只改变它所渲染的游戏画布中的位置。 对于场景的位置( 在合理范围内) 没有任何限制, 并且可以随你喜欢的将它们堆放在顶上。

如果你考虑这两点: 斯宾塞可以有一个大小, 而不是游戏画布大小, 你可以把它们定位到任何地方, 你应该开始对可能的东西进行精选。 这让我们能很好地进入到最后的演示。

### 多场演示 {#multi-scene-demo}

为了展示培养多种镜头并把它们绕到画布上的能力,我将创造一个模拟桌面环境, 以我对复古的热爱和借用 [Amiga workbench](https://en.wikipedia.org/wiki/Workbench_(AmigaOS) 来作为灵感来源。 和之前的演示一样, 所有东西都被分割成单一文件, 并且可以在例回波中找到, 这样你就可以随意把它拆分 。

此演示的概念如下:

您将看到一个模拟的 Amiga 桌面, 并带有一个单一的磁盘图标。 点击图标将打开一个包含六个不同的演示的窗口。 点击任何图标都会启动演示。 您可以点击多少次, 只需在屏幕上保留演示的复制件。 您可以拖动任何窗口, 并让窗口在屏幕列表的顶端。 最后, 演示会按浏览器大小运行, 并响应调整大小的事件 。

虽然有重新调整和关闭窗口的控制,但为了简洁起见,我们不会实施。如果你愿意,请随意,请给我一个与演示的链接。 )

六个不同的演示可以推出:

1. **眼睛 双眼** 双眼跟随屏幕的指针,如果你产下一串这些,就会变得非常超现实!
2. **星野( S)** - 经典的演示效果,用闪光画一些星星。
3. **杂耍家** - 循环动画播放的一个例子。
4. **宾** 球在拱廊物理世界里弹跳 视窗大小大小
5. **时钟** - 以你系统时间为基础的真实时钟
6. **入侵者** 使用左/右光标控制飞船, 它会自动开火。 喷出一大堆这些, 你可以同时播放所有游戏 !

最后,这里是每个演示运行的屏幕镜头。单击它打开演示,这样您就可以自己体验到:

**此处的性能图片**

老实说,我很高兴看到这个: )重要的是要记住,每一个打开的小窗口,都像它自己的Phaser游戏实例,与其它一切隔绝.

上面的演示甚至运行在平板电脑上,而且可能还有手机,尽管屏幕会很小。你不能在移动上玩入侵者游戏,但即使这样,也可以在游戏中进行演示,然后拖动它们。在它开始受苦之前,你还能跑多少个。这实在令人惊讶。

如果你看看每个场景的代码, 你会看到它们基本上相当简单。 里面很少你以前不会遇到的。 控制器是负责处理“ 桌面” 和预装所有演示资产的场景。 它做所有的调试工作, 然后在窗口打开时管理窗口。 和Sceneing 演示一样, 控制器除了图像和输入事件之外, 几乎没有其他的, 尽管有一件事情值得更详细地涵盖: 如何将场景拖到周围 。

### 场景拖曳是如何完成的 {#how-the-scene-dragging-is-done}

您可以实现这种效果的方式有很多不同, 但为了这个演示, 我选择了以下方法。 当您点击演示图标, 如“ Juggler” 时, 它会称之为此函数 :

```js
createWindow (func)
{
    var x = Phaser.Math.Between(400, 600);
    var y = Phaser.Math.Between(64, 128);

    var handle = 'window' + this.count++;

    var win = this.add.zone(x, y, func.WIDTH, func.HEIGHT).setInteractive().setOrigin(0);

    var demo = new func(handle, win);

    this.input.setDraggable(win);

    win.on('drag', function (pointer, dragX, dragY) {

        this.x = dragX;
        this.y = dragY;

        demo.refresh()

    });

    this.scene.add(handle, demo, true);
}

this.createWindow(Juggler);
```

我们通过一个我们想要产下的场景类的参考。 然后它会给它分配一个新的密钥( 即 `window7`) , 在控制场景内创建一个 ZZG 对象。 这个区域的位置和大小与刚刚创建的场景相同, 它被设定为交互和可拖动的。 最后, 我们听它拖动事件, 然后在它连接的场景上调用 `refresh`Z 函数。 所有 `refresh` 都叫 Camera setPosition, 并将场景带到顶端 。

区域是非交接游戏对象。 它们没有视觉属性, 也不占用任何渲染时间 - 但你仍然可以让他们互动, 点击或拖动它们, 我们利用这个事实将看不见的区域与我们可见的场景联系起来 。

因为它意味着你可以从任何一点拖动窗口, 不仅仅是像真正的OS一样从标题栏拖动窗口, 也很容易改变, 只需给区一个较小的高度。 或者, 你可以让Scene处理输入事件本身, 从那里拖动它, 但我喜欢这个方法的简单, 所以把它保存在这个演示中。 记住, 很少有一种方法可以剥猫皮 。

我希望你已经知道 斯皮斯能做什么,如何工作,如何用视觉来操纵它们。如前所述,所有代码都可以在回波中找到,并将与Phaser 3.7.0及以上操作.

---
