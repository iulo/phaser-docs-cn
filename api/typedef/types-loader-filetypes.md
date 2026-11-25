# Types.Loader.FileTypes {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-loader-filetypes)

## AsepriteFileConfig {#asepritefileconfig}

### \<static> AsepriteFileConfig {#static-asepritefileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和纹理管理器中独有 。 |
| textureURL | string | 是 |  | 绝对或相对的URL可以从中加载纹理图像文件. |
| textureExtension | string | 是 | "'png'" | 如果没有提供 URL , 用于图像纹理的默认文件扩展名 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 特为纹理图像文件设置额外的 XHR 设置 。 |
| atlasURL | object \| string | 是 |  | 绝对或相对的 URL 来从地图集 json 文件装入。 或者, 一个 已经形成好的 JSON 对象来代替它 。 |
| atlasExtension | string | 是 | "'json'" | 如果没有提供url, 则默认文件扩展名将用于地图集 json 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 特别为地图集json文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/AsepriteFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/AsepriteFileConfig.js#L1)  


---

## AtlasJSONFileConfig {#atlasjsonfileconfig}

### \<static> AtlasJSONFileConfig {#static-atlasjsonfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和纹理管理器中独有 。 |
| textureURL | string | 是 |  | 绝对或相对的URL可以从中加载纹理图像文件. |
| textureExtension | string | 是 | "'png'" | 如果没有提供 URL , 用于图像纹理的默认文件扩展名 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 特为纹理图像文件设置额外的 XHR 设置 。 |
| normalMap | string | 是 |  | 关联的普通地图的文件名。 它使用相同的路径和 URL 来装入纹理图像 。 |
| atlasURL | object \| string | 是 |  | 绝对或相对的 URL 来从地图集 json 文件装入。 或者, 一个 已经形成好的 JSON 对象来代替它 。 |
| atlasExtension | string | 是 | "'json'" | 如果没有提供url, 则默认文件扩展名将用于地图集 json 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 特别为地图集json文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/AtlasJSONFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/AtlasJSONFileConfig.js#L1)  


---

## AtlasXMLFileConfig {#atlasxmlfileconfig}

### \<static> AtlasXMLFileConfig {#static-atlasxmlfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和纹理管理器中独有 。 |
| textureURL | string | 是 |  | 绝对或相对的URL可以从中加载纹理图像文件. |
| textureExtension | string | 是 | "'png'" | 如果没有提供 URL , 用于图像纹理的默认文件扩展名 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 特为纹理图像文件设置额外的 XHR 设置 。 |
| normalMap | string | 是 |  | 关联的普通地图的文件名。 它使用相同的路径和 URL 来装入纹理图像 。 |
| atlasURL | string | 是 |  | 装入地图集 xml 文件的绝对或相对 URL 。 |
| atlasExtension | string | 是 | "'xml'" | 如果没有提供url,则用于地图集 xml 的默认文件扩展名 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为地图集xml文件设置额外的 XHR 设置. |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/AtlasXMLFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/AtlasXMLFileConfig.js#L1)  


---

## AudioFileConfig {#audiofileconfig}

### \<static> AudioFileConfig {#static-audiofileconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 文件的键。 必须在资源加载器和音频缓存中独有 。 |
| url | string \| Array.\<string> | [Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig) | Array.\<[Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig)> | 是 | 绝对或相对的URL来从中加载音频文件. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |
| context | AudioContext | 是 | 此文件将用来自行处理的可选音频 Context 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/AudioFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/AudioFileConfig.js#L1)  


---

## AudioFileURLConfig {#audiofileurlconfig}

### \<static> AudioFileURLConfig {#static-audiofileurlconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 类型 | string | 否 | 音频文件格式。 请在 QQlink Phaser.Device.Audio} 中看到属性名称 。 |
| url | string | 否 | 音频文件的绝对或相对的 URL 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/AudioFileURLConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/AudioFileURLConfig.js#L1)  


