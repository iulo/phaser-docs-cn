# Matter 物理 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/physics/matter)

物质物理是一个开源第三方物理库,Phaser有它自己的自定义版本捆绑。 加入物质的理由是它提供了一个更先进的“ 完整的” 物理系统。 如果您需要超越矩形和圆形, 物理形状更复杂, 以及约束、 关节和行为等特征, 那么物质就是要使用的系统 。

物质物理必须启用后才能使用。 可以通过游戏配置或每场游戏完成。 一旦启用, 您可以在游戏中添加物理化的游戏对象。 这将允许您使用内置物理函数来控制 Sprite, 如速度、 加速、 重力等 。

默认情况下, 无法为物理启用游戏对象。 这是因为并非所有游戏对象都需要。 例如, 背景图像或游戏标志可能不需要受到物理影响, 而玩家字符需要。 因此, 您必须启用您特别希望受其影响的游戏对象上的物理。 我们将在后面章节中详细论述这个问题 。

弧形物理和物质物理是两个独立的系统。例如,弧形物理图案不能与物质物理图案相撞。不能在两个系统上添加相同的Sprite,你需要选择一个或另一个。尽管这样做是不寻常的,但这两个系统实际上可以在同一场景中平行运行。这意味着可以有一个使用Arcade物理的Sprite和一个使用物质物理的Sprite,它们将同时工作,尽管它们不会一起互动。

## 物质世界 {#matter-world}

物质物理学世界提供了比Arcade物理更先进和更现实的物理相互作用模拟。 它在 Matter.js 库上建构了这样的模拟,它允许更复杂的物理行为,如刚性的身体动力学、约束和高级碰撞探测。

### 世界组合 {#world-configuration}

物质物理`config`对象定义了物质物理系统在全球的行为.

- 基本配置对象

```js
const config = {
  // ...
  physics: {
    default: "matter",
  },
  // ...
};

const game = new Phaser.Game(config);
```

- 完整配置

```js
var config = {
  // ...
  physics: {
    default: "matter",
    matter: {
      //    enabled: true,
      //    positionIterations: 6,
      //    velocityIterations: 4,
      //    constraintIterations: 2,
      //    enableSleeping: false,
      //    plugins: {
      //        attractors: false,
      //        wrap: false,
      //    },
      //    gravity: {
      //        x: 0,
      //        y: 0,
      //    }
      //    setBounds: {
      //        x: 0,
      //        y: 0,
      //        width: scene.sys.scale.width,
      //        height: scene.sys.scale.height,
      //        thickness: 64,
      //        left: true,
      //        right: true,
      //        top: true,
      //        bottom: true,
      //    },
      //    timing: {
      //        timestamp: 0,
      //        timeScale: 1,
      //    },
      //    correction: 1,
      //    getDelta: (function() { return 1000 / 60; }),
      //    autoUpdate: true,
      //    debug: false,
      //    debug: {
      //        showAxes: false,
      //        showAngleIndicator: false,
      //        angleColor: 0xe81153,
      //        showBroadphase: false,
      //        broadphaseColor: 0xffb400,
      //        showBounds: false,
      //        boundsColor: 0xffffff,
      //        showVelocity: false,
      //        velocityColor: 0x00aeef,
      //        showCollisions: false,
      //        collisionColor: 0xf5950c,
      //        showSeparations: false,
      //        separationColor: 0xffa500,
      //        showBody: true,
      //        showStaticBody: true,
      //        showInternalEdges: false,
      //        renderFill: false,
      //        renderLine: true,
      //        fillColor: 0x106909,
      //        fillOpacity: 1,
      //        lineColor: 0x28de19,
      //        lineOpacity: 1,
      //        lineThickness: 1,
      //        staticFillColor: 0x0d177b,
      //        staticLineColor: 0x1327e4,
      //        showSleeping: false,
      //        staticBodySleepOpacity: 0.7,
      //        sleepFillColor: 0x464646,
      //        sleepLineColor: 0x999a99,
      //        showSensors: true,
      //        sensorFillColor: 0x0d177b,
      //        sensorLineColor: 0x1327e4,
      //        showPositions: true,
      //        positionSize: 4,
      //        positionColor: 0xe042da,
      //        showJoint: true,
      //        jointColor: 0xe0e042,
      //        jointLineOpacity: 1,
      //        jointLineThickness: 2,
      //        pinSize: 4,
      //        pinColor: 0x42e0e0,
      //        springColor: 0xe042e0,
      //        anchorColor: 0xefefef,
      //        anchorSize: 4,
      //        showConvexHulls: false,
      //        hullColor: 0xd703d0
      //    }
    },
  },
  // ...
};
var game = new Phaser.Game(config);
```

