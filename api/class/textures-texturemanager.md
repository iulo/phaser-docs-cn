# TextureManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/textures-texturemanager)

当Phaser靴子时,它会创建一个纹理管理器类的实例.

它是处理游戏中所有纹理的全局管理器。 您可以通过 `this.textures` 属性从场景内部访问它 。

它的作用是管理您游戏使用的所有纹理。 它可以在全球创建、 更新和删除纹理, 以及从外部文件中解析纹理数据, 如图示工作表和纹理图集 。

螺旋和其他基于纹理的游戏对象直接从这一类获得其纹理数据.

**构造函数**

`new TextureManager(game)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 这个纹理管理器属于Phaser.Game的例子. |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/textures/TextureManager.js#L33](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L33)  
引入版本：3.0.0

## 公开成员 {#public-members}

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

纹理管理器所属的游戏.

游戏中只有一次有纹理管理器.


> 源码：[src/textures/TextureManager.js#L64](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L64)  
引入版本：3.0.0


---

### list {#list}

#### list: object {#list-object}


**说明:**

此对象包含属于此纹理管理器的所有纹理 。

纹理由字符串键识别,这些键被用作此对象内部的属性。因此,您可以直接从此对象获取任何纹理,而无需重复。

您通常不应该直接修改此对象,而是使用纹理管理器提供的方法来添加和删除其中的条目.


> 源码：[src/textures/TextureManager.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L85)  
引入版本：3.0.0


---

### name {#name}

#### name: string {#name-string}


**说明:**

此经理内名.


> 源码：[src/textures/TextureManager.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L75)  
引入版本：3.0.0


---

### silentWarnings {#silentWarnings}

#### silentWarnings: boolean {#silentwarnings-boolean}


**说明:**

如果这个旗子是 `true`, 那么纹理管理器永远不会向报告缺失纹理的控制台日志发出任何警告 。


> 源码：[src/textures/TextureManager.js#L174](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L174)  
引入版本：3.60.0


---

### stamp {#stamp}

#### stamp: [Phaser.GameObjects.Stamp](/api/class/gameobjects-stamp) {#stamp-phasergameobjectsstamp}


**说明:**

属于此纹理管理器的图像游戏对象 。

用作动态纹理内部的绘图邮票.

这不是显示列表的一部分,也不渲染。

在v4.0.0之前,这是`Phaser.GameObjects.Image`型.


> 源码：[src/textures/TextureManager.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L135)  
引入版本：3.60.0


---

### stampCrop {#stampCrop}

#### stampCrop: [Phaser.Geom.Rectangle](/api/class/geom-rectangle) {#stampcrop-phasergeomrectangle}


**说明:**

庄稼矩形(英语:crop 矩形),是邮票在需要自己收割时使用的.


> 源码：[src/textures/TextureManager.js#L151](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L151)  
引入版本：3.60.0


---

### tileSprite {#tileSprite}

#### tileSprite: [Phaser.GameObjects.TileSprite](/api/class/gameobjects-tilesprite) {#tilesprite-phasergameobjectstilesprite}


**说明:**

属于此纹理管理器的 TileSprite 游戏对象 。

用于在动态纹理内重复绘图 。

这不是显示列表的一部分,也不渲染。


> 源码：[src/textures/TextureManager.js#L160](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L160)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Events.EventEmitter](/api/class/events-eventemitter):**


 - [addListener](/api/class/events-eventemitter#addListener)
 - [emit](/api/class/events-eventemitter#emit)
 - [eventNames](/api/class/events-eventemitter#eventNames)
 - [listenerCount](/api/class/events-eventemitter#listenerCount)
 - [listeners](/api/class/events-eventemitter#listeners)
 - [off](/api/class/events-eventemitter#off)
 - [on](/api/class/events-eventemitter#on)
 - [once](/api/class/events-eventemitter#once)
 - [removeAllListeners](/api/class/events-eventemitter#removeAllListeners)
 - [removeListener](/api/class/events-eventemitter#removeListener)
 - [shutdown](/api/class/events-eventemitter#shutdown)




---

## 公开方法 {#public-methods}

### addAtlas {#addAtlas}

#### \<instance> addAtlas(key, source, data, [dataSource]) {#instance-addatlaskey-source-data-datasource}


**说明:**

向此纹理管理器添加一个纹理图集。

在Phaser术语中,一个纹理图集是图集图像和描述其内帧的数据文件的组合,如纹理包机等应用程序输出的框.

这种方法接受三种不同的地图集数据格式:

- **JSON Array** ——`frames`或`textures`字段是阵列。

  "JSON阵列"和"Phaser(多图集)"出口,发送至`addAtlasJSONArray`.

- **JSON Hash** ——`frames`字段是对象,用于Texture Packer的"JSON Hash"导出.

  被派往`addAtlasJSONHash`。

- **Phaser Compact Texture (PCT)** ——一个带有`pages`阵列的解码的PCT数据对象。这是

  由 `LoaderPlugin#atlasPCT` 装入的紧凑线形格式。已发送到 `addAtlasPCT` 。

