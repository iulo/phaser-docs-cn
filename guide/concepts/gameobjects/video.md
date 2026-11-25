# 视频 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/video)

这个游戏对象能够处理视频文件,视频流或媒体流的播放回放.

您可以选择“ 预装” 视频到 Phaser 视频缓存 :

```js
preload () {
  this.load.video('ripley', 'assets/aliens.mp4');
}

create () {
  this.add.video(400, 300, 'ripley');
}
```

您不必“ 预装” 视频。 您也可以直接从 URL 播放 :

```js
create () {
  this.add.video(400, 300).loadURL('assets/aliens.mp4');
}
```

在所有意图和目的上,视频都是标准的游戏对象,就像Sprite一样。因此,你可以做所有通常的事情,比如缩放、旋转、裁剪、涂料、制作互动、赋予物理体等等。

透明视频也可以通过WebM文件格式进行。提供视频文件已经用α频道编码,并提供浏览器支持WebM播放(不是全部支持),然后它将完全透明地进行游戏。

回放完全通过大多数现代浏览器支持的"请求视频框架 API"处理,为旧浏览器提供了多填充.

**自动播放视频**

视频只能自动播放, 如果浏览器已经解锁了交互, 或者满足了 MEI 设置。 控制自动播放的政策是巨大的, 并且不同浏览器不同。 您可以, 并且应该在这里读更多关于它的信息 : https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide

如果您的视频没有包含任何音频,那么在视频装入时将noAudio参数设定为真实,并且它会经常允许视频立即播放:

```js
preload () {
  this.load.video('pixar', 'nemo.mp4', true);
}
```

负载调用中的第3个参数告诉 Phaser 视频中没有任何音频音轨. 视频没有音频就可以自动播放,不需要用户交互. 带音频的视频不能做到这一点,除非它满足浏览器的MEI设置. 详见 MDN 自动播放指南.

Or:

```js
create () {
  this.add.video(400, 300).loadURL('assets/aliens.mp4', true);
}
```

您可以设置 noAudio 参数为真, 即使视频中包含音频。 它仍然允许视频立即播放, 但音频不会启动 。

注意,由于IE11中存在错误,您无法在WebGL中播放视频纹理给Sprite。对于IE11强制Canvas模式,您无法播放视频纹理 。

关于视频回放和所支持的媒体格式的更多细节,请查看MDN:

- https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement
- https://developer.mozilla.org/en-US/docs/Web/Media/Formats

## 加载视频 {#load-video}

```javascript
this.load.video(key, url, noAudio);
```

