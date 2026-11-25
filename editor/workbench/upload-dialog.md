# 上传文件 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/workbench/upload-dialog)

要将文件或文件夹上传到您的工程, 您只需要从操作系统探索器( 如 Windows Explorer 或 Finder) 拖曳文件并把它们放入应用程序。 您可以在应用程序的任意部分丢弃文件。 然后打开对话框来选择工程中的目标文件夹 :

![Select destination folder](https://cdn.phaser.io/editor-docs/upload-select-folder.webp)

选择目标文件夹后, 文件会被上传到工程中。 下次, 对话框将在最后一个选中的文件夹中打开 。

除了在应用程序的任意部分丢弃文件外, 您可以在 [Files view](/editor/workbench/files-view) 中选择一个文件夹, 并在 [Inspector view](/editor/workbench/inspector-view) 中丢弃文件。 本节还显示一个 ** 浏览器文件 ** 按钮来打开操作系统文件选择器对话框 :

![Add Files section](https://cdn.phaser.io/editor-docs/upload-add-files-section-inspector-view-20240903.webp)

另外,您还可以在 [Files view](/editor/workbench/files-view) 中选择一个文件夹,右键单击,并选择 **Add 文件** 选项。它打开了操作系统文件选择器对话框 :

![description](https://cdn.phaser.io/editor-docs/upload-browse-files-20240903.webp)

当文件被上传到项目时,它们被选中在 [Files view](/editor/workbench/files-view) 中, [Inspector view](/editor/workbench/inspector-view) 显示 ** Asset Pack Entertaination ** 的段落. ** Assset Pack Account ** 的段落允许您在资源包文件中添加新文件,这使得它可以随时使用 Scene 编辑器中的资源.

在 Phaser 编辑器中, 您必须在资源包列表中声明资源, 以便引擎可以加载。 资源包列表是包含资源列表的 JSON 文件。 更多了解 [Asset Pack manifest](/editor/asset-pack-editor/intro) , 以及您如何使用 [import the files](/editor/asset-pack-editor/add-file#importing-from-the-files-view) 。

![Add files to the asset pack](https://cdn.phaser.io/editor-docs/upload-asset-pack-section-20240903.webp)

** 套装包条目 ** 部分显示不同按钮, 以导入不同类型的文件。 在下一个截图中, 它显示导入纹理图集的选项 :

![Selected files](https://cdn.phaser.io/editor-docs/upload-files-selected-20240903.webp)

![Select the asset pack](https://cdn.phaser.io/editor-docs/upload-asset-pack-import-option-20240903.webp)

将您输入到“资源包”的文件后, 检查器视图会显示资源预览, 以便您添加到场景编辑器中 :

![Asset preview](https://cdn.phaser.io/editor-docs/upload-asset-preview-20240903.webp)

---
