# DrawingContext {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-drawingcontext)

DrawingContext

**构造函数**

`new DrawingContext(renderer, [options])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有这个背景的渲染器. |
| options | [Phaser.Types.Renderer.WebGL.RenderNodes.DrawingContextOptions](/api/typedef/types-renderer-webgl-rendernodes#drawingcontextoptions) | 是 | 这方面的选择。 |

---


**作用域**: static

> 源码：[src/renderer/webgl/DrawingContext.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L36)  
引入版本：4.0.0

## 公开成员 {#public-members}

### autoClear {#autoClear}

#### autoClear: number {#autoclear-number}


**说明:**

用于解析图解的帧缓冲器。 这是用于解析的缓冲器的掩码 : gl.COLOR_BUFFER_BIT, gl.DEPTH_BUFFL_BIT, gL.STENCIL_BUFFFER_Bit 。


> 源码：[src/renderer/webgl/DrawingContext.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L104)  
引入版本：4.0.0


---

### blendMode {#blendMode}

#### blendMode: number {#blendmode-number}


**说明:**

渲染时使用的混合模式。 这是用于渲染器 blendModes 阵列的索引。 检查速度比状态对象快 。


> 源码：[src/renderer/webgl/DrawingContext.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L90)  
引入版本：4.0.0


---

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#camera-phasercamerasscene2dcamera}


**说明:**

此上下文使用的摄像机。 使用 `setCamera` 设置此功能, 以确保视图矩阵更新 。 在渲染前确保此功能不是 `null` 。


> 源码：[src/renderer/webgl/DrawingContext.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L52)  
引入版本：4.0.0


---

### enableMipmap {#enableMipmap}

#### enableMipmap: boolean {#enablemipmap-boolean}


**说明:**

是否启用帧缓冲纹理上的 mipmaps, 如果存在的话。 游戏必须设置使用 mipmaps 才能工作 。


> 源码：[src/renderer/webgl/DrawingContext.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L156)  
引入版本：4.1.0


---

### framebuffer {#framebuffer}

#### framebuffer: [Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](/api/class/renderer-webgl-wrappers-webglframebufferwrapper) {#framebuffer-phaserrendererwebglwrapperswebglframebufferwrapper}


**说明:**

将持有帧缓冲器输出的 WebGLFramebofferWrapper 。 这可能包含画布 。


> 源码：[src/renderer/webgl/DrawingContext.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L135)  
引入版本：4.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

帧缓冲器的高度.


> 源码：[src/renderer/webgl/DrawingContext.js#L198](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L198)  
引入版本：4.0.0


---

### lastUsed {#lastUsed}

#### lastUsed: number {#lastused-number}


**说明:**

上次使用绘图康特。 用于确定上下文是否为池中再利用的候选条件 。


> 源码：[src/renderer/webgl/DrawingContext.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L178)  
引入版本：4.0.0


---

### pool {#pool}

#### pool: [Phaser.Renderer.WebGL.DrawingContextPool](/api/class/renderer-webgl-drawingcontextpool) {#pool-phaserrendererwebgldrawingcontextpool}


**说明:**

不再需要时返回的集合。 仅用于临时背景 。


> 源码：[src/renderer/webgl/DrawingContext.js#L167](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L167)  
引入版本：4.0.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrendererwebglwebglrenderer}


**说明:**

拥有这个背景的渲染器.


> 源码：[src/renderer/webgl/DrawingContext.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L43)  
引入版本：4.0.0


---

### state {#state}

#### state: [Phaser.Types.Renderer.WebGL.WebGLGlobalParameters](/api/typedef/types-renderer-webgl#webglglobalparameters) {#state-phasertypesrendererwebglwebglglobalparameters}


**说明:**

绘图连接的相关的 WebGL 状态。 包含帧缓冲器、 剪刀盒和视图 。


> 源码：[src/renderer/webgl/DrawingContext.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L66)  
引入版本：4.0.0


---

### texture {#texture}

#### texture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#texture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

将持有帧缓冲器输出的 WebGLTexture Wrapper 。 只有在 `useCanvas` 谓 `false`.


> 源码：[src/renderer/webgl/DrawingContext.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L145)  
引入版本：4.0.0


---

### useCanvas {#useCanvas}

#### useCanvas: boolean {#usecanvas-boolean}


**说明:**

是否使用画布作为帧缓冲器 。


> 源码：[src/renderer/webgl/DrawingContext.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L125)  
引入版本：4.0.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

帧缓冲器的宽度 。


> 源码：[src/renderer/webgl/DrawingContext.js#L189](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L189)  
引入版本：4.0.0


---

## 公开方法 {#public-methods}

### beginDraw {#beginDraw}

#### \<instance> beginDraw() {#instance-begindraw}


**说明:**

开始绘制绘图 Context 。

在渲染设置帧缓冲器和其他WebGL状态之前,应该先使用这个功能.


> 源码：[src/renderer/webgl/DrawingContext.js#L591](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L591)  
引入版本：4.0.0


---

### clear {#clear}

#### \<instance> clear([bits]) {#instance-clearbits}


**说明:**

清除帧缓冲器,这个会绑住帧缓冲器.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| bits | number | 是 | 用于清除的 WebGL缓冲位数的位表( 如 `gl.COLOR_BUFFER_BIT`, `gl.DEPTH_BUFFER_BIT`, `gl.STENCIL_BUFFER_BIT`) 。 默认为上下文的 `autoClear` 值 。 |


> 源码：[src/renderer/webgl/DrawingContext.js#L610](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L610)  
引入版本：4.0.0


---

### copy {#copy}

#### \<instance> copy(source) {#instance-copysource}


**说明:**

复制另一个绘图康特的状态 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 复制到的绘图康特文 。 |


> 源码：[src/renderer/webgl/DrawingContext.js#L314](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L314)  
引入版本：4.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁绘图协议及其资源。


> 源码：[src/renderer/webgl/DrawingContext.js#L631](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L631)  
引入版本：4.0.0


---

### getClone {#getClone}

#### \<instance> getClone([preserveAutoClear]) {#instance-getclonepreserveautoclear}


**说明:**

创建绘图康特的克隆。 这样做是为了临时使用而变异的, 然后丢弃 。

autoClear 设置被设定为虚假, 除非指定。 这是因为大多数克隆人参考了用于积累绘图操作的现有帧缓冲器 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| preserveAutoClear | boolean | 是 | false | 是否保留 autoClear 设置 。 |


**返回值:** [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) - 克隆的绘图康特文.


> 源码：[src/renderer/webgl/DrawingContext.js#L356](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L356)  
引入版本：4.0.0


---

### isLocked {#isLocked}

#### \<instance> isLocked() {#instance-islocked}


**说明:**

检查是否锁定绘图康特 。


**返回值:** boolean - 是否锁定绘图康特 。


> 源码：[src/renderer/webgl/DrawingContext.js#L579](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L579)  
引入版本：4.0.0


---

### lock {#lock}

#### \<instance> lock(key) {#instance-lockkey}


**说明:**

锁定绘图康文本用于使用。 这阻止 `release` 返回其池中, 直到使用合适的键调用 `unlock` 。 这用于临时绘图康文本, 可能返回池中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | any | 否 | 锁定绘图连接的键 。 |


> 源码：[src/renderer/webgl/DrawingContext.js#L536](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L536)  
引入版本：4.0.0


---

### release {#release}

#### \<instance> release() {#instance-release}


**说明:**

结束使用绘图康特。 这标志着上下文没有在使用, 因此不再需要其帧缓冲器和纹理, 并且可以随时清除。 这将完成任何未完成的批次 。

若画孔亭上无锁,而从池中出,则归其池.


> 源码：[src/renderer/webgl/DrawingContext.js#L514](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L514)  
引入版本：4.0.0


---

### resize {#resize}

#### \<instance> resize(width, height) {#instance-resizewidth-height}


**说明:**

调整绘图康特的大小 。

如果还没有帧缓冲器, 则在特定维度上会创建一个新的纹理和帧缓冲器。 如果帧缓冲器已经存在, 则会重新调整大小 。 剪刀框和视图会重新设置, 以匹配新的大小 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 帧缓冲器的新宽度 。 |
| height | number | 否 | 帧缓冲器的新高度. |


> 源码：[src/renderer/webgl/DrawingContext.js#L233](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L233)  
引入版本：4.0.0


---

### setAutoClear {#setAutoClear}

#### \<instance> setAutoClear(color, depth, stencil) {#instance-setautoclearcolor-depth-stencil}


**说明:**

设定缓冲器, 以在绘图康特语被使用时清除 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | boolean | 否 | 是否清除颜色缓冲 。 |
| depth | boolean | 否 | 是否清除深度缓冲 。 |
| stencil | boolean | 否 | 是否清除天线缓冲器 。 |


> 源码：[src/renderer/webgl/DrawingContext.js#L381](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L381)  
引入版本：4.0.0


---

### setBlendMode {#setBlendMode}

#### \<instance> setBlendMode(blendMode, [blendColor]) {#instance-setblendmodeblendmode-blendcolor}


**说明:**

设置绘图连接的混合模式 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| blendMode | number | 否 | 要设置的混合模式 。 |
| blendColor | Array.\<number> | 是 | 要设置的混合颜色。 这是由4个值组成的阵列: 红色、 绿色、 蓝色、 α 。 |


> 源码：[src/renderer/webgl/DrawingContext.js#L400](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L400)  
引入版本：4.0.0


---

### setCamera {#setCamera}

#### \<instance> setCamera(camera) {#instance-setcameracamera}


**说明:**

设定绘图康特的摄像机 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 摄像机要设定。 |


> 源码：[src/renderer/webgl/DrawingContext.js#L431](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L431)  
引入版本：4.0.0


---

### setClearColor {#setClearColor}

#### \<instance> setClearColor(r, g, b, a) {#instance-setclearcolorr-g-b-a}


**说明:**

设置绘图背景的清晰颜色。 如果颜色与当前清晰颜色相同, 则不修改 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| r | number | 否 | 颜色的红色部分要用它来清除 。 |
| g | number | 否 | 颜色的绿色成分要用它来清除. |
| b | number | 否 | 颜色的蓝色部分要用它来清除。 |
| a | number | 否 | 颜色的α部分要用它来清除. |


> 源码：[src/renderer/webgl/DrawingContext.js#L443](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L443)  
引入版本：4.0.0


---

### setScissorBox {#setScissorBox}

#### \<instance> setScissorBox(x, y, width, height) {#instance-setscissorboxx-y-width-height}


**说明:**

设置绘图康特文的剪刀框。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 剪刀盒的x坐标. |
| y | number | 否 | 剪刀盒的y坐标. |
| width | number | 否 | 剪刀盒的宽度 。 |
| height | number | 否 | 剪刀盒的高度 。 |


> 源码：[src/renderer/webgl/DrawingContext.js#L467](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L467)  
引入版本：4.0.0


---

### setScissorEnable {#setScissorEnable}

#### \<instance> setScissorEnable(enable) {#instance-setscissorenableenable}


**说明:**

启用或禁用绘图康特文本的剪刀框。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| enable | boolean | 否 | 是否启用剪刀框 。 |


> 源码：[src/renderer/webgl/DrawingContext.js#L485](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L485)  
引入版本：4.0.0


---

### unlock {#unlock}

#### \<instance> unlock(key, [release]) {#instance-unlockkey-release}


**说明:**

解锁绘图康特。 这样可以让 `release` 返回其池中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | any | 否 | 用此键解锁绘图康特。 这一定是用来锁定它的关键 。 |
| release | boolean | 是 | 是否立即发布绘图康特。 只有当没有其他锁定时才会发生 。 |


> 源码：[src/renderer/webgl/DrawingContext.js#L556](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L556)  
引入版本：4.0.0


---

### use {#use}

#### \<instance> use() {#instance-use}


**说明:**

开始使用绘图连接。 这将完成任何未完成的批次并运行任何 autoClear 。


> 源码：[src/renderer/webgl/DrawingContext.js#L497](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/DrawingContext.js#L497)  
引入版本：4.0.0


---

---
