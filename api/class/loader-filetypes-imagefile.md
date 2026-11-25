# ImageFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-imagefile)

适合装入器加载的单个图像文件 。

这些是使用 Phaser.Loader.LoaderPlugin#图像方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#image.

**构造函数**

`new ImageFile(loader, key, [url], [xhrSettings], [frameConfig])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.ImageFileConfig](/api/typedef/types-loader-filetypes#imagefileconfig) | 否 | 此文件使用的密钥, 或文件配置对象 。 |
| url | string \| Array.\<string> | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.png`, 即 `key` 是"外国人", 那么 URL 将是"外国人. png" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |
| frameConfig | [Phaser.Types.Loader.FileTypes.ImageFrameConfig](/api/typedef/types-loader-filetypes#imageframeconfig) | 是 | 框架配置对象。 只提供和用于Sprite工作表 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/ImageFile.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/ImageFile.js#L15)  
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

成功加载和处理后,将此文件添加到纹理管理器中。

如果此图像有链接的普通地图文件, 方法将等待两个文件完成加载后, 通过 `cache.addImage` 将它们合并为一对。 如果没有正常地图, 图像将自动添加到纹理管理器中 。


**Overrides:** Phaser.Loader.File#addToCache


> 源码：[src/loader/filetypes/ImageFile.js#L192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/ImageFile.js#L192)  
引入版本：3.7.0


---

### onProcess {#onProcess}

#### \<instance> onProcess() {#instance-onprocess}


**说明:**

自动调用 `Loader.nextFile` 作为 XHR 加载路径的一部分。创建 HTML ImageElement 并指定 XHR 的blob 响应通过对象 URL 作为源, 触发浏览器解码图像。 成功时, 调用 `onProcessComplete`; 失败时, 拨打 `onProcessError`。只有在图像通过 XHR(默认)加载时才使用这种方法。当 `loader.imageLoadType` 设置为 `"HTMLImageElement"`,则 `onProcessImage` 方法被使用。


**Overrides:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/ImageFile.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/ImageFile.js#L98)  
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
