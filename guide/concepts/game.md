# 游戏 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/game)

如果你看看任何 Phaser 的例子,你会看到它们都创造了 Phaser.Game 的例。事实上,没有它,就没有什么会发生。这个课可以被视为你游戏的核心,因为没有它,就没有什么能运行了。

通常情况下, 您在任何特定时间都只有过一次 Phaser 游戏。 游戏类本身没有做很多事情, 除了创建, 您很少与它互动。 然而它负责创建和更新您游戏执行时需要的所有内部系统 。

即使你正在创造包含许多较小游戏的游戏类型(认为是马里奥党,或沃里奥·沃雷),你仍然只能有一次Phaser游戏类本身.

## 创建基本的 Phaser 游戏实例 {#creating-a-basic-phaser-game-instance}

```js
new Phaser.Game({
  scene: {
    create: function () {
      this.add.text(0, 0, 'Hello world');
    }
  }
});
```

游戏创作前不需要等待[DOMContentLoaded](https://developer.mozilla.org/en-US/docs/Web/API/Window/DOMContentLoaded_event)或[window.onload](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event).

但是,如果您有外部样式表或图像影响页面布局,并且您正在使用缩放管理器,您可能需要使用[window.onload](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event).

游戏作为`this.game`在所有场景中都可以使用,并作为参数传递给相关的回调和事件监听器,因此通常不需要保存游戏的引用,除非需要从外部Phaser联系到游戏.

## 游戏配置 {#game-configuration}

- 基本游戏配置对象 :

    ```js
    const config = {
        type: Phaser.AUTO, // automatically detect browser WebGL support
        width: 800, // canvas width
        height: 600, // canvas height
        backgroundColor: '#2d2d2d', // canvas background color
        parent: 'phaser-example', // parent DOM element
        scene: Example // 
    };
    ```

- [Game config examples](https://labs.phaser.io/index.html?dir=game%20config/&q=)

您可以阅读完整列表 [config options here](/api/typedef/types-core#gameconfig)。由于历史原因,一些配置值可以设置在两个地方:例如, `width` 财务报告和已审计财务报表 `height` 与 `scale.width` 财务报告和已审计财务报表 `scale.height`.

对于大多数情况,你应该直接在游戏配置中添加场景和任何插件,因为这是最简单的方法.

任何特殊的启动工作通常都应该在`preBoot`或`postBoot`回调中完成.

`preBoot`只在[DOMContentLoaded](https://developer.mozilla.org/en-US/docs/Web/API/Window/DOMContentLoaded_event)之后运行. `game.config`和`game.device`是可用的. ** 有些** `game.config`值在这里仍然可以修改,大多数游戏系统还没有设置,你可以在这里添加场景,游戏中的[BOOT](/api/event/core-events#boot)事件大约在同一时间发生.

`postBoot`在所有游戏系统都准备好了之后运行。游戏的[READY](/api/event/core-events#ready)事件大约在同一时间发生。任何在此之前添加的场景(非待决),如果设定要运行,则开始运行 。

游戏循环在`postBoot`之后立即开始.

```js
const config = {
    preBoot: function (game) {
      // Config (including defaults) has been created.
      console.log('game config' game.config);
    },
    postBoot: function (game) {
      // Game canvas has been created.
      console.log('game canvas', game.canvas);
    }
};

const game = new Phaser.Game(config);
```

## 全球成员 {#global-members}

### 场景管理器 {#scene-manager}

环球[scene manager](/guide/concepts/scenes)在`game.scene`,或每场的`scene.scene`.

### 数据管理器 {#data-manager}

例[data manager](/guide/concepts/data-manager)在`game.registry`,或每场的`scene.registry`.

- 获取数据管理器 :

    ```javascript
    var value = scene.registry.get(key);
    // var value = game.registry.get(key);
    ```

- 在数据管理器中添加/更新数据 :

    ```javascript
    scene.registry.set(key, value);
    // game.registry.set(key, value);
    ```

- 事件
  - 设置数据事件 :

    ```javascript
    scene.registry.events.on('setdata', function(parent, key, value){ /* ... */ });
    // game.registry.events.on('setdata', function(parent, key, value){ /* ... */ })
    ```

  - 更改数据事件 :

    ```javascript
    scene.registry.events.on('changedata', function(parent, key, value, previousValue){ /* ... */ });
    // game.registry.events.on('changedata', function(parent, key, value, previousValue){ /* ... */ })
    ```

    ```javascript
    scene.registry.events.on('changedata-' + key, function(parent, value, previousValue){ /* ... */ });
    // game.registry.events.on('changedata-' + key, function(parent, value, previousValue){ /* ... */ });
    ```

### 游戏时间 {#game-time}

- 当前游戏步骤开始的时间 。

    ```javascript
    var time = game.getTime();
    // var time = scene.game.getTime();
    ```

- 现游戏框.

    ```javascript
    var frameCount = game.getFrame();
    // var frameCount = scene.game.getFrame();
    ```

- 三角洲时间, 自游戏最后一步以来。 这是一个被夹住和平滑的平均值 。

    ```javascript
    var delta = game.loop.delta;
    // var delta = scene.game.loop.delta;
    ```

### 游戏配置 {#game-config}

```javascript
var config = game.config;
// var config = scene.game.config;
```

### 窗口大小 {#window-size}

- 窗口宽度 :

    ```javascript
    var width = game.config.width;
    // var width = scene.game.config.width;
    ```

- 窗口高度 :

    ```javascript
    var height = game.config.height;
    // var height = scene.game.config.height;
    ```

## 暂停并恢复 {#pause-and-resume}

您可以暂停或恢复整个游戏, 使用其 `pause()` 和 `resume()` 方法。 您无法从 Phaser 的输入事件恢复游戏, 因为这些事件也暂停了 。

- 暂停整个游戏,并发出一个`PAUSE`事件.

    ```javascript
    game.pause();
    ```

- 继续整个游戏,并发出一个`RESUME`事件.

    ```javascript
    game.resume();

    ```

- 暂停

    ```javascript
    var isPaused = game.isPaused;
    ```

## 事件 {#events}

[Game events](/api/event/core-events)是游戏的`events`发射出来的.

`FOCUS`和`BLUR`发生于游戏窗口或帧通过用户鼠标点击或按键获得或失去焦点时.

`HIDDEN` 财务报告和已审计财务报表 `VISIBLE` 当游戏标签或窗口被隐藏、切换、最小化或恢复时,则发生 [Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API)。操作系统在此可有所不同。 `PAUSE` 财务报告和已审计财务报表 `RESUME` 事件通常同时发生.

你可以在这个发射器上发出并听自己的事件,只要你避开Phaser的事件名称.

- 暂停(窗口是隐形的) / 恢复(窗口是可见的) 事件

    ```javascript
    game.events.on('pause', function() {});
    ```

    ```javascript
    game.events.on('resume', function() {});
    ```

- 由 `game.destroy()` 触发的销毁事件

    ```javascript
    game.events.on('destroy', function() {})
    ```

- 窗口焦点/乱七八糟的活动

    ```javascript
    game.events.on('focus', function() {})
    ```

    ```javascript
    game.events.on('blur', function(){ })
    ```

## 书记官处 {#registry}

注册是游戏的[data store](https://github.com/samme/phaser3-faq/wiki/Data).

无法直接通过游戏配置传递注册数据,但可以在回调中完成: .

```js
const config = {
    callbacks: {
    preBoot: function (game) {
      game.registry.merge({
        highScore: 0
      });
    }
  }
};

const game = new Phaser.Game(config);
```

## 系统 {#systems}

| 游戏       | 场景           | 说明           | 页:1                                         |
| ---------- | --------------- | --------------------- | --------------------------------------------- |
| `anims`    | `anims`         | 动画管理器     |                                               |
| `cache`    | `cache`         | 快取管理器         |                                               |
| `device`   | `game.device`   | 设备记录         |                                               |
| `events`   | `game.events`   | 全球活动发射器 | 现场的`events`是它自己的发射装置.      |
| `input`    | `input.manager` | 输入管理器         | 使用现场的输入插件 `input`代替. |
| `loop`     | `game.loop`     | 游戏循环         |                                               |
| `plugins`  | `plugins`       | 插件管理器       |                                               |
| `registry` | `registry`      | 全球登记册       |                                               |
| `renderer` | `renderer`      | 渲染器              |                                               |
| `scale`    | `scale`         | 缩放管理器         |                                               |
| `scene`    | `scene.manager` | 场景管理器         | 换成现场的场景插件`scene`. |
| `sound`    | `sound`         | 声音管理器         |                                               |
| `textures` | `textures`      | 纹理管理器       |                                               |

## 正在破坏游戏实例 {#destroying-the-game-instance}

```javascript
game.destroy();
// game.destroy(removeCanvas, noReturn);
```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)
- [samme](https://github.com/samme)

---
