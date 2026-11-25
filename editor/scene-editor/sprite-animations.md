# 精灵动画 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/sprite-animations)

斯普丽特游戏对象是一个具有逐帧显示动画能力的图像对象.

Phaser编辑器中有两个工作流程用于在游戏中制作动画:

## 工作流程 1 {#workflow-1}

使用 [Animations Editor](/editor/animations-editor/intro) 。 它从 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 中获取图像框, 并将框组为动画。 您可以设定动画的不同属性, 如帧率、 重复率、 延迟率等。 最后, 将动画文件加载到 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 中 。

## 工作流程 2 {#workflow-2}

从 Asesprite 软件导出动画。 它输出兼容 Phaser 的 Asperite 动画文件, 并且您可以装入 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 。

## 终于 {#finally}

一旦[Asset Pack file](/editor/asset-pack-editor/asset-pack-file)中定义了动画资源(由[Animations Editor](/editor/animations-editor/intro)或Aesprite制作),您就可以在场景编辑器的不同工具中使用: .

- 块视图中的动画块。 您可以通过 [dropping an animation block into the scene](/editor/scene-editor/game-objects/sprite-object) 创建 Sprite 游戏对象 。
  ![Create sprite from animation block](https://cdn.phaser.io/editor-docs/scene-editor-sprite-create-from-animation-block-20240917.webp)
- ** 督察** 视图的 [Animation and Animation Configuration sections](/editor/scene-editor/game-objects/common-object-properties#animation-properties) 允许在 Sprite 游戏对象上播放动画 。
  ![Animation properties.](https://cdn.phaser.io/editor-docs/scene-editor-animations-props-custom-config-20240917.webp)
  如果您选中 ** 动画预览 ** 参数, 它会在现场编辑器中实时播放该动画 。
  ![Coin animation preview](https://cdn.phaser.io/editor-docs/coin.gif)
- [Animation Key user property type](/editor/scene-editor/prefabs/prefab-user-properties#animation-key-property-type),它允许选择一个[Asset Pack file](/editor/asset-pack-editor/asset-pack-file)定义的动画名称.
  ![Animation Key user property](https://cdn.phaser.io/editor-docs/prefab-user-props-animation-key-dialog-20231027.webp)

## 斯匹特动画预览 {#sprite-animation-preview}

Phaser编辑器提供了一个预览图案动画的对话框:

![Sprite animation preview dialog.](https://cdn.phaser.io/editor-docs/scene-editor-sprite-animations-preview-dialog-20231102.webp)

您可以在不同的背景中打开此对话框 :

* 在 [Asset Pack Editor](/editor/asset-pack-editor/intro) 中,当您在大纲视图中选择 Sprite 动画时 :
  
  ![Preview in the Asset Pack editor.](https://cdn.phaser.io/editor-docs/aseprite-preview-asset-pack-20231102.webp)

* 在场景编辑器的块视图中,作为一个Sprite动画块:
  
  ![Animation block.](https://cdn.phaser.io/editor-docs/scene-editor-aseprite-animation-block-preview-1-20231102.webp)![Animation block properties.](https://cdn.phaser.io/editor-docs/scene-editor-aseprite-animation-block-preview-2-20231102.webp)

* 在 [Animation properties section](/editor/scene-editor/game-objects/common-object-properties#animation-properties) 中,当选择 Sprite 编辑器中的 Sprite 游戏对象时 :

  ![Animation properties.](https://cdn.phaser.io/editor-docs/scene-editor-sprite-animation-preview-inspector-20231102.webp)

## 支持Aepprite 动画 {#aseprite-animation-support}

Aseprite([www.aseprite.org](https://www.aseprite.org))是制作像素艺术和动画的流行软件. Phaser提供了Aseprite文件加载器和一种与文件一起制作动画的方法.

这是Phaser编辑器中与Aseprite动画合作的工作流程 :

* 导出 Asesprite 文件到 Phaser 编辑器项目。 您应该跟随 [these instructions](#aseprite-exporting-instructions) 来导出文件。 以下图像显示“ paladin” 和“ 坦克” 动画的地图集和 PNG 文件 :
  
  ![Aseprite exported files.](https://cdn.phaser.io/editor-docs/scene-editor-aseprite-export-1-20231102.webp)

* 导入 Asesprite 文件为 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 。 您可以选择地图集文件( `.json`) , 并用 [import buttons of the Inspector view](/editor/asset-pack-editor/add-file#importing-from-the-files-view) 导入 :
  
  ![Select the Aseprite files](https://cdn.phaser.io/editor-docs/scene-editor-import-aseprite-files-files-view-20231102.webp)![Import the files](https://cdn.phaser.io/editor-docs/scene-editor-import-aseprite-files-inspector-view-20231102.webp)

  您可以检查文件在 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 中定义正确 :
  ![Aseprite files in the pack file](https://cdn.phaser.io/editor-docs/scene-editor-aseprite-pack-file-1-20231102.webp)![Aseprite files in the pack file](https://cdn.phaser.io/editor-docs/scene-editor-aseprite-pack-file-2-20231102.webp)

* 现在Asesprite文件在[Asset Pack file](/editor/asset-pack-editor/asset-pack-file)中,你可以访问编辑器不同工具中的动画:
  
  ![Aseprite animation in the scene editor blocks view.](https://cdn.phaser.io/editor-docs/scene-editor-aseprite-animation-block-20231102.webp)

## 编译代码片断 {#aseprite-code-snippets}

在Phaser中,在在"宝石"中播放Asesprite动画之前,应该先在动画管理器中创建动画.

对于动画的创建,你应该叫[createFromAseprite](/api/class/animations-animationmanager#createFromAseprite),然后通过作为参数的Asesprite资源键.

在 Phaser 编辑器中,您可以辅助方式添加此块代码 :

* 右键单击场景, 它打开上下文菜单。 在 ** Code 片段 ** 菜单中, 请选择 **Add 从 Aseprite ** 选项创建动画 。
  
  ![Select the Aseprite code snippet to add.](https://cdn.phaser.io/editor-docs/scene-editor-aseprite-code-snippet-1-20231107.webp)

* 它打开了与项目 [Asset Pack files](/editor/asset-pack-editor/asset-pack-file) 中定义的所有 Asesprite 资源键的对话框。 请选择您想要在项目中使用的键 。 可能全部使用 :

  ![Select the Aseprite_ asset key.](https://cdn.phaser.io/editor-docs/scene-editor-aseprite-code-snippet-2-20231107.webp)

* 最后,当编译场景时,它会在**create()**场景方法的第一行生成这些代码的线条:
  
  ```javascript
  // snippets
  this.anims.createFromAseprite("paladin");
  this.anims.createFromAseprite("tank");
  ```

### 以 empt 格式导出指令 {#aseprite-exporting-instructions}

拍自[Phaser documentation](https://phaser.io/oss/docs/api-documentation/class/loader-loaderplugin.md#aseprite_anchor):

要在 Aseprite 中导出兼容的 JSON 文件, 请做以下操作 :

- 转到“ 文件 - 导出工作表”
- 在布局标签上: 2a. 将“ 弹匣类型” 设置为“ 装入” 2b。 将“ 约束” 设置为“ 无” 2c。 请检查“ 复制件” 复选框
- 在Sprite标签上: 3a. 将“ 标签” 设置为“ 可视层 ” 3b。 将“ 框架” 设置为“ 所有框架”, 除非您仅希望导出一组子标签
- 边框标签: 4a. 请检查“ 三角形玻璃” 和“ 三角形单元格” 选项 4b. 确保“ 边界铺设”、“ 间隔” 和“ 内部铺设” 全部为 0 (通常足够)
- 在输出标签: 5a. 选中“ 输出文件” , 给您图像一个名称, 并确保您选择“ png 文件” 作为文件类型 5b 。 请选中“ JSON 数据” , 并给您的 json 文件一个名称 5c。 JSON Data 类型可以是 Hash 或 阵列 。 Phaser 5d. 请在“项目文件名”输入框中,请确保“标签”在“项目文件名 ” 输入框中被选中。请在“项目文件名 “项目文件名”输入栏中,请在“项目文件名称”输入框中输入“标签”。 `{frame}` 并且没有更多的。
- 点击导出 。

测试时采用了Aeprite 1.2.25.

这将导出一个 png 和 json 文件, 您可以使用 Aseprite 加载器 来加载它 。

---
