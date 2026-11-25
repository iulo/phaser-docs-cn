# 游戏对象 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects)

Phaser中的所有游戏对象都从一个叫做`Phaser.GameObjects.GameObject`的基类扩展出来。这个类本身不能做很多事情,例如不能渲染,也不能添加到显示列表中。它所做的就是提供Game Objects所需的所有组件和核心功能。

在本节中,我们将涵盖游戏对象类的基础属性和方法。这意味着,您在本节中读到的任何东西也可以在Phaser内的其他游戏对象中找到。

## 场景 {#scene}

一个游戏对象只能属于一个场景。 属于它的场景的参考文献可以在 `scene` 属性中找到 :

```js
const scene = sprite.scene;
```

虽然它不是,但出于内部原因, 您应该将此属性视为只读。 您不能更改游戏对象创建后属于的场景。 `scene` 属性在游戏对象的构建器中传递, 并立即设定 。

当游戏对象被销毁时, 引用的游戏对象将被取消。 如果您在代码中发现了任何与“ 未定义的” 游戏对象有关的错误, 请确定您不会处理被破坏的游戏对象 。

游戏对象有两个回调,当它们被添加到或删除到一个场景中时,它们会被引用:

```js
class MySprite extends Phaser.GameObjects.Sprite
{
    constructor (scene, x, y, texture, frame)
    {
        super(scene, x, y, texture, frame);
    }

    addedToScene ()
    {
        super.addedToScene();

        //  This Game Object has been added to a Scene
    }

    removedFromScene ()
    {
        super.removedFromScene();

        //  This Game Object has been removed from a Scene
    }
}
```

您可以在自定义的游戏对象中自由使用这些调用, 以便设置任何特定的数据, 或者执行游戏对象添加到或删除到场景中时需要完成的任何任务。 请注意, 一些游戏对象, 如Sprites, 使用这些调用, 所以请确保您在覆盖时总是使用 `super`, 如上例中所示 。

而不是使用回调, 你可以听 `ADDED_TO_SCENE` 和 `REMOVED_FROM_SCENE` 事件代替:

```js
sprite.on(Phaser.GameObjects.Events.ADDED_TO_SCENE, handler);
sprite.on(Phaser.GameObjects.Events.REMOVED_FROM_SCENE, handler);
```

两次事件处理器都被发送到一个参考文献,将Game Object作为第一个参数,而Scene作为第二个参数.

## 创建游戏对象 {#creating-a-game-object}

通常,在场景的`create()`方法中创建和添加游戏对象.

`add`方法一时创建并添加:

```js
const sprite = this.add.sprite(0, 0, 'mummy');
```

`make`方法也一样,当给`add: true`:

```js
const sprite = this.make.sprite({ x: 0, y: 0, key: 'mummy', add: true });
// OR
const sprite = this.make.sprite({ x: 0, y: 0, key: 'mummy' }, true);
```

游戏对象可以即时化,然后手动添加: 

```js
const sprite = this.add.existing(new Phaser.GameObjects.Sprite(this, 0, 0, 'mummy'));
```

游戏对象可以在禁用状态或隐形状态下创建:

```js
const sprite = this.add.sprite(0, 0, 'mummy').setActive(false).setVisible(false);
```

`add: false`使用,`make`方法不会将新游戏对象添加到场景显示列表中:

```js
const sprite = this.make.sprite({ x: 0, y: 0, key: 'mummy', add: false });
// OR
const sprite = this.make.sprite({ x: 0, y: 0, key: 'mummy' }, false);
```

这些游戏对象根本没有显示.

直接被即时化的游戏对象不添加到场景显示列表或更新列表中:

```js
const sprite = new Phaser.GameObjects.Sprite(this, 0, 0, 'mummy');
```

更新列表还将更新任何使用`active: true`和`preUpdate()`方法的天体:

```js
this.sys.updateList.add({
  active: true,
  preUpdate: () => { console.count(); }
});
```

## 删除游戏对象 {#removing-a-game-object}

暂时删除游戏对象 :

```js
sprite.setActive(false).setVisible(false);
```

永久删除游戏对象 :

```js
sprite.destroy();
```

毁灭的游戏对象不能被重用。 您可以用 `gameObject.scene === undefined` 检测到一个被破坏的游戏对象。 (它也有 `active === false` 和 `visible === false` 。)

所有游戏对象在现场停止时都会被摧毁,所以你不需要自己这样做.

## 显示列表 {#display-list}

如果游戏对象位于显示列表上,而大多数显示列表上,则可以通过`displayList`属性获取:

```js
const list = sprite.displayList;
```

游戏对象可以或者放在属于其母景的显示列表上,或者放在属于景的层上。此属性也可以是`null`。如同`scene`属性一样,您应该将此属性视为只读,而永远不要直接更改它。

`displayList` 属性在调用 `addToDisplayList` 和 `removeFromDisplayList` 方法时设定。这在您通过 Game Object Factory 创建游戏对象时自动发生, 或者从图层中添加或删除 。

游戏对象只能在任何特定时间存在于一个显示列表或层上,但可以在它们之间自由移动。如果在调用此方法时,游戏对象已经在另一个显示列表上,则首先从中移除,然后添加到新的列表中。

如果游戏对象不在任何显示列表中, 则不会被渲染。 如果您只是希望暂时禁用它来渲染, 请考虑使用 `setVisible` 方法, 而不是添加和删除它 。

添加和移除游戏对象的行为将分别释放`ADDED_TO_SCENE`和`REMOVED_FROM_SCENE`事件.

直接调用这些方法并不常见,但是如果需要,它们就会暴露出来.

## 状态和名称 {#state-and-name}

