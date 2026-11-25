# 设置 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/workbench/settings)

在本章中,我们将了解Phaser编辑器中的设置UI。

您可以点击主菜单打开设置对话框, 使用 ** 设置** 选项 :

![Settings menu](https://cdn.phaser.games/oss-docs/assets/9e733cb47193c38e-workbench-settings-menu.webp)

设置对话框包含多个选项卡, 设置不同 :

* 默认 Apps 标签
* 键盘标签
* 场景标签

有一些设置是全球存储的, 还有一些是每个项目存储的。 在下面的一节中, 我们详细解释不同的设置存储 。

## 默认 Apps 设置 {#default-apps-settings}

Phaser编辑器可能使用外部应用程序来完成两个主要任务:

* 以浏览器打开游戏.
* 在外部代码编辑器中打开工程.

在此标签中,您可以设置用于这些任务的默认应用程序 。

### 默认系统浏览器 {#default-system-browser}

**浏览器** 部分包含在浏览器中打开游戏的设置.

您可以选择 ** 使用默认系统浏览器** 参数来使用默认系统浏览器, 不管其他参数的值是多少 :

![Use default system browser](https://cdn.phaser.games/oss-docs/assets/13f91411d4a12ffa-workbench-settings-system-browser-proper.webp)

### 自定义浏览器 {#custom-browser}

如果您想要使用特定的浏览器, 您可以将 ** 外部浏览器 ** 参数设置为浏览器可执行路径。 如果引用符( `"`) 之间包含空格, 则必须写入路径 。 这是 macOS 中的路径示例 :

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
```

注,文本字段右侧有一个三点菜单,有以下选项:

* **配置颜色** - 为Google Chrome设定一个预定义的路径.
* **配置 Firefox 工具** - 为Mozilla Firefox设定一个预设路径。
* **配置其它...** - 打开系统文件选择器对话框,以选择浏览器可执行文件。

![Browser executable configuration options](https://cdn.phaser.games/oss-docs/assets/9a28f6dc31f64eb0-workbench-settings-browser-config-option.webp)


使用 ** 外部浏览器参数** 参数,您可以设置参数, 将参数传递给浏览器可执行文件。 最重要的参数是 `$URL`Z 变量, 包含游戏的URL 打开:

![Browser executable arguments](https://cdn.phaser.games/oss-docs/assets/25b261f08522f452-workbench-settings-browser-arg-parameter.webp)

### 自定义代码编辑器 {#custom-code-editor}

在 ** 外部代码编辑器 ** 部分, 您可以设置默认代码编辑器打开工程文件。 设置类似于浏览器设置。 ** 外部代码编辑员** 参数包含编辑器可执行的路径。 如果您引用时包含空格, 您可以在引用( `"`) 之间写入路径。 这是 macOS 中的视觉工作室代码路径的一个例子 :

```
"/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"
```

文本字段右侧有一个三点菜单,有以下选项:

* **配置视觉工作室代码** - 为Visual Studio代码设定一个预定义的路径。
* **配置 JetBrains 网络风暴** - 为JetBraiins WebStorm设定一个预设路径.
* **配置 JetBrains 骑师** - 为JetBrains骑手设定一个预设路径.
* **配置其它...** - 打开系统文件选择器对话框来选择编辑器可执行文件 。

** 外部代码编辑器参数 ** 包含要传递给编辑器可执行的参数。最重要的参数是 `$LOC` 变量,其中包含要打开的文件路径或要打开的项目文件夹。您可以添加附加参数。

**外部代码编辑器显示名称**参数是编辑器的名称,用于在Phaser编辑器的UI的不同位置显示.

![External code editor parameters](https://cdn.phaser.games/oss-docs/assets/7e003b8b623b4404-workbench-settings-external-code-editor-.webp)

## 键盘设置 {#keyboard-settings}

在 ** Keyboard ** 标签中, 您可以设置 Phaser 编辑器中不同命令的键盘快捷键。 设置是全球存储的, 所以所有工程都是一样的 。

标签显示所有命令及其当前快捷键。带有自定义键绑定的命令在列表开头处被突出显示。

![Keyboard settings](https://cdn.phaser.games/oss-docs/assets/44346bee59670b43-workbench-settings-keyboard-tab.webp)

要改变快捷键,请遵循此步骤:

- 选择命令。
- 按下**Edit**按钮。
- 按新键组合键.
- 如果您想要取消更改,请按 **Cancel ** 按钮。

![Edit shortcut](https://cdn.phaser.games/oss-docs/assets/45a178d4e4293b75-workbench-settings-edit-shortcut.webp)

另外,您还可以通过选择命令并按 ** Reset** 按钮来重置命令的键绑定.

## 主题设置 {#theme-settings}

本节显示 [Color Themes available in Phaser Editor](/editor/workbench/color-themes)。 您可以选择工作台使用的主题。 设置为每个工程的全局存储 。

![Color themes](https://cdn.phaser.games/oss-docs/assets/993815900f3037b8-workbench-settings-color-themes-20250317.webp)

## AI 聊天设置 {#ai-chat-settings}

AI Chat 标签包含 Phaser 编辑器的内部聊天器的设置。 您可以设置 API 键, 用于 Google, OpenAI, 和 Anthropic LLM 服务。 键是本地存储在您的机器中, 编辑器直接连接到服务, 而不通过任何第三方服务器 。

这是一个实验性特征,未来可能会有所改变.

![ai settings](https://cdn.phaser.games/oss-docs/assets/792bd3ea571af1b5-settings-ai-tab.webp)

## 编译器设置 {#compiler-settings}

此标签包含场景编译器的设置。 您可以设置以下参数 :

- **Spine 模块名称**: 用于生成代码的 Spine 模块名称。默认情况下,它是 `@esotericsoftware/spine-phaser`。

## 场景设置 {#scene-settings}

在 ** 场景** 标签中, 您可以设置工程中场景的全局设置 :

- **在大纲中显示用户组件**: 场景编辑器的大纲视图中 [show/hide the user components](/editor/scene-editor/user-components/user-components-instancing#browsing-the-user-components-in-a-scene) 的旗帜。
- **Phaser 渲染器类型** : 用于场景的渲染器类型。可用的选项有: WebGL和 Canvas。
- **启用像素艺术**: 启用场景中的像素艺术模式的旗帜。 请选中此选项。 游戏中的此选项是像素艺术 。
- **启用缩略图**: 启用/ 禁用场景缩略图的旗。 制作缩略图是一项昂贵的操作, 这样您就可以禁用它来提高非常大项目的性能 。
- **启动时预装缩略图**: 打开工程时启用/ 取消预装场景缩略图的旗帜。预装缩略图可能很密集, 但启动时需要时间加载, 可能会提高编辑器在操作场景时的性能 。

设置是每个项目存储的, 保存在 `phasereditor2d.config.json` 文件, 因此每个项目都不同。 更多了解 [project's configuration file](/editor/misc/project-config) 。

![Scene settings](https://cdn.phaser.games/oss-docs/assets/b2be21cd648f5d8c-workbench-settings-scene-20251125.webp)

---
