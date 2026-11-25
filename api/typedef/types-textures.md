# Types.Textures {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-textures)

## CaptureConfig {#captureconfig}

### \<static> CaptureConfig {#static-captureconfig}


`DynamicTexture.capture`方法的配置对象.

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| transform | 'local' \| 'world' | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | "'world'" | 应用其他配置设置后使用的转换 。 “ 本地” 使用 Game Object 的属性 。 “ 世界” 使用 GameObject 的 `parentContainer` 值计算世界位置 。 也可以提供 `TransformMatrix`, 直接使用 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 |  | 将游戏对象渲染成动态图时使用的相机。 如果没有指定, 请使用动态图自己的相机 。 |
| x | number | 是 |  | ××位置. |
| y | number | 是 |  | 位置是Y的,你应该知道 |
| alpha | number | 是 |  | 阿尔法值. |
| tint | number | 是 |  | 颜色值,只有WebGL |
| angle | number | 是 |  | 角度为度。旋转围绕其起源进行。 如果 `angle` 是非零, 则忽略 `rotation` 。 |
| rotation | number | 是 |  | 弧度旋转,旋转围绕其起源进行. |
| scale | number | 是 |  | 设置水平和垂直尺度,并有一个单一的值。 |
| scaleX | number | 是 |  | 设置水平比例尺。如果提供了比例尺属性,则覆盖该属性。 |
| scaleY | number | 是 |  | 设置垂直比例。如果提供了比例尺属性,则覆盖该属性。 |
| originX | number | 是 |  | 水平源. 0为左,0.5为中,1为右. |
| originY | number | 是 |  | 垂直起源. 0为上部,0.5为中部,1为下部. |
| blendMode | string \| [Phaser.BlendModes](/api/namespace/blendmodes) | number | 是 |  | 绘图时使用的混合模式 。 |

**类型**: object

