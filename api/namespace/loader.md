# Phaser.Loader {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/loader)

Scope: 
static
> 源码：[src/loader/index.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/index.js#L10)  


## 静态函数 {#static-functions}

- [File](/api/class/loader-file)
- [LoaderPlugin](/api/class/loader-loaderplugin)
- [MultiFile](/api/class/loader-multifile)
## 静态函数 {#static-functions-1}

### FILE_COMPLETE {#FILE_COMPLETE}

#### FILE_COMPLETE: number {#file_complete-number}


**说明:**

文件处理完毕 。


> 源码：[src/loader/const.js#L117](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L117)  
引入版本：3.0.0


---

### FILE_DESTROYED {#FILE_DESTROYED}

#### FILE_DESTROYED: number {#file_destroyed-number}


**说明:**

文件已被销毁 。


> 源码：[src/loader/const.js#L126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L126)  
引入版本：3.0.0


---

### FILE_ERRORED {#FILE_ERRORED}

#### FILE_ERRORED: number {#file_errored-number}


**说明:**

文件在处理过程中遇到错误 。


> 源码：[src/loader/const.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L108)  
引入版本：3.0.0


---

### FILE_FAILED {#FILE_FAILED}

#### FILE_FAILED: number {#file_failed-number}


**说明:**

文件装入失败 。


> 源码：[src/loader/const.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L90)  
引入版本：3.0.0


---

### FILE_LOADED {#FILE_LOADED}

#### FILE_LOADED: number {#file_loaded-number}


**说明:**

文件已成功装入, 等待处理 。


> 源码：[src/loader/const.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L81)  
引入版本：3.0.0


---

### FILE_LOADING {#FILE_LOADING}

#### FILE_LOADING: number {#file_loading-number}


**说明:**

文件已经由加载器开始加载(onLoad呼叫).


> 源码：[src/loader/const.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L72)  
引入版本：3.0.0


---

### FILE_PENDING {#FILE_PENDING}

#### FILE_PENDING: number {#file_pending-number}


**说明:**

文件处于负载队列中,但尚未启动 。


> 源码：[src/loader/const.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L63)  
引入版本：3.0.0


---

### FILE_PENDING_DESTROY {#FILE_PENDING_DESTROY}

#### FILE_PENDING_DESTROY: number {#file_pending_destroy-number}


**说明:**

文件正在销毁中 。


> 源码：[src/loader/const.js#L144](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L144)  
引入版本：3.60.0


---

### FILE_POPULATED {#FILE_POPULATED}

#### FILE_POPULATED: number {#file_populated-number}


**说明:**

文件是从本地数据中被覆盖的,不需要HTTP请求.


> 源码：[src/loader/const.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L135)  
引入版本：3.0.0


---

### FILE_PROCESSING {#FILE_PROCESSING}

#### FILE_PROCESSING: number {#file_processing-number}


**说明:**

文件正在处理中( onProcess 回调) 。


> 源码：[src/loader/const.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L99)  
引入版本：3.0.0


---

### LOADER_COMPLETE {#LOADER_COMPLETE}

#### LOADER_COMPLETE: number {#loader_complete-number}


**说明:**

装货机已完成装货和加工.


> 源码：[src/loader/const.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L36)  
引入版本：3.0.0


---

### LOADER_DESTROYED {#LOADER_DESTROYED}

#### LOADER_DESTROYED: number {#loader_destroyed-number}


**说明:**

装货机已经被毁了。


> 源码：[src/loader/const.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L54)  
引入版本：3.0.0


---

### LOADER_IDLE {#LOADER_IDLE}

#### LOADER_IDLE: number {#loader_idle-number}


**说明:**

装货机闲置.


> 源码：[src/loader/const.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L9)  
引入版本：3.0.0


---

### LOADER_LOADING {#LOADER_LOADING}

#### LOADER_LOADING: number {#loader_loading-number}


**说明:**

装货机正在积极装货.


> 源码：[src/loader/const.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L18)  
引入版本：3.0.0


---

### LOADER_PROCESSING {#LOADER_PROCESSING}

#### LOADER_PROCESSING: number {#loader_processing-number}


**说明:**

装入器正在处理它装入的文件 。


> 源码：[src/loader/const.js#L27](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L27)  
引入版本：3.0.0


---

### LOADER_SHUTDOWN {#LOADER_SHUTDOWN}

#### LOADER_SHUTDOWN: number {#loader_shutdown-number}


**说明:**

装货机要关机了


> 源码：[src/loader/const.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/const.js#L45)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-2}

- [Events](/api/namespace/loader-events)
- [FileTypes](/api/namespace/loader-filetypes)
- [FileTypesManager](/api/namespace/loader-filetypesmanager)
## 静态函数 {#static-functions-3}

### GetURL {#GetURL}

#### \<static> GetURL(file, baseURL) {#static-geturlfile-baseurl}


**说明:**

以文件及 baseURL 值计算, 返回文件将使用的 URL 下载 。

如果文件没有 URL, `false` 返回。如果文件 URL 已经是绝对的(即它开始于 `blob:`, `data:`, `capacitor://`, `file://`, `http://`, `https://`,或 ,或 , `//`,然后按原样返回。否则, baseURL 准备到文件 URL 以形成完整的 URL。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 将解析 URL 的文件对象 。 |
| baseURL | string | 否 | 当文件 URL 是相对时, 默认要预置的基址 。 |


**返回值:** string - 文件将使用解析的 URL 下载, 或如果文件没有 URL 则使用 `false` 。


> 源码：[src/loader/GetURL.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/GetURL.js#L7)  
引入版本：3.0.0


---

### MergeXHRSettings {#MergeXHRSettings}

#### \<static> MergeXHRSettings(global, local) {#static-mergexhrsettingsglobal-local}


**说明:**

取两个 XHR 设置对象,并从它们中创建一个新的 XHR 设置对象.

新对象被全局设置中给出的值所种子, 但是本地对象中的任何设置都会凌驾全局设置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| global | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 否 | 全球 XHR 设置对象. |
| local | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 否 | 本地 XHRSettings 对象. |


**返回值:** [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) - 一个新形成的 XHRSettings 对象.


> 源码：[src/loader/MergeXHRSettings.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/MergeXHRSettings.js#L10)  
引入版本：3.0.0


---

### XHRLoader {#XHRLoader}

#### \<static> XHRLoader(file, globalXHRSettings) {#static-xhrloaderfile-globalxhrsettings}


**说明:**

创建基于给定的文件和 XHRSettings 的新 XMLHttprequest (xhr) 对象并开始下载。它使用文件自己的 XHRSetting 并合并到全局 XHRSettingst 对象,在下载前设置 xhr 值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 要下载的文件 。 |
| globalXHRSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 否 | 全球 XHR 设置对象. |


**返回值:** XMLHttpRequest - XHR对象。对于 Base64 文件, `file.onBase64Load` 直接调用,此函数返回 `undefined` 。


> 源码：[src/loader/XHRLoader.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/XHRLoader.js#L9)  
引入版本：3.0.0


---

### XHRSettings {#XHRSettings}

#### \<static> XHRSettings([responseType], [async], [user], [password], [timeout], [withCredentials]) {#static-xhrsettingsresponsetype-async-user-password-timeout-withcredentials}


**说明:**

创建一个带有默认值的 XHRSettings 对象。

XHRSettings 对象用于: Phaser 装入器在制作 XMLHttp 请求调用以获取外部资产,例如图像、音频、 JSON 和其他文件时。您可以将自定义的 XHRSettings 对象传递给单个文件装入调用(例如, `this.load.image`) 在每个文件的基础上推翻默认请求配置,或通过加载器设置全局默认 `xhr` 属性。在从服务器上加载需要认证证书、自定义头、特定的 MIME 类型覆盖或非默认响应类型时,此功能是有用的。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| responseType | XMLHttpRequestResponseType | 是 | "''" | The responseType, such as 'text'. |
| async | boolean | 是 | true | XHR请求是否使用同步? |
| user | string | 是 | "''" | XHR 请求的可选用户名 。 |
| password | string | 是 | "''" | XHR 请求的可选密码 。 |
| timeout | number | 是 | 0 | 可选 XHR 超时值, 以毫秒计。 0 的值会禁用超时值 。 |
| withCredentials | boolean | 是 | false | 备选XHR withCredentials值. |


**返回值:** [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) - XHRSettings 对象为加载器所使用的对象.


> 源码：[src/loader/XHRSettings.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/XHRSettings.js#L7)  
引入版本：3.0.0


---

---
