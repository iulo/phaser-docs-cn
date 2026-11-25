# Types.GameObjects.Text {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-text)

## GetTextSizeObject {#gettextsizeobject}

### \<static> GetTextSizeObject {#static-gettextsizeobject}


调用到 GetTextsize 的结果对象 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 文本对象中最长行的宽度。 |
| height | number | 否 | 文本对象的高度 。 |
| lines | number | 否 | 文本对象中的行数。 |
| lineWidths | Array.\<number> | 否 | 文本对象中每行的行数组。 |
| lineSpacing | number | 否 | 文本对象的行距。 |
| lineHeight | number | 否 | 字体和中风中线的高度。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.Text
> 源码：[src/gameobjects/text/typedefs/GetTextSizeObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/typedefs/GetTextSizeObject.js#L1)  
引入版本：3.0.0

---

## TextConfig {#textconfig}

### \<static> TextConfig {#static-textconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| text | string \| Array.\<string> | 是 | 此文本对象将显示的文本 。 |
| style | [Phaser.Types.GameObjects.Text.TextStyle](/api/typedef/types-gameobjects-text#textstyle) | 是 | 文本样式配置对象。 |
| padding | [Phaser.Types.GameObjects.Text.TextPadding](/api/typedef/types-gameobjects-text#textpadding) | 是 | 一个文本铺设对象 。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.Text
> 源码：[src/gameobjects/text/typedefs/TextConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/typedefs/TextConfig.js#L1)  
引入版本：3.0.0

---

## TextMetrics {#textmetrics}

### \<static> TextMetrics {#static-textmetrics}


文本样式对象的字体参数。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ascent | number | 否 | 字体的升华。 |
| descent | number | 否 | 字体的降序. |
| fontSize | number | 否 | 字体大小 。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.Text
> 源码：[src/gameobjects/text/typedefs/TextMetrics.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/typedefs/TextMetrics.js#L1)  
引入版本：3.0.0

---

## TextPadding {#textpadding}

### \<static> TextPadding {#static-textpadding}


文本样式所用的文本铺设配置对象。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 是 | 如果设置此值, 则用于左右的垫。 Name |
| y | number | 是 | 如果设置此值, 则用于上下粘贴 。 |
| left | number | 是 | 文本对象左侧添加的粘贴量 。 |
| right | number | 是 | 文本对象右侧添加的贴子量 。 |
| top | number | 是 | 文本对象顶部添加的粘贴量 。 |
| bottom | number | 是 | 文本对象底部添加的粘贴量 。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.Text
> 源码：[src/gameobjects/text/typedefs/TextPadding.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/typedefs/TextPadding.js#L1)  
引入版本：3.18.0

---

## TextShadow {#textshadow}

### \<static> TextShadow {#static-textshadow}


文本样式所用的文本阴影配置对象。

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| offsetX | number | 是 | 0 | 阴之横向偏移. |
| offsetY | number | 是 | 0 | 阴之垂直偏. |
| color | string | 是 | "'#000'" | 阴影的颜色,作为 CSS 字符串值给出 。 |
| blur | number | 是 | 0 | 模糊度被应用到阴影中。 离开为 0 表示硬阴影 。 |
| stroke | boolean | 是 | false | 将阴影应用到文本对象的中风效果中? |
| fill | boolean | 是 | false | 将阴影应用到文本对象的填充效果中吗 ? |

**类型**: object

**所属**: Phaser.Types.GameObjects.Text
> 源码：[src/gameobjects/text/typedefs/TextShadow.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/typedefs/TextShadow.js#L1)  
引入版本：3.0.0

---

## TextStyle {#textstyle}

### \<static> TextStyle {#static-textstyle}


文本游戏对象所用的文本样式配置对象。

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| fontFamily | string | 是 | "'Courier'" | 文本对象将渲染的字体。 这是 Canvas 样式的字体字符串 。 |
| fontSize | number \| string | 是 | "'16px'" | 字体大小,作为 CSS 大小字符串. |
| fontStyle | string | 是 |  | 任何添加的字体样式, 如“ 粗体 ” 。 |
| font | string | 是 |  | 要设置的字体家族或字体设置。 覆盖其他字体设置。 |
| backgroundColor | string | 是 |  | 文本对象后面的固态填充颜色。 以 `#ff0` 等 CSS 字符串颜色为背景 。 |
| color | string \| CanvasGradient | CanvasPattern | 是 | "'#fff'" | 文字的颜色。 以 CSS 字符串颜色如 `#fff` 或 `rgb()` 。 |
| stroke | string \| CanvasGradient | CanvasPattern | 是 | "'#fff'" | 如果 `strokeThickness` 属性大于 0, 则按下文字所用的颜色 。 |
| strokeThickness | number | 是 | 0 | 文字周围的描边粗细。 设置为零, 以不中风 。 |
| shadow | [Phaser.Types.GameObjects.Text.TextShadow](/api/typedef/types-gameobjects-text#textshadow) | 是 |  | 文本阴影配置对象 。 |
| padding | [Phaser.Types.GameObjects.Text.TextPadding](/api/typedef/types-gameobjects-text#textpadding) | 是 |  | 一个文本铺设对象 。 |
| align | string | 是 | "'left'" | 文本的对齐。仅影响多行文本。 `left`, `right`, `center` 或 或 时 间 `justify`. |
| maxLines | number | 是 | 0 | 文本对象内显示的最大行数。 |
| fixedWidth | number | 是 | 0 | 强制文本对象在此属性中指定精确的宽度。 留为零, 以便它相应更改内容 。 |
| fixedHeight | number | 是 | 0 | 强制文本对象在此属性中指定精确的高度。 留为零, 以便它相应更改内容 。 |
| resolution | number | 是 | 0 | 设置文本对象的分辨率(DPI)。将零留到零,以便使用游戏分辨率。 |
| rtl | boolean | 是 | false | 如果文本对象从右到左渲染, 则设定为 `true` 。 |
| testString | string | 是 | "'\|MÃ‰qgy'" | 这是用来帮助Canvas计算字体高度的字符串. |
| baselineX | number | 是 | 1.2 | 水平加码的量在计算字体度量时会增加文字的宽度. |
| baselineY | number | 是 | 1.4 | 计算字体度量时,垂直加码的量会加到文字的高度. |
| wordWrap | [Phaser.Types.GameObjects.Text.TextWordWrap](/api/typedef/types-gameobjects-text#textwordwrap) | 是 |  | 文本文字包配置对象 。 |
| metrics | [Phaser.Types.GameObjects.Text.TextMetrics](/api/typedef/types-gameobjects-text#textmetrics) | 是 |  | 一个文本量度对象。 使用此工具可以避免文本重游戏中昂贵的字体大小计算 。 |
| lineSpacing | number | 是 |  | 增加字体高度的金额,以实现整体线高. |
| letterSpacing | number | 是 |  | 字符间距的加法。可以是负数或正数。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.Text
> 源码：[src/gameobjects/text/typedefs/TextStyle.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/typedefs/TextStyle.js#L1)  
引入版本：3.0.0

---

## TextWordWrap {#textwordwrap}

### \<static> TextWordWrap {#static-textwordwrap}


文本样式配置所用的文本文字包配置对象。

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 是 |  | 文字的文字包装应考虑的宽度 。 |
| callback | TextStyleWordWrapCallback | 是 |  | 启用文字包时提供自定义的回调 。 |
| callbackScope | any | 是 |  | 引用“ 包” 一词的上下文 。 |
| useAdvancedWrap | boolean | 是 | false | 使用基本或高级的字包包装吗 ? |

**类型**: object

**所属**: Phaser.Types.GameObjects.Text
> 源码：[src/gameobjects/text/typedefs/TextWordWrap.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/typedefs/TextWordWrap.js#L1)  
引入版本：3.0.0

---

---
