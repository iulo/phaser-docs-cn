# AudioSpriteFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-audiospritefile)

一个适合装入器加载的音频Sprite文件 。

这些是使用Phaser.Loader.LoaderPlugin#audioSprite方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#audioSprite.

**构造函数**

`new AudioSpriteFile(loader, key, jsonURL, [audioURL], [audioConfig], [audioXhrSettings], [jsonXhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.AudioSpriteFileConfig](/api/typedef/types-loader-filetypes#audiospritefileconfig) | 否 | 此文件使用的密钥, 或文件配置对象 。 |
| jsonURL | string | 否 | 绝对或相对的 URL 来从 json 文件装入。 或者一个 良好形成的 JSON 对象来代替 。 |
| audioURL | Object | 是 | 装入音频文件的绝对或相对 URL。 如果是空的, 则通过解析 JSON 文件来获取 。 |
| audioConfig | any | 是 | 音频配置选项 。 |
| audioXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 音频文件的 XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |
| jsonXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于 json 文件的 XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.MultiFile](/api/class/loader-multifile)  



> 源码：[src/loader/filetypes/AudioSpriteFile.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AudioSpriteFile.js#L15)  
引入版本：3.7.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Loader.MultiFile](/api/class/loader-multifile):**


 - [addToMultiFile](/api/class/loader-multifile#addToMultiFile)
 - [destroy](/api/class/loader-multifile#destroy)
 - [isReadyToProcess](/api/class/loader-multifile#isReadyToProcess)
 - [onFileFailed](/api/class/loader-multifile#onFileFailed)
 - [pendingDestroy](/api/class/loader-multifile#pendingDestroy)




---

## 公开方法 {#public-methods}

### addToCache {#addToCache}

#### \<instance> addToCache() {#instance-addtocache}


**说明:**

成功加载和处理后将此文件添加到目标缓存中。


> 源码：[src/loader/filetypes/AudioSpriteFile.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AudioSpriteFile.js#L121)  
引入版本：3.7.0


---

### onFileComplete {#onFileComplete}

#### \<instance> onFileComplete(file) {#instance-onfilecompletefile}


**说明:**

每个文件在装入完毕时都调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 已完成处理的文件 。 |


**Overrides:** Phaser.Loader.MultiFile#onFileComplete


> 源码：[src/loader/filetypes/AudioSpriteFile.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AudioSpriteFile.js#L85)  
引入版本：3.7.0


---

## 继承的成员 {#inherited-members}


**From [Phaser.Loader.MultiFile](/api/class/loader-multifile):**


 - [baseURL](/api/class/loader-multifile#baseURL)
 - [complete](/api/class/loader-multifile#complete)
 - [config](/api/class/loader-multifile#config)
 - [failed](/api/class/loader-multifile#failed)
 - [files](/api/class/loader-multifile#files)
 - [key](/api/class/loader-multifile#key)
 - [loader](/api/class/loader-multifile#loader)
 - [path](/api/class/loader-multifile#path)
 - [pending](/api/class/loader-multifile#pending)
 - [prefix](/api/class/loader-multifile#prefix)
 - [state](/api/class/loader-multifile#state)
 - [type](/api/class/loader-multifile#type)




---

---
