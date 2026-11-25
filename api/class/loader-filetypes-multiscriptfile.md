# MultiScriptFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-multiscriptfile)

适合资源加载器加载的多脚本文件 。

这些是使用 Phaser.Loader.LoaderPlugin#scripts 方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#scripts。

**构造函数**

`new MultiScriptFile(loader, key, [url], [xhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.MultiScriptFileConfig](/api/typedef/types-loader-filetypes#multiscriptfileconfig) | 否 | 此文件使用的键, 或文件配置对象 。 |
| url | Array.\<string> | 是 | 一组绝对或相对的 URL 来从中加载脚本文件。它们按数组中给出的顺序处理 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 脚本文件的 XHR 设置配置对象。 用于替换资源加载器默认 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.MultiFile](/api/class/loader-multifile)  



> 源码：[src/loader/filetypes/MultiScriptFile.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/MultiScriptFile.js#L14)  
引入版本：3.17.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Loader.MultiFile](/api/class/loader-multifile):**


 - [addToMultiFile](/api/class/loader-multifile#addToMultiFile)
 - [destroy](/api/class/loader-multifile#destroy)
 - [isReadyToProcess](/api/class/loader-multifile#isReadyToProcess)
 - [onFileComplete](/api/class/loader-multifile#onFileComplete)
 - [onFileFailed](/api/class/loader-multifile#onFileFailed)
 - [pendingDestroy](/api/class/loader-multifile#pendingDestroy)




---

## 公开方法 {#public-methods}

### addToCache {#addToCache}

#### \<instance> addToCache() {#instance-addtocache}


**说明:**

当此多文件中的所有文件装入完毕时, 资源加载器自动调用。 为每个装入的文件创建 `<script>` 元素, 设置语言为 JavaScript , 禁用延迟执行, 将元素与响应文本一起填充, 并按指定文件的准确顺序附加到 `document.head` 。 这导致每个脚本立即按正确的顺序执行, 保留任何字符间依赖性 。


> 源码：[src/loader/filetypes/MultiScriptFile.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/MultiScriptFile.js#L80)  
引入版本：3.17.0


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