---

## AudioSpriteFileConfig {#audiospritefileconfig}

### \<static> AudioSpriteFileConfig {#static-audiospritefileconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 文件的键。 必须在资源加载器和音频缓存中独有 。 |
| jsonURL | string | 否 | 绝对或相对的 URL 来从 json 文件装入。 或者一个 良好形成的 JSON 对象来代替 。 |
| jsonXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 特别为 json 文件设置额外的 XHR 设置 。 |
| audioURL | Object | 是 | 绝对或相对的URL来从音频文件加载. |
| audioConfig | any | 是 | 音频配置选项 。 |
| audioXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 音频文件的额外 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/AudioSpriteFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/AudioSpriteFileConfig.js#L1)  


---

## BinaryFileConfig {#binaryfileconfig}

### \<static> BinaryFileConfig {#static-binaryfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在加载器和二进制缓存中独有 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'bin'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |
| dataType | any | 是 |  | 可选类型将二进制文件投放到一次装入。 例如, `Uint8Array` 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/BinaryFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/BinaryFileConfig.js#L1)  


---

## BitmapFontFileConfig {#bitmapfontfileconfig}

### \<static> BitmapFontFileConfig {#static-bitmapfontfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和纹理管理器中独有 。 |
| textureURL | string | 是 |  | 绝对或相对的URL可以从中加载纹理图像文件. |
| textureExtension | string | 是 | "'png'" | 如果没有提供 URL , 用于图像纹理的默认文件扩展名 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 特为纹理图像文件设置额外的 XHR 设置 。 |
| normalMap | string | 是 |  | 关联的普通地图的文件名。 它使用相同的路径和 URL 来装入纹理图像 。 |
| fontDataURL | string | 是 |  | 绝对或相对的URL来装入字体数据 xml 文件. |
| fontDataExtension | string | 是 | "'xml'" | 如果没有提供url,则用于字体数据xml的默认文件扩展名. |
| fontDataXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为字体数据xml文件设置额外的 XHR 设置. |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/BitmapFontFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/BitmapFontFileConfig.js#L1)  


---

## CompressedTextureFileEntry {#compressedtexturefileentry}

### \<static> CompressedTextureFileEntry {#static-compressedtexturefileentry}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| format | string | 是 | 浏览器必须支持的纹理压缩基础格式才能加载此文件。可以是“ ETC” 、 “ ETC1” 、 “ ATC” 、 “ ASTC” 、 “ BPTC” 、 “ RGTC” 、“ PVRTC” 、 “ S3TC” 、 ” S3TCSRGB ” 或 “ IMG” 的倒置格式 。 |
| 类型 | string | 是 | 容器格式, PVR 或 KTX。 如果不给它, 将尝试从 textureURL 扩展中提取 。 |
| textureURL | string | 是 | 要加载的压缩纹理文件的 URL 。 |
| atlasURL | string | 是 | 纹理图集 JSON 数据文件的可选 URL。 如果不给出, 纹理将被装入到单个图像中 。 |
| multiAtlasURL | string | 是 | 由Texture Packer Pro创建的多文本地图集JSON数据文件的可选 URL. |
| multiPath | string | 是 | 装入多图集数据中定义的纹理时可选用的路径 。 |
| multiBaseURL | string | 是 | 添加多图集数据中定义的纹理时使用的可选基址 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/CompressedTextureFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/CompressedTextureFileConfig.js#L1)  


---

## CompressedTextureFileConfig {#compressedtexturefileconfig}

