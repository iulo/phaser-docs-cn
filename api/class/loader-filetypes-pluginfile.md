# PluginFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-pluginfile)

适合 Phaser 加载器加载的单个插件脚本文件。 插件文件代表一个外部的 JavaScript文件, 装入后, 注册一个 Phaser 插件, 并提供给插件管理器。 脚本执行方式是将其作为 `<script>` 元素附加到文档头部。 该插件可以在给定属性键下自动启动并注入当前场景 。

这些是使用 Phaser.Loader.LoaderPlugin#插件方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#plugin。

**构造函数**

`new PluginFile(loader, key, [url], [start], [mapping], [xhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 |  | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.PluginFileConfig](/api/typedef/types-loader-filetypes#pluginfileconfig) | 否 |  | 此文件使用的键, 或文件配置对象 。 |
| url | string | 是 |  | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.js`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. js" 。 |
| start | boolean | 是 | false | 装入后自动启动插件吗 ? |
| mapping | string | 是 |  | 如果要将此插件注入到场景中, 这就是所用的属性键 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为此文件设置额外的 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/PluginFile.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/PluginFile.js#L14)  
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

由 Loader. nextFile自动调用。 处理已装入的插件文件, 并将其安装到 Scene 的插件管理器中。 如果插件是作为类或函数直接提供的, 则立即安装。 否则, 将创建新的 `<script>` 元素, 包含已装入的 JavaScript 源, 并附在文档头上执行, 然后用文件键从全局范围安装插件。 如果设置了 Scene 映射键或自动启动旗, 插件也会被注入到当前 Scene 和 Scene Systems 中 。


**重写:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/PluginFile.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/PluginFile.js#L85)  
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
