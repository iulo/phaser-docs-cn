# ProgramManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-programmanager)

程序管理器(Programmanager)是用于管理即时遮阳程序以及VAO等相关数据的套件的通用类,它维持一个共享的制服池,因此如果使用不同的遮阳程序,制服可以应用于新程序.

**构造函数**

`new ProgramManager(renderer, attributeBufferLayouts, [indexBuffer])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 当前的 WebGLRender 实例 。 |
| attributeBufferLayouts | Array.\<[Phaser.Types.Renderer.WebGL.WebGLAttributeBufferLayout](/api/typedef/types-renderer-webgl#webglattributebufferlayout)> | 否 | 程序中使用的属性缓冲布局. |
| indexBuffer | [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) | 是 | 程序中使用的索引缓冲器,如果有的话. |

---


**作用域**: static

> 源码：[src/renderer/webgl/ProgramManager.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L10)  
引入版本：4.0.0

## 公开成员 {#public-members}

### attributeBufferLayouts {#attributeBufferLayouts}

#### attributeBufferLayouts: Array.\<[Phaser.Types.Renderer.WebGL.WebGLAttributeBufferLayout](/api/typedef/types-renderer-webgl#webglattributebufferlayout)> {#attributebufferlayouts-arrayphasertypesrendererwebglwebglattributebufferlayout}


**说明:**

程序中使用的属性缓冲布局。这些布局用于创建 VAO 。


> 源码：[src/renderer/webgl/ProgramManager.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L48)  
引入版本：4.0.0


---

### currentConfig {#currentConfig}

#### currentConfig: object {#currentconfig-object}


**说明:**

正在组装的配置对象 。


> 源码：[src/renderer/webgl/ProgramManager.js#L67](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L67)  
引入版本：4.0.0


---

### currentProgramKey {#currentProgramKey}

#### currentProgramKey: string {#currentprogramkey-string}


**说明:**

当前活动阴影程序的关键 。


> 源码：[src/renderer/webgl/ProgramManager.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L58)  
引入版本：4.0.0


---

### indexBuffer {#indexBuffer}

#### indexBuffer: [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](/api/class/renderer-webgl-wrappers-webglbufferwrapper) {#indexbuffer-phaserrendererwebglwrapperswebglbufferwrapper}


**说明:**

如果有的话, 程序中使用的索引缓冲器。 用于创建 VAO 。


> 源码：[src/renderer/webgl/ProgramManager.js#L38](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L38)  
引入版本：4.0.0


---

### programs {#programs}

#### programs: object {#programs-object}


**说明:**

以独特的密钥识别的荫色程序和相关数据套件的映射.

每个键对应于一个形状如下的对象:

- `program`(WebGL ProgramWrapper) - 编译的遮阳程序.

- `vao`(WebGLVAOWrapper) - 与程序相关的VAO.

- `config`(对象) - 用于创建程序的配置对象.


> 源码：[src/renderer/webgl/ProgramManager.js#L83](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L83)  
引入版本：4.0.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrendererwebglwebglrenderer}


**说明:**

当前的 WebGLRender 实例 。


> 源码：[src/renderer/webgl/ProgramManager.js#L29](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L29)  
引入版本：4.0.0


---

### uniforms {#uniforms}

#### uniforms: object {#uniforms-object}


**说明:**

以阴影统一名称识别的统一值地图。 这使得制服可以保存在阴影程序之间 。


> 源码：[src/renderer/webgl/ProgramManager.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L99)  
引入版本：4.0.0


---

## 公开方法 {#public-methods}

### addAddition {#addAddition}

#### \<instance> addAddition(addition, [index]) {#instance-addadditionaddition-index}


**说明:**

在当前配置中添加一个着色器。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| addition | [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) | 否 | 阴者加之以加之. |
| index | number | 是 | 插入添加的索引。如果不指定,则在结尾处添加。 |


> 源码：[src/renderer/webgl/ProgramManager.js#L253](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L253)  
引入版本：4.0.0


---

### addFeature {#addFeature}

#### \<instance> addFeature(feature) {#instance-addfeaturefeature}


**说明:**

在当前配置中添加一个特性 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| feature | string | 否 | 须加之特征. |


> 源码：[src/renderer/webgl/ProgramManager.js#L368](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L368)  
引入版本：4.0.0


---

### applyUniforms {#applyUniforms}

#### \<instance> applyUniforms(program) {#instance-applyuniformsprogram}


**说明:**

将所有存储的统一值应用到给定的阴影程序。 用于在阴影程序之间切换时恢复统一状态, 确保新程序接收到与上一个相同的统一值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| program | [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](/api/class/renderer-webgl-wrappers-webglprogramwrapper) | 否 | 将制服应用到遮阳器程序. |


> 源码：[src/renderer/webgl/ProgramManager.js#L216](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L216)  
引入版本：4.0.0


---

### clearFeatures {#clearFeatures}

#### \<instance> clearFeatures() {#instance-clearfeatures}


**说明:**

清除当前配置中的所有特性 。


> 源码：[src/renderer/webgl/ProgramManager.js#L398](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L398)  
引入版本：4.0.0


---

### clearUniforms {#clearUniforms}

#### \<instance> clearUniforms() {#instance-clearuniforms}


**说明:**

脱掉所有制服


> 源码：[src/renderer/webgl/ProgramManager.js#L205](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L205)  
引入版本：4.0.0


---

### getAddition {#getAddition}

#### \<instance> getAddition(name) {#instance-getadditionname}


**说明:**

返回添加名称。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 寻之名曰. |


**返回值:** [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) - 添加,或者如果找不到的话,`null`.


> 源码：[src/renderer/webgl/ProgramManager.js#L273](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L273)  
引入版本：4.0.0


---

### getAdditionIndex {#getAdditionIndex}

#### \<instance> getAdditionIndex(name) {#instance-getadditionindexname}


**说明:**

返回带有给定名称的阴影添加索引。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 寻之名曰. |


**返回值:** number - 添加的索引,或者如果找不到的话, 编号为 `-1` 。


> 源码：[src/renderer/webgl/ProgramManager.js#L316](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L316)  
引入版本：4.0.0


---

### getAdditionsByTag {#getAdditionsByTag}

#### \<instance> getAdditionsByTag(tag) {#instance-getadditionsbytagtag}


**说明:**

返回当前配置中带有特定标签的阴影添加列表。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tag | string | 否 | 过滤器的标签 。 |


**返回值:** Array.\<[Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig)> - 带有标签的阴影加法.


> 源码：[src/renderer/webgl/ProgramManager.js#L295](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L295)  
引入版本：4.0.0


---

### getCurrentProgramSuite {#getCurrentProgramSuite}

#### \<instance> getCurrentProgramSuite() {#instance-getcurrentprogramsuite}


**说明:**

返回基于当前配置的程序套件。 如果程序不存在, 则创建该套件 。

套房包含以下属性: 套房: 套房: 套房: 套房: 套房: 套房: 套房: 套房: 套房: 套房: 套房: 套房: 套房: 套房: 套房: 套房: 套房:

- `program`(WebGL ProgramWrapper) - 编译的遮阳程序.

- `vao`(WebGLVAOWrapper) - 与程序相关的VAO.

- `config`(对象) - 用于创建程序的配置对象.

如果启用并行的阴影编译, 程序可能不会立即可用。 在这种情况下, `null` 会被返回 。


**返回值:** Object - 程序套件,或者程序不可用时的`null`.


> 源码：[src/renderer/webgl/ProgramManager.js#L110](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L110)  
引入版本：4.0.0


---

### removeAddition {#removeAddition}

#### \<instance> removeAddition(name) {#instance-removeadditionname}


**说明:**

从当前配置中删除阴影添加。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 遮盖加法名以除. |


> 源码：[src/renderer/webgl/ProgramManager.js#L332](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L332)  
引入版本：4.0.0


---

### removeFeature {#removeFeature}

#### \<instance> removeFeature(feature) {#instance-removefeaturefeature}


**说明:**

从当前配置中删除一个特性 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| feature | string | 否 | 切除的特性 。 |


> 源码：[src/renderer/webgl/ProgramManager.js#L383](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L383)  
引入版本：4.0.0


---

### removeUniform {#removeUniform}

#### \<instance> removeUniform(name) {#instance-removeuniformname}


**说明:**

删除一个统一的值。 虽然未使用的制服没有有害,但处理起来确实需要时间,而且可能是一个混乱的根源。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 服之名曰  . |


> 源码：[src/renderer/webgl/ProgramManager.js#L192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L192)  
引入版本：4.0.0


---

### replaceAddition {#replaceAddition}

#### \<instance> replaceAddition(name, addition) {#instance-replaceadditionname-addition}


**说明:**

替换当前配置中的阴影添加。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 遮荫加法名以补之. |
| addition | [Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig) | 否 | 新荫增. |


> 源码：[src/renderer/webgl/ProgramManager.js#L347](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L347)  
引入版本：4.0.0


---

### resetCurrentConfig {#resetCurrentConfig}

#### \<instance> resetCurrentConfig() {#instance-resetcurrentconfig}


**说明:**

将当前配置对象重新设置为默认的空状态,清除底顶点和片段阴影,所有阴影添加,以及所有特性.


> 源码：[src/renderer/webgl/ProgramManager.js#L162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L162)  
引入版本：4.0.0


---

### setBaseShader {#setBaseShader}

#### \<instance> setBaseShader(name, vertexShader, fragmentShader) {#instance-setbaseshadername-vertexshader-fragmentshader}


**说明:**

为当前配置设置底部阴影。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 荫泽程序的名称. |
| vertexShader | string | 否 | 顶点阴影源代码. |
| fragmentShader | string | 否 | 碎片遮蔽源代码. |


> 源码：[src/renderer/webgl/ProgramManager.js#L236](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L236)  
引入版本：4.0.0


---

### setUniform {#setUniform}

#### \<instance> setUniform(name, value) {#instance-setuniformname-value}


**说明:**

设置一个统一值, 可供此管理器中所有阴影程序使用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 服之名曰  . |
| value | any | 否 | 制服的价值. |


> 源码：[src/renderer/webgl/ProgramManager.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ProgramManager.js#L178)  
引入版本：4.0.0


---

---
