# BinaryFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-binaryfile)

适合装入器装入的单二进制文件 。

二进制文件用于加载原始二进制数据,如自定义关卡格式,游戏数据档案,或任何必须作为`ArrayBuffer`处理而非解析文本或图像的文件. 数据一旦加载,就存储在二进制缓存中,并且可以通过提供`dataType`构建器自动投放到一个打字阵列(如`Uint8Array`)中.

这些是使用 Phaser.Loader.LoaderPlugin#二进制方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#binary.

**构造函数**

`new BinaryFile(loader, key, [url], [xhrSettings], [dataType])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.BinaryFileConfig](/api/typedef/types-loader-filetypes#binaryfileconfig) | 否 | 此文件使用的密钥, 或文件配置对象 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 它将被设定为 `<key>.bin`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. bin" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |
| dataType | any | 是 | 可选类型将二进制文件投放到一次装入。 例如, `Uint8Array` 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/BinaryFile.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/BinaryFile.js#L14)  
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

由 Loader. nextFile自动调用。 这种方法处理原始 XHR 响应: 如果指定了 `dataType` 构造器( 如 `Uint8Array`), 它会将 `ArrayBuffer` 响应包在一个新实例中; 否则, 原始的 `ArrayBuffer` 直接存储为文件的数据 。


**Overrides:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/BinaryFile.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/BinaryFile.js#L74)  
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
