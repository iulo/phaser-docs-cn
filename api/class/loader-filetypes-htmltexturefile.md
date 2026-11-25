# HTMLTextureFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-htmltexturefile)

适合加载器加载的 HTML 纹理文件。 此文件类型从服务器中加载 HTML 文件, 将其内容包裹在 SVG `foreignObject` 元素内, 大小为指定的宽度和高度, 将 SVG 转换为 `Blob` URL, 然后使其成为 `Image` 元素。 由此生成的图像存储在纹理管理器中, 并且可以被任何接受纹理键的游戏对象用作纹理 。

这些是使用Phaser.Loader.LoaderPlugin#htmlTexture方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#htmlTexture.

**构造函数**

`new HTMLTextureFile(loader, key, [url], [width], [height], [xhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.HTMLTextureFileConfig](/api/typedef/types-loader-filetypes#htmltexturefileconfig) | 否 | 此文件使用的键, 或文件配置对象 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.html`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. html" 。 |
| width | number | 是 | HTML 的纹理宽度将被渲染到 。 |
| height | number | 是 | HTML 的纹理高度将被渲染到 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/HTMLTextureFile.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/HTMLTextureFile.js#L14)  
引入版本：3.12.0

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


> 源码：[src/loader/filetypes/HTMLTextureFile.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/HTMLTextureFile.js#L145)  
引入版本：3.7.0


---

### onProcess {#onProcess}

#### \<instance> onProcess() {#instance-onprocess}


**说明:**

由 Loader. nextFile 自动调用。 将 HTML 内容包入一个大小为配置宽度和高度的 SVG `foreignObject` 元素内处理。 SVG 标记后转换为 `window.Blob` , 指定为新的 `Image` 元素的对象 URL。 一旦图像负载成功, 文件会向完成状态过渡, 并准备添加到纹理管理器中。 如果 Blob 创建或图像加载失败, 文件会被标记为错误 。


**重写:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/HTMLTextureFile.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/HTMLTextureFile.js#L80)  
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
