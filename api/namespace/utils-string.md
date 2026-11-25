# Phaser.Utils.String {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/utils-string)

Scope: 
static
> 源码：[src/utils/string/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/string/index.js#L7)  


## 静态函数 {#static-functions}

### Format {#Format}

#### \<static> Format(string, values) {#static-formatstring-values}


**说明:**

取字符串, 并用给定数组中的值替换标记实例。 标记的形式为 `%1`、 `%2`等。 例如:

`Format("The %1 is worth %2 gold", [ 'Sword', 500 ])`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| string | string | 否 | 包含替换标记的字符串 。 |
| values | array | 否 | 包含将替换标记的数值的数组。如果没有数值,则插入空字符串。 |


**返回值:** string - 包含替换值的字符串 。


> 源码：[src/utils/string/Format.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/string/Format.js#L7)  
引入版本：3.0.0


---

### Pad {#Pad}

#### \<static> Pad(str, [len], [pad], [dir]) {#static-padstr-len-pad-dir}


**说明:**

使用指定的字符串, 将给定的字符串和垫子取出, 并按需要的长度, 例如, 如果您需要一个字符串, 需要长到 6 个字符, 您可以调用 :

`pad('bob', 6, '-', 2)`

这将返回: `bob---`,因为它已经添加到6个字符,使用右侧的 `-`.

也可以使用它来贴上数字( 它们总是作为字符串返回) :

`pad(512, 6, '0', 1)`

返回: `000512` 左侧加线。

如果你不指明方向,双方就会同意:

`pad('c64', 7, '*')`

将返回: `**c64**`

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| str | string \| number | object | 否 |  | 目标字符串. `toString()`将调用在字符串上,这意味着您也可以通过像数字这样的常见数据类型. |
| len | number | 是 | 0 | 由此产生的加长字符串的总长度 。 |
| pad | string | 是 | "\" \"" | 用( 默认为空格) 来铺设它 的字符串 。 |
| dir | number | 是 | 3 | 方向 dir = 1 (左), 2 (右), 3 (双). |


**返回值:** string - 补弦.


> 源码：[src/utils/string/Pad.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/string/Pad.js#L7)  
引入版本：3.0.0


---

### RemoveAt {#RemoveAt}

#### \<static> RemoveAt(string, index) {#static-removeatstring-index}


**说明:**

取字符串并删除给定索引中的字符。

指数为零。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| string | string | 否 | 弦乐要修. |
| index | number | 否 | 要删除的字符索引。 此值为零 。 |


**返回值:** string - 修改过的字符串 。


> 源码：[src/utils/string/RemoveAt.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/string/RemoveAt.js#L7)  
引入版本：3.50.0


---

### Reverse {#Reverse}

#### \<static> Reverse(string) {#static-reversestring}


**说明:**

取给定的字符串并反转, 返回倒转的字符串。 例如, 如果给定的字符串 `Atari 520ST`, 则返回 `TS025 iratA` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| string | string | 否 | 须逆之弦. |


**返回值:** string - 倒转的弦.


> 源码：[src/utils/string/Reverse.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/string/Reverse.js#L7)  
引入版本：3.0.0


---

### UppercaseFirst {#UppercaseFirst}

#### \<static> UppercaseFirst(str) {#static-uppercasefirststr}


**说明:**

如果有字符串,则大写第一个字母。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| str | string | 否 | 用来利用的字符串 。 |


**返回值:** string - 新的字符串,与第一个相同,但第一个字母被资本化了.


> 源码：[src/utils/string/UppercaseFirst.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/string/UppercaseFirst.js#L7)  
引入版本：3.0.0


---

### UUID {#UUID}

#### \<static> UUID() {#static-uuid}


**说明:**

创建并返回一个符合的 RFC4122 版本 4 的 UUID 。

弦形为:`xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx`,其中每张`x`被从0到f的随机十六进制数字取代,`y`被从8到b的随机十六进制数码取代.


**返回值:** string - 用户界面字符串。


> 源码：[src/utils/string/UUID.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/string/UUID.js#L7)  
引入版本：3.12.0


---

---
