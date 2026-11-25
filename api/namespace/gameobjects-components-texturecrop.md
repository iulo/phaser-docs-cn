# Phaser.GameObjects.Components.TextureCrop {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-texturecrop)

Scope: 
static
> 源码：[src/gameobjects/components/TextureCrop.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TextureCrop.js#L12)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### frame {#frame}

#### frame: [Phaser.Textures.Frame](/api/class/textures-frame) {#frame-phasertexturesframe}


**说明:**

此游戏对象正在使用质地框架来渲染 。


> 源码：[src/gameobjects/components/TextureCrop.js#L30](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TextureCrop.js#L30)  
引入版本：3.0.0


---

### isCropped {#isCropped}

#### isCropped: boolean {#iscropped-boolean}


**说明:**

显示此游戏对象是否正在被裁剪的布尔旗。 您可以在 `setCrop` 被调用后随时切换, 打开或关闭。 同样, 拨打 `setCrop` 时没有参数会重置并禁用它 。


> 源码：[src/gameobjects/components/TextureCrop.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TextureCrop.js#L39)  
引入版本：3.11.0


---

### texture {#texture}

#### texture: [Phaser.Textures.Texture](/api/class/textures-texture), [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) {#texture-phasertexturestexture-phasertexturescanvastexture}


**说明:**

游戏对象所用的质素 。


> 源码：[src/gameobjects/components/TextureCrop.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TextureCrop.js#L21)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### setCrop {#setCrop}

#### \<instance> setCrop([x], [y], [width], [height]) {#instance-setcropx-y-width-height}


**说明:**

将一个裁剪应用到基于纹理的游戏对象,例如Sprite或Image.

裁剪是一个矩形,它限制了渲染时可见的纹理帧的区域.

裁剪游戏对象不会改变其大小,尺寸,物理体或命中区域,它只是改变在渲染时显示的内容.

作物大小以及坐标不得超过纹理帧的大小。

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


**返回值:** [Phaser.GameObjects.Components.TextureCrop](/api/namespace/gameobjects-components-texturecrop) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/TextureCrop.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TextureCrop.js#L50)  
引入版本：3.11.0


---

### setFrame {#setFrame}

#### \<instance> setFrame(frame, [updateSize], [updateOrigin]) {#instance-setframeframe-updatesize-updateorigin}


**说明:**

设置此游戏对象将使用的框架 。

如果您通过字符串或索引,则框架必须属于当前这个游戏对象正在使用的纹理。

如果您通过一个框架实例, 此游戏对象正在使用的纹理也会被更新 。

呼叫 `setFrame` 会修改您的游戏对象的 `width` 和 `height` 属性 。

如果框架有一个自定义的枢轴点, 也可以改变 `origin`, 如Texture Packer 等包的导出点 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| frame | string \| number | [Phaser.Textures.Frame](/api/class/textures-frame) | 否 |  | 纹理内框架的名称或索引,或框架实例。 |
| updateSize | boolean | 是 | true | 此调用是否应该调整游戏对象的大小 ? |
| updateOrigin | boolean | 是 | true | 此调用是否应该调整游戏对象的起源 ? |


**返回值:** [Phaser.GameObjects.Components.TextureCrop](/api/namespace/gameobjects-components-texturecrop) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/TextureCrop.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TextureCrop.js#L130)  
引入版本：3.0.0


---

### setTexture {#setTexture}

#### \<instance> setTexture(key, [frame]) {#instance-settexturekey-frame}


**说明:**

设置此游戏对象将使用的纹理和框架。

纹理通过基于字符串的键来引用, 存储在纹理管理器中.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要使用的纹理键, 如存储在纹理管理器中 。 |
| frame | string \| number | 是 | 纹理内框的名称或索引. |


**返回值:** [Phaser.GameObjects.Components.TextureCrop](/api/namespace/gameobjects-components-texturecrop) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/TextureCrop.js#L110](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/TextureCrop.js#L110)  
引入版本：3.0.0


---

---
