# Phaser Editor v5 手册 {#page-title}

Phaser Editor v5 · [英文原文](https://www.phaser.io/oss/docs/phaser-editor/)

Phaser Editor 是为 Phaser 2D 游戏开发设计的工具。手册介绍如何从模板创建项目、管理资源、搭建场景、制作动画和编辑代码。

![Phaser Editor 界面](https://cdn.phaser.io/editor-docs/welcome-20241005.webp)

## 为什么使用 Phaser Editor？ {#why-phaser-editor}

编辑器把 Phaser 项目的常用工具集成在一起，减少项目配置和资源管理的手工工作。可以用它创建新项目，也可以迁移已有的 Phaser 项目。

## 主要功能 {#main-features}

### 资源包编辑器 {#asset-pack-editor}

[资源包编辑器](/editor/asset-pack-editor/intro)可以将图像、音频等资源导入[资源包文件](/editor/asset-pack-editor/asset-pack-file)。资源包是 Phaser 原生支持的格式，场景编辑器和 Phaser 代码都可以使用。通过可视化导入资源，可以减少手写加载代码。

![资源包编辑器](https://cdn.phaser.io/editor-docs/asset-pack-editor-overview-20241005.webp)

### 场景编辑器 {#scene-editor}

[场景编辑器](/editor/scene-editor/intro)可以通过在画布上摆放图像和其他游戏对象来创建场景。预制体、用户组件和脚本节点用于复用对象、配置和行为。编辑器还支持 [Spine](https://esotericsoftware.com) 动画和 [Tiled](https://www.mapeditor.org) 地图。

- [游戏对象](/editor/scene-editor/game-objects)，包括图像、精灵、九宫格、位图文本和图层
- [精灵动画](/editor/scene-editor/sprite-animations)与 [Spine 动画](/editor/scene-editor/spine-animations)
- [瓦片地图](/editor/scene-editor/game-objects/editable-tilemap-object)
- [Arcade 物理](/editor/scene-editor/arcade-physics)与[滤镜](/editor/scene-editor/filters)
- [粒子发射器](/editor/scene-editor/game-objects/particle-emitter-object)
- [预制体](/editor/scene-editor/prefabs)、[用户组件](/editor/scene-editor/user-components)和[脚本节点](/editor/scene-editor/script-node)
- [布局工具](/editor/scene-editor/layout-tools)

场景编辑器使用自己的场景文件格式，并生成 Phaser 代码。可以查看生成的代码，在内置编辑器或 [Visual Studio Code](https://code.visualstudio.com) 等外部编辑器中修改。

![场景编辑器](https://cdn.phaser.io/editor-docs/welcome-scene-editor-overview-20241005.webp)

### 动画编辑器 {#animations-editor}

[动画编辑器](/editor/animations-editor/intro)用于创建精灵动画。它生成的 JSON 文件可通过 [Phaser Loader API](/api/class/loader-loaderplugin#animation)或资源包加载。也可以[自动生成动画](/editor/animations-editor/auto-build-animations)。

![动画编辑器](https://cdn.phaser.io/editor-docs/welcome-animations-editor-overview.webp)

### 代码编辑器 {#code-editor}

Phaser Editor 内置基于 [Monaco Editor](https://microsoft.github.io/monaco-editor/) 的[代码编辑器](/editor/code-editor/intro)，支持编辑 JavaScript、TypeScript、HTML、CSS 和 JSON，并提供跨文件自动补全、代码大纲和文档提示，便于制作原型。需要更完整的编码功能时，可以使用 Visual Studio Code。项目模板包含所需的编辑器配置与类型文件。

![代码编辑器](https://cdn.phaser.io/editor-docs/welcome-code-editor-20241005.webp)

### 项目模板 {#project-templates}

Phaser 项目可以按自己的方式组织和构建。Phaser Editor 提供[项目模板](/editor/first-steps/create-first-project)，可以用它生成项目初始文件，例如编辑器配置、资源包和第一个场景。也可以从示例创建项目，边做边学。

![项目模板](https://cdn.phaser.io/editor-docs/project-templates-20240410.webp)

### 轻量、跨平台 {#lightweight-and-cross-platform}

编辑器支持 Windows、macOS 和 Linux。本地程序提供服务，主要界面在现代浏览器中运行。客户端利用浏览器加速，文件读写采用异步操作。项目中的图像数量会影响内存占用，网络环境下的资源加载速度则取决于连接速度。

### 桌面与云端 {#ready-for-the-desktop-and-the-cloud}

编辑器有两个发行版本。[Phaser Editor Core](/editor/intro/distributions#phaser-editor-core)可以集成到现代 Web 开发工具链或 Gitpod、GitHub Codespaces 等云开发环境。[Phaser Editor Desktop](/editor/intro/distributions#phaser-editor-desktop)提供传统的桌面 IDE 体验。

## 教程 {#tutorials}

以下是社区和 Phaser 团队制作的视频教程。

[Phaser Studio 的 YouTube 频道](https://www.youtube.com/@PhaserYouTube/playlists)

![Phaser Studio 视频频道](https://cdn.phaser.games/oss-docs/assets/ea27fb78b098ae58-phaser-youtube-banner-20241108.webp)

[Scott Westover 的 Phaser Editor 播放列表](https://www.youtube.com/playlist?list=PLmcXe0-sfoShBVVcab8kB0A_2KGf30ClP)

![Scott Westover 教程](https://cdn.phaser.games/oss-docs/assets/b9b708328938daf9-scott-phaser-editor-playlist-20241108.webp)

[旧版 Phaser Editor 2D 教程](https://www.youtube.com/@PhaserEditor2D) · [旧版 Ourcade / SuperTommy 教程](https://www.youtube.com/playlist?list=PLNwtXgWIx3riMHtFVL_x2PkiNhwPtX0gJ)
