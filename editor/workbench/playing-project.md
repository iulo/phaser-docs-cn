# 运行项目 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/workbench/playing-project)

要在 Phaser 编辑器中运行游戏,只需点击编辑器左上方工具栏的**Play**按钮,或按 `F12`:

![Play button](https://cdn.phaser.io/editor-docs/run-editor-toolbar-20241004.webp)

此动作在网页浏览器中打开编辑器并运行游戏。 然而, 有些复杂之处需要我们处理 。

Phaser开发的游戏基于网络技术,这意味着游戏需要两个部分来运行:一个网络服务器和一个网页浏览器. 网络在服务器和客户端都有各种各样的开发工具和技术. 您的Phaser游戏是网络游戏,也可以使用所有这些工具,如流行的前端框架 React,Angular,以及其他许多工具.

然而,Phaser编辑器提供了一个足以运行最基本的项目的网络服务器,这些基于**Basic JavaScript**模板,或任何其他静态内容项目.

如果您的项目是用任何使用 Webpack, Vite, ESBuild 等网络捆绑器的模板创建的, 那么编辑器将会发现, 在运行游戏之前, 它必须运行这些第三方工具提供的本地网络服务器 。

通常这些本地服务器是通过像`npm start`或`npm run dev`这样的命令运行的。为此,编辑器打开窗口,为您运行命令:

![Start dev server](https://cdn.phaser.io/editor-docs/first-steps-play-game-development-server-dialog-20240709.webp)

如果您想要从另一个应用程序,如VSCode或您的系统终端,手动运行网页服务器,那么您可以点击 ** Skip** 按钮。如果您想要 Phaser编辑器为您运行网页服务器,请点击 **Start Dev Server** 按钮。

## 故障排查 {#troubleshooting}

正如我解释的那样,运行游戏可能涉及几个步骤,但编辑器可以自动为您完成这些步骤,但是,它们有可能失败或者你忽略了它们。为此原因,有时游戏不会运行,浏览器会显示一个“找不到页”消息。在这种情况下,您应该检查游戏的网络服务器是否运行。由于有如此多的网络技术和Phaser项目模板,我们建议您阅读每个项目根部中存在的`README.md`文件。您将在该文件中找到运行游戏网络服务器的适当指令 。

## 在内部窗口中玩游戏 {#play-the-game-in-an-internal-window}

默认情况下,单击 **Play** 按钮时,编辑器会打开系统浏览器并运行游戏。您也可以在编辑器内,内部窗口中直接运行游戏。要做到这一点,您必须单击 [**Quick Play Project** command](/editor/workbench/command-palette)z或按 `F10`z 。

![play game dialog](https://cdn.phaser.games/oss-docs/assets/e42a11aa1b5a1cdc-play-project-internal-window-20251125.webp)

对话框显示以下选项 :

- **刷新( E)**: 重新在内部窗口中装入游戏。
- **在新标签中打开**: 在系统浏览器的新标签 - 或窗口中打开游戏。
- **取消( E)**: 关闭对话框。 您可以按下 `ESC` 键来关闭它 。

如果在游戏运行时项目被更改,对话框会自动重新装入游戏以反映变化.

---
