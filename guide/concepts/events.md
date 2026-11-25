# 事件 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/events)

事件是某个系统发送信号的一种方式,其他系统可以听然后采取行动。例如,如果玩家在游戏上点击他们的鼠标,就会在内部释放Phaser内的一系列事件。或者,如果资源加载器完成文件下载,则会释放一个相关的事件。

事件是Phaser的核心部分,你会发现它们在整个框架中被使用。它们既用于内部,用于一个系统与另一个系统交谈,也用于外部,用于您的游戏代码,用于倾听和响应。在游戏过程中,Phaser将发出数百个这样的事件。

事件总是被所谓的事件 Emitter 所释放。 Phaser 中的大多数系统和游戏对象都是事件 Emiters, 意思是它们可以直接释放事件, 你可以将事件处理器连接到它们上 。

我们之所以采用这种做法,是因为事件在网页浏览器中极为常见。大多数浏览器API都是事件驱动的,因此遵循这个模式是有意义的。这也意味着您可以通过添加自己的事件,或者听从已有的事件并响应它们,来方便地扩展Phaser。

## 事件纪念器 {#the-event-emitter}

Phaser 3使用稍作修改的[eventemitter3](https://github.com/primus/eventemitter3),作为[Phaser.Events.EventEmitter](/api/class/events-eventemitter).

- 事件名称是字符串
- 发送器选择默认上下文( `this` 值), 但听者可以覆盖此值
- 发送器选择调用参数
- `on()`与`addListener()`相同,是"  "的缩写.
- `off()`与`removeListener()`相同,是"  "的缩写.
- 无参数的`off()`与`removeAllListeners()`相同
- `off()`可以匹配事件名称;事件名称和监听器;或者事件名称,监听器,以及上下文;但不能匹配其他组合
- 第一次通话后, 添加 `once()` 的监听器会被删除

[Phaser's events](https://phaser.io/oss/docs/docs/latest/events.md)(名称,默认上下文,参数)全部在API中定义.

一些Phaser类(如Game Object)直接扩展Phaser.Events.EventEmitter,一些(如Game,Scene)在其`events`属性上持有一个发射器.

您可以在这些物体上发出并聆听自己的事件, 但不要使用任何 Phaser 事件名称( 如“ 更新 ” ) , 也不要删除不属于您的监听器。 请注意删除更多您想要的 `off()` 。

```js
// NO (removes all listeners on all events)
this.game.events.off();

// NO (removes all listeners to `step`)
this.game.events.off('step');

// YES (same arguments used on `on()`)
this.game.events.off('step', this.onStep, this);
```

记住事件发送器只是连接到其他函数。 发送器不知道或关心与监听器相关的任何状态, 由您酌情删除监听器 。

### 获取事件发送器 {#get-event-emitter}

- Scene:

    ```js
    var ee = scene.events;
    ```

- 游戏对象 :

    ```js
    var ee = gameObject;
    ```

### 附加收听器 {#attach-listener}

```js
ee.on(eventName, callback, scope);
ee.once(eventName, callback, scope);  // only fire listeners one time
```

Alias

```js
ee.addListener(eventName, callback, scope);
ee.addListener(eventName, callback, scope, true);  // only fire listeners one time
```

### 火灾事件 {#fire-event}

```js
ee.emit(eventName, parameter0, ...);
```

### 删除收听器 {#remove-listeners}

- 删除一个监听器

    ```js
    ee.off(eventName, callback, scope);
    ee.off(eventName, callback, scope, true);   // only remove one-time listeners
    ```

    or

    ```js
    ee.removeListener(eventName, callback, scope); 
    ee.removeListener(eventName, callback, scope, true);  // only remove one-time listeners
    ```

- 删除事件的监听器

    ```js
    ee.off(eventName);
    ```

    or

    ```js
    ee.removeListener(eventName); 
    ```

- 删除全部事件的监听器

    ```js
    ee.removeAllListeners();
    ```

### 获取监听器数量 {#get-listeners-count}

```js
var count = ee.listenerCount(eventName);
//var noListener = (ee.listenerCount(eventName) === 0);
```

### 获取监听器 {#get-listeners}

```js
var listeners = ee.listeners(eventName);
```

### 获取事件名称 {#get-event-names}

```js
var names = ee.eventNames();
```

### 听声音 {#listener}

```js
{
    fn: callback,
    context: scope,
    once: once
}
```

## 自定义事件发送类 {#custom-event-emitter-class}

```js
class MyEventEmitter extends Phaser.Events.EventEmitter {
    // construct() {
    //     super();
    // }

    // destroy() {
    //     super.destroy();
    // }
}
```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)
- [samme](https://github.com/samme)

---
