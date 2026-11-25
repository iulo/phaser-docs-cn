# 平面（Plane） {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/plane)

Plane Game Object 是使用 Mesh Game Objects 并扩展其功能的帮助类, 允许快速和轻松地创建 Planes 。 Plane 是单面的单元格网格, 您可以指定每个维度的单元格数量。 Plane 可以有一个纹理, 要么在每一个单元格中重复( 平面) , 要么应用到整个 Plane 。

然后,Plane可以被3D空间操纵,并跨3轴旋转.

这使得您可以创建无法使用正则 Sprites 的效应, 例如视角扭曲。 您也可以在每顶点的基础上调整顶点。 Plante 数据成为其中的一部分 。 WebGL 批量,就像标准Sprites一样,所以不会引入任何额外的遮蔽层。因为平面板只是产生顶点进入 WebGL 批量,与其他任何Sprite一样,也可以在Plane上使用所有常见的Game Object组件,如自定义管道,掩码,混合模式或纹理.

您可以使用 `uvScroll` 和 `uvScale` 方法来调整纹理的放置和缩放, 如果此 Plane 使用单一的纹理, 而不是来自纹理图集或图示表的框 。

Plane Game Object 也有动画组件,允许您像使用Sprite一样在Plane上方播放动画。动画框的尺寸必须固定,因为第一个帧将是整个动画的大小,例如使用 `SpriteSheet` 。

注意Plane对象仅为WebGL,没有Canvas对应物.

飞机的原产地始终是0.5×0.5,而且_不能更改_.

## 装入纹理 {#load-texture}

```javascript
this.load.image(key, url);
```

参考文献: [load image](/guide/concepts/loader#image)

## 添加平面对象 {#add-plane-object}

```javascript
var plane = this.add.plane(x, y, key);
// var plane = this.add.plane(x, y, key, frame);
// var plane = this.add.plane(x, y, texture, frame, width, height, tile);
```

- `x`, `y` : 位置
- `key`,`frame`: 纹理键为
- `width`,`height`:本平面宽度/高度,**在单元格**,不像素.
- `tile` :纹理是否铺设?

从 JSON 添加平面

```javascript
var plane = this.make.plane({
    x: 0,
    y: 0,
    key: '',
    // frame: '',
    // width: 8,
    // height: 8,
    // tile: false,
    // checkerboard: null,
    // checkerboard: { color1, color2, alpha1, alpha2, height }

    // angle: 0,
    // alpha: 1,
    // scale : {
    //    x: 1,
    //    y: 1
    //},
    // origin: {x: 0.5, y: 0.5},

    add: true
});
```

## 自定义类 {#custom-class}

- 定义类

    ```javascript
    class MyPlane extends Phaser.GameObjects.Plane {
        constructor(scene, x, y, texture, frame, width, height, tile) {
            super(scene, x, y, texture, frame, width, height, tile);
            // ...
            this.add.existing(this);
        }
        // ...

        // preUpdate(time, delta) {}
    }
    ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.
- 创建实例

    ```javascript
    var plane = new MyPlane(scene, x, y, texture, frame, width, height, tile);
    ```

## 纹理 {#texture}

见[game object - texture](/guide/concepts/gameobjects#textures)

## 动画 {#animation}

见[Sprite's animation section](/guide/concepts/gameobjects/sprite#animation).

### 播放动画 {#play-animation}

- Play

    ```javascript
    plane.play(key);
    // plane.play(key, ignoreIfPlaying);
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
    plane.playReverse(key);
    // plane.playReverse(key, ignoreIfPlaying);
    ```

  - `key`:动画密钥字符串,或动画配置
- 延迟后播放

    ```javascript
    plane.playAfterDelay(key, delay);
    ```

  - `key`:动画密钥字符串,或动画配置
- 重复后播放

    ```javascript
    plane.playAfterRepeat(key, repeatCount);
    ```

  - `key`:动画密钥字符串,或动画配置

### 停下来 {#stop}

- 立刻停车

    ```javascript
    plane.stop();
    ```

- 延迟后停止

    ```javascript
    plane.stopAfterDelay(delay);
    ```

- 停止于边框

    ```javascript
    plane.stopOnFrame(frame);
    ```

  - `frame`:当前动画中的框架对象.

    ```javascript
    var currentAnim = plane.anims.currentAnim;
    var frame = currentAnim.getFrameAt(index);
    ```

- 重复后停止

    ```javascript
    plane.stopAfterRepeat(repeatCount);
    ```

### 属性 {#properties}

- 已经开始

    ```javascript
    var hasStarted = plane.anims.hasStarted;
    ```

- 正在玩游戏

    ```javascript
    var isPlaying = plane.anims.isPlaying;
    ```

- 暂停

    ```javascript
    var isPaused = plane.anims.isPaused;
    ```

- 框架总数

    ```javascript
    var frameCount = plane.anims.getTotalFrames();
    ```

- Delay

    ```javascript
    var delay = plane.anims.delay;
    ```

- Repeat
  - 重复计数总数

    ```javascript
    var repeatCount = plane.anims.repeat;
    ```

  - 重复计数器

    ```javascript
    var repeatCount = plane.anims.repeatCounter;
    ```

  - 重复延迟

    ```javascript
    var repeatDelay = plane.anims.repeatDelay;
    ```

  - Yoyo

    ```javascript
    var repeatDelay = plane.anims.yoyo;
    ```

- 当前动画密钥

    ```javascript
    var key = plane.anims.getName();
    ```

  - `key` : 返回( E) `''` 如果没有播放任何动画。
- 当前框架名称

    ```javascript
    var frameName = plane.anims.getFrameName();
    ```

  - `frameName` : 返回( E) `''` 如果没有播放任何动画。
- 当前动画

    ```javascript
    var currentAnim = plane.anims.currentAnim;
    ```

- 当前框架

    ```javascript
    var currentFrame = plane.anims.currentFrame;
    ```

## 交互式 {#interactive}

测试指针是否位于此网格游戏对象的任意一面.

```javascript
plane.setInteractive();
```

## 跳棋游戏 {#checkerboard}

创建一个检查板样式纹理,
以给定的颜色和α值为基础,并将其应用到这个 Plane,
替换它可能拥有的任何当前纹理。

- Create

    ```javascript
    plane.createCheckerboard(color1, color2, alpha1, alpha2, height)
    ```

- Remove

    ```javascript
    plane.removeCheckerboard();
    ```

## 其他属性 {#other-properties}

见[Mesh game object](/guide/concepts/gameobjects/mesh),[game object](/guide/concepts/gameobjects).

## 创建遮罩 {#create-mask}

```javascript
var mask = plane.createBitmapMask();
```

见[mask](/guide/concepts/display#masks)

## 阴影效果 {#shader-effects}

支持 [postFX effects](/guide/concepts/gameobjects/shader) 软件

!!! note
    无 preFX 效果支持

## 作者的信用额度 {#author-credits}

本页的内容包括下列工作:

- [RexRainbow](https://github.com/rexrainbow)

---
