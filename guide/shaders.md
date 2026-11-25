# Phaser 4 着色器指南

Phaser 4 更新了 WebGL 渲染系统，扩展了渲染能力并提高了可靠性。本指南介绍核心概念，以及如何在新系统中使用着色器。

译自 Phaser v4.2.1 的[着色器指南](https://github.com/phaserjs/phaser/blob/41be1e462bc600064e498cba370bfa8c5c055a22/docs/Phaser%204%20Shader%20Guide/Phaser%204%20Shader%20Guide.md)。[上游 MIT 许可证](/license.txt)

## 1. 渲染概念 {#rendering-concepts}

Phaser 4 的 WebGL 渲染器是在 Phaser 3 之后完全重写的。它把绘制操作封装起来，让它们可以在渲染系统的不同位置运行。

### WebGL 状态管理 {#webgl-state-management}

Phaser 4 封装了 WebGL 调用。需要访问 WebGL 内部状态时，使用 Phaser 的包装器，避免直接调用 `gl.someFunction()`。

- `Phaser.Renderer.WebGL.Wrappers.WebGLGlobalWrapper` 的实例位于 `game.renderer.glWrapper`。它镜像 GL 状态，例如混合模式、当前绑定的纹理、着色器和帧缓冲区，以及裁剪区域（scissor）和纹理预乘设置。
- `WebGLShaderSetterWrapper` 的实例位于 `game.renderer.shaderSetters`，存储供内部使用的 GL 常量、数据大小和着色器 uniform 设置方法。
- `WebGLTextureUnitsWrapper` 的实例位于 `game.renderer.glTextureUnits`。渲染器用它自动分配纹理单元，并将纹理绑定到对应单元，以便着色器访问。
- 资源包装器（如 `Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper`）保存 `WebGLTexture` 等 WebGL 资源及其创建信息。一般用 `game.renderer.createTextureFromSource` 之类的方法来创建，避免直接调用构造函数。
  - `WebGLBufferWrapper` 管理顶点着色器使用的数据缓冲区。索引缓冲区按顺序保存顶点索引，以复用顶点并提高效率，用 `game.renderer.createIndexBuffer()` 创建。顶点缓冲区保存位置、着色和纹理坐标等顶点数据，用 `game.renderer.createVertexBuffer()` 创建。
  - `WebGLFrameBufferWrapper` 管理帧缓冲区。帧缓冲区创建于 DrawingContext，可将绘制结果写入用作渲染目标的纹理。
  - `WebGLProgramWrapper` 管理着色器程序，即编译并链接的顶点和片元着色器组合。渲染节点内的 ProgramManager 管理这些程序，可以包含多个包装器，各自保存一个程序变体。
  - `WebGLTextureWrapper` 管理纹理。创建 Texture 对象时会自动创建包装器，也可以通过 `game.renderer.createTextureFromSource()` 创建。
  - `WebGLVAOWrapper` 管理顶点数组对象（VAO）。VAO 记住顶点缓冲区的属性布局，避免重复应用设置。ProgramManager 会自动创建这些包装器。
  - `WebGLVertexBufferLayoutWrapper` 管理顶点缓冲区的包装器及其数据类型，通过 `new WebGLVertexBufferLayoutWrapper(...)` 创建。负责组织渲染所需顶点缓冲区的节点会用到它。

这些包装器用来跟踪不同函数调用之间的状态，并在 WebGL 渲染上下文丢失后重建状态。

> **DynamicTexture 与上下文丢失**
>
> RenderTexture 使用的 DynamicTexture 在 WebGL 中将内容绘制到纹理。WebGL 渲染上下文恢复后，这些纹理会变为空白。其他纹理与资源应能完整重建。

绕开包装器改动 WebGL 状态可能导致不稳定。需要直接发出 GL 调用时，请使用内置的管理机制。

### DrawingContext 对象 {#drawingcontext-objects}

DrawingContext 用于封装渲染器内部的绘制操作。只有编写渲染器内部代码时才需要直接使用它。

`Phaser.Renderer.WebGL.DrawingContext` 描述当前绘制操作使用的局部 WebGL 状态，包括摄像机、混合模式、帧缓冲区，以及影响像素绘制位置与方式的其他设置。

DrawingContext 可以嵌套。可以创建一个临时上下文绘制若干对象，完成后回到上一个上下文。需要复制时，调用 `drawingContext.getClone()` 并直接修改副本。

开始和结束使用上下文时，分别调用 `drawingContext.use()` 和 `drawingContext.release()`。这会执行清理等待复用的上下文、开启新渲染批次等必要操作。新的 DrawingContext 有一套不同的绘制设置，因此在生效前要通知当前批次完成绘制。

DrawingContext 可以持有帧缓冲区，此时 `drawingContext.texture` 指向绘制目标纹理。使用这个上下文绘制的内容都会写入该纹理。DynamicTexture 等持久资源会保留纹理，滤镜等临时资源对应的纹理则会在下次使用前清空。

### 批量渲染 {#batched-rendering}

引擎会自动处理批次。了解批次何时结束，有助于改善游戏性能。

最基本的绘制方式是独立渲染（Stand Alone Render，SAR），每个对象单独发起一次绘制调用。绘制调用的开销随设备和内容而变，通常每帧不宜超过几百次。

Phaser 会把能在一次调用中绘制的常见对象自动合批。大多数对象由四边形（quad）组成，使用相同的着色器和一组纹理，可以一起绘制。批次越大，通常越高效。

以下情况会结束当前批次，绘制已有内容，再开始下一批。

- 批次已满，达到 16384 个四边形。
- 可用的纹理单元耗尽。
  - 大多数设备提供 8 或 16 个纹理单元，单个批次可使用相应数量的纹理。
  - 移动设备可能支持多个纹理单元，但只用一个时性能往往最好。启用游戏配置项 `autoMobileTextures` 后，Phaser 在检测到移动设备时会将纹理单元数降为 1。
- 使用了不同的着色器程序。
  - 游戏对象类型不同。许多对象共享着色器，常见分组包括基本四边形（Image、Sprite、Text、BitmapText 等）、重复四边形（TilemapLayer、TileSprite 等）、矢量对象（Graphics、Shape 等）和独立渲染对象（TilemapGPULayer、Rope 等）。
  - 使用滤镜。滤镜会切换着色器和 DrawingContext。
  - 同一种游戏对象因状态不同需要切换着色器。例如相邻对象一个使用光照、另一个不使用。启用 `roundPixels`（例如通过 `smoothPixelArt`）后，处于默认缩放和旋转状态的对象与经过缩放或旋转的对象也可能分批。

其他操作也可能结束批次，具体表现因设备而异。通常可以把同类游戏对象排在显示列表中的相邻位置，并把独立纹理合并成纹理图集。

### 渲染节点 {#render-nodes}

RenderNode 是在渲染系统中执行一项任务的对象。只有修改渲染系统内部实现时才需要直接操作它。

在 `game.renderer.renderNodes`（`Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager`）中注册节点。用 `addNode()` 注册已有实例，用 `addNodeConstructor()` 注册按需实例化的构造函数，通过 `getNode()` 获取节点。

节点可存放状态，但节点实例会复用。若一个节点可能触发后续渲染，可以用新对象保存状态。

按惯例，每个节点负责一个任务，通过 `node.run()` 执行。在 `run` 的起止处调用 `this.onRunBegin()` 和 `this.onRunEnd()`，方便调试。

提供批处理功能的节点通过 `node.batch()` 调用。使用 `this.manager.setCurrentBatchNode(this, drawingContext)` 通知管理器批次已开始。其他节点报告渲染状态将变更时，管理器会调用 `run(drawingContext)` 绘制当前批次。如果 `batch` 自己发现批次已经完成，也可以直接调用 `run`。这里的 `run` 应立即执行绘制。

节点可相互调用，由此构成渲染树。调用 `game.renderer.renderNodes.setDebug(true)` 捕获一帧，再用 `game.renderer.renderNodes.debugToString()` 获取这一帧运行过的渲染节点说明。

> 渲染节点可以灵活拆分工作。出于性能考虑，默认节点集中处理少数大任务；也可以按需拆成更多更易定制的小任务。

### 统一绘制命令 {#unified-draw-commands}

Phaser 4 使用统一的 WebGL 绘制命令。这些方法面向渲染器内部开发。

目前 Phaser 4 的绘制操作都通过 `game.renderer.drawElements()` 执行。需要实例化绘制时，还可以调用 `game.renderer.drawInstancedArrays()`，两种方法的状态管理方式相同。

WebGL 状态在调用绘制命令时才更新，以避免不必要的重复状态变更。其他情况下也可以手动更新状态，通常很少需要这样做。

## 2. 编写 Shader 游戏对象 {#shader-game-object}

`Shader` 游戏对象用自定义着色器绘制四边形。它的使用方式类似 Sprite，可以在对象覆盖的区域内生成自定义画面。

> 本文用大写的 Shader 指 Phaser 的游戏对象。着色器程序是用于 WebGL 渲染的已编译顶点和片元着色器组合。

### Shader 的渲染方式 {#shader-rendering}

Shader 是独立渲染的四边形。它会打断当前批次，自身也无法与别的对象合批。每个 Shader 都需要一次绘制调用，应控制使用数量。

### 为 Phaser 编写着色器 {#authoring-shaders}

Shader 支持自定义顶点和片元着色器。默认顶点着色器通常已经足够，可以主要编写片元着色器。

#### Varying 变量 {#varyings}

默认顶点着色器通过 `varying vec2 outTexCoord` 向片元着色器传入坐标。X 和 Y 都在 0 到 1 之间，表示片元在四边形内的位置。

Phaser 4 的纹理原点 `(0, 0)` 位于左下角。WebGL 通常也如此约定，使用其他程序或着色器处理纹理时要核对方向。Phaser 4 的顶点坐标仍然从上向下计算。

#### 着色器扩展（Additions） {#additions}

只实现单一功能时，一个文件就够了。需要在运行时切换功能时，可用 Phaser 4 的 Additions 系统，通过模板将多个 GLSL 文件组合使用。

着色器模板使用 GLSL 预处理指令标记代码插入点，便于编辑器继续提供语法支持。使用 `#pragma phaserTemplate(key)` 定义插入点。系统按定义顺序插入所有使用该键的扩展代码。没有对应扩展时，该指令会被移除。

`#pragma phaserTemplate(shaderName)` 会将 `SHADER_NAME` 定义为游戏中的着色器名称，方便调试。

可以使用 `#define KEY` 定义宏，再用 `#ifdef KEY`、`#ifndef KEY`、`#else` 和 `#endif` 编写条件代码，尤其适合通过扩展定义宏。

```glsl
#pragma phaserTemplate(enableBigNumber)

float getNumber ()
{
    #ifdef BIG_NUMBER
    return 10;
    #else
    return 2;
    #endif
}
```

默认返回 `2`。如果某个扩展在 `enableBigNumber` 位置插入 `#define BIG_NUMBER`，就会返回 `10`。扩展也可用于共享代码，以缩小游戏包体或简化大型代码库的维护。

### 在游戏中加载着色器 {#loading-shaders}

可以加载 GLSL 文件，也可以内联代码字符串。两种方式功能相同，也可以混用。

#### 加载 GLSL 文件 {#load-glsl-files}

单个 GLSL 文件包含一段着色器或 GLSL 片段。加载方式如下。

```js
class Example extends Phaser.Scene
{
    preload ()
    {
        this.load.glsl('Marble', 'assets/shaders/marble.frag');
    }
}
```

文件以 `Marble` 为键加入游戏的着色器缓存，后续可以引用这个键。通过 `game.cache.shader.get('Marble')` 检索以 `Phaser.Display.BaseShader` 存储的数据，`baseShader.glsl` 包含文件中的代码。

> Phaser 3 的着色器包可存放多个着色器及其元数据。Phaser 4 不再把这类包解析成多个着色器。要加载大量着色器代码，可以用 JSON、XML 或其他受支持的格式。
>
> Phaser 3 在加载时将着色器分为顶点和片元两类并进行组合。Phaser 4 的代码片段可以按需组合，因此 GLSL 文件作为单个文本文件加载。

#### 内联字符串 {#inline-strings}

也可以在代码中把着色器或着色器片段定义成字符串。这能减少文件数量，但编辑器可能无法对字符串里的 GLSL 执行语法检查。

### 创建 Shader 对象 {#creating-shader-objects}

着色器编写并加载后，使用 `Phaser.GameObjects.Shader` 在游戏中创建 Shader 对象。

```js
// `this` is a Scene.
this.add.shader(config, x, y, width, height, textures)
```

- `config` 是主要配置对象。
- `x` 和 `y` 是位置。
- `width` 和 `height` 是着色器四边形的尺寸。
- `textures` 是 Shader 使用的纹理或纹理键列表。

#### 配置对象 {#config-object}

Shader 配置对象的结构如下。

```ts
type ShaderQuadConfig =
{
    // Required:
    name: string;

    // Following are optional:
    shaderName: string;
    fragmentSource: string;
    vertexSource: string;
    fragmentKey: string;
    vertexKey: string;
    initialUniforms: { [string]: number | number[] | TypedArray | boolean | boolean[] };
    setupUniforms: (
        setUniform: (name: string, value: any) => void,
        drawingContext: Phaser.Renderer.WebGL.DrawingContext
    ) => void;
    shaderAdditions: Phaser.Types.Renderer.WebGL.ShaderAdditionConfig[];
    updateShaderConfig: (
        drawingContext: Phaser.Renderer.WebGL.DrawingContext,
        gameObject: Phaser.GameObjects.Shader,
        renderNode: Phaser.Renderer.WebGL.RenderNodes.ShaderQuad
    ) => void;
}
```

常见配置可以很简短。

```ts
// When using a loaded GLSL file:
const config1 = {
    name: 'myShader',
    fragmentKey: 'Marble'
};

// Or when using inline GLSL code:
const glsl = '// GLSL code goes here';
const config2 = {
    name: 'myOtherShader',
    fragmentSource: glsl
};
```

**`name`** 为必填项，用于给 Shader 命名。Shader 会用这个名称创建一个 `Phaser.Renderer.WebGL.RenderNodes.ShaderQuad`。节点只在 Shader 内部存储，所以名称可以重复，主要用于调试。

**`shaderName`** 是着色器程序名称的基础部分，默认使用 `name`。存在 `#pragma phaserTemplate(shaderName)` 时，会在该处插入完整名称，其中包含基础名称、已启用的着色器扩展，以及顶点或片元着色器的标识。

**`fragmentSource` 和 `vertexSource`** 是内联的片元和顶点着色器源码。两者都有默认实现。默认顶点着色器通常够用，默认片元着色器绘制颜色渐变，方便确认着色器是否正常运行。

**`fragmentKey` 和 `vertexKey`** 是片元和顶点着色器在游戏缓存中的键。若同时提供了对应的 `fragmentSource` 或 `vertexSource`，内联源码优先。

![默认顶点着色器和片元着色器绘制的颜色渐变](/guide-images/default-fragment-shader.png)

**`initialUniforms`** 是一组只在创建着色器程序时设置一次的 uniform。如果创建后无需更换纹理，可以在这里分配纹理单元。

```ts
// How to set textures on a Shader:
const config = {
    initialUniforms: {
        uTexture: 0,
        uSecondaryTexture: 1,
        uThirdTexture: 2
    }
};
```

**`setupUniforms`** 用来为程序设置 uniform。此函数被交给 Shader 的渲染节点，并在每次渲染这个 Shader 时调用。节点传入 `setUniform()` 和 `drawingContext`。调用 `setUniform(name, value)` 可以更新着色器值，例如驱动动画或切换纹理。`drawingContext` 包含当前 GL 状态。

```ts
// How to update the `time` uniform on a Shader:
const config = {
    setupUniforms: (setUniform, drawingContext) =>
    {
        setUniform('time', this.game.loop.getDuration());
    }
};
```

**`shaderAdditions`** 是着色器扩展列表。不同扩展可以向同一个模板位置插入代码，因此顺序很重要。每个扩展都是一份描述待插入代码的配置。

```ts
type Phaser.Types.Renderer.WebGL.ShaderAdditionConfig =
{
    // The name of this addition. This contributes to the full shader program key.
    name: string;

    // A list of additions to make. The `key` is located in the shader by `#pragma phaserTemplate(key)`. The value is added to that location in the shader, as well as values from other additions.
    additions: { key: string, value: string }[];

    // Optional tags used to identify the addition if the name changes.
    tags: string[] | undefined;

    // Whether to disable the addition. A disabled addition is not compiled into the shader program.
    disable: boolean | undefined;
};
```

下面的扩展在默认片元着色器（Phaser 源码中的 `ShaderQuad.frag`）中添加纹理映射。

```ts
const addition = {
    name: 'myAddition',
    additions: [
        { key: 'fragmentHeader', value: 'uniform sampler2D iChannel0;' },
        { key: 'fragmentProcess', value: 'fragColor = texture2D(iChannel0, outTexCoord);' }
    ]
};
```

**`updateShaderConfig`** 用于在运行时重新配置着色器程序，例如因游戏设置改变而重新编译着色器。该函数交给 Shader 的渲染节点，在渲染期间先于 `setupUniforms` 调用。若用箭头函数，`this` 不会指向渲染节点，所以回调会通过参数提供该节点。

```ts
// How to toggle a shader addition on a Shader:
const config = {
    updateShaderConfig: (gameObject, drawingContext, renderNode) =>
    {
        // Manages the shader program and cached variants.
        const programManager = renderNode.programManager;

        // How to get an existing addition:
        const myAddition = programManager.getAddition('myAddition');

        // Toggle addition:
        myAddition.disable = !myAddition.disable;

        // The shader will recompile additions once this function returns.
    }
};
```

除了启用或停用扩展，也可以直接更改扩展代码。Phaser 4 按名称缓存着色器以避免重复编译，因此需要改动扩展名称才会编译改动。例如，核心精灵渲染着色器有一个扩展，会根据批次中容纳的纹理数量改名为 `1TexCount`、`8TexCount` 等。

扩展可以附加标签，方便在它改名后仍能重新找到它。

```ts
// How to successfully edit a shader addition on a Shader:
const config = {
    updateShaderConfig: (gameObject, drawingContext, renderNode) =>
    {
        const programManager = renderNode.programManager;

        // How to get an addition when you don't know its name:
        // (it's up to you to handle the case where multiple additions share a tag)
        const myAddition = programManager.getAdditionsByTag('ITERATOR')[0];

        // Edit the tag:
        const iterations = gameObject.iterations;
        myAddition.name = 'ITERATIONS_' + iterations; // Trigger recompilation.
        myAddition.fragmentHeader = '#define ITERATION_COUNT ' + iterations;
        // Note: this edit has a SPACE before the variable.
        // Note 2: GLSL will interpret this as an `int`, not a `float`,
        // unless you add a trailing '.0' or '.'.
        //
        // We use a similar pattern to change the length of `for` loops internally,
        // because GLSL does not support variable loop length after compile time.
    }
};
```

#### 在着色器中使用纹理 {#textures-in-shaders}

创建 Shader 时传入所需纹理，并为其设置对应的 uniform。下面演示了最简的纹理着色器。

```ts
class Example extends Phaser.Scene
{
    preload ()
    {
        this.load.image('checker', 'assets/pics/checker.png');
    }

