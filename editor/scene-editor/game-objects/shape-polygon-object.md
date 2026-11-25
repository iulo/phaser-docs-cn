# 多边形 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/shape-polygon-object)

可以通过将来自Blocks视图的**Polygon**块扔到现场来创建[Polygon](/api/class/gameobjects-polygon)对象.

![Create a polygon.](https://cdn.phaser.io/editor-docs/scene-editor-polygon-create-20220623.webp)

多边形带有点。 您可以编辑 ** 波利贡 部分 ** 或 [Polygon tool](/editor/scene-editor/manipulation-tools#polygon-tool) 中的点。

Polygon 部分显示点字段。点作为点的X Y对的字符串,用空格分隔。

![Polygon section.](https://cdn.phaser.io/editor-docs/scene-editor-polygon-section-20220623.webp)

多边形工具( 您可以用 `Y` 键激活) 显示多边形在场景中的点。 它允许您:

* 更改点的位置:用鼠标光标拖动点。
* 删除点:将鼠标光标移到点上并按“删除”键(或双击)。当光标在点上时,它会被涂成红色。

![Move polygon point.](https://cdn.phaser.io/editor-docs/scene-editor-polygon-edit-points-20220623.webp)
* 添加新点: 将鼠标光标移过一行。 它显示光标下的白色处理器, 您可以拖动它创建新点 。

![Add new point.](https://cdn.phaser.io/editor-docs/scene-editor-polygon-add-point-20220623.webp)![Add new point.](https://cdn.phaser.io/editor-docs/scene-editor-polygon-add-point-2-20220623.webp)

[Polygon](/api/class/gameobjects-polygon)代码由[scene compiler](/editor/scene-editor/scene-compiler)使用[polygon object factory](/api/class/gameobjects-gameobjectfactory#polygon)生成:

```javascript
const polygon = this.add.polygon(10, 10, "0 0 20 70 100 100 80 20");
```

---
