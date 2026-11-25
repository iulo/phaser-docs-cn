# 输入 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/input)

Phaser维持一个在所有浏览器和设备上都起作用的统一输入系统。我们统一是指,您不必担心用户是否在桌面上有鼠标,还是移动设备上有触摸输入,甚至一个触摸能力桌面。您只需要聆听和响应Phaser提供的输入事件。您也可以对键盘和游戏盘上的输入事件作出回应。

内部有一个全局输入管理器,每个场景都有输入插件的例子。输入管理器负责监听本地的 DOM 事件,如鼠标移动、触摸手势和键盘按键。然后将这些事件传递给输入插件,然后由它们处理。

默认情况下, Phaser 中的 Game Objects 不处理输入。 这是因为并非所有 Game Objects 都需要对输入作出回应。 例如, 背景图像或游戏标志可能不需要对输入作出回应, 而需要按钮。 因此, 您必须启用您特别想要对输入作出回应的 Game Objece 上的输入处理 。

一旦启用输入, 游戏对象将先从输入插件中听到输入事件, 并检查是否已被“ 点击 ” 。 有很多事件可以释放, 如上下事件、 拖动事件、 滚动轮事件等。 我们将在本指南中更详细地探索这些事件, 以及输入系统的内部工作方式。 目前, 只需知道您可以启用对几乎所有游戏对象的输入, 然后按您的游戏要求对它所显示的事件作出反应 。

## 启用输入的游戏对象 {#enabling-a-game-object-for-input}

Phaser将鼠标和触摸(指针)事件组合为一个统一的API,当您启用一个游戏对象输入并听取一个事件,如“指针下沉”时,鼠标点击桌面或移动上指针导致的鼠标,则无关紧要. Phaser会发出同一事件供您游戏听.

要启用输入的游戏对象 :

```js
gameObject.setInteractive();
```

并非所有游戏对象都可以接收输入。 请检查API 文档中的具体内容。 然而, 所有常见的文档( Sprites, Images, Text, 等) 都可以 。

## 设置受打击区域 {#setting-hit-areas}

`setInteractive`方法可以取自定制的命中区域.

- 设定游戏对象使用的纹理从宽度和高度( 矩形) 的命中区域 :

  ```js
  gameObject.setInteractive();
  ```

