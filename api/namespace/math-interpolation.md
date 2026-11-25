# Phaser.Math.Interpolation {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-interpolation)

Scope: 
static
> 源码：[src/math/interpolation/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/index.js#L7)  


## 静态函数 {#static-functions}

### Bezier {#Bezier}

#### \<static> Bezier(v, k) {#static-bezierv-k}


**说明:**

执行一个通用的贝塞尔插值, 覆盖任意数控制点。 `v` 阵列提供了控制点值, `k`( 0 至 1) 确定了曲线上的位置。 与使用精确4 点的 CubicBezier 刑警组织不同, 它支持任意数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | Array.\<number> | 否 | 输入值阵列, 以插入值之间 。 |
| k | number | 否 | 插值的百分比,在0到1之间. |


**返回值:** number - 内插值.


> 源码：[src/math/interpolation/BezierInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/BezierInterpolation.js#L9)  
引入版本：3.0.0


---

### CatmullRom {#CatmullRom}

#### \<static> CatmullRom(v, k) {#static-catmullromv-k}


**说明:**

在一个数值阵列上执行 Catmull-Rom 线性插值,产生一个平滑曲线,通过每个控制点。 `k`参数(0至1) 确定整个曲线的位置。

如果`v`中的第一和最后一个值相等,则曲线被视作闭合(rooping),插值被无缝地包裹起来。否则曲线被视作开阔,而0至1范围以外的`k`值将推导出终点之外。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | Array.\<number> | 否 | 用于插入控制点值的输入数组。 |
| k | number | 否 | 插值的百分比,介于0到1之间,在这个范围以外的数值在开阔曲线上推算,或者在闭合曲线上包扎. |


**返回值:** number - 内插值.


> 源码：[src/math/interpolation/CatmullRomInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/CatmullRomInterpolation.js#L9)  
引入版本：3.0.0


---

### CubicBezier {#CubicBezier}

#### \<static> CubicBezier(t, p0, p1, p2, p3) {#static-cubicbeziert-p0-p1-p2-p3}


**说明:**

计算给定参数的立方贝塞尔插值 `t`,基于四个控制点。曲线通过 `p0` 时 `t=0` 财务报告和已审计财务报表 `p3` 时 `t=1`时 `p1` 财务报告和已审计财务报表 `p2` 充当拉点,在不必然出现在这些终点之间塑造曲线。这使得立方贝塞尔插值非常适合动画、相机路径和程序运动中平滑、艺术引导的转换。

[https://medium.com/@adrian_cooney/bezier-interpolation-13b68563313a](https://medium.com/@adrian_cooney/bezier-interpolation-13b68563313a)

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 插值的百分比,在0到1之间. |
| p0 | number | 否 | 始发点. |
| p1 | number | 否 | 初总控点. |
| p2 | number | 否 | 第二控制点. |
| p3 | number | 否 | 终处. |


**返回值:** number - 内插值.


> 源码：[src/math/interpolation/CubicBezierInterpolation.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/CubicBezierInterpolation.js#L43)  
引入版本：3.0.0


---

### Linear {#Linear}

#### \<static> Linear(v, k) {#static-linearv-k}


**说明:**

进行一系列数值的线性插值。

鉴于`v`和进展因子`k`在0到1之间,此函数将`k`映射到数组沿边的位置,并返回两个最接近数组元素之间的线性插值。一个0的`k`返回第一个元素附近的值,而一个1的`k`返回最后一个元素附近的值。在0到1之间值的`k`被推导到数组的末尾。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| v | Array.\<number> | 否 | 输入值阵列, 以插入值之间 。 |
| k | number | 否 | 插值的百分比,在0到1之间. |


**返回值:** number - 内插值.


> 源码：[src/math/interpolation/LinearInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/LinearInterpolation.js#L9)  
引入版本：3.0.0


---

### QuadraticBezier {#QuadraticBezier}

#### \<static> QuadraticBezier(t, p0, p1, p2) {#static-quadraticbeziert-p0-p1-p2}


**说明:**

沿着一个起点、一个控制点和一个终点定义的四边形贝塞尔曲线计算一个单一点。 `t`的数值决定了返回值沿曲线的大小:0返回起始点值,1返回终点值,而中间的值是顺畅的插值。控制点将曲线拉向它,在起点和终点之间形成弧线,而不会直接穿过曲线。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 沿曲线的插值位置,介于 0(起始)至 1(结束)之间. |
| p0 | number | 否 | 起点值. |
| p1 | number | 否 | 控制点值,将曲线拉向它,决定它的弧. |
| p2 | number | 否 | 终点值. |


**返回值:** number - 沿四面体贝塞尔曲线的`t`位置的插值。


> 源码：[src/math/interpolation/QuadraticBezierInterpolation.js#L35](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/QuadraticBezierInterpolation.js#L35)  
引入版本：3.2.0


---

### SmootherStep {#SmootherStep}

#### \<static> SmootherStep(t, min, max) {#static-smootherstept-min-max}


**说明:**

基于肯·佩林的平滑步态函数的插值法,它是标准平滑步态曲线的改进变体. 平滑步态不同于平滑步态,平滑步态在终点有0个首辅衍生物,平滑步态还在终点有0个次辅衍生物,导致`min`和`max`之间更平滑的S曲线过渡. 使用此方法时需要特别流畅的松动,在过渡开始或结束时没有可视加速或减速的文物.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 插值的百分比,在0到1之间. |
| min | number | 否 | 最小值,又称"左边",假定比"右边"小. |
| max | number | 否 | 最大值,又称"右边缘",假定值大于"左边缘". |


**返回值:** number - 内插值.


> 源码：[src/math/interpolation/SmootherStepInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/SmootherStepInterpolation.js#L9)  
引入版本：3.9.0


---

### SmoothStep {#SmoothStep}

#### \<static> SmoothStep(t, min, max) {#static-smoothstept-min-max}


**说明:**

平滑步态插值法,它利用平滑步态函数在`min`和`max`值之间产生平滑的,S形的过渡。与线性插值不同,平滑步态在两边都容易进出,导致过渡的逐渐开始和结束。这使得它非常适合动画和过渡,因为边界的突然变化看起来是不自然的。

插值参数 `t` 首先是通过平滑步曲线重新映射(它夹住并应用立方赫米特函数),然后使用结果线性插到 `min` 财务报告和已审计财务报表 `max`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 插值的百分比,在0到1之间. |
| min | number | 否 | 最小值,又称"左边",假定比"右边"小. |
| max | number | 否 | 最大值,又称"右边缘",假定值大于"左边缘". |


**返回值:** number - 内插值.


> 源码：[src/math/interpolation/SmoothStepInterpolation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/interpolation/SmoothStepInterpolation.js#L9)  
引入版本：3.9.0


---

---
