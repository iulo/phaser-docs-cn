# Phaser.Display.Canvas.CanvasInterpolation {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/display-canvas-canvasinterpolation)

Scope: 
static
> 源码：[src/display/canvas/CanvasInterpolation.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasInterpolation.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setBicubic {#setBicubic}

#### \<static> setBicubic(canvas) {#static-setbicubiccanvas}


**说明:**

将给定的画布上的 CSS `image-rendering` 属性设置为 `auto` , 恢复默认浏览器行为。 这样浏览器在画布缩放时可以应用平滑( 典型的双立) 插值, 其边缘比较柔和, 更适合高分辨率的纹理或非像素艺术的内容 。 同时将 IE 专用的 `msInterpolationMode` 设置为 `bicubic` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| canvas | HTMLCanvasElement | 否 | 要设置样式的画布对象 。 |


**返回值:** HTMLCanvasElement - 画布


> 源码：[src/display/canvas/CanvasInterpolation.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasInterpolation.js#L49)  
引入版本：3.0.0


---

### setCrisp {#setCrisp}

#### \<static> setCrisp(canvas) {#static-setcrispcanvas}


**说明:**

设置 CSS 设置 `image-rendering` 属性在给定的画布上使用最近的邻(crisp)缩放。这可以禁用反变异功能,使每个像素都变成硬的块,这是像素艺术游戏的理想。多个供应商前置的值被按顺序应用,以确保交叉浏览器兼容性,包括Firefox()`-moz-crisp-edges`),歌剧(`-o-crisp-edges`),WebKit(英语:`-webkit-optimize-contrast`),和互联网浏览器(`msInterpolationMode: nearest-neighbor`).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| canvas | HTMLCanvasElement | 否 | 要设置样式的画布对象 。 |


**返回值:** HTMLCanvasElement - 画布


> 源码：[src/display/canvas/CanvasInterpolation.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasInterpolation.js#L21)  
引入版本：3.0.0


---

---