`state` 属性是数字或字符串值,您可以用来存储游戏对象的当前状态。 使用此属性来跟踪游戏对象在存在期间的状况。 例如, 它可能从“ 移动” 状态变为“ 攻击” 状态, 变为“ 死亡 ” 状态。 状态值应该是整数( 在游戏代码中理想地映射到常数) , 或字符串。 推荐这些值以保持光线和简单, 并进行快速比较 。 如果您需要存储关于游戏对象的复杂数据, 请使用数据组件来查看 。

```js
sprite.state = 'ALIVE';
```

您也可以使用可链式`setState`方法:

```js
sprite.setState('ALIVE');
```

`name`属性是一个基于字符串的名称,您可以用来识别游戏对象。例如,您可以使用它来存储游戏对象的类型,例如`player`或`enemy`.

```js
sprite.name = 'player';
```

您也可以使用可链式`setName`方法:

```js
sprite.setName('player');
```

这些属性都不是Phaser直接使用的,它们纯粹是供您用来帮助构建游戏的。

## 更新列表与激活状态 {#update-list-and-active}

每个场景都有更新列表。 这是特殊类型的列表, 负责在列表中的所有游戏对象上调用 `preUpdate` 方法, 一次是每游戏步骤。 有些游戏对象需要这个, 其他则不需要。 例如, Sprite 需要更新其动画组件, 所以它会加入更新列表。 然而, 文本对象没有需要更新的组件, 所以它不会添加到更新列表中。 如果您创建自定义类, 您可以选择是否应该添加到更新列表中, 或者不添加。 您可以调用其 `addToUpdateList` 方法来完成此任务 :

```js
sprite.addToUpdateList();
```

只要游戏对象有`preUpdate`方法,且在场景更新列表中并不存在,它就会被添加。然后,您就可以使用`preUpdate`方法运行您游戏对象需要的任何自定义逻辑,即:

```js
class Bullet extends Phaser.GameObjects.Image
{
    constructor (scene, x, y)
    {
        super(scene, x, y, 'bullet');

        this.addToUpdateList();
    }

    preUpdate (time, delta)
    {
        this.x += 10;

        if (this.x > 800)
        {
            this.setActive(false);
            this.setVisible(false);
        }
    }
}
```

这里我们有一个自定义的游戏对象, 叫做 `Bullet`。 它从通常不使用更新列表的 `Phaser.GameObjects.Image` 延伸出来。 这就是为什么我们在构建器中使用 `addToUpdateList` 。 然后使用 `preUpdate` 方法在屏幕上移动, 如果它脱离边缘, 它会关闭它。 这意味着它将不再被更新列表更新, 并且在未来的游戏步骤中被跳过 。

当调用 `preUpdate` 时, 它会通过更新列表发送两个参数。 第一个是当前时间戳, 由浏览器生成 。 第二个是三角形值, 由时间戳衍生 。 这是当前框架和上一个框架的区别 。 它是以毫秒表示的值, 是不同框架之间时间的间隔 。 这是您应该用来更新游戏对象的, 而不是依赖 `setTimeout` 或其他方法, 因为它处理浏览器中的暂停和减速 。

与更新列表相关, `active`属性是一个布尔,它可以控制游戏对象是否被更新列表处理。一个游戏对象,即 `active`,在游戏步骤中会调用其 `preUpdate`方法,否则会跳过:

```js
sprite.active = false;
```

您也可以使用可链式`setActive`方法设定游戏对象的活跃状态:

```js
sprite.setActive(false);
```

如前所述,并非所有游戏对象都添加到更新列表中。例如,在基本图像游戏对象上显示此属性不会真正改变任何东西,因为图像不会通过更新列表更新。然而,如果您有更新列表中自定义的游戏对象,那么您会如何切换它,或者不切换,而不需要从列表中添加或删除它。

## 父容器 {#parent-containers}

游戏对象只能有一个父容器。 `parentContainer` 属性中可以引用它所属的容器:

```js
const container = sprite.parentContainer;
```

您应该将此属性视为只读。 当您将游戏对象添加到容器时, 它会自动设定, 当它被移除或销毁时, 它会失效 。

与此相关的是 `getIndexList` 方法。 这将返回游戏对象祖先的所有索引, 从位置到显示列表的根端, 通过任何父容器:

```js
const indexes = sprite.getIndexList();
```

内部,这是输入插件使用的。但是,如果需要了解显示列表中游戏对象的深度,您可以直接调用它。

## 可见度 {#visibility}

游戏对象可以被隐形或隐藏. 隐形游戏对象会跳过渲染,但仍会处理更新逻辑.

- 获取游戏对象的可见度 :

    ```javascript
    var visible = gameObject.visible; // returns true or false
    ```

- 设定游戏对象的可见度 :

    ```javascript
    gameObject.visible = visible;
    gameObject.setVisible(visible);
    ```

## 纹理 {#textures}

某些游戏对象持有纹理和纹理帧.

- 创建带有纹理和框架的游戏对象 :

    ```js
    const gameObject = this.add.sprite(0, 0, key, frame);
    ```

    - `key`:要使用的纹理的键,存储在纹理管理器中,或一个纹理实例.
    - `frame`:纹理内框的名称或索引.

- 获取纹理 :

    ```javascript
    var texture = gameObject.texture;
    var frame = gameObject.frame;
    ```

- 获取纹理键, 框名 :

    ```javascript
    var textureKey = gameObject.texture.key;
    var frameName = gameObject.frame.name;
    ```

- Example:

    ```js
    const sprite = this.add.sprite(0, 0, 'mummy', 1);
    ```

`texture`参数(`'mummy'`)是创建时装入到图示中的纹理键(名称).

游戏对象如果没有纹理是无法创建的,相反,它们会收到"默认"纹理和帧(32×32透明):

```js
const sprite = this.add.sprite(0, 0);
console.log(sprite.texture.key); // → '__DEFAULT'
console.log(sprite.displayWidth, sprite.displayHeight); // → 32, 32
```

