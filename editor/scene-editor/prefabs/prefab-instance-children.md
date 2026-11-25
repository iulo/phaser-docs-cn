# 为预制体实例添加子对象 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/prefabs/prefab-instance-children)

Phaser编辑器的v3.35.0可以将孩子添加到预制体实例中。当然,它应该是图层或容器预制体实例。

对于后向兼容性, 默认情况下, 这种行为在预制体中被禁用。 您应该在 [Children properties section](/editor/scene-editor/game-objects/common-object-properties#children-properties) 中启用, 设置在 ALLOW 附加子对象** 参数上。 这意味着您必须在容器或图层预制体或嵌入预制体参数中检查该参数 。

这是一个用于创建可重复使用的对象的方便功能。 让我们看看下一个示例 。

我们要创建一个可重用对话框对象, 用于显示 *Level Complete* 对话框或 *Game 暂停* 对话框 。

我们创建了一个**DialogPrefab**,其基本结构是:**背景**图像和关闭按钮。除了结构外,它还有一个基本行为:它从屏幕底部产生动画,如果点击**close**按钮,它就会关闭对话框:

![Basic dialog](https://cdn.phaser.io/editor-docs/prefab-children-basic-dialog-20221004.webp)

某些考虑:

* 允许在预制体中添加新的子对象,我们应检查** Allow Append子对象** 参数。
* 也许我们想改变 预制体中**近**按钮的纹理, 所以我们把它做成一个嵌套式预制体。

现在让我们创建**LevelCompleteDialogPrefab**。这是一个新预告,是**DialogPrefab**的变体。这意味着`LevelCompleteDialogPrefab`类扩展了`DialogPrefab`类。在这个新的对话框中,我们添加了**LevelComple** 消息和三颗奖励星,并更改了**close** 按钮的纹理(改为绿色 ) 。

![The Level Complete dialog prefab](https://cdn.phaser.io/editor-docs/prefab-children-level-complete-dialog-20221004.webp)

注意新**levelCompleteRibbon**,以及新**Star1**,**Star2**,**Star3**物体都是一个“DialogPrefab”前身实例的子对象。在以前的版本中,由于获得类似结构,你必须用新容器包装一个“DiallogPrefab”。但是现在,你可以在同一前身中添加新的孩子,同时,它继承了“Dialogprefab”的行为。它不需要任何手动的行为授权。

![Structure of the Complete Level prefab.](https://cdn.phaser.io/editor-docs/prefab-children-level-complete-dialog-outline-20221004.webp)

因此,我们获得`LevelCompletePrefab`级的以下代码:          ,       .

```javascript
class LevelCompleteDialogPrefab extends DialogPrefab {

constructor(scene: Phaser.Scene, x?: number, y?: number) {
super(scene, x ?? 400, y ?? 303);

this.closeButton.setTexture("Button Pack - Green_Button Green - Close");

// levelCompleteRibbon
const levelCompleteRibbon = scene.add.image(0, -30, "Casual Game GUI_Attribute - Ribbon Green");
levelCompleteRibbon.scaleX = 0.5;
levelCompleteRibbon.scaleY = 0.5;
this.add(levelCompleteRibbon);

// star1
const star1 = scene.add.image(-89, 81, "Casual Game GUI_Icon - Star Yellow");
star1.scaleX = 0.5;
star1.scaleY = 0.5;
star1.angle = -10;
this.add(star1);

// star2
const star2 = scene.add.image(-2, 71, "Casual Game GUI_Icon - Star Yellow");
star2.scaleX = 0.5;
star2.scaleY = 0.5;
this.add(star2);

// star3
const star3 = scene.add.image(85, 81, "Casual Game GUI_Icon - Star Yellow");
star3.scaleX = 0.5;
star3.scaleY = 0.5;
star3.angle = 10;
this.add(star3);
}
}
```

照同样的模式,我们可以创建一个“PauseDialogPrefab” :

![Game paused prefab](https://cdn.phaser.io/editor-docs/prefab-children-game-pause-dialog-20221004.webp)

---
