# HTMLFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-htmlfile)

适合装入器加载的单一 HTML 文件 。

HTML 文件作为原始文本字符串加载,并存储在 HTML 缓存中。它们通常用于为 `Phaser.GameObjects.DOMElement` 实例提供 HTML 标记,允许您直接将基于 DOM 的 UI 元素嵌入游戏中。 所装入的字符串可以从缓存中检索, 并传递到 DOMelament 的 `createFromCache` 方法, 或者在使用前进一步操纵 。

这些是使用 Phaser.Loader.LoaderPlugin#html 方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#html.

**构造函数**

`new HTMLFile(loader, key, [url], [xhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.HTMLFileConfig](/api/typedef/types-loader-filetypes#htmlfileconfig) | 否 | 此文件使用的密钥, 或文件配置对象 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.html`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. html" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/HTMLFile.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/HTMLFile.js#L14)  
引入版本：3.12.0

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

此文件装入完成后, 由装入器自动调用。 从 XHR 响应中读取 HTML 原始文本, 并将其保存在 `this.data` 中, 然后标记文件为已处理 。


**Overrides:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/HTMLFile.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/HTMLFile.js#L71)  
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
