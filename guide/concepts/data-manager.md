# 数据管理器 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/data-manager)

数据管理器是一个允许您存储、查询和获取密钥/值对等信息的组件。此信息被隔离到数据管理器的母端 。

Phaser 3 默认情况下, 游戏中有一个数据管理器的例子, 叫做“ 注册”。 除此之外, 每个游戏都有数据管理器的例子。 最后, 所有游戏对象也可以有一个数据管理器的例子。 此外, 如果您需要, 您可以创建自己的实例并管理这些实例 。

## 数据管理器父母 {#data-manager-parents}

数据管理器需要绑定到父程序。 数据管理器可以属于四种类型: 游戏、 场景、 游戏对象或自定义对象 。

### 游戏对象数据管理器 {#game-object-data-manager}

所有游戏对象都有名为“ 游戏对象” 的属性 `data`这是 `null` 默认,但被设定为持有实例 `DataManager` 如果使用该方法,则分类 `setDataEnabled` 调用游戏对象 :

```js
const sprite = this.add.sprite();

sprite.setDataEnabled();
```

或者,如果使用下列与数据有关的方法:`setData`、`incData`、`toggleData`或`getData`,它们也会触发创建属于游戏对象的数据管理器。本节将更详细地介绍这些方法。

一旦数据管理器存在,它就可以充当任何数据存储库,您想要绑定到该特定游戏对象上.

### 场景数据管理器插件 {#scene-data-manager-plugin}

每个场景都有它自己的数据管理器插件实例。 可以通过场景内部的 `data` 属性访问, 例如:

```js
class MyScene extends Phaser.Scene
{
    constructor ()
    {
        super('myScene');
    }

    create ()
    {
        this.data.set('lives', 3);
    }
}
```

数据管理器插件与数据管理器完全相同,包括所有相同的特性和方法,但构造时可以作为场景插件发挥作用.

### 游戏数据管理器 {#game-data-manager}

Game 实例中还有一个数据管理器,通过 S`registry` 属性从场景内访问:

```js
class MyScene extends Phaser.Scene
{
    constructor ()
    {
        super('myScene');
    }

    create ()
    {
        this.registry.set('lives', 3);
    }
}
```

与Scene的数据管理器不同,此数据管理器由Game Enter本身拥有,它由启动过程中自动创建,然后通过`registry`的属性在所有Scenes中都可以使用.

这意味着一个场景中输入注册簿的任何数据集在游戏中所有其他场景中立即可以获取。这也意味着您可以将其作为存储全球数据的地方,如高分,级别数据,设置等.

### 自定义数据管理器实例 {#custom-data-manager-instances}

您可以创建自己的数据管理器实例。 数据管理器必须总是有父和事件 Emitter , 它可以使用。 虽然父为游戏对象或场景, 它可以是您想要绑定的任何自定义对象 。

以下是一个类可以作为自己的数据管理器运行的例子:

```js
class CustomDataManager extends Phaser.Data.DataManager
{
    constructor ()
    {
        super(this, new Phaser.Events.EventEmitter());
    }
}

const myData = new CustomDataManager();
```

第一个参数是数据管理器的母体,在这种情况下是类本身。第二个参数是它将使用的 Emitter 事件实例。您可以使用您喜欢的任何 Emitter 活动实例,但它必须有一个实例 。

## 数据管理方法 {#data-manager-methods}

一旦一个数据管理器被创建或引用,你就可以准备在其中存储数据.

### 设置数据 {#set-data}

首先,你需要设定一些数据。你可以使用 `set` 方法做到这一点:

```js
//  In the Registry
this.registry.set('playerName', 'Vasquez');

//  From within a Scene
this.data.set('playerName', 'Vasquez');

//  On a Game Object instance
sprite.setData('playerName', 'Vasquez');
//  or:
sprite.data.set('playerName', 'Vasquez');
```

电话 `set` 方法需要两个参数:一个键和一个值。_key_是一个独特的字符串,它充当这个值的标识符,即。 `playerName`。与大多数东西一样 JavaScript,关键是区分大小写,所以 `playerName` 与 `PlayerName`。它也必须是一个有效的字符串。在设置和获取数据时记住这一点。

第二个参数是_value_,这可以是您喜欢的任意一种:字符串,整数,数组,对象,甚至指另一个类或函数.

