# PCTAtlasFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-pctatlasfile)

PCT Atlas 文件是一个复合文件类型,它会随其引用的所有纹理图像文件一起加载一个Phaser 压缩纹理图集 (`.pct`) 数据文件。一个PCT文件可以描述一个或多个地图集页面;每个页面由`P:`记录宣布,并装入一个单独的图像。Phaser解析了PCT数据,提取了其页面记录中列出的文件名,并在将完整的地图集添加到纹理管理器之前自动排队并加载每个纹理。解码的PCT数据也存储在全域的Atlas Cache中,由文件键键键键。

这些是使用Phaser.Loader.LoaderPlugin#atlasPCT方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#atlasPCT.

**构造函数**

`new PCTAtlasFile(loader, key, [atlasURL], [path], [baseURL], [atlasXhrSettings], [textureXhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.PCTAtlasFileConfig](/api/typedef/types-loader-filetypes#pctatlasfileconfig) | 否 | 文件的键。 必须在资源加载器和纹理管理器中都独有。 或配置对象 。 |
| atlasURL | string | 是 | 装入PCT数据文件的绝对或相对 URL 。 |
| path | string | 是 | 装入PCT数据中定义的纹理时可选用的路径 。 |
| baseURL | string | 是 | 装入PCT数据中定义的纹理时要使用的可选基址 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为PCT数据文件设置额外的 XHR 设置. |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 特为纹理文件设置额外的 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.MultiFile](/api/class/loader-multifile)  



> 源码：[src/loader/filetypes/PCTAtlasFile.js#L64](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/PCTAtlasFile.js#L64)  
引入版本：4.0.0

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

成功加载和处理后将此文件添加到目标缓存中。解码的PCT数据被添加到Atlas缓存中,加载的纹理图像和解码的框架数据被添加到纹理管理器中,成为单一的多源纹理.


> 源码：[src/loader/filetypes/PCTAtlasFile.js#L194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/PCTAtlasFile.js#L194)  
引入版本：4.0.0


---

### onFileComplete {#onFileComplete}

#### \<instance> onFileComplete(file) {#instance-onfilecompletefile}


**说明:**

每个文件在装入完成时都会调用。 当 PCT 数据文件完成后, 这种方法检查其解码的 `pages` 阵列, 并动态创建和排队它所引用的每一条纹理页的图像文件。 资源加载器的 baseURL、 路径和前缀在此过程中被临时覆盖到 PCTatlasFile 配置中指定的位置, 然后恢复 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 已完成处理的文件 。 |


**重写:** Phaser.Loader.MultiFile#onFileComplete


> 源码：[src/loader/filetypes/PCTAtlasFile.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/PCTAtlasFile.js#L132)  
引入版本：4.0.0


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
