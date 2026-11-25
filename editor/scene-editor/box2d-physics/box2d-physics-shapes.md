# Box2D 碰撞形状 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/box2d-physics/box2d-physics-shapes)

Box2D 形状是 Box2D 物理体的构件。您可以创建形状并将其添加到 Box2D 体内。形状定义了物理体的物理属性,如质量、摩擦和还原。

Phaser编辑器为您提供了创建和调整外观形状的工具,尽管它尚未覆盖所有外观类型.

要将形状添加到一个物理体中,请选择场景(或图景)中的物理体,并激活上下文菜单(右键点击)**Box2D Physics**,并选择其中之一来添加形状:

![Add shape to body](https://cdn.phaser.games/oss-docs/assets/43f675bc25573df3-box2d-add-shape-menu-20250214.webp)

另一种添加形状的方法来自检查器视图中的 **Box2D 物理体形状** 部分。此部分显示所有物理体形状的快捷键加一个按钮来添加新形状 :

![Box2D body shapes section](https://cdn.phaser.games/oss-docs/assets/bcb53bf804251c75-box2d-shapes-section-20250214.webp)

快捷键的目的是可以在检查器视图中选择一个形状并编辑其属性.

## 形状为独立对象 {#shapes-as-independent-objects}

形状与物理体一样,独立于游戏对象和实体本身。您可以在“大纲”视图中选择一个形状,并在“督察”视图中编辑其属性。

您也可以使用 [assign a variable](/editor/scene-editor/game-objects/common-object-properties#variable-properties) 来查看一个形状, 并从 Phaser 编辑器生成的代码中访问它。 也可以把它宣布为嵌套预制体文件。 虽然对于 [the reasons explained in the previous section](/editor/scene-editor/box2d-physics/box2d-physics-add-body#box2d-body-as-nested-prefab)来说, 您暂时无法修改其属性 。

## 所有形状的共有属性 {#properties-common-to-all-shapes}

所有形状类型都有共同的属性,可以在检查器视图中的**Box2D形状**部分中编辑:

![Shape properties](https://cdn.phaser.games/oss-docs/assets/1a2a3ca54ac07489-box2d-shape-properties-20250214.webp)

还有一些其它的属性是一组形状共同的,我们将看到这些属性的下个特征.

## 形状中心属性 {#shape-center-properties}

一些形状,如圆形和偏移箱,可以用从体中心中取出的偏移来居中。您可以在检查器视图中的 **Box2D 形状中心** 部分编辑中心属性 :

![Center properties](https://cdn.phaser.games/oss-docs/assets/09f3080595961729-box2d-center-section-20250214.webp)

另外,还可以使用[Translate tool](/editor/scene-editor/manipulation-tools#translate-tool)来改变这些属性.

## 形状角度属性 {#shape-angle-property}

一组形状可以围绕物理体中心或自身中心旋转。 您可以编辑检查器视图中 ** Box2D 形状角** 部分中的角度属性 :

![Shape angle property](https://cdn.phaser.games/oss-docs/assets/6d38a76a6b11b00d-box2d-shape-angle-section-20250214.webp)

您也可以使用 [Rotate tool](/editor/scene-editor/manipulation-tools#rotate-tool) 更改角度 。

## 形状大小属性 {#shape-size-properties}

有些形状具有大小属性,或者说, 半大小属性。 您可以在检查器视图中的 ** Box2D 形状大小** 部分编辑这些属性 :

![Shape size properties](https://cdn.phaser.games/oss-docs/assets/bf8cc8f1734d22c6-box2d-shape-size-properties-20250214.webp)

也可以使用[Resize tool](/editor/scene-editor/manipulation-tools#resize-tool)更改大小.

## 框形状 {#box-shape}

Box 形状是一个长方形,宽度和高度。您可以在 [Size section](#shape-size-properties) 或用 [Resize tool](/editor/scene-editor/manipulation-tools#resize-tool) 编辑大小属性 。

![Box shape](https://cdn.phaser.games/oss-docs/assets/7c4cfb8723a63858-box2d-box-shape-20250215.webp)

## 偏移框形状 {#offset-box-shape}

偏移箱形状是一个长方形,宽度和高度均匀,但可以由物理体中心抵消,旋转。您可以在 [Center section](#shape-center-properties) 或与 [Translate tool](/editor/scene-editor/manipulation-tools#translate-tool),并用 [Angle section](#shape-angle-property) 或与 [Rotate tool](/editor/scene-editor/manipulation-tools#rotate-tool).

![Offset Box shape](https://cdn.phaser.games/oss-docs/assets/9b35bbbd532c7320-box2d-offset-box-shape-20250215.webp)

## 圆形 {#circle-shape}

圆形是一个半径和中心圆形,可以编辑**拉迪乌斯区**或[Resize tool](/editor/scene-editor/manipulation-tools#resize-tool)中的半径属性,也可以编辑[Center section](#shape-center-properties)或[Translate tool](/editor/scene-editor/manipulation-tools#translate-tool)中的中心属性.

![Circle shape](https://cdn.phaser.games/oss-docs/assets/8813ee8e9716017b-box2d-circle-shape-20250215.webp)

## 多边形形状 {#polygon-shape}

多边形形状是一个多边形,有顶点列表和半径。 您可以编辑 ** Polygon 部分** 中的顶点, 或者使用 [visual Polygon tool](/editor/scene-editor/manipulation-tools#polygon-tool) :

![Polygon shape](https://cdn.phaser.games/oss-docs/assets/c55c553b29957c07-box2d-polygon-shape-20250215.webp)

## 偏移多边形形状 {#offset-polygon-shape}

同样的 [Polygon](#polygon-shape) 形状,但带有中心偏移和旋转。您可以在 [Center section](#shape-center-properties) 或与 [Translate tool](/editor/scene-editor/manipulation-tools#translate-tool),并用 [Angle section](#shape-angle-property) 或与 [Rotate tool](/editor/scene-editor/manipulation-tools#rotate-tool).

![Offset polygon shape](https://cdn.phaser.games/oss-docs/assets/1138a41dfe0d3215-box2d-offset-polygon-shape-20250215.webp)

## 盖状形状 {#capsule-shape}

Capsule 形状是一个半径和两个中心点的胶囊。 您可以编辑 ** Box2D Capsule 元件部分中的属性** :

![Capsule shape](https://cdn.phaser.games/oss-docs/assets/06709450663a32f7-box2d-capsule-shape-20250215.webp)

## 嵌套预制体箱形状 {#a-box2d-shapes-as-nested-prefab}

通常配置Box2D形状的方法是通过构造器中我们通过的配置对象。为此,嵌入的形状预制体体需要特殊的方法来修改其属性。我们称之为**xargs**。您可以在[The nested prefab constructor and the xargs](/editor/scene-editor/prefabs/prefab-nested#the-nested-prefab-constructor-and-the-xargs)区中更多地了解**xargs **。

---
