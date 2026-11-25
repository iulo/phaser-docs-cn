# NormalTools {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-normaltools)

普通工具过滤控制器 。

此过滤控制器管理摄像机的正常工具效果 。

普通工具是用于操纵普通地图的正常功能的过滤器。它具有以下几种功能:

- 旋转或调整普通地图。

- 改变正常人面对镜头的强烈程度.

- 输出灰色的纹理,显示正常人面对摄像机的强度,或者其他的向量.

输出可用于各种目的,例如:

- 编辑用于特殊应用程序的普通地图。

- 通过操纵面力来改变普通地图的明显视觉深度.

- 创建其它效果的基点,例如用于梯度或其他效果的遮罩.

您甚至可以使用输出作为常规照明的普通地图。 通常, 普通地图会和主纹理一起加载, 但您可以覆盖此功能 。

```js
// Given a dynamic texture `dyn` where the filter output is drawn,
// and a texture `spiderTex` with lighting enabled,
// we can inject the WebGL texture straight into the scene lighting as a normal map.
spiderTex.setDataSource(dyn.getWebGLTexture());
```

通过过滤列表组件,将正常工具效应添加到摄像机中:

```js
const camera = this.cameras.main;
camera.filters.internal.addNormalTools({
    rotation: 0,
    facingPower: 1,
    outputRatio: false,
    ratioVector: [ 0, 0, 1 ],
    ratioRadius: 1
});
camera.filters.external.addNormalTools({});
```

**构造函数**

`new NormalTools(camera, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 拥有这个过滤器的摄像机. |
| config | [Phaser.Types.Filters.NormalToolsConfig](/api/typedef/types-filters#normaltoolsconfig) | 是 | 普通工具效果的配置对象。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/NormalTools.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/NormalTools.js#L12)  
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

### facingPower {#facingPower}

#### facingPower: number {#facingpower-number}


**说明:**

面部效果的功率。 值较高会向摄像机弯曲; 值较低会将其弯曲。 这对建议 2D 场景的深度很有用 。


> 源码：[src/filters/NormalTools.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/NormalTools.js#L113)  
引入版本：4.0.0


---

### outputRatio {#outputRatio}

#### outputRatio: boolean {#outputratio-boolean}


**说明:**

是否输出普通地图的比例。 如果输出是真实的, 输出将是灰色的纹理, 白色区域是正常人面对摄像机的区域, 向正交时会变黑。 您可以用 `ratioVector` 和 `ratioRadius` 来操纵这个比例。 这可以作为其他效果的基点 。


> 源码：[src/filters/NormalTools.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/NormalTools.js#L125)  
引入版本：4.0.0


---

### ratioRadius {#ratioRadius}

#### ratioRadius: number {#ratioradius-number}


**说明:**

比例输出时, 需要考虑一个半球的多少。 1 时, 将计算整个半球的比例。 0时, 将计算一个点的比例。 这使用与 `PanoramaBlur.radius` 相同的算法 。

只有在 outputRatio 属实时才使用此功能.


> 源码：[src/filters/NormalTools.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/NormalTools.js#L158)  
引入版本：4.0.0


---

### ratioVector {#ratioVector}

#### ratioVector: [Phaser.Math.Vector3](/api/class/math-vector3) {#ratiovector-phasermathvector3}


**说明:**

比例输出使用的矢量。 这是计算比例的方向。 默认是摄像机的前进方向。 操纵此方向可以突出显示地图中正面临特定方向的部分 。

只有在 outputRatio 属实时才使用此功能.


> 源码：[src/filters/NormalTools.js#L140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/NormalTools.js#L140)  
引入版本：4.0.0


---

### rotationSource {#rotationSource}

#### rotationSource: [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject), [Phaser.Types.Filters.NormalToolsSourceCallback](/api/typedef/types-filters#normaltoolssourcecallback), null {#rotationsource-phasergameobjectsgameobject-phasertypesfiltersnormaltoolssourcecallback-null}


**说明:**

旋转的来源。 如果函数, 则会叫它来获得旋转。 如果是游戏对象, 则它会用来从游戏对象的世界变换中获取旋转。 如果无效, 旋转将不会被过滤器更新 。


> 源码：[src/filters/NormalTools.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/NormalTools.js#L101)  
引入版本：4.0.0


---

### viewMatrix {#viewMatrix}

#### viewMatrix: [Phaser.Math.Matrix4](/api/class/math-matrix4) {#viewmatrix-phasermathmatrix4}


**说明:**

用于普通工具效果的视图矩阵。 此矩阵控制了普通地图的方向。 使用此矩阵来控制普通地图的3D旋转。 通常情况下, 您只使用 `setRotation`来旋转 2D 。


> 源码：[src/filters/NormalTools.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/NormalTools.js#L87)  
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

### getRotation {#getRotation}

#### \<instance> getRotation() {#instance-getrotation}


**说明:**

获得普通地图的2D旋转,由`setRotation`或`rotationSource`设定.

如果 `viewMatrix` 直接被操纵, 即用于3D旋转, 此值并不准确。 没有单一的值能够准确代表3D旋转 。


**返回值:** number - 弧度旋转.


> 源码：[src/filters/NormalTools.js#L174](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/NormalTools.js#L174)  
引入版本：4.0.0


---

### setRotation {#setRotation}

#### \<instance> setRotation(rotation) {#instance-setrotationrotation}


**说明:**

设置普通地图的旋转。 这将 `viewMatrix` 设置为 Z轴周围的旋转, 适合 2D 旋转。 对于更高级的控制, 操纵过滤器的 `viewMatrix` 来控制 3D 旋转 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rotation | number | 否 | 弧度旋转. |


**返回值:** [Phaser.Filters.NormalTools](/api/class/filters-normaltools) - 这个普通工具的例子 。


> 源码：[src/filters/NormalTools.js#L204](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/NormalTools.js#L204)  
引入版本：4.0.0


---

### updateRotation {#updateRotation}

#### \<instance> updateRotation() {#instance-updaterotation}


**说明:**

更新普通地图从 rotationSource,如果设置了。在渲染过程中自动调用。


**返回值:** [Phaser.Filters.NormalTools](/api/class/filters-normaltools) - 这个普通工具的例子 。


> 源码：[src/filters/NormalTools.js#L223](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/NormalTools.js#L223)  
引入版本：4.0.0


---

---
