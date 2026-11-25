# 内容查看器 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/misc/content-viewers)

查看器是显示结构化数据的元素。 在主要情况下, 这些元素有文本和图标。 图标可以是正则图标或缩略图图像, 元素的线内预览。 图像文件、 场景文件、 地图集等资源包元素以及图示表。

所有观众都拥有一套共同的特征:

* 您可以放大图像。 按下 `Shift` 键, 并滚动鼠标轮 。
* 查看器可以有树形布局或网格布局,如果网格布局,只要足够放大,它就会切换到树形布局.
* 您可以过滤查看器的内容, 只显示与搜索框中文本匹配的标签。 如果您清理了搜索框, 则显示所有项目 。
* 网格和树形布局都允许崩溃/扩展项目。您使用 `Space` 键崩溃/扩展选中项目。使用 `C` 键,您可以崩溃所有项目。使用 `E` 键, 您可以扩展所有项目 。

![Viewers. Filtering and zooming.](https://cdn.phaser.io/editor-docs/misc-viewers-1-05032020.webp)![Gird layout of the viewer.](https://cdn.phaser.io/editor-docs/misc-viewers-2-05032020.webp)

* 一些观众(如Blocks视图),显示列表/格线视图图标,在两种布局之间切换.
  ![grid icon](https://cdn.phaser.games/oss-docs/assets/8c665caacf0ca654-viewer-grid-layout-20251125.webp)
  ![list icon](https://cdn.phaser.games/oss-docs/assets/9a89de9fed03e885-viewer-list-layout-20251125.webp)
* 一些观众(如场景编辑器的大纲视图)允许根据项目类型或其他标准设置自定义过滤.
  ![custom filter](https://cdn.phaser.games/oss-docs/assets/6f9a5962356360e5-viewer-custom-filter-20251125.webp)
* 您可以在某个项目上徘徊鼠标, 以显示关于该项目的附加信息的工具提示 。
  ![viewer tooltip](https://cdn.phaser.games/oss-docs/assets/ecc5603c47f58301-viewer-tooltip-20251125.webp)

---
