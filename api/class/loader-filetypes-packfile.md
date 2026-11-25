# PackFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-packfile)

一个适合资源加载器装入的JSON Pack文件.

Pack File 是描述要加载的其他资源的集合的JSON 运单。在处理Pack File时,加载者会读取其内容,并排队列出每个资源供加载,这样您就可以在单个外部的JSON文件中定义一组游戏资源,而不是在代码中调用单个加载方法.

这些是使用 Phaser.Loader.LoaderPlugin# pack 方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#pack。

**构造函数**

`new PackFile(loader, key, [url], [xhrSettings], [dataKey])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.PackFileConfig](/api/typedef/types-loader-filetypes#packfileconfig) | 否 | 此文件使用的键, 或文件配置对象 。 |
| url | string \| any | 是 | 从或准备中的 JSON 对象加载此文件的绝对或相对的 URL 。 如果未定义或 `null` , 则它将被设定为 `<key>.json`, 即 `key` 是"外国人", 那么 URL 将是 "alien.json" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |
| dataKey | string | 是 | 当 JSON 文件加载时, 将只存储此属性到缓存 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/PackFile.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/PackFile.js#L12)  
引入版本：3.7.0

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

由 Loader. nextFile 自动调用。 此方法控制了文件在加载数据中的额外工作 。


**重写:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/PackFile.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/PackFile.js#L52)  
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
