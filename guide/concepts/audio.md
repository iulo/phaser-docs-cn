# 音频 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/audio)

网络浏览器提供了两种不同方式播放音频的能力。 第一种是称为音频标签。 这是您可以在网页上设置的 HTML 标签, 它提供 UI 控件来播放和暂停/重现音频文件。 第二种是称为 Web Audio API。 这是一个 JavaScript API, 它允许您直接从代码创建并控制音频文件。 它比音频标签要强大得多, 但并非所有浏览器都支持它 。

Phaser有一个内置的音效管理器,允许您在游戏中播放音频文件。它会自动检测浏览器是否支持Web音频 API,如果支持的话,它会使用它。如果不支持,它会掉回音频标签。这意味着您可以使用相同的API在所有浏览器中播放音频文件,不管他们对Web音频 CPI的支持如何.

和WebGL vs. Canvas一样,有些东西只有Web Audio可以做,比如位置音频,即在整个游戏世界中都有"跟随"玩家的声音,它也更适合在快速的接续中演奏大量短时间的音效,即"枪声"或"爆炸".

您可以通过 Game 配置选择您想要使用的音频系统, 或甚至完全禁用音频。 毕竟并非所有游戏都需要音频 。

Phaser声音管理器是一个全局系统。 这意味着它属于游戏实例, 如果您开始在一个场景中播放声音, 它不会自动停止, 仅仅是因为你改变到另一个场景。 这给了你很多控制权, 但也意味着当你完成这些声音时, 您需要小心停止循环, 或者它们会继续播放 。

## 自动播放 {#autoplay}

大多数浏览器在用户点击/taps在游戏中才会播放声音。 您可以检查声音管理器的 `locked` 属性 。

Chrome 给使用 Web Audio 的游戏靴子提供控制台警告:

> 音频连接无法启动。 在页面上显示用户手势后必须恢复( 或创建) 。

正常。 Phaser 将尝试在第一个用户手势( 点击/ tap) 后恢复音频上下文。 如果您在游戏中不需要声音, 请禁用音频, 并且您不会看到此警告 。

也可以通过点击/tap创建游戏以避免这个问题.

有些浏览器在播放锁定的声音时会给出控制台错误,有些则不会.

- [Autoplay guide for media and Web Audio APIs](https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide)

## 配置 {#configuration}

### 网络音频 {#web-audio}

网络音频是默认音频上下文.

### 禁用网络音频 {#disable-web-audio}

```js
var config = {
  // ....
  audio: {
    disableWebAudio: true,
  },
  // ....
};
var game = new Phaser.Game(config);
```

### 禁用所有音频 {#disable-all-audio}

```js
var config = {
  // ....
  audio: {
    noAudio: true,
  },
  // ....
};
var game = new Phaser.Game(config);
```

## 加载音频文件 {#loading-audio-files}

