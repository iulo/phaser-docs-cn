# 编辑器 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/workbench/editors)

编辑器是专门编辑对象或输入的面板,它有一个标题和内容区域。标题显示输入对象的名称或标识符,内容区域提供编辑输入的UI元素。在大多数情况下,编辑器的输入是一个文件。


## 肮脏的状态 {#dirty-state}

编辑器的一个重要特点是“ 脏” 状态。 当用户在编辑器中更改某物时, 编辑器被标记为“ 脏” , 并显示应该保存它来坚持更改。 如果您关闭编辑器但内容脏, 则显示确认信息, 因为更改会丢失 。

![Editor dirty state and content preview.](https://cdn.phaser.games/oss-docs/assets/029b1929cfa9eb00-workbench-editor-dirty-20241219.webp)


## 标题图像 {#title-image}

编辑器的标题,在许多情况下,会显示输入内容的预览。这是场景或图像的情况。这有助于识别编辑器打开时的输入。

您可以按下 `Ctrl+3` 和 `Ctrl+4` 使标题图像大小大小 :

![small tab image](https://cdn.phaser.games/oss-docs/assets/e4184bea2762d059-workbench-editor-title-small.webp)

![bigger tab image](https://cdn.phaser.games/oss-docs/assets/33c9f52d4991187e-workbench-editor-title-big.webp)


## 标题菜单 {#title-menu}

编辑器的标题提供了带有几个选项的上下文菜单。要关闭编辑器,请关闭其他编辑器,或更改标题的图像大小:

![The context menu of the editor's title.](https://cdn.phaser.games/oss-docs/assets/e5eb5c8ebfbe0c6b-workbench-editor-title-menu-20241219.webp)


## 恢复编辑器 {#restore-editors}

当您打开一个工程时, IDE 打开上一个会话中使用的编辑器。 这些信息存储在浏览器的本地存储中。 这意味着, 它不存在于其它浏览器实例中, 或者您可以通过清除浏览器的私人数据来删除它 。

---
