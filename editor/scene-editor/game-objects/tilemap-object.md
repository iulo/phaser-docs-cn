# 瓦片地图 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/tilemap-object)

[Tilemap](/editor/scene-editor/game-objects/tilemap-object)是一种内置的Phaser类型:[Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap)。它不是一个显示对象,只是存储地图的数据。显示地图是用[TilemapLayer objects](/editor/scene-editor/game-objects/tilemap-layer-object)添加到场景的。

场景编辑器只支持由[Tiled](https://www.mapeditor.org)(流行的第三方工具)与[JSON format](https://doc.mapeditor.org/en/stable/manual/export/#json)创建的地图. 自Phaser v3.50起,支持以下地图方向: 向正弦, 异构, 六角形, 和Stagggered.

工作流程如下:

* 以 [Tiled](https://www.mapeditor.org) 创建地图 。
* 使用 JSON 格式导出地图 。
* 使用资源包编辑器将地图(和砖块图像)导入 Phaser编辑器.
* 在场景编辑器中创建 [Tilemap](/editor/scene-editor/game-objects/tilemap-object)对象(和 TilemapLayer 对象) 。

要创建 [Tilemap](/editor/scene-editor/game-objects/tilemap-object) 对象,您可以从块视图中拖动 ** tilemap ** 元素并将其丢入场景:

![Drop Tilemap type into the scene.](https://cdn.phaser.io/editor-docs/scene-editor-add-tilemap-1-10152020.webp)

它立即显示一个向导来配置 Tilemap 。 此向导显示三页 :

* 选择图片键的页面(定义在资源包编辑器中).
* 指定图像到图片的页 。
* 选择一个与图版一起创建的图版层的页面。 但此页是可选的 。

第一步是选择 ** Tilemap 键**。 它与您在资源包编辑器中导入 [Tiled](https://www.mapeditor.org) JSON 映射时所用的键相同 :

![Select the tilemap key.](https://cdn.phaser.io/editor-docs/scene-editor-add-tilemap-2-10152020.webp)

然后,向导会显示牌匾的名称,您必须选择每个牌匾的图像。 选择一个牌匾, 并点击 **Set Tileset 图像** 按钮。 它打开一个对话框, 与资源包文件中定义的所有图像( 和图示表) 。 另外, 您还可以双击牌匾名称打开对话框 :

![It shows the name of the tilesets.](https://cdn.phaser.io/editor-docs/scene-editor-add-tilemap-3-10152020.webp)![Select the image for each tileset.](https://cdn.phaser.io/editor-docs/scene-editor-add-tilemap-4-10152020.webp)

当设置了所有平板图像时, 启用了 **Finnish ** 按钮。 单击它来完成进程。 或者您可以继续到下一页选择一个平板层。 在这种情况下, 将创建一个新的平板层和 [Tilemap Layer](/editor/scene-editor/game-objects/tilemap-layer-object) 。

![Select the image for each tileset.](https://cdn.phaser.io/editor-docs/scene-editor-add-tilemap-5-10152020.webp)

由于[Tilemap](/editor/scene-editor/game-objects/tilemap-object)不是显示对象,所以在现场,其他的图景中,与瓦片一起显示:

![Tilemap object in the Outline view.](https://cdn.phaser.io/editor-docs/scene-editor-tilemap-outline-10152020.webp)

当您选择 [Tilemap](/editor/scene-editor/game-objects/tilemap-object) 时, 检查器视图会显示其一些属性 :

![Tilemap properties.](https://cdn.phaser.io/editor-docs/scene-editor-tilemap-properties-10152020.webp)

另外,如果选择了平板,检查器视图显示其属性和修改相关图像的选择:

![image](https://cdn.phaser.io/editor-docs/scene-editor-tileset-image-property-10152020.webp)

[Tilemap](/editor/scene-editor/game-objects/tilemap-object) 对象由 [scene compiler](/editor/scene-editor/scene-compiler) 使用该 [tilemap](/api/class/gameobjects-gameobjectfactory#tilemap) 厂房。而砖块图像是使用 [Tilemap.addTilesetImage](/api/class/tilemaps-tilemap#addTilesetImage) 方法 :

```javascript
// super_mario_1
const super_mario_1 = this.add.tilemap("super-mario_1");
super_mario_1.addTilesetImage("SuperMarioBros-World1-1", "super-mario");
```

默认情况下, [Tilemap](/editor/scene-editor/game-objects/tilemap-object) 是一个用 [CLASS scope](/editor/scene-editor/game-objects/common-object-properties#scope-property) 创建的。 它意味着, 生成一个字段代码来引用对象, 这样您就可以手动配置地图的其他方面, 或者手动创建层 :

```javascript
this.super_mario_1 = super_mario_1;
```

然而,为了创建层,您在场景编辑器中得到了[TilemapLayer objects](/editor/scene-editor/game-objects/tilemap-layer-object)的支持,下一节对此有解释.

---
