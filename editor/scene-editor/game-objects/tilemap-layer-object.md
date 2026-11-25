# 瓦片地图图层（TilemapLayer） {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/tilemap-layer-object)

** 平面图层** 是显示基于平面图的映射对象。有两个 Phaser 用于此的内建类型, 即 [StaticTilemapLayer](https://phaser.io/oss/docs/api-documentation/class/tilemaps-statictilemaplayer.md) 和《公约》第2条 [DynamicTilemapLayer](https://phaser.io/oss/docs/api-documentation/class/tilemaps-statictilemaplayer.md).

主要区别在于静态层只读但更快,同时可以修改动态层的瓦片.

要创建平面层, 首先, 您必须使用 [create a Tilemap object](/editor/scene-editor/game-objects/tilemap-object)。 然后, 您可以从 Blocks 视图中拖动 ** StaticTilemapLayer ** 或 ** DynamicTilemapLayer ** 并将其丢入现场 :

![Adding a tilemap layer.](https://cdn.phaser.io/editor-docs/scene-editor-add-tilemap-layer-1-10152020.webp)

场景编辑器不支持空的图片层,您必须选择在场景中创建的图片中定义的层之一:

![Selecting the layer.](https://cdn.phaser.io/editor-docs/scene-editor-add-tilemap-layer-2-10152020.webp)

片面上显示:

![The layer is created in the scene.](https://cdn.phaser.io/editor-docs/scene-editor-add-tilemap-layer-2310152020.webp)

当你拯救现场, [scene compiler](/editor/scene-editor/scene-compiler) 使用 [createStaticLayer](https://phaser.io/oss/docs/api-documentation/class/tilemaps-tilemap.md#createstaticlayer) 或 或 时 间 [createDynamicLayer](https://phaser.io/oss/docs/api-documentation/class/tilemaps-tilemap.md#createdynamiclayer) 方法, 方法, 方法, 方法, 方法, 方法, 方法, 方法, 方法。

在下一个代码中,创建了一个新的静态层,使用`World1`层数据和`SuperMarioBros-World1-1`的砖块:

```javascript
// world1
super_mario_1.createStaticLayer("World1", ["SuperMarioBros-World1-1"], 107, 110);
```

层只使用图案定义的片段。编译器扫描了层的所有片段,仅将片段中引用的片段的名称作为参数。

平面图层有很多实用方法和属性,所以你可能想通过设置其字段来指定它. [variable scope](/editor/scene-editor/game-objects/common-object-properties#scope-property) 改为: `Class`.

当您选择一个图片层时, 检查器视图会显示该层的一些属性( 所有属性都是只读的 ):

![Tilemap layer properties.](https://cdn.phaser.io/editor-docs/scene-editor-tilemap-layer-properties-2310152020.webp)

另外,由于它是一个显示对象,所以还有其他常见的属性:

* [Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties)
* [Lists properties](/editor/scene-editor/game-objects/common-object-properties#lists-properties)
* [Transform properties](/editor/scene-editor/game-objects/common-object-properties#transform-properties)
* [Visible property](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/common-object-properties.md#visible-property)

---
