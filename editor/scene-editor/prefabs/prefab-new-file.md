# 创建预制体文件 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/prefabs/prefab-new-file)

Prefab 是您可以用 [New File dialog](/editor/workbench/new-file-dialog) 创建的场景文件。 在对话框中, 请选择 ** Prefab 文件 ** 选项。 它打开了 ** 新 Prefab ** 对话框, 您可以在此选择父文件夹和新 Prefab 文件的名称。 此名称将用来生成 Prefab 的类名, 因此让我们写一个有效的类名 。

![Create prefab file.](https://cdn.phaser.io/editor-docs/scene-editor-new-prefab-file-04202020.webp)

注意 Prefab 文件只是一个场景文件。 当它创建时, 它为空; 您应该创建一个会是 [the prefab object](/editor/scene-editor/prefabs/prefab-object) 的对象 。

另外,您还可以在场景编辑器中直接创建 Prefab。 此操作非常方便。 您可以选择和反对并将其转换为新的 Prefab :

- 选择场景中的某个对象。
- 打开上下文菜单并选择 **Prefab ** ** ** ** Create Prefab With Object ** 选项。
  
  ![Create prefab with object.](https://cdn.phaser.io/editor-docs/scene-editor-new-prefab-file-with-object-06082020.webp)

- 它打开了 ** 新预制体文件** 对话框。 请选择文件名称和位置 。
  
  ![New prefab with object dialog.](https://cdn.phaser.io/editor-docs/scene-editor-new-prefab-file-with-object-dialog-06082020.webp)

- 选中的对象转换为新 Prefab 实例。 新 Prefab 已列在 Blocks 视图中, 并准备创建新实例 。

---
