# 平铺精灵（TileSprite） {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/tile-sprite-object)

砖块螺旋形是一个内置的 Phaser对象类型: [Phaser.GameObjects.TileSprite](/api/class/gameobjects-tilesprite)。该类型允许创建带有重复纹理的物体,如背景元素。

使用 [tileSprite factory](/api/class/gameobjects-gameobjectfactory#tileSprite) 创建了 拖拉丝 。 [scene compiler](/editor/scene-editor/scene-compiler) 就是这样生成 拖拉丝 的 代码 :

```javascript
// x = 0, y = 600, width = 600, height = 800, texture = "rocks_1"
const rocks = this.add.tileSprite(0, 600, 800, 225, "rocks_1");
```

要在现场创建一个Tile Sprite对象,可以在现场投放一个TileSprite内置块.

![Create default TileSprite object.](https://cdn.phaser.io/editor-docs/scene-editor-tile-sprite-block-09252020.webp)

或者说 [convert an Image or Sprite into a Tile Sprite](/editor/scene-editor/game-objects/replace-object-type).


## 砖石属性 {#tile-sprite-properties}

平面闪电筒类型与其他对象类型共享属性 :

* [Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties)
* [Lists properties](/editor/scene-editor/game-objects/common-object-properties#lists-properties)
* [Transform properties](/editor/scene-editor/game-objects/common-object-properties#transform-properties)
* [Origin properties](/editor/scene-editor/game-objects/common-object-properties#origin-properties)
* [Size properties](/editor/scene-editor/game-objects/common-object-properties#size-properties)
* [Flip properties](/editor/scene-editor/game-objects/common-object-properties#flip-properties)
* [Visible property](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/common-object-properties.md#visible-property)
* [Alpha properties](/editor/scene-editor/game-objects/common-object-properties#alpha-properties)
* [Texture property](/editor/scene-editor/game-objects/common-object-properties#texture-property)

但也有特殊属性:

![Tile sprite object.](https://cdn.phaser.io/editor-docs/scene-editor-tile-sprite-props-04152020.webp)
* [width](https://phaser.io/oss/docs/api-documentation/class/gameobjects-tilesprite.md#width)和[height](https://phaser.io/oss/docs/api-documentation/class/gameobjects-tilesprite.md#height)大小属性。如果对象的大小大于原始纹理,则对象会重复纹理。您可以在检查器视图中修改这些属性或使用[Resize manipulator tool](/editor/scene-editor/manipulation-tools#resize-tool):按`Z`键,或在上下文菜单中选择**工具** = **Resize Tool**。
* [tilePositionX](/api/class/gameobjects-tilesprite#tilePositionX)和[tilePositionY](/api/class/gameobjects-tilesprite#tilePositionY)的属性,它会改变原始纹理渲染的偏移。您可以在监察官视图中修改它 。
* [tileScaleX](/api/class/gameobjects-tilesprite#tileScaleX)和[tileScaleY](/api/class/gameobjects-tilesprite#tileScaleY)的属性,它改变原始纹理渲染的尺度(而不是对象的尺度),可以在检查器视图中修改它。

---
