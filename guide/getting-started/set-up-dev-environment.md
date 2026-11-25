# 配置开发环境 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/getting-started/set-up-dev-environment)

在此教程中, 我们将覆盖一个开发环境, 您可以在此建立您的 Phaser 游戏。 这将包括运行本地网络服务器, 选择一个 IDE, 获取最新的 Phaser 版本, 并检查所有操作。

如果你相信我们,你*do* 需要本地的网络服务器来开发,那么你可以跳过下面的解释和[head directly to part 2](#installing-a-web-server).

如果你想知道为什么,请阅读...

### 网络服务器? {#a-web-server-but-i-want-to-make-games}

<blockquote><q>Why do I need a local web server? Can't I just drag the html files onto my browser?</q><cite>A. Sane, Developer</cite></blockquote>

现在不是, 不。 我很感激这有点混乱, 有时甚至是矛盾的, 但是这一切都归结为浏览器安全。 如果您正在制作一个静态的 html 网页, 那么您可以愉快地将这个文件拖入浏览器并查看最终结果。 您也可以在当地“ 保存如” 整个网页, 并重新打开它们, 并且大部分内容都完好无损。 如果这两种东西都有效, 为什么您不能将 HTML5 游戏拖入浏览器并运行它 ?

与访问文件所用的协议有关。 当你在网络上请求任何您正在使用 `http` 的文件时, 服务器级别的安全性足以确保您只能访问您想要访问的文件。 但是, 当你拖动文件时, 它通过本地文件系统( 技术上是 `file://`) 被大量限制, 原因很明显。 `file://` 下没有域的概念, 没有服务器级别安全, 只是一个原始文件系统。 如果 JavaScript 在 `file://` 下运行时有自由统治, 就不会有任何东西阻止它装入 几乎* 任何* 文件, 并且发送给谁知道在哪里的文件 。

因为这样在 `file://` 下运行时,浏览器会把自己锁起来。 每个页面都会被当作一个独特的本地域。 这就是为什么“保存网页”在某种程度上起作用。 它在相同的跨站点限制下打开, 仿佛它们是在一个现场服务器上。

有关这个,[Chromium blog](http://blog.chromium.org/2008/12/security-in-depth-local-web-pages.html)上有一个详细的文章,如果你想多学点,那就值得一读.

您的游戏需要加载资源: 图像、 音频文件、 JSON 数据, 可能还有其他的 JavaScript 文件。 为了做到这一点, 它需要不受浏览器安全枷锁的干扰地运行。 它需要 `http://` 访问游戏文件。 为此我们需要一个网络服务器 。

## 安装网络服务器 {#installing-a-web-server}

### 窗口 {#windows}

在Windows上,有许多“捆绑安装器”可用,这些设备可以一起包装,并从一个单exe中设置Apache、PHP和MySQL等流行的网络技术。

我们推荐 [WAMP.Net](https://wamp.net/)。 它有一个简单的设置指南, 在您的系统磁盘中安装一个图标, 您可以从中停止并重新启动服务, 以及修改 Apache 或 Nginx 设置, 让创建新站点成为微风, 包括 SSL 证书 。

Cesanta 提供 [Mongoose web server](https://cesanta.com/binary.html)。 这是一个非常小的应用程序,不需要安装,也可以作为单个exe文件运行。 没有SSI和WebDAV(不需要HTML5游戏)等所有附加捆绑,exe的大小就是一个微不足道的45KB,甚至完全被显示的版本也只有355KB。

而不是“ 全部在一” 解决方案中, 您也可以自行下载一个网络服务器。 [Microsoft IIS](http://www.iis.net) 和 [Apache](http://httpd.apache.org) 都可以免费下载 。

### macOS {#macos}

作为Unix环境的核心,macOS上有更多的选项比Windows更可用。但是如果你想要像WAMP那样的“全部”方法,一个干净而容易使用的界面,那么我们强烈推荐[MAMP](http://www.mamp.info/en/index.html)。这有两个版本:一个免费,一个付费。

当然,还有手动设置本地网络服务器的指南, 如 [this guide written for Mountain Lion](https://discussions.apple.com/docs/DOC-3083)。 选择您最满意的任意一个方法 。

### 带有 Python 的简单 HTTP 服务器 {#simple-http-server-with-python}

如果您需要快速运行的网络服务器, 并且您不想乱设置 Apache 或下载一个应用程序, Python 就可以帮助。 Python 带有一个简单的内置的 HTTP 服务器, 它可以服务任何本地文件夹中的文件。 自然, 您需要安装的只是 Python 。 [Read the full guide here](http://www.linuxjournal.com/content/tech-tip-really-simple-http-server-python)

### 节点的 http-server.js 服务器 {#http-server-for-nodejs}

*http-server * 是简单零配置命令行 http 服务器 [node.js](http://nodejs.org)。它足够强大,可用于生产,但简单且可以黑客化,足以用于测试、本地开发和学习。或者,正如网站所说的,“服务像被绑在火箭上的龟一样的静态文件”。 npm 和指示 [http-server web site](https://npmjs.org/package/http-server)

### php 内置网络服务器 {#php-built-in-web-server}

截至 PHP 5. 4.0, CLI SAPI 提供了内置的网络服务器, 它只真正适合开发目的, 并按顺序服务所有文件, 但可以轻松地测试 HTML5 游戏。 它从一个命令行呼叫中被引用, 您可以在这里找到如何做到这一点的细节 [in the PHP Manual](http://php.net/manual/en/features.commandline.webserver.php) 。

无论你做什么,都很重要, 拥有在当地服务文件的能力。你已经准备好选择一个编辑了。

--------------------------------

## 选择编辑器 {#choosing-an-editor}

您需要编辑器来准备您的 JavaScript 代码。 有许多* 可用, 每一个都有自己的优点和缺点。 如果您是有经验的开发者, 您可能已经拥有自己的首选编辑器, 在这种情况下, 继续使用本指南的第四部分。 否则您可以选择:

### 视觉工作室代码 {#visual-studio-code}

这是用于构建框架和所有工程的 Phaser 团队的编辑器。 甚至这个指南的编辑器也被写入其中 。 

Visual Studio Code 是一款轻量级但强大的源代码编辑器,运行在您的桌面上,可用于Windows,macOS和Linux. 它与内置支持的JavaScript,TypeScript和Node.js并具有丰富的其他语言(如C++,C#,Java,Python,PHP,Go)和运行时的扩展生态系统(如.NET和Unity).

访问[VS Code](https://code.visualstudio.com/)网站.

### 下标文本 {#sublime-text}

低音应该被认为是一个极其强大的文本编辑器,而不是一个IDE.

诸如“Goto”任何东西的能力, 分块编辑,多光标, 分散式自由模式和强大的插件负荷等功能, 使得这个编辑器成为了我们用过最快和最多功能的编辑器。 并且,它能够用在十年的开发中。

使用其全面的软件包系统,您可以通过多种方式增强它。 这里有一个用于Sublime的特性和软件包的 [excellent guide](http://scotch.io/bar-talk/best-of-sublime-text-3-features-plugins-and-settings) 。

完整版本成本70美元,但每分钱都值钱,可供Windows,OS X和Linux使用.

访问[Sublime Text](http://www.sublimetext.com)网站.

### 网络结构 {#webstorm}

JetBraiens WebStorm是一个极其先进的全开发环境,它远远超出了简单的代码编辑,提供了您期望从一个合适的IDE中可以实现的所有高级功能. 包括代码透视,npm内置,代码风格和语法报告,源控和丰富的其他功能. 有很多功能是为网页开发者设计的,而不是游戏开发者,但依然可以随意地拥有.

它基于一个基于Java的庞大编辑器IntelliJ EIDEA, 既好又坏。 首先, 实际代码编辑体验不像Sublime那样平滑和自由, 非标准OS集成也很弱。 但权力特性往往可以弥补这一点。 在你测试游戏之前, 发现代码时有错误, 可能真的有用。 而代码完成也很好, 尽管显然受到JavaScript 的众多写法的限制。

完整版本从49美元开始,可供Windows和OS X使用. 经常在JetBraiins网站找到交易.

访问[JetBrains WebStorm](http://www.jetbrains.com/webstorm/)网站.

--------------------------------

## 正在下载 Phaser {#downloading-phaser}

Phaser 现作为《京都议定书》 JavaScript 。可以下载、链接到内容传送网络,也可以通过任何标准安装 JavaScript 软件包管理器,例如 npm. Phaser 不是一个桌面应用程序。您没有“ 安装” , 没有“ ”Phaser IDE',这是个 JavaScript 对话框,您将它包含在自己的网页中,或者捆绑。然后将游戏代码写入 JavaScript 并用浏览器一起运行。

Phaser是一个开放源代码项目,可以免费下载。使用Phaser时,无论您是用于商业还是免费项目,都无需付费。我们使用GitHub管理项目,您有各种选择,可以下载。这些在[download page](https://phaser.io/download/stable)上都有解释。

### 我能拿个拉链文件吗? {#can-i-just-get-a-ziptar-file}

> 通过克隆寄存器、抓Js文件或下载所有文件作为拉链来获取 Phaser

是的, GitHub 提供了将整个寄存器作为zip或tar文件下载的选项。 但是, 我们强烈建议您学会使用 git 。 它将使您在发布时能够轻松更新到最新的 Phaser 版本。 如果您希望及时为 Phaser 提供代码, 这样做会更容易。

如果你不想通过命令线学习使用git, 你可以使用一些伟大的应用程序。我们推荐 [SmartGIT](http://www.syntevo.com/smartgithg/) 窗口或窗口 [Git Tower](http://www.git-tower.com) 打开 macOS.

--------------------------------

## 环球你好! {#hello-world}

有了你的编辑器设置, 网络服务器安装和Phaser下载 是时候创建一些东西 检查所有的东西都起作用了。

您需要发现您的“ web root” 在您的机器上。 这是服务器查找文件的文件夹。 如果您在 Windows 上使用 WAMP , 您可以点击系统磁盘中的 WAMP 图标来定位它, 从弹出菜单中选择“ www 目录 ” 。 其他服务器将拥有确定位置的其他方法, 但从这里起, 我们将称之为“ webroot ” 。

在 Webroot 内部创建一个名为 `index.html` 的文件,并将以下代码粘贴到其中:

```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/phaser@3.85.2/dist/phaser-arcade-physics.min.js"></script>
</head>
<body>

    <script>
    class Example extends Phaser.Scene
    {
        preload ()
        {
            this.load.setBaseURL('https://cdn.phaserfiles.com/v385');

            this.load.image('sky', 'assets/skies/space3.png');
            this.load.image('logo', 'assets/sprites/phaser3-logo.png');
            this.load.image('red', 'assets/particles/red.png');
        }

        create ()
        {
            this.add.image(400, 300, 'sky');

            const particles = this.add.particles(0, 0, 'red', {
                speed: 100,
                scale: { start: 1, end: 0 },
                blendMode: 'ADD'
            });

            const logo = this.physics.add.image(400, 100, 'logo');

            logo.setVelocity(100, 200);
            logo.setBounce(1, 1);
            logo.setCollideWorldBounds(true);

            particles.startFollow(logo);
        }
    }

    const config = {
        type: Phaser.AUTO,
        width: 800,
        height: 600,
        scene: Example,
        physics: {
            default: 'arcade',
            arcade: {
                gravity: { y: 200 }
            }
        }
    };

    const game = new Phaser.Game(config);
    </script>

</body>
</html>
```

### 测试,测试... {#testing-testing}

打开您的网页浏览器, 将 `index.html` 页面加载。 这可能和在 `localhost/` 或 `127.0.0.1/` 中输入您的浏览器一样简单。 或者您还需要指定一个端口号码, 这完全取决于您使用的服务器设置方法 。

如果一切顺利, 将在浏览器中显示以下演示:

![Phaser 3 Demo](https://cdn.phaser.games/oss-docs/assets/bfe6cb4bd0ae9953-sample1.png)

如果它不为任何原因需要调试控制台并查看输出出错。 在大多数浏览器中, 您可以按下 `F12` 来完成此操作。 这在 Chrome, Firefox 和 Internet Explorer 11. 请检查错误是什么, 希望它像文件丢失一样简单, 这样可以检查您的文件夹名称并刷新页面 。

如果有更复杂的事情 请加入我们的[Phaser Discord](https://phaser.io/community/discord) 和我们的初学者频道,我们尽力帮忙

这只是个小例子,我们有[hundreds more](https://phaser.io/examples)给你探索,但希望它能显示Phaser的表达和快速使用,只要几行容易读的代码,屏幕上就可以看到相当令人印象深刻的东西!

## Phaser 示例 {#phaser-examples}

从我们发布第一个版本的Phaser开始,我们就知道人们学习如何使用它的最佳方法之一是产生实例。所以我们开始创造许多不同的实例,涵盖Phaser的所有关键领域。从如何设置动画到如何使用物理。

### 在线 Phaser 示例 {#online-phaser-examples}

您可以浏览此网站的所有 [Phaser Examples](https://phaser.io/examples) 。 您也会找到一个活代码编辑器, 这样您就可以修改源代码并实时重运行, 以立即看到修改 。

### 在 Phaser 教程中进行游戏 {#making-a-game-in-phaser-tutorial}

现在你们都准备好了 我们强烈推荐你们通过[Making a Game in Phaser 3](https://phaser.io/tutorials/making-your-first-phaser-3-game)的指南工作。从这个指南中,你们将学会如何构建一个游戏, 让你能够控制一个可以跳出平台和收集项目的人物。

## 下一步 {#next-steps}

您使用 Phaser 的游戏开发体验开始于这里! 尽管我们只触及了基本内容,但如果你通过这个指南,现在可以完全工作开发环境,访问API docs和上百个实例.

即便如此,我们最好还是把这个社区编成一个社区的一部分。我们也不能建议我们这个论坛足够多。在过去几个月里,它已经从实力到力量,而且你肯定在最需要的时候会找到帮助和支持。

向别人发泄想法,在聊天室闲逛,浏览游戏展示,参与其中!

[Join the Forum](https://phaser.io/community/forum) 或 或 时 间 [Chat on Discord](https://discord.gg/phaser)

### 贡献 {#contribute}

您可以帮助构建 Phaser 生长方式。 如果您发现错误, 请报告它。 它不会花费很长时间, 到目前为止我们已经解决了91%以上的已报告问题( 而我们还在研究另外9% ) 。 您也可以针对开发分支发布 Pull 请求, 或者发布您自己的插件或过滤器 。

[Report Issues on GitHub](https://github.com/phaserjs/phaser/issues/new)

### 给我们看你的游戏! {#show-us-your-games}

我们花了许多时间 努力工作 Phaser 我们理解它不会是每个人的完美,我们对此也很酷。但是如果你使用它并做一些东西,无论你认为它有多小,请告诉我们。当人们向我们展示他们一直在玩的游戏时,你不会相信这是多么的激励性。通过推特在论坛上向我们伸出手来(掌声)[@phaser_](https://twitter.com/phaser_))或由 [email](mailto:support@phaser.io).

不过我们真心希望你玩得开心

---
