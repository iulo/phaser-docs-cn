# Device {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/device)

## Audio {#audio}

### \<static> Audio {#static-audio}


确定运行此 Phaser Game 实例的设备的音频回放能力 。
这些值在游戏的后缀序列中只读,并被包含在内.
然后通过内部游戏系统引用,并可供您访问
透过`this.sys.game.device.audio`从任何场景。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| audioData | boolean | 否 | 此设备能播放 HTML 音频标记吗 ? |
| dolby | boolean | 否 | 这个设备能播放EC-3 Dolby Digital Plus文件吗? |
| m4a | boolean | 否 | 此设备能播放 m4a 文件吗 ? |
| aac | boolean | 否 | 这个设备能播放 aac 文件吗? |
| flac | boolean | 否 | 这个设备能播放 flac 文件吗 ? |
| mp3 | boolean | 否 | 此设备能播放 mp3 文件吗 ? |
| ogg | boolean | 否 | 这个设备能播放ogg文件吗? |
| opus | boolean | 否 | 这个设备能播放 opus 文件吗 ? |
| wav | boolean | 否 | 这个设备能播放 wav 文件吗? |
| webAudio | boolean | 否 | 这个设备有Web音频 API吗? |
| webm | boolean | 否 | 此设备能播放 Webm 文件吗 ? |

**类型**: object

