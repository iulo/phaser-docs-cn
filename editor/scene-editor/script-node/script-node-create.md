# 创建脚本节点 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/script-node/script-node-create)

一个脚本节点对象与游戏对象共享很多,可以通过从块视图拖曳到场景中并丢到场景中来添加:

![Create script node from the blocks view.](https://cdn.phaser.io/editor-docs/script-node-create-1-20230322.webp)

此动作创建 [ScriptNode class](/editor/scene-editor/script-node/script-node-class) 实例, 并添加到场景中选择的对象中。 如果没有选中对象, 那么它会添加脚本节点到场景中 。

除了[ScriptNode class](/editor/scene-editor/script-node/script-node-class)的示例,还可以添加[ScriptNode prefab](/editor/scene-editor/script-node/script-node-prefab)的示例:在**Scripting**上下文菜单中选择**Add脚本**选项,或者按**Add脚本**命令(`U`).

![Add Script command.](https://cdn.phaser.io/editor-docs/script-node-add-script-dialog-20230627.webp)

它打开了 **Add 脚本** 对话框。 您可以在此选择您要添加的脚本 :

![The Add Script dialog.](https://cdn.phaser.io/editor-docs/script-node-add-script-dialog.webp)


## 浏览脚本节点 {#browsing-the-script-nodes}

脚本节点显示在大纲视图中,在父对象下方,或场景中:

![Script nodes in the outline view.](https://cdn.phaser.io/editor-docs/script-node-outline-20230322.webp)

另外,您还可以按命令`Shift+U`浏览对象的脚本。命令也可以在上下文菜单的**脚本** 部分中找到。该命令打开了**眉本** 对话框:

![Browsing the script nodes.](https://cdn.phaser.io/editor-docs/script-node-browse-scripts-20230322.webp)


## 创建脚本的代码生成 {#code-generation-of-the-creation-of-a-script}

当向对象添加脚本节点时,它会生成这样的代码:

```javascript
editorCreate() {
    // btn
    const btn = this.add.image(359, 223, "ui", "btn.png");

    // onPointerDownScript
    new OnPointerDownScript(btn);
    ...
}
```

添加脚本节点预制体时,是 [scene compiler](/editor/scene-editor/scene-compiler) 生成的代码。如果添加内置脚本节点的实例,则代码类似,但使用 [ScriptNode class](/editor/scene-editor/script-node/script-node-class) :

```javascript
editorCreate() {

  // btn
  const btn = this.add.image(359, 223, "ui", "btn.png");

  // scriptnode_1
  new ScriptNode(btn);
  ...
}
```

**脚本节点**类不是Phaser的一部分,但可由Phaser编辑器生成,下一节是相关内容.

---
