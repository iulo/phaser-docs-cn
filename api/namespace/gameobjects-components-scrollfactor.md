# Phaser.GameObjects.Components.ScrollFactor {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-scrollfactor)

Scope: 
static
> 源码：[src/gameobjects/components/ScrollFactor.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ScrollFactor.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### scrollFactorX {#scrollFactorX}

#### scrollFactorX: number {#scrollfactorx-number}


**说明:**

此游戏对象的横向滚动因子 。

滚动因子控制了相机移动对这个游戏对象的影响.

当相机滚动时, 将更改屏幕上显示此游戏对象的位置。 它不会改变游戏对象的实际位置值 。

1 值表示它会和相机同步移动。 0 值表示它不会移动, 即使相机移动。 其他值控制了相机移动到此 Game Object 的映射程度 。

请注意,在计算物理碰撞时,不考虑1以外的滚动因子值。天体总是根据它们的世界位置碰撞,但改变滚动因子是对纹理的渲染地的视觉调整,如果在您的代码中不计及的话,这种调整可以抵消物理体。


> 源码：[src/gameobjects/components/ScrollFactor.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ScrollFactor.js#L16)  
引入版本：3.0.0


---

### scrollFactorY {#scrollFactorY}

#### scrollFactorY: number {#scrollfactory-number}


**说明:**

此游戏对象的垂直滚动因子 。

滚动因子控制了相机移动对这个游戏对象的影响.

当相机滚动时, 将更改屏幕上显示此游戏对象的位置。 它不会改变游戏对象的实际位置值 。

1 值表示它会和相机同步移动。 0 值表示它不会移动, 即使相机移动。 其他值控制了相机移动到此 Game Object 的映射程度 。

请注意,在计算物理碰撞时,不考虑1以外的滚动因子值。天体总是根据它们的世界位置碰撞,但改变滚动因子是对纹理的渲染地的视觉调整,如果在您的代码中不计及的话,这种调整可以抵消物理体。


> 源码：[src/gameobjects/components/ScrollFactor.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ScrollFactor.js#L40)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### setScrollFactor {#setScrollFactor}

#### \<instance> setScrollFactor(x, [y]) {#instance-setscrollfactorx-y}


**说明:**

设置此游戏对象的横向和纵向滚动因子。 如果只提供 `x`值, 它将应用到两个轴上。 这是在一次调用中设置 `scrollFactorX`和 `scrollFactorY` 的方便方法 。

滚动因子控制了相机移动对这个游戏对象的影响.

当相机滚动时, 将更改屏幕上显示此游戏对象的位置。 它不会改变游戏对象的实际位置值 。

1 值表示它会和相机同步移动。 0 值表示它不会移动, 即使相机移动。 其他值控制了相机移动到此 Game Object 的映射程度 。

请注意,在计算物理碰撞时,不考虑1以外的滚动因子值。天体总是根据它们的世界位置碰撞,但改变滚动因子是对纹理的渲染地的视觉调整,如果在您的代码中不计及的话,这种调整可以抵消物理体。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 此游戏对象的横向滚动因子 。 |
| y | number | 是 | "x" | 此游戏对象的垂直滚动因子。 如果不设定, 则会使用 `x` 值 。 |


**返回值:** [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/ScrollFactor.js#L64](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ScrollFactor.js#L64)  
引入版本：3.0.0


---

---
