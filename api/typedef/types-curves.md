# Types.Curves {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-curves)

## EllipseCurveConfig {#ellipsecurveconfig}

### \<static> EllipseCurveConfig {#static-ellipsecurveconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 椭圆形的x坐标. |
| y | number | 是 | 0 | 椭圆形的y坐标. |
| xRadius | number | 是 | 0 | 椭圆的横向半径. |
| yRadius | number | 是 | 0 | 椭圆的垂直半径. |
| startAngle | number | 是 | 0 | 椭圆的起始角,以度计. |
| endAngle | number | 是 | 360 | 椭圆的端角,以度计. |
| clockwise | boolean | 是 | false | 如果椭圆旋转是顺时针( 真实) 或逆时针( 假) 设置 |
| rotation | number | 是 | 0 | 椭圆的旋转,以度数表示. |

**类型**: object

**所属**: Phaser.Types.Curves
> 源码：[src/curves/typedefs/EllipseCurveConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/typedefs/EllipseCurveConfig.js#L1)  


---

## JSONCurve {#jsoncurve}

### \<static> JSONCurve {#static-jsoncurve}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 类型 | string | 否 | 曲线的类型 |
| points | Array.\<number> | 否 | 诸如 `[x1, y1, x2, y2]` 的点数组 |

**类型**: object

**所属**: Phaser.Types.Curves
> 源码：[src/curves/typedefs/JSONCurve.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/typedefs/JSONCurve.js#L1)  
引入版本：3.0.0

---

## JSONEllipseCurve {#jsonellipsecurve}

### \<static> JSONEllipseCurve {#static-jsonellipsecurve}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 类型 | string | 否 | 曲线的类型. |
| x | number | 否 | 椭圆形的x坐标. |
| y | number | 否 | 椭圆形的y坐标. |
| xRadius | number | 否 | 椭圆的横向半径. |
| yRadius | number | 否 | 椭圆的垂直半径. |
| startAngle | number | 否 | 椭圆的起始角,以度计. |
| endAngle | number | 否 | 椭圆的端角,以度计. |
| clockwise | boolean | 否 | 如果椭圆旋转是顺时针( 真实) 或逆时针( 假) 设置 |
| rotation | number | 否 | 椭圆旋转,以度计. |

**类型**: object

**所属**: Phaser.Types.Curves
> 源码：[src/curves/typedefs/JSONEllipseCurve.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/typedefs/JSONEllipseCurve.js#L1)  
引入版本：3.0.0

---

## JSONPath {#jsonpath}

### \<static> JSONPath {#static-jsonpath}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 类型 | string | 否 | 路径的类型. |
| x | number | 否 | 曲线起点的X坐标. |
| y | number | 否 | 路径起点的Y坐标. |
| autoClose | boolean | 否 | 路径是自动关闭的 。 |
| curves | Array.\<[Phaser.Types.Curves.JSONCurve](/api/typedef/types-curves#jsoncurve)> | 否 | 曲线列表 |

**类型**: object

**所属**: Phaser.Types.Curves
> 源码：[src/curves/typedefs/JSONPath.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/curves/typedefs/JSONPath.js#L1)  
引入版本：3.0.0

---

---
