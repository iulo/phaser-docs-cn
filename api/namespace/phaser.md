# Phaser {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/phaser)

Scope: 
global
> 源码：[src/phaser.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/phaser.js#L12)  


## 静态函数 {#static-functions}

- [Game](/api/class/game)
- [Scene](/api/class/scene)
## 静态函数 {#static-functions-1}

- [Actions](/api/namespace/actions)
- [Animations](/api/namespace/animations)
- [BlendModes](/api/namespace/blendmodes)
- [Cache](/api/namespace/cache)
- [Cameras](/api/namespace/cameras)
- [Core](/api/namespace/core)
- [Curves](/api/namespace/curves)
- [Data](/api/namespace/data)
- [Device](/api/namespace/device)
- [Display](/api/namespace/display)
- [DOM](/api/namespace/dom)
- [Events](/api/namespace/events)
- [Filters](/api/namespace/filters)
- [GameObjects](/api/namespace/gameobjects)
- [Geom](/api/namespace/geom)
- [Input](/api/namespace/input)
- [Loader](/api/namespace/loader)
- [Math](/api/namespace/math)
- [Physics](/api/namespace/physics)
- [Plugins](/api/namespace/plugins)
- [Renderer](/api/namespace/renderer)
- [Scale](/api/namespace/scale)
- [ScaleModes](/api/namespace/scalemodes)
- [Scenes](/api/namespace/scenes)
- [Sound](/api/namespace/sound)
- [Structs](/api/namespace/structs)
- [Textures](/api/namespace/textures)
- [Tilemaps](/api/namespace/tilemaps)
- [Time](/api/namespace/time)
- [TintModes](/api/namespace/tintmodes)
- [Tweens](/api/namespace/tweens)
- [Types](/api/namespace/types)
- [Utils](/api/namespace/utils)
## 静态函数 {#static-functions-2}

### AUTO {#AUTO}

#### AUTO: number {#auto-number}


**说明:**

如果浏览器有能力支持 WebGL, 此设置将自动检测。 如果是, 它会使用 WebGL 渲染器。 如果不是, 则会掉回 Canvas 渲染器 。


> 源码：[src/const.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/const.js#L39)  
引入版本：3.0.0


---

### CANVAS {#CANVAS}

#### CANVAS: number {#canvas-number}


**说明:**

强迫Phaser只使用Canvas 渲染器,无论浏览器是否支持WebGL.


> 源码：[src/const.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/const.js#L50)  
引入版本：3.0.0


---

### DOWN {#DOWN}

#### DOWN: number {#down-number}


**说明:**

方向常数代表向下运动或方向。用于物理、瓦片和其他与主方向配合的Phaser系统。


> 源码：[src/const.js#L118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/const.js#L118)  
引入版本：3.0.0


---

### FOREVER {#FOREVER}

#### FOREVER: number {#forever-number}


**说明:**

在Phaser中,值 -1 在许多情况下是“永远”的,这个康斯特允许您使用它来帮助您记住值在代码中在做什么.


> 源码：[src/const.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/const.js#L85)  
引入版本：3.0.0


---

### HEADLESS {#HEADLESS}

#### HEADLESS: number {#headless-number}


**说明:**

无头渲染器既不创建Canvas,也不创建WebGL 渲染器。然而,它仍然绝对依赖于 DOM 存在和可用。这个模式是用于单位测试的,而不是用于在服务器上运行Phaser,这是你不该做的。


> 源码：[src/const.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/const.js#L73)  
引入版本：3.0.0


---

### LEFT {#LEFT}

#### LEFT: number {#left-number}


**说明:**

方向常数代表左向运动或方向。用于物理、瓦片和其他与主方向配合的Phaser系统。


> 源码：[src/const.js#L129](https://github.com/phaserjs/phaser/blob/v4.1.0/src/const.js#L129)  
引入版本：3.0.0


---

### LOG_VERSION {#LOG_VERSION}

#### LOG_VERSION: string {#log_version-string}


**说明:**

Phaser 发布版本,显示在控制台.log头 URL中.


> 源码：[src/const.js#L25](https://github.com/phaserjs/phaser/blob/v4.1.0/src/const.js#L25)  
引入版本：3.87.0


---

### NONE {#NONE}

#### NONE: number {#none-number}


**说明:**

方向常数代表无方向或未设定方向。用于物理学和输入等各种Phaser系统,其中需要方向值,但无方向值。


> 源码：[src/const.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/const.js#L96)  
引入版本：3.0.0


---

### RIGHT {#RIGHT}

#### RIGHT: number {#right-number}


**说明:**

方向常数代表向右运动或方向。用于物理、瓦片和其他与主方向配合的Phaser系统。


> 源码：[src/const.js#L140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/const.js#L140)  
引入版本：3.0.0


---

### UP {#UP}

#### UP: number {#up-number}


**说明:**

方向常数代表向上运动或方向。用于物理、瓦片和其他与主方向配合的Phaser系统。


> 源码：[src/const.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/const.js#L107)  
引入版本：3.0.0


---

### VERSION {#VERSION}

#### VERSION: string {#version-string}


**说明:**

Phaser 发布版本


> 源码：[src/const.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/const.js#L15)  
引入版本：3.0.0


---

### WEBGL {#WEBGL}

#### WEBGL: number {#webgl-number}


**说明:**

强制 Phaser 使用 WebGL 渲染器。 如果浏览器不支持它, 则没有使用此设置的 Canvas 的倒置, 因此您应该将其设置在其中, 并向用户显示合适的消息 。


> 源码：[src/const.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/const.js#L61)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-3}

### DeviceConf {#DeviceConf}

#### DeviceConf {#deviceconf}


> 源码：[src/device/index.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/device/index.js#L17)  



---

## 静态函数 {#static-functions-4}

### CSSBlendModes {#CSSBlendModes}

#### CSSBlendModes: string {#cssblendmodes-string}


**说明:**

Phaser 混合模式到 CSS 混合模式地图.


> 源码：[src/gameobjects/domelement/CSSBlendModes.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/domelement/CSSBlendModes.js#L7)  
引入版本：3.12.0


---

---
