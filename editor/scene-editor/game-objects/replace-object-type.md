# 替换对象的类型 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/replace-object-type)

当将块视图项目扔入场景时,会创建新对象。如果您所丢的项目是图像或地图框,则会创建 [Image](/editor/scene-editor/game-objects/image-object) 对象。

然而, 您可以将 [Image](/editor/scene-editor/game-objects/image-object) 对象的类型更改为另一个, 如 Sprite 或 [TileSprite](/editor/scene-editor/game-objects/tile-sprite-object) 。 您可以将任意类型的对象转换为其它类型。 我们给它命名为对象类型替换 。

要替换类型, 请执行上下文菜单 ** 类型** 子菜单中显示的 ** 替换类型** 命令。 该命令打开了 ** 替换类型**对话框。 对话框显示编辑器支持的不同类型, 包括您的预制体文件。 请选择新类型, 按 ** 替换** 。

例如,您可以将文本对象转换为位图图文集 :

- 选择文本对象, 打开上下文菜单并启动 ** 替换类型 ** 对话框 :

  ![Open the Replace Type dialog.](https://cdn.phaser.io/editor-docs/scene-editor-replace-type-1-04262020.webp)

- 在 ** 替换类型 ** 对话框中, 选择 BitmapText 类型。 它打开了 ** 选择 Bitmab 字体 ** 对话框。 为新对象选择想要的字体( 没有字体, 您无法创建 BitmapTExt 对象 ):

  ![Select the font for the new BitmapText.](https://cdn.phaser.io/editor-docs/scene-editor-replace-type-2-06092020.webp)

- 最后,对象被转换为比特玛普Text。注意两种类型共有的属性都保存不变。[Text property](/editor/scene-editor/game-objects/common-object-properties#text-property)就是一个例子:

  ![Converted to BitmapText.](https://cdn.phaser.io/editor-docs/scene-editor-replace-type-3-04262020.webp)


## 保持原始纹理 {#keeping-the-original-texture}

** 替换类型** 对话框可以在您用 Prefab 类型替换图像对象时保留原始纹理。默认情况下,该对象将获得 Prefab 的纹理。然而,如果您选择了 ** 保留原始纹理** 选项,在类型替换后,对象将解锁纹理属性并使用原始纹理 。

![The Keep original texture parameter.](https://cdn.phaser.io/editor-docs/scene-editor-replace-type-keep-original-texture-06092020.webp)

---
