# Phaser.Display.Canvas.Smoothing {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/display-canvas-smoothing)

Scope: 
static
> 源码：[src/display/canvas/Smoothing.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/Smoothing.js#L10)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### disable {#disable}

#### \<static> disable(context) {#static-disablecontext}


**说明:**

禁用给定上下文的图像平滑属性。 默认浏览器启用图像平滑, 这并不总是您想要的, 特别是在游戏中使用像素艺术时。 请注意, 将属性设置在上下文本身上, 这样任何绘制到上下文的图像都会受到影响 。 这将设置当前所有浏览器的属性, 但支持在先前的浏览器上, 特别是在移动上是补丁的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| context | CanvasRenderingContext2D \| WebGLRenderingContext | 否 | 禁用平滑的上下文 。 |


**返回值:** CanvasRenderingContext2D, WebGLRenderingContext - 提供的背景。


> 源码：[src/display/canvas/Smoothing.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/Smoothing.js#L80)  
引入版本：3.0.0


---

### enable {#enable}

#### \<static> enable(context) {#static-enablecontext}


**说明:**

启用给定上下文的图像平滑属性。 默认浏览器启用图像平滑, 这并不总是您想要的, 特别是在游戏中使用像素艺术时。 请注意, 将属性设置在上下文本身上, 这样任何绘制到上下文的图像都会受到影响 。 这将设置当前所有浏览器的属性, 但支持在先前的浏览器上, 特别是在移动上是补丁的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| context | CanvasRenderingContext2D \| WebGLRenderingContext | 否 | 使平滑化成为可能的上下文 。 |


**返回值:** CanvasRenderingContext2D, WebGLRenderingContext - 提供的背景。


> 源码：[src/display/canvas/Smoothing.js#L51](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/Smoothing.js#L51)  
引入版本：3.0.0


---

### getPrefix {#getPrefix}

#### \<static> getPrefix(context) {#static-getprefixcontext}


**说明:**

获取给定上下文使用的平滑启用的供应商前缀, 或设置无效 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| context | CanvasRenderingContext2D \| WebGLRenderingContext | 否 | 画布上下文要检查 。 |


**返回值:** string - 控制图像平滑的上下文(`imageSmoothingEnabled`或供应商前缀版本)上的财产名称,或者不支持的`null`。


> 源码：[src/display/canvas/Smoothing.js#L24](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/Smoothing.js#L24)  
引入版本：3.0.0


---

### isEnabled {#isEnabled}

#### \<static> isEnabled(context) {#static-isenabledcontext}


**说明:**

如果上下文允许图像平滑, 返回 `true`, 否则返回 `false`。 如果无法平滑前缀, 返回无效 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| context | CanvasRenderingContext2D \| WebGLRenderingContext | 否 | 需要检查的背景 。 |


**返回值:** boolean - 如果上下文允许平滑,则使用`true`,否则使用`false`。如果不支持,则使用`null`。


> 源码：[src/display/canvas/Smoothing.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/Smoothing.js#L109)  
引入版本：3.0.0


---

---
