# 编译动画键常量 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/animations-editor/compiler)

您可以启用一个有动画键常数定义的代码文件的编译。

每部动画, 编译器将生成一个恒定声明。 例如 :

![Animations constants compiler.](https://cdn.phaser.io/editor-docs/animtions-editor-compiler-20221114.webp)

如果您在游戏中有很多动画, 我们建议使用此功能。 您可以使用常数( 和自动补全) 来参考动画, 而不是“ 手” 写关键名称 。

默认情况下, 编译器被禁用。 您可以在 ** 编译器设置 ** 区启用它。 本区显示没有选择动画时 :

![Compiler settings.](https://cdn.phaser.io/editor-docs/animations-editor-compiler-settings-20221114.webp)

这是一个带有参数的表格:

* **生成代码**: 启用代码生成 。
* **输出语言**: 选择JavaScript和TypeScript.
* **ES 模块**: 如果选中, 它会生成一个 ES 模块文件 。
* **输出文件夹**: 选择输出文件的父文件夹。 如果您正在使用 WebPack 或类似的捆绑器, 您可能想要在 src 文件夹的子目录中生成代码 。

![Select the output folder.](https://cdn.phaser.io/editor-docs/animations-editor-select-output-folder-20221114.webp)

---
