# 显示 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/display)

## 混合模式 {#blend-mode}

控制渲染时纹理与背景的混合。 设置混合模式会影响图示或游戏对象的颜色与后面像素的颜色的结合。

混合模式在 Canvas 和 WebGL 下,以及浏览器到浏览器之间, 取决于支持, 混合模式在遇到新的混合模式时也会产生 WebGL 批量冲洗。 由于这些原因, 请注意您所构建的场景和使用混合模式的频率 。

### WebGL 和彩色画 {#webgl-and-canvas}

- `'NORMAL'`,或 ,或 , `Phaser.BlendModes.NORMAL`,或 ,或 , `0`
  - 默认设置和绘制新形状, 覆盖现有画布内容 。
- `'ADD'`,或 ,或 , `Phaser.BlendModes.ADD`,或 ,或 , `1`
  - 在两种形状重叠的情况下,颜色通过添加颜色值来确定.
- `'MULTIPLY'`,或 ,或 , `Phaser.BlendModes.MULTIPLY`,或 ,或 , `2`
  - 像素属于顶层,与底层相应的像素相乘,结果为更暗的图片.
- `'SCREEN'`,或 ,或 , `Phaser.BlendModes.SCREEN`,或 ,或 , `3`
  - 像素是倒数,乘数,再反数,一个较轻的图片就是结果(对乘数)
- `'ERASE'`,或 ,或 , `Phaser.BlendModes.ERASE`,或 ,或 , `17`
  - Alpha 擦除混合模式。 只有在向帧缓冲器渲染时才有效, 如 * 渲染纹理 *

### 仅限画板 {#canvas-only}

- `'OVERLAY'`,或 ,或 , `Phaser.BlendModes.OVERLAY`,或 ,或 , `4`
  - 复数和屏幕的结合,底层上的暗部分变暗,光部分变轻.
- `'DARKEN'`,或 ,或 , `Phaser.BlendModes.DARKEN`,或 ,或 , `5`
  - 保留两层最黑暗的像素。
- `'LIGHTEN'`,或 ,或 , `Phaser.BlendModes.LIGHTEN`,或 ,或 , `6`
  - 保留两层最轻的像素.
- `'COLOR_DODGE'`,或 ,或 , `Phaser.BlendModes.COLOR_DODGE`,或 ,或 , `7`
  - 将底层除以倒数顶层。
- `'COLOR_BURN'`,或 ,或 , `Phaser.BlendModes.COLOR_BURN`,或 ,或 , `8`
  - 将倒转的底层除以顶层,然后反转结果。
- `'HARD_LIGHT'`,或 ,或 , `Phaser.BlendModes.HARD_LIGHT`,或 ,或 , `9`
  - 混合了倍数和屏幕,如覆面,但上层和下层互换.
- `'SOFT_LIGHT'`,或 ,或 , `Phaser.BlendModes.SOFT_LIGHT`,或 ,或 , `10`
  - 较软的硬灯版本,纯黑或白不会产生纯黑或白.
- `'DIFFERENCE'`,或 ,或 , `Phaser.BlendModes.DIFFERENCE`,或 ,或 , `11`
  - 从顶层或反方向切换下层,以获得一个正值。
- `'EXCLUSION'`,或 ,或 , `Phaser.BlendModes.EXCLUSION`,或 ,或 , `12`
  - 和不同,但对比较低
- `'HUE'`,或 ,或 , `Phaser.BlendModes.HUE`,或 ,或 , `13`
  - 保留底层的露马和染色体,同时采用顶层的花蕾.
- `'SATURATION'`,或 ,或 , `Phaser.BlendModes.SATURATION`,或 ,或 , `14`
  - 保留底层的露马和花蕾,同时采用顶层的染色体.
- `'COLOR'`,或 ,或 , `Phaser.BlendModes.COLOR`,或 ,或 , `15`
  - 保留底层的露米,同时采用顶层的乳腺和铬.
- `'LUMINOSITY'`,或 ,或 , `Phaser.BlendModes.LUMINOSITY`,或 ,或 , `16`
  - 保留底层层的乳腺和铬,同时采用顶层的乳腺.
- `'SOURCE_IN'`,或 ,或 , `Phaser.BlendModes.SOURCE_IN`,或 ,或 , `18`
  - 新的形状只有在新形状和目的地画布重叠时才画出来。其他的都透明。
