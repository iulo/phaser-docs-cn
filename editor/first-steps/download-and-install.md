# 下载与安装 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/first-steps/download-and-install)

Phaser编辑器是用网络技术建造的。您可以在您的桌面、您的私人网络或云中运行。

我们提供两种不同的发行类型:[Phaser Editor Core](/editor/intro/distributions#phaser-editor-core)和[Phaser Editor Desktop](/editor/intro/distributions#phaser-editor-desktop)。每个发行版本都提供给Windows,macOS和Linux。

[Download Phaser Editor](https://phaser.io/account/downloads)

在本章中,我们论述如何安装两个分布.

## 安装 Phaser 编辑器桌面 {#install-phaser-editor-desktop}

[Phaser Editor Desktop](/editor/intro/distributions#phaser-editor-desktop)发行版将[Phaser Editor Core](/editor/intro/distributions#phaser-editor-core)包装在一个[ElectronJS](https://www.electronjs.org)应用程序中,它的工作就像一个普通的桌面应用程序,并允许打开多个项目和窗口,它也提供了创建新项目的项目模板.

每个平台都有不同安装[Phaser Editor Desktop](/editor/intro/distributions#phaser-editor-desktop)的方法.

### 窗口安装 {#windows-installation}

单击 [downloads page](https://phaser.io/account/downloads) 的 ** Desktop ** 部分中的 ** Windows ** 选项。 它应该开始下载 MSI (微软安装器) 文件。 执行并遵循步骤 。

您可以在 ** Install ** 菜单中按下 ** 配置 ** 选项来配置安装 :

![Windows installer](https://cdn.phaser.io/editor-docs/first-steps-install-windows-20240709.webp)


### macOS 安装 {#macos-installation}

点击 **macOS( Apple silicone) ** 选项下载图像文件。 打开它( 双击) , 将 `Phaser Editor` 图标拖到 `Applications` 文件夹 。

![macOS installer](https://cdn.phaser.io/editor-docs/first-steps-install-desktop-macos-20240709.webp)

注意 macOS 有两台安装器。 一台用于基于ARM的Macs,另一台用于基于Intel的Macs。 基于ARM的Mac是新Macs的M1芯片。 如果您不确定要下载哪个, 您可以下载基于ARM的版本 。

### Linux 安装 {#linux-installation}

我们没有合适的安装器用于Linux,所以我们分发二进制在ZIP文件中.

点击 **Linux ** 选项下载文件并解析。 打开终端并运行 `PhaserEditor` 文件 :

```bash
$ ./PhaserEditor
```

然而,我们建议在桌面和桌面环境创建快捷键和菜单项。为此,执行脚本`install.sh`:

```bash
$ ./install.sh
```

和`uninstall.sh`去除快捷键:

```bash
$ ./uninstall.sh
```

并不会提供`root`权限。

[Phaser Editor Core](/editor/intro/distributions#phaser-editor-core)二进制在`resources/app/server`文件夹中,你可以单独运行.

## 安装 Phaser 编辑器核心 {#install-phaser-editor-core}

Phaser编辑器核心是服务器应用程序,在网页浏览器中为Phaser编辑器IDE服务,是轻量级服务器,为运行云中或桌面中的Phaser编辑器提供必要的服务.

Phaser编辑器 Core作为ZIP文件分发,要下载,请点击[Downloads page](https://phaser.io/account/downloads)中 **Core**部分的平台选项.

解压缩下载文件,打开终端并运行 :

```bash
$ cd /path/to/downloaded/PhaserEditor
$ ./PhaserEditor -project path/to/project
```

服务器在地址中启动并打开默认浏览器:`http://127.0.0.1:1959/editor`.

`-project`旗是强制的,其价值必须是游戏项目的路径.

检查[Create your first project](/editor/first-steps/create-first-project)区创建新游戏.

默认情况下,服务器运行在应用程序模式中。 这意味着它会尽最大努力提供更好的与您的 OS 集成:

* 它打开了右URL的默认浏览器(您可以使用`-browser-command`选项修改).
* 它允许启动第三方OS应用程序,如Visual Studio代码或文件管理器(Windows Explorer,macOS Finder等).
* 它否认远程连接。

然而,您可以使用 `-public` 选项在远程主机中运行服务器 :

```bash
$ ./PhaserEditor -public
```

它允许远程连接,但禁用之前描述的所有OS集成.

[Learn more about all the command line options](/editor/misc/server-options)

---
