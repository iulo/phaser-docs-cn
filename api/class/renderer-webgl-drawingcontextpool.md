# DrawingContextPool {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-drawingcontextpool)

一组画文

此类被 WebGLRender 内部用于管理绘图康文本。 它试图高效地重用绘图康文本。 当调用 `get` 时, 它会返回给定维度的绘图康文本, 使用以下优先级 :

1. 具有相同维度的备用绘图康特文.

2. 近期没有使用的备用绘图格式, 已调整大小 。

3. 新的绘图康特,在最大池大小范围内。

4. 最早的备用绘图机 重新尺寸

5. 一个新的绘图康特, 超过最大池大小 。

我们假设,一定规模的绘图格式有可能从帧到帧重复使用,因此我们试图保存这些格式,以便提高效率。

**构造函数**

`new DrawingContextPool(renderer, maxAge, maxPoolSize)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有这个绘图孔特普尔的渲染器. |
| maxAge | number | 否 | 集合绘图康特的最大年龄以毫秒计,之后它就有资格重新定型和再利用。 |
| maxPoolSize | number | 否 | 需要时, 池内可保留绘图的软最大数量。 池内可临时超过此限制 。 |

---


**作用域**: static

> 源码：[src/renderer/webgl/DrawingContextPool.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContextPool.js#L10)  
引入版本：4.0.0

## 公开成员 {#public-members}

### agePool {#agePool}

#### agePool: Array.\<[Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext)> {#agepool-arrayphaserrendererwebgldrawingcontext}


**说明:**

按年龄划分的绘图康特文库。 这是一系列最古老的绘图康特文库 。


> 源码：[src/renderer/webgl/DrawingContextPool.js#L69](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContextPool.js#L69)  
引入版本：4.0.0


---

### maxAge {#maxAge}

#### maxAge: number {#maxage-number}


**说明:**

绘图康特的最大年龄以毫秒计。 之后, 绘图康特可用于重定大小 。


> 源码：[src/renderer/webgl/DrawingContextPool.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContextPool.js#L48)  
引入版本：4.0.0


---

### maxPoolSize {#maxPoolSize}

#### maxPoolSize: number {#maxpoolsize-number}


**说明:**

要存储的绘图康文本的最大数量。 这不是一个硬限制, 但池将尝试重新使用绘图康文本, 而不是创建新的 。


> 源码：[src/renderer/webgl/DrawingContextPool.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContextPool.js#L58)  
引入版本：4.0.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrendererwebglwebglrenderer}


**说明:**

拥有这个绘图孔特普尔的渲染器.


> 源码：[src/renderer/webgl/DrawingContextPool.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContextPool.js#L39)  
引入版本：4.0.0


---

### sizePool {#sizePool}

#### sizePool: object {#sizepool-object}


**说明:**

按大小排列绘图连接池。这是带有`${width}x${height}`窗体键的对象。每个值都是绘图连接的数组。


> 源码：[src/renderer/webgl/DrawingContextPool.js#L79](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContextPool.js#L79)  
引入版本：4.0.0


---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(drawingContext) {#instance-adddrawingcontext}


**说明:**

向池中添加绘图康文本。此选项被绘图康文本用于表示其可用于再利用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 画孔图文以加于池. |


> 源码：[src/renderer/webgl/DrawingContextPool.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContextPool.js#L91)  
引入版本：4.0.0


---

### clear {#clear}

#### \<instance> clear() {#instance-clear}


**说明:**

清除绘图康特宝。 这将不破坏当前正在使用的任何绘图康特。


> 源码：[src/renderer/webgl/DrawingContextPool.js#L255](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContextPool.js#L255)  
引入版本：4.0.0


---

### get {#get}

#### \<instance> get([width], [height]) {#instance-getwidth-height}


**说明:**

返回所请求尺寸的绘图背景, 遵循池的优先级顺序: 精确大小的备用件、 旧的备用件重塑大小、 池限内新建的上下文、 最古老的备用件重塑, 或者最后新建的上下文超过池限。 如果省略宽度或高度, 则使用渲染器的当前尺寸。 两种值都会被夹在 渲染器的最大纹理大小 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 是 | 绘图康特的宽度 。 |
| height | number | 是 | 画画康特的高度. |


**返回值:** [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) - 画画康特文.


> 源码：[src/renderer/webgl/DrawingContextPool.js#L120](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContextPool.js#L120)  
引入版本：4.0.0


---

### prune {#prune}

#### \<instance> prune() {#instance-prune}


**说明:**

将绘图康特宝拖到最大池大小。 最旧的绘图康特将首先被销毁。 这将不会销毁任何正在使用的绘图康特 。


> 源码：[src/renderer/webgl/DrawingContextPool.js#L273](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContextPool.js#L273)  
引入版本：4.0.0


---

### setMaxAge {#setMaxAge}

#### \<instance> setMaxAge(maxAge) {#instance-setmaxagemaxage}


**说明:**

设定绘图康特的最大年龄,以毫秒计。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| maxAge | number | 否 | 绘图康特的最大年龄, 以毫秒计。 |


> 源码：[src/renderer/webgl/DrawingContextPool.js#L231](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContextPool.js#L231)  
引入版本：4.0.0


---

### setMaxPoolSize {#setMaxPoolSize}

#### \<instance> setMaxPoolSize(maxPoolSize) {#instance-setmaxpoolsizemaxpoolsize}


**说明:**

设置要存储的绘图康文本的最大数量。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| maxPoolSize | number | 否 | 要存储的绘图康特文本的最大数量 。 |


> 源码：[src/renderer/webgl/DrawingContextPool.js#L243](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContextPool.js#L243)  
引入版本：4.0.0


---

---
