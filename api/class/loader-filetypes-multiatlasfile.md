# MultiAtlasFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-multiatlasfile)

多纹理 Atlas 文件是一个复合文件类型,它可以将一个纹理 Packer 多纹理 ASON 文件连同它引用的所有纹理图像文件一起装入。 当您的图示表资产太大, 无法装入单一纹理, 并且被分割到多个图像文件时, 多纹理 Atlas 有用, 每一个文件由一个共享的 JSON 数据文件描述。 Phaser 将 JSON 自动排队并加载每个引用的图像( 以及任何相关的普通地图) , 然后将完整的地图集添加到单一密钥下的纹理管理器中。

这些是使用Phaser.Loader.LoaderPlugin#multilatlas方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#multilatlas。

**构造函数**

`new MultiAtlasFile(loader, key, [atlasURL], [path], [baseURL], [atlasXhrSettings], [textureXhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.MultiAtlasFileConfig](/api/typedef/types-loader-filetypes#multiatlasfileconfig) | 否 | 文件的密钥。 必须在装入器和纹理管理器中都独有。 或配置对象 。 |
| atlasURL | string | 是 | 装入多图集 json 文件的绝对或相对 URL 。 |
| path | string | 是 | 装入地图集数据中定义的纹理时可选使用路径 。 |
| baseURL | string | 是 | 装入地图集数据中定义的纹理时使用的可选基址 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 特别为地图集json文件设置额外的 XHR 设置 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 特为纹理文件设置额外的 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.MultiFile](/api/class/loader-multifile)  



> 源码：[src/loader/filetypes/MultiAtlasFile.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/MultiAtlasFile.js#L15)  
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


> 源码：[src/loader/filetypes/MultiAtlasFile.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/MultiAtlasFile.js#L156)  
引入版本：3.7.0


---

### onFileComplete {#onFileComplete}

#### \<instance> onFileComplete(file) {#instance-onfilecompletefile}


**说明:**

在每个文件装入完毕时被调用。 当 JSON 地图集文件完成时, 这种方法检查其 `textures` 阵列, 并动态创建和排队它所引用的每个纹理。 如果任何纹理项也定义了 `normalMap` , 也会为此创建链接的 ImageFile。 装入器的 baseURL 路径和前缀在此过程中被临时覆盖到 MultiAtlasFile 配置中指定的位置, 然后恢复 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 已完成处理的文件 。 |


**Overrides:** Phaser.Loader.MultiFile#onFileComplete


> 源码：[src/loader/filetypes/MultiAtlasFile.js#L79](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/MultiAtlasFile.js#L79)  
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
