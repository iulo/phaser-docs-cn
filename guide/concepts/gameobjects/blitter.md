# 位块传送器（Blitter） {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/blitter)

Blitter Game Object 是一类特殊容器, 用于创建、 更新和管理 Bob 对象。 Bob 是为渲染速度而不是灵活性而设计的。 它们由纹理、 或纹理、 位置和α值的帧组成。 您不能缩放或旋转它们。 在渲染速度时,它们使用批量绘图方法 。

闪光游戏对象有一个纹理绑定在它上。 闪光游戏创建的鲍勃可以使用这个纹理中的任何框架来渲染, 但是他们不能使用其他的纹理。 正是这个单一的纹理- 包, 允许它们速度 。

如果您需要将大量框架在屏幕周围爆破, 那么闪光物体就值得调查。 它们对使用自己的特效系统特别有用 。

## 装入纹理 {#load-texture}

```javascript
this.load.image(key, url);
```

参考文献: [load image](/guide/concepts/loader#image)

## 添加缓冲容器 {#add-blitter-container}

添加缓冲容器

```javascript
var blitter = this.add.blitter(x, y, key);
```

- `key` : 此游戏对象用于渲染的纹理密钥。 纹理在纹理管理器中已经存在 。

从 JSON 添加缓冲容器

```javascript
var blitter = this.make.blitter({
    x: 0,
    y: 0,
    key: '',

    // angle: 0,
    // alpha: 1
    // flipX: true,
    // flipY: true,
    // origin: {x: 0.5, y: 0.5},
    
    add: true
});
```

## 自定义类 {#custom-class}

```javascript
class MyBlitter extends Phaser.GameObjects.Blitter {
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
var blitter = new MyBlitter(scene, x, y, key);
```

## 添加 bb 对象 {#add-bob-object}

```javascript
var bob = blitter.create(x, y);
// var bob = blitter.create(x, y, frame, visible, index);
```

- `frame`: Bob 将使用的框架。 它必须是父闪点对象所使用的纹理的一部分 。
- `visible` : 创造出来的鲍勃是否应该使出?
- `index`: 布莱特斯显示列表中的位置, 以添加新的 Bob 。 默认为列表的首位 。

### 添加变形波形对象 {#add-mutiple-bob-objects}

```javascript
var bobs = blitter.createMultiple(quantity, frame, visible);
```

- `quantity` : Bob 对象的数量创建。

### 从回调中添加 bb 对象 {#add-bob-object-from-callback}

```javascript
var bobs = blitter.createFromCallback(callback, quantity, frame, visible);
// var callback = function(bob, i){};
```

## 获取 Bob 对象 {#get-bob-objects}

```javascript
var bobs = blitter.children.list;
```

## 清除所有 Bob 对象 {#clear-all-bob-objects}

```javascript
blitter.clear();
```

## 鲍勃对象 {#bob-object}

鲍勃有个位置 `alpha` 价值和a `frame` 也可以切换 Bob 的翻转和可见状态。

### 职位 {#position}

- Get

  ```javascript
  var x = bob.x;
  var y = bob.y;
  ```

- Set

  ```javascript
  bob.setPosition(x, y);
  // bob.x = 0;
  // bob.y = 0;
  ```

  or

  ```javascript
  bob.reset(x, y);
  // bob.reset(x, y, frame);
  ```

### 框架 {#frame}

- Get

  ```javascript
  var frame = bob.frame;
  ```

  - `frame` : [Frame object](/guide/concepts/textures#frames).
- Set

    ```javascript
    bob.setFrame(frame);
    ```

### 翻转 {#flip}

- Get

  ```javascript
  var flipX = bob.flipX;
  var flipY = bob.flipY;
  ```

- Set

  ```javascript
  bob.setFlip(boolX, boolY);
  // bob.setFlipX(boolean);
  // bob.setFlipY(boolean);
  // bob.flipX = flipX;
  // bob.flipY = flipY;
  ```
  
  or
  
  ```javascript
  bob.resetFlip(); // bob.setFlip(false, false)
  ```

### 可见 {#visible}

- Get
  
  ```javascript
  var visible = bob.visible;
  ```

- Set
  
  ```javascript
  bob.setVisible(boolean);
  // bob.visible = v;
  ```

### 阿尔法 {#alpha}

- Get
  
  ```javascript
  var alpha = bob.alpha;
  ```

- Set
  
  ```javascript
  bob.setAlpha(v);
  // bob.aplha = v;
  ```

### 叮当 {#tint}

- Get

  ```javascript
  var tint = bob.tint;
  ```

- Set
  
  ```javascript
  bob.setTint(tint);
  // bob.tint = tint;
  ```
  
  - `tint` : 丁值,介于之间 `0` 财务报告和已审计财务报表 `0xffffff`.

### 摧毁 {#destroy}

```javascript
bob.destroy();
```

### 数据 {#data}

```javascript
var data = bob.data;  // {}
```

## 其他属性 {#other-properties}

见[game object](/guide/concepts/gameobjects)

## 创建遮罩 {#create-mask}

```javascript
var mask = bob.createBitmapMask();
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
