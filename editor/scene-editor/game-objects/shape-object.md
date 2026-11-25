# 形状 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/shape-object)

形状对象是几何显示对象。您可以将它们添加到场景、容器或组合中。

所有形状对象扩展 [Phaser.GameObjects.Shape](/api/class/gameobjects-shape) 类并共享这些共同属性 :

* [Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties)
* [Lists properties](/editor/scene-editor/game-objects/common-object-properties#lists-properties)
* [Transform properties](/editor/scene-editor/game-objects/common-object-properties#transform-properties)
* [Origin properties](/editor/scene-editor/game-objects/common-object-properties#origin-properties)
* [Size properties](/editor/scene-editor/game-objects/common-object-properties#size-properties)
* [Visible property](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/common-object-properties.md#visible-property)
* [Alpha properties](/editor/scene-editor/game-objects/common-object-properties#alpha-properties)

但他们有以下属性:

![Shape properties.](https://cdn.phaser.io/editor-docs/scene-editor-shape-properties-11092020.webp)
* [Is Filled](/api/class/gameobjects-shape#isFilled): 如果此形状是否填充的话控制。 请注意, 有些形状不支持填充( 如行形状) 。
* [Fill Color](/api/class/gameobjects-shape#fillColor): 此形状所用的填充颜色 。
* [Fill Alpha](/api/class/gameobjects-shape#fillAlpha):这个形状所用的填充值α.
* [Is Stroked](/api/class/gameobjects-shape#isStroked): 如果此形状是否被中键控制。 请注意, 有些形状不支持被中键( 如 Iso Box 形状) 。
* [Stroke Color](/api/class/gameobjects-shape#strokeColor): 此形状所用的描边颜色 。
* [Stroke Alpha](/api/class/gameobjects-shape#strokeAlpha):此形状所用的中风α值.
* [Line Width](/api/class/gameobjects-shape#lineWidth):这个形状所用的中风线宽.

---
