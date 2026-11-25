# 在 Phaser Editor 中编写代码 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/code-editor/intro)

Phaser编辑器主要专注于提供设计工具,可以使用高级第三方编辑器来编码游戏.

您可以使用任意的编码编辑器, 但我们推荐 [Visual Studio Code](https://code.visualstudio.com)。 实际上, IDE 生成的工程与该编辑器完全兼容, 并包含配置文件 。

然而,我们把基本的代码编辑器包含在Phaser编辑器内,这样你就可以对代码进行快速的预览或修改.

这些编辑器基于 [Monaco editor](https://microsoft.github.io/monaco-editor/), 并具有相当数量的功能, 特别是用于 JavaScript 开发。 如果您使用高级工具链来编码您的游戏, 如使用捆绑器, 我们强烈建议您使用 Visual Studio 代码 。

Phaser编辑器运行在桌面或云中,您可以在两种环境中找到卓越的代码编辑器。尤其是基于Visual Studio代码的编辑器。学习Phaser编辑器如何在下一节中与Visual Stopio代码融合。

## 视觉工作室代码兼容性 {#visual-studio-code-compatibility}

[Visual Studio Code](https://code.visualstudio.com)编辑器是写作Phaser编辑器游戏代码的首席主管,第一,t极受欢迎,威力极强,第二,使Phaser编辑器创建的项目包含[Visual Studio Code](https://code.visualstudio.com)所需的文件,以提供Phaser的良好编码经验.

### 项目结构 {#project-structure}

JavaScript项目模板包括这些文件:

![JavaScript project.](https://cdn.phaser.io/editor-docs/code-editor-vscode-js-05012020.webp)
1. 文档 `lib/phaser.js`。这是 Phaser 运行时间 。
2. Phaser类型定义文件:`types/phaser.d.ts`和`types/matter.d.ts`。这些文件由Phaser提供,由[Visual Studio Code](https://code.visualstudio.com)用来“理解”[Phaser API](https://phaser.io/oss/docs/docs/latest.md)。
3. [project configuration](https://code.visualstudio.com/docs/languages/jsconfig)文件: `jsconfig.json`。如果是 TypeScript项目,则包括 [tsconfig.json file](https://www.typescriptlang.org/docs/handbook/tsconfig-json) ,而不是 `jsconfig.json` 。

### 代码服务器 {#code-server}

如果您正在使用 Phaser 编辑器的远程实例, 您可以尝试 [Code Server](https://github.com/cdr/code-server/)。 它允许在同一 Phaser 编辑器服务器上运行 VS 代码, 并编辑本地浏览器中的游戏代码 。

另外,您还可以使用 GitHub 代码空间或 Gitpod 等云服务。在这两种情况下,您都可以安装 Phaser编辑器 Core 作为项目依赖,并同时运行 VS 代码 。


### 视觉工作室代码 & Phaser 编辑器集成 {#visual-studio-code-phaser-editor-integration}

您可以从 Phaser 编辑器中启动 Visual Studio 代码。 命令是 ** Open Visual Standio 代码 ** `(Ctrl+Alt+U)`。 这是一个智能命令, 因此它除了打开 Visual Startio 代码的项目之外, 还可以找到正确的文件, 打开 Visual studio 代码 。

如果 Phaser 编辑器中的文件是场景,它会打开场景的源文件。如果当前文件是用户组件编辑器,它会打开选中组件的源文件 。

此命令对于快速导航设计工具和代码编辑器至关重要。 您可以从主工具栏中触发它 :

![Open Vs Code button](https://cdn.phaser.io/editor-docs/code-editor-vscode-button-20240918.webp)

---