如果数据成功设定, 将会释放 `SET_DATA` 事件 。

或者, 如果密钥已经存在于数据管理器中, 那么其先前的值将被新值覆盖, 而将释放 `CHANGE_DATA` 事件。 请参看事件 一节 。

#### 设置多值 {#setting-multiple-values}

您可以在一个调用中设置多个值, 将对象传递到 `set` 方法 :

```js
//  In the Registry
this.registry.set({ playerName: 'Hicks', weapon: 'M41A Pulse Rifle', score: 0 });

//  From within a Scene
this.data.set({ playerName: 'Hicks', weapon: 'M41A Pulse Rifle', score: 0 });

//  On a Game Object instance
sprite.setData({ playerName: 'Hicks', weapon: 'M41A Pulse Rifle', score: 0 });
//  or:
sprite.data.set({ playerName: 'Hicks', weapon: 'M41A Pulse Rifle', score: 0 });
```

在此情况下, 3 个新值将设定为数据管理器, 并带有密钥 `playerName`, `weapon` 财务报告和已审计财务报表 `score`A. 财务和预算 `SET_DATA` 事件会为每个事件释放。例如,如果其中两个值是新值,一个值是更新了先前的值,那么您将得到两个值。 `SET_DATA` 活动及1 `CHANGE_DATA` 活动。

传递到 `set` 方法的天体只重复一个深的一级。如果通过一个嵌入对象,例如:

```js
this.data.set({ playerName: 'Hicks', weapon: { name: 'M41A Pulse Rifle', ammo: 10 }, score: 0 });
```

然后,`weapon`对象将被设定为`weapon`条目本身的值,而不是其中的单个属性.

#### 将一个已有对象合并到数据管理器中 {#merge-an-existing-object-into-the-data-manager}

您可以使用 `merge` 方法从已有对象中填充密钥/值对的数据管理器 :

```js
const weapon = { name: 'M41A Pulse Rifle', ammo: 10 };

//  In the Registry
this.registry.merge(weapon, true);

//  From within a Scene
this.data.merge(weapon, true);

//  On a Game Object instance
sprite.data.merge(weapon, true);
```

第一个参数是合并到数据管理器的对象。 第二个参数是布尔 `overwrite`。 如果 `true`, 它将用对象的值覆盖数据管理器中的任何现有值。 如果 `false`, 它将跳过数据管理器中已经存在的任何密钥 。

如果数据管理器中不存在密钥, 则会创建并释放 `SET_DATA`事件。 如果密钥存在, `overwrite`为 `true`, 将会更新, 并释放 `CHANGE_DATA`事件 。

所有规则都与`set`方法一样适用,因为对象只重复一层深,密钥对大小写敏感等等.

#### 以对象为值 {#using-objects-as-values}

您可以将对象作为值, 但这样做时应当小心。 例如:

```js
const weapon = { name: 'M41A Pulse Rifle', ammo: 10 };

this.data.set({ playerName: 'Hicks', weapon });
```

在上述中, `weapon`值是一个对对象本身的_参考_。 数据管理器不会复制它。 这意味着如果您以后直接更新 `weapon` 对象, 存储在数据管理器中的值也会更新 。 例如:

```js
weapon.ammo = 20;
```

然而,这样做不会释放任何事件,而你将失去使用数据管理器的优势。

### 获取数据 {#get-data}

一旦你存储了一些数据,你可以再次用`get`方法检索到:

```js
//  In the Registry
this.registry.get('playerName');

//  From within a Scene
this.data.get('playerName');

//  On a Game Object instance
sprite.getData('playerName');
//  or:
sprite.data.get('playerName');
```

如果密钥存在于数据管理器中, 则该值将被返回。 如果密钥不存在, 则 `undefined` 将被返回 。

要同时获得数个值, 需要通过一系列密钥 :

```js
//  In the Registry
this.registry.get([ 'playerName', 'score' ]);

//  From within a Scene
this.data.get([ 'playerName', 'score' ]);

//  On a Game Object instance
sprite.getData([ 'playerName', 'score' ]);
//  or:
sprite.data.get([ 'playerName', 'score' ]);
```

