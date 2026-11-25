# JSONFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-jsonfile)

适合资源加载器加载的单个 JSON 文件。 JSON 文件在装入时会自动解析, 生成的数据对象会存储在全局的 JSON 缓存中, 由文件键键键键。 您可以选择提供 `dataKey` , 仅从 JSON 中提取并缓存特定的嵌入属性, 而非全部文件 。 JSON 文件通常用于存储游戏配置、 关卡数据、 拼图数据、 本地化字符串, 或您游戏所需的任何其他结构化数据 。

这些是使用Phaser.Loader.LoaderPlugin#json方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#json.

**构造函数**

`new JSONFile(loader, key, [url], [xhrSettings], [dataKey])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.JSONFileConfig](/api/typedef/types-loader-filetypes#jsonfileconfig) | 否 | 此文件使用的键, 或文件配置对象 。 |
| url | object \| string | 是 | 装入此文件的绝对或相对的 URL。 如果未定义或 `null` , 它将设定为 `<key>.json`, 即如果 `key` 是“ 外国人 ” 那么 URL 将是“ 外国人 . json ” 。 或者, 可以是完全形成的 JSON 对象 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |
| dataKey | string | 是 | 当 JSON 文件加载时, 将只存储此属性到缓存 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/JSONFile.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/JSONFile.js#L15)  
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

由 Loader. nextFile自动调用。 这种方法将 XHR 响应文本解析为 JSON。 如果在加载队列时指定了 `dataKey` , 则只将该点标记键路径的值存储在 `this.data`; 否则将存储整个解析的 JSON 对象。 处理完成后,它就称为 `onProcessComplete` 。


**重写:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/JSONFile.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/JSONFile.js#L92)  
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
