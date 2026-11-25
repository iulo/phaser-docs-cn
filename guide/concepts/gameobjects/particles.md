# 粒子 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/particles)

粒子 Emitter 是一类特殊类型的游戏对象,它控制着一组粒子.

粒子 Emitters 是通过配置对象创建的。 对象的属性可以多种格式指定, 相对于它们返回的值来说, 其范围很大, 导致复杂的视觉效果。 以下是您可以给出的不同形式的配置值 :

## 明确的静态值 : {#an-explicit-static-value}

```js
x: 400
```

当粒子产卵时,x值永远是400.

## 随机值 : {#a-random-value}

```js
x: [ 100, 200, 300, 400 ]
```

x 值将是给定阵列中随机选择的4个元素之一。

## 习惯回调 : {#a-custom-callback}

```js
x: (particle, key, t, value) => {
  return value + 50;
}
```

x值是调用此函数的结果。 仅在粒子被发射时才使用, 因此它提供了初始起始值。 当粒子被更新时不使用( 请参见 onUpdate 调用) 。

## 起始/ 结束对象 : {#a-start-end-object}

这使得您可以控制在粒子寿命过程中给定的起始参数和结束参数之间的值变化:

```js
scale: { start: 0, end: 1 }
```

当粒子尺度在寿命期内被排放并易于1的尺度时, 粒子尺度将从 0 开始。 您也可以指定用于此变化的易度函数( 默认为 Linear ):

```js
scale: { start: 0, end: 1, ease: 'bounce.out' }
```

## 起始/结束随机对象 : {#a-start-end-random-object}

起始和结尾对象可以有一个可选的 `random` 参数。这迫使它从两个值之间随机选择一个值,并将其作为起始值,然后在参数存在期间将其放松到“结束”参数。

```js
scale: { start: 4, end: 0.5, random: true }
```

粒子将先从0.5到4的随机尺度开始,然后在整个寿命期间缩放到最终值。您可以将以上参数与`ease`参数结合起来,从而控制值的放松。

## 插值对象 : {#an-interpolation-object}

您可以提供一系列在粒子寿命期间用于插值的数值。 您也可以定义要使用的插值函数。 提供了三种: `linear`( 默认值)、 `bezier`和 `catmull`, 或者您可以提供自己的函数 。

```js
x: { values: [ 50, 500, 200, 800 ], interpolation: 'catmull' }
```

粒子尺度在寿命期内通过其他点从50到800的射出时会插到800。您还可以指定一个通过值控制变化速率的易函数(默认为线性):

```js
x: { values: [ 50, 500, 200, 800 ], interpolation: 'catmull', ease: 'bounce.out }
```

## 已踩踏的发射对象 : {#a-stepped-emitter-object}

`steps`参数允许您控制顺序粒子在起始范围之间的位置:

```js
x: { steps: 32, start: 0, end: 576 }
```

这里有576个范围(开始到结束),分为32个步骤。

第一个粒子会在 0 的 x 位置发射。 下一个粒子将在下一个“ 末端” 的 沿边发射, 也就是 18 个。 以下粒子将在下一个步骤发射, 也就是 36 个, 诸如此类。 因为 576 的射程已被 32 个除去, 从而产生 18 像素 。 当一个粒子达到“ 末端”值时, 下一个粒子将重新开始 。

## 带有 Yyo 的 阶梯式发射对象 : {#a-stepped-emitter-object-with-yoyo}

您可以将可选的 `yoyo` 属性添加到一个已踩到的对象中 :

```js
x: { steps: 32, start: 0, end: 576, yoyo: true }
```

和已踩踏的发射器一样, 粒子会按顺序发射, 从“ 启动” 到“ 结束” 的跳跃。 通常情况下, 当一个已踩踏的发射机到达终点时, 它会转动到开始值。 然而, 如果您提供了“ yo” 参数, 那么当它到达终点时, 它将会反向向向返回到“ 启动 ” 。 取决于您需要的效果, 这样的效果通常会更好 。

## 分钟/ 最大对象 : {#a-min-max-object}

这使得您可以在分钟和最大属性之间选择随机浮点值:

```js
x: { min: 100, max: 700 }
```

