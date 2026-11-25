# 创建带 Arcade 物理的图像和精灵 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/arcade-physics/arcade-physics-add-object)

以Arcade物理体创建物体的最简单方式是将一个[Phaser.Physics.Arcade.Image](/api/class/physics-arcade-image)或[Phaser.Physics.Arcade.Sprite](/api/class/physics-arcade-sprite)物理体添加到场景中。在Blocks视图的Arcade部分中,可以找到这两种类型:

![Drop arcade image from blocks view.](https://cdn.phaser.io/editor-docs/arcade-add-image-1-20221005.webp)

当你把它扔到现场时, 它会显示一个选择纹理的对话框 :

![Select the image's texture.](https://cdn.phaser.io/editor-docs/arcade-add-image-2-20221005.webp)
![A physics object in the scene.](https://cdn.phaser.io/editor-docs/arcade-add-image-3-20221005.webp)

街机游戏对象与Arcade 物理系统的[image](/api/class/physics-arcade-factory#image)和[sprite](/api/class/physics-arcade-factory#sprite)工厂以代码生成:

```javascript
// gorilla
const gorilla = this.physics.add.image(310, 313, "gorilla");
gorilla.body.setOffset(216, 58);
gorilla.body.setSize(186, 365, false);
```

**Acade Image ** 和 **Acade Sprite ** 游戏对象类型提供了物理体配置的辅助方法,但是,你可以[enable an Arcade physics body in any other game object](/editor/scene-editor/arcade-physics/arcade-physics-add-body).

---