    create ()
    {
        const frag = `
        precision mediump float;
        uniform sampler2D iChannel0;
        varying vec2 outTexCoord;

        void main ()
        {
            vec4 pixel = texture2D(iChannel0, outTexCoord);
            gl_FragColor = vec4(outTexCoord.xyx * pixel.rgb, 1.0);
        }
        `;

        const shader = this.add.shader({
            name: 'simpleTexture',
            fragmentSource: frag,
            initialUniforms: {
                iChannel0: 0
            }
        }, 400, 300, 800, 600, [ 'checker' ]);
    }
}

const game = new Phaser.Game({
    type: Phaser.WEBGL,
    width: 800,
    height: 600,
    scene: Example
});
```

示例用 `initialUniforms` 设置纹理 uniform，同时传入 `[ 'checker' ]`。纹理在列表中的索引为 0，因而会分配到纹理单元 0，uniform 也设为 0。其余纹理依次对应单元 1、2、3 等。不设置纹理 uniform 时，其值为 0，只有一张纹理时可能仍能正常工作。

需要调整纹理坐标时可使用 `shader.setTextureCoordinates()`。使用纹理图集中的某一帧时可用 `shader.setTextureCoordinatesFromFrame()`。

## 3. 编写自定义滤镜 {#sample-filter}

Shader 只有输出，滤镜则同时有输入和输出。多个滤镜会组成一个栈，图像逐级通过滤镜并发生变化。摄像机和所有游戏对象都可以使用滤镜。

### 使用滤镜 {#using-filters}

摄像机默认提供 `camera.filters`。对游戏对象使用滤镜前，先调用 `gameObject.enableFilters()`，再访问 `gameObject.filters`。

滤镜分为 `filters.internal` 和 `filters.external` 两个列表。内部滤镜随摄像机或对象移动。外部滤镜在内部滤镜之后运行，作用在摄像机或对象外部的渲染上下文中，通常会影响整个屏幕。

调用列表上的添加方法创建滤镜，例如 `const filterController = gameObject.filters.internal.addBlur()`。滤镜通常提供多个参数，可以通过返回的控制器更新。

通过 `filterController.setPaddingOverride()` 设置各滤镜的内边距，依次传入左、上、右、下四个值。只传入 `null` 时，支持自动内边距的滤镜会使用自动值。

![滤镜的内部和外部上下文及对应的内边距](/guide-images/filter-padding.png)

外部上下文通常是屏幕。如果对象嵌套在其他对象内部渲染，外部上下文可能是另一个滤镜的内部上下文。没有宽度和高度的对象使用内部滤镜时，两种滤镜会使用同一个上下文。

每个滤镜将结果绘制到一个新的帧缓冲区中，绘制结果作为纹理传给下一个滤镜。渲染器通过 DrawingContext 对象池管理这些上下文。

### 编写滤镜 {#authoring-filters}

滤镜比 Shader 略复杂，两者使用同一套底层着色器程序系统。带自定义着色器程序的滤镜需要两部分，一个 Controller 和一个 RenderNode。

```ts
class BumpToNormal extends Phaser.Filters.Controller
{
    constructor (camera)
    {
        // The name 'FilterBumpToNormal' is defined in FilterBumpToNormal.
        super(camera, 'FilterBumpToNormal');

        // Properties on the controller are used to pass data to the shader.
        this.radius = 1;
    }
}

