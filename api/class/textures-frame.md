# Frame {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/textures-frame)

框架是纹理的一部分。 它定义了纹理源内的长方形子区域, 存储其位置、 维度、 紫外线坐标和可选的修饰数据( 对于已包装的地图册框架, 并删除了白空 ) 。 框架是游戏对象所使用的纹理地址的主要单位 — 当一个Sprite显示特定图像时, 它会引用一个框架 。

**构造函数**

`new Frame(texture, name, sourceIndex, x, y, width, height)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此框架的纹理是其中的一部分 。 |
| 名称 | number \| string | 否 | 此框架的名称。 名称在纹理内是独一无二的 。 |
| sourceIndex | number | 否 | 纹理源的索引,这个框架是其中的一部分. |
| x | number | 否 | 此框架左上角的 x 坐标 。 |
| y | number | 否 | 此框架左上角的 Y 坐标 。 |
| width | number | 否 | 此框架的宽度 。 |
| height | number | 否 | 此框架的高度 。 |

---


**作用域**: static

> 源码：[src/textures/Frame.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L11)  
引入版本：3.0.0

## 公开成员 {#public-members}

### autoRound {#autoRound}

#### autoRound: number {#autoround-number}


**说明:**

覆盖渲染器设置 。 -1 = 使用渲染器设置 0 = 无圆形 1 = 圆形


> 源码：[src/textures/Frame.js#L231](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L231)  
引入版本：3.0.0


---

### canvasData {#canvasData}

#### canvasData: object {#canvasdata-object}


**说明:**

Canvas drawImage数据对象.


> 源码：[src/textures/Frame.js#L958](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L958)  
引入版本：3.0.0


---

### centerX {#centerX}

#### centerX: number {#centerx-number}


**说明:**

这个框的X中心,地板。


> 源码：[src/textures/Frame.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L169)  
引入版本：3.0.0


---

### centerY {#centerY}

#### centerY: number {#centery-number}


**说明:**

这个框的y中心,地板。


> 源码：[src/textures/Frame.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L178)  
引入版本：3.0.0


---

### customData {#customData}

#### customData: object {#customdata-object}


**说明:**

任何框架特定自定义数据都可以在此存储 。


> 源码：[src/textures/Frame.js#L244](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L244)  
引入版本：3.0.0


---

### customPivot {#customPivot}

#### customPivot: boolean {#custompivot-boolean}


**说明:**

此框架是否有自定义的中枢点 ?


> 源码：[src/textures/Frame.js#L207](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L207)  
引入版本：3.0.0


---

### cutHeight {#cutHeight}

#### cutHeight: number {#cutheight-number}


**说明:**

源图像中要剪切的区域高度 。


> 源码：[src/textures/Frame.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L102)  
引入版本：3.0.0


---

### cutWidth {#cutWidth}

#### cutWidth: number {#cutwidth-number}


**说明:**

要剪切的源图像中区域宽度 。


> 源码：[src/textures/Frame.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L93)  
引入版本：3.0.0


---

### cutX {#cutX}

#### cutX: number {#cutx-number}


**说明:**

X 在要剪切的源图像中的位置 。


> 源码：[src/textures/Frame.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L75)  
引入版本：3.0.0


---

### cutY {#cutY}

#### cutY: number {#cuty-number}


**说明:**

Y 位置在要剪切的源图像中 。


> 源码：[src/textures/Frame.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L84)  
引入版本：3.0.0


---

### glTexture {#glTexture}

#### glTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#gltexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

引用此框架使用的纹理源 WebGL纹理 。


> 源码：[src/textures/Frame.js#L838](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L838)  
引入版本：3.11.0


---

### halfHeight {#halfHeight}

#### halfHeight: number {#halfheight-number}


**说明:**

高度一半,地板,预估造型器


> 源码：[src/textures/Frame.js#L159](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L159)  
引入版本：3.0.0


---

### halfWidth {#halfWidth}

#### halfWidth: number {#halfwidth-number}


**说明:**

宽度的一半,地板,预估了制造器的尺寸。


> 源码：[src/textures/Frame.js#L149](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L149)  
引入版本：3.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

将此框架的渲染高度考虑为修剪高度 。


> 源码：[src/textures/Frame.js#L140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L140)  
引入版本：3.0.0


---

### is3Slice {#is3Slice}

#### is3Slice: boolean {#is3slice-boolean}


**说明:**

如果框架有大小9的边框数据,是3-切片还是9-切片数据?


> 源码：[src/textures/Frame.js#L941](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L941)  
引入版本：3.70.0


---

### name {#name}

#### name: string {#name-string}


**说明:**

此框架的名称。 名称在纹理内是独一无二的 。


> 源码：[src/textures/Frame.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L47)  
引入版本：3.0.0


---

### pivotX {#pivotX}

#### pivotX: number {#pivotx-number}


**说明:**

此框架的横向轴点 。


> 源码：[src/textures/Frame.js#L187](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L187)  
引入版本：3.0.0


---

### pivotY {#pivotY}

#### pivotY: number {#pivoty-number}


**说明:**

此框架的垂直偏转点 。


> 源码：[src/textures/Frame.js#L197](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L197)  
引入版本：3.0.0


---

### radius {#radius}

#### radius: number {#radius-number}


**说明:**

框架半径( 来源于 sqrt( w * + h * h) / 2)


> 源码：[src/textures/Frame.js#L890](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L890)  
引入版本：3.0.0


---

### realHeight {#realHeight}

#### realHeight: number {#realheight-number}


**说明:**

框架的高度,在未加边,未加边,在艺术包中准备,然后被打包.


> 源码：[src/textures/Frame.js#L872](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L872)  
引入版本：3.0.0


---

### realWidth {#realWidth}

#### realWidth: number {#realwidth-number}


**说明:**

框架的宽度, 如艺术包中准备的, 以未加边, 未加边的状态, 然后再装入 。


> 源码：[src/textures/Frame.js#L854](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L854)  
引入版本：3.0.0


---

### rotated {#rotated}

#### rotated: boolean {#rotated-boolean}


**说明:**

**CURRENTLY UNSUPPORTED**

此框架是否在纹理中旋转 ? 旋转允许您在纹理图集包装中使用旋转框架。 这与斯普丽特旋转无关 。


> 源码：[src/textures/Frame.js#L217](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L217)  
引入版本：3.0.0


---

### scale9 {#scale9}

#### scale9: boolean {#scale9-boolean}


**说明:**

框架是否有缩放9的边框数据?


> 源码：[src/textures/Frame.js#L924](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L924)  
引入版本：3.70.0


---

### source {#source}

#### source: [Phaser.Textures.TextureSource](/api/class/textures-texturesource) {#source-phasertexturestexturesource}


**说明:**

纹理源 此框架是其中的一部分 。


> 源码：[src/textures/Frame.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L57)  
引入版本：3.0.0


---

### sourceIndex {#sourceIndex}

#### sourceIndex: number {#sourceindex-number}


**说明:**

纹理源阵列中的纹理源索引.


> 源码：[src/textures/Frame.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L66)  
引入版本：3.0.0


---

### texture {#texture}

#### texture: [Phaser.Textures.Texture](/api/class/textures-texture) {#texture-phasertexturestexture}


**说明:**

此框架的纹理是其中的一部分 。


> 源码：[src/textures/Frame.js#L38](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L38)  
引入版本：3.0.0


---

### trimmed {#trimmed}

#### trimmed: boolean {#trimmed-boolean}


**说明:**

框架是否修剪过 ?


> 源码：[src/textures/Frame.js#L907](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L907)  
引入版本：3.0.0


---

### u0 {#u0}

#### u0: number {#u0-number}


**说明:**

WebGL UVu0值 。


> 源码：[src/textures/Frame.js#L253](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L253)  
引入版本：3.11.0


---

### u1 {#u1}

#### u1: number {#u1-number}


**说明:**

WebGL UV u1值 .


> 源码：[src/textures/Frame.js#L273](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L273)  
引入版本：3.11.0


---

### v0 {#v0}

#### v0: number {#v0-number}


**说明:**

WebGL UV v0 值 。


> 源码：[src/textures/Frame.js#L263](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L263)  
引入版本：3.11.0


---

### v1 {#v1}

#### v1: number {#v1-number}


**说明:**

WebGL UV v1 值 。


> 源码：[src/textures/Frame.js#L283](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L283)  
引入版本：3.11.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

将此框架的渲染宽度考虑在 brim 中 。


> 源码：[src/textures/Frame.js#L131](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L131)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

将此框架的X 渲染值抵消, 同时考虑到修饰值 。


> 源码：[src/textures/Frame.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L111)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

将 Y 渲染值与此框架相抵消, 同时考虑到修饰值 。


> 源码：[src/textures/Frame.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L121)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### clone {#clone}

#### \<instance> clone() {#instance-clone}


**说明:**

将这个框架克隆成一个新的框架对象 。


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 此框架的克隆 。


> 源码：[src/textures/Frame.js#L786](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L786)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

取消对母纹理和数据对象的引用,从而销毁此框架。


> 源码：[src/textures/Frame.js#L824](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L824)  
引入版本：3.0.0


---

### setCropUVs {#setCropUVs}

#### \<instance> setCropUVs(crop, x, y, width, height, flipX, flipY) {#instance-setcropuvscrop-x-y-width-height-flipx-flipy}


**说明:**

使用一个裁剪数据对象,并根据给定的矩区域计算所需的紫外坐标,以便裁剪此框架用于WebGL和Canvas渲染。

作物大小和坐标不得超过框架的大小。

直接使用 Game Object 纹理组件 `setCrop` 方法来命名。 请使用这种方法来设定 Game Object 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| crop | object | 否 | 裁剪数据对象。 这是 `GameObject._crop` 属性 。 |
| x | number | 否 | 启动裁剪的x坐标。 无法为负或超过框架宽度 。 |
| y | number | 否 | 启动裁剪的 Y 坐标。 无法为负或超过框架高度 。 |
| width | number | 否 | 裁剪矩形的宽度。 无法超过框架宽度 。 |
| height | number | 否 | 裁剪矩形的高度。 无法超过框架高度 。 |
| flipX | boolean | 否 | 父游戏对象是否设置了 flipX ? |
| flipY | boolean | 否 | 父游戏对象是否设置了 flipY ? |


**返回值:** object - 更新的作物数据对象.


> 源码：[src/textures/Frame.js#L527](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L527)  
引入版本：3.11.0


---

### setCutPosition {#setCutPosition}

#### \<instance> setCutPosition([x], [y]) {#instance-setcutpositionx-y}


**说明:**

设置要剪切的源图像中的 x 和 y 位置。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | X 在要剪切的源图像中的位置 。 |
| y | number | 是 | 0 | Y 位置在要剪切的源图像中 。 |


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 此框架对象 。


> 源码：[src/textures/Frame.js#L343](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L343)  
引入版本：3.85.0


---

### setCutSize {#setCutSize}

#### \<instance> setCutSize(width, height) {#instance-setcutsizewidth-height}


**说明:**

设定要剪切的源图像中的区域宽度和高度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 要剪切的源图像中区域宽度 。 |
| height | number | 否 | 源图像中要剪切的区域高度 。 |


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 此框架对象 。


> 源码：[src/textures/Frame.js#L365](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L365)  
引入版本：3.85.0


---

### setScale9 {#setScale9}

#### \<instance> setScale9(x, y, width, height) {#instance-setscale9x-y-width-height}


**说明:**

设置比例尺9中心矩形值。

Scale9是纹理包装器的一个特征,允许您定义一个九切缩放网格.

这是由 JSONArray 和 JSONHash 解析器自动设置的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 中尺度9矩形的左坐标. |
| y | number | 否 | 中心尺度9矩形的顶部坐标. |
| width | number | 否 | 中心尺度9矩形的宽度. |
| height | number | 否 | 中心尺度9的高度矩形. |


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 此框架对象 。


> 源码：[src/textures/Frame.js#L495](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L495)  
引入版本：3.70.0


---

### setSize {#setSize}

#### \<instance> setSize(width, height, [x], [y]) {#instance-setsizewidth-height-x-y}


**说明:**

设置此框架的宽度、 高度、 x 和 y 。

这被构造者自动称为,在飞行时很少应该更改.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 否 |  | 修剪前的框宽度 。 |
| height | number | 否 |  | 被修剪前的帧高度. |
| x | number | 是 | 0 | 此框架左上角的 x 坐标 。 |
| y | number | 是 | 0 | 此框架左上角的 Y 坐标 。 |


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 此框架对象 。


> 源码：[src/textures/Frame.js#L384](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L384)  
引入版本：3.7.0


---

### setTrim {#setTrim}

#### \<instance> setTrim(actualWidth, actualHeight, destX, destY, destWidth, destHeight) {#instance-settrimactualwidth-actualheight-destx-desty-destwidth-destheight}


**说明:**

如果在添加到Texture Atlas时对帧进行了修剪,则此记录了修剪和源数据.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| actualWidth | number | 否 | 修剪前的框宽度 。 |
| actualHeight | number | 否 | 被修剪前的帧高度. |
| destX | number | 否 | 用于显示的修剪框架的目的地 X 位置 。 |
| destY | number | 否 | 用于显示的修剪框的目的地 Y 位置 。 |
| destWidth | number | 否 | 用于显示的修剪框架的目的地宽度 。 |
| destHeight | number | 否 | 用于显示的修剪框架的目的地高度 。 |


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 此框架对象 。


> 源码：[src/textures/Frame.js#L445](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L445)  
引入版本：3.0.0


---

### setUVs {#setUVs}

#### \<instance> setUVs(width, height, u0, v0, u1, v1) {#instance-setuvswidth-height-u0-v0-u1-v1}


**说明:**

直接设置此帧的画布和WebGL UV数据.

如果您需要覆盖创建框架时自动生成的值, 请使用此选项 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 坎瓦斯数据这个框架的宽度. |
| height | number | 否 | 坎瓦斯数据显示这个框架的高度 。 |
| u0 | number | 否 | 紫外线u0值. |
| v0 | number | 否 | 紫外线v0值. |
| u1 | number | 否 | UV u1值 。 |
| v1 | number | 否 | 紫外线v1值. |


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 此框架对象 。


> 源码：[src/textures/Frame.js#L688](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L688)  
引入版本：3.50.0


---

### updateCropUVs {#updateCropUVs}

#### \<instance> updateCropUVs(crop, flipX, flipY) {#instance-updatecropuvscrop-flipx-flipy}


**说明:**

取一个裁剪数据对象,并根据裁剪对象的尺寸重新计算紫外线。由 `setFrame` 自动调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| crop | object | 否 | 裁剪数据对象。 这是 `GameObject._crop` 属性 。 |
| flipX | boolean | 否 | 父游戏对象是否设置了 flipX ? |
| flipY | boolean | 否 | 父游戏对象是否设置了 flipY ? |


**返回值:** object - 更新的作物数据对象.


> 源码：[src/textures/Frame.js#L670](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L670)  
引入版本：3.11.0


---

### updateUVs {#updateUVs}

#### \<instance> updateUVs() {#instance-updateuvs}


**说明:**

更新内部的 WebGL UV 缓存和 drawImage 缓存.


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 此框架对象 。


> 源码：[src/textures/Frame.js#L726](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L726)  
引入版本：3.0.0


---

### updateUVsInverted {#updateUVsInverted}

#### \<instance> updateUVsInverted() {#instance-updateuvsinverted}


**说明:**

更新内部的WebGL UV缓存以换取一个旋转的帧,将宽度和高度轴互换,这样紫外线坐标图就能够正确到纹理图集中旋转90度的帧.


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 此框架对象 。


> 源码：[src/textures/Frame.js#L762](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/Frame.js#L762)  
引入版本：3.0.0


---

---