- `'SOURCE_OUT'`,或 ,或 , `Phaser.BlendModes.SOURCE_OUT`,或 ,或 , `19`
  - 新形状绘制时不与现有的画布内容重叠.
- `'SOURCE_ATOP'`,或 ,或 , `Phaser.BlendModes.SOURCE_ATOP`,或 ,或 , `20`
  - 新形状只画在与现有画布内容重叠的地方.
- `'DESTINATION_OVER'`,或 ,或 , `Phaser.BlendModes.DESTINATION_OVER`,或 ,或 , `21`
  - 在现有画布内容后面绘制新的形状。
- `'DESTINATION_IN'`,或 ,或 , `Phaser.BlendModes.DESTINATION_IN`,或 ,或 , `22`
  - 现有的画布内容保存在新形状和现有的画布内容重叠的地方。其他内容都透明。
- `'DESTINATION_OUT'`,或 ,或 , `Phaser.BlendModes.DESTINATION_OUT`,或 ,或 , `23`
  - 现存内容保存在不与新形状重叠的地方.
- `'DESTINATION_ATOP'`,或 ,或 , `Phaser.BlendModes.DESTINATION_ATOP`,或 ,或 , `24`
  - 现有的画布只保存在与新形状重叠的地方。新形状在画布内容后面绘制。
- `'LIGHTER'`,或 ,或 , `Phaser.BlendModes.LIGHTER`,或 ,或 , `25`
  - 在两种形状重叠的情况下,颜色通过添加颜色值来确定.
- `'COPY'`,或 ,或 , `Phaser.BlendModes.COPY`,或 ,或 , `26`
  - 仅显示新形状 。
- `'XOR'`,或 ,或 , `Phaser.BlendModes.XOR`,或 ,或 , `27`
  - 形状在其他地方都重叠和正常地画出来时,是透明的。

## 颜色 {#color}

彩色类持有单一的彩色值,并允许轻松修改和阅读.

### 获得颜色整数 {#get-color-integer}

- 十六进制字符串, 或颜色整数

    ```javascript
    var color = Phaser.Display.Color.ValueToColor(input);
    ```

  - `input` : 十六进制字符串,或颜色整数
- RGB 到颜色

    ```javascript
    var color = Phaser.Display.Color.GetColor(red, green, blue);
    ```

  - `red`, `green`, `blue` : 0 ~ 255
- RGBA 颜色

    ```javascript
    var color = Phaser.Display.Color.GetColor32(red, green, blue, alpha);
    ```

  - `red`, `green`, `blue`, `alpha` : 0 ~ 255
- 十六进制字符串为颜色

    ```javascript
    var color = Phaser.Display.Color.HexStringToColor(hex).color;
    ```

  - 十六进制 : `#0033ff`, `#03f`, `0x0033ff`,或 ,或 , `0x03f`
- RGB 字符串为颜色

    ```javascript
    var color = Phaser.Display.Color.RGBStringToColor(rgb);
    ```

  - rgb: `'rgb(r,g,b)'`,或称 `'rgba(r,g,b,a)'`.
    - r, g, b: 0~ 255
    - a : 0 ~ 1
- HSV 改为颜色

    ```javascript
    var color = Phaser.Display.Color.HSVToRGB(h, s, v).color;
    ```

  - `h`, `s`, `v` : 0 ~ 1

### 颜色整数到 RGB {#color-integer-to-rgb}

```javascript
var rgb = Phaser.Display.Color.IntegerToRGB(color);
```

- `color` : 颜色整数 (`0xAARRGGBB`)
- `rgb` : JSON对象( 以`{r, g, b, a}`)

### HSV 彩色轮 {#hsv-color-wheel}

1. 创建颜色阵列

    ```javascript
    var colorArray = Phaser.Display.Color.HSVColorWheel(s, v);
    ```

1. 获取颜色

    ```javascript
    var color = colorArray[i].color;  // i : 0 ~ 359
    ```

### 颜色对象 {#color-object}

#### 创建颜色对象 {#create-color-object}

- 通过 r,g,b,a 组件创建

    ```javascript
    var color = new Phaser.Display.Color(red, green, blue); // alpha = 255
    // var color = new Phaser.Display.Color(red, green, blue, alpha);
    ```

  - `red`, `green`, `blue`, `alpha`: 0 ~ 255
