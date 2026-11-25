# File {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-file)

装入器可以支持的所有文件类型所使用的基本文件类。 它管理一个文件从队列到下载到处理到完成的生命周期, 处理 XHR 配置、 URL 分辨率、 进度跟踪和错误状态。 您不应该直接创建文件实例, 而是应该用自己的类扩展它, 设置自定义类型并覆盖 `onProcess` 处理已装入的数据的方法。见 `Phaser.Loader.FileTypes` 用于内建文件类型示例。

**构造函数**

`new File(loader, fileConfig)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 装入此文件的装入器 。 |
| fileConfig | [Phaser.Types.Loader.FileConfig](/api/typedef/types-loader#fileconfig) | 否 | 文件配置对象,由文件类型创建. |

---


**作用域**: static

> 源码：[src/loader/File.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L16)  
引入版本：3.0.0

## 公开成员 {#public-members}

### base64 {#base64}

#### base64: boolean {#base64-boolean}


**说明:**

此文件是否包含数据 URI ?


> 源码：[src/loader/File.js#L240](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L240)  
引入版本：3.80.0


---

### bytesLoaded {#bytesLoaded}

#### bytesLoaded: number {#bytesloaded-number}


**说明:**

以文件载荷更新。 只有在通过 XHR 装入时才设置 。


> 源码：[src/loader/File.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L169)  
引入版本：3.0.0


---

### bytesTotal {#bytesTotal}

#### bytesTotal: number {#bytestotal-number}


**说明:**

此文件的总大小。 由 onProgress 设定, 并且只能通过 XHR 装入 。


> 源码：[src/loader/File.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L158)  
引入版本：3.0.0


---

### cache {#cache}

#### cache: [Phaser.Cache.BaseCache](/api/class/cache-basecache), [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) {#cache-phasercachebasecache-phasertexturestexturemanager}


**说明:**

缓存的引用, 或纹理管理器, 如果它装入的话, 将会存储此文件 。


> 源码：[src/loader/File.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L48)  
引入版本：3.7.0


---

### config {#config}

#### config: * {#config-1}


**说明:**

一个配置对象,可以被文件类型用来存储过渡数据.


> 源码：[src/loader/File.js#L210](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L210)  
引入版本：3.0.0


---

### crossOrigin {#crossOrigin}

#### crossOrigin: string, undefined {#crossorigin-string-undefined}


**说明:**

对于基于 CORS 的加载。 如果未定义, 文件将检查加载器。 crossOrigin 并使用( 如果设置)


> 源码：[src/loader/File.js#L191](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L191)  
引入版本：3.0.0


---

### data {#data}

#### data: * {#data-1}


**说明:**

已处理的文件数据, 在文件装入后保存在此 。


> 源码：[src/loader/File.js#L201](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L201)  
引入版本：3.0.0


---

### key {#key}

#### key: string {#key-string}


**说明:**

独有缓存密钥( 其文件类型中独一无二)


> 源码：[src/loader/File.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L71)  
引入版本：3.0.0


---

### linkFile {#linkFile}

#### linkFile: [Phaser.Loader.File](/api/class/loader-file) {#linkfile-phaserloaderfile}


**说明:**

此文件是否有关联的链接文件? 例如图像和普通地图。 Atlass and Bitmap Fonts 使用 multiFile , 因为这些文件需要加载, 但实际上没有数据绑定, 以 linkFile 所在 。


> 源码：[src/loader/File.js#L229](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L229)  
引入版本：3.7.0


---

### loader {#loader}

#### loader: [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) {#loader-phaserloaderloaderplugin}


**说明:**

引用要装入此文件的装入器 。


> 源码：[src/loader/File.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L39)  
引入版本：3.0.0


---

### multiFile {#multiFile}

#### multiFile: [Phaser.Loader.MultiFile](/api/class/loader-multifile) {#multifile-phaserloadermultifile}


**说明:**

如果这是多部分文件, 即地图集及其 json 一起使用, 那么这个文件就是对母多文件的引用。 设定并被装入器或特定文件类型内部使用 。


> 源码：[src/loader/File.js#L219](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L219)  
引入版本：3.7.0


---

### percentComplete {#percentComplete}

#### percentComplete: number {#percentcomplete-number}


**说明:**

0 至 1 之间的百分比值表示此文件装入了多少。 只有在通过 XHR 装入时才设置 。


> 源码：[src/loader/File.js#L180](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L180)  
引入版本：3.0.0


---

### retryAttempts {#retryAttempts}

#### retryAttempts: number {#retryattempts-number}


**说明:**

重试此文件失败前的计数器 。

您可以在文件连接对象中设置此属性值。 如果不存在, 此属性将在创建此文件实例时从 `LoaderPlugin.maxRetries` 属性中读取 。

您可以通过 Game Config 设置此值, 或者可以在装入器启动后的任何时间调整 `LoaderPlugin` 属性。 但是, 它不会适用于已经添加到装入器的文件, 仅适用于该值被更改后添加的文件 。


> 源码：[src/loader/File.js#L249](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L249)  
引入版本：3.85.0


---

### src {#src}

#### src: string {#src-string}


**说明:**

此文件将从最后的 URL 中加载, 包括 baseURL 和路径 。 当加载器调用此文件中的“ 装入 ” 时, 自动设定 。


> 源码：[src/loader/File.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L116)  
引入版本：3.0.0


---

### state {#state}

#### state: number {#state-number}


**说明:**

文件的当前状态。 FILE_CONST 值之一 。


> 源码：[src/loader/File.js#L149](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L149)  
引入版本：3.0.0


---

### type {#type}

#### type: string {#type-string}


**说明:**

用于在装入器内排序的文件类型字符串(图像,json等).


> 源码：[src/loader/File.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L57)  
引入版本：3.0.0


---

### url {#url}

#### url: object, string {#url-object-string}


**说明:**

文件的URL,不包括baseURL.

如果有字符串, 自动有Lauger. path 预设 。

也可以是JavaScript对象,如解析JSON数据的结果.


> 源码：[src/loader/File.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L103)  
引入版本：3.0.0


---

### xhrLoader {#xhrLoader}

#### xhrLoader: XMLHttpRequest {#xhrloader-xmlhttprequest}


**说明:**

正在装入此文件的 XMLHttpRequest 实例( XHR Loader 创建) 。


> 源码：[src/loader/File.js#L140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L140)  
引入版本：3.0.0


---

### xhrSettings {#xhrSettings}

#### xhrSettings: [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) {#xhrsettings-phasertypesloaderxhrsettingsobject}


**说明:**

合并的 XHR 设置用于此文件 。


> 源码：[src/loader/File.js#L126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L126)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### addToCache {#addToCache}

#### \<instance> addToCache() {#instance-addtocache}


**说明:**

成功加载和处理后将此文件添加到目标缓存中。 此方法经常被特定文件类型所覆盖 。


> 源码：[src/loader/File.js#L509](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L509)  
引入版本：3.7.0


---

### createObjectURL {#createObjectURL}

#### \<static> createObjectURL(image, blob, defaultType) {#static-createobjecturlimage-blob-defaulttype}


**说明:**

使用 URL API 创建对象 URL 并设置为图像“ sc” 属性的静态方法。如果 URL APi 不被支持( 通常是在旧浏览器上) , 则会回到使用文件阅读器创建 Base64 编码的 URL 上 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| image | HTMLImageElement | 否 | 图像对象“ 弧” 属性应设定为对象 URL 。 |
| blob | Blob | 否 | Blob 对象创建对象 URL 。 |
| defaultType | string | 否 | 如果 blob 类型不可用, 则使用默认 MIME 类型 。 |


> 源码：[src/loader/File.js#L571](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L571)  
引入版本：3.7.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此文件及其所有引用 。


> 源码：[src/loader/File.js#L553](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L553)  
引入版本：3.7.0


---

### hasCacheConflict {#hasCacheConflict}

#### \<instance> hasCacheConflict() {#instance-hascacheconflict}


**说明:**

检查匹配此文件使用的密钥是否存在于目标缓存中。 由 Loader Plugin 自动调用, 以决定文件是否安全上载或会发生冲突 。


**返回值:** boolean - `true` 如果添加此文件将引发冲突, 否则 `false`.


> 源码：[src/loader/File.js#L494](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L494)  
引入版本：3.7.0


---

### load {#load}

#### \<instance> load() {#instance-load}


**说明:**

由装入器调用, 开始实际文件下载。 在装入过程中, 使用 onLoad、 onError 和 onProgress 的方法, 其依据是 XHR 事件。 您通常不应该直接调用这种方法, 而是要由装入器引用 。


> 源码：[src/loader/File.js#L301](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L301)  
引入版本：3.0.0


---

### onBase64Load {#onBase64Load}

#### \<instance> onBase64Load(xhr) {#instance-onbase64loadxhr}


**说明:**

如果它被赋予了一个有基础64数据的文件来加载,则由 XHR Loader 调用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| xhr | XMLHttpRequest | 否 | 包含解码的基数64数据的 FakeXHR 对象. |


> 源码：[src/loader/File.js#L369](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L369)  
引入版本：3.80.0


---

### onError {#onError}

#### \<instance> onError(xhr, event) {#instance-onerrorxhr-event}


**说明:**

如果装入时文件错误, 则会调用。 重新设置 XHR 状态, 然后将重载的 `retryAttempts` 重新进行调试, 或者在没有尝试重试的情况下, 通过 `nextFile` 向装入器发出失败信号 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| xhr | XMLHttpRequest | 否 | XMLHttp 请求导致这个偏差事件 。 |
| event | ProgressEvent | 否 | 由此错误产生的 DOM 进步事件 。 |


> 源码：[src/loader/File.js#L390](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L390)  
引入版本：3.0.0


---

### onLoad {#onLoad}

#### \<instance> onLoad(xhr, event) {#instance-onloadxhr-event}


**说明:**

文件装入完成后调用, 发送 DOM 进步事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| xhr | XMLHttpRequest | 否 | XMLHttp 请求导致本次上载事件 。 |
| event | ProgressEvent | 否 | 由这个负载产生的 DOM 进步事件 。 |


> 源码：[src/loader/File.js#L336](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L336)  
引入版本：3.0.0


---

### onProcess {#onProcess}

#### \<instance> onProcess() {#instance-onprocess}


**说明:**

通常被文件类型覆盖, 并被 Loader. nextFile 所调用。 这种方法控制了此文件在加载数据时的额外工作, 例如, JSON 文件将在这个阶段中解析自身 。


> 源码：[src/loader/File.js#L439](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L439)  
引入版本：3.0.0


---

### onProcessComplete {#onProcessComplete}

#### \<instance> onProcessComplete() {#instance-onprocesscomplete}


**说明:**

当文件完成处理时调用。 如果设置, 请检查其多文件状态 。


> 源码：[src/loader/File.js#L453](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L453)  
引入版本：3.7.0


---

### onProcessError {#onProcessError}

#### \<instance> onProcessError() {#instance-onprocesserror}


**说明:**

当文件完成处理但产生错误时调用。 如果设置, 请检查其多文件的状态 。


> 源码：[src/loader/File.js#L472](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L472)  
引入版本：3.7.0


---

### onProgress {#onProgress}

#### \<instance> onProgress(event) {#instance-onprogressevent}


**说明:**

正在调用文件加载进度。 发送了 DOM 进步事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | ProgressEvent | 否 | DOM进步晚会. |


**Fires:** [Phaser.Loader.Events#event:FILE_PROGRESS](/api/event/loader-events#file_progress)


> 源码：[src/loader/File.js#L417](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L417)  
引入版本：3.0.0


---

### pendingDestroy {#pendingDestroy}

#### \<instance> pendingDestroy() {#instance-pendingdestroy}


**说明:**

一旦文件被添加到缓存中, 即已调用, 并准备从装入器中删除。 它将从装入器 Plugin 中释放一个 `filecomplete` 事件 。


**Fires:** [Phaser.Loader.Events#event:FILE_COMPLETE](/api/event/loader-events#file_complete), [Phaser.Loader.Events#event:FILE_KEY_COMPLETE](/api/event/loader-events#file_key_complete)


> 源码：[src/loader/File.js#L524](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L524)  
引入版本：3.7.0


---

### resetXHR {#resetXHR}

#### \<instance> resetXHR() {#instance-resetxhr}


**说明:**

从此文件使用的 XHR Loader 实例清除 `onload`、 `onerror` 和 `onprogress` 事件处理器,防止在负载完成或出错后进行 stale callbacks 开火。


> 源码：[src/loader/File.js#L284](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L284)  
引入版本：3.0.0


---

### revokeObjectURL {#revokeObjectURL}

#### \<static> revokeObjectURL(image) {#static-revokeobjecturlimage}


**说明:**

释放一个已有对象 URL的静态方法,它以前是通过调用 [Phaser.Loader.File.createObjectURL](/api/class/loader-file#createObjectURL) 方法创建的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| image | HTMLImageElement | 否 | 图像对象的“ 弧” 属性应当取消 。 |


> 源码：[src/loader/File.js#L605](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L605)  
引入版本：3.7.0


---

### setLink {#setLink}

#### \<instance> setLink(fileB) {#instance-setlinkfileb}


**说明:**

将该文件与另一个文件链接, 因此它们依赖对方进行加载和处理 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| fileB | [Phaser.Loader.File](/api/class/loader-file) | 否 | 连接到此文件的文件 。 |


> 源码：[src/loader/File.js#L269](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/File.js#L269)  
引入版本：3.7.0


---

---
