# Phaser.GameObjects.Components.Filters {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-filters)

Scope: 
static
> 源码：[src/gameobjects/components/Filters.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L11)  
引入版本：4.0.0

## 静态函数 {#static-functions}

### filterCamera {#filterCamera}

#### filterCamera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#filtercamera-phasercamerasscene2dcamera}


**说明:**

用于过滤器的摄像机。 您可以用它来改变过滤器的视角。 不需要使用此摄像机进行普通渲染 。

只有在使用 `enableFilters` 方法时,此选项才可用 。

**标签:**

 - webglOnly


> 源码：[src/gameobjects/components/Filters.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L58)  
引入版本：4.0.0


---

### filters {#filters}

#### filters: [Phaser.Types.GameObjects.FiltersInternalExternal](/api/typedef/types-gameobjects#filtersinternalexternal), null {#filters-phasertypesgameobjectsfiltersinternalexternal-null}


**说明:**

此游戏对象的过滤列表。 这是一个具有 `internal` 和 `external` 属性的对象。 每个列表都是 [Phaser.GameObjects.Components.FilterList](/api/class/gameobjects-components-filterlist) 对象 。

只有在使用 `enableFilters` 方法时,此选项才可用 。

**标签:**

 - webglOnly


> 源码：[src/gameobjects/components/Filters.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L73)  
引入版本：4.0.0


---

### filtersAutoFocus {#filtersAutoFocus}

#### filtersAutoFocus: boolean {#filtersautofocus-boolean}


**说明:**

`filterCamera`是否更新每个帧以聚焦游戏对象。 如果您想要手动控制摄像机, 请禁用此选项 。

**标签:**

 - webglOnly


> 源码：[src/gameobjects/components/Filters.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L125)  
引入版本：4.0.0


---

### filtersFocusContext {#filtersFocusContext}

#### filtersFocusContext: boolean {#filtersfocuscontext-boolean}


**说明:**

过滤器是否应该聚焦上下文,而不是试图聚焦游戏对象。 当启用过滤器时, 将自动启用此功能, 过滤器将覆盖没有明确界限的对象 。

这有效地设置了内部滤波器,以和外部滤波器一样的制法.

只有在启用 `filtersAutoFocus` 时才使用此选项 。

“ 文本” 是游戏对象被渲染的帧缓冲器。 这通常是主帧缓冲器, 但可能是另一个帧缓冲器。 如果游戏对象被多次渲染, 则甚至可以是多个不同的帧缓冲器 。

**标签:**

 - webglOnly


