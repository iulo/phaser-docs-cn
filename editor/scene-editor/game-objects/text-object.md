# 文本 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/text-object)

[Text type](/api/class/gameobjects-text)允许创建文本对象.

 基于 HTML 字体。 它允许自定义文本的颜色、 阴影、 中风等...

可以通过在现场投放文本内置块来创建 [Text object](/editor/scene-editor/game-objects/text-object).

![Create a default Text object.](https://cdn.phaser.io/editor-docs/scene-editor-text-object-create-block-09252020.webp)

另外,使用[type replacing dialog](/editor/scene-editor/game-objects/replace-object-type),也可以将[Bitmap Text](/editor/scene-editor/game-objects/bitmap-text-object)(或任何其他物体)转换成[Text object](/editor/scene-editor/game-objects/text-object).

![Text object.](https://cdn.phaser.io/editor-docs/scene-editor-text-object-05242020.webp)

文本对象是使用 [text factory](/api/class/gameobjects-gameobjectfactory#text) 创建的代码。 [scene compiler](/editor/scene-editor/scene-compiler) 就是这样生成该代码的:

```javascript
const text_1 = this.add.text(90, 385, "", {});
text_1.text = "New Text object";
text_1.setStyle({
    "backgroundColor":"blue",
    "color":"orange",
    "fontFamily":"serif",
    "fontSize":"60px",
    "fontStyle":"bold italic",
    "stroke":"orange",
    "shadow.offsetX":5,
    "shadow.offsetY":5,
    "shadow.color":"brown",
    "shadow.blur":7,
    "shadow.stroke":true,
    "shadow.fill":true});
text_1.setPadding({"left":10,"top":10,"right":10,"bottom":10});
```

## 字体家族属性 {#font-family-property}

文本游戏对象中的一个特殊属性是 **Font Family **. 您可以写出浏览器支持的任何字体名称, 如“ Arial ” , “Verdana ” , “ Monospace ” 等, 或者您可以使用您游戏中装入的自定义字体 。

Phaser提供了一个简单的资源加载器API,可以装入游戏中的自定义字体:

 ```javascript
 this.load.font({
    key: "Nokia",
    url: "assets/nokia.ttf",
    format: "truetype",
    descriptors: { style: "normal", weight: "400" }
 });
 ```

然后,您可以使用文本对象中的字体 :

```javascript
this.add.text(x, y, "Hello World", { 
    fontFamily: "Nokia", 
    fontSize: 48 
});
```

使用Phaser编辑器,工作流程相同,可以加载[Asset Pack editor](/editor/asset-pack-editor/intro)中的字体,并用于**Font Family**属性.

您可以遵循这些步骤:

- 上传字体文件到工程中 。
- 选择文件视图中的字体文件 :

    ![select font file](https://cdn.phaser.games/oss-docs/assets/389abb063a9ae277-scene-editor-select-font-in-files-view.webp)
- 单击检查员视图中的 ** 导入为字体** 按钮:

    ![import font file](https://cdn.phaser.games/oss-docs/assets/dcae291e56fb44cd-scene-editor-import-font-file.webp)
- 在 ** Font Family ** 属性中,您可以写字体名称,也可以从三点菜单中选择:

    ![select font family](https://cdn.phaser.games/oss-docs/assets/fee710f07a0d7446-scene-editor-font-family-parameter.webp)

斯科特·韦斯特沃(Scott Westover)做了一个惊人的视频教程,内容是如何在Phaser游戏中添加自定义字体. 请检查!

[Phaser Editor v4 Tutorial: Native Custom Fonts!](https://www.youtube.com/watch?v=QnDJkBdAz0k)

[![Phaser Editor v4 Tutorial: Native Custom Fonts!](https://cdn.phaser.games/oss-docs/assets/1d1bd6029f7ad192-scott-tutorial-native-fonts.webp)](https://www.youtube.com/watch?v=QnDJkBdAz0k)

## 文本类型属性 {#text-type-properties}

[Text type](/api/class/gameobjects-text)包含许多[common object properties](/editor/scene-editor/game-objects/common-object-properties):

* [Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties)
* [Lists properties](/editor/scene-editor/game-objects/common-object-properties#lists-properties)
* [Transform properties](/editor/scene-editor/game-objects/common-object-properties#transform-properties)
* [Origin properties](/editor/scene-editor/game-objects/common-object-properties#origin-properties)
* [Flip properties](/editor/scene-editor/game-objects/common-object-properties#flip-properties)
* [Visible property](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/common-object-properties.md#visible-property)
* [Alpha properties](/editor/scene-editor/game-objects/common-object-properties#alpha-properties)

也包含[Text property](/editor/scene-editor/game-objects/common-object-properties#text-property),它专门用于所有有文本的对象,及其具体属性:

* 电话 [TextStyle](https://phaser.io/oss/docs/api-documentation/class/types-gameobjects-text.md#-textstyle) 属性。
* 电话 [TextShadow](https://phaser.io/oss/docs/api-documentation/class/types-gameobjects-text.md#-textshadow) 属性。
* 电话 [TextPadding](https://phaser.io/oss/docs/api-documentation/class/types-gameobjects-text.md#-textpadding) 属性。
* 电话 [TextWordWrap](https://phaser.io/oss/docs/api-documentation/class/types-gameobjects-text.md#-textwordwrap) 属性。

在检查员看来,在每块属性的标签上悬停鼠标,以获得一个带有[Phaser API](https://phaser.io/oss/docs/docs/latest.md)的工具提示.

---
