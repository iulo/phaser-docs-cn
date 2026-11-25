# 图像 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/image-object)

[Image](/editor/scene-editor/game-objects/image-object)是一种内置的Phaser天体类型:[Phaser.GameObjects.Image](/api/class/gameobjects-image).

您可以通过从块视图中丢弃图像内置类型或纹理来创建 [Image](/editor/scene-editor/game-objects/image-object) 对象 。

![Add image from Blocks view.](https://cdn.phaser.io/editor-docs/scene-editor-drop-image-04152020.webp)

两者的主要区别是 [Image](/editor/scene-editor/game-objects/image-object) 和一个闪光的,是 [Image](/editor/scene-editor/game-objects/image-object) 无法播放对象 [sprite animations](/api/class/gameobjects-sprite#play).

[Image](/editor/scene-editor/game-objects/image-object)在代码中使用[image factory](/api/class/gameobjects-gameobjectfactory#image)创建。[scene compiler](/editor/scene-editor/scene-compiler)就是这样生成一个[Image](/editor/scene-editor/game-objects/image-object)的代码的:

```javascript
const branch_1 = this.add.image(192, 512, "atlas-props", "branch-01");
```

[Image](/editor/scene-editor/game-objects/image-object)具有与其他对象类型相同的属性: .

* [Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties)
* [Lists properties](/editor/scene-editor/game-objects/common-object-properties#lists-properties)
* [Transform properties](/editor/scene-editor/game-objects/common-object-properties#transform-properties)
* [Origin properties](/editor/scene-editor/game-objects/common-object-properties#origin-properties)
* [Flip properties](/editor/scene-editor/game-objects/common-object-properties#flip-properties)
* [Visible property](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/common-object-properties.md#visible-property)
* [Alpha properties](/editor/scene-editor/game-objects/common-object-properties#alpha-properties)
* [Texture property](/editor/scene-editor/game-objects/common-object-properties#texture-property)

---