更改纹理帧 :

- 设定框架

    ```javascript
    gameObject.setFrame(frame);
    // gameObject.setFrame(frame, updateSize, updateOrigin);
    ```

    - `frame`:纹理内框的名称或索引.
    - `updateSize`:这个电话应该调整游戏对象的大小吗?
    - `updateOrigin`:这个电话应该调整游戏对象的起源吗?

- 按帧对象设置帧

    ```javascript
    gameObject.setFrame(frameObject);
    // gameObject.setFrame(frameObject, updateSize, updateOrigin);
    ```

```js
// Spritesheet-style frame names
sprite.setFrame(2);
sprite.setFrame('2');

// Atlas-style frame names
sprite.setFrame('walkLeft');
```

改变纹理 :

- 通过键字符串设置纹理

    ```javascript
    gameObject.setTexture(key);
    // gameObject.setTexture(key, frame);
    // gameObject.setTexture(key, frame, updateSize, updateOrigin);
    ```

- Example:

    ```js
    const sprite = this.add.sprite(0, 0, 'mummy');

    sprite.setTexture('bat');
    console.log(sprite.texture.key); // → 'bat'
    ```

装入或播放动画也可以改变Sprite的纹理:

```js
const sprite = this.add.sprite(0, 0, 'mummy');

sprite.play('snakeAttack');
console.log(sprite.texture.key); // → 'snake'
```

## 位置、原点与尺寸 {#position-origin-and-size}

`x` 财务报告和已审计财务报表 `y` 是指游戏对象的本地位置(如果在容器内)或本地和世界位置(如果不在容器内)。 `z` 财务报告和已审计财务报表 `w` 被没有使用 Phaser让你自己用 `z` 不是,是"我们"的 `depth`.

- 获取游戏对象的位置 :

    ```javascript
    var x = gameObject.x;
    var y = gameObject.y;
    ```

- 设定游戏对象的位置 :

    ```javascript
    gameObject.x = 0;
    gameObject.y = 0;
    gameObject.setPosition(x,y);
    gameObject.setX(x);
    gameObject.setY(y);
    ```

- 设置随机位置 :

    ```javascript
    gameObject.setRandomPosition(x, y, width, height);
    // gameObject.setRandomPosition(); // x=0, y=0, width=game.width, height=game.height
        ```

`width`和`height`是游戏对象的内在大小或未标定大小。对于基于帧的对象(图像、Sprite),这些是当前纹理帧的大小,你不应该设置它们。对于其他对象(容器、TileSprite),你可以这样设定内在大小。

- 获取游戏对象的大小 :

    ```javascript
    var width = gameObject.width;
    var height = gameObject.height;
    ```

- 设定游戏对象大小 :

    ```javascript
    gameObject.setSize(width, height);
    ```
    or

    ```javascript
    gameObject.width = width;
    gameObject.height = height;
    ```

`originX`和`originY`是游戏对象的视觉起源,在正版坐标中为(0,0)是左上角,1,1是右下角. 旋转和缩放发生于原源;翻转发生在中心之间. 大部分游戏对象默认起源为(0.5,0.5),中心. Render Texture, Text,和Bitmap Text游戏对象默认起源为 (0,0),左上角. 容器游戏对象的特性为(0.5, 0.5),Blitter和Graphics游戏对象名义起源为(0,0,),因为其无维度.

- 获取游戏对象的起源 :

    ```javascript
    var originX = gameObject.originX;
    var originY = gameObject.originY;
    ```

- 设定游戏对象的起源 :

    ```javascript
    gameObject.setOrigin(x, y);
    // gameObject.setOrigin(x); // y = x if y is not set
    ```

- 将游戏对象的起源设置为左上角

    ```javascript
    gameObject.setOrigin(0);
    ```

- 将游戏对象的起源设定为顶端中心

    ```javascript
    gameObject.setOrigin(0.5, 0);
    ```

- 将游戏对象的起源设置为右上角

    ```javascript
    gameObject.setOrigin(1, 0);
    ```

- 将游戏对象的起源设定为左中点

    ```javascript
    gameObject.setOrigin(0, 0.5);
    ```

- 设定游戏对象的源头为中心

    ```javascript
    gameObject.setOrigin(0.5);
    ```

- 将游戏对象的起源设定为右中心

    ```javascript
    gameObject.setOrigin(1, 0.5);
    ```

- 将游戏对象的起源设置为左下角

    ```javascript
    gameObject.setOrigin(0, 1);
    ```

- 设定游戏对象的源头为下端中心

    ```javascript
    gameObject.setOrigin(0.5, 1);
    ```

- 将游戏对象的起源设置为右下角

    ```javascript
    gameObject.setOrigin(1);
    ```

`flipX`和`flipY`是游戏对象的渲染切换,以翻转横向或垂直轴上的渲染纹理,不影响游戏对象的尺度值或物理体.

- 获取游戏对象的翻转值 :
    ```javascript
    var flip = gameObject.flipX;  // flip: true/false
    var flip = gameObject.flipY;  // flip: true/false
    ```
- 设定游戏对象的翻转值 :
    ```javascript
    gameObject.flipX = flip;
    gameObject.flipY = flip;
    gameObject.setFlipX(flip);
    gameObject.setFlipY(flip);
    gameObject.setFlip(flipX, flipY);
    gameObject.toggleFlipX();
    gameObject.toggleFlipY();
    gameObject.resetFlip();  // equal to gameObject.setFlip(false, false);
    ```

`displayOriginX`和`displayOriginY`是游戏对象在未缩放像素坐标上的起源:

    (displayOriginX, displayOriginY) == (width, height) * (originX, originY)

它们与`displayWidth`和`displayHeight`无关,因为它们指的是内在的大小.

