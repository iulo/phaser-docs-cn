# 编辑动画的属性 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/animations-editor/edit-animations-properties)

这些是动画的属性:

**键**: 动画的标识符。 用于在图示中播放动画: `sprite.play("walk")`。

**帧率**: 帧每秒播放的帧率(默认为24).

**延迟**: 延迟开始重播。 数值以毫秒计 。

**重复**: 重复动画的次数(无穷无尽的1次).

**重复延迟**: 动画重现前的延迟。 数值以毫秒表示 。

**哟**: 动画Yoyo应该吗?

**启动时显示**: 动画开始播放时, should sprite. visible = true = 真实性?

**完成时隐藏**: 动画完成时应该用`sprite.visible = false`.

**跳过未选中的框架**: 如果时间滞后, 跳过框架, 还是总是向前?

默认情况下,编辑器会显示所有动画,并在检查器视图中显示所有动画的属性。然而,您可以在编辑器中点击动画,以编辑该单动画的属性。或者在大纲视图中选择几部动画。

![Edit the animations.](https://cdn.phaser.io/editor-docs/animations-edit.webp)

---
