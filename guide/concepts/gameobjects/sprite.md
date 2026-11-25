# 精灵 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/sprite)

斯普林特游戏对象用于在游戏中显示静态和动画图像。斯普林特可以有输入事件和物理体,也可以被调色,有色,有卷轴和动画.

斯普丽特和图像游戏对象的主要区别在于无法动画图像。因此,斯普丽特需要花费更长的时间来处理,并且由于动画组件而具有更大的API脚印。如果不需要动画,那么可以安全地使用图像来替换所有情况下的斯普丽特.

## 装入纹理 {#load-texture}

静态图像的纹理

```javascript
this.load.image(key, url);
```

参考文献: [load image](/guide/concepts/loader#image)

## 装入地图集 {#load-atlas}

动画图像的图集

```javascript
this.load.atlas(key, textureURL, atlasURL);
```

参考文献: [load atlas](/guide/concepts/loader#texture-atlas)

## 添加图示对象 {#add-sprite-object}

```javascript
var sprite = this.add.sprite(x, y, key);
// var sprite = this.add.sprite(x, y, key, frame);
```

从 JSON 添加图示

```javascript
var sprite = this.make.sprite({
    x: 0,
    y: 0,
    key: '',
    // frame: '',

    // angle: 0,
    // alpha: 1
    // flipX: true,
    // flipY: true,
    // scale : {
    //    x: 1,
    //    y: 1
    //},

    // anims: {
        // key: ,
        // repeat: ,
        // ...
    // },
    // origin: {x: 0.5, y: 0.5},
    
    add: true
});
```

- `key` :
  - 字符串
  - 随机选择一个元素的字符串阵列
- `x`, `y`, `scale.x`, `scale.y` :
  - 数字
  - 回调以获取返回值

    ```javascript
    function() { return 0; }
    ```

  - 分钟和最大值之间的随机整数

    ```javascript
    { randInt: [min, max] }
    ```

  - 分钟到最大值之间随机浮点数

    ```javascript
    { randFloat: [min, max] }
    ```

## 自定义类 {#custom-class}

- 定义类

    ```javascript
    class MySprite extends Phaser.GameObjects.Sprite {
        constructor(scene, x, y, texture, frame) {
            super(scene, x, y, texture, frame);
            // ...
            this.add.existing(this);
        }
        // ...

        // preUpdate(time, delta) {
        //     super.preUpdate(time, delta);
        // }
    }
    ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.
- 创建实例

    ```javascript
    var sprite = new MySprite(scene, x, y, key);
    ```

## 纹理 {#texture}

见[game object - texture](https://phaser.io/oss/docs/phaser/concepts/gameobjects.md#texture)

## 其他属性 {#other-properties}

见[game object](/guide/concepts/gameobjects)

## 创建遮罩 {#create-mask}

```javascript
var mask = sprite.createBitmapMask();
```

见[mask](/guide/concepts/display#masks)

## 阴影效果 {#shader-effects}

支持 [preFX and postFX effects](/guide/concepts/gameobjects/shader) 软件

## 动画 {#animation}

### 创建动画 {#create-animation}

- 适用于所有图案的全球动画

    ```javascript
    this.anims.create(config);
    ```

- 此图案的私人动画

    ```javascript
    sprite.anims.create(config);
    ```

`config` : 见 [Add animation section](/guide/concepts/animations#add-animation).

### 创建 Aeprite 动画 {#create-aseprite-animation}

- 全局所有图案的 Asprite 动画

    ```javascript
    this.anims.createFromAseprite(key, tags);
    ```

- 用于此图案的私有 Aseprite 动画

    ```javascript
    sprite.anims.createFromAseprite(key, tags);
    ```

#### 删除动画 {#remove-animation}

- 从全局动画管理器中删除

    ```javascript
    this.anims.remove(key);
    ```

    or

    ```javascript
    sprite.anims.globalRemove(key);
    ```

- 从私人动画状态删除

    ```javascript
    sprite.anims.remove(key);
    ```

#### 获得动画 {#get-animation}

- 获取全球 [animation object](/guide/concepts/animations#animation-object)

    ```javascript
    var anim = this.anims.get(key);
    ```

- 获取私人 [animation object](/guide/concepts/animations#animation-object)

    ```javascript
    var anim = sprite.anims.get(key);
    ```

#### 有动画 {#has-animation}

- 有全局动画对象

    ```javascript
    var hasAnim = this.anims.exists(key);
    ```

- 获取私人动画对象

    ```javascript
    var hasAnim = sprite.anims.exists(key);
    ```

### 播放动画 {#play-animation}

- Play

    ```javascript
    sprite.play(key);
    // sprite.play(key, ignoreIfPlaying);
    ```

  - `key`:动画密钥字符串,或动画配置
    - 动画的字符串密钥
    - 动画配置, 以覆盖默认配置

        ```javascript
        {
            key,
            frameRate,
            duration,
            delay,
            repeat,
            repeatDelay,
            yoyo,
            showOnStart,
            hideOnComplete,
            startFrame,
            timeScale
        }
        ```

- 反向播放

    ```javascript
    sprite.playReverse(key);
    // sprite.playReverse(key, ignoreIfPlaying);
    ```

  - `key`:动画密钥字符串,或动画配置
- 延迟后播放

    ```javascript
    sprite.playAfterDelay(key, delay);
    ```

  - `key`:动画密钥字符串,或动画配置
- 重复后播放

    ```javascript
    sprite.playAfterRepeat(key, repeatCount);
    ```

  - `key`:动画密钥字符串,或动画配置

### 链 {#chain}

- 链条下一张动画

    ```javascript
    sprite.chain(key);
    ```

  - `key`:动画密钥字符串,或动画配置
- 链条下一场和下一场动画

    ```javascript
    sprite.chain(key0).chain(key1);
    ```

  - `key0`,`key1`:动画密钥串,或动画配置

### 停下来 {#stop}

- 立刻停车

    ```javascript
    sprite.stop();
    ```

- 延迟后停止

    ```javascript
    sprite.stopAfterDelay(delay);
    ```

- 停止于边框

    ```javascript
    sprite.stopOnFrame(frame);
    ```

  - `frame`:当前动画中的框架对象.

    ```javascript
    var currentAnim = sprite.anims.currentAnim;
    var frame = currentAnim.getFrameAt(index);
    ```

- 重复后停止

    ```javascript
    sprite.stopAfterRepeat(repeatCount);
    ```

### 重新启动 {#restart}

```javascript
sprite.anims.restart();
// sprite.anims.restart(includeDelay, resetRepeats);
```

### 时间尺度 {#time-scale}

- Get

    ```javascript
    var timeScale = sprite.anims.globalTimeScale;
    ```

- Set

    ```javascript
    sprite.anims.globalTimeScale = timeScale;
    ```

另见 [Global time scale](/guide/concepts/animations#global-time-scale)

### 属性 {#properties}

- 已经开始

    ```javascript
    var hasStarted = sprite.anims.hasStarted;
    ```

- 正在玩游戏

    ```javascript
    var isPlaying = sprite.anims.isPlaying;
    ```

- 暂停

    ```javascript
    var isPaused = sprite.anims.isPaused;
    ```

- 框架总数

    ```javascript
    var frameCount = sprite.anims.getTotalFrames();
    ```

- Delay

    ```javascript
    var delay = sprite.anims.delay;
    ```

- Repeat
  - 重复计数总数

    ```javascript
    var repeatCount = sprite.anims.repeat;
    ```

  - 重复计数器

    ```javascript
    var repeatCount = sprite.anims.repeatCounter;
    ```

  - 重复延迟

    ```javascript
    var repeatDelay = sprite.anims.repeatDelay;
    ```

  - Yoyo

    ```javascript
    var repeatDelay = sprite.anims.yoyo;
    ```

- 当前动画密钥

    ```javascript
    var key = sprite.anims.getName();
    ```

  - `key` : 返回( E) `''` 如果没有播放任何动画。
- 当前框架名称

    ```javascript
    var frameName = sprite.anims.getFrameName();
    ```

  - `frameName` : 返回( E) `''` 如果没有播放任何动画。
- 当前动画

    ```javascript
    var currentAnim = sprite.anims.currentAnim;
    ```

- 当前框架

    ```javascript
    var currentFrame = sprite.anims.currentFrame;
    ```

### 事件 {#events}

- 开始

    ```javascript
    sprite.on('animationstart', function(currentAnim, currentFrame, sprite){});
    ```

    ```javascript
    sprite.on('animationstart-' + key, function(currentAnim, currentFrame, sprite){});
    ```

- 重新启动时

    ```javascript
    sprite.on('animationrestart', function(currentAnim, currentFrame, sprite){});
    ```

    ```javascript
    sprite.on('animationrestart-' + key, function(currentAnim, currentFrame, sprite){});
    ```

- 完成时

    ```javascript
    sprite.on('animationcomplete', function(currentAnim, currentFramee, sprite){});
    ```

    ```javascript
    sprite.on('animationcomplete-' + key, function(currentAnim, currentFramee, sprite){});
    ```

- 停车

    ```javascript
    sprite.on('animationstop', function(currentAnim, currentFrame, sprite){});
    ```

    ```javascript
    sprite.on('animationstop-' + key, function(currentAnim, currentFrame, sprite){});
    ```

- 更新

    ```javascript
    sprite.on('animationupdate', function(currentAnim, currentFrame, sprite){});
    ```

    ```javascript
    sprite.on('animationupdate-' + key, function(currentAnim, currentFrame, sprite){});
    ```

- 重复时

    ```javascript
    sprite.on('animationrepeat', function(currentAnim, currentFrame, sprite){});
    ```

    ```javascript
    sprite.on('animationrepeat-' + key, function(currentAnim, currentFrame, sprite){});
    ```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
