# Phaser.GameObjects.Components.Flip {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-flip)

Scope: 
static
> 源码：[src/gameobjects/components/Flip.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Flip.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### flipX {#flipX}

#### flipX: boolean {#flipx-boolean}


**说明:**

游戏对象的横向翻转状态 。

横向翻转的游戏对象会在横向轴上反转。翻转总是从纹理中间进行,不会影响比例值。如果游戏对象有一个物理体,它不会改变主体。这只是一个渲染切换。


> 源码：[src/gameobjects/components/Flip.js#L20](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Flip.js#L20)  
引入版本：3.0.0


---

### flipY {#flipY}

#### flipY: boolean {#flipy-boolean}


**说明:**

游戏对象的垂直翻转状态 。

垂直翻转的游戏对象会在垂直轴上反转( 即倒转) 。 翻转总是从纹理中间进行, 并且不会影响比例值。 如果游戏对象有物理体, 它不会改变身体。 仅此而已 。


> 源码：[src/gameobjects/components/Flip.js#L34](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Flip.js#L34)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### resetFlip {#resetFlip}

#### \<instance> resetFlip() {#instance-resetflip}


**说明:**

将游戏对象的横向和垂直翻转状态重回默认的未擦除状态 。


**返回值:** [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Flip.js#L151](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Flip.js#L151)  
引入版本：3.0.0


---

### setFlip {#setFlip}

#### \<instance> setFlip(x, y) {#instance-setflipx-y}


**说明:**

设置此游戏对象的横向和纵向翻转状态。

翻转的游戏对象会在翻转的轴上反转。翻转总是从纹理中间进行,不会影响比例值。如果游戏对象有一个物理体,它不会改变主体。这只是一个渲染切换。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | boolean | 否 | 水平翻转状态。 `false` 用于不翻转,或者 `true` 用于翻转 。 |
| y | boolean | 否 | 垂直翻转状态。 `false` 表示不翻转,或 `true` 表示不翻转 。 |


**返回值:** [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Flip.js#L128](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Flip.js#L128)  
引入版本：3.0.0


---

### setFlipX {#setFlipX}

#### \<instance> setFlipX(value) {#instance-setflipxvalue}


**说明:**

设置此游戏对象的横向翻转状态。

横向翻转的游戏对象会在横向轴上反转。翻转总是从纹理中间进行,不会影响比例值。如果游戏对象有一个物理体,它不会改变主体。这只是一个渲染切换。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 翻转状态,`false`无翻转,或`true`被翻转. |


**返回值:** [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Flip.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Flip.js#L86)  
引入版本：3.0.0


---

### setFlipY {#setFlipY}

#### \<instance> setFlipY(value) {#instance-setflipyvalue}


**说明:**

设置此游戏对象的垂直翻转状态。

垂直翻转的游戏对象会在垂直轴上反转。翻转总是从纹理中间进行,不会影响比例值。如果游戏对象有一个物理体,它不会改变身体。这只是一个渲染切换。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 翻转状态,`false`无翻转,或`true`被翻转. |


**返回值:** [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Flip.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Flip.js#L107)  
引入版本：3.0.0


---

### toggleFlipX {#toggleFlipX}

#### \<instance> toggleFlipX() {#instance-toggleflipx}


**说明:**

切换此游戏对象的横向翻转状态。

横向翻转的游戏对象会在横向轴上反转。翻转总是从纹理中间进行,不会影响比例值。如果游戏对象有一个物理体,它不会改变主体。这只是一个渲染切换。


**返回值:** [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Flip.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Flip.js#L48)  
引入版本：3.0.0


---

### toggleFlipY {#toggleFlipY}

#### \<instance> toggleFlipY() {#instance-toggleflipy}


**说明:**

切换此游戏对象的垂直翻转状态。

垂直翻转的游戏对象会在垂直轴上反转。翻转总是从纹理中间进行,不会影响比例值。如果游戏对象有一个物理体,它不会改变身体。这只是一个渲染切换。


**返回值:** [Phaser.GameObjects.Components.Flip](/api/namespace/gameobjects-components-flip) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Flip.js#L67](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Flip.js#L67)  
引入版本：3.0.0


---

---
