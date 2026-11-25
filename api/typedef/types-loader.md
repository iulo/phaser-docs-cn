# Types.Loader {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-loader)

## FileConfig {#fileconfig}

### \<static> FileConfig {#static-fileconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 类型 | string | 否 |  | 装入此文件的加载器方法的名称, 例如“ 图像 ” 、 “ json ” 、 “ 拼写表 ” 。 |
| cache | [Phaser.Cache.BaseCache](/api/class/cache-basecache) \| false | 否 |  | 引用此文件类型的缓存实例。 如果您不需要从游戏中获取文件, 则引用错误; 例如: 浏览器跟踪的字体文件 。 |
| key | string | 否 |  | 独有缓存键( 其文件类型中独一无二) |
| url | object \| string | 是 |  | 文件的URL,不包括baseURL. |
| path | string | 是 |  | 文件的路径,不包括baseURL. |
| extension | string | 是 |  | 此文件使用的默认扩展名 。 |
| responseType | XMLHttpRequestResponseType | 是 |  | XHR请求使用的responseType. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) \| false | 是 | false | 自定义此文件的 XHR 设置, 并与加载器默认合并 。 |
| config | any | 是 |  | 一个配置对象,可以被文件类型用来存储过渡数据. |
| textureURL | string | 是 |  | 绝对或相对的URL可以从中加载纹理图像文件. |
| textureExtension | string | 是 | "'png'" | 如果没有提供 URL , 用于图像纹理的默认文件扩展名 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 特为纹理图像文件设置额外的 XHR 设置 。 |
| atlasURL | object \| string | 是 |  | 绝对或相对的 URL 来从地图集 json 文件装入。 或者, 一个 已经形成好的 JSON 对象来代替它 。 |
| atlasExtension | string | 是 | "'json'" | 如果没有提供url, 则默认文件扩展名将用于地图集 json 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 特别为地图集json文件设置额外的 XHR 设置 。 |
| normalMap | string | 是 |  | 关联的普通地图的文件名。 它使用相同的路径和 URL 来装入纹理图像 。 |
| context | AudioContext | 是 |  | 此文件将使用可选的音频Context来自行处理( 仅用于声音对象) 。 |
| jsonURL | string | 是 |  | 绝对或相对的 URL 来从 json 文件装入。 或者一个 良好形成的 JSON 对象来代替 。 |
| jsonXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 特别为 json 文件设置额外的 XHR 设置 。 |
| audioURL | Object | 是 |  | 绝对或相对的URL来从音频文件加载. |
| audioConfig | any | 是 |  | 音频配置选项 。 |
| audioXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 音频文件的额外 XHR 设置 。 |
| dataType | any | 是 |  | 可选类型将二进制文件投放到一次装入。 例如, `Uint8Array` 。 |
| fontDataURL | string | 是 |  | 绝对或相对的URL来装入字体数据 xml 文件. |
| fontDataExtension | string | 是 | "'xml'" | 如果没有提供url,则用于字体数据xml的默认文件扩展名. |
| fontDataXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为字体数据xml文件设置额外的 XHR 设置. |
| ETC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 |  | ETC格式纹理的字符串,或文件条目对象. |
| ETC1 | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 |  | ETC1格式纹理的字符串,或文件条目对象. |
| ATC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 |  | ATC格式纹理的字符串,或文件条目对象. |
| ASTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 |  | 字符串,或文件条目对象,用于一个 ASTC 格式的纹理. |
| BPTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 |  | 字符串,或文件条目对象,用于BPTC格式纹理. |
| RGTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 |  | 用于 RGTC 格式纹理的字符串,或文件条目对象. |
| PVRTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 |  | 光电图格式纹理的字符串,或文件条目对象。 |
| S3TC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 |  | 用于S3TC格式纹理的字符串,或文件条目对象. |
| S3TCSRGB | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 |  | 用于S3TCSRGB格式纹理的字符串,或文件条目对象. |
| IMG | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) \| string | 是 |  | 倒置图像文件的字符串,或文件条目对象. |
| shaderType | string | 是 | "'fragment'" | 着色器的类型。 要么是碎片着色器的 `fragment`, 要么是顶点着色器的 `vertex`。 如果您装入着色器捆绑, 则忽略了此选项 。 |
| width | number | 是 | 512 | HTML 的纹理宽度将被渲染到 。 |
| height | number | 是 | 512 | HTML 的纹理高度将被渲染到 。 |
| frameConfig | [Phaser.Types.Loader.FileTypes.ImageFrameConfig](/api/typedef/types-loader-filetypes#imageframeconfig) | 是 |  | 框架配置对象。 只提供和用于精灵表 。 |
| dataKey | string | 是 |  | 如果指定了而不是正在解析并添加到缓存中的全部 JSON 文件, 则只添加与此属性键相对应的段落。 如果您想要提取的属性是嵌入的, 请使用时段分割它 。 |
| baseURL | string | 是 |  | 装入地图集数据中定义的纹理时使用的可选基址 。 |
| flipUV | boolean | 是 |  | 翻转模型数据中存储的紫外线坐标? |
| matURL | string | 是 |  | 对象材料文件的可选绝对或相对的 URL。 如果未定义或 `null` , 则不会装入材料文件 。 |
| matExtension | string | 是 | "'mat'" | 如果没有提供url,则使用默认的材料文件扩展名 。 |
| start | boolean | 是 | false | 装入后自动启动插件吗 ? |
| mapping | string | 是 |  | 如果要将此插件注入到场景中, 这就是所用的属性键 。 |
| systemKey | string | 是 |  | 如果要将此插件添加到 Scene.Systems 中, 此插件的属性键 。 |
| sceneKey | string | 是 |  | 如果要将此插件添加到场景中, 这是它属性的键 。 |
| svgConfig | [Phaser.Types.Loader.FileTypes.SVGSizeConfig](/api/typedef/types-loader-filetypes#svgsizeconfig) | 是 |  | svg 大小配置对象 。 |
| maxRetries | number | 是 | 2 | 如果文件负载失败, 重试的次数 。 |

**类型**: object

**所属**: Phaser.Types.Loader
> 源码：[src/loader/typedefs/FileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/typedefs/FileConfig.js#L1)  
引入版本：3.0.0

---

## XHRSettingsObject {#xhrsettingsobject}

### \<static> XHRSettingsObject {#static-xhrsettingsobject}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| responseType | XMLHttpRequestResponseType | 否 |  | XHR请求的响应类型,即`blob`,`text`等. |
| async | boolean | 是 | true | XHR请求是否使用同步? |
| user | string | 是 | "''" | XHR 请求的可选用户名 。 |
| password | string | 是 | "''" | XHR 请求的可选密码 。 |
| timeout | number | 是 | 0 | 可选 XHR 超时值 。 |
| headers | object \| undefined | 是 |  | 此值用于充值 XHR `setRequestHeader`, 默认时未定义 。 |
| header | string \| undefined | 是 |  | 此值用于充值 XHR `setRequestHeader`, 默认时未定义 。 |
| headerValue | string \| undefined | 是 |  | 此值用于充值 XHR `setRequestHeader`, 默认时未定义 。 |
| requestedWith | string \| undefined | 是 |  | 此值用于充值 XHR `setRequestHeader`, 默认时未定义 。 |
| overrideMimeType | string \| undefined | 是 |  | 提供自定义的 mime 类型来代替默认 。 |
| withCredentials | boolean | 是 | false | withCredentials属性表示是否应当使用cookie,授权头或TLS客户端证书等证书来提出跨站点访问控制请求. 设置withCredentials对同一站点请求没有影响. |

**类型**: object

**所属**: Phaser.Types.Loader
> 源码：[src/loader/typedefs/XHRSettingsObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/typedefs/XHRSettingsObject.js#L1)  
引入版本：3.0.0

---

---
