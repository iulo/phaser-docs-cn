# 图像 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/image)

图像是用于在游戏中显示静态图像的轻量级游戏对象,例如标识,背景,景色或其他非动画元素. 图像可以有输入事件和物理体,或者被调色,有色或滚动. 图像和Sprite的主要区别在于,由于没有动画组件,无法给图像动画.

## 装入纹理 {#load-texture}

```javascript
this.load.image(key, url);
```

参考文献: [load image](/guide/concepts/loader#image)

## 添加图像对象 {#add-image-object}

```javascript
var image = this.add.image(x, y, key);
// var image = this.add.image(x, y, key, frame);
```

从 JSON 添加图像

```javascript
var image = this.make.image({
    x: 0,
    y: 0,
    key: '',
    // frame: '',

    // angle: 0,
    // alpha: 1,
    // flipX: true,
    // flipY: true,
    // scale : {
    //    x: 1,
    //    y: 1
    //},
    // origin: {x: 0.5, y: 0.5},

    add: true
});
```

- `key`, `frame` :
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

```javascript
class MyImage extends Phaser.GameObjects.Image {
    constructor(scene, x, y, texture, frame) {
        super(scene, x, y, texture, frame);
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

示例

```javascript
var image = new MyImage(scene, x, y, key);
```

## 纹理 {#texture}

见[game object - texture](/guide/concepts/gameobjects#textures)

## 其他属性 {#other-properties}

见[game object](/guide/concepts/gameobjects)

## 创建遮罩 {#create-mask}

```javascript
var mask = image.createBitmapMask();
```

见[mask](/guide/concepts/display#masks)

## 阴影效果 {#shader-effects}

支持 [preFX and postFX effects](/guide/concepts/gameobjects/shader) 软件

## 作者的信用额度 {#author-credits}

本页的内容包括下列工作:

- [RexRainbow](https://github.com/rexrainbow)

---