### \<static> CompressedTextureFileConfig {#static-compressedtexturefileconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ETC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 | ETC格式纹理的字符串,或文件条目对象. |
| ETC1 | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 | ETC1格式纹理的字符串,或文件条目对象. |
| ATC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 | ATC格式纹理的字符串,或文件条目对象. |
| ASTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 | 字符串,或文件条目对象,用于一个 ASTC 格式的纹理. |
| BPTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 | 字符串,或文件条目对象,用于BPTC格式纹理. |
| RGTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 | 用于 RGTC 格式纹理的字符串,或文件条目对象. |
| PVRTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 | 光电图格式纹理的字符串,或文件条目对象。 |
| S3TC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 | 用于S3TC格式纹理的字符串,或文件条目对象. |
| S3TCSRGB | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 | 用于S3TCSRGB格式纹理的字符串,或文件条目对象. |
| IMG | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 | 倒置图像文件的字符串,或文件条目对象. |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/CompressedTextureFileConfig.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/CompressedTextureFileConfig.js#L13)  


---

## CSSFileConfig {#cssfileconfig}

### \<static> CSSFileConfig {#static-cssfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器内独有 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'css'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/CSSFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/CSSFileConfig.js#L1)  


---

## FontFileConfig {#fontfileconfig}

### \<static> FontFileConfig {#static-fontfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器内独有 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'ttf'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| format | string | 是 | "'truetype'" | 字体类型。 应该是字符串, 如“ truetype ” 或“ opentype ” 。 |
| descriptors | object | 是 |  | 含有字体面部字体描述符的可选对象。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/FontFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/FontFileConfig.js#L1)  


---

## GLSLFileConfig {#glslfileconfig}

### \<static> GLSLFileConfig {#static-glslfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和文本缓存中都具有独有性 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'glsl'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/GLSLFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/GLSLFileConfig.js#L1)  


---

## HTMLFileConfig {#htmlfileconfig}

### \<static> HTMLFileConfig {#static-htmlfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和文本缓存中都具有独有性 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'html'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/HTMLFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/HTMLFileConfig.js#L1)  


---

## HTMLTextureFileConfig {#htmltexturefileconfig}

### \<static> HTMLTextureFileConfig {#static-htmltexturefileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和纹理管理器中独有 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'html'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |
| width | number | 是 | 512 | HTML 的纹理宽度将被渲染到 。 |
| height | number | 是 | 512 | HTML 的纹理高度将被渲染到 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/HTMLTextureFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/HTMLTextureFileConfig.js#L1)  


---

## ImageFileConfig {#imagefileconfig}