x 值将是在分钟和最大值之间的随机浮点。

您可以通过设置“ int” 旗来强制它选择整数 :

```js
x: { min: 100, max: 700, int: true }
```

或者,您可以使用“ 随机” 矩阵方法( 见下文)

## 随机对象 : {#a-random-object}

这使得您可以在第一个和第二个阵列元素之间选择随机整数值:

```js
x: { random: [ 100, 700 ] }
```

x 值将是100到700之间的随机整数,因为它将“ 随机” 阵列中的第一个元素作为“ min” 值, 第 2 元素作为“ max” 值。

## 自定义 onEmit和 onUpdate 回调: {#custom-onemit-and-onupdate-callbacks}

如果以上内容不能给您带来您所追求的效果,您可以提供您自己的回调,当粒子同时被排放和更新时,这些回调将被使用:

```js
x: {
  onEmit: (particle, key, t, value) => {
    return value;
  },
  onUpdate: (particle, key, t, value) => {
    return value;
  }
}
```

您可以提供一种或两种功能。 `onEmit` 是在粒子生命开始时调用, 并定义属性在出生时的价值 。

`onUpdate`函数每次粒子 Emitter 更新到粒子死亡时都称为它。两者都必须返回一个值 。

属性为:

`particle` - 指粒子实例.
`key` - 属性的字符串键,即“ x” 或“ lifespan” 。
`t` - 目前粒子正常寿命,0(出生)至1(死亡)之间.
`value` - 当前属性值。 您至少应该返回此值 。

通过使用上述配置选项,您可以无限控制您的粒子行为。

## v3.55 差异 {#v355-differences}

在v3.60 Phaser之前,它使用了`ParticleEmitterManager`。在v3.60中,这个被删除,现在叫`this.add.particles`返回一个`ParticleEmitter`的例子。

为了精简内存和显示列表,我们已经完全删除了 `ParticleEmitterManager`。当你拨打 `this.add.particles`时,你正在创建 `ParticleEmitter` 实例,它正直接添加到
显示列表,并且可以像其他游戏对象一样被操纵,即缩放,旋转,定位,添加到容器等。它现在扩展了 `GameObject`的基础类,意思是它也是一个事件发射器,它允许我们
用于创建一些对粒子有用的新事件。

所以,为了创建一个发射器,你现在给它一个xy坐标,一个纹理和一个发射器配置对象(你也可以在稍后设置,但最常见的是,你会在创建时这样做). I. e:

```js
const emitter = this.add.particles(100, 300, 'flares', {
  frame: 'red',
  angle: { min: -30, max: 30 },
  speed: 150
});
```

这将在100×300时产生一个"红色信号弹"发射器.

请更新您的代码, 以确保它遵守新的函数签名 。

## 高级 Emitter 示例 {#advanced-emitter-examples}

首先,装入图像 :

```javascript
this.load.image(key, url);
```

