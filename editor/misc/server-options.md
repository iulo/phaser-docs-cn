# 服务器选项 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/misc/server-options)

要获得 Phaser 编辑器服务器的完整选项列表, 您可以使用 `--help` 选项。 在此我们详细解释 。

```bash
$ PhaserEditor --help
```

Following,

**- 标志**
:用Phaser.io用户认证并解锁编辑器.

**- 挂断**
: 登录当前 Phaser.io用户会话.

**- 公开**

默认情况下,编辑器会作为一个本地应用程序启动。它允许您执行第三方工具,如 [Visual Studio Code](https://code.visualstudio.com) 或文件管理器,并在启动时自动打开默认的网页浏览器 。

然而,您可能想要在远程机器中执行服务器。 要做到这一点, 您必须使用 `-public` 选项。 当设置时, 服务器允许远程连接, 并禁用远程主机应用程序的所有集成 。

**- 残疾的gzip(英语:**

默认情况下,服务器 gzip 压缩网络发送的文件。 它需要额外的 CPU 使用, 因此, 如果您想要在服务器中使用更少的 CPU , 您可以禁用它 。

**- 无法打开浏览器**

如果您不想打开服务器启动时的默认浏览器。 如果您用 `-public` 选项运行服务器, 则不需要 。

**-浏览器命令**

当服务器启动时, 它打开了 OS 的默认浏览器。 如果您想要启用不同的浏览器, 您可以使用 ** 浏览器命令 ** 选项 :

```bash
$ PhaserEditor -browser-command "/path/to/firefox $URL"
```

在上述命令中,服务器将启动 firefox. 注意 `$URL` 变量被编辑器的URL所取代.

我们建议使用 Google Chrome。 它有一个类似桌面应用程序的运行编辑器的应用程序模式。 尝试像这样运行编辑器 :

```bash
$ PhaserEditor -browser-command '/path/to/google-chrome "--app=$URL"'
```

**- 外部编辑指挥**

当服务器运行在应用程序模式中时, IDE 允许启动外部编辑器。 默认情况下, 它被配置为运行 [Visual Studio Code](https://code.visualstudio.com)( `code`命令) 。

然而,您可以更改命令以启动不同的外部编辑器。例如,如果您想要启动Atom编辑器,而不是[Visual Studio Code](https://code.visualstudio.com),您可以用这些选项运行服务器:

```bash
$ PhaserEditor -external-editor-command '/path/to/atom "$LOC"' -external-editor-name Atom
```

注意`$LOC`变量将扩展至项目位置.

**- 外部编辑名称**

外部编辑器的显示名称。 默认是  ** Visual Studio Code ** 。

**- 编辑字符串**

Phaser编辑器的安装文件夹中,有`editor`文件夹,包含IDE的代码。如果想要装入其他执行的IDE,可以使用`-editor /other/editor/implementation`选项。这可用于测试或开发不同版本的IDE。

**- 密码字符串**

使用此选项解锁编辑器: `-lickey <valid-lic-key>`.

**- 端口输入**

默认情况下,服务器会使用 `1959` 端口进行 HTTP 网络化。 您可以使用此选项来更改它 。

**- 项目字符串**

这是强制的旗帜。 用于设置工程路径 :

```bash
$ PhaserEditor -project /path/to/project
```


## 从文件中获取选项 {#getting-the-options-from-a-file}

您可以总是用同样的选项运行编辑器, 每次每次输入每个选项都可能浪费时间 。

如果是这样, 您可以创建一个脚本( 批次) 来运行编辑器, 并附带所希望的选项。 或者, 您可以更改编辑器安装根部的 `flags.txt` 文件 。

当编辑器开始时, 它会读取 `flags.txt` 文件, 并读取其中提供的选项。 这是配置编辑器的一种方法 。

`flags.txt`文件的格式很简单。每行都包含一个参数。例如,如果您总是想这样运行服务器:

```bash
$ PhaserEditor -public -port 80 -project /path/to/project
```

您可以在 `flags.txt` 文件中写下此内容 :

```bash
-public
-port
80
```

另外,您还可以写空行和注释。注释是从 `#` 字符开始的行 :

```bash
-public

# -port

# 80
```

如果您在Windows机中安装了 Google Chrome, 就可以在文件中写这些行 :

```bash
-browser-command
"C:\Program Files\Google\Chrome\Application\chrome.exe" "--app=$URL"
```

它会在Google Chrome浏览器的一个例子中打开编辑器,但以应用模式进行.

---
