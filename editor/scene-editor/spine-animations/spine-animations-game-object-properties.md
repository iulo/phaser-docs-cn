# Spine 游戏对象属性 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/spine-animations/spine-animations-game-object-properties)

检查器视图显示您在现场选择的 [SpineGameObject](/editor/scene-editor/spine-animations/spine-animations-game-object) 实例的属性 。

**Spine**部分显示的是**Data键**,**Atlas键**,以及**Skin**名称.

您可以按 ** 配置 ** 按钮重新配置这些值。 它显示一个配置对话框, 您可以选择骨架、 地图集和皮肤 :

![Configuring the skeleton, atlas, and skin of a game object.](https://cdn.phaser.games/oss-docs/assets/ae437ba5b1478ac9-spine-animations-game-object-config-2025.webp)

这是改变物体骨架和地图图的唯一方法, 但你可以在 ** Skin ** 参数中直接改变皮肤:

![Skin property](https://cdn.phaser.games/oss-docs/assets/84ede3ebfb6d02d7-spine-animations-game-object-skin-proper.webp)

** Data 键** 和 ** Atlas 键** 属性只能通过构造器设置到Spine 游戏对象上。为此原因,场景编译器使用 e special **xargs ** 参数将这些属性设置在嵌入的预制体上. [Learn more about the xargs](/editor/scene-editor/prefabs/prefab-nested#the-nested-prefab-constructor-and-the-xargs).

## 约束提供者属性 {#bounds-provider-properties}

边框提供者负责计算 [SpineGameObject](/editor/scene-editor/spine-animations/spine-animations-game-object) 的大小。默认情况下,它使用设置的姿势边框。边框有两个内置执行: **SetupPoseBounds Provider **(默认)和 **SkinsAndimation Bonds Provider**。

检查器视图中的 ** Spine** 部分包含设定游戏对象的边框参数 :

![Bounds provider section](https://cdn.phaser.games/oss-docs/assets/85100ba05eac3333-spine-animations-bounds-provider-2025030.webp)

您选择了**BP Type** 的边框提供者类型: **SETUP_POSE** (`SetupPoseBoundsProvider``或**SKINS_AND_ANMIMATION**(英语:`SkinsAndAnimationBoundsProvider`).

其他参数只有在您选择 **SKINS_AND_ANIMATION** 的边框提供者时才有效。此提供者使用动画和一系列的外观来计算边框。

您可以在 **BP 皮肤** 参数中为边框提供者选择皮肤。 它会给你两个选项: ** CURRENT ** (在游戏对象中使用当前皮肤) 或 **ALL ** (使用游戏对象骨架数据中所有可用的皮肤) 。

使用 **BP 动画** 参数, 您可以选择用于边框提供者的动画。 它列出骨架数据中可用的所有动画 。

![Bounds provider animation.](https://cdn.phaser.games/oss-docs/assets/810d85b1c1d361d9-spine-animations-object-bounds-provider-.webp)

使用**BP时间步**参数,您可以设定计算边距大小的算法精度。一个较小的时间步意味着更精度,但计算速度更慢。

## 动画属性 {#animations-properties}

**Spine动画**部分包含动画属性.

![Animation properties](https://cdn.phaser.io/editor-docs/spine-animations-object-animation-properties-20230925.webp)

**时间缩放倍率**: 播放动画和混音慢或快。默认 `1` 。

**默认混合**: 在两部动画之间没有定义混音时间时使用的混音时间.

**混合**: 两部动画的混音持续时间.

** 混合** 按钮显示定义的动画组合数。 点击它来编辑组合。 它打开 [Spine Game Object preview dialog](https://phaser.io/oss/docs/phaser-editor/scene-editor/spine-animations/spine-animations-game-object-properties#spinegameobject-preview) , 您可以在此编辑和预览组合 :

![Spine game object preview dialog.](https://cdn.phaser.io/editor-docs/spine-animations-object-preview-dialog-20230925.webp)

## Spine Game 对象在场预览 {#spinegameobject-in-scene-preview}

爱的爱的爱的爱 爱的爱的情的爱的爱的情 [sprite animations](/editor/scene-editor/game-objects/common-object-properties#animation-properties) y 输 者 [particle emitters](/editor/scene-editor/game-objects/particle-emitter-object-properties#preview-properties), también puedes visionizar las Spine 动画 en la propia escena del 编辑器.

要启用内景预览, 您必须首先从 ** Spine 预览** 部分中选择 ***Run 预览动画** 选项。 以下参数 ** Preview Loop**, ** Preview Time**, 和 ** Preview 动画** 仅用于内景预览, 不影响游戏中对象的状态 。

**Preview Animation ** 将选择动画预览 。 **Preview Loop** 将播放动画的循环。 **Previce Time** 将预览动画提前到给定时间, 以毫秒计。 它不需要您运行更新循环 。 在某个特定时刻获得动画的静态预览很有用 。

![Preview parameters](https://cdn.phaser.games/oss-docs/assets/0ae20e0365cc43d1-spine-animation-scene-preview-20250306.webp)

这很重要,你已经启用了[update loop in the scene editor](/editor/scene-editor/misc#play-scene-update-loop),否则预览动画不会顺利运行.

![Play the update loop](https://cdn.phaser.games/oss-docs/assets/f40d66c0f2cedaa3-spine-animations-update-loop-20250306.webp)

## spineGame 对象预览窗口 {#spinegameobject-preview-window}

您可以在 ** Spine Preview ** 部分按下 ** Preview 窗口** 按钮预览 [SpineGameObject](/editor/scene-editor/spine-animations/spine-animations-game-object) 。

![Preview Window button](https://cdn.phaser.games/oss-docs/assets/f6e6f8bf019ed1a2-spine-animations-preview-button-20250306.webp)

它打开了预览对话框,您可以在此选择动画名称,动画音轨,以及其他参数.

这个对话框与[Spine Preview dialog](/editor/scene-editor/spine-animations/spine-animations-assets-preview#preview-spine-animations)类似,但也允许编辑游戏对象的一些属性,如默认混音,动画混音,以及时间缩放倍率:

![Spine game object preview dialog.](https://cdn.phaser.io/editor-docs/spine-animations-object-preview-dialog-20230925.webp)

对话框有两个部分: ** 预览** 和 ** 设置** 。 预览部分有 ** 预览轨迹 ** 、 ** 预览动画 ** 、 ** 复评循环 ** 和 ** 复评事件** 参数。 它和 [Spine Preview dialog](/editor/scene-editor/spine-animations/spine-animations-assets-preview#preview-spine-animations) 一样有效, 并且不影响对象状态 。

** 设置 ** 包含 ** Time Scale ** 和 ** Default Mix ** 参数。如果您修改了这些参数并按 ** Update ** 按钮,则数值会设定到游戏对象,并在场景中坚持不变。

此外,还可以设置游戏对象的动画组合值:

![Animation mix](https://cdn.phaser.io/editor-docs/spine-animations-object-preview-mix-20230925.webp)

[Learn more about the Spine animation concepts](https://esotericsoftware.com/spine-phaser#Applying-Animations)

---