参考文献: [load image](/guide/concepts/loader#image)

## 添加粒子 {#add-particle}

```javascript
var particles = this.add.particles(x, y, texture, {
    
    // EmitterOp
    accelerationX: 0,
    accelerationY: 0,
    alpha: 1,
    angle: { min: 0, max: 360 },
    bounce: 0,
    color: undefined,
    delay: 0,
    hold: 0,
    lifespan: 1000,
    maxVelocityX: 10000,
    maxVelocityY: 10000,
    moveToX: 0,
    moveToY: 0,
    quantity: 1,
    rotate: 0,
    scaleX: 1,
    scaleY: 1,
    // scale:
    speedX: 0,
    speedY: 0,
    speed: 
    tint: 0xffffff,
    x: 0,
    y: 0,

    // Emitter properties
    active:
    advance:
    blendMode:
    colorEase:
    deathCallback:
    deathCallbackScope:
    duration:
    emitCallback:
    emitCallbackScope:
    // callbackScope    
    frequency:
    gravityX:
    gravityY:
    maxAliveParticles:
    maxParticles:
    name:
    emitting:
    particleBringToTop:
    particleClass:
    radial:
    sortCallback:
    sortOrderAsc:
    sortProperty:
    stopAfter:
    tintFill:
    timeScale:
    trackVisible:
    visible:

    // Position
    // emitZone : random-zone, edge-zone
    // random-zone
    emitZone: {
        type: 'random',
        source: geom,
    },

    // edge-zone
    emitZone:{
        type: 'edge',
        source: geom,
        quantity: 1,
        stepRate: 0,
        total: -1,
        yoyo: false,
        seamless: true
    },

    deathZone: {
        type: 'onEnter', // 'onEnter', or 'onLeave'
        source: geom,
    },

    bounds:               // {x, y, w, h}, or {x, y, width, height}, or Phaser.Geom.Rectangle
    collideLeft: true,
    collideRight: true,
    collideTop: true,
    collideBottom: true,

    follow:
    followOffset:{
       x: 0,
       y: 0
    },

    // Texture
    texture:
    frame:
    anim: [],  // string, or array of string
    
    reserve: 0,
    advance: 0
});
```

- EmitterOp 参数: 数字、 随机矩阵、 自定义调用、 步入始/ 终、 易控始/ 终、 分钟/ 最大、 随机对象、 自定义 onEmit onUpdate内插
  - 数字
  - `{min, max}`: 在分钟和最大值之间选择一个随机值
  - `{min, max, int}`
  - `{start, end}` : 选择一个范围内连续递增的数值。 (`ease`=`'Linear'`)
    - `{start, end, ease}`
    - `{start, end, ease, easeParams}`
  - `{start, end, steps}` : 选择跨区域递增的数值。
  - `{start, end, steps, yoyo: true}`
  - `{start, end, random}`
    - `random`: `true` 或 或 时 间 `false`
  - `{random: [start, end]}` :在开始和开始之间选择随机数字。
  - `[a, b, c, d]` :从数组中选择随机数字。
  - `{min, max, steps}` : 选择分钟到最大值之间,并有阶梯。
  - `{ values: [ a, b, c, d ], interpolation: 'catmull', ease: 'linear' }` : 内插(`linear`, `bezier`, `catmull`),值数组中。
  - `function(particle, key, t, value) { return value; }`
  - `{onEmit, onUpdate}`:从函数引用中获取返回值。

    ```javascript
    function(particle, key, t, value) {
        return value;
    }
    ```

- `active`:这个发射器是否更新了自身及其粒子.
  - `false` :等于暂停.
- `advance` : 如果您希望* 及时向外转发 * , 请将这个值设定为代表 向外 发送 的 ms 数 。
- `blendMode` : 见 [blend mode](/guide/concepts/display#blend-mode)
- `colorEase`:如果通过`color`属性启用粒子颜色插值,则基于字符串的易控函数名称将使用,否则无效.
- `deathCallback`, `deathCallbackScope`

    ```javascript
    function(particle) {

    }
    ```

- `emitCallback`, `emitCallbackScope`

    ```javascript
    function(particle, emitter) {

    }
    ```

- `duration`:限制发射器发射粒子,最大可发射`duration` ms.
  - `0` :永远,默认行为.
- `follow`:一个以位置作为粒子源的游戏对象.
- `followOffset`:从以下目标中抵消粒子来源.
- `frequency`
  - `0`:每次逻辑更新(最大流频)的1个粒子流周期.
  - `> 0`:粒子流周期间以ms计的时间间隔.
  - `-1` : 爆裂发射器.
- `hold`:在它完成使用期后,在固定的毫秒后冻结或“原地保存”
- `gravityX`, `gravityY`
- `maxAliveParticles`
- `maxParticles`
  - `0` : Unlimited.
  - `> 0` : 硬限制粒子物体的数量.
- `frames`:一个或多个纹理帧,或配置对象.
  - 字符串或数字值
  - 字符串或数字值的矩阵
  - 配置对象 :

    ```javascript
    {
        frames: [],
        cycle: false,
        quantity: 1
    }
    ```

- `anim` :
  - String
  - 字符串矩阵
  - 配置对象 :

    ```javascript
    {
        anim: [],  // Array of string
        cycle: false,
        quantity: 1
    }
    ```

- `particleBringToTop` :
  - `true`: 粒子列表的顶部添加了新排放的粒子, 即被制成在已经活着的粒子之上。 默认行为 。
- `sortCallback` :用于排序粒子的调用。
- `sortProperty`: 粒子在根据此属性制成前可选排序。 属性必须存在于 `Particle` 类上, 如 `y` 、 `lifeT` 、 `scaleX` 等 。
- `sortOrderAsc`:当`sortProperty`被定义时,它控制了排序顺序,无论是升降顺序.
- `stopAfter`: 粒子发射器将在达到这个总数后停止发射粒子。 然后进入“ 停止” 状态, 发射 `STOP` 事件 。
- `radial`:射线发射器将在角点和最大点之间向各个方向发射粒子,
- `emitting`:如果发射体目前排放粒子流(当频率为QQ0时),则控制.
  已经存在的粒子会不断更新,直到到期.
  - `false` : 等于停止( E)
- `tintFill` :
- `timeScale` : 活性粒子应用的时间率, 影响寿命、 运动和扭矩。 大于 1 的值比正常的要快 。
- `trackVisible`:发射方的`visible`状态是否会跟踪后续目标可见状态.
- `emitZone` :
  - [Emit zone](#emit-zone)

    ```javascript
    {
        type: 'random',
        source: geom,
    }            
    ```

  - [Emit edge](#add-emit-edge)

    ```javascript
    {
        type: 'edge',
        source: curve,
    
        quantity: 1,
        stepRate: 0,
        yoyo: false,
        seamless: true
    }            
    ```

- [`deathZone`](#death-zone)

    ```javascript
    {
        type: 'onEnter', // 'onEnter', or 'onLeave'
        source: geom
    }
    ```

- `bounds` : `{x, y, w, h}`,或 ,或 , `{x, y, width, height}`,或 ,或 , [Rectangle](/guide/concepts/geometry#rectangle).
- `collideLeft`,`collideRight`,`collideTop`,`collideBottom`:粒子是否与边界的左/右/上/下边缘相互作用.
- `name`
- [`particleClass`](#custom-particle-class)

## 控制 {#control}

- Start

    ```javascript
    emitter.start();
    // emitter.start(advance, duration);
    ```

  - `advance` :通过发射器及时推进这一个毫秒。
  - `duration` : 将这个发射器限制在只为给定的 ms 数发射粒子。 设置此参数将覆盖 Emitter 配置对象中已经设定的任何持续时间 。
- Stop

    ```javascript
    emitter.stop();
    // emitter.stop(kill);
    ```

  - `kill` :
    - `true`:立即杀死所有粒子
    - `false` : 让他们在寿命到期后死去。默认行为 。
- Pause

    ```javascript
    emitter.pause();  // set `active` to false
    ```

- Resume

    ```javascript
    emitter.resume();  // set `active` to true
    ```

- 启动( 或重新启动) 粒子流 。

    ```javascript
    emitter.flow(frequency, count, stopAfter);
    ```

  - `frequency` :
    - `>= 0`:每个流周期的时间间隔,以毫秒计
    - `-1` : 爆炸模式.
  - `count`:每个流周期中发射的粒子数量.
  - `stopAfter`:一旦达到这个值,就停止发射这个粒子。
    - 设置此参数将覆盖 Emitter 配置对象中已经设定的任何 `stopAfter` 值 。
    - `0` : Unlimited
- 爆炸:将发射器置于爆炸模式(`frequency` = `-1`),停止任何流粒子流,同时发射数颗粒子。

    ```javascript
    emitter.explode();
    // emitter.explode(count, x, y);
    ```

  - `count` : 发射的粒子数。
  - `x`, `y` : x,y 坐标以释放粒子。
- 释放 : 在指定位置发射粒子。 如果没有给出位置, 它将会从此 Emitters 当前位置中发射 。

    ```javascript
    emitter.emitParticleAt();
    // emitter.emitParticleAt(x, y, count);    
    ```

    or

    ```javascript
    emitter.emitParticle(count, x, y);
    ```

  - `count` : 发射的粒子数。
  - `x`, `y` : x,y 坐标以释放粒子。
- 快速前进

    ```javascript
    emitter.fastForward(time, delta);
    ```

  - `time`: 推进粒子发射的毫秒数 。
  - `delta`: 每一步使用的三角洲数量。默认为`1000 / 60` 。
- 杀死所有活着的粒子

    ```javascript
    emitter.killAll()
    ```

## 跟着目标 {#follow-target}

- Start

    ```javascript
    emitter.startFollow(target);
    // emitter.startFollow(target, offsetX, offsetY, trackVisible);
    ```

  - 游戏对象(`target`):要遵循的游戏对象.
  - `offsetX`,`offsetY`:从游戏对象中获取粒子源的横向/纵向抵消.
  - `trackVisible` : 发射器的可见状态是否会跟踪目标可见状态.
- Stop

    ```javascript
    emitter.stopFollow();
    ```

## 帧 {#frame}

```javascript
emitter.setEmitterFrame(frames);
// emitter.setEmitterFrame(frames, pickRandom, quantity);
```

- `frames`:一个或多个纹理帧,或配置对象.
  - 字符串或数字值
  - 字符串或数字值的矩阵
  - 配置对象 :

    ```javascript
    {
        frames: [],
        cycle: false,
        quantity: 1
    }
    ```

- `pickRandom` :
  - `true`: 是否从`frames`随机指定帧。 默认行为 。
- `quantity`: 将接收每个帧的连续粒子数。 默认值为 `1` 。

## 动画 {#animation}

```javascript
emitter.setAnim(anims);
// emitter.setAnim(anims, pickRandom, quantity);
```

- `anims`:一个或多个动画,或一个配置对象.
  - String
  - 字符串矩阵
  - 配置对象 :

    ```javascript
    {
        anims: [],
        cycle: false,
        quantity: 1
    }
    ```

    - `anims`:一个或多个动画名称,或播放动画配置对象.
      - String
      - 字符串矩阵
      - [Animation config](/guide/concepts/animations#add-animation)
      - 组合 [Animation config](/guide/concepts/animations#add-animation)
- `pickRandom` :
  - `true`: 是否从`frames`随机指定帧。 默认行为 。
- `quantity`: 将接收每个帧的连续粒子数。 默认值为 `1` 。

## 粒子 {#particle}

- Speed

    ```javascript
    emitter.setParticleSpeed(x, y);
    ```

    or

    ```javascript
    emitter.speedX = x;
    emitter.speedY = y;
    ```

  - 将发射器从射线改为点发射器
- Bounce

    ```javascript
    emitter.bounce = value;
    ```

  - `0` : 无反弹
  - `1` : 全面反弹
- 最大速度( T)

    ```javascript
    emitter.maxVelocityX = x;
    emitter.maxVelocityY = y;
    ```

- Gravity

    ```javascript
    emitter.setParticleGravity(x, y);
    ```

    or

    ```javascript
    emitter.gravityX = x;
    emitter.gravityY = y;
    ```

- Acceleration

    ```javascript
    emitter.accelerationX = x;
    emitter.accelerationY = y;
    ```

- 寿命:设定新排放颗粒的寿命,以毫秒计。

    ```javascript
    emitter.setParticleLifespan(time);
    ```

    or

    ```javascript
    emitter.lifespan = time
    ```

- 粒子开始更新前, 排放后等待的毫秒数 。

    ```javascript
    emitter.delay = time;
    ```

- 粒子完成生命后等待的毫秒数,然后被移除.

    ```javascript
    emitter.hold = time;
    ```

- Tint

    ```javascript
    emitter.setParticleTint(tint);
    ```

    or

    ```javascript
    emitter.particleTint = tint;
    ```

  - 仅使用网络gl
- Color

    ```javascript
    emitter.particleColor = color;   // WebGL only.
    emitter.colorEase = easeName;
    ```

  - 仅使用网络gl
- Alpha

    ```javascript
    emitter.setParticleAlpha(alpha);
    ```

    or

    ```javascript
    emitter.setAlpha(alpha);
    ```

    or

    ```javascript
    emitter.particleAlpha = alpha;
    ```

- 缩放 : 设置所排放粒子的垂直和水平尺度。

    ```javascript
    emitter.setParticleScale(x, y);
    ```

    or

    ```javascript
    emitter.setScale(x, y);
    ```

    or

    ```javascript
    emitter.particleScaleX = x;
    emitter.particleScaleY = y;
    ```

- Position

    ```javascript
    emitter.particleX = x;
    emitter.particleY = y;
    ```

- 向前进的位置

    ```javascript
    emitter.moveToX = x;
    emitter.moveToY = y;
    ```

- 粒子发射的角度 。

    ```javascript
    emitter.particleAngle = angle;  // degrees    
    ```

- 每个粒子发射时的旋转(或角度).

    ```javascript
    emitter.particleRotate = rotation; // degrees
    ```

- 每次排放时排放的颗粒数量

    ```javascript
    emitter.quantity = quantity;
    ```

- 硬限制粒子对象的数量

    ```javascript
    var count = emitter.maxParticles;
    ```

  - 是否该发射器处于极限

    ```javascript
    var atLimit = emitter.atLimit();
    ```

- 活性(活性)粒子
  - 活颗粒量

    ```javascript
    var count = emitter.getAliveParticleCount();
    ```

    or

    ```javascript
    var count = emitter.alive.length;
    ```

  - 添加新发射粒子的回调

      ```javascript
      var callback = function(particle, emitter) { /* ... */ }
      emitter.onParticleEmit(callback, context);
      ```

    - 清除回调

      ```javascript
      emitter.onParticleEmit();
      ```

  - 每一个活的粒子

    ```javascript
    var callback = function(particle, emitter) { /* ... */ }
    emitter.forEachAlive(callback, context);
    ```

- 死亡( 不活动) 粒子
  - 死亡颗粒量

    ```javascript
    var count = emitter.getDeadParticleCount();
    ```

    or

    ```javascript
    var count = emitter.dead.length;
    ```

  - 为每个粒子死亡添加回调

    ```javascript
    var callback = function(particle, emitter) { /* ... */ }
    emitter.onParticleDeath(callback, context);
    ```

    - 清除回调

      ```javascript
      emitter.onParticleDeath();
      ```

  - 每一个死颗粒

    ```javascript
    var callback = function(particle, emitter) { /* ... */ }
    emitter.forEachDead(callback, context);
    ```

  - 将死颗粒添加到池中

    ```javascript
    emitter.reserve(count);
    ```

- 颗粒总量(活性+死性).

    ```javascript
    var count = emitter.getParticleCount();
    ```

- 活性粒子与矩形几何天体或Arcade 物理天体重叠.

    ```javascript
    var particles = emitter.overlap(target);
    ```

  - `target` :
    - A. 国家 [Rectangle](/guide/concepts/geometry#rectangle).
    - 拱门物理体.
  - `particles`:与给定目标重叠的粒子阵列
- 从所有当前活动的粒子的边框中计算出边框矩形

    ```javascript
    emitter.getBounds(padding, advance, delta, output);
    ```

  - `padding`: 贴的量,以像素表示,以加入边框矩形.
  - `advance`, `delta` :*快前* 及时尝试让界限更准确.
  - `output` : 数据 [Rectangle](/guide/concepts/geometry#rectangle) 以存储结果。
- 以几何矩形获取此粒子的边界

    ```javascript
    particle.getBounds();
    ```

### 渲染顺序 {#render-order}

- 按属性排序

    ```javascript
    emitter.setSortProperty(property, ascending);
    ```

  - `property` : 属性 `Particle` 班级来排序。
  - `ascending`: 粒子是按上升还是下降顺序排序的吗?
- 以回调方式排序

    ```javascript
    var callback = function(particleA, particleB) {
        return 1; // 0,1,-1
    }
    emitter.setSortCallback(callback);
    ```

## 发送器 {#emitter}

- Frequency

    ```javascript
    emitter.setFrequency(frequency);
    // emitter.setFrequency(frequency, quantity);
    ```

  - `frequency` :
    - `>= 0`:每个流周期的时间间隔,以毫秒计
    - `-1` : 爆炸模式.
  - `quantity`:每个流周期或爆炸时要释放的粒子数量.
- Quantity

    ```javascript
    emitter.setQuantity(quantity);
    ```

  - `quantity`:每个流周期或爆炸时要释放的粒子数量.

## 区 {#zone}

## 释放区 {#emit-zone}

### 添加发射区 {#add-emit-zone}

```javascript
var zone = emitter.addEmitZone({
    type: 'random',
    source: geom,
});
```

- `source` : 地理像 : [Circle](/guide/concepts/geometry#circle), [Ellipse](/guide/concepts/geometry#ellipse), [Rectangle](/guide/concepts/geometry#rectangle),[Triangle](/guide/concepts/geometry#triangle), [Polygon](/guide/concepts/geometry#polygon),或 ,或 , [Path or Curve](/guide/concepts/math#path),它已经 `getRandomPoint(point)` 方法
  - 自定义区域

    ```javascript
    {
        getRandomPoint: function(point) {
            // point.x = ...
            // point.y = ...
            return point;
        }
    }
    ```

### 添加弹出边 {#add-emit-edge}

```javascript
var zone = emitter.addEmitZone({
    type: 'edge',
    source: curve,

    quantity: 1,
    stepRate: 0,
    yoyo: false,
    seamless: true,
    total: -1
});
```

- `source` : 地理像 : [Circle](/guide/concepts/geometry#circle), [Ellipse](/guide/concepts/geometry#ellipse), [Rectangle](/guide/concepts/geometry#rectangle),[Triangle](/guide/concepts/geometry#triangle), [Polygon](/guide/concepts/geometry#polygon),或 ,或 , [Path or Curve](/guide/concepts/math#path),它已经 `getPoints(quantity, stepRate)` 方法
  - 自定义边

    ```javascript
    {
        getPoints: function(quantity, stepRate) {
            // output = [point0, point1, ...];  // point: Phaser.Math.Vector2, or {x, y}
            return output;
        }
    }
    ```

- `quantity`: 将粒子数放置在源边上。 设定为 0 , 改为使用 `stepRate` 。
- `stepRate` : 每个粒子之间的距离。设定时, `quantity` 被暗示,并应当设定为0。
- `yoyo`:粒子是否从始至终被放置,然后从始至终被放置。默认是`false`。
- `seamless`:如果一个端点与另一个端点相同,是否将移除。默认为`true`。
- `total`:这个区域在传递到埃米特的下一个排放区之前,将发射粒子的总数。

注意"数量或stepRate"
    - 任何几何学类 [circle](/guide/concepts/geometry#circle), [ellipse](/guide/concepts/geometry#ellipse), [line](/guide/concepts/geometry#line), [polygon](/guide/concepts/geometry#polygon), [rectangle](/guide/concepts/geometry#rectangle), [triangle](/guide/concepts/geometry#triangle) 资料来源有*数量*或*stepRate*
    - [Curve](/guide/concepts/math#curve)源有*数量*或*stepRate*.
    - [Path](/guide/concepts/math#path)源只有*数量*

### 设定发射区域 {#set-emit-zone}

```javascript
emitter.setEmitZone(zone);
```

- `zone`: 将"解放区"设定为活动区.
  - 区域对象
  - 数字作为索引

### 区源 {#zone-source}

- Get

    ```javascript
    // var zone = emitter.emitZones[i];
    var source = zone.source;    
    ```

- (仅标类型) 曲线源的更新点

    ```javascript
    zone.updateSource();
    ```

- (仅选择类型)设定源到另一个曲线, 也更新点

    ```javascript
    zone.changeSource(curve);
    ```

### 删除发件区域 {#remove-emit-zone}

```javascript
emitter.removeEmitZone(zone)
```

### 清除发射区 {#clear-emit-zone}

```javascript
emitter.clearEmitZones();
```

or

```javascript
emitter.emitZones.length = 0;
emitter.zoneIndex = 0;
```

## 死亡区 {#death-zone}

```javascript
var zone = emitter.addDeathZone({
     type: 'onEnter',
     source: geom
});
```

- `type` : `'onEnter'` 或 或 时 间 `'onLeave'`
- `source` : 地理像 : [Circle](/guide/concepts/geometry#circle), [Ellipse](/guide/concepts/geometry#ellipse), [Rectangle](/guide/concepts/geometry#rectangle),[Triangle](/guide/concepts/geometry#triangle), [Polygon](/guide/concepts/geometry#polygon)
  - 自定义 `source` :

    ```javascript
    {
        contains: function (x, y) {
            // ...
            return bool;
        }
    }
    ```

### 删除死亡区域 {#remove-death-zone}

```javascript
emitter.removeDeathZone(zone)
```

### 清除死亡区域 {#clear-death-zone}

```javascript
emitter.clearDeathZones();
```

or

```javascript
emitter.deathZones.length = 0;
```

## 事件 {#events}

- 开始排放颗粒。

    ```javascript
    emitter.on('start', function(emitter) {

    })
    ```

- 爆炸了一组粒子。

    ```javascript
    emitter.on('explode', function(emitter, particle) {

    })
    ```

- 死亡区杀死了粒子案例

    ```javascript
    emitter.on('deathzone', function(emitter, particle, zone) {

    })
    ```

- 停止排放

    ```javascript
    emitter.on('stop', function(emitter) {

    })
    ```

  - 直接叫`ParticleEmitter.stop`方法.
  - 过了一定时间再通过`duration`地产停止.
  - 通过 `stopAfter` 属性对一组粒子进行后停止 。
- 完全事件,此时没有粒子在渲染.

    ```javascript
    emitter.on('complete', function(emitter) {

    })
    ```

## 边界 {#bounds}

- 添加界限

    ```javascript
    var bounds = emitter.addParticleBounds(x, y, width, height);
    // var bounds = emitter.addParticleBounds(x, y, width, height, collideLeft, collideRight, collideTop, collideBottom);
    ```

    or

    ```javascript
    var bounds = emitter.addParticleBounds(rect);
    ```

  - `x, y, width, height`, `{x, y, width, height}`, or `{x, y, w, h}`, or [Rectangle](/guide/concepts/geometry#rectangle) : Bounds
  - `collideLeft`,`collideRight`,`collideTop`,`collideBottom`:粒子是否与边界的左/右/上/下边缘相互作用.
- 折叠边缘

    ```javascript
    bounds.collideLeft = enabled;
    bounds.collideRight = enabled;
    bounds.collideTop = enabled;
    bounds.collideBottom = enabled;
    ```

- 捆绑矩形

    ```javascript
    var rect = bounds.bounds;
    ```

  - `rect` : [Rectangle](/guide/concepts/geometry#rectangle)

## 引力不错 {#gravity-well}

- 创造引力井

    ```javascript
    var well = particles.createGravityWell({
        // x: 0,
        // y: 0,
        // power: 0,
        // epsilon: 100,
        // gravity: 50
    });
    ```

- Enable
  - Active

       ```javascript
       well.active = true;
       ```

  - Inactive

       ```javascript
       well.active = false;
       ```

- Position

    ```javascript
    well.x = x;
    well.y = y;
    ```

- Gravity

    ```javascript
    well.gravity = value;
    ```

- Power

    ```javascript
    well.power = value;
    ```

## 自定义粒子处理器 {#custom-particle-processor}

- 宣告粒子处理器类

    ```javascript
    class MyParticleProcessor extends Phaser.GameObjects.Particles.ParticleProcessor {
        constructor() {
            super(x, y, active);
            // ...
        }

        update(particle, delta, step, t) {
            // particle : The Particle to update.
            // delta : The delta time in ms.
            // step : The delta value divided by 1000.
            // t : The current normalized lifetime of the particle, between 0 (birth) and 1 (death).
        }

        destroy() {
            super.destroy();
        }
    }
    ```

  - 覆盖 `update` 方法
- 添加到发射器

    ```javascript
    var myParticleProcessor = emitter.addParticleProcessor(new MyParticleProcessor);
    ```

## 自定义粒子类 {#custom-particle-class}

```javascript
class MyParticle extends Phaser.GameObjects.Particles.Particle {
    constructor (emitter) {
        super(emitter);
        /* ... */
    }

    update (delta, step, processors) {
        super.update(delta, step, processors);
        /* ... */
    }
}
```

## 其他属性 {#other-properties}

见[game object](/guide/concepts/gameobjects)

## 创建遮罩 {#create-mask}

```javascript
var mask = emitter.createBitmapMask();
```

见[mask](/guide/concepts/display#masks)

## 着色器效果 {#shader-effects}

支持 [postFX effects](/guide/concepts/gameobjects/shader) 软件

!!! note
    无 preFX 效果支持

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