格式从 `data` 参数的形状自动检测。截至 Phaser 3.60 您可以使用这种方法在现有的 Phaser 纹理中添加地图集 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| source | HTMLImageElement \| Array.\<HTMLImageElement> | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 源图像元素/s,或 Phaser 纹理. |
| data | object \| Array.\<object> | 否 | 纹理图集数据/s. |
| dataSource | HTMLImageElement \| HTMLCanvasElement | Array.\<HTMLImageElement> | Array.\<HTMLCanvasElement> | 是 | 一种可选的数据图像元素. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建的纹理, 或如果密钥已经使用的话, 则使用 `null` 。


> 源码：[src/textures/TextureManager.js#L763](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L763)  
引入版本：3.0.0


---

### addAtlasJSONArray {#addAtlasJSONArray}

#### \<instance> addAtlasJSONArray(key, source, data, [dataSource]) {#instance-addatlasjsonarraykey-source-data-datasource}


**说明:**

向此纹理管理器添加一个纹理图集。

在Phaser术语中,一个纹理图集是图集图像和JSON数据文件的组合,如Texture Packer等应用程序输出的数据文件.

地图集的框架数据必须存储在JSON内部的阵列中.

这在Texture Packer等软件中被称为JSON阵列.

至Phaser 3.60,您可以使用这种方法在现有的Phaser纹理中添加地图集数据集.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| source | HTMLImageElement \| Array.\<HTMLImageElement> | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 源图像元素/s,或 Phaser 纹理. |
| data | object \| Array.\<object> | 否 | 纹理图集数据/s. |
| dataSource | HTMLImageElement \| HTMLCanvasElement | Array.\<HTMLImageElement> | Array.\<HTMLCanvasElement> | 是 | 一种可选的数据图像元素. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建的纹理, 或如果密钥已经使用的话, 则使用 `null` 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L810](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L810)  
引入版本：3.0.0


---

### addAtlasJSONHash {#addAtlasJSONHash}

#### \<instance> addAtlasJSONHash(key, source, data, [dataSource]) {#instance-addatlasjsonhashkey-source-data-datasource}


**说明:**

向此纹理管理器添加一个纹理图集。

在Phaser术语中,一个纹理图集是图集图像和JSON数据文件的组合,如Texture Packer等应用程序输出的数据文件.

地图集的帧数据必须存储在JSON内部的物体中.

在Texture Packer等软件中,这被称为JSON Hash.

至Phaser 3.60,您可以使用这种方法在现有的Phaser纹理中添加地图集数据集.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| source | HTMLImageElement \| Array.\<HTMLImageElement> | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 源图像元素/s,或 Phaser 纹理. |
| data | object \| Array.\<object> | 否 | 纹理图集数据/s. |
| dataSource | HTMLImageElement \| HTMLCanvasElement | Array.\<HTMLImageElement> | Array.\<HTMLCanvasElement> | 是 | 一种可选的数据图像元素. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建的纹理, 或如果密钥已经使用的话, 则使用 `null` 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L879](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L879)  
引入版本：3.0.0


---

### addAtlasPCT {#addAtlasPCT}

#### \<instance> addAtlasPCT(key, source, data, [dataSource]) {#instance-addatlaspctkey-source-data-datasource}


**说明:**

在此纹理管理器中添加一个 Phaser 压缩纹理图集( PCT) 。

