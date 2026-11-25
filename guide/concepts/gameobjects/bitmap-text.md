# 位图文本 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/bitmap-text)

位图文字游戏对象由基于位图的纹理文件, 如 PNG 文件创建。 此纹理包含每个字符, 以固定结构排列。 以下图像是位图文字纹理文件的示例 :

![image](https://cdn.phaser.games/oss-docs/assets/3b86f065116c9dec-bitmapfont-example-texture.png)

纹理文件几乎总是附有一个基于XML或JSON的文件,描述字体结构。这个文件包含纹理中每个字符的位置,因此渲染器知道如何剪除它们,以及kerning数据.

由于字体来自纹理,所以对于是否安装在用户系统中,或装入Web字体等,并不担心。但是,由于从纹理中抽取的纹理,您在使用纹理时会受到更大的限制。例如,您不能对比图文字进行中风或填充模式等。此外,您也只局限于纹理文件中的字符,所以如果您的游戏需要支持多种语言,就必须直接在字体纹理中满足这个要求。

附加方面,WebGL Bitmap Texts下极快的渲染,与Text Game Objects不同,由于基础纹理不变,在更新内容时不会出现任何速度速速的处罚. 也可以通过在图像编辑器中准备,应用填充和其他需要的效果来创建视觉印象深刻的字体. 以上图像中可以看到,这种样式用Web字体将极其难以实现.

## 位图文本创建软件 {#bitmap-text-creation-software}

要创建 Bitmap 文本数据文件, 您需要一个 3rd 党的应用程序。 这里有四个最常见的文件 :

* [BMFont](http://www.angelcode.com/products/bmfont/)(窗户,免费)
* [Glyph Designer](https://www.71squared.com/en/glyphdesigner) (macOS,商业)
* [SnowB BMF](https://snowb.org/)(基于网络、免费)
* [Littera](http://kvazars.com/littera/)( 以闪光为主 - 是的, 真的, 免费)

在大多数使用的情况下,建议使用 XML 文件格式。例如, BMFont 生成其数据为 XML。 当它保存文件时, 它们有一个 `.fnt` 扩展名, 但是您可以简单地将其重命名为 `.xml` 。

如果您想要使用JSON,格式化应该等于通过流行的X2JS库转换一个有效的XML文件的结果. 在[Code Beautify](https://codebeautify.org/xmltojson)网站上可以找到一个转换的在线工具.

### 从图像和字体数据 {#from-an-image-and-font-data}

位图字体生成器会制作图像和 XML 数据文件。 使用 `load.bitmapFont()` :

```js
this.load.bitmapFont('key', 'font.png', 'font.xml');
```

要创建多行文本,请在文本字符串中插入\r,\n或\rn 逃逸代码.

### 从地图集和字体数据中 {#from-an-atlas-and-font-data}

分别装入图像和XML数据,然后调用`ParseFromAtlas()`来创建字体.

* [bitmap text from atlas](https://labs.phaser.io/edit.html?src=src/game%20objects/bitmaptext/static/bitmaptext-atlas.js)

### 从“ 反转字体” 图像 {#from-a-retro-font-image}

装上图像,然后用[font data](/api/typedef/types-gameobjects-bitmaptext#retrofontconfig)呼叫`RetroFont.Parse()`.

* [retro text 1](https://labs.phaser.io/view.html?src=src\game%20objects\bitmaptext\retro%20font\retro%20text%201.js)

## 位图文本 {#bitmap-text}

这些是使用字体显示文本的游戏对象。 有两类, [BitmapText](/api/class/gameobjects-bitmaptext)和 [DynamicBitmapText](/api/class/gameobjects-dynamicbitmaptext)。 它们都是“ 动态” , 意思是您可以随时更改文本内容。 不同的是 Dynamic BitmapText 具有 [callbacks](/api/typedef/types-gameobjects-bitmaptext#displaycallbackconfig) , 用于每个字符的渲染效果和 [scrolling](https://labs.phaser.io/view.html?src=src\game%20objects\bitmaptext\dynamic\vertical%20scroller.js) 。

### 装入位图字体 {#load-bitmap-font}

* 从纹理和xml 配置中装入位图字体

    ```js
    this.load.bitmapFont(key, textureURL, xmlURL);
    ```

  * 参考文献: [load bitmap font](/guide/concepts/loader#bitmap-font)
  * 装入的纹理也可以用于 [Image](#load-bitmap-font), [Sprite](#load-bitmap-font),或 ,或 , [Arcade Image](/guide/concepts/physics/arcade#image-object), [Arcade Sprite](/guide/concepts/physics/arcade#sprite-object)

        ```js
        this.add.image(x, y, key, char);
        ```

- 从纹理和JSON配置中装入复刻点图字体
    1. 在 * preload* 阶段装入纹理

        ```js
        this.load.image(key, url);
        ```

        参考文献: [load image](/guide/concepts/loader#image)
    2. 添加复古位图字体

        ```js
        var config = {
            // image
            image: '',
            offset: {
                x: 0,
                y: 0
            },
            // characters
            width: 32,
            height: 32,
            chars: '',
            charsPerRow: 10,
            // spacing
            spacing: {
                x: 0,
                y: 0
            },
            lineSpacing: 0
        }
        this.cache.bitmapFont.add(key, Phaser.GameObjects.RetroFont.Parse(scene, config));
        ```

        * Image :
            * `image`:包含字体的图像的密钥.
            * `offset`:如果字体集没有从给定图像左上方开始,请在此指定 X/Y坐标偏移.
        * Characters :
            * `width`:字体集中每个字符的宽度.
            * `height`:字体集中每个字符的高度.
            * `chars`:字体集中所使用的字符,按显示顺序排列.
                * [Default characters set](#default-characters-set-of-retro-font)
            * `charsPerRow`:字体集中每行字符数。如果不给charsPerRow,则图像宽度为 / characterWidth 。
        * Spacing :
            * `spacing` : 如果字体集中的字符之间有水平/垂直间隔,则在此设定所需数量.
            * `lineSpacing`:用于添加字体行高的垂直空间的量.

### 添加位图文本对象 {#add-bitmap-text-object}

```js
var txt = this.add.bitmapText(x, y, key, text);
// var txt = this.add.bitmapText(x, y, key, text, size, align);
```

* `size`:字体大小
* `align`: 将文本对齐于 * 多行 * 比特玛普文本对象。
  * `0`:左侧对齐(默认)
  * `1`: 中调
  * `2`: 右侧对齐

从 JSON 添加文字

```js
var txt = this.make.bitmapText({
    x: 0,
    y: 0,
    text: 'Text\nGame Object\nCreated from config',
    font: '',
    size: false,
    align: 0,
    // origin: {x: 0.5, y: 0.5},
    add: true
});
```

### 自定义类 {#custom-class}

* 定义类

    ```js
    class MyText extends Phaser.GameObjects.BitmapText {
        constructor(scene, x, y, key, text, size, align) {
            super(scene, x, y, key, text, size, align);
            // ...
            this.add.existing(this);
        }
        // ...

        // preUpdate(time, delta) {}
    }
    ```

  * `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    * 如果游戏对象使它成为了,它会被添加到显示列表中.
    * 如果它有`preUpdate`方法,它将被添加到更新列表中.
* 创建实例

    ```js
    var txt = new MyText(scene, x, y, key, text);
    ```

### 设定文本 {#set-text}

```js
txt.setText('...');
```

or

```js
txt.text = '...';
```

### 设定对齐 {#set-align}

* 左对齐

    ```js
    txt.setLeftAlign();
    ```

- 中调

    ```js
    txt.setCenterAlign();
    ```

- 右对齐

    ```js
    txt.setRightAlign();
    ```

or

```js
txt.align = align;
```

* `align` :
  * `0`:左侧对齐(默认)
  * `1`: 中调
  * `2`: 右侧对齐

### 设定字母间隔 {#set-letter-spacing}

```js
txt.setLetterSpacing(spacing);
```

or

```js
txt.letterSpacing = spacing;
```

可以是增加空间的积极值,也可以是减少空间的负值.

### 设定行距 {#set-line-spacing}

```js
txt.setLineSpacing(spacing);
```

or

```js
txt.lineSpacing = spacing;
```

可以是增加空间的积极值,也可以是减少空间的负值.

### 设置字体大小 {#set-font-size}

```js
txt.setFontSize(size);
```

or

```js
txt.fontSize = size;
```

### 设置字体 {#set-font}

```js
txt.setFont(key);
// txt.setFont(key, size, align);
```

### 叮当 {#tint}

见[Tint](/guide/concepts/gameobjects#tint).

### 字符颜色 {#color-of-characters}

* 按字符分类

    ```js
    txt.setCharacterTint(start, length, tintFill, color);
    // txt.setCharacterTint(start, length, tintFill, topLeft, topRight, bottomLeft, bottomRight);
    ```

  * `start` : 索引起始字符。
    * `< 0` :从文字的结尾算回来.
  * `length` : 字符数为锡.
    * `-1`: 所有字符来自`start`
  * `tintFill` :
    * `true`: 填充锡
    * `false` : 添加锡
  * `color`,或 ,或 , `topLeft, topRight, bottomLeft, bottomRight` : 颜色整数。
* 以字为单位

    ```js
    txt.setWordTint(word, count, tintFill, color);
    // txt.setWordTint(word, count, tintFill, topLeft, topRight, bottomLeft, bottomRight);
    ```

  * `word` :要寻之词.
    * 字符串
    * 单词阵列中的单词索引 。
  * `count` : 匹配字数与锡。
    * `-1` : 所有匹配的单词
  * `tintFill` :
    * `true`: 填充锡
    * `false` : 添加锡
  * `color`,或 ,或 , `topLeft, topRight, bottomLeft, bottomRight` : 颜色整数。

### 丢弃阴影效果 {#drop-shadow-effect}

```js
txt.setDropShadow(x, y, color, alpha);
```

or

```js
txt.dropShadowX = x;
txt.dropShadowY = y;
txt.dropShadowColor = color;
txt.dropShadowAlpha = alpha;
```

* `x`,`y`:滴影的横向/纵向偏移.
* `color` :投影的颜色.
* `alpha` : 投影的α.

!!! note
    仅限WebGL

### 环绕 {#wrap}

* Wrap

    ```js
    txt.setMaxWidth(width);
    // txt.setMaxWidth(width, wordWrapCharCode);
    ```

  * `width`:线宽以像素表示.
  * `wordWrapCharCode`: 字包包装时要检查的字符代码。 默认为 32 (* space * 字符)
* 禁用围网

    ```js
    txt.setMaxWidth(0);
    ```

### 获得界限 {#get-bounds}

```js
var width = txt.width;
var height = txt.height;
```

or

```js
var bounds = txt.getTextBounds(round);
// bounds = {
//     local: {
//         x: 0,
//         y: 0,
//         width: 0,
//         height: 0
//     },
//     global: {
//         x: 0,
//         y: 0,
//         width: 0,
//         height: 0
//     },
//     lines: {
//         shortest: 0,
//         longest: 0,
//         lengths: null,
//         height: 0
//     },
//     wrappedText: '',
//     words: [],
//     characters: [],
//     scaleX: 0,
//     scaleY: 0
// };
```

* `round` 设置 `true` 以将结果整数整数为单位。
* `local`:基于fontSize和0x0coords的位图图文集.
* `global`:位图图文集,考虑到规模和世界位置.
* `lines`:位图Text行数据.
* `wrappedText` : 已包装的内容已加入 `'\n'`.
* `characters` : 每种字符的信息。

    ```js
    {
        char, code, i, idx, x, y, w, h, t, b, r, line
    }
    ```

  * `char`:字符(字符串).
  * `code`:字符代码(数字)
  * `i`: 人物索引 人物索引 人物索引 人物索引 人物索引 人物索引 人物索引 人物索引 人物索引 人物索引 人物索引
  * `x`,`y`:这个角色的世界位置.
  * `w`, `h` : 此字符的宽度/ 高度
  * `t`, `b` : 此字符的上下行 。
  * `r` : 此字符的最右侧点, 包括 xAdvance.
  * `line` : 字符出现的行号.
* `words` : 每个字的信息。

    ```js
    {
        word, i, x, y, w, h, cr

    }
    ```

  * `word` :字弦("  ").
  * `i`: 起始字符索引
  * `x`,`y`:开始角色的世界位置
  * `w` , `h` : 宽度/高值
  * `cr`:是当前行的最后一个字
* `scaleX`,`scaleY`:宽度和高度的尺度.

#### 获取字符信息 {#get-information-of-character}

```js
var data = txt.getCharacterAt(x, y);
// var data = txt.getCharacterAt(x, y, camera);
```

* `x`, `y` : 世界立场.
* `camera` 正在测试的相机。
* `data` :世界位置的人物信息.

    ```js
    {
        char, code, i, x, y, w, h, t, b, r, line
    }
    ```

  * `char`:字符(字符串).
  * `code`:字符代码(数字)
  * `i`: 人物索引 人物索引 人物索引 人物索引 人物索引 人物索引 人物索引 人物索引 人物索引 人物索引 人物索引
  * `x`,`y`:这个角色的世界位置.
  * `w`, `h` : 此字符的宽度/ 高度
  * `t`, `b` : 此字符的上下行 。
  * `r` : 此字符的最右侧点, 包括 xAdvance.
  * `line` : 字符出现的行号.

### 其他属性 {#other-properties}

见[game object](/guide/concepts/gameobjects)

### 创建遮罩 {#create-mask}

```js
var mask = txt.createBitmapMask();
```

### 阴影效果 {#shader-effects}

只支持postFX效果.

## 附 录 {#appendix}

### 复古字体的默认字符集 {#default-characters-set-of-retro-font}

* `Phaser.GameObjects.RetroFont.TEXT_SET1` :

    ```
    ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    ```

- `Phaser.GameObjects.RetroFont.TEXT_SET2` :

    ```
    ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ```

- `Phaser.GameObjects.RetroFont.TEXT_SET3` :

    ```
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
    ```

- `Phaser.GameObjects.RetroFont.TEXT_SET4` :

    ```
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789'
    ```

- `Phaser.GameObjects.RetroFont.TEXT_SET5` :

    ```
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ.,/() \'!?-*:0123456789'
    ```

- `Phaser.GameObjects.RetroFont.TEXT_SET6` :

    ```
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ!?:;0123456789"(),-.\' '
    ```

- `Phaser.GameObjects.RetroFont.TEXT_SET7` :

    ```
    'AGMSY+:4BHNTZ!;5CIOU.?06DJPV,(17EKQW")28FLRX-\'39'
    ```

- `Phaser.GameObjects.RetroFont.TEXT_SET8` :

    ```
    '0123456789 .ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ```

- `Phaser.GameObjects.RetroFont.TEXT_SET9` :

    ```
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ()-0123456789.:,\'"?!'
    ```

- `Phaser.GameObjects.RetroFont.TEXT_SET10` :

    ```
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ```

- `Phaser.GameObjects.RetroFont.TEXT_SET11` :

    ```
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ.,"-+!?()\':;0123456789'
    ```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)
- [samme](https://github.com/samme)

---
