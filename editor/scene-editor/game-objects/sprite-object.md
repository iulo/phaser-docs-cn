# 精灵 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/sprite-object)

Sprite是内置的Phaser对象类型:[Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite)。它就像[Image](/editor/scene-editor/game-objects/image-object),但也能够玩[sprite animations](/api/class/gameobjects-sprite#play)。这意味着,只有当一个Sprite对象在游戏中被动画化时,你才可以使用,否则,最好使用[Image](/editor/scene-editor/game-objects/image-object).

使用 [sprite factory](/api/class/gameobjects-gameobjectfactory#sprite) 创建了 Sprite 代码。 [scene compiler](/editor/scene-editor/scene-compiler) 就是这样生成 [Sprite](/editor/scene-editor/game-objects/sprite-object) 代码的 :

```javascript
const player = this.add.sprite(192, 512, "dragon-atlas", "idle-000");
```

要创建Sprite对象,您可以:

* 将一个内置的 Sprite 块丢入现场 :
  ![Create an empty Sprite.](https://cdn.phaser.io/editor-docs/scene-editor-sprite-create-20231023.webp)
* 丢一个[animation block](/editor/scene-editor/sprite-animations)在现场:
  ![Create a Sprite object from an animation block.](https://cdn.phaser.io/editor-docs/scene-editor-sprite-create-from-animation-block-20231023.webp)
* 或者你可以把一个[Image](/editor/scene-editor/game-objects/image-object)或[TileSprite](/editor/scene-editor/game-objects/tile-sprite-object)转换成一个螺旋桨.

[Learn more about type conversion](/editor/scene-editor/game-objects/replace-object-type)

如果您创建了图案, 您可能想要用它来播放动画。 要做到这一点, 您可以设置 [Animation properties](/editor/scene-editor/game-objects/common-object-properties#animation-properties) 。

闪光闪烁类型具有与其他对象类型相同的属性:

* [Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties)
* [Lists properties](/editor/scene-editor/game-objects/common-object-properties#lists-properties)
* [Transform properties](/editor/scene-editor/game-objects/common-object-properties#transform-properties)
* [Origin properties](/editor/scene-editor/game-objects/common-object-properties#origin-properties)
* [Flip properties](/editor/scene-editor/game-objects/common-object-properties#flip-properties)
* [Visible property](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/common-object-properties.md#visible-property)
* [Alpha properties](/editor/scene-editor/game-objects/common-object-properties#alpha-properties)
* [Animation properties](/editor/scene-editor/game-objects/common-object-properties#animation-properties)
* [Texture property](/editor/scene-editor/game-objects/common-object-properties#texture-property)

---
