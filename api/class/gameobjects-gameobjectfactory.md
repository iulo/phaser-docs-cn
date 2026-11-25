# GameObjectFactory {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-gameobjectfactory)

游戏对象工厂是一个场景插件,可以快速创建许多常见类型的游戏对象,并自动在场景注册,可以通过场景内部的`this.add`访问.

游戏对象直接在工厂注册,并将自己的创作方法注入类中.

**构造函数**

`new GameObjectFactory(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此游戏对象工厂所属景区 。 |

---


**作用域**: static

> 源码：[src/gameobjects/GameObjectFactory.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectFactory.js#L11)  
引入版本：3.0.0

## 公开方法 {#public-methods}

### arc {#arc}

#### \<instance> arc([x], [y], [radius], [startAngle], [endAngle], [anticlockwise], [fillColor], [fillAlpha]) {#instance-arcx-y-radius-startangle-endangle-anticlockwise-fillcolor-fillalpha}


**说明:**

创建新的Arc形状游戏对象,并添加到场景中.

注意:只有在Arc Game Object被建入Phaser时,此方法才会被使用.

Arc 形状是游戏对象,可以添加到景物、 组合或容器中。 您可以把它当作游戏中的其他对象, 如对它进行曲折、 缩放或允许输入或物理。 它为您提供了快速和容易的方法, 可以在游戏中不使用纹理来渲染此形状, 同时仍然利用在 WebGL 中被完全批量处理 。

此形状既支持填充颜色,也支持中风颜色.

当它显示弧形时, 您可以控制弧形的起始和结束角度, 或者这些角度是顺时针或逆时针旋转的。 默认设置会形成一个完整的圆形。 通过改变角度, 您可以创建其他的弧形, 如半圆形 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| radius | number | 是 | 128 | 弧的半径. |
| startAngle | number | 是 | 0 | 弧的起始角度,以度计. |
| endAngle | number | 是 | 360 | 弧的端角,以度计. |
| anticlockwise | boolean | 是 | false | 弧是否在起始角度和结束角度之间逆时针绘制。 `false` 时, 弧是顺时针绘制的 。 |
| fillColor | number | 是 |  | 弧的颜色会被填充,即0xff000为红色. |
| fillAlpha | number | 是 |  | 弧的α会被填充。 您也可以使用其`alpha`属性设置整个形状的α 。 |


**返回值:** [Phaser.GameObjects.Arc](/api/class/gameobjects-arc) - 创建的游戏对象 。


> 源码：[src/gameobjects/shape/arc/ArcFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/arc/ArcFactory.js#L10)  
引入版本：3.13.0


---

### bitmapText {#bitmapText}

#### \<instance> bitmapText(x, y, font, [text], [size], [align]) {#instance-bitmaptextx-y-font-text-size-align}


**说明:**

创建新的位图文本游戏对象,并添加到场景中。

BitmapText 对象通过取一个纹理文件以及描述字体结构的XML或JSON文件来工作.

在渲染过程中,每个文字字母都会被渲染到显示器,按比例间隔,并配合字体结构.

比特玛普Text对象不如Text对象灵活,因为它们具有较少的特性,如阴影、填充和能够使用Web字体,但您可以用这种灵活性来进行渲染速度。您还可以通过在图像编辑器中处理字体纹理、应用填充和所需的任何其他效果来创建视觉上具有说服力的比特玛普Texts。

要创建多行文本,请在文本字符串中插入\r,\n或\rn 逃逸代码.

要创建 BitmapText 数据文件, 您需要一个 3rd party app , 例如 :

BMFont(Windows,免费):[http://www.angelcode.com/products/bmfont/](http://www.angelcode.com/products/bmfont/) 格莱夫设计师(OS X,商用):[http://www.71squared.com/en/glyphdesigner](http://www.71squared.com/en/glyphdesigner) Littra(基于网络,免费):[http://kvazars.com/littera/](http://kvazars.com/littera/)

对于大多数使用的案例,建议使用XML。如果您想要使用JSON,格式化应当等于通过流行的X2JS库转换一个有效的XML文件的结果。这里可以找到一个转换的在线工具:[http://codebeautify.org/xmltojson](http://codebeautify.org/xmltojson)

注意:只有在将位图文字游戏对象建为Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 游戏对象的x位置. |
| y | number | 否 |  | 游戏对象的y位置 。 |
| font | string | 否 |  | BitmapFont 缓存中要使用的字体的密钥 。 |
| text | string \| Array.\<string> | 是 |  | 字符串,或字符串的数组,将设置为此位图文本的内容 。 |
| size | number | 是 |  | 要设置的字体大小 。 |
| align | number | 是 | 0 | 多行比图Text对象中的文本对齐。 |


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 创建的游戏对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapTextFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapTextFactory.js#L10)  
引入版本：3.0.0


---

### blitter {#blitter}

#### \<instance> blitter(x, y, texture, [frame]) {#instance-blitterx-y-texture-frame}


**说明:**

创建新的闪光游戏对象,并添加到场景中。

闪光器是一种特殊、高度优化的游戏对象, 设计用于渲染大量相同或类似的图像, 并且最小的俯仰。 闪光器不是为每个图像创建单独的游戏对象, 而是管理一个轻量级的 `Bob` 对象集合, 都具有相同的纹理。 这使得它对于粒子类效果、 人群、 弹道模式, 或者任何需要在高性能时显示许多相同图案的副本的情景都非常理想 。

注意:只有当闪光游戏对象已建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 游戏对象的x位置. |
| y | number | 否 | 游戏对象的y位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此游戏对象将使用用于渲染的纹理的密钥或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 | 闪光器默认框架子将使用 。 |


**返回值:** [Phaser.GameObjects.Blitter](/api/class/gameobjects-blitter) - 创建的游戏对象 。


> 源码：[src/gameobjects/blitter/BlitterFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/BlitterFactory.js#L10)  
引入版本：3.0.0


---

### captureFrame {#captureFrame}

#### \<instance> captureFrame(key) {#instance-captureframekey}


**说明:**

创建新的 CaptureFrame 游戏对象并将其添加到场景中。

ACaptionFrame 捕捉到显示列表中显示的 WebGL帧缓冲器的当前状态, 将结果存储为给定键所识别的纹理。 其他游戏对象可以引用此键来显示或处理捕获的图像。 这对全景后处理效果如水反射或屏幕- 空间扭曲很有用 。

这是 WebGL 唯一的特性, 无法在 Canvas 模式下工作。 相机必须启用 `forceComposite` , 或者捕获Frame 必须在帧缓冲上下文中( 如过滤器、 动态显示器或具有非默认的α值的相机) 。

注意:只有在将 CaptureFrame 游戏对象建为 Phaser 时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 用于存储被捕获的纹理的密钥。 其他游戏对象可以使用此密钥来引用被捕获的框架 。 |


**返回值:** [Phaser.GameObjects.CaptureFrame](/api/class/gameobjects-captureframe) - 创建的游戏对象 。


> 源码：[src/gameobjects/captureframe/CaptureFrameFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/captureframe/CaptureFrameFactory.js#L10)  
引入版本：4.0.0


---

### circle {#circle}

#### \<instance> circle([x], [y], [radius], [fillColor], [fillAlpha]) {#instance-circlex-y-radius-fillcolor-fillalpha}


**说明:**

创建新的圆形游戏对象,并添加到场景中。

A Circle 是一个弧形,固定的起始角为 0,端角为 360 度,所以它总是作为完整的圆形来制成。如果需要控制起始角和端角,请使用 `arc` 工厂方法。

注意:只有在Arc Game Object被建入Phaser时,此方法才会被使用.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| radius | number | 是 | 128 | 圆之半径. |
| fillColor | number | 是 |  | 圆圈的颜色会填充,即0xff000为红色. |
| fillAlpha | number | 是 |  | 圆圈的α将填充。您也可以使用其`alpha`属性设置整体形状的α 。 |


**返回值:** [Phaser.GameObjects.Arc](/api/class/gameobjects-arc) - 创建的游戏对象 。


> 源码：[src/gameobjects/shape/arc/ArcFactory.js#L46](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/arc/ArcFactory.js#L46)  
引入版本：3.13.0


---

### container {#container}

#### \<instance> container([x], [y], [children]) {#instance-containerx-y-children}


**说明:**

创建新的容器游戏对象,并添加到场景中。

容器是游戏对象的特殊类型,可以将其他游戏对象作为儿童持有。您可以使用容器将相关的游戏对象组合在一起,然后移动、旋转、缩放或设置容器的α,以同时影响其所有的孩子。儿童会相对于容器的位置和变换而成为容器,使容器可用于构建复合对象、UI面板,或任何应该一起移动的游戏对象。

注:只有在容器游戏对象已建为Phaser时,才能使用这种方法.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| children | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 是 |  | 用于添加到此容器的可选游戏对象, 或游戏对象阵列 。 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 创建的游戏对象 。


> 源码：[src/gameobjects/container/ContainerFactory.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/ContainerFactory.js#L11)  
引入版本：3.4.0


---

### curve {#curve}

#### \<instance> curve([x], [y], [curve], [fillColor], [fillAlpha]) {#instance-curvex-y-curve-fillcolor-fillalpha}


**说明:**

创建新的曲线形状游戏对象,并添加到场景中。

注意:只有在曲线游戏对象已建为Phaser时,此方法才会可用.

曲线形状是一个游戏对象,可以添加到景物,组或容器中。您可以把它像游戏中其它任何游戏对象一样对待,比如对它进行曲折,缩放,或者允许它输入或物理。它为您提供了快速和容易的方法,可以在游戏中不使用纹理来渲染此形状,同时仍然利用WebGL进行完整的批量处理.

此形状既支持填充颜色,也支持中风颜色.

要制作出曲线形状, 您必须先创建 `Phaser.Curves.Curve` 对象, 然后传递到构造器中的曲线形状 。

曲线形状还具有`smoothness`属性和相应的`setSmoothness`方法。这允许您通过控制构造过程中发生的迭代数量来控制形状在WebGL中是如何平滑的。 增减更平滑或更划线的形状的默认值。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| curve | [Phaser.Curves.Curve](/api/class/curves-curve) | 是 |  | 用于创建形状的曲线对象 。 |
| fillColor | number | 是 |  | 曲线的颜色会填充,即0xff000为红色. |
| fillAlpha | number | 是 |  | 曲线的α将被填充。您也可以使用其`alpha`属性设置整体形状的α 。 |


**返回值:** [Phaser.GameObjects.Curve](/api/class/gameobjects-curve) - 创建的游戏对象 。


> 源码：[src/gameobjects/shape/curve/CurveFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/curve/CurveFactory.js#L10)  
引入版本：3.13.0


---

### dom {#dom}

#### \<instance> dom(x, y, [element], [style], [innerText]) {#instance-domx-y-element-style-innertext}


**说明:**

DOM Element Game Objects 是控制并操纵HTML Elements在游戏顶端的一种方法.

DOM 元素要显示, 您必须加入以下游戏配置对象, 才能显示 :

```javascript
dom {
  createContainer: true
}
```

当添加此选项时, Phaser 会自动创建一个位于游戏画布顶部的 DOM 容器 div 。 此画布大小与画布相匹配, 如果画布大小发生变化, 由于在 Scale 管理器内设置, 则对  dom 容器进行相应的调整 。

您可以通过 DOM 元素在 DOM 环绕中通过, 或者通过一个引用当前想要置于 Phaser 控制之下的元素来创建 DOM 元素。 例如 :

```javascript
this.add.dom(x, y, 'div', 'background-color: lime; width: 220px; height: 100px; font: 48px Arial', 'Phaser');
```

上述代码将在给定的x/y坐标处将一个 div 元素插入 DOM 容器。 DOMSTring 在 4 参数中设置了 div 的初始 CSS 样式, 最终参数是内文本。 在这种情况下, 它将创建一个 石灰色 div, 大小为 220px 乘 100px, 其文本为 Phaser, 字体为 Arial 字体 。

您几乎应该毫无例外地使用明确大小的 HTML 元素,以便完全控制元素在常规游戏内容旁边的对齐和定位.

与其直接指定 CSS 和 HTML , 您可以使用 `load.html` 文件加载器将其加载到缓存中, 然后使用 `createFromCache` 方法。 您也可以使用 `createFromHTML` 和该类中可用的其他各种方法来帮助构建您的要素 。

一旦元素被创建, 您就可以像其他游戏对象一样控制它。 您可以设定它的位置、 尺度、 旋转、 α 等属性。 它会随着主要场景相机的移动而移动, 并在画布的边缘被剪辑。 必须记住 DOM 元素的一些限制: 显而易见的是它们出现在您的游戏画布上或下方。 您不能把它们混入显示列表, 也就是说您不能有一个 DOM 元素, 然后是 Sprite, 然后是另一个 DOM 元素。

无法启用它们来输入。 要做到这一点, 您必须使用 `addListener` 方法直接添加本地事件听器。 最后的限制是使用相机。 DOM 容器大小可以完全匹配游戏布, 并相应剪辑。 DOM Elements 尊重相机滚动和 scrollFactor 设置, 但是如果您改变相机的大小, 从而与画布的大小不再匹配, 就不会相应剪辑 。

此外,所有DOM元素都插入到同一个DOM容器中,不管它们是在哪个场景中创建的.

DOM Elements 是将本地 HTML 与您的 Phaser 游戏对象对齐的有力方法。 例如, 您可以在您的标题屏幕中直接插入多人游戏的登录表。 或者是高分表的文本输入框。 或者是来自 3rd 派对服务的横幅广告。 或者您想用它们来高分辨率文本显示和UI 。 选择权在你, 请记住您正在处理标的 HTML 和 CSS 浮在游戏顶部, 并应该相应处理它 。

注意:只有在DOM元素游戏对象已建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这个DOM元素在世界的横向位置. |
| y | number | 否 | 这个DOM元素在世界的垂直位置. |
| element | HTMLElement \| string | 是 | 已有的 DOM 元素, 或者字符串。 如果从 # 开始的字符串, 将会在字符串上进行 `getElementById` 的查询( 减去散列) 。 没有散列, 它代表要创建的元素类型, 即“ div ” 。 |
| style | string \| any | 是 | 如果字符串, 将直接设置为元素 `style` 属性值。 如果一个普通对象, 将被标注, 并传输值。 在这两种情况下, 值都会替换任何 CSS 样式 。 |
| innerText | string | 是 | 如果给出,将直接设定为元素`innerText`属性值,以取代之前的任意值。 |


**返回值:** [Phaser.GameObjects.DOMElement](/api/class/gameobjects-domelement) - 创建的游戏对象 。


> 源码：[src/gameobjects/domelement/DOMElementFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/DOMElementFactory.js#L10)  
引入版本：3.17.0


---

### dynamicBitmapText {#dynamicBitmapText}

#### \<instance> dynamicBitmapText(x, y, font, [text], [size]) {#instance-dynamicbitmaptextx-y-font-text-size}


**说明:**

创建新的动态位图文本游戏对象,并添加到场景中。

BitmapText 对象通过取一个纹理文件以及描述字体结构的XML或JSON文件来工作.

在渲染过程中,每个文字字母都会被渲染到显示器,按比例间隔,并配合字体结构.

动态位图文本对象不同于静态位图文本,因为它们为在渲染传递时所给出的每个字母引用回调。这种回调允许您操纵每个正在渲染的字母的属性,如其位置,比例或锡值,允许您创建像拼接文本这样的有趣效果,而拼接文本是无法完成的。这意味着动态文本需要更多的处理时间,所以只有在您需要它们具有的回调能力时才使用它们.

比特玛普Text对象不如Text对象灵活,因为它们具有较少的特性,如阴影、填充和能够使用Web字体,但您可以用这种灵活性来进行渲染速度。您还可以通过在图像编辑器中处理字体纹理、应用填充和所需的任何其他效果来创建视觉上具有说服力的比特玛普Texts。

要创建多行文本,请在文本字符串中插入\r,\n或\rn 逃逸代码.

要创建 BitmapText 数据文件, 您需要 3 个 party app , 例如 :

BMFont(Windows,免费):[http://www.angelcode.com/products/bmfont/](http://www.angelcode.com/products/bmfont/) 格莱夫设计师(OS X,商用):[http://www.71squared.com/en/glyphdesigner](http://www.71squared.com/en/glyphdesigner) Littra(基于网络,免费):[http://kvazars.com/littera/](http://kvazars.com/littera/)

对于大多数使用的案例,建议使用XML。如果您想要使用JSON,格式化应当等于通过流行的X2JS库转换一个有效的XML文件的结果。这里可以找到一个转换的在线工具:[http://codebeautify.org/xmltojson](http://codebeautify.org/xmltojson)

注意:只有在动态位图文字游戏对象已建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 游戏对象的x位置. |
| y | number | 否 | 游戏对象的y位置 。 |
| font | string | 否 | BitmapFont 缓存中要使用的字体的密钥 。 |
| text | string \| Array.\<string> | 是 | 字符串,或字符串的数组,将设置为此位图文本的内容 。 |
| size | number | 是 | 要设置的字体大小 。 |


**返回值:** [Phaser.GameObjects.DynamicBitmapText](/api/class/gameobjects-dynamicbitmaptext) - 创建的游戏对象 。


> 源码：[src/gameobjects/bitmaptext/dynamic/DynamicBitmapTextFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/dynamic/DynamicBitmapTextFactory.js#L10)  
引入版本：3.0.0


---

### ellipse {#ellipse}

#### \<instance> ellipse([x], [y], [width], [height], [fillColor], [fillAlpha]) {#instance-ellipsex-y-width-height-fillcolor-fillalpha}


**说明:**

创建新的椭圆形状游戏对象,并添加到场景中。

注意:只有在椭圆游戏对象已建入Phaser时,此方法才会可用.

椭圆形状是一个游戏对象,可以添加到景物,组或容器中。您可以把它像游戏中其它游戏对象一样对待,比如对它进行扭动,缩放,或者允许它输入或物理。它为您提供了快速和容易的方法,可以在游戏中不使用纹理来渲染此形状,同时仍然利用WebGL进行完整的批量.

此形状既支持填充颜色,也支持中风颜色.

当它显示椭圆形状时, 您可以控制椭圆的宽度和高度。 如果宽度和高度匹配, 则它会变成圆形。 如果宽度小于高度, 它看起来会更像一个卵形 。

椭圆形状还具有`smoothness`属性和相应的`setSmoothness`方法。这允许您通过控制构造过程中发生的迭代数量来控制形状在WebGL中是如何平滑的。 增减更平滑或更划线的形状的默认值。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 椭圆的宽度。 宽度和高度相等的椭圆会变成圆形 。 |
| height | number | 是 | 128 | 椭圆的高度。宽度和高度相等的椭圆会形成圆形。 |
| fillColor | number | 是 |  | 椭圆的颜色会填充,即0xff000为红色. |
| fillAlpha | number | 是 |  | 椭圆的α将被填充。 您也可以使用其 `alpha` 属性设置整个形状的α 。 |


**返回值:** [Phaser.GameObjects.Ellipse](/api/class/gameobjects-ellipse) - 创建的游戏对象 。


> 源码：[src/gameobjects/shape/ellipse/EllipseFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/ellipse/EllipseFactory.js#L10)  
引入版本：3.13.0


---

### existing {#existing}

#### \<instance> existing(child) {#instance-existingchild}


**说明:**

将已有的游戏对象添加到此场景。

如果游戏对象生成, 将添加到显示列表中。 如果它有 `preUpdate` 方法, 它将添加到更新列表中 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| [Phaser.GameObjects.Group](/api/class/gameobjects-group) | [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) | 否 | 今景中所加之子. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 添加的游戏对象 。


> 源码：[src/gameobjects/GameObjectFactory.js#L117](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectFactory.js#L117)  
引入版本：3.0.0


---

### extern {#extern}

#### \<instance> extern() {#instance-extern}


**说明:**

创建新的 Extend Game Object,并添加到Scene 的显示列表中.

extern 是游戏对象的一种特殊类型,它允许您直接将自定义渲染逻辑集成到其中 Phaser正在渲染管道。 通过在显示列表中添加一个 extern , 您可以在您自己的列表中注入 WebGL 或 Canvas 在渲染顺序中的特定点绘制调用, 不 Phaser 干扰渲染器状态。当您需要使用第三方渲染器、执行自定义的 GPU 操作或提供内容时,此操作是有用的。 Phaser 中不支持本地化,同时仍然将它与您场景中的其他游戏对象进行正确的复合。

注意:只有在将Extern游戏对象建为Phaser时,此方法才会可用.


**返回值:** [Phaser.GameObjects.Extern](/api/class/gameobjects-extern) - 已创建并添加到显示列表中的Extern Game Object.


> 源码：[src/gameobjects/extern/ExternFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/extern/ExternFactory.js#L10)  
引入版本：3.16.0


---

### follower {#follower}

#### \<instance> follower(path, x, y, texture, [frame]) {#instance-followerpath-x-y-texture-frame}


**说明:**

创建新的路径跟踪游戏对象,并添加到场景中。

路径跟踪器是一个捆绑在 Phaser.Curves.Path 上的Sprite, 并可以随时间自动沿着该路径移动。 它对于在预定的路线上进行动画角色或对象很有用, 例如敌人在某一关卡上巡逻, 车辆在路上, 或任何需要经过曲线或多分区路径的游戏对象。 后续者会显示启动、 停止、 暂停和恢复移动的控制, 以及沿着路径循环和旋转的选项 。

注:只有在路径跟踪游戏对象已建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| path | [Phaser.Curves.Path](/api/class/curves-path) | 否 | 此路径跟踪器连接到的路径 。 |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此游戏对象将使用用于渲染的纹理的密钥或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |


**返回值:** [Phaser.GameObjects.PathFollower](/api/class/gameobjects-pathfollower) - 创建的游戏对象 。


> 源码：[src/gameobjects/pathfollower/PathFollowerFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/pathfollower/PathFollowerFactory.js#L10)  
引入版本：3.0.0


---

### gradient {#gradient}

#### \<instance> gradient([config], [x], [y], [width], [height]) {#instance-gradientconfig-x-y-width-height}


**说明:**

创建新的渐变游戏对象并添加到场景中.

注意:只有在渐变游戏对象和WebGL支持已经建入Phaser时,才能使用这种方法.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | string \| [Phaser.Types.GameObjects.Gradient.GradientQuadConfig](/api/typedef/types-gameobjects-gradient#gradientquadconfig) | 是 |  | 此渐变将使用的配置对象。 这定义了渐变纹理的形状和外观 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |


**返回值:** [Phaser.GameObjects.Gradient](/api/class/gameobjects-gradient) - 创建的游戏对象 。


> 源码：[src/gameobjects/gradient/GradientFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/gradient/GradientFactory.js#L10)  
引入版本：4.0.0


---

### graphics {#graphics}

#### \<instance> graphics([config]) {#instance-graphicsconfig}


**说明:**

创建新的图形游戏对象,并添加到场景中。

注意:只有在图形游戏对象已建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Graphics.Options](/api/typedef/types-gameobjects-graphics#options) | 是 | 图形配置 。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 创建的游戏对象 。


> 源码：[src/gameobjects/graphics/GraphicsFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/GraphicsFactory.js#L10)  
引入版本：3.0.0


---

### grid {#grid}

#### \<instance> grid([x], [y], [width], [height], [cellWidth], [cellHeight], [fillColor], [fillAlpha], [outlineFillColor], [outlineFillAlpha]) {#instance-gridx-y-width-height-cellwidth-cellheight-fillcolor-fillalpha-outlinefillcolor-outlinefillalpha}


**说明:**

创建新的网格形状游戏对象,并添加到场景中。

注意:只有在网格游戏对象已建入Phaser时,此方法才会可用.

网格形状是一个游戏对象,可以添加到场景、组或容器中。您可以把它像游戏中其它游戏对象一样对待,比如对它进行扭动、缩放或允许输入或物理。它为您提供了快速和容易的方法,在游戏中不使用纹理来渲染此形状,同时仍然利用WebGL的完整批量。

此形状只支持填充颜色, 无法被中键 。

网格形状允许您在游戏中显示网格, 您可以在此控制网格大小以及网格单元格的宽度和高度。 您可以为每个网格单元格设置填充色以及替代填充色。 当设定了替代填充色后, 网格单元格会随其生成时而替换填充色, 从而创建棋盘效果。 您也可以选择使用大纲填充色。 如果设定的话, 则在网格单元格之间绘制线条, 指定带有零的α的轮廓颜色, 则会绘制被分隔的单元格, 但不显示它们之间的线条 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 网格的宽度. |
| height | number | 是 | 128 | 网格的高度. |
| cellWidth | number | 是 | 32 | 网格中一个单元格的宽度 。 |
| cellHeight | number | 是 | 32 | 网格中一个细胞的高度. |
| fillColor | number | 是 |  | 网格单元格的颜色会填充,即0xff000表示红色. |
| fillAlpha | number | 是 |  | 网格单元格将填充α。您也可以使用其`alpha`属性设置整个形状的α 。 |
| outlineFillColor | number | 是 |  | 网格单元格间线条的颜色. |
| outlineFillAlpha | number | 是 |  | 网格细胞之间的线条的α. |


**返回值:** [Phaser.GameObjects.Grid](/api/class/gameobjects-grid) - 创建的游戏对象 。


> 源码：[src/gameobjects/shape/grid/GridFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/grid/GridFactory.js#L10)  
引入版本：3.13.0


---

### group {#group}

#### \<instance> group([children], [config]) {#instance-groupchildren-config}


**说明:**

创建新的 Group 游戏对象并添加到场景中。

A Group 是将游戏对象组合在一起的一种方法, 以便它们能够作为一个单一的单位进行管理。 团体没有自己的位置或视觉表现, 它们纯粹是一个组织工具。 一个常用的集合是对象集合: 预先创建一组固定的游戏对象, 并回收它们, 而不是在运行时创建和销毁它们。 团体也可以同时对所有成员应用批量操作( 如设定能见度或授权物理) 。

注意:只有在组游戏对象已建为Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| children | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> \| [Phaser.Types.GameObjects.Group.GroupConfig](/api/typedef/types-gameobjects-group#groupconfig) | Array.\<[Phaser.Types.GameObjects.Group.GroupConfig](/api/typedef/types-gameobjects-group#groupconfig)> | [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) | 是 | 要添加到此组的游戏对象; 或 `config` 参数 。 |
| config | [Phaser.Types.GameObjects.Group.GroupConfig](/api/typedef/types-gameobjects-group#groupconfig) \| [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) | 是 | 组合配置对象 。 |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 创建的游戏对象 。


> 源码：[src/gameobjects/group/GroupFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/GroupFactory.js#L10)  
引入版本：3.0.0


---

### image {#image}

#### \<instance> image(x, y, texture, [frame]) {#instance-imagex-y-texture-frame}


**说明:**

创建新的图像游戏对象并添加到场景中。

注意:只有当图像游戏对象已经建入Phaser时,此方法才会被使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此游戏对象将使用用于渲染的纹理的密钥或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |


**返回值:** [Phaser.GameObjects.Image](/api/class/gameobjects-image) - 创建的游戏对象 。


> 源码：[src/gameobjects/image/ImageFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/image/ImageFactory.js#L10)  
引入版本：3.0.0


---

### isobox {#isobox}

#### \<instance> isobox([x], [y], [size], [height], [fillTop], [fillLeft], [fillRight]) {#instance-isoboxx-y-size-height-filltop-fillleft-fillright}


**说明:**

创建新的 IsoBox 形状游戏对象,并添加到场景中。

注意:只有当IsoBox游戏对象已经建入Phaser时,此方法才会可用.

IsoBox形状是游戏对象,可以添加到游戏场景,组或容器中。您可以把它像游戏中其它任何游戏对象一样对待,比如对它进行曲折,缩放,或者允许它输入或物理。它为您提供了快速和容易的方法,可以在游戏中不使用纹理来渲染此形状,同时仍然利用WebGL的完整批量.

此形状只支持填充颜色, 无法被中键 。

IsoBox 是“ 同位素” 矩形。 每个面部的填充颜色不同。 您可以分别设置矩形的上方、左方和右方的颜色。 您也可以选择哪个面部通过 `showTop` 、 `showLeft` 和 `showRight` 属性来渲染 。

您不能从下方查看 IsoBox, 但是您可以通过设置 `projection` 属性来更改“ 角 ” 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| size | number | 是 | 48 | 以像素表示的等效框的宽度。 左右面将完全为此值的一半 。 |
| height | number | 是 | 32 | 异位框的高度。 左右面部会如此高。 异位框的整体高度将是这个值加上`size`值的一半 。 |
| fillTop | number | 是 | "0xeeeeee" | 以等效框顶部面部的填充颜色. |
| fillLeft | number | 是 | "0x999999" | 以等效框左面的填充颜色。 |
| fillRight | number | 是 | "0xcccccc" | 以等效框右面的填充颜色. |


**返回值:** [Phaser.GameObjects.IsoBox](/api/class/gameobjects-isobox) - 创建的游戏对象 。


> 源码：[src/gameobjects/shape/isobox/IsoBoxFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isobox/IsoBoxFactory.js#L10)  
引入版本：3.13.0


---

### isotriangle {#isotriangle}

#### \<instance> isotriangle([x], [y], [size], [height], [reversed], [fillTop], [fillLeft], [fillRight]) {#instance-isotrianglex-y-size-height-reversed-filltop-fillleft-fillright}


**说明:**

创建新的 IsoTriangle 形状游戏对象,并将其添加到场景中。

注意:只有在IsoTriangle游戏对象已建入Phaser时,此方法才会可用.

IsoTriangle 形状是游戏对象,可以添加到游戏场景、组或容器中。您可以把它当作游戏中的其他任何游戏对象,比如对它进行曲折、缩放或允许输入或物理。它为您提供了快速和容易的方法,在游戏中不使用纹理来渲染此形状,同时仍然利用WebGL的完整批量。

此形状只支持填充颜色, 无法被中键 。

IsoTriangle 是“ 同位素” 三角形。 把它当金字塔一样看待。 每个面都有一个不同的填充颜色。 您可以分别设置三角形的上方、 左方和右方的颜色 。 您也可以选择哪个面孔是通过 `showTop` 、 `showLeft` 和 `showRight` 属性来渲染的 。

您不能从下面查看 IsoTriangle , 但是您可以通过设置 `projection` 属性来更改“ 角 ” 。 如果 IsoTriangel 是否被倒置, 则 `reversed` 属性控制 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| size | number | 是 | 48 | 以像素表示的等距三角形的宽度。 左右面将完全为此值的一半 。 |
| height | number | 是 | 32 | 以等距三角形的高度。 左右面部会如此高。 以等距三角形的总高度将是这个值加半个`size`值 。 |
| reversed | boolean | 是 | false | 异形三角形是倒着的吗? |
| fillTop | number | 是 | "0xeeeeee" | 以异形三角形顶部面部的填充颜色. |
| fillLeft | number | 是 | "0x999999" | 以等距三角形左面的填充颜色. |
| fillRight | number | 是 | "0xcccccc" | 以等效三角形右面的填充颜色. |


**返回值:** [Phaser.GameObjects.IsoTriangle](/api/class/gameobjects-isotriangle) - 创建的游戏对象 。


> 源码：[src/gameobjects/shape/isotriangle/IsoTriangleFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/isotriangle/IsoTriangleFactory.js#L10)  
引入版本：3.13.0


---

### layer {#layer}

#### \<instance> layer([children]) {#instance-layerchildren}


**说明:**

创建新的图层游戏对象,并添加到场景中。

注意:只有在层游戏对象已建为Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| children | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 是 | 添加到此图层的游戏对象可选数组 。 |


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 创建的游戏对象 。


> 源码：[src/gameobjects/layer/LayerFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/LayerFactory.js#L10)  
引入版本：3.50.0


---

### line {#line}

#### \<instance> line([x], [y], [x1], [y1], [x2], [y2], [strokeColor], [strokeAlpha]) {#instance-linex-y-x1-y1-x2-y2-strokecolor-strokealpha}


**说明:**

创建新的线条形状游戏对象,并添加到场景中。

注意:只有当线性游戏对象已建为Phaser时,此方法才会可用.

Line 形状是游戏对象, 可以添加到游戏场景、 组合或容器中。 您可以把它当作游戏中的其他任何游戏对象, 如进行曲折、 缩放或允许输入或物理。 它为您提供了快速和容易的方法, 可以在游戏中不使用纹理来渲染此形状, 同时仍然利用在 WebGL 中被完全批量处理 。

此形状只支持中风颜色,不能填充 。

线形允许您在游戏中绘制两点之间的线条。 您可以控制线条的中风颜色和厚度。 在 WebGL 中, 您只能指定线条的起始和结尾的厚度, 允许您渲染线条的自启动 。

如果您需要绘制序列中的多行, 您可能希望使用多边形形状代替 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| x1 | number | 是 | 0 | 线起处的横向位置. |
| y1 | number | 是 | 0 | 线条起始的垂直位置. |
| x2 | number | 是 | 128 | 线尾的横向位置. |
| y2 | number | 是 | 0 | 线尾的垂直位置. |
| strokeColor | number | 是 |  | 线条的颜色会被绘制为红色,即0xff000. |
| strokeAlpha | number | 是 |  | 线条的alpha 将被绘制。 您也可以使用它的 `alpha` 属性设置整个形状的alpha 。 |


**返回值:** [Phaser.GameObjects.Line](/api/class/gameobjects-line) - 创建的游戏对象 。


> 源码：[src/gameobjects/shape/line/LineFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/line/LineFactory.js#L10)  
引入版本：3.13.0


---

### nineslice {#nineslice}

#### \<instance> nineslice(x, y, texture, [frame], [width], [height], [leftWidth], [rightWidth], [topHeight], [bottomHeight], [tileX], [tileY]) {#instance-nineslicex-y-texture-frame-width-height-leftwidth-rightwidth-topheight-bottomheight-tilex-tiley}


**说明:**

九切游戏对象允许您显示一个既可以水平伸展又可以垂直伸展的纹理对象,但保留固定大小的角。角的尺寸通过参数设定到此类。

这对UI和元素等按钮极为有用,需要它们扩展以容纳内容而不扭曲纹理.

您为此游戏对象提供的纹理应该基于以下布局结构:

```
     A                          B
   +---+----------------------+---+
 C | 1 |          2           | 3 |
   +---+----------------------+---+
   |   |                      |   |
   | 4 |          5           | 6 |
   |   |                      |   |
   +---+----------------------+---+
 D | 7 |          8           | 9 |
   +---+----------------------+---+
