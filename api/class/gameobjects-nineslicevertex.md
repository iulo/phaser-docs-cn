# NineSliceVertex {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-nineslicevertex)

代表一个九角星游戏对象中的单个顶点。

一个NineSlice游戏对象被分为3x3区域网格,每个网格由网格的顶点定义. 这个类存储一个顶点所需的全部数据:它的正态位置(x,y继承自矢量2),它的预测屏幕-空间位置(vx,vy),以及它在渲染时使用的UV纹理坐标(u,v).

您通常不会直接创建 NineSlicVertex 实例。 它们是由 NineSlic 游戏对象创建和管理的 。

**构造函数**

`new NineSliceVertex(x, y, u, v)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 顶点的x位置. |
| y | number | 否 | 顶点的y位置. |
| u | number | 否 | 顶点的紫外线u坐标. |
| v | number | 否 | 紫外线v顶点坐标. |

---


**作用域**: static


**继承**

> [Phaser.Math.Vector2](/api/class/math-vector2)  



> 源码：[src/gameobjects/nineslice/NineSliceVertex.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSliceVertex.js#L10)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Math.Vector2](/api/class/math-vector2):**


 - [x](/api/class/math-vector2#x)
 - [y](/api/class/math-vector2#y)




---

## 公开成员 {#public-members}

### u {#u}

#### u: number {#u-number}


**说明:**

紫外线u坐标 这个顶点。


> 源码：[src/gameobjects/nineslice/NineSliceVertex.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSliceVertex.js#L61)  
引入版本：4.0.0


---

### v {#v}

#### v: number {#v-number}


**说明:**

UV v 坐标为此顶点 。


> 源码：[src/gameobjects/nineslice/NineSliceVertex.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSliceVertex.js#L70)  
引入版本：4.0.0


---

### vx {#vx}

#### vx: number {#vx-number}


**说明:**

这个顶点的预测x坐标.


> 源码：[src/gameobjects/nineslice/NineSliceVertex.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSliceVertex.js#L43)  
引入版本：4.0.0


---

### vy {#vy}

#### vy: number {#vy-number}


**说明:**

这个顶点的预测Y坐标 。


> 源码：[src/gameobjects/nineslice/NineSliceVertex.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSliceVertex.js#L52)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Math.Vector2](/api/class/math-vector2):**


 - [add](/api/class/math-vector2#add)
 - [angle](/api/class/math-vector2#angle)
 - [ceil](/api/class/math-vector2#ceil)
 - [clone](/api/class/math-vector2#clone)
 - [copy](/api/class/math-vector2#copy)
 - [cross](/api/class/math-vector2#cross)
 - [distance](/api/class/math-vector2#distance)
 - [distanceSq](/api/class/math-vector2#distanceSq)
 - [divide](/api/class/math-vector2#divide)
 - [dot](/api/class/math-vector2#dot)
 - [equals](/api/class/math-vector2#equals)
 - [floor](/api/class/math-vector2#floor)
 - [fuzzyEquals](/api/class/math-vector2#fuzzyEquals)
 - [invert](/api/class/math-vector2#invert)
 - [length](/api/class/math-vector2#length)
 - [lengthSq](/api/class/math-vector2#lengthSq)
 - [lerp](/api/class/math-vector2#lerp)
 - [limit](/api/class/math-vector2#limit)
 - [mirror](/api/class/math-vector2#mirror)
 - [multiply](/api/class/math-vector2#multiply)
 - [negate](/api/class/math-vector2#negate)
 - [normalize](/api/class/math-vector2#normalize)
 - [normalizeLeftHand](/api/class/math-vector2#normalizeLeftHand)
 - [normalizeRightHand](/api/class/math-vector2#normalizeRightHand)
 - [project](/api/class/math-vector2#project)
 - [projectUnit](/api/class/math-vector2#projectUnit)
 - [reflect](/api/class/math-vector2#reflect)
 - [reset](/api/class/math-vector2#reset)
 - [rotate](/api/class/math-vector2#rotate)
 - [scale](/api/class/math-vector2#scale)
 - [set](/api/class/math-vector2#set)
 - [setAngle](/api/class/math-vector2#setAngle)
 - [setFromObject](/api/class/math-vector2#setFromObject)
 - [setLength](/api/class/math-vector2#setLength)
 - [setTo](/api/class/math-vector2#setTo)
 - [setToPolar](/api/class/math-vector2#setToPolar)
 - [subtract](/api/class/math-vector2#subtract)
 - [transformMat3](/api/class/math-vector2#transformMat3)
 - [transformMat4](/api/class/math-vector2#transformMat4)




---

## 公开方法 {#public-methods}

### resize {#resize}

#### \<instance> resize(x, y, width, height, originX, originY) {#instance-resizex-y-width-height-originx-originy}


**说明:**

更新这个顶点的位置并计算其预测的屏幕-空间坐标.

设置已规范 `x` 财务报告和已审计财务报表 `y` 位置,然后按主对象的大小 `width` 财务报告和已审计财务报表 `height` 将产生预测 `vx` 财务报告和已审计财务报表 `vy` 值。然后将母对象的源值抵消,并计入,移转 `vx` 财务报告和已审计财务报表 `vy` ,使网格相对于对象的原点正确对齐。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 顶点的x位置. |
| y | number | 否 | 顶点的y位置. |
| width | number | 否 | 父对象的宽度 。 |
| height | number | 否 | 父对象的高度 。 |
| originX | number | 否 | 母对象的 originX 。 |
| originY | number | 否 | 母对象的 originY 。 |


**返回值:** [Phaser.GameObjects.NineSliceVertex](/api/class/gameobjects-nineslicevertex) - 这个Vertex。


> 源码：[src/gameobjects/nineslice/NineSliceVertex.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSliceVertex.js#L99)  
引入版本：4.0.0


---

### setUVs {#setUVs}

#### \<instance> setUVs(u, v) {#instance-setuvsu-v}


**说明:**

设置此顶点的紫外线纹理坐标 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| u | number | 否 | 顶点的紫外线u坐标. |
| v | number | 否 | 紫外线v顶点坐标. |


**返回值:** [Phaser.GameObjects.NineSliceVertex](/api/class/gameobjects-nineslicevertex) - 这个Vertex。


> 源码：[src/gameobjects/nineslice/NineSliceVertex.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/NineSliceVertex.js#L80)  
引入版本：4.0.0


---

---
