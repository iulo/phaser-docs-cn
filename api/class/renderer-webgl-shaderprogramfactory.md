# ShaderProgramFactory {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-shaderprogramfactory)

ShaderProgramFactory是一个用于为 WebGL渲染器创建和缓存 [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](/api/class/renderer-webgl-wrappers-webglprogramwrapper)对象的实用类,它从基部遮蔽器中组装编译的遮蔽程序,结合可选的添加和特征标记,然后将结果存储在独有的密钥下,这样就永远不能不止一次编译同一组合。当您需要获得一个在运行时间可能因渲染器能力或管道配置而变化的遮蔽程序时,使用该类.

**构造函数**

`new ShaderProgramFactory(renderer)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) | 否 | 拥有此 Shader Program Factory 的 WebGLRender 软件软件软件软件软件 。 |

---


**作用域**: static

> 源码：[src/renderer/webgl/ShaderProgramFactory.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ShaderProgramFactory.js#L16)  
引入版本：4.0.0

## 公开成员 {#public-members}

### programs {#programs}

#### programs: object {#programs-object}


**说明:**

由独特的密钥识别的阴影程序地图.

每个遮阳程序的关键由以下组件组成: 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光线 光光光 光光 光光光光 光光光 光光 光 光光光 光 光 光光 光光 光光光 光 光 光光 光 光 光光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光 光

- 底荫方案的关键.

- 每个着色器加的键,另外顺序.

- 每个启用的阴影特性的密钥, 按字母顺序排序 。


> 源码：[src/renderer/webgl/ShaderProgramFactory.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ShaderProgramFactory.js#L44)  
引入版本：4.0.0


---

### renderer {#renderer}

#### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](/api/class/renderer-webgl-webglrenderer) {#renderer-phaserrendererwebglwebglrenderer}


**说明:**

拥有此 Shader Program Factory 的 WebGLRender 软件软件软件软件软件 。


> 源码：[src/renderer/webgl/ShaderProgramFactory.js#L35](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ShaderProgramFactory.js#L35)  
引入版本：4.0.0


---

## 公开方法 {#public-methods}

### createShaderProgram {#createShaderProgram}

#### \<instance> createShaderProgram(name, base, [additions], [features]) {#instance-createshaderprogramname-base-additions-features}


**说明:**

基于给定的配置设置创建阴影程序。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 遮荫程序的独特密钥. |
| base | BaseShaderConfig | 否 | 底荫面配置. |
| additions | Array.\<[Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig)> | 是 | 一组着色器添加配置 。 |
| features | Array.\<string> | 是 | 一组启用的阴影特性密钥 。 |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](/api/class/renderer-webgl-wrappers-webglprogramwrapper) - 新编译和缓存的遮阳程序包.


> 源码：[src/renderer/webgl/ShaderProgramFactory.js#L143](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ShaderProgramFactory.js#L143)  
引入版本：4.0.0


---

### getKey {#getKey}

#### \<instance> getKey(base, [additions], [features]) {#instance-getkeybase-additions-features}


**说明:**

返回基于给定配置设置的阴影程序独有的密钥 。

关键由以下部分组成: 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键词 关键 关键词 关键 关键词 关键词 关键词 关键词 关键 关键词 关键 关键 关键 关键词 关键 关键 关键 关键 关键词 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键 关键

- 底荫方案的关键.

- 每个着色器加的键,另外顺序.

- 每个启用的阴影特性的密钥, 按字母顺序排序 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| base | BaseShaderConfig | 否 | 底荫面配置. |
| additions | Array.\<[Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig)> | 是 | 一组着色器添加配置 。 |
| features | Array.\<string> | 是 | 一组启用的阴影特性密钥 。 |


**返回值:** string - 此阴影配置的独有缓存密钥 。


> 源码：[src/renderer/webgl/ShaderProgramFactory.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ShaderProgramFactory.js#L101)  
引入版本：4.0.0


---

### getShaderProgram {#getShaderProgram}

#### \<instance> getShaderProgram(base, [additions], [features]) {#instance-getshaderprogrambase-additions-features}


**说明:**

返回已编译的用于指定配置的阴影程序。 如果匹配所衍生密钥的程序已经存在于缓存中, 则立即返回; 否则将编译一个新的程序, 存储在缓存中, 并返回 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| base | BaseShaderConfig | 否 | 底荫面配置. |
| additions | Array.\<[Phaser.Types.Renderer.WebGL.ShaderAdditionConfig](/api/typedef/types-renderer-webgl#shaderadditionconfig)> | 是 | 一组着色器添加配置 。 |
| features | Array.\<string> | 是 | 一组启用的阴影特性密钥 。 |


**返回值:** [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](/api/class/renderer-webgl-wrappers-webglprogramwrapper) - 编译的遮阳程序包装器 。


> 源码：[src/renderer/webgl/ShaderProgramFactory.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ShaderProgramFactory.js#L74)  
引入版本：4.0.0


---

### has {#has}

#### \<instance> has(key) {#instance-haskey}


**说明:**

检查内部缓存中是否已经存在带有给定密钥的编译阴影程序 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 遮荫程序的独特密钥. |


**返回值:** boolean - 如果缓存中存在带有此密钥的遮蔽程序,则`true`,否则则`false`.


> 源码：[src/renderer/webgl/ShaderProgramFactory.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/ShaderProgramFactory.js#L60)  
引入版本：4.0.0


---

---
