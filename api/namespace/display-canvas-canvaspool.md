# Phaser.Display.Canvas.CanvasPool {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/display-canvas-canvaspool)

Scope: 
static
> 源码：[src/display/canvas/CanvasPool.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L16)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### create {#create}

#### \<static> create(parent, [width], [height], [canvasType], [selfParent]) {#static-createparent-width-height-canvastype-selfparent}


**说明:**

创建新的 Canvas DOM 元素,如果空闲,则从池中拉出。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| parent | * | 否 |  | 坎瓦斯天体的母体. |
| width | number | 是 | 1 | 坎瓦斯号的宽度. |
| height | number | 是 | 1 | 坎瓦斯人的高度。 |
| canvasType | number | 是 | "Phaser.CANVAS" | 风扇的型号,要么是`Phaser.CANVAS`,要么是`Phaser.WEBGL`. |
| selfParent | boolean | 是 | false | 使用生成的 Canvas 元素作为父元素 ? |


**返回值:** HTMLCanvasElement - 由池中创建或提取的画布元素 。


> 源码：[src/display/canvas/CanvasPool.js#L29](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L29)  
引入版本：3.0.0


---

### create2D {#create2D}

#### \<static> create2D(parent, [width], [height]) {#static-create2dparent-width-height}


**说明:**

创建新的 2D 坎瓦 DOM 元素,或者如果空闲的话从池中拉出一个。

这是`create`周围的方便包装器,它将`canvasType`强制到`Phaser.CANVAS`,确保返回的画布总是用于2D渲染上下文.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| parent | * | 否 |  | 坎瓦斯天体的母体. |
| width | number | 是 | 1 | 坎瓦斯号的宽度. |
| height | number | 是 | 1 | 坎瓦斯人的高度。 |


**返回值:** HTMLCanvasElement - 由池中创建或提取的画布元素 。


> 源码：[src/display/canvas/CanvasPool.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L91)  
引入版本：3.0.0


---

### createWebGL {#createWebGL}

#### \<static> createWebGL(parent, [width], [height]) {#static-createwebglparent-width-height}


**说明:**

创建新的 WebGL Canvas DOM 元素。

这是`create`周围的方便包装,将`canvasType`强制到`Phaser.WEBGL`. WebGL画布从不添加到游泳池,因为一旦设置了WebGL上下文的选项,它们就不能被更改,使得集合不适合它们.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| parent | * | 否 |  | 坎瓦斯天体的母体. |
| width | number | 是 | 1 | 坎瓦斯号的宽度. |
| height | number | 是 | 1 | 坎瓦斯人的高度。 |


**返回值:** HTMLCanvasElement - 创建的 WebGL画布.


> 源码：[src/display/canvas/CanvasPool.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L111)  
引入版本：3.0.0


---

### disableSmoothing {#disableSmoothing}

#### \<static> disableSmoothing() {#static-disablesmoothing}


**说明:**

禁用创建的任何新 Canvas 元素上的环境平滑 。


> 源码：[src/display/canvas/CanvasPool.js#L225](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L225)  
引入版本：3.0.0


---

### enableSmoothing {#enableSmoothing}

#### \<static> enableSmoothing() {#static-enablesmoothing}


**说明:**

启用创建的任何新 Canvas 元素上下文的平滑 。


> 源码：[src/display/canvas/CanvasPool.js#L236](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L236)  
引入版本：3.0.0


---

### first {#first}

#### \<static> first([canvasType]) {#static-firstcanvastype}


**说明:**

从泳池里拿到第一个免费帆布容器.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| canvasType | number | 是 | "Phaser.CANVAS" | 风扇的型号,要么是`Phaser.CANVAS`,要么是`Phaser.WEBGL`. |


**返回值:** HTMLCanvasElement - 如果需要WebGL帆布,或者游泳池没有免费帆布,则使用第一个免费帆布,或者`null`.


> 源码：[src/display/canvas/CanvasPool.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L132)  
引入版本：3.0.0


---

### free {#free}

#### \<static> free() {#static-free}


**说明:**

获取池中自由画布元素的总数。


**返回值:** number - 免费画布的数量 。


> 源码：[src/display/canvas/CanvasPool.js#L212](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L212)  
引入版本：3.0.0


---

### remove {#remove}

#### \<static> remove(parent) {#static-removeparent}


**说明:**

以父画为基础, 查看一张画布, 如果发现它会放回池中, 将它放出来重新使用。 画布的宽度和高度设定为 1, 而它的父属性无效 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | * | 否 | 画布或画布的母体可以自由使用. |


> 源码：[src/display/canvas/CanvasPool.js#L164](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L164)  
引入版本：3.0.0


---

### total {#total}

#### \<static> total() {#static-total}


**说明:**

获取池中已使用的画布元素的总数。


**返回值:** number - 旧画布的数量 。


> 源码：[src/display/canvas/CanvasPool.js#L189](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L189)  
引入版本：3.0.0


---

---
