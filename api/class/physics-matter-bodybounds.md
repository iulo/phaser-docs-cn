# BodyBounds {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-matter-bodybounds)

物理体边界类包含一些方法,可以帮助您从物质实体的边界周围的各个点提取世界坐标。由于物质实体的位置是基于其质量中心,而不是基于维度的中心,所以您往往需要获得边界坐标,以便正确调整它们在世界中的位置。

您可以通过场景的物理课进入这个课,即:

```javascript
this.matter.bodyBounds.getTopLeft(body);
```

另见`MatterPhysics.alignBody`方法.


**作用域**: static

> 源码：[src/physics/matter-js/BodyBounds.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/BodyBounds.js#L10)  
引入版本：3.22.0

## 公开成员 {#public-members}

### boundsCenter {#boundsCenter}

#### boundsCenter: [Phaser.Math.Vector2](/api/class/math-vector2) {#boundscenter-phasermathvector2}


**说明:**

一个矢量2,它通过本类中的方法计算时存储临时的边框中心值.


> 源码：[src/physics/matter-js/BodyBounds.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/BodyBounds.js#L36)  
引入版本：3.22.0


---

### centerDiff {#centerDiff}

#### centerDiff: [Phaser.Math.Vector2](/api/class/math-vector2) {#centerdiff-phasermathvector2}


**说明:**

用于在此类中按方法计算时存储临时中心 diff 值的矢量 2 。


> 源码：[src/physics/matter-js/BodyBounds.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/BodyBounds.js#L45)  
引入版本：3.22.0


---

## 公开方法 {#public-methods}

### getBottomCenter {#getBottomCenter}

#### \<instance> getBottomCenter(body, [x], [y]) {#instance-getbottomcenterbody-x-y}


**说明:**

取一个体并返回其_bounds_的下方中心的世界坐标。

物理体界限通过 Matter 的每个步骤和因素在尺度和旋转中更新。 这将根据物理体的_ current_ 位置和界限返回世界坐标 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) | 否 |  | 物理体从得到的位置。 |
| x | number | 是 | 0 | 可选水平偏移,以添加返回的坐标。 |
| y | number | 是 | 0 | 可选垂直偏移,以添加返回的坐标 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2), false - 含有坐标的矢量2,或者如果无法剖析物理体,则使用`false`.


> 源码：[src/physics/matter-js/BodyBounds.js#L330](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/BodyBounds.js#L330)  
引入版本：3.22.0


---

### getBottomLeft {#getBottomLeft}

#### \<instance> getBottomLeft(body, [x], [y]) {#instance-getbottomleftbody-x-y}


**说明:**

取一个物理体并返回其 _bours_左下方的世界坐标。

物理体界限通过 Matter 的每个步骤和因素在尺度和旋转中更新。 这将根据物理体的_ current_ 位置和界限返回世界坐标 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) | 否 |  | 物理体从得到的位置。 |
| x | number | 是 | 0 | 可选水平偏移,以添加返回的坐标。 |
| y | number | 是 | 0 | 可选垂直偏移,以添加返回的坐标 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2), false - 含有坐标的矢量2,或者如果无法剖析物理体,则使用`false`.


> 源码：[src/physics/matter-js/BodyBounds.js#L296](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/BodyBounds.js#L296)  
引入版本：3.22.0


---

### getBottomRight {#getBottomRight}

#### \<instance> getBottomRight(body, [x], [y]) {#instance-getbottomrightbody-x-y}


**说明:**

取一个物理体并返回其_bounds_的下方右侧的世界坐标。

物理体界限通过 Matter 的每个步骤和因素在尺度和旋转中更新。 这将根据物理体的_ current_ 位置和界限返回世界坐标 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) | 否 |  | 物理体从得到的位置。 |
| x | number | 是 | 0 | 可选水平偏移,以添加返回的坐标。 |
| y | number | 是 | 0 | 可选垂直偏移,以添加返回的坐标 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2), false - 含有坐标的矢量2,或者如果无法剖析物理体,则使用`false`.


> 源码：[src/physics/matter-js/BodyBounds.js#L364](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/BodyBounds.js#L364)  
引入版本：3.22.0


---

### getCenter {#getCenter}

#### \<instance> getCenter(body, [x], [y]) {#instance-getcenterbody-x-y}


**说明:**

取一个物理体,返回其中心世界坐标_bounds_。

物理体界限通过 Matter 的每个步骤和因素在尺度和旋转中更新。 这将根据物理体的_ current_ 位置和界限返回世界坐标 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) | 否 |  | 物理体从得到的位置。 |
| x | number | 是 | 0 | 可选水平偏移,以添加返回的坐标。 |
| y | number | 是 | 0 | 可选垂直偏移,以添加返回的坐标 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2), false - 含有坐标的矢量2,或者如果无法剖析物理体,则使用`false`.


