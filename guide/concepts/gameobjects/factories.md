# 游戏对象工厂 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/factories)

## 游戏对象厂 {#game-object-factory}

游戏对象工厂的角色是为您创建游戏对象并加入场景,使其立即准备使用.

工厂本身是一个很小的类,只提供几个属性和钩子,其力量来自所有游戏对象都用它自己注册,用新方法动态扩展该类,甚至可以创建自己的游戏对象,包含工厂功能,允许您扩展工厂以适应自己的需要.

每个场景都有一个 `GameObjectFactory` 类实例。 默认情况下, 这是绘制到 Scene 的 `add` 属性 。 例如, 这里要说明如何通过游戏对象工厂创建 Sprite :

```js
const sprite = this.add.sprite(x, y, key);
```

内部,游戏对象工厂本身没有实际的`sprite`方法。 如果您要在编辑器中打开类文件, 就不会找到它。 这是因为每个游戏对象都负责自己的工厂功能。 这里有一个用于Sprite :

```js
GameObjectFactory.register('sprite', function (x, y, texture, frame)
{
    return this.displayList.add(new Sprite(this.scene, x, y, texture, frame));
});
```

此代码可以在Phaser仓库内的`src/gameobjects/sprite/SpriteFactory.js`文件中找到. 几乎所有游戏对象都有类似的`Factory.js`文件,它们负责自己在工厂注册.

可见,代码将调用静态的`GameObjectFactory.register`函数,并传递给它自己的工厂函数的名称,`sprite`,以及回调。`register`函数将带回这个调用,并添加到工厂,在`sprite`属性下。

而这个回调就是在游戏代码中每次使用`this.add.sprite`时都会被引用。在这种情况下,它负责创建Sprite实例并将其添加到显示列表中,但任何实际逻辑都可以在这里发生.

调用回调被引用为游戏对象工厂作为上下文, 意思是调用中 `this` 是该厂本身的参考。 这就是为什么您可以看到它访问 `this.displayList` 属性。 这是游戏对象工厂类中可用的属性, 这是对 Scene 显示列表的参考 。

必须明白,虽然每个场景都有自己的游戏对象工厂的实例,但游戏对象在工厂的注册是全球性的,这意味着一旦一个游戏对象注册,其工厂功能就可以从游戏中任意场景中获取.

最终, Factory 完全是为了方便。 它允许您创建游戏对象而无需担心其创建的内部细节。 它还允许您用自己的游戏对象来扩展 Factory, 甚至可以覆盖现有的游戏对象, 允许您定制 Factory 来适应您的需要 。

### 如何绕过游戏对象厂 {#how-to-bypass-the-game-object-factory}

如果您想要创建游戏对象而不使用 Factory , 您可以直接调用游戏对象构建器。 例如, 要创建 Sprite , 您会这样做 :

```js
const sprite = new Phaser.GameObjects.Sprite(scene, x, y, key);

sprite.addToDisplayList();
```

### 删除工厂函数 {#removing-a-factory-function}

如果游戏对象工厂已经有一个用指定名称注册的功能, 它会简单地跳过其它任何对应名称的重命名。 因此, 如果您想要用自己的功能替换一个内部的 Phaser 游戏对象, 您需要先删除已有的条目, 然后再添加您的条目 。

你可以使用`remove`方法来做到这一点:

```js
Phaser.GameObjects.GameObjectFactory.remove('sprite');
```

这将从工厂中移除 `sprite` 方法, 允许您添加您自己的名称 。 这个过程是立即的 。

### 将自定义游戏对象添加到游戏对象厂 {#adding-custom-game-objects-to-the-game-object-factory}

您可以通过在游戏中添加自己的游戏对象来扩展游戏对象工厂。 这样做的方法是将静态的 `register` 方法调用在工厂本身上。 这种方法需要两个参数: 游戏对象的名称, 以及一个将创建其实例的回调函数 。

以下是我们自定义的游戏对象的简单类:

```js
class Bomb extends Phaser.GameObjects.Sprite
{
    constructor (scene, x, y)
    {
        super(scene, x, y, 'bomb');

        this.setScale(0.5);
    }

    preUpdate (time, delta)
    {
        super.preUpdate(time, delta);

        this.rotation += 0.01;
    }
}
```

