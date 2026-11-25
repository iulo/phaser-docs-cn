# Phaser.GameObjects.Components.Tint {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-tint)

Scope: 
static
> 源码：[src/gameobjects/components/Tint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Tint.js#L9)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### isTinted {#isTinted}

#### isTinted: boolean {#istinted-boolean}


**说明:**

此游戏对象是否应用了 tin ?

如果四个角形锡值中的任何一个与 0xffffff 不同,或者如果 `tintMode` 属性设定为 `MULTIPLY` 以外的任何值,则返回 `true` 。当所有四个角形锡值均为 0xffffff, 锡模式为 `MULTIPLY` 时,返回 `false` , 即默认的未连接状态 。

**Tags:**

 - webglOnly


> 源码：[src/gameobjects/components/Tint.js#L218](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Tint.js#L218)  
引入版本：3.11.0


---

### tint {#tint}

#### tint: number {#tint-number}


**说明:**

将数值应用到整个游戏对象。返回值为 `tintTopLeft` 当读时。写时,对所有四个角锡克属性都应用相同的颜色值(`tintTopLeft`, `tintTopRight`, `tintBottomLeft`,和 `tintBottomRight`)同时.

**Tags:**

 - webglOnly


> 源码：[src/gameobjects/components/Tint.js#L194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Tint.js#L194)  
引入版本：3.0.0


---

### tintBottomLeft {#tintBottomLeft}

#### tintBottomLeft: number {#tintbottomleft-number}


**说明:**

正在应用到游戏对象左下角顶点的锡值。该值从游戏对象的角到中心被插入。该值应该设置为六进制数字,即红色为0xff000,紫色为0xff00ff。


> 源码：[src/gameobjects/components/Tint.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Tint.js#L44)  
引入版本：3.0.0


---

### tintBottomRight {#tintBottomRight}

#### tintBottomRight: number {#tintbottomright-number}


**说明:**

正在应用到游戏对象右下方顶点的锡值。 此值从游戏对象的角到中心位置插入。 数值应该设置为六进制, 即: 0xff000 表示红色, 0xff00ff表示紫色 。


> 源码：[src/gameobjects/components/Tint.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Tint.js#L56)  
引入版本：3.0.0


---

### tintMode {#tintMode}

#### tintMode: [Phaser.TintModes](/api/namespace/tintmodes) {#tintmode-phasertintmodes}


**说明:**

将锡剂应用到纹理时使用的锡剂模式 。

可用模式有:

- Phaser.TintModes.MULTIPLY( 默认)

- Phaser.TintModes.FILL

- Phaser.TintModes.ADD

- Phaser.TintModes.SCREEN

- Phaser.TintModes.OVERLAY

- Phaser.TintModes.HARD_LIGHT

请注意, Phaser 3 中,锡模式和颜色是同时设置的。 Phaser 4 中,它们是单独的设置 。


> 源码：[src/gameobjects/components/Tint.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Tint.js#L68)  
引入版本：4.0.0


---

### tintTopLeft {#tintTopLeft}

#### tintTopLeft: number {#tinttopleft-number}


**说明:**

正在应用到游戏对象左上角顶点的锡值。该值从游戏对象的角到中心位置内插。该值应当设置为六进制,即红色为0xff000,紫色为0xff00ff。


> 源码：[src/gameobjects/components/Tint.js#L20](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Tint.js#L20)  
引入版本：3.0.0


---

### tintTopRight {#tintTopRight}

#### tintTopRight: number {#tinttopright-number}


**说明:**

正在应用到游戏对象右上方顶点的锡值。 此值从游戏对象的角到中心位置插入。 数值应该设置为六进制, 即: 0xff000 表示红色, 0xff00ff表示紫色 。


> 源码：[src/gameobjects/components/Tint.js#L32](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Tint.js#L32)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### clearTint {#clearTint}

#### \<instance> clearTint() {#instance-cleartint}


**说明:**

清除与此游戏对象相关的所有锡值。

立即将颜色值设定为0xffffff,锡模式设定为`MULTIPLY`,这导致纹理没有明显变化.

**Tags:**

 - webglOnly


**返回值:** [Phaser.GameObjects.Components.Tint](/api/namespace/gameobjects-components-tint) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Tint.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Tint.js#L89)  
引入版本：3.0.0


---

### setTint {#setTint}

#### \<instance> setTint([topLeft], [topRight], [bottomLeft], [bottomRight]) {#instance-settinttopleft-topright-bottomleft-bottomright}


**说明:**

设置此游戏对象的颜色 。

锡特通过从游戏对象纹理中取出像素颜色值,然后将其与锡的颜色值结合,来工作。您可以提供一种颜色值,在这种情况下,整个游戏对象将用该颜色涂上。或者您可以提供每个角的颜色。颜色将混合到游戏对象的全程。

要修改已设定的锡色, 要么用新值再次调用这种方法, 要么使用 `tint` 属性,可以同时设置所有颜色。或者,使用属性 `tintTopLeft`, `tintTopRight`, `tintBottomLeft` 财务报告和已审计财务报表 `tintBottomRight` 以独立设置角色值。

取出一个叫`clearTint`的字眼

锡色按照锡色模式组合。默认这是 `MULTIPLY` 。

注意,在 Phaser 3, 如果设定填充, 也会换成锡模式。  in Phaser 4, 锡模式是分开的: 使用 `setTintMode`.

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| topLeft | number | 是 | "0xffffff" | 正在应用到游戏对象左上角的锡。 如果没有其他值被给出, 则将整个游戏对象都用锡。 Name |
| topRight | number | 是 |  | 正在应用到游戏对象右上角的锡. |
| bottomLeft | number | 是 |  | 正在应用到游戏对象左下角的锡。 |
| bottomRight | number | 是 |  | 正在应用到游戏对象的右下角的锡条 。 |


**返回值:** [Phaser.GameObjects.Components.Tint](/api/namespace/gameobjects-components-tint) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Tint.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Tint.js#L109)  
引入版本：3.0.0


---

### setTintFill {#setTintFill}

#### \<instance> setTintFill() {#instance-settintfill}


**说明:**

折价方法,无用。 Phaser 3, 这将设置锡色, 并设置要填充的锡色模式。 单位 Phaser 4, 使用( 4) `gameObject.setTint(color).setTintMode(Phaser.TintModes.FILL)` 换成是的

**Tags:**

 - webglOnly


> 源码：[src/gameobjects/components/Tint.js#L178](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Tint.js#L178)  
引入版本：3.11.0


---

### setTintMode {#setTintMode}

#### \<instance> setTintMode(mode) {#instance-settintmodemode}


**说明:**

设置将锡语应用到纹理时使用的锡字模式。

请注意,Phaser 3 中,锡模式和颜色是同时设置的。在Phaser 4 中,它们是单独的设置。

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mode | number \| [Phaser.TintModes](/api/namespace/tintmodes) | 否 | 使用锡金模式 。 |


**返回值:** [Phaser.GameObjects.Components.Tint](/api/namespace/gameobjects-components-tint) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Tint.js#L159](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Tint.js#L159)  
引入版本：4.0.0


---

---
