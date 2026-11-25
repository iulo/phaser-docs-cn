# Mask {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-mask)

遮罩过滤器控制器 。

此过滤器控制器管理一个掩码效果 。

遮罩使用纹理来隐藏输入的部分,它将遮罩的α在相应的texel中输入的颜色和α相乘.

遮罩可以反转, 开关他们隐藏的东西和他们展示的东西。

遮罩可以使用纹理或游戏对象。如果使用游戏对象,遮罩会使游戏对象变成动态图案,并使用该图案。当游戏对象改变时,遮罩会自动更新,除非`autoUpdate`旗设定为`false`。

当遮罩过滤器被用作内部过滤器时,遮罩将匹配被过滤的对象/视图。这对创建随对象而来的效果是有用的,例如意在匹配动画图案的效果。

当遮罩滤镜被用作外部滤镜时,遮罩会匹配摄像机的上下文,这对创建覆盖整个视图的效果很有用.

在创建掩码时可以指定一个可选的 `viewCamera`。如果不使用,则会通过当前摄像机或默认摄像机查看掩码对象,如果没有其他选项,则会通过默认摄像机查看。例如,在正常渲染流外向动态图渲染时。

通过过滤列表组件,将遮罩效果添加到摄像机中:

```js
const camera = this.cameras.main;
const texture = 'MyMask';

camera.filters.internal.addMask(texture);
camera.filters.external.addMask(texture, true, myCamera);
```

**构造函数**

