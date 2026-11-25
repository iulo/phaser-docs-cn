# 创建新的动画文件 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/animations-editor/new-file-wizard)

要创建动画文件,请打开新文件对话框,并选择 ** 动画文件** 选项:

![Select create a new animations file.](https://cdn.phaser.io/editor-docs/animations-new-file-1.webp)

它打开了 ** 新动画文件 ** 对话框, 并询问文件名称和位置 :

![Select name and location.](https://cdn.phaser.io/editor-docs/animations-new-file-2.webp)

文件在动画编辑器中创建并打开.

在大多数情况下, 您想要将动画文件添加到 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 中。 要做到这一点, 请选择文件视图中的文件, 检查器视图会显示您可以选择将动画添加到 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 中 :

![Import animation file into the Asset Pack file.](https://cdn.phaser.io/editor-docs/animations-add-to-pack-file.webp)

另外,您还可以使用 [Animations Loader](/api/class/loader-loaderplugin#animation) 装入动画文件:

```javascript
this.load.animation("playerAnimations", "assets/animations.json");
```

---
