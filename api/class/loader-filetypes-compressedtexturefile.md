# CompressedTextureFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-compressedtexturefile)

压缩纹理文件是一种特殊的多文件,它处理GPU-内置压缩纹理格式,如PVR和KTX容器文件,它支持一系列的内部压缩格式,包括ASTC,S3TC,ETC,PVRTC等,在负载时间选择当前GPU支持的最佳格式.

它可以装入单个压缩纹理,带有配套JSON地图集的压缩纹理,或者由Texture Packer Pro导出多图集. `IMG`还可能为不支持任何压缩格式的浏览器或GPU提供回落条目.

这些是使用Phaser.Loader.LoaderPlugin#文字方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#文字。

**构造函数**

`new CompressedTextureFile(loader, key, entry, [xhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string | 否 | 此文件使用的密钥 。 |
| entry | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](/api/typedef/types-loader-filetypes#compressedtexturefileentry) | 否 | 要加载的压缩纹理文件条目 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.MultiFile](/api/class/loader-multifile)  



> 源码：[src/loader/filetypes/CompressedTextureFile.js#L22](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/CompressedTextureFile.js#L22)  
引入版本：3.60.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Loader.MultiFile](/api/class/loader-multifile):**


 - [addToMultiFile](/api/class/loader-multifile#addToMultiFile)
 - [destroy](/api/class/loader-multifile#destroy)
 - [isReadyToProcess](/api/class/loader-multifile#isReadyToProcess)
 - [onFileFailed](/api/class/loader-multifile#onFileFailed)
 - [pendingDestroy](/api/class/loader-multifile#pendingDestroy)




---

## 公开方法 {#public-methods}

### addMultiToCache {#addMultiToCache}

#### \<instance> addMultiToCache() {#instance-addmultitocache}


**说明:**

在成功加载和处理时, 将所有多文件条目添加到目标缓存中。 将多图集中每个二进制纹理文件上加载, 用 PVR 或 KTX 解析器 来解析, 并将其与 JSON 运算表中的相应条目匹配。 仅包含其压缩格式得到当前 GPU 支持的纹理。 任何相关的普通地图也都会被收集和传送。 生成的图像、 地图集数据以及普通地图都会与纹理管理器一起登记为 JSON 阵列地图集 。


> 源码：[src/loader/filetypes/CompressedTextureFile.js#L272](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/CompressedTextureFile.js#L272)  
引入版本：3.60.0


---

### addToCache {#addToCache}

#### \<instance> addToCache() {#instance-addtocache}


**说明:**

成功加载和处理时将此文件添加到目标缓存中。 如果文件是多图集, 它会向 `addMultiToCache` 授权。 否则, 它会使用 PVR 或 KTX 解析器来解析二进制纹理数据, 校验纹理尺寸符合压缩格式的要求, 并检查 GPU 支持内部格式。 如果所有检查都通过纹理管理器, 则随附 JSON 解析器数据即可。 对任何未验证的纹理发出控制台警告 。


> 源码：[src/loader/filetypes/CompressedTextureFile.js#L196](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/CompressedTextureFile.js#L196)  
引入版本：3.60.0


---

### onFileComplete {#onFileComplete}

#### \<instance> onFileComplete(file) {#instance-onfilecompletefile}


**说明:**

在每个文件完成加载时调用。 减少待加文件的计数, 并在加载多图集配置时, 解析已完成的 JSON , 以动态排队方式列出地图集中引用的每个纹理的二进制实例, 以及任何相关的普通地图。 装入器的基础 URL、 路径和前缀在此过程中临时调整到多图集设置中, 然后恢复 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 已完成处理的文件 。 |


**Overrides:** Phaser.Loader.MultiFile#onFileComplete


> 源码：[src/loader/filetypes/CompressedTextureFile.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/CompressedTextureFile.js#L103)  
引入版本：3.60.0


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
