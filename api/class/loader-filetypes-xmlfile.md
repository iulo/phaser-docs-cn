# XMLFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-xmlfile)

适合 Phaser 加载器加载的单个 XML 文件。 装入后, XML 响应文本会被解析成 DOM 文件对象, 并存储在全局 XML 缓存中, 由您提供的文件键键键 。 然后您可以随时通过 `this.cache.xml.get(key)` 检索, 并使用标准的 DOM 方法进行转录 。

这些是使用Phaser.Loader.LoaderPlugin#xml方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#xml.

**构造函数**

`new XMLFile(loader, key, [url], [xhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.XMLFileConfig](/api/typedef/types-loader-filetypes#xmlfileconfig) | 否 | 此文件使用的键, 或文件配置对象 。 |
| url | string | 是 | 装入此文件的绝对或相对 URL。 如果未定义或 `null` , 则会设置为 `<key>.xml`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. xml" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/XMLFile.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/XMLFile.js#L15)  
引入版本：3.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Loader.File](/api/class/loader-file):**


 - [addToCache](/api/class/loader-file#addToCache)
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

### onProcess {#onProcess}

#### \<instance> onProcess() {#instance-onprocess}


**说明:**

由 Loader. nextFile自动调用。 使用 `ParseXML` 将原始 XHR 响应文本解析为 XML , 并将生成的 DOM 文档保存在 `this.data` 中。 如果解析成功, 请使用 `onProcessComplete` 将文档添加到 XML 缓存中, 并推进负载队列。 如果解析失败( 即 `ParseXML` 返回一个 falsy 值) , 则使用 `onProcessError` 来替代 。


**重写:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/XMLFile.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/XMLFile.js#L69)  
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
