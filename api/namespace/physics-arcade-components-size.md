# Phaser.Physics.Arcade.Components.Size {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-components-size)

Scope: 
static
> 源码：[src/physics/arcade/components/Size.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Size.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setBodySize {#setBodySize}

#### \<instance> setBodySize(width, height, [center]) {#instance-setbodysizewidth-height-center}


**说明:**

设置此物理正体的大小。 设置大小不会调整父游戏对象的尺寸 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 否 |  | 物理体的新宽度,以像素表示. |
| height | number | 否 |  | 物理体的新高度,以像素表示. |
| center | boolean | 是 | true | 身体是否应该重新定位, 使其中心与母游戏对象一致 ? |


**返回值:** [Phaser.Physics.Arcade.Components.Size](/api/namespace/physics-arcade-components-size) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Size.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Size.js#L59)  
引入版本：3.24.0


---

### setCircle {#setCircle}

#### \<instance> setCircle(radius, [offsetX], [offsetY]) {#instance-setcircleradius-offsetx-offsety}


**说明:**

设定此物理体使用圆形来进行碰撞,而不是矩形.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| radius | number | 否 | 物理体的半径,以像素表示. |
| offsetX | number | 是 | 沿x轴从母游戏对象中抵消正体的金额. |
| offsetY | number | 是 | 沿 Y 轴从母游戏对象中抵消天体的金额 。 |


**返回值:** [Phaser.Physics.Arcade.Components.Size](/api/namespace/physics-arcade-components-size) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Size.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Size.js#L78)  
引入版本：3.0.0


---

### setOffset {#setOffset}

#### \<instance> setOffset(x, [y]) {#instance-setoffsetx-y}


**说明:**

设置正文偏移。这可以调整正文中心与母游戏对象的x和y坐标之间的差。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 从父游戏对象沿x轴,以像素表示的抵消正文的金额. |
| y | number | 是 | "x" | 从母游戏对象沿 Y 轴的正文中抵消的金额, 以像素表示。 默认为 x 轴的值 。 |


**返回值:** [Phaser.Physics.Arcade.Components.Size](/api/namespace/physics-arcade-components-size) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Size.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Size.js#L18)  
引入版本：3.0.0


---

### setSize {#setSize}

#### \<instance> setSize(width, height, [center]) {#instance-setsizewidth-height-center}


**说明:**

**DEPRECATED**: 请用`setBodySize`代替.

设置此物理正体的大小。 设置大小不会调整父游戏对象的尺寸 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 否 |  | 物理体的新宽度,以像素表示. |
| height | number | 否 |  | 物理体的新高度,以像素表示. |
| center | boolean | 是 | true | 身体是否应该重新定位, 使其中心与母游戏对象一致 ? |


**返回值:** [Phaser.Physics.Arcade.Components.Size](/api/namespace/physics-arcade-components-size) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Size.js#L37](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Size.js#L37)  
引入版本：3.0.0


---

---
