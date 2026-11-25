# 位图文本（BitmapText） {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/bitmap-text-object)

[Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext)在Phaser游戏开发中被广泛使用,用于显示文本.

您可以以两种方式创建 [Bitmap Text](/editor/scene-editor/game-objects/bitmap-text-object) 对象 :

* 拖动一个 BitmapText 内置块并丢到现场.
* 从块视图中拖取一个 [BitmapFontFile](/api/class/loader-filetypes-bitmapfontfile)键,并丢入现场。 [BitmapFontFile](/api/class/loader-filetypes-bitmapfontfile)应该出现在 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file)中 。
  ![Drop BitmapFont key to create a BitmapText object.](https://cdn.phaser.io/editor-docs/scene-editor-bitmap-text-12212020.webp)

[Bitmap Text](/editor/scene-editor/game-objects/bitmap-text-object)对象在代码中使用[bitmapText factory](/api/class/gameobjects-gameobjectfactory#bitmapText)创建:

```javascript
this.add.bitmapText(100, 150, "desyrel", "Hello bitmap text!", 70, 0);
```
## 位图文本属性 {#the-bitmap-text-properties}

[Bitmap Text](/editor/scene-editor/game-objects/bitmap-text-object)型包含许多[common object properties](/editor/scene-editor/game-objects/common-object-properties):

* [Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties)
* [Lists properties](/editor/scene-editor/game-objects/common-object-properties#lists-properties)
* [Transform properties](/editor/scene-editor/game-objects/common-object-properties#transform-properties)
* [Origin properties](/editor/scene-editor/game-objects/common-object-properties#origin-properties)
* [Flip properties](/editor/scene-editor/game-objects/common-object-properties#flip-properties)
* [Visible property](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/common-object-properties.md#visible-property)
* [Alpha properties](/editor/scene-editor/game-objects/common-object-properties#alpha-properties)

也包含[Text property](/editor/scene-editor/game-objects/common-object-properties#text-property),它专门用于所有有文本的对象,及其具体属性:

* [font](/api/class/gameobjects-bitmaptext#font)属性显示 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file)中 BitmapFont 的键。 要更改字体, 请点击按钮。 它打开 ** 选择 Bitmap 字体** 对话框 。
  ![Select Bitmap Font dialog.](https://cdn.phaser.io/editor-docs/scene-editor-select-bitmap-font-dialog-12212020.webp)
* 电话 [fontSize](/api/class/gameobjects-bitmaptext#fontSize) 属性。
* 电话 [align](/api/class/gameobjects-bitmaptext#align) 属性。
* 电话 [letterSpacing](/api/class/gameobjects-bitmaptext#letterSpacing) 属性。
* [dropShadow](/api/class/gameobjects-bitmaptext#setDropShadow)相关的属性.

---
