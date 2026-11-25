# 场景属性 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/scene-properties)

场景具有不同属性,不属于编辑器或编译器.

当没有选择对象时, 属性会在检查器视图中显示。 这意味着, 如果您点击现场的空白空间或按下 `ESC` 键, 则会显示场景属性 。

编译器设置在[Scene Compiler chapter](/editor/scene-editor/scene-compiler)中覆盖.

## 抓取属性 {#snapping-properties}

抓取属性允许您将场景分割成网格,并将对象放置在网格的单元格中。这是一个非常有用的技术,可以使对象保持适当的对齐。

![Snapping properties.](https://cdn.phaser.io/editor-docs/scene-editor-snap-properties-04222020.webp)
* **启用属性**: 激活抓取。 您可以用 `E` 键更改检查器视图中的值 。
* **正在抓取宽度和高度**: 是一个网格大小,可以按下对象。您可以在检查器视图中更改它。此外,您还可以选择一个对象并执行 **Snap to Object Size** 命令。

## 边框属性 {#border-properties}

场景编辑器显示一个框架,或边框,可以用作游戏大小的参考,一个Prefab大小,或需要框架的任意.

它不是[Phaser API](https://phaser.io/oss/docs/docs/latest.md)的一部分,它只是编辑器资源,并且不会以任何方式影响游戏.

您可以更改检查器视图中的边框值。 它具有位置和大小 。

![Border properties.](https://cdn.phaser.io/editor-docs/scene-editor-border-properties-04222020.webp)

## 场景显示属性 {#scene-display-properties}

编辑器显示不同地点的场景名称。 默认情况下, 名称是场景文件的名称, 但不包含扩展名。 但是, 您可以在 ** Scene Display Name ** 属性中更改此 UI 名称。 此外, 您还可以在 ** Scene Director 属性中添加对场景的描述 。

![scene display properties](https://cdn.phaser.games/oss-docs/assets/2d68c6efdf434dde-scene-display-properties-20251124.webp)

![scene display name in blocks view](https://cdn.phaser.games/oss-docs/assets/8993eb7b5dbc9180-scene-display-in-blocks-view-20251124.webp)

### 上下文菜单 {#context-menu}

现场的上下文菜单显示 ** 抓取** 子菜单,并带有抓取命令:

* 切换抓取( `E`).
* 向对象大小( `W`) 键对。 此命令将选定对象的大小设定为场景的快取大小值 。
* 移动对象位置命令。 这些命令将选定的对象按任何方向按按键大小( `Arrow keys`) 或按键大小( `Shift+Arrow keys`) 10x 翻译。 如果按键被禁用, 这些命令将按键对象按 1 或 10 像素翻译 。

![Snapping commands in context menu.](https://cdn.phaser.io/editor-docs/scene-editor-snap-menu-06172020.webp)

---
