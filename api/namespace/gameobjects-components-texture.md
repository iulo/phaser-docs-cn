# Phaser.GameObjects.Components.Texture {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-texture)

Scope: 
static
> 源码：[src/gameobjects/components/Texture.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Texture.js#L12)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### frame {#frame}

#### frame: [Phaser.Textures.Frame](/api/class/textures-frame) {#frame-phasertexturesframe}


**说明:**

此游戏对象正在使用质地框架来渲染 。


> 源码：[src/gameobjects/components/Texture.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Texture.js#L36)  
引入版本：3.0.0


---

### texture {#texture}

#### texture: [Phaser.Textures.Texture](/api/class/textures-texture), [Phaser.Textures.CanvasTexture](/api/class/textures-canvastexture) {#texture-phasertexturestexture-phasertexturescanvastexture}


**说明:**

游戏对象所用的质素 。


> 源码：[src/gameobjects/components/Texture.js#L27](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Texture.js#L27)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

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


**返回值:** [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Texture.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Texture.js#L81)  
引入版本：3.0.0


---

### setTexture {#setTexture}

#### \<instance> setTexture(key, [frame], [updateSize], [updateOrigin]) {#instance-settexturekey-frame-updatesize-updateorigin}


**说明:**

设置此游戏对象将使用的纹理和框架。

纹理通过基于字符串的键来引用, 存储在纹理管理器中.

调用此方法将修改您的游戏对象的 `width` 和 `height` 属性 。

如果框架有一个自定义的枢轴点, 也可以改变 `origin`, 如Texture Packer 等包的导出点 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 |  | 要使用的纹理键, 如存储在纹理管理器中, 或纹理实例 。 |
| frame | string \| number | 是 |  | 纹理内框的名称或索引. |
| updateSize | boolean | 是 | true | 此调用是否应该调整游戏对象的大小 ? |
| updateOrigin | boolean | 是 | true | 此调用是否应该改变游戏对象的起源 ? |


**返回值:** [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Texture.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Texture.js#L55)  
引入版本：3.0.0


---

---
