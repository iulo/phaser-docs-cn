# UnityAtlasFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-unityatlasfile)

以 Oliver 文本文件为基础的单一文本文件 Atlas 文件, 适合装入器加载 。

这些是使用Phaser.Loader.LoaderPlugin#unityAtlas方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#unityAtlas.

**构造函数**

`new UnityAtlasFile(loader, key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.UnityAtlasFileConfig](/api/typedef/types-loader-filetypes#unityatlasfileconfig) | 否 | 此文件使用的密钥, 或文件配置对象 。 |
| textureURL | string \| Array.\<string> | 是 | 装入纹理图像文件的绝对或相对 URL。 如果未定义或 `null` , 则会设置为 `<key>.png`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. png" 。 |
| atlasURL | string | 是 | 装入纹理图集数据文件的绝对或相对的 URL。 如果未定义或 `null` , 它将被设定为 `<key>.txt`, 即如果 `key` 是“ 外国人” , 那么 URL 将是“ 外国人. txt ” 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于地图集图像文件的 XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于地图集数据文件的 XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.MultiFile](/api/class/loader-multifile)  



> 源码：[src/loader/filetypes/UnityAtlasFile.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/UnityAtlasFile.js#L15)  
引入版本：3.0.0

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

成功加载和处理后将此文件添加到目标缓存中。


> 源码：[src/loader/filetypes/UnityAtlasFile.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/UnityAtlasFile.js#L85)  
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
