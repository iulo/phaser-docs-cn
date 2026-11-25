# 为预制体添加用户组件 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/user-components/user-components-in-prefab-object)

在上一节中, 我们显示您如何在对象中添加用户组件。 但如果您在预制体文件中添加用户组件, 会发生什么 ? 几乎是相同的, 但是此组件也会出现在所有预制体文件中 。

以移动平台的预制体为例。 它包含** Horizontal Move** 组件:

![The user components of a prefab.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-add-prefab-object-20230627.webp)

当选择此**MoovingPlatform1**预制体文件时,它也显示该**Horizontal Move**组件,但强调它属于**MoovingPlaform1** 预制体文件.

区域的标题包含组件的名称和它所属的预制体名称。区域主体显示组件属性,并看您可以锁定/解锁它们 :

![Components of a prefab instance.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-prefab-instance-components-20230627.webp)


## 生成预制体实例中组件的代码 {#generating-the-code-for-a-component-in-a-prefab-instance}

[user components compiler](/editor/scene-editor/user-components/user-components-compiler)将生成代码来改变组件的属性, 像这样:

```javascript
// movingPlatform2 (components)
const movingPlatform2HorizontalMove = HorizontalMove
                           .getComponent(movingPlatform2);
movingPlatform2HorizontalMove.horizVelocity = -50;
movingPlatform2HorizontalMove.minX = 540;
movingPlatform2HorizontalMove.maxX = 1170;
```

注意它不会创造组件, 否则它从**movingPlatform2** 预制体实例中获取组件 。


## 隐藏预制体实例的组件 {#hiding-a-component-to-the-prefab-instances}

可能您不想在预制体实例中显示预制体组件。 因为预制体组件具有本地属性和行为, 并且可以完全隐藏到预制体实例中。 为此, 您可以取消检查预制体实例中组件的** Export** 参数 :

![Export parameter.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-export-parameter-20230627.webp)


## 预选实例中组件的行动 {#actions-for-a-component-in-a-prefab-instance}

这些都是与预制体实例的用户组件相关的动作 :

![Actions for a user component instance.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-instance-menu-20230627.webp)
* **选择带有水平移动的对象**: 在现场选择包含 ** Horizontal Move ** 组件的所有对象。
* **打开水平移动的定义**: 打开 [User Components Editor](/editor/scene-editor/user-components/user-components-editor) 中组件的定义。
* **在 MovePlatform1 文件中显示**: 在新的场景编辑器中打开预页,并选择 ** Horizontal Move ** 组件。

---
