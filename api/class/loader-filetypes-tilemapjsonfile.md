# TilemapJSONFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-tilemapjsonfile)

一个适合资源加载器加载的单层Tilemap JSON文件.

这些是使用Phaser.Loader.LoaderPlugin#tilemapTiledJSON方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#tilemapTiledJSON.

**构造函数**

`new TilemapJSONFile(loader, key, [url], [xhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.TilemapJSONFileConfig](/api/typedef/types-loader-filetypes#tilemapjsonfileconfig) | 否 | 此文件使用的键, 或文件配置对象 。 |
| url | object \| string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则它将被设定为 `<key>.json`, 即如果 `key` 是“ 外国人 ” 那么 URL 将是“ 外国人. json ” 。 或者, 一个 已形成好的 JSON 对象 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.FileTypes.JSONFile](/api/class/loader-filetypes-jsonfile)  



> 源码：[src/loader/filetypes/TilemapJSONFile.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/TilemapJSONFile.js#L12)  
引入版本：3.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Loader.File](/api/class/loader-file):**


 - [destroy](/api/class/loader-file#destroy)
 - [hasCacheConflict](/api/class/loader-file#hasCacheConflict)
 - [load](/api/class/loader-file#load)
 - [onBase64Load](/api/class/loader-file#onBase64Load)
 - [onError](/api/class/loader-file#onError)
 - [onLoad](/api/class/loader-file#onLoad)
 - [onProcessComplete](/api/class/loader-file#onProcessComplete)
 - [onProcessError](/api/class/loader-file#onProcessError)
 - [onProgress](/api/class/loader-file#onProgress)
 - [pendingDestroy](/api/class/loader-file#pendingDestroy)
 - [resetXHR](/api/class/loader-file#resetXHR)
 - [setLink](/api/class/loader-file#setLink)





**From [Phaser.Loader.FileTypes.JSONFile](/api/class/loader-filetypes-jsonfile):**


 - [onProcess](/api/class/loader-filetypes-jsonfile#onProcess)




---

## 公开方法 {#public-methods}

### addToCache {#addToCache}

#### \<instance> addToCache() {#instance-addtocache}


**说明:**

成功加载和处理后将此文件添加到目标缓存中。


**重写:** Phaser.Loader.FileTypes.JSONFile#addToCache


> 源码：[src/loader/filetypes/TilemapJSONFile.js#L46](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/TilemapJSONFile.js#L46)  
引入版本：3.7.0


---

## 继承的成员 {#inherited-members}


**From [Phaser.Loader.File](/api/class/loader-file):**


 - [base64](/api/class/loader-file#base64)
 - [bytesLoaded](/api/class/loader-file#bytesLoaded)
 - [bytesTotal](/api/class/loader-file#bytesTotal)
 - [cache](/api/class/loader-file#cache)
 - [config](/api/class/loader-file#config)
 - [crossOrigin](/api/class/loader-file#crossOrigin)
 - [data](/api/class/loader-file#data)
 - [key](/api/class/loader-file#key)
 - [linkFile](/api/class/loader-file#linkFile)
 - [loader](/api/class/loader-file#loader)
 - [multiFile](/api/class/loader-file#multiFile)
 - [percentComplete](/api/class/loader-file#percentComplete)
 - [retryAttempts](/api/class/loader-file#retryAttempts)
 - [src](/api/class/loader-file#src)
 - [state](/api/class/loader-file#state)
 - [type](/api/class/loader-file#type)
 - [url](/api/class/loader-file#url)
 - [xhrLoader](/api/class/loader-file#xhrLoader)
 - [xhrSettings](/api/class/loader-file#xhrSettings)




---

---
