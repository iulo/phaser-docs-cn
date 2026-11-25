# 场景编译器 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/scene-compiler)

传统上,游戏引擎具有创建场景的文件格式,其API的一部分则专注于与场景编辑器的集成.

Phaser不是一个传统的游戏引擎,它是一个框架,并且不附着在任何特定的工具上。要创建 Phaser游戏,只需要简单的文本编辑器。

当然,Phaser提供了API,可以与一些广泛使用,第三方格式进行互动,如纹理图集,图纸,位图字体等. 但并没有完整的场景格式,可以将所有元素整合在一起.

对于场景编辑器,我们使用自定义的场景文件格式,但是我们没有创建自定义的库来解析和创建运行时的Phaser场景,而是创建了编译器.

电话 [scene compiler](/editor/scene-editor/scene-compiler) 将自定义场景文件(基于 JSON) 输入并生成写得很好的文件 Phaser 代码。换句话说, [scene compiler](/editor/scene-editor/scene-compiler) 写作 Phaser 密码给你

这一点有一些好处:

* 您的游戏不需要加载额外的第三方库。
* 你完全理解 场景物体是如何形成的
* 一个现代的JavaScript编辑器可以处理场景代码,并将其与内容辅助工具集成.
* 您可以自定义生成代码的某些方面, 并/或插入您的代码 。

## 正在执行编译器 {#executing-the-compiler}

您有多个选项来编译一个场景文件 :

