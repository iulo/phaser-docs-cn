# Shader {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-shader)

一个Shader游戏对象.

此游戏对象允许您在显示列表中轻松添加带有自身阴影的四进制, 并像您一样操纵其它游戏对象, 包括缩放、 旋转、 定位和添加到容器中。 阴影可以被交互并用于输入事件。 也可以在过滤器中用于创建视觉惊人的效果 。

它通过创建自定义的 RenderNode 来工作, 它运行自定义的着色器程序来绘制一个四边形。 着色器程序可以从阴影缓存中加载, 或者作为字符串提供线内程序 。

请参看Phaser实例 GitHub Repo , 以动态方式加载和创建着色器的几个实例 。

由于其工作方式, 您不能直接改变一个 Shader 的α 。 它应该通过 cound 本身 的 shader 代码处理 。

默认情况下, 阴影罩会自动设置一个名为 `uProjectionMatrix`的制服。 您可以使用阴影罩每次生成时运行的 Shader 配置对象中的 `setupUniforms` 方法来控制额外的制服 。

阴影是独立的: 完成任何当前渲染批次, 并自己运行一次。 由于需要抽取, 请稍加使用。 如果您需要完整的批次自定义阴影, 请查看使用自定义的 RenderNode 。 然而, 对于背景效果或特殊遮罩效果, 效果极为有效 。

注:在阴影码中使用纹理坐标时要小心。内置变量`gl_FragCoord`和默认的统一`outTexCoord`都使用WebGL坐标,这些坐标是左下角的`0,0`。此外,`gl_FragCoord`说它位于“窗口相对”坐标中。但这实际上与帧缓冲器大小相对。

**构造函数**

