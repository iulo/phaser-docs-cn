# Phaser.Display.Canvas {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/display-canvas)

Scope: 
static
> 源码：[src/display/canvas/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/index.js#L7)  


## 静态函数 {#static-functions}

- [CanvasInterpolation](/api/namespace/display-canvas-canvasinterpolation)
- [CanvasPool](/api/namespace/display-canvas-canvaspool)
- [Smoothing](/api/namespace/display-canvas-smoothing)
## 静态函数 {#static-functions-1}

### TouchAction {#TouchAction}

#### \<static> TouchAction(canvas, [value]) {#static-touchactioncanvas-value}


**说明:**

设置画布样式上的触摸动作属性。 可用于禁用默认浏览器触摸动作 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| canvas | HTMLCanvasElement | 否 |  | 应用样式的画布元素 。 |
| value | string | 是 | "'none'" | 画布上设定的触摸动作值。 设定为 `none` 以禁用触摸动作 。 |


**返回值:** HTMLCanvasElement - 画布元素.


> 源码：[src/display/canvas/TouchAction.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/TouchAction.js#L7)  
引入版本：3.0.0


---

### UserSelect {#UserSelect}

#### \<static> UserSelect(canvas, [value]) {#static-userselectcanvas-value}


**说明:**

设置画布样式上的用户选择属性。可用于禁用默认浏览器选择动作。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| canvas | HTMLCanvasElement | 否 |  | 应用样式的画布元素 。 |
| value | string | 是 | "'none'" | 用户选择要在画布上设定的值。 设定为 `none` 以禁用默认浏览器文本选择和触摸点名 。 |


**返回值:** HTMLCanvasElement - 画布元素.


> 源码：[src/display/canvas/UserSelect.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/UserSelect.js#L7)  
引入版本：3.0.0


---

---
