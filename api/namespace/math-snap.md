# Phaser.Math.Snap {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math-snap)

Scope: 
static
> 源码：[src/math/snap/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/snap/index.js#L7)  


## 静态函数 {#static-functions}

### Ceil {#Ceil}

#### \<static> Ceil(value, gap, [start], [divide]) {#static-ceilvalue-gap-start-divide}


**说明:**

使用 ceil 来将一个值与最近的网格切片相匹配 。

示例:如果间隔间距间距为 `5` 和职位 `12`...你会很快地 `15`。 。 。 。 `14` 转弯到 `15`. 不过... `16` 将会迅速 `20`.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 价值来扣 |
| gap | number | 否 |  | 网格的间隔间隙 。 |
| start | number | 是 | 0 | 可选起始数冲抵缺口。 |
| divide | boolean | 是 | false | 如果 `true` 返回前, 它会将断裂值除以空隙 。 |


**返回值:** number - 崩溃的值。


> 源码：[src/math/snap/SnapCeil.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/snap/SnapCeil.js#L7)  
引入版本：3.0.0


---

### Floor {#Floor}

#### \<static> Floor(value, gap, [start], [divide]) {#static-floorvalue-gap-start-divide}


**说明:**

使用地板将一个值与最近的下网格切片对齐。

示例:如果间隔间距间距为 `5` 和职位 `12`...你会很快地 `10`。 。 。 。 `14` 转弯到 `10`. 不过... `16` 将会迅速 `15`.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 价值来扣 |
| gap | number | 否 |  | 网格的间隔间隙 。 |
| start | number | 是 | 0 | 可选起始数冲抵缺口。 |
| divide | boolean | 是 | false | 如果 `true` 返回前, 它会将断裂值除以空隙 。 |


**返回值:** number - 崩溃的值。


> 源码：[src/math/snap/SnapFloor.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/snap/SnapFloor.js#L7)  
引入版本：3.0.0


---

### To {#To}

#### \<static> To(value, gap, [start], [divide]) {#static-tovalue-gap-start-divide}


**说明:**

使用四舍五入来将一个值与最近的网格切片相匹配。在两个切片之间完全落到一半的值会向更高的切片相匹配。

示例:如果间隔间距间距为 `5` 和职位 `12`...你会很快地 `10` 却 `14` 将会迅速 `15`.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 价值来扣 |
| gap | number | 否 |  | 网格的间隔间隙 。 |
| start | number | 是 | 0 | 可选起始值为网格抵消,允许网格对齐开始值为零以外的值. |
| divide | boolean | 是 | false | 如果 `true` 返回前, 它会将断裂值除以空隙 。 |


**返回值:** number - 崩溃的值。


> 源码：[src/math/snap/SnapTo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/snap/SnapTo.js#L7)  
引入版本：3.0.0


---

---