如果您通过数组, 那么会返回一系列的值, 顺序与给定的键相同。 如果一个键不存在, 则返回 `undefined` 的位置 。

这对调整结构特别有用:

```js
const { playerName, score } = this.data.get([ 'playerName', 'score' ]);
```

### 数据值 {#data-values}

当你得到数据时,你得到的大多是数据的一个_副本_。例如,如果数据是字符串、数字或布尔,那么拨打`get`会返回该值。如果您再操纵该值,数据管理器就不会知道这个变化。例如:

```js
const score = this.data.get('score');

score += 10;
```

在这种情况下, `score` 值是存储在数据管理器中的值的复制件。 尽管您修改了, 添加了 10 个, 但数据管理器不会意识到这个变化。 如果您再给 `get` 打电话, 返回的值将是原始值, 而不是更新的值 。

为避免这种情况,使用数据管理器的`values`财产:

```js
const score = this.data.values.score;

score += 10;
```

数据管理器中的任何值都可通过`values`属性获取。

在此, `score` 是存储在数据管理器中的特殊值的引用。 这次, 如果您添加了 10 , 数据管理器会意识到这个变化, 并且也会发出 `CHANGE_DATA` 事件。 如果您再次呼叫 `get`, 返回的值将是更新的 。

也可以直接修改值,例如:

```js
this.data.values.score += 10;
```

这也是修改数据管理器中的值的“ 安全” 方法, 因为这样会释放 `CHANGE_DATA` 事件, 并且更新值 。

### 增量数据 {#increment-data}

`inc`方法会按照给定的金额递增一个值。如果数据管理器中不存在该值,则会创建该值,并给出该值的值:

```js
//  In the Registry
this.registry.inc('score', 10);

//  From within a Scene
this.data.inc('score', 10);

//  On a Game Object instance
sprite.incData('score', 10);
//  or:
sprite.data.inc('score', 10);
```

在这种情况下,如果`score`值已经不存在,它会被创建,并且给出10的值,如果存在,它会被递增10. 和其他设置数据的形式一样,相关事件也会被释放,取决于该值是否创建或更新.

要减少一个数值, 只需传递一个负数 :

```js
this.data.inc('score', -10);
```

注意 `inc` 特性只在值为标准时才有效 JavaScript 数字数据类型。如果尝试加长字符串,它会将数值附加到字符串的末尾。 `"10"` 将变成 `"1010"`。如果尝试并加长布尔,它将被转换为第一个数字,即。 `true` 变成 `1` 财务报告和已审计财务报表 `false` 变成 `0`中,将数字值错误地添加到对象中,将实际破坏原对象,代之以字符串 `[object Object]` 并附上你的电话号码。所以请务必只打电话。 `inc` 数字数据类型。

基本上, 打电话和电话没有区别 `inc` 方法,并仅通过 `values` 财产,但 `inc` 方法调用是可链的。

### 切换数据 {#toggle-data}

电话 `toggle` 方法将切换布尔值 `true` 财务报告和已审计财务报表 `false`:

```js
//  In the Registry
this.registry.toggle('musicEnabled');

//  From within a Scene
this.data.toggle('musicEnabled');

//  On a Game Object instance
sprite.toggleData('musicEnabled');
//  or:
sprite.data.toggle('musicEnabled');
```

如果数据管理器中不存在该值, 则会创建该值, 并给出`true`的值。 如果存在, 则该值会被切换到相反的布尔值。 与其它设置数据的形式一样, 相关事件也会被释放, 取决于该值是否创建或更新 。

### 冻结数据 {#freezing-data}

数据管理器具有被“ 冻结” 的能力。 如果您启用此功能, 则无法从数据管理器中添加或删除更多数据, 并且无法修改存储在其中的值。 如果您想要锁定数据管理器并让它只读, 这样做将很有用 。

要冻结或解冻数据管理器,请使用可链式`setFreeze`方法:

```js
//  In the Registry
this.registry.setFreeze(true);

//  From within a Scene
this.data.setFreeze(true);

//  On a Game Object instance
sprite.data.setFreeze(true);
```

或者,你可以直接修改 `freeze` 属性:

```js
//  In the Registry
this.registry.freeze = true;

//  From within a Scene
this.data.freeze = true;

//  On a Game Object instance
sprite.data.freeze = true;
```

