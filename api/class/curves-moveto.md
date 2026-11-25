# MoveTo {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/curves-moveto)

一个 MoveTo Curve 是一个由单个点组成的特殊曲线类型。它与其他曲线类型不同,它不画任何东西——它只是重新定位一个`Path`的当前端点,类似于SVG `moveto`命令。在`Phaser.Curves.Path`内部使用它来在两个子路径之间产生一个缺口,或者开始从新位置绘制,而不连接到以前的曲线。

**构造函数**

`new MoveTo([x], [y])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | `x`像素坐标. |
| y | number | 是 | 0 | `y`像素坐标. |

---


**作用域**: static

> 源码：[src/curves/path/MoveTo.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/MoveTo.js#L10)  
引入版本：3.0.0

## 公开成员 {#public-members}

### active {#active}

#### active: boolean {#active-boolean}


**说明:**

表示此曲线不活动且不贡献其母路径的界限、长度或渲染的旗帜。 它总是对一个 MoveTo 的 `false`Z , 它标记为位置标记而不是可绘制的段 。


> 源码：[src/curves/path/MoveTo.js#L31](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/MoveTo.js#L31)  
引入版本：3.0.0


---

### p0 {#p0}

#### p0: [Phaser.Math.Vector2](/api/class/math-vector2) {#p0-phasermathvector2}


**说明:**

这个曲线构成的孤点.


> 源码：[src/curves/path/MoveTo.js#L41](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/MoveTo.js#L41)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### getLength {#getLength}

#### \<instance> getLength() {#instance-getlength}


**说明:**

获得此曲线的长度 。


**返回值:** number - 此曲线的长度。 对于“ 移动到” , 值总是 0 。


> 源码：[src/curves/path/MoveTo.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/MoveTo.js#L102)  
引入版本：3.0.0


---

### getPoint {#getPoint}

#### \<instance> getPoint(t, [out]) {#instance-getpointt-out}


**说明:**

返回此 MoveTo 曲线所代表的单一点。 因为 MoveTo 只有一个点, 其值为 `t` 被忽略,并且 `p0` 总是返回。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 沿曲线返回的位置。 0 开始和 1 结束。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储结果的矢量2 对象。 如果不给定, 将会创建 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 曲线上点的坐标。 如果给定了 `out` 对象, 将会返回 。


> 源码：[src/curves/path/MoveTo.js#L51](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/MoveTo.js#L51)  
引入版本：3.0.0


---

### getPointAt {#getPointAt}

#### \<instance> getPointAt(u, [out]) {#instance-getpointatu-out}


**说明:**

获取曲线中指定位置的点。 这将总是返回此曲线的唯一点 。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| u | number | 否 | 检索路径中的位置, 0 至 1 之间, 未使用 。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 存储点的可选矢量 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 修改后的`out`向量,或者如果没有提供新的`Vector2`。


> 源码：[src/curves/path/MoveTo.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/MoveTo.js#L71)  
引入版本：3.0.0


---

### getResolution {#getResolution}

#### \<instance> getResolution() {#instance-getresolution}


**说明:**

获得此曲线的分辨率。


**返回值:** number - 此曲线的分辨率。 对于“ 移动到” , 值总是 1 。


> 源码：[src/curves/path/MoveTo.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/MoveTo.js#L89)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

将这个曲线转换为可串行的 JSON 对象。


**返回值:** [Phaser.Types.Curves.JSONCurve](/api/typedef/types-curves#jsoncurve) - 具有曲线类型和唯一点的原始天体.


> 源码：[src/curves/path/MoveTo.js#L115](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/path/MoveTo.js#L115)  
引入版本：3.0.0


---

---
