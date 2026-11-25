# Phaser.GameObjects.Components.Mask {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-mask)

Scope: 
static
> 源码：[src/gameobjects/components/Mask.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Mask.js#L10)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### mask {#mask}

#### mask: [Phaser.Display.Masks.GeometryMask](/api/class/display-masks-geometrymask) {#mask-phaserdisplaymasksgeometrymask}


**说明:**

渲染过程中此游戏对象使用的遮罩, 如果没有设置遮罩, 则使用 `null` 。


> 源码：[src/gameobjects/components/Mask.js#L26](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Mask.js#L26)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### clearMask {#clearMask}

#### \<instance> clearMask([destroyMask]) {#instance-clearmaskdestroymask}


**说明:**

清除游戏对象使用的掩码 。

这只在Canvas Renderer中有效. WebGL中,改用面具滤波器(见[Phaser.GameObjects.Components.FilterList#addMask](/api/class/gameobjects-components-filterlist#addMask)).

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| destroyMask | boolean | 是 | false | 清理前先销毁面具? |


**返回值:** [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Mask.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Mask.js#L70)  
引入版本：3.6.2


---

### createGeometryMask {#createGeometryMask}

#### \<instance> createGeometryMask([graphics]) {#instance-creategeometrymaskgraphics}


**说明:**

创建并返回几何面具。 此面具可用于任何游戏对象, 包括此对象 。

要创建此面具, 您需要通过一个图形游戏对象的引用 。

如果您不提供图形对象, 而这个 Game Object 是图形对象的实例, 那么它会用自己来创建遮罩 。

这意味着你可以使用这种方法从任意图形游戏对象中创建几何遮罩.

这只在Canvas Renderer中有效. WebGL中,改用面具滤波器(见[Phaser.GameObjects.Components.FilterList#addMask](/api/class/gameobjects-components-filterlist#addMask)).

**Tags:**

 - generic
 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| graphics | [Phaser.GameObjects.Graphics](/api/class/gameobjects-graphics) \| [Phaser.GameObjects.Shape](/api/class/gameobjects-shape) | 是 | 图形游戏对象,或任何形状游戏对象。其中的几何将被用作遮罩。 |


**返回值:** [Phaser.Display.Masks.GeometryMask](/api/class/display-masks-geometrymask) - 所创造的几何面具。


> 源码：[src/gameobjects/components/Mask.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Mask.js#L97)  
引入版本：3.6.2


---

### setMask {#setMask}

#### \<instance> setMask(mask) {#instance-setmaskmask}


**说明:**

设置此游戏对象将用来渲染的遮罩 。

面具必须是以前创建的, 而且必须是几何掩码。 这只在 Canvas 渲染器中有效。 在 WebGL 中, 改用一个 Mask 过滤器( 见 [Phaser.GameObjects.Components.FilterList#addMask](/api/class/gameobjects-components-filterlist#addMask)) 。

如果在这个游戏对象上已经设置了面具, 将会立即替换它 。

面具位于全球空间,与它们被应用的游戏对象无关。原因就是多个游戏对象可以都共享相同的面具。

遮罩对物理或输入检测没有影响。 它们是纯粹的渲染组件, 允许您限制在渲染传出时可见的东西 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mask | [Phaser.Display.Masks.GeometryMask](/api/class/display-masks-geometrymask) | 否 | 渲染时此游戏对象将使用的遮罩 。 |


**返回值:** [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Mask.js#L35](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Mask.js#L35)  
引入版本：3.6.2


---

---
