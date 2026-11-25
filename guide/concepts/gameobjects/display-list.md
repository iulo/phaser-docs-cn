# 显示列表 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/display-list)

Phaser使用显示列表来管理游戏对象在世界内的顺序。每个场景都有自己的显示列表。当您在显示列表中添加游戏对象时,它会自动添加到显示列表中。显示列表是特殊类型的容器,可以控制游戏对象的渲染顺序。默认情况下,游戏对象会按照添加到显示列表的顺序进行渲染。

显示列表还负责管理游戏对象在世界范围内的位置。当您在显示列表中添加一个游戏对象时,它会自动被定位在列表的底部。这意味着它将被先渲染,因此出现在所有其他游戏对象的后面。

您可以使用它的辅助功能, 如 `sendToBack`、 `moveDown`、 `bringToTop` 和 `moveUp` 来改变游戏对象在显示列表中的位置。 这些功能允许您将游戏对象移动到显示列表周围, 从而影响显示的顺序或输入事件的检查顺序, 因为对象“ 在顶端” 获得输入优先级 。

内 Phaser 2 有可能作为另一个游戏对象的孩子添加游戏对象。 实际上,它们都是自成一体的显示列表。 情况已不复存在 。 Phaser 3. 唯一游戏对象 Phaser 3,可以生孩子的,是: 3,可以生小孩的,是: 4,可以生孩子的3,是: 3 [Container](/guide/concepts/gameobjects#parent-containers) 游戏对象.

## 访问场景中的显示列表 {#accessing-the-display-list-in-a-scene}

每个场景都有名为`children`的属性,这是该场景显示列表的参考. 这个`children`属性允许您更改每个游戏对象的渲染顺序.

```js
let displayList = this.children;
```

- `this` :指当前场景.
- `children`:代表该场景的显示列表对象.

## 显示列表方法 {#display-list-methods}

当您创建游戏对象(例如图示、图像、文本)时, Phaser会自动将其添加到场景的显示列表中。 但是, 如果需要, 您也可以手动将对象添加到显示列表中。 显示对象的顺序取决于它们在显示列表中的顺序。 添加的对象会比先前添加的对象多, 除非您修改其深度或使用各种显示列表方法重新排列它们 。

### 将游戏对象添加到显示列表 {#adding-game-objects-to-the-display-list}

- 创建新的游戏对象,并使用场景游戏对象工厂添加.

  ```js
  let player = this.add.sprite(400, 300, "player");
  ```

- 添加一个已有的游戏对象

  ```js
  const player = new Phaser.GameObjects.Sprite(this, x, y, "player");
  player.addToDisplayList();
  ```

  Or

  ```js
  const player = new Phaser.GameObjects.Sprite(this, x, y, "player");
  this.children.add(player);
  ```

  - `this`:指当前场景

### 从显示列表中删除游戏对象 {#removing-game-objects-from-the-display-list}

- 使用 `destroy()` 将游戏对象从游戏中移除, 如果您再也没有计划使用它。 `destroy()` 也将它从显示列表、 更新列表、 输入管理器和物理管理器中移除。 只要您自己的代码中没有关于游戏对象的引用, 它就应该可以免费使用浏览器收集垃圾 。

  ```js
  let player = this.add.sprite(400, 300, "player");
  player.destroy();
  ```

- 从场景显示列表中删除一个已有的游戏对象 。

  ```js
  let player = this.add.sprite(400, 300, "player");
  player.removeFromDisplayList();
  ```

  Or

  ```js
  let player = this.add.sprite(400, 300, "player");
  this.children.remove(player);
  ```

### 排序游戏对象 {#sorting-game-objects}

- 将游戏对象移动到显示列表的顶端。

  ```js
  this.children.bringToTop(gameObject); // gameObject renders above all other objects
  ```

- 将游戏对象移动到显示列表的底部。

  ```js
  this.children.sendToBack(gameObject); // gameObject renders below all other objects
  ```

- 按深度排序

  默认情况下,Game Objects的创建深度为0. 深度值较高的Game Object总是在数值较低的一个前方渲染.

  - 获取游戏对象深度

    ```js
    const depth = gameObject.depth; // Returns the depth of this Game Object within the Scene.
    ```

  - 设定游戏对象深度

    ```js
    gameObject.setDepth(depth);
    ```

  - 示例

    ```js
    player.setDepth(2); // Set a higher depth for the player to render above other objects
    background.setDepth(0); // Set a lower depth for the background
    this.children.depthSort(); // Sort all game objects based on their depth values
    ```

- 上下移动游戏对象

  - 将游戏对象上移到一个位置

    ```js
    this.children.moveUp(gameObject);
    ```

  - 将游戏对象下移到一个位置

    ```js
    this.children.moveDown(gameObject);
    ```

### 从显示列表中获取游戏对象 {#retrieving-a-game-object-from-the-display-list}

```js
let gameObject = this.children.getAt(index);
```

- `index`:游戏对象在显示列表中的位置(开始于0).

Example:

```js
let firstObject = this.children.getAt(0); // Retrieves the first object in the Display List
```

---