PCT 是一个紧凑的面向行的地图集格式。一个单一的PCT文件可以描述多个地图集的页面,每个文件都引用一个单独的纹理图像。 `data` 参数必须是由 3 生成的解码的PCT 结构 `Phaser.Textures.Parsers.PCTDecode` ——即含有 `pages`, `folders`,和 `frames` 字段中。 `source` 参数应该是一个图像或图像矩阵,每页一个,顺序与 `pages` 字段,则在解码数据上。

您通常不需要直接调用这种方法。 `LoaderPlugin#atlasPCT`方法完成装入PCT 文件时会自动调用。 您也可以使用这种方法在已有的 Phaser 纹理中添加一个解码的 PCT 数据集 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| source | HTMLImageElement \| Array.\<HTMLImageElement> | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 源图像元素——每PCT页一个,或现有的Phaser纹理. |
| data | object | 否 | 解码的PCT数据对象. |
| dataSource | HTMLImageElement \| HTMLCanvasElement | Array.\<HTMLImageElement> | Array.\<HTMLCanvasElement> | 是 | 一种可选数据图像元素(正常的地图源). |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建的纹理, 或如果密钥已经使用的话, 则使用 `null` 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L942](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L942)  
引入版本：4.0.0


---

### addAtlasXML {#addAtlasXML}

#### \<instance> addAtlasXML(key, source, data, [dataSource]) {#instance-addatlasxmlkey-source-data-datasource}


**说明:**

向此纹理管理器添加一个纹理图集。

在Phaser术语中,一个纹理图集是图集图像和数据文件的组合,如由Texture Packer等应用程序输出的图集.

地图集的帧数据必须存储在XML文件中.

至Phaser 3.60,您可以使用这种方法在现有的Phaser纹理中添加地图集数据集.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| source | HTMLImageElement \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 源图像元素,或Phaser纹理. |
| data | object | 否 | 纹理图集 XML 数据. |
| dataSource | HTMLImageElement \| HTMLCanvasElement | Array.\<HTMLImageElement> | Array.\<HTMLCanvasElement> | 是 | 一种可选的数据图像元素. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建的纹理, 或如果密钥已经使用的话, 则使用 `null` 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L996](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L996)  
引入版本：3.7.0


---

### addBase64 {#addBase64}

#### \<instance> addBase64(key, data) {#instance-addbase64key-data}


**说明:**

向从给定的 Base64 编码数据创建的纹理管理器添加新的纹理 。

它通过创建 `Image` DOM 对象来工作,然后将 `src` 属性设置到给定的基数64 编码数据中。因此,这一过程就其性质而言是同步的,所以在使用纹理之前一定要先听这个方法发送的事件.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| data | * | 否 | Base64编码了数据. |


**返回值:** [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) - 这个纹理管理器实例 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add), [Phaser.Textures.Events#event:ERROR](/api/event/textures-events#error), [Phaser.Textures.Events#event:LOAD](/api/event/textures-events#load)


> 源码：[src/textures/TextureManager.js#L352](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L352)  
引入版本：3.0.0


---

### addCanvas {#addCanvas}

#### \<instance> addCanvas(key, source, [skipCache]) {#instance-addcanvaskey-source-skipcache}


**说明:**

从已有的 Canvas 元素创建新的 Canvas 纹理对象, 并添加到此纹理管理器中, 除非 `skipCache` 是真的 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 纹理中独特的基于字符串的密钥. |
| source | HTMLCanvasElement | 否 |  | 构成新纹理基础的坎瓦斯元素. |
| skipCache | boolean | 是 | false | 跳过将此纹理添加到缓存中吗 ? |


**返回值:** [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) - 创建的 Canvas 纹理, 或 `null` 如果密钥已经使用 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L667](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L667)  
引入版本：3.0.0


---

### addCompressedTexture {#addCompressedTexture}

#### \<instance> addCompressedTexture(key, textureData, [atlasData]) {#instance-addcompressedtexturekey-texturedata-atlasdata}


**说明:**

将压缩的纹理添加到此纹理管理器中 。

纹理一般应该通过`CompressedTextureFile`加载器装入,以便制备这种方法所需要的正确数据对象.

也可以选择将地图集数据传递到这种方法,在这种情况下,会从给定的压缩纹理中生成一个纹理图集,与地图集数据结合.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| textureData | [Phaser.Types.Textures.CompressedTextureData](/api/typedef/types-textures#compressedtexturedata) | 否 | 压缩纹理数据对象. |
| atlasData | object | 是 | 可选纹理图集数据. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建的纹理, 或如果密钥已经使用的话, 则使用 `null` 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L545](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L545)  
引入版本：3.60.0


---

### addDynamicTexture {#addDynamicTexture}

#### \<instance> addDynamicTexture(key, [width], [height], [forceEven]) {#instance-adddynamictexturekey-width-height-forceeven}


**说明:**

创建动态纹理实例,并加入到此纹理管理器中。

动态纹理(Dynamic Texture)是一种特殊的纹理,它允许您直接绘制纹理,帧和最类游戏对象.

您可以带许多复杂的对象到这个纹理, 然后可以用来作为其他游戏对象, 如Sprites 的基础纹理。 如果您再更新这个纹理, 所有使用它的游戏对象都会立即更新, 立即反映变化 。

这是一种强大的方法,在运行时生成动态纹理,这种纹理是WebGL友好的,并且不会在每个变化上引用昂贵的GPU上传.

详见`DynamicTexture`类上可用的方法.

可选的,您也可以通过此方法的动态纹理实例,使其添加到纹理管理器中.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) | 否 |  | 此纹理的字符串键。 必须是纹理管理器中唯一的。 或是一个动态图例 。 |
| width | number | 是 | 256 | 此动态纹理在像素中的宽度。 默认为 256 x 256。 如果一个实例被传递为密钥, 则忽略 。 |
| height | number | 是 | 256 | 此动态纹理在像素中的高度。 默认为 256 x 256。 如果一个实例被传递为密钥, 则忽略了 。 |
| forceEven | boolean | 是 | true | 如果宽度和高度是奇数, 是否应该强制它们均匀 ? 如果一个实例被传递为密钥, 则忽略 。 |