请参看 [Media container formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Containers)和 [Web audio codec guide](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Audio_codecs) 的细节。 如果您要发布游戏, 您应该至少支持 [MP3](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Containers#mpegmpeg-2) 。

在加载音频时, Phaser 匹配了介质类型( 从 URL 或 您给出的) , 设备支持该类型 。 如果没有匹配, ** 无任何信息 ** 会被下载, 如果您尝试用该键创建或播放声音, 则会因错误而失败 。

```js
this.load.audio(key, urls, config, xhrSettings);
```

- `key` : 此文件使用的键, 或文件配置对象, 或其中的数组 。
- `urls`:从音频文件装入的绝对或相对URL.
- `config`: HTML5Audio 包含实例属性的对象。默认为 1 。
- `xhrSettings`: 一个 XHR 设置配置对象。 用于替换资源加载器默认 XHR 设置 。

### 解码音频 {#decode-audio}

将音频数据解码为一种通过Web Audio可以播放的格式。音频数据可以是一个基码字符串、一个音频媒体类型的数据uri,或者一个ArrayBuffer实例。

```js
this.sound.decodeAudio(key, audioData);
```

- `audioData`:音频数据
  - 一个编码为 Base64 的字符串
  - 音频媒体类数据 UR
  - 矩阵缓冲实例

Or

```js
this.sound.decodeAudio(audioFiles);
```

- `audioFiles`: 一组`{key, data}`
  - `data`:音频数据
    - 一个编码为 Base64 的字符串
    - 音频媒体类数据 UR
    - 矩阵缓冲实例

### 解码事件 {#decoded-events}

- 完成音频数据的解码

  ```js
  this.sound.on("decoded", key);
  ```

- 已完成所有音频数据的解码

  ```js
  this.sound.on("decodedall");
  ```

## 解锁音频 {#unlock-audio}

解锁初始输入事件的Web音频 API/HTML5音频加载.

```js
this.sound.unlock();
```

## 播放声音 {#play-sound}

播放结束时声音实例会被销毁 。

```js
this.sound.play(key);
```

or

```js
this.sound.play(key, config);
/*
var sound = this.sound.add(key);
sound.play(config);
*/
```

## 空间音频听器的位置 {#position-of-the-spatial-audio-listener}

设置此 Web Audios 上下文空间音频监听器的 `x`和 `y` 位置 。

```js
this.sound.setListenerPosition(x, y);
```

- `x`, `y`:空间音频听器的 x/y 位置. 默认值是游戏画布的中心.

!!! note
仅限网络音频

## 声音实例 {#sound-instance}

### 创建声音实例 {#create-sound-instance}

将新声音添加到声音管理器中。

```js
var music = this.sound.add(key);
```

```js
var music = this.sound.add(key, config);
```

- `config`:包含默认声音设置的可选配置对象.

#### 声音实例配置 {#sound-instance-configuration}

```js
{
    mute: false,
    volume: 1,
    rate: 1,
    detune: 0,
    seek: 0,
    loop: false,
    delay: 0,

    // source of the spatial sound
    source: {
        x: 0,
        y: 0,
        z: 0,
        panningModel: 'equalpower',
        distanceModel: 'inverse',
        orientationX: 0,
        orientationY: 0,
        orientationZ: -1,
        refDistance: 1,
        maxDistance: 10000,
        rolloffFactor: 1,
        coneInnerAngle: 360,
        coneOuterAngle: 0,
        coneOuterGain: 0,
        follow: undefined
    }
}
```

- `source`:空间声音的来源
  - `x`,`y`:音频在右手笛卡尔坐标系统中的横向/纵向位置.
  - `z`:代表音频在右手笛卡尔坐标系统中的纵向(前后)位置.
  - `panningModel`:一个列出的数值,决定了用于将音频定位在3D空间的空间化算法.
    - `'equalpower'`
    - `'HRTF'`
  - `orientationX`,`orientationY`:音频源矢量在右手笛卡尔坐标系统中的横向/垂直位置.
  - `orientationZ`:代表音频源矢量在右手笛卡尔坐标系统中的纵向(前后)位置.
  - `refDistance` : 表示音频源离监听器更远时减小音量的参考距离的双值。 对于比此更大的音量,则会根据`rolloffFactor`和`distanceModel`来减小音量。
  - `maxDistance`:音频源与听器的最大距离,之后音量不再进一步缩小.
  - `rolloffFactor` : 描述源移离听器时音量减少的双值。 此值被所有距离模型使用 。
  - `coneInnerAngle`: 内有圆锥的角, 以度计, 其内无减量 。
  - `coneOuterAngle`:其外圆锥形的角,以度计,其体积将减少为恒值,由`coneOuterGain`属性定义.
  - `coneOuterGain`: `coneOuterAngle`属性定义的圆锥外的体积还原量,它的默认值是 `0`,意思是听不到声音。 `0`和 `1`之间的一个值。
  - `follow` : 设置此声音对象可自动跟踪此对象的 x/y 位置。 可以是 Phaser 游戏对象, Vec2 或任何暴露 公共 x/y 属性的 。

### 播放声音实例 {#play-sound-instance}

- 开始玩

  ```js
  music.play();
  ```

- 开始玩配置

  ```js
  music.play(config);
  ```

  - [config](#sound-instance-configuration)
- Stop

  ```js
  music.stop();
  ```

- Pause

  ```js
  music.pause();
  ```

- Resume

  ```js
  music.resume();
  ```

### 方法 {#methods}

#### 静音 {#mute}

- Set

  ```js
  music.setMute(mute); // mute: true/false
  // music.mute = mute;
  ```

- Get

  ```js
  var mute = music.mute;
  ```

#### 音量 {#volume}

- Set

  ```js
  music.setVolume(volume); // volume: 0 to 1
  // music.volume = volume;
  ```

- Get

  ```js
  var volume = music.volume;
  ```

#### 调试 {#detune}

设置 [cents](https://en.wikipedia.org/wiki/Cent_%28music%29) 中所有声音的全球调制。 值的范围为 - 1200 到 1200, 但我们建议设定为 50 。

- Set

  ```js
  music.setDetune(detune); // detune: -1200 to 1200
  // music.detune = detune;
  ```

- Get

  ```js
  var detune = music.detune;
  ```

#### 回放率 {#playback-rate}

- Set

  ```js
  music.setRate(rate); // rate: 1.0(normal speed), 0.5(half speed), 2.0(double speed)
  // music.rate = rate;
  ```

- Get

  ```js
  var rate = music.rate;
  ```

#### 寻求 {#seek-to}

- 寻求

  ```js
  music.setSeek(time); // seek: playback time
  // music.seek = seek;
  ```

- 获得当前播放时间

  ```js
  var time = music.seek; // return 0 when playback ends
  ```

#### 循环 {#loop}

- Set

  ```js
  music.setLoop(loop); // loop: true/false
  // music.loop = loop;
  ```

- Get

  ```js
  var loop = music.loop;
  ```

### 属性 {#properties}

- 持续时间: 此声音的持续时间

  ```js
  var duration = music.duration;
  ```

- 正在玩游戏

  ```js
  var isPlaying = music.isPlaying;
  ```

- 暂停

  ```js
  var isPaused = music.isPaused;
  ```

- 资源键

  ```js
  var key = music.key;
  ```

### 事件 {#events}

- 开始玩

  ```js
  music.once("play", function (music) {});
  ```

- 播放结束

  ```js
  music.once("complete", function (music) {});
  ```

- Looping

  ```js
  music.once("looped", function (music) {});
  ```

- Pause

  ```js
  music.once("pause", function (music) {});
  ```

- Resume

  ```js
  music.once("resume", function (music) {});
  ```

- Stop

  ```js
  music.once("stop", function (music) {});
  ```

- 设置哑弹

  ```js
  music.once("mute", function (music, mute) {});
  ```

- 设定音量

  ```js
  music.once("volume", function (music, volume) {});
  ```

- 设置调试

  ```js
  music.once("detune", function (music, detune) {});
  ```

- 设定播放率

  ```js
  music.once("rate", function (music, rate) {});
  ```

- 寻求

  ```js
  music.once("seek", function (music, time) {});
  ```

- 设置循环

  ```js
  music.once("loop", function (music, loop) {});
  ```

## 播放标记的声音 {#play-marked-sound}

播放结束时声音实例会被销毁 。

```js
this.sound.play(key, marker);
```

- `marker`:以名称为代表的音节标记,可选的起始时间,持续时间,以及配置对象.

### 标记 {#marker}

```js
{
    name: '',
    start: 0,
    duration: music.duration,
    config: {
        mute: false,
        volume: 1,
        rate: 1,
        detune: 0,
        seek: 0,
        loop: false,
        delay: 0
    }
}
```

## 声音实例中的标记 {#markers-in-sound-instance}

### 添加标记 {#add-marker}

```js
music.addMarker(marker);
```

[Marker](#marker)

### 播放标记的声音 {#play-marked-sound-1}

```js
music.play(markerName);
```

```js
music.play(markerName, config);
```

[config](#sound-instance-configuration)

## 音频图示 {#audio-sprite}

### 加载音频精灵 {#load-audio-sprite}

```js
scene.load.audioSprite(key, urls, markersConfig, config);
```

见[loader](/guide/concepts/loader#audio-sprite)

markersConfig 格式

```js
{
    resources: urls, // an array of audio files
    spritemap: {
        markerName0: {
            start: 0,
            end: 0
        },
        markerName1: {
            start: 0,
            end: 0
        }
        // ...
    }
}
```

### 播放声音 {#play-sound-1}

创建一个声音实例然后播放标记的段落, 当播放结束时, 此声音实例将被销毁 。

```js
this.sound.playAudioSprite(key, markerName, config);
```

[config](#sound-instance-configuration)

### 声音实例 {#sound-instance-1}

创建带有标记的音效实例 。

```js
var music = this.sound.addAudioSprite(key, config);
```

[config](#sound-instance-configuration)

### 播放声音实例 {#play-sound-instance-1}

```js
music.play(markerName);
```

```js
music.play(markerName, config);
```

[config](#sound-instance-configuration)

## 声音管理器 {#sound-manager}

### 静音 {#mute-1}

- Set

  ```js
  this.sound.setMute(mute); // mute: true/false
  // this.sound.mute = mute;
  ```

- Get

  ```js
  var mute = this.sound.mute;
  ```

### 音量 {#volume-1}

- Set

  ```js
  this.sound.setVolume(volume); // volume: 0 to 1
  // this.sound.volume = volume;
  ```

- Get

  ```js
  var volume = this.sound.volume;
  ```

### 调试 {#detune-1}

- Set

  ```js
  this.sound.setDetune(detune); // detune: -1200 to 1200
  // this.sound.detune = detune;
  ```

- Get

  ```js
  var detune = this.sound.detune;
  ```

### 回放率 {#playback-rate-1}

- Set

  ```js
  this.sound.setRate(rate); // rate: 1.0(normal speed), 0.5(half speed), 2.0(double speed)
  // this.sound.rate = rate;
  ```

- Get

  ```js
  var rate = this.sound.rate;
  ```

### 获取音乐实例 {#get-music-instance}

- 先按键

  ```js
  var music = this.sound.get(key); // music instance, or null
  ```

- 都按键

  ```js
  var musicArray = this.sound.getAll(key); // music instance, or null
  ```

- 都给我拿来

  ```js
  var musicArray = this.sound.getAll();
  ```

- 都玩起来

  ```js
  var musicArray = this.sound.getAllPlaying();
  ```

### 删除音乐实例 {#remove-music-instance}

- 以键删除

  ```js
  var removed = this.sound.removeByKey(key);
  ```

  - `removed`: 被移除的匹配声音对象的数量 。
- 删除全部

  ```js
  this.sound.removeAll();
  ```

### 停止音乐实例 {#stop-music-instance}

- 由键停车

  ```js
  var stopped = this.sound.stopByKey(key);
  ```

  - `stopped` : 有多少声音被停止.
- 都别闹了

  ```js
  this.sound.stopAll();
  ```

## 分析器 {#analyser}

Web Audio API具有从您的音频源提取频率,波形,以及其他数据的能力,然后可以用来创建[visualizations](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Visualizations_with_Web_Audio_API).

1. 创建分析器节点

   ```js
   var analyser = this.sound.context.createAnalyser();
   ```

2. 配置分析器节点

   ```js
   analyser.smoothingTimeConstant = 1;
   analyser.fftSize = 8192;
   analyser.minDecibels = -90;
   analyser.maxDecibels = -10;
   ```

   - `smoothingTimeConstant`:与最后的分析框架相伴的恒定值.
     - `0`(无时间平均)~`1`. 默认值为`0.8`.
   - `fftSize` : 窗口大小。
     - `32`, `64`, `128`, `256`, `512`, `1024`, `2048`, `4096`, `8192`, `16384`,和 `32768`默认值。 `2048`.
   - `minDecibels`:最小值_decibel_用于缩放FFT分析数据.
     - `0` dB 声音最大, `-10` dB 是一个第 10 个等。默认值是 `-100` dB
   - `maxDecibels`: 缩放FFT分析数据的最大值_decibel_值.
     - 默认值是 `-30` dB.
3. 设置分析器节点的来源
   - 全球积节点 - > 分析器节点

     ```js
     this.sound.masterVolumeNode.connect(analyser);
     ```

   - 声音实例 - > 分析器节点

     ```js
     music.volumeNode.connect(analyser);
     ```

4. 音频上下文的 Oput分析器节点

   ```js
   analyser.connect(this.sound.context.destination);
   ```

5. 创建输出数据数组

   ```js
   var dataArrayLength = analyser.frequencyBinCount;
   var dataArray = new Uint8Array(dataArrayLength);
   ```

6. 获取输出数据

   ```js
   analyser.getByteTimeDomainData(dataArray);
   ```

   - 获取输出数据

     ```js
     for (var i = 0; i < dataArrayLength; i++) {
       var data = dataArray[i];
     }
     ```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)
- [samme](https://github.com/samme)

---
