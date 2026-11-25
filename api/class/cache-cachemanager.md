# CacheManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/cache-cachemanager)

快取管理器是Game 实例拥有和维护的全球缓存.

各种系统,例如文件加载器,都依赖此缓存来存储它们所装入的文件。 管理器本身不存储任何文件,而是拥有多个 BaseCache 例, 每种类型的文件各一个。 已建入缓存用于二进制文件、 位图字体、 JSON、 物理数据、 遮荫器、 音频、 视频、 文本、 HTML、 WaveFront OBJ、 tiemaps 和 XML 。 您也可以通过 `addCustom` 方法添加自定义缓存 。

缓存管理器通过`this.cache`在任意场景中都可以使用,并被所有场景共享.

**构造函数**

`new CacheManager(game)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 提到拥有这个缓存管理员的 Phaser.Game 实例 。 |

---


**作用域**: static

> 源码：[src/cache/CacheManager.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L11)  
引入版本：3.0.0

## 公开成员 {#public-members}

### atlas {#atlas}

#### atlas: [Phaser.Cache.BaseCache](/api/class/cache-basecache) {#atlas-phasercachebasecache}


**说明:**

一个缓存存储所有 Phaser 压缩纹理 Atlas 数据文件,一般通过加载器添加.


> 源码：[src/cache/CacheManager.js#L147](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L147)  
引入版本：4.0.0


---

### audio {#audio}

#### audio: [Phaser.Cache.BaseCache](/api/class/cache-basecache) {#audio-phasercachebasecache}


**说明:**

一个缓存存储所有非流式音频文件,一般通过加载器添加.


> 源码：[src/cache/CacheManager.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L92)  
引入版本：3.0.0


---

### binary {#binary}

#### binary: [Phaser.Cache.BaseCache](/api/class/cache-basecache) {#binary-phasercachebasecache}


**说明:**

一个缓存存储所有二进制文件, 通常通过加载器添加 。


> 源码：[src/cache/CacheManager.js#L46](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L46)  
引入版本：3.0.0


---

### bitmapFont {#bitmapFont}

#### bitmapFont: [Phaser.Cache.BaseCache](/api/class/cache-basecache) {#bitmapfont-phasercachebasecache}


**说明:**

一个缓存存储所有位图字体数据文件, 通常通过加载器添加。 只有字体数据存储在这个缓存中, 纹理是纹理管理器的一部分 。


> 源码：[src/cache/CacheManager.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L55)  
引入版本：3.0.0


---

### custom {#custom}

#### custom: Object.\<[Phaser.Cache.BaseCache](/api/class/cache-basecache)> {#custom-objectphasercachebasecache}


**说明:**

包含您自定义的 BaseCache 项的对象。 通过 `addCustom` 方法添加到此项 。


> 源码：[src/cache/CacheManager.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L156)  
引入版本：3.0.0


---

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

提到拥有这个缓存管理员的 Phaser.Game 实例 。


**访问权限:** 受保护


> 源码：[src/cache/CacheManager.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L36)  
引入版本：3.0.0


---

### html {#html}

#### html: [Phaser.Cache.BaseCache](/api/class/cache-basecache) {#html-phasercachebasecache}


**说明:**

一个缓存存储所有 html 文件, 通常通过加载器添加 。


> 源码：[src/cache/CacheManager.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L119)  
引入版本：3.12.0


---

### json {#json}

#### json: [Phaser.Cache.BaseCache](/api/class/cache-basecache) {#json-phasercachebasecache}


**说明:**

一个缓存存储所有 JSON 数据文件, 通常通过加载器添加 。


> 源码：[src/cache/CacheManager.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L65)  
引入版本：3.0.0


---

### physics {#physics}

#### physics: [Phaser.Cache.BaseCache](/api/class/cache-basecache) {#physics-phasercachebasecache}


**说明:**

缓存存储所有物理数据文件, 通常通过加载器添加 。


> 源码：[src/cache/CacheManager.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L74)  
引入版本：3.0.0


---

### shader {#shader}

#### shader: [Phaser.Cache.BaseCache](/api/class/cache-basecache) {#shader-phasercachebasecache}


**说明:**

一个缓存存储所有阴影源文件, 通常通过加载器添加 。


> 源码：[src/cache/CacheManager.js#L83](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L83)  
引入版本：3.0.0


---

### text {#text}

#### text: [Phaser.Cache.BaseCache](/api/class/cache-basecache) {#text-phasercachebasecache}


**说明:**

缓存存储所有文本文件, 通常通过加载器添加 。


> 源码：[src/cache/CacheManager.js#L110](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L110)  
引入版本：3.0.0


---

### tilemap {#tilemap}

#### tilemap: [Phaser.Cache.BaseCache](/api/class/cache-basecache) {#tilemap-phasercachebasecache}


**说明:**

缓存存储所有图案数据文件, 通常通过加载器添加。 只有数据存储在这个缓存中, 纹理是纹理管理器的一部分 。


> 源码：[src/cache/CacheManager.js#L128](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L128)  
引入版本：3.0.0


---

### video {#video}

#### video: [Phaser.Cache.BaseCache](/api/class/cache-basecache) {#video-phasercachebasecache}


**说明:**

一个缓存存储所有非流视频文件,一般通过加载器添加.


> 源码：[src/cache/CacheManager.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L101)  
引入版本：3.20.0


---

### xml {#xml}

#### xml: [Phaser.Cache.BaseCache](/api/class/cache-basecache) {#xml-phasercachebasecache}


**说明:**

一个缓存存储所有 xml 数据文件, 通常通过加载器添加 。


> 源码：[src/cache/CacheManager.js#L138](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L138)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### addCustom {#addCustom}

#### \<instance> addCustom(key) {#instance-addcustomkey}


**说明:**

添加自定义缓存以存储自己的文件。 缓存将在 `Cache.custom.key` 下可用。 缓存只有在键尚未使用时才会被创建 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 您自定义缓存中唯一的键 。 |


**返回值:** [Phaser.Cache.BaseCache](/api/class/cache-basecache) - 引用创建的 BaseCache 。 如果键已经使用, 则返回对现有缓存的引用 。


> 源码：[src/cache/CacheManager.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L169)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁所有内置的 BaseCaches 和所有自定义缓存, 然后取消它们的引用。 当游戏实例被销毁时自动调用 。


> 源码：[src/cache/CacheManager.js#L191](https://github.com/phaserjs/phaser/blob/v4.1.0/src/cache/CacheManager.js#L191)  
引入版本：3.0.0


---

---
