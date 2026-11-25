# Phaser.GameObjects.Components.Alpha {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-alpha)

Scope: 
static
> 源码：[src/gameobjects/components/Alpha.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Alpha.js#L12)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### alpha {#alpha}

#### alpha: number {#alpha-number}


**说明:**

游戏对象的α值,介于 0(完全透明)到 1(完全不透明)之间.

这是一个影响整个游戏对象的全局值。 设置它也会将所有四个角α值( `alphaTopLeft`, `alphaTopRight`, `alphaBottomLeft`, `alphaBottomRight`) 更新到相同的值。 输入被夹在范围 [0, 1] 上 。


> 源码：[src/gameobjects/components/Alpha.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Alpha.js#L136)  
引入版本：3.0.0


---

### alphaBottomLeft {#alphaBottomLeft}

#### alphaBottomLeft: number {#alphabottomleft-number}


**说明:**

以游戏对象左下角开始的α值。 此值从游戏对象的角插入到其中心 。

**Tags:**

 - webglOnly


> 源码：[src/gameobjects/components/Alpha.js#L236](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Alpha.js#L236)  
引入版本：3.0.0


---

### alphaBottomRight {#alphaBottomRight}

#### alphaBottomRight: number {#alphabottomright-number}


**说明:**

从游戏对象右下方开始的α值。此值从游戏对象的角到中心间插.

**Tags:**

 - webglOnly


> 源码：[src/gameobjects/components/Alpha.js#L266](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Alpha.js#L266)  
引入版本：3.0.0


---

### alphaTopLeft {#alphaTopLeft}

#### alphaTopLeft: number {#alphatopleft-number}


**说明:**

从游戏对象左上方开始的α值。此值从游戏对象的角落插到游戏对象的中心。

**Tags:**

 - webglOnly


> 源码：[src/gameobjects/components/Alpha.js#L176](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Alpha.js#L176)  
引入版本：3.0.0


---

### alphaTopRight {#alphaTopRight}

#### alphaTopRight: number {#alphatopright-number}


**说明:**

从游戏对象的右上角开始的α值。这个值从游戏对象的角到中心被插到中间。

**Tags:**

 - webglOnly


> 源码：[src/gameobjects/components/Alpha.js#L206](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Alpha.js#L206)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### clearAlpha {#clearAlpha}

#### \<instance> clearAlpha() {#instance-clearalpha}


**说明:**

清除所有与此游戏对象相关的α值。

立即将α级设回1级(完全不透明).


**返回值:** [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Alpha.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Alpha.js#L84)  
引入版本：3.0.0


---

### setAlpha {#setAlpha}

#### \<instance> setAlpha([topLeft], [topRight], [bottomLeft], [bottomRight]) {#instance-setalphatopleft-topright-bottomleft-bottomright}


**说明:**

设置此游戏对象的 Alpha 级别。 阿尔法控制游戏对象的不透明性。 Alpha 值作为浮点在 0 、 完全透明、 和 1 之间。

如果游戏运行在 WebGL 下, 您可以选择指定四个不同的字母值, 每个值对应游戏对象的四个角。 在 Canvas 下只使用给出的 `topLeft` 值 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| topLeft | number | 是 | 1 | 用于游戏对象左上角的α值。 如果这是唯一给出的值, 则应用在整个游戏对象中 。 |
| topRight | number | 是 |  | 游戏对象右上角使用的α值。 WebGL 仅限 。 |
| bottomLeft | number | 是 |  | 游戏对象左下角使用的α值。 WebGL 仅限 。 |
| bottomRight | number | 是 |  | 游戏对象右下角使用的α值。 只使用 WebGL 。 |


**返回值:** [Phaser.GameObjects.Components.Alpha](/api/namespace/gameobjects-components-alpha) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Alpha.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Alpha.js#L99)  
引入版本：3.0.0


---

---
