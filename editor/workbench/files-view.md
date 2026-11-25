# 文件视图 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/workbench/files-view)

文件视图显示工程的文件。 文件以树状结构显示, 和其他许多文件导航器一样 。

与 IDE 中的其他 [content viewers](/editor/misc/content-viewers) 一样, 文件视图显示某种类型的文件的内置预览。 同时, 您可以按 `Shift` 键和滚动鼠标轮来放大 。

![Files view zooming.](https://cdn.phaser.io/editor-docs/files-view-zoom-04052020.webp)

## 上下文菜单 {#context-menu}

上下文菜单列出了几套常见的文件操作.

** New... ** 子菜单显示快捷键,以创建与 IDE 工具相关的新文件.

![Context menu of the Files view.](https://cdn.phaser.games/oss-docs/assets/3963e3d9dc2eaee1-files-view-context-menu-20241220.webp)

** Open With ** 子菜单显示您可以用来打开所选文件的所有编辑器 。

此处 **Rename**, **Move**, **Copy To** 和 **Move to Trash** 选项与其他文件管理器一样有效。 但是警告, 此时, 这些操作无法被撤销, 所以要小心。 在编辑器的桌面分发中, **Move to Track** 操作将文件移动到系统垃圾中 。

如果您在本地运行服务器( 不使用 `-public` 选项), 那么上下文菜单会显示 ** Locate 文件 ** 项目。 它会在所选文件或文件夹的位置打开您的操作系统默认文件管理器 。

同样,**在终端**命令中打开了所选文件或文件夹位置的OS终端.

**Add文件** 打开UI到[copy external files to the project](/editor/workbench/upload-dialog).

## 在检查器视图中编辑资源包 {#inspector-view-integration}

检查器视图显示活动视图或部分中所选择对象的属性。当您在文件视图中选择文件时,检查器视图显示文件的不同属性部分。

在所有情况下,检查官视图都显示**File**部分,显示**Name**、**FulName**、**Size**,并显示一个按钮,以编辑器打开文件。

此外,插件还可以提供自己的文件属性部分供Scooker查看。有图像预览、场景预览或[Asset Pack Editor section](/editor/asset-pack-editor/add-file#importing-from-the-files-view)等案例,允许将文件导入到显示的资源中。

![Inspector view shows the selected file properties.](https://cdn.phaser.games/oss-docs/assets/eccdf5c0f9988a2e-files-view-inspector-20241220.webp)

---