const fragmentShaderBumpToNormal = `// GLSL code goes here`;

const additions = {}; // You would define any additions here.

class FilterBumpToNormal extends Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader
{
    constructor (manager)
    {
        // The name 'FilterBumpToNormal' is used by the Controller.
        super('FilterBumpToNormal', manager, null, fragmentShaderBumpToNormal, additions);
    }

    // This function is called by the renderer.
    setupTextures (controller, textures, drawingContext)
    {
      // Custom code goes here.
      // `textures` is an array of WebGLTextureWrapper objects.
      // These will be assigned to texture units in list order.
      // `textures[0]` is always the input from the previous step in the filter stack.
      // Assign your textures to `textures[1]` and up.
    }

    // This function is called by the renderer after `setupTextures`.
    updateShaderConfig (controller, drawingContext)
    {
        // Custom code goes here.
        // This works just like a Shader: update your shader additions here.
        const programManager = this.programManager;
    }

    // This method sets up the uniforms for the shader.
    // It is called by the renderer after `updateShaderConfig`.
    setupUniforms (controller, drawingContext)
    {
        // Custom code goes here.
        // This works much like a Shader, except because you're defining a whole class,
        // you have access to `this.programManager` directly.
        const programManager = this.programManager;

        programManager.setUniform('resolution', [ drawingContext.width, drawingContext.height ]);
        programManager.setUniform('radius', controller.radius);
    }
}
```

滤镜只接收片元着色器。Phaser 在合成滤镜栈时计算顶点。上面的 `BaseFilterShader` 子类使用内联 GLSL，也可以传入加载后的 GLSL 缓存键，例如 `super('FilterBumpToNormal', manager, key)`，让 `key` 取代示例中的 `null`。

要使用滤镜，先注册渲染节点，再把滤镜加到游戏对象上。

```ts
class Example extends Phaser.Scene
{
    preload ()
    {
        this.load.image('distortion8', 'assets/textures/distortion8.png');
    }