`new Mask(camera, [mask], [invert], [viewCamera], [viewTransform], [scaleFactor])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的摄像机。 |
| mask | string \| [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 是 | "'__WHITE'" | 遮罩的来源。 这可以是用于遮罩的独特的基于字符串的纹理键, 它必须存在于纹理管理器中。 或者它可以是 Game Object, 在这种情况下, 遮罩会让 Game Objects 变成动态图解并使用 。 |
| invert | boolean | 是 | false | 是否要反转遮罩 。 |
| viewCamera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 |  | 使用 Game Object 渲染遮罩时使用的摄像机。 如果没有指定, 请使用该场景的 `main` 摄像机 。 |
| viewTransform | 'local' \| 'world' | 是 | "'world'" | 使用 Game Object 渲染掩码时使用的转换 。 “ 本地” 使用 Game October 的属性 。 “ 世界” 使用 GameObject 的 `parentContainer` 值来计算世界位置 。 |
| scaleFactor | number | 是 | 1 | 适用于底部遮罩纹理的尺度因子。 可用于平衡内存使用和所需的遮罩精度。 这只调整纹理的大小; 您还必须调整遮罩大小以匹配, 例如, scaleFactor为0. 5, 您的遮罩可能是带有0. 5 尺度的容器。 当组合尺度因子、 对象转换和摄像机转换时, 很容易使事情变得复杂, 所以在使用此选项时要尽量精确 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Mask.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Mask.js#L11)  
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

### autoUpdate {#autoUpdate}

#### autoUpdate: boolean {#autoupdate-boolean}


**说明:**

遮罩是否应该自动更新。 仅当遮罩是 Game Object 时才适用。 如果 `false` , 遮罩即使 Game Object 更改也不会改变 。


> 源码：[src/filters/Mask.js#L120](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Mask.js#L120)  
引入版本：4.0.0


---

### glTexture {#glTexture}

#### glTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) {#gltexture-phaserrendererwebglwrapperswebgltexturewrapper}


**说明:**

遮罩的内在纹理


> 源码：[src/filters/Mask.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Mask.js#L77)  
引入版本：4.0.0


---

### invert {#invert}

#### invert: boolean {#invert-boolean}


**说明:**

是否反转遮罩。 反转遮罩会切换它隐藏的和显示的 。


> 源码：[src/filters/Mask.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Mask.js#L109)  
引入版本：4.0.0


---

### maskGameObject {#maskGameObject}

#### maskGameObject: [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) {#maskgameobject-phasergameobjectsgameobject}


**说明:**

用于遮罩的游戏对象。 只有在遮罩是 Game Object 时才会设定 。


> 源码：[src/filters/Mask.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Mask.js#L98)  
引入版本：4.0.0


---

### needsUpdate {#needsUpdate}

#### needsUpdate: boolean {#needsupdate-boolean}


**说明:**

是否需要更新遮罩, 一次。 仅当遮罩是 Game Object 时才适用。 如果 `true` , 遮罩将在下一次渲染前更新。 当遮罩是 Game Ocject 时, 自动设置为 `true`, 但遮罩更新后关闭 。


> 源码：[src/filters/Mask.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Mask.js#L132)  
引入版本：4.0.0


---

### scaleFactor {#scaleFactor}

#### scaleFactor: number {#scalefactor-number}


**说明:**

适用于底部遮罩纹理的尺度因子。 低于 1 值会降低纹理分辨率, 以掩罩精度为代价保存内存。 大于 1 值会增加清晰的遮罩分辨率, 但使用更多的内存。 当更改此值时, 您还必须将遮罩 Game Object 或 Contain 缩放以匹配, 这样其输出会正确填补纹理 。


> 源码：[src/filters/Mask.js#L170](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Mask.js#L170)  
引入版本：4.0.0


---

### viewCamera {#viewCamera}

#### viewCamera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#viewcamera-phasercamerasscene2dcamera}


**说明:**

用于制作遮罩的摄像机。 如果未指定, 则使用当前渲染摄像机, 或者失败, 即内部摄像机 。


> 源码：[src/filters/Mask.js#L159](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Mask.js#L159)  
引入版本：4.0.0


---

### viewTransform {#viewTransform}

#### viewTransform: 'local', 'world' {#viewtransform-local-world}


**说明:**

在使用 Game Object 渲染掩码时使用的变换类型。 “ 本地” 使用 Game Oblem 的属性 。 “ 世界” 使用 GameObject 的 `parentContainer` 值来计算世界位置 。 仅在 掩码为 Game Objects 时才适用 。


> 源码：[src/filters/Mask.js#L146](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Mask.js#L146)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Filters.Controller](/api/class/filters-controller):**


 - [getPadding](/api/class/filters-controller#getPadding)
 - [getPaddingCeil](/api/class/filters-controller#getPaddingCeil)
 - [setActive](/api/class/filters-controller#setActive)
 - [setPaddingOverride](/api/class/filters-controller#setPaddingOverride)




---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此过滤器, 释放所有引用和资源 。

如果为遮罩游戏对象创建了动态纹理,它也会被销毁.


**重写:** Phaser.Filters.Controller#销毁


> 源码：[src/filters/Mask.js#L294](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Mask.js#L294)  
引入版本：4.0.0


---

### setGameObject {#setGameObject}

#### \<instance> setGameObject(gameObject) {#instance-setgameobjectgameobject}


**说明:**

设置用于遮罩的游戏对象。 游戏对象将在下一个渲染通道上被渲染为内部动态显示。 设置一个新的游戏对象也会将 `needsUpdate` 设置为 `true`, 确保在绘制下一个框架前刷新纹理 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 用于遮罩的游戏对象 。 |


**返回值:** [Phaser.Filters.Mask](/api/class/filters-mask) - 此过滤控制器 。


> 源码：[src/filters/Mask.js#L246](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Mask.js#L246)  
引入版本：4.0.0


---

### setTexture {#setTexture}

#### \<instance> setTexture([texture]) {#instance-settexturetexture}


**说明:**

设置一个静态纹理作为遮罩使用, 由纹理管理器的键查找。 任何先前指定的遮罩 Game Object 都被清除。 与 Game Objects 掩码不同, 静态纹理掩码不会在帧之间自动更新 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| texture | string | 是 | "'__WHITE'" | 用于遮罩的纹理中唯一基于字符串的键,它必须存在于纹理管理器中. |


**返回值:** [Phaser.Filters.Mask](/api/class/filters-mask) - 此过滤控制器 。


> 源码：[src/filters/Mask.js#L270](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Mask.js#L270)  
引入版本：4.0.0


---

### updateDynamicTexture {#updateDynamicTexture}

#### \<instance> updateDynamicTexture(width, height) {#instance-updatedynamictexturewidth-height}


**说明:**

更新掩码的动态图案。 必要时, 创建或调整了动态图案。 当掩码是游戏对象, 并设置了 `needsUpdate`或 `autoUpdate` 标记时, 其自动调用。 不应直接调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 动态图的宽度 。 |
| height | number | 否 | 动态图解的高度. |


> 源码：[src/filters/Mask.js#L195](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Mask.js#L195)  
引入版本：4.0.0


---

---
