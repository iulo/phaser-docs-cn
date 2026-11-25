# WebGLTextureUnitsWrapper {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-wrappers-webgltextureunitswrapper)

用于 WebGLRendering Context 纹理单元的包装器。 它跟踪哪些纹理被绑定到哪个单元, 并提供约束的公用事业 。

**构造函数**

`new WebGLTextureUnitsWrapper(renderer)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有这个包装的 WebGLRender 实例 。 |

---


**作用域**: static

> 源码：[src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L9)  
引入版本：4.0.0

## 公开成员 {#public-members}

### renderer {#renderer}

#### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrendererwebglwebglrenderer}


**说明:**

拥有这个包装的 WebGLRender 实例 。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L27](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L27)  
引入版本：4.0.0


---

### unitIndices {#unitIndices}

#### unitIndices: Array.\<number> {#unitindices-arraynumber}


**说明:**

可用纹理单位索引列表,用于设置制服.


> 源码：[src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L45)  
引入版本：4.0.0


---

### units {#units}

#### units: Array.\<([Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | null)> {#units-arrayphaserrendererwebglwrapperswebgltexturewrapper-null}


**说明:**

网络GLRendering Context 可用的纹理单位列表 。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L36)  
引入版本：4.0.0


---

## 公开方法 {#public-methods}

### bind {#bind}

#### \<instance> bind(texture, unit, [force], [forceActive]) {#instance-bindtexture-unit-force-forceactive}


**说明:**

将纹理绑入纹理单元。

这将将活动纹理单元改变为给定单元,除非`forceActive`是虚假的.

这应该是将纹理绑在一个单位上的唯一方法.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) \| null | 否 |  | 绑定的纹理,或解封单位的纹理无效. |
| unit | number | 否 |  | 纹理单位将纹理绑定在. |
| force | boolean | 是 | false | 如果是真的,它会约束纹理,即使它已经约束了。 |
| forceActive | boolean | 是 | true | 如果为真,即使已经激活,它也会将活动纹理单位更改为给定单位。否则,它只会在尚未激活时改变活动纹理单位。 |


> 源码：[src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L97)  
引入版本：4.0.0


---

### bindUnits {#bindUnits}

#### \<instance> bindUnits(textures, [force]) {#instance-bindunitstextures-force}


**说明:**

将特定的纹理单位设置为特定的纹理.

主动纹理单位可更改以适应装订.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| textures | Array.\<([Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) \| null | undefined)> | 否 |  | 绑定的纹理。 无效值将不绑定。 未定义的值将被跳过 。 |
| force | boolean | 是 | false | 如果是真的,它会约束所有纹理,即使它们已经捆绑了. |


> 源码：[src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L136)  
引入版本：4.0.0


---

### init {#init}

#### \<instance> init() {#instance-init}


**说明:**

初始化纹理单元到 `null`。 运行后, 活动纹理单元为 0 。

此填充每个纹理单元带有1x1纹理。 这可以停止 MacOS 上的 WebGL 错误。 这些纹理不是包, 也不是要使用的, 因此纹理单元被记录为无效 。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L58)  
引入版本：4.0.0


---

### unbindAllUnits {#unbindAllUnits}

#### \<instance> unbindAllUnits() {#instance-unbindallunits}


**说明:**

取消所有纹理单元的所有纹理。 这将将活动纹理单元更改为 0 。


> 源码：[src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L180](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L180)  
引入版本：4.0.0


---

### unbindTexture {#unbindTexture}

#### \<instance> unbindTexture(texture) {#instance-unbindtexturetexture}


**说明:**

取消当前所有纹理单位的特定纹理。

在所有纹理单元上标注, 并用 `null` 替换任何匹配给定纹理的绑定。 通常在纹理即将被销毁时使用此名称, 以确保没有单位持有 stale 引用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](/api/class/renderer-webgl-wrappers-webgltexturewrapper) | 否 | 纹理从所有单位拆开。 |


> 源码：[src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/wrappers/WebGLTextureUnitsWrapper.js#L158)  
引入版本：4.0.0


---

---
