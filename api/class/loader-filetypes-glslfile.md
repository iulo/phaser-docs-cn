# GLSLFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-filetypes-glslfile)

适合装入器装入的单一 GLSL 文件 。

GLSL(OpenGL Shading Language)文件包含WebGL渲染器用于创建自定义视觉效果的阴影源代码. 原始的GLSL源被装入后,被包裹在一个`BaseShader`实例中,并存储在全球的阴影缓存中,可以在此检索并应用到支持自定义阴影的游戏对象,例如使用`Phaser.GameObjects.Shader`类的游戏对象.

这些是使用 Phaser.Loader.LoaderPlugin#glsl 方法创建的,一般不直接创建.

关于所有参数和配置选项的文档,请参见Phaser.Loader.LoaderPlugin#glsl.

**构造函数**

`new GLSLFile(loader, key, [url], [xhrSettings])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.GLSLFileConfig](/api/typedef/types-loader-filetypes#glslfileconfig) | 否 | 此文件使用的密钥, 或文件配置对象 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 它将被设定为 `<key>.glsl`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. glsl" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |

---


**作用域**: static


**继承**

> [Phaser.Loader.File](/api/class/loader-file)  



> 源码：[src/loader/filetypes/GLSLFile.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/GLSLFile.js#L15)  
引入版本：3.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Loader.File](/api/class/loader-file):**


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

### addToCache {#addToCache}

#### \<instance> addToCache() {#instance-addtocache}


**说明:**

成功加载和处理后将此文件添加到目标缓存中。 原始的 GLSL 源字符串被新 `BaseShader` 实例包裹, 并存储在这个文件的密钥下的全球缓存中, 使其可用阴影驱动的游戏对象 。


**Overrides:** Phaser.Loader.File#addToCache


> 源码：[src/loader/filetypes/GLSLFile.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/GLSLFile.js#L90)  
引入版本：3.17.0


---

### onProcess {#onProcess}

#### \<instance> onProcess() {#instance-onprocess}


**说明:**

由 Loader. nextFile自动调用。 此方法读取了从已完成的 XHR 响应中生成的原始 GLSL 源文本, 并将其存储在 `this.data` 中, 然后立即发出信号, 显示处理完成 。 在此阶段没有进行进一步的解析或转换; 源被存储到 `addToCache` 运行 。


**Overrides:** Phaser.Loader.File#onProcess


> 源码：[src/loader/filetypes/GLSLFile.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/GLSLFile.js#L72)  
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