**返回值:** [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) - 已创建的动态纹理, 或如果密钥已经使用的话, 则使用 `null` 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L704](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L704)  
引入版本：3.60.0


---

### addFlatColor {#addFlatColor}

#### \<instance> addFlatColor(key, width, height, [color], [alpha]) {#instance-addflatcolorkey-width-height-color-alpha}


**说明:**

从颜色和α创建纹理。纹理将充满给定的颜色和α。

这可能用作代理纹理, 以后可以替换为真实纹理。 更多关于替换代用纹理的信息请参见 [Phaser.Textures.Texture#setSource](/api/class/textures-texture#setSource) 。

这只可用WebGL模式.

**Tags:**

 - webglonly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 纹理中独特的基于字符串的密钥. |
| width | number | 否 |  | 纹理的宽度. |
| height | number | 否 |  | 纹理的高度. |
| color | number | 是 | "0x000000" | 纹理之色. |
| alpha | number | 是 | 0 | 纹理的α. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建的纹理,或 `null` 如果密钥已经使用,或者宽度或高度不为正数。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L1250](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1250)  
引入版本：4.0.0


---

### addGLTexture {#addGLTexture}

#### \<instance> addGLTexture(key, glTexture) {#instance-addgltexturekey-gltexture}


**说明:**

使用一个WebGLTextureWrapper,并从中创建一个Phaser纹理,它使用给定的密钥添加到纹理管理器中.

这样您就可以使用纹理作为像Sprites这样的基于纹理的游戏对象的普通纹理.

这是WebGL的唯一功能。

在此之前 Phaser 3.8.0.0,这个方法没有了 `WebGLTexture` 作为 `glTexture` 参数。您现在必须围起来 `WebGLTexture` 在一个 `WebGLTextureWrapper` 以实例的形式,然后将其传递给这种方法。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| glTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 否 | 源流雷达纹理. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建的纹理, 或如果密钥已经使用的话, 则使用 `null` 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L505](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L505)  
引入版本：3.19.0


---

### addImage {#addImage}

#### \<instance> addImage(key, source, [dataSource]) {#instance-addimagekey-source-datasource}


**说明:**

向从给定的图像元素创建的纹理管理器中添加新的纹理。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| source | HTMLImageElement | 否 | 源图像元素. |
| dataSource | HTMLImageElement \| HTMLCanvasElement | 是 | 一种可选的数据图像元素. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建的纹理, 或如果密钥已经使用的话, 则使用 `null` 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L470](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L470)  
引入版本：3.0.0


---

### addRenderTexture {#addRenderTexture}

