# Phaser.GameObjects.Components.RenderNodes {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-rendernodes)

Scope: 
static
> 源码：[src/gameobjects/components/RenderNodes.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/RenderNodes.js#L9)  
引入版本：4.0.0

## 静态函数 {#static-functions}

### customRenderNodes {#customRenderNodes}

#### customRenderNodes: object {#customrendernodes-object}


**说明:**

自定义的 WebGL 渲染此游戏对象的节点。 RenderNodes 负责管理此游戏对象的渲染过程。 默认的一组 RenderNodes 在引擎中编码, 但渲染器会先检查此对象, 以查看是否设置了自定义节点 。

**Tags:**

 - webglOnly


> 源码：[src/gameobjects/components/RenderNodes.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/RenderNodes.js#L17)  
引入版本：4.0.0


---

### defaultRenderNodes {#defaultRenderNodes}

#### defaultRenderNodes: object {#defaultrendernodes-object}


**说明:**

此游戏对象的默认 RenderNodes。 RenderNodes 负责管理此游戏对象的渲染过程。 如果没有设置自定义的, 则使用这些节点 。

伦德节点由他们作用的独特密钥识别.

共同的角色键包括:

- 'Submiter':负责运行每个元素的其他节点角色.

- “ Transfer”:负责为某一元素提供顶点坐标。

- “ 文本器” : 负责处理元素的纹理。

**Tags:**

 - webglOnly


> 源码：[src/gameobjects/components/RenderNodes.js#L30](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/RenderNodes.js#L30)  
引入版本：4.0.0


---

### renderNodeData {#renderNodeData}

#### renderNodeData: object {#rendernodedata-object}


**说明:**

存储此游戏对象使用的渲染节点特定数据, 由渲染节点读取的对象 。

伦德节点以自己的名字而不是角色存储数据.

**Tags:**

 - webglOnly


> 源码：[src/gameobjects/components/RenderNodes.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/RenderNodes.js#L50)  
引入版本：4.0.0


---

## 静态函数 {#static-functions-1}

### initRenderNodes {#initRenderNodes}

#### \<instance> initRenderNodes(defaultNodes) {#instance-initrendernodesdefaultnodes}


**说明:**

初始化此游戏对象的渲染节点。

当游戏对象被添加到场景时, 这种方法被称为“ 游戏对象”。 它负责设置此游戏对象将使用的默认渲染节点 。

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| defaultNodes | Map.\<string, string> | 否 | 默认会使此游戏对象设置节点 。 |


> 源码：[src/gameobjects/components/RenderNodes.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/RenderNodes.js#L62)  
引入版本：4.0.0


---

### setRenderNodeData {#setRenderNodeData}

#### \<instance> setRenderNodeData(renderNode, key, value) {#instance-setrendernodedatarendernode-key-value}


**说明:**

设置或删除数据对象中的特定渲染节点在`renderNodeData`中的属性。

如果 `key` 未设置,则创建。如果设置了,则更新。

如果`value`是未定义的,且`key`存在,则将密钥移除.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderNode | string \| [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode) | 否 | 用于设定数据的渲染节点。 如果字符串, 应该是渲染节点的名称 。 |
| key | string | 否 | 要设置的属性的密钥 。 |
| value | * | 否 | 设置属性的值 。 |


**返回值:** [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/RenderNodes.js#L167](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/RenderNodes.js#L167)  
引入版本：4.0.0


---

### setRenderNodeRole {#setRenderNodeRole}

#### \<instance> setRenderNodeRole(key, renderNode, [renderNodeData], [copyData]) {#instance-setrendernoderolekey-rendernode-rendernodedata-copydata}


**说明:**

为给定角色设置“RenderNode”。

如果指定, 还要设置相关的渲染节点数据对象 。

如果节点不能设置,则不做修改.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 设置渲染节点的角色的关键 。 |
| renderNode | string \| [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode) | null | 否 |  | 在此游戏对象上设置的渲染节点。 要么是一个字符串, 要么是一个RenderNode实例。 如果 `null` , 渲染节点及其数据将被移除 。 |
| renderNodeData | object | 是 |  | 存储此游戏对象使用的渲染节点特定数据, 由渲染节点读取的对象 。 |
| copyData | boolean | 是 | false | 数据是否应该从 `renderNodeData` 对象复制? |


**返回值:** [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/RenderNodes.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/RenderNodes.js#L101)  
引入版本：4.0.0


---

---
