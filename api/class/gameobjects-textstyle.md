# TextStyle {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-textstyle)

一个文本样式类管理文本对象的所有样式设置。

文本游戏对象自动创建文本样式实例,通过 `Text.style` 属性访问。您通常不需要自己即时访问。

**构造函数**

`new TextStyle(text, style)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| text | [Phaser.GameObjects.Text](/api/class/gameobjects-text) | 否 | 文本对象此文本样式 。 |
| style | [Phaser.Types.GameObjects.Text.TextStyle](/api/typedef/types-gameobjects-text#textstyle) | 否 | 要设置的样式设置 。 |

---


**作用域**: static

> 源码：[src/gameobjects/text/TextStyle.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L43)  
引入版本：3.0.0

## 公开成员 {#public-members}

### align {#align}

#### align: string {#align-string}


**说明:**

文本对齐.


> 源码：[src/gameobjects/text/TextStyle.js#L202](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L202)  
引入版本：3.0.0


---

### backgroundColor {#backgroundColor}

#### backgroundColor: string {#backgroundcolor-string}


**说明:**

后色相为.


> 源码：[src/gameobjects/text/TextStyle.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L103)  
引入版本：3.0.0


---

### baselineX {#baselineX}

#### baselineX: number {#baselinex-number}


**说明:**

水平加码的量在计算字体度量时会增加文字的宽度.


> 源码：[src/gameobjects/text/TextStyle.js#L277](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L277)  
引入版本：3.3.0


---

### baselineY {#baselineY}

#### baselineY: number {#baseliney-number}


**说明:**

计算字体度量时,垂直加码的量会加到文字的高度.


> 源码：[src/gameobjects/text/TextStyle.js#L287](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L287)  
引入版本：3.3.0


---

### color {#color}

#### color: string, CanvasGradient, CanvasPattern {#color-string-canvasgradient-canvaspattern}


**说明:**

文字充色.


> 源码：[src/gameobjects/text/TextStyle.js#L112](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L112)  
引入版本：3.0.0


---

### fixedHeight {#fixedHeight}

#### fixedHeight: number {#fixedheight-number}


**说明:**

文字的固定高度.

`0`表示没有固定高度.


> 源码：[src/gameobjects/text/TextStyle.js#L234](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L234)  
引入版本：3.0.0


---

### fixedWidth {#fixedWidth}

#### fixedWidth: number {#fixedwidth-number}


**说明:**

文字的固定宽度 。

`0`表示没有固定宽度.


> 源码：[src/gameobjects/text/TextStyle.js#L222](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L222)  
引入版本：3.0.0


---

### fontFamily {#fontFamily}

#### fontFamily: string {#fontfamily-string}


**说明:**

字体家族.


> 源码：[src/gameobjects/text/TextStyle.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L74)  
引入版本：3.0.0


---

### fontSize {#fontSize}

#### fontSize: string, number {#fontsize-string-number}


**说明:**

字体大小 。


> 源码：[src/gameobjects/text/TextStyle.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L84)  
引入版本：3.0.0


---

### fontStyle {#fontStyle}

#### fontStyle: string {#fontstyle-string}


**说明:**

字体样式。


> 源码：[src/gameobjects/text/TextStyle.js#L94](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L94)  
引入版本：3.0.0


---

### maxLines {#maxLines}

#### maxLines: number {#maxlines-number}


**说明:**

绘制的最大行数 。


> 源码：[src/gameobjects/text/TextStyle.js#L212](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L212)  
引入版本：3.0.0


---

### parent {#parent}

#### parent: [Phaser.GameObjects.Text](/api/class/gameobjects-text) {#parent-phasergameobjectstext}


**说明:**

文本对象此文本样式 。


> 源码：[src/gameobjects/text/TextStyle.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L65)  
引入版本：3.0.0


---

### resolution {#resolution}

#### resolution: number {#resolution-number}


**说明:**

文本的分辨率被转换到内部画布上。 默认值为 0, 这意味着它会使用 Game Config 中设定的分辨率 。


> 源码：[src/gameobjects/text/TextStyle.js#L246](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L246)  
引入版本：3.12.0


---

### rtl {#rtl}

#### rtl: boolean {#rtl-boolean}


**说明:**

文本是否应当向左右移动 。


> 源码：[src/gameobjects/text/TextStyle.js#L257](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L257)  
引入版本：3.0.0


---

### shadowBlur {#shadowBlur}

#### shadowBlur: number {#shadowblur-number}


**说明:**

阴影模糊半径。


> 源码：[src/gameobjects/text/TextStyle.js#L172](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L172)  
引入版本：3.0.0


---

### shadowColor {#shadowColor}

#### shadowColor: string {#shadowcolor-string}


**说明:**

阴色.


> 源码：[src/gameobjects/text/TextStyle.js#L162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L162)  
引入版本：3.0.0


---

### shadowFill {#shadowFill}

#### shadowFill: boolean {#shadowfill-boolean}


**说明:**

是否启用阴影填充 。


> 源码：[src/gameobjects/text/TextStyle.js#L192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L192)  
引入版本：3.0.0


---

### shadowOffsetX {#shadowOffsetX}

#### shadowOffsetX: number {#shadowoffsetx-number}


**说明:**

横向阴影抵消。


> 源码：[src/gameobjects/text/TextStyle.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L142)  
引入版本：3.0.0


---

### shadowOffsetY {#shadowOffsetY}

#### shadowOffsetY: number {#shadowoffsety-number}


**说明:**

垂直阴影抵消。


> 源码：[src/gameobjects/text/TextStyle.js#L152](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L152)  
引入版本：3.0.0


---

### shadowStroke {#shadowStroke}

#### shadowStroke: boolean {#shadowstroke-boolean}


**说明:**

是否启用阴影中风 。


> 源码：[src/gameobjects/text/TextStyle.js#L182](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L182)  
引入版本：3.0.0


---

### stroke {#stroke}

#### stroke: string, CanvasGradient, CanvasPattern {#stroke-string-canvasgradient-canvaspattern}


**说明:**

文字描边颜色.


> 源码：[src/gameobjects/text/TextStyle.js#L122](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L122)  
引入版本：3.0.0


---

### strokeThickness {#strokeThickness}

#### strokeThickness: number {#strokethickness-number}


**说明:**

文字描边粗细.


> 源码：[src/gameobjects/text/TextStyle.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L132)  
引入版本：3.0.0


---

### testString {#testString}

#### testString: string {#teststring-string}


**说明:**

测量字体时使用的测试字符串 。


> 源码：[src/gameobjects/text/TextStyle.js#L267](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L267)  
引入版本：3.0.0


---

### wordWrapCallback {#wordWrapCallback}

#### wordWrapCallback: TextStyleWordWrapCallback, null {#wordwrapcallback-textstylewordwrapcallback-null}


**说明:**

用于包装文本的自定义函数。 它将收到两个参数: 文本( 要包装的字符串) , textObject( 这个文本实例) 。 它应该将包装的行作为数列返回, 或者作为有新线字符的字符串返回, 以指示中断点的位置。 设置此选项不会重运行字词包算法 。 要修改调用和重新包装, 请使用 [Phaser.GameObjects.TextStyle#setWordWrapCallback](/api/class/gameobjects-textstyle#setWordWrapCallback) 。


> 源码：[src/gameobjects/text/TextStyle.js#L309](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L309)  
引入版本：3.24.0


---

### wordWrapCallbackScope {#wordWrapCallbackScope}

#### wordWrapCallbackScope: object, null {#wordwrapcallbackscope-object-null}


**说明:**

引用 wordWrapCallback 时将应用的范围 。 直接设置此选项不会重运行字包算法 。 要更改调用和重包装, 请使用 [Phaser.GameObjects.TextStyle#setWordWrapCallback](/api/class/gameobjects-textstyle#setWordWrapCallback) 。


> 源码：[src/gameobjects/text/TextStyle.js#L324](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L324)  
引入版本：3.24.0


---

### wordWrapUseAdvanced {#wordWrapUseAdvanced}

#### wordWrapUseAdvanced: boolean {#wordwrapuseadvanced-boolean}


**说明:**

是否使用高级包线算法。 如果是真, 空格会崩溃, 空格会从线条中剪切。 如果是假的, 空格和空格会像现在一样留下。 直接设置此属性不会重运行词形包线算法。 要更改高级设置和重新包线, 请使用 [Phaser.GameObjects.TextStyle#setWordWrapWidth](/api/class/gameobjects-textstyle#setWordWrapWidth) 。


> 源码：[src/gameobjects/text/TextStyle.js#L336](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L336)  
引入版本：3.24.0


---

### wordWrapWidth {#wordWrapWidth}

#### wordWrapWidth: number, null {#wordwrapwidth-number-null}


**说明:**

文本的最大宽度以像素表示。 Null 表示不进行行包。 直接设置此属性不会重运行字包算法。 要更改宽度和重包装, 请使用 [Phaser.GameObjects.TextStyle#setWordWrapWidth](/api/class/gameobjects-textstyle#setWordWrapWidth) 。


> 源码：[src/gameobjects/text/TextStyle.js#L297](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L297)  
引入版本：3.24.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

破坏此文本样式 。


> 源码：[src/gameobjects/text/TextStyle.js#L1083](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L1083)  
引入版本：3.0.0


---

### getTextMetrics {#getTextMetrics}

#### \<instance> getTextMetrics() {#instance-gettextmetrics}


**说明:**

获取当前文本的参数 。


**返回值:** [Phaser.Types.GameObjects.Text.TextMetrics](/api/typedef/types-gameobjects-text#textmetrics) - 文字的度量衡.


> 源码：[src/gameobjects/text/TextStyle.js#L1042](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L1042)  
引入版本：3.0.0


---

### setAlign {#setAlign}

#### \<instance> setAlign([align]) {#instance-setalignalign}


**说明:**

设置此文本对象中文本的对齐 。

论点可以是: `left`, `right`, `center` 或 或 时 间 `justify`.

只有当文本对象有不止一行文字时,对齐才有效。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| align | string | 是 | "'left'" | 多行文本的文本对齐。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L1000](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L1000)  
引入版本：3.0.0


---

### setBackgroundColor {#setBackgroundColor}

#### \<instance> setBackgroundColor(color) {#instance-setbackgroundcolorcolor}


**说明:**

设置文本后面显示的背景颜色。 此处应该是一个 CSS 颜色字符串, 如 `'#ff0000'` 或 `'rgba(0,0,0,0.5)'` 。 设置为 `null` 以禁用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | string | 否 | 后色相为. |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L712](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L712)  
引入版本：3.0.0


---

### setColor {#setColor}

#### \<instance> setColor(color) {#instance-setcolorcolor}


**说明:**

设置文本填充颜色。 可以是任何有效的 CSS 颜色字符串、 CanvasGradient 或 CanvasPattern 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | string \| CanvasGradient | CanvasPattern | 否 | 文字充色. |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L746](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L746)  
引入版本：3.0.0


---

### setFill {#setFill}

#### \<instance> setFill(color) {#instance-setfillcolor}


**说明:**

设置文本填充颜色。 这可以是任何有效的 CSS 颜色字符串, 如六进制值 `'#ff0000'` 、 rgba 字符串 或命名的颜色 。 也可以是 CanvasGradient 或 CanvasPattern , 用于更复杂的填充样式 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | string \| CanvasGradient | CanvasPattern | 否 | 文字充色. |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L729](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L729)  
引入版本：3.0.0


---

### setFixedSize {#setFixedSize}

#### \<instance> setFixedSize(width, height) {#instance-setfixedsizewidth-height}


**说明:**

设置文本的固定宽度和高度 。

在`0`中通过其中任一参数分别禁用固定宽度或高度.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 要设置的固定宽度 。 |
| height | number | 否 | 固定高度要设置。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L681](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L681)  
引入版本：3.0.0


---

### setFont {#setFont}

#### \<instance> setFont(font, [updateText]) {#instance-setfontfont-updatetext}


**说明:**

设置字体 。

如果给出了字符串,则设置了字体家族.

如果给出了某个物体,则设定该物体的`fontFamily`,`fontSize`和`fontStyle`属性.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| font | string \| object | 否 |  | 要设置的字体家族或字体设置 。 |
| updateText | boolean | 是 | true | 是否立即更新文本 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L537](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L537)  
引入版本：3.0.0


---

### setFontFamily {#setFontFamily}

#### \<instance> setFontFamily(family) {#instance-setfontfamilyfamily}


**说明:**

设置字体家族。 这应该是有效的 CSS 字体家族值, 如 `'Arial'` 、 `'verdana'` 或 `'Courier'` 。 带有空格的字体名称应该用单引号, 如 `'Comic Sans MS'` 来包住 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| family | string | 否 | 字体家族. |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L593](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L593)  
引入版本：3.0.0


---

### setFontSize {#setFontSize}

#### \<instance> setFontSize(size) {#instance-setfontsizesize}


**说明:**

设置字体大小。 可以是带有效 CSS 单元的字符串, 即 `16px`, 或数字 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| size | number \| string | 否 | 字体大小 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L637](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L637)  
引入版本：3.0.0


---

### setFontStyle {#setFontStyle}

#### \<instance> setFontStyle(style) {#instance-setfontstylestyle}


**说明:**

设置字体样式, 如 `'bold'`、 `'italic'` 或 `'bold italic'`。 使用空字符串来清除样式 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| style | string | 否 | 字体样式。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L615](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L615)  
引入版本：3.0.0


---

### setMaxLines {#setMaxLines}

#### \<instance> setMaxLines([max]) {#instance-setmaxlinesmax}


**说明:**

设置要绘制的最大行数 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| max | number | 是 | 0 | 绘制的最大行数 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L1023](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L1023)  
引入版本：3.0.0


---

### setResolution {#setResolution}

#### \<instance> setResolution(value) {#instance-setresolutionvalue}


**说明:**

设置文本对象所使用的分辨率。

它允许在High DPI设备上更清晰的文本,因为其使用更大的内部Canvas纹理来进行文本的存储成本.

请小心使用,因为您拥有的文字越高,它使用的内存就越多.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 此文本的分辨率为对象 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L763](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L763)  
引入版本：3.12.0


---

### setShadow {#setShadow}

#### \<instance> setShadow([x], [y], [color], [blur], [shadowStroke], [shadowFill]) {#instance-setshadowx-y-color-blur-shadowstroke-shadowfill}


**说明:**

设置阴影设置 。

调用此方法总是重报父文本对象, 所以只有在您实际更改阴影设置时才调用它 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 横向阴影抵消。 |
| y | number | 是 | 0 | 垂直阴影抵消。 |
| color | string | 是 | "'#000'" | 阴色. |
| blur | number | 是 | 0 | 阴影模糊半径。 |
| shadowStroke | boolean | 是 | false | 是否要打中阴影. |
| shadowFill | boolean | 是 | true | 是否填满阴影. |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L818](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L818)  
引入版本：3.0.0


---

### setShadowBlur {#setShadowBlur}

#### \<instance> setShadowBlur([blur]) {#instance-setshadowblurblur}


**说明:**

设定阴影模糊半径 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| blur | number | 是 | 0 | 阴影模糊半径。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L896](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L896)  
引入版本：3.0.0


---

### setShadowColor {#setShadowColor}

#### \<instance> setShadowColor([color]) {#instance-setshadowcolorcolor}


**说明:**

设影色.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| color | string | 是 | "'#000'" | 阴色. |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L877](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L877)  
引入版本：3.0.0


---

### setShadowFill {#setShadowFill}

#### \<instance> setShadowFill(enabled) {#instance-setshadowfillenabled}


**说明:**

启用或禁用阴影填充 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| enabled | boolean | 否 | 是否启用阴影填充 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L932](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L932)  
引入版本：3.0.0


---

### setShadowOffset {#setShadowOffset}

#### \<instance> setShadowOffset([x], [y]) {#instance-setshadowoffsetx-y}


**说明:**

设阴偏.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 横向阴影抵消。 |
| y | number | 是 | 0 | 垂直阴影抵消。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L855](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L855)  
引入版本：3.0.0


---

### setShadowStroke {#setShadowStroke}

#### \<instance> setShadowStroke(enabled) {#instance-setshadowstrokeenabled}


**说明:**

启用或禁用阴影中风 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| enabled | boolean | 否 | 是否启用阴影中风 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L915](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L915)  
引入版本：3.0.0


---

### setStroke {#setStroke}

#### \<instance> setStroke(color, thickness) {#instance-setstrokecolor-thickness}


**说明:**

设置中风设置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | string \| CanvasGradient | CanvasPattern | 否 | 描边颜色. |
| thickness | number | 否 | 描边粗细。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L785](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L785)  
引入版本：3.0.0


---

### setStyle {#setStyle}

#### \<instance> setStyle(style, [updateText], [setDefaults]) {#instance-setstylestyle-updatetext-setdefaults}


**说明:**

设置文本样式。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| style | [Phaser.Types.GameObjects.Text.TextStyle](/api/typedef/types-gameobjects-text#textstyle) | 否 |  | 要设置的样式设置 。 |
| updateText | boolean | 是 | true | 是否立即更新文本 。 |
| setDefaults | boolean | 是 | false | 如果未设定, 则使用默认值, 或本地值 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L363](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L363)  
引入版本：3.0.0


---

### setTestString {#setTestString}

#### \<instance> setTestString(string) {#instance-setteststringstring}


**说明:**

设置测量字体时使用的测试字符串 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| string | string | 否 | 测量字体时使用的测试字符串 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L664](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L664)  
引入版本：3.0.0


---

### setWordWrapCallback {#setWordWrapCallback}

#### \<instance> setWordWrapCallback(callback, [scope]) {#instance-setwordwrapcallbackcallback-scope}


**说明:**

设置一个自定义的回调线条来包装 。

无法通过回调来删除包装 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| callback | TextStyleWordWrapCallback | 否 |  | 用于包装文本的自定义函数。 它将收到两个参数: 文本( 要包装的字符串) , textObject( 此文本实例) 。 它应该将包装的行作为数组或带有新行字符的字符串返回, 以指示中断点的发生地点 。 |
| scope | object | 是 | null | 引用回调时将适用的范围 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L974](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L974)  
引入版本：3.0.0


---

### setWordWrapWidth {#setWordWrapWidth}

#### \<instance> setWordWrapWidth(width, [useAdvancedWrap]) {#instance-setwordwrapwidthwidth-useadvancedwrap}


**说明:**

设置用于包线的宽度( 像素) 。

擦除宽度的包件时通过无值。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number \| null | 否 |  | 线条的最大宽度, 以像素表示。 设置为无法删除包线 。 |
| useAdvancedWrap | boolean | 是 | false | 是否使用高级的包线算法。 如果为真, 空格会崩溃, 空格会从线条中剪切。 如果错误, 空格和空格会照原样保留 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L949](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L949)  
引入版本：3.0.0


---

### syncFont {#syncFont}

#### \<instance> syncFont(canvas, context) {#instance-syncfontcanvas-context}


**说明:**

将字体设置同步到给定的 Canvas 渲染上下文 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| canvas | HTMLCanvasElement | 否 | 坎瓦斯元素(英语:Canvas Elements). |
| context | CanvasRenderingContext2D | 否 | 坎瓦斯渲染背景. |


> 源码：[src/gameobjects/text/TextStyle.js#L453](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L453)  
引入版本：3.0.0


---

### syncShadow {#syncShadow}

#### \<instance> syncShadow(context, enabled) {#instance-syncshadowcontext-enabled}


**说明:**

同步阴影设置到给定的 Canvas 渲染上下文 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| context | CanvasRenderingContext2D | 否 | 坎瓦斯渲染背景. |
| enabled | boolean | 否 | 阴影是否被启用 。 |


> 源码：[src/gameobjects/text/TextStyle.js#L488](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L488)  
引入版本：3.0.0


---

### syncStyle {#syncStyle}

#### \<instance> syncStyle(canvas, context) {#instance-syncstylecanvas-context}


**说明:**

将文本样式设置同步到给定的 Canvas 渲染上下文 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| canvas | HTMLCanvasElement | 否 | 坎瓦斯元素(英语:Canvas Elements). |
| context | CanvasRenderingContext2D | 否 | 坎瓦斯渲染背景. |


> 源码：[src/gameobjects/text/TextStyle.js#L467](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L467)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

构建此文本样式的 JSON 表示式 。


**返回值:** object - 用于此文本样式的 JSON 代表 。


> 源码：[src/gameobjects/text/TextStyle.js#L1061](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L1061)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update(recalculateMetrics) {#instance-updaterecalculatemetrics}


**说明:**

更新父文本对象的样式设置。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| recalculateMetrics | boolean | 否 | 是否重新计算字体和文本度量符 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 父文本对象 。


> 源码：[src/gameobjects/text/TextStyle.js#L515](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextStyle.js#L515)  
引入版本：3.0.0


---

---
