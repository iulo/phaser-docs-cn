# 资源加载器 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/loader)

资源加载器, 其名称意味着它负责装入您游戏可能需要的任何外部资源。 常见的资源类型包括图像、 纹理图集、 图示表、 字体、 音频文件和 JSON 数据, 但 Phaser 还可以处理更多的 。

默认情况下, 每个场景都能够访问自己的加载器实例。 加载器在一个队列基数上工作, 这意味着您可以任意添加尽可能多的“ 装载请求” , 并且它们都被加到内部队列中。 然后告诉加载器启动, 它会通过队列工作, 依次加载每个资源 。

镜像有一种特殊的方法可以称为“ 预装值 ” 。 当镜像开始时, 这种方法会被 Phaser 自动称为“ 预装数 ” 。 这是一个将您的全部游戏资源添加到“ 预装值” 的好地方, 您将会看到这个常规在我们的例子和第三方的教程中大量使用。 然而, 您也可以在游戏的任意时间, 而不仅仅是预装值方法中添加“ 预装值“ ” 。

当您在加载器中添加一个文件时, 您必须给它一个基于字符串的键。 这是该文件及其相关资源的一个独特的标识符。 例如, 如果您加载了一个图像并给出了键“ 玩家 ” , 那么您就用键“ 玩者” 来识别该图像。 键是区分大小写, 并且每个文件类型都应用其独有性 。 即, 声音文件可以有键“ 玩手” 以及图像文件 。 键在 Phaser 中是一个非常重要的概念, 您会看到它在整个框架中使用 。

文件通过内置浏览器API加载,这往往允许根据浏览器和服务器设置,同时下载许多文件。资源加载器专门根据网络请求和整个网络加载文件,不是用于从本地文件系统加载文件,因为安全原因,所有现代网页浏览器都禁止这样做。

和 Phaser 中的大多数系统一样, 有很多事件您可以从资源加载器中听到。 这些事件自然围绕装入进度进行: 比如哪些文件已经完成, 或可能失败, 以及进程有多远。 您可以利用这些事件为您的游戏创建装入条和进度显示 。

## 战略 {#strategy}

- 在使用资源前装入资源
- 在“ 启动” 或“ 预装” 场景中装入共享资源
- 装入场景中任何非共享资源,它们将被使用
- 必要时,在现场回调前使用场景有效载荷装载小资源`preload()`
- 在特殊情况下,手动运行场景加载器,并访问新装入的资源,以防回调
- 如果保存一些内存不再需要资源, 您可以移除这些资源

## 资源 {#assets}

有很多[types](/api/namespace/loader-filetypes),你可以读到所有它们。

资源需要加载才能使用, 但一旦加载, 资源就随处可见。 哪个加载器或场景加载并不重要。 一旦加载, 资源就会在纹理管理器( Z`this.textures`) 或资源缓存( `this.cache`) 中 。

资源使用独有的键( names) 。

### 在哪里加载资源 {#where-to-load-assets}

在单场比赛中,你自然会把资源装进场景中.

在多场游戏中,在"启动"或"预装机"场景中加载共享资源,然后在之后开始其他场景,方便,任何非共享资源都可以在使用这些资源的场景中加载,必要时当该场景关闭时可以移除.

### 资源类型 {#asset-types}

#### 图像 {#image}

- Image

  ```js
  this.load.image(key, url);
  // this.load.image(key, url, xhrSettings);
  ```

  - `url` : Url 纹理,或base64 字符串的Uri.

- 图像和普通地图

  ```js
  this.load.image(key, [url, normalMapUrl]);
  // this.load.image(key, [url, normalMapUrl], xhrSettings);
  ```

  - `url` : Url 纹理,或base64 字符串的Uri.
  - `normalMapUrl` : 法线贴图的Url.

