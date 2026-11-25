# Phaser.Renderer.Snapshot {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/renderer-snapshot)

Scope: 
static
> 源码：[src/renderer/snapshot/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/snapshot/index.js#L7)  


## 静态函数 {#static-functions}

### Canvas {#Canvas}

#### \<static> Canvas(canvas, config) {#static-canvascanvas-config}


**说明:**

绘制画布显示的当前框架的快照。 根据配置, 它可以以三种模式之一运行: 单像素颜色取样、 局部区域捕获或全画布捕获 。

在像素模式下,读取给定(x,y)坐标的颜色,并立即用`Phaser.Display.Color`对象引用回调.

在区域或全捕获模式中,相关区域被编码为数据 URL,并被指定给一个新的图像对象。一旦图像被装入,就会以图像为参数引用Snapshot配置对象中提供的调用回调。如果图像未能装入,则仍然引用调用回调,但没有参数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| canvas | HTMLCanvasElement | 否 | 画布来拍一张照片 |
| config | [Phaser.Types.Renderer.Snapshot.SnapshotState](/api/typedef/types-renderer-snapshot#snapshotstate) | 否 | 即时配置对象 。 |


> 源码：[src/renderer/snapshot/CanvasSnapshot.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/snapshot/CanvasSnapshot.js#L11)  
引入版本：3.0.0


---

### WebGL {#WebGL}

#### \<static> WebGL(sourceContext, config) {#static-webglsourcecontext-config}


**说明:**

取出一个由 WebGL 画布显示的当前框架的快照,或者读取一个像素的颜色值,这取决于快照配置对象的 `getPixel` 属性.

捕获一个区域时,原始像素数据从 WebGL 上下文读取,并合成到一个临时画布,核算 WebGL 的反转Y轴,并可选地逆转预先多倍化的α. 画布然后被串装到数据 URL 并装入一个图像对象,一旦装入完成,就会传递到Snapshot配置对象定义的回调中.

在读取单个像素时,给定坐标的RGBA值直接通过`gl.readPixels`读取,并通过调用返回作为`Phaser.Display.Color`对象.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sourceContext | WebGLRenderingContext | 否 | 需要一览的 WebGL上下文 。 |
| config | [Phaser.Types.Renderer.Snapshot.SnapshotState](/api/typedef/types-renderer-snapshot#snapshotstate) | 否 | 即时配置对象 。 |


> 源码：[src/renderer/snapshot/WebGLSnapshot.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/snapshot/WebGLSnapshot.js#L11)  
引入版本：3.0.0


---

---
