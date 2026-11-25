# 使用精灵表 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/working-with-spritesheets)

将“拼贴图像”包装成单一图像有多种方式,其中最受欢迎的就是精灵表。

在 Phaser 编辑器中,您可以在 [Asset Pack Editor](/editor/asset-pack-editor/intro) 中定义一个图示表资源 :

![Define sprite-sheet](https://cdn.phaser.io/editor-docs/scene-editor-spritesheet-define-20240530.webp)

一旦定义了图示表资源,您就可以在场景编辑器中使用它.

与其它资源一样,图示表显示在块视图中,与地图集资源一样,可以扩展图示表块,以获得框架并放入场景:

![Sprite-sheet blocks](https://cdn.phaser.io/editor-docs/scene-editor-spritesheet-blocks-20240530.webp)

Sprite-sheet在反像素艺术游戏中非常常见,这些游戏大多使用[tile maps](/editor/scene-editor/game-objects/tilemap-object)来创建关卡或关卡的重要部分. Phaser编辑器中,您可以将一个瓦片映射导入到场景中,不过,您可能喜欢在砖块上方添加几个元素,并使用常规的Sprite游戏对象.

有些图案工作表,瓦片的位置很重要, 因此在块视图中将它们分割成列表, 使得人类的眼睛更难阅读。 在这种情况下, 您可以从Spritesheet Preview 视图的段落中获取框架。 这个查看器可以显示原始的图案工作表图像, 但允许选择一个框架并将其拖放到现场。 它有类似图编辑器中的瓦片集的行为, 如 Tiled :

![Sprite sheet viewer](https://cdn.phaser.io/editor-docs/scene-editor-spritesheet-instepctor-view.webp)

图像可能很大,但可以持有`Alt`或`Option`键,拖动鼠标翻译图像.

检查器视图在您选择块视图中的“ 闪存” 预览部分时显示“ 闪存” 表单资源, 但也可以显示您在屏幕中选择带有“ 闪存”表纹理的对象时显示该视图。

Spritesheet Preview 查看器缺少一些功能, 例如选择多个帧或缩放在/ 外。 在接下来的发行中, 我们将不断改进它, 并给以对图片创建的全力支持 。

---
