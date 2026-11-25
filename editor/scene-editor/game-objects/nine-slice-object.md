# 九宫格（NineSlice） {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/nine-slice-object)

九弦是内置的 PhaserZ 对象类型: [Phaser.GameObjects.NineSlice](/api/class/gameobjects-nineslice)。该类型允许您显示一个既可以水平伸展,也可以垂直伸展,但保留固定大小角的纹理对象。

使用 [nineSlice factory](/api/class/gameobjects-gameobjectfactory#nineslice) 创建一个 九切的代码。 这就是 [scene compiler](/editor/scene-editor/scene-compiler) 生成 九切的代码的方法 :

```javascript
const nineslice = this.add.nineslice(
                              0, 600, // x, y
                              "ui", "green-button", // texture, frame
                              300, 200, // width, height
                              70, 70, // leftWidth, rightWith
                              60, 60); // topHeight, bottomHeight
```

要在现场创建一个九切对象,你应该遵循这些步骤:

- 将一个内置的九元立格块丢到现场:

   ![Drop a nine slice object to the scene](https://cdn.phaser.io/editor-docs/scene-editor-create-9slice-1-20230208.webp)

- 选择对象的纹理, 按 X 键, 或在纹理部分打开纹理对话框 :

  ![Select texture](https://cdn.phaser.io/editor-docs/scene-editor-nineslice-create-2-20230208.webp)![The result of selecting the texture](https://cdn.phaser.io/editor-docs/scene-editor-nineslice-create-3-20230208.webp)

- 更改对象大小。 在 [Size section](/editor/scene-editor/game-objects/common-object-properties#size-properties) 中, 您可以设置对象的宽度和高度。 同时您也可以使用 [Resize tool](/editor/scene-editor/manipulation-tools#resize-tool)( 按 `Z` 键 ) :

  ![Resize the object](https://cdn.phaser.io/editor-docs/scene-editor-nineslice-create-4-20230208.webp)

- 在 ** 9ine 切片属性部分, 更改切片大小。 您还可以激活 [Nine Slice tool](/editor/scene-editor/manipulation-tools#slice-tool), 并更改场景大小 :

  ![Edit the slice size.](https://cdn.phaser.io/editor-docs/scene-editor-nineslice-create-5-20230208.webp)

顺便说一句,你可以[convert an Image or Sprite or any other game object into a Nine Slice](/editor/scene-editor/game-objects/replace-object-type)。


## 九块切片属性 {#nine-slice-properties}

九切片类型与其他对象类型共享属性 :

* [Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties)
* [Lists properties](/editor/scene-editor/game-objects/common-object-properties#lists-properties)
* [Transform properties](/editor/scene-editor/game-objects/common-object-properties#transform-properties)
* [Origin properties](/editor/scene-editor/game-objects/common-object-properties#origin-properties)
* [Size properties](/editor/scene-editor/game-objects/common-object-properties#size-properties)
* [Visible property](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/common-object-properties.md#visible-property)
* [Alpha single property](/editor/scene-editor/game-objects/common-object-properties#alpha-single-property)
* [Tint properties](/editor/scene-editor/game-objects/common-object-properties#tint-properties)
* [Texture property](/editor/scene-editor/game-objects/common-object-properties#texture-property)

但也有特殊属性:

![Nine Slice properties.](https://cdn.phaser.io/editor-docs/scene-editor-nine-slice-properties-20230208.webp)

* [leftWidth](/api/class/gameobjects-nineslice#leftWidth)和[rightWidth](/api/class/gameobjects-nineslice#rightWidth)的特性,会改变水平切片的大小.
* [topHeight](/api/class/gameobjects-nineslice#topHeight)和[bottomHeight](/api/class/gameobjects-nineslice#bottomHeight)的特性,它改变垂直切片的大小.


## 3 个切片模式 {#three-slice-mode}

九晶体可以只用三个水平切片来创建。这是对只需要水平拉伸的对象的一种优化。如果将**上**和**下**高度设置为`0`,则该优化将启动。

在 Phaser 编辑器中, 我们提供一个 ** TreeSlice** 块来创建 九切对象的这个特定配置。 您可以将这个块降入创建对象的场景 :

![Create a 3 slice object.](https://cdn.phaser.io/editor-docs/scene-editor-threeslice-create-1-20230208.webp)

九切片对象处于三切片模式时,可以使用[Slice Tool](/editor/scene-editor/manipulation-tools#slice-tool)和**三切片属性** 部分更改切片的大小,注意只显示宽度属性和操纵器:

![Changes the width of the slices.](https://cdn.phaser.io/editor-docs/scene-editor-three-slice-create-2-20230208.webp)

---