    create ()
    {
        if (!this.renderer.renderNodes.hasNode('FilterBumpToNormal'))
        {
            // Load the custom filter.
            // We load during scene creation because the renderer has booted by this point.
            this.renderer.renderNodes.addNodeConstructor('FilterBumpToNormal', FilterBumpToNormal);
        }

        // Add an image for filtering.
        const image = this.add.image(640, 360, 'distortion8')
        .enableFilters();

        // Add custom filter to the image.
        // Note that the filter requires a camera to be passed to it.
        const bumpToNormal = image.filters.internal.add(
            new BumpToNormal(image.filterCamera)
        );
        bumpToNormal.radius = 8;
    }
}
```

滤镜也能使用 Shader 的高级功能，例如通过 `updateShaderConfig` 管理着色器扩展。要创建带扩展的滤镜，可将扩展传给 `BaseFilterShader`。

```ts
super(name, manager, fragmentShaderKey, fragmentShaderSource, shaderAdditions);
```

## 4. 内置着色器和扩展 {#built-in-shaders}

Phaser 4 使用的着色器和扩展的代码都包含在库中。可以直接使用它们，或参考它们编写自己的着色器。

### 着色器扩展详解 {#shader-additions-redux}

Phaser 4 的 Additions 模板系统用于创建着色器变体。要支持扩展，先在着色器中用 `#pragma phaserTemplate(KEY)` 声明插入点。扩展把与 `KEY` 关联的代码插到这里。该指令是合法的 GLSL 预处理语法，会在编译着色器前被替换。

