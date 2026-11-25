# 使用父对象 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/working-with-parent-objects)

在Phaser中,只有两种类型的场景物体可以用作其他物体的“容器”或“父母”:[Container](/editor/scene-editor/game-objects/container-object)和[Layer](/editor/scene-editor/game-objects/layer-object)。

在下一节中,您可以了解两种类型物体的常见操作.


## 父上下文菜单 {#parent-context-menu}

场景上下文菜单的**家长**子菜单显示您可以应用到容器和层中的命令。其中许多命令都与两种类型兼容:

![The Parent context menu.](https://cdn.phaser.io/editor-docs/parent-context-menu--07082021.webp)


## 将对象移动到父对象 {#moving-an-object-to-a-parent}

您可以将对象移动到新父目录。 命令 ** 移动到父目录 ** 打开了 ** 父目录 ** 对话框。 此对话框显示对象的所有可用的父目录( 包括场景) , 您可以选择新父目录 。

命令可以通过按下`Shift+P`键或选择上下文菜单中的**Move To Pententify**选项来执行.

![Move object to parent.](https://cdn.phaser.io/editor-docs/scene-editor-move-to-container-07082021.webp)


## 打破父母关系 {#breaking-a-parent}

父母** 命令删除容器或层,但保留孩子,孩子被添加到父母的家长身上,并保留同样的绝对位置。

您可以按下 `Shift+B` 键或选择父菜单中的 ** Break Pentro ** 选项来执行命令 。


## 选择对象的父程序 {#selecting-the-parent-of-an-object}

** 选择父 ** 命令选择对象的父。 要执行命令, 请按 `P` 键, 或点击 父上下文菜单中的 ** 选择父 **选项 。


## 选择对象的子 {#selecting-the-children-of-an-object}

** 选择子对象 ** 命令选择容器或层中的孩子。要执行此命令,请按 `N` 键,或点击 ** 选择子对象 ** 选项,请在父上下文菜单中选择。


## 改变子对象的制作顺序 {#changing-the-rendering-order-of-children}

您可以更改对象的渲染顺序。 上下文菜单显示 ** Edit ** → ** 移动 ** 命令, 以移动对象的深度方向不同 :

![Changing the rendering order of objects.](https://cdn.phaser.io/editor-docs/scene-editor-display-list-move-objects-20230627.webp)

---