### \<static> ImageFileConfig {#static-imagefileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和纹理管理器中独有 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'png'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| normalMap | string | 是 |  | 关联的普通地图的文件名。 它使用相同的路径和url来装入图像 。 |
| frameConfig | [Phaser.Types.Loader.FileTypes.ImageFrameConfig](/api/typedef/types-loader-filetypes#imageframeconfig) | 是 |  | 框架配置对象。 只提供和用于精灵表 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/ImageFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/ImageFileConfig.js#L1)  


---

## ImageFrameConfig {#imageframeconfig}

### \<static> ImageFrameConfig {#static-imageframeconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| frameWidth | number | 否 |  | 框架的宽度, 以像素为单位 。 |
| frameHeight | number | 是 |  | 框架的高度以像素表示。 如果不提供 `frameWidth` 值, 请使用 。 |
| startFrame | number | 是 | 0 | 第一个开始解析的帧 。 |
| endFrame | number | 是 |  | 停止解析的框。 如果不提供, 它将根据图像和框尺寸计算值 。 |
| margin | number | 是 | 0 | 图像中的边距。 这是框边缘的空间 。 |
| spacing | number | 是 | 0 | 图像中每个框架之间的间隔。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/ImageFrameConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/ImageFrameConfig.js#L1)  


---

## JSONFileConfig {#jsonfileconfig}

### \<static> JSONFileConfig {#static-jsonfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和 JSON 缓存中独有 。 |
| url | string \| any | 是 |  | 从文件装入的绝对或相对 URL。 或者可以是已准备好的 JSON 对象, 这样它会直接添加到缓存中 。 |
| extension | string | 是 | "'json'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| dataKey | string | 是 |  | 如果指定了而不是正在解析并添加到缓存中的全部 JSON 文件, 则只添加与此属性键相对应的段落。 如果您想要提取的属性是嵌入的, 请使用时段分割它 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/JSONFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/JSONFileConfig.js#L1)  


---

## MultiAtlasFileConfig {#multiatlasfileconfig}

### \<static> MultiAtlasFileConfig {#static-multiatlasfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和纹理管理器中独有 。 |
| atlasURL | string | 是 |  | 绝对或相对的 URL 来从多图集 json 文件加载。 或者, 一个 已经形成好的 JSON 对象 。 |
| url | string | 是 |  | 用于“ atlasURL” 的别名。 如果给定, 它将覆盖“ atlasURL” 中设置的任意内容 。 |
| atlasExtension | string | 是 | "'json'" | 如果没有提供url, 则默认文件扩展名将用于地图集 json 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 特别为地图集json文件设置额外的 XHR 设置 。 |
| path | string | 是 |  | 装入地图集数据中定义的纹理时可选使用路径 。 |
| baseURL | string | 是 |  | 装入地图集数据中定义的纹理时使用的可选基址 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 特为纹理文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/MultiAtlasFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/MultiAtlasFileConfig.js#L1)  


---

## MultiScriptFileConfig {#multiscriptfileconfig}

### \<static> MultiScriptFileConfig {#static-multiscriptfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器内独有 。 |
| url | Array.\<string> | 是 |  | 一组绝对或相对的 URL 来从中加载脚本文件。它们按数组中给出的顺序处理 。 |
| extension | string | 是 | "'js'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为这些文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/MultiScriptFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/MultiScriptFileConfig.js#L1)  


---

## OBJFileConfig {#objfileconfig}

### \<static> OBJFileConfig {#static-objfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和 OBJ 快取器中独有 。 |
| url | string | 是 |  | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 它将被设定为 `<key>.obj`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. obj" 。 |
| extension | string | 是 | "'obj'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| flipUV | boolean | 是 |  | 翻转模型数据中存储的紫外线坐标? |
| matURL | string | 是 |  | 对象材料文件的可选绝对或相对的 URL。 如果未定义或 `null` , 则不会装入材料文件 。 |
| matExtension | string | 是 | "'mat'" | 如果没有提供url,则使用默认的材料文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/OBJFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/OBJFileConfig.js#L1)  


---

## PackFileConfig {#packfileconfig}

### \<static> PackFileConfig {#static-packfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和 JSON 缓存中独有 。 |
| url | string \| any | 是 |  | 装入文件的绝对或相对 URL。 或者可以是已准备好的 JSON 对象, 届时将直接处理 。 |
| extension | string | 是 | "'json'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| dataKey | string | 是 |  | 如果指定了而不是正在解析的整个 JSON 文件, 则只添加与此属性键对应的段落。 如果您想要提取的属性是嵌入的, 请使用时段来分割它 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/PackFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/PackFileConfig.js#L1)  


---

## PackFileSection {#packfilesection}

### \<static> PackFileSection {#static-packfilesection}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| files | Array.\<[Phaser.Types.Loader.FileConfig](/api/typedef/types-loader#fileconfig)> | 否 | 装入的文件。 请见 QQLink Phaser.Types.Loader.FileTypes} |
| baseURL | string | 是 | 用于解析 `files` 路径的 URL。 例如 : “ http://labs.phaser.io/assets/'. ” |
| defaultType | string | 是 | 默认的QQLINK Phaser.Types.Loader.FileConfig}`type`. |
| path | string | 是 | 用于解析 `files` 中相对路径的 URL 路径。 例如 : “ 图像/ 粘贴 / ” 。 |
| prefix | string | 是 | 自动为每个文件键准备的可选前缀 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/PackFileSection.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/PackFileSection.js#L1)  


---

## PCTAtlasFileConfig {#pctatlasfileconfig}

