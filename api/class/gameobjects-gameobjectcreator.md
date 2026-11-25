# GameObjectCreator {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-gameobjectcreator)

游戏对象创建器是一个场景插件,它允许您快速创建许多常见类型的游戏对象,并使用配置对象返回,而不是需要按照游戏对象事实的要求指定单个参数.

通过此类制作的游戏对象,除非在配置对象中明确设置`add`属性为`false`,否则会自动添加到场景和更新列表中.

**构造函数**

`new GameObjectCreator(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此游戏对象创建者所属景区 。 |

---


**作用域**: static

> 源码：[src/gameobjects/GameObjectCreator.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectCreator.js#L11)  
引入版本：3.0.0

## 公开方法 {#public-methods}

### bitmapText {#bitmapText}

#### \<instance> bitmapText(config, [addToScene]) {#instance-bitmaptextconfig-addtoscene}


**说明:**

创建新的位图文本游戏对象并返回它。

BitmapText 对象通过取一个预发字体纹理并用该纹理戳出文本的每个字符来工作。这使得渲染速度与使用基于 Canvas 的字体相比非常快, 但这意味着字体必须预先创建并作为纹理图集保存。 如果您在游戏中需要高性能的静态文本渲染, 请通过 `scene.make.bitmapText()` 使用这种方法 。

注意:只有在将位图文字游戏对象建为Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.BitmapText.BitmapTextConfig](/api/typedef/types-gameobjects-bitmaptext#bitmaptextconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.BitmapText](/api/class/gameobjects-bitmaptext) - 创建的游戏对象 。


> 源码：[src/gameobjects/bitmaptext/static/BitmapTextCreator.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/static/BitmapTextCreator.js#L13)  
引入版本：3.0.0


---

### blitter {#blitter}

#### \<instance> blitter(config, [addToScene]) {#instance-blitterconfig-addtoscene}


**说明:**

创建新的闪烁游戏对象并返回它。

闪光器是一种高效的游戏对象,可以渲染大量Bob对象,所有物体的纹理都相同。 与使用单个的Game Objects不同,闪光器将所有Bob批量成一个单一的图调,使其理想化为粒子类效果、人群、弹池或任何需要用最小的俯仰来制作许多相同图像的情景。

注意:只有当闪光游戏对象已建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Sprite.SpriteConfig](/api/typedef/types-gameobjects-sprite#spriteconfig) | 否 | 此游戏对象将用来创建自身的配置对象。 `key`属性确定要使用的纹理, 选项 `frame`属性确定该纹理内的特定框架 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.Blitter](/api/class/gameobjects-blitter) - 创建的游戏对象 。


> 源码：[src/gameobjects/blitter/BlitterCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/BlitterCreator.js#L12)  
引入版本：3.0.0


---

### captureFrame {#captureFrame}

#### \<instance> captureFrame(config, [addToScene]) {#instance-captureframeconfig-addtoscene}


**说明:**

创建新的 CaptionFrame 游戏对象并返回它。

捕获Frame 是一个特殊的游戏对象,它捕捉显示列表中显示的 WebGL 帧缓冲器的当前状态。 捕获到前的物体会被捕获到一个命名的纹理; 捕获后的对象不会被捕获。 这对全景后处理效果有用, 如一层水或扭曲的覆叠。 所捕获的纹理会被键引用, 并用于其他游戏对象或过滤器上 。

这是仅使用WebGL的特性,在Canvas模式中没有效果. 相机必须启用`forceComposite`,或者捕获Frame必须在帧缓冲上下文中使用(如滤镜,动态透视,或者在0到1之间带有α的相机).

注意:只有在将 CaptureFrame 游戏对象建为 Phaser 时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.GameObjectConfig](/api/typedef/types-gameobjects#gameobjectconfig) | 否 | 此游戏对象将用来创建自己的配置对象。 抓取Frame 仅使用 `key`, `visible`, `depth`, 和 `add` 属性 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.CaptureFrame](/api/class/gameobjects-captureframe) - 创建的游戏对象 。


> 源码：[src/gameobjects/captureframe/CaptureFrameCreator.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/captureframe/CaptureFrameCreator.js#L11)  
引入版本：4.0.0


---

### container {#container}

#### \<instance> container(config, [addToScene]) {#instance-containerconfig-addtoscene}


**说明:**

创建新的容器游戏对象并返回。

注:只有在容器游戏对象已建为Phaser时,才能使用这种方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Container.ContainerConfig](/api/typedef/types-gameobjects-container#containerconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.Container](/api/class/gameobjects-container) - 创建的游戏对象 。


> 源码：[src/gameobjects/container/ContainerCreator.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/container/ContainerCreator.js#L14)  
引入版本：3.4.0


---

### dynamicBitmapText {#dynamicBitmapText}

#### \<instance> dynamicBitmapText(config, [addToScene]) {#instance-dynamicbitmaptextconfig-addtoscene}


**说明:**

创建新的动态位图文本游戏对象并返回。

注意:只有在动态位图文字游戏对象已建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.BitmapText.BitmapTextConfig](/api/typedef/types-gameobjects-bitmaptext#bitmaptextconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.DynamicBitmapText](/api/class/gameobjects-dynamicbitmaptext) - 创建的游戏对象 。


> 源码：[src/gameobjects/bitmaptext/dynamic/DynamicBitmapTextCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/dynamic/DynamicBitmapTextCreator.js#L12)  
引入版本：3.0.0


---

### gradient {#gradient}

#### \<instance> gradient(config, [addToScene]) {#instance-gradientconfig-addtoscene}


**说明:**

创建新的渐变游戏对象并返回它。 渐变是一个矩形游戏对象, 它使用 WebGL 使其表面的颜色梯度平滑。 它对于背景、 覆盖和装饰性视觉效果很有用, 因为在需要多彩的填充时不需要纹理。 位置、 大小和渐变外观都通过 `config` 对象来配置 。

注意:只有在渐变游戏对象和WebGL支持已经建入Phaser时,才能使用这种方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Gradient.GradientConfig](/api/typedef/types-gameobjects-gradient#gradientconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.Gradient](/api/class/gameobjects-gradient) - 创建的游戏对象 。


> 源码：[src/gameobjects/gradient/GradientCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/gradient/GradientCreator.js#L12)  
引入版本：4.0.0


---

### graphics {#graphics}

#### \<instance> graphics([config], [addToScene]) {#instance-graphicsconfig-addtoscene}


**说明:**

创建新的图形游戏对象并返回它。

注意:只有在图形游戏对象已建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Graphics.Options](/api/typedef/types-gameobjects-graphics#options) | 是 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) - 创建的游戏对象 。


> 源码：[src/gameobjects/graphics/GraphicsCreator.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/graphics/GraphicsCreator.js#L10)  
引入版本：3.0.0


---

### group {#group}

#### \<instance> group(config) {#instance-groupconfig}


**说明:**

创建新的 Group 游戏对象并返回它。

注意:只有在组游戏对象已建为Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Group.GroupConfig](/api/typedef/types-gameobjects-group#groupconfig) \| [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 创建的游戏对象 。


> 源码：[src/gameobjects/group/GroupCreator.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/GroupCreator.js#L10)  
引入版本：3.0.0


---

### image {#image}

#### \<instance> image(config, [addToScene]) {#instance-imageconfig-addtoscene}


**说明:**

创建新的图像游戏对象并返回它。

注意:只有当图像游戏对象已经建入Phaser时,此方法才会被使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.GameObjectConfig](/api/typedef/types-gameobjects#gameobjectconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.Image](/api/class/gameobjects-image) - 创建的游戏对象 。


> 源码：[src/gameobjects/image/ImageCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/image/ImageCreator.js#L12)  
引入版本：3.0.0


---

### layer {#layer}

#### \<instance> layer(config, [addToScene]) {#instance-layerconfig-addtoscene}


**说明:**

创建新的图层游戏对象并返回。

层是将其他游戏对象组合在一起的游戏对象的特殊类型。与容器不同,层不对其子进行任何转换。相反,层提供了管理渲染顺序的方法,并将后管线或效果应用到游戏对象的集合中,作为单单位。配置对象的`children`属性可以用来通过一系列游戏对象,以便在创建时立即添加到层中。

注意:只有在层游戏对象已建为Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Sprite.SpriteConfig](/api/typedef/types-gameobjects-sprite#spriteconfig) | 否 | 此游戏对象将用来创建自己的配置对象。 `children` 密钥可以设置到一系列游戏对象上, 以添加到图层中 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) - 创建的游戏对象 。


> 源码：[src/gameobjects/layer/LayerCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/layer/LayerCreator.js#L12)  
引入版本：3.50.0


---

### nineslice {#nineslice}

#### \<instance> nineslice(config, [addToScene]) {#instance-ninesliceconfig-addtoscene}


**说明:**

创建新的九切游戏对象并返回它。

注:只有在九切游戏对象和WebGL支持已经建入Phaser的情况下,才能使用这种方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.NineSlice.NineSliceConfig](/api/typedef/types-gameobjects-nineslice#ninesliceconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.NineSlice](/api/class/gameobjects-nineslice) - 创建的游戏对象 。


> 源码：[src/gameobjects/nineslice/NineSliceCreator.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSliceCreator.js#L13)  
引入版本：3.60.0


---

### noise {#noise}

#### \<instance> noise(config, [addToScene]) {#instance-noiseconfig-addtoscene}


**说明:**

创建新的噪音游戏对象并返回它。

噪音游戏对象使用遮蔽器直接将程序噪音(如Perlin或simplex location)放到WebGL四位星上,对产生动态视觉效果(如云,雾,地形预览),动画背景,或任何能从平滑,有机外观随机性中获益的效果都非常有用,噪音模式完全产生在GPU上,使得每个帧都具有非常高效的动画效果.

注意:只有在噪声游戏对象和WebGL支持已经建入Phaser时,这种方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Noise.NoiseConfig](/api/typedef/types-gameobjects-noise#noiseconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.Noise](/api/class/gameobjects-noise) - 创建的游戏对象 。


> 源码：[src/gameobjects/noise/NoiseCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/NoiseCreator.js#L12)  
引入版本：4.0.0


---

### noisecell2d {#noisecell2d}

#### \<instance> noisecell2d(config, [addToScene]) {#instance-noisecell2dconfig-addtoscene}


**说明:**

创建新的噪声Cell2D游戏对象并返回。

注意:只有在噪声Cell2D游戏对象和WebGL支持已经建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.NoiseCell2D.NoiseCell2DConfig](/api/typedef/types-gameobjects-noisecell2d#noisecell2dconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.NoiseCell2D](/api/class/gameobjects-noisecell2d) - 创建的游戏对象 。


> 源码：[src/gameobjects/noise/noisecell2d/NoiseCell2DCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell2d/NoiseCell2DCreator.js#L12)  
引入版本：4.0.0


---

### noisecell3d {#noisecell3d}

#### \<instance> noisecell3d(config, [addToScene]) {#instance-noisecell3dconfig-addtoscene}


**说明:**

创建新的NoiseCell3D游戏对象并返回。

注意:只有在将噪声Cell3D游戏对象和WebGL支持构建到Phaser中时,此方法才会被使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.NoiseCell3D.NoiseCell3DConfig](/api/typedef/types-gameobjects-noisecell3d#noisecell3dconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.NoiseCell3D](/api/class/gameobjects-noisecell3d) - 创建的游戏对象 。


> 源码：[src/gameobjects/noise/noisecell3d/NoiseCell3DCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell3d/NoiseCell3DCreator.js#L12)  
引入版本：4.0.0


---

### noisecell4d {#noisecell4d}

#### \<instance> noisecell4d(config, [addToScene]) {#instance-noisecell4dconfig-addtoscene}


**说明:**

创建新的噪声Cell4D游戏对象并返回。

注:只有在噪声Cell4D游戏对象和WebGL支持已经建入Phaser时,才能使用这种方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.NoiseCell4D.NoiseCell4DConfig](/api/typedef/types-gameobjects-noisecell4d#noisecell4dconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.NoiseCell4D](/api/class/gameobjects-noisecell4d) - 创建的游戏对象 。


> 源码：[src/gameobjects/noise/noisecell4d/NoiseCell4DCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell4d/NoiseCell4DCreator.js#L12)  
引入版本：4.0.0


---

### noisesimplex2d {#noisesimplex2d}

#### \<instance> noisesimplex2d(config, [addToScene]) {#instance-noisesimplex2dconfig-addtoscene}


**说明:**

创建新的噪声Simplex2D游戏对象并返回它。

注:只有在噪声Simplex2D游戏对象和WebGL支持已经建入Phaser时,这种方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.NoiseSimplex2D.NoiseSimplex2DConfig](/api/typedef/types-gameobjects-noisesimplex2d#noisesimplex2dconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.NoiseSimplex2D](/api/class/gameobjects-noisesimplex2d) - 创建的游戏对象 。


> 源码：[src/gameobjects/noise/noisesimplex2d/NoiseSimplex2DCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex2d/NoiseSimplex2DCreator.js#L12)  
引入版本：4.0.0


---

### noisesimplex3d {#noisesimplex3d}

#### \<instance> noisesimplex3d(config, [addToScene]) {#instance-noisesimplex3dconfig-addtoscene}


**说明:**

创建新的噪声Simplex3D游戏对象并返回它。

注:只有在噪声Simplex3D游戏对象和WebGL支持已经建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.NoiseSimplex3D.NoiseSimplex3DConfig](/api/typedef/types-gameobjects-noisesimplex3d#noisesimplex3dconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.NoiseSimplex3D](/api/class/gameobjects-noisesimplex3d) - 创建的游戏对象 。


> 源码：[src/gameobjects/noise/noisesimplex3d/NoiseSimplex3DCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex3d/NoiseSimplex3DCreator.js#L12)  
引入版本：4.0.0


---

### particles {#particles}

#### \<instance> particles(config, [addToScene]) {#instance-particlesconfig-addtoscene}


**说明:**

创建新的粒子 Emitter 游戏对象并返回。

粒子 Emitter 是一个基于配置对象生成粒子流的游戏对象,可用于产生爆炸,火,烟,雨等效果,或者任何其他基于粒子的视觉效果. 发射器被添加到景色中,并作为标准的游戏对象管理,支持变换,深度,以及其他常见属性.

在 Phaser v3.60 之前, 此函数将创建 `ParticleEmitterManager`。 这些功能在 v3. 60 中被删除, 并直接替换为 `ParticleEmitter` 实例。 请参看更新的函数参数和类文档 。

注意:只有在Particles Game Object被建入Phaser时,此方法才会被使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Particles.ParticleEmitterCreatorConfig](/api/typedef/types-gameobjects-particles#particleemittercreatorconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 创建的游戏对象 。


> 源码：[src/gameobjects/particles/ParticleEmitterCreator.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitterCreator.js#L13)  
引入版本：3.0.0


---

### pointlight {#pointlight}

#### \<instance> pointlight(config, [addToScene]) {#instance-pointlightconfig-addtoscene}


**说明:**

创建新的点光游戏对象并返回。

注意:只有在点光游戏对象已建入Phaser时,此方法才会被使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | object | 否 | 游戏对象将用来创建自己的配置对象。 支持的属性包括 `color` (光线的正色,默认值) `0xffffff`), `radius` (光线以像素表示,默认值) `128`), `intensity` (光亮度,默认值) `1`),以及 `attenuation` (光线向边缘掉落的速度,默认) `0.1`). |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.PointLight](/api/class/gameobjects-pointlight) - 创建的游戏对象 。


> 源码：[src/gameobjects/pointlight/PointLightCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/pointlight/PointLightCreator.js#L12)  
引入版本：3.50.0


---

### register {#register}

#### \<static> register(factoryType, factoryFunction) {#static-registerfactorytype-factoryfunction}


**说明:**

在Game ObjectCreator原型上注册一个游戏对象创建者功能,使其通过Scene的制作属性来创建游戏对象.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| factoryType | string | 否 | 工厂的钥匙,你用来叫Phaser.Scene.make[factoryType]方法。 |
| factoryFunction | function | 否 | 使用 Phaser.Scene.make 方法时要调用的构造器函数 。 |


> 源码：[src/gameobjects/GameObjectCreator.js#L154](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectCreator.js#L154)  
引入版本：3.0.0


---

### remove {#remove}

#### \<static> remove(factoryType) {#static-removefactorytype}


**说明:**

从游戏对象创建者原型中删除一个先前注册的游戏对象创建者,使其不再通过Scene的制作属性提供.

通过这种方法,您可以删除一个自定义的游戏对象创建器, 之前在游戏对象创建器中注册过。 以 `factoryType` 的方式通过它以删除它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| factoryType | string | 否 | 您想要从游戏对象创建器中移除的工厂密钥 。 |


> 源码：[src/gameobjects/GameObjectCreator.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectCreator.js#L173)  
引入版本：3.0.0


---

### renderTexture {#renderTexture}

#### \<instance> renderTexture(config, [addToScene]) {#instance-rendertextureconfig-addtoscene}


**说明:**

创建新的纹理游戏对象并返回它。

注意:只有在Render纹理游戏对象已建入Phaser时,此方法才会可用.

成形纹理是动态纹理和图像游戏对象的结合,使用动态纹理来显示自己.

动态纹理(Dynamic Texture)是一种特殊的纹理,它允许您直接绘制纹理,帧和最类游戏对象.

您可以带许多复杂的对象到这个纹理, 然后可以用来作为其他游戏对象, 如Sprites 的基础纹理。 如果您再更新这个纹理, 所有使用它的游戏对象都会立即更新, 立即反映变化 。

这是一种强大的方法,在运行时生成动态纹理,这种纹理是WebGL友好的,并且不会在每个变化上引用昂贵的GPU上传.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.RenderTexture.RenderTextureConfig](/api/typedef/types-gameobjects-rendertexture#rendertextureconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.RenderTexture](/api/class/gameobjects-rendertexture) - 创建的游戏对象 。


> 源码：[src/gameobjects/rendertexture/RenderTextureCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rendertexture/RenderTextureCreator.js#L12)  
引入版本：3.2.0


---

### rope {#rope}

#### \<instance> rope(config, [addToScene]) {#instance-ropeconfig-addtoscene}


**说明:**

创建新的游戏绳索对象并返回它。

绳索是仅使用WebGL的游戏对象,它使一条带纹三角形沿一系列点形成一条带纹三角形。这使它最理想地可以创建绳索、丝带、布或其他柔性带纹状视觉效果。这些点定义绳索的脊椎,纹理被拉伸,并绘制在所形成的网格上。可以设定顶点颜色和α值,以在绳索长度上产生梯度或淡化效果。

注意:只有在将绳形游戏对象和WebGL支持构建为Phaser时,此方法才会被使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Rope.RopeConfig](/api/typedef/types-gameobjects-rope#ropeconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.Rope](/api/class/gameobjects-rope) - 创建的游戏对象 。


> 源码：[src/gameobjects/rope/RopeCreator.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/RopeCreator.js#L13)  
引入版本：3.23.0


---

### shader {#shader}

#### \<instance> shader(config, [addToScene]) {#instance-shaderconfig-addtoscene}


**说明:**

创建新的Shader游戏对象并返回它。

注意:只有在将Shader游戏对象和WebGL支持构建为Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Shader.ShaderConfig](/api/typedef/types-gameobjects-shader#shaderconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.Shader](/api/class/gameobjects-shader) - 创建的游戏对象 。


> 源码：[src/gameobjects/shader/ShaderCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/shader/ShaderCreator.js#L12)  
引入版本：3.17.0


---

### sprite {#sprite}

#### \<instance> sprite(config, [addToScene]) {#instance-spriteconfig-addtoscene}


**说明:**

创建新的 Sprite 游戏对象并返回它。

注意:只有在Sprite游戏对象已经建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | [Phaser.Types.GameObjects.Sprite.SpriteConfig](/api/typedef/types-gameobjects-sprite#spriteconfig) | 否 |  | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | true | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.Sprite](/api/class/gameobjects-sprite) - 创建的游戏对象 。


> 源码：[src/gameobjects/sprite/SpriteCreator.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/SpriteCreator.js#L13)  
引入版本：3.0.0


---

### spriteGPULayer {#spriteGPULayer}

#### \<instance> spriteGPULayer(config, [addToScene]) {#instance-spritegpulayerconfig-addtoscene}


**说明:**

创建新的 SpriteGPULayer 游戏对象并返回它。

注意:只有在SpriteGPULayer游戏对象已经建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.SpriteGPULayer.SpriteGPULayerConfig](/api/typedef/types-gameobjects-spritegpulayer#spritegpulayerconfig) | 否 | 此游戏对象将用来创建自己的配置对象。 `size` 属性设定了图示层的最大数量, 如果未指定则默认为 1 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.SpriteGPULayer](/api/class/gameobjects-spritegpulayer) - 创建的游戏对象 。


> 源码：[src/gameobjects/spritegpulayer/SpriteGPULayerCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/spritegpulayer/SpriteGPULayerCreator.js#L12)  
引入版本：4.0.0


---

### stamp {#stamp}

#### \<instance> stamp(config, [addToScene]) {#instance-stampconfig-addtoscene}


**说明:**

创建新的邮票游戏对象并返回它。

注意:只有在将Stamp Game Object建为Phaser时,此方法才会被使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Sprite.SpriteConfig](/api/typedef/types-gameobjects-sprite#spriteconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.Stamp](/api/class/gameobjects-stamp) - 创建的游戏对象 。


> 源码：[src/gameobjects/stamp/StampCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/stamp/StampCreator.js#L12)  
引入版本：4.0.0


---

### text {#text}

#### \<instance> text(config, [addToScene]) {#instance-textconfig-addtoscene}


**说明:**

创建新的文本游戏对象并返回它。

一个文本游戏对象将一串文本变成内部的 Canvas 纹理, 然后用作向游戏画布渲染的源头。 它支持一系列广泛的样式选项, 包括字体家族、大小、重量、填色、中风、投影、文本对齐、文字包装、 贴补、 固定尺寸和右到左的渲染。 文本内容和样式可以在创建后随时更新 。

与工厂方法(`scene.add.text`)不同,这种创建方法返回文本游戏对象,而不会自动添加到Scene的显示列表中. 使用配置对象中的`add`属性,或者通过`true`作为`addToScene`参数,将其添加到Scene中.

注意:只有在文本游戏对象已建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Text.TextConfig](/api/typedef/types-gameobjects-text#textconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.Text](/api/class/gameobjects-text) - 创建的游戏对象 。


> 源码：[src/gameobjects/text/TextCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/text/TextCreator.js#L12)  
引入版本：3.0.0


---

### tilemap {#tilemap}

#### \<instance> tilemap([config]) {#instance-tilemapconfig}


**说明:**

从给定的密钥或数据创建一个 Tilemap, 或如果没有提供密钥/数据而创建空白的 Tilemap。从 CSV 或 2D 阵列加载时, 您应该指定 tileWidth & tileHeight。从图中解析时, tileWidth, tileHeight,宽度和高度将从地图数据中拉出。对于空地图,您应当指定 tileWidth, tileHeight,宽度和高度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Tilemaps.TilemapConfig](/api/typedef/types-tilemaps#tilemapconfig) | 是 | Tilemap 的配置选项 。 |


**返回值:** [Phaser.Tilemaps.Tilemap](/api/class/tilemaps-tilemap) - 


> 源码：[src/tilemaps/TilemapCreator.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/TilemapCreator.js#L10)  
引入版本：3.0.0


---

### tileSprite {#tileSprite}

#### \<instance> tileSprite(config, [addToScene]) {#instance-tilespriteconfig-addtoscene}


**说明:**

创建新的 TileSprite 游戏对象并返回它。

注意:只有在TileSprite游戏对象已建入Phaser时,此方法才会被使用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.TileSprite.TileSpriteConfig](/api/typedef/types-gameobjects-tilesprite#tilespriteconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.TileSprite](/api/class/gameobjects-tilesprite) - 创建的游戏对象 。


> 源码：[src/gameobjects/tilesprite/TileSpriteCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/tilesprite/TileSpriteCreator.js#L12)  
引入版本：3.0.0


---

### tween {#tween}

#### \<instance> tween(config) {#instance-tweenconfig}


**说明:**

创建新的 Tween 对象并返回它。

注:只有将Tweens建入Phaser时,才能使用这种方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Tweens.TweenBuilderConfig](/api/typedef/types-tweens#tweenbuilderconfig) \| [Phaser.Types.Tweens.TweenChainBuilderConfig](/api/typedef/types-tweens#tweenchainbuilderconfig) | [Phaser.Tweens.Tween](/api/class/tweens-tween) | [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) | 否 | Tween 配置对象,或 Tween 或 TweenChain 实例 。 |


**返回值:** [Phaser.Tweens.Tween](/api/class/tweens-tween) - 所创之特温.


> 源码：[src/tweens/tween/Tween.js#L850](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Tween.js#L850)  
引入版本：3.0.0


---

### tweenchain {#tweenchain}

#### \<instance> tweenchain(config) {#instance-tweenchainconfig}


**说明:**

创建新的 TweenChain 对象并返回,而不添加到 Tween 管理器中 。

注:只有将Tweens建入Phaser时,才能使用这种方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Tweens.TweenBuilderConfig](/api/typedef/types-tweens#tweenbuilderconfig) \| object | 否 | 特温钱组合. |


**返回值:** [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) - 所创之特温琴.


> 源码：[src/tweens/tween/TweenChain.js#L566](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/TweenChain.js#L566)  
引入版本：3.60.0


---

### video {#video}

#### \<instance> video(config, [addToScene]) {#instance-videoconfig-addtoscene}


**说明:**

创建新的视频游戏对象并返回它。

注意:只有在游戏对象已建入Phaser时,此方法才会可用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Video.VideoConfig](/api/typedef/types-gameobjects-video#videoconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |
| addToScene | boolean | 是 | 创建此游戏对象后添加到场景中 ? 如果设置此参数将覆盖配置对象中的 `add` 属性 。 |


**返回值:** [Phaser.GameObjects.Video](/api/class/gameobjects-video) - 创建的游戏对象 。


> 源码：[src/gameobjects/video/VideoCreator.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/video/VideoCreator.js#L12)  
引入版本：3.20.0


---

### zone {#zone}

#### \<instance> zone(config) {#instance-zoneconfig}


**说明:**

创建新的区域游戏对象并返回。

注意: 只有在 Zone 游戏对象已建入时, 才能使用此方法 Phaser.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Zone.ZoneConfig](/api/typedef/types-gameobjects-zone#zoneconfig) | 否 | 此游戏对象将用来创建自己的配置对象 。 |


**返回值:** [Phaser.GameObjects.Zone](/api/class/gameobjects-zone) - 创建的游戏对象 。


> 源码：[src/gameobjects/zone/ZoneCreator.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/zone/ZoneCreator.js#L11)  
引入版本：3.0.0


---

## 公开成员 {#public-members}

### displayList {#displayList}

#### displayList: [Phaser.GameObjects.DisplayList](/api/class/gameobjects-displaylist) {#displaylist-phasergameobjectsdisplaylist}


**说明:**

用于引用场景显示列表的参考 。


**Access:** 保护


> 源码：[src/gameobjects/GameObjectCreator.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectCreator.js#L63)  
引入版本：3.0.0


---

### events {#events}

#### events: [Phaser.Events.EventEmitter](/api/class/events-eventemitter) {#events-phasereventseventemitter}


**说明:**

参考景点事件 Emitter.


**Access:** 保护


> 源码：[src/gameobjects/GameObjectCreator.js#L53](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectCreator.js#L53)  
引入版本：3.50.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

此游戏对象创建者所属景区 。


**Access:** 保护


> 源码：[src/gameobjects/GameObjectCreator.js#L33](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectCreator.js#L33)  
引入版本：3.0.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

参考神话. 连载.


**Access:** 保护


> 源码：[src/gameobjects/GameObjectCreator.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectCreator.js#L43)  
引入版本：3.0.0


---

### updateList {#updateList}

#### updateList: [Phaser.GameObjects.UpdateList](/api/class/gameobjects-updatelist) {#updatelist-phasergameobjectsupdatelist}


**说明:**

参考景区更新列表.


**Access:** 保护


> 源码：[src/gameobjects/GameObjectCreator.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObjectCreator.js#L73)  
引入版本：3.0.0


---

---
