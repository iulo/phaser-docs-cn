# MultiFile {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-multifile)

多文件是一个复合文件,将两个或两个以上的单个文件对象作为儿童组合,并作为一个单一单位协调其装载和处理。当所有儿童文件都装入时,会叫它使用多文件的`addToCache`方法来组合结果(例如,将纹理图像与其JSON地图集数据连接起来)。它通常被扩展为文件类型的一个基础类,如AtlasJSON、BitmapFont和AudioSprite。您不应该直接创建实例,而是要扩展并覆盖`addToCache`。

**构造函数**

`new MultiFile(loader, type, key, files)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 装入此文件的装入器 。 |
| 类型 | string | 否 | 在装入器内排序的文件类型字符串 。 |
| key | string | 否 | 装填器内文件的密钥 。 |
| files | Array.\<[Phaser.Loader.File](/api/class/loader-file)> | 否 | 构成此多文件的文件阵列 。 |

---


**作用域**: static

> 源码：[src/loader/MultiFile.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L11)  
引入版本：3.7.0

## 公开成员 {#public-members}

### baseURL {#baseURL}

#### baseURL: string {#baseurl-string}


**说明:**

引用了创建多文件时的装入器 baseURL 。 用于插入子文件 。


> 源码：[src/loader/MultiFile.js#L150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L150)  
引入版本：3.20.0


---

### complete {#complete}

#### complete: boolean {#complete-boolean}


**说明:**

此多文件的完成状态 。


> 源码：[src/loader/MultiFile.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L109)  
引入版本：3.7.0


---

### config {#config}

#### config: any {#config-any}


**说明:**

装入文件所需的瞬态数据的存储容器 。


> 源码：[src/loader/MultiFile.js#L141](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L141)  
引入版本：3.7.0


---

### failed {#failed}

#### failed: number {#failed-number}


**说明:**

无法装入的文件数量 。


> 源码：[src/loader/MultiFile.js#L131](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L131)  
引入版本：3.7.0


---

### files {#files}

#### files: Array.\<[Phaser.Loader.File](/api/class/loader-file)> {#files-arrayphaserloaderfile}


**说明:**

构成此多文件的文件组 。


> 源码：[src/loader/MultiFile.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L91)  
引入版本：3.7.0


---

### key {#key}

#### key: string {#key-string}


**说明:**

独有缓存密钥( 在其文件类型中独一无二) 。


> 源码：[src/loader/MultiFile.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L65)  
引入版本：3.7.0


---

### loader {#loader}

#### loader: [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) {#loader-phaserloaderloaderplugin}


**说明:**

引用要装入此文件的装入器 。


> 源码：[src/loader/MultiFile.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L47)  
引入版本：3.7.0


---

### path {#path}

#### path: string {#path-string}


**说明:**

创建多文件时的加载器路径的引用。 用于插入子文件 。


> 源码：[src/loader/MultiFile.js#L160](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L160)  
引入版本：3.20.0


---

### pending {#pending}

#### pending: number {#pending-number}


**说明:**

仍然待补的儿童文件数量。 以儿童文件总数开始, 每次儿童文件完成装入时会减少。 当文件达到零时, 所有的儿童都已完成, 多文件可以处理 。


> 源码：[src/loader/MultiFile.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L119)  
引入版本：3.7.0


---

### prefix {#prefix}

#### prefix: string {#prefix-string}


**说明:**

引用此多文件创建时的加载器前缀。 用于插入子文件 。


> 源码：[src/loader/MultiFile.js#L170](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L170)  
引入版本：3.20.0


---

### state {#state}

#### state: number {#state-number}


**说明:**

文件的当前状态。 FILE_CONST 值之一 。


> 源码：[src/loader/MultiFile.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L100)  
引入版本：3.60.0


---

### type {#type}

#### type: string {#type-string}


**说明:**

在装入器内排序的文件类型字符串 。


> 源码：[src/loader/MultiFile.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L56)  
引入版本：3.7.0


---

## 公开方法 {#public-methods}

### addToMultiFile {#addToMultiFile}

#### \<instance> addToMultiFile(file) {#instance-addtomultifilefile}


**说明:**

将另一个孩子添加到此多文件, 增加待补的计数并重排完成状态 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 要添加到此多文件的文件 。 |


**返回值:** [Phaser.Loader.MultiFile](/api/class/loader-multifile) - 此多文件实例 。


> 源码：[src/loader/MultiFile.js#L200](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L200)  
引入版本：3.7.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此多文件及其所有引用 。


> 源码：[src/loader/MultiFile.js#L296](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L296)  
引入版本：3.60.0


---

### isReadyToProcess {#isReadyToProcess}

#### \<instance> isReadyToProcess() {#instance-isreadytoprocess}


**说明:**

检查此多功能是否准备处理其子/ 是否 。


**返回值:** boolean - 如果这个多功能的孩子们都装好了,就用`true`, 否则用`false`.


> 源码：[src/loader/MultiFile.js#L187](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L187)  
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


> 源码：[src/loader/MultiFile.js#L223](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L223)  
引入版本：3.7.0


---

### onFileFailed {#onFileFailed}

#### \<instance> onFileFailed(file) {#instance-onfilefailedfile}


**说明:**

由每个文件调用, 无法装入 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 装入失败的文件 。 |


> 源码：[src/loader/MultiFile.js#L241](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L241)  
引入版本：3.7.0


---

### pendingDestroy {#pendingDestroy}

#### \<instance> pendingDestroy() {#instance-pendingdestroy}


**说明:**

一旦此多文件的所有子被添加到其缓存中, 多文件现在可以从加载器中删除 。

它将从装填器中发出`filecomplete`事件.


**Fires:** [Phaser.Loader.Events#event:FILE_COMPLETE](/api/event/loader-events#file_complete), [Phaser.Loader.Events#event:FILE_KEY_COMPLETE](/api/event/loader-events#file_key_complete)


> 源码：[src/loader/MultiFile.js#L262](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MultiFile.js#L262)  
引入版本：3.60.0


---

---