### \<static> PCTAtlasFileConfig {#static-pctatlasfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和纹理管理器中独有 。 |
| atlasURL | string | 是 |  | 从 PCT 地图集数据文件装入的绝对或相对 URL 。 |
| url | string | 是 |  | 用于“ atlasURL” 的别名。 如果给定, 它将覆盖“ atlasURL” 中设置的任意内容 。 |
| atlasExtension | string | 是 | "'pct'" | 如果没有提供 URL 数据, 则默认文件扩展名 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 特别为地图集json文件设置额外的 XHR 设置 。 |
| path | string | 是 |  | 装入地图集数据中定义的纹理时可选使用路径 。 |
| baseURL | string | 是 |  | 装入地图集数据中定义的纹理时使用的可选基址 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 特为纹理文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/PCTAtlasFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/PCTAtlasFileConfig.js#L1)  


---

## PluginFileConfig {#pluginfileconfig}

### \<static> PluginFileConfig {#static-pluginfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器内独有 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'js'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| start | boolean | 是 | false | 装入后自动启动插件吗 ? |
| mapping | string | 是 |  | 如果要将此插件注入到场景中, 这就是所用的属性键 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/PluginFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/PluginFileConfig.js#L1)  


---

## SceneFileConfig {#scenefileconfig}

### \<static> SceneFileConfig {#static-scenefileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和文本缓存中都具有独有性 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'js'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/SceneFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/SceneFileConfig.js#L1)  


---

## ScenePluginFileConfig {#scenepluginfileconfig}

### \<static> ScenePluginFileConfig {#static-scenepluginfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器内独有 。 |
| url | string \| function | 是 |  | 绝对或相对的 URL 来从文件加载。 或者, 场景插件 。 |
| extension | string | 是 | "'js'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| systemKey | string | 是 |  | 如果要将此插件添加到 Scene.Systems 中, 此插件的属性键 。 |
| sceneKey | string | 是 |  | 如果要将此插件添加到场景中, 这是它属性的键 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/ScenePluginFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/ScenePluginFileConfig.js#L1)  


---

## ScriptFileConfig {#scriptfileconfig}

### \<static> ScriptFileConfig {#static-scriptfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器内独有 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'js'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| 类型 | string | 是 | "'script'" | 脚本类型。 如果文件包含导出模块, 则应该为经典 JavaScript 的“ 标语 ” , 或“ 模块 ” 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/ScriptFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/ScriptFileConfig.js#L1)  


---

## SpriteSheetFileConfig {#spritesheetfileconfig}

