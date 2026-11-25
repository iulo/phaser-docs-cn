# Phaser.GameObjects.Components.Origin {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-origin)

Scope: 
static
> 源码：[src/gameobjects/components/Origin.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Origin.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### displayOriginX {#displayOriginX}

#### displayOriginX: number {#displayoriginx-number}


**说明:**

这个游戏对象的横向显示源, 以像素表示。 不同于 `originX`, 它是一个在 0 到 1 之间的正常化值, 显示源是游戏对象宽度乘以它的 `originX`值而得出的计算出来的像素偏移 。 设置此属性时, 将 `originX` 进行相应的更新 。


> 源码：[src/gameobjects/components/Origin.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Origin.js#L62)  
引入版本：3.0.0


---

### displayOriginY {#displayOriginY}

#### displayOriginY: number {#displayoriginy-number}


**说明:**

此游戏对象的垂直显示源, 以像素表示。 不同于 `originY`, 它是一个在 0 到 1 之间的正常值, 显示源是游戏对象高度乘以它的 `originY`值而得出的计算像素偏移。 设置此属性时相应更新 `originY` 。


> 源码：[src/gameobjects/components/Origin.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Origin.js#L87)  
引入版本：3.0.0


---

### originX {#originX}

#### originX: number {#originx-number}


**说明:**

此游戏对象的横向来源。 来源图示了游戏对象大小和位置之间的关系。 默认值为 0. 5, 表示所有游戏对象的位置都基于其中心。 设定值为 0 表示该位置与游戏对象左侧相关。 用 `setOrigin()` 设定此值 。


> 源码：[src/gameobjects/components/Origin.js#L30](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Origin.js#L30)  
引入版本：3.0.0


---

### originY {#originY}

#### originY: number {#originy-number}


**说明:**

此游戏对象的垂直来源。 来源图示了游戏对象大小和位置之间的关系。 默认值为 0. 5, 表示所有游戏对象都根据中心定位。 设定值为 0 表示当前位置与游戏对象顶端相关。 以 `setOrigin()` 设定此值 。


> 源码：[src/gameobjects/components/Origin.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Origin.js#L44)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### setDisplayOrigin {#setDisplayOrigin}

#### \<instance> setDisplayOrigin([x], [y]) {#instance-setdisplayoriginx-y}


**说明:**

设置此游戏对象的显示源。 此和设置源的区别在于, 您可以使用像素值来设置显示源 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 水平显示源值 。 |
| y | number | 是 | "x" | 垂直显示源值。 如果定义不明确, 将设定为 `x` 值 。 |


**返回值:** [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Origin.js#L162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Origin.js#L162)  
引入版本：3.0.0


---

### setOrigin {#setOrigin}

#### \<instance> setOrigin([x], [y]) {#instance-setoriginx-y}


**说明:**

设置此游戏对象的源头 。

数值在0到1之间。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0.5 | 水平源值 。 |
| y | number | 是 | "x" | 垂直源值。 如果定义不明确, 则将设定为 `x` 值 。 |


**返回值:** [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Origin.js#L112](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Origin.js#L112)  
引入版本：3.0.0


---

### setOriginFromFrame {#setOriginFromFrame}

#### \<instance> setOriginFromFrame() {#instance-setoriginfromframe}


**说明:**

设定基于其框架中的枢轴值的游戏对象的源头。 如果框架定义了自定义的枢轴点, 则设定源头与之匹配。 如果框架没有自定义的枢轴, 这种方法会回到 `setOrigin()`, 将源头重置为两个轴的默认值0. 5 。


**返回值:** [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Origin.js#L136](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Origin.js#L136)  
引入版本：3.0.0


---

### updateDisplayOrigin {#updateDisplayOrigin}

#### \<instance> updateDisplayOrigin() {#instance-updatedisplayorigin}


**说明:**

更新存储在此游戏对象上的“显示源”缓存值。您通常不直接调用,但会暴露在边缘大小写中。


**返回值:** [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Origin.js#L185](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Origin.js#L185)  
引入版本：3.0.0


---

---
