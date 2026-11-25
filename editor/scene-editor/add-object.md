# 将对象添加到场景 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/add-object)

在现场中创建新对象有多种方法。 从块视图中丢弃一个资源或内置类型。 或者粘贴一个对象(包括来自其他场景的) 。

另外,在[set of rules](#automatic-parenting-of-new-objects)之后,编辑器会为新对象确定(或创建)父对象.

## 块视图集成 {#blocks-view-integration}

当场景编辑器活动时, 块视图会显示您可以进入场景并跳入的“块”, 以创建新的对象。 这些是块 :

* 内置类型. Phaser类型和其他与Phaser编辑器相关的类型.
* 资源包文件中定义的资源,如图像,图示表框,动画,脊椎动画等.
* 汝所造前法宝.

块视图中显示的第一批项目是原始对象类型,由场景编辑器支持。您可以在类型上将其拖入场景以创建类型实例,并带有默认值。

对于图像、 示意图或砖块的粘贴, 新实例中不包含纹理。 如果您想要设置对象的纹理, 您可以在 [Texture section](/editor/scene-editor/game-objects/common-object-properties#text-property) 中选择一个 。

![Add an empty image to the scene.](https://cdn.phaser.io/editor-docs/scene-editor-blocks-view--add-empty-image-02242021.webp)

然而,如果将一个图像或纹理帧投放到场景中,编辑器会创建一个新的[Image object](/editor/scene-editor/game-objects/image-object),并将掉落的纹理设定为物体的纹理.

也许,而不是一个 [Image](/editor/scene-editor/game-objects/image-object),需要创建 [TileSprite](/editor/scene-editor/game-objects/tile-sprite-object) 同样的纹理,在这种情况下,你可以只是 [convert it to a TileSprite](/editor/scene-editor/game-objects/replace-object-type).

如果你掉了一个**BitmapFont**,编辑器会创建一个[Bitmap Text](/editor/scene-editor/game-objects/bitmap-text-object).

如果你放弃了Prefab,编辑器会创建一个实例.

![Blocks view.](https://cdn.phaser.io/editor-docs/scene-editor-blocks-view-02242021.webp)

上下文菜单显示资源分组的不同选项:按类型,按资源包文件,以及文件位置:

![Grouping the assets.](https://cdn.phaser.io/editor-docs/scene-editor-blocks-view-grouping-02282021.webp)

块视图的标签显示“tab 区域”,您可以选择用于过滤内容 :

![Select different tab-sections for filtering content.](https://cdn.phaser.io/editor-docs/scene-editor-blocks-view-tab-section-03012021.webp)

注意有三种选择:

**内建**: 视图中仅显示内置类型。

**预制体**: 只显示预制体文件 。

**资源**: 仅显示资源包文件中定义的资源。

## 从上下文菜单中添加内置对象 {#add-built-in-object-from-context-menu}

场景编辑器的上下文菜单显示不同的选项来创建新的内置对象.

**Add Object**子菜单显示内置对象类型的所有类别:

![Add Object context menu.](https://cdn.phaser.io/editor-docs/scene-editor-add-object-menu-02232021.webp)

另外, **Add... ** (`A`) 选项打开了与所有内置类型的对话。 这对快速添加新对象是有好处的 :

![Add Object dialog.](https://cdn.phaser.io/editor-docs/scene-editor-add-object-dialog-02232021.webp)

## 新对象的自动父程序 {#automatic-parenting-of-new-objects}

当新对象被创建(通过丢弃块,或通过粘贴对象)时,会评价一套规则,以确定新对象的母体:

* 如果在现场中选择了对象 :
  * 如果是容器,则会添加新的对象.
  * 否则,如果它有一个父容器,那么新对象会添加到父容器中.
* 如果现场是预制体场景:
  * 如果场景为空,则会将新物体添加到场景中.
  * 如果[root object](/editor/scene-editor/prefabs/prefab-object)是一个容器,那么新的物体会加入其中.
  * 换句话说, 将创建一个新的容器, 并将新添加的旧的 [root object](/editor/scene-editor/prefabs/prefab-object) 和新添加的对象添加到新容器中。 因此, 场景将有一个新的 [root object](/editor/scene-editor/prefabs/prefab-object): 自动创建的容器 。

---
