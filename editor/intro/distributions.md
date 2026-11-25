# 发行版本 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/intro/distributions)

Phaser编辑器作为两种不同的产品分布:

这两种产品都可供Linux,Windows,和macOS使用.

为什么有两种不同的产品?

当开发HTML5游戏时,使用Phaser,需要熟悉两个技术堆栈:游戏开发工具和网络开发工具.

游戏开发工具是最重要的工具(它包括地图编辑器,纹理包,动画工具),但是,在制作专业游戏时,建议在您的工作流程中添加一个现代的网络开发技术堆栈,例如TypeScript等静态型编码语言,[NPM](https://www.npmjs.com)等软件包管理工具,[WebpackJS](https://webpack.js.org)等网络捆绑工具.

可能来自主流游戏开发界的开发者,并不熟悉网页开发堆栈,并且将Phaser编辑器作为团结编辑器,Godot,Construction等主流编辑器的替代物. .

对这些用户来说,有[Phaser Editor Desktop](/editor/intro/distributions#phaser-editor-desktop)产品。它将[Phaser Editor Core](/editor/intro/distributions#phaser-editor-core)(编辑器的服务器和客户端)包裹在一个[ElectronJS](https://www.electronjs.org)的应用软件中,并提供类似于传统IDE的经验:项目模板,以及更深入地融入本地操作系统。

另一方面,还有[Phaser Editor Core](/editor/intro/distributions#phaser-editor-core),它包含了编辑器的服务器和客户端,其架构可以更好地与网络开发工具集成.

现代网络开发正在向云端移动,使用[Gitpod](https://gitpod.io)和[GitHub Codespaces](https://github.com/codespaces)等平台. [Phaser Editor Core](/editor/intro/distributions#phaser-editor-core)允许在这些基于云端的开发环境中使用编辑器.

## Phaser 编辑器核心 {#phaser-editor-core}

电话 [Phaser Editor Core](/editor/intro/distributions#phaser-editor-core) 分布是微小的,集中的分布 Phaser 编辑.

它之所以很小,是因为它只包括编辑器的服务器和客户端,并且只提供Phaser游戏开发工具(尤其是Scene编辑器插件),将代码编辑等第三方工具问题委托给第三方.

微小并不意味着它缺少什么,而是它专注于困难的问题:设计Phaser场景。 它允许在不同情景中整合编辑器,比如在本地桌面或基于云的远程环境中开发(让我们说[Gitpod](https://gitpod.io)或[GitHub Codespaces](https://github.com/codespaces) ) 。

您可以在 Docker 文件 中添加 [Phaser Editor Core](/editor/intro/distributions#phaser-editor-core), 将其作为对节点包的依赖, 或者只是下载并执行您的 OS 。

## Phaser 编辑器桌面 {#phaser-editor-desktop}

[Phaser Editor Desktop](/editor/intro/distributions#phaser-editor-desktop)发行将[Phaser Editor Core](/editor/intro/distributions#phaser-editor-core)的发行包装在一个[ElectronJS](https://www.electronjs.org)的app中,增加了更多的特性,并与操作系统融合.

如果你们不熟悉网络开发工具(TypeScript、[NPM](https://www.npmjs.com)、[WebpackJS](https://webpack.js.org)),我们建议你们分发此文件。

分发情况如下:

* Phaser编辑器的安装器.
* 打开创建项目的起始页( C) 。
* 为所有现代捆绑者和前端框架配置了多个项目模板。 包括一些实例游戏 。
* 一个安装和运行本地开发服务器的内部节点分布.

开始页面, 项目列表 :

![Recent projects.](https://cdn.phaser.io/editor-docs/intro-desktop-start-page-20240711.webp)

开始页面, 项目模板 :

![Select project template](https://cdn.phaser.io/editor-docs/first-steps-desktop-new-project-2-20240711.webp)

---
