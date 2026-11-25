# Phaser.Renderer.WebGL.Utils {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/renderer-webgl-utils)

Scope: 
static
> 源码：[src/renderer/webgl/Utils.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/Utils.js#L11)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### checkShaderMax {#checkShaderMax}

#### \<static> checkShaderMax(gl, maxTextures) {#static-checkshadermaxgl-maxtextures}


**说明:**

选中可查看 GPU 在片段阴影中支持的纹理单元 , 以及是否允许游戏配置中指定的值 。

由于Android设备上的性能原因,这个值硬解为16.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gl | WebGLRenderingContext | 否 | WebGLContext用来创建阴间. |
| maxTextures | number | 否 | 游戏配置 maxTextures值. |


**返回值:** number - 此浏览器和 GPU 支持的纹理单元的数量 。


> 源码：[src/renderer/webgl/Utils.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/Utils.js#L101)  
引入版本：3.50.0


---

### getFloatsFromUintRGB {#getFloatsFromUintRGB}

#### \<static> getFloatsFromUintRGB(rgb) {#static-getfloatsfromuintrgbrgb}


**说明:**

将一个 Uint24 RGB 拆卸成数值在 0.0 到 1.0 之间的浮动阵列

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rgb | number | 否 | RGB 装入 Uint24 时 |


**返回值:** array - 以浮点表示每个组件的浮点阵


> 源码：[src/renderer/webgl/Utils.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/Utils.js#L82)  
引入版本：3.0.0


---

### getTintAppendFloatAlpha {#getTintAppendFloatAlpha}

#### \<static> getTintAppendFloatAlpha(rgb, a) {#static-gettintappendfloatalphargb-a}


**说明:**

包装一个代表 RGB 组件的 Uint24, 并装有代表α组件的 Float32, 范围在 0.0 和 1.0 之间, 并返回一个 Uint32

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rgb | number | 否 | 代表 RGB 组件的 Uint24 |
| a | number | 否 | 代表阿尔法组件的浮点32 |


**返回值:** number - 包装为 Uint32 的 RGBA


> 源码：[src/renderer/webgl/Utils.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/Utils.js#L40)  
引入版本：3.0.0


---

### getTintAppendFloatAlphaAndSwap {#getTintAppendFloatAlphaAndSwap}

#### \<static> getTintAppendFloatAlphaAndSwap(rgb, a) {#static-gettintappendfloatalphaandswaprgb-a}


**说明:**

包装一个代表 RGB 组件的 Uint24, 并装有代表α组件的 Float32, 范围在 0.0 和 1.0 之间, 并返回一个与红和蓝通道交换的旋绕的 Uint32( RGB 成为 BGR)

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rgb | number | 否 | 代表 RGB 组件的 Uint24 |
| a | number | 否 | 代表阿尔法组件的浮点32 |


**返回值:** number - 包装为 Uint32 的 RGBA


> 源码：[src/renderer/webgl/Utils.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/Utils.js#L59)  
引入版本：3.0.0


---

### getTintFromFloats {#getTintFromFloats}

#### \<static> getTintFromFloats(r, g, b, a) {#static-gettintfromfloatsr-g-b-a}


**说明:**

将 0.0 到 1.0 之间的四个浮点装入一个 Uint32

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| r | number | 否 | 红色组件,介于 0.0 到 1.0 之间 |
| g | number | 否 | 绿色成分,介于 0.0 到 1.0 之间 |
| b | number | 否 | 蓝色成分,介于 0.0 到 1.0 之间 |
| a | number | 否 | 阿尔法组件,范围为 0.0 到 1.0 |


**返回值:** number - 装入的 RGBA 值为 Uint32 。


> 源码：[src/renderer/webgl/Utils.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/Utils.js#L17)  
引入版本：3.0.0


---

### updateLightingUniforms {#updateLightingUniforms}

#### \<static> updateLightingUniforms(enable, drawingContext, programManager, textureUnit, vec, [selfShadow], [selfShadowPenumbra], [selfShadowThreshold]) {#static-updatelightinguniformsenable-drawingcontext-programmanager-textureunit-vec-selfshadow-selfshadowpenumbra-selfshadowthreshold}


**说明:**

设置或清除给定的荫影程序管理器上所有与照明相关的制服.

`enable`是`true`时,此函数会查询Scene的灯光管理器对相机可见的所有活动灯光进行查询,并将它们的位置,颜色,强度,以及光度作为统一的阵列上传到遮荫层。它也会上传环境光色,相机变换,以及普通的地图纹理单元。通过上传笔光和散射阈值制服,可以选择地实现自我遮蔽。

当 `enable`是 `false`时,所有先前设置的照明制服都会从程序管理器中移除. 如果Scene没有活动光管理器,则函数会提前返回而无需做任何更改.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| enable | boolean | 否 | 是否启用照明 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 绘图康特实例。 |
| programManager | [Phaser.Renderer.WebGL.ProgramManager](/api/class/renderer-webgl-programmanager) | 否 | 阴影程序管理器实例 。 |
| textureUnit | number | 否 | 用于普通地图的纹理单元。 |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 一种矢量2 实例。 |
| selfShadow | boolean | 是 | 是否启用自我阴影 。 |
| selfShadowPenumbra | number | 是 | 笔形的自影价值. |
| selfShadowThreshold | number | 是 | 自我影视的阈值 。 |


> 源码：[src/renderer/webgl/Utils.js#L133](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/Utils.js#L133)  
引入版本：4.0.0


---

---
