# ScriptFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-scriptfile)

适合装入器加载的单个脚本文件。 它通过 XHR 获取一个外部的 JavaScript 文件, 并在加载后, 将它注入文档中, 作为附加在 `document.head` 的 `<script>` 元素, 导致其代码立即执行。 经典脚本和 ES 模块都通过 `type` 参数支持 。

这些是使用 Phaser.Loader.LoaderPlugin#script 方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#script。

**构造函数**

`new ScriptFile(loader, key, [url], [type], [xhrSettings])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 |  | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.ScriptFileConfig](/api/typedef/types-loader-filetypes#scriptfileconfig) | 否 |  | 此文件使用的密钥, 或文件配置对象 。 |
| url | string | 是 |  | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.js`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. js" 。 |
| 类型 | string | 是 | "'script'" | 脚本类型。 如果文件包含导出模块, 则应该为经典 JavaScript 的“ 标语 ” , 或“ 模块 ” 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/ScriptFile.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/ScriptFile.js#L14)  
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

由 Loader. nextFile 自动通过文件完成通过 XHR 装入后调用。 创建 `<script>` 元素, 将其 `text` 内容设置在装入文件的原始响应文本中, 并附加到 `document.head` 中, 这使得脚本立即执行。 然后设定文件状态完成 。


**Overrides:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/ScriptFile.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/ScriptFile.js#L74)  
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
