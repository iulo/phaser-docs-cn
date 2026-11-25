# 文本 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/text)

文本对象通过创建自己的内部隐藏的 Canvas 来工作, 然后使用标准的 Canvas `fillText`Z API 来制作文本。 然后从这个画布中创建一个纹理, 在渲染传阅时将它交给您的游戏 。

因为它使用 Canvas API 您可以利用所有这些要约的特性, 比如在文本中应用渐变填充, 或者用中键、 阴影等。 您也可以使用外部加载的自定义字体, 如 Google 或 TypeKit Web 字体 。

重要:如果字体名称包含某些数字或特殊字符组合,则必须引用该字体名称,或者在创建文本对象时,或者在通过`setFont`或`setFontFamily`设置字体时,例如:

```js
this.add.text(0, 0, 'Hello World', { fontFamily: 'Georgia, "Goudy Bookletter 1911", Times, serif' });
```

```js
this.add.text(0, 0, 'Hello World', { font: '"Press Start 2P"' });
```

您只能显示当前已装入且可供浏览器使用的字体: 因此字体必须预装. Phaser不会为您这样做, 因此您需要使用第3方字体加载器, 或者在您 Phaser游戏所居住的页面上, CSS 中可以备妥字体 。

移动浏览器中可用的默认字体,请参见 [this](http://www.jordanm.co.uk/tinytype).

性能说明: 每次文本对象的内容发生变化, 即更改显示的文本或文本样式, 它需要重新制作文本画布, 如果在 WebGL 上, 则将新纹理重新加载到 GPU 。 如果经常使用, 或者在游戏中有大量文本对象, 这将是一个昂贵的操作。 如果您遇到性能问题, 您最好使用 Bitmap Text , 因为它从批量中获利, 避免了昂贵的 Canvas API 调用 。

## 添加文本对象 {#add-text-object}

```javascript
var txt = this.add.text(x, y, 'hello');
// var txt = this.add.text(x, y, 'hello', { fontFamily: 'Arial', fontSize: 64, color: '#00ff00' });
```

默认样式

```javascript
{
    fontFamily: 'Courier',
    fontSize: '16px',
    fontStyle: '',
    backgroundColor: null,
    color: '#fff',
    stroke: '#fff',
    strokeThickness: 0,
    shadow: {
        offsetX: 0,
        offsetY: 0,
        color: '#000',
        blur: 0,
        stroke: false,
        fill: false
    },
    align: 'left',  // 'left'|'center'|'right'|'justify'
    padding: {
        left: 0,
        right: 0,
        top: 0,
        bottom: 0,
    },
    maxLines: 0,
    lineSpacing: 0,
    fixedWidth: 0,
    fixedHeight: 0,
    rtl: false,
    testString: '|MÉqgy',
    wordWrap: {
        width: null,
        callback: null,
        callbackScope: null,
        useAdvancedWrap: false
    },
    metrics: false,
    // metrics: {
    //     ascent: 0,
    //     descent: 0,
    //     fontSize: 0
    // },
}
```

从 JSON 添加文字

```javascript
var txt = this.make.text({
    x: 100,
    y: 100,
    padding: {
        left: 64,
        right: 16,
        top: 20,
        bottom: 40
        //x: 32,    // 32px padding on the left/right
        //y: 16     // 16px padding on the top/bottom
    },
    text: 'Text\nGame Object\nCreated from config',
    style: {
        fontSize: '64px',
        fontFamily: 'Arial',
        color: '#ffffff',
        align: 'center',  // 'left'|'center'|'right'|'justify'
        backgroundColor: '#ff00ff'
    },
    // origin: {x: 0.5, y: 0.5},
    add: true
});
```

## 自定义类 {#custom-class}

- 定义类

    ```javascript
    class MyText extends Phaser.GameObjects.Text {
        constructor(scene, x, y, text, style) {
            super(scene, x, y, text, style);
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
    var txt = new MyText(scene, x, y, 'hello');
    ```

## 文字包换 {#word-wrap}

- 以宽度环绕

    ```javascript
    var txt = this.make.text({
        x: 400,
        y: 100,
        text: 'The sky above the port was the color of television, tuned to a dead channel.',
        origin: { x: 0.5, y: 0.5 },
        style: {
            font: 'bold 25px Arial',
            fill: 'white',
            wordWrap: { width: 300 }
        },
        // origin: {x: 0.5, y: 0.5},
    });
    ```

- 以回调方式环绕

    ```javascript
    var txt = this.make.text({
        x: 400,
        y: 300,
        text: 'The sky above the port was the color of television, tuned to a dead channel.',
        origin: 0.5,
        style: {
            font: 'bold 30px Arial',
            fill: 'white',
            wordWrap: { callback: wordWrap, scope: this }
        },
        // origin: {x: 0.5, y: 0.5},
    });
    
    function wordWrap (text, textObject)
    {
        // First parameter will be the string that needs to be wrapped
        // Second parameter will be the Text game object that is being wrapped currently
    
        // This wrap just puts each word on a separate line, but you could inject your own
        // language-specific logic here.
        var words = text.split(' ');
    
        // You can return either an array of individual lines or a string with line breaks (e.g. \n) in
        // the correct place.
        return words;
    }
    ```

- 环绕宽度
  - Get

    ```javascript
    var width = txt.style.wordWrapWidth;
    var useAdvancedWrap = txt.style.wordWrapUseAdvanced;
    ```

  - Set

    ```javascript
    txt.setWordWrapWidth(width);
    // txt.setWordWrapWidth(width, useAdvancedWrap);
    ```

- 环绕回调
  - Get

    ```javascript
    var callback = txt.style.wordWrapCallback;
    var scope = txt.style.wordWrapCallbackScope;
    ```

  - Set

    ```javascript
    txt.setWordWrapCallback(callback, scope);
    ```

## 内容 {#content}

- Get

    ```javascript
    var content = txt.text;
    ```

- Set

    ```javascript
    txt.setText(text);
    // txt.text = text;
    ```

- Append

    ```javascript
    txt.appendText(text);
    // txt.text += '\n' + text;
    ```

    or

    ```javascript
    txt.appendText(text, false);
    // txt.text += text;
    ```

## 设置样式 {#set-style}

```javascript
txt.setStyle(style);
txt.setFont(font);
txt.setFontFamily(family);
txt.setFontSize(size);
txt.setFontStyle(style);
```

## 设定对齐 {#set-align}

```javascript
txt.setAlign(align);
```

- `align` : `'left'`, `'center'`, `'right'`, `'justify'`

## 颜色 {#color}

- 文本颜色
  - Get

    ```javascript
    var color = txt.style.color;
    ```

  - Set

    ```javascript
    txt.setColor(color);
    ```

    or

    ```javascript
    txt.setFill(color);
    ```

- 弦色, 厚度
  - Get

    ```javascript
    var color = txt.style.stroke;
    var thickness = txt.style.strokeThickness;
    ```

  - Set

    ```javascript
    txt.setStroke(color, thickness);
    ```

  - Clear

    ```javascript
    txt.setStroke();
    ```

- 背景颜色
  - Get

    ```javascript
    var color = txt.style.backgroundColor;
    ```

  - Set

    ```javascript
    txt.setBackgroundColor(color);
    ```

- Shadow
  - Get

    ```javascript
    var color = txt.style.shadowColor;
    var offsetX = txt.style.shadowOffsetX;
    var offsetY = txt.style.shadowOffsetY;
    var blur = txt.style.shadowBlur;
    var stroke = txt.style.shadowStroke;
    var enabled = txt.style.shadowFill;
    ```

  - Set

    ```javascript
    txt.setShadow(x, y, color, blur, shadowStroke, shadowFill);
    txt.setShadowOffset(x, y);
    txt.setShadowColor(color);
    txt.setShadowBlur(blur);
    txt.setShadowStroke(enabled);
    txt.setShadowFill(enabled);
    ```

## 线条间隔 {#line-spacing}

此值在计算整行高度时被 * 添加到字体的高度 。

- Get

   ```javascript
   var lineSpacing = txt.lineSpacing;
   ```

- Set

   ```javascript
   txt.setLineSpacing(value);
   ```

## 字母间隔 {#letter-spacing}

- Get

   ```javascript
   var letterSpacing = txt.letterSpacing;
   ```

- Set

   ```javascript
   txt.setLetterSpacing(value);
   ```

  - `value` :正值或负值。

!!! note
    启用此特性将会导致 Phaser 使此文本对象中的每个字符都生效
    逐个,而不是用一个图来表示整个字符串。
    这使得它使用时,无论是长弦还是总共很多弦,都变得极其昂贵.

## 铺垫 {#padding}

- Get

    ```javascript
    var left = txt.padding.left;
    var top = txt.padding.top;
    var right = txt.padding.right;
    var bottom = txt.padding.bottom;
    ```

- Set

    ```javascript
    txt.setPadding(left, top, right, bottom);
    // txt.setPadding(padding); // padding: {left, top, right, bottom}
    ```

## 最大行数 {#max-lines}

- Get

    ```javascript
    var maxLines = txt.style.maxLines;
    ```

- Set

    ```javascript
    txt.setMaxLines(max);
    ```

## 固定大小 {#fixed-size}

- Get

    ```javascript
    var width = txt.style.fixedWidth;
    var height = txt.style.fixedHeight;
    ```

- Set

    ```javascript
    txt.setFixedSize(width, height);
    ```

## 测试字符串 {#test-string}

设置测量字体时使用的测试字符串 。

```javascript
txt.style.setTestString(text);
```

## RTL 语言 {#rtl}

- 创建此文本游戏对象时, 将 `rtl` 设置为样式配置
- 运行时更改 `rtl`

    ```javascript
    txt.setRTL(rtl).setText(newContent);
    ```

  - 在设定新内容前,请使用 `setRTL` 方法 。

## 其他属性 {#other-properties}

见[game object](/guide/concepts/gameobjects)

## 创建遮罩 {#create-mask}

```javascript
var mask = txt.createBitmapMask();
```

见[mask](/guide/concepts/display#masks)

## 着色器效果 {#shader-effects}

支持 [preFX and postFX effects](/guide/concepts/gameobjects/shader) 软件

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
