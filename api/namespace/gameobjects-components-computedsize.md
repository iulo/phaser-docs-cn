# Phaser.GameObjects.Components.ComputedSize {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-computedsize)

Scope: 
static
> 源码：[src/gameobjects/components/ComputedSize.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ComputedSize.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### displayHeight {#displayHeight}

#### displayHeight: number {#displayheight-number}


**说明:**

此游戏对象的显示高度 。

这一数值考虑到了比额表系数。

设置此值将调整游戏对象的缩放属性 。


> 源码：[src/gameobjects/components/ComputedSize.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ComputedSize.js#L74)  
引入版本：3.0.0


---

### displayWidth {#displayWidth}

#### displayWidth: number {#displaywidth-number}


**说明:**

此游戏对象的显示宽度 。

这一数值考虑到了比额表系数。

设置此值将调整游戏对象的缩放属性 。


> 源码：[src/gameobjects/components/ComputedSize.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ComputedSize.js#L49)  
引入版本：3.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

此游戏对象的原生高度( 未标定) 。

更改此值不会改变游戏对象在游戏中显示的大小。 为此, 您需要设置游戏对象( `setScale`) 的大小, 或者使用 `displayHeight` 属性 。


> 源码：[src/gameobjects/components/ComputedSize.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ComputedSize.js#L36)  
引入版本：3.0.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

此游戏对象的原生( 未标定) 宽度 。

更改此值不会改变游戏对象在游戏中显示的大小。 为此, 您需要设置游戏对象( `setScale`) 的大小, 或者使用 `displayWidth` 属性 。


> 源码：[src/gameobjects/components/ComputedSize.js#L23](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ComputedSize.js#L23)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### setDisplaySize {#setDisplaySize}

#### \<instance> setDisplaySize(width, height) {#instance-setdisplaysizewidth-height}


**说明:**

设定此游戏对象的显示大小。

调用此选项将调整 `scaleX` 和 `scaleY` 属性, 使游戏对象在指定的像素维度上渲染。 它相当于手动设置比例表, 但以像素表示, 而不是作为乘数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 此游戏对象的宽度 。 |
| height | number | 否 | 此游戏对象的高度 。 |


**返回值:** [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/ComputedSize.js#L126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ComputedSize.js#L126)  
引入版本：3.4.0


---

### setSize {#setSize}

#### \<instance> setSize(width, height) {#instance-setsizewidth-height}


**说明:**

设置用于帧或物理体创建的此游戏对象的内部大小。

这将不会改变游戏对象在游戏中渲染的大小。 为此, 您需要设置游戏对象的大小( `setScale`) 或调用 `setDisplaySize` 方法, 与改变大小是相同的, 但允许您通过像素值来做到这一点 。

如果您启用了此游戏对象输入, 更改大小将_ not_ 更改命中区域的大小。 要做到这一点, 您应该直接调整 `input.hitArea` 对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 此游戏对象的宽度 。 |
| height | number | 否 | 此游戏对象的高度 。 |


**返回值:** [Phaser.GameObjects.Components.ComputedSize](/api/namespace/gameobjects-components-computedsize) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/ComputedSize.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/ComputedSize.js#L99)  
引入版本：3.4.0


---

---
