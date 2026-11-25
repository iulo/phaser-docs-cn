# 向场景添加图像 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/first-steps/add-image-to-scene)

让我们在由** Basic JavaScript** 项目模板创建的 `Level.scene` 文件中添加一个图像 。

1. 要上传图像到工程, 请右键单击 `assets` 文件夹, 从上下文菜单中选择 ** Add 文件 ** 选项。 这将打开操作系统的文件选择器对话框 。

   ![Add files menu](https://cdn.phaser.io/editor-docs/first-steps-upload-file-20241004.webp)

   ![Native file chooser](https://cdn.phaser.io/editor-docs/first-steps-upload-file-file-chooser-20241004.webp)

2. 选择想要的图像, 如 `background.png`。 图像将上传到 `assets` 文件夹, 并显示在文件视图中 。

   ![Image in the files view](https://cdn.phaser.io/editor-docs/first-steps-upload-file-filesview-20241004.webp)

3. 保证在文件视图中选择新图像。 在检查器视图中, 您将找到图像文件的属性。 在 ** 套装包条目** 部分中, 有两个按钮将图像导入 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 。 单击 ** 导入为图像** 按钮, 并选择 ** Add To/asset/asset- pack.json ** 。

   ![Add image](https://cdn.phaser.io/editor-docs/first-steps-add-image-1.webp)

   电话 `assets/asset-pack.json` 文件为 Phaser 配置文件包含您可以加载到游戏中的所有文件。 场景编辑器使用此文件访问图像和其它资源。 您可以在游戏中添加图像文件 。 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 使用前一种方法,或打开 `assets-pack.json` 文件中的 [Asset Pack Editor](/editor/asset-pack-editor/intro).

4. 现在,在块视图中,你会看到新的图像。 将图像拖动并放入场景的中间。 按下 `End` 键将图像移动到场景的底部, 或者右键单击图像并选择 ** Edit ** ~ ** 移动底部 ** 选项 :

   ![Add image](https://cdn.phaser.io/editor-docs/first-steps-add-image-2-20241004.webp)

5. 保存场景( E)`Ctrl+S`和 。 和 。 (a) 和 [play the project](/editor/workbench/playing-project) (`F12`).

工程中添加图像有多种方法,例如选择系统探索器中的文件并把它丢入编辑窗口。您可以更多地了解这个过程 [here](/editor/workbench/upload-dialog) 。

## 社区辅导 {#community-tutorials}

有几个内容创建者在Phaser编辑器上制作了教程。我们在此部分建议其中一些:

斯科特·韦斯特沃的[Phaser Editor v4 Beginner's Guide: Make Games Fast with Phaser 3!](https://www.youtube.com/watch?v=upx7DST2blA&list=PLmcXe0-sfoShBVVcab8kB0A_2KGf30ClP&index=3)

![scott tutorial](https://cdn.phaser.games/oss-docs/assets/7d82fa68ea08e98c-scott-crash-course-video-20241108.webp)

由Arian Fornaris制作的[Make your first Phaser game](https://www.youtube.com/playlist?list=PLB8gI_5U0MvBiK7GExn8ONPk5jDPd2KlE)(为编辑器第3版制作,但仍能为初学者提供帮助)

![arian youtube channel](https://cdn.phaser.games/oss-docs/assets/0a2e19e1faa46613-arian-youtube-channel-20241108.webp)

---
