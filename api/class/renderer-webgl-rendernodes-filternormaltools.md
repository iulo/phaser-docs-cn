# FilterNormalTools {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-filternormaltools)

这个 RenderNode 使正常 Tools 过滤器效果, 处理正常的地图纹理, 用于照明计算。 它使用视图矩阵来改变正常的矢量, 使其相对于相机正确定向, 从而能够在正常的游戏对象上准确定向照明 。

通过控制器可以实现两个可选特性: 面对电,使点产品提高给定的导电器使照明掉落变尖或变软; 比例输出,将正常的贡献与方向向量和半径混合在一起,产生下游照明通道使用的比例值.

这个节点由[Phaser.Filters.NormalTools](/api/class/filters-normaltools)内部使用,不需要直接即时使用. 见[Phaser.Filters.NormalTools](/api/class/filters-normaltools).

**构造函数**

`new FilterNormalTools(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader)  



> 源码：[src/renderer/webgl/renderNodes/filters/FilterNormalTools.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterNormalTools.js#L12)  
引入版本：4.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader):**


 - [run](/api/class/renderer-webgl-rendernodes-basefiltershader#run)
 - [setupTextures](/api/class/renderer-webgl-rendernodes-basefiltershader#setupTextures)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### setupUniforms {#setupUniforms}

#### \<instance> setupUniforms(controller, drawingContext) {#instance-setupuniformscontroller-drawingcontext}


**说明:**

设定 WebGL 基于当前控制器设置的普通工具遮蔽器的统一值。 总是将视图矩阵上传为 `uViewMatrix`如果控制器是 `facingPower` 与默认值不同 `1`,则 `uFacingPower` 制服也上传。如果 `outputRatio` 启用在控制器上, `uRatioVector` (a) 3个组成部分方向向量)和 `uRatioRadius` 制服也上传了

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.NormalTools](/api/class/filters-normaltools) | 否 | 提供统一值的过滤控制器 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#setupUniforms


> 源码：[src/renderer/webgl/renderNodes/filters/FilterNormalTools.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterNormalTools.js#L86)  
引入版本：4.0.0


---

### updateShaderConfig {#updateShaderConfig}

#### \<instance> updateShaderConfig(controller, drawingContext) {#instance-updateshaderconfigcontroller-drawingcontext}


**说明:**

基于当前控制器设置更新着色器程序配置. 重新设置在基部`VIEW_MATRIX`定义中添加的片段头,然后有条件地附加`FACING_POWER`和`OUTPUT_RATIO`定义的——并相应调整添加名称,这样就可以编译正确的着色器变体,并缓存用于特性的主动组合.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| controller | [Phaser.Filters.NormalTools](/api/class/filters-normaltools) | 否 | 提供当前配置的过滤控制器 。 |
| drawingContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader#updateShaderConfig


> 源码：[src/renderer/webgl/renderNodes/filters/FilterNormalTools.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/filters/FilterNormalTools.js#L54)  
引入版本：4.0.0


---

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader](/api/class/renderer-webgl-rendernodes-basefiltershader):**


 - [indexBuffer](/api/class/renderer-webgl-rendernodes-basefiltershader#indexBuffer)
 - [programManager](/api/class/renderer-webgl-rendernodes-basefiltershader#programManager)
 - [vertexBufferLayout](/api/class/renderer-webgl-rendernodes-basefiltershader#vertexBufferLayout)





**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

---
