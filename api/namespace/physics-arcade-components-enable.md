# Phaser.Physics.Arcade.Components.Enable {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-components-enable)

Scope: 
static
> 源码：[src/physics/arcade/components/Enable.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Enable.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### disableBody {#disableBody}

#### \<instance> disableBody([disableGameObject], [hideGameObject]) {#instance-disablebodydisablegameobject-hidegameobject}


**说明:**

停止并禁用此游戏对象的Arcade 物理体。 物理体的速度设定为零, 并且从物理模拟中的碰撞和重叠检测中移除。 可选的设置为游戏对象的`active`和`visible`属性同时为假, 用于解除集合游戏对象的激活时 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disableGameObject | boolean | 是 | false | 还将此游戏对象的 `active` 设定为虚假 。 |
| hideGameObject | boolean | 是 | false | 还将此游戏对象的 `visible` 设定为虚假 。 |


**返回值:** [Phaser.Physics.Arcade.Components.Enable](/api/namespace/physics-arcade-components-enable) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Enable.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Enable.js#L87)  
引入版本：3.0.0


---

### enableBody {#enableBody}

#### \<instance> enableBody([reset], [x], [y], [enableGameObject], [showGameObject]) {#instance-enablebodyreset-x-y-enablegameobject-showgameobject}


**说明:**

启用此游戏对象的Arcade 物理体, 允许它参与物理模拟中的碰撞和重叠检测。 可选地将对象重排, 并重新定位到指定的坐标。 如果您重设对象, 您也必须通过 `x` 和 `y` 。 您也可以选择同时设置游戏对象的 `active` 和 `visible` 属性 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| reset | boolean | 是 | 同时重置物理体,并放置游戏对象于(x,y). |
| x | number | 是 | 如果 `reset` 是真的, 则设置游戏对象的横向位置 。 |
| y | number | 是 | 如果 `reset` 是真的, 设置游戏对象的垂直位置 。 |
| enableGameObject | boolean | 是 | 同时设定此游戏对象的 `active` 真实性 。 |
| showGameObject | boolean | 是 | 同时设定此游戏对象的 `visible` 真实性 。 |


**返回值:** [Phaser.Physics.Arcade.Components.Enable](/api/namespace/physics-arcade-components-enable) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Enable.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Enable.js#L40)  
引入版本：3.0.0


---

### refreshBody {#refreshBody}

#### \<instance> refreshBody() {#instance-refreshbody}


**说明:**

将物理体的位置和大小与它的父游戏对象同步。 您不需要将它称为动态对象, 因为它会自动发生。 但对于静态对象来说, 静态对象是一种有用的方法, 它可以基于它的游戏对象来修改静态对象在物理世界中的地位 。


**返回值:** [Phaser.Physics.Arcade.Components.Enable](/api/namespace/physics-arcade-components-enable) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Enable.js#L128](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Enable.js#L128)  
引入版本：3.1.0


---

### setDirectControl {#setDirectControl}

#### \<instance> setDirectControl([value]) {#instance-setdirectcontrolvalue}


**说明:**

设定此物理体是否应该根据它在每个框架的位置变化来计算其速度。 默认, 即不这样做, 意味着您通过直接设置速度来让此物理体移动。 然而, 如果您试图通过调温移动此物理体, 或者它遵循路径, 那么您应该启用它。 这将允许它与其他物理体碰撞, 如果您只是直接改变它的位置, 则不可能实现 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 如果机体根据位置变化计算速度,则`true`,否则则`false`. |


**返回值:** [Phaser.Physics.Arcade.Components.Enable](/api/namespace/physics-arcade-components-enable) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Enable.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Enable.js#L18)  
引入版本：3.70.0


---

---
