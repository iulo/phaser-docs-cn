# FontFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-fontfile)

适合由 Phaser 加载器加载的单一字体文件 。

此文件类型会使用浏览器的字体FontFace API 来加载网络字体。 处理时, 它会从已解析的 URL 和字体格式中构建一个字体FontFace对象, 同步加载, 并用文档的字体收藏来注册, 以便浏览器可以使用。 一旦加载, 您可以通过 `fontFamily` 样式属性在任意 Phaser 文本对象中按键引用字体 。

这些是使用 Phaser.Loader.LoaderPlugin#font 方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#font。

**构造函数**

`new FontFile(loader, key, [url], [format], [descriptors], [xhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 |  | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.FontFileConfig](/api/typedef/types-loader-filetypes#fontfileconfig) | 否 |  | 此文件使用的键, 或文件配置对象 。 |
| url | string | 是 |  | 装入此文件的绝对或相对的 URL。 如果未定义或 `null` , 它将被设定为 `<key>.ttf`, 即如果 `key` 是" 外国人", 那么 URL 将是" alien. ttf" 。 |
| format | string | 是 | "'truetype'" | 字体类型。 应该是字符串, 如“ truetype ” 或“ opentype ” 。 |
| descriptors | object | 是 |  | 含有字体面部字体描述符的可选对象。 详见 https://developer.mozilla.org/en-US/docs/Web/API/FontFace/FontFace#descriptors 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/FontFile.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/FontFile.js#L15)  
引入版本：3.87.0

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

由 Loader. nextFile自动调用。 这种方法解决了字体的源地址, 并使用浏览器的 FontFace API 构造并同步加载字体。 成功后, 字体会添加到文档的字体收藏中, CSS 类 `fonts-loaded` 将应用到文档正文中。 如果失败, 警告会登录到控制台上。 在这两种情况下, `onProcessComplete`都会被调用来推进资源加载器 。


**重写:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/FontFile.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/FontFile.js#L87)  
引入版本：3.87.0


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
