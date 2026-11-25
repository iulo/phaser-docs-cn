# Texture {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/textures-texture)

纹理图集包含一个源,通常是缓存的图像,以及一个框架集合。 纹理图集代表着纹理的不同区域。 例如, 纹理图集可能有许多框架, 每一个要素都有一个框架。 单个图像的图像只有一个框架, 包含整个图像 。

每个纹理,无论来自何处,都至少有一个叫做`__BASE`框架的帧,这个帧代表了源图像的全部.

纹理由全局纹理管理器管理。 这是一个单顿类,负责创建和向游戏对象发送纹理及其相应的框架。

螺旋兽和其他游戏对象从纹理管理器获得它们需要的纹理数据.

**构造函数**

`new Texture(manager, key, source, [width], [height])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) | 否 | 引用此纹理属于的纹理管理器 。 |
| key | string | 否 | 此纹理中独特的基于字符串的密钥 。 |
| source | HTMLImageElement \| HTMLCanvasElement | Array.\<HTMLImageElement> | Array.\<HTMLCanvasElement> | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 否 | 用于创建纹理的源数组,通常为图像,但也可以是Canvas. |
| width | number | 是 | 纹理的宽度。 这是可选的, 并且自动从源图像中导出 。 |
| height | number | 是 | 纹理的高度。 这是可选的, 并且自动从源图像中衍生出来 。 |

---


**作用域**: static

> 源码：[src/textures/Texture.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L13)  
引入版本：3.0.0

## 公开成员 {#public-members}

### customData {#customData}

#### customData: object {#customdata-object}


**说明:**

来源JSON中设置的任何额外数据(如果有的话),或者您想要存储的与此纹理相关的任何额外数据.


> 源码：[src/textures/Texture.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L97)  
引入版本：3.0.0


---

### dataSource {#dataSource}

#### dataSource: array {#datasource-array}


**说明:**

一系列的纹理源数据实例。 用于存储额外的数据图像, 如普通的地图或光谱图 。


> 源码：[src/textures/Texture.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L78)  
引入版本：3.0.0


---

### firstFrame {#firstFrame}

#### firstFrame: string {#firstframe-string}


**说明:**

纹理第一帧的名称.


> 源码：[src/textures/Texture.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L107)  
引入版本：3.0.0


---

### frames {#frames}

#### frames: object {#frames-object}


**说明:**

将唯一框架键与框架对象连接在一起的密钥值对象对。


> 源码：[src/textures/Texture.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L88)  
引入版本：3.0.0


---

### frameTotal {#frameTotal}

#### frameTotal: number {#frametotal-number}


**说明:**

包括`__BASE`框架在内的此纹理中框架的总数.

纹理总是包含至少1帧,因为每个纹理默认包含一个`__BASE`帧,此外,任何额外的帧也被添加到其中,比如在解析Sprite工作表或纹理图集时.


> 源码：[src/textures/Texture.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L116)  
引入版本：3.0.0


---

### key {#key}

#### key: string {#key-string}


**说明:**

此纹理中独特的基于字符串的密钥 。


> 源码：[src/textures/Texture.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L59)  
引入版本：3.0.0


---

### manager {#manager}

#### manager: [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) {#manager-phasertexturestexturemanager}


**说明:**

引用此纹理属于的纹理管理器 。


> 源码：[src/textures/Texture.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L50)  
引入版本：3.0.0


---

### smoothPixelArt {#smoothPixelArt}

#### smoothPixelArt: boolean {#smoothpixelart-boolean}


**说明:**

控制使用此纹理的着色器在渲染像素艺术时是否应用平滑插值。启用时,渲染器使用基于阴影的平滑处理来减少升平像素艺术的夹痕外观。这依赖于着色器的支持。

如果 `null`,游戏默认会被使用.


> 源码：[src/textures/Texture.js#L129](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L129)  
引入版本：4.0.0


---

### source {#source}

#### source: Array.\<[Phaser.Textures.TextureSource](/api/class/textures-texturesource)> {#source-arrayphasertexturestexturesource}


**说明:**

一系列的纹理源实例。 这些是这种纹理所独有的, 包含实际的图像( 或 Canvas) 数据 。


> 源码：[src/textures/Texture.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L68)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(name, sourceIndex, x, y, width, height) {#instance-addname-sourceindex-x-y-width-height}


**说明:**

向此纹理添加新框架。

AFrame是一个纹理源的矩形区域,具有独特的索引或字符串键.

给定的名称必须是此纹理中唯一的。 如果它已经存在, 此方法将返回 `null` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | number \| string | 否 | 此框架的名称。 名称在纹理内是独一无二的 。 |
| sourceIndex | number | 否 | 纹理源的索引,这个框架是其中的一部分. |
| x | number | 否 | 此框架左上角的 x 坐标 。 |
| y | number | 否 | 此框架左上角的 Y 坐标 。 |
| width | number | 否 | 此框架的宽度 。 |
| height | number | 否 | 此框架的高度 。 |


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 添加到此纹理中的框架, 或者 `null` 如果给定的名称已经存在 。


> 源码：[src/textures/Texture.js#L150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L150)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

破坏这种纹理并发布其来源和框架的引用。


> 源码：[src/textures/Texture.js#L676](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L676)  
引入版本：3.0.0


---

### get {#get}

#### \<instance> get([name]) {#instance-getname}


**说明:**

以“框架”的密钥或索引为基础,从此纹理中获取框架。

在纹理图集框架中,通常用密钥来引用。在Sprite工作表框架中,用索引来引用。名称不通过值返回基本纹理。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string \| number | 是 | 要从此纹理中获取框架的字符串名称,或整数索引。 |


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 纹理框架 。


> 源码：[src/textures/Texture.js#L238](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L238)  
引入版本：3.0.0


---

### getDataSourceImage {#getDataSourceImage}

#### \<instance> getDataSourceImage([name]) {#instance-getdatasourceimagename}


**说明:**

给定框架名称, 请返回它用来渲染的数据源图像。 您可以用它来获取图像的普通映射 。

这将返回 DOM 图像 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string \| number | 是 | 要从此纹理中获取框架的字符串名称,或整数索引。 |


**返回值:** HTMLImageElement, HTMLCanvasElement - DOM 图像或 Canvas 元素 。


> 源码：[src/textures/Texture.js#L453](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L453)  
引入版本：3.7.0


---

### getFrameBounds {#getFrameBounds}

#### \<instance> getFrameBounds([sourceIndex]) {#instance-getframeboundssourceindex}


**说明:**

根据给定的纹理源索引,这种方法将使用该源来获取所有框架,然后确定它们包含的界限,在对象中返回。

如果这个纹理是图集中的图案工作表, 并且您需要知道图案工作表的总界限, 则此功能是有用的 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| sourceIndex | number | 是 | 0 | 纹理源的索引以获取框架的界限 。 |


**返回值:** [Phaser.Types.Math.RectangleLike](/api/typedef/types-math#rectanglelike) - 使用给定的纹理源索引包含框架界限的对象。


> 源码：[src/textures/Texture.js#L333](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L333)  
引入版本：3.80.0


---

### getFrameNames {#getFrameNames}

#### \<instance> getFrameNames([includeBase]) {#instance-getframenamesincludebase}


**说明:**

返回带有此纹理中所有框架名称的数组。

如果您想要随机指定一个框架到游戏对象, 则有用, 因为您可以从返回的数组中选择一个随机元素 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| includeBase | boolean | 是 | false | 在输出阵列中包含 `__BASE`框架吗 ? |


**返回值:** Array.\<string> - 此纹理中所有框架名称的数组 。


> 源码：[src/textures/Texture.js#L388](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L388)  
引入版本：3.0.0


---

### getFramesFromTextureSource {#getFramesFromTextureSource}

#### \<instance> getFramesFromTextureSource(sourceIndex, [includeBase]) {#instance-getframesfromtexturesourcesourceindex-includebase}


**说明:**

返回给定的纹理源中所有框架的数组。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| sourceIndex | number | 否 |  | 纹理源代码的索引来获取框架 。 |
| includeBase | boolean | 是 | false | 在输出阵列中包含 `__BASE`框架吗 ? |


**返回值:** Array.\<[Phaser.Textures.Frame](/api/class/textures-frame)> - 一系列纹理框架 。


> 源码：[src/textures/Texture.js#L298](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L298)  
引入版本：3.0.0


---

### getSourceImage {#getSourceImage}

#### \<instance> getSourceImage([name]) {#instance-getsourceimagename}


**说明:**

给定框架名称, 返回它用来渲染的源图像 。

这将返回 DOM 图像或 Canvas 元素 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string \| number | 是 | 要从此纹理中获取框架的字符串名称,或整数索引。 |


**返回值:** HTMLImageElement, HTMLCanvasElement, [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - DOM图像, Canvas元素或渲染纹理.


> 源码：[src/textures/Texture.js#L420](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L420)  
引入版本：3.0.0


---

### getTextureSourceIndex {#getTextureSourceIndex}

#### \<instance> getTextureSourceIndex(source) {#instance-gettexturesourceindexsource}


**说明:**

取给定的纹理源并返回它在这个纹理内内的索引。 如果它不在纹理内, 它返回 -1. 除非这个纹理有多个纹理源, 如多阿特拉斯, 此方法将总是返回零或 -1.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Textures.TextureSource](/api/class/textures-texturesource) | 否 | 纹理来源要检查 。 |


**返回值:** number - 此纹理内纹理源的索引, 或 - 1 如果不是此纹理中纹理源的索引 。


> 源码：[src/textures/Texture.js#L272](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L272)  
引入版本：3.0.0


---

### has {#has}

#### \<instance> has(name) {#instance-hasname}


**说明:**

检查是否在此纹理中存在匹配给定密钥的框架 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 要检查的框架的密钥 。 |


**返回值:** boolean - 如果此纹理中存在匹配密钥的框架, 则为真 。


> 源码：[src/textures/Texture.js#L223](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L223)  
引入版本：3.0.0


---

### remove {#remove}

#### \<instance> remove(name) {#instance-removename}


**说明:**

从此纹理中删除给定的框架。 框架立即被销毁 。

使用此框架的游戏对象, 应在_ 删除前停止使用, 因为不会自动发生 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 要删除的框架的密钥 。 |


**返回值:** boolean - 如果此纹理中移除了匹配密钥的框架, 则为真 。


> 源码：[src/textures/Texture.js#L194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L194)  
引入版本：3.19.0


---

### setDataSource {#setDataSource}

#### \<instance> setDataSource(data, [startIndex], [renew], [width], [height]) {#instance-setdatasourcedata-startindex-renew-width-height}


**说明:**

将数据源图像添加到此纹理中。

数据源图像的一个例子是普通地图,这个纹理的所有框架都同样适用于普通地图。

每个"正规"源条目只能有一个数据源.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| data | [Phaser.Types.Textures.TextureSource](/api/typedef/types-textures#texturesource) \| Array.\<[Phaser.Types.Textures.TextureSource](/api/typedef/types-textures#texturesource)> | 否 |  | 源头图像数据. |
| startIndex | number | 是 | 0 | 第一个源更新的索引。如果有多个数据要素,它们将应用于后续的索引。 |
| renew | boolean | 是 | false | 是否销毁已有源并创建新源, 如果一个源已经在索引中的数组中 。 |
| width | number | 是 |  | 如果数据中找不到, 则需要使用宽度( 例如使用 Uint8 箭头) |
| height | number | 是 |  | 如果数据不可用,使用高度(例如使用Uint8箭头) |


> 源码：[src/textures/Texture.js#L544](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L544)  
引入版本：4.0.0


---

### setFilter {#setFilter}

#### \<instance> setFilter(filterMode) {#instance-setfilterfiltermode}


**说明:**

设置此纹理的过滤模式。

模式可以是线性,默认,也可以是近似.

对于像素艺术,你应该使用最接近。

该模式适用于整个纹理,而不仅仅是它的特定框架.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| filterMode | [Phaser.Textures.FilterMode](/api/namespace/textures-filtermode) | 否 | 过滤模式。 |


> 源码：[src/textures/Texture.js#L590](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L590)  
引入版本：3.0.0


---

### setSmoothPixelArt {#setSmoothPixelArt}

#### \<instance> setSmoothPixelArt(value) {#instance-setsmoothpixelartvalue}


**说明:**

设置此纹理的 `smoothPixelArt` 属性。 如果 `true`, 也会运行 `setFilter(Phaser.Textures.FilterMode.LINEAR)` 以启用必要的线性过滤。 如果 `false` , 它不会改变过滤模式, 因为它不知道以前的状态, 也没有必要更改它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean \| null | 否 | 设定为 `true` 以启用平滑像素艺术插值并应用 LINEAR 过滤。 设定为 `false` 以禁用平滑插值而不改变过滤模式。 设定为 `null` 以使用游戏的默认设置 。 |


> 源码：[src/textures/Texture.js#L619](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L619)  
引入版本：4.0.0


---

### setSource {#setSource}

#### \<instance> setSource(data, [startIndex], [renew], [width], [height]) {#instance-setsourcedata-startindex-renew-width-height}


**说明:**

设置此纹理的源数据。 默认情况下, 这将更新任何已有的源, 并有效覆盖它们 。

最好只交换大小相同的纹理,因为游戏对象的维度往往来自纹理大小,如果不匹配,可能会以意想不到的方式变化.

任何相关的`dataSource`成员必须更新。见[Phaser.Textures.Texture#setDataSource](/api/class/textures-texture#setDataSource)。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| data | [Phaser.Textures.TextureSource](/api/class/textures-texturesource) \| [Phaser.Types.Textures.TextureSource](/api/typedef/types-textures#texturesource) | Array.\<[Phaser.Textures.TextureSource](/api/class/textures-texturesource)> | Array.\<[Phaser.Types.Textures.TextureSource](/api/typedef/types-textures#texturesource)> | 否 |  | 源头图像数据. |
| startIndex | number | 是 | 0 | 第一个源更新的索引。如果有多个数据要素,它们将应用于后续的索引。 |
| renew | boolean | 是 | false | 是否销毁已有源并创建新源, 如果一个源已经在索引中的数组中 。 |
| width | number | 是 |  | 如果数据中找不到, 则需要使用宽度( 例如使用 Uint8 箭头) |
| height | number | 是 |  | 如果数据不可用,使用高度(例如使用Uint8箭头) |


> 源码：[src/textures/Texture.js#L490](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L490)  
引入版本：4.0.0


---

### setWrap {#setWrap}

#### \<instance> setWrap(wrapModeS, [wrapModeT]) {#instance-setwrapwrapmodes-wrapmodet}


**说明:**

设置此纹理的包覆模式 。

仅供WebGL使用。

包装模式可以是以下一种: 包装模式:

- Phaser.Textures.WrapMode.CLAMP_TO_EDGE

- Phaser.Textures.WrapMode.REPEAT

- Phaser.Textures.WrapMode.MIRRORED_REPEAT

注意, 仅支持 CLAMP_ TO_ EDGE 的非纹理功率。 如果为这样的纹理指定了另一个包模式, 则会忽略它 。

**Tags:**

 - webglonly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| wrapModeS | [Phaser.Textures.WrapMode](/api/namespace/textures-wrapmode) | 否 | S( 横向) 轴的包覆模式 。 |
| wrapModeT | [Phaser.Textures.WrapMode](/api/namespace/textures-wrapmode) | 是 | T(垂直)轴的包模式。 |


> 源码：[src/textures/Texture.js#L640](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Texture.js#L640)  
引入版本：4.0.0


---

---
