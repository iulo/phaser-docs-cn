# Phaser.GameObjects.Components.RenderSteps {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-rendersteps)

Scope: 
static
> 源码：[src/gameobjects/components/RenderSteps.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/RenderSteps.js#L7)  
引入版本：4.0.0

## 静态函数 {#static-functions}

## 静态函数 {#static-functions-1}

### addRenderStep {#addRenderStep}

#### \<instance> addRenderStep(fn, [index]) {#instance-addrenderstepfn-index}


**说明:**

将一个渲染步骤函数添加到此 Game Object 的 WebGL 渲染管道中 。

`_renderSteps`的第一个渲染步骤是先运行的。 它应该调用列表中的下一个渲染步骤。 这样就可以调制步骤来控制渲染流 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| fn | [Phaser.Types.GameObjects.RenderWebGLStep](/api/typedef/types-gameobjects#renderwebglstep) | 否 | 要添加的渲染步骤函数 。 |
| index | number | 是 | 参数列表中的索引将步骤添加到。 Omit 将添加到结尾 。 |


**返回值:** [Phaser.GameObjects.Components.RenderSteps](/api/namespace/gameobjects-components-rendersteps) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/RenderSteps.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/RenderSteps.js#L91)  



---

### renderWebGLStep {#renderWebGLStep}

#### \<instance> renderWebGLStep(renderer, gameObject, drawingContext, [parentMatrix], [renderStep], [displayList], [displayListIndex]) {#instance-renderwebglsteprenderer-gameobject-drawingcontext-parentmatrix-renderstep-displaylist-displaylistindex}


**说明:**

在渲染过程中运行一个步骤。 由 Render 模块自动调用 。

在大多数情况下,它只是运行`renderWebGL`功能.

当`_renderSteps`拥有多个条目时,例如当为这个对象启用滤镜时,它允许这些过程推迟`renderWebGL`,并用其他方式管理渲染的流量.

**标签:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 |  | 需要制作的WebGL 渲染器实例。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 正在渲染游戏对象 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 |  | 当前绘图背景 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 |  | 游戏对象的母矩阵, 如果它有的话 。 |
| renderStep | number | 是 | 0 | 渲染过程的哪一步应该运行? |
| displayList | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 是 |  | 目前正在提供的显示列表。 如果不提供, 将随游戏对象创建 。 |
| displayListIndex | number | 是 | 0 | 显示列表中的游戏对象索引 。 |


> 源码：[src/gameobjects/components/RenderSteps.js#L34](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/RenderSteps.js#L34)  
引入版本：4.0.0


---

---
