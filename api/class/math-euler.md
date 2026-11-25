# Euler {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/math-euler)

代表用于3D旋转的一组欧勒角度(绕X,Y,和Z轴旋转). Euler角度用坐标轴周围连续三次旋转来描述方向. `order`属性定义了哪些轴以及采用旋转的顺序(例如,"XYZ"先应用X周围旋转,然后应用Y,然后应用Z).

**构造函数**

`new Euler([x], [y], [z], [order])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 围绕X轴旋转,以弧度表示. |
| y | number | 是 | 0 | 绕Y轴旋转,以弧度表示. |
| z | number | 是 | 0 | 绕Z轴旋转,以弧度表示. |
| order | string | 是 | "'XYZ'" | 旋转的顺序, 其中一个是"XYZ", “YXZ” , “ ZXY” , “ ZYX” , “ YZX” , 或 “ XZY” 。 |

---


**作用域**: static

> 源码：[src/math/Euler.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Euler.js#L14)  
引入版本：3.50.0

## 公开成员 {#public-members}

### order {#order}

#### order: string {#order-string}


**说明:**

应用 Euler 角度时使用的旋转顺序。 确定 X 、 Y 和 Z 轴周围的旋转顺序。 必须是“ XYZ ” 、 “ YXZ ” 、“ ZXY ” 、 “ ZYX ” 、 “ XZX ” 或 “ XZY ” 之一 。

如果设置了此属性, 则会引用 `onChangeCallback` 。


> 源码：[src/math/Euler.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Euler.js#L119)  
引入版本：3.50.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

围绕X轴旋转,以弧度表示.

如果设置了此属性, 则会引用 `onChangeCallback` 。


> 源码：[src/math/Euler.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Euler.js#L50)  
引入版本：3.50.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

绕Y轴旋转,以弧度表示.

如果设置了此属性, 则会引用 `onChangeCallback` 。


> 源码：[src/math/Euler.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Euler.js#L73)  
引入版本：3.50.0


---

### z {#z}

#### z: number {#z-number}


**说明:**

绕Z轴旋转,以弧度表示.

如果设置了此属性, 则会引用 `onChangeCallback` 。


> 源码：[src/math/Euler.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Euler.js#L96)  
引入版本：3.50.0


---

## 公开方法 {#public-methods}

### copy {#copy}

#### \<instance> copy(euler) {#instance-copyeuler}


**说明:**

复制X,Y,Z 从另一个欧拉实例订购属性 进入这个实例。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| euler | [Phaser.Math.Euler](/api/class/math-euler) | 否 | 欧拉的例子 复制。 |


**返回值:** [Phaser.Math.Euler](/api/class/math-euler) - 这个欧拉的例子。


> 源码：[src/math/Euler.js#L174](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Euler.js#L174)  
引入版本：3.50.0


---

### set {#set}

#### \<instance> set(x, y, z, [order]) {#instance-setx-y-z-order}


**说明:**

设置 Euler 角度的 X、 Y、 Z 组件并同时排序 。

在更新所有内部值后, `onChangeCallback` 被引用为参数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 围绕X轴旋转,以弧度表示. |
| y | number | 否 | 绕Y轴旋转,以弧度表示. |
| z | number | 否 | 绕Z轴旋转,以弧度表示. |
| order | string | 是 | 旋转顺序。 如果未指定, 默认为当前顺序 。 |


**返回值:** [Phaser.Math.Euler](/api/class/math-euler) - 这个欧拉的例子。


> 源码：[src/math/Euler.js#L144](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Euler.js#L144)  
引入版本：3.50.0


---

### setFromQuaternion {#setFromQuaternion}

#### \<instance> setFromQuaternion(quaternion, [order], [update]) {#instance-setfromquaternionquaternion-order-update}


**说明:**

使用指定的旋转顺序,从 Quaternion 设置 Euler 角度。

ennion首先在内部转换为旋转矩阵,然后`setFromRotationMatrix`被调用以得出Euler角度,这样通过矩阵表达法可以避免 gimbal 锁问题.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| quaternion | [Phaser.Math.Quaternion](/api/class/math-quaternion) | 否 |  | 以四角为单位从欧拉角度得到的 |
| order | string | 是 |  | 要使用的旋转顺序。 如果未指定, 默认为当前顺序 。 |
| update | boolean | 是 | false | 设置值后是否引用 `onChangeCallback` 。 |


**返回值:** [Phaser.Math.Euler](/api/class/math-euler) - 这个欧拉的例子。


> 源码：[src/math/Euler.js#L189](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Euler.js#L189)  
引入版本：3.50.0


---

### setFromRotationMatrix {#setFromRotationMatrix}

#### \<instance> setFromRotationMatrix(matrix, [order], [update]) {#instance-setfromrotationmatrixmatrix-order-update}


**说明:**

使用指定的旋转顺序,从四轮驱动矩阵4的左上方3x3旋转部分设置欧拉角。

矩阵被假定为纯旋转矩阵( 未缩放)。 每个支持旋转顺序都有自己的解析公式。 如果 `update` 参数是 `true`, 则在设定值后引用 `onChangeCallback` 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| matrix | [Phaser.Math.Matrix4](/api/class/math-matrix4) | 否 |  | 旋转矩阵可以从 Euler 角度得出。 必须是纯( 未标定的) 旋转矩阵 。 |
| order | string | 是 |  | 要使用的旋转顺序。 如果未指定, 默认为当前顺序 。 |
| update | boolean | 是 | false | 设置值后是否引用 `onChangeCallback` 。 |


**返回值:** [Phaser.Math.Euler](/api/class/math-euler) - 这个欧拉的例子。


> 源码：[src/math/Euler.js#L215](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Euler.js#L215)  
引入版本：3.50.0


---

---
