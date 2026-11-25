# Phaser.GameObjects.RetroFont {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-retrofont)

Scope: 
static
> 源码：[src/gameobjects/bitmaptext/RetroFont.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/RetroFont.js#L10)  
引入版本：3.6.0

## 静态函数 {#static-functions}

### TEXT_SET1 {#TEXT_SET1}

#### TEXT_SET1: string {#text_set1-string}


**说明:**

一个RetroFont字符集,包含完整的可打印的ASCII范围(通过tide的空间),包括大写和小写字母,数字,和符号.

文本集 1 = !\ #$  ()  (  ), -. /0123456789:  (  )? @ ABCDEFGHIJKLMNOPQLSTUVWXYZ [\\]   abcdefghijklmnopqrstuvwxyz


> 源码：[src/gameobjects/bitmaptext/const.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/const.js#L9)  
引入版本：3.6.0


---

### TEXT_SET10 {#TEXT_SET10}

#### TEXT_SET10: string {#text_set10-string}


**说明:**

仅包含字母表的26个大写字母的RetroFont字符集。用于没有数字、空格或页格的字体图案工作表。

文本集 10 = ABCDEFGHIJKLMNOPQRSTUVWXYZ 语言


> 源码：[src/gameobjects/bitmaptext/const.js#L118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/const.js#L118)  
引入版本：3.6.0


---

### TEXT_SET11 {#TEXT_SET11}

#### TEXT_SET11: string {#text_set11-string}


**说明:**

一个包含大写字母的RetroFont字符集,一个包括引号及算术操作符在内的泛选的平调符号,后面是数字.

文本集11 = ABCDEFGHIJKLMNOPQRSTUVWXYZ.,"-+!!!''()'''''';0123456789 ="  "(")"(")".


> 源码：[src/gameobjects/bitmaptext/const.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/const.js#L130)  
引入版本：3.6.0


---

### TEXT_SET2 {#TEXT_SET2}

#### TEXT_SET2: string {#text_set2-string}


**说明:**

一个RetroFont字符集,通过大写Z从空间中包含可打印的ASCII字符,包括数字和常见符号,但没有小写字母.

文本集2=!#$  '()  , -. /0123456789:  ? @ABCDEFGHIJKLMNOPQRSTUVWXYZ


> 源码：[src/gameobjects/bitmaptext/const.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/const.js#L21)  
引入版本：3.6.0


---

### TEXT_SET3 {#TEXT_SET3}

#### TEXT_SET3: string {#text_set3-string}


**说明:**

包含大写字母的RetroFont字符集,后面是数字,并带有一个后缀空间.

文本集 3 = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 文本集 3 = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 文本集 3 = ABCDEFGHIJKLMNOPQRSTUVVVWXYZ0123456789 文本集 文本集 3 文本集 3 = ABCDEFGHIJLMNQLQRSTUVVVWXYZ0123456789


> 源码：[src/gameobjects/bitmaptext/const.js#L33](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/const.js#L33)  
引入版本：3.6.0


---

### TEXT_SET4 {#TEXT_SET4}

#### TEXT_SET4: string {#text_set4-string}


**说明:**

包含大写字母、空格、然后是数字的RetroFont字符集。该字符出现在字母和数字之间,而不是在结尾。

文本集 4 = ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 = 翻译: 刘晓 翻译: 刘晓 翻译: 陈晓 翻译: 陈晓 翻译: 陈晓 翻译: 陈晓 陈晓 翻译: 陈晓 陈晓 翻译: 陈晓 翻译: 陈晓 陈晓 翻译:


> 源码：[src/gameobjects/bitmaptext/const.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/const.js#L44)  
引入版本：3.6.0


---

### TEXT_SET5 {#TEXT_SET5}

#### TEXT_SET5: string {#text_set5-string}


**说明:**

包含大写字母的 RetroFont 字符集,后面是常见的 punctuation 符号和数字。对于包含句子 punctuation, 如时段、逗号、括号和问号的字体, 很有用 。

文本集 5 = ABCDEFGHIJKLMNOPQRSTUVWXYZ.,/() '? -*:0123456789


> 源码：[src/gameobjects/bitmaptext/const.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/const.js#L56)  
引入版本：3.6.0


---

### TEXT_SET6 {#TEXT_SET6}

#### TEXT_SET6: string {#text_set6-string}


**说明:**

一个RetroFont字符集,包含大写字母,数字,以及一系列的标点符号,包括引号,括号,以及一个后缀空间.

文本集6 = ABCDEFGHIJKLMNOPQRSTUVWXYZ!??:0123456789"(),-.


> 源码：[src/gameobjects/bitmaptext/const.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/const.js#L69)  
引入版本：3.6.0


---

### TEXT_SET7 {#TEXT_SET7}

#### TEXT_SET7: string {#text_set7-string}


**说明:**

一组RetroFont字符, 字符排列顺序为非顺序的, 互开。 这符合某些Retro字体工作表的图示布局, 每五个字符都延续序列( A, G, M, S, Y, 然后是 B, H, N, T, Z等) 。

文本集 7 = AGMSY+: 4BHNTZ!; 5CIOU.?06DJPV, (17EKQW") 28FLRX-'39


> 源码：[src/gameobjects/bitmaptext/const.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/const.js#L81)  
引入版本：3.6.0


---

### TEXT_SET8 {#TEXT_SET8}

#### TEXT_SET8: string {#text_set8-string}


**说明:**

复古字体字符集,数字先出现,然后是空格、周期,然后是大写字母。当字体图示表将数字放在字母表之前时使用此字符集。

文本集8=0123456789. ABCDEFGHIJKLMNOPQRSTUVWXYZ 互联网档案馆的存档,存档日期2013-09-02.


> 源码：[src/gameobjects/bitmaptext/const.js#L94](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/const.js#L94)  
引入版本：3.6.0


---

### TEXT_SET9 {#TEXT_SET9}

#### TEXT_SET9: string {#text_set9-string}


**说明:**

包含大写字母,括号和一个连字符,数字,以及包括引号在内的常用句子的调值,以及感叹标记的 RetroFont字符集.

文本集9 = ABCDEFGHIJKLMNOPQRSTUVWXYZ ()-0123456789.,'?)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


> 源码：[src/gameobjects/bitmaptext/const.js#L106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/const.js#L106)  
引入版本：3.6.0


---

## 静态函数 {#static-functions-1}

### Parse {#Parse}

#### \<static> Parse(scene, config) {#static-parsescene-config}


**说明:**

分析一个 Retro 字体配置对象,并构建一个 `BitmapFontData` 结构,可以传递到 BitmapText 构造器,以使用固定的宽度 retro 字体渲染文本.

复古字体是一个包含一个统一的字符网格的纹理,每个单元格的宽度和高度都是一样的。这个函数读取配置,查看源纹理框架,然后在`config.chars`定义的每个字符上进行重排,计算其像素位置和纹理内正常的紫外线坐标。生成的数据对象将每个字符代码映射到自己的格律条目,并适合在Bitmap字体缓存中注册。

如果 `config.chars` 是空字符串,则函数返回 `undefined` 而不产生任何数据 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 参考Phaser场景. |
| config | [Phaser.Types.GameObjects.BitmapText.RetroFontConfig](/api/typedef/types-gameobjects-bitmaptext#retrofontconfig) | 否 | 字体配置对象 。 |


**返回值:** [Phaser.Types.GameObjects.BitmapText.BitmapFontData](/api/typedef/types-gameobjects-bitmaptext#bitmapfontdata) - 解析的位图字体数据条目,包含每个字符的格言数据和紫外坐标,准备用于位图字体缓存.


> 源码：[src/gameobjects/bitmaptext/ParseRetroFont.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/ParseRetroFont.js#L9)  
引入版本：3.0.0


---

---
