# 创建 Spine 游戏对象 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/spine-animations/spine-animations-game-object)

[SpineGameObject](https://esotericsoftware.com/spine-phaser#SpineGameObject)是Phaser游戏对象的实现,用于显示,控制和定制[Spine](https://esotericsoftware.com)动画.

[Spine Phaser runtime](https://esotericsoftware.com/spine-phaser)提供`spine()`工厂创建[SpineGameObject](https://esotericsoftware.com/spine-phaser#SpineGameObject).

```javascript
const spineObject = this.add.spine(400, 500, "spineboy", "spineboy-atlas");
```

但你不需要写那个代码。 场景编辑器可以为你生成那个代码。 您只需要从块视图中拖动一个 [Spine](https://esotericsoftware.com) 块, 并把它丢到现场 。

也请见不同方式。


## 创建一个带有 SpineGame 内置块的 Spine 对象 {#create-a-spine-object-with-a-spinegameobject-built-in-block}

将 [SpineGameObject](https://esotericsoftware.com/spine-phaser#SpineGameObject) 添加到现场的主要方法是将 ** SpineGame Object ** 块丢到现场。 这个块位于 Blocks 视图的 ** Built - in ** 部分, 位于 ** Spine ** 文件夹下。 拖放到现场:

![Add spine game object to the scene.](https://cdn.phaser.io/editor-docs/spine-animations-add-game-object-1-20230924.webp)

它打开一个配置对话框来选择 [SpineGameObject](https://esotericsoftware.com/spine-phaser#SpineGameObject) 使用的骨架数据键和地图集键。 每个 [SpineGameObject](https://esotericsoftware.com/spine-phaser#SpineGameObject) 都需要对骨架数据和地图集的引用。 这意味着, 您首先需要 [add the skeleton data and atlas files to an Asset Pack file](/editor/scene-editor/spine-animations/spine-animations-loading)。 此外, Scue Editor 需要您选择动画的外观 。

工作流程如下:

* 选择骨架数据并按 ** Next** :

  ![Select skeleton data.](https://cdn.phaser.io/editor-docs/spine-animations-add-object-data-20230924.webp)

* 选择地图集并按 ** 下一步** :

  ![Select the atlas](https://cdn.phaser.io/editor-docs/spine-animations-add-object-atlas-20230924.webp)

* 选择皮肤并按 ** 完成** :

  ![Select the skin.](https://cdn.phaser.io/editor-docs/spine-animations-add-object-skin-20230924.webp)

* 最后,它增加了现场的[SpineGameObject](https://esotericsoftware.com/spine-phaser#SpineGameObject):

  ![Spine game object in the scene.](https://cdn.phaser.io/editor-docs/spine-animations-add-obejct-done-20230924.webp)


## 创建一个带有骨架数据块的 Spine 对象 {#create-a-spine-object-with-a-skeleton-data-block}

块视图的 ** Spine JSON ** 和 ** Spine Binary ** 部分显示所有您 [defined in the Asset Pack file](/editor/scene-editor/spine-animations/spine-animations-loading) 的骨架数据。 您可以拖动一个骨架数据块并将其丢到现场。 它显示配置对话框, 以选择地图集和皮肤, 和上一节一样。 下一张图像显示 `spineboy`z 骨架块 :

![Add a skeleton block.](https://cdn.phaser.io/editor-docs/spine-animations-add-skeleton-block-20230924.webp)


## 创建带有骨架皮肤块的Spine 游戏对象 {#create-a-spine-object-with-a-skeletons-skin-block}

如果您在 [default naming rules](/editor/scene-editor/spine-animations/spine-animations-loading#spine-assets-default-naming-rules) 之后导入了 资源包中的 骨架数据和地图集资源, 那么 Blocks 视图显示在骨架数据块中 特殊 ** skin ** 块 。

拖动此皮肤块并把它扔到现场。 它会立即创建 [SpineGameObject](https://esotericsoftware.com/spine-phaser#SpineGameObject), 而不会显示配置对话框 :

![Add the skin block.](https://cdn.phaser.io/editor-docs/spine-animations-add-object-skin-block-20230924.webp)

---
