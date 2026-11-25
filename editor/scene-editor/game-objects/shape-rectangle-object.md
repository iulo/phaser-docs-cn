# 矩形 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/shape-rectangle-object)

通过将来自Blocks视图的**矩形**块扔到现场,可以创建[Rectangle](/api/class/gameobjects-rectangle).

![Create a rectangle.](https://cdn.phaser.io/editor-docs/scene-editor-rectangle-1-11092020.webp)

您可以改变**Size 一节**中的矩形大小,或者使用[Size tool](/editor/scene-editor/manipulation-tools#resize-tool).

![Change the rectangle size.](https://cdn.phaser.io/editor-docs/scene-editor-rectangle-2-11092020.webp)

自 Phaser 4 起, 您可以设置 ** Rounded ** 属性, 将圆角给矩形。 默认它会被设定为 `0`( 无圆角) 。

![rectangle rounded](https://cdn.phaser.games/oss-docs/assets/d53acd97b9ee498a-scene-editor-rectangle-section-20251126.webp)

[Rectangle](/api/class/gameobjects-rectangle)代码由[scene compiler](/editor/scene-editor/scene-compiler)使用[rectangle object factory](/api/class/gameobjects-gameobjectfactory#rectangle)生成:

```javascript
const rectangle = this.add.rectangle(10, 10, 100, 100);
```

---