```

当更改对象的宽度和 / 或高度时 :

区域1、3、7和9(角)将保持无标

    areas 2 and 8 will be stretched horizontally only

    areas 4 and 6 will be stretched vertically only

    area 5 will be stretched both horizontally and vertically

您也可以创建3个切片游戏对象 :

这种方法效果类似,但只能水平拉伸。 因此,它需要更少的配置:

```
     A                          B
   +---+----------------------+---+
   |   |                      |   |
 C | 1 |          2           | 3 |
   |   |                      |   |
   +---+----------------------+---+
```

当更改对象的宽度( 您不能更改其高度) 时

区域1和3将保持不变

    area 2 will be stretched horizontally

上述配置概念改编自Pixi NineSlicesPlane.

要指定一个3个切片对象而不是9个切片, 您只应该提供 `leftWidth` 和 `rightWidth` 参数。 要创建 9 个切片, 您必须提供所有参数 。

此游戏对象最小宽度的(_L) 共 `leftWidth` + `rightWidth`中,该游戏对象的高度可以达到 _最小_高度。 `topHeight` + `bottomHeight`。如果需要以较小的尺寸显示此对象,可以将其缩放。

在性能方面,使用3切游戏对象相当于连续有3个Sprites. 使用9切游戏对象相当于连续9个Sprites,这个对象的顶点全部进行批次,可以与显示列表上的其他Sprites和图形共存,而不会引起任何额外的间接费用.

至Phaser 3.60 此游戏对象仅为WebGL.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 这个游戏对象的中心在世界的横向位置. |
| y | number | 否 |  | 这个游戏对象的中心在世界的垂直位置. |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 |  | 此游戏对象将使用用于渲染的纹理的密钥或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 |  | 游戏对象正在用此渲染的纹理的可选框架 。 |
| width | number | 是 | 256 | 九切游戏对象的宽度。 您可以调整创建后的宽度 。 |
| height | number | 是 | 256 | 九切游戏对象的高度。 如果这是 3 切片对象, 高度将固定到纹理高度, 无法更改 。 |
| leftWidth | number | 是 | 10 | 左纵列的大小(A). |
| rightWidth | number | 是 | 10 | 右垂直列的大小(B). |
| topHeight | number | 是 | 0 | 水平线顶端的大小( C) 。 设置为 0 或未定义以创建 3 个切片对象 。 |
| bottomHeight | number | 是 | 0 | 下水平行的大小( D) 。 设置为 0 或未定义以创建 3 个切片对象 。 |
| tileX | boolean | 是 | false | 是否将横向区域铺设为平面,而不是拉伸。 仍会发生一些拉伸, 使平面计数为整数 。 |
| tileY | boolean | 是 | false | 是否将垂直区域铺设为平面, 而不是拉伸。 仍会发生一些拉伸, 以使平面计数为整数 。 |


**返回值:** [Phaser.GameObjects.NineSlice](/api/class/gameobjects-nineslice) - 创建的游戏对象 。


> 源码：[src/gameobjects/nineslice/NineSliceFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSliceFactory.js#L10)  
引入版本：3.60.0


---

### noise {#noise}

#### \<instance> noise([config], [x], [y], [width], [height]) {#instance-noiseconfig-x-y-width-height}


**说明:**

创建新的噪音游戏对象并添加到场景中。

注意:只有在噪声游戏对象和WebGL支持已经建入Phaser时,这种方法才会可用.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | string \| [Phaser.Types.GameObjects.Noise.NoiseQuadConfig](/api/typedef/types-gameobjects-noise#noisequadconfig) | 是 |  | 此噪声将使用的配置对象。 这定义了噪声纹理的形状和外观 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 游戏对象的宽度,以像素为单位. |
| height | number | 是 | 128 | 游戏对象的高度,以像素表示. |


**返回值:** [Phaser.GameObjects.Noise](/api/class/gameobjects-noise) - 创建的游戏对象 。


> 源码：[src/gameobjects/noise/NoiseFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/NoiseFactory.js#L10)  
引入版本：4.0.0


---

### noisecell2d {#noisecell2d}

#### \<instance> noisecell2d([config], [x], [y], [width], [height]) {#instance-noisecell2dconfig-x-y-width-height}


**说明:**

创建新的噪声Cell2D游戏对象,并添加到场景中.

注意:只有在噪声Cell2D游戏对象和WebGL支持已经建入Phaser时,此方法才会可用.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | string \| [Phaser.Types.GameObjects.NoiseCell2D.NoiseCell2DQuadConfig](/api/typedef/types-gameobjects-noisecell2d#noisecell2dquadconfig) | 是 |  | 此噪声Cell2D 将使用的配置对象。 这定义了噪声Cell2D 纹理的形状和外观 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |


**返回值:** [Phaser.GameObjects.NoiseCell2D](/api/class/gameobjects-noisecell2d) - 创建的游戏对象 。


> 源码：[src/gameobjects/noise/noisecell2d/NoiseCell2DFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell2d/NoiseCell2DFactory.js#L10)  
引入版本：4.0.0


---

### noisecell3d {#noisecell3d}

#### \<instance> noisecell3d([config], [x], [y], [width], [height]) {#instance-noisecell3dconfig-x-y-width-height}


**说明:**

创建新的噪声Cell3D游戏对象并添加到场景中.

注意:只有在将噪声Cell3D游戏对象和WebGL支持构建到Phaser中时,此方法才会被使用.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | string \| [Phaser.Types.GameObjects.NoiseCell3D.NoiseCell3DQuadConfig](/api/typedef/types-gameobjects-noisecell3d#noisecell3dquadconfig) | 是 |  | 此噪声Cell3D 将使用的配置对象。 这定义了噪声Cell3D 纹理的形状和外观 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |


**返回值:** [Phaser.GameObjects.NoiseCell3D](/api/class/gameobjects-noisecell3d) - 创建的游戏对象 。


> 源码：[src/gameobjects/noise/noisecell3d/NoiseCell3DFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell3d/NoiseCell3DFactory.js#L10)  
引入版本：4.0.0


---

### noisecell4d {#noisecell4d}

#### \<instance> noisecell4d([config], [x], [y], [width], [height]) {#instance-noisecell4dconfig-x-y-width-height}


**说明:**

创建新的噪声Cell4D游戏对象,并添加到场景中.

注:只有在噪声Cell4D游戏对象和WebGL支持已经建入Phaser时,才能使用这种方法.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | string \| [Phaser.Types.GameObjects.NoiseCell4D.NoiseCell4DQuadConfig](/api/typedef/types-gameobjects-noisecell4d#noisecell4dquadconfig) | 是 |  | 此噪声Cell4D 将使用的配置对象。 这定义了噪声Cell4D 纹理的形状和外观 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |


**返回值:** [Phaser.GameObjects.NoiseCell4D](/api/class/gameobjects-noisecell4d) - 创建的游戏对象 。


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4DFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4DFactory.js#L10)  
引入版本：4.0.0


---

### noisesimplex2d {#noisesimplex2d}

#### \<instance> noisesimplex2d([config], [x], [y], [width], [height]) {#instance-noisesimplex2dconfig-x-y-width-height}


**说明:**

创建新的噪声Simplex2D游戏对象并添加到场景中.

注:只有在噪声Simplex2D游戏对象和WebGL支持已经建入Phaser时,这种方法才会可用.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | string \| [Phaser.Types.GameObjects.NoiseSimplex2D.NoiseSimplex2DQuadConfig](/api/typedef/types-gameobjects-noisesimplex2d#noisesimplex2dquadconfig) | 是 |  | 此噪声Simplex2D 将使用的配置对象。 这定义了噪声Simplex2D 纹理的形状和外观 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |


**返回值:** [Phaser.GameObjects.NoiseSimplex2D](/api/class/gameobjects-noisesimplex2d) - 创建的游戏对象 。


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2DFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2DFactory.js#L10)  
引入版本：4.0.0


---

### noisesimplex3d {#noisesimplex3d}

#### \<instance> noisesimplex3d([config], [x], [y], [width], [height]) {#instance-noisesimplex3dconfig-x-y-width-height}


**说明:**

创建新的噪声Simplex3D游戏对象,并添加到场景中.

注:只有在噪声Simplex3D游戏对象和WebGL支持已经建入Phaser时,此方法才会可用.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | string \| [Phaser.Types.GameObjects.NoiseSimplex3D.NoiseSimplex3DQuadConfig](/api/typedef/types-gameobjects-noisesimplex3d#noisesimplex3dquadconfig) | 是 |  | 此噪声Simplex3D 将使用的配置对象。 这定义了噪声Simplex3D 纹理的形状和外观 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |


**返回值:** [Phaser.GameObjects.NoiseSimplex3D](/api/class/gameobjects-noisesimplex3d) - 创建的游戏对象 。


> 源码：[src/gameobjects/noise/noisesimplex3d/NoiseSimplex3DFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex3d/NoiseSimplex3DFactory.js#L10)  
引入版本：4.0.0


---

### particles {#particles}

#### \<instance> particles([x], [y], [texture], [config]) {#instance-particlesx-y-texture-config}


**说明:**

创建一个新的粒子 Emiter 游戏对象,并添加到场景中。

如果您希望在创建后配置 Emitter,请使用 `ParticleEmitter.setConfig` 方法.

在 Phaser v3.60 之前, 此函数将创建 `ParticleEmitterManager`。 这些功能在 v3. 60 中被删除, 并直接替换为 `ParticleEmitter` 实例。 请参看更新的函数参数和类文档 。

注意:只有在Particles Game Object被建入Phaser时,此方法才会被使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 是 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 此游戏对象在世界的垂直位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 | 此游戏对象将使用用于渲染的纹理的密钥或实例, 如保存在纹理管理器中 。 |
| config | [Phaser.Types.GameObjects.Particles.ParticleEmitterConfig](/api/typedef/types-gameobjects-particles#particleemitterconfig) | 是 | 粒子 Emitter 的配置设置 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 创建的游戏对象 。


> 源码：[src/gameobjects/particles/ParticleEmitterFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitterFactory.js#L10)  
引入版本：3.60.0


---

### path {#path}

#### \<instance> path(x, y) {#instance-pathx-y}


**说明:**

创建新的路径对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 此路径的横向位置 。 |
| y | number | 否 | 此路径的垂直位置 。 |


**返回值:** [Phaser.Curves.Path](/api/class/curves-path) - 创建的路径对象 。


> 源码：[src/curves/path/Path.js#L912](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/Path.js#L912)  
引入版本：3.0.0


---

### pointlight {#pointlight}

#### \<instance> pointlight(x, y, [color], [radius], [intensity], [attenuation]) {#instance-pointlightx-y-color-radius-intensity-attenuation}


**说明:**

创建新的点光游戏对象,并添加到场景中。

注意:只有在点光游戏对象已建入Phaser时,此方法才会被使用.

点光游戏对象提供了一个在你的游戏中添加点光效果的方法,而不需要传统的点光游戏对象的昂贵的遮荫处理要求.

不同之处在于点光会使用自定义的遮阳器,设计来给人以点光源的印象,在游戏中可以变的半径,强度和颜色。然而,与点光游戏对象不同,它不会影响其他任何游戏对象,或者使用普通的地图进行计算。这使得它们与灯光相比,制作速度非常快,并且适合特殊效果,例如闪烁的火炬或口袋闪光。

为了达到最大性能, 您应该将点光游戏对象进行批量。 这意味着它们可以确保显示列表中彼此连续跟踪。 理想的做法是使用一个图层游戏对象, 然后在其中添加点光, 这样它就可以将显示的灯光进行批量。 您没有_ 这样做, 如果您的游戏中只有少数点光, 那么将它们作为正常的显示列表中混合是完全安全的。 但是, 如果您使用了大量的, 请考虑它们是如何被混合到显示列表中的 。

渲染器会自动凸出点光。 半径与相机不相交的会跳过渲染列表。 自动发生这种情况, 并且刷新每个相机的凹陷状态 。

点光的起源总是0.5,不能改变.

点灯是WebGL唯一的特性,没有Canvas对应功能.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 世界上这个点光的横向位置. |
| y | number | 否 |  | 世界上这个点光的垂直位置. |
| color | number | 是 | "0xffffff" | 点光的颜色,作为六进制值给出. |
| radius | number | 是 | 128 | 点光号的半径. |
| intensity | number | 是 | 1 | 点光的强度,或颜色混合. |
| attenuation | number | 是 | 0.1 | 点光的衰减,这是从中心点的光的衰减. |


**返回值:** [Phaser.GameObjects.PointLight](/api/class/gameobjects-pointlight) - 创建的游戏对象 。


> 源码：[src/gameobjects/pointlight/PointLightFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/pointlight/PointLightFactory.js#L10)  
引入版本：3.50.0


---

### polygon {#polygon}

#### \<instance> polygon([x], [y], [points], [fillColor], [fillAlpha]) {#instance-polygonx-y-points-fillcolor-fillalpha}


**说明:**

创建新的多边形形状游戏对象,并添加到场景中。

注:只有在Polygon游戏对象已建为Phaser时,此方法才会被使用.

多边形形状是游戏对象, 可以添加到游戏、 组合或容器中。 您可以把它当作游戏中的其他对象, 如进行曲折、 缩放或允许输入或物理。 它为您提供了快速和简单的方式, 可以在游戏中不使用纹理来渲染此形状, 同时仍然利用在 WebGL 中被完整批量 。

此形状既支持填充颜色,也支持中风颜色.

多边形形状是通过提供点列表创建的,然后用来创建内部的多边形几何对象。这些点可以从多种格式设置:

- 点或矢量2对象阵列: `[new Phaser.Math.Vector2(x1, y1), ...]`

- 具有公共 x/y 属性的天体阵列: `[obj1, obj2, ...]`

- 代表点坐标的对数组: `[x1,y1, x2,y2, ...]`

- 一组阵列,其中两个元素代表x/y坐标:`[[x1, y1], [x2, y2], ...]`

默认情况下,此形状的`x`和`y`坐标是指其中心,但视所提供的点的坐标而定,最终形状可能会被其来源抵消.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| points | any | 是 |  | 构成多边形的点. |
| fillColor | number | 是 |  | 多边形的颜色会填充,即0xff000为红色. |
| fillAlpha | number | 是 |  | 多边形的α将被填充。 您也可以使用它的 `alpha` 属性设置整个形状的α 。 |


**返回值:** [Phaser.GameObjects.Polygon](/api/class/gameobjects-polygon) - 创建的游戏对象 。


> 源码：[src/gameobjects/shape/polygon/PolygonFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/polygon/PolygonFactory.js#L10)  
引入版本：3.13.0


---

### rectangle {#rectangle}

#### \<instance> rectangle([x], [y], [width], [height], [fillColor], [fillAlpha]) {#instance-rectanglex-y-width-height-fillcolor-fillalpha}


**说明:**

创建新的矩形形状游戏对象,并添加到场景中。

注意:只有在矩形游戏对象已经建入Phaser时,此方法才会被使用.

矩形形状是游戏对象,可以添加到景物、组或容器中。您可以把它当作游戏中的其他任何游戏对象,比如对它进行曲折、缩放或允许输入或物理。它为您提供了快速和容易的方法,在游戏中不使用纹理来制作此形状,同时仍然利用WebGL的完整批量。

此形状既支持填充颜色,也支持中风颜色.

通过改变`width`和`height`的属性,可以改变矩形的大小.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 矩形的宽度 。 |
| height | number | 是 | 128 | 长方形的高度. |
| fillColor | number | 是 |  | 矩形的颜色会填充,即0xff000为红色. |
| fillAlpha | number | 是 |  | 矩形的α会被填充。 您也可以使用它的`alpha`属性设置整个形状的α 。 |


**返回值:** [Phaser.GameObjects.Rectangle](/api/class/gameobjects-rectangle) - 创建的游戏对象 。


> 源码：[src/gameobjects/shape/rectangle/RectangleFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/rectangle/RectangleFactory.js#L10)  
引入版本：3.13.0


---

### register {#register}

#### \<static> register(factoryType, factoryFunction) {#static-registerfactorytype-factoryfunction}


**说明:**

在Game ObjectFactory原型上注册一个游戏对象工厂功能,使其通过Scene的添加属性创建游戏对象.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| factoryType | string | 否 | 工厂注册的钥匙,可使用`Phaser.Scene.add[factoryType]`. |
| factoryFunction | function | 否 | 引用 `Phaser.Scene.add[factoryType]` 时要调用工厂功能 。 |


> 源码：[src/gameobjects/GameObjectFactory.js#L186](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectFactory.js#L186)  
引入版本：3.0.0


---

### remove {#remove}

#### \<static> remove(factoryType) {#static-removefactorytype}


**说明:**

从 GameObjectFactory 原型中删除游戏对象工厂的功能.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| factoryType | string | 否 | 您想要从游戏对象数据库中移除的工厂密钥 。 |


> 源码：[src/gameobjects/GameObjectFactory.js#L205](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectFactory.js#L205)  
引入版本：3.0.0


---

### renderTexture {#renderTexture}

#### \<instance> renderTexture(x, y, [width], [height]) {#instance-rendertexturex-y-width-height}


**说明:**

创建新的纹理游戏对象,并添加到场景中。

注意:只有在Render纹理游戏对象已建入Phaser时,此方法才会可用.

成形纹理是动态纹理和图像游戏对象的结合,使用动态纹理来显示自己.

动态纹理是一种特殊的纹理,它允许您直接绘制纹理,帧和大多数类型的游戏对象.

您可以带许多复杂的对象到这个纹理, 然后可以用来作为其他游戏对象, 如Sprites 的基础纹理。 如果您再更新这个纹理, 所有使用它的游戏对象都会立即更新, 立即反映变化 。

这是一种强大的方法,在运行时生成动态纹理,这种纹理是WebGL友好的,并且不会在每个变化上引用昂贵的GPU上传.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 这个游戏对象在世界的横向位置. |
| y | number | 否 |  | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 32 | 宽度的Render纹理。 |
| height | number | 是 | 32 | 风化纹理的高度。 |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 创建的游戏对象 。


> 源码：[src/gameobjects/rendertexture/RenderTextureFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTextureFactory.js#L10)  
引入版本：3.2.0


---

### rope {#rope}

#### \<instance> rope(x, y, texture, [frame], [points], [horizontal], [colors], [alphas]) {#instance-ropex-y-texture-frame-points-horizontal-colors-alphas}


**说明:**

创建新的绳索游戏对象并将其添加到场景中。

注意:只有在将绳形游戏对象和WebGL支持构建为Phaser时,此方法才会被使用.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 这个游戏对象在世界的横向位置. |
| y | number | 否 |  | 此游戏对象在世界的垂直位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 |  | 此游戏对象将使用用于渲染的纹理的密钥或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 |  | 游戏对象正在用此渲染的纹理的可选框架 。 |
| points | Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 是 |  | 包含此绳索的顶点数据的阵列。 如果没有提供, 则创建一个简单的四边形。 请参见 `setPoints` 设置此创建后 。 |
| horizontal | boolean | 是 | true | 这个绳子的顶点应水平对齐(`true`),还是垂直对齐(`false`)? |
| colors | Array.\<number> | 是 |  | 包含此绳索的颜色数据的可选数组。 您应该提供每对顶点一个颜色值 。 |
| alphas | Array.\<number> | 是 |  | 包含此绳索的α数据的可选数组。 您应该提供每对顶点一个α值 。 |


**返回值:** [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) - 创建的游戏对象 。


> 源码：[src/gameobjects/rope/RopeFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/RopeFactory.js#L10)  
引入版本：3.23.0


---

### shader {#shader}

#### \<instance> shader(config, [x], [y], [width], [height], [textures]) {#instance-shaderconfig-x-y-width-height-textures}


**说明:**

创建新的Shader游戏对象,并添加到场景中.

一个Shader Game Object 使自定义的 GLSL 碎片遮蔽器成为矩形的 Game Objects , 允许您在游戏世界中直接显示程序视觉效果, 基因图形, 或处理后式视觉。 遮蔽器运行在 GPU 上, 可以接收自定义的制服以及最多四个纹理通道输入( iChannel0Z 到 iChannel3) , 使其与以 Shadertoy 风格编写的遮蔽器兼容 。

注意:只有在将Shader游戏对象和WebGL支持构建为Phaser时,此方法才会可用.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | string \| [Phaser.Types.GameObjects.Shader.ShaderQuadConfig](/api/typedef/types-gameobjects-shader#shaderquadconfig) | 否 |  | 用于此 Shader 的配置对象。 它也可以是阴影缓存中对应的着色器的密钥, 它将在新配置对象中用作 `fragmentKey` 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |
| textures | Array.\<string> | 是 |  | 可选的纹理键组绑定在 iChannel0... 3 制服上。 纹理管理器中必须已经存在 。 |


**返回值:** [Phaser.GameObjects.Shader](/api/class/gameobjects-shader) - 创建的游戏对象 。


> 源码：[src/gameobjects/shader/ShaderFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/ShaderFactory.js#L10)  
引入版本：3.17.0


---

### sprite {#sprite}

#### \<instance> sprite(x, y, texture, [frame]) {#instance-spritex-y-texture-frame}


**说明:**

创建新的 Sprite 游戏对象并添加到场景中。

注意:只有在Sprite游戏对象已经建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此游戏对象将使用用于渲染的纹理的密钥或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |


**返回值:** [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) - 创建的游戏对象 。


> 源码：[src/gameobjects/sprite/SpriteFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/SpriteFactory.js#L10)  
引入版本：3.0.0


---

### spriteGPULayer {#spriteGPULayer}

#### \<instance> spriteGPULayer(texture, [size]) {#instance-spritegpulayertexture-size}


**说明:**

创建一个新的 SpriteGPULayer 游戏对象,并添加到景点中.

SpriteGPULayer 是高性能的批量渲染器,它绘制了共享同一纹理的图案集,用于一个单一的GPU绘图调用。当您需要制作许多相同的图案时,使用它,其上调用量最小的图案,例如粒子类效果、图列或大量相同对象。

注意:只有在SpriteGPULayer游戏对象已经建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此游戏对象将使用用于渲染的纹理的密钥或实例, 如保存在纹理管理器中 。 |
| size | number | 是 | SpriteGPULayer 的最大成像数量可以单批制成。 默认 1 。 |


**返回值:** [Phaser.GameObjects.SpriteGPULayer](/api/class/gameobjects-spritegpulayer) - 创建的游戏对象 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayerFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayerFactory.js#L10)  
引入版本：4.0.0


---

### stamp {#stamp}

#### \<instance> stamp(x, y, texture, [frame]) {#instance-stampx-y-texture-frame}


**说明:**

创建新的邮票游戏对象并添加到场景中。

注意:只有在将Stamp Game Object建为Phaser时,此方法才会被使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此游戏对象将使用用于渲染的纹理的密钥或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |


**返回值:** [Phaser.GameObjects.Stamp](/api/class/gameobjects-stamp) - 创建的游戏对象 。


> 源码：[src/gameobjects/stamp/StampFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/stamp/StampFactory.js#L10)  
引入版本：4.0.0


---

### star {#star}

#### \<instance> star([x], [y], [points], [innerRadius], [outerRadius], [fillColor], [fillAlpha]) {#instance-starx-y-points-innerradius-outerradius-fillcolor-fillalpha}


**说明:**

创建新的星形游戏对象,并添加到场景中.

注意:只有在星游戏对象已建为Phaser时,此方法才会可用.

星形是游戏对象, 可以添加到场景、 组合或容器中。 您可以把它当作游戏中的其他游戏对象, 如进行曲折、 缩放或允许输入或物理。 它为您提供了快速和容易的方法, 可以在游戏中不使用纹理来渲染此形状, 同时仍然利用在 WebGL 中被完全批量处理 。

此形状既支持填充颜色,也支持中风颜色.

正如名称所暗示的,星形会在游戏中显示一颗恒星。 您可以控制其中的几个方面, 包括构成恒星的点数。 默认值是 5, 如果您将其改为 4, 它会变成 钻石 。 如果您增加它们, 您将得到一个更闪烁的恒星形状 。

您也可以控制内侧和外侧半径, 恒星的每个点是怎样的“ 长 ” 。 修改这些值以创建更有趣的形状 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| points | number | 是 | 5 | 星上积分数. |
| innerRadius | number | 是 | 32 | 恒星的内半径. |
| outerRadius | number | 是 | 64 | 恒星的外半径. |
| fillColor | number | 是 |  | 星会的颜色会充满,即0xff000为红色. |
| fillAlpha | number | 是 |  | 恒星的α将充满。 您也可以使用它的 `alpha` 属性设置整个形状的α 。 |


**返回值:** [Phaser.GameObjects.Star](/api/class/gameobjects-star) - 创建的游戏对象 。


> 源码：[src/gameobjects/shape/star/StarFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/star/StarFactory.js#L10)  
引入版本：3.13.0


---

### text {#text}

#### \<instance> text(x, y, text, [style]) {#instance-textx-y-text-style}


**说明:**

创建新的文本游戏对象,并添加到场景中。

文本对象将一个或多个行的样式文本制作成内部隐藏的Canvas,然后作为纹理上传,并在景区内显示.

文本对象通过创建自己的内部隐藏的 Canvas 来工作, 然后使用标准的 Canvas `fillText`Z API 来制作文本。 然后从这个画布中创建一个纹理, 在渲染传阅时将它交给您的游戏 。

因为它使用 Canvas API 您可以利用所有这些要约的特性, 比如在文本中应用渐变填充, 或者用中键、 阴影等。 您也可以使用外部加载的自定义字体, 如 Google 或 TypeKit Web 字体 。

您只能显示当前已装入且可供浏览器使用的字体: 因此字体必须预先装入. Phaser 并不为您这样做, 因此您需要使用 3 party 字体加载器, 或在您 Phaser 游戏所居住的页面上已有 CSS 中可用的字体 。

移动浏览器中可用的默认字体,请参见 [this](http://www.jordanm.co.uk/tinytype).

性能说明: 每次文本对象的内容发生变化, 即更改显示的文本或文本样式, 它需要重新制作文本画布, 如果在 WebGL 上, 则将新纹理重新加载到 GPU 。 如果经常使用, 或者在游戏中有大量文本对象, 这将是一个昂贵的操作。 如果您遇到性能问题, 您最好使用 Bitmap Text , 因为它从批量中获利, 避免了昂贵的 Canvas API 调用 。

注意:只有在文本游戏对象已建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| text | string \| Array.\<string> | 否 | 此文本对象将显示的文本 。 |
| style | [Phaser.Types.GameObjects.Text.TextStyle](/api/typedef/types-gameobjects-text#textstyle) | 是 | 文本样式配置对象。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 创建的游戏对象 。


> 源码：[src/gameobjects/text/TextFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextFactory.js#L10)  
引入版本：3.0.0


---

### tilemap {#tilemap}

#### \<instance> tilemap([key], [tileWidth], [tileHeight], [width], [height], [data], [insertNull]) {#instance-tilemapkey-tilewidth-tileheight-width-height-data-insertnull}


**说明:**

从给定的密钥或数据创建一个 Tilemap, 或如果没有提供密钥/数据而创建空白的 Tilemap。从 CSV 或 2D 阵列加载时, 您应该指定 tileWidth & tileHeight。从图中解析时, tileWidth, tileHeight,宽度和高度将从地图数据中拉出。对于空地图,您应当指定 tileWidth, tileHeight,宽度和高度。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 是 |  | Phaser缓存中对应已装入的图片数据的密钥. |
| tileWidth | number | 是 | 32 | 以像素表示的瓦片宽度。 以 `null` 表示默认值。 |
| tileHeight | number | 是 | 32 | 像素中的瓦片高度。 通过 `null` 以默认方式离开 。 |
| width | number | 是 | 10 | 以平面图表示的地图宽度。 以 `null` 表示默认值。 |
| height | number | 是 | 10 | 地图的高度用平板块表示。 以 `null` 键通过, 以默认方式离开 。 |
| data | Array.\<Array.\<number>> | 是 |  | 而不是从缓存中加载, 您也可以直接从 2D 的瓦片索引中加载。 不需要数据, 可在 `null` 中通过 。 |
| insertNull | boolean | 是 | false | 控制如何处理地图数据中的空牌, 带有 -1 索引的牌。 如果 `true`, 空位置将获得 `null` 值。 如果 `false` , 空位置将得到一个带有 - 1 索引的牌对象, 如果您有大片人烟稀少的地图, 牌块数据不需要更改, 那么设置这个值到 `true` 将会帮助内存消耗。 但是, 如果您的地图很小, 或者您需要动态更新牌, 那么留下默认值设定 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 


> 源码：[src/tilemaps/TilemapFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapFactory.js#L10)  
引入版本：3.0.0


---

### tileSprite {#tileSprite}

#### \<instance> tileSprite(x, y, width, height, texture, [frame]) {#instance-tilespritex-y-width-height-texture-frame}


**说明:**

创建新的 TileSprite 游戏对象并添加到场景中。

注意:只有在TileSprite游戏对象已建入Phaser时,此方法才会被使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| width | number | 否 | 游戏对象的宽度。 如果为零, 则会使用纹理框架的大小 。 |
| height | number | 否 | 游戏对象的高度。 如果为零, 则会使用纹理框架的大小 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此游戏对象将使用用于渲染的纹理键或实例, 如保存在纹理管理器中。 无法成为动态纹理 。 |
| frame | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |


**返回值:** [Phaser.GameObjects.TileSprite](/api/class/gameobjects-tilesprite) - 创建的游戏对象 。


> 源码：[src/gameobjects/tilesprite/TileSpriteFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSpriteFactory.js#L10)  
引入版本：3.0.0


---

### timeline {#timeline}

#### \<instance> timeline(config) {#instance-timelineconfig}


**说明:**

A Timeline是未来特定时间安排事件发生的一种方式.

你可以把它看作是游戏的事件排序器,允许你在未来特定时间安排回调,事件和其他动作的运行.

一个时间线是一个场景级别系统,意思是您可以任意拥有尽可能多的时间线,每个时间线属于不同的场景,也可以同时运行多个时间线.

如果暂停了场景, 时间线也会暂停。 如果破坏场景, 时间线会自动被销毁。 然而, 您可以直接控制时间线, 拖动、 恢复和停止它 。

通过游戏对象工厂创建时间线实例 :

```js
const timeline = this.add.timeline();
```

时间线总是暂停。 你必须打电话给`play`,以便启动它。

您也可以在创建时在配置对象中通过,或者在其中的数组中通过:

```js
const timeline = this.add.timeline({
    at: 1000,
    run: () => {
        this.add.sprite(400, 300, 'logo');
    }
});