#### \<instance> addRenderTexture(key, renderTexture) {#instance-addrendertexturekey-rendertexture}


**说明:**

使用给定的密钥在纹理管理器中添加一个纹理。这允许您使用纹理作为像Sprites这样的纹理游戏对象的普通纹理。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| renderTexture | [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) | 否 | 源流雷达纹理. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建的纹理, 或如果密钥已经使用的话, 则使用 `null` 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L607](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L607)  
引入版本：3.12.0


---

### addSpriteSheet {#addSpriteSheet}

#### \<instance> addSpriteSheet(key, source, config, [dataSource]) {#instance-addspritesheetkey-source-config-datasource}


**说明:**

将 Sprite 工作表添加到此纹理管理器中 。

在 Phaser 术语中, Sprite 工作表是一个包含不同帧的纹理, 但每个帧的尺寸完全相同, 无法修剪或旋转。 这与Texture Packer 等工具创建的纹理图集不同, 与 Aseprite 或 旧街机 等应用获得的固定帧导出更相似 。

至Phaser 3.60,您可以使用这种方法在现有的Phaser纹理中添加一个图示表.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中唯一基于字符串的密钥。 如果您提供了 Phaser 纹理作为第 2 个参数, 请给出一个空字符串 。 |
| source | HTMLImageElement \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 源图像元素,或Phaser纹理. |
| config | [Phaser.Types.Textures.SpriteSheetConfig](/api/typedef/types-textures#spritesheetconfig) | 否 | 此 Sprite 工作表的配置对象 。 |
| dataSource | HTMLImageElement \| HTMLCanvasElement | 是 | 一种可选的数据图像元素. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建或更新的纹理, 或者如果密钥已经使用的话, `null` 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L1098](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1098)  
引入版本：3.0.0


---

### addSpriteSheetFromAtlas {#addSpriteSheetFromAtlas}

#### \<instance> addSpriteSheetFromAtlas(key, config) {#instance-addspritesheetfromatlaskey-config}


**说明:**

将 Sprite 工作表添加到此纹理管理器中, 即该工作表作为框架存在于纹理图集中 。

在Phaser术语中,Sprite Sheet是一个包含不同框架的纹理,但每个框架的大小完全相同,不能修剪或旋转.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| config | [Phaser.Types.Textures.SpriteSheetFromAtlasConfig](/api/typedef/types-textures#spritesheetfromatlasconfig) | 否 | 此 Sprite 工作表的配置对象 。 |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建的纹理, 或如果密钥已经使用的话, 则使用 `null` 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L1152](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1152)  
引入版本：3.0.0


---

### addUint8Array {#addUint8Array}

#### \<instance> addUint8Array(key, data, width, height) {#instance-adduint8arraykey-data-width-height}


**说明:**

从一系列颜色数据创建纹理。

这只可用WebGL模式.

如果提供的尺寸是两个功率,则由此产生的纹理会自动被WebGL渲染器设定为包扎.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| data | Uint8Array | 否 | 纹理的颜色数据 。 |
| width | number | 否 | 纹理的宽度. |
| height | number | 否 | 纹理的高度. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建的纹理, 或如果密钥已经使用的话, 则使用 `null` 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L1211](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1211)  
引入版本：3.80.0


---

### addUnityAtlas {#addUnityAtlas}

#### \<instance> addUnityAtlas(key, source, data, [dataSource]) {#instance-addunityatlaskey-source-data-datasource}


**说明:**

将一个统一纹理图集添加到此纹理管理器中 。

在Phaser术语中,一个纹理图集是图集图像和数据文件的组合,例如由Texture Packer或Unity等应用程序导出的数据文件.

地图集的框架数据必须存储在Unity YAML文件中.

至Phaser 3.60,您可以使用这种方法在现有的Phaser纹理中添加地图集数据集.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| source | HTMLImageElement | 否 | 源图像元素. |
| data | object | 否 | 纹理图集数据. |
| dataSource | HTMLImageElement \| HTMLCanvasElement | Array.\<HTMLImageElement> | Array.\<HTMLCanvasElement> | 是 | 一种可选的数据图像元素. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建的纹理, 或如果密钥已经使用的话, 则使用 `null` 。


