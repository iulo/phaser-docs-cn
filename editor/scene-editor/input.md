# 输入 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/input)

我们正在探索如何帮助您处理游戏输入。 首先,我们正在支持场景编辑器和[Hit Area of an object](/editor/scene-editor/input#hit-area)中的[Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) API。

## 键盘键盘对象 {#keyboard-key-object}

场景编辑器支持在场景中添加一个 [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) 对象。 只需从块视图中拖动 ** Keyboard. Key** 对象, 并把它丢入场景 :

![Add Keyboard Key to the scene.](https://cdn.phaser.io/editor-docs/scene-editor-input-add-key-20221114.webp)

编辑器在大纲视图的**输入**部分显示**关键**对象:

![Key objects in the Outline view.](https://cdn.phaser.io/editor-docs/scene-editor-input-keys-in-outline-20221114.webp)

选择一个用于编辑检查器视图中属性的键 :

![The Keyboard Key properties.](https://cdn.phaser.io/editor-docs/scene-editor-input-key-properties-20221114.webp)

** 可变** 属性:

* **名称**: 键对象变量的名称 。
* **作用域**: The scope of the variable. It may be `LOCAL`, `METHOD`, `CLASS`, or `PUBLIC`. By default it is `PUBLIC`. You can [learn more about the variable scopes](/editor/scene-editor/game-objects/common-object-properties#scope-property).

** 键盘键** 属性 :

* **键代码**: 编号 [keyCode](/api/class/input-keyboard-key#keyCode)。单击按钮选择代码 :

![KeyCode dialog.](https://cdn.phaser.io/editor-docs/scene-editor-input-keycode-dialog-20221114.webp)

为键代码生成的代码是这样的:

```javascript
// in the context of a scene:

const jumpKey = this.input.keyboard
        .addKey(Phaser.Input.Keyboard.KeyCodes.UP);

// in the context of a prefab:

 const jumpKey = this.scene.input.keyboard
        .addKey(Phaser.Input.Keyboard.KeyCodes.UP);
```

键的一种常用方法是将其分配到一个字段(设置 `Class` 范围),并以 ** 更新** 方法检查其** 下** 状态:

```javascript
update() {

    if (this.jumpKey,isDown) {

        this.player.body.velocity.y = -400;
    }
}
```

## 点击区域 {#hit-area}

制作交互式对象几乎是每个游戏的一部分。 您可以为检查器视图中的某个对象启用交互式命中区域。 您可以在 ** Hit 区域** 区域中选择对象交互区域的形状。 默认形状是 `NONE`, 也就是说对象根本没有命中区域 。

可用的命中区形状有:

* Rectangle
* Ellipse
* Circle
* Polygon
* 像素完美

![The hit area shapes](https://cdn.phaser.io/editor-docs/scene-editor-input-hit-area-options-20230517.webp)

每个形状都有用于形状属性的专用区域。除了该区域外,还可以激活**Edit Hit Area**工具(`I`),并通过拖动场景中的处理器来改变区域属性。

### 矩形命中区域 {#rectangle-hit-area}

设定一个矩形命中值在对象上, 请在 ** 希特区域** 的 ** 形状** 参数中选择 `RECTANGLE` 选项。 它允许 ** Hit 区域( 矩形) ** 区域, 您可以在此设定区域的位置和大小 :

![Enable rectangle hit area](https://cdn.phaser.io/editor-docs/scene-editor-input-hit-area-rectangle-20230517.webp)

另外,您还可以使用 ** Edit Hit 区域** 工具(`I`)更改值 :

![Changes rectangular hit area with the tool.](https://cdn.phaser.io/editor-docs/scene-editor-input-hit-area-rectangle-tool-20230517.webp)

当创建矩形命中区域时,场景编译器会生成这样的代码: .

```javascript
// eye
const eye = this.add.image(369, 277, "lance-overdose-loader-eye");
eye.setInteractive(
    new Phaser.Geom.Rectangle(17, 16, 90, 80),
    Phaser.Geom.Rectangle.Contains);
```

### 椭圆命中区域 {#ellipse-hit-area}

您可以设置一个椭圆形, 用于对象的命中区域。 在 ** 形状** 参数中选择 `ELLIPSE` 选项, 并修改 ** Hit 区域( 椭圆) ** 的椭圆属性 :

![Ellipse hit area](https://cdn.phaser.io/editor-docs/scene-editor-input-hit-area-ellipse-20230517.webp)

另外,您还可以使用 ** Edit Hit 区域工具** (`I`) 更改椭圆属性 :

![Edit ellipse hit area tool.](https://cdn.phaser.io/editor-docs/scene-editor-input-hit-area-ellipse-tool-20230517.webp)

[scene compiler](/editor/scene-editor/scene-compiler)生成的命中值是形状代码像这样:

```javascript
// chicken
const chicken = this.add.image(684, 126, "budbrain_chick");
chicken.setInteractive(
    new Phaser.Geom.Ellipse(30, 70, 66, 133),
    Phaser.Geom.Ellipse.Contains);
```

### 圆形命中区域 {#circle-hit-area}

您可以在 ** Hit 区域** 区域中通过 select effect 中将 `CIRCLE` 形状切换到对象上, 从而改变 ** Hit 区域( 环)** 区域中的圆半径和位置 :

![Set the circle hit area.](https://cdn.phaser.io/editor-docs/scene-editor-input-hit-area-circle-20230517.webp)

另外,您还可以使用 ** Edit Hit 区域工具** (`I`) 来更改圆形属性 :

![Circle hit area tool.](https://cdn.phaser.io/editor-docs/scene-editor-input-hit-area-circle-tool-20230517.webp)

[scene compiler](/editor/scene-editor/scene-compiler)生成代码,用于以此设定圆形区域:

```javascript
// wizball
const wizball = this.add.image(191, 161, "wizball");
wizball.setInteractive(
    new Phaser.Geom.Circle(46, 46, 46),
    Phaser.Geom.Circle.Contains);
```

### 多边形命中区域 {#polygon-hit-area}

您可以在 ** 希特区域** 部分选择 ** 形状** 参数中的 `POLYGON` 选项, 设置一个多边形命中区域。 多边形用数组点来制作。 这些点用字符串表示, 使用此语法: `"{P1.x} {P2.y} ... {Pn.x} {Pn.y}"`。 您可以更改 ** 希特区域( 波利贡) ** 中的点:

![Set polygon hit area.](https://cdn.phaser.io/editor-docs/scene-editor-input-hit-area-polygon-20230517.webp)

您可以在3 点按钮中单击以获取更大的文本框并编辑所有点 :

![Polygon points.](https://cdn.phaser.io/editor-docs/scene-editor-hit-area-polygon-points-20230517.webp)

或者可以使用**Edit Hit区域工具**(`I`)来添加,删除,并更改多边形的点:

![Polygon tool.](https://cdn.phaser.io/editor-docs/scene-editor-input-hit-area-polygon-tool-20230517.webp)

您可以将鼠标放在一条线上并拖曳粉红色点来添加点 :

![Add point to the polygon hit area.](https://cdn.phaser.io/editor-docs/scene-editor-input-polygon-tool-add-point-20230517.webp)

您可以将鼠标指针放在上面并按下 `Delete` 键删除多边形点。 删除点用红色突出显示:

![Delete polygon point.](https://cdn.phaser.io/editor-docs/scene-editor-input-polygon-delete-point-20230517.webp)

要修改点,请拖动它 QQ 。

[scene compiler](/editor/scene-editor/scene-compiler)生成设定多边形命中区域的代码, 像这样:

```javascript
// car
const car = this.add.image(616, 523, "supercars-parsec");
car.setInteractive(
  new Phaser.Geom.Polygon(
    "1 85 83 37 245 -0 381 3 574 13 597 57 586 76 603 88 562 115 548 140 510 162 456 147 316 139 158 146 110 160 68 149 0 138"
    ), Phaser.Geom.Polygon.Contains);
```

### 像素完美命中区域 {#pixel-perfect-hit-area}

为了让对象中的像素完美命中区域能够使用,在**Hit Area**区选择`PIXEL_PERFECT`选项,并将`alphaTolerance`设定在**Hit ARea(像素完美)**区:

![Pixel perfect hit area.](https://cdn.phaser.io/editor-docs/scene-editor-input-hit-area-pixel-perfect-20230517.webp)

** Alpha 容忍** 参数是“像素应高于的α级,以便作为成功的相互作用列入”。

[scene compiler](/editor/scene-editor/scene-compiler)生成以这种方式设置像素完美命中区域的代码:

```javascript
const ship = this.add.image(1000, 281, "thrust_ship2");
ship.setInteractive(this.input.makePixelPerfect());
```

---
