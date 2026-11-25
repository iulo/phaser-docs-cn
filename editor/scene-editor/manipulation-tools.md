# 操作工具 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/manipulation-tools)

操纵工具是允许改变对象属性的场内工具.

每个工具都有命令可以激活/解除它。您可以使用键、上下文菜单或 [Main toolbar](/editor/workbench/main-toolbar)执行命令。

您可以激活一个工具或时间。 或者关闭工具 。

![Manipulators.](https://cdn.phaser.io/editor-docs/scene-editor-tools-20230518.webp)

## 坐标 {#coordinates}

一些工具可以在本地或全局坐标中使用。 您可以修改上下文菜单的 ** Coords ** 菜单中的coords :

![Transformation orientation.](https://cdn.phaser.io/editor-docs/scene-editor-tools-coords-05242020.webp)

## 翻译工具 {#translate-tool}

此工具允许您移动屏幕上的对象。 它会影响 & # ## # 和 ** Y** 属性 。

您可以用 `T` 键激活它, 或者在上下文菜单或 [Main toolbar](/editor/workbench/main-toolbar) 中激活它 。

拖动红箭头以更改QQ,绿箭头则更改**Y**.

![Translate tool.](https://cdn.phaser.io/editor-docs/scene-editor-tools-translate-04262020.webp)

## 缩放工具 {#scale-tool}

激活此工具以改变对象的大小。 您可以在上下文菜单中激活它, 即 [Main toolbar](/editor/workbench/main-toolbar),或与 `S` 键。继续按 `Shift` 键,如果您想要按比例缩放。

![Scale tool.](https://cdn.phaser.io/editor-docs/scene-editor-tools-scale-04262020.webp)

## 旋转工具 {#rotate-tool}

此工具会改变对象的角度。 您可以在上下文菜单中激活它, 即 [Main toolbar](/editor/workbench/main-toolbar), 或者用 `R` 键 。

![Rotate tool.](https://cdn.phaser.io/editor-docs/scene-editor-tools-rotate-04262020.webp)

## 来源工具 {#origin-tool}

您可以使用此工具编辑对象的源头。 您可以在上下文菜单中激活它, 即 [Main toolbar](/editor/workbench/main-toolbar), 或者用 `O` 键 。

Phaser v3 中, [containers](/editor/scene-editor/game-objects/container-object)的旋转轴固定在 `x=0, y=0` 上。 但是, 原产地工具模拟了该轴的变化, 绕容器的孩子移动, 但保持相同的全局位置 。

![Origin tool.](https://cdn.phaser.io/editor-docs/scene-editor-tools-origin-05242020.webp)

## 切片工具 {#slice-tool}

这是一个用于改变 [NineSlice](/editor/scene-editor/game-objects/nine-slice-object) 对象切片大小的工具。 您可以在上下文菜单中激活它, 使用 ** Tools – Slic Tool ** 选项。 或者您可以点击 ** Edit Slics ** 按钮, 在 九 Slic 属性部分激活它 :

![Activate the Slice tool.](https://cdn.phaser.io/editor-docs/scene-editor-slice-tool-edit-button-20230208.webp)

工具显示四个曼尼普塔罗斯用于改变切片的大小:

![Slice manipulators.](https://cdn.phaser.io/editor-docs/scene-editor-slice-tool-manipulators-20230208.webp)

如果您想要改变**左**和**rigth**切片的宽度,可以同时并用同一值按下并按住`Shift`键,它也适用于**顶**和**底**切片的高度.

如果对象处于3切片模式,则只显示操纵器的宽度切片:

![Nine Slice with 3 slices mode.](https://cdn.phaser.io/editor-docs/scene-editor-3-slice-tool-20230208.webp)

## 调整工具大小 {#resize-tool}

此工具允许更改一些对象的大小, 如 [TileSprite](/editor/scene-editor/game-objects/tile-sprite-object)、 [Rectangle](/editor/scene-editor/game-objects/shape-rectangle-object)和 [Ellipse](/editor/scene-editor/game-objects/shape-ellipse-object) 。 您可以在上下文菜单中或用 `Z` 键激活它。 修改对象大小与缩放不同 。

![TileSprite size tool.](https://cdn.phaser.io/editor-docs/scene-editor-tools-tilesprite-size-04262020.webp)

## 多边形工具 {#polygon-tool}

多边形工具( 您可以用 `Y` 键激活) 显示多边形在场景中的点。 它允许您:

* 更改点的位置:用鼠标光标拖动点。
* 删除点:将鼠标光标移到点上并按“删除”键(或双击)。当光标在点上时,它会被涂成红色。

![Move polygon point.](https://cdn.phaser.io/editor-docs/scene-editor-polygon-edit-points-20220623.webp)
* 添加新点: 将鼠标光标移过一行。 它显示光标下的白色处理器, 您可以拖动它创建新点 。

![Add new point.](https://cdn.phaser.io/editor-docs/scene-editor-polygon-add-point-20220623.webp)![Add new point.](https://cdn.phaser.io/editor-docs/scene-editor-polygon-add-point-2-20220623.webp)

## 拱门物理体工具 {#arcade-physics-body-tool}

此工具允许更改 Arcade 物理体的大小和抵消。 您可以按 `B` 键, 激活场景上下文菜单中的工具 。

身体有两种类型:圆形和长方形。当您编辑一个圆形时,工具会显示身体的圆形,中心(抵消)和半径处理器:

![Editing the circular body.](https://cdn.phaser.io/editor-docs/arcade-physics-body-circle-tool-20221005.webp)

如果对象有矩形体,则工具会显示偏移和大小处理器:

![Editing the rectangular body.](https://cdn.phaser.io/editor-docs/arcade-physics-tool-rect-body-20221006.webp)

## 点击区域工具 {#hit-area-tool}

此工具允许更改对象的交互命中区域。 您可以用 `I` 命令激活此工具, 或者在 ** Tools ** 上下文菜单中选择它 。

命中区域有不同类型形状。 此工具为每种类型形状提供不同的操纵器 :

* [Rectangle](/editor/scene-editor/input#rectangle-hit-area)
* [Ellipse](/editor/scene-editor/input#ellipse-hit-area)
* [Circle](/editor/scene-editor/input#circle-hit-area)
* [Polygon](/editor/scene-editor/input#polygon-hit-area)

## 泛工具 {#pan-tool}

此工具允许您将场景打包。 您可以用 `Space` 键激活它。 当选中时, 鼠标光标会显示一个“ 抓取” 图标, 然后点击场景并拖动它 。

另外,您还可以按下 `Alt` 键并拖动鼠标来打压场景。这种方法不需要激活 Pan 工具 。

## 选择区域工具 {#select-region-tool}

此工具允许您在现场绘制一个区域, 并选择该区域内的所有对象。 您可以在工具栏、 上下文菜单中选择, 或者按下 `Shift+S` 键。 如果您继续按 Ctrl 键, 则会保留先前选定的对象 。

![Select objects in region tool.](https://cdn.phaser.io/editor-docs/scene-editor-tools-select-region-06172020.webp)

---