- SVG

  ```js
  this.load.svg(key, url);
  // this.load.svg(key, url, svgConfig);
  // this.load.svg(key, url, svgConfig, xhrSettings);
  ```

  - `svgConfig` : `{width, height}`,或 ,或 , `{scale}`

- Html 纹理

  ```js
  this.load.htmlTexture(key, url, width, height);
  // this.load.htmlTexture(key, url, width, height, xhrSettings);
  ```

#### 精灵表 {#sprite-sheet}

```js
this.load.spritesheet(key, url, {
  // frameWidth: frameWidth,
  // frameHeight: frameHeight,
  // startFrame: startFrame,
  // endFrame: endFrame,
  // margin: margin,
  // spacing: spacing
});
// this.load.spritesheet(key, url, frameConfig, xhrSettings);
```

#### 纹理图集 {#texture-atlas}

```js
this.load.atlas(key, textureURL, atlasURL);
// this.load.atlas(key, textureURL, atlasURL, textureXhrSettings, atlasXhrSettings);
```

#### 多文件纹理图集 {#multi-file-texture-atlas}

```js
this.load.multiatlas(key, atlasURL);
// this.load.multiatlas(key, atlasURL, path, baseURL, atlasXhrSettings);
```

- `atlasURL`:从中加载纹理图集json数据文件的绝对或相对URL.
- `path`:在加载地图集数据中定义的纹理时使用的可选路径.
- `baseURL`:在加载地图集数据中定义的纹理时使用的可选基址 URL.

#### 统一纹理图集 {#unity-texture-atlas}

```js
this.load.unityAtlas(key, textureURL, atlasURL);
// this.load.unityAtlas(key, textureURL, atlasURL, textureXhrSettings, atlasXhrSettings);
```

#### 动画 {#animation}

```js
this.load.animation(key, url);
// this.load.animation(key, url, dataKey, xhrSettings);
```

#### 音频 {#audio}

```js
this.load.audio(key, urls);
// this.load.audio(key, urls, {instances: 1}, xhrSettings);
```

- `urls`:从或blob,或一个基数64字符串Uri装入音频文件的绝对或相对URL.
- `config.instances`: HTML5Audio 的音频实例数量。默认为 `1` 。

#### 音频图示 {#audio-sprite}

```js
this.load.audioSprite(key, jsonURL, audioURL, audioConfig);
// this.load.audioSprite(key, jsonURL, audioURL, audioConfig, audioXhrSettings, jsonXhrSettings);
```

- `jsonURL`:从json文件装入的绝对或相对URL.
- `audioURL`:从音频文件装入的绝对或相对的URL.
- `audioConfig`: HTML5Audio 含有 `instances` 属性的天体。默认为 `1` 。

#### 视频 {#video}

```js
this.load.video(key, url, noAudio);
// this.load.video(key, url, noAudio, xhrSettings);
```

- `url`:从视频文件装入的绝对或相对URL,或blob.
- `loadEvent`:当 _ not_ 装入为blob时要听的负载事件.
  - `'loadeddata'`: 已有当前框架的数据。 默认值 。
  - `'canplay'` :视频准备开始播放.
  - `'canplaythrough'` :视频可以全程播放,不停车.
- `asBlob`: 将视频装入数据blob, 或者通过视频元素? 默认值为`false` 。
- `noAudio` : 视频是否有音频音轨?如果无法,您可以启用自动播放。
  - `false` :有音频音轨,默认行为.

#### 位图字体 {#bitmap-font}

```js
this.load.bitmapFont(key, textureURL, fontDataURL);
// this.load.bitmapFont(key, textureURL, fontDataURL, textureXhrSettings, fontDataXhrSettings);
```

