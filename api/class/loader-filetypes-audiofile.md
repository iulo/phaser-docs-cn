# AudioFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-audiofile)

适合装入器通过Web Audio API加载的单个音频文件.

此文件类型将音频数据作为ArrayBuffer 载入 XHR 之上, 然后使用 Web Audio API 的 `decodeAudioData` 方法将其解码为 AudioBuff 。 由此生成的 AudioBuf 存储在 Phaser 音频缓存中, 可供 Sound 管理器使用 。

如果设备不支持Web Audio API,或者如果Web Audi在游戏配置中已被禁用,则会创建一个`HTML5AudioFile`。您不需要手动选择其中的功能——使用`Phaser.Loader.LoaderPlugin#audio`和Phaser将自动根据设备能力选择正确的文件类型.

这些是使用Phaser.Loader.LoaderPlugin#autio方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#adio.

**构造函数**

`new AudioFile(loader, key, [urlConfig], [xhrSettings], [audioContext])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.AudioFileConfig](/api/typedef/types-loader-filetypes#audiofileconfig) | 否 | 此文件使用的密钥, 或文件配置对象 。 |
| urlConfig | [Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig) | 是 | 从配置对象中装入此文件的绝对或相对 URL 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |
| audioContext | AudioContext | 是 | 此文件将用来处理自己 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/AudioFile.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AudioFile.js#L15)  
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

### create {#create}

#### \<static> create(loader, key, [urls], [config], [xhrSettings]) {#static-createloader-key-urls-config-xhrsettings}


**说明:**

静态厂制方法,为当前设备创建正确的音频文件类型.

检查游戏的音频配置和设备能力, 以决定是返回基于Web Audio API的 `AudioFile`还是回放的 `HTML5AudioFile`。 它首先呼叫 `AudioFile.getAudioURL`, 从指定的列表中找到一个合适的 URL, 浏览器可以播放 。 如果没有找到兼容的 URL, 则会登录警告, 返回 `null` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.AudioFileConfig](/api/typedef/types-loader-filetypes#audiofileconfig) | 否 | 此文件使用的密钥, 或文件配置对象 。 |
| urls | string \| Array.\<string> | [Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig) | Array.\<[Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig)> | 是 | 装入音频的绝对或相对的 URL 。 |
| config | any | 是 | 包含 HTML5Audio 的 `instances` 属性的对象。默认为 1 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |


**返回值:** [Phaser.Loader.FileTypes.AudioFile](/api/class/loader-filetypes-audiofile), [Phaser.Loader.FileTypes.HTML5AudioFile](/api/class/loader-filetypes-html5audiofile) - 创建的音频文件实例, 或 `null` 如果找不到支持的 URL 。


> 源码：[src/loader/filetypes/AudioFile.js#L115](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AudioFile.js#L115)  
引入版本：3.0.0


---

### getAudioURL {#getAudioURL}

#### \<static> getAudioURL(game, urls) {#static-getaudiourlgame-urls}


**说明:**

使用一系列音频 URL, 并返回当前设备能够播放的第一个条目的 URL 配置对象, 其依据是文件扩展名显示的音频格式或 URL 配置物体上明确的 `type` 属性 。

Blob 和数据 URI 总是被接受并立即返回, 不论格式如何。 对于普通的 URL , 扩展名从文件名中提取, 并对照 `game.device.audio` 检查。 如果找不到支持的 URL, 则返回 `null` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 参考 Phaser游戏实例. |
| urls | string \| Array.\<string> | [Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig) | Array.\<[Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig)> | 否 | 一个或多个音频URL,用于测试浏览器支持. |


**返回值:** [Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig) - 第一个支持的音频 URL 配置对象为 `url` 和 `type` 属性,如果没有支持的话,则使用 `null` 属性。


> 源码：[src/loader/filetypes/AudioFile.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AudioFile.js#L169)  
引入版本：3.0.0


---

### onProcess {#onProcess}

#### \<instance> onProcess() {#instance-onprocess}


**说明:**

由装入器自动调用.nextFile。这种方法将使用Web Audio API的编码,通过 XHR 装入的原始音频矩阵缓冲器解码 `decodeAudioData` 方法。成功时,产生的音频缓冲器将存储在 `this.data` 财务报告和已审计财务报表 `onProcessComplete` 用于推进负载队列。失败时,一个错误会被记录到控制台上, `onProcessError` 。在解码开始后,将发布音频链接引用,以避免不必要的保留。


**Overrides:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/AudioFile.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AudioFile.js#L76)  
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
