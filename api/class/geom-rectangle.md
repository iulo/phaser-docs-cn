# Rectangle {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/geom-rectangle)

矩形是轴向相交区域,由它的左上角位置定义的2D空间(`x`, `y`及其层面(第12条)`width`, `height`它是其中的核心几何原始物之一 Phaser 并被广泛用于整个框架的边界检查、摄像机、受冲击地区、凸轮区和UI布局。

矩形支持封闭试验、周边点取样和通过该装置可以使用的许多其他几何操作。 `Phaser.Geom.Rectangle` 静态方法。 `left`, `right`, `top`, `bottom`, `centerX`,和 `centerY` 属性为获取衍生位置值提供了方便,可以直接设定为矩形的重新定位或调整大小.

**构造函数**

`new Rectangle([x], [y], [width], [height])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 矩形左上角的X坐标. |
| y | number | 是 | 0 | 矩形左上角的Y坐标. |
| width | number | 是 | 0 | 矩形的宽度 。 |
| height | number | 是 | 0 | 矩形的高度. |

---


**作用域**: static

> 源码：[src/geom/rectangle/Rectangle.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L15)  
引入版本：3.0.0

## 公开方法 {#public-methods}

### Area {#Area}

#### \<static> Area(rect) {#static-arearect}


**说明:**

计算给定矩形对象的区域。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 用于计算区域范围的矩形。 |


**返回值:** number - 矩形天体的区域。


> 源码：[src/geom/rectangle/Area.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Area.js#L7)  
引入版本：3.0.0


---

### Ceil {#Ceil}

#### \<static> Ceil(rect) {#static-ceilrect}


**说明:**

绕一个矩形的位置,其最小整数大于或等于每个电流坐标。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形要调整. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 调整后的矩形.


> 源码：[src/geom/rectangle/Ceil.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Ceil.js#L7)  
引入版本：3.0.0


---

### CeilAll {#CeilAll}

#### \<static> CeilAll(rect) {#static-ceilallrect}


**说明:**

圆形矩形的位置和大小,以大于或等于每个相应值的最小整数为限。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形要修改 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 修改后的矩形.


> 源码：[src/geom/rectangle/CeilAll.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/CeilAll.js#L7)  
引入版本：3.0.0


---

### CenterOn {#CenterOn}

#### \<static> CenterOn(rect, x, y) {#static-centeronrect-x-y}


**说明:**

移动矩形左上角,使其中心位于给定坐标。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形要以圆为中心. |
| x | number | 否 | 矩形中心X坐标. |
| y | number | 否 | 矩形中心Y坐标. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 中心矩形(原变种).


> 源码：[src/geom/rectangle/CenterOn.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/CenterOn.js#L7)  
引入版本：3.0.0


---

### Clone {#Clone}

#### \<static> Clone(source) {#static-clonesource}


**说明:**

创建与给定的矩形相同的新矩形。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形变克隆. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 新建的矩形,它与给定的矩形是分开的.


> 源码：[src/geom/rectangle/Clone.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Clone.js#L9)  
引入版本：3.0.0


---

### contains {#contains}

#### \<instance> contains(x, y) {#instance-containsx-y}


**说明:**

检查给定的点是否在矩形的界限内 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 检查点的X坐标 |
| y | number | 否 | 检查点的Y坐标 |


**返回值:** boolean - 如果点在矩形的界限内,则`true`,否则则`false`.


> 源码：[src/geom/rectangle/Rectangle.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L99)  
引入版本：3.0.0


---

### Contains {#Contains}

#### \<static> Contains(rect, x, y) {#static-containsrect-x-y}


**说明:**

检查某个点是否位于矩形的界限内。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形要检查。 |
| x | number | 否 | 检查点的X坐标 |
| y | number | 否 | 检查点的Y坐标 |


**返回值:** boolean - 如果点在矩形的界限内,则`true`,否则则`false`.


> 源码：[src/geom/rectangle/Contains.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Contains.js#L7)  
引入版本：3.0.0


---

### ContainsPoint {#ContainsPoint}

#### \<static> ContainsPoint(rect, vec) {#static-containspointrect-vec}


**说明:**

确定指定的点是否包含在这个矩形对象定义的矩形区域之内。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形对象. |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 矢量2对象检查坐标 。 |


**返回值:** boolean - 如果矩形对象包含指定的点,则真实值,否则为虚假值。


> 源码：[src/geom/rectangle/ContainsPoint.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/ContainsPoint.js#L9)  
引入版本：3.0.0


---

### ContainsRect {#ContainsRect}

#### \<static> ContainsRect(rectA, rectB) {#static-containsrectrecta-rectb}


**说明:**

如果一个矩形完全包含另一个矩形。 如果一个矩形的边缘( 左、 右、 上、 下) 全部严格位于外矩形的界限内, 则该矩形被认为完全被控制。 仅触摸或重叠的矩形并不被视为被控制 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectA | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 外矩作为容器进行试验. |
| rectB | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 内侧矩形测试rectA内部的全封闭. |


**返回值:** boolean - 只有rectA完全包含rectB时才算属实.


> 源码：[src/geom/rectangle/ContainsRect.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/ContainsRect.js#L7)  
引入版本：3.0.0


---

### CopyFrom {#CopyFrom}

#### \<static> CopyFrom(source, dest) {#static-copyfromsource-dest}


**说明:**

将一个矩形的值复制到一个目的地矩形。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 源矩形复制这些值。 |
| dest | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 目标矩形将数值复制到 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 目的地矩形.


> 源码：[src/geom/rectangle/CopyFrom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/CopyFrom.js#L7)  
引入版本：3.0.0


---

### Decompose {#Decompose}

#### \<static> Decompose(rect, [out]) {#static-decomposerect-out}


**说明:**

创建矩形四个角的平面 `{x, y}` 点对象阵列, 顺序为: 左上右下右下左下。 如果提供了输出数组, 每个点对象将被推到它的末尾, 否则将创建并返回一个新的数组 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 要分解的矩形对象 。 |
| out | array | 是 | 如果提供,每个点都会被添加到这个数组中. |


**返回值:** array - 将返回您指定的数组或包含矩形点的新数组。


> 源码：[src/geom/rectangle/Decompose.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Decompose.js#L7)  
引入版本：3.0.0


---

### Equals {#Equals}

#### \<static> Equals(rect, toCompare) {#static-equalsrect-tocompare}


**说明:**

比较 `x`, `y`, `width` 财务报告和已审计财务报表 `height` 返回 `true` 只有所有四个值都完全使用严格的平等。此函数并不认为具有相同区域但不同位置或维度的矩形是平等的。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 初对矩相类. |
| toCompare | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 与第二矩相对. |


**返回值:** boolean - 如果矩形的属性是精确匹配的,则`true`,否则`false`.


> 源码：[src/geom/rectangle/Equals.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Equals.js#L7)  
引入版本：3.0.0


---

### FitInside {#FitInside}

#### \<static> FitInside(target, source) {#static-fitinsidetarget-source}


**说明:**

调整目标矩,改变其宽度,高度和位置,使其适合源矩区域内部,同时保持其原宽比.

与`FitOutside`函数不同,源区内部可能有一些空间没有覆盖.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 目标矩形以调整. |
| source | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 源矩以包围目标. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 修改的目标矩形实例 。


> 源码：[src/geom/rectangle/FitInside.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/FitInside.js#L9)  
引入版本：3.0.0


---

### FitOutside {#FitOutside}

#### \<static> FitOutside(target, source) {#static-fitoutsidetarget-source}


**说明:**

调整目标矩,改变其宽度,高度和位置,使其完全覆盖源矩的区域,同时保持其原宽比.

与`FitInside`函数不同,目标矩形可能比源头更远的延伸.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 目标矩形以调整. |
| source | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 源矩形可以将目标包入. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 修改的目标矩形实例 。


> 源码：[src/geom/rectangle/FitOutside.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/FitOutside.js#L9)  
引入版本：3.0.0


---

### Floor {#Floor}

#### \<static> Floor(rect) {#static-floorrect}


**说明:**

向下(地板)圆,向下(底),向下(底),向下(底),向下(底),向下),向下(底),向下(底),向下),向下(底),向下(底),向下),向下(底),向下(底),向下),向下(底),向下),向下(底),向下(底),向下),向下(底),向下(底),向下(底),向下),向下(底),向下(底),向下(底),向下(底),向下(底),向下(底),向下(底),向下(底),向下(底),向下(底),向下(底),向下,向下(底),向下(底),向下,向下),向下(底,向下),向下(底),向上),向上(底),向下(底),向下),(底,向上(底),向下),(底),(底,(底),向下),向下(底,向下),向下(底(底),(底),向下),向下),(底,(底,(底,(底),(底),(底),(底),(底,(底),(底),(底)/底),(底),(底),(底(底)和(底),(底),(底),(底),向上),(底),(底),(底),(底),(底),向(底),(底),(底),(底),(底),(底),(底),(底),(底),(底),

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 左上方的X和Y坐标 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 坐标为底座的矩形传递到此函数上。


> 源码：[src/geom/rectangle/Floor.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Floor.js#L7)  
引入版本：3.0.0


---

### FloorAll {#FloorAll}

#### \<static> FloorAll(rect) {#static-floorallrect}


**说明:**

圆矩形的位置和大小下至最大整数小于或等于每个电流坐标或维度。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形要调整. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 调整后的矩形.


> 源码：[src/geom/rectangle/FloorAll.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/FloorAll.js#L7)  
引入版本：3.0.0


---

### FromPoints {#FromPoints}

#### \<static> FromPoints(points, [out]) {#static-frompointspoints-out}


**说明:**

构造新的矩形或重新定位并调整现有矩形的大小,以便所有给定的点都位于或在其界限之内。

`points`参数是类似点的天体阵列:

```js
const points = [
    [100, 200],
    [200, 400],
    { x: 30, y: 60 }
]
```

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| points | array | 否 | 由矩形环绕的点阵(既包括两个与X和Y坐标相对应的元素的阵列,也包括一个具有公共`x`和`y`属性的物体)。 |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 可选矩形以调整 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 调整后的 `out`矩形,或者如果没有提供新的矩形。


> 源码：[src/geom/rectangle/FromPoints.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/FromPoints.js#L10)  
引入版本：3.0.0


---

### FromXY {#FromXY}

#### \<static> FromXY(x1, y1, x2, y2, [out]) {#static-fromxyx1-y1-x2-y2-out}


**说明:**

创建最小的矩形, 包含两个坐标对 。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x1 | number | 否 | 第一点的X坐标. |
| y1 | number | 否 | 初点的Y坐标 |
| x2 | number | 否 | 第二点的X坐标. |
| y2 | number | 否 | 第二点的Y坐标. |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 可选矩形以调整 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 调整后的 `out`矩形,或者如果没有提供新的矩形。


> 源码：[src/geom/rectangle/FromXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/FromXY.js#L9)  
引入版本：3.23.0


---

### GetAspectRatio {#GetAspectRatio}

#### \<static> GetAspectRatio(rect) {#static-getaspectratiorect}


**说明:**

计算矩形的宽度/ 高比。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 长方形. |


**返回值:** number - 矩形的宽度/ 高度比 。


> 源码：[src/geom/rectangle/GetAspectRatio.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/GetAspectRatio.js#L7)  
引入版本：3.0.0


---

### GetCenter {#GetCenter}

#### \<static> GetCenter(rect, [out]) {#static-getcenterrect-out}


**说明:**

返回矩形中心作为点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形以获得中心. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 可选矢量2对象,可使用中心坐标进行更新. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 修改后的 `out` 对象,或者如果没有提供新的矢量2。


> 源码：[src/geom/rectangle/GetCenter.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/GetCenter.js#L9)  
引入版本：3.0.0


---

### getLineA {#getLineA}

#### \<instance> getLineA([line]) {#instance-getlinealine}


**说明:**

返回一个对应此矩形顶部的行对象。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 是 | 一个设置结果的行对象。 如果 `undefined` 将创建新行 。 |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 与此矩形顶端相对应的直线对象。


> 源码：[src/geom/rectangle/Rectangle.js#L264](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L264)  
引入版本：3.0.0


---

### getLineB {#getLineB}

#### \<instance> getLineB([line]) {#instance-getlinebline}


**说明:**

返回与矩形右侧相对应的行对象。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 是 | 一个设置结果的行对象。 如果 `undefined` 将创建新行 。 |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 与此矩形右侧相对应的直线对象。


> 源码：[src/geom/rectangle/Rectangle.js#L285](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L285)  
引入版本：3.0.0


---

### getLineC {#getLineC}

#### \<instance> getLineC([line]) {#instance-getlinecline}


**说明:**

返回一个与矩形下方相对应的行对象。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 是 | 一个设置结果的行对象。 如果 `undefined` 将创建新行 。 |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 与此矩形下方对应的直线对象。


> 源码：[src/geom/rectangle/Rectangle.js#L306](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L306)  
引入版本：3.0.0


---

### getLineD {#getLineD}

#### \<instance> getLineD([line]) {#instance-getlinedline}


**说明:**

返回与矩形左侧对应的行对象。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| line | [Phaser.Geom.Line](/api/class/geom-line) | 是 | 一个设置结果的行对象。 如果 `undefined` 将创建新行 。 |


**返回值:** [Phaser.Geom.Line](/api/class/geom-line) - 与此矩形左侧相对应的直线对象。


> 源码：[src/geom/rectangle/Rectangle.js#L327](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L327)  
引入版本：3.0.0


---

### getPoint {#getPoint}

#### \<instance> getPoint(position, [output]) {#instance-getpointposition-output}


**说明:**

计算矩形周边某个特定`position`的点的坐标。

`position`是0到1之间的一个分数,它定义了该点的周界有多远.

0或1值返回矩形左上角的点,0.5值返回矩形右下角的点。0至0.5值位于上方或右侧,0.5至1值位于下方或左侧。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| position | number | 否 | 正常的距离进入矩形的周界返回. |
| output | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于更新点坐标的`x`和`y`的矢量2实例。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 更新后的 `output` 对象,或者如果没有给出 `output` 对象,则会给新的矢量2 。


> 源码：[src/geom/rectangle/Rectangle.js#L115](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L115)  
引入版本：3.0.0


---

### GetPoint {#GetPoint}

#### \<static> GetPoint(rectangle, position, [out]) {#static-getpointrectangle-position-out}


**说明:**

计算矩形周边某个特定`position`的点的坐标。

`position`是0到1之间的一个分数,它定义了该点的周界有多远.

0或1值返回矩形左上角的点,0.5值返回矩形右下角的点。0至0.5值位于上方或右侧,0.5至1值位于下方或左侧。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectangle | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形以获得周边点. |
| position | number | 否 | 正常的距离进入矩形的周界返回. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 使用点的`x`和`y`坐标更新的矢量2对象. |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 更新后的 `out` 对象,或者如果没有给出 `out` 对象,则会给新的矢量2 。


> 源码：[src/geom/rectangle/GetPoint.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/GetPoint.js#L10)  
引入版本：3.0.0


---

### getPoints {#getPoints}

#### \<instance> getPoints(quantity, [stepRate], [output]) {#instance-getpointsquantity-steprate-output}


**说明:**

从矩形的周界返回一系列点,每个点根据所需数量或步骤而间隔。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| quantity | number | 否 | 返回点数。 设定为 `false` 或 0 返回任意点数( `perimeter / stepRate`) , 以 `stepRate` 为基础, 将矩形周围的点数平匀地间隔 。 |
| stepRate | number | 是 | 如果 `quantity` 是 0, 确定每个返回点之间的正常距离 。 |
| output | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 附加点的数组。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 修改后的 `output` 阵列, 或者如果没有提供新的阵列。


> 源码：[src/geom/rectangle/Rectangle.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L137)  
引入版本：3.0.0


---

### GetPoints {#GetPoints}

#### \<static> GetPoints(rectangle, quantity, stepRate, [out]) {#static-getpointsrectangle-quantity-steprate-out}


**说明:**

从矩形的周长返回一个矢量2的数组点,每个点根据所需数量或步骤而间隔.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectangle | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形对象以获取点数 。 |
| quantity | number | 否 | 从矩形的周界返回的均匀间隔点数。 如果有假, 则使用 stepRate 参数来计算点数 。 |
| stepRate | number | 否 | 点间步骤。 用于计算数量不实时返回的点数。 如果数量为正数, 则忽略 。 |
| out | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 将点数存储到的可选数组 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 矩形周边的一阵矢量2点.


> 源码：[src/geom/rectangle/GetPoints.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/GetPoints.js#L10)  
引入版本：3.0.0


---

### getRandomPoint {#getRandomPoint}

#### \<instance> getRandomPoint([vec]) {#instance-getrandompointvec}


**说明:**

返回矩形界限内的随机点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 存储点坐标的 `x`和 `y` 的天体 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 更新的`vec`, 或如果没有提供新的矢量2。


> 源码：[src/geom/rectangle/Rectangle.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L156)  
引入版本：3.0.0


---

### GetSize {#GetSize}

#### \<static> GetSize(rect, [out]) {#static-getsizerect-out}


**说明:**

返回矩形的大小, 以矢量2 对象表示。 以 `width` 的值为 `x` 属性, 以 `height` 属性为 `y` 属性。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形以获得大小. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 矢量2 对象将大小存储在其中。 如果不给定, 则创建新的矢量2 实例 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - `x`持有宽度,`y`持有矩形高度的矢量2物体.


> 源码：[src/geom/rectangle/GetSize.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/GetSize.js#L9)  
引入版本：3.0.0


---

### Inflate {#Inflate}

#### \<static> Inflate(rect, x, y) {#static-inflaterect-x-y}


**说明:**

将矩形的大小增加指定数量。

矩形的中心保持不变,金额被加到两侧,所以实际的宽度或高度的增加比相应的参数大2倍.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 长方形以充气. |
| x | number | 否 | 左侧和右侧应水平移动多少像素. |
| y | number | 否 | 上下两侧应垂直移动多少像素. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 充气矩形的圆柱形.


> 源码：[src/geom/rectangle/Inflate.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Inflate.js#L9)  
引入版本：3.0.0


---

### Intersection {#Intersection}

#### \<static> Intersection(rectA, rectB, [out]) {#static-intersectionrecta-rectb-out}


**说明:**

需要两个矩形并首先检查它们是否交叉。 如果它们相交, 则返回`out`矩形中的交叉区域。 如果它们不相交, `out`矩形的宽度和高度为0 。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectA | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 最早的矩形从路口得到. |
| rectB | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第二矩形从中取出交汇点. |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 用于存储交叉结果的矩形 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 交叉结果。 如果宽度和高度为零, 则没有发生交叉 。


> 源码：[src/geom/rectangle/Intersection.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Intersection.js#L10)  
引入版本：3.11.0


---

### isEmpty {#isEmpty}

#### \<instance> isEmpty() {#instance-isempty}


**说明:**

确定矩形是否为空。如果矩形的宽度或高度小于或等于0,则为空。


**返回值:** boolean - `true` 如果矩形是空的,否则 `false`.


> 源码：[src/geom/rectangle/Rectangle.js#L251](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L251)  
引入版本：3.0.0


---

### MarchingAnts {#MarchingAnts}

#### \<static> MarchingAnts(rect, [step], [quantity], [out]) {#static-marchingantsrect-step-quantity-out}


**说明:**

返回矩形周边平均分布的矢量2点数组。这通常用来创建“总体蚂蚁”选择效果,即返回的点用来激活一个表面在矩形边缘行进的破折的轮廓。

您可以通过提供每个点之间的像素`step`距离来控制点间距, 或者指定在全周周周周平均分布点的`quantity`。 如果省略了两者, 则返回空阵列。 如果提供了`step`, `quantity` 则从周周长中导出, 由该步位除以。 如果只提供了 `quantity`, 则取而代之 。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形以获得周边点. |
| step | number | 是 | 周界每个点之间的距离。 如果您想要使用 `quantity` 参数, 请设定为 `null` 。 |
| quantity | number | 是 | 返回的点数总数。然后,该步骤根据矩形的长度计算,除以此值。 |
| out | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 是 | 将存储周边点的数组。 如果不给出, 则创建新的数组实例 。 |


**返回值:** Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> - 包含矩形周边点的阵列。


> 源码：[src/geom/rectangle/MarchingAnts.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/MarchingAnts.js#L10)  
引入版本：3.0.0


---

### MergePoints {#MergePoints}

#### \<static> MergePoints(target, points) {#static-mergepointstarget-points}


**说明:**

将矩形与点列表合并,重新定位和/或重新调整大小,使所有点都位于其界限或界限内。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形,应该合并。 |
| points | Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> | 否 | 向量2 对象的阵列,应该与矩形合并。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 修改后的矩形.


> 源码：[src/geom/rectangle/MergePoints.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/MergePoints.js#L7)  
引入版本：3.0.0


---

### MergeRect {#MergeRect}

#### \<static> MergeRect(target, source) {#static-mergerecttarget-source}


**说明:**

将源矩合并到目标矩形中并返回目标。两个矩形都不应该有负宽度或高度。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 目标矩形。 将修改以包含源矩形 。 |
| source | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 将合并为目标矩形的矩形 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 含有源矩的修改目标矩形.


> 源码：[src/geom/rectangle/MergeRect.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/MergeRect.js#L7)  
引入版本：3.0.0


---

### MergeXY {#MergeXY}

#### \<static> MergeXY(target, x, y) {#static-mergexytarget-x-y}


**说明:**

通过重新定位和/或重新调整大小将矩形与点合并,使点处于或在其界限内。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形,应该合并和修改。 |
| x | number | 否 | 合并点的X坐标。 |
| y | number | 否 | 合并点的Y坐标。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 修改后的`target`矩形.


> 源码：[src/geom/rectangle/MergeXY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/MergeXY.js#L7)  
引入版本：3.0.0


---

### Offset {#Offset}

#### \<static> Offset(rect, x, y) {#static-offsetrect-x-y}


**说明:**

以给定的横向和纵向数量翻译一个矩形,在保留其大小的同时移动其位置。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形要调整. |
| x | number | 否 | 水平移动矩形的距离 。 |
| y | number | 否 | 垂直移动矩形的距离 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 调整后的矩形.


> 源码：[src/geom/rectangle/Offset.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Offset.js#L7)  
引入版本：3.0.0


---

### OffsetPoint {#OffsetPoint}

#### \<static> OffsetPoint(rect, vec) {#static-offsetpointrect-vec}


**说明:**

用翻译向量的坐标翻译矩形左上角。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形要调整. |
| vec | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 坐标应用作抵消的矢量2点。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 调整后的矩形.


> 源码：[src/geom/rectangle/OffsetPoint.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/OffsetPoint.js#L7)  
引入版本：3.0.0


---

### Overlaps {#Overlaps}

#### \<static> Overlaps(rectA, rectB) {#static-overlapsrecta-rectb}


**说明:**

检查两个矩形重叠。 如果一个矩形在另一个矩形内, 两者将被视为重叠。 因此, 矩形被视作“ 固体 ” 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectA | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 首座矩形检查. |
| rectB | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第二矩形来验. |


**返回值:** boolean - `true` 如果两个矩形重叠, `false` 否则。


> 源码：[src/geom/rectangle/Overlaps.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Overlaps.js#L7)  
引入版本：3.0.0


---

### Perimeter {#Perimeter}

#### \<static> Perimeter(rect) {#static-perimeterrect}


**说明:**

计算矩形的周界。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形来用. |


**返回值:** number - 矩形的周长,等于`(width * 2) + (height * 2)`.


> 源码：[src/geom/rectangle/Perimeter.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Perimeter.js#L7)  
引入版本：3.0.0


---

### PerimeterPoint {#PerimeterPoint}

#### \<static> PerimeterPoint(rectangle, angle, [out]) {#static-perimeterpointrectangle-angle-out}


**说明:**

返回一个点,从矩形的周界,以给定角度为基础,从矩形的中心以度数测量。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectangle | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形以获得周边点. |
| angle | number | 否 | 点角,以度计. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 矢量2 对象将位置存储在其中。 如果不给定, 则创建新的矢量2 实例 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 位于矩形周长的矢量2物体,持有点坐标.


> 源码：[src/geom/rectangle/PerimeterPoint.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/PerimeterPoint.js#L10)  
引入版本：3.0.0


---

### Random {#Random}

#### \<static> Random(rect, out) {#static-randomrect-out}


**说明:**

返回矩形内的随机点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 矩形从这里返回一点. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 | 以点坐标更新的对象 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 修改后的 `out` 对象,或者如果未提供新的点。


> 源码：[src/geom/rectangle/Random.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Random.js#L9)  
引入版本：3.0.0


---

### RandomOutside {#RandomOutside}

#### \<static> RandomOutside(outer, inner, [out]) {#static-randomoutsideouter-inner-out}


**说明:**

计算位于 `outer` 矩形,但外侧 `inner` 矩形。 内矩形必须完全包含在外矩形内才能产生点。 如果 `inner` 尚未完全纳入 `outer`,函数返回 `out` 矢量不变。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| outer | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 外矩形以获得内部的随机点. |
| inner | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 内矩形以排除返回点。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 一个用于存储结果的矢量2对象。 如果未指定, 将会创建一个新的矢量2 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 一个矢量2对象,含有其`x`和`y`属性中的随机值.


> 源码：[src/geom/rectangle/RandomOutside.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/RandomOutside.js#L11)  
引入版本：3.10.0


---

### SameDimensions {#SameDimensions}

#### \<static> SameDimensions(rect, toCompare) {#static-samedimensionsrect-tocompare}


**说明:**

确定两个对象(矩形或类似矩形)在严格平等的情况下是否具有相同的宽度和高度值.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第一个矩形物体. |
| toCompare | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第二矩形物体. |


**返回值:** boolean - `true` 如果对象具有等值,则 `width` 财务报告和已审计财务报表 `height` 属性,否则 `false`.


> 源码：[src/geom/rectangle/SameDimensions.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/SameDimensions.js#L7)  
引入版本：3.15.0


---

### Scale {#Scale}

#### \<static> Scale(rect, x, y) {#static-scalerect-x-y}


**说明:**

以给定的因子缩放给定的矩形的宽度和高度。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rect | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 将缩放到指定数量中的 `Rectangle` 对象 。 |
| x | number | 否 | 水平地缩放矩形的因子 。 |
| y | number | 否 | 垂直缩放矩形的因子。如果不指定,则矩形将按双向的因子`x`缩放。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 矩形对象,其特性为更新后的`width`和`height`,由缩放系数计算.


> 源码：[src/geom/rectangle/Scale.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Scale.js#L7)  
引入版本：3.0.0


---

### setEmpty {#setEmpty}

#### \<instance> setEmpty() {#instance-setempty}


**说明:**

将矩形的位置、宽度和高度重新调整为 0。


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 此矩形对象 。


> 源码：[src/geom/rectangle/Rectangle.js#L196](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L196)  
引入版本：3.0.0


---

### setPosition {#setPosition}

#### \<instance> setPosition(x, [y]) {#instance-setpositionx-y}


**说明:**

设置矩形的位置。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 矩形左上角的X坐标. |
| y | number | 是 | "x" | 矩形左上角的Y坐标. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 此矩形对象 。


> 源码：[src/geom/rectangle/Rectangle.js#L209](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L209)  
引入版本：3.0.0


---

### setSize {#setSize}

#### \<instance> setSize(width, [height]) {#instance-setsizewidth-height}


**说明:**

设置矩形的宽度和高度。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 否 |  | 设置矩形的宽度 。 |
| height | number | 是 | "width" | 设置矩形的高度 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 此矩形对象 。


> 源码：[src/geom/rectangle/Rectangle.js#L230](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L230)  
引入版本：3.0.0


---

### setTo {#setTo}

#### \<instance> setTo(x, y, width, height) {#instance-settox-y-width-height}


**说明:**

设置矩形的位置、宽度和高度。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 矩形左上角的X坐标. |
| y | number | 否 | 矩形左上角的Y坐标. |
| width | number | 否 | 矩形的宽度 。 |
| height | number | 否 | 矩形的高度. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 此矩形对象 。


> 源码：[src/geom/rectangle/Rectangle.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L173)  
引入版本：3.0.0


---

### Union {#Union}

#### \<static> Union(rectA, rectB, [out]) {#static-unionrecta-rectb-out}


**说明:**

创建新的矩形或重新定位和/或调整已有矩形的大小,使其包含两个给定的矩形,即计算它们的结合。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rectA | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 最早使用的矩形. |
| rectB | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 否 | 第二矩形用. |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 将工会存放在矩形的. |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 修改后的 `out` 矩形,或者如果没有提供新的矩形。


> 源码：[src/geom/rectangle/Union.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Union.js#L9)  
引入版本：3.0.0


---

## 公开成员 {#public-members}

### bottom {#bottom}

#### bottom: number {#bottom-number}


**说明:**

y 和高度属性的总和。 改变矩形对象的底部属性对x、y 和宽度属性没有影响, 但确实改变高度属性。


> 源码：[src/geom/rectangle/Rectangle.js#L439](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L439)  
引入版本：3.0.0


---

### centerX {#centerX}

#### centerX: number {#centerx-number}


**说明:**

矩形中心部的x坐标.


> 源码：[src/geom/rectangle/Rectangle.js#L468](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L468)  
引入版本：3.0.0


---

### centerY {#centerY}

#### centerY: number {#centery-number}


**说明:**

矩形中心y坐标.


> 源码：[src/geom/rectangle/Rectangle.js#L489](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L489)  
引入版本：3.0.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

矩形的高度,即其上侧(由`y`定义)与下侧的距离.


> 源码：[src/geom/rectangle/Rectangle.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L88)  
引入版本：3.0.0


---

### left {#left}

#### left: number {#left-number}


**说明:**

矩形左侧的 x 坐标。 改变矩形对象的左侧属性对y 和高度属性没有影响。 但是它确实影响宽度属性, 而改变 x 值不影响宽度属性 。


> 源码：[src/geom/rectangle/Rectangle.js#L348](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L348)  
引入版本：3.0.0


---

### right {#right}

#### right: number {#right-number}


**说明:**

x 和宽度属性的总和。 改变矩形对象的右属性对x, y 和高度属性没有影响, 但是它确实影响宽度属性 。


> 源码：[src/geom/rectangle/Rectangle.js#L379](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L379)  
引入版本：3.0.0


---

### top {#top}

#### top: number {#top-number}


**说明:**

矩形顶部的y坐标。 改变矩形对象的顶端属性对x和宽度属性没有影响。 但是它确实影响高度属性, 而改变y值不影响高度属性 。


> 源码：[src/geom/rectangle/Rectangle.js#L408](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L408)  
引入版本：3.0.0


---

### type {#type}

#### type: number {#type-number}


**说明:**

此对象的几何常数类型: `GEOM_CONST.RECTANGLE`. 用于快速类型比较.


> 源码：[src/geom/rectangle/Rectangle.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L47)  
引入版本：3.19.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

矩形的宽度,即它的左侧(由`x`定义)与它的右侧之间的距离.


> 源码：[src/geom/rectangle/Rectangle.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L78)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

矩形左上角的X坐标.


> 源码：[src/geom/rectangle/Rectangle.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L58)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

矩形左上角的Y坐标.


> 源码：[src/geom/rectangle/Rectangle.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/geom/rectangle/Rectangle.js#L68)  
引入版本：3.0.0


---

---