`displayWidth`和`displayHeight`是游戏对象的缩放尺寸,以像素坐标表示:

    (displayWidth, displayHeight) == (width, height) * (scaleX, scaleY)

- 获取游戏对象的显示大小 :

    ```javascript
    var displayWidth = gameObject.displayWidth;
    var displayHeight = gameObject.displayHeight;
    ```

- 设定游戏对象的显示大小 :

    ```javascript
    gameObject.setDisplaySize(displayWidth, displayHeight);
    ```

    or

    ```javascript
    gameObject.displayWidth = displayWidth;
    gameObject.displayHeight = displayHeight;
    ```

- 获取游戏对象的大小 :

    ```javascript
    var scaleX = gameObject.scaleX;
    var scaleY = gameObject.scaleY;
    ```

    or

    ```javascript
    var scale = gameObject.scale;  // Returns (scaleX + scaleY)/2
    ```        

- 设定游戏对象的大小 :

    ```javascript
    gameObject.setScale(scaleX, scaleY);
    ```

    or

    ```javascript
    gameObject.scaleX = scaleX;
    gameObject.scaleY = scaleY;
    ```

    or

    ```javascript
    gameObject.scale = scale;  // Set scaleX, scaleY to scale
    ```

您可以从这些游戏中获取或设定游戏对象的视觉大小。 不需要同时设置 `displayWidth` 和 `scaleX` 或 `displayHeight` 和 `scaleY` , 因为这两个属性都做了同样的事情 。

基于帧的游戏对象(Image,Sprite)在切换帧或纹理时可能会改变大小.

当一个纹理帧有自定义的枢轴集(通常在纹理图集中)时,在修改帧时,游戏对象源头会自动更新.

`angle`(度, -180–180)和`rotation`(弧度, -  –  –  )是相同的属性,在不同的单位中,一个游戏对象在初始位置上具有角度和旋转0.

- 获取游戏对象的角度 :

    ```javascript
    var angle = gameObject.angle;
    var radians = gameObject.rotation;  // angle in radians
    ```

- 设定游戏对象的角度 :

    ```javascript
    gameObject.angle = degrees;
    gameObject.rotation = radians;
    gameObject.setAngle(degrees);
    gameObject.setRotation(radians);
    ```

## 局部位置与边界 {#local-position-and-bounds}

对于不在容器内的游戏对象,本地坐标也是世界坐标.

当地中心为`gameObject.x`,原产地为`gameObject.y`(0.5,0.5),或任何原产地为`gameObject.getCenter()`.

本地的,未旋转的,未标定的界限由

```js
const rect = Phaser.Display.Bounds.GetBounds(gameObject);
// → Rectangle { x, y, width, height, left, top, right, bottom … }
```

这是一个矩形,尺寸与游戏对象的`width`和`height`完全相同,其位置是其起源.

您可以单独获得边缘坐标 :

```js
const left = Phaser.Display.Bounds.GetLeft(gameObject);
```

你可以让他们:

```js
Phaser.Display.Bounds.SetLeft(gameObject, 0);
```

您可以计算本地的, 未旋转的, 缩放的自定义 :

```js
const left = gameObject.x - gameObject.originX * gameObject.displayWidth;
const top = gameObject.y - gameObject.originY * gameObject.displayHeight;
```

四个角和四个边缘中点的局部,旋转,缩放坐标由`getTopLeft()`,`getLeftCenter()`等给出.  

`getLocalPoint()`方法将世界坐标转换为游戏对象的**own**坐标空间(包括变换),对于一个图像来说,这些也是纹理坐标。对于一个形状来说,这些坐标可能与几何坐标相似。对于一个容器来说,这些是儿童对象的局部坐标。 

```javascript
var point = gameObject.getLocalPoint(x, y);  // point : {x, y}
// var out = gameObject.getLocalPoint(x, y, out);
```
or
```javascript
var out = gameObject.getLocalPoint(x, y, out, camera);
```

## 世界坐标中的位置与边界 {#world-position-and-bounds}

这些是用于容器中的游戏对象。 (对于不是容器中的游戏对象,世界坐标也是本地坐标。 )

游戏对象在世界坐标中的位置是

```js
const { tx, ty } = gameObject.getWorldTransformMatrix();
```

世界坐标的界限是:

```js
const bounds = gameObject.getBounds();
// → Rectangle { x, y, width, height, left, top, right, bottom, centerX, centerY, … }
```

这是包含游戏对象旋转,缩放角的最小轴向对齐矩形.

世界坐标变化的角是:

```js
const { x, y } = gameObject.getTopLeft(undefined, true);
const { x, y } = gameObject.getTopCenter(undefined, true);
const { x, y } = gameObject.getTopRight(undefined, true);
const { x, y } = gameObject.getLeftCenter(undefined, true);
const { x, y } = gameObject.getRightCenter(undefined, true);
const { x, y } = gameObject.getBottomLeft(undefined, true);
const { x, y } = gameObject.getBottomCenter(undefined, true);
const { x, y } = gameObject.getBottomRight(undefined, true);
```

而世界坐标的中心是

```js
const { x, y } = gameObject.prepareBoundsOutput(gameObject.getCenter(), true);
```

或 (Phaser v3.60) (中文(简体) ).

```js
const { x, y } = gameObject.getCenter(undefined, true);
```

## 几何 {#geometry}

可将大多数游戏对象转换成Geom点,圆,或矩等进行一些计算,如交叉检查.

## 裁剪 {#crop}

裁剪剪游戏对象纹理帧的可见区域。

- 将裁剪应用到纹理

    ```javascript
    gameObject.setCrop(x, y, width, height);
    ```

- 重置作物( E)

    ```javascript
    gameObject.setCrop();
    // gameObject.isCropped = false;
    ```
        
- Example:

    ```js
    image.setCrop(0, 0, 64, 32);
    ```