- 通过颜色整数创建

    ```javascript
    var color = Phaser.Display.Color.IntegerToColor(colorInteger);
    ```

  - colorInteger : 颜色整数 (`0xAARRGGBB`)

#### 设定颜色 {#set-color}

- 设定颜色

    ```javascript
    color.setTo(red, green, blue);  // alpha = 255
    // color.setTo(red, green, blue, alpha);
    ```

  - `red`, `green`, `blue`, `alpha`: 0 ~ 255
- 以 GL 值设置颜色

    ```javascript
    color.setGLTo(red, green, blue);  // alpha = 1
    // color.setTo(red, green, blue, alpha);
    ```

  - `red`, `green`, `blue`, `alpha`: 0 ~ 1
- 从颜色对象设置颜色

    ```javascript
    color.setFromRGB(rgba);
    ```

  - rgba :

    ```javascript
    {
        r: 0,
        g: 0,
        b: 0,
        // a: 0
    }
    ```

- 从 HSV 设置颜色

    ```javascript
    color.setFromHSV(h, s, v);
    ```

- 设置为透明( )

    ```javascript
    color.transparent();
    ```

  - 设定( 红色、 绿色、 蓝色) 到 `0`
- 设置为灰色

   ```javascript
   color.gray(value);
   ```

- 设置为随机颜色

    ```javascript
    color.random();
    ```

    or

    ```javascript
    color.random(min, max);
    ```

  - `min`: 0~255. 默认值为0.
  - `max`: 0~255,默认值为255.
- 设置为随机灰色

    ```javascript
    color.randomGray();
    ```

    or

    ```javascript
    color.randomGray(min, max);
    ```

- 设置红/绿/蓝/阿尔法通道: 0~ 255

    ```javascript
    color.red = value;
    // color.red += value;
    color.green = value;
    // color.green += value;
    color.blue = value;
    // color.blue += value;
    color.alpha = value;
    // color.alpha += value;
    ```

- 设置 H/S/V 频道: 0~ 1

    ```javascript
    color.h = value;
    // color.h += value;
    color.s = value;
    // color.s += value;
    color.v = value;
    // color.v += value;
    ```

- 设定正态的红色、绿色、蓝色、 α : 0~ 1

    ```javascript
    color.redGL = value;
    // color.redGL += value;
    color.greenGL = value;
    // color.greenGL += value;
    color.blueGL = value;
    // color.blueGL += value;
    color.alphaGL = value;
    // color.alphaGL += value;
    ```

- 设置亮度

    ```javascript
    color.brighten(value);
    ```

  - `value`: 百分比,0~100
- 饱和 : 将此颜色的饱和度( S) 增加给定的百分比量 。

    ```javascript
    color.saturate(value);
    ```

  - `value`: 百分比,0~100
- 饱和 : 将此颜色的饱和度( S) 减少给定的百分比量。

    ```javascript
    color.desaturate(value);
    ```

  - `value`: 百分比,0~100
- 亮度 : 以给定的百分比数增加此颜色的亮度( V) 。

    ```javascript
    color.lighten(value);
    ```

  - `value`: 百分比,0~100
- 暗:用给定的百分比数来减少此颜色的亮度( V) 。

    ```javascript
    color.darken(value);
    ```

  - `value`: 百分比,0~100

#### 属性 {#properties}

- RGB 颜色,不包括α通道

    ```javascript
    var c = color.color;
    ```

- RGB Color,包括α通道.

    ```javascript
    var c = color.color32;
    ```

- 可用于 CSS 颜色值的 RGB 颜色字符串 。

    ```javascript
    var c = color.rgba;
    ```

- 红、绿、蓝、阿尔法:0~255

    ```javascript
    var r = color.red;
    var g = color.green;
    var b = color.blue;
    var a = color.alpha;
    ```

- 高、西、五:0~1

    ```javascript
    var h = color.h;
    var s = color.s;
    var v = color.v;
    ```

- 常态化红、绿、蓝、α : 0~ 1

    ```javascript
    var r = color.redGL;
    var g = color.greenGL;
    var b = color.blueGL;
    var a = color.alphaGL;
    ```

#### 克隆 {#clone}

