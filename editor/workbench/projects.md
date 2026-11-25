# 项目 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/workbench/projects)

一个 Phaser 编辑器项目只是一个文件夹。 它包含您的游戏文件, 通常它也是游戏网络路径的根。 这意味着, 您可能应该将 `index.html` 文件放在文件夹的根 。

有些项目设置(例如基于[WebpackJS](https://webpack.js.org)),项目文件夹不是游戏的根.

[Learn more about setting the public root of the project](/editor/asset-pack-editor/add-file#setting-the-root-folder-for-the-asset-files)

在 [Phaser Editor Core](/editor/intro/distributions#phaser-editor-core)中,您应该通过工程路径作为程序参数:

```bash
$ PhaserEditor -project /path/to/project
```

在[Phaser Editor Desktop](/editor/intro/distributions#phaser-editor-desktop)中,可以创建一个新的项目:

[Learn how to create your first project](/editor/first-steps/create-first-project)

![Create project](https://cdn.phaser.io/editor-docs/first-steps-desktop-new-project-1-20240926.webp)

或从最近的项目部分中选择一个项目:

![Recent projects](https://cdn.phaser.games/oss-docs/assets/4a8b306632dbbeb7-desktop-projects-recent-section-20260414.webp)

## 从最近的项目中删除 {#remove-from-recent-projects}

随着时间的推移,这个部分可能会充满旧的项目,所以删除任何你不再需要的都是好主意.

要从最近列表中删除一个工程, 请单击项目行末尾的垃圾图标 。

![Remove from recent projects](https://cdn.phaser.games/oss-docs/assets/f75c908408e4831c-desktop-projects-recent-section-remove.webp)

## 重新装入工程 {#reload-project}

Phaser编辑器不是在考虑协作编辑的情况下创建的。这意味着它假设只有一个用户在同一时间在同一个工程上工作。您可以使用`Git`这样的源控件管理器与您的团队合作.

然而,您可能用外部工具更改项目文件, 并且需要刷新IDE中的修改。 当IDE获得焦点时, 它会进行由外部工具进行的修改的递增重载, 但是您可以强制(并且我们建议) 完全重载项目:

* 正在按下 `Ctrl+Alt+R`.
* 或点击 [Main menu](/editor/workbench/main-menu) 的 ** Reload Project** 选项.

整个项目重新装入也可以帮助修复与场景编辑器或任何其他编辑器的故障.

重新加载项目不同于整个网页的重新加载, 因为只有项目的文件再次被请求。 但是如果看到您的 IDE 正在消耗大量的内存资源, 重新加载整个网页是一个很好的程序 。

您可以读取 [Resources caching](/editor/misc/resources-caching) 一节以获取更多信息。

## 不包括项目中的文件 {#excluding-files-from-project}

您有可能将 Phaser 编辑器文件与其他工具的文件合并。 在这种情况下, 您可以过滤 [Files view](/editor/workbench/files-view) 中显示的文件 。

[Learn how to filter resources in the project](/editor/misc/resources-filtering)

## 文件缓存 {#files-cache}

Phaser编辑器缓存项目的文件,以提高IDE的性能。此缓存主要存储在内存和浏览器的存储中。这不常见,但如果看到IDE显示过时的文件,或者如果项目耗尽了大量内存,可以通过刷新页面(`Ctrl+R`)来清除缓存.

[Learn more about resources cache](/editor/misc/resources-caching).

---