这是一个非常简单的游戏对象,可以扩展Sprite类。它是一个在屏幕上旋转的炸弹,由`preUpdate`的旋转管理。我们将使用`bomb`键在游戏对象工厂注册。我们将用我们的Scene `init`方法做到这一点:

```js
class Example extends Phaser.Scene
{
    init ()
    {
        Phaser.GameObjects.GameObjectFactory.register('bomb', function (x, y)
        {
            return this.displayList.add(new Bomb(this.scene, x, y));
        });
    }
}
```

`init`方法在场景中被首先使用。这意味着我们可以在这里安全地注册自定义的游戏对象,并且它将可用于场景`create`方法:

```js
create ()
{
    this.add.bomb(200, 200);
    this.add.bomb(400, 300);
    this.add.bomb(600, 400);
}
```

您可以在此看到完整的示例 : [文件: gameobjects/ factory.js]

当您编码您的注册函数时, 您可以访问以下属性 :

| 属性 | 说明 |
| --- | --- |
| `this.scene` | 参考了拥有游戏对象工厂的场景. |
| `this.systems` | 参考景区系统. |
| `this.events` | 参考景点事件 Emitter. |
| `this.displayList` | 用于引用场景显示列表的参考 。 |
| `this.updateList` | 参考景区更新列表. |

上面的例子中,我们在 Scene `init` 方法中注册了 Game Object。 然而,为了保持事物的整洁和齐头并进,在 Game Objects 文件本身中注册也是非常常见的 。

以下是炸弹游戏对象的变体,它本身在工厂注册:

```js
export class Bomb extends Phaser.GameObjects.Sprite
{
    constructor (scene, x, y)
    {
        super(scene, x, y, 'bomb');

        this.setScale(0.5);
    }

    preUpdate (time, delta)
    {
        super.preUpdate(time, delta);

        this.rotation += 0.01;
    }
}

Phaser.GameObjects.GameObjectFactory.register('bomb', function (x, y)
{
    return this.displayList.add(new Bomb(this.scene, x, y));
});
```

然后我们就可以把它导入我们的场景:

```js
import { Bomb } from './Bomb.js';
```

并呼唤`this.add.bomb`方法如前.

## 游戏对象创建者 {#game-object-creator}

游戏对象创建者的作用是基于配置对象创建游戏对象。您也可以选择是否自动将其添加到场景中。这使得创建者功能对于提前创建游戏对象非常有用,这样您就可以避免在游戏中时间关键部分,如运行时,进行对象即时化.

游戏对象创建者和游戏对象工厂的主要不同之处在于所有创建者都使用配置对象。当工厂函数使用固定参数时,您使用的参数由您决定。 创建者在解析配置对象时更加灵活,并具有一些强大的特性, 但工厂函数较易从TypeScript语言中理解、记住和解析。

创建者本身是一个非常小的类,仅提供几个属性和钩子,其力量来自所有游戏对象都用它自己注册,用新方法动态扩展类,甚至可以创建包含创建者功能的自己的游戏对象,允许您扩展创建者以适应自己的需要.

每个场景都有一个实例的 `GameObjectCreator` 类。 默认情况下, 这是映射到 Scene 的 `make` 属性。 例如, 这里就是如何通过游戏对象创建器创建 :

```js
const sprite = this.make.sprite({
    x: 400,
    y: 300,
    key: 'playerAtlas',
    frame: 'idle'
});
```

以上例子可以作出一些假设,如纹理键和帧名称,但您应该把它当作一个简单的配置对象的例子,而不是可以复制和粘贴的东西.

内部, 游戏对象创建器本身没有实际的 `sprite` 方法。 如果您要在编辑器中打开类文件, 您不会找到。 这是因为每个游戏对象都负责自己的创建器功能。 Sprite 创建器代码可以在 Phaser 仓库内的 `src/gameobjects/sprite/SpriteCreator.js` 文件里找到。 几乎所有游戏对象都有类似的 `Creator.js` 文件, 负责自己在创建器中注册 。

