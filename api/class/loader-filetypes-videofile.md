# VideoFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-videofile)

适合装入器加载的单个视频文件 。

这些是使用Phaser.Loader.LoaderPlugin#video方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#video.

**构造函数**

`new VideoFile(loader, key, [urls], [noAudio])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 |  | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.VideoFileConfig](/api/typedef/types-loader-filetypes#videofileconfig) | 否 |  | 此文件使用的密钥, 或文件配置对象 。 |
| urls | string \| Array.\<string> | [Phaser.Types.Loader.FileTypes.VideoFileURLConfig](/api/typedef/types-loader-filetypes#videofileurlconfig) | Array.\<[Phaser.Types.Loader.FileTypes.VideoFileURLConfig](/api/typedef/types-loader-filetypes#videofileurlconfig)> | 是 |  | 绝对或相对的URL从中加载视频文件. |
| noAudio | boolean | 是 | false | 视频是否有音频音轨? 如果您不能, 您可以启用自动播放 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/VideoFile.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/VideoFile.js#L15)  
引入版本：3.20.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Loader.File](/api/class/loader-file):**


 - [addToCache](/api/class/loader-file#addToCache)
 - [destroy](/api/class/loader-file#destroy)
 - [hasCacheConflict](/api/class/loader-file#hasCacheConflict)
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

### load {#load}

#### \<instance> load() {#instance-load}


**说明:**

由装入器调用处理此文件 。 与大多数文件类型不同, VideoFile 不在此步骤中执行 XHR 请求或下载视频数据 。 相反, 它会解决最终的 URL 并立即标记文件已装入, 因此装入器可以继续。 视频游戏对象在需要播放时, 实际的视频内容会在稍后被获取。 您通常不应该直接调用这种方法, 而是要由装入器引用 。


**Overrides:** Phaser.Loader.File# 装弹量


> 源码：[src/loader/filetypes/VideoFile.js#L94](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/VideoFile.js#L94)  
引入版本：3.20.0


---

### onProcess {#onProcess}

#### \<instance> onProcess() {#instance-onprocess}


**说明:**

由 Loader. nextFile自动调用。 这种方法为此文件组装了已处理的数据对象, 存储解析的 URL, `noAudio` 旗, 以及跨原产地设置, 这样一个视频游戏对象可以使用它们来在适当的时候加载视频 。


**Overrides:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/VideoFile.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/VideoFile.js#L74)  
引入版本：3.20.0


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
