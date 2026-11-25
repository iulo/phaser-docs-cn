# Phaser.GameObjects.Components.AlphaSingle {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-alphasingle)

Scope: 
static
> 源码：[src/gameobjects/components/AlphaSingle.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/AlphaSingle.js#L12)  
引入版本：3.22.0

## 静态函数 {#static-functions}

### alpha {#alpha}

#### alpha: number {#alpha-number}


**说明:**

游戏对象的α值 。

这是一个全局值,它会影响整个游戏对象,而不只是它的一个区域。该值会被夹在范围 [0, 1] 上。设置 alpha 到 0 也可以清除渲染的旗,防止游戏对象被绘制到再次提升到 0 以上 。


> 源码：[src/gameobjects/components/AlphaSingle.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/AlphaSingle.js#L70)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### clearAlpha {#clearAlpha}

#### \<instance> clearAlpha() {#instance-clearalpha}


**说明:**

清除与此游戏对象相关的α值。

立即将α放回1(完全不透明).


**返回值:** [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/AlphaSingle.js#L35](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/AlphaSingle.js#L35)  
引入版本：3.0.0


---

### setAlpha {#setAlpha}

#### \<instance> setAlpha([value]) {#instance-setalphavalue}


**说明:**

设置此游戏对象的 Alpha 级别。 阿尔法控制游戏对象的不透明性。 Alpha 值作为浮点在 0 、 完全透明、 和 1 之间。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 1 | 在整个游戏对象中应用的α值. |


**返回值:** [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/AlphaSingle.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/AlphaSingle.js#L50)  
引入版本：3.0.0


---

---
