# 预制体的用户属性 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/prefabs/prefab-user-properties)

正如我们在前面几节中所提到的, Prefab 扩展了 Phaser 内置类型或另一个 Prefab 。 这意味着 Prefab 继承了 Phaser内置类型中定义的属性。 但是, 您可以选择定义新属性 。

具有Prefab用户属性,您可以创建更多可重复使用的预制体游戏。您可以表达游戏游戏概念:玩家的“健康”,硬币的“价值”,敌人的“速度”等。

## 创建预制体的用户属性 {#creating-a-prefab-user-property}

检查器视图中的 ** Prefab 属性** 部分显示创建新用户属性的按钮。 当您选择该场景( 点击该场景的空白空间) 时, 或当您在大纲视图中选择 ** Prefab Personality** 元素时, 此部分会显示 :

![The Prefabs Properties in the Outline view.](https://cdn.phaser.io/editor-docs/prefab-user-props-node-outline-view-20221102.webp)

点击 **Add 属性 ** 按钮创建新属性。 它打开了与不同属性类型的对话框 :

![Property types dialog.](https://cdn.phaser.io/editor-docs/prefab-user-props-add-property-dialog-20230626.webp)![Add Property button.](https://cdn.phaser.io/editor-docs/prefab-user-props-add-property-button-20230626.webp)

属性显示为 ** Prefab 属性** 元素的子 。 单击属性进行编辑 。

![Display all properties of a prefab.](https://cdn.phaser.io/editor-docs/prefab-user-props-as-children-outline-20221102.webp)

所有类型的属性都需要一些共同的参数,您应当提供:

* 属性的 ** 名称 **。 它被编译器用来生成属性声明代码。 它应该是有效的 JavaScript标识符 。
* ** Label **. 是**Name**的UI友好版本,例如,**maxSpeed**名称的标签可以是**Maxim speed**. 在代码中,生成了**maxSpeed**字段,但UI显示的是**Maxim sped**.
* **Tooltip**. 在UI中用作属性的证明文件。
* ** Is 矩阵类型** 旗帜。 如果启用, 属性是选定类型的数组 。
* ** 过失** 值。
* ** Custom 定义** 旗帜。 如果启用, 场景编译器会用属性声明跳过代码生成。 它允许您写入属性的自定义执行。 例如, 使用自定义获取器和设置器。 更多关于 [using properties with custom definition](/editor/scene-editor/prefabs/prefab-user-properties#using-properties-with-custom-definition) 的信息 。
* ** Editor Only ** 旗帜。 如果启用, 属性仅存在于编辑器中, 而不在生成的代码中编译。 它对于只用于编辑器元数据和功能的属性有用。 例如, 用于预制体的 [Object Display Format](/editor/scene-editor/prefabs/prefab-display-properties) 参数 。
* ** 已过期的** 旗帜。 如果启用, 属性会被标记为已过期。 已过期属性将被隐藏在检查器视图中, 除非解锁。 如果您想要淘汰一个属性, 请使用此旗帜, 但保留它以进行后向兼容 。

![Common parameters of a property.](https://cdn.phaser.games/oss-docs/assets/1caf6cbb62eb7160-prefab-user-props-common-params-20251122.webp)

属性部分的菜单显示以下动作:

* 更改属性类型 。
* 删除属性。

要更改属性的顺序, 请使用上下文菜单的 ** Edit ** → ** Move ** 命令 。

您可以撤销/重做所有这些更改 。

![Property menu.](https://cdn.phaser.io/editor-docs/prefab-user-props-menu-20230627.webp)

## 简单属性类型 {#simple-property-type}

** 数字 ** 、 ** String ** 和 ** Boolean ** 属性是最简单的。 场景编译器生成属性为类字段。 请注意, 每个属性被设定为 ** Default** 值 :

```javascript
class Dragon extends Phaser.GameObjects.Sprite {

    constructor(scene, x, y, texture, frame) {
        super(...);

        ...
    }

    /** @type {number} */
    maxSpeed = 100;

    /** @type {"fire"|"smoke"|"laser"} */
    flameType = "fire";

    /** @type {(obj:Dragon)=>void} */
    onClickHandler = obj => {};
}
```

## 备选属性类型 {#option-property-type}

选项类型允许用户选择一个预定义的字符串值。 它就像传统的enum类型。 除了常见参数外, 选项属性还有** 选项** 参数。 您应该用有效的 JSON 矩阵语法来写入所有可能的值 :

![The Options parameter of the Option property.](https://cdn.phaser.io/editor-docs/prefab-user-props-options-param-06062020.webp)

注意** 默认值** 应为可能值之一。

编译的地产是这样的:

```javascript
class Dragon extends Phaser.GameObjects.Sprite {

    constructor(...) {
        super(...);
        ...
    }

    /** @type {"fire"|"smoke"|"laser"} */
    flameType = "fire";
}
```

## 颜色属性类型 {#color-property-type}

色彩属性类型接受带有颜色格式的字符串值,它提供了一个对话框,用于选择一个颜色,并以六进制格式(包括α组件)返回它.

![The color property editor.](https://cdn.phaser.io/editor-docs/prefab-user-props-color-type-20220409.webp)

场景编译器生成定义这样一个色彩属性的代码 :

```javascript
class GoToSceneButton extends Phaser.GameObjects.Image {

    ...

    /** @type {string} */
    fadeOutColor = "#ffffffff";
}
```

生成设置在场景中的属性的代码 :

```javascript
// goToSceneButton (prefab fields)
goToSceneButton.fadeOutColor = "#ff00b5ff";
```

代表一种颜色的方式有很多种,你可以使用[Phaser.Display.Color](/api/class/display-color)类转换成不同的格式.

## 表达式属性类型 {#expression-property-type}

表达式类型是您创建任何类型属性的方式。 您可以使用任意类型来设定值和任何 JavaScript 表达式。 例如, 您可以使用它来创建属性来引用事件处理器( 或召回函数) :

![Expression property declaration.](https://cdn.phaser.io/editor-docs/prefab-user-props-expression-param-06062020.webp)

场景编译器生成这样的表达式属性 :

```javascript
class Dragon extends Phaser.GameObjects.Sprite {

    constructor(..) {
        ...
    }

    /** @type {(obj:Dragon)=>void} */
    onClickHandler = obj => {};
}
```

## 对象可变属性类型 {#object-variable-property-type}

此用户属性类型是用于引用场景中的对象的。 它提供了一个对话框, 用于选择场景中的对象, 并设定为属性的值, 变量引用对象的名称 :

![The object reference editor.](https://cdn.phaser.io/editor-docs/prefab-user-props-object-variable-20220409.webp)

如果 [Expression property type](/editor/scene-editor/prefabs/prefab-user-properties#expression-property-type) 的子集, 则该属性类型。 您可以定义属性的类型。 默认情况下, 它就是 `Phaser.GameObjects.Game`, 但是您可以写入其它类型 。

```javascript
class Eagle extends Phaser.GameObjects.Sprite {

  ...

  /** @type {Phaser.GameObjects.GameObject} */
  attackTarget;
}
```

此属性的值集是逐字复制到生成代码 :

```javascript
// eagle (prefab fields)
eagle.attackTarget = player;
```

## 游戏对象 引用属性类型 {#game-object-reference-property-type}

游戏对象引用属性类型与[Object Variable property type](#object-variable-property-type)相似,但允许严格从场景中选择游戏对象,并与对象保持真实链接。在对象变量属性类型中,该值只是一个引用对象的变量名称的字符串。在游戏对象引用属性类型中,该数值是对象本身的引用(ID),因此,如果您更改了引用对象的变量名称,链接就不会丢失.

另一个不同之处是,Game Object Reference属性允许设定对它可以引用的对象的限制,这个限制是基于[prefab tags](/editor/scene-editor/prefabs/prefab-tags)或游戏对象类型.

例如,如果想要属性只用于引用带有`enemy`标记的对象,可以这样定义属性:

![game object reference filters](https://cdn.phaser.games/oss-docs/assets/965adfce2392b9c4-scene-editor-object-reference-property-f.webp)

** Filter Tags ** 参数允许您设置一个逗号分隔的标签列表。 属性将只允许选择至少包含一个标签在此参数中定义的对象。 要选择标签, 您可以使用参数旁边的“ 文件夹” 图标。 它会打开一个对话框, 并打开工程中定义的标签列表。 您可以选择一个或多个标签 。

** Filter 操作员** 参数允许您设置操作员过滤对象。可用的操作员是 ** Match All** 和 ** Match Any** 。** Match All**操作员表示对象必须拥有在 ** Filter 标记** 参数中定义的所有标记。** Match Any**操作员表示对象至少必须拥有在 ** Fillter 标记** 指标中定义的标记之一。

除了基于标签的过滤, 您还可以通过游戏对象类型过滤。 例如, 如果您想要将属性仅用于`Phaser.GameObjects.Sprite`类型的参考对象, 您可以设置 Sprite 值为 ** Filter 对象类型** 属性。 在属性旁边有一个按钮来选择该类型 :

![Set the game object type filter](https://cdn.phaser.games/oss-docs/assets/d3247efd5e71d33e-scene-editor-object-reference-property-f.webp)

## 对象构造属性类型 {#object-constructor-property-type}

有了这种属性类型,您可以创建一个持有对象构造器的用户属性(用另一种方式表达:类)。它就像[Expression property type](/editor/scene-editor/prefabs/prefab-user-properties#expression-property-type),但是有一个对话框来选择一个预制体类或内置的游戏对象类。

查看下一张图像,您如何选择一个预制体或内置的 Phaser 类型作为表达式 :

![Object Constructor property type](https://cdn.phaser.io/editor-docs/prefab-user-props-object-ctr-20220427.webp)

它将产生这样的属性定义:

```javascript
bulletCtr!: typeof Cherry & typeof Gem = Cherry;
```

这意味着,您可以使用该属性创建新对象,**Chery**或**Gem**对象:

```javascript
createBullet(x: number, y: number) {

    const bullet = new this.bulletCtr(this.scene, x, y);

    return bullet;
}
```
## 事件属性类型 {#event-property-type}

这种属性允许从 Phaser 事件列表中选择事件名称, 并自定义事件。 它还允许写入任意事件名称 。

要打开可用事件列表, 请单击搜索按钮。 它打开了 Phaser 和自定义事件对话框 :

![Select an event name.](https://cdn.phaser.io/editor-docs/prefab-user-props-select-event-name-20230626.webp)

当单击事件名称时,对话框的下方窗格显示文档。


### 动态键盘事件 {#dynamic-keyboard-events}

Phaser提供了特殊的`Phaser.Input.Keyboard.Events.KEY_DOWN`和`Phaser.Input.Keyboard.Events.KEY_UP`事件,这些活动允许收听`KeyCodes`类中定义的键,并以此方式组合: .

```javascript
this.input.keyboard.on('keydown-SPACE', listener);
```

`SPACE`在`KeyCodes`类中属于常数的,`keydown`(或称`keyup`)是事件的名称.

事件属性对话框显示 `keydown-`和 `keyup-` 的所有组合, 并带有 `KeyCodes` 值 。

![Keyboard events.](https://cdn.phaser.io/editor-docs/prefab-user-props-keydown-events-20230626.webp)

### 动态动画事件 {#dynamic-animation-events}

从Phaser文档中:

动画"完整的动态键事件".

当一个动画在它上播放完成播放时,这个事件由Sprite发出.
当动画到达其序列的尽头时, 就会发生这种情况, 将任何延迟都考虑在内
或者重复它可能必须处理。

这与**ANIMATION_COMPLETE**事件的不同之处在于,这起事件有一个动态事件名称,包含其中的动画名称.
例如,如果你有名为爆炸的动画,你可以通过使用:

`sprite.on('animationcomplete-explode', listener)`

事件属性对话框收集您项目 [animation files](/editor/animations-editor/intro) 中所有可用的动画, 并生成 `animationcomplete-key` 事件 :

![Dynamic animation events.](https://cdn.phaser.io/editor-docs/prefab-user-props-dynamic-animation-events-20230626.webp)


### 动态旋柱事件 {#dynamic-spine-events}

[Spine](https://esotericsoftware.com) 模板包含在动画的某一时刻发射的用户事件。事件属性对话框显示所有定义的事件 [Spine](https://esotericsoftware.com) 模板中存在的 [Asset Pack files](/editor/asset-pack-editor/asset-pack-file):

![Spine events.](https://cdn.phaser.io/editor-docs/prefab-user-props-spine-events-20230927.webp)

[Learn more about the Spine events](https://esotericsoftware.com/spine-events)

**Event**属性类型是一种普通类型,允许选择不同的Phaser事件,包括斯宾事件。但是,如果您想要创建一个属性,专门用于选择斯宾事件,则可以使用**Spine Event**属性类型。

### 自定义事件 {#custom-events}

除了 Phaser 事件, 对话框还显示 `events.txt` 文件定义的自定义事件。 自编辑器的3. 62.0 版本以来, 此文件包含在所有工程模板中。 然而, 您可以在您的工程的任意文件夹中创建此文件。 语法非常简单。 每行中, 您定义一个事件, 并且名称和文件与空格分隔。 例如 :

```bash
my-event-name My event name documentation

# the editor ignores all lines starting with #
other-event My other event.
```

之后,事件属性对话框将显示列表开头的自定义事件:

![Custom events.](https://cdn.phaser.io/editor-docs/prefab-user-props-custom-event-20230626.webp)


### 事件代码生成 {#event-code-generation}

场景编译器生成事件属性如下:

```bash
class Dragon extends Phaser.GameObjects.Sprite {

        constructor(..) {
                ...
        }

        jumpEvent = Phaser.Input.Events.GAMEOBJECT_POINTER_DOWN;
}
```
## 键代码属性类型 {#key-code-property-type}

这种属性允许选择 `Phaser.Input.Keyboard.KeyCodes` 类中可用的键代码之一 :

![KeyCode property.](https://cdn.phaser.io/editor-docs/prefab-user-props-keycode-1-20230627.webp)![KeyCode dialog.](https://cdn.phaser.io/editor-docs/prefab-user-props-keycode-2-20230627.webp)

您可以使用该类型的属性来约束某个对象的行为或游戏动作,并使用某个键盘键.


## 属性代码生成 {#property-code-generation}

场景编译器生成键代码属性如下:

```javascript
class Dragon extends Phaser.GameObjects.Sprite {

        constructor(..) {
                ...
        }

        private jumpKey: number = Phaser.Input.Keyboard.KeyCodes.UP;
}
```
## 纹理配置属性类型 {#texture-config-property-type}

这类属性允许在一个“资源包”文件中定义的所有纹理之间选择一个纹理。当选择纹理时,属性会得到纹理配置值。例如,如果选中的纹理是带有** 背面** 键的图像,则属性被设定为:

```javascript
{ "key": "background" }
```

如果选中的纹理是图集**阿特拉斯-道具**的框** 分支-01**,则属性设定为:

```javascript
{ "key": "atlas-props", "frame": "branch-01" }
```

![The Texture Config property.](https://cdn.phaser.io/editor-docs/prefab-user-props-texture-config-param-09102020.webp)

场景编译器生成像这样的纹理配置属性 :

```javascript
class Dragon extends Phaser.GameObjects.Sprite {

    constructor(..) {
        ...
    }

    /** @type {{key:string,frame?:string|number}} */
    myTexture = {"key":"atlas-props","frame":"branch-01"};
}
```
## 资源 键属性类型 {#asset-key-property-type}

资源键属性类型就像简单的字符串属性类型, 但允许打开一个对话框, 与工程中定义的所有 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 键进行对齐。 然后, 当您在对话框中选择一个键时, 它将被设定为属性的值 。

![Select asset key value.](https://cdn.phaser.io/editor-docs/prefab-user-props-asset-key-param-09102020.webp)

场景编译器生成这样的“资源键”属性 :

```javascript
class Dragon extends Phaser.GameObjects.Sprite {

    constructor(..) {
        ...
    }

    /** @type {string} */
    myAssetKey = "acorn-3";
}
```

## 动画键属性类型 {#animation-key-property-type}

这种类型就像[Asset Key property type](/editor/scene-editor/prefabs/prefab-user-properties#asset-key-property-type),但对话框只显示项目中定义的动画.

在动画键字段旁边,有一个用于选择动画键的按钮和一个用于预览所选动画的按钮:

![Animation Key property definition](https://cdn.phaser.io/editor-docs/prefab-user-props-animation-key-section-20231027.webp)

这是选择动画键的对话框 :

![A dialog for selecting the animation key.](https://cdn.phaser.io/editor-docs/prefab-user-props-animation-key-dialog-20231027.webp)

这是预览所选动画的对话框 :

![Animation key preview.](https://cdn.phaser.io/editor-docs/prefab-user-props-animation-key-preview-dialog-20231027.webp)

## 音频键属性类型 {#audio-key-property-type}

此类型类似于 [Asset Key property type](/editor/scene-editor/prefabs/prefab-user-properties#asset-key-property-type), 但对话框只显示音频资源 :

![Audio Key property type.](https://cdn.phaser.io/editor-docs/prefab-user-props-audio-key-param-09102020.webp)

## 场景键属性类型 {#scene-key-property-type}

此用户属性类型允许任意字符串值, 但为选择一个场景键提供了对话框。 此对话框显示工程的所有场景, 您可以选择一个场景。 然后, 其键被设定为值 。

![The scene key editor.](https://cdn.phaser.io/editor-docs/prefab-user-props-scene-key-20220409.webp)

场景编译器生成这样场景键属性 :

```javascript
class GoToSceneButton extends Phaser.GameObjects.Sprite {

    constructor(..) {
        ...
    }

    /** @type {string} */
    jumpTo;
}
```

现场产生的代码是这样的:

```javascript
// goToSceneButton (prefab fields)
goToSceneButton.jumpTo = "Level";
```

## 斯皮尔( Spine) 名称属性类型 {#spine-skin-name-property-type}

此用户属性类型允许任意字符串值, 但为选择 Spine 骨架皮肤提供了一个对话框。 此对话框列出所有定义的皮肤的名称 。 [Spine](https://esotericsoftware.com) 骨架资源 [Asset Pack files](/editor/asset-pack-editor/asset-pack-file) 中。您可以选择一个名称,然后将其设定为属性的值。

![Spine skin dialog.](https://cdn.phaser.io/editor-docs/spine-animations-user-property-skin-20230927.webp)

场景编译器生成 Spine Skin Name 这样的属性 :

```javascript
class Player extends SpineGameObject {

    constructor(..) {
        ...
    }

    theSkin: string;
}
```

现场产生的代码是这样的:

```javascript
player.theSkin = "Wolf02";
```

## Spine 动画名称属性类型 {#spine-animation-name-property-type}

此用户属性类型允许任意字符串值, 但为选择动画名称提供了一个对话框。 此对话框列出所有定义的动画名称 。 [Spine](https://esotericsoftware.com) 骨架资源 [Asset Pack files](/editor/asset-pack-editor/asset-pack-file) 中。您可以选择一个名称,然后将其设定为属性的值。

![Spine animation name dialog.](https://cdn.phaser.io/editor-docs/spine-animations-user-properties-animation-20230927.webp)

场景编译器生成 Spine 动画名称属性 :

```javascript
class Player extends SpineGameObject {

    constructor(..) {
        ...
    }

    startAnimation: string;
}
```

现场产生的代码是这样的:

```javascript
player.startAnimation = "idle";
```

## Spine 斯洛特名称属性类型 {#spine-slot-name-property-type}

此用户属性类型允许任意字符串值, 但为选择 Spine 骨架槽名称提供了一个对话框。 此对话框列出所有定义的槽的名称 。 [Spine](https://esotericsoftware.com) 骨架资源 [Asset Pack files](/editor/asset-pack-editor/asset-pack-file) 中。您可以选择一个名称,然后将其设定为属性的值。

![Slot name user property](https://cdn.phaser.games/oss-docs/assets/17dfd28bf2f4d5da-user-property-spine-slot-name-20251121.webp)

位址名称选择对话框按骨架资源将位址名称分组 :

![Slot name selection dialog](https://cdn.phaser.games/oss-docs/assets/b7e1a0a88b1af89f-user-property-spine-slot-name-dialog-202.webp)

## JSON 属性类型 {#json-property-type}

JSON 属性类型允许您创建可以持有 JSON 数据的用户属性。 它提供了输入 JSON 格式化文本的文本区域, 它验证输入, 以确保它有效 JSON 。 校验是基于标准的 JSON 语法和 ** JSON Schema** 参数, 如果提供了的话 。

以`items`属性为对象的JSON 计划为例, 我们用`name`和`points`字段来编组拖拉图:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "points": {
            "type": "number"
          }
        },
        "required": ["name", "points"],
        "additionalProperties": false
      }
    }
  },
  "required": ["items"],
  "additionalProperties": false
}
```

![JSON property declaration](https://cdn.phaser.games/oss-docs/assets/071b4159ce07abc7-user-property-json-property-20251121.webp)

要编辑 JSON 数据, 编辑器会显示一个专用对话框, 并带有语法突出显示、 验证和自动补全 :

![JSON editor](https://cdn.phaser.games/oss-docs/assets/a29e5b3199b196d2-user-property-json-edit-20251121.webp)

场景编译器生成 JSON 值为 JSON 对象 :

```javascript
myPrefab.myData = {
    "items": [
        {
            "name": "coin",
            "points": 10
        },
        {
            "name": "apple",
            "points": 5
        }
    ]
```

## 矩阵属性类型 {#array-properties-types}

Phaser编辑器 5 中新建了我们添加了对类型矩阵的用户属性的支持。 这样您就可以创建可以持有多个值的属性, 如项目列表或对象集合。 这意味着您可以将任何先前的用户属性类型声明为矩阵 。

要声明一个属性为矩阵, 您可以设置 ** Is 矩阵类型 ** 旗 :

![Declare array user property](https://cdn.phaser.games/oss-docs/assets/35b03bf9971e8182-scene-editor-user-property-array-flag-20.webp)

当您选择此选项时, **Type ** 参数成为 ** 项目类型 ** 参数,并提及矩阵项的类型。 ** Default** 参数成为 ** Default 项目** 参数,并提及了矩阵项的默认值。

此外,您还可以设置数组的默认项目。 **Default Array ** 参数显示默认数组项目的列表。 您可以添加、 删除或编辑数组元素 :

![Array user property default items](https://cdn.phaser.games/oss-docs/assets/31fde76338920aad-scene-editor-user-property-array-2025060.webp)

用于在预制体文件及用户组件实例中设置数组值的 UI 十分相似:

![Array user property in a prefab instance](https://cdn.phaser.games/oss-docs/assets/e8d8533b6a2728f2-scene-editor-user-proeprty-array-prefab-.webp)

## 初始化其他属性 {#initializing-other-properties}

可能您想要改变预制体实例的其他属性, 以依赖用户属性的值。 例如, 如果** flameType** 属性值是 `"fire"`, 那么您将天体质量设置为 `50`。 由于属性值不是设置在构造器中, 您可以监听 `scene-awake`事件并设置天体属性 :

```javascript
class Dragon extends Phaser.GameObjects.Sprite {

    constructor(scene,...) {
        ...

        /* START-USER-CTR-CODE */

        scene.events.once("scene-awake", this.awake, this);

        /* END-USER-CTR-CODE */
    }

    /** @type {"fire"|"smoke"|"laser"} */
    flameType = "fire";

    /* START-USER-CODE */

    awake() {

        // at this point, all objects in the scene are created
        // and the user properties are set with new values

        if (this.flameType === "fire") {
            this.body.mass = 50;
        }
    }

    /* END-USER-CODE */
}
```

如果您启用了 ** 编译器 Prefab 设置** 中的 ** Generate Awake Hanler ** 旗, 场景编译器会为您生成此代码:

![Generate awake event handler.](https://cdn.phaser.io/editor-docs/scene-editor-prefab-settings-08212021.webp)
```javascript
class Level extends Phaser.GameObjects.Image {

    constructor(scene,...) {

        // awake handler
        this.scene.events.once("scene-awake", () => this.awake());

        ...
    }
}
```

写`awake`方法是你的责任

### `scene-awake`事件 {#the-scene-awake-event}

`scene-awake`事件不是Phaser API的一部分。这是场景编辑器用作常规的自定义事件。当场景编译器生成场景代码时,它也会生成释放`scene-awake`事件的代码。在所有对象创建后,此事件即被发布:

```javascript
class Level extends Phaser.Scene {
...
    editorCreate() {
        ...

        // dragon
        const dragon = new Dragon(this, 370, 218);
        this.add.existing(dragon);

        ...

        // dragon (prefab fields)
        dragon.maxSpeed = 300;
        dragon.flameType = "smoke";
        dragon.onClickHandler = obj => this.selectDragon(obj);
        ...

        this.events.emit("scene-awake");
    }
...
}
```

正如我们在前面的章节中所提到的,预制体和[user components](/editor/scene-editor/user-components)可以听这个事件读取设定到用户属性的值.

重要的是,你要记住,如果你创建动态预制体实例,并且它需要`scene-awake`事件,那么你应该手动称呼它:

```javascript
spawnDino(scene, x, y, flame) {

    const dragon = new Dragon(scene, x, y);
    dragon.flameType = flame;
    // send the awake notification to the new object
    scene.events.emit("scene-awake");
}
```

由于`scene-awake`事件在预制体和[user components](/editor/scene-editor/user-components)中被听一次,所以只有新对象才会被通知.

作为`scene-awake`事件的其他选择,您可以聆听`Phaser.Scenes.Events.UPDATE`事件。它由现场在每一次滴答时释放,所以您只需要注册收听者,以被叫做**ce**:

```javascript
scene.events.once("Phaser.Scenes.Events.UPDATE", this.start, this);
```

请注意,如果在游戏开始更新前需要“醒”前,您应该听`scene-awake`事件。

`scene-awake`事件也被组件[learn more about it](/editor/scene-editor/user-components/user-components-awake-event)使用.

## 使用自定义属性 {#using-properties-with-custom-definition}

您可以使用 ** 海关定义** 设置用户属性 :

![Set custom definition flag.](https://cdn.phaser.io/editor-docs/prefab-user-properties-initializing-custom-prop-07092021.webp)

这意味着, 场景编译器跳过属性定义。 例如, 如果您将 `flameType` 设置为 ** Custom Definition**, `flameType` 属性声明没有生成。 相反, `flameType` 属性初始化包含在构造器中 :

```javascript
class Dragon extends Phaser.GameObjects.Sprite {

    constructor(scene,...) {
        ...

        // the compiler adds this
        this.flameType = "fire";
    }

    // the compiler skips this:
    // flameType = "fire";
}
```

然后,您可以写一个自定义设置器,并初始化预制体文件的其他字段:

```javascript
class Dragon extends Phaser.GameObjects.Sprite {

    constructor(scene,...) {
        ...
        this.flameType = "fire";
    }

    /* START-USER-CODE */

    set flameType(flameType) {

        // update the body with the flameType

        if (flameType === "fire") {
            this.body.mass = 50;
        }
    }

    /* END-USER-CODE */
}
```

请注意, 您不再需要再听 `prefab-awake`事件。 设置 `flameType` 属性将按预期方式更新预制体状态。 您可能需要定义 `flameType` 的获取器。 如果是这样, 您可以将其值存储在新字段中, 或者计算它 。

## 预制体实例中的用户属性 {#user-properties-in-a-prefab-instance}

这就是您在 Prefab 中定义的属性在 Prefab 文件的 ** Prefab 实例的 一节中被显示的方式 :

![User properties in a prefab instance.](https://cdn.phaser.io/editor-docs/prefab-user-props-prefab-instance-20230627.webp)

检查器视图显示对象的每个 Prefab( 和 prefab 变体) 的一节。 用户属性与 Prefab 实例的其他属性一样 。

每个部分包含一个菜单,其中包含选项:

* **打开预制体**: 打开预制体文件。
* **选择全部预制体**: 选择场景中的所有对象, 在同一预制体位置上进行跳动。

![Prefab instance section and menu.](https://cdn.phaser.io/editor-docs/prefab-user-props-prefab-instance-menu-20230627.webp)

由场景编译器生成的创建 Prefab 实例并初始化属性的代码将看起来类似以下。 注意** dragon** 实例是先创建的, 用户属性是后初始化的, 其结尾处设置用户属性, 允许您设定引用到场景中创建的另一个对象 :

```javascript
class Level extends Phaser.Scene {
...
    create() {
        ...

        // dragon
        const dragon = new Dragon(this, 370, 218);
        this.add.existing(dragon);

        ...

        // dragon (prefab fields)
        dragon.maxSpeed = 300;
        dragon.flameType = "smoke";
        dragon.onClickHandler = obj => this.selectDragon();
        dragon.emit("prefab-awake");
        ...
    }
...
}
```

下一节将讨论创建 Prefab 实例和更改属性的主题。

---