**Fires:** [Phaser.Textures.Events#event:ADD](/api/event/textures-events#add)


> 源码：[src/textures/TextureManager.js#L1047](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1047)  
引入版本：3.0.0


---

### checkKey {#checkKey}

#### \<instance> checkKey(key) {#instance-checkkeykey}


**说明:**

检查给定的纹理密钥, 如果密钥已经使用, 则记录一个控制台. error, 然后返回假 。

如果你想避开控制台. warn, 那就用`TextureManager.exists`代替.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理键要检查 。 |


**返回值:** boolean - 如果安全使用纹理键,则使用`true`,否则使用`false`.


> 源码：[src/textures/TextureManager.js#L254](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L254)  
引入版本：3.7.0


---

### cloneFrame {#cloneFrame}

#### \<instance> cloneFrame(key, frame) {#instance-cloneframekey-frame}


**说明:**

使用纹理密钥和框架名称,如果找到,则返回该框架的克隆。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| frame | string \| number | 否 | 要克隆的框架的字符串或索引 。 |


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 给定框架的克隆体 。


> 源码：[src/textures/TextureManager.js#L1385](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1385)  
引入版本：3.0.0


---

### create {#create}

#### \<instance> create(key, source, [width], [height]) {#instance-createkey-source-width-height}


**说明:**

使用给定的源和维度创建新的纹理。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| source | [Phaser.Types.Textures.TextureSource](/api/typedef/types-textures#texturesource) \| Array.\<[Phaser.Types.Textures.TextureSource](/api/typedef/types-textures#texturesource)> | 否 | 用于创建纹理的源或数组源,通常为图像,但也可以是Canvas或其他类型. |
| width | number | 是 | 纹理的宽度。 这是可选的, 并且自动从源图像中导出 。 |
| height | number | 是 | 纹理的高度。 这是可选的, 并且自动从源图像中衍生出来 。 |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 创建的纹理, 或如果密钥已经使用的话, 则使用 `null` 。


> 源码：[src/textures/TextureManager.js#L1303](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1303)  
引入版本：3.0.0


---

### createCanvas {#createCanvas}

#### \<instance> createCanvas(key, [width], [height]) {#instance-createcanvaskey-width-height}


**说明:**

使用大小为空白的 Canvas 元素创建新纹理 。

罐头元素自动集合,称这种方法将从罐头波尔提取一个免费的画布,或者在没有可用的情况下创建一个.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 纹理中独特的基于字符串的密钥. |
| width | number | 是 | 256 | 坎瓦斯元素的宽度 。 |
| height | number | 是 | 256 | 坎瓦斯元素的高度. |


**返回值:** [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) - 创建的 Canvas 纹理, 或 `null` 如果密钥已经使用 。


> 源码：[src/textures/TextureManager.js#L637](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L637)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁纹理管理器和存储在其中的所有纹理管理器。


**Overrides:** Phaser.Events.EventEmitter#销毁


> 源码：[src/textures/TextureManager.js#L1744](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1744)  
引入版本：3.0.0


---

### each {#each}

#### \<instance> each(callback, scope, [args]) {#instance-eachcallback-scope-args}


**说明:**

将所有纹理传递给给给定的回调。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | EachTextureCallback | 否 | 发送到纹理的回调函数 。 |
| scope | object | 否 | 执行回调时用作 `this` 的值 。 |
| args | * | 是 | 更多论点,在孩子出生后,会转给回电者。 |


> 源码：[src/textures/TextureManager.js#L1660](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1660)  
引入版本：3.0.0


---

### exists {#exists}

#### \<instance> exists(key) {#instance-existskey}


**说明:**

检查给定的密钥, 以查看此纹理管理器中是否有使用它纹理的纹理 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |


**返回值:** boolean - 如果此纹理管理器中存在匹配给定密钥的纹理, 则返回 `true` 。


> 源码：[src/textures/TextureManager.js#L1330](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1330)  
引入版本：3.0.0


---

### get {#get}

#### \<instance> get(key) {#instance-getkey}


**说明:**

从纹理管理器返回匹配给定密钥的纹理。

如果钥匙是`undefined`,它会还原`__DEFAULT`纹理.

如果密钥是纹理的实例,它会返回实例.

如果密钥是框架实例, 它将会返回框架父纹理实例 。

最后,如果给定了密钥,但没有找到,也没有纹理或框架实例,它会返回`__MISSING`纹理.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | [Phaser.Textures.Frame](/api/class/textures-frame) | 否 | 纹理,或纹理,或框架实例中唯一基于字符串的密钥 。 |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 匹配给定密钥的纹理 。


> 源码：[src/textures/TextureManager.js#L1345](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1345)  
引入版本：3.0.0


---

### getBase64 {#getBase64}

#### \<instance> getBase64(key, [frame], [type], [encoderOptions]) {#instance-getbase64key-frame-type-encoderoptions}


**说明:**

获得一个已有的纹理框架并将其转换为基质64编码的图像,并返回基质64数据.

也可以提供图像类型和编码器选项.

这将只与位图纹理框架(例如从纹理图集创建的纹理框架)配合。 它不会与 GL 纹理对象(例如Shaders) 或 Render 纹理对象配合。 对于这些对象,请参见 WebGL Snapshot 函数 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 纹理中独特的基于字符串的密钥. |
| frame | string \| number | 是 |  | 框架的字符串名称,或整数索引,从纹理中获取。 |
| 类型 | string | 是 | "'image/png'" | 表示图像格式的 DOMSTring。默认格式类型是图像/png 。 |
| encoderOptions | number | 是 | 0.92 | 0到 1 之间的数字表示图像格式所使用的图像质量, 使用图像/ jpeg 和图像/ webp 等失落压缩。 如果此参数是其它任何参数, 则使用图像质量的默认值。 默认值为 0. 92. 其他参数被忽略 。 |


**返回值:** string - 碱基64编码数据,或者无法找到纹理框架的空字符串.


> 源码：[src/textures/TextureManager.js#L405](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L405)  
引入版本：3.12.0


---

### getFrame {#getFrame}

#### \<instance> getFrame(key, [frame]) {#instance-getframekey-frame}


**说明:**

使用纹理密钥和框架名称,如果找到,则返回引用该框架的选项。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| frame | string \| number | 是 | 框架的字符串名称,或整数索引,从纹理中获取。 |


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 纹理框架对象 。


> 源码：[src/textures/TextureManager.js#L1404](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1404)  
引入版本：3.0.0


---

### getPixel {#getPixel}

#### \<instance> getPixel(x, y, key, [frame]) {#instance-getpixelx-y-key-frame}


**说明:**

以纹理和`x`和`y`为坐标,这种方法将返回一个新的彩色对象,该对象在纹理中该位置上已包含像素的颜色和α值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 纹理内部像素的x坐标. |
| y | number | 否 | 纹理内像素的y坐标. |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| frame | string \| number | 是 | 框架的字符串或索引 。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 包含有请求像素的颜色值的颜色对象,或者如果坐标超出界限,则使用 `null` 。


> 源码：[src/textures/TextureManager.js#L1493](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1493)  
引入版本：3.0.0


---

### getPixelAlpha {#getPixelAlpha}

#### \<instance> getPixelAlpha(x, y, key, [frame]) {#instance-getpixelalphax-y-key-frame}


**说明:**

给定一个纹理和一个`x`和`y`协调此方法, 返回一个值在 0 到 255 之间, 与纹理中该位置的像素的α值相对应。 如果坐标脱离了界限, 则返回无效 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 纹理内部像素的x坐标. |
| y | number | 否 | 纹理内像素的y坐标. |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| frame | string \| number | 是 | 框架的字符串或索引 。 |


**返回值:** number - 值在 0 到 255 之间,如果坐标超出界限,则为 `null` 。


> 源码：[src/textures/TextureManager.js#L1548](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1548)  
引入版本：3.10.0


---

### getTextureKeys {#getTextureKeys}

#### \<instance> getTextureKeys() {#instance-gettexturekeys}


**说明:**

返回一个带有此纹理管理器中所有纹理密钥的阵列。 输出阵列将排除 `__DEFAULT` 、 `__MISSING` 、 `__WHITE` 和 `__NORMAL` 密钥 。


**返回值:** Array.\<string> - 包含存储在此纹理管理器中的所有纹理密钥的阵列 。


> 源码：[src/textures/TextureManager.js#L1469](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1469)  
引入版本：3.0.0


---

### parseFrame {#parseFrame}

#### \<instance> parseFrame(key) {#instance-parseframekey}


**说明:**

解析“ key” 参数并返回一个纹理框架实例 。

它可以接受以下格式:

1) 字符串 2 元素为: [键, [框] 的数组 3 属性为: {键, [框]} 4 的对象 纹理实例 - 从纹理 5 返回默认框架 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| array | object | [Phaser.Textures.Texture](/api/class/textures-texture) | [Phaser.Textures.Frame](/api/class/textures-frame) | 否 | 解开的钥匙 |


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 如果找到纹理框架对象, 或如果没有定义, 则未定义 。


> 源码：[src/textures/TextureManager.js#L1423](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1423)  
引入版本：3.60.0


---

### remove {#remove}

#### \<instance> remove(key) {#instance-removekey}


**说明:**

从纹理管理器中删除一个纹理并销毁它。 这将立即清除纹理管理器中所有引用, 如果有, 则销毁它的 WebGLTexture。 这将释放一个 `removetexture`事件 。

注意: 如果您还有游戏对象仍然使用此纹理, 它们在下次尝试渲染时会开始抛出错误。 请确定删除纹理是清理后避免出现这种情况的最后一步 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 纹理要删除的密钥,或指代它. |


**返回值:** [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) - 纹理经理.


**Fires:** [Phaser.Textures.Events#event:REMOVE](/api/event/textures-events#remove)


> 源码：[src/textures/TextureManager.js#L282](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L282)  
引入版本：3.7.0


---

### removeKey {#removeKey}

#### \<instance> removeKey(key) {#instance-removekeykey}


**说明:**

从纹理管理器中删除密钥, 但不会破坏正在使用密钥的纹理 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 从纹理列表中删除的密钥 。 |


**返回值:** [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) - 纹理经理.


> 源码：[src/textures/TextureManager.js#L332](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L332)  
引入版本：3.17.0


---

### renameTexture {#renameTexture}

#### \<instance> renameTexture(currentKey, newKey) {#instance-renametexturecurrentkey-newkey}


**说明:**

将纹理使用的密钥更改为新提供的密钥 。

旧键被移除,允许重新使用.

游戏对象通过引用纹理对象与纹理连接,因此所有现有的引用都会被保留.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| currentKey | string | 否 | 您想要重命名的纹理当前基于字符串的密钥 。 |
| newKey | string | 否 | 用于纹理的新的基于字符串的密钥 。 |


**返回值:** boolean - 如果纹理键成功改名为`true`,否则`false`.


> 源码：[src/textures/TextureManager.js#L1626](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1626)  
引入版本：3.12.0


---

### resetStamp {#resetStamp}

#### \<instance> resetStamp([alpha], [tint]) {#instance-resetstampalpha-tint}


**说明:**

重置内部的 Samp 对象, 准备绘制并返回 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| alpha | number | 是 | 1 | 用来使用的α. |
| tint | number | 是 | "0xffffff" | 仅限WebGL,使用的色调 |


**返回值:** [Phaser.GameObjects.Image](/api/class/gameobjects-image) - 参考邮票游戏对象.


> 源码：[src/textures/TextureManager.js#L1687](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1687)  
引入版本：3.60.0


---

### resetTileSprite {#resetTileSprite}

#### \<instance> resetTileSprite([alpha], [tint]) {#instance-resettilespritealpha-tint}


**说明:**

重置内部的 Tile 闪光对象, 准备绘制, 并返回 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| alpha | number | 是 | 1 | 用来使用的α. |
| tint | number | 是 | "0xffffff" | 仅限WebGL,使用的色调 |


**返回值:** [Phaser.GameObjects.TileSprite](/api/class/gameobjects-tilesprite) - 提及 Tile Sprite 游戏对象 。


> 源码：[src/textures/TextureManager.js#L1716](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1716)  
引入版本：4.0.0


---

### setTexture {#setTexture}

#### \<instance> setTexture(gameObject, key, [frame]) {#instance-settexturegameobject-key-frame}


**说明:**

设定指定的游戏对象 `texture` 财务报告和已审计财务报表 `frame` 属性,以便使用 `key` 财务报告和已审计财务报表 `frame` 参数到此方法。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 将设置纹理的游戏对象 。 |
| key | string | 否 | 纹理中独特的基于字符串的密钥. |
| frame | string \| number | 是 | 框架的字符串或索引 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 纹理设定的游戏对象 。


> 源码：[src/textures/TextureManager.js#L1602](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/TextureManager.js#L1602)  
引入版本：3.0.0


---

---
