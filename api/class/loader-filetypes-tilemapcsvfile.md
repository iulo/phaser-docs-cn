# TilemapCSVFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-tilemapcsvfile)

一个适合资源加载器装入的单台图列马普 CSV 文件.

CSV 平面文件包含一个逗号分隔整数值的网格,每个值代表一个平面图中的瓦片索引。这是Phaser支持的最简单的平面格式之一,对基于网格的基本地图有用。加载后,CSV数据可以使用`this.make.tilemap`来创建您场景中的`Tilemap`对象.

这些是使用Phaser.Loader.LoaderPlugin#tilemapCSV方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#tilemapCSV.

**构造函数**

`new TilemapCSVFile(loader, key, [url], [xhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.TilemapCSVFileConfig](/api/typedef/types-loader-filetypes#tilemapcsvfileconfig) | 否 | 此文件使用的键, 或文件配置对象 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.csv`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. csv" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/TilemapCSVFile.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/TilemapCSVFile.js#L15)  
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




---

## 公开方法 {#public-methods}

### addToCache {#addToCache}

#### \<instance> addToCache() {#instance-addtocache}


**说明:**

成功加载和处理后将此文件添加到目标缓存中。


**重写:** Phaser.Loader.File#addToCache


> 源码：[src/loader/filetypes/TilemapCSVFile.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/TilemapCSVFile.js#L89)  
引入版本：3.7.0


---

### onProcess {#onProcess}

#### \<instance> onProcess() {#instance-onprocess}


**说明:**

由 Loader. nextFile 自动调用。 此方法控制了文件在加载数据中的额外工作 。


**重写:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/TilemapCSVFile.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/TilemapCSVFile.js#L73)  
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
