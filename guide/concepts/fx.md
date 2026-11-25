# 视觉特效（FX） {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/fx)

截至Phaser v3.60,框架包括了一个新的FX管道系统,具有许多内置效果,这是将处理前和处理后效果都应用到您的游戏中的一种强大而灵活的方式,它只是WebGL的特性,由于依赖于遮荫剂,所以没有Canvas模式.

内置的FX包括:巴雷尔,布隆,布卢尔,博凯,圆,彩色马特里克斯,流离失所,格洛,渐变,皮克斯拉特,影子,闪电,维涅特和擦拭.

FX可以被启用在所有常见类型的游戏对象上,并且可以堆叠效果并控制堆叠顺序。例如,你可以同时对Sprite应用发光和阴光效应。摄像机也可以应用FX,它影响它们所创造的一切,并让你创造效果,如“zoom模糊”或像素。

- [Barrel Distortion](#barrel) :一个很好的夹/凸起扭曲效果.
- [Bloom](#bloom):在任意游戏对象中添加开花,带有自定义的偏移,模糊的强度,步骤和颜色.
- [Blur](#blur): 3个不同的加西语模糊度(低,中,高)和自定义距离和颜色.
- [Bokeh](#bokeh) / [Tilt Shift](#tilt-shift):具有烈度,对比度和距离设置的波音和倾斜变速效应.
- [Circle Outline](#circle-outline):在任意游戏对象周围添加一个圆环,用于遮盖/变形框,带有自定义的颜色,宽度和背景颜色.
- [Color Matrix](#colormatrix) : 在任何游戏对象中添加一个色彩映射, 并访问其所有方法, 例如 `sepia`, `greyscale`, `lsd` 还有很多
- [Glow](#glow):增加一个光滑的内光或外光,带有自定义的距离,强度和颜色.
- [Displacement](#displacement):使用一个取代纹理,如噪声纹理,来急剧(或潜移!)改变游戏对象的外观.
- [Gradient](#gradient) :在任意游戏对象的两种颜色之间画一个梯度,经典的复古风格游戏可选的“春基”模式.
- [Pixelate](#pixelate):使任何游戏对象出现像素化,程度不同.
- [Shine](#shine):在游戏对象上运行一个"阳光"效果,或者添加效果,或者作为披露的一部分.
- [Shadow](#shadow):在游戏对象后添加一个投影,带有自定义的深度和颜色.
- [Vignette](#vignette):围绕游戏对象应用一个阴极,带有自定义的偏移位置,半径和颜色.
- [Wipe](#wipe) / [Reveal](#reveal):设置一个游戏对象为"Wipe"或"reveal",其效果的自定义线宽度,方向和轴.

基于纹理的游戏对象也支持Pre FX,包括:图像,Sprite,TileSprite,Text,RenderTexture,视频.

所有游戏对象和摄像机支持 Post FX 。 这些是游戏对象被渲染后应用的效果 。

- 作者:理查德·戴维
- 预fx, 和后fx 阴影效果

警告我,我警告你,我警告你,你该死WebGL 仅此而已"
    只在WebGL渲染模式下工作.

## 现场演示 {#live-demos}

- [Official demos](https://labs.phaser.io/index.html?dir=3.60/fx/&q=)

## 弹匣 {#barrel}

- 将预值添加到游戏对象

    ```javascript
    // gameObject.preFX.setPadding(padding);
    var effect = gameObject.preFX.addBarrel(amount);
    ```

  - `padding`:要添加到此游戏对象的粘贴量, 以像素表示 。
    - 使用时`amount`大于`1`.
  - `amount`:适用于枪管效果的扭曲量。
    - `1` : 无扭曲
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addBarrel(amount);
    ```

    ```javascript
    var effect = camera.postFX.addBarrel(amount);
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.amount = amount;
    ```

## 布鲁姆 {#bloom}

- 将预值添加到游戏对象

    ```javascript
    var effect = gameObject.preFX.addBloom(color, offsetX, offsetY, blurStrength, strength, steps);
    ```

  - `color` :布鲁姆的颜色,作为六分值.
  - `offsetX`,`offsetY`:花朵效果的横向/纵向抵消. 默认值为`1`.
  - `blurStrength`, `strength`: 开花效果的模糊/宽度过程的强度,默认值为`1`.
  - `steps` : 运行 Bloom 效果的步骤数。 此值应该总是整数。 默认值是 `4` 。
    - 值越高,布鲁姆越平滑,但代价是指数性地增加gl操作.
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addBloom(color, offsetX, offsetY, blurStrength, strength, steps);
    ```

    ```javascript
    var effect = camera.postFX.addBloom(color, offsetX, offsetY, blurStrength, strength, steps);
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.color = color;  // hex value
    effect.offsetX = offsetX;
    effect.offsetY = offsetY;
    effect.blurStrength = blurStrength;
    effect.strength = strength;
    effect.steps = steps; // integer
    ```

## 模糊 {#blur}

- 将预值添加到游戏对象

    ```javascript
    var effect = gameObject.preFX.addBlur(quality, x, y, strength, color, steps);
    ```

  - `quality`:模糊效果的质量,默认值为`0`.
    - `0`: 低质量
    - `1`: 中质素
    - `2`: 高品质
  - `x`, `y`:模糊效果的横向/纵向抵消. 默认值为 `2`.
  - `strength`:模糊效果的强度,默认值为`1`.
  - `color`:模糊的颜色,作为六进制值。默认值为`0xffffff`。
  - `steps` : 运行模糊效果的步骤数。 此值应该总是整数 。
    - 值越高,越平滑,模糊度越高,但代价是指数性地增加gl操作.
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addBlur(quality, x, y, strength, color, steps);
    ```

    ```javascript
    var effect = camera.postFX.addBlur(quality, x, y, strength, color, steps);
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.quality = quality;
    effect.x = x;
    effect.y = y;
    effect.strength = strength;
    effect.color = color;
    effect.steps = steps;
    ```

## 博凯 {#bokeh}

- 将预值添加到游戏对象

    ```javascript
    var effect = gameObject.preFX.addBokeh(radius, amount, contrast);
    ```

  - `radius`:波音效应的半径,默认值为`0.5`.
  - `amount` : bokeh效应的金额。默认值为 `1`.
  - `contrast`: bokeh效应的颜色对比值。默认值为`0.2`。
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addBlur(quality, x, y, strength, color, steps);
    ```

    ```javascript
    var effect = camera.postFX.addBokeh(radius, amount, contrast);
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.radius = radius;
    effect.amount = amount;
    effect.contrast = contrast;
    ```

## 倾斜移动 {#tilt-shift}

- 将预值添加到游戏对象

    ```javascript
    var effect = gameObject.preFX.addTiltShift(radius, amount, contrast, blurX, blurY, strength);
    ```

  - `radius`:波音效应的半径,默认值为`0.5`.
  - `amount` : bokeh效应的金额。默认值为 `1`.
  - `contrast`: bokeh效应的颜色对比值。默认值为`0.2`。
  - `blurX`, `blurY` :水平/垂直模糊度的大小.
  - `strength` :模糊的强度.
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addTiltShift(radius, amount, contrast, blurX, blurY, strength);
    ```

    ```javascript
    var effect = camera.postFX.addTiltShift(radius, amount, contrast, blurX, blurY, strength);
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.radius = radius;
    effect.amount = amount;
    effect.contrast = contrast;
    effect.blurX = blurX;
    effect.blurY = blurY;
    effect.strength = strength;
    ```

## 圆形轮廓 {#circle-outline}

- 将预值添加到游戏对象

    ```javascript
    var effect = gameObject.preFX.addCircle(thickness, color, backgroundColor, scale, feather);
    ```

  - `thickness`: 纹理周围圆的宽度, 以像素表示。 默认值为 `8` 。
  - `color`:圆环的颜色,以数字值表示。默认值为`0xfeedb6`。
  - `backgroundColor`:背景颜色,纹理后面,作为数字值给出。默认值为`0xff0000`。
  - `scale` : 圆的大小。默认值为 `1`.
    - `1` : 基础纹理的全尺寸.
  - `feather`: 将羽毛的量从环面应用到圆形上。 默认值为 `0.005` 。
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addCircle(thickness, color, backgroundColor, scale, feather);
    ```

    ```javascript
    var effect = camera.postFX.addCircle(thickness, color, backgroundColor, scale, feather);
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.thickness = thickness;
    effect.color = color;
    effect.backgroundColor = backgroundColor;
    effect.backgroundAlpha = backgroundAlpha;
    effect.scale = scale;
    effect.feather = feather;
    ```

## 颜色Matrix 颜色 {#colormatrix}

- 将预值添加到游戏对象

    ```javascript
    var effect = gameObject.preFX.addColorMatrix();
    ```

- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addColorMatrix();
    ```

    ```javascript
    var effect = camera.postFX.addColorMatrix();
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 方法
  - 亮度 : 以给定的量来修改此 ColorMatrix 的亮度 。

    ```javascript
    effect.brightness(value, multiply);
    ```

    - `value` : 此 ColorMatrix 应用的亮度量 。 `0`( 黑色) ~ `1`。 默认值为 `0` 。
    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - 饱和 : 以给定的量更改此 ColorMatrix 的饱和度 。

    ```javascript
    effect.saturate(value, multiply);
    ```

    - `value`: 适用于此 ColorMatrix 的饱和度。 默认值为 `0` 。
    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - 脱饱和:脱饱和这个颜色Matrix(从它中切除颜色).

    ```javascript
    effect.desaturate(value, multiply);
    ```

    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - 色调: 以给定的值旋转此颜色Matrix的色调 。

    ```javascript
    effect.hue(rotation, multiply);
    ```

    - `rotation`: 适用于此 ColorMatrix 的 旋转量, 以度计。 默认值为 `0` 。
    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - 灰度 : 将此颜色Matrix 设定为灰度 。

    ```javascript
    effect.grayscale(value, multiply);
    ```

    - `value`:灰度尺`0`(黑色)~`1`. 默认值为`1`.
    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - 黑白 : 设置此颜色Matrix为黑白 。

    ```javascript
    effect.blackWhite(multiply);
    ```

    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - 对比度 : 以给定的量改变此 ColorMatrix 的对比度 。

    ```javascript
    effect.contrast(value, multiply);
    ```

    - `value` : 适用于此 ColorMatrix 的对比量。 默认值为 `0` 。
    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - 负数 : 转换此颜色Matrix 以负值 。

    ```javascript
    effect.negative(multiply);
    ```

    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - 脱饱和光度:对这个 ColorMatrix 应用脱饱和光度.

    ```javascript
    effect.desaturateLuminance(multiply);
    ```

    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - 塞皮亚:对这个 ColorMatrix 应用一个塞皮亚语调.

    ```javascript
    effect.sepia(multiply);
    ```

    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - 夜:对这个 ColorMatrix 应用夜视音.

    ```javascript
    effect.night(intensity, multiply);
    ```

    - `intensity`: 此效果的强度。 默认值为 `0.1` 。
    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - LSD: 将一个三进制的颜色补间应用到这个 ColorMatrix 上.

    ```javascript
    effect.lsd(multiply);
    ```

    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - 棕色:对这个ColorMatrix应用一个棕色的音色.

    ```javascript
    effect.brown(multiply);
    ```

    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - VintagePinhole:对这个 ColorMatrix 应用一个Vintage Pinhole的颜色效果.

    ```javascript
    effect.vintagePinhole(multiply);
    ```

    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - Kodachrome : 将 kodachrome 颜色效果应用到这个 ColorMatrix 上.

    ```javascript
    effect.kodachrome(multiply);
    ```

    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - Technicolor : 将一种技术色彩效果应用到此 ColorMatrix 上.

    ```javascript
    effect.technicolor(multiply);
    ```

    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - Polyoid : 将极性颜色效果应用到这个 ColorMatrix 上.

    ```javascript
    effect.polaroid(multiply);
    ```

    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。
  - ShiftToBGR : 将此 ColorMatrix 的值移到 BGR 顺序 。

    ```javascript
    effect.shiftToBGR(multiply);
    ```

    - `multiply` : 乘以产生的颜色Matrix(`true`),或设置(`false`) ?
      - `true` :乘以结果.
      - `false` : 设置结果。默认行为。

## 流离失所 {#displacement}

- 将预值添加到游戏对象

    ```javascript
    var effect = gameObject.preFX.addDisplacement(texture, x, y);
    ```

  - `texture`:用于移位的纹理中唯一基于字符串的键,它必须存在于纹理管理器中。默认值为`'__WHITE'`。
    - 您只能使用整个纹理, 而不是来自纹理图集或图示表的框 。
  - `x`, `y`: 应用的水平/垂直移位量。默认值为 `0.005` 。
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addDisplacement(texture, x, y);
    ```

    ```javascript
    var effect = camera.postFX.addDisplacement(texture, x, y);
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.x = x;
    effect.y = y;    
    ```

- 方法
  - 设置纹理

    ```javascript
    effect.setTexture(key);
    ```

## 轻 {#glow}

- 将预值添加到游戏对象

    ```javascript
    // gameObject.preFX.setPadding(padding);
    var effect = gameObject.preFX.addGlow(color, outerStrength, innerStrength, knockout);
    ```

  - `padding`:要添加到此游戏对象的粘贴量, 以像素表示 。
    - 使用时`amount`大于`1`.
  - `color`: 以数字值表示的发光效果的颜色。默认值为`0xffffff`。
  - `outerStrength`, `innerStrength` : 闪光从闪光板边缘向外/向外的强度。默认值是 `4`/`0`.
  - `knockout` :
    - `true`:只有光线被画出来
    - `false` : 画出发光和纹理, 默认行为 。
  - `quality` : 仅供 PostFX 使用。 设定此 Glow 效果的质量。 默认为 0.1 。 无法更改创建后 。
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addGlow(color, outerStrength, innerStrength, knockout, quality, distance);
    ```

    ```javascript
    var effect = camera.postFX.addGlow(color, outerStrength, innerStrength, knockout, quality, distance);
    ```

  - `quality`: 设置此 Glow 效果的质量。 默认为 `0.1`。 无法更改创建后 。
  - `distance`: 设定此Glow效果的距离。 默认为 `10`。 无法更改创建后 。
- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.color = color;
    effect.outerStrength = outerStrength;
    effect.innerStrength = innerStrength;
    effect.knockout = knockout;
    ```

## 渐变 {#gradient}

- 将预值添加到游戏对象

    ```javascript
    var effect = gameObject.preFX.addGradient(color1, color2, alpha, fromX, fromY, toX, toY, size);
    ```

  - `color1`, `color2` : 第一种/第二种梯度颜色,作为数字值。默认值是 `0xff0000`/`0x00ff00`.
  - `alpha`:梯度效应的α值.
  - `fromX`, `fromY` : 水平/垂直位置,梯度将开始。数值介于 `0` 财务报告和已审计财务报表 `1`.
  - `toX`, `toY` : 水平/垂直位置梯度将结束。值介于 `0` 财务报告和已审计财务报表 `1`.
  - `size`:梯度分为多少个"圆",如分布在纹理的整个高度.
    - `0` : 平滑梯度。 默认行为 。
    - 其他:逆向块状效应.
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addGradient(color1, color2, alpha, fromX, fromY, toX, toY, size);
    ```

    ```javascript
    var effect = camera.postFX.addGradient(color1, color2, alpha, fromX, fromY, toX, toY, size);
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.color1 = color1;
    effect.color2 = color2;
    effect.alpha = alpha;
    effect.fromX = fromX;
    effect.fromY = fromY;
    effect.toX = toX;
    effect.toY = toY;
    effect.size = size;
    ```

## 像素 {#pixelate}

- 将预值添加到游戏对象

    ```javascript
    var effect = gameObject.preFX.addPixelate(amount);
    ```

  - `amount`:应用的像素的量,以像素表示.
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addPixelate(amount);
    ```

    ```javascript
    var effect = camera.postFX.addPixelate(amount);
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.amount = amount;
    ```

## 阴影 {#shadow}

- 将预值添加到游戏对象

    ```javascript
    // gameObject.preFX.setPadding(padding);
    var effect = gameObject.preFX.addShadow(x, y, decay, power, color, samples, intensity);
    ```

  - `padding`:要添加到此游戏对象的粘贴量, 以像素表示 。
    - 使用时`amount`大于`1`.
  - `x`,`y`:阴影效应的横向/纵向抵消. 默认值为`0`.
  - `decay`: 阴影效应的衰变量。 默认值为 `0.1` 。
  - `power`:阴影效应的功率,默认值为`1`.
  - `color` : 阴影的颜色。默认值是 `0x000000`.
  - `samples`: 阴影效应将运行的样本数量。 `1`和 `12`之间的整数。
  - `intensity`: 阴影效应的强度。 默认值为 `1` 。
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addShadow(x, y, decay, power, color, samples, intensity);
    ```

    ```javascript
    var effect = camera.postFX.addShadow(x, y, decay, power, color, samples, intensity);
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.x = x;
    effect.y = y;
    effect.decay = decay;
    effect.power = power;
    effect.color = color;
    effect.samples = samples;
    effect.intensity = intensity;
    ```

## 闪耀 {#shine}

- 将预值添加到游戏对象

    ```javascript
    var effect = gameObject.preFX.addShine(speed, lineWidth, gradient, reveal);
    ```

  - `speed`:闪电效应的速度。默认值为`0.5`。
  - `lineWidth`:闪电效应的线宽。默认值为`0.5`。
  - `gradient`:闪电效应的梯度。默认值为`3`。
  - `reveal` :这种闪光效应是揭示还是被添加到目标中?
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addShine(speed, lineWidth, gradient, reveal);
    ```

    ```javascript
    var effect = camera.postFX.addShine(speed, lineWidth, gradient, reveal);
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.speed = speed;
    effect.lineWidth = lineWidth;
    effect.gradient = gradient;
    effect.reveal = reveal;
    ```

## 维涅特 {#vignette}

- 将预值添加到游戏对象

    ```javascript
    var effect = gameObject.preFX.addVignette(x, y, radius, strength);
    ```

  - `x`, `y` : 阴极效应的横向/纵向抵消。值介于 `0` 财务报告和已审计财务报表 `1`默认值为 `0.5`.
  - `radius`: 阴极效应的半径。 值介于 `0` 和 `1`之间。 默认值为 `0.5` 。
  - `strength`: 阴极效应的强度。默认值为`0.5`。
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addVignette(x, y, radius, strength);
    ```

    ```javascript
    var effect = camera.postFX.addVignette(x, y, radius, strength);
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.x = x;
    effect.y = y;
    effect.radius = radius;
    effect.strength = strength;
    ```

## 擦除( E) {#wipe}

- 将预值添加到游戏对象

    ```javascript
    var effect = gameObject.preFX.addWipe(wipeWidth, direction, axis);
    ```

  - `wipeWidth`: 擦拭效果的宽度。 值介于 `0` 和 `1`之间。 默认值为 `0.1` 。
  - `direction` :擦拭效果的方向.
    - `0`: 左到右, 或上到下
    - `1`: 右到左,或下到上
  - `axis` :擦拭效果的轴.
    - `0`: 左到右, 或右到左
    - `1`: 下到上,或上到下
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addWipe(wipeWidth, direction, axis);
    ```

    ```javascript
    var effect = camera.postFX.addWipe(wipeWidth, direction, axis);
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.progress = t; // 0~1
    effect.wipeWidth = wipeWidth;
    effect.direction = direction;  // 0, 1
    effect.axis = axis;  // 0, 1    
    ```

## 启示 {#reveal}

- 将预值添加到游戏对象

    ```javascript
    var effect = gameObject.preFX.addReveal(wipeWidth, direction, axis);
    ```

  - `wipeWidth`: 擦拭效果的宽度。 值介于 `0` 和 `1`之间。 默认值为 `0.1` 。
  - `direction` :擦拭效果的方向.
    - `0`: 左到右, 或上到下
    - `1`: 右到左,或下到上
  - `axis` :擦拭效果的轴.
    - `0`: 左到右, 或右到左
    - `1`: 下到上,或上到下
- 将 fx 后添加到游戏对象, 或摄像机

    ```javascript
    var effect = gameObject.postFX.addReveal(wipeWidth, direction, axis);
    ```

    ```javascript
    var effect = camera.postFX.addReveal(wipeWidth, direction, axis);
    ```

- 禁用效果

    ```javascript
    effect.setActive(false);
    // effect.active = false;
    ```

- 删除效果

    ```javascript
    gameObject.preFX.remove(effect);
    ```

    ```javascript
    camera.postFX.remove(effect);
    ```

- 属性

    ```javascript
    effect.progress = t; // 0~1
    effect.wipeWidth = wipeWidth;
    effect.direction = direction;  // 0, 1
    effect.axis = axis;  // 0, 1
    ```

## 删除所有效果 {#remove-all-effects}

```javascript
gameObject.preFX.clear();
```

```javascript
gameObject.postFX.clear();
```

```javascript
camera.postFX.clear();
```

## 禁用所有效果 {#disable-all-effects}

```javascript
gameObject.preFX.disable();
// gameObject.preFX.disable(true);  // Also remove all effects
```

```javascript
gameObject.postFX.disable();
// gameObject.postFX.disable(true);  // Also remove all effects
```

```javascript
camera.postFX.disable();
// camera.postFX.disable(true);  // Also remove all effects
```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