### 控制器 {#control}

#### 暂停 {#pause}

```js
this.matter.world.pause();
```

#### 继续 {#resume}

```js
this.matter.world.resume();
```

#### 拖动对象 {#drag-object}

```js
this.matter.add.mouseSpring();
// this.matter.add.mouseSpring(options);
```

- `options`

  ```js
  {
      length: 0.01,
      stiffness: 0.1,
      damping: 0,
      angularStiffness: 1,
      collisionFilter: {
          category: 0x0001,
          mask: 0xFFFFFFFF,
          group: 0
      }
  }
  ```

  - `collisionFilter` : 拖动过滤器,参见 [collision](#game-object-collision).

### 世界界限 {#world-bounds}

#### 启用 {#enable}

- World :

  - 设定界限

        ```js
        this.matter.world.setBounds(x, y, width, height);
        // this.matter.world.setBounds(x, y, width, height, thickness, left, right, top, bottom);
        ```

    - `thickness` :每面壁的厚度,以像素为单位.
    - `left`,`right`,`top`,`bottom`:如果真能创建左/右/上/下界壁.

### 重力 {#gravity}

- Set

  ```js
  this.matter.world.setGravity(x, y);
  // this.matter.world.setGravity(x, y, scale);
  ```

- Disable

  ```js
  this.matter.world.disableGravity();
  ```

### 约束 {#constraint}

#### 约束两个游戏对象 {#constraint-of-2-game-objects}

```js
var constraint = this.matter.add.constraint(gameObjectA, gameObjectB);
// var constraint = this.matter.add.constraint(gameObjectA, gameObjectB, length, stiffness, options);
```

- `gameObjectA`,`gameObjectB`:物质游戏对象,或物质身体对象.
- `length` : 约束的剩余目标长度。
  - `undefined`:当前gameObjectA和gameObjectB之间的距离。 (默认值)
- `stiffness` : 约束的僵硬性.
  - `1` : 非常僵硬。 (默认值)
  - `0.2` :扮演柔软的弹簧.
- `options` :

  ```js
  {
      pointA: {
          x: 0,
          y: 0,
      },
      pointB: {
          x: 0,
          y: 0,
      },
      damping: 0,
      angularStiffness: 0,
      // render: {
      //     visible: true
      // }
  }
  ```

  - `pointA`, `pointB` : 偏移位置( 单位:千米) `gameObjectA`, `gameObjectB`.

Alias:

```js
var constraint = this.matter.add.spring(
  gameObjectA,
  gameObjectB,
  length,
  stiffness,
  options
);
var constraint = this.matter.add.joint(
  gameObjectA,
  gameObjectB,
  length,
  stiffness,
  options
);
```

#### 限制在世界位置上 {#constraint-to-world-position}

```js
var constraint = this.matter.add.worldConstraint(
  gameObjectB,
  length,
  stiffness,
  options
);
```

- `gameObjectB` :物质游戏对象,或物质体对象.
- `length` : 约束的剩余目标长度。
  - `undefined`:当前gameObjectA和gameObjectB之间的距离。 (默认值)
- `stiffness` : 约束的僵硬性.
  - `1` : 非常僵硬。 (默认值)
  - `0.2` :扮演柔软的弹簧.
- `options` :

  ```js
  {
      pointA: {
          x: 0,
          y: 0,
      },
      pointB: {
          x: 0,
          y: 0,
      },
      damping: 0,
      angularStiffness: 0,
      // render: {
      //     visible: true
      // }
  }
  ```

  - `pointA` : 世界立场.
  - `pointB` : 偏移位置( 单位:千米) `gameObjectB`.

#### 链式游戏对象 {#chain-game-objects}

```js
var composite = this.matter.add.chain(
  composite,
  xOffsetA,
  yOffsetA,
  xOffsetB,
  yOffsetB,
  options
);
```

- `composite` : [Image composite](#image-composite)
- `xOffsetA`, `yOffsetA` : 偏移位置( 单位:千米) gameObjectA,在比例上。
  - xOffset = (离相/宽)
  - yOffset = (偏差/ 高度)
- `xOffsetB`, `yOffsetB` : 偏移位置( 单位:千米) gameObjectB,在比例上。
- `options` :

  ```js
  {
      length: undefined,
      stiffness: 1,
      damping: 0,
      angularStiffness: 0,
      // render: {
      //     visible: true
      // }
  }
  ```

  - `length` : 约束的剩余目标长度。
    - `undefined`:当前gameObjectA和gameObjectB之间的距离。 (默认值)
  - `stiffness` : 约束的僵硬性.
    - `1` : 非常僵硬。 (默认值)
    - `0.2` :扮演柔软的弹簧.

- `composite`
  - `composite.bodies` : 一系列身体。
  - `composite.constraints`:一系列制约因素

#### 删除约束 {#remove-constraint}

```js
this.matter.world.removeConstraint(constraint);
```

## 物质游戏对象 {#matter-game-object}

游戏对象是您的游戏的构件。常见的物质游戏对象包括:Sprites, Images和TileBody 。

### 使用量 {#usage}

#### 添加游戏对象 {#add-game-objects}

[Enable physics world](#world-configuration).

##### 图像对象 {#image-object}

```js
var image = this.matter.add.image(x, y, key, frame);
// var image = this.matter.add.image(x, y, key, frame, config);
```

- `config` : [Config object](#game-object-configuration)

##### 闪烁对象 {#sprite-object}

```js
var image = this.matter.add.sprite(x, y, key, frame);
// var image = this.matter.add.sprite(x, y, key, frame, config);
```

- `config` : [Config object](#game-object-configuration)

##### 任意游戏对象 {#any-game-object}

```js
var gameObject = this.matter.add.gameObject(gameObject);
// var gameObject = this.matter.add.gameObject(gameObject, config);
```

- `config` : [Config object](#game-object-configuration)

##### 图像复合材料 {#image-composite}

创建包含在网格安排中创建的 Matter Image 对象的新复合材料 。

```js
var composite = this.matter.add.imageStack(key, frame, x, y, columns, rows);
// var composite = this.matter.add.imageStack(key, frame, x, y, columns, rows, columnGap, rowGap, options);
```

- `key`,`frame`:纹理键和帧名称.
- `x`, `y` :这些游戏对象的左上方位置.
- `columns`, `rows` : 网格中的列/行数.
- `columnGap`, `rowGap` : 每个列/行之间的距离。
- `config` : [Config object](#game-object-configuration)
- `composite` : 复合物质对象。
  - `composite.bodies` : 一系列身体。

##### 游戏对象配置 {#game-object-configuration}

```js
{
    label: 'Body',
    shape: 'rectangle',
    chamfer: null,

    isStatic: false,
    isSensor: false,
    isSleeping: false,
    ignoreGravity: false,
    ignorePointer: false,

    sleepThreshold: 60,
    density: 0.001,
    restitution: 0,
    friction: 0.1,
    frictionStatic: 0.5,
    frictionAir: 0.01,

    force: { x: 0, y: 0 },
    angle: 0,
    torque: 0,

    collisionFilter: {
        group: 0,
        category: 0x0001,
        mask: 0xFFFFFFFF,
    },

    // parts: [],

    // plugin: {
    //     attractors: [
    //         (function(bodyA, bodyB) { return {x, y}}),
    //     ]
    // },

    slop: 0.05,

    timeScale: 1,
}
```

- `label`:一个任意的`String`名称,帮助用户识别和管理尸体.
- `shape` :

  - 字符串 : `'rectangle'`, `'circle'`, `'trapezoid'`, `'polygon'`, `'fromVertices'`, `'fromPhysicsEditor'`
  - 对象 :

    - 矩形形状

            ```js
            {
                type: 'rectangle',
                // width: gameObject.width
                // height: gameObject.height
            }
            ```

    - 圆形

            ```js
            {
                type: 'circle',
                // radius: (Math.max(gameObject.width, gameObject.height) / 2),
                // maxSides: 25
            }
            ```

    - 拖动形状

            ```js
            {
                type: 'trapezoid',
                // slope: 0.5,
            }
            ```

    - 多边形形状

            ```js
            {
                type: 'polygon',
                // radius: (Math.max(gameObject.width, gameObject.height) / 2),
                // sides: 5,
            }
            ```

    - Vertices

            ```js
            {
                type: 'fromVertices',
                verts: points,
                // flagInternal: false,
                // removeCollinear: 0.01,
                // minimumArea: 10,
            }
            ```

      - `points` :
        - 字符串: `'x0 y0 x1 y1 ...'`
        - 数组点数 : `[{x:x0, y:y0}, {x:x1, y:y1}, ...]`

- `chamfer` :
  - `null`
  - 数字
  - `{radius: value}`
  - `{radius: [topLeft, topRight, bottomRight, bottomLeft]}`
- `isStatic` : 表示一个身体是否被视为静止的旗帜,一个静止的身体永远不能改变位置或角度,并且是完全固定的.
- `isSensor`:指向身体是否是传感器的旗帜,传感器触发碰撞事件,但不会与碰撞身体发生物理反应.
- `isSleeping`:表示身体是否被视为睡眠的旗帜,睡眠的身体行为类似于静态的身体,但只是暂时的,可以震动.
- `sleepThreshold`:在设定为睡眠前,这个身体必须拥有_近零速度_的更新数量.
- `density` : 身体密度,即单位面积的质量。
- `restitution`: 身体的还原/弹跳/弹性。数值总是正值,在`(0, 1)`的范围之内。
  - `0` :碰撞可能完全没有弹性,并且不会发生波澜.
  - `0.8` :身体可能以大约80%的动能反弹.
- `friction` : 身体的滑动。 数值总是正值, 并且范围是 。 `(0, 1)`.
  - `0` :身体可能无限期滑动.
  - `1` : 施用武力后,尸体几乎会立即停机。
- `frictionStatic`:身体的静电摩擦(在库伦布摩擦模型中).
  - `0` :身体在接近静止状态时,只有动态状态时,就不会"棒" `friction` 用于使用。
  - `10`:值越高,在接近固定状态时,它会用更多的力量来让身体开始运动.
- `frictionAir` :身体的空气摩擦(空气阻力).
  - `0` :身体在太空中移动时永远不会减速.
  - 值越高,一个身体在穿越空间时速度越快.
- `force` : 适用于当前步骤的力。
- `angle` :身体角,以弧度表示.
- `torque`:当前步骤中应用的扭矩(转力).
- `collisionFilter`:一个指定了这个机体碰撞过滤特性的`Object`.
  - `collisionFilter.group`
  - `collisionFilter.category`: 指定此天体所属碰撞类别的位字段 。
  - `collisionFilter.mask`:一个指定了身体可能碰撞的碰撞类别的小遮罩.
- `slop` : 容忍一个身体被允许"沉入"或旋转到其它身体的距离.
  - 默认一般应足够,尽管非常大的体可能需要更大的值来进行稳定的堆叠.

###### 游戏对象碰撞 {#game-object-collision}

两个机构之间的碰撞将遵守以下规则:

- (grpupA > 0) && (groupB > 0) :
  - 碰撞=( 缩写)groupA == groupB)
- (grpupA == 0) || (groupB == 0) :
  - 碰撞=((()categoryA & maskB) !== 0) && ((categoryB & maskA) !== 0)

#### 移动 {#movement}

##### 速度 {#velocity}

```js
gameObject.setVelocity(x, y);
```

```js
gameObject.setVelocityX(x);
```

```js
gameObject.setVelocityY(x);
```

##### 加速 {#acceleration}

###### 强制 {#force}

- 将力量应用到身体上.

  ```js
  gameObject.applyForce(force);
  ```

  - `force` : `{x, y}`

- 从特定位置对身体施加力量.

  ```js
  gameObject.applyForceFrom(position, force); // position, force: {x, y}
  ```

  - `position` : `{x, y}`
  - `force` : `{x, y}`

- 将推力应用到身体的前进位置.

  ```js
  gameObject.thrust(speed);
  ```

  - `speed` : 一个数字。

- 将推力应用到身体的左侧位置.

  ```js
  gameObject.thrustLeft(speed);
  ```

  - `speed` : 一个数字。

- 将推力应用到身体的正确位置.

  ```js
  gameObject.thrustRight(speed);
  ```

  - `speed` : 一个数字。

- 将推力应用到身体的后方位置.

  ```js
  gameObject.thrustBack(speed);
  ```

  - `speed` : 一个数字。

- 将推力应用到身体的后方位置.

  ```js
  gameObject.thrustBack(speed);
  ```

  - `speed` : 一个数字。

###### 重力 {#gravity-1}

- 忽略世界引力

  ```js
  gameObject.setIgnoreGravity(ignore);
  ```

  - `ignore` : 设定为真实,以忽略世界引力的影响

###### 闪光灯 {#friction}

```js
gameObject.setFriction(value, air, fstatic);
```

```js
gameObject.setFrictionAir(v);
```

```js
gameObject.setFrictionStatic(v);
```

#### 旋转 {#rotation}

##### 固定轮换 {#fixed-rotation}

```js
gameObject.setFixedRotation();
```

##### 角速度 {#angular-velocity}

```js
gameObject.setAngularVelocity(v);
```

#### 碰撞 {#collision}

##### 启用 {#enable-1}

- Get

  ```js
  var isSensor = gameObject.isSensor();
  ```

- Set

  ```js
  gameObject.setSensor(value);
  ```

  - `value` 设置 `true` 以启用传感器。

##### 碰撞组 {#collision-group}

- 碰撞 grpup

  ```js
  gameObject.setCollisionGroup(value);
  ```

- 碰撞类别

  1. 获取新的碰撞类别

     ```js
     var category = this.matter.world.nextCategory();
     ```

     - `category` : 一发号码 `(1, 2, 4, 8, ...., 2147483648 (1<<31))`

  1. 设定游戏对象的碰撞类别

     ```js
     gameObject.setCollisionCategory(category);
     ```

  1. 设置分类掩码

     ```js
     gameObject.setCollidesWith([categoryA, categoryB, ...]);
     // gameObject.setCollidesWith(categoryA);
     ```

##### 碰撞事件 {#collision-event}

```js
this.matter.world.on("collisionstart", function (event, bodyA, bodyB) {
  // var pairs = event.pairs;
});
```

- `event` :
  - `event.pairs`: 一系列碰撞对
    - `event.pairs[i].bodyA`, `event.pairs[i].bodyB` :物质物体。
      - `body.gameObject` : 物质体的游戏对象.
- `bodyA`, `bodyB` : 等于 `event.pairs[0].bodyA`, `event.pairs[0].bodyB`.

##### 碰撞绑定 {#collision-bound}

- Rectangle

  ```js
  gameObject.setRectangle(width, height, options);
  ```

- Circle

  ```js
  gameObject.setCircle(radius, options);
  ```

- Polygon

  ```js
  gameObject.setPolygon(radius, sides, options);
  ```

- Trapezoid

  ```js
  gameObject.setTrapezoid(width, height, slope, options);
  ```

- Any

  ```js
  gameObject.setBody(config, options);
  ```

  - `config` :

    - 矩形形状

            ```js
            {
                type: 'rectangle',
                // width: gameObject.width
                // height: gameObject.height
            }
            ```

    - 圆形

            ```js
            {
                type: 'circle',
                // radius: (Math.max(gameObject.width, gameObject.height) / 2),
                // maxSides: 25
            }
            ```

    - 拖动形状

            ```js
            {
                type: 'trapezoid',
                // slope: 0.5,
            }
            ```

    - 多边形形状

            ```js
            {
                type: 'polygon',
                // radius: (Math.max(gameObject.width, gameObject.height) / 2),
                // sides: 5,
            }
            ```

##### 弹跳 {#bounce}

```js
gameObject.setBounce(v);
```

- restitution

#### 质量 {#mass}

```js
gameObject.setMass(v);
```

```js
gameObject.setDensity(v);
```

#### 睡觉 {#sleep}

##### 启用 {#enable-2}

```js
var config = {
  // ...
  physics: {
    matter: {
      // ...
      enableSleeping: true,
      // ...
    },
  },
};
```

##### 睡眠门槛 {#sleep-threshold}

```js
gameObject.setSleepThreshold(value);
```

##### 睡眠活动 {#sleep-events}

- 睡觉开始

  ```js
  this.matter.world.on("sleepstart", function (event, body) {});
  ```

- 沉睡的结束

  ```js
  this.matter.world.on("sleepend", function (event, body) {});
  ```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)
- [samme](https://github.com/samme)

---