所有创建器函数都叫静态的 `GameObjectCreator.register`函数,并传回它自己的创建器函数`sprite`的名称和回调。 `register`函数将带回这个调用并添加到创建器,在 `sprite` 属性下.

而这个调用在游戏代码中每次调用 `this.make.sprite` 时都会被引用。在这种情况下,它负责从配置对象创建Sprite 实例并将其添加到显示列表中,但任何实际逻辑都可以在这里发生.

调用回调被以游戏对象创建者作为上下文引用,这意味着调用回调中的`this`是参考创建者本身.

必须明白,虽然每个场景都有自己的游戏对象创建者实例,但游戏对象在创建者注册是全球性的,这意味着一旦一个游戏对象注册,其创建者功能可以从游戏中任意场景中获取.

最终, 创建者只涉及方便。 它允许您创建游戏对象, 无需担心其内部细节是如何创建的 。 它还允许您用自己的游戏对象来扩展创建者, 甚至覆盖现有的对象, 允许您定制创建者来适应您的需要 。

### 如何设置配置属性 {#how-to-set-configuration-properties}

正如我们在上面看到的,您将配置对象传递到创建者函数中,以便制作游戏对象。这些配置对象由创建者解析,并使用这些值设定正在创建的游戏对象的属性,如其位置,尺度,或旋转等.

然而,这些属性的解析方式是造物主的真正力量的出现。大多数属性是通过一个 Phaser 函数调用 `GetAdvancedValue`,允许属性以5种不同的方式表达。

为了简洁起见,我们将专注于创建Sprite并设置它的x/y坐标。然而,你实际上可以将这种方法用于几乎所有的游戏对象属性(见下表).

#### 1. 明确价值 {#1-explicit-value}

第一个也是最明显的方法是简单地提供固定价值:

```js
const sprite = this.make.sprite({
    x: 400
});
```

斯普拉蒂特将拥有400的X位置.

#### 2. 随机矩阵值 {#2-random-array-value}

您可以在一系列数值中传递,在这种情况下,将选择和使用数组中的随机元素:

```js
const sprite = this.make.sprite({
    x: [ 400, 500, 600 ]
});
```

Sprite x 位置将从给定的数组中随机选择。 因此, 它的x坐标可以是 400 、 500 或 600 。 您可以随意通过 。 而创建者将每次从数组中随机选择一个值 。

#### 3. 敏和马克之间随机整数 {#3-random-integer-between-min-and-max}

您可以在一个带有 `randInt` 属性的对象中通过。 这将是一个 2 元素阵列, 其中第一个元素是最小值, 第二个元素是最大值。 将选择并使用两个元素之间的随机整数 :

```js
const sprite = this.make.sprite({
    x: { randInt: [ 100, 600 ]}
});
```

Sprite x 位置将是100到600之间的随机整数.

#### 4. 民与最大之间随机浮点数 {#4-random-float-between-min-and-max}

您可以在一个带有 `randFloat` 属性的对象中通过。 这将是一个 2 元素阵列, 其中第一个元素是最小值, 第二个元素是最大值。 将选择并使用两个元素之间的随机浮点数 :

```js
const sprite = this.make.sprite({
    x: { randFloat: [ 100, 600 ]}
});
```

Sprite x 位置将在 100 到 600 之间随机浮点 。

#### 5. 回调值 {#5-callback-value}

最后,您可以在调用函数中通过。这应当返回一个值,该值将作为属性值:

```js
const sprite = this.make.sprite({
    x: function (key)
    {
        return Math.random() * 800;
    }
});
```

Sprite x 位置将在 0 到 800 之间随机浮点。 回调会发送一个参数, 即设置属性的键。 上面的例子中, `key` 将是 `x` 。

### 游戏对象配置属性 {#game-object-configuration-properties}

下表列出您可以在任意游戏对象上设置的所有属性。大多数游戏对象在此列表之外还有额外的属性,然而,以下是所有游戏对象的共同属性.

所有属性价值都可以通过上述5种方法中的任何一种方法表示。

