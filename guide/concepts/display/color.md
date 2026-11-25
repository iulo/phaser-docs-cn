# 颜色 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/display/color)

彩色类持有单一的彩色值,并允许轻松修改和阅读.

## 获得颜色整数 {#get-color-integer}

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

## 颜色整数到 RGB {#color-integer-to-rgb}

```javascript
var rgb = Phaser.Display.Color.IntegerToRGB(color);
```

- `color` : 颜色整数 (`0xAARRGGBB`)
- `rgb` : JSON对象( 以`{r, g, b, a}`)

## HSV 彩色轮 {#hsv-color-wheel}

1. 创建颜色阵列

    ```javascript
    var colorArray = Phaser.Display.Color.HSVColorWheel(s, v);
    ```

1. 获取颜色

    ```javascript
    var color = colorArray[i].color;  // i : 0 ~ 359
    ```

## 颜色对象 {#color-object}

### 创建颜色对象 {#create-color-object}

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

### 设定颜色 {#set-color}

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

### 属性 {#properties}

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

### 克隆 {#clone}

```javascript
var newColor = color.clone();
```

## 切换到十六进制字符串 {#to-hex-string}

```javascript
var hexString = Phaser.Display.Color.RGBToString(color.r, color.g, color.b, color.a);
// var hexString = Phaser.Display.Color.RGBToString(color.r, color.g, color.b, color.a, prefix);
```

## 内插 {#interpolation}

内插在2种颜色之间.

```javascript
var colorOut = Phaser.Display.Color.Interpolate.RGBWithRGB(r1, g1, b1, r2, g2, b2, length, index);
var colorOut = Phaser.Display.Color.Interpolate.ColorWithColor(color1, color2, length, index);
var colorOut = Phaser.Display.Color.Interpolate.ColorWithRGB(color, r, g, b, length, index);
```

- `length`, `index` = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = `index/length` (0~1)

## 作者的信用额度 {#author-credits}

本页的内容包括下列工作:

- [RexRainbow](https://github.com/rexrainbow)

---
