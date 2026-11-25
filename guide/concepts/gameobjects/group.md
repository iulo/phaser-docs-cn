# 组（Group） {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/group)

A组是您创建、 操纵或循环类似游戏对象的一种方式。 组成员不是专属的。 游戏对象可以属于多个组, 一个组, 也可以是无组 。

团体本身是无法显示的,不能被定位,旋转,缩放,或隐藏.

## 添加组对象 {#add-group-object}

```javascript
var group = this.add.group(config);
// var group = this.add.group(gameObjects, config);  // Add game objects into group
```

- `config`

    ```javascript
    {
        classType: Phaser.GameObjects.Sprite,
        defaultKey: null,
        defaultFrame: null,
        active: true,
        maxSize: -1,
        runChildUpdate: false,
        createCallback: null,
        removeCallback: null,
        createMultipleCallback: null
    }
    ```

  - `classType` :
    - [Sprite](/guide/concepts/gameobjects/sprite) : `Phaser.GameObjects.Sprite`
    - [Image](/guide/concepts/gameobjects/image) : `Phaser.GameObjects.Image`
  - `runChildUpdate` 设置 `true` 要运行 `gameObject.update()` 每一个滴答。
  - `createCallback` : 添加或创建组成员时要调用的函数.

    ```javascript
    var callback = function(gameObject) {
    }
    ```

  - `removeCallback` : 一个在删除组成员时要调用的函数 。

    ```javascript
    var callback = function(gameObject) {
    }
    ```

  - `createMultipleCallback` : 一次创建多个组成员时要调用的一个函数 。

    ```javascript
    var callback = function(gameObjects) {
    }
    ```

## 添加游戏对象 {#add-game-object}

```javascript
group.add(gameObject);
// group.add(gameObject, true);  // add this game object to display and update list of scene
```

```javascript
group.addMultiple(gameObjects);   // array of game objects
// group.addMultiple(gameObjects, true);
```

- 游戏对象只添加一次.
- 游戏对象在被破坏时会自动删除.

## 删除游戏对象 {#remove-game-object}

```javascript
group.remove(gameObject);
// group.remove(gameObject, true);  // also remove this game object from display and update list of scene
```

删除所有游戏对象

```javascript
group.clear();
// group.clear(removeFromScene, destroyChild);
```

## 获取游戏对象 {#get-game-objects}

- 获取所有游戏对象.

    ```javascript
    var gameObjects = group.getChildren();  // array of game objects
    ```

- 获取所有匹配的游戏对象

    ```javascript
    var gameObjects = group.getMatching(property, value);
    // var gameObjects = group.getMatching(property, value, startIndex, endIndex);
    ```

- 游戏对象的数量 。

    ```javascript
    var len = group.getLength();
    ```

- 组装满了,马克森的大小设定在`maxSize`中.

    ```javascript
    var isFull = group.isFull();
    ```

- 游戏对象为组.

    ```javascript
    var isInGroup = group.contains(child);
    ```

## 集体行动 {#group-actions}

### 财产 {#property}

- 设置属性

    ```javascript
    group.propertyValueSet(key, value);
    // group.propertyValueSet(key, value, step, index, direction);
    ```

  - `direction` :
    - `1` : 从开始到结束
    - 由尾到尾的`-1`:
- 增加财产

    ```javascript
    group.propertyValueInc(key, value);
    // group.propertyValueInc(key, value, step, index, direction);
    ```

  - `direction` :
    - `1` : 从开始到结束
    - 由尾到尾的`-1`:

### 职位 {#position}

- 设置位置

    ```javascript
    group.setX(value);
    // group.setX(value, step);
    group.setX(value);
    // group.setY(value, step);
    group.setXY(x, y);
    // group.setXY(x, y, stepX, stepY);
    ```

- 增加位置( E)

    ```javascript
    group.incX(value);
    // group.incX(value, step);
    group.incY(value);
    // group.incY(value, step);
    group.incXY(x, y);
    // group.incXY(x, y, stepX, stepY);
    ```

- 移动位置

    ```javascript
    group.shiftPosition(x, y);
    // group.shiftPosition(x, y, direction);
    ```

  - `direction` :
    - `0` : 首到最后一页
    - `1` : 最后一个至第一个

### 角度 {#angle}

- 设定角度

    ```javascript
    group.angle(value);
    // group.angle(value, step);
    ```

    or

    ```javascript
    group.rotate(value);
    // group.rotate(value, step);
    ```

- 旋转

    ```javascript
    group.rotateAround(point, angle);
    ```

    or

    ```javascript
    group.rotateAroundDistance(point, angle, distance);
    ```

### 可见 {#visible}

- 设定可见

    ```javascript
    group.setVisible(value);
    // group.setVisible(value, index, direction);
    ```

  - `index`: 从项目阵列中开始搜索的可选偏移 。
  - `direction` : 向通过阵列的斜拉线方向。
    - `1` : 从开始到结束
    - 由尾到尾的`-1`:
- 切换可见

    ```javascript
    group.toggleVisible();
    ```

### 阿尔法 {#alpha}

- 设置阿尔法

    ```javascript
    group.setAlpha(value);
    // group.setAlpha(value, step);
    ```

### 叮当 {#tint}

- 设置线

    ```javascript
    group.setTint(value);
    // group.setTint(topLeft, topRight, bottomLeft, bottomRight);
    ```