> 源码：[src/gameobjects/components/Filters.js#L138](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L138)  
引入版本：4.0.0


---

### filtersForceComposite {#filtersForceComposite}

#### filtersForceComposite: boolean {#filtersforcecomposite-boolean}


**说明:**

过滤器组件是否应该总是绘制到帧缓冲器上, 即使没有活动过滤器 。

**标签:**

 - webglOnly


> 源码：[src/gameobjects/components/Filters.js#L162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L162)  
引入版本：4.0.0


---

### maxFilterSize {#maxFilterSize}

#### maxFilterSize: [Phaser.Math.Vector2](/api/class/math-vector2) {#maxfiltersize-phasermathvector2}


**说明:**

底部滤波器纹理的最大尺寸。 滤波器在底部纹理渲染后可能使用更大的纹理。 根据硬件, WebGL 的最大纹理尺寸至少为4096 。 您可以设置这个下限来保存内存或防止重定大小 。

**标签:**

 - webglOnly


> 源码：[src/gameobjects/components/Filters.js#L112](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L112)  
引入版本：4.0.0


---

### renderFilters {#renderFilters}

#### renderFilters: boolean {#renderfilters-boolean}


**说明:**

是否在此游戏对象上打开任何过滤器 。 即使还没有过滤器, 默认情况下, 这也是 `true` 。 禁用此以跳过过滤器渲染 。

使用 `willRenderFilters()` 来查看是否有活动过滤器 。

**标签:**

 - webglOnly


> 源码：[src/gameobjects/components/Filters.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L97)  
引入版本：4.0.0


---

## 静态函数 {#static-functions-1}

### enableFilters {#enableFilters}

#### \<instance> enableFilters() {#instance-enablefilters}


**说明:**

启用此游戏对象可设置过滤器 。

如果您想要使用 `filterCamera` 和 `filters` 属性, 您需要调用此方法。 它会设置必要的数据结构。 您可以禁用 `renderFilters` 属性的过滤器渲染 。

这是 WebGL 唯一的功能。 如果无法使用, 它将提前返回 。

**标签:**

 - webglOnly


**返回值:** [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters) - 


> 源码：[src/gameobjects/components/Filters.js#L223](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L223)  
引入版本：4.0.0


---

### focusFilters {#focusFilters}

#### \<instance> focusFilters() {#instance-focusfilters}


**说明:**

聚焦滤镜摄像机。 此设定滤镜摄像机的大小和位置, 以匹配 Game Object。 如果启用 `filtersAutoFocus`, 则自动调用渲染 。

这将聚焦于 Game Object 的原始维度( 如果可用)。 如果 Game Objects 没有维度, 这将聚焦于上下文: 属于用于渲染 Game Objekt 的绘图康特的摄像机。 上下文焦点发生在渲染过程中, 因为上下文在此之前还不知道 。

**标签:**

 - webglOnly


**返回值:** [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters) - 


> 源码：[src/gameobjects/components/Filters.js#L455](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L455)  
引入版本：4.0.0


---

### focusFiltersOnCamera {#focusFiltersOnCamera}

#### \<instance> focusFiltersOnCamera(camera) {#instance-focusfiltersoncameracamera}


**说明:**

将滤波摄像机聚焦在特定的摄像机上。 `filtersFocusContext` 启用时, 内部使用此摄像机 。

**标签:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 专注的摄像机。 |


**返回值:** [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters) - 


> 源码：[src/gameobjects/components/Filters.js#L524](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L524)  
引入版本：4.0.0


---

### focusFiltersOverride {#focusFiltersOverride}

#### \<instance> focusFiltersOverride([x], [y], [width], [height]) {#instance-focusfiltersoverridex-y-width-height}


**说明:**

手动覆盖过滤摄像机的焦点。 这样您就可以手动设定过滤摄像机的大小和位置。 它会在调用时解除 `filtersAutoFocus` 。

摄像机会设置滚动,将游戏对象放置在指定宽度和高度的矩形内,例如,调用`focusFiltersOverride(400, 200, 800, 600)`会将摄像机聚焦于将对象中心100像素置于摄像机中心(即400x300)之上.

**标签:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 是 | 焦点点的x坐标,相对于过滤器大小。默认是中心。 |
| y | number | 是 | 焦点的y坐标,相对于过滤器大小。默认是中心。 |
| width | number | 是 | 焦点区域的宽度。 默认是过滤宽度 。 |
| height | number | 是 | 焦点区域的高度。 默认为过滤高度 。 |


**返回值:** [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters) - 


> 源码：[src/gameobjects/components/Filters.js#L554](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L554)  
引入版本：4.0.0


---

### renderWebGLFilters {#renderWebGLFilters}

#### \<instance> renderWebGLFilters(renderer, gameObject, drawingContext, [parentMatrix], [renderStep]) {#instance-renderwebglfiltersrenderer-gameobject-drawingcontext-parentmatrix-renderstep}


**说明:**

使用过滤器渲染此对象 。

这个函数的范围没有保证,所以它不是指`this`.

**标签:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 |  | 需要制作的WebGL 渲染器实例。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 正在渲染游戏对象 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 |  | 当前绘图背景 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 |  | 游戏对象的母矩阵, 如果它有的话 。 |
| renderStep | number | 是 | 0 | 游戏对象渲染过程列表中此函数的索引。 用于支持多个渲染函数 。 |


**返回值:** [Phaser.Types.GameObjects.RenderWebGLStep](/api/typedef/types-gameobjects#renderwebglstep) - 


> 源码：[src/gameobjects/components/Filters.js#L289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L289)  
引入版本：4.0.0


---

### setFiltersAutoFocus {#setFiltersAutoFocus}

#### \<instance> setFiltersAutoFocus(value) {#instance-setfiltersautofocusvalue}


**说明:**

设定过滤摄像机是否应该自动重聚焦于游戏对象的每个帧。设置 `filtersAutoFocus` 属性 。

**标签:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 是否应该更新每个框架的过滤器 。 |


**返回值:** [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters) - 


> 源码：[src/gameobjects/components/Filters.js#L651](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L651)  
引入版本：4.0.0


---

### setFiltersFocusContext {#setFiltersFocusContext}

#### \<instance> setFiltersFocusContext(value) {#instance-setfiltersfocuscontextvalue}


**说明:**

设定过滤器是否应该聚焦上下文。 设置 `filtersFocusContext` 属性 。

**标签:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 过滤器是否应该聚焦于上下文 。 |


**返回值:** [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters) - 


> 源码：[src/gameobjects/components/Filters.js#L668](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L668)  
引入版本：4.0.0


---

### setFiltersForceComposite {#setFiltersForceComposite}

#### \<instance> setFiltersForceComposite(value) {#instance-setfiltersforcecompositevalue}


**说明:**

设定过滤器是否总是绘制到帧缓冲器。 设置 `filtersForceComposite` 属性 。

**标签:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 即使没有活动过滤器,对象是否应该总是向帧缓冲器绘图 。 |


**返回值:** [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters) - 


> 源码：[src/gameobjects/components/Filters.js#L685](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L685)  
引入版本：4.0.0


---

### setFilterSize {#setFilterSize}

#### \<instance> setFilterSize(width, height) {#instance-setfiltersizewidth-height}


**说明:**

设置过滤摄像机的基数大小。 这是内部过滤器将绘制的纹理大小。 外部过滤器将绘制到上下文大小( 通常是游戏画布) 。

这通常是游戏对象的大小。 当游戏对象被渲染并启用 `filtersAutoFocus` 时, 自动设定。 关闭自动焦点可以手动设定 。

技术上,较大的帧器可能用于提供编程。这是用于“内部”渲染的末端帧器的大小 。

**标签:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 滤波纹理的基宽度 。 |
| height | number | 否 | 滤波纹理的基高度. |


**返回值:** [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters) - 


> 源码：[src/gameobjects/components/Filters.js#L615](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L615)  
引入版本：4.0.0


---

### setRenderFilters {#setRenderFilters}

#### \<instance> setRenderFilters(value) {#instance-setrenderfiltersvalue}


**说明:**

设定是否要渲染过滤器 。 设置 `renderFilters` 属性 。

**标签:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 是否应该打开过滤器 。 |


**返回值:** [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters) - 


> 源码：[src/gameobjects/components/Filters.js#L702](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L702)  
引入版本：4.0.0


---

### willRenderFilters {#willRenderFilters}

#### \<instance> willRenderFilters() {#instance-willrenderfilters}


**说明:**

此游戏对象是否将渲染过滤器。 如果它有活动过滤器, 以及 `renderFilters` 属性是否也是真实的, 则此特性是真实的 。

**标签:**

 - webglOnly


**返回值:** boolean - 游戏对象是否将渲染过滤器 。


> 源码：[src/gameobjects/components/Filters.js#L202](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Filters.js#L202)  
引入版本：4.0.0


---

---
