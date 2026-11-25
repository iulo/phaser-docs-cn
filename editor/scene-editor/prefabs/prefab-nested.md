# 嵌套预制体 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/prefabs/prefab-nested)

巢穴预制体是一个强大的概念,与整体的预制体概念一样,它受[Unity Engine](https://unity.com)的启发,它的名字描述了它的目的:允许巢穴预制体.

有许多情况下, 您的预制体文件是对象的复合体, 您想要在预制体文件中修改它们。 例如, 请看看这个 ** AlienShip** 预制体文件 :

![AlienShip, a prefab with nested prefabs.](https://cdn.phaser.io/editor-docs/scene-editor-nested-prefab-alienship-08182021.webp)

这是一个容器,有一个**外国人**和一个**船只**子对象。

当你创建了 lienPrefab 的 例( 即容器的例) , 您可以改变其位置和大小。 这是自定义属性。 但你不能改变 lien 或 lien 子对象 的 属性 。

但如果你把**alien**和**ship** 物体宣布为巢状预制体,你可以在预制体中访问它们.

将对象设置为嵌套预制体文件时,您可在**可变** 部分的** STED_PREFAB**参数中选择 ** Specope** 选项:

![Setting the nested prefab scope.](https://cdn.phaser.io/editor-docs/scene-editor-nested-prefab-scope-20230516.webp)

带有**NESTED_PREFAB**范围的变量作为公共字段生成。它类似于**PUBLIC**范围,但允许在预制体情况下修改对象。


## 嵌套预制体实例 {#nested-prefab-instances}

当创建包含嵌套预制体文件的预制体文件实例时, 大纲视图会显示嵌套预制体件。 另外, 场景编辑器允许选择嵌套预制体文本实例 :

![Prefab instance with nested prefabs.](https://cdn.phaser.io/editor-docs/scene-editor-nested-prefab-instance-08192021.webp)

注意** AlienShip 的 place 预fab 实例中的 嵌套式预fab 实例 **ship ** 的纹理不同。 Nested 预fab 例和预fab 实例一样有效: 对于改变一个属性, 它首先需要解锁该属性 :

![Changing the texture property of a nested prefab instance.](https://cdn.phaser.io/editor-docs/scene-editor-nested-prefab-instance-change-texture-08192021.webp)

为**alien1**对象生成的代码是这样的:

```javascript
// alien1
const alien1 = new AlienShip(this, 142, 398);
this.add.existing(alien1);
alien1.ship.setTexture("shipYellow");
```

注意巢型预制体**船**是预制体**阿利安1**的一个场.

## 巢的预制体构造器和Xargs {#the-nested-prefab-constructor-and-the-xargs}

在大多数情况下,当用户修改了现场一个嵌套预制体器的属性时,场景编译器会生成一个像我们在前一个例子中看到的代码: .

```javascript
alien1 = new AlienShip(this, 142, 398);
// ...
// change the texture of the nested prefab instance **ship**
alien1.ship.setTexture("shipYellow");
```

`alien1`是母体前方fab的例子,`ship`是嵌入式前方fab的例子;`setTexture()`是修改`texture`属性的方法。但是,对于绝大多数Phaser支持的对象类型来说,这是真实的,但是有些对象类型只在构造器中接收其属性。这意味着一旦对象被创建,它就不能通过属性来修改。

如果嵌套预制体**船**不允许通过方法或属性来修改其纹理,但必须在构造器中传递。然而,从场景来看,我们只创建了母预制体**AlienShip**的实例。它是在**AlienShips**类中创建的**船**物体:

```javascript
class AlienShip extends Phaser.GameObjects.Container {

    constructor(scene, x, y) {
        super()
        // ...
        this.ship = scene.add.image(10, 10, "shipBlue");
    }
}
```

如你所见,**船**收到其构造器中的纹理**``shipBlue``**。如果我们想改变**船**的纹理,我们也应该通过**船**的纹质**的论点。它看起来是这样的:

```javascript
class AlienShip {
    constructor(scene, x, y, key, frame, ship_key, ship_frame) {
        // ...
        this.ship = scene.add.image(scene, 10, 10, ship_key ?? "shipBlue", ship_frame);
    }
}
```

现场的密码是:

```javascript
alien1 = new AlienShip(this, 142, 398, "shipYellow");
```

这可以是一个选择,但缺点是,在前部含有多个巢状前部,而每个巢状前部又拥有其他巢状前部,母体前部的构造器变得非常长,难以读取,因为它必须包含所有巢状前部的所有参数.

因此,为了简化构造器,场景编译器会使用一个特殊的参数来表示名为**xargs**(extra 参数)的预制体构造器。该参数包含所有嵌套预制体器的配置,格式为平原JavaScript对象,嵌套预制体件将访问它来取其参数。上面的例子生成的代码会看起来类似这样:

在父前页中** AlienShip**:

```javascript
class AlienShip {
    constructor(scene, x, y, xargs) {
        // ...
        this.ship = scene.add.image(scene, 10, 10, xargs?.ship?.key ?? "shipBlue", xargs?.ship?.frame);
    }
}
```

现场:

```javascript
alien1 = new AlienShip(this, 142, 398, { 
        ship: {
            key: "shipYellow" 
        }
    });
```

如果筑巢的预制体** 本身是筑巢的预制体机** 引擎** 在这种情况下, 母的预制体** AlienShip** 的代码会像这样:

```javascript
class AlienShip {
    constructor(scene, x, y, xargs) {
        // ...
        this.ship = new Ship(scene, 10, 10, xargs?.ship?.key ?? "shipBlue", xargs?.ship?.frame, { ...xargs?.ship, engine: xargs?.ship?.engine });
    }
}
```

以法语为主:

```javascript
alien1 = new AlienShip(this, 142, 398, { 
        ship: {
            key: "shipYellow",
            engine: {
                key: "engines",
                frame: "red"
            } 
        }
    });
```

目前,只有[SpineGameObject](/editor/scene-editor/spine-animations/spine-animations-game-object)类型和所有[Box2D](/editor/scene-editor/box2d-physics)对象类型才需要使用**xargs**参数.

## 无法处理的嵌套预制体事件 {#things-you-cannot-do-with-nested-prefab-instances}

在实践中,巢状的前叶像前叶,有一定区别:

(记住预制体是类型,模板,预制体是场景中预制体的实现).

* 在代码中,一个预制体文件是用户 JavaScript 类。一个嵌套预制体文件是预制体文件的一部分。它是由预制体文件类域引用的对象。
* 您无法定义嵌套预制体文件的用户属性( 请检查下面的注释) 。
* 您不能删除嵌套预制体实例 。
* 您不能改变嵌套预制体实例的类型 。

嵌套预制体是嵌套预制体的一部分。其类型可以是内置的 Phaser 类型或预制体。如果嵌套预制体有 Phaser 内置类型,则无法定义该嵌套预制体的用户属性。但是,如果嵌套预制体本有类型,则可以定义该嵌套预交件的用户属性。换句话说,如果需要将自定义属性添加到嵌套预制体(**A**),那么您可以创建一个带用户属性的分隔预制体场景(**B**),并且使用该预制体**B****作为创建嵌套预制体**A**。

---
