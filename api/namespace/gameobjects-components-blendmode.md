# Phaser.GameObjects.Components.BlendMode {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-blendmode)

Scope: 
static
> 源码：[src/gameobjects/components/BlendMode.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/BlendMode.js#L9)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### blendMode {#blendMode}

#### blendMode: [Phaser.BlendModes](/api/namespace/blendmodes), string, number {#blendmode-phaserblendmodes-string-number}


**说明:**

设置此游戏对象正在使用的混合模式。

这可以是凸轮,如`Phaser.BlendModes.SCREEN`,也可以是整数,如4(用于重叠)

WebGL只提供以下组合模式:

* NORMAL

* ADD

* MULTIPLY

* SCREEN

* ERASE

视浏览器支持情况,Canvas的可用性更高.

也可以在WebGL中创建自定义的混合模式.

混合模式在 Canvas 和 WebGL 下,以及浏览器到浏览器之间, 效果不同, 取决于支持。 混合模式在遇到新的混合模式时, 也会产生 WebGL 批量冲洗。 由于这些原因, 尝试谨慎构建您的色调以及混合模式的频率 。


> 源码：[src/gameobjects/components/BlendMode.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/BlendMode.js#L36)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### setBlendMode {#setBlendMode}

#### \<instance> setBlendMode(value) {#instance-setblendmodevalue}


**说明:**

设置此游戏对象正在使用的混合模式。

这可以是凸轮,如`Phaser.BlendModes.SCREEN`,也可以是整数,如4(用于重叠)

WebGL只提供以下组合模式:

* NORMAL

* ADD

* MULTIPLY

* SCREEN

* ERSE( 只在向帧缓冲器渲染时工作, 如 Render 纹理)

视浏览器支持情况,Canvas的可用性更高.

也可以在WebGL中创建自定义的混合模式.

混合模式在 Canvas 和 WebGL 下,以及浏览器到浏览器之间, 效果不同, 取决于支持。 混合模式在遇到新的混合模式时, 也会产生 WebGL 批量冲洗。 由于这些原因, 尝试谨慎构建您的色调以及混合模式的频率 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | string \| [Phaser.BlendModes](/api/namespace/blendmodes) | number | 否 | 混合模式值。 要么是字符串、 CONST 或数字 。 |


**返回值:** [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/BlendMode.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/BlendMode.js#L86)  
引入版本：3.0.0


---

---
