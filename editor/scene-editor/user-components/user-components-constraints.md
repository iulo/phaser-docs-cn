# 用户组件约束 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/user-components/user-components-constraints)

默认情况下, 您可以在现场中的任何对象中添加一个用户组件。 但是, 您可以限制哪些对象可以有一个特定的用户组件。 为此, 我们引入了用户组件限制 。

用户组件限制与[Script Node constraints](/editor/scene-editor/script-node/script-node-constraints)类似,我们建议查看该指南,以便更好地了解一般限制是如何起作用的。

为了界定用户组件的局限性,我们在用户组件编辑器中创建了名为**组件制约**的新部分:

![Component constraints section](https://cdn.phaser.games/oss-docs/assets/7bf540126fdbf891-user-components-constraints-section-2025.webp)

上面的图像显示了对 *HealthComp* 用户组件的限制。 您可以看到, 这只能添加到 `EnemyPrefab` 或 `PlayerPrefab` 类的对象中 。

要添加约束,请单击**Add Controlint ** 按钮。菜单将打开,您可以选择您要添加的制约类型:

- **对象有标记**: 将用户组件限制在具有特定预制体标记的对象. [Learn more about prefab tags](/editor/scene-editor/prefabs/prefab-tags).
- **对象为实例**: 将用户组件限制在属于特定类对象的对象。

现在,所有这些约束都与一个** Match Any** 或 ** Match All** 逻辑运算符结合。这意味着您可以添加多个约束,如果至少一个约束是真实的(** Match Any **),或者所有约束都是真实的(** Mack All**),用户组件将被应用.

与脚本节点限制不同,用户组件限制没有继承,因为用户组件没有继承等级.

---