值在纹理坐标中,其中(0,0)是纹理左上方.

裁剪不会改变游戏对象的实际界限或其输入命中区.

## 输入 {#input}

使用 `setInteractive()` 来让游戏对象接收输入事件。 任何游戏对象都可以被交互, 但只有部分对象有自动命中区域。 对于其他对象, 您需要提供命中区域并命中测试功能 。

- 基本用途:

```javascript
gameObject.setInteractive().on('pointerdown', function(pointer, localX, localY, event){
    // ...
});
```

对于纹理帧(`frame`)或非零`width`和`height`的游戏对象,没有参数的`setInteractive()`会创建一个大小相同的矩形命中区域: .

```js
const sprite = this.add.sprite(0, 0, 'mummy').setInteractive();

console.log(sprite.input.hitArea); // → Rectangle { x: 0, y: 0, width: 32, height: 48 }
```

`hitArea`位于本地坐标,其中(0,0)是游戏对象的左上角,无论来源为何.

您可以手动构造同一个命中区域。 您必须通过命中区域 ** 和 ** 命中测试功能 :

```js
sprite.setInteractive(
  new Phaser.Geom.Rectangle(0, 0, sprite.frame.realWidth, sprite.frame.realHeight),
  Phaser.Geom.Rectangle.Contains
);
```

您可以使用任意几何形状, 并带有相应的 `Contains` 函数 :

```js
sprite.setInteractive(
  new Phaser.Geom.Circle(sprite.displayOriginX, sprite.displayOriginY, sprite.width),
  Phaser.Geom.Circle.Contains
);
```

您可以使用自己的命中区和测试功能:

```js
sprite.setInteractive({
  hitArea: [
    new Phaser.Geom.Circle(0, 0, 32),
    new Phaser.Geom.Circle(64, 64, 32),
    new Phaser.Geom.Circle(128, 128, 32)
  ],

  hitAreaCallback: (hitArea, x, y, gameObject) => {
    return hitArea[0].contains(x, y) ||
        hitArea[1].contains(x, y) ||
        hitArea[2].contains(x, y);
  }
});
```

## 不透明度（Alpha） {#alpha}

带有`alpha === 0`的游戏对象是隐形的.

在WebGL模式中,纹理的四角可以有不同的α值.

- 获取游戏对象的α :

    ```javascript
    var alpha = gameObject.alpha;  // 0~1
    ```
    
- 设定游戏对象的α :

    ```javascript
    gameObject.setAlpha(alpha);
    // gameObject.alpha = alpha;
    ```

    或以 WebGL 模式:

    ```javascript
    gameObject.setAlpha(topLeft, topRight, bottomLeft, bottomRight);
    // gameObject.alphaTopLeft = alpha;
    // gameObject.alphaTopRight = alpha;
    // gameObject.alphaBottomLeft = alpha;
    // gameObject.alphaBottomRight = alpha;
    ```

- 清除( 设置为 `1`)

    ```javascript
    gameObject.clearAlpha();
    ```

## 着色（Tint） {#tint}

**叮当** 是对游戏对象的纹理的一种染色效果。它只是WebGL。

- 获取游戏对象的颜色 :

    ```javascript
    var color = gameObject.tintTopLeft; // color: 0xRRGGBB
    var color = gameObject.tintTopRight;
    var color = gameObject.tintBottomLeft;
    var color = gameObject.tintBottomRight;
    var isTinted = gameObject.isTinted; // is the game object tinted?
    ```

数学上,锡将每个纹理像素乘以锡色,所以一个锡色像素永远比一个无纹色像素亮,白锡(0xffffff)没有效果,黑锡(0x000000)使所有像素都变得黑色,在纹理上,白象素的锡完全和黑色像素完全没有,所以白像素对锡形或位图文字都好.

**丁补** 是一个不透明的填充, 就像一个油漆桶填充:

```js
sprite.setTintFill(0x01ff70);
```

`clearTint()`可以去除两种锡.

游戏对象纹理的四角可以分别用锡,形成梯度:

```js
sprite.setTint(0xff4136, 0xffdc00, 0x2ecc40, 0x0074d9);
// OR
sprite.tintTopLeft = 0xff4136; // etc.
```

!!! note 
    `gameObject.tint`是只写属性

## 深度与渲染顺序 {#depth-and-render-order}

游戏对象由他们在显示列表中的位置来渲染, 开始结束( 或回到前面) 。 默认这是您在现场添加的命令 。

您可以在显示列表中移动 :

```js
this.children.bringToTop(gameObject);

this.children.sendToBack(gameObject);

this.children.moveUp(gameObject);
this.children.moveDown(gameObject);
this.children.moveAbove(child1, child2);  // Move child1 above child2
this.children.moveBelow(child1, child2);  // Move child1 below child2

this.children.moveTo(gameObject, depth);
this.children.swap(child1, child2);
```

(`this.children`是场景显示列表,也发现于`this.sys.displayList`).

容器中的游戏对象可以通过容器的方法同样移动:

```js
container.bringToTop(gameObject);
// etc.
```

您可以指定一个深度排序( Z- index) :

```js
gameObject.depth = value;
gameObject.setDepth(value);
```

`depth`(z-index)是**排序顺序,而不是显示列表中的位置**。所有游戏对象的默认 `depth` 0. 深度排序到较小深度的前方。排序发生在场景做出之前。游戏对象在排序后保留其 `depth` 。

- 获得游戏对象的`depth`:

    ```javascript
    var depth = gameObject.depth;
    ```

您可以使用分数或负数来表示 `depth`。 您不需要使用巨大的值 。 

层层的游戏对象也可以这样进行深度排序,但容器中的游戏对象不能.

