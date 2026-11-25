# 预制体实例的显示属性 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/prefabs/prefab-display-properties)

当创建预制体实例时, 大纲视图显示变量的名称为对象的显示名称 。

以这个例子为例。

按钮的变量名称为**buttonDown**:

![The variable name.](https://cdn.phaser.io/editor-docs/scene-editor-prefabs-display-name-variable-name-1.webp)

...和大纲视图在标注对象时使用相同名称:

![The label in the Outline view.](https://cdn.phaser.io/editor-docs/scene-editor-prefabs-display-name-outline-1.webp)

然而,您可以更改对象的标签, 并使用更描述性的名称。 您可以在预制体场景的属性部分中设置 ** 对象显示名称 ** :

![Object display name definition.](https://cdn.phaser.io/editor-docs/scene-editor-prefabs-display-name-definition.webp)

按钮实例的显示名称将是 `Button - ${action}`。 它是带有占位符的名称模板, `${action}` 占位符中包含按钮的** Action ** 预fab 属性的值 。

`action`名称是用户属性`Action`的可变名称。 您可以在属性中盘旋鼠标以获取属性信息 :

![The info of a prefab property.](https://cdn.phaser.io/editor-docs/scene-editor-prefab-display-name-property-tooltip-20231205.webp)

现在,按钮以新显示名称显示在大纲视图中。注意`${action}`表达式根据** Action**属性的值被`UP`、`DOWN`或`FIRE`取代:

![The new display name of the objects in the outline view.](https://cdn.phaser.io/editor-docs/scene-editor-prefabs-display-name-outline-2.webp)

当您添加对象时, 特别是此技术, 但其变量名称与游戏执行无关。 或者当您想要提供更详细对象信息时, 也特别有用 。

许多脚本节点就是如此:

![Using the prefab display name in the script nodes.](https://cdn.phaser.io/editor-docs/scene-editor-prefabs-display-name-script-node-20231205.webp)

除此之外, `${propName}` 语法,您可以使用 `#{propName}` 表达式。它将被属性名称所取代(`propName`)如果属性的价值是 `true`, `undefined`, `""`,或等值于 JavaScript.

这是一个实例。 显示名称是 `Collide #{up} #{down}`如果该值的值为 `up` 属性是 `true` 编辑 `down` 属性是 `false`,则最后显示名称将是 `Collide #up`.

表示您可以使用这个语法来显示“ tags ” 。

Prefab 显示属性部分也包含属性:

- 对象填充颜色
- 对象描边颜色
- 对象文字颜色

这些属性允许您为代表预制体实例的大纲视图项目设置自定义颜色 :

![prefab color display properties](https://cdn.phaser.games/oss-docs/assets/6feccaf5ec583f37-color-prefab-display-properties-20251124.webp)

![prefab instance display color properties](https://cdn.phaser.games/oss-docs/assets/d5cab2f45c88718c-color-display-prefab-instance-20251124.webp)

---
