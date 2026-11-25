# 添加 Box2D 物理体 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/box2d-physics/box2d-physics-add-body)

Box2D体是Phaser游戏对象的独立对象,可以将其添加到一个场景中,或者与游戏对象关联.

要在场景中添加一个Box2D体,你有两种选择:

1. 将 B2Body 块从 Blocks 视图中拖出, 并丢入现场:
![Drop body](https://cdn.phaser.games/oss-docs/assets/1656696e9ccf015a-box2d-drop-body-blodk-20250214.webp)
2. 打开场景上下文菜单(右键点击),并选择 **Box2D Physics ** → ** Add Body To Scene ** 选项:
![Add body to scene](https://cdn.phaser.games/oss-docs/assets/f6333ee16d9effe5-box2d-add-body-to-scene-20250214.webp)

要将一个正体添加到 Phaser 游戏对象中,您必须先选择场景中的对象,然后从上下文菜单中激活 ** Box2D Physics ** → ** Add Body To Sprite ** 选项 :
![Add body to [sprite](https://cdn.phaser.games/oss-docs/assets/841c5a006e8f7c87-box2d-add-body-to-sprite-20250214.webp)

物理体一进入现场,您就可以在督察视图中编辑其属性:

![Body properties](https://cdn.phaser.games/oss-docs/assets/3412c0c369b76d95-box2d-body-properties-20250214.webp)

## Box2D 物理体转换属性 {#box2d-body-transform-properties}

由于Box2D机身独立于Phaser游戏对象,因此它们具有位置和旋转性,但是,如果机身附着在游戏对象上,机身的位置与游戏对象的位置同步,因此这些字段被禁用.

[Translate](/editor/scene-editor/manipulation-tools#translate-tool)和[Rotate](/editor/scene-editor/manipulation-tools#rotate-tool)操纵工具也可用于Box2D机构,这是调整机构位置和旋转的有效方法. 如上所述,**Translate**只能用于与游戏对象无关的机构.

以下图像显示一个与游戏对象无关的静态体,可视它对应两个形成平台的石块,但在场景中,物理体独立于这些块: 平面图 平面图 图片 平面图 地图 平面图 图像 平面图 画面 平面图 显示平面图 平形图 平面图

![Body in scene](https://cdn.phaser.games/oss-docs/assets/a1e8eb26a1748553-box2d-body-in-scene-20250214.webp)

![Body in outline view](https://cdn.phaser.games/oss-docs/assets/fcc99f9787f2d3b7-box2d-body-independent-from-gameobjects-.webp)

## Box2D 主体为变量 {#box2d-body-as-a-variable}

对于Phaser编辑器,一个Box2D体不是游戏对象,而是场景中与游戏对象共享许多特性的物体:

- 它们是一个独立对象。
- 您可以为它指定一个范围和名称,因此编辑器生成代码来访问它们,例如字段和临时变量.
- 虽然你不能创建Box2D体的预制体体,但可以宣布它们为巢预制体体.
- [Variable](/editor/scene-editor/game-objects/common-object-properties#variable-properties)部分由游戏对象和Box2D体共同使用.

## 箱形2D 体形为嵌入式前置 {#box2d-body-as-nested-prefab}

通常配置Box2D 物理体的方法是通过构造器中我们通过的配置对象。为此,嵌入体的预制体体需要特殊的方法来修改其属性。我们称之为**xargs**。您可以在[The nested prefab constructor and the xargs](/editor/scene-editor/prefabs/prefab-nested#the-nested-prefab-constructor-and-the-xargs)区中更多地了解**xargs **。

---