参考文献: [load video](/guide/concepts/loader#video)

记下"起源于"
    无法通过`this.load.video(...)`装入视频交叉原产地.  
    使用`this.add.video(x, y).loadURL(urls, noAudio, crossOrigin)`来装入视频交叉原产地.

## 添加视频对象 {#add-video-object}

### 来自 Video 缓存 的参考视频 {#reference-video-from-video-cache}

```javascript
var video = this.add.video(x, y, key);
```

- `key`: 此游戏对象将播放的视频的键, 如存储在视频缓存中 。

### 从 URL 加载视频 {#load-video-from-url}

1. 添加视频对象

    ```javascript
    var video = this.add.video(x, y);
    ```

2. 播放 URL 的视频

    ```javascript
    video.loadURL(url);
    // video.loadURL(urls, noAudio, crossOrigin);
    ```

    - `noAudio` : 视频是否有音频音轨?如果无法,您可以启用自动播放。
        - `false` :有音频跟踪。默认行为。
    - `crossOrigin`:在视频负载请求中用于`crossOrigin`属性的值.  
        - `undefined`:请求中不会设置`crossorigin`,默认行为.
        - `'anonymous'`
        - `'use-credentials'`

### 从 MediaStream 加载视频 {#load-video-from-mediastream}

```javascript
video.loadMediaStream(stream);
// video.loadMediaStream(stream, noAudio, crossOrigin);
```

- `stream` : MediaStream 对象.
- `noAudio` : 视频是否有音频音轨?如果无法,您可以启用自动播放。
  - `false` :有音频跟踪。默认行为。
- `crossOrigin`:在视频负载请求中用于`crossOrigin`属性的值.  
  - `undefined`:请求中不会设置`crossorigin`,默认行为.
  - `'anonymous'`
  - `'use-credentials'`

```javascript
navigator.mediaDevices.getUserMedia({ video: true, audio: false })
    .then(function(stream) {
        video.loadMediaStream(stream, true);
        video.play();
    })
    .catch(function(err) {

    })
```

- [navigator.mediaDevices.getUserMedia](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia)

### 大小 {#size}

- 初大小:256x265(`video.setSize(256, 256)`)
- 播放后大小 : 元数据视频大小

## 播放 {#play}

```javascript
video.play();
// video.play(loop, markerIn, markerOut);
```

- `loop`: 视频循环到尾端时是否应该自动循环? 请注意,并非所有浏览器都支持所有编码格式的_无缝_视频循环.
- `markerIn`,`markerOut`:可选在/出标记时间,以秒计,用于播放视频的序列.

记下"第一次播放视频"
    第一次播放视频时给`video.play()`打电话.

!!! note
    如果你需要视频中的音频, 那你必须考虑的事实
    **视频在用户与浏览器互动之前无法开始播放**进入游戏流中

## 暂停 {#pause}

- Pause

    ```javascript
    video.setPaused();
    // video.setPaused(true);
    ```

- Resume

    ```javascript
    video.setPaused(false);
    ```

注意"暂停播放后播放视频"
    呼叫`video.setPaused(false)`恢复播放.

## 停下来 {#stop}

停止播放视频,清除所有内部事件监听器.

```javascript
video.stop();
```

## 正在玩游戏 {#is-playing}

- 正在玩游戏

    ```javascript
    var isPlaying = video.isPlaying();  // (not PAUSE) and (not not ENDED)
    ```

- 暂停

    ```javascript
    var isPaused = video.isPaused();
    ```

## 播放时间 {#playback-time}

- Get

    ```javascript
    var playbackTime = video.getCurrentTime();
    ```

    or

    ```javascript
    var t = video.getProgress(); // t: 0~1
    ```

- Set
  - 设定为

    ```javascript
    video.setCurrentTime(playbackTime);  // time in seconds
    ```

    or

    ```javascript
    video.seekTo(t); // t: 0~1
    ```

    - 正在寻找

        ```javascript
        var isSeeking = video.isSeeking();
        ```

  - Forward

    ```javascript
    video.setCurrentTime('+' + time);  // time in seconds
    // video.setCurrentTime('+2');
    ```

  - Backeard

    ```javascript
    video.setCurrentTime('-' + time);  // time in seconds
    // video.setCurrentTime('-2');
    ```

## 回放率 {#playback-rate}

- Get

    ```javascript
    var rate = video.getPlaybackRate();
    ```

- Set

    ```javascript
    video.setPlaybackRate(rate);
    ```

## 会期 {#duration}

```javascript
var duration = video.getDuration();  // time in seconds
```

## 音量 {#volume}

- Get

    ```javascript
    var volume = video.getVolume();  // volume: 0~1
    ```

- Set

    ```javascript
    video.setVolume(volume);  // volume: 0~1
    ```

## 静音 {#mute}

- Get

    ```javascript
    var muted = video.isMuted();  // muted: true/false
    ```

- Set

    ```javascript
    video.setMute(muted);  // muted: true/false
    ```

## 循环 {#loop}

- Get

    ```javascript
    var loop = video.getLoop();  // loop: true/false
    ```

- Set

    ```javascript
    video.setLoop(loop);  // loop: true/false
    ```

## 视频密钥 {#video-key}

- Get

    ```javascript
    var key = video.getVideoKey();
    ```

- 更改视频键( 视频来源)

    ```javascript
    video.changeSource(key);
    // video.changeSource(key, autoplay, loop, markerIn, markerOut);
    ```

  - `autoplay` : 视频一旦交换完成,是否应该立即播放?
  - `loop`:视频循环在到达尾声时是否应该自动循环? **并非所有浏览器都支持所有编码格式的_无缝_视频循环**.
  - `markerIn`,`markerOut`:可选的在/出标记时间,以_秒_表示,用于播放视频的序列.

## 标记 {#marks}

- 添加标记

    ```javascript
    video.addMarker(key, markerIn, markerOut);
    ```

  - `key` : 一个给这个标记的独有名称.
  - `markerIn`, `markerOut` : 时间, 以秒计, 代表此标记的起始/ 结束 。
- 播放标记

    ```javascript
    video.playMarker(key, loop);
    ```

- 删除标记

    ```javascript
    video.removeMarker(key);
    ```

## 抓图 {#snapshot}

1. 分配画布 texrure

    ```javascript
    video.saveSnapshotTexture(key);
    ```

    - `key` :纹理键.
2. 拍个快照

    ```javascript
    var canvasTexture = video.video.snapshot();
    // var canvasTexture = video.snapshot(width, height);
    ```

    or

    ```javascript
    var canvasTexture = video.snapshotArea(x, y, srcWidth, srcHeight);
    // var canvasTexture = video.snapshotArea(x, y, srcWidth, srcHeight, destWidth, destHeight);
    ```

    - `x`,`y`:从区域左上方抓取的横向/纵向位置.
    - `srcWidth`, `srcHeight` : 从视频中抓取的区域宽度/高度。
    - `destWidth`, `destHeight` : 抓取的目的地宽度/ 高度, 允许您调整大小 。
    - `canvasTexture` : Canvas纹理对象.
        - 获取纹理键

            ```javascript
            var key = canvasTexture.key;
            ```

## 保存纹理 {#save-texture}

保存的纹理会随着视频播放自动更新。 如果您暂停此视频, 或者更改其来源, 那么保存的纹理会立即更新 。

```javascript
var texture = video.saveTexture(key);
// var texture = video.saveTexture(key, flipY);
```

- `flipY`:如果用作一个沙德的输入,则设定为`true`.

## 事件 {#events}

- 媒体来源并不代表支持的媒体格式.

    ```javascript
    video.on('unsupported', function(video, error){

    }, scope);
    ```

- 视频通过用户姿态解锁.

    ```javascript
    video.on('unlocked', function(video, error){

    }, scope);
    ```

- 一个视频试图播放一个不存在的源,或者是错误的文件类型.

    ```javascript
    video.on('error', function(video, error){

    }, scope);
    ```

- 视频可以访问元数据。

    ```javascript
    video.on('metadata', function(video){

    }, scope);
    ```

- 视频在尝试连接到视频源开始播放时,已经耗尽了分配的时间.

    ```javascript
    video.on('timeout', function(video){

    }, scope);
    ```

- 视频开始播放。

    ```javascript
    video.on('play', function(video){

    }, scope);
    ```

- 开始或重新启动 。

    ```javascript
    video.on('playing', function(video){

    }, scope);
    ```

- 视频已经装入足够的数据,可以进行第一帧拍摄.

    ```javascript
    video.on('textureready', function(video){

    }, scope);
    ```

- 视频通过达到持续时间的结束,即`markerOut`完成播放.

    ```javascript
    video.on('complete', function(video){

    }, scope);
    ```

- 正在播放的视频已循环 。

    ```javascript
    video.on('loop', function(video){

    }, scope);
    ```

- 视频_ begins_ 寻求时间线中的新点.

    ```javascript
    video.on('seeking', function(video){

    }, scope);
    ```

- 影片将完成 寻找新点子的时间。

    ```javascript
    video.on('seeked', function(video){

    }, scope);
    ```

- 已经装入足够多的视频源,使浏览器能够从中制作出帧.

    ```javascript
    video.on('created', function(video, width, height){

    }, scope);
    ```

- 由`stalled`,`suspend`,`waiting`DOM事件编组.

    ```javascript
    video.on('stalled', function(video, width, height){

    }, scope);
    ```

- 视频通过`Video.stop`方法的呼叫停止播放,

    ```javascript
    video.on('stop', function(video){

    }, scope);
    ```

## 其他属性 {#other-properties}

见[game object](/guide/concepts/gameobjects)

## 创建遮罩 {#create-mask}

```javascript
var mask = video.createBitmapMask();
```

见[mask](/guide/concepts/display#masks)

## 着色器效果 {#shader-effects}

支持 [preFX and postFX effects](/guide/concepts/gameobjects/shader) 软件

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
