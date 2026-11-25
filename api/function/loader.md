# Phaser.Loader.File {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/function/loader)

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


# Phaser.Loader.FileTypes.AudioFile {#page-title-1}

### create {#create}

#### \<static> create(loader, key, [urls], [config], [xhrSettings]) {#static-createloader-key-urls-config-xhrsettings}


**说明:**

静态厂制方法,为当前设备创建正确的音频文件类型.

检查游戏的音频配置和设备能力, 以决定是返回基于Web Audio API的 `AudioFile`还是回放的 `HTML5AudioFile`。 它首先呼叫 `AudioFile.getAudioURL`, 从指定的列表中找到一个合适的 URL, 浏览器可以播放 。 如果没有找到兼容的 URL, 则会登录警告, 返回 `null` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用此文件的加载器 。 |
| key | string \| [Phaser.Types.Loader.FileTypes.AudioFileConfig](/api/typedef/types-loader-filetypes#audiofileconfig) | 否 | 此文件使用的键, 或文件配置对象 。 |
| urls | string \| Array.\<string> | [Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig) | Array.\<[Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig)> | 是 | 装入音频的绝对或相对的 URL 。 |
| config | any | 是 | 包含 HTML5Audio 的 `instances` 属性的对象。默认为 1 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 专门为此文件设置额外的 XHR 设置 。 |


**返回值:** [Phaser.Loader.FileTypes.AudioFile](/api/class/loader-filetypes-audiofile), [Phaser.Loader.FileTypes.HTML5AudioFile](/api/class/loader-filetypes-html5audiofile) - 创建的音频文件实例, 或 `null` 如果找不到支持的 URL 。


> 源码：[src/loader/filetypes/AudioFile.js#L115](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AudioFile.js#L115)  
引入版本：3.0.0


### getAudioURL {#getAudioURL}

#### \<static> getAudioURL(game, urls) {#static-getaudiourlgame-urls}


**说明:**

使用一系列音频 URL, 并返回当前设备能够播放的第一个条目的 URL 配置对象, 其依据是文件扩展名显示的音频格式或 URL 配置物体上明确的 `type` 属性 。

Blob 和数据 URI 总是被接受并立即返回, 不论格式如何。 对于普通的 URL , 扩展名从文件名中提取, 并对照 `game.device.audio` 检查。 如果找不到支持的 URL, 则返回 `null` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 参考 Phaser游戏实例. |
| urls | string \| Array.\<string> | [Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig) | Array.\<[Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig)> | 否 | 一个或多个音频URL,用于测试浏览器支持. |


**返回值:** [Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig) - 第一个支持的音频 URL 配置对象为 `url` 和 `type` 属性,如果没有支持的话,则使用 `null` 属性。


> 源码：[src/loader/filetypes/AudioFile.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AudioFile.js#L169)  
引入版本：3.0.0


# Phaser.Loader.FileTypesManager {#page-title-2}

### install {#install}

#### \<static> install(loader) {#static-installloader}


**说明:**

当Lader Plugin创建时, 使用静态方法调用 。

循环通过本地类型对象,并将所有对象作为属性注入LaderPlugin实例。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 资源加载器 Plugin 以安装类型 。 |


> 源码：[src/loader/FileTypesManager.js#L22](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/FileTypesManager.js#L22)  
引入版本：3.0.0


### register {#register}

#### \<static> register(key, factoryFunction) {#static-registerkey-factoryfunction}


**说明:**

由文件类型直接调用的稳定方法.

键是用来通过资源加载器加载文件的函数的参考,即`image`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 将用作加载器Plugin中方法名的键 。 |
| factoryFunction | function | 否 | 当LaugerPlugin.key被引用时,将调用函数 。 |


> 源码：[src/loader/FileTypesManager.js#L41](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/FileTypesManager.js#L41)  
引入版本：3.0.0


### destroy {#destroy}

#### \<static> destroy() {#static-destroy}


**说明:**

删除所有相关文件类型。


> 源码：[src/loader/FileTypesManager.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/FileTypesManager.js#L57)  
引入版本：3.0.0


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


### XHRSettings {#XHRSettings}

#### \<static> XHRSettings([responseType], [async], [user], [password], [timeout], [withCredentials]) {#static-xhrsettingsresponsetype-async-user-password-timeout-withcredentials}


**说明:**

创建一个带有默认值的 XHRSettings 对象。

XHRSettings 对象用于: Phaser 资源加载器在制作 XMLHttp 请求调用以获取外部资源,例如图像、音频、 JSON 和其他文件时。您可以将自定义的 XHRSettings 对象传递给单个文件装入调用(例如, `this.load.image`) 在每个文件的基础上推翻默认请求配置,或通过加载器设置全局默认 `xhr` 属性。在从服务器上加载需要认证证书、自定义头、特定的 MIME 类型覆盖或非默认响应类型时,此功能是有用的。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
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