- 从游戏对象设定命中区域

  ```js
  gameObject.setInteractive(shape, callback);
  ```

  - [Circle](/guide/concepts/geometry#circle)
    - 形状 : `new Phaser.Geom.Circle(x, y, radius)`
    - 回调: `Phaser.Geom.Circle.Contains`
  - [Ellipse](/guide/concepts/geometry#ellipse)
    - 形状 : `new Phaser.Geom.Ellipse(x, y, width, height)`
    - 回调: `Phaser.Geom.Ellipse.Contains`
  - [Rectangle](/guide/concepts/geometry#rectangle)
    - 形状 : `new Phaser.Geom.Rectangle(x, y, width, height)`
    - 回调: `Phaser.Geom.Rectangle.Contains`
  - [Triangle](/guide/concepts/geometry#triangle)
    - 形状 : `new Phaser.Geom.Triangle(x1, y1, x2, y2, x3, y3)`
    - 回调: `Phaser.Geom.Triangle.Contains`
  - [Polygon](/guide/concepts/geometry#polygon)
    - 形状 : `new Phaser.Geom.Polygon(points)`
    - 回调: `Phaser.Geom.Polygon.Contains`
  - [Hexagon](https://phaser.io/oss/docs/phaser/concepts/geometry.md#Hexagon)
    - 形状 : `new Phaser.Geom.rexHexagon(x, y, size, type)`
    - 回调: `Phaser.Geom.Polygon.Contains`
  - [Rhombus](https://phaser.io/oss/docs/phaser/concepts/geometry.md#Rhombus)
    - 形状 : `new Phaser.Geom.rexRhombus(x, y, width, height)`
    - 回调: `Phaser.Geom.Polygon.Contains`
  - 说明: `x`, `y` 与《京都议定书》 gameObject.

- 从输入插件中设定命中区域

  ```js
  scene.input.setHitArea(gameObjects, shape, callback);
  ```

  - Circle

    ```js
    scene.input.setHitAreaCircle(gameObjects, x, y, radius);
    // scene.input.setHitAreaCircle(gameObjects, x, y, radius, callback); // callback = Circle.Contains
    ```

  - Ellipse

    ```js
    scene.input.setHitAreaEllipse(gameObjects, x, y, width, height);
    // scene.input.setHitAreaEllipse(gameObjects, x, y, width, height, callback); // callback = Ellipse.Contains
    ```

  - Rectangle

    ```js
    scene.input.setHitAreaRectangle(gameObjects, x, y, width, height);
    // scene.input.setHitAreaRectangle(gameObjects, x, y, width, height, callback); // callback = Rectangle.Contains
    ```

  - Triangle

    ```js
    scene.input.setHitAreaTriangle(gameObjects, x1, y1, x2, y2, x3, y3);
    // scene.input.setHitAreaTriangle(gameObjects, x1, y1, x2, y2, x3, y3, callback); // callback = Triangle.Contains
    ```

  - 说明: `x`, `y` 与《京都议定书》 gameObject.

- 设定交互式配置

  ```js
  gameObject.setInteractive({
    hitArea: shape,
    hitAreaCallback: callback,
    hitAreaDebug: shape,
    draggable: false,
    dropZone: false,
    useHandCursor: false,
    cursor: CSSString,
    pixelPerfect: false,
    alphaTolerance: 1,
  });
  ```

  - 命中区域
    - shape
    - 像素α
      - `pixelPerfect` : `true`
      - `alphaTolerance` : `1` (0-255)
    - 自定义命中测试功能
      - `hitAreaCallback`
        `javascript
        函数(形状, x, y, gameObject) {
            返回命中; // 真实/ 假
        }
        `
        - `shape` : 命中区域对象
        - `x`,`y`:纹理的局部位置.
        - `gameObject` : 游戏对象.
    - `hitAreaDebug` :调试形状.
  - [Dragging](#dragging)
    - `draggable` : `true`
  - [Drop zone](#drop-zone)
    - `dropZone` : `true`
  - [Cursor](#cursor)
    - `cursor` : CSS 字符串
    - `useHandCursor` : `true`

警告"像素完美测试"
这是一个昂贵的过程,只应在真正需要它的游戏对象上启用.

## 禁用输入 {#disable-input}

- 禁用临时

  ```js
  gameObject.disableInteractive();
  ```

- 删除交互

  ```js
  gameObject.removeInteractive();
  ```

## 仅限游戏对象输入 {#top-only-game-object-input}

当设定到 `true` 时, 此输入插件将只从显示列表中最顶级的游戏对象中释放事件来模拟 DOM 行为 。
如果设定为 `false`, 它将会从指针下方的所有游戏对象中释放出事件, 而不仅仅是顶部的事件 。

- 仅获取游戏对象输入值 :

  ```js
  var topOnly = scene.input.topOnly;
  ```

- 设置仅顶部游戏对象输入值 :

  ```js
  scene.input.topOnly = value; // true or false
  scene.input.setTopOnly(value); // true or false
  ```

每个场景都可以有自己的`scene.input.topOnly`设定.

## 触摸活动 {#touch-events}

从上到下都触发这些事件.

1. 触摸游戏对象的事件

   ```js
   gameObject.on(
     "pointerdown",
     function (pointer, localX, localY, event) {
       /* ... */
     },
     scope
   );
   gameObject.on(
     "pointerup",
     function (pointer, localX, localY, event) {
       /* ... */
     },
     scope
   );
   gameObject.on(
     "pointermove",
     function (pointer, localX, localY, event) {
       /* ... */
     },
     scope
   );
   gameObject.on(
     "pointerover",
     function (pointer, localX, localY, event) {
       /* ... */
     },
     scope
   );
   gameObject.on(
     "pointerout",
     function (pointer, event) {
       /* ... */
     },
     scope
   );
   ```

   - 取消剩余的触摸事件

     ```js
     function(pointer, localX, localY, event) {
         event.stopPropagation();
     }
     ```

2. 在每个触摸的游戏对象的输入插件上的事件

   ```js
   scene.input.on(
     "gameobjectdown",
     function (pointer, gameObject, event) {
       /* ... */
     },
     scope
   );
   scene.input.on(
     "gameobjectup",
     function (pointer, gameObject, event) {
       /* ... */
     },
     scope
   );
   scene.input.on(
     "gameobjectmove",
     function (pointer, gameObject, event) {
       /* ... */
     },
     scope
   );
   scene.input.on(
     "gameobjectover",
     function (pointer, gameObject, event) {
       /* ... */
     },
     scope
   );
   scene.input.on(
     "gameobjectout",
     function (pointer, gameObject, event) {
       /* ... */
     },
     scope
   );
   ```

   - 取消未触及的事件

     ```js
     function(pointer, gameObject, event) {
         event.stopPropagation();
     }
     ```

3. 获取 ** ** 全部** 被触摸的游戏对象的事件

   ```js
   scene.input.on(
     "pointerdown",
     function (pointer, currentlyOver) {
       /* ... */
     },
     scope
   );
   scene.input.on(
     "pointerdownoutside",
     function (pointer) {
       /* ... */
     },
     scope
   );
   scene.input.on(
     "pointerup",
     function (pointer, currentlyOver) {
       /* ... */
     },
     scope
   );
   scene.input.on(
     "pointerupoutside",
     function (pointer) {
       /* ... */
     },
     scope
   );
   scene.input.on(
     "pointermove",
     function (pointer, currentlyOver) {
       /* ... */
     },
     scope
   );
   scene.input.on(
     "pointerover",
     function (pointer, justOver) {
       /* ... */
     },
     scope
   );
   scene.input.on(
     "pointerout",
     function (pointer, justOut) {
       /* ... */
     },
     scope
   );
   scene.input.on(
     "gameout",
     function (timeStamp, domEvent) {
       /* ... */
     },
     scope
   );
   scene.input.on(
     "gameover",
     function (timeStamp, domEvent) {
       /* ... */
     },
     scope
   );
   ```

   - 检查`pointer.camera`在多镜头场景。

#### 游戏画布 {#game-canvas}

```js
scene.input.on(
  "gameout",
  function (timeStamp, event) {
    /* ... */
  },
  scope
);
scene.input.on(
  "gameover",
  function (timeStamp, event) {
    /* ... */
  },
  scope
);
```

### 拖动 {#dragging}

#### 启用拖曳 {#enable-dragging}

- [registering interactive](#enabling-a-game-object-for-input) 启用拖曳

  ```js
  gameObject.setInteractive({ draggable: true });
  ```

- 启用拖放, 并添加到已注册的交互式后拖放检测列表中

  ```js
  scene.input.setDraggable(gameObject);
  ```

- 启用拖曳

  ```js
  gameObject.input.draggable = true;
  ```

#### 禁用拖曳 {#disable-dragging}

- 从拖动检测列表中删除游戏对象

  ```js
  scene.input.setDraggable(gameObject, false);
  ```

- 禁用拖曳, 但保留在拖曳检测列表中

  ```js
  gameObject.input.draggable = false;
  ```

#### 拖拉事件 {#dragging-events}

```js
gameObject.on(
  "dragstart",
  function (pointer, dragX, dragY) {
    /* ... */
  },
  scope
);
gameObject.on(
  "drag",
  function (pointer, dragX, dragY) {
    /* ... */
  },
  scope
);
gameObject.on(
  "dragend",
  function (pointer, dragX, dragY, dropped) {
    /* ... */
  },
  scope
);
```

```js
scene.input.on(
  "dragstart",
  function (pointer, gameObject) {
    /* ... */
  },
  scope
);
scene.input.on(
  "drag",
  function (pointer, gameObject, dragX, dragY) {
    /* ... */
  },
  scope
);
scene.input.on(
  "dragend",
  function (pointer, gameObject, dropped) {
    /* ... */
  },
  scope
);
```

- `dropped` : `'dragend'` and also `'drop'`.

#### 拖动属性 {#dragging-properties}

```js
scene.input.dragDistanceThreshold = 16;
scene.input.dragTimeThreshold = 500;
```

### 投放区 {#drop-zone}

#### 启用投放区 {#enable-drop-zone}

- [registering interactive](#enabling-a-game-object-for-input) 启用投放

  ```js
  gameObject.setInteractive({ dropZone: true });
  ```

- 启用注册互动后丢弃

  ```js
  gameObject.input.dropZone = true;
  ```

#### 禁用投放区 {#disable-drop-zone}

```js
gameObject.input.dropZone = false;
```

#### 丢弃事件 {#dropping-events}

```js
gameObject.on(
  "drop",
  function (pointer, target) {
    /* ... */
  },
  scope
);

gameObject.on(
  "dragenter",
  function (pointer, target) {
    /* ... */
  },
  scope
);
gameObject.on(
  "dragover",
  function (pointer, target) {
    /* ... */
  },
  scope
);
gameObject.on(
  "dragleave",
  function (pointer, target) {
    /* ... */
  },
  scope
);
```

```js
scene.input.on(
  "drop",
  function (pointer, gameObject, target) {
    /* ... */
  },
  scope
);

scene.input.on(
  "dragenter",
  function (pointer, gameObject, target) {
    /* ... */
  },
  scope
);
scene.input.on(
  "dragover",
  function (pointer, gameObject, target) {
    /* ... */
  },
  scope
);
scene.input.on(
  "dragleave",
  function (pointer, gameObject, target) {
    /* ... */
  },
  scope
);
```

### 第一次事件 {#first-event-of-all}

```js
scene.input.on(
  "preupdate",
  function () {
    /* ... */
  },
  scope
);
```

### 单次触摸 {#single-touch}

#### 指针 {#pointer}

```js
var pointer = scene.input.activePointer;
```

### 多触摸 {#multi-touch}

#### 有效指针数量 {#amount-of-active-pointers}

游戏配置中设定活动指针的数量

```js
var config = {
  // ...
  input: {
    activePointers: 1,
    // ...
  },
};
var game = new Phaser.Game(config);
```

或于运行时加指针.

```js
scene.input.addPointer(num); // total points = num + 1
```

#### 指针 {#pointers}

- pointer 1 ~ 10

  ```js
  var pointer = scene.input.pointer1;
  // ...
  var pointer = scene.input.pointer10;
  ```

- 指针n

  ```js
  var pointer = scene.input.manager.pointers[n];
  ```

- 指针总数

  ```js
  var amount = scene.input.manager.pointersTotal;
  ```

  - 桌面中的 `1` 键
  - `2`在触摸设备中。 (鼠标`0`, 1 触摸指针`1`)

### 指针 {#pointer-1}

- Position
  - 当前的触摸
    - 屏幕位置: `pointer.x`, `pointer.y`
    - 处于不公开位置 :
      - 单摄像机 :
        ```js
        var worldX = pointer.worldX;
        var worldY = pointer.worldY;
        ```
      - 多摄像机 :
        ```js
        var worldXY = pointer.positionToCamera(camera); // worldXY: {x, y}
        // var worldXY = pointer.positionToCamera(camera, worldXY);
        var worldX = worldXY.x;
        var worldY = worldXY.y;
        ```
      - 摄像机
        ```js
        var camera = pointer.camera;
        ```
    - 上一个移动的位置 : `pointer.prevPosition.x` , `pointer.prevPosition.y`
      - 指向下, 指向上, 指向上, 更新时更新 。
    - 内插位置 :
      ```js
      var points = pointer.getInterpolatedPosition(step);
      // var out = pointer.getInterpolatedPosition(step, out);
      ```
  - Drag
    - 触摸开始:`pointer.downX`,`pointer.downY`
    - 触角: `pointer.upX`, `pointer.upY`
    - 将指针下拉到最近指针之间的距离 : `pointer.getDistance()`
      - 水平拖曳距离 : `pointer.getDistanceX()`
      - 垂直拖曳距离 : `pointer.getDistanceY()`
    - 拖曳角度 : `pointer.getAngle()`
- Time
  - 触摸开始: `pointer.downTime`
  - 触摸端: `pointer.upTime`
  - 拖动: `pointer.getDuration()`
- 触摸状态
  - 触摸/任何按钮下方: `pointer.isDown`
  - 首键下方: `pointer.primaryDown`
- 按钮状态: `pointer.button`
  - 在触摸设备上,值总是`0`.
- 扣上按钮
  - 没有按钮下: `pointer.noButtonDown()`
  - 首键( 左) 下方 : `pointer.leftButtonDown()`
  - 二级( 右) 按钮下方 : `pointer.rightButtonDown()`
  - 中间( mouse 轮子) 按钮下方 : `pointer.middleButtonDown()`
  - 后键下方: `pointer.backButtonDown()`
  - 向下按键 : `pointer.forwardButtonDown()`
- 释放按钮
  - 是否发布了主( 左) 按钮 : `pointer.leftButtonReleased()`
  - 二级( 右) 按钮已发布 : `pointer.rightButtonReleased()`
  - 中间( mouse 轮子) 按钮已发布 : `pointer.middleButtonReleased()`
  - 后键已发布 : `pointer.backButtonReleased()`
  - 已发布前置按钮 : `pointer.forwardButtonReleased()`
- 以`scene.input.manager.pointers`表示的索引: `pointer.id`
- Motion
  - 角度: `pointer.angle`
  - 距离: `pointer.distance`
  - 速度: `pointer.velocity`
    - `pointer.velocity.x`, ``pointer.velocity.y`

### 输入对象 {#input-object}

- `gameObject.input`:游戏对象的输入对象.
- `gameObject.input.localX`,`gameObject.input.localY`:指向局部的纹理位置.
- `gameObject.input.dragStartX`, `gameObject.input.dragStartY`:游戏对象的x/y坐标
  当拖曳开始时,该对象拥有此交互对象。
- `gameObject.input.dragStartXGlobal`, `gameObject.input.dragStartYGlobal` : x/y 坐标
  指针开始拖曳此交互式对象 。
- `gameObject.input.dragX`, `gameObject.input.dragY` : x/y 坐标为此交互式对象
  正在拖动。

### 平滑 {#smooth}

从先前触摸位置和当前触摸位置的插值中获取触摸位置.

```
Touch-position = (current-touch-position * smooth-factor) + (previous-touch-position * (1 - smooth-factor))
```

1. 设置平滑因子。 在 [game configuration](/guide/concepts/scenes#game-configuration) 中

   ```js
   var config = {
     // ....
     input: {
       smoothFactor: 0,
     },
   };
   ```

1. 获取触摸位置

   ```js
   var x = pointer.x;
   var y = pointer.y;
   var worldX = pointer.worldX;
   var worldY = pointer.worldY;
   ```

### 调试 {#debug}

- 启用, 绘制( 形状) 命中区域的形状 。

  ```js
  scene.input.enableDebug(gameObject);
  // scene.input.enableDebug(gameObject, color);
  ```

- Disable

  ```js
  scene.input.removeDebug(gameObject);
  ```

- 获取调试形状游戏对象

  ```js
  var shape = gameObject.input.hitAreaDebug;
  ```

### 保费 {#poll-rate}

- 触摸移动时进行投票,或更新,默认行为。

  ```js
  scene.input.setPollOnMove();
  ```

- 每一次打一通电话

  ```js
  scene.input.setPollAlways();
  ```

- 设定民调率.

  ```js
  scene.input.setPollRate(rate);
  ```

## 触摸/ 鼠标输入 {#touch-mouse-input}

!!! note
在预装阶段没有启动触摸输入事件 。

### 用法 {#usage}

- 正在按下触摸/ 鼠标按钮。 通常在 `update()` 游戏循环中使用 :

  ```js
  var pointer = scene.input.activePointer;
  if (pointer.isDown) {
    var touchX = pointer.x;
    var touchY = pointer.y;
    // ...
  }
  ```

- 任何触摸开始/ 鼠标按钮的按键事件 :

  ```js
  scene.input.on(
    "pointerdown",
    function (pointer) {
      var touchX = pointer.x;
      var touchY = pointer.y;
      // ...
    },
    scope
  );
  ```

- 在任何触摸端/ 鼠标按钮放出事件上 :

  ```js
  scene.input.on(
    "pointerup",
    function (pointer) {
      var touchX = pointer.x;
      var touchY = pointer.y;
      // ...
    },
    scope
  );
  ```

- 在触摸游戏对象开始/ 鼠标按钮按键时按下事件 :

  ```js
  gameObject.setInteractive().on(
    "pointerdown",
    function (pointer, localX, localY, event) {
      // ...
    },
    scope
  );
  ```

- 在触摸游戏对象端/ 鼠标按钮发布事件上 :

  ```js
  gameObject.setInteractive().on(
    "pointerup",
    function (pointer, localX, localY, event) {
      // ...
    },
    scope
  );
  ```

- 拖动游戏对象 :

  ```js
  gameObject
      .setInteractive({ draggable: true })
      .on('dragstart', function(pointer, dragX, dragY){
          // ...
      }, scope);
      .on('drag', function(pointer, dragX, dragY){
          gameObject.setPosition(dragX, dragY);
      }, scope);
      .on('dragend', function(pointer, dragX, dragY, dropped){
          // ...
      }, scope);
  ```

参考:[Properties of point](/guide/concepts/geometry#point)

### 光标 {#cursor}

### 用法 {#usage-1}

References:

- [Cursor](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor)

### 设置默认光标 {#set-default-cursor}

```js
scene.input.setDefaultCursor(CSSString);
// CSSString: 'url(assets/input/cursors/sword.cur), pointer'
```

### 设定游戏对象的光标 {#set-cursor-of-a-game-object}

光标超过该游戏对象时更改光标图像 。

```js
gameObject.setInteractive({
  cursor: CSSString,
});
// CSSString: 'url(assets/input/cursors/sword.cur), pointer'
```

直接在 `gameObject.setInteractive()` 之后设置光标图像 。

```js
gameObject.input.cursor = CSSString;
// CSSString: 'url(assets/input/cursors/sword.cur), pointer'
```

使用指针(手游标).

```js
gameObject.setInteractive({
  useHandCursor: true,
});
```

### 更改当前光标 {#change-current-cursor}

```js
scene.input.manager.canvas.style.cursor = cursor;
```

- `cursor` : CSSSTring 键盘

## 键盘输入 {#keyboard-input}

### 快速开始 {#quick-start}

- 键盘下/ 是键盘上

  ```js
  var keyObject = scene.input.keyboard.addKey("W"); // Get key object
  var isDown = keyObject.isDown;
  var isUp = keyObject.isUp;
  var shiftKey = keyObject.shiftKey;
  ```

- 钥匙在一段时间后会下调

  ```js
  var keyObject = scene.input.keyboard.addKey("W"); // Get key object
  var isDown = scene.input.keyboard.checkDown(keyObject, duration);
  ```

- 键盘下/键盘上

  ```js
  var keyObject = scene.input.keyboard.addKey("W"); // Get key object
  keyObject.on("down", function (event) {
    /* ... */
  });
  keyObject.on("up", function (event) {
    /* ... */
  });
  ```

  or

  ```js
  scene.input.keyboard.on("keydown-" + "W", function (event) {
    /* ... */
  });
  scene.input.keyboard.on("keyup-" + "W", function (event) {
    /* ... */
  });
  ```

- 任何按键下/ 任何按键上下

  ```js
  scene.input.keyboard.on("keydown", function (event) {
    /* ... */
  });
  scene.input.keyboard.on("keyup", function (event) {
    /* ... */
  });
  ```

  - `event` : [KeyboardEvent](https://www.w3schools.com/jsref/obj_keyboardevent.asp)
    - `event.code`:"键"+"W"

### 密钥对象 {#key-object}

- 获取键对象

  ```js
  var keyObject = scene.input.keyboard.addKey("W"); // see `Key map` section
  // var keyObject = scene.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.W);
  ```

  or

  ```js
  var keyObject = scene.input.keyboard.addKey("W", enableCapture, emitOnRepeat);
  ```

  - `enableCapture`:在本地DOM浏览器事件上自动调用`preventDefault`,用于添加键代码.
  - `emitOnRepeat` : 控件在被扣下时是否会连续发出一个"下"事件(真),或者只发出一次事件(假,默认).

- 获取键对象

  ```js
  var keyObjects = scene.input.keyboard.addKeys("W,S,A,D"); // keyObjects.W, keyObjects.S, keyObjects.A, keyObjects.D
  // var keyObjects = scene.input.keyboard.addKeys('W,S,A,D', enableCapture, emitOnRepeat);
  ```

  or

  ```js
  var keyObjects = scene.input.keyboard.addKeys({
    up: "W",
    down: "S",
    left: "A",
    right: "D",
  }); // keyObjects.up, keyObjects.down, keyObjects.left, keyObjects.right
  ```

- 删除键对象

  ```js
  scene.input.keyboard.removeKey("W");
  // scene.input.keyboard.removeKey(Phaser.Input.Keyboard.KeyCodes.W);
  // scene.input.keyboard.removeKey(key, destroy, removeCapture);
  ```

  - `destroy`: 在每个已删除的键对象上调用 `Key.destroy`
  - `removeCapture` : 删除此插件欠下的键对象的全部键抓取吗 ?

- 删除全部键对象

  ```js
  scene.input.keyboard.removeAllKeys(true);
  // scene.input.keyboard.removeAllKeys(destroy, removeCapture);
  ```

  - `destroy`: 在每个已删除的键对象上调用 `Key.destroy`
  - `removeCapture` : 删除此插件欠下的键对象的全部键抓取吗 ?

- 键下/键上状态

  ```js
  var isDown = keyObject.isDown;
  var isUp = keyObject.isUp;
  ```

- 扣值持续时间

  ```js
  var duration = keyObject.getDuration(); // ms
  ```

- 启用/ 禁用

  ```js
  keyObject.enabled = enabled; // Set false to disable key event
  ```

### 光标键的密钥对象 {#key-object-of-cursorkeys}

1. 获取键状态对象

   ```js
   var cursorKeys = scene.input.keyboard.createCursorKeys();
   ```

1. 获取键状态

   ```js
   var isUpDown = cursorKeys.up.isDown;
   var isDownDown = cursorKeys.down.isDown;
   var isLeftDown = cursorKeys.left.isDown;
   var isRightDown = cursorKeys.right.isDown;
   var isSpaceDown = cursorKeys.space.isDown;
   var isShiftDown = cursorKeys.shift.isDown;
   ```

### 关键下/关键上的活动顺序 {#order-of-key-downkey-up-events}

1. 关键对象的按键下/按键事件

   ```js
   var keyObject = scene.input.keyboard.addKey("W"); // Get key object
   keyObject.on("down", function (event) {
     /* ... */
   });
   keyObject.on("up", function (event) {
     /* ... */
   });
   ```

   - `event.stopImmediatePropagation()`: 停止在目前场景中引用任何进一步的监听器.
   - `event.stopPropagation()` 停止它到达任何其它场景。

1. 键盘下/键盘上

   ```js
   scene.input.keyboard.on("keydown-" + "W", function (event) {
     /* ... */
   });
   scene.input.keyboard.on("keyup-" + "W", function (event) {
     /* ... */
   });
   ```

   - `event.stopImmediatePropagation()`: 停止在目前场景中引用任何进一步的监听器.
   - `event.stopPropagation()` 停止它到达任何其它场景。
   - 启动`event.preventDefault()`停止向本地DOM传播事件.

1. 任何按键下/按键上

   ```js
   scene.input.keyboard.on("keydown", function (event) {
     /* ... */
   });
   scene.input.keyboard.on("keyup", function (event) {
     /* ... */
   });
   ```

   - `event.key` : `'a'`
   - `event.keyCode` : `65`
   - `event.code` : `'KeyA'`
   - `event.stopImmediatePropagation()`: 停止在目前场景中引用任何进一步的监听器.
   - `event.stopPropagation()` 停止它到达任何其它场景。

### 销毁密钥对象 {#destroy-key-object}

```js
keyObject.destroy();
```

### 关键地图 {#key-map}

- `A` ~ `Z`
- `F1` ~ `F12`
- `BACKSPACE`
- `TAB`
- `ENTER`
- `SHIFT`
- `CTRL`. `ALT`
- `PAUSE`
- `CAPS_LOCK`
- `ESC`
- `SPACE`
- `PAGE_UP`, `PAGE_DOWN`
- `END`, `HOME`
- `LEFT`, `UP`, `RIGHT`,`DOWN`
- `PRINT_SCREEN`
- `INSERT`, `DELETE`
- `ZERO`, `ONE`, `TWO`, `THREE`, `FOUR`, `FIVE`, `SIX`, `SEVEN`, `EIGHT`, `NINE`
- `NUMPAD_ZERO`, `NUMPAD_ONE`, `NUMPAD_TWO`, `NUMPAD_THREE`, `NUMPAD_FOUR`, `NUMPAD_FIVE`, `NUMPAD_SIX`, `NUMPAD_SEVEN`, `NUMPAD_EIGHT`, `NUMPAD_NINE`, `NUMPAD_ADD`, `NUMPAD_SUBTRACT`
- `OPEN_BRACKET`, `CLOSED_BRACKET`
- `SEMICOLON_FIREFOX`, `COLON`, `COMMA_FIREFOX_WINDOWS`, `COMMA_FIREFOX`, `BRACKET_RIGHT_FIREFOX`, `BRACKET_LEFT_FIREFOX`

### 键盘组合 {#keyboard-combos}

1. 创建组合

   ```js
   var keyCombo = scene.input.keyboard.createCombo(keys, {
     // resetOnWrongKey: true,
     // maxKeyDelay: 0,
     // resetOnMatch: false,
     // deleteOnMatch: false,
   });
   ```

   - `keys`: 一组keyCodes
     - 弦乐,例如:`['up', 'up', 'down', 'down']`,或`['UP', 'UP', 'DOWN', 'DOWN']`
     - 以[key map](#key-map)表示,例如:`[Phaser.Input.Keyboard.KeyCodes.UP, ... ]`
     - 数字,例如:`[38, 38, 40, 40]`
   - `resetOnWrongKey` 设置 `true` 以重置组合键,但按错键时。
   - `maxKeyDelay`: 每个键按键之间的最大延迟。 设置 `0` 以禁用此特性 。
   - `resetOnMatch`:设置`true`,用于在之前匹配时重置组合.
   - `deleteOnMatch` 设置 `true` 以匹配时删除此组合。

2. 听齐比对事件

   ```js
   scene.input.keyboard.on("keycombomatch", function (keyCombo, keyboardEvent) {
     /* ... */
   });
   ```

## 游戏板输入 {#gamepad-input}

### 启用游戏板管理器 {#enable-gamepad-manager}

```js
var config = {
  // ...
  input: {
    gamepad: true,
  },
  // ...
};
var game = new Phaser.Game(config);
```

### 获取游戏板 {#get-gamepad}

- 获取当前连接的 Gamepads 。

  ```js
  var gamepads = scene.input.gamepad.getAll();
  ```

- 按索引获取游戏板

  ```js
  var gamepad = scene.input.gamepad.getPad(0);
  // var gamepad = scene.input.gamepad.getPad(index);
  ```

- 按钮时得到游戏板。

  ```js
  scene.input.gamepad.once('down', function (gamepad, button, value) {
  }
  ```

  - `gamepad`: 显示该按钮的 Gamepad 的参考。 请参看 [Properties of gamepad](#properties)
  - `button`: 引用了已发布的按钮.
  - `value`: 发布时按钮的值, 0 至 1 之间,有些 Gamepad 具有对压力敏感的按钮.

### 事件 {#events}

- 扣上按钮

  ```js
  scene.input.gamepad.on("down", function (gamepad, button, value) {});
  ```

  or

  ```js
  gamepad.on("down", function (buttonIndex, value, button) {});
  ```

- 按钮

  ```js
  scene.input.gamepad.on('up', function (gamepad, button, value) {
  }
  ```

  or

  ```js
  gamepad.on("up", function (buttonIndex, value, button) {});
  ```

- 游戏板已连接

  ```js
  scene.input.gamepad.on('connected', function (gamepad, event) {
  }
  ```

- 游戏板断开

  ```js
  scene.input.gamepad.on('disconnected', function (gamepad, event) {
  }
  ```

### 游戏盘 {#gamepad}

#### 按钮 {#buttons}

- 光标按钮

  ```js
  var isLeftDown = gamepad.left;
  var isRightftDown = gamepad.right;
  var isUpDown = gamepad.up;
  var isDownDown = gamepad.down;
  ```

- 右键集群

  ```js
  var isADown = gamepad.A; // Dual Shock controller: X button
  var isYDown = gamepad.Y; // Dual Shock controller: Triangle button
  var isXDown = gamepad.X; // Dual Shock controller: Square button.
  var isBDown = gamepad.B; // Dual Shock controller: Circle button
  ```

- 肩部按钮

  ```js
  var isL1Down = gamepad.L1; // XBox controller: LB button
  var isL2Down = gamepad.L2; // XBox controller: LT button
  var isR1Down = gamepad.R1; // XBox controller: RB button
  var isR2Down = gamepad.R2; // XBox controller: RT button
  ```

#### 轴线 {#axis-sticks}

- 左棍,右棍,右棍,左棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右棍,右,右棍,右棍,右棍,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右棒,右,右棒,右棒,右棒,右,右,右棒,右,右,右,右,右,右,右,右,右,右,右,右棒,右棒,右,右棒,右,右,右,右,右,右,右,右,右,右棒,右,右棒,右,右,右,右,右,右,右,右,右,右,右,右,右,

  ```js
  var leftStick = gamepad.leftStick;
  var rightStick = gamepad.rightStick;
  ```

  - `leftStick`, `rightStick` : 只读 [vector2](/guide/concepts/math#vector).
    - 角度: `leftStick.angle()`
    - 长度: `leftStick.length()`
    - x, y : (中文(简体) ). `leftStick.x` , `leftStick.y`

#### 属性 {#properties}

- `gamepad.index`:目前与系统相连的每个Gamepad独有的整数.
  这可用于区分多个控制器.
  注意连接设备然后连接新设备可能会重用以前的索引 。
- `gamepad.id`:包含一些控制器信息的字符串.
- `gamepad.buttons`:一组Gamepad按钮对象,对应Gamepad上可用的不同按钮.
- `gamepad.axes`:一组Gamepad轴对象,对应Gamepad上可用的不同轴,如果有的话.

## 鼠标轮键输入 {#mouse-wheel-input}

### 鼠标轮事件 {#mouse-wheel-events}

1. 触摸游戏对象的事件

   ```js
   gameObject.on("wheel", function (pointer, dx, dy, dz, event) {
     /* ... */
   });
   ```

1. 在每个触摸的游戏对象的输入插件上的事件

   ```js
   scene.input.on(
     "gameobjectwheel",
     function (pointer, gameObject, dx, dy, dz, event) {
       /* ... */
     }
   );
   ```

1. 获取 ** ** 全部** 被触摸的游戏对象的事件

   ```js
   scene.input.on(
     "wheel",
     function (pointer, currentlyOver, dx, dy, dz, event) {
       /* ... */
     }
   );
   ```

### 鼠标轮子属性 {#mouse-wheel-properties}

- `pointer.deltaX`:由于用户移动鼠标轮或类似的输入设备而发生的水平滚动量.
- `pointer.deltaY`:由于用户移动鼠标轮或类似的输入设备而发生的垂直滚动量.
- `pointer.deltaZ`:由于用户移动鼠标轮或类似的输入设备而发生的z轴滚动量.

## 禁用所有输入事件 {#disable-all-input-events}

要启用/ 禁用输入事件 :

```js
scene.input.enabled = enabled; // enabled: true/false
```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