- `textureURL`:从字体图像文件装入的绝对或相对URL.
- `fontDataURL` : 由软件创建的用于装入字体_ xml_ 数据文件的绝对或相对 URL
  - [Angelcode Bitmap Font Generator](http://www.angelcode.com/products/bmfont/)
  - [Glyph Designer](https://71squared.com/glyphdesigner)
  - [Littera](http://kvazars.com/littera/)( 以闪光为主 - 是的, 真的, 免费)

#### 平铺图 {#tile-map}

- JSON : 使用平面映射编辑器创建, 并选择 JSON 作为导出格式

  ```js
  this.load.tilemapTiledJSON(key, url);
  // this.load.tilemapTiledJSON(key, url, xhrSettings);
  ```

- CSV:在文本编辑器中创建,或以CSV出口的第三方app.

  ```js
  this.load.tilemapCSV(key, url);
  // this.load.tilemapCSV(key, url, xhrSettings);
  ```

#### 文本 {#text}

```js
this.load.text(key, url);
// this.load.text(key, url, xhrSettings);
```

#### 贾森 {#json}

```js
this.load.json(key, url);
// this.load.json(key, url, dataKey, xhrSettings);
```

- `dataKey`:当JSON文件加载时,只将这个属性存储在缓存中.

#### XML 数据 {#xml}

```js
this.load.xml(key, url);
// this.load.xml(key, url, xhrSettings);
```

#### HTML 语句 {#html}

```js
this.load.html(key, url);
// this.load.html(key, url, xhrSettings);
```

#### 支助科 {#css}

```js
this.load.css(key, url);
// this.load.css(key, url, xhrSettings);
```

#### 场景 {#scene}

```js
this.load.sceneFile(key, url);
// this.load.sceneFile(key, url, xhrSettings);
```

电话 `key` 匹配该词组中的**类名称** JavaScript 文档。

##### 脚本 {#script}

```js
this.load.script(key, url);
// this.load.script(key, url, type, xhrSettings);
```

- `type` :　`'script'`,或 ,或 , `'module'`.

##### 脚本 {#scripts}

```js
this.load.scripts(key, urlArray);
// this.load.scripts(key, urlArray, xhrSettings);
```

以`urlArray`的精确顺序添加脚本.

##### GLSL 语言 {#glsl}

```js
this.load.glsl(key, url);
// this.load.glsl(key, url, shaderType, xhrSettings);
```

- `shaderType` : 遮阳器的类型.
  - `'fragment'` : 断层着色器。默认值。
  - `'vertex'` : 韦特克斯荫影.

从缓存获取数据

```js
var cache = scene.cache.shader;
var data = cache.get(key);
```

glsl 文件可以包含多个遮蔽器,全部由前题块分隔.

```GLSL
---
name:
type:
---

void main(void)
{
}
```

##### 二进制 {#binary}

```js
this.load.binary(key, url, dataType); // dataType: Uint8Array
// this.load.binary(key, url, dataType, xhrSettings);
```

- `dataType`:可以选择的类型,将二进制文件投放到一次加载.
  - `Uint8Array`, `Uint8ClampedArray`, `Uint16Array` `Uint32Array`
  - `Int8Array`, `Int16Array`, `Int32Array`
  - `Float32Array`, `Float64Array`
  - `BigInt64Array`, `BigUint64Array`

从缓存获取数据

```js
var cache = scene.cache.binary;
var data = cache.get(key);
```

##### 插件 {#plugin}

```js
this.load.plugin(key, url, true); // start plugin when loaded
// this.load.plugin(key, url, true, undefined, xhrSettings);
```

- `url` : 文件 URL 或类实例 。

##### 场景插件 {#scene-plugin}

```js
this.load.scenePlugin(key, url, systemKey, sceneKey);
// this.load.scenePlugin(key, url, systemKey, sceneKey, xhrSettings);
```

- `url` : 文件 URL 或类实例 。

##### 文件包 {#file-pack}

以 JSON 格式装入文件 。

```js
this.load.pack(key, url);
// this.load.pack(key, url, dataKey, xhrSettings);
```

or

```js
this.load.pack(key, json);
// this.load.pack(key, json, dataKey);
```

- `dataKey`:当JSON文件加载时,只将这个属性存储在缓存中.

JSON包文件 :

```js
{
    'dataKey': {
        // "prefix": "...",          // optional, extend key by prefix
        // "path": "...",            // optional, extend url by path
        // "defaultType": "image",   // optional, default file type
        'files': [
            {
                'type': 'image',
                'key': '...',
                'url': '...'
            },
            {
                'type': 'image',
                'key': '...',
                'url': '...'
            }
            // ...
        ]
    },

    'node0': {
        'node1': {
            'node2': {
                'files': [
                    // ....
                ]
            }
        }
    }
    // dataKey: 'node0.node1.node2'
}
```

文件类型 :

- `audio`
- `binary`
- `glsl`
- `html`
- `htmlTexture`
- `image`
- `json`
- `script`
- `spritesheet`
- `svg`
- `text`
- `tilemapCSV`
- `tilemapJSON`
- `xml`

从缓存获取 json 数据

```js
var cache = scene.cache.json; // pack json is stored in json cache
var data = cache.get(key);
```

`'filecomplete'`事件中的事件名称: `'filecomplete-packfile-' + key`

## 装填器 {#the-loader}

每个场景都有一个装填器插件,`this.load`,用于装填资源.

### 设置路径 {#set-path}

`path`值在文件名之前添加, 而在 `baseURL`( 如果设置) 之后添加。 一旦设置了路径, 将影响从此添加到加载器中的每个文件。 它不会改变任何已经载入载重队列的文件。 要重置它, 请使用这个方法, 无需参数 。

#### 用法 {#usage}

```js
this.load.setPath(path);
```

- Example:

  ```js
  this.load.setPath("images/sprites/");
  this.load.image("ball", "ball.png"); // loads the ball.png file from images/sprites/ball.png
  ```

### 装载器状况 {#status-of-loader}

- 准备开始装入

  ```js
  var isReady = this.load.isReady();
  ```

- 正在装入

  ```js
  var isLoading = this.load.isLoading();
  ```
  
### 正在将文件添加到加载器 {#adding-files-to-the-loader}

每个资源加载方法都按键和 URL 排列资源队列。您稍后会使用键识别该资源 。

有一种 `(key, url)` 参数格式 :

```js
this.load.image("treasure", "treasure.png");
```

还有一个[object config format](/api/namespace/loader-filetypes):

```js
this.load.image({ key: "treasure", url: "treasure.png" });
```

和数组格式 :

```js
this.load.spritesheet([
  {
    key: "mermaid",
    url: "mermaid.png",
    frameConfig: { frameWidth: 16, frameHeight: 16 },
  },
  {
    key: "merman",
    url: "merman.png",
    frameConfig: { frameWidth: 16, frameHeight: 16 },
  },
]);
```

资源加载器将完全不添加有重复键( 每类资源) 的资源 :

```js
this.load.image("sky", "sky1.png");
// 'sky1.png' will be queued and (if loaded) stored as texture key 'sky'

// OOPS:
this.load.image("sky", "sky2.png");
// 'sky2.png' will not be queued at all
```

某些`key`例外:

- 对于某些资源类型(`script()`,有时是`pack()`),你不会再使用键来获取任何东西,所以选择哪个键并不重要.
- 对于`plugin()`,`sceneFile()`,以及`scenePlugin()`,`key`,必须作为插件或场景的全局类名.

相对的URL解析为[base URL of the document](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base),除非您配置加载器的`path`或`baseURL`值.

每个资源加载方法为加载器创建一个临时的[File](/api/class/loader-file)对象,如果需要,您可以通过加载事件处理器访问。这些只持续到加载周期。

你可以写出你自己的资源 很容易:

```js
const files = {
  animation: [/* … */],
  audio: [/* … */],
  image: [/* … */],
  spritesheet: [/* … */],
};

this.load.animation(files.animation);
this.load.audio(files.audio);
this.load.image(files.images);
this.load.spritesheet(files.spritesheet};
```

A [File Pack](/api/class/loader-loaderplugin#pack) could do as well:

```js
this.load.pack("pack1", {
  section1: {
    files: [
      { type: "image", key: "conch", url: "conch.png" },
      {
        type: "spritesheet",
        key: "mermaid",
        url: "mermaid.png",
        frameConfig: {
          /* … */
        },
      },
    ],
  },
});
```

文件包至少需要一个命名的区段(例如, `section1` 上面)。如果您正在同时装入所有包资源,那么它并不真正重要。文件描述的是单独下载包资源的方法,但是如果您想要这样做,那么下载整个包更为实用。 `load.json()` 然后从 JSON 数据中选择区域,并将这些区域传送到 `load.pack()`.

您可以在加载器运行时将资源添加到加载队列中 :

```js
this.load.json("level1", "level1.json");
this.load.on("filecomplete-json-level1", (key, type, data) => {
  this.load.image(data.images);
  this.load.spritesheet(data.spritesheets);
});
```

`load.multiatlas()`,`load.pack()`,和`load.spine()`工作这种方式。

### 加载事件 {#load-events}

#### 事件 {#events}

- 装入文件完成事件

  ```js
  this.load.on("filecomplete", function (key, type, data) {}, scope);
  ```

  or
  
  ```js
  this.load.on(
    "filecomplete-" + type + "-" + key,
    function (key, type, data) {},
    scope
  );
  ```

- 添加加载文件事件

  ```js
  this.load.on("addfile", function (key, type, file) {}, scope);
  ```

- 开始装入

  ```js
  this.load.once("start", function () {}, scope);
  ```

- 正在装入进度

  ```js
  this.load.on("progress", function (progress) {}, scope);
  ```

  - `progress`值会在文件加载时增加,在添加新文件加载请求时减少.

    ```js
    var loader = this.load;
    var total = loader.totalToLoad;
    var remainder = loader.list.size + loader.inflight.size;
    var progress = 1 - remainder / total;
    ```

- 正在装入文件进度

  ```js
  this.load.on(
    "fileprogress",
    function (file, progress) {
      // var key = file.key;
    },
    scope
  );
  ```

- 装入文件对象成功

  ```js
  this.load.once("load", function (fileObj) {}, scope);
  ```

- 装入文件对象失败

  ```js
  this.load.once("loaderror", function (fileObj) {}, scope);
  ```

- 所有装入完成
  - 释放资源前

    ```js
    this.load.once("postprocess", function (loader) {}, scope);
    ```

  - 释放资源后

    ```js
    this.load.once("complete", function (loader) {}, scope);
    ```

- 场景 `'preupdate'`, `'update'`, `'postupdate'`, `'render'` 预装阶段将触发事件。

#### 预装阶段 {#preload-stage}

大多数时候你都会在场景中装入资源 `preload()`方法.

`preload()`返回时,资源加载器会自动启动,然后在装入完成后才调用`create()`。在此期间,场景处于`LOADING`状态,仍然更新并制作出其游戏对象,但不调用场景`update()`。您可以这样显示装入进度 。

##### 用法 {#usage-1}

```js
this.load.image(key, url);
// this.load.image(config); // config: {key, url}
```

预装阶段的装货员会通过场景自动开始装货.

#### 加载进度 {#loading-progress}

最好在负载Z`START`事件中创建任何游戏对象,并在负载`COMPLETE`事件中销毁它们,这样重启装填器就不会产生任何错误.

- [load progress event](https://labs.phaser.io/edit.html?src=src/loader/loader%20events/load%20progress.js)
- [file progress event](https://labs.phaser.io/edit.html?src=src/loader/loader%20events/file%20progress%20event.js)
 
#### 预装阶段后加载 {#loading-after-preload-stage}

要在 `preload()` 之外加载资源,您要像往常一样添加文件,为完成事件添加监听器,然后自己启动加载器.

##### 用法 {#usage-2}

```js
this.load.image(key, url); // add task
// this.load.image(config); // config: {key, url}
this.load.once("complete", callback, scope); // add callback of 'complete' event
this.load.start(); // start loading
```

```js
this.load
  .image(["conch", "treasure", "trident"])
  .once("complete", () => {
    // All files complete
  })
  .start();
```

如果两个过程分别调用加载器的`start()`,则无妨。如果已经装入,则不会重新启动或清除队列。

其他场景应该从游戏缓存或纹理管理器中收听"添加"事件:

```js
this.cache.audio.on("add", (cache, key) => {
  if (key === "music") {
    this.sound.play("music");
  }
});

this.textures.on("addtexture-map", (texture) => {
  // The key is also in `texture.key`.
  this.add.image(0, 0, "map");
});
```

## 场景有效载荷 {#scene-payload}

场景有效载荷是`preload()`的替代方案,它允许您在场景开始时立即加载资源。它经常被使用,因为您需要加载一些小资源来使用**Turing** `preload()`,您不希望在此之前启动额外场景(及其加载器)的麻烦。一个场景下载有效载荷时,不会处于`LOADING`状态,无法更新或渲染任何东西,所以最好能保持有效载荷的小型.

包式物体结构与[pack file](/api/class/loader-loaderplugin#pack)部分的`files`部分相同.

```js
const sceneConfig = {
  pack: {
    files: [
      { type: "json", key: "settings", url: "settings.json" },
      { type: "image", key: "bar", url: "bar.png" },
    ],
  },
  init: function () {
    // Pack has downloaded. 'settings' is in JSON cache.
    this.game.registry.merge(this.cache.json.get("settings"));
  },
  preload: function () {
    // 'bar' is in the Texture Manager.
    this.load.on("start", () => {
      const loadingBar = this.add.image(0, 0, "bar");
    });
  },
};
```

## 移除资源 {#removing-assets}

您可以移除资源以保存内存。 首先删除任何使用这些资源的游戏对象或场景对象( 如 Sounds) !

从纹理管理器中删除纹理 :

```js
this.textures.remove("conch");
```

以及来自各自缓存的其他资源:

```js
this.cache.audio.remove("chime");
this.cache.json.remove("settings");
```

移除资源以重新使用其钥匙换换不同资源的通常是一个坏主意.

## XHR 设置对象 {#xhr-settings-object}

您对每个装入的文件所用的 `xhrSettings` 对象有不少控制。 这样您就可以修改超时、 请求或证书信头。 对象的形式如下 :

```js
{
    async: true,
    user: '',
    password: '',
    timeout: 0,
    headers: undefined,
    header: undefined,
    headerValue: undefined,
    requestedWith: undefined,
    overrideMimeType: undefined,
    withCredentials: false
}
```

- `user`: XHR请求的可选用户名.
- `password`: XHR请求的可选密码.
- `timeout`:可选 XHR超时值.
- `headers`, `header`, `headerValue`, `requestedWith` : 此值用于填充 XHR 值 `setRequestHeader`
- `overrideMimeType`:提供自定义的mime类型来代替默认使用.
- `withCredentials` : 是否应当使用cookie,授权头或TLS客户端证书等证书来提出跨站点访问控制请求. _Setting `withCredentials` 对同一地点的请求没有效力。 _

## 更多配置 {#more-configurations}

游戏配置中更多的配置

```js
loader:{
    baseURL: '',
    path: '',
    enableParallel: true,
    maxParallelDownloads: 4,
    crossOrigin: undefined,
    responseType: '',
    async: true,
    user: '',
    password: '',
    timeout: 0,
    withCredentials: false,
    imageLoadType: 'XHR',    // 'HTMLImageElement'
    localScheme: [ 'file://', 'capacitor://' ]
},
```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)
- [samme](https://github.com/samme)

---