```javascript
var newColor = color.clone();
```

### 切换到十六进制字符串 {#to-hex-string}

```javascript
var hexString = Phaser.Display.Color.RGBToString(color.r, color.g, color.b, color.a);
// var hexString = Phaser.Display.Color.RGBToString(color.r, color.g, color.b, color.a, prefix);
```

### 内插 {#interpolation}

内插在2种颜色之间.

```javascript
var colorOut = Phaser.Display.Color.Interpolate.RGBWithRGB(r1, g1, b1, r2, g2, b2, length, index);
var colorOut = Phaser.Display.Color.Interpolate.ColorWithColor(color1, color2, length, index);
var colorOut = Phaser.Display.Color.Interpolate.ColorWithRGB(color, r, g, b, length, index);
```

- `length`, `index` = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = `index/length` (0~1)

## 面具 {#masks}

Phaser具有“ 隐藏” 游戏对象的渲染能力。 遮罩允许您从渲染中“ 隐藏” 的游戏对象区域。 可用两种遮罩: 几何遮罩和比特玛普遮罩。 几何遮罩通过使用几何数据来创建遮罩。 例如, 矩形、 圆形、 椭圆形、 多边形等。 这个数据用于创建一个构成遮罩的路径。 内部, 它使用WebGL中被称为的天花板缓冲器和坎瓦斯的剪贴路径 。

Bitmap Mask 工作方式是使用纹理作为遮罩。 这种纹理可以是您喜欢的任何大小和形状, 也可以是动画, 甚至是一个视频。 纹理控制中像素的α值是屏幕上像素。 例如, α值为 0 的像素会隐藏游戏对象, 以α值为1的像素显示它。 这样您就可以创建详细的效果, 如羽毛, 使用几何遮罩是不可能的。 Bitmap Maks 是一个仅包含 WebGL 的特性 。

Phaser中的面具在画和定位世界空间中略为独特。 游戏对象只能有一个面具在任何时间应用。 但是, 如果您愿意, 您可以对多个游戏对象应用同样的面具。 这些面具不是游戏对象的特异性, 如果移动游戏对象, 面具将不会“ 跟踪” 。 这意味着它们需要一些谨慎的计划才能有效使用 。

### 创建遮盖对象 {#create-mask-object}

#### 位图掩码 {#bitmap-mask}

```javascript
var mask =  scene.add.bitmapMask([maskObject], [x], [y], [texture], [frame]);
```

- `maskObject`: 游戏对象或动态纹理, 将作为遮罩使用。 如果无效, 则会使用其余参数生成图像游戏对象 。
- `x`:如果创建游戏对象,则世界水平位置.
- `y`:如果创建游戏对象,则世界垂直位置.
- `texture`:如果创建游戏对象,它会用它用来渲染的纹理的密钥或实例,如存储在纹理管理器中.
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

#### 几何掩码 {#geometry-mask}

面具本质上是一种剪辑路径,它只能使一个蒙面像素完全可见或完全看不见,而不会改变它的α(不透明).

1. 创建 [graphics](/guide/concepts/gameobjects/graphics)

    ```javascript
    var shape = scene.make.graphics();
    ```

1. 创建遮罩

    ```javascript
    var mask = shape.createGeometryMask();
    ```

### 应用遮罩对象 {#apply-mask-object}

```javascript
gameObject.setMask(mask); // image.mask = mask;
```

面具对象可以添加到许多游戏对象中.

!!! error
    别把游戏对象和面具放进 [container](/guide/concepts/gameobjects/container) 一起来
    看看这个[testing](https://codepen.io/rexrainbow/pen/mdBZJmb), 启用线路22 -24。

!!! note
    位图面具只有WebGL.

!!! note
    在同一游戏对象上可以结合几何面具和混合模式,
    但是,比特玛普面具不能。

### 清除掩码 {#clear-mask}

- 清除掩码

    ```javascript
    image.clearMask();
    ```

- 清除掩码并销毁掩码对象

    ```javascript
    image.clearMask(true);
    ```

### 反转 alpha {#invert-alpha}

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

### 获取形状游戏对象 {#get-shape-game-object}

- 位图掩码

    ```javascript
    var shape = mask.bitmapMask;
    ```

- 几何掩码

    ```javascript
    var shape = mask.geometryMask;
    ```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