**Member of**: Phaser.Device
> 源码：[src/device/Audio.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/Audio.js#L9)  
引入版本：3.0.0

---

## Browser {#browser}

### \<static> Browser {#static-browser}


确定运行此 Phaser Game 实例的浏览器类型和版本 。
这些值在游戏的后缀序列中只读,并被包含在内.
然后通过内部游戏系统引用,并可供您访问
透过`this.sys.game.device.browser`从任何场景。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| chrome | boolean | 否 | 在 Chrome 中运行时设定为真 。 |
| edge | boolean | 否 | 如果运行在 Microsoft Edge 浏览器中, 则设定为真 。 |
| firefox | boolean | 否 | 如果运行在 Firefox 中, 则设定为真 。 |
| ie | boolean | 否 | 如果运行在 Internet Explorer 11 或更少(不是边缘), 设置为真 。 |
| mobileSafari | boolean | 否 | 如果在移动 Safari 中运行, 则设定为真实 。 |
| opera | boolean | 否 | 在 Opera 中运行时设置为真 。 |
| safari | boolean | 否 | 如果在萨法里运行, 则设定为真实 。 |
| silk | boolean | 否 | 如果运行在丝绸浏览器中, 则设定为真( 如在Amazon Kindle 上使用) 。 |
| trident | boolean | 否 | 如果运行一个三叉戟版的Internet Explorer( IE11 或更早), 则设定为真 。 |
| es2019 | boolean | 否 | 如果浏览器显示支持ES2019特性,则设定为真. |
| chromeVersion | number | 否 | 如果在 Chrome 中运行, 此选项将包含主要版本编号 。 |
| firefoxVersion | number | 否 | 如果在 Firefox 中运行, 则包含主要版本号 。 |
| ieVersion | number | 否 | 如果在 Internet Explorer 中运行, 则此选项将包含主要版本编号。 IE10 之外, 您应该使用浏览器. trident 和浏览器 。tridentVersion. |
| safariVersion | number | 否 | 如果运行在 Safari 中, 这将包含主要版本号 。 |
| tridentVersion | number | 否 | 如果运行在 Internet Explorer 11 中, 这将包含主要版本号。 请参看 QQlink http://msdn.microsoft.com/en-us/library/ie/ms537503(v=vs.85).aspx} |

**类型**: object

**Member of**: Phaser.Device
> 源码：[src/device/Browser.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/Browser.js#L9)  
引入版本：3.0.0

---

## CanvasFeatures {#canvasfeatures}

### \<static> CanvasFeatures {#static-canvasfeatures}


确定运行此 Phaser Game 实例的浏览器的画布特性 。
这些值在游戏的后缀序列中只读,并被包含在内.
然后通过内部游戏系统引用,并可供您访问
透过`this.sys.game.device.canvasFeatures`从任何场景。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| supportInverseAlpha | boolean | 否 | 如果浏览器支持反转的α, 则设定为真 。 |
| supportNewBlendModes | boolean | 否 | 如果浏览器支持新的画布混合模式, 则设定为真实 。 |

**类型**: object

**Member of**: Phaser.Device
> 源码：[src/device/CanvasFeatures.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/CanvasFeatures.js#L9)  
引入版本：3.0.0

---

## Features {#features}

### \<static> Features {#static-features}


确定运行此 Phaser Game 实例的浏览器的特性 。
这些值在游戏的后缀序列中只读,并被包含在内.
然后通过内部游戏系统引用,并可供您访问
透过`this.sys.game.device.features`从任何场景。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| canvas | boolean | 否 | 指定此浏览器中是否有 HTML5 Canvas API( CanvasRendering Context2D) 。 Canvas 渲染器需要运行 。 |
| canvasBitBltShift | boolean | 否 | 如果画布支持当源区域与目的区域重叠时, 将“ 复制” 比特Blt 本身为 True。 用于快速像素复制操作。 将使用 `null` 如果无法确定, `false` 打开 iOS 和不起作用的Safari。 |
| file | boolean | 否 | 指示文件、 文件阅读器、 文件列表和 Blob API 是否全部可用, 允许在浏览器内进行文件读取操作 。 |
| fileSystem | boolean | 否 | 指示是否可用的文件系统 API( requestFileSystem),允许沙盒本地文件存储访问 。 |
| getUserMedia | boolean | 否 | 显示是否有可用的 getUserMedia API。 用于访问相机和麦克风输入。 注意: Firefox( 低于 21) 的旧版本可能报告支持, 但实际操作不正确 。 |
| littleEndian | boolean | 否 | 显示设备是否使用小端字节排序。 只有在浏览器支持 TypedArray 时才会被检测。 如果无法确定端位, 将变为 `null` 。 |
| localStorage | boolean | 否 | 指出浏览器会话之间是否有持续使用的密钥值数据可用Web存储 localStorage API。 |
| pointerLock | boolean | 否 | 指示是否可用的指针锁 API,允许鼠标光标被隐藏并锁定到游戏画布上,用于第一人称样式输入. |
| stableSort | boolean | 否 | 表示浏览器的Array.sort执行是否稳定,意思是等元在排序后保留其原来的相对顺序. |
| support32bit | boolean | 否 | 指示设备是否支持32位像素使用 ArrayBuffer 和 键入数组视图(Uint8ClampedArray / Int32Array) 来操纵画布图像数据。需要小端字节排序 。 |
| vibration | boolean | 否 | 显示是否具备振动 API, 从而可以对支持的移动设备进行随机反馈 。 |
| webGL | boolean | 否 | 显示此浏览器中是否有 WebGL 。 WebGL 渲染器需要运行 。 |
| worker | boolean | 否 | 显示是否有Web Workers, 允许背景 JavaScript 执行在单独的线程上 。 |

**类型**: object

**Member of**: Phaser.Device
> 源码：[src/device/Features.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/Features.js#L11)  
引入版本：3.0.0

---

## Fullscreen {#fullscreen}

### \<static> Fullscreen {#static-fullscreen}


确定运行此 Phaser Game 实例的浏览器的全屏幕支持 。
这些值在游戏的后缀序列中只读,并被包含在内.
然后通过内部游戏系统引用,并可供您访问
透过`this.sys.game.device.fullscreen`从任何场景。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| available | boolean | 否 | 浏览器是否支持全屏 API ? |
| keyboard | boolean | 否 | 浏览器是否支持在全屏模式下访问键盘 ? |
| active | boolean | 否 | 浏览器目前是否处于全屏模式? 这是一个只读的获取器,用于检查文档上各种供应商前置的全屏元素属性 。 |
| cancel | string | 否 | 如果浏览器支持全屏 API,则此文件持有调用方法的名称,以便退出全屏模式. |
| request | string | 否 | 如果浏览器支持全屏 API,则持有调用 DOM 元素的方法名称,以便请求全屏模式. |

**类型**: object

**Member of**: Phaser.Device
> 源码：[src/device/Fullscreen.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/Fullscreen.js#L7)  
引入版本：3.0.0

---

## Input {#input}

### \<static> Input {#static-input}


确定运行此 Phaser Game 实例的浏览器的输入支持 。
这些值在游戏的后缀序列中只读,并被包含在内.
然后通过内部游戏系统引用,并可供您访问
透过`this.sys.game.device.input`从任何场景。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| wheelEvent | string | 否 | 浏览器支持的最现代轮/滚动事件类型 : `'wheel'` (DOM3), (中文(简体) ). `'mousewheel'` (legacy Chrome/IE/Safari),或 互联网档案馆的存档,存档日期2013-03-02. `'DOMMouseScroll'` (法尔福克斯传). `null` 如果不支持轮盘事件。 |
| gamepads | boolean | 否 | 是否在此浏览器中提供 Gamepad API (`navigator.getGamepads`), 允许读取 gamepad 输入 。 |
| mspointer | boolean | 否 | Microsoft Pointer API(`navigator.msPointerEnabled`或`navigator.pointerEnabled`)是否可用,用于在旧的IE/Edge浏览器上进行指针输入. |
| touch | boolean | 否 | 是否支持触摸输入,通过`ontouchstart`事件或`navigator.maxTouchPoints`检测. |

**类型**: object

**Member of**: Phaser.Device
> 源码：[src/device/Input.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/Input.js#L9)  
引入版本：3.0.0

---

## OS {#os}

### \<static> OS {#static-os}


确定运行此 Phaser Game 实例的设备的操作系统 。
这些值在游戏的后缀序列中只读,并被包含在内.
然后通过内部游戏系统引用,并可供您访问
透过`this.sys.game.device.os`从任何场景。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| android | boolean | 否 | 运行在Android上? |
| chromeOS | boolean | 否 | 运行在chromeOS上? |
| cordova | boolean | 否 | 游戏在Apache Cordova下进行吗? |
| crosswalk | boolean | 否 | 游戏是在Intel Crosswalk XDK下运行的吗? |
| desktop | boolean | 否 | 正在运行在桌面上吗 ? |
| ejecta | boolean | 否 | 游戏是在弹射下运行的吗? |
| electron | boolean | 否 | 游戏是在GitHub Electron下运行的吗? |
| iOS | boolean | 否 | 运行在iOS上? |
| iPad | boolean | 否 | 运行在iPad上? |
| iPhone | boolean | 否 | 运行在iPhone上? |
| kindle | boolean | 否 | 跑在亚马逊金德上? |
| linux | boolean | 否 | 运行在Linux? |
| macOS | boolean | 否 | 运行在macOS上? |
| node | boolean | 否 | 游戏是在Node.js下运行的吗? |
| nodeWebkit | boolean | 否 | 游戏是在节点-Webkit下运行的? |
| webApp | boolean | 否 | 设置为真实的, 如果运行为 WebApp, 即运行在 WebView 内 |
| windows | boolean | 否 | 正在运行在Windows上? |
| windowsPhone | boolean | 否 | 是在Windows手机上运行吗? |
| iOSVersion | number | 否 | 如果运行在 iOS 中, 这将包含主版本编号 。 |
| pixelRatio | number | 否 | 主机设备的像素比. |

**类型**: object

**Member of**: Phaser.Device
> 源码：[src/device/OS.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/OS.js#L7)  
引入版本：3.0.0

---

## Video {#video}

### \<static> Video {#static-video}


确定运行此 Phaser Game 实例的浏览器的视频支持 。

这些值在游戏的后缀序列中只读,并被包含在内.

然后通过内部游戏系统引用,并可供您访问
透过`this.sys.game.device.video`从任何场景。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| h264 | boolean | 否 | 这个设备能播放 h264 mp4 视频文件吗 ? |
| hls | boolean | 否 | 这个设备能播放hls视频文件吗?. |
| mov | boolean | 否 | 这个设备能播放 Mov 视频文件吗 ? |
| mp4 | boolean | 否 | 这个设备能播放 h264 mp4 视频文件吗 ? |
| m4v | boolean | 否 | 此设备能播放 m4v( 通常为mp4) 视频文件吗 ? |
| ogg | boolean | 否 | 这个设备能播放 ogg 视频文件吗? |
| vp9 | boolean | 否 | 此设备能播放 vp9 视频文件吗 ? |
| webm | boolean | 否 | 此设备能播放 Webm 视频文件吗 ? |
| hasRequestVideoFrame | boolean | 否 | 这个设备是否支持 `requestVideoFrameCallback` API ? |
| getVideoURL | function | 否 | 鉴于视频 URL 的 数组( 或 单个 URL 字符串) , 返回一个具有 `url` 和 `type` 属性的对象, 用于此浏览器可以播放的第一个条目, 或者如果没有支持任何提供的格式, 则返回 `null` 。 |

**类型**: object

**Member of**: Phaser.Device
> 源码：[src/device/Video.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/Video.js#L9)  
引入版本：3.0.0

---

---
