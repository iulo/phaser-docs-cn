# AtlasXMLFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-atlasxmlfile)

基于 XML 的 Texture Atlas 文件, 将文本图像及其关联的 XML 数据文件作为单单元进行加载协调。 这两个文件必须在地图集注册到 Texture 管理器之前成功加载。 注册后, XML 中定义的单个框架可以在整个游戏中用作游戏对象的纹理 。

这些是使用Phaser.Loader.LoaderPlugin#atlasXML方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#atlasXML.

**构造函数**

`new AtlasXMLFile(loader, key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.AtlasXMLFileConfig](/api/typedef/types-loader-filetypes#atlasxmlfileconfig) | 否 | 此文件使用的密钥, 或文件配置对象 。 |
| textureURL | string \| Array.\<string> | 是 | 装入纹理图像文件的绝对或相对 URL。 如果未定义或 `null` , 则会设置为 `<key>.png`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. png" 。 |
| atlasURL | string | 是 | 从中加载纹理图集 xml 数据文件的绝对或相对的 URL 。 如果未定义或 `null` , 则它将被设定为 `<key>.xml` , 即如果 `key` 是"外国人" , 那么 URL 将是 "alien. xml" 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于地图集图像文件的 XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于替换加载器默认 XHR 设置的 XHR 设置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.MultiFile](/api/class/loader-multifile)  



> 源码：[src/loader/filetypes/AtlasXMLFile.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AtlasXMLFile.js#L15)  
引入版本：3.7.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Loader.MultiFile](/api/class/loader-multifile):**


 - [addToMultiFile](/api/class/loader-multifile#addToMultiFile)
 - [destroy](/api/class/loader-multifile#destroy)
 - [isReadyToProcess](/api/class/loader-multifile#isReadyToProcess)
 - [onFileComplete](/api/class/loader-multifile#onFileComplete)
 - [onFileFailed](/api/class/loader-multifile#onFileFailed)
 - [pendingDestroy](/api/class/loader-multifile#pendingDestroy)




---

## 公开方法 {#public-methods}

### addToCache {#addToCache}

#### \<instance> addToCache() {#instance-addtocache}


**说明:**

检查图像和 XML 数据文件是否都装入完毕, 如果装入完毕, 则将纹理图集与纹理管理器注册。 如果存在, 还可以通过可选的普通地图( 套件中的第三个文件) 。 设置 `complete` 改为: `true` 一旦添加了地图集。


> 源码：[src/loader/filetypes/AtlasXMLFile.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AtlasXMLFile.js#L87)  
引入版本：3.7.0


---

## 继承的成员 {#inherited-members}


**From [Phaser.Loader.MultiFile](/api/class/loader-multifile):**


 - [baseURL](/api/class/loader-multifile#baseURL)
 - [complete](/api/class/loader-multifile#complete)
 - [config](/api/class/loader-multifile#config)
 - [failed](/api/class/loader-multifile#failed)
 - [files](/api/class/loader-multifile#files)
 - [key](/api/class/loader-multifile#key)
 - [loader](/api/class/loader-multifile#loader)
 - [path](/api/class/loader-multifile#path)
 - [pending](/api/class/loader-multifile#pending)
 - [prefix](/api/class/loader-multifile#prefix)
 - [state](/api/class/loader-multifile#state)
 - [type](/api/class/loader-multifile#type)




---

---
