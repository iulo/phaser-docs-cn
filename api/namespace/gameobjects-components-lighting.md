# Phaser.GameObjects.Components.Lighting {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-lighting)

Scope: 
static
> 源码：[src/gameobjects/components/Lighting.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Lighting.js#L7)  
引入版本：4.0.0

## 静态函数 {#static-functions}

### lighting {#lighting}

#### lighting: boolean {#lighting-boolean}


**说明:**

控制此游戏对象是否参与 WebGL 照明系统。 当 `true` 时, 对象会响应通过 Lights 插件添加的动态灯光, 使用普通的地图来计算每个像素的散射照明 。

此旗帜用于在渲染时选择相应的 WebGL 着色器 。

**Tags:**

 - webglOnly


> 源码：[src/gameobjects/components/Lighting.js#L24](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Lighting.js#L24)  
引入版本：4.0.0


---

### selfShadow {#selfShadow}

#### selfShadow: Object {#selfshadow-object}


**说明:**

配置对象控制此游戏对象的自我阴影。 自我阴影会让表面根据普通地图在自己身上投射接触阴影, 并给出深度的外观。 它只在 `lighting` 也启用时才活动 。

如果 `enabled`是 `null`,则取而代之的是游戏配置选项 `render.selfShadow`的值.

此对象用于在渲染时选择和配置相应的 WebGL 遮蔽器 。

**Tags:**

 - webglOnly


> 源码：[src/gameobjects/components/Lighting.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Lighting.js#L40)  
引入版本：4.0.0


---

## 静态函数 {#static-functions-1}

### setLighting {#setLighting}

#### \<instance> setLighting(enable) {#instance-setlightingenable}


**说明:**

启用或禁用基于 WebGL 的每像素的此游戏对象照明。 启用后, 该对象将通过灯光插件对场景添加的动态灯光做出响应, 使用普通的映射图进行照明计算。 禁用照明恢复标准的未读渲染路径 。

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| enable | boolean | 否 | `true`用来使用照明,或者`false`用来禁用它. |


**返回值:** [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Lighting.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Lighting.js#L62)  
引入版本：4.0.0


---

### setSelfShadow {#setSelfShadow}

#### \<instance> setSelfShadow([enabled], [penumbra], [diffuseFlatThreshold]) {#instance-setselfshadowenabled-penumbra-diffuseflatthreshold}


**说明:**

配置此游戏对象的自我阴影属性。 自阴影使用普通映射在表面本身投影, 给人深刻的印象和提升的细节。 它只在活动时使用 。 `lighting` 也在此游戏对象上启用。

属于`undefined`的参数保持不变,允许部分更新.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| enabled | boolean | 是 | `true` 以自影为音, `false` 无法操作 `null` 默认使用游戏 `config.render.selfShadow`,或 ,或 , `undefined` 来保持环境。 |
| penumbra | number | 是 | 阴影的笔形值。 下方更尖但更横。 默认值为 0. 5。 |
| diffuseFlatThreshold | number | 是 | 将将扩散光线视为平坦的纹理亮度阈值。 范围为 0– 1。 默认为 1/ 3 。 |


**返回值:** [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Lighting.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Lighting.js#L81)  
引入版本：4.0.0


---

---