立即改变数据管理器的冻结状态。 例如, 如果您正在添加包含数个新值的对象, 您在 `SET_DATA` 事件听器中调用 `setFreeze(true)`, 那么剩下的值将永远不会添加 。

### 删除数据 {#removing-data}

您可以使用 `remove` 方法从数据管理器中删除单个数据项 :

```js
//  In the Registry
this.registry.remove('playerName');

//  From within a Scene
this.data.remove('playerName');

//  On a Game Object instance
sprite.data.remove('playerName');
```

如果密钥存在于数据管理器中, 将会被移除, 并释放一个 `REMOVE_DATA` 事件。 如果密钥不存在, 则不会发生任何事件 。

您可以通过将一系列字符串传递到 `remove` 方法, 立即删除多个值 :

```js
//  In the Registry
this.registry.remove([ 'playerName', 'score' ]);

//  From within a Scene
this.data.remove([ 'playerName', 'score' ]);

//  On a Game Object instance
sprite.data.remove([ 'playerName', 'score' ]);
```

数据管理器还提供了`pop`方法。 这种方法与`remove`相同, 但返回被删除的值 :

```js
//  In the Registry
const playerName = this.registry.pop('playerName');

//  From within a Scene
const playerName = this.data.pop('playerName');

//  On a Game Object instance
const playerName = sprite.data.pop('playerName');
```

如果数据管理器中不存在密钥,则返回 `undefined` 。

每个成功移除的密钥,无论用何种方法去除,都会发出`REMOVE_DATA`事件.

和设置数据一样,如果数据管理器已被冻结,则不会删除任何值.

### 重置数据管理器 {#reset-the-data-manager}

您可以通过调用 `reset` 方法来重置数据管理器,删除它包含的所有数据 :

```js
//  In the Registry
this.registry.reset();

//  From within a Scene
this.data.reset();

//  On a Game Object instance
sprite.data.reset();
```

这将从数据管理器中移除所有数据, 并将其冻结状态重置为虚假。 任何事件都不会被这种方法释放。 如果您愿意, 这只是完全清除数据管理器的快速方法 。

### 查询数据管理器 {#querying-the-data-manager}

查询数据管理器有几种方法。

#### 已经 {#has}

第一个,也是最简单的,是`has`方法。此检查可以检查数据管理器是否有匹配给定字符串的密钥 :

```js
//  In the Registry
this.registry.has('playerName');

//  From within a Scene
this.data.has('playerName');

//  On a Game Object instance
sprite.data.has('playerName');
```

如果数据管理器中存在密钥, 它会返回 `true`, 否则它会返回 `false`。 和 JavaScript 中所有密钥的使用一样, 请记住, 这是高度区分大小写 。

#### 数 {#count}

要返回数据管理器中当前存储的条目总数, 请使用 `count` 属性 :

```js
//  In the Registry
this.registry.count;

//  From within a Scene
this.data.count;

//  On a Game Object instance
sprite.data.count;
```

这是一个数值,代表数据管理器中的条目总数。

#### getAll {#getall}

要返回数据管理器内的所有内容,请使用 `getAll` 方法:

```js
//  In the Registry
this.registry.getAll();

//  From within a Scene
this.data.getAll();

//  On a Game Object instance
sprite.data.getAll();
```

这将返回包含数据管理器中存储的所有数据的新对象。 例如 :

```js
{
    playerName: 'Hicks',
    weapon: 'M41A Pulse Rifle',
    score: 0
}
```

如果数据管理器为空,则返回一个空对象。

使用 `getAll` 时, 您应该将返回的对象视为只读。 如果您直接修改, 数据管理器将不会意识到这些修改 。

#### 每一个 {#each}

`each`方法允许您将数据管理器中的所有条目传递给给给定的回调。 您将回调作为第一个参数, 将可选上下文作为第二个参数, 然后将任何进一步参数 :

```js
//  In the Registry
this.registry.each((parent, key, value) => {
    console.log(key, value);
});

//  From within a Scene
this.data.each((parent, key, value) => {
    console.log(key, value);
});

//  On a Game Object instance
sprite.data.each((parent, key, value) => {
    console.log(key, value);
});
```

调用将发送三个参数:数据管理器的母参数、密钥和值。如果您指定了额外的参数,它们将在这三个参数之后发送。