`new Shader(scene, config, [x], [y], [width], [height], [textures])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 |  | 此游戏对象所属景点 。 |
| config | string \| [Phaser.Types.GameObjects.Shader.ShaderQuadConfig](/api/typedef/types-gameobjects-shader#shaderquadconfig) | 否 |  | 用于此 Shader 的配置对象。 它也可以是阴影缓存中对应的着色器的键, 它将在新配置对象中用作 `fragmentKey` 。 |
| x | number | 是 | 0 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 此游戏对象在世界的垂直位置 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |
| textures | Array.\<string> \| Array.\<[Phaser.Textures.Texture](/api/class/textures-texture)> | 是 |  | 着色器使用的纹理, 如果有的话。 如果您打算稍后定义纹理, 请使用 `'__DEFAULT'` 作为占位符, 以避免初始化错误 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.GetBounds](/api/namespace/gameobjects-components-getbounds)  
> [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/shader/Shader.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L17)  
引入版本：3.17.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode):**


 - [blendMode](/api/namespace/gameobjects-components-blendmode#blendMode)





**From [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize):**


 - [displayHeight](/api/namespace/gameobjects-components-computedsize#displayHeight)
 - [displayWidth](/api/namespace/gameobjects-components-computedsize#displayWidth)
 - [height](/api/namespace/gameobjects-components-computedsize#height)
 - [width](/api/namespace/gameobjects-components-computedsize#width)





**From [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth):**


 - [depth](/api/namespace/gameobjects-components-depth#depth)





**From [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters):**


 - [filterCamera](/api/namespace/gameobjects-components-filters#filterCamera)
 - [filters](/api/namespace/gameobjects-components-filters#filters)
 - [filtersAutoFocus](/api/namespace/gameobjects-components-filters#filtersAutoFocus)
 - [filtersFocusContext](/api/namespace/gameobjects-components-filters#filtersFocusContext)
 - [filtersForceComposite](/api/namespace/gameobjects-components-filters#filtersForceComposite)
 - [maxFilterSize](/api/namespace/gameobjects-components-filters#maxFilterSize)
 - [renderFilters](/api/namespace/gameobjects-components-filters#renderFilters)





**From [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin):**


 - [displayOriginX](/api/namespace/gameobjects-components-origin#displayOriginX)
 - [displayOriginY](/api/namespace/gameobjects-components-origin#displayOriginY)
 - [originX](/api/namespace/gameobjects-components-origin#originX)
 - [originY](/api/namespace/gameobjects-components-origin#originY)





**From [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor):**


 - [scrollFactorX](/api/namespace/gameobjects-components-scrollfactor#scrollFactorX)
 - [scrollFactorY](/api/namespace/gameobjects-components-scrollfactor#scrollFactorY)





**From [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform):**


 - [angle](/api/namespace/gameobjects-components-transform#angle)
 - [hasTransformComponent](/api/namespace/gameobjects-components-transform#hasTransformComponent)
 - [rotation](/api/namespace/gameobjects-components-transform#rotation)
 - [scale](/api/namespace/gameobjects-components-transform#scale)
 - [scaleX](/api/namespace/gameobjects-components-transform#scaleX)
 - [scaleY](/api/namespace/gameobjects-components-transform#scaleY)
 - [w](/api/namespace/gameobjects-components-transform#w)
 - [x](/api/namespace/gameobjects-components-transform#x)
 - [y](/api/namespace/gameobjects-components-transform#y)
 - [z](/api/namespace/gameobjects-components-transform#z)





**From [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible):**


 - [visible](/api/namespace/gameobjects-components-visible#visible)





**From [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject):**


 - [active](/api/class/gameobjects-gameobject#active)
 - [body](/api/class/gameobjects-gameobject#body)
 - [cameraFilter](/api/class/gameobjects-gameobject#cameraFilter)
 - [data](/api/class/gameobjects-gameobject#data)
 - [displayList](/api/class/gameobjects-gameobject#displayList)
 - [ignoreDestroy](/api/class/gameobjects-gameobject#ignoreDestroy)
 - [input](/api/class/gameobjects-gameobject#input)
 - [isDestroyed](/api/class/gameobjects-gameobject#isDestroyed)
 - [name](/api/class/gameobjects-gameobject#name)
 - [parentContainer](/api/class/gameobjects-gameobject#parentContainer)
 - [renderFlags](/api/class/gameobjects-gameobject#renderFlags)
 - [scene](/api/class/gameobjects-gameobject#scene)
 - [state](/api/class/gameobjects-gameobject#state)
 - [tabIndex](/api/class/gameobjects-gameobject#tabIndex)
 - [type](/api/class/gameobjects-gameobject#type)
 - [vertexRoundMode](/api/class/gameobjects-gameobject#vertexRoundMode)




---

## 公开成员 {#public-members}

### drawingContext {#drawingContext}

#### drawingContext: [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) {#drawingcontext-phaserrendererwebgldrawingcontext}


**说明:**

包含向着色器渲染的帧缓冲器和纹理的绘图上下文。 只有当着色器向纹理渲染时才会设置此上下文 。


> 源码：[src/gameobjects/shader/Shader.js#L166](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L166)  
引入版本：4.0.0


---

### glTexture {#glTexture}

#### glTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#gltexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

引用此 Shader 正在渲染的 WebGLTexture Wrapper 。 此属性只有在您调用 `Shader.setRenderToTexture` 时才设定 。


> 源码：[src/gameobjects/shader/Shader.js#L176](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L176)  
引入版本：3.19.0


---

### renderNode {#renderNode}

#### renderNode: [Phaser.Renderer.WebGL.RenderNodes.ShaderQuad](/api/class/renderer-webgl-rendernodes-shaderquad) {#rendernode-phaserrendererwebglrendernodesshaderquad}


**说明:**

着色器用来渲染的基质RenderNode对象.


> 源码：[src/gameobjects/shader/Shader.js#L144](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L144)  
引入版本：4.0.0


---

### renderToTexture {#renderToTexture}

#### renderToTexture: boolean {#rendertotexture-boolean}


**说明:**

显示此阴影是否被设定为向纹理而不是显示列表的旗帜 。

如果你把`Shader.setRenderToTexture`叫做`true`, 否则就是`false`.

显示列表中显示的纹理(_D) 。


> 源码：[src/gameobjects/shader/Shader.js#L186](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L186)  
引入版本：3.19.0


---

### texture {#texture}

#### texture: [Phaser.Textures.Texture](/api/class/textures-texture) {#texture-phasertexturestexture}


**说明:**

参考了此 Shader 的纹理管理器中存储的 Phaser.Textures.Texture 。

只有在您用键调用 `Shader.setRenderToTexture` 时, 才设置此属性, 否则它就是 `null` 。


> 源码：[src/gameobjects/shader/Shader.js#L200](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L200)  
引入版本：3.19.0


---

### textureCoordinateBottomLeft {#textureCoordinateBottomLeft}

#### textureCoordinateBottomLeft: [Phaser.Math.Vector2](/api/class/math-vector2) {#texturecoordinatebottomleft-phasermathvector2}


**说明:**

着色器左下方的纹理坐标。 默认情况下, 设置为 0 。 它使用 WebGL 纹理坐标 。


> 源码：[src/gameobjects/shader/Shader.js#L231](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L231)  
引入版本：4.0.0


---

### textureCoordinateBottomRight {#textureCoordinateBottomRight}

#### textureCoordinateBottomRight: [Phaser.Math.Vector2](/api/class/math-vector2) {#texturecoordinatebottomright-phasermathvector2}


**说明:**

着色器的右下方纹理坐标。 默认情况下, 设置为 1,0。 它使用 WebGL 纹理坐标 。


> 源码：[src/gameobjects/shader/Shader.js#L241](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L241)  
引入版本：4.0.0


---

### textureCoordinateTopLeft {#textureCoordinateTopLeft}

#### textureCoordinateTopLeft: [Phaser.Math.Vector2](/api/class/math-vector2) {#texturecoordinatetopleft-phasermathvector2}


**说明:**

着色器左上方的纹理坐标。 默认情况下, 设置为 0, 1。 它使用 WebGL 纹理坐标 。


> 源码：[src/gameobjects/shader/Shader.js#L211](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L211)  
引入版本：4.0.0


---

### textureCoordinateTopRight {#textureCoordinateTopRight}

#### textureCoordinateTopRight: [Phaser.Math.Vector2](/api/class/math-vector2) {#texturecoordinatetopright-phasermathvector2}


**说明:**

着色器的右上方纹理坐标。 默认情况下, 设置为 1, 使用 WebGL 纹理坐标 。


> 源码：[src/gameobjects/shader/Shader.js#L221](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L221)  
引入版本：4.0.0


---

### textures {#textures}

#### textures: Array.\<[Phaser.Textures.Texture](/api/class/textures-texture)> {#textures-arrayphasertexturestexture}


**说明:**

着色器使用的纹理。 当着色器被制成时, 这些纹理单位将分配到 0 到 N, 而 N 是 `textures.length - 1` 。


> 源码：[src/gameobjects/shader/Shader.js#L133](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L133)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Events.EventEmitter](/api/class/events-eventemitter):**


 - [addListener](/api/class/events-eventemitter#addListener)
 - [emit](/api/class/events-eventemitter#emit)
 - [eventNames](/api/class/events-eventemitter#eventNames)
 - [listenerCount](/api/class/events-eventemitter#listenerCount)
 - [listeners](/api/class/events-eventemitter#listeners)
 - [off](/api/class/events-eventemitter#off)
 - [on](/api/class/events-eventemitter#on)
 - [once](/api/class/events-eventemitter#once)
 - [removeAllListeners](/api/class/events-eventemitter#removeAllListeners)
 - [removeListener](/api/class/events-eventemitter#removeListener)
 - [shutdown](/api/class/events-eventemitter#shutdown)





**From [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode):**


 - [setBlendMode](/api/namespace/gameobjects-components-blendmode#setBlendMode)





**From [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize):**


 - [setDisplaySize](/api/namespace/gameobjects-components-computedsize#setDisplaySize)
 - [setSize](/api/namespace/gameobjects-components-computedsize#setSize)





**From [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth):**


 - [setAbove](/api/namespace/gameobjects-components-depth#setAbove)
 - [setBelow](/api/namespace/gameobjects-components-depth#setBelow)
 - [setDepth](/api/namespace/gameobjects-components-depth#setDepth)
 - [setToBack](/api/namespace/gameobjects-components-depth#setToBack)
 - [setToTop](/api/namespace/gameobjects-components-depth#setToTop)





**From [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters):**


 - [enableFilters](/api/namespace/gameobjects-components-filters#enableFilters)
 - [focusFilters](/api/namespace/gameobjects-components-filters#focusFilters)
 - [focusFiltersOnCamera](/api/namespace/gameobjects-components-filters#focusFiltersOnCamera)
 - [focusFiltersOverride](/api/namespace/gameobjects-components-filters#focusFiltersOverride)
 - [renderWebGLFilters](/api/namespace/gameobjects-components-filters#renderWebGLFilters)
 - [setFiltersAutoFocus](/api/namespace/gameobjects-components-filters#setFiltersAutoFocus)
 - [setFiltersFocusContext](/api/namespace/gameobjects-components-filters#setFiltersFocusContext)
 - [setFiltersForceComposite](/api/namespace/gameobjects-components-filters#setFiltersForceComposite)
 - [setFilterSize](/api/namespace/gameobjects-components-filters#setFilterSize)
 - [setRenderFilters](/api/namespace/gameobjects-components-filters#setRenderFilters)
 - [willRenderFilters](/api/namespace/gameobjects-components-filters#willRenderFilters)





**From [Phaser.GameObjects.Components.GetBounds](/api/namespace/gameobjects-components-getbounds):**


 - [getBottomCenter](/api/namespace/gameobjects-components-getbounds#getBottomCenter)
 - [getBottomLeft](/api/namespace/gameobjects-components-getbounds#getBottomLeft)
 - [getBottomRight](/api/namespace/gameobjects-components-getbounds#getBottomRight)
 - [getBounds](/api/namespace/gameobjects-components-getbounds#getBounds)
 - [getCenter](/api/namespace/gameobjects-components-getbounds#getCenter)
 - [getLeftCenter](/api/namespace/gameobjects-components-getbounds#getLeftCenter)
 - [getRightCenter](/api/namespace/gameobjects-components-getbounds#getRightCenter)
 - [getTopCenter](/api/namespace/gameobjects-components-getbounds#getTopCenter)
 - [getTopLeft](/api/namespace/gameobjects-components-getbounds#getTopLeft)
 - [getTopRight](/api/namespace/gameobjects-components-getbounds#getTopRight)





**From [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin):**


 - [setDisplayOrigin](/api/namespace/gameobjects-components-origin#setDisplayOrigin)
 - [setOrigin](/api/namespace/gameobjects-components-origin#setOrigin)
 - [setOriginFromFrame](/api/namespace/gameobjects-components-origin#setOriginFromFrame)
 - [updateDisplayOrigin](/api/namespace/gameobjects-components-origin#updateDisplayOrigin)





**From [Phaser.GameObjects.Components.RenderSteps](/api/namespace/gameobjects-components-rendersteps):**


 - [addRenderStep](/api/namespace/gameobjects-components-rendersteps#addRenderStep)
 - [renderWebGLStep](/api/namespace/gameobjects-components-rendersteps#renderWebGLStep)





**From [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor):**


 - [setScrollFactor](/api/namespace/gameobjects-components-scrollfactor#setScrollFactor)





**From [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform):**


 - [copyPosition](/api/namespace/gameobjects-components-transform#copyPosition)
 - [getLocalPoint](/api/namespace/gameobjects-components-transform#getLocalPoint)
 - [getLocalTransformMatrix](/api/namespace/gameobjects-components-transform#getLocalTransformMatrix)
 - [getParentRotation](/api/namespace/gameobjects-components-transform#getParentRotation)
 - [getWorldPoint](/api/namespace/gameobjects-components-transform#getWorldPoint)
 - [getWorldTransformMatrix](/api/namespace/gameobjects-components-transform#getWorldTransformMatrix)
 - [setAngle](/api/namespace/gameobjects-components-transform#setAngle)
 - [setPosition](/api/namespace/gameobjects-components-transform#setPosition)
 - [setRandomPosition](/api/namespace/gameobjects-components-transform#setRandomPosition)
 - [setRotation](/api/namespace/gameobjects-components-transform#setRotation)
 - [setScale](/api/namespace/gameobjects-components-transform#setScale)
 - [setW](/api/namespace/gameobjects-components-transform#setW)
 - [setX](/api/namespace/gameobjects-components-transform#setX)
 - [setY](/api/namespace/gameobjects-components-transform#setY)
 - [setZ](/api/namespace/gameobjects-components-transform#setZ)





**From [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible):**


 - [setVisible](/api/namespace/gameobjects-components-visible#setVisible)





**From [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject):**


 - [addedToScene](/api/class/gameobjects-gameobject#addedToScene)
 - [addToDisplayList](/api/class/gameobjects-gameobject#addToDisplayList)
 - [addToUpdateList](/api/class/gameobjects-gameobject#addToUpdateList)
 - [destroy](/api/class/gameobjects-gameobject#destroy)
 - [disableInteractive](/api/class/gameobjects-gameobject#disableInteractive)
 - [getData](/api/class/gameobjects-gameobject#getData)
 - [getDisplayList](/api/class/gameobjects-gameobject#getDisplayList)
 - [getIndexList](/api/class/gameobjects-gameobject#getIndexList)
 - [incData](/api/class/gameobjects-gameobject#incData)
 - [removedFromScene](/api/class/gameobjects-gameobject#removedFromScene)
 - [removeFromDisplayList](/api/class/gameobjects-gameobject#removeFromDisplayList)
 - [removeFromUpdateList](/api/class/gameobjects-gameobject#removeFromUpdateList)
 - [removeInteractive](/api/class/gameobjects-gameobject#removeInteractive)
 - [setActive](/api/class/gameobjects-gameobject#setActive)
 - [setData](/api/class/gameobjects-gameobject#setData)
 - [setDataEnabled](/api/class/gameobjects-gameobject#setDataEnabled)
 - [setInteractive](/api/class/gameobjects-gameobject#setInteractive)
 - [setName](/api/class/gameobjects-gameobject#setName)
 - [setState](/api/class/gameobjects-gameobject#setState)
 - [setVertexRoundMode](/api/class/gameobjects-gameobject#setVertexRoundMode)
 - [toggleData](/api/class/gameobjects-gameobject#toggleData)
 - [toJSON](/api/class/gameobjects-gameobject#toJSON)
 - [update](/api/class/gameobjects-gameobject#update)
 - [willRender](/api/class/gameobjects-gameobject#willRender)
 - [willRoundVertices](/api/class/gameobjects-gameobject#willRoundVertices)




---

## 公开方法 {#public-methods}

### getUniform {#getUniform}

#### \<instance> getUniform(name) {#instance-getuniformname}


**说明:**

从渲染节点返回一个制服的当前值。这个值实际上被复制到所有使用它的遮蔽器。修改非原始值,如数组和对象,将修改原始值。

一般最好在阴影配置对象中使用`setupUniforms`功能,在改变制服时设定统一值,这种方法是本着读回值的精神提供的.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 服名以得之. |


**返回值:** any - 制服的价值.


> 源码：[src/gameobjects/shader/Shader.js#L257](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L257)  
引入版本：4.0.0


---

### preDestroy {#preDestroy}

#### \<instance> preDestroy() {#instance-predestroy}


**说明:**

销毁对象时调用的内部处理函数。


**访问权限:** 受保护


> 源码：[src/gameobjects/shader/Shader.js#L582](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L582)  
引入版本：3.17.0


---

### renderImmediate {#renderImmediate}

#### \<instance> renderImmediate() {#instance-renderimmediate}


**说明:**

立即将阴影涂上。 这对显示列表中未包含的着色器有用, 但您想要使用 `renderToTexture` 。


**返回值:** [Phaser.GameObjects.Shader](/api/class/gameobjects-shader) - 此沙德例(云云).


> 源码：[src/gameobjects/shader/Shader.js#L430](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L430)  
引入版本：4.0.0


---

### setRenderToTexture {#setRenderToTexture}

#### \<instance> setRenderToTexture([key]) {#instance-setrendertotexturekey}


**说明:**

更改此阴影, 而不是将其渲染到显示列表中, 而是将其渲染到 WebGL 框架缓冲器和纹理中。 这样您就可以使用此阴影的输出来做纹理 。

使用这种方法后,以下属性会被覆盖: 使用 :

- `Shader.drawingContext`

- `Shader.glTexture`

此外,您还可以提供这种方法的键。 这样做可以从此阴影创建 Phaser 纹理, 将其存储在 `Shader.texture` 中, 保存到纹理管理器中, 允许您使用它来获取任何纹理游戏对象, 如 Sprite 或 图像 :

```javascript
var shader = this.add.shader('myShader', x, y, width, height);

