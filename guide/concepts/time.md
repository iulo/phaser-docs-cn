# 时间 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/time)

每个场景都有时钟类的实例。 它负责跟踪时间、 三角洲时间和其他时间相关值。 它还允许您创建时钟事件, 即特定时间过后发生的火灾。 例如, 您可以创建一个时钟事件, 5秒或10秒或1分钟后开火。 您也可以创建重复的时钟事件, 如每5秒或每10秒。

属于一个场景的时钟被所有场景系统,如tweens和声音等使用,它也被游戏对象使用,如Sprite动画系统,这意味着所有这些系统都与同一个时钟同步。您具有单个时钟的“缩放”时间的能力,从而减速,或者加速系统在单个场景范围内运行。

## 计时器 {#timer}

超时时执行调用, Phaser的内置对象 。

### 开始计时器 {#start-timer}

- 循环计时器

  ```js
  var timer = this.time.addEvent({
    delay: 500, // ms
    callback: callback,
    //args: [],
    callbackScope: thisArg,
    loop: true,
  });
  ```

- 重复计时器

  ```js
  var timer = this.time.addEvent({
    delay: 500, // ms
    callback: callback,
    //args: [],
    callbackScope: thisArg,
    repeat: 4,
  });
  ```

- 延迟计时器

  ```js
  var timer = this.time.delayedCall(delay, callback, args, scope); // delay in ms
  ```

- 计时器的所有属性

  ```js
  var timer = this.time.addEvent({
    delay: 500, // ms
    callback: callback,
    args: [],
    callbackScope: thisArg,
    loop: false,
    repeat: 0,
    startAt: 0,
    timeScale: 1,
    paused: false,
  });
  ```

- 重置和再利用计时器

  ```js
  timer.reset({
    delay: 500, // ms
    callback: callback,
    args: [],
    callbackScope: thisArg,
    loop: false,
    repeat: 0,
    startAt: 0,
    timeScale: 1,
    paused: false,
  });
  this.time.addEvent(timer);
  ```

!!! note
丢弃错误消息( 如果 `delay : 0` 与( )`repeat > 0` 或 或 时 间 `loop: true`)

### 暂停/恢复 {#pauseresume}

- 暂停计时器

  ```js
  timer.paused = true;
  ```

- 恢复计时器

  ```js
  timer.paused = false;
  ```

- 暂停

  ```js
  var isPaused = timer.paused;
  ```

### 停止计时器 {#stop-timer}

- 停止运行的计时器

  ```js
  timer.remove();
  ```

- 从时间线中删除全部内部列表, 以供计时器重用

  ```js
  this.time.removeEvent(timer);
  ```

### 时间尺度 {#time-scale}

使用乘数缩放定时器 。

- Set

  ```js
  timer.timeScale = 0.5; // half speed
  //timer.timeScale = 2; // double speed
  ```

- Get

  ```js
  var timeScale = timer.timeScale;
  ```

### 其他属性 {#other-properties}

- 时间过长

  ```js
  var elapsed = timer.getElapsed(); // ms
  var elapsed = timer.getElapsedSeconds(); // sec
  // var elapsed = timer.elapsed;  // ms
  ```

- 获得剩下的时间

  ```js
  var remaining = timer.getRemaining(); // ms
  var remaining = timer.getRemainingSeconds(); // sec
  // var remaining = timer.getOverallRemaining();   // ms
  // var remaining = timer.getOverallRemainingSeconds(); // sec
  ```

- 重复计数

  ```js
  var repeat = timer.getRepeatCount();
  ```

- 获取当前迭代的进度

  ```js
  var progress = timer.getProgress(); // elapsed / delay
  ```

- 获得计时器的总体进度,计入重复。

  ```js
  var progress = timer.getOverallProgress(); // totalElapsed / totalDuration
  ```

- 获取延迟时间

  ```js
  var delay = timer.delay; // ms
  ```

## 时间线 {#timeline}

时光线是未来特定时间调用回调,事件和其他动作运行的一种方式,是一个景层系统,指每个时光线属于自己的景层,可以在同一景点同时使用多个时线运行.

如果暂停了场景, 时间线也会暂停。 如果破坏场景, 时间线会自动被销毁。 然而, 您可以直接控制时间线, 拖动、 恢复和停止它 。

### 创建时间 {#create-timeline}