> 容器本身可以像其他任何东西一样进行深度排序,因此,当容器被用于容纳多个不同的实体时,即一个容器持有者会说所有敌人都有一个级别,而你突然想要一个级别高于其他级别时,它本身就可能成为一个问题。 在这种情况下,它需要从容器中移除,在另一个容器中(将提交清单的高度提升),然后在效果结束之前再放回去。

## 混合模式 {#blend-mode}

混合模式影响游戏对象在它下面的另一游戏对象时如何渲染.

混合模式在Canvas和WebGL下,以及从浏览器到浏览器,根据支持的不同,具有不同的效果.

- 获取游戏对象的混合模式 :

    ```javascript
    var blendMode = gameObject.blendMode;
    ```

- 设定游戏对象的混合模式 :

    ```javascript
    gameObject.blendMode = blendMode;
    gameObject.setBlendMode(blendMode);
    ```

### WebGL 与 Canvas {#webgl-and-canvas}

- `'NORMAL'`,或 ,或 , `Phaser.BlendModes.NORMAL`,或 ,或 , `0` 
    - 默认设置和绘制新形状, 覆盖现有画布内容 。
- `'ADD'`,或 ,或 , `Phaser.BlendModes.ADD`,或 ,或 , `1`
    - 在两种形状重叠的情况下,颜色通过添加颜色值来确定.
- `'MULTIPLY'`,或 ,或 , `Phaser.BlendModes.MULTIPLY`,或 ,或 , `2`
    - 像素属于顶层,与底层相应的像素相乘,结果为更暗的图片.
- `'SCREEN'`,或 ,或 , `Phaser.BlendModes.SCREEN`,或 ,或 , `3`
    - 像素是倒数,乘数,再反数,一个较轻的图片就是结果(对乘数)
- `'ERASE'`,或 ,或 , `Phaser.BlendModes.ERASE`,或 ,或 , `17`
    - Alpha 擦除混合模式。 只有在向帧缓冲器渲染时才有效, 如 * 渲染纹理 *

### 仅限 Canvas {#canvas-only}

- `'OVERLAY'`,或 ,或 , `Phaser.BlendModes.OVERLAY`,或 ,或 , `4`
    - 复数和屏幕的结合,底层上的暗部分变暗,光部分变轻.
- `'DARKEN'`,或 ,或 , `Phaser.BlendModes.DARKEN`,或 ,或 , `5`
    - 保留两层最黑暗的像素。
- `'LIGHTEN'`,或 ,或 , `Phaser.BlendModes.LIGHTEN`,或 ,或 , `6`
    - 保留两层最轻的像素.
- `'COLOR_DODGE'`,或 ,或 , `Phaser.BlendModes.COLOR_DODGE`,或 ,或 , `7`
    - 将底层除以倒数顶层。
- `'COLOR_BURN'`,或 ,或 , `Phaser.BlendModes.COLOR_BURN`,或 ,或 , `8`
    - 将倒转的底层除以顶层,然后反转结果。
- `'HARD_LIGHT'`,或 ,或 , `Phaser.BlendModes.HARD_LIGHT`,或 ,或 , `9`
    - 混合了倍数和屏幕,如覆面,但上层和下层互换.
- `'SOFT_LIGHT'`,或 ,或 , `Phaser.BlendModes.SOFT_LIGHT`,或 ,或 , `10`
    - 较软的硬灯版本,纯黑或白不会产生纯黑或白.
- `'DIFFERENCE'`,或 ,或 , `Phaser.BlendModes.DIFFERENCE`,或 ,或 , `11`
    - 从顶层或反方向切换下层,以获得一个正值。
- `'EXCLUSION'`,或 ,或 , `Phaser.BlendModes.EXCLUSION`,或 ,或 , `12`
    - 和不同,但对比较低
- `'HUE'`,或 ,或 , `Phaser.BlendModes.HUE`,或 ,或 , `13`
    - 保留底层的露马和染色体,同时采用顶层的花蕾.
- `'SATURATION'`,或 ,或 , `Phaser.BlendModes.SATURATION`,或 ,或 , `14`
    - 保留底层的露马和花蕾,同时采用顶层的染色体.
- `'COLOR'`,或 ,或 , `Phaser.BlendModes.COLOR`,或 ,或 , `15`
    - 保留底层的露米,同时采用顶层的乳腺和铬.
- `'LUMINOSITY'`,或 ,或 , `Phaser.BlendModes.LUMINOSITY`,或 ,或 , `16`
    - 保留底层层的乳腺和铬,同时采用顶层的乳腺.
- `'SOURCE_IN'`,或 ,或 , `Phaser.BlendModes.SOURCE_IN`,或 ,或 , `18`
    - 新的形状只有在新形状和目的地画布重叠时才画出来。其他的都透明。
- `'SOURCE_OUT'`,或 ,或 , `Phaser.BlendModes.SOURCE_OUT`,或 ,或 , `19`
    - 新形状绘制时不与现有的画布内容重叠.
- `'SOURCE_ATOP'`,或 ,或 , `Phaser.BlendModes.SOURCE_ATOP`,或 ,或 , `20`
    - 新形状只画在与现有画布内容重叠的地方.
- `'DESTINATION_OVER'`,或 ,或 , `Phaser.BlendModes.DESTINATION_OVER`,或 ,或 , `21`
    - 在现有画布内容后面绘制新的形状。
- `'DESTINATION_IN'`,或 ,或 , `Phaser.BlendModes.DESTINATION_IN`,或 ,或 , `22`
    - 现有的画布内容保存在新形状和现有的画布内容重叠的地方。其他内容都透明。
- `'DESTINATION_OUT'`,或 ,或 , `Phaser.BlendModes.DESTINATION_OUT`,或 ,或 , `23`
    - 现存内容保存在不与新形状重叠的地方.
- `'DESTINATION_ATOP'`,或 ,或 , `Phaser.BlendModes.DESTINATION_ATOP`,或 ,或 , `24`
    - 现有的画布只保存在与新形状重叠的地方。新形状在画布内容后面绘制。