**Member of**: Phaser.Types.Textures
> 源码：[src/textures/typedefs/CaptureConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/typedefs/CaptureConfig.js#L1)  
引入版本：4.0.0

---

## CompressedTextureData {#compressedtexturedata}

### \<static> CompressedTextureData {#static-compressedtexturedata}


包含压缩纹理的尺寸和 mipmap 数据的对象。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| compressed | boolean | 否 | 这是压缩的纹理吗? |
| generateMipmap | boolean | 否 | 是否该由这个纹理产生? |
| width | number | 否 | 纹理最大尺寸的宽度 。 |
| height | number | 否 | 纹理最大尺寸的高度. |
| internalFormat | GLenum | 否 | WebGL内部纹理格式. |
| mipmaps | Array.\<[Phaser.Types.Textures.MipmapType](/api/typedef/types-textures#mipmaptype)> | 否 | 一组 MipmapType 对象。 |

**类型**: object

**Member of**: Phaser.Types.Textures
> 源码：[src/textures/typedefs/CompressedTextureData.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/typedefs/CompressedTextureData.js#L1)  
引入版本：3.60.0

---

## MipmapType {#mipmaptype}

### \<static> MipmapType {#static-mipmaptype}


压缩纹理的 Mipmap 数据条目。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | mipmap的这一关宽. |
| height | number | 否 | 的这个水平的高度. |
| data | Uint8Array | 否 | 解码的像素数据. |

**类型**: object

**Member of**: Phaser.Types.Textures
> 源码：[src/textures/typedefs/MipmapType.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/typedefs/MipmapType.js#L1)  
引入版本：3.60.0

---

## PixelConfig {#pixelconfig}

### \<static> PixelConfig {#static-pixelconfig}


包含 CanvasTexture 中单个像素位置和颜色数据的对象。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 象素的x坐标. |
| y | number | 否 | 象素的y坐标. |
| color | number | 否 | 像素的颜色,不包括α通道. |
| alpha | number | 否 | 象素的α,在0到1之间. |

**类型**: object

**Member of**: Phaser.Types.Textures
> 源码：[src/textures/typedefs/PixelConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/typedefs/PixelConfig.js#L1)  
引入版本：3.16.0

---

## RepeatConfig {#repeatconfig}

### \<static> RepeatConfig {#static-repeatconfig}


`DynamicTexture.repeat`方法的配置选项.

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tilePositionX | number | 是 | 0 | 纹理的横向滚动位置 。 |
| tilePositionY | number | 是 | 0 | 纹理的垂直滚动位置 。 |
| tileRotation | number | 是 | 0 | 纹理的旋转. |
| tileScaleX | number | 是 | 1 | 纹理的横向尺度. |
| tileScaleY | number | 是 | 1 | 纹理的垂直尺度. |

**类型**: object

**Member of**: Phaser.Types.Textures
> 源码：[src/textures/typedefs/RepeatConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/typedefs/RepeatConfig.js#L1)  
引入版本：4.0.0

---

## SpriteSheetConfig {#spritesheetconfig}

### \<static> SpriteSheetConfig {#static-spritesheetconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| frameWidth | number | 否 |  | 每个帧的固定宽度. |
| frameHeight | number | 是 |  | 每个帧的固定高度。 如果不设定, 则会使用 frameWidth 来作为高度 。 |
| startFrame | number | 是 | 0 | 跳过多个框架。 当一个纹理中存在多个图案工作表时有用 。 |
| endFrame | number | 是 | -1 | 从Sprite工作表提取的框架总数。 -1 的默认值表示“ 提取全部框架 ”。 |
| margin | number | 是 | 0 | 如果框架已绘制了边距, 请在此指定金额 。 |
| spacing | number | 是 | 0 | 如果画框之间有间隔,请在此指定金额。 |

**类型**: object

**Member of**: Phaser.Types.Textures
> 源码：[src/textures/typedefs/SpriteSheetConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/typedefs/SpriteSheetConfig.js#L1)  
引入版本：3.0.0

---

## SpriteSheetFromAtlasConfig {#spritesheetfromatlasconfig}

### \<static> SpriteSheetFromAtlasConfig {#static-spritesheetfromatlasconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| atlas | string | 否 |  | 用于找到此 Sprite 工作表的纹理图集的密钥 。 |
| frame | string | 否 |  | 用于找到此 Sprite 工作表的纹理图集框架的密钥 。 |
| frameWidth | number | 否 |  | 每个帧的固定宽度. |
| frameHeight | number | 是 |  | 每个帧的固定高度。 如果不设定, 则会使用 frameWidth 来作为高度 。 |
| startFrame | number | 是 | 0 | 跳过多个框架。 当一个纹理中存在多个图案工作表时有用 。 |
| endFrame | number | 是 | -1 | 从Sprite工作表提取的框架总数。 -1 的默认值表示“ 提取全部框架 ”。 |
| margin | number | 是 | 0 | 如果框架已绘制了边距, 请在此指定金额 。 |
| spacing | number | 是 | 0 | 如果画框之间有间隔,请在此指定金额。 |

**类型**: object

**Member of**: Phaser.Types.Textures
> 源码：[src/textures/typedefs/SpriteSheetFromAtlasConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/typedefs/SpriteSheetFromAtlasConfig.js#L1)  
引入版本：3.0.0

---

## StampConfig {#stampconfig}

### \<static> StampConfig {#static-stampconfig}


`DynamicTexture.stamp`方法的配置对象.

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| alpha | number | 是 | 1 | 邮票所用的α值 。 |
| tint | number | 是 | "0xffffff" | 印章所用的颜色值。 WebGL 仅此而已 。 |
| angle | number | 是 | 0 | 印章角度以度为单位,旋转围绕其起源进行。如果 `angle`是非零,则忽略 `rotation` 。 |
| rotation | number | 是 | 0 | 邮票的旋转用弧度表示,旋转围绕其起源进行. |
| scale | number | 是 | 1 | 设置印章的横向和纵向比例,并设定一个值。 |
| scaleX | number | 是 | 1 | 设置章的横向比例。如果提供了,则覆盖比例尺属性。 |
| scaleY | number | 是 | 1 | 设置印章的垂直比例。如果提供了,则覆盖比例尺属性。 |
| originX | number | 是 | 0.5 | 章的横向起源. 0为左,0.5为中,1为右. |
| originY | number | 是 | 0.5 | 印章的垂直起源. 0为上部,0.5为中部,1为下部. |
| blendMode | string \| [Phaser.BlendModes](/api/namespace/blendmodes) | number | 是 | 0 | 绘制邮票时使用的混合模式。 默认为 0( 正常) 。 |

**类型**: object

**Member of**: Phaser.Types.Textures
> 源码：[src/textures/typedefs/StampConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/typedefs/StampConfig.js#L1)  
引入版本：3.60.0

---

## TextureSource {#texturesource}

### \<static> TextureSource {#static-texturesource}

**类型**: HTMLImageElement | HTMLCanvasElement | HTMLVideoElement | [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | [Phaser.Types.Textures.CompressedTextureData](/api/typedef/types-textures#compressedtexturedata) | [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) | Uint8Array

**Member of**: Phaser.Types.Textures
> 源码：[src/textures/typedefs/TextureSource.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/typedefs/TextureSource.js#L1)  
引入版本：4.0.0

---

## TextureSourceElement {#texturesourceelement}

### \<static> TextureSourceElement {#static-texturesourceelement}

**类型**: HTMLImageElement | HTMLCanvasElement | HTMLVideoElement

**Member of**: Phaser.Types.Textures
> 源码：[src/textures/typedefs/TextureSourceElement.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/typedefs/TextureSourceElement.js#L1)  
引入版本：4.0.0

---

---
