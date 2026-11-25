# 动画 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/animations)

Phaser中的主要动画手段是使用基于“帧”的动画。如前所述,Phaser维持一个纹理类,该类包含着尽可能多的纹理上可能存在的框架。动画节允许您以一个相继的帧速率来播放这些框架的序列。这就是您如何在游戏中创造斯普里特斯动画的幻觉。为了实现这一点,您经常看到纹理图像文件被分为一个帧的“格”,每个帧是一个不同的动画框架。这被称为斯普里特工作表或纹理图集。

动画是通过动画管理器创建的。 每个场景都有自己的动画管理器。 您可以任意创建多少场动画, 并且每场动画可以有多少帧。 如果您愿意, 您也可以创建多个动画, 全部使用相同的帧。 例如, 您可以拥有一个使用帧 1 到 4 的“ 步行” 动画, 以及一个使用帧 1 到 8 的“ 运行” 动画, 两场动画都会使用重叠的帧, 但播放速度不同 。

并非所有游戏对象都可以被动画化。 您将使用的主要游戏对象是 Sprite 游戏对象。 此游戏带有它自己的动画状态组件, 允许您直接在 Sprite 实例上创建和播放动画 。

动画可以是全球动画也可以是本地动画,全球动画是通过动画管理器创建的,可供游戏中所有游戏对象使用. 本地动画是直接在游戏对象上创建的,如Sprite,本地动画只供该游戏对象使用,其他游戏对象无法使用.

值得一提的是,动画也可以通过调谐对象来实现,如果只需要运动+微妙变化的混合(如尺度或α),Phaser 3也有用于斯宾尼动画的插件,这是Esoteric Software公司发布的骨质动画软件包.

## 动画管理器 {#animation-manager}

### 添加动画 {#add-animation}

```js
var animationConfig = {
  key: "",

  frames: [],

  sortFrames: true,
  defaultTextureKey: null,
  skipMissedFrames: true,
  randomFrame: false,

  // time
  delay: 0,
  duration: null,
  frameRate: null,
  timeScale: 1,

  // repeat
  repeat: 0, // set to (-1) to repeat forever
  repeatDelay: 0,
  yoyo: false,

  // visible
  showBeforeDelay: false,
  showOnStart: false,
  hideOnComplete: false,
};

this.anims.create(animationConfig);
```

- `key`:此动画数据独有的密钥
- `frames`: 一组`{key, frame}`

  - 属性

    ```js
    {
        key: '',
        frame: '', // string, or number
        duration: 0
    }
    ```

    - `duration` : 动画的这个帧的长度,以ms表示.

  - 字符串:纹理键。
  - 地图集中的每个框架

    ```js
    this.anims.generateFrameNames(key);
    ```

  - 框架序列索引从头到尾

    ```js
    var config = ;
    this.anims.generateFrameNames(key,
    {
        prefix: '',
        start: 0,
        end: 0,
        suffix: '',
        zeroPad: 0,
        // outputArray: [], // Append frames into this array
    });
    ```

    - `prefix + Pad(i, zeroPad, '0', 1) + suffix`,i:开始~结束

  - 自定义帧序列

    ```js
    var config = ;
    this.anims.generateFrameNames(key,
    {
        prefix: '',
        suffix: '',
        zeroPad: 0,
        frames: [ ... ]
        // outputArray: [], // Append frames into this array
    });
    ```

    - `prefix + Pad(frames[i], zeroPad, '0', 1) + suffix`

- `sortFrames`:框架名称按数字排序。默认值为`true`。
- `defaultTextureKey`:动画所有帧的纹理键将使用,每个帧可以覆盖.
- `skipMissedFrames` : 如果时间滞后, 跳过框架, 或者总是提前? 默认值是 `true` 。
- `randomFrame`: 从随机选择的框架开始播放此动画? 默认值为`false`.
- `delay`: 开始重播前的延迟。 数值以毫秒表示 。
- `duration`: 动画在毫秒内播放的时间。 如果不是从`frameRate`得到的话。
- `frameRate`: 帧每秒播放的帧速率。默认值为`24` 。
- `timeScale`: 用于重播此动画的时间尺度。 默认值为 `1` 。
- `repeat`:重复动画的次数。默认值为`0`。
  - `-1` : Infinity