### 混合模式 {#blend-mode}

- 设定 [blend mode](/guide/concepts/display#blend-mode)

    ```javascript
    group.setBlendMode(value);
    ```

### 缩放 {#scale}

- 设定比例

    ```javascript
    group.scaleX(value);
    // group.scaleX(value, step);
    group.scaleY(value);
    // group.scaleY(value, step);
    group.scaleXY(scaleX, scaleY);
    // group.scaleXY(scaleX, scaleY, stepX, stepY);
    ```

### 来源 {#origin}

- 设定来源

    ```javascript
    group.setOrigin(originX, originY);
    // group.setOrigin(originX, originY, stepX, stepY);
    ```

### 深度 {#depth}

- 设置深度

    ```javascript
    group.setDepth(value, step);
    ```

### 动画 {#animation}

- 播放动画

    ```javascript
    group.playAnimation(key, startFrame);
    ```

### 命中区域 {#hit-area}

- 设定命中区域

    ```javascript
    group.setHitArea();
    // group.setHitArea(hitArea, hitAreaCallback);
    ```

### 散牌游戏 {#shuffle}

- 摇摆阵列

    ```javascript
    group.shuffle();
    ```

## 活动/ 不活动游戏对象 {#activeinactive-game-objects}

- 设定不活动

    ```javascript
    group.kill(gameObject);         // gameObject.setActive(false)
    group.killAndHide(gameObject);  // gameObject.setActive(false).setVisible(false)
    ```

- 活动游戏对象的数量

    ```javascript
    var activeCount = group.countActive();
    ```

    or

    ```javascript
    var activeCount = group.getTotalUsed();
    ```

- 活动游戏对象的数量

    ```javascript
    var inactiveCount = group.countActive(false);
    ```

- 免费( maxSize - activeCount) 游戏对象的数量

    ```javascript
    var freeCount = group.getTotalFree();  // group.maxSize - group.getTotalUsed()
    ```

- 获取第一个活动/ 非活动游戏对象,
  - 如果没有选中游戏对象, 返回 `null` 。

    ```javascript
    var gameObject = group.getFirst(active);  // active = true/false
    var gameObject = group.getFirstAlive(); // Equal to group.getFirst(true, ...)
    var gameObject = group.getFirstDead(); // Equal to group.getFirst(false, ...)
    ```

  - 如果没有选中游戏对象, 请创建一个 。

    ```javascript
    var gameObject = group.getFirst(active, true, x, y, key, frame, visible);  // active = true/false
    var gameObject = group.getFirstAlive(true, x, y, key, frame, visible); // Equal to group.getFirst(true, ...)
    var gameObject = group.getFirstDead(true, x, y, key, frame, visible); // Equal to group.getFirst(false, ...)
    var gameObject = group.get(x, y, key, frame, visible); // Equal to group.getFirst(false, true, ...)
    ```

    - 使用(`x`,`y`,`key`,`frame`),创建[Image](/guide/concepts/gameobjects/image)/[Sprite](/guide/concepts/gameobjects/sprite)游戏对象.

    ```javascript
    var newGameObject = new GameObjectClass(x, y, key, frame);
    ```

## 创建游戏对象 {#create-game-objects}

```javascript
var gameObjects = group.createFromConfig(config);
var gameObjects = group.createMultiple(config);    // config in array
```

- `config`

    ```javascript
    {
        classType: this.classType,
        key: undefined,             // Required
        frame: null,
        visible: true,
        active: true,
        repeat: 0,                  // Create (1 + repeat) game objects
        createCallback: undefined,  // Override this.createCallback if not undefined

        // Position
        setXY: {
            x:0,
            y:0,
            stepX:0,
            stepY:0
        },
        // Actions.SetXY(gameObjects, x, y, stepX, stepY)
        gridAlign: false,
        // {
        //     width: -1,
        //     height: -1,
        //     cellWidth: 1,
        //     cellHeight: 1,
        //     position: Phaser.Display.Align.TOP_LEFT,
        //     x: 0,
        //     y: 0
        // }
        // Actions.GridAlign(gameObjects, gridAlign)

        // Angle
        setRotation: {
            value: 0,
            step:
        },
        // Actions.SetRotation(gameObjects, value, step)

        // Scale
        setScale: {
            x:0,
            y:0,
            stepX:0,
            stepY:0
        },
        // Actions.SetScale(gameObjects, x, y, stepX, stepY)

        // Alpha
        setAlpha: {
            value: 0,
            step:
        },
        // Actions.SetAlpha(gameObjects, value, step)

        setOrigin: {
            x:0,
            y:0,
            stepX:0, 
            stepY:0
        },

        // Input
        hitArea: null,
        hitAreaCallback: null,
        // Actions.SetHitArea(gameObjects, hitArea, hitAreaCallback)
    }
    ```

  - `classType` :
    - [Sprite](/guide/concepts/gameobjects/sprite): `Phaser.GameObjects.Sprite`
    - [Image](/guide/concepts/gameobjects/image): `Phaser.GameObjects.Image`

## 摧毁 {#destroy}

- 仅销毁组

    ```javascript
    group.destroy();
    ```

- 摧毁群体和儿童

    ```javascript
    group.destroy(true);
    ```

## 作者的信用额度 {#author-credits}

本页的内容包括下列工作:

- [RexRainbow](https://github.com/rexrainbow)

---
