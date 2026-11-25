# 遮罩 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/display/masks)

Phaser具有“ 隐藏” 游戏对象的渲染能力。 遮罩允许您从渲染中“ 隐藏” 的游戏对象区域。 可用两种遮罩: 几何遮罩和比特玛普遮罩。 几何遮罩通过使用几何数据来创建遮罩。 例如, 矩形、 圆形、 椭圆形、 多边形等。 这个数据用于创建一个构成遮罩的路径。 内部, 它使用WebGL中被称为的天花板缓冲器和坎瓦斯的剪贴路径 。

Bitmap Mask 工作方式是使用纹理作为遮罩。 这种纹理可以是您喜欢的任何大小和形状, 也可以是动画, 甚至是一个视频。 纹理控制中像素的α值是屏幕上像素。 例如, α值为 0 的像素会隐藏游戏对象, 以α值为1的像素显示它。 这样您就可以创建详细的效果, 如羽毛, 使用几何遮罩是不可能的。 Bitmap Maks 是一个仅包含 WebGL 的特性 。

Phaser中的遮罩在画和定位世界空间中略为独特。 游戏对象只能有一个遮罩在任何时间应用。 但是, 如果您愿意, 您可以对多个游戏对象应用同样的遮罩。 这些遮罩不是游戏对象的特异性, 如果移动游戏对象, 遮罩将不会“ 跟踪” 。 这意味着它们需要一些谨慎的计划才能有效使用 。

## 创建遮罩对象 {#create-mask-object}

### 位图遮罩 {#bitmap-mask}

```javascript
var mask =  scene.add.bitmapMask([maskObject], [x], [y], [texture], [frame]);
```

- `maskObject`: 游戏对象或动态纹理, 将作为遮罩使用。 如果无效, 则会使用其余参数生成图像游戏对象 。
- `x`:如果创建游戏对象,则世界水平位置.
- `y`:如果创建游戏对象,则世界垂直位置.
- `texture`:如果创建游戏对象,它会用它用来渲染的纹理的键或实例,如存储在纹理管理器中.
- `frame`:如果创建游戏对象,则从此游戏对象的渲染纹理中可以选择的框架.

示例

1. 创建图像( E)[image](/guide/concepts/gameobjects/image), [sprite](/guide/concepts/gameobjects/sprite), [bitmap text](/guide/concepts/gameobjects/bitmap-text), [particles](/guide/concepts/gameobjects/particles), [text](/guide/concepts/gameobjects/text)),或 ,或 , 或 , 或 , 或 [shader](/guide/concepts/gameobjects/shader)

    ```javascript
    var shape = scene.add.image(x, y, key).setVisible(false);
    ```

2. 创建遮罩

    ```javascript
    var mask = shape.createBitmapMask();
    ```

    or

    ```javascript
    var mask = scene.add.bitmapMask(shape);
    ```

### 几何遮罩 {#geometry-mask}

遮罩本质上是一种剪辑路径,它只能使一个蒙面像素完全可见或完全看不见,而不会改变它的α(不透明).

1. 创建 [graphics](/guide/concepts/gameobjects/graphics)

    ```javascript
    var shape = scene.make.graphics();
    ```

1. 创建遮罩

    ```javascript
    var mask = shape.createGeometryMask();
    ```

## 应用遮罩对象 {#apply-mask-object}

```javascript
gameObject.setMask(mask); // image.mask = mask;
```

遮罩对象可以添加到许多游戏对象中.

!!! error
    别把游戏对象和遮罩放进 [container](/guide/concepts/gameobjects/container) 一起来
    看看这个[testing](https://codepen.io/rexrainbow/pen/mdBZJmb), 启用线路22 -24。

!!! note
    位图遮罩只有WebGL.

!!! note
    在同一游戏对象上可以结合几何遮罩和混合模式,
    但是,比特玛普遮罩不能。

## 清除遮罩 {#clear-mask}

- 清除掩码

    ```javascript
    image.clearMask();
    ```

- 清除掩码并销毁掩码对象

    ```javascript
    image.clearMask(true);
    ```

## 反转 alpha {#invert-alpha}

只有几何Mask有`inverse alpha`的特性.

- 反向阿尔法

    ```javascript
    mask.setInvertAlpha();
    // mask.invertAlpha = true;
    ```

- Disable

    ```javascript
    mask.setInvertAlpha(false);
    // mask.invertAlpha = false;
    ```

## 获取形状游戏对象 {#get-shape-game-object}

- 位图遮罩

    ```javascript
    var shape = mask.bitmapMask;
    ```

- 几何遮罩

    ```javascript
    var shape = mask.geometryMask;
    ```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