- `repeatDelay`: 动画重现前的延迟。 数值以毫秒表示 。
- `yoyo` : 动画 Yoyo 是否在重复之前要返回( 倒转到开始) ? 默认值是 `false`.
- `showBeforeDelay`:如果这款动画有延迟,它应该立即显示第一帧(`true`),或者只在延迟(`false`)之后显示.
- `showOnStart`: 当动画开始播放时, `sprite.visible = true`是否应该? 如果设定, 会发生 _after_ any laild, 如果设置的话。 默认值为 `false` 。
- `hideOnComplete`: 当动画完成时, should smart. visible = 假的? 默认值为 `false`.

#### 使用纹理中的每个框架 {#use-every-frame-in-a-texture}

```js
// Create animation 'mummyWalk' from every frame in texture 'mummy':
this.anims.create({
  key: "mummyWalk",
  frames: "mummy",
});
```

#### 选择纹理框架 {#choosing-texture-frames}

您通常需要知道纹理框架名称。 要获取框架名称:

```js
console.assert(this.texture.exists("mummy"));
console.log(this.textures.get("mummy").getFrameNames());
```

```js
// Create animation 'mummyWalk' from frames 0, 1, 2 of texture 'mummy':
this.anims.create({
  key: "mummyWalk",
  frames: [
    { key: "mummy", frame: 0 },
    { key: "mummy", frame: 1 },
    { key: "mummy", frame: 2 },
  ],
});
```

当然,你可以使用任何技术来制作动画.

```js
// We have 3 textures with identical frame patterns.
const textureKeys = ["giant", "elf", "goblin"];

// We will create 9 animations from 3 sequences.
const anims = {
  idle: [0],
  walk: [1, 2],
  attack: [3, 4],
};

for (const textureKey of textureKeys) {
  for (const animName of anims) {
    this.anims.create({
      // 'giant:idle', 'giant:walk', etc.
      key: `${textureKey}:${animName}`,
      frames: anims[animName],
    });
  }
}
```

#### 框架时间 {#frame-timing}

您可以为整部动画给出 `frameRate`( 默认为 24 英尺) 或 `duration`。 帧持续时间为 `1000 / frameRate` 或 `duration / frames.length` 。

如果设置了每个帧的长度,这些长度是****加到计算出来的帧长度。所以如果想要设置帧长度,请使用1ms的动画长度。

```js
this.anims.create({
  key: "spikes",
  repeat: -1,
  defaultTextureKey: "spikes",
  duration: 1, // 1 ms, close enough to 0
  frames: [
    { frame: 0, duration: 3000 },
    { frame: 1, duration: 250 },
    { frame: 2, duration: 250 },
    { frame: 3, duration: 3000 },
    { frame: 2, duration: 250 },
    { frame: 1, duration: 250 },
  ],
});
```

#### generateFrameNumbers(a) 与 generateFrameNames() {#generateframenumbers-and-generateframenames}

