# Phaser.GameObjects.Components.Depth {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-depth)

Scope: 
static
> 源码：[src/gameobjects/components/Depth.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Depth.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### depth {#depth}

#### depth: number {#depth-number}


**说明:**

此游戏对象在场景中的深度。 确保此值只设置为数字数据类型 。

深度在一些环境中也被称为"z-index",并允许您更改Game Objects的渲染顺序,而不会实际移动其在显示列表中的位置.

默认深度为 0。 深度值较高的游戏对象总是在值较低的游戏对象前面渲染 。

设置深度会排队在场景内进行深度排序事件 。


> 源码：[src/gameobjects/components/Depth.js#L30](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Depth.js#L30)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### setAbove {#setAbove}

#### \<instance> setAbove(gameObject) {#instance-setabovegameobject}


**说明:**

移动此游戏对象, 使其出现在给定的游戏对象上方 。

这意味着它会紧接着显示列表中的另一个对象来渲染.

两种物体必须属于相同的显示列表,或父容器。

这种方法不会改变这个 Game Objects `depth` 值, 它只是改变它的列表位置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 移动到此游戏对象的游戏对象 。 |


**返回值:** [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Depth.js#L138](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Depth.js#L138)  
引入版本：3.85.0


---

### setBelow {#setBelow}

#### \<instance> setBelow(gameObject) {#instance-setbelowgameobject}


**说明:**

移动此游戏对象,使其出现在给定的游戏对象下方 。

这意味着它会立即在显示列表中的另一对象下渲染.

两种物体必须属于相同的显示列表,或父容器。

这种方法不会改变这个 Game Objects `depth` 值, 它只是改变它的列表位置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 将移动到下面的游戏对象 。 |


**返回值:** [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Depth.js#L166](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Depth.js#L166)  
引入版本：3.85.0


---

### setDepth {#setDepth}

#### \<instance> setDepth(value) {#instance-setdepthvalue}


**说明:**

设定此游戏对象的深度。 如果未提供 `value` 参数, 深度默认为 `0` 。

深度在一些环境中也被称为"z-index",并允许您更改Game Objects的渲染顺序,而不会实际移动其在显示列表中的位置.

深度值较高的游戏对象总是会在数值较低的游戏对象面前渲染.

设置深度会排队在场景内进行深度排序事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 此游戏对象的深度。 确保此值仅是一个数字数据类型 。 |


**返回值:** [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Depth.js#L64](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Depth.js#L64)  
引入版本：3.0.0


---

### setToBack {#setToBack}

#### \<instance> setToBack() {#instance-settoback}


**说明:**

将此游戏对象设定到显示列表的背面, 或其父容器的背面。

背面的距离意味着它会让一切变得低于其他的距离

这种方法不会改变这个 Game Objects `depth` 值, 它只是改变它的列表位置 。


**返回值:** [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Depth.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Depth.js#L114)  
引入版本：3.85.0


---

### setToTop {#setToTop}

#### \<instance> setToTop() {#instance-settotop}


**说明:**

设定此游戏对象位于显示列表的首位,或者其父容器的首位.

处于顶端意味着它会 使其他一切。

这种方法不会改变这个 Game Objects `depth` 值, 它只是改变它的列表位置 。


**返回值:** [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Depth.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Depth.js#L90)  
引入版本：3.85.0


---

---
