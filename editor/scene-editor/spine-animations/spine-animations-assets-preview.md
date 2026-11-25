# 预览 Spine 资源 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/spine-animations/spine-animations-assets-preview)

Phaser编辑器中存在不同的上下文,其中有[Spine](https://esotericsoftware.com)资源,您可以预览: 在[Asset Pack Editor](/editor/asset-pack-editor/intro)和场景编辑器的块视图中.

对于显示和检查Spine 游戏对象, [Spine Phaser runtime](https://esotericsoftware.com/spine-phaser)需要骨架数据文件和地图集文件。如果遵循默认的 [Spine](https://esotericsoftware.com) 资源 [naming rules](/editor/scene-editor/spine-animations/spine-animations-loading#spine-assets-default-naming-rules), 那么 Phaser 编辑器可以构建骨架实例并预览它们 。

在下面的章节中,我们详细解释。

## 预览斯皮尔地图集资源 {#preview-spine-atlas-assets}

[Asset Pack Editor](/editor/asset-pack-editor/intro)显示您在 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 中添加的 [Spine](https://esotericsoftware.com) 地图集资源。 如果您在编辑器中选中它, 检查器视图会显示所有地图集框架 :

![Atlas preview](https://cdn.phaser.io/editor-docs/spine-animations-atlas-preview-20230924.webp)

## 预览斯宾骨架和动画数据 {#preview-spine-skeleton-and-animation-data}

您可以在 [Asset Pack Editor](/editor/asset-pack-editor/intro) 或 Scene 编辑器的块视图中选择一个 [Spine](https://esotericsoftware.com) 骨架数据。 在这两种情况下, 检查器视图显示两个属性部分: ** Spine Skeleton ** 和 ** Spine Preview ** 。

** Spine Skeleton ** 显示 ** Skeleton 键 ** 和 ** 预览 Atlas 键 ** 。 默认它从骨架键中猜测地图集键, 但如果需要, 您可以更改它 。

![Skeleton assets info](https://cdn.phaser.games/oss-docs/assets/b39e96846b331a1a-spine-animations-skeleton-asset-preview-.webp)

** Spine Preview** 部分显示骨架数据中定义的皮肤:

![Displays the skins of a skeleton data.](https://cdn.phaser.io/editor-docs/spine-animations-skeleton-skins-preview-20230924.webp)

## 预览斯宾卡动画 {#preview-spine-animations}

注意到 ** Spine Skeleton ** 部分包含一个 ** 预览动画 ** 按钮。 它打开了 ** Spine 预览 ** 对话框 。

在这个对话框中,你可以播放骨架动画,并改变皮肤等其他属性.

![Skeleton preview dialog](https://cdn.phaser.games/oss-docs/assets/e69525214608a183-spine-animations-skeleton-preview-dialog.webp)

让我们用参数来参数化。

### 皮肤预览 {#skin-preview}

您可以在 ** 皮肤** 按钮中按下 :

![Change skin](https://cdn.phaser.io/editor-docs/spine-animations-asset-preview-dialog-skin-20230924.webp)

### 动画和音轨 {#animation-and-track}

使用 [Spine](https://esotericsoftware.com) ,您可以在不同的音轨上同时播放动画。使用 ** Track ** 按钮,您可以选择播放您在 ** 动画 ** 按钮中选择的动画的音轨 ID 。

在下一张画面中,可以看到它正在播放**idle**动画在**Track 0**,而**shot**动画在**track 1**.

![Tracks](https://cdn.phaser.io/editor-docs/spine-animations-assets-preview-dialog-track-20230924.webp)

当您在 ** 动画 ** 按钮中选择动画时, 它会立即在选中的音轨上播放 :

![Select the animation.](https://cdn.phaser.io/editor-docs/spine-animations-preview-assets-dialog-animation-20230924.webp)

如果选中 ** Loop ** 参数, 动画会以循环播放 。

如果选中了 ** Events ** 参数, 那么画布会显示动画所显示的事件名称。 请在此图像中查看 ** footstep ** 事件 :

![Events.](https://cdn.phaser.io/editor-docs/spine-animations-preview-dialog-events-20230924.webp)

另外,还可以设置动画的**Default Mix**和**Time Scale**. **Default Mx**在从一个动画转换到另一个动画时应用.

[Learn more about applying animations in the Spine Phaser runtime](http://esotericsoftware.com/spine-phaser#Applying-Animations)

## 动画事件 {#animation-events}

动画事件部分显示当前动画所释放的事件列表, 显示事件的时间和名称 。

![animation event table](https://cdn.phaser.games/oss-docs/assets/731fdb5fe28cfb57-spine-animations-preview-dialog-events-t.webp)

---