```js
var timeline = this.add.timeline([
    {
        // Time condition
        at: 0,
        in:
        from:

        // Enable condition
        if(event) {
            // this: target parameter
            return true;  // false
        },

        set: {
            key: value,
        },

        tween: {
            targets: gameObject,
            alpha: 1,
            ease: 'Linear',       // 'Cubic', 'Elastic', 'Bounce', 'Back'
            duration: 1000,
            repeat: 0,            // -1: infinity
            yoyo: false
        },

        run(){
            // this: target parameter
        },

        loop() {

        },

        sound: '',

        event: '',

        // target: this,

        // once: false,
        // stop: false,
    },

    // ...
])
```

- Time :
  - `at` : 开始于毫秒后绝对延迟时间。
  - `in`: 在当前时间之后绝对延迟时间,以毫秒计。
  - `from` : 上一个事件之后的相对延迟时间, 以毫秒计
- Enable :
  - `if`: 一个函数。 引用每个勾选, 返回 `true`时运行动作 。
- Actions :

  - `set`:一个要设置在`target`上的属性的键值对象.
  - `tween` : [tween config](/guide/concepts/tweens#creating-a-tween)
  - `run` : 事件发生时将称为函数。

    ```js
    function() {
        // this: target parameter
    }
    ```

  - `loop` : 当事件序列再次重复时, 函数将调用 。

    ```js
    function() {
        // this: target parameter
    }
    ```

  - `sound` :

    - 字符串:要播放的音效管理器的键
    - 当事件发生时要播放声音的配置对象 。

      ```js
      {
        key, config;
      }
      ```

      - `key`:要播放的音响的键
      - `config` : [config of playing sound](/guide/concepts/audio#configuration)

  - `event`: 事件发生时以字符串为基础的事件名称。 事件由时间线实例释放 。

    ```js
    timeline.on(eventName);
    ```

  - `target`:用于引用`run`的瞄准镜(`this`对象).

- Control
  - `once`:如果设定,活动在开火时会从时间线上移除.
  - `stop` : 如果设定, 时间线将会在本次事件起火时停止并进入完整状态, 即使事件之后还有其他事件.

时行常起暂停.

### 命令步骤 {#steps-of-commands}

每一个勾选,每个命令:

1. 测试时间( 4月 4月 4月 5月 4日)`at`, `in`, `from`)
1. 测试启用( `if`)
1. 运行动作( R)`set`, `tween`, `run`, `sound`, `event`)
1. 控制( 4)`once`, `stop`)

### 开始 {#start}

```js
timeline.play();
```

#### 重新启动 {#restart}

```js
timeline.play(true);
```

#### 以重复开始 {#start-with-repeat}

- 重复无限

  ```js
  timeline.repeat().play();
  // timeline.repeat(true).play();
  // timeline.repeat(-1).play();
  ```

- 重复次数

  ```js
  timeline.repeat(amount).play();
  ```

  - `amount`:一个正数

- 无重复

  ```js
  timeline.repeat(false);
  ```

- 当前循环计数器

  ```js
  var loopCounter = timeline.iteration;
  ```

### 停下来 {#stop}

```js
timeline.stop();
```

### 暂停/ 恢复 {#pause-resume}

```js
timeline.pause();
// timeline.paused = true;
```

```js
timeline.resume();
// timeline.paused = false;
```

### 重置 {#reset}

将这个时间线重新放回开始,包括循环计数器.

如果时间线有任何事件被设定为`once` 已经删除,
他们称此方法后,将不再出席。

```js
timeline.reset();
```

如果时间线目前没有运行(即暂停或完成),则
调用这种方法重置这些状态, 和调用 `Timeline.play(true)`( 重新开始) 相同 。

### 添加命令 {#add-command}

```js
timeline.add(config);
```

or

```js
timeline.add([config0, config1, ...]);
```

### 清除所有命令 {#clear-all-commands}

```js
timeline.clear();
```

### 事件 {#events}

- 完成所有命令

  ```js
  timeline.on("complete", function () {});
  ```

### 其他属性 {#other-properties-1}

- 时间线正在播放,没有暂停或不完整 。

  ```js
  var isPlaying = timeline.isPlaying();
  ```

- 暂停

  ```js
  var isPaused = timeline.paused;
  ```

- 所有命令都完成 。

  ```js
  var isCompleted = timeline.complete;
  ```

### 摧毁 {#destroy}

同时删除更新 。

```js
timeline.destroy();
```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