* 当您在场景编辑器中保存一个场景文件的修改时,该场景会自动编译.
* 在场景编辑器的上下文菜单中,您可以点击**编译场景**命令.
  ![Compile scene command in context menu.](https://cdn.phaser.io/editor-docs/scene-compiler-command-in-scene-editor-04272020.webp)
* ** 编译工程** 命令汇编工程的所有文件,包括场景文件。 您可以用 `Ctrl+Alt+B` 键执行命令。 也可以在 [Main menu](/editor/workbench/main-menu) 中找到。

## 用户代码 {#user-code}

场景编辑器帮助构建游戏关卡,但涵盖游戏的各个方面却相距遥远,尤其是游戏逻辑应该由您执行,写代码.

在Phaser编程中,常见的是在同一文件中,代码创建关卡对象(Scene Editor对什么好)和代码处理对象之间的相互作用(游戏逻辑,即不是Scene Editer对对象).

我们设计了[scene compiler](/editor/scene-editor/scene-compiler), 让你可以把生成的代码和你的代码合并到同一个文件中.

这一概念很简单:

* [scene compiler](/editor/scene-editor/scene-compiler)创建了初始的JavaScript文件.
* 初始文件包含保护区域,用户可以在此插入其代码。这些区域由JavaScript评论,如`/* START-USER-CODE */`和`/* END-USER-CODE */`来划分 。
* 您可以在保护区内插入您的代码 。
* 下一次编译器更新文件时,用户保护区域被保存,这意味着,您的代码没有更改,只有编译器生成的代码才更新.

[scene compiler](/editor/scene-editor/scene-compiler)使用不同的注释来定义用户代码:

* 从文件开始到`/* START OF COMPILED CODE */`评论开始.
* 从`/* END OF COMPILED CODE */`评论结尾到文件结尾.
* 从末 `/* START-USER-IMPORT */` 注释到开始 `/* END-USER-IMPORT-CODE */` 评论。
* 从末 `/* START-USER-CTR-CODE */` 注释到开始 `/* END-USER-CTR-CODE */` 评论。
* 从末 `/* START-USER-CODE */` 注释到开始 `/* END-USER-CODE */` 评论。

下一个图像是一个实例。 您可以导入一个 `MyUtils` 类, 并将其用于 `create()` 方法 :

![User code.](https://cdn.phaser.io/editor-docs/scene-compiler-user-code-27022022.webp)


### 编辑生成的代码 {#editing-the-generated-code}

[scene compiler](/editor/scene-editor/scene-compiler)生成的代码可以在外部编辑器中编辑(类似于[Visual Studio Code](https://code.visualstudio.com)),也可以使用Phaser编辑器中内置的[Monaco editor](https://microsoft.github.io/monaco-editor/).

我们建议你读一下[Code Editor](/editor/code-editor/intro)章

场景编辑器提供两个命令,以快速编辑[scene compiler](/editor/scene-editor/scene-compiler)生成的代码文件:

![Commands to edit the Scene Compiler output code.](https://cdn.phaser.io/editor-docs/scene-compiler-edit-code-menu-02242021.webp)

** Open Outlook File ** 命令以传统方式,以新的 [Code Editor](/editor/code-editor/intro) 打开生成的文件.

** VS 代码** (`Ctrl+Alt+E`) 中的 Open Outfile 命令会发射一个本地的 [Visual Studio Code](https://code.visualstudio.com) 实例(或任何其他配置的外部编辑器),打开生成的文件.

QQQ快速编辑输出文件** 命令( 绑定在 `Q` 键上) 打开嵌入模式对话框的 [Code Editor](/editor/code-editor/intro) 生成的文件。 这样可以快速修改, 但是, Intellisense 和所有其他 [Monaco editor](https://microsoft.github.io/monaco-editor/) 特性都启用了, 因此与传统的编辑方式相比, 您有类似的经验 。

![Quick editing of compiled code.](https://cdn.phaser.io/editor-docs/scene-compiler-quick-edit-code-06092020.webp)

## 编译器设置 {#compiler-settings}

[scene compiler](/editor/scene-editor/scene-compiler)使用两组不同的参数来完善Phaser场景和预制体文件的代码生成。但是,这两种情况下都使用一般或共享的设置:

![general settings](https://cdn.phaser.games/oss-docs/assets/4879468a3bd11cef-scene-compiler-general-settings-20251125.webp)

参数:

* **生成代码**: 如果您不想编译器编译文件, 请取消选中。 [Using a prefab as a black box](/editor/scene-editor/prefabs/prefab-black-box) 区有一个实例可以使用一个没有代码生成的场景文件 。
* **输出语言**: 您可以选择如果该场景编译为 JavaScript 或 或 时 间 TypeScript。如果您选择了 TypeScript,你需要编译自己 TypeScript 生成的文件, 带有 TypeScript 编译器( E)`tsc`).
* **构造器中的字段( JS)**: 启用此选项生成类构建器中属性的初始化。默认情况下,该选项是虚假的,并且该字段在类声明中初始化。此参数仅在输出语言为 JavaScript时使用。
* **宣布字段( JS)**: 禁用此字段来跳过类中的字段。 如果您想要使用类中的字段而不声明, 则此字段将有所帮助。 此参数只用于输出语言 JavaScript 时 。
* **导出类( ES 模块)**: 包括`export default`类修饰剂.
* **自动导入( ES 模块)**: 添加“ 导入” 语句,用于导入代码生成的不同部分中使用的类型。 由用户编写的代码不处理。 如果您使用其他类型, 您应该手动导入。
* **导入文件扩展名( ES 模块)**: 在编译器生成的导入语句中添加 `.js`扩展。默认情况下,该扩展会被省略。
* **父类**: ,可以强制生成的类(预制体或场景),以扩展给定的类。如果是空的,编译器将检测相应的类。
* **允许用户类修改器( TS)**: 如果选中, 编译器生成一个用户代码区域, 允许用户声明类修改器。 仅供 TypeScript 输出使用。 用户代码区域由 `/* START-USER-CLASS-MODIFIERS */` 和 `/* END-USER-CLASS-MODIFIERS */` 注释来划分 。
* **允许用户界面( TS)**: 如果选中, 编译器将生成一个用户代码区域, 允许用户声明该类的界面。 仅供 TypeScript 输出使用。 用户代码区域由 `/* START-USER-INTERFACES */` 和 `/* END-USER-INTERFACES */` 注释来划分 。
* **插入空格**: 如果选中, 标签将被转换为空格。
* **标签大小**: 选中 ** 插入空格 ** 选项时使用的空格数。

顺便说一句,编译器生成的文件名称和类与场景文件相同。例如,a `Zombie.scene` 文件编译为 `Zombie.js` 或 减 减 `Zombie.ts`),该班的名字将是: `Zombie`.

## 场景设置 {#scene-settings}

Phaser场景的编译可以与**编译器场景设置** 进行调和:

![Scene settings.](https://cdn.phaser.io/editor-docs/scene-compiler-scene-settings-04272020.webp)

* **场景键**: 设置[Phaser.Scene configuration key](https://phaser.io/oss/docs/api-documentation/class/types-scenes.md#-settingsconfig),是可选的。

* **只生成方法**: 如果选中, 编译器不会生成 [Phaser.Scene](https://phaser.io/oss/docs/api-documentation/class/types-scenes.md) 类, 而只生成 ** creative ** 和 ** preload ** 方法 :

![Only generate methods.](https://cdn.phaser.io/editor-docs/scene-compiler-scene-settings-only-methods-04272020.webp)

如果您想要使用任何上下文创建对象, 则此选项可能有用 :
```javascript
create.call(anySceneLikeContext);
```
* **创建方法**: 编译器以您在此参数中设定的名称生成所有“创建代码 ” 。 默认情况下, 名称是 `editorCreate` 。 您第一次创建一个场景时, 它有一个 `create` 方法, 将编辑器生成的 `editorCreate` 方法调用 :

```javascript
/* START OF COMPILED CODE */

class Level2 extends Phaser.Scene {

    constructor() {
        super("Level2");

    }

    editorCreate() {

        // dino
        const dino = this.add.image(346, 233, "dino");

        // fields
        this.dino = dino;
    }

    /* START-USER-CODE */

    // this is the method called by Phaser,
    // when the scene is created.
    create() {

        this.editorCreate();

        // you can add more code here

        this.dino.setInteractive()
            .on("pointerdown", () ={
                // do something
            });
    }

    /* END-USER-CODE */
}

/* END OF COMPILED CODE */
```

* **预装包装文件**: 您可以选择要装入到场景中的包文件。如果点击按钮,它会打开 **Select Pack 文件** 对话框:

![Load asset pack files.](https://cdn.phaser.io/editor-docs/scene-compiler-scene-settings-load-pack-file-04272020.webp)

如果您选择加载一个包文件,那么编译器生成一个** 预装** 方法 :

```javascript
class Level extends Phaser.Scene {

    preload() {
        this.load.pack("asset-pack", "assets/asset-pack.json");
    }

    create() {
        // ...
    }
}
```

* **预装方法**: 类似 ** Create 方法 **, 您可以更改编译器生成的 ** 预装** 方法的名称。 然后, 您可以写出自己的 ** 预装**方法, 并给编辑器打电话 。

---
