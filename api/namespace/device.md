# Phaser.Device {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/device)

Scope: 
static
> 源码：[src/device/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/index.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### Audio {#Audio}

#### Audio {#audio}


**说明:**

确定运行此 Phaser Game 实例的设备的音频播放能力。 这些值只在游戏启动序列中被读取并被覆盖, 然后被内部游戏系统引用, 并且可以在任意场景内通过 `this.sys.game.device.audio` 访问 。


> 源码：[src/device/Audio.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/Audio.js#L9)  
引入版本：3.0.0


---

### Browser {#Browser}

#### Browser {#browser}


**说明:**

确定运行此 Phaser Game 实例的浏览器类型和版本。 这些值只在游戏的启动序列中被读取并被覆盖。 然后被内部游戏系统引用, 并可供您通过 `this.sys.game.device.browser`从任意场景内访问 。


> 源码：[src/device/Browser.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/Browser.js#L9)  
引入版本：3.0.0


---

### CanvasFeatures {#CanvasFeatures}

#### CanvasFeatures {#canvasfeatures}


**说明:**

确定运行 Phaser Game 实例的浏览器的画布特性。 这些值在游戏的启动序列中只读且被覆盖。 然后被内部游戏系统引用, 并可供您通过 `this.sys.game.device.canvasFeatures` 从任意场景中访问 。


> 源码：[src/device/CanvasFeatures.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/CanvasFeatures.js#L9)  
引入版本：3.0.0


---

### Features {#Features}

#### Features {#features}


**说明:**

确定运行此 Phaser Game 实例的浏览器的特性。 这些值只在游戏的启动序列中被读取并被覆盖, 然后被内部游戏系统引用, 并可供您通过 `this.sys.game.device.features`从任意场景内访问 。


> 源码：[src/device/Features.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/Features.js#L11)  
引入版本：3.0.0


---

### Fullscreen {#Fullscreen}

#### Fullscreen {#fullscreen}


**说明:**

确定运行此 Phaser Game 实例的浏览器的全屏幕支持。 这些值在游戏的启动序列中只读且被覆盖, 然后被内部游戏系统引用, 并可供您通过 `this.sys.game.device.fullscreen` 从任意场景中访问 。


> 源码：[src/device/Fullscreen.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/Fullscreen.js#L7)  
引入版本：3.0.0


---

### Input {#Input}

#### Input {#input}


**说明:**

确定运行此 Phaser Game 实例的浏览器的输入支持。 这些值在游戏启动序列中只读, 并且被包含。 然后被内部游戏系统引用, 并且可供您通过 `this.sys.game.device.input`从任意场景内访问 。


> 源码：[src/device/Input.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/Input.js#L9)  
引入版本：3.0.0


---

### OS {#OS}

#### OS {#os}


**说明:**

确定运行此 Phaser Game 实例的设备的操作系统。 这些值在游戏的启动序列中只读且包含在内。 然后由内部游戏系统引用, 并可供您通过 `this.sys.game.device.os`从任意场景内访问 。


> 源码：[src/device/OS.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/OS.js#L7)  
引入版本：3.0.0


---

### Video {#Video}

#### Video {#video}


**说明:**

确定运行此 Phaser Game 实例的浏览器的视频支持 。

这些值在游戏启动时初始化，供只读访问。

然后通过内部游戏系统来参考,并可供您通过`this.sys.game.device.video`从任何场景内访问.


> 源码：[src/device/Video.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/Video.js#L9)  
引入版本：3.0.0


---

---
