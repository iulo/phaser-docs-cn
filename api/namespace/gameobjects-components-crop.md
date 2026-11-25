# Phaser.GameObjects.Components.Crop {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-crop)

Scope: 
static
> 源码：[src/gameobjects/components/Crop.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Crop.js#L7)  
引入版本：3.12.0

## 静态函数 {#static-functions}

### frame {#frame}

#### frame: [Phaser.Textures.Frame](/api/class/textures-frame) {#frame-phasertexturesframe}


**说明:**

此游戏对象正在使用质地框架来渲染 。


> 源码：[src/gameobjects/components/Crop.js#L31](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Crop.js#L31)  
引入版本：3.0.0


---

### isCropped {#isCropped}

#### isCropped: boolean {#iscropped-boolean}


**说明:**

显示此游戏对象是否正在被裁剪的布尔旗。 您可以在 `setCrop` 被调用后随时切换, 打开或关闭。 同样, 拨打 `setCrop` 时没有参数会重置并禁用它 。


> 源码：[src/gameobjects/components/Crop.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Crop.js#L40)  
引入版本：3.11.0


---

### texture {#texture}

#### texture: [Phaser.Textures.Texture](/api/class/textures-texture), [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) {#texture-phasertexturestexture-phasertexturescanvastexture}


**说明:**

游戏对象所用的质素 。


> 源码：[src/gameobjects/components/Crop.js#L22](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Crop.js#L22)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### setCrop {#setCrop}

#### \<instance> setCrop([x], [y], [width], [height]) {#instance-setcropx-y-width-height}


**说明:**

将一个裁剪应用到基于纹理的游戏对象,例如Sprite或Image.

裁剪是一个矩形,它限制了渲染时可见的纹理帧的区域.

裁剪游戏对象不会改变其大小,尺寸,物理体或命中区域,它只是改变在渲染时显示的内容.

作物大小以及坐标不能超过纹理帧的大小。

裁剪坐标相对纹理帧,而非Game Object,意思是0 x 0是左上角.

因此,如果你有一个游戏对象,有一个800x600大小的纹理,并且你想只显示其左半部,你可以叫`setCrop(0, 0, 400, 600)`.

也可以自动调整它,以匹配游戏对象的尺度。因此,如果一个大小因子为2的游戏对象被应用,则100x50的裁剪矩会裁剪面积为200x100。

您可以直接通过数字值,也可以提供单个矩形对象作为第一个参数。

使用这个完全没有参数的方法来重设裁剪, 或者将属性 `isCropped` 切换为 `false` 。

如果裁剪矩形变成与框架本身相同的大小,您应该这样做,因为它会让渲染器跳过多个内部计算.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number \| [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 启动裁剪的x坐标。 无法是负数或超过框架宽度。 或是一个 Phaser.Geom.Rectangle 对象, 此时忽略了其余参数 。 |
| y | number | 是 | 启动裁剪的 Y 坐标。 无法为负或超过框架高度 。 |
| width | number | 是 | 裁剪矩形的宽度, 以像素计。 无法超过框架宽度 。 |
| height | number | 是 | 裁剪矩形的高度, 以像素计。 无法超过框架高度 。 |


**返回值:** [Phaser.GameObjects.Components.Crop](/api/namespace/gameobjects-components-crop) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Crop.js#L51](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Crop.js#L51)  
引入版本：3.11.0


---

---
