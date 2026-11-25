# 为游戏对象启用 Arcade 物理 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/arcade-physics/arcade-physics-add-body)

您可以在任意游戏对象中启用一个 Arcade 物理体 :

* 选择对象并打开上下文菜单。
* 在 ** Arcade 物理** 菜单中,选择 ** Add body** 选项.
  
  ![Add Arcade body to an object](https://cdn.phaser.io/editor-docs/arcade-physics-add-body-20221005.webp)

* 按下`B`键,用于[editing the body’s offset & size](/editor/scene-editor/manipulation-tools#arcade-physics-body-tool):

  ![Edit the body's size with the tool.](https://cdn.phaser.io/editor-docs/arcade-physics-edit-body-tool.webp)

* 或编辑检查员认为的任何其他机构的属性:

  ![Edit the body's properties in the Inspector view.](https://cdn.phaser.io/editor-docs/arcade-physics-edit-body-inspector.webp)

您可以删除对象的物理体。 在相同的 ** Arcade 物理** 中, 请选择 ** 移动对象** 选项。 此选项只有在选定对象不是 [built-in Arcade Image or Arcade Sprite](/editor/scene-editor/arcade-physics/arcade-physics-add-object) 对象时才可用 。

当您在对象中添加物理体时,创建对象的代码会像这样生成:

```javascript
const gorilla = this.add.image(379, 271, "gorilla")
    as Phaser.GameObjects.Image & { body: Phaser.Physics.Arcade.Body };
this.physics.add.existing(gorilla, false);
```

注意 `as Phaser.GameObjects.Image & { body: Phaser.Physics.Arcade.Body }` 表达式。 它告诉 TypeScript 编译器, `image(...)` 方法创建的对象是 `Image` , 但也有一个弧形体。 生成有效的 TypeScript 代码需要注释 。

---
