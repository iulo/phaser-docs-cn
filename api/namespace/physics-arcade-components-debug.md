# Phaser.Physics.Arcade.Components.Debug {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-components-debug)

Scope: 
static
> 源码：[src/physics/arcade/components/Debug.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Debug.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setDebug {#setDebug}

#### \<instance> setDebug(showBody, showVelocity, bodyColor) {#instance-setdebugshowbody-showvelocity-bodycolor}


**说明:**

设置此物理体的调试值。

机构只有在已启用整个Arcade Physics 调试时才会绘制调试。 请注意, 绘制调试显示时需要花费性能, 生产中不应该使用调试 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| showBody | boolean | 否 | 设定为 `true` , 以使此物理体将其大纲变成调试显示 。 |
| showVelocity | boolean | 否 | 设定为 `true` , 以使此物理体为调试显示制成一个速度标记 。 |
| bodyColor | number | 否 | 向调试显示器渲染时的物理体轮廓颜色 。 |


**返回值:** [Phaser.Physics.Arcade.Components.Debug](/api/namespace/physics-arcade-components-debug) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Debug.js#L20](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Debug.js#L20)  
引入版本：3.0.0


---

### setDebugBodyColor {#setDebugBodyColor}

#### \<instance> setDebugBodyColor(value) {#instance-setdebugbodycolorvalue}


**说明:**

设置调试显示时的物理体轮廓颜色。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 向调试显示器渲染时的物理体轮廓颜色 。 |


**返回值:** [Phaser.Physics.Arcade.Components.Debug](/api/namespace/physics-arcade-components-debug) - 此游戏对象 。


> 源码：[src/physics/arcade/components/Debug.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Debug.js#L44)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### debugBodyColor {#debugBodyColor}

#### debugBodyColor: number {#debugbodycolor-number}


**说明:**

调试显示时的物理体轮廓颜色 。


> 源码：[src/physics/arcade/components/Debug.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Debug.js#L103)  
引入版本：3.0.0


---

### debugShowBody {#debugShowBody}

#### debugShowBody: boolean {#debugshowbody-boolean}


**说明:**

设定为 `true` , 以使此物理体将其大纲变成调试显示 。


> 源码：[src/physics/arcade/components/Debug.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Debug.js#L61)  
引入版本：3.0.0


---

### debugShowVelocity {#debugShowVelocity}

#### debugShowVelocity: boolean {#debugshowvelocity-boolean}


**说明:**

设定为 `true` , 以使此物理体为调试显示制成一个速度标记 。


> 源码：[src/physics/arcade/components/Debug.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/Debug.js#L82)  
引入版本：3.0.0


---

---