| 属性 | 数据类型 |
| --- | --- |
| `x` | `number` |
| `y` | `number` |
| `depth` | `number` |
| `scaleX` | `number` |
| `scaleY` | `number` |
| `rotation` | `number` |
| `angle` | `number` |
| `flipX` | `boolean` |
| `flipY` | `boolean` |
| `visible` | `boolean` |
| `alpha` | `number` |
| `blendMode` | `number` |
| `scrollFactorX` | `number` |
| `scrollFactorY` | `number` |
| `originX` | `number` |
| `originY` | `number` |

另有3种特殊属性作为上述的组合:

| 属性 | 数据类型 |
| --- | --- |
| `scale` | `number` |
| `origin` | `number` |
| `scrollFactor` | `number` |

所以,与其说具体 `scaleX` 财务报告和已审计财务报表 `scaleY` 单独指定 `scale` 并设定两个值。 `origin` 财务报告和已审计财务报表 `scrollFactor`.

在 Phaser 内部,设置所有常见属性都由 `BuildGameObject` 函数处理, 您可以在 `src/gameobjects/BuildGameObject.js` 文件中找到。 如果您正在开发自己的创建器函数, 那么您可以使用此函数来处理您的常见属性 。

### 动画配置 {#animation-configuration}

如果您正在创建一个支持动画的游戏对象, 如Sprite, 您也可以指定配置对象中的动画细节。 例如, 要创建 Sprite 并在它上播放动画 :

```js
const sprite = this.make.sprite({
    x: 400,
    y: 300,
    key: 'playerAtlas',
    anims: 'idle'
});
```

`anims`属性是一款由Sprite创建器函数解析的特殊属性,它告诉创建器您想要在Sprite上播放动画。`anims`属性的值可以是字符串,也可以是对象。

上面的例子,我们告诉它播放"idle"动画,因为这是我们定义的动画关键.

创建者功能不会创建_ 动画, 它只是播放它们。 因此, 您必须假设此动画在您的游戏中已经定义了, 在此之前, 如果没有定义, 创建者游戏不会找到动画, 并且会跳过设定 。

与其通过字符串,你也可以通过一个对象,这样可以让您更详细地指定动画:

```js
const sprite = this.make.sprite({
    x: 400,
    y: 300,
    key: 'playerAtlas',
    anims: {
        key: 'idle',
        yoyo: true,
        repeat: -1
    }
});
```

在Phaser内部,这是由`BuildGameObjectAnimation`函数处理的,可以在`src/gameobjects/BuildGameObjectAnimation.js`文件中找到.

### 跳过显示列表 {#skipping-the-display-list}

当您调用 `make` 函数时, 您可以在配置对象之后通过第二个参数, 即 `addToScene`。 如果游戏对象自动添加到场景显示列表中, 则此值将控制它 。

默认情况下, 这是 `true`, 不过您可以两种方式之一 来覆盖。 首先, 简单地通过 `false` 作为第二个参数 :

```js

const config = {
    x: 400,
    y: 300,
    key: 'playerAtlas',
    frame: 'idle'
};

const sprite = this.make.sprite(config, false);
```

或者,通过设置配置对象本身中的`add`属性到`false`:

```js
const sprite = this.make.sprite({
    x: 400,
    y: 300,
    key: 'playerAtlas',
    frame: 'idle',
    add: false
});
```

在这两种情况下, Sprite 都会被创建, 但不会添加到 Scene 显示列表中。 这样您就可以提前生成一批 Sprite , 但会处于休眠状态, 直到您需要它们 。

另外,有些游戏对象也无需添加到显示列表中。例如,如果您创建了图形游戏对象作为遮罩,那么您就不需要实际显示它,所以可以不添加到显示列表中而创建它.

### 删除创建者函数 {#removing-a-creator-function}

如果游戏对象创建者已经有一个用指定名称注册的函数, 它会简单地跳过其它任何重命名的功能。 因此, 如果您想要用自己的功能替换一个内部的 Phaser 游戏对象, 您需要先删除已有的条目, 然后再添加您的条目 。

你可以使用`remove`方法来做到这一点:

```js
Phaser.GameObjects.GameObjectCreator.remove('sprite');
```

这将从创建者中删除 `sprite` 方法, 允许您添加自己的名字。 此进程是立即的 。

---
