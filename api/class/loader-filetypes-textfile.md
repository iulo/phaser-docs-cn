# TextFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-textfile)

适合资源加载器加载的单一文本文件 。

文本文件从外部文件装入纯文本内容, 并将其保存在文本缓存中, 并将其作为原始字符串。 这些文件对于载入任何基于文本的数据, 如对话框脚本、 CSV 数据、 GLSL 阴影源代码、 级别数据, 或任何其他可以作为字符串显示的内容, 都非常有用。 文本一旦装入, 可以按游戏要求从缓存中检索并解析或处理 。

这些是使用 Phaser.Loader.LoaderPlugin # text 方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#text。

**构造函数**

`new TextFile(loader, key, [url], [xhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.TextFileConfig](/api/typedef/types-loader-filetypes#textfileconfig) | 否 | 此文件使用的键, 或文件配置对象 。 |
| url | string | 是 | 装入此文件的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.txt`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. txt" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/TextFile.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/TextFile.js#L14)  
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

由 Loader. nextFile 自动调用。 此方法控制了文件对已装入的数据的额外工作。 它从 XHR 响应中读取纯文本内容, 并将其保存在 `this.data` 中, 然后调用 `onProcessComplete` 来标记文件, 以备文本缓存使用 。


**重写:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/TextFile.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/TextFile.js#L75)  
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
