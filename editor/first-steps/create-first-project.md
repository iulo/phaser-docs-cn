# 创建第一个项目 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/first-steps/create-first-project)

[Phaser Editor Desktop](/editor/intro/distributions#phaser-editor-desktop)提供了从模板创建新项目的方法.

大部分模板是从互联网下载的,并经常更新,列表中的第一个模板是内置的,可以脱机使用.

每个项目模板都有一个README文件,并附有安装依赖和运行项目的指示.


## 创建项目 {#creating-a-project}

点击 ** 新工程** 按钮:

![Desktop new project.](https://cdn.phaser.io/editor-docs/first-steps-desktop-new-project-1-20240926.webp)

选择项目模板之一。 内建部分提供的模板可脱机使用。 其他项目模板将首次从互联网下载 :

![Select the project template](https://cdn.phaser.io/editor-docs/first-steps-desktop-new-project-2-20240926.webp)

当您选择项目模板时, IDE 打开 OS 文件探索器。 请选择一个空目录( 或创建新目录) , 将复制项目内容。 如果模板从互联网下载, 获取文件可能需要一些时间 :

![Select the project folder.](https://cdn.phaser.io/editor-docs/first-steps-select-project-template-20220415.webp)

如果模板是基于捆绑或前端框架等网络技术, 编辑器会要求您自动安装依赖性。 如果您想在稍后安装这些依赖性, 请选择 ** Discard** 选项。 安装依赖性可能需要几分钟。 在 Windows 机器中, 它应该在“ 黑终端” 窗口中显示安装过程 。

![Install project dependencies](https://cdn.phaser.io/editor-docs/first-steps-install-project-dependencies-20240709.webp)

最后,该项目在IDE中开放:

![Workbench shows the new project](https://cdn.phaser.io/editor-docs/first-steps-new-project-open-ide-20240926.webp)

它显示欢迎页。 您可以点击 ** Open Scene ** 按钮打开项目的任何场景。 另外, 您可以浏览 ** Files ** 视图中的所有工程文件 。

当点击 ** 打开场景** 按钮时, 编辑器会打开 [Go To dialog](/editor/scene-editor/misc#go-to-dialog), 您可以选择打开的场景 :

![Open scene](https://cdn.phaser.io/editor-docs/first-steps-new-project-open-scene-20240926.webp)


## 运行项目 {#running-the-project}

要运行您的项目, 请单击工具栏开头的 ** Play ** 按钮 :

![Play the project.](https://cdn.phaser.io/editor-docs/first-steps-new-play-project-20240926.webp)

Phaser编辑器提供内置的HTTP服务器来运行纯JavaScript项目。然而,大多数项目都基于Webpack, Parcel, 或Vite 等现代网络技术。 在这种情况下, 您应该手动运行一个开发服务器。 如果您不运行开发服务器, 编辑器可能会检测开发服务器没有运行, 并显示一个可选择运行的对话框 :

![Start development server](https://cdn.phaser.io/editor-docs/first-steps-play-game-development-server-dialog-20240709.webp)

如果您点击 **Start Dev Server** 按钮, 编辑器会运行开发服务器, 并随工程运行打开默认浏览器。 浏览器可能在服务器准备好之前打开。 在这种情况下, 您可以手动刷新浏览器 。

启动开发服务器的过程可能需要安装项目依赖性,因此可能需要几分钟时间.


## 节点和国家预防机制 {#node-and-npm}

大多数现代前端网络技术都基于Node.js和NPL.编辑器包含一个用于运行自动任务的NPL和NPL的内部分布. 如果您的项目依赖于一个特定的版本的NPL,你可以在OS终端应用中手动运行所有命令.

---