shader.setRenderToTexture('doodle');

this.add.image(400, 300, 'doodle');
```

注意它存储了此阴影的主动引用。 这意味着当此阴影更新时, 纹理和任何用它渲染的物体也会更新。 另外, 如果您摧毁了此阴影, 请确定清除任何可能作为纹理使用的对象 。

默认情况下, 它会创建一个单一的基础纹理。 您可以使用 `Texture.add` 方法在纹理中添加帧。 这样做之后, 您可以允许 Game Objects 从 Render 纹理中使用特定的帧 。

如果您想要零星更新纹理, 请不要使用这种方法。 相反, 请使用动态图解 :

```javascript
var shader = this.add.shader('myShader', x, y, width, height);

var dynamic = this.textures.addDynamicTexture('myTexture', shader.width, shader.height);

// To update the texture:
dynamic.clear().draw(shader).render();
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 是 | 将纹理存储在全球纹理管理器内部的独有键 。 |


**返回值:** [Phaser.GameObjects.Shader](/api/class/gameobjects-shader) - 此沙德例(云云).


> 源码：[src/gameobjects/shader/Shader.js#L345](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L345)  
引入版本：3.19.0


---

### setTextureCoordinates {#setTextureCoordinates}

#### \<instance> setTextureCoordinates([topLeftX], [topLeftY], [topRightX], [topRightY], [bottomLeftX], [bottomLeftY], [bottomRightX], [bottomRightY]) {#instance-settexturecoordinatestopleftx-toplefty-toprightx-toprighty-bottomleftx-bottomlefty-bottomrightx-bottomrighty}


**说明:**

设置阴影的纹理坐标。 这些值用于为阴影提供纹理映射, 并通常用于驱动基因输出 。

默认情况下, 着色器使用整个纹理, 范围为 0-1。 坐标位于 WebGL 纹理空间中, 在下左方为 0 。 这种方法允许您指定纹理区域使用, 或甚至超出 0-1 界限。 如果您想要使用一个从纹理中切换的单一框架, 重复着色器的纹理, 使用更大的数值范围, 或者扭曲着色器, 则会有所帮助 。

注意一个四角是由两个三角形组成的, 由左上角到右下角的对角分隔。 这意味着坐标的某些排列可能只影响一个三角形。 这可能造成在对角线上突然扭曲。 注意输出。 矩形和平行图是安全的下注。 旋转和缩放转换也是一样。 移动单个点是危险的 。

使用此方法无需参数来调用着色器以使用整个纹理 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| topLeftX | number | 是 | 0 | 纹理的左上角x坐标. |
| topLeftY | number | 是 | 1 | 纹理的左上方的Y坐标 。 |
| topRightX | number | 是 | 1 | 纹理的上右X坐标. |
| topRightY | number | 是 | 1 | 纹理的上右侧坐标 。 |
| bottomLeftX | number | 是 | 0 | 纹理的左下角x坐标. |
| bottomLeftY | number | 是 | 0 | 纹理的左下方和坐标 。 |
| bottomRightX | number | 是 | 1 | 纹理的下方右侧x坐标. |
| bottomRightY | number | 是 | 0 | 纹理的下方右侧坐标 。 |


**返回值:** [Phaser.GameObjects.Shader](/api/class/gameobjects-shader) - 这个擦拭实例


> 源码：[src/gameobjects/shader/Shader.js#L491](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L491)  
引入版本：4.0.0


---

### setTextureCoordinatesFromFrame {#setTextureCoordinatesFromFrame}

#### \<instance> setTextureCoordinatesFromFrame(frame, [texture]) {#instance-settexturecoordinatesfromframeframe-texture}


**说明:**

从一个框架设置着色器的纹理坐标。这是一种方便方法,它设置纹理坐标,以匹配一个纹理中的框。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| frame | [Phaser.Textures.Frame](/api/class/textures-frame) \| string | 否 | 设置纹理坐标的框。 如果给出了字符串, 则用于查找纹理中的框 。 |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) \| string | 是 | 框架来自的纹理。 只有在 `frame` 是一个字符串时才使用此纹理。 如果给出了字符串, 将用来在纹理管理器中查找纹理。 如果不给出, 则使用 `Shader.textures` 的第一个成员。 如果 `Shader.textures` 空, 就会发生错误 。 |


> 源码：[src/gameobjects/shader/Shader.js#L549](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L549)  
引入版本：4.0.0


---

### setTextures {#setTextures}

#### \<instance> setTextures([textures]) {#instance-settexturestextures}


**说明:**

设置着色器使用的纹理 。

有些遮蔽器不使用任何纹理。 有些可能使用一个或多个纹理。 当遮蔽器被渲染时, 纹理被分配到 0 到 N 的纹理单元, 而 N 是 `textures.length - 1`。 您必须在遮蔽器中设置制服, 以便与这些纹理单元匹配 。

调用这种方法将用新的方法取代现有的纹理阵列。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| textures | Array.\<string> \| Array.\<[Phaser.Textures.Texture](/api/class/textures-texture)> | 是 | 阴者用之纹理. |


> 源码：[src/gameobjects/shader/Shader.js#L297](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L297)  
引入版本：4.0.0


---

### setUniform {#setUniform}

#### \<instance> setUniform(name, value) {#instance-setuniformname-value}


**说明:**

设置阴影中制服的值。该值实际上被复制到所有使用它的地方。

一般最好在遮阳器配置对象中使用`setupUniforms`功能,在改变制服时设定统一值,使用这种方法设定制服一次.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 所要设置的制服名称. |
| value | any | 否 | 设置制服的值 。 |


**返回值:** [Phaser.GameObjects.Shader](/api/class/gameobjects-shader) - 


> 源码：[src/gameobjects/shader/Shader.js#L277](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L277)  
引入版本：4.0.0


---

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(setUniform, drawingContext) {#instance-setupuniformssetuniform-drawingcontext}


**说明:**

设置遮蔽器制服的函数。 渲染时自动调用。 它由构造器中传来的 `config` 对象设置。 您应该使用此函数设定您遮蔽器运行所需的任何统一值 。

您可以在对象创建后直接设置此函数, 但建议使用 `config` 对象来保持您的逻辑封装 。

函数用两个参数引用: `setUniform`和 `drawingContext`. `setUniform` 是一个需要两个参数的函数:字符串(制服的名称)和值。确保值匹配阴影中的预期类型。您不需要太精确, 因为系统会按需要转换例如阵列和浮图32Array类型。 要在阴影中设置阵列, 请将 `[0]`附加到统一名称中。 `drawingContext`是当前绘图上下文的参考, 如果您需要查询摄像机或类似的, 可能有用 。

注意`uProjectionMatrix`是自动为你设定的.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| setUniform | function | 否 | 设置制服的功能 `(name: string, value: any) => void` |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 参考当前绘图背景 。 |


> 源码：[src/gameobjects/shader/Shader.js#L446](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/Shader.js#L446)  
引入版本：4.0.0


---

---
