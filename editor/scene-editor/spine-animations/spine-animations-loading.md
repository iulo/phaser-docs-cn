# 加载 Spine 资源 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/spine-animations/spine-animations-loading)

要将 [Spine](https://esotericsoftware.com)动画装入 Phaser游戏中,首先需要从 [Spine](https://esotericsoftware.com) 编辑器中导出该动画.

输出动画可产生以下资源:

* 斯凯勒顿和动画数据.
* 纹理图集,包含骨架的图像.

您可以将骨架和动画数据导出到 JSON 文件或二进制文件( `.skel`) 。 Phaser 编辑器支持两种格式。 另外, 您也可以将骨架图像导出为纹理图集。 它会产生带有帧信息和 `.png`图像的 `.atlas` 文件 。

[Learn more about Assets Management in the Spine editor](https://esotericsoftware.com/spine-phaser#Asset-Management)

将[Spine](https://esotericsoftware.com)资源导入Phaser游戏的常用方式是使用Phaser加载器方法:

* `spineBinary(key, url)` - 装入包含骨架和动画数据的`.skel`文件.
* `spineJson(key, url)` - 装入包含骨架和动画数据的`.json`文件.
* `spineAtlas(key, url, premultipliedAlpha)` - 装入纹理图集文件.

举例来说:

```javascript
preload() {
   this.load.spineBinary("skeleton", "path/to/skeleton.skel");
   this.load.spineAtlas("skeleton-atlas", "path/to/skeleton.atlas");
}
```

然而,Phaser编辑器提供了[Asset Pack Editor](/editor/asset-pack-editor/intro),这是将资源装入Phaser游戏机的视觉工具.

将 [Spine](https://esotericsoftware.com) 资源导入到资源包文件的工作流程为:

* 从 [Spine](https://esotericsoftware.com) 编辑器中导出资源到游戏项目的“ 资源” 文件夹 :

  ![Copy Spine files into the assets folder of your game.](https://cdn.phaser.io/editor-docs/spine-animations-assets-20230923.webp)

* 在 [Files view](/editor/workbench/files-view) 中,选择数据 `.json` 文件(或如果以二进制格式导出 `.skel` ):

  ![Select the data file in the Files view](https://cdn.phaser.io/editor-docs/spine-animations-select-data-file-20230923.webp)

* 检查者认为, ** 资源包条目 ** 的一节显示用于将选中文件导入资源包文件的按钮 :

  ![Import the file into an asset pack.](https://cdn.phaser.io/editor-docs/spine-animations-import-data-file-20230923.webp)

* 使用 `.atlas` 文件进行同样的处理。 在 [Files view](/editor/workbench/files-view) 中选择, 并添加到一个资源包中 :

  ![Select the atlas file.](https://cdn.phaser.io/editor-docs/spine-animations-select-atlas-file-20230923.webp)![Add the atlas file to the asset pack.](https://cdn.phaser.io/editor-docs/spine-animations-add-atlas-to-pack-20230923.webp)
  
* 打开 `asset-pack.json` 文件中的 [Asset Pack Editor](/editor/asset-pack-editor/intro) 并检查Spine 资源是否在那里:

  ![The spine assets in the Asset Pack editor.](https://cdn.phaser.io/editor-docs/spine-animations-asset-pack-20230923.webp)

如果一切顺利, 您会在包编辑器中找到数据文件和地图集文件。 如果您选择数据文件条目, 检查器视图会显示信息和动画预览。 您可以点击 ** 预览动画** 按钮, 它打开一个对话框, 您可以在其中播放动画。 我们稍后会更多地谈论这个对话框 。

![Preview button.](https://cdn.phaser.io/editor-docs/spine-animations-asset-preview-button-20230923.webp)![Preview dialog.](https://cdn.phaser.io/editor-docs/spine-animations-asset-preview-dialog-20230923.webp)

## Spine 资源默认命名规则 {#spine-assets-default-naming-rules}

**重要** [Spine Phaser runtime](https://esotericsoftware.com/spine-phaser)允许使用不同的地图集来绘制同一骨架。在预览骨架时,编辑器会寻找一个带有相同键但带有`-atlas`后缀的地图集资源。在上述例子中,骨架数据有`spineboy`键,地图集则拥有`spineboy-atlas`键:

![Spine data and atlas assets.](https://cdn.phaser.io/editor-docs/spine-animations-data-and-atlas-assets-20230923.webp)

---
