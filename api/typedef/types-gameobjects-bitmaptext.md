# Types.GameObjects.BitmapText {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-bitmaptext)

## BitmapFontCharacterData {#bitmapfontcharacterdata}

### \<static> BitmapFontCharacterData {#static-bitmapfontcharacterdata}


位图字体的单个字符的字体数据。



描述角色的位置,大小,偏移和克宁.



至3.50版本为止,它还包括WebGL纹理uv数据.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 角色的x位置. |
| y | number | 否 | 人物的y位置. |
| width | number | 否 | 字符的宽度 。 |
| height | number | 否 | 人物的高度(图). |
| centerX | number | 否 | 角色的中X位置. |
| centerY | number | 否 | 人物的中Y位置. |
| xOffset | number | 否 | 字符的x偏移。 |
| yOffset | number | 否 | 字符的y 折合数。 |
| u0 | number | 否 | WebGL 纹理u0. |
| v0 | number | 否 | WebGL 纹理 v0. |
| u1 | number | 否 | WebGL纹理u1. |
| v1 | number | 否 | WebGL 纹理 v1. |
| data | object | 否 | 字符的额外数据 。 |
| kerning | Object.\<number> | 否 | Kerning 值,按字符代码键. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.BitmapText
> 源码：[src/gameobjects/bitmaptext/typedefs/BitmapFontCharacterData.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/BitmapFontCharacterData.js#L1)  
引入版本：3.0.0

---

## BitmapFontData {#bitmapfontdata}

### \<static> BitmapFontData {#static-bitmapfontdata}


位图字体数据,可以被一个位图Text游戏对象使用.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| font | string | 否 | 字体名称 。 |
| size | number | 否 | 字体大小 。 |
| lineHeight | number | 否 | 字体的线高. |
| retroFont | boolean | 否 | 此字体是否为复古字体( monospace) 。 |
| chars | Object.\<number, [Phaser.Types.GameObjects.BitmapText.BitmapFontCharacterData](/api/typedef/types-gameobjects-bitmaptext#bitmapfontcharacterdata)> | 否 | 字体的字符数据,按字符代码键。每个字符数据包括一个位置、大小、偏移和更多。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.BitmapText
> 源码：[src/gameobjects/bitmaptext/typedefs/BitmapFontData.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/BitmapFontData.js#L1)  
引入版本：3.0.0

---

## BitmapTextCharacter {#bitmaptextcharacter}

### \<static> BitmapTextCharacter {#static-bitmaptextcharacter}


`BitmapTextSize`字符阵列的单个条目.

位置和尺寸考虑到字体大小,
,但不翻译为游戏对象本身的本地空间.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| i | number | 否 | 此字符在 BitmapText 包的文本字符串中的索引 。 |
| idx | number | 否 | BitmapText 文本字符串中的此字符索引 。 |
| char | string | 否 | 人物传. |
| code | number | 否 | 人物的人物代码. |
| x | number | 否 | BitmapText中字符的x位置. |
| y | number | 否 | 字符在位图图文集中的y位置 。 |
| w | number | 否 | 字符的宽度 。 |
| h | number | 否 | 人物的高度(图). |
| t | number | 否 | 此字符的顶部位置是上方. |
| r | number | 否 | 这个字符的右下角,包括xAdvance. |
| b | number | 否 | 此字符的底部为上. |
| line | number | 否 | 字符的行号出现于上. |
| glyph | [Phaser.Types.GameObjects.BitmapText.BitmapFontCharacterData](/api/typedef/types-gameobjects-bitmaptext#bitmapfontcharacterdata) | 否 | 引用此字符所用的格言对象 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.BitmapText
> 源码：[src/gameobjects/bitmaptext/typedefs/BitmapTextCharacter.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/BitmapTextCharacter.js#L1)  
引入版本：3.50.0

---

## BitmapTextConfig {#bitmaptextconfig}

### \<static> BitmapTextConfig {#static-bitmaptextconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| font | string | 是 | "''" | BitmapFont 缓存中要使用的字体的密钥 。 |
| text | string | 是 | "''" | 字符串,或字符串的数组,将设置为此位图文本的内容 。 |
| size | number \| false | 是 | false | 要设置的字体大小 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.BitmapText
> 源码：[src/gameobjects/bitmaptext/typedefs/BitmapTextConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/BitmapTextConfig.js#L1)  
引入版本：3.0.0

---

## BitmapTextLines {#bitmaptextlines}

### \<static> BitmapTextLines {#static-bitmaptextlines}


详细介绍`BitmapTextSize`对象中的行数据.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| shortest | number | 否 | 文本最短行的宽度 。 |
| longest | number | 否 | 最长行文字的宽度 。 |
| height | number | 否 | 一行文字的高度( ) 。 |
| lengths | Array.\<number> | 否 | 每个条目包含该行文字长度的数组。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.BitmapText
> 源码：[src/gameobjects/bitmaptext/typedefs/BitmapTextLines.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/BitmapTextLines.js#L1)  
引入版本：3.50.0

---

## BitmapTextSize {#bitmaptextsize}

### \<static> BitmapTextSize {#static-bitmaptextsize}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| global | [Phaser.Types.GameObjects.BitmapText.GlobalBitmapTextSize](/api/typedef/types-gameobjects-bitmaptext#globalbitmaptextsize) | 否 | 参考游戏对象的位置和规模,BitmapText的位置和大小. |
| local | [Phaser.Types.GameObjects.BitmapText.LocalBitmapTextSize](/api/typedef/types-gameobjects-bitmaptext#localbitmaptextsize) | 否 | 仅考虑字体大小的位图Text的位置和大小 。 |
| lines | [Phaser.Types.GameObjects.BitmapText.BitmapTextLines](/api/typedef/types-gameobjects-bitmaptext#bitmaptextlines) | 否 | 关于比特玛普Text内文字行的数据. |
| characters | Array.\<[Phaser.Types.GameObjects.BitmapText.BitmapTextCharacter](/api/typedef/types-gameobjects-bitmaptext#bitmaptextcharacter)> | 否 | 包含每个字符数据的阵列。 `includeChars` 只有在 `getTextBounds` 呼叫中才有 `true` 。 |
| words | Array.\<[Phaser.Types.GameObjects.BitmapText.BitmapTextWord](/api/typedef/types-gameobjects-bitmaptext#bitmaptextword)> | 否 | 包含 BitmapText 的单词数据的数组 。 |
| scale | number | 否 | 文本数据中正在渲染的比特玛普Text字体相对于字体大小的大小 。 |
| scaleX | number | 否 | 比特玛普Text的缩放值 X 。 |
| scaleY | number | 否 | 位图Text的缩放 Y 值 。 |
| wrappedText | string | 否 | 如果已启用并需要包扎, 则包裹的文字 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.BitmapText
> 源码：[src/gameobjects/bitmaptext/typedefs/BitmapTextSize.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/BitmapTextSize.js#L1)  
引入版本：3.0.0

---

## BitmapTextWord {#bitmaptextword}

### \<static> BitmapTextWord {#static-bitmaptextword}


有关`BitmapTextSize`对象字数组中单个世界条目的详情.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | BitmapText 中单词的 x 位置 。 |
| y | number | 否 | 字词在位图图文集中的y位置 。 |
| w | number | 否 | 字宽. |
| h | number | 否 | 字之高处. |
| i | number | 否 | 整个字符串中此词的第一个字符的索引。 注意: 此索引因子在空格、 引号、 车厢返回等中 。 |
| word | string | 否 | 字义. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.BitmapText
> 源码：[src/gameobjects/bitmaptext/typedefs/BitmapTextWord.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/BitmapTextWord.js#L1)  
引入版本：3.50.0

---

## DisplayCallbackConfig {#displaycallbackconfig}

### \<static> DisplayCallbackConfig {#static-displaycallbackconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | [Phaser.GameObjects.DynamicBitmapText](/api/class/gameobjects-dynamicbitmaptext) | 否 | 拥有此字符的动态位图文本对象正在渲染中 。 |
| tint | [Phaser.Types.GameObjects.BitmapText.TintConfig](/api/typedef/types-gameobjects-bitmaptext#tintconfig) | 否 | 人物的颜色 , 总是在 Canvas 中为零 。 |
| tintMode | [Phaser.TintModes](/api/namespace/tintmodes) | 否 | 正在渲染的字符的锡模式 。 |
| index | number | 否 | 正在渲染的字符索引 。 |
| charCode | number | 否 | 正在渲染的字符代码 。 |
| x | number | 否 | 正在显示的字符的 x 位置 。 |
| y | number | 否 | 正在显示的字符的y 位置 。 |
| scale | number | 否 | 正在渲染的字符的大小 。 |
| rotation | number | 否 | 正在呈现的字符的旋转 。 |
| data | any | 否 | 自定义数据随字符的提供而存储 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.BitmapText
> 源码：[src/gameobjects/bitmaptext/typedefs/DisplayCallbackConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/DisplayCallbackConfig.js#L1)  
引入版本：3.0.0

---

## DisplayCallback {#displaycallback}

### \<static> DisplayCallback {#static-displaycallback}

**类型**: function

**Member of**: Phaser.Types.GameObjects.BitmapText
> 源码：[src/gameobjects/bitmaptext/typedefs/DisplayCallbackConfig.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/DisplayCallbackConfig.js#L17)  


---

## GlobalBitmapTextSize {#globalbitmaptextsize}

### \<static> GlobalBitmapTextSize {#static-globalbitmaptextsize}


结合游戏对象的尺度和世界位置,将比图文本在全球空间中的位置和大小.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | BitmapText的x位置,考虑到游戏对象的x位置和规模. |
| y | number | 否 | 参考游戏对象的y位置和尺度,BitmapText的y位置. |
| width | number | 否 | 参考游戏对象的x尺度,比特玛普Text的宽度. |
| height | number | 否 | 位图Text的高度,考虑到游戏对象的y尺度. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.BitmapText
> 源码：[src/gameobjects/bitmaptext/typedefs/GlobalBitmapTextSize.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/GlobalBitmapTextSize.js#L1)  
引入版本：3.0.0

---

## JSONBitmapText {#jsonbitmaptext}

### \<static> JSONBitmapText {#static-jsonbitmaptext}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| font | string | 否 | 字体名称 。 |
| text | string | 否 | 此位图文本显示的文本 。 |
| fontSize | number | 否 | 字体大小 。 |
| letterSpacing | number | 否 | 添加/ 删除字符之间的间隔。 |
| lineSpacing | number | 否 | 在多行文本中添加/删除行间距。 |
| align | number | 否 | 多行比图Text对象中的文本对齐。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.BitmapText
> 源码：[src/gameobjects/bitmaptext/typedefs/JSONBitmapText.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/JSONBitmapText.js#L1)  
引入版本：3.0.0

---

## LocalBitmapTextSize {#localbitmaptextsize}

### \<static> LocalBitmapTextSize {#static-localbitmaptextsize}


本地空间中位图文本的位置和大小, 仅考虑字体大小 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 比特玛普Text的x位置. |
| y | number | 否 | 位图图文集的y位置 。 |
| width | number | 否 | 比特玛普Text的宽度. |
| height | number | 否 | 比特玛普Text的高度. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.BitmapText
> 源码：[src/gameobjects/bitmaptext/typedefs/LocalBitmapTextSize.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/LocalBitmapTextSize.js#L1)  
引入版本：3.0.0

---

## RetroFontConfig {#retrofontconfig}

### \<static> RetroFontConfig {#static-retrofontconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| image | string | 否 | 包含字体的图像键 。 |
| offset.x | number | 否 | 如果字体集不从给定图像左上方开始,请在此指定 X 坐标偏移 。 |
| offset.y | number | 否 | 如果字体集不从给定图像左上方开始,请在此指定 Y 坐标偏移 。 |
| width | number | 否 | 字体集中每个字符的宽度 。 |
| height | number | 否 | 字体集中每个字符的高度 。 |
| chars | string | 否 | 字体集中使用的字符,按显示顺序排列。您可以使用 TEXT_SET 缩写来进行常见字体集安排。 |
| charsPerRow | number | 否 | 字体集中每行字符数。 如果不给定 charsPerRow , 则将是图像宽度 / characterWidth 。 |
| spacing.x | number | 否 | 如果字体集中的字符之间有水平间距,则在此设定所需金额. |
| spacing.y | number | 否 | 如果字体集中的字符之间有垂直间隔,则在此设定所需金额。 |
| lineSpacing | number | 否 | 字体行高的垂直空间的量。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.BitmapText
> 源码：[src/gameobjects/bitmaptext/typedefs/RetroFontConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/RetroFontConfig.js#L1)  
引入版本：3.6.0

---

## TintConfig {#tintconfig}

### \<static> TintConfig {#static-tintconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| topLeft | number | 否 | 左上角的锡值, 画布中总是零 。 |
| topRight | number | 否 | 右上角的线性值, 画布中总是零 |
| bottomLeft | number | 否 | 左下方的锡值。 画布中总是零 。 |
| bottomRight | number | 否 | 右下方的线性值, 画布中总是零 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.BitmapText
> 源码：[src/gameobjects/bitmaptext/typedefs/TintConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/TintConfig.js#L1)  
引入版本：3.0.0

---

---
