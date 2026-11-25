# Phaser.Physics.Arcade.Components.Drag {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-components-drag)

Scope: 
static
> 源码：[src/physics/arcade/components/Drag.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Drag.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setDamping {#setDamping}

#### \<instance> setDamping(value) {#instance-setdampingvalue}


**说明:**

如果此物理体正在使用 `drag` 来减速此函数, 控制拖动是如何应用的。 如果设置到 `true` 拖动, 将使用一个加坝效果而不是线性方法。 如果您正在创建一个游戏, 使物理体在任意角度上自由移动( 即像小行星中的飞船) , 那么您将会通过使用加坝来获得一个更平滑、 更直观的减速, 避免线性减速而容易触发轴线的拖动 。

如果您启用此属性, 您应该使用比线性小得多的 `drag`值, 因为这些值被用作速度的乘数。 例如 0. 95 等值将给一个良好的慢减速, 在那里, 如 0. 5 等较小的值几乎会立即停止一个对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | `true`使用坝式减速,或`false`使用线性减速. |


**返回值:** [Phaser.Physics.Arcade.Components.Drag](/api/namespace/physics-arcade-components-drag) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Drag.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Drag.js#L100)  
引入版本：3.10.0


---

### setDrag {#setDrag}

#### \<instance> setDrag(x, [y]) {#instance-setdragx-y}


**说明:**

设置物理体的横向和纵向拖曳。如果不提供纵向拖曳值,则垂直拖曳值与水平拖曳值相同。

拖曳可以被认为是一种减速形式,它会随着时间的推移将一个物理体的速度还原为零。它是运动导致的速度的绝对损失,以像素每二次方秒计。x和y两个组件是分开应用的。

`useDamping`是真实的,这是1减去加压系数。1值表示物理体失去速度。0.95值表示物理体每步失去速度的5%。0.5值表示物理体每步丧失速度的50%。

拖曳只在 `acceleration` 零时才应用.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 要应用的水平拖曳量 。 |
| y | number | 是 | "x" | 要应用的垂直拖曳量 。 |


**返回值:** [Phaser.Physics.Arcade.Components.Drag](/api/namespace/physics-arcade-components-drag) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Drag.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Drag.js#L15)  
引入版本：3.0.0


---

### setDragX {#setDragX}

#### \<instance> setDragX(value) {#instance-setdragxvalue}


**说明:**

设置物理体水平拖曳。

拖曳可以被认为是一种减速形式,它会随着时间的推移将一个物理体的速度还原为零。它是运动导致的速度的绝对损失,以像素每二次方秒计。x和y两个组件是分开应用的。

`useDamping`是真实的,这是1减去加压系数。1值表示物理体失去速度。0.95值表示物理体每步失去速度的5%。0.5值表示物理体每步丧失速度的50%。

拖曳只在 `acceleration` 零时才应用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 要应用的水平拖曳量 。 |


**返回值:** [Phaser.Physics.Arcade.Components.Drag](/api/namespace/physics-arcade-components-drag) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Drag.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Drag.js#L44)  
引入版本：3.0.0


---

### setDragY {#setDragY}

#### \<instance> setDragY(value) {#instance-setdragyvalue}


**说明:**

设置物理体的垂直拖曳。

拖曳可以被认为是一种减速形式,它会随着时间的推移将一个物理体的速度还原为零。它是运动导致的速度的绝对损失,以像素每二次方秒计。x和y两个组件是分开应用的。

`useDamping`是真实的,这是1减去加压系数。1值表示物理体失去速度。0.95值表示物理体每步失去速度的5%。0.5值表示物理体每步丧失速度的50%。

拖曳只在 `acceleration` 零时才应用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 要应用的垂直拖曳量 。 |


**返回值:** [Phaser.Physics.Arcade.Components.Drag](/api/namespace/physics-arcade-components-drag) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Drag.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Drag.js#L72)  
引入版本：3.0.0


---

---
