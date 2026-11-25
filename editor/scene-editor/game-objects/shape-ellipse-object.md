# 椭圆 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/shape-ellipse-object)

你可以在现场从块视图中掉下**椭圆**块,从而创建[Ellipse](/api/class/gameobjects-ellipse).

![Create an ellipse.](https://cdn.phaser.io/editor-docs/scene-editor-ellipse-1-11092020.webp)

您可以改变**Size 一节中的椭圆形大小**,也可以使用[Size tool](/editor/scene-editor/manipulation-tools#resize-tool).

![Change the ellipse size.](https://cdn.phaser.io/editor-docs/scene-editor-ellipse-2-11092020.webp)

此外,椭圆形还拥有[Smoothness](/api/class/gameobjects-ellipse#smoothness)属性(渲染时使用的点数):

![Ellipse's smoothness property.](https://cdn.phaser.io/editor-docs/scene-editor-ellipse-3-11092020.webp)

[Ellipse](/api/class/gameobjects-ellipse)代码由[scene compiler](/editor/scene-editor/scene-compiler)使用[ellipse object factory](/api/class/gameobjects-gameobjectfactory#ellipse)生成:

```javascript
const ellipse = this.add.ellipse(10, 10, 100, 100);
```

---
