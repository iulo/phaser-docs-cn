# 导入文件 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/asset-pack-editor/add-file)

在游戏中使用文件之前,您必须在 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 中创建配置项。这叫做 **导入** 文件 。

您可以使用资源包编辑器的 [Main toolbar](#importing-using-the-main-toolbar) 或 [Blocks view](#importing-from-the-blocks-view) 导入文件,
或使用 [Files view](#importing-from-the-files-view) 。我们将在以下各节讨论每个问题。

您可以取消导入文件, 删除它 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 条目,按下 `Delete` 键在 [Asset Pack Editor](/editor/asset-pack-editor/intro) 或 时间 [Outline view](/editor/asset-pack-editor/outline-view),或从上下文菜单中。

## 使用主工具栏导入 {#importing-using-the-main-toolbar}

这些都是:

1. 在资源包编辑器活动时,按 [Main toolbar](/editor/workbench/main-toolbar) 中的 ** 导入文件** 按钮(也可以在上下文菜单中或按 `A` 键使用).
2. 它打开了所有文件类型的对话框。选择要添加的文件类型 。

   ![Select the file type.](https://cdn.phaser.io/editor-docs/asset-pack-editor-add-file-1-01012022.webp)

3. 当您选择文件类型时, 它会打开一个对话框, 并列出要添加的候选文件列表。 候选文件会按照这些规则选择 :

   - 文件属于编辑器输入文件的文件夹,或子文件夹。 这不是 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 的限制, 但我们用它来简化文件导入过程 。
   - 文件名称的内容类型或扩展名与所选类型兼容。例如,如果选择添加图像,则只显示图像文件。
   - 这些文件不包含在项目中的任何其他[Asset Pack file](/editor/asset-pack-editor/asset-pack-file)中.

   然而,您总是可以选择选择任何文件,按下对话框的 **Show All File ** 按钮。
   ![Select the files to be added.](https://cdn.phaser.io/editor-docs/asset-pack-editor-add-file-2-01012022.webp)

4. 更改检查器视图中文件配置的属性。 字段的许多值是自动设定的。 文件 URL 是在项目中使用它的相对路径计算出来的。 读 [Setting the root folder for the asset files](#setting-the-root-folder-for-the-asset-files) 以了解更多关于资源文件 URL 的信息 。

   ![Edit properties of a file configuration.](https://cdn.phaser.io/editor-docs/asset-pack-editor-edit-file-inspector-view-2-01012022.webp)

## 从块视图导入 {#importing-from-the-blocks-view}

Blocks视图是一个通用视图,它与活动编辑器连接,并提供构建编辑器对象所需的"块".

[Asset Pack Editor](/editor/asset-pack-editor/intro) 活动时, 块视图显示要导入的候选文件。 如果 : 文件是要导入的候选文件 。

- 文件属于[Asset Pack file](/editor/asset-pack-editor/asset-pack-file)的文件夹,或子文件夹,是编辑器的输入(除非您禁用此限制,在本节末尾讨论).
- 此文件在工程中的其他 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 中不存在 。
- 如果文件有我们知道从未在游戏中加载的内容类型或文件名扩展名:

  - TypeScript 文档( Q)`.ts`).
  - 场景编辑器文件 (`.scene`).
  - 又一个[Asset Pack file](/editor/asset-pack-editor/asset-pack-file)。

这些都是:

1. 选择要导入的块视图中的文件。
2. 在检查器视图的** 套装包条目** 部分中选择一个导入选项。

   ![Import files from Blocks view.](https://cdn.phaser.io/editor-docs/asset-pack-add-file-from-blocks-view-01012022.webp)

1. 当文件导入时, 请编辑 检查 视图中的新配置 。

这比使用[Main toolbar](/editor/workbench/main-toolbar)按钮简单:一旦您选择了文件,编辑器只根据内容类型和名称显示相关的导入选项.

## 在块视图中显示全部文件 {#showing-all-files-in-the-blocks-view}

正如我们以前提到的那样, 块视图只显示与 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 相同的文件夹( 或子文件夹) 中的文件。 您可以检查 检查 Project** 中的所有文件 :

![Show all files in the Blocks view.](https://cdn.phaser.io/editor-docs/asset-pack-show-all-files-in-blocks-20210529.webp)

## 从文件视图导入 {#importing-from-the-files-view}

从文件视图导入与从块视图导入非常相似, 但你不需要打开 [Asset Pack Editor](/editor/asset-pack-editor/intro) 。

无论[Asset Pack Editor](/editor/asset-pack-editor/intro)是否活动,您都可以在文件视图中选择一个或一个以上的文件,在检查器视图的 ** Asset Pack Entertain ** 部分中,选择将文件导入到一个存在的[Asset Pack file](/editor/asset-pack-editor/asset-pack-file)或一个新的文件的选项。

![Import files from the Files view.](https://cdn.phaser.io/editor-docs/asset-pack-editor-import-from-files-view-1-01012022.webp)

如果在文件视图中您选中的文件已经在一个配置条目中 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file),然后检查器视图显示一个按钮打开 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 输入 [Asset Pack Editor](/editor/asset-pack-editor/intro).

![Open Asset Pack file with configuration for the selected files.](https://cdn.phaser.io/editor-docs/asset-pack-editor-import-from-files-view-2-01012022.webp)

## 设置资源文件的根文件夹 {#setting-the-root-folder-for-the-asset-files}

当您在资源包中添加新文件条目时,编辑器会使用工程相对于文件的路径URL作为此路径。例如,如果您添加了全路径的图像文件 `<project root>/assets/background.png`,然后将资源包条目中的 URL 设置为 `assets/background.png`.

这一点对很多案件来说是不错的。 但是,如果你使用[WebpackJS](https://webpack.js.org)或Parcel等网络捆绑器,那就可能不同了。 也许资源在项目和网站上的相对路径是不一样的。

举个例子。 [WebpackJS](https://webpack.js.org) 项目模板 Phaser 编辑器有这样的布局 :

![Project layout of the Webpack template.](https://cdn.phaser.io/editor-docs/asset-pack-static-folder-webpack-03312021.webp)

注意如果将 `FufuSuperDino.png`文件添加到资源包中, 它会将图像的URL设置为 `static/assets/FufuSuperDino.png`。 然而, `static`文件夹不在发行架构中( 在网站上) 。 它只复制其内容到发行架构文件夹中。 所以, 当您在浏览器中打开游戏时, 图像文件的路径是 `assets/FufuSuperDino.png`( 没有 `static` 元素) 。

现在, Phaser 编辑器允许更改资源的根文件夹。如果添加空的 `publicroot` 文件,在 `static` 文件夹,然后编辑器将创建文件 URL,并附带与 URL 的相对路径 `<project root>/static` 文件夹 :

![the publicroot file.](https://cdn.phaser.io/editor-docs/asset-pack-publicroot-file-03312021.webp)

规则很简单。 当您为新文件添加一个条目时, 它会使用根文件夹的相对路径构建文件的 URL。 要找到根文件夹, 它会检查每个包含 `publicroot`文件的父文件夹, 然后将该文件夹作为根文件夹来构建 URL。 如果没有找到 `publicroot` 文件, 它会默认为工程的根文件夹 。

---