> 源码：[src/physics/matter-js/BodyBounds.js#L229](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/BodyBounds.js#L229)  
引入版本：3.22.0


---

### getLeftCenter {#getLeftCenter}

#### \<instance> getLeftCenter(body, [x], [y]) {#instance-getleftcenterbody-x-y}


**说明:**

取一个体并返回其_bounds_左中点的世界坐标。

物理体界限通过 Matter 的每个步骤和因素在尺度和旋转中更新。 这将根据物理体的_ current_ 位置和界限返回世界坐标 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) | 否 |  | 物理体从得到的位置。 |
| x | number | 是 | 0 | 可选水平偏移,以添加返回的坐标。 |
| y | number | 是 | 0 | 可选垂直偏移,以添加返回的坐标 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2), false - 含有坐标的矢量2,或者如果无法剖析物理体,则使用`false`.


> 源码：[src/physics/matter-js/BodyBounds.js#L195](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/BodyBounds.js#L195)  
引入版本：3.22.0


---

### getRightCenter {#getRightCenter}

#### \<instance> getRightCenter(body, [x], [y]) {#instance-getrightcenterbody-x-y}


**说明:**

取一个物理体并返回其_bounds_的右中心的世界坐标。

物理体界限通过 Matter 的每个步骤和因素在尺度和旋转中更新。 这将根据物理体的_ current_ 位置和界限返回世界坐标 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) | 否 |  | 物理体从得到的位置。 |
| x | number | 是 | 0 | 可选水平偏移,以添加返回的坐标。 |
| y | number | 是 | 0 | 可选垂直偏移,以添加返回的坐标 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2), false - 含有坐标的矢量2,或者如果无法剖析物理体,则使用`false`.


> 源码：[src/physics/matter-js/BodyBounds.js#L262](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/BodyBounds.js#L262)  
引入版本：3.22.0


---

### getTopCenter {#getTopCenter}

#### \<instance> getTopCenter(body, [x], [y]) {#instance-gettopcenterbody-x-y}


**说明:**

取一个物理体并返回其顶端中心世界坐标_bounds_。

物理体界限通过 Matter 的每个步骤和因素在尺度和旋转中更新。 这将根据物理体的_ current_ 位置和界限返回世界坐标 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) | 否 |  | 物理体从得到的位置。 |
| x | number | 是 | 0 | 可选水平偏移,以添加返回的坐标。 |
| y | number | 是 | 0 | 可选垂直偏移,以添加返回的坐标 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2), false - 含有坐标的矢量2,或者如果无法剖析物理体,则使用`false`.


> 源码：[src/physics/matter-js/BodyBounds.js#L127](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/BodyBounds.js#L127)  
引入版本：3.22.0


---

### getTopLeft {#getTopLeft}

#### \<instance> getTopLeft(body, [x], [y]) {#instance-gettopleftbody-x-y}


**说明:**

取一个物理体并返回其_bourns_左上角的世界坐标。

物理体界限通过 Matter 的每个步骤和因素在尺度和旋转中更新。 这将根据物理体的_ current_ 位置和界限返回世界坐标 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) | 否 |  | 物理体从得到的位置。 |
| x | number | 是 | 0 | 可选水平偏移,以添加返回的坐标。 |
| y | number | 是 | 0 | 可选垂直偏移,以添加返回的坐标 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2), false - 含有坐标的矢量2,或者如果无法剖析物理体,则使用`false`.


> 源码：[src/physics/matter-js/BodyBounds.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/BodyBounds.js#L93)  
引入版本：3.22.0


---

### getTopRight {#getTopRight}

#### \<instance> getTopRight(body, [x], [y]) {#instance-gettoprightbody-x-y}


**说明:**

取一个物理体并返回其顶部右侧的世界坐标_bounds_。

物理体界限通过 Matter 的每个步骤和因素在尺度和旋转中更新。 这将根据物理体的_ current_ 位置和界限返回世界坐标 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) | 否 |  | 物理体从得到的位置。 |
| x | number | 是 | 0 | 可选水平偏移,以添加返回的坐标。 |
| y | number | 是 | 0 | 可选垂直偏移,以添加返回的坐标 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2), false - 含有坐标的矢量2,或者如果无法剖析物理体,则使用`false`.


> 源码：[src/physics/matter-js/BodyBounds.js#L161](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/BodyBounds.js#L161)  
引入版本：3.22.0


---

### parseBody {#parseBody}

#### \<instance> parseBody(body) {#instance-parsebodybody}


**说明:**

解析给定的物理体以从中获取 diff 值的界限 。

存放于本类中,属于临时属性的`boundsCenter`和`centerDiff`.

这种方法在本类中被所有其他方法自动称为方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| body | [Phaser.Types.Physics.Matter.MatterBody](/api/typedef/types-physics-matter#matterbody) | 否 | 物理体来获得极限位置。 |


**返回值:** boolean - 如果能拿到界码,就用`true`,否则用`false`.


> 源码：[src/physics/matter-js/BodyBounds.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/BodyBounds.js#L55)  
引入版本：3.22.0


---

---