扩展配置包含以下属性。

- `name` 是唯一标识，例如 `'ITERATIONS_1'`。可以加上数字来区分变体。即便着色器代码不同，同名扩展也会被视为相同。
- `tags` 是可选的标签数组，例如包含 `'ITERATION'`。可用于给扩展分类，也便于改名后按标签获取。
- `disable` 是可选的停用标记。停用时会暂时从着色器中移除扩展代码，其名称也会从着色器的组合名称中去掉。
- `additions` 描述模板插入点和对应的 GLSL 代码，例如将 `someCode` 插入 `fragmentHeader`。
  - 键取自 `phaserTemplate` 指令。
  - 多个扩展可以使用同一个键，代码会按扩展顺序加入。
  - 插入操作会在顶点和片元着色器中查找相同的键。找不到该键时不插入代码。
  - 扩展可以引入新的 `phaserTemplate` 键，只有顺序在它之后的扩展能找到这些键。

### 可扩展着色器的结构 {#extensible-shader-structure}

Phaser 4 中很多着色器都有模板插入点。大部分面向特定功能，下面列出通用模板点，以及 Filter、Shader 游戏对象和常规精灵渲染所用的 Multi 着色器的插入点。

模板点由 `#pragma phaserTemplate(KEY)` 中的 `KEY` 标识。

