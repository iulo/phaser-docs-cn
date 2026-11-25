# ColorRamp {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/display-colorramp)

彩色Ramp 类代表一系列的色彩过渡。 它的用途是 QQSee Phaser.GameObjects.Gradient} 。

您应该确保您的带是排列到端的, 没有空隙。 渐变着色器假设这是 。 您可以在开始和结束时留下空隙 。 重叠和空白可能不会像预期的那样 。

默认情况下, ColorRamp 将数据存储在 GPU 上, 用于数据纹理。 创建时和运行 `setBands()` 时都会自动更新, 但如果您手动编辑带, 您应该运行 `encode()` 来重建纹理。 我们不会自动更新它, 因为我们不想浪费即将覆盖的重建周期 。

**构造函数**

`new ColorRamp(scene, bands, [gpuEncode])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 现场景. |
| bands | [Phaser.Types.Display.ColorBandConfig](/api/typedef/types-display#colorbandconfig) \| [Phaser.Display.ColorBand](/api/class/display-colorband) | Array.\<([Phaser.Types.Display.ColorBandConfig](/api/typedef/types-display#colorbandconfig) | [Phaser.Display.ColorBand](/api/class/display-colorband))> | 否 |  | 构成这个坡道的带。 这可以是一个条目或一个阵列, 也可以是配置或已有实例。 超过 1048576 的带数可能是不安全的 。 |
| gpuEncode | boolean | 是 | true | 是否创建数据纹理来使用阴影中的这个斜坡 。 |

---


**作用域**: static

> 源码：[src/display/ColorRamp.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L15)  
引入版本：4.0.0

## 公开成员 {#public-members}

### bands {#bands}

#### bands: Array.\<[Phaser.Display.ColorBand](/api/class/display-colorband)> {#bands-arrayphaserdisplaycolorband}


**说明:**

组成这个坡道的颜色带.


> 源码：[src/display/ColorRamp.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L56)  
引入版本：4.0.0


---

### bandTreeDepth {#bandTreeDepth}

#### bandTreeDepth: number {#bandtreedepth-number}


**说明:**

带状树中的关卡数。 内部用于解码数据纹理 。


> 源码：[src/display/ColorRamp.js#L112](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L112)  
引入版本：4.0.0


---

### dataTexture {#dataTexture}

#### dataTexture: [Phaser.Textures.Texture](/api/class/textures-texture) {#datatexture-phasertexturestexture}


**说明:**

Phaser 纹理将 GPU 数据纹理包在这个斜坡上。 它在 Scene 的纹理管理器中注册在 独有的密钥下, 因此可以在其它地方引用 。 它不是要显示的 。


> 源码：[src/display/ColorRamp.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L76)  
引入版本：4.0.0


---

### dataTextureFirstBand {#dataTextureFirstBand}

#### dataTextureFirstBand: number {#datatexturefirstband-number}


**说明:**

如果已编码, 则包含 `glTexture` 中第一个带状数据的 Texel 索引。 内部使用 。


> 源码：[src/display/ColorRamp.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L100)  
引入版本：4.0.0


---

### dataTextureResolution {#dataTextureResolution}

#### dataTextureResolution: Array.\<number> {#datatextureresolution-arraynumber}


**说明:**

如果已编码, 数据纹理的分辨率。 内部使用 。


> 源码：[src/display/ColorRamp.js#L123](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L123)  
引入版本：4.0.0


---

### glTexture {#glTexture}

#### glTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#gltexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

包含 GPU 编码的斜坡纹理。 内部通过诸如渐变游戏对象等效果来读取复杂的斜坡数据 。


> 源码：[src/display/ColorRamp.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L88)  
引入版本：4.0.0


---

### gpuEncode {#gpuEncode}

#### gpuEncode: boolean {#gpuencode-boolean}


**说明:**

是否将着色器用于 GPU 的斜坡编码。 已编码的斜坡被存储为纹理 。


> 源码：[src/display/ColorRamp.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L65)  
引入版本：4.0.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

彩色Ramp创建的场景.


> 源码：[src/display/ColorRamp.js#L46](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L46)  
引入版本：4.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁此 ColorRamp。 如果它有数据纹理, 请销毁它 。


> 源码：[src/display/ColorRamp.js#L497](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L497)  
引入版本：4.0.0


---

### encode {#encode}

#### \<instance> encode() {#instance-encode}


**说明:**

将颜色坡道带的数据纹理编码。

当 `gpuEncode` 启用, 带被设置或用 `setBands` 更新时, 此进程会自动运行。 如果您直接修改带, 您必须亲自调用 `encode` 。

数据以texels编码如下:

数字以"RG.BA"形式编码,数字等于R * 255 + G + B / 255 + A / 255 / 255.

- 前2特克塞尔:开始和结束.

  - 开始是第一个乐队的开始.

  - 结尾是最后一个乐队的结束.

- 下块的Texels:二进制对称的波段范围树,

  以中点波段的结束值表示。

- 最终块的特克塞尔,开始于`dataTextureFirstBand`:

  带状数据, 以 3 块表示 :

  - colorStart

  - colorEnd

  - colorSpace * 255 + 插值+(中/2)

二进制对称树将带状列表与每个节点分开一半。 它旨在快速找到与斜坡上某个特定进度相对应的带状。 例如, 带有10个带状的坡道会按此顺序存储端点 :

`[ 7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14 ]`

但是,由于它没有从指数10到上,它实际上:

`[ 7, 3, 9, 1, 5, 9, 9, 0, 2, 4, 6, 8, 9, 9, 9 ]`

请注意,如果改变坡道中的带数, `dataTexture` 可能不再有正确的分辨率, 并不打算显示 。


> 源码：[src/display/ColorRamp.js#L191](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L191)  
引入版本：4.0.0


---

### fixFit {#fixFit}

#### \<instance> fixFit(start, end, purgeZeroLength, encode) {#instance-fixfitstart-end-purgezerolength-encode}


**说明:**

修复此 ColorRamp 中的带的合位 。

这把每个乐段的开始时间设定到前一个乐段的结束,确保没有空白.

可选的,可以定义起始和结尾值,将斜坡拉伸到某些特定范围,例如0-1.

默认情况下,任何现在长度为0的带会被删除.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| start | number | 否 | 取代了第一个乐队的开始. |
| end | number | 否 | 覆盖上一个乐队的结束. |
| purgeZeroLength | boolean | 否 | 是否丢弃现在为 0 大小的带 。 |
| encode | boolean | 否 | 是否重新编码数据纹理 。 |


**返回值:** [Phaser.Display.ColorRamp](/api/class/display-colorramp) - - 这个彩色的Ramp实例。


> 源码：[src/display/ColorRamp.js#L324](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L324)  
引入版本：4.0.0


---

### getColor {#getColor}

#### \<instance> getColor(index) {#instance-getcolorindex}


**说明:**

获取该坡道内给定索引的颜色值 。

如果该位置没有带,颜色是透明的.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 颜色索引,从 0( 开始) 到 1( 结束) 。 |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) - 指数上的颜色。


> 源码：[src/display/ColorRamp.js#L462](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L462)  



---

### setBands {#setBands}

#### \<instance> setBands(bands, [encode]) {#instance-setbandsbands-encode}


**说明:**

设置或替换此斜坡中的颜色带。 创建后使用此功能更新这些带 。

如果 `gpuEncode` 设定为 `encode` 而非 `false` , 这将重新编码数据纹理 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| bands | [Phaser.Types.Display.ColorBandConfig](/api/typedef/types-display#colorbandconfig) \| [Phaser.Display.ColorBand](/api/class/display-colorband) | Array.\<([Phaser.Types.Display.ColorBandConfig](/api/typedef/types-display#colorbandconfig) | [Phaser.Display.ColorBand](/api/class/display-colorband))> | 否 |  | 构成这个斜坡的带。 这可以是一个条目或一个阵列, 也可以是配置或已有实例 。 |
| encode | boolean | 是 | true | 是否将新坡道数据编码为数据纹理, 以用于阴影 。 |


**返回值:** [Phaser.Display.ColorRamp](/api/class/display-colorramp) - - 这个彩色的Ramp实例。


> 源码：[src/display/ColorRamp.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L137)  
引入版本：4.0.0


---

### splitBand {#splitBand}

#### \<instance> splitBand(band, steps, [quantize], [encode]) {#instance-splitbandband-steps-quantize-encode}


**说明:**

从这个斜坡上将一个带分成几个带,然后插入斜坡.

你可以选择是否"量化"乐队,其中每个乐队都有平淡的颜色.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| band | number \| [Phaser.Display.ColorBand](/api/class/display-colorband) | 否 |  | 乐队要分裂, 要么在这个坡道上 , 要么就是这个带子实例。 乐队必须在这个坡道上 。 |
| steps | number | 否 |  | 要创建的乐队数量 。 |
| quantize | boolean | 是 | false | 是否将带子量化为单一颜色 。 |
| encode | boolean | 是 | true | 是否重建数据纹理 。 |


**返回值:** [Phaser.Display.ColorRamp](/api/class/display-colorramp) - 此颜色朗普实例 。


> 源码：[src/display/ColorRamp.js#L387](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/ColorRamp.js#L387)  
引入版本：4.0.0


---

---