- `'LIGHTER'`,或 ,或 , `Phaser.BlendModes.LIGHTER`,或 ,或 , `25`
    - 在两种形状重叠的情况下,颜色通过添加颜色值来确定.
- `'COPY'`,或 ,或 , `Phaser.BlendModes.COPY`,或 ,或 , `26`
    - 仅显示新形状 。
- `'XOR'`,或 ,或 , `Phaser.BlendModes.XOR`,或 ,或 , `27`
    - 形状在其他地方都重叠和正常地画出来时,是透明的。

## 效果 {#effects}

所有效果都只使用WebGL模式,没有画布对应物. 效果包括:

- 弹匣扭曲
- Bloom
- Blur
- 博凯/ 倾斜移动
- 圆形轮廓
- 颜色矩阵
- Glow
- Displacement
- Gradient
- Pixelate
- Shine
- Shadow
- Vignette
- 擦拭/ 曝光

> FX前身只针对纹理游戏对象(Sprite,TileSprite,Video等),但Post FX适用于包括摄像机在内的任何事物,区别在于Pre FX可以改变游戏对象的实际图画,这类似于有自定义的管道,但压力要小得多.
> 
> 如果将“FX”应用到一个容器,那么它将使所有的孩子都进入这个FX,然后运行着色器,然后将结果放入游戏中 — — 因此如果你有一个“光”着色器,它就会将所有东西都作为单一物体发光。 另一方面,FX前导会依次发光每个物体。如此昂贵,但可能更多取决于游戏结果。

## 滚动因子 {#scroll-factor}

滚动因子控制了摄像机滚动时游戏对象移动多少(相对于游戏画布).

- 获取游戏对象的滚动因子 :
    
    ```javascript
    var scrollFactorX = gameObject.scrollFactorX;
    var scrollFactorY = gameObject.scrollFactorY;
    ```

- 设置游戏对象的滚动因子 :

    ```javascript
    gameObject.setScrollFactor(scrollFactor);
    gameObject.setScrollFactor(scrollFactorX, scrollFactorY);
    ```

滚动因子: 0~1

- 0=固定在摄像机上
- 0.25=摄像机速度的四分之一
- 0.5 = 摄像机速度的一半

默认值为(1,1). 滚动因子(0,0)可用于固定背景或UI元素. 0到1之间的因子可用于 Parlax 滚动效应.

对物理游戏对象不要使用1,1以外的滚动因子,因为没有意义.

## 状态 {#state}

您可以在 `state` 字段中存储简单的值( 数字或字符串) 。

- 获取游戏对象的状态 :

    ```javascript
    var state = gameObject.state;
    ```

- 设定游戏对象的状态 :
    ```javascript
    gameObject.setState(state);
    ```

- Examples:

    ```js
    // State
    mummy.state = 'sleeping';
    bat.state = 'movingLeft';

    // Coins
    treasure.state = 10;
    treasure.state -= 1;

    // Health
    snake.state = 3;
    ```

## 数据 {#data}

使用数据存储来进行结构化化化化化化的处理,或者使用大量数据。默认情况下,数据管理器会被设定为 `null`。通常不需要启用,因为数据在添加时会自动启用。要启用游戏对象的数据管理器:
    
```javascript
gameObject.setDataEnabled();
```

- 获取游戏对象的数据 :

    ```javascript
    var value = gameObject.getData(key);
    var values = gameObject.getData(keys); // keys: an array of keys
    var value = gameObject.data.values[key];
    ```

    Example:

    ```js
    mummy.getData('health'); // → 3
    ```
- 设定游戏对象的数据( 自动启用数据管理器 ) :

    ```javascript
    gameObject.setData(key, value);
    gameObject.incData(key, value); // increments existing value or if the key doesn't exist, increases the value from 0
    gameObject.setData(obj); // obj: {key0:value0, key1:value1, ...}
    gameObject.data.values[key] = value;
    gameObject.data.values[key] += inc;
    gameObject.toggleData(key); // toggles a boolean value for the given key or if the key doesn't exist, toggles the value from false
    ```

    Example:

    ```js
    mummy.setData('isAlive', true);
    mummy.setData('health', 3);
    mummy.incData('health', 3); // increments existing value (health += 3) or if the key doesn't exist, increases the value from 0

    let obj = { health: 3 };
    mummy.setData(obj);
    mummy.data.values['health'] = 3;
    mummy.data.values['health'] += 3;

    mummy.toggleData('isAlive');
    ```

数据存储在添加或更改值时会释放事件( 从游戏对象本身) 。 请在绑定任何数据更改的事件之前, 请确定数据管理器已被启用 。

- 设定数据流

    ```javascript
    gameObject.on('setdata', function(gameObject, key, value){ /* ... */ });
    ```

- 更改数据事件

    ```javascript
    gameObject.on('changedata', function(gameObject, key, value, previousValue){ /* ... */ });
    ```

    ```javascript
    gameObject.on('changedata-' + key, function(gameObject, value, previousValue){ /* ... */ });
    ```

    Example:

    ```js
    mummy.on('changedata-health', (gameObject, dataKey, dataValue) => {/*…*/});
    ```

您可以存储其他对象, 如游戏对象, 计时器事件, 或是 tweens。 当父游戏对象被销毁时, 数据存储被清除, 所以清理没有问题 。

```js
const cat = this.add.sprite(/*…*/);

mummy.setData('familiar', cat);
// …
mummy.destroy();
```

## 名称 {#name}

您可以使用 `name` 字段来识别您的游戏对象, 用于游戏逻辑或调试. Phaser 不使用此字段.

- 获取游戏对象名称 :

    ```javascript
    var name = gameObject.name;
    ```

- 设定游戏对象名称 :

    ```javascript
    gameObject.setName(name);
    gameObject.name = name;
    ```

