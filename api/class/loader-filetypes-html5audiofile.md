# HTML5AudioFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-html5audiofile)

通过 HTML5 音频 API 装入的单个音频文件,适合装入器装入.

与使用Web Audio API的`WebAudioFile`不同,此文件类型创建了标准的HTML `Audio`元素。当Web Audi API无法使用时,或者当游戏配置完全使用HTML5音频时,它被用作倒置。可以创建多个音频元素实例,允许同一声音同时播放而不受干扰。

这些是使用Phaser.Loader.LoaderPlugin#autio方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#adio.

**构造函数**

`new HTML5AudioFile(loader, key, [urlConfig], [audioConfig])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.AudioFileConfig](/api/typedef/types-loader-filetypes#audiofileconfig) | 否 | 此文件使用的密钥, 或文件配置对象 。 |
| urlConfig | string | 是 | 要从中装入此文件的绝对或相对 URL 。 |
| audioConfig | object | 是 | 音频Context 配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/HTML5AudioFile.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/HTML5AudioFile.js#L14)  
引入版本：3.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Loader.File](/api/class/loader-file):**


 - [addToCache](/api/class/loader-file#addToCache)
 - [destroy](/api/class/loader-file#destroy)
 - [hasCacheConflict](/api/class/loader-file#hasCacheConflict)
 - [onBase64Load](/api/class/loader-file#onBase64Load)
 - [onProcess](/api/class/loader-file#onProcess)
 - [onProcessComplete](/api/class/loader-file#onProcessComplete)
 - [onProcessError](/api/class/loader-file#onProcessError)
 - [pendingDestroy](/api/class/loader-file#pendingDestroy)
 - [resetXHR](/api/class/loader-file#resetXHR)
 - [setLink](/api/class/loader-file#setLink)




---

## 公开方法 {#public-methods}

### load {#load}

#### \<instance> load() {#instance-load}


**说明:**

由装入器调用, 启动实际文件下载。 创建一个或多个 HTML 音频元素( 基于配置实例数) , 并为每个元素分配源 URL。 在装入过程中, 使用 onLoad 、 onError 和 onProgress 的方法, 使用 Audio 元素事件。 您通常不应该直接调用这种方法, 但它被装入器引用 。


**Overrides:** Phaser.Loader.File# 装弹量


> 源码：[src/loader/filetypes/HTML5AudioFile.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/HTML5AudioFile.js#L135)  
引入版本：3.0.0


---

### onError {#onError}

#### \<instance> onError() {#instance-onerror}


**说明:**

装入时文件出错时调用 。


**Overrides:** Phaser.Loader.File#onError


> 源码：[src/loader/filetypes/HTML5AudioFile.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/HTML5AudioFile.js#L90)  
引入版本：3.0.0


---

### onLoad {#onLoad}

#### \<instance> onLoad() {#instance-onload}


**说明:**

文件装入完成后调用 。


**Overrides:** Phaser.Loader.File#onLoad


> 源码：[src/loader/filetypes/HTML5AudioFile.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/HTML5AudioFile.js#L72)  
引入版本：3.0.0


---

### onProgress {#onProgress}

#### \<instance> onProgress() {#instance-onprogress}


**说明:**

当一个音频元素点燃其`canplaythrough`事件时,它被调用,表明它准备播放.


**Overrides:** Phaser.Loader.File#onProgress


**Fires:** [Phaser.Loader.Events#event:FILE_PROGRESS](/api/event/loader-events#file_progress)


> 源码：[src/loader/filetypes/HTML5AudioFile.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/HTML5AudioFile.js#L109)  
引入版本：3.0.0


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
