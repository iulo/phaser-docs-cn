# 故障排查 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/misc/troubleshooting)

在本节中,我们将研究在使用Phaser编辑器时可能出现的一些最常见的问题,以及如何解决或报告这些问题。

首先,如果您有问题, 请确定您正在使用 Phaser 编辑器的最新版本。 您可以在主菜单中检查新版本, 并使用 ** Check for Updates ** 选项 。

如果问题依然存在,请通过下列渠道与我们联系:

* 给我们写封`support@phaser.io`的邮件
* 联系我们[our Discord server](https://discord.gg/phaser), 在`#phaser-editor`频道:
* 打开与我们整合在应用程序中的聊天的交谈 。

以下是通常要求用户执行的一些操作,以帮助我们诊断和解决问题.

## 配置文件夹 {#configuration-folder}

Phaser编辑器在您的操作系统中创建了配置文件夹。 在此文件夹中, 编辑器存储应用程序日志、 用户首选、 最近的项目等。 这个文件夹名为 `.phasereditor2d`, 位于您的操作系统的用户文件夹 :

```
<user-home>/.phasereditor2d
```

有时删除此文件夹会帮助解决问题.

## 应用程序日志 {#application-logs}

在 [configuration folder](#configuration-folder) 中,您可以找到应用程序的日志。 这些文件是 :

```
server.log
desktop.log
```

如果你有问题,请给我们发这些文件的内容.

## 浏览器日志 {#browser-logs}

Phaser编辑器使用网页浏览器来渲染游戏。浏览器日志对诊断问题很有用。要打开浏览器控制台,请按 `Ctrl+Shift+I`或 `Cmd+Option+I`。在**Console ** 标签中,您可以看到游戏的错误和警告。您可能还要检查**Networks** 标签。

![Open dev logs](https://cdn.phaser.io/editor-docs/troubleshooting-browser-tools-20241011.webp)

## 刷新浏览器 {#refresh-browser}

如果您对编辑器有问题, 如空白屏幕, 或是断开的场景, 请尝试刷新浏览器/ 应用程序。 您可以按 `Ctrl+R`( `Cmd+R`) 来完成 。

## 清除浏览器缓存 {#clear-browser-cache}

有时浏览器缓存会引发问题。您可以通过按下即可清除缓存 `Ctrl+Shift+R` (`Cmd+Shift+R`。或者你可以打开 **DevTools ** (`Ctrl+Shift+I` 或 或 时 间 `Cmd+Option+I`)和勾选 ** 网络** 标签中的 ** 无法缓存** 选项,并刷新页面(`Ctrl+R` 或 或 时 间 `Cmd+R`).

![Disable network cache](https://cdn.phaser.io/editor-docs/troubleshooting-disable-cache-20241011.webp)

## Phaser 编辑器核心 {#phaser-editor-core}

Phaser编辑器核心是编辑器发行,优化后在云中运行.
Phaser编辑器桌面版是传统的桌面应用程序,它建立在Phaser编辑器核心上,但包含桌面应用程序特有的特性。如果桌面版有问题,请从操作系统的命令行中运行核心版。这可能有助于识别桌面版是否有特殊问题。

[In this chapter we show you how to run Core](/editor/first-steps/download-and-install#install-phaser-editor-core)

## 游戏开发服务器 {#game-development-server}

Phaser项目大多使用第三方技术来制作 Phaser 发行。 我们谈论的工具有Vite、 Webpack、 Esbuilt等。 所有这些技术都提供了本地开发服务器, 您必须运行该服务器才能在浏览器中玩游戏。 这是一个常见的问题, 您在运行本地服务器之前尝试运行游戏。 默认情况下, [Phaser Editor detects the need to run the development server and gives you the ability to run it for you](/editor/first-steps/create-first-project#running-the-project)。 但是, 您可能忘记了这一步骤, 所以您应该确认服务器确实在运行。 我们建议您读读您的项目的说明, 通常这些说明会出现在 `README.md`文件 中 。

## 场景编辑器故障 {#scene-editor-troubles}

看看[troubleshooting section of the Scene Editor chapter](/editor/scene-editor/troubleshooting),你觉得怎么样?

---