- Example:

    ```js
    this.add.sprite(0, 0, 'bat').setName('bat1');

    mummy.setName('Reginald');
    ```

## 类型 {#type}

比如"TileSprite" Phaser用这个,你应该别管它了.

## 事件 {#events}

游戏对象直接发出事件.

每个游戏对象都发出 [ADDED_TO_SCENE](/api/event/gameobjects-events#added_to_scene), [REMOVED_FROM_SCENE](/api/event/gameobjects-events#removed_from_scene),和 [DESTROY](/api/event/gameobjects-events#destroy). `ADDED_TO_SCENE` 财务报告和已审计财务报表 `REMOVED_FROM_SCENE` 添加或删除任何显示列表时,例如容器,则会开火。 `DESTROY` 只会发生一次

动画游戏对象(如Sprite)也发出[animation events](/api/event/animations-events).

互动游戏对象也发出互动事件.

电子游戏对象也发出回放事件.

拥有数据存储的游戏对象也发出[data events](/api/event/data-events).

## 创建模式 {#creation-patterns}

`make`方法灵活,与结构化数据配合良好,如JSON.

团体提供`create()`和`createMultiple()`方法.

游戏对象创建的组织方式简单,不扩展类:

```js
function create() {
  const mummy = createMummy.call(this, 0, 0);
}

function createMummy(x, y) {
  return this.add.mummy(x, y, 'mummy');
}
```

如果你不喜欢`call()`:

```js
function create() {
  const mummy = createMummy(this, 0, 0);
}

function createMummy(scene, x, y) {
  return scene.add.mummy(x, y, 'mummy');
}
```

无需扩展课程,您可以添加创作和工厂方法:

```js
function create() {
  const mummy = this.add.mummy(0, 0);
}

Phaser.GameObjects.GameObjectFactory.register('mummy', function (x, y) {
  return this.sprite(x, y, 'mummy');
}
```

## 扩展游戏对象 {#extending-game-objects}

大多数初学者现在不应该扩展游戏对象类.

选择一个类, 以扩展和调用 `super()` , 并带有所有所需的参数。 不要自行扩展 [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) 。

```js
class MummySprite extends Phaser.GameObjects.Sprite {
  constructor(scene, x, y, texture = 'mummy', frame = 0) {
    super(scene, x, y, texture, frame);
    // this.scene, this.x, this.y, this.texture, this.frame are set.
  }
}
```

Phaser游戏对象类不**将自己添加到现场,因此`super()`不会这样做.

游戏对象在现场中分别添加:

```js
this.add.existing(new MummySprite(this, 0, 0));
```

或者从班上加:

```js
this.scene.add.existing(this);
```

如果您超越了类的 `preUpdate()` 方法, 请使用相同的参数调用超类方法。 否则游戏对象可能会被冻结 。

```js
class MummySprite extends Phaser.GameObjects.Sprite {
  // …
  preUpdate (time, delta) {
    super.preUpdate(time, delta);
    // …
  }
}
```

如果您超过该类的 `destroy()` 方法, 请也叫超类方法。 或者考虑使用 [DESTROY](/api/event/gameobjects-events#destroy) 事件 。

游戏对象的 `update()` 方法不自动调用。 您可以

- 自行调用 `update()`方法;或
- 将游戏对象添加到带有 `runChildUpdate = true` 的组; 或
- 将 `update()` 方法绑定在现场的 UPDATE 事件(参数匹配):

```js
class MummySprite extends Phaser.GameObjects.Sprite {
  constructor () {
    // …
    const { events } = this.scene;

    events.on('update', this.update, this);

    this.once('destroy', function () {
      events.off('update', this.update, this);
    }, this);
  }

  update (time, delta) {
    // …
  }
}
```

## 自定义游戏对象类 {#custom-game-object-classes}

- 创建持有游戏对象的纯实体类 :

    ```js
    class Mummy {
        constructor (scene, x, y) {
            this.sprite = scene.add.sprite(x, y, 'mummy');
            
            // You may need to reach the parent object from the sprite, e.g., from within a callback.
            this.sprite.setData('parent', this);

            this.sprite.once('destroy', this.onSpriteDestroyed, this);
        }
        
        onSpriteDestroyed (sprite) {
            this.sprite = null;
        }
    }
    ```

- 创建自定义游戏对象类 :

    ```javascript
    class MyClass extends BaseClass {
        constructor(scene, x, y) {
            super(scene, x, y);
            // ...
            scene.add.existing(this);
        }
        // ...

        // preUpdate(time, delta) {
        //     if (super.preUpdate) {
        //         super.preUpdate(time, delta);
        //     }
        // }

        // destroy(fromScene) {
        //     //  This Game Object has already been destroyed
        //     if (!this.scene) {
        //         return;
        //     }
        //     super.destroy(fromScene);
        // }
    }
    ```

    - `scene.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
        - 如果游戏对象使它成为了,它会被添加到显示列表中.
        - 如果它有`preUpdate`方法,它将被添加到更新列表中.
            - 一些类型的游戏对象如Sprite,Dom-element已经拥有`preUpdate`方法.

- 创建自定义类实例 :

    ```javascript
    var image = new MyClass(scene, x, y, key);
    ```

## 常见问题 {#common-problems}

### 我加了一个游戏对象,但看不见 {#i-added-a-game-object-but-i-cant-see-it}

游戏开发商的哀叹.

- 是在摄像机的视门外
- 是在另一个游戏对象后面
- 它有"默认"(空白)纹理
- 显示列表上没有
- 里面有`visible === false`的音乐
- 里面有`alpha === 0`的音乐
- 它有0级
- 蒙着面
- 已经销毁了

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。
- [RexRainbow](https://github.com/rexrainbow)
- [samme](https://github.com/samme)

---
