# Phaser.Loader.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/loader-events)

Scope: 
static
> 源码：[src/loader/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/events/index.js#L7)  


## 静态函数 {#static-functions}

### ADD {#ADD}

#### ADD {#add}


**说明:**

资源加载器插件添加文件事件 。

当新文件成功添加到加载器并被放置到加载队列时,此事件会被发送 。

听听场景用`this.load.on('addfile', listener)`

如果您从 `preload` 方法将大量文件添加到加载器中, 它会为每个加载器发送此事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 添加到资源加载器中的文件的独有键 。 |
| 类型 | string | 否 | [文件类型]QQLink Phaser.Loader.File#类型] 添加到加载器中的文件的字符串,即`image`. |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用发送此事件的资源加载器插件 。 |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 引用加载器中添加的文件 。 |


> 源码：[src/loader/events/ADD_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/events/ADD_EVENT.js#L7)  
引入版本：3.0.0


---

### COMPLETE {#COMPLETE}

#### COMPLETE {#complete}


**说明:**

资源加载器插件完成事件 。

当资源加载器已完全处理装入队列中的所有文件时, 此事件将发出。 到此点, 每个装入的文件都将处于其相关的缓存中, 并准备使用 。

听听场景用`this.load.on('complete', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用发送此事件的资源加载器插件 。 |
| totalComplete | number | 否 | 成功装入的文件总数 。 |
| totalFailed | number | 否 | 无法装入的文件总数 。 |


> 源码：[src/loader/events/COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/events/COMPLETE_EVENT.js#L7)  
引入版本：3.0.0


---

### FILE_COMPLETE {#FILE_COMPLETE}

#### FILE_COMPLETE {#file_complete}


**说明:**

文件装入完成事件 。

当队列中的 _ 任何_ 文件完成装入时, 由资源加载器插件发送此事件 。

听听场景用`this.load.on('filecomplete', listener)`

完成后请务必移除此听器,否则如果场景重新装弹,它会继续开火.

您也可以收听特定文件的完成情况。 请参看 [``FILE_KEY_COMPLETE``](/api/event/loader-events#file_key_complete)事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 刚刚装入并完成处理的文件的键 。 |
| 类型 | string | 否 | 刚刚装入的文件的[文件类型] QQlink Phaser.Loader.File#类型],即`image`. |
| data | any | 是 | 文件包含的原始数据。 如果文件是一个多文件, 如地图集或位图字体, 此参数将不被定义 。 |


> 源码：[src/loader/events/FILE_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/events/FILE_COMPLETE_EVENT.js#L7)  
引入版本：3.0.0


---

### FILE_KEY_COMPLETE {#FILE_KEY_COMPLETE}

#### FILE_KEY_COMPLETE {#file_key_complete}


**说明:**

文件装入完成事件 。

当队列中的任何文件完成装入时,此事件由资源加载器插件发送 。

它使用从文件的键和类型构建的特殊动态事件名称.

例如,如果装上了`image`的键,可以使用以下方法监听: 使用`monster`的键.

```javascript
this.load.on('filecomplete-image-monster', function (key, type, data) {
    // Your handler code
});
```

或者,如果你装上了一个带`Level1`键的纹理`atlas`:

```javascript
this.load.on('filecomplete-atlasjson-Level1', function (key, type, data) {
    // Your handler code
});
```

或者,如果你装上了一个带有`Explosion`键和`GAMEOVER`前缀的图示表:

```javascript
this.load.on('filecomplete-spritesheet-GAMEOVERExplosion', function (key, type, data) {
    // Your handler code
});
```

完成后请务必移除监听器,否则如果场景重新装弹,他们将继续开火.

您也可以收听文件的通用补全。 请参看 [``FILE_COMPLETE``](/api/event/loader-events#file_complete) 事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 刚刚装入并完成处理的文件的键 。 |
| 类型 | string | 否 | 刚刚装入的文件的[文件类型] QQlink Phaser.Loader.File#类型],即`image`. |
| data | any | 是 | 文件包含的原始数据。 如果文件是一个多文件, 如地图集或位图字体, 此参数将不被定义 。 |


> 源码：[src/loader/events/FILE_KEY_COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/events/FILE_KEY_COMPLETE_EVENT.js#L7)  
引入版本：3.0.0


---

### FILE_LOAD {#FILE_LOAD}

#### FILE_LOAD {#file_load}


**说明:**

文件装入事件 。

此事件由资源加载器插件在文件装入完成时发送, 但_ 在_ 之前处理并添加到内部的 Phaser 缓存中 。

听听场景用`this.load.on('load', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 引用刚刚装入的文件 。 |


> 源码：[src/loader/events/FILE_LOAD_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/events/FILE_LOAD_EVENT.js#L7)  
引入版本：3.0.0


---

### FILE_LOAD_ERROR {#FILE_LOAD_ERROR}

#### FILE_LOAD_ERROR {#file_load_error}


**说明:**

文件装入错误事件 。

当文件无法装入时, 由资源加载器插件发送此事件 。

听听场景用`this.load.on('loaderror', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 引用在加载时出错的文件 。 |


> 源码：[src/loader/events/FILE_LOAD_ERROR_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/events/FILE_LOAD_ERROR_EVENT.js#L7)  
引入版本：3.0.0


---

### FILE_PROGRESS {#FILE_PROGRESS}

#### FILE_PROGRESS {#file_progress}


**说明:**

文件加载进度事件 。

如果浏览器收到 DOM 进步Event , 而 `lengthComputable` 事件属性为真实, 则此事件由资源加载器插件在文件加载时发送。 取决于使用中的文件大小和浏览器大小, 这可能发生, 也可能不会发生 。

听听场景用`this.load.on('fileprogress', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 引用已更新进度的文件 。 |
| percentComplete | number | 否 | 0到1之间的值表示此文件的“ 完成” 如何 。 |


> 源码：[src/loader/events/FILE_PROGRESS_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/events/FILE_PROGRESS_EVENT.js#L7)  
引入版本：3.0.0


---

### POST_PROCESS {#POST_PROCESS}

#### POST_PROCESS {#post_process}


**说明:**

资源加载器插件后处理事件 。

当资源加载器装入了装入队列中的所有内容时, 此事件由资源加载器插件发送。 它在清除内部列表并销毁每个文件之前发送 。

使用此钩来进行任何仅能在资源加载器完成后,但在排放`complete`事件之前进行的文件的最后一分钟处理.

听听场景用`this.load.on('postprocess', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用发送此事件的资源加载器插件 。 |


> 源码：[src/loader/events/POST_PROCESS_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/events/POST_PROCESS_EVENT.js#L7)  
引入版本：3.0.0


---

### PROGRESS {#PROGRESS}

#### PROGRESS {#progress}


**说明:**

资源加载器插件进度事件 。

当资源加载器更新其载荷进度时,通常由于文件已完成装入,此事件会被发送.

听听场景用`this.load.on('progress', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| progress | number | 否 | 负载当前进度。 0 到 1 之间的值 。 |


> 源码：[src/loader/events/PROGRESS_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/events/PROGRESS_EVENT.js#L7)  
引入版本：3.0.0


---

### START {#START}

#### START {#start}


**说明:**

资源加载器插件启动事件 。

当资源加载器开始运行时, 此事件会被发送。 此时负载进度为 0 。

即使负载队列中没有任何文件,此事件也会被发送.

听听场景用`this.load.on('start', listener)`

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 引用发送此事件的资源加载器插件 。 |


> 源码：[src/loader/events/START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/events/START_EVENT.js#L7)  
引入版本：3.0.0


---

---