#### 通用模板点 {#universal-template-points}

- `shaderName` 在此定义着色器名称，供调试使用。

#### Shader 游戏对象的模板点 {#shader-game-object-template-points}

默认片元着色器提供了多个模板点，可以据此模块化组织代码。若使用自定义片元着色器，需要自行声明要用的模板点。

- `extensions` 用于启用可选的 WebGL 扩展，也须在 `game.renderer` 中启用。
  - 扩展必须放在其他 GLSL 代码之前。
  - Phaser 4 自动启用了若干 WebGL 扩展，其中和着色器代码有关的是 `OES_standard_derivatives`。用 `#extension GL_OES_standard_derivatives : enable` 启用。
  - 顶点着色器也使用这个键。
- `features` 用于定义功能开关。
  - 例如 `#define ENABLE_FOO` 会使 `#ifdef ENABLE_FOO` 下的代码生效。
  - 顶点着色器也使用这个键。
  - 功能开关可以由 ProgramManager 管理。
- `fragmentDefine` 用于定义常量。
  - 例如 `#define ITERATIONS 1` 可以让后续代码把 `ITERATIONS` 当作编译期常量使用。
  - 着色器通常用这种方式处理可配置的循环次数。
- `outVariables` 用于定义从顶点着色器传来的 `varying` 变量。
  - 例如 `varying vec2 outTexCoord;` 已用于传递纹理坐标。
  - 顶点和片元着色器共享此键，两个阶段的 varying 声明必须相符。