timeline.play();
```

在这个例子中,我们排列了几个不同的事件:

```js
const timeline = this.add.timeline([
    {
        at: 1000,
        run: () => { this.logo = this.add.sprite(400, 300, 'logo'); },
        sound: 'TitleMusic'
    },
    {
        at: 2500,
        tween: {
            targets: this.logo,
            y: 600,
            yoyo: true
        },
        sound: 'Explode'
    },
    {
        at: 8000,
        event: 'HURRY_PLAYER',
        target: this.background,
        set: {
            tint: 0xff0000
        }
    }
]);

timeline.play();
```

时间线也可以用重复方法循环: +  js .
时间线. repeat (. play (); ;
```

There are lots of options available to you via the configuration object. See the [Phaser.Types.Time.TimelineEventConfig](../typedef/Phaser.Types.Time.md#TimelineEventConfig) typedef for more details.

**Parameters:**
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Time.TimelineEventConfig](../typedef/Phaser.Types.Time.md#TimelineEventConfig) \| Array.\<[Phaser.Types.Time.TimelineEventConfig](../typedef/Phaser.Types.Time.md#TimelineEventConfig)> | No | The configuration object for this Timeline Event, or an array of them. |


**Returns:** [Phaser.Time.Timeline](../class/Phaser.Time.Timeline.md) - The Timeline that was created.


> Source: [src/time/Timeline.js#L808](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/Timeline.js#L808)  
Since: 3.60.0


---

### triangle

#### \<instance> triangle([x], [y], [x1], [y1], [x2], [y2], [x3], [y3], [fillColor], [fillAlpha])


**Description:**

Creates a new Triangle Shape Game Object and adds it to the Scene.

Note: This method will only be available if the Triangle Game Object has been built into Phaser.

The Triangle Shape is a Game Object that can be added to a Scene, Group or Container. You can treat it like any other Game Object in your game, such as tweening it, scaling it, or enabling it for input or physics. It provides a quick and easy way for you to render this shape in your game without using a texture, while still taking advantage of being fully batched in WebGL.

This shape supports both fill and stroke colors.

The Triangle consists of 3 lines, joining up to form a triangular shape. You can control the position of each point of these lines. The triangle is always closed and cannot have an open face. If you require that, consider using a Polygon instead.

**Parameters:**
| name | type | optional | default | description |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | Yes | 0 | The horizontal position of this Game Object in the world. |
| y | number | Yes | 0 | The vertical position of this Game Object in the world. |
| x1 | number | Yes | 0 | The horizontal position of the first point in the triangle. |
| y1 | number | Yes | 128 | The vertical position of the first point in the triangle. |
| x2 | number | Yes | 64 | The horizontal position of the second point in the triangle. |
| y2 | number | Yes | 0 | The vertical position of the second point in the triangle. |
| x3 | number | Yes | 128 | The horizontal position of the third point in the triangle. |
| y3 | number | Yes | 128 | The vertical position of the third point in the triangle. |
| fillColor | number | Yes |  | The color the triangle will be filled with, i.e. 0xff0000 for red. |
| fillAlpha | number | Yes |  | The alpha the triangle will be filled with. You can also set the alpha of the overall Shape using its `alpha` property. |


**Returns:** [Phaser.GameObjects.Triangle](../class/Phaser.GameObjects.Triangle.md) - The Game Object that was created.


> Source: [src/gameobjects/shape/triangle/TriangleFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shape/triangle/TriangleFactory.js#L10)  
Since: 3.13.0


---

### tween

#### \<instance> tween(config)


**Description:**

Creates a new Tween object.

Note: This method will only be available if Tweens have been built into Phaser.

**Parameters:**
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Tweens.TweenBuilderConfig](../typedef/Phaser.Types.Tweens.md#TweenBuilderConfig) \| [Phaser.Types.Tweens.TweenChainBuilderConfig](../typedef/Phaser.Types.Tweens.md#TweenChainBuilderConfig) | [Phaser.Tweens.Tween](../class/Phaser.Tweens.Tween.md) | [Phaser.Tweens.TweenChain](../class/Phaser.Tweens.TweenChain.md) | No | A Tween Configuration object, or a Tween or TweenChain instance. |


**Returns:** [Phaser.Tweens.Tween](../class/Phaser.Tweens.Tween.md) - The Tween that was created.


> Source: [src/tweens/tween/Tween.js#L833](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L833)  
Since: 3.0.0


---

### tweenchain

#### \<instance> tweenchain(config)


**Description:**

Creates a new TweenChain object and adds it to the Tween Manager.

Note: This method will only be available if Tweens have been built into Phaser.

**Parameters:**
| name | type | optional | description |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Tweens.TweenBuilderConfig](../typedef/Phaser.Types.Tweens.md#TweenBuilderConfig) \| object | No | The TweenChain configuration. |


**Returns:** [Phaser.Tweens.TweenChain](../class/Phaser.Tweens.TweenChain.md) - The TweenChain that was created.


> Source: [src/tweens/tween/TweenChain.js#L549](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L549)  
Since: 3.60.0


---

### video

#### \<instance> video(x, y, [key])


**Description:**

Creates a new Video Game Object and adds it to the Scene.

This Game Object is capable of handling playback of a video file, video stream or media stream.

You can optionally 'preload' the video into the Phaser Video Cache:

```javascript
preload () {
  this.load.video('ripley', 'assets/aliens.mp4');
}

create () {
  this.add.video(400, 300, 'ripley');
}
```

您不必“ 预装” 视频。 您也可以直接从 URL 播放 :

```javascript
create () {
  this.add.video(400, 300).loadURL('assets/aliens.mp4');
}
```

在所有意图和目的上,视频都是标准的游戏对象,就像Sprite一样。因此,你可以做所有通常的事情,比如缩放、旋转、裁剪、涂料、制作互动、赋予物理体等等。

透明视频也可以通过WebM文件格式进行. 提供视频文件已经用α通道编码,并提供浏览器支持WebM的播放(并非全部如此),然后它会以完全透明的方式渲染游戏中.

### Autoplaying Videos {#autoplaying-videos}

视频只能自动播放, 如果浏览器已经解锁了交互, 或者满足了 MEI 设置。 控制自动播放的政策是巨大的, 并且不同浏览器不同。 您可以, 并且应该在这里读更多关于它的信息 : [https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide](https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide)

如果您的视频没有包含任何音频,那么当视频被_load_时,将`noAudio`参数设置为`true`,并且它会经常允许视频立即播放:

```javascript
preload () {
  this.load.video('pixar', 'nemo.mp4', true);
}
```

负载调用中的第3个参数告诉 Phaser 视频中没有任何音频音轨. 视频没有音频就可以自动播放,不需要用户交互. 带音频的视频不能做到这一点,除非它满足浏览器的MEI设置. 详见 MDN 自动播放指南.

Or:

```javascript
create () {
  this.add.video(400, 300).loadURL('assets/aliens.mp4', true);
}
```

您可以将 `noAudio` 参数设置为 `true` , 即使视频中包含音频。 它仍然允许视频立即播放, 但音频不会启动 。

关于视频回放和所支持的媒体格式的更多细节,请查看MDN:

[https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement) [https://developer.mozilla.org/en-US/docs/Web/Media/Formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats)

注意:只有在游戏对象已建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| key | string | 是 | 游戏对象将播放的视频的可选密钥, 如存储在视频缓存中 。 |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 创建的游戏对象 。


> 源码：[src/gameobjects/video/VideoFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/VideoFactory.js#L10)  
引入版本：3.20.0


---

### zone {#zone}

#### \<instance> zone(x, y, width, height) {#instance-zonex-y-width-height}


**说明:**

创建新的区域游戏对象并添加到场景中。

注意: 只有在 Zone 游戏对象已建入时, 才能使用此方法 Phaser.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| width | number | 否 | 游戏对象的宽度 。 |
| height | number | 否 | 游戏对象的高度 。 |


**返回值:** [Phaser.GameObjects.Zone](/api/class/gameobjects-zone) - 创建的游戏对象 。


> 源码：[src/gameobjects/zone/ZoneFactory.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/zone/ZoneFactory.js#L10)  
引入版本：3.0.0


---

## 公开成员 {#public-members}

### displayList {#displayList}

#### displayList: [Phaser.GameObjects.DisplayList](/api/class/gameobjects-displaylist) {#displaylist-phasergameobjectsdisplaylist}


**说明:**

用于引用场景显示列表的参考 。


**Access:** 保护


> 源码：[src/gameobjects/GameObjectFactory.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectFactory.js#L63)  
引入版本：3.0.0


---

### events {#events}

#### events: [Phaser.Events.EventEmitter](/api/class/events-eventemitter) {#events-phasereventseventemitter}


**说明:**

参考景点事件 Emitter.


**Access:** 保护


> 源码：[src/gameobjects/GameObjectFactory.js#L53](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectFactory.js#L53)  
引入版本：3.50.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

此游戏对象工厂所属景区 。


**Access:** 保护


> 源码：[src/gameobjects/GameObjectFactory.js#L33](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectFactory.js#L33)  
引入版本：3.0.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

参考神话. 连载.


**Access:** 保护


> 源码：[src/gameobjects/GameObjectFactory.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectFactory.js#L43)  
引入版本：3.0.0


---

### updateList {#updateList}

#### updateList: [Phaser.GameObjects.UpdateList](/api/class/gameobjects-updatelist) {#updatelist-phasergameobjectsupdatelist}


**说明:**

参考景区更新列表.


**Access:** 保护


> 源码：[src/gameobjects/GameObjectFactory.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectFactory.js#L73)  
引入版本：3.0.0


---

---
