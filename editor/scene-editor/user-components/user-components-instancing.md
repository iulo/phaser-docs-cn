# 将用户组件添加到游戏对象 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/user-components/user-components-instancing)

您可以以两种方式向对象(实体)添加用户组件:手动,以及使用场景编辑器.

手动向对象添加组件 :

```javascript
const platform = ...;
const move = new HorizontalMove(platform);
move.minX = 100;
move.maxX = 400;
```

用户组件**HorizontalMove**的构建器将组件添加到对象中。您可以保留组件的引用或者从游戏对象中获取组件,使用**getComponent**方法:

```javascript
const move = HorizontalMove.getComponent(platform);
```

然而,有趣的是,在场景编辑器中的对象中添加组件.

使用 ** Add 用户组件** 命令可以做到这一点:

- 选择一个对象。

- 执行 **Add 用户组件**命令(`M`),也可以在上下文菜单中找到 **脚本** ** **Add 用户组件 ** 。

   ![Add User Component command.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-obj-add-component-1-20230627.webp)
   
- 命令打开一个对话框, 对话框中包含工程中定义的所有组件( 由 `*.components` 文件组合) 。 请选择您要添加的组件 :

   ![Select user component.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-obj-add-component-2-20230627.webp)

- 检查员的意见提供了一个新的**Horizontal Move**部分,其中包含该部分的属性:

   ![Showing the user components of an object.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-show-components-20230627.webp)

## 生成对象中组件的代码 {#generating-the-code-for-a-component-in-an-object}

[user components compiler](/editor/scene-editor/user-components/user-components-compiler)会生成代码来创建组件,就像你用手写:

```javascript
// bridge2 (components)
const bridge2HorizontalMove = new HorizontalMove(bridge2);
bridge2HorizontalMove.horizVelocity = 100;
bridge2HorizontalMove.minX = 10;
bridge2HorizontalMove.maxX = 400;
```

## 用于某个构成部分的行动 {#actions-for-a-component}

这些是与对象的用户组件相关的动作 :

![User component section's menu.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-section-menu-20230627.webp)
* **选择带有水平移动的对象**: 在现场选择包含 ** Horizontal Move ** 组件的所有对象。
* **打开水平移动的定义**: 打开 [User Components Editor](/editor/scene-editor/user-components/user-components-editor) 中组件的定义。
* **上移( A)**, ** 移动下**:改变组件的顺序。
* **删除**: 从对象中删除组件。

## 在场景中浏览用户组件 {#browsing-the-user-components-in-a-scene}

您可以使用 ** 浏览用户组件 ** (`Shift+M`) 命令来查看场景所有对象中的所有用户组件的概览 :

![Browse User Component command.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-browse-1-20230627.webp)![User components in the scene.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-browse-2-20230627.webp)


您可以让 [setting](/editor/workbench/settings) ** 显示大纲中的用户组件 ** 来显示/隐藏大纲视图中的用户组件 :

![show user component in outline setting](https://cdn.phaser.games/oss-docs/assets/54cb644dd3d64a17-scene-editor-user-components-outline-set.webp)

如果启用了该参数,您将在“大纲”视图中看到对象的用户组件:

![user components in the outline view](https://cdn.phaser.games/oss-docs/assets/26f8937ba846a06e-scene-editor-user-components-in-outline-.webp)

---