帮助器方法 [generateFrameNumbers()](/api/class/animations-animationmanager#generateFrameNumbers)和 [generateFrameNames()](/api/class/animations-animationmanager#generateFrameNames) 都按照图案选择**帧名称,然后根据图案选择** 基因** 一组[AnimationFrame](/api/typedef/types-animations#animationframe)对象,可以随`frames`属性而传递. `generateFrameNumbers()`选择图案表式框架名称(index),`generateFrameNames()`选择地图册式框架名称,它们从不选择在纹理中不存在的帧名称.

例如,

```js
this.anims.generateFrameNumbers("mummy", { frames: [0, 1, 2] });
```

or

```js
this.anims.generateFrameNumbers("mummy", { start: 0, end: 2 });
```

将产生我们在上面写的3个框架配置的阵列。

`generateFrameNames()`配置具有`generateFrameNumbers()`的所有选项,加上`prefix`,`suffix`,以及`zeroPad`.

如果您遇到麻烦, 请记录这些方法的输出 。

#### 从 Aeprite 添加 {#add-from-aseprite}

[Aseprite](https://www.aseprite.org/)是一个强大的动画图案编辑器和像素艺术工具。从装入的 Aseprite JSON 文件创建一个或多个动画。

```js
this.anims.createFromAseprite(key);
// this.anims.createFromAseprite(key, tags, target);
```

- `key` : 已装入的 Aseprite 地图集的密钥.
- `tags` :
  - `undefined` : 装入所有标记 。
  - 字符串标记组:装入这些标记.
- `target` : 创建此目标Sprite上的动画.
  - `undefined`: 在全球创建的动画管理器。默认行为 。

### 删除动画 {#remove-animation}

```js
this.anims.remove(key);
```

### 混合和延迟两个动画 {#mixing-and-delaying-between-two-animations}

- Add

  ```js
  this.anims.addMix(animA, animB, delay);
  ```

  - `animA`, `animB` :动画的弦键,或动画的实例.

- Remove

  ```js
  this.anims.removeMix(animA, animB);
  // this.anims.removeMix(animA);
  ```

- Get

  ```js
  var delay = this.anims.getMix(animA, animB);
  ```

- 动画组合的例子,用于从一个动画向另一个动画过渡.

  ```js
  this.anims.create({ key: "animA" /* etc. */ });
  this.anims.create({ key: "animB" /* etc. */ });

  this.anims.addMix("animA", "animB", 200);
  ```

  如果在第一次播放时播放第二部动画,则会自动应用延迟.

  ```js
  sprite.play("animA");
  // Later:
  sprite.play("animB");
  ```

  和我们很相似

  ```js
  if (sprite.anims.isPlaying && sprite.anims.getName() === "animA") {
    sprite.anims.playAfterDelay("animB", 200);
  }
  ```

### 播放动画 {#play-animation}

- Play

  ```js
  this.anims.play(key, children);
  ```

- 跳跃游戏( 延迟游戏)

  ```js
  this.anims.staggerPlay(key, children, stagger, staggerFirst);
  ```

  - `children`: 游戏对象阵列, 用于播放动画
  - `stagger`: 将每次播放时间抵消的时间, 以毫秒计
  - `staggerFirst`: 设置 `true` 以应用第1个孩子的延迟

- 当事件触发时播放动画

  ```js
  sprite.on(event, function () {
    sprite.play(key);
  }

  ```

  Example:

  ```js
  sprite.on('pointerdown', function () {
    sprite.play('smile');
  }
  ```

- 如果动画已经播放, 则忽略播放

  ```js
  sprite.play(key, ignoreIfPlaying);
  ```

  - `ignoreIfPlaying` : 设置为 `true` 忽略重启动画。

  Example:

  ```js
  sprite.play("run", true); // only plays the "run" animation if it is not already playing
  ```

- 链路动画

`chain()` 将动画排在当前 ** 完成 ** 或 ** stops ** 之后播放。 重复的链条会添加到队列的 ** 尾** 。 如果动画重复, 只有 `stop()` 将推进队列。 如果您想要最后的停止, 请执行 。

```js
sprite.chain().stop();
```

要小心错把太多的动画连起来.

```js
function update() {
  // Choose a reasonable maximum.
  if (sprite.anims.nextAnimsQueue.length > 10) {
    throw new Error("Too many chained animations");
  }
}
```

内部,下一部连锁动画是`nextAnim`,其他任何一部都是`nextAnimsQueue`.

- 延迟或重复计数后播放动画
  
  - `playAfterDelay()`

    ```js
    sprite.playAfterDelay(key, delay);
    ```

    - `key`:动画中以弦键为主的键.
    - `delay` : 延迟,以毫秒计,等待后再播放动画.

  - `playAfterRepeat()`

    ```js
    sprite.playAfterRepeat(key, repeatCount);
    ```

    - `key`:动画中以弦键为主的键.
    - `repeatCount`:默认为1. 下一部动画剧之前,当前动画的数量重复.

### 暂停所有动画 {#pause-all-animations}

```js
this.anims.pauseAll();
```

### 恢复所有动画 {#resume-all-animations}

```js
this.anims.resumeAll();
```

### 全球时间范围 {#global-time-scale}

动画管理器的全球时间尺度。 将时间三角形缩放在两个帧之间, 从而影响动画管理器的时间速度 。

- Get

  ```js
  var timeScale = this.anims.globalTimeScale;
  ```

- Set

  ```js
  this.anims.globalTimeScale = timeScale;
  ```

### 有动画 {#has-animation}

```js
var hasAnim = this.anims.exists(key);
```

### 导出/ 装入量 {#exportload}

- 导出 JSON

  ```js
  var json = this.anims.toJSON();
  ```

- 从 JSON 装入

  ```js
  this.anims.fromJSON(json);
  // this.anims.fromJSON(json, clearCurrentAnimations);
  ```

  - 在预装阶段装入 JSON

    ```js
    scene.load.json(key, url);
    ```

  - 在预装阶段装入动画

    ```js
    scene.load.animation(key, url);
    ```

### 事件 {#events}

- 添加动画时

  ```js
  this.anims.on("add", function (key, anim) {});
  ```

- 删除动画时

  ```js
  this.anims.on("remove", function (key, anim) {});
  ```

- 暂停所有动画

  ```js
  this.anims.on("pauseall", function () {});
  ```

- 在恢复所有动画时

  ```js
  this.anims.on("resumeall", function () {});
  ```

## 动画对象 {#animation-object}

```js
var anim = this.anims.get(key);
```

Example:

```js
const mummyWalkAnim = this.anims.get("mummyWalk");
```

### 添加帧 {#add-frame}

- 附加框架

  ```js
  anim.addFrame(frame);
  ```

  - `frame` : `this.anims.generateFrameNames(key, config)`

- 在索引中插入框架

  ```js
  anim.addFrameAt(index, frame);
  ```

  - `frame` : `this.anims.generateFrameNames(key, config)`

### 删除框架 {#remove-frame}

- 删除框架时

  ```js
  anim.removeFrameAt(index);
  ```

- 删除框架

  ```js
  anim.removeFrame(frame);
  ```

### 获取帧 {#get-frame}

- 有框架索引

  ```js
  var HasFrameAt = anim.checkFrame(index);
  ```

- 获取索引框

  ```js
  var frame = anim.getFrameAt(index);
  ```

  Example:

  ```js
  const mummyWalkFrame1 = this.anims.get("mummyWalk").getFrameAt(1);
  ```

- 获取最后一个框架

  ```js
  var frame = anim.getLastFrame();
  ```

### 导出 {#export}

- 导出 JSON

  ```js
  var json = anim.toJSON();
  ```

  or

  ```js
  var jsonString = JSON.stringify(anim);
  ```

## 常见错误 {#common-errors}

> TypeError: 未定义不是对象( 正在评价“ animationFrame. frame. texture ”)

在 [setCurrentFrame()](/api/class/animations-animationstate#setCurrentFrame) 中。通常您会用坏的纹理键创建动画。

> TypeError: 未定义不是对象( 正在评价“ 状态 . currentFrame. dultation ” )

输入 [getFirstTick()](/api/class/animations-animation#getFirstTick)。您正在播放空动画(无帧),或者您正在播放 `startFrame` 如果动画没有框,这通常是因为 `generateFrameNames()` 或 或 时 间 `generateFrameNumbers()` 无法选择任何; 查找控制台中先前的警告 。

> 类型错误: 未定义不是对象( 正在评价“ this.anims.play ” )

你在一个被摧毁的Sprite或一个非Sprite游戏对象(黑`anims`)上玩.

> TypeError: sprite. play 不是函数

你在玩非斯普利特游戏

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)
- [samme](https://github.com/samme)

---
