# ImageLight {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-imagelight)

图像光过滤控制器 。

此过滤器控制器管理相机的图像光效应 。

图像灯(ImageLight)是用于图像基照明(IBL)的滤镜,用于使用环境图和普通地图模拟图像的照明.

环境图是描述场景照明的图像,此过滤器使用单一全景图作为环境图,图像的顶部是天空,底部是地面,X轴覆盖全旋转,这种图像向上和底部扭曲,因为X轴伸展宽,所以如果您正在创建自己的环境图,请小心.

立方体地图在撰写时不由Phaser支持.

效果基本上是无限范围内的环境反射。 锐利的环境图将产生尖锐的反射, 而模糊的环境图则会产生分散的反射。 使用全景图Blur过滤器来创建正确的模糊的环境图。 必要时使用普通工具过滤器来操纵普通的地图, 使用动态图来捕捉输出 。

图像灯效果通过过滤列表组件添加到相机中:

```js
const camera = this.cameras.main;

camera.filters.internal.addImageLight({ texture: 'lightmap' });
camera.filters.external.addImageLight({ texture: 'lightmap' });
```

**构造函数**

`new ImageLight(camera, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 拥有这个过滤器的相机. |
| config | [Phaser.Types.Filters.ImageLightConfig](/api/typedef/types-filters#imagelightconfig) | 是 | 图像光效果的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/ImageLight.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ImageLight.js#L12)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Filters.Controller](/api/class/filters-controller):**


 - [active](/api/class/filters-controller#active)
 - [allowBaseDraw](/api/class/filters-controller#allowBaseDraw)
 - [camera](/api/class/filters-controller#camera)
 - [currentPadding](/api/class/filters-controller#currentPadding)
 - [ignoreDestroy](/api/class/filters-controller#ignoreDestroy)
 - [paddingOverride](/api/class/filters-controller#paddingOverride)
 - [renderNode](/api/class/filters-controller#renderNode)




---

## 公开成员 {#public-members}

### bulge {#bulge}

#### bulge: number {#bulge-number}


**说明:**

用于图像光效应的凸起量。 这略微扭曲了表面, 防止了普通地图中的平面区域反映单一的平面颜色。 值为 0.1 的值往往很充足 。


> 源码：[src/filters/ImageLight.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ImageLight.js#L114)  
引入版本：4.0.0


---

### colorFactor {#colorFactor}

#### colorFactor: Array.\<number> {#colorfactor-arraynumber}


**说明:**

适用于图像光效应的颜色因子。这可以乘以每个色通道中光线的强度。使用高于1的值来取代高动态范围照明。


> 源码：[src/filters/ImageLight.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ImageLight.js#L125)  
引入版本：4.0.0


---

### environmentGlTexture {#environmentGlTexture}

#### environmentGlTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#environmentgltexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

图像光效应环境图所使用的基础纹理.


> 源码：[src/filters/ImageLight.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ImageLight.js#L72)  
引入版本：4.0.0


---

### modelRotation {#modelRotation}

#### modelRotation: number {#modelrotation-number}


**说明:**

模型的初始旋转值为弧度。 如果设定了, 则该值会被 modelRotationSource 覆盖 。


> 源码：[src/filters/ImageLight.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ImageLight.js#L92)  
引入版本：4.0.0


---

### modelRotationSource {#modelRotationSource}

#### modelRotationSource: [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject), [Phaser.Types.Filters.ImageLightSourceCallback](/api/typedef/types-filters#imagelightsourcecallback), null {#modelrotationsource-phasergameobjectsgameobject-phasertypesfiltersimagelightsourcecallback-null}


**说明:**

用于过滤器时使用的模型旋转源。 如果函数, 则会叫它来获得旋转。 如果是 Game Object, 则它会用来从 Game Objects 的世界转换中获取旋转。 如果无效, 模型旋转将取自 modelRotation 属性 。


> 源码：[src/filters/ImageLight.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ImageLight.js#L102)  
引入版本：4.0.0


---

### normalGlTexture {#normalGlTexture}

#### normalGlTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#normalgltexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

图像光效应普通地图所使用的基础纹理.


> 源码：[src/filters/ImageLight.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ImageLight.js#L63)  
引入版本：4.0.0


---

### viewMatrix {#viewMatrix}

#### viewMatrix: [Phaser.Math.Matrix4](/api/class/math-matrix4) {#viewmatrix-phasermathmatrix4}


**说明:**

图像光效果使用的视图矩阵。此矩阵控制环境图的方向。 您应该设置此矩阵来反映相机的视角 。


> 源码：[src/filters/ImageLight.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ImageLight.js#L81)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Filters.Controller](/api/class/filters-controller):**


 - [destroy](/api/class/filters-controller#destroy)
 - [getPadding](/api/class/filters-controller#getPadding)
 - [getPaddingCeil](/api/class/filters-controller#getPaddingCeil)
 - [setActive](/api/class/filters-controller#setActive)
 - [setPaddingOverride](/api/class/filters-controller#setPaddingOverride)




---

## 公开方法 {#public-methods}

### getModelRotation {#getModelRotation}

#### \<instance> getModelRotation() {#instance-getmodelrotation}


**说明:**

获得用于图像光效果的旋转。 如果设定了, 这将使用 modelRotationSource 。


**返回值:** number - 弧度中用于图像光效应的旋转.


> 源码：[src/filters/ImageLight.js#L225](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ImageLight.js#L225)  
引入版本：4.0.0


---

### setEnvironmentMap {#setEnvironmentMap}

#### \<instance> setEnvironmentMap(texture) {#instance-setenvironmentmaptexture}


**说明:**

设置用于图像光效应环境图的纹理。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 图像光效应环境图所用的纹理 。 |


**返回值:** [Phaser.Filters.ImageLight](/api/class/filters-imagelight) - 这个图像灯实例 。


> 源码：[src/filters/ImageLight.js#L162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ImageLight.js#L162)  
引入版本：4.0.0


---

### setNormalMap {#setNormalMap}

#### \<instance> setNormalMap(texture) {#instance-setnormalmaptexture}


**说明:**

设置用于图像光效果普通映射的纹理。这应该与被过滤的对象匹配。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 图像光效果普通映射所用的纹理 。 |


**返回值:** [Phaser.Filters.ImageLight](/api/class/filters-imagelight) - 这个图像灯实例 。


> 源码：[src/filters/ImageLight.js#L182](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ImageLight.js#L182)  
引入版本：4.0.0


---

### setNormalMapFromGameObject {#setNormalMapFromGameObject}

#### \<instance> setNormalMapFromGameObject(gameObject) {#instance-setnormalmapfromgameobjectgameobject}


**说明:**

设置用于 Game Object 图像光效果的正常纹理。 这将使用对象纹理中的第一个数据源图像。 使用此功能提取一个作为数据源加载的普通地图 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 用于图像光效果普通映射的游戏对象 。 |


**返回值:** [Phaser.Filters.ImageLight](/api/class/filters-imagelight) - 这个图像灯实例 。


> 源码：[src/filters/ImageLight.js#L203](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ImageLight.js#L203)  
引入版本：4.0.0


---

---
