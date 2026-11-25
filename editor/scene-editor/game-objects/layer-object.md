# 层 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/layer-object)

[Phaser.GameObjects.Layer](/api/class/gameobjects-layer)对象类型允许将对象分组。 与 [Container](/editor/scene-editor/game-objects/container-object) 对象不同, 层不能被改变。 它没有位置、 角度或尺度。 它的唯一目的是快速排序用于渲染的对象 。

[Learn more about Layers in the Phaser docs](/api/class/gameobjects-layer).

[Learn more about working with parent objects in the Scene Editor](/editor/scene-editor/working-with-parent-objects).

您可以在现场投放一个内置的图层块, 或者使用 [Create Layer with Selection](#grouping-objects-in-a-layer) 命令来创建图层 。

![Creating an empty layer.](https://cdn.phaser.io/editor-docs/scene-editor-layer-drop-into-scene-12172020.webp)

[scene compiler](/editor/scene-editor/scene-compiler)生成的代码,创建一个图层,就是这样:

```javascript
// create the layer
const layer_1 = this.add.layer();

// create an object and add it to the layer
const someObject = ... ;
layer_1.add(someObject);
```


## 将对象分组于层中 {#grouping-objects-in-a-layer}

您可以用几个对象创建一层。 您可以选择对象并执行 [Create Layer with Selection](#grouping-objects-in-a-layer) 命令。 命令可用 [Parent context menu](/editor/scene-editor/working-with-parent-objects#parent-context-menu) 。

当执行命令时,所选对象从原主对象中移除并添加到新层中。所有对象都保持相同的绝对位置。如果所有对象都是普通层的子,那么新层将添加到原主对象层中。


## 层属性 {#layer-properties}

层类型包含一些 [common object properties](/editor/scene-editor/game-objects/common-object-properties) :

* [Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties)
* [Lists properties](/editor/scene-editor/game-objects/common-object-properties#lists-properties)
* [Children properties](/editor/scene-editor/game-objects/common-object-properties#children-properties)
* [Visible property](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/common-object-properties.md#visible-property)
* [Alpha property](/editor/scene-editor/game-objects/common-object-properties#alpha-properties)

---
