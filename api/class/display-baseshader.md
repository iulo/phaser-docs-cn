# BaseShader {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/display-baseshader)

一个BaseShader是一个小资源类,它包含GLSL代码用于遮蔽器.

它包含着色器的键,源代码,以及可选元数据. Phaser不强制执行特定的着色器类型:源代码可以是片段着色器,顶点着色器,甚至可能是GLSL不完整片段. 它作为原始源代码存储,可以按您的意愿被检索和编译. `Phaser.GameObjects.Shader`和`Phaser.Renderer.WebGL.RenderNodes.BaseFilterShader`都可以使用这些键.

基片包存储在缓存中,通过`this.cache.shaders`在一个场景中可用,并通过一个独特的基于键的字符串来引用。通过`this.cache.shaders.get(key)`来获取它们。

底片包由 GLSL 文件加载器在加载外部着色器资源时自动创建。它们也可以在运行时创建,允许您使用动态生成的阴影源代码 。

**构造函数**

`new BaseShader(key, glsl, [metadata])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 此阴影的键。 必须是在阴影缓存中独有的 。 |
| glsl | string | 否 | 遮荫器的GLSL源代码. |
| metadata | object | 是 | 此阴影码的额外元数据 。 |

---


**作用域**: static

> 源码：[src/display/shader/BaseShader.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/shader/BaseShader.js#L9)  
引入版本：4.0.0

## 公开成员 {#public-members}

### glsl {#glsl}

#### glsl: string {#glsl-string}


**说明:**

GLSL 源代码用于遮蔽器。 此代码的使用不是由 Phaser 指定。 您可以添加元数据来进一步描述其目的 。


> 源码：[src/display/shader/BaseShader.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/shader/BaseShader.js#L50)  
引入版本：4.0.0


---

### key {#key}

#### key: string {#key-string}


**说明:**

这个阴影码的键,在这个 Phaser 游戏实例的阴影缓存中独一无二.


> 源码：[src/display/shader/BaseShader.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/shader/BaseShader.js#L40)  
引入版本：3.17.0


---

### metadata {#metadata}

#### metadata: object {#metadata-object}


**说明:**

此着色器的额外元数据。 这不是 Phaser 使用的, 但可以用您的游戏代码或外部工具使用。 例如, 您可以添加描述着色器的目的、 作者、 版本等属性 。


> 源码：[src/display/shader/BaseShader.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/shader/BaseShader.js#L61)  
引入版本：4.0.0


---

---
