# SVGFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-svgfile)

一个适合资源加载器装入的单一 SVG 文件 。

SVG文件作为文本加载,可选择根据宽度,高度或尺度因素调整大小,然后光栅化成位图图像并存储在纹理管理器中。一旦加载,任何接受纹理键的游戏对象都可以使用所产生的纹理,就像PNG或JPEG图像一样.

这些是使用 Phaser.Loader.LoaderPlugin#svg 方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#svg.

**构造函数**

`new SVGFile(loader, key, [url], [svgConfig], [xhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.SVGFileConfig](/api/typedef/types-loader-filetypes#svgfileconfig) | 否 | 此文件使用的键, 或文件配置对象 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL 。 如果未定义或 `null` , 则会设置为 `<key>.svg`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. svg" 。 |
| svgConfig | [Phaser.Types.Loader.FileTypes.SVGSizeConfig](/api/typedef/types-loader-filetypes#svgsizeconfig) | 是 | svg 大小配置对象 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/SVGFile.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/SVGFile.js#L14)  
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


> 源码：[src/loader/filetypes/SVGFile.js#L189](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/SVGFile.js#L189)  
引入版本：3.7.0


---

### onProcess {#onProcess}

#### \<instance> onProcess() {#instance-onprocess}


**说明:**

由资源加载器自动调用.nextFile中,此方法可解析原始 SVG 文本响应,可选择修改 SVG 的宽度、高度或 viewBox 属性根据文件的 svgConfig,然后将结果序列化成Blob并将其加载到HTML ImageElement。在不支持对象URL(如旧版本的Safari)的浏览器上,它会回到一个数据URI。一旦图像加载, `onProcessComplete` 需要最终确定文件。


**重写:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/SVGFile.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/SVGFile.js#L77)  
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
