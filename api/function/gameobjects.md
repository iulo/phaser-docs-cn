# Phaser.GameObjects.GameObjectFactory {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/function/gameobjects)

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


### remove {#remove}

#### \<static> remove(factoryType) {#static-removefactorytype}


**说明:**

从 GameObjectFactory 原型中删除游戏对象工厂的功能.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| factoryType | string | 否 | 您想要从游戏对象数据库中移除的工厂键 。 |


> 源码：[src/gameobjects/GameObjectFactory.js#L205](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectFactory.js#L205)  
引入版本：3.0.0


# Phaser.GameObjects.GameObjectCreator {#page-title-1}

### register {#register-1}

#### \<static> register(factoryType, factoryFunction) {#static-registerfactorytype-factoryfunction-1}


**说明:**

在Game ObjectCreator原型上注册一个游戏对象创建者功能,使其通过Scene的制作属性来创建游戏对象.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| factoryType | string | 否 | 工厂的钥匙,你用来叫Phaser.Scene.make[factoryType]方法。 |
| factoryFunction | function | 否 | 使用 Phaser.Scene.make 方法时要调用的构造器函数 。 |


> 源码：[src/gameobjects/GameObjectCreator.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectCreator.js#L154)  
引入版本：3.0.0


### remove {#remove-1}

#### \<static> remove(factoryType) {#static-removefactorytype-1}


**说明:**

从游戏对象创建者原型中删除一个先前注册的游戏对象创建者,使其不再通过Scene的制作属性提供.

通过这种方法,您可以删除一个自定义的游戏对象创建器, 之前在游戏对象创建器中注册过。 以 `factoryType` 的方式通过它以删除它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| factoryType | string | 否 | 您想要从游戏对象创建器中移除的工厂键 。 |


> 源码：[src/gameobjects/GameObjectCreator.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectCreator.js#L173)  
引入版本：3.0.0


# Phaser.GameObjects.RetroFont {#page-title-2}

### Parse {#Parse}

#### \<static> Parse(scene, config) {#static-parsescene-config}


**说明:**

分析一个 Retro 字体配置对象,并构建一个 `BitmapFontData` 结构,可以传递到 BitmapText 构造器,以使用固定的宽度 retro 字体渲染文本.

复古字体是一个包含一个统一的字符网格的纹理,每个单元格的宽度和高度都是一样的。这个函数读取配置,查看源纹理帧,然后在`config.chars`定义的每个字符上进行重排,计算其像素位置和纹理内正常的紫外线坐标。生成的数据对象将每个字符代码映射到自己的格律条目,并适合在Bitmap字体缓存中注册。

如果 `config.chars` 是空字符串,则函数返回 `undefined` 而不产生任何数据 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 参考Phaser场景. |
| config | [Phaser.Types.GameObjects.BitmapText.RetroFontConfig](/api/typedef/types-gameobjects-bitmaptext#retrofontconfig) | 否 | 字体配置对象 。 |


**返回值:** [Phaser.Types.GameObjects.BitmapText.BitmapFontData](/api/typedef/types-gameobjects-bitmaptext#bitmapfontdata) - 解析的位图字体数据条目,包含每个字符的格言数据和紫外坐标,准备用于位图字体缓存.


> 源码：[src/gameobjects/bitmaptext/ParseRetroFont.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/ParseRetroFont.js#L9)  
引入版本：3.0.0


# Phaser.GameObjects.BitmapText {#page-title-3}

### ParseFromAtlas {#ParseFromAtlas}

#### \<static> ParseFromAtlas(scene, fontName, textureKey, frameKey, xmlKey, [xSpacing], [ySpacing]) {#static-parsefromatlasscene-fontname-texturekey-framekey-xmlkey-xspacing-yspacing}


**说明:**

从一个 Atlas 中分析一个 XML 位图字体 。

将解析的位图字体数据添加到缓存中,并配有 `fontName` 键。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 解析位图字体的场景 。 |
| fontName | string | 否 | 添加到位图字体缓存的字体键 。 |
| textureKey | string | 否 | 比特玛普方块纹理的键. |
| frameKey | string | 否 | 比特玛普方格纹理帧的键. |
| xmlKey | string | 否 | 字体的 XML 数据解析的键 。 |
| xSpacing | number | 是 | 每个字母之间要添加的x轴间隔。 |
| ySpacing | number | 是 | 线高的Y轴间隔。 |


**返回值:** boolean - 解析是否成功 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1253](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1253)  
引入版本：3.0.0


### ParseXMLBitmapFont {#ParseXMLBitmapFont}

#### \<static> ParseXMLBitmapFont(xml, frame, [xSpacing], [ySpacing]) {#static-parsexmlbitmapfontxml-frame-xspacing-yspacing}


**说明:**

为位图字体缓存分析一个 XML 字体到位图字体数据 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| xml | XMLDocument | 否 |  | XML 文档从中解析字体 。 |
| frame | [Phaser.Textures.Frame](/api/class/textures-frame) | 否 |  | 创建 uv 数据时要考虑的纹理帧 。 |
| xSpacing | number | 是 | 0 | 每个字母之间要添加的x轴间隔。 |
| ySpacing | number | 是 | 0 | 线高的Y轴间隔。 |


**返回值:** [Phaser.Types.GameObjects.BitmapText.BitmapFontData](/api/typedef/types-gameobjects-bitmaptext#bitmapfontdata) - 解析的位图字体数据 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapText.js#L1273](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapText.js#L1273)  
引入版本：3.17.0


### BuildGameObject {#BuildGameObject}

#### \<static> BuildGameObject(scene, gameObject, config) {#static-buildgameobjectscene-gameobject-config}


**说明:**

使用提供的配置对象构建游戏对象, 应用诸如位置、 深度、 翻转、 尺度、 滚动因子、 旋转、 α、 来源、 混合模式、 和可见度等属性。 如果配置的 `add` 属性是 `true`( 默认) , 游戏对象会被添加到 Scene 显示列表中。 如果游戏对象有 `preUpdate` 方法, 也会被添加到 Scene的更新列表中。 此功能由 Game Object 工厂和创建者内部使用, 一般不直接使用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 参考景区. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 初游戏对象. |
| config | [Phaser.Types.GameObjects.GameObjectConfig](/api/typedef/types-gameobjects#gameobjectconfig) | 否 | 用于构建游戏对象的配置 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已建游戏对象.


> 源码：[src/gameobjects/BuildGameObject.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/BuildGameObject.js#L10)  
引入版本：3.0.0


### BuildGameObjectAnimation {#BuildGameObjectAnimation}

#### \<static> BuildGameObjectAnimation(sprite, config) {#static-buildgameobjectanimationsprite-config}


**说明:**

从游戏对象配置对象读取 `anims` 属性,并使用它来配置给定的Sprite 的动画状态。如果 `anims` 属性不存在,则Sprite 返回时不变 。

电话 `anims` 值可以是字符串或对象。如果是字符串,则它被当作动画键,动画立即播放。如果是对象,则动画键和回放选项(例如: `delay`, `repeat`, `yoyo`,和 `startFrame`)从中读取。 `play` 财务报告和已审计财务报表 `delayedPlay` 属性,动画会立即播放,在延迟后播放,或者只是装入准备稍后播放。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sprite | [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) | 否 | 将配置动画状态的 Sprite 。 |
| config | object | 否 | 游戏对象配置对象。 此对象的 `anims` 属性用于配置动画 。 |


**返回值:** [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) - 更新的Sprite( 斯普拉蒂 ).


> 源码：[src/gameobjects/BuildGameObjectAnimation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/BuildGameObjectAnimation.js#L9)  
引入版本：3.0.0


### GetCalcMatrix {#GetCalcMatrix}

#### \<static> GetCalcMatrix(src, camera, [parentMatrix], [ignoreCameraPosition]) {#static-getcalcmatrixsrc-camera-parentmatrix-ignorecameraposition}


**说明:**

计算给定的游戏对象和摄像机的变换矩阵,如果提供的话,在母矩阵中计算。

注意此结果包含 _References_ to the Transform Matrices,而不是新实例。因此,您应该立即使用它们的值,或者将其复制到自己的矩阵中,因为一旦推出另一个游戏对象,它们就会被替换 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| src | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 计算变换矩阵的游戏对象 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 用于渲染游戏对象的摄像机 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 |  | 父容器的变换矩阵,如果有的话。 |
| ignoreCameraPosition | boolean | 是 | false | 摄像机的翻译是否应当忽略? 这就是在屏幕上移动摄像机的原因, 但是当摄像机被传送到帧缓冲器时, 却应该忽略它 。 |


**返回值:** [Phaser.Types.GameObjects.GetCalcMatrixResults](/api/typedef/types-gameobjects#getcalcmatrixresults) - 包含更新的变换矩阵的结果对象.


> 源码：[src/gameobjects/GetCalcMatrix.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GetCalcMatrix.js#L21)  
引入版本：3.50.0


### GetTextSize {#GetTextSize}

#### \<static> GetTextSize(text, size, lines) {#static-gettextsizetext-size-lines}


**说明:**

计算并返回文本对象的已渲染尺寸,包括每行宽度、最大线宽度、总高度(计算行距)和绘图线数(尊重`maxLines`)。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| text | [Phaser.GameObjects.Text](/api/class/gameobjects-text) | 否 | 计算大小的文本对象。 |
| size | [Phaser.Types.GameObjects.Text.TextMetrics](/api/typedef/types-gameobjects-text#textmetrics) | 否 | 计算大小时使用的文本度量。 |
| lines | Array.\<string> | 否 | 用来计算大小的文字线条。 |


**返回值:** [Phaser.Types.GameObjects.Text.GetTextSizeObject](/api/typedef/types-gameobjects-text#gettextsizeobject) - 包含文本对象尺寸的天体。


> 源码：[src/gameobjects/text/GetTextSize.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/GetTextSize.js#L7)  
引入版本：3.0.0


### MeasureText {#MeasureText}

#### \<static> MeasureText(textStyle) {#static-measuretexttextstyle}


**说明:**

通过将文本渲染到一个临时的屏幕外布上并测量像素边界来计算给定的文本Style的升空、降空和fontSize的度量。它使用`actualBoundingBoxAscent`/`actualBoundingBoxDescent` API(如果有的话),回到旧浏览器的像素扫描方法。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| textStyle | [Phaser.GameObjects.TextStyle](/api/class/gameobjects-textstyle) | 否 | 文本样式对象可以测量 。 |


**返回值:** [Phaser.Types.GameObjects.Text.TextMetrics](/api/typedef/types-gameobjects-text#textmetrics) - 包含文本样式的升降、降降和fontSize的天体。


> 源码：[src/gameobjects/text/MeasureText.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/MeasureText.js#L9)  
引入版本：3.0.0


# Phaser.GameObjects.Components {#page-title-4}

### ToJSON {#ToJSON}

#### \<static> ToJSON(gameObject) {#static-tojsongameobject}


**说明:**

构建给定游戏对象的 JSON 代表 。

这通常通过Game Object特定执行来进一步扩展.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 要导出为 JSON 的游戏对象 。 |


**返回值:** [Phaser.Types.GameObjects.JSONGameObject](/api/typedef/types-gameobjects#jsongameobject) - 游戏对象的JSON代表.


> 源码：[src/gameobjects/components/ToJSON.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ToJSON.js#L7)  
引入版本：3.0.0

---