数据管理器不使用,或期望调回的值返回,所以如果您想要修改发送给您的调回的值,就必须通过正常的数据管理器方法进行修改.

#### 查询 {#query}

`query`方法允许您搜索数据管理器的密钥, 以匹配给定的正则表达式。 然后返回包含任何匹配密钥/ 值对的对象 。

例如,假设我们用一些不同的武器 给数据管理员寄了信息:

```js
this.data.set({
    'M41A Pulse Rifle': 10,
    'M56 Smartgun': 20,
    'M240 Flamethrower': 30,
    'M42A Scope Rifle': 40,
    'M83 SADAR': 50,
    'M92 Grenade Launcher': 60
});
```

然后,我们可以使用`query`方法,将所有含有"Rifle"一词的武器退回:

```js
const rifles = this.data.query(/Rifle/);
```

返回对象将包含所有匹配的密钥/ 值对 :

```js
{
    'M41A Pulse Rifle': 10,
    'M42A Scope Rifle': 40
}
```

如果没有找到匹配,则返回空对象。

`query`方法接受任何有效的正则表达式.

#### 电话 `list` 财务报告和已审计财务报表 `values` 属性 {#the-list-and-values-properties}

`list`属性是一个包含数据管理器中所有密钥的数组:

```js
//  In the Registry
this.registry.list;

//  From within a Scene
this.data.list;

//  On a Game Object instance
sprite.data.list;
```

`values`属性是一个包含数据管理器中所有值的数组:

```js
//  In the Registry
this.registry.values;

//  From within a Scene
this.data.values;

//  On a Game Object instance
sprite.data.values;
```

这些对象应该被当作只读,而绝不直接修改。然而,它们被公开,以便您能够使用任何普通的JavaScript方法,如解构、`map`、`forEach`等。

## 数据管理器事件 {#data-manager-events}

当创建数据管理器时, 需要给它一个事件 Emitter 。 这意味着有几种不同的方式来倾听数据管理器的事件, 取决于您设置数据的位置。 以下是您可以听到数据管理器事件的不同方式 。

游戏数据管理器(注册)将发布事件:

```js
//  From within a Scene:
this.registry.events.on('setdata', (parent, key, value) => {
    console.log('Registry set:', key, value);
});
```

场景数据管理器将通过场景系统发布事件,从场景内映射到`events`属性:

```js
//  From within a Scene:
this.events.on('setdata', (parent, key, value) => {
    console.log('Scene data set:', key, value);
});
```

游戏对象数据管理器会通过游戏对象本身发布事件:

```js
sprite.on('setdata', (parent, key, value) => {
    console.log('Sprite data set:', key, value);
});
```

最后,如果你创建了数据管理器的实例, 那么,你这样做时会提供事件Emitter。 这是您应该从中听到的发送器 。

## 正在销毁数据管理器 {#destroying-the-data-manager}

如果数据管理器属于一个游戏(即注册),一个场景,或者一个游戏对象,当母对象被销毁时,它会自动被销毁。但是,如果你创建了自己的数据管理器实例,那么,当不再需要的时候,你就负责销毁它。

要做到这一点,请拨打`destroy`方法:

```js
myData.destroy();
```

这将发出一个 `DESTROY` 事件,删除所有听众,并清除它持有的与其他对象的引用 。

请注意, 如果一个场景是关闭而不是销毁, 那么数据管理器将会坚持并保留其中的所有数据。 如果您想要在场景关闭时从数据管理器中清除数据, 那么您应该为关闭事件收听, 并给其数据管理器打电话 `reset` :

```js
class MyScene extends Phaser.Scene
{
    constructor ()
    {
        super('myScene');
    }

    create ()
    {
        this.data.set('lives', 3);

        this.events.once('shutdown', this.shutdown, this);
    }

    shutdown ()
    {
        this.data.reset();
    }
}
```

### 使用 JSON 软件 {#using-json}

您可以通过 :

```js
const json = JSON.stringify(data.list);
```

`data`是数据管理器的参考,它可能属于游戏或游戏对象.

也可以做相反的动作:

```js
data.reset().merge(JSON.parse(json));
```

在那里`json`是你的 完善的JSON数据。

---