### \<static> SpriteSheetFileConfig {#static-spritesheetfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和纹理管理器中独有 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'png'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| normalMap | string | 是 |  | 关联的普通地图的文件名。 它使用相同的路径和url来装入图像 。 |
| frameConfig | [Phaser.Types.Loader.FileTypes.ImageFrameConfig](/api/typedef/types-loader-filetypes#imageframeconfig) | 是 |  | 帧配置对象. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/SpriteSheetFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/SpriteSheetFileConfig.js#L1)  


---

## SVGFileConfig {#svgfileconfig}

### \<static> SVGFileConfig {#static-svgfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和纹理管理器中独有 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'svg'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |
| svgConfig | [Phaser.Types.Loader.FileTypes.SVGSizeConfig](/api/typedef/types-loader-filetypes#svgsizeconfig) | 是 |  | svg 大小配置对象 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/SVGFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/SVGFileConfig.js#L1)  


---

## SVGSizeConfig {#svgsizeconfig}

### \<static> SVGSizeConfig {#static-svgsizeconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 是 | 一个可选的宽度。 SVG 会在被渲染成纹理之前调整到这个大小 。 |
| height | number | 是 | 可选的高度。 SVG 会在被渲染成纹理之前调整到这个大小 。 |
| scale | number | 是 | 可选的缩放。 如果它覆盖了宽度/ 高度属性。 SVG 在被渲染为纹理之前, 会被缩放为缩放因子 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/SVGSizeConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/SVGSizeConfig.js#L1)  


---

## TextFileConfig {#textfileconfig}

### \<static> TextFileConfig {#static-textfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和文本缓存中都具有独有性 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'txt'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/TextFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/TextFileConfig.js#L1)  


---

## TilemapCSVFileConfig {#tilemapcsvfileconfig}

### \<static> TilemapCSVFileConfig {#static-tilemapcsvfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和 Tilemap 缓存中独有 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'csv'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/TilemapCSVFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/TilemapCSVFileConfig.js#L1)  


---

## TilemapImpactFileConfig {#tilemapimpactfileconfig}

### \<static> TilemapImpactFileConfig {#static-tilemapimpactfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和 Tilemap 缓存中独有 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'json'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/TilemapImpactFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/TilemapImpactFileConfig.js#L1)  


---

## TilemapJSONFileConfig {#tilemapjsonfileconfig}

### \<static> TilemapJSONFileConfig {#static-tilemapjsonfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和 Tilemap 缓存中独有 。 |
| url | object \| string | 是 |  | 绝对或相对的 URL 来从文件加载。 或者, 一个 已经形成好的 JSON 对象 。 |
| extension | string | 是 | "'json'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/TilemapJSONFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/TilemapJSONFileConfig.js#L1)  


---

## UnityAtlasFileConfig {#unityatlasfileconfig}

### \<static> UnityAtlasFileConfig {#static-unityatlasfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和纹理管理器中独有 。 |
| textureURL | string | 是 |  | 绝对或相对的URL可以从中加载纹理图像文件. |
| textureExtension | string | 是 | "'png'" | 如果没有提供 URL , 用于图像纹理的默认文件扩展名 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 特为纹理图像文件设置额外的 XHR 设置 。 |
| normalMap | string | 是 |  | 关联的普通地图的文件名。 它使用相同的路径和 URL 来装入纹理图像 。 |
| atlasURL | string | 是 |  | 绝对或相对的URL来加载地图集数据文件. |
| atlasExtension | string | 是 | "'txt'" | 如果没有提供 URL 数据, 则默认文件扩展名 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为地图集数据文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/UnityAtlasFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/UnityAtlasFileConfig.js#L1)  


---

## VideoFileConfig {#videofileconfig}

### \<static> VideoFileConfig {#static-videofileconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.VideoFileConfig](/api/typedef/types-loader-filetypes#videofileconfig) | 否 | 此文件使用的键, 或文件配置对象 。 |
| url | string \| Array.\<string> | [Phaser.Types.Loader.FileTypes.VideoFileURLConfig](/api/typedef/types-loader-filetypes#videofileurlconfig) | Array.\<[Phaser.Types.Loader.FileTypes.VideoFileURLConfig](/api/typedef/types-loader-filetypes#videofileurlconfig)> | 是 | 绝对或相对的URL从中加载视频文件. |
| noAudio | boolean | 是 | 视频是否有音频音轨? 如果您不能, 您可以启用自动播放 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/VideoFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/VideoFileConfig.js#L1)  


---

## VideoFileURLConfig {#videofileurlconfig}

### \<static> VideoFileURLConfig {#static-videofileurlconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 类型 | string | 否 | 视频文件格式。 请在 QQlink Phaser.Device.Video} 中看到属性名称 。 |
| url | string | 否 | 视频文件的绝对或相对的URL. |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/VideoFileURLConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/VideoFileURLConfig.js#L1)  


---

## XMLFileConfig {#xmlfileconfig}

### \<static> XMLFileConfig {#static-xmlfileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 文件的键。 必须在资源加载器和文本缓存中都具有独有性 。 |
| url | string | 是 |  | 要从文件中装入文件的绝对或相对的 URL 。 |
| extension | string | 是 | "'xml'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

**类型**: object

**所属**: Phaser.Types.Loader.FileTypes
> 源码：[src/loader/filetypes/typedefs/XMLFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/typedefs/XMLFileConfig.js#L1)  


---

---