- `fragmentHeader` 用于定义片元着色器需要的其他代码，例如 uniform 和函数。
  - 它位于 `main` 函数上方。
  - 注意函数定义的顺序，先定义被调用的函数。
- `fragmentProcess` 用于添加片元处理步骤。
  - 它位于 `main` 中的 `vec4 fragColor = vec4(outTexCoord.xyx, 1.0);` 和 `gl_FragColor = fragColor;` 之间。
  - 可插入覆盖 `fragColor` 的处理步骤。

通常无需调整 Shader 的顶点着色器。需要调整时，可以使用以下模板点。

- `extensions`
- `features`
- `vertexDefine` 相当于顶点着色器中的 `fragmentDefine`。
- `outVariables`
- `vertexHeader` 相当于顶点着色器中的 `fragmentHeader`。
- `vertexProcess` 相当于顶点着色器中的 `fragmentProcess`。
  - 它位于 `main` 中，放在 `gl_Position` 和 `outTexCoord` 赋值之后。
  - 可插入覆盖标准输出或更新额外 `varying` 变量的步骤。

#### Filter 的模板点 {#filter-template-points}

滤镜通常定义自己的片元着色器，必要时可定义模板点，例如用 `fragmentHeader` 引入通用函数。也可参考 Shader 系统设计自己的模板点。

