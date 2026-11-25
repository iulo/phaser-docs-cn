# 用户组件编辑器 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/user-components/user-components-editor)

组件(或类似的图案)被广泛用于流行的游戏引擎或编辑器中. 许多这些工具使用自定义的脚本语言或某种语言的某些元素(如元数据或属性)来提供组件信息,如属性描述,默认值,UI渲染等. 组件的代码有组件的元数据作为其执行的一部分.

在 Phaser 编辑器中,现在情况不同。我们使用配置文件(JSON)和一个[User Components compiler](/editor/scene-editor/user-components/user-components-compiler)来解析这些文件,生成组件的 JavaScript(或TypeScript) 代码。或者说,最好说,组件代码的一部分,因为,就像场景编辑器对场景文件所做的那样,你可以将代码插入到 [User Components compiler](/editor/scene-editor/user-components/user-components-compiler)的输出中。

配置文件( `*.components`) 中的信息被 Scene 编辑器用于构建游戏对象添加和编辑组件所需的UI 元素, 游戏运行时不需要它。 我们强烈建议将其排除在游戏的发行架构之外 。

## 添加新组件 {#add-new-component}

要添加一个新的用户组件,您可以:按下 `A` 键,点击 [Main toolbar](/editor/workbench/main-toolbar) 中的 ** Add 组件** 按钮,或在上下文菜单中选择 ** Add 组件 ** 选项。

![Add new user component.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-add-component-20221101.webp)

新建的组件有一个默认名称,因此在检查专员看来,你可能希望更改它。

如您在图像中看到的,组件以查看器显示,并像类声明一样渲染:带有类名以及属性的名称和类型.

要删除组件, 请按 `Delete` 键。 或者在上下文菜单中选择 ** Delete ** 选项 。

## 编辑组件信息 {#edit-the-component-info}

组件是使用组件将状态和行为添加到游戏对象的类。要编辑组件的信息,可以在编辑器中选择,并在检查器视图中编辑值。

这是您可以编辑的元数据 :

* 组件类的名称 。
* 游戏对象(或实体)的类型。在字段旁边,您可以打开一个菜单,其中包含共同可能的选项。
* 组件类的超级类。 它是可选的。 在字段旁边, 您可以打开一个菜单, 并附带其他组件中所用的共同选项和名称 。
* 组件的显示名称。 这是编辑器不同部分使用的名称。 它默认是可选的和空的。 当 ** Display Name ** 空时, 则使用 ** Name ** 。
* 对象显示格式。 这是用于在“ 大纲” 视图中显示预制体实例显示名称旁边的组件信息的一个模板字符串。 它的工作原理与 [the prefab display properties](/editor/scene-editor/prefabs/prefab-display-properties) 一样。 它是可选的 。

![Edit component info.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-edit-props-2-20240110.webp)

属性与[Prefab user properties](/editor/scene-editor/prefabs/prefab-user-properties#creating-a-prefab-user-property)相同.

您可以按 ** Add 属性** 按钮添加新属性 。

上面的图像显示的是 ** Horizontal Move ** 组件, 它有一个游戏对象类型 `Phaser.GameObjects.Image`。 这意味着您应该将这个组件添加到该类型对象( 实体) 。 以及 ** horizVelocity**, ** minX** 和 ** minY** 属性 。

![The component's properties.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-props-20221101.webp)

为编辑属性信息,请在编辑器中选择,并在检查器视图中设置值 :

![Edit property.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-edit-property-20221101.webp)

此组件被编译为此 JavaScript 代码 :

```javascript
// You can write more code here

/* START OF COMPILED CODE */

class HorizontalMove {

    constructor(gameObject) {
        gameObject["__HorizontalMove"] = this;

        /** @type {Phaser.GameObjects.Image} */
        this.gameObject = gameObject;
        /** @type {number} */
        this.horizVelocity = 0;
        /** @type {number} */
        this.minX = 0;
        /** @type {number} */
        this.maxX = 3070;

        /* START-USER-CTR-CODE */
        // You can write code here
        /* END-USER-CTR-CODE */
    }

    /** @returns {HorizontalMove} */
    static getComponent(gameObject) {
        return gameObject["__HorizontalMove"];
    }

    /* START-USER-CODE */
    // You can write code here
    /* END-USER-CODE */
}

/* END OF COMPILED CODE */

// You can write more code here
```

请检查[User Components compiler](/editor/scene-editor/user-components/user-components-compiler) 一节,以了解更多组件是如何被翻译为JavaScript代码的.

## 编辑组件代码 {#edit-the-component-code}

要编辑组件的 [code generated](/editor/scene-editor/user-components/user-components-compiler), 您可以双击编辑器中的组件。 它会打开内置代码编辑器中的组件代码文件 。

另外,您还可以选择组件并按下 `Q` 键。它会打开一个使用代码编辑器的快速编辑对话框:

![Edit component code in the Quick Edit dialog.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-edit-code-20221101.webp)

上下文菜单显示编辑组件输出文件的所有选项 :

![Open output file options.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-open-editor-menu-20221101.webp)

** 打开工作室代码**(`Ctrl+Alt+E`)中的输出文件,命令打开配置的外部编辑器中的输出文件.

---