滤镜使用 `SimpleTexture-vert` 作为顶点着色器。它由自动化流程使用，需要精确对齐，因此没有模板点。它提供 `vec2 outFragCoord`（归一化的屏幕空间坐标）和 `vec2 outTexCoord`（纹理坐标）两个 varying。

#### Multi 着色器的模板点 {#multi-shader-template-points}

Multi 着色器提供与 Shader 相同的一组插入点，并实现了大量扩展。详见 `BatchHandlerQuad` 的源码。

### 内置着色器代码 {#existing-shader-code}

Phaser 将着色器代码以 GLSL 字符串存放在 `Phaser.Renderer.WebGL.Shaders` 中，代码优先考虑运行性能。

- 顶点着色器使用 `Vert` 后缀，例如 `MultiVert`。大部分可以直接使用。
- 片元着色器使用 `Frag` 后缀，例如 `MultiFrag`。大部分可以直接使用，少数需要额外定义才是有效代码。
- 两种后缀都没有的代码通常是供扩展注入的片段，需嵌入其他着色器才能使用。

可以把这些源码用于自己的扩展，或作为自定义着色器的基础。它们会随引擎实现变更。一般可以优先使用下面介绍的扩展工厂函数。

### 着色器扩展工厂函数 {#shader-addition-makers}

`Phaser.Renderer.WebGL.ShaderAdditionMakers` 提供了一组工厂函数。函数返回的扩展可以直接放进配置对象。

工厂函数可接受多个参数，最后一个参数总是 `disable`。设为真值时，扩展已创建但初始处于停用状态。

- `MakeDefineLights`、`MakeRotationDatum`、`MakeOutInverseRotation`、`MakeGetNormalFromMap` 和 `MakeApplyLighting` 可组合用于 Phaser 的动态光照。它们各自独立，便于在其他场景使用光源和法线贴图。
- `MakeFlatNormal` 无需法线贴图即可提供平面法线向量。
- `MakeApplyTint` 使用 Multi 顶点着色器提供的 `outTint` varying，将各种着色混合模式应用到颜色。
- `MakeBoundedSampler` 为片元着色器提供 `boundedSampler` 函数。超出 0 到 1 的标准 GL 纹理坐标范围时，它返回透明像素。滤镜着色器用它避免纹理帧边缘出现不必要的拉伸或环绕。
- `MakeSmoothPixelArt` 提供带抗锯齿的未过滤纹理采样函数。在保留像素块状外观的同时，减少锯齿和移动时的画面跳变。它通过名为 `texCoord` 的模板点调用该函数。

大多数工厂函数会定义短代码片段。为了保持 GLSL 字符串简洁，这些短片段和 GLSL 源码分别存放，用来衔接不同扩展。可以查看源码了解每个片段的具体作用。

有些工厂函数接收变量来配置扩展。可以通过 Filter 和 Shader 的 `updateShaderConfig` 在运行时更新变量。也可以通过 ProgramManager 添加、替换或移除扩展和功能，复用工厂函数来构造所需扩展。

## 深入阅读 {#further-steps}

本文介绍了 Phaser 4 渲染与着色器的主要用法。可以继续阅读 [Phaser 源码](https://github.com/phaserjs/phaser)，查看引擎如何应用这些机制。设计带自定义属性布局的顶点着色器时，还需要了解索引缓冲区、VAO 和属性绑定等 GPU 资源的设置过程。Shader 和 Filter 使用 Phaser 4 渲染器管理的四边形，日常使用时这些工作由引擎负责。
